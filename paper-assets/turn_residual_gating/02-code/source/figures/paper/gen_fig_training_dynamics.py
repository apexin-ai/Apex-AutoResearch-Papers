"""Generate training dynamics figure: TF vs AR GAR collapse (paired bar + slope)."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import matplotlib.patheffects as pe
import numpy as np

apply_style()

models = ['Base', 'TG', 'UG', 'LoRA']

# TF GAR-ours (heldout eval, from registry phase2_4way_eval_heldout)
tf_gar = [0.0128, 0.5035, 0.5053, 0.4978]

# AR GAR-ours (autoregressive generation eval)
ar_gar = [0.019, 0.064, 0.033, 0.037]

gaps = [None, 7.8, 15.5, 13.5]

fig, ax = plt.subplots(figsize=(3.33, 2.5))

x = np.arange(len(models))
w = 0.26

bars_tf = ax.bar(x - w/2, tf_gar, w, color=C_TF, label='Teacher-forced',
                 zorder=2, alpha=0.88, edgecolor='white', linewidth=0.5)
bars_ar = ax.bar(x + w/2, ar_gar, w, color=C_AR, label='Autoregressive',
                 zorder=2, alpha=0.88, edgecolor='white', linewidth=0.5)

ax.set_yscale('log')
ax.set_ylim(0.005, 1.2)
ax.set_xlim(-0.55, 3.95)

# Background regime bands
ax.axhspan(0.005, 0.08, color='#FFF3E0', alpha=0.25, zorder=0)
ax.axhspan(0.08, 1.2, color='#E8F5E9', alpha=0.25, zorder=0)

# Slope lines connecting TF to AR (only where collapse occurs)
for i in range(1, len(models)):
    ax.plot([x[i] - w/2, x[i] + w/2], [tf_gar[i], ar_gar[i]],
            '--', color=C_GRAY, linewidth=0.8, zorder=3)

# Value labels on TF bars
for i, v in enumerate(tf_gar):
    if v > 0.1:
        ax.text(x[i] - w/2, v * 0.72, f'.{round(v*100):02d}', ha='center',
                va='top', fontsize=5.5, color='white', fontweight='bold')
    else:
        ax.text(x[i] - w/2, v * 1.35, f'{v:.3f}', ha='center', va='bottom',
                fontsize=5.5, color='#333333')

# Value labels on AR bars
for i, v in enumerate(ar_gar):
    if v < 0.025:
        ax.text(x[i] + w/2, v * 1.35, f'{v:.3f}', ha='center', va='bottom',
                fontsize=5, color='#333333')
    else:
        ax.text(x[i] + w/2, v * 0.65, f'.{round(v*1000):03d}', ha='center',
                va='top', fontsize=5, color='white', fontweight='bold')

# Gap annotations
for i, gap in enumerate(gaps):
    if gap is not None:
        geo_mean = np.sqrt(tf_gar[i] * ar_gar[i])
        t = ax.text(x[i] + w/2 + 0.14, geo_mean, f'{gap:.1f}×',
                    fontsize=6.5, fontweight='bold', color=C_AR,
                    ha='left', va='center')
        t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylabel('GAR (ours)')

ax.legend(loc='lower right',
          handletextpad=0.3, borderpad=0.4)

import matplotlib.ticker
ax.yaxis.set_minor_locator(matplotlib.ticker.LogLocator(base=10, subs=np.arange(2, 10)))
ax.grid(axis='y', which='major', alpha=0.15, zorder=0)
ax.grid(axis='y', which='minor', alpha=0.06, zorder=0)

plt.tight_layout()
save_fig(fig, 'fig_training_dynamics')
