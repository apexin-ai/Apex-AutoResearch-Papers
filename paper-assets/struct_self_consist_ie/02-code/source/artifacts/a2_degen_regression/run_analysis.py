#!/usr/bin/env python3
"""A2: Degeneracy-Capability regression analysis and scatter plot."""

import json
import numpy as np
from scipy import stats
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

OUT_DIR = Path(__file__).parent

# ── Data points: (model_family, regime, dataset, greedy_f1, degen_pct) ──
# Each row is a seed-level or single-run observation.

DATA = [
    # ── Qwen3-8B FT (T=1.0, 5-epoch, rank=1024, N=16 unless noted) ──
    ("Qwen3-8B", "FT", "SciERC",  0.6439, 17.77),
    ("Qwen3-8B", "FT", "SciERC",  0.6457, 17.20),
    ("Qwen3-8B", "FT", "SciERC",  0.6478, 20.42),
    ("Qwen3-8B", "FT", "CoNLL",   0.9070, 57.95),
    ("Qwen3-8B", "FT", "CoNLL",   0.9077, 63.03),
    ("Qwen3-8B", "FT", "CoNLL",   0.9070, 62.88),
    ("Qwen3-8B", "FT", "FewNERD", 0.7478, 14.43),
    ("Qwen3-8B", "FT", "FewNERD", 0.7480, 13.12),
    ("Qwen3-8B", "FT", "FewNERD", 0.7486, 12.12),
    ("Qwen3-8B", "FT", "FewNERD", 0.7478, 11.77),  # seed 789
    # Qwen3-8B FT N=16 FewNERD (from exp_027_fewnerd_n16)
    ("Qwen3-8B", "FT", "FewNERD-N16", 0.7478, 7.06),
    # Qwen3-8B WNUT17
    ("Qwen3-8B", "FT", "WNUT17",  0.5250, 53.70),  # from sample_f1_pct_zero as proxy; note this is actually pct_zero not degen

    # ── Qwen3-4B FT ──
    ("Qwen3-4B", "FT", "SciERC",  0.6622, 10.40),
    ("Qwen3-4B", "FT", "CoNLL",   0.9212, 90.57),

    # ── Qwen2.5-7B FT (FewNERD, 3 seeds) ──
    ("Qwen2.5-7B", "FT", "FewNERD", 0.7851, 31.10),
    ("Qwen2.5-7B", "FT", "FewNERD", 0.7850, 32.80),
    ("Qwen2.5-7B", "FT", "FewNERD", 0.7825, 31.30),

    # ── Qwen2.5-72B Zero-Shot ──
    ("Qwen2.5-72B", "ZS", "SciERC",  0.3993, 21.00),
    ("Qwen2.5-72B", "ZS", "CoNLL",   0.7120, 67.70),
    ("Qwen2.5-72B", "ZS", "FewNERD", 0.6281, 46.20),

    # ── Qwen2.5-72B Few-Shot ──
    ("Qwen2.5-72B", "FS", "SciERC",  0.4610, 16.60),
    ("Qwen2.5-72B", "FS", "CoNLL",   0.7450, 70.00),
    ("Qwen2.5-72B", "FS", "FewNERD", 0.6190, 45.20),

    # ── LLaMA-3.1-8B FT SciERC (3 seeds) ──
    ("LLaMA-3.1-8B", "FT", "SciERC",  0.6460, 24.95),
    ("LLaMA-3.1-8B", "FT", "SciERC",  0.6454, 26.65),
    ("LLaMA-3.1-8B", "FT", "SciERC",  0.6459, 27.41),
    # ── LLaMA-3.1-8B FT CoNLL (3 seeds) ──
    ("LLaMA-3.1-8B", "FT", "CoNLL",   0.9239, 89.44),
    ("LLaMA-3.1-8B", "FT", "CoNLL",   0.9238, 89.30),
    ("LLaMA-3.1-8B", "FT", "CoNLL",   0.9242, 89.44),
    # ── LLaMA-3.1-8B FT FewNERD (3 seeds) ──
    ("LLaMA-3.1-8B", "FT", "FewNERD", 0.7841, 27.32),
    ("LLaMA-3.1-8B", "FT", "FewNERD", 0.7840, 24.63),
    ("LLaMA-3.1-8B", "FT", "FewNERD", 0.7844, 18.13),

    # ── LLaMA-3.2-3B FT SciERC ──
    ("LLaMA-3.2-3B", "FT", "SciERC", 0.6267, None),  # no degen data, skip
]

