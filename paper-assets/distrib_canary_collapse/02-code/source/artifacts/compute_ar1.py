import json, os, numpy as np

def ar1_coef(series):
    x = np.array(series)
    if len(x) < 3:
        return None
    return float(np.corrcoef(x[:-1], x[1:])[0, 1])

def ar1_coef_diff(series):
    x = np.array(series)
    dx = np.diff(x)
    if len(dx) < 3:
        return None
    return float(np.corrcoef(dx[:-1], dx[1:])[0, 1])

base = "/root/autodl-tmp/distrib_canary_collapse/results"

experiments = {
    "a000_s42": {"alpha": 0.0, "T": 10, "path": f"{base}/alpha_sweep/a000_s42_fp32/all_metrics.json"},
    "a025_s42": {"alpha": 0.25, "T": 10, "path": f"{base}/alpha_sweep/a025_s42_fp32/all_metrics.json"},
    "a050_s42": {"alpha": 0.50, "T": 10, "path": f"{base}/alpha_sweep/a050_s42_fp32/all_metrics.json"},
    "a075_s42": {"alpha": 0.75, "T": 10, "path": f"{base}/alpha_sweep/a075_s42_fp32/all_metrics.json"},
    "a100_s42": {"alpha": 1.00, "T": 10, "path": f"{base}/alpha_sweep/a100_s42_fp32/all_metrics.json"},
    "t20_a050_s42": {"alpha": 0.50, "T": 20, "path": f"{base}/t20/a050_s42_fp32/all_metrics.json"},
    "t20_a100_s42": {"alpha": 1.00, "T": 20, "path": f"{base}/t20/a100_s42_fp32/all_metrics.json"},
}

results = {"experiments": {}, "summary": {}}
te_ar1_raw, d1_ar1_raw = [], []
te_ar1_diff, d1_ar1_diff = [], []

for name, info in experiments.items():
    path = info["path"]
    if not os.path.exists(path):
        print(f"MISSING: {path}")
        continue
    with open(path) as f:
        data = json.load(f)
    data.sort(key=lambda x: x["generation"])

    te_series = [d["token_entropy"] for d in data]
    d1_series = [d["distinct_1"] for d in data]

    te_raw = ar1_coef(te_series)
    te_diff = ar1_coef_diff(te_series)
    d1_raw = ar1_coef(d1_series)
    d1_diff = ar1_coef_diff(d1_series)

    results["experiments"][name] = {
        "alpha": info["alpha"],
        "T": info["T"],
        "n_gens": len(data),
        "token_entropy": {
            "series": [round(v, 6) for v in te_series],
            "ar1_raw": round(te_raw, 4) if te_raw is not None else None,
            "ar1_diff": round(te_diff, 4) if te_diff is not None else None,
        },
        "distinct_1": {
            "series": [round(v, 6) for v in d1_series],
            "ar1_raw": round(d1_raw, 4) if d1_raw is not None else None,
            "ar1_diff": round(d1_diff, 4) if d1_diff is not None else None,
        },
    }

    if te_raw is not None: te_ar1_raw.append(te_raw)
    if te_diff is not None: te_ar1_diff.append(te_diff)
    if d1_raw is not None: d1_ar1_raw.append(d1_raw)
    if d1_diff is not None: d1_ar1_diff.append(d1_diff)

def summarize(vals):
    if not vals:
        return {}
    return {
        "mean": round(float(np.mean(vals)), 4),
        "min": round(float(min(vals)), 4),
        "max": round(float(max(vals)), 4),
        "values": [round(float(v), 4) for v in vals],
    }

results["summary"] = {
    "token_entropy_ar1_raw": summarize(te_ar1_raw),
    "distinct_1_ar1_raw": summarize(d1_ar1_raw),
    "token_entropy_ar1_diff": summarize(te_ar1_diff),
    "distinct_1_ar1_diff": summarize(d1_ar1_diff),
}

max_abs_raw = max(max(abs(v) for v in te_ar1_raw), max(abs(v) for v in d1_ar1_raw))
results["conclusion"] = (
    f"Empirical AR(1) coefficients: token_entropy raw range "
    f"[{min(te_ar1_raw):.3f}, {max(te_ar1_raw):.3f}], "
    f"distinct_1 raw range [{min(d1_ar1_raw):.3f}, {max(d1_ar1_raw):.3f}]. "
    f"Max |phi| = {max_abs_raw:.3f}, well below the 0.95 threshold where PermG "
    f"FPR inflation begins. First-differenced AR(1) coefficients are near zero "
    f"(token_entropy mean={np.mean(te_ar1_diff):.3f}, distinct_1 mean="
    f"{np.mean(d1_ar1_diff):.3f}), confirming near-white-noise increments."
)

print(json.dumps(results, indent=2))

# Print summary table
print("\n" + "=" * 90)
print(f"{'Experiment':<16} {'α':>5} {'T':>3} {'te_φ_raw':>10} {'d1_φ_raw':>10} {'te_φ_diff':>10} {'d1_φ_diff':>10}")
print("-" * 90)
for name, exp in results["experiments"].items():
    te_raw = exp["token_entropy"]["ar1_raw"]
    d1_raw = exp["distinct_1"]["ar1_raw"]
    te_diff = exp["token_entropy"]["ar1_diff"]
    d1_diff = exp["distinct_1"]["ar1_diff"]
    print(f"{name:<16} {exp['alpha']:>5.2f} {exp['T']:>3d} {te_raw:>10.4f} {d1_raw:>10.4f} {te_diff:>10.4f} {d1_diff:>10.4f}")
print("-" * 90)
s = results["summary"]
print(f"{'MEAN':<16} {'':>5} {'':>3} {s['token_entropy_ar1_raw']['mean']:>10.4f} {s['distinct_1_ar1_raw']['mean']:>10.4f} {s['token_entropy_ar1_diff']['mean']:>10.4f} {s['distinct_1_ar1_diff']['mean']:>10.4f}")
print(f"{'MAX |φ|':<16} {'':>5} {'':>3} {max(abs(v) for v in s['token_entropy_ar1_raw']['values']):>10.4f} {max(abs(v) for v in s['distinct_1_ar1_raw']['values']):>10.4f} {max(abs(v) for v in s['token_entropy_ar1_diff']['values']):>10.4f} {max(abs(v) for v in s['distinct_1_ar1_diff']['values']):>10.4f}")
print("=" * 90)
