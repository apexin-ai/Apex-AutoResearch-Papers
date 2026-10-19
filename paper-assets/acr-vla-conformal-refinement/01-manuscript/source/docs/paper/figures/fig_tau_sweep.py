"""Tau-sweep line plot: SR vs threshold for 4 LIBERO suites."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

SHARED_HEIGHT = 2.5          # inches — must match fig_magnitude_curve.py
SHARED_WIDTH  = 3.3          # inches — must match fig_magnitude_curve.py

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'lines.linewidth': 2.0,
    'lines.markersize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

data = {
    'Spatial': {'tau': [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.45],
                'sr':  [78.0, 80.5, 81.0, 80.0, 79.5, 80.0, 80.0],
                'baseline': 79.3},
    'Goal':    {'tau': [0.15, 0.25, 0.35, 0.45],
                'sr':  [84.5, 83.8, 84.0, 83.5],
                'baseline': 83.7},
    'Object':  {'tau': [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45],
                'sr':  [75.0, 78.0, 76.2, 78.5, 76.5, 79.0, 75.5, 73.5, 71.5],
                'baseline': 77.7},
    'Long':    {'tau': [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45],
                'sr':  [53.5, 61.0, 56.5, 54.5, 55.0, 58.8, 60.0, 59.5],
                'baseline': 58.0},
}

colors = {
    'Spatial': '#7BAACF',
    'Object': '#82C8A0',
    'Goal': '#F0B87A',
    'Long': '#BB8FCC',
}
markers = {'Spatial': 'o', 'Goal': 's', 'Object': '^', 'Long': 'D'}

fig, ax = plt.subplots(figsize=(SHARED_WIDTH, SHARED_HEIGHT))

ax.axvspan(0.15, 0.35, color='#F0F0F0', zorder=0)
bracket_y = 89.0
ax.plot([0.15, 0.15, 0.35, 0.35], [bracket_y - 0.8, bracket_y, bracket_y, bracket_y - 0.8],
        color='#AAAAAA', lw=0.6, zorder=5)
ax.text(0.25, bracket_y + 0.3, 'recommended', ha='center', va='bottom',
        fontsize=9.5, color='#888888', fontstyle='italic')

for suite, d in data.items():
    ax.plot(d['tau'], d['sr'], color=colors[suite], marker=markers[suite],
            markersize=6, linewidth=2.0, label=suite, zorder=3, alpha=0.9)
    ax.axhline(d['baseline'], color=colors[suite], linestyle='--', alpha=0.25,
               linewidth=0.8, zorder=1)

label_positions = {
    'Spatial': (0.012, 0.5),
    'Goal':    (0.012, 0.3),
    'Object':  (0.012, -0.3),
    'Long':    (0.012, 0.8),
}
for suite, d in data.items():
    dx, dy = label_positions[suite]
    x = d['tau'][-1]
    y = d['sr'][-1]
    ax.text(x + dx, y + dy, suite, fontsize=9, color=colors[suite],
            fontweight='bold', va='center')

crm_on = {'Spatial': 78.0, 'Object': 73.0, 'Goal': 80.0, 'Long': 43.2}
for suite, sr in crm_on.items():
    ax.plot(0.0, sr, marker='x', color=colors[suite], markersize=8,
            markeredgewidth=1.8, zorder=4)

ax.annotate(r'CRM always-on ($\tau{\to}0$)', xy=(0.0, 43.2), xytext=(0.07, 45),
            fontsize=9, color='#777777', fontstyle='italic',
            arrowprops=dict(arrowstyle='->', color='#AAAAAA', lw=0.7))

tr_annotations = [
    ('Spatial', 0.10, 78.0 + 2.5, '74%', 'center'),
    ('Spatial', 0.35, 80.0 + 2.0, '12%', 'center'),
    ('Object', 0.35, 75.5 - 3.0, '1.3%', 'center'),
    ('Goal', 0.165, 84.5 + 2.0, '34%', 'left'),
    ('Long', 0.155, 61.0 + 2.5, '24%', 'left'),
]

for suite, x, y, tr_str, ha in tr_annotations:
    ax.text(x, y, tr_str, ha=ha, va='center',
            fontsize=9, color=colors[suite], alpha=0.8,
            bbox=dict(boxstyle='round,pad=0.12', facecolor='white',
                      edgecolor='none', alpha=0.75))

ax.text(0.97, 0.03, '% = trigger rate',
        transform=ax.transAxes, fontsize=9, color='#999999',
        ha='right', va='bottom', fontstyle='italic')

ax.set_xlabel(r'Threshold $\tau$')
ax.set_ylabel('Success rate (%)')
ax.set_xlim(-0.02, 0.53)
ax.set_ylim(38, 93)
# Legend removed: each line is labeled at its endpoint (see label_positions)

ax.yaxis.grid(True, alpha=0.2, linewidth=0.4, zorder=0)

plt.tight_layout()

out = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out, 'fig_tau_sweep.pdf'), format='pdf')
fig.savefig(os.path.join(out, 'fig_tau_sweep.png'), format='png', dpi=300)
plt.close()
print('Tau sweep saved.')
