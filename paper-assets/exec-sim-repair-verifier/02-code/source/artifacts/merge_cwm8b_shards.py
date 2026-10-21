"""Merge CWM 8B ckpt-400 test eval shards into a single results file.

Input:
  - 4 shard JSONL files from /root/autodl-tmp/eval_results/:
    - cwm_8b_ckpt400_test/results_incremental.jsonl   (v3, idx ~0-6200+)
    - cwm_8b_ckpt400_test_shard3/results_incremental.jsonl (idx 6200-7679)
    - cwm_8b_ckpt400_test_shard2/results_incremental.jsonl (idx 7680-9783)
    - cwm_8b_ckpt400_test_shard4/results_incremental.jsonl (idx 9100-9783)
  - Test dataset: data/swebench_full/swebench_test.jsonl (for mutation_type)

Output (written to --output_dir, default = same as this script):
  - cwm_8b_ckpt400_test_merged.jsonl  — all 9784 results, sorted by index
  - cwm_8b_ckpt400_test_summary.json  — accuracy, F1, confusion matrix,
    unparseable rate, truncation stats, per-mutation breakdown

Dedup priority: v3 > shard3 > shard4 > shard2 (earlier in the list wins).

Usage:
  python merge_cwm8b_shards.py \
    --eval_dir /root/autodl-tmp/eval_results \
    --data_path /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl \
    --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_merged
"""

import argparse
import json
import os
import sys
from collections import Counter

SHARD_DIRS = [
    "cwm_8b_ckpt400_test",
    "cwm_8b_ckpt400_test_shard3",
    "cwm_8b_ckpt400_test_shard4",
    "cwm_8b_ckpt400_test_shard2",
]
EXPECTED_TOTAL = 9784


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def merge_shards(eval_dir):
    merged = {}
    shard_stats = {}
    for shard_name in SHARD_DIRS:
        path = os.path.join(eval_dir, shard_name, "results_incremental.jsonl")
        if not os.path.exists(path):
            print(f"WARNING: {path} not found, skipping")
            shard_stats[shard_name] = {"count": 0, "path": path, "exists": False}
            continue
        records = load_jsonl(path)
        new_count = 0
        dup_count = 0
        for r in records:
            idx = r["index"]
            if idx not in merged:
                merged[idx] = r
                new_count += 1
            else:
                dup_count += 1
        shard_stats[shard_name] = {
            "count": len(records),
            "new": new_count,
            "dup": dup_count,
            "path": path,
            "exists": True,
            "idx_min": min(r["index"] for r in records) if records else None,
            "idx_max": max(r["index"] for r in records) if records else None,
        }
        print(f"  {shard_name}: {len(records)} records, {new_count} new, {dup_count} duplicates")
    return merged, shard_stats


def check_coverage(merged):
    indices = set(merged.keys())
    expected = set(range(EXPECTED_TOTAL))
    missing = sorted(expected - indices)
    extra = sorted(indices - expected)
    return missing, extra


def compute_metrics(labels, preds):
    from sklearn.metrics import (
        accuracy_score, confusion_matrix, f1_score,
        precision_score, recall_score,
    )
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average="binary", zero_division=0)
    precision = precision_score(labels, preds, average="binary", zero_division=0)
    recall = recall_score(labels, preds, average="binary", zero_division=0)
    cm = confusion_matrix(labels, preds, labels=[0, 1]).tolist()
    return {
        "accuracy": round(acc * 100, 2),
        "f1": round(f1 * 100, 2),
        "precision": round(precision * 100, 2),
        "recall": round(recall * 100, 2),
        "confusion_matrix": cm,
    }


def per_mutation_breakdown(results, test_data):
    mutation_map = {}
    for i, d in enumerate(test_data):
        mutation_map[i] = d.get("mutation_type", "unknown")

    by_mutation = {}
    for r in results:
        mt = mutation_map.get(r["index"], "unknown")
        if mt not in by_mutation:
            by_mutation[mt] = {"correct": 0, "total": 0, "unparseable": 0,
                               "label_0": 0, "label_1": 0, "pred_0": 0, "pred_1": 0}
        entry = by_mutation[mt]
        entry["total"] += 1
        entry["correct"] += r["correct"]
        entry["unparseable"] += int(r.get("unparseable", False))
        entry[f"label_{r['label']}"] += 1
        entry[f"pred_{r['pred']}"] += 1

    for mt, entry in by_mutation.items():
        entry["accuracy"] = round(entry["correct"] / entry["total"] * 100, 2) if entry["total"] else 0
        entry["unparseable_rate"] = round(entry["unparseable"] / entry["total"] * 100, 2) if entry["total"] else 0

    return by_mutation


