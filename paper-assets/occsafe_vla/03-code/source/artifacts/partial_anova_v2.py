"""
Partial ANOVA — v2 data, gradient effect within BN (BatchNorm) only.

Data source (all v2 code):
  Cell 1 (Full OCC BN, Grad ON):  mvp_occ_s0 CAR=0.746, full_occ_bn_v2_s1_eval CAR=0.654
  Cell 3 (Detach BN, Grad OFF):   detach_bn_v2_s0_eval CAR=0.774, detach_bn_v2_s1_eval CAR=0.736, detach_bn_v2_s2_eval CAR=0.762
  Vanilla (No OCC):               vanilla_v2_s0_eval CAR=0.768

LN conditions excluded — only v1 data available for LN.
"""

import numpy as np
from scipy import stats
import sys
import warnings

np.random.seed(42)

# ── Data ──
cell1 = np.array([0.746, 0.654])        # Full OCC BN, Grad ON (n=2)
cell3 = np.array([0.774, 0.736, 0.762]) # Detach BN, Grad OFF (n=3)
vanilla = np.array([0.768])              # No OCC (n=1)

groups = {'Cell 1 (Full OCC BN, Grad ON)': cell1,
          'Cell 3 (Detach BN, Grad OFF)': cell3,
          'Vanilla (No OCC)': vanilla}

out_lines = []

def pr(s=''):
    print(s)
    out_lines.append(s)

def fmt(x):
    return f'{x:.3f}'

# ── 1. Descriptive Statistics ──
pr('=' * 70)
pr('1. DESCRIPTIVE STATISTICS')
pr('=' * 70)
for name, data in groups.items():
    n = len(data)
    m = np.mean(data)
    s = np.std(data, ddof=1) if n > 1 else float('nan')
    if n > 1:
        se = s / np.sqrt(n)
        t_crit = stats.t.ppf(0.975, df=n-1)
        ci_lo = m - t_crit * se
        ci_hi = m + t_crit * se
        ci_str = f'[{fmt(ci_lo)}, {fmt(ci_hi)}]'
    else:
        ci_str = 'N/A (n=1)'
    pr(f'  {name}:')
    pr(f'    n={n}, mean={fmt(m)}, std={fmt(s) if n>1 else "N/A"}, 95% CI={ci_str}')
pr()

# ── 2. Cell 1 vs Cell 3: Welch's t-test ──
pr('=' * 70)
pr('2. CELL 1 vs CELL 3: GRADIENT EFFECT (Welch\'s t-test)')
pr('=' * 70)

t_stat, p_val = stats.ttest_ind(cell1, cell3, equal_var=False)
n1, n2 = len(cell1), len(cell3)
m1, m2 = np.mean(cell1), np.mean(cell3)
s1, s2 = np.std(cell1, ddof=1), np.std(cell3, ddof=1)

# Welch-Satterthwaite df
df_welch = ((s1**2/n1 + s2**2/n2)**2 /
            ((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1)))

# Cohen's d with Hedges' g correction
s_pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
d_cohen = (m1 - m2) / s_pooled
# Hedges' correction factor J
df_hedge = n1 + n2 - 2
J = 1 - 3 / (4 * df_hedge - 1)
g_hedges = d_cohen * J

# eta-squared from t
eta_sq = t_stat**2 / (t_stat**2 + df_welch)

pr(f'  Cell 1 mean: {fmt(m1)}, Cell 3 mean: {fmt(m2)}')
pr(f'  Mean diff (Cell1 - Cell3): {fmt(m1 - m2)}')
pr(f'  t = {fmt(t_stat)}, df = {fmt(df_welch)}, p = {fmt(p_val)}')
pr(f'  Cohen\'s d = {fmt(d_cohen)}')
pr(f'  Hedges\' g = {fmt(g_hedges)} (corrected for small n)')
pr(f'  eta² = {fmt(eta_sq)}')

# Effect size interpretation
abs_g = abs(g_hedges)
if abs_g < 0.2:
    interp = 'negligible'
elif abs_g < 0.5:
    interp = 'small'
elif abs_g < 0.8:
    interp = 'medium'
else:
    interp = 'large'
pr(f'  Effect size interpretation: |g|={fmt(abs_g)} → {interp} (Cohen benchmarks: 0.2/0.5/0.8)')
pr(f'  Direction: Grad OFF (Cell 3) {">" if m2 > m1 else "<"} Grad ON (Cell 1)')
pr()

# ── 3. Bootstrap CI for mean difference (Cell 3 - Cell 1) ──
pr('=' * 70)
pr('3. BOOTSTRAP CI FOR MEAN DIFFERENCE (Cell3 - Cell1)')
pr('=' * 70)

n_boot = 10000
obs_diff = np.mean(cell3) - np.mean(cell1)
boot_diffs = np.zeros(n_boot)

for i in range(n_boot):
    b1 = np.random.choice(cell1, size=n1, replace=True)
    b3 = np.random.choice(cell3, size=n2, replace=True)
    boot_diffs[i] = np.mean(b3) - np.mean(b1)

