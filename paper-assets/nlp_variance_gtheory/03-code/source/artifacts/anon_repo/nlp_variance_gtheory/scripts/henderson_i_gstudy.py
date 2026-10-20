"""
Henderson Method I G-study for exp001 llama single-model data.

6-facet fully-crossed balanced design:
  P (precision)      x T (temperature)     x Q (prompt_template)
  x S (seed)         x O (ordering)        x I (item_id)

Method: ANOVA-based Expected Mean Squares (EMS) → unbiased variance components.
Model: main effects + all 2-way interactions + residual (3-way+ absorbed).
"""

import json
import sys
import glob
import numpy as np
import pandas as pd
from itertools import combinations
from math import prod

# ── Step 1: Load & merge data ──────────────────────────────────────────────

def load_and_merge():
    files = sorted(
        glob.glob('./results/exp001_llama/llama_shard_*.jsonl') +
        glob.glob('./results/exp001_llama/llama_fp32_t0_backfill.jsonl')
    )
    print(f"Input files: {files}")

    rows = []
    seen = set()
    for f in files:
        count = 0
        with open(f) as fh:
            for line in fh:
                r = json.loads(line)
                # Normalize precision names
                prec = r.get('precision', r.get('dtype', ''))
                if prec == 'bfloat16':
                    prec = 'bf16'
                elif prec == 'float16':
                    prec = 'fp16'
                elif prec == 'float32':
                    prec = 'fp32'
                r['precision'] = prec

                key = (prec,
                       str(r['temperature']),
                       str(r['prompt_template']),
                       str(r['seed']),
                       str(r['ordering']),
                       str(r['item_id']))
                if key not in seen:
                    seen.add(key)
                    rows.append(r)
                    count += 1
        print(f"  {f}: +{count} new rows")

    df = pd.DataFrame(rows)
    print(f"\nTotal unique rows: {len(df)}")
    return df


def verify_balance(df, facets):
    """Verify fully-crossed balanced design."""
    n = {f: df[f].nunique() for f in facets}
    expected_N = prod(n.values())
    actual_N = len(df)
    print(f"\nFacet levels: {n}")
    print(f"Expected N = {'×'.join(str(v) for v in n.values())} = {expected_N}")
    print(f"Actual N  = {actual_N}")

    if actual_N != expected_N:
        # Find missing conditions
        from itertools import product as iproduct
        all_combos = set(iproduct(*[sorted(df[f].unique()) for f in facets]))
        actual_combos = set(df[facets].itertuples(index=False, name=None))
        missing = all_combos - actual_combos
        print(f"WARNING: {len(missing)} missing cells!")
        if len(missing) <= 10:
            for m in sorted(missing)[:10]:
                print(f"  {dict(zip(facets, m))}")
        return False
    print("Design is fully balanced ✓")
    return True


# ── Step 2: Henderson I ANOVA ──────────────────────────────────────────────

