"""
Trigger-rate vs Improvement scatter plot for ACR-VLA paper.
4-suite scatter: x = trigger rate (%), y = Δ SR vs VLA-only (pp).
D134 narrative: gating modulates intervention intensity.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

suites = ["Spatial", "Goal", "Long", "Object"]
trigger_rates = [20.0, 8.0, 4.0, 3.5]
deltas = [2.1, 1.3, -0.3, 0.1]
colors = ["#2171b5", "#6baed6", "#bdd7e7", "#eff3ff"]
markers = ["o", "s", "D", "^"]

fig, ax = plt.subplots(figsize=(4.5, 3.2))

for i, (suite, tr, delta) in enumerate(zip(suites, trigger_rates, deltas)):
    ax.scatter(tr, delta, s=120, c=colors[i], edgecolors="black",
               linewidths=0.8, marker=markers[i], zorder=5)
    offset_x = 0.8
    offset_y = 0.18
    if suite == "Object":
        offset_y = -0.35
    elif suite == "Long":
        offset_y = -0.35
    ax.annotate(suite, (tr, delta), fontsize=9, fontweight="bold",
                xytext=(tr + offset_x, delta + offset_y), zorder=6)

ax.axhline(y=0, color="gray", linestyle="--", linewidth=0.7, alpha=0.6)
ax.axvline(x=5.0, color="#d62728", linestyle=":", linewidth=1.0, alpha=0.5)

ax.annotate("trigger > 7%\nimprovement",
            xy=(12, 1.7), fontsize=7.5, color="#2171b5", ha="center",
            fontstyle="italic")
ax.annotate("trigger < 5%\nbaseline preserved",
            xy=(3.75, -0.8), fontsize=7.5, color="#999999", ha="center",
            fontstyle="italic")

ax.set_xlabel("CRM trigger rate (%)", fontsize=10)
ax.set_ylabel(r"$\Delta$ SR vs VLA-only (pp)", fontsize=10)
ax.set_xlim(0, 25)
ax.set_ylim(-1.5, 3.0)
ax.tick_params(labelsize=9)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

out_dir = os.path.dirname(os.path.abspath(__file__))
for ext in ["pdf", "png"]:
    path = os.path.join(out_dir, f"trigger_rate_scatter.{ext}")
    fig.savefig(path, dpi=300, bbox_inches="tight")

plt.close()
print("Saved trigger_rate_scatter.pdf and .png")
