#!/usr/bin/env python3
"""Fig 1 Version B: Flow-emphasis overview — prominent arrows, narrative connections."""

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
    'rose': '#E7B8D4',
    'light_gray': '#E8E8E8',
    'medium_gray': '#E0E0E0',
    'dark': '#4A4A4A',
    'soft_red': '#E07070',
    'soft_green': '#7CB97C',
    'flow_gray': '#B0B0B0',
    'dashed_gray': '#C0C0C0',
}
SANS = {'fontfamily': 'sans-serif'}
SERIF = {'fontfamily': 'serif'}


def shadow_box(ax, x, y, w, h, fc, ec='#C8C8C8', lw=0.8,
               bs="round,pad=0.02", alpha=1.0, ls='-'):
    ax.add_patch(FancyBboxPatch((x + 0.006, y - 0.009), w, h, boxstyle=bs,
                 facecolor='#D0D0D0', edgecolor='none', alpha=0.25, zorder=1))
    p = FancyBboxPatch((x, y), w, h, boxstyle=bs, facecolor=fc,
                       edgecolor=ec, linewidth=lw, alpha=alpha,
                       linestyle=ls, zorder=2)
    ax.add_patch(p)
    return p


def num_circle(ax, x, y, n, color, r=0.042, fs=11):
    ax.add_patch(Circle((x + 0.005, y - 0.008), r, fc='#D0D0D0', ec='none',
                        alpha=0.25, zorder=1))
    ax.add_patch(Circle((x, y), r, fc=color, ec='white', lw=2.0, zorder=3))
    ax.text(x, y, str(n), ha='center', va='center', fontsize=fs,
            fontweight='bold', color='white', zorder=4, **SANS)


def thick_arrow(ax, s, e, color='#888888', lw=2.0, style='-|>', rad=0.0, ms=14):
    conn = f'arc3,rad={rad}'
    a = FancyArrowPatch(s, e, arrowstyle=style, connectionstyle=conn,
                        color=color, lw=lw, mutation_scale=ms, zorder=3)
    ax.add_patch(a)
    return a


def thin_arrow(ax, s, e, color='#AAAAAA', lw=0.8, style='->', rad=0.0, ms=8):
    conn = f'arc3,rad={rad}'
    a = FancyArrowPatch(s, e, arrowstyle=style, connectionstyle=conn,
                        color=color, lw=lw, mutation_scale=ms, zorder=3)
    ax.add_patch(a)
    return a


# ── Figure ────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 4.5), dpi=300)

ax_a = fig.add_axes([0.03, 0.04, 0.27, 0.91])
ax_b = fig.add_axes([0.33, 0.04, 0.35, 0.91])
ax_c = fig.add_axes([0.71, 0.04, 0.27, 0.91])

for ax in [ax_a, ax_b, ax_c]:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')


# ═══════════════════════════════════════════════════════════════════════════════
# Panel (a): VLA Sequence Structure — FLOW EMPHASIS
# ═══════════════════════════════════════════════════════════════════════════════
ax_a.text(0.02, 0.97, '(a)', fontsize=14, fontweight='bold', va='top', **SERIF)
ax_a.text(0.52, 0.97, 'VLA sequence structure', ha='center', va='top',
          fontsize=10, fontweight='bold', color=C['dark'], **SERIF)

# ── Large "causal flow" arrow on far left ──
thick_arrow(ax_a, (0.05, 0.87), (0.05, 0.12), color=C['flow_gray'],
            lw=3.0, style='-|>', ms=18)
ax_a.text(0.015, 0.50, 'causal\nflow', ha='center', va='center',
          fontsize=7, color='#999999', rotation=90, style='italic',
          **SANS, linespacing=1.2)

# ── Image tokens ──
shadow_box(ax_a, 0.18, 0.76, 0.72, 0.14, fc='white', ec=C['sky_blue'],
           lw=1.4, ls='--', bs="round,pad=0.02")
ax_a.text(0.54, 0.93, 'Image tokens', ha='center', va='top',
          fontsize=9, color=C['dark'], **SANS)

for tx in [0.24, 0.40, 0.56, 0.72]:
    shadow_box(ax_a, tx, 0.78, 0.10, 0.10, fc=C['sky_blue'],
               ec='#9BBDD4', lw=0.6, bs="round,pad=0.01")

