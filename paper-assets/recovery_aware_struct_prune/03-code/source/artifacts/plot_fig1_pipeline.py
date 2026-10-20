#!/usr/bin/env python3
"""Generate RASP Pipeline Figure 1 — three-stage concept diagram."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

# ── Style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'mathtext.fontset': 'dejavusans',
})

# Okabe-Ito palette
OI_GREEN  = '#009E73'
OI_RED    = '#D55E00'
OI_BLUE   = '#0072B2'
OI_ORANGE = '#E69F00'
OI_SKY    = '#56B4E9'
OI_PINK   = '#CC79A7'

C_DARK  = '#333333'
C_MID   = '#666666'
C_LIGHT = '#AAAAAA'
C_VLIGHT = '#CCCCCC'

# Regime colours
C_KEEP    = OI_GREEN    # Protected
C_PRUNE_R = OI_RED      # Pruned: redundant
C_PRUNE_U = '#999999'   # Pruned: unimportant

# Stage background tints
BG_S1 = '#EBF2FA'
BG_S2 = '#FEF4E8'
BG_S3 = '#E8F5E9'

# ── Figure setup (inch-based coordinates) ──────────────────────────────
fig = plt.figure(figsize=(6.5, 3.2))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 6.5)
ax.set_ylim(0, 3.2)
ax.set_aspect('equal')
ax.axis('off')


# ── Helpers ────────────────────────────────────────────────────────────
def rbox(x, y, w, h, fc='white', ec=C_VLIGHT, lw=0.7, zorder=1, pad=0.05):
    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',
                       fc=fc, ec=ec, lw=lw, zorder=zorder)
    ax.add_patch(b)
    return b

def head_block(x, y, w, h, fc, label=None, fs=7):
    r = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.015',
                       fc=fc, ec=C_DARK, lw=0.5, zorder=3)
    ax.add_patch(r)
    if label:
        lum = 0.299 * int(fc[1:3], 16) + 0.587 * int(fc[3:5], 16) + 0.114 * int(fc[5:7], 16)
        tc = 'white' if lum < 160 else C_DARK
        ax.text(x + w / 2, y + h / 2, label, ha='center', va='center',
                fontsize=fs, color=tc, fontweight='bold', zorder=4)

def arrow(x1, y1, x2, y2, color=C_DARK, lw=1.5, hl=0.08, hw=0.06, style=None):
    props = dict(arrowstyle=f'->,head_length={hl},head_width={hw}',
                 color=color, lw=lw)
    if style:
        props['connectionstyle'] = style
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=props, zorder=5)


# ══════════════════════════════════════════════════════════════════════
#  LAYOUT CONSTANTS
# ══════════════════════════════════════════════════════════════════════
# Stage box geometry (x, width)
S1_X, S1_W = 0.08,  1.52
S2_X, S2_W = 1.95,  2.65
S3_X, S3_W = 4.95,  1.45
BOX_Y, BOX_H = 0.06, 2.70
TITLE_Y = 2.88

# ── Stage boxes ────────────────────────────────────────────────────
rbox(S1_X, BOX_Y, S1_W, BOX_H, fc=BG_S1, ec='#C4D7EA')
rbox(S2_X, BOX_Y, S2_W, BOX_H, fc=BG_S2, ec='#E5D4B8')
rbox(S3_X, BOX_Y, S3_W, BOX_H, fc=BG_S3, ec='#B8D8BA')

# ── Stage titles ───────────────────────────────────────────────────
for cx, txt, dy in [
    (S1_X + S1_W / 2, 'Stage 1: Structural\nAnalysis',         0),
    (S2_X + S2_W / 2, 'Stage 2: Recovery-Aware Scoring',       0.12),
    (S3_X + S3_W / 2, 'Stage 3: Two-Stage\nRecovery',          0),
]:
    ax.text(cx, TITLE_Y + dy, txt, ha='center', va='bottom',
            fontsize=8.5, fontweight='bold', color=C_DARK, linespacing=1.15)

# ── Big connecting arrows ──────────────────────────────────────────
for x1, x2 in [(S1_X + S1_W + 0.04, S2_X - 0.04),
                (S2_X + S2_W + 0.04, S3_X - 0.04)]:
    arrow(x1, 1.40, x2, 1.40, lw=2.2, hl=0.10, hw=0.08)


# ══════════════════════════════════════════════════════════════════════
#  STAGE 1 — Structural Analysis
# ══════════════════════════════════════════════════════════════════════
s1cx = S1_X + S1_W / 2

# Input label
ax.text(s1cx, 2.60, r'Model $\mathcal{M}$ + CoT Data', ha='center', va='center',
        fontsize=7, color=C_DARK,
        bbox=dict(boxstyle='round,pad=0.06', fc='white', ec=C_VLIGHT, lw=0.5))

arrow(s1cx, 2.46, s1cx, 2.34, color=C_MID, lw=0.8, hl=0.05, hw=0.03)

# Attention heads grid (2 rows × 3 cols)
head_info = [
    # (dx, dy, importance)
    (-0.32, 0.22, 0.95), (0.0, 0.22, 0.85), (0.32, 0.22, 0.70),
    (-0.32, -0.10, 0.55), (0.0, -0.10, 0.45), (0.32, -0.10, 0.30),
]
grid_cx, grid_cy = s1cx, 2.05
cmap_imp = plt.cm.YlOrRd
for dx, dy, imp in head_info:
    c = plt.Circle((grid_cx + dx, grid_cy + dy), 0.10,
                   fc=cmap_imp(imp * 0.7 + 0.2), ec=C_DARK, lw=0.4, zorder=3)
    ax.add_patch(c)

ax.text(s1cx, grid_cy + 0.48, 'Attention Heads', ha='center', fontsize=6.5,
        color=C_MID, style='italic')

# Branching arrows to I(h) and F(h)
arrow(s1cx - 0.15, 1.72, s1cx - 0.30, 1.58, color=C_MID, lw=0.8, hl=0.05, hw=0.03)
arrow(s1cx + 0.15, 1.72, s1cx + 0.30, 1.58, color=C_MID, lw=0.8, hl=0.05, hw=0.03)

# I(h) gradient bar
bar_w, bar_h = 1.10, 0.14
bx = s1cx - bar_w / 2
grad = np.linspace(0, 1, 256).reshape(1, -1)

ax.text(s1cx, 1.55, 'Taylor Importance', ha='center', fontsize=6, color=C_MID)
im1 = ax.imshow(grad, extent=[bx, bx + bar_w, 1.25, 1.25 + bar_h],
                cmap='YlOrRd', aspect='auto', zorder=3, interpolation='bilinear')
ax.text(bx - 0.04, 1.25 + bar_h / 2, '$I(h)$', ha='right', va='center',
        fontsize=8, color=C_DARK)

# F(h) gradient bar
ax.text(s1cx, 1.05, 'Intra-layer CKA Overlap', ha='center', fontsize=6, color=C_MID)
im2 = ax.imshow(grad, extent=[bx, bx + bar_w, 0.75, 0.75 + bar_h],
                cmap='PuBu', aspect='auto', zorder=3, interpolation='bilinear')
ax.text(bx - 0.04, 0.75 + bar_h / 2, '$F(h)$', ha='right', va='center',
        fontsize=8, color=C_DARK)

# Low / High labels
for yb in [1.25, 0.75]:
    ax.text(bx, yb - 0.04, 'Low', ha='left', va='top', fontsize=5, color=C_LIGHT)
    ax.text(bx + bar_w, yb - 0.04, 'High', ha='right', va='top', fontsize=5, color=C_LIGHT)

# Bottom annotation
ax.text(s1cx, 0.40, 'Per-head importance\n& redundancy profiling',
        ha='center', va='center', fontsize=6, color=C_MID, style='italic',
        linespacing=1.3)


# ══════════════════════════════════════════════════════════════════════
#  STAGE 2 — Recovery-Aware Scoring  (THE KEY PART)
# ══════════════════════════════════════════════════════════════════════
s2cx = S2_X + S2_W / 2

# Formula box
ax.text(s2cx, 2.60, r'$S(h) = I(h) \times \left(1 - F(h)\right)^{\alpha}$',
        ha='center', va='center', fontsize=9.5, color=C_DARK,
        bbox=dict(boxstyle='round,pad=0.07', fc='white', ec=OI_ORANGE, lw=1.2))

# ── Head data ──
#        name  I(h)  F(h)
heads = [('A', 0.95, 0.15),
         ('B', 0.85, 0.80),
         ('C', 0.70, 0.10),
         ('D', 0.55, 0.05),
         ('E', 0.45, 0.60),
         ('F', 0.30, 0.40)]

S_vals = [I * (1 - F) for _, I, F in heads]
# A→0.81  B→0.17  C→0.63  D→0.52  E→0.18  F→0.18

std_order  = sorted(range(6), key=lambda i: heads[i][1], reverse=True)
rasp_order = sorted(range(6), key=lambda i: S_vals[i],    reverse=True)
std_keep   = set(std_order[:3])    # {A=0, B=1, C=2}
rasp_keep  = set(rasp_order[:3])   # {A=0, C=2, D=3}

# ── Draw comparison panels ──
hw, hh = 0.28, 0.30
hgap = 0.07
n = len(heads)
total_hw = n * hw + (n - 1) * hgap
hx0 = s2cx - total_hw / 2

# -- Standard panel --
std_row_y = 1.88
ax.text(s2cx, 2.35, 'Standard Pruning  (rank by $I(h)$)',
        ha='center', va='center', fontsize=7.5, color=C_MID, style='italic')

for pos, idx in enumerate(std_order):
    name, I, F = heads[idx]
    x = hx0 + pos * (hw + hgap)
    kept = idx in std_keep
    fc = C_KEEP if kept else C_PRUNE_U
    head_block(x, std_row_y, hw, hh, fc=fc, label=name)
    # Show I(h) for all; highlight F(h) for key swapped heads (B, D)
    if name in ('B', 'D'):
        ax.text(x + hw / 2, std_row_y - 0.05, f'I={I:.2f}  F={F:.2f}',
                ha='center', va='top', fontsize=4.5, color=C_DARK, fontweight='bold')
    else:
        ax.text(x + hw / 2, std_row_y - 0.05, f'I={I:.2f}',
                ha='center', va='top', fontsize=4.5, color=C_MID)

# Threshold dashed line
thresh_x = hx0 + 3 * (hw + hgap) - hgap / 2
ax.plot([thresh_x, thresh_x], [std_row_y - 0.03, std_row_y + hh + 0.03],
        color='#CC0000', lw=1.2, ls='--', zorder=4)

# "keep" / "prune" labels
mid_keep_x = hx0 + 1 * (hw + hgap) + hw / 2
mid_prune_x = hx0 + 4 * (hw + hgap) + hw / 2
ax.text(mid_keep_x, std_row_y + hh + 0.07, 'keep', ha='center', va='bottom',
        fontsize=6, color=OI_GREEN, fontweight='bold')
ax.text(mid_prune_x, std_row_y + hh + 0.07, 'prune', ha='center', va='bottom',
        fontsize=6, color='#CC0000', fontweight='bold')

# -- RASP panel --
rasp_row_y = 1.10
ax.text(s2cx, 1.57, r'RASP  (rank by $S(h) = I \times (1{-}F)^\alpha$)',
        ha='center', va='center', fontsize=7.5, color=C_MID, style='italic')

for pos, idx in enumerate(rasp_order):
    name, I, F = heads[idx]
    x = hx0 + pos * (hw + hgap)
    kept = idx in rasp_keep
    if kept:
        fc = C_KEEP
    elif I >= 0.70 and F > 0.5:
        fc = C_PRUNE_R   # B: high I but high overlap → redundant
    else:
        fc = C_PRUNE_U   # E, F: low I → unimportant
    head_block(x, rasp_row_y, hw, hh, fc=fc, label=name)
    s = I * (1 - F)
    ax.text(x + hw / 2, rasp_row_y - 0.05, f'S={s:.2f}',
            ha='center', va='top', fontsize=4.5, color=C_MID)

# Threshold dashed line (same visual position: after 3rd element)
ax.plot([thresh_x, thresh_x], [rasp_row_y - 0.03, rasp_row_y + hh + 0.03],
        color='#CC0000', lw=1.2, ls='--', zorder=4)
ax.text(mid_keep_x, rasp_row_y + hh + 0.07, 'keep', ha='center', va='bottom',
        fontsize=6, color=OI_GREEN, fontweight='bold')
ax.text(mid_prune_x, rasp_row_y + hh + 0.07, 'prune', ha='center', va='bottom',
        fontsize=6, color='#CC0000', fontweight='bold')

# ── Key-swap annotations ──
# B: kept in Standard (pos=1) → pruned in RASP (pos=5)
b_std_pos  = list(std_order).index(1)
b_rasp_pos = list(rasp_order).index(1)
bx_std  = hx0 + b_std_pos  * (hw + hgap) + hw / 2
bx_rasp = hx0 + b_rasp_pos * (hw + hgap) + hw / 2
ax.annotate('B: high overlap\n     → pruned',
            xy=(bx_rasp, rasp_row_y + hh + 0.02),
            xytext=(bx_std + 0.05, std_row_y - 0.18),
            fontsize=6, color=OI_RED, ha='center', va='top', fontweight='bold',
            arrowprops=dict(arrowstyle='->,head_length=0.08,head_width=0.05',
                            color=OI_RED, lw=1.3,
                            connectionstyle='arc3,rad=0.3'),
            zorder=6)

# D: pruned in Standard (pos=3) → kept in RASP (pos=2)
d_std_pos  = list(std_order).index(3)
d_rasp_pos = list(rasp_order).index(3)
dx_std  = hx0 + d_std_pos  * (hw + hgap) + hw / 2
dx_rasp = hx0 + d_rasp_pos * (hw + hgap) + hw / 2
ax.annotate('D: low overlap\n  → protected',
            xy=(dx_rasp, rasp_row_y + hh + 0.02),
            xytext=(dx_std - 0.05, std_row_y - 0.18),
            fontsize=6, color=OI_GREEN, ha='center', va='top', fontweight='bold',
            arrowprops=dict(arrowstyle='->,head_length=0.08,head_width=0.05',
                            color=OI_GREEN, lw=1.3,
                            connectionstyle='arc3,rad=-0.3'),
            zorder=6)

# ── Legend (bottom of Stage 2) ──
leg_y = 0.18
leg_items = [
    (C_KEEP,    'Protected: Irreplaceable Scaffolding'),
    (C_PRUNE_R, 'Pruned: Redundant but Recoverable'),
    (C_PRUNE_U, 'Pruned: Unimportant'),
]
# Stack vertically
for i, (color, label) in enumerate(leg_items):
    ly = leg_y + (2 - i) * 0.20
    r = mpatches.Rectangle((s2cx - 1.15, ly), 0.12, 0.10,
                           fc=color, ec=C_DARK, lw=0.4, zorder=3)
    ax.add_patch(r)
    ax.text(s2cx - 1.15 + 0.17, ly + 0.05, label,
            va='center', fontsize=6.5, color=C_DARK, zorder=4)


# ══════════════════════════════════════════════════════════════════════
#  STAGE 3 — Two-Stage Recovery
# ══════════════════════════════════════════════════════════════════════
s3cx = S3_X + S3_W / 2

steps = [
    ('Pruned\nModel',     OI_RED,    2.40),
    ('SFT\nWarmup',       OI_ORANGE, 1.70),
    ('GRPO\nRLVR',        OI_BLUE,   1.00),
    ('Recovered\nModel',  OI_GREEN,  0.30),
]

bw, bh = 0.95, 0.38
for label, color, cy in steps:
    bx = s3cx - bw / 2
    by = cy - bh / 2
    # Light fill with coloured border
    rbox(bx, by, bw, bh, fc=color + '20', ec=color, lw=1.0, zorder=2, pad=0.03)
    ax.text(s3cx, cy, label, ha='center', va='center', fontsize=7.5,
            color=C_DARK, fontweight='bold', zorder=3, linespacing=1.1)

# Arrows between steps
for i in range(len(steps) - 1):
    y1 = steps[i][2] - bh / 2 - 0.04
    y2 = steps[i + 1][2] + bh / 2 + 0.04
    arrow(s3cx, y1, s3cx, y2, color=C_DARK, lw=1.2, hl=0.06, hw=0.04)

# Side annotations
ax.text(s3cx + bw / 2 + 0.04, steps[1][2], 'Format\n+ EOS',
        ha='left', va='center', fontsize=6, color=C_MID, style='italic',
        linespacing=1.2)
ax.text(s3cx + bw / 2 + 0.04, steps[2][2], 'Reasoning\nrecovery',
        ha='left', va='center', fontsize=6, color=C_MID, style='italic',
        linespacing=1.2)


# ══════════════════════════════════════════════════════════════════════
#  SAVE
# ══════════════════════════════════════════════════════════════════════
outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/figures'
os.makedirs(outdir, exist_ok=True)
pdf_path = os.path.join(outdir, 'fig1_rasp_pipeline.pdf')
png_path = os.path.join(outdir, 'fig1_rasp_pipeline.png')

fig.savefig(pdf_path, format='pdf')
fig.savefig(png_path, format='png')
plt.close()

print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')
