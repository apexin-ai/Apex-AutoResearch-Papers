"""Figure 1 (single): TF vs AR GAR gap bar chart — no steering panels."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import matplotlib.patheffects as pe
import matplotlib.ticker as ticker
import numpy as np

apply_style()

fig, ax = plt.subplots(figsize=(6.0, 2.8))

configs = ['Base', 'ThreadGate', '+PCGrad', 'Uniform Gate', 'LoRA-only']
config_colors = [C_BASE, C_TG, C_PC, C_UG, C_LO]
tf_gar  = [0.01, 0.50, 0.50, 0.49, 0.50]
ar_gar  = [0.019, 0.064, 0.030, 0.033, 0.037]
gaps    = [None, 7.8, 16.7, 14.8, 13.5]

x = np.arange(len(configs))
w = 0.30

bars_tf = ax.bar(x - w/2, tf_gar, w, color=C_TF, label='Teacher-forced (TF)',
                 zorder=2, edgecolor='white', linewidth=0.5)
bars_ar = ax.bar(x + w/2, ar_gar, w, color=C_AR, label='Autoregressive (AR)',
                 zorder=2, edgecolor='white', linewidth=0.5)

ax.set_yscale('log')
ax.set_ylim(0.005, 1.8)
ax.set_xlim(-0.6, 4.8)

ax.axhspan(0.005, 0.08, color='#FFF3E0', alpha=0.12, zorder=0)
ax.axhspan(0.08, 1.8, color='#E8F5E9', alpha=0.12, zorder=0)

for i in range(1, len(configs)):
    ax.plot([x[i] - w/2, x[i] + w/2], [tf_gar[i], ar_gar[i]],
            color='#CCCCCC', linewidth=0.6, zorder=3, linestyle=(0, (3, 2)))

for i, v in enumerate(tf_gar):
    label = f'.{round(v*100):02d}' if v >= 0.1 else f'{v:.2f}'
    ax.text(x[i] - w/2, v * 1.15, label, ha='center', va='bottom',
            fontsize=7, color=C_TF_DARK, fontweight='bold')

for i, v in enumerate(ar_gar):
    label = f'.{round(v*1000):03d}'
    ax.text(x[i] + w/2, v * 1.20, label, ha='center', va='bottom',
            fontsize=6.5, color=C_AR_DARK)

for i, gap in enumerate(gaps):
    if gap is not None:
        geo_mean = np.sqrt(tf_gar[i] * ar_gar[i])
        t = ax.text(x[i] + w/2 + 0.18, geo_mean, f'{gap:.0f}×',
                    fontsize=9, fontweight='bold', color=C_AR_DARK,
                    ha='left', va='center')
        t.set_path_effects([pe.withStroke(linewidth=2.8, foreground='white')])

ax.set_xticks(x)
ax.set_xticklabels(configs, fontsize=9)
ax.set_ylabel('GAR-ours (log scale)', fontsize=10)

ax.legend(loc='upper left',
          handletextpad=0.4, borderpad=0.4, fontsize=8)

ax.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))
ax.grid(axis='y', which='major', alpha=0.10, zorder=0)

save_fig(fig, 'fig1_headline_single')
