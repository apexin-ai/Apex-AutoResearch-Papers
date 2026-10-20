"""
Task-specificity analysis: quantify cross-architecture convergence per benchmark.

Computes cross-architecture std (across GDN, RetNet, HGRN2) at each attention ratio
for 6 benchmarks, tests monotonic convergence via exact Spearman permutation test,
and classifies benchmarks by task taxonomy.

Input:
  - /root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv
  - /root/entrainment_gated_ft/lm_eval_clean/340m/*.json

Output:
  - /root/entrainment_gated_ft/analysis/task_specificity_results.csv
  - /root/entrainment_gated_ft/analysis/task_specificity_figure.{pdf,png}
"""

import json
import glob
import os
import math
import numpy as np
import pandas as pd
from itertools import permutations
from scipy.stats import spearmanr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BENCHMARKS = ['lambada_acc', 'hellaswag_norm', 'arc_challenge_norm',
              'winogrande_acc', 'arc_easy_norm', 'mmlu_acc']

BENCH_LABELS = {
    'lambada_acc': 'LAMBADA',
    'hellaswag_norm': 'HellaSwag',
    'arc_challenge_norm': 'ARC-C',
    'winogrande_acc': 'WinoGrande',
    'arc_easy_norm': 'ARC-E',
    'mmlu_acc': 'MMLU',
}

TAXONOMY = {
    'lambada_acc': 'Retrieval-dependent',
    'hellaswag_norm': 'Reasoning-dependent',
    'arc_challenge_norm': 'Reasoning-dependent',
    'winogrande_acc': 'Reasoning-dependent',
    'arc_easy_norm': 'Mixed',
    'mmlu_acc': 'Mixed',
}

VARIANT_ORDER = ['pure', 'h24-1', 'h12-1', 'h6-1', 'h3-1']
VARIANT_TO_ATTN = {'pure': 0, 'h24-1': 1, 'h12-1': 2, 'h6-1': 4, 'h3-1': 8}
ATTN_LEVELS = [0, 1, 2, 4, 8]

JSON_BENCHMARKS = {
    'lambada_acc': ('lambada_openai', 'acc,none'),
    'hellaswag_norm': ('hellaswag', 'acc_norm,none'),
    'winogrande_acc': ('winogrande', 'acc,none'),
    'arc_easy_norm': ('arc_easy', 'acc_norm,none'),
    'arc_challenge_norm': ('arc_challenge', 'acc_norm,none'),
    'mmlu_acc': ('mmlu', 'acc,none'),
}


