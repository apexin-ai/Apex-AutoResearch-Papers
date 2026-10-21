"""Per-layer gradient norm analysis for ConvNeXt-T and DeiT-S (D215 P1).

Extends R50-BN/LN gradient norm ratio analysis to native-LN architectures:
  - ConvNeXt-T (CNN with LayerNorm)
  - DeiT-S (ViT with LayerNorm)

Computes per-layer mean gradient norms, cross-optimizer ratios (vs AdamW),
cross-layer CV, and depth-group aggregation.
"""

import json
import os
import random
from collections import defaultdict, OrderedDict
from datetime import datetime

import numpy as np
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import timm

CKPT_DIR = "/root/autodl-tmp/checkpoints/spectral_optim"
DATA_ROOT = "/root/spectral_optim_vision_geometry/data"
OUTPUT_DIR = "/root/spectral_optim_vision_geometry"
DEVICE = "cuda:0"
N_BATCHES = 5
BATCH_SIZE = 64
SEED = 42

CIFAR100_MEAN = (0.5071, 0.4867, 0.4408)
CIFAR100_STD  = (0.2675, 0.2565, 0.2761)

ARCHITECTURES = OrderedDict([
    ("ConvNeXt-T", {
        "timm_name": "convnext_tiny",
        "checkpoints": OrderedDict([
            ("muon",    "convnext_tiny_muon_s42_best.pt"),
            ("adamw",   "convnext_tiny_adamw_s42_lr1e-3_best.pt"),
            ("soap",    "convnext_tiny_soap_s42_lr1e-2_best.pt"),
            ("shampoo", "convnext_tiny_shampoo_s42_lr7e-3_best.pt"),
        ]),
    }),
    ("DeiT-S", {
        "timm_name": "deit_small_patch16_224",
        "checkpoints": OrderedDict([
            ("muon",    "deit_small_muon_s42_best.pt"),
            ("adamw",   "deit_small_adamw_s42_lr5e-4_best.pt"),
            ("soap",    "deit_small_soap_s42_lr1e-2_best.pt"),
            ("shampoo", "deit_small_shampoo_s42_lr5e-3_best.pt"),
        ]),
    }),
])

CONVNEXT_DEPTH_ORDER = ["Stem", "Stage 0", "Stage 1", "Stage 2", "Stage 3", "Head"]
DEIT_DEPTH_ORDER = ["Stem", "Early (0-3)", "Mid (4-7)", "Late (8-11)", "Head"]


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def get_depth_group_convnext(name):
    if name.startswith("stem"):
        return "Stem"
    for i in range(4):
        if name.startswith(f"stages.{i}"):
            return f"Stage {i}"
    if "head" in name or "norm_pre" in name:
        return "Head"
    return "Other"


def get_depth_group_deit(name):
    if name.startswith("blocks."):
        idx = int(name.split(".")[1])
        if idx <= 3:
            return "Early (0-3)"
        elif idx <= 7:
            return "Mid (4-7)"
        else:
            return "Late (8-11)"
    if "patch_embed" in name:
        return "Stem"
    if name.startswith("head") or name == "head":
        return "Head"
    return "Other"


def get_depth_fn(arch_name):
    if "ConvNeXt" in arch_name:
        return get_depth_group_convnext
    return get_depth_group_deit


def get_depth_order(arch_name):
    if "ConvNeXt" in arch_name:
        return CONVNEXT_DEPTH_ORDER
    return DEIT_DEPTH_ORDER


def load_checkpoint(ckpt_path, timm_name, device):
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)

    if isinstance(ckpt, dict):
        for key in ["model_state_dict", "state_dict", "model"]:
            if key in ckpt:
                sd = ckpt[key]
                break
        else:
            sd = ckpt
        val_acc = ckpt.get("val_acc", ckpt.get("best_val_acc", None))
        epoch = ckpt.get("epoch", None)
    else:
        sd = ckpt
        val_acc = None
        epoch = None

    model = timm.create_model(timm_name, pretrained=False, num_classes=100)

    if any(k.startswith("module.") for k in sd.keys()):
        sd = {k.replace("module.", ""): v for k, v in sd.items()}

    result = model.load_state_dict(sd, strict=False)
    if result.missing_keys:
        print(f"  WARNING: {len(result.missing_keys)} missing keys: {result.missing_keys[:5]}")
    if result.unexpected_keys:
        print(f"  WARNING: {len(result.unexpected_keys)} unexpected keys: {result.unexpected_keys[:5]}")

    model = model.to(device)
    model.eval()
    return model, val_acc, epoch


