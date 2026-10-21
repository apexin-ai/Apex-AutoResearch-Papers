# DeiT-S AdamW + mild augmentation on CIFAR-100 (v2 kill gate).
#
# D022 decision: v1 full augmentation (RandAug M=9, Mixup, CutMix, DropPath,
# RandomErasing) was too aggressive for 20ep — epoch 7 only reached 15.65%.
# v2 uses mild augmentation appropriate for short training.
#
# Augmentation (mild):
#   RandAugment N=2 M=3 | Label Smoothing 0.1
#   NO Mixup / CutMix / RandomErasing / DropPath
#
# Kill gate: if val_acc >= 58% and Muon gap <= 3pp, magnitude claim collapses.
#
# Schedule: linear warmup (2ep) -> cosine decay
# Output: checkpoints/deit_adamw_mild_aug_s{seed}_ep{epochs}.pt
# checkpoint path migrated to /root/autodl-tmp (root partition is ~30G; checkpoints filled it).
import argparse
import os
import shutil
import random
import time

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


# --- Augmentation config (mild, 20ep-appropriate) ---
AUGMENTATION = {
    "randaugment_n": 2,
    "randaugment_m": 3,    # M=3 not 9; v1 M=9 was too strong for 20ep
    "label_smoothing": 0.1,
    # Explicitly disabled for v2:
    # mixup, cutmix, random_erasing, drop_path
}

CIFAR100_MEAN = (0.5071, 0.4867, 0.4408)
CIFAR100_STD = (0.2675, 0.2565, 0.2761)


def get_dataloaders(batch_size):
    train_tf = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandAugment(
            num_ops=AUGMENTATION["randaugment_n"],
            magnitude=AUGMENTATION["randaugment_m"],
        ),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
    ])
    val_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
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

    # No drop_path_rate — mild augmentation skips DropPath
    model = timm.create_model(
        "deit_small_patch16_224", pretrained=False, num_classes=100,
    ).to(device)

    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.lr, weight_decay=0.05,
    )

    # Linear warmup (2ep) -> cosine decay
    warmup_scheduler = torch.optim.lr_scheduler.LinearLR(
        optimizer, start_factor=1e-3, end_factor=1.0,
        total_iters=args.warmup_epochs,
    )
    cosine_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=args.epochs - args.warmup_epochs,
    )
    scheduler = torch.optim.lr_scheduler.SequentialLR(
        optimizer, schedulers=[warmup_scheduler, cosine_scheduler],
        milestones=[args.warmup_epochs],
    )

    # Label smoothing via CrossEntropyLoss (no Mixup/CutMix -> no SoftTargetCrossEntropy)
    criterion = nn.CrossEntropyLoss(label_smoothing=AUGMENTATION["label_smoothing"])

    train_dl, val_dl = get_dataloaders(args.batch_size)
    n_batches_total = len(train_dl)
    param_count = sum(p.numel() for p in model.parameters()) / 1e6

    print(
        f"model=deit_small_patch16_224, params={param_count:.1f}M, device={device}, "
        f"optimizer=AdamW(lr={args.lr}, wd=0.05), warmup={args.warmup_epochs}ep, "
        f"augmentation=mild(RandAug_N{AUGMENTATION['randaugment_n']}_M{AUGMENTATION['randaugment_m']}, "
        f"LabelSmooth={AUGMENTATION['label_smoothing']}, no_mixup/cutmix/RE/droppath)",
        flush=True,
    )
    print(f"Train transforms: {train_dl.dataset.transform}", flush=True)

    os.makedirs(args.output_dir, exist_ok=True)
    best_acc = 0.0

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
        current_lr = scheduler.get_last_lr()[0]
        print(
            f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, "
            f"time={epoch_time:.1f}s, lr={current_lr:.6f}",
            flush=True,
        )

        if val_acc > best_acc:
            best_acc = val_acc
            ckpt_path = os.path.join(
                args.output_dir,
                f"deit_adamw_mild_aug_s{args.seed}_ep{args.epochs}.pt",
            )
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
                    "optimizer": "adamw", "lr": args.lr, "weight_decay": 0.05,
                    "warmup_epochs": args.warmup_epochs, "total_epochs": args.epochs,
                    "augmentation": "mild_v2",
                    "randaugment": f"N{AUGMENTATION['randaugment_n']}_M{AUGMENTATION['randaugment_m']}",
                    "label_smoothing": AUGMENTATION["label_smoothing"],
                    "mixup": None, "cutmix": None,
                    "random_erasing": None, "drop_path": None,
                },
            }, ckpt_path)
            print(f"  best checkpoint saved: {ckpt_path}", flush=True)

    print(f"TRAINING_COMPLETE best_val_acc={best_acc:.2f}%", flush=True)
    print("EXIT_CODE=0", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="DeiT-S AdamW + mild augmentation (v2 kill gate)",
    )
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--warmup-epochs", type=int, default=2)
    parser.add_argument("--output-dir", type=str,
                        default="/root/autodl-tmp/checkpoints/spectral_optim/")
    args = parser.parse_args()
    # _DISK_CHECK_STARTUP_INJECTED_
    _disk_free_gb = shutil.disk_usage('/').free / (1024**3)
    if _disk_free_gb < 2.0:
        raise RuntimeError(
            f"Disk space critically low: {_disk_free_gb:.1f}G free on /. "
            f"Need >= 2G. Clean up checkpoints or use /root/autodl-tmp/."
        )
    train(args)
