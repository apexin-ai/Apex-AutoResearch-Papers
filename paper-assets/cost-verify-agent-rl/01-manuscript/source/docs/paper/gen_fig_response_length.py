import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from collections import defaultdict

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'dejavuserif',
})

# Unified palette (D143 color unification)
C_COLLAPSE  = '#4477AA'   # blue — collapsed
C_TREATMENT = '#EE7733'   # orange — stagnant
C_SAFE      = '#228833'   # green — generalized
C_NEUTRAL   = '#808080'   # gray — SFT init

cat_to_color = {
    'Collapsed': C_COLLAPSE,
    'Stagnant': C_TREATMENT,
    'Generalized': C_SAFE,
}

cat_to_marker = {
    'Collapsed': 'o',
    'Stagnant': '^',
    'Generalized': 's',
}

cat_to_linestyle = {
    'Collapsed': '-',
    'Stagnant': '--',
    'Generalized': '-.',
}

resp_data = {
    'seed2048': {'cat': 'Collapsed', 'steps': [1,2,3,4], 'resp': [15511.5, 15865.1, 15544.1, 14940.3]},
    'seed42': {'cat': 'Collapsed', 'steps': [1,2,3,4], 'resp': [12683.7, 12227.9, 10948.4, 13759.8]},
    'seed8': {'cat': 'Collapsed', 'steps': list(range(1,10)), 'resp': [9879.0, 9535.7, 11502.0, 8879.9, 12670.0, 15165.9, 14827.1, 15168.0, 14868.9]},
    'seed100': {'cat': 'Stagnant', 'steps': [1,2,3,4], 'resp': [10635.1, 11826.2, 10838.3, 12773.0]},
    'seed4': {'cat': 'Generalized', 'steps': list(range(1,15)), 'resp': [12541.8, 12916.0, 12807.7, 11988.8, 12329.6, 9889.2, 13774.2, 13033.1, 11355.9, 10810.9, 12135.4, 13172.1, 10624.9, 10467.4]},
    'seed5': {'cat': 'Generalized', 'steps': list(range(1,11)), 'resp': [9047.0, 7444.9, 6360.0, 9547.2, 9547.2, 7944.5, 4994.0, 6449.2, 10593.7, 12150.0]},
    'seed6': {'cat': 'Generalized', 'steps': list(range(1,15)), 'resp': [14909.6, 8191.5, 10179.2, 9297.0, 8418.9, 9603.5, 5507.5, 7091.9, 6835.4, 4865.2, 4174.7, 4454.0, 6659.9, 3328.5]},
}

fig, ax = plt.subplots(figsize=(5.5, 3.2))

# Draw individual seed lines (alpha-reduced)
for seed_name, d in resp_data.items():
    cat = d['cat']
    color = cat_to_color[cat]
    ax.plot(d['steps'], [r/1000 for r in d['resp']], color=color,
            linewidth=1.0, alpha=0.35, marker='o', markersize=2.5,
            markeredgewidth=0, zorder=2)

# Compute and draw category means (bold)
cat_data = defaultdict(lambda: defaultdict(list))
for seed_name, d in resp_data.items():
    cat = d['cat']
    for s, r in zip(d['steps'], d['resp']):
        cat_data[cat][s].append(r)

for cat in ['Collapsed', 'Stagnant', 'Generalized']:
    steps_sorted = sorted(cat_data[cat].keys())
    means = [np.mean(cat_data[cat][s]) / 1000 for s in steps_sorted]
    ax.plot(steps_sorted, means, color=cat_to_color[cat],
            linewidth=2.5, alpha=0.9, marker=cat_to_marker[cat],
            linestyle=cat_to_linestyle[cat],
            markersize=5, markeredgewidth=0, zorder=4, label=cat)

# SFT init dashed line
ax.axhline(y=12.0, color=C_NEUTRAL, linestyle='--', linewidth=1.0, alpha=0.6, zorder=1)
ax.text(14.3, 12.3, 'SFT init', fontsize=8, color=C_NEUTRAL, ha='right', va='bottom')

ax.set_xlabel('Training Step')
ax.set_ylabel('Response Length (k tokens)')
ax.set_xlim(0.5, 15)
ax.set_ylim(0, 18)
ax.set_xticks([1, 3, 5, 7, 9, 11, 13])
ax.set_yticks([0, 4, 8, 12, 16])
ax.yaxis.grid(True, alpha=0.08, linestyle='-', zorder=0)

ax.legend(fontsize=8.5, loc='upper right', frameon=False,
          handlelength=1.5, borderpad=0.3)

# ── Save ──
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper'
fig.savefig(f'{out_dir}/fig_response_length.pdf')
fig.savefig(f'{out_dir}/fig_response_length.png')
plt.close()
print('Done: fig_response_length.pdf + .png')
