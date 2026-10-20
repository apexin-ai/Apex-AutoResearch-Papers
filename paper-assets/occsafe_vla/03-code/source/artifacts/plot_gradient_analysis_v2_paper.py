#!/usr/bin/env python3
"""V2 Gradient Analysis Paper Figures for OccSafe-VLA.

Generates three publication-quality figures from per-layer gradient analysis:
  Fig 1: Gradient magnitude heatmap (conditions × layer, log-scale)
  Fig 2: Cosine similarity curves (action vs OCC gradients per layer)
  Fig 3: Cross-seed CAR variance bar chart (2×2 factorial)

Input: .pt or .json files, one per experimental condition.

Expected .pt format per condition (structured):
  {
    'gradient_stats': {
      layer_name: {'grad_norm_mean': float, 'grad_norm_std': float,
                   'grad_norms': [float, ...]},
      ...
    },
    'cosine_stats': {  # optional, only for non-detach + OCC conditions
      layer_name: {'cosine_mean': float, 'cosine_std': float,
                   'conflict_rate': float},
      ...
    }
  }

Also supports:
  - Flat .pt: {layer_name: {'grad_norm_mean': ..., 'cosine_mean': ..., ...}}
  - same_seed JSON: {'condition': str, 'per_layer': {layer_name: {...}}}

Usage:
  # All figures
  python plot_gradient_analysis_v2_paper.py \
    --data vanilla_v2:results/vanilla.pt \
           full_occ_ln_v2:results/full_occ_ln.pt \
           detach_ln_v2:results/detach_ln.pt \
           full_occ_bn_v2:results/full_occ_bn.pt \
    --output_dir figures/

  # With CAR variance for Figure 3
  python plot_gradient_analysis_v2_paper.py \
    --data vanilla_v2:vanilla.pt \
    --car_variance "Full OCC BN=0.045" "Detach BN=0.0065" \
                   "Full OCC LN=0.012" "Detach LN=0.008" \
    --output_dir figures/

  # Specific figures only
  python plot_gradient_analysis_v2_paper.py \
    --data vanilla_v2:vanilla.pt full_occ_ln_v2:full_ln.pt \
    --figures heatmap cosine --output_dir figures/

  # Separate cosine data files
  python plot_gradient_analysis_v2_paper.py \
    --data full_occ_ln_v2:grad.pt detach_ln_v2:grad2.pt \
    --cosine_data full_occ_ln_v2:cosine.pt \
    --output_dir figures/
"""

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
try:
    import seaborn as sns  # noqa: F401
except ImportError:
    pass


# === Style ===
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "lines.linewidth": 1.5,
})

# Okabe-Ito colorblind-friendly palette
CONDITION_STYLES = OrderedDict([
    ("vanilla_v2",     {"color": "#999999", "label": "Vanilla",     "marker": "x", "ls": ":"}),
    ("full_occ_bn_v2", {"color": "#009E73", "label": "Full OCC BN", "marker": "^", "ls": "-"}),
    ("full_occ_ln_v2", {"color": "#0072B2", "label": "Full OCC LN", "marker": "o", "ls": "-"}),
    ("detach_bn_v2",   {"color": "#CC79A7", "label": "Detach BN",   "marker": "D", "ls": "--"}),
    ("detach_ln_v2",   {"color": "#D55E00", "label": "Detach LN",   "marker": "s", "ls": "--"}),
])

ENCODERS = OrderedDict([
    ("featurizer",       {"name": "DINOv2", "n_blocks": 23}),
    ("fused_featurizer", {"name": "SigLIP", "n_blocks": 26}),
])

# Colors for factorial cells in Figure 3
FACTORIAL_COLORS = {
    "full occ bn": "#0072B2",
    "full occ ln": "#009E73",
    "detach bn":   "#D55E00",
    "detach ln":   "#E69F00",
}


# ====================================================================
# Argument parsing
# ====================================================================

def parse_args():
    p = argparse.ArgumentParser(
        description="V2 gradient analysis paper figures for OccSafe-VLA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--data", nargs="+", metavar="NAME:PATH",
        help="Gradient data files as NAME:PATH pairs "
             "(e.g., vanilla_v2:results/vanilla.pt)",
    )
    p.add_argument(
        "--cosine_data", nargs="+", metavar="NAME:PATH", default=None,
        help="Separate cosine similarity files if not in --data files",
    )
    p.add_argument(
        "--car_variance", nargs="+", metavar='"NAME=VALUE"', default=None,
        help='CAR std values for Fig 3 (e.g., "Full OCC BN=0.045")',
    )
    p.add_argument(
        "--output_dir", type=str, required=True,
        help="Output directory for PDF/PNG figures",
    )
    p.add_argument("--dpi", type=int, default=300)
    p.add_argument(
        "--figures", nargs="+", default=None,
        choices=["heatmap", "cosine", "variance", "all"],
        help="Which figures to generate (default: all available)",
    )
    p.add_argument(
        "--prefix", type=str, default="v2",
        help="Output filename prefix (default: v2)",
    )
    return p.parse_args()


