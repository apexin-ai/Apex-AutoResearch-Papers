#!/usr/bin/env python3
"""Fig 3 combined: CAR inflation scatter (left) + oracle bar chart (right).

Single figure with two subplots — eliminates height alignment issues in LaTeX.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np
from pathlib import Path

OUT = Path('./output/fig3_scatter_and_oracle')

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.7,
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))

# ============================================================
# LEFT: CAR inflation scatter
# ============================================================
left_cluster = [
    ('(a)', 0, 91.5, 'blue', 'o'),
    ('(b)', 0.5, 83, 'blue', 'o'),
    ('(c)', 0, 82, 'blue', 'o'),
    ('(d)', 0, 76.9, 'purple', 'D'),
    ('(e)', 0, 75, 'purple', 'D'),
    ('(f)', 0, 74.5, 'blue', 'o'),
    ('(g)', 0, 73.1, 'purple', 'D'),
]

pi05_cluster = [
    ('Pi0.5 s0', 73, 28, 'green', 's'),
    ('Pi0.5 s1', 76, 25, 'green', 's'),
    ('Pi0.5 s2', 75, 27.5, 'green', 's'),
]

pi05_a1 = [
    ('λ=0.005', 47, 58, 'orange', '*'),
    ('λ=0.01', 49, 56.5, 'orange', '*'),
]

ax1.fill_between([0, 5], 60, 100, alpha=0.12, color='gray', zorder=0)
ax1.text(10, 97, 'Action-Collapsed\nSafety Zone', ha='left', va='top', fontsize=7,
         color='gray', style='italic')

for label, x, y, color, marker in left_cluster:
    ax1.scatter(x, y, c=color, marker=marker, s=50, zorder=5, edgecolors='black', linewidths=0.3)

label_positions = [
    (7, 92),    # (a) y=91.5
    (7, 86),    # (b) y=83
    (7, 82),    # (c) y=82
    (7, 78),    # (d) y=76.9
    (7, 74.5),  # (e) y=75
    (7, 71),    # (f) y=74.5
    (7, 67.5),  # (g) y=73.1
]
arrow_cfg = dict(arrowstyle='-', lw=0.4, color='#888888', shrinkA=0, shrinkB=2)
for (label, x, y, color, marker), (lx, ly) in zip(left_cluster, label_positions):
    needs_arrow = abs(ly - y) > 2.5
    ax1.annotate(label, (x, y), xytext=(lx, ly),
                 fontsize=7, ha='left', va='center', color='black',
                 arrowprops=arrow_cfg if needs_arrow else None)

for label, x, y, color, marker in pi05_cluster:
    ax1.scatter(x, y, c=color, marker=marker, s=60, zorder=5, edgecolors='black', linewidths=0.3)

cx = np.mean([p[1] for p in pi05_cluster])
cy = np.mean([p[2] for p in pi05_cluster])
ax1.annotate('Pi0.5\nbaseline', (cx, cy), xytext=(cx + 5, cy - 6),
             fontsize=7.5, ha='left', va='top',
             arrowprops=dict(arrowstyle='->', lw=0.7, color='gray'),
             color='black')

for label, x, y, color, marker in pi05_a1:
    ax1.scatter(x, y, c=color, marker=marker, s=100, zorder=5, edgecolors='black', linewidths=0.3)

mid_x = np.mean([p[1] for p in pi05_a1])
mid_y = np.mean([p[2] for p in pi05_a1])
ax1.annotate('Pi0.5+A1\n(SDF aux)', (mid_x, mid_y), xytext=(mid_x + 8, mid_y + 8),
             fontsize=7.5, ha='left', va='bottom',
             arrowprops=dict(arrowstyle='->', lw=0.7, color='gray'),
             color='black')

arrow = FancyArrowPatch((cx, cy), (mid_x - 2, mid_y - 2),
                        arrowstyle='->', mutation_scale=12,
                        lw=1.5, color='darkorange', zorder=4)
ax1.add_patch(arrow)
ax1.text((cx + mid_x) / 2 - 3, (cy + mid_y) / 2 + 3, 'SDF training\neffect',
         fontsize=7, ha='center', va='bottom', color='darkorange', style='italic')

legend_text = (
    "(a) A1-LoRA (91.5%)\n"
    "(b) Full-FT baseline (83%)\n"
    "(c) LoRA baseline (82%)\n"
    "(d) Oracle-feature (76.9%)\n"
    "(e) Oracle-adaptive (75%)\n"
    "(f) A3 (74.5%)\n"
    "(g) Oracle-fixed (73.1%)"
)
props = dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='gray', alpha=0.9)
ax1.text(0.02, 0.02, legend_text, transform=ax1.transAxes, fontsize=6,
         verticalalignment='bottom', horizontalalignment='left',
         bbox=props, family='monospace')

legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=7,
               markeredgecolor='black', markeredgewidth=0.3, label='Pi0-family'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='purple', markersize=7,
               markeredgecolor='black', markeredgewidth=0.3, label='Oracle variants'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='green', markersize=7,
               markeredgecolor='black', markeredgewidth=0.3, label='Pi0.5 baseline'),
    plt.Line2D([0], [0], marker='*', color='w', markerfacecolor='orange', markersize=9,
               markeredgecolor='black', markeredgewidth=0.3, label='Pi0.5+A1 (SDF aux)'),
]
ax1.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

ax1.set_xlabel('Task Success Rate (%)', fontsize=10)
ax1.set_ylabel('Collision Avoidance Rate (%)', fontsize=10)
ax1.set_xlim(-5, 100)
ax1.set_ylim(15, 100)

# ============================================================
# RIGHT: oracle bar chart
# ============================================================
methods = [
    'Oracle-fixed\n(GT SDF)',
    'A3 no-refine\n(learned SDF)',
    'Oracle-adaptive\n(GT SDF)',
    'Oracle-feature\n(GT SDF)',
    'LoRA baseline',
    'Full-FT baseline',
]
cars = [73.1, 74.5, 75.0, 76.9, 82.0, 83.0]

colors_bar = [
    '#A78BFA',
    '#3274A1',
    '#8B5CF6',
    '#7C3AED',
    '#9CA3AF',
    '#6B7280',
]

y_pos = np.arange(len(methods))
bars = ax2.barh(y_pos, cars, height=0.55, color=colors_bar, edgecolor='white', linewidth=0.5)

for bar, val in zip(bars, cars):
    ax2.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2,
             f'{val:.1f}%', va='center', ha='left', fontsize=9, color='#333333')

baseline_avg = (82.0 + 83.0) / 2
ax2.axvline(x=baseline_avg, color='#6B7280', linestyle='--', linewidth=0.9, alpha=0.7, zorder=3)
ax2.text(baseline_avg + 0.5, len(methods) - 0.3, 'No Refinement\navg', fontsize=7,
         color='#6B7280', va='bottom', ha='left', style='italic')

ax2.set_yticks(y_pos)
ax2.set_yticklabels(methods, fontsize=9)
ax2.set_xlabel('Collision Avoidance Rate (%)', fontsize=10)
ax2.set_xlim(65, 92)
ax2.tick_params(axis='x', labelsize=9)
ax2.invert_yaxis()

# ============================================================
# Save
# ============================================================
plt.tight_layout()
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT.with_suffix('.pdf'), dpi=300)
fig.savefig(OUT.with_suffix('.png'), dpi=300)
plt.close(fig)
print(f'Saved: {OUT.with_suffix(".pdf")} and {OUT.with_suffix(".png")}')
