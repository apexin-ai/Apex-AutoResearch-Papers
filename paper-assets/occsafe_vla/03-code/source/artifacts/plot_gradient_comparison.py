"""
4-condition same-seed gradient comparison plots for OccSafe-VLA.

Reads JSON outputs from same_seed_gradient_analysis.py and produces
publication-quality comparison figures.

Usage:
  python plot_gradient_comparison.py \
    --results_dir /root/occsafe_vla/analysis/same_seed_results \
    --output_dir /root/occsafe_vla/analysis/same_seed_results/figures

  # Or specify individual files:
  python plot_gradient_comparison.py \
    --files full_occ_bn_gradient_stats.json detach_bn_gradient_stats.json \
            full_occ_ln_gradient_stats.json detach_ln_gradient_stats.json \
    --output_dir ./figures

Env: conda activate occsafe
"""

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.ticker as mticker


CONDITION_STYLES = {
    "vanilla":      {"color": "#607D8B", "marker": "x", "ls": ":",  "label": "Vanilla"},
    "full_occ_bn":  {"color": "#2196F3", "marker": "o", "ls": "-",  "label": "Full OCC + BN"},
    "detach_bn":    {"color": "#F44336", "marker": "s", "ls": "--", "label": "Detach + BN"},
    "full_occ_ln":  {"color": "#4CAF50", "marker": "^", "ls": "-",  "label": "Full OCC + LN"},
    "detach_ln":    {"color": "#FF9800", "marker": "D", "ls": "--", "label": "Detach + LN"},
}

BACKBONE_PREFIXES = {
    "featurizer": "DINOv2",
    "fused_featurizer": "SigLIP",
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", type=str, default=None,
                        help="Directory with *_gradient_stats.json files")
    parser.add_argument("--files", nargs="+", default=None,
                        help="Explicit list of JSON stat files")
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--dpi", type=int, default=300)
    return parser.parse_args()


def load_results(args):
    if args.files:
        paths = [Path(f) for f in args.files]
    elif args.results_dir:
        paths = sorted(Path(args.results_dir).glob("*_gradient_stats.json"))
    else:
        raise ValueError("Must specify --results_dir or --files")

    results = {}
    for p in paths:
        with open(p) as f:
            data = json.load(f)
        cond = data["condition"]
        results[cond] = data
        print(f"Loaded {cond}: {p.name}")
    return results


def extract_blocks(per_layer, prefix):
    blocks = []
    for layer_name, stats in per_layer.items():
        if layer_name.startswith(f"{prefix}.blocks."):
            idx = int(layer_name.split(".")[-1])
            blocks.append((idx, stats))
    blocks.sort(key=lambda x: x[0])
    return blocks


def setup_style():
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "DejaVu Serif"],
        "font.size": 10,
        "axes.labelsize": 11,
        "axes.titlesize": 12,
        "legend.fontsize": 9,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "axes.grid": True,
        "grid.alpha": 0.3,
        "grid.linewidth": 0.5,
    })


def get_style(cond):
    if cond in CONDITION_STYLES:
        return CONDITION_STYLES[cond]
    return {"color": "gray", "marker": "x", "ls": "-", "label": cond}


