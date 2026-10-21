import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os, sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/artifacts')
from visual_design_language_v2 import (
    apply_style, COLORS, LINES, PHASES, FIGSIZE,
    style_axes, add_inline_label
)
apply_style()

generations = np.arange(11)

r0_s42_slv = np.array([2366.68, 2464.76, 2469.93, 2440.57, 2405.05, 2370.17, 2335.17, 2304.19, 2252.12, 2207.57, 2178.95])
r0_s43_slv = np.array([2366.68, 2462.62, 2466.63, 2438.38, 2404.60, 2365.13, 2325.01, 2291.55, 2248.26, 2234.80, 2210.77])
r0_s44_slv = np.array([2366.68, 2459.40, 2467.38, 2442.40, 2408.35, 2362.67, 2318.17, 2283.98, 2237.81, 2188.92, 2154.34])
slv_mean = (r0_s42_slv + r0_s43_slv + r0_s44_slv) / 3

r0_s42_ppl = np.array([9.5536, 11.3832, 13.5810, 16.2464, 19.8041, 24.5927, 30.9139, 38.8888, 49.2899, 63.3248, 76.7808])
r0_s43_ppl = np.array([9.554, 11.371, 13.565, 16.219, 19.94, 24.603, 30.064, 37.442, 46.943, 58.003, 70.5])
r0_s44_ppl = np.array([9.55, 11.36, 13.54, 16.22, 19.97, 24.3, 30.21, 37.14, 44.48, 54.34, 65.7])
ppl_mean = (r0_s42_ppl + r0_s43_ppl + r0_s44_ppl) / 3

PH_LABELS = [('I', 'Decompression'), ('II', 'Onset'), ('III', 'Collapse')]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.4, 3.2),
                                gridspec_kw={'height_ratios': [1.2, 1]},
                                sharex=True)

for ax in [ax1, ax2]:
    for key in ['I', 'II', 'III']:
        p = PHASES[key]
        ax.axvspan(p['gen_range'][0], p['gen_range'][1],
                   facecolor=p['fill_color'], alpha=p['fill_alpha'],
                   edgecolor='none', zorder=0)
    for xb in [2, 4]:
        ax.axvline(xb, **LINES['phase_boundary'])

ax1.plot(generations, slv_mean, '-', color=COLORS['r05'],
         marker='o', markersize=3.5, markeredgecolor='white', markeredgewidth=0.4,
         linewidth=1.2, zorder=3)
ax1.set_ylabel('SLV')
ax1.set_ylim(slv_mean.min() - 30, slv_mean.max() + 50)

add_inline_label(ax1, 1, slv_mean[1] + 5, 'SLV', COLORS['r05'], offset=(5, 3))

for (lbl, sub), xc in zip(PH_LABELS, [1, 3, 7]):
    ax1.text(xc, 1.02, f'{lbl}', fontsize=6, fontstyle='italic',
             color=PHASES[lbl]['text_color'],
             ha='center', va='bottom', transform=ax1.get_xaxis_transform())

ax2.plot(generations, ppl_mean, '-', color=COLORS['r0'],
         marker='s', markersize=3.0, markeredgecolor='white', markeredgewidth=0.4,
         linewidth=1.2, zorder=3)
ax2.set_ylabel('Perplexity')
ax2.set_xlabel('Generation')
ax2.set_xlim(-0.3, 10.3)
ax2.set_xticks(np.arange(0, 11))

add_inline_label(ax2, 8, ppl_mean[8], 'PPL', COLORS['r0'], offset=(5, -8))

for ax in [ax1, ax2]:
    style_axes(ax)

plt.tight_layout()
plt.subplots_adjust(hspace=0.10)

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/figures/paper'
PAPDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/figures'
os.makedirs(PAPDIR, exist_ok=True)
for d, n in [(OUTDIR, 'fig3_slv_ppl_decoupling'), (PAPDIR, 'slv_ppl_decoupling')]:
    fig.savefig(f'{d}/{n}.pdf')
    fig.savefig(f'{d}/{n}.png')
plt.close()
print('Fig 3 done.')
