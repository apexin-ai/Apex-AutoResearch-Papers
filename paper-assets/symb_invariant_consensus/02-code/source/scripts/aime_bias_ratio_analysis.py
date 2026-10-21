"""AIME Cross-Task Bias Ratio Analysis (Direction 3A).

Computes and compares Symbolic Confirmation Bias between FOLIO (logic) and AIME (math).
FOLIO data: from exp-033 confirmation_bias results on westd-25068.
AIME data: from sica_aime30_v3 metadata (raw traces on dead westd-32608, using archived metrics).
"""

import json
import statistics
from pathlib import Path

# ============================================================
# FOLIO bias ratio (from confirmation_bias/results.json)
# ============================================================
FOLIO_RESULTS = {
    "model": "Mistral-7B-Instruct-v0.3",
    "dataset": "FOLIO-204",
    "domain": "logic",
    "n_problems": 204,
    "answer_space": ["True", "False", "Unknown"],
    "K": 12,
    "T": 0.7,
    "sica_accuracy": 0.5931,
    "sc_accuracy": 0.5441,
    "category_stats": {
        "sica_correct": {
            "n": 121,
            "constraints_gold_frac": 0.7808,
            "constraints_wrong_frac": 0.2192,
            "bias_ratio": 0.2808,
        },
        "sica_wrong": {
            "n": 83,
            "constraints_gold_frac": 0.1674,
            "constraints_wrong_frac": 0.8326,
            "bias_ratio": 4.9746,
        },
        "both_wrong": {
            "n": 81,
            "constraints_gold_frac": 0.1603,
            "constraints_wrong_frac": 0.8397,
            "bias_ratio": 5.2391,
        },
        "both_correct": {
            "n": 109,
            "constraints_gold_frac": 0.8193,
            "constraints_wrong_frac": 0.1807,
            "bias_ratio": 0.2205,
        },
    },
    "sica_wrong_follows_sc_rate": 0.9398,
}

# ============================================================
# AIME data (from sica_aime30_v3 checkpoint + partial analysis)
# ============================================================
AIME_PARTIAL_PROBLEMS = [
    {
        "problem_id": "AIME_II_01",
        "gold_answer": 73,
        "sica_answer": 73,
        "sc_answer": 73,
        "sica_correct": True,
        "sc_correct": True,
        "total_constraints": 56,
        "unique_constraints": 33,
        "satisfied": 28,
        "excluded": 5,
        "exclusion_rate": 0.152,
        "sc_distribution": {"73": 12},
        "n_candidates": 1,
        "traces_with_constraints": 9,
    },
    {
        "problem_id": "AIME_II_02",
        "gold_answer": 236,
        "sica_answer": None,
        "sc_answer": None,
        "sica_correct": False,
        "sc_correct": False,
        "total_constraints": 0,
        "unique_constraints": 0,
        "satisfied": 0,
        "excluded": 0,
        "exclusion_rate": None,
        "sc_distribution": {},
        "n_candidates": 0,
        "traces_with_constraints": 0,
        "note": "complete extraction failure",
    },
    {
        "problem_id": "AIME_II_03",
        "gold_answer": 45,
        "sica_answer": 45,
        "sc_answer": 45,
        "sica_correct": True,
        "sc_correct": True,
        "total_constraints": 51,
        "unique_constraints": 18,
        "satisfied": 18,
        "excluded": 0,
        "exclusion_rate": 0.0,
        "sc_distribution": {"45": 11},
        "n_candidates": 1,
        "traces_with_constraints": 11,
    },
    {
        "problem_id": "AIME_II_04",
        "gold_answer": 33,
        "sica_answer": 33,
        "sc_answer": 33,
        "sica_correct": True,
        "sc_correct": True,
        "total_constraints": 20,
        "unique_constraints": 5,
        "satisfied": 4,
        "excluded": 1,
        "exclusion_rate": 0.20,
        "sc_distribution": {"33": 12},
        "n_candidates": 1,
        "traces_with_constraints": 4,
    },
]

