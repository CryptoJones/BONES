#!/usr/bin/env python3
"""
Fetch EMS drug label data from FDA DailyMed (public domain, U.S. government).

DailyMed API: https://dailymed.nlm.nih.gov/dailymed/services/
All content is in the public domain per 17 U.S.C. § 105.
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"

DAILYMED_API = "https://dailymed.nlm.nih.gov/dailymed/services/v2"

# Core EMS formulary — standard prehospital drugs across most state protocols
EMS_DRUGS = [
    "epinephrine",
    "albuterol",
    "nitroglycerin",
    "naloxone",
    "aspirin",
    "adenosine",
    "amiodarone",
    "lidocaine",
    "atropine",
    "diphenhydramine",
    "glucagon",
    "dextrose",
    "furosemide",
    "morphine",
    "fentanyl",
    "midazolam",
    "diazepam",
    "lorazepam",
    "ondansetron",
    "metoprolol",
    "labetalol",
    "ketamine",
    "etomidate",
    "succinylcholine",
    "rocuronium",
    "vecuronium",
    "tranexamic acid",
    "magnesium sulfate",
    "sodium bicarbonate",
    "calcium gluconate",
    "calcium chloride",
    "activated charcoal",
    "dexamethasone",
    "methylprednisolone",
    "oxytocin",
    "terbutaline",
    "ipratropium",
    "dopamine",
    "norepinephrine",
    "vasopressin",
]


def search_drug(drug_name: str) -> list[dict]:
    params = urllib.parse.urlencode({"drug_name": drug_name, "pagesize": 5})
    url = f"{DAILYMED_API}/spls.json?{params}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.loads(resp.read())
    return data.get("data", [])


def fetch_label(set_id: str) -> dict | None:
    url = f"{DAILYMED_API}/spls/{set_id}.json"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def extract_sections(label_data: dict) -> dict:
    """Pull dosage and indication sections from a DailyMed label."""
    result = {"sections": {}}
    data = label_data.get("data", {})
    spl = data.get("spl", {})
    sections = spl.get("sections", [])
    target_codes = {
        "34068-7": "dosage_and_administration",
        "34067-9": "indications_and_usage",
        "34070-3": "contraindications",
        "34071-1": "warnings",
        "43685-7": "warnings_and_precautions",
        "34090-1": "clinical_pharmacology",
    }
    for section in sections:
        code = section.get("code", "")
        if code in target_codes:
            key = target_codes[code]
            text = section.get("text", "").strip()
            if text:
                result["sections"][key] = text[:4000]
    return result


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / "dailymed_ems_drugs.jsonl"
    total = 0
    seen_set_ids = set()

    with open(out_path, "w") as f:
        for drug in EMS_DRUGS:
            print(f"Fetching: {drug}")
            try:
                results = search_drug(drug)
                for r in results[:2]:
                    set_id = r.get("setid", "")
                    if not set_id or set_id in seen_set_ids:
                        continue
                    seen_set_ids.add(set_id)
                    label = fetch_label(set_id)
                    if not label:
                        continue
                    sections = extract_sections(label)
                    record = {
                        "drug_name": drug,
                        "set_id": set_id,
                        "title": r.get("title", ""),
                        "published": r.get("published_date", ""),
                        **sections,
                    }
                    if record["sections"]:
                        f.write(json.dumps(record, ensure_ascii=False) + "\n")
                        total += 1
                time.sleep(0.3)
            except Exception as e:
                print(f"  Error for {drug}: {e}", file=sys.stderr)

    print(f"\nWrote {total} drug records -> {out_path}")


if __name__ == "__main__":
    main()