# ====================================================================
# Data loading / normalization
# ====================================================================

def _norm_grad(stats):
    """Normalize gradient stat entry to {mean, std, values}."""
    return {
        "mean": stats.get("grad_norm_mean",
                          stats.get("action_grad_norm_mean", 0)),
        "std":  stats.get("grad_norm_std",
                          stats.get("action_grad_norm_std", 0)),
        "values": stats.get("grad_norms",
                            stats.get("values", [])),
    }


def _norm_cos(stats):
    """Normalize cosine stat entry to {mean, std, conflict_rate}."""
    return {
        "mean": stats.get("cosine_mean",
                          stats.get("cosine_sim_mean")),
        "std":  stats.get("cosine_std",
                          stats.get("cosine_sim_std", 0)),
        "conflict_rate": stats.get("conflict_rate"),
    }


def load_data(path_str):
    """Load gradient/cosine data from .pt or .json, normalize to:
      {'gradient': {layer: {...}}, 'cosine': {layer: {...}}}
    """
    path = Path(path_str)
    if path.suffix == ".pt":
        import torch
        raw = torch.load(path, map_location="cpu", weights_only=False)
    elif path.suffix == ".json":
        with open(path) as f:
            raw = json.load(f)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")

    gradient, cosine = {}, {}

    # Format A: structured {'gradient_stats': ..., 'cosine_stats': ...}
    if "gradient_stats" in raw:
        for layer, s in raw["gradient_stats"].items():
            gradient[layer] = _norm_grad(s)
        for layer, s in (raw.get("cosine_stats") or {}).items():
            cosine[layer] = _norm_cos(s)

    # Format B: same_seed JSON {'per_layer': {layer: {...}}}
    elif "per_layer" in raw:
        for layer, s in raw["per_layer"].items():
            gradient[layer] = _norm_grad(s)
            cos_mean = s.get("cosine_sim_mean", s.get("cosine_mean"))
            if cos_mean is not None:
                cosine[layer] = _norm_cos(s)

    # Format C: flat {layer_name: {grad_norm_mean, cosine_mean, ...}}
    else:
        for layer, s in raw.items():
            if not isinstance(s, dict):
                continue
            if any(k in s for k in ("grad_norm_mean", "action_grad_norm_mean")):
                gradient[layer] = _norm_grad(s)
            if any(k in s for k in ("cosine_mean", "cosine_sim_mean")):
                cosine[layer] = _norm_cos(s)

    return {"gradient": gradient, "cosine": cosine}


def extract_encoder_blocks(per_layer, prefix):
    """Extract blocks for encoder prefix, deduplicated and sorted by index."""
    seen = {}
    for layer_name, stats in per_layer.items():
        if layer_name.startswith(f"{prefix}.blocks."):
            idx = int(layer_name.split(".")[2])
            if idx not in seen:
                seen[idx] = stats
    return sorted(seen.items())


def get_style(cond):
    """Look up plotting style; falls back to grey if unknown."""
    if cond in CONDITION_STYLES:
        return CONDITION_STYLES[cond]
    base = cond.replace("_v2", "")
    for k, v in CONDITION_STYLES.items():
        if k.replace("_v2", "") == base:
            return v
    return {"color": "#888888", "label": cond, "marker": ".", "ls": "-"}


# ====================================================================
# Figure 1: Gradient Magnitude Heatmap
# ====================================================================