def get_val_loader(batch_size):
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
    ])
    ds = torchvision.datasets.CIFAR100(
        root=DATA_ROOT, train=False, download=True, transform=transform)
    return torch.utils.data.DataLoader(
        ds, batch_size=batch_size, shuffle=True,
        num_workers=4, pin_memory=True, drop_last=True)


def collect_weight_layers(model):
    layers = {}
    for name, mod in model.named_modules():
        if isinstance(mod, (nn.Conv2d, nn.Linear)):
            layers[name] = mod
    return layers


def compute_gradient_norms(model, loader, device, n_batches):
    criterion = nn.CrossEntropyLoss()
    layers = collect_weight_layers(model)
    all_norms = defaultdict(list)

    batch_iter = iter(loader)
    for _ in range(n_batches):
        try:
            images, labels = next(batch_iter)
        except StopIteration:
            batch_iter = iter(loader)
            images, labels = next(batch_iter)

        images, labels = images.to(device), labels.to(device)
        model.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()

        for name, mod in layers.items():
            if mod.weight.grad is not None:
                gnorm = mod.weight.grad.detach().float().norm().item()
                all_norms[name].append(gnorm)

        del images, labels, outputs, loss
        torch.cuda.empty_cache()

    result = {}
    for name in sorted(all_norms.keys()):
        norms = all_norms[name]
        result[name] = {
            "mean": float(np.mean(norms)),
            "std": float(np.std(norms)),
            "n_params": layers[name].weight.numel(),
        }

    return result


