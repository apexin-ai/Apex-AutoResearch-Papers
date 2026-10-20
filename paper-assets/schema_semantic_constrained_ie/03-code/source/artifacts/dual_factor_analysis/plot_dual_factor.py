"""
Dual-factor scatter plot: tightness × baseline_RV vs residual_DR.
Shows that the product of constraint tightness and baseline RV explains
the variation in residual DR across 4 model-dataset configurations.
Output: dual_factor_scatter.pdf
"""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

here = Path(__file__).parent
with open(here / "dual_factor_data.json") as f:
    data = json.load(f)

configs = data["configurations"]
labels = [c["label"] for c in configs]
x = np.array([c["tightness_x_RV"] for c in configs])
y = np.array([c["residual_DR_pct"] for c in configs])

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
r_squared = r_value ** 2

fig, ax = plt.subplots(figsize=(5, 4))

markers = {"Qwen3-8B": "o", "Llama-3.1-8B-Instruct": "s"}
colors = {"SciERC": "#2B4C7E", "DocRED": "#8BAED4"}

for c in configs:
    xi = c["tightness_x_RV"]
    yi = c["residual_DR_pct"]
    m = markers[c["model"]]
    col = colors[c["dataset"]]
    short_model = "Qwen" if "Qwen" in c["model"] else "Llama"
    ax.scatter(xi, yi, marker=m, c=col, s=90, zorder=5, edgecolors="#333333", linewidths=0.5)
    offset_x, offset_y = 0.4, 0.3
    if c["label"] == "Qwen DocRED":
        offset_x, offset_y = -1.0, 0.6
    elif c["label"] == "Llama DocRED":
        offset_x, offset_y = 0.5, -0.7
    elif c["label"] == "Llama SciERC":
        offset_x, offset_y = 1.0, -0.3
    elif c["label"] == "Qwen SciERC":
        offset_x, offset_y = 0.5, 0.8
    ax.annotate(f"{short_model}\n{c['dataset']}",
                (xi, yi), textcoords="offset points",
                xytext=(offset_x * 30, offset_y * 30),
                fontsize=8, ha="center", color="#333333",
                arrowprops=dict(arrowstyle="-", color="#888888", lw=0.5))

x_fit = np.linspace(0, max(x) * 1.15, 100)
y_fit = slope * x_fit + intercept
ax.plot(x_fit, y_fit, "--", color="#666666", linewidth=1, alpha=0.7,
        label=f"$y = {slope:.3f}x + {intercept:.3f}$\n$R^2 = {r_squared:.3f}$")

ax.set_xlabel(r"$\bar{\tau} \times \mathrm{RV}_{\mathrm{baseline}}$ (%)", fontsize=11)
ax.set_ylabel("Residual DR (%)", fontsize=11)
ax.set_xlim(-2, max(x) * 1.25)
ax.set_ylim(-1, max(y) * 1.35)
ax.legend(fontsize=9, loc="upper left", framealpha=0.9, edgecolor="#DDDDDD")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(labelsize=9)

fig.tight_layout()
out_pdf = here / "dual_factor_scatter.pdf"
out_png = here / "dual_factor_scatter.png"
fig.savefig(out_pdf, dpi=300, bbox_inches="tight")
fig.savefig(out_png, dpi=150, bbox_inches="tight")
print(f"Saved: {out_pdf}")
print(f"Saved: {out_png}")
print(f"\nFitted line: y = {slope:.4f}x + {intercept:.4f}")
print(f"R² = {r_squared:.4f}, p = {p_value:.4f}")
print(f"\nData points:")
for l, xi, yi in zip(labels, x, y):
    print(f"  {l}: τ×RV = {xi:.3f}, residual_DR = {yi:.2f}%")