def plot_gradient_heatmap(all_data, output_dir, dpi, prefix):
    """Two-panel heatmap (DINOv2 + SigLIP): conditions × layers, log scale."""
    cond_order = [c for c in CONDITION_STYLES if c in all_data]
    if not cond_order:
        cond_order = list(all_data.keys())
    if not cond_order:
        print("No gradient data for heatmap, skipping")
        return

    enc_list = list(ENCODERS.items())
    matrices = []
    for enc_key, enc_info in enc_list:
        n_b = enc_info["n_blocks"]
        mat = np.full((len(cond_order), n_b), np.nan)
        for ci, cond in enumerate(cond_order):
            for idx, stats in extract_encoder_blocks(
                    all_data[cond]["gradient"], enc_key):
                if idx < n_b:
                    mat[ci, idx] = stats["mean"]
        matrices.append(mat)

    all_vals = np.concatenate([m[np.isfinite(m)] for m in matrices])
    if len(all_vals) == 0:
        print("No finite gradient values for heatmap, skipping")
        return

    norm = mcolors.LogNorm(vmin=max(all_vals.min(), 1e-6), vmax=all_vals.max())
    cmap = plt.cm.inferno.copy()
    cmap.set_bad(color="#f0f0f0")

    width_ratios = [ENCODERS[e]["n_blocks"] for e in ENCODERS]
    fig, axes = plt.subplots(
        1, len(enc_list),
        figsize=(7.5, 0.45 * len(cond_order) + 0.8),
        gridspec_kw={"width_ratios": width_ratios, "wspace": 0.06},
        sharey=True,
    )
    if len(enc_list) == 1:
        axes = [axes]

    cond_labels = [get_style(c)["label"] for c in cond_order]
    im = None

    for i, ((enc_key, enc_info), mat) in enumerate(zip(enc_list, matrices)):
        ax = axes[i]
        im = ax.imshow(mat, aspect="auto", cmap=cmap, norm=norm,
                        interpolation="nearest")

        n_b = enc_info["n_blocks"]
        xticks = list(range(0, n_b, 5))
        if n_b - 1 not in xticks:
            xticks.append(n_b - 1)
        ax.set_xticks(xticks)
        ax.set_xticklabels([str(t) for t in xticks])

        if i == 0:
            ax.set_yticks(range(len(cond_labels)))
            ax.set_yticklabels(cond_labels)
        else:
            ax.yaxis.set_tick_params(labelleft=False)

        sub = chr(ord("a") + i)
        ax.set_xlabel(f"{enc_info['name']} block index")
        ax.set_title(f"({sub}) {enc_info['name']}", fontsize=10, pad=6)

        for spine in ax.spines.values():
            spine.set_visible(False)

    fig.colorbar(
        im, ax=axes, location="right", fraction=0.02, pad=0.02,
        label="Gradient norm (log scale)",
    )

    _save(fig, output_dir, f"{prefix}_grad_heatmap", dpi)


# ====================================================================
# Figure 2: Cosine Similarity Curves
# ====================================================================

def plot_cosine_similarity(all_data, output_dir, dpi, prefix):
    """Two-panel line plot: cosine similarity per layer with shaded std."""
    conds = [c for c in CONDITION_STYLES if c in all_data and all_data[c]["cosine"]]
    if not conds:
        conds = [c for c in all_data if all_data[c]["cosine"]]
    if not conds:
        print("No cosine similarity data, skipping")
        return

    enc_list = list(ENCODERS.items())
    width_ratios = [ENCODERS[e]["n_blocks"] for e in ENCODERS]
    fig, axes = plt.subplots(
        1, len(enc_list),
        figsize=(7.2, 2.8),
        gridspec_kw={"width_ratios": width_ratios, "wspace": 0.14},
        sharey=True,
    )
    if len(enc_list) == 1:
        axes = [axes]

    for i, (enc_key, enc_info) in enumerate(enc_list):
        ax = axes[i]
        for cond in conds:
            style = get_style(cond)
            blocks = extract_encoder_blocks(all_data[cond]["cosine"], enc_key)
            if not blocks:
                continue
            xs = np.array([b[0] for b in blocks])
            ys = np.array([b[1]["mean"] for b in blocks], dtype=float)
            stds = np.array([b[1].get("std", 0) or 0 for b in blocks],
                            dtype=float)

            ax.plot(xs, ys, color=style["color"], label=style["label"],
                    marker=style["marker"], markersize=3, linewidth=1.4,
                    ls=style["ls"], alpha=0.85, markeredgewidth=0)
            ax.fill_between(xs, ys - stds, ys + stds,
                            alpha=0.12, color=style["color"])

        ax.axhline(0, color="#888888", linestyle="--", linewidth=0.7,
                    alpha=0.5, zorder=1)
        ax.set_ylim(-1, 1)
        ax.set_xlim(-0.5, enc_info["n_blocks"] - 0.5)
        ax.set_xticks(range(0, enc_info["n_blocks"], 5))
        ax.set_xlabel(f"{enc_info['name']} block index")

        if i == 0:
            ax.set_ylabel("Cosine similarity")
        else:
            ax.yaxis.set_tick_params(labelleft=False)

        sub = chr(ord("a") + i)
        ax.set_title(f"({sub}) {enc_info['name']}", fontsize=10, pad=6)
        ax.legend(loc="best", framealpha=0.9, edgecolor="none")
        ax.grid(True, alpha=0.15, axis="y")

    _save(fig, output_dir, f"{prefix}_cosine_similarity", dpi)


