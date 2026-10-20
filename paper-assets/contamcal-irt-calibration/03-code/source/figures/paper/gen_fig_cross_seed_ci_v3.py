#!/usr/bin/env python3
"""Figure 5: Cross-seed CI forest plot — unified paper style."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paper_style import *

apply_style()

import matplotlib.pyplot as plt
import numpy as np

# ── Data ─────────────────────────────────────────────────────────────
families = [
    ('Qwen2.5-14B',  'Collapse',   -15.7,  -24.99, -10.49, True),
    ('Qwen2.5-7B',   'V-recovery', -1.1,   -1.82,  -0.34,  True),
    ('Phi-4 14.7B',  'Immune',     +0.73,  -0.17,  +1.39,  False),
    ('OLMo-2 7B',    'Benefit',    +1.0,   -0.55,  +2.60,  False),
    ('Gemma-2 9B',   'Benefit',    +2.4,   +1.49,  +3.14,  True),
    ('Falcon3-7B',   'Benefit',    +4.1,   +3.91,  +4.19,  True),
]

# ── Figure ───────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=figsize_column(aspect=0.54))

n = len(families)
y_positions = np.arange(n)[::-1]

x_left = -27
x_right = 5.5

# Background sections
ax.axhspan(3.5, 6.1, color=COLORS['zone_harm'],
           alpha=ALPHA['zone'], zorder=0)
ax.axhspan(-0.7, 2.5, color=COLORS['zone_benefit'],
           alpha=ALPHA['zone'], zorder=0)

# Separator lines
ax.axhline(y=3.5, color=FOREST['separator_color'],
           linewidth=FOREST['separator_linewidth'], linestyle='-', zorder=1)
ax.axhline(y=2.5, color=FOREST['separator_color'],
           linewidth=FOREST['separator_linewidth'], linestyle='-', zorder=1)

# Zero reference line
zero_line(ax, direction='v')

# CI bars + markers
for i, (name, pattern, mean, ci_lo, ci_hi, sig) in enumerate(families):
    y = y_positions[i]
    col = get_pattern_color(pattern)

    ax.hlines(y, ci_lo, ci_hi, color=col,
              linewidth=FOREST['ci_linewidth'], zorder=2, capstyle='butt')

    ci_width = ci_hi - ci_lo
    cap_h = FOREST['cap_height'] if ci_width > 2.0 else FOREST['cap_height'] * 0.67
    ax.vlines(ci_lo, y - cap_h, y + cap_h, color=col,
              linewidth=FOREST['cap_linewidth'], zorder=2)
    ax.vlines(ci_hi, y - cap_h, y + cap_h, color=col,
              linewidth=FOREST['cap_linewidth'], zorder=2)

    if sig:
        ax.plot(mean, y, 'o', color=col,
                markersize=FOREST['marker_size'], zorder=3,
                markeredgecolor=FOREST['marker_edgecolor'],
                markeredgewidth=FOREST['marker_edgewidth'])
    else:
        ax.plot(mean, y, 'o', color='white',
                markersize=FOREST['marker_size'], zorder=3,
                markeredgecolor=col, markeredgewidth=2.0)

    sign_char = '+' if mean > 0 else ''
    label = f"{sign_char}{mean:.1f} pp"
    ax.annotate(label, xy=(1.03, y), xycoords=('axes fraction', 'data'),
                va='center', ha='left', fontsize=9, color=col,
                fontweight='medium', annotation_clip=False)

# Falcon3 n=2 sub-annotation
falcon_y = y_positions[5]
ax.annotate('n = 2', xy=(1.03, falcon_y - 0.40),
            xycoords=('axes fraction', 'data'),
            va='center', ha='left',
            fontsize=LABEL['inline_fontsize'],
            color=COLORS['Benefit'], fontstyle='italic',
            alpha=0.55, annotation_clip=False)

# Section labels
label_x = x_left + 0.8
ax.text(label_x, 5.88, 'Harm',
        fontsize=LABEL['section_fontsize'],
        color=COLORS['Collapse'],
        fontweight=LABEL['section_fontweight'],
        va='top', ha='left', alpha=LABEL['section_alpha'])
ax.text(label_x, 2.38, 'Benefit',
        fontsize=LABEL['section_fontsize'],
        color=COLORS['Benefit'],
        fontweight=LABEL['section_fontweight'],
        va='top', ha='left', alpha=LABEL['section_alpha'])

ax.set_yticks(y_positions)
ax.set_yticklabels([f[0] for f in families], fontsize=10.5)

ax.set_xlabel(r'Cross-seed mean $\Delta$acc at $d_{100}$ (pp)')
ax.set_xlim(x_left, x_right)
ax.set_ylim(-0.7, 6.1)
ax.grid(False)
ax.set_xticks([-25, -20, -15, -10, -5, 0, 5])

plt.subplots_adjust(right=0.81, top=0.97, bottom=0.15, left=0.18)

# ── Save ─────────────────────────────────────────────────────────────
out_dir = Path(__file__).parent
paper_dir = Path(__file__).resolve().parent.parent.parent / 'docs' / 'paper' / 'figures'
for d in [out_dir, paper_dir]:
    fig.savefig(d / 'fig_cross_seed_ci.pdf', format='pdf')
    fig.savefig(d / 'fig_cross_seed_ci.png', format='png')
plt.close()
print("Saved fig_cross_seed_ci.pdf/png")
