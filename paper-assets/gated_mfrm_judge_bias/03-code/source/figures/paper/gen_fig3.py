"""Generate Figure 3: Error Propagation Sensitivity.

Dual-panel plot showing θ-RMSE and c_n-RMSE as functions of exposure noise σ_e.
Demonstrates graceful degradation below σ_crit ≈ 0.2 and rapid nonlinear
degradation beyond, establishing a falsifiable applicability boundary.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper"

# --- Data from exp-012 (20 seeds) ---
sigma = np.array([0.0, 0.1, 0.2, 0.5])

theta_rmse_mean = np.array([0.1277, 0.1295, 0.1352, 0.1748])
theta_rmse_std = np.array([0.0178, 0.0178, 0.0175, 0.0266])

cn_rmse_mean = np.array([0.533, 0.5452, 0.5751, 0.8415])
cn_rmse_std = np.array([0.1869, 0.1934, 0.1981, 0.1954])

# Percentage degradation relative to baseline (σ=0)
theta_pct = (theta_rmse_mean - theta_rmse_mean[0]) / theta_rmse_mean[0] * 100
cn_pct = (cn_rmse_mean - cn_rmse_mean[0]) / cn_rmse_mean[0] * 100

SIGMA_CRIT = 0.2
BLUE = "#1f4e79"

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 3.0))

for ax, y_mean, y_std, pct, ylabel, panel_label in [
    (ax1, theta_rmse_mean, theta_rmse_std,
     theta_pct, r"$\theta$-RMSE", "(a)"),
    (ax2, cn_rmse_mean, cn_rmse_std,
     cn_pct, r"$c_n$-RMSE", "(b)"),
]:
    # Regime bands
    ax.axvspan(-0.02, SIGMA_CRIT, color="green", alpha=0.12, zorder=0)
    ax.axvspan(SIGMA_CRIT, 0.58, color="red", alpha=0.10, zorder=0)

    # σ_crit vertical line
    ax.axvline(SIGMA_CRIT, color="black", linestyle="--", linewidth=0.9, zorder=2)
    ax.text(SIGMA_CRIT + 0.01, ax.get_ylim()[0] if ax.get_ylim()[0] != 0 else 0.99,
            r"$\sigma_{\mathrm{crit}}$", fontsize=8, va="top",
            transform=ax.get_xaxis_transform(), ha="left")

    # Empirical data with error bars
    ax.errorbar(sigma, y_mean, yerr=y_std, fmt="o-", color=BLUE,
                markersize=5, linewidth=1.4, capsize=3, capthick=1.0,
                label="Empirical (20 seeds)", zorder=5)

    # Percentage degradation annotations
    for i in range(len(sigma)):
        if pct[i] == 0:
            continue
        offset_y = 8 if i < 3 else 10
        offset_x = 0
        if i == 1:
            offset_x = 5
        ax.annotate(
            f"+{pct[i]:.1f}%",
            xy=(sigma[i], y_mean[i]),
            xytext=(offset_x, offset_y),
            textcoords="offset points",
            fontsize=7, color="#b03030", fontweight="bold",
            ha="center", va="bottom",
        )

    ax.set_xlabel(r"Exposure noise $\sigma_e$", fontsize=9)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.tick_params(labelsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlim(-0.02, 0.55)

    # Panel label
    ax.text(0.03, 0.95, panel_label, transform=ax.transAxes,
            fontsize=10, fontweight="bold", va="top")

# Fix σ_crit label placement after axes limits are set
for ax in (ax1, ax2):
    ylim = ax.get_ylim()
    y_top = ylim[1] - (ylim[1] - ylim[0]) * 0.04
    for txt in ax.texts:
        if r"$\sigma_{\mathrm{crit}}$" in txt.get_text():
            txt.set_position((SIGMA_CRIT + 0.015, y_top))
            txt.set_transform(ax.transData)
            txt.set_va("top")
            txt.set_ha("left")

# Legend (shared, in panel a)
ax1.legend(fontsize=7, loc="lower right", framealpha=0.8,
           edgecolor="0.7", borderpad=0.4)

fig.tight_layout(w_pad=2.5, pad=0.4)

pdf_path = f"{OUT_DIR}/fig3_error_propagation.pdf"
png_path = f"{OUT_DIR}/fig3_error_propagation.png"
fig.savefig(pdf_path, bbox_inches="tight", dpi=300)
fig.savefig(png_path, bbox_inches="tight", dpi=300)
plt.close(fig)

print(f"Saved: {pdf_path}")
print(f"Saved: {png_path}")
