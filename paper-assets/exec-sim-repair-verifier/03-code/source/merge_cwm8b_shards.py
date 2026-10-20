#!/usr/bin/env python3
"""
merge_cwm8b_shards.py — 合并 CWM 8B eval 多 shard 结果
输入: 多个 JSONL 结果文件（v3 + shard2 + shard3）
输出: 合并去重后的 JSONL + 统计摘要
关键: 按 sample index 去重（shard 之间有重叠区间）
"""

import argparse
import json
import os
import sys
from collections import Counter, defaultdict

SHARD_CONFIG = {
    "v3":     {"dir": "cwm_8b_ckpt400_test",        "priority": 1},
    "shard3": {"dir": "cwm_8b_ckpt400_test_shard3",  "priority": 3},
    "shard2": {"dir": "cwm_8b_ckpt400_test_shard2",  "priority": 2},
    "shard4": {"dir": "cwm_8b_ckpt400_test_shard4",  "priority": 4},
}

TEST_DATA_PATH = "data/swebench_full/swebench_test.jsonl"
EXPECTED_TOTAL = 9784


def load_jsonl(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_mutation_types(path):
    mapping = {}
    with open(path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if line:
                mapping[i] = json.loads(line).get("mutation_type", "unknown")
    return mapping


def merge_shards(eval_root):
    best = {}  # idx -> (priority, record, shard_name)

    for shard_name, cfg in SHARD_CONFIG.items():
        fpath = os.path.join(eval_root, cfg["dir"], "results_incremental.jsonl")
        if not os.path.exists(fpath):
            print(f"WARNING: {fpath} not found, skipping", file=sys.stderr)
            continue
        rows = load_jsonl(fpath)
        prio = cfg["priority"]
        kept = 0
        for r in rows:
            idx = r["index"]
            if idx not in best or prio > best[idx][0]:
                best[idx] = (prio, r, shard_name)
                kept += 1
        print(f"  {shard_name:<8} ({cfg['dir']}): {len(rows):>5} rows, {kept} kept as highest-priority")

    merged = [best[idx][1] for idx in sorted(best)]
    source_counts = Counter(best[idx][2] for idx in best)
    print(f"  Total merged: {len(merged)} (sources: {dict(source_counts)})")
    return merged


def analyze(merged, mutation_map):
    total = len(merged)
    indices = {r["index"] for r in merged}
    missing = sorted(set(range(EXPECTED_TOTAL)) - indices)

    label_counts = Counter(r["label"] for r in merged)
    majority_class = 1 if label_counts.get(1, 0) >= label_counts.get(0, 0) else 0
    majority_baseline = max(label_counts.values()) / total * 100 if total else 0

    n_unparseable = sum(1 for r in merged if r.get("unparseable", False))
    n_parseable = total - n_unparseable

    # Overall: parseable uses model pred, unparseable defaults to "pass" (pred=1)
    overall_correct = 0
    parseable_correct = 0
    for r in merged:
        if r.get("unparseable", False):
            overall_correct += int(1 == r["label"])
        else:
            overall_correct += r["correct"]
            parseable_correct += r["correct"]

    overall_acc = overall_correct / total * 100 if total else 0
    parseable_acc = parseable_correct / n_parseable * 100 if n_parseable else 0

    # Per-mutation
    mut_stats = defaultdict(lambda: {
        "total": 0, "parseable": 0, "overall_correct": 0, "parseable_correct": 0
    })
    for r in merged:
        mt = mutation_map.get(r["index"], "unknown")
        s = mut_stats[mt]
        s["total"] += 1
        is_p = not r.get("unparseable", False)
        if is_p:
            s["parseable"] += 1
            s["parseable_correct"] += r["correct"]
            s["overall_correct"] += r["correct"]
        else:
            s["overall_correct"] += int(1 == r["label"])

    per_mutation = {}
    for mt in sorted(mut_stats):
        s = mut_stats[mt]
        per_mutation[mt] = {
            "count": s["total"],
            "accuracy": round(s["overall_correct"] / s["total"] * 100, 2) if s["total"] else 0,
            "parse_rate": round(s["parseable"] / s["total"] * 100, 2) if s["total"] else 0,
            "parseable_acc": round(s["parseable_correct"] / s["parseable"] * 100, 2) if s["parseable"] else 0,
        }

    return {
        "total_samples": total,
        "expected_samples": EXPECTED_TOTAL,
        "n_missing": len(missing),
        "missing_indices": missing[:50],
        "coverage_complete": len(missing) == 0,
        "class_balance": {"pass": label_counts.get(1, 0), "fail": label_counts.get(0, 0)},
        "majority_class": majority_class,
        "majority_baseline_accuracy": round(majority_baseline, 2),
        "overall_accuracy": round(overall_acc, 2),
        "unparseable_count": n_unparseable,
        "unparseable_rate": round(n_unparseable / total * 100, 2) if total else 0,
        "parseable_only_accuracy": round(parseable_acc, 2),
        "accuracy_gap_over_majority": round(overall_acc - majority_baseline, 2),
        "per_mutation": per_mutation,
    }


def print_summary(m):
    print("\n" + "=" * 72)
    print("CWM 8B ckpt-400 TEST EVAL — MERGED RESULTS")
    print("=" * 72)
    print(f"\nTotal: {m['total_samples']} / {m['expected_samples']}")
    if m["n_missing"] > 0:
        print(f"  MISSING {m['n_missing']} indices: {m['missing_indices']}")
    else:
        print("  Coverage: COMPLETE (idx 0-9783)")

    cb = m["class_balance"]
    t = m["total_samples"]
    print(f"\nClass balance: pass={cb['pass']} ({cb['pass']/t*100:.1f}%), "
          f"fail={cb['fail']} ({cb['fail']/t*100:.1f}%)")
    print(f"Majority baseline:       {m['majority_baseline_accuracy']:.2f}%")
    print(f"Overall accuracy:        {m['overall_accuracy']:.2f}%  (unparseable→pass)")
    print(f"  Gap over majority:     {m['accuracy_gap_over_majority']:+.2f}pp")
    print(f"Unparseable rate:        {m['unparseable_rate']:.2f}% ({m['unparseable_count']}/{t})")
    print(f"Parseable-only accuracy: {m['parseable_only_accuracy']:.2f}%")

    pm = m["per_mutation"]
    print(f"\n{'Mutation':<25} {'Count':>6} {'Accuracy':>10} {'ParseRate':>10} {'ParseAcc':>10}")
    print(f"{'─'*25} {'─'*6} {'─'*10} {'─'*10} {'─'*10}")
    for mt in sorted(pm, key=lambda k: -pm[k]["count"]):
        s = pm[mt]
        print(f"{mt:<25} {s['count']:>6} {s['accuracy']:>9.2f}% {s['parse_rate']:>9.2f}% {s['parseable_acc']:>9.2f}%")
    print("=" * 72)


def main():
    p = argparse.ArgumentParser(description="Merge CWM 8B eval shards and analyze")
    p.add_argument("--eval_root", default="/root/autodl-tmp/eval_results",
                   help="Root dir containing shard subdirs")
    p.add_argument("--project_dir", default="/home/sonny/exec-sim-repair-verifier",
                   help="Project root (for dataset lookup)")
    p.add_argument("--output_dir", default=None,
                   help="Output dir (default: <eval_root>/cwm_8b_ckpt400_test_merged)")
    p.add_argument("--dry-run", action="store_true",
                   help="Only report stats without writing output files")
    args = p.parse_args()

    eval_root = args.eval_root
    dataset_path = os.path.join(args.project_dir, TEST_DATA_PATH)
    output_dir = args.output_dir or os.path.join(eval_root, "cwm_8b_ckpt400_test_merged")

    print(f"Eval root:    {eval_root}")
    print(f"Dataset:      {dataset_path}")
    print(f"Output dir:   {output_dir}")
    if args.dry_run:
        print("** DRY RUN — no files will be written **")
    print()

    # Load mutation types
    print("Loading mutation types from dataset...")
    mutation_map = load_mutation_types(dataset_path)
    print(f"  {len(mutation_map)} entries loaded")

    # Merge shards
    print("\nMerging shards (higher priority wins on overlap)...")
    merged = merge_shards(eval_root)

    # Attach mutation_type to records
    for r in merged:
        r["mutation_type"] = mutation_map.get(r["index"], "unknown")

    # Analysis
    metrics = analyze(merged, mutation_map)
    print_summary(metrics)

    if args.dry_run:
        print("\nDry run complete. No files written.")
        return

    # Write outputs
    os.makedirs(output_dir, exist_ok=True)

    jsonl_path = os.path.join(output_dir, "results_merged.jsonl")
    with open(jsonl_path, "w") as f:
        for r in merged:
            f.write(json.dumps(r) + "\n")
    print(f"\nMerged JSONL → {jsonl_path}")

    metrics_path = os.path.join(output_dir, "metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Metrics JSON → {metrics_path}")


if __name__ == "__main__":
    main()
