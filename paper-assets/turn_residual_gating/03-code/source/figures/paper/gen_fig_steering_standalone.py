"""Standalone steering figure: GAR recovery + PPL cost vs beta."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(4.5, 4.0), sharex=True,
                                gridspec_kw={'hspace': 0.12, 'height_ratios': [1, 0.8]})

beta    = [0.0, 2.0, 3.0, 4.0, 5.0, 10.0]
gar     = [0.064, 0.128, 0.556, 0.644, 0.727, 0.961]
gar_std = [0.081, 0.110, 0.060, 0.061, 0.061, 0.015]
ppl     = [1.43, 1.48, 1.56, 1.67, 1.77, 3.45]
ppl_std = [0.10, 0.14, 0.17, 0.22, 0.27, 1.78]

# ── Top: GAR recovery ──
ax1.axvspan(2, 5, alpha=0.08, color=C_SWEET, zorder=0)
ax1.axhline(0.50, color=C_GRAY, linestyle=':', linewidth=0.6, zorder=1)
ax1.text(0.3, 0.535, 'TF level', fontsize=6.5, color=C_GRAY, ha='left')

C_GAR_VIVID = '#2166AC'
ax1.errorbar(beta, gar, yerr=gar_std, fmt='-o', color=C_GAR_VIVID,
             markersize=6, markerfacecolor=C_GAR_VIVID, markeredgecolor='white',
             markeredgewidth=0.6, capsize=2.5, capthick=0.8, elinewidth=0.8,
             zorder=3, linewidth=1.8)

ax1.plot(3, 0.556, 'o', color=C_GAR_VIVID, markersize=9, markerfacecolor='none',
         markeredgecolor=C_GAR_VIVID, markeredgewidth=1.5, zorder=4)

ax1.text(7.5, 0.20, r'$\beta$=3: 8.7$\times$ recovery',
         fontsize=7, color='#555555', ha='center',
         bbox=dict(boxstyle='round,pad=0.25', facecolor='#FAFAF5', alpha=0.9, linewidth=0.3, edgecolor='#CCCCCC'))
ax1.annotate('', xy=(3.2, 0.53), xytext=(5.8, 0.24),
             arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=0.6,
                             connectionstyle='arc3,rad=-0.1'))

ax1.set_ylabel('GAR-ours', fontsize=9)
ax1.set_ylim(-0.02, 1.08)
ax1.set_xlim(-0.5, 10.8)
ax1.tick_params(labelsize=8)
ax1.grid(axis='y', alpha=0.08, zorder=0)
plt.setp(ax1.get_xticklabels(), visible=False)

# ── Bottom: PPL cost ──
ax2.axvspan(2, 5, alpha=0.08, color=C_SWEET, zorder=0)
ax2.axhline(ppl[0], color=C_GRAY, linestyle=':', linewidth=0.6, zorder=1)

C_PPL_VIVID = '#B2182B'
ax2.errorbar(beta, ppl, yerr=ppl_std, fmt='-s', color=C_PPL_VIVID,
             markersize=5, markerfacecolor=C_PPL_VIVID, markeredgecolor='white',
             markeredgewidth=0.6, capsize=2.5, capthick=0.8, elinewidth=0.8,
             zorder=3, linewidth=1.8)

ax2.plot(3, 1.56, 's', color=C_PPL_VIVID, markersize=8, markerfacecolor='none',
         markeredgecolor=C_PPL_VIVID, markeredgewidth=1.3, zorder=4)
ax2.text(6.0, 3.2, '9% PPL cost', fontsize=7, color='#555555',
         ha='center',
         bbox=dict(boxstyle='round,pad=0.25', facecolor='#FAFAF5', alpha=0.9, linewidth=0.3, edgecolor='#CCCCCC'))
ax2.annotate('', xy=(3.2, 1.65), xytext=(5.0, 3.0),
             arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=0.6,
                             connectionstyle='arc3,rad=0.1'))

ax2.set_ylabel('PPL', fontsize=9)
ax2.set_xlabel(r'$\beta$ (steering strength)', fontsize=9)
ax2.set_ylim(0.8, 5.5)
ax2.set_xticks([0, 2, 3, 4, 5, 10])
ax2.tick_params(labelsize=8)
ax2.grid(axis='y', alpha=0.08, zorder=0)

for ax in [ax1, ax2]:
    ax.axvline(3, color='#DDDDDD', linewidth=0.4, linestyle=':', zorder=0)

save_fig(fig, 'fig_steering_standalone')