def analyze_architecture(arch_name, arch_cfg, loader, device):
    depth_fn = get_depth_fn(arch_name)
    depth_order = get_depth_order(arch_name)
    timm_name = arch_cfg["timm_name"]

    print(f"\n{'=' * 70}")
    print(f"=== Architecture: {arch_name} ===")
    print(f"{'=' * 70}")

    opt_results = {}
    for opt_name, ckpt_file in arch_cfg["checkpoints"].items():
        ckpt_path = os.path.join(CKPT_DIR, ckpt_file)
        mtime = datetime.fromtimestamp(os.path.getmtime(ckpt_path)).strftime("%Y-%m-%d %H:%M")

        print(f"\nCheckpoint: {ckpt_file} (best checkpoint, modified: {mtime})")

        model, val_acc, epoch = load_checkpoint(ckpt_path, timm_name, device)
        info_parts = []
        if val_acc is not None:
            info_parts.append(f"val_acc={val_acc:.2f}")
        if epoch is not None:
            info_parts.append(f"epoch={epoch}")
        if info_parts:
            print(f"  {', '.join(info_parts)}")

        set_seed(SEED)
        norms = compute_gradient_norms(model, loader, device, N_BATCHES)

        layer_means = [v["mean"] for v in norms.values()]
        overall = float(np.mean(layer_means))
        cv = float(np.std(layer_means) / (np.mean(layer_means) + 1e-12))

        depth_norms = defaultdict(list)
        for layer_name, v in norms.items():
            depth = depth_fn(layer_name)
            depth_norms[depth].append(v["mean"])

        depth_stats = {}
        for depth in depth_order:
            if depth in depth_norms:
                vals = depth_norms[depth]
                depth_stats[depth] = {
                    "mean": float(np.mean(vals)),
                    "std": float(np.std(vals)),
                    "n_layers": len(vals),
                }

        opt_results[opt_name] = {
            "ckpt_file": ckpt_file,
            "modified": mtime,
            "val_acc": val_acc,
            "epoch": epoch,
            "per_layer": norms,
            "depth_stats": depth_stats,
            "overall_mean": overall,
            "cross_layer_cv": cv,
        }

        del model
        torch.cuda.empty_cache()

    # === Print results ===

    print(f"\nMean Gradient Norms:")
    for opt, r in opt_results.items():
        print(f"  {opt:>10}: {r['overall_mean']:.6f}")

    print(f"\nCross-layer CV:")
    for opt, r in opt_results.items():
        print(f"  {opt:>10}: {r['cross_layer_cv']:.4f}")

    print(f"\nPer-depth Mean Gradient Norms:")
    header = f"  {'Depth':<16}"
    for opt in opt_results:
        header += f" {opt:>10}"
    print(header)
    print(f"  {'-' * (16 + 11 * len(opt_results))}")
    for depth in depth_order:
        row = f"  {depth:<16}"
        for opt, r in opt_results.items():
            if depth in r["depth_stats"]:
                row += f" {r['depth_stats'][depth]['mean']:>10.6f}"
            else:
                row += f" {'N/A':>10}"
        print(row)

    if "adamw" in opt_results:
        adamw_norms = opt_results["adamw"]["per_layer"]

        for ratio_opt in ["muon", "soap", "shampoo"]:
            if ratio_opt not in opt_results:
                continue
            other_norms = opt_results[ratio_opt]["per_layer"]

            depth_ratios = defaultdict(list)
            for layer_name in adamw_norms:
                if layer_name in other_norms:
                    a_val = adamw_norms[layer_name]["mean"]
                    o_val = other_norms[layer_name]["mean"]
                    if a_val > 1e-12:
                        ratio = o_val / a_val
                        depth = depth_fn(layer_name)
                        depth_ratios[depth].append(ratio)

            print(f"\n{ratio_opt.upper()}/AdamW Ratio by Depth:")
            for depth in depth_order:
                if depth in depth_ratios:
                    ratios = depth_ratios[depth]
                    print(f"  {depth:<16}: {np.mean(ratios):>8.4f} "
                          f"(n={len(ratios)}, std={np.std(ratios):.4f})")
            all_ratios = [r for rs in depth_ratios.values() for r in rs]
            if all_ratios:
                print(f"  {'Overall':<16}: {np.mean(all_ratios):>8.4f}")

    if "shampoo" in opt_results and "adamw" in opt_results:
        sh_mean = opt_results["shampoo"]["overall_mean"]
        aw_mean = opt_results["adamw"]["overall_mean"]
        print(f"\nShampoo Gradient Norm Check (P4):")
        print(f"  Shampoo:  {sh_mean:.6f}")
        print(f"  AdamW:    {aw_mean:.6f}")
        print(f"  Ratio:    {sh_mean / (aw_mean + 1e-12):.2f}x")
        if sh_mean > 3 * aw_mean:
            print(f"  ** Shampoo gradient norms significantly higher than AdamW **")

    return opt_results


def main():
    set_seed(SEED)
    device = torch.device(DEVICE)
    print(f"Device: {device}")
    print(f"Config: N_BATCHES={N_BATCHES}, BATCH_SIZE={BATCH_SIZE}, SEED={SEED}")

    loader = get_val_loader(BATCH_SIZE)
    print(f"CIFAR-100 test: {len(loader.dataset)} images")

    all_results = {}
    for arch_name, arch_cfg in ARCHITECTURES.items():
        all_results[arch_name] = analyze_architecture(
            arch_name, arch_cfg, loader, device)

    # Cross-architecture comparison
    print(f"\n{'=' * 70}")
    print("CROSS-ARCHITECTURE COMPARISON")
    print(f"{'=' * 70}")

    print(f"\n{'Arch':<12} {'Optimizer':<10} {'MeanNorm':>10} {'CV':>8} {'Val Acc':>8}")
    print(f"{'-' * 52}")
    for arch_name, opts in all_results.items():
        for opt, r in opts.items():
            acc_str = f"{r['val_acc']:.2f}" if r['val_acc'] else "N/A"
            print(f"{arch_name:<12} {opt:<10} {r['overall_mean']:>10.6f} "
                  f"{r['cross_layer_cv']:>8.4f} {acc_str:>8}")

    out_path = os.path.join(OUTPUT_DIR, "gradient_norm_extended_results.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
