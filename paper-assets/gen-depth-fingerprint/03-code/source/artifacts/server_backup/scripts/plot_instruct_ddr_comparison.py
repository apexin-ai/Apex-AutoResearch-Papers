#!/usr/bin/env python3
"""Appendix figure: Base vs Instruct DDR partition comparison (|Cohen's d|)."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif", "Nimbus Roman"],
    "font.size": 10,
    "axes.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "mathtext.fontset": "cm",
})

with open("/root/gen-depth-fingerprint/results/instruct_analysis_summary.json") as f:
    data = json.load(f)

MODELS = ["Qwen3-1.7B", "OLMo-2-1B", "Llama-3.2-3B"]
MODEL_MARKERS = {"Qwen3-1.7B": "o", "OLMo-2-1B": "s", "Llama-3.2-3B": "D"}

FEATURES = [
    ("hapax_ratio",  "Drifting"),
    ("ttr",          "Drifting"),
    ("entropy_mean", "Drifting"),
    ("entropy_std",  "Intermediate"),
    ("entropy_min",  "Near-stationary"),
    ("entropy_max",  "Near-stationary"),
    ("tail_decay",   "Near-stationary"),
]

FEAT_LABELS = {
    "entropy_mean": r"$\bar{H}$ (Ent. Mean)",
    "entropy_std":  r"$\sigma_H$ (Ent. Std)",
    "entropy_min":  r"$H_{\min}$ (Ent. Min)",
    "entropy_max":  r"$H_{\max}$ (Ent. Max)",
    "ttr":          "TTR",
    "hapax_ratio":  "Hapax Ratio",
    "tail_decay":   "Tail Decay",
}

ZONE_COLORS = {
    "Drifting":        "#2ca02c",
    "Intermediate":    "#9467bd",
    "Near-stationary": "#ff7f0e",
}

n = len(FEATURES)

def extract_abs_d(condition):
    """Extract |Cohen's d| per feature per model for a condition ('base' or 'instruct')."""
    per_model = {}
    for m in MODELS:
        per_model[m] = {feat: abs(data[m][condition]["cohens_d"][feat])
                        for feat, _ in FEATURES}
    medians = {}
    for feat, _ in FEATURES:
        vals = [per_model[m][feat] for m in MODELS]
        medians[feat] = float(np.median(vals))
    return per_model, medians


base_per_model, base_median = extract_abs_d("base")
inst_per_model, inst_median = extract_abs_d("instruct")

fig, (ax_base, ax_inst) = plt.subplots(1, 2, figsize=(6.0, 3.2),
                                        sharey=True, gridspec_kw={"wspace": 0.08})
rng = np.random.default_rng(42)

def draw_panel(ax, medians, per_model, title, sil):
    for i, (feat, zone) in enumerate(FEATURES):
        y = n - 1 - i
        val = medians[feat]
        ax.barh(y, val, color=ZONE_COLORS[zone], height=0.55, alpha=0.82, zorder=2)
        for m in MODELS:
            mv = per_model[m][feat]
            jit = rng.uniform(-0.12, 0.12)
            ax.scatter(mv, y + jit, marker=MODEL_MARKERS[m],
                       color="#444444", s=18, alpha=0.7, zorder=3, edgecolors="none")

    ax.set_xlabel(r"|Cohen's $d$|  (depth 0 vs 4)", fontsize=9)
    ax.xaxis.grid(True, color="#eeeeee", linewidth=0.5, zorder=0)
    ax.set_xlim(-0.02, 1.35)
    ax.set_ylim(-0.5, n - 0.5)
    ax.set_title(title, fontsize=9.5, fontweight="bold", pad=6)
    ax.text(0.97, 0.03, f"Silhouette = {sil:.3f}",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=7.5, fontstyle="italic",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#cccccc", alpha=0.9))

draw_panel(ax_base, base_median, base_per_model, "Base Models", 0.660)
draw_panel(ax_inst, inst_median, inst_per_model, "Instruct Models", 0.338)

yticks = list(range(n))
ylabels = [FEAT_LABELS[FEATURES[n - 1 - i][0]] for i in range(n)]
ax_base.set_yticks(yticks)
ax_base.set_yticklabels(ylabels, fontsize=8)

zone_patches = [
    mpatches.Patch(color="#2ca02c", alpha=0.82, label="Drifting"),
    mpatches.Patch(color="#9467bd", alpha=0.82, label="Intermediate"),
    mpatches.Patch(color="#ff7f0e", alpha=0.82, label="Near-stationary"),
]
model_handles = [
    plt.Line2D([], [], marker=MODEL_MARKERS[m], color="#444444", linestyle="None",
               markersize=4.5, label=m)
    for m in MODELS
]
ax_inst.legend(handles=zone_patches + model_handles, loc="center right",
               fontsize=6.5, frameon=True, framealpha=0.9,
               edgecolor="#cccccc", fancybox=False,
               handletextpad=0.4, borderpad=0.4)

outdir = Path("/root/gen-depth-fingerprint/results")
fig.savefig(outdir / "fig_appendix_instruct_ddr.pdf",
            bbox_inches="tight", dpi=300, pad_inches=0.03)
fig.savefig(outdir / "fig_appendix_instruct_ddr.png",
            bbox_inches="tight", dpi=300, pad_inches=0.03)

print("=== Base |Cohen's d| (median) ===")
for feat, zone in FEATURES:
    vals = [base_per_model[m][feat] for m in MODELS]
    print(f"  {feat:15s}  med={base_median[feat]:.4f}  [{', '.join(f'{v:.4f}' for v in vals)}]  {zone}")

print("\n=== Instruct |Cohen's d| (median) ===")
for feat, zone in FEATURES:
    vals = [inst_per_model[m][feat] for m in MODELS]
    print(f"  {feat:15s}  med={inst_median[feat]:.4f}  [{', '.join(f'{v:.4f}' for v in vals)}]  {zone}")

print("\nSaved fig_appendix_instruct_ddr.pdf + .png")