# image_mean label
ax_a.text(0.14, 0.84, 'image\nmean', ha='center', va='center',
          fontsize=6, color='#888888', style='italic', **SANS, linespacing=1.1)
thin_arrow(ax_a, (0.14, 0.80), (0.14, 0.77), color='#BBBBBB', lw=0.6, ms=5)

# ── THICK arrow: Image → Instruction ──
thick_arrow(ax_a, (0.54, 0.74), (0.54, 0.66), color=C['flow_gray'],
            lw=2.0, style='-|>', ms=12)

# ── Causal mask X marker ──
ax_a.text(0.40, 0.60, 'X', fontsize=14, ha='center', va='center',
          color=C['soft_red'], fontweight='bold', zorder=5, **SANS)
ax_a.text(0.59, 0.60, 'causal mask:\nno backward\nattention',
          ha='center', va='center', fontsize=6.5, color=C['soft_red'],
          style='italic', **SANS, linespacing=1.2)

# ── Instruction tokens ──
shadow_box(ax_a, 0.18, 0.42, 0.72, 0.14, fc='white', ec=C['gold'],
           lw=1.4, ls='--', bs="round,pad=0.02")
ax_a.text(0.54, 0.59, 'Instruction tokens', ha='center', va='top',
          fontsize=9, color=C['dark'], **SANS)
ax_a.text(0.54, 0.49, '"pick up the red block"', ha='center', va='center',
          fontsize=7.5, color=C['dark'], style='italic', **SANS)

# ── Green curved arrow: full context access ──
thick_arrow(ax_a, (0.14, 0.49), (0.14, 0.79), color=C['soft_green'],
            lw=1.5, rad=-0.45, ms=10, style='-|>')
ax_a.text(0.09, 0.65, 'full\ncontext\naccess', ha='center', va='center',
          fontsize=5.5, color=C['soft_green'], fontweight='bold',
          **SANS, linespacing=1.1)

# ── THICK arrow: Instruction → R + Act ──
thick_arrow(ax_a, (0.54, 0.40), (0.54, 0.32), color=C['flow_gray'],
            lw=2.0, style='-|>', ms=12)

# ── Readout box ──
shadow_box(ax_a, 0.18, 0.10, 0.27, 0.20, fc=C['lavender'],
           ec='#B0A0D0', lw=1.0, bs="round,pad=0.02")
ax_a.text(0.315, 0.21, 'R', ha='center', va='center',
          fontsize=16, fontweight='bold', color=C['dark'], **SERIF)
ax_a.text(0.315, 0.06, 'readout', ha='center', va='center',
          fontsize=8, color=C['dark'], **SANS)

# ── Action box ──
shadow_box(ax_a, 0.56, 0.10, 0.27, 0.20, fc=C['mint_green'],
           ec='#8CC08C', lw=1.0, bs="round,pad=0.02")
ax_a.text(0.695, 0.21, 'Act', ha='center', va='center',
          fontsize=14, fontweight='bold', color=C['dark'], **SERIF)
ax_a.text(0.695, 0.06, 'action', ha='center', va='center',
          fontsize=8, color=C['dark'], **SANS)

# Arrow R → Act
thick_arrow(ax_a, (0.46, 0.20), (0.55, 0.20), color='#AAAAAA', lw=1.2, ms=10)


# ═══════════════════════════════════════════════════════════════════════════════
# Panel (b): Three Analysis Methods — with dashed separators
# ═══════════════════════════════════════════════════════════════════════════════
ax_b.text(0.01, 0.97, '(b)', fontsize=14, fontweight='bold', va='top', **SERIF)
ax_b.text(0.50, 0.97, 'Three analysis methods', ha='center', va='top',
          fontsize=10, fontweight='bold', color=C['dark'], **SERIF)

# ── Method 1: Layer-wise action probes ──
m1_y = 0.76
num_circle(ax_b, 0.055, m1_y + 0.10, '1', C['sky_blue'])
ax_b.text(0.12, m1_y + 0.10, 'Layer-wise action probes', ha='left',
          va='center', fontsize=9.5, fontweight='bold', color=C['dark'], **SANS)

for lx, ll in zip([0.06, 0.19, 0.32], ['L1', 'L2', 'L3']):
    shadow_box(ax_b, lx, m1_y - 0.02, 0.10, 0.10, fc=C['sky_blue'],
               ec='#9BBDD4', lw=0.6, bs="round,pad=0.01")
    ax_b.text(lx + 0.05, m1_y + 0.03, ll, ha='center', va='center',
              fontsize=8.5, color=C['dark'], **SANS)

