"""Figure A: SS Gap Compression — TF/AR gap ratio by config (horizontal bars)."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

configs =    ['Llama SS', 'Qwen SS', 'ThreadGate', 'LoRA', 'UG', 'PCGrad', 'Llama TG']
gap_ratios = [2.9,        1.3,       7.8,          13.5,   14.8, 16.7,     12.5]
color_keys = ['SS',       'SS',      'ThreadGate', 'LoRA', 'UG', 'PCGrad', 'ThreadGate']
colors = [COLORS.get(c, C_GRAY) for c in color_keys]

fig, ax = plt.subplots(figsize=(5.2, 2.8))

y = np.arange(len(configs))
alphas = [1.0 if 'SS' in c else 0.55 for c in configs]

for i, (cfg, gap, col) in enumerate(zip(configs, gap_ratios, colors)):
    ax.barh(i, gap, height=0.6, color=col, alpha=alphas[i],
            edgecolor='white', linewidth=0.4, zorder=2)
    is_ss = 'SS' in cfg
    ax.text(gap + 0.4, i, f'{gap:.1f}×', va='center', ha='left',
            fontsize=7.5, fontweight='bold' if is_ss else 'normal',
            color=col if is_ss else '#666666')

ax.axvline(1.0, color=C_GRAY, linestyle='--', linewidth=0.8, zorder=1, alpha=0.6)
ax.text(1.0, len(configs) - 0.15, 'parity', fontsize=6, color=C_GRAY,
        ha='center', va='bottom')

# Separator between Qwen and Llama entries
ax.axhline(1.5, color='#DDDDDD', linewidth=0.5, linestyle='-', zorder=0)

ax.set_yticks(y)
ax.set_yticklabels(configs, fontsize=8)
ax.set_xlabel('TF / AR Gap Ratio', fontsize=9)
ax.set_xlim(0, 20)
ax.invert_yaxis()

save_fig(fig, 'fig_ss_gap_compression')
