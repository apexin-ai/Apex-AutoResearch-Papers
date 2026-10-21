#!/usr/bin/env python3
"""SCS v3: Spectral analysis for ConvNeXt-T checkpoints (Muon/AdamW/SGD, T_max=20 terminal states)."""
import argparse
import json
import os
import sys

sys.path.insert(0, "/root/spectral_optim_vision_geometry")

import numpy as np
import torch
import timm
from scripts.spectral_analysis.spectral_structure import (
    compute_spectral_metrics, get_layer_type, reshape_for_svd, should_analyze
)

SCSV3_DIR = "/root/spectral_optim_vision_geometry/checkpoints/scs_v3"

CHECKPOINTS = {
    "muon": os.path.join(SCSV3_DIR, "convnext_t_muon_lr002_s42_tmax20_ep20.pt"),
    "adamw": os.path.join(SCSV3_DIR, "convnext_t_adamw_lr1e-3_s42_tmax20_ep20.pt"),
    "sgd": os.path.join(SCSV3_DIR, "convnext_t_sgd_lr0.01_s42_ep20.pt"),
}


def analyze_checkpoint(ckpt_path: str) -> dict:
    """Load checkpoint and compute aggregate spectral metrics."""
    model = timm.create_model("convnext_tiny", pretrained=False, num_classes=100)
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    state_dict = ckpt["state_dict"] if "state_dict" in ckpt else ckpt
    model.load_state_dict(state_dict)
    model.eval()

    val_acc = ckpt.get("val_acc", None)

    all_sr, all_er, all_cn, all_sg, all_alpha = [], [], [], [], []
    n_layers = 0

    for name, param in model.named_parameters():
        if not should_analyze(name, param.data):
            continue
        weight = param.data
        layer_type = get_layer_type(name, weight, "cnn")
        if layer_type == "other":
            continue
        W_2d = reshape_for_svd(weight, layer_type)
        if W_2d is None or min(W_2d.shape) < 2:
            continue
        metrics = compute_spectral_metrics(W_2d)
        if metrics is None:
            continue
        all_sr.append(metrics["stable_rank"])
        all_er.append(metrics["effective_rank"])
        all_cn.append(metrics["condition_number"])
        all_sg.append(metrics["spectral_gap"])
        all_alpha.append(metrics["spectral_decay_exponent"])
        n_layers += 1

    return {
        "stable_rank": float(np.mean(all_sr)),
        "effective_rank": float(np.mean(all_er)),
        "condition_number": float(np.mean(all_cn)),
        "spectral_gap": float(np.mean(all_sg)),
        "decay_alpha": float(np.mean(all_alpha)),
        "val_acc": float(val_acc) if val_acc is not None else None,
        "n_layers": n_layers,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--muon-ckpt", default=CHECKPOINTS["muon"])
    parser.add_argument("--adamw-ckpt", default=CHECKPOINTS["adamw"])
    parser.add_argument("--sgd-ckpt", default=CHECKPOINTS["sgd"])
    args = parser.parse_args()

    results = {}
    for opt_name, path in [("muon", args.muon_ckpt), ("adamw", args.adamw_ckpt), ("sgd", args.sgd_ckpt)]:
        if not os.path.exists(path):
            print(f"WARNING: {path} not found, skipping {opt_name}")
            continue
        print(f"Analyzing {opt_name}: {path}")
        results[opt_name] = analyze_checkpoint(path)
        r = results[opt_name]
        print(f"  SR={r['stable_rank']:.2f}, ER={r['effective_rank']:.2f}, "
              f"CN={r['condition_number']:.1f}, SG={r['spectral_gap']:.4f}, "
              f"alpha={r['decay_alpha']:.4f}, val_acc={r['val_acc']:.2f}%, layers={r['n_layers']}")

    if "muon" in results and "adamw" in results:
        ratio = results["muon"]["stable_rank"] / results["adamw"]["stable_rank"]
        print(f"\nmuon_adamw_sr_ratio = {ratio:.2f}")
        results["muon_adamw_sr_ratio"] = ratio

    output_path = os.path.join(SCSV3_DIR, "scs_v3_spectral_results.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
