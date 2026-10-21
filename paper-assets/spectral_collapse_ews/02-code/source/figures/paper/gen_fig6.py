import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os, sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/artifacts')
from visual_design_language_v2 import (
    apply_style, COLORS, FIGSIZE, style_axes, LEGEND
)
apply_style()

generations = np.arange(11)

r0_s42 = np.array([2366.68, 2464.76, 2469.93, 2440.57, 2405.05, 2370.17, 2335.17, 2304.19, 2252.12, 2207.57, 2178.95])
r0_s43 = np.array([2366.68, 2462.62, 2466.63, 2438.38, 2404.60, 2365.13, 2325.01, 2291.55, 2248.26, 2234.80, 2210.77])
r0_s44 = np.array([2366.68, 2459.40, 2467.38, 2442.40, 2408.35, 2362.67, 2318.17, 2283.98, 2237.81, 2188.92, 2154.34])

r0_all = np.array([r0_s42, r0_s43, r0_s44])
r0_mean = r0_all.mean(axis=0)
r0_std = r0_all.std(axis=0, ddof=1)
cv_gen10 = r0_std[10] / r0_mean[10] * 100

fig, ax = plt.subplots(figsize=FIGSIZE['single'])

for i, (data, mk) in enumerate([(r0_s42, 'o'), (r0_s43, 's'), (r0_s44, '^')]):
    ax.plot(generations, data, marker=mk, markersize=3.0, linewidth=0.8,
            color=COLORS['r0'], alpha=0.30,
            label='Individual seeds' if i == 0 else '_nolegend_')

ax.fill_between(generations, r0_mean - r0_std, r0_mean + r0_std,
                color=COLORS['r0'], alpha=0.10, label=r'$\pm$1 s.d.')

ax.plot(generations, r0_mean, marker='o', markersize=3.5, linewidth=1.2,
        color=COLORS['r0'], markeredgecolor='white', markeredgewidth=0.4,
        label='3-seed mean', zorder=5)

ax.annotate(
    f'CV = {cv_gen10:.1f}%',
    xy=(10, r0_mean[10] + r0_std[10]), xytext=(8.0, 2280),
    fontsize=6.5, fontstyle='italic', color=COLORS['r0'],
    arrowprops=dict(arrowstyle='->', color=COLORS['r0'], lw=0.5),
    ha='center', va='bottom',
)

ax.set_xlabel('Generation')
ax.set_ylabel('SLV')
ax.set_xlim(-0.3, 10.3)
ax.set_ylim(2140, 2490)
ax.set_xticks(generations)
ax.legend(**LEGEND, loc='upper right')
style_axes(ax)
plt.tight_layout()

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/figures/paper'
PAPDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/figures'
os.makedirs(PAPDIR, exist_ok=True)
for d, n in [(OUTDIR, 'fig6_seed_variability'), (PAPDIR, 'seed_variability')]:
    fig.savefig(f'{d}/{n}.pdf')
    fig.savefig(f'{d}/{n}.png')
plt.close()
print("Fig 6 done.")
