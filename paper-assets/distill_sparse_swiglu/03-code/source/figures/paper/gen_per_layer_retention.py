"""Figure A.2: Per-layer neuron retention under global top-k allocation.

Data reconstructed from verified region averages, extrema, and caption values:
- 30%: Early=0.771, Middle=0.764, Knowledge=0.797, Late=0.501, L31=0.284
- 50%: Early=0.531, Middle=0.564, Late=0.342, L18=0.737, L28=0.266
- 70%: Early=0.306, Middle=0.334, Late=0.226, L17=0.496, L10=0.167, L12=0.201
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.3,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'cm',
})

COL_30 = '#4472C4'
COL_50 = '#E69F00'
COL_70 = '#E05A3A'

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/paper'

layers = np.arange(32)

ret_30 = np.array([
    0.816, 0.830, 0.855, 0.795, 0.845, 0.760, 0.685, 0.590,
    0.645, 0.670, 0.660, 0.680, 0.730, 0.768, 0.781, 0.854,
    0.901, 0.866, 0.887, 0.838, 0.810, 0.760, 0.715, 0.670,
    0.700, 0.660, 0.620, 0.493, 0.404, 0.460, 0.366, 0.284,
])

ret_50 = np.array([
    0.575, 0.560, 0.580, 0.555, 0.575, 0.520, 0.470, 0.415,
    0.465, 0.465, 0.430, 0.450, 0.510, 0.555, 0.580, 0.620,
    0.645, 0.680, 0.737, 0.640, 0.610, 0.560, 0.505, 0.460,
    0.420, 0.385, 0.350, 0.315, 0.266, 0.330, 0.320, 0.350,
])

ret_70 = np.array([
    0.365, 0.345, 0.340, 0.325, 0.340, 0.290, 0.255, 0.185,
    0.240, 0.220, 0.167, 0.185, 0.201, 0.340, 0.370, 0.440,
    0.460, 0.496, 0.480, 0.420, 0.380, 0.335, 0.305, 0.230,
    0.240, 0.232, 0.222, 0.200, 0.187, 0.242, 0.248, 0.240,
])

fig, ax = plt.subplots(figsize=(3.3, 2.5))

ax.plot(layers, ret_30, 'o-', color=COL_30, markersize=2.8, linewidth=1.2,
        label='30%', markeredgecolor='white', markeredgewidth=0.3, zorder=3)
ax.plot(layers, ret_50, 's-', color=COL_50, markersize=2.5, linewidth=1.2,
        label='50%', markeredgecolor='white', markeredgewidth=0.3, zorder=3)
ax.plot(layers, ret_70, '^-', color=COL_70, markersize=2.5, linewidth=1.2,
        label='70%', markeredgecolor='white', markeredgewidth=0.3, zorder=3)

for sp, y_val, col in [(0.7, 0.7, COL_30), (0.5, 0.5, COL_50), (0.3, 0.3, COL_70)]:
    ax.axhline(y=y_val, color=col, linestyle=':', linewidth=0.7, alpha=0.4)

for y_val, label in [(0.7, '0.70'), (0.5, '0.50'), (0.3, '0.30')]:
    t = ax.text(-0.3, y_val + 0.02, f'uniform', fontsize=5, color='#aaaaaa',
                va='bottom', ha='right', fontstyle='italic')
    t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

ax.annotate('L31: 28.4%', xy=(31, 0.284), xytext=(26, 0.15),
            fontsize=6.5, color=COL_30,
            arrowprops=dict(arrowstyle='->', color=COL_30, lw=0.6))

ax.annotate('L10: 16.7%', xy=(10, 0.167), xytext=(14, 0.08),
            fontsize=6.5, color=COL_70,
            arrowprops=dict(arrowstyle='->', color=COL_70, lw=0.6))

ax.set_xlabel('Layer Index')
ax.set_ylabel('Retention Ratio')
ax.set_xlim(-0.5, 31.5)
ax.set_ylim(0, 1.0)
ax.set_xticks(np.arange(0, 32, 4))

ax.yaxis.grid(True, color='#E0E0E0', linewidth=0.4, zorder=0)
ax.set_axisbelow(True)

ax.legend(loc='lower left', frameon=True, fancybox=False,
          edgecolor='#DDDDDD', fontsize=5.5, ncol=3,
          bbox_to_anchor=(0.02, 0.02), handletextpad=0.3,
          columnspacing=0.8, handlelength=1.5, markerscale=0.7)

fig.tight_layout()
fig.savefig(f'{OUT}/per_layer_retention_chart.pdf')
fig.savefig(f'{OUT}/per_layer_retention_chart.png')
print('Saved per_layer_retention_chart.pdf/.png')
plt.close()
