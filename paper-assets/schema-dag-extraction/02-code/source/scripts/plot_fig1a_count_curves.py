"""Generate Figure 1a: count curves for FewRel and Few-NERD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "figures" / "paper"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Data from d051: 3 seeds (42, 123, 456) x 25 batches per seed
# Grand mean = mean of 3 seed means; std = mean of per-seed batch SDs
fewrel = {
    4:  {"mean": 0.8561, "std": 0.0874},
    8:  {"mean": 0.7965, "std": 0.0819},
    16: {"mean": 0.7186, "std": 0.0626},
    32: {"mean": 0.6482, "std": 0.0461},
    40: {"mean": 0.6080, "std": 0.0421},
    64: {"mean": 0.5367, "std": 0.0244},
    80: {"mean": 0.4955, "std": 0.0001},  # full schema
}

fewnerd = {
    2:  {"mean": 0.5085, "std": 0.1764},
    6:  {"mean": 0.4069, "std": 0.1230},
    12: {"mean": 0.3225, "std": 0.1062},
    22: {"mean": 0.2676, "std": 0.0952},
    44: {"mean": 0.2876, "std": 0.1209},
    66: {"mean": 0.4068, "std": 0.0016},  # full schema
}

FEWREL_FULL = 80
FEWNERD_FULL = 66

# Extract arrays
rel_counts = sorted(fewrel.keys())
rel_mean = [fewrel[c]["mean"] for c in rel_counts]
rel_std = [fewrel[c]["std"] for c in rel_counts]

ner_counts = sorted(fewnerd.keys())
ner_mean = [fewnerd[c]["mean"] for c in ner_counts]
ner_std = [fewnerd[c]["std"] for c in ner_counts]

# --- Plot ---
plt.rcParams.update({
    'font.size': 8,
    'font.family': 'DejaVu Sans',
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'lines.linewidth': 1.2,
    'lines.markersize': 5,
})

fig, ax = plt.subplots(figsize=(3.3, 2.4))

c_rel = '#3B6CB5'
c_ner = '#ED7D31'

# FewRel subset points (filled circles + error bars)
rel_sub = [(c, fewrel[c]) for c in rel_counts if c != FEWREL_FULL]
rel_sub_x = [c for c, _ in rel_sub]
rel_sub_y = [d["mean"] for _, d in rel_sub]
rel_sub_e = [d["std"] for _, d in rel_sub]

ax.errorbar(
    rel_sub_x, rel_sub_y, yerr=rel_sub_e,
    fmt='o-', color=c_rel, markerfacecolor=c_rel, markeredgecolor=c_rel,
    capsize=2, capthick=0.8, elinewidth=0.8,
    zorder=3
)

# FewRel full schema (open circle, no error bar)
ax.plot(
    [FEWREL_FULL], [fewrel[FEWREL_FULL]["mean"]],
    'o', color=c_rel, markerfacecolor='white', markeredgecolor=c_rel,
    markeredgewidth=1.2, markersize=6, zorder=4
)
# Connect last subset point to full schema point
ax.plot(
    [rel_sub_x[-1], FEWREL_FULL],
    [rel_sub_y[-1], fewrel[FEWREL_FULL]["mean"]],
    '-', color=c_rel, linewidth=1.2, zorder=2
)

# Few-NERD subset points (filled triangles + error bars)
ner_sub = [(c, fewnerd[c]) for c in ner_counts if c != FEWNERD_FULL]
ner_sub_x = [c for c, _ in ner_sub]
ner_sub_y = [d["mean"] for _, d in ner_sub]
ner_sub_e = [d["std"] for _, d in ner_sub]

ax.errorbar(
    ner_sub_x, ner_sub_y, yerr=ner_sub_e,
    fmt='^-', color=c_ner, markerfacecolor=c_ner, markeredgecolor=c_ner,
    capsize=2, capthick=0.8, elinewidth=0.8,
    zorder=3
)

# Few-NERD full schema (open triangle, no error bar)
ax.plot(
    [FEWNERD_FULL], [fewnerd[FEWNERD_FULL]["mean"]],
    '^', color=c_ner, markerfacecolor='white', markeredgecolor=c_ner,
    markeredgewidth=1.2, markersize=6, zorder=4
)
# Connect last subset point to full schema point
ax.plot(
    [ner_sub_x[-1], FEWNERD_FULL],
    [ner_sub_y[-1], fewnerd[FEWNERD_FULL]["mean"]],
    '-', color=c_ner, linewidth=1.2, zorder=2
)

# Annotate Few-NERD plateau region (counts 22-44)
plateau_val = min(fewnerd[22]["mean"], fewnerd[44]["mean"])
ax.annotate(
    '~0.27',
    xy=(33, plateau_val),
    xytext=(45, plateau_val - 0.08),
    fontsize=7, color=c_ner,
    arrowprops=dict(arrowstyle='->', color=c_ner, lw=0.6),
)

# Axes
ax.set_xlabel('Number of schema types', fontsize=8)
ax.set_ylabel('Performance', fontsize=8)
ax.set_ylim(0.12, 1.0)
ax.set_xlim(0, 85)

# Legend
legend_elements = [
    Line2D([0], [0], marker='o', color=c_rel, markerfacecolor=c_rel,
           markersize=5, linewidth=1.2, label='FewRel (RE accuracy)'),
    Line2D([0], [0], marker='^', color=c_ner, markerfacecolor=c_ner,
           markersize=5, linewidth=1.2, label='Few-NERD (NER recall)'),
    Line2D([0], [0], marker='o', color='gray', markerfacecolor='white',
           markeredgecolor='gray', markeredgewidth=1.2,
           markersize=6, linewidth=0, label='Full schema'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=7,
          framealpha=0.9, edgecolor='none')

ax.grid(True, alpha=0.3, linewidth=0.4)
ax.tick_params(labelsize=7)

plt.tight_layout(pad=0.3)
fig.savefig(OUT_DIR / "fig_count_curves.pdf", bbox_inches='tight', dpi=300)
fig.savefig(OUT_DIR / "fig_count_curves.png", bbox_inches='tight', dpi=200)
print(f"Saved: {OUT_DIR / 'fig_count_curves.pdf'}")
print(f"Saved: {OUT_DIR / 'fig_count_curves.png'}")
