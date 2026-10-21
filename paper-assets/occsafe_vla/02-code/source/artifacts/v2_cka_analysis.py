#!/usr/bin/env python3
"""v2 CKA Analysis: per-layer CKA of DINOv2/SigLIP between finetuned v2 checkpoints and pretrained OpenVLA-7B.
Runs on CPU to avoid interfering with GPU training."""

import gc, json, os, sys, time
from pathlib import Path

import numpy as np
import torch
from PIL import Image

sys.path.insert(0, "/root/occsafe_vla/openvla-oft")
from transformers import AutoModelForVision2Seq, AutoProcessor

PRETRAINED_PATH = "/root/autodl-tmp/models/openvla-7b"
CHECKPOINTS = {
    "Full_OCC_BN_v2": "/root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_bn_v2_s1--50000_chkpt",
    "Detach_BN_v2": "/root/autodl-tmp/checkpoints/detach_bn_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_bn_v2_s0--50000_chkpt",
    "Vanilla_v2": "/root/autodl-tmp/checkpoints/vanilla_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt",
}
DATA_DIR = "/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops"
OUTPUT_DIR = "/root/occsafe_vla/artifacts"
NUM_SAMPLES = 200
BATCH_SIZE = 8


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def load_images_from_rlds(data_dir, num_images=200):
    """Load agentview images from RLDS TFRecord dataset."""
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    import tensorflow as tf
    tf.config.set_visible_devices([], 'GPU')
    import tensorflow_datasets as tfds

    builder = tfds.builder_from_directory(data_dir)
    ds = builder.as_dataset(split='train')

    images = []
    for episode in ds:
        if len(images) >= num_images:
            break
        steps = list(episode['steps'])
        n_steps = len(steps)
        stride = max(1, n_steps // 4)
        for idx in range(0, n_steps, stride):
            if len(images) >= num_images:
                break
            img_np = steps[idx]['observation']['image'].numpy()
            images.append(Image.fromarray(img_np))

    log(f"  Loaded {len(images)} images from RLDS")
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


def extract_vision_features(model_path, pixel_values_batches):
    """Load model on CPU and extract per-layer vision encoder features."""
    log(f"  Loading model from {Path(model_path).name}")
    model = AutoModelForVision2Seq.from_pretrained(
        model_path, torch_dtype=torch.float32,
        low_cpu_mem_usage=True, trust_remote_code=True,
    )

    vb = model.vision_backbone
    vb.eval()

    model._modules.pop('vision_backbone', None)
    del model
    gc.collect()
    log("  Freed LLM, keeping vision backbone on CPU")

    featurizer_blocks = list(vb.featurizer.blocks)
    has_fused = hasattr(vb, "fused_featurizer")
    fused_blocks = list(vb.fused_featurizer.blocks) if has_fused else []
    log(f"  DINOv2: {len(featurizer_blocks)} blocks, SigLIP: {len(fused_blocks)} blocks")

    features = {}
    hooks = []

    def make_hook(name):
        def hook_fn(module, input, output):
            out = output[0] if isinstance(output, tuple) else output
            pooled = out.mean(dim=1).detach().float()
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
    log(f"  Forward pass: {n_total} samples, {len(pixel_values_batches)} batches")

    with torch.no_grad():
        for batch_idx, pv in enumerate(pixel_values_batches):
            pv = pv.float()
            _ = vb(pv)
            if (batch_idx + 1) % 5 == 0:
                log(f"    Batch {batch_idx + 1}/{len(pixel_values_batches)}")

    log("  Forward pass complete")
    for h in hooks:
        h.remove()

    result = {}
    for name, feat_list in features.items():
        if feat_list:
            result[name] = torch.cat(feat_list, dim=0)

    del vb
    gc.collect()
    return result


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    log("=== v2 CKA Analysis (CPU) ===")

    log("Loading images from RLDS...")
    images = load_images_from_rlds(DATA_DIR, NUM_SAMPLES)
    log(f"Got {len(images)} images")

    log("Preprocessing with AutoProcessor...")
    processor = AutoProcessor.from_pretrained(PRETRAINED_PATH, trust_remote_code=True)
    pixel_values_batches = []
    for i in range(0, len(images), BATCH_SIZE):
        batch_imgs = images[i:i + BATCH_SIZE]
        pv = processor.image_processor(batch_imgs, return_tensors="pt")["pixel_values"]
        pixel_values_batches.append(pv.cpu())
    del images, processor
    gc.collect()

    total = sum(pv.shape[0] for pv in pixel_values_batches)
    log(f"Preprocessed {total} samples, shape: {pixel_values_batches[0].shape}")

    all_features = {}

    log("=== Extracting: Pretrained ===")
    all_features["Pretrained"] = extract_vision_features(PRETRAINED_PATH, pixel_values_batches)
    first_key = next(iter(all_features["Pretrained"]))
    log(f"  {len(all_features['Pretrained'])} layers x {all_features['Pretrained'][first_key].shape[0]} samples")

    for cond_name, ckpt_path in CHECKPOINTS.items():
        log(f"=== Extracting: {cond_name} ===")
        all_features[cond_name] = extract_vision_features(ckpt_path, pixel_values_batches)
        log(f"  {len(all_features[cond_name])} layers")

    log("Computing CKA...")
    layer_names = list(all_features["Pretrained"].keys())
    dino_layers = [l for l in layer_names if l.startswith("dinov2.")]
    siglip_layers = [l for l in layer_names if l.startswith("siglip.")]

    cka_results = {}
    for cond_name in CHECKPOINTS:
        cka_results[cond_name] = {}
        for layer_name in layer_names:
            X = all_features["Pretrained"][layer_name]
            Y = all_features[cond_name][layer_name]
            cka_results[cond_name][layer_name] = round(linear_cka(X, Y), 6)

    for cond_name in CHECKPOINTS:
        print()
        print(f"=== CKA Analysis: {cond_name} vs Pretrained ===")
        print()
        print("DINOv2 per-layer CKA:")
        for l in dino_layers:
            print(f"  {l}: {cka_results[cond_name][l]:.6f}")
        dino_vals = [cka_results[cond_name][l] for l in dino_layers]
        print(f"  Mean CKA: {np.mean(dino_vals):.6f}")
        print()
        print("SigLIP per-layer CKA:")
        for l in siglip_layers:
            print(f"  {l}: {cka_results[cond_name][l]:.6f}")
        siglip_vals = [cka_results[cond_name][l] for l in siglip_layers]
        print(f"  Mean CKA: {np.mean(siglip_vals):.6f}")

    print()
    print("=" * 75)
    print("CKA Summary (higher = more similar to pretrained)")
    print("=" * 75)
    fmt = "{:20s}  {:>12s} {:>11s}  {:>12s} {:>11s}"
    print(fmt.format("Condition", "DINOv2 mean", "DINOv2 min", "SigLIP mean", "SigLIP min"))
    print("-" * 75)
    for cond_name in CHECKPOINTS:
        dino_vals = [cka_results[cond_name][l] for l in dino_layers]
        siglip_vals = [cka_results[cond_name][l] for l in siglip_layers]
        print(f"{cond_name:20s}  {np.mean(dino_vals):12.4f} {np.min(dino_vals):11.4f}  "
              f"{np.mean(siglip_vals):12.4f} {np.min(siglip_vals):11.4f}")
    print("=" * 75)

    output = {
        "metadata": {
            "pretrained_path": PRETRAINED_PATH,
            "checkpoints": CHECKPOINTS,
            "num_samples": total,
            "device": "cpu",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "cka_results": cka_results,
        "summary": {},
    }
    for cond_name in CHECKPOINTS:
        dino_vals = [cka_results[cond_name][l] for l in dino_layers]
        siglip_vals = [cka_results[cond_name][l] for l in siglip_layers]
        output["summary"][cond_name] = {
            "dinov2_mean": round(float(np.mean(dino_vals)), 6),
            "dinov2_min": round(float(np.min(dino_vals)), 6),
            "siglip_mean": round(float(np.mean(siglip_vals)), 6),
            "siglip_min": round(float(np.min(siglip_vals)), 6),
        }

    json_path = os.path.join(OUTPUT_DIR, "v2_cka_analysis.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {json_path}")
    log("DONE")


if __name__ == "__main__":
    main()
