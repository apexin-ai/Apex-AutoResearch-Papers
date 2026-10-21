#!/usr/bin/env python3
"""Figure 1: Cross-lingual Conflict Probing Pipeline Overview.

Three blocks left-to-right:
  1. Data Construction  2. Probing Framework  3. Confound Exclusion
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

# ── Global style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.06,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# ── Palette (as specified) ────────────────────────────────────────────────────
BG_BLUE   = '#E8F4FD'
BG_ORANGE = '#FFF3E0'
BG_GREEN  = '#E8F5E9'
C_EN      = '#0072B2'
C_ZH      = '#E69F00'
C_CHECK   = '#009E73'
C_CROSS   = '#CC79A7'
C_ARROW   = '#555555'
C_TXT     = '#222222'

# ── Canvas ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 3.8))
ax.set_xlim(0, 11)
ax.set_ylim(0, 3.8)
ax.axis('off')


# ── Helpers ───────────────────────────────────────────────────────────────────
def rbox(cx, cy, w, h, text, fc='white', ec='#BBBBBB', fs=8, lw=0.8,
         fw='normal', tc=C_TXT):
    ax.add_patch(FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle='round,pad=0.04', fc=fc, ec=ec, lw=lw, zorder=3))
    if text:
        ax.text(cx, cy, text, ha='center', va='center', fontsize=fs,
                color=tc, fontweight=fw, linespacing=1.15, zorder=4)


def varrow(x, y1, y2):
    ax.add_patch(FancyArrowPatch(
        (x, y1), (x, y2),
        arrowstyle='-|>', color=C_ARROW, lw=1.0, mutation_scale=8, zorder=2))


def harrow(x1, x2, y):
    ax.add_patch(FancyArrowPatch(
        (x1, y), (x2, y),
        arrowstyle='-|>', color=C_ARROW, lw=2.2, mutation_scale=16, zorder=6))


# ══════════════════════════════════════════════════════════════════════════════
# BLOCK BACKGROUNDS + TITLES + SECTION LABELS
# ══════════════════════════════════════════════════════════════════════════════
B1X, B1W = 0.12, 3.08
B2X, B2W = 3.68, 3.60
B3X, B3W = 7.78, 3.02
BY, BH   = 0.25, 3.30

block_defs = [
    (B1X, B1W, BG_BLUE,   'Data Construction',  u'§3.2 Data'),
    (B2X, B2W, BG_ORANGE, 'Probing Framework',  u'§3.4–3.5 Probing'),
    (B3X, B3W, BG_GREEN,  'Confound Exclusion', u'§3.6 Controls'),
]

for bx, bw, bg, title, sec in block_defs:
    ax.add_patch(FancyBboxPatch(
        (bx, BY), bw, BH,
        boxstyle='round,pad=0.10', fc=bg, ec='#AAAAAA', lw=1.0, zorder=0))
    cx = bx + bw / 2
    ax.text(cx, BY + BH - 0.15, title, ha='center', va='top',
            fontsize=11, fontweight='bold', color='#333333', zorder=1)
    ax.text(cx, BY + 0.10, sec, ha='center', va='bottom',
            fontsize=7.5, color='#777777', fontstyle='italic', zorder=1)

B1C = B1X + B1W / 2
B2C = B2X + B2W / 2
B3C = B3X + B3W / 2


# ══════════════════════════════════════════════════════════════════════════════
# BLOCK 1 — Data Construction
# ══════════════════════════════════════════════════════════════════════════════
bw1 = 2.58

items1 = [
    (2.92, 0.26, 'ConflictQA Dataset',                         '#E3F2FD', C_EN,     'normal'),
    (2.50, 0.30, 'Parametric Knowledge\nVerification (per-model)', 'white', '#BBBBBB', 'normal'),
    (2.04, 0.30, u'Translation (EN→ZH,\nvia Qwen3-8B)',      '#FFF8E1', C_ZH,    'normal'),
    (1.58, 0.30, 'COMET Back-translation\nValidation',            'white', '#BBBBBB', 'normal'),
    (1.08, 0.30, 'EN / ZH Parallel\nConflict Data',               '#E8EAF6', '#5C6BC0', 'bold'),
]

for cy, h, label, fc, ec, fw in items1:
    rbox(B1C, cy, bw1, h, label, fc=fc, ec=ec, fw=fw, fs=7.5)

for i in range(len(items1) - 1):
    y_from = items1[i][0] - items1[i][1] / 2
    y_to   = items1[i+1][0] + items1[i+1][1] / 2
    varrow(B1C, y_from, y_to)


# ══════════════════════════════════════════════════════════════════════════════
# BLOCK 2 — Probing Framework
# ══════════════════════════════════════════════════════════════════════════════
bw2 = 3.05

# Step A
rbox(B2C, 2.92, bw2, 0.28,
     'Residual Stream Extraction\n(last-token, all L layers)', fs=7.5)

# Step B
rbox(B2C, 2.48, bw2, 0.28,
     'Linear Probe Training\n(per-layer logistic regression)', fs=7.5)

varrow(B2C, 2.92 - 0.14, 2.48 + 0.14)

# Step C: 4-Direction Transfer Protocol — 2x2 mini-matrix
MAT_CY = 1.58
MAT_W, MAT_H = 2.65, 0.88

ax.add_patch(FancyBboxPatch(
    (B2C - MAT_W/2, MAT_CY - MAT_H/2), MAT_W, MAT_H,
    boxstyle='round,pad=0.05', fc='#FFFAF0', ec='#CCAA77', lw=0.8, zorder=3))

# Title above matrix
ax.text(B2C, MAT_CY + MAT_H/2 + 0.04, '4-Direction Transfer Protocol',
        ha='center', va='bottom', fontsize=7.5, fontweight='bold',
        color=C_TXT, zorder=5)

varrow(B2C, 2.48 - 0.14, MAT_CY + MAT_H/2 + 0.06)

# Column headers: Train EN / Train ZH
col1x = B2C - 0.38
col2x = B2C + 0.58
hdr_y = MAT_CY + 0.28
ax.text(col1x, hdr_y, 'Train EN', ha='center', va='center',
        fontsize=6.5, color=C_EN, fontweight='bold', zorder=5)
ax.text(col2x, hdr_y, 'Train ZH', ha='center', va='center',
        fontsize=6.5, color=C_ZH, fontweight='bold', zorder=5)

# Row labels: Test EN / Test ZH
row1y = MAT_CY + 0.04
row2y = MAT_CY - 0.22
lbl_x = B2C - 1.05
ax.text(lbl_x, row1y, 'Test EN', ha='center', va='center',
        fontsize=6.5, color=C_EN, fontweight='bold', zorder=5)
ax.text(lbl_x, row2y, 'Test ZH', ha='center', va='center',
        fontsize=6.5, color=C_ZH, fontweight='bold', zorder=5)

# Cell boxes
CW, CH_c = 0.68, 0.22
matrix_cells = [
    (col1x, row1y, u'EN→EN', '#E3F2FD', C_EN),      # mono
    (col2x, row1y, u'ZH→EN', '#FDE8EF', C_CROSS),   # cross
    (col1x, row2y, u'EN→ZH', '#FDE8EF', C_CROSS),   # cross
    (col2x, row2y, u'ZH→ZH', '#FFF8E1', C_ZH),      # mono
]
for cx, cy, txt, fc, ec in matrix_cells:
    ax.add_patch(FancyBboxPatch(
        (cx - CW/2, cy - CH_c/2), CW, CH_c,
        boxstyle='round,pad=0.02', fc=fc, ec=ec, lw=0.7, zorder=4))
    ax.text(cx, cy, txt, ha='center', va='center',
            fontsize=6.5, color=C_TXT, fontfamily='monospace', zorder=5)

# Thin divider lines
div_y = hdr_y - 0.10
left_edge  = B2C - MAT_W/2 + 0.10
right_edge = B2C + MAT_W/2 - 0.10
ax.plot([left_edge, right_edge], [div_y, div_y],
        color='#CCAA77', lw=0.5, zorder=4)
vert_x = lbl_x + 0.42
ax.plot([vert_x, vert_x], [div_y, row2y - CH_c/2 - 0.04],
        color='#CCAA77', lw=0.5, zorder=4)

# Step D: Bootstrap CI
rbox(B2C, 0.88, 2.40, 0.28, 'Bootstrap CI (n = 2000)', fs=7.5)
varrow(B2C, MAT_CY - MAT_H/2, 0.88 + 0.14)


# ══════════════════════════════════════════════════════════════════════════════
# BLOCK 3 — Confound Exclusion
# ══════════════════════════════════════════════════════════════════════════════
bw3 = 2.50
ch3 = 0.38
checks = [
    (2.45, 'COMET Tercile Ablation'),
    (1.85, 'Token Overlap Analysis'),
    (1.25, 'XNLI Non-conflict Baseline'),
]

for cy, label in checks:
    ax.add_patch(FancyBboxPatch(
        (B3C - bw3/2, cy - ch3/2), bw3, ch3,
        boxstyle='round,pad=0.04', fc='#F1F8F1', ec='#88BB88', lw=0.9, zorder=3))
    # Checkmark left-aligned
    ax.text(B3C - bw3/2 + 0.25, cy, u'✓', ha='center', va='center',
            fontsize=12, color=C_CHECK, fontweight='bold', zorder=4)
    # Label centred in remaining space
    label_cx = B3C - bw3/2 + 0.25 + (bw3 - 0.25) / 2
    ax.text(label_cx, cy, label, ha='center', va='center',
            fontsize=7.5, color=C_TXT, zorder=4)


# ══════════════════════════════════════════════════════════════════════════════
# INTER-BLOCK ARROWS
# ══════════════════════════════════════════════════════════════════════════════
harrow(B1X + B1W + 0.04, B2X - 0.04, 1.85)
harrow(B2X + B2W + 0.04, B3X - 0.04, 1.85)


# ══════════════════════════════════════════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════════════════════════════════════════
outdir = '/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/figures/paper'
os.makedirs(outdir, exist_ok=True)
fig.savefig(f'{outdir}/fig1_pipeline.pdf', format='pdf')
fig.savefig(f'{outdir}/fig1_pipeline.png', format='png')
plt.close(fig)
print('Done: fig1_pipeline.pdf + fig1_pipeline.png')
