"""Generate additional appendix figures for pages 27-31."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
})

# ── Figure 1: Semantic Similarity Progression ──
fig, ax = plt.subplots(figsize=(3.3, 2.2))

depths = [0, 1, 2, 3]
depth_labels = ['0→1', '1→2', '2→3', '3→4']
cosine_sim = [0.622, 0.683, 0.801, 0.859]

ax.plot(depths, cosine_sim, 'o-', color='#2166AC', linewidth=2, markersize=7, zorder=3)
for i, (d, s) in enumerate(zip(depths, cosine_sim)):
    ax.annotate(f'{s:.3f}', (d, s), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=7.5, color='#2166AC')

prompt_types = {'Continuation': 0.717, 'Elab./Rewrite': 0.808}
colors_pt = ['#D95F02', '#7570B3']
for i, (pt, val) in enumerate(prompt_types.items()):
    ax.axhline(y=val, color=colors_pt[i], linestyle=':', linewidth=0.8, alpha=0.6)
    ax.text(3.15, val, pt, fontsize=6.5, color=colors_pt[i], va='center')

ax.set_xticks(depths)
ax.set_xticklabels(depth_labels)
ax.set_xlabel('Depth transition')
ax.set_ylabel('Embedding cosine similarity')
ax.set_ylim(0.55, 0.92)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-0.3, 3.8)

plt.tight_layout()
plt.savefig('fig_appendix_semantic_sim.pdf')
plt.savefig('fig_appendix_semantic_sim.png')
plt.close()
print("✓ semantic similarity figure")


# ── Figure 2: TOST Equivalence Heatmap ──
fig, ax = plt.subplots(figsize=(3.4, 3.0))

generators = ['Py-2.8B', 'Py-1B', 'Qw-1.7B', 'Llama-3B', 'OLMo-1B',
              'Qw-8B', 'Qw-0.6B', 'Mistral-7B']
features = ['$\\bar{H}$', 'TTR', 'hapax', '$\\sigma_H$',
            '$H_{\\mathrm{max}}$', 'tail', '$H_{\\mathrm{min}}$']

d_values = np.array([
    [1.20, 0.77, 0.67, 0.39, 0.25, 0.07, 0.03],
    [1.40, 0.80, 0.65, 0.53, 0.21, 0.08, 0.02],
    [1.12, 0.93, 0.83, 0.52, 0.02, 0.09, 0.05],
    [1.15, 1.04, 0.98, 0.50, 0.01, 0.19, 0.01],
    [1.19, 1.08, 1.00, 0.61, 0.06, 0.22, 0.07],
    [0.86, 0.71, 0.66, 0.37, 0.04, 0.15, 0.01],
    [0.92, 0.63, 0.50, 0.56, 0.01, 0.08, 0.10],
    [0.89, 0.82, 0.82, 0.23, 0.00, 0.16, 0.04],
])

equiv_pass = d_values < 0.20

from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('ddr',
    ['#2166AC', '#92C5DE', '#F7F7F7', '#F4A582', '#D6604D', '#B2182B'])

im = ax.imshow(d_values, cmap=cmap, aspect='auto', vmin=0, vmax=1.4)

for i in range(len(generators)):
    for j in range(len(features)):
        val = d_values[i, j]
        color = 'white' if val > 0.7 else 'black'
        text = f'{val:.2f}'
        if equiv_pass[i, j]:
            text += '*'
        ax.text(j, i, text, ha='center', va='center', fontsize=6.5, color=color)

ax.set_xticks(range(len(features)))
ax.set_xticklabels(features, fontsize=8)
ax.set_yticks(range(len(generators)))
ax.set_yticklabels(generators, fontsize=8)

ax.axvline(x=2.5, color='white', linewidth=2)
ax.axvline(x=3.5, color='white', linewidth=2)

ax.text(1.0, -0.8, 'Drifting', ha='center', fontsize=7, fontstyle='italic', color='#B2182B')
ax.text(3.0, -0.8, 'Int.', ha='center', fontsize=7, fontstyle='italic', color='#7570B3')
ax.text(5.0, -0.8, 'Stationary', ha='center', fontsize=7, fontstyle='italic', color='#2166AC')

cbar = plt.colorbar(im, ax=ax, fraction=0.03, pad=0.04)
cbar.set_label("Cohen's $d$", fontsize=8)

plt.tight_layout()
plt.savefig('fig_appendix_tost_heatmap.pdf')
plt.savefig('fig_appendix_tost_heatmap.png')
plt.close()
print("✓ TOST heatmap figure")


# ── Figure 3: Cross-Reference Model Comparison ──
fig, ax = plt.subplots(figsize=(3.3, 1.8))

refs = ['Pythia-410M\n(Pythia)', 'OLMo-2-1B\n(OLMo)', 'Qwen3-0.6B\n(Qwen)']
f1_vals = [0.803, 0.807, 0.816]
families = ['Pythia', 'OLMo', 'Qwen']
colors = ['#2166AC', '#D95F02', '#1B9E77']

bars = ax.bar(range(len(refs)), f1_vals, color=colors, edgecolor='white',
              linewidth=0.5, width=0.6)

for i, v in enumerate(f1_vals):
    ax.text(i, v + 0.002, f'{v:.3f}', ha='center', fontsize=8, fontweight='bold')

ax.axhline(y=np.mean(f1_vals), color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
ax.text(2.45, np.mean(f1_vals) + 0.001, f'mean: {np.mean(f1_vals):.3f}',
        fontsize=6.5, color='gray')

spread = max(f1_vals) - min(f1_vals)
ax.annotate('', xy=(0, min(f1_vals)-0.003), xytext=(2, min(f1_vals)-0.003),
            arrowprops=dict(arrowstyle='<->', color='gray', lw=0.8))
ax.text(1, min(f1_vals) - 0.007, f'spread = {spread:.3f}',
        ha='center', fontsize=7, color='gray')

ax.set_xticks(range(len(refs)))
ax.set_xticklabels(refs, fontsize=7.5)
ax.set_ylabel('LOGO F1 (5-gen)')
ax.set_ylim(0.78, 0.83)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('fig_appendix_ref_comparison.pdf')
plt.savefig('fig_appendix_ref_comparison.png')
plt.close()
print("✓ reference comparison figure")

print("\nAll extra figures generated.")
