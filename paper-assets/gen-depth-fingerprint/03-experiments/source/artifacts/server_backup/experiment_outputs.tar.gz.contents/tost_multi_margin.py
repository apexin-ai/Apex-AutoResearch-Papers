import json, math
from scipy import stats

data = {
    "all_data": [2.3348388849917665, 2.3349729068924905, 2.335356366136214],
    "size_matched": [2.367420224547984, 2.366607856947016, 2.367365333689391],
    "depth01": [2.3877152582337495, 2.3868926542907234, 2.386663183991205],
}
MARGINS_PCT = [1, 2, 3, 5]
ALPHA = 0.05

def compute_stats(vals):
    n = len(vals)
    m = sum(vals) / n
    s = math.sqrt(sum((x - m) ** 2 for x in vals) / (n - 1))
    return m, s, n

def pooled_std(s1, n1, s2, n2):
    return math.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))

def tost(vals1, vals2, margin):
    m1, s1, n1 = compute_stats(vals1)
    m2, s2, n2 = compute_stats(vals2)
    se = math.sqrt(s1**2 / n1 + s2**2 / n2)
    df = n1 + n2 - 2
    diff = m1 - m2
    t_upper = (diff - margin) / se
    t_lower = (diff + margin) / se
    p_upper = float(stats.t.cdf(t_upper, df))
    p_lower = float(1 - stats.t.cdf(t_lower, df))
    p_tost = max(p_upper, p_lower)
    return round(p_tost, 6), bool(p_tost < ALPHA)

def run_comparison(vals1, vals2, baseline_mean):
    m1, s1, n1 = compute_stats(vals1)
    m2, s2, n2 = compute_stats(vals2)
    sp = pooled_std(s1, n1, s2, n2)
    d = (m1 - m2) / sp if sp > 0 else float("inf")
    margins = {}
    for pct in MARGINS_PCT:
        margin_abs = baseline_mean * pct / 100.0
        p, eq = tost(vals1, vals2, margin_abs)
        margins[str(pct) + "pct"] = {
            "margin_pct": pct,
            "margin_abs": round(margin_abs, 6),
            "tost_p": p,
            "equivalent": eq,
        }
    return {
        "mean1": round(m1, 6),
        "mean2": round(m2, 6),
        "mean_diff": round(m1 - m2, 6),
        "cohens_d": round(d, 4),
        "pooled_std": round(sp, 6),
        "n_per_group": n1,
        "margins": margins,
    }

baseline_mean = compute_stats(data["all_data"])[0]
comparisons = {
    "all_vs_size_matched": run_comparison(data["all_data"], data["size_matched"], baseline_mean),
    "all_vs_depth01": run_comparison(data["all_data"], data["depth01"], baseline_mean),
}
output = {
    "experiment": "tost_multi_margin_s3",
    "date": "2026-05-17",
    "baseline_mean": round(baseline_mean, 6),
    "alpha": ALPHA,
    "comparisons": comparisons,
}
with open("results/tost_multi_margin.json", "w") as f:
    json.dump(output, f, indent=2)

print("=" * 65)
print("TOST Multi-Margin Equivalence Test Results")
print("=" * 65)
print("Baseline (all_data) mean PPL: %.4f" % baseline_mean)
print()
for cname, cdata in comparisons.items():
    print("--- %s ---" % cname)
    print("  mean diff = %.6f, Cohens d = %.4f" % (cdata["mean_diff"], cdata["cohens_d"]))
    for mname, mdata in cdata["margins"].items():
        eq = "YES" if mdata["equivalent"] else "NO"
        print("  %s: margin=%.4f (%d%%), p=%.6f, equivalent=%s" % (
            mname, mdata["margin_abs"], mdata["margin_pct"], mdata["tost_p"], eq))
    print()
print("Output: results/tost_multi_margin.json")
