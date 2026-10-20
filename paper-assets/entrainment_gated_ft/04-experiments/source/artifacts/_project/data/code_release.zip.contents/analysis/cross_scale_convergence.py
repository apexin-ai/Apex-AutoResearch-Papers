import json
import glob
import os
import re
import numpy as np
import pandas as pd
from itertools import permutations
from scipy.stats import spearmanr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BENCHMARKS = {
    'lambada_acc': ('lambada_openai', 'acc,none'),
    'lambada_ppl': ('lambada_openai', 'perplexity,none'),
    'hellaswag_norm': ('hellaswag', 'acc_norm,none'),
    'winogrande_acc': ('winogrande', 'acc,none'),
    'arc_easy_norm': ('arc_easy', 'acc_norm,none'),
    'arc_challenge_norm': ('arc_challenge', 'acc_norm,none'),
    'mmlu_acc': ('mmlu', 'acc,none'),
}

VARIANT_TO_ATTN = {
    'pure': 0,
    'h24-1': 1,
    'h12-1': 2,
    'h6-1': 4,
    'h3-1': 8,
}

ACC_BENCHMARKS = ['lambada_acc', 'hellaswag_norm', 'winogrande_acc',
                  'arc_easy_norm', 'arc_challenge_norm', 'mmlu_acc']


def exact_spearman_p(x, y):
    """Exact permutation test for Spearman rho (n<=8, brute-force all n! permutations)."""
    x = np.asarray(x)
    y = np.asarray(y)
    rho_obs = spearmanr(x, y)[0]
    n = len(x)
    count = sum(1 for perm in permutations(range(n))
                if abs(spearmanr(x, y[list(perm)])[0]) >= abs(rho_obs))
    import math; return rho_obs, count / math.factorial(n)


def parse_340m_filename(filepath):
    basename = os.path.basename(filepath).replace('.json', '')

    if basename == 'transformer_340M_baseline':
        return 'Transformer', 'baseline', 24

    family = None
    variant = None

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

    attn_layers = VARIANT_TO_ATTN.get(variant)
    return family, variant, attn_layers


def extract_metrics(data):
    results = data['results']
    metrics = {}
    for bm_name, (task_key, metric_key) in BENCHMARKS.items():
        if task_key in results and metric_key in results[task_key]:
            metrics[bm_name] = results[task_key][metric_key]
    return metrics


def load_340m_data():
    base = '/root/entrainment_gated_ft/lm_eval_clean/340m'
    json_files = glob.glob(os.path.join(base, '**/*.json'), recursive=True)
    json_files += glob.glob(os.path.join(base, '*.json'))
    json_files = list(set(os.path.abspath(f) for f in json_files))

    rows = []
    for jf in json_files:
        family, variant, attn_layers = parse_340m_filename(jf)
        if family is None:
            print(f"  Skipping unrecognized: {os.path.basename(jf)}")
            continue

        with open(jf) as f:
            data = json.load(f)
        metrics = extract_metrics(data)

        row = {
            'model_family': family,
            'variant': variant,
            'attn_layers': attn_layers,
            'scale': '340M',
            'file': os.path.basename(jf),
        }
        row.update(metrics)
        rows.append(row)

    return pd.DataFrame(rows)


def load_1_3b_data():
    csv_path = '/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv'
    df = pd.read_csv(csv_path)
    df['scale'] = '1.3B'
    df = df.rename(columns={'model_family': 'model_family'})
    return df


def compute_cross_arch_stats(df, scale):
    archs = ['GDN', 'RetNet', 'HGRN2']
    df_arch = df[df['model_family'].isin(archs)].copy()

    records = []
    for attn in sorted(df_arch['attn_layers'].unique()):
        sub = df_arch[df_arch['attn_layers'] == attn]
        for bm in ACC_BENCHMARKS:
            if bm not in sub.columns:
                continue
            vals = sub.set_index('model_family')[bm].reindex(archs).dropna()
            if len(vals) < 2:
                continue
            arch_vals_str = ','.join(f"{a}={v:.4f}" for a, v in vals.items())
            records.append({
                'scale': scale,
                'attn_layers': int(attn),
                'benchmark': bm,
                'arch_std': vals.std(ddof=0),
                'arch_range': vals.max() - vals.min(),
                'arch_values': arch_vals_str,
            })
    return pd.DataFrame(records)


