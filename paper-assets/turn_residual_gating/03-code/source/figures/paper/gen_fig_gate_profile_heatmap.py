"""Generate appendix Figure 6: Per-layer gate values heatmap (Qwen + Llama)."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import matplotlib.colors as mcolors
import numpy as np

apply_style()

qwen_tg = np.array([
    .883, .793, .996, .988, .984, .797, .961, .918,
    .965, .934, .969, .918, .926, .941, .930, .965,
    .941, .910, .961, .965, .973, .988, .969, .980,
    .980, .984, .988, 1.00
])
qwen_ug = np.array([
    .875, .918, .953, .777, .961, .812, .949, .934,
    .957, .945, .961, .949, .953, .957, .953, .965,
    .957, .949, .969, .969, .977, .984, .973, .984,
    .988, .988, .992, 1.00
])
qwen_pcgrad = np.array([
    .891, .813, .988, .980, .977, .816, .953, .926,
    .957, .941, .965, .930, .934, .945, .938, .961,
    .945, .918, .957, .961, .969, .984, .965, .977,
    .977, .980, .984, .996
])

llama_tg = np.array([
    0.957, 0.973, 0.977, 0.965, 0.992, 0.969, 0.957, 0.957,
    0.961, 0.949, 0.938, 0.934, 0.969, 0.953, 0.957, 0.965,
    0.953, 0.961, 0.922, 0.902, 0.883, 0.863, 0.836, 0.844,
    0.809, 0.719, 0.762, 0.805, 0.801, 0.855, 0.898, 0.934
])

cmap = mcolors.LinearSegmentedColormap.from_list(
    'gate_cmap', ['#1B4965', '#5FA8D3', '#BEE3F8', '#EDF6FC', '#FAFAFA'], N=256
)
norm = mcolors.Normalize(vmin=0.70, vmax=1.00)

fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 4.0),
                                  gridspec_kw={'height_ratios': [28, 32]})

# Panel (a): Qwen (28 layers x 3 conditions)
qwen_data = np.array([qwen_tg, qwen_ug, qwen_pcgrad])
im_a = ax_a.imshow(qwen_data, aspect='auto', cmap=cmap, norm=norm,
                    interpolation='nearest')
ax_a.set_yticks([0, 1, 2])
ax_a.set_yticklabels(['TG', 'UG', 'PCGrad'])
ax_a.set_xticks(np.arange(0, 28, 4))
ax_a.set_xlabel('Layer Index')
ax_a.set_title('(a) Qwen-2.5-7B (28 layers)', fontsize=9,
               fontweight='bold', loc='left')

for i in range(qwen_data.shape[0]):
    for j in range(qwen_data.shape[1]):
        v = qwen_data[i, j]
        if v < 0.92:
            tc = 'white' if v < 0.88 else '#1B4965'
            ax_a.text(j, i, f'{v:.2f}', ha='center', va='center',
                      fontsize=4.5, color=tc, fontweight='bold')

# Panel (b): Llama (32 layers x 1 condition)
llama_data = llama_tg.reshape(1, -1)
im_b = ax_b.imshow(llama_data, aspect='auto', cmap=cmap, norm=norm,
                     interpolation='nearest')
ax_b.set_yticks([0])
ax_b.set_yticklabels(['TG'])
ax_b.set_xticks(np.arange(0, 32, 4))
ax_b.set_xlabel('Layer Index')
ax_b.set_title('(b) Llama-3.1-8B (32 layers)', fontsize=9,
               fontweight='bold', loc='left')

for j in range(llama_data.shape[1]):
    v = llama_data[0, j]
    if v < 0.85:
        tc = 'white' if v < 0.80 else '#1B4965'
        ax_b.text(j, 0, f'{v:.2f}', ha='center', va='center',
                  fontsize=4.5, color=tc, fontweight='bold')

fig.colorbar(im_b, ax=[ax_a, ax_b], shrink=0.8, label='Gate Value',
             pad=0.02)

fig.subplots_adjust(hspace=0.45)
save_fig(fig, 'fig_gate_profile_heatmap')
