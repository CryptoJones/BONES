#!/usr/bin/env python3
"""
Fetch EMS-relevant data from NIH public APIs (public domain, U.S. government).

Sources:
- PubMed Central Open Access (PMC OA) full-text articles via NCBI E-utilities
- MedlinePlus Drug Information via REST API
- NLM RxNorm drug data

All content from U.S. government sources is in the public domain (17 U.S.C. § 105).
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
RXNORM = "https://rxnav.nlm.nih.gov/REST"

EMS_SEARCH_TERMS = [
    "prehospital emergency medical services protocol guideline",
    "paramedic out-of-hospital cardiac arrest resuscitation",
    "emergency medical technician airway management",
    "prehospital trauma hemorrhage control tourniquet",
    "naloxone opioid overdose prehospital reversal",
    "pediatric prehospital triage JumpSTART START",
    "anaphylaxis epinephrine prehospital emergency",
    "CPAP prehospital pulmonary edema congestive heart failure",
    "prehospital stroke recognition Cincinnati scale",
    "ketamine prehospital sedation analgesia",
    "tranexamic acid TXA prehospital trauma hemorrhage",
    "rapid sequence intubation prehospital paramedic",
    "prehospital spinal immobilization selective",
    "EMS mass casualty incident triage protocol",
    "prehospital pediatric dosing weight estimation Broselow",
    "prehospital sepsis early recognition treatment",
    "prehospital hypoglycemia dextrose glucagon",
    "prehospital burn assessment fluid resuscitation",
    "AEMT advanced EMT scope practice medications",
    "EMS protocol scope practice EMR EMT paramedic",
]

EMS_DRUGS_RXNORM = [
    "epinephrine", "albuterol", "nitroglycerin", "naloxone", "adenosine",
    "amiodarone", "lidocaine", "atropine", "diphenhydramine", "glucagon",
    "dextrose", "furosemide", "morphine", "fentanyl", "midazolam",
    "ketamine", "etomidate", "succinylcholine", "rocuronium",
    "tranexamic acid", "magnesium sulfate", "sodium bicarbonate",
    "ondansetron", "aspirin", "dopamine", "norepinephrine",
]


def pubmed_search(term: str, retmax: int = 30) -> list[str]:
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "term": term,
        "retmax": retmax,
        "retmode": "json",
        "datetype": "pdat",
        "mindate": "2010",
        "maxdate": "2025",
    })
    with urllib.request.urlopen(f"{EUTILS}/esearch.fcgi?{params}", timeout=30) as r:
        return json.loads(r.read()).get("esearchresult", {}).get("idlist", [])


def pubmed_abstracts(pmids: list[str]) -> list[dict]:
    if not pmids:
        return []
    params = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(pmids), "retmode": "json"})
    with urllib.request.urlopen(f"{EUTILS}/esummary.fcgi?{params}", timeout=30) as r:
        data = json.loads(r.read())
    out = []
    for pmid, art in data.get("result", {}).items():
        if pmid == "uids":
            continue
        title = art.get("title", "").strip()
        source = art.get("source", "").strip()
        authors = [a.get("name", "") for a in art.get("authors", [])[:3]]
        year = art.get("pubdate", "")[:4]
        if title:
            out.append({
                "pmid": pmid,
                "title": title,
                "source": source,
                "authors": authors,
                "year": year,
                "type": "pubmed_abstract",
            })
    return out


def rxnorm_drug_info(drug_name: str) -> dict | None:
    """Fetch RxNorm concept and drug class for a drug name."""
    params = urllib.parse.urlencode({"name": drug_name})
    try:
        with urllib.request.urlopen(f"{RXNORM}/rxcui.json?{params}", timeout=15) as r:
            data = json.loads(r.read())
        rxcui = data.get("idGroup", {}).get("rxnormId", [None])[0]
        if not rxcui:
            return None
        with urllib.request.urlopen(f"{RXNORM}/rxcui/{rxcui}/properties.json", timeout=15) as r:
            props = json.loads(r.read()).get("properties", {})
        return {
            "drug_name": drug_name,
            "rxcui": rxcui,
            "name": props.get("name", ""),
            "synonym": props.get("synonym", ""),
            "tty": props.get("tty", ""),
            "type": "rxnorm",
        }
    except Exception:
        return None


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    seen_pmids = set()

    # PubMed abstracts
    pubmed_out = RAW_DIR / "pubmed_ems_nih.jsonl"
    total_pubmed = 0
    with open(pubmed_out, "w") as f:
        for term in EMS_SEARCH_TERMS:
            print(f"PubMed: {term!r}")
            try:
                pmids = pubmed_search(term)
                new_pmids = [p for p in pmids if p not in seen_pmids]
                seen_pmids.update(new_pmids)
                articles = pubmed_abstracts(new_pmids)
                for art in articles:
                    f.write(json.dumps(art, ensure_ascii=False) + "\n")
                    total_pubmed += 1
                print(f"  +{len(articles)} articles")
                time.sleep(0.4)
            except Exception as e:
                print(f"  Error: {e}", file=sys.stderr)

    print(f"\nPubMed: {total_pubmed} articles -> {pubmed_out}")

    # RxNorm drug data
    rxnorm_out = RAW_DIR / "rxnorm_ems_drugs.jsonl"
    total_rx = 0
    with open(rxnorm_out, "w") as f:
        for drug in EMS_DRUGS_RXNORM:
            print(f"RxNorm: {drug}")
            info = rxnorm_drug_info(drug)
            if info:
                f.write(json.dumps(info, ensure_ascii=False) + "\n")
                total_rx += 1
            time.sleep(0.2)

    print(f"RxNorm: {total_rx} drug records -> {rxnorm_out}")


if __name__ == "__main__":
    main()
