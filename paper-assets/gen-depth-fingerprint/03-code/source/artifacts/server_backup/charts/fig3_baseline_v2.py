"""Figure 3: Baseline comparison -- LOGO binary F1 with inference cost.
Column-width dot plot with cost annotations."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'mathtext.fontset': 'cm',
})

methods = [
    '4-det. + surface',
    '7-feature (ours)',
    '4-detector ens.',
    'LD-Score',
    'Avg-LogProb',
    'FastDetectGPT',
    'Binoculars',
]
bin_f1 = [0.708, 0.705, 0.700, 0.675, 0.673, 0.569, 0.539]
n_feat = [6, 7, 4, 1, 1, 1, 1]
ms_text = [22.8, 9.7, 22.8, None, None, None, None]
mem_mb  = [2868, 905, 2868, None, None, None, None]

COLOR_MAP = {
    '7-feature (ours)':  '#0072B2',
    '4-det. + surface':  '#009E73',
    '4-detector ens.':   '#009E73',
    'LD-Score':          '#E69F00',
    'Avg-LogProb':       '#CC79A7',
    'FastDetectGPT':     '#D55E00',
    'Binoculars':        '#555555',
}

is_ours     = [False, True, False, False, False, False, False]
colors = [COLOR_MAP[m] for m in methods]

n = len(methods)
y_pos = np.arange(n)[::-1]

fig, ax = plt.subplots(figsize=(3.25, 2.4))

for i in range(n):
    yi = y_pos[i]
    ms = 7.5 if is_ours[i] else 5.5
    mfc = colors[i]
    mec = colors[i]
    mew = 1.3 if is_ours[i] else 1.0
    zorder = 5 if is_ours[i] else 3

    ax.plot(bin_f1[i], yi, 'o', markersize=ms,
            markerfacecolor=mfc, markeredgecolor=mec,
            markeredgewidth=mew, zorder=zorder)

    label_x = bin_f1[i] + 0.008
    fw = 'bold' if is_ours[i] else 'normal'
    ax.text(label_x, yi, f'{bin_f1[i]:.3f}', va='center', ha='left',
            fontsize=6, color=colors[i], fontweight=fw)

for i in range(n):
    yi = y_pos[i]
    if ms_text[i] is not None:
        cost_str = f'{ms_text[i]:.0f}ms / {mem_mb[i]:,}MB' if ms_text[i] == 22.8 else f'{ms_text[i]:.1f}ms / {mem_mb[i]:,}MB'
        x_pos = 0.50
        ax.text(x_pos, yi - 0.22, cost_str, fontsize=4.5, color='#777',
                va='top', ha='left')

ax.axvline(x=0.5, color='#ddd', linewidth=0.5, linestyle='--', zorder=0)

ax.set_yticks(y_pos)
ax.set_yticklabels(methods, fontsize=6.5)
ax.set_xlabel('LOGO Binary F1 (gen-1 vs. gen-2+)', fontsize=7.5)
ax.set_xlim(0.48, 0.76)
ax.set_ylim(-0.6, n - 0.4)
ax.tick_params(axis='y', length=0)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#999')
ax.spines['bottom'].set_linewidth(0.5)

ax.grid(axis='x', color='#eee', linewidth=0.4, zorder=0)

for i in range(n):
    if is_ours[i]:
        yi = y_pos[i]
        ax.axhspan(yi - 0.42, yi + 0.42, color='#0072B2', alpha=0.05, zorder=0)

plt.tight_layout()

import os
out = os.path.dirname(os.path.abspath(__file__)) if os.path.isfile(__file__) else os.getcwd()
fig.savefig(f'{out}/fig3_baseline_comparison.pdf', format='pdf')
fig.savefig(f'{out}/fig3_baseline_comparison.png', format='png')
print(f'Saved fig3 to {out}/')
