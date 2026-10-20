#!/usr/bin/env python3
"""Figure 17: Per-method detection phase diagrams — vertical layout.
5 stacked panels (one per method), each showing /8 pair counts across alpha.
Data from Table tab:dose_response_full (T=10, seed 42, Pythia-410M, fp32)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

alphas = [0.00, 0.10, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.75, 1.00]
alpha_labels = ['0.00', '0.10', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50', '0.55', '0.60', '0.75', '1.00']

data = {
    'Naive XCorr':     [8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8],
    'Diff. XCorr':     [4, 6, 3, 4, 4, 3, 6, 7, 8, 6, 6, 6],
    'Threshold':       [3, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2],
    'Perm. Granger':   [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 6, 6],
    'Toda-Yamamoto':   [1, 0, 2, 3, 1, 4, 1, 3, 1, 0, 3, 1],
}

method_colors = {
    'Naive XCorr':   '#B2182B',
    'Diff. XCorr':   '#E08214',
    'Threshold':     '#8CB4D5',
    'Perm. Granger': '#2166AC',
    'Toda-Yamamoto': '#5AAE61',
}

hero = 'Perm. Granger'
x = np.arange(len(alphas))

fig, axes = plt.subplots(5, 1, figsize=(3.4, 8.5), sharex=True)

for ax, (method, vals) in zip(axes, data.items()):
    color = method_colors[method]
    alpha_face = 1.0 if method == hero else 0.75
    edge = 'black' if method == hero else color
    lw = 0.8 if method == hero else 0.3

    bars = ax.bar(x, vals, 0.7, color=color, alpha=alpha_face,
                  edgecolor=edge, linewidth=lw)

    for i, v in enumerate(vals):
        if v > 0:
            ax.text(i, v + 0.2, str(v), ha='center', va='bottom',
                    fontsize=6, fontweight='bold' if method == hero else 'normal')

    ax.set_ylabel('/8 sig.', fontsize=7)
    ax.set_ylim(0, 9.5)
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.axhline(0, color='#CCCCCC', linewidth=0.3)
    ax.yaxis.grid(True, alpha=0.15, linewidth=0.3)
    ax.set_axisbelow(True)

    label = '(a)' if method == 'Naive XCorr' else \
            '(b)' if method == 'Diff. XCorr' else \
            '(c)' if method == 'Threshold' else \
            '(d)' if method == 'Perm. Granger' else '(e)'
    ax.set_title(f'{label}  {method}', fontsize=9, fontweight='bold' if method == hero else 'normal',
                 loc='left', pad=4)

axes[-1].set_xticks(x)
axes[-1].set_xticklabels(alpha_labels, fontsize=7)
axes[-1].set_xlabel('Contamination level $\\alpha$', fontsize=9)

fig.tight_layout(h_pad=0.8)

for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_per_method_phase.{fmt}', dpi=300)
plt.close()
print('Saved fig_per_method_phase.pdf + .png')
