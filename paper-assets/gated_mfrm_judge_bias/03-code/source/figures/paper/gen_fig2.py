"""Generate Figure 2: OVB Bias Scatter Plot (optimized for EMNLP)."""
import sys
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from scipy import stats

DATA_PATH = sys.argv[1] if len(sys.argv) > 1 else "fig2_permodel_data.csv"
OUT_DIR = "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper"

COLORS = {
    'baseline': '#0072B2',
    'treatment': '#E69F00',
    'collapse': '#D55E00',
    'safe': '#009E73',
    'neutral': '#999999',
}

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Times'],
    'mathtext.fontset': 'cm',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
})

with open(DATA_PATH, 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

x_all = np.array([float(r['c_true']) for r in rows])
y_all = np.array([float(r['bias']) for r in rows])
r_all, p_all = stats.pearsonr(x_all, y_all)

fig, ax = plt.subplots(figsize=(3.3, 3.3))

# Background zones for narrative
ax.axhspan(0, 1.2, color='#FDF1E2', alpha=0.45, zorder=0)
ax.axhspan(-0.7, 0, color='#E6F2F7', alpha=0.45, zorder=0)


# Zero reference line
ax.axhline(0, color=COLORS['neutral'], linestyle='-', linewidth=0.6, alpha=0.4, zorder=1)

# Scatter: color by bias sign for semantic meaning
pos_mask = y_all >= 0
neg_mask = y_all < 0
ax.scatter(x_all[neg_mask], y_all[neg_mask], c=COLORS['baseline'],
           s=8, alpha=0.35, edgecolors='none', zorder=3, rasterized=True)
ax.scatter(x_all[pos_mask], y_all[pos_mask], c=COLORS['collapse'],
           s=8, alpha=0.35, edgecolors='none', zorder=3, rasterized=True)

# Regression line + 95% CI
slope, intercept, r_val, p_val, se = stats.linregress(x_all, y_all)
x_line = np.linspace(-0.15, 5.1, 200)
y_line = slope * x_line + intercept

n = len(x_all)
x_mean = x_all.mean()
se_y = np.sqrt(np.sum((y_all - (slope * x_all + intercept))**2) / (n - 2))
se_line = se_y * np.sqrt(1.0 / n + (x_line - x_mean)**2 / np.sum((x_all - x_mean)**2))
t_crit = stats.t.ppf(0.975, n - 2)

ax.plot(x_line, y_line, color='#2C3E50', linewidth=1.3, zorder=5)
ax.fill_between(x_line, y_line - t_crit * se_line, y_line + t_crit * se_line,
                color='#2C3E50', alpha=0.12, zorder=2)

# Correlation annotation (bottom-left, inside the blue zone)
p_str = r"$p < 0.001$" if p_all < 0.001 else f"$p = {p_all:.3f}$"
ann_text = f"$r = {r_all:.2f}$, {p_str}"
ax.text(0.04, 0.04, ann_text, transform=ax.transAxes, fontsize=7.5,
        va='bottom', ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.85,
                  edgecolor='#CCCCCC', linewidth=0.5))

# Data source (bottom-right, compact)
ax.text(0.97, 0.14, "Synthetic ($N$=50, $I$=100,\n$J$=8, 20 seeds)",
        transform=ax.transAxes, fontsize=6, color='#999999',
        va='bottom', ha='right')

# Key insight annotation with arrow pointing to high-bias region
ax.annotate('contaminated models\nsystematically overestimated',
            xy=(4.2, 0.65), xytext=(1.8, 0.92),
            fontsize=6.5, color=COLORS['collapse'],
            style='italic', ha='center', va='bottom',
            arrowprops=dict(arrowstyle='->', color=COLORS['collapse'],
                            lw=0.7, connectionstyle='arc3,rad=-0.2'),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor=COLORS['collapse'], alpha=0.85, linewidth=0.5))

ax.set_xlabel(r"True contamination susceptibility $c_n$", fontsize=9.5)
ax.set_ylabel(r"Sequential $\hat{\theta}$ bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$)",
              fontsize=9.5)
ax.set_xlim(-0.15, 5.1)
ax.set_ylim(-0.65, 1.1)
ax.tick_params(labelsize=8.5)

fig.tight_layout(pad=0.3)
fig.savefig(f"{OUT_DIR}/fig2_ovb_bias.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/fig2_ovb_bias.png", bbox_inches="tight", dpi=300)
plt.close(fig)
print(f"Saved fig2_ovb_bias")
