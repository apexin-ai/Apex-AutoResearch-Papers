#!/usr/bin/env python3
"""Generate paper figure: JSD decay across generational depth.

Blue band = C4 K*=2 models (min-max), with median line.
Separate lines for Mistral-7B (K*=1), arXiv Pythia (K*=3), Retrain-chain (K*>=4).

Output: docs/paper/figures/fig_jsd_decay.{pdf,png}
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

PAIR_LABELS = ["0 vs 1", "1 vs 2", "2 vs 3", "3 vs 4", "4 vs 5"]
x = np.arange(len(PAIR_LABELS))

# --- C4 K*=2 models (band) ---
c4_k2 = {
    "Qwen-1.5B":       [0.163726, 0.010810, 0.005311, 0.003942, 0.003522],
    "Qwen-1.5B-cont":  [0.238045, 0.010089, 0.005309, 0.003699, 0.003942],
    "LLaMA-8B":        [0.076925, 0.012301, 0.004631, 0.004292, 0.003572],
    "Pythia-greedy":    [0.617756, 0.070498, 0.004498, 0.003202, 0.002579],
    "Pythia-nuc0.9":    [0.252017, 0.017922, 0.006115, 0.004110, 0.003301],
    "Pythia-T0.7":      [0.403980, 0.043741, 0.015638, 0.008836, 0.005122],
    "Pythia-T1.2":      [0.166001, 0.009573, 0.003991, 0.003303, 0.003177],
    "Qwen-7B":          [0.127422, 0.010114, 0.004798, 0.004821, 0.003335],
}

c4_arr = np.array(list(c4_k2.values()))
c4_median = np.median(c4_arr, axis=0)
c4_min = np.min(c4_arr, axis=0)
c4_max = np.max(c4_arr, axis=0)

# --- Individual lines ---
mistral_c4 = [0.124194, 0.008051, 0.005047, 0.004516, 0.004109]
arxiv_pythia = [0.171338, 0.057344, 0.019524, 0.009917, 0.008846]
retrain_chain = [0.169964, 0.129382, 0.107086, 0.064225]

# --- Plot ---
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.direction": "in",
    "ytick.direction": "in",
})

fig, ax = plt.subplots(figsize=(5.0, 3.5), constrained_layout=True)

ax.fill_between(x, c4_min, c4_max, color="#4e79a7", alpha=0.2, zorder=2)
ax.semilogy(x, c4_median, "-o", color="#4e79a7", lw=1.8, ms=5,
            label=r"C4, $K^*\!=\!2$ (8 configs, min–max)", zorder=3)

ax.semilogy(x, mistral_c4, "--s", color="#9467bd", lw=1.5, ms=5,
            label=r"Mistral-7B, $K^*\!=\!1$", zorder=3)

ax.semilogy(x, arxiv_pythia, "-^", color="#2ca02c", lw=1.5, ms=5,
            label=r"arXiv Pythia, $K^*\!=\!3$", zorder=3)

x_rt = np.arange(len(retrain_chain))
ax.semilogy(x_rt, retrain_chain, ":D", color="#d62728", lw=1.5, ms=5,
            label=r"Retrain-chain, $K^*\!\geq 4$", zorder=3)

ax.text(0.55, c4_median[0] * 1.35, "$K^*\\!=\\!2$", fontsize=8.5,
        color="#4e79a7", fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(PAIR_LABELS)
ax.set_xlabel("Depth Pair")
ax.set_ylabel("JSD (log scale)")
ax.set_ylim(1.5e-3, 0.8)
ax.set_xlim(-0.15, 4.15)

ax.legend(fontsize=7.5, loc="upper right", framealpha=0.9, edgecolor="0.8")

out_dir = Path(__file__).resolve().parent.parent / "docs" / "paper" / "figures"
out_dir.mkdir(parents=True, exist_ok=True)

pdf_path = out_dir / "fig_jsd_decay.pdf"
png_path = out_dir / "fig_jsd_decay.png"
fig.savefig(pdf_path, dpi=300, bbox_inches="tight")
fig.savefig(png_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"PDF: {pdf_path} ({pdf_path.stat().st_size / 1024:.1f} KB)")
print(f"PNG: {png_path} ({png_path.stat().st_size / 1024:.1f} KB)")
print(f"C4 band models ({len(c4_k2)}): {list(c4_k2.keys())}")
