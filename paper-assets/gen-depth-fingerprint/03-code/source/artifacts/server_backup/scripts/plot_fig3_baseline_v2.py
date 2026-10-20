#!/usr/bin/env python3
"""Figure 3: Baseline Comparison — horizontal lollipop chart with bootstrap CI."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 10,
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Data: 8gen_table3_v6_unified.json (pooled LOGO 8-fold, binary F1)
# Cost: efficiency_comparison.json
methods = [
    {'name': '4-Det + Surface',  'f1': 0.707,  'ci_lo': 0.701,  'ci_hi': 0.7121, 'cost_ms': 22.8, 'group': 'ensemble'},
    {'name': 'DDR 7-Feature',    'f1': 0.7014, 'ci_lo': 0.6957, 'ci_hi': 0.7066, 'cost_ms': 9.7,  'group': 'ours'},
    {'name': '4-Det Ensemble',   'f1': 0.6975, 'ci_lo': 0.6914, 'ci_hi': 0.703,  'cost_ms': 22.8, 'group': 'ensemble'},
    {'name': 'LD-Score',       'f1': 0.6756, 'ci_lo': 0.6699, 'ci_hi': 0.6814, 'cost_ms': 0.6,  'group': 'individual'},
    {'name': 'Avg Log-Prob',     'f1': 0.6735, 'ci_lo': 0.6673, 'ci_hi': 0.6792, 'cost_ms': 8.6,  'group': 'individual'},
    {'name': 'Fast-DetectGPT',   'f1': 0.576,  'ci_lo': 0.57,   'ci_hi': 0.5819, 'cost_ms': 8.6,  'group': 'individual'},
    {'name': 'Binoculars',       'f1': 0.5336, 'ci_lo': 0.5278, 'ci_hi': 0.5393, 'cost_ms': 13.6, 'group': 'individual'},
]

methods.sort(key=lambda x: x['f1'], reverse=True)

COLORS = {'ensemble': '#4c72b0', 'ours': '#c44e52', 'individual': '#999999'}

fig, ax = plt.subplots(figsize=(3.4, 2.8))
n = len(methods)
x_left = 0.50

for i, m in enumerate(methods):
    y = n - 1 - i
    c = COLORS[m['group']]

    # Lollipop stem
    ax.hlines(y=y, xmin=x_left, xmax=m['f1'], color=c, linewidth=1.5, alpha=0.7, zorder=2)

    # Bootstrap 95% CI whisker
    ax.hlines(y=y, xmin=m['ci_lo'], xmax=m['ci_hi'], color=c, linewidth=3.0, alpha=0.3, zorder=3)

    # Endpoint marker
    marker = 'D' if m['group'] == 'ours' else 'o'
    ms = 7 if m['group'] == 'ours' else 6
    ax.plot(m['f1'], y, marker=marker, color=c, markersize=ms,
            markeredgecolor='white', markeredgewidth=0.5, zorder=5)

# Highlight "Ours" row
ours_y = n - 1 - next(i for i, m in enumerate(methods) if m['group'] == 'ours')
ax.axhspan(ours_y - 0.4, ours_y + 0.4, color='#fde8e8', alpha=0.5, zorder=0)

# Y-axis labels (top = highest F1)
ax.set_yticks(range(n))
ax.set_yticklabels([methods[n - 1 - j]['name'] for j in range(n)], fontsize=8)

# X-axis
ax.set_xlim(x_left, 0.72)
ax.set_ylim(-0.6, n - 0.4)
ax.set_xlabel('Binary F1 (LOGO)', fontsize=9)
ax.xaxis.grid(True, color='#eeeeee', linewidth=0.5, zorder=0)

# Cost labels in right margin
for i, m in enumerate(methods):
    y = n - 1 - i
    cost_str = f"{m['cost_ms']:.0f} ms" if m['cost_ms'] >= 1 else f"{m['cost_ms']:.1f} ms"
    ax.text(0.724, y, cost_str, fontsize=6.5, color='#888888', va='center', ha='left', clip_on=False)

out_base = '/root/gen-depth-fingerprint/artifacts/_project/chart/fig3_baseline_comparison'
plt.savefig(f'{out_base}.pdf', bbox_inches='tight', dpi=300, pad_inches=0.02)
plt.savefig(f'{out_base}.png', bbox_inches='tight', dpi=300, pad_inches=0.02)
print('Done: fig3_baseline_comparison.pdf/.png')
