#!/usr/bin/env python3
"""
CKA (Centered Kernel Alignment) analysis for OccSafe-VLA.

Compares vision encoder representations across training conditions
(Vanilla, Full OCC, Detach OCC) against the pretrained OpenVLA-7B baseline.
Extracts per-block features via forward hooks and computes Linear CKA.

Usage:
    conda activate occsafe
    python cka_analysis.py \
        --pretrained_path /root/autodl-tmp/models/openvla-7b \
        --checkpoint_paths \
            /root/autodl-tmp/checkpoints/vanilla_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
            /root/autodl-tmp/checkpoints/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
            /root/autodl-tmp/checkpoints/ablation_occ_detach_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
        --condition_names "Vanilla" "Full OCC" "Detach OCC" \
        --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial \
        --output_dir /root/autodl-tmp/analysis/cka \
        --gpu 2
"""

import argparse
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

from transformers import AutoModelForVision2Seq, AutoProcessor


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretrained_path", type=str, required=True)
    parser.add_argument("--checkpoint_paths", type=str, nargs="+", required=True)
    parser.add_argument("--condition_names", type=str, nargs="+", required=True)
    parser.add_argument("--libero_data_dir", type=str, required=True)
    parser.add_argument("--num_samples", type=int, default=200)
    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_dir", type=str, required=True)
    return parser.parse_args()


def load_libero_images(data_dir, num_images=200):
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


def extract_vision_features(model_path, pixel_values_batches, device):
    log(f"  Loading model from {model_path}")
    model = AutoModelForVision2Seq.from_pretrained(
        model_path, torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True, trust_remote_code=True,
    )
    log("  Model loaded, extracting vision backbone")

    vb = model.vision_backbone
    vb = vb.to(device)
    vb.eval()
    log("  Vision backbone on GPU")

    model._modules.pop('vision_backbone', None)
    del model
    gc.collect()
    torch.cuda.empty_cache()
    log("  Freed base model")

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

    n_total = sum(pv.shape[0] for pv in pixel_values_batches)
    log(f"  Running forward pass on {n_total} samples ({len(pixel_values_batches)} batches)...")

    with torch.no_grad():
        for batch_idx, pv in enumerate(pixel_values_batches):
            pv = pv.to(device, dtype=torch.bfloat16)
            try:
                _ = vb(pv)
            except Exception as e:
                log(f"  ERROR in forward pass batch {batch_idx}: {e}")
                raise
            del pv
            if (batch_idx + 1) % 5 == 0:
                log(f"  Batch {batch_idx + 1}/{len(pixel_values_batches)} done")

    torch.cuda.synchronize(device)
    log("  Forward pass complete")

    for h in hooks:
        h.remove()

    result = {}
    for name, feat_list in features.items():
        if feat_list:
            result[name] = torch.cat(feat_list, dim=0)

    del vb
    torch.cuda.empty_cache()
    gc.collect()
    log(f"  Cleaned up, GPU cache cleared")

    return result


