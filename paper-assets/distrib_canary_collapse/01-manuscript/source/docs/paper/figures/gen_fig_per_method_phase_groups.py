#!/usr/bin/env python3
"""Per-method dose-response: 2 group PDFs for cross-page floating.
Group 1: (a) Naive XCorr, (b) Diff. XCorr, (c) Threshold
Group 2: (d) Perm. Granger, (e) Toda-Yamamoto"""
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

panels = [
    ('(a)', 'Naive XCorr', '#E66101', [8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7], False),
    ('(b)', 'Diff. XCorr', '#FDB863', [4, None, 6, 3, 4, 4, None, 7, 8, 6, 6], False),
    ('(c)', 'Threshold',   '#5E3C99', [3, None, None, None, None, None, None, 4, None, None, 2], False),
    ('(d)', 'Perm. Granger', '#2166AC', [0, 0, 0, 0, 0, 0, 0, 6, 0, 6, 6], True),
    ('(e)', 'Toda-Yamamoto', '#B2ABD2', [1, None, 2, None, 1, None, 1, 4, 3, None, 3], False),
]

groups = [
    ('top', panels[:3]),
    ('bottom', panels[3:]),
]

x = np.arange(len(alphas))

for gname, gpanels in groups:
    n = len(gpanels)
    fig, axes = plt.subplots(n, 1, figsize=(5.5, 1.7 * n), sharex=True)
    if n == 1:
        axes = [axes]

    for ax, (plabel, mname, color, counts, hero) in zip(axes, gpanels):
        valid_x = [i for i, c in enumerate(counts) if c is not None]
        valid_c = [c for c in counts if c is not None]

        ax.bar(valid_x, valid_c, 0.7, color=color, alpha=0.85,
               edgecolor='white', linewidth=0.3)

        for xi, c in zip(valid_x, valid_c):
            if c > 0:
                fw = 'bold' if hero and c >= 6 else 'normal'
                ax.text(xi, c + 0.15, str(c), ha='center', va='bottom',
                        fontsize=7, fontweight=fw)

        ax.set_ylim(0, 8.8)
        ax.set_yticks([0, 2, 4, 6, 8])
        ax.set_ylabel('/8 sig.', fontsize=8)
        ax.set_title(f'{plabel}  {mname}', fontsize=9, fontweight='bold', loc='left')
        ax.yaxis.grid(True, alpha=0.15, linewidth=0.3)
        ax.set_axisbelow(True)

    axes[-1].set_xticks(x)
    axes[-1].set_xticklabels(alpha_labels, fontsize=6.5)
    axes[-1].set_xlabel('Contamination level α', fontsize=8)

    fig.tight_layout(h_pad=0.6)
    for fmt in ['pdf', 'png']:
        fig.savefig(OUT / f'fig_per_method_phase_{gname}.{fmt}', dpi=300)
    plt.close()
    print(f'Saved fig_per_method_phase_{gname}.pdf ({n} panels)')
