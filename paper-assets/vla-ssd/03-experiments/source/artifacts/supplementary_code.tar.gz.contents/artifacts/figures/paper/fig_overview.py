#!/usr/bin/env python3
"""Fig 1: Overview diagram — VLA sequence structure, analysis methods, finding classification."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'axes.facecolor': 'white',
    'figure.facecolor': 'white',
    'axes.edgecolor': 'none',
    'axes.linewidth': 0,
    'xtick.bottom': False,
    'ytick.left': False,
    'xtick.labelbottom': False,
    'ytick.labelleft': False,
})

C = {
    'sky_blue': '#B8D4E8',
    'salmon': '#F4A582',
    'mint_green': '#A6DBA0',
    'gold': '#FDB863',
    'lavender': '#C7B8E8',
    'light_gray': '#F0F0F0',
    'medium_gray': '#E0E0E0',
    'dark': '#4A4A4A',
    'soft_red': '#E07070',
    'soft_green': '#7CB97C',
}
SANS = {'fontfamily': 'sans-serif'}
SERIF = {'fontfamily': 'serif'}


def shadow_box(ax, x, y, w, h, fc, ec='#C8C8C8', lw=0.8,
               bs="round,pad=0.02", alpha=1.0, ls='-'):
    ax.add_patch(FancyBboxPatch((x+0.008, y-0.012), w, h, boxstyle=bs,
                 facecolor='#D0D0D0', edgecolor='none', alpha=0.3, zorder=1))
    p = FancyBboxPatch((x, y), w, h, boxstyle=bs, facecolor=fc,
                       edgecolor=ec, linewidth=lw, alpha=alpha,
                       linestyle=ls, zorder=2)
    ax.add_patch(p)
    return p


def num_circle(ax, x, y, n, color, r=0.035, fs=9):
    ax.add_patch(Circle((x+0.005, y-0.008), r, fc='#D0D0D0', ec='none',
                        alpha=0.3, zorder=1))
    ax.add_patch(Circle((x, y), r, fc=color, ec='white', lw=1.5, zorder=3))
    ax.text(x, y, str(n), ha='center', va='center', fontsize=fs,
            fontweight='bold', color='white', zorder=4, **SANS)


def arrow(ax, s, e, color='#888888', lw=1.0, style='->', rad=0.0, ms=10):
    conn = f'arc3,rad={rad}'
    a = FancyArrowPatch(s, e, arrowstyle=style, connectionstyle=conn,
                        color=color, lw=lw, mutation_scale=ms, zorder=3)
    ax.add_patch(a)
    return a


# ── Figure ────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 4), dpi=300)

# Panel axes — extra left margin for panel (a) labels
ax_a = fig.add_axes([0.04, 0.05, 0.26, 0.90])
ax_b = fig.add_axes([0.34, 0.05, 0.34, 0.90])
ax_c = fig.add_axes([0.72, 0.05, 0.26, 0.90])

for ax in [ax_a, ax_b, ax_c]:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

# ═══════════════════════════════════════════════════════════════════════════════
# Panel (a): VLA Sequence Structure
# ═══════════════════════════════════════════════════════════════════════════════
ax_a.text(0.03, 0.97, '(a)', fontsize=12, fontweight='bold', va='top', **SERIF)

# Image tokens dashed region
shadow_box(ax_a, 0.12, 0.78, 0.80, 0.17, fc='white', ec=C['sky_blue'],
           lw=1.2, ls='--', bs="round,pad=0.02")
ax_a.text(0.52, 0.98, 'Image tokens', ha='center', va='top',
          fontsize=9, color=C['dark'], **SANS)

# 4 token squares
for tx in [0.20, 0.37, 0.54, 0.71]:
    shadow_box(ax_a, tx, 0.81, 0.10, 0.10, fc=C['sky_blue'],
               ec='#9BBDD4', lw=0.6, bs="round,pad=0.01")

# image_mean label (left, outside the box)
ax_a.text(0.07, 0.87, 'image\nmean', ha='center', va='center',
          fontsize=6.5, color='#777777', style='italic', **SANS)
arrow(ax_a, (0.07, 0.82), (0.07, 0.79), color='#AAAAAA', lw=0.6, ms=6)

# Vertical connector arrow
arrow(ax_a, (0.52, 0.77), (0.52, 0.72), color='#BBBBBB', lw=0.8)

# Causal mask X marker — use plain 'X' to avoid glyph issues
ax_a.text(0.38, 0.67, 'X', fontsize=13, ha='center', va='center',
          color=C['soft_red'], fontweight='bold', zorder=5, **SANS)
ax_a.text(0.58, 0.67, 'cannot attend\nto instruction',
          ha='center', va='center', fontsize=7, color=C['soft_red'],
          style='italic', **SANS, linespacing=1.3)

# Vertical connector
arrow(ax_a, (0.52, 0.62), (0.52, 0.58), color='#BBBBBB', lw=0.8)

# Instruction tokens dashed region
shadow_box(ax_a, 0.12, 0.42, 0.80, 0.15, fc='white', ec=C['gold'],
           lw=1.2, ls='--', bs="round,pad=0.02")
ax_a.text(0.52, 0.60, 'Instruction tokens', ha='center', va='top',
          fontsize=9, color=C['dark'], **SANS)
ax_a.text(0.52, 0.49, 'pick up the red block', ha='center', va='center',
          fontsize=8, color=C['dark'], style='italic', **SANS)

# "attends to all context" arc arrow on left
arrow(ax_a, (0.13, 0.51), (0.13, 0.80), color=C['soft_green'],
      lw=0.9, rad=-0.5, ms=8)
ax_a.text(0.055, 0.65, 'attends\nto all\ncontext', ha='center', va='center',
          fontsize=5.5, color=C['soft_green'], **SANS, linespacing=1.2)

# Vertical connector
arrow(ax_a, (0.52, 0.41), (0.52, 0.32), color='#BBBBBB', lw=0.8)

# Readout box
shadow_box(ax_a, 0.16, 0.11, 0.25, 0.19, fc=C['lavender'],
           ec='#B0A0D0', lw=0.8, bs="round,pad=0.02")
ax_a.text(0.285, 0.21, 'R', ha='center', va='center',
          fontsize=15, fontweight='bold', color=C['dark'], **SERIF)
ax_a.text(0.285, 0.06, 'readout', ha='center', va='center',
          fontsize=8, color=C['dark'], **SANS)

# Action box
shadow_box(ax_a, 0.56, 0.11, 0.25, 0.19, fc=C['mint_green'],
           ec='#8CC08C', lw=0.8, bs="round,pad=0.02")
ax_a.text(0.685, 0.21, 'Act', ha='center', va='center',
          fontsize=13, fontweight='bold', color=C['dark'], **SERIF)
ax_a.text(0.685, 0.06, 'action', ha='center', va='center',
          fontsize=8, color=C['dark'], **SANS)

# Arrow R → Act
arrow(ax_a, (0.42, 0.205), (0.55, 0.205), color='#AAAAAA', lw=0.8)


# ═══════════════════════════════════════════════════════════════════════════════
# Panel (b): Three Analysis Methods
# ═══════════════════════════════════════════════════════════════════════════════
ax_b.text(0.02, 0.97, '(b)', fontsize=12, fontweight='bold', va='top', **SERIF)

# ── Method 1: Layer-wise action probes ──
m1_y = 0.74
num_circle(ax_b, 0.06, m1_y + 0.12, '1', C['sky_blue'])
ax_b.text(0.12, m1_y + 0.12, 'Layer-wise action probes', ha='left',
          va='center', fontsize=9.5, fontweight='bold', color=C['dark'], **SANS)

for lx, ll in zip([0.06, 0.20, 0.34], ['L1', 'L2', 'L3']):
    shadow_box(ax_b, lx, m1_y - 0.03, 0.11, 0.11, fc=C['sky_blue'],
               ec='#9BBDD4', lw=0.6, bs="round,pad=0.01")
    ax_b.text(lx + 0.055, m1_y + 0.025, ll, ha='center', va='center',
              fontsize=8.5, color=C['dark'], **SANS)

arrow(ax_b, (0.47, m1_y + 0.025), (0.52, m1_y + 0.025), color='#888888', lw=0.8)

# Probe box
shadow_box(ax_b, 0.53, m1_y - 0.03, 0.14, 0.11, fc='white',
           ec='#C8C8C8', lw=0.8, bs="round,pad=0.01")
ax_b.text(0.60, m1_y + 0.025, 'Probe', ha='center', va='center',
          fontsize=8, color=C['dark'], **SANS)

# R² badge on arrow
r2_x, r2_y = 0.505, m1_y + 0.075
ax_b.add_patch(Circle((r2_x, r2_y), 0.024, fc=C['salmon'], ec='white',
                       lw=1.0, zorder=5))
ax_b.text(r2_x, r2_y, 'R²', ha='center', va='center',
          fontsize=5.5, color='white', fontweight='bold', zorder=6, **SANS)

arrow(ax_b, (0.68, m1_y + 0.025), (0.73, m1_y + 0.025), color='#888888', lw=0.8)

# 7-DoF box
shadow_box(ax_b, 0.74, m1_y - 0.03, 0.21, 0.11, fc=C['light_gray'],
           ec='#C8C8C8', lw=0.6, bs="round,pad=0.01")
ax_b.text(0.845, m1_y + 0.025, '7-DoF action', ha='center', va='center',
          fontsize=7.5, color=C['dark'], **SANS)


# ── Method 2: Counterfactual perturbation ──
m2_y = 0.43
num_circle(ax_b, 0.06, m2_y + 0.16, '2', C['sky_blue'])
ax_b.text(0.12, m2_y + 0.16, 'Counterfactual perturbation', ha='left',
          va='center', fontsize=9.5, fontweight='bold', color=C['dark'], **SANS)

pills = [
    ('correct',   C['mint_green'], 'v'),
    ('empty',     '#E8E8E8',       'O'),
    ('wrong',     C['salmon'],     'x'),
    ('shuffle',   C['gold'],       's'),
    ('paraph.',   C['lavender'],   '~'),
]
pw, pg = 0.155, 0.165
for i, (label, color, sym) in enumerate(pills):
    px = 0.045 + i * pg
    shadow_box(ax_b, px, m2_y + 0.04, pw, 0.08, fc=color,
               ec='#C8C8C8', lw=0.5, bs="round,pad=0.02")
    ax_b.text(px + pw/2, m2_y + 0.08, label, ha='center', va='center',
              fontsize=6.5, color=C['dark'], **SANS)

# Arrow down to delta-action
arrow(ax_b, (0.50, m2_y + 0.03), (0.50, m2_y - 0.02), color='#888888', lw=0.8)
ax_b.text(0.55, m2_y - 0.01, 'Δaction', ha='left', va='center',
          fontsize=8, color=C['dark'], style='italic', **SANS)


# ── Method 3: L1 attention profiling ──
m3_y = 0.04
num_circle(ax_b, 0.06, m3_y + 0.24, '3', C['sky_blue'])
ax_b.text(0.12, m3_y + 0.24, 'L1 attention profiling', ha='left',
          va='center', fontsize=9.5, fontweight='bold', color=C['dark'], **SANS)

# Heatmap in figure coordinates
# ax_b is at [0.34, 0.05, 0.34, 0.90] in figure coords
hm_l = 0.34 + 0.10 * 0.34
hm_b = 0.05 + (m3_y + 0.01) * 0.90
hm_w = 0.09
hm_h = 0.18
heatmap_ax = fig.add_axes([hm_l, hm_b, hm_w, hm_h])

attn_data = np.array([
    [0.85, 0.65, 0.08, 0.04, 0.02],
    [0.50, 0.90, 0.12, 0.06, 0.03],
    [0.25, 0.20, 0.75, 0.45, 0.10],
    [0.15, 0.25, 0.65, 0.90, 0.55],
])
cmap = LinearSegmentedColormap.from_list('pb', ['#FFFFFF', C['sky_blue'], '#5B8EAA'])
heatmap_ax.imshow(attn_data, cmap=cmap, aspect='auto', vmin=0, vmax=1)
heatmap_ax.set_xticks([])
heatmap_ax.set_yticks(range(4))
heatmap_ax.set_yticklabels(['img', 'img', 'inst', 'ro'], fontsize=6.5, **SANS)
heatmap_ax.tick_params(axis='y', length=0, pad=2)
for sp in heatmap_ax.spines.values():
    sp.set_visible(False)

# Legend
lx = 0.62
ax_b.plot([lx, lx+0.07], [m3_y+0.16, m3_y+0.16], color=C['sky_blue'],
          lw=2.5, zorder=3, solid_capstyle='round')
ax_b.text(lx+0.09, m3_y+0.16, 'ro → instr.', fontsize=6.5,
          va='center', color=C['dark'], **SANS)

ax_b.plot([lx, lx+0.07], [m3_y+0.09, m3_y+0.09], color=C['salmon'],
          lw=2.5, zorder=3, solid_capstyle='round')
ax_b.text(lx+0.09, m3_y+0.09, 'ro → image', fontsize=6.5,
          va='center', color=C['dark'], **SANS)

ax_b.text(lx+0.12, m3_y+0.02, 'attention ratio', fontsize=7,
          ha='center', va='center', color=C['dark'], style='italic', **SANS)


# ═══════════════════════════════════════════════════════════════════════════════
# Panel (c): Finding Classification
# ═══════════════════════════════════════════════════════════════════════════════
ax_c.text(0.02, 0.97, '(c)', fontsize=12, fontweight='bold', va='top', **SERIF)

findings = [
    ('1', C['sky_blue'], 'Exit collapse\n(ΔR² > 0.10)',
     'Training-\nassociated', C['sky_blue'], 0.80),
    ('2', C['salmon'],   'CF sensitivity\n(d ≥ 0.45)',
     'Action-\nlinked',     C['salmon'],   0.50),
    ('3', C['gold'],     'L1 instruction\nattention',
     'Inherited\nprior',    C['gold'],     0.20),
]

for num, col, desc, cat, cat_col, yc in findings:
    num_circle(ax_c, 0.07, yc, num, col)

    # Description box
    shadow_box(ax_c, 0.15, yc-0.08, 0.36, 0.16, fc='white',
               ec='#D0D0D0', lw=0.8, bs="round,pad=0.02")
    ax_c.text(0.33, yc, desc, ha='center', va='center',
              fontsize=8, color=C['dark'], **SANS, linespacing=1.3)

    # Arrow
    arrow(ax_c, (0.53, yc), (0.60, yc), color='#AAAAAA', lw=0.8)

    # Category box — left accent bar + tinted background
    # Accent bar (thin rectangle on left edge)
    bar = mpatches.Rectangle((0.62, yc-0.08), 0.025, 0.16,
                              facecolor=cat_col, edgecolor='none', zorder=3)
    ax_c.add_patch(bar)
    # Tinted background
    shadow_box(ax_c, 0.645, yc-0.08, 0.30, 0.16, fc=cat_col,
               ec='none', lw=0, bs="round,pad=0.02", alpha=0.25)
    ax_c.text(0.795, yc, cat, ha='center', va='center',
              fontsize=8.5, fontweight='bold', color=C['dark'],
              **SANS, linespacing=1.3)


# ── Save ──────────────────────────────────────────────────────────────────────
out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures'
fig.savefig(f'{out}/fig_overview.pdf', bbox_inches='tight', pad_inches=0.02)
fig.savefig(f'{out}/fig_overview.png', bbox_inches='tight', pad_inches=0.02, dpi=300)
plt.close()
print("Done: fig_overview.pdf + fig_overview.png")
