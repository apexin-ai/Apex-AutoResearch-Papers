"""A1: Natural cascade length analysis.

Analyzes ack chain length vs pruning outcome to test the cascade dissolution hypothesis:
longer ack chains → more redundancy → safer pruning.
"""
import json
import glob
import os
import sys
from collections import defaultdict

import numpy as np
from scipy import stats

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "cascade_length_analysis")


def load_oracle_data(backbone: str) -> list[dict]:
    """Load all seed files for a backbone, return flat list of per-task records."""
    if backbone == "qwen":
        pattern = os.path.join(BASE_DIR, "outputs", "oracle_qwen_10run", "seed_*.json")
    elif backbone == "llama":
        pattern = os.path.join(BASE_DIR, "outputs", "oracle_llama_10run", "seed_*.json")
    else:
        raise ValueError(f"Unknown backbone: {backbone}")

    tasks = []
    seen = set()
    for fpath in sorted(glob.glob(pattern)):
        seed = os.path.basename(fpath).replace("seed_", "").replace(".json", "")
        with open(fpath) as f:
            data = json.load(f)
        for task in data["per_task"]:
            key = (seed, task["task_id"])
            if key not in seen:
                seen.add(key)
                task["_seed"] = seed
                tasks.append(task)
    return tasks


def compute_max_ack_chain(oracle_decisions: list[dict]) -> int:
    """Compute longest consecutive ack chain in a task's oracle decisions."""
    max_chain = 0
    current_chain = 0
    for dec in oracle_decisions:
        if dec.get("is_ack", False):
            current_chain += 1
            max_chain = max(max_chain, current_chain)
        else:
            current_chain = 0
    return max_chain


def compute_total_ack_count(oracle_decisions: list[dict]) -> int:
    """Total number of ack messages in a task."""
    return sum(1 for d in oracle_decisions if d.get("is_ack", False))


def bucket_chain_length(length: int) -> str:
    if length >= 4:
        return "4+"
    return str(length)


def analyze_backbone(backbone: str) -> dict:
    tasks = load_oracle_data(backbone)
    if not tasks:
        return {"error": f"No data for {backbone}"}

    records = []
    for task in tasks:
        decisions = task.get("oracle_decisions", [])
        if not decisions:
            continue
        chain_len = compute_max_ack_chain(decisions)
        total_acks = compute_total_ack_count(decisions)
        baseline_correct = task["baseline_correct"]
        pruned_correct = task["oracle_pruned_correct"]

        if baseline_correct == pruned_correct:
            outcome = "safe"
        elif not baseline_correct and pruned_correct:
            outcome = "improved"
        else:
            outcome = "degraded"

        records.append({
            "task_id": task["task_id"],
            "seed": task["_seed"],
            "chain_length": chain_len,
            "total_acks": total_acks,
            "baseline_correct": baseline_correct,
            "pruned_correct": pruned_correct,
            "outcome": outcome,
            "safe": 1 if outcome == "safe" else 0,
        })

    # Bucket analysis
    buckets = defaultdict(lambda: {"n": 0, "safe": 0, "improved": 0, "degraded": 0})
    for r in records:
        b = bucket_chain_length(r["chain_length"])
        buckets[b]["n"] += 1
        buckets[b][r["outcome"]] += 1

    bucket_results = {}
    for b in sorted(buckets.keys(), key=lambda x: (0, int(x)) if x.isdigit() else (1, 0)):
        d = buckets[b]
        bucket_results[b] = {
            "n_tasks": d["n"],
            "n_safe": d["safe"],
            "n_improved": d["improved"],
            "n_degraded": d["degraded"],
            "safe_rate": round(d["safe"] / d["n"] * 100, 1) if d["n"] > 0 else 0,
            "improved_rate": round(d["improved"] / d["n"] * 100, 1) if d["n"] > 0 else 0,
            "degraded_rate": round(d["degraded"] / d["n"] * 100, 1) if d["n"] > 0 else 0,
        }

    # Statistical tests
    chain_lengths = np.array([r["chain_length"] for r in records])
    safety_binary = np.array([r["safe"] for r in records])

    # Point-biserial correlation
    if len(np.unique(safety_binary)) > 1:
        pb_r, pb_p = stats.pointbiserialr(safety_binary, chain_lengths)
    else:
        pb_r, pb_p = float("nan"), float("nan")

    # Mann-Whitney U: chain lengths of safe vs changed tasks
    safe_chains = chain_lengths[safety_binary == 1]
    changed_chains = chain_lengths[safety_binary == 0]
    if len(safe_chains) > 0 and len(changed_chains) > 0:
        mw_stat, mw_p = stats.mannwhitneyu(safe_chains, changed_chains, alternative="two-sided")
    else:
        mw_stat, mw_p = float("nan"), float("nan")

    # Cochran-Armitage trend test (manual implementation)
    # H0: no linear trend in degradation rate across ordered chain length groups
    bucket_order = sorted(buckets.keys(), key=lambda x: (0, int(x)) if x.isdigit() else (1, 4))
    scores = []
    n_i = []
    x_i = []
    for i, b in enumerate(bucket_order):
        score = int(b) if b.isdigit() else 4
        scores.append(score)
        n_i.append(buckets[b]["n"])
        x_i.append(buckets[b]["degraded"])

    scores = np.array(scores, dtype=float)
    n_i = np.array(n_i, dtype=float)
    x_i = np.array(x_i, dtype=float)
    N = n_i.sum()
    p_hat = x_i.sum() / N if N > 0 else 0

    t_bar = np.sum(scores * n_i) / N if N > 0 else 0
    numerator = np.sum(scores * (x_i - n_i * p_hat))
    denominator_sq = p_hat * (1 - p_hat) * (np.sum(n_i * scores**2) - N * t_bar**2)
    if denominator_sq > 0:
        ca_z = numerator / np.sqrt(denominator_sq)
        ca_p = 2 * (1 - stats.norm.cdf(abs(ca_z)))
    else:
        ca_z, ca_p = float("nan"), float("nan")

    return {
        "backbone": backbone,
        "total_records": len(records),
        "unique_tasks": len(set(r["task_id"] for r in records)),
        "n_seeds": len(set(r["seed"] for r in records)),
        "buckets": bucket_results,
        "stats": {
            "point_biserial_r": round(pb_r, 4) if not np.isnan(pb_r) else None,
            "point_biserial_p": round(pb_p, 4) if not np.isnan(pb_p) else None,
            "mann_whitney_U": round(float(mw_stat), 2) if not np.isnan(mw_stat) else None,
            "mann_whitney_p": round(mw_p, 4) if not np.isnan(mw_p) else None,
            "cochran_armitage_z": round(ca_z, 4) if not np.isnan(ca_z) else None,
            "cochran_armitage_p": round(ca_p, 4) if not np.isnan(ca_p) else None,
        },
        "descriptive": {
            "mean_chain_safe": round(float(safe_chains.mean()), 2) if len(safe_chains) > 0 else None,
            "mean_chain_changed": round(float(changed_chains.mean()), 2) if len(changed_chains) > 0 else None,
            "median_chain_safe": round(float(np.median(safe_chains)), 1) if len(safe_chains) > 0 else None,
            "median_chain_changed": round(float(np.median(changed_chains)), 1) if len(changed_chains) > 0 else None,
        },
    }


