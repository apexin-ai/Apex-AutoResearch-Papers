#!/usr/bin/env python3
"""D127 Specification Curve Analysis for 5-method lead-lag results.

Exhaustive matrix: method × α × seed × pair.
Uses only D102 canonical results (true_3sigma_d105 threshold criterion).
FDR-corrected significance where available.
"""

import json
import os
import glob
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from collections import defaultdict, OrderedDict

RESULTS_BASE = "/root/autodl-tmp/distrib_canary_collapse/results"
OUTPUT_DIR = "/root/autodl-tmp/distrib_canary_collapse/artifacts/d127_spec_curve"

METHODS = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']
METHOD_LABELS = {
    'naive_xcorr': 'Naive XCorr',
    'diff_xcorr': 'Diff XCorr',
    'threshold_onset': 'Threshold Onset',
    'perm_granger': 'Perm Granger',
    'ty_granger': 'TY Granger',
}
CANONICAL_PAIRS = [
    ('token_entropy', 'distinct_1'), ('token_entropy', 'distinct_2'),
    ('token_entropy', 'distinct_3'), ('token_entropy', 'mauve'),
    ('ece', 'distinct_1'), ('ece', 'distinct_2'),
    ('ece', 'distinct_3'), ('ece', 'mauve'),
]

EXCLUDE_DIRS = {'a050_postd093_s42_fp32'}


def get_significance(method_result, method_name):
    if method_name in ('diff_xcorr', 'perm_granger'):
        return bool(method_result.get('significant_fdr', method_result.get('significant', False)))
    return bool(method_result.get('significant', False))


def classify_experiment(path):
    """Return (category, model, dataset) from experiment path."""
    if '/alpha_sweep/' in path:
        dirname = os.path.basename(path)
        if dirname.startswith('c4_'):
            return 'c4', 'pythia-410m', 'c4'
        return 'alpha_sweep', 'pythia-410m', 'wikitext'
    elif '/generalize/' in path:
        dirname = os.path.basename(path)
        if 'gpt2m' in dirname:
            return 'generalize', 'gpt2-medium', 'wikitext'
        elif 'qwen35_08b' in dirname:
            return 'generalize', 'qwen2.5-0.8b', 'wikitext'
        elif 'pythia410m' in dirname:
            return 'generalize', 'pythia-410m', 'wikitext'
        elif 'smollm3_3b' in dirname:
            return 'generalize', 'smollm3-3b', 'wikitext'
        return 'generalize', 'unknown', 'wikitext'
    elif '/scale_check/' in path:
        return 'scale_check', 'pythia-6.9b', 'wikitext'
    elif '/scale/' in path:
        return 'scale', 'pythia-1.4b', 'c4'
    elif '/padding_robustness/' in path:
        return 'padding_robustness', 'gpt2-small', 'wikitext'
    return 'unknown', 'unknown', 'unknown'


def load_all_results():
    json_files = sorted(glob.glob(
        os.path.join(RESULTS_BASE, '**/analysis/5method_leadlag.json'),
        recursive=True
    ))

    rows = []
    skipped = []

    for jf in json_files:
        exp_dir = os.path.dirname(os.path.dirname(jf))
        dirname = os.path.basename(exp_dir)

        if dirname in EXCLUDE_DIRS:
            skipped.append((dirname, 'excluded'))
            continue
        if '/intervention/' in jf:
            skipped.append((dirname, 'intervention'))
            continue

        with open(jf) as f:
            data = json.load(f)

        # Check for canonical threshold criterion
        if 'meta' in data:
            criterion = data['meta'].get('threshold_criterion', '')
            alpha = data['meta']['alpha']
            seed = data['meta']['seed']
        else:
            criterion = data.get('config', {}).get('threshold_criterion', '')
            alpha = data.get('alpha', -1)
            seed = data.get('seed', -1)

        if criterion != 'true_3sigma_d105':
            skipped.append((dirname, f'wrong criterion: {criterion}'))
            continue

        category, model, dataset = classify_experiment(exp_dir)

        for pair_data in data.get('pairs', []):
            canary = pair_data['canary']
            downstream = pair_data['downstream']

            if (canary, downstream) not in CANONICAL_PAIRS:
                continue

            forward = pair_data.get('forward', {})

            for method in METHODS:
                if method not in forward:
                    rows.append({
                        'method': method,
                        'alpha': alpha,
                        'seed': seed,
                        'canary': canary,
                        'downstream': downstream,
                        'pair': f"{canary} → {downstream}",
                        'significant': None,
                        'category': category,
                        'model': model,
                        'dataset': dataset,
                        'exp_dir': dirname,
                    })
                    continue

                sig = get_significance(forward[method], method)
                rows.append({
                    'method': method,
                    'alpha': alpha,
                    'seed': seed,
                    'canary': canary,
                    'downstream': downstream,
                    'pair': f"{canary} → {downstream}",
                    'significant': 1 if sig else 0,
                    'category': category,
                    'model': model,
                    'dataset': dataset,
                    'exp_dir': dirname,
                })

    return rows, skipped


