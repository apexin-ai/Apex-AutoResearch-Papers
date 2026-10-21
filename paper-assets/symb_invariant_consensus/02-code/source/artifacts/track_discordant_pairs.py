#!/usr/bin/env python3
"""Track discordant pairs cumulative curve for exp-028b (Qwen3-14B thinking mode).

Reads intermediates or final results from exp-028b, computes running SC vs SICA
discordant pairs, override precision, and cumulative delta.

Input:
  results/exp028b_qwen3_thinking_folio204/ (intermediates/ or exp028b_results.json)

Output:
  - Console table: every 10 problems, cumulative stats
  - results/exp028b_discordant_tracking.json

Usage:
  python scripts/track_discordant_pairs.py [--results-dir /path/to/results]
"""

import argparse
import json
import os
import sys
from pathlib import Path


VALID_ANSWERS = {"True", "False", "Unknown"}


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
            "problem_idx": r.get("problem_idx", 0),
            "ground_truth": r["ground_truth"],
            "sica_correct": r.get("sica_correct"),
            "sc_correct": r.get("sc_correct"),
        })
    return results


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


def load_from_intermediates_ordered(intermediates_dir):
    files = []
    for fname in os.listdir(intermediates_dir):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(intermediates_dir, fname)
        mtime = os.path.getmtime(fpath)
        files.append((mtime, fname, fpath))

    files.sort(key=lambda x: x[0])

    results = []
    for _, fname, fpath in files:
        r = load_intermediate(fpath)
        results.append(r)
    return results


def main():
    parser = argparse.ArgumentParser(description="Track discordant pairs for exp-028b")
    parser.add_argument("--results-dir", default="/root/symb_invariant_consensus/results",
                        help="Root results directory")
    parser.add_argument("--exp-dir", default=None,
                        help="Direct path to exp-028b directory")
    args = parser.parse_args()

    if args.exp_dir:
        exp_dir = args.exp_dir
    else:
        candidates = [
            os.path.join(args.results_dir, "exp028b_qwen3_thinking_folio204"),
            os.path.join(args.results_dir, "exp028b_qwen3_14b_thinking_folio204"),
        ]
        exp_dir = None
        for c in candidates:
            if os.path.isdir(c):
                exp_dir = c
                break
        if exp_dir is None:
            print(f"ERROR: exp-028b directory not found. Tried: {candidates}", file=sys.stderr)
            sys.exit(1)

    intermediates = os.path.join(exp_dir, "intermediates")
    results_json = None
    for fname in os.listdir(exp_dir):
        if fname.endswith("_results.json") or fname == "results.json":
            results_json = os.path.join(exp_dir, fname)
            break

    if os.path.isdir(intermediates) and os.listdir(intermediates):
        print(f"Loading from intermediates: {intermediates}")
        results = load_from_intermediates_ordered(intermediates)
    elif results_json:
        print(f"Loading from results JSON: {results_json}")
        results = load_results_json(results_json)
    else:
        print("ERROR: No data found", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(results)} problems\n")

    cumulative_data = []
    sc_cum = 0
    sica_cum = 0
    b_cum = 0
    c_cum = 0

    for i, r in enumerate(results):
        if r["sc_correct"]:
            sc_cum += 1
        if r["sica_correct"]:
            sica_cum += 1
        if r["sica_correct"] and not r["sc_correct"]:
            b_cum += 1
        elif r["sc_correct"] and not r["sica_correct"]:
            c_cum += 1

        n = i + 1
        sc_pct = 100.0 * sc_cum / n
        sica_pct = 100.0 * sica_cum / n
        delta = sica_pct - sc_pct
        precision = b_cum / (b_cum + c_cum) if (b_cum + c_cum) > 0 else 0.0

        cumulative_data.append({
            "n": n,
            "problem_id": r["problem_id"],
            "sc_cum": sc_cum,
            "sica_cum": sica_cum,
            "sc_pct": round(sc_pct, 2),
            "sica_pct": round(sica_pct, 2),
            "delta": round(delta, 2),
            "b_cum": b_cum,
            "c_cum": c_cum,
            "precision": round(precision, 4),
        })

    print("Discordant Pairs Cumulative Tracking (exp-028b, Qwen3-14B Thinking, FOLIO-204)")
    print("=" * 95)
    header = f"{'n':>5} | {'SC_cum':>7} | {'SICA_cum':>8} | {'SC%':>7} | {'SICA%':>7} | {'delta':>7} | {'b_cum':>5} | {'c_cum':>5} | {'prec':>6}"
    print(header)
    print("-" * 95)

    for entry in cumulative_data:
        n = entry["n"]
        if n % 10 == 0 or n == len(results):
            delta_str = f"+{entry['delta']:.2f}" if entry["delta"] >= 0 else f"{entry['delta']:.2f}"
            print(f"{entry['n']:>5} | {entry['sc_cum']:>7} | {entry['sica_cum']:>8} | {entry['sc_pct']:>7.2f} | {entry['sica_pct']:>7.2f} | {delta_str:>7} | {entry['b_cum']:>5} | {entry['c_cum']:>5} | {entry['precision']:>6.4f}")

    final = cumulative_data[-1]
    total_disc = final["b_cum"] + final["c_cum"]
    rate = final["n"] / total_disc if total_disc > 0 else float("inf")

    print()
    print(f"Total problems: {final['n']}")
    print(f"Total discordant pairs: {total_disc} (b={final['b_cum']}, c={final['c_cum']})")
    print(f"Discordant rate: 1 per {rate:.1f} problems")
    print(f"Override precision (b/(b+c)): {final['precision']:.4f}")
    print(f"Final delta: {'+' if final['delta'] >= 0 else ''}{final['delta']:.2f}pp")

    output = {
        "experiment": "exp-028b",
        "model": "Qwen3-14B (thinking mode)",
        "dataset": "FOLIO-204",
        "k": 12,
        "total_problems": final["n"],
        "final_sc_pct": final["sc_pct"],
        "final_sica_pct": final["sica_pct"],
        "final_delta": final["delta"],
        "total_discordant": total_disc,
        "b_total": final["b_cum"],
        "c_total": final["c_cum"],
        "override_precision": final["precision"],
        "discordant_rate": round(rate, 2),
        "cumulative_curve": cumulative_data,
    }

    out_path = os.path.join(args.results_dir, "exp028b_discordant_tracking.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
