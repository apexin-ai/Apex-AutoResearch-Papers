#!/usr/bin/env python3
"""Generate Figure 6: AUC decay with bootstrap CI bands (4 models).

Reads bootstrap_ci_4model.json (Qwen-RW, Pythia-1.4B, OLMo-1B, Qwen-cont).
Output: docs/paper/figures/fig_s1_auc_decay_ci.{pdf,png}
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

PAIR_KEYS = ["0v1", "1v2", "2v3", "3v4", "4v5"]
X_LABELS = ["0 vs 1", "1 vs 2", "2 vs 3", "3 vs 4", "4 vs 5"]
x = np.arange(len(PAIR_KEYS))

MODELS = {
    "mvp_001_qwen_rewrite": {"label": "Qwen-1.5B-RW", "color": "#4e79a7", "marker": "o"},
    "exp_001_pythia":       {"label": "Pythia-1.4B",   "color": "#e15759", "marker": "s"},
    "exp_002_olmo":         {"label": "OLMo-1B",       "color": "#59a14f", "marker": "^"},
    "exp_017_qwen_cont":    {"label": "Qwen-1.5B-cont","color": "#b07aa1", "marker": "D"},
}

root = Path(__file__).resolve().parent.parent
data_path = root / "artifacts" / "bootstrap_ci_4model.json"
with open(data_path) as f:
    raw = json.load(f)

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

for key, style in MODELS.items():
    d = raw[key]
    means = [d[p]["mean_auc"] for p in PAIR_KEYS]
    ci_lo = [d[p]["ci_lower"] for p in PAIR_KEYS]
    ci_hi = [d[p]["ci_upper"] for p in PAIR_KEYS]

    ax.plot(x, means, f"-{style['marker']}", color=style["color"],
            lw=1.5, ms=5, label=style["label"], zorder=3)
    ax.fill_between(x, ci_lo, ci_hi, color=style["color"], alpha=0.15, zorder=2)

ax.axhline(y=0.60, color="gray", ls="--", lw=0.8, alpha=0.7, zorder=1)
ax.text(4.15, 0.603, r"$\theta=0.60$", fontsize=7.5, color="gray", va="bottom")

ax.axhline(y=0.50, color="lightgray", ls=":", lw=0.6, alpha=0.7, zorder=1)

ax.set_xticks(x)
ax.set_xticklabels(X_LABELS)
ax.set_xlabel("Depth Pair")
ax.set_ylabel("Pairwise AUC")
ax.set_ylim(0.45, 1.02)
ax.set_xlim(-0.15, 4.35)

ax.legend(fontsize=7.5, loc="upper right", framealpha=0.9, edgecolor="0.8")

out_dir = root / "docs" / "paper" / "figures"
out_dir.mkdir(parents=True, exist_ok=True)

pdf_path = out_dir / "fig_s1_auc_decay_ci.pdf"
png_path = out_dir / "fig_s1_auc_decay_ci.png"
fig.savefig(pdf_path, dpi=300, bbox_inches="tight")
fig.savefig(png_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"PDF: {pdf_path} ({pdf_path.stat().st_size / 1024:.1f} KB)")
print(f"PNG: {png_path} ({png_path.stat().st_size / 1024:.1f} KB)")
for key, style in MODELS.items():
    d = raw[key]
    print(f"  {style['label']}: 1v2={d['1v2']['mean_auc']:.3f} CI[{d['1v2']['ci_lower']:.3f}, {d['1v2']['ci_upper']:.3f}]")