def compute_henderson_i(df, facets, metric='correct'):
    """
    Henderson Method I for balanced fully-crossed random model.

    Model: main effects + 2-way interactions + residual.
    EMS rule (Cornfield-Tukey): σ²_θ appears in E(MS_ψ) iff S_ψ ⊆ S_θ.
    Coefficient = ∏_{j ∉ S_θ} n_j.
    """
    n = {f: df[f].nunique() for f in facets}
    N = len(df)
    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    SS_total = ((y - grand_mean) ** 2).sum()

    print(f"\n{'='*65}")
    print(f"Henderson I G-study: metric={metric}")
    print(f"Grand mean: {grand_mean:.6f}, SS_total: {SS_total:.6f}, N: {N}")
    print(f"{'='*65}")

    # Compute SS and df for all effects
    effects = {}

    # Main effects
    for f in facets:
        means = df.groupby(f)[metric].mean()
        n_per = N // n[f]
        ss = n_per * ((means.values - grand_mean) ** 2).sum()
        df_eff = n[f] - 1
        effects[f] = {'ss': ss, 'df': df_eff, 'ms': ss / df_eff, 'subscripts': {f}}

    # 2-way interactions (SS_AB = SS_cells(AB) - SS_A - SS_B)
    main_means = {f: df.groupby(f)[metric].mean() for f in facets}
    for f1, f2 in combinations(facets, 2):
        cell_means = df.groupby([f1, f2])[metric].mean().reset_index()
        cell_means.columns = [f1, f2, 'cell_mean']
        cell_means['f1_mean'] = cell_means[f1].map(main_means[f1])
        cell_means['f2_mean'] = cell_means[f2].map(main_means[f2])
        n_per = N // (n[f1] * n[f2])
        deviations = cell_means['cell_mean'] - cell_means['f1_mean'] - cell_means['f2_mean'] + grand_mean
        ss = n_per * (deviations ** 2).sum()
        df_eff = (n[f1] - 1) * (n[f2] - 1)
        key = f'{f1}:{f2}'
        effects[key] = {'ss': ss, 'df': df_eff, 'ms': ss / df_eff, 'subscripts': {f1, f2}}

    # Residual
    ss_explained = sum(e['ss'] for e in effects.values())
    ss_resid = SS_total - ss_explained
    df_total = N - 1
    df_explained = sum(e['df'] for e in effects.values())
    df_resid = df_total - df_explained
    effects['residual'] = {
        'ss': ss_resid, 'df': df_resid, 'ms': ss_resid / df_resid,
        'subscripts': set(facets)  # residual contains all subscripts
    }

    # ── EMS-based variance component estimation ──
    # For balanced design: σ̂²_ε = MS_ε
    # For 2-way XY: σ̂²_{XY} = (MS_{XY} - MS_ε) / c_{XY}
    #   where c_{XY} = ∏_{j ∉ {X,Y}} n_j
    # For main X: σ̂²_X = (MS_X - MS_ε - Σ_{Y≠X} c_{XY_in_EMS_X} × σ̂²_{XY}) / c_X
    #   where c_X = ∏_{j ∉ {X}} n_j

    MS_e = effects['residual']['ms']
    var_comps = {}

    # Residual
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
        # Subtract all 2-way interaction contributions
        correction = 0
        for f_other in facets:
            if f_other == f_main:
                continue
            key = f'{f_main}:{f_other}' if f'{f_main}:{f_other}' in var_comps else f'{f_other}:{f_main}'
            coeff_int = prod(n[f] for f in facets if f not in {f_main, f_other})
            correction += coeff_int * var_comps[key]
        sigma2 = (effects[f_main]['ms'] - MS_e - correction) / coeff_main
        var_comps[f_main] = sigma2

    # Report raw estimates (including negatives)
    print("\nRaw Henderson I variance component estimates:")
    total_var_raw = sum(var_comps.values())
    for comp in list(facets) + [f'{a}:{b}' for a, b in combinations(facets, 2)] + ['residual']:
        v = var_comps[comp]
        pct = v / total_var_raw * 100 if total_var_raw > 0 else 0
        flag = " ← NEGATIVE" if v < 0 else ""
        print(f"  {comp:30s}: σ² = {v:12.8f}  ({pct:7.3f}%){flag}")

    # Handle negatives: set to 0
    var_comps_adj = {}
    for k, v in var_comps.items():
        var_comps_adj[k] = max(v, 0.0)

    total_var = sum(var_comps_adj.values())
    pct = {k: v / total_var * 100 for k, v in var_comps_adj.items()}

    print(f"\nAdjusted variance components (negatives → 0):")
    sorted_comps = sorted(pct.items(), key=lambda x: -x[1])
    for comp, p in sorted_comps:
        if p >= 0.001:
            print(f"  {comp:30s}: σ² = {var_comps_adj[comp]:12.8f}  ({p:7.3f}%)")

    print(f"\n  Total σ² = {total_var:.8f}")

    return {
        'grand_mean': round(grand_mean, 6),
        'SS_total': round(SS_total, 6),
        'N': N,
        'facet_levels': n,
        'anova_table': {
            comp: {'SS': round(e['ss'], 6), 'df': e['df'], 'MS': round(e['ms'], 10)}
            for comp, e in effects.items()
        },
        'variance_components_raw': {k: round(v, 10) for k, v in var_comps.items()},
        'variance_components_adj': {k: round(v, 10) for k, v in var_comps_adj.items()},
        'variance_pct': {k: round(v, 4) for k, v in sorted_comps},
        'total_variance': round(total_var, 10),
    }


