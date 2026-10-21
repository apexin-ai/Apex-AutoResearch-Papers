"""Generate Figure 1: Experimental Pipeline Overview for policy_ambiguity_safety paper."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# ---------- color palette ----------
WARM_DARK = '#C44E52'      # spec-layer primary (vermillion-ish)
WARM_LIGHT = '#FADBD8'     # spec-layer fill
WARM_MID = '#E6998A'        # spec-layer secondary
COOL_DARK = '#4C72B0'      # ling-layer primary
COOL_LIGHT = '#D6E4F0'     # ling-layer fill
COOL_MID = '#8FAED0'        # ling-layer secondary
NEUTRAL_DARK = '#2D2D2D'   # text
NEUTRAL_MID = '#555555'    # secondary text
NEUTRAL_LIGHT = '#F7F7F7'  # panel bg
ACCENT_GREEN = '#3A7D44'   # evaluation / findings
ACCENT_GREEN_LIGHT = '#DFF0D8'
BORDER_GRAY = '#CCCCCC'
ARROW_GRAY = '#888888'
WHITE = '#FFFFFF'

fig = plt.figure(figsize=(16, 7), dpi=300, facecolor=WHITE)

# Panel x-boundaries (in figure coords)
LEFT_X = (0.02, 0.32)
MID_X = (0.345, 0.67)
RIGHT_X = (0.695, 0.98)

def draw_panel_bg(ax_coords, title, title_color=NEUTRAL_DARK):
    """Draw a light background panel with title."""
    x0, y0, w, h = ax_coords
    ax = fig.add_axes([x0, y0, w, h])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('auto')
    ax.axis('off')

    bg = FancyBboxPatch((0.01, 0.01), 0.98, 0.98,
                         boxstyle="round,pad=0.015",
                         facecolor=NEUTRAL_LIGHT, edgecolor=BORDER_GRAY,
                         linewidth=1.0, zorder=0)
    ax.add_patch(bg)
    ax.text(0.5, 0.96, title, ha='center', va='top',
            fontsize=11, fontweight='bold', color=title_color, zorder=5)
    return ax


def rounded_box(ax, xy, w, h, text, fc, ec, fontsize=8, text_color=NEUTRAL_DARK,
                fontweight='normal', alpha=1.0, lw=1.2, zorder=3, text_lines=None):
    """Draw a rounded rectangle with centered text."""
    box = FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.012",
                          facecolor=fc, edgecolor=ec, linewidth=lw,
                          alpha=alpha, zorder=zorder)
    ax.add_patch(box)
    cx = xy[0] + w / 2
    cy = xy[1] + h / 2
    if text_lines:
        n = len(text_lines)
        line_h = 0.035
        start_y = cy + (n - 1) * line_h / 2
        for i, (line, fs, fw, tc) in enumerate(text_lines):
            ax.text(cx, start_y - i * line_h, line, ha='center', va='center',
                    fontsize=fs, fontweight=fw, color=tc, zorder=zorder + 1)
    else:
        ax.text(cx, cy, text, ha='center', va='center',
                fontsize=fontsize, fontweight=fontweight, color=text_color,
                zorder=zorder + 1, wrap=True)
    return box


def arrow(ax, xy_start, xy_end, color=ARROW_GRAY, lw=1.5, style='->', connectionstyle='arc3,rad=0'):
    """Draw an arrow between two points."""
    arr = FancyArrowPatch(xy_start, xy_end,
                           arrowstyle=style, color=color,
                           linewidth=lw, mutation_scale=12,
                           connectionstyle=connectionstyle,
                           zorder=4)
    ax.add_patch(arr)
    return arr


# ============================================================
# PANEL 1: Ambiguity Taxonomy (left)
# ============================================================
ax1 = draw_panel_bg((0.02, 0.04, 0.30, 0.92), 'Policy Ambiguity Taxonomy')

# root node
rounded_box(ax1, (0.28, 0.82), 0.44, 0.07, 'Ambiguity', fc=WHITE, ec=NEUTRAL_MID,
            fontsize=9, fontweight='bold')

# Specification Layer group
rounded_box(ax1, (0.04, 0.54), 0.42, 0.08, 'Specification Layer',
            fc=WARM_LIGHT, ec=WARM_DARK, fontsize=9, fontweight='bold', text_color=WARM_DARK)

spec_types = ['Authorization\nScope', 'Incompleteness', 'Conditional\nPrecedence']
spec_x = [0.06, 0.20, 0.34]
for i, (label, sx) in enumerate(zip(spec_types, spec_x)):
    rounded_box(ax1, (sx, 0.37), 0.14, 0.12, label,
                fc=WARM_LIGHT, ec=WARM_DARK, fontsize=7.0, text_color=WARM_DARK, lw=1.0)
    arrow(ax1, (sx + 0.07, 0.54), (sx + 0.07, 0.49), color=WARM_DARK, lw=1.0)

# Linguistic Layer group
rounded_box(ax1, (0.54, 0.54), 0.42, 0.08, 'Linguistic Layer',
            fc=COOL_LIGHT, ec=COOL_DARK, fontsize=9, fontweight='bold', text_color=COOL_DARK)

ling_types = ['Scopal', 'Lexical', 'Coreferential']
ling_x = [0.56, 0.70, 0.84]
for i, (label, lx) in enumerate(zip(ling_types, ling_x)):
    rounded_box(ax1, (lx, 0.37), 0.14, 0.12, label,
                fc=COOL_LIGHT, ec=COOL_DARK, fontsize=7.5, text_color=COOL_DARK, lw=1.0)
    arrow(ax1, (lx + 0.07, 0.54), (lx + 0.07, 0.49), color=COOL_DARK, lw=1.0)

# Connect root to layer groups
arrow(ax1, (0.40, 0.82), (0.25, 0.62), color=WARM_DARK, lw=1.2, connectionstyle='arc3,rad=0.1')
arrow(ax1, (0.60, 0.82), (0.75, 0.62), color=COOL_DARK, lw=1.2, connectionstyle='arc3,rad=-0.1')

# Layer labels at bottom
ax1.text(0.25, 0.30, '(Spec)', ha='center', va='top', fontsize=7, fontstyle='italic', color=WARM_DARK)
ax1.text(0.75, 0.30, '(Ling)', ha='center', va='top', fontsize=7, fontstyle='italic', color=COOL_DARK)

# Summary counts
ax1.text(0.50, 0.20, '2 layers  ×  3 types  =  6 ambiguity categories',
         ha='center', va='center', fontsize=7.5, color=NEUTRAL_MID, fontstyle='italic')

# Color legend
legend_y = 0.10
rounded_box(ax1, (0.08, legend_y - 0.01), 0.08, 0.05, '', fc=WARM_LIGHT, ec=WARM_DARK, lw=0.8)
ax1.text(0.20, legend_y + 0.015, 'Specification', ha='left', va='center', fontsize=7, color=WARM_DARK)
rounded_box(ax1, (0.52, legend_y - 0.01), 0.08, 0.05, '', fc=COOL_LIGHT, ec=COOL_DARK, lw=0.8)
ax1.text(0.64, legend_y + 0.015, 'Linguistic', ha='left', va='center', fontsize=7, color=COOL_DARK)


# ============================================================
# PANEL 2: Matched-Pair Experimental Design (center)
# ============================================================
ax2 = draw_panel_bg((0.345, 0.04, 0.325, 0.92), 'Matched-Pair Experimental Design')

# Policy clause origin
rounded_box(ax2, (0.30, 0.82), 0.40, 0.07, 'Policy Clause', fc=WHITE, ec=NEUTRAL_MID,
            fontsize=9, fontweight='bold')

# Fork: ambiguous vs unambiguous
# Ambiguous branch (top)
rounded_box(ax2, (0.05, 0.63), 0.40, 0.09, '', fc='#FFF5F5', ec=WARM_DARK, lw=1.2)
ax2.text(0.25, 0.695, 'Ambiguous Variant', ha='center', va='center',
         fontsize=8, fontweight='bold', color=WARM_DARK, zorder=5)

# Unambiguous branch (bottom)
rounded_box(ax2, (0.55, 0.63), 0.40, 0.09, '', fc='#F0F5FF', ec=COOL_DARK, lw=1.2)
ax2.text(0.75, 0.695, 'Unambiguous Variant', ha='center', va='center',
         fontsize=8, fontweight='bold', color=COOL_DARK, zorder=5)

# Fork arrows
arrow(ax2, (0.40, 0.82), (0.25, 0.72), color=WARM_DARK, lw=1.5, connectionstyle='arc3,rad=0.15')
arrow(ax2, (0.60, 0.82), (0.75, 0.72), color=COOL_DARK, lw=1.5, connectionstyle='arc3,rad=-0.15')

# Mini-example boxes
ex_y = 0.48
rounded_box(ax2, (0.02, ex_y), 0.46, 0.10, '', fc='#FFF9F5', ec='#DDD', lw=0.8)
ax2.text(0.25, ex_y + 0.075, '"Items may be returned\nwithin 30 days"', ha='center', va='center',
         fontsize=6.5, fontstyle='italic', color=WARM_DARK, zorder=5)
ax2.text(0.25, ex_y + 0.015, 'scopal: "items" → all categories?', ha='center', va='center',
         fontsize=5.8, color=NEUTRAL_MID, zorder=5)

rounded_box(ax2, (0.52, ex_y), 0.46, 0.10, '', fc='#F5F8FF', ec='#DDD', lw=0.8)
ax2.text(0.75, ex_y + 0.075, '"Standard items may be\nreturned within 30 days"', ha='center', va='center',
         fontsize=6.5, fontstyle='italic', color=COOL_DARK, zorder=5)
ax2.text(0.75, ex_y + 0.015, 'explicit: excludes custom items', ha='center', va='center',
         fontsize=5.8, color=NEUTRAL_MID, zorder=5)

# Downward arrows to agent box
arrow(ax2, (0.25, ex_y), (0.35, 0.38), color=ARROW_GRAY, lw=1.2, connectionstyle='arc3,rad=0.1')
arrow(ax2, (0.75, ex_y), (0.65, 0.38), color=ARROW_GRAY, lw=1.2, connectionstyle='arc3,rad=-0.1')

# τ²-bench agent box
rounded_box(ax2, (0.22, 0.26), 0.56, 0.12, '', fc='#F0F0F0', ec=NEUTRAL_MID, lw=1.2)
ax2.text(0.50, 0.345, 'τ²-bench Agent Environment', ha='center', va='center',
         fontsize=8.5, fontweight='bold', color=NEUTRAL_DARK, zorder=5)
ax2.text(0.50, 0.29, 'Agent executes customer-service dialogues', ha='center', va='center',
         fontsize=6.5, color=NEUTRAL_MID, zorder=5)

# Scale annotation
ax2.text(0.50, 0.17, '300 clause pairs × 2 models × 2 conditions',
         ha='center', va='center', fontsize=7.5, fontweight='bold', color=NEUTRAL_DARK)
ax2.text(0.50, 0.12, '= 1,200 episodes', ha='center', va='center',
         fontsize=8, fontweight='bold', color=ACCENT_GREEN)

# Down arrow to panel 3
arrow(ax2, (0.50, 0.26), (0.50, 0.06), color=ARROW_GRAY, lw=1.5, style='->')


# ============================================================
# PANEL 3: Evaluation & Analysis (right)
# ============================================================
ax3 = draw_panel_bg((0.695, 0.04, 0.285, 0.92), 'Evaluation & Analysis')

# Cross-judge evaluation
rounded_box(ax3, (0.10, 0.76), 0.80, 0.12, '', fc='#F5F5F5', ec=NEUTRAL_MID, lw=1.2)
ax3.text(0.50, 0.845, 'Cross-Judge Evaluation', ha='center', va='center',
         fontsize=8.5, fontweight='bold', color=NEUTRAL_DARK, zorder=5)
ax3.text(0.50, 0.79, 'Model A judges B,  Model B judges A', ha='center', va='center',
         fontsize=6.5, color=NEUTRAL_MID, zorder=5)

arrow(ax3, (0.50, 0.76), (0.50, 0.70), color=ARROW_GRAY, lw=1.2)

# 3-tier severity
rounded_box(ax3, (0.10, 0.50), 0.80, 0.20, '', fc='#FFF', ec=NEUTRAL_MID, lw=1.2)
ax3.text(0.50, 0.68, '4-Tier Violation Severity', ha='center', va='center',
         fontsize=8.5, fontweight='bold', color=NEUTRAL_DARK, zorder=5)

tiers = [
    ('None', '#E8F5E9', '#2E7D32'),
    ('Minor', '#FFF3CD', '#856404'),
    ('Moderate', '#FFE0CC', '#C45000'),
    ('Critical', '#F8D7DA', '#842029'),
]
for (label, fc, tc), ty in zip(tiers, [0.64, 0.60, 0.56, 0.52]):
    rounded_box(ax3, (0.15, ty - 0.01), 0.70, 0.032, label,
                fc=fc, ec=tc, fontsize=6.5, text_color=tc, lw=0.8)

arrow(ax3, (0.50, 0.50), (0.50, 0.46), color=ARROW_GRAY, lw=1.2)

# Key findings box
rounded_box(ax3, (0.06, 0.15), 0.88, 0.30, '', fc=ACCENT_GREEN_LIGHT, ec=ACCENT_GREEN, lw=1.5)
ax3.text(0.50, 0.42, 'Key Findings', ha='center', va='center',
         fontsize=9, fontweight='bold', color=ACCENT_GREEN, zorder=5)

findings = [
    ('+36.5 pp', 'violation rate increase\nunder ambiguous policies', WARM_DARK),
    ('~2×', 'Spec-layer impact vs.\nLinguistic-layer', COOL_DARK),
]

fx_positions = [0.28, 0.72]
for (num, desc, color), fx in zip(findings, fx_positions):
    ax3.text(fx, 0.33, num, ha='center', va='center',
             fontsize=14, fontweight='bold', color=color, zorder=5)
    ax3.text(fx, 0.23, desc, ha='center', va='center',
             fontsize=6.2, color=NEUTRAL_MID, zorder=5, linespacing=1.3)

# Divider between findings
ax3.plot([0.50, 0.50], [0.20, 0.40], color=BORDER_GRAY, linewidth=0.8, zorder=4)


# ============================================================
# Inter-panel flow arrows
# ============================================================
# Arrow from Panel 1 to Panel 2
arr12 = fig.patches
fig_arrow1 = FancyArrowPatch(
    (0.325, 0.50), (0.35, 0.50),
    arrowstyle='->', color=ARROW_GRAY, linewidth=2.0,
    mutation_scale=15, transform=fig.transFigure, zorder=10
)
fig.patches.append(fig_arrow1)

# Arrow from Panel 2 to Panel 3
fig_arrow2 = FancyArrowPatch(
    (0.675, 0.50), (0.70, 0.50),
    arrowstyle='->', color=ARROW_GRAY, linewidth=2.0,
    mutation_scale=15, transform=fig.transFigure, zorder=10
)
fig.patches.append(fig_arrow2)

# ============================================================
# Save
# ============================================================
out_dir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/figures/paper'

plt.savefig(f'{out_dir}/fig1_overview.pdf', format='pdf', dpi=300,
            bbox_inches='tight', pad_inches=0.05, facecolor=WHITE)
plt.savefig(f'{out_dir}/fig1_overview.png', format='png', dpi=300,
            bbox_inches='tight', pad_inches=0.05, facecolor=WHITE)
plt.close()

import os
pdf_size = os.path.getsize(f'{out_dir}/fig1_overview.pdf')
png_size = os.path.getsize(f'{out_dir}/fig1_overview.png')
print(f'PDF: {pdf_size:,} bytes')
print(f'PNG: {png_size:,} bytes')
print('Done.')
