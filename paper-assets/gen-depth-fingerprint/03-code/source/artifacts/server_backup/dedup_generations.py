#!/usr/bin/env python3
"""Deduplicate multi_domain_seeds generation JSONL files.

Input:  data/pythia-2.8b-{news,scientific,creative}/generations_shard0.jsonl
Output: Same files with duplicates removed (originals backed up as .jsonl.bak)

Dedup key: (seed_id, depth). Keeps the LAST occurrence (newest write).
Usage:  python dedup_generations.py [--dry-run]
"""

import argparse
import json
import shutil
from collections import OrderedDict
from pathlib import Path

BASE = Path("/root/gen-depth-fingerprint/data")
DOMAINS = ["news", "scientific", "creative"]
EXPECTED_PER_DOMAIN = 2500  # 500 seeds × 5 depths
TOLERANCE = 0.20


def dedup_file(path: Path, dry_run: bool) -> dict:
    """Deduplicate a single JSONL file. Returns stats dict."""
    if not path.exists():
        return {"status": "skipped", "reason": "file not found"}

    records = OrderedDict()
    bad_lines = 0
    total = 0

    with open(path, "r") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                bad_lines += 1
                print(f"  WARNING: invalid JSON at line {lineno}, skipping")
                continue
            key = (obj.get("seed_id"), obj.get("depth"))
            records[key] = line  # last write wins

    deduped = total - bad_lines - len(records) + (bad_lines)  # duplicates removed
    kept = len(records)
    removed = total - kept - bad_lines

    lo = EXPECTED_PER_DOMAIN * (1 - TOLERANCE)
    hi = EXPECTED_PER_DOMAIN * (1 + TOLERANCE)
    in_range = lo <= kept <= hi

    stats = {
        "status": "ok",
        "original": total,
        "kept": kept,
        "removed": removed,
        "bad_lines": bad_lines,
        "expected_range": f"{int(lo)}-{int(hi)}",
        "in_range": in_range,
    }

    if not dry_run and removed > 0:
        bak = path.with_suffix(".jsonl.bak")
        shutil.copy2(path, bak)
        print(f"  Backup: {bak}")
        with open(path, "w") as f:
            for record in records.values():
                f.write(record + "\n")
        print(f"  Written: {path}")

    return stats


def main():
    parser = argparse.ArgumentParser(description="Deduplicate generation JSONL files")
    parser.add_argument("--dry-run", action="store_true", help="Report only, no writes")
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN (no files will be modified) ===\n")

    for domain in DOMAINS:
        path = BASE / f"pythia-2.8b-{domain}" / "generations_shard0.jsonl"
        print(f"[{domain}] {path}")
        stats = dedup_file(path, args.dry_run)

        if stats["status"] == "skipped":
            print(f"  Skipped: {stats['reason']}\n")
            continue

        print(f"  Original: {stats['original']}")
        print(f"  Kept:     {stats['kept']}")
        print(f"  Removed:  {stats['removed']}")
        print(f"  Bad JSON: {stats['bad_lines']}")
        print(f"  Expected: {stats['expected_range']}  {'OK' if stats['in_range'] else 'WARNING: out of range'}")
        print()


if __name__ == "__main__":
    main()
