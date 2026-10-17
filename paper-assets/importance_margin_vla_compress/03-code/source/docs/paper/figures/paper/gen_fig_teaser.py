import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

# Okabe-Ito semantic colors
C_SAFE = '#009E73'       # green
C_MILD = '#E69F00'       # orange/yellow
C_DANGER = '#D55E00'     # vermillion
C_SEVERE = '#CC3311'     # dark red
C_BLUE = '#0072B2'       # blue (Object suite)
C_RED = '#D55E00'        # vermillion (Goal suite)
C_GRAY = '#999999'

fig = plt.figure(figsize=(13, 5.0))
gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.32)

# ============================================================
# Panel (a): 2x2 Conceptual Grid
# ============================================================
ax_a = fig.add_subplot(gs[0])
ax_a.set_xlim(0, 1)
ax_a.set_ylim(0, 1)
ax_a.axis('off')

ax_a.text(-0.02, 1.06, '(a)', fontsize=14, fontweight='bold',
          transform=ax_a.transAxes, va='top', ha='left')

# Grid boundaries
x_mid, y_mid = 0.5, 0.5
pad = 0.02

# Background colors for quadrants (green->yellow->orange->red gradient)
quadrant_colors = {
    'TL': '#d4edda',  # Independent + Simple → mostly safe (light green)
    'TR': '#fff3cd',  # Independent + Complex → mild degradation (light yellow)
    'BL': '#f8d7da',  # Entangling + Simple → mixed (light pink)
    'BR': '#f5c6cb',  # Entangling + Complex → severe (pink)
}

quads = [
    ('TL', 0.0, y_mid, x_mid, 1.0),
    ('TR', x_mid, y_mid, 1.0, 1.0),
    ('BL', 0.0, 0.0, x_mid, y_mid),
    ('BR', x_mid, 0.0, 1.0, y_mid),
]

for qid, x0, y0, x1, y1 in quads:
    rect = FancyBboxPatch((x0 + pad, y0 + pad), x1 - x0 - 2*pad, y1 - y0 - 2*pad,
                           boxstyle="round,pad=0.01", facecolor=quadrant_colors[qid],
                           edgecolor='#aaaaaa', linewidth=0.8, zorder=0)
    ax_a.add_patch(rect)

# Axis labels
ax_a.text(0.5, -0.06, 'Task Complexity', fontsize=12, ha='center', va='top',
          fontweight='bold')
ax_a.annotate('', xy=(0.85, -0.02), xytext=(0.15, -0.02),
              arrowprops=dict(arrowstyle='->', color='#555555', lw=1.2))
ax_a.text(0.18, -0.02, 'Simple', fontsize=9, ha='left', va='bottom', color='#555555')
ax_a.text(0.82, -0.02, 'Complex', fontsize=9, ha='right', va='bottom', color='#555555')

ax_a.text(-0.07, 0.5, 'Token Coupling', fontsize=12, ha='center', va='center',
          fontweight='bold', rotation=90)
ax_a.annotate('', xy=(-0.03, 0.15), xytext=(-0.03, 0.85),
              arrowprops=dict(arrowstyle='->', color='#555555', lw=1.2))
ax_a.text(-0.03, 0.82, 'Independent', fontsize=9, ha='right', va='top',
          color='#555555', rotation=90)
ax_a.text(-0.03, 0.18, 'Entangling', fontsize=9, ha='right', va='bottom',
          color='#555555', rotation=90)

# Quadrant content
stroke = [pe.withStroke(linewidth=2.5, foreground='white')]

# TL: Independent + Simple
ax_a.text(0.25, 0.90, 'Object Suite', fontsize=10, ha='center', va='center',
          fontweight='bold', color='#333333')
# pi0.5
ax_a.text(0.25, 0.81, r'$\pi$0.5: 98.2% $\rightarrow$ 98.2%', fontsize=9,
          ha='center', va='center', color=C_SAFE)
ax_a.text(0.25, 0.73, '(0.0pp drop at k=0.9)', fontsize=8,
          ha='center', va='center', color=C_SAFE, fontstyle='italic')
# OpenVLA
ax_a.text(0.25, 0.63, 'OpenVLA: 74% $\\rightarrow$ 62%', fontsize=9,
          ha='center', va='center', color=C_MILD)
ax_a.text(0.25, 0.56, '(−12pp at k=0.9)', fontsize=8,
          ha='center', va='center', color=C_MILD, fontstyle='italic')

# TR: Independent + Complex
ax_a.text(0.75, 0.90, 'Goal Suite', fontsize=10, ha='center', va='center',
          fontweight='bold', color='#333333')
ax_a.text(0.75, 0.79, r'$\pi$0.5: 98.2% $\rightarrow$ −7.0pp', fontsize=9,
          ha='center', va='center', color=C_MILD)
ax_a.text(0.75, 0.71, '(at k=0.95)', fontsize=8,
          ha='center', va='center', color=C_MILD, fontstyle='italic')

# BL: Entangling + Simple
ax_a.text(0.25, 0.40, 'Object Suite', fontsize=10, ha='center', va='center',
          fontweight='bold', color='#333333')
# X-VLA
ax_a.text(0.25, 0.31, 'X-VLA: 99.2% $\\rightarrow$ 99.2%', fontsize=9,
          ha='center', va='center', color=C_SAFE)
ax_a.text(0.25, 0.24, '(0.0pp at k=0.9)', fontsize=8,
          ha='center', va='center', color=C_SAFE, fontstyle='italic')
# SmolVLA
ax_a.text(0.25, 0.14, 'SmolVLA: 59.2% $\\rightarrow$ 0%', fontsize=9,
          ha='center', va='center', color=C_SEVERE)
