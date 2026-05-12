#!/usr/bin/env python3
"""
Fetch FEMA Emergency Management Institute (EMI) independent study course content.

All FEMA/EMI course content is produced by the U.S. federal government
and is in the public domain (17 U.S.C. § 105).

Pass course numbers on the command line, or add them to COURSES below.
Example: python fetch_fema.py IS-100 IS-200 IS-700 IS-800

EMI course catalog: https://training.fema.gov/is/crslist.aspx
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"

# EMS-relevant FEMA/EMI courses (public domain)
# Add course numbers here or pass on command line
COURSES: dict[str, str] = {
    # ICS / NIMS / Incident Command — required for all first responders
    "IS-100.c":  "Introduction to Incident Command System, ICS-100",
    "IS-200.c":  "Basic Incident Command System for Initial Response, ICS-200",
    "IS-700.b":  "An Introduction to the National Incident Management System",
    "IS-800.d":  "National Response Framework, An Introduction",
    "IS-702.a":  "NIMS Public Information",
    "IS-703.a":  "NIMS Resource Management",
    "IS-706":    "NIMS Intrastate Mutual Aid, An Introduction",
    # MCI / Mass Casualty
    "IS-368":    "Including People with Disabilities in Disaster Operations",
    "IS-552":    "Considerations for Integration of Community Health and Medical Preparedness with COOP",
    "IS-2900":   "National Disaster Recovery Framework Overview",
    # Hazmat / WMD — relevant for EMRs at hazmat scenes
    "IS-5.a":    "An Introduction to Hazardous Materials",
    "IS-346":    "An Approach to Outreach for Disaster Preparedness",
    # Additional first responder preparedness
    "IS-317":    "Introduction to Community Emergency Response Teams",
    "IS-393.b":  "Introduction to Hazard Mitigation",
    "IS-271":    "Anticipating Hazardous Weather and Community Risk",
    "IS-909":    "Community Preparedness: Implementing Simple Activities for Everyone",
}

EMI_BASE = "https://training.fema.gov/emiweb/is/courseoverview.aspx"
EMI_STUDY = "https://training.fema.gov/is/courseoverview.aspx"


def fetch_course_metadata(course_id: str, title: str) -> dict:
    """Build a metadata record for a FEMA course (full content requires login/download)."""
    clean_id = course_id.upper().replace("IS-", "").replace(".", "")
    return {
        "course_id": course_id,
        "title": title,
        "source": "FEMA Emergency Management Institute (EMI)",
        "url": f"https://training.fema.gov/is/courseoverview.aspx?code={course_id}",
        "certificate_url": f"https://training.fema.gov/is/course.aspx?code={course_id}",
        "license": "Public Domain (U.S. Government work, 17 U.S.C. § 105)",
        "type": "fema_course",
        "relevance": "EMS / First Responder ICS and emergency operations",
    }


def fetch_course_list_page() -> list[dict]:
    """
    Fetch the EMI IS course list for EMS-relevant courses.
    Returns a list of {course_id, title} dicts.
    """
    url = "https://training.fema.gov/is/crslist.aspx"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; BONES-datacollect/1.0)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", errors="replace")
        # Simple extraction of course entries from page
        courses = []
        for line in html.split("\n"):
            if "courseoverview.aspx?code=IS-" in line:
                try:
                    code_start = line.index("code=") + 5
                    code_end = line.index('"', code_start)
                    code = line[code_start:code_end]
                    title_start = line.index(">", code_end) + 1
                    title_end = line.index("<", title_start)
                    title = line[title_start:title_end].strip()
                    if code and title:
                        courses.append({"course_id": code, "title": title})
                except ValueError:
                    continue
        return courses
    except Exception as e:
        print(f"  Warning: Could not fetch course list: {e}", file=sys.stderr)
        return []


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Merge built-in courses with any passed on command line
    course_dict = dict(COURSES)
    for arg in sys.argv[1:]:
        code = arg.upper()
        if not code.startswith("IS-"):
            code = f"IS-{code}"
        if code not in course_dict:
            course_dict[code] = f"FEMA EMI {code}"

    out_path = RAW_DIR / "fema_emi_courses.jsonl"
    total = 0

    with open(out_path, "w") as f:
        for course_id, title in course_dict.items():
            print(f"Recording: {course_id} — {title}")
            record = fetch_course_metadata(course_id, title)
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            total += 1
            time.sleep(0.1)

    print(f"\nWrote {total} FEMA course records -> {out_path}")
    print("\nTo get full course content (public domain):")
    print("  Visit: https://training.fema.gov/is/crslist.aspx")
    print("  Download PDF study materials for each course")
    print("  Place PDFs in data/raw/fema/ and run scripts/data_collection/parse_fema_pdfs.py")


if __name__ == "__main__":
    main()
