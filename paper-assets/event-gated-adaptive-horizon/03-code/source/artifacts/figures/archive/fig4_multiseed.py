# Fig 4: Multi-seed robustness — trained dt_emb vs no dt_emb across seeds.
# Shows eval curves + nve trajectories for same config, different seeds.
# Data source: 008d/009b (trained, seeds 1-2), 008f/009c (no dt_emb, seeds 1-2).
# Paper section: Results (C2 — nve>1.5x threshold, 4/4 separation).

import numpy as np
import matplotlib.pyplot as plt
from fig_style import apply_style, savefig, COLORS, DOUBLE_WIDTH, GOLDEN

apply_style()

steps = np.array([25, 35, 45, 55, 65, 75, 85, 95, 105])

# ── Eval return data ──────────────────────────────────────────────────

# Trained dt_emb seed 1 (008d) — collapse
eval_008d = np.array([167.22, 146.34, 140.80, 82.75, np.nan, np.nan, np.nan, np.nan, np.nan])

# Trained dt_emb seed 2 (009b) — self-correcting
eval_009b = np.array([141.12, 164.14, 141.04, 172.33, 209.16, np.nan, np.nan, np.nan, 268.0])

# No dt_emb seed 1 (008f)
eval_008f = np.array([196.78, 206.67, 194.08, 173.45, 375, 324, 246, 319, 503.0])

# No dt_emb seed 2 (009c)
eval_009c = np.array([168.75, 178.94, 211.08, 238.91, 244.15, np.nan, np.nan, np.nan, 148.0])

# ── NVE data ──────────────────────────────────────────────────────────

nve_008d = np.array([1.78, 1.71, 2.09, 4.12, np.nan, np.nan, np.nan, np.nan, np.nan])
nve_009b = np.array([2.05, 1.24, 1.62, 1.41, 0.94, 0.66, 0.51, 0.43, 0.38])
nve_008f = np.array([1.02, 0.73, 0.83, 0.97, 0.37, 0.42, 0.65, np.nan, 0.30])
nve_009c = np.array([1.26, 0.79, 0.72, 0.66, np.nan, np.nan, np.nan, np.nan, 1.14])

# ── Plot: 2 rows × 2 cols ────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(DOUBLE_WIDTH, DOUBLE_WIDTH / GOLDEN),
                         sharex=True, gridspec_kw={"hspace": 0.35, "wspace": 0.3})

# Top-left: Eval — trained dt_emb (both seeds)
ax = axes[0, 0]
ax.plot(steps[:4], eval_008d[:4], "-s", color=COLORS["dt2_trained"],
        label="seed 1 (collapse)", markerfacecolor="white")
ax.plot(steps, eval_009b, "-s", color=COLORS["seed2"],
        label="seed 2 (self-correct)", markerfacecolor="white")
ax.set_ylabel("Eval Return")
ax.set_title("Trained dt_emb — Eval", fontsize=8)
ax.legend(fontsize=6)
ax.set_ylim(0, 400)

# Top-right: Eval — no dt_emb (both seeds)
ax = axes[0, 1]
ax.plot(steps, eval_008f, "-P", color=COLORS["no_dt_emb"],
        label="seed 1", markerfacecolor="white")
ax.plot(steps, eval_009c, "--P", color=COLORS["no_dt_emb"], alpha=0.55,
        label="seed 2", markerfacecolor="white")
ax.set_title("No dt_emb — Eval", fontsize=8)
ax.legend(fontsize=6)
ax.set_ylim(0, 600)

# Bottom-left: NVE — trained dt_emb
ax = axes[1, 0]
ax.axhspan(1.5, 5.0, color=COLORS["pathological"], alpha=0.07)
ax.axhline(1.5, color=COLORS["threshold"], ls="--", lw=0.7)
ax.plot(steps[:4], nve_008d[:4], "-s", color=COLORS["dt2_trained"],
        label="seed 1", markerfacecolor="white")
ax.plot(steps, nve_009b, "-s", color=COLORS["seed2"],
        label="seed 2", markerfacecolor="white")
ax.axhline(1.0, color="gray", ls="-", lw=0.3, alpha=0.3)
ax.set_ylabel("Normalized v/e")
ax.set_xlabel("Steps (×1000)")
ax.set_title("Trained dt_emb — NVE", fontsize=8)
ax.legend(fontsize=6)
ax.set_ylim(0, 4.5)
ax.text(107, 1.55, "1.5×", fontsize=5.5, color=COLORS["threshold"], va="bottom")

# Bottom-right: NVE — no dt_emb
ax = axes[1, 1]
ax.axhspan(1.5, 5.0, color=COLORS["pathological"], alpha=0.07)
ax.axhline(1.5, color=COLORS["threshold"], ls="--", lw=0.7)
ax.plot(steps, nve_008f, "-P", color=COLORS["no_dt_emb"],
        label="seed 1", markerfacecolor="white")
ax.plot(steps, nve_009c, "--P", color=COLORS["no_dt_emb"], alpha=0.55,
        label="seed 2", markerfacecolor="white")
ax.axhline(1.0, color="gray", ls="-", lw=0.3, alpha=0.3)
ax.set_xlabel("Steps (×1000)")
ax.set_title("No dt_emb — NVE", fontsize=8)
ax.legend(fontsize=6)
ax.set_ylim(0, 4.5)
ax.text(107, 1.55, "1.5×", fontsize=5.5, color=COLORS["threshold"], va="bottom")

for ax_row in axes:
    for ax in ax_row:
        ax.set_xticks([25, 35, 45, 55, 65, 75, 85, 95, 105])

savefig(fig, "fig4_multiseed")
print("Saved fig4_multiseed.pdf/.png")
