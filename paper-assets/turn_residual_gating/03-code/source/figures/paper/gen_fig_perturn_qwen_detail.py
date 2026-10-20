"""Per-turn AR GAR decay for Qwen2.5-7B — 6 configurations."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

turns = np.arange(1, 6)

data = {
    'Base':       [0.0853, 0.0319, 0.0206, 0.0125, 0.0042],
    'ThreadGate': [0.1297, 0.0725, 0.0591, 0.0428, 0.0664],
    'PCGrad':     [0.0903, 0.0382, 0.0276, 0.0292, 0.0267],
    'UG':         [0.1130, 0.0564, 0.0328, 0.0198, 0.0160],
    'LoRA':       [0.1072, 0.0586, 0.0304, 0.0489, 0.0397],
    'SS':         [0.4581, 0.3813, 0.3436, 0.3699, 0.3653],
}

markers = {
    'Base': 'o', 'ThreadGate': 's', 'PCGrad': 'D',
    'UG': '^', 'LoRA': 'v', 'SS': 'P',
}

fig, ax = plt.subplots(figsize=(3.4, 2.4))

for name in CONFIG_ORDER:
    vals = data[name]
    ax.plot(turns, vals, marker=markers[name], markersize=4,
            color=COLORS[name], label=name, zorder=3)

ax.set_xlabel('Turn index')
ax.set_ylabel('AR GAR-ours')
ax.set_xticks(turns)
ax.set_xlim(0.7, 5.3)
ax.set_ylim(-0.01, 0.50)

ax.axhline(y=0, color=C_GRAY, linewidth=0.4, zorder=1)

ax.legend(ncol=2, loc='center right', borderpad=0.4, handlelength=1.5, fontsize=6.5)

fig.tight_layout()
save_fig(fig, 'fig_perturn_qwen_detail')
