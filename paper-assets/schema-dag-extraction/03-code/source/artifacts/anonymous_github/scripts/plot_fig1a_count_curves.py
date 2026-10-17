import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

ARTIFACTS = Path("./artifacts")
OUT_DIR = Path("./figures/paper")

# Load summaries
with open(ARTIFACTS / "d051_fewrel_n25_s42" / "count_curve_summary.json") as f:
    fewrel_data = json.load(f)
with open(ARTIFACTS / "d051_fewnerd_n25_s42" / "count_curve_summary.json") as f:
    fewnerd_data = json.load(f)

# Parse FewRel
fewrel_counts = sorted([int(k.split("_")[1]) for k in fewrel_data.keys()])
fewrel_mean = [fewrel_data[f"count_{c}"]["mean_accuracy"] for c in fewrel_counts]
fewrel_std = [fewrel_data[f"count_{c}"]["std_accuracy"] for c in fewrel_counts]
fewrel_full = fewrel_counts[-1]  # 80

# Parse Few-NERD
fewnerd_counts = sorted([int(k.split("_")[1]) for k in fewnerd_data.keys()])
fewnerd_mean = [fewnerd_data[f"count_{c}"]["mean_recall"] for c in fewnerd_counts]
fewnerd_std = [fewnerd_data[f"count_{c}"]["std_recall"] for c in fewnerd_counts]
fewnerd_full = fewnerd_counts[-1]  # 66

# --- Plot ---
plt.rcParams.update({
    'font.size': 8,
    'font.family': 'serif',
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'lines.linewidth': 1.2,
    'lines.markersize': 5,
})

fig, ax = plt.subplots(figsize=(3.3, 2.4))

# Colors
c_rel = '#2166AC'   # blue
c_ner = '#D6604D'   # red/orange

# FewRel: filled circles for subsets, open circle for full schema
rel_sub_idx = [i for i, c in enumerate(fewrel_counts) if c != fewrel_full]
rel_full_idx = [i for i, c in enumerate(fewrel_counts) if c == fewrel_full]

ax.errorbar(
    [fewrel_counts[i] for i in rel_sub_idx],
    [fewrel_mean[i] for i in rel_sub_idx],
    yerr=[fewrel_std[i] for i in rel_sub_idx],
    fmt='o-', color=c_rel, markerfacecolor=c_rel, markeredgecolor=c_rel,
    capsize=2, capthick=0.8, elinewidth=0.8,
    label='FewRel (RE accuracy)', zorder=3
)
# Full schema point (open marker, no error bar)
ax.plot(
    [fewrel_counts[i] for i in rel_full_idx],
    [fewrel_mean[i] for i in rel_full_idx],
    'o', color=c_rel, markerfacecolor='white', markeredgecolor=c_rel,
    markeredgewidth=1.2, markersize=6, zorder=4
)

# Few-NERD: filled triangles for subsets, open triangle for full schema
ner_sub_idx = [i for i, c in enumerate(fewnerd_counts) if c != fewnerd_full]
ner_full_idx = [i for i, c in enumerate(fewnerd_counts) if c == fewnerd_full]

ax.errorbar(
    [fewnerd_counts[i] for i in ner_sub_idx],
    [fewnerd_mean[i] for i in ner_sub_idx],
    yerr=[fewnerd_std[i] for i in ner_sub_idx],
    fmt='^-', color=c_ner, markerfacecolor=c_ner, markeredgecolor=c_ner,
    capsize=2, capthick=0.8, elinewidth=0.8,
    label='Few-NERD (NER recall)', zorder=3
)
# Full schema point (open triangle, no error bar)
ax.plot(
    [fewnerd_counts[i] for i in ner_full_idx],
    [fewnerd_mean[i] for i in ner_full_idx],
    '^', color=c_ner, markerfacecolor='white', markeredgecolor=c_ner,
    markeredgewidth=1.2, markersize=6, zorder=4
)

# Annotate Few-NERD minimum (count_22)
min_idx = fewnerd_counts.index(22)
min_val = fewnerd_mean[min_idx]
ax.annotate(
    f'{min_val:.3f}',
    xy=(22, min_val),
    xytext=(28, min_val - 0.06),
    fontsize=7,
    color=c_ner,
    arrowprops=dict(arrowstyle='-', color=c_ner, lw=0.6),
)

# Axes
ax.set_xlabel('Number of schema types', fontsize=8)
ax.set_ylabel('Performance', fontsize=8)
ax.set_ylim(0.15, 1.0)
ax.set_xlim(0, 85)

# Legend with full-schema markers explained
from matplotlib.lines import Line2D
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
print(f"Saved to {OUT_DIR / 'fig_count_curves.pdf'}")
print(f"Saved to {OUT_DIR / 'fig_count_curves.png'}")

# Print data summary
print("\n--- Data Summary ---")
print("FewRel (accuracy):")
for c, m, s in zip(fewrel_counts, fewrel_mean, fewrel_std):
    full_tag = " [FULL]" if c == fewrel_full else ""
    print(f"  count_{c}: {m:.4f} ± {s:.4f}{full_tag}")
print("Few-NERD (recall):")
for c, m, s in zip(fewnerd_counts, fewnerd_mean, fewnerd_std):
    full_tag = " [FULL]" if c == fewnerd_full else ""
    print(f"  count_{c}: {m:.4f} ± {s:.4f}{full_tag}")
