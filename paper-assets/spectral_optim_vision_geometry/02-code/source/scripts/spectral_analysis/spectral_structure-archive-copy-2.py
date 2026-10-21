#!/usr/bin/env python3
"""Spectral structure analysis of trained weight matrices.

Compares spectral properties (singular value distribution, effective rank,
condition number, etc.) between ResNet-50 and DeiT-S trained with Muon vs AdamW.
Outputs per-layer CSV for downstream analysis.
"""
import argparse
import csv
import os
from collections import OrderedDict

import numpy as np
import torch
import timm
from scipy.optimize import curve_fit


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

CKPT_DIR = "/root/autodl-tmp/checkpoints/spectral_optim"

MODELS = OrderedDict([
    ("resnet50_muon", {
        "ckpt": os.path.join(CKPT_DIR, "resnet50_muon_s42.pt"),
        "timm_name": "resnet50",
        "arch": "cnn",
    }),
    ("resnet50_adamw", {
        "ckpt": os.path.join(CKPT_DIR, "resnet50_adamw.pt"),
        "timm_name": "resnet50",
        "arch": "cnn",
    }),
    ("deit_small_muon", {
        "ckpt": os.path.join(CKPT_DIR, "deit_small_muon_lr0003_s42_ep20.pt"),
        "timm_name": "deit_small_patch16_224",
        "arch": "vit",
    }),
    ("deit_small_adamw", {
        "ckpt": os.path.join(CKPT_DIR, "deit_small_adamw_s42.pt"),
        "timm_name": "deit_small_patch16_224",
        "arch": "vit",
    }),
])

OUTPUT_DIR = "/root/spectral_optim_vision_geometry/results/spectral_analysis"


# ---------------------------------------------------------------------------
# Spectral metrics
# ---------------------------------------------------------------------------

def compute_spectral_metrics(weight: torch.Tensor):
    """Compute spectral features for a 2D weight matrix.

    Returns dict with: condition_number, effective_rank, stable_rank,
    spectral_gap, spectral_decay_exponent, singular_values (normalized).
    """
    with torch.no_grad():
        S = torch.linalg.svdvals(weight.float())

    S_np = S.cpu().numpy()
    sigma_1 = S_np[0]

    if sigma_1 == 0:
        return None

    # Normalized singular values
    S_norm = S_np / sigma_1

    # Condition number
    sigma_min = S_np[-1]
    condition_number = sigma_1 / max(sigma_min, 1e-10)

    # Effective rank: nuclear norm / operator norm = sum(sigma_i) / sigma_1
    effective_rank = S_np.sum() / sigma_1

    # Stable rank: ||W||_F^2 / ||W||_op^2 = sum(sigma_i^2) / sigma_1^2
    stable_rank = (S_np ** 2).sum() / (sigma_1 ** 2)

    # Spectral gap: (sigma_1 - sigma_2) / sigma_1
    spectral_gap = (S_np[0] - S_np[1]) / sigma_1 if len(S_np) > 1 else 1.0

    # Spectral decay exponent: fit power law sigma_i/sigma_1 ~ i^(-alpha)
    decay_exponent = _fit_power_law_decay(S_norm)

    return {
        "condition_number": float(condition_number),
        "effective_rank": float(effective_rank),
        "stable_rank": float(stable_rank),
        "spectral_gap": float(spectral_gap),
        "spectral_decay_exponent": float(decay_exponent),
        "singular_values_normalized": S_norm.tolist(),
    }


def _fit_power_law_decay(S_norm: np.ndarray) -> float:
    """Fit power law: S_norm[i] ~ (i+1)^(-alpha). Returns alpha."""
    n = len(S_norm)
    if n < 3:
        return 0.0

    # Use log-log linear regression (robust, no convergence issues)
    indices = np.arange(1, n + 1, dtype=np.float64)
    # Filter out zeros to avoid log(0)
    mask = S_norm > 1e-10
    if mask.sum() < 3:
        return 0.0

    log_i = np.log(indices[mask])
    log_s = np.log(S_norm[mask])

    # Linear fit: log(s) = -alpha * log(i) + c
    coeffs = np.polyfit(log_i, log_s, 1)
    alpha = -coeffs[0]
    return alpha


# ---------------------------------------------------------------------------
# Weight extraction
# ---------------------------------------------------------------------------

def get_layer_type(name: str, weight: torch.Tensor, arch: str) -> str:
    """Classify layer as conv or linear."""
    if weight.ndim == 4:
        return "conv"
    elif weight.ndim == 2:
        return "linear"
    return "other"


def reshape_for_svd(weight: torch.Tensor, layer_type: str) -> torch.Tensor:
    """Reshape weight to 2D for SVD computation."""
    if layer_type == "conv":
        # (C_out, C_in, H, W) -> (C_out, C_in*H*W)
        return weight.reshape(weight.shape[0], -1)
    elif layer_type == "linear":
        return weight
    return None


