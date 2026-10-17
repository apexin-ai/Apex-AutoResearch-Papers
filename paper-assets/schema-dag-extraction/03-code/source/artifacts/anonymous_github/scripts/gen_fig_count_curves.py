#!/usr/bin/env python3
"""Figure: Count-Degradation Curves (NER + RE)."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

CB_BLUE = '#0173B2'
CB_ORANGE = '#DE8F05'

fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))

# --- Panel (a): Few-NERD NER — exp001 Qwen3-32B-FP8 Recall ---
ax = axes[0]
counts_a = [1, 2, 6, 12, 22, 44, 64]
recall_a = [0.720, 0.698, 0.620, 0.539, 0.527, 0.551, 0.418]
ax.plot(counts_a, recall_a, 'o-', color=CB_BLUE, markersize=7, linewidth=1.8,
        markeredgecolor='white', markeredgewidth=0.8)
ax.set_xlabel('Number of Entity Types')
ax.set_ylabel('Recall')
ax.text(0.03, 0.97, '(a)', transform=ax.transAxes, fontsize=13,
        fontweight='bold', va='top', ha='left')
ax.set_xscale('log', base=2)
ax.set_xticks(counts_a)
ax.set_xticklabels([str(c) for c in counts_a])
ax.set_ylim(0.38, 0.78)
ax.grid(True, alpha=0.3, color='grey', linewidth=0.5)

# --- Panel (b): FewRel RE — exp_fewrel_formal_80rel Qwen3-32B-FP8 Accuracy ---
ax = axes[1]
counts_b = [1, 4, 8, 16, 32, 40, 64, 80]
acc_b   = [0.8573, 0.8667, 0.8021, 0.6958, 0.6578, 0.588, 0.5424, 0.5042]
ax.plot(counts_b, acc_b, 's-', color=CB_ORANGE, markersize=7, linewidth=1.8,
        markeredgecolor='white', markeredgewidth=0.8)
ax.set_xlabel('Number of Relation Types')
ax.set_ylabel('Accuracy')
ax.text(0.03, 0.97, '(b)', transform=ax.transAxes, fontsize=13,
        fontweight='bold', va='top', ha='left')
ax.set_xscale('log', base=2)
ax.set_xticks(counts_b)
ax.set_xticklabels([str(c) for c in counts_b])
ax.set_ylim(0.45, 0.92)
ax.grid(True, alpha=0.3, color='grey', linewidth=0.5)

plt.tight_layout(w_pad=2.5)
outpath = './figures/paper/fig_count_curves.pdf'
fig.savefig(outpath, format='pdf')
print(f'Saved: {outpath}')

# Verification
print('\n--- Data Verification ---')
print('Panel (a) Few-NERD NER [exp001]:')
for c, r in zip(counts_a, recall_a):
    print(f'  count_{c}: recall={r}')
print(f'  y-range: [{min(recall_a):.3f}, {max(recall_a):.3f}]')

print('Panel (b) FewRel RE [exp_fewrel_formal_80rel + 40rel_r4]:')
for c, a in zip(counts_b, acc_b):
    print(f'  count_{c}: accuracy={a}')
print(f'  y-range: [{min(acc_b):.4f}, {max(acc_b):.4f}]')

plt.close()
