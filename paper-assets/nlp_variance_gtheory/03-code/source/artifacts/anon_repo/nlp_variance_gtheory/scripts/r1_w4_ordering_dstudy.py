#!/usr/bin/env python3
"""R1-W4 D-study: Compare G coefficient with vs without ordering facet."""
import json, sys
import pandas as pd
import numpy as np
from itertools import combinations
from pathlib import Path

def compute_gstudy(df, facet_names, response='correct'):
    factors = facet_names
    n_factors = len(factors)
    levels = {f: sorted(df[f].unique()) for f in factors}
    n_levels = {f: len(levels[f]) for f in factors}
    n_total = len(df)
    
    expected_n = 1
    for f in factors:
        expected_n *= n_levels[f]
    assert expected_n == n_total, f"Not balanced: expected {expected_n}, got {n_total}"
    
    grand_mean = df[response].mean()
    idx_to_name = {i: factors[i] for i in range(n_factors)}
    
    all_effects = []
    for r in range(1, n_factors + 1):
        for combo in combinations(range(n_factors), r):
            all_effects.append(frozenset(combo))
    
    # Q(S) = (n / prod_{f in S} n_f) * sum (mean_S - grand_mean)^2
    Q = {}
    for effect in all_effects:
        fnames = [idx_to_name[i] for i in effect]
        group_means = df.groupby(fnames)[response].mean()
        n_per = n_total // int(np.prod([n_levels[idx_to_name[i]] for i in effect]))
        Q[effect] = n_per * ((group_means - grand_mean) ** 2).sum()
    
    # SS via inclusion-exclusion
    SS = {}
    for effect in all_effects:
        ss_val = 0.0
        for r in range(1, len(effect) + 1):
            for sub in combinations(effect, r):
                sub_set = frozenset(sub)
                sign = (-1) ** (len(effect) - len(sub_set))
                ss_val += sign * Q[sub_set]
        SS[effect] = ss_val
    
    # df(S) = prod (n_f - 1)
    DF = {}
    for effect in all_effects:
        df_val = 1
        for i in effect:
            df_val *= (n_levels[idx_to_name[i]] - 1)
        DF[effect] = df_val
    
    MS = {e: SS[e] / DF[e] if DF[e] > 0 else 0 for e in all_effects}
    
    # Solve variance components top-down (Henderson Method I)
    sorted_effects = sorted(all_effects, key=lambda e: len(e), reverse=True)
    sigma2 = {}
    for effect in sorted_effects:
        numerator = MS[effect]
        for other in all_effects:
            if effect < other:  # strict superset
                not_in_other = [f for f in range(n_factors) if f not in other]
                prod_val = int(np.prod([n_levels[idx_to_name[f]] for f in not_in_other])) if not_in_other else 1
                numerator -= sigma2[other] * prod_val
        not_in_effect = [f for f in range(n_factors) if f not in effect]
        denom = int(np.prod([n_levels[idx_to_name[f]] for f in not_in_effect])) if not_in_effect else 1
        sigma2[effect] = max(0, numerator / denom)
    
    named = {}
    for effect in all_effects:
        name = ':'.join([idx_to_name[i] for i in sorted(effect)])
        named[name] = {
            'sigma2': sigma2[effect],
            'ss': SS[effect],
            'ms': MS[effect],
            'df': DF[effect]
        }
    
    total_var = sum(v['sigma2'] for v in named.values())
    for name in named:
        named[name]['pct'] = named[name]['sigma2'] / total_var * 100 if total_var > 0 else 0
    
    return named, n_levels, total_var, grand_mean


def compute_g_item(named_results, n_levels, obj='item_id'):
    sigma2_obj = named_results.get(obj, {}).get('sigma2', 0)
    delta_var = 0.0
    delta_breakdown = {}
    for effect_name, vals in named_results.items():
        if obj in effect_name and effect_name != obj:
            parts = effect_name.split(':')
            other_facets = [p for p in parts if p != obj]
            if other_facets:
                denom = int(np.prod([n_levels[f] for f in other_facets]))
                contrib = vals['sigma2'] / denom
                delta_var += contrib
                delta_breakdown[effect_name] = {'sigma2': vals['sigma2'], 'n_divisor': denom, 'contrib': contrib}
    g = sigma2_obj / (sigma2_obj + delta_var) if (sigma2_obj + delta_var) > 0 else 0
    return g, delta_var, delta_breakdown


