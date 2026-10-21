import sys
sys.path.insert(0, '/root/spectral_optim_vision_geometry')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from plot_style import apply_style, COLORS
apply_style()

plt.rcParams.update({
    'font.family': 'serif',
    'savefig.pad_inches': 0.05,
    'hatch.linewidth': 1.2,
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 14,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
})

settings = ['C100\nResNet-50', 'C100\nDeiT-S', 'C100\nConvNeXt-T',
            'IN100\nResNet-50', 'IN100\nConvNeXt-T']
gap_20 = [9.03, 10.34, 16.08, 11.47, 24.30]
gap_50 = [6.76, 10.37, 12.60, 3.56, 11.37]
change_pp = [g5 - g2 for g2, g5 in zip(gap_20, gap_50)]

yerr_20 = [0.67, 0.45, 0.88, 0.80, 1.53]
yerr_50 = [0.36, 0.60, 1.74, 0.0, 0.0]

c20 = COLORS['Muon']
c50 = COLORS['AdamW']

x = np.arange(len(settings))
width = 0.26

fig, ax = plt.subplots(figsize=(5.5, 3.5))

bars1 = ax.bar(x - width/2, gap_20, width, label='20 epochs', color=c20,
               edgecolor='white', linewidth=0.7, zorder=3,
               yerr=yerr_20, error_kw=dict(ecolor='black', capsize=3, capthick=1, lw=1))
bars2 = ax.bar(x + width/2, gap_50, width, label='50 epochs',
               facecolor=c50, edgecolor='white', linewidth=0.7, hatch='//', zorder=3,
               yerr=yerr_50, error_kw=dict(ecolor='black', capsize=3, capthick=1, lw=1))

for i, (b1, b2) in enumerate(zip(bars1, bars2)):
    x1 = b1.get_x() + b1.get_width() / 2
    x2 = b2.get_x() + b2.get_width() / 2
    if i == 1:
        ha1, ha2 = 'right', 'left'
    else:
        ha1, ha2 = 'center', 'center'
    ax.text(x1, b1.get_height() + yerr_20[i] + 0.3,
            f'+{gap_20[i]:.1f}pp', ha=ha1, va='bottom',
            fontsize=9, color='#333333')
    ax.text(x2, b2.get_height() + yerr_50[i] + 0.3,
            f'+{gap_50[i]:.1f}pp', ha=ha2, va='bottom',
            fontsize=9, color='#333333')

for i, (b1, b2) in enumerate(zip(bars1, bars2)):
    max_h = max(b1.get_height(), b2.get_height())
    bracket_y = 30 if i == 4 else min(max_h + 6.0, 27.5)
    x_left = b1.get_x() + b1.get_width() / 2
    x_right = b2.get_x() + b2.get_width() / 2
    x_mid = (x_left + x_right) / 2
    tick_h = 0.5
    delta = change_pp[i]
    bracket_color = '#888888' if abs(delta) < 0.1 else '#CC3311'
    ax.plot([x_left, x_left, x_right, x_right],
            [bracket_y - tick_h, bracket_y, bracket_y, bracket_y - tick_h],
            color=bracket_color, linewidth=1.0, zorder=5)
    if abs(delta) < 0.1:
        label = "0pp"
    else:
        arrow = "↓" if delta < 0 else "↑"
        label = f"{arrow}{abs(delta):.1f}pp"
    ax.text(x_mid, bracket_y + 0.15, label, ha='center', va='bottom',
            fontsize=9.5, fontweight='bold', color=bracket_color)

ax.set_ylabel('Muon $-$ AdamW gap (pp)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(settings, fontsize=10.5)
ax.set_ylim(0, 32)
ax.set_yticks([0, 5, 10, 15, 20, 25])
ax.legend(fontsize=11, loc='upper left', framealpha=0.9, edgecolor='none')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.3, linewidth=0.5)
ax.set_axisbelow(True)
ax.set_title('Spectral Optimizer Advantage:\nTraining Duration Effect',
             fontsize=10, fontweight='bold', pad=6, loc='center')

plt.tight_layout()
for p in [
    '/root/spectral_optim_vision_geometry/figures/fig2_gap_evolution.pdf',
    '/root/spectral_optim_vision_geometry/figures/fig2_gap_evolution.png',
    '/root/spectral_optim_vision_geometry/paper/figures/fig2_gap_evolution.pdf',
    '/root/spectral_optim_vision_geometry/paper/figures/fig2_gap_evolution.png',
]:
    fig.savefig(p)
plt.close(fig)
print('Figure 2 v2 saved.')
