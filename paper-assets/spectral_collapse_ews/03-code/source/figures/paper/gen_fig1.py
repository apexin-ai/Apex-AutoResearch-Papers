import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os, sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/artifacts')
from visual_design_language_v2 import (
    apply_style, COLORS, MARKERS, LINES, PHASES, FIGSIZE,
    style_axes, add_inline_label
)
apply_style()

generations = np.arange(11)

r0_s42 = np.array([2366.68, 2464.76, 2469.93, 2440.57, 2405.05, 2370.17, 2335.17, 2304.19, 2252.12, 2207.57, 2178.95])
r0_s43 = np.array([2366.68, 2462.62, 2466.63, 2438.38, 2404.60, 2365.13, 2325.01, 2291.55, 2248.26, 2234.80, 2210.77])
r0_s44 = np.array([2366.68, 2459.40, 2467.38, 2442.40, 2408.35, 2362.67, 2318.17, 2283.98, 2237.81, 2188.92, 2154.34])
r0_mean = (r0_s42 + r0_s43 + r0_s44) / 3

r05_s42 = np.array([2366.68, 2366.58, 2395.36, 2425.64, 2451.72, 2486.34, 2507.62, 2525.55, 2544.03, 2562.13, 2573.20])
r05_s43 = np.array([2366.68, 2361.66, 2393.57, 2419.34, 2454.90, 2479.81, 2507.73, 2528.07, 2548.02, 2560.14, 2570.09])
r05_mean = (r05_s42 + r05_s43) / 2

fig, ax = plt.subplots(figsize=FIGSIZE['single'])

for key in ['I', 'II', 'III']:
    p = PHASES[key]
    ax.axvspan(p['gen_range'][0], p['gen_range'][1],
               facecolor=p['fill_color'], alpha=p['fill_alpha'],
               edgecolor='none', zorder=0)
for xb in [2, 4]:
    ax.axvline(xb, **LINES['phase_boundary'])

ax.fill_between(generations, r0_mean, r05_mean, alpha=0.07,
                color=COLORS['light_ref'], zorder=1)

ax.plot(generations, r0_mean, '-', color=COLORS['r0'],
        marker='o', markersize=3.5, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, solid_capstyle='round', zorder=3)
ax.plot(generations, r05_mean, '--', color=COLORS['r05'],
        marker='v', markersize=3.5, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, solid_capstyle='round', zorder=3)

ax.axhline(y=2366.68, color=COLORS['light_ref'], linestyle=':', linewidth=0.6, zorder=1)
ax.text(10.45, 2366.68, r'$S_0$', fontsize=6.5, color=COLORS['light_ref'], va='center')

peak_val = r0_mean[2]
ax.annotate(f'peak ({peak_val:.0f})', xy=(2, peak_val),
            xytext=(3.8, peak_val + 55), fontsize=6.5, color=COLORS['r0'],
            fontstyle='italic',
            arrowprops=dict(arrowstyle='->', color=COLORS['r0'], lw=0.5,
                            connectionstyle='arc3,rad=-0.15'),
            zorder=5)

add_inline_label(ax, 8, r0_mean[8], r'$r\!=\!0$', COLORS['r0'], offset=(5, -8))
add_inline_label(ax, 8, r05_mean[8], r'$r\!=\!0.5$', COLORS['r05'], offset=(5, 3))

for xc, lbl in [(1, 'I'), (3, 'II'), (7, 'III')]:
    ax.text(xc, 1.02, lbl, fontsize=6, fontstyle='italic',
            color=PHASES[lbl]['text_color'],
            ha='center', va='bottom', transform=ax.get_xaxis_transform())

ax.set_xlabel('Generation')
ax.set_ylabel('SLV')
ax.set_xlim(-0.3, 10.6)
ax.set_ylim(2140, 2590)
ax.set_xticks(np.arange(0, 11))
style_axes(ax)
plt.tight_layout()

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/figures/paper'
PAPDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/figures'
os.makedirs(PAPDIR, exist_ok=True)
for d, n in [(OUTDIR, 'fig1_spectral_trajectory'), (PAPDIR, 'spectral_trajectory')]:
    fig.savefig(f'{d}/{n}.pdf')
    fig.savefig(f'{d}/{n}.png')
plt.close()
print('Fig 1 done.')
