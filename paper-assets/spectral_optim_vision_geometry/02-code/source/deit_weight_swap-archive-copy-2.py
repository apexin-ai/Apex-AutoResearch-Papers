"""DeiT-S weight swap ablation: Muon vs AdamW on CIFAR-100.

Swaps weights at three granularity levels and measures val_acc change:
  1. Special components: cls_token, pos_embed, patch_embed, final norm, head
  2. Per-block: swap entire transformer block (blocks.0-11)
  3. Per-component: attn.qkv, attn.proj, mlp.fc1, mlp.fc2, norm1, norm2

Direction: bidirectional -- in Muon model replace with AdamW (muon_drop),
in AdamW model replace with Muon (adamw_gain).

If AdamW checkpoint does not exist, trains it first (20ep, AdamW, lr=3e-4).
"""

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
DELTA_THRESHOLD = 0.5  # pp


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


def get_train_loader(data_dir, batch_size=128, num_workers=4):
    tf = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
    ])
    ds = datasets.CIFAR100(root=data_dir, train=True, download=True, transform=tf)
    return DataLoader(ds, batch_size=batch_size, shuffle=True,
                      num_workers=num_workers, pin_memory=True, drop_last=True)


def load_state_dict(ckpt_path):
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    if isinstance(ckpt, dict) and "state_dict" in ckpt:
        return ckpt["state_dict"]
    return ckpt


def create_model(num_classes=100):
    return timm.create_model("deit_small_patch16_224", pretrained=False,
                             num_classes=num_classes)


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct, total = 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        correct += (model(images).argmax(1) == labels).sum().item()
        total += labels.size(0)
    return 100.0 * correct / total