def should_analyze(name: str, weight: torch.Tensor) -> bool:
    """Filter: only analyze conv/linear weight matrices with ndim >= 2."""
    if not name.endswith(".weight"):
        return False
    if weight.ndim < 2:
        return False
    # Skip batch norm, layer norm, embedding weights that are 1D
    if weight.ndim == 2 and min(weight.shape) < 2:
        return False
    return True


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def analyze_model(model_name: str, config: dict) -> list:
    """Load checkpoint, compute spectral metrics for all eligible layers."""
    print(f"Analyzing {model_name}...")

    # Create model architecture
    model = timm.create_model(config["timm_name"], pretrained=False, num_classes=100)

    # Load checkpoint
    ckpt = torch.load(config["ckpt"], map_location="cpu", weights_only=False)
    state_dict = ckpt["state_dict"] if "state_dict" in ckpt else ckpt
    model.load_state_dict(state_dict)
    model.eval()

    results = []
    for name, param in model.named_parameters():
        if not should_analyze(name, param.data):
            continue

        weight = param.data
        layer_type = get_layer_type(name, weight, config["arch"])
        if layer_type == "other":
            continue

        W_2d = reshape_for_svd(weight, layer_type)
        if W_2d is None or min(W_2d.shape) < 2:
            continue

        metrics = compute_spectral_metrics(W_2d)
        if metrics is None:
            continue

        results.append({
            "model_name": model_name,
            "layer_name": name,
            "layer_type": layer_type,
            "shape": str(list(weight.shape)),
            "matrix_shape": str(list(W_2d.shape)),
            "param_count": int(weight.numel()),
            "condition_number": metrics["condition_number"],
            "effective_rank": metrics["effective_rank"],
            "stable_rank": metrics["stable_rank"],
            "spectral_gap": metrics["spectral_gap"],
            "spectral_decay_exponent": metrics["spectral_decay_exponent"],
        })

    print(f"  -> {len(results)} layers analyzed")
    return results


def save_results(all_results: list, output_path: str):
    """Save results to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fieldnames = [
        "model_name", "layer_name", "layer_type", "shape", "matrix_shape",
        "param_count", "condition_number", "effective_rank", "stable_rank",
        "spectral_gap", "spectral_decay_exponent",
    ]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)
    print(f"Saved {len(all_results)} rows to {output_path}")


def save_singular_values(model_name: str, layer_name: str, sv: list, output_dir: str):
    """Save raw normalized singular values for detailed distribution analysis."""
    sv_dir = os.path.join(output_dir, "singular_values")
    os.makedirs(sv_dir, exist_ok=True)
    safe_layer = layer_name.replace(".", "_")
    path = os.path.join(sv_dir, f"{model_name}__{safe_layer}.npy")
    np.save(path, np.array(sv, dtype=np.float32))


def main():
    parser = argparse.ArgumentParser(description="Spectral structure analysis")
    parser.add_argument("--output-dir", type=str, default=OUTPUT_DIR)
    parser.add_argument("--save-sv", action="store_true",
                        help="Save full singular value arrays as .npy files")
    parser.add_argument("--models", nargs="+", default=None,
                        help="Subset of models to analyze (default: all)")
    parser.add_argument("--device", type=str, default="cpu",
                        help="Device for SVD computation (cpu recommended)")
    args = parser.parse_args()

    models_to_run = MODELS
    if args.models:
        models_to_run = {k: v for k, v in MODELS.items() if k in args.models}

    all_results = []
    for model_name, config in models_to_run.items():
        if not os.path.exists(config["ckpt"]):
            print(f"WARNING: checkpoint not found: {config['ckpt']}, skipping {model_name}")
            continue

        results = analyze_model(model_name, config)
        all_results.extend(results)

        if args.save_sv:
            # Re-run to get SVs (or cache in analyze_model if memory allows)
            model = timm.create_model(config["timm_name"], pretrained=False, num_classes=100)
            ckpt = torch.load(config["ckpt"], map_location="cpu", weights_only=False)
            state_dict = ckpt["state_dict"] if "state_dict" in ckpt else ckpt
            model.load_state_dict(state_dict)
            for name, param in model.named_parameters():
                if not should_analyze(name, param.data):
                    continue
                weight = param.data
                layer_type = get_layer_type(name, weight, config["arch"])
                if layer_type == "other":
                    continue
                W_2d = reshape_for_svd(weight, layer_type)
                if W_2d is None or min(W_2d.shape) < 2:
                    continue
                metrics = compute_spectral_metrics(W_2d)
                if metrics:
                    save_singular_values(model_name, name, metrics["singular_values_normalized"], args.output_dir)

    output_path = os.path.join(args.output_dir, "spectral_metrics.csv")
    save_results(all_results, output_path)


if __name__ == "__main__":
    main()
