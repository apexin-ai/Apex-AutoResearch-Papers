#!/usr/bin/env python3
"""
CKA dose-response analysis: per-layer CKA vs pretrained for different cutoff timings.
Compares DINOv2 (24 blocks) and SigLIP (27 blocks) encoder representations.

Loads pretrained base + applies LoRA adapter via PEFT for each condition,
because merged checkpoint shards contain condition-specific weights.

Usage:
    CUDA_VISIBLE_DEVICES=0 python cka_dose_response.py
"""

import gc
import json
import os
import sys
import time
from pathlib import Path

import h5py
import numpy as np
import torch
from PIL import Image

sys.path.insert(0, "/root/occsafe_vla/openvla-oft")
from peft import PeftModel
from transformers import AutoModelForVision2Seq, AutoProcessor


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# === Configuration ===
PRETRAINED_PATH = "/root/autodl-tmp/models/openvla-7b"
LIBERO_DATA_DIR = "/root/autodl-tmp/libero_datasets/libero_spatial"
OUTPUT_DIR = "/root/autodl-tmp/analysis/cka_dose_response"
NUM_SAMPLES = 100
BATCH_SIZE = 8
GPU = 0

CKPT_BASE = "/root/autodl-tmp/checkpoints"

# Map condition name -> lora_adapter directory path
CONDITIONS = {
    "Vanilla": f"{CKPT_BASE}/vanilla_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/lora_adapter",
    "Full OCC": f"{CKPT_BASE}/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/lora_adapter",
    "Cutoff 15K": f"{CKPT_BASE}/cutoff_15k_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_15k_s1--50000_chkpt/lora_adapter",
    # Add when LoRA adapters are available:
    # "Cutoff 25K": f"{CKPT_BASE}/cutoff_25k_.../lora_adapter",
    # "Cutoff 45K": f"{CKPT_BASE}/cutoff_45k_.../lora_adapter",
    # "Reverse Cutoff": f"{CKPT_BASE}/reverse_cutoff_.../lora_adapter",
}

COLORS = {
    "Vanilla": "#607D8B",
    "Full OCC": "#4CAF50",
    "Cutoff 15K": "#2196F3",
    "Cutoff 25K": "#03A9F4",
    "Cutoff 35K": "#FF9800",
    "Cutoff 45K": "#F44336",
    "Reverse Cutoff": "#9C27B0",
}


