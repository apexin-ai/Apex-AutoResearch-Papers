#!/usr/bin/env python3
"""Generate Figure 2: (a) CAR bar chart + (b) 2x2 interaction plot."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# Data
conditions = ['Full OCC\n(BN)', 'Detach\n(BN)', 'Full OCC\n(LN)', 'Detach\n(LN)', 'Vanilla']
car_means = [0.725, 0.767, 0.773, 0.802, 0.745]
car_sds =   [0.064, 0.024, 0.027, 0.024, 0.024]
colors = ['#4878CF', '#6A9FD8', '#E8833A', '#F0A868', '#999999']
edge_colors = ['#2A5BAA', '#4878CF', '#C0611A', '#E8833A', '#666666']

vanilla_mean = 0.745

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.8),
                                gridspec_kw={'width_ratios': [1.15, 1], 'wspace': 0.35})

# --- Panel (a): Bar chart ---
x = np.arange(len(conditions))
bars = ax1.bar(x, car_means, yerr=car_sds, width=0.6,
               color=colors, edgecolor=edge_colors, linewidth=0.8,
               capsize=3, error_kw={'linewidth': 1.0, 'capthick': 1.0})

ax1.axhline(y=vanilla_mean, color='#888888', linestyle='--', linewidth=1.0,
            label=f'Vanilla ({vanilla_mean:.3f})', zorder=0)

ax1.set_xticks(x)
ax1.set_xticklabels(conditions, fontsize=8)
ax1.set_ylabel('Collision Avoidance Rate (CAR)')
ax1.set_ylim(0.62, 0.86)
ax1.yaxis.set_major_locator(mticker.MultipleLocator(0.04))
ax1.yaxis.set_minor_locator(mticker.MultipleLocator(0.02))
ax1.legend(loc='lower right', framealpha=0.9, edgecolor='#cccccc')
ax1.set_title('(a)', fontweight='bold', loc='left', pad=4)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

for i, (m, s) in enumerate(zip(car_means, car_sds)):
    if i < 4:
        delta = m - vanilla_mean
        sign = '+' if delta > 0 else ''
        ax1.text(i, m + s + 0.008, f'{sign}{delta*100:.1f}pp',
                 ha='center', va='bottom', fontsize=7, color=edge_colors[i])

# --- Panel (b): Interaction plot ---
x_flow = [0, 1]
x_labels = ['Gradient ON', 'Gradient OFF']

bn_means = [0.725, 0.767]
bn_sds = [0.064, 0.024]
ln_means = [0.773, 0.802]
ln_sds = [0.027, 0.024]

ax2.errorbar(x_flow, bn_means, yerr=bn_sds, fmt='o-', color='#4878CF',
             linewidth=2.0, markersize=7, capsize=4, capthick=1.2,
             label='BatchNorm', zorder=3)
ax2.errorbar(x_flow, ln_means, yerr=ln_sds, fmt='s--', color='#E8833A',
             linewidth=2.0, markersize=7, capsize=4, capthick=1.2,
             label='LayerNorm', zorder=3)

ax2.axhline(y=vanilla_mean, color='#888888', linestyle=':', linewidth=1.2,
            label=f'Vanilla ({vanilla_mean:.3f})', zorder=1)

ax2.set_xticks(x_flow)
ax2.set_xticklabels(x_labels)
ax2.set_ylabel('Collision Avoidance Rate (CAR)')
ax2.set_ylim(0.62, 0.86)
ax2.yaxis.set_major_locator(mticker.MultipleLocator(0.04))
ax2.yaxis.set_minor_locator(mticker.MultipleLocator(0.02))
ax2.set_xlim(-0.3, 1.3)
ax2.legend(loc='lower right', framealpha=0.9, edgecolor='#cccccc')
ax2.set_title('(b)', fontweight='bold', loc='left', pad=4)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

ax2.annotate('', xy=(0.5, bn_means[0] + 0.003), xytext=(0.5, ln_means[0] - 0.003),
             arrowprops=dict(arrowstyle='<->', color='#666666', lw=1.0))
ax2.text(0.65, (bn_means[0] + ln_means[0])/2, '4.8pp',
         fontsize=7.5, color='#666666', va='center')

ax2.annotate('', xy=(0.5, bn_means[1] + 0.003), xytext=(0.5, ln_means[1] - 0.003),
             arrowprops=dict(arrowstyle='<->', color='#666666', lw=1.0))
ax2.text(0.65, (bn_means[1] + ln_means[1])/2, '3.5pp',
         fontsize=7.5, color='#666666', va='center')

fig.savefig('fig_car_factorial_combined.pdf', format='pdf')
fig.savefig('fig_car_factorial_combined.png', format='png', dpi=200)
print('Saved fig_car_factorial_combined.pdf and .png')
plt.close()