def compute_spearman(stats_df):
    records = []
    for (scale, bm), grp in stats_df.groupby(['scale', 'benchmark']):
        if len(grp) < 4:
            continue
        x = grp['attn_layers'].values
        y = grp['arch_std'].values
        rho, pval = exact_spearman_p(x, y)
        records.append({
            'scale': scale,
            'benchmark': bm,
            'spearman_rho': rho,
            'p_value': pval,
            'p_value_method': 'exact_permutation',
            'n_points': len(grp),
        })
    return pd.DataFrame(records)


def analyze_non_monotonic(stats_all):
    print("=" * 70)
    print("=== Non-Monotonic Pattern Analysis ===")
    print("-" * 70)

    nm_records = []
    for scale in ['340M', '1.3B']:
        for bm in ACC_BENCHMARKS:
            sub = stats_all[(stats_all['scale'] == scale) & (stats_all['benchmark'] == bm)]
            sub = sub.sort_values('attn_layers')
            if sub.empty or len(sub) < 2:
                continue

            std_vals = sub.set_index('attn_layers')['arch_std']
            min_attn = std_vals.idxmin()
            min_std = std_vals[min_attn]
            pure_std = std_vals.get(0, np.nan)

            if np.isnan(pure_std) or pure_std == 0:
                reduction_pct = np.nan
            else:
                reduction_pct = (min_std - pure_std) / pure_std * 100

            rebound_str = "no rebound (monotonic)"
            rebound_pct = np.nan
            if min_attn != 8 and 8 in std_vals.index:
                std_at_8 = std_vals[8]
                if min_std > 0:
                    rebound_pct = (std_at_8 - min_std) / min_std * 100
                rebound_str = f"rebound at attn=8 (std={std_at_8:.4f}, +{rebound_pct:.1f}% from min)"

            print(f"  {scale} {bm}: min_std at attn={min_attn} "
                  f"(std={min_std:.4f}, {reduction_pct:+.1f}% from pure), {rebound_str}")

            nm_records.append({
                'scale': scale,
                'benchmark': bm,
                'min_std_attn': int(min_attn),
                'min_std': min_std,
                'pure_std': pure_std,
                'reduction_pct': reduction_pct,
                'rebound_pct': rebound_pct,
            })
    print()
    return pd.DataFrame(nm_records)


