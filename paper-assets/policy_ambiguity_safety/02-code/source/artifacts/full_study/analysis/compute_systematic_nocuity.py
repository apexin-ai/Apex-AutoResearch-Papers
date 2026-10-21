#!/usr/bin/env python3
"""Compute systematic nocuity decomposition: convergent-but-wrong rates across models."""

import json
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
JUDGMENT_DIR = BASE / "judgments"
OUTPUT_PATH = Path(__file__).resolve().parent / "systematic_nocuity.json"

VIOLATION_THRESHOLD = {"moderate", "critical"}


def load_judgments(model: str) -> dict:
    """Load judgments keyed by (clause_id, condition)."""
    path = JUDGMENT_DIR / model / "judgments.jsonl"
    data = {}
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            key = (rec["clause_id"], rec["condition"])
            data[key] = rec
    return data


def is_violation(judgment: dict) -> bool:
    return judgment["judgment"]["violation_level"] in VIOLATION_THRESHOLD


def compute_decomposition(j54: dict, j41: dict, condition: str):
    """Compute convergent/divergent/no-violation breakdown for a given condition."""
    keys = sorted(k for k in j54 if k[1] == condition)
    clause_ids = [k[0] for k in keys]

    per_type = defaultdict(lambda: {"convergent": 0, "divergent": 0, "none": 0, "total": 0})
    totals = {"convergent": 0, "divergent": 0, "none": 0}

    level_agreement = {"same": 0, "different": 0}

    for clause_id, cond in keys:
        key = (clause_id, cond)
        if key not in j41:
            continue

        v54 = is_violation(j54[key])
        v41 = is_violation(j41[key])
        amb_type = j54[key]["ambiguity_type"]

        if v54 and v41:
            category = "convergent"
            lv54 = j54[key]["judgment"]["violation_level"]
            lv41 = j41[key]["judgment"]["violation_level"]
            if lv54 == lv41:
                level_agreement["same"] += 1
            else:
                level_agreement["different"] += 1
        elif v54 or v41:
            category = "divergent"
        else:
            category = "none"

        totals[category] += 1
        per_type[amb_type][category] += 1
        per_type[amb_type]["total"] += 1

    n = len(keys)
    result = {
        "convergent_violation": {
            "count": totals["convergent"],
            "rate": round(totals["convergent"] / n, 4) if n else 0,
        },
        "divergent_violation": {
            "count": totals["divergent"],
            "rate": round(totals["divergent"] / n, 4) if n else 0,
        },
        "no_violation": {
            "count": totals["none"],
            "rate": round(totals["none"] / n, 4) if n else 0,
        },
        "level_agreement_in_convergent": level_agreement,
        "per_type": {},
    }

    for atype in sorted(per_type):
        d = per_type[atype]
        t = d["total"]
        result["per_type"][atype] = {
            "total": t,
            "convergent_violation": {"count": d["convergent"], "rate": round(d["convergent"] / t, 4) if t else 0},
            "divergent_violation": {"count": d["divergent"], "rate": round(d["divergent"] / t, 4) if t else 0},
            "no_violation": {"count": d["none"], "rate": round(d["none"] / t, 4) if t else 0},
        }

    return result


def rank_systematic_danger(per_type: dict) -> list:
    """Rank ambiguity types by convergent violation rate (most dangerous first)."""
    return sorted(
        [{"type": t, "convergent_rate": v["convergent_violation"]["rate"]} for t, v in per_type.items()],
        key=lambda x: -x["convergent_rate"],
    )


def main():
    j54 = load_judgments("gpt-5.4")
    j41 = load_judgments("gpt-4.1")

    ambiguous = compute_decomposition(j54, j41, "ambiguous")
    unambiguous = compute_decomposition(j54, j41, "unambiguous")

    danger_ranking = rank_systematic_danger(ambiguous["per_type"])

    top_type = danger_ranking[0]
    amb_conv = ambiguous["convergent_violation"]
    unamb_conv = unambiguous["convergent_violation"]
    level_agree = ambiguous["level_agreement_in_convergent"]

    interpretation_parts = [
        f"Convergent violation rate: {amb_conv['rate']:.1%} ambiguous vs {unamb_conv['rate']:.1%} unambiguous.",
        f"Most systematically dangerous type: {top_type['type']} ({top_type['convergent_rate']:.1%} convergent rate).",
    ]
    if level_agree["same"] + level_agree["different"] > 0:
        agree_rate = level_agree["same"] / (level_agree["same"] + level_agree["different"])
        interpretation_parts.append(
            f"Among convergent violations, {agree_rate:.1%} have identical severity level."
        )

    output = {
        "n_clauses": 300,
        "models": ["gpt-5.4", "gpt-4.1"],
        "violation_threshold": "moderate+",
        "ambiguous": ambiguous,
        "unambiguous": unambiguous,
        "danger_ranking": danger_ranking,
        "interpretation": " ".join(interpretation_parts),
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
