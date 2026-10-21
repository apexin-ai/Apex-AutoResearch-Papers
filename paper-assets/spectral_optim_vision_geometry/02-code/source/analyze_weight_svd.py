"""
Weight Matrix SVD Analysis for Spectral Optimizer Comparison (D215b)

Analyzes singular value distributions of trained ResNet50 weight matrices across
different optimizers (Muon/SOAP/Shampoo vs AdamW/SGD) and normalization layers (BN/LN).

Input:  Checkpoint files from /root/autodl-tmp/checkpoints/spectral_optim/
Output: stdout summary, svd_results.json, PNG visualizations
"""

import json
import os
import sys
from collections import defaultdict

import torch
import numpy as np

CKPT_DIR = "/root/autodl-tmp/checkpoints/spectral_optim"
OUT_DIR = "/root/autodl-tmp/checkpoints/spectral_optim/svd_analysis"

# Checkpoints to analyze: (display_name, filename)
CHECKPOINTS = {
    # BN variants (seed 42)
    "Muon-BN":    "resnet50_muon_s42_best.pt",
    "AdamW-BN":   "resnet50_adamw_s42_lr1e-3_best.pt",
    "SGD-BN":     "resnet50_sgd_s42_lr1e-1_best.pt",
    "SOAP-BN":    "resnet50_soap_s42_lr1e-2_best.pt",
    "Shampoo-BN": "resnet50_shampoo_s42_lr7e-3_best.pt",
    # LN variants (seed 42)
    "Muon-LN":    "resnet50_ln_muon_s42_best.pt",
    "AdamW-LN":   "resnet50_ln_adamw_s42_lr1e-3_best.pt",
    "SGD-LN":     "resnet50_ln_sgd_s42_lr1e-1_best.pt",
}


def get_depth_group(layer_name: str) -> str:
    """Map a parameter name to its depth group in ResNet50."""
    if layer_name.startswith("conv1") or layer_name.startswith("bn1") or layer_name.startswith("ln1"):
        return "stem"
    for g in ["layer1", "layer2", "layer3", "layer4"]:
        if layer_name.startswith(g):
            return g
    if layer_name.startswith("fc"):
        return "fc"
    return "other"


def extract_weight_matrices(state_dict: dict) -> list:
    """
    Extract all conv/linear weight matrices from state_dict.
    Returns list of (name, tensor_2d) tuples.
    """
    matrices = []
    for name, param in state_dict.items():
        if not name.endswith(".weight"):
            continue
        # Skip norm layers (BN/LN/GN scale params are 1D)
        if param.dim() < 2:
            continue
        # Reshape to 2D: (out_features, in_features * kernel)
        t = param.detach().float()
        if t.dim() > 2:
            t = t.reshape(t.shape[0], -1)
        matrices.append((name, t))
    return matrices


def compute_svd_metrics(matrix: torch.Tensor, top_k: int = 10) -> dict:
    """
    Compute SVD-based metrics for a 2D weight matrix.

    Returns dict with: singular_values (all), top_k_sv, condition_number,
    stable_rank, effective_dim, frobenius_norm, spectral_norm.
    """
    sv = torch.linalg.svdvals(matrix)
    sv_np = sv.cpu().numpy().tolist()

    sigma_max = sv[0].item()
    # Use top-k smallest nonzero SV for condition number (avoid near-zero)
    nonzero_sv = sv[sv > 1e-8]
    sigma_min = nonzero_sv[-1].item() if len(nonzero_sv) > 0 else 1e-8

    frob_sq = (sv ** 2).sum().item()
    spec_sq = sigma_max ** 2

    sv_sum = sv.sum().item()
    sv_sq_sum = (sv ** 2).sum().item()

    return {
        "shape": list(matrix.shape),
        "num_singular_values": len(sv_np),
        "top10_sv": sv_np[:top_k],
        "condition_number": sigma_max / sigma_min,
        "stable_rank": frob_sq / spec_sq if spec_sq > 0 else float("inf"),
        "effective_dim": (sv_sum ** 2) / sv_sq_sum if sv_sq_sum > 0 else 0.0,
        "frobenius_norm": frob_sq ** 0.5,
        "spectral_norm": sigma_max,
        "all_sv": sv_np,
    }


