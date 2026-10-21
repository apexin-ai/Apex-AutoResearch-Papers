#!/usr/bin/env python3
"""Figure 1: Multi-task Count-Degradation Curves with error bars."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# ---------- Style ----------
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

CB_BLUE = '#0173B2'
CB_ORANGE = '#DE8F05'
CB_GREEN = '#029E73'

fig, axes = plt.subplots(1, 3, figsize=(6.75, 2.25))

# ===== (a) Few-NERD NER =====
ax = axes[0]
counts_a = [1, 2, 6, 12, 22, 44, 64]
recall_a = [0.641, 0.560, 0.475, 0.329, 0.267, 0.396, 0.304]
# SD across 5 random batches (text_match recall); count_1 = solo baseline (no batch variance)
sd_a = [0, 0.070, 0.161, 0.088, 0.086, 0.099, 0.002]
ax.errorbar(counts_a, recall_a, yerr=sd_a, fmt='o-', color=CB_BLUE,
            markersize=4, linewidth=1.5, capsize=2, capthick=0.8, elinewidth=0.8)
ax.set_xlabel('Number of Entity Types')
ax.set_ylabel('Recall')
ax.set_title('(a) Few-NERD NER', fontweight='bold', fontsize=9)
ax.set_xscale('log', base=2)
ax.set_xticks(counts_a)
ax.set_xticklabels([str(c) for c in counts_a])
ax.set_ylim(0.10, 0.75)
ax.tick_params(axis='x', rotation=0)

# ===== (b) FewRel RE =====
ax = axes[1]
counts_b = [1, 4, 8, 16, 32, 64, 80]
acc_b = [0.8573, 0.8667, 0.8021, 0.6958, 0.6578, 0.5424, 0.5042]
# SD across 5 random batches; count_1 = solo (80 types), count_80 = full schema (SD=0)
sd_b = [0, 0.111, 0.077, 0.080, 0.053, 0.026, 0]
ax.errorbar(counts_b, acc_b, yerr=sd_b, fmt='s-', color=CB_ORANGE,
            markersize=4, linewidth=1.5, capsize=2, capthick=0.8, elinewidth=0.8)
ax.set_xlabel('Number of Relation Types')
ax.set_ylabel('Accuracy')
ax.set_title('(b) FewRel RE', fontweight='bold', fontsize=9)
ax.set_xscale('log', base=2)
ax.set_xticks(counts_b)
ax.set_xticklabels([str(c) for c in counts_b])
ax.set_ylim(0.40, 1.00)

# ===== (c) MAVEN ED =====
ax = axes[2]
counts_c = [1, 6, 12, 22, 44, 64]
f1_c = [0.106, 0.103, 0.146, 0.185, 0.247, 0.245]
# SD across 5 random batches (relaxed F1); count_1 = solo baseline
sd_c = [0, 0.079, 0.057, 0.057, 0.038, 0.020]
ax.errorbar(counts_c, f1_c, yerr=sd_c, fmt='D-', color=CB_GREEN,
            markersize=4, linewidth=1.5, capsize=2, capthick=0.8, elinewidth=0.8)
ax.set_xlabel('Number of Event Types')
ax.set_ylabel('Relaxed F1')
ax.set_title('(c) MAVEN ED', fontweight='bold', fontsize=9)
ax.set_xscale('log', base=2)
ax.set_xticks(counts_c)
ax.set_xticklabels([str(c) for c in counts_c])
ax.set_ylim(0.00, 0.32)

# annotate upward trend
ax.annotate('↑ centrality\n   confound', xy=(44, 0.247), xytext=(20, 0.29),
            fontsize=7, color=CB_GREEN, fontstyle='italic',
            arrowprops=dict(arrowstyle='->', color=CB_GREEN, lw=0.8))

plt.tight_layout(w_pad=1.8)
import os
outdir = os.environ.get('FIG_OUTDIR', '/root/schema-dag-extraction/figures/paper')
outpath = os.path.join(outdir, 'fig_count_curves.pdf')
os.makedirs(outdir, exist_ok=True)
fig.savefig(outpath, format='pdf')
fig.savefig(outpath.replace('.pdf', '.png'), format='png', dpi=300)
print(f'Saved: {outpath}')
plt.close()
