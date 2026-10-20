#!/usr/bin/env python3
"""Analyze seed replication results for FOLIO-204 with Mistral-7B, K=12.

Compares exp-052 (seed=123) and exp-053 (seed=456) against exp-033 (seed=42).
Reads from final results JSON if available, otherwise reconstructs from intermediates.

Input paths:
  - exp-052: results/exp052_mistral_folio204_seed123/
  - exp-053: results/exp053_mistral_folio204_seed456/
  - exp-033: results/exp033_mistral_7b_folio204/exp033_results.json (or hardcoded reference)

Output:
  - Console table comparing SC/SICA/delta/McNemar across seeds
  - results/seed_replication_summary.json

Usage:
  python scripts/analyze_seed_replication.py [--results-dir /path/to/results]
"""

import argparse
import json
import os
import sys
from collections import Counter
from pathlib import Path

try:
    from scipy.stats import binomtest
except ImportError:
    binomtest = None


VALID_ANSWERS = {"True", "False", "Unknown"}

EXP033_REFERENCE = {
    "seed": 42,
    "exp": "exp-033",
    "n": 204,
    "sc_pct": 54.41,
    "sica_pct": 59.31,
    "delta": 4.90,
    "b": 12,
    "c": 2,
    "p_value": 0.013,
    "source": "hardcoded",
}


def normalize_answer(ans):
    if not isinstance(ans, str):
        return None
    a = ans.strip().lower()
    if a in ("true", "yes"):
        return "True"
    if a in ("false", "no"):
        return "False"
    if a in ("unknown", "uncertain", "undetermined"):
        return "Unknown"
    return None


def load_results_json(path):
    with open(path) as f:
        data = json.load(f)
    results = []
    for r in data["results"]:
        results.append({
            "problem_id": r["problem_id"],
            "ground_truth": r["ground_truth"],
            "sica_answer": r.get("sica_answer"),
            "sica_correct": r.get("sica_correct"),
            "sc_answer": r.get("sc_answer"),
            "sc_correct": r.get("sc_correct"),
        })
    return results


def load_from_intermediates(intermediates_dir):
    results = []
    for fname in sorted(os.listdir(intermediates_dir)):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(intermediates_dir, fname)
        with open(fpath) as f:
            data = json.load(f)

        problem = data["problem"]
        gt = problem["answer"]
        sica_result = data["sica_result"]

        sica_scores = sica_result.get("scores", {})
        if sica_scores:
            sica_answer = max(sica_scores, key=sica_scores.get)
        else:
            sica_answer = sica_result.get("answer")

        answer_counts = sica_result.get("answer_counts", {})
        if answer_counts:
            sc_answer = max(answer_counts, key=answer_counts.get)
        else:
            sc_answer = sica_result.get("answer")

        norm_gt = normalize_answer(gt) or gt
        norm_sica = normalize_answer(sica_answer)
        norm_sc = normalize_answer(sc_answer)

        results.append({
            "problem_id": problem["id"],
            "ground_truth": norm_gt,
            "sica_answer": norm_sica or sica_answer,
            "sica_correct": (norm_sica == norm_gt) if norm_sica else False,
            "sc_answer": norm_sc or sc_answer,
            "sc_correct": (norm_sc == norm_gt) if norm_sc else False,
        })
    return results


def load_experiment(exp_dir, results_filename=None):
    if results_filename:
        results_path = os.path.join(exp_dir, results_filename)
        if os.path.exists(results_path):
            return load_results_json(results_path), "results_json"

    for fname in os.listdir(exp_dir):
        if fname.endswith("_results.json") or fname == "results.json":
            return load_results_json(os.path.join(exp_dir, fname)), "results_json"

    intermediates = os.path.join(exp_dir, "intermediates")
    if os.path.isdir(intermediates):
        return load_from_intermediates(intermediates), "intermediates"

    return [], "not_found"


