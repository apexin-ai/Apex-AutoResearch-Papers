"""
Robustness check: 5-type ambiguity hierarchy excluding incompleteness.

Motivation: Reviewer N3 argues that the incompleteness type is confounded because
its unambiguous variant adds new information rather than merely disambiguating.
This script verifies whether the ambiguity-type hierarchy holds with the
remaining 5 types.

Input: full_statistics.json (type_effect.rates section)
Output: five_type_no_incompleteness.json

Tests performed:
  1. Chi-squared omnibus test on 5-type violation rates
  2. All 10 pairwise Fisher exact tests with Holm-Bonferroni correction
  3. TOST equivalence tests at +/-15pp and +/-10pp for all 10 pairs
  4. Specific analysis: coreferential vs each other type
  5. Cramer's V effect size
"""

import json
import math
import os
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy import stats

SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "full_statistics.json"
OUTPUT_PATH = SCRIPT_DIR / "five_type_no_incompleteness.json"

EXCLUDE_TYPE = "incompleteness"
TYPES_INCLUDED = [
    "scopal", "lexical", "coreferential",
    "conditional_precedence", "authorization_scope",
]


def load_data():
    with open(INPUT_PATH) as f:
        data = json.load(f)
    rates = data["type_effect"]["rates"]
    # Extract only the 5 included types
    result = {}
    for t in TYPES_INCLUDED:
        r = rates[t]
        result[t] = {
            "n_violations": r["n_violations"],
            "n_total": r["n_total"],
            "violation_rate": r["violation_rate"],
        }
    excluded = rates[EXCLUDE_TYPE]
    n_excluded = excluded["n_total"]
    return result, n_excluded


def chi2_omnibus(type_data):
    """Chi-squared test of independence: type x (violation, no-violation)."""
    types = sorted(type_data.keys())
    observed = np.zeros((len(types), 2), dtype=int)
    for i, t in enumerate(types):
        v = type_data[t]["n_violations"]
        n = type_data[t]["n_total"]
        observed[i, 0] = v
        observed[i, 1] = n - v
    chi2, p, dof, expected = stats.chi2_contingency(observed)
    return {
        "chi2": chi2,
        "p": p,
        "dof": dof,
        "significant_005": bool(p < 0.05),
    }


def cramers_v(type_data):
    """Cramer's V for the type x outcome contingency table."""
    types = sorted(type_data.keys())
    observed = np.zeros((len(types), 2), dtype=int)
    for i, t in enumerate(types):
        v = type_data[t]["n_violations"]
        n = type_data[t]["n_total"]
        observed[i, 0] = v
        observed[i, 1] = n - v
    chi2, _, dof, _ = stats.chi2_contingency(observed)
    n_obs = observed.sum()
    k = min(observed.shape)
    v = math.sqrt(chi2 / (n_obs * (k - 1)))
    return v


def pairwise_fisher(type_data):
    """All pairwise Fisher exact tests with Holm-Bonferroni correction."""
    types = sorted(type_data.keys())
    pairs = list(combinations(types, 2))
    raw_results = []
    for t1, t2 in pairs:
        v1 = type_data[t1]["n_violations"]
        n1 = type_data[t1]["n_total"]
        v2 = type_data[t2]["n_violations"]
        n2 = type_data[t2]["n_total"]
        table = np.array([
            [v1, n1 - v1],
            [v2, n2 - v2],
        ])
        odds_ratio, p = stats.fisher_exact(table, alternative="two-sided")
        raw_results.append({
            "pair": [t1, t2],
            "rate_1": type_data[t1]["violation_rate"],
            "rate_2": type_data[t2]["violation_rate"],
            "difference": type_data[t1]["violation_rate"] - type_data[t2]["violation_rate"],
            "odds_ratio": odds_ratio,
            "p_raw": p,
        })

    # Holm-Bonferroni correction
    raw_results.sort(key=lambda x: x["p_raw"])
    m = len(raw_results)
    for rank_i, r in enumerate(raw_results):
        adjusted_p = r["p_raw"] * (m - rank_i)
        r["p_holm"] = min(adjusted_p, 1.0)
        r["significant_005"] = bool(r["p_holm"] < 0.05)

    # Enforce monotonicity: p_holm[i] >= p_holm[i-1]
    for i in range(1, len(raw_results)):
        if raw_results[i]["p_holm"] < raw_results[i - 1]["p_holm"]:
            raw_results[i]["p_holm"] = raw_results[i - 1]["p_holm"]
            raw_results[i]["significant_005"] = bool(raw_results[i]["p_holm"] < 0.05)

    # Re-sort by pair name for readability
    raw_results.sort(key=lambda x: (x["pair"][0], x["pair"][1]))
    return raw_results


