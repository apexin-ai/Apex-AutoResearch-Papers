#!/usr/bin/env python3
"""Figure 4: Cross-model transfer heatmap — two panels, column width.
Data from exp-013 (verified). Improved readability at column width."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
import numpy as np

MODELS = ["Qwen-rw", "Pythia", "OLMo", "Qwen-cont"]

ACC_MATRIX = np.array([
    [0.423, 0.259, 0.265, 0.347],
    [0.272, 0.386, 0.353, 0.329],
    [0.277, 0.345, 0.382, 0.324],
    [0.344, 0.328, 0.311, 0.388],
])

RETENTION = np.zeros_like(ACC_MATRIX)
for i in range(4):
    for j in range(4):
        RETENTION[i, j] = ACC_MATRIX[i, j] / ACC_MATRIX[i, i] * 100

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

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(6.8, 3.0),
                                  gridspec_kw={"wspace": 0.55})

# ═══════════════════════════════════════════════════════════════
# Panel (a): Ordinal Accuracy
# ═══════════════════════════════════════════════════════════════
cmap_a = plt.cm.Blues
norm_a = mcolors.Normalize(vmin=0.22, vmax=0.45)
im_a = ax_a.imshow(ACC_MATRIX, cmap=cmap_a, norm=norm_a, aspect="equal")

for i in range(4):
    for j in range(4):
        val = ACC_MATRIX[i, j]
        color = "white" if val > 0.36 else "#333333"
        weight = "bold" if i == j else "normal"
        t = ax_a.text(j, i, f".{int(val*1000):03d}", ha="center", va="center",
                      fontsize=9, color=color, fontweight=weight)
        if color == "white":
            t.set_path_effects([pe.withStroke(linewidth=0.5, foreground="#00000033")])

for i in range(4):
    rect = plt.Rectangle((i - 0.5, i - 0.5), 1, 1, linewidth=1.5,
                          edgecolor="#0072B2", facecolor="none", zorder=5)
    ax_a.add_patch(rect)

# Separator: rewrite vs continuation block
ax_a.axhline(0.5, color="#AAAAAA", ls="-", lw=0.6, xmin=0, xmax=1, zorder=6)
ax_a.axvline(0.5, color="#AAAAAA", ls="-", lw=0.6, ymin=0, ymax=1, zorder=6)

ax_a.set_xticks(range(4))
ax_a.set_xticklabels(MODELS, fontsize=7.5, rotation=20, ha="right")
ax_a.set_yticks(range(4))
ax_a.set_yticklabels(MODELS, fontsize=7.5)
ax_a.set_xlabel("Test Model", fontsize=8.5)
ax_a.set_ylabel("Train Model", fontsize=8.5)
ax_a.tick_params(direction="in", length=0)

cbar_a = fig.colorbar(im_a, ax=ax_a, shrink=0.82, pad=0.04, aspect=15)
cbar_a.set_label("Accuracy", fontsize=7.5)
cbar_a.ax.tick_params(labelsize=6.5)
cbar_a.outline.set_linewidth(0.3)
ax_a.set_title(r"$\mathbf{(a)}$ Ordinal Accuracy", fontsize=8.5, loc="left", pad=5)

# ═══════════════════════════════════════════════════════════════
# Panel (b): Transfer Retention
# ═══════════════════════════════════════════════════════════════
cmap_b = plt.cm.RdYlBu_r
norm_b = mcolors.TwoSlopeNorm(vmin=55, vcenter=80, vmax=100)
im_b = ax_b.imshow(RETENTION, cmap=cmap_b, norm=norm_b, aspect="equal")

for i in range(4):
    for j in range(4):
        val = RETENTION[i, j]
        color = "white" if val < 70 or val == 100 else "#333333"
        weight = "bold" if i == j else "normal"
        label = "100%" if i == j else f"{val:.0f}%"
        t = ax_b.text(j, i, label, ha="center", va="center",
                      fontsize=8.5, color=color, fontweight=weight)
        if color == "white":
            t.set_path_effects([pe.withStroke(linewidth=0.5, foreground="#00000033")])

for i in range(4):
    rect = plt.Rectangle((i - 0.5, i - 0.5), 1, 1, linewidth=1.5,
                          edgecolor="#0072B2", facecolor="none", zorder=5)
    ax_b.add_patch(rect)

# Separator
ax_b.axhline(0.5, color="#AAAAAA", ls="-", lw=0.6, xmin=0, xmax=1, zorder=6)
ax_b.axvline(0.5, color="#AAAAAA", ls="-", lw=0.6, ymin=0, ymax=1, zorder=6)

# Annotation: Qwen-rw poor transfer — bracket on first row
for j in [1, 2]:
    rect_ann = plt.Rectangle((j - 0.5, -0.5), 1, 1, linewidth=1.0,
                              edgecolor="#C0392B", facecolor="none",
                              linestyle="--", alpha=0.5, zorder=6)
    ax_b.add_patch(rect_ann)

ax_b.set_xticks(range(4))
ax_b.set_xticklabels(MODELS, fontsize=7.5, rotation=20, ha="right")
ax_b.set_yticks(range(4))
ax_b.set_yticklabels(MODELS, fontsize=7.5)
ax_b.set_xlabel("Test Model", fontsize=8.5)
ax_b.set_ylabel("Train Model", fontsize=8.5)
ax_b.tick_params(direction="in", length=0)

cbar_b = fig.colorbar(im_b, ax=ax_b, shrink=0.82, pad=0.04, aspect=15)
cbar_b.set_label("Retention (%)", fontsize=7.5)
cbar_b.ax.tick_params(labelsize=6.5)
cbar_b.outline.set_linewidth(0.3)
ax_b.set_title(r"$\mathbf{(b)}$ Transfer Retention", fontsize=8.5, loc="left", pad=5)

fig.subplots_adjust(left=0.08, right=0.95, top=0.90, bottom=0.15)

out = "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures"
fig.savefig(f"{out}/fig3_transfer_heatmap.pdf")
fig.savefig(f"{out}/fig3_transfer_heatmap.png")
plt.close(fig)
print("OK fig4")
