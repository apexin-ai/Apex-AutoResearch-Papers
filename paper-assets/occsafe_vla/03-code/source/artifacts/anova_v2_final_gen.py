"""
anova_v2_final_gen.py — 2x2 Factorial ANOVA with full v2 data (all cells n>=3).
Outputs anova_v2_final.txt.
"""
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import warnings
warnings.filterwarnings('ignore')

data = {
    'grad_on_bn':  [0.654, 0.746, 0.776],          # Cell 1: Full OCC BN, n=3
    'grad_on_ln':  [0.798, 0.792, 0.740, 0.762],    # Cell 2: Full OCC LN, n=4
    'grad_off_bn': [0.794, 0.762, 0.736, 0.774],    # Cell 3: Detach BN, n=4
    'grad_off_ln': [0.802, 0.826, 0.778, 0.784],      # Cell 4: Detach LN, n=4
}
vanilla = np.array([0.768, 0.748, 0.720])            # Vanilla, n=3

rows = []
for key, vals in data.items():
    parts = key.split('_')
    grad = 'ON' if parts[1] == 'on' else 'OFF'
    norm = 'BN' if parts[2] == 'bn' else 'LN'
    for v in vals:
        rows.append({'gradient_flow': grad, 'norm_type': norm, 'car': v})
df = pd.DataFrame(rows)

out = []
def p(s=''):
    out.append(s)
    print(s)

p("=" * 70)
p("2x2 FACTORIAL ANOVA: gradient_flow x norm_type on CAR (v2 data)")
p(f"Date: 2026-05-28")
p("=" * 70)

p("\n--- Cell Descriptives ---")
labels = {
    'grad_on_bn': 'Cell 1 (Full OCC BN, grad ON + BN)',
    'grad_on_ln': 'Cell 2 (Full OCC LN, grad ON + LN)',
    'grad_off_bn': 'Cell 3 (Detach BN, grad OFF + BN)',
    'grad_off_ln': 'Cell 4 (Detach LN, grad OFF + LN)',
}
for key, vals in data.items():
    a = np.array(vals)
    p(f"  {labels[key]}: n={len(vals)}, mean={a.mean():.4f}, SD={a.std(ddof=1):.4f}, range=[{a.min():.3f}, {a.max():.3f}]")
p(f"  Vanilla baseline:                    n={len(vanilla)}, mean={vanilla.mean():.4f}, SD={vanilla.std(ddof=1):.4f}, range=[{vanilla.min():.3f}, {vanilla.max():.3f}]")

margin_grad = df.groupby('gradient_flow')['car'].agg(['mean', 'count'])
margin_norm = df.groupby('norm_type')['car'].agg(['mean', 'count'])
p("\n--- Marginal Means ---")
p(f"  Gradient ON:  mean={margin_grad.loc['ON','mean']:.4f} (n={int(margin_grad.loc['ON','count'])})")
p(f"  Gradient OFF: mean={margin_grad.loc['OFF','mean']:.4f} (n={int(margin_grad.loc['OFF','count'])})")
p(f"  BN:           mean={margin_norm.loc['BN','mean']:.4f} (n={int(margin_norm.loc['BN','count'])})")
p(f"  LN:           mean={margin_norm.loc['LN','mean']:.4f} (n={int(margin_norm.loc['LN','count'])})")

# 2x2 ANOVA (Type III)
p("\n" + "=" * 70)
p("2x2 FACTORIAL ANOVA (Type III Sum of Squares)")
p("=" * 70)

