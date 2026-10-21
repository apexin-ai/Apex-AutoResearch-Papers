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

center = np.array(data["bstar"]["center"])
mean = np.array(data["bstar"]["mean"])
median = np.array(data["bstar"]["median"])
p25 = np.array(data["bstar"]["p25"])
p75 = np.array(data["bstar"]["p75"])

fig, ax = plt.subplots(figsize=(5.5, 3.2))

ax.fill_between(center, p25, p75, color="#1f77b4", alpha=0.2, label="P25–P75")
ax.plot(center, median, color="#1f77b4", linewidth=1.5, label="Median")
ax.plot(center, mean, color="#1f77b4", linewidth=1.0, linestyle="--", alpha=0.7, label="Mean")

ax.set_xlabel("Training Step")
ax.set_ylabel("$b^*$")
ax.legend(loc="upper right", framealpha=0.9)
ax.set_xlim(0, center[-1])
ax.set_ylim(0, 2.0)

out_dir = Path(__file__).parent
fig.savefig(out_dir / "fig_bstar_trajectory.pdf")
fig.savefig(out_dir / "fig_bstar_trajectory.png")
plt.close()
print(f"Saved to {out_dir / 'fig_bstar_trajectory.pdf'}")
