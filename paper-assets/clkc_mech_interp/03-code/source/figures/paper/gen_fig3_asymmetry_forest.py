"""
Forest plot: Cross-lingual transfer asymmetry (ZH→EN − EN→ZH)
comparing Conflict vs XNLI tasks across two models.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────
rows = [
    # label, point, ci_lo, ci_hi, task  (n=2000 bootstrap)
    ("Llama-3.1-8B (Conflict)", 7.27, 0.37, 13.97, "conflict"),
    ("Llama-3.1-8B (XNLI)",    5.97, 0.92, 11.33, "xnli"),
    ("Qwen3-8B (Conflict)",    7.23, -0.60, 13.69, "conflict"),
    ("Qwen3-8B (XNLI)",        6.72, 2.36, 11.73, "xnli"),
    ("Gemma-2-9B (Conflict)",   6.62, 1.90, 11.08, "conflict"),
    ("Gemma-2-9B (XNLI)",       7.81, 5.71,  9.99, "xnli"),
]

# ── Colors ────────────────────────────────────────────────────────────
COLOR_CONFLICT = "#D55E00"
COLOR_XNLI     = "#0072B2"

def task_color(task):
    return COLOR_CONFLICT if task == "conflict" else COLOR_XNLI

# ── Y positions (top-to-bottom: Llama pair, gap, Qwen pair, gap, Gemma)
#    matplotlib y-axis goes bottom-up, so we invert at the end
y_positions = [5.9, 5.1, 3.9, 3.1, 1.7, 0.9]   # Llama-c, Llama-x, Qwen-c, Qwen-x, Gemma-c, Gemma-x

# ── Figure ────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(7, 4.3))
gs = gridspec.GridSpec(1, 3, width_ratios=[2.2, 4, 2.2],
                       wspace=0.05, left=0.02, right=0.98,
                       top=0.88, bottom=0.18)

ax_labels = fig.add_subplot(gs[0, 0])
ax_ci     = fig.add_subplot(gs[0, 1])
ax_nums   = fig.add_subplot(gs[0, 2])

# ── Shared y-limits ───────────────────────────────────────────────────
y_lo, y_hi = -0.2, 6.6
for ax in [ax_labels, ax_ci, ax_nums]:
    ax.set_ylim(y_lo, y_hi)

# ── Left panel: row labels ───────────────────────────────────────────
ax_labels.set_xlim(0, 1)
ax_labels.axis("off")
for (label, _, _, _, task), y in zip(rows, y_positions):
    ax_labels.text(0.95, y, label, ha="right", va="center",
                   fontsize=10, fontfamily="DejaVu Sans",
                   color=task_color(task), fontweight="medium")

# Model group headers
for hdr, idx in [("Llama-3.1-8B", 0), ("Qwen3-8B", 2), ("Gemma-2-9B", 4)]:
    ax_labels.text(0.95, y_positions[idx] + 0.55, hdr,
                   ha="right", va="center", fontsize=10,
                   fontfamily="DejaVu Sans", fontweight="bold", color="#333333")

# ── Center panel: CI plot ────────────────────────────────────────────
ax_ci.set_xlim(-4, 16)

# Equivalence zone
ax_ci.axvspan(-2, 2, color="#cccccc", alpha=0.25, zorder=0)
ax_ci.text(0, y_hi - 0.25, "±2 pp", ha="center", va="top",
           fontsize=7.5, color="#888888", fontstyle="italic")

# Zero line
ax_ci.axvline(0, color="black", linewidth=0.8, linestyle="--", zorder=1)

# Light horizontal separators between model groups
sep_y1 = (y_positions[1] + y_positions[2]) / 2
sep_y2 = (y_positions[3] + y_positions[4]) / 2
for sep_y in [sep_y1, sep_y2]:
    ax_ci.axhline(sep_y, color="#dddddd", linewidth=0.8, zorder=0)
    ax_labels.axhline(sep_y, color="#dddddd", linewidth=0.8, zorder=0)
    ax_nums.axhline(sep_y, color="#dddddd", linewidth=0.8, zorder=0)

# Plot CIs and dots
for (label, pt, lo, hi, task), y in zip(rows, y_positions):
    c = task_color(task)
    ax_ci.hlines(y, lo, hi, colors=c, linewidth=2, zorder=2)
    ax_ci.plot(pt, y, "o", color=c, markersize=8, zorder=3,
               markeredgecolor="white", markeredgewidth=0.6)

# Spines
ax_ci.spines["top"].set_visible(False)
ax_ci.spines["right"].set_visible(False)
ax_ci.spines["left"].set_visible(False)
ax_ci.tick_params(left=False, labelleft=False)
ax_ci.set_xlabel("Transfer Asymmetry (ZH→EN − EN→ZH), pp",
                 fontsize=10, fontfamily="DejaVu Sans")
ax_ci.tick_params(axis="x", labelsize=9)

# Legend
from matplotlib.lines import Line2D
legend_handles = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor=COLOR_CONFLICT,
           markersize=7, label="Conflict"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=COLOR_XNLI,
           markersize=7, label="XNLI"),
]
ax_ci.legend(handles=legend_handles, loc="upper right", frameon=True,
             framealpha=0.9, edgecolor="#cccccc", fontsize=9,
             handletextpad=0.3, borderpad=0.3)

# ── Right panel: inline numbers ──────────────────────────────────────
ax_nums.set_xlim(0, 1)
ax_nums.axis("off")
for (label, pt, lo, hi, task), y in zip(rows, y_positions):
    sign = lambda v: f"+{v:.1f}" if v >= 0 else f"{v:.1f}"
    txt = f"{sign(pt)}  [{sign(lo)}, {sign(hi)}] pp"
    ax_nums.text(0.05, y, txt, ha="left", va="center",
                 fontsize=9, fontfamily="DejaVu Sans",
                 color=task_color(task))

# ── Save ──────────────────────────────────────────────────────────────
out_dir = "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/figures/paper"
fig.savefig(f"{out_dir}/fig3_asymmetry_forest.pdf",
            bbox_inches="tight", dpi=300)
fig.savefig(f"{out_dir}/fig3_asymmetry_forest.png",
            bbox_inches="tight", dpi=300)
plt.close(fig)
print("Done — saved PDF + PNG")
