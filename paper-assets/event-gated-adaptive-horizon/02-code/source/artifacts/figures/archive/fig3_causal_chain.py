# Fig 3: Causal chain diagram — mechanism from dt_embedding to collapse.
# Conceptual figure rendered with matplotlib text/arrows (no external deps).
# Paper section: Discussion (mechanism explanation).

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches, matplotlib.patheffects as pe
from fig_style import apply_style, savefig, COLORS, DOUBLE_WIDTH

apply_style()

fig, ax = plt.subplots(figsize=(DOUBLE_WIDTH, 2.0))
ax.set_xlim(0, 10)
ax.set_ylim(0, 2)
ax.axis("off")

box_style = dict(boxstyle="round,pad=0.3", facecolor="#F8F9FA", edgecolor="#2C3E50", lw=0.8)
arrow_kw = dict(arrowstyle="->,head_width=0.15,head_length=0.1",
                color="#2C3E50", lw=1.0, connectionstyle="arc3,rad=0.0")

# Nodes
nodes = [
    (0.8,  1.0, "Trained\ndt_embedding"),
    (2.8,  1.0, "Precise dt\nprediction in\nimagination"),
    (5.0,  1.0, "RSSM fidelity\ngap at dt>1\n(reward gap 2.78×)"),
    (7.2,  1.0, "Pathological\nvalue overestimation\n(nve > 1.5×)"),
    (9.2,  1.0, "Actor\ndegradation\n→ collapse"),
]

for x, y, txt in nodes:
    ax.text(x, y, txt, ha="center", va="center", fontsize=7, bbox=box_style)

# Arrows between boxes
arrow_pairs = [(1.5, 2.0), (3.7, 4.1), (6.0, 6.4), (8.1, 8.5)]
for x0, x1 in arrow_pairs:
    ax.annotate("", xy=(x1, 1.0), xytext=(x0, 1.0), arrowprops=arrow_kw)

# Feedback loop (dashed, from actor degradation back to value overestimation)
ax.annotate("", xy=(7.9, 0.55), xytext=(9.0, 0.55),
            arrowprops=dict(arrowstyle="->", color=COLORS["dt2_trained"],
                            lw=0.8, ls="--", connectionstyle="arc3,rad=-0.3"))
ax.text(8.5, 0.25, "positive\nfeedback", fontsize=5.5, ha="center", color=COLORS["dt2_trained"],
        fontstyle="italic")

# Mitigation annotation
ax.annotate("Mitigation:\nrestrict imag to dt=1",
            xy=(5.0, 0.45), fontsize=6, ha="center", va="top",
            color=COLORS["mitigation"], fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#E8F8F0", edgecolor=COLORS["mitigation"], lw=0.6))
ax.annotate("", xy=(5.0, 0.58), xytext=(5.0, 0.7),
            arrowprops=dict(arrowstyle="-[,widthB=1.5", color=COLORS["mitigation"], lw=0.8))

ax.set_title("Causal Chain: Trained dt_embedding → Delusional Critic → Collapse", fontsize=9, pad=8)

savefig(fig, "fig3_causal_chain")
print("Saved fig3_causal_chain.pdf/.png")