ax_a.text(0.25, 0.07, '(collapse at k=0.95)', fontsize=8,
          ha='center', va='center', color=C_SEVERE, fontstyle='italic')

# BR: Entangling + Complex
ax_a.text(0.75, 0.40, 'Goal Suite', fontsize=10, ha='center', va='center',
          fontweight='bold', color='#333333')
# X-VLA
ax_a.text(0.75, 0.31, 'X-VLA: 98% $\\rightarrow$ 70.2%', fontsize=9,
          ha='center', va='center', color=C_DANGER)
ax_a.text(0.75, 0.24, '(−27.8pp at k=0.9)', fontsize=8,
          ha='center', va='center', color=C_DANGER, fontstyle='italic',
          fontweight='bold')
# SmolVLA
ax_a.text(0.75, 0.14, 'SmolVLA: 0% at any k', fontsize=9,
          ha='center', va='center', color=C_SEVERE)
ax_a.text(0.75, 0.07, '(total collapse)', fontsize=8,
          ha='center', va='center', color=C_SEVERE, fontstyle='italic')

# Method note
ax_a.text(0.5, 1.04, 'L2-norm pruning', fontsize=9, ha='center', va='bottom',
          color='#777777', fontstyle='italic')

# Divider lines
ax_a.plot([x_mid, x_mid], [0.02, 0.98], color='#aaaaaa', linewidth=0.8,
          linestyle='--', zorder=1)
ax_a.plot([0.02, 0.98], [y_mid, y_mid], color='#aaaaaa', linewidth=0.8,
          linestyle='--', zorder=1)

# ============================================================
# Panel (b): X-VLA pruning curves
# ============================================================
ax_b = fig.add_subplot(gs[1])

ax_b.text(-0.12, 1.06, '(b)', fontsize=14, fontweight='bold',
          transform=ax_b.transAxes, va='top', ha='left')

# Data
k_object = [1.0, 0.95, 0.9, 0.85, 0.8, 0.7, 0.5, 0.3]
sr_object = [99.2, 99.0, 99.2, 68.0, 89.0, 56.2, 42.6, 23.0]

k_goal = [1.0, 0.9, 0.5]
sr_goal = [98.0, 70.2, 61.0]

# Plot Object suite
ax_b.plot(k_object, sr_object, 'o-', color=C_BLUE, markersize=7,
          label='Object suite', zorder=3, markeredgecolor='white', markeredgewidth=0.8)

# Plot Goal suite
ax_b.plot(k_goal, sr_goal, 's-', color=C_RED, markersize=8,
          label='Goal suite', zorder=3, markeredgecolor='white', markeredgewidth=0.8)

# Baseline dashed lines
ax_b.axhline(y=99.2, color=C_BLUE, linestyle=':', linewidth=0.9, alpha=0.4, zorder=1)
ax_b.axhline(y=98.0, color=C_RED, linestyle=':', linewidth=0.9, alpha=0.4, zorder=1)

# Annotate key points with path effects
def annotate_pt(ax, text, xy, xytext, color, fontsize=9, bold=False):
    t = ax.annotate(text, xy=xy, xytext=xytext,
                    textcoords='offset points', fontsize=fontsize,
                    color=color, fontweight='bold' if bold else 'normal',
                    arrowprops=dict(arrowstyle='-', color=color, lw=0.6, alpha=0.5),
                    zorder=5)
    t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
    return t

# Direct labels near k=0.9 points — no connecting arrows, just text
ax_b.text(0.9, 100.5, '99.2%', fontsize=9, color=C_BLUE, ha='center', va='bottom',
          path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])
ax_b.text(0.9, 66.5, '70.2%', fontsize=9.5, color=C_RED, ha='center', va='top',
          fontweight='bold',
          path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# Vertical double-arrow at k=0.895 (slightly offset to avoid marker overlap)
ax_b.annotate('', xy=(0.895, 95.5), xytext=(0.895, 72.5),
              arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.5),
              zorder=4)

# "27.8pp gap" label — placed to the right of the arrow (lower k region)
ax_b.text(0.845, 84, '27.8pp\ngap', fontsize=10, ha='right', va='center',
          color='#333333', fontweight='bold', linespacing=1.2,
          path_effects=[pe.withStroke(linewidth=3, foreground='white')])

# Light shaded band at k=0.9
ax_b.axvspan(0.888, 0.912, alpha=0.07, color='#555555', zorder=0)

# Axis config
ax_b.set_xlabel('Keep ratio $k$', fontsize=12)
ax_b.set_ylabel('Success Rate (%)', fontsize=12)
ax_b.set_xlim(0.25, 1.07)
ax_b.set_ylim(15, 105)
ax_b.set_xticks([0.3, 0.5, 0.7, 0.8, 0.9, 1.0])
ax_b.set_xticklabels(['0.3', '0.5', '0.7', '0.8', '0.9', '1.0'])
ax_b.invert_xaxis()

ax_b.set_title('X-VLA (L2-norm pruning): same model, same $k$,\ndramatic task-dependent gap',
               fontsize=10, fontstyle='italic', color='#444444', pad=8)

# Direct curve labels near the curves
ax_b.text(0.42, 38, 'Object', fontsize=10, color=C_BLUE, fontweight='bold',
          path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])
ax_b.text(0.42, 64, 'Goal', fontsize=10, color=C_RED, fontweight='bold',
          path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# ============================================================
# Save
# ============================================================
outdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper'
fig.savefig(f'{outdir}/fig_teaser.pdf')
fig.savefig(f'{outdir}/fig_teaser.png')
print(f'Saved fig_teaser.pdf and fig_teaser.png')
