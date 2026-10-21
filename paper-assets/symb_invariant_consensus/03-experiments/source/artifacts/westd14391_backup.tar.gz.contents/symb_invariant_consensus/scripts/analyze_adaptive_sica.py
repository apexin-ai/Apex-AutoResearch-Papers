#!/usr/bin/env python3
import json, math, os, sys
from collections import Counter

RESULTS_BASE = "/root/symb_invariant_consensus/results"
EXPERIMENTS = [
    ("exp-033", "Mistral-7B", "FOLIO-204", "exp033_mistral_7b_folio204/exp033_results.json"),
    ("exp-001/026", "Qwen2.5-14B", "FOLIO-204", "folio_204_14b/folio_204_results.json"),
    ("exp-027", "Qwen3-14B-NT", "FOLIO-204", "exp027_qwen3_14b_nonthinking/exp027_results.json"),
    ("exp-035", "Qwen2.5-7B", "FOLIO-204", "exp035_qwen25_7b_folio204/exp035_results.json"),
    ("exp-044b", "Qwen2.5-14B", "FOLIO-199-ICL", "exp044b_icl_oracle_qwen14b/results.json"),
    ("exp-046", "Mistral-7B", "PW-600", "exp046_mistral_7b_pw600/exp046_results.json"),
    ("exp-034-pw", "Qwen2.5-14B", "PW-600", "exp034_qwen25_14b_proofwriter/exp034_results.json"),
    ("exp-028b", "Qwen3-14B-T", "FOLIO-204", "exp028b_qwen3_thinking_folio204/exp028b_results.json"),
    ("exp-051-k4", "Mistral-7B", "FOLIO-204-k4", "exp051_mistral_k_sensitivity/k4/results.json"),
    ("exp-051-k8", "Mistral-7B", "FOLIO-204-k8", "exp051_mistral_k_sensitivity/k8/results.json"),
    ("exp-051-k16", "Mistral-7B", "FOLIO-204-k16", "exp051_mistral_k_sensitivity/k16/results.json"),
]
ENTROPY_THRESHOLD = 1.0

def answer_entropy(vote_distribution):
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
            adaptive_ok = sc_ok
        else:
            n_high += 1
            adaptive_ok = sica_ok
        sc_correct_total += int(sc_ok)
        sica_correct_total += int(sica_ok)
        adaptive_correct_total += int(adaptive_ok)
        per_problem.append({"problem_id": p.get("problem_id", p.get("problem_idx")), "entropy": round(H, 4), "group": "low" if H < ENTROPY_THRESHOLD else "high", "sc_correct": sc_ok, "sica_correct": sica_ok, "adaptive_correct": adaptive_ok})
    return {"n": n, "n_low": n_low, "n_high": n_high, "sc_correct": sc_correct_total, "sica_correct": sica_correct_total, "adaptive_correct": adaptive_correct_total, "sc_acc": round(100 * sc_correct_total / n, 2), "sica_acc": round(100 * sica_correct_total / n, 2), "adaptive_acc": round(100 * adaptive_correct_total / n, 2), "delta_adaptive_sc": round(100 * (adaptive_correct_total - sc_correct_total) / n, 2), "per_problem": per_problem}

