#!/usr/bin/env python3
"""Figure 1: Strip plot of per-generator Spearman rho (8 generators)."""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
})

with open('/root/gen-depth-fingerprint/results/8gen_per_gen_spearman.json') as f:
    data = json.load(f)

features = ['hapax_ratio', 'ttr', 'entropy_mean', 'entropy_min', 'entropy_std', 'entropy_max', 'tail_decay']
feat_labels = ['Hapax', 'TTR', r'$\bar{H}$', r'$H_{\min}$', r'$\sigma_H$', r'$H_{\max}$', 'Tail Dec.']

overall = data['_median']

ZONE_COLORS = {
    'strong':     '#B2182B',
    'moderate':   '#2166AC',
    'stationary': '#666666',
}

generators = [
    'pythia-1b', 'pythia-2.8b', 'olmo-2-1b',
    'qwen3-0.6b', 'qwen3-1.7b', 'qwen3-8b',
    'llama-3.2-3b', 'mistral-7b-v0.3',
]

# Family-grouped colors (same family = same color, different marker)
COLORS = {
    'pythia-1b':       '#E69F00',
    'pythia-2.8b':     '#E69F00',
    'olmo-2-1b':       '#009E73',
    'qwen3-0.6b':      '#0072B2',
    'qwen3-1.7b':      '#0072B2',
    'qwen3-8b':        '#0072B2',
    'llama-3.2-3b':    '#D55E00',
    'mistral-7b-v0.3': '#CC79A7',
}

MARKERS = {
    'pythia-1b':       'o',
    'pythia-2.8b':     's',
    'olmo-2-1b':       '^',
    'qwen3-0.6b':      'D',
    'qwen3-1.7b':      'v',
    'qwen3-8b':        'P',
    'llama-3.2-3b':    'h',
    'mistral-7b-v0.3': '*',
}

LABELS = {
    'pythia-1b':       'Pythia-1B',
    'pythia-2.8b':     'Pythia-2.8B',
    'olmo-2-1b':       'OLMo-2-1B',
    'qwen3-0.6b':      'Qwen3-0.6B',
    'qwen3-1.7b':      'Qwen3-1.7B',
    'qwen3-8b':        'Qwen3-8B',
    'llama-3.2-3b':    'Llama-3.2-3B',
    'mistral-7b-v0.3': 'Mistral-7B-v0.3',
}

fig, ax = plt.subplots(figsize=(3.25, 2.8))

x = np.arange(len(features))
jitter_offsets = np.linspace(-0.25, 0.25, len(generators))

for gi, gen in enumerate(generators):
    vals = [data[gen][f] for f in features]
    ax.scatter(
        x + jitter_offsets[gi], vals,
        marker=MARKERS[gen], color=COLORS[gen], s=18, linewidths=0.4,
        edgecolors='white', zorder=3, label=LABELS[gen],
    )

overall_vals = [overall[f] for f in features]
ax.scatter(
    x, overall_vals, marker='X', color='black', s=45, linewidths=0.5,
    edgecolors='black', zorder=4, label='Overall',
)

ax.axhline(0, color='black', linewidth=0.4, zorder=1)
ax.axhline(-0.15, color='gray', linewidth=0.5, linestyle='--', alpha=0.4, zorder=1)
ax.axhline(0.15, color='gray', linewidth=0.5, linestyle='--', alpha=0.4, zorder=1)

# Zone background shading
zone_spans = [(0, 2, 'strong'), (3, 4, 'moderate'), (5, 6, 'stationary')]
for start, end, zone in zone_spans:
    color = ZONE_COLORS[zone]
    for i in range(start, end + 1):
        ax.axvspan(i - 0.4, i + 0.4, color=color, alpha=0.05, zorder=0)

ax.set_xticks(x)
ax.set_xticklabels(feat_labels)
ax.set_ylabel(r"Spearman $\rho$ with Depth")
ax.set_ylim(-0.82, 0.45)

# --- Three-tier bracket annotations ---
bracket_y = 0.27
tick_len = 0.02
name_y = bracket_y + 0.025
range_y = bracket_y + 0.09

def draw_bracket(ax, x_left, x_right, y, color, name, rho_range, lw=0.9):
    ax.plot([x_left, x_left, x_right, x_right],
            [y - tick_len, y, y, y - tick_len],
            color=color, lw=lw, clip_on=False, solid_capstyle='butt')
    cx = (x_left + x_right) / 2
    ax.text(cx, name_y, name,
            fontsize=5.5, fontstyle='italic', fontweight='bold', color=color,
            ha='center', va='bottom', clip_on=False)
    ax.text(cx, range_y, rho_range,
            fontsize=4.5, color=color,
            ha='center', va='bottom', clip_on=False)

draw_bracket(ax, -0.4, 2.4, bracket_y, ZONE_COLORS['strong'],
             'Strong drift', r'$|\rho| \gtrsim 0.6$')
draw_bracket(ax, 2.6, 4.4, bracket_y, ZONE_COLORS['moderate'],
             'Moderate', r'$|\rho|\approx 0.16$–$0.40$')
draw_bracket(ax, 4.6, 6.4, bracket_y, ZONE_COLORS['stationary'],
             'Near-stationary', r'$|\rho| < 0.07$')

handles, labels_list = ax.get_legend_handles_labels()
leg = ax.legend(handles, labels_list, loc='lower center', ncol=3, frameon=True,
          fancybox=False, edgecolor='#cccccc', framealpha=0.95,
          handletextpad=0.3, columnspacing=0.6, borderpad=0.3,
          bbox_to_anchor=(0.5, -0.62))

plt.subplots_adjust(bottom=0.32)

outdir = Path('/root/gen-depth-fingerprint')
fig.savefig(outdir / 'fig1_differential_response.pdf', facecolor='white')
fig.savefig(outdir / 'fig1_differential_response.png', dpi=300, facecolor='white')
print(f'Saved to {outdir}/fig1_differential_response.{{pdf,png}}')

plt.close()
