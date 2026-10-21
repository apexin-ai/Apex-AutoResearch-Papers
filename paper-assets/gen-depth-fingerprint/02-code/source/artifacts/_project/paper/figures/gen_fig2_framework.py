#!/usr/bin/env python3
"""Generate Figure 2: Depth Fingerprinting Framework Overview. v4

Three-phase horizontal pipeline with embedded DDR feature response bars.
Fixed: ρ label overlap, color legend stacked, LOGO title position.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

def add_shadow(ax, x, y, w, h, pad=0.08, offset=(0.04, -0.04), alpha=0.08):
    """Add a subtle drop shadow behind a FancyBboxPatch."""
    shadow = FancyBboxPatch((x + offset[0], y + offset[1]), w, h,
                            boxstyle=f'round,pad={pad}',
                            facecolor='#000000', edgecolor='none',
                            alpha=alpha, zorder=-1)
    ax.add_patch(shadow)
    return shadow

C_DRIFT  = '#2471A3'
C_STAT   = '#D4A017'
C_INTER  = '#8B4557'
C_BG1    = '#FDF6F0'
C_BG2    = '#F0F4F8'
C_BG3    = '#F4F0F8'
C_ARROW  = '#555555'

fig = plt.figure(figsize=(7.2, 4.2))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 10.8)
ax.set_ylim(0, 5.7)
ax.axis('off')

# ═══════════════ PHASE BACKGROUNDS ═══════════════
phases = [
    (0.05, 2.50, C_BG1, '(a) Generation Chain'),
    (2.75, 4.65, C_BG2, '(b) Feature Extraction & Differential Depth Response'),
    (7.60, 3.10, C_BG3, '(c) Depth Classification'),
]
for x0, w, color, title in phases:
    add_shadow(ax, x0, 0.15, w, 5.30, pad=0.08, offset=(0.06, -0.06), alpha=0.06)
    bg = FancyBboxPatch((x0, 0.15), w, 5.30, boxstyle='round,pad=0.08',
                        facecolor=color, edgecolor='#BBBBBB', linewidth=0.8,
                        zorder=0)
    ax.add_patch(bg)
    ax.text(x0 + w/2, 5.25, title, ha='center', va='top',
            fontsize=7.5, fontweight='bold', color='#333333', zorder=1)

# ═══════════════ (a) GENERATION CHAIN ═══════════════
chain_x = 0.30
chain_y0 = 4.55
dy = -0.58

labels_a = ['gen-0  (human)', 'gen-1', 'gen-2', 'gen-3', 'gen-4']
colors_a = ['#27AE60', '#3498DB', '#E67E22', '#E74C3C', '#9B59B6']

for i, (lab, col) in enumerate(zip(labels_a, colors_a)):
    y = chain_y0 + i * dy
    box = FancyBboxPatch((chain_x, y - 0.20), 1.65, 0.40,
                         boxstyle='round,pad=0.06',
                         facecolor=col, edgecolor='white',
                         alpha=0.85, linewidth=0.8, zorder=2)
    ax.add_patch(box)
    ax.text(chain_x + 0.825, y, lab, ha='center', va='center',
            fontsize=7.5, color='white', fontweight='bold', zorder=3)
    if i < 4:
        mid = y + dy / 2
        ax.annotate('', xy=(chain_x + 0.825, y + dy + 0.22),
                    xytext=(chain_x + 0.825, y - 0.22),
                    arrowprops=dict(arrowstyle='->', color=C_ARROW,
                                   lw=1.0, shrinkA=1, shrinkB=1), zorder=2)
        ax.text(chain_x + 1.82, mid, 'G(·)', ha='left', va='center',
                fontsize=6.5, color='#777777', style='italic', zorder=3)
    ax.text(chain_x - 0.08, y, f'd={i}', ha='right', va='center',
            fontsize=6.5, color='#888888', zorder=3)

for j, line in enumerate(['8 generators · 5 families',
                           '0.6B – 8B parameters',
                           'τ = 0.7,  top-p = 0.9',
                           'max 256 new tokens']):
    ax.text(chain_x + 0.825, 0.80 - j * 0.24, line,
            ha='center', va='center', fontsize=6.5, color='#555555', zorder=3)

# ═══════════════ A → B arrow ═══════════════
ax.annotate('', xy=(2.95, 2.90), xytext=(2.60, 2.90),
            arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=1.8), zorder=5)

# ═══════════════ (b) FEATURE EXTRACTION + DDR ═══════════════
fx = 3.00

# Reference model
add_shadow(ax, fx + 0.20, 4.45, 2.50, 0.38, pad=0.06)
ref_box = FancyBboxPatch((fx + 0.20, 4.45), 2.50, 0.38,
                         boxstyle='round,pad=0.06',
                         facecolor='#ECF0F1', edgecolor='#95A5A6',
                         linewidth=1.0, zorder=2)
ax.add_patch(ref_box)
ax.text(fx + 1.45, 4.64, 'Pythia-410M (reference)', ha='center', va='center',
        fontsize=7.5, fontweight='bold', color='#2C3E50', zorder=3)

ax.annotate('', xy=(fx + 1.45, 4.10), xytext=(fx + 1.45, 4.32),
            arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=1.0), zorder=2)
ax.text(fx + 1.45, 4.02, 'per-token NLL:  $\\ell_1, \\ell_2, \\ldots, \\ell_n$',
        ha='center', va='center', fontsize=7.5, color='#555555', zorder=3)
ax.annotate('', xy=(fx + 1.45, 3.62), xytext=(fx + 1.45, 3.84),
            arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=1.0), zorder=2)

# Feature table
features = [
    ('hapax_ratio *',  -0.63, C_DRIFT),
    ('TTR *',          -0.61, C_DRIFT),
    ('entropy_mean',   -0.60, C_DRIFT),
    ('entropy_std',    -0.17, C_INTER),
    ('entropy_min',    -0.41, C_STAT),
    ('entropy_max',     0.08, C_STAT),
    ('tail_decay',      0.04, C_STAT),
]

table_y_top = 3.48
row_h = 0.34
name_x = fx + 0.20

# Bar geometry: ρ=0 line placed with room for labels on both sides
bar_zero_x = 5.80
bar_scale = 1.8   # reduced to avoid overlap

# ρ=0 reference line
ax.plot([bar_zero_x, bar_zero_x],
        [table_y_top + 0.15, table_y_top - 6 * row_h - 0.15],
        color='#BBBBBB', linewidth=0.7, zorder=1)
ax.text(bar_zero_x, table_y_top + 0.22, 'ρ = 0', ha='center', va='bottom',
        fontsize=5.5, color='#999999', zorder=3)

for i, (name, rho, color) in enumerate(features):
    y = table_y_top - i * row_h

    # Feature name
    ax.text(name_x, y, name, ha='left', va='center',
            fontsize=6.8, fontfamily='monospace', color='#333333', zorder=3)

    # Bar
    bar_w = abs(rho) * bar_scale
    bx = bar_zero_x - bar_w if rho < 0 else bar_zero_x
    bar = FancyBboxPatch((bx, y - 0.09), bar_w, 0.18,
                         boxstyle='round,pad=0.02',
                         facecolor=color, alpha=0.70,
                         edgecolor='none', zorder=2)
    ax.add_patch(bar)

    # ρ text outside bar
    rho_str = f'{rho:+.2f}'
    if rho < 0:
        ax.text(bx - 0.06, y, rho_str, ha='right', va='center',
                fontsize=6.5, color=color, fontweight='bold', zorder=3)
    else:
        ax.text(bx + bar_w + 0.06, y, rho_str, ha='left', va='center',
                fontsize=6.5, color=color, fontweight='bold', zorder=3)

# Group separators
for sep_idx in [2.5, 3.5]:
    y = table_y_top - sep_idx * row_h
    ax.plot([name_x, bar_zero_x + 0.50], [y, y],
            color='#CCCCCC', linewidth=0.5, linestyle='--', zorder=1)

# Group labels (right of bars, stacked vertically within each group)
glabel_x = bar_zero_x + 0.55
group_defs = [
    (0, 2, C_DRIFT, 'Drifting'),
    (3, 3, C_INTER, 'Intermediate'),
    (4, 6, C_STAT,  'Near-stationary'),
]
for si, ei, gc, gl in group_defs:
    y_mid = (table_y_top - si * row_h + table_y_top - ei * row_h) / 2
    # Small colored square + label
    sq = FancyBboxPatch((glabel_x, y_mid - 0.07), 0.14, 0.14,
                        boxstyle='round,pad=0.01',
                        facecolor=gc, alpha=0.7, edgecolor='none', zorder=2)
    ax.add_patch(sq)
    ax.text(glabel_x + 0.20, y_mid, gl, ha='left', va='center',
            fontsize=6, color=gc, fontweight='bold', zorder=3)

# Footnote
ax.text(name_x, table_y_top - 7.1 * row_h + 0.12,
        '* surface features (no reference model needed)',
        ha='left', va='center', fontsize=5.5, color='#888888',
        style='italic', zorder=3)

# ═══════════════ B → C arrow ═══════════════
ax.annotate('', xy=(7.75, 2.90), xytext=(7.40, 2.90),
            arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=1.8), zorder=5)
ax.text(7.57, 3.08, '7 features', ha='center', va='bottom',
        fontsize=6, color=C_ARROW, zorder=5)

# ═══════════════ (c) DEPTH CLASSIFICATION ═══════════════
cx = 7.80

# XGBoost box
add_shadow(ax, cx, 4.45, 2.65, 0.38, pad=0.06)
xgb = FancyBboxPatch((cx, 4.45), 2.65, 0.38,
                     boxstyle='round,pad=0.06',
                     facecolor='#ECF0F1', edgecolor='#95A5A6',
                     linewidth=1.0, zorder=2)
ax.add_patch(xgb)
ax.text(cx + 1.325, 4.64, 'XGBoost Classifier', ha='center', va='center',
        fontsize=7.5, fontweight='bold', color='#2C3E50', zorder=3)

ax.annotate('', xy=(cx + 1.325, 4.05), xytext=(cx + 1.325, 4.32),
            arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=1.0), zorder=2)

# Output class boxes
out_y = 3.85
for j, (lab, col) in enumerate([('gen-0', '#27AE60'),
                                  ('gen-1', '#3498DB'),
                                  ('gen-2+', '#E67E22')]):
    bx = cx + 0.05 + j * 0.87
    box = FancyBboxPatch((bx, out_y - 0.20), 0.78, 0.38,
                         boxstyle='round,pad=0.05',
                         facecolor=col, edgecolor='white',
                         alpha=0.85, linewidth=0.8, zorder=2)
    ax.add_patch(box)
    ax.text(bx + 0.39, out_y, lab, ha='center', va='center',
            fontsize=8, color='white', fontweight='bold', zorder=3)

# Results
results = [
    ('LOGO (8 generators)', '', True),
    ('  Binary F1 (1 vs 2+)', '0.694', False),
    ('  3-class macro F1', '0.762', False),
    ('', '', False),
    ('Cross-model (5 generators)', '', True),
    ('  Binary F1 (1 vs 2+)', '0.830', False),
    ('  3-class macro F1', '0.789', False),
]
ry = 3.25
for k, (lab, val, hdr) in enumerate(results):
    y = ry - k * 0.25
    if hdr:
        ax.text(cx + 0.05, y, lab, ha='left', va='center',
                fontsize=6.5, color='#444444', fontweight='bold', zorder=3)
    elif lab:
        ax.text(cx + 0.05, y, lab, ha='left', va='center',
                fontsize=6.5, color='#555555', zorder=3)
        ax.text(cx + 2.55, y, val, ha='right', va='center',
                fontsize=7.5, color='#2C3E50', fontweight='bold', zorder=3)

# LOGO mini-diagram
logo_x = cx + 0.05
logo_y = 0.85
ax.text(logo_x + 1.0, logo_y + 0.58, 'Leave-One-Generator-Out CV',
        ha='center', va='center',
        fontsize=6.0, color='#555555', fontweight='bold', zorder=3)

gen_short = ['Py-2.8', 'Py-1B', 'OLMo', 'Q-1.7',
             'Q-0.6', 'Q-8B', 'Llama', 'Mistral']
for g in range(8):
    gx = logo_x + (g % 4) * 0.55
    gy = logo_y + 0.12 - (g // 4) * 0.36
    is_test = (g == 7)
    fc = '#E74C3C' if is_test else '#D5D8DC'
    box = FancyBboxPatch((gx, gy - 0.12), 0.48, 0.24,
                         boxstyle='round,pad=0.03',
                         facecolor=fc, edgecolor='white',
                         alpha=0.85, linewidth=0.5, zorder=2)
    ax.add_patch(box)
    ax.text(gx + 0.24, gy, gen_short[g], ha='center', va='center',
            fontsize=4.5, color='white' if is_test else '#444444',
            fontweight='bold' if is_test else 'normal', zorder=3)

# LOGO legend
ax.plot([logo_x + 2.28, logo_x + 2.43], [logo_y + 0.12, logo_y + 0.12],
        color='#D5D8DC', linewidth=5, solid_capstyle='round', zorder=2)
ax.text(logo_x + 2.48, logo_y + 0.12, 'train (7)', ha='left', va='center',
        fontsize=5.5, color='#777777', zorder=3)
ax.plot([logo_x + 2.28, logo_x + 2.43], [logo_y - 0.12, logo_y - 0.12],
        color='#E74C3C', linewidth=5, solid_capstyle='round', zorder=2)
ax.text(logo_x + 2.48, logo_y - 0.12, 'test (1)', ha='left', va='center',
        fontsize=5.5, color='#E74C3C', zorder=3)

# ═══════════════ Save ═══════════════
outdir = os.path.dirname(os.path.abspath(__file__))
for fmt in ['pdf', 'png']:
    fig.savefig(os.path.join(outdir, f'fig2_framework.{fmt}'), dpi=300)
    print(f'Saved fig2_framework.{fmt}')
plt.close()
