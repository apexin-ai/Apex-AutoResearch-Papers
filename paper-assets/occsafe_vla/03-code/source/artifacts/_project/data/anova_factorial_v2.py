# 2x2 Factorial ANOVA: Gradient Flow (ON/OFF) × Norm Type (BN/LN) on CAR metric
# Analyzes v2 factorial data with Type III SS for unbalanced design (n=2,3,3,3)

import sys
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import warnings
warnings.filterwarnings('ignore')

VANILLA_CAR = 0.768

data = {
    'grad_on_bn': [0.746, 0.654],
    'grad_on_ln': [0.766, 0.718, 0.744],
    'grad_off_bn': [0.746, 0.744, 0.780],
    'grad_off_ln': [0.792, 0.756, 0.748],
}

rows = []
for key, vals in data.items():
    parts = key.split('_')
    grad = 'ON' if parts[1] == 'on' else 'OFF'
    norm = 'BN' if parts[2] == 'bn' else 'LN'
    for v in vals:
        rows.append({'gradient_flow': grad, 'norm_type': norm, 'car': v})
df = pd.DataFrame(rows)

out_lines = []
def p(s=''):
    out_lines.append(s)
    print(s)

p("=" * 70)
p("2×2 Factorial ANOVA: Gradient Flow × Norm Type on CAR")
p("=" * 70)

p("\n--- Descriptive Statistics ---")
for key, vals in data.items():
    arr = np.array(vals)
    p(f"  {key:15s}: n={len(vals)}, mean={arr.mean():.4f}, sd={arr.std(ddof=1):.4f}, "
      f"range=[{arr.min():.3f}, {arr.max():.3f}]")

cell_means = df.groupby(['gradient_flow', 'norm_type'])['car'].mean()
margin_grad = df.groupby('gradient_flow')['car'].mean()
margin_norm = df.groupby('norm_type')['car'].mean()
grand_mean = df['car'].mean()

p(f"\n  Marginal means:")
p(f"    Grad ON:  {margin_grad['ON']:.4f}   Grad OFF: {margin_grad['OFF']:.4f}")
p(f"    BN:       {margin_norm['BN']:.4f}   LN:       {margin_norm['LN']:.4f}")
p(f"    Grand mean: {grand_mean:.4f}")

# --- Assumption checks ---
p("\n--- Assumption Checks ---")

groups = [np.array(v) for v in data.values()]
group_labels = list(data.keys())

# Levene's test
lev_stat, lev_p = stats.levene(*groups)
p(f"  Levene's test: F={lev_stat:.4f}, p={lev_p:.4f}", )
if lev_p < 0.05:
    p("    ⚠ Homogeneity of variance assumption violated (p < 0.05)")
else:
    p("    ✓ Homogeneity of variance assumption met")

# Shapiro-Wilk per cell
p("  Shapiro-Wilk normality tests:")
all_normal = True
for key, vals in data.items():
    if len(vals) < 3:
        p(f"    {key}: n={len(vals)}, too few observations for Shapiro-Wilk")
        all_normal = False
    else:
        w, sw_p = stats.shapiro(vals)
        status = "✓" if sw_p >= 0.05 else "⚠ non-normal"
        if sw_p < 0.05:
            all_normal = False
        p(f"    {key}: W={w:.4f}, p={sw_p:.4f} {status}")

p(f"\n  ⚠ Note: Cell 'grad_on_bn' has only n=2 observations.")
p(f"    This severely limits statistical power and assumption testing.")
p(f"    All results should be interpreted with caution.")

# --- 2×2 ANOVA (Type III SS) ---
p("\n--- 2×2 ANOVA (Type III Sum of Squares) ---")

