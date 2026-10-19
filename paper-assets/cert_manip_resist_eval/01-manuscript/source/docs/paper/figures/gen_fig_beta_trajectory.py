import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

K_vals = [3, 5, 7]

# Meta-analytic DerSimonian-Laird pooled estimates (position-bias fix)
keff_mean = [0.286, 0.353, 0.309]
keff_lo   = [0.073, 0.125, 0.100]
keff_hi   = [0.499, 0.581, 0.517]

eta_mean  = [0.243, 0.091, 0.086]
eta_lo    = [0.163, -0.031, -0.039]
eta_hi    = [0.323, 0.212, 0.211]

# Per-condition scatter data (position-bias fix)
keff_scatter = {
    3: [0.483, 0.483, 0.542, 0.378, -0.334, 0.523, 0.357, 0.283, 0.466, 0.347, -0.372, 0.291],
    5: [0.529, 0.455, 0.645, 0.335, -0.378, 0.499, 0.558, 0.065, 1.172, 0.418, -0.280, 0.226],
    7: [0.545, 0.443, 0.556, 0.295, -0.375, 0.459, 0.608, 0.046, 0.845, 0.367, -0.209, 0.127],
}
eta_scatter = {
    3: [0.212, 0.193, 0.119, 0.292, 0.516, 0.081, 0.265, 0.260, 0.083, 0.250, 0.378, 0.202],
    5: [0.151, 0.162, -0.110, 0.376, 0.391, -0.082, -0.048, 0.347, -0.712, 0.142, 0.216, 0.226],
    7: [0.112, 0.090, -0.101, 0.429, 0.380, -0.142, -0.135, 0.345, -0.413, 0.131, 0.144, 0.187],
}

fig, ax = plt.subplots(figsize=(4.5, 3.5))

blue = "#1E88E5"
red = "#E53935"
jitter = 0.08

# Per-condition scatter (background)
for k in K_vals:
    ax.scatter(
        np.full(len(keff_scatter[k]), k) - jitter,
        keff_scatter[k],
        color=blue, alpha=0.15, s=12, zorder=1, edgecolors="none",
    )
    ax.scatter(
        np.full(len(eta_scatter[k]), k) + jitter,
        eta_scatter[k],
        color=red, alpha=0.15, s=12, zorder=1, edgecolors="none",
    )

# CI bands
ax.fill_between(K_vals, keff_lo, keff_hi, color=blue, alpha=0.2, zorder=2)
ax.fill_between(K_vals, eta_lo, eta_hi, color=red, alpha=0.2, zorder=2)

# Lines + markers
ax.plot(K_vals, keff_mean, color=blue, linewidth=1.8, zorder=3)
ax.scatter(K_vals, keff_mean, color=blue, s=60, marker="s", zorder=4, label=r"$K_{\mathrm{eff}}$", edgecolors="white", linewidths=0.6)

ax.plot(K_vals, eta_mean, color=red, linewidth=1.8, zorder=3)
ax.scatter(K_vals, eta_mean, color=red, s=60, marker="o", zorder=4, label=r"$\eta_{\max}$", edgecolors="white", linewidths=0.6)

# Reference line
ax.axhline(0, color="grey", linestyle="--", linewidth=0.8, zorder=1)
ax.text(7.15, 0.015, r"$\beta = 0$", fontsize=8, color="grey", va="bottom")

# Axes
ax.set_xlabel("Panel size $K$", fontsize=10, fontfamily="DejaVu Sans")
ax.set_ylabel("Standardized $\\beta$ (pooled)", fontsize=10, fontfamily="DejaVu Sans")
ax.set_xticks(K_vals)
ax.set_xlim(2.3, 7.7)
ax.set_ylim(-0.45, 0.65)

# Legend
ax.legend(loc="upper right", fontsize=9, framealpha=0.9, edgecolor="none")

# Clean spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(labelsize=9)

plt.tight_layout()

out_base = "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/figures/fig_beta_trajectory"
fig.savefig(out_base + ".pdf", dpi=300, bbox_inches="tight")
fig.savefig(out_base + ".png", dpi=300, bbox_inches="tight")
plt.close()
print("Done:", out_base + ".pdf")
