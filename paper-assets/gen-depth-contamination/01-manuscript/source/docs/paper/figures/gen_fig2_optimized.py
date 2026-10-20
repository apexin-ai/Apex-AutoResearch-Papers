#!/usr/bin/env python3
"""Figure 2: AUC decay across depth pairs — EMNLP column width.
Data source: Table 1 (tab:kstar_ci) + Table S2b (tab:kstar_ci_extended) + Table S2 (decoding).
All values use Qwen2.5-1.5B cross-scoring (updated D107)."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.lines import Line2D

# ── Data from paper tables (Qwen cross-scored, verified) ──
MODELS = [
    ("Qwen-rw",    [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],
                   [0.993, 0.686, 0.580, 0.534, 0.524],
                   [0.998, 0.704, 0.599, 0.553, 0.544]),
    ("Pythia",     [0.9722, 0.6074, 0.5440, 0.5051, 0.5079],
                   [0.967, 0.598, 0.534, 0.495, 0.498],
                   [0.977, 0.617, 0.554, 0.515, 0.518]),
    ("Qwen-cont",  [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],
                   [0.996, 0.602, 0.551, 0.531, 0.504],
                   [0.999, 0.621, 0.571, 0.551, 0.524]),
    ("Qwen-7B",    [0.9644, 0.6178, 0.5492, 0.5276, 0.5085],
                   [0.961, 0.608, 0.539, 0.517, 0.499],
                   [0.967, 0.626, 0.559, 0.538, 0.519]),
    ("LLaMA-8B",   [0.9224, 0.6123, 0.5273, 0.5168, 0.5159],
                   [0.917, 0.603, 0.517, 0.506, 0.505],
                   [0.927, 0.622, 0.538, 0.528, 0.527]),
    ("Qwen-base",  [0.9870, 0.6260, 0.5500, 0.5290, 0.5180],
                   [0.985, 0.617, 0.540, 0.519, 0.508],
                   [0.989, 0.635, 0.560, 0.540, 0.529]),
]

K1_MODELS = [
    ("OLMo",       [0.9861, 0.5001, 0.4973, 0.5034, 0.4971],
                   [0.984, 0.496, 0.486, 0.492, 0.484],
                   [0.989, 0.519, 0.509, 0.513, 0.505]),
    ("Mistral-7B", [0.9209, 0.5695, 0.5335, 0.5140, 0.5184],
                   [0.919, 0.565, 0.528, 0.508, 0.508],
                   [0.923, 0.575, 0.538, 0.520, 0.528]),
]

DECODING = [
    ("Greedy",           [0.980, 0.689, 0.561, 0.540, 0.514]),
    (r"Nuc $p{=}0.9$",  [0.995, 0.686, 0.592, 0.547, 0.507]),
    (r"$T{=}0.7$",      [0.988, 0.689, 0.590, 0.539, 0.535]),
    (r"$T{=}1.2$",      [0.998, 0.704, 0.582, 0.529, 0.524]),
]

MODEL_STYLE = {
    "Qwen-rw":    {"c": "#0072B2", "m": "o"},
    "Pythia":     {"c": "#D55E00", "m": "s"},
    "Qwen-cont":  {"c": "#009E73", "m": "^"},
    "Qwen-7B":    {"c": "#CC79A7", "m": "D"},
    "LLaMA-8B":   {"c": "#E69F00", "m": "v"},
    "Qwen-base":  {"c": "#56B4E9", "m": "P"},
    "OLMo":       {"c": "#BBBBBB", "m": "x"},
    "Mistral-7B": {"c": "#999999", "m": "+"},
}
DECODE_STYLE = [
    {"c": "#8B7355", "m": "*"},
    {"c": "#A0926E", "m": "h"},
    {"c": "#B8A88A", "m": "<"},
    {"c": "#C4B496", "m": ">"},
]

x_labels = ["0v1", "1v2", "2v3", "3v4", "4v5"]
x = np.arange(len(x_labels))

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.linewidth": 0.5,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.03,
})

fig, ax = plt.subplots(figsize=(3.4, 2.8))

# ── θ reference line (primary visual anchor) ──
ax.axhline(0.60, color="#888888", ls="--", lw=0.7, zorder=1)
t = ax.text(4.30, 0.607, r"$\theta{=}0.60$", fontsize=6.5, color="#666666",
            va="bottom", ha="right")
t.set_path_effects([pe.withStroke(linewidth=2, foreground="white")])

# ── Chance baseline ──
ax.axhline(0.50, color="#DDDDDD", ls=":", lw=0.4, zorder=0)

# ── Discriminable zone shading ──
ax.axhspan(0.60, 1.02, color="#F0F7F0", alpha=0.5, zorder=0, lw=0)

# ── K*=2 models (solid, prominent) ──
model_handles = []
for name, auc, lo, hi in MODELS:
    s = MODEL_STYLE[name]
    y, ci_lo, ci_hi = np.array(auc), np.array(lo), np.array(hi)
    ax.fill_between(x, ci_lo, ci_hi, color=s["c"], alpha=0.08, zorder=2, lw=0)
    line, = ax.plot(x, y, "-", color=s["c"], lw=1.4, marker=s["m"],
                    markersize=3.5, markeredgewidth=0.5, markeredgecolor="white",
                    zorder=5, solid_capstyle="round")
    model_handles.append((line, name))

# ── K*=1 models (muted, dashed) ──
k1_handles = []
for name, auc, lo, hi in K1_MODELS:
    s = MODEL_STYLE[name]
    y = np.array(auc)
    ax.fill_between(x, np.array(lo), np.array(hi), color=s["c"], alpha=0.05, zorder=2, lw=0)
    line, = ax.plot(x, y, "--", color=s["c"], lw=0.8, marker=s["m"],
                    markersize=3, markeredgewidth=0.5, alpha=0.7,
                    zorder=3, solid_capstyle="round")
    k1_handles.append((line, name))

# ── Decoding strategies (very thin dotted, background context) ──
dec_handles = []
for i, (name, auc) in enumerate(DECODING):
    s = DECODE_STYLE[i]
    y = np.array(auc)
    line, = ax.plot(x, y, ":", color=s["c"], lw=0.7, marker=s["m"],
                    markersize=2.5, markeredgewidth=0.2, alpha=0.50,
                    zorder=2, solid_capstyle="round")
    dec_handles.append((line, name))

# ── Compact legend ──
hdr_k2 = Line2D([], [], color="none")
hdr_k1 = Line2D([], [], color="none")
hdr_d = Line2D([], [], color="none")

all_h = ([hdr_k2] + [h for h, _ in model_handles] +
         [hdr_k1] + [h for h, _ in k1_handles] +
         [hdr_d] + [h for h, _ in dec_handles])
all_l = ([r"$K^*{=}2$ models"] + [n for _, n in model_handles] +
         [r"$K^*{=}1$ models"] + [n for _, n in k1_handles] +
         ["Decoding (Qwen-rw)"] + [n for _, n in dec_handles])

leg = ax.legend(all_h, all_l,
                fontsize=4.8, loc="center right", bbox_to_anchor=(1.0, 0.52),
                framealpha=0.95, edgecolor="#DDDDDD", fancybox=True,
                handlelength=1.3, borderpad=0.3, labelspacing=0.10,
                handletextpad=0.3, ncol=1)
leg.get_frame().set_linewidth(0.3)

for text in leg.get_texts():
    lbl = text.get_text()
    if lbl in [r"$K^*{=}2$ models", r"$K^*{=}1$ models", "Decoding (Qwen-rw)"]:
        text.set_fontsize(5)
        text.set_fontweight("bold")
        text.set_color("#555555")

# ── Axes ──
ax.set_xticks(x)
ax.set_xticklabels(x_labels, fontsize=7.5)
ax.set_xlabel("Depth Pair", fontsize=8.5)
ax.set_ylabel("Pairwise AUC", fontsize=8.5)
ax.set_ylim(0.46, 1.02)
ax.set_xlim(-0.15, len(x_labels) - 0.60)
ax.tick_params(direction="in", labelsize=7, length=2.5)

plt.tight_layout(pad=0.3)

out = "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures"
fig.savefig(f"{out}/fig2_auc_decay.pdf")
fig.savefig(f"{out}/fig2_auc_decay.png")
plt.close(fig)
print("OK fig2")
