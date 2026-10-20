#!/usr/bin/env python3
"""Entropy-Gated Adaptive SICA Validation.

For each experiment, computes Shannon entropy from SC vote distributions,
splits problems into low/high entropy groups, and constructs Adaptive SICA
(SC for low-entropy, SICA for high-entropy). Validates whether Adaptive SICA
consistently >= SC across all experiments.
"""

import json
import math
import os
import sys
from collections import Counter

RESULTS_BASE = "/root/symb_invariant_consensus/results"

EXPERIMENTS = [
    # (exp_id, model, dataset, relative_path_to_results_json)
    ("exp-033", "Mistral-7B", "FOLIO-204", "exp033_mistral_7b_folio204/exp033_results.json"),
    ("exp-001/026", "Qwen2.5-14B", "FOLIO-204", "folio_204_14b/folio_204_results.json"),
    ("exp-027", "Qwen3-14B-NT", "FOLIO-204", "exp027_qwen3_14b_nonthinking/exp027_results.json"),
    ("exp-035", "Qwen2.5-7B", "FOLIO-204", "exp035_qwen25_7b_folio204/exp035_results.json"),
    ("exp-044b", "Qwen2.5-14B", "FOLIO-199-ICL", "exp044b_icl_oracle_qwen14b/results.json"),
    ("exp-050b", "Mistral-7B", "FOLIO-199-ICL", "exp050b_mistral_icl_oracle/exp050b_results.json"),
    ("exp-046", "Mistral-7B", "PW-600", "exp046_mistral_7b_pw600/exp046_results.json"),
    ("exp-034-pw", "Qwen2.5-14B", "PW-600", "exp034_qwen25_14b_proofwriter/exp034_results.json"),
    ("exp-028b", "Qwen3-14B-T", "FOLIO-204", "exp028b_qwen3_thinking_folio204/exp028b_results.json"),
    ("exp-052", "Mistral-7B", "FOLIO-204-s123", "exp052_mistral_folio204_seed123/exp052_results.json"),
    ("exp-053", "Mistral-7B", "FOLIO-204-s456", "exp053_mistral_folio204_seed456/exp053_results.json"),
    ("exp-038", "Qwen2.5-14B", "LogiQA-200", "exp038_qwen25_14b_logiqa200/results.json"),
    ("exp-049b", "Mistral-7B", "LogiQA-200", "exp049b_mistral_logiqa200/exp049b_results.json"),
    ("exp-041", "Qwen2.5-14B", "FOLIO-204", "exp036_qwen25_14b_folio204/results.json"),
    ("exp-032", "Qwen2.5-14B", "PW-600", "exp032_qwen25_14b_pw600/results.json"),
    ("exp-033-pw", "Qwen3-14B-NT", "PW-600", "exp033_qwen3_14b_pw600_nonthinking/results.json"),
    # K-sensitivity
    ("exp-051-k4", "Mistral-7B", "FOLIO-204-k4", "exp051_mistral_k_sensitivity/k4/results.json"),
    ("exp-051-k8", "Mistral-7B", "FOLIO-204-k8", "exp051_mistral_k_sensitivity/k8/results.json"),
    ("exp-051-k16", "Mistral-7B", "FOLIO-204-k16", "exp051_mistral_k_sensitivity/k16/results.json"),
]

ENTROPY_THRESHOLD = 1.0


def answer_entropy(vote_distribution):
    """Compute Shannon entropy (bits) from vote distribution dict."""
    total = sum(vote_distribution.values())
    if total == 0:
        return 0.0
    H = 0.0
    for count in vote_distribution.values():
        if count > 0:
            p = count / total
            H -= p * math.log2(p)
    return H


