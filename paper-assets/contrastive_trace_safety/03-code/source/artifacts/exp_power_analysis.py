#!/usr/bin/env python3
"""Post-hoc power analysis for R1-32B and QwQ-32B.

Estimates required test set size for 80% power using normal approximation
based on bootstrap CI-derived standard errors.
"""

import json
import math
import os
from scipy import stats

ARTIFACTS = "/root/autodl-tmp/contrastive_trace_safety/artifacts"
R1_BOOTSTRAP = f"{ARTIFACTS}/r1_32b_paired_bootstrap/results.json"
QWQ_ACC_PREC = f"{ARTIFACTS}/acc_precision_bootstrap/results.json"
QWQ_FPR = f"{ARTIFACTS}/qwq_paired_bootstrap_w5/fpr_bootstrap_w5.json"
OUTPUT_DIR = f"{ARTIFACTS}/power_analysis"
OUTPUT_FILE = f"{OUTPUT_DIR}/results.json"


def load_json(path):
    with open(path) as f:
        return json.load(f)


def sigma_from_ci(ci_lower, ci_upper, alpha=0.05):
    """Estimate SE of delta from bootstrap percentile CI (normal approx)."""
    z = stats.norm.ppf(1 - alpha / 2)
    return (ci_upper - ci_lower) / (2 * z)


def sigma_from_pvalue(delta, p_value):
    """Fallback: estimate SE from two-sided p-value."""
    if p_value <= 0 or p_value >= 1 or abs(delta) < 1e-12:
        return None
    z_p = stats.norm.ppf(1 - p_value / 2)
    if abs(z_p) < 1e-10:
        return None
    return abs(delta) / abs(z_p)


def required_n(n_obs, delta, sigma, alpha=0.05, power=0.80):
    """Required n for target power.

    Bootstrap SE scales as sigma(n) = sigma(n_obs) * sqrt(n_obs/n).
    Solving |delta| / sigma(n) >= z_alpha + z_beta gives:
      n = n_obs * ((z_alpha + z_beta) / z_obs)^2
    where z_obs = |delta| / sigma(n_obs).
    """
    if abs(delta) < 1e-12 or sigma < 1e-12:
        return float("inf")
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)
    z_obs = abs(delta) / sigma
    n_req = n_obs * ((z_alpha + z_beta) / z_obs) ** 2
    return math.ceil(n_req)


def check_for_bootstrap_deltas(data, keys_to_check):
    """Check if raw bootstrap delta arrays exist in the JSON."""
    for k in keys_to_check:
        if k in data and isinstance(data[k], list) and len(data[k]) > 10:
            return k
    return None


# --- Load data ---
r1 = load_json(R1_BOOTSTRAP)
qwq_ap = load_json(QWQ_ACC_PREC)
qwq_fpr = load_json(QWQ_FPR)

# Check for raw bootstrap deltas (preferred but not expected)
for name, data in [("R1", r1), ("QwQ_acc_prec", qwq_ap), ("QwQ_fpr", qwq_fpr)]:
    found = check_for_bootstrap_deltas(data, ["bootstrap_deltas", "deltas", "diff_samples"])
    if found:
        print(f"[INFO] Found bootstrap deltas in {name} under key '{found}'")
    else:
        print(f"[INFO] No bootstrap delta arrays in {name} — using CI-based sigma")

print()

# --- Build records ---
records = []

# R1-32B from dedicated paired bootstrap file
for key, metric in [("balanced_accuracy", "bal_acc"), ("precision", "precision"), ("precp_fpr", "pre_cp_fpr")]:
    m = r1[key]
    records.append({
        "model": "R1-32B",
        "metric": metric,
        "delta": m["diff_mean"],
        "n_obs": m["n_valid"],
        "ci_lower": m["diff_ci95"][0],
        "ci_upper": m["diff_ci95"][1],
        "p_value": m["p_value"],
    })

# QwQ-32B balanced accuracy & precision
q = qwq_ap["qwq_32b"]
records.append({
    "model": "QwQ-32B",
    "metric": "bal_acc",
    "delta": q["acc_diff_mean"],
    "n_obs": q["n_test_traces"],
    "ci_lower": q["acc_diff_ci95"][0],
    "ci_upper": q["acc_diff_ci95"][1],
    "p_value": q["acc_p_value"],
})
records.append({
    "model": "QwQ-32B",
    "metric": "precision",
    "delta": q["prec_diff_mean"],
    "n_obs": q["n_prec_valid_traces"],
    "ci_lower": q["prec_diff_ci95"][0],
    "ci_upper": q["prec_diff_ci95"][1],
    "p_value": q["prec_p_value"],
})