def train_adamw_baseline(device, data_dir, output_path, epochs=20, seed=42):
    """Train DeiT-S with AdamW when checkpoint is missing."""
    print(f"\n=== Training AdamW baseline ({epochs} epochs) ===", flush=True)
    set_seed(seed)
    model = create_model().to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.05)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    criterion = nn.CrossEntropyLoss()

    train_loader = get_train_loader(data_dir, batch_size=128)
    val_loader = get_val_loader(data_dir, batch_size=256)

    best_acc = 0.0
    for epoch in range(1, epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            loss = criterion(model(images), labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            n_batches += 1
        scheduler.step()

        val_acc = evaluate(model, val_loader, device)
        avg_loss = running_loss / n_batches
        print(f"  epoch={epoch}/{epochs}, loss={avg_loss:.4f}, "
              f"val_acc={val_acc:.2f}%", flush=True)

        if val_acc > best_acc:
            best_acc = val_acc
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            torch.save({
                "state_dict": model.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
            }, output_path)

    print(f"  AdamW training done. best_val_acc={best_acc:.2f}%, "
          f"saved to {output_path}", flush=True)
    return best_acc


# ---------------------------------------------------------------------------
# Swap group definitions for DeiT-S
# ---------------------------------------------------------------------------

def get_swap_groups(state_dict_keys):
    """Build hierarchical swap groups for DeiT-S.

    Returns list of (group_name, group_type, key_list) where group_type is
    one of: special, block, component.
    """
    groups = []

    # Special components
    special = {
        "cls_token": [k for k in state_dict_keys if k == "cls_token"],
        "pos_embed": [k for k in state_dict_keys if k == "pos_embed"],
        "patch_embed": [k for k in state_dict_keys
                        if k.startswith("patch_embed.")],
        "final_norm": [k for k in state_dict_keys
                       if k.startswith("norm.") and "blocks" not in k],
        "head": [k for k in state_dict_keys if k.startswith("head.")],
    }
    for name, keys in special.items():
        if keys:
            groups.append((name, "special", keys))

    # Per-block (blocks.0 through blocks.11)
    for i in range(12):
        prefix = f"blocks.{i}."
        keys = [k for k in state_dict_keys if k.startswith(prefix)]
        if keys:
            groups.append((f"block_{i}", "block", keys))

    # Per-component within each block
    components = ["norm1", "attn.qkv", "attn.proj", "norm2", "mlp.fc1", "mlp.fc2"]
    for i in range(12):
        for comp in components:
            prefix = f"blocks.{i}.{comp}."
            keys = [k for k in state_dict_keys if k.startswith(prefix)]
            if keys:
                groups.append((f"block_{i}.{comp}", "component", keys))

    return groups


def count_params(state_dict, keys):
    return sum(state_dict[k].numel() for k in keys if k in state_dict)


def swap_keys(model, keys, source_sd):
    """Replace parameters matching keys with source_sd values. Returns originals."""
    originals = {}
    sd = model.state_dict()
    for k in keys:
        if k in source_sd and k in sd:
            originals[k] = sd[k].clone()

    if originals:
        new_sd = model.state_dict()
        for k in originals:
            new_sd[k] = source_sd[k]
        model.load_state_dict(new_sd, strict=True)
    return originals


def restore_keys(model, originals):
    if originals:
        sd = model.state_dict()
        for k, v in originals.items():
            sd[k] = v
        model.load_state_dict(sd, strict=True)


# ---------------------------------------------------------------------------
# Main ablation
# ---------------------------------------------------------------------------

def run_ablation(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}", flush=True)

    # Train AdamW baseline if checkpoint missing
    if not os.path.exists(args.adamw_ckpt):
        print(f"AdamW checkpoint not found at {args.adamw_ckpt}, "
              "training...", flush=True)
        train_adamw_baseline(device, args.data_dir, args.adamw_ckpt,
                             epochs=args.adamw_epochs, seed=args.seed)

    muon_sd = load_state_dict(args.muon_ckpt)
    adamw_sd = load_state_dict(args.adamw_ckpt)
    print(f"Loaded: muon={len(muon_sd)} keys, "
          f"adamw={len(adamw_sd)} keys", flush=True)

    val_loader = get_val_loader(args.data_dir, batch_size=args.batch_size)
    print(f"Val set: {len(val_loader.dataset)} images", flush=True)

    # Baselines
    muon_model = create_model().to(device)
    muon_model.load_state_dict(muon_sd)
    muon_baseline = evaluate(muon_model, val_loader, device)
    print(f"Muon baseline: {muon_baseline:.2f}%", flush=True)

    adamw_model = create_model().to(device)
    adamw_model.load_state_dict(adamw_sd)
    adamw_baseline = evaluate(adamw_model, val_loader, device)
    print(f"AdamW baseline: {adamw_baseline:.2f}%", flush=True)
    print(f"Gap: {muon_baseline - adamw_baseline:.2f}pp", flush=True)

    swap_groups = get_swap_groups(list(muon_sd.keys()))
    n_groups = len(swap_groups)
    print(f"\nSwap groups: {n_groups} (special + block + component)", flush=True)

    if args.dry_run:
        print("\n[DRY RUN] Groups:")
        for i, (name, gtype, keys) in enumerate(swap_groups):
            pc = count_params(muon_sd, keys)
            print(f"  {i+1}. {name} ({gtype}, {pc:,} params, {len(keys)} keys)")
        print(f"\nBaselines: Muon={muon_baseline:.2f}%, "
              f"AdamW={adamw_baseline:.2f}%")
        return

    results = []
    t0 = time.time()

    for i, (group_name, group_type, keys) in enumerate(swap_groups, 1):
        param_count = count_params(muon_sd, keys)

        # Direction 1: Muon model, replace group with AdamW weights
        originals = swap_keys(muon_model, keys, adamw_sd)
        if originals:
            swapped_acc = evaluate(muon_model, val_loader, device)
            muon_drop = muon_baseline - swapped_acc
            restore_keys(muon_model, originals)
        else:
            muon_drop = 0.0

        # Direction 2: AdamW model, replace group with Muon weights
        originals = swap_keys(adamw_model, keys, muon_sd)
        if originals:
            swapped_acc = evaluate(adamw_model, val_loader, device)
            adamw_gain = swapped_acc - adamw_baseline
            restore_keys(adamw_model, originals)
        else:
            adamw_gain = 0.0

        muon_benefit = ((muon_drop > DELTA_THRESHOLD)
                        or (adamw_gain > DELTA_THRESHOLD))

        results.append({
            "group_name": group_name,
            "group_type": group_type,
            "param_count": param_count,
            "n_keys": len(keys),
            "muon_drop_pp": f"{muon_drop:.2f}",
            "adamw_gain_pp": f"{adamw_gain:.2f}",
            "muon_benefit": int(muon_benefit),
        })

        elapsed = time.time() - t0
        tag = " ** BENEFIT" if muon_benefit else ""
        print(f"  [{i}/{n_groups}] {group_name} ({group_type}, "
              f"{param_count:,}p): muon_drop={muon_drop:+.2f} "
              f"adamw_gain={adamw_gain:+.2f}{tag}  [{elapsed:.0f}s]",
              flush=True)

    # Save CSV
    out_dir = os.path.dirname(args.output)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    fields = ["group_name", "group_type", "param_count", "n_keys",
              "muon_drop_pp", "adamw_gain_pp", "muon_benefit"]
    with open(args.output, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    n_benefit = sum(r["muon_benefit"] for r in results)
    total_time = time.time() - t0
    print(f"\nDone in {total_time:.0f}s. Results: {args.output}")
    print(f"Muon baseline: {muon_baseline:.2f}%, "
          f"AdamW baseline: {adamw_baseline:.2f}%")
    print(f"Groups with muon_benefit: {n_benefit}/{len(results)} "
          f"(tau={DELTA_THRESHOLD}pp)")
    print(f"ABLATION_COMPLETE n_groups={len(results)} n_benefit={n_benefit}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="DeiT-S weight swap ablation: Muon vs AdamW")
    p.add_argument("--muon-ckpt", type=str, required=True)
    p.add_argument("--adamw-ckpt", type=str, required=True,
                   help="If missing, trains automatically.")
    p.add_argument("--adamw-epochs", type=int, default=20,
                   help="Epochs for AdamW training if ckpt missing.")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--data-dir", type=str,
                   default="/root/spectral_optim_vision_geometry/data")
    p.add_argument("--output", type=str,
                   default="/root/spectral_optim_vision_geometry/results/"
                   "deit_weight_swap.csv")
    p.add_argument("--batch-size", type=int, default=256)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    run_ablation(args)
