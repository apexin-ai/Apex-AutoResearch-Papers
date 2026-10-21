import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import json

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
    'axes.spines.top': False,
    'axes.spines.right': False,
})

with open('/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_5arch.json') as f:
    data = json.load(f)

archs = ['GDN', 'RetNet', 'HGRN2', 'GLA', 'DeltaNet']
n = len(archs)
arch_idx = {a: i for i, a in enumerate(archs)}

name_map = {'GatedDeltaNet': 'GDN'}

def build_matrices(benchmark_data):
    helped = np.full((n, n), np.nan)
    hurt = np.full((n, n), np.nan)
    for pair_key, vals in benchmark_data['pairwise'].items():
        a_name, b_name = pair_key.split('-', 1)
        a_name = name_map.get(a_name, a_name)
        b_name = name_map.get(b_name, b_name)
        i, j = arch_idx[a_name], arch_idx[b_name]
        helped[i, j] = vals['J_helped']
        helped[j, i] = vals['J_helped']
        hurt[i, j] = vals['J_hurt']
        hurt[j, i] = vals['J_hurt']
    # Build display matrix: upper triangle = helped, lower triangle = hurt
    display = np.full((n, n), np.nan)
    for i in range(n):
        for j in range(n):
            if i < j:
                display[i, j] = helped[i, j]
            elif i > j:
                display[i, j] = hurt[i, j]
    return display

bench_keys = {'lambada_openai': 'LAMBADA', 'arc_easy': 'ARC-Easy'}
matrices = {}
for bk, label in bench_keys.items():
    matrices[label] = build_matrices(data['benchmarks'][bk])

cmap = plt.cm.YlGnBu
norm = mcolors.Normalize(vmin=0, vmax=0.20)
grey_color = '#D0D0D0'

fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.5))
fig.subplots_adjust(wspace=0.35)

for ax_idx, (label, order) in enumerate([('LAMBADA', 0), ('ARC-Easy', 1)]):
    ax = axes[order]
    mat = matrices[label]

    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(archs, rotation=45, ha='right')
    ax.set_yticklabels(archs)
    ax.set_title(label, pad=8)
    ax.set_aspect('equal')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(length=0)

    for i in range(n):
        for j in range(n):
            if i == j:
                rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1,
                                      facecolor=grey_color, edgecolor='white', linewidth=1.5)
                ax.add_patch(rect)
                ax.text(j, i, '—', ha='center', va='center', fontsize=9, color='#888888')
            else:
                val = mat[i, j]
                color = cmap(norm(val))
                rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1,
                                      facecolor=color, edgecolor='white', linewidth=1.5)
                ax.add_patch(rect)
                # text color: white for dark cells, black for light
                r, g, b, _ = color
                lum = 0.299 * r + 0.587 * g + 0.114 * b
                txt_color = 'white' if lum < 0.55 else 'black'
                ax.text(j, i, f'{val:.2f}', ha='center', va='center',
                        fontsize=9, color=txt_color, fontweight='medium')

# Colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=axes, shrink=0.8, aspect=25, pad=0.03)
cbar.set_label('Jaccard Index', fontsize=11)
cbar.ax.tick_params(labelsize=9)

# Annotation for upper/lower triangle
fig.text(0.5, 0.98, '▲ upper tri = J_helped    ▼ lower tri = J_hurt',
         ha='center', va='top', fontsize=9, color='#555555')

out_base = '/root/entrainment_gated_ft/results/figures/jaccard_heatmap_5arch'
fig.savefig(out_base + '.pdf')
fig.savefig(out_base + '.png')
print('Saved PDF and PNG.')
