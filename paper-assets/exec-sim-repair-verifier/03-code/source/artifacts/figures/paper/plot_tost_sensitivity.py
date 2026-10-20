"""Regenerate Figure 3: TOST p-value vs equivalence margin for CLS-CWM and CLS-TRAJ."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import t as t_dist, norm

# ── CLS-CWM: seed-level paired TOST (df=4) ──
CWM_MEAN_D = 1.24
CWM_SE = 0.1821
CWM_DF = 4
CWM_MIN_MARGIN = 1.628

def tost_paired(mean_d, se, df, delta):
    t_upper = (mean_d - delta) / se
    t_lower = (mean_d + delta) / se
    p_upper = t_dist.cdf(t_upper, df)
    p_lower = 1 - t_dist.cdf(t_lower, df)
    return max(p_upper, p_lower)

# ── CLS-TRAJ: clustered bootstrap (normal approx) ──
TRAJ_MEAN_D = -0.4505
TRAJ_SE = 0.6517

def tost_bootstrap(mean_d, se, delta):
    z_lower = (-delta - mean_d) / se
    z_upper = (delta - mean_d) / se
    p_lower = norm.cdf(z_lower)
    p_upper = 1 - norm.cdf(z_upper)
    return max(p_lower, p_upper)

# ── Compute smooth curves ──
margins = np.linspace(0.6, 5.5, 200)
p_cwm = np.array([tost_paired(CWM_MEAN_D, CWM_SE, CWM_DF, d) for d in margins])
p_traj = np.array([tost_bootstrap(TRAJ_MEAN_D, TRAJ_SE, d) for d in margins])

# Data points from source files
cwm_pts = [(1.0, 0.871), (1.5, 0.113), (2.0, 0.007), (3.0, 0.000321), (5.0, 1.6e-5)]
traj_pts = [(1.0, 0.200), (1.5, 0.054), (1.71, 0.027), (2.0, 0.009), (3.0, 4.6e-5), (5.0, 1e-7)]

# ── Plot ──
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(margins, p_cwm, color="#1f77b4", linewidth=2, zorder=3)
ax.plot(margins, p_traj, color="#2ca02c", linewidth=2, zorder=3)

ax.scatter(*zip(*cwm_pts), color="#1f77b4", s=50, zorder=4, facecolors="white",
           edgecolors="#1f77b4", linewidths=1.5, label="CLS–CWM")
ax.scatter(*zip(*traj_pts[:-1]), color="#2ca02c", s=50, zorder=4, facecolors="white",
           edgecolors="#2ca02c", linewidths=1.5, label="CLS–TRAJ")

ax.axhline(0.05, color="red", linestyle="--", linewidth=1.2, zorder=2)
ax.text(4.8, 0.058, r"$\alpha = 0.05$", color="red", fontsize=10, ha="right", va="bottom")

holm_alpha = 0.05 / 2
ax.axhline(holm_alpha, color="red", linestyle=":", linewidth=0.8, alpha=0.6, zorder=2)
ax.text(4.8, holm_alpha * 1.15, r"$\alpha/2$ (Holm)", color="red", fontsize=9,
        ha="right", va="bottom", alpha=0.7)

# Annotation for CLS-CWM min equivalence margin
cwm_min_p = tost_paired(CWM_MEAN_D, CWM_SE, CWM_DF, CWM_MIN_MARGIN)
ax.annotate("$\\pm$1.63pp\n(min. equiv.)",
            xy=(CWM_MIN_MARGIN, cwm_min_p),
            xytext=(1.05, 0.22),
            fontsize=9, color="#1f77b4",
            arrowprops=dict(arrowstyle="->", color="#1f77b4", lw=1.2),
            ha="center", va="bottom")

ax.set_yscale("log")
ax.set_xlabel("Equivalence Margin (±pp)", fontsize=12)
ax.set_ylabel("TOST p-value", fontsize=12)
ax.set_xlim(0.5, 5.5)
ax.set_ylim(1e-7, 2)
ax.legend(fontsize=11, loc="upper right", framealpha=0.9)
ax.tick_params(labelsize=10)
ax.grid(True, alpha=0.15, which="both")

fig.tight_layout()
fig.savefig("fig_tost_sensitivity.pdf", bbox_inches="tight", dpi=300)
fig.savefig("fig_tost_sensitivity.png", bbox_inches="tight", dpi=200)
print("Saved fig_tost_sensitivity.pdf and .png")
