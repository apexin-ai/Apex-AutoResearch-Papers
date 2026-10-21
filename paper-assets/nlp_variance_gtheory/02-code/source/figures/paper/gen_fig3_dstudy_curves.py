#!/usr/bin/env python3
"""Figure 3: D-Study Projection Curves — G coefficient vs. number of benchmark items."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

BLUE = '#2166ac'
RED  = '#e41a1c'
GRAY = '#666666'

# ---------------------------------------------------------------------------
# D-study G coefficient: G(n) = n / (n + C), where C = sigma_delta / sigma_p
#
# Variance components from exp-001 single-model G-study (Henderson I, Llama-3.1-8B):
#   item_id (sigma_p): 58.4%  |  residual 23.1%  |  prompt:item 5.5%
#   seed:item 4.7%  |  precision:item 3.3%  |  temp:item 2.9%  |  ordering:item 0.8%
#
# Single-model design: 1,296 conditions/item (3 prec × 6 prompt × 6 seed × 3 temp × 4 ord)
# C = sigma_rel / sigma_p; solved from n(G≥0.80) = C / (1/0.80 - 1) = 4C
# ---------------------------------------------------------------------------
C_MULTI  = 13.75   # multi-facet (1,296 conditions/item); n(G≥0.80) = 55
C_SINGLE = 138.0   # single-condition (1 condition/item); n(G≥0.80) = 552

n = np.arange(1, 701)
G_m = n / (n + C_MULTI)
G_s = n / (n + C_SINGLE)

N_M80 = 55
N_S80 = 552
N_IRT = 116
G_IRT = N_IRT / (N_IRT + C_SINGLE)

stroke = [pe.withStroke(linewidth=2.5, foreground='white')]

fig, ax = plt.subplots(figsize=(3.5, 2.8))

# Shaded region below G = 0.80
ax.fill_between([0, 700], 0, 0.80, color='#f4f4f4', zorder=0)

# Threshold line
ax.axhline(0.80, color=GRAY, ls='--', lw=1.0, alpha=0.7, zorder=2)

# IRT vertical line
ax.axvline(N_IRT, color='#bbbbbb', ls=':', lw=0.8, zorder=1)

# Curves
ax.plot(n, G_m, color=BLUE, lw=1.5, solid_capstyle='round', zorder=3)
ax.plot(n, G_s, color=RED, lw=1.5, ls='--', zorder=3)

# Intersection dots
for nx, c in [(N_M80, BLUE), (N_S80, RED)]:
    ax.plot(nx, 0.80, 'o', color=c, ms=4, zorder=5, mec='white', mew=0.6)

# IRT diamond
ax.plot(N_IRT, G_IRT, 'D', color='#888888', ms=3.5, zorder=5)

# --- Direct curve labels (no legend) ---
t = ax.text(320, 0.965, 'Multi-facet', fontsize=7, color=BLUE,
            ha='center', va='bottom', fontstyle='italic')
t.set_path_effects(stroke)

t = ax.text(480, 0.665, 'Single-condition', fontsize=7, color=RED,
            ha='center', va='top', fontstyle='italic')
t.set_path_effects(stroke)

# --- Annotations ---

t = ax.annotate('55 items', xy=(55, 0.80), xytext=(170, 0.63),
                fontsize=7, color=BLUE, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=0.8),
                ha='left', zorder=6)
t.set_path_effects(stroke)

t = ax.annotate('552 items', xy=(552, 0.80), xytext=(430, 0.92),
                fontsize=7, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=0.8),
                ha='right', zorder=6)
t.set_path_effects(stroke)

t = ax.annotate(f'IRT rec. → G = {G_IRT:.2f}',
                xy=(N_IRT, G_IRT), xytext=(240, 0.33),
                fontsize=6.5, color='#777777',
                arrowprops=dict(arrowstyle='->', color='#aaaaaa', lw=0.7),
                zorder=6)
t.set_path_effects(stroke)

t = ax.text(460, 0.82, 'Reliability threshold (G = 0.80)',
            fontsize=6.5, color=GRAY, ha='center', va='bottom',
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

ax.text(350, 0.06, 'Below reliability threshold',
        fontsize=6.5, color='#cccccc', ha='center', fontstyle='italic')

# --- Axes ---
ax.set_xlim(0, 700)
ax.set_ylim(0, 1.0)
ax.set_xlabel('Number of items')
ax.set_ylabel('Generalizability coefficient (G)')
ax.set_xticks([0, 100, 200, 300, 400, 500, 600, 700])
ax.set_yticks(np.arange(0, 1.1, 0.2))

ax.yaxis.grid(True, alpha=0.12, lw=0.4)

plt.tight_layout()

# --- Save ---
outdir = os.path.dirname(os.path.abspath(__file__))
for ext in ('pdf', 'png'):
    fig.savefig(os.path.join(outdir, f'fig3_dstudy_curves.{ext}'))
plt.close()

# Verification
print('Saved fig3_dstudy_curves.pdf + .png')
for label, ni, C in [('Multi@55', 55, C_MULTI), ('Multi@200', 200, C_MULTI),
                      ('Single@200', 200, C_SINGLE), ('Single@552', 552, C_SINGLE)]:
    print(f'  {label}: G = {ni/(ni+C):.3f}')
print(f'  IRT@116 (single): G = {G_IRT:.3f}')
print(f'  Ratio: {N_S80/N_M80:.1f}x')