# Filter out entries without degen data
DATA = [(m, r, d, f1, dg) for m, r, d, f1, dg in DATA if dg is not None]

# Remove WNUT17 pct_zero proxy — not true degeneracy
DATA = [(m, r, d, f1, dg) for m, r, d, f1, dg in DATA if d != "WNUT17"]
# Remove FewNERD-N16 (different N, confounded)
DATA = [(m, r, d, f1, dg) for m, r, d, f1, dg in DATA if d != "FewNERD-N16"]

# ── Color/marker scheme ──
FAMILY_STYLE = {
    "Qwen3-8B":     {"color": "#2166ac", "marker": "o", "label": "Qwen3-8B FT"},
    "Qwen3-4B":     {"color": "#67a9cf", "marker": "s", "label": "Qwen3-4B FT"},
    "Qwen2.5-7B":   {"color": "#1b7837", "marker": "D", "label": "Qwen2.5-7B FT"},
    "Qwen2.5-72B_ZS": {"color": "#d6604d", "marker": "^", "label": "Qwen2.5-72B ZS"},
    "Qwen2.5-72B_FS": {"color": "#f4a582", "marker": "v", "label": "Qwen2.5-72B FS"},
    "LLaMA-3.1-8B": {"color": "#e66101", "marker": "P", "label": "LLaMA-3.1-8B FT"},
}

def get_family_key(model, regime):
    if model == "Qwen2.5-72B" and regime == "ZS":
        return "Qwen2.5-72B_ZS"
    if model == "Qwen2.5-72B" and regime == "FS":
        return "Qwen2.5-72B_FS"
    return model

# ── Arrays ──
f1_arr = np.array([row[3] for row in DATA])
dg_arr = np.array([row[4] for row in DATA])

# ── Regression ──
# Linear
slope, intercept, r_lin, p_lin, se_lin = stats.linregress(f1_arr, dg_arr)
lin_eq = f"degen = {slope:.1f} × F1 + {intercept:.1f}"

# Quadratic
coeffs = np.polyfit(f1_arr, dg_arr, 2)
poly = np.poly1d(coeffs)
ss_res = np.sum((dg_arr - poly(f1_arr))**2)
ss_tot = np.sum((dg_arr - np.mean(dg_arr))**2)
r2_quad = 1 - ss_res / ss_tot
quad_eq = f"degen = {coeffs[0]:.1f}×F1² + {coeffs[1]:.1f}×F1 + {coeffs[2]:.1f}"

# Spearman rank correlation
rho_sp, p_sp = stats.spearmanr(f1_arr, dg_arr)

results = {
    "n_points": len(DATA),
    "linear": {
        "equation": lin_eq,
        "slope": round(slope, 3),
        "intercept": round(intercept, 3),
        "R2": round(r_lin**2, 4),
        "r": round(r_lin, 4),
        "p_value": float(f"{p_lin:.4e}"),
        "std_err": round(se_lin, 3),
    },
    "quadratic": {
        "equation": quad_eq,
        "coefficients": [round(c, 3) for c in coeffs],
        "R2": round(r2_quad, 4),
    },
    "spearman": {
        "rho": round(rho_sp, 4),
        "p_value": float(f"{p_sp:.4e}"),
    },
    "summary": (
        f"Positive correlation: higher greedy F1 → higher degeneracy rate. "
        f"Spearman ρ={rho_sp:.3f} (p={p_sp:.2e}). "
        f"Linear R²={r_lin**2:.3f}. Quadratic R²={r2_quad:.3f}. "
        f"The relationship is largely driven by dataset difficulty: "
        f"CoNLL (easy, high F1) has very high degeneracy, while SciERC (hard, low F1) has low degeneracy."
    ),
    "data_points": [
        {"model": m, "regime": r, "dataset": d, "greedy_f1": f1, "degen_pct": dg}
        for m, r, d, f1, dg in DATA
    ],
}

