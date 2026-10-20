import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from io import StringIO

plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'axes.linewidth': 1.2,
    'xtick.major.width': 1.0,
    'ytick.major.width': 1.0,
    'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Read only the first section (before the blank line / comment)
lines = []
with open('/root/autodl-tmp/pacs/analysis_output/n500_unified_final.csv') as f:
    for line in f:
        line = line.strip()
        if line == '' or line.startswith('#'):
            break
        lines.append(line)

df = pd.read_csv(StringIO('\n'.join(lines)))

# Parse sparsity to float
sparsity_map = {'s015': 0.15, 's020': 0.20, 's025': 0.25, 's030': 0.30}
df['sparsity_val'] = df['sparsity'].map(sparsity_map)

# Compute asymmetric error bars
df['err_lo'] = df['median_ii_diff'] - df['ci_lo']
df['err_hi'] = df['ci_hi'] - df['median_ii_diff']

models = ['deepseek', 'qwen']
model_labels = {'deepseek': 'DeepSeek-R1-Distill-Qwen-1.5B', 'qwen': 'Qwen2.5-1.5B-Instruct'}

# Colors and markers
style = {
    'imp': {'color': '#D64541', 'marker': 'o', 'label': 'Importance eviction'},
    'rand': {'color': '#4A90D9', 'marker': 's', 'label': 'Random eviction'},
}

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=False)

for ax, model in zip(axes, models):
    for masking in ['imp', 'rand']:
        sub = df[(df['model'] == model) & (df['masking'] == masking)].sort_values('sparsity_val')
        s = style[masking]
        yerr = np.array([sub['err_lo'].values, sub['err_hi'].values])
        ax.errorbar(
            sub['sparsity_val'], sub['median_ii_diff'],
            yerr=yerr,
            fmt=s['marker'] + '-',
            color=s['color'],
            capsize=4,
            capthick=1.5,
            linewidth=1.8,
            markersize=7,
            label=s['label'],
            markeredgecolor='white',
            markeredgewidth=0.8,
            elinewidth=1.3,
        )

    ax.set_xlabel('Sparsity Level', fontsize=13)
    ax.set_xticks([0.15, 0.20, 0.25, 0.30])
    ax.set_xticklabels(['15%', '20%', '25%', '30%'])
    ax.set_title(model_labels[model], fontsize=12, fontweight='bold', pad=8)
    ax.legend(fontsize=10, frameon=False, loc='upper left')

axes[0].set_ylabel(r'Interaction Index (median $\Delta$II)', fontsize=13)

fig.tight_layout(w_pad=3.0)

# Save
outdir = '/root/autodl-tmp/pacs/artifacts'
os.makedirs(outdir, exist_ok=True)
pdf_path = os.path.join(outdir, 'figure1_ii_scatter.pdf')
png_path = os.path.join(outdir, 'figure1_ii_scatter.png')
fig.savefig(pdf_path, bbox_inches='tight', dpi=300)
fig.savefig(png_path, bbox_inches='tight', dpi=300)
print(f"Saved: {pdf_path}")
print(f"Saved: {png_path}")

# Print data summary
print("\n=== Data Summary ===")
for model in models:
    print(f"\n{model_labels[model]}:")
    for masking in ['imp', 'rand']:
        sub = df[(df['model'] == model) & (df['masking'] == masking)].sort_values('sparsity_val')
        label = style[masking]['label']
        for _, row in sub.iterrows():
            sig = row['significance']
            print(f"  {label} @ {row['sparsity_val']:.0%}: {row['median_ii_diff']:.3f} [{row['ci_lo']:.3f}, {row['ci_hi']:.3f}] {sig}")
