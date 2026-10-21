"""Generate Figure 2: Dual-panel OVB Mechanism + Empirical Validation (EMNLP 2026).

Hybrid approach:
  Panel (a): cropped from PaperBanana output (AI-generated concept diagram)
  Panel (b): matplotlib scatter plot with real CSV data
"""
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy import stats
from PIL import Image

OUT_DIR = "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper"
DATA_PATH = f"{OUT_DIR}/fig2_permodel_data.csv"
PAPERBANANA_IMG = f"{OUT_DIR}/run_20260524_162151_ac71d4/final_output.png"

NAVY = '#2C3E50'
CORAL = '#E74C3C'
BLUE = '#2980B9'
GRAY = '#7F8C8D'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Times'],
    'mathtext.fontset': 'cm',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})


def get_panel_a_image():
    """Crop Panel (a) from PaperBanana output."""
    img = Image.open(PAPERBANANA_IMG)
    w, h = img.size
    # Panel (a) is roughly the left 48% of the image
    crop_x = int(w * 0.48)
    panel_a = img.crop((0, 0, crop_x, h))
    return np.array(panel_a)


def draw_panel_b(ax):
    with open(DATA_PATH) as f:
        rows = list(csv.DictReader(f))
    x = np.array([float(r['c_true']) for r in rows])
    y = np.array([float(r['bias']) for r in rows])
    r_val, p_val = stats.pearsonr(x, y)

    ax.axhspan(0, 1.2, color='#FDF1E2', alpha=0.40, zorder=0)
    ax.axhspan(-0.7, 0, color='#E6F2F7', alpha=0.40, zorder=0)
    ax.axhline(0, color=GRAY, ls='--', lw=0.6, alpha=0.5, zorder=1)

    pos = y >= 0
    ax.scatter(x[~pos], y[~pos], c=BLUE, s=14, alpha=0.35,
               edgecolors='none', zorder=3, rasterized=True)
    ax.scatter(x[pos], y[pos], c=CORAL, s=14, alpha=0.35,
               edgecolors='none', zorder=3, rasterized=True)

    slope, intercept, _, _, _ = stats.linregress(x, y)
    xl = np.linspace(-0.15, 5.1, 200)
    yl = slope * xl + intercept
    n = len(x)
    se_y = np.sqrt(np.sum((y - (slope * x + intercept)) ** 2) / (n - 2))
    se_l = se_y * np.sqrt(1 / n + (xl - x.mean()) ** 2 / np.sum((x - x.mean()) ** 2))
    tc = stats.t.ppf(0.975, n - 2)

    ax.plot(xl, yl, color=NAVY, lw=1.5, zorder=5)
    ax.fill_between(xl, yl - tc * se_l, yl + tc * se_l,
                    color=NAVY, alpha=0.12, zorder=2)

    ax.text(0.04, 0.04, f"$r = {r_val:.2f}$, $p < 0.001$",
            transform=ax.transAxes, fontsize=9.5,
            bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.9,
                      ec='#CCC', lw=0.5))

    ax.annotate('contaminated models\nsystematically overestimated',
                xy=(4.2, 0.65), xytext=(2.0, 0.95),
                fontsize=8, color=CORAL, style='italic', ha='center', va='bottom',
                arrowprops=dict(arrowstyle='->', color=CORAL, lw=0.8,
                                connectionstyle='arc3,rad=-0.2'),
                bbox=dict(boxstyle='round,pad=0.25', fc='white',
                          ec=CORAL, alpha=0.9, lw=0.5))

    ax.text(0.97, 0.14, "Synthetic ($N$=50, $I$=100,\n$J$=8, 20 seeds)",
            transform=ax.transAxes, fontsize=7, color='#999', ha='right')

    ax.set_xlabel(r"True contamination susceptibility $c_n$", fontsize=11)
    ax.set_ylabel(r"Sequential $\hat{\theta}$ bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$)",
                  fontsize=11)
    ax.set_xlim(-0.15, 5.1)
    ax.set_ylim(-0.65, 1.1)
    ax.tick_params(labelsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.text(-0.02, 1.04, '(b)', fontsize=14, fontweight='bold',
            transform=ax.transAxes)
    ax.text(0.06, 1.04, 'Empirical Validation', fontsize=12.5, fontweight='bold',
            transform=ax.transAxes)


# Load Panel (a) image
panel_a_img = get_panel_a_image()
pa_h, pa_w = panel_a_img.shape[:2]

fig = plt.figure(figsize=(14, 5.5))
gs = GridSpec(1, 2, width_ratios=[0.45, 0.55], wspace=0.04, figure=fig)

# Panel (a): image
ax_a = fig.add_subplot(gs[0])
ax_a.imshow(panel_a_img)
ax_a.axis('off')

# Panel (b): scatter
ax_b = fig.add_subplot(gs[1])
draw_panel_b(ax_b)

fig.savefig(f"{OUT_DIR}/fig2_ovb_bias_v2.png", bbox_inches='tight', dpi=300)
fig.savefig(f"{OUT_DIR}/fig2_ovb_bias_v2.pdf", bbox_inches='tight', dpi=300)
plt.close(fig)
print("Done")
