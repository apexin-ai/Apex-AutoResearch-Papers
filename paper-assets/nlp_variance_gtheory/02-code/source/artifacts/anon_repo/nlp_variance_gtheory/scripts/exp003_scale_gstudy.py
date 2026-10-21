"""
Henderson Method I G-study for exp003 scale validation (Qwen2.5-3B and 7B).

5-facet fully-crossed balanced design:
  T (temperature: 2) x Q (prompt_template: 6) x S (seed: 6)
  x O (ordering: 4) x I (item_id: 200)

Model: main effects + all 2-way interactions + residual (3-way+ absorbed).
"""

import json
import numpy as np
import pandas as pd
from itertools import combinations
from math import prod

FACETS = ['temperature', 'prompt_template', 'seed', 'ordering', 'item_id']

DATA_FILES = {
    'qwen2.5_3b': './results/exp003_scale_3b_mmlu.jsonl',
    'qwen2.5_7b': './results/exp003_scale_7b_mmlu.jsonl',
}
OUTPUT_PATH = './results/exp003_scale_gstudy.json'


def load_data(path):
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


def verify_balance(df, facets):
    n = {f: df[f].nunique() for f in facets}
    expected_N = prod(n.values())
    actual_N = len(df)
    print(f"Facet levels: {n}")
    print(f"Expected N = {'×'.join(str(v) for v in n.values())} = {expected_N}")
    print(f"Actual N  = {actual_N}")
    assert actual_N == expected_N, f"Unbalanced: {actual_N} != {expected_N}"
    print("Design is fully balanced ✓")
    return n


def compute_henderson_i(df, facets, metric='correct'):
    n = {f: df[f].nunique() for f in facets}
    N = len(df)
    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    SS_total = ((y - grand_mean) ** 2).sum()

    print(f"\n{'='*65}")
    print(f"Henderson I G-study: metric={metric}")
    print(f"Grand mean: {grand_mean:.6f}, SS_total: {SS_total:.6f}, N: {N}")
    print(f"{'='*65}")

    effects = {}

    # Main effects
    for f in facets:
        means = df.groupby(f)[metric].mean()
        n_per = N // n[f]
        ss = n_per * ((means.values - grand_mean) ** 2).sum()
        df_eff = n[f] - 1
        effects[f] = {'ss': ss, 'df': df_eff, 'ms': ss / df_eff, 'subscripts': {f}}

    # 2-way interactions
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
        effects[f'{f1}:{f2}'] = {'ss': ss, 'df': df_eff, 'ms': ss / df_eff, 'subscripts': {f1, f2}}

    # Residual
    ss_explained = sum(e['ss'] for e in effects.values())
    ss_resid = SS_total - ss_explained
    df_resid = N - 1 - sum(e['df'] for e in effects.values())
    effects['residual'] = {'ss': ss_resid, 'df': df_resid, 'ms': ss_resid / df_resid}

    # ANOVA table
    print(f"\n{'Effect':<30} {'SS':>14} {'df':>8} {'MS':>14}")
    print("-" * 68)
    for comp in list(facets) + [f'{a}:{b}' for a, b in combinations(facets, 2)] + ['residual']:
        e = effects[comp]
        print(f"  {comp:<28} {e['ss']:>14.4f} {e['df']:>8d} {e['ms']:>14.10f}")

    # Henderson I variance components via EMS
    MS_e = effects['residual']['ms']
    var_comps = {}
    var_comps['residual'] = MS_e

    # 2-way interactions
    for f1, f2 in combinations(facets, 2):
        key = f'{f1}:{f2}'
        coeff = prod(n[f] for f in facets if f not in {f1, f2})
        sigma2 = (effects[key]['ms'] - MS_e) / coeff
        var_comps[key] = sigma2

    # Main effects
    for f_main in facets:
        coeff_main = prod(n[f] for f in facets if f != f_main)
        correction = 0
        for f_other in facets:
            if f_other == f_main:
                continue
            key = f'{f_main}:{f_other}' if f'{f_main}:{f_other}' in var_comps else f'{f_other}:{f_main}'
            coeff_int = prod(n[f] for f in facets if f not in {f_main, f_other})
            correction += coeff_int * var_comps[key]
        sigma2 = (effects[f_main]['ms'] - MS_e - correction) / coeff_main
        var_comps[f_main] = sigma2

    # Raw estimates
    print("\nRaw variance components:")
    total_raw = sum(var_comps.values())
    for comp in list(facets) + [f'{a}:{b}' for a, b in combinations(facets, 2)] + ['residual']:
        v = var_comps[comp]
        pct = v / total_raw * 100 if total_raw > 0 else 0
        flag = " ← NEGATIVE" if v < 0 else ""
        print(f"  {comp:<30}: σ² = {v:12.8f}  ({pct:7.3f}%){flag}")

    # Clamp negatives to 0
    var_comps_adj = {k: max(v, 0.0) for k, v in var_comps.items()}
    total_var = sum(var_comps_adj.values())
    pct = {k: v / total_var * 100 for k, v in var_comps_adj.items()}

    print(f"\nAdjusted variance components (negatives → 0):")
    sorted_comps = sorted(pct.items(), key=lambda x: -x[1])
    for comp, p in sorted_comps:
        print(f"  {comp:<30}: σ² = {var_comps_adj[comp]:12.8f}  ({p:7.3f}%)")
    print(f"\n  Total σ² = {total_var:.8f}")

    return {
        'grand_mean': round(float(grand_mean), 6),
        'SS_total': round(float(SS_total), 6),
        'N': N,
        'facet_levels': n,
        'anova_table': {
            comp: {'SS': round(float(e['ss']), 6), 'df': int(e['df']), 'MS': round(float(e['ms']), 10)}
            for comp, e in effects.items()
        },
        'variance_components_raw': {k: round(float(v), 10) for k, v in var_comps.items()},
        'variance_components_adj': {k: round(float(v), 10) for k, v in var_comps_adj.items()},
        'variance_pct': {k: round(float(v), 4) for k, v in sorted_comps},
        'total_variance': round(float(total_var), 10),
    }