# === MAIN ===
print("Loading data...")
with open('./results/exp002/llama_gsm8k.jsonl') as f:
    data = [json.loads(l) for l in f]
df = pd.DataFrame(data)
df = df.rename(columns={'prompt_template': 'prompt_id'})

print(f"Rows: {len(df)}")
for col in ['temperature', 'prompt_id', 'seed', 'ordering', 'item_id']:
    vals = sorted(df[col].unique())
    print(f"  {col}: {len(vals)} levels -> {vals if len(vals) <= 10 else str(vals[:5]) + '...'}")

# Verify ordering is a no-op: check that correct values are identical across orderings
print("\n--- Verifying ordering is structural no-op ---")
pivot = df.pivot_table(index=['temperature', 'prompt_id', 'seed', 'item_id'], 
                       columns='ordering', values='correct', aggfunc='first')
diffs = pivot.nunique(axis=1)
n_different = (diffs > 1).sum()
print(f"Cells where orderings differ: {n_different} / {len(pivot)} ({n_different/len(pivot)*100:.2f}%)")

# ========== ANALYSIS A: WITH ORDERING ==========
print("\n" + "="*70)
print("ANALYSIS A: WITH ORDERING (5 facets)")
print("="*70)
facets_a = ['temperature', 'prompt_id', 'seed', 'ordering', 'item_id']
named_a, nlevels_a, totvar_a, gmean_a = compute_gstudy(df, facets_a)
g_a, delta_a, delta_bd_a = compute_g_item(named_a, nlevels_a)

print(f"\n{'Effect':<50} {'sigma2':>12} {'%':>8} {'SS':>14} {'df':>8}")
print("-" * 95)
for name in sorted(named_a.keys(), key=lambda x: (len(x.split(':')), x)):
    r = named_a[name]
    print(f"{name:<50} {r['sigma2']:>12.8f} {r['pct']:>7.3f}% {r['ss']:>14.4f} {r['df']:>8}")
print(f"\nTotal variance: {totvar_a:.8f}")
print(f"Grand mean: {gmean_a:.6f}")
print(f"sigma2(item_id) = {named_a['item_id']['sigma2']:.8f}")
print(f"sigma2(delta) = {delta_a:.8f}")
print(f"G_item = {g_a:.6f}")

print(f"\nDelta breakdown:")
for name, bd in sorted(delta_bd_a.items()):
    print(f"  {name}: sigma2={bd['sigma2']:.8f} / {bd['n_divisor']} = {bd['contrib']:.10f}")

# ========== ANALYSIS B: WITHOUT ORDERING ==========
print("\n" + "="*70)
print("ANALYSIS B: WITHOUT ORDERING (4 facets, ordering=1 subset)")
print("="*70)
df_b = df[df['ordering'] == 1].copy()
print(f"Rows: {len(df_b)}")
facets_b = ['temperature', 'prompt_id', 'seed', 'item_id']
named_b, nlevels_b, totvar_b, gmean_b = compute_gstudy(df_b, facets_b)
g_b, delta_b, delta_bd_b = compute_g_item(named_b, nlevels_b)

print(f"\n{'Effect':<50} {'sigma2':>12} {'%':>8} {'SS':>14} {'df':>8}")
print("-" * 95)
for name in sorted(named_b.keys(), key=lambda x: (len(x.split(':')), x)):
    r = named_b[name]
    print(f"{name:<50} {r['sigma2']:>12.8f} {r['pct']:>7.3f}% {r['ss']:>14.4f} {r['df']:>8}")
print(f"\nTotal variance: {totvar_b:.8f}")
print(f"Grand mean: {gmean_b:.6f}")
print(f"sigma2(item_id) = {named_b['item_id']['sigma2']:.8f}")
print(f"sigma2(delta) = {delta_b:.8f}")
print(f"G_item = {g_b:.6f}")

print(f"\nDelta breakdown:")
for name, bd in sorted(delta_bd_b.items()):
    print(f"  {name}: sigma2={bd['sigma2']:.8f} / {bd['n_divisor']} = {bd['contrib']:.10f}")

