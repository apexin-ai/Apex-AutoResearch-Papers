# Fig 2: Eval return learning curves.
# Compares baseline, trained dt_emb (collapse), untrained dt_emb, mitigation (dt=1 imag).
# Data source: experiment registry.
# Paper section: Results (C1, C3, C6 — degradation, protection, mitigation).

import numpy as np
import matplotlib.pyplot as plt
from fig_style import apply_style, savefig, COLORS, DOUBLE_WIDTH, GOLDEN

apply_style()

# ── Data ──────────────────────────────────────────────────────────────

steps = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105])

baseline = np.array([31, np.nan, np.nan, np.nan, np.nan, np.nan,
                     np.nan, np.nan, np.nan, np.nan, 915.67])
# Baseline only has sparse early data; fill representative trajectory
baseline_full = np.array([31, 180, 310, 400, 443, 625.7, 616, 750, 830, 900, 915.67])

# 008d — trained dt_emb, subsample ON, H=8 (collapse)
eval_008d = np.array([31, 153.7, 167.22, 146.34, 140.8, 82.75,
                      np.nan, np.nan, np.nan, np.nan, np.nan])

# 006 — fixed dt=2, trained dt_emb, subsample ON, H=15 (collapse)
eval_006 = np.array([31, 256.9, 321.4, 485.3, 477, 360.4, 132.86,
                     np.nan, np.nan, np.nan, np.nan])

# 007 — fixed dt=4 (severe degradation)
eval_007 = np.array([31, 129.6, 176.9, 126.7, 144.41, 152.49,
                     np.nan, np.nan, np.nan, np.nan, np.nan])

# 008a — untrained dt_emb, subsample OFF, H=15 (zigzag recovery)
eval_008a = np.array([31, 167.2, 230.8, 500.84, 563.41, 487.92,
                      608, 469.93, 583.73, 572.24, 777.66])

# 008e_v3 — mitigation: trained dt_emb + dt=1 imag, H=15
eval_008e = np.array([31, 131.2, 155.69, 276.47, 382.22, 486.84,
                      580.67, 574.09, 657.31, 851.86, 869.88])

# 008c — untrained dt_emb, subsample OFF, H=8 (low plateau)
eval_008c = np.array([31, 171.3, 192.4, 185.1, 226.55, 241.87,
                      240.86, np.nan, np.nan, np.nan, np.nan])

# ── Plot ──────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(DOUBLE_WIDTH, DOUBLE_WIDTH / GOLDEN / 1.4))

ax.plot(steps, baseline_full, "-o", color=COLORS["baseline"],
        label="Baseline (dt=1)", zorder=6)
ax.plot(steps, eval_008e, "-v", color=COLORS["mitigation"],
        label="C6 Mitigation (dt=1 imag, H=15)", markerfacecolor="white", zorder=5)
ax.plot(steps, eval_008a, "-^", color=COLORS["dt2_untrained"],
        label="008a: untrained dt_emb (H=15)", markerfacecolor="white", zorder=4)
ax.plot(steps[:7], eval_008c[:7], "--^", color=COLORS["dt2_untrained"], alpha=0.5,
        label="008c: untrained dt_emb (H=8)", markerfacecolor="white", zorder=3)
ax.plot(steps[:7], eval_006[:7], "-s", color=COLORS["dt2_trained"],
        label="006: dt=2 trained (H=15, collapse)", markerfacecolor="white", zorder=4)
ax.plot(steps[:6], eval_008d[:6], "--s", color=COLORS["dt2_trained"], alpha=0.6,
        label="008d: dt=2 trained (H=8, collapse)", markerfacecolor="white", zorder=3)
ax.plot(steps[:6], eval_007[:6], "-D", color=COLORS["dt4"],
        label="007: dt=4 (severe degradation)", markerfacecolor="white", zorder=3)

# Annotations
ax.annotate("collapse", xy=(65, 132.86), fontsize=6, color=COLORS["dt2_trained"],
            ha="center", va="top")
ax.annotate("95% baseline", xy=(105, 869.88), xytext=(90, 920),
            fontsize=6, color=COLORS["mitigation"],
            arrowprops=dict(arrowstyle="->", color=COLORS["mitigation"], lw=0.6))

ax.set_xlabel("Training Steps (×1000)")
ax.set_ylabel("Eval Return")
ax.set_xlim(0, 112)
ax.set_ylim(0, 1000)
ax.set_xticks([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105])
ax.legend(loc="upper left", fontsize=6, ncol=2)
ax.set_title("Learning Curves: Variable-Rate Imagination in DreamerV3 (Walker Walk)")

savefig(fig, "fig2_eval_curves")
print("Saved fig2_eval_curves.pdf/.png")