# QwQ-32B FPR (file convention: diff = some_sign, we use |delta| for power)
records.append({
    "model": "QwQ-32B",
    "metric": "pre_cp_fpr",
    "delta": qwq_fpr["fpr_diff_mean"],
    "n_obs": qwq_fpr["n_valid_fpr_traces"],
    "ci_lower": qwq_fpr["fpr_diff_ci95"][0],
    "ci_upper": qwq_fpr["fpr_diff_ci95"][1],
    "p_value": qwq_fpr["fpr_p_value"],
})

# --- Compute sigma and required n ---
for r in records:
    r["sigma_from_ci"] = sigma_from_ci(r["ci_lower"], r["ci_upper"])
    r["sigma_from_pvalue"] = sigma_from_pvalue(r["delta"], r["p_value"])
    r["sigma_used"] = r["sigma_from_ci"]  # prefer CI-based
    r["observed_z"] = abs(r["delta"]) / r["sigma_used"] if r["sigma_used"] > 1e-12 else 0
    r["observed_power"] = stats.norm.cdf(r["observed_z"] - 1.96) + stats.norm.cdf(-r["observed_z"] - 1.96)
    r["required_n_005"] = required_n(r["n_obs"], r["delta"], r["sigma_used"], alpha=0.05)
    r["required_n_017"] = required_n(r["n_obs"], r["delta"], r["sigma_used"], alpha=0.05 / 3)

# --- Print tables ---
def fmt_n(n):
    if n == float("inf") or n > 100000:
        return ">100k"
    return str(n)


def print_table(recs, alpha_key, title):
    print(f"{'=' * 95}")
    print(f"  {title}")
    print(f"{'=' * 95}")
    print(f"  {'Model':<10} {'Metric':<12} {'Obs Delta':>10} {'n_obs':>6} {'σ_boot':>8} {'Obs z':>7} {'Obs Pwr':>8} {'Req n':>8}")
    print(f"  {'-'*10} {'-'*12} {'-'*10} {'-'*6} {'-'*8} {'-'*7} {'-'*8} {'-'*8}")
    for r in recs:
        print(
            f"  {r['model']:<10} {r['metric']:<12} {r['delta']:>+10.4f} "
            f"{r['n_obs']:>6d} {r['sigma_used']:>8.4f} "
            f"{r['observed_z']:>7.3f} {r['observed_power']:>8.1%} "
            f"{fmt_n(r[alpha_key]):>8}"
        )
    print()


print_table(records, "required_n_005", "Table 1: α=0.05 (uncorrected), target 80% power")
print_table(records, "required_n_017", "Table 2: α=0.017 (Bonferroni, k=3), target 80% power")

# --- Summary interpretation ---
print("=" * 95)
print("  Interpretation")
print("=" * 95)
for r in records:
    n5 = r["required_n_005"]
    n17 = r["required_n_017"]
    pwr = r["observed_power"]
    print(
        f"  {r['model']:10s} {r['metric']:12s}: "
        f"current power={pwr:.1%}, "
        f"need {fmt_n(n5):>6s} (α=.05) / {fmt_n(n17):>6s} (Bonf) traces"
    )
print()

# --- Save JSON ---
os.makedirs(OUTPUT_DIR, exist_ok=True)
output = {
    "method": "normal_approximation_from_bootstrap_CI",
    "power_target": 0.80,
    "alpha_uncorrected": 0.05,
    "alpha_bonferroni": 0.016667,
    "records": [
        {
            "model": r["model"],
            "metric": r["metric"],
            "observed_delta": round(r["delta"], 5),
            "n_obs": r["n_obs"],
            "sigma_bootstrap": round(r["sigma_used"], 5),
            "observed_z": round(r["observed_z"], 3),
            "observed_power": round(r["observed_power"], 4),
            "required_n_alpha005": r["required_n_005"] if r["required_n_005"] != float("inf") else None,
            "required_n_alpha017": r["required_n_017"] if r["required_n_017"] != float("inf") else None,
        }
        for r in records
    ],
}
with open(OUTPUT_FILE, "w") as f:
    json.dump(output, f, indent=2)
print(f"Saved: {OUTPUT_FILE}")
