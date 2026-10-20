#!/usr/bin/env python3
"""Generate fig_selection_gap: 2-panel vertical (rho bars + delta-F1 dots).

Style matched to Figs 3-5 (project palette, white background, pill labels).
Semantic colors: consensus signals = treatment blue, LP = baseline blue.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path
from matplotlib.patches import FancyBboxPatch, Patch

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'dejavusans',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

FIG_DIR = Path(__file__).parent

# ── Data ──
signal_labels = ['SJ', 'FK', 'EM', 'VC', 'LP']
rho_vals = np.array([0.359, 0.266, 0.294, 0.379, 0.205])
delta_f1 = np.array([-0.45, -0.46, -1.19, -2.65, +0.04])
oracle_delta = 13.0
random_delta = -3.9

# ── Semantic colors (project palette) ──
COL_CONSENSUS = '#B3D4FC'       # treatment - instance-level signals
COL_CONSENSUS_EDGE = '#3B7DD8'
COL_LP = '#1A5BB5'              # baseline - per-sample signal
COL_LP_EDGE = '#0D47A1'
COL_ORACLE = '#43A047'          # safe green
COL_RANDOM = '#999999'          # neutral

bar_colors = [COL_CONSENSUS] * 4 + [COL_LP]
bar_edges = [COL_CONSENSUS_EDGE] * 4 + [COL_LP_EDGE]
dot_colors = [COL_CONSENSUS_EDGE] * 4 + [COL_LP]

x = np.arange(len(signal_labels))

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(3.4, 3.6),
    gridspec_kw={'height_ratios': [1, 1.4], 'hspace': 0.10},
    sharex=True,
)
fig.patch.set_facecolor('white')
fig.suptitle('SciERC NER, $N{=}8$, $T{=}1.0$', fontsize=10, y=1.02)


def style_ax(ax):
    ax.set_facecolor('white')
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('#CCCCCC')
        ax.spines[spine].set_linewidth(0.8)
    ax.tick_params(colors='#555555', which='both')
    ax.set_axisbelow(True)


# ═══ Top panel: Spearman ρ bars ═══
style_ax(ax1)

bar_width = 0.50
for xi, rv, fc, ec in zip(x, rho_vals, bar_colors, bar_edges):
    bar = FancyBboxPatch(
        (xi - bar_width / 2, 0), bar_width, rv,
        boxstyle='round,pad=0,rounding_size=0.015',
        facecolor=fc, edgecolor=ec, linewidth=0.6,
        alpha=0.88, zorder=2,
    )
    ax1.add_patch(bar)
    ax1.text(xi, rv + 0.013, f'{rv:.3f}', ha='center', va='bottom',
             fontsize=7, color=ec, fontweight='medium')

ax1.set_ylabel(r'Spearman $\rho$', labelpad=4)
ax1.set_ylim(0, 0.48)
ax1.set_xlim(-0.55, 4.55)
ax1.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
ax1.grid(axis='y', alpha=0.15, linewidth=0.5, color='#888888', zorder=0)
ax1.tick_params(axis='x', length=0)
legend_elements = [
    Patch(facecolor=COL_CONSENSUS, edgecolor=COL_CONSENSUS_EDGE,
          alpha=0.88, label='Consensus'),
    Patch(facecolor=COL_LP, edgecolor=COL_LP_EDGE,
          alpha=0.88, label='Per-sample (LP)'),
]
ax1.legend(handles=legend_elements, loc='lower center',
           bbox_to_anchor=(0.5, 1.0), ncol=2,
           fontsize=5.5, handlelength=1.0, handleheight=0.6,
           frameon=True, fancybox=True, edgecolor='#CCCCCC',
           facecolor='white', framealpha=0.95,
           borderpad=0.3, columnspacing=0.8, handletextpad=0.3)

# ═══ Bottom panel: ΔF1 dots + line ═══
style_ax(ax2)

ax2.plot(x, delta_f1, '-', color='#CCCCCC', linewidth=1.5, zorder=2)

for xi, d, col in zip(x, delta_f1, dot_colors):
    ax2.plot(xi, d, 'o', color=col, markersize=8,
             markeredgecolor='white', markeredgewidth=0.8, zorder=4)

label_offsets = {0: (0, -9), 1: (0, -9), 2: (0, -9), 3: (0, -9), 4: (-14, 7)}
for xi, d, col in zip(x, delta_f1, dot_colors):
    ox, oy = label_offsets[xi]
    va = 'bottom' if oy > 0 else 'top'
    ax2.annotate(f'{d:+.2f}', xy=(xi, d), xytext=(ox, oy),
                 textcoords='offset points', ha='center', va=va,
                 fontsize=6.5, color=col, fontweight='medium')

pill_box = dict(boxstyle='round,pad=0.15', facecolor='white',
                edgecolor='#CCCCCC', linewidth=0.4, alpha=0.9)

ax2.axhline(y=0, color='#888888', linestyle='-', linewidth=0.6, zorder=1)
ax2.text(-0.42, 0.20, 'Greedy', fontsize=6, color='#888888',
         ha='left', va='bottom', fontstyle='italic', bbox=pill_box, zorder=10)

ax2.axhline(y=random_delta, color=COL_RANDOM, linestyle=':', linewidth=0.7,
            alpha=0.4, zorder=1)
ax2.text(-0.42, random_delta + 0.20, 'Random', fontsize=6, color='#999999',
         ha='left', va='bottom', fontstyle='italic', bbox=pill_box, zorder=10)

ax2.annotate(
    f'↑ Oracle: +{oracle_delta:.1f} pp', xy=(2.0, 1.45),
    fontsize=6.5, color=COL_ORACLE, ha='center', va='bottom',
    bbox=dict(boxstyle='round,pad=0.25', facecolor='#eef7ee',
              edgecolor=COL_ORACLE, linewidth=0.5, alpha=0.9),
)

ax2.set_ylabel(r'$\Delta$F1 vs Greedy (pp)', labelpad=4)
ax2.set_ylim(-4.6, 2.0)
ax2.set_xticks(x)
ax2.set_xticklabels(signal_labels)
ax2.grid(axis='y', alpha=0.15, linewidth=0.5, color='#888888', zorder=0)

fig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png')
plt.close(fig)
print('Done: fig_selection_gap')
