"""Generate Figure 6: Optimizer stability ratio bar chart (Muon vs AdamW)."""
import sys
sys.path.insert(0, '/root/spectral_optim_vision_geometry')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from plot_style import COLORS, apply_style
apply_style()

plt.rcParams.update({
    'font.family': 'serif',
    'savefig.pad_inches': 0.05,
})

OUT_DIR = "/root/spectral_optim_vision_geometry/paper/figures"

# Data from Table 1: σ(AdamW) / σ(Muon) = stability ratio
# ratio > 1 means Muon more stable, ratio < 1 means AdamW more stable
settings = [
    'C100\nResNet-50', 'C100\nDeiT-S', 'C100\nConvNeXt-T',
    'TIN\nResNet-50', 'TIN\nDeiT-S', 'TIN\nConvNeXt-T',
    'IN100\nResNet-50', 'IN100\nDeiT-S', 'IN100\nConvNeXt-T',
]

# σ values from paper Table 1
sigma_muon =  [0.27, 0.41, 0.15, 0.32, 0.21, 0.19, 0.25, 0.38, 0.21]
sigma_adamw = [0.17, 0.34, 2.17, 0.45, 0.42, 0.29, 0.76, 0.10, 1.51]

ratios = [sa / sm for sa, sm in zip(sigma_adamw, sigma_muon)]

# Colors: Muon-favorable (ratio>1) in Muon blue, AdamW-favorable (ratio<1) in AdamW orange
bar_colors = [COLORS['Muon'] if r >= 1.0 else COLORS['AdamW'] for r in ratios]

# --- Broken axis for the extreme 14.5x bar ---
fig, (ax_top, ax_bot) = plt.subplots(
    2, 1, sharex=True, figsize=(6.5, 3.5),
    gridspec_kw={'height_ratios': [1, 3], 'hspace': 0.08}
)

x = np.arange(len(settings))

# Clip ratios for bottom axis (show up to 4.5)
BREAK_LOW = 4.0
BREAK_HIGH = 13.0

