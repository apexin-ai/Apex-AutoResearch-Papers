#!/usr/bin/env python3
"""TOST multi-margin sensitivity analysis for pairwise ambiguity type comparisons."""

import json
import math
from itertools import combinations
from pathlib import Path
from scipy.stats import norm

JUDGMENTS_DIR = Path(__file__).parent.parent / "judgments"
OUTPUT_PATH = Path(__file__).parent / "tost_sensitivity.json"
MARGINS = [0.05, 0.10, 0.15, 0.20]
ALPHA = 0.05


def load_violation_rates():
    """Compute violation rates (moderate+) for ambiguous condition, both models combined."""
    counts = {}
    totals = {}
    for model_dir in ["gpt-5.4", "gpt-4.1"]:
        path = JUDGMENTS_DIR / model_dir / "judgments.jsonl"
        with open(path) as f:
            for line in f:
                d = json.loads(line)
                if d["condition"] != "ambiguous":
                    continue
                t = d["ambiguity_type"]
                totals[t] = totals.get(t, 0) + 1
                if d["judgment"]["violation_level"] in ("moderate", "critical"):
                    counts[t] = counts.get(t, 0) + 1
    rates = {}
    for t in sorted(totals):
        rates[t] = {"violations": counts.get(t, 0), "total": totals[t],
                     "rate": counts.get(t, 0) / totals[t]}
    return rates


def tost_two_proportions(p1, n1, p2, n2, margin):
    """TOST equivalence test for two proportions.

    H0: |p1 - p2| >= margin
    H1: |p1 - p2| < margin
    """
    diff = p1 - p2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    if se == 0:
        equiv = abs(diff) < margin
        return {"p_upper": 0.0 if equiv else 1.0,
                "p_lower": 0.0 if equiv else 1.0,
                "tost_p": 0.0 if equiv else 1.0,
                "equivalent": equiv}
    z_lower = (diff + margin) / se
    p_lower = 1 - norm.cdf(z_lower)
    z_upper = (diff - margin) / se
    p_upper = norm.cdf(z_upper)
    tost_p = max(p_lower, p_upper)
    return {
        "z_lower": round(z_lower, 4),
        "p_lower": round(p_lower, 4),
        "z_upper": round(z_upper, 4),
        "p_upper": round(p_upper, 4),
        "tost_p": round(tost_p, 4),
        "equivalent": bool(tost_p < ALPHA),
    }


def main():
    rates = load_violation_rates()
    types = sorted(rates.keys())
    pairwise_results = []

    for t1, t2 in combinations(types, 2):
        r1, n1 = rates[t1]["rate"], rates[t1]["total"]
        r2, n2 = rates[t2]["rate"], rates[t2]["total"]
        diff = round(r1 - r2, 4)

        tost_results = {}
        smallest_equiv_margin = None
        for margin in MARGINS:
            result = tost_two_proportions(r1, n1, r2, n2, margin)
            tost_results[str(margin)] = result
            if result["equivalent"] and smallest_equiv_margin is None:
                smallest_equiv_margin = margin

        pairwise_results.append({
            "type_1": t1,
            "type_2": t2,
            "rate_1": r1,
            "rate_2": r2,
            "n_1": n1,
            "n_2": n2,
            "diff": diff,
            "tost": tost_results,
            "smallest_equiv_margin": smallest_equiv_margin,
        })

    summary = {
        "n_pairs": len(pairwise_results),
        "equivalent_at_5pp": sum(1 for p in pairwise_results if p["tost"]["0.05"]["equivalent"]),
        "equivalent_at_10pp": sum(1 for p in pairwise_results if p["tost"]["0.1"]["equivalent"]),
        "equivalent_at_15pp": sum(1 for p in pairwise_results if p["tost"]["0.15"]["equivalent"]),
        "equivalent_at_20pp": sum(1 for p in pairwise_results if p["tost"]["0.2"]["equivalent"]),
    }

    equiv_counts = [summary[f"equivalent_at_{m}pp"] for m in [5, 10, 15, 20]]
    never_equiv = sum(1 for p in pairwise_results if p["smallest_equiv_margin"] is None)
    summary["never_equivalent_at_20pp"] = never_equiv
    summary["interpretation"] = (
        f"Of 15 type pairs, {equiv_counts[0]}/{equiv_counts[1]}/{equiv_counts[2]}/{equiv_counts[3]} "
        f"are equivalent at 5/10/15/20pp margins respectively. "
        f"{never_equiv} pairs remain non-equivalent even at ±20pp, "
        f"indicating substantive violation-rate differences between those ambiguity types."
    )

    output = {
        "test": "TOST two one-sided z-tests for proportions — multi-margin sensitivity",
        "alpha": ALPHA,
        "margins_tested": MARGINS,
        "violation_definition": "moderate or critical",
        "condition": "ambiguous",
        "data_sources": ["gpt-5.4", "gpt-4.1"],
        "per_type_rates": {t: {"rate": rates[t]["rate"], "n": rates[t]["total"],
                                "violations": rates[t]["violations"]}
                           for t in types},
        "pairwise_results": pairwise_results,
        "summary": summary,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Written to {OUTPUT_PATH}")
    print(f"\nSummary: {summary['interpretation']}")
    print(f"\nEquivalence counts by margin:")
    for m in MARGINS:
        key = f"equivalent_at_{int(m*100)}pp"
        print(f"  ±{int(m*100)}pp: {summary[key]}/15 pairs equivalent")


if __name__ == "__main__":
    main()
