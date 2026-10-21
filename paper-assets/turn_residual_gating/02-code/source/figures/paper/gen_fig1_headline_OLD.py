"""Generate Figure 1: Headline result — TF-AR collapse + steering recovery.

Layout: (a) TF vs AR bar chart | (b-top) GAR recovery | (b-bottom) PPL cost.
"""
from palette import *
import matplotlib.patheffects as pe
import matplotlib.ticker as ticker
import numpy as np

apply_style()

fig = plt.figure(figsize=(7.2, 3.4))
gs = fig.add_gridspec(2, 2, width_ratios=[1.25, 1], height_ratios=[1, 1],
                       hspace=0.20, wspace=0.48)
ax_a = fig.add_subplot(gs[:, 0])
ax_b1 = fig.add_subplot(gs[0, 1])
ax_b2 = fig.add_subplot(gs[1, 1], sharex=ax_b1)

# ======================================================================
# Panel (a): TF vs AR GAR bar chart
# ======================================================================
configs = ['Base', 'TG', '+PCGrad', 'UG', 'LoRA']
tf_gar  = [0.01, 0.50, 0.50, 0.49, 0.50]
ar_gar  = [0.019, 0.064, 0.030, 0.033, 0.037]
gaps    = [None, 7.8, 16.7, 14.8, 13.5]

x = np.arange(len(configs))
w = 0.28

bars_tf = ax_a.bar(x - w/2, tf_gar, w, color=C_TF, label='Teacher-forced (TF)',
                   zorder=2, edgecolor='white', linewidth=0.4)
bars_ar = ax_a.bar(x + w/2, ar_gar, w, color=C_AR, label='Autoregressive (AR)',
                   zorder=2, edgecolor='white', linewidth=0.4)

ax_a.set_yscale('log')
ax_a.set_ylim(0.005, 1.8)
ax_a.set_xlim(-0.55, 4.70)

ax_a.axhspan(0.005, 0.08, color='#FFF3E0', alpha=0.15, zorder=0)
ax_a.axhspan(0.08, 1.8, color='#E8F5E9', alpha=0.15, zorder=0)

for i in range(1, len(configs)):
    ax_a.plot([x[i] - w/2, x[i] + w/2], [tf_gar[i], ar_gar[i]],
             color='#CCCCCC', linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))

for i, v in enumerate(tf_gar):
    label = f'.{round(v*100):02d}' if v >= 0.1 else f'{v:.2f}'
    ax_a.text(x[i] - w/2, v * 1.15, label, ha='center', va='bottom',
              fontsize=5.5, color='#3D7D3D', fontweight='bold')

for i, v in enumerate(ar_gar):
    label = f'.{round(v*1000):03d}'
    ax_a.text(x[i] + w/2, v * 1.20, label, ha='center', va='bottom',
              fontsize=5, color='#A05050')

for i, gap in enumerate(gaps):
    if gap is not None:
        geo_mean = np.sqrt(tf_gar[i] * ar_gar[i])
        t = ax_a.text(x[i] + w/2 + 0.16, geo_mean, f'{gap:.0f}×',
                      fontsize=7.5, fontweight='bold', color='#B35A4A',
                      ha='left', va='center')
        t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax_a.set_xticks(x)
ax_a.set_xticklabels(configs, fontsize=8)
ax_a.set_ylabel('GAR-ours', fontsize=9)
ax_a.set_title('(a)  Training succeeds, inference collapses',
               fontsize=9.5, fontweight='bold', pad=8, loc='left')

ax_a.legend(loc='lower left', framealpha=0.95, edgecolor='#dddddd',
            handletextpad=0.4, borderpad=0.35, fontsize=6.5, fancybox=True)

ax_a.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))
ax_a.grid(axis='y', which='major', alpha=0.10, zorder=0)

