# Per-layer weight swap ablation: Muon vs AdamW on ResNet-50 / CIFAR-100
# For each module, swap Muon<->AdamW weights and measure accuracy change.
# Output: CSV with muon_drop_pp, adamw_gain_pp, muon_benefit per layer.

import argparse
import csv
import os
import random
import time

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm

CIFAR100_MEAN = (0.5071, 0.4867, 0.4408)
CIFAR100_STD = (0.2675, 0.2565, 0.2761)
DELTA_THRESHOLD = 0.5  # pp, D003


def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def get_val_loader(data_dir, batch_size=256, num_workers=4):
    tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
    ])
    ds = datasets.CIFAR100(root=data_dir, train=False, download=True, transform=tf)
    return DataLoader(ds, batch_size=batch_size, shuffle=False,
                      num_workers=num_workers, pin_memory=True)


def load_state_dict(ckpt_path):
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    if isinstance(ckpt, dict) and "state_dict" in ckpt:
        return ckpt["state_dict"]
    return ckpt


def create_model(model_name, num_classes=100):
    registry = {"resnet50": "resnet50", "deit_small": "deit_small_patch16_224"}
    return timm.create_model(registry[model_name], pretrained=False, num_classes=num_classes)


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct, total = 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        correct += (model(images).argmax(1) == labels).sum().item()
        total += labels.size(0)
    return 100.0 * correct / total


def get_swappable_modules(model):
    """Return dict of module_name -> (module, layer_type) for Conv2d and Linear layers."""
    modules = {}
    for name, mod in model.named_modules():
        if isinstance(mod, nn.Conv2d):
            modules[name] = (mod, "conv")
        elif isinstance(mod, nn.Linear):
            modules[name] = (mod, "linear")
    return modules


def count_module_params(state_dict, module_name):
    prefix = module_name + "."
    total = 0
    for k, v in state_dict.items():
        if k.startswith(prefix) or k == module_name:
            total += v.numel()
    return total


def swap_module_weights(model, module_name, source_sd):
    """Swap all parameters of a module with values from source_sd. Returns originals for restore."""
    originals = {}
    param_dict = dict(model.named_parameters())
    buf_dict = dict(model.named_buffers())

    for suffix in ("weight", "bias"):
        key = f"{module_name}.{suffix}"
        if key in source_sd and key in param_dict:
            originals[key] = param_dict[key].data.clone()
            param_dict[key].data.copy_(source_sd[key])

    return originals


def restore_weights(model, originals):
    param_dict = dict(model.named_parameters())
    for key, data in originals.items():
        param_dict[key].data.copy_(data)


def run_ablation(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}", flush=True)

    muon_sd = load_state_dict(args.muon_ckpt)
    adamw_sd = load_state_dict(args.adamw_ckpt)
    print(f"Loaded checkpoints: muon={len(muon_sd)} keys, adamw={len(adamw_sd)} keys", flush=True)

    val_loader = get_val_loader(args.data_dir, batch_size=args.batch_size)
    print(f"Val set: {len(val_loader.dataset)} images", flush=True)

    # Build Muon model and evaluate baseline
    muon_model = create_model(args.model).to(device)
    muon_model.load_state_dict(muon_sd)
    muon_baseline = evaluate(muon_model, val_loader, device)
    print(f"Muon baseline: {muon_baseline:.2f}%", flush=True)

    # Build AdamW model and evaluate baseline
    adamw_model = create_model(args.model).to(device)
    adamw_model.load_state_dict(adamw_sd)
    adamw_baseline = evaluate(adamw_model, val_loader, device)
    print(f"AdamW baseline: {adamw_baseline:.2f}%", flush=True)
    print(f"Gap: {muon_baseline - adamw_baseline:.2f}pp", flush=True)

    modules = get_swappable_modules(muon_model)
    n_modules = len(modules)
    print(f"\nSwappable modules: {n_modules}", flush=True)

    if args.dry_run:
        print("\n[DRY RUN] Would test these modules:")
        for i, (name, (mod, ltype)) in enumerate(modules.items()):
            pc = count_module_params(muon_sd, name)
            print(f"  {i+1}. {name} ({ltype}, {pc:,} params)")
        print(f"\nDry run complete. Baselines: Muon={muon_baseline:.2f}%, AdamW={adamw_baseline:.2f}%")
        return

    results = []
    t0 = time.time()

    for i, (module_name, (mod, ltype)) in enumerate(modules.items(), 1):
        param_count = count_module_params(muon_sd, module_name)

        # Direction 1: In Muon model, replace this layer with AdamW weights -> measure drop
        originals = swap_module_weights(muon_model, module_name, adamw_sd)
        if originals:
            muon_swapped_acc = evaluate(muon_model, val_loader, device)
            muon_drop = muon_baseline - muon_swapped_acc
            restore_weights(muon_model, originals)
        else:
            muon_drop = 0.0

        # Direction 2: In AdamW model, replace this layer with Muon weights -> measure gain
        originals = swap_module_weights(adamw_model, module_name, muon_sd)
        if originals:
            adamw_swapped_acc = evaluate(adamw_model, val_loader, device)
            adamw_gain = adamw_swapped_acc - adamw_baseline
            restore_weights(adamw_model, originals)
        else:
            adamw_gain = 0.0

        muon_benefit = (muon_drop > DELTA_THRESHOLD) or (adamw_gain > DELTA_THRESHOLD)

        results.append({
            "layer_name": module_name,
            "layer_type": ltype,
            "param_count": param_count,
            "muon_drop_pp": f"{muon_drop:.2f}",
            "adamw_gain_pp": f"{adamw_gain:.2f}",
            "muon_benefit": int(muon_benefit),
        })

        elapsed = time.time() - t0
        tag = " ** BENEFIT" if muon_benefit else ""
        print(f"  [{i}/{n_modules}] {module_name} ({ltype}, {param_count:,}p): "
              f"muon_drop={muon_drop:+.2f} adamw_gain={adamw_gain:+.2f}{tag}  "
              f"[{elapsed:.0f}s]", flush=True)

    # Save CSV
    os.makedirs(args.output_dir, exist_ok=True)
    csv_path = os.path.join(args.output_dir, f"{args.model}_weight_swap.csv")
    fields = ["layer_name", "layer_type", "param_count", "muon_drop_pp", "adamw_gain_pp", "muon_benefit"]
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    n_benefit = sum(r["muon_benefit"] for r in results)
    total_time = time.time() - t0
    print(f"\nDone in {total_time:.0f}s. Results: {csv_path}")
    print(f"Muon baseline: {muon_baseline:.2f}%, AdamW baseline: {adamw_baseline:.2f}%")
    print(f"Layers with muon_benefit: {n_benefit}/{len(results)} (τ={DELTA_THRESHOLD}pp)")
    print(f"ABLATION_COMPLETE n_layers={len(results)} n_benefit={n_benefit}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Per-layer weight swap ablation: Muon vs AdamW")
    parser.add_argument("--model", type=str, default="resnet50", choices=["resnet50", "deit_small"])
    parser.add_argument("--muon-ckpt", type=str, required=True)
    parser.add_argument("--adamw-ckpt", type=str, required=True)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--data-dir", type=str, default="/root/spectral_optim_vision_geometry/data")
    parser.add_argument("--output-dir", type=str, default="/root/spectral_optim_vision_geometry/results")
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run_ablation(args)
