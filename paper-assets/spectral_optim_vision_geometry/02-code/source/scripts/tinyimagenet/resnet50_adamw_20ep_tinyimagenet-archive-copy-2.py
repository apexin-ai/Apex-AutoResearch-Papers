"""B5.2 ResNet-50 + AdamW baseline on Tiny-ImageNet-200 (20 epochs).

Dataset: Tiny-ImageNet-200 (200 classes, ~100k train / ~10k val)
Model: ResNet-50 (timm, from scratch)
Optimizer: AdamW (lr=2e-3, betas=(0.9,0.999), wd=0.05)
Schedule: cosine annealing, T_max=20, no warmup
Batch size: 128, seed=42

Usage:
  python resnet50_adamw_20ep_tinyimagenet.py --gpu 0 --seed 42
  python resnet50_adamw_20ep_tinyimagenet.py --dry-run
"""
import argparse
import os
import random
import shutil
import time

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm


NUM_CLASSES = 200
DATA_DIR = "/root/autodl-tmp/tiny-imagenet-200"
IMAGENET_MEAN = (0.4802, 0.4481, 0.3975)
IMAGENET_STD = (0.2770, 0.2691, 0.2821)
CKPT_DIR = "/root/runs/spectral_optim_vision_geometry/checkpoints"


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def get_dataloaders(batch_size):
    train_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])
    val_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])
    train_ds = datasets.ImageFolder(os.path.join(DATA_DIR, "train"), transform=train_tf)
    val_ds = datasets.ImageFolder(os.path.join(DATA_DIR, "val"), transform=val_tf)
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

    model = timm.create_model("resnet50", pretrained=False, num_classes=NUM_CLASSES).to(device)

    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.lr,
        betas=(0.9, 0.999), weight_decay=0.05,
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    criterion = nn.CrossEntropyLoss()

    train_dl, val_dl = get_dataloaders(args.batch_size)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(
        f"model=resnet50, params={param_count:.1f}M, device={device}, "
        f"optimizer=AdamW(lr={args.lr}), dataset=TinyImageNet-200, "
        f"batches/epoch={n_batches_total}",
        flush=True,
    )

    if args.dry_run:
        print("=== DRY RUN ===", flush=True)
        images, labels = next(iter(train_dl))
        images, labels = images.to(device), labels.to(device)
        logits = model(images)
        print(f"  batch: images={images.shape}, labels={labels.shape}", flush=True)
        print(f"  model output: {logits.shape}", flush=True)
        loss = criterion(logits, labels)
        print(f"  loss={loss.item():.4f}", flush=True)
        loss.backward()
        optimizer.step()
        print("=== DRY RUN PASSED ===", flush=True)
        return

    os.makedirs(CKPT_DIR, exist_ok=True)
    best_acc = 0.0
    ckpt_path = os.path.join(
        CKPT_DIR, f"resnet50_adamw_lr2e-3_tinyimagenet_s{args.seed}_best.pt"
    )

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            loss = criterion(model(images), labels)
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
            f"Epoch [{epoch}/{args.epochs}] "
            f"Train Loss: {avg_loss:.4f} Val Acc: {val_acc:.2f}% "
            f"time={epoch_time:.1f}s lr={scheduler.get_last_lr()[0]:.6f}",
            flush=True,
        )

        if val_acc > best_acc:
            best_acc = val_acc
            _save_free_gb = shutil.disk_usage('/root').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space: {_save_free_gb:.1f}G free", flush=True)
            torch.save({
                "state_dict": model.state_dict(),
                "optimizer_state": optimizer.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "train_loss": avg_loss,
                "model": "resnet50",
                "optimizer": "adamw",
                "lr": args.lr,
                "dataset": "tiny-imagenet-200",
            }, ckpt_path)

    print(f"TRAINING_COMPLETE best_val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="B5.2 ResNet-50 + AdamW on Tiny-ImageNet-200")
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--lr", type=float, default=2e-3)
    parser.add_argument("--output-dir", type=str, default=CKPT_DIR)
    parser.add_argument("--dry-run", action="store_true", help="Verify pipeline only")
    args = parser.parse_args()
    _disk_free_gb = shutil.disk_usage('/').free / (1024**3)
    if _disk_free_gb < 2.0:
        raise RuntimeError(
            f"Disk space critically low: {_disk_free_gb:.1f}G free on /. "
            f"Need >= 2G. Clean up or use data disk."
        )
    train(args)
