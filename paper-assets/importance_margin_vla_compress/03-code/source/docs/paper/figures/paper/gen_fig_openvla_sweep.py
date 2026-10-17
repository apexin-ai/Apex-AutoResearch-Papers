"""
OpenVLA k-value sweep — 2×2 panel (Object/Spatial/Goal/Long).
Shows L2/Random/Attention degradation across retention ratios.
Highlights the suite-dependent crossover: L2 wins on Object,
Attention wins on Spatial, Random wins on Goal, all converge on Long.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

OUT = Path(__file__).parent

COL_L2   = '#0072B2'
COL_RAND = '#D55E00'
COL_ATTN = '#009E73'

SUITES = {
    'Object': {
        'baseline': 74.0,
        'l2':   {'k': [1.0, 0.95, 0.9, 0.85, 0.75, 0.5],  'sr': [74.0, 70.6, 70.6, 55.2, 57.4, 39.2]},
        'rand': {'k': [1.0, 0.9, 0.85, 0.5],               'sr': [74.0, 62.8, 60.4, 35.8]},
        'attn': {'k': [1.0, 0.9, 0.85, 0.75, 0.5],         'sr': [74.0, 61.4, 55.0, 53.2, 40.6]},
        'winner_k09': 'L2',
    },
    'Spatial': {
        'baseline': 80.0,
        'l2':   {'k': [1.0, 0.9],  'sr': [80.0, 75.0]},
        'rand': {'k': [1.0, 0.9],  'sr': [80.0, 79.8]},
        'attn': {'k': [1.0, 0.9],  'sr': [80.0, 80.4]},
        'winner_k09': 'A',
    },
    'Goal': {
        'baseline': 74.8,
        'l2':   {'k': [1.0, 0.9, 0.75, 0.7],  'sr': [74.8, 74.8, 70.2, 68.4]},
        'rand': {'k': [1.0, 0.9, 0.85, 0.7],         'sr': [74.8, 79.6, 78.6, 68.4]},
        'attn': {'k': [1.0, 0.9, 0.7],               'sr': [74.8, 73.2, 66.4]},
        'winner_k09': 'R',
    },
    'Long': {
        'baseline': 52.8,
        'l2':   {'k': [1.0, 0.9, 0.85, 0.7],  'sr': [52.8, 43.6, 38.8, 31.2]},
        'rand': {'k': [1.0, 0.9, 0.7],         'sr': [52.8, 46.8, 38.8]},
        'attn': {'k': [1.0, 0.9, 0.85, 0.7],   'sr': [52.8, 44.0, 45.8, 24.0]},
        'winner_k09': '≈',
    },
}

fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.0), sharex=False)
axes = axes.flatten()

for idx, (suite, data) in enumerate(SUITES.items()):
    ax = axes[idx]
    bl = data['baseline']

    ax.axhline(bl, color='#cccccc', linestyle=':', linewidth=0.7, zorder=0)

    for method, color, marker, label in [
        ('l2',   COL_L2,   'o', 'L2 Norm'),
        ('rand', COL_RAND, 's', 'Random'),
        ('attn', COL_ATTN, '^', 'Attention'),
    ]:
        d = data[method]
        ax.plot(d['k'], d['sr'], '-' + marker, color=color,
                linewidth=1.8, markersize=5, markerfacecolor='white',
                markeredgewidth=1.3, zorder=3, label=label if idx == 0 else None)

    winner = data['winner_k09']
    winner_colors = {'L2': COL_L2, 'A': COL_ATTN, 'R': COL_RAND, '≈': '#888888'}
    ax.text(0.97, 0.05, f'Best at k=0.9: {winner}',
            transform=ax.transAxes, fontsize=7, color=winner_colors[winner],
            fontweight='bold', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=winner_colors[winner], alpha=0.85, linewidth=0.6))

    ax.set_title(suite, fontsize=10.5, fontweight='semibold', pad=6)
    ax.set_ylabel('SR (%)' if idx % 2 == 0 else '', fontsize=9)
    ax.set_xlabel('Retention Ratio $k$' if idx >= 2 else '', fontsize=9)
    ax.set_xlim(0.45, 1.05)
    y_lo = max(0, min(min(d['sr']) for d in [data['l2'], data['rand'], data['attn']]) - 8)
    y_hi = bl + 8
    ax.set_ylim(y_lo, y_hi)
    ax.tick_params(axis='both', labelsize=8)
    ax.grid(axis='y', color='#f0f0f0', linewidth=0.4, zorder=0)

fig.legend(axes[0].get_legend_handles_labels()[0],
           axes[0].get_legend_handles_labels()[1],
           loc='upper center', ncol=3, fontsize=8.5,
           frameon=True, edgecolor='#dddddd', framealpha=0.9,
           bbox_to_anchor=(0.5, 1.02))

fig.suptitle('OpenVLA — Suite-Dependent Method Crossover',
             fontsize=12, fontweight='semibold', y=1.06, color='#222222')

plt.tight_layout(rect=[0, 0, 1, 0.97])
fig.savefig(OUT / 'fig_openvla_sweep.pdf', format='pdf', bbox_inches='tight')
fig.savefig(OUT / 'fig_openvla_sweep.png', format='png', bbox_inches='tight')
print(f"Saved: {OUT / 'fig_openvla_sweep.pdf'}")
print(f"Saved: {OUT / 'fig_openvla_sweep.png'}")
plt.close()
