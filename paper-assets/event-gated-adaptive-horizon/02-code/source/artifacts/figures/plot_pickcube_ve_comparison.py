import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

with open("/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/pickcube_ve_trajectory.json") as f:
    data = json.load(f)

baseline = data["experiments"]["exp_019a_v2_pickcube_baseline"]["checkpoints"]
civo = data["experiments"]["exp_019b_pickcube_civo_trigger"]["checkpoints"]
nve_data = data["experiments"]["exp_019b_pickcube_civo_trigger"]["nve_vs_baseline"]["values"]

steps_a = [c["step"] for c in baseline]
ve_a = [c["ve_ratio"] for c in baseline]
steps_b = [c["step"] for c in civo]
ve_b = [c["ve_ratio"] for c in civo]
nve_steps = [d["step"] for d in nve_data]
nve_vals = [d["nve"] for d in nve_data]

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 4.5), sharex=True,
                                gridspec_kw={"height_ratios": [3, 2], "hspace": 0.08})

# --- Upper panel: V/E ratio ---
ax1.plot(np.array(steps_a) / 1000, ve_a, color="#999999", linewidth=1.4,
         marker="o", markersize=3, label="Baseline (no dt-emb)", zorder=2)
ax1.plot(np.array(steps_b) / 1000, ve_b, color="#D55E00", linewidth=1.4,
         marker="s", markersize=3, label="CIVO trigger (trained dt-emb)", zorder=3)

ax1.set_ylabel("V/E Ratio")
ax1.legend(loc="upper left", frameon=True, fancybox=False, edgecolor="#cccccc")
ax1.set_xlim(0, 200)
ax1.set_ylim(bottom=0)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax1.grid(axis="y", linewidth=0.3, alpha=0.5)
ax1.tick_params(axis="x", which="both", labelbottom=False)

# --- Lower panel: NVE ---
ax2.plot(np.array(nve_steps) / 1000, nve_vals, color="#0072B2", linewidth=1.4,
         marker="D", markersize=4, zorder=3, label="NVE$_t$")
ax2.axhline(y=1.5, color="#E69F00", linewidth=1.0, linestyle="--", label="Threshold (1.5$\\times$)", zorder=2)
ax2.axhline(y=1.0, color="#bbbbbb", linewidth=0.6, linestyle=":", zorder=1)

peak_idx = nve_vals.index(max(nve_vals))
peak_step = nve_steps[peak_idx] / 1000
peak_val = nve_vals[peak_idx]
ax2.annotate(f"Peak: {peak_val:.2f}$\\times$\n(step {nve_steps[peak_idx]:,})",
             xy=(peak_step, peak_val),
             xytext=(peak_step + 18, peak_val - 0.15),
             fontsize=7.5,
             arrowprops=dict(arrowstyle="-|>", color="#333333", lw=0.8),
             bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#aaaaaa", lw=0.5),
             zorder=4)

ax2.set_xlabel("Training Step ($\\times 10^3$)")
ax2.set_ylabel("NVE$_t$  (CIVO / Baseline)")
ax2.set_xlim(0, 200)
ax2.set_ylim(0, 4.5)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax2.legend(loc="upper right", frameon=True, fancybox=False, edgecolor="#cccccc", fontsize=7.5)
ax2.grid(axis="y", linewidth=0.3, alpha=0.5)

out_base = "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/pickcube_ve_comparison"
fig.savefig(out_base + ".pdf")
fig.savefig(out_base + ".png", dpi=300)
plt.close()
print("Saved PDF and PNG.")