def analyze_experiment(results_path):
    """Analyze a single experiment file. Returns dict with results or None."""
    if not os.path.exists(results_path):
        return None

    with open(results_path) as f:
        data = json.load(f)

    if isinstance(data, dict) and "results" in data:
        problems = data["results"]
    elif isinstance(data, list):
        problems = data
    else:
        return None

    if not problems:
        return None

    n = len(problems)
    sc_correct_total = 0
    sica_correct_total = 0
    adaptive_correct_total = 0
    n_low = 0
    n_high = 0

    per_problem = []

    for p in problems:
        vote_dist = p.get("sc_vote_distribution", {})
        gt = p.get("ground_truth")
        sc_ans = p.get("sc_answer")
        sica_ans = p.get("sica_answer")
        sc_ok = p.get("sc_correct", sc_ans == gt)
        sica_ok = p.get("sica_correct", sica_ans == gt)

        H = answer_entropy(vote_dist)

        if H < ENTROPY_THRESHOLD:
            n_low += 1
            adaptive_ans = sc_ans
            adaptive_ok = sc_ok
        else:
            n_high += 1
            adaptive_ans = sica_ans
            adaptive_ok = sica_ok

        sc_correct_total += int(sc_ok)
        sica_correct_total += int(sica_ok)
        adaptive_correct_total += int(adaptive_ok)

        per_problem.append({
            "problem_id": p.get("problem_id", p.get("problem_idx")),
            "entropy": round(H, 4),
            "group": "low" if H < ENTROPY_THRESHOLD else "high",
            "sc_correct": sc_ok,
            "sica_correct": sica_ok,
            "adaptive_correct": adaptive_ok,
            "ground_truth": gt,
            "sc_answer": sc_ans,
            "sica_answer": sica_ans,
        })

    return {
        "n": n,
        "n_low": n_low,
        "n_high": n_high,
        "sc_correct": sc_correct_total,
        "sica_correct": sica_correct_total,
        "adaptive_correct": adaptive_correct_total,
        "sc_acc": round(100 * sc_correct_total / n, 2),
        "sica_acc": round(100 * sica_correct_total / n, 2),
        "adaptive_acc": round(100 * adaptive_correct_total / n, 2),
        "delta_adaptive_sc": round(100 * (adaptive_correct_total - sc_correct_total) / n, 2),
        "per_problem": per_problem,
    }


