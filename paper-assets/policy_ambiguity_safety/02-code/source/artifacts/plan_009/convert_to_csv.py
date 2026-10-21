#!/usr/bin/env python3
"""Convert annotation_sheet_clean.jsonl to annotation_sheet.csv for human annotation.

Reads the JSONL produced by calibration.py (Step 3) and writes a CSV with the subset
of columns needed by human annotators.  severity_label and justification columns are
left empty for annotators to fill in.

Input : artifacts/plan_009/annotation_sheet_clean.jsonl   (100 rows)
Output: artifacts/plan_009/annotation_sheet.csv           (header + 100 data rows)
"""

import csv
import json
from pathlib import Path

PLAN_DIR = Path(__file__).resolve().parent
INPUT_JSONL = PLAN_DIR / "annotation_sheet_clean.jsonl"
OUTPUT_CSV = PLAN_DIR / "annotation_sheet.csv"

CSV_COLUMNS = [
    "annotation_id",
    "episode_id",
    "ambiguity_type",
    "condition",
    "ground_truth_clause",
    "agent_clause",
    "trajectory_summary",
    "severity_label",
    "justification",
]


def main():
    rows = []
    with open(INPUT_JSONL, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            rows.append({
                "annotation_id": record["annotation_id"],
                "episode_id": record["episode_id"],
                "ambiguity_type": record["ambiguity_type"],
                "condition": record["condition"],
                "ground_truth_clause": record["ground_truth_clause"],
                "agent_clause": record["agent_clause"],
                "trajectory_summary": record["trajectory_summary"],
                "severity_label": "",   # to be filled by annotator
                "justification": "",    # to be filled by annotator
            })

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
