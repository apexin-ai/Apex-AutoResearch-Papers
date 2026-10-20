import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'text.usetex': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
})

# Data: (baseline_acc%, |d|, ci_lo, ci_hi, model_label, benchmark)
# 5% contamination
data_5 = [
    (67.8, 4.15, 2.74, 9.85, 'Qwen', 'MMLU'),
]
# 15% contamination
data_15 = [
    (67.8, 6.57, 4.54, 15.19, 'Qwen', 'MMLU'),
    (59.4,  2.80, 2.20,  3.40, 'Llama', 'MMLU'),
    (52.4,  3.37, 2.69,  4.05, 'Mistral', 'MMLU'),
    (89.7,  3.16, 2.01,  9.54, 'Qwen\nARC-C', 'ARC-C'),
]
# 25% contamination
data_25 = [
    (67.8, 8.22, 5.73, 18.88, 'Qwen', 'MMLU'),
    (59.4,  2.56, 2.04,  3.08, 'Llama', 'MMLU'),
]
# 50% contamination
data_50 = [
    (67.8, 1.90, 1.04, 4.95, 'Qwen', 'MMLU'),
    (59.4,  2.30, 2.00, 2.60, 'Llama', 'MMLU'),
    (52.4,  3.50, 2.10, 9.40, 'Mistral', 'MMLU'),
    (89.7,  5.30, 3.60, 15.20, 'Qwen\nARC-C', 'ARC-C'),
]

C_QWEN = '#2166ac'
C_LLAMA = '#b2182b'
C_MISTRAL = '#1b7837'
C_ARCC = '#666666'

model_colors = {
    'Qwen': C_QWEN,
    'Llama': C_LLAMA,
    'Mistral': C_MISTRAL,
    'Qwen\nARC-C': C_ARCC,
}

fig, ax = plt.subplots(figsize=(5.5, 4.5))

def plot_points(data, marker, size, label_suffix, zorder=5):
    for acc, d, ci_lo, ci_hi, model, bm in data:
        color = model_colors[model]
        ax.scatter(acc, d, marker=marker, s=size, color=color,
                   edgecolors='white', linewidths=0.5, zorder=zorder)
        ax.plot([acc, acc], [ci_lo, ci_hi], color=color,
                linewidth=1.2, alpha=0.5, zorder=zorder - 1)

# Plot each contamination level with different markers
plot_points(data_5,  'D', 50, '5%',  zorder=6)
plot_points(data_15, '^', 60, '15%', zorder=6)
plot_points(data_25, 's', 55, '25%', zorder=7)
plot_points(data_50, 'o', 60, '50%', zorder=6)

# Legend entries (manual)
ax.scatter([], [], marker='D', s=40, color='gray', label='5% contam.')
ax.scatter([], [], marker='^', s=50, color='gray', label='15% contam.')
ax.scatter([], [], marker='s', s=45, color='gray', label='25% contam.')
ax.scatter([], [], marker='o', s=50, color='gray', label='50% contam.')

# Model labels — positioned near the data points
offsets = {
    ('Qwen', '15'): (3, 6),
    ('Qwen', '25'): (3, 3),
    ('Llama', '50'): (2, 4),
    ('Mistral', '50'): (2, 4),
}

# Label Qwen (blue cluster)
ax.annotate('Qwen', xy=(67.8, 8.22), xytext=(72, 8.5),
            fontsize=8, color=C_QWEN, fontweight='bold',
            arrowprops=dict(arrowstyle='-', color=C_QWEN, lw=0.5, alpha=0.4))

# Label Llama
ax.annotate('Llama', xy=(59.4, 2.33), xytext=(61.5, 3.8),
            fontsize=8, color=C_LLAMA, fontweight='bold',
            arrowprops=dict(arrowstyle='-', color=C_LLAMA, lw=0.5, alpha=0.4))

# Label Mistral
ax.annotate('Mistral', xy=(52.4, 3.50), xytext=(46, 4.5),
            fontsize=8, color=C_MISTRAL, fontweight='bold',
            arrowprops=dict(arrowstyle='-', color=C_MISTRAL, lw=0.5, alpha=0.4))

# Label Qwen ARC-C
ax.annotate('Qwen\nARC-C', xy=(89.7, 5.30), xytext=(92, 6.2),
            fontsize=7, color=C_ARCC, fontweight='bold',
            arrowprops=dict(arrowstyle='-', color=C_ARCC, lw=0.5, alpha=0.4))

# θ-shift absorption annotation (arrow from Qwen 25% down to 50%)
ax.annotate('θ-shift\nabsorption', xy=(68.4, 1.90), xytext=(75, 1.3),
            fontsize=6.5, color='#555555', style='italic',
            arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8))

# Ceiling reversal annotation
ax.annotate('ceiling\nreversal', xy=(89.7, 6.0), xytext=(93, 7.2),
            fontsize=6.5, color='#555555', style='italic',
            arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8))

# Large effect threshold
ax.axhline(y=0.8, color='#cccccc', linestyle=':', linewidth=0.8, zorder=1)
ax.text(46, 0.65, 'large effect (0.8)', fontsize=6, color='#aaaaaa', style='italic')

ax.set_xlabel('Baseline Accuracy (%)')
ax.set_ylabel("Cohen's |d|")
ax.set_xlim(45, 98)
ax.set_ylim(0, 10)
ax.set_yticks([0, 2, 4, 6, 8, 10])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

leg = ax.legend(loc='upper left', framealpha=0.95, edgecolor='#cccccc',
                borderpad=0.4, handletextpad=0.4, handlelength=1.5)
leg.get_frame().set_linewidth(0.4)

out = Path(__file__).resolve().parent
fig.savefig(out / 'fig_theta_scatter.pdf', format='pdf')
fig.savefig(out / 'fig_theta_scatter.png', format='png')
plt.close()
print("Done. Files saved.")