def plot_action_gradient_norms(results, output_dir, dpi):
    """Fig 1: Per-layer action gradient norms across 4 conditions, split by backbone."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 4.5), sharey=True)

    for i, (prefix, backbone_name) in enumerate(BACKBONE_PREFIXES.items()):
        ax = axes[i]
        for cond, data in results.items():
            style = get_style(cond)
            blocks = extract_blocks(data["per_layer"], prefix)
            if not blocks:
                continue
            xs = [b[0] for b in blocks]
            ys = [b[1]["action_grad_norm_mean"] for b in blocks]
            ax.plot(xs, ys, marker=style["marker"], ls=style["ls"],
                    color=style["color"], label=style["label"],
                    markersize=4, linewidth=1.5, alpha=0.85)

        ax.set_xlabel("Block Index")
        ax.set_ylabel("Action Gradient L2 Norm" if i == 0 else "")
        ax.set_title(f"{backbone_name}")
        ax.set_yscale("log")
        ax.legend(loc="best", framealpha=0.9)

    fig.suptitle("Action Gradient Norms per Block (Same Seed)", fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"action_gradient_norms.{ext}"), dpi=dpi)
    plt.close(fig)
    print("Saved: action_gradient_norms.pdf/png")


def plot_occ_gradient_norms(results, output_dir, dpi):
    """Fig 2: OCC gradient norms (only for non-detach conditions)."""
    non_detach = {c: d for c, d in results.items() if not d["occ_detach"]}
    if not non_detach:
        print("No non-detach conditions, skipping occ gradient norms plot")
        return

    fig, axes = plt.subplots(1, 2, figsize=(14, 4.5), sharey=True)

    for i, (prefix, backbone_name) in enumerate(BACKBONE_PREFIXES.items()):
        ax = axes[i]
        for cond, data in non_detach.items():
            style = get_style(cond)
            blocks = extract_blocks(data["per_layer"], prefix)
            if not blocks:
                continue
            xs = [b[0] for b in blocks]
            ys = [b[1]["occ_grad_norm_mean"] for b in blocks]
            ax.plot(xs, ys, marker=style["marker"], ls=style["ls"],
                    color=style["color"], label=style["label"],
                    markersize=4, linewidth=1.5, alpha=0.85)

        ax.set_xlabel("Block Index")
        ax.set_ylabel("OCC Gradient L2 Norm" if i == 0 else "")
        ax.set_title(f"{backbone_name}")
        ax.set_yscale("log")
        ax.legend(loc="best", framealpha=0.9)

    fig.suptitle("OCC Gradient Norms per Block (Non-Detach Only)", fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"occ_gradient_norms.{ext}"), dpi=dpi)
    plt.close(fig)
    print("Saved: occ_gradient_norms.pdf/png")


def plot_gradient_amplification(results, output_dir, dpi):
    """Fig 3: Action gradient ratio (Full OCC / Detach) per backbone, comparing BN vs LN."""
    pairs = [
        ("full_occ_bn", "detach_bn", "BN"),
        ("full_occ_ln", "detach_ln", "LN"),
    ]
    available_pairs = [(f, d, l) for f, d, l in pairs if f in results and d in results]
    if not available_pairs:
        print("No full/detach pairs available, skipping amplification plot")
        return

    fig, axes = plt.subplots(1, 2, figsize=(14, 4.5), sharey=True)
    colors_pair = {"BN": "#9C27B0", "LN": "#009688"}

    for i, (prefix, backbone_name) in enumerate(BACKBONE_PREFIXES.items()):
        ax = axes[i]
        for full_cond, detach_cond, norm_label in available_pairs:
            full_blocks = {b[0]: b[1] for b in extract_blocks(results[full_cond]["per_layer"], prefix)}
            detach_blocks = {b[0]: b[1] for b in extract_blocks(results[detach_cond]["per_layer"], prefix)}
            common = sorted(set(full_blocks) & set(detach_blocks))
            xs, ys = [], []
            for idx in common:
                f_val = full_blocks[idx]["action_grad_norm_mean"]
                d_val = detach_blocks[idx]["action_grad_norm_mean"]
                if f_val > 0 and d_val > 0:
                    xs.append(idx)
                    ys.append(f_val / d_val)
            ax.plot(xs, ys, "o-", color=colors_pair[norm_label],
                    label=f"{norm_label} (Full/Detach)", markersize=4, linewidth=1.5)

        ax.axhline(y=1, color="gray", linestyle="--", alpha=0.5, linewidth=1)
        ax.set_xlabel("Block Index")
        ax.set_ylabel("Gradient Ratio (Full OCC / Detach)" if i == 0 else "")
        ax.set_title(f"{backbone_name}")
        ax.set_yscale("log")
        ax.legend(loc="best", framealpha=0.9)

    fig.suptitle("Action Gradient Amplification by OCC Task", fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"gradient_amplification.{ext}"), dpi=dpi)
    plt.close(fig)
    print("Saved: gradient_amplification.pdf/png")


def plot_cosine_similarity_heatmap(results, output_dir, dpi):
    """Fig 4: Cosine similarity between action and occ gradients (non-detach conditions)."""
    non_detach = {c: d for c, d in results.items() if not d["occ_detach"]}
    if not non_detach:
        print("No non-detach conditions, skipping cosine similarity plot")
        return

    fig, axes = plt.subplots(1, 2, figsize=(14, 4.5), sharey=True)

    for i, (prefix, backbone_name) in enumerate(BACKBONE_PREFIXES.items()):
        ax = axes[i]
        for cond, data in non_detach.items():
            style = get_style(cond)
            blocks = extract_blocks(data["per_layer"], prefix)
            xs, ys = [], []
            for idx, stats in blocks:
                if stats["cosine_sim_mean"] is not None:
                    xs.append(idx)
                    ys.append(stats["cosine_sim_mean"])
            if xs:
                ax.plot(xs, ys, marker=style["marker"], ls=style["ls"],
                        color=style["color"], label=style["label"],
                        markersize=4, linewidth=1.5, alpha=0.85)

        ax.axhline(y=0, color="red", linestyle="--", alpha=0.4, linewidth=1)
        ax.set_xlabel("Block Index")
        ax.set_ylabel("Cosine Similarity" if i == 0 else "")
        ax.set_title(f"{backbone_name}")
        ax.set_ylim(-1, 1)
        ax.legend(loc="best", framealpha=0.9)

    fig.suptitle("Action-OCC Gradient Cosine Similarity per Block", fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"cosine_similarity.{ext}"), dpi=dpi)
    plt.close(fig)
    print("Saved: cosine_similarity.pdf/png")


def plot_conflict_rate(results, output_dir, dpi):
    """Fig 5: Gradient conflict rate (non-detach conditions)."""
    non_detach = {c: d for c, d in results.items() if not d["occ_detach"]}
    if not non_detach:
        print("No non-detach conditions, skipping conflict rate plot")
        return

    fig, axes = plt.subplots(1, 2, figsize=(14, 4.5), sharey=True)

    for i, (prefix, backbone_name) in enumerate(BACKBONE_PREFIXES.items()):
        ax = axes[i]
        n_conds = len(non_detach)
        bar_w = 0.8 / max(n_conds, 1)

        for j, (cond, data) in enumerate(non_detach.items()):
            style = get_style(cond)
            blocks = extract_blocks(data["per_layer"], prefix)
            xs, ys = [], []
            for idx, stats in blocks:
                if stats["conflict_rate"] is not None:
                    xs.append(idx)
                    ys.append(stats["conflict_rate"])
            offset = (j - (n_conds - 1) / 2) * bar_w
            if xs:
                ax.bar([x + offset for x in xs], ys, width=bar_w,
                       color=style["color"], label=style["label"], alpha=0.7)

        ax.set_xlabel("Block Index")
        ax.set_ylabel("Conflict Rate" if i == 0 else "")
        ax.set_title(f"{backbone_name}")
        ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))
        ax.legend(loc="best", framealpha=0.9)

    fig.suptitle("Gradient Conflict Rate per Block (cosine < 0)", fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"conflict_rate.{ext}"), dpi=dpi)
    plt.close(fig)
    print("Saved: conflict_rate.pdf/png")


def plot_bn_drift(results, output_dir, dpi):
    """Fig 6: BN running stats drift comparison (BN conditions only)."""
    bn_conds = {c: d for c, d in results.items()
                if d.get("occ_norm") == "bn" and d.get("bn_drift")}
    if not bn_conds:
        print("No BN conditions with drift data, skipping BN drift plot")
        return

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    # Collect BN layer names
    all_bn_layers = set()
    for data in bn_conds.values():
        all_bn_layers.update(data["bn_drift"].keys())
    bn_layer_names = sorted(all_bn_layers)

    # Mean drift
    ax = axes[0]
    x = np.arange(len(bn_layer_names))
    bar_w = 0.8 / len(bn_conds)
    for j, (cond, data) in enumerate(bn_conds.items()):
        style = get_style(cond)
        ys = []
        for layer in bn_layer_names:
            if layer in data["bn_drift"]:
                ys.append(data["bn_drift"][layer]["mean_drift_l2"])
            else:
                ys.append(0)
        offset = (j - (len(bn_conds) - 1) / 2) * bar_w
        ax.bar(x + offset, ys, width=bar_w, color=style["color"],
               label=style["label"], alpha=0.8)
    ax.set_xlabel("BN Layer")
    ax.set_ylabel("L2 Norm of running_mean")
    ax.set_title("BN Running Mean Drift from Init")
    ax.set_xticks(x)
    ax.set_xticklabels([n.replace("decoder.", "d.") for n in bn_layer_names],
                       rotation=30, ha="right")
    ax.legend(framealpha=0.9)

    # Var drift
    ax = axes[1]
    for j, (cond, data) in enumerate(bn_conds.items()):
        style = get_style(cond)
        ys = []
        for layer in bn_layer_names:
            if layer in data["bn_drift"]:
                ys.append(data["bn_drift"][layer]["var_drift_from_one_l2"])
            else:
                ys.append(0)
        offset = (j - (len(bn_conds) - 1) / 2) * bar_w
        ax.bar(x + offset, ys, width=bar_w, color=style["color"],
               label=style["label"], alpha=0.8)
    ax.set_xlabel("BN Layer")
    ax.set_ylabel("L2 Norm of (running_var - 1)")
    ax.set_title("BN Running Var Drift from Init")
    ax.set_xticks(x)
    ax.set_xticklabels([n.replace("decoder.", "d.") for n in bn_layer_names],
                       rotation=30, ha="right")
    ax.legend(framealpha=0.9)

    fig.suptitle("BN Running Stats Drift: Full OCC vs Detach",
                 fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"bn_drift.{ext}"), dpi=dpi)
    plt.close(fig)
    print("Saved: bn_drift.pdf/png")


def plot_combined_summary(results, output_dir, dpi):
    """Fig 7: Combined 2x3 summary figure for paper."""
    fig = plt.figure(figsize=(18, 10))
    gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3)

    prefix = "featurizer"  # DINOv2 as main backbone for summary

    # (0,0) Action gradient norms
    ax = fig.add_subplot(gs[0, 0])
    for cond, data in results.items():
        style = get_style(cond)
        blocks = extract_blocks(data["per_layer"], prefix)
        if blocks:
            xs = [b[0] for b in blocks]
            ys = [b[1]["action_grad_norm_mean"] for b in blocks]
            ax.plot(xs, ys, marker=style["marker"], ls=style["ls"],
                    color=style["color"], label=style["label"],
                    markersize=3, linewidth=1.2, alpha=0.85)
    ax.set_xlabel("DINOv2 Block")
    ax.set_ylabel("L2 Norm")
    ax.set_title("(a) Action Grad Norms")
    ax.set_yscale("log")
    ax.legend(fontsize=7, loc="best")

    # (0,1) OCC gradient norms (non-detach)
    ax = fig.add_subplot(gs[0, 1])
    for cond, data in results.items():
        if data["occ_detach"]:
            continue
        style = get_style(cond)
        blocks = extract_blocks(data["per_layer"], prefix)
        if blocks:
            xs = [b[0] for b in blocks]
            ys = [b[1]["occ_grad_norm_mean"] for b in blocks]
            ax.plot(xs, ys, marker=style["marker"], ls=style["ls"],
                    color=style["color"], label=style["label"],
                    markersize=3, linewidth=1.2, alpha=0.85)
    ax.set_xlabel("DINOv2 Block")
    ax.set_ylabel("L2 Norm")
    ax.set_title("(b) OCC Grad Norms")
    ax.set_yscale("log")
    ax.legend(fontsize=7, loc="best")

    # (0,2) Gradient amplification ratio
    ax = fig.add_subplot(gs[0, 2])
    pairs = [("full_occ_bn", "detach_bn", "BN", "#9C27B0"),
             ("full_occ_ln", "detach_ln", "LN", "#009688")]
    for full_c, det_c, nl, clr in pairs:
        if full_c in results and det_c in results:
            fb = {b[0]: b[1] for b in extract_blocks(results[full_c]["per_layer"], prefix)}
            db = {b[0]: b[1] for b in extract_blocks(results[det_c]["per_layer"], prefix)}
            common = sorted(set(fb) & set(db))
            xs, ys = [], []
            for idx in common:
                fv = fb[idx]["action_grad_norm_mean"]
                dv = db[idx]["action_grad_norm_mean"]
                if fv > 0 and dv > 0:
                    xs.append(idx)
                    ys.append(fv / dv)
            ax.plot(xs, ys, "o-", color=clr, label=f"{nl}", markersize=3, linewidth=1.2)
    ax.axhline(y=1, color="gray", linestyle="--", alpha=0.5)
    ax.set_xlabel("DINOv2 Block")
    ax.set_ylabel("Ratio")
    ax.set_title("(c) Amplification (Full/Detach)")
    ax.set_yscale("log")
    ax.legend(fontsize=7, loc="best")

    # (1,0) Cosine similarity
    ax = fig.add_subplot(gs[1, 0])
    for cond, data in results.items():
        if data["occ_detach"]:
            continue
        style = get_style(cond)
        blocks = extract_blocks(data["per_layer"], prefix)
        xs, ys = [], []
        for idx, stats in blocks:
            if stats["cosine_sim_mean"] is not None:
                xs.append(idx)
                ys.append(stats["cosine_sim_mean"])
        if xs:
            ax.plot(xs, ys, marker=style["marker"], ls=style["ls"],
                    color=style["color"], label=style["label"],
                    markersize=3, linewidth=1.2, alpha=0.85)
    ax.axhline(y=0, color="red", linestyle="--", alpha=0.4)
    ax.set_xlabel("DINOv2 Block")
    ax.set_ylabel("Cosine Sim")
    ax.set_title("(d) Action-OCC Cosine Similarity")
    ax.set_ylim(-1, 1)
    ax.legend(fontsize=7, loc="best")

    # (1,1) Conflict rate
    ax = fig.add_subplot(gs[1, 1])
    non_detach = {c: d for c, d in results.items() if not d["occ_detach"]}
    n_conds = len(non_detach)
    bar_w = 0.8 / max(n_conds, 1)
    for j, (cond, data) in enumerate(non_detach.items()):
        style = get_style(cond)
        blocks = extract_blocks(data["per_layer"], prefix)
        xs, ys = [], []
        for idx, stats in blocks:
            if stats["conflict_rate"] is not None:
                xs.append(idx)
                ys.append(stats["conflict_rate"])
        offset = (j - (n_conds - 1) / 2) * bar_w
        if xs:
            ax.bar([x + offset for x in xs], ys, width=bar_w,
                   color=style["color"], label=style["label"], alpha=0.7)
    ax.set_xlabel("DINOv2 Block")
    ax.set_ylabel("Conflict Rate")
    ax.set_title("(e) Gradient Conflict Rate")
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))
    ax.legend(fontsize=7, loc="best")

    # (1,2) BN drift
    ax = fig.add_subplot(gs[1, 2])
    bn_conds = {c: d for c, d in results.items()
                if d.get("occ_norm") == "bn" and d.get("bn_drift")}
    if bn_conds:
        all_bn = set()
        for d in bn_conds.values():
            all_bn.update(d["bn_drift"].keys())
        bn_names = sorted(all_bn)
        x = np.arange(len(bn_names))
        bw = 0.8 / len(bn_conds)
        for j, (cond, data) in enumerate(bn_conds.items()):
            style = get_style(cond)
            ys = [data["bn_drift"].get(n, {}).get("mean_drift_l2", 0) for n in bn_names]
            offset = (j - (len(bn_conds) - 1) / 2) * bw
            ax.bar(x + offset, ys, width=bw, color=style["color"],
                   label=style["label"], alpha=0.8)
        ax.set_xticks(x)
        ax.set_xticklabels([n.split(".")[-1] for n in bn_names], rotation=30, ha="right")
        ax.legend(fontsize=7)
    else:
        ax.text(0.5, 0.5, "No BN data", transform=ax.transAxes,
                ha="center", va="center", fontsize=14, color="gray")
    ax.set_xlabel("BN Layer")
    ax.set_ylabel("Mean Drift L2")
    ax.set_title("(f) BN Running Stats Drift")

    fig.suptitle("Same-Seed Gradient Analysis: 4-Condition Comparison (DINOv2)",
                 fontsize=14, fontweight="bold", y=0.98)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"gradient_summary.{ext}"), dpi=dpi)
    plt.close(fig)
    print("Saved: gradient_summary.pdf/png")


def print_summary_table(results):
    """Print markdown-style summary table."""
    print("\n## Summary Table\n")
    print("| Condition | Avg Act Loss | Avg OCC Loss | Mean Act Grad (DINOv2) | Mean Act Grad (SigLIP) |")
    print("|-----------|-------------|-------------|----------------------|----------------------|")
    for cond, data in results.items():
        dino_blocks = extract_blocks(data["per_layer"], "featurizer")
        siglip_blocks = extract_blocks(data["per_layer"], "fused_featurizer")
        dino_mean = np.mean([b[1]["action_grad_norm_mean"] for b in dino_blocks]) if dino_blocks else 0
        siglip_mean = np.mean([b[1]["action_grad_norm_mean"] for b in siglip_blocks]) if siglip_blocks else 0
        label = CONDITION_STYLES.get(cond, {}).get("label", cond)
        print(f"| {label} | {data['avg_action_loss']:.4f} | {data['avg_occ_loss']:.4f} | "
              f"{dino_mean:.6f} | {siglip_mean:.6f} |")

    # Amplification ratios
    pairs = [("full_occ_bn", "detach_bn", "BN"), ("full_occ_ln", "detach_ln", "LN")]
    available = [(f, d, l) for f, d, l in pairs if f in results and d in results]
    if available:
        print("\n## Gradient Amplification (Full OCC / Detach)\n")
        print("| Norm | Backbone | Mean Ratio | Median Ratio | Range |")
        print("|------|----------|-----------|-------------|-------|")
        for full_c, det_c, nl in available:
            for prefix, bname in BACKBONE_PREFIXES.items():
                fb = {b[0]: b[1] for b in extract_blocks(results[full_c]["per_layer"], prefix)}
                db = {b[0]: b[1] for b in extract_blocks(results[det_c]["per_layer"], prefix)}
                ratios = []
                for idx in sorted(set(fb) & set(db)):
                    fv = fb[idx]["action_grad_norm_mean"]
                    dv = db[idx]["action_grad_norm_mean"]
                    if fv > 0 and dv > 0:
                        ratios.append(fv / dv)
                if ratios:
                    print(f"| {nl} | {bname} | {np.mean(ratios):.1f}x | "
                          f"{np.median(ratios):.1f}x | [{np.min(ratios):.1f}x, {np.max(ratios):.1f}x] |")


def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    setup_style()

    results = load_results(args)
    if not results:
        print("No results found!")
        sys.exit(1)

    print(f"\nLoaded {len(results)} conditions: {list(results.keys())}")

    plot_action_gradient_norms(results, args.output_dir, args.dpi)
    plot_occ_gradient_norms(results, args.output_dir, args.dpi)
    plot_gradient_amplification(results, args.output_dir, args.dpi)
    plot_cosine_similarity_heatmap(results, args.output_dir, args.dpi)
    plot_conflict_rate(results, args.output_dir, args.dpi)
    plot_bn_drift(results, args.output_dir, args.dpi)
    plot_combined_summary(results, args.output_dir, args.dpi)

    print_summary_table(results)

    print(f"\nAll figures saved to {args.output_dir}")


if __name__ == "__main__":
    main()