# ======================================================================
# Panel (b1): GAR recovery with steering
# ======================================================================
beta    = [0.0, 2.0, 3.0, 4.0, 5.0, 10.0]
gar     = [0.064, 0.128, 0.556, 0.644, 0.727, 0.961]
gar_std = [0.081, 0.110, 0.060, 0.061, 0.061, 0.015]

ax_b1.axvspan(2, 5, alpha=0.06, color=C_SWEET, zorder=0)
ax_b1.axhline(0.50, color=C_GRAY, linestyle=':', linewidth=0.6, zorder=1)
ax_b1.text(0.2, 0.535, 'TF level', fontsize=5.5, color=C_GRAY, ha='left')

ax_b1.errorbar(beta, gar, yerr=gar_std, fmt='-o', color=C_GAR,
               markersize=4.5, markerfacecolor=C_GAR, markeredgecolor='white',
               markeredgewidth=0.5, capsize=2, capthick=0.6, elinewidth=0.6,
               zorder=3)

ax_b1.plot(3, 0.556, 'o', color=C_GAR, markersize=7, markerfacecolor='none',
           markeredgecolor=C_GAR, markeredgewidth=1.2, zorder=4)

ax_b1.text(7.5, 0.18, r'$\beta$=3: 8.7× recovery',
           fontsize=6, color='#444444', ha='center',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                     edgecolor='#dddddd', alpha=0.9, linewidth=0.4))
ax_b1.annotate('', xy=(3.2, 0.53), xytext=(5.8, 0.22),
               arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=0.5,
                               connectionstyle='arc3,rad=-0.1'))

ax_b1.set_ylabel('GAR', fontsize=8)
ax_b1.set_ylim(-0.02, 1.08)
ax_b1.set_xlim(-0.5, 10.8)
ax_b1.tick_params(labelsize=7)
ax_b1.set_title('(b)  Steering recovers attention',
                fontsize=9.5, fontweight='bold', pad=6, loc='left')
plt.setp(ax_b1.get_xticklabels(), visible=False)
ax_b1.grid(axis='y', alpha=0.08, zorder=0)

# ======================================================================
# Panel (b2): PPL cost with steering
# ======================================================================
ppl     = [1.43, 1.48, 1.56, 1.67, 1.77, 3.45]
ppl_std = [0.10, 0.14, 0.17, 0.22, 0.27, 1.78]

ax_b2.axvspan(2, 5, alpha=0.06, color=C_SWEET, zorder=0)
ax_b2.axhline(ppl[0], color=C_GRAY, linestyle=':', linewidth=0.6, zorder=1)

ax_b2.errorbar(beta, ppl, yerr=ppl_std, fmt='-s', color=C_PPL,
               markersize=3.5, markerfacecolor=C_PPL, markeredgecolor='white',
               markeredgewidth=0.5, capsize=2, capthick=0.6, elinewidth=0.6,
               zorder=3)

ax_b2.plot(3, 1.56, 's', color=C_PPL, markersize=6, markerfacecolor='none',
           markeredgecolor=C_PPL, markeredgewidth=1.0, zorder=4)
ax_b2.text(5.5, 3.2, '9% PPL cost', fontsize=6, color='#555555',
           ha='center',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                     edgecolor='#dddddd', alpha=0.9, linewidth=0.4))
ax_b2.annotate('', xy=(3.2, 1.65), xytext=(4.8, 3.0),
               arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=0.5,
                               connectionstyle='arc3,rad=0.1'))

ax_b2.set_ylabel('PPL', fontsize=8)
ax_b2.set_xlabel(r'$\beta$ (steering strength)', fontsize=8)
ax_b2.set_ylim(0.8, 5.5)
ax_b2.set_xticks([0, 2, 3, 4, 5, 10])
ax_b2.tick_params(labelsize=7)
ax_b2.grid(axis='y', alpha=0.08, zorder=0)

for ax in [ax_b1, ax_b2]:
    ax.axvline(3, color='#DDDDDD', linewidth=0.4, linestyle=':', zorder=0)

save_fig(fig, 'fig1_headline')
