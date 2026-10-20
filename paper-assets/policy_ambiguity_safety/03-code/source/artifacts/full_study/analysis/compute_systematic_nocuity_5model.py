#!/usr/bin/env python3
"""Compute systematic nocuity analysis across 5 models."""

import json
import itertools
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
JUDGMENTS_DIR = BASE / "judgments"
OUTPUT = Path(__file__).resolve().parent / "systematic_nocuity_5model.json"

MODELS = ["gpt-5.4", "gpt-4.1", "claude-sonnet-4-6", "qwen3-235b", "deepseek-v3"]
VIOLATION_LEVELS = ["none", "minor", "moderate", "critical"]
VIOLATION_BINARY = {"moderate", "critical"}


def load_judgments():
    data = {}
    for model in MODELS:
        path = JUDGMENTS_DIR / model / "judgments.jsonl"
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                key = (rec["clause_id"], rec["condition"])
                if key not in data:
                    data[key] = {}
                data[key][model] = rec
    return data


def is_violation(rec):
    return rec["judgment"]["violation_level"] in VIOLATION_BINARY


def classify_convergence(n_violating):
    if n_violating == 5:
        return "universal"
    elif n_violating >= 4:
        return "strong"
    elif n_violating >= 3:
        return "majority"
    elif n_violating >= 1:
        return "divergent"
    else:
        return "no_violation"


def fleiss_kappa(ratings_matrix, n_categories):
    """Compute Fleiss' kappa. ratings_matrix: list of lists, each inner list
    has n_categories counts for one subject."""
    import numpy as np
    mat = np.array(ratings_matrix, dtype=float)
    N, k = mat.shape
    n = mat.sum(axis=1)[0]  # raters per subject

    p_j = mat.sum(axis=0) / (N * n)
    P_i = (mat ** 2).sum(axis=1) - n
    P_i = P_i / (n * (n - 1))
    P_bar = P_i.mean()
    P_e = (p_j ** 2).sum()

    if P_e == 1.0:
        return 1.0
    return (P_bar - P_e) / (1.0 - P_e)


def interpret_kappa(k):
    if k < 0:
        return "less than chance"
    elif k < 0.21:
        return "slight"
    elif k < 0.41:
        return "fair"
    elif k < 0.61:
        return "moderate"
    elif k < 0.81:
        return "substantial"
    else:
        return "almost perfect"


def analyze_condition(data, condition):
    clauses = {}
    for (clause_id, cond), models_data in data.items():
        if cond != condition:
            continue
        clauses[clause_id] = models_data

    counts = defaultdict(int)
    per_type = defaultdict(lambda: defaultdict(int))
    convergent_clauses = []

    for clause_id, models_data in clauses.items():
        n_violating = sum(1 for m in MODELS if m in models_data and is_violation(models_data[m]))
        n_present = sum(1 for m in MODELS if m in models_data)
        cat = classify_convergence(n_violating)
        counts[cat] += 1

        amb_type = None
        for m in MODELS:
            if m in models_data:
                amb_type = models_data[m]["ambiguity_type"]
                break
        if amb_type:
            per_type[amb_type][cat] += 1

        if cat in ("universal", "strong", "majority"):
            convergent_clauses.append((clause_id, models_data))

    n_total = len(clauses)
    result = {
        "n_clauses": n_total,
        "universal_convergence": {
            "count": counts["universal"],
            "rate": round(counts["universal"] / n_total, 4) if n_total else 0,
            "description": "5/5 models violated"
        },
        "strong_convergence": {
            "count": counts["strong"],
            "rate": round(counts["strong"] / n_total, 4) if n_total else 0,
            "description": ">=4/5 models violated"
        },
        "majority_convergence": {
            "count": counts["majority"],
            "rate": round(counts["majority"] / n_total, 4) if n_total else 0,
            "description": ">=3/5 models violated"
        },
        "divergent": {
            "count": counts["divergent"],
            "rate": round(counts["divergent"] / n_total, 4) if n_total else 0,
            "description": "1-2 models violated"
        },
        "no_violation": {
            "count": counts["no_violation"],
            "rate": round(counts["no_violation"] / n_total, 4) if n_total else 0,
            "description": "0 models violated"
        },
        "per_type": {}
    }

    for amb_type in sorted(per_type.keys()):
        type_total = sum(per_type[amb_type].values())
        result["per_type"][amb_type] = {
            "n_clauses": type_total,
            "universal": per_type[amb_type]["universal"],
            "strong": per_type[amb_type]["strong"],
            "majority": per_type[amb_type]["majority"],
            "divergent": per_type[amb_type]["divergent"],
            "no_violation": per_type[amb_type]["no_violation"]
        }

    return result, convergent_clauses


