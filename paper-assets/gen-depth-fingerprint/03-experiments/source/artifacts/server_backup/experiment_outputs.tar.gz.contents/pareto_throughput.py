"""Pareto frontier scatter plot: Accuracy vs Throughput."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

RESULTS_DIR = Path("/root/gen-depth-fingerprint/results")

methods = {
    "7-Feature (Ours)": {"ms": 9.7, "binary_f1": 0.6935, "3class_f1": 0.7616,
                          "marker": "*", "color": "#D62728", "size": 280, "zorder": 5},
    "4-Det Ensemble":   {"ms": 22.8, "binary_f1": 0.6993, "3class_f1": 0.779,
                          "marker": "D", "color": "#1F77B4", "size": 90, "zorder": 4},
    "4-Det+Surface":    {"ms": 22.8, "binary_f1": 0.7044, "3class_f1": 0.7823,
                          "marker": "D", "color": "#2CA02C", "size": 90, "zorder": 4},
    "AvgLogProb":       {"ms": 8.58, "binary_f1": 0.6785, "3class_f1": 0.7085,
                          "marker": "o", "color": "#9467BD", "size": 60, "zorder": 3},
    "FastDetectGPT":    {"ms": 8.58, "binary_f1": 0.5805, "3class_f1": 0.6654,
                          "marker": "o", "color": "#8C564B", "size": 60, "zorder": 3},
    "Binoculars":       {"ms": 22.17, "binary_f1": 0.5327, "3class_f1": 0.4094,
                          "marker": "o", "color": "#E377C2", "size": 60, "zorder": 3},
    "LD-Score":         {"ms": 0.61, "binary_f1": 0.6788, "3class_f1": 0.6326,
                          "marker": "^", "color": "#FF7F0E", "size": 80, "zorder": 3},
}

def pareto_frontier(points):
    sorted_idx = sorted(range(len(points)), key=lambda i: points[i][0])
    frontier = []
    max_f1 = -1
    for i in sorted_idx:
        if points[i][1] > max_f1:
            frontier.append(i)
            max_f1 = points[i][1]
    return frontier

names = list(methods.keys())
pts_binary = [(methods[n]["ms"], methods[n]["binary_f1"]) for n in names]
frontier_idx = pareto_frontier(pts_binary)
frontier_names = [names[i] for i in frontier_idx]
frontier_pts = sorted([(methods[n]["ms"], methods[n]["binary_f1"]) for n in frontier_names])

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
})

fig, ax = plt.subplots(figsize=(5.5, 4.2))

# Pareto frontier line
fx = [p[0] for p in frontier_pts]
fy = [p[1] for p in frontier_pts]
ax.plot(fx, fy, '--', color='#AAAAAA', alpha=0.6, linewidth=1.0, zorder=1)

# Scatter
for name, d in methods.items():
    ax.scatter(d["ms"], d["binary_f1"], marker=d["marker"], c=d["color"],
               s=d["size"], edgecolors='black', linewidths=0.5, zorder=d["zorder"],
               label=name)

# Annotations with arrow connectors for crowded region
annot_cfg = {
    "7-Feature (Ours)":  {"xy_text": (13.5, 0.716), "fontweight": "bold", "fontsize": 8.5},
    "4-Det Ensemble":    {"xy_text": (14.0, 0.675), "fontweight": "normal", "fontsize": 7.5},
    "4-Det+Surface":     {"xy_text": (17.5, 0.724), "fontweight": "normal", "fontsize": 7.5},
    "AvgLogProb":        {"xy_text": (1.5, 0.650), "fontweight": "normal", "fontsize": 7.5},
    "FastDetectGPT":     {"xy_text": (10.5, 0.570), "fontweight": "normal", "fontsize": 7.5},
    "Binoculars":        {"xy_text": (14.5, 0.520), "fontweight": "normal", "fontsize": 7.5},
    "LD-Score":          {"xy_text": (-1.5, 0.705), "fontweight": "normal", "fontsize": 7.5},
}

for name, d in methods.items():
    cfg = annot_cfg[name]
    ax.annotate(name,
                xy=(d["ms"], d["binary_f1"]),
                xytext=cfg["xy_text"],
                fontsize=cfg["fontsize"],
                fontweight=cfg["fontweight"],
                color=d["color"],
                arrowprops=dict(arrowstyle='-', color='#CCCCCC', linewidth=0.6),
                zorder=2)

ax.set_xlabel("Latency (ms / text)")
ax.set_ylabel("Binary F1 (pooled, 8 generators)")
ax.set_title("Accuracy vs. Throughput")
ax.set_xlim(-3, 27)
ax.set_ylim(0.50, 0.74)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.text(0.98, 0.02, "RTX 5090, FP16, avg seq len $\\approx$ 237",
        transform=ax.transAxes, fontsize=7, ha='right', va='bottom',
        color='gray', style='italic')

plt.tight_layout()
out_pdf = RESULTS_DIR / "fig_appendix_pareto.pdf"
out_png = RESULTS_DIR / "fig_appendix_pareto.png"
plt.savefig(out_pdf, dpi=300, bbox_inches='tight')
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"Saved: {out_pdf}")
print(f"Saved: {out_png}")

print(f"\nPareto frontier: {frontier_names}")
print(f"\n{'Method':<20s} {'ms/text':>8s} {'Binary F1':>10s} {'3-class F1':>11s} {'Pareto':>7s}")
print("-" * 60)
for name in names:
    d = methods[name]
    p = "  *" if name in frontier_names else ""
    print(f"{name:<20s} {d['ms']:>8.2f} {d['binary_f1']:>10.4f} {d['3class_f1']:>11.4f}{p}")
print(f"\nSpeedup: 7-Feature is {22.8/9.7:.1f}x faster than 4-Det+Surface, F1 gap = {0.7044-0.6935:.4f}")
