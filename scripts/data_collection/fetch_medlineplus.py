#!/usr/bin/env python3
"""
Fetch EMS-relevant health topic data from MedlinePlus (NIH, public domain).

MedlinePlus Connect API: https://medlineplus.gov/connect/service.html
Content is produced by the U.S. National Library of Medicine — public domain.
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"

MEDLINEPLUS_API = "https://connect.medlineplus.gov/service"

# ICD-10 codes for core EMS presentations
EMS_ICD10_CODES = [
    ("I46.9",  "Cardiac arrest, unspecified"),
    ("I21.9",  "Acute myocardial infarction, unspecified"),
    ("I50.9",  "Heart failure, unspecified"),
    ("I63.9",  "Cerebral infarction, unspecified"),
    ("I61.9",  "Intracerebral hemorrhage, unspecified"),
    ("J96.00", "Acute respiratory failure, unspecified"),
    ("J18.9",  "Pneumonia, unspecified organism"),
    ("J45.901","Unspecified asthma with (acute) exacerbation"),
    ("J44.1",  "COPD with acute exacerbation"),
    ("R57.9",  "Shock, unspecified"),
    ("T40.1X1","Poisoning by heroin, accidental"),
    ("T39.1X1","Poisoning by 4-Aminophenol derivatives, accidental"),
    ("T65.91", "Toxic effects of unspecified substance"),
    ("S06.9X9","Unspecified intracranial injury"),
    ("S72.001","Fracture of unspecified part of neck of right femur"),
    ("T79.4XXA","Traumatic shock, initial encounter"),
    ("O60.14", "Preterm labor with preterm delivery"),
    ("O62.0",  "Primary inadequate contractions"),
    ("R55",    "Syncope and collapse"),
    ("E11.65", "Type 2 diabetes mellitus with hyperglycemia"),
    ("E16.0",  "Drug-induced hypoglycemia without coma"),
    ("G40.909","Epilepsy, unspecified, not intractable"),
    ("T71.1",  "Asphyxiation due to smothering"),
    ("W19",    "Unspecified fall"),
    ("X71",    "Intentional self-harm by drowning and submersion"),
]


def fetch_topic(icd10: str) -> dict | None:
    params = urllib.parse.urlencode({
        "mainSearchCriteria.v.c": icd10,
        "mainSearchCriteria.v.cs": "2.16.840.1.113883.6.90",
        "informationRecipient.languageCode.c": "en",
        "knowledgeResponseType": "application/json",
    })
    url = f"{MEDLINEPLUS_API}?{params}"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def extract_entries(response: dict, icd10: str, description: str) -> list[dict]:
    entries = []
    feed = response.get("feed", {})
    for entry in feed.get("entry", []):
        title = entry.get("title", {}).get("_value", "").strip()
        summary = entry.get("summary", {}).get("_value", "").strip()
        link = ""
        for lnk in entry.get("link", []):
            if lnk.get("rel") == "alternate":
                link = lnk.get("href", "")
                break
        if title and summary:
            entries.append({
                "icd10": icd10,
                "condition": description,
                "title": title,
                "summary": summary[:3000],
                "source": "MedlinePlus/NIH",
                "url": link,
            })
    return entries


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / "medlineplus_ems.jsonl"
    total = 0

    with open(out_path, "w") as f:
        for icd10, description in EMS_ICD10_CODES:
            print(f"Fetching ICD-10 {icd10}: {description}")
            try:
                resp = fetch_topic(icd10)
                if resp:
                    entries = extract_entries(resp, icd10, description)
                    for entry in entries:
                        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
                        total += 1
                    print(f"  {len(entries)} entries")
                time.sleep(0.3)
            except Exception as e:
                print(f"  Error: {e}", file=sys.stderr)

    print(f"\nWrote {total} records -> {out_path}")


if __name__ == "__main__":
    main()