# Percentile CI
ci_pct_lo = np.percentile(boot_diffs, 2.5)
ci_pct_hi = np.percentile(boot_diffs, 97.5)

# BCa CI
# Bias correction
z0 = stats.norm.ppf(np.mean(boot_diffs < obs_diff))

# Acceleration (jackknife)
all_data_c1 = cell1
all_data_c3 = cell3
jack_vals = []
for j in range(n1):
    jk1 = np.delete(cell1, j)
    jack_vals.append(np.mean(cell3) - np.mean(jk1))
for j in range(n2):
    jk3 = np.delete(cell3, j)
    jack_vals.append(np.mean(jk3) - np.mean(cell1))
jack_vals = np.array(jack_vals)
jack_mean = np.mean(jack_vals)
num = np.sum((jack_mean - jack_vals)**3)
den = 6 * (np.sum((jack_mean - jack_vals)**2))**1.5
a_hat = num / den if den != 0 else 0

# BCa percentiles
alpha = 0.05
z_alpha2 = stats.norm.ppf(alpha / 2)
z_1alpha2 = stats.norm.ppf(1 - alpha / 2)

def bca_percentile(z_val):
    return stats.norm.cdf(z0 + (z0 + z_val) / (1 - a_hat * (z0 + z_val)))

p_lo = bca_percentile(z_alpha2)
p_hi = bca_percentile(z_1alpha2)
p_lo = np.clip(p_lo, 0.001, 0.999)
p_hi = np.clip(p_hi, 0.001, 0.999)
ci_bca_lo = np.percentile(boot_diffs, p_lo * 100)
ci_bca_hi = np.percentile(boot_diffs, p_hi * 100)

pr(f'  Observed mean diff (Cell3 - Cell1): {fmt(obs_diff)}')
pr(f'  Bootstrap (n={n_boot}):')
pr(f'    Percentile 95% CI: [{fmt(ci_pct_lo)}, {fmt(ci_pct_hi)}]')
pr(f'    BCa 95% CI:        [{fmt(ci_bca_lo)}, {fmt(ci_bca_hi)}]')
pr(f'    Bootstrap mean: {fmt(np.mean(boot_diffs))}, std: {fmt(np.std(boot_diffs))}')
contains_zero = 'Yes' if ci_pct_lo <= 0 <= ci_pct_hi else 'No'
pr(f'    CI contains zero: {contains_zero}')
pr()

# ── 4. Effect size interpretation (summary) ──
pr('=' * 70)
pr('4. EFFECT SIZE SUMMARY')
pr('=' * 70)
pr(f'  Cohen\'s d = {fmt(d_cohen)} (raw)')
pr(f'  Hedges\' g = {fmt(g_hedges)} (small-sample corrected)')
pr(f'  eta² = {fmt(eta_sq)} (variance explained by gradient condition)')
pr(f'  Interpretation: {interp} effect')
pr(f'  Note: With n1=2, n2=3, all estimates have very wide CIs.')
pr(f'  The Hedges\' g correction is important here due to total N=5.')
pr()

# ── 5. Bayesian t-test (optional) ──
pr('=' * 70)
pr('5. BAYESIAN ANALYSIS (approximate)')
pr('=' * 70)
# JZS Bayes Factor approximation using BIC method
# BF10 ≈ exp((BIC_H0 - BIC_H1) / 2)
n_total = n1 + n2
bic_h0 = n_total * np.log(np.var(np.concatenate([cell1, cell3]), ddof=0))
combined_ss = np.sum((cell1 - m1)**2) + np.sum((cell3 - m2)**2)
bic_h1 = n_total * np.log(combined_ss / n_total) + np.log(n_total)
bf10_approx = np.exp((bic_h0 - bic_h1) / 2)

pr(f'  BF10 (BIC approximation): {fmt(bf10_approx)}')
if bf10_approx < 1/3:
    bf_interp = 'moderate evidence for H0 (no effect)'
elif bf10_approx < 1:
    bf_interp = 'anecdotal evidence for H0'
elif bf10_approx < 3:
    bf_interp = 'anecdotal evidence for H1 (effect exists)'
elif bf10_approx < 10:
    bf_interp = 'moderate evidence for H1'
else:
    bf_interp = 'strong evidence for H1'
pr(f'  Interpretation: {bf_interp}')
pr(f'  (Jeffreys scale: <1/3 moderate H0, 1/3-1 anecdotal H0, 1-3 anecdotal H1, 3-10 moderate H1)')
pr()

# ── 6. One-way ANOVA: Cell 1 vs Cell 3 vs Vanilla ──
pr('=' * 70)
pr('6. ONE-WAY ANOVA: 3 groups (Cell1 vs Cell3 vs Vanilla)')
pr('=' * 70)

all_data = np.concatenate([cell1, cell3, vanilla])
all_groups = [0]*n1 + [1]*n2 + [2]*len(vanilla)
grand_mean = np.mean(all_data)
N = len(all_data)
k = 3

