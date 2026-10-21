"""Confirmation Bias Analysis for SICA (exp-033, Mistral-7B, FOLIO-204).

Quantifies whether SICA's FOL constraints systematically support the LLM's
majority-vote answer (SC) rather than the gold answer, especially when SICA
gets the answer wrong.
"""

import json
import os
from pathlib import Path
from collections import defaultdict

RESULTS_PATH = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
CACHE_DIR = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/confirmation_bias"


def load_data():
    with open(RESULTS_PATH) as f:
        data = json.load(f)
    return data["results"]


def load_constraint_cache(pid):
    path = os.path.join(CACHE_DIR, f"{pid}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def analyze_constraint_directions(cache_data):
    """Count constraints per answer direction from per-trace data."""
    answer_constraint_counts = defaultdict(int)
    answer_trace_counts = defaultdict(int)
    total_constraints = 0

    for trace in cache_data.get("per_trace", []):
        ans = trace.get("answer", "").strip()
        if not ans:
            continue
        n_constraints = len(trace.get("constraints", []))
        answer_constraint_counts[ans] += n_constraints
        answer_trace_counts[ans] += 1
        total_constraints += n_constraints

    return dict(answer_constraint_counts), dict(answer_trace_counts), total_constraints


def classify_problem(gt, sc, sica, sica_scores, constraint_counts, total_constraints):
    """Classify constraint support for a single problem."""
    result = {
        "gt": gt,
        "sc_answer": sc,
        "sica_answer": sica,
        "sica_correct": sica == gt,
        "sc_correct": sc == gt,
    }

    # From sica_scores (MaxSAT weighted)
    total_weight = sum(sica_scores.values()) if sica_scores else 0
    result["weight_for_gold"] = sica_scores.get(gt, 0)
    result["weight_total"] = total_weight
    result["weight_gold_frac"] = sica_scores.get(gt, 0) / total_weight if total_weight > 0 else 0

    # From raw constraint counts
    result["constraints_for_gold"] = constraint_counts.get(gt, 0)
    result["constraints_for_sc"] = constraint_counts.get(sc, 0)
    result["constraints_total"] = total_constraints
    result["constraints_gold_frac"] = constraint_counts.get(gt, 0) / total_constraints if total_constraints > 0 else 0
    result["constraints_sc_frac"] = constraint_counts.get(sc, 0) / total_constraints if total_constraints > 0 else 0

    # When SC != GT: what fraction supports SC (wrong) vs GT (correct)?
    if sc != gt:
        result["constraints_for_wrong_sc"] = constraint_counts.get(sc, 0)
        result["constraints_wrong_sc_frac"] = constraint_counts.get(sc, 0) / total_constraints if total_constraints > 0 else 0
    else:
        result["constraints_for_wrong_sc"] = 0
        result["constraints_wrong_sc_frac"] = 0

    return result


def compute_category_stats(problems, category_name):
    """Compute aggregate stats for a category of problems."""
    if not problems:
        return {
            "category": category_name,
            "n_problems": 0,
            "constraints_gold_frac": 0,
            "constraints_wrong_frac": 0,
            "weight_gold_frac": 0,
            "bias_ratio": 0,
        }

    n = len(problems)
    gold_fracs = [p["constraints_gold_frac"] for p in problems]
    wrong_fracs = [1 - p["constraints_gold_frac"] for p in problems]
    weight_gold_fracs = [p["weight_gold_frac"] for p in problems]

    avg_gold = sum(gold_fracs) / n
    avg_wrong = sum(wrong_fracs) / n
    avg_weight_gold = sum(weight_gold_fracs) / n

    bias_ratio = avg_wrong / avg_gold if avg_gold > 0 else float("inf")

    return {
        "category": category_name,
        "n_problems": n,
        "constraints_gold_frac": round(avg_gold, 4),
        "constraints_wrong_frac": round(avg_wrong, 4),
        "weight_gold_frac": round(avg_weight_gold, 4),
        "bias_ratio": round(bias_ratio, 4),
    }


def main():
    results = load_data()

    all_classified = []
    skipped = 0

    for r in results:
        pid = r["problem_id"]
        gt = r["ground_truth"]
        sc = r["sc_answer"]
        sica = r["sica_answer"]
        sica_scores = r.get("sica_scores", {})

        cache = load_constraint_cache(pid)
        if cache is None:
            skipped += 1
            continue

        constraint_counts, trace_counts, total_constraints = analyze_constraint_directions(cache)

        classified = classify_problem(gt, sc, sica, sica_scores, constraint_counts, total_constraints)
        classified["problem_id"] = pid
        classified["constraint_counts_by_answer"] = constraint_counts
        classified["trace_counts_by_answer"] = trace_counts
        all_classified.append(classified)

    # Split into categories
    sica_correct = [p for p in all_classified if p["sica_correct"]]
    sica_wrong = [p for p in all_classified if not p["sica_correct"]]
    sc_wrong_sica_correct = [p for p in all_classified if not p["sc_correct"] and p["sica_correct"]]
    sc_correct_sica_wrong = [p for p in all_classified if p["sc_correct"] and not p["sica_correct"]]
    both_wrong = [p for p in all_classified if not p["sc_correct"] and not p["sica_correct"]]
    both_correct = [p for p in all_classified if p["sc_correct"] and p["sica_correct"]]

    categories = [
        ("SICA correct", sica_correct),
        ("SICA wrong", sica_wrong),
        ("SC wrong, SICA correct", sc_wrong_sica_correct),
        ("SC correct, SICA wrong", sc_correct_sica_wrong),
        ("Both wrong", both_wrong),
        ("Both correct", both_correct),
    ]

    cat_stats = [compute_category_stats(probs, name) for name, probs in categories]

    # SC-answer alignment analysis for SICA-wrong cases
    sica_wrong_follows_sc = [p for p in sica_wrong if p["sica_answer"] == p["sc_answer"]]
    sica_wrong_diverges_sc = [p for p in sica_wrong if p["sica_answer"] != p["sc_answer"]]

    # Constraint support for SC answer specifically in wrong cases
    sc_bias_in_wrong = []
    for p in sica_wrong:
        sc_frac = p["constraints_sc_frac"]
        gold_frac = p["constraints_gold_frac"]
        sc_bias_in_wrong.append({
            "problem_id": p["problem_id"],
            "gt": p["gt"],
            "sc_answer": p["sc_answer"],
            "sica_answer": p["sica_answer"],
            "constraints_sc_frac": round(sc_frac, 4),
            "constraints_gold_frac": round(gold_frac, 4),
            "sica_follows_sc": p["sica_answer"] == p["sc_answer"],
        })

    # Summary
    summary = {
        "total_problems": len(all_classified),
        "skipped_no_cache": skipped,
        "sica_accuracy": round(len(sica_correct) / len(all_classified), 4) if all_classified else 0,
        "sc_accuracy": round(sum(1 for p in all_classified if p["sc_correct"]) / len(all_classified), 4) if all_classified else 0,
        "sica_wrong_follows_sc_count": len(sica_wrong_follows_sc),
        "sica_wrong_diverges_sc_count": len(sica_wrong_diverges_sc),
        "sica_wrong_follows_sc_rate": round(len(sica_wrong_follows_sc) / len(sica_wrong), 4) if sica_wrong else 0,
    }

    # Print table
    print("\n=== Confirmation Bias Analysis (exp-033, Mistral-7B, FOLIO-204) ===\n")
    print(f"Total analyzed: {summary['total_problems']}, Skipped: {summary['skipped_no_cache']}")
    print(f"SICA accuracy: {summary['sica_accuracy']:.1%}, SC accuracy: {summary['sc_accuracy']:.1%}\n")

    header = f"{'Category':<30} {'N':>5} {'Constr→Gold':>12} {'Constr→Wrong':>13} {'Weight→Gold':>12} {'Bias Ratio':>11}"
    print(header)
    print("-" * len(header))
    for s in cat_stats:
        print(f"{s['category']:<30} {s['n_problems']:>5} {s['constraints_gold_frac']:>11.1%} {s['constraints_wrong_frac']:>12.1%} {s['weight_gold_frac']:>11.1%} {s['bias_ratio']:>11.2f}")

    print(f"\n--- SICA-Wrong Breakdown ---")
    print(f"SICA wrong & follows SC: {summary['sica_wrong_follows_sc_count']} ({summary['sica_wrong_follows_sc_rate']:.1%})")
    print(f"SICA wrong & diverges from SC: {summary['sica_wrong_diverges_sc_count']}")

    if sica_wrong_follows_sc:
        avg_sc_frac = sum(p["constraints_sc_frac"] for p in sica_wrong_follows_sc) / len(sica_wrong_follows_sc)
        avg_gold_frac = sum(p["constraints_gold_frac"] for p in sica_wrong_follows_sc) / len(sica_wrong_follows_sc)
        print(f"\nWhen SICA follows SC (both wrong):")
        print(f"  Avg constraint support for SC answer: {avg_sc_frac:.1%}")
        print(f"  Avg constraint support for gold answer: {avg_gold_frac:.1%}")

    if sica_wrong_diverges_sc:
        avg_sc_frac_div = sum(p["constraints_sc_frac"] for p in sc_bias_in_wrong if not p["sica_follows_sc"]) / len(sica_wrong_diverges_sc)
        avg_gold_frac_div = sum(p["constraints_gold_frac"] for p in sc_bias_in_wrong if not p["sica_follows_sc"]) / len(sica_wrong_diverges_sc)
        print(f"\nWhen SICA diverges from SC:")
        print(f"  Avg constraint support for SC answer: {avg_sc_frac_div:.1%}")
        print(f"  Avg constraint support for gold answer: {avg_gold_frac_div:.1%}")

    # Save results
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output = {
        "summary": summary,
        "category_stats": cat_stats,
        "sica_wrong_details": sc_bias_in_wrong,
        "per_problem": [{k: v for k, v in p.items() if k != "constraint_counts_by_answer"} for p in all_classified],
    }

    output_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
