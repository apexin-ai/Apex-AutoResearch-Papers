import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np

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
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

conditions = ['Vanilla', 'Full OCC\n(BN)', 'Full OCC\n(LN)', 'Detach\n+BN', 'Detach\n+LN']
car_means  = [0.780,     0.797,            None,              0.746,         0.765]
car_stds   = [0.012,     0.032,            None,              0.002,         0.023]

colors      = ['#9E9E9E', '#3778BF', '#D0D0D0', '#C95B4B', '#D98880']
edge_colors = ['#757575', '#2C5F8A', '#A0A0A0', '#A0392B', '#B5544A']

fig, ax = plt.subplots(figsize=(6.2, 4.0))

x = np.arange(len(conditions))
bar_width = 0.58

for i, (mean, std, c, ec) in enumerate(zip(car_means, car_stds, colors, edge_colors)):
    if mean is None:
        ax.bar(x[i], 0.790, width=bar_width, color='#EEEEEE', edgecolor='#BBBBBB',
               linewidth=1.2, linestyle='--', zorder=2, alpha=0.6)
        ax.text(x[i], 0.792, 'RUNNING', ha='center', va='bottom', fontsize=7.5,
                color='#999999', fontstyle='italic', fontweight='bold')
    else:
        ax.bar(x[i], mean, width=bar_width, color=c, edgecolor=ec,
               linewidth=0.8, zorder=2, alpha=0.88)
        ax.errorbar(x[i], mean, yerr=std, fmt='none', ecolor='#444444',
                    capsize=4.5, capthick=1.0, elinewidth=1.0, zorder=3)
        t = ax.text(x[i], mean + std + 0.004, f'{mean:.3f}', ha='center', va='bottom',
                    fontsize=9, fontweight='bold', color='#333333')
        t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Vanilla baseline dashed line
ax.axhline(y=0.780, color='#9E9E9E', linestyle=':', linewidth=1.0, alpha=0.5, zorder=1)

# Arrow 1: Detach+BN → Detach+LN  "+1.9pp (BN fix)"
mid_x_bn = 3.5
ax.annotate('', xy=(4, 0.765), xytext=(3, 0.746),
            arrowprops=dict(arrowstyle='->', color='#A0392B', lw=1.5,
                            connectionstyle='arc3,rad=-0.3'))
t_bn = ax.text(mid_x_bn, 0.725, '+1.9pp\n(norm fix)', ha='center', va='top',
               fontsize=8, color='#A0392B', fontstyle='italic', fontweight='bold',
               linespacing=1.0)
t_bn.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

# Arrow 2: Detach+LN → Vanilla  "+1.5pp (gradient flow)"
ax.annotate('', xy=(0, 0.780), xytext=(4, 0.765),
            arrowprops=dict(arrowstyle='->', color='#2C5F8A', lw=1.5,
                            connectionstyle='arc3,rad=0.3'))
t_gf = ax.text(2.0, 0.810, '+1.5pp (gradient flow)', ha='center', va='bottom',
               fontsize=8, color='#2C5F8A', fontstyle='italic', fontweight='bold')
t_gf.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

# Legend
legend_handles = [
    mpatches.Patch(facecolor='#9E9E9E', edgecolor='#757575', label='Baseline (no OCC)'),
    mpatches.Patch(facecolor='#3778BF', edgecolor='#2C5F8A', label='With gradient flow'),
    mpatches.Patch(facecolor='#C95B4B', edgecolor='#A0392B', label='No gradient flow (detach)'),
    mpatches.Patch(facecolor='#EEEEEE', edgecolor='#BBBBBB', label='Running', linestyle='--'),
]
ax.legend(handles=legend_handles, loc='lower left', framealpha=0.95,
          edgecolor='#DDDDDD', fontsize=8.5, borderpad=0.6)

ax.set_xticks(x)
ax.set_xticklabels(conditions)
ax.set_ylabel('Collision Avoidance Rate (CAR)')
ax.set_ylim(0.705, 0.855)
ax.set_xlim(-0.5, len(conditions) - 0.5)
ax.grid(axis='y', alpha=0.15, zorder=0)

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/figures'
plt.savefig(f'{outdir}/factorial_2x2_bar.pdf')
plt.savefig(f'{outdir}/factorial_2x2_bar.png')
print('Saved factorial_2x2_bar.pdf/.png')