def compute_statistics(rows):
    valid = [r for r in rows if r['significant'] is not None]
    n_total = len(valid)
    n_sig = sum(r['significant'] for r in valid)

    stats = {
        'n_specifications': n_total,
        'n_significant': n_sig,
        'overall_positive_rate': n_sig / n_total if n_total else 0,
        'n_experiments': len(set(r['exp_dir'] for r in valid)),
    }

    # Per-method
    stats['per_method'] = {}
    for m in METHODS:
        sub = [r for r in valid if r['method'] == m]
        n = len(sub)
        s = sum(r['significant'] for r in sub)
        stats['per_method'][m] = {
            'n': n, 'n_sig': s,
            'rate': s / n if n else 0,
        }

    # Per-alpha
    alphas = sorted(set(r['alpha'] for r in valid))
    stats['per_alpha'] = {}
    for a in alphas:
        sub = [r for r in valid if r['alpha'] == a]
        n = len(sub)
        s = sum(r['significant'] for r in sub)
        stats['per_alpha'][str(a)] = {
            'n': n, 'n_sig': s,
            'rate': s / n if n else 0,
        }

    # High alpha (>=0.50) vs low alpha (<0.50)
    high = [r for r in valid if r['alpha'] >= 0.50]
    low = [r for r in valid if r['alpha'] < 0.50]
    stats['alpha_split'] = {
        'high_ge050': {
            'n': len(high),
            'n_sig': sum(r['significant'] for r in high),
            'rate': sum(r['significant'] for r in high) / len(high) if high else 0,
        },
        'low_lt050': {
            'n': len(low),
            'n_sig': sum(r['significant'] for r in low),
            'rate': sum(r['significant'] for r in low) / len(low) if low else 0,
        },
    }

    # Per canary type
    stats['per_canary'] = {}
    for c in ['token_entropy', 'ece']:
        sub = [r for r in valid if r['canary'] == c]
        n = len(sub)
        s = sum(r['significant'] for r in sub)
        stats['per_canary'][c] = {'n': n, 'n_sig': s, 'rate': s / n if n else 0}

    # Per downstream type
    stats['per_downstream'] = {}
    for d in ['distinct_1', 'distinct_2', 'distinct_3', 'mauve']:
        sub = [r for r in valid if r['downstream'] == d]
        n = len(sub)
        s = sum(r['significant'] for r in sub)
        stats['per_downstream'][d] = {'n': n, 'n_sig': s, 'rate': s / n if n else 0}

    # Distinct vs mauve
    dist = [r for r in valid if r['downstream'].startswith('distinct')]
    mauv = [r for r in valid if r['downstream'] == 'mauve']
    stats['downstream_split'] = {
        'distinct': {
            'n': len(dist),
            'n_sig': sum(r['significant'] for r in dist),
            'rate': sum(r['significant'] for r in dist) / len(dist) if dist else 0,
        },
        'mauve': {
            'n': len(mauv),
            'n_sig': sum(r['significant'] for r in mauv),
            'rate': sum(r['significant'] for r in mauv) / len(mauv) if mauv else 0,
        },
    }

    # Per category
    stats['per_category'] = {}
    for cat in sorted(set(r['category'] for r in valid)):
        sub = [r for r in valid if r['category'] == cat]
        n = len(sub)
        s = sum(r['significant'] for r in sub)
        stats['per_category'][cat] = {'n': n, 'n_sig': s, 'rate': s / n if n else 0}

    # Per model
    stats['per_model'] = {}
    for model in sorted(set(r['model'] for r in valid)):
        sub = [r for r in valid if r['model'] == model]
        n = len(sub)
        s = sum(r['significant'] for r in sub)
        stats['per_model'][model] = {'n': n, 'n_sig': s, 'rate': s / n if n else 0}

    return stats


