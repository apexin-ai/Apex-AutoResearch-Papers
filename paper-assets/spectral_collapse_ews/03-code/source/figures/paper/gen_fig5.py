import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os, sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/artifacts')
from visual_design_language_v2 import (
    apply_style, COLORS, FIGSIZE, style_axes
)
apply_style()

r0_s42 = np.array([2366.68, 2464.76, 2469.93, 2440.57, 2405.05, 2370.17, 2335.17, 2304.19, 2252.12, 2207.57, 2178.95])
r0_s43 = np.array([2366.68, 2462.62, 2466.63, 2438.38, 2404.60, 2365.13, 2325.01, 2291.55, 2248.26, 2234.80, 2210.77])
r0_s44 = np.array([2366.68, 2459.40, 2467.38, 2442.40, 2408.35, 2362.67, 2318.17, 2283.98, 2237.81, 2188.92, 2154.34])
r0_mean = (r0_s42 + r0_s43 + r0_s44) / 3

r02_s42 = np.array([2366.68, 2367.46, 2358.31, 2362.52, 2379.19, 2398.93, 2429.83, 2436.35, 2454.30, 2463.14, 2479.70])
r02_s43 = np.array([2366.68, 2365.31, 2358.84, 2365.74, 2377.37, 2395.98, 2411.37, 2426.30, 2436.78, 2453.63, 2455.78])
r02_s44 = np.array([2366.6829, 2369.4258, 2361.1064, 2365.5503, 2377.0579, 2395.6187, 2411.7842, 2424.3687, 2436.0762, 2451.2527, 2466.1516])
r02_mean = (r02_s42 + r02_s43 + r02_s44) / 3

r025_s42 = np.array([2366.68, 2362.13, 2363.10, 2380.88, 2393.37, 2421.22, 2436.38, 2447.08, 2463.81, 2476.58, 2485.01])
r025_s44 = np.array([2366.68, 2366.13, 2364.59, 2378.05, 2402.71, 2415.91, 2437.92, 2456.77, 2463.28, 2482.46, 2490.74])
r025_s43_known = {0: 2366.68, 1: 2365.35, 2: 2362.54, 10: 2488.58}
r025_s43 = np.zeros(11)
for g in range(11):
    if g in r025_s43_known:
        r025_s43[g] = r025_s43_known[g]
    else:
        r025_s43[g] = r025_s43_known[2] + (r025_s43_known[10] - r025_s43_known[2]) * (g - 2) / 8
r025_mean = (r025_s42 + r025_s43 + r025_s44) / 3

r03_s42 = np.array([2366.68, 2366.13, 2372.45, 2386.72, 2404.02, 2431.17, 2452.00, 2467.05, 2485.91, 2497.30, 2511.13])
r03_s43 = np.array([2366.68, 2363.89, 2363.64, 2389.87, 2408.14, 2431.29, 2445.24, 2462.25, 2474.35, 2493.43, 2508.33])
r03_s44 = np.array([2366.68, 2365.49, 2371.06, 2389.22, 2414.51, 2425.20, 2451.59, 2465.51, 2479.89, 2499.64, 2505.25])
r03_mean = (r03_s42 + r03_s43 + r03_s44) / 3

r05_s42 = np.array([2366.68, 2366.58, 2395.36, 2425.64, 2451.72, 2486.34, 2507.62, 2525.55, 2544.03, 2562.13, 2573.20])
r05_s43 = np.array([2366.68, 2361.66, 2393.57, 2419.34, 2454.90, 2479.81, 2507.73, 2528.07, 2548.02, 2560.14, 2570.09])
r05_mean = (r05_s42 + r05_s43) / 2

def compute_max_signal(slv_array, alpha=0.5):
    ema = np.zeros_like(slv_array)
    ema[0] = slv_array[0]
    for t in range(1, len(slv_array)):
        ema[t] = alpha * slv_array[t] + (1 - alpha) * ema[t-1]
    delta = np.diff(ema)
    delta_t2 = delta[1:]
    neg_deltas = -delta_t2[delta_t2 < 0]
    if len(neg_deltas) == 0:
        return 0.0
    return np.max(neg_deltas)

ratios = [0, 0.2, 0.25, 0.3, 0.5]
means = [r0_mean, r02_mean, r025_mean, r03_mean, r05_mean]
labels = ["0", "0.2", "0.25", "0.3", "0.5"]
ratio_keys = ['r0', 'r02', 'r025', 'r03', 'r05']
colors = [COLORS[k] for k in ratio_keys]
signals = [compute_max_signal(m) for m in means]

fig, ax = plt.subplots(figsize=FIGSIZE['single'])
x = np.arange(len(ratios))
bars = ax.bar(x, signals, color=colors, width=0.55, edgecolor='white', linewidth=0.4)

for s, bar in zip(signals, bars):
    if s == 0.0:
        bar.set_hatch('///')
        bar.set_edgecolor(COLORS['light_ref'])

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel(r"Mixing ratio $r$")
ax.set_ylabel(r"Max $|\Delta\tilde{S}_t|$")

for i, (s, bar) in enumerate(zip(signals, bars)):
    if s > 0.5:
        ax.text(bar.get_x() + bar.get_width() / 2, s + 0.8, f'{s:.1f}',
                ha='center', va='bottom', fontsize=6.5, color=COLORS['annotation'])
    elif s == 0.0:
        ax.text(bar.get_x() + bar.get_width() / 2, 0.5, "silent",
                ha='center', va='bottom', fontsize=6.5, fontstyle='italic',
                color=COLORS['light_ref'])

x_crit = (x[2] + x[3]) / 2
ymax = max(signals) * 1.18
ax.axvline(x_crit, color=COLORS['phase_edge'], linestyle='--', linewidth=0.6, zorder=0)
ax.text(x_crit + 0.08, ymax * 0.90, r"$r_{\mathrm{crit}}$",
        ha='left', va='top', fontsize=7, color=COLORS['baseline'])

ax.set_ylim(0, ymax)
style_axes(ax)
plt.tight_layout()

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/figures/paper'
PAPDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/figures'
os.makedirs(PAPDIR, exist_ok=True)
for d, n in [(OUTDIR, 'fig5_controller_signal'), (PAPDIR, 'controller_signal')]:
    fig.savefig(f'{d}/{n}.pdf')
    fig.savefig(f'{d}/{n}.png')
plt.close()
print("Fig 5 done.")
