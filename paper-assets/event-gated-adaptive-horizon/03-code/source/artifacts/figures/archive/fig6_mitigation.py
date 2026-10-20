# Fig 6: Mitigation comparison (C6).
# 008e_v3 (dt=1 imag) vs 006 (dt=2 imag, collapse) vs baseline.
# Note: 008e_v3 currently has 1 independent seed (seed=1). s2 running.
# Data source: experiment registry.
# Paper section: Results (C6 — practical mitigation).

import numpy as np
import matplotlib.pyplot as plt
from fig_style import apply_style, savefig, COLORS, DOUBLE_WIDTH, GOLDEN

apply_style()

steps = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105])

# Baseline (representative trajectory)
baseline = np.array([31, 180, 310, 400, 443, 625.7, 616, 750, 830, 900, 915.67])

# 008e_v3 — mitigation (seed 1)
eval_008e_s1 = np.array([31, 131.2, 155.69, 276.47, 382.22, 486.84,
                         580.67, 574.09, 657.31, 851.86, 869.88])

# 008e_v3 — seed 2 (partial, running at 72K)
steps_s2 = np.array([5, 15, 25, 35, 45, 55, 65])
eval_008e_s2 = np.array([39.3, 180.9, 211.8, 320.4, 356.9, 418.3, 435.1])

# 006 — dt=2 imag, trained dt_emb, collapse
eval_006 = np.array([31, 256.9, 321.4, 485.3, 477, 360.4, 132.86,
                     np.nan, np.nan, np.nan, np.nan])

# 008a — untrained dt_emb (for reference)
eval_008a = np.array([31, 167.2, 230.8, 500.84, 563.41, 487.92,
                      608, 469.93, 583.73, 572.24, 777.66])

# ── NVE subplot data ──────────────────────────────────────────────────

steps_nve = np.array([25, 35, 45, 55, 65, 75, 85, 95, 105])
nve_008e = np.array([1.93, 0.94, 0.88, 0.87, 0.72, 0.73, 0.76, 0.75, 0.80])

# 006 nve (from paper_framing: 1.29@35K, 1.61@45K, 2.31@55K)
nve_006 = np.array([np.nan, 1.29, 1.61, 2.31, 4.83, np.nan, np.nan, np.nan, np.nan])

# ── Plot ──────────────────────────────────────────────────────────────

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(DOUBLE_WIDTH * 0.65, DOUBLE_WIDTH / GOLDEN),
                                sharex=True, gridspec_kw={"hspace": 0.15, "height_ratios": [2, 1]})

# Top: Eval return
ax1.plot(steps, baseline, "-o", color=COLORS["baseline"], label="Baseline (dt=1)", zorder=5)
ax1.plot(steps, eval_008e_s1, "-v", color=COLORS["mitigation"],
         label="008e_v3: dt=1 imag, seed 1", markerfacecolor="white", zorder=5)
ax1.plot(steps_s2, eval_008e_s2, "--v", color=COLORS["mitigation"], alpha=0.5,
         label="008e_v3: seed 2 (in progress)", markerfacecolor="white", zorder=4)
ax1.plot(steps[:7], eval_006[:7], "-s", color=COLORS["dt2_trained"],
         label="006: dt=2 imag (collapse)", markerfacecolor="white", zorder=4)
ax1.plot(steps, eval_008a, "-^", color=COLORS["dt2_untrained"], alpha=0.5,
         label="008a: untrained dt_emb", markerfacecolor="white", zorder=3)

ax1.annotate("95% baseline", xy=(105, 869.88), xytext=(85, 930),
             fontsize=6, color=COLORS["mitigation"],
             arrowprops=dict(arrowstyle="->", color=COLORS["mitigation"], lw=0.5))
ax1.set_ylabel("Eval Return")
ax1.set_ylim(0, 1000)
ax1.legend(loc="upper left", fontsize=5.5, ncol=2)
ax1.set_title("C6 Mitigation: dt=1 Imagination with Multi-dt Training", fontsize=9)

# Bottom: NVE
ax2.axhspan(1.5, 5.5, color=COLORS["pathological"], alpha=0.07)
ax2.axhline(1.5, color=COLORS["threshold"], ls="--", lw=0.7)
ax2.plot(steps_nve, nve_008e, "-v", color=COLORS["mitigation"],
         label="008e_v3 (dt=1 imag)", markerfacecolor="white")
ax2.plot(steps_nve[:5], nve_006[:5], "-s", color=COLORS["dt2_trained"],
         label="006 (dt=2 imag)", markerfacecolor="white")
ax2.axhline(1.0, color="gray", ls="-", lw=0.3, alpha=0.3)
ax2.set_ylabel("Normalized v/e")
ax2.set_xlabel("Training Steps (×1000)")
ax2.set_ylim(0, 5.5)
ax2.set_xticks([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105])
ax2.legend(fontsize=6)

savefig(fig, "fig6_mitigation")
print("Saved fig6_mitigation.pdf/.png")
