import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'text.usetex': False,
})

# Okabe-Ito colors
OI_GREEN = '#009E73'
OI_RED = '#D55E00'
OI_BLUE = '#0072B2'
OI_ORANGE = '#E69F00'
OI_GREY = '#999999'

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(6.5, 3.5),
                                  gridspec_kw={'width_ratios': [1, 1], 'wspace': 0.35})

# ============================================================
# Panel (a): 2x2 Annotated Heatmap — Effect of First-Differencing
# ============================================================

channels = ['canary→diversity', 'canary→perplexity']
conditions = ['Undifferenced', 'First-Differenced']

sig_rates = np.array([
    [24/24, 24/24],   # canary→diversity
    [6/8,   0/8],     # canary→perplexity
])

sig_labels = [
    ['24/24\nF = 74–3370',  '24/24\nF = 71–7643'],
    ['6/8\nF = 16–36',      '0/8\nF ≈ 0, p = 0.99'],
]

green_cmap = mcolors.LinearSegmentedColormap.from_list(
    'green_red', ['#FDEDEC', '#F5B7B1', '#ABEBC6', '#27AE60'], N=256)

custom_cmap = mcolors.LinearSegmentedColormap.from_list(
    'sig_cmap', [OI_RED, '#F5CBA7', '#A9DFBF', OI_GREEN], N=256)

im = ax_a.imshow(sig_rates, cmap=custom_cmap, vmin=0, vmax=1, aspect='auto')

for i in range(2):
    for j in range(2):
        rate = sig_rates[i, j]
        text_color = 'white' if rate > 0.7 or rate < 0.15 else 'black'
        fontweight = 'bold' if (i == 1 and j == 1) else 'normal'
        ax_a.text(j, i, sig_labels[i][j], ha='center', va='center',
                  fontsize=8, color=text_color, fontweight=fontweight,
                  linespacing=1.4)

ax_a.set_xticks([0, 1])
ax_a.set_xticklabels(conditions, fontsize=8)
ax_a.set_yticks([0, 1])
ax_a.set_yticklabels(channels, fontsize=8)
ax_a.set_title('(a) Differencing flips perplexity channel', fontsize=10, pad=8)

ax_a.spines['top'].set_visible(True)
ax_a.spines['right'].set_visible(True)
ax_a.spines['bottom'].set_visible(True)
ax_a.spines['left'].set_visible(True)
for spine in ax_a.spines.values():
    spine.set_color('#CCCCCC')
    spine.set_linewidth(0.5)

ax_a.tick_params(length=0)

# Highlight the bottom-right cell with a red border
from matplotlib.patches import Rectangle
rect = Rectangle((0.5, 0.5), 1, 1, linewidth=2.5, edgecolor=OI_RED,
                 facecolor='none', transform=ax_a.transData, clip_on=False)
ax_a.add_patch(rect)

# ============================================================
# Panel (b): Bar Chart — TY Granger d_max Sensitivity
# ============================================================

dmax_labels = ['$d_{max}$=0\n(permissive)', '$d_{max}$=adaptive\n(ADF-based)', '$d_{max}$=1\n(conservative)']
rejection_rates = [6.25, 75.0, 93.75]
bar_colors = [OI_ORANGE, OI_BLUE, OI_GREEN]

x_pos = np.arange(len(dmax_labels))
bars = ax_b.bar(x_pos, rejection_rates, width=0.55, color=bar_colors,
                edgecolor='white', linewidth=0.5, zorder=2)

for bar, rate in zip(bars, rejection_rates):
    ax_b.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
              f'{rate:.1f}%', ha='center', va='bottom', fontsize=8, fontweight='bold')

ax_b.axhline(100, color=OI_GREY, linestyle='--', linewidth=1.0, alpha=0.7, zorder=1)
ax_b.text(2.35, 101, 'naive baseline\n(16/16 sig)', fontsize=7, color=OI_GREY,
          ha='right', va='bottom', linespacing=1.3)

ax_b.set_xticks(x_pos)
ax_b.set_xticklabels(dmax_labels, fontsize=8)
ax_b.set_ylabel('Pairs rejected by TY (%)', fontsize=9)
ax_b.set_ylim(0, 115)
ax_b.set_title('(b) $d_{max}$ sensitivity of TY Granger', fontsize=10, pad=8)
ax_b.grid(axis='y', alpha=0.15, zorder=0)

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper'
plt.savefig(f'{outdir}/fig_differencing_dmax.pdf', format='pdf')
plt.savefig(f'{outdir}/fig_differencing_dmax.png', format='png', dpi=300)
plt.close()

print(f'Saved: {outdir}/fig_differencing_dmax.pdf')
print(f'Saved: {outdir}/fig_differencing_dmax.png')
