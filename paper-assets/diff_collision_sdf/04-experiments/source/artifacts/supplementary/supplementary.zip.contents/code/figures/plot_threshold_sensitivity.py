#!/usr/bin/env python3
"""Threshold Sensitivity: δ vs dfCAR (v2 — rotation-fixed reeval data)."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import csv
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).resolve().parent
DATA = HERE / 'threshold_sensitivity_v2.csv'
OUT = HERE / 'fig_threshold_sensitivity'


def load_data():
    rows = defaultdict(lambda: {'threshold_mm': [], 'dfCAR': []})
    with open(DATA) as f:
        for row in csv.DictReader(f):
            label = row['label']
            rows[label]['threshold_mm'].append(float(row['threshold_mm']))
            val = row['dfCAR']
            rows[label]['dfCAR'].append(float(val) if val else np.nan)
    return dict(rows)


def compute_group_mean(data, prefix):
    seeds = {k: v for k, v in data.items() if k.startswith(prefix)}
    if not seeds:
        return None, None
    thresholds = list(seeds.values())[0]['threshold_mm']
    all_vals = np.array([s['dfCAR'] for s in seeds.values()])
    return thresholds, np.nanmean(all_vals, axis=0)


def main():
    data = load_data()

    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 12,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.08,
    })

    fig, ax = plt.subplots(figsize=(8, 5))

    group_cfg = [
        ('LoRA', r'LoRA ($\lambda$=0)', '#888888'),
        ('SDF λ=0.005', r'SDF ($\lambda$=0.005)', '#1b9e77'),
        ('SDF λ=0.01', r'SDF ($\lambda$=0.01)', '#d95f02'),
    ]

    for prefix, mean_label, color in group_cfg:
        seeds = {k: v for k, v in data.items() if k.startswith(prefix)}
        for k, v in seeds.items():
            ax.plot(v['threshold_mm'], v['dfCAR'],
                    ls='--', color=color, lw=0.8, alpha=0.35,
                    marker='o', markersize=2.5, zorder=2)

        th, mean_vals = compute_group_mean(data, prefix)
        if th is not None:
            ax.plot(th, mean_vals,
                    ls='-', color=color, lw=2.2, marker='o', markersize=5,
                    markeredgecolor='white', markeredgewidth=0.8,
                    label=f'{mean_label} mean (n={len(seeds)})',
                    zorder=4)

    all_thresholds = list(data.values())[0]['threshold_mm']
    all_vals = np.array([v['dfCAR'] for v in data.values()])
    pooled_mean = np.nanmean(all_vals, axis=0)
    ax.plot(all_thresholds, pooled_mean,
            ls='-', color='#2171B5', lw=2.5, marker='s', markersize=6,
            markeredgecolor='white', markeredgewidth=1.0,
            label=f'All Pooled (n={len(data)})', zorder=5)

    ax.axvline(x=100, color='#666666', ls='--', lw=1.2, alpha=0.6, zorder=1)
    ax.text(115, 0.92, r'Paper threshold ($\delta$=100 mm)',
            fontsize=9, color='#555555', ha='left', va='top',
            transform=ax.get_xaxis_transform())

    ax.set_xscale('log')
    ax.set_xlabel(r'Displacement Threshold $\delta$ (mm)', fontsize=13)
    ax.set_ylabel('dfCAR (%)', fontsize=13)
    ax.set_title(r'Threshold Sensitivity: dfCAR vs $\delta$', fontsize=14, pad=12)

    ax.set_xticks([2, 5, 10, 20, 50, 100, 200, 300])
    ax.get_xaxis().set_major_formatter(mticker.ScalarFormatter())
    ax.tick_params(axis='x', which='minor', bottom=False)

    flat_vals = all_vals.flatten()
    flat_vals = flat_vals[~np.isnan(flat_vals)]
    ymin = max(0, flat_vals.min() - 3)
    ymax = min(100, flat_vals.max() + 3)
    ax.set_ylim(ymin, ymax)

    ax.grid(axis='y', alpha=0.2, lw=0.5)
    ax.grid(axis='x', alpha=0.1, lw=0.5)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.legend(loc='lower left', frameon=True, fancybox=False,
              edgecolor='#cccccc', fontsize=10, ncol=2)

    fig.tight_layout()
    fig.savefig(OUT.with_suffix('.pdf'))
    fig.savefig(OUT.with_suffix('.png'))
    plt.close(fig)
    print(f"Saved: {OUT.with_suffix('.pdf')} and {OUT.with_suffix('.png')}")


if __name__ == '__main__':
    main()
