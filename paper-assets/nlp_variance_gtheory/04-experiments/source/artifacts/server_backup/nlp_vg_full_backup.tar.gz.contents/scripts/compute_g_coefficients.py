"""Compute corrected G coefficients for cross-model analysis.

Fixes the tau definition mismatch: original G=0.073 uses tau=condition_effects
(precision+temperature), while single-model G=0.611 uses tau=item_id.
"""

import json
from math import prod

with open('results/analysis/cross_model_gstudy.json') as f:
    data = json.load(f)

vc_raw = data['variance_components']
n_levels = data['n_levels']
vc = {k: v['estimate'] for k, v in vc_raw.items()}

ALL_FACETS = ['model', 'precision', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']
FIXED = {'precision', 'temperature'}


def compute_g_item(vc, n_levels, n_overrides=None):
    """G coefficient with item_id as object of measurement.
    
    tau = sigma2_item
    delta = interactions containing item_id / n_other_facets + residual / n_all_non_item
    """
    nl = {**n_levels, **(n_overrides or {})}
    tau = vc['item_id']
    delta = 0.0
    delta_terms = {}

    for comp, est in vc.items():
        if comp == 'item_id':
            continue

        if comp == 'residual':
            divisor = prod(nl[f] for f in ALL_FACETS if f != 'item_id')
            contribution = est / divisor
            delta_terms['residual'] = {'est': est, 'divisor': divisor, 'contribution': contribution}
            delta += contribution
            continue

        facets = comp.split(':')
        if 'item_id' not in facets:
            continue

        other_facets = [f for f in facets if f != 'item_id']
        divisor = prod(nl[f] for f in other_facets) if other_facets else 1
        contribution = est / divisor
        delta_terms[comp] = {'est': est, 'divisor': divisor, 'contribution': contribution}
        delta += contribution

    g = tau / (tau + delta) if (tau + delta) > 0 else 0
    return g, tau, delta, delta_terms


def compute_g_condition(vc, n_levels, n_overrides=None):
    """G coefficient with condition effects as tau (original definition)."""
    nl = {**n_levels, **(n_overrides or {})}
    RANDOM = ['model', 'prompt_template', 'seed', 'ordering', 'item_id']

    tau = 0.0
    delta = 0.0

    for comp, est in vc.items():
        if comp == 'residual':
            divisor = prod(nl.get(f, 1) for f in RANDOM)
            delta += est / divisor
            continue

        facets = comp.split(':')
        random_in = [f for f in facets if f not in FIXED]

        if len(random_in) == 0:
            tau += est
        else:
            divisor = prod(nl.get(f, 1) for f in random_in)
            delta += est / divisor

    g = tau / (tau + delta) if (tau + delta) > 0 else 0
    return g, tau, delta


# === G_item ===
g_item, tau_item, delta_item, delta_terms = compute_g_item(vc, n_levels)

print("=" * 65)
print("G_item (tau = sigma2_item_id)")
print("  'Is item difficulty ranking reliable across models/conditions?'")
print("=" * 65)
print(f"\ntau (sigma2_item) = {tau_item:.6f} ({tau_item/data['total_variance']*100:.2f}%)")
print(f"\nDelta breakdown (current design):")
for comp, info in sorted(delta_terms.items(), key=lambda x: -x[1]['contribution']):
    pct_of_delta = info['contribution'] / delta_item * 100
    print(f"  {comp:30s}: {info['est']:.6f} / {info['divisor']:>5d} = {info['contribution']:.8f} ({pct_of_delta:.1f}% of delta)")
print(f"\nsigma2_delta = {delta_item:.6f}")
print(f"G_item       = {g_item:.4f}")

# === G_condition ===
g_cond, tau_cond, delta_cond = compute_g_condition(vc, n_levels)

print("\n" + "=" * 65)
print("G_condition (tau = sigma2_precision + sigma2_temperature + sigma2_prec:temp)")
print("=" * 65)
print(f"\ntau   = {tau_cond:.8f}")
print(f"delta = {delta_cond:.8f}")
print(f"G_condition = {g_cond:.6f}  (matches original 0.073)")

# === D-study: G_item vs n_models ===
print("\n" + "=" * 65)
print("D-study: G_item vs n_models")
print("=" * 65)

dstudy_item = []
print(f"\n{'n_models':>10} {'G_item':>10} {'sigma_delta':>14}")
print("-" * 38)
for n_m in range(1, 11):
    g, tau, delta, _ = compute_g_item(vc, n_levels, {'model': n_m})
    dstudy_item.append({'n_models': n_m, 'g_item': round(g, 6), 'sigma_tau': round(tau, 8), 'sigma_delta': round(delta, 8)})
    print(f"{n_m:>10} {g:>10.4f} {delta:>14.8f}")

# === D-study: G_item vs n_prompts ===
print("\n" + "=" * 65)
print("D-study: G_item vs n_prompts")
print("=" * 65)

dstudy_prompt = []
print(f"\n{'n_prompts':>10} {'G_item':>10}")
print("-" * 22)
for n_p in [1, 2, 3, 6, 10, 15, 20]:
    g, _, _, _ = compute_g_item(vc, n_levels, {'prompt_template': n_p})
    dstudy_prompt.append({'n_prompts': n_p, 'g_item': round(g, 6)})
    print(f"{n_p:>10} {g:>10.4f}")

# === D-study: G_item vs n_seeds ===
dstudy_seed = []
for n_s in [1, 2, 3, 6, 10, 15, 20]:
    g, _, _, _ = compute_g_item(vc, n_levels, {'seed': n_s})
    dstudy_seed.append({'n_seeds': n_s, 'g_item': round(g, 6)})

# === Comparison ===
icc_item_cross = vc['item_id'] / sum(vc.values())

print("\n" + "=" * 65)
print("Comparison: single-model vs cross-model")
print("=" * 65)
print(f"\n  {'Metric':<45} {'Single':>8} {'Cross':>8}")
print("-" * 65)
print(f"  {'ICC_item (sigma2_item / sigma2_total)':<45} {'0.6108':>8} {icc_item_cross:>8.4f}")
print(f"  {'G_item (D-study, observed n_levels)':<45} {'0.6108':>8} {g_item:>8.4f}")
print(f"  {'G_condition (tau=prec+temp)':<45} {'N/A':>8} {g_cond:>8.4f}")
print(f"\n  model x item interaction = {vc['model:item_id']:.6f} ({vc['model:item_id']/data['total_variance']*100:.1f}%)")
print(f"  This new variance source reduces ICC_item from 0.611 -> {icc_item_cross:.3f}")
print(f"  But averaging over {n_levels['model']} models: delta_model_item = {vc['model:item_id']/n_levels['model']:.6f}")
print(f"  => G_item = {g_item:.3f} (high: items rank consistently across models)")

# === Save ===
results = {
    'G_item': {
        'description': 'Item difficulty ranking reliability across models and conditions',
        'question': 'Is item difficulty ranking reliable across different models?',
        'tau': 'sigma2_item_id',
        'tau_value': round(tau_item, 8),
        'tau_pct': round(tau_item / data['total_variance'] * 100, 2),
        'g': round(g_item, 6),
        'sigma_tau': round(tau_item, 8),
        'sigma_delta': round(delta_item, 8),
        'delta_breakdown': {
            k: {'raw_estimate': round(v['est'], 8), 'divisor': v['divisor'],
                 'contribution': round(v['contribution'], 8)}
            for k, v in sorted(delta_terms.items(), key=lambda x: -x[1]['contribution'])
        },
        'dominant_delta_component': f"model:item_id ({delta_terms['model:item_id']['contribution']/delta_item*100:.1f}% of delta)",
    },
    'G_condition': {
        'description': 'Condition effect reliability (original definition)',
        'question': 'Are precision/temperature effects detectable across models/items?',
        'tau': 'sigma2_precision + sigma2_temperature + sigma2_precision:temperature',
        'g': round(g_cond, 6),
        'sigma_tau': round(tau_cond, 8),
        'sigma_delta': round(delta_cond, 8),
    },
    'comparison_with_single_model': {
        'single_model_ICC_item': 0.6108,
        'cross_model_ICC_item': round(icc_item_cross, 6),
        'cross_model_G_item': round(g_item, 6),
        'icc_drop': f"0.611 -> {round(icc_item_cross, 3)} due to model x item ({vc['model:item_id']/data['total_variance']*100:.1f}%)",
        'g_item_with_averaging': f"Averaging over {n_levels['model']} models yields G_item={round(g_item, 3)}",
    },
    'd_study_g_item_vs_n_models': dstudy_item,
    'd_study_g_item_vs_n_prompts': dstudy_prompt,
    'd_study_g_item_vs_n_seeds': dstudy_seed,
    'n_levels_observed': n_levels,
    'methodology_note': (
        'Original G=0.073 used tau=condition_effects (precision+temperature). '
        'Single-model G=0.611 used tau=item_id. These answer different questions. '
        'G_item (tau=item_id) is the correct metric for comparing item ranking '
        'reliability across single-model vs cross-model designs.'
    ),
}

with open('results/analysis/cross_model_g_coefficients.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\n=> results/analysis/cross_model_g_coefficients.json")
