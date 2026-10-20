import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.colors as mcolors
import numpy as np
import os, sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/artifacts')
from visual_design_language_v2 import (
    apply_style, COLORS, PHASES
)
apply_style()

fig, ax = plt.subplots(figsize=(7.0, 2.0))
ax.set_xlim(0, 7)
ax.set_ylim(0, 2)
ax.axis('off')

BOX_H = 0.42
Y_MAIN = 1.10
Y_CTRL = 0.38

def draw_box(x, y, w, h, text, color, fontsize=7):
    fill = mcolors.to_rgba(color, alpha=0.15)
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle='round,pad=0.06',
                          facecolor=fill, edgecolor=color,
                          linewidth=0.6, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=fontsize, ha='center', va='center',
            color='#222222', zorder=4)

def draw_arrow(x1, y1, x2, y2):
    arr = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=8,
                           color='#444444', linewidth=0.5, zorder=2)
    ax.add_patch(arr)

draw_box(0.70, Y_MAIN, 1.00, BOX_H, r'Gen $t$ Model', COLORS['r05'])
draw_box(2.05, Y_MAIN, 0.80, BOX_H, 'Fine-tune', COLORS['r025'])
draw_box(3.35, Y_MAIN, 1.00, BOX_H, r'Gen $t\!+\!1$ Model', COLORS['r05'])
draw_box(4.70, Y_MAIN, 0.90, BOX_H, 'Spectral\nMonitor', COLORS['r03'], fontsize=6.5)
draw_box(5.65, Y_MAIN, 0.50, BOX_H, 'SVD', COLORS['r03'])

ax.text(5.95, Y_MAIN, r'$\rightarrow$ {SLV, $r_{\mathrm{eff}}$, $\sigma_1$}',
        fontsize=6, color=COLORS['annotation'], ha='left', va='center')

for x1, x2 in [(1.20, 1.65), (2.45, 2.85), (3.85, 4.25), (5.15, 5.40)]:
    draw_arrow(x1, Y_MAIN, x2, Y_MAIN)

ax.text(2.05, Y_MAIN - 0.35, r'synth + real ($r_t$)', fontsize=5.5,
        ha='center', va='top', color=COLORS['baseline'], fontstyle='italic')

draw_box(3.35, Y_CTRL, 1.00, 0.35, 'Controller', COLORS['r0'], fontsize=6.5)

ax.annotate('', xy=(3.85, Y_CTRL), xytext=(5.65, Y_MAIN - BOX_H/2),
            arrowprops=dict(arrowstyle='->', color=COLORS['annotation'],
                            lw=0.5, linestyle='--',
                            connectionstyle='arc3,rad=-0.3'),
            zorder=2)

ax.annotate('', xy=(2.05, Y_MAIN - BOX_H/2), xytext=(2.85, Y_CTRL),
            arrowprops=dict(arrowstyle='->', color=COLORS['r0'],
                            lw=0.5, linestyle='--',
                            connectionstyle='arc3,rad=-0.3'),
            zorder=2)

ax.text(5.0, 0.62, 'SLV rate', fontsize=5.5, color=COLORS['annotation'],
        ha='center', va='center', fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.08', facecolor='white', edgecolor='none'))
ax.text(2.3, 0.62, r'adjust $r_{t+1}$', fontsize=5.5, color=COLORS['r0'],
        ha='center', va='center', fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.08', facecolor='white', edgecolor='none'))

phase_spans = [
    (0, 2.3, 'I', 'Decompression'),
    (2.3, 4.5, 'II', 'Onset'),
    (4.5, 7.0, 'III', 'Acceleration'),
]
for x0, x1, key, sublabel in phase_spans:
    ax.axvspan(x0, x1, ymin=0.87, ymax=0.97,
               facecolor=PHASES[key]['fill_color'], alpha=0.50,
               edgecolor='none', zorder=1)
    xc = (x0 + x1) / 2
    ax.text(xc, 1.88, f'{key}  {sublabel}', fontsize=5.5, fontstyle='italic',
            color=PHASES[key]['text_color'], ha='center', va='center')

for xb in [2.3, 4.5]:
    ax.axvline(xb, ymin=0.87, ymax=0.97, color=COLORS['phase_edge'],
               linestyle=':', linewidth=0.4, alpha=0.45, zorder=1)

plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/figures/paper'
PAPDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/figures'
os.makedirs(OUTDIR, exist_ok=True)
os.makedirs(PAPDIR, exist_ok=True)
for d in [OUTDIR, PAPDIR]:
    fig.savefig(f'{d}/pipeline_overview.pdf')
    fig.savefig(f'{d}/pipeline_overview.png')
plt.close()
print("Pipeline overview done.")
