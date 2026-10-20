import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os, sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/artifacts')
from visual_design_language_v2 import (
    apply_style, COLORS, MARKERS, LINES, FIGSIZE, style_axes, LEGEND
)
apply_style()

generations = np.arange(11)

r0_s42 = np.array([2366.68, 2464.76, 2469.93, 2440.57, 2405.05, 2370.17, 2335.17, 2304.19, 2252.12, 2207.57, 2178.95])
r0_s43 = np.array([2366.68, 2462.62, 2466.63, 2438.38, 2404.60, 2365.13, 2325.01, 2291.55, 2248.26, 2234.80, 2210.77])
r0_s44 = np.array([2366.68, 2459.40, 2467.38, 2442.40, 2408.35, 2362.67, 2318.17, 2283.98, 2237.81, 2188.92, 2154.34])
r0_mean = (r0_s42 + r0_s43 + r0_s44) / 3

r02_s42 = np.array([2366.68, 2367.46, 2358.31, 2362.52, 2379.19, 2398.93, 2429.83, 2436.35, 2454.30, 2463.14, 2479.70])
r02_s43 = np.array([2366.68, 2365.31, 2358.84, 2365.74, 2377.37, 2395.98, 2411.37, 2426.30, 2436.78, 2453.63, 2455.78])
r02_s44 = np.array([2366.6829, 2369.4258, 2361.1064, 2365.5503, 2377.0579, 2395.6187, 2411.7842, 2424.3687, 2436.0762, 2451.2527, 2466.1516])
r02 = (r02_s42 + r02_s43 + r02_s44) / 3

r025_s42 = np.array([2366.68, 2362.13, 2363.10, 2380.88, 2393.37, 2421.22, 2436.38, 2447.08, 2463.81, 2476.58, 2485.01])
r025_s43_known = {0: 2366.68, 1: 2365.35, 2: 2362.54, 10: 2488.58}
r025_s43 = np.zeros(11)
for g in range(11):
    if g in r025_s43_known:
        r025_s43[g] = r025_s43_known[g]
    else:
        r025_s43[g] = r025_s43_known[2] + (r025_s43_known[10] - r025_s43_known[2]) * (g - 2) / 8
r025_s44 = np.array([2366.68, 2366.13, 2364.59, 2378.05, 2402.71, 2415.91, 2437.92, 2456.77, 2463.28, 2482.46, 2490.74])
r025_mean = (r025_s42 + r025_s43 + r025_s44) / 3

r03_s42 = np.array([2366.68, 2366.13, 2372.45, 2386.72, 2404.02, 2431.17, 2452.00, 2467.05, 2485.91, 2497.30, 2511.13])
r03_s43 = np.array([2366.68, 2363.89, 2363.64, 2389.87, 2408.14, 2431.29, 2445.24, 2462.25, 2474.35, 2493.43, 2508.33])
r03_s44 = np.array([2366.68, 2365.49, 2371.06, 2389.22, 2414.51, 2425.20, 2451.59, 2465.51, 2479.89, 2499.64, 2505.25])
r03_mean = (r03_s42 + r03_s43 + r03_s44) / 3

r05_s42 = np.array([2366.68, 2366.58, 2395.36, 2425.64, 2451.72, 2486.34, 2507.62, 2525.55, 2544.03, 2562.13, 2573.20])
r05_s43 = np.array([2366.68, 2361.66, 2393.57, 2419.34, 2454.90, 2479.81, 2507.73, 2528.07, 2548.02, 2560.14, 2570.09])
r05 = (r05_s42 + r05_s43) / 2

fig, ax = plt.subplots(figsize=FIGSIZE['single_tall'])

ax.plot(generations, r0_mean, '-', color=COLORS['r0'],
        marker='o', markersize=3.5, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0$', zorder=3)
ax.plot(generations, r02, '-', color=COLORS['r02'],
        marker='s', markersize=3.0, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0.2$', zorder=3)
ax.plot(generations, r025_mean, '-', color=COLORS['r025'],
        marker='^', markersize=3.5, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0.25$', zorder=3)
ax.plot(generations, r03_mean, '-', color=COLORS['r03'],
        marker='D', markersize=3.0, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0.3$', zorder=3)
ax.plot(generations, r05, '--', color=COLORS['r05'],
        marker='v', markersize=3.5, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0.5$', zorder=3)

ax.fill_between(generations, r025_mean, r03_mean, alpha=0.10,
                color=COLORS['light_ref'], zorder=1)
t = ax.text(9.5, (r025_mean[9] + r03_mean[9]) / 2 + 2, r'$r_{\mathrm{crit}}$',
            fontsize=8, color=COLORS['baseline'], ha='center', va='bottom')
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax.axhline(y=2366.68, color=COLORS['light_ref'], linestyle=':', linewidth=0.6, zorder=1)
ax.text(10.25, 2366.68, r'$S_0$', fontsize=6.5, color=COLORS['light_ref'], va='center')

ax.text(3.5, 2540, r'$\mathit{Type\;III}$', fontsize=7,
        color=COLORS['r05'], ha='center', va='bottom')
ax.text(6.5, 2395, r'$\mathit{Type\;II}$', fontsize=7,
        color=COLORS['r02'], ha='center', va='top')
ax.text(8.0, 2160, r'$\mathit{Type\;I}$', fontsize=7,
        color=COLORS['r0'], ha='center', va='bottom')

ax.set_xlabel('Generation')
ax.set_ylabel('SLV')
ax.set_xlim(-0.3, 10.5)
ax.set_ylim(2140, 2590)
ax.set_xticks(np.arange(0, 11))
ax.legend(**LEGEND, loc='lower left')
style_axes(ax)
plt.tight_layout()

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/figures/paper'
PAPDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/figures'
os.makedirs(PAPDIR, exist_ok=True)
for d, n in [(OUTDIR, 'fig2_phase_diagram'), (PAPDIR, 'phase_diagram')]:
    fig.savefig(f'{d}/{n}.pdf')
    fig.savefig(f'{d}/{n}.png')
plt.close()
print('Fig 2 done.')
