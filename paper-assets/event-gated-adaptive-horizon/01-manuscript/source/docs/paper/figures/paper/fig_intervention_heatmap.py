#!/usr/bin/env python3
"""Intervention Heatmap — §4 "Why Standard Remedies Fail"

Visualises prevention rates across 9 interventions × 2 environments.
Wong/Okabe-Ito: orange (#E69F00) = CIVO onset, blue (#0072B2) = full prevention.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.colors import to_rgb

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# ── Colours (Wong / Okabe-Ito) ──
C_BLUE   = '#0072B2'
C_ORANGE = '#E69F00'
C_NA     = '#E8E8E8'

def rate_to_color(rate):
    if rate is None:
        return C_NA
    keys = [
        (0.00, np.array(to_rgb('#E69F00'))),
        (0.25, np.array(to_rgb('#CCA44C'))),
        (0.50, np.array(to_rgb('#7FA5B8'))),
        (0.75, np.array(to_rgb('#3E8FB4'))),
        (1.00, np.array(to_rgb('#0072B2'))),
    ]
    for i in range(len(keys) - 1):
        t0, c0 = keys[i]
        t1, c1 = keys[i + 1]
        if rate <= t1 + 1e-9:
            f = (rate - t0) / (t1 - t0) if t1 > t0 else 0.0
            return tuple((1 - f) * c0 + f * c1)
    return C_BLUE

# ── Data ──
grid = [
    [(0,2), (0,2), (1,4), (0,2), (2,4), (1,2), (0,2), (0,2), (3,3)],
    [None,  (0,1), (0,2), None,  (1,1), (0,1), None,  None,  (0,1)],
]
BORDERLINE = set()

col_labels = [
    "Reward\nSGS", "Full\nSGS", "Obs-dec.\nSGS",
    "RAVE",
    "TCN\nσ=0.2", "TCN\nσ=0.5",
    "Narrow\nDual", "Wide\nSingle", "Wide\nDual",
]
row_labels = ["Walker Walk", "Cheetah Run"]
groups = [
    (0, 2, "Gradient"),
    (3, 3, "Output"),
    (4, 5, "Repr."),
    (6, 8, "Architecture"),
]
group_starts = {3, 4, 6}

N_R, N_C = 2, 9

# ── Layout geometry (data units, aspect='equal') ──
CW   = 1.0     # cell width
CH   = 0.78    # cell height
XG   = 0.055   # x gap between cells
YG   = 0.055   # y gap between rows
GG   = 0.16    # extra gap at group boundaries
RAD  = 0.08    # corner radius

# Column x-positions
xpos = []
x = 0.0
for c in range(N_C):
    if c in group_starts:
        x += GG
    xpos.append(x)
    x += CW + XG

# Row y-positions (top to bottom)
ypos = [0.0, CH + YG]

grid_w = xpos[-1] + CW
grid_h = ypos[-1] + CH

# ── Figure ──
fig, ax = plt.subplots(figsize=(7, 3.2))

for r in range(N_R):
    for c in range(N_C):
        cell = grid[r][c]
        bl = (r, c) in BORDERLINE

        if cell is None:
            color, txt, na = C_NA, '—', True
        else:
            num, den = cell
            rate = num / den
            if bl:
                rate = 0.50
            color = rate_to_color(rate)
            txt = f'{num}/{den}' + ('*' if bl else '')
            na = False

        rx, ry = xpos[c], ypos[r]
        rect = mpatches.FancyBboxPatch(
            (rx, ry), CW, CH,
            boxstyle=mpatches.BoxStyle.Round(pad=0, rounding_size=RAD),
            facecolor=color, edgecolor='none', zorder=1)
        ax.add_patch(rect)

        tc = '#888888' if na else 'white'
        tw = 'normal' if na else 'bold'
        t = ax.text(rx + CW / 2, ry + CH / 2, txt,
                    ha='center', va='center',
                    fontsize=10, fontweight=tw, color=tc, zorder=2)
        if not na:
            t.set_path_effects([
                pe.withStroke(linewidth=2.0, foreground='#00000050')])

# Axes
ax.set_xlim(-1.6, grid_w + 0.3)
ax.set_ylim(grid_h + 1.0, -0.7)
ax.set_aspect('equal')
ax.axis('off')

# ── Column labels ──
for c in range(N_C):
    ax.text(xpos[c] + CW / 2, grid_h + 0.12, col_labels[c],
            ha='center', va='top', fontsize=7.5, color='#444444',
            linespacing=0.88)

# ── Row labels ──
for r in range(N_R):
    ax.text(-0.12, ypos[r] + CH / 2, row_labels[r],
            ha='right', va='center', fontsize=9, color='#333333')

# ── Group brackets ──
bk_bot = -0.08
bk_top = -0.20
for s, e, lab in groups:
    x0 = xpos[s] + 0.08
    x1 = xpos[e] + CW - 0.08
    xm = (x0 + x1) / 2
    ax.plot([x0, x0, x1, x1], [bk_bot, bk_top, bk_top, bk_bot],
            color='#888888', lw=0.7, solid_capstyle='butt', clip_on=False)
    ax.text(xm, bk_top - 0.04, lab, ha='center', va='bottom',
            fontsize=7.5, color='#666666', fontstyle='italic', clip_on=False)

# ── Legend ──
handles = [
    mpatches.Patch(facecolor=C_BLUE, edgecolor='none', label='Full Prevention'),
    mpatches.Patch(facecolor=rate_to_color(0.5), edgecolor='none', label='Partial'),
    mpatches.Patch(facecolor=C_ORANGE, edgecolor='none', label='CIVO Onset'),
    mpatches.Patch(facecolor=C_NA, edgecolor='#CCCCCC', lw=0.5, label='Untested'),
]
ax.legend(handles=handles, loc='upper center',
          bbox_to_anchor=(0.53, -0.01), ncol=4,
          fontsize=7, frameon=False,
          handlelength=1.0, handleheight=0.7,
          handletextpad=0.3, columnspacing=0.8)


# ── Save ──
import os
outdir = os.path.dirname(os.path.abspath(__file__))
for ext in ('pdf', 'png'):
    fig.savefig(os.path.join(outdir, f'fig_intervention_heatmap.{ext}'))
plt.close()
print('Saved fig_intervention_heatmap.{pdf,png}')
