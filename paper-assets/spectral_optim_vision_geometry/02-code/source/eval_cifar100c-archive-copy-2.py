"""CIFAR-100-C corruption robustness evaluation."""
import argparse
import csv
import os
import time

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision import transforms
import timm

CORRUPTIONS = [
    "gaussian_noise", "shot_noise", "impulse_noise",
    "defocus_blur", "glass_blur", "motion_blur", "zoom_blur",
    "snow", "frost", "fog", "brightness", "contrast",
    "elastic_transform", "pixelate", "jpeg_compression",
    "speckle_noise", "gaussian_blur", "saturate", "spatter",
]

MEAN = (0.5071, 0.4867, 0.4408)
STD = (0.2675, 0.2565, 0.2761)

MODEL_REGISTRY = {
    "convnext_tiny": "convnext_tiny",
    "resnet50": "resnet50",
    "resnet50_ln": "resnet50",
    "deit_small": "deit_small_patch16_224",
}


def replace_bn_with_gn(module, num_groups=1):
    for name, child in module.named_children():
        if isinstance(child, nn.BatchNorm2d):
            setattr(module, name, nn.GroupNorm(num_groups, child.num_features))
        else:
            replace_bn_with_gn(child, num_groups)


def build_model(model_name, use_gn=False, num_groups=1, device="cpu"):
    timm_name = MODEL_REGISTRY[model_name]
    model = timm.create_model(timm_name, pretrained=False, num_classes=100)
    if model_name == "resnet50_ln" or use_gn:
        replace_bn_with_gn(model, num_groups=num_groups)
    model = model.to(device)
    model.eval()
    return model


def load_checkpoint(ckpt_path, model_name, device):
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    sd = ckpt["state_dict"] if "state_dict" in ckpt else ckpt
    needs_gn = not any("running_mean" in k for k in sd.keys())
    num_groups = 1
    if needs_gn:
        basename = os.path.basename(ckpt_path)
        if "gn32" in basename:
            num_groups = 32
    model = build_model(model_name, use_gn=needs_gn, num_groups=num_groups, device=device)
    model.load_state_dict(sd)
    if needs_gn and model_name in ("resnet50",):
        print(f"  Auto-detected GroupNorm checkpoint (no running stats), num_groups={num_groups}")
    return model, ckpt.get("val_acc", None)


def get_transform():
    return transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.Normalize(MEAN, STD),
    ])


def preprocess_numpy_batch(images_np, transform, device):
    t = torch.from_numpy(images_np).permute(0, 3, 1, 2).float() / 255.0
    t = transform(t)
    return t.to(device)


@torch.no_grad()
def evaluate_corruption(model, images_np, labels_np, transform, device, batch_size=256):
    correct = 0
    total = len(labels_np)
    labels_t = torch.from_numpy(labels_np).long()

    for i in range(0, total, batch_size):
        batch_img = images_np[i:i + batch_size]
        batch_lbl = labels_t[i:i + batch_size].to(device)
        batch_tensor = preprocess_numpy_batch(batch_img, transform, device)
        preds = model(batch_tensor).argmax(1)
        correct += (preds == batch_lbl).sum().item()

    return 100.0 * correct / total


def main():
    parser = argparse.ArgumentParser(description="CIFAR-100-C corruption robustness evaluation")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--model", type=str, required=True, choices=list(MODEL_REGISTRY.keys()))
    parser.add_argument("--data-dir", type=str, required=True, help="Path to CIFAR-100-C directory")
    parser.add_argument("--output-csv", type=str, required=True)
    parser.add_argument("--optimizer", type=str, default="", help="Optimizer label for CSV")
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--device", type=str, default="cuda")
    parser.add_argument("--corruptions", type=str, default="all",
                        help="Comma-separated corruption names, or 'all'")
    args = parser.parse_args()

    device = torch.device(args.device)
    model, orig_acc = load_checkpoint(args.checkpoint, args.model, device)
    print(f"Loaded {args.checkpoint} (original val_acc={orig_acc})")

    transform = get_transform()
    labels = np.load(os.path.join(args.data_dir, "labels.npy"))

    corruptions = CORRUPTIONS if args.corruptions == "all" else args.corruptions.split(",")

    os.makedirs(os.path.dirname(args.output_csv), exist_ok=True)
    results = []

    for corruption in corruptions:
        npy_path = os.path.join(args.data_dir, f"{corruption}.npy")
        if not os.path.exists(npy_path):
            print(f"SKIP {corruption}: {npy_path} not found")
            continue

        images_all = np.load(npy_path)

        for severity in range(1, 6):
            start = (severity - 1) * 10000
            end = severity * 10000
            images = images_all[start:end]
            lbls = labels[start:end]

            t0 = time.time()
            acc = evaluate_corruption(model, images, lbls, transform, device, args.batch_size)
            elapsed = time.time() - t0

            results.append({
                "model": args.model,
                "optimizer": args.optimizer,
                "corruption": corruption,
                "severity": severity,
                "accuracy": f"{acc:.2f}",
                "num_correct": int(acc * len(lbls) / 100),
                "num_total": len(lbls),
            })
            print(f"  {corruption} sev={severity}: {acc:.2f}% ({elapsed:.1f}s)")

        avg = np.mean([float(r["accuracy"]) for r in results if r["corruption"] == corruption])
        print(f"  {corruption} mean: {avg:.2f}%")

    with open(args.output_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["model", "optimizer", "corruption", "severity",
                                                "accuracy", "num_correct", "num_total"])
        writer.writeheader()
        writer.writerows(results)

    overall_mean = np.mean([float(r["accuracy"]) for r in results])
    print(f"\nOverall mean corruption accuracy: {overall_mean:.2f}%")
    print(f"Results saved to {args.output_csv}")


if __name__ == "__main__":
    main()