def main():
    print(f"Adaptive SICA Validation (entropy threshold = {ENTROPY_THRESHOLD} bit)")
    print(f"{'='*120}")

    header = f"| {'Experiment':<14} | {'Model':<14} | {'Dataset':<16} | {'n':>4} | {'n_low':>5} | {'n_high':>5} | {'SC%':>6} | {'SICA%':>6} | {'Adaptive%':>9} | {'D(A-SC)':>8} |"
    sep = f"|{'-'*16}|{'-'*16}|{'-'*18}|{'-'*6}|{'-'*7}|{'-'*7}|{'-'*8}|{'-'*8}|{'-'*11}|{'-'*10}|"

    print(header)
    print(sep)

    all_results = {}
    n_better = 0
    n_equal = 0
    n_worse = 0
    total_found = 0

    for exp_id, model, dataset, rel_path in EXPERIMENTS:
        full_path = os.path.join(RESULTS_BASE, rel_path)
        result = analyze_experiment(full_path)
        if result is None:
            continue

        total_found += 1
        r = result
        delta = r["delta_adaptive_sc"]
        if delta > 0:
            n_better += 1
            flag = "+"
        elif delta == 0:
            n_equal += 1
            flag = "="
        else:
            n_worse += 1
            flag = "!!WORSE!!"

        row = f"| {exp_id:<14} | {model:<14} | {dataset:<16} | {r['n']:>4} | {r['n_low']:>5} | {r['n_high']:>5} | {r['sc_acc']:>6} | {r['sica_acc']:>6} | {r['adaptive_acc']:>9} | {delta:>+7.2f}{flag} |"
        print(row)

        all_results[exp_id] = {
            "model": model,
            "dataset": dataset,
            "n": r["n"],
            "n_low": r["n_low"],
            "n_high": r["n_high"],
            "sc_acc": r["sc_acc"],
            "sica_acc": r["sica_acc"],
            "adaptive_acc": r["adaptive_acc"],
            "delta_adaptive_sc": delta,
        }

    print(sep)
    print()
    print("Summary:")
    print(f"  Experiments found: {total_found}")
    print(f"  Adaptive SICA > SC:  {n_better}/{total_found}")
    print(f"  Adaptive SICA = SC:  {n_equal}/{total_found}")
    print(f"  Adaptive SICA < SC:  {n_worse}/{total_found}  {'(MUST BE 0!)' if n_worse > 0 else '(OK)'}")
    print()

    if n_worse > 0:
        print("*** WARNING: Adaptive SICA is WORSE than SC in some experiments! ***")
        print("*** The method does NOT consistently improve over SC. ***")
    else:
        print("Adaptive SICA consistently >= SC across all experiments.")

    # Also print entropy distribution analysis
    print()
    print("Entropy Group Analysis (high-entropy subset only):")
    print(f"| {'Experiment':<14} | {'n_high':>5} | {'SC_high%':>8} | {'SICA_high%':>10} | {'D(SICA-SC)':>10} |")
    print(f"|{'-'*16}|{'-'*7}|{'-'*10}|{'-'*12}|{'-'*12}|")

    for exp_id, model, dataset, rel_path in EXPERIMENTS:
        full_path = os.path.join(RESULTS_BASE, rel_path)
        result = analyze_experiment(full_path)
        if result is None:
            continue
        high_problems = [p for p in result["per_problem"] if p["group"] == "high"]
        if not high_problems:
            continue
        sc_high = sum(1 for p in high_problems if p["sc_correct"])
        sica_high = sum(1 for p in high_problems if p["sica_correct"])
        n_h = len(high_problems)
        sc_pct = round(100 * sc_high / n_h, 2)
        sica_pct = round(100 * sica_high / n_h, 2)
        delta_h = round(sica_pct - sc_pct, 2)
        print(f"| {exp_id:<14} | {n_h:>5} | {sc_pct:>8} | {sica_pct:>10} | {delta_h:>+10.2f} |")

    # Also sweep thresholds
    print()
    print("Threshold Sensitivity (fraction of experiments where Adaptive >= SC):")
    for thresh in [0.5, 0.75, 1.0, 1.25, 1.5]:
        wins = 0
        ties = 0
        losses = 0
        found = 0
        for exp_id, model, dataset, rel_path in EXPERIMENTS:
            full_path = os.path.join(RESULTS_BASE, rel_path)
            if not os.path.exists(full_path):
                continue
            with open(full_path) as f:
                data = json.load(f)
            problems = data["results"] if isinstance(data, dict) and "results" in data else data
            if not problems:
                continue
            found += 1
            sc_c = 0
            ad_c = 0
            for p in problems:
                vd = p.get("sc_vote_distribution", {})
                H = answer_entropy(vd)
                sc_ok = p.get("sc_correct", p.get("sc_answer") == p.get("ground_truth"))
                sica_ok = p.get("sica_correct", p.get("sica_answer") == p.get("ground_truth"))
                sc_c += int(sc_ok)
                if H < thresh:
                    ad_c += int(sc_ok)
                else:
                    ad_c += int(sica_ok)
            delta = ad_c - sc_c
            if delta > 0:
                wins += 1
            elif delta == 0:
                ties += 1
            else:
                losses += 1
        print(f"  threshold={thresh:.2f}: {wins} better, {ties} equal, {losses} worse (of {found})")

    # Save JSON
    output_path = os.path.join(RESULTS_BASE, "adaptive_sica_validation.json")
    with open(output_path, "w") as f:
        json.dump({
            "entropy_threshold": ENTROPY_THRESHOLD,
            "summary": {
                "total_experiments": total_found,
                "adaptive_better": n_better,
                "adaptive_equal": n_equal,
                "adaptive_worse": n_worse,
            },
            "experiments": all_results,
        }, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
