"""Generate death_action_timeline figure (Figure 4): representative death episodes.

Horizontal stacked bar showing action sequences of 6 death episodes (Internal).
Fatal step marked with red border + red pin marker above bar (no overlap).
"""
import paper_style; paper_style.apply_style()
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle
from matplotlib.lines import Line2D
import os

COLORS = {
    "focus on [X]":        paper_style.C_ACCENT,
    "connect [X] to [Y]": paper_style.C_INTERNAL,
    "disconnect [X]":      paper_style.C_PURPLE,
    "observation":         paper_style.C_NEUTRAL,
    "object interaction":  paper_style.C_GREEN,
    "movement":            paper_style.C_DEATH_SCORE,
    "move [X] to [Y]":    paper_style.C_DETERMINISTIC,
    "other":               '#D9D9D9',
}

C_FATAL = '#C0392B'

C = "connect [X] to [Y]"
F = "focus on [X]"
O = "observation"
D = "disconnect [X]"
OI = "object interaction"

EPISODES = [
    {"task": "chem-mix",       "cats": [O] + [C]*13 + [O, F, F], "fatal_idx": 15},
    {"task": "freeze",         "cats": [O] + [C]*13 + [D, F, F], "fatal_idx": 16},
    {"task": "find-animal",    "cats": [O] + [C]*14 + [F, F],    "fatal_idx": 16},
    {"task": "life-stages-1",  "cats": [O] + [C]*14 + [F, F],    "fatal_idx": 16},
    {"task": "incl-plane",     "cats": [O] + [C]*14 + [F, F],    "fatal_idx": 16},
    {"task": "lifespan-long",  "cats": [O] + [C]*15 + [F, F],    "fatal_idx": 17},
]

max_steps = max(len(ep["cats"]) for ep in EPISODES)
bar_h = 0.6

fig, ax = plt.subplots(figsize=(3.4, 2.0))

for y, ep in enumerate(EPISODES):
    for x_pos, cat in enumerate(ep["cats"]):
        is_fatal = (x_pos == ep["fatal_idx"])
        rect = Rectangle(
            (x_pos, y - bar_h/2), 1, bar_h,
            facecolor=COLORS[cat],
            edgecolor=C_FATAL if is_fatal else "none",
            linewidth=1.2 if is_fatal else 0,
            zorder=3 if is_fatal else 1,
        )
        ax.add_patch(rect)

    fx = ep["fatal_idx"] + 0.5
    bar_top = y + bar_h/2
    pin_top = bar_top + 0.45
    ax.plot([fx, fx], [bar_top + 0.04, pin_top - 0.08],
            color=C_FATAL, linewidth=0.6, zorder=4)
    ax.plot(fx, pin_top, marker='v', markersize=3.5, color=C_FATAL,
            markeredgecolor=C_FATAL, markeredgewidth=0, zorder=5)

ax.set_xlim(-0.5, max_steps + 0.5)
ax.set_ylim(-0.55, len(EPISODES) + 0.15)
ax.set_yticks(range(len(EPISODES)))
ax.set_yticklabels([ep["task"] for ep in EPISODES], fontsize=6)
ax.set_xlabel("Step number")

legend_cats = ["focus on [X]", "connect [X] to [Y]", "disconnect [X]",
               "observation", "object interaction"]
legend_elements = [Patch(facecolor=COLORS[c], label=c) for c in legend_cats]
legend_elements.append(Line2D([0], [0], marker='v', color=C_FATAL,
                               markerfacecolor=C_FATAL, markeredgecolor=C_FATAL,
                               markersize=3.5, linewidth=0.6, label='fatal step'))
leg = ax.legend(handles=legend_elements, fontsize=4.5,
                loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=3,
                borderpad=0.3, handletextpad=0.3, columnspacing=0.6,
                frameon=True)
paper_style.style_legend(leg)

plt.tight_layout(pad=0.3)

out_dir = os.path.dirname(os.path.abspath(__file__))
for ext in ("pdf", "png"):
    path = os.path.join(out_dir, f"death_action_timeline.{ext}")
    fig.savefig(path, format=ext if ext == "png" else None,
                dpi=300, bbox_inches="tight", pad_inches=0.08)
    print(f"Saved: {path} ({os.path.getsize(path)} bytes)")
plt.close()