def main():
    args = parse_args()
    assert len(args.checkpoint_paths) == len(args.condition_names)

    device = torch.device(f"cuda:{args.gpu}")
    os.makedirs(args.output_dir, exist_ok=True)

    log(f"Using GPU {args.gpu}")
    log(f"Loading {args.num_samples} images from {args.libero_data_dir}")
    images = load_libero_images(args.libero_data_dir, args.num_samples)
    log(f"Loaded {len(images)} images")

    processor = AutoProcessor.from_pretrained(args.pretrained_path, trust_remote_code=True)
    pixel_values_batches = []
    for i in range(0, len(images), args.batch_size):
        batch_imgs = images[i:i + args.batch_size]
        pv = processor.image_processor(batch_imgs, return_tensors="pt")["pixel_values"]
        pixel_values_batches.append(pv.cpu())
    del images, processor
    gc.collect()

    total_samples = sum(pv.shape[0] for pv in pixel_values_batches)
    log(f"Preprocessed {total_samples} samples, shape: {pixel_values_batches[0].shape}")

    all_model_paths = [args.pretrained_path] + args.checkpoint_paths
    all_model_names = ["Pretrained"] + args.condition_names
    all_features = {}

    for model_path, model_name in zip(all_model_paths, all_model_names):
        log(f"=== Extracting: {model_name} ===")
        try:
            all_features[model_name] = extract_vision_features(
                model_path, pixel_values_batches, device
            )
            n_layers = len(all_features[model_name])
            first_key = next(iter(all_features[model_name]))
            n_samples = all_features[model_name][first_key].shape[0]
            log(f"  Result: {n_layers} layers x {n_samples} samples")
        except Exception as e:
            log(f"  FAILED: {e}")
            import traceback
            traceback.print_exc(file=sys.stdout)
            sys.stdout.flush()
            raise

    log("Computing CKA...")
    layer_names = list(all_features["Pretrained"].keys())

    cka_results = {}
    for cond_name in args.condition_names:
        cka_results[cond_name] = {}
        for layer_name in layer_names:
            X = all_features["Pretrained"][layer_name]
            Y = all_features[cond_name][layer_name]
            cka_results[cond_name][layer_name] = round(linear_cka(X, Y), 6)

    results_path = os.path.join(args.output_dir, "cka_results.json")
    with open(results_path, "w") as f:
        json.dump(cka_results, f, indent=2)
    log(f"Saved: {results_path}")

    log("Generating plots...")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    dino_layers = [l for l in layer_names if l.startswith("dinov2.")]
    siglip_layers = [l for l in layer_names if l.startswith("siglip.")]

    colors = {"Vanilla": "#2196F3", "Full OCC": "#4CAF50", "Detach OCC": "#F44336"}

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    for cond_name in args.condition_names:
        color = colors.get(cond_name, None)
        xs = list(range(len(dino_layers)))
        ys = [cka_results[cond_name][l] for l in dino_layers]
        axes[0].plot(xs, ys, "o-", label=cond_name, color=color, markersize=4, linewidth=1.5, alpha=0.85)
        xs = list(range(len(siglip_layers)))
        ys = [cka_results[cond_name][l] for l in siglip_layers]
        axes[1].plot(xs, ys, "o-", label=cond_name, color=color, markersize=4, linewidth=1.5, alpha=0.85)

    for ax, title, n_blocks in zip(axes, ["DINOv2 ViT-L", "SigLIP ViT-SO400M"],
                                    [len(dino_layers), len(siglip_layers)]):
        ax.set_xlabel("Block Index")
        ax.set_ylabel("CKA Similarity to Pretrained")
        ax.set_title(title)
        ax.legend(loc="lower left")
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.05)
        ax.set_xlim(-0.5, n_blocks - 0.5)

    fig.suptitle("CKA: Vision Encoder Similarity to Pretrained OpenVLA-7B (50K steps)",
                 fontsize=12, fontweight="bold")
    plt.tight_layout()
    for ext in ("pdf", "png"):
        path = os.path.join(args.output_dir, f"cka_analysis.{ext}")
        fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    log("Saved: cka_analysis.pdf, cka_analysis.png")

    log("")
    log("=" * 65)
    log("CKA Summary (higher = more similar to pretrained)")
    log("=" * 65)
    fmt = "{:15s}  {:>12s} {:>11s}  {:>12s} {:>11s}"
    log(fmt.format("Condition", "DINOv2 mean", "DINOv2 min", "SigLIP mean", "SigLIP min"))
    log("-" * 65)
    for cond_name in args.condition_names:
        dino_vals = [cka_results[cond_name][l] for l in dino_layers]
        siglip_vals = [cka_results[cond_name][l] for l in siglip_layers]
        log(f"{cond_name:15s}  {np.mean(dino_vals):12.4f} {np.min(dino_vals):11.4f}  "
              f"{np.mean(siglip_vals):12.4f} {np.min(siglip_vals):11.4f}")
    log("=" * 65)
    log("DONE")


if __name__ == "__main__":
    main()