def tost_test(type_data, delta):
    """
    Two one-sided tests (TOST) for equivalence at +/-delta for all pairs.
    Tests H0: |p1 - p2| >= delta against H1: |p1 - p2| < delta.
    Uses z-test for proportions.
    """
    types = sorted(type_data.keys())
    pairs = list(combinations(types, 2))
    results = []
    for t1, t2 in pairs:
        p1 = type_data[t1]["violation_rate"]
        n1 = type_data[t1]["n_total"]
        p2 = type_data[t2]["violation_rate"]
        n2 = type_data[t2]["n_total"]
        diff = p1 - p2
        se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
        if se == 0:
            results.append({
                "pair": [t1, t2],
                "difference": diff,
                "delta": delta,
                "equivalent": bool(abs(diff) < delta),
                "p_tost": 0.0 if abs(diff) < delta else 1.0,
            })
            continue
        # Upper test: H0: diff >= delta  => z_upper = (diff - delta) / se
        z_upper = (diff - delta) / se
        p_upper = stats.norm.cdf(z_upper)  # want this small
        # Lower test: H0: diff <= -delta => z_lower = (diff + delta) / se
        z_lower = (diff + delta) / se
        p_lower = 1 - stats.norm.cdf(z_lower)  # = P(Z > z_lower), want this small
        p_tost = max(p_upper, p_lower)
        results.append({
            "pair": [t1, t2],
            "difference": round(diff, 6),
            "delta": delta,
            "z_upper": round(z_upper, 4),
            "z_lower": round(z_lower, 4),
            "p_upper": p_upper,
            "p_lower": p_lower,
            "p_tost": p_tost,
            "equivalent_005": bool(p_tost < 0.05),
        })
    n_equiv = sum(1 for r in results if r.get("equivalent_005", r.get("equivalent", False)))
    return {
        "delta_pp": round(delta * 100),
        "pairs": results,
        "n_equivalent": n_equiv,
        "n_total_pairs": len(results),
    }


def coreferential_analysis(type_data, pairwise_results):
    """Specific analysis: is coreferential significantly lower than each other type?"""
    coref_rate = type_data["coreferential"]["violation_rate"]
    coref_v = type_data["coreferential"]["n_violations"]
    coref_n = type_data["coreferential"]["n_total"]

    comparisons = []
    for t in sorted(type_data.keys()):
        if t == "coreferential":
            continue
        v = type_data[t]["n_violations"]
        n = type_data[t]["n_total"]
        table = np.array([
            [coref_v, coref_n - coref_v],
            [v, n - v],
        ])
        # One-sided: is coreferential LOWER?
        _, p_one = stats.fisher_exact(table, alternative="less")
        diff = coref_rate - type_data[t]["violation_rate"]
        comparisons.append({
            "comparison": f"coreferential vs {t}",
            "coref_rate": round(coref_rate, 4),
            "other_rate": round(type_data[t]["violation_rate"], 4),
            "difference": round(diff, 4),
            "fisher_p_one_sided": p_one,
        })

    # Holm-Bonferroni on these 4 one-sided tests
    comparisons.sort(key=lambda x: x["fisher_p_one_sided"])
    m = len(comparisons)
    for rank_i, c in enumerate(comparisons):
        adj_p = c["fisher_p_one_sided"] * (m - rank_i)
        c["p_holm"] = min(adj_p, 1.0)
        c["significant_005"] = bool(c["p_holm"] < 0.05)

    for i in range(1, len(comparisons)):
        if comparisons[i]["p_holm"] < comparisons[i - 1]["p_holm"]:
            comparisons[i]["p_holm"] = comparisons[i - 1]["p_holm"]
            comparisons[i]["significant_005"] = bool(comparisons[i]["p_holm"] < 0.05)

    n_sig = sum(1 for c in comparisons if c["significant_005"])
    comparisons.sort(key=lambda x: x["comparison"])

    return {
        "coreferential_rate": round(coref_rate, 4),
        "comparisons": comparisons,
        "n_significant": n_sig,
        "n_comparisons": len(comparisons),
        "still_lowest": bool(all(
            coref_rate <= type_data[t]["violation_rate"]
            for t in type_data if t != "coreferential"
        )),
    }


