# exp003_scale_crossed_gstudy.py
# 3-model within-family (Qwen2.5-3B/7B/72B) crossed G-study
# Henderson Method I variance decomposition
# Facets: model(3) × temperature(2) × prompt(6) × seed(6) × ordering(4) × item(200)
# Input: results/exp003_scale_{3b,7b,72b}_mmlu.jsonl
# Output: results/exp003_scale_crossed_gstudy.json

import json
import sys
import numpy as np
import pandas as pd
from itertools import combinations
from math import prod

FACETS = ['model', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']

DATA_DIR = './results'
DATA_FILES = {
    '3b': f'{DATA_DIR}/exp003_scale_3b_mmlu.jsonl',
    '7b': f'{DATA_DIR}/exp003_scale_7b_mmlu.jsonl',
    '72b': f'{DATA_DIR}/exp003_scale_72b_mmlu.jsonl',
}
OUTPUT_PATH = f'{DATA_DIR}/exp003_scale_crossed_gstudy.json'


def load_data(files):
    dfs = []
    for model_key, path in files.items():
        rows = []
        with open(path) as f:
            for line in f:
                rows.append(json.loads(line))
        df = pd.DataFrame(rows)
        df['model'] = model_key
        dfs.append(df)
        print(f"  Loaded {len(df)} records from {path}")
    df = pd.concat(dfs, ignore_index=True)
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
    print(f"Expected N = {'x'.join(str(v) for v in n.values())} = {expected_N}")
    print(f"Actual N  = {actual_N}")
    assert actual_N == expected_N, f"Unbalanced: {actual_N} != {expected_N}"
    print("Design is fully balanced")
    return n


def compute_henderson_i(df, facets, metric='correct'):
    n = {f: df[f].nunique() for f in facets}
    N = len(df)
    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    SS_total = ((y - grand_mean) ** 2).sum()

    print(f"\n{'='*65}")
    print(f"Henderson I: metric={metric}")
    print(f"Grand mean: {grand_mean:.6f}, SS_total: {SS_total:.6f}, N: {N}")
    print(f"{'='*65}")

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

    all_keys = list(facets) + [f'{a}:{b}' for a, b in combinations(facets, 2)] + ['residual']
    print(f"\n{'Effect':<30} {'SS':>14} {'df':>8} {'MS':>14}")
    print("-" * 68)
    for comp in all_keys:
        e = effects[comp]
        print(f"  {comp:<28} {e['ss']:>14.4f} {e['df']:>8d} {e['ms']:>14.10f}")

    MS_e = effects['residual']['ms']
    var_comps = {}
    var_comps['residual'] = MS_e

    for f1, f2 in combinations(facets, 2):
        key = f'{f1}:{f2}'
        coeff = prod(n[f] for f in facets if f not in {f1, f2})
        sigma2 = (effects[key]['ms'] - MS_e) / coeff
        var_comps[key] = sigma2

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

    print("\nRaw variance components:")
    total_raw = sum(var_comps.values())
    for comp in all_keys:
        v = var_comps[comp]
        pct = v / total_raw * 100 if total_raw > 0 else 0
        flag = " <- NEGATIVE" if v < 0 else ""
        print(f"  {comp:<30}: {v:12.8f}  ({pct:7.3f}%){flag}")

    var_comps_adj = {k: max(v, 0.0) for k, v in var_comps.items()}
    total_var = sum(var_comps_adj.values())
    pct = {k: v / total_var * 100 for k, v in var_comps_adj.items()}

    print(f"\nAdjusted (negatives -> 0):")
    sorted_comps = sorted(pct.items(), key=lambda x: -x[1])
    for comp, p in sorted_comps:
        print(f"  {comp:<30}: {var_comps_adj[comp]:12.8f}  ({p:7.3f}%)")
    print(f"\n  Total = {total_var:.8f}")

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


def compute_g_item(result, facets):
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

    print(f"\nG_item (item as object of measurement):")
    print(f"  tau (item_id) = {tau:.8f}")
    print(f"  delta breakdown:")
    for comp, info in sorted(delta_breakdown.items(), key=lambda x: -x[1]['contribution']):
        pct_d = info['contribution'] / delta * 100 if delta > 0 else 0
        print(f"    {comp:<30}: {info['estimate']:.8f} / {info['divisor']:>5d} = {info['contribution']:.10f} ({pct_d:.1f}% of delta)")
    print(f"  delta total = {delta:.8f}")
    print(f"  G_item = {G:.6f}")

    return {
        'G_item': round(float(G), 6),
        'tau': round(float(tau), 10),
        'sigma_delta': round(float(delta), 10),
        'delta_breakdown': {k: round(float(v['contribution']), 10) for k, v in delta_breakdown.items()},
    }


def compute_d_study(result, facets):
    vc = result['variance_components_adj']
    n = result['facet_levels']
    non_item_facets = [f for f in facets if f != 'item_id']

    tau = vc.get('item_id', 0)

    delta_at_current = 0.0
    for comp, est in vc.items():
        if comp == 'item_id':
            continue
        if comp == 'residual':
            divisor = prod(n[f] for f in non_item_facets)
            delta_at_current += est / divisor
        else:
            parts = comp.split(':')
            if 'item_id' not in parts:
                continue
            other = [p for p in parts if p != 'item_id']
            divisor = prod(n[f] for f in other) if other else 1
            delta_at_current += est / divisor

    actual_ni = n['item_id']
    d_study = {}
    print(f"\nD-study (n_items -> G):")
    for ni in [25, 50, 100, 200, 500]:
        scaling = actual_ni / ni
        G_ni = tau / (tau + delta_at_current * scaling) if (tau + delta_at_current * scaling) > 0 else 0
        d_study[str(ni)] = round(float(G_ni), 6)
        print(f"  n_items={ni:4d}: G = {G_ni:.6f}")

    return d_study


def main():
    test_mode = '--test' in sys.argv

    if test_mode:
        files = {k: v for k, v in DATA_FILES.items() if k != '72b'}
        design_label = "2-model TEST (Qwen2.5-3B/7B)"
        out_path = OUTPUT_PATH.replace('.json', '_test.json')
        print(">>> TEST MODE: 2 models (3B + 7B) only <<<")
    else:
        files = DATA_FILES
        design_label = "3-model crossed (Qwen2.5-3B/7B/72B)"
        out_path = OUTPUT_PATH

    print(f"\nLoading data...")
    df = load_data(files)
    print(f"Total: {len(df)} records")

    n = verify_balance(df, FACETS)

    result = compute_henderson_i(df, FACETS, metric='correct')
    g_result = compute_g_item(result, FACETS)
    d_study = compute_d_study(result, FACETS)

    item_related = result['variance_pct'].get('item_id', 0)
    for comp, pct in result['variance_pct'].items():
        if 'item_id' in comp and comp != 'item_id':
            item_related += pct

    output = {
        'design': design_label,
        'n_records': result['N'],
        'n_levels': result['facet_levels'],
        'grand_mean': result['grand_mean'],
        'total_variance': result['total_variance'],
        'components': {
            k: {'estimate': result['variance_components_adj'][k], 'pct': result['variance_pct'][k]}
            for k, _ in sorted(result['variance_pct'].items(), key=lambda x: -x[1])
        },
        'item_related_pct': round(item_related, 4),
        'G_item': g_result['G_item'],
        'sigma_tau': g_result['tau'],
        'sigma_delta': g_result['sigma_delta'],
        'comparison_8model': {
            'ref_item_id_pct': 37.88,
            'ref_model_item_pct': 30.21,
            'ref_item_related_pct': 68.09,
            'ref_G_item': 0.896,
        },
        'd_study_curve': d_study,
    }

    pct_sum = sum(c['pct'] for c in output['components'].values())
    print(f"\nValidation:")
    print(f"  Pct sum = {pct_sum:.2f}%")
    assert abs(pct_sum - 100.0) < 0.2, f"Pct sum check failed: {pct_sum}"

    vals = list(d_study.values())
    assert all(vals[i] <= vals[i+1] for i in range(len(vals)-1)), "D-study not monotonic"
    print(f"  D-study monotonic OK")

    g = output['G_item']
    assert 0.5 <= g <= 1.0, f"G_item out of range: {g}"
    print(f"  G_item = {g:.4f} in [0.5, 1.0] OK")

    print(f"\nItem-related: {item_related:.2f}% (8-model ref: 68.09%)")
    print(f"G_item: {g:.4f} (8-model ref: 0.896)")

    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")
    print("DONE")


if __name__ == '__main__':
    main()
