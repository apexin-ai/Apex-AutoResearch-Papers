"""Death decomposition analysis.

Quantifies how much of the Det-Internal gap comes from death avoidance
vs genuine score improvement. Core evidence for the paper.

Input:  results/{task_name}/episodes.jsonl
Output: JSON report, CSV summary

Dependencies: Python 3.8+ stdlib only (scipy optional for exact p-values)
"""

import argparse
import csv
import json
import math
import os
import random
import statistics
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

DEATH_THRESHOLD = -100
BOOTSTRAP_N = 10000
BOOTSTRAP_CI = 0.95
BOOTSTRAP_SEED = 42


def is_dead(score: float) -> bool:
    return score <= DEATH_THRESHOLD


def classify_episode(int_score: float, det_score: float) -> Tuple[str, str, str]:
    """Returns (label, reason, signal_source)."""
    int_died = is_dead(int_score)
    det_died = is_dead(det_score)

    if int_died and not det_died:
        return "det-preferred", "int_died_det_alive", "death_asymmetry"
    if det_died and not int_died:
        return "internal-preferred", "det_died_int_alive", "death_asymmetry"
    if int_died and det_died:
        return "no-preference", "both_died", "both_dead"
    if det_score > int_score:
        return "det-preferred", "both_alive_det_wins", "score_comparison"
    if int_score > det_score:
        return "internal-preferred", "both_alive_int_wins", "score_comparison"
    return "no-preference", "tie", "tied_alive"


def safe_mean(values: List[float]) -> float:
    return statistics.mean(values) if values else float("nan")


def bootstrap_ci(values: List[float], n_boot: int = BOOTSTRAP_N,
                 ci: float = BOOTSTRAP_CI, seed: int = BOOTSTRAP_SEED) -> Tuple[float, float]:
    if len(values) < 2:
        m = safe_mean(values)
        return m, m
    rng = random.Random(seed)
    n = len(values)
    means = []
    for _ in range(n_boot):
        sample = [values[rng.randint(0, n - 1)] for _ in range(n)]
        means.append(statistics.mean(sample))
    alpha = (1 - ci) / 2
    means.sort()
    lo = means[int(alpha * len(means))]
    hi = means[int((1 - alpha) * len(means))]
    return lo, hi


def analyze_task(episodes: List[Dict]) -> Dict:
    n = len(episodes)
    classifications = []
    for ep in episodes:
        int_score = ep["always_internal"]["final_score"]
        det_score = ep["always_deterministic"]["final_score"]
        label, reason, source = classify_episode(int_score, det_score)
        classifications.append({
            "label": label, "reason": reason, "source": source,
            "int_score": int_score, "det_score": det_score,
        })

    # Count signal sources
    source_counts = defaultdict(int)
    label_counts = defaultdict(int)
    for c in classifications:
        source_counts[c["source"]] += 1
        label_counts[c["label"]] += 1

    # Death rates
    int_deaths = sum(1 for ep in episodes if is_dead(ep["always_internal"]["final_score"]))
    det_deaths = sum(1 for ep in episodes if is_dead(ep["always_deterministic"]["final_score"]))

    # Score gaps
    all_gaps = [c["det_score"] - c["int_score"] for c in classifications]
    alive_gaps = [c["det_score"] - c["int_score"] for c in classifications
                  if not is_dead(c["int_score"]) and not is_dead(c["det_score"])]

    gap_mean = safe_mean(all_gaps)
    gap_alive_mean = safe_mean(alive_gaps)

    # DAF for this task
    det_pref = [c for c in classifications if c["label"] == "det-preferred"]
    if det_pref:
        delta_full = safe_mean([c["det_score"] - c["int_score"] for c in det_pref])
        det_pref_alive = [c for c in det_pref if not is_dead(c["int_score"])]
        delta_nd = safe_mean([c["det_score"] - c["int_score"] for c in det_pref_alive]) if det_pref_alive else 0.0
        daf = 1.0 - delta_nd / delta_full if delta_full != 0 else None
    else:
        daf = None
        delta_full = 0
        delta_nd = 0

    return {
        "n_episodes": n,
        "label_counts": dict(label_counts),
        "source_counts": dict(source_counts),
        "death_rate_internal": int_deaths / n if n else 0,
        "death_rate_deterministic": det_deaths / n if n else 0,
        "mean_gap_all": gap_mean,
        "mean_gap_alive": gap_alive_mean,
        "gap_ci": bootstrap_ci(all_gaps),
        "daf": daf,
        "delta_full": delta_full,
        "delta_nd": delta_nd,
    }


def main():
    parser = argparse.ArgumentParser(description="Death decomposition analysis")
    parser.add_argument("--data_dir", type=str, required=True,
                        help="Directory with {task_type}/episodes.jsonl")
    parser.add_argument("--output", type=str, default="results/decomposition")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    all_results = {}
    all_episodes = []

    for task_dir in sorted(os.listdir(args.data_dir)):
        ep_path = os.path.join(args.data_dir, task_dir, "episodes.jsonl")
        if not os.path.exists(ep_path):
            continue

        episodes = []
        with open(ep_path) as f:
            for line in f:
                if line.strip():
                    episodes.append(json.loads(line))

        if not episodes:
            continue

        result = analyze_task(episodes)
        all_results[task_dir] = result
        all_episodes.extend(episodes)
        print(f"{task_dir}: n={result['n_episodes']}, "
              f"death_int={result['death_rate_internal']:.2f}, "
              f"death_det={result['death_rate_deterministic']:.2f}, "
              f"DAF={result['daf']}")

    # Global analysis
    if all_episodes:
        global_result = analyze_task(all_episodes)
        all_results["_global"] = global_result
        print(f"\nGlobal: n={global_result['n_episodes']}, DAF={global_result['daf']}")

    # Save JSON
    with open(os.path.join(args.output, "decomposition_report.json"), "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    # Save CSV
    with open(os.path.join(args.output, "decomposition_summary.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "task_name", "n_episodes", "death_rate_int", "death_rate_det",
            "mean_gap", "daf", "n_det_pref", "n_int_pref", "n_no_pref",
        ])
        for task, r in sorted(all_results.items()):
            if task == "_global":
                continue
            writer.writerow([
                task, r["n_episodes"],
                f"{r['death_rate_internal']:.3f}",
                f"{r['death_rate_deterministic']:.3f}",
                f"{r['mean_gap_all']:.2f}",
                f"{r['daf']:.4f}" if r["daf"] is not None else "N/A",
                r["label_counts"].get("det-preferred", 0),
                r["label_counts"].get("internal-preferred", 0),
                r["label_counts"].get("no-preference", 0),
            ])

    print(f"\nSaved to {args.output}/")


if __name__ == "__main__":
    main()
