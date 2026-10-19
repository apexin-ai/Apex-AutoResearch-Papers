#!/usr/bin/env python3
"""
MF-2: Y-Stratified Non-Differential Misclassification Test

Tests whether LLM annotation error rates are independent of outcome proxies Y,
i.e. P(A*|A, Y) = P(A*|A). Uses permutation tests on column-stochastic
confusion matrices stratified by three Y proxies across 12 VAST configs
(4 models × 3 prompt types).

Input:  --data-dir containing *.jsonl files (one per config)
Output: artifacts/nondiff_y_stratified_results.json

Usage:
  python3 nondiff_y_stratified.py [--permutations 10000] [--data-dir <path>]

Dependencies: numpy (stdlib otherwise)
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = SCRIPT_DIR / "nondiff_y_stratified_data"
RESULTS_PATH = SCRIPT_DIR / "nondiff_y_stratified_results.json"

CLASS_NAMES = ["pro", "con", "neutral"]
K = 3
LABEL_TO_IDX = {name: i for i, name in enumerate(CLASS_NAMES)}

POSITIVE_WORDS = {"good", "great", "best", "love", "right", "support",
                  "agree", "positive", "benefit", "important"}
NEGATIVE_WORDS = {"bad", "worst", "hate", "wrong", "against", "oppose",
                  "negative", "harm", "dangerous", "fail"}


def load_config(path):
    records = []
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            gl = (r.get("gold_label") or "").lower().strip()
            pl = (r.get("pred_label") or "").lower().strip()
            if gl not in LABEL_TO_IDX or pl not in LABEL_TO_IDX:
                continue
            records.append({
                "idx": r["idx"],
                "text": r["text"],
                "topic": r.get("topic", "unknown"),
                "gold": LABEL_TO_IDX[gl],
                "pred": LABEL_TO_IDX[pl],
            })
    return records


def column_stochastic_cm(records):
    counts = np.zeros((K, K), dtype=float)
    for r in records:
        counts[r["pred"], r["gold"]] += 1
    col_sums = counts.sum(axis=0)
    C = np.full((K, K), np.nan)
    for k in range(K):
        if col_sums[k] > 0:
            C[:, k] = counts[:, k] / col_sums[k]
    return C


def max_deviation(C0, C1):
    diff = np.abs(C0 - C1)
    valid = ~np.isnan(diff)
    return float(np.nanmax(diff)) if valid.any() else 0.0


def frobenius_deviation(C0, C1):
    diff = C0 - C1
    valid = ~np.isnan(diff)
    return float(np.sqrt(np.nansum(diff[valid] ** 2))) if valid.any() else 0.0


def compute_sentiment(text):
    words = set(re.findall(r'\w+', text.lower()))
    pos = len(words & POSITIVE_WORDS)
    neg = len(words & NEGATIVE_WORDS)
    ratio = pos / (pos + neg + 1)
    return 1 if ratio > 0.5 else 0


def permutation_test_binary(records, y_values, n_perm, rng):
    y_arr = np.array(y_values)
    mask0 = y_arr == 0
    mask1 = y_arr == 1

    C0 = column_stochastic_cm([r for r, m in zip(records, mask0) if m])
    C1 = column_stochastic_cm([r for r, m in zip(records, mask1) if m])
    T_obs = max_deviation(C0, C1)
    frob = frobenius_deviation(C0, C1)

    T_perms = np.empty(n_perm)
    n = len(records)
    for b in range(n_perm):
        py = rng.permutation(y_arr)
        pm0, pm1 = py == 0, py == 1
        pC0 = column_stochastic_cm([records[i] for i in range(n) if pm0[i]])
        pC1 = column_stochastic_cm([records[i] for i in range(n) if pm1[i]])
        T_perms[b] = max_deviation(pC0, pC1)

    p_value = (1 + np.sum(T_perms >= T_obs)) / (1 + n_perm)
    return {
        "n_y0": int(mask0.sum()),
        "n_y1": int(mask1.sum()),
        "max_deviation": round(T_obs, 6),
        "frobenius_deviation": round(frob, 6),
        "p_value": round(float(p_value), 6),
        "null_95pct": round(float(np.percentile(T_perms, 95)), 6),
        "reject_005": bool(p_value <= 0.05),
    }


def permutation_test_categorical(records, y_values, n_perm, rng):
    groups = sorted(set(y_values))
    group_counts = Counter(y_values)
    y_arr = np.array(y_values)

    C_per = {}
    for g in groups:
        C_per[g] = column_stochastic_cm([r for r, yv in zip(records, y_values) if yv == g])

    max_pw = 0.0
    for i, g1 in enumerate(groups):
        for g2 in groups[i + 1:]:
            d = max_deviation(C_per[g1], C_per[g2])
            if d > max_pw:
                max_pw = d

    C_stack = np.array([C_per[g] for g in groups])
    with np.errstate(all="ignore"):
        var_per_entry = np.nanvar(C_stack, axis=0)
    T_obs = float(np.nanmax(var_per_entry)) if not np.all(np.isnan(var_per_entry)) else 0.0

    T_perms = np.empty(n_perm)
    n = len(records)
    for b in range(n_perm):
        py = rng.permutation(y_arr)
        pC_stack = []
        for g in groups:
            pC_stack.append(column_stochastic_cm([records[i] for i in range(n) if py[i] == g]))
        pC_arr = np.array(pC_stack)
        with np.errstate(all="ignore"):
            pvar = np.nanvar(pC_arr, axis=0)
        T_perms[b] = float(np.nanmax(pvar)) if not np.all(np.isnan(pvar)) else 0.0

    p_value = (1 + np.sum(T_perms >= T_obs)) / (1 + n_perm)
    return {
        "n_groups": len(groups),
        "groups": {g: int(group_counts[g]) for g in groups},
        "max_pairwise_deviation": round(max_pw, 6),
        "p_value": round(float(p_value), 6),
        "null_95pct": round(float(np.percentile(T_perms, 95)), 6),
        "reject_005": bool(p_value <= 0.05),
    }


def process_config(name, records, n_perm, rng):
    correct = sum(1 for r in records if r["gold"] == r["pred"])
    accuracy = correct / len(records) if records else 0.0

    # Y1: text_length
    lengths = [len(r["text"]) for r in records]
    median_len = float(np.median(lengths))
    y1 = [1 if l > median_len else 0 for l in lengths]
    res_y1 = permutation_test_binary(records, y1, n_perm, rng)

    # Y2: topic
    topic_counts = Counter(r["topic"] for r in records)
    big_topics = {t for t, c in topic_counts.items() if c >= 20}
    y2 = [r["topic"] if r["topic"] in big_topics else "other" for r in records]
    res_y2 = permutation_test_categorical(records, y2, n_perm, rng)

    # Y3: sentiment
    y3 = [compute_sentiment(r["text"]) for r in records]
    res_y3 = permutation_test_binary(records, y3, n_perm, rng)

    return {
        "n_samples": len(records),
        "n_valid": len(records),
        "overall_accuracy": round(accuracy, 4),
        "text_length": res_y1,
        "topic": res_y2,
        "sentiment": res_y3,
    }


def main():
    parser = argparse.ArgumentParser(description="MF-2: Y-Stratified Non-Differential Misclassification Test")
    parser.add_argument("--permutations", type=int, default=10000)
    parser.add_argument("--data-dir", type=str, default=None)
    args = parser.parse_args()

    data_dir = Path(args.data_dir) if args.data_dir else DEFAULT_DATA_DIR
    if not data_dir.exists():
        print(f"ERROR: data dir not found: {data_dir}", file=sys.stderr)
        sys.exit(1)

    jsonl_files = sorted(data_dir.glob("*.jsonl"))
    if not jsonl_files:
        print(f"ERROR: no .jsonl files in {data_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(jsonl_files)} configs in {data_dir}")
    print(f"Permutations: {args.permutations}")

    rng = np.random.default_rng(42)
    per_config = {}
    all_rejections_005 = 0
    all_rejections_010 = 0
    all_p_values = []
    all_max_devs = []

    for fpath in jsonl_files:
        config_name = fpath.stem
        records = load_config(fpath)
        print(f"\n  {config_name}: {len(records)} valid samples")

        result = process_config(config_name, records, args.permutations, rng)
        per_config[config_name] = result

        for proxy_name in ["text_length", "sentiment"]:
            p = result[proxy_name]["p_value"]
            md = result[proxy_name]["max_deviation"]
            all_p_values.append(p)
            all_max_devs.append(md)
            if p <= 0.05:
                all_rejections_005 += 1
            if p <= 0.10:
                all_rejections_010 += 1
            print(f"    {proxy_name}: max_dev={md:.4f}, p={p:.4f}")

        p = result["topic"]["p_value"]
        md = result["topic"]["max_pairwise_deviation"]
        all_p_values.append(p)
        all_max_devs.append(md)
        if p <= 0.05:
            all_rejections_005 += 1
        if p <= 0.10:
            all_rejections_010 += 1
        print(f"    topic: max_pw_dev={md:.4f}, p={p:.4f}, groups={result['topic']['n_groups']}")

    n_configs = len(per_config)
    n_proxies = 3
    total_tests = n_configs * n_proxies

    if all_rejections_005 == 0:
        conclusion = f"Non-differential misclassification supported: 0/{total_tests} tests reject at α=0.05"
    else:
        conclusion = f"Differential detected: {all_rejections_005}/{total_tests} tests reject at α=0.05"

    output = {
        "description": "Y-stratified non-differential misclassification test for VAST (K=3)",
        "n_configs": n_configs,
        "n_proxies": n_proxies,
        "total_tests": total_tests,
        "permutations": args.permutations,
        "summary": {
            "rejections_at_005": all_rejections_005,
            "rejections_at_010": all_rejections_010,
            "max_deviation_across_all": round(max(all_max_devs), 6) if all_max_devs else 0.0,
            "median_p_value": round(float(np.median(all_p_values)), 6) if all_p_values else 0.0,
            "min_p_value": round(min(all_p_values), 6) if all_p_values else 0.0,
            "conclusion": conclusion,
        },
        "per_config": per_config,
    }

    with open(RESULTS_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*60}")
    print(f"Results saved to {RESULTS_PATH}")
    print(f"Total tests: {total_tests}")
    print(f"Rejections at α=0.05: {all_rejections_005}")
    print(f"Rejections at α=0.10: {all_rejections_010}")
    print(f"Min p-value: {min(all_p_values):.4f}")
    print(f"Median p-value: {float(np.median(all_p_values)):.4f}")
    print(f"Max deviation: {max(all_max_devs):.4f}")
    print(f"Conclusion: {conclusion}")


if __name__ == "__main__":
    main()
