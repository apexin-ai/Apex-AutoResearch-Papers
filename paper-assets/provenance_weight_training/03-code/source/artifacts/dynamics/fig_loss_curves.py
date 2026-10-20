import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.labelsize": 10,
    "legend.fontsize": 8,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

data_path = Path(__file__).parent / "training_dynamics_data.json"
with open(data_path) as f:
    data = json.load(f)

steps = np.array(data["loss"]["steps"])
adaptive = np.array(data["loss"]["adaptive"])
uniform = np.array(data["loss"]["uniform"])
grid = np.array(data["loss"]["grid"])


def ema(values, alpha=0.15):
    out = np.zeros_like(values)
    out[0] = values[0]
    for i in range(1, len(values)):
        out[i] = alpha * values[i] + (1 - alpha) * out[i - 1]
    return out


fig, ax = plt.subplots(figsize=(5.5, 3.2))

ax.plot(steps, ema(uniform), color="#888888", linewidth=1.5, label="Uniform ($b=0$)")
ax.plot(steps, ema(grid), color="#2ca02c", linewidth=1.5, label="Grid-best ($b=0.3$)")
ax.plot(steps, ema(adaptive), color="#1f77b4", linewidth=1.5, label="Adaptive $b^*$")

ax.fill_between(steps, uniform - 0.02, uniform + 0.02, color="#888888", alpha=0.08)
ax.fill_between(steps, grid - 0.02, grid + 0.02, color="#2ca02c", alpha=0.08)
ax.fill_between(steps, adaptive - 0.02, adaptive + 0.02, color="#1f77b4", alpha=0.08)

ax.set_xlabel("Training Step")
ax.set_ylabel("Unweighted Loss")
ax.legend(loc="upper right", framealpha=0.9)
ax.set_xlim(0, steps[-1])
ax.set_ylim(1.0, 2.8)

out_dir = Path(__file__).parent
fig.savefig(out_dir / "fig_loss_curves.pdf")
fig.savefig(out_dir / "fig_loss_curves.png")
plt.close()
print(f"Saved to {out_dir / 'fig_loss_curves.pdf'}")