def load_libero_images(data_dir, num_images):
    images = []
    hdf5_files = sorted(Path(data_dir).glob("*.hdf5"))
    if not hdf5_files:
        raise FileNotFoundError(f"No HDF5 files in {data_dir}")
    for hdf5_file in hdf5_files:
        if len(images) >= num_images:
            break
        with h5py.File(hdf5_file, "r") as f:
            for demo_key in sorted(f["data"].keys()):
                if len(images) >= num_images:
                    break
                rgb = f["data"][demo_key]["obs"]["agentview_rgb"]
                n_frames = rgb.shape[0]
                step = max(1, n_frames // 4)
                for idx in range(0, n_frames, step):
                    images.append(Image.fromarray(rgb[idx]))
                    if len(images) >= num_images:
                        break
    return images[:num_images]


def linear_cka(X, Y):
    X = X.double()
    Y = Y.double()
    X = X - X.mean(dim=0, keepdim=True)
    Y = Y - Y.mean(dim=0, keepdim=True)
    YtX = Y.T @ X
    XtX = X.T @ X
    YtY = Y.T @ Y
    numerator = (YtX ** 2).sum()
    denominator = torch.sqrt((XtX ** 2).sum() * (YtY ** 2).sum())
    if denominator < 1e-12:
        return 0.0
    return (numerator / denominator).item()


def extract_vision_features_pretrained(pretrained_path, pixel_values_batches, device):
    """Extract from the pretrained model directly (no LoRA)."""
    log(f"  Loading pretrained from {pretrained_path}")
    model = AutoModelForVision2Seq.from_pretrained(
        pretrained_path, torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True, trust_remote_code=True,
    )
    return _extract_from_model(model, pixel_values_batches, device)


def extract_vision_features_lora(pretrained_path, lora_adapter_path, pixel_values_batches, device):
    """Load pretrained base + apply LoRA adapter, then extract vision features."""
    log(f"  Loading pretrained base + LoRA from {Path(lora_adapter_path).parent.parent.name}/.../{Path(lora_adapter_path).name}")
    base_model = AutoModelForVision2Seq.from_pretrained(
        pretrained_path, torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True, trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(base_model, lora_adapter_path)
    model = model.merge_and_unload()
    return _extract_from_model(model, pixel_values_batches, device)


def _extract_from_model(model, pixel_values_batches, device):
    """Extract per-block vision features from a loaded model."""
    vb = model.vision_backbone
    vb = vb.to(device)
    vb.eval()

    model._modules.pop('vision_backbone', None)
    del model
    gc.collect()
    torch.cuda.empty_cache()

    featurizer_blocks = list(vb.featurizer.blocks)
    has_fused = hasattr(vb, "fused_featurizer")
    fused_blocks = list(vb.fused_featurizer.blocks) if has_fused else []
    log(f"  DINOv2: {len(featurizer_blocks)} blocks, SigLIP: {len(fused_blocks)} blocks")

    features = {}
    hooks = []

    def make_hook(name):
        def hook_fn(module, input, output):
            out = output[0] if isinstance(output, tuple) else output
            pooled = out.mean(dim=1).detach().cpu().float()
            features[name].append(pooled)
        return hook_fn

    for i, block in enumerate(featurizer_blocks):
        name = f"dinov2.block.{i}"
        features[name] = []
        hooks.append(block.register_forward_hook(make_hook(name)))

    for i, block in enumerate(fused_blocks):
        name = f"siglip.block.{i}"
        features[name] = []
        hooks.append(block.register_forward_hook(make_hook(name)))

    with torch.no_grad():
        for batch_idx, pv in enumerate(pixel_values_batches):
            pv = pv.to(device, dtype=torch.bfloat16)
            _ = vb(pv)
            del pv
            if (batch_idx + 1) % 5 == 0:
                log(f"  Batch {batch_idx + 1}/{len(pixel_values_batches)} done")

    torch.cuda.synchronize(device)

    for h in hooks:
        h.remove()

    result = {}
    for name, feat_list in features.items():
        if feat_list:
            result[name] = torch.cat(feat_list, dim=0)

    del vb
    torch.cuda.empty_cache()
    gc.collect()

    return result


def main():
    device = torch.device(f"cuda:{GPU}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    valid_conditions = {}
    for name, path in CONDITIONS.items():
        if os.path.isdir(path):
            valid_conditions[name] = path
        else:
            log(f"WARNING: {name} lora_adapter not found: {path}")

    log(f"Conditions: {list(valid_conditions.keys())} ({len(valid_conditions)}/{len(CONDITIONS)})")

    log(f"Loading {NUM_SAMPLES} images from {LIBERO_DATA_DIR}")
    images = load_libero_images(LIBERO_DATA_DIR, NUM_SAMPLES)
    log(f"Loaded {len(images)} images")

    processor = AutoProcessor.from_pretrained(PRETRAINED_PATH, trust_remote_code=True)
    pixel_values_batches = []
    for i in range(0, len(images), BATCH_SIZE):
        batch_imgs = images[i:i + BATCH_SIZE]
        pv = processor.image_processor(batch_imgs, return_tensors="pt")["pixel_values"]
        pixel_values_batches.append(pv.cpu())
    del images, processor
    gc.collect()

    total_samples = sum(pv.shape[0] for pv in pixel_values_batches)
    log(f"Preprocessed {total_samples} samples, shape: {pixel_values_batches[0].shape}")

    log("=== Extracting: Pretrained ===")
    pretrained_features = extract_vision_features_pretrained(PRETRAINED_PATH, pixel_values_batches, device)
    log(f"  {len(pretrained_features)} layers x {pretrained_features[next(iter(pretrained_features))].shape[0]} samples")

    condition_features = {}
    for cond_name, lora_path in valid_conditions.items():
        log(f"=== Extracting: {cond_name} (via LoRA) ===")
        condition_features[cond_name] = extract_vision_features_lora(
            PRETRAINED_PATH, lora_path, pixel_values_batches, device
        )

    log("Computing CKA...")
    layer_names = list(pretrained_features.keys())
    cka_results = {}
    for cond_name in valid_conditions:
        cka_results[cond_name] = {}
        for layer_name in layer_names:
            X = pretrained_features[layer_name]
            Y = condition_features[cond_name][layer_name]
            cka_results[cond_name][layer_name] = round(linear_cka(X, Y), 6)

    dino_layers = [l for l in layer_names if l.startswith("dinov2.")]
    siglip_layers = [l for l in layer_names if l.startswith("siglip.")]

    summary = {}
    for cond_name in valid_conditions:
        dino_vals = [cka_results[cond_name][l] for l in dino_layers]
        siglip_vals = [cka_results[cond_name][l] for l in siglip_layers]
        summary[cond_name] = {
            "dinov2_mean": round(float(np.mean(dino_vals)), 4),
            "dinov2_min": round(float(np.min(dino_vals)), 4),
            "dinov2_std": round(float(np.std(dino_vals)), 4),
            "siglip_mean": round(float(np.mean(siglip_vals)), 4),
            "siglip_min": round(float(np.min(siglip_vals)), 4),
            "siglip_std": round(float(np.std(siglip_vals)), 4),
        }

    results_path = os.path.join(OUTPUT_DIR, "cka_dose_response_results.json")
    with open(results_path, "w") as f:
        json.dump({"per_layer": cka_results, "summary": summary}, f, indent=2)
    log(f"Saved: {results_path}")

    log("Generating plots...")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for cond_name in valid_conditions:
        color = COLORS.get(cond_name, None)
        xs = list(range(len(dino_layers)))
        ys = [cka_results[cond_name][l] for l in dino_layers]
        axes[0].plot(xs, ys, "o-", label=cond_name, color=color, markersize=3, linewidth=1.5, alpha=0.85)

        xs = list(range(len(siglip_layers)))
        ys = [cka_results[cond_name][l] for l in siglip_layers]
        axes[1].plot(xs, ys, "o-", label=cond_name, color=color, markersize=3, linewidth=1.5, alpha=0.85)

    for ax, title, n_blocks in zip(axes, ["DINOv2 ViT-L (24 blocks)", "SigLIP ViT-SO400M (27 blocks)"],
                                    [len(dino_layers), len(siglip_layers)]):
        ax.set_xlabel("Block Index")
        ax.set_ylabel("CKA Similarity to Pretrained")
        ax.set_title(title)
        ax.legend(loc="lower left", fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.05)
        ax.set_xlim(-0.5, n_blocks - 0.5)

    fig.suptitle("Per-layer CKA vs Pretrained — Dose-Response Conditions (50K steps)",
                 fontsize=12, fontweight="bold")
    plt.tight_layout()

    for ext in ("pdf", "png"):
        path = os.path.join(OUTPUT_DIR, f"cka_dose_response.{ext}")
        fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    log("Saved: cka_dose_response.pdf, cka_dose_response.png")

    log("")
    log("=" * 70)
    log("CKA Summary (higher = more similar to pretrained)")
    log("=" * 70)
    fmt = "{:18s}  {:>10s} {:>10s} {:>8s}  {:>10s} {:>10s} {:>8s}"
    log(fmt.format("Condition", "DINO mean", "DINO min", "DINO std", "SigLIP mean", "SigLIP min", "SIG std"))
    log("-" * 70)
    for cond_name in valid_conditions:
        s = summary[cond_name]
        log(f"{cond_name:18s}  {s['dinov2_mean']:10.4f} {s['dinov2_min']:10.4f} {s['dinov2_std']:8.4f}  "
            f"{s['siglip_mean']:10.4f} {s['siglip_min']:10.4f} {s['siglip_std']:8.4f}")
    log("=" * 70)
    log("DONE")


if __name__ == "__main__":
    main()
