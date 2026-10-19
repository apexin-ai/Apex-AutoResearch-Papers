"""Teaser figure: degradation vs recovery across 4 LIBERO suites."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

suites = ['Spatial', 'Object', 'Goal', 'Long']
delta_crm = [-1.3, -4.7, -3.7, -14.8]
delta_gate = [+2.8, +4.8, +4.8, +13.5]

fig, ax = plt.subplots(figsize=(5.5, 2.5))

x = np.arange(len(suites))
w = 0.35

bars1 = ax.bar(x - w/2, delta_crm, w, color='#F4C28C', alpha=0.92,
               label=r'$\Delta_{\mathrm{CRM}}$: unconditional correction',
               edgecolor='#D68910', linewidth=0.4, zorder=3)
bars2 = ax.bar(x + w/2, delta_gate, w, color='#9DC4DB', alpha=0.92,
               label=r'$\Delta_{\mathrm{gate}}$: $\tau$-gating recovery',
               edgecolor='#1A5276', linewidth=0.4, zorder=3)

for bar, val in zip(bars1, delta_crm):
    ax.text(bar.get_x() + bar.get_width()/2, val - 0.6, f'{val:+.1f}',
            ha='center', va='top', fontsize=7, color='#D68910', fontweight='bold')
for bar, val in zip(bars2, delta_gate):
    ax.text(bar.get_x() + bar.get_width()/2, val + 0.4, f'+{val:.1f}',
            ha='center', va='bottom', fontsize=7, color='#1A5276', fontweight='bold')

ax.axhline(0, color='#333333', linewidth=0.8, zorder=2)
ax.set_xticks(x)
ax.set_xticklabels(suites)
ax.set_ylabel('Success rate change (pp)')
ax.set_ylim(-16.5, 16.5)
ax.legend(loc='upper left', frameon=True, fancybox=False, edgecolor='#cccccc',
          framealpha=0.95)

ax.annotate('CRM is OOD\non Long', xy=(3 - w/2, -13.0), xytext=(1.95, -10),
            fontsize=7, color='#666666', fontstyle='italic',
            arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8))

ax.yaxis.grid(True, alpha=0.3, linewidth=0.4, color='#cccccc', zorder=0)

plt.tight_layout(pad=0.3)
out = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out, 'fig_teaser.pdf'), bbox_inches='tight', pad_inches=0.02)
fig.savefig(os.path.join(out, 'fig_teaser.png'), bbox_inches='tight', pad_inches=0.02)
print('Teaser saved.')