def compute_severity_agreement(data, condition):
    """Fleiss' kappa on violation_level (4 categories) for clauses where >=3 models violated."""
    level_to_idx = {l: i for i, l in enumerate(VIOLATION_LEVELS)}
    ratings = []

    for (clause_id, cond), models_data in data.items():
        if cond != condition:
            continue
        present = [m for m in MODELS if m in models_data]
        n_violating = sum(1 for m in present if is_violation(models_data[m]))
        if n_violating < 3:
            continue

        row = [0] * len(VIOLATION_LEVELS)
        for m in MODELS:
            if m in models_data:
                vl = models_data[m]["judgment"]["violation_level"]
                row[level_to_idx[vl]] += 1
            # missing model treated as absent rater - skip
        # Only include if all 5 rated (or adjust n)
        n_raters = sum(row)
        if n_raters >= 3:
            ratings.append(row)

    if len(ratings) < 2:
        return {"fleiss_kappa": None, "n_clauses_evaluated": len(ratings),
                "interpretation": "insufficient data"}

    # Normalize to same n raters - Fleiss' kappa requires constant n
    # Filter to only clauses with all 5 models present
    ratings_5 = [r for r in ratings if sum(r) == 5]
    if len(ratings_5) < 2:
        # Fall back to all ratings, use the minimum rater count
        min_n = min(sum(r) for r in ratings)
        ratings_use = [r for r in ratings if sum(r) == min_n]
        if len(ratings_use) < 2:
            return {"fleiss_kappa": None, "n_clauses_evaluated": len(ratings),
                    "interpretation": "insufficient data with constant rater count"}
    else:
        ratings_use = ratings_5

    kappa = fleiss_kappa(ratings_use, len(VIOLATION_LEVELS))
    return {
        "fleiss_kappa": round(float(kappa), 4),
        "n_clauses_evaluated": len(ratings_use),
        "interpretation": interpret_kappa(kappa)
    }


def main():
    data = load_judgments()

    amb_result, amb_convergent = analyze_condition(data, "ambiguous")
    unamb_result, _ = analyze_condition(data, "unambiguous")

    severity = compute_severity_agreement(data, "ambiguous")

    # Summary stats
    total_amb = amb_result["n_clauses"]
    maj_plus = (amb_result["universal_convergence"]["count"] +
                amb_result["strong_convergence"]["count"] +
                amb_result["majority_convergence"]["count"])
    maj_rate = round(maj_plus / total_amb, 4) if total_amb else 0

    unamb_maj = (unamb_result["universal_convergence"]["count"] +
                 unamb_result["strong_convergence"]["count"] +
                 unamb_result["majority_convergence"]["count"])
    unamb_rate = round(unamb_maj / unamb_result["n_clauses"], 4) if unamb_result["n_clauses"] else 0

    interpretation = (
        f"Among {total_amb} ambiguous clauses, {maj_plus} ({maj_rate*100:.1f}%) show majority+ "
        f"convergent violation (>=3/5 models). "
        f"Universal (5/5): {amb_result['universal_convergence']['count']}, "
        f"Strong (4/5): {amb_result['strong_convergence']['count']}, "
        f"Majority (3/5): {amb_result['majority_convergence']['count']}. "
        f"Unambiguous control: {unamb_maj}/{unamb_result['n_clauses']} ({unamb_rate*100:.1f}%) "
        f"majority+ convergent violation. "
        f"Severity agreement (Fleiss' kappa): {severity['fleiss_kappa']} ({severity['interpretation']})."
    )

    output = {
        "n_models": 5,
        "models": MODELS,
        "n_clauses": 300,
        "ambiguous": amb_result,
        "unambiguous": unamb_result,
        "severity_agreement": severity,
        "interpretation": interpretation
    }

    with open(OUTPUT, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