def print_summary(results: list[dict]):
    print("=" * 80)
    print("A1: CASCADE LENGTH ANALYSIS — Ack Chain Length vs Pruning Outcome")
    print("=" * 80)

    for res in results:
        if "error" in res:
            print(f"\n{res['backbone']}: {res['error']}")
            continue

        print(f"\n{'─' * 40}")
        print(f"Backbone: {res['backbone'].upper()} | {res['total_records']} task-seed pairs "
              f"({res['unique_tasks']} unique tasks × {res['n_seeds']} seeds)")
        print(f"{'─' * 40}")
        print(f"{'Chain Len':<12}{'N_tasks':<10}{'Safe(%)':<12}{'Improved(%)':<14}{'Degraded(%)':<14}")
        print(f"{'-'*60}")
        for b, d in res["buckets"].items():
            print(f"{b:<12}{d['n_tasks']:<10}{d['safe_rate']:<12}{d['improved_rate']:<14}{d['degraded_rate']:<14}")

        s = res["stats"]
        desc = res["descriptive"]
        print(f"\nDescriptive:")
        print(f"  Mean chain length: safe={desc['mean_chain_safe']}, changed={desc['mean_chain_changed']}")
        print(f"  Median chain length: safe={desc['median_chain_safe']}, changed={desc['median_chain_changed']}")
        print(f"\nStatistical tests:")
        print(f"  Point-biserial r = {s['point_biserial_r']}, p = {s['point_biserial_p']}")
        print(f"  Mann-Whitney U: U = {s['mann_whitney_U']}, p = {s['mann_whitney_p']}")
        print(f"  Cochran-Armitage trend: z = {s['cochran_armitage_z']}, p = {s['cochran_armitage_p']}")

    print(f"\n{'=' * 80}")
    print("Hypothesis: longer ack chains → safer pruning (more redundancy to dissolve)")
    print("Support requires: positive r, safe tasks having longer chains, significant trend")
    print("=" * 80)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    results = []
    for backbone in ["qwen", "llama"]:
        print(f"Processing {backbone}...")
        res = analyze_backbone(backbone)
        results.append(res)

    print_summary(results)

    output_path = os.path.join(OUTPUT_DIR, "cascade_length_results.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    main()
