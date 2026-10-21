#!/usr/bin/env python3
"""Scatter plot: Degeneracy Rate vs LP Selection Delta F1."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats

with open("/root/autodl-tmp/struct_self_consist_ie/output/scatter_v2_data.json") as f:
    data = json.load(f)

CATEGORY_STYLE = {
    "cross-dataset":  {"marker": "o", "color": "#1976D2", "size": 120, "label": "Qwen3-8B (canonical)", "zorder": 5},
    "multi-seed":     {"marker": "o", "color": "#90CAF9", "size": 60,  "label": "Qwen3-8B (multi-seed)", "zorder": 4},
    "LLaMA3.1-8B":   {"marker": "s", "color": "#E64A19", "size": 80,  "label": "LLaMA3.1-8B", "zorder": 4},
    "epoch":          {"marker": "^", "color": "#388E3C", "size": 80,  "label": "Epoch ablation", "zorder": 4},
    "rank":           {"marker": "D", "color": "#7B1FA2", "size": 70,  "label": "Rank ablation", "zorder": 4},
    "temperature":    {"marker": "v", "color": "#F57C00", "size": 80,  "label": "Temperature ablation", "zorder": 4},
    "Qwen3-4B":       {"marker": "P", "color": "#00796B", "size": 80,  "label": "Qwen3-4B", "zorder": 4},
}

fig, ax = plt.subplots(figsize=(7, 4.8))

all_x, all_y = [], []
for cat_name, style in CATEGORY_STYLE.items():
    points = [p for p in data if p["category"] == cat_name]
    if not points:
        continue
    xs = [p["degen_pct"] for p in points]
    ys = [p["lp_delta_pp"] for p in points]
    ax.scatter(xs, ys, marker=style["marker"], c=style["color"],
               s=style["size"], label=style["label"],
               edgecolors="black", linewidths=0.4, zorder=style["zorder"], alpha=0.85)
    all_x.extend(xs)
    all_y.extend(ys)

# Trend line
all_x = np.array(all_x)
all_y = np.array(all_y)
slope, intercept, r_val, p_val_lr, se = stats.linregress(all_x, all_y)
x_line = np.linspace(min(all_x) - 2, max(all_x) + 2, 200)
ax.plot(x_line, slope * x_line + intercept, 'k--', alpha=0.35, linewidth=1, zorder=2)

# Spearman
rho, p_val = stats.spearmanr(all_x, all_y)

# Zero line
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3, linewidth=0.5, zorder=1)

ax.set_xlabel('Degeneracy Rate (%)', fontsize=11)
ax.set_ylabel('LP Selection $\\Delta$F1 (pp)', fontsize=11)
ax.tick_params(labelsize=9)

# Legend
ax.legend(fontsize=7.5, loc='upper left', framealpha=0.9, edgecolor='0.8',
          handletextpad=0.4, borderpad=0.4, labelspacing=0.3)

# Annotation
ax.annotate(f'Spearman $\\rho$ = {rho:.3f} (p = {p_val:.4f})\n'
            f'n = {len(all_x)} conditions',
            xy=(0.98, 0.02), xycoords='axes fraction', fontsize=8.5,
            ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='0.8', alpha=0.9))

plt.tight_layout()

outdir = "/root/autodl-tmp/struct_self_consist_ie/output/figures"
import os
os.makedirs(outdir, exist_ok=True)
plt.savefig(f"{outdir}/fig_degeneracy_lp_scatter_v2.pdf", dpi=300, bbox_inches='tight')
plt.savefig(f"{outdir}/fig_degeneracy_lp_scatter_v2.png", dpi=150, bbox_inches='tight')
print(f"Saved to {outdir}/fig_degeneracy_lp_scatter_v2.{{pdf,png}}")
print(f"\nSpearman rho={rho:.4f}, p={p_val:.6f}")
print(f"Linear: slope={slope:.4f}, intercept={intercept:.4f}, R^2={r_val**2:.4f}")
print(f"N data points: {len(all_x)}")
