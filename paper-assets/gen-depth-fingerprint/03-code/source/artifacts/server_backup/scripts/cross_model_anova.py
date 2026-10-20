import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('/root/gen-depth-fingerprint/data/cross-model-chains/features.csv')
features = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay', 'ttr', 'hapax_ratio']

# ── Analysis 1: Two-way ANOVA on depths 1-4 (fully crossed) ──
df_gen = df[df['depth'] > 0].copy()
print(f"Analysis 1: Two-way ANOVA on depths 1–4 (n={len(df_gen)})")
print(f"Depths: {sorted(df_gen['depth'].unique())}")
print(f"Generators: {sorted(df_gen['generator_at_depth'].unique())}")
print()

results = []
for feat in features:
    model = ols(f'{feat} ~ C(depth) + C(generator_at_depth) + C(depth):C(generator_at_depth)', data=df_gen).fit()
    table = sm.stats.anova_lm(model, typ=2)
    ss_resid = table.loc['Residual', 'sum_sq']
    row = {'feature': feat}
    for factor, label in [('C(depth)', 'depth'), ('C(generator_at_depth)', 'generator'), ('C(depth):C(generator_at_depth)', 'interaction')]:
        ss = table.loc[factor, 'sum_sq']
        row[f'eta2_{label}'] = ss / (ss + ss_resid)
        row[f'F_{label}'] = table.loc[factor, 'F']
        row[f'p_{label}'] = table.loc[factor, 'PR(>F)']
    results.append(row)

rdf = pd.DataFrame(results)

print("=" * 110)
print("Two-way ANOVA (depths 1–4): η²(partial)")
print("=" * 110)
print(f"{'Feature':<15} {'η²(depth)':>12} {'η²(gen)':>12} {'η²(inter)':>12} {'F(depth)':>12} {'F(gen)':>12} {'F(inter)':>12}")
print("-" * 110)
for _, r in rdf.iterrows():
    def sig(p):
        if p < 0.001: return '***'
        if p < 0.01: return ' **'
        if p < 0.05: return '  *'
        return ' ns'
    print(f"{r['feature']:<15} {r['eta2_depth']:>8.4f}{sig(r['p_depth']):>4} {r['eta2_generator']:>8.4f}{sig(r['p_generator']):>4} {r['eta2_interaction']:>8.4f}{sig(r['p_interaction']):>4} {r['F_depth']:>12.2f} {r['F_generator']:>12.2f} {r['F_interaction']:>12.2f}")

print()
gen_eta2 = rdf['eta2_generator'].values
depth_eta2 = rdf['eta2_depth'].values
inter_eta2 = rdf['eta2_interaction'].values
print(f"Depth η² range:       [{depth_eta2.min():.4f}, {depth_eta2.max():.4f}], mean={depth_eta2.mean():.4f}")
print(f"Generator η² range:   [{gen_eta2.min():.4f}, {gen_eta2.max():.4f}], mean={gen_eta2.mean():.4f}")
print(f"Interaction η² range: [{inter_eta2.min():.4f}, {inter_eta2.max():.4f}], mean={inter_eta2.mean():.4f}")
print(f"Generator η² < 10% for all features: {all(v < 0.10 for v in gen_eta2)}")
print()

# ── Analysis 2: One-way ANOVA across all depths (0-4) ──
print("=" * 80)
print("One-way ANOVA (depths 0–4): depth main effect")
print("=" * 80)
print(f"{'Feature':<15} {'η²(depth)':>12} {'F':>12} {'p':>14}")
print("-" * 80)
oneway = []
for feat in features:
    model = ols(f'{feat} ~ C(depth)', data=df).fit()
    table = sm.stats.anova_lm(model, typ=2)
    ss = table.loc['C(depth)', 'sum_sq']
    ss_r = table.loc['Residual', 'sum_sq']
    eta2 = ss / (ss + ss_r)
    f_val = table.loc['C(depth)', 'F']
    p_val = table.loc['C(depth)', 'PR(>F)']
    def sig(p):
        if p < 0.001: return '***'
        if p < 0.01: return ' **'
        if p < 0.05: return '  *'
        return ' ns'
    print(f"{feat:<15} {eta2:>8.4f}{sig(p_val):>4} {f_val:>12.2f} {p_val:>14.2e}")
    oneway.append({'feature': feat, 'eta2_depth_oneway': eta2, 'F_depth_oneway': f_val, 'p_depth_oneway': p_val})

oneway_df = pd.DataFrame(oneway)

# ── Save combined results ──
out = rdf.merge(oneway_df, on='feature')
out.to_csv('/root/gen-depth-fingerprint/data/cross-model-chains/cross_model_anova.csv', index=False)
print(f"\nSaved to /root/gen-depth-fingerprint/data/cross-model-chains/cross_model_anova.csv")
