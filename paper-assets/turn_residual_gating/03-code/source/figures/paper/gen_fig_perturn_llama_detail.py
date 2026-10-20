"""Per-turn AR GAR decay for Llama-3.1-8B — Base/TG/LoRA-only."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

# N=20 T=4 data (eval_llama_ar_n20) — reliable estimates
turns_4 = np.arange(1, 5)
data_4 = {
    'Base':       [0.0282, 0.0128, 0.0092, 0.0084],
    'ThreadGate': [0.0409, 0.0415, 0.0486, 0.0383],
    'LoRA':       [0.0332, 0.0490, 0.0254, 0.0314],
}

# Base T=10 decay profile (llama_phase1_gar_diag, N=5)
turns_10 = np.arange(1, 11)
base_t10 = [0.0263, 0.0183, 0.0087, 0.0055, 0.0060,
            0.0035, 0.0038, 0.0037, 0.0050, 0.0026]

markers = {'Base': 'o', 'ThreadGate': 's', 'LoRA': 'v'}
fancy_colors = {'Base': C_BASE, 'ThreadGate': C_TEAL, 'LoRA': C_PURPLE}

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.5, 4.5),
                                gridspec_kw={'height_ratios': [1, 1.3]})

# --- Left panel: 3-way comparison T=1-4 ---
for name, vals in data_4.items():
    ax1.plot(turns_4, vals, marker=markers[name], markersize=4.5,
             color=fancy_colors[name], label=name, zorder=3)

ax1.set_xlabel('Turn index')
ax1.set_ylabel('AR GAR-ours')
ax1.set_xticks(turns_4)
ax1.set_xlim(0.7, 4.3)
ax1.set_ylim(-0.002, 0.058)
ax1.set_title('(a) 3-way ($N{=}20$, $T{=}4$)', fontsize=8)
ax1.legend(
           borderpad=0.3, handlelength=1.5, loc='upper right')

# --- Right panel: Base decay T=1-10 ---
ax2.plot(turns_10, base_t10, marker='o', markersize=4, color=C_BASE,
         label='Base', zorder=3)
ax2.fill_between(turns_10, 0, base_t10, alpha=0.12, color=C_BASE)

ax2.annotate('−90.1%', xy=(10, base_t10[-1]),
             xytext=(8.5, 0.018), fontsize=7, color=C_BASE,
             arrowprops=dict(arrowstyle='->', color=C_BASE, lw=0.8))

ax2.set_xlabel('Turn index')
ax2.set_ylabel('AR GAR-ours')
ax2.set_xticks(turns_10)
ax2.set_xlim(0.5, 10.5)
ax2.set_ylim(-0.001, 0.032)
ax2.set_title('(b) Base decay ($N{=}5$, $T{=}10$)', fontsize=8)

fig.tight_layout(h_pad=1.5)
save_fig(fig, 'fig_perturn_llama_detail')
