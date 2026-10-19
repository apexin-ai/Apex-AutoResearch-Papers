"""
Trigger rate vs Δ SR scatter plot (D159 data).
Narrative: monotone positive correlation between trigger rate and effect size.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os

# --- rcParams ---
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 13,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# --- D159 data ---
suites        = ["Spatial", "Goal", "Object", "Long"]
trigger_rates = [20.0,      8.0,    4.0,      4.3]
deltas        = [1.5,       1.1,    0.1,      -1.3]
std_adaptive  = [1.1,       1.5,    3.0,      2.3]
std_vla       = [0.8,       1.3,    1.3,      1.5]
propagated    = [np.sqrt(sa**2 + sv**2) for sa, sv in zip(std_adaptive, std_vla)]

AMBER = "#6BA3C8"
AMBER_TEXT = "#1A5276"
markers = ["o", "s", "d", "^"]

# --- label offsets (hand-tuned for compactness) ---
label_offsets = {
    "Spatial": (-1.2, 0.35),
    "Goal":    (0.8, 0.35),
    "Object":  (0.8, -0.50),
    "Long":    (1.5, -0.50),
}

fig, ax = plt.subplots(figsize=(5.8, 3.2))

# zero line
ax.axhline(y=0, color="#AAAAAA", linestyle="--", linewidth=1.0, zorder=1)
t_zero = ax.text(22.5, 0.15, "no change", fontsize=11, color="#AAAAAA",
                 fontstyle="italic", va="bottom", ha="right")
t_zero.set_path_effects([pe.withStroke(linewidth=2, foreground="white")])

# subtle linear trend line
tr_arr = np.array(trigger_rates)
d_arr = np.array(deltas)
slope, intercept = np.polyfit(tr_arr, d_arr, 1)
x_fit = np.linspace(2, 21.5, 100)
ax.plot(x_fit, slope * x_fit + intercept, color=AMBER, linestyle=":",
        linewidth=1.0, alpha=0.35, zorder=2)

# scatter + error bars
for i, (suite, tr, delta, err) in enumerate(
        zip(suites, trigger_rates, deltas, propagated)):
    ax.errorbar(tr, delta, yerr=err, fmt="none",
                ecolor=AMBER, elinewidth=1.5, capsize=4, capthick=1.2,
                alpha=0.55, zorder=3)
    ax.scatter(tr, delta, s=140, color=AMBER, edgecolors="white",
               linewidths=1.0, marker=markers[i], zorder=5)
    ox, oy = label_offsets[suite]
    ha = "right" if ox < 0 else "left"
    arrow = None
    if suite == "Long":
        arrow = dict(arrowstyle="-", color="#999999", lw=0.5)
    ax.annotate(suite, (tr, delta), fontsize=13, fontweight="bold",
                color="#333333", ha=ha,
                xytext=(tr + ox, delta + oy),
                arrowprops=arrow, zorder=6)

# n.s. text box
ax.text(0.97, 0.03,
        "all suites n.s.\n(p ≥ 0.05, n = 3)",
        transform=ax.transAxes, fontsize=10, color="#666666",
        ha="right", va="bottom",
        bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
                  edgecolor="#CCCCCC", linewidth=0.6, alpha=0.9))

ax.set_xlabel("CRM trigger rate (%)")
ax.set_ylabel("$\\Delta$ SR (pp)\nCRM $\\tau$-gated $-$ VLA-only")
ax.set_xlim(0, 24)
ax.set_ylim(-3.5, 3.5)

plt.tight_layout(pad=0.4)

out_dir = os.path.dirname(os.path.abspath(__file__))
for ext in ["pdf", "png"]:
    path = os.path.join(out_dir, f"fig_trigger_scatter.{ext}")
    fig.savefig(path, dpi=300, bbox_inches="tight")
    print(f"Saved {path}")
plt.close()