def analyze_checkpoint(name: str, path: str) -> dict:
    """Analyze all weight matrices in a checkpoint."""
    ckpt = torch.load(path, map_location="cpu", weights_only=False)
    state_dict = ckpt.get("state_dict", ckpt)

    val_acc = ckpt.get("val_acc", None)
    epoch = ckpt.get("epoch", None)

    matrices = extract_weight_matrices(state_dict)
    results = {
        "val_acc": val_acc,
        "epoch": epoch,
        "layers": {},
        "depth_groups": defaultdict(list),
    }

    for layer_name, mat in matrices:
        metrics = compute_svd_metrics(mat)
        depth = get_depth_group(layer_name)
        metrics["depth_group"] = depth
        results["layers"][layer_name] = metrics
        results["depth_groups"][depth].append({
            "layer": layer_name,
            "condition_number": metrics["condition_number"],
            "stable_rank": metrics["stable_rank"],
            "effective_dim": metrics["effective_dim"],
            "spectral_norm": metrics["spectral_norm"],
            "frobenius_norm": metrics["frobenius_norm"],
        })

    # Convert defaultdict to dict for JSON
    results["depth_groups"] = dict(results["depth_groups"])
    return results


def aggregate_depth_stats(results: dict) -> dict:
    """Compute per-depth-group aggregate statistics."""
    agg = {}
    for depth, layers in results["depth_groups"].items():
        conds = [l["condition_number"] for l in layers]
        sranks = [l["stable_rank"] for l in layers]
        edims = [l["effective_dim"] for l in layers]
        snorms = [l["spectral_norm"] for l in layers]
        agg[depth] = {
            "num_layers": len(layers),
            "condition_number": {"mean": np.mean(conds), "median": np.median(conds), "max": np.max(conds), "min": np.min(conds)},
            "stable_rank": {"mean": np.mean(sranks), "median": np.median(sranks), "max": np.max(sranks), "min": np.min(sranks)},
            "effective_dim": {"mean": np.mean(edims), "median": np.median(edims), "max": np.max(edims), "min": np.min(edims)},
            "spectral_norm": {"mean": np.mean(snorms), "median": np.median(snorms), "max": np.max(snorms), "min": np.min(snorms)},
        }
    return agg


def print_summary(all_results: dict):
    """Print formatted summary to stdout."""
    # Header
    print("=" * 100)
    print("D215b: Weight Matrix SVD Analysis — Spectral Optimizers vs Baselines")
    print("=" * 100)

    # Per-optimizer summary
    for opt_name, res in all_results.items():
        acc_str = f"{res['val_acc']:.2f}%" if res['val_acc'] is not None else "N/A"
        print(f"\n{'─' * 80}")
        print(f"  {opt_name}  (val_acc={acc_str}, epoch={res.get('epoch', '?')})")
        print(f"{'─' * 80}")

        agg = aggregate_depth_stats(res)
        depth_order = ["stem", "layer1", "layer2", "layer3", "layer4", "fc"]
        existing = [d for d in depth_order if d in agg]

        print(f"  {'Depth':<8} {'#Layers':>7} {'CondNum(med)':>14} {'CondNum(max)':>14} {'StableRank(med)':>16} {'EffDim(med)':>14} {'SpecNorm(med)':>15}")
        for depth in existing:
            s = agg[depth]
            print(f"  {depth:<8} {s['num_layers']:>7d} {s['condition_number']['median']:>14.2f} {s['condition_number']['max']:>14.2f} {s['stable_rank']['median']:>16.2f} {s['effective_dim']['median']:>14.2f} {s['spectral_norm']['median']:>15.4f}")

    # Cross-optimizer comparison table
    print(f"\n{'=' * 100}")
    print("CROSS-OPTIMIZER COMPARISON (whole-model aggregates)")
    print(f"{'=' * 100}")
    print(f"  {'Optimizer':<14} {'Val Acc':>8} {'Cond(med)':>11} {'Cond(mean)':>11} {'Cond(max)':>11} {'SRank(med)':>11} {'EDim(med)':>11} {'SN(med)':>9}")

    for opt_name, res in all_results.items():
        all_conds = [m["condition_number"] for m in res["layers"].values()]
        all_sranks = [m["stable_rank"] for m in res["layers"].values()]
        all_edims = [m["effective_dim"] for m in res["layers"].values()]
        all_snorms = [m["spectral_norm"] for m in res["layers"].values()]
        acc_str = f"{res['val_acc']:.2f}" if res['val_acc'] is not None else "N/A"
        print(f"  {opt_name:<14} {acc_str:>8} {np.median(all_conds):>11.2f} {np.mean(all_conds):>11.2f} {np.max(all_conds):>11.2f} {np.median(all_sranks):>11.2f} {np.median(all_edims):>11.2f} {np.median(all_snorms):>9.4f}")

    # BN vs LN comparison
    bn_opts = [k for k in all_results if k.endswith("-BN")]
    ln_opts = [k for k in all_results if k.endswith("-LN")]
    if bn_opts and ln_opts:
        print(f"\n{'=' * 100}")
        print("BN vs LN COMPARISON (same optimizer)")
        print(f"{'=' * 100}")
        for bn_name in bn_opts:
            base = bn_name.replace("-BN", "")
            ln_name = f"{base}-LN"
            if ln_name not in all_results:
                continue
            bn = all_results[bn_name]
            ln = all_results[ln_name]
            bn_conds = [m["condition_number"] for m in bn["layers"].values()]
            ln_conds = [m["condition_number"] for m in ln["layers"].values()]
            bn_sranks = [m["stable_rank"] for m in bn["layers"].values()]
            ln_sranks = [m["stable_rank"] for m in ln["layers"].values()]
            print(f"  {base:<10}  BN cond_med={np.median(bn_conds):.2f}  LN cond_med={np.median(ln_conds):.2f}  "
                  f"BN srank_med={np.median(bn_sranks):.2f}  LN srank_med={np.median(ln_sranks):.2f}")


