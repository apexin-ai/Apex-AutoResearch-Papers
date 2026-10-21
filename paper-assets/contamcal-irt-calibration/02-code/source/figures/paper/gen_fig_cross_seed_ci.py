#!/usr/bin/env python3
"""Cross-seed CI forest plot: mean Δacc ± BCa 95% CI for each family."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3.5,
    'ytick.major.size': 3.5,
    'lines.linewidth': 1.8,
    'grid.alpha': 0.3,
    'grid.linewidth': 0.5,
    'grid.linestyle': '--',
})

# Unified palette matching Figure 3
PATTERN_COLORS = {
    'Benefit':    '#2e86ab',
    'Immune':     '#6c757d',
    'Collapse':   '#c0392b',
    'V-recovery': '#e67e22',
}

families = [
    ('Qwen2.5-14B',  'Collapse',   -15.7,  -24.99, -10.49, True),
    ('Qwen2.5-7B',   'V-recovery', -1.1,   -1.82,  -0.34,  True),
    ('Phi-4 14.7B',  'Immune',     +0.73,  -0.17,  +1.39,  False),
    ('OLMo-2 7B',    'Benefit',    +1.0,   -0.55,  +2.60,  False),
    ('Gemma-2 9B',   'Benefit',    +2.4,   +1.49,  +3.14,  True),
    ('Falcon3-7B',   'Benefit',    +4.1,   +3.91,  +4.19,  True),
]

fig, ax = plt.subplots(figsize=(6.5, 3))

xlim = (-27, 7)
ax.set_xlim(xlim)

y_positions = np.arange(len(families))[::-1]

# --- Background zones: Benefit (x>0) and Harm (x<0) ---
ax.axvspan(0, xlim[1], color='#2e86ab', alpha=0.04, zorder=0)
ax.axvspan(xlim[0], 0, color='#c0392b', alpha=0.04, zorder=0)

# Zone labels in corners
ax.text(xlim[1] - 0.3, y_positions[0] + 0.42, 'Benefit',
        ha='right', va='top', fontsize=7, color='#2e86ab', alpha=0.55,
        fontstyle='italic')
ax.text(xlim[0] + 0.3, y_positions[0] + 0.42, 'Harm',
        ha='left', va='top', fontsize=7, color='#c0392b', alpha=0.55,
        fontstyle='italic')

# --- Alternating row shading ---
for i, y in enumerate(y_positions):
    if i % 2 == 1:
        ax.axhspan(y - 0.5, y + 0.5, color='#888888', alpha=0.05, zorder=0)

# --- Zero reference line (more prominent: solid, dark gray) ---
ax.axvline(x=0, color='#333333', linestyle='-', linewidth=0.9, alpha=0.5, zorder=1)

# --- CI bars with caps ---
CAP_SIZE = 0.15  # half-height of cap tick in y-units

for i, (name, pattern, mean, ci_lo, ci_hi, excludes_zero) in enumerate(families):
    y = y_positions[i]
    color = PATTERN_COLORS[pattern]
    facecolor = color if excludes_zero else 'white'

    # CI line (thicker)
    ax.hlines(y, ci_lo, ci_hi, color=color, linewidth=2.5, zorder=2)

    # Cap lines at endpoints
    ax.vlines(ci_lo, y - CAP_SIZE, y + CAP_SIZE, color=color, linewidth=1.2, zorder=2)
    ax.vlines(ci_hi, y - CAP_SIZE, y + CAP_SIZE, color=color, linewidth=1.2, zorder=2)

    # Mean marker
    ax.plot(mean, y, 'o', color=facecolor, markersize=8, zorder=3,
            markeredgecolor=color, markeredgewidth=1.5)

    # Falcon3 annotation
    if name == 'Falcon3-7B':
        ax.text(ci_hi + 0.4, y, '$n$=2', va='center', ha='left',
                fontsize=7.5, color=color, fontstyle='italic')

ax.set_yticks(y_positions)
ax.set_yticklabels([f[0] for f in families], fontsize=9.5)
ax.set_xlabel(r'Cross-seed mean $\Delta$acc at d100 (pp)')
ax.xaxis.grid(True)

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#555',
           markeredgecolor='#555', markersize=8, markeredgewidth=1.5,
           label='CI excludes zero'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='white',
           markeredgecolor='#555', markersize=8, markeredgewidth=1.5,
           label='CI includes zero'),
]
ax.legend(handles=legend_elements, loc='lower left', frameon=True,
          fancybox=False, edgecolor='#cccccc', framealpha=1.0,
          handletextpad=0.4, borderpad=0.4, fontsize=8)

plt.tight_layout()

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig_cross_seed_ci.pdf')
fig.savefig(out_dir / 'fig_cross_seed_ci.png')
print(f"Saved: {out_dir / 'fig_cross_seed_ci.pdf'}")
print(f"Saved: {out_dir / 'fig_cross_seed_ci.png'}")
plt.close()
