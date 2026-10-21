"""
Shapiro-Wilk normality test and bootstrap 95% CI for Qwen oracle pruning deltas.

Input: 10-run deltas (accuracy difference in pp) from Qwen online oracle pruning.
Output: Shapiro-Wilk W and p-value; bootstrap 95% CI (BCa, 10000 resamples).

Usage: python a2_shapiro_bootstrap.py
"""

import numpy as np
from scipy import stats

# 10-run Qwen oracle pruning deltas (pp)
deltas = np.array([0, 0, -2, 0.5, 1, -1.5, 0.5, 0, 1, 0])

# --- 1. Shapiro-Wilk test ---
W, p_shapiro = stats.shapiro(deltas)
print("=" * 55)
print("Shapiro-Wilk test for normality")
print("=" * 55)
print(f"  W = {W:.4f}")
print(f"  p = {p_shapiro:.4f}")
if p_shapiro > 0.05:
    print("  Interpretation: fail to reject normality (p > 0.05)")
else:
    print("  Interpretation: reject normality (p <= 0.05)")

# --- 2. Bootstrap 95% CI (BCa) ---
rng = np.random.default_rng(seed=42)
n = len(deltas)
B = 10_000

# Bootstrap resamples
boot_means = np.array([
    np.mean(rng.choice(deltas, size=n, replace=True))
    for _ in range(B)
])

# Percentile CI
alpha = 0.05
lo_pct = np.percentile(boot_means, 100 * alpha / 2)
hi_pct = np.percentile(boot_means, 100 * (1 - alpha / 2))

# BCa correction
# (a) bias correction: z0
obs_mean = np.mean(deltas)
z0 = stats.norm.ppf(np.mean(boot_means < obs_mean))

# (b) acceleration: jackknife
jack_means = np.array([np.mean(np.delete(deltas, i)) for i in range(n)])
jack_bar = np.mean(jack_means)
num = np.sum((jack_bar - jack_means) ** 3)
den = 6.0 * (np.sum((jack_bar - jack_means) ** 2)) ** 1.5
a_hat = num / den if den != 0 else 0.0

# (c) adjusted percentiles
z_lo = stats.norm.ppf(alpha / 2)
z_hi = stats.norm.ppf(1 - alpha / 2)

def bca_percentile(z_alpha):
    numer = z0 + z_alpha
    adj = z0 + numer / (1 - a_hat * numer)
    return stats.norm.cdf(adj) * 100

lo_bca_pct = bca_percentile(z_lo)
hi_bca_pct = bca_percentile(z_hi)
lo_bca = np.percentile(boot_means, lo_bca_pct)
hi_bca = np.percentile(boot_means, hi_bca_pct)

print()
print("=" * 55)
print(f"Bootstrap 95% CI ({B} resamples)")
print("=" * 55)
print(f"  Observed mean:      {obs_mean:.3f} pp")
print(f"  Percentile CI:      [{lo_pct:.3f}, {hi_pct:.3f}] pp")
print(f"  BCa CI:             [{lo_bca:.3f}, {hi_bca:.3f}] pp")
print(f"  BCa bias (z0):      {z0:.4f}")
print(f"  BCa acceleration:   {a_hat:.4f}")
print()
print("=" * 55)
print("Comparison with parametric 95% CI")
print("=" * 55)
print(f"  Parametric CI (t):  [-0.75, +0.65] pp")
print(f"  BCa bootstrap CI:   [{lo_bca:.3f}, {hi_bca:.3f}] pp")
print()

# Also compute parametric CI for verification
t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
se = np.std(deltas, ddof=1) / np.sqrt(n)
ci_lo_t = obs_mean - t_crit * se
ci_hi_t = obs_mean + t_crit * se
print(f"  Parametric CI (recomputed): [{ci_lo_t:.3f}, {ci_hi_t:.3f}] pp")