AIME_AGGREGATE = {
    "model": "QwQ-32B",
    "dataset": "AIME-2024",
    "domain": "math",
    "n_completed": 22,
    "n_planned": 30,
    "K": 12,
    "T": 0.7,
    "sica_accuracy": 0.7273,
    "sc_accuracy": 0.7273,
    "sica_sc_gap_pp": 0.0,
    "multi_candidate_rate": 0.0,
    "valid_problems": 16,
    "zero_vote_problems": 6,
    "zero_vote_indices": [1, 7, 8, 10, 13, 14],
    "constraints_extracted_problems": 19,
    "exclusion_rate_overall": 0.387,
    "answer_space": "integers 0-999",
}


def compute_folio_summary():
    """Summarize FOLIO bias ratio with context."""
    f = FOLIO_RESULTS
    cs = f["category_stats"]
    return {
        "dataset": f["dataset"],
        "model": f["model"],
        "domain": f["domain"],
        "n_problems": f["n_problems"],
        "sica_accuracy": f["sica_accuracy"],
        "sc_accuracy": f["sc_accuracy"],
        "multi_candidate_rate": "high (3-category answer space, model produces diverse answers)",
        "bias_ratio_sica_wrong": cs["sica_wrong"]["bias_ratio"],
        "bias_ratio_both_wrong": cs["both_wrong"]["bias_ratio"],
        "bias_ratio_sica_correct": cs["sica_correct"]["bias_ratio"],
        "bias_ratio_both_correct": cs["both_correct"]["bias_ratio"],
        "sica_wrong_follows_sc_rate": f["sica_wrong_follows_sc_rate"],
        "interpretation": (
            "When SICA gets wrong answer, 83.3% of constraints support "
            "the SC majority (wrong) answer vs 16.7% for gold. "
            "Bias ratio = 4.97x. Constraints are not independent of LLM majority — "
            "they systematically mirror the model's collective error."
        ),
    }


def compute_aime_analysis():
    """Analyze AIME bias ratio (or explain why it's degenerate)."""
    a = AIME_AGGREGATE
    partial = AIME_PARTIAL_PROBLEMS

    valid_partial = [p for p in partial if p["total_constraints"] > 0]
    correct_partial = [p for p in valid_partial if p["sica_correct"]]
    wrong_partial = [p for p in valid_partial if not p["sica_correct"]]

    exclusion_rates = [p["exclusion_rate"] for p in valid_partial if p["exclusion_rate"] is not None]

    # Since all valid problems have exactly 1 candidate answer,
    # constraints_for_majority / constraints_total = 1.0 trivially.
    # bias_ratio = 1.0/0.0 = undefined (no minority to compare against).

    structural_analysis = {
        "multi_candidate_rate": a["multi_candidate_rate"],
        "n_candidates_per_problem": 1,
        "bias_ratio_computable": False,
        "reason": (
            "All 16 valid AIME problems have exactly 1 candidate answer "
            "(multi_candidate_rate = 0%). The FOLIO-style bias ratio requires "
            "at least 2 candidate answers to compare constraint support for "
            "majority vs gold. With 1 candidate: P(support majority) = 1.0, "
            "P(support non-majority) = 0.0, ratio is undefined (division by zero)."
        ),
    }

    # Alternative metric: constraint exclusion patterns
    exclusion_analysis = {
        "overall_exclusion_rate": a["exclusion_rate_overall"],
        "partial_data_exclusion_rates": {
            p["problem_id"]: p["exclusion_rate"]
            for p in partial
            if p["exclusion_rate"] is not None
        },
        "correct_problems_avg_exclusion": (
            statistics.mean([p["exclusion_rate"] for p in correct_partial])
            if correct_partial else None
        ),
        "interpretation": (
            "Even with unanimous correct answers, 15-20% of constraints are "
            "excluded as self-contradictory. This suggests constraints encode "
            "reasoning errors even when the final answer is correct, but these "
            "errors don't manifest as answer-level bias because answer diversity = 0."
        ),
    }

    # The 6 wrong problems had zero votes → extraction failure
    extraction_failure_analysis = {
        "zero_vote_problems": a["zero_vote_problems"],
        "zero_vote_rate": a["zero_vote_problems"] / a["n_completed"],
        "extraction_success_rate": a["valid_problems"] / a["n_completed"],
        "all_wrong_are_extraction_failures": True,
        "interpretation": (
            "All 6 wrong problems had 0 extractable votes. The 'bias' in AIME "
            "manifests as complete extraction failure rather than biased constraints — "
            "the LLM either solves the problem correctly (with unanimous answer) or "
            "fails so completely that no answer/constraints can be extracted."
        ),
    }

    return {
        "dataset": a["dataset"],
        "model": a["model"],
        "domain": a["domain"],
        "n_completed": a["n_completed"],
        "n_planned": a["n_planned"],
        "sica_accuracy": a["sica_accuracy"],
        "sc_accuracy": a["sc_accuracy"],
        "sica_eq_sc": True,
        "structural_analysis": structural_analysis,
        "exclusion_analysis": exclusion_analysis,
        "extraction_failure_analysis": extraction_failure_analysis,
    }


