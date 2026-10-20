"""Generate death_action_distribution figure: Internal strategy action distribution.

Dual panel: (a) full action distribution, (b) non-connect zoomed.
Data from death taxonomy analysis (245 episodes, 11 tasks).
"""
import paper_style; paper_style.apply_style()
import matplotlib.pyplot as plt
import numpy as np
import os

CAT_ORDER = [
    "focus on [X]", "connect [X] to [Y]", "disconnect [X]",
    "move [X] to [Y]", "movement", "object interaction", "observation", "other",
]
CAT_SHORT = {
    "focus on [X]": "focus on\n[X]",
    "connect [X] to [Y]": "connect\n[X] to [Y]",
    "disconnect [X]": "disconnect\n[X]",
    "move [X] to [Y]": "move [X]\nto [Y]",
    "movement": "movement",
    "object interaction": "object\ninteraction",
    "observation": "observation",
    "other": "other",
}

N_DEATH = 105
N_ALIVE = 140

# Internal strategy action category distribution (exact from analysis output)
DEATH_PCT = {
    "focus on [X]":        5.4,
    "connect [X] to [Y]": 82.0,
    "disconnect [X]":      1.8,
    "move [X] to [Y]":     0.0,
    "movement":            0.0,
    "object interaction":  3.4,
    "observation":         7.1,
    "other":               0.3,
}
ALIVE_PCT = {
    "focus on [X]":        3.4,
    "connect [X] to [Y]": 72.0,
    "disconnect [X]":      4.3,
    "move [X] to [Y]":     0.0,
    "movement":            0.0,
    "object interaction": 13.1,
    "observation":         5.6,
    "other":               1.6,
}

cats_all = [c for c in CAT_ORDER if DEATH_PCT.get(c, 0) > 0 or ALIVE_PCT.get(c, 0) > 0]
d_vals_all = [DEATH_PCT[c] for c in cats_all]
a_vals_all = [ALIVE_PCT[c] for c in cats_all]

fig, (ax_full, ax_zoom) = plt.subplots(1, 2, figsize=(6.5, 2.4))

x = np.arange(len(cats_all))
w = 0.35

ax_full.bar(x - w/2, d_vals_all, w, color=paper_style.C_DETERMINISTIC, alpha=0.88,
            label=f"Death (n={N_DEATH})", **paper_style.bar_edge_style())
ax_full.bar(x + w/2, a_vals_all, w, color=paper_style.C_INTERNAL, alpha=0.88,
            label=f"Non-death (n={N_ALIVE})", **paper_style.bar_edge_style())
ax_full.set_xticks(x)
ax_full.set_xticklabels([CAT_SHORT[c] for c in cats_all], fontsize=6)
ax_full.set_ylabel("Proportion of actions (%)")
ax_full.set_title("(a) Full action distribution", fontsize=9)
paper_style.add_y_grid(ax_full)
leg1 = ax_full.legend(fontsize=6, loc="upper right")
paper_style.style_legend(leg1)

cats_zoom = [c for c in cats_all if c != "connect [X] to [Y]"]
d_vals_zoom = [DEATH_PCT[c] for c in cats_zoom]
a_vals_zoom = [ALIVE_PCT[c] for c in cats_zoom]
x2 = np.arange(len(cats_zoom))

ax_zoom.bar(x2 - w/2, d_vals_zoom, w, color=paper_style.C_DETERMINISTIC, alpha=0.88,
            label=f"Death (n={N_DEATH})", **paper_style.bar_edge_style())
ax_zoom.bar(x2 + w/2, a_vals_zoom, w, color=paper_style.C_INTERNAL, alpha=0.88,
            label=f"Non-death (n={N_ALIVE})", **paper_style.bar_edge_style())
ax_zoom.set_xticks(x2)
ax_zoom.set_xticklabels([CAT_SHORT[c] for c in cats_zoom], fontsize=6)
ax_zoom.set_title("(b) Non-connect actions (zoomed)", fontsize=9)
paper_style.add_y_grid(ax_zoom)
leg2 = ax_zoom.legend(fontsize=6, loc="upper right")
paper_style.style_legend(leg2)

ax_zoom.text(0.02, 0.95,
             f"connect: {DEATH_PCT['connect [X] to [Y]']:.0f}% (death) / "
             f"{ALIVE_PCT['connect [X] to [Y]']:.0f}% (non-death)",
             transform=ax_zoom.transAxes, fontsize=5.5, va="top",
             fontstyle="italic", color="#555555")

plt.tight_layout(pad=0.3)

out_dir = os.path.dirname(os.path.abspath(__file__))
for ext in ("pdf", "png"):
    path = os.path.join(out_dir, f"death_action_distribution.{ext}")
    fig.savefig(path, format=ext if ext == "png" else None,
                dpi=300, bbox_inches="tight", pad_inches=0.08)
    print(f"Saved: {path} ({os.path.getsize(path)} bytes)")
plt.close()
