#!/usr/bin/env python3
"""
Fetch EMS-relevant medical literature from PubMed Central and OpenMedSpel.

Data written to data/raw/ as JSONL.
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"

PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
PUBMED_SEARCH = f"{PUBMED_BASE}/esearch.fcgi"
PUBMED_FETCH = f"{PUBMED_BASE}/efetch.fcgi"
PUBMED_SUMMARY = f"{PUBMED_BASE}/esummary.fcgi"

EMS_QUERIES = [
    "emergency medical services prehospital protocol",
    "paramedic advanced life support cardiac arrest",
    "prehospital trauma hemorrhage control tourniquet",
    "pediatric emergency prehospital triage",
    "naloxone opioid overdose EMS",
    "CPAP prehospital pulmonary edema",
    "anaphylaxis epinephrine emergency",
    "stroke prehospital tPA time",
    "mass casualty incident triage START JumpSTART",
]


def pubmed_search(query: str, retmax: int = 50) -> list[str]:
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json",
        "usehistory": "n",
    })
    url = f"{PUBMED_SEARCH}?{params}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.loads(resp.read())
    return data.get("esearchresult", {}).get("idlist", [])


def pubmed_fetch_abstracts(pmids: list[str]) -> list[dict]:
    if not pmids:
        return []
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json",
        "rettype": "abstract",
    })
    url = f"{PUBMED_SUMMARY}?{params}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.loads(resp.read())

    results = []
    for pmid, article in data.get("result", {}).items():
        if pmid == "uids":
            continue
        title = article.get("title", "").strip()
        source = article.get("source", "").strip()
        pubdate = article.get("pubdate", "").strip()
        if title:
            results.append({
                "pmid": pmid,
                "title": title,
                "source": source,
                "pubdate": pubdate,
            })
    return results


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / "pubmed_ems.jsonl"
    seen = set()
    total = 0

    with open(out_path, "w") as f:
        for query in EMS_QUERIES:
            print(f"Searching PubMed: {query!r}")
            try:
                pmids = pubmed_search(query, retmax=50)
                print(f"  Found {len(pmids)} PMIDs")
                articles = pubmed_fetch_abstracts(pmids)
                for art in articles:
                    if art["pmid"] not in seen:
                        seen.add(art["pmid"])
                        f.write(json.dumps(art, ensure_ascii=False) + "\n")
                        total += 1
                time.sleep(0.5)
            except Exception as e:
                print(f"  Error: {e}", file=sys.stderr)

    print(f"\nTotal articles written: {total} -> {out_path}")


if __name__ == "__main__":
    main()
