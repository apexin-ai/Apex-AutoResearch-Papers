#!/usr/bin/env python3
"""Generate Fig.3: Strategy Transition Heatmaps for Crescendo / FITD / DD."""

import argparse
import json
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

DISPLAY_NAMES = {
    'none': 'None',
    'rapport_building': 'Rapport',
    'authority_appeal': 'Authority',
    'emotional_manipulation': 'Emotion',
    'logical_reframing': 'Logic',
    'role_assignment': 'Role',
    'gradual_escalation': 'Escalation',
    'obfuscation': 'Obfuscation',
    'direct_request': 'Direct',
}

ATTACK_TITLES = {
    'crescendo': 'Crescendo',
    'fitd': 'FITD',
    'deceptive_delight': 'Deceptive Delight',
}


def make_heatmap(ax, matrix, labels, title, total_transitions):
    n = len(labels)
    mat = np.array(matrix, dtype=float)

    vmax = mat.max()
    if vmax <= 0:
        vmax = 1.0

    norm = mcolors.SymLogNorm(linthresh=1.0, linscale=0.5, vmin=0, vmax=vmax)

    cmap = plt.cm.YlOrRd.copy()
    cmap.set_under('white')

    im = ax.imshow(mat, cmap=cmap, norm=norm, aspect='equal',
                   interpolation='nearest')

    for i in range(n):
        for j in range(n):
            val = int(mat[i, j])
            if val == 0:
                continue
            brightness = im.cmap(im.norm(val))[:3]
            lum = 0.299 * brightness[0] + 0.587 * brightness[1] + 0.114 * brightness[2]
            color = 'white' if lum < 0.5 else 'black'
            ax.text(j, i, str(val), ha='center', va='center',
                    fontsize=6.5, color=color, fontweight='medium')

    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_yticklabels(labels)
    ax.set_xlabel('To Strategy')
    ax.set_ylabel('From Strategy')
    ax.set_title(f'{title}\n(n={total_transitions} transitions)', fontsize=10, pad=6)

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.5)

    return im


def main():
    parser = argparse.ArgumentParser(description='Plot strategy transition heatmaps')
    parser.add_argument('--input', required=True, help='Path to strategy_transition_matrices.json')
    parser.add_argument('--output', required=True, help='Output path (PDF)')
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)

    strategy_names = data['strategy_names']
    labels = [DISPLAY_NAMES.get(s, s) for s in strategy_names]

    attack_keys = ['crescendo', 'fitd', 'deceptive_delight']

    fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.8))

    ims = []
    for idx, key in enumerate(attack_keys):
        attack = data[key]
        mat = attack['raw_counts']
        total = attack['stats']['total_transitions']
        title = ATTACK_TITLES[key]
        im = make_heatmap(axes[idx], mat, labels, title, total)
        ims.append(im)

    fig.subplots_adjust(bottom=0.22, wspace=0.35, right=0.92)

    cbar_ax = fig.add_axes([0.93, 0.22, 0.015, 0.65])
    cbar = fig.colorbar(ims[0], cax=cbar_ax)
    cbar.set_label('Transition Count', fontsize=9)

    base, ext = os.path.splitext(args.output)
    pdf_path = base + '.pdf'
    png_path = base + '.png'

    fig.savefig(pdf_path, format='pdf')
    fig.savefig(png_path, format='png')
    print(f'Saved: {pdf_path}')
    print(f'Saved: {png_path}')
    plt.close(fig)


if __name__ == '__main__':
    main()
