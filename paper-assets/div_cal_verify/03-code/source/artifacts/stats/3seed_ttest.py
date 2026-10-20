#!/usr/bin/env python3
"""3-seed statistical tests for div_cal_verify Gen7 results."""

import json
import numpy as np
from scipy import stats

# === Data ===
ppl = {
    "Random_50pct": [43.20, 41.75, 44.60],
    "External_only": [45.51, 49.66, 43.90],
    "Uncurated": [50.28, 46.15, 44.69],
    "RGDS": [75.07, 81.57],
}

rare_ngram = {
    "Random_50pct": [0.0096, 0.0098, 0.0101],
    "External_only": [0.0099, 0.0104, 0.0106],
    "Uncurated": [0.0090, 0.0093, 0.0086],
    "RGDS": [0.0051, 0.0062],
}

ratio = {
    "External_only": [1.0953, 1.1299, 1.2430],
    "RGDS": [0.5173, 0.5236],
}


def cohens_d(a, b):
    na, nb = len(a), len(b)
    va, vb = np.var(a, ddof=1), np.var(b, ddof=1)
    pooled_std = np.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    if pooled_std == 0:
        return float("inf")
    return (np.mean(a) - np.mean(b)) / pooled_std


def do_ttest(a, b, name_a, name_b, equal_var=True):
    t_stat, p_val = stats.ttest_ind(a, b, equal_var=equal_var)
    d = cohens_d(a, b)
    return {
        "comparison": f"{name_a} vs {name_b}",
        "mean_a": round(float(np.mean(a)), 4),
        "mean_b": round(float(np.mean(b)), 4),
        "n_a": len(a),
        "n_b": len(b),
        "t_stat": round(float(t_stat), 4),
        "p_value": round(float(p_val), 6),
        "cohens_d": round(float(d), 4),
        "significant_0.05": bool(p_val < 0.05),
        "test_type": "Welch" if not equal_var else "Student",
    }


results = {"ppl_ttests": [], "rare_ngram_ttests": [], "ratio_ttest": None, "ppl_anova": None}

# === PPL t-tests ===
pairs_equal = [
    ("Random_50pct", "Uncurated"),
    ("Random_50pct", "External_only"),
    ("External_only", "Uncurated"),
]
pairs_welch = [
    ("RGDS", "Random_50pct"),
    ("RGDS", "External_only"),
    ("RGDS", "Uncurated"),
]

for a_name, b_name in pairs_equal:
    results["ppl_ttests"].append(do_ttest(ppl[a_name], ppl[b_name], a_name, b_name, equal_var=True))

for a_name, b_name in pairs_welch:
    results["ppl_ttests"].append(do_ttest(ppl[a_name], ppl[b_name], a_name, b_name, equal_var=False))

# === Rare n-gram t-tests ===
for a_name, b_name in pairs_equal:
    results["rare_ngram_ttests"].append(
        do_ttest(rare_ngram[a_name], rare_ngram[b_name], a_name, b_name, equal_var=True)
    )

for a_name, b_name in pairs_welch:
    results["rare_ngram_ttests"].append(
        do_ttest(rare_ngram[a_name], rare_ngram[b_name], a_name, b_name, equal_var=False)
    )

# === Ratio t-test: External vs RGDS ===
results["ratio_ttest"] = do_ttest(
    ratio["External_only"], ratio["RGDS"], "External_only", "RGDS", equal_var=False
)

# === One-way ANOVA on PPL (Random, External, Uncurated) ===
f_stat, p_anova = stats.f_oneway(ppl["Random_50pct"], ppl["External_only"], ppl["Uncurated"])
results["ppl_anova"] = {
    "test": "One-way ANOVA (Random vs External vs Uncurated)",
    "groups": {
        name: {"mean": round(float(np.mean(v)), 4), "sd": round(float(np.std(v, ddof=1)), 4), "n": len(v)}
        for name, v in [("Random_50pct", ppl["Random_50pct"]),
                        ("External_only", ppl["External_only"]),
                        ("Uncurated", ppl["Uncurated"])]
    },
    "F_stat": round(float(f_stat), 4),
    "p_value": round(float(p_anova), 6),
    "significant_0.05": bool(p_anova < 0.05),
    "interpretation": "No significant difference → supports 'normal cluster' framing"
    if p_anova >= 0.05
    else "Significant difference detected among the three methods",
}

# === Rare n-gram ANOVA ===
f_rn, p_rn = stats.f_oneway(rare_ngram["Random_50pct"], rare_ngram["External_only"], rare_ngram["Uncurated"])
results["rare_ngram_anova"] = {
    "test": "One-way ANOVA rare n-gram (Random vs External vs Uncurated)",
    "F_stat": round(float(f_rn), 4),
    "p_value": round(float(p_rn), 6),
    "significant_0.05": bool(p_rn < 0.05),
}

# === Summary ===
results["descriptive"] = {}
for metric_name, metric_data in [("ppl", ppl), ("rare_ngram", rare_ngram)]:
    results["descriptive"][metric_name] = {
        name: {
            "mean": round(float(np.mean(v)), 4),
            "sd": round(float(np.std(v, ddof=1)), 4),
            "n": len(v),
        }
        for name, v in metric_data.items()
    }

out_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/artifacts/stats/3seed_ttest_results.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# === Print ===
print("=" * 70)
print("PPL T-TESTS")
print("=" * 70)
for r in results["ppl_ttests"]:
    sig = "***" if r["significant_0.05"] else "n.s."
    print(f"  {r['comparison']:35s}  t={r['t_stat']:7.3f}  p={r['p_value']:.6f}  d={r['cohens_d']:6.3f}  {sig}")

print()
print("=" * 70)
print("RARE N-GRAM T-TESTS")
print("=" * 70)
for r in results["rare_ngram_ttests"]:
    sig = "***" if r["significant_0.05"] else "n.s."
    print(f"  {r['comparison']:35s}  t={r['t_stat']:7.3f}  p={r['p_value']:.6f}  d={r['cohens_d']:6.3f}  {sig}")

print()
print("=" * 70)
print("RATIO T-TEST (External vs RGDS)")
print("=" * 70)
r = results["ratio_ttest"]
sig = "***" if r["significant_0.05"] else "n.s."
print(f"  {r['comparison']:35s}  t={r['t_stat']:7.3f}  p={r['p_value']:.6f}  d={r['cohens_d']:6.3f}  {sig}")

print()
print("=" * 70)
print("PPL ANOVA (Normal Cluster)")
print("=" * 70)
a = results["ppl_anova"]
print(f"  F={a['F_stat']:.4f}  p={a['p_value']:.6f}  → {a['interpretation']}")

print()
print("=" * 70)
print("RARE N-GRAM ANOVA")
print("=" * 70)
a = results["rare_ngram_anova"]
print(f"  F={a['F_stat']:.4f}  p={a['p_value']:.6f}  sig={a['significant_0.05']}")

print(f"\nResults saved to {out_path}")
