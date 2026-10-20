"""DDR trajectory with fonttype fix."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'mathtext.fontset': 'cm',
})

DATA = '/root/gen-depth-fingerprint/data/features_all_models.csv'
df = pd.read_csv(DATA)

PALETTE = ['#0072B2','#56B4E9','#009E73','#E69F00','#D55E00','#CC79A7','#F0E442','#882255']
GENERATORS = [
    ('pythia-2.8b','Py-2.8B',PALETTE[0]),('pythia-1b','Py-1B',PALETTE[1]),
    ('olmo-2-1b','OLMo',PALETTE[2]),('qwen3-0.6b','Qw-0.6B',PALETTE[3]),
    ('qwen3-1.7b','Qw-1.7B',PALETTE[4]),('qwen3-8b','Qw-8B',PALETTE[5]),
    ('llama-3.2-3b','Llama','#999900'),('mistral-7b-v0.3','Mistral',PALETTE[7]),
]
C_DRIFT_MEAN = '#0072B2'
C_STAT_MEAN = '#E69F00'

features = [
    ('entropy_mean', r'Entropy Mean ($\bar{H}$)', 'drifting'),
    ('hapax_ratio', r'Hapax Ratio', 'drifting'),
    ('entropy_max', r'Entropy Max ($H_{\max}$)', 'stationary'),
    ('tail_decay', r'Tail Decay', 'stationary'),
]
depths = sorted(df['depth'].unique())

fig, axes = plt.subplots(2, 2, figsize=(6.8, 4.0), sharex=True)
panel_labels = ['(a)', '(b)', '(c)', '(d)']

for idx, (feat, label, zone) in enumerate(features):
    ax = axes[idx // 2][idx % 2]
    c_mean = C_DRIFT_MEAN if zone == 'drifting' else C_STAT_MEAN
    all_means = []
    for gen_name, gen_short, gen_color in GENERATORS:
        sub = df[df['model_name'] == gen_name]
        means = sub.groupby('depth')[feat].mean().reindex(depths)
        all_means.append(means.values)
        ax.plot(depths, means.values, color=gen_color, linewidth=0.8, alpha=0.5,
                marker='o', markersize=2.5, markeredgewidth=0, zorder=2)
    grand = np.mean(all_means, axis=0)
    ax.plot(depths, grand, color=c_mean, linewidth=1.4, alpha=0.85, zorder=4)
    ax.scatter(depths, grand, color=c_mean, marker='D', s=30,
               edgecolors='white', linewidths=0.6, zorder=5)
    all_depth_vals, all_feat_vals = [], []
    for gen_name, _, _ in GENERATORS:
        sub = df[df['model_name'] == gen_name]
        all_depth_vals.extend(sub['depth'].values)
        all_feat_vals.extend(sub[feat].values)
    rho, _ = spearmanr(all_depth_vals, all_feat_vals)
    ax.text(0.97, 0.95, rf'$\rho = {rho:.3f}$', transform=ax.transAxes, fontsize=6.5,
            va='top', ha='right', color='#555',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='#ddd', linewidth=0.4, alpha=0.9))
    ax.set_title(f'{panel_labels[idx]} {label}', fontsize=8, pad=4, loc='left', fontweight='normal')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#999'); ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_color('#999'); ax.spines['bottom'].set_linewidth(0.5)
    ax.tick_params(length=3, width=0.5, color='#999')
    ax.set_xticks(depths)
    if idx >= 2:
        ax.set_xlabel('Generation Depth', fontsize=7.5)

for ax in axes[0]:
    ax.xaxis.set_tick_params(labelbottom=False)

fig.text(0.005, 0.73, 'Drifting', fontsize=7.5, fontweight='bold',
         color='#0072B2', rotation=90, va='center', ha='left')
fig.text(0.005, 0.30, 'Stationary', fontsize=7.5, fontweight='bold',
         color='#E69F00', rotation=90, va='center', ha='left')

from matplotlib.lines import Line2D
handles = []
for _, gen_short, gen_color in GENERATORS:
    handles.append(Line2D([0], [0], color=gen_color, linewidth=0.8, alpha=0.6,
                          marker='o', markersize=2.5, markeredgewidth=0, label=gen_short))
handles.append(Line2D([0], [0], color='#0072B2', linewidth=0, marker='D',
                       markersize=5, markeredgecolor='white', markeredgewidth=0.6, label='Grand Mean'))
fig.legend(handles=handles, loc='lower center', ncol=5, fontsize=5.5, frameon=True,
           framealpha=0.95, edgecolor='#ddd', fancybox=False,
           handletextpad=0.3, columnspacing=1.0, bbox_to_anchor=(0.5, -0.02))
plt.tight_layout(rect=[0.03, 0.06, 1, 1])
plt.subplots_adjust(hspace=0.25, wspace=0.28)

out = '/root/gen-depth-fingerprint/chart'
fig.savefig(f'{out}/fig_ddr_trajectory.pdf', format='pdf')
fig.savefig(f'{out}/fig_ddr_trajectory.png', format='png')
print(f'Saved trajectory figure to {out}/')
