import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

with open('/root/autodl-tmp/struct_self_consist_ie/artifacts/f1_scaling/scaling_results.json') as f:
    data = json.load(f)

def scaling_law(N, a, b, c):
    return a - b * N**(-c)

plt.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 4,
    'ytick.major.size': 4,
})

fig, ax = plt.subplots(1, 1, figsize=(7, 4.5))

dataset_colors = {
    'SciERC': '#D62728',
    'CoNLL2003': '#1F77B4',
    'FewNERD': '#2CA02C',
}
dataset_markers = {
    'SciERC': 'o',
    'CoNLL2003': 's',
    'FewNERD': '^',
}
model_linestyle = {
    'Qwen2.5-7B': '-',
    'LLaMA-3.1-8B': '--',
}

plot_order = ['Qwen_SciERC', 'LLaMA_SciERC', 'Qwen_FewNERD', 'LLaMA_FewNERD', 'Qwen_CoNLL', 'LLaMA_CoNLL']

N_smooth = np.linspace(1, 35, 300)

for key in plot_order:
    entry = data[key]
    model = entry['model']
    dataset = entry['dataset']
    N_vals = np.array(entry['N_values'])
    oracle = np.array(entry['oracle_f1_mean'])
    std = np.array(entry['oracle_f1_std'])
    fit = entry['fit']
    a, b, c = fit['a'], fit['b'], fit['c']

    color = dataset_colors[dataset]
    marker = dataset_markers[dataset]
    ls = model_linestyle[model]

    ax.errorbar(N_vals, oracle, yerr=std, fmt=marker, color=color,
                markersize=6, capsize=2.5, capthick=0.8, linewidth=0,
                elinewidth=0.8, zorder=5, markeredgecolor='white',
                markeredgewidth=0.6)

    fitted = scaling_law(N_smooth, a, b, c)
    ax.plot(N_smooth, fitted, color=color, linestyle=ls, linewidth=1.5,
            alpha=0.85, zorder=3)

    greedy = entry['greedy_f1']
    ax.plot(N_vals[0], greedy, marker='x', color=color, markersize=5,
            markeredgewidth=1.2, zorder=4, alpha=0.5)

# Annotations — hand-tuned to avoid all overlaps
# Data endpoints for reference:
# Qwen_CoNLL N=16 → 0.964    LLaMA_CoNLL N=16 → 0.952
# Qwen_FewNERD N=16 → 0.912  LLaMA_FewNERD N=8 → 0.887
# Qwen_SciERC N=32 → 0.841   LLaMA_SciERC N=16 → 0.811
annots = [
    ('Qwen_SciERC',  '$c$=0.39',              32, 0.841,  6, -2),
    ('LLaMA_SciERC', '$c$=0.30',              16, 0.811,  6,  8),
    ('Qwen_FewNERD', '$c$=0.61',              16, 0.912,  6, -12),
    ('LLaMA_FewNERD','$c$=0.61 (4-pt)',        8, 0.887, 10, -14),
    ('Qwen_CoNLL',   '$a$=0.97, $b$=0.10',   16, 0.964,  3,  8),
    ('LLaMA_CoNLL',  '$a$=0.97, $b$=0.04',   16, 0.952,  3,  8),
]

for key, txt, xd, yd, dx, dy in annots:
    entry = data[key]
    color = dataset_colors[entry['dataset']]
    ax.annotate(txt, xy=(xd, yd),
                xytext=(dx, dy), textcoords='offset points',
                fontsize=7.5, color=color, alpha=0.9, va='center')

legend_elements = []
for ds in ['SciERC', 'CoNLL2003', 'FewNERD']:
    legend_elements.append(Line2D([0], [0], marker=dataset_markers[ds],
                           color=dataset_colors[ds], linewidth=1.5,
                           markersize=6, markeredgecolor='white',
                           markeredgewidth=0.6, label=ds))
legend_elements.append(Line2D([0], [0], color='gray', linestyle='-',
                       linewidth=1.5, label='Qwen2.5-7B'))
legend_elements.append(Line2D([0], [0], color='gray', linestyle='--',
                       linewidth=1.5, label='LLaMA-3.1-8B'))

ax.set_xscale('log', base=2)
ax.set_xticks([1, 2, 4, 8, 16, 32])
ax.set_xticklabels(['1', '2', '4', '8', '16', '32'])
ax.set_xlabel('Number of Samples ($N$)', fontsize=12)
ax.set_ylabel('Oracle F1', fontsize=12)
ax.set_xlim(0.8, 50)
ax.set_ylim(0.60, 1.0)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(handles=legend_elements, loc='lower right', frameon=False,
          fontsize=9.5, handlelength=2.0)

ax.text(0.02, 0.98, r'$F_1(N) = a - b \cdot N^{-c}$',
        transform=ax.transAxes, fontsize=10, va='top', color='#444444')

plt.tight_layout()
out_dir = '/root/autodl-tmp/struct_self_consist_ie/artifacts/f1_scaling/'
plt.savefig(out_dir + 'fig_oracle_scaling.pdf', dpi=300, bbox_inches='tight')
plt.savefig(out_dir + 'fig_oracle_scaling.png', dpi=150, bbox_inches='tight')
print('DONE')
