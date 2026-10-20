import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# Data source: SciERC columns from exp_015 unified evaluation
# (exp_012_logprob/samples_with_logprobs.jsonl, N=8, T=1.0, seed=42)
# CoNLL from exp_002, WNUT-17 from exp_003, LLaMA from exp_007

signals = ['Voting Conf', 'Soft Jaccard', 'Exact Match', "Fleiss' Kappa", 'Log-prob']
columns = ['CoNLL NER', 'SciERC NER', 'SciERC RE\n(full)', 'SciERC RE\n(cond)', 'WNUT-17']
subtitles = ['Easy (F1=0.91)', 'Hard (F1=0.66)', 'Harder', '', 'Boundary\n(SJ≈0)']

data = np.array([
    [0.424, 0.502, 0.422, 0.463, 0.08],
    [0.436, 0.357, 0.211, 0.368, 0.082],
    [0.451, 0.257, 0.100, 0.361, np.nan],
    [0.400, 0.265, 0.253, 0.317, np.nan],
    [0.316, 0.140, 0.247, 0.146, -0.41],
])

llama_data = {
    (1, 1): 0.363,  # SJ, SciERC NER
    (1, 2): 0.299,  # SJ, RE full
    (1, 3): 0.405,  # SJ, RE cond
    (3, 1): 0.327,  # FK, SciERC NER
    (3, 2): 0.305,  # FK, RE full
    (3, 3): 0.259,  # FK, RE cond
    (4, 1): 0.183,  # LP, SciERC NER
    (4, 2): 0.288,  # LP, RE full
    (4, 3): 0.092,  # LP, RE cond
}

cmap = matplotlib.colormaps['RdYlGn']
norm = mcolors.TwoSlopeNorm(vmin=-0.45, vcenter=0.25, vmax=0.50)

fig, ax = plt.subplots(figsize=(8, 5))

masked = np.ma.masked_invalid(data)
im = ax.pcolormesh(
    np.arange(data.shape[1] + 1), np.arange(data.shape[0] + 1),
    masked, cmap=cmap, norm=norm, edgecolors='white', linewidth=2,
)

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if np.isnan(data[i, j]):
            ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor='#d9d9d9', edgecolor='white', linewidth=2))
            ax.text(j + 0.5, i + 0.5, '—', ha='center', va='center', fontsize=12, color='#888888', fontweight='bold')
        else:
            val = data[i, j]
            color_val = cmap(norm(val))
            lum = 0.299 * color_val[0] + 0.587 * color_val[1] + 0.114 * color_val[2]
            text_color = 'white' if lum < 0.5 else 'black'
            ax.text(j + 0.5, i + 0.5, f'{val:.2f}', ha='center', va='center',
                    fontsize=11, fontweight='bold', color=text_color)

for i, j in llama_data:
    lval = llama_data[(i, j)]
    color_val = cmap(norm(data[i, j]))
    lum = 0.299 * color_val[0] + 0.587 * color_val[1] + 0.114 * color_val[2]
    sub_color = 'white' if lum < 0.5 else '#555555'
    ax.text(j + 0.5, i + 0.78, f'L:{lval:.2f}', ha='center', va='center',
            fontsize=7.5, color=sub_color, style='italic')

ax.axvline(x=4, color='#333333', linewidth=2.5, linestyle='--')
ax.text(4.5, -0.55, 'method\nboundary', ha='center', va='center', fontsize=8,
        color='#555555', style='italic')

ax.set_xticks(np.arange(data.shape[1]) + 0.5)
ax.set_xticklabels(columns, ha='center')
ax.set_yticks(np.arange(data.shape[0]) + 0.5)
ax.set_yticklabels(signals)

ax.tick_params(axis='both', which='both', length=0)
ax.set_xlim(0, data.shape[1])
ax.set_ylim(data.shape[0], 0)

for idx, sub in enumerate(subtitles):
    if sub:
        ax.text(idx + 0.5, data.shape[0] + 0.25, sub, ha='center', va='top',
                fontsize=8, color='#666666', style='italic')

cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label('Spearman ρ', fontsize=11)
cbar.ax.tick_params(labelsize=9)

ax.set_title('Confidence Signal Effectiveness Across Tasks\n(Qwen3-8B, N=8, T=1.0; L: = LLaMA-3.1-8B)',
             fontsize=12, pad=12)

ax.spines[:].set_visible(False)

plt.tight_layout()
out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf'
plt.savefig(out_path, format='pdf')
plt.close()
print(f'Saved to {out_path}')
