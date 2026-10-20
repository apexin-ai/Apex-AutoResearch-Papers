import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

operators = [
    'P2: Sub-Goal Deletion',
    'C1: Context Truncation',
    'P1: Step Order Swap',
    'C4: Observation Masking',
]
deltas = [-8.4, -5.6, -2.7, 6.1]

colors = ['#009E73' if d > 0 else '#D55E00' for d in deltas]

fig, ax = plt.subplots(figsize=(3.5, 2.2))

y_pos = np.arange(len(operators))
bars = ax.barh(y_pos, deltas, height=0.55, color=colors, edgecolor='white', linewidth=0.5)

ax.set_yticks(y_pos)
ax.set_yticklabels(operators)
ax.set_xlabel('TaxEI − Vanilla (pp)')
ax.set_xlim(-12, 10)

ax.axvline(x=0, color='black', linewidth=0.6)

for i, (bar, delta) in enumerate(zip(bars, deltas)):
    label = f'+{delta}' if delta > 0 else f'{delta}'
    if delta > 0:
        ax.text(delta + 0.3, i, label, va='center', ha='left', fontsize=7.5, color='#007a5a')
    else:
        ax.text(delta - 0.3, i, label, va='center', ha='right', fontsize=7.5, color='#b04a00')

ax.annotate(
    '', xy=(1.03, -0.02), xycoords='axes fraction',
    xytext=(1.03, 1.02), textcoords='axes fraction',
    arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8),
)
ax.text(1.07, 0.95, 'Local/\nObservable', transform=ax.transAxes,
        fontsize=5.5, color='#999999', va='top', ha='left', rotation=-90,
        linespacing=1.2)
ax.text(1.07, 0.25, 'Global/\nCascading', transform=ax.transAxes,
        fontsize=5.5, color='#999999', va='top', ha='left', rotation=-90,
        linespacing=1.2)

ax.grid(axis='x', alpha=0.15, linewidth=0.5)

plt.tight_layout()

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/figures/paper/fig2_operator_gradient'
fig.savefig(out_base + '.pdf')
fig.savefig(out_base + '.png')
plt.close()
print('Done')
