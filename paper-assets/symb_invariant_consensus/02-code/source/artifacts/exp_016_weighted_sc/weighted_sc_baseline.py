#!/usr/bin/env python3
"""exp-016: Weighted Self-Consistency Baselines

Implements 4 weighted voting methods on exp-001 (sica_expanded_14b) data:
  1. Uniform (= standard SC majority vote)
  2. Length-weighted (weight = trace_len)
  3. Inverse-length-weighted (weight = 1/trace_len)
  4. Constraint-count-weighted (weight = trace_len as proxy; per-trace
     constraint counts were not stored in exp-001)

Input:  results/sica_expanded_14b.json
Output: results/weighted_sc_results.json
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path


def weighted_vote(traces: list[dict], weight_fn) -> str:
    """Return the answer with highest total weight. Ties broken alphabetically."""
    scores: dict[str, float] = defaultdict(float)
    for t in traces:
        w = weight_fn(t)
        scores[t["answer"]] += w
    if not scores:
        return ""
    max_score = max(scores.values())
    winners = sorted(k for k, v in scores.items() if v == max_score)
    return winners[0]


METHODS = {
    "uniform": lambda t: 1.0,
    "length_weighted": lambda t: t["trace_len"],
    "inv_length_weighted": lambda t: 1.0 / max(t["trace_len"], 1),
    "constraint_count_weighted": lambda t: t["trace_len"],  # proxy
}


def mcnemar_test(a_correct: list[bool], b_correct: list[bool]) -> dict:
    """Two-sided McNemar test. Returns chi2, p-value, and contingency counts."""
    n01 = sum(1 for a, b in zip(a_correct, b_correct) if a and not b)
    n10 = sum(1 for a, b in zip(a_correct, b_correct) if not a and b)
    n00 = sum(1 for a, b in zip(a_correct, b_correct) if not a and not b)
    n11 = sum(1 for a, b in zip(a_correct, b_correct) if a and b)
    denom = n01 + n10
    if denom == 0:
        chi2, p = 0.0, 1.0
    else:
        chi2 = (abs(n01 - n10) - 1) ** 2 / denom  # continuity correction
        try:
            from scipy.stats import chi2 as chi2_dist
            p = 1 - chi2_dist.cdf(chi2, df=1)
        except ImportError:
            p = math.exp(-chi2 / 2) if chi2 < 30 else 0.0  # rough approx
    return {
        "n11": n11, "n01": n01, "n10": n10, "n00": n00,
        "chi2": round(chi2, 4), "p_value": round(p, 6),
    }


def run(data_path: str, output_path: str):
    with open(data_path) as f:
        data = json.load(f)

    results_list = data["results"]
    n = len(results_list)
    print(f"Loaded {n} problems from {data_path}")

    # Reference accuracies from the file
    ref_sica_acc = data["summary"]["sica_accuracy"]
    ref_sc_acc = data["summary"]["sc_accuracy"]
    print(f"Reference: SICA={ref_sica_acc:.4f}, SC={ref_sc_acc:.4f}")

    # Per-method results
    method_results = {}
    method_correct = {}

    for method_name, weight_fn in METHODS.items():
        per_problem = []
        correct_flags = []
        for r in results_list:
            traces = r["per_trace"]
            pred = weighted_vote(traces, weight_fn)
            is_correct = pred == r["ground_truth"]
            per_problem.append({
                "problem_idx": r["problem_idx"],
                "problem_id": r["problem_id"],
                "dataset": r.get("dataset", ""),
                "ground_truth": r["ground_truth"],
                "predicted": pred,
                "correct": is_correct,
            })
            correct_flags.append(is_correct)

        acc = sum(correct_flags) / n
        n_correct = sum(correct_flags)

        # Per-dataset breakdown
        ds_stats = defaultdict(lambda: {"correct": 0, "total": 0})
        for p in per_problem:
            ds = p["dataset"] or "unknown"
            ds_stats[ds]["total"] += 1
            if p["correct"]:
                ds_stats[ds]["correct"] += 1
        per_dataset = {
            ds: {"accuracy": s["correct"] / s["total"], "n": s["total"]}
            for ds, s in ds_stats.items()
        }

        method_results[method_name] = {
            "accuracy": round(acc, 6),
            "n_correct": n_correct,
            "n_total": n,
            "per_dataset": per_dataset,
            "per_problem": per_problem,
        }
        method_correct[method_name] = correct_flags
        print(f"  {method_name:30s}: {acc:.4f} ({n_correct}/{n})")

    # SICA correct flags
    sica_correct = [r["sica_correct"] for r in results_list]
    sc_correct = [r["sc_correct"] for r in results_list]

    # McNemar tests
    print("\n--- McNemar tests ---")
    comparisons = []
    for method_name in METHODS:
        mc = method_correct[method_name]
        # vs SC
        test_vs_sc = mcnemar_test(mc, sc_correct)
        test_vs_sica = mcnemar_test(mc, sica_correct)
        comp = {
            "method": method_name,
            "vs_sc": test_vs_sc,
            "vs_sica": test_vs_sica,
        }
        comparisons.append(comp)
        print(f"  {method_name} vs SC:   chi2={test_vs_sc['chi2']:.4f}, p={test_vs_sc['p_value']:.4f}")
        print(f"  {method_name} vs SICA: chi2={test_vs_sica['chi2']:.4f}, p={test_vs_sica['p_value']:.4f}")

    # Sanity: uniform should match SC
    uniform_acc = method_results["uniform"]["accuracy"]
    sc_acc_computed = sum(sc_correct) / n
    print(f"\nSanity check: uniform={uniform_acc:.6f}, SC(computed)={sc_acc_computed:.6f}", end="")
    if abs(uniform_acc - sc_acc_computed) < 1e-9:
        print(" ✓ MATCH")
    else:
        print(f" ✗ MISMATCH (delta={uniform_acc - sc_acc_computed:.6f})")

    # Check if length_weighted == constraint_count_weighted
    lw_acc = method_results["length_weighted"]["accuracy"]
    cc_acc = method_results["constraint_count_weighted"]["accuracy"]
    print(f"Length-weighted vs Constraint-count: {lw_acc:.6f} vs {cc_acc:.6f}", end="")
    if abs(lw_acc - cc_acc) < 1e-9:
        print(" (identical, as expected: trace_len is only available proxy)")
    else:
        print(" (differ — unexpected)")

    # Trace length statistics
    all_lens = []
    for r in results_list:
        for t in r["per_trace"]:
            all_lens.append(t["trace_len"])
    all_lens.sort()
    print(f"\nTrace length stats (n={len(all_lens)}):")
    print(f"  min={all_lens[0]}, median={all_lens[len(all_lens)//2]}, "
          f"max={all_lens[-1]}, mean={sum(all_lens)/len(all_lens):.0f}")

    # Output
    output = {
        "experiment": "exp-016",
        "description": "Weighted Self-Consistency Baselines",
        "n_problems": n,
        "reference": {
            "sica_accuracy": ref_sica_acc,
            "sc_accuracy": ref_sc_acc,
        },
        "methods": {
            name: {
                "accuracy": mr["accuracy"],
                "n_correct": mr["n_correct"],
                "n_total": mr["n_total"],
                "per_dataset": mr["per_dataset"],
            }
            for name, mr in method_results.items()
        },
        "mcnemar_tests": comparisons,
        "notes": {
            "constraint_count_weighted": (
                "Per-trace constraint counts were not stored in exp-001. "
                "trace_len (char count) is used as proxy. This makes "
                "constraint_count_weighted identical to length_weighted."
            ),
            "tie_breaking": "Alphabetical (same as SC baseline).",
        },
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults written to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="exp-016: Weighted SC Baselines")
    parser.add_argument("--data-dir", default="results",
                        help="Directory containing sica_expanded_14b.json")
    parser.add_argument("--output", default="results/weighted_sc_results.json",
                        help="Output JSON path")
    args = parser.parse_args()

    data_path = Path(args.data_dir) / "sica_expanded_14b.json"
    if not data_path.exists():
        print(f"ERROR: {data_path} not found", file=sys.stderr)
        sys.exit(1)

    run(str(data_path), args.output)


if __name__ == "__main__":
    main()