def plot_spec_curve(rows, stats, output_path):
    valid = [r for r in rows if r['significant'] is not None]

    # Sort: significant first, then by alpha descending, then by method
    method_order = {m: i for i, m in enumerate(METHODS)}
    valid_sorted = sorted(valid, key=lambda r: (
        -r['significant'],
        -r['alpha'],
        method_order.get(r['method'], 99),
        r['pair'],
        r['seed'],
    ))

    n = len(valid_sorted)
    x = np.arange(n)
    effects = np.array([r['significant'] for r in valid_sorted])

    # Colors for attributes
    method_colors = {
        'naive_xcorr': '#e41a1c',
        'diff_xcorr': '#377eb8',
        'threshold_onset': '#4daf4a',
        'perm_granger': '#984ea3',
        'ty_granger': '#ff7f00',
    }

    alphas_unique = sorted(set(r['alpha'] for r in valid_sorted))
    alpha_cmap = plt.cm.viridis(np.linspace(0.1, 0.9, len(alphas_unique)))
    alpha_colors = {a: alpha_cmap[i] for i, a in enumerate(alphas_unique)}

    seed_colors = {42: '#66c2a5', 43: '#fc8d62', 44: '#8da0cb'}

    canary_colors = {'token_entropy': '#a6d854', 'ece': '#e78ac3'}

    downstream_colors = {
        'distinct_1': '#1b9e77', 'distinct_2': '#d95f02',
        'distinct_3': '#7570b3', 'mauve': '#e7298a',
    }

    fig, axes = plt.subplots(
        6, 1, figsize=(16, 10),
        gridspec_kw={'height_ratios': [3, 0.5, 0.5, 0.5, 0.5, 0.5], 'hspace': 0.05},
        sharex=True
    )

    # Panel 0: Effect (sorted significance)
    ax = axes[0]
    n_sig_total = int(effects.sum())
    ax.bar(x[:n_sig_total], effects[:n_sig_total], width=1.0, color='#2c3e50', alpha=0.85, linewidth=0)
    ax.bar(x[n_sig_total:], effects[n_sig_total:], width=1.0, color='#bdc3c7', alpha=0.5, linewidth=0)
    ax.set_ylabel('Significant\n(FDR p<.05)', fontsize=9)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['No', 'Yes'], fontsize=8)
    ax.axvline(n_sig_total - 0.5, color='red', linestyle='--', alpha=0.5, linewidth=0.8)
    rate_pct = stats['overall_positive_rate'] * 100
    ax.set_title(
        f'Specification Curve: {n} specifications, {n_sig_total} significant ({rate_pct:.1f}%)',
        fontsize=12, fontweight='bold', pad=10
    )
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Helper for attribute strips
    def draw_strip(ax_idx, values, color_map, label):
        ax = axes[ax_idx]
        for i, v in enumerate(values):
            c = color_map.get(v, '#cccccc')
            ax.bar(i, 1, width=1.0, color=c, linewidth=0)
        ax.set_ylabel(label, fontsize=8, rotation=0, ha='right', va='center')
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)

    # Panel 1: Method
    draw_strip(1, [r['method'] for r in valid_sorted], method_colors, 'Method')
    # Panel 2: Alpha
    draw_strip(2, [r['alpha'] for r in valid_sorted], alpha_colors, 'α')
    # Panel 3: Seed
    draw_strip(3, [r['seed'] for r in valid_sorted], seed_colors, 'Seed')
    # Panel 4: Canary
    draw_strip(4, [r['canary'] for r in valid_sorted], canary_colors, 'Canary')
    # Panel 5: Downstream
    draw_strip(5, [r['downstream'] for r in valid_sorted], downstream_colors, 'Down-\nstream')

    axes[-1].set_xlabel('Specifications (sorted by significance)', fontsize=10)
    axes[-1].set_xlim(-0.5, n - 0.5)

    # Legends
    legend_items = []

    legend_items.append(Patch(facecolor='white', edgecolor='white', label='── Method ──'))
    for m in METHODS:
        r = stats['per_method'][m]['rate'] * 100
        legend_items.append(Patch(facecolor=method_colors[m], label=f"{METHOD_LABELS[m]} ({r:.0f}%)"))

    legend_items.append(Patch(facecolor='white', edgecolor='white', label='── Canary ──'))
    legend_items.append(Patch(facecolor=canary_colors['token_entropy'], label=f"Entropy ({stats['per_canary']['token_entropy']['rate']*100:.0f}%)"))
    legend_items.append(Patch(facecolor=canary_colors['ece'], label=f"ECE ({stats['per_canary']['ece']['rate']*100:.0f}%)"))

    legend_items.append(Patch(facecolor='white', edgecolor='white', label='── Downstream ──'))
    for d in ['distinct_1', 'distinct_2', 'distinct_3', 'mauve']:
        r = stats['per_downstream'][d]['rate'] * 100
        legend_items.append(Patch(facecolor=downstream_colors[d], label=f"{d} ({r:.0f}%)"))

    fig.legend(
        handles=legend_items, loc='center right',
        bbox_to_anchor=(1.0, 0.5), fontsize=7,
        frameon=True, fancybox=True, shadow=False,
        ncol=1, handlelength=1.2, handleheight=0.8,
    )

    plt.subplots_adjust(right=0.82)
    fig.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Saved: {output_path}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Loading results...")
    rows, skipped = load_all_results()

    valid = [r for r in rows if r['significant'] is not None]
    na = [r for r in rows if r['significant'] is None]
    print(f"Total specs: {len(rows)} ({len(valid)} valid, {len(na)} NA)")
    print(f"Skipped experiments: {len(skipped)}")
    for d, reason in skipped:
        print(f"  {d}: {reason}")

    print("\nComputing statistics...")
    stats = compute_statistics(rows)

    print(f"\n=== Specification Curve Summary ===")
    print(f"Specifications: {stats['n_specifications']}")
    print(f"Experiments: {stats['n_experiments']}")
    print(f"Significant: {stats['n_significant']}/{stats['n_specifications']} ({stats['overall_positive_rate']*100:.1f}%)")

    print(f"\nPer-method positive rate:")
    for m in METHODS:
        s = stats['per_method'][m]
        print(f"  {METHOD_LABELS[m]:18s}: {s['n_sig']:3d}/{s['n']:3d} ({s['rate']*100:.1f}%)")

    print(f"\nPer-alpha positive rate:")
    for a_str in sorted(stats['per_alpha'].keys(), key=float):
        s = stats['per_alpha'][a_str]
        print(f"  α={float(a_str):.2f}: {s['n_sig']:3d}/{s['n']:3d} ({s['rate']*100:.1f}%)")

    print(f"\nα split:")
    for k, s in stats['alpha_split'].items():
        print(f"  {k}: {s['n_sig']}/{s['n']} ({s['rate']*100:.1f}%)")

    print(f"\nCanary type:")
    for c, s in stats['per_canary'].items():
        print(f"  {c}: {s['n_sig']}/{s['n']} ({s['rate']*100:.1f}%)")

    print(f"\nDownstream type:")
    for d, s in stats['per_downstream'].items():
        print(f"  {d}: {s['n_sig']}/{s['n']} ({s['rate']*100:.1f}%)")

    print(f"\nDistinct vs Mauve:")
    for k, s in stats['downstream_split'].items():
        print(f"  {k}: {s['n_sig']}/{s['n']} ({s['rate']*100:.1f}%)")

    print(f"\nPer-category:")
    for cat, s in stats['per_category'].items():
        print(f"  {cat}: {s['n_sig']}/{s['n']} ({s['rate']*100:.1f}%)")

    print(f"\nPer-model:")
    for model, s in stats['per_model'].items():
        print(f"  {model}: {s['n_sig']}/{s['n']} ({s['rate']*100:.1f}%)")

    # Save JSON
    json_path = os.path.join(OUTPUT_DIR, 'd127_spec_curve.json')
    output = {
        'statistics': stats,
        'matrix': [
            {k: v for k, v in r.items()}
            for r in rows
        ],
        'skipped': skipped,
    }
    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved JSON: {json_path}")

    # Plot
    png_path = os.path.join(OUTPUT_DIR, 'spec_curve.png')
    print("Plotting specification curve...")
    plot_spec_curve(rows, stats, png_path)

    print("\nDone.")


if __name__ == '__main__':
    main()
