#!/usr/bin/env python3
"""Generate Fig 2: Layer-wise Probe Accuracy Curves (Llama-3.1, Qwen-3, Gemma-2)."""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path(__file__).parent / "layerwise_probe_curves.json"
OUT_DIR = Path(__file__).parent.parent / "figures" / "paper"
OUT_DIR.mkdir(parents=True, exist_ok=True)

with open(DATA_PATH) as f:
    data = json.load(f)

# --- helpers ---
DIR_LABELS = {
    "en_en": r"EN$\rightarrow$EN",
    "zh_zh": r"ZH$\rightarrow$ZH",
    "en_zh": r"EN$\rightarrow$ZH",
    "zh_en": r"ZH$\rightarrow$EN",
}
DIR_COLORS = {
    "en_en": "#2171b5",
    "zh_zh": "#e6550d",
    "en_zh": "#31a354",
    "zh_en": "#de2d26",
}

def get_curve(section, direction):
    d = section["directions"][direction]
    layers = sorted(d.keys(), key=int)
    return np.array([int(l) for l in layers]), np.array([d[l] for l in layers])

def get_ci(ci_section, direction):
    d = ci_section["directions"][direction]
    layers = sorted(d.keys(), key=int)
    mean = np.array([d[l]["mean"] for l in layers])
    lo = np.array([d[l]["ci_lower"] for l in layers])
    hi = np.array([d[l]["ci_upper"] for l in layers])
    return np.array([int(l) for l in layers]), mean, lo, hi

# --- figure: 1×3 layout ---
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.4), sharey=True)

models = [
    ("(a) Llama-3.1-8B", "llama31", "llama31_mlp", None, 32),
    ("(b) Qwen3-8B", "qwen3", "qwen3_mlp", "qwen3_bootstrap_ci", 36),
    ("(c) Gemma-2-9B", "gemma2", None, "gemma2_bootstrap_ci", 42),
]

for ax, (title, res_key, mlp_key, ci_key, n_layers) in zip(axes, models):
    for direction in ["en_en", "zh_zh", "en_zh", "zh_en"]:
        c = DIR_COLORS[direction]

        lx, ly = get_curve(data[res_key], direction)
        ax.plot(lx, ly, color=c, linewidth=1.4, zorder=3)

        if mlp_key and mlp_key in data:
            mx, my = get_curve(data[mlp_key], direction)
            ax.plot(mx, my, color=c, linewidth=1.0, linestyle="--", alpha=0.65,
                    zorder=2)

        if ci_key and ci_key in data:
            cx, cm, clo, chi = get_ci(data[ci_key], direction)
            ax.fill_between(cx, clo, chi, color=c, alpha=0.08, zorder=1)

    # peak markers (residual — star)
    for direction in ["en_en", "zh_zh", "en_zh", "zh_en"]:
        pk = data[res_key]["peaks"][direction]
        ax.plot(pk["peak_layer"], pk["peak_acc"], marker="*", markersize=8,
                color=DIR_COLORS[direction], zorder=5,
                markeredgecolor="k", markeredgewidth=0.4)

    # peak markers (MLP — diamond)
    if mlp_key and mlp_key in data:
        for direction in ["en_en", "zh_zh", "en_zh", "zh_en"]:
            pk = data[mlp_key]["peaks"][direction]
            ax.plot(pk["peak_layer"], pk["peak_acc"], marker="D", markersize=4.5,
                    color=DIR_COLORS[direction], zorder=5, alpha=0.85,
                    markeredgecolor="k", markeredgewidth=0.4)

    # L13 annotation for Llama (steering causal node)
    if res_key == "llama31":
        ax.axvline(x=13, color="#555555", linewidth=0.9, linestyle=":",
                   zorder=1, alpha=0.7)
        ax.annotate("L13\n(steering)", xy=(13, 0.47), fontsize=7.5,
                    color="#555555", ha="center", va="bottom",
                    fontstyle="italic")

    ax.set_title(title, fontsize=11, fontweight="bold", pad=6)
    ax.set_xlabel("Layer Index", fontsize=10)
    ax.set_xlim(-0.5, n_layers - 0.5)
    ax.set_ylim(0.45, 0.84)
    ax.tick_params(labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

axes[0].set_ylabel("Balanced Accuracy", fontsize=10)

# compact legend
handles = []
for direction in ["en_en", "zh_zh", "en_zh", "zh_en"]:
    handles.append(plt.Line2D([], [], color=DIR_COLORS[direction], lw=1.5,
                               label=DIR_LABELS[direction]))
handles.append(plt.Line2D([], [], color="grey", lw=1.3, ls="-",
                           label="Residual stream"))
handles.append(plt.Line2D([], [], color="grey", lw=1.0, ls="--", alpha=0.65,
                           label="MLP output"))
handles.append(plt.Line2D([], [], marker="*", color="grey", ls="",
                           markersize=7, markeredgecolor="k",
                           markeredgewidth=0.3, label="Peak (res.)"))
handles.append(plt.Line2D([], [], marker="D", color="grey", ls="",
                           markersize=4, markeredgecolor="k",
                           markeredgewidth=0.3, label="Peak (MLP)"))
labels = [h.get_label() for h in handles]

fig.legend(handles, labels, loc="lower center", ncol=4, fontsize=7.5,
           frameon=False, bbox_to_anchor=(0.5, -0.10), columnspacing=1.5,
           handletextpad=0.5)

plt.tight_layout(rect=[0, 0.04, 1, 1])

# --- save ---
fig.savefig(OUT_DIR / "fig2_layerwise_probes.pdf",
            bbox_inches="tight", dpi=300)
fig.savefig(OUT_DIR / "fig2_layerwise_probes.png",
            bbox_inches="tight", dpi=300)
print(f"Saved to {OUT_DIR / 'fig2_layerwise_probes.pdf'}")
print(f"Saved to {OUT_DIR / 'fig2_layerwise_probes.png'}")
plt.close()
