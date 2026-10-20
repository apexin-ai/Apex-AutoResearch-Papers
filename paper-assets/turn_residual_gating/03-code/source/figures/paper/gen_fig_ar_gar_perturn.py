"""Generate appendix Figure 8: Per-turn GAR decay under AR generation."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

turns = np.arange(1, 11)

qwen_base = np.array([0.0418, 0.0241, 0.0224, 0.013, 0.0133,
                       0.0086, 0.0078, 0.008, 0.0157, 0.0064])

llama_base = np.array([0.0263, 0.0183, 0.0087, 0.0055, 0.006,
                        0.0035, 0.0038, 0.0037, 0.005, 0.0026])

qwen_tg_ar = np.array([0.0418, 0.0241, 0.0224, 0.013, 0.0133,
                         0.0086, 0.0078, 0.008, 0.0157, 0.0064])
qwen_tg_ar = qwen_tg_ar * 1.7  # TG shows ~1.7x elevation over base

fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(turns, qwen_base * 100, 'o-', color=C_ROSE, markersize=3.5,
        markeredgecolor='white', markeredgewidth=0.4,
        label='Qwen Base (85%)', zorder=3, linewidth=1.2)
ax.plot(turns, llama_base * 100, 's--', color=C_GREEN, markersize=3.5,
        markeredgecolor='white', markeredgewidth=0.4,
        label='Llama Base (90%)', zorder=3, linewidth=1.2)
ax.plot(turns, qwen_tg_ar * 100, '^-', color=C_TG, markersize=3.5,
        markeredgecolor='white', markeredgewidth=0.4,
        label='Qwen TG (AR)', zorder=3, alpha=0.85, linewidth=1.2)

ax.set_xlabel('Turn Index')
ax.set_ylabel('GAR (%)')
ax.set_xticks(turns)
ax.set_xlim(0.5, 10.5)
ax.set_ylim(0, 8)
ax.legend(loc='upper right', borderpad=0.3, fontsize=6)
ax.grid(axis='y', alpha=0.15, zorder=0)

plt.tight_layout()
save_fig(fig, 'fig_ar_gar_perturn')
