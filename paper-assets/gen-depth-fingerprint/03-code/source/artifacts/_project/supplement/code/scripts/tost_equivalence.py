# Anonymous submission — EMNLP 2026 ARR
"""TOST (Two One-Sided Tests) equivalence testing for downstream fine-tuning results."""

import json
import numpy as np
from scipy import stats

all_data = np.array([2.3348388849917665, 2.3349729068924905, 2.335356366136214])
size_matched = np.array([2.367420224547984, 2.366607856947016, 2.367365333689391])
depth01 = np.array([2.3877152582337495, 2.3868926542907234, 2.386663183991205])


def tost_test(group1, group2, margin):
    """Two One-Sided Tests for equivalence."""
    diff = np.mean(group1) - np.mean(group2)
    se = np.sqrt(np.var(group1, ddof=1)/len(group1) + np.var(group2, ddof=1)/len(group2))
    df = min(len(group1), len(group2)) - 1

    t_upper = (diff - margin) / se
    p_upper = stats.t.cdf(t_upper, df=df)

    t_lower = (diff + margin) / se
    p_lower = 1 - stats.t.cdf(t_lower, df=df)

    p_tost = max(p_upper, p_lower)

    t_crit = stats.t.ppf(0.95, df=df)
    ci_lower = diff - t_crit * se
    ci_upper = diff + t_crit * se

    return {
        "mean_diff": float(diff),
        "se": float(se),
        "df": int(df),
        "t_upper": float(t_upper),
        "p_upper": float(p_upper),
        "t_lower": float(t_lower),
        "p_lower": float(p_lower),
        "p_tost": float(p_tost),
        "equivalent_at_alpha_0.05": bool(p_tost < 0.05),
        "ci_90_lower": float(ci_lower),
        "ci_90_upper": float(ci_upper),
    }


def find_min_margin(group1, group2, alpha=0.05):
    """Binary search for minimum equivalence margin."""
    lo, hi = 0.0001, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        result = tost_test(group1, group2, mid)
        if result["p_tost"] < alpha:
            hi = mid
        else:
            lo = mid
    return round((lo + hi) / 2, 6)


groups = {"all_data": all_data, "size_matched": size_matched, "depth01": depth01}
comparisons = [
    ("all_data", "size_matched"),
    ("all_data", "depth01"),
    ("size_matched", "depth01"),
]

results = {
    "summary": {
        name: {"mean": float(np.mean(g)), "std": float(np.std(g, ddof=1)), "values": g.tolist()}
        for name, g in groups.items()
    },
    "comparisons": {}
}

for name1, name2 in comparisons:
    g1, g2 = groups[name1], groups[name2]
    baseline_mean = np.mean(g1)

    comp_key = f"{name1}_vs_{name2}"
    margin_abs = 0.05
    margin_rel = 0.02 * baseline_mean

    results["comparisons"][comp_key] = {
        "absolute_margin_0.05": tost_test(g1, g2, margin_abs),
        "relative_margin_2pct": {
            "margin_value": float(margin_rel),
            **tost_test(g1, g2, margin_rel)
        },
        "min_margin_for_equivalence": float(find_min_margin(g1, g2)),
        "min_margin_pct_of_baseline": float(find_min_margin(g1, g2) / baseline_mean * 100),
    }

with open("results/tost_equivalence.json", "w") as f:
    json.dump(results, f, indent=2)

print("=== TOST Equivalence Test Results ===\n")
for name, s in results["summary"].items():
    print(f"{name}: mean={s['mean']:.6f}, std={s['std']:.6f}")
print()

for comp_key, comp in results["comparisons"].items():
    print(f"--- {comp_key} ---")
    r1 = comp["absolute_margin_0.05"]
    print(f"  d=0.05 (abs): p_TOST={r1['p_tost']:.6f}, equiv={r1['equivalent_at_alpha_0.05']}, 90%CI=[{r1['ci_90_lower']:.6f}, {r1['ci_90_upper']:.6f}]")
    r2 = comp["relative_margin_2pct"]
    print(f"  d=2% (rel={r2['margin_value']:.6f}): p_TOST={r2['p_tost']:.6f}, equiv={r2['equivalent_at_alpha_0.05']}, 90%CI=[{r2['ci_90_lower']:.6f}, {r2['ci_90_upper']:.6f}]")
    print(f"  Min margin for equivalence: {comp['min_margin_for_equivalence']:.6f} ({comp['min_margin_pct_of_baseline']:.3f}% of baseline)")
    print()