def main():
    type_data, n_excluded = load_data()

    # Print summary
    print("=" * 60)
    print("5-Type Hierarchy Analysis (Excluding Incompleteness)")
    print("=" * 60)
    print(f"\nExcluded: incompleteness (n={n_excluded})")
    print(f"\nIncluded types and ambiguous-condition violation rates:")
    for t in sorted(type_data.keys()):
        d = type_data[t]
        print(f"  {t:30s}: {d['violation_rate']:.3f} ({d['n_violations']}/{d['n_total']})")

    # 1. Chi-squared omnibus
    omnibus = chi2_omnibus(type_data)
    print(f"\nOmnibus chi2: {omnibus['chi2']:.4f}, p={omnibus['p']:.6e}, dof={omnibus['dof']}")
    print(f"  Significant at 0.05: {omnibus['significant_005']}")

    # 2. Cramer's V
    cv = cramers_v(type_data)
    print(f"\nCramer's V: {cv:.4f}")

    # 3. Pairwise Fisher
    fisher_results = pairwise_fisher(type_data)
    print(f"\nPairwise Fisher exact tests (Holm-Bonferroni corrected):")
    n_sig = sum(1 for r in fisher_results if r["significant_005"])
    for r in fisher_results:
        sig_str = "*" if r["significant_005"] else ""
        print(f"  {r['pair'][0]:25s} vs {r['pair'][1]:25s}: "
              f"diff={r['difference']:+.3f}, p_holm={r['p_holm']:.4e} {sig_str}")
    print(f"  {n_sig}/{len(fisher_results)} significant at 0.05")

    # 4. TOST
    tost_15 = tost_test(type_data, 0.15)
    tost_10 = tost_test(type_data, 0.10)
    print(f"\nTOST at +/-15pp: {tost_15['n_equivalent']}/{tost_15['n_total_pairs']} equivalent")
    print(f"TOST at +/-10pp: {tost_10['n_equivalent']}/{tost_10['n_total_pairs']} equivalent")

    for label, tost in [("15pp", tost_15), ("10pp", tost_10)]:
        print(f"\n  TOST +/-{label} details:")
        for p in tost["pairs"]:
            eq_str = "EQ" if p.get("equivalent_005", p.get("equivalent", False)) else "  "
            print(f"    {p['pair'][0]:25s} vs {p['pair'][1]:25s}: "
                  f"diff={p['difference']:+.4f}, p_tost={p.get('p_tost', 'N/A'):.4e} {eq_str}")

    # 5. Coreferential analysis
    coref = coreferential_analysis(type_data, fisher_results)
    print(f"\nCoreferential vs others (one-sided Fisher, Holm-corrected):")
    print(f"  Coreferential rate: {coref['coreferential_rate']:.4f}")
    print(f"  Still lowest: {coref['still_lowest']}")
    for c in coref["comparisons"]:
        sig_str = "*" if c["significant_005"] else ""
        print(f"  vs {c['comparison'].split('vs ')[1]:25s}: "
              f"diff={c['difference']:+.4f}, p_holm={c['p_holm']:.4e} {sig_str}")
    print(f"  {coref['n_significant']}/{coref['n_comparisons']} significantly lower")

    # Build conclusion
    parts = []
    if omnibus["significant_005"]:
        parts.append(f"omnibus chi2 significant (p={omnibus['p']:.2e})")
    else:
        parts.append(f"omnibus chi2 NOT significant (p={omnibus['p']:.2e})")

    if coref["still_lowest"]:
        parts.append("coreferential still lowest")
        if coref["n_significant"] > 0:
            parts.append(f"significantly lower than {coref['n_significant']}/{coref['n_comparisons']} types")
        else:
            parts.append("but not significantly lower than any after correction")
    conclusion = "; ".join(parts) + f"; Cramer's V={cv:.3f} (small effect)"

    print(f"\nConclusion: {conclusion}")

    # Assemble output
    output = {
        "analysis_name": "5-Type Hierarchy (Excluding Incompleteness)",
        "motivation": "Response to reviewer N3: incompleteness type excluded because its unambiguous variant adds new information, creating a confound",
        "types_included": sorted(TYPES_INCLUDED),
        "type_excluded": EXCLUDE_TYPE,
        "n_episodes_excluded": n_excluded,
        "per_type_rates": {
            t: {
                "violation_rate": round(type_data[t]["violation_rate"], 6),
                "n_violations": type_data[t]["n_violations"],
                "n_total": type_data[t]["n_total"],
            }
            for t in sorted(type_data.keys())
        },
        "omnibus_chi2": omnibus,
        "cramers_v": round(cv, 6),
        "pairwise_fisher": fisher_results,
        "tost_15pp": tost_15,
        "tost_10pp": tost_10,
        "coreferential_vs_others": coref,
        "conclusion": conclusion,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