model = ols('car ~ C(gradient_flow, Sum) * C(norm_type, Sum)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=3)

p(f"\n  {'Source':<25s} {'SS':>10s} {'df':>5s} {'F':>10s} {'p':>10s}")
p(f"  {'-'*60}")
def pretty_label(idx_str):
    s = str(idx_str)
    if ':' in s:
        return 'Gradient × Norm'
    if 'gradient' in s.lower():
        return 'Gradient Flow'
    if 'norm' in s.lower():
        return 'Norm Type'
    if s == 'Intercept':
        return 'Intercept'
    return s

for idx, row in anova_table.iterrows():
    label = pretty_label(idx)
    ss = row.get('sum_sq', np.nan)
    d = row.get('df', np.nan)
    f_val = row.get('F', np.nan)
    p_val = row.get('PR(>F)', np.nan)
    if pd.notna(f_val):
        p(f"  {label:<25s} {ss:>10.6f} {d:>5.0f} {f_val:>10.4f} {p_val:>10.4f}")
    else:
        p(f"  {label:<25s} {ss:>10.6f} {d:>5.0f} {'':>10s} {'':>10s}")

ss_residual = anova_table.loc['Residual', 'sum_sq']
df_residual = anova_table.loc['Residual', 'df']

# --- Effect Sizes ---
p("\n--- Effect Sizes ---")

p("\n  Partial η² (from ANOVA):")
for idx, row in anova_table.iterrows():
    if idx in ['Intercept', 'Residual']:
        continue
    ss_effect = row['sum_sq']
    partial_eta2 = ss_effect / (ss_effect + ss_residual)
    label = pretty_label(idx)
    p(f"    {label:<25s}: η²_p = {partial_eta2:.4f}")

def cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    m1, m2 = np.mean(g1), np.mean(g2)
    s1, s2 = np.var(g1, ddof=1), np.var(g2, ddof=1)
    sp = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    return (m2 - m1) / sp if sp > 0 else 0.0

grad_on_all = df[df['gradient_flow'] == 'ON']['car'].values
grad_off_all = df[df['gradient_flow'] == 'OFF']['car'].values
bn_all = df[df['norm_type'] == 'BN']['car'].values
ln_all = df[df['norm_type'] == 'LN']['car'].values

d_grad = cohens_d(grad_on_all, grad_off_all)
d_norm = cohens_d(bn_all, ln_all)

p(f"\n  Cohen's d (pairwise):")
p(f"    Grad OFF vs ON:   d = {d_grad:.4f}  (positive = OFF > ON)")
p(f"    LN vs BN:         d = {d_norm:.4f}  (positive = LN > BN)")

p(f"\n  Cohen's f (overall):")
for idx, row in anova_table.iterrows():
    if idx in ['Intercept', 'Residual']:
        continue
    ss_effect = row['sum_sq']
    partial_eta2 = ss_effect / (ss_effect + ss_residual)
    f_effect = np.sqrt(partial_eta2 / (1 - partial_eta2)) if partial_eta2 < 1 else float('inf')
    label = pretty_label(idx)
    p(f"    {label:<25s}: f = {f_effect:.4f}")

# --- Simple Effects ---
p("\n--- Simple Effects Analysis ---")
p("  (Independent samples t-tests within each level of the other factor)\n")

def simple_effect(g1, g2, label1, label2, factor_label):
    t_stat, t_p = stats.ttest_ind(g1, g2, equal_var=True)
    d = cohens_d(g1, g2)
    p(f"  {factor_label}:")
    p(f"    {label1}: mean={np.mean(g1):.4f} (n={len(g1)})")
    p(f"    {label2}: mean={np.mean(g2):.4f} (n={len(g2)})")
    p(f"    t={t_stat:.4f}, p={t_p:.4f}, Cohen's d={d:.4f}")
    p(f"    Mean diff = {np.mean(g2) - np.mean(g1):.4f}")
    p()

grad_on_bn = np.array(data['grad_on_bn'])
grad_on_ln = np.array(data['grad_on_ln'])
grad_off_bn = np.array(data['grad_off_bn'])
grad_off_ln = np.array(data['grad_off_ln'])

simple_effect(grad_on_bn, grad_off_bn, 'Grad ON+BN', 'Grad OFF+BN',
              'Gradient Flow effect within BN')
simple_effect(grad_on_ln, grad_off_ln, 'Grad ON+LN', 'Grad OFF+LN',
              'Gradient Flow effect within LN')
simple_effect(grad_on_bn, grad_on_ln, 'BN+Grad ON', 'LN+Grad ON',
              'Norm Type effect within Grad ON')
simple_effect(grad_off_bn, grad_off_ln, 'BN+Grad OFF', 'LN+Grad OFF',
              'Norm Type effect within Grad OFF')

# --- Bootstrap CIs ---
p("--- Bootstrap 95% CI for Cell Means (10000 resamples) ---\n")

rng = np.random.default_rng(42)
n_boot = 10000

for key, vals in data.items():
    arr = np.array(vals)
    boot_means = np.array([rng.choice(arr, size=len(arr), replace=True).mean()
                           for _ in range(n_boot)])
    ci_lo, ci_hi = np.percentile(boot_means, [2.5, 97.5])
    p(f"  {key:15s}: mean={arr.mean():.4f}, 95% CI=[{ci_lo:.4f}, {ci_hi:.4f}]")

p()

# --- Comparison vs Vanilla ---
p("--- Comparison vs Vanilla (CAR = 0.768) ---\n")

for key, vals in data.items():
    arr = np.array(vals)
    cell_mean = arr.mean()
    diff = cell_mean - VANILLA_CAR
    direction = "above" if diff > 0 else "below"
    pct = abs(diff) / VANILLA_CAR * 100
    t_stat, t_p = stats.ttest_1samp(arr, VANILLA_CAR)
    p(f"  {key:15s}: mean={cell_mean:.4f}, diff={diff:+.4f} ({pct:.1f}% {direction}), "
      f"t={t_stat:.4f}, p={t_p:.4f}")

p()
p("  Note: One-sample t-tests vs Vanilla=0.768. With n=2-3 per cell,")
p("  these tests have very low power. Non-significant p-values should")
p("  NOT be interpreted as evidence of no difference.")

# --- Overall summary ---
p("\n--- Summary & Caveats ---")
p(f"  Grand mean across OCC conditions: {grand_mean:.4f} vs Vanilla: {VANILLA_CAR:.3f}")
p(f"  Difference: {grand_mean - VANILLA_CAR:+.4f}")
p()
p("  ⚠ Key limitations:")
p("    1. Very small sample sizes (n=2 to 3 per cell). Statistical power is extremely low.")
p("    2. Cell 'grad_on_bn' has only n=2, making variance estimates unreliable.")
p("    3. Unbalanced design requires Type III SS (used here).")
p("    4. With total N=11, even medium-to-large effects may not reach significance.")
p("    5. Bootstrap CIs for n=2 cells have limited resolution (only 3 unique resampled means).")
p("    6. These results are best treated as descriptive/exploratory, not confirmatory.")

# --- Non-parametric alternative ---
p("\n--- Non-parametric Check (Kruskal-Wallis across 4 cells) ---")
h_stat, kw_p = stats.kruskal(*groups)
p(f"  Kruskal-Wallis H={h_stat:.4f}, p={kw_p:.4f}")
if kw_p < 0.05:
    p("  Significant overall difference across cells (non-parametric)")
else:
    p("  No significant overall difference across cells (non-parametric)")

# Save results
results_path = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/anova_factorial_v2_results.txt'
with open(results_path, 'w') as f:
    f.write('\n'.join(out_lines))
print(f"\nResults saved to {results_path}")
