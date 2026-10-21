"""
Sub-population analysis: SICA vs SC by answer type and constraint count.

Input: exp033_results.json (FOLIO-204) and exp046_results.json (PW-600)
       from Mistral-7B experiments.

Each result entry has:
  - ground_truth: "True" / "False" / "Unknown"
  - sica_correct: bool
  - sc_correct: bool
  - constraints_stats.unique_after_dedup: int (constraint count per problem)

Output: sub_population_results.json with per-group stats + McNemar exact p-values.
"""

import json
import sys
import os
import math
import numpy as np
from collections import defaultdict


def mcnemar_exact_pvalue(b, c):
    """Exact McNemar test (two-sided) using binomial distribution.
    b = # problems where SICA correct & SC wrong
    c = # problems where SICA wrong & SC correct
    Returns two-sided p-value under H0: b/(b+c) = 0.5
    """
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    # P(X <= k) under Binomial(n, 0.5), two-sided = 2 * P(X <= k)
    from math import comb
    p = 0.0
    for i in range(k + 1):
        p += comb(n, i) * (0.5 ** n)
    return min(2.0 * p, 1.0)


def analyze_group(items, group_name):
    """Compute SC/SICA accuracy and McNemar test for a group of problems."""
    n = len(items)
    if n == 0:
        return None

    sica_correct = sum(1 for x in items if x["sica_ok"])
    sc_correct = sum(1 for x in items if x["sc_ok"])

    # McNemar contingency: discordant pairs
    b = sum(1 for x in items if x["sica_ok"] and not x["sc_ok"])  # SICA+ SC-
    c = sum(1 for x in items if not x["sica_ok"] and x["sc_ok"])  # SICA- SC+

    sica_acc = sica_correct / n
    sc_acc = sc_correct / n
    delta_pp = sica_acc - sc_acc

    p_value = mcnemar_exact_pvalue(b, c)

    return {
        "group": group_name,
        "n": n,
        "sc_correct": sc_correct,
        "sc_accuracy": round(sc_acc, 4),
        "sica_correct": sica_correct,
        "sica_accuracy": round(sica_acc, 4),
        "delta_pp": round(delta_pp, 4),
        "mcnemar_b_sica_plus_sc_minus": b,
        "mcnemar_c_sica_minus_sc_plus": c,
        "mcnemar_exact_p": round(p_value, 6),
    }


def load_compact_data(results_json_path):
    """Load results JSON and extract compact per-problem data."""
    with open(results_json_path) as f:
        data = json.load(f)

    items = []
    for r in data["results"]:
        items.append({
            "pid": r["problem_id"],
            "gt": r["ground_truth"],
            "sica_ok": r["sica_correct"],
            "sc_ok": r["sc_correct"],
            "n_constr": r["constraints_stats"]["unique_after_dedup"],
        })
    return items


def analyze_by_answer_type(items, dataset_name):
    """Group by gold label and analyze each group."""
    groups = defaultdict(list)
    for x in items:
        groups[x["gt"]].append(x)

    results = []
    for label in ["True", "False", "Unknown"]:
        if label in groups:
            r = analyze_group(groups[label], f"{dataset_name}/{label}")
            if r:
                results.append(r)

    overall = analyze_group(items, f"{dataset_name}/Overall")
    if overall:
        results.append(overall)

    return results


def analyze_by_constraint_count(items, dataset_name):
    """Split into tertiles by constraint count and analyze each group."""
    counts = sorted(x["n_constr"] for x in items)
    n = len(counts)
    t1 = counts[n // 3]
    t2 = counts[2 * n // 3]

    groups = {"Low": [], "Mid": [], "High": []}
    for x in items:
        c = x["n_constr"]
        if c <= t1:
            groups["Low"].append(x)
        elif c <= t2:
            groups["Mid"].append(x)
        else:
            groups["High"].append(x)

    results = []
    for label in ["Low", "Mid", "High"]:
        grp = groups[label]
        if not grp:
            continue
        constraint_values = [x["n_constr"] for x in grp]
        r = analyze_group(grp, f"{dataset_name}/constr_{label}")
        if r:
            r["constraint_range"] = f"[{min(constraint_values)}, {max(constraint_values)}]"
            r["mean_constraints"] = round(np.mean(constraint_values), 1)
            r["tertile_thresholds"] = [int(t1), int(t2)]
            results.append(r)

    return results


def main():
    if len(sys.argv) < 3:
        print("Usage: python sub_population_analysis.py <folio_results.json> <pw_results.json> [output.json]")
        sys.exit(1)

    folio_path = sys.argv[1]
    pw_path = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else "sub_population_results.json"

    folio_items = load_compact_data(folio_path)
    pw_items = load_compact_data(pw_path)

    output = {
        "metadata": {
            "model": "Mistral-7B-Instruct-v0.3",
            "folio_source": os.path.abspath(folio_path),
            "pw_source": os.path.abspath(pw_path),
            "folio_n": len(folio_items),
            "pw_n": len(pw_items),
            "analysis": "sub-population SICA vs SC comparison",
            "mcnemar_test": "exact (two-sided binomial)",
        },
        "by_answer_type": {
            "folio204": analyze_by_answer_type(folio_items, "FOLIO-204"),
            "pw600": analyze_by_answer_type(pw_items, "PW-600"),
        },
        "by_constraint_count": {
            "folio204": analyze_by_constraint_count(folio_items, "FOLIO-204"),
            "pw600": analyze_by_constraint_count(pw_items, "PW-600"),
        },
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # Print summary table
    print("=" * 80)
    print("SUB-POPULATION ANALYSIS: SICA vs SC (Mistral-7B)")
    print("=" * 80)

    for section_name, section_key in [("By Answer Type", "by_answer_type"),
                                       ("By Constraint Count", "by_constraint_count")]:
        print(f"\n{'─' * 80}")
        print(f"  {section_name}")
        print(f"{'─' * 80}")
        for ds_name, ds_results in output[section_key].items():
            print(f"\n  [{ds_name.upper()}]")
            print(f"  {'Group':<30} {'n':>4} {'SC':>7} {'SICA':>7} {'Δpp':>7} {'p':>8}")
            print(f"  {'─' * 65}")
            for r in ds_results:
                p_str = f"{r['mcnemar_exact_p']:.4f}" if r['mcnemar_exact_p'] < 1 else "1.0"
                sig = "*" if r['mcnemar_exact_p'] < 0.05 else ""
                extra = ""
                if "mean_constraints" in r:
                    extra = f"  (μ={r['mean_constraints']:.0f})"
                print(f"  {r['group']:<30} {r['n']:>4} {r['sc_accuracy']:>7.1%} {r['sica_accuracy']:>7.1%} {r['delta_pp']:>+7.1%} {p_str:>7}{sig}{extra}")

    print(f"\n{'=' * 80}")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()
