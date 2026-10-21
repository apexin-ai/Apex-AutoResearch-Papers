"""
72B single-model Henderson I + 3-model crossed G-study.
Outputs two JSON files.
"""
import json
import numpy as np
import pandas as pd
from itertools import combinations
from math import prod

SINGLE_FACETS = ['temperature', 'prompt_template', 'seed', 'ordering', 'item_id']
CROSSED_FACETS = ['model', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']

DATA_DIR = './results'

def load_single(path):
    rows = []
    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))
    df = pd.DataFrame(rows)
    df['temperature'] = df['temperature'].astype(float)
    df['prompt_template'] = df['prompt_template'].astype(int)
    df['seed'] = df['seed'].astype(int)
    df['ordering'] = df['ordering'].astype(int)
    df['correct'] = df['correct'].astype(int)
    return df

def load_crossed():
    dfs = []
    for tag, fname in [('3b', 'exp003_scale_3b_mmlu.jsonl'),
                       ('7b', 'exp003_scale_7b_mmlu.jsonl'),
                       ('72b', 'exp003_scale_72b_mmlu.jsonl')]:
        path = f'{DATA_DIR}/{fname}'
        rows = []
        with open(path) as f:
            for line in f:
                rows.append(json.loads(line))
        df = pd.DataFrame(rows)
        df['model'] = tag
        dfs.append(df)
        print(f"  Loaded {len(df)} records from {fname}")
    df = pd.concat(dfs, ignore_index=True)
    df['temperature'] = df['temperature'].astype(float)
    df['prompt_template'] = df['prompt_template'].astype(int)
    df['seed'] = df['seed'].astype(int)
    df['ordering'] = df['ordering'].astype(int)
    df['correct'] = df['correct'].astype(int)
    return df

def henderson_i(df, facets, metric='correct'):
    n = {f: df[f].nunique() for f in facets}
    N = len(df)
    expected = prod(n.values())
    assert N == expected, f"Unbalanced: {N} != {expected}"
    print(f"  Balanced design: {' x '.join(f'{f}({n[f]})' for f in facets)} = {N}")

    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    SS_total = ((y - grand_mean) ** 2).sum()

    effects = {}
    for f in facets:
        means = df.groupby(f)[metric].mean()
        n_per = N // n[f]
        ss = n_per * ((means.values - grand_mean) ** 2).sum()
        df_eff = n[f] - 1
        effects[f] = {'ss': ss, 'df': df_eff, 'ms': ss / df_eff}

    main_means = {f: df.groupby(f)[metric].mean() for f in facets}
    for f1, f2 in combinations(facets, 2):
        cell_means = df.groupby([f1, f2])[metric].mean()
        n_per = N // (n[f1] * n[f2])
        ss_cells = 0.0
        for (v1, v2), cm in cell_means.items():
            deviation = cm - main_means[f1][v1] - main_means[f2][v2] + grand_mean
            ss_cells += deviation ** 2
        ss = n_per * ss_cells
        df_eff = (n[f1] - 1) * (n[f2] - 1)
        effects[f'{f1}:{f2}'] = {'ss': ss, 'df': df_eff, 'ms': ss / df_eff}

    ss_explained = sum(e['ss'] for e in effects.values())
    ss_resid = SS_total - ss_explained
    df_resid = N - 1 - sum(e['df'] for e in effects.values())
    effects['residual'] = {'ss': ss_resid, 'df': df_resid, 'ms': ss_resid / df_resid}

    # ANOVA table
    all_keys = list(facets) + [f'{a}:{b}' for a, b in combinations(facets, 2)] + ['residual']
    print(f"\n{'Effect':<35} {'SS':>14} {'df':>8} {'MS':>14}")
    print("-" * 73)
    for comp in all_keys:
        e = effects[comp]
        print(f"  {comp:<33} {e['ss']:>14.4f} {e['df']:>8d} {e['ms']:>14.10f}")

    # Variance components via EMS
    MS_e = effects['residual']['ms']
    var_comps = {'residual': MS_e}

    for f1, f2 in combinations(facets, 2):
        key = f'{f1}:{f2}'
        coeff = prod(n[f] for f in facets if f not in {f1, f2})
        var_comps[key] = (effects[key]['ms'] - MS_e) / coeff

    for f_main in facets:
        coeff_main = prod(n[f] for f in facets if f != f_main)
        correction = 0
        for f_other in facets:
            if f_other == f_main:
                continue
            key = f'{f_main}:{f_other}' if f'{f_main}:{f_other}' in var_comps else f'{f_other}:{f_main}'
            coeff_int = prod(n[f] for f in facets if f not in {f_main, f_other})
            correction += coeff_int * var_comps[key]
        var_comps[f_main] = (effects[f_main]['ms'] - MS_e - correction) / coeff_main

    # Print raw
    print("\nRaw variance components:")
    total_raw = sum(var_comps.values())
    for comp in all_keys:
        v = var_comps[comp]
        pct = v / total_raw * 100 if total_raw > 0 else 0
        flag = " <- NEG" if v < 0 else ""
        print(f"  {comp:<33}: {v:12.8f}  ({pct:7.3f}%){flag}")

    # Clamp negatives
    var_adj = {k: max(v, 0.0) for k, v in var_comps.items()}
    total_var = sum(var_adj.values())
    pct = {k: v / total_var * 100 for k, v in var_adj.items()}

    print(f"\nAdjusted (negatives -> 0):")
    for comp, p in sorted(pct.items(), key=lambda x: -x[1]):
        print(f"  {comp:<33}: {var_adj[comp]:12.8f}  ({p:7.3f}%)")
    print(f"  Total var = {total_var:.8f}")

    return {
        'grand_mean': float(grand_mean),
        'total_variance': float(total_var),
        'N': N,
        'facet_levels': n,
        'var_raw': {k: float(v) for k, v in var_comps.items()},
        'var_adj': {k: float(v) for k, v in var_adj.items()},
        'pct': {k: round(float(v), 4) for k, v in pct.items()},
    }

