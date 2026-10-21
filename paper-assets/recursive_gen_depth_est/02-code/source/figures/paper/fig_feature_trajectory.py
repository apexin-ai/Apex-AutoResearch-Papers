import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
from pathlib import Path

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
    'lines.linewidth': 1.8,
})

data_path = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/matrix_data.json')
out_dir = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper')

with open(data_path) as f:
    data = json.load(f)

cells = data['cells']
depths = [0, 1, 2, 3]
features = ['p90_ppl', 'var_surprisal', 'mean_surprisal', 'p75_ppl', 'type_token_ratio']
feature_colors = {
    'p90_ppl': '#D55E00',
    'var_surprisal': '#0072B2',
    'mean_surprisal': '#56B4E9',
    'p75_ppl': '#E69F00',
    'type_token_ratio': '#CC79A7',
}
feature_labels = {
    'p90_ppl': 'p90 PPL',
    'var_surprisal': 'Var(surprisal)',
    'mean_surprisal': 'Mean surprisal',
    'p75_ppl': 'p75 PPL',
    'type_token_ratio': 'TTR',
}

models = [
    ('Pythia-1.4B', ['pythia_nucleus', 'pythia_temp09', 'pythia_topk50']),
    ('OLMo-1B', ['olmo_nucleus', 'olmo_temp09', 'olmo_topk50']),
    ('GPT-2 XL', ['gpt2xl_nucleus', 'gpt2xl_temp09', 'gpt2xl_topk50']),
]

strategy_styles = {
    'nucleus': '-',
    'temp09': '--',
    'topk50': ':',
}
strategy_labels = {
    'nucleus': 'nucleus',
    'temp09': 'temp 0.9',
    'topk50': 'top-k 50',
}

def get_strategy(cell_key):
    if 'nucleus' in cell_key:
        return 'nucleus'
    elif 'temp09' in cell_key:
        return 'temp09'
    else:
        return 'topk50'

def has_trajectory(cell_key):
    c = cells.get(cell_key, {})
    ft = c.get('feature_trajectory', {})
    return ft.get('available', False) and 'depth_means' in ft

fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)

for ax_idx, (model_name, cell_keys) in enumerate(models):
    ax = axes[ax_idx]
    valid_keys = [k for k in cell_keys if has_trajectory(k)]
    multi_strategy = len(valid_keys) > 1

    for cell_key in valid_keys:
        strat = get_strategy(cell_key)
        ls = strategy_styles[strat]
        dm = cells[cell_key]['feature_trajectory']['depth_means']

        for feat in features:
            vals = [dm[str(d)].get(feat) for d in depths]
            if vals[0] is None or vals[0] == 0:
                continue
            normed = [v / vals[0] for v in vals]
            label = None
            if ax_idx == 0 and strat == 'nucleus':
                label = feature_labels[feat]
            ax.plot(depths, normed, color=feature_colors[feat], linestyle=ls,
                    marker='o', markersize=4, label=label)

    ax.set_title(model_name)
    ax.set_xlabel('Recursive Depth')
    ax.set_xticks(depths)
    ax.set_ylim(0, 1.05)
    if ax_idx == 0:
        ax.set_ylabel('Normalized Feature Mean\n(relative to depth 0)')

# Build legend entries
legend_handles = []
for feat in features:
    line, = axes[0].plot([], [], color=feature_colors[feat], linestyle='-',
                          linewidth=1.8, label=feature_labels[feat])
    legend_handles.append(line)

# Check if any model has multiple strategies
any_multi = any(sum(1 for k in ks if has_trajectory(k)) > 1 for _, ks in models)
if any_multi:
    from matplotlib.lines import Line2D
    for strat_key, strat_ls in strategy_styles.items():
        if any(has_trajectory(k) for _, ks in models for k in ks if get_strategy(k) == strat_key):
            legend_handles.append(Line2D([0], [0], color='gray', linestyle=strat_ls,
                                          linewidth=1.5, label=strategy_labels[strat_key]))

fig.legend(handles=legend_handles, loc='lower center', ncol=len(legend_handles),
           bbox_to_anchor=(0.5, -0.08), frameon=False, fontsize=10)

plt.tight_layout()
plt.subplots_adjust(bottom=0.18)

fig.savefig(out_dir / 'fig_feature_trajectory.pdf')
fig.savefig(out_dir / 'fig_feature_trajectory.png')
plt.close()

pdf_size = (out_dir / 'fig_feature_trajectory.pdf').stat().st_size
png_size = (out_dir / 'fig_feature_trajectory.png').stat().st_size
print(f"PDF: {pdf_size} bytes, PNG: {png_size} bytes")
