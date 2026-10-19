#!/usr/bin/env python3
"""Fig 4: Representation Geometry — 2-panel figure for StructFuse paper."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

# ── Data ──────────────────────────────────────────────────────────────────────
strategies = ['Random', 'Embedding', 'Dataflow']

data = {
    'Qwen2.5-Coder-3B': {
        'pos_sim':      [0.9855, 0.9855, 0.9856],
        'neg_sim':      [0.9111, 0.9685, 0.9563],
        'margin':       [0.0743, 0.0170, 0.0293],
        'margin_std':   [0.2322, 0.1140, 0.1407],
        'pct_positive': [81.8,   58.8,   73.9],
    },
    'StarCoder2-3B': {
        'pos_sim':      [0.7985, 0.8079, 0.8009],
        'neg_sim':      [0.6045, 0.7409, 0.6818],
        'margin':       [0.1940, 0.0670, 0.1192],
        'margin_std':   [0.2788, 0.2056, 0.2264],
        'pct_positive': [78.0,   55.0,   70.4],
    },
}

# ── Style ─────────────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 8.5,
    'axes.labelsize': 9,
    'axes.titlesize': 9.5,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# Colorblind-friendly: blue for Qwen, orange for StarCoder
c_qwen = '#4477AA'
c_star = '#EE7733'
c_qwen_light = '#88BBDD'
c_star_light = '#FFBB78'

# ── Figure ────────────────────────────────────────────────────────────────────
fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7.0, 2.8),
                                  gridspec_kw={'width_ratios': [1, 1.15], 'wspace': 0.35})

# ── Panel (a): Margin Comparison ─────────────────────────────────────────────
x = np.arange(len(strategies))
bar_w = 0.32

bars_q = ax_a.bar(x - bar_w/2, data['Qwen2.5-Coder-3B']['margin'], bar_w,
                  yerr=data['Qwen2.5-Coder-3B']['margin_std'],
                  color=c_qwen, edgecolor='white', linewidth=0.4,
                  error_kw=dict(lw=0.7, capsize=2.5, capthick=0.7),
                  label='Qwen2.5-Coder-3B', zorder=3)
bars_s = ax_a.bar(x + bar_w/2, data['StarCoder2-3B']['margin'], bar_w,
                  yerr=data['StarCoder2-3B']['margin_std'],
                  color=c_star, edgecolor='white', linewidth=0.4,
                  error_kw=dict(lw=0.7, capsize=2.5, capthick=0.7),
                  label='StarCoder2-3B', zorder=3)

# Ratio annotations
ratios = [2.61, 3.94, 4.07]
for i, r in enumerate(ratios):
    y_top = data['StarCoder2-3B']['margin'][i] + data['StarCoder2-3B']['margin_std'][i] + 0.012
    ax_a.annotate(f'{r:.1f}×', xy=(x[i], y_top), fontsize=6.5,
                  ha='center', va='bottom', color='#555555',
                  fontweight='medium')

ax_a.set_ylabel('Margin (pos − neg similarity)')
ax_a.set_xticks(x)
ax_a.set_xticklabels(strategies)
ax_a.set_ylim(0, 0.52)
ax_a.yaxis.set_major_locator(mticker.MultipleLocator(0.1))
ax_a.legend(loc='upper right', frameon=True, fancybox=False,
            edgecolor='#cccccc', framealpha=0.95)
ax_a.set_axisbelow(True)
ax_a.yaxis.grid(True, linewidth=0.3, alpha=0.5)
ax_a.text(-0.12, 1.04, '(a)', transform=ax_a.transAxes,
          fontsize=10, fontweight='bold', va='bottom')

# ── Panel (b): Similarity Distribution (box-style comparison) ────────────────
# Visualize neg_sim ranges with pos_sim reference lines
# Use a grouped layout: for each strategy, show Qwen and StarCoder neg_sim as
# boxes (mean ± std) with pos_sim as a marker

encoders = ['Qwen2.5-Coder-3B', 'StarCoder2-3B']
colors = [c_qwen, c_star]
labels_enc = ['Qwen2.5-Coder-3B', 'StarCoder2-3B']

group_positions = np.arange(len(strategies))
offsets = [-0.18, 0.18]
box_w = 0.28

for ei, (enc, col) in enumerate(zip(encoders, colors)):
    for si, strat in enumerate(strategies):
        pos = group_positions[si] + offsets[ei]
        neg_mean = data[enc]['neg_sim'][si]
        neg_std = data[enc]['margin_std'][si]
        pos_sim = data[enc]['pos_sim'][si]

        # Neg similarity range box (mean ± 0.5*std to show typical spread)
        box_lo = neg_mean - 0.5 * neg_std
        box_hi = neg_mean + 0.5 * neg_std
        whisker_lo = neg_mean - neg_std
        whisker_hi = min(neg_mean + neg_std, 1.0)

        # Box
        ax_b.bar(pos, box_hi - box_lo, box_w, bottom=box_lo,
                 color=col, alpha=0.35, edgecolor=col, linewidth=0.6, zorder=3)
        # Median line (neg_sim mean)
        ax_b.hlines(neg_mean, pos - box_w/2, pos + box_w/2,
                     colors=col, linewidth=1.2, zorder=4)
        # Whiskers
        ax_b.vlines(pos, whisker_lo, box_lo, colors=col, linewidth=0.6, zorder=3)
        ax_b.vlines(pos, box_hi, whisker_hi, colors=col, linewidth=0.6, zorder=3)
        ax_b.hlines(whisker_lo, pos - box_w/4, pos + box_w/4,
                     colors=col, linewidth=0.6, zorder=3)
        ax_b.hlines(whisker_hi, pos - box_w/4, pos + box_w/4,
                     colors=col, linewidth=0.6, zorder=3)

        # Pos_sim reference marker
        ax_b.plot(pos, pos_sim, marker='D', markersize=3.5, color=col,
                  markeredgecolor='white', markeredgewidth=0.4, zorder=5)

# Ceiling effect annotation
ax_b.annotate('ceiling\neffect', xy=(-0.18, 0.97), fontsize=6, color=c_qwen,
              ha='center', va='bottom', fontstyle='italic',
              arrowprops=dict(arrowstyle='->', color=c_qwen, lw=0.6),
              xytext=(-0.45, 1.04))

# Add a shaded region for Qwen saturation zone
ax_b.axhspan(0.90, 1.02, color=c_qwen, alpha=0.04, zorder=1)
ax_b.text(2.65, 0.955, 'Qwen\nsaturation\nzone', fontsize=5.5, color=c_qwen,
          alpha=0.7, ha='left', va='center', fontstyle='italic')

ax_b.set_ylabel('Cosine similarity')
ax_b.set_xticks(group_positions)
ax_b.set_xticklabels(strategies)
ax_b.set_ylim(0.45, 1.08)
ax_b.yaxis.set_major_locator(mticker.MultipleLocator(0.1))
ax_b.set_axisbelow(True)
ax_b.yaxis.grid(True, linewidth=0.3, alpha=0.5)

# Custom legend for panel (b)
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=c_qwen, alpha=0.35, edgecolor=c_qwen, label='Qwen neg sim'),
    Patch(facecolor=c_star, alpha=0.35, edgecolor=c_star, label='StarCoder neg sim'),
    Line2D([0], [0], marker='D', color='w', markerfacecolor='gray',
           markersize=4, label='pos sim (ref)'),
]
ax_b.legend(handles=legend_elements, loc='lower left', frameon=True,
            fancybox=False, edgecolor='#cccccc', framealpha=0.95)
ax_b.text(-0.12, 1.04, '(b)', transform=ax_b.transAxes,
          fontsize=10, fontweight='bold', va='bottom')

# ── Save ──────────────────────────────────────────────────────────────────────
out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig4_rep_geometry.pdf', format='pdf')
fig.savefig(out_dir / 'fig4_rep_geometry.png', format='png', dpi=300)
plt.close(fig)
print(f"Saved to {out_dir / 'fig4_rep_geometry.pdf'}")
print(f"Saved to {out_dir / 'fig4_rep_geometry.png'}")
