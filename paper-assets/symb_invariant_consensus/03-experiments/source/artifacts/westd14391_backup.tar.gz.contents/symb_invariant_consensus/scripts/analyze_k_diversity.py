#!/usr/bin/env python
"""K Sensitivity Diversity Analysis: quantify K vs trace diversity."""

import json
import os
import math
from collections import Counter
from itertools import combinations
from pathlib import Path

RESULTS_DIR = Path("/root/symb_invariant_consensus/results")

DATA_SOURCES = {
    4:  RESULTS_DIR / "exp051_mistral_k_sensitivity" / "k4",
    8:  RESULTS_DIR / "exp051_mistral_k_sensitivity" / "k8",
    12: RESULTS_DIR / "exp033_mistral_7b_folio204",
    16: RESULTS_DIR / "exp051_mistral_k_sensitivity" / "k16",
    20: RESULTS_DIR / "exp051_mistral_k_sensitivity" / "k20",
}


def load_intermediates(base_dir):
    idir = base_dir / "intermediates"
    if not idir.exists():
        return []
    results = []
    for f in sorted(idir.glob("folio_*.json")):
        with open(f) as fh:
            results.append(json.load(fh))
    return results


def shannon_entropy(counts):
    total = sum(counts.values())
    if total == 0:
        return 0.0
    probs = [c / total for c in counts.values() if c > 0]
    return -sum(p * math.log2(p) for p in probs)


def effective_diversity(counts):
    total = sum(counts.values())
    if total == 0:
        return 0.0
    max_p = max(counts.values()) / total
    return 1.0 - max_p


def jaccard_similarity(set_a, set_b):
    if not set_a and not set_b:
        return 1.0
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union) if union else 1.0


def extract_constraint_set(constraint_list):
    return set(c.get("expression", c.get("z3_formula", str(c))) for c in constraint_list)


def analyze_k(k, base_dir):
    intermediates = load_intermediates(base_dir)
    n = len(intermediates)
    if n == 0:
        return None

    # Load summary if available
    summary = None
    for name in ["results.json", "exp033_results.json"]:
        rpath = base_dir / name
        if rpath.exists():
            with open(rpath) as f:
                summary = json.load(f).get("summary", {})
            break

    entropies = []
    eff_divs = []
    unique_constraint_counts = []
    mean_jaccards = []
    sc_correct = 0
    sica_correct = 0
    has_per_trace = False

    for item in intermediates:
        sr = item["sica_result"]
        gt = item["problem"].get("answer", "")

        # Answer counts
        ac = sr.get("answer_counts", {})
        entropies.append(shannon_entropy(ac))
        eff_divs.append(effective_diversity(ac))

        # Accuracy
        sc_answer = max(ac, key=ac.get) if ac else ""
        sica_answer = sr.get("answer", "")
        if sc_answer == gt:
            sc_correct += 1
        if sica_answer == gt:
            sica_correct += 1

        # Per-trace constraints
        ptc = sr.get("per_trace_constraints")
        if ptc and isinstance(ptc, list) and len(ptc) > 0:
            has_per_trace = True
            all_constraints = set()
            trace_sets = []
            for tc in ptc:
                if isinstance(tc, list):
                    cs = extract_constraint_set(tc)
                    trace_sets.append(cs)
                    all_constraints.update(cs)
            unique_constraint_counts.append(len(all_constraints))

            # Pairwise Jaccard
            if len(trace_sets) >= 2:
                jaccards = []
                for a, b in combinations(range(len(trace_sets)), 2):
                    jaccards.append(jaccard_similarity(trace_sets[a], trace_sets[b]))
                mean_jaccards.append(sum(jaccards) / len(jaccards))
        else:
            # For exp033 K=12: use aggregate constraints_stats
            cs = sr.get("constraints_stats", {})
            if cs:
                unique_constraint_counts.append(cs.get("unique_after_dedup", 0))

    sc_acc = sc_correct / n if n > 0 else 0
    sica_acc = sica_correct / n if n > 0 else 0

    result = {
        "K": k,
        "n": n,
        "n_total": 204,
        "status": "complete" if n == 204 else f"in-progress ({n}/204)",
        "SC_accuracy": round(sc_acc * 100, 2),
        "SICA_accuracy": round(sica_acc * 100, 2),
        "delta": round((sica_acc - sc_acc) * 100, 2),
        "mean_entropy": round(sum(entropies) / len(entropies), 4) if entropies else None,
        "mean_unique_constraints": round(sum(unique_constraint_counts) / len(unique_constraint_counts), 2) if unique_constraint_counts else None,
        "has_per_trace_constraints": has_per_trace,
    }

    if mean_jaccards:
        result["mean_jaccard"] = round(sum(mean_jaccards) / len(mean_jaccards), 4)
    else:
        result["mean_jaccard"] = None

    if eff_divs:
        result["effective_diversity"] = round(sum(eff_divs) / len(eff_divs), 4)
    else:
        result["effective_diversity"] = None

    # Add summary-level constraint stats
    if summary:
        result["total_constraints"] = summary.get("total_constraints_extracted")
        result["total_unique_constraints"] = summary.get("total_unique_constraints")
        result["contradiction_rate"] = round(summary.get("contradiction_rate", 0) * 100, 2)
        result["problems_with_contradictions"] = summary.get("problems_with_contradictions")

    return result


