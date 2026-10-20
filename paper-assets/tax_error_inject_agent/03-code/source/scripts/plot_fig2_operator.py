#!/usr/bin/env python3
"""Fig 2: Per-Operator Recovery Differential (TaxEI − Vanilla)."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# --- Data ---
vanilla_rates = {
    "C1_context_truncation": 9 / 12,
    "C4_observation_masking": 6 / 11,
    "P1_step_order_swap": 7 / 12,
    "P2_sub_goal_deletion": 7 / 12,
}

taxei_rates = {
    "C1_context_truncation": 8 / 12,
    "C4_observation_masking": 7 / 11,
    "P1_step_order_swap": 7 / 12,
    "P2_sub_goal_deletion": 6 / 12,
}

labels = {
    "C4_observation_masking": "C4: Obs. Masking",
    "P1_step_order_swap": "P1: Step Swap",
    "C1_context_truncation": "C1: Context Trunc.",
    "P2_sub_goal_deletion": "P2: Goal Deletion",
}

deltas = {k: (taxei_rates[k] - vanilla_rates[k]) * 100 for k in vanilla_rates}

# Sort by delta descending
order = sorted(deltas, key=lambda k: deltas[k], reverse=True)

y_labels = [labels[k] for k in order]
x_vals = [deltas[k] for k in order]

# --- Colors ---
colors = []
for v in x_vals:
    if v > 0.01:
        colors.append("#2E86AB")   # blue for positive
    elif v < -0.01:
        colors.append("#D7263D")   # red for negative
    else:
        colors.append("#888888")   # grey for zero

# --- Figure ---
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
})

fig, ax = plt.subplots(figsize=(6, 2.8))

y_pos = range(len(order))
bars = ax.barh(y_pos, x_vals, color=colors, height=0.55, edgecolor="white", linewidth=0.5)

ax.set_yticks(list(y_pos))
ax.set_yticklabels(y_labels)
ax.invert_yaxis()

ax.axvline(0, color="black", linewidth=0.8, zorder=1)

# Annotations
for i, (bar, val) in enumerate(zip(bars, x_vals)):
    sign = "+" if val > 0 else ""
    text = f"{sign}{val:.1f}pp"
    x_offset = 0.6 if val >= 0 else -0.6
    ha = "left" if val >= 0 else "right"
    ax.text(val + x_offset, i, text, va="center", ha=ha, fontsize=10, fontweight="bold")

# Bracket annotations for local vs global split
ax.annotate(
    "local info loss",
    xy=(0, -0.55), xycoords=("axes fraction", "data"),
    fontsize=8.5, fontstyle="italic", color="#2E86AB", ha="left",
)
ax.plot([-0.02, -0.02], [-0.3, 0.3], transform=ax.get_yaxis_transform(),
        color="#2E86AB", linewidth=1.5, clip_on=False)

ax.annotate(
    "global plan disruption",
    xy=(0, 1.45), xycoords=("axes fraction", "data"),
    fontsize=8.5, fontstyle="italic", color="#D7263D", ha="left",
)
ax.plot([-0.02, -0.02], [0.7, 3.3], transform=ax.get_yaxis_transform(),
        color="#D7263D", linewidth=1.5, clip_on=False)

ax.set_xlabel("Δ Recovery Rate (TaxEI − Vanilla, pp)")
ax.set_title("Per-Operator Recovery Differential", fontsize=12, fontweight="bold", pad=10)

ax.set_xlim(-12, 12)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

# --- Save ---
out_dir = Path(__file__).resolve().parent.parent / "figures" / "paper"
out_dir.mkdir(parents=True, exist_ok=True)

pdf_path = out_dir / "fig2_operator_gradient.pdf"
png_path = out_dir / "fig2_operator_gradient.png"

fig.savefig(pdf_path, dpi=300, bbox_inches="tight")
fig.savefig(png_path, dpi=300, bbox_inches="tight")
plt.close()

print(f"Saved: {pdf_path}")
print(f"Saved: {png_path}")
