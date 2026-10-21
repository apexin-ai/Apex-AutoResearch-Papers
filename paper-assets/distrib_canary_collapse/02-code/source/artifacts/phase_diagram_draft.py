#!/usr/bin/env python3
"""Phase Diagram heatmap: α × T detection landscape with α_c(T) overlay."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
import numpy as np

# --- Data ---
alphas = [0.45, 0.50, 0.60, 0.75]
Ts = [5, 10, 15, 20, 25]

# Known data: (T, α) → detection rate (out of 8)
data = {
    (5, 0.45): 0, (5, 0.50): 0, (5, 0.60): 0, (5, 0.75): 0,
    (10, 0.45): 0, (10, 0.50): 6, (10, 0.60): 0, (10, 0.75): 6,
    (15, 0.45): 6, (15, 0.50): 6, (15, 0.60): 0, (15, 0.75): 6,
    (20, 0.45): 5, (20, 0.50): 6, (20, 0.60): 0, (20, 0.75): 6,
    (25, 0.45): 6, (25, 0.75): 6,
}
# Missing: T=25 α=0.50 and α=0.60★ — 2 experiments RUNNING

# Build matrix (T × α), NaN for missing
grid = np.full((len(Ts), len(alphas)), np.nan)
for i, T in enumerate(Ts):
    for j, a in enumerate(alphas):
        if (T, a) in data:
            grid[i, j] = data[(T, a)]

# --- α_c(T) theory curve ---
T_curve = np.linspace(4, 30, 200)
alpha_c = 0.193 + 75.68 * T_curve ** (-2.41)
alpha_c = np.clip(alpha_c, 0, 1.0)

# --- Figure ---
fig, ax = plt.subplots(figsize=(4.5, 3.2))

# Custom colormap: deep blue (0/8) → light blue (1-3) → orange (4-5) → red (6-8)
colors_list = ['#1A5276', '#2E86C1', '#85C1E9', '#F5B041', '#E74C3C', '#922B21']
nodes = [0.0, 0.125, 0.375, 0.625, 0.75, 1.0]
cmap = mcolors.LinearSegmentedColormap.from_list('detection', list(zip(nodes, colors_list)))

# Cell dimensions
cell_w = 1.0
cell_h = 1.0

for i, T in enumerate(Ts):
    for j, a in enumerate(alphas):
        val = grid[i, j]
        x = j
        y = i

        if np.isnan(val):
            # Missing data: darker gray with dense hatch
            rect = plt.Rectangle((x - 0.5, y - 0.5), cell_w, cell_h,
                                  facecolor='#C0C0C0', edgecolor='#888888',
                                  linewidth=0.5, hatch='xxx', zorder=1)
            ax.add_patch(rect)
            ax.text(x, y, '?', ha='center', va='center', fontsize=10,
                    color='#555555', fontweight='bold', zorder=3)
        else:
            rate = val / 8.0
            color = cmap(rate)
            rect = plt.Rectangle((x - 0.5, y - 0.5), cell_w, cell_h,
                                  facecolor=color, edgecolor='#666666',
                                  linewidth=0.5, zorder=1)
            ax.add_patch(rect)

            # Text: detection count — white on dark cells, dark on light
            txt_color = 'white' if (rate >= 0.5 or rate == 0) else '#1A1A1A'
            txt_kwargs = dict(ha='center', va='center', fontsize=10,
                              fontweight='bold', color=txt_color, zorder=3)
            if rate >= 0.5 or rate == 0:
                txt_kwargs['path_effects'] = [
                    pe.withStroke(linewidth=2.5, foreground='#0E3651' if rate == 0 else '#333333')]
            ax.text(x, y, f'{int(val)}/8', **txt_kwargs)

            # Sync-dip marker: diamond outline at α=0.60 (persistent)
            if a == 0.60 and val == 0:
                diamond = plt.Polygon(
                    [(x, y + 0.35), (x + 0.35, y), (x, y - 0.35), (x - 0.35, y)],
                    fill=False, edgecolor='#8E44AD', linewidth=2.0,
                    linestyle='-', zorder=4)
                ax.add_patch(diamond)

# Overlay α_c(T) curve — convert to grid coordinates
alpha_to_x = {a: j for j, a in enumerate(alphas)}
T_to_y = {T: i for i, T in enumerate(Ts)}

# Map continuous α_c values to x-coordinates via interpolation
x_curve = np.interp(alpha_c, alphas, range(len(alphas)))
y_curve = np.interp(T_curve, Ts, range(len(Ts)))

ax.plot(x_curve, y_curve, color='#2C3E50', linewidth=2.0, linestyle='--',
        zorder=5, label=r'$\alpha_c(T)$ theory')

# Add α_c label near the curve
idx_label = np.argmin(np.abs(T_curve - 12))
ax.annotate(r'$\alpha_c(T)$', xy=(x_curve[idx_label], y_curve[idx_label]),
            xytext=(x_curve[idx_label] + 0.6, y_curve[idx_label] - 0.3),
            fontsize=8, color='#2C3E50', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=1.0),
            zorder=6)

# Axes
ax.set_xticks(range(len(alphas)))
xlabels = [f'{a:.2f}' for a in alphas]
xlabels[2] = '0.60\n(sync-dip)'
ax.set_xticklabels(xlabels, fontsize=9)
ax.set_yticks(range(len(Ts)))
ax.set_yticklabels([str(T) for T in Ts], fontsize=9)
ax.set_xlabel(r'Contamination level $\alpha$', fontsize=10)
ax.set_ylabel(r'Observation length $T$', fontsize=10)

ax.set_xlim(-0.5, len(alphas) - 0.5)
ax.set_ylim(-0.5, len(Ts) - 0.5)

# Colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 8))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.04, ticks=[0, 2, 4, 6, 8])
cbar.set_label('PermG fwd (of 8)', fontsize=9)
cbar.ax.tick_params(labelsize=8)

# Legend entries
sync_patch = mpatches.Patch(facecolor='white', edgecolor='#8E44AD',
                             linewidth=1.5, label='Sync dip')
missing_patch = mpatches.Patch(facecolor='#C0C0C0', edgecolor='#888888',
                                hatch='xxx', label='Pending')
ax.legend(handles=[sync_patch, missing_patch], loc='upper left',
          fontsize=7, framealpha=0.9, edgecolor='#CCCCCC')

# Region labels — placed inside cells to avoid clipping
ax.text(0, 0.32, 'BLIND', fontsize=5.5, color='#5D6D7E', ha='center', va='center',
        fontstyle='italic', zorder=6)
ax.text(1, 1.35, 'ONSET', fontsize=5.5, color='#922B21',
        ha='center', va='center', fontstyle='italic', fontweight='bold', zorder=6)

plt.tight_layout()

out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_draft.pdf'
fig.savefig(out_path, dpi=300, bbox_inches='tight')
print(f'Saved: {out_path}')

# Also PNG for preview
png_path = out_path.replace('.pdf', '.png')
fig.savefig(png_path, dpi=200, bbox_inches='tight')
print(f'Preview: {png_path}')