# ── Save regression results ──
with open(OUT_DIR / "regression_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("Regression results saved.")
print(f"  Linear:    {lin_eq}  (R²={r_lin**2:.4f}, p={p_lin:.2e})")
print(f"  Quadratic: {quad_eq}  (R²={r2_quad:.4f})")
print(f"  Spearman:  ρ={rho_sp:.4f}, p={p_sp:.2e}")

# ── Scatter plot ──
fig, ax = plt.subplots(figsize=(8, 5.5))

DATASET_ABBREV = {
    "SciERC": "Sci", "CoNLL": "CoN", "FewNERD": "Few",
}

for m, regime, ds, f1, dg in DATA:
    fk = get_family_key(m, regime)
    sty = FAMILY_STYLE[fk]
    ax.scatter(f1, dg, c=sty["color"], marker=sty["marker"],
               s=70, edgecolors="white", linewidths=0.5, zorder=5)

# Dataset labels: annotate cluster centroids only
from collections import defaultdict
clusters = defaultdict(list)
for m, regime, ds, f1, dg in DATA:
    fk = get_family_key(m, regime)
    clusters[(fk, ds)].append((f1, dg))

for (fk, ds), pts in clusters.items():
    xs = np.mean([p[0] for p in pts])
    ys = np.mean([p[1] for p in pts])
    abbr = DATASET_ABBREV.get(ds, ds[:3])
    ax.annotate(abbr, (xs, ys), textcoords="offset points",
                xytext=(6, 4), fontsize=6.5, color="gray", alpha=0.8)

# Regression lines
x_fit = np.linspace(f1_arr.min() - 0.02, f1_arr.max() + 0.02, 200)
ax.plot(x_fit, slope * x_fit + intercept, "--", color="gray", alpha=0.6, linewidth=1.2,
        label=f"Linear (R²={r_lin**2:.3f})")
ax.plot(x_fit, poly(x_fit), "-", color="#984ea3", alpha=0.55, linewidth=1.2,
        label=f"Quadratic (R²={r2_quad:.3f})")

# Legend
handles = []
for fk, sty in FAMILY_STYLE.items():
    handles.append(Line2D([0], [0], marker=sty["marker"], color="w",
                          markerfacecolor=sty["color"], markersize=8,
                          markeredgecolor="white", markeredgewidth=0.5,
                          label=sty["label"]))
handles.append(Line2D([0], [0], linestyle="--", color="gray", alpha=0.6, label=f"Linear (R²={r_lin**2:.3f})"))
handles.append(Line2D([0], [0], linestyle="-", color="#984ea3", alpha=0.55, label=f"Quadratic (R²={r2_quad:.3f})"))

ax.legend(handles=handles, fontsize=7.5, loc="upper left", framealpha=0.9,
          borderpad=0.6, handletextpad=0.5)

ax.set_xlabel("Greedy F1", fontsize=11)
ax.set_ylabel("Degeneracy Rate (%)", fontsize=11)
ax.set_title("Degeneracy Rate vs. Capability (Greedy F1)", fontsize=12, pad=10)
ax.tick_params(labelsize=9)
ax.set_xlim(0.35, 0.96)
ax.set_ylim(-2, 98)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(alpha=0.15)

fig.tight_layout()
fig.savefig(OUT_DIR / "degen_capability_scatter.png", dpi=200, bbox_inches="tight")
fig.savefig(OUT_DIR / "degen_capability_scatter.pdf", bbox_inches="tight")
print("Scatter plot saved (PNG + PDF).")
