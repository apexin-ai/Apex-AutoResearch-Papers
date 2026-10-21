#!/usr/bin/env python3
"""Figure A3: MF2 ρ degradation — DIF-ordered vs random item removal."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'font.size': 7,
    'axes.titlesize': 7.5,
    'axes.labelsize': 6.5,
    'xtick.labelsize': 5.5,
    'ytick.labelsize': 5.5,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 0.9,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

COL_DIF = '#D55E00'
COL_RND = '#0072B2'

DATA_PATH = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_rho_degradation/degradation_curves.csv'
OUT_DIR = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper'

df = pd.read_csv(DATA_PATH)

# Total item counts (back-calculated from 5% removal row)
bench_items = {}
for b in df['benchmark'].unique():
    n_at_5 = df[(df['benchmark'] == b) & (df['removal_pct'] == 5) & (df['removal_type'] == 'dif_ordered')]['n_items_remaining'].values[0]
    bench_items[b] = round(n_at_5 / 0.95)

BENCH_ORDER = ['truthfulqa', 'arc', 'winogrande', 'gsm8k', 'hellaswag', 'mmlu']
BENCH_LABELS = {
    'truthfulqa': 'TruthfulQA',
    'arc': 'ARC',
    'winogrande': 'WinoGrande',
    'gsm8k': 'GSM8K',
    'hellaswag': 'HellaSwag',
    'mmlu': 'MMLU',
}

fig, axes = plt.subplots(2, 3, figsize=(7, 3.5))
axes = axes.flatten()

for idx, bench in enumerate(BENCH_ORDER):
    ax = axes[idx]
    bdf = df[df['benchmark'] == bench]

    dif = bdf[bdf['removal_type'] == 'dif_ordered'].sort_values('removal_pct')
    rnd_mean = bdf[bdf['removal_type'] == 'random_mean'].sort_values('removal_pct')
    rnd_std = bdf[bdf['removal_type'] == 'random_std'].sort_values('removal_pct')

    pcts = dif['removal_pct'].values
    y_dif = dif['spearman_rho'].values
    y_rnd = rnd_mean['spearman_rho'].values
    y_std = rnd_std['spearman_rho'].values

    ax.fill_between(pcts, y_rnd - y_std, y_rnd + y_std,
                    color=COL_RND, alpha=0.15, linewidth=0)
    ax.plot(pcts, y_dif, color=COL_DIF, marker='o', markersize=2.5,
            label='DIF-ordered', zorder=3)
    ax.plot(pcts, y_rnd, color=COL_RND, marker='s', markersize=2.5,
            linestyle='--', label='Random', zorder=3)

    # Threshold lines
    for xv, lbl in [(15, 'Monitor/Flag'), (25, 'Flag/Act')]:
        ax.axvline(xv, color='#888888', linewidth=0.5, linestyle=':', zorder=1)

    # Y-axis: adaptive per panel with some padding
    all_y = np.concatenate([y_dif, y_rnd - y_std, y_rnd + y_std])
    ymin, ymax = all_y.min(), all_y.max()
    margin = (ymax - ymin) * 0.15
    ax.set_ylim(ymin - margin, ymax + margin * 2)  # extra top margin for labels

    # Re-draw threshold text after ylim is set
    for txt in ax.texts:
        txt.remove()
    ytop = ax.get_ylim()[1]
    for xv, lbl in [(15, 'Monitor/Flag'), (25, 'Flag/Act')]:
        ax.text(xv, ytop, lbl, ha='center', va='bottom',
                fontsize=4.5, color='#666666', clip_on=False)

    n_total = bench_items[bench]
    ax.set_title(f'{BENCH_LABELS[bench]} ($N$={n_total:,})')

    ax.set_xticks([5, 10, 15, 20, 25, 30, 35, 40, 50])
    ax.tick_params(axis='both', which='both', length=2, pad=2)

    if idx >= 3:
        ax.set_xlabel('Items removed (%)')
    if idx % 3 == 0:
        ax.set_ylabel('Spearman $\\rho$')

    # Legend only in first panel
    if idx == 0:
        ax.legend(loc='lower left', frameon=False, handlelength=1.5)

fig.tight_layout(h_pad=1.0, w_pad=0.8)

os.makedirs(OUT_DIR, exist_ok=True)
fig.savefig(os.path.join(OUT_DIR, 'fig_A3_rho_degradation.pdf'))
fig.savefig(os.path.join(OUT_DIR, 'fig_A3_rho_degradation.png'))
print('Saved fig_A3_rho_degradation.pdf and .png')
