import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats

df = pd.read_csv('/root/gen-depth-fingerprint/data/features_all_models.csv')
features = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay', 'ttr', 'hapax_ratio']
feature_labels = ['Entropy Mean', 'Entropy Std', 'Entropy Min', 'Entropy Max', 'Tail Decay', 'TTR', 'Hapax Ratio']

fig, axes = plt.subplots(4, 2, figsize=(10, 12))
axes_flat = axes.flatten()
depth_colors = {0: '#009E73', 1: '#0072B2', 2: '#D55E00', 3: '#CC79A7', 4: '#F0E442'}
palette = [depth_colors[d] for d in sorted(df['depth'].unique())]

for i, (feat, label) in enumerate(zip(features, feature_labels)):
    ax = axes_flat[i]
    sns.violinplot(data=df, x='depth', y=feat, ax=ax, palette=palette,
                   inner='quartile', linewidth=0.8, cut=0, density_norm='width')
    ax.set_xlabel('Generation Depth', fontsize=10)
    ax.set_ylabel(label, fontsize=10)
    ax.set_title(label, fontsize=11, fontweight='bold')
    ax.tick_params(labelsize=9)
    rho, _ = stats.spearmanr(df['depth'], df[feat])
    ax.text(0.98, 0.95, f'ρ = {rho:.3f}', transform=ax.transAxes,
            ha='right', va='top', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8))

axes_flat[-1].set_visible(False)
plt.tight_layout(pad=1.5)
plt.savefig('/root/gen-depth-fingerprint/chart/fig_appendix_violin.pdf', bbox_inches='tight', dpi=300)
print("Saved fig_appendix_violin.pdf")
