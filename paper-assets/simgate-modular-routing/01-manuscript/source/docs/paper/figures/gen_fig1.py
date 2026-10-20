"""Generate Figure 1: DAF scatter plot for EMNLP short paper.

Per-task death rate differential vs performance gap (delta_full).
Data from plan-012-full: 11 ScienceWorld task types, 245 episodes.
"""
import paper_style; paper_style.apply_style()
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

tasks = [
    ("id-life-stages-1",   20, 47.50, 55, 10),
    ("lifespan-long",       25, 44.00, 56, 16),
    ("lifespan-l-then-s",   20, 40.80, 45, 10),
    ("inclined-plane",      20, 36.00, 55, 20),
    ("freeze",              20, 30.50, 55, 25),
    ("meas-melt-point",     20, 30.05, 55, 25),
    ("id-life-stages-2",    20, 30.00, 50, 20),
    ("find-animal",         20, 26.65, 50, 25),
    ("grow-fruit",          20, 25.10, 45, 20),
    ("chem-mix",            20, 21.80, 45, 25),
    ("find-non-living-thing", 40,  9.58,  0,  0),
]

names = [t[0] for t in tasks]
delta_full = np.array([t[2] for t in tasks])
death_diff = np.array([t[3] - t[4] for t in tasks])

is_special = np.array([t[0].startswith("find-non-living") for t in tasks])

slope, intercept, r, p, se = stats.linregress(death_diff, delta_full)

fig, ax = plt.subplots(figsize=(3.25, 2.6))

ax.scatter(death_diff[~is_special], delta_full[~is_special],
           c=paper_style.C_INTERNAL, s=45, zorder=4,
           edgecolors='white', linewidths=paper_style.MARKER_EDGE_WIDTH,
           alpha=0.92, label='Regular tasks',
           path_effects=paper_style.marker_shadow())
ax.scatter(death_diff[is_special], delta_full[is_special],
           c=paper_style.C_ACCENT, s=60, marker='D', zorder=4,
           edgecolors='white', linewidths=paper_style.MARKER_EDGE_WIDTH,
           alpha=0.92, label='Zero-death outlier',
           path_effects=paper_style.marker_shadow())

x_fit = np.linspace(-2, 48, 200)
y_fit = slope * x_fit + intercept
y_pred = slope * death_diff + intercept
residuals = delta_full - y_pred
se_fit = np.sqrt(np.sum(residuals**2) / (len(death_diff) - 2))
x_mean = np.mean(death_diff)
ss_x = np.sum((death_diff - x_mean)**2)
ci = 1.96 * se_fit * np.sqrt(1/len(death_diff) + (x_fit - x_mean)**2 / ss_x)

ax.fill_between(x_fit, y_fit - ci, y_fit + ci,
                color=paper_style.C_REGRESSION, alpha=paper_style.CI_ALPHA,
                zorder=1, edgecolor='none')
ax.plot(x_fit, y_fit, linestyle='-', color=paper_style.C_REGRESSION,
        linewidth=paper_style.REGRESSION_LW,
        alpha=paper_style.REGRESSION_ALPHA, zorder=2)

ax.text(0.03, 0.97, f'$r = {r:.4f}$\n$p = 8.12 \\times 10^{{-7}}$',
        transform=ax.transAxes, ha='left', va='top', fontsize=6.5,
        bbox=paper_style.annotation_box())

ax.annotate('find-non-living-thing\n(zero deaths)',
            xy=(death_diff[is_special][0], delta_full[is_special][0]),
            xytext=(45, -10), textcoords='offset points',
            fontsize=7, fontweight='medium',
            color=paper_style.C_ACCENT, fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='none', alpha=0.9),
            arrowprops=dict(arrowstyle='->', color=paper_style.C_ACCENT,
                            lw=1.2, connectionstyle='arc3,rad=-0.2'))

ax.set_xlabel('Death rate differential (int. $-$ det., pp)')
ax.set_ylabel('$\\Delta_{\\mathrm{full}}$ (points)')
ax.set_xlim(-3, 50)
ax.set_ylim(5, 52)

paper_style.add_y_grid(ax)

leg = ax.legend(fontsize=6, loc='upper left',
                bbox_to_anchor=(0.0, 0.78),
                frameon=True, handlelength=1.0, handletextpad=0.35,
                borderpad=0.35, labelspacing=0.3)
paper_style.style_legend(leg)

plt.tight_layout(pad=0.3)

out_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(out_dir, 'fig1_daf_scatter.pdf')
png_path = os.path.join(out_dir, 'fig1_daf_scatter.png')
fig.savefig(pdf_path, bbox_inches='tight', pad_inches=0.08)
fig.savefig(png_path, format='png', dpi=300, bbox_inches='tight', pad_inches=0.08)
plt.close()
print(f"Saved: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
print(f"Saved: {png_path} ({os.path.getsize(png_path)} bytes)")
