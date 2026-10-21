#!/usr/bin/env python3
"""§3 Method overview: Model Zoo → Per-Example Decomposition → Cross-Architecture Overlap."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from palette import BLUE, CORAL, TEAL, AMBER, GRAY, DARK, LIGHT, SLATE, RCPARAMS

plt.rcParams.update(RCPARAMS)
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['savefig.facecolor'] = 'white'

fig, ax = plt.subplots(figsize=(3.35, 2.2))
fig.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

ARCHS = [('GDN', BLUE), ('RetNet', CORAL), ('HGRN2', TEAL)]

C_HELPED = AMBER
C_HURT   = '#996B6B'
C_UNCH   = LIGHT

SHADOW_C = '#00000008'

def rbox(x, y, w, h, fc, ec=None, alpha=1.0, lw=0.4, zorder=2, shadow=False):
    if shadow:
        s = FancyBboxPatch((x + 0.03, y - 0.03), w, h, boxstyle="round,pad=0.06",
                            fc='#00000009', ec='none', lw=0, zorder=zorder - 1)
        ax.add_patch(s)
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                        fc=fc, ec=ec or fc, lw=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(p)

# ── panel backgrounds with subtle shadow ──
panel_bg, panel_ec = '#FFFFFF', '#E0E0E0'
for px, pw in [(0.05, 2.45), (2.85, 3.65), (6.85, 3.05)]:
    rbox(px, 0.35, pw, 6.05, panel_bg, ec=panel_ec, lw=0.3, zorder=0, shadow=True)

# ── stage titles with circled numbers ──
ax.text(1.28, 6.55, '①  Model Zoo', ha='center', fontsize=6.5,
        fontweight='bold', color=DARK)
ax.text(4.68, 6.55, '②  Per-Example', ha='center', fontsize=6.5,
        fontweight='bold', color=DARK)
ax.text(4.68, 6.12, 'Decomposition', ha='center', fontsize=5.5, color=SLATE)
ax.text(8.38, 6.55, '③  Cross-Architecture', ha='center', fontsize=5.8,
        fontweight='bold', color=DARK)
ax.text(8.38, 6.15, 'Overlap', ha='center', fontsize=5.2, color=SLATE)

# ═══════════════════════════════════════════════
# STAGE 1 — Model Zoo
# ═══════════════════════════════════════════════
bw, bh = 0.72, 0.48
y_rows = [4.85, 3.50, 2.15]

for (name, color), y in zip(ARCHS, y_rows):
    rbox(0.22, y, bw, bh, color, alpha=0.15, ec=color, lw=0.45, shadow=True)
    ax.text(0.22 + bw / 2, y + bh / 2, 'Pure', ha='center', va='center',
            fontsize=4.5, color=color, fontweight='medium', zorder=3)

    x2 = 0.22 + bw + 0.10
    rbox(x2, y, bw, bh, color, alpha=0.82, lw=0.45, shadow=True)
    ax.text(x2 + bw / 2, y + bh / 2, '+Attn', ha='center', va='center',
            fontsize=4.5, color='white', fontweight='bold', zorder=3)

    ax.text(1.28, y - 0.15, name, ha='center', va='top',
            fontsize=5, color=color, fontweight='bold')

# ═══════════════════════════════════════════════
# ARROWS  Stage 1 → Stage 2
# ═══════════════════════════════════════════════
arrow_c = '#8C8C8C'
for y in y_rows:
    yc = y + bh / 2
    ax.annotate('', xy=(3.05, yc), xytext=(2.52, yc),
                arrowprops=dict(arrowstyle='->', color=arrow_c, lw=0.55,
                                mutation_scale=6))

# ═══════════════════════════════════════════════
# STAGE 2 — Per-Example Decomposition
# ═══════════════════════════════════════════════
ax.text(4.68, 5.72, r'pure($x_i$)  vs  hybrid($x_i$)', ha='center',
        fontsize=5, color=SLATE, fontstyle='italic')

dot_cx  = 4.18
dot_r   = 0.10
dot_gap = 0.27
group_gap = 0.20

groups = [
    (3, 'helped',    C_HELPED, '#7A6020'),
    (2, 'hurt',      C_HURT,   '#6B4444'),
    (5, 'unchanged', C_UNCH,   '#999999'),
]

y = 5.25
group_mids = []
for gi, (n, label, fill, txt_c) in enumerate(groups):
    y_top_g = y
    for i in range(n):
        circ = mpatches.Circle((dot_cx, y), dot_r, fc=fill, ec='white',
                                lw=0.4, zorder=3, alpha=0.88)
        ax.add_patch(circ)
        y -= dot_gap
    y_mid = y_top_g - (n - 1) * dot_gap / 2
    group_mids.append(y_mid)
    ax.text(dot_cx + 0.28, y_mid, label, fontsize=4.5, va='center',
            color=txt_c, fontweight='bold')
    y += dot_gap
    y -= dot_gap
    if gi < len(groups) - 1:
        y -= group_gap
        sep_y = y + group_gap / 2 + dot_gap / 2 - 0.02
        ax.plot([dot_cx - 0.20, dot_cx + 0.20], [sep_y, sep_y],
                color='#D8D8D8', lw=0.35, zorder=1)

ax.text(4.68, y - 0.28, r'$\times\,$3 architecture pairs',
        ha='center', fontsize=4.5, color=SLATE, fontstyle='italic')

# ═══════════════════════════════════════════════
# ARROWS  Stage 2 → Stage 3  (converging)
# ═══════════════════════════════════════════════
venn_cx, venn_cy = 8.25, 3.50
target_x = venn_cx - 0.95

src_x = 5.55
rads = [-0.15, 0.0, 0.15]
src_ys = [4.80, 3.70, 2.50]
for sy, rad in zip(src_ys, rads):
    ax.annotate('', xy=(target_x, venn_cy), xytext=(src_x, sy),
                arrowprops=dict(arrowstyle='->', color=arrow_c, lw=0.45,
                                connectionstyle=f'arc3,rad={rad}',
                                mutation_scale=6))

# ═══════════════════════════════════════════════
# STAGE 3 — Cross-Architecture Overlap  (Venn)
# Circles BARELY touch — separation tuned for J ≈ 0.10
# ═══════════════════════════════════════════════
r_w, r_h = 0.82, 0.62
sep = 0.82

import math
angle_offsets = [
    (-sep * math.cos(math.radians(30)), sep * math.sin(math.radians(30))),
    ( sep * math.cos(math.radians(30)), sep * math.sin(math.radians(30))),
    (0.0, -sep * 0.58),
]
label_push = 1.10
label_offsets = [
    (-label_push * math.cos(math.radians(30)), label_push * math.sin(math.radians(30))),
    ( label_push * math.cos(math.radians(30)), label_push * math.sin(math.radians(30))),
    (0.0, -label_push * 0.70),
]

for (dx, dy), (lx, ly), (name, color) in zip(angle_offsets, label_offsets, ARCHS):
    ell = mpatches.Ellipse((venn_cx + dx, venn_cy + dy),
                            r_w, r_h,
                            fc=color, alpha=0.12, ec=color, lw=0.55, zorder=2,
                            linestyle='-')
    ax.add_patch(ell)
    t = ax.text(venn_cx + lx, venn_cy + ly, name, ha='center', va='center',
            fontsize=4.8, color=color, fontweight='bold', zorder=3)
    t.set_path_effects([pe.withStroke(linewidth=1.0, foreground='white')])

vc = venn_cy + 0.10
t = ax.text(venn_cx, vc, r'$J \approx 0.10$', ha='center',
            va='center', fontsize=6.5, color=DARK, fontweight='bold', zorder=4)
t.set_path_effects([pe.withStroke(linewidth=2.2, foreground='white')])

ax.text(venn_cx, venn_cy - 1.05,
        'low overlap\n→ architecture-specific\nsensitivity',
        ha='center', va='top', fontsize=4, color=SLATE, fontstyle='italic',
        linespacing=1.2)

# ═══════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════
out_dir = os.path.dirname(os.path.abspath(__file__))
paper_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures'
os.makedirs(paper_dir, exist_ok=True)

for d in [out_dir, paper_dir]:
    fig.savefig(os.path.join(d, 'fig_method_overview.pdf'),
                facecolor='white', edgecolor='none')
    fig.savefig(os.path.join(d, 'fig_method_overview.png'), dpi=300,
                facecolor='white', edgecolor='none')
plt.close()
print('Saved fig_method_overview')
