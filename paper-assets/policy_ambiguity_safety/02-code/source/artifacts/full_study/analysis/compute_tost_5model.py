#!/usr/bin/env python3
"""TOST multi-margin sensitivity analysis — 5-model pooled data."""

import json
import math
from itertools import combinations
from pathlib import Path
from scipy.stats import norm

JUDGMENTS_DIR = Path(__file__).parent.parent / "judgments"
OUTPUT_PATH = Path(__file__).parent / "tost_sensitivity_5model.json"
MODELS = ["gpt-5.4", "gpt-4.1", "claude-sonnet-4-6", "qwen3-235b", "deepseek-v3"]
MARGINS = [0.05, 0.10, 0.15, 0.20]
ALPHA = 0.05


def load_violation_rates():
    counts = {}
    totals = {}
    for model in MODELS:
        path = JUDGMENTS_DIR / model / "judgments.jsonl"
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
        rates[t] = {
            "violations": counts.get(t, 0),
            "total": totals[t],
            "rate": round(counts.get(t, 0) / totals[t], 4),
        }
    return rates


def tost_two_proportions(p1, n1, p2, n2, margin):
    diff = p1 - p2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    if se == 0:
        equiv = abs(diff) < margin
        return {"tost_p": 0.0 if equiv else 1.0, "equivalent": equiv}
    z_upper = (diff - margin) / se
    p_upper = norm.cdf(z_upper)
    z_lower = (diff + margin) / se
    p_lower = 1 - norm.cdf(z_lower)
    tost_p = max(p_upper, p_lower)
    return {
        "z_lower": round(z_lower, 4),
        "p_lower": round(p_lower, 6),
        "z_upper": round(z_upper, 4),
        "p_upper": round(p_upper, 6),
        "tost_p": round(tost_p, 6),
        "equivalent": bool(tost_p < ALPHA),
    }


def main():
    rates = load_violation_rates()
    types = sorted(rates.keys())

    print("Per-type violation rates (from judgments):")
    for t in types:
        r = rates[t]
        print(f"  {t}: {r['violations']}/{r['total']} = {r['rate']:.1%}")

    pairwise_results = []
    for t1, t2 in combinations(types, 2):
        r1, n1 = rates[t1]["rate"], rates[t1]["total"]
        r2, n2 = rates[t2]["rate"], rates[t2]["total"]
        diff = round(r1 - r2, 4)

        tost_results = {}
        smallest_equiv_margin = None
        for margin in MARGINS:
            result = tost_two_proportions(r1, n1, r2, n2, margin)
            tost_results[str(margin)] = {
                "tost_p": result["tost_p"],
                "equivalent": result["equivalent"],
            }
            if result["equivalent"] and smallest_equiv_margin is None:
                smallest_equiv_margin = margin

        pairwise_results.append({
            "type_1": t1,
            "type_2": t2,
            "rate_1": r1,
            "rate_2": r2,
            "diff": diff,
            "tost": tost_results,
            "smallest_equiv_margin": smallest_equiv_margin,
        })

    summary = {
        "equivalent_at_5pp": sum(1 for p in pairwise_results if p["tost"]["0.05"]["equivalent"]),
        "equivalent_at_10pp": sum(1 for p in pairwise_results if p["tost"]["0.1"]["equivalent"]),
        "equivalent_at_15pp": sum(1 for p in pairwise_results if p["tost"]["0.15"]["equivalent"]),
        "equivalent_at_20pp": sum(1 for p in pairwise_results if p["tost"]["0.2"]["equivalent"]),
    }

    output = {
        "n_models": len(MODELS),
        "n_per_type": 250,
        "margins_tested": MARGINS,
        "per_type_rates": {t: rates[t]["rate"] for t in types},
        "pairwise_results": pairwise_results,
        "summary": summary,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nWritten to {OUTPUT_PATH}")
    print(f"\nEquivalence counts by margin:")
    for m in MARGINS:
        key = f"equivalent_at_{int(m * 100)}pp"
        print(f"  ±{int(m * 100)}pp: {summary[key]}/15 pairs")


if __name__ == "__main__":
    main()
