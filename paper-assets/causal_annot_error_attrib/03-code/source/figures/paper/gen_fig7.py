"""
fig7_dirichlet_overlay: overlay 14 empirical confusion-matrix configs on theoretical
Dirichlet-subspace violation curves (exposure + IV topologies).

X-axis: min diagonal dominance = min_k C[k,k]
Y-axis: rate (violation_rate / sign_flip_rate from Dirichlet subspace analysis)
Theory: violation_rate as gray-shaded area; sign_flip_rate as dashed line.
Empirical: 14 points placed at (min_diag, interpolated_violation_rate), markers
encode dataset/model. Demonstrates "theory (K=3) vs practice (K=2,3,10)" gap.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from scipy.interpolate import PchipInterpolator

PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
ART = PROJ / "artifacts"
OUT = PROJ / "figures/paper/fig7_dirichlet_overlay.pdf"

# === UNIFIED PAPER COLOR PALETTE ===
COLOR_SAFE = '#154360'      # Deep navy — structural guarantee topologies
COLOR_DANGER = '#922B21'    # Deep crimson — sign-flip topologies
COLOR_NEUTRAL = '#1C2833'   # Near-black for text/axes
COLOR_GRID = '#D5D8DC'      # Light gray for grids
COLOR_ACCENT = '#B7950B'    # Burnished gold

# ---------- global style ----------
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 8,
    "axes.titlesize": 9,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 7,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.03,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
    "lines.linewidth": 1.4,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.size": 3,
    "ytick.major.size": 3,
})

# ---------- theoretical data (K=3 Dirichlet subspace) ----------
EXPOSURE_THEORY = {
    "diag_thresh":     [0.0,   0.5,   0.7,   0.9],
    "violation_rate":  [0.850, 0.325, 0.137, 0.119],
    "sign_flip_rate":  [0.834, 0.216, 0.021, 0.000],
}

with open(ART / "iv_dirichlet_subspace_results.json") as f:
    iv_raw = json.load(f)
IV_THEORY = {
    "diag_thresh":    [],
    "violation_rate": [],
    "sign_flip_rate": [],
}
for t in ("0.0", "0.5", "0.7", "0.9"):
    IV_THEORY["diag_thresh"].append(float(t))
    IV_THEORY["violation_rate"].append(iv_raw["thresholds"][t]["violation_rate"])
    IV_THEORY["sign_flip_rate"].append(iv_raw["thresholds"][t]["sign_flip_rate"])

# ---------- empirical 14 configs ----------
with open(ART / "plan006/asv_empirical_results.json") as f:
    plan006 = json.load(f)
HUMAID_CMS = plan006["confusion_matrices"]

VAST_DIAG = {
    "qwen2.5-7b_zero-shot":   [0.4613733905579399, 0.847457627118644,   0.10956175298804781],
    "qwen2.5-7b_few-shot-3":  [0.4132762312633833, 0.8210922787193974,  0.1254980079681275],
    "qwen2.5-7b_few-shot-5":  [0.4753747323340471, 0.775894538606403,   0.1254980079681275],
}
CIVIL_DIAG = {
    "qwen2.5-7b_zero-shot":   [0.7481536189069424, 0.684931506849315],
    "qwen2.5-7b_few-shot-3":  [0.6787296898079763, 0.7808219178082192],
    "qwen2.5-7b_few-shot-5":  [0.7370753323485968, 0.7602739726027398],
}

PAPER_CONFIGS = []
HUMAID_KEYS = [
    "humaid_llama4_zero-shot",
    "humaid_llama4_few-shot-3",
    "humaid_llama4_few-shot-5",
    "humaid_qwen3_zero-shot",
    "humaid_qwen3_few-shot-3",
    "humaid_deepseek_zero-shot",
    "humaid_deepseek_few-shot-3",
    "humaid_deepseek_few-shot-5",
]
for k in HUMAID_KEYS:
    C = np.array(HUMAID_CMS[k])
    mind = float(np.min(np.diag(C)))
    parts = k.split("_", 2)
    PAPER_CONFIGS.append({
        "dataset": "humaid", "model": parts[1], "prompt": parts[2],
        "K": 10, "min_diag": mind,
    })
for k, diag in VAST_DIAG.items():
    model, prompt = k.split("_", 1)
    PAPER_CONFIGS.append({
        "dataset": "vast", "model": model, "prompt": prompt,
        "K": 3, "min_diag": float(min(diag)),
    })
for k, diag in CIVIL_DIAG.items():
    model, prompt = k.split("_", 1)
    PAPER_CONFIGS.append({
        "dataset": "civil_comments", "model": model, "prompt": prompt,
        "K": 2, "min_diag": float(min(diag)),
    })

assert len(PAPER_CONFIGS) == 14, f"expected 14, got {len(PAPER_CONFIGS)}"

# ---------- marker / color encoding ----------
HUMAID_COLOR = {
    "llama4":   "#1B4F72",   # Royal navy
    "qwen3":    "#117A65",   # Dark emerald teal
    "deepseek": "#154360",   # Deep navy
}
DATASET_STYLE = {
    "humaid":         {"marker": "o", "size": 55},
    "vast":           {"marker": "s", "color": "#922B21", "size": 55},   # Dark crimson
    "civil_comments": {"marker": "^", "color": "#117A65", "size": 65},   # Dark emerald
}


def smooth_curve(xs, ys, n=200):
    """Monotonic interpolation on [0, 1]; extend constant beyond endpoints."""
    xs = np.asarray(xs, dtype=float)
    ys = np.asarray(ys, dtype=float)
    interp = PchipInterpolator(xs, ys, extrapolate=False)
    xx = np.linspace(0.0, 1.0, n)
    yy = interp(xx)
    yy[xx < xs[0]] = ys[0]
    yy[xx > xs[-1]] = ys[-1]
    return xx, yy


def interp_at(x, xs, ys):
    """Evaluate monotone interp at a single x with constant tails."""
    xs = np.asarray(xs, dtype=float)
    ys = np.asarray(ys, dtype=float)
    if x <= xs[0]:
        return float(ys[0])
    if x >= xs[-1]:
        return float(ys[-1])
    return float(PchipInterpolator(xs, ys, extrapolate=False)(x))


def draw_panel(ax, theory, panel_title, panel_letter, *, show_violation_fill=True):
    xs_t = theory["diag_thresh"]
    vr_t = theory["violation_rate"]
    sf_t = theory["sign_flip_rate"]

    xx, vr_curve = smooth_curve(xs_t, vr_t)
    _,  sf_curve = smooth_curve(xs_t, sf_t)

    # Theory: violation zone (fill) + sign-flip dashed line
    if show_violation_fill:
        ax.fill_between(
            xx, 0, vr_curve,
            color=COLOR_NEUTRAL, alpha=0.10, zorder=1,
            label="Violation rate (theory)",
        )
        ax.plot(xx, vr_curve, color=COLOR_NEUTRAL, linewidth=1.2, zorder=2)
    else:
        ax.axhline(1.0, color=COLOR_NEUTRAL, linewidth=0.9, alpha=0.5, zorder=1,
                   label="Violation rate (theory) $=1$")
    ax.plot(xx, sf_curve, color=COLOR_DANGER, linewidth=1.4,
            linestyle="--", zorder=3,
            label="Sign-flip rate (theory)")

    # Theory anchor points
    ax.scatter(xs_t, vr_t, s=16, color=COLOR_NEUTRAL,
               marker="x", linewidth=0.9, zorder=4, label="_nolegend_")
    ax.scatter(xs_t, sf_t, s=16, color=COLOR_DANGER,
               marker="x", linewidth=0.9, zorder=4, label="_nolegend_")

    # Safe / danger zone shading
    ax.axvspan(0.9, 1.0, color=COLOR_SAFE, alpha=0.06, zorder=0)
    ax.axvspan(0.0, 0.5, color=COLOR_DANGER, alpha=0.04, zorder=0)

    # Empirical points
    handled = set()
    for cfg in PAPER_CONFIGS:
        x = cfg["min_diag"]
        y = interp_at(x, xs_t, vr_t)
        ds = cfg["dataset"]
        style = DATASET_STYLE[ds]
        marker = style["marker"]
        size = style["size"]
        color = HUMAID_COLOR[cfg["model"]] if ds == "humaid" else style["color"]

        legend_key = (ds, cfg["model"]) if ds == "humaid" else (ds,)
        if legend_key not in handled:
            handled.add(legend_key)
            if ds == "humaid":
                lbl = f"HumAID/{cfg['model']} (K=10)"
            elif ds == "vast":
                lbl = "VAST/qwen2.5-7b (K=3)"
            else:
                lbl = "CivilComments/qwen2.5-7b (K=2)"
        else:
            lbl = None

        ax.scatter(
            x, y, marker=marker, s=size,
            facecolor=color, edgecolor="white", linewidth=0.8,
            zorder=6, label=lbl,
        )

    # Zone annotations
    txt_safe = ax.text(
        0.93, 0.06, "safe", ha="center", va="bottom",
        fontsize=7, color=COLOR_SAFE, fontstyle="italic",
        transform=ax.transAxes,
    )
    txt_safe.set_path_effects([pe.withStroke(linewidth=2.0, foreground="white")])
    txt_danger = ax.text(
        0.07, 0.42, "danger", ha="left", va="center",
        fontsize=7, color=COLOR_DANGER, fontstyle="italic",
        transform=ax.transAxes,
    )
    txt_danger.set_path_effects([pe.withStroke(linewidth=2.0, foreground="white")])

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(-0.02, 1.12)
    ax.set_xlabel(r"$\min_k C_{kk}$", fontsize=9)
    if panel_letter == "a":
        ax.set_ylabel("Rate", fontsize=9)
    ax.set_title(f"({panel_letter}) {panel_title}", loc="left", pad=3,
                 fontsize=9, fontweight='normal')
    ax.grid(True, axis="y", alpha=0.10, linewidth=0.5, color=COLOR_GRID, zorder=0)


# ---------- build figure (side-by-side, compact for single column) ----------
fig, axes = plt.subplots(1, 2, figsize=(3.4, 3.0), sharey=True)

draw_panel(axes[0], EXPOSURE_THEORY,
           "Exposure", "a",
           show_violation_fill=True)
draw_panel(axes[1], IV_THEORY,
           "IV", "b",
           show_violation_fill=False)
axes[1].set_xticks([0.0, 0.25, 0.50, 0.75, 1.00])
axes[1].set_xticklabels(["", "0.25", "0.50", "0.75", "1.00"])

# Compact spacing — minimize internal whitespace so panels fill column width
plt.subplots_adjust(left=0.06, right=0.99, wspace=0.12)

# Unified legend below both panels
handles, labels = [], []
for ax in axes:
    h, l = ax.get_legend_handles_labels()
    for hh, ll in zip(h, l):
        if ll and ll not in labels:
            handles.append(hh); labels.append(ll)
fig.legend(
    handles, labels,
    loc="lower center", bbox_to_anchor=(0.5, -0.18),
    ncol=3, frameon=True, framealpha=0.85, edgecolor='none',
    columnspacing=0.8, handletextpad=0.4, fontsize=7,
)

OUT.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUT, bbox_inches='tight', pad_inches=0.03)
plt.savefig(str(OUT).replace(".pdf", ".png"), bbox_inches='tight', pad_inches=0.03)
plt.close()
print(f"Saved: {OUT}")
print(f"Saved: {str(OUT).replace('.pdf', '.png')}")

# ---------- print empirical points for sanity ----------
print()
print(f"{'config':<48} {'K':>3} {'min_diag':>9}")
for cfg in sorted(PAPER_CONFIGS, key=lambda c: c["min_diag"]):
    key = f"{cfg['dataset']}_{cfg['model']}_{cfg['prompt']}"
    print(f"{key:<48} {cfg['K']:>3} {cfg['min_diag']:>9.4f}")
