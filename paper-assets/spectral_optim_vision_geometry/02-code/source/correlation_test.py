"""FCSB δ² vs Weight Swap Δacc Spearman Correlation Test.

Purpose: Test whether FCSB δ² (Grishina variant) predicts per-layer Muon benefit
         magnitude (weight swap Δacc). Kill criterion: Spearman ρ ≥ 0.3, p < 0.05.

Input:
  - gradient_geometry_resnet50.csv: Phase 0 scan with delta_grishina per layer per epoch
  - resnet50_weight_swap.csv: Weight swap results with muon_drop_pp per layer

Output:
  - JSON results to --output path
  - Scatter plot PNG to results/correlation_scatter.png
  - Human-readable summary to stdout
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict

import numpy as np
from scipy import stats


def load_geometry_scan(path):
    """Load phase0 gradient geometry scan, return {epoch: {layer_name: delta_grishina²}}."""
    data = defaultdict(dict)
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            epoch = int(row['epoch'])
            layer = row['layer_name']
            delta_g = float(row['delta_grishina'])
            data[epoch][layer] = delta_g ** 2
    return dict(data)


def load_weight_swap(path):
    """Load weight swap CSV, return {layer_name: muon_drop_pp}."""
    data = {}
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row['layer_name']] = float(row['muon_drop_pp'])
    return data


def match_layers(geometry_layers, swap_layers):
    """Match layer names between geometry scan and weight swap.
    Returns (matched_pairs, unmatched_geometry, unmatched_swap).
    Both datasets use identical PyTorch module names so direct matching works.
    """
    geo_set = set(geometry_layers)
    swap_set = set(swap_layers)
    matched = sorted(geo_set & swap_set)
    return matched, sorted(geo_set - swap_set), sorted(swap_set - geo_set)


def compute_correlation(delta_sq, muon_drop):
    """Compute Spearman and Pearson correlations between δ² and Δacc."""
    x = np.array(delta_sq)
    y = np.array(muon_drop)
    sp_rho, sp_p = stats.spearmanr(x, y)
    pe_r, pe_p = stats.pearsonr(x, y)
    return {
        'spearman_rho': round(float(sp_rho), 4),
        'spearman_p': float(f'{sp_p:.6e}'),
        'pearson_r': round(float(pe_r), 4),
        'pearson_p': float(f'{pe_p:.6e}'),
    }


def make_scatter(results, output_dir):
    """Save scatter plots of δ² vs muon_drop_pp for each epoch."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print('[WARN] matplotlib not available, skipping scatter plot')
        return None

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    for idx, (epoch_key, epoch_data) in enumerate(
        [(k, v) for k, v in sorted(results['epochs'].items())]
    ):
        ax = axes[idx]
        layers = epoch_data['layers']
        x = [l['delta_sq'] for l in layers]
        y = [l['muon_drop_pp'] for l in layers]
        ax.scatter(x, y, alpha=0.7, edgecolors='k', linewidths=0.5, s=50)
        rho = epoch_data['spearman_rho']
        p = epoch_data['spearman_p']
        ax.set_title(f'Epoch {epoch_key}  (ρ={rho:.3f}, p={p:.2e})', fontsize=13)
        ax.set_xlabel('FCSB δ² (Grishina)', fontsize=11)
        ax.set_ylabel('muon_drop_pp (%)', fontsize=11)

        # Annotate outlier layers (top-3 muon_drop)
        sorted_layers = sorted(layers, key=lambda l: l['muon_drop_pp'], reverse=True)
        for l in sorted_layers[:3]:
            ax.annotate(l['layer'], (l['delta_sq'], l['muon_drop_pp']),
                        fontsize=7, alpha=0.8,
                        xytext=(5, 5), textcoords='offset points')

    fig.suptitle('FCSB δ² vs Weight Swap Δacc — Spearman Correlation', fontsize=14, y=1.02)
    plt.tight_layout()
    png_path = os.path.join(output_dir, 'correlation_scatter.png')
    fig.savefig(png_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return png_path


def main():
    parser = argparse.ArgumentParser(description='FCSB δ² vs Weight Swap Δacc correlation test')
    parser.add_argument('--geometry', default='results/gradient_geometry_resnet50.csv',
                        help='Path to gradient geometry scan CSV')
    parser.add_argument('--swap', default='results/resnet50_weight_swap.csv',
                        help='Path to weight swap CSV')
    parser.add_argument('--output', default='results/correlation_test.json',
                        help='Output JSON path')
    parser.add_argument('--rho-threshold', type=float, default=0.3,
                        help='Minimum Spearman ρ for PASS')
    parser.add_argument('--p-threshold', type=float, default=0.05,
                        help='Maximum p-value for PASS')
    args = parser.parse_args()

    # Load data
    geometry = load_geometry_scan(args.geometry)
    swap = load_weight_swap(args.swap)
    epochs_available = sorted(geometry.keys())
    print(f'Geometry scan epochs: {epochs_available}')
    print(f'Weight swap layers: {len(swap)}')

    results = {'model': 'resnet50', 'epochs': {}, 'matching': {}}
    all_pass = True

    for epoch in epochs_available:
        matched, unmatch_geo, unmatch_swap = match_layers(
            geometry[epoch].keys(), swap.keys()
        )
        print(f'\nEpoch {epoch}: {len(matched)} matched, '
              f'{len(unmatch_geo)} geometry-only, {len(unmatch_swap)} swap-only')

        if epoch == epochs_available[0]:
            results['matching'] = {
                'n_geometry': len(geometry[epoch]),
                'n_swap': len(swap),
                'n_matched': len(matched),
                'unmatched_geometry': unmatch_geo,
                'unmatched_swap': unmatch_swap,
            }

        delta_sq = [geometry[epoch][l] for l in matched]
        muon_drop = [swap[l] for l in matched]

        corr = compute_correlation(delta_sq, muon_drop)
        epoch_pass = (corr['spearman_rho'] >= args.rho_threshold
                      and corr['spearman_p'] < args.p_threshold)
        if not epoch_pass:
            all_pass = False

        layer_details = [
            {'layer': l, 'delta_sq': round(geometry[epoch][l], 4),
             'muon_drop_pp': swap[l]}
            for l in matched
        ]

        results['epochs'][str(epoch)] = {
            **corr,
            'n_layers': len(matched),
            'pass': epoch_pass,
            'layers': layer_details,
        }

        print(f'  Spearman ρ = {corr["spearman_rho"]:.4f}, p = {corr["spearman_p"]:.2e}')
        print(f'  Pearson  r = {corr["pearson_r"]:.4f}, p = {corr["pearson_p"]:.2e}')
        print(f'  → {"PASS" if epoch_pass else "FAIL"}')

    results['pass_criteria'] = f'ρ ≥ {args.rho_threshold} and p < {args.p_threshold}'
    results['overall_result'] = 'PASS' if all_pass else 'FAIL'

    # Scatter plot
    output_dir = os.path.dirname(args.output) or '.'
    png = make_scatter(results, output_dir)
    if png:
        results['scatter_plot'] = png
        print(f'\nScatter plot saved: {png}')

    # Strip per-layer details from JSON output (keep it concise)
    json_results = {
        'resnet50': {
            'n_layers_matched': results['matching']['n_matched'],
            'matching_details': {
                'n_geometry_layers': results['matching']['n_geometry'],
                'n_swap_layers': results['matching']['n_swap'],
                'unmatched_geometry': results['matching']['unmatched_geometry'],
                'unmatched_swap': results['matching']['unmatched_swap'],
            },
        }
    }
    for ep_key, ep_data in results['epochs'].items():
        json_results['resnet50'][f'epoch_{ep_key}'] = {
            'spearman_rho': ep_data['spearman_rho'],
            'spearman_p': ep_data['spearman_p'],
            'pearson_r': ep_data['pearson_r'],
            'pearson_p': ep_data['pearson_p'],
            'n_layers': ep_data['n_layers'],
            'pass': ep_data['pass'],
        }
    json_results['resnet50']['pass_criteria'] = results['pass_criteria']
    json_results['resnet50']['overall_result'] = results['overall_result']

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(json_results, f, indent=2)
    print(f'\nResults saved: {args.output}')
    print(f'\n=== OVERALL: {results["overall_result"]} ===')


if __name__ == '__main__':
    main()
