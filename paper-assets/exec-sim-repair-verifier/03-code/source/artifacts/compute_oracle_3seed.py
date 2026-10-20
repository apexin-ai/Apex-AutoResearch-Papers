#!/usr/bin/env python3
"""Compute cross-seed oracle accuracy (CLS ∪ CWM) at repo level.

Target: 94.27 ± 2.59% (3 seeds: 42, 123, 456)

Oracle = for each problem, if either CLS or CWM (from any seed) predicts
correctly, count as correct. Computed per-seed (each seed gets its own oracle),
then mean ± std across seeds.

Requires prediction JSONL files on the evaluation server. This script documents
the computation logic; to run, provide paths to the prediction files.

Usage:
  python3 compute_oracle_3seed.py \\
    --cls-preds cls_s42.jsonl cls_s123.jsonl cls_s456.jsonl \\
    --cwm-preds cwm_s42.jsonl cwm_s123.jsonl cwm_s456.jsonl

Without prediction files, the script shows the documented per-seed results.
"""

import argparse
import json
import math
import sys
from collections import defaultdict


# --- Documented results from worker analysis (2026-05-22) ---
# Source: worker_analysis_multi-seed-oracle_20260522T124959_result.json
DOCUMENTED_RESULTS = {
    "s42": {
        "cls_acc": 85.34,
        "cwm_acc": 65.17,
        "oracle_acc": 91.28,
        "note": "Same training seed for both CLS and CWM → higher error correlation",
    },
    "s123": {
        "cls_acc": 85.34,
        "cwm_acc": 67.33,
        "oracle_acc": 95.86,
        "note": "CWM uses different seed → lower error correlation with CLS",
    },
    "s456": {
        "cls_acc": 85.34,
        "cwm_acc": 66.93,
        "oracle_acc": 95.68,
        "note": "CWM uses different seed → lower error correlation with CLS",
    },
}


def load_predictions(path):
    """Load prediction file (JSON list or JSONL)."""
    with open(path) as f:
        raw = json.load(f)
    if isinstance(raw, dict) and "predictions" in raw:
        records = raw["predictions"]
    elif isinstance(raw, list):
        records = raw
    else:
        with open(path) as f:
            records = [json.loads(line) for line in f if line.strip()]
    out = {}
    for r in records:
        idx = r.get("index", r.get("idx"))
        label = int(r.get("label", r.get("true_label")))
        pred = int(r.get("pred", r.get("prediction", r.get("predicted_label"))))
        pid = r["problem_id"]
        out[idx] = {"label": label, "pred": pred, "problem_id": pid, "correct": pred == label}
    return out


def compute_oracle(cls_preds, cwm_preds):
    """Compute oracle (CLS ∪ CWM) accuracy at problem level."""
    common = sorted(set(cls_preds) & set(cwm_preds))
    if not common:
        raise ValueError("No common indices between CLS and CWM predictions")

    # Group by problem
    problems = defaultdict(lambda: {"cls_correct": [], "cwm_correct": [], "labels": []})
    for idx in common:
        c, w = cls_preds[idx], cwm_preds[idx]
        assert c["label"] == w["label"], f"Label mismatch at {idx}"
        pid = c["problem_id"]
        problems[pid]["cls_correct"].append(c["correct"])
        problems[pid]["cwm_correct"].append(w["correct"])

    n_problems = len(problems)
    cls_correct_problems = 0
    cwm_correct_problems = 0
    oracle_correct_problems = 0

    for pid, data in problems.items():
        cls_all_correct = all(data["cls_correct"])
        cwm_all_correct = all(data["cwm_correct"])
        cls_correct_problems += cls_all_correct
        cwm_correct_problems += cwm_all_correct
        oracle_correct_problems += (cls_all_correct or cwm_all_correct)

    return {
        "n_tests": len(common),
        "n_problems": n_problems,
        "cls_acc": round(cls_correct_problems / n_problems * 100, 2),
        "cwm_acc": round(cwm_correct_problems / n_problems * 100, 2),
        "oracle_acc": round(oracle_correct_problems / n_problems * 100, 2),
        "oracle_gain_over_cls": round(
            (oracle_correct_problems - cls_correct_problems) / n_problems * 100, 2
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cls-preds", nargs="+", help="CLS prediction files (one per seed)")
    ap.add_argument("--cwm-preds", nargs="+", help="CWM prediction files (one per seed)")
    args = ap.parse_args()

    if args.cls_preds and args.cwm_preds:
        if len(args.cls_preds) != len(args.cwm_preds):
            ap.error("Must provide same number of CLS and CWM prediction files")

        print("Computing oracle from prediction files...")
        print("=" * 60)

        oracle_accs = []
        for i, (cls_path, cwm_path) in enumerate(zip(args.cls_preds, args.cwm_preds)):
            print(f"\nSeed {i+1}: {cls_path} vs {cwm_path}")
            cls_preds = load_predictions(cls_path)
            cwm_preds = load_predictions(cwm_path)
            result = compute_oracle(cls_preds, cwm_preds)
            oracle_accs.append(result["oracle_acc"])
            print(f"  CLS: {result['cls_acc']}%  CWM: {result['cwm_acc']}%")
            print(f"  Oracle: {result['oracle_acc']}%  (+{result['oracle_gain_over_cls']}pp)")

        mean_oracle = sum(oracle_accs) / len(oracle_accs)
        if len(oracle_accs) > 1:
            std_oracle = math.sqrt(
                sum((x - mean_oracle) ** 2 for x in oracle_accs) / (len(oracle_accs) - 1)
            )
        else:
            std_oracle = 0.0

        print(f"\n{'='*60}")
        print(f"Cross-seed oracle: {mean_oracle:.2f} ± {std_oracle:.2f}%")
        print(f"Per-seed: {oracle_accs}")
    else:
        # Show documented results
        print("Cross-seed Oracle (CLS ∪ CWM) — Repo Level")
        print("Source: worker_analysis_multi-seed-oracle_20260522T124959_result.json")
        print("=" * 60)

        oracle_accs = []
        for seed, data in DOCUMENTED_RESULTS.items():
            print(f"\n{seed}:")
            print(f"  CLS: {data['cls_acc']}%  CWM: {data['cwm_acc']}%")
            print(f"  Oracle: {data['oracle_acc']}%")
            print(f"  ({data['note']})")
            oracle_accs.append(data["oracle_acc"])

        mean_oracle = sum(oracle_accs) / len(oracle_accs)
        std_oracle = math.sqrt(
            sum((x - mean_oracle) ** 2 for x in oracle_accs) / (len(oracle_accs) - 1)
        )

        print(f"\n{'='*60}")
        print(f"Cross-seed oracle: {mean_oracle:.2f} ± {std_oracle:.2f}%")
        print(f"Per-seed: {oracle_accs}")

        target_mean, target_std = 94.27, 2.59
        mean_match = abs(mean_oracle - target_mean) < 0.05
        std_match = abs(std_oracle - target_std) < 0.05
        print(f"\nTarget: {target_mean} ± {target_std}%")
        print(f"Mean: {'MATCH' if mean_match else 'MISMATCH'}")
        print(f"Std:  {'MATCH' if std_match else 'MISMATCH'}")

        if not args.cls_preds:
            print("\nTo compute from raw predictions, run:")
            print("  python3 compute_oracle_3seed.py \\")
            print("    --cls-preds cls_s42.jsonl cls_s123.jsonl cls_s456.jsonl \\")
            print("    --cwm-preds cwm_s42.jsonl cwm_s123.jsonl cwm_s456.jsonl")


if __name__ == "__main__":
    main()
