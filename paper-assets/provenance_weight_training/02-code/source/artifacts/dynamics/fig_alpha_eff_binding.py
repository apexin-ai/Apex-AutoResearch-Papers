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

center = np.array(data["alpha"]["center"])
rate = np.array(data["alpha"]["rate"])


def rolling_mean(x, w=5):
    kernel = np.ones(w) / w
    padded = np.pad(x, (w // 2, w - 1 - w // 2), mode="edge")
    return np.convolve(padded, kernel, mode="valid")


fig, ax = plt.subplots(figsize=(5.5, 3.2))

ax.plot(center, rate, color="#d62728", linewidth=0.8, alpha=0.5)
ax.plot(center, rolling_mean(rate), color="#d62728", linewidth=1.5, label="Rolling avg (w=5)")

ax.axhline(y=np.mean(rate), color="#666666", linestyle=":", linewidth=0.8,
           label=f"Overall mean = {np.mean(rate):.3f}")

ax.set_xlabel("Training Step")
ax.set_ylabel("$\\alpha_{\\mathrm{eff}}$ Binding Rate")
ax.legend(loc="upper right", framealpha=0.9)
ax.set_xlim(0, center[-1])
ax.set_ylim(0, 0.6)

out_dir = Path(__file__).parent
fig.savefig(out_dir / "fig_alpha_eff_binding.pdf")
fig.savefig(out_dir / "fig_alpha_eff_binding.png")
plt.close()
print(f"Saved to {out_dir / 'fig_alpha_eff_binding.pdf'}")
