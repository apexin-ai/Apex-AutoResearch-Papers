"""DeiT-S + AdamW + standard DeiT augmentation on CIFAR-100 (224x224, 20ep).

Augmentation recipe (DeiT standard):
  - RandAugment N=2 M=9
  - Mixup alpha=0.8
  - CutMix alpha=1.0, switch_prob=0.5
  - Label Smoothing 0.1
  - Stochastic Depth (drop_path) 0.1
  - Random Erasing p=0.25

Usage:
  python deit_adamw_augmented.py --gpu 0 --seed 42
  python deit_adamw_augmented.py --dry-run          # verify pipeline only
"""
# checkpoint path migrated to /root/autodl-tmp (root partition is ~30G; checkpoints filled it).
import argparse
import os
import random
import time

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm
from timm.data import Mixup
from timm.loss import SoftTargetCrossEntropy
import shutil


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def get_dataloaders(batch_size):
    mean, std = (0.5071, 0.4867, 0.4408), (0.2675, 0.2565, 0.2761)
    train_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandAugment(num_ops=2, magnitude=9),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
        transforms.RandomErasing(p=0.25),
    ])
    val_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    train_ds = datasets.CIFAR100(
        root="/root/spectral_optim_vision_geometry/data",
        train=True, download=True, transform=train_tf,
    )
    val_ds = datasets.CIFAR100(
        root="/root/spectral_optim_vision_geometry/data",
        train=False, download=True, transform=val_tf,
    )
    train_dl = DataLoader(
        train_ds, batch_size=batch_size, shuffle=True,
        num_workers=4, pin_memory=True, drop_last=True,
    )
    val_dl = DataLoader(
        val_ds, batch_size=batch_size, shuffle=False,
        num_workers=4, pin_memory=True,
    )
    return train_dl, val_dl


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct, total = 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        correct += (model(images).argmax(1) == labels).sum().item()
        total += labels.size(0)
    return 100.0 * correct / total


def train(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    model = timm.create_model(
        "deit_small_patch16_224", pretrained=False,
        num_classes=100, drop_path_rate=0.1,
    ).to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.05)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    mixup_fn = Mixup(
        mixup_alpha=0.8, cutmix_alpha=1.0,
        prob=1.0, switch_prob=0.5, mode="batch",
        label_smoothing=0.1, num_classes=100,
    )
    train_criterion = SoftTargetCrossEntropy()

    train_dl, val_dl = get_dataloaders(args.batch_size)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(
        f"model=deit_small_aug, params={param_count:.1f}M, device={device}, "
        f"optimizer=AdamW, lr={args.lr}, augmentation=DeiT-standard, "
        f"batches/epoch={n_batches_total}",
        flush=True,
    )

    if args.dry_run:
        print("=== DRY RUN: verifying augmentation pipeline ===", flush=True)
        images, labels = next(iter(train_dl))
        print(f"  raw batch: images={images.shape}, labels={labels.shape} (dtype={labels.dtype})", flush=True)
        images, labels = images.to(device), labels.to(device)
        mixed_images, mixed_labels = mixup_fn(images, labels)
        print(f"  after mixup: images={mixed_images.shape}, labels={mixed_labels.shape} (dtype={mixed_labels.dtype})", flush=True)
        print(f"  mixed_labels sample (first 3 rows, first 5 cols):", flush=True)
        print(f"  {mixed_labels[:3, :5]}", flush=True)
        logits = model(mixed_images)
        print(f"  model output: {logits.shape}", flush=True)
        loss = train_criterion(logits, mixed_labels)
        print(f"  loss={loss.item():.4f}", flush=True)
        loss.backward()
        print("=== DRY RUN PASSED ===", flush=True)
        return

    os.makedirs(args.output_dir, exist_ok=True)
    best_acc = 0.0
    ckpt_name = f"deit_small_adamw_aug_s{args.seed}.pt"

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            images, labels = mixup_fn(images, labels)

            optimizer.zero_grad()
            loss = train_criterion(model(images), labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            n_batches += 1
            if n_batches % 50 == 0:
                elapsed = time.time() - t0
                print(
                    f"  batch {n_batches}/{n_batches_total}, "
                    f"loss={loss.item():.4f}, elapsed={elapsed:.1f}s",
                    flush=True,
                )
        scheduler.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(
            f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, "
            f"time={epoch_time:.1f}s, lr={scheduler.get_last_lr()[0]:.6f}",
            flush=True,
        )

        if val_acc > best_acc:
            best_acc = val_acc
            # _DISK_CHECK_SAVE_INJECTED_
            _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space on data disk: {_save_free_gb:.1f}G free", flush=True)
            torch.save({
                "state_dict": model.state_dict(),
                "optimizer_state": optimizer.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "train_loss": avg_loss,
                "config": {
                    "lr": args.lr, "augmentation": "deit_standard",
                    "mixup_alpha": 0.8, "cutmix_alpha": 1.0,
                    "label_smoothing": 0.1, "drop_path_rate": 0.1,
                    "rand_augment": "N2_M9", "random_erasing": 0.25,
                },
            }, os.path.join(args.output_dir, ckpt_name))

    print(f"TRAINING_COMPLETE best_val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DeiT-S + AdamW + standard augmentation")
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    parser.add_argument("--dry-run", action="store_true", help="Verify pipeline only, no training")
    args = parser.parse_args()
    # _DISK_CHECK_STARTUP_INJECTED_
    _disk_free_gb = shutil.disk_usage('/').free / (1024**3)
    if _disk_free_gb < 2.0:
        raise RuntimeError(
            f"Disk space critically low: {_disk_free_gb:.1f}G free on /. "
            f"Need >= 2G. Clean up checkpoints or use /root/autodl-tmp/."
        )
    train(args)