def compute_g_coefficient(result, facets):
    vc = result['variance_components_adj']
    n = result['facet_levels']
    non_item_facets = [f for f in facets if f != 'item_id']

    tau = vc.get('item_id', 0)

    delta = 0.0
    delta_breakdown = {}
    for comp, est in vc.items():
        if comp == 'item_id':
            continue
        if comp == 'residual':
            divisor = prod(n[f] for f in non_item_facets)
            contrib = est / divisor
            delta_breakdown['residual'] = {'estimate': est, 'divisor': divisor, 'contribution': round(contrib, 10)}
            delta += contrib
        else:
            parts = comp.split(':')
            if 'item_id' not in parts:
                continue
            other = [p for p in parts if p != 'item_id']
            divisor = prod(n[f] for f in other) if other else 1
            contrib = est / divisor
            delta_breakdown[comp] = {'estimate': est, 'divisor': divisor, 'contribution': round(contrib, 10)}
            delta += contrib

    G = tau / (tau + delta) if (tau + delta) > 0 else 0

    print(f"\nG coefficient (item as object of measurement):")
    print(f"  τ (σ²_item) = {tau:.8f}")
    print(f"  δ breakdown:")
    for comp, info in sorted(delta_breakdown.items(), key=lambda x: -x[1]['contribution']):
        pct_d = info['contribution'] / delta * 100 if delta > 0 else 0
        print(f"    {comp:<30}: {info['estimate']:.8f} / {info['divisor']:>5d} = {info['contribution']:.10f} ({pct_d:.1f}% of δ)")
    print(f"  σ²_δ = {delta:.8f}")
    print(f"  G_item = τ / (τ + δ) = {G:.6f}")

    return {
        'G_item': round(float(G), 6),
        'tau': round(float(tau), 10),
        'sigma_delta': round(float(delta), 10),
        'delta_breakdown': delta_breakdown,
    }


def compute_d_study(result, facets):
    vc = result['variance_components_adj']
    n = result['facet_levels']
    non_item_facets = [f for f in facets if f != 'item_id']

    tau_per_item = vc.get('item_id', 0)

    delta_per_item = 0.0
    for comp, est in vc.items():
        if comp == 'item_id':
            continue
        if comp == 'residual':
            divisor = prod(n[f] for f in non_item_facets)
            delta_per_item += est / divisor
        else:
            parts = comp.split(':')
            if 'item_id' not in parts:
                continue
            other = [p for p in parts if p != 'item_id']
            divisor = prod(n[f] for f in other) if other else 1
            delta_per_item += est / divisor

    actual_ni = n['item_id']
    d_study = {}
    print(f"\nD-study (n_items → G):")
    for ni in [25, 50, 75, 100, 150, 200, 300, 500]:
        scaling = actual_ni / ni
        G_ni = tau_per_item / (tau_per_item + delta_per_item * scaling) if (tau_per_item + delta_per_item * scaling) > 0 else 0
        d_study[ni] = round(float(G_ni), 6)
        print(f"  n_items={ni:4d}: G = {G_ni:.6f}")

    return d_study


