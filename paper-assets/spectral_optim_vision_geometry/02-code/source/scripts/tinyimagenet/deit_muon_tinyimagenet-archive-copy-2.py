"""DeiT-S + Muon on Tiny-ImageNet-200 (64x64 -> 224x224, 20ep).

Dataset: Tiny-ImageNet-200 (200 classes, ~100k train / ~10k val)
Model: DeiT-S (deit_small_patch16_224, timm)
Optimizer: Muon for attention/MLP weights, AdamW for head/embed/norm/bias.

Differences from CIFAR-100 version (muon_train.py --model deit_small):
  - num_classes=200 (was 100)
  - ImageFolder loader (was datasets.CIFAR100)
  - data_path=/root/autodl-tmp/tiny-imagenet-200/
  - Tiny-ImageNet mean/std normalization

Usage:
  python deit_muon_tinyimagenet.py --gpu 0 --seed 42
  python deit_muon_tinyimagenet.py --dry-run
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
from muon import muon_update


# --- Tiny-ImageNet config (differs from CIFAR-100) ---
NUM_CLASSES = 200
DATA_DIR = "/root/autodl-tmp/tiny-imagenet-200"
IMAGENET_MEAN = (0.4802, 0.4481, 0.3975)
IMAGENET_STD = (0.2770, 0.2691, 0.2821)

_HEAD_PREFIXES = ("head.",)
_EMBED_PREFIXES = ("cls_token", "pos_embed", "dist_token", "patch_embed.")


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def _norm_param_names(model):
    names = set()
    for mname, mod in model.named_modules():
        if isinstance(mod, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.GroupNorm)):
            for pname, _ in mod.named_parameters():
                names.add(f"{mname}.{pname}" if mname else pname)
    return names


def partition_params(model):
    """Split params: Muon for attention/MLP weights, AdamW for head/embed/norm/bias."""
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
    # --- ImageFolder instead of CIFAR100 ---
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

    # --- num_classes=200 (was 100), resize 64->224 handled by transforms ---
    model = timm.create_model(
        "deit_small_patch16_224", pretrained=False,
        num_classes=NUM_CLASSES, drop_path_rate=0.1,
    ).to(device)

    muon_params, adam_params = partition_params(model)
    print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)

    muon_opt = SingleGPUMuon(muon_params, lr=args.muon_lr, momentum=0.95)
    adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)
    muon_sched = torch.optim.lr_scheduler.CosineAnnealingLR(muon_opt, T_max=args.epochs)
    adam_sched = torch.optim.lr_scheduler.CosineAnnealingLR(adam_opt, T_max=args.epochs)
    criterion = nn.CrossEntropyLoss()

    train_dl, val_dl = get_dataloaders(args.batch_size)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(
        f"model=deit_small_patch16_224, params={param_count:.1f}M, device={device}, "
        f"optimizer=Muon(lr={args.muon_lr})+AdamW, dataset=TinyImageNet-200, "
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
        muon_opt.step()
        adam_opt.step()
        print("=== DRY RUN PASSED ===", flush=True)
        return

    os.makedirs(args.output_dir, exist_ok=True)
    best_acc = 0.0
    ckpt_name = f"tinyimagenet_deit_muon_s{args.seed}.pt"

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            muon_opt.zero_grad()
            adam_opt.zero_grad()
            loss = criterion(model(images), labels)
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
                "model": "deit_small",
                "optimizer": "muon",
                "dataset": "tiny-imagenet-200",
            }, os.path.join(args.output_dir, ckpt_name))

    print(f"TRAINING_COMPLETE best_val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DeiT-S + Muon on Tiny-ImageNet-200")
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--muon-lr", type=float, default=0.003)
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    parser.add_argument("--dry-run", action="store_true", help="Verify pipeline only, no training")
    args = parser.parse_args()
    _disk_free_gb = shutil.disk_usage('/').free / (1024**3)
    if _disk_free_gb < 2.0:
        raise RuntimeError(
            f"Disk space critically low: {_disk_free_gb:.1f}G free on /. "
            f"Need >= 2G. Clean up checkpoints or use /root/autodl-tmp/."
        )
    train(args)
