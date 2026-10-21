# DeiT-S with standard DeiT augmentation recipe on CIFAR-100 (224x224).
# Supports both AdamW and Muon optimizers for fair comparison.
#
# Augmentation recipe (DeiT standard from timm):
#   RandAugment N=2, M=9 | Mixup alpha=0.8 | CutMix alpha=1.0 (switch_prob=0.5)
#   Label Smoothing 0.1 | Stochastic Depth (drop_path) 0.1 | Random Erasing p=0.25
#
# Usage:
#   python3 deit_augmented_train.py --optimizer adamw --seed 42 --gpu 0
#   python3 deit_augmented_train.py --optimizer muon --muon-lr 0.003 --seed 42 --gpu 0
#   python3 deit_augmented_train.py --dry-run
#
# Output: checkpoints/deit_small_{optimizer}_aug_s{seed}.pt
# Deps: torch, torchvision, timm (for model + Mixup)
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
from timm.data import Mixup
from timm.loss import SoftTargetCrossEntropy


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


# --- Muon support ---
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
        from muon import muon_update
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


# --- Data ---
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
        "deit_small_patch16_224", pretrained=False, num_classes=100,
        drop_path_rate=0.1,
    ).to(device)

    # Optimizer setup
    if args.optimizer == "adamw":
        optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.05)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
        optimizers = [optimizer]
        schedulers = [scheduler]
        opt_tag = "adamw"
    else:
        muon_params, adam_params = partition_params(model)
        muon_opt = SingleGPUMuon(muon_params, lr=args.muon_lr, momentum=0.95)
        adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)
        muon_sched = torch.optim.lr_scheduler.CosineAnnealingLR(muon_opt, T_max=args.epochs)
        adam_sched = torch.optim.lr_scheduler.CosineAnnealingLR(adam_opt, T_max=args.epochs)
        optimizers = [muon_opt, adam_opt]
        schedulers = [muon_sched, adam_sched]
        opt_tag = "muon"
        print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)

    # Mixup / CutMix
    mixup_fn = Mixup(
        mixup_alpha=0.8, cutmix_alpha=1.0, cutmix_minmax=None,
        prob=1.0, switch_prob=0.5, mode="batch",
        label_smoothing=0.1, num_classes=100,
    )
    train_criterion = SoftTargetCrossEntropy()
    val_criterion = nn.CrossEntropyLoss()

    train_dl, val_dl = get_dataloaders(args.batch_size)
    n_batches_total = len(train_dl)
    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    print(
        f"model=deit_small_patch16_224, params={param_count:.1f}M, device={device}, "
        f"optimizer={args.optimizer}, augmentation=deit_standard",
        flush=True,
    )

    # Dry-run: one forward+backward step
    if args.dry_run:
        model.train()
        images, labels = next(iter(train_dl))
        images, labels = images.to(device), labels.to(device)
        mixed_images, mixed_labels = mixup_fn(images, labels)
        for opt in optimizers:
            opt.zero_grad()
        loss = train_criterion(model(mixed_images), mixed_labels)
        loss.backward()
        for opt in optimizers:
            opt.step()
        print(f"=== DRY RUN PASSED === loss={loss.item():.4f}", flush=True)
        return

    os.makedirs(args.output_dir, exist_ok=True)
    best_acc = 0.0

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            images, labels = mixup_fn(images, labels)

            for opt in optimizers:
                opt.zero_grad()
            loss = train_criterion(model(images), labels)
            loss.backward()
            for opt in optimizers:
                opt.step()
            running_loss += loss.item()
            n_batches += 1
            if n_batches % 50 == 0:
                elapsed = time.time() - t0
                print(
                    f"  batch {n_batches}/{n_batches_total}, "
                    f"loss={loss.item():.4f}, elapsed={elapsed:.1f}s",
                    flush=True,
                )
        for sched in schedulers:
            sched.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        lr_info = f"lr={schedulers[0].get_last_lr()[0]:.6f}"
        print(
            f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, "
            f"time={epoch_time:.1f}s, {lr_info}",
            flush=True,
        )

        if val_acc > best_acc:
            best_acc = val_acc
            ckpt_name = f"deit_small_{opt_tag}_aug_s{args.seed}.pt"
            ckpt_path = os.path.join(args.output_dir, ckpt_name)
            save_dict = {
                "state_dict": model.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "train_loss": avg_loss,
                "config": {
                    "optimizer": args.optimizer,
                    "augmentation": "deit_standard",
                    "mixup_alpha": 0.8, "cutmix_alpha": 1.0,
                    "label_smoothing": 0.1, "drop_path_rate": 0.1,
                    "rand_augment": "N2_M9", "random_erasing": 0.25,
                },
            }
            if args.optimizer == "adamw":
                save_dict["optimizer_state"] = optimizer.state_dict()
            else:
                save_dict["muon_optimizer_state"] = muon_opt.state_dict()
                save_dict["adam_optimizer_state"] = adam_opt.state_dict()
                save_dict["muon_lr"] = args.muon_lr
            # _DISK_CHECK_SAVE_INJECTED_
            _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space on data disk: {_save_free_gb:.1f}G free", flush=True)
            torch.save(save_dict, ckpt_path)
            print(f"  best checkpoint saved: {ckpt_path}", flush=True)

    print(f"TRAINING_COMPLETE best_val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="DeiT-S + DeiT standard augmentation (AdamW or Muon)"
    )
    parser.add_argument("--optimizer", type=str, default="adamw", choices=["adamw", "muon"])
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--lr", type=float, default=3e-4, help="AdamW learning rate")
    parser.add_argument("--muon-lr", type=float, default=0.003, help="Muon learning rate")
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    parser.add_argument("--dry-run", action="store_true", help="One-step verification, no training")
    args = parser.parse_args()
    # _DISK_CHECK_STARTUP_INJECTED_
    _disk_free_gb = shutil.disk_usage('/').free / (1024**3)
    if _disk_free_gb < 2.0:
        raise RuntimeError(
            f"Disk space critically low: {_disk_free_gb:.1f}G free on /. "
            f"Need >= 2G. Clean up checkpoints or use /root/autodl-tmp/."
        )
    train(args)