def compute_g_item(result, facets):
    vc = result['var_adj']
    n = result['facet_levels']
    non_item = [f for f in facets if f != 'item_id']

    tau = vc.get('item_id', 0)
    delta = 0.0
    breakdown = {}
    for comp, est in vc.items():
        if comp == 'item_id':
            continue
        if comp == 'residual':
            divisor = prod(n[f] for f in non_item)
            contrib = est / divisor
            delta += contrib
            breakdown['residual'] = {'raw': est, 'divisor': divisor, 'contribution': contrib}
        else:
            parts = comp.split(':')
            if 'item_id' not in parts:
                continue
            other = [p for p in parts if p != 'item_id']
            divisor = prod(n[f] for f in other) if other else 1
            contrib = est / divisor
            delta += contrib
            breakdown[comp] = {'raw': est, 'divisor': divisor, 'contribution': contrib}

    G = tau / (tau + delta) if (tau + delta) > 0 else 0
    print(f"\n  tau (item) = {tau:.8f}")
    print(f"  sigma_delta = {delta:.8f}")
    print(f"  G_item = {G:.6f}")
    for k, v in breakdown.items():
        print(f"    {k}: {v['raw']:.8f} / {v['divisor']} = {v['contribution']:.10f}")
    return {'G_item': round(float(G), 6), 'tau': float(tau), 'sigma_delta': float(delta),
            'delta_breakdown': {k: float(v['contribution']) for k, v in breakdown.items()}}

def compute_d_study(result, facets):
    vc = result['var_adj']
    n = result['facet_levels']
    non_item = [f for f in facets if f != 'item_id']
    tau = vc.get('item_id', 0)
    delta = 0.0
    for comp, est in vc.items():
        if comp == 'item_id': continue
        if comp == 'residual':
            delta += est / prod(n[f] for f in non_item)
        else:
            parts = comp.split(':')
            if 'item_id' not in parts: continue
            other = [p for p in parts if p != 'item_id']
            delta += est / (prod(n[f] for f in other) if other else 1)
    actual_ni = n['item_id']
    d = {}
    for ni in [25, 50, 100, 200, 500]:
        scaling = actual_ni / ni
        G_ni = tau / (tau + delta * scaling) if (tau + delta * scaling) > 0 else 0
        d[str(ni)] = round(float(G_ni), 6)
    print(f"\n  D-study: {d}")
    return d

# ============================================================
# PART 1: 72B single-model
# ============================================================
print("=" * 80)
print("PART 1: 72B Single-Model Henderson I G-study")
print("=" * 80)

df_72b = load_single(f'{DATA_DIR}/exp003_scale_72b_mmlu.jsonl')
print(f"Loaded {len(df_72b)} records")

