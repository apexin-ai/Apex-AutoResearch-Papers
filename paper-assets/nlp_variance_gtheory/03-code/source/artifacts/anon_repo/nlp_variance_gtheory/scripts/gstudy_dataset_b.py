import pandas as pd
import numpy as np
import json
import os

df = pd.read_csv('./results/analysis/cross_model_2way_precision.csv')
N = len(df)
DV = 'correct'
grand_mean = df[DV].mean()
total_var = df[DV].var(ddof=1)
ss_total = total_var * (N - 1)
print(f"N={N}, grand_mean={grand_mean:.4f}, total_var={total_var:.6f}, SS_total={ss_total:.2f}")

facets = ['model', 'precision', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']

# ========== Main effects ==========
results = {}
for facet in facets:
    group_means = df.groupby(facet)[DV].mean()
    n_levels = len(group_means)
    n_per_level = N // n_levels
    ss = n_per_level * ((group_means - grand_mean) ** 2).sum()
    df_effect = n_levels - 1
    ms = ss / df_effect if df_effect > 0 else 0
    results[facet] = {'n_levels': n_levels, 'ss': float(ss), 'df': df_effect, 'ms': float(ms)}
    print(f"  {facet}: {n_levels} levels, SS={ss:.6f}, range=[{group_means.min():.4f}, {group_means.max():.4f}]")

# ========== All 2-way interactions ==========
interactions_list = []
for i, f1 in enumerate(facets):
    for f2 in facets[i+1:]:
        interactions_list.append((f1, f2))

for f1, f2 in interactions_list:
    cell_means = df.groupby([f1, f2])[DV].mean()
    marginal_A = df.groupby(f1)[DV].mean()
    marginal_B = df.groupby(f2)[DV].mean()
    n_a, n_b = df[f1].nunique(), df[f2].nunique()
    n_per_cell = N // (n_a * n_b)

    interaction_ss = 0
    for (a, b), cell_mean in cell_means.items():
        expected = grand_mean + (marginal_A[a] - grand_mean) + (marginal_B[b] - grand_mean)
        interaction_ss += (cell_mean - expected) ** 2
    interaction_ss *= n_per_cell

    df_int = (n_a - 1) * (n_b - 1)
    ms_int = interaction_ss / df_int if df_int > 0 else 0
    key = f"{f1}:{f2}"
    results[key] = {'n_levels': n_a * n_b, 'ss': float(interaction_ss), 'df': df_int, 'ms': float(ms_int)}

# ========== Variance percentages ==========
all_ss = {k: v['ss'] for k, v in results.items()}
ss_accounted = sum(all_ss.values())
ss_residual = ss_total - ss_accounted
all_ss['residual'] = max(0, ss_residual)
total_ss_sum = sum(all_ss.values())
variance_pct = {k: v / total_ss_sum * 100 for k, v in all_ss.items()}

print("\n=== Variance Components (% of total SS) ===")
for k, v in sorted(variance_pct.items(), key=lambda x: -x[1]):
    if v > 0.01:
        print(f"  {k}: {v:.2f}%")

# ========== G coefficients ==========
sigma2_total = total_var
components = {k: v / 100 * sigma2_total for k, v in variance_pct.items()}

n_model, n_prec, n_temp = 2, 2, 2
n_prompt, n_seed, n_order, n_item = 6, 6, 4, 200

# G_item: universe score = item difficulty
sigma2_item = components.get('item_id', 0)
sigma2_delta_item = (
    components.get('model:item_id', 0) / n_model +
    components.get('precision:item_id', 0) / n_prec +
    components.get('temperature:item_id', 0) / n_temp +
    components.get('prompt_template:item_id', 0) / n_prompt +
    components.get('seed:item_id', 0) / n_seed +
    components.get('ordering:item_id', 0) / n_order +
    components.get('residual', 0) / (n_model * n_prec * n_temp * n_prompt * n_seed * n_order)
)
G_item = sigma2_item / (sigma2_item + sigma2_delta_item) if (sigma2_item + sigma2_delta_item) > 0 else 0
print(f"\nG_item = {G_item:.4f}")

# G_condition: object = model x precision x temperature conditions
sigma2_tau_cond = (
    components.get('model', 0) +
    components.get('precision', 0) +
    components.get('temperature', 0) +
    components.get('model:precision', 0) +
    components.get('model:temperature', 0) +
    components.get('precision:temperature', 0)
)

sigma2_delta_cond = (
    components.get('model:item_id', 0) / n_item +
    components.get('precision:item_id', 0) / n_item +
    components.get('temperature:item_id', 0) / n_item +
    components.get('model:prompt_template', 0) / n_prompt +
    components.get('model:seed', 0) / n_seed +
    components.get('model:ordering', 0) / n_order +
    components.get('precision:prompt_template', 0) / n_prompt +
    components.get('precision:seed', 0) / n_seed +
    components.get('precision:ordering', 0) / n_order +
    components.get('temperature:prompt_template', 0) / n_prompt +
    components.get('temperature:seed', 0) / n_seed +
    components.get('temperature:ordering', 0) / n_order +
    components.get('prompt_template:item_id', 0) / (n_prompt * n_item) +
    components.get('seed:item_id', 0) / (n_seed * n_item) +
    components.get('ordering:item_id', 0) / (n_order * n_item) +
    components.get('residual', 0) / (n_prompt * n_seed * n_order * n_item)
)
G_cond = sigma2_tau_cond / (sigma2_tau_cond + sigma2_delta_cond) if (sigma2_tau_cond + sigma2_delta_cond) > 0 else 0
print(f"G_condition = {G_cond:.4f}")

# ========== D-study ==========
print("\nD-study: G_item vs n_models")
d_study_models = {}
for n_m in [1, 2, 3, 4, 5, 10]:
    delta = (
        components.get('model:item_id', 0) / n_m +
        components.get('precision:item_id', 0) / n_prec +
        components.get('temperature:item_id', 0) / n_temp +
        components.get('prompt_template:item_id', 0) / n_prompt +
        components.get('seed:item_id', 0) / n_seed +
        components.get('ordering:item_id', 0) / n_order +
        components.get('residual', 0) / (n_m * n_prec * n_temp * n_prompt * n_seed * n_order)
    )
    g = sigma2_item / (sigma2_item + delta) if (sigma2_item + delta) > 0 else 0
    d_study_models[str(n_m)] = round(g, 4)
    print(f"  n_models={n_m}: G_item={g:.4f}")

print("\nD-study: G_item vs n_prompts")
d_study_prompts = {}
for n_p in [1, 2, 3, 6, 10, 20]:
    delta = (
        components.get('model:item_id', 0) / n_model +
        components.get('precision:item_id', 0) / n_prec +
        components.get('temperature:item_id', 0) / n_temp +
        components.get('prompt_template:item_id', 0) / n_p +
        components.get('seed:item_id', 0) / n_seed +
        components.get('ordering:item_id', 0) / n_order +
        components.get('residual', 0) / (n_model * n_prec * n_temp * n_p * n_seed * n_order)
    )
    g = sigma2_item / (sigma2_item + delta) if (sigma2_item + delta) > 0 else 0
    d_study_prompts[str(n_p)] = round(g, 4)
    print(f"  n_prompts={n_p}: G_item={g:.4f}")

print("\nD-study: G_item vs n_seeds")
d_study_seeds = {}
for n_s in [1, 2, 3, 6, 10, 20]:
    delta = (
        components.get('model:item_id', 0) / n_model +
        components.get('precision:item_id', 0) / n_prec +
        components.get('temperature:item_id', 0) / n_temp +
        components.get('prompt_template:item_id', 0) / n_prompt +
        components.get('seed:item_id', 0) / n_s +
        components.get('ordering:item_id', 0) / n_order +
        components.get('residual', 0) / (n_model * n_prec * n_temp * n_prompt * n_s * n_order)
    )
    g = sigma2_item / (sigma2_item + delta) if (sigma2_item + delta) > 0 else 0
    d_study_seeds[str(n_s)] = round(g, 4)
    print(f"  n_seeds={n_s}: G_item={g:.4f}")

# ========== Comparison with unbalanced ==========
print("\n=== Comparison: Balanced vs Unbalanced ===")
unbalanced = {
    'item_id': 37.90, 'model:item_id': 26.20, 'residual': 24.50,
    'prompt_template:item_id': 3.60, 'model': 3.10, 'ordering:item_id': 1.80,
    'seed:item_id': 0.50, 'temperature:item_id': 0.30,
    'G_item': 0.707
}
print(f"{'Component':>35s}  {'Unbalanced':>10s}  {'Balanced':>10s}  {'Delta':>8s}")
for k in ['item_id', 'model:item_id', 'residual', 'prompt_template:item_id', 'model',
           'ordering:item_id', 'seed:item_id', 'temperature:item_id']:
    ub = unbalanced.get(k, 0)
    bal = variance_pct.get(k, 0)
    print(f"  {k:>33s}: {ub:8.2f}%  {bal:8.2f}%  {bal-ub:+7.2f}")

# New components only in balanced (precision-related)
print("\n  --- New in balanced (precision facet) ---")
for k in sorted(variance_pct.keys()):
    if 'precision' in k and variance_pct[k] > 0.01:
        print(f"  {k:>33s}:     N/A   {variance_pct[k]:8.2f}%")

print(f"\n  G_item:    unbalanced={unbalanced['G_item']:.4f}  balanced={G_item:.4f}  delta={G_item - unbalanced['G_item']:+.4f}")
print(f"  G_condition: {G_cond:.4f}")

# ========== Save ==========
os.makedirs('./results/analysis', exist_ok=True)
output = {
    'dataset': 'cross_model_2way_precision (balanced)',
    'n_records': int(N),
    'design': {
        'models': 2, 'precisions': 2, 'temperatures': 2,
        'prompt_templates': 6, 'seeds': 6, 'orderings': 4, 'items': 200,
        'description': '2 models (Llama, Gemma) x 2 precisions (bf16, fp32) x 2 temps (0.3, 0.7) x 6 prompts x 6 seeds x 4 orderings x 200 items'
    },
    'grand_mean': round(float(grand_mean), 4),
    'variance_components_pct': {k: round(v, 4) for k, v in sorted(variance_pct.items(), key=lambda x: -x[1])},
    'G_item': round(float(G_item), 4),
    'G_condition': round(float(G_cond), 4),
    'd_study': {
        'vary_n_models': d_study_models,
        'vary_n_prompts': d_study_prompts,
        'vary_n_seeds': d_study_seeds
    },
    'comparison_with_unbalanced': {
        'unbalanced_N': 325600,
        'balanced_N': 230400,
        'unbalanced_G_item': 0.707,
        'balanced_G_item': round(float(G_item), 4),
        'notes': 'Unbalanced included temp=0.0 (but Llama fp32 missing at temp=0.0); balanced excluded temp=0.0'
    }
}
with open('./results/analysis/dataset_b_gstudy.json', 'w') as f:
    json.dump(output, f, indent=2)
print("\nSaved to results/analysis/dataset_b_gstudy.json")