# ====================================================================
# Figure 3: Cross-seed CAR Variance Bar Chart
# ====================================================================

def plot_car_variance(variance_specs, output_dir, dpi, prefix):
    """Bar chart comparing cross-seed CAR variance across factorial cells.

    Args:
        variance_specs: list of "NAME=VALUE" strings
    """
    if not variance_specs:
        print("No CAR variance data, skipping")
        return

    names, values = [], []
    for spec in variance_specs:
        name, val = spec.rsplit("=", 1)
        names.append(name.strip())
        values.append(float(val.strip()))
    values = np.array(values)

    colors = []
    for name in names:
        nl = name.lower()
        matched = False
        for key, col in FACTORIAL_COLORS.items():
            if key in nl:
                colors.append(col)
                matched = True
                break
        if not matched:
            colors.append("#999999")

    fig, ax = plt.subplots(figsize=(4.5, 3.0))
    x = np.arange(len(names))
    bars = ax.bar(x, values, width=0.55, color=colors,
                  edgecolor="white", linewidth=0.5)

    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=8)
    ax.set_ylabel("Cross-seed CAR std")
    ax.set_title("Variance across factorial cells", fontsize=10)

    # Value labels
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2,
                val + values.max() * 0.01,
                f"{val:.4f}", ha="center", va="bottom",
                fontsize=7, color="#444444")

    # Annotate max/min ratio with bracket
    if len(values) >= 2:
        imax, imin = int(np.argmax(values)), int(np.argmin(values))
        if values[imin] > 0:
            ratio = values[imax] / values[imin]
            bracket_y = values[imax] * 1.08
            i_left, i_right = min(imax, imin), max(imax, imin)
            ax.plot(
                [x[i_left], x[i_left], x[i_right], x[i_right]],
                [values[i_left] * 1.02, bracket_y, bracket_y,
                 values[i_right] * 1.02],
                color="#555555", linewidth=0.8,
            )
            ax.text(
                (x[i_left] + x[i_right]) / 2, bracket_y * 1.03,
                f"{ratio:.2f}×",
                fontsize=9, fontweight="bold", ha="center", va="bottom",
                color="#333333",
            )

    ax.set_ylim(0, values.max() * 1.35)
    ax.grid(True, alpha=0.15, axis="y")

    _save(fig, output_dir, f"{prefix}_car_variance", dpi)


# ====================================================================
# Helpers
# ====================================================================

def _save(fig, output_dir, stem, dpi):
    out = Path(output_dir)
    for ext in ("pdf", "png"):
        fig.savefig(out / f"{stem}.{ext}", dpi=dpi)
    plt.close(fig)
    print(f"Saved: {stem}.pdf / {stem}.png -> {out}")


# ====================================================================
# Main
# ====================================================================

def main():
    args = parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    figures = args.figures or ["all"]
    if "all" in figures:
        figures = ["heatmap", "cosine", "variance"]

    all_data = OrderedDict()
    if args.data:
        for spec in args.data:
            if ":" not in spec:
                print(f"Warning: skipping '{spec}' "
                      f"(expected NAME:PATH)", file=sys.stderr)
                continue
            name, path = spec.split(":", 1)
            all_data[name] = load_data(path)
            n_grad = len(all_data[name]["gradient"])
            n_cos = len(all_data[name]["cosine"])
            print(f"Loaded {name}: {n_grad} gradient layers, "
                  f"{n_cos} cosine layers")

    if args.cosine_data:
        for spec in args.cosine_data:
            name, path = spec.split(":", 1)
            extra = load_data(path)
            if name in all_data:
                all_data[name]["cosine"].update(extra.get("cosine", {}))
                if not extra["cosine"] and extra["gradient"]:
                    all_data[name]["cosine"].update(extra["gradient"])
            else:
                all_data[name] = extra
            print(f"Loaded cosine data for {name}: {path}")

    if not all_data and "variance" not in figures:
        print("Error: no data. Use --data NAME:PATH.", file=sys.stderr)
        sys.exit(1)

    pfx = args.prefix

    if "heatmap" in figures and all_data:
        plot_gradient_heatmap(all_data, args.output_dir, args.dpi, pfx)

    if "cosine" in figures and all_data:
        plot_cosine_similarity(all_data, args.output_dir, args.dpi, pfx)

    if "variance" in figures:
        if args.car_variance:
            plot_car_variance(
                args.car_variance, args.output_dir, args.dpi, pfx)
        else:
            print("Skipping variance figure (no --car_variance provided)")

    print("Done.")


if __name__ == "__main__":
    main()
