"""
exp-d126-70b-sica post-processing: extended metrics for Qwen2.5-72B SICA on FOLIO-204.
Input: results.json from run_full_mvp.py + intermediates/
Output: metrics.json with McNemar, Fleiss' kappa, Eff-K, Bias Ratio, constraint stats
"""
from __future__ import annotations

import argparse
import json
import os
import glob
import sys
import numpy as np
from scipy.stats import binomtest
from collections import Counter

FOLIO_CATEGORIES = ['True', 'False', 'Unknown']
K_NOMINAL = 12


def normalize_answer(ans):
    if not ans:
        return ""
    a = str(ans).strip().lower()
    mapping = {"true": "True", "false": "False", "unknown": "Unknown",
               "proved": "True", "disproved": "False"}
    return mapping.get(a, str(ans).strip())


def deterministic_sc(vote_dist):
    if not vote_dist:
        return ""
    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])


def compute_mcnemar(results):
    n = len(results)
    b, c = 0, 0
    sc_correct_count, sica_correct_count = 0, 0

    for r in results:
        gt = normalize_answer(r.get("ground_truth", ""))
        sica_correct = r.get("sica_correct", False)
        vote_dist = r.get("sc_vote_distribution", {})
        sc_answer = deterministic_sc(vote_dist)
        sc_correct = normalize_answer(sc_answer) == gt

        if sc_correct:
            sc_correct_count += 1
        if sica_correct:
            sica_correct_count += 1
        if sc_correct and not sica_correct:
            b += 1
        elif not sc_correct and sica_correct:
            c += 1

    sc_pct = sc_correct_count / n * 100 if n else 0
    sica_pct = sica_correct_count / n * 100 if n else 0

    if b + c == 0:
        p_value = 1.0
    else:
        p_value = binomtest(min(b, c), b + c, 0.5).pvalue

    return {
        "n": n,
        "sc_accuracy": round(sc_pct, 2),
        "sica_accuracy": round(sica_pct, 2),
        "delta_pp": round(sica_pct - sc_pct, 2),
        "b_sc_correct_sica_wrong": b,
        "c_sc_wrong_sica_correct": c,
        "mcnemar_p_value": round(p_value, 6),
        "significance": "**" if p_value < 0.02 else "*" if p_value < 0.05 else "ns",
    }


def compute_fleiss_kappa(intermediates_dir):
    categories = FOLIO_CATEGORIES
    cat_idx = {c: i for i, c in enumerate(categories)}

    files = sorted(glob.glob(os.path.join(intermediates_dir, "*.json")))
    if not files:
        return {"kappa": float("nan"), "eff_k": float("nan"), "n_problems": 0}

    ratings = []
    for fpath in files:
        with open(fpath) as f:
            data = json.load(f)
        traces = data.get("sica_result", {}).get("traces", [])
        row = [0] * len(categories)
        for t in traces:
            ans = str(t.get("answer", "")).strip()
            norm = {"true": "True", "false": "False", "unknown": "Unknown"}.get(ans.lower())
            if norm is None and ans:
                norm = "Unknown"
            if norm is not None:
                row[cat_idx[norm]] += 1
        ratings.append(row)

    M = np.array(ratings, dtype=float)
    n_i = M.sum(axis=1)
    valid = n_i >= 2
    M_valid = M[valid]
    n_valid_i = M_valid.sum(axis=1)
    n = M_valid.shape[0]

    if n == 0:
        return {"kappa": float("nan"), "eff_k": float("nan"), "n_problems": len(M)}

    P_i = (np.sum(M_valid ** 2, axis=1) - n_valid_i) / (n_valid_i * (n_valid_i - 1))
    P_bar = np.mean(P_i)
    p_j = M_valid.sum(axis=0) / n_valid_i.sum()
    P_e = np.sum(p_j ** 2)

    kappa = (P_bar - P_e) / (1 - P_e) if (1 - P_e) != 0 else 1.0

    K = K_NOMINAL
    denom = 1 + (K - 1) * kappa
    eff_k = K / denom if denom != 0 else float("inf")

    unanimous = float(np.sum(M.max(axis=1) == n_i) / len(M) * 100)

    return {
        "kappa": round(float(kappa), 4),
        "eff_k": round(float(eff_k), 2),
        "n_problems": int(len(M)),
        "n_valid_kappa": int(n),
        "unanimous_rate_pct": round(unanimous, 1),
    }


def compute_bias_ratio(results):
    sica_wrong = [r for r in results if not r.get("sica_correct", False)]
    if not sica_wrong:
        return {"n_sica_wrong": 0, "bias_ratio": None}

    bias_ratios = []
    for r in sica_wrong:
        scores = r.get("sica_scores", {})
        gt = normalize_answer(r.get("ground_truth", ""))
        sica_ans = normalize_answer(r.get("sica_answer", ""))

        if not scores or not gt or not sica_ans or gt == sica_ans:
            continue

        wrong_score = scores.get(sica_ans, 0)
        gold_score = scores.get(gt, 0)

        if isinstance(wrong_score, (int, float)) and isinstance(gold_score, (int, float)):
            if gold_score != 0:
                bias_ratios.append(wrong_score / gold_score)
            elif wrong_score > 0:
                bias_ratios.append(float("inf"))

    finite = [r for r in bias_ratios if r != float("inf")]
    return {
        "n_sica_wrong": len(sica_wrong),
        "n_with_scores": len(bias_ratios),
        "n_infinite": len(bias_ratios) - len(finite),
        "mean_bias_ratio": round(float(np.mean(finite)), 3) if finite else None,
        "median_bias_ratio": round(float(np.median(finite)), 3) if finite else None,
    }