def main():
    results = {}

    for model_key, path in DATA_FILES.items():
        print(f"\n{'█'*65}")
        print(f"█  {model_key.upper()}")
        print(f"{'█'*65}")

        df = load_data(path)
        print(f"Loaded {len(df)} records from {path}")

        n = verify_balance(df, FACETS)

        result = compute_henderson_i(df, FACETS, metric='correct')
        g_result = compute_g_coefficient(result, FACETS)
        d_study = compute_d_study(result, FACETS)

        # Item-related variance = item_id + all ×item interactions
        item_related = result['variance_pct'].get('item_id', 0)
        for comp, pct in result['variance_pct'].items():
            if 'item_id' in comp and comp != 'item_id':
                item_related += pct

        results[model_key] = {
            'n_records': result['N'],
            'grand_mean': result['grand_mean'],
            'total_variance': result['total_variance'],
            'components': {
                k: {'estimate': result['variance_components_adj'][k], 'pct': result['variance_pct'][k]}
                for k, _ in sorted(result['variance_pct'].items(), key=lambda x: -x[1])
            },
            'G_item': g_result['G_item'],
            'sigma_tau': g_result['tau'],
            'sigma_delta': g_result['sigma_delta'],
            'delta_breakdown': g_result['delta_breakdown'],
            'd_study': d_study,
            'item_related_pct': round(item_related, 4),
            'facet_ranking': [k for k, _ in sorted(result['variance_pct'].items(), key=lambda x: -x[1])],
            'variance_components_raw': result['variance_components_raw'],
        }

    # Comparison
    r3b = results['qwen2.5_3b']
    r7b = results['qwen2.5_7b']

    ranking_3b = r3b['facet_ranking']
    ranking_7b = r7b['facet_ranking']

    print(f"\n{'='*80}")
    print("COMPARISON TABLE")
    print(f"{'='*80}")
    print(f"{'Component':<30} {'3B %':>10} {'7B %':>10} {'exp001 ref':>12}")
    print("-" * 64)

    ref_item = 68.45
    for comp in ranking_3b:
        v3 = r3b['components'][comp]['pct']
        v7 = r7b['components'].get(comp, {}).get('pct', 0)
        print(f"  {comp:<28} {v3:>10.2f} {v7:>10.2f}")

    print("-" * 64)
    print(f"  {'item_related_total':<28} {r3b['item_related_pct']:>10.2f} {r7b['item_related_pct']:>10.2f} {ref_item:>12.2f}")
    print(f"  {'G_item':<28} {r3b['G_item']:>10.4f} {r7b['G_item']:>10.4f} {'0.937':>12}")
    print(f"  {'grand_mean':<28} {r3b['grand_mean']:>10.4f} {r7b['grand_mean']:>10.4f}")

    # Pct sum check
    for mk in ['qwen2.5_3b', 'qwen2.5_7b']:
        pct_sum = sum(c['pct'] for c in results[mk]['components'].values())
        print(f"\n  {mk} pct sum = {pct_sum:.2f}%")
        assert abs(pct_sum - 100.0) < 0.2, f"Pct sum check failed: {pct_sum}"

    # D-study monotonicity check
    for mk in ['qwen2.5_3b', 'qwen2.5_7b']:
        vals = list(results[mk]['d_study'].values())
        assert all(vals[i] <= vals[i+1] for i in range(len(vals)-1)), f"D-study not monotonic for {mk}"
        print(f"  {mk} D-study monotonic ✓")

    # G_item range check
    for mk in ['qwen2.5_3b', 'qwen2.5_7b']:
        g = results[mk]['G_item']
        assert 0.7 <= g <= 1.0, f"G_item out of range for {mk}: {g}"
        print(f"  {mk} G_item={g:.4f} in [0.7, 1.0] ✓")

    comparison = {
        'item_related_3b': r3b['item_related_pct'],
        'item_related_7b': r7b['item_related_pct'],
        'item_related_8model_ref': ref_item,
        'facet_ranking_3b': ranking_3b,
        'facet_ranking_7b': ranking_7b,
        'facet_ranking_consistent': ranking_3b == ranking_7b,
        'G_item_3b': r3b['G_item'],
        'G_item_7b': r7b['G_item'],
        'G_item_ref': 0.937,
        'conclusion': (
            f"3B item_related={r3b['item_related_pct']:.1f}%, 7B item_related={r7b['item_related_pct']:.1f}% "
            f"(ref single-model ~68.5%). "
            f"G_item: 3B={r3b['G_item']:.3f}, 7B={r7b['G_item']:.3f} (ref ~0.937). "
            f"Facet ranking consistent: {ranking_3b == ranking_7b}."
        ),
    }

    output = {
        'qwen2.5_3b': results['qwen2.5_3b'],
        'qwen2.5_7b': results['qwen2.5_7b'],
        'comparison': comparison,
    }

    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {OUTPUT_PATH}")
    print("DONE")


if __name__ == '__main__':
    main()