def compute_stats(results):
    n = len(results)
    if n == 0:
        return None

    sc_correct = sum(1 for r in results if r["sc_correct"])
    sica_correct = sum(1 for r in results if r["sica_correct"])

    b = 0  # SICA correct, SC wrong
    c = 0  # SC correct, SICA wrong
    for r in results:
        if r["sica_correct"] and not r["sc_correct"]:
            b += 1
        elif r["sc_correct"] and not r["sica_correct"]:
            c += 1

    sc_pct = 100.0 * sc_correct / n
    sica_pct = 100.0 * sica_correct / n
    delta = sica_pct - sc_pct

    p_value = None
    if binomtest is not None and (b + c) > 0:
        result = binomtest(b, b + c, 0.5, alternative="two-sided")
        p_value = result.pvalue
    elif b + c > 0:
        from math import comb
        total = b + c
        k = min(b, c)
        p_val = 0.0
        for i in range(k + 1):
            p_val += comb(total, i) * (0.5 ** total)
        p_value = 2.0 * p_val
        p_value = min(p_value, 1.0)

    per_type = {}
    for answer_type in ["True", "False", "Unknown"]:
        subset = [r for r in results if r["ground_truth"] == answer_type]
        if subset:
            sc_c = sum(1 for r in subset if r["sc_correct"])
            sica_c = sum(1 for r in subset if r["sica_correct"])
            per_type[answer_type] = {
                "n": len(subset),
                "sc_correct": sc_c,
                "sc_pct": 100.0 * sc_c / len(subset),
                "sica_correct": sica_c,
                "sica_pct": 100.0 * sica_c / len(subset),
            }

    return {
        "n": n,
        "sc_correct": sc_correct,
        "sica_correct": sica_correct,
        "sc_pct": round(sc_pct, 2),
        "sica_pct": round(sica_pct, 2),
        "delta": round(delta, 2),
        "b": b,
        "c": c,
        "p_value": round(p_value, 4) if p_value is not None else None,
        "per_answer_type": per_type,
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze seed replication for FOLIO-204 Mistral-7B K=12")
    parser.add_argument("--results-dir", default="/root/symb_invariant_consensus/results",
                        help="Root results directory")
    args = parser.parse_args()

    results_dir = args.results_dir

    experiments = [
        {
            "seed": 123,
            "exp": "exp-052",
            "dir": os.path.join(results_dir, "exp052_mistral_folio204_seed123"),
            "results_file": "exp052_results.json",
        },
        {
            "seed": 456,
            "exp": "exp-053",
            "dir": os.path.join(results_dir, "exp053_mistral_folio204_seed456"),
            "results_file": "exp053_results.json",
        },
    ]

    exp033_path = os.path.join(results_dir, "exp033_mistral_7b_folio204", "exp033_results.json")
    exp033_alt = os.path.join(results_dir, "exp033_mistral_folio204", "exp033_results.json")

    exp033_stats = None
    for p in [exp033_path, exp033_alt]:
        if os.path.exists(p):
            results_033, src = load_experiment(os.path.dirname(p))
            if results_033:
                exp033_stats = compute_stats(results_033)
                exp033_stats["seed"] = 42
                exp033_stats["exp"] = "exp-033"
                exp033_stats["source"] = src
                break

    if exp033_stats is None:
        exp033_stats = dict(EXP033_REFERENCE)
        exp033_stats["per_answer_type"] = {}

    all_rows = [exp033_stats]

    for exp in experiments:
        if not os.path.isdir(exp["dir"]):
            print(f"WARNING: {exp['dir']} not found, skipping {exp['exp']}", file=sys.stderr)
            continue
        results, source = load_experiment(exp["dir"], exp["results_file"])
        if not results:
            print(f"WARNING: No results found for {exp['exp']}", file=sys.stderr)
            continue
        stats = compute_stats(results)
        stats["seed"] = exp["seed"]
        stats["exp"] = exp["exp"]
        stats["source"] = source
        all_rows.append(stats)

    print()
    print("Seed Replication Summary (FOLIO-204, Mistral-7B, K=12)")
    print("=" * 80)
    header = f"{'Seed':>12} | {'Exp':>8} | {'n':>5} | {'SC%':>7} | {'SICA%':>7} | {'delta':>7} | {'b':>3} | {'c':>3} | {'p-value':>8} | {'src':>12}"
    print(header)
    print("-" * 80)
    for row in all_rows:
        p_str = f"{row['p_value']:.4f}" if row.get("p_value") is not None else "N/A"
        delta_str = f"+{row['delta']:.2f}" if row["delta"] >= 0 else f"{row['delta']:.2f}"
        src = row.get("source", "")
        print(f"{row['seed']:>12} | {row['exp']:>8} | {row['n']:>5} | {row['sc_pct']:>7.2f} | {row['sica_pct']:>7.2f} | {delta_str:>7} | {row['b']:>3} | {row['c']:>3} | {p_str:>8} | {src:>12}")

    print()
    print("Per Answer Type Breakdown:")
    print("-" * 80)
    for row in all_rows:
        pat = row.get("per_answer_type", {})
        if not pat:
            print(f"  Seed {row['seed']} ({row['exp']}): no per-type data")
            continue
        print(f"  Seed {row['seed']} ({row['exp']}):")
        for atype in ["True", "False", "Unknown"]:
            if atype in pat:
                t = pat[atype]
                print(f"    {atype:>8}: n={t['n']:>3}, SC={t['sc_pct']:>6.2f}% ({t['sc_correct']}/{t['n']}), SICA={t['sica_pct']:>6.2f}% ({t['sica_correct']}/{t['n']})")

    output = {
        "description": "Seed replication analysis for FOLIO-204, Mistral-7B, K=12",
        "seeds": []
    }
    for row in all_rows:
        entry = {k: v for k, v in row.items()}
        if "per_answer_type" in entry:
            for atype, vals in entry["per_answer_type"].items():
                vals["sc_pct"] = round(vals["sc_pct"], 2)
                vals["sica_pct"] = round(vals["sica_pct"], 2)
        output["seeds"].append(entry)

    out_path = os.path.join(results_dir, "seed_replication_summary.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
