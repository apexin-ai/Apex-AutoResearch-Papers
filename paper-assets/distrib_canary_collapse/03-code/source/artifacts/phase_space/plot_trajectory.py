import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(SCRIPT_DIR, "trajectory_data.json")) as f:
    raw = json.load(f)

data = {}
for alpha_str, v in raw.items():
    data[float(alpha_str)] = v

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman'],
    'font.size': 8,
    'axes.labelsize': 10,
    'legend.fontsize': 7.5,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'axes.linewidth': 0.6,
    'lines.linewidth': 1.1,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
})

fig, ax = plt.subplots(1, 1, figsize=(7.0, 4.5))

cmap = plt.cm.coolwarm
norm = Normalize(vmin=0.0, vmax=1.0)

plot_alphas = sorted(data.keys())

# Emphasize key trajectories
key_alphas = {0.0, 0.25, 0.50, 0.55, 0.75, 1.00}

for alpha in plot_alphas:
    v = data[alpha]
    x = v['e']
    y = v['d']
    color = cmap(norm(alpha))
    is_key = alpha in key_alphas
    lw = 1.6 if is_key else 0.9
    line_alpha = 0.9 if is_key else 0.55

    ax.plot(x, y, color=color, linewidth=lw, alpha=line_alpha, zorder=2 if is_key else 1,
            solid_capstyle='round')

    # Direction arrow at ~30%
    n = len(x)
    idx = max(1, int(n * 0.3))
    if idx < n and is_key:
        ax.annotate('', xy=(x[idx], y[idx]),
                    xytext=(x[idx-1], y[idx-1]),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.0,
                                    mutation_scale=9, shrinkA=0, shrinkB=0),
                    zorder=3)

    # Start (gen 0): circle
    ms = 35 if is_key else 18
    ax.scatter(x[0], y[0], color=color, marker='o', s=ms, zorder=5,
               edgecolors='k', linewidths=0.35)
    # End: square
    ax.scatter(x[-1], y[-1], color=color, marker='s', s=ms, zorder=5,
               edgecolors='k', linewidths=0.35)

# Endpoint labels with manual positions
label_config = {
    0.0:  {'ox': 0.04, 'oy': 0.0005, 'ha': 'left'},
    0.25: {'ox': 0.04, 'oy': -0.0015, 'ha': 'left'},
    0.50: {'ox': 0.04, 'oy': 0.0015, 'ha': 'left'},
    0.55: {'ox': 0.04, 'oy': -0.003, 'ha': 'left'},
    0.75: {'ox': -0.20, 'oy': 0.003, 'ha': 'right'},
    1.00: {'ox': 0.04, 'oy': 0.003, 'ha': 'left'},
}
for alpha in key_alphas:
    if alpha not in data:
        continue
    v = data[alpha]
    x_end, y_end = v['e'][-1], v['d'][-1]
    color = cmap(norm(alpha))
    cfg = label_config[alpha]
    ax.annotate(f'$\\alpha$={alpha:.2f}', xy=(x_end, y_end),
                xytext=(x_end + cfg['ox'], y_end + cfg['oy']),
                fontsize=7, color=color, fontweight='bold',
                ha=cfg['ha'], va='center')

# --- Phase boundary ---
# Sharp bifurcation between alpha=0.25 (entropy stays ~3.0) and alpha=0.30 (drops to ~2.5)
ax.axvspan(2.70, 2.96, alpha=0.05, color='#666666', zorder=0)
ax.text(2.83, 0.055, 'phase boundary\n($\\alpha_c \\approx 0.30$)',
        fontsize=7, color='#555555', style='italic', ha='center', va='bottom',
        bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                 edgecolor='#aaaaaa', linewidth=0.4, alpha=0.9))

# --- Sync dip shading ---
sync_alphas = [a for a in data.keys() if 0.54 <= a <= 0.66]
if sync_alphas:
    all_x, all_y = [], []
    for a in sync_alphas:
        all_x.extend(data[a]['e'][1:])
        all_y.extend(data[a]['d'][1:])
    pad_x, pad_y = 0.03, 0.0015
    x_min, x_max = min(all_x) - pad_x, max(all_x) + pad_x
    y_min, y_max = min(all_y) - pad_y, max(all_y) + pad_y
    rect = mpatches.FancyBboxPatch(
        (x_min, y_min), x_max - x_min, y_max - y_min,
        boxstyle="round,pad=0.01", facecolor='#F5EDE0', alpha=0.5,
        edgecolor='#AA8844', linewidth=0.5, linestyle='--', zorder=0)
    ax.add_patch(rect)
    ax.text(x_max + 0.01, (y_min + y_max)/2, 'sync dip\n$\\alpha \\in [0.55, 0.65]$',
            fontsize=6.5, color='#886633', style='italic', va='center', ha='left')

# --- Sweep direction indicator ---
ax.annotate('', xy=(1.4, 0.068), xytext=(2.8, 0.094),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.15',
                           color='#999999', lw=1.3, alpha=0.25))
ax.text(1.85, 0.087, 'increasing $\\alpha$', fontsize=7.5, color='#999999',
        style='italic', ha='center', va='center', rotation=-12)

# Colorbar
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, shrink=0.82, aspect=28, pad=0.015)
cbar.set_label('$\\alpha$ (synthetic data fraction)', fontsize=9)
cbar.ax.tick_params(labelsize=7)

ax.set_xlabel('Token Entropy')
ax.set_ylabel('Distinct-1')
ax.grid(True, alpha=0.12, linewidth=0.3)

legend_elements = [
    Line2D([0], [0], marker='o', color='none', markersize=5.5,
           markerfacecolor='gray', markeredgecolor='k', markeredgewidth=0.4,
           label='Gen 0 (start)'),
    Line2D([0], [0], marker='s', color='none', markersize=5.5,
           markerfacecolor='gray', markeredgecolor='k', markeredgewidth=0.4,
           label='Gen 10 (end)'),
    Line2D([0], [0], color='gray', linewidth=1.0, label='Trajectory (gen 0$\\to$10)'),
]
ax.legend(handles=legend_elements, loc='lower left', framealpha=0.92,
          edgecolor='none', borderpad=0.6)

ax.set_xlim(1.1, 3.40)
ax.set_ylim(0.052, 0.105)

plt.tight_layout(pad=0.5)
fig.savefig(os.path.join(SCRIPT_DIR, "fig_trajectory.pdf"), bbox_inches='tight')
fig.savefig(os.path.join(SCRIPT_DIR, "fig_trajectory.png"), bbox_inches='tight')
print("Saved fig_trajectory.pdf and fig_trajectory.png")