def main():
    parser = argparse.ArgumentParser(description="Merge CWM 8B eval shards")
    parser.add_argument("--eval_dir", default="/root/autodl-tmp/eval_results",
                        help="Directory containing shard subdirectories")
    parser.add_argument("--data_path",
                        default="/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl",
                        help="Test dataset JSONL for mutation_type lookup")
    parser.add_argument("--output_dir", default=None,
                        help="Output directory (default: <eval_dir>/cwm_8b_ckpt400_test_merged)")
    parser.add_argument("--strict", action="store_true",
                        help="Exit with error if any indices are missing")
    args = parser.parse_args()

    output_dir = args.output_dir or os.path.join(args.eval_dir, "cwm_8b_ckpt400_test_merged")
    os.makedirs(output_dir, exist_ok=True)

    print("Loading shards...")
    merged, shard_stats = merge_shards(args.eval_dir)
    print(f"\nTotal unique results: {len(merged)}/{EXPECTED_TOTAL}")

    missing, extra = check_coverage(merged)
    if missing:
        msg = f"MISSING {len(missing)} indices: {missing[:20]}{'...' if len(missing) > 20 else ''}"
        print(f"\n{'ERROR' if args.strict else 'WARNING'}: {msg}")
        if args.strict:
            sys.exit(1)
    if extra:
        print(f"WARNING: {len(extra)} unexpected indices (>{EXPECTED_TOTAL-1}): {extra[:20]}")

    results = [merged[i] for i in sorted(merged.keys())]

    labels = [r["label"] for r in results]
    preds = [r["pred"] for r in results]

    print("\nComputing metrics...")
    metrics = compute_metrics(labels, preds)

    n_unparseable = sum(1 for r in results if r.get("unparseable", False))
    unparseable_rate = round(n_unparseable / len(results) * 100, 2)

    n_truncated = sum(1 for r in results if r.get("truncated", False))
    truncated_rate = round(n_truncated / len(results) * 100, 2)
    trunc_correct = [r["correct"] for r in results if r.get("truncated", False)]
    non_trunc_correct = [r["correct"] for r in results if not r.get("truncated", False)]
    truncation_stats = {
        "truncated_count": n_truncated,
        "truncated_rate": truncated_rate,
        "truncated_accuracy": round(sum(trunc_correct) / len(trunc_correct) * 100, 2) if trunc_correct else None,
        "non_truncated_accuracy": round(sum(non_trunc_correct) / len(non_trunc_correct) * 100, 2) if non_trunc_correct else None,
    }

    print("Loading test data for mutation breakdown...")
    test_data = load_jsonl(args.data_path)
    mutation_breakdown = per_mutation_breakdown(results, test_data)

    summary = {
        "model": "CWM-8B",
        "checkpoint": "ckpt-400",
        "split": "test",
        "n_instances": len(results),
        "n_expected": EXPECTED_TOTAL,
        "n_missing": len(missing),
        "missing_indices": missing,
        "metrics": metrics,
        "n_unparseable": n_unparseable,
        "unparseable_rate": unparseable_rate,
        "truncation": truncation_stats,
        "per_mutation": mutation_breakdown,
        "shard_stats": shard_stats,
    }

    merged_path = os.path.join(output_dir, "cwm_8b_ckpt400_test_merged.jsonl")
    with open(merged_path, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    print(f"Merged results: {merged_path} ({len(results)} records)")

    summary_path = os.path.join(output_dir, "cwm_8b_ckpt400_test_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary: {summary_path}")

    print(f"\n{'='*60}")
    print(f"Accuracy:        {metrics['accuracy']}%")
    print(f"F1:              {metrics['f1']}%")
    print(f"Precision:       {metrics['precision']}%")
    print(f"Recall:          {metrics['recall']}%")
    print(f"Unparseable:     {n_unparseable}/{len(results)} ({unparseable_rate}%)")
    print(f"Truncated:       {n_truncated}/{len(results)} ({truncated_rate}%)")
    print(f"Confusion Matrix: {metrics['confusion_matrix']}")
    print(f"\nPer-mutation breakdown:")
    for mt in sorted(mutation_breakdown.keys()):
        entry = mutation_breakdown[mt]
        print(f"  {mt:30s}  n={entry['total']:5d}  acc={entry['accuracy']:6.2f}%  unparse={entry['unparseable_rate']:5.2f}%")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
