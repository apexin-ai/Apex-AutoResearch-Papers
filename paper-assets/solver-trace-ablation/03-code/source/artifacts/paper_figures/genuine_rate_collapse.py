"""Temporal Genuine Rate Collapse figure for §4.2."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'legend.fontsize': 7,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'lines.linewidth': 1.4,
    'lines.markersize': 5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

steps = [500, 1000]

conditions = {
    'Exec-only':       {'500': 7.5,  '1000': 0.0,  'color': '#1f77b4', 'marker': 'o',  'ls': '-'},
    r'ISR $\beta{=}0.1$': {'500': 30.9, '1000': 2.2,  'color': '#ff7f0e', 'marker': 's',  'ls': '-'},
    r'ISR $\beta{=}0.3$': {'500': 5.6,  '1000': 0.0,  'color': '#2ca02c', 'marker': '^',  'ls': '-'},
    r'Random $\beta{=}0.1$': {'500': 29.1, '1000': 0.0, 'color': '#d62728', 'marker': 'D', 'ls': '-'},
    'SFT':             {'500': 93.0, '1000': 92.3, 'color': '#7f7f7f', 'marker': 'x',  'ls': '--'},
}

fig, ax = plt.subplots(figsize=(3.5, 2.5))

for name, d in conditions.items():
    vals = [d['500'], d['1000']]
    ax.plot(steps, vals, color=d['color'], marker=d['marker'],
            linestyle=d['ls'], label=name, zorder=3)

ax.set_xlabel('Training Steps')
ax.set_ylabel('Genuine Rate (%)')
ax.set_title('Temporal Genuine Rate Collapse Under Reward Optimization')
ax.set_xticks(steps)
ax.set_xlim(400, 1100)
ax.set_ylim(-3, 100)
ax.legend(loc='center right', frameon=True, fancybox=False, edgecolor='0.7')
ax.grid(True, alpha=0.3, linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_figures'
fig.savefig(f'{outdir}/genuine_rate_collapse.pdf')
fig.savefig(f'{outdir}/genuine_rate_collapse.png')
plt.close()
print('Saved genuine_rate_collapse.pdf and .png')
