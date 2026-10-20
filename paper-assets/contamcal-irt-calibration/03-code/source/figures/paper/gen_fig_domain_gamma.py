"""Figure 6: Per-domain gamma forest plot with pooled estimate."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paper_style import *

apply_style()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# ── Data: J=13 Qwen2.5 (8x1.5B + 5x3B) ─────────────────────────────
domains = ['STEM: Math', 'STEM: Science', 'STEM: CS/Eng',
           'Business/Law', 'Medical', 'Humanities', 'Social Sci.']
gamma_mean = [0.499, 0.504, 0.497, 0.044, 0.235, -0.309, -0.571]
ci_lower   = [-0.213, -0.189, -0.425, -0.497, -0.421, -0.852, -1.054]
ci_upper   = [1.203, 1.202, 1.397, 0.579, 0.879, 0.257, -0.103]
ppp        = [0.206, 0.149, 0.392, 0.299, 0.124, 0.530, 0.570]

significant = [False, False, False, False, False, False, True]

# Pooled J=13
pooled_gamma = 0.107
pooled_ci = [-0.401, 0.625]

# ── Figure ───────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=figsize_column(aspect=0.62))

y_positions = np.arange(len(domains))[::-1]

# Background: STEM vs non-STEM
ax.axhspan(3.5, 7.5, color=COLORS['zone_benefit'],
           alpha=ALPHA['zone'], zorder=0)
ax.axhspan(-0.5, 3.5, color=COLORS['zone_harm'],
           alpha=ALPHA['zone'], zorder=0)

# Zero reference line
zero_line(ax, direction='v')

# Domain-level estimates
for i, (y, gm, cl, cu, sig) in enumerate(
        zip(y_positions, gamma_mean, ci_lower, ci_upper, significant)):
    if sig:
        col = COLORS['positive_gamma'] if gm > 0 else COLORS['negative_gamma']
    else:
        col = COLORS['nonsignificant']

    ax.hlines(y, cl, cu, color=col,
              linewidth=FOREST['ci_linewidth'], zorder=2)

    if sig:
        ax.plot(gm, y, 'o', color=col,
                markersize=FOREST['marker_size'], zorder=3,
                markeredgecolor=FOREST['marker_edgecolor'],
                markeredgewidth=FOREST['marker_edgewidth'])
    else:
        ax.plot(gm, y, 'o', color='white',
                markersize=FOREST['marker_size'], zorder=3,
                markeredgecolor=col, markeredgewidth=2.0)

    ppp_text = f"PPP={ppp[i]:.2f}"
    ax.text(1.55, y, ppp_text, va='center', ha='left',
            fontsize=LABEL['annotation_fontsize'],
            color=col, fontweight='medium')

# Pooled bar — diamond marker, gray
pooled_y = -1.3
ax.hlines(pooled_y, pooled_ci[0], pooled_ci[1],
          color=COLORS['pooled'], linewidth=2.0, linestyle='-', zorder=2)
ax.plot(pooled_gamma, pooled_y, 'D', color=COLORS['pooled'],
        markersize=8, zorder=3,
        markeredgecolor=FOREST['marker_edgecolor'],
        markeredgewidth=FOREST['marker_edgewidth'])

# Separator
ax.axhline(y=-0.5, color=FOREST['separator_color'],
           linewidth=FOREST['separator_linewidth'], linestyle='-')

# Y-axis
ax.set_yticks(list(y_positions) + [pooled_y])
ax.set_yticklabels(domains + ['Pooled MMLU'], fontsize=10.5)
ytick_labels = ax.get_yticklabels()
ytick_labels[-1].set_fontstyle('italic')
ytick_labels[-1].set_color(COLORS['pooled'])

# Group labels
ax.text(-1.05, 6.85, 'STEM',
        fontsize=LABEL['section_fontsize'],
        color=COLORS['positive_gamma'],
        fontweight=LABEL['section_fontweight'],
        va='top', ha='left', alpha=LABEL['section_alpha'])
ax.text(-1.05, 2.15, 'Non-STEM',
        fontsize=LABEL['section_fontsize'],
        color=COLORS['negative_gamma'],
        fontweight=LABEL['section_fontweight'],
        va='bottom', ha='left', alpha=LABEL['section_alpha'])

# Pooled annotation
ax.text(pooled_ci[1] + 0.12, pooled_y, 'n.s. — dilution masking',
        va='center', ha='left', fontsize=8.5,
        color=COLORS['pooled'], fontstyle='italic')

ax.set_xlabel(r'Contamination effect ($\gamma$)')
ax.set_xlim(-1.2, 1.8)
ax.set_ylim(-2.0, 7.2)

# Legend
legend_elements = [
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor=COLORS['negative_gamma'], markersize=9,
           markeredgecolor='white', markeredgewidth=0.5,
           label='CI excludes zero'),
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor=COLORS['nonsignificant'], markersize=9,
           markeredgecolor='white', markeredgewidth=0.5,
           label='Non-significant'),
]
ax.legend(handles=legend_elements, loc='upper center', framealpha=0.92,
          edgecolor='#DDDDDD', bbox_to_anchor=(0.45, 1.08), ncol=2,
          columnspacing=1.0, handletextpad=0.3)

ax.xaxis.grid(True)
plt.tight_layout()

# ── Save ─────────────────────────────────────────────────────────────
out_dir = Path(__file__).parent
paper_dir = Path(__file__).resolve().parent.parent.parent / 'docs' / 'paper' / 'figures'
for d in [out_dir, paper_dir]:
    fig.savefig(d / 'fig_domain_gamma.pdf', format='pdf')
    fig.savefig(d / 'fig_domain_gamma.png', format='png')
plt.close()
print("Saved fig_domain_gamma.pdf/png")
