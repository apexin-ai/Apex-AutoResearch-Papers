import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
})

regimes = ['LoRA (r=16)', 'Full-FT\nlr=5e-6', 'Full-FT\nlr=2e-5']
curation_gaps = [-3.40, -0.46, +0.63]

bar_colors = ['#D55E00', '#E69F00', '#0072B2']
edge_colors = ['#A34800', '#B87E00', '#005A8C']

fig, ax = plt.subplots(figsize=(5, 3.5))

x = np.arange(len(regimes))
bars = ax.bar(x, curation_gaps, width=0.6, color=bar_colors,
              edgecolor=edge_colors, linewidth=1.0, zorder=2)

ax.axhline(0, color='black', linestyle='--', linewidth=0.8, zorder=1)

ax.set_ylim(-4.5, 1.8)

for i, (bar, val) in enumerate(zip(bars, curation_gaps)):
    offset = 0.18 if val >= 0 else -0.18
    va = 'bottom' if val >= 0 else 'top'
    sign = '+' if val > 0 else ''
    ax.text(bar.get_x() + bar.get_width() / 2, val + offset,
            f'{sign}{val:.2f}', ha='center', va=va,
            fontsize=10, fontweight='bold')

param_labels = ['Params: 1.67%', 'Params: 100%', 'Params: 100%']
regime_labels = ['LoRA (r=16)', 'Full-FT\nlr=5e-6', 'Full-FT\nlr=2e-5']
combined_labels = [f'{r}\n{p}' for r, p in zip(regime_labels, param_labels)]

ax.set_xticks(x)
ax.set_xticklabels(combined_labels, fontsize=9.5)

ax.set_ylabel('Curation gap (pp)')
ax.grid(False)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/figures/paper'
plt.savefig(f'{outdir}/fig3_direction_reversal.pdf')
plt.savefig(f'{outdir}/fig3_direction_reversal.png')
plt.close()
print('Done: fig3_direction_reversal.pdf + .png')