# SS calculations
group_means = [np.mean(g) for g in [cell1, cell3, vanilla]]
group_ns = [n1, n2, len(vanilla)]

ss_between = sum(ni * (mi - grand_mean)**2 for ni, mi in zip(group_ns, group_means))
ss_within = sum(np.sum((g - np.mean(g))**2) for g in [cell1, cell3, vanilla])
ss_total = np.sum((all_data - grand_mean)**2)

df_between = k - 1
df_within = N - k
ms_between = ss_between / df_between
ms_within = ss_within / df_within if df_within > 0 else float('nan')

if df_within > 0 and ms_within > 0:
    F_stat = ms_between / ms_within
    p_anova = 1 - stats.f.cdf(F_stat, df_between, df_within)
else:
    F_stat = float('nan')
    p_anova = float('nan')

eta_sq_anova = ss_between / ss_total if ss_total > 0 else float('nan')
omega_sq = (ss_between - df_between * ms_within) / (ss_total + ms_within) if (ss_total + ms_within) > 0 else float('nan')

pr(f'  Grand mean: {fmt(grand_mean)}')
pr(f'  SS_between={fmt(ss_between)}, SS_within={fmt(ss_within)}, SS_total={fmt(ss_total)}')
pr(f'  df_between={df_between}, df_within={df_within}')
pr(f'  MS_between={fmt(ms_between)}, MS_within={fmt(ms_within)}')
pr(f'  F({df_between},{df_within}) = {fmt(F_stat)}, p = {fmt(p_anova)}')
pr(f'  eta² = {fmt(eta_sq_anova)}')
pr(f'  omega² = {fmt(omega_sq)}')

if omega_sq < 0:
    pr(f'  Note: omega² < 0 indicates no meaningful effect (set to 0 in practice)')

pr()
pr(f'  WARNING: Vanilla has n=1, so within-group variance for that cell is 0.')
pr(f'  ANOVA results should be interpreted with extreme caution.')
pr()

# ── 7. Post-hoc pairwise comparisons ──
pr('=' * 70)
pr('7. POST-HOC PAIRWISE COMPARISONS')
pr('=' * 70)

pairs = [
    ('Cell1 vs Cell3', cell1, cell3),
    ('Cell1 vs Vanilla', cell1, vanilla),
    ('Cell3 vs Vanilla', cell3, vanilla),
]

pr('  Using Welch\'s t-test with Bonferroni correction (3 comparisons)')
pr()
alpha_bonf = 0.05 / 3

for name, g1, g2 in pairs:
    n_a, n_b = len(g1), len(g2)
    m_a, m_b = np.mean(g1), np.mean(g2)

    if n_a < 2 or n_b < 2:
        pr(f'  {name}: SKIPPED (n_a={n_a}, n_b={n_b}; need n≥2 in both groups for t-test)')
        pr()
        continue

    t_pw, p_pw = stats.ttest_ind(g1, g2, equal_var=False)
    s_a, s_b = np.std(g1, ddof=1), np.std(g2, ddof=1)
    sp = np.sqrt(((n_a-1)*s_a**2 + (n_b-1)*s_b**2) / (n_a+n_b-2))
    d_pw = (m_a - m_b) / sp if sp > 0 else float('nan')

    p_adj = min(p_pw * 3, 1.0)  # Bonferroni
    sig = '*' if p_adj < 0.05 else 'n.s.'

    pr(f'  {name}:')
    pr(f'    diff = {fmt(m_a - m_b)}, t = {fmt(t_pw)}, p_raw = {fmt(p_pw)}, p_bonf = {fmt(p_adj)} {sig}')
    pr(f'    Cohen\'s d = {fmt(d_pw)}')
    pr()

# ── 8. Summary ──
pr('=' * 70)
pr('8. SUMMARY')
pr('=' * 70)
pr(f'  Gradient effect (Cell1 vs Cell3):')
pr(f'    Grad ON mean = {fmt(m1)}, Grad OFF mean = {fmt(m2)}, diff = {fmt(m1-m2)}')
pr(f'    Welch t = {fmt(t_stat)}, p = {fmt(p_val)}, Hedges g = {fmt(g_hedges)}')
pr(f'    Bootstrap 95% CI for (Cell3-Cell1): [{fmt(ci_pct_lo)}, {fmt(ci_pct_hi)}]')
pr(f'    Interpretation: {interp} effect, {"significant" if p_val < 0.05 else "not significant"} at α=0.05')
pr(f'  One-way ANOVA (3 groups):')
pr(f'    F = {fmt(F_stat)}, p = {fmt(p_anova)}, eta² = {fmt(eta_sq_anova)}')
pr(f'  Caveat: Very small samples (N=6 total). Power is extremely low.')
pr(f'    Minimum detectable effect at 80% power with these n\'s ≈ d=3.0+')

# Save results
out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/partial_anova_v2_results.txt'
with open(out_path, 'w') as f:
    f.write('\n'.join(out_lines) + '\n')
print(f'\nResults saved to {out_path}')
