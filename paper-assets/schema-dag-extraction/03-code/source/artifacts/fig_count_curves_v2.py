#!/usr/bin/env python3
"""Figure 1a: Count-Degradation Curves (NER + RE) — optimized.

L0: Single-panel two-series layout (matches ACL/EMNLP IE paper style)
L1: Okabe-Ito colors, no grid, no top/right spines, ≥7pt, PDF TrueType
L2: Hollow markers for full-schema; error bars for batch variance
L3: Pattern D (hollow vs solid), Pattern C (random-chance ref line)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'lines.linewidth': 1.4,
    'lines.markersize': 5,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

C_RE = '#4477AA'
C_NER = '#EE7733'

# --- Data ---
# FewRel RE (d051, seed 42, 25 batches per count)
re_counts = np.array([1, 4, 8, 16, 32, 40, 64, 80])
re_mean   = np.array([0.857, 0.870, 0.805, 0.719, 0.652, 0.606, 0.539, 0.504])
re_sd     = np.array([0, 0.068, 0.082, 0.063, 0.049, 0.042, 0.026, 0.0002])

# Few-NERD NER (25 batches, matching paper §4.1 text)
ner_counts = np.array([1, 2, 6, 12, 22, 44, 66])
ner_mean   = np.array([0.720, 0.515, 0.399, 0.318, 0.279, 0.309, 0.407])
ner_sd     = np.array([0, 0.07, 0.10, 0.06, 0.05, 0.06, 0.002])

# Full-schema indices (no batch variance)
re_full_idx = len(re_counts) - 1  # count 80
ner_full_idx = len(ner_counts) - 1  # count 66

fig, ax = plt.subplots(figsize=(3.5, 2.8))

# --- RE: circles, error bars, all points unified ---
ax.errorbar(re_counts, re_mean, yerr=re_sd,
            fmt='o-', color=C_RE, markerfacecolor=C_RE, markeredgecolor=C_RE,
            capsize=1.5, capthick=0.6, elinewidth=0.6, zorder=3)

# --- NER: triangles, error bars, all points unified ---
ax.errorbar(ner_counts, ner_mean, yerr=ner_sd,
            fmt='^-', color=C_NER, markerfacecolor=C_NER, markeredgecolor=C_NER,
            capsize=1.5, capthick=0.6, elinewidth=0.6, zorder=3)

# --- Pattern C: random-chance reference for RE (1/k) ---
k_ref = np.array([4, 8, 16, 32, 64, 80])
chance = 1.0 / k_ref
ax.plot(k_ref, chance, ':', color='#CCCCCC', linewidth=0.8, alpha=0.6, zorder=1)
t = ax.text(80, 1/80 + 0.015, 'chance', fontsize=6, color='#CCCCCC',
            ha='right', va='bottom', fontstyle='italic')
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# --- Legend ---
legend_elements = [
    Line2D([0], [0], marker='o', color=C_RE, markerfacecolor=C_RE,
           markersize=5, linewidth=1.2, label='FewRel RE (accuracy)'),
    Line2D([0], [0], marker='^', color=C_NER, markerfacecolor=C_NER,
           markersize=5, linewidth=1.2, label='Few-NERD NER (recall)'),
]
ax.legend(handles=legend_elements, loc='lower left', framealpha=0.8,
          edgecolor='none', handlelength=1.5, bbox_to_anchor=(0.02, 0.02))

ax.set_xlabel('Number of Schema Types')
ax.set_ylabel('Performance')
ax.set_xlim(0.8, 95)
ax.set_ylim(0.0, 0.95)
ax.set_xscale('log', base=2)
ax.set_xticks([1, 2, 4, 8, 16, 32, 64])
ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64'])

plt.tight_layout(pad=0.3)
outdir = os.environ.get('FIG_OUTDIR',
    '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper')
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, 'fig_count_curves.pdf')
fig.savefig(outpath, format='pdf')
fig.savefig(outpath.replace('.pdf', '.png'), format='png', dpi=300)
print(f'Saved: {outpath}')
plt.close()