model = ols('car ~ C(gradient_flow, Sum) * C(norm_type, Sum)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=3)

ss_resid = anova_table.loc['Residual', 'sum_sq']
df_resid = anova_table.loc['Residual', 'df']

p(f"\n{'Source':<50s} {'SS':>10s} {'df':>5s} {'F':>10s} {'p':>10s} {'η²_p':>10s}")
p("-" * 85)
for idx, row in anova_table.iterrows():
    if idx == 'Intercept':
        continue
    label = idx
    if 'gradient' in str(idx).lower():
        label = '  C(gradient_flow)'
    elif 'norm' in str(idx).lower() and ':' not in str(idx):
        label = '  C(norm_type)'
    elif ':' in str(idx):
        label = '  C(gradient_flow):C(norm_type)'
    elif idx == 'Residual':
        label = '  Residual'
    ss = row['sum_sq']
    d = row['df']
    f_val = row.get('F', np.nan)
    p_val = row.get('PR(>F)', np.nan)
    if pd.notna(f_val):
        eta2 = ss / (ss + ss_resid)
        p(f"{label:<50s} {ss:>10.6f} {d:>5.0f} {f_val:>10.3f} {p_val:>10.4f} {eta2:>10.4f}")
    else:
        p(f"{label:<50s} {ss:>10.6f} {d:>5.0f}")
p("-" * 85)
p("Significance: *** p<.001, ** p<.01, * p<.05, † p<.10")

# Effect sizes
def cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    s1, s2 = np.var(g1, ddof=1), np.var(g2, ddof=1)
    sp = np.sqrt(((n1-1)*s1 + (n2-1)*s2) / (n1+n2-2))
    return (np.mean(g2) - np.mean(g1)) / sp if sp > 0 else 0.0

# Cell vs Vanilla
p("\n" + "=" * 70)
p("WELCH'S T-TESTS: Each Cell vs Vanilla")
p("=" * 70)
p(f"\nVanilla: mean={vanilla.mean():.4f}, SD={vanilla.std(ddof=1):.4f}, n={len(vanilla)}")
p(f"\n{'Cell':<50s} {'mean':>8s} {'t':>8s} {'p(2-tail)':>10s} {'Cohen d':>10s}")
p("-" * 90)
for key, vals in data.items():
    a = np.array(vals)
    t, pv = stats.ttest_ind(a, vanilla, equal_var=False)
    d = cohens_d(vanilla, a)
    p(f"  {labels[key]:<48s} {a.mean():>8.4f} {t:>8.3f} {pv:>10.4f} {d:>10.3f}")

# Simple effects
p("\n" + "=" * 70)
p("SIMPLE EFFECTS: LN-BN within each gradient condition")
p("=" * 70)
on_bn = np.array(data['grad_on_bn'])
on_ln = np.array(data['grad_on_ln'])
off_bn = np.array(data['grad_off_bn'])
off_ln = np.array(data['grad_off_ln'])

diff_on = on_ln.mean() - on_bn.mean()
diff_off = off_ln.mean() - off_bn.mean()
p(f"\n  Under gradient ON:  LN-BN = {on_ln.mean():.4f} - {on_bn.mean():.4f} = {diff_on:+.4f} ({diff_on*100:+.1f}pp)")
p(f"  Under gradient OFF: LN-BN = {off_ln.mean():.4f} - {off_bn.mean():.4f} = {diff_off:+.4f} ({diff_off*100:+.1f}pp)")

d_cell4_vanilla = cohens_d(vanilla, off_ln)
t_c4v, p_c4v = stats.ttest_ind(off_ln, vanilla, equal_var=False)
p(f"\n  Cell 4 vs Vanilla: Cohen's d={d_cell4_vanilla:.2f}, t={t_c4v:.3f}, p={p_c4v:.3f}")

d_cell2_vanilla = cohens_d(vanilla, on_ln)
p(f"  Cell 2 vs Vanilla: Cohen's d={d_cell2_vanilla:+.2f}")

p("\n" + "=" * 70)
p("SUMMARY")
p("=" * 70)
for idx, row in anova_table.iterrows():
    if idx in ['Intercept', 'Residual']:
        continue
    f_val = row.get('F', np.nan)
    p_val = row.get('PR(>F)', np.nan)
    eta2 = row['sum_sq'] / (row['sum_sq'] + ss_resid)
    if 'gradient' in str(idx).lower() and ':' not in str(idx):
        p(f"  Gradient flow: F={f_val:.2f}, p={p_val:.3f}, η²={eta2:.3f}")
    elif 'norm' in str(idx).lower() and ':' not in str(idx):
        p(f"  Norm type:     F={f_val:.2f}, p={p_val:.3f}, η²={eta2:.3f}")
    elif ':' in str(idx):
        p(f"  Interaction:   F={f_val:.2f}, p={p_val:.3f}, η²={eta2:.3f}")

p(f"\n  Cell 4 vs Vanilla: Cohen's d={d_cell4_vanilla:.2f}, p={p_c4v:.3f}")
p(f"  Cell 2 vs Vanilla: d={d_cell2_vanilla:+.2f}")
p(f"  LN-BN under gradient ON:  {diff_on*100:+.1f}pp")
p(f"  LN-BN under gradient OFF: {diff_off*100:+.1f}pp")

# Save
out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/anova_v2_final.txt'
with open(out_path, 'w') as f:
    f.write('\n'.join(out))
print(f"\nSaved to {out_path}")
