# Fig 1: Normalized v/e ratio diagnostic plot.
# Shows nve over training for key experiments. >1.5x red zone (35K+).
# Data source: experiment registry (exp_001, 008d, 009b, 008f, 009c, 008e_v3).
# Paper section: Results (C2 — trained dt_emb triggers pathological overestimation).

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from fig_style import apply_style, savefig, COLORS, COLUMN_WIDTH, GOLDEN, DOUBLE_WIDTH

apply_style()

# ── Data (from registry + paper_framing.md) ──────────────────────────

steps_k = np.array([25, 35, 45, 55, 65, 75, 85, 95, 105])

baseline_ve = np.array([0.087, 0.241, 0.331, 0.404, 0.563, 0.719, 0.701, 0.632, 0.656])

# Trained dt_emb — seed 1 (008d, collapse)
nve_008d = np.array([1.78, 1.71, 2.09, 4.12, np.nan, np.nan, np.nan, np.nan, np.nan])
steps_008d = steps_k[:4]
nve_008d_valid = nve_008d[:4]

# Trained dt_emb — seed 2 (009b, self-correcting)
nve_009b = np.array([2.05, 1.24, 1.62, 1.41, 0.94, 0.66, 0.51, 0.43, 0.38])

# No dt_emb — seed 1 (008f)
nve_008f = np.array([1.02, 0.73, 0.83, 0.97, 0.37, 0.42, 0.65, np.nan, 0.30])

# No dt_emb — seed 2 (009c)
nve_009c = np.array([1.26, 0.79, 0.72, 0.66, np.nan, np.nan, np.nan, np.nan, 1.14])

# Mitigation (008e_v3, dt=1 imag)
nve_008e = np.array([1.93, 0.94, 0.88, 0.87, 0.72, 0.73, 0.76, 0.75, 0.80])

# Untrained dt_emb (008a, H=15)
nve_008a = np.array([np.nan, np.nan, np.nan, 0.93, 0.66, 0.75, 0.68, 0.79, 0.59])

# ── Plot ──────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(DOUBLE_WIDTH, DOUBLE_WIDTH / GOLDEN / 1.4))

# Pathological zone (35K+)
ax.axhspan(1.5, 5.0, xmin=0, xmax=1, color=COLORS["pathological"], alpha=0.07, zorder=0)
ax.axhline(1.5, color=COLORS["threshold"], ls="--", lw=0.8, zorder=1)
ax.text(106, 1.55, "pathological\nthreshold (1.5×)", fontsize=6, color=COLORS["threshold"],
        va="bottom", ha="left")

# Vertical line at 35K (diagnostic window start)
ax.axvline(35, color="gray", ls=":", lw=0.6, alpha=0.5)
ax.text(35.5, 4.3, "diagnostic\nwindow (≥35K)", fontsize=6, color="gray", va="top", rotation=0)

# Healthy zone
ax.axhspan(0, 1.0, color=COLORS["healthy_zone"], alpha=0.04, zorder=0)

# Plot lines
ax.plot(steps_008d, nve_008d_valid, "-s", color=COLORS["dt2_trained"],
        label="008d: trained dt_emb (seed 1, collapse)", markerfacecolor="white", zorder=5)
ax.plot(steps_k, nve_009b, "-s", color=COLORS["seed2"],
        label="009b: trained dt_emb (seed 2, self-correct)", markerfacecolor="white", zorder=5)
ax.plot(steps_k, nve_008f, "-P", color=COLORS["no_dt_emb"],
        label="008f: no dt_emb (seed 1)", markerfacecolor="white", zorder=4)
ax.plot(steps_k, nve_009c, "--P", color=COLORS["no_dt_emb"], alpha=0.55,
        label="009c: no dt_emb (seed 2)", markerfacecolor="white", zorder=4)
ax.plot(steps_k, nve_008e, "-v", color=COLORS["mitigation"],
        label="008e_v3: dt=1 imag (mitigation)", markerfacecolor="white", zorder=4)
ax.plot(steps_k[3:], nve_008a[3:], "-^", color=COLORS["dt2_untrained"],
        label="008a: untrained dt_emb", markerfacecolor="white", zorder=4)

# Reference line at 1.0
ax.axhline(1.0, color="gray", ls="-", lw=0.4, alpha=0.3)

ax.set_xlabel("Training Steps (×1000)")
ax.set_ylabel("Normalized v/e Ratio\n(experiment v/e ÷ baseline v/e)")
ax.set_xlim(22, 110)
ax.set_ylim(0, 4.5)
ax.set_xticks([25, 35, 45, 55, 65, 75, 85, 95, 105])
ax.legend(loc="upper right", ncol=2, fontsize=6)
ax.set_title("Normalized Value/Eval Ratio: Diagnostic Marker for Delusional Critic")

savefig(fig, "fig1_nve_diagnostic")
print("Saved fig1_nve_diagnostic.pdf/.png")
