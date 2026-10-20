"""
Cliff Highlight — π₀.₅ Long: Scoring method determines cliff behavior.
Shows L2/Random/Attention SR across retention ratios, highlighting the
k=0.925 divergence as smoking-gun evidence for importance margin.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

OUT = Path(__file__).parent
BASELINE = 91.6

# 5-seed means (sample std, ddof=1). n=5 except baseline and k=0.925 (n=1).
k_all = np.array([1.0, 0.95, 0.925, 0.9, 0.85, 0.75, 0.7, 0.5])
l2     = np.array([BASELINE, 86.8, 83.2, 80.4, 78.1, 70.6, 63.2, 51.7])
l2_std = np.array([0.0,      0.8,  0.0,  0.5,  1.0,  2.7,  1.5,  1.5])
rand   = np.array([BASELINE, 61.2, 38.6, 33.6, 44.9, 63.0, 64.6, 50.4])
rand_std = np.array([0.0,    0.7,  0.0,  1.2,  1.3,  1.7,  1.8,  0.6])

k_attn = np.array([1.0, 0.95, 0.9, 0.85, 0.75, 0.7, 0.5])
attn   = np.array([BASELINE, 77.3, 64.2, 50.8, 51.4, 53.0, 49.4])
attn_std = np.array([0.0,    1.2,  1.0,  1.3,  1.2,  1.1,  1.5])

COL_L2   = '#0072B2'
COL_RAND = '#D55E00'
COL_ATTN = '#009E73'
COL_FILL = '#0072B2'

fig, ax = plt.subplots(figsize=(5.2, 3.6))

ax.axhline(BASELINE, color='#bbbbbb', linestyle=':', linewidth=0.8, zorder=0)
ax.text(0.505, BASELINE + 1.2, f'baseline {BASELINE}%',
        fontsize=7.5, color='#999999', va='bottom')

fill_mask = (k_all >= 0.85) & (k_all <= 0.95)
k_fill = k_all[fill_mask]
l2_fill = l2[fill_mask]
rand_fill = rand[fill_mask]
ax.fill_between(k_fill, rand_fill, l2_fill,
                color=COL_FILL, alpha=0.08, zorder=1)

ax.fill_between(k_all, l2 - l2_std, l2 + l2_std,
                color=COL_L2, alpha=0.10, zorder=2, linewidth=0)
ax.fill_between(k_all, rand - rand_std, rand + rand_std,
                color=COL_RAND, alpha=0.10, zorder=2, linewidth=0)
ax.fill_between(k_attn, attn - attn_std, attn + attn_std,
                color=COL_ATTN, alpha=0.10, zorder=2, linewidth=0)

ax.plot(k_all, l2, '-o', color=COL_L2, linewidth=2.0, markersize=5,
        markerfacecolor='white', markeredgewidth=1.5, zorder=4,
        label='L2 Norm ($n{=}5$)')
ax.plot(k_all, rand, '-s', color=COL_RAND, linewidth=2.0, markersize=5,
        markerfacecolor='white', markeredgewidth=1.5, zorder=4,
        label='Random ($n{=}5$)')
ax.plot(k_attn, attn, '--^', color=COL_ATTN, linewidth=1.5, markersize=5,
        markerfacecolor='white', markeredgewidth=1.5, zorder=4,
        label='Attention ($n{=}5$)')

hi_k = 0.9
hi_l2 = 80.4
hi_rand = 33.6
ax.plot(hi_k, hi_l2, 'o', color=COL_L2, markersize=8,
        markerfacecolor=COL_L2, markeredgecolor='white',
        markeredgewidth=1.5, zorder=5)
ax.plot(hi_k, hi_rand, 's', color=COL_RAND, markersize=8,
        markerfacecolor=COL_RAND, markeredgecolor='white',
        markeredgewidth=1.5, zorder=5)

mid_y = (hi_l2 + hi_rand) / 2
ax.annotate('',
            xy=(hi_k + 0.008, hi_rand + 1.5),
            xytext=(hi_k + 0.008, hi_l2 - 1.5),
            arrowprops=dict(arrowstyle='<->', color='#444444',
                            lw=1.2, shrinkA=0, shrinkB=0),
            zorder=6)
ax.text(hi_k + 0.022, mid_y, '46.8 pp\n(max, at valley)',
        fontsize=8, fontweight='bold', color='#333333',
        va='center', ha='left', zorder=6)

ax.annotate(f'L2: {hi_l2}%',
            xy=(hi_k, hi_l2), xytext=(hi_k - 0.06, hi_l2 + 5),
            fontsize=7.5, color=COL_L2, fontweight='semibold',
            arrowprops=dict(arrowstyle='->', color=COL_L2,
                            lw=0.8, connectionstyle='arc3,rad=-0.2'),
            zorder=6)
ax.annotate(f'Random: {hi_rand}%\n(valley)',
            xy=(hi_k, hi_rand), xytext=(hi_k - 0.06, hi_rand - 8),
            fontsize=7.5, color=COL_RAND, fontweight='semibold',
            arrowprops=dict(arrowstyle='->', color=COL_RAND,
                            lw=0.8, connectionstyle='arc3,rad=0.2'),
            zorder=6)

ax.axvspan(0.845, 0.955, color='#f5f0e0', alpha=0.35, zorder=0)
ax.text(0.90, 96, 'cliff zone', fontsize=7.5, color='#b08800',
        ha='center', fontstyle='italic', zorder=1)

ax.set_xlabel('Retention Ratio $k$', fontsize=10.5)
ax.set_ylabel('Success Rate (%)', fontsize=10.5)
ax.set_xlim(0.48, 1.02)
ax.set_ylim(20, 100)
ax.set_xticks([0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.925, 0.95, 1.0])
ax.set_xticklabels(['0.5', '0.6', '0.7', '0.8', '', '0.9', '', '0.95', '1.0'],
                    fontsize=8.5)
ax.set_yticks([20, 40, 60, 80, 100])
ax.tick_params(axis='both', which='major', labelsize=8.5)
ax.yaxis.set_minor_locator(plt.MultipleLocator(10))
ax.grid(axis='y', color='#eeeeee', linewidth=0.5, zorder=0)

legend = ax.legend(loc='lower left', fontsize=8.5, framealpha=0.9,
                   edgecolor='#dddddd', borderpad=0.5)
legend.get_frame().set_linewidth(0.5)

ax.set_title(r'$\pi_{0.5}$ Long — Scoring Method Determines Cliff Behavior',
             fontsize=11, fontweight='semibold', pad=10, color='#222222')

plt.tight_layout()
fig.savefig(OUT / 'fig_cliff_highlight.pdf', format='pdf')
fig.savefig(OUT / 'fig_cliff_highlight.png', format='png')
print(f"Saved: {OUT / 'fig_cliff_highlight.pdf'}")
print(f"Saved: {OUT / 'fig_cliff_highlight.png'}")
plt.close()