thick_arrow(ax_b, (0.44, m1_y + 0.03), (0.50, m1_y + 0.03),
            color='#888888', lw=1.2, ms=10)

shadow_box(ax_b, 0.51, m1_y - 0.02, 0.13, 0.10, fc='white',
           ec='#C8C8C8', lw=0.8, bs="round,pad=0.01")
ax_b.text(0.575, m1_y + 0.03, 'Probe', ha='center', va='center',
          fontsize=8, color=C['dark'], **SANS)

# R² badge — positioned below the arrow, not overlapping title
r2_x, r2_y = 0.475, m1_y - 0.005
ax_b.add_patch(Circle((r2_x, r2_y), 0.025, fc=C['salmon'], ec='white',
                       lw=1.2, zorder=5))
ax_b.text(r2_x, r2_y, 'R²', ha='center', va='center',
          fontsize=6, color='white', fontweight='bold', zorder=6, **SANS)

thick_arrow(ax_b, (0.65, m1_y + 0.03), (0.71, m1_y + 0.03),
            color='#888888', lw=1.2, ms=10)

shadow_box(ax_b, 0.72, m1_y - 0.02, 0.23, 0.10, fc=C['light_gray'],
           ec='#C8C8C8', lw=0.6, bs="round,pad=0.01")
ax_b.text(0.835, m1_y + 0.03, '7-DoF action', ha='center', va='center',
          fontsize=7.5, color=C['dark'], **SANS)

# ── Dashed separator 1 ──
sep1_y = 0.62
ax_b.plot([0.05, 0.95], [sep1_y, sep1_y], color=C['dashed_gray'],
          lw=0.8, ls='--', zorder=1)
ax_b.text(0.50, sep1_y + 0.025, 'complementary analyses', ha='center',
          va='center', fontsize=7, color='#AAAAAA', style='italic',
          **SANS, bbox=dict(facecolor='white', edgecolor='none', pad=2))

# ── Method 2: Counterfactual perturbation ──
m2_y = 0.42
num_circle(ax_b, 0.055, m2_y + 0.14, '2', C['salmon'])
ax_b.text(0.12, m2_y + 0.14, 'Counterfactual perturbation', ha='left',
          va='center', fontsize=9.5, fontweight='bold', color=C['dark'], **SANS)

pills = [
    ('correct',  C['mint_green']),
    ('empty',    '#E8E8E8'),
    ('wrong',    C['salmon']),
    ('shuffle',  C['gold']),
    ('paraph.',  C['lavender']),
]
pw, pg = 0.155, 0.165
for i, (label, color) in enumerate(pills):
    px = 0.04 + i * pg
    shadow_box(ax_b, px, m2_y + 0.03, pw, 0.08, fc=color,
               ec='#C8C8C8', lw=0.5, bs="round,pad=0.02")
    ax_b.text(px + pw / 2, m2_y + 0.07, label, ha='center', va='center',
              fontsize=6.5, color=C['dark'], **SANS)

thick_arrow(ax_b, (0.50, m2_y + 0.02), (0.50, m2_y - 0.03),
            color='#888888', lw=1.5, ms=10)
ax_b.text(0.56, m2_y - 0.015, 'Δ-action', ha='left', va='center',
          fontsize=8, color=C['dark'], style='italic', **SANS)

# ── Dashed separator 2 ──
sep2_y = 0.28
ax_b.plot([0.05, 0.95], [sep2_y, sep2_y], color=C['dashed_gray'],
          lw=0.8, ls='--', zorder=1)
ax_b.text(0.50, sep2_y + 0.025, 'complementary analyses', ha='center',
          va='center', fontsize=7, color='#AAAAAA', style='italic',
          **SANS, bbox=dict(facecolor='white', edgecolor='none', pad=2))

# ── Method 3: L1 attention profiling ──
m3_y = 0.03
num_circle(ax_b, 0.055, m3_y + 0.21, '3', C['gold'])
ax_b.text(0.12, m3_y + 0.21, 'L1 attention profiling', ha='left',
          va='center', fontsize=9.5, fontweight='bold', color=C['dark'], **SANS)

# Heatmap
hm_l = 0.33 + 0.08 * 0.35
hm_b = 0.04 + (m3_y + 0.01) * 0.91
hm_w = 0.09
hm_h = 0.16
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