def exact_spearman_p(x, y):
    """Exact two-sided permutation test for Spearman rho (n<=8)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    rho_obs = spearmanr(x, y)[0]
    n = len(x)
    count = sum(1 for perm in permutations(range(n))
                if abs(spearmanr(x, y[list(perm)])[0]) >= abs(rho_obs))
    return rho_obs, count / math.factorial(n)


def load_1_3b_data():
    csv_path = '/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv'
    df = pd.read_csv(csv_path)
    df = df[df['model_family'].isin(['GDN', 'RetNet', 'HGRN2'])]
    df = df[df['variant'].isin(VARIANT_ORDER)]
    return df


def parse_340m_filename(filepath):
    basename = os.path.basename(filepath).replace('.json', '')
    if basename == 'transformer_340M_baseline':
        return None, None, None

    family, variant = None, None
    if 'GatedDeltaNet' in basename:
        family = 'GDN'
        if 'pure-baseline' in basename:
            variant = 'pure'
        elif 'New-hybrid-24-1' in basename:
            variant = 'h24-1'
        elif 'hybrid-12-1' in basename:
            variant = 'h12-1'
        elif 'hybrid-6-1' in basename:
            variant = 'h6-1'
        elif 'hybrid-3-1' in basename:
            variant = 'h3-1'
    elif 'RetNet' in basename:
        family = 'RetNet'
        if 'pure' in basename:
            variant = 'pure'
        elif 'hybrid-24-1' in basename:
            variant = 'h24-1'
        elif 'hybrid-12-1' in basename:
            variant = 'h12-1'
        elif 'hybrid-6-1' in basename:
            variant = 'h6-1'
        elif 'hybrid-3-1' in basename:
            variant = 'h3-1'
    elif 'HGRN2' in basename:
        family = 'HGRN2'
        if 'pure' in basename:
            variant = 'pure'
        elif 'hybrid-24-1' in basename:
            variant = 'h24-1'
        elif 'hybrid-12-1' in basename:
            variant = 'h12-1'
        elif 'hybrid-6-1' in basename:
            variant = 'h6-1'
        elif 'hybrid-3-1' in basename:
            variant = 'h3-1'

    if family is None or variant is None:
        return None, None, None
    return family, variant, VARIANT_TO_ATTN.get(variant)


def load_340m_data():
    base = '/root/entrainment_gated_ft/lm_eval_clean/340m'
    json_files = glob.glob(os.path.join(base, '**/*.json'), recursive=True)
    json_files += glob.glob(os.path.join(base, '*.json'))
    json_files = list(set(os.path.abspath(f) for f in json_files))

    rows = []
    for jf in json_files:
        family, variant, attn_layers = parse_340m_filename(jf)
        if family is None:
            continue
        with open(jf) as f:
            data = json.load(f)
        results = data.get('results', {})
        metrics = {}
        for bm_name, (task_key, metric_key) in JSON_BENCHMARKS.items():
            if task_key in results and metric_key in results[task_key]:
                metrics[bm_name] = results[task_key][metric_key]
        row = {'model_family': family, 'variant': variant, 'attn_layers': attn_layers}
        row.update(metrics)
        rows.append(row)
    return pd.DataFrame(rows)


def compute_cross_arch_std(df, benchmarks, attn_levels):
    """Cross-architecture std (population) at each attention level."""
    results = {}
    for bm in benchmarks:
        stds = []
        for attn in attn_levels:
            vals = df[df['attn_layers'] == attn][bm].dropna().values
            stds.append(np.std(vals) if len(vals) >= 2 else np.nan)
        results[bm] = stds
    return results


def main():
    outdir = '/root/entrainment_gated_ft/analysis'
    os.makedirs(outdir, exist_ok=True)

    df_1b = load_1_3b_data()
    df_340m = load_340m_data()
    print(f"Loaded: 1.3B={len(df_1b)} models, 340M={len(df_340m)} models")

    stds_1b = compute_cross_arch_std(df_1b, BENCHMARKS, ATTN_LEVELS)
    stds_340m = compute_cross_arch_std(df_340m, BENCHMARKS, ATTN_LEVELS)

    # --- Spearman tests + CSV ---
    rows = []
    print(f"\n{'Benchmark':12s} {'Taxonomy':22s} {'Scale':5s}  {'rho':>6s}  {'p':>6s}  Sig")
    print("-" * 65)
    for bm in BENCHMARKS:
        for scale_label, stds in [('1.3B', stds_1b), ('340M', stds_340m)]:
            y = np.array(stds[bm])
            x = np.array(ATTN_LEVELS, dtype=float)
            valid = ~np.isnan(y)
            if valid.sum() >= 3:
                rho, p = exact_spearman_p(x[valid], y[valid])
            else:
                rho, p = np.nan, np.nan
            sig = p < 0.05 if not np.isnan(p) else False
            sig_mark = '*' if sig else ''
            print(f"{BENCH_LABELS[bm]:12s} {TAXONOMY[bm]:22s} {scale_label:5s}  "
                  f"{rho:+.3f}  {p:.4f}  {sig_mark}")

            if scale_label == '1.3B':
                row = {
                    'benchmark': BENCH_LABELS[bm],
                    'taxonomy_category': TAXONOMY[bm],
                }
                for i, v in enumerate(VARIANT_ORDER):
                    row[f'std_{v}_1.3B'] = stds_1b[bm][i]
                    row[f'std_{v}_340M'] = stds_340m[bm][i]
                row['spearman_rho_1.3B'] = rho
                row['p_value_1.3B'] = p
                row['significant_1.3B'] = sig

        # add 340M stats to the same row
        y_340m = np.array(stds_340m[bm])
        x_340m = np.array(ATTN_LEVELS, dtype=float)
        valid_340m = ~np.isnan(y_340m)
        if valid_340m.sum() >= 3:
            rho_340m, p_340m = exact_spearman_p(x_340m[valid_340m], y_340m[valid_340m])
        else:
            rho_340m, p_340m = np.nan, np.nan
        row['spearman_rho_340M'] = rho_340m
        row['p_value_340M'] = p_340m
        row['significant_340M'] = p_340m < 0.05 if not np.isnan(p_340m) else False
        rows.append(row)

    csv_df = pd.DataFrame(rows)
    csv_path = os.path.join(outdir, 'task_specificity_results.csv')
    csv_df.to_csv(csv_path, index=False)
    print(f"\nCSV saved: {csv_path}")

    # --- 6-panel figure ---
    fig, axes = plt.subplots(2, 3, figsize=(13, 7.5))
    axes = axes.flatten()

    for idx, bm in enumerate(BENCHMARKS):
        ax = axes[idx]
        r = csv_df.iloc[idx]

        # 1.3B line
        y_1b = np.array(stds_1b[bm])
        v_1b = ~np.isnan(y_1b)
        p_1b = r['p_value_1.3B']
        rho_1b = r['spearman_rho_1.3B']
        c_1b = '#d62728' if p_1b < 0.05 else '#1f77b4'
        lw_1b = 2.5 if p_1b < 0.05 else 1.5
        ax.plot(np.array(ATTN_LEVELS)[v_1b], y_1b[v_1b],
                marker='o', color=c_1b, linewidth=lw_1b, markersize=6,
                label=f'1.3B (ρ={rho_1b:+.2f}, p={p_1b:.3f})')

        # 340M line
        y_340m = np.array(stds_340m[bm])
        v_340m = ~np.isnan(y_340m)
        p_340m = r['p_value_340M']
        rho_340m = r['spearman_rho_340M']
        c_340m = '#d62728' if p_340m < 0.05 else '#aec7e8'
        ls_340m = '-' if p_340m < 0.05 else '--'
        ax.plot(np.array(ATTN_LEVELS)[v_340m], y_340m[v_340m],
                marker='s', color=c_340m, linewidth=1.2, markersize=5,
                linestyle=ls_340m,
                label=f'340M (ρ={rho_340m:+.2f}, p={p_340m:.3f})')

        cat_tag = {'Retrieval-dependent': '[R]',
                   'Reasoning-dependent': '[Z]',
                   'Mixed': '[M]'}[TAXONOMY[bm]]
        ax.set_title(f'{BENCH_LABELS[bm]} {cat_tag}', fontsize=11, fontweight='bold')
        ax.set_ylabel('Cross-arch σ', fontsize=9)
        ax.set_xlabel('Attention layers', fontsize=9)
        ax.set_xticks(ATTN_LEVELS)
        ax.set_xticklabels(['0\n(pure)', '1\n(h24)', '2\n(h12)', '4\n(h6)', '8\n(h3)'],
                           fontsize=7)
        ax.legend(fontsize=6.5, loc='best')
        ax.grid(True, alpha=0.3)

    plt.suptitle('Task-Specificity: Cross-Architecture Convergence by Benchmark',
                 fontsize=13, fontweight='bold', y=0.99)
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    for ext in ['pdf', 'png']:
        fig.savefig(os.path.join(outdir, f'task_specificity_figure.{ext}'),
                    dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"Figure saved: {outdir}/task_specificity_figure.{{pdf,png}}")

    # --- Summary ---
    print("\n=== TASK-SPECIFICITY SUMMARY ===")
    for _, r in csv_df.iterrows():
        sig_1b = 'SIG' if r['significant_1.3B'] else 'n.s.'
        sig_340m = 'SIG' if r['significant_340M'] else 'n.s.'
        print(f"  {r['benchmark']:12s} ({r['taxonomy_category']:20s}): "
              f"1.3B rho={r['spearman_rho_1.3B']:+.3f} [{sig_1b}], "
              f"340M rho={r['spearman_rho_340M']:+.3f} [{sig_340m}]")


if __name__ == '__main__':
    main()
