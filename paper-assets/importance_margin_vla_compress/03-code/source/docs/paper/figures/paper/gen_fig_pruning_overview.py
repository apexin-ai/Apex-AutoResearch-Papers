#!/usr/bin/env python3
"""Generate fig_pruning_overview: VLA disruption curves under token pruning."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

# ── rcParams ──────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10.5,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.06,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 2.0,
})

# ── Data (LIBERO-Object, best scoring method per model) ──────────────
data = {
    r'$\pi_{0.5}$': {
        'k':  [1.0,  0.95, 0.9,  0.85, 0.7,  0.5],
        'sr': [98.2, 98.2, 98.2, 98.0, 55.0, 33.4],
        'cv': 0.055,
        'method': 'L2',
        'color': '#0072B2',
        'marker': 'o',
    },
    'X-VLA': {
        'k':  [1.0,  0.95, 0.9,  0.7,  0.5],
        'sr': [99.2, 99.0, 99.2, 56.2, 43.4],
        'cv': 0.151,
        'method': 'L2',
        'color': '#E69F00',
        'marker': '^',
    },
    'OpenVLA': {
        'k':  [1.0,  0.9,  0.5],
        'sr': [74.0, 70.6, 39.2],
        'cv': 0.215,
        'method': 'L2',
        'color': '#009E73',
        'marker': 's',
    },
    'SmolVLA': {
        'k':  [1.0,  0.95, 0.9, 0.7, 0.5],
        'sr': [59.2, 0.0,  0.0, 0.0, 0.0],
        'cv': 0.314,
        'method': 'L2',
        'color': '#D55E00',
        'marker': 'X',
    },
}

# ── Figure ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(4.2, 2.8))

# Pattern A: regime bands (vertical spans)
ax.axvspan(0.9, 1.01, alpha=0.05, color='#009E73', zorder=0)
ax.axvspan(0.28, 0.5, alpha=0.05, color='#D55E00', zorder=0)

# Band labels — at top
t = ax.text(0.955, 105, 'safe zone', fontsize=5.5, color='#5a9a5a',
            ha='center', va='bottom', fontstyle='italic', alpha=0.8)
t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])
t = ax.text(0.39, 105, 'aggressive', fontsize=5.5, color='#aa6644',
            ha='center', va='bottom', fontstyle='italic', alpha=0.8)
t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

# Plot curves
for name, d in data.items():
    k, sr = d['k'], d['sr']
    label = f"{name} (CV={d['cv']:.3f}, {d['method']})"
    ax.plot(k, sr, color=d['color'], marker=d['marker'],
            linewidth=2, markersize=5, markeredgewidth=0.5,
            markeredgecolor='white', label=label, zorder=3,
            solid_capstyle='round')

# ── Annotations (Pattern F + Pattern J) ──────────────────────────────

# SmolVLA cliff at k=0.95 → arrow pointing down to 0%
ax.annotate('0%', xy=(0.95, 0.0), xytext=(0.865, 24),
            fontsize=7, fontweight='bold', color='#D55E00',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='->', color='#D55E00',
                            lw=0.9, shrinkA=0, shrinkB=3),
            zorder=5)
t = ax.text(0.865, 18.5, 'cliff', fontsize=5.5, color='#D55E00',
            ha='center', fontstyle='italic', alpha=0.85)
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# π₀.₅ plateau label at k=0.85 — below the curve
t = ax.text(0.845, 91, '98%', fontsize=6.5, fontweight='bold',
            color='#0072B2', ha='center', va='top')
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# X-VLA cliff at k=0.7 — offset to avoid intersection with other curves
ax.annotate('56%', xy=(0.7, 56.2), xytext=(0.62, 64),
            fontsize=6.5, fontweight='bold', color='#E69F00',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='-', color='#E69F00',
                            lw=0.5, shrinkA=0, shrinkB=2),
            zorder=5)

# ── Axes ──────────────────────────────────────────────────────────────
ax.set_xlim(1.02, 0.28)
ax.set_xticks([1.0, 0.95, 0.9, 0.85, 0.7, 0.5, 0.3])
ax.set_xticklabels(['1.0', '.95', '.9', '.85', '.7', '.5', '.3'])
ax.set_ylim(-5, 112)
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_xlabel('Retention Ratio $k$')
ax.set_ylabel('Success Rate (%)')

# Grid
ax.grid(True, alpha=0.25, linewidth=0.4, zorder=0)
ax.set_axisbelow(True)

# Legend — upper right (visually: low k, high SR — empty area)
ax.legend(loc='upper right', frameon=False, fontsize=7,
          handlelength=1.6, handletextpad=0.4, borderpad=0.3,
          labelspacing=0.3, bbox_to_anchor=(0.98, 0.96))

plt.tight_layout()

# ── Save ──────────────────────────────────────────────────────────────
out_dir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper'
fig.savefig(f'{out_dir}/fig_pruning_overview.pdf')
fig.savefig(f'{out_dir}/fig_pruning_overview.png')
plt.close()
print(f'Saved to {out_dir}/fig_pruning_overview.{{pdf,png}}')