def compute_constraint_stats(results):
    total_extracted = 0
    total_unique = 0
    total_satisfied = 0
    total_excluded = 0
    n_with_constraints = 0

    for r in results:
        cs = r.get("constraints_stats", {})
        ms = r.get("maxsat_stats", {})

        extracted = cs.get("total_extracted", 0) or cs.get("n_raw", 0) or 0
        unique = cs.get("unique_after_dedup", 0) or cs.get("n_unique", 0) or 0
        sat = ms.get("satisfied", 0) or ms.get("n_satisfied", 0) or 0
        exc = ms.get("excluded", 0) or ms.get("n_excluded", 0) or 0

        total_extracted += extracted
        total_unique += unique
        total_satisfied += sat
        total_excluded += exc

        if extracted > 0:
            n_with_constraints += 1

    n = len(results)
    z3_compiled = total_satisfied + total_excluded
    dedup_rate = 1 - (total_unique / total_extracted) if total_extracted > 0 else 0
    z3_compile_rate = z3_compiled / total_unique if total_unique > 0 else 0

    return {
        "n_problems": n,
        "n_with_constraints": n_with_constraints,
        "total_extracted": total_extracted,
        "total_unique_after_dedup": total_unique,
        "dedup_rate": round(dedup_rate, 3),
        "total_z3_compiled": z3_compiled,
        "z3_compile_rate": round(z3_compile_rate, 3),
        "total_satisfied": total_satisfied,
        "total_excluded": total_excluded,
        "avg_extracted_per_problem": round(total_extracted / n, 1) if n > 0 else 0,
        "avg_unique_per_problem": round(total_unique / n, 1) if n > 0 else 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    parser.add_argument("--intermediates", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    with open(args.results) as f:
        data = json.load(f)

    results = data.get("results", [])
    summary = data.get("summary", {})

    print(f"Loaded {len(results)} results")

    mcnemar = compute_mcnemar(results)
    print(f"\n{'='*60}")
    print(f"  McNemar Exact Test")
    print(f"{'='*60}")
    print(f"  SC:   {mcnemar['sc_accuracy']:.2f}%")
    print(f"  SICA: {mcnemar['sica_accuracy']:.2f}%")
    print(f"  Dpp:  {mcnemar['delta_pp']:+.2f}")
    print(f"  b={mcnemar['b_sc_correct_sica_wrong']}  c={mcnemar['c_sc_wrong_sica_correct']}  p={mcnemar['mcnemar_p_value']:.6f} ({mcnemar['significance']})")

    kappa_stats = compute_fleiss_kappa(args.intermediates)
    print(f"\n{'='*60}")
    print(f"  Fleiss' Kappa & Eff-K")
    print(f"{'='*60}")
    print(f"  kappa:     {kappa_stats['kappa']:.4f}")
    print(f"  Eff-K:     {kappa_stats['eff_k']:.2f}")
    print(f"  Unanimous: {kappa_stats['unanimous_rate_pct']:.1f}%")

    bias = compute_bias_ratio(results)
    print(f"\n{'='*60}")
    print(f"  Bias Ratio (SICA-wrong problems)")
    print(f"{'='*60}")
    print(f"  n_wrong:      {bias['n_sica_wrong']}")
    print(f"  mean_bias:    {bias.get('mean_bias_ratio', 'N/A')}")
    print(f"  median_bias:  {bias.get('median_bias_ratio', 'N/A')}")

    constraints = compute_constraint_stats(results)
    print(f"\n{'='*60}")
    print(f"  Constraint Statistics")
    print(f"{'='*60}")
    print(f"  Total extracted:   {constraints['total_extracted']}")
    print(f"  Unique (deduped):  {constraints['total_unique_after_dedup']} (dedup rate: {constraints['dedup_rate']:.1%})")
    print(f"  Z3 compile rate:   {constraints['z3_compile_rate']:.1%}")
    print(f"  Satisfied:         {constraints['total_satisfied']}")
    print(f"  Excluded:          {constraints['total_excluded']}")
    print(f"  Avg/problem:       {constraints['avg_extracted_per_problem']} extracted, {constraints['avg_unique_per_problem']} unique")

    output = {
        "exp_id": "exp-d126-70b-sica",
        "model": "Qwen2.5-72B-Instruct-AWQ",
        "dataset": "FOLIO-204",
        "K": K_NOMINAL,
        "T_trace": 0.7,
        "T_extract": 0.3,
        "seed": 42,
        "mcnemar": mcnemar,
        "fleiss_kappa": kappa_stats,
        "bias_ratio": bias,
        "constraint_stats": constraints,
        "pipeline_summary": summary,
    }

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nMetrics saved to {args.output}")


if __name__ == "__main__":
    main()
