#!/usr/bin/env python3
"""Compute supplementary statistics for EMNLP 2026 submission."""

import numpy as np
from scipy import stats
from statsmodels.stats.power import TTestPower
from datetime import datetime
import os

# ── Data ──────────────────────────────────────────────────────────────────────
# Table 3: Repo-level multi-seed accuracy (%)
CLS_REPO = {
    "Qwen3-8B": [84.48, 85.60, 84.40],  # s42: cls8b-s42-resume-ckpt3600-test-v2
    "DeepSeek":  [82.61, 74.93, 86.15],
    "DeepSeek_no_outlier": [82.61, 86.15],
}
TRAJ_REPO = {
    "Qwen3-8B": [70.83, 77.08, 70.83],  # s42: qwen3-8b-traj-repo-s42-best-eval (D159)
    "DeepSeek":  [81.25, 75.00, 75.00],
    "DeepSeek_no_outlier": [81.25, 75.00],
}
CWM_REPO = {
    "Qwen3-8B": 64.36,
    "DeepSeek":  61.49,
}

# Table 1: Function-level accuracy (%)
CLS_FUNC = {"DeepSeek": [86.93, 86.77]}
TRAJ_FUNC = {
    "Qwen3-8B": [87.60, 87.79],
    "DeepSeek":  [83.24, 85.08],
}
CWM_FUNC = {"DeepSeek": [85.77, 87.88]}

np.random.seed(42)


