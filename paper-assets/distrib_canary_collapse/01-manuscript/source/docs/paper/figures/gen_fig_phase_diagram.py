#!/usr/bin/env python3
"""Phase Diagram heatmap: α × T detection landscape with α_c(T) overlay.
Optimized for EMNLP 2026 top-conference visual quality."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
})

# ── Data (20/20 complete, Pythia-410M fp32 PermG direction-checked) ──
alphas = [0.45, 0.50, 0.60, 0.75]
Ts = [5, 10, 15, 20, 25]

data = {
    (5, 0.45): 0, (5, 0.50): 0, (5, 0.60): 0, (5, 0.75): 0,
    (10, 0.45): 0, (10, 0.50): 6, (10, 0.60): 0, (10, 0.75): 6,
    (15, 0.45): 6, (15, 0.50): 6, (15, 0.60): 0, (15, 0.75): 6,
    (20, 0.45): 5, (20, 0.50): 6, (20, 0.60): 0, (20, 0.75): 6,
    (25, 0.45): 6, (25, 0.50): 6, (25, 0.60): 5, (25, 0.75): 6,
}

grid = np.full((len(Ts), len(alphas)), np.nan)
for i, T in enumerate(Ts):
    for j, a in enumerate(alphas):
        grid[i, j] = data[(T, a)]

# ── α_c(T) theory curve ──
T_curve = np.linspace(4, 30, 500)
alpha_c = 130.39 * T_curve ** (-2.083)
alpha_c = np.clip(alpha_c, 0, 1.0)

# ── Colormap: softened YlOrRd (lighter, less saturated) ──
from matplotlib.colors import LinearSegmentedColormap
_base = plt.cm.YlOrRd(np.linspace(0.05, 0.75, 256))
_base = _base * 0.92 + 0.08  # lighten
cmap = LinearSegmentedColormap.from_list('soft_ylorrd', _base)

# ── Figure ──
fig, ax = plt.subplots(figsize=(3.4, 2.8))

CELL_PAD = 0.48

for i, T in enumerate(Ts):
    for j, a in enumerate(alphas):
        val = int(grid[i, j])
        rate = val / 8.0

        rect = plt.Rectangle(
            (j - CELL_PAD, i - CELL_PAD), CELL_PAD * 2, CELL_PAD * 2,
            facecolor=cmap(rate), edgecolor='white', linewidth=1.0,
            zorder=1, joinstyle='round',
        )
        ax.add_patch(rect)

        # Cell text — semibold with subtle stroke for readability
        is_dark = rate >= 0.75
        txt_color = '#FFFFFF' if is_dark else '#333333'
        stroke_col = '#00000033' if is_dark else '#FFFFFF33'
        ax.text(j, i, f'{val}/8', ha='center', va='center',
                fontsize=9, fontweight='semibold', color=txt_color, zorder=8,
                path_effects=[pe.withStroke(linewidth=1.5, foreground=stroke_col)])

        # Sync-dip diamond: α=0.60 cells with 0/8
        if a == 0.60 and val == 0:
            d = 0.28
            diamond = plt.Polygon(
                [(j, i + d), (j + d, i), (j, i - d), (j - d, i)],
                fill=False, edgecolor='#8B6BB0', linewidth=1.4,
                linestyle='-', zorder=6)
            ax.add_patch(diamond)

        # Dissolution star: T=25 α=0.60
        if T == 25 and a == 0.60:
            ax.plot(j + 0.26, i + 0.26, marker='*', markersize=9,
                    color='#D4A843', markeredgecolor='#6B5A30',
                    markeredgewidth=0.5, zorder=7, clip_on=False)

# ── α_c(T) theory curve ──
mask = (alpha_c >= alphas[0] - 0.02) & (alpha_c <= alphas[-1] + 0.02)
x_crv = np.interp(alpha_c, alphas, range(len(alphas)))
y_crv = np.interp(T_curve, Ts, range(len(Ts)))
valid = mask & (x_crv >= -0.5) & (x_crv <= len(alphas) - 0.5)
ax.plot(x_crv[valid], y_crv[valid], color='#1A1A1A', linewidth=1.3,
        linestyle='--', zorder=5, solid_capstyle='round',
        dash_capstyle='round', dashes=(4, 3))

# ── Axes ──
ax.set_xticks(range(len(alphas)))
ax.set_xticklabels([f'{a:.2f}' for a in alphas])
ax.set_yticks(range(len(Ts)))
ax.set_yticklabels([str(T) for T in Ts])
ax.set_xlabel(r'Contamination strength $\alpha$', labelpad=4)
ax.set_ylabel(r'Observation window $T$', labelpad=4)
ax.set_xlim(-0.5, len(alphas) - 0.5)
ax.set_ylim(-0.5, len(Ts) - 0.5)
ax.tick_params(length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# ── Colorbar ──
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 8))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.06,
                     ticks=[0, 2, 4, 6, 8], aspect=18)
cbar.set_label('Detection count (of 8)', fontsize=8, labelpad=6)
cbar.ax.tick_params(labelsize=7.5, length=2)
cbar.outline.set_linewidth(0.3)
cbar.outline.set_edgecolor('#AAAAAA')

# ── Legend ──
handles = [
    plt.Line2D([], [], color='#1A1A1A', linewidth=1.2, linestyle='--',
               dashes=(4, 3), label=r'$\alpha_c(T)$ theory'),
    plt.Line2D([], [], marker='D', color='#8B6BB0', markersize=4.5,
               linestyle='None', markerfacecolor='none',
               markeredgecolor='#8B6BB0', markeredgewidth=1.2,
               label=r'Sync-dip ($\alpha{=}0.60$)'),
    plt.Line2D([], [], marker='*', color='#D4A843', markersize=7,
               linestyle='None', markeredgecolor='#6B5A30',
               markeredgewidth=0.4, label='Dissolution'),
]
leg = ax.legend(handles=handles, loc='upper center',
                bbox_to_anchor=(0.45, -0.15), ncol=3,
                framealpha=0.0, edgecolor='none',
                handlelength=1.8, handletextpad=0.4,
                borderpad=0.2, labelspacing=0.3, columnspacing=0.8,
                fontsize=7.5)

plt.tight_layout(rect=[0, 0.04, 1, 1])

for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_phase_diagram.{fmt}', dpi=300)
plt.close()
print(f'Saved: {OUT}/fig_phase_diagram.pdf + .png')