def make_plots(all_results: dict, out_dir: str):
    """Generate visualization plots."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # ---- Plot 1: Condition number by depth group ----
    fig, axes = plt.subplots(1, 5, figsize=(22, 5), sharey=True)
    depth_order = ["stem", "layer1", "layer2", "layer3", "layer4"]
    # Separate BN and LN
    bn_opts = {k: v for k, v in all_results.items() if k.endswith("-BN")}
    colors = {"Muon-BN": "#e41a1c", "AdamW-BN": "#377eb8", "SGD-BN": "#4daf4a",
              "SOAP-BN": "#ff7f00", "Shampoo-BN": "#984ea3",
              "Muon-LN": "#e41a1c", "AdamW-LN": "#377eb8", "SGD-LN": "#4daf4a"}

    for idx, depth in enumerate(depth_order):
        ax = axes[idx]
        for opt_name, res in bn_opts.items():
            agg = aggregate_depth_stats(res)
            if depth in agg:
                layers = res["depth_groups"][depth]
                conds = sorted([l["condition_number"] for l in layers])
                ax.plot(range(len(conds)), conds, "o-", label=opt_name,
                        color=colors.get(opt_name, "gray"), markersize=3, alpha=0.8)
        ax.set_title(depth, fontsize=12)
        ax.set_xlabel("Layer index (sorted)")
        if idx == 0:
            ax.set_ylabel("Condition Number")
        ax.set_yscale("log")
        ax.grid(True, alpha=0.3)
        if idx == 4:
            ax.legend(fontsize=7, loc="upper left")

    fig.suptitle("Condition Number by Depth Group (BN models, sorted per group)", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "condition_number_by_depth.png"), dpi=150)
    plt.close()
    print(f"\n  Saved: condition_number_by_depth.png")

    # ---- Plot 2: Stable rank by depth group ----
    fig, axes = plt.subplots(1, 5, figsize=(22, 5), sharey=True)
    for idx, depth in enumerate(depth_order):
        ax = axes[idx]
        for opt_name, res in bn_opts.items():
            if depth in res["depth_groups"]:
                layers = res["depth_groups"][depth]
                sranks = sorted([l["stable_rank"] for l in layers])
                ax.plot(range(len(sranks)), sranks, "o-", label=opt_name,
                        color=colors.get(opt_name, "gray"), markersize=3, alpha=0.8)
        ax.set_title(depth, fontsize=12)
        ax.set_xlabel("Layer index (sorted)")
        if idx == 0:
            ax.set_ylabel("Stable Rank")
        ax.grid(True, alpha=0.3)
        if idx == 4:
            ax.legend(fontsize=7, loc="upper left")

    fig.suptitle("Stable Rank by Depth Group (BN models, sorted per group)", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "stable_rank_by_depth.png"), dpi=150)
    plt.close()
    print(f"  Saved: stable_rank_by_depth.png")

    # ---- Plot 3: SV spectrum comparison for select layers ----
    target_layers = [
        "layer2.0.conv2.weight",
        "layer3.0.conv2.weight",
        "layer4.0.conv2.weight",
    ]
    fig, axes = plt.subplots(1, len(target_layers), figsize=(6 * len(target_layers), 5))
    if len(target_layers) == 1:
        axes = [axes]

    for idx, layer_name in enumerate(target_layers):
        ax = axes[idx]
        for opt_name, res in bn_opts.items():
            if layer_name in res["layers"]:
                sv = res["layers"][layer_name]["all_sv"]
                sv_norm = [s / sv[0] for s in sv]  # Normalize by top SV
                ax.plot(sv_norm, label=opt_name, color=colors.get(opt_name, "gray"), alpha=0.8)
        ax.set_title(layer_name, fontsize=10)
        ax.set_xlabel("Singular value index")
        if idx == 0:
            ax.set_ylabel("Normalized SV (sigma_i / sigma_1)")
        ax.set_yscale("log")
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=7)

    fig.suptitle("Normalized Singular Value Spectrum (BN models)", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "sv_spectrum_comparison.png"), dpi=150)
    plt.close()
    print(f"  Saved: sv_spectrum_comparison.png")

    # ---- Plot 4: Cross-optimizer bar chart (whole model medians) ----
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    metrics_to_plot = [
        ("condition_number", "Condition Number (median)", True),
        ("stable_rank", "Stable Rank (median)", False),
        ("effective_dim", "Effective Dimension (median)", False),
    ]
    opt_names_bn = list(bn_opts.keys())
    x = np.arange(len(opt_names_bn))

    for ax_idx, (metric, title, use_log) in enumerate(metrics_to_plot):
        ax = axes[ax_idx]
        vals = []
        for opt_name in opt_names_bn:
            layer_vals = [m[metric] for m in all_results[opt_name]["layers"].values()]
            vals.append(np.median(layer_vals))
        bars = ax.bar(x, vals, color=[colors.get(n, "gray") for n in opt_names_bn], alpha=0.8)
        ax.set_xticks(x)
        ax.set_xticklabels([n.replace("-BN", "") for n in opt_names_bn], rotation=30)
        ax.set_title(title)
        if use_log:
            ax.set_yscale("log")
        ax.grid(True, alpha=0.3, axis="y")
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2., bar.get_height(),
                    f"{val:.1f}", ha="center", va="bottom", fontsize=8)

    fig.suptitle("Whole-Model SVD Metrics Comparison (BN, median across layers)", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "svd_metrics_barplot.png"), dpi=150)
    plt.close()
    print(f"  Saved: svd_metrics_barplot.png")

    # ---- Plot 5: BN vs LN comparison ----
    ln_opts_avail = {k: v for k, v in all_results.items() if k.endswith("-LN")}
    if ln_opts_avail:
        pairs = []
        for bn_name in bn_opts:
            ln_name = bn_name.replace("-BN", "-LN")
            if ln_name in all_results:
                pairs.append((bn_name, ln_name))

        if pairs:
            fig, axes = plt.subplots(1, len(pairs), figsize=(6 * len(pairs), 5))
            if len(pairs) == 1:
                axes = [axes]
            for idx, (bn_name, ln_name) in enumerate(pairs):
                ax = axes[idx]
                bn_agg = aggregate_depth_stats(all_results[bn_name])
                ln_agg = aggregate_depth_stats(all_results[ln_name])
                depths = [d for d in depth_order if d in bn_agg and d in ln_agg]
                x = np.arange(len(depths))
                w = 0.35
                bn_vals = [bn_agg[d]["condition_number"]["median"] for d in depths]
                ln_vals = [ln_agg[d]["condition_number"]["median"] for d in depths]
                ax.bar(x - w/2, bn_vals, w, label="BN", alpha=0.8, color="#377eb8")
                ax.bar(x + w/2, ln_vals, w, label="LN", alpha=0.8, color="#e41a1c")
                ax.set_xticks(x)
                ax.set_xticklabels(depths)
                ax.set_ylabel("Condition Number (median)")
                ax.set_title(bn_name.replace("-BN", ""))
                ax.set_yscale("log")
                ax.legend()
                ax.grid(True, alpha=0.3, axis="y")

            fig.suptitle("BN vs LN: Condition Number by Depth", fontsize=14)
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, "bn_vs_ln_condition.png"), dpi=150)
            plt.close()
            print(f"  Saved: bn_vs_ln_condition.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    all_results = {}
    for name, filename in CHECKPOINTS.items():
        path = os.path.join(CKPT_DIR, filename)
        if not os.path.exists(path):
            print(f"  [SKIP] {name}: {filename} not found")
            continue
        print(f"  Analyzing {name} ({filename})...")
        all_results[name] = analyze_checkpoint(name, path)
        print(f"    -> {len(all_results[name]['layers'])} weight matrices analyzed")

    if not all_results:
        print("ERROR: No checkpoints found!")
        sys.exit(1)

    # Print summary
    print_summary(all_results)

    # Save JSON (without full SV arrays to keep size manageable)
    json_results = {}
    for opt_name, res in all_results.items():
        json_results[opt_name] = {
            "val_acc": res["val_acc"],
            "epoch": res["epoch"],
            "layers": {},
            "depth_groups": res["depth_groups"],
        }
        for layer_name, metrics in res["layers"].items():
            json_results[opt_name]["layers"][layer_name] = {
                k: v for k, v in metrics.items() if k != "all_sv"
            }

    json_path = os.path.join(OUT_DIR, "svd_results.json")
    with open(json_path, "w") as f:
        json.dump(json_results, f, indent=2, default=lambda x: float(x) if isinstance(x, (np.floating, np.integer)) else x)
    print(f"\n  Saved JSON: {json_path}")

    # Generate plots
    try:
        make_plots(all_results, OUT_DIR)
    except Exception as e:
        print(f"  [WARN] Plot generation failed: {e}")

    print(f"\n  All outputs saved to: {OUT_DIR}")


if __name__ == "__main__":
    main()