def main():
    print("Adaptive SICA Validation (entropy threshold = %.1f bit)" % ENTROPY_THRESHOLD)
    print("=" * 130)
    header = "| %-14s | %-14s | %-16s | %4s | %5s | %5s | %6s | %6s | %9s | %8s |" % ("Experiment", "Model", "Dataset", "n", "n_low", "n_high", "SC%", "SICA%", "Adaptive%", "D(A-SC)")
    sep = "|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|" % ("-"*16, "-"*16, "-"*18, "-"*6, "-"*7, "-"*7, "-"*8, "-"*8, "-"*11, "-"*10)
    print(header)
    print(sep)
    all_results = {}
    n_better = n_equal = n_worse = total_found = 0
    for exp_id, model, dataset, rel_path in EXPERIMENTS:
        full_path = os.path.join(RESULTS_BASE, rel_path)
        result = analyze_experiment(full_path)
        if result is None:
            continue
        total_found += 1
        r = result
        delta = r["delta_adaptive_sc"]
        if delta > 0: n_better += 1; flag = "+"
        elif delta == 0: n_equal += 1; flag = "="
        else: n_worse += 1; flag = "!!WORSE"
        print("| %-14s | %-14s | %-16s | %4d | %5d | %5d | %6.2f | %6.2f | %9.2f | %+7.2f%s |" % (exp_id, model, dataset, r["n"], r["n_low"], r["n_high"], r["sc_acc"], r["sica_acc"], r["adaptive_acc"], delta, flag))
        all_results[exp_id] = {"model": model, "dataset": dataset, "n": r["n"], "n_low": r["n_low"], "n_high": r["n_high"], "sc_acc": r["sc_acc"], "sica_acc": r["sica_acc"], "adaptive_acc": r["adaptive_acc"], "delta_adaptive_sc": delta}
    print(sep)
    print()
    print("Summary:")
    print("  Experiments found: %d" % total_found)
    print("  Adaptive SICA > SC:  %d/%d" % (n_better, total_found))
    print("  Adaptive SICA = SC:  %d/%d" % (n_equal, total_found))
    print("  Adaptive SICA < SC:  %d/%d  %s" % (n_worse, total_found, "(MUST BE 0!)" if n_worse > 0 else "(OK)"))
    if n_worse > 0:
        print("\n*** WARNING: Adaptive SICA is WORSE than SC in some experiments! ***")
    else:
        print("\nAdaptive SICA consistently >= SC across all experiments.")
    print()
    print("Entropy Group Analysis (high-entropy subset only):")
    print("| %-14s | %5s | %8s | %10s | %10s |" % ("Experiment", "n_high", "SC_high%", "SICA_high%", "D(SICA-SC)"))
    print("|%s|%s|%s|%s|%s|" % ("-"*16, "-"*7, "-"*10, "-"*12, "-"*12))
    for exp_id, model, dataset, rel_path in EXPERIMENTS:
        full_path = os.path.join(RESULTS_BASE, rel_path)
        result = analyze_experiment(full_path)
        if result is None: continue
        high_problems = [p for p in result["per_problem"] if p["group"] == "high"]
        if not high_problems: continue
        sc_high = sum(1 for p in high_problems if p["sc_correct"])
        sica_high = sum(1 for p in high_problems if p["sica_correct"])
        n_h = len(high_problems)
        sc_pct = round(100 * sc_high / n_h, 2)
        sica_pct = round(100 * sica_high / n_h, 2)
        delta_h = round(sica_pct - sc_pct, 2)
        print("| %-14s | %5d | %8.2f | %10.2f | %+10.2f |" % (exp_id, n_h, sc_pct, sica_pct, delta_h))
    print()
    print("Threshold Sensitivity:")
    for thresh in [0.5, 0.75, 1.0, 1.25, 1.5]:
        wins = ties = losses = found = 0
        for exp_id, model, dataset, rel_path in EXPERIMENTS:
            full_path = os.path.join(RESULTS_BASE, rel_path)
            if not os.path.exists(full_path): continue
            with open(full_path) as f: data = json.load(f)
            problems = data["results"] if isinstance(data, dict) and "results" in data else data
            if not problems: continue
            found += 1
            sc_c = ad_c = 0
            for p in problems:
                vd = p.get("sc_vote_distribution", {})
                H = answer_entropy(vd)
                sc_ok = p.get("sc_correct", p.get("sc_answer") == p.get("ground_truth"))
                sica_ok = p.get("sica_correct", p.get("sica_answer") == p.get("ground_truth"))
                sc_c += int(sc_ok)
                ad_c += int(sc_ok) if H < thresh else int(sica_ok)
            d = ad_c - sc_c
            if d > 0: wins += 1
            elif d == 0: ties += 1
            else: losses += 1
        print("  threshold=%.2f: %d better, %d equal, %d worse (of %d)" % (thresh, wins, ties, losses, found))
    output_path = os.path.join(RESULTS_BASE, "adaptive_sica_validation.json")
    with open(output_path, "w") as f:
        json.dump({"entropy_threshold": ENTROPY_THRESHOLD, "summary": {"total_experiments": total_found, "adaptive_better": n_better, "adaptive_equal": n_equal, "adaptive_worse": n_worse}, "experiments": all_results}, f, indent=2)
    print("\nResults saved to %s" % output_path)

if __name__ == "__main__":
    main()
