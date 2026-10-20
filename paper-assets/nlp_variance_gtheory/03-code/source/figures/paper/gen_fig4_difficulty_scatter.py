"""Regenerate fig4_difficulty_scatter: difficulty heterogeneity vs item variance.
Data source: cross_benchmark_difficulty_heterogeneity.json (exp004).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
    'font.size': 9,
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

data = {
    'MMLU':     {'std_pi': 0.3112, 'item_id_pct': 37.88, 'fmt': 'MC'},
    'ARC':      {'std_pi': 0.2737, 'item_id_pct': 37.88, 'fmt': 'MC'},
    'HellaSwag':{'std_pi': 0.2822, 'item_id_pct': 34.27, 'fmt': 'MC'},
    'GSM8K':    {'std_pi': 0.2203, 'item_id_pct': 16.86, 'fmt': 'FF'},
    'MATH':     {'std_pi': 0.2283, 'item_id_pct': 24.03, 'fmt': 'FF'},
}
rho, pval = 0.8208, 0.0886

mc_color = '#2166AC'
ff_color = '#B2182B'

fig, ax = plt.subplots(figsize=(5.0, 3.0))
fig.subplots_adjust(left=0.065, right=0.995, top=0.95, bottom=0.15)

mc_bms = [k for k, v in data.items() if v['fmt'] == 'MC']
ff_bms = [k for k, v in data.items() if v['fmt'] == 'FF']

offsets = {
    'MMLU': (-8, -10), 'ARC': (6, 5), 'HellaSwag': (-12, -10),
    'GSM8K': (6, -7), 'MATH': (6, 5),
}
ha_map = {
    'MMLU': 'right', 'ARC': 'left', 'HellaSwag': 'right',
    'GSM8K': 'left', 'MATH': 'left',
}

for bm in mc_bms:
    d = data[bm]
    ax.scatter(d['std_pi'], d['item_id_pct'], c=mc_color, marker='o',
               s=120, zorder=5, edgecolors='white', linewidths=0.6)
    ox, oy = offsets[bm]
    ax.annotate(bm, (d['std_pi'], d['item_id_pct']),
                xytext=(ox, oy), textcoords='offset points',
                fontsize=9, ha=ha_map[bm], va='center', fontweight='bold')

for bm in ff_bms:
    d = data[bm]
    ax.scatter(d['std_pi'], d['item_id_pct'], c=ff_color, marker='s',
               s=120, zorder=5, edgecolors='white', linewidths=0.6)
    ox, oy = offsets[bm]
    ax.annotate(bm, (d['std_pi'], d['item_id_pct']),
                xytext=(ox, oy), textcoords='offset points',
                fontsize=9, ha=ha_map[bm], va='center', fontweight='bold')

mc_pts = sorted([(data[b]['std_pi'], data[b]['item_id_pct']) for b in mc_bms])
ax.plot([p[0] for p in mc_pts], [p[1] for p in mc_pts],
        '--', color=mc_color, alpha=0.4, linewidth=1.0, zorder=3)
ff_pts = sorted([(data[b]['std_pi'], data[b]['item_id_pct']) for b in ff_bms])
ax.plot([p[0] for p in ff_pts], [p[1] for p in ff_pts],
        '--', color=ff_color, alpha=0.4, linewidth=1.0, zorder=3)

ax.text(0.97, 0.05, f"Spearman $\\rho$ = {rho:.2f}\n$p$ = {pval:.3f}",
        transform=ax.transAxes, fontsize=8, va='bottom', ha='right',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='wheat', alpha=0.5))

legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=mc_color,
           markersize=8, label='MC (filled)'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor=ff_color,
           markersize=8, label='FF (open)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=8, framealpha=0.7)

ax.set_xlabel(r"Difficulty heterogeneity std($p_i$)")
ax.set_ylabel("Item var. (%)", labelpad=2)
ax.spines['left'].set_linewidth(0.8)
ax.spines['bottom'].set_linewidth(0.8)
ax.tick_params(axis='both', pad=1)
ax.tick_params(axis='y', pad=1)

ax.set_xlim(0.21, 0.32)
ax.set_ylim(13, 42)

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig4_difficulty_scatter.pdf', dpi=300)
fig.savefig(out_dir / 'fig4_difficulty_scatter.png', dpi=200)
plt.close()
print("Saved fig4_difficulty_scatter.pdf and .png")