for ax in [ax_top, ax_bot]:
    bars = ax.bar(x, ratios, width=0.6, color=bar_colors, edgecolor='white', linewidth=0.5, zorder=3)
    ax.axhline(1.0, color='#333333', linestyle='--', linewidth=1.5, zorder=2)
    ax.grid(axis='y', alpha=0.25, linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Bottom axis: 0 to BREAK_LOW
ax_bot.set_ylim(0, BREAK_LOW)
ax_bot.spines['top'].set_visible(False)

# Top axis: BREAK_HIGH to max+1
ax_top.set_ylim(BREAK_HIGH, 16.0)
ax_top.spines['bottom'].set_visible(False)
ax_top.tick_params(bottom=False)

# Draw broken axis markers
d = 0.012
kwargs = dict(transform=ax_top.transAxes, color='k', clip_on=False, linewidth=1)
ax_top.plot((-d, +d), (0-d, 0+d), **kwargs)
ax_top.plot((1-d, 1+d), (0-d, 0+d), **kwargs)

kwargs.update(transform=ax_bot.transAxes)
ax_bot.plot((-d, +d), (1-d, 1+d), **kwargs)
ax_bot.plot((1-d, 1+d), (1-d, 1+d), **kwargs)

# "equal stability" label next to baseline
ax_bot.text(len(settings) - 0.5, 1.12, 'equal stability', fontsize=7.5,
            ha='right', va='bottom', color='#333333', style='italic')

# Annotate bars
for i, r in enumerate(ratios):
    if r >= 1.0:
        if r > BREAK_HIGH:
            # Annotate on top axis
            ax_top.text(i, r + 0.3, f'{r:.1f}×', ha='center', va='bottom',
                       fontsize=7.5, fontweight='bold', color=COLORS['Muon'])
        elif r > BREAK_LOW:
            pass  # In the break zone (shouldn't happen with our data)
        else:
            ax_bot.text(i, r + 0.12, f'{r:.1f}×', ha='center', va='bottom',
                       fontsize=7.5, fontweight='bold', color=COLORS['Muon'])
    else:
        # ratio < 1: annotate outside bar, below
        ax_bot.text(i, r - 0.18, f'{r:.2f}×', ha='center', va='top',
                   fontsize=7.5, fontweight='bold', color=COLORS['AdamW'])

# Axis labels
ax_bot.set_xticks(x)
ax_bot.set_xticklabels(settings, fontsize=7.5)
ax_bot.set_ylabel('Stability ratio (higher = Muon more stable)', fontsize=10)
ax_bot.yaxis.set_label_coords(-0.08, 0.7)  # Shift label to cover both axes

# Top axis: minimal ticks
ax_top.set_yticks([14, 15])

# Legend
legend_elements = [
    mpatches.Patch(facecolor=COLORS['Muon'], edgecolor='white', label='Muon more stable (ratio > 1)'),
    mpatches.Patch(facecolor=COLORS['AdamW'], edgecolor='white', label='AdamW more stable (ratio < 1)'),
]
ax_top.legend(handles=legend_elements, fontsize=7.5, loc='upper left',
              framealpha=0.9, edgecolor='none')

plt.savefig(f'{OUT_DIR}/fig6_stability_ratio.pdf')
plt.savefig(f'{OUT_DIR}/fig6_stability_ratio.png')
plt.close(fig)
print(f'Figure 6 saved to {OUT_DIR}/fig6_stability_ratio.{{pdf,png}}')

# --- Grayscale verification ---
fig_g, (ax_top_g, ax_bot_g) = plt.subplots(
    2, 1, sharex=True, figsize=(6.5, 3.5),
    gridspec_kw={'height_ratios': [1, 3], 'hspace': 0.08}
)

gray_above = '#444444'
gray_below = '#AAAAAA'
hatch_above = None
hatch_below = '///'
bar_colors_g = [gray_above if r >= 1.0 else gray_below for r in ratios]
bar_hatches = [hatch_above if r >= 1.0 else hatch_below for r in ratios]

for ax_g in [ax_top_g, ax_bot_g]:
    for i, (r, c, h) in enumerate(zip(ratios, bar_colors_g, bar_hatches)):
        ax_g.bar(i, r, width=0.6, color=c, edgecolor='black', linewidth=0.5,
                hatch=h, zorder=3)
    ax_g.axhline(1.0, color='black', linestyle='--', linewidth=1.5, zorder=2)
    ax_g.grid(axis='y', alpha=0.25, linewidth=0.5, zorder=0)
    ax_g.set_axisbelow(True)
    ax_g.spines['top'].set_visible(False)
    ax_g.spines['right'].set_visible(False)

ax_bot_g.set_ylim(0, BREAK_LOW)
ax_bot_g.spines['top'].set_visible(False)
ax_top_g.set_ylim(BREAK_HIGH, 16.0)
ax_top_g.spines['bottom'].set_visible(False)
ax_top_g.tick_params(bottom=False)

kwargs = dict(transform=ax_top_g.transAxes, color='k', clip_on=False, linewidth=1)
ax_top_g.plot((-d, +d), (0-d, 0+d), **kwargs)
ax_top_g.plot((1-d, 1+d), (0-d, 0+d), **kwargs)
kwargs.update(transform=ax_bot_g.transAxes)
ax_bot_g.plot((-d, +d), (1-d, 1+d), **kwargs)
ax_bot_g.plot((1-d, 1+d), (1-d, 1+d), **kwargs)

ax_bot_g.text(len(settings) - 0.5, 1.12, 'equal stability', fontsize=7.5,
              ha='right', va='bottom', color='black', style='italic')

for i, r in enumerate(ratios):
    if r >= 1.0:
        if r > BREAK_HIGH:
            ax_top_g.text(i, r + 0.3, f'{r:.1f}×', ha='center', va='bottom',
                         fontsize=7.5, fontweight='bold')
        else:
            ax_bot_g.text(i, r + 0.12, f'{r:.1f}×', ha='center', va='bottom',
                         fontsize=7.5, fontweight='bold')
    else:
        ax_bot_g.text(i, r - 0.18, f'{r:.2f}×', ha='center', va='top',
                     fontsize=7.5, fontweight='bold')

ax_bot_g.set_xticks(x)
ax_bot_g.set_xticklabels(settings, fontsize=7.5)
ax_bot_g.set_ylabel('Stability ratio (higher = Muon more stable)', fontsize=10)
ax_bot_g.yaxis.set_label_coords(-0.08, 0.7)
ax_top_g.set_yticks([14, 15])

legend_g = [
    mpatches.Patch(facecolor=gray_above, edgecolor='black', label='Muon more stable'),
    mpatches.Patch(facecolor=gray_below, edgecolor='black', hatch='///', label='AdamW more stable'),
]
ax_top_g.legend(handles=legend_g, fontsize=7.5, loc='upper left',
                framealpha=0.9, edgecolor='none')

plt.savefig(f'{OUT_DIR}/fig6_stability_ratio_gray.png')
plt.close(fig_g)
print(f'Grayscale version saved to {OUT_DIR}/fig6_stability_ratio_gray.png')