def main():
    all_results = {}
    for k in sorted(DATA_SOURCES.keys()):
        base_dir = DATA_SOURCES[k]
        if not base_dir.exists():
            print(f"K={k}: directory not found ({base_dir})")
            continue
        result = analyze_k(k, base_dir)
        if result is None:
            print(f"K={k}: no data")
            continue
        all_results[k] = result

    # Print table
    print(f"\nK vs Diversity Metrics (FOLIO-204, Mistral-7B, T=0.7)")
    print(f"{'K':>3} | {'n':>5} | {'SC%':>6} | {'SICA%':>6} | {'delta':>6} | {'Entropy':>8} | {'Uniq Constr':>11} | {'Jaccard':>8} | {'Eff Div':>8} | {'Contr%':>6} | Status")
    print("-" * 110)

    for k in sorted(all_results.keys()):
        r = all_results[k]
        entropy_s = f"{r['mean_entropy']:.4f}" if r['mean_entropy'] is not None else "N/A"
        uc_s = f"{r['mean_unique_constraints']:.1f}" if r['mean_unique_constraints'] is not None else "N/A"
        jac_s = f"{r['mean_jaccard']:.4f}" if r['mean_jaccard'] is not None else "N/A"
        ed_s = f"{r['effective_diversity']:.4f}" if r['effective_diversity'] is not None else "N/A"
        contr_s = f"{r.get('contradiction_rate', 'N/A')}"
        delta_s = f"+{r['delta']:.2f}" if r['delta'] >= 0 else f"{r['delta']:.2f}"
        status = r['status']
        print(f"{r['K']:>3} | {r['n']:>5} | {r['SC_accuracy']:>6.2f} | {r['SICA_accuracy']:>6.2f} | {delta_s:>6} | {entropy_s:>8} | {uc_s:>11} | {jac_s:>8} | {ed_s:>8} | {contr_s:>6} | {status}")

    # Additional analysis: per-K constraint growth
    print(f"\n--- Constraint Scaling ---")
    for k in sorted(all_results.keys()):
        r = all_results[k]
        tc = r.get('total_constraints')
        tuc = r.get('total_unique_constraints')
        if tc and tuc:
            ratio = tuc / tc * 100
            per_problem_total = tc / r['n']
            per_problem_unique = tuc / r['n']
            print(f"K={k:>2}: total={tc:>6}, unique={tuc:>6} ({ratio:.1f}%), "
                  f"per-problem: {per_problem_total:.1f} total / {per_problem_unique:.1f} unique")

    # Marginal gain analysis
    print(f"\n--- Marginal Accuracy Gain ---")
    sorted_ks = sorted(all_results.keys())
    for i in range(1, len(sorted_ks)):
        k_prev = sorted_ks[i - 1]
        k_curr = sorted_ks[i]
        if all_results[k_prev]['n'] == 204 and all_results[k_curr]['n'] == 204:
            sc_gain = all_results[k_curr]['SC_accuracy'] - all_results[k_prev]['SC_accuracy']
            sica_gain = all_results[k_curr]['SICA_accuracy'] - all_results[k_prev]['SICA_accuracy']
            dk = k_curr - k_prev
            print(f"K={k_prev}->{k_curr} (dk={dk}): SC {sc_gain:+.2f}%, SICA {sica_gain:+.2f}%")

    # Save results
    output_path = RESULTS_DIR / "k_sensitivity_diversity_analysis.json"
    with open(output_path, "w") as f:
        json.dump({
            "analysis": "K Sensitivity Diversity Analysis",
            "dataset": "FOLIO-204",
            "model": "Mistral-7B",
            "temperature": 0.7,
            "timestamp": "2026-05-19",
            "results": {str(k): v for k, v in all_results.items()},
        }, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
