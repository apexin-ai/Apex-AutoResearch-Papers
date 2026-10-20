import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

sizes = [4, 8, 14]
cls_acc = [88.68, 89.94, 89.21]
cwm_acc = [87.36, 87.33, 89.26]

fig, ax = plt.subplots(figsize=(5, 3.5))

ax.axvspan(12.5, 15.5, color='#f0f0f0', zorder=0)
ax.axvline(x=13, color='#cccccc', linestyle=':', linewidth=0.8, zorder=0)
ax.text(14, 90.65, 'exploratory', fontsize=7, color='#888888',
        ha='center', fontstyle='italic')

ax.fill_between(sizes, cls_acc, cwm_acc, color='#e0e0e0', alpha=0.5, zorder=1)

ax.plot(sizes[:2], cls_acc[:2], 'o-', color='#2c7fb8', linewidth=1.8,
        markersize=7, markerfacecolor='#2c7fb8', markeredgecolor='#2c7fb8',
        label='CLS', zorder=3)
ax.plot(sizes[:2], cwm_acc[:2], 's-', color='#d95f02', linewidth=1.8,
        markersize=7, markerfacecolor='#d95f02', markeredgecolor='#d95f02',
        label='CWM', zorder=3)

ax.plot(sizes[2], cls_acc[2], 'o', color='#2c7fb8', markersize=7,
        markerfacecolor='white', markeredgecolor='#2c7fb8', markeredgewidth=1.8, zorder=3)
ax.plot(sizes[2], cwm_acc[2], 's', color='#d95f02', markersize=7,
        markerfacecolor='white', markeredgecolor='#d95f02', markeredgewidth=1.8, zorder=3)

ax.plot([sizes[1], sizes[2]], [cls_acc[1], cls_acc[2]], '--', color='#2c7fb8',
        linewidth=1.8, zorder=2)
ax.plot([sizes[1], sizes[2]], [cwm_acc[1], cwm_acc[2]], '--', color='#d95f02',
        linewidth=1.8, zorder=2)

mid_4b = (cls_acc[0] + cwm_acc[0]) / 2
ax.annotate('1.32 pp', xy=(4, mid_4b), fontsize=7.5, fontweight='bold',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#aaaaaa', lw=0.5))

mid_8b = (cls_acc[1] + cwm_acc[1]) / 2
ax.annotate('2.62 pp', xy=(8, mid_8b), fontsize=7.5, fontweight='bold',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#aaaaaa', lw=0.5))

mid_14b = (cls_acc[2] + cwm_acc[2]) / 2
ax.annotate('$\\approx$0 pp', xy=(14, mid_14b), xytext=(13.2, 90.15),
            fontsize=7.5, fontweight='bold', ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8),
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#aaaaaa', lw=0.5))

ax.set_xlabel('Model Size', fontsize=10)
ax.set_ylabel('Accuracy (%)', fontsize=10)
ax.set_xticks(sizes)
ax.set_xticklabels(['4B', '8B', '14B'], fontsize=9)
ax.set_xlim(2.5, 15.5)
ax.set_ylim(86, 91)
ax.yaxis.set_major_locator(mticker.MultipleLocator(1))
ax.tick_params(axis='y', labelsize=9)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.3, linewidth=0.5)

ax.legend(loc='lower right', fontsize=8.5, framealpha=0.9, edgecolor='#cccccc')

fig.tight_layout(pad=0.4)

out_dir = Path('/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/figures/paper')
fig.savefig(out_dir / 'figure2_v2.pdf', bbox_inches='tight', dpi=300)
fig.savefig(out_dir / 'figure2_v2.png', bbox_inches='tight', dpi=300)
plt.close()
print('Done.')
