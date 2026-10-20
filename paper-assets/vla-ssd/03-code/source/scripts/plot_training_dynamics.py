"""Strip plot of ΔR² across four training pathway categories.
Shows that exit collapse emerges at VLM→VLA transition and does not intensify at VLA→VLA.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Liberation Serif',
    'mathtext.it': 'Liberation Serif:italic',
    'mathtext.bf': 'Liberation Serif:bold',
})
import numpy as np
import os

# --- Data from Table 1 ---
categories = ["NLP\nfinetune", "Reference\n(pretrained)", "VLA→VLA\ntrained", "VLM→VLA\ntrained"]

data = {
    "NLP\nfinetune": [
        (0.000, "Llama-2-chat"),
        (0.000, "Phi-3-instruct"),
        (0.000, "Qwen2.5-Instruct"),
    ],
    "Reference\n(pretrained)": [
        (0.065, "TraceVLA"),   # Goal ref
        (0.048, "TraceVLA"),   # Spatial ref
        (0.009, "TraceVLA"),   # Object ref
        (0.097, "TraceVLA"),   # Long ref
        (0.081, "NORA"),      # Goal ref
        (0.089, "NORA"),      # Spatial ref
        (0.056, "OpenVLA"),   # Goal ref
        (0.044, "OpenVLA"),   # Spatial ref
        (0.051, "OpenVLA"),   # Object ref
        (0.035, "OpenVLA"),   # Long ref
    ],
    "VLA→VLA\ntrained": [
        (0.086, "OpenVLA"),   # Goal
        (0.037, "OpenVLA"),   # Spatial
        (0.037, "OpenVLA"),   # Object
        (0.033, "OpenVLA"),   # Long
    ],
    "VLM→VLA\ntrained": [
        (0.333, "TraceVLA"),   # Goal
        (0.156, "TraceVLA"),   # Spatial
        (0.362, "TraceVLA"),   # Object
        (0.358, "TraceVLA"),   # Long
        (0.455, "NORA"),      # Goal
        (0.308, "NORA"),      # Spatial
    ],
}

arch_markers = {"OpenVLA": "o", "TraceVLA": "s", "NORA": "D",
                "Llama-2-chat": "o", "Phi-3-instruct": "s", "Qwen2.5-Instruct": "D"}
arch_colors = {"OpenVLA": "#1f77b4", "TraceVLA": "#ff7f0e", "NORA": "#2ca02c",
               "Llama-2-chat": "#1f77b4", "Phi-3-instruct": "#ff7f0e", "Qwen2.5-Instruct": "#2ca02c"}

fig, ax = plt.subplots(figsize=(4.5, 3.2))

np.random.seed(42)
for i, cat in enumerate(categories):
    points = data[cat]
    for val, arch in points:
        jitter = np.random.uniform(-0.12, 0.12)
        ax.scatter(i + jitter, val, marker=arch_markers[arch], c=arch_colors[arch],
                   s=45, edgecolors="k", linewidths=0.4, zorder=3)

ax.axhline(0.10, color="gray", linestyle="--", linewidth=0.8, zorder=1, label=r"$\Delta R^2 = 0.10$ threshold")

ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, fontsize=8)
ax.set_ylabel(r"$\Delta R^2$ (peak $-$ exit)", fontsize=9)
ax.set_xlim(-0.5, len(categories) - 0.5)
ax.set_ylim(-0.02, 0.50)
ax.tick_params(axis="y", labelsize=8)

# Legend for architectures
from matplotlib.lines import Line2D
handles = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#1f77b4", markeredgecolor="k",
           markeredgewidth=0.4, markersize=6, label="OpenVLA / Llama-2"),
    Line2D([0], [0], marker="s", color="w", markerfacecolor="#ff7f0e", markeredgecolor="k",
           markeredgewidth=0.4, markersize=6, label="TraceVLA / Phi-3"),
    Line2D([0], [0], marker="D", color="w", markerfacecolor="#2ca02c", markeredgecolor="k",
           markeredgewidth=0.4, markersize=6, label="NORA / Qwen2.5"),
    Line2D([0], [0], color="gray", linestyle="--", linewidth=0.8, label=r"$\Delta R^2=0.10$"),
]
ax.legend(handles=handles, fontsize=6.5, loc="upper left", framealpha=0.9)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

out_paper = os.path.join(os.path.dirname(__file__), "..", "docs", "paper", "figures", "fig_training_dynamics.pdf")
out_artifact = os.path.join(os.path.dirname(__file__), "..", "artifacts", "figures", "paper", "fig_training_dynamics.pdf")
os.makedirs(os.path.dirname(out_paper), exist_ok=True)
os.makedirs(os.path.dirname(out_artifact), exist_ok=True)
fig.savefig(out_paper, bbox_inches="tight", dpi=300)
fig.savefig(out_artifact, bbox_inches="tight", dpi=300)
print(f"Saved: {out_paper}")
print(f"Saved: {out_artifact}")
plt.close()
