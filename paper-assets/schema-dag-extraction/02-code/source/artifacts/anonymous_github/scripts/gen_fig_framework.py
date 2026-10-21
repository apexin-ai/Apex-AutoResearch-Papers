"""Generate Figure A: Experimental Design Overview — Count × BCS scatter."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "figures" / "paper"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DATA_PATH = ROOT / "results" / "d051_fewrel_n25_s42" / "eval_results.json"

with open(DATA_PATH) as f:
    raw = json.load(f)

counts = []
bcs_vals = []
acc_vals = []
for rec in raw.values():
    counts.append(rec["num_types"])
    bcs_vals.append(rec["bcs"])
    acc_vals.append(rec["accuracy"])

counts = np.array(counts)
bcs_vals = np.array(bcs_vals)
acc_vals = np.array(acc_vals)

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

OI_BLUE = '#0072B2'
OI_ORANGE = '#D55E00'

fig, ax = plt.subplots(figsize=(3.25, 2.8))

norm = mcolors.Normalize(vmin=acc_vals.min(), vmax=acc_vals.max())
cmap = plt.cm.RdYlGn

sc = ax.scatter(
    counts, bcs_vals,
    c=acc_vals, cmap=cmap, norm=norm,
    s=22, alpha=0.7, edgecolors='white', linewidths=0.3,
    zorder=3,
)

ax.set_xscale('log', base=2)
tick_vals = [4, 8, 16, 32, 64, 80]
ax.set_xticks(tick_vals)
ax.set_xticklabels([str(v) for v in tick_vals])
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())

ax.set_xlabel('Number of Schema Types')
ax.set_ylabel('Batch Confusability Score (BCS)')

ax.set_xlim(3, 110)
ax.set_ylim(0.39, 0.69)

# --- Dimension 1 arrow: horizontal (count effect) ---
arrow_y = 0.655
ax.annotate(
    '', xy=(72, arrow_y), xytext=(5, arrow_y),
    arrowprops=dict(
        arrowstyle='->', color=OI_BLUE, lw=1.5,
        alpha=0.6, shrinkA=0, shrinkB=0,
    ),
    zorder=2,
)
ax.text(
    18, arrow_y + 0.008, 'Dimension 1: Type Count (§4.1)',
    fontsize=7, color=OI_BLUE, fontweight='semibold',
    ha='center', va='bottom',
    bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85),
    zorder=4,
)

# --- Dimension 2 arrow: vertical (BCS effect) ---
arrow_x = 4.7
ax.annotate(
    '', xy=(arrow_x, 0.645), xytext=(arrow_x, 0.43),
    arrowprops=dict(
        arrowstyle='->', color=OI_ORANGE, lw=1.5,
        alpha=0.6, shrinkA=0, shrinkB=0,
    ),
    zorder=2,
)
ax.text(
    arrow_x * 1.25, 0.535, 'Dim 2:\nConfusability\n(§4.3)',
    fontsize=6.5, color=OI_ORANGE, fontweight='semibold',
    ha='left', va='center',
    bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85),
    zorder=4,
)

# --- BCS range narrows annotation ---
# Draw dashed lines connecting BCS range at count=4 vs count=80
for c in [4, 80]:
    mask = counts == c
    bcs_lo, bcs_hi = bcs_vals[mask].min(), bcs_vals[mask].max()
    ax.plot([c, c], [bcs_lo - 0.005, bcs_hi + 0.005],
            color='#888888', ls='--', lw=0.7, alpha=0.5, zorder=1)

ax.annotate(
    'BCS range\nnarrows',
    xy=(56, 0.558), xytext=(42, 0.44),
    fontsize=6, color='#666666', fontstyle='italic',
    ha='center', va='top',
    arrowprops=dict(arrowstyle='->', color='#999999', lw=0.7, alpha=0.6),
    bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='#cccccc', alpha=0.8, lw=0.4),
    zorder=4,
)

# --- Colorbar ---
cbar = fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('RE Accuracy', fontsize=8)
cbar.ax.tick_params(labelsize=7)
cbar.outline.set_linewidth(0.4)

fig.savefig(OUT_DIR / "fig_framework.pdf")
fig.savefig(OUT_DIR / "fig_framework.png")
plt.close(fig)
print(f"Saved to {OUT_DIR / 'fig_framework.pdf'}")
print(f"Saved to {OUT_DIR / 'fig_framework.png'}")
