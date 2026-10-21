"""Generate Figure 3: ResNet-50 single-panel SR divergence vs weight-swap impact."""
import sys
sys.path.insert(0, '/root/spectral_optim_vision_geometry')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from plot_style import apply_style
apply_style()

csv_path = "/root/spectral_optim_vision_geometry/results/resnet50_bn_recal_ablation.csv"
df = pd.read_csv(csv_path)

x = df['sr_divergence'].values
y = df['drop_recal'].values

rho, p_val = stats.spearmanr(x, y)
print(f"Spearman rho = {rho:.4f}, p = {p_val:.2e}, n = {len(x)}")

fig, ax = plt.subplots(figsize=(5, 4))

ax.scatter(x, y, alpha=0.6, s=40, color='#0077BB', edgecolors='white',
           linewidths=0.4, zorder=3)

slope, intercept, _, _, _ = stats.linregress(x, y)
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = slope * x_fit + intercept
ax.plot(x_fit, y_fit, color='#CC3311', linestyle='--', linewidth=2,
        label='OLS fit', zorder=4)

n = len(x)
x_mean = x.mean()
se = np.sqrt(np.sum((y - (slope * x + intercept))**2) / (n - 2))
ci = stats.t.ppf(0.975, n - 2) * se * np.sqrt(
    1/n + (x_fit - x_mean)**2 / np.sum((x - x_mean)**2))
ax.fill_between(x_fit, y_fit - ci, y_fit + ci, alpha=0.3,
                color='salmon', linewidth=0, zorder=2)

for idx, row in df.iterrows():
    if 'downsample' in row['layer_name']:
        short = row['layer_name'].replace('layer', 'L').replace('.downsample.0', '.ds')
        if short in ('L2.0.ds', 'L3.0.ds'):
            ax.annotate(short, (row['sr_divergence'], row['drop_recal']),
                       fontsize=9, xytext=(8, 6), textcoords='offset points',
                       color='#555555', style='italic',
                       arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8))

stat_text = f'$\\rho$ = {rho:+.2f}\n$p$ = {p_val:.1e}\n$n$ = {n}'
ax.text(0.05, 0.95, stat_text,
        transform=ax.transAxes, fontsize=11, va='top', ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                  alpha=0.8, edgecolor='gray'))

ax.set_xlabel(r'SR divergence $|\Delta \mathrm{sr}_l|$', fontsize=12)
ax.set_ylabel(r'Accuracy impact $\Delta a_l$' + '\n(pp, BN-corrected)', fontsize=12)
ax.set_ylim(0, 25)
ax.set_yticks([0, 5, 10, 15, 20, 25])
ax.set_xlim(0, 250)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10, loc='upper right', framealpha=0.9, edgecolor='none')

plt.tight_layout()
out = "/root/spectral_optim_vision_geometry/paper/figures"
fig.savefig(f'{out}/fig3_spectral_divergence.pdf')
fig.savefig(f'{out}/fig3_spectral_divergence.png')
fig.savefig('/root/spectral_optim_vision_geometry/figures/fig3_spectral_divergence.pdf')
fig.savefig('/root/spectral_optim_vision_geometry/figures/fig3_spectral_divergence.png')
plt.close(fig)
print(f'Saved to {out}/fig3_spectral_divergence.{{pdf,png}}')
