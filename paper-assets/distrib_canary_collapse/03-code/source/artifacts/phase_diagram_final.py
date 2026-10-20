#!/usr/bin/env python3
"""Phase Diagram heatmap (final): α × T detection landscape with α_c(T) overlay."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# ── Data (20/20 complete) ──
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

# ── α_c(T) theory curve (D102 Cross-T, α_∞=0) ──
T_curve = np.linspace(4, 30, 500)
alpha_c = 130.39 * T_curve ** (-2.083)
alpha_c = np.clip(alpha_c, 0, 1.0)

# ── Figure ──
fig, ax = plt.subplots(figsize=(3.5, 3.0))

# Colormap: deep blue (0) → light blue → orange → red (8)
cmap = mcolors.LinearSegmentedColormap.from_list('det',
    list(zip([0, 0.125, 0.375, 0.625, 0.75, 1.0],
             ['#1A5276', '#2E86C1', '#85C1E9', '#F5B041', '#E74C3C', '#922B21'])))

for i, T in enumerate(Ts):
    for j, a in enumerate(alphas):
        val = int(grid[i, j])
        x, y = j, i
        rate = val / 8.0

        rect = plt.Rectangle((x - 0.5, y - 0.5), 1, 1,
                              facecolor=cmap(rate), edgecolor='#999999',
                              linewidth=0.3, zorder=1)
        ax.add_patch(rect)

        # Cell text
        dark_bg = rate >= 0.625 or rate == 0
        txt_color = 'white' if dark_bg else '#1A1A1A'
        effects = ([pe.withStroke(linewidth=2.5,
                    foreground='#000000' if rate == 0 else '#444444')]
                   if dark_bg else [])
        ax.text(x, y, f'{val}/8', ha='center', va='center', fontsize=8.5,
                fontweight='bold', color=txt_color, zorder=8,
                path_effects=effects or None)

        # Sync-dip diamond: α=0.60 cells with 0/8
        if a == 0.60 and val == 0:
            d = 0.33
            ax.add_patch(plt.Polygon(
                [(x, y+d), (x+d, y), (x, y-d), (x-d, y)],
                fill=False, edgecolor='#8E44AD', linewidth=1.5, zorder=4))

        # Dissolution ★: T=25 α=0.60 recovered from sync-dip
        if T == 25 and a == 0.60:
            ax.plot(x + 0.30, y + 0.30, marker='*', markersize=9,
                    color='#DAA520', markeredgecolor='#333333',
                    markeredgewidth=0.4, zorder=5, clip_on=False)


# ── α_c(T) theory curve ──
mask = (alpha_c >= alphas[0]) & (alpha_c <= alphas[-1])
x_crv = np.interp(alpha_c, alphas, range(len(alphas)))
y_crv = np.interp(T_curve, Ts, range(len(Ts)))
ax.plot(x_crv[mask], y_crv[mask], color='#2C3E50', linewidth=1.8,
        linestyle='--', zorder=5, solid_capstyle='round', dash_capstyle='round')

# ── Axes ──
ax.set_xticks(range(len(alphas)))
ax.set_xticklabels([f'{a:.2f}' for a in alphas])
ax.set_yticks(range(len(Ts)))
ax.set_yticklabels([str(T) for T in Ts])
ax.set_xlabel(r'Contamination strength $\alpha$')
ax.set_ylabel(r'Observation window $T$')
ax.set_xlim(-0.5, len(alphas) - 0.5)
ax.set_ylim(-0.5, len(Ts) - 0.5)

# ── Colorbar ──
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 8))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.04, ticks=[0, 2, 4, 6, 8])
cbar.set_label('Detection count (of 8)', fontsize=9)
cbar.ax.tick_params(labelsize=8)

# ── Legend ──
handles = [
    plt.Line2D([], [], color='#2C3E50', linewidth=1.8, linestyle='--',
               label=r'$\alpha_c(T)$ theory'),
    plt.Line2D([], [], marker='D', color='#8E44AD', markersize=5,
               linestyle='None', markerfacecolor='none',
               markeredgecolor='#8E44AD', markeredgewidth=1.5,
               label='Sync-dip ($\\alpha$=0.60)'),
    plt.Line2D([], [], marker='*', color='#DAA520', markersize=8,
               linestyle='None', markeredgecolor='#333333',
               markeredgewidth=0.4, label='Dissolution'),
]
ax.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.45, -0.18),
          ncol=3, framealpha=0.92, edgecolor='#CCCCCC',
          handlelength=1.5, handletextpad=0.4,
          borderpad=0.3, labelspacing=0.3, columnspacing=1.0)

plt.tight_layout(rect=[0, 0.02, 1, 1])

base = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts'
fig.savefig(f'{base}/phase_diagram_final.pdf', dpi=300, bbox_inches='tight')
fig.savefig(f'{base}/phase_diagram_final.png', dpi=300, bbox_inches='tight')
print('Saved: phase_diagram_final.pdf + .png')