def make_figure(stats_df, spearman_df, outdir):
    bm_labels = {
        'lambada_acc': 'LAMBADA',
        'hellaswag_norm': 'HellaSwag',
        'winogrande_acc': 'WinoGrande',
        'arc_easy_norm': 'ARC-Easy',
        'arc_challenge_norm': 'ARC-Challenge',
        'mmlu_acc': 'MMLU',
    }

    fig, axes = plt.subplots(2, 3, figsize=(12, 7), sharex=True)
    axes = axes.flatten()

    for idx, bm in enumerate(ACC_BENCHMARKS):
        ax = axes[idx]
        for scale, color, ls, marker in [('1.3B', '#2c3e50', '-', 'o'),
                                          ('340M', '#e74c3c', '--', 's')]:
            sub = stats_df[(stats_df['scale'] == scale) & (stats_df['benchmark'] == bm)]
            sub = sub.sort_values('attn_layers')
            if sub.empty:
                continue
            ax.plot(sub['attn_layers'], sub['arch_std'], color=color,
                    linestyle=ls, marker=marker, markersize=5, linewidth=1.5,
                    label=scale)

            sp = spearman_df[(spearman_df['scale'] == scale) &
                             (spearman_df['benchmark'] == bm)]
            if not sp.empty:
                rho = sp.iloc[0]['spearman_rho']
                pval = sp.iloc[0]['p_value']
                sig = '*' if pval < 0.05 else ''
                y_pos = 0.95 if scale == '1.3B' else 0.82
                ax.text(0.98, y_pos, f'{scale}: ' + r'$\rho$' + f'={rho:.2f}{sig}',
                        transform=ax.transAxes, fontsize=7.5, ha='right', va='top',
                        color=color)

        ax.set_title(bm_labels.get(bm, bm), fontsize=10, fontweight='bold')
        ax.set_ylabel('Cross-arch Std', fontsize=8)
        ax.tick_params(labelsize=7)
        if idx >= 3:
            ax.set_xlabel('Attention Layers', fontsize=8)
        ax.set_xticks([0, 1, 2, 4, 8])
        if idx == 0:
            ax.legend(fontsize=7.5, loc='upper left')

    plt.suptitle('Cross-Architecture Convergence: Std across GDN, RetNet, HGRN2',
                 fontsize=11, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    for ext in ['pdf', 'png']:
        fig.savefig(os.path.join(outdir, f'cross_scale_convergence.{ext}'),
                    dpi=200, bbox_inches='tight')
    plt.close(fig)


def main():
    outdir = '/root/entrainment_gated_ft/analysis'

    print("=" * 70)
    print("Loading 1.3B data...")
    df_1b = load_1_3b_data()
    print(f"  {len(df_1b)} models loaded")

    print("Loading 340M data...")
    df_340m = load_340m_data()
    print(f"  {len(df_340m)} models loaded")
    print()

    print("=" * 70)
    print("340M data summary:")
    cols = ['model_family', 'variant', 'attn_layers'] + ACC_BENCHMARKS
    display_cols = [c for c in cols if c in df_340m.columns]
    print(df_340m[display_cols].sort_values(['model_family', 'attn_layers']).to_string(index=False))
    print()

    stats_1b = compute_cross_arch_stats(df_1b, '1.3B')
    stats_340m = compute_cross_arch_stats(df_340m, '340M')
    stats_all = pd.concat([stats_1b, stats_340m], ignore_index=True)

    print("=" * 70)
    print("Cross-Architecture Std/Range Table:")
    print(stats_all.to_string(index=False))
    print()

    csv_path = os.path.join(outdir, 'cross_scale_summary.csv')
    stats_all.to_csv(csv_path, index=False)
    print(f"Saved: {csv_path}")
    print()

    spearman_df = compute_spearman(stats_all)
    print("=" * 70)
    print("Spearman Correlation (arch_std vs attn_layers) [exact permutation p-values]:")
    print(spearman_df.to_string(index=False))
    print()

    nm_df = analyze_non_monotonic(stats_all)

    # Merge min_std_attn into stats_all CSV
    if not nm_df.empty:
        merge_cols = nm_df[['scale', 'benchmark', 'min_std_attn', 'min_std', 'reduction_pct', 'rebound_pct']]
        stats_merged = stats_all.merge(merge_cols, on=['scale', 'benchmark'], how='left')
        stats_merged.to_csv(csv_path, index=False)
        print(f"Updated CSV with non-monotonic columns: {csv_path}")
        print()

    make_figure(stats_all, spearman_df, outdir)
    print(f"Saved: {outdir}/cross_scale_convergence.pdf")
    print(f"Saved: {outdir}/cross_scale_convergence.png")
    print()

    print("=" * 70)
    print("KEY FINDINGS:")
    print("-" * 70)

    for bm in ACC_BENCHMARKS:
        for scale in ['1.3B', '340M']:
            sub = stats_all[(stats_all['scale'] == scale) & (stats_all['benchmark'] == bm)]
            if sub.empty:
                continue
            std_at_0 = sub[sub['attn_layers'] == 0]['arch_std'].values
            std_at_8 = sub[sub['attn_layers'] == 8]['arch_std'].values
            if len(std_at_0) > 0 and len(std_at_8) > 0:
                change = std_at_8[0] - std_at_0[0]
                direction = "CONVERGE" if change < 0 else "DIVERGE"
                pct = abs(change / std_at_0[0]) * 100 if std_at_0[0] > 0 else 0
                sp = spearman_df[(spearman_df['scale'] == scale) &
                                 (spearman_df['benchmark'] == bm)]
                rho_str = f"rho={sp.iloc[0]['spearman_rho']:.3f}" if not sp.empty else "N/A"
                pval_str = f"p={sp.iloc[0]['p_value']:.4f}" if not sp.empty else ""
                print(f"  {scale:4s} {bm:22s}: std {std_at_0[0]:.4f} -> {std_at_8[0]:.4f} "
                      f"({direction}, {pct:.1f}%) {rho_str} {pval_str}")

    print()
    print("Note: MMLU at 340M is near random (0.25), high noise expected.")
    print("* = p < 0.05 (exact permutation test)")


if __name__ == '__main__':
    main()
