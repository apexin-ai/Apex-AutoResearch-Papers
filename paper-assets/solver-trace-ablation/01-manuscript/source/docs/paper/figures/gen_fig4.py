#!/usr/bin/env python3
"""Cross-logic: FOL vs Prolog exec-only ISR* + Prolog gaming modes (side-by-side)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 10,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "xtick.major.size": 3,
    "ytick.major.size": 3,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

C_FOL = "#5889B0"
C_PROLOG = "#9CBDD8"
C_FOL_TEXT = "#4A7898"
C_PROLOG_TEXT = "#7AA4C0"

C_TS = "#B8605A"
C_DEGEN = "#D4ACA8"
C_QUERY = "#B0B8C0"

seeds = ["s42", "s43", "s44"]
x = np.arange(len(seeds))
bar_w = 0.28

fol_isr = [0.132, 0.000, 0.582]
prolog_isr = [0.037, 0.015, 0.387]
fol_pr = [93, 13, 98]
prolog_pr = [83, 56, 21]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.4),
                                gridspec_kw={"width_ratios": [1, 1], "wspace": 0.15})
stroke = [pe.withStroke(linewidth=2.5, foreground="white")]

# ── Panel (a): Exec-only ISR* ──
b1 = ax1.bar(x - bar_w / 2, fol_isr, bar_w, color=C_FOL, label="FOL",
             edgecolor="white", linewidth=0.4, zorder=3)
b2 = ax1.bar(x + bar_w / 2, prolog_isr, bar_w, color=C_PROLOG, label="Prolog",
             edgecolor="white", linewidth=0.4, zorder=3)

ax1.yaxis.grid(True, alpha=0.12, linewidth=0.4, zorder=0)

pr_y_fol = [0.018, 0.10, 0.018]
pr_y_prolog = [0.018, 0.018, 0.018]

for i, (bar, pr) in enumerate(zip(b1, fol_pr)):
    label = f"{pr}%" + ("†" if i == 1 else "")
    bx = bar.get_x() + bar.get_width() / 2
    by = max(bar.get_height(), 0.005) + pr_y_fol[i]
    t = ax1.text(bx, by, label, ha="center", va="bottom",
                 fontsize=6.5, color=C_FOL_TEXT)
    t.set_path_effects(stroke)

for i, (bar, pr) in enumerate(zip(b2, prolog_pr)):
    bx = bar.get_x() + bar.get_width() / 2
    by = bar.get_height() + pr_y_prolog[i]
    if i == 2:
        t = ax1.text(bx, by + 0.03, f"{pr}%",
                     ha="center", va="bottom",
                     fontsize=6.5, color=C_PROLOG_TEXT)
        t.set_path_effects(stroke)
        t2 = ax1.text(bx, by, f"($n$=21)",
                      ha="center", va="bottom",
                      fontsize=5.5, color=C_PROLOG_TEXT, alpha=0.8)
        t2.set_path_effects(stroke)
    else:
        t = ax1.text(bx, by, f"{pr}%", ha="center", va="bottom",
                     fontsize=6.5, color=C_PROLOG_TEXT)
        t.set_path_effects(stroke)

ax1.set_xticks(x)
ax1.set_xticklabels(seeds)
ax1.set_ylabel("ISR* (exec-only)")
ax1.set_ylim(0, 0.75)
ax1.set_yticks(np.arange(0, 0.8, 0.1))
ax1.legend(fontsize=7.5, loc="upper left", frameon=False)
ax1.set_title("(a) Exec-only ISR*: FOL vs Prolog", fontsize=9,
              loc="left", pad=4)
ax1.set_xlim(-0.5, 2.5)

# ── Panel (b): Prolog Gaming Modes ──
bw2 = bar_w
mode_colors = [C_TS, C_DEGEN, C_QUERY]
mode_labels = ["TS tautol.", "Degen. syntax", "Query as-fact"]

for i in range(3):
    ax2.bar(x[i], 100, bw2, color=mode_colors[i], edgecolor="white",
            linewidth=0.4, zorder=3)
    ax2.text(x[i], 103, mode_labels[i], ha="center", va="bottom",
             fontsize=6.5, color=mode_colors[i], fontweight="medium")

ax2.yaxis.grid(True, alpha=0.12, linewidth=0.4, zorder=0)
ax2.set_xticks(x)
ax2.set_xticklabels(seeds)
ax2.set_ylabel("Percentage (%)")
ax2.set_ylim(0, 118)
ax2.set_yticks([0, 50, 100])
ax2.set_title("(b) Prolog gaming modes", fontsize=9, loc="left", pad=4)
ax2.set_xlim(-0.5, 2.5)

out_base = "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/fig4_prolog_comparison"
fig.savefig(f"{out_base}.pdf", dpi=300, bbox_inches="tight", pad_inches=0.05)
fig.savefig(f"{out_base}.png", dpi=300, bbox_inches="tight", pad_inches=0.05)
plt.close()
print(f"Saved: {out_base}.pdf and .png")
