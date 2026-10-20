import pandas as pd
import numpy as np
import json

import sys
sys.path.insert(0, '.')
from src.config.model_paths import normalize_model_name

df = pd.read_csv('results/analysis/cross_model_4way_bf16.csv')
df['model'] = df['model'].apply(normalize_model_name)
models = sorted(df['model'].unique())
print(f"Models: {models}, Total: {len(df)}")

def compute_gstudy(data):
    grand_mean = data['correct'].mean()
    N = len(data)
    total_var = data['correct'].var()
    
    facets = ['model', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']
    results = {}
    
    for facet in facets:
        if facet not in data.columns or data[facet].nunique() < 2:
            continue
        group_means = data.groupby(facet)['correct'].mean()
        n_levels = len(group_means)
        n_per_level = N // n_levels
        ss = n_per_level * ((group_means - grand_mean) ** 2).sum()
        results[facet] = ss
    
    # model x item interaction
    if data['model'].nunique() >= 2:
        cell_means = data.groupby(['model', 'item_id'])['correct'].mean()
        marg_model = data.groupby('model')['correct'].mean()
        marg_item = data.groupby('item_id')['correct'].mean()
        nm, ni = data['model'].nunique(), data['item_id'].nunique()
        npc = N // (nm * ni)
        iss = 0
        for (m, i), cm in cell_means.items():
            exp = grand_mean + (marg_model[m] - grand_mean) + (marg_item[i] - grand_mean)
            iss += (cm - exp) ** 2
        iss *= npc
        results['model:item_id'] = iss
    
    # Other interactions with item
    for f1 in ['temperature', 'prompt_template', 'seed', 'ordering']:
        if f1 not in data.columns or data[f1].nunique() < 2:
            continue
        cell_means2 = data.groupby([f1, 'item_id'])['correct'].mean()
        marg_f1 = data.groupby(f1)['correct'].mean()
        marg_item2 = data.groupby('item_id')['correct'].mean()
        na, nb = data[f1].nunique(), data['item_id'].nunique()
        npc2 = N // (na * nb)
        iss2 = 0
        for (a, b), cm in cell_means2.items():
            exp = grand_mean + (marg_f1[a] - grand_mean) + (marg_item2[b] - grand_mean)
            iss2 += (cm - exp) ** 2
        iss2 *= npc2
        results[f'{f1}:item_id'] = iss2
    
    # Convert to percentages
    ss_total = total_var * (N - 1)
    ss_residual = ss_total - sum(results.values())
    results['residual'] = max(0, ss_residual)
    total_ss = sum(results.values())
    pct = {k: v / total_ss * 100 for k, v in results.items()}
    
    # G_item
    sigma2_total = total_var
    components = {k: v / 100 * sigma2_total for k, v in pct.items()}
    sigma2_item = components.get('item_id', 0)
    n_model = data['model'].nunique()
    n_temp = data['temperature'].nunique() if 'temperature' in data.columns else 1
    n_prompt = data['prompt_template'].nunique() if 'prompt_template' in data.columns else 1
    n_seed = data['seed'].nunique() if 'seed' in data.columns else 1
    n_order = data['ordering'].nunique() if 'ordering' in data.columns else 1
    sigma2_delta = (
        components.get('model:item_id', 0) / max(n_model, 1) +
        components.get('temperature:item_id', 0) / max(n_temp, 1) +
        components.get('prompt_template:item_id', 0) / max(n_prompt, 1) +
        components.get('seed:item_id', 0) / max(n_seed, 1) +
        components.get('ordering:item_id', 0) / max(n_order, 1) +
        components.get('residual', 0) / max(n_model * n_temp * n_prompt * n_seed * n_order, 1)
    )
    g_item = sigma2_item / (sigma2_item + sigma2_delta) if (sigma2_item + sigma2_delta) > 0 else 0
    
    return pct, g_item

# Full 4-model baseline
full_pct, full_g = compute_gstudy(df)
print(f"Full 4-model: item_id={full_pct['item_id']:.2f}%, model*item={full_pct['model:item_id']:.2f}%, G_item={full_g:.4f}")

# Leave-one-out
loo_results = {}
for drop_model in models:
    subset = df[df['model'] != drop_model]
    remaining = sorted(subset['model'].unique())
    pct, g = compute_gstudy(subset)
    loo_results[drop_model] = {
        'remaining_models': remaining,
        'n_records': int(len(subset)),
        'item_id_pct': round(pct['item_id'], 2),
        'model_item_pct': round(pct.get('model:item_id', 0), 2),
        'model_pct': round(pct.get('model', 0), 2),
        'residual_pct': round(pct['residual'], 2),
        'G_item': round(g, 4),
    }
    print(f"Drop {drop_model}: item_id={pct['item_id']:.2f}%, model*item={pct.get('model:item_id',0):.2f}%, G_item={g:.4f}")

# Summary table
print()
print("=== Leave-One-Model-Out Summary ===")
print(f"{'Dropped':<35} {'item_id%':>8} {'m*i%':>8} {'G_item':>8}")
print("-" * 65)
print(f"{'(none - full 4-model)':<35} {full_pct['item_id']:>8.2f} {full_pct['model:item_id']:>8.2f} {full_g:>8.4f}")
for model, r in loo_results.items():
    print(f"{model:<35} {r['item_id_pct']:>8.2f} {r['model_item_pct']:>8.2f} {r['G_item']:>8.4f}")

item_pcts = [r['item_id_pct'] for r in loo_results.values()]
mi_pcts = [r['model_item_pct'] for r in loo_results.values()]
g_items = [r['G_item'] for r in loo_results.values()]

print(f"\nStability:")
print(f"  item_id range: [{min(item_pcts):.2f}, {max(item_pcts):.2f}] (spread={max(item_pcts)-min(item_pcts):.2f})")
print(f"  model*item range: [{min(mi_pcts):.2f}, {max(mi_pcts):.2f}] (spread={max(mi_pcts)-min(mi_pcts):.2f})")
print(f"  G_item range: [{min(g_items):.4f}, {max(g_items):.4f}] (spread={max(g_items)-min(g_items):.4f})")
print(f"  model*item >=25% in all subsets: {all(p >= 25 for p in mi_pcts)}")

# Find max/min impact
max_impact_model = max(loo_results.keys(), key=lambda m: abs(loo_results[m]['model_item_pct'] - full_pct['model:item_id']))
min_impact_model = min(loo_results.keys(), key=lambda m: abs(loo_results[m]['model_item_pct'] - full_pct['model:item_id']))
print(f"  Largest impact when dropping: {max_impact_model} (m*i delta={loo_results[max_impact_model]['model_item_pct'] - full_pct['model:item_id']:.2f}pp)")
print(f"  Smallest impact when dropping: {min_impact_model} (m*i delta={loo_results[min_impact_model]['model_item_pct'] - full_pct['model:item_id']:.2f}pp)")

# Save
output = {
    'full_4model': {
        'item_id_pct': round(full_pct['item_id'], 2),
        'model_item_pct': round(full_pct['model:item_id'], 2),
        'G_item': round(full_g, 4),
        'all_pct': {k: round(v, 2) for k, v in full_pct.items()},
    },
    'leave_one_out': loo_results,
    'stability': {
        'item_id_range': [min(item_pcts), max(item_pcts)],
        'model_item_range': [min(mi_pcts), max(mi_pcts)],
        'G_item_range': [min(g_items), max(g_items)],
        'model_item_all_above_25': all(p >= 25 for p in mi_pcts),
    }
}
with open('results/analysis/leave_one_model_out.json', 'w') as f:
    json.dump(output, f, indent=2)
print("\nSaved to results/analysis/leave_one_model_out.json")
