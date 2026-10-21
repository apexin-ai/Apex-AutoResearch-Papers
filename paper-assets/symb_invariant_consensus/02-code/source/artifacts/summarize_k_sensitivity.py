#!/usr/bin/env python3
"""Summarize K sensitivity results from exp-051 (Mistral-7B, FOLIO-204, T=0.7).

Scans k4/, k8/, k16/, k20/ subdirectories and computes SC, SICA, delta,
discordant pairs, McNemar p-value for each K. Includes K=12 reference from exp-033.

Input:
  results/exp051_mistral_k_sensitivity/ (with k4/, k8/, k16/, k20/ subdirs)
  results/exp033_mistral_7b_folio204/exp033_results.json (optional, for K=12 reference)

Output:
  - Console table comparing all K values
  - results/k_sensitivity_summary.json

Usage:
  python scripts/summarize_k_sensitivity.py [--results-dir /path/to/results]
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from scipy.stats import binomtest
except ImportError:
    binomtest = None


VALID_ANSWERS = {"True", "False", "Unknown"}

K12_REFERENCE = {
    "k": 12,
    "n": 204,
    "sc_pct": 54.41,
    "sica_pct": 59.31,
    "delta": 4.90,
    "b": 12,
    "c": 2,
    "p_value": 0.013,
    "status": "done (exp-033)",
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
            "sica_correct": r.get("sica_correct"),
            "sc_correct": r.get("sc_correct"),
        })
    k = data.get("summary", {}).get("k")
    return results, k


def load_intermediate(fpath):
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

    return {
        "problem_id": problem["id"],
        "ground_truth": norm_gt,
        "sica_correct": (norm_sica == norm_gt) if norm_sica else False,
        "sc_correct": (norm_sc == norm_gt) if norm_sc else False,
    }


def load_from_intermediates(intermediates_dir):
    results = []
    for fname in sorted(os.listdir(intermediates_dir)):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(intermediates_dir, fname)
        results.append(load_intermediate(fpath))
    return results


def load_k_dir(k_dir):
    results_json = os.path.join(k_dir, "results.json")
    intermediates = os.path.join(k_dir, "intermediates")

    if os.path.exists(results_json):
        results, k = load_results_json(results_json)
        n_total = len(results)

        if os.path.isdir(intermediates):
            n_intermediates = len([f for f in os.listdir(intermediates) if f.endswith(".json")])
        else:
            n_intermediates = n_total

        status = "done" if n_total >= 204 else f"running ({n_total}/204)"
        return results, status

    if os.path.isdir(intermediates):
        files = [f for f in os.listdir(intermediates) if f.endswith(".json")]
        if files:
            results = load_from_intermediates(intermediates)
            status = f"running ({len(results)}/204)"
            return results, status

    return [], "pending"


def compute_mcnemar_p(b, c):
    if b + c == 0:
        return None
    if binomtest is not None:
        return binomtest(b, b + c, 0.5, alternative="two-sided").pvalue
    from math import comb
    total = b + c
    k = min(b, c)
    p_val = 0.0
    for i in range(k + 1):
        p_val += comb(total, i) * (0.5 ** total)
    return min(2.0 * p_val, 1.0)


def compute_stats(results):
    n = len(results)
    if n == 0:
        return None

    sc_correct = sum(1 for r in results if r["sc_correct"])
    sica_correct = sum(1 for r in results if r["sica_correct"])

    b = sum(1 for r in results if r["sica_correct"] and not r["sc_correct"])
    c = sum(1 for r in results if r["sc_correct"] and not r["sica_correct"])

    sc_pct = 100.0 * sc_correct / n
    sica_pct = 100.0 * sica_correct / n
    delta = sica_pct - sc_pct

    p_value = compute_mcnemar_p(b, c)

    return {
        "n": n,
        "sc_pct": round(sc_pct, 2),
        "sica_pct": round(sica_pct, 2),
        "delta": round(delta, 2),
        "b": b,
        "c": c,
        "p_value": round(p_value, 4) if p_value is not None else None,
    }


def main():
    parser = argparse.ArgumentParser(description="Summarize K sensitivity (exp-051, Mistral-7B, FOLIO-204)")
    parser.add_argument("--results-dir", default="/root/symb_invariant_consensus/results",
                        help="Root results directory")
    args = parser.parse_args()

    results_dir = args.results_dir
    k_sens_dir = os.path.join(results_dir, "exp051_mistral_k_sensitivity")

    if not os.path.isdir(k_sens_dir):
        print(f"ERROR: {k_sens_dir} not found", file=sys.stderr)
        sys.exit(1)

    k_values = [4, 8, 12, 16, 20]
    rows = []

    for k in k_values:
        if k == 12:
            exp033_path = os.path.join(results_dir, "exp033_mistral_7b_folio204", "exp033_results.json")
            exp033_alt = os.path.join(results_dir, "exp033_mistral_folio204", "exp033_results.json")

            loaded = False
            for p in [exp033_path, exp033_alt]:
                if os.path.exists(p):
                    results, _ = load_results_json(p)
                    stats = compute_stats(results)
                    stats["k"] = 12
                    stats["status"] = "done (exp-033)"
                    stats["source"] = "exp033_results.json"
                    rows.append(stats)
                    loaded = True
                    break

            if not loaded:
                rows.append(dict(K12_REFERENCE))
            continue

        k_dir = os.path.join(k_sens_dir, f"k{k}")
        if not os.path.isdir(k_dir):
            rows.append({
                "k": k, "n": 0, "sc_pct": 0, "sica_pct": 0,
                "delta": 0, "b": 0, "c": 0, "p_value": None,
                "status": "pending", "source": "not_found",
            })
            continue

        results, status = load_k_dir(k_dir)
        if not results:
            rows.append({
                "k": k, "n": 0, "sc_pct": 0, "sica_pct": 0,
                "delta": 0, "b": 0, "c": 0, "p_value": None,
                "status": status, "source": "empty",
            })
            continue

        stats = compute_stats(results)
        stats["k"] = k
        stats["status"] = status
        stats["source"] = "results.json" if os.path.exists(os.path.join(k_dir, "results.json")) else "intermediates"
        rows.append(stats)

    print()
    print("K Sensitivity (FOLIO-204, Mistral-7B, T=0.7)")
    print("=" * 100)
    header = f"{'K':>4} | {'n':>5} | {'SC%':>7} | {'SICA%':>7} | {'delta':>7} | {'b':>3} | {'c':>3} | {'p-value':>8} | {'status':>20}"
    print(header)
    print("-" * 100)

    for row in rows:
        p_str = f"{row['p_value']:.4f}" if row.get("p_value") is not None else "N/A"
        delta_str = f"+{row['delta']:.2f}" if row["delta"] >= 0 else f"{row['delta']:.2f}"
        n_str = str(row["n"]) if row["n"] > 0 else "-"
        sc_str = f"{row['sc_pct']:.2f}" if row["n"] > 0 else "-"
        sica_str = f"{row['sica_pct']:.2f}" if row["n"] > 0 else "-"
        delta_str = delta_str if row["n"] > 0 else "-"
        b_str = str(row["b"]) if row["n"] > 0 else "-"
        c_str = str(row["c"]) if row["n"] > 0 else "-"
        p_str = p_str if row["n"] > 0 else "-"
        print(f"{row['k']:>4} | {n_str:>5} | {sc_str:>7} | {sica_str:>7} | {delta_str:>7} | {b_str:>3} | {c_str:>3} | {p_str:>8} | {row['status']:>20}")

    print()

    output = {
        "description": "K sensitivity analysis for FOLIO-204, Mistral-7B, T=0.7",
        "k_values": rows,
    }

    out_path = os.path.join(results_dir, "k_sensitivity_summary.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()
