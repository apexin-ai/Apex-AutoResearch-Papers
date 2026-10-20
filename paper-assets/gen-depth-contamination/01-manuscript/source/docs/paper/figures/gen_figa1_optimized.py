#!/usr/bin/env python3
"""Figure A.1: Filtering strategies bar chart — appendix, column width.
Data from exp-006 (verified). Polish: better emphasis hierarchy, delta annotation."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import Patch

STRATEGIES = [
    ("No filter",               0.5867, 0.0021, "baseline"),
    ("DSIR",                    0.5867, 0.0019, "baseline"),
    ("Surprisal\nselection",    0.5894, 0.0018, "alternative"),
    ("Graduated\nweighting",    0.5892, 0.0022, "alternative"),
    (r"Binary $K^*$" + "\nfiltering", 0.5941, 0.0017, "ours"),
]

CAT_COLORS = {
    "baseline":    "#BBBBBB",
    "alternative": "#0072B2",
    "ours":        "#D55E00",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.linewidth": 0.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.03,
})

names = [s[0] for s in STRATEGIES]
scores = np.array([s[1] for s in STRATEGIES])
stds = np.array([s[2] for s in STRATEGIES])
cats = [s[3] for s in STRATEGIES]
colors = [CAT_COLORS[c] for c in cats]

fig, ax = plt.subplots(figsize=(3.4, 2.7))

x = np.arange(len(names))
bar_width = 0.56

bars = ax.bar(x, scores, bar_width, color=colors, edgecolor="white",
              linewidth=0.6, zorder=3)

ax.errorbar(x, scores, yerr=1.96 * stds, fmt="none", ecolor="#444444",
            elinewidth=0.7, capsize=2.5, capthick=0.7, zorder=4)

for i, (bar, score) in enumerate(zip(bars, scores)):
    fw = "bold" if cats[i] == "ours" else "normal"
    fs = 7 if cats[i] == "ours" else 6.5
    t = ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0006,
                f"{score:.4f}", ha="center", va="bottom", fontsize=fs, fontweight=fw)
    t.set_path_effects([pe.withStroke(linewidth=1.5, foreground="white")])

# Highlight best bar
best_idx = np.argmax(scores)
bars[best_idx].set_edgecolor("#D55E00")
bars[best_idx].set_linewidth(1.2)

# No-filter reference line
no_filter = scores[0]
ax.axhline(no_filter, color="#BBBBBB", ls="--", lw=0.6, zorder=1)
t_ref = ax.text(len(names) - 0.6, no_filter + 0.0002, "no-filter baseline",
                fontsize=5.5, color="#999999", ha="right", va="bottom")
t_ref.set_path_effects([pe.withStroke(linewidth=1.5, foreground="white")])

# Delta annotation: best vs baseline
delta = scores[best_idx] - no_filter
ax.annotate(f"+{delta*100:.1f}pp",
            xy=(best_idx, scores[best_idx] + 0.002),
            xytext=(best_idx - 1.2, scores[best_idx] + 0.003),
            fontsize=6.5, fontweight="bold", color="#C0392B",
            arrowprops=dict(arrowstyle="->", color="#C0392B", lw=0.7,
                            connectionstyle="arc3,rad=-0.2"))

y_min = min(scores) - 0.005
y_max = max(scores) + 0.006
ax.set_ylim(y_min, y_max)

ax.set_xticks(x)
ax.set_xticklabels(names, fontsize=7)
ax.set_ylabel("MMLU (5-shot)", fontsize=8.5)
ax.tick_params(direction="in", labelsize=7, length=2.5)

legend_elements = [
    Patch(facecolor="#BBBBBB", edgecolor="white", label="Baseline"),
    Patch(facecolor="#0072B2", edgecolor="white", label="Alternative"),
    Patch(facecolor="#D55E00", edgecolor="white", label="Ours"),
]
ax.legend(handles=legend_elements, fontsize=6, loc="upper left",
          framealpha=0.95, edgecolor="#DDDDDD", fancybox=True,
          borderpad=0.3, labelspacing=0.15, handletextpad=0.3)

plt.tight_layout(pad=0.3)

out = "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures"
fig.savefig(f"{out}/fig_filtering_strategies.pdf")
fig.savefig(f"{out}/fig_filtering_strategies.png")
plt.close(fig)
print("OK figa1")