# Legend lines
lx = 0.60
ax_b.plot([lx, lx + 0.08], [m3_y + 0.16, m3_y + 0.16], color=C['sky_blue'],
          lw=2.5, zorder=3, solid_capstyle='round')
ax_b.text(lx + 0.10, m3_y + 0.16, 'ro → instr.', fontsize=6.5,
          va='center', color=C['dark'], **SANS)

ax_b.plot([lx, lx + 0.08], [m3_y + 0.09, m3_y + 0.09], color=C['salmon'],
          lw=2.5, zorder=3, solid_capstyle='round')
ax_b.text(lx + 0.10, m3_y + 0.09, 'ro → image', fontsize=6.5,
          va='center', color=C['dark'], **SANS)

ax_b.text(lx + 0.12, m3_y + 0.02, 'attention ratio', fontsize=7,
          ha='center', va='center', color=C['dark'], style='italic', **SANS)


# ═══════════════════════════════════════════════════════════════════════════════
# Panel (c): Finding Classification — 4 rows with summary
# ═══════════════════════════════════════════════════════════════════════════════
ax_c.text(0.02, 0.97, '(c)', fontsize=14, fontweight='bold', va='top', **SERIF)
ax_c.text(0.52, 0.97, 'Finding classification', ha='center', va='top',
          fontsize=10, fontweight='bold', color=C['dark'], **SERIF)

findings = [
    ('1', C['sky_blue'], 'Exit collapse\n(ΔR² > 0.10)',
     'Training-\nassociated', C['sky_blue'], 0.80),
    ('2', C['salmon'],   'CF sensitivity\n(d ≥ 0.45)',
     'Action-\nlinked',     C['salmon'],   0.55),
    ('3', C['gold'],     'L1 instruction\nattention',
     'Inherited\nprior',    C['gold'],     0.30),
]

for num, col, desc, cat, cat_col, yc in findings:
    num_circle(ax_c, 0.06, yc, num, col)

    shadow_box(ax_c, 0.14, yc - 0.08, 0.36, 0.16, fc='white',
               ec='#D0D0D0', lw=0.8, bs="round,pad=0.02")
    ax_c.text(0.32, yc, desc, ha='center', va='center',
              fontsize=8, color=C['dark'], **SANS, linespacing=1.3)

    thick_arrow(ax_c, (0.52, yc), (0.59, yc), color='#AAAAAA', lw=1.2, ms=10)

    bar = mpatches.Rectangle((0.61, yc - 0.08), 0.025, 0.16,
                              facecolor=cat_col, edgecolor='none', zorder=3)
    ax_c.add_patch(bar)
    shadow_box(ax_c, 0.635, yc - 0.08, 0.31, 0.16, fc=cat_col,
               ec='none', lw=0, bs="round,pad=0.02", alpha=0.25)
    ax_c.text(0.79, yc, cat, ha='center', va='center',
              fontsize=8.5, fontweight='bold', color=C['dark'],
              **SANS, linespacing=1.3)

# ── Thin separator before summary ──
ax_c.plot([0.05, 0.95], [0.17, 0.17], color='#D0D0D0', lw=0.6, zorder=1)

# ── Summary row ──
# Three-color left border stripes (stacked vertically)
stripe_h = 0.04
stripe_colors = [C['gold'], C['salmon'], C['sky_blue']]
for i, sc in enumerate(stripe_colors):
    sy = 0.02 + i * stripe_h
    bar = mpatches.Rectangle((0.05, sy), 0.03, stripe_h,
                              facecolor=sc, edgecolor='none', zorder=4)
    ax_c.add_patch(bar)

# Summary box with subtle gradient-like background
shadow_box(ax_c, 0.075, 0.02, 0.87, 0.12, fc='#F5F5F5',
           ec='#D8D8D8', lw=0.8, bs="round,pad=0.02", alpha=0.9)
ax_c.text(0.51, 0.08, 'Combined: Cross-architecture\ninstruction routing decomposition',
          ha='center', va='center', fontsize=8.5, fontweight='bold',
          color=C['dark'], **SANS, linespacing=1.3)


# ── Save ──────────────────────────────────────────────────────────────────────
fig.savefig('/tmp/fig_overview_vB.png', bbox_inches='tight', pad_inches=0.02, dpi=300)
plt.close()
print("Done: /tmp/fig_overview_vB.png")
