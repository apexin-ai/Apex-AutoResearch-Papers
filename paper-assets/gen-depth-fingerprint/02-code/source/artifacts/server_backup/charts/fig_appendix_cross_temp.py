import json
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_PATH = os.path.join(ROOT, "results", "cross_temp_transfer.json")
OUT_DIR = os.path.join(ROOT, "chart")

with open(RESULTS_PATH) as f:
    data = json.load(f)

res = data["results"]
conditions = ["0.7_to_0.7", "0.7_to_1.0", "1.0_to_1.0", "1.0_to_0.7"]
cond_labels = [
    "T=0.7→0.7\n(matched)",
    "T=0.7→1.0\n(transfer)",
    "T=1.0→1.0\n(matched)",
    "T=1.0→0.7\n(transfer)",
]

three_f1 = [res[c]["three_class_f1"] for c in conditions]
bin_f1 = [res[c]["binary_f1"] for c in conditions]

generators = ["olmo-2-1b", "pythia-1b", "pythia-2.8b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
gen_labels = ["OLMo-2-1B", "Pythia-1B", "Pythia-2.8B", "Qwen3-0.6B", "Qwen3-1.7B", "Qwen3-8B"]
heatmap_labels = ["0.7→0.7", "0.7→1.0", "1.0→1.0", "1.0→0.7"]

heatmap_data = np.array([
    [res[c]["per_generator_3class"][g] for c in conditions]
    for g in generators
])

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    "font.family": "serif",
    "font.size": 7,
    "axes.labelsize": 7,
    "axes.titlesize": 8,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "legend.fontsize": 6,
})

fig = plt.figure(figsize=(3.25, 4.8))
gs = fig.add_gridspec(2, 1, height_ratios=[1, 1.0], hspace=0.45)
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

# --- (a) Bar chart ---
x = np.arange(len(conditions))
w = 0.32
bars_3 = ax1.bar(x - w/2, three_f1, w, label="3-class F1", color="#1976D2", zorder=3)
bars_b = ax1.bar(x + w/2, bin_f1, w, label="Binary F1", color="#E65100", zorder=3)

for bar, val in zip(bars_3, three_f1):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.008,
             f"{val:.3f}", ha="center", va="bottom", fontsize=5, color="#1976D2")
for bar, val in zip(bars_b, bin_f1):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.008,
             f"{val:.3f}", ha="center", va="bottom", fontsize=5, color="#E65100")

ax1.set_ylim(0.6, 1.03)
ax1.set_ylabel("Macro F1")
ax1.set_xticks(x)
ax1.set_xticklabels(cond_labels, fontsize=5.5)
ax1.set_xlabel("Train → Test Temperature", fontsize=6.5)
ax1.legend(loc="lower left", framealpha=0.85, edgecolor="0.7", fontsize=5.5)
ax1.set_title("(a) Cross-Temperature Transfer", fontweight="bold", fontsize=8)
ax1.grid(axis="y", alpha=0.25, zorder=0)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# --- (b) Heatmap ---
cmap = mcolors.LinearSegmentedColormap.from_list(
    "custom_rdgn", ["#C62828", "#FFEE58", "#2E7D32"], N=256
)
im = ax2.imshow(heatmap_data, cmap=cmap, aspect="auto", vmin=0.4, vmax=0.9)

for i in range(len(generators)):
    for j in range(len(conditions)):
        val = heatmap_data[i, j]
        color = "white" if val < 0.5 else "black"
        ax2.text(j, i, f"{val:.3f}", ha="center", va="center", fontsize=5.5,
                 fontweight="bold" if val < 0.5 else "normal", color=color)

ax2.set_xticks(np.arange(len(conditions)))
ax2.set_xticklabels(heatmap_labels, fontsize=6)
ax2.set_yticks(np.arange(len(generators)))
ax2.set_yticklabels(gen_labels, fontsize=6)
ax2.set_xlabel("Train → Test", fontsize=6.5)
ax2.set_title("(b) Per-Generator 3-Class F1", fontweight="bold", fontsize=8)

cbar = fig.colorbar(im, ax=ax2, fraction=0.046, pad=0.04, shrink=0.95)
cbar.set_label("3-class F1", fontsize=6)
cbar.ax.tick_params(labelsize=5.5)

os.makedirs(OUT_DIR, exist_ok=True)
out_pdf = os.path.join(OUT_DIR, "fig_appendix_cross_temp.pdf")
out_png = os.path.join(OUT_DIR, "fig_appendix_cross_temp.png")
fig.savefig(out_pdf, bbox_inches="tight", dpi=300)
fig.savefig(out_png, bbox_inches="tight", dpi=300)
print(f"Saved: {out_pdf}")
print(f"Saved: {out_png}")
plt.close()