def compute_cross_task_comparison(folio_summary, aime_analysis):
    """Compare FOLIO and AIME bias ratios."""

    comparison = {
        "folio_bias_ratio": folio_summary["bias_ratio_sica_wrong"],
        "aime_bias_ratio": "undefined (degenerate — zero answer diversity)",
        "aime_bias_ratio_numeric": None,
        "cross_task_generalizable": "inconclusive",

        "root_cause_analysis": {
            "folio": {
                "answer_diversity": "high (3 categories, model frequently disagrees across traces)",
                "constraint_bias": "4.97x toward majority → Symbolic Mirage confirmed",
                "mechanism": "Constraints from each trace inherit that trace's answer direction. "
                             "When majority is wrong, constraints overwhelmingly support wrong answer.",
            },
            "aime": {
                "answer_diversity": "zero (reasoning model converges to single answer)",
                "constraint_bias": "cannot measure (no minority answer to compare)",
                "mechanism": "QwQ-32B as a reasoning model produces near-deterministic traces. "
                             "Failure mode is binary: unanimous-correct OR complete-extraction-failure.",
            },
            "confound": (
                "FOLIO uses Mistral-7B (weaker), AIME uses QwQ-32B (stronger reasoning model). "
                "The zero-diversity result may be model-driven (QwQ-32B is too deterministic) "
                "rather than task-driven (AIME vs FOLIO). To disentangle: need AIME experiment "
                "with Mistral-7B or FOLIO experiment with QwQ-32B."
            ),
        },

        "available_comparisons": {
            "model_strength_evidence": {
                "QwQ-32B_effective_C0": "2.6%",
                "Qwen2.5-14B_C0": "46.0%",
                "diversity_ratio": "17.7x (14B has 17.7x more answer diversity than QwQ-32B)",
                "source": "exp-005 operating regime analysis",
            },
            "conclusion": (
                "The lack of answer diversity on AIME is primarily a MODEL effect "
                "(strong reasoning model → deterministic output), not a TASK effect. "
                "QwQ-32B also shows near-zero diversity on ProofWriter (logic domain, "
                "same answer space as FOLIO). Cross-task generalization of Symbolic Mirage "
                "cannot be tested without matching model strength."
            ),
        },

        "recommended_followup": [
            "Run AIME with Mistral-7B or Qwen2.5-14B to get answer diversity",
            "Run FOLIO with QwQ-32B to confirm zero-diversity is model-driven",
            "If 14B on AIME shows diversity: compute bias ratio for direct comparison",
        ],

        "statistical_caveats": [
            "AIME N=22 (8 incomplete), FOLIO N=204 — very different sample sizes",
            "AIME partial data: only 4/22 problems have detailed constraint breakdown",
            "Raw AIME traces lost (westd-32608 server decommissioned)",
            "Different models between tasks prevents clean cross-task comparison",
        ],
    }

    return comparison


