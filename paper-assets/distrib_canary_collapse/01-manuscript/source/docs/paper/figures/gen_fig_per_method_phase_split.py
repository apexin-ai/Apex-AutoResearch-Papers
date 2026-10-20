#!/usr/bin/env python3
"""Per-method dose-response: 5 individual panel PDFs for cross-page floating.
Each panel is a single bar chart showing /8 sig counts per alpha level."""
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
    'xtick.labelsize': 7,
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

alphas = [0.00, 0.10, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.60, 0.75, 1.00]
alpha_labels = [f'{a:.2f}' for a in alphas]

methods = {
    'naive_xcorr': {
        'label': 'Naive XCorr',
        'panel': '(a)',
        'color': '#E66101',
        'counts': [8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7],
    },
    'diff_xcorr': {
        'label': 'Diff. XCorr',
        'panel': '(b)',
        'color': '#FDB863',
        'counts': [4, None, 6, 3, 4, 4, None, 7, 8, 6, 6],
    },
    'threshold': {
        'label': 'Threshold',
        'panel': '(c)',
        'color': '#5E3C99',
        'counts': [3, None, None, None, None, None, None, 4, None, None, 2],
    },
    'perm_granger': {
        'label': 'Perm. Granger',
        'panel': '(d)',
        'color': '#2166AC',
        'counts': [0, 0, 0, 0, 0, 0, 0, 6, 0, 6, 6],
        'hero': True,
    },
    'toda_yamamoto': {
        'label': 'Toda-Yamamoto',
        'panel': '(e)',
        'color': '#B2ABD2',
        'counts': [1, None, 2, None, 1, None, 1, 4, 3, None, 3],
    },
}

x = np.arange(len(alphas))

for key, m in methods.items():
    fig, ax = plt.subplots(figsize=(5.5, 1.6))

    counts = []
    valid_x = []
    for i, c in enumerate(m['counts']):
        if c is not None:
            counts.append(c)
            valid_x.append(i)

    bars = ax.bar(valid_x, counts, 0.7, color=m['color'], alpha=0.85,
                  edgecolor='white', linewidth=0.3)

    for xi, c in zip(valid_x, counts):
        if c > 0:
            fw = 'bold' if m.get('hero') and c >= 6 else 'normal'
            ax.text(xi, c + 0.15, str(c), ha='center', va='bottom',
                    fontsize=7, fontweight=fw)

    ax.set_ylim(0, 8.8)
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.set_ylabel('/8 sig.', fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(alpha_labels, fontsize=6.5)
    ax.set_xlabel('Contamination level α', fontsize=8)
    ax.set_title(f'{m["panel"]}  {m["label"]}', fontsize=9, fontweight='bold', loc='left')
    ax.yaxis.grid(True, alpha=0.15, linewidth=0.3)
    ax.set_axisbelow(True)

    fig.tight_layout()
    for fmt in ['pdf', 'png']:
        fig.savefig(OUT / f'fig_per_method_phase_{key}.{fmt}', dpi=300)
    plt.close()
    print(f'Saved fig_per_method_phase_{key}.pdf')

print('Done: 5 individual panel PDFs')
