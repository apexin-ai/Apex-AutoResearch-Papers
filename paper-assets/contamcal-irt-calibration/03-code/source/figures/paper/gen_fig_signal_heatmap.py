import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.colors import TwoSlopeNorm

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3.5,
    'ytick.major.size': 3.5,
    'lines.linewidth': 1.8,
    'grid.alpha': 0.3,
    'grid.linewidth': 0.5,
    'grid.linestyle': '--',
})

signals = ['S1: Embedding', 'S2: Min-K++', 'S4: Self-Critique']
benchmarks = ['MMLU', 'GSM8K', 'ARC']

auc_d005 = np.array([
    [0.9530, 0.9882, 0.9950],
    [0.4655, 0.4649, 0.4659],
    [0.5165, 0.4947, 0.4325],
])

cohens_d_d100 = np.array([
    [4.1622, 2.8331, 3.7993],
    [-1.2203, -2.6660, -2.0480],
    [0.4673, 0.2034, 0.6708],
])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.5))

# Panel A: AUC heatmap
im1 = ax1.imshow(auc_d005, cmap='YlOrRd', vmin=0.4, vmax=1.0, aspect='auto')
ax1.set_xticks(range(3))
ax1.set_xticklabels(benchmarks)
ax1.set_yticks(range(3))
ax1.set_yticklabels(signals)
ax1.set_title('Item-Level Detection (AUC)')

for i in range(3):
    for j in range(3):
        val = auc_d005[i, j]
        color = 'white' if val > 0.75 else 'black'
        ax1.text(j, i, f'{val:.2f}', ha='center', va='center', color=color, fontsize=9.5, fontweight='bold')

cbar1 = fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)
cbar1.ax.axhline(y=0.5, color='red', linewidth=1.5, linestyle='--')
cbar1.ax.text(1.5, 0.5, 'random', transform=cbar1.ax.get_yaxis_transform(),
              va='center', ha='left', fontsize=8, color='red')

# Panel B: Cohen's d heatmap (diverging)
vmax = max(abs(cohens_d_d100.min()), abs(cohens_d_d100.max()))
norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
im2 = ax2.imshow(cohens_d_d100, cmap='RdBu_r', norm=norm, aspect='auto')
ax2.set_xticks(range(3))
ax2.set_xticklabels(benchmarks)
ax2.set_yticks(range(3))
ax2.set_yticklabels(signals)
ax2.set_title("Cross-Model Effect Size (Cohen's d)")

for i in range(3):
    for j in range(3):
        val = cohens_d_d100[i, j]
        color = 'white' if abs(val) > 2.0 else 'black'
        text = f'{val:.2f}'
        ax2.text(j, i, text, ha='center', va='center', color=color, fontsize=9.5, fontweight='bold')

# Highlight S2 reversal cells with red border
for j in range(3):
    rect = mpatches.FancyBboxPatch(
        (j - 0.48, 1 - 0.48), 0.96, 0.96,
        linewidth=2.5, edgecolor='red', facecolor='none',
        boxstyle='round,pad=0.02'
    )
    ax2.add_patch(rect)

# Add reversal label directly on the right side
ax2.annotate('⚠ Reversal', xy=(2.48, 1), xytext=(3.1, 1),
             ha='left', va='center', fontsize=8.5, color='red', fontweight='bold',
             annotation_clip=False,
             arrowprops=dict(arrowstyle='->', color='red', lw=1.2))

cbar2 = fig.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)
cbar2.ax.axhline(y=0.0, color='black', linewidth=0.8, linestyle='-')

fig.text(0.5, -0.02, 'Scale: Qwen2.5-0.5B  |  d005: 0.5% contamination  |  d100: 10% contamination',
         ha='center', fontsize=9, color='gray')

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper'
fig.savefig(f'{out_dir}/fig_signal_heatmap.pdf')
fig.savefig(f'{out_dir}/fig_signal_heatmap.png')
print('Saved fig_signal_heatmap.pdf and .png')
