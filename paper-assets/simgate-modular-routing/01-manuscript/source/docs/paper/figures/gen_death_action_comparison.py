"""Generate death_action_comparison figure: Internal vs Deterministic.

Dual panel showing non-connect action distribution for both strategies.
Data: Internal exact from analysis output; Deterministic approximate from figure.
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
    "focus on [X]": "focus on",
    "connect [X] to [Y]": "connect",
    "disconnect [X]": "disconnect",
    "move [X] to [Y]": "move",
    "movement": "movement",
    "object interaction": "obj. int.",
    "observation": "obs.",
    "other": "other",
}

STRATEGIES = {
    "Internal (LLM)": {
        "n_death": 105,
        "n_alive": 140,
        "death_pct": {
            "focus on [X]": 5.4, "connect [X] to [Y]": 82.0,
            "disconnect [X]": 1.8, "move [X] to [Y]": 0.0,
            "movement": 0.0, "object interaction": 3.4,
            "observation": 7.1, "other": 0.3,
        },
        "alive_pct": {
            "focus on [X]": 3.4, "connect [X] to [Y]": 72.0,
            "disconnect [X]": 4.3, "move [X] to [Y]": 0.0,
            "movement": 0.0, "object interaction": 13.1,
            "observation": 5.6, "other": 1.6,
        },
    },
    "Deterministic": {
        "n_death": 40,
        "n_alive": 205,
        "death_pct": {
            "focus on [X]": 5.2, "connect [X] to [Y]": 74.0,
            "disconnect [X]": 3.5, "move [X] to [Y]": 0.4,
            "movement": 0.3, "object interaction": 6.0,
            "observation": 10.3, "other": 0.3,
        },
        "alive_pct": {
            "focus on [X]": 3.0, "connect [X] to [Y]": 76.0,
            "disconnect [X]": 4.5, "move [X] to [Y]": 0.7,
            "movement": 0.3, "object interaction": 7.5,
            "observation": 6.5, "other": 1.5,
        },
    },
}

fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.6), sharey=False)

for idx, (label, data) in enumerate(STRATEGIES.items()):
    ax = axes[idx]
    cats_zoom = [c for c in CAT_ORDER
                 if c != "connect [X] to [Y]" and
                 (data["death_pct"].get(c, 0) > 0 or data["alive_pct"].get(c, 0) > 0)]

    d_vals = [data["death_pct"][c] for c in cats_zoom]
    a_vals = [data["alive_pct"][c] for c in cats_zoom]

    x = np.arange(len(cats_zoom))
    w = 0.35

    ax.bar(x - w/2, d_vals, w, color=paper_style.C_DETERMINISTIC, alpha=0.88,
           label=f"Death (n={data['n_death']})", **paper_style.bar_edge_style())
    ax.bar(x + w/2, a_vals, w, color=paper_style.C_INTERNAL, alpha=0.88,
           label=f"Non-death (n={data['n_alive']})", **paper_style.bar_edge_style())

    ax.set_xticks(x)
    ax.set_xticklabels([CAT_SHORT[c] for c in cats_zoom], fontsize=5.5,
                        rotation=30, ha='right')
    ax.set_title(label, fontsize=9)
    paper_style.add_y_grid(ax)
    leg = ax.legend(fontsize=5.5, loc="upper right")
    paper_style.style_legend(leg)

    d_conn = data["death_pct"]["connect [X] to [Y]"]
    a_conn = data["alive_pct"]["connect [X] to [Y]"]
    ax.text(0.02, 0.95,
            f"connect: {d_conn:.0f}% (death) / {a_conn:.0f}% (non-death)",
            transform=ax.transAxes, fontsize=5, va="top",
            fontstyle="italic", color="#555555")

axes[0].set_ylabel("Proportion of actions (%)")

plt.tight_layout(pad=0.3)

out_dir = os.path.dirname(os.path.abspath(__file__))
for ext in ("pdf", "png"):
    path = os.path.join(out_dir, f"death_action_comparison.{ext}")
    fig.savefig(path, format=ext if ext == "png" else None,
                dpi=300, bbox_inches="tight", pad_inches=0.08)
    print(f"Saved: {path} ({os.path.getsize(path)} bytes)")
plt.close()