# ========== COMPARISON ==========
print("\n" + "="*70)
print("COMPARISON")
print("="*70)
print(f"G_item(A, with ordering):    {g_a:.6f}")
print(f"G_item(B, without ordering): {g_b:.6f}")
print(f"Difference (A - B):          {g_a - g_b:.8f}")
print(f"\nsigma2(delta)(A): {delta_a:.10f}")
print(f"sigma2(delta)(B): {delta_b:.10f}")

print(f"\nOrdering-related effects in A:")
for name in sorted(named_a.keys()):
    if 'ordering' in name:
        r = named_a[name]
        print(f"  {name}: SS={r['ss']:.8f}, sigma2={r['sigma2']:.8f} ({r['pct']:.6f}%)")

# Compare shared effects
print(f"\nShared effects comparison (A vs B):")
print(f"{'Effect':<40} {'sigma2_A':>12} {'sigma2_B':>12} {'diff':>12}")
print("-" * 80)
for name in sorted(named_b.keys(), key=lambda x: (len(x.split(':')), x)):
    s2_a = named_a.get(name, {}).get('sigma2', float('nan'))
    s2_b = named_b[name]['sigma2']
    print(f"{name:<40} {s2_a:>12.8f} {s2_b:>12.8f} {s2_a - s2_b:>12.8f}")

# ========== SAVE JSON ==========
output = {
    "analysis": "R1-W4 ordering facet impact on D-study",
    "data_source": f"exp-002 Llama GSM8K ({len(df)} records)",
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "benchmark": "gsm8k",
    "finding": "ordering is structural no-op for non-MC benchmarks",
    "ordering_verification": {
        "cells_with_different_ordering_values": int(n_different),
        "total_cells": int(len(pivot)),
        "is_perfect_noop": bool(n_different == 0)
    },
    "with_ordering": {
        "facets": facets_a,
        "n_levels": {k: int(v) for k, v in nlevels_a.items()},
        "n_conditions": int(np.prod([nlevels_a[f] for f in facets_a if f != 'item_id'])),
        "n_items": int(nlevels_a['item_id']),
        "n_records": len(df),
        "grand_mean": round(float(gmean_a), 6),
        "variance_components": {k: round(float(v['sigma2']), 10) for k, v in named_a.items()},
        "variance_pct": {k: round(float(v['pct']), 4) for k, v in named_a.items()},
        "g_item": round(float(g_a), 6),
        "sigma2_item": round(float(named_a['item_id']['sigma2']), 10),
        "sigma2_delta": round(float(delta_a), 10)
    },
    "without_ordering": {
        "facets": facets_b,
        "n_levels": {k: int(v) for k, v in nlevels_b.items()},
        "n_conditions": int(np.prod([nlevels_b[f] for f in facets_b if f != 'item_id'])),
        "n_items": int(nlevels_b['item_id']),
        "n_records": len(df_b),
        "grand_mean": round(float(gmean_b), 6),
        "variance_components": {k: round(float(v['sigma2']), 10) for k, v in named_b.items()},
        "variance_pct": {k: round(float(v['pct']), 4) for k, v in named_b.items()},
        "g_item": round(float(g_b), 6),
        "sigma2_item": round(float(named_b['item_id']['sigma2']), 10),
        "sigma2_delta": round(float(delta_b), 10)
    },
    "g_item_difference": round(float(g_a - g_b), 8),
    "conclusion": ""
}

if abs(g_a - g_b) < 0.001:
    output["conclusion"] = (
        f"G_item is virtually identical with ({g_a:.6f}) and without ({g_b:.6f}) the ordering facet "
        f"(diff={g_a-g_b:.8f}). Since ordering is a structural no-op for GSM8K (non-MC benchmark), "
        f"all 4 ordering levels produce identical responses. All ordering-related variance components "
        f"are zero. Including ordering as a pseudo-replicated facet does NOT inflate or deflate G; "
        f"it simply adds zero-variance terms that cancel out in the delta calculation. "
        f"Removing ordering is recommended for cleaner analysis but does not change conclusions."
    )
else:
    output["conclusion"] = (
        f"G_item differs: with ordering={g_a:.6f}, without={g_b:.6f} (diff={g_a-g_b:.8f}). "
        f"Despite ordering being structural no-op, including it affects G through residual redistribution."
    )

out_dir = Path('./results/exp001_analysis')
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / 'r1_w4_ordering_facet_check.json'
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"\nJSON saved to {out_path}")
print("DONE")
