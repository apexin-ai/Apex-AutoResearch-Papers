"""Generate Figure 6: Gate Turn Conditioning + Distribution Shift (horizontal 2-panel, double-column)."""
from palette import *
import matplotlib.patheffects as pe
import matplotlib.ticker as ticker
import numpy as np

apply_style()

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7.0, 2.2),
                                   gridspec_kw={'width_ratios': [1, 1.15]})

# ======================================================================
# Panel (a): Gate Turn Conditioning — Cleveland dot plot (top-5 layers)
# ======================================================================
layers = ['L9', 'L20', 'L12', 'L14', 'L23']
turn1  = [0.8578, 0.8228, 0.8200, 0.7473, 0.7693]
turn21 = [0.9679, 0.9393, 0.9465, 0.9276, 0.9793]
diffs  = [-0.1101, -0.1165, -0.1265, -0.1803, -0.2100]

y = np.arange(len(layers))

for i in range(len(layers)):
    ax_a.plot([turn1[i], turn21[i]], [y[i], y[i]],
             color='#DDDDDD', linewidth=2.0, zorder=1, solid_capstyle='round')

ax_a.scatter(turn1, y, color=C_PURPLE, s=50, zorder=3,
            edgecolors='white', linewidths=0.6, label='Turn 1 (early)')
ax_a.scatter(turn21, y, color=C_GREEN, s=50, zorder=3,
            edgecolors='white', linewidths=0.6, label='Turn 21 (late)')

for i, d in enumerate(diffs):
    ax_a.text(1.012, y[i], f'{d:+.2f}', fontsize=6.5, va='center',
              color='#666666', family='monospace')

ax_a.set_yticks(y)
ax_a.set_yticklabels(layers, fontsize=8)
ax_a.set_xlim(0.70, 1.02)
ax_a.set_xlabel('Gate value', fontsize=8)
ax_a.set_title('(a) Gates become passive at late turns',
               fontsize=9, fontweight='bold', pad=8, loc='left')
ax_a.legend(loc='lower right', fontsize=6.5, frameon=False,
           handletextpad=0.3, borderpad=0.35)

ax_a.text(0.97, 0.05, 'p = 3.7e-8, r = 0.975',
          transform=ax_a.transAxes, fontsize=6, va='bottom', ha='right',
          color=C_GRAY, fontstyle='italic')

ax_a.grid(axis='x', alpha=0.08, zorder=0)

# ======================================================================
# Panel (b): Distribution Shift — Grouped bar chart (log scale)
# ======================================================================
models = ['Base', 'TG', 'PCGrad', 'UG', 'LoRA']
iid    = [0.0122, 0.5035, 0.5002, 0.5053, 0.4978]
mg     = [0.0122, 0.0157, 0.0151, 0.0149, 0.0245]

x = np.arange(len(models))
w = 0.30

import matplotlib.patches as mpatches
variant_colors = [C_BASE, C_TG, C_PC, C_UG, C_LO]
bars_iid = ax_b.bar(x - w/2, iid, w, color=variant_colors,
                     zorder=2, edgecolor='white', linewidth=0.4)
bars_mg = ax_b.bar(x + w/2, mg, w, color=variant_colors,
                    zorder=2, edgecolor='white', linewidth=0.4, alpha=0.55)

ax_b.set_yscale('log')
ax_b.set_ylim(0.005, 1.2)
ax_b.set_xticks(x)
ax_b.set_xticklabels(models, fontsize=8)
ax_b.set_ylabel('GAR (ours)', fontsize=9)
ax_b.set_title('(b) 20–33× gap across all variants',
               fontsize=9, fontweight='bold', pad=8, loc='left')
p_iid = mpatches.Patch(facecolor=C_TG, edgecolor='white', linewidth=0.4, label='IID eval')
p_mg  = mpatches.Patch(facecolor=C_TG, edgecolor='white', linewidth=0.4, alpha=0.55, label='Model-gen.')
ax_b.legend(handles=[p_iid, p_mg], loc='upper right', fontsize=6.5, frameon=False,
           handletextpad=0.3, borderpad=0.35, ncol=1)

for i, v in enumerate(iid):
    if v > 0.1:
        label = f'{v:.2f}'
        ax_b.text(i - w/2, v * 1.15, label, ha='center', va='bottom',
                 fontsize=5.5, color=C_TF_DARK)

for i, v in enumerate(mg):
    if i > 0:
        ax_b.text(i + w/2, v * 1.25, f'{v:.4f}', ha='center', va='bottom',
                 fontsize=5, color=C_AR_DARK)

for i in range(1, len(models)):
    gap = iid[i] / mg[i]
    geo_mean = np.sqrt(iid[i] * mg[i])
    t = ax_b.text(i + w/2 + 0.17, geo_mean, f'{gap:.0f}×', fontsize=7,
                  fontweight='bold', color=C_AR_DARK, ha='left', va='center')
    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

    ax_b.plot([x[i] - w/2, x[i] + w/2], [iid[i], mg[i]],
             color='#CCCCCC', linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))

ax_b.axhspan(0.005, 0.05, color='#FFF3E0', alpha=0.15, zorder=0)
ax_b.axhspan(0.05, 1.2, color='#E8F5E9', alpha=0.15, zorder=0)

ax_b.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))
ax_b.grid(axis='y', which='major', alpha=0.10, zorder=0)

plt.tight_layout(w_pad=2.5)

save_fig(fig, 'fig3_gate_shift')
