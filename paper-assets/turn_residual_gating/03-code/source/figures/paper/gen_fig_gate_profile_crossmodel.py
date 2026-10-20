"""Generate appendix Figure 7: Side-by-side gate profiles for Qwen vs Llama."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

qwen_gates = np.array([
    .883, .793, .996, .988, .984, .797, .961, .918,
    .965, .934, .969, .918, .926, .941, .930, .965,
    .941, .910, .961, .965, .973, .988, .969, .980,
    .980, .984, .988, 1.00
])
llama_gates = np.array([
    0.957, 0.973, 0.977, 0.965, 0.992, 0.969, 0.957, 0.957,
    0.961, 0.949, 0.938, 0.934, 0.969, 0.953, 0.957, 0.965,
    0.953, 0.961, 0.922, 0.902, 0.883, 0.863, 0.836, 0.844,
    0.809, 0.719, 0.762, 0.805, 0.801, 0.855, 0.898, 0.934
])

fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 5.0), sharex=False)

# Panel (a): Qwen
layers_q = np.arange(len(qwen_gates))
ax_a.bar(layers_q, qwen_gates, color=C_TG, alpha=0.85, edgecolor='white',
         linewidth=0.3, zorder=2)
ax_a.axhline(1.0, color='#cccccc', linestyle=':', linewidth=0.8, zorder=1)
ax_a.set_xlabel('Layer Index')
ax_a.set_ylabel('Gate Value')
ax_a.set_title('(a) Qwen-2.5-7B', fontsize=9, fontweight='bold', loc='left')
ax_a.set_ylim(0.68, 1.03)
ax_a.set_xticks([0, 4, 8, 12, 16, 20, 24, 27])
ax_a.grid(axis='y', alpha=0.15, zorder=0)

for idx, val in [(1, qwen_gates[1]), (5, qwen_gates[5])]:
    ax_a.annotate(f'L{idx}={val:.3f}', xy=(idx, val),
                  xytext=(idx + 3, val - 0.04), fontsize=6.5, color=C_TG,
                  arrowprops=dict(arrowstyle='->', color=C_TG, lw=0.7))

# Panel (b): Llama
layers_l = np.arange(len(llama_gates))
ax_b.bar(layers_l, llama_gates, color=C_GREEN, alpha=0.85, edgecolor='white',
         linewidth=0.3, zorder=2)
ax_b.axhline(1.0, color='#cccccc', linestyle=':', linewidth=0.8, zorder=1)
ax_b.set_xlabel('Layer Index')
ax_b.set_ylabel('Gate Value')
ax_b.set_title('(b) Llama-3.1-8B', fontsize=9, fontweight='bold', loc='left')
ax_b.set_ylim(0.68, 1.03)
ax_b.set_xticks([0, 4, 8, 12, 16, 20, 24, 28, 31])
ax_b.grid(axis='y', alpha=0.15, zorder=0)

ax_b.annotate(f'L25={llama_gates[25]:.3f}', xy=(25, llama_gates[25]),
              xytext=(18, 0.70), fontsize=6.5, color=C_GREEN,
              arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=0.7))

plt.tight_layout(h_pad=1.5)
save_fig(fig, 'fig_gate_profile_crossmodel')