# ── Step 3: G coefficient (item as object of measurement) ─────────────────

def compute_g_coefficient(result, facets):
    """
    G coefficient with item_id as object of measurement.

    G = σ²_item / (σ²_item + σ²_delta)
    where σ²_delta = Σ (interactions with item / n_other) + residual / n_all_non_item
    """
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
        print(f"    {comp:30s}: {info['estimate']:.8f} / {info['divisor']:>5d} = {info['contribution']:.10f} ({pct_d:.1f}% of δ)")
    print(f"  σ²_δ = {delta:.8f}")
    print(f"  G_item = τ / (τ + δ) = {G:.6f}")

    return {
        'G_item': round(G, 6),
        'tau': round(tau, 10),
        'sigma_delta': round(delta, 10),
        'delta_breakdown': delta_breakdown,
    }


def compute_d_study(result, facets, metric_name='correct'):
    """D-study: G as a function of number of items."""
    vc = result['variance_components_adj']
    n = result['facet_levels']
    non_item_facets = [f for f in facets if f != 'item_id']

    tau_per_item = vc.get('item_id', 0)  # σ²_item (universe score variance)

    # Compute delta components that scale with n_items
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

    d_study = {}
    print(f"\nD-study (n_items → G):")
    for ni in [25, 50, 75, 100, 150, 200, 300, 500]:
        # tau scales linearly, delta inversely with n_items
        # But actually: G = σ²_item / (σ²_item + Σ relative_delta / n_items)
        # More precisely: when we change n_items, each delta component gets divided by n_items/n_items_original
        # Actually the proper way:
        # G(n_i) = σ²_p / (σ²_p + σ²_δ * (n_i_obs / n_i))
        # where σ²_p = σ²_item, σ²_δ computed at observed n levels
        actual_ni = n['item_id']
        scaling = actual_ni / ni
        G_ni = tau_per_item / (tau_per_item + delta_per_item * scaling) if (tau_per_item + delta_per_item * scaling) > 0 else 0
        d_study[ni] = round(G_ni, 6)
        print(f"  n_items={ni:4d}: G = {G_ni:.6f}")

    return d_study


