"""Generate fig_bound: SC gain vs degeneracy bound (2-panel vertical)."""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib.lines import Line2D

OUT_DIR = Path(__file__).parent

with open(Path(__file__).resolve().parents[3] / "artifacts" / "p_impossibility" / "bound_verification.json") as f:
    data = json.load(f)

configs = data["per_config"]

ALPHA = 0.068
G_ND_REF = 14.8
EPSILON = 0.3
THETA_CRIT = 0.70

STYLE = {
    "FewNERD": {"color": "#3B7DD8", "marker": "o"},
    "SciERC":  {"color": "#E8930C", "marker": "^"},
    "CoNLL":   {"color": "#43A047", "marker": "s"},
}

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'dejavusans',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

MS = 55
EW = 0.6

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.4, 5.2),
                                gridspec_kw={"hspace": 0.55})
fig.patch.set_facecolor('white')

def style_ax(ax):
    ax.set_facecolor('white')
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('#CCCCCC')
        ax.spines[spine].set_linewidth(0.8)
    ax.tick_params(colors='#555555', which='both')
    ax.grid(True, alpha=0.15, linewidth=0.5, color='#888888')
    ax.set_axisbelow(True)

LEGEND_BOX = dict(frameon=True, facecolor='white', framealpha=0.92,
                  edgecolor='#CCCCCC')

# ===== Top panel: SC gain vs Degeneracy =====
style_ax(ax1)

for c in configs:
    s = STYLE[c["dataset"]]
    ax1.scatter(c["D"], c["actual_best_delta_pp"],
                color=s["color"], marker=s["marker"],
                s=MS, zorder=5, edgecolors="white",
                linewidths=EW, alpha=0.90)

D_range = np.linspace(0, 0.85, 200)
bound_curve = (1 - D_range) * G_ND_REF * ALPHA
ax1.plot(D_range, bound_curve, color="#CC3333", linewidth=1.6, zorder=4)

ax1.axvline(x=THETA_CRIT, color="0.50", linestyle="--", linewidth=0.8, zorder=3)
ax1.axhline(y=EPSILON, color="0.50", linestyle=":", linewidth=0.8, zorder=3)
ax1.axhline(y=0, color="0.65", linewidth=0.4, zorder=2)

ax1.set_xlabel(r"Degeneracy rate $D$")
ax1.set_ylabel(r"SC gain $\Delta F_1$ (pp)")
ax1.set_xlim(-0.02, 0.85)
ax1.set_ylim(-1.0, 2.1)
ax1.set_title("(a) All gains respect the bound", fontsize=9, pad=5,
              fontweight='medium', loc='left')

handles = [
    Line2D([0], [0], marker=STYLE[ds]['marker'], color='w',
           markerfacecolor=STYLE[ds]['color'], markeredgecolor='white',
           markeredgewidth=EW, markersize=6, label=ds)
    for ds in ["FewNERD", "SciERC", "CoNLL"]
] + [
    Line2D([0], [0], color='#CC3333', linewidth=1.4,
           label=fr'Bound ($\alpha$={ALPHA})'),
    Line2D([0], [0], color='0.50', linestyle='--', linewidth=0.8,
           label=fr'$\theta_{{\mathrm{{crit}}}}$={THETA_CRIT}'),
    Line2D([0], [0], color='0.50', linestyle=':', linewidth=0.8,
           label=fr'$\varepsilon$={EPSILON} pp'),
]
ax1.legend(handles=handles, loc="upper right",
           bbox_to_anchor=(0.99, 0.99),
           handletextpad=0.3, borderpad=0.4, labelspacing=0.25,
           columnspacing=0.7, fontsize=7, ncol=2, frameon=False)

# ===== Bottom panel: Ratio to weak bound =====
style_ax(ax2)

positive = [c for c in configs if c["actual_best_delta_pp"] > 0]
for c in positive:
    s = STYLE[c["dataset"]]
    ax2.scatter(c["D"], c["bound_ratio"],
                color=s["color"], marker=s["marker"],
                s=MS, zorder=5, edgecolors="white",
                linewidths=EW, alpha=0.90)

ax2.axhline(y=0.13, color="#CC3333", linestyle="--", linewidth=1.2, zorder=4)
ax2.axhline(y=0, color="0.65", linewidth=0.4, zorder=2)
ax2.text(0.02, 0.138, r'Empirical ceiling $\approx$ 0.13', fontsize=6.5,
         color='#CC3333', va='bottom', ha='left')

handles2 = [
    Line2D([0], [0], marker=STYLE[ds]['marker'], color='w',
           markerfacecolor=STYLE[ds]['color'], markeredgecolor='white',
           markeredgewidth=EW, markersize=6, label=ds)
    for ds in ["FewNERD", "SciERC", "CoNLL"]
]

ax2.set_xlabel(r"Degeneracy rate $D$")
ax2.set_ylabel("Ratio to weak bound")
ax2.set_xlim(-0.02, 0.85)
ax2.set_ylim(-0.005, 0.19)
ax2.set_title("(b) Low recovery ratio confirms bound looseness", fontsize=9,
              pad=5, fontweight='medium', loc='left')
ax2.legend(handles=handles2, loc="upper right",
           handletextpad=0.3, borderpad=0.4, labelspacing=0.25, fontsize=7,
           **LEGEND_BOX)

fig.savefig(OUT_DIR / "fig_bound.pdf")
fig.savefig(OUT_DIR / "fig_bound.png")
print("Saved fig_bound.pdf and fig_bound.png")