r72 = henderson_i(df_72b, SINGLE_FACETS)
g72 = compute_g_item(r72, SINGLE_FACETS)
d72 = compute_d_study(r72, SINGLE_FACETS)

out1 = {
    "model": "Qwen2.5-72B-Instruct",
    "benchmark": "mmlu",
    "n_items": r72['facet_levels']['item_id'],
    "n_conditions": prod(r72['facet_levels'][f] for f in SINGLE_FACETS if f != 'item_id'),
    "total_records": r72['N'],
    "grand_mean": round(r72['grand_mean'], 6),
    "total_variance": round(r72['total_variance'], 8),
    "components_pct": {k: v for k, v in sorted(r72['pct'].items(), key=lambda x: -x[1])},
    "components_raw": {k: round(v, 10) for k, v in sorted(r72['var_adj'].items(), key=lambda x: -x[1])},
    "G_item": g72['G_item'],
    "sigma_tau": g72['tau'],
    "sigma_delta": g72['sigma_delta'],
    "delta_breakdown": g72['delta_breakdown'],
    "d_study": d72,
    "comparison": {
        "3B_item_id_pct": 75.3,
        "3B_G_item": 0.963,
        "7B_item_id_pct": 73.4,
        "7B_G_item": 0.956,
        "72B_item_id_pct": r72['pct'].get('item_id', 0),
        "72B_G_item": g72['G_item'],
    }
}

# Validate
pct_sum = sum(r72['pct'].values())
print(f"\n  Pct sum = {pct_sum:.4f}%")
assert abs(pct_sum - 100.0) < 0.2
assert 0 <= g72['G_item'] <= 1.0

with open(f'{DATA_DIR}/exp003_72b_single_gstudy.json', 'w') as f:
    json.dump(out1, f, indent=2)
print(f"Saved: {DATA_DIR}/exp003_72b_single_gstudy.json")

# ============================================================
# PART 2: 3-model crossed G-study
# ============================================================
print("\n" + "=" * 80)
print("PART 2: 3-Model Crossed Henderson I G-study")
print("=" * 80)

df_all = load_crossed()
print(f"Total: {len(df_all)} records")

rc = henderson_i(df_all, CROSSED_FACETS)
gc = compute_g_item(rc, CROSSED_FACETS)
dc = compute_d_study(rc, CROSSED_FACETS)

out2 = {
    "models": ["Qwen2.5-3B-Instruct", "Qwen2.5-7B-Instruct", "Qwen2.5-72B-Instruct"],
    "benchmark": "mmlu",
    "n_items": rc['facet_levels']['item_id'],
    "n_models": rc['facet_levels']['model'],
    "total_records": rc['N'],
    "grand_mean": round(rc['grand_mean'], 6),
    "total_variance": round(rc['total_variance'], 8),
    "components_pct": {k: v for k, v in sorted(rc['pct'].items(), key=lambda x: -x[1])},
    "components_raw": {k: round(v, 10) for k, v in sorted(rc['var_adj'].items(), key=lambda x: -x[1])},
    "G_item": gc['G_item'],
    "sigma_tau": gc['tau'],
    "sigma_delta": gc['sigma_delta'],
    "delta_breakdown": gc['delta_breakdown'],
    "d_study": dc,
    "comparison": {
        "8model_item_id_pct": 37.9,
        "8model_model_item_pct": 30.2,
        "8model_G_item": 0.896,
        "2model_3b7b_item_id_pct": 43.5,
        "2model_3b7b_model_item_pct": 31.7,
        "2model_3b7b_G_item": 0.713,
        "3model_item_id_pct": rc['pct'].get('item_id', 0),
        "3model_model_item_pct": rc['pct'].get('model:item_id', 0),
        "3model_G_item": gc['G_item'],
    }
}

pct_sum2 = sum(rc['pct'].values())
print(f"\n  Pct sum = {pct_sum2:.4f}%")
assert abs(pct_sum2 - 100.0) < 0.2
assert 0 <= gc['G_item'] <= 1.0

with open(f'{DATA_DIR}/exp003_scale_crossed_3model.json', 'w') as f:
    json.dump(out2, f, indent=2)
print(f"Saved: {DATA_DIR}/exp003_scale_crossed_3model.json")

print("\n" + "=" * 80)
print("DONE - Both analyses complete")
print("=" * 80)
