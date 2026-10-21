#!/usr/bin/env python3
"""SCS v3 spectral analysis: ConvNeXt-T CIFAR-100 (Muon/AdamW/SGD, T_max=20)."""
import os
import sys
import json

import numpy as np
import torch
import timm

sys.path.insert(0, "/root/spectral_optim_vision_geometry/scripts/spectral_analysis")
from spectral_structure import compute_spectral_metrics, reshape_for_svd, should_analyze, get_layer_type

CKPT_DIR = "/root/spectral_optim_vision_geometry/checkpoints/scs_v3"
OUT_DIR = "/root/spectral_optim_vision_geometry/results/spectral_analysis"


def find_checkpoint(optimizer_name):
    """Find the ep20 or best checkpoint for a given optimizer."""
    for f in sorted(os.listdir(CKPT_DIR), reverse=True):
        if f.startswith(f"convnext_t_{optimizer_name}_") and f.endswith(".pt"):
            if "_ep20.pt" in f:
                return os.path.join(CKPT_DIR, f)
    for f in sorted(os.listdir(CKPT_DIR), reverse=True):
        if f.startswith(f"convnext_t_{optimizer_name}_") and f.endswith(".pt"):
            if "_best.pt" in f:
                return os.path.join(CKPT_DIR, f)
    return None


def analyze_checkpoint(model_name, ckpt_path):
    print(f"\n{'='*60}")
    print(f"Analyzing {model_name}: {ckpt_path}")

    model = timm.create_model("convnext_tiny", pretrained=False, num_classes=100)
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    state_dict = ckpt.get("state_dict", ckpt)
    model.load_state_dict(state_dict)
    model.eval()

    val_acc = ckpt.get("val_acc", None)
    epoch = ckpt.get("epoch", None)
    T_max = ckpt.get("T_max", None)
    print(f"  val_acc={val_acc}, epoch={epoch}, T_max={T_max}")

    results = []
    for name, param in model.named_parameters():
        if not should_analyze(name, param.data):
            continue
        weight = param.data
        layer_type = get_layer_type(name, weight, "hybrid")
        if layer_type == "other":
            continue
        W_2d = reshape_for_svd(weight, layer_type)
        if W_2d is None or min(W_2d.shape) < 2:
            continue
        metrics = compute_spectral_metrics(W_2d)
        if metrics is None:
            continue
        results.append({
            "layer_name": name,
            "layer_type": layer_type,
            "shape": str(list(weight.shape)),
            "condition_number": metrics["condition_number"],
            "effective_rank": metrics["effective_rank"],
            "stable_rank": metrics["stable_rank"],
            "spectral_gap": metrics["spectral_gap"],
            "spectral_decay_exponent": metrics["spectral_decay_exponent"],
        })
    print(f"  -> {len(results)} layers analyzed")
    return results, val_acc, epoch


def summarize(results):
    conds = [r["condition_number"] for r in results]
    eranks = [r["effective_rank"] for r in results]
    sranks = [r["stable_rank"] for r in results]
    sgaps = [r["spectral_gap"] for r in results]
    decays = [r["spectral_decay_exponent"] for r in results]
    return {
        "n_layers": len(results),
        "stable_rank": {"mean": float(np.mean(sranks)), "median": float(np.median(sranks)), "std": float(np.std(sranks))},
        "effective_rank": {"mean": float(np.mean(eranks)), "median": float(np.median(eranks)), "std": float(np.std(eranks))},
        "condition_number": {"mean": float(np.mean(conds)), "median": float(np.median(conds)), "std": float(np.std(conds))},
        "spectral_gap": {"mean": float(np.mean(sgaps)), "median": float(np.median(sgaps)), "std": float(np.std(sgaps))},
        "spectral_decay_exponent": {"mean": float(np.mean(decays)), "median": float(np.median(decays)), "std": float(np.std(decays))},
    }


def main():
    optimizers = ["muon", "adamw", "sgd"]
    summary = {}

    for opt_name in optimizers:
        ckpt_path = find_checkpoint(opt_name)
        if ckpt_path is None:
            print(f"WARNING: no checkpoint found for {opt_name} in {CKPT_DIR}")
            continue
        model_key = f"convnext_tiny_{opt_name}"
        results, val_acc, epoch = analyze_checkpoint(model_key, ckpt_path)
        if results:
            s = summarize(results)
            s["val_acc"] = float(val_acc) if val_acc is not None else None
            s["epoch"] = int(epoch) if epoch is not None else None
            summary[model_key] = s

    # Cross-optimizer comparison
    comparison = {}
    if "convnext_tiny_muon" in summary and "convnext_tiny_adamw" in summary:
        muon_sr = summary["convnext_tiny_muon"]["stable_rank"]["mean"]
        adamw_sr = summary["convnext_tiny_adamw"]["stable_rank"]["mean"]
        comparison["muon_adamw_sr_ratio"] = float(muon_sr / adamw_sr)
    if "convnext_tiny_muon" in summary and "convnext_tiny_sgd" in summary:
        muon_sr = summary["convnext_tiny_muon"]["stable_rank"]["mean"]
        sgd_sr = summary["convnext_tiny_sgd"]["stable_rank"]["mean"]
        comparison["muon_sgd_sr_ratio"] = float(muon_sr / sgd_sr)
    if comparison:
        summary["cross_optimizer_comparison"] = comparison

    # Print summary table
    print(f"\n{'='*80}")
    print("SCS v3 SUMMARY: ConvNeXt-T CIFAR-100 (T_max=epochs)")
    print(f"{'='*80}")
    fmt = "{:<25} {:>10} {:>10} {:>10} {:>12} {:>10} {:>10}"
    print(fmt.format("Model", "val_acc", "eff_rank", "stbl_rank", "cond_num", "spc_gap", "decay_a"))
    print("-" * 90)
    for mname in ["convnext_tiny_muon", "convnext_tiny_adamw", "convnext_tiny_sgd"]:
        if mname not in summary:
            continue
        s = summary[mname]
        print(fmt.format(
            mname,
            f"{s['val_acc']:.2f}%" if s['val_acc'] else "N/A",
            f"{s['effective_rank']['mean']:.2f}",
            f"{s['stable_rank']['mean']:.2f}",
            f"{s['condition_number']['mean']:.1f}",
            f"{s['spectral_gap']['mean']:.4f}",
            f"{s['spectral_decay_exponent']['mean']:.4f}",
        ))

    if comparison:
        print(f"\nMuon/AdamW stable_rank ratio: {comparison.get('muon_adamw_sr_ratio', 'N/A'):.4f}")
        if "muon_sgd_sr_ratio" in comparison:
            print(f"Muon/SGD   stable_rank ratio: {comparison['muon_sgd_sr_ratio']:.4f}")

    # Save JSON
    os.makedirs(OUT_DIR, exist_ok=True)
    json_path = os.path.join(OUT_DIR, "convnext_scs_v3_cifar100_ep20.json")
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved to {json_path}")


if __name__ == "__main__":
    main()