def per_question_bias_ratio_aime():
    """Per-question bias ratio for AIME (where computable)."""
    results = []
    for p in AIME_PARTIAL_PROBLEMS:
        entry = {
            "problem_id": p["problem_id"],
            "gold_answer": p["gold_answer"],
            "sica_answer": p["sica_answer"],
            "sc_answer": p["sc_answer"],
            "sica_correct": p["sica_correct"],
            "n_candidates": p["n_candidates"],
            "total_constraints": p["total_constraints"],
            "unique_constraints": p["unique_constraints"],
            "exclusion_rate": p["exclusion_rate"],
        }

        if p["n_candidates"] == 1 and p["total_constraints"] > 0:
            entry["constraints_for_majority_frac"] = 1.0
            entry["constraints_for_gold_frac"] = 1.0 if p["sica_correct"] else 0.0
            entry["bias_ratio"] = None
            entry["bias_ratio_note"] = "undefined: only 1 candidate answer"
        elif p["total_constraints"] == 0:
            entry["constraints_for_majority_frac"] = None
            entry["constraints_for_gold_frac"] = None
            entry["bias_ratio"] = None
            entry["bias_ratio_note"] = "no constraints extracted"
        else:
            entry["bias_ratio"] = None
            entry["bias_ratio_note"] = "multi-candidate case (not observed in data)"

        results.append(entry)

    return results


def main():
    folio_summary = compute_folio_summary()
    aime_analysis = compute_aime_analysis()
    comparison = compute_cross_task_comparison(folio_summary, aime_analysis)
    per_question = per_question_bias_ratio_aime()

    output = {
        "analysis": "Direction 3A — AIME Cross-Task Bias Ratio",
        "date": "2026-05-20",
        "folio_summary": folio_summary,
        "aime_analysis": aime_analysis,
        "cross_task_comparison": comparison,
        "aime_per_question": per_question,
        "headline_result": {
            "folio_bias_ratio": 4.97,
            "aime_bias_ratio": None,
            "aime_bias_ratio_status": "structurally undefined",
            "is_cross_task": "inconclusive — confounded by model strength difference",
            "key_finding": (
                "AIME (QwQ-32B) produces zero answer diversity (multi_candidate_rate=0%), "
                "making the FOLIO-style bias ratio structurally undefined. "
                "This is primarily a MODEL effect (strong reasoning model → deterministic output), "
                "not a TASK effect. The Symbolic Mirage may still exist in math reasoning but "
                "cannot be measured without weaker model experiments. "
                "FOLIO bias ratio (Mistral-7B) = 4.97x remains the only confirmed datapoint."
            ),
        },
    }

    # Print summary table
    print("=" * 70)
    print("Direction 3A: AIME Cross-Task Bias Ratio Analysis")
    print("=" * 70)

    print("\n--- FOLIO (Mistral-7B, N=204) ---")
    print(f"  SICA accuracy:       {folio_summary['sica_accuracy']:.1%}")
    print(f"  SC accuracy:         {folio_summary['sc_accuracy']:.1%}")
    print(f"  Bias ratio (wrong):  {folio_summary['bias_ratio_sica_wrong']:.2f}x")
    print(f"  Bias ratio (correct):{folio_summary['bias_ratio_sica_correct']:.4f}")
    print(f"  Wrong follows SC:    {folio_summary['sica_wrong_follows_sc_rate']:.1%}")

    print("\n--- AIME (QwQ-32B, N=22/30) ---")
    print(f"  SICA accuracy:       {aime_analysis['sica_accuracy']:.1%}")
    print(f"  SC accuracy:         {aime_analysis['sc_accuracy']:.1%}")
    print(f"  SICA ≡ SC:           {aime_analysis['sica_eq_sc']}")
    print(f"  Multi-candidate rate:{aime_analysis['structural_analysis']['multi_candidate_rate']}")
    print(f"  Bias ratio:          UNDEFINED (zero answer diversity)")
    print(f"  Extraction failures: {aime_analysis['extraction_failure_analysis']['zero_vote_problems']}/22")

    print("\n--- Cross-Task Comparison ---")
    print(f"  FOLIO bias ratio:    4.97x (confirmed)")
    print(f"  AIME bias ratio:     N/A (degenerate)")
    print(f"  Generalizable?       INCONCLUSIVE")
    print(f"  Confound:            Different models (Mistral-7B vs QwQ-32B)")

    print("\n--- AIME Per-Question (partial, 4/22) ---")
    for pq in per_question:
        status = "✓" if pq["sica_correct"] else "✗"
        br = pq["bias_ratio_note"]
        print(f"  {pq['problem_id']}: {status} | constraints={pq['total_constraints']} | exclusion={pq['exclusion_rate']} | bias_ratio={br}")

    print("\n" + "=" * 70)

    return output


if __name__ == "__main__":
    result = main()
    out_path = Path("/tmp/aime_bias_ratio_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")