# ── Main ───────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    facets_6 = ['precision', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']

    # Load and merge
    df = load_and_merge()

    # Normalize types
    df['temperature'] = df['temperature'].astype(float)
    df['prompt_template'] = df['prompt_template'].astype(int)
    df['seed'] = df['seed'].astype(int)
    df['ordering'] = df['ordering'].astype(int)
    df['correct'] = df['correct'].astype(int)

    # Save merged CSV
    csv_cols = ['condition_id', 'item_id', 'subject', 'precision', 'temperature',
                'prompt_template', 'seed', 'ordering', 'correct', 'latency_ms', 'answer_logprob']
    # Add text_exact_match if present
    if 'text_exact_match' in df.columns:
        csv_cols.append('text_exact_match')
    # Only keep columns that exist
    csv_cols = [c for c in csv_cols if c in df.columns]
    df[csv_cols].to_csv('./results/analysis/llama_full_259200.csv', index=False)
    print(f"\nSaved merged CSV: results/analysis/llama_full_259200.csv ({len(df)} rows)")

    # Verify balance
    balanced = verify_balance(df, facets_6)
    if not balanced:
        print("ERROR: Design not balanced. Cannot proceed with Henderson I.")
        sys.exit(1)

    # ═══ 6-facet Henderson I (full data) ═══
    print("\n" + "█" * 65)
    print("█  6-FACET HENDERSON I G-STUDY (259,200 records)")
    print("█" * 65)
    result_6f = compute_henderson_i(df, facets_6, metric='correct')
    g_6f = compute_g_coefficient(result_6f, facets_6)
    d_study_6f = compute_d_study(result_6f, facets_6)

    # Also run for text_exact_match if available
    result_6f_tem = None
    if 'text_exact_match' in df.columns and df['text_exact_match'].notna().all():
        result_6f_tem = compute_henderson_i(df, facets_6, metric='text_exact_match')
        g_6f_tem = compute_g_coefficient(result_6f_tem, facets_6)

    # ═══ 5-facet BF16-only Henderson I ═══
    print("\n" + "█" * 65)
    print("█  5-FACET BF16-ONLY HENDERSON I G-STUDY")
    print("█" * 65)
    df_bf16 = df[df['precision'] == 'bf16'].copy()
    facets_5 = ['temperature', 'prompt_template', 'seed', 'ordering', 'item_id']
    print(f"\nBF16 subset: {len(df_bf16)} rows")
    balanced_bf16 = verify_balance(df_bf16, facets_5)

    result_5f = None
    g_5f = None
    d_study_5f = None
    if balanced_bf16:
        result_5f = compute_henderson_i(df_bf16, facets_5, metric='correct')
        g_5f = compute_g_coefficient(result_5f, facets_5)
        d_study_5f = compute_d_study(result_5f, facets_5)

    # ═══ Save unified output ═══
    unified = {
        'single_model_6facet': {
            'data_source': 'exp001_llama (4 shards + fp32_t0_backfill)',
            'records': result_6f['N'],
            'conditions': prod(result_6f['facet_levels'][f] for f in facets_6[:5]),
            'items': result_6f['facet_levels']['item_id'],
            'method': 'Henderson I (EMS-based)',
            'facets': facets_6,
            'facet_levels': result_6f['facet_levels'],
            'grand_mean': result_6f['grand_mean'],
            'metric': 'correct',
            'anova_table': result_6f['anova_table'],
            'variance_components_raw': result_6f['variance_components_raw'],
            'variance_components_adj': result_6f['variance_components_adj'],
            'variance_pct': result_6f['variance_pct'],
            'total_variance': result_6f['total_variance'],
            'G_item': g_6f['G_item'],
            'G_item_detail': g_6f,
            'd_study': d_study_6f,
        },
    }

    if result_6f_tem:
        unified['single_model_6facet_text_exact_match'] = {
            'metric': 'text_exact_match',
            'grand_mean': result_6f_tem['grand_mean'],
            'variance_pct': result_6f_tem['variance_pct'],
            'total_variance': result_6f_tem['total_variance'],
            'G_item': g_6f_tem['G_item'],
        }

    if result_5f:
        unified['single_model_bf16_5facet'] = {
            'data_source': 'exp001_llama bf16 subset',
            'records': result_5f['N'],
            'conditions': prod(result_5f['facet_levels'][f] for f in facets_5[:4]),
            'items': result_5f['facet_levels']['item_id'],
            'method': 'Henderson I (EMS-based)',
            'facets': facets_5,
            'facet_levels': result_5f['facet_levels'],
            'grand_mean': result_5f['grand_mean'],
            'metric': 'correct',
            'variance_components_raw': result_5f['variance_components_raw'],
            'variance_components_adj': result_5f['variance_components_adj'],
            'variance_pct': result_5f['variance_pct'],
            'total_variance': result_5f['total_variance'],
            'G_item': g_5f['G_item'],
            'G_item_detail': g_5f,
            'd_study': d_study_5f,
        }

    # Comparison with old numbers
    unified['comparison_with_old'] = {
        'old_data': '239,200 records (missing FP32×T=0.0)',
        'old_method': 'SS proportion (SS_component / SS_total)',
        'old_item_id_pct': 54.8479,
        'old_G_item_200': 0.9184,
        'new_data': '259,200 records (complete)',
        'new_method': 'Henderson I (EMS-based)',
        'new_item_id_pct': unified['single_model_6facet']['variance_pct'].get('item_id', 0),
        'new_G_item': unified['single_model_6facet']['G_item'],
        'note': 'Henderson I yields unbiased variance component estimates; SS proportion is biased for unbalanced/complex designs. With balanced data, differences are primarily from the 20,000 added FP32 T=0.0 records.'
    }

    out_path = './results/analysis/unified_henderson_i_numbers.json'
    with open(out_path, 'w') as f:
        json.dump(unified, f, indent=2, ensure_ascii=False)
    print(f"\n{'='*65}")
    print(f"Saved: {out_path}")
    print("DONE")
