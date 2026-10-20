#!/usr/bin/env python3
"""Figure 2: Metric trajectories showing entropy-leads-diversity pattern."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import json
from pathlib import Path

OUT = Path(__file__).parent
DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_space/trajectory_data.json')

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
    'lines.linewidth': 1.6,
})

with open(DATA) as f:
    raw = json.load(f)

PALETTE = {
    0.00: '#B8D4E8',
    0.25: '#4A90C4',
    0.50: '#E8A04C',
    0.75: '#CC5A5A',
}
MARKERS = {0.00: 'o', 0.25: 's', 0.50: 'D', 0.75: '^'}

alphas_to_plot = [0.00, 0.25, 0.50, 0.75]
gens = np.arange(11)

fig, (ax_ent, ax_div) = plt.subplots(
    1, 2, figsize=(7.0, 2.4),
    gridspec_kw={'wspace': 0.32}
)

for alpha in alphas_to_plot:
    key = str(alpha)
    if key not in raw:
        key = f'{alpha:.1f}'
    v = raw[key]
    color = PALETTE[alpha]
    marker = MARKERS[alpha]
    label = f'$\\alpha={alpha:.2f}$'

    ax_ent.plot(gens, v['e'], '-', color=color, marker=marker, markersize=3.5,
                markeredgewidth=0, label=label, zorder=3)
    ax_div.plot(gens, v['d'], '-', color=color, marker=marker, markersize=3.5,
                markeredgewidth=0, label=label, zorder=3)

# Panel (a): Token Entropy
ax_ent.set_ylabel('Token entropy')
ax_ent.set_xlabel('Generation')
ax_ent.set_xticks(gens)
ax_ent.set_ylim(1.95, 3.35)
ax_ent.yaxis.grid(True, alpha=0.12, linewidth=0.4, zorder=0)
ax_ent.set_axisbelow(True)
ax_ent.legend(loc='upper right', framealpha=0.92, edgecolor='none',
              handlelength=1.5, borderpad=0.2, ncol=1, columnspacing=0.8,
              bbox_to_anchor=(0.99, 0.98))
ax_ent.text(-0.15, 1.02, '(a)', transform=ax_ent.transAxes,
            fontsize=11, fontweight='bold', va='bottom')

ax_ent.annotate('entropy diverges\nat gen 1',
                xy=(1, raw['0.75']['e'][1]), xytext=(4.5, 2.05),
                fontsize=7, color='#555555', fontstyle='italic', ha='center',
                arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8,
                                connectionstyle='arc3,rad=0.15'),
                zorder=5)

# Panel (b): Distinct-1
ax_div.set_ylabel('Distinct-1')
ax_div.set_xlabel('Generation')
ax_div.set_xticks(gens)
ax_div.set_ylim(0.055, 0.102)
ax_div.yaxis.grid(True, alpha=0.12, linewidth=0.4, zorder=0)
ax_div.set_axisbelow(True)
ax_div.text(-0.15, 1.02, '(b)', transform=ax_div.transAxes,
            fontsize=11, fontweight='bold', va='bottom')

ax_div.annotate('diversity lags\nby $\\geq$1 gen',
                xy=(2, raw['0.75']['d'][2]), xytext=(7.5, 0.093),
                fontsize=7, color='#555555', fontstyle='italic', ha='center',
                arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8,
                                connectionstyle='arc3,rad=-0.2'),
                zorder=5)

fig.subplots_adjust(left=0.07, right=0.97, top=0.94, bottom=0.17)

for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'metric_trajectory.{fmt}', dpi=300)
plt.close()
print(f'Saved: {OUT}/metric_trajectory.pdf + .png')