def bootstrap_ci(values, n_boot=10000, ci=0.95):
    """Bootstrap CI for mean from seed-level values."""
    arr = np.array(values, dtype=float)
    n = len(arr)
    boot_means = np.array([np.mean(np.random.choice(arr, size=n, replace=True))
                           for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    lo, hi = np.percentile(boot_means, [alpha * 100, (1 - alpha) * 100])
    return np.mean(arr), np.std(arr, ddof=1), lo, hi


def cohens_d(a, b):
    """Cohen's d with pooled SD."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    na, nb = len(a), len(b)
    pooled_sd = np.sqrt(((na - 1) * np.var(a, ddof=1) + (nb - 1) * np.var(b, ddof=1))
                        / (na + nb - 2))
    if pooled_sd == 0:
        return float('inf') if np.mean(a) != np.mean(b) else 0.0
    return (np.mean(a) - np.mean(b)) / pooled_sd


def interpret_d(d):
    ad = abs(d)
    if ad < 0.2:
        return "negligible"
    elif ad < 0.5:
        return "small"
    elif ad < 0.8:
        return "medium"
    else:
        return "large"


def paired_power_analysis(a, b, alpha=0.05):
    """Power analysis for paired t-test given two matched arrays."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    diffs = a - b
    n = len(diffs)
    d_obs = np.mean(diffs) / np.std(diffs, ddof=1) if np.std(diffs, ddof=1) > 0 else float('inf')
    power_obj = TTestPower()
    # Current power
    try:
        current_power = power_obj.power(effect_size=abs(d_obs), nobs=n, alpha=alpha,
                                        alternative='two-sided')
    except Exception:
        current_power = np.nan
    # MDE at power=0.80
    try:
        mde = power_obj.solve_power(nobs=n, alpha=alpha, power=0.80,
                                    alternative='two-sided')
    except Exception:
        mde = np.nan
    # Required n for power=0.80
    try:
        req_n = power_obj.solve_power(effect_size=abs(d_obs), alpha=alpha, power=0.80,
                                      alternative='two-sided')
        req_n = int(np.ceil(req_n))
    except Exception:
        req_n = np.nan
    return d_obs, current_power, mde, req_n


# ── Build output ──────────────────────────────────────────────────────────────
lines = []
w = lines.append

w("=" * 65)
w("  Supplementary Statistics for EMNLP 2026 Submission")
w("=" * 65)
w(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
w("Data source: experiment registry (exec-sim-repair-verifier)")
w("")

# ── 1. Bootstrap CI ──────────────────────────────────────────────────────────
w("-" * 65)
w("  1. Bootstrap 95% CI (Table 3, Repo-level, 10000 resamples)")
w("-" * 65)
w("")
w(f"{'Config':<40} {'Mean':>6} {'± SD':>8} {'95% CI':>20}")
w(f"{'-'*40} {'-'*6} {'-'*8} {'-'*20}")

for task, data in [("CLS", CLS_REPO), ("TRAJ", TRAJ_REPO)]:
    for model, vals in data.items():
        if len(vals) < 3:
            continue
        mean, sd, lo, hi = bootstrap_ci(vals)
        label = f"{task} / {model}"
        if model == "DeepSeek":
            label += " (incl. outlier s123)"
        w(f"{label:<40} {mean:6.2f} {sd:>7.2f}  [{lo:6.2f}, {hi:6.2f}]")

# DeepSeek CLS without outlier
vals = CLS_REPO["DeepSeek_no_outlier"]
mean, sd, lo, hi = bootstrap_ci(vals)
w(f"{'CLS / DeepSeek (excl. outlier s123)':<40} {mean:6.2f} {sd:>7.2f}  [{lo:6.2f}, {hi:6.2f}]")

w("")

# ── 2. Effect Size ───────────────────────────────────────────────────────────
w("-" * 65)
w("  2. Effect Size (Cohen's d)")
w("-" * 65)
w("")
w(f"{'Comparison':<50} {'d':>7} {'Interp.':>12}")
w(f"{'-'*50} {'-'*7} {'-'*12}")

comparisons = [
    ("CLS vs TRAJ (Qwen3-8B, repo, 3 seeds)",
     CLS_REPO["Qwen3-8B"], TRAJ_REPO["Qwen3-8B"]),
    ("CLS vs TRAJ (DeepSeek, repo, 3 seeds, incl. outlier)",
     CLS_REPO["DeepSeek"], TRAJ_REPO["DeepSeek"]),
    ("CLS vs TRAJ (DeepSeek, repo, 2 seeds, excl. outlier)",
     CLS_REPO["DeepSeek_no_outlier"], TRAJ_REPO["DeepSeek_no_outlier"]),
]

for label, a, b in comparisons:
    d = cohens_d(a, b)
    w(f"{label:<50} {d:>7.3f} {interpret_d(d):>12}")

w("")
w("CLS vs CWM repo-level (point estimates, CWM has only s42):")
for model in ["Qwen3-8B", "DeepSeek"]:
    cls_mean = np.mean(CLS_REPO[model])
    cwm_val = CWM_REPO[model]
    diff = cls_mean - cwm_val
    w(f"  {model}: CLS mean={cls_mean:.2f}, CWM s42={cwm_val:.2f}, "
      f"Δ={diff:+.2f} pp (no d: CWM n=1)")

w("")

# ── 3. Power Analysis ────────────────────────────────────────────────────────
w("-" * 65)
w("  3. Power Analysis (paired t-test, α=0.05, two-sided)")
w("-" * 65)
w("")
w(f"{'Comparison':<45} {'d_paired':>8} {'Power':>7} {'MDE@.80':>8} {'n@.80':>6}")
w(f"{'-'*45} {'-'*8} {'-'*7} {'-'*8} {'-'*6}")

power_cases = [
    ("CLS vs TRAJ (Qwen3-8B, 3 seeds)",
     CLS_REPO["Qwen3-8B"], TRAJ_REPO["Qwen3-8B"]),
    ("CLS vs TRAJ (DeepSeek, 3 seeds, incl. outlier)",
     CLS_REPO["DeepSeek"], TRAJ_REPO["DeepSeek"]),
    ("CLS vs TRAJ (DeepSeek, 2 seeds, excl. outlier)",
     CLS_REPO["DeepSeek_no_outlier"], TRAJ_REPO["DeepSeek_no_outlier"]),
]

for label, a, b in power_cases:
    d_p, pwr, mde, req_n = paired_power_analysis(a, b)
    pwr_s = f"{pwr:.3f}" if not np.isnan(pwr) else "N/A"
    mde_s = f"{mde:.3f}" if not np.isnan(mde) else "N/A"
    req_s = f"{req_n}" if not (isinstance(req_n, float) and np.isnan(req_n)) else "N/A"
    w(f"{label:<45} {d_p:>8.3f} {pwr_s:>7} {mde_s:>8} {req_s:>6}")

w("")
w("Interpretation:")
w("  - 'd_paired' = mean(diff) / SD(diff), the paired effect size")
w("  - 'Power' = P(reject H0 | H1 true) with current n and observed d")
w("  - 'MDE@.80' = minimum detectable paired d at power=0.80 with current n")
w("  - 'n@.80' = required n (seeds) to reach power=0.80 with observed d")

w("")

# ── Notes ─────────────────────────────────────────────────────────────────────
w("-" * 65)
w("  Notes")
w("-" * 65)
w("")
w("1. n=3 seeds yields very wide CIs and low statistical power.")
w("   Bootstrap CIs from 3 points are inherently limited; they")
w("   reflect the observed spread but cannot capture the true")
w("   population variance reliably.")
w("")
w("2. DeepSeek CLS s123 (74.93%) is a known outlier caused by")
w("   NaN eval_loss during training. Results are reported both")
w("   with and without this seed for transparency.")
w("")
w("3. CWM repo-level has only s42 completed; Cohen's d is not")
w("   computable (n=1). Point differences are reported instead.")
w("")
w("4. Power analysis uses paired formulation since seeds are")
w("   matched across conditions (same seed → same train/val split).")
w("")

# ── Write ─────────────────────────────────────────────────────────────────────
os.makedirs("artifacts", exist_ok=True)
output_path = "artifacts/supplementary_statistics.txt"
with open(output_path, "w") as f:
    f.write("\n".join(lines))

print(f"Written to {output_path}")
print()
print("\n".join(lines))
