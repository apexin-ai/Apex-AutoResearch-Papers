"""DeiT-S + Muon + standard DeiT augmentation on CIFAR-100 (224x224, 20ep).

Augmentation recipe (DeiT standard, same as deit_adamw_augmented.py):
  - RandAugment N=2 M=9
  - Mixup alpha=0.8
  - CutMix alpha=1.0, switch_prob=0.5
  - Label Smoothing 0.1
  - Stochastic Depth (drop_path) 0.1
  - Random Erasing p=0.25

Optimizer: Muon for attention/MLP weights, AdamW for head/embed/norm/bias.

Usage:
  python deit_muon_augmented.py --gpu 0 --seed 42
  python deit_muon_augmented.py --dry-run
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
from muon import muon_update
import shutil


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


_HEAD_PREFIXES = ("head.",)
_EMBED_PREFIXES = ("cls_token", "pos_embed", "dist_token", "patch_embed.")


def _norm_param_names(model):
    names = set()
    for mname, mod in model.named_modules():
        if isinstance(mod, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.GroupNorm)):
            for pname, _ in mod.named_parameters():
                names.add(f"{mname}.{pname}" if mname else pname)
    return names


def partition_params(model):
    norm_names = _norm_param_names(model)
    muon_params, adam_params = [], []
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        is_adam = (
            any(name.startswith(p) for p in _HEAD_PREFIXES)
            or any(name.startswith(p) or name == p.rstrip(".") for p in _EMBED_PREFIXES)
            or name in norm_names
            or name.endswith(".bias")
            or param.ndim < 2
        )
        (adam_params if is_adam else muon_params).append(param)
    return muon_params, adam_params


class SingleGPUMuon(torch.optim.Optimizer):
    def __init__(self, params, lr=0.02, momentum=0.95, weight_decay=0):
        defaults = dict(lr=lr, momentum=momentum, weight_decay=weight_decay)
        super().__init__(params, defaults)

    @torch.no_grad()
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()
        for group in self.param_groups:
            for p in group["params"]:
                if p.grad is None:
                    continue
                state = self.state[p]
                if len(state) == 0:
                    state["momentum_buffer"] = torch.zeros_like(p)
                g = p.grad.clone()
                update = muon_update(g, state["momentum_buffer"], beta=group["momentum"])
                p.mul_(1 - group["lr"] * group["weight_decay"])
                p.add_(update.reshape(p.shape), alpha=-group["lr"])
        return loss


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

    muon_params, adam_params = partition_params(model)
    print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)

    muon_opt = SingleGPUMuon(muon_params, lr=args.muon_lr, momentum=0.95)
    adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)
    muon_sched = torch.optim.lr_scheduler.CosineAnnealingLR(muon_opt, T_max=args.epochs)
    adam_sched = torch.optim.lr_scheduler.CosineAnnealingLR(adam_opt, T_max=args.epochs)

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
        f"optimizer=Muon(lr={args.muon_lr})+AdamW, augmentation=DeiT-standard, "
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
        print("  Muon step...", flush=True)
        muon_opt.step()
        adam_opt.step()
        print("=== DRY RUN PASSED ===", flush=True)
        return

    os.makedirs(args.output_dir, exist_ok=True)
    best_acc = 0.0
    lr_tag = str(args.muon_lr).replace(".", "")

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            images, labels = mixup_fn(images, labels)

            muon_opt.zero_grad()
            adam_opt.zero_grad()
            loss = train_criterion(model(images), labels)
            loss.backward()
            muon_opt.step()
            adam_opt.step()
            running_loss += loss.item()
            n_batches += 1
            if n_batches % 50 == 0:
                elapsed = time.time() - t0
                print(
                    f"  batch {n_batches}/{n_batches_total}, "
                    f"loss={loss.item():.4f}, elapsed={elapsed:.1f}s",
                    flush=True,
                )
        muon_sched.step()
        adam_sched.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(
            f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, "
            f"time={epoch_time:.1f}s, muon_lr={muon_sched.get_last_lr()[0]:.6f}",
            flush=True,
        )

        if val_acc > best_acc:
            best_acc = val_acc

        ckpt_path = os.path.join(
            args.output_dir,
            f"deit_small_muon_aug_lr{lr_tag}_s{args.seed}_ep{epoch}.pt",
        )
        if epoch in {1, 5, 10, 15, 20} or epoch == args.epochs:
            # _DISK_CHECK_SAVE_INJECTED_
            _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space on data disk: {_save_free_gb:.1f}G free", flush=True)
            torch.save({
                "state_dict": model.state_dict(),
                "muon_optimizer_state": muon_opt.state_dict(),
                "adam_optimizer_state": adam_opt.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "train_loss": avg_loss,
                "muon_lr": args.muon_lr,
                "config": {
                    "muon_lr": args.muon_lr, "augmentation": "deit_standard",
                    "mixup_alpha": 0.8, "cutmix_alpha": 1.0,
                    "label_smoothing": 0.1, "drop_path_rate": 0.1,
                    "rand_augment": "N2_M9", "random_erasing": 0.25,
                },
            }, ckpt_path)
            print(f"  checkpoint saved: {ckpt_path}", flush=True)

    print(f"TRAINING_COMPLETE best_val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DeiT-S + Muon + standard augmentation")
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--muon-lr", type=float, default=0.003)
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
