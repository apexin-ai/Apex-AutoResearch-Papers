"""
Importance Margin Profile — π₀.₅ Long: L2-Random margin vs retention ratio.
Shows the asymmetric peak at k=0.9 and crossover at k≈0.70.
Multi-seed means with error bars (sample std, ddof=1).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

# All ± values are sample std (ddof=1). All n=5.
# L2  n: k0.95=5, k0.9=5, k0.85=5, k0.75=5, k0.7=5, k0.5=5
# Rand n: k0.95=5, k0.9=5, k0.85=5, k0.75=5, k0.7=5, k0.5=5
k      = np.array([0.95,  0.90,  0.85,  0.75,  0.70,  0.50])
margin = np.array([25.6,  46.8,  33.2,   7.6,  -1.4,   1.3])

l2_err   = np.array([0.8, 0.5, 1.0, 2.7, 1.5, 1.5])
rand_err = np.array([0.7, 1.2, 1.3, 1.7, 1.8, 0.6])
margin_err = np.sqrt(l2_err**2 + rand_err**2)

COL_POS = '#0072B2'
COL_NEG = '#D55E00'

fig, ax = plt.subplots(figsize=(5.2, 3.2))

ax.axhline(0, color='#999999', linewidth=0.8, linestyle='-', zorder=1)

ax.fill_between(k, 0, margin, where=(margin >= 0),
                color=COL_POS, alpha=0.08, interpolate=True, zorder=1)
ax.fill_between(k, 0, margin, where=(margin < 0),
                color=COL_NEG, alpha=0.08, interpolate=True, zorder=1)

ax.errorbar(k, margin, yerr=margin_err,
            fmt='o-', color=COL_POS, linewidth=2.0, markersize=6,
            markerfacecolor='white', markeredgewidth=1.5,
            ecolor='#888888', elinewidth=1.0, capsize=3, capthick=1.0,
            zorder=4)

# Peak annotation at k=0.9
ax.plot(0.9, 46.8, 'o', color=COL_POS, markersize=9,
        markerfacecolor=COL_POS, markeredgecolor='white',
        markeredgewidth=1.5, zorder=5)
ax.annotate('46.8 pp\n(peak, at valley)',
            xy=(0.9, 46.0), xytext=(0.82, 42),
            fontsize=8, fontweight='bold', color='#333333',
            ha='center', va='top',
            arrowprops=dict(arrowstyle='->', color='#444444',
                            lw=0.8, connectionstyle='arc3,rad=-0.2'),
            zorder=6)

# Crossover annotation at k≈0.72
cross_k = 0.75 - 7.6 * (0.70 - 0.75) / (-1.1 - 7.6)
ax.plot(cross_k, 0, 'D', color=COL_NEG, markersize=7,
        markerfacecolor=COL_NEG, markeredgecolor='white',
        markeredgewidth=1.5, zorder=5)
ax.annotate(f'crossover\n$k \\approx {cross_k:.2f}$',
            xy=(cross_k, 0), xytext=(0.60, -6),
            fontsize=8, fontweight='semibold', color=COL_NEG,
            ha='center', va='top',
            arrowprops=dict(arrowstyle='->', color=COL_NEG,
                            lw=0.8, connectionstyle='arc3,rad=0.2'),
            zorder=6)

# Zone labels
ax.text(0.88, 15, 'L2 > Random', fontsize=7.5, color=COL_POS,
        ha='center', fontstyle='italic', alpha=0.7)
ax.text(0.58, -4, 'L2 ≈ Random', fontsize=7.5, color='#888888',
        ha='center', fontstyle='italic', alpha=0.7)


ax.set_xlabel('Retention Ratio $k$', fontsize=10.5)
ax.set_ylabel('Importance Margin (pp)\n(L2 $-$ Random SR)', fontsize=10)
ax.set_xlim(0.45, 1.0)
ax.set_ylim(-12, 55)
ax.set_xticks([0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
ax.set_xticklabels(['0.5', '0.6', '0.7', '0.75', '0.8', '0.85', '0.9', '0.95'],
                    fontsize=8.5)
ax.set_yticks([-10, 0, 10, 20, 30, 40, 50])
ax.tick_params(axis='both', which='major', labelsize=8.5)
ax.grid(axis='y', color='#eeeeee', linewidth=0.5, zorder=0)

ax.set_title(r'$\pi_{0.5}$ Long — Importance Margin Profile',
             fontsize=11, fontweight='semibold', pad=10, color='#222222')

plt.tight_layout()
fig.savefig(OUT / 'fig_margin_profile.pdf', format='pdf')
fig.savefig(OUT / 'fig_margin_profile.png', format='png')
print(f"Saved: {OUT / 'fig_margin_profile.pdf'}")
print(f"Saved: {OUT / 'fig_margin_profile.png'}")
plt.close()
