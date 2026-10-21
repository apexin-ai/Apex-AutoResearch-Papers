import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

categories = ['STEM', 'Social\nSciences', 'Humanities', 'Other', 'Overall']

data = {
    'Base':      [70.69, 77.28, 83.95, 68.25, 74.23],
    'ThreadGate':[69.20, 76.92, 83.33, 67.59, 73.47],
    'PCGrad':    [69.55, 76.79, 84.08, 68.12, 73.86],
    'SS':        [69.97, 76.83, 83.39, 67.95, 73.75],
    'LoRA':      [70.03, 77.08, 83.62, 67.06, 73.57],
    'UG':        [69.65, 77.02, 83.95, 66.80, 73.46],
}

x = np.arange(len(categories))
n = len(data)
width = 0.13

fig, ax = plt.subplots(figsize=(6.5, 2.8))

for i, (name, vals) in enumerate(data.items()):
    offset = (i - n / 2 + 0.5) * width
    color = COLORS.get(name, C_GRAY)
    bars = ax.bar(x + offset, vals, width, label=name, color=color,
                  edgecolor='white', linewidth=0.3, alpha=0.85)

ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=8)
ax.set_ylabel('Accuracy (%)')
ax.set_ylim(62, 88)

ax.axhline(y=74.23, color=C_BASE, linestyle=':', linewidth=0.6, alpha=0.5)

ax.legend(frameon=False, ncol=3, loc='upper left', fontsize=6.5,
          bbox_to_anchor=(0.0, 1.02))

fig.tight_layout()
save_fig(fig, 'fig_mmlu_comparison')
