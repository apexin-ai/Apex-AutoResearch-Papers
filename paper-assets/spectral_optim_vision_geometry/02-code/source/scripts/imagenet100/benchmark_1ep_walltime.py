"""1-epoch wall-time benchmark on ImageNet-100.

Measures training throughput (images/sec) and wall time for 1 train + 1 val epoch.
Supports ResNet-50, DeiT-S with Muon, AdamW, or SGD optimizer.

Usage:
    python benchmark_1ep_walltime.py --arch resnet50 --optimizer muon --data-dir /root/autodl-tmp/imagenet100 --gpu 0
    python benchmark_1ep_walltime.py --arch deit_small --optimizer adamw --data-dir /root/autodl-tmp/imagenet100 --gpu 0
    python benchmark_1ep_walltime.py --help
"""
import argparse
import os
import sys
import time

sys.path.insert(0, "/root/spectral_optim_vision_geometry")

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm

from muon import muon_update

IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)

MODEL_REGISTRY = {
    "resnet50": "resnet50",
    "deit_small": "deit_small_patch16_224",
}


class SingleGPUMuon(torch.optim.Optimizer):
    def __init__(self, params, lr=0.02, momentum=0.95, weight_decay=0):
        defaults = dict(lr=lr, momentum=momentum, weight_decay=weight_decay)
        super().__init__(params, defaults)

    @torch.no_grad()
    def step(self, closure=None):
        for group in self.param_groups:
            for p in group["params"]:
                if p.grad is None:
                    continue
                state = self.state[p]
                if len(state) == 0:
                    state["momentum_buffer"] = torch.zeros_like(p)
                update = muon_update(p.grad, state["momentum_buffer"], beta=group["momentum"])
                p.mul_(1 - group["lr"] * group["weight_decay"])
                p.add_(update.reshape(p.shape), alpha=-group["lr"])


def _norm_param_names(model):
    names = set()
    for mname, mod in model.named_modules():
        if isinstance(mod, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.GroupNorm)):
            for pname, _ in mod.named_parameters():
                names.add(f"{mname}.{pname}" if mname else pname)
    return names


HEAD_PREFIXES = {"resnet50": ("fc.",), "deit_small": ("head.",)}
EMBED_PREFIXES = {
    "resnet50": (),
    "deit_small": ("cls_token", "pos_embed", "dist_token", "patch_embed."),
}


def partition_params(model, arch):
    head_pf = HEAD_PREFIXES[arch]
    embed_pf = EMBED_PREFIXES[arch]
    norm_names = _norm_param_names(model)
    muon_params, adam_params = [], []
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        is_adam = (
            any(name.startswith(p) for p in head_pf)
            or any(name.startswith(p) or name == p.rstrip(".") for p in embed_pf)
            or name in norm_names
            or name.endswith(".bias")
            or param.ndim < 2
        )
        (adam_params if is_adam else muon_params).append(param)
    return muon_params, adam_params


def build_dataloaders(data_dir, batch_size, num_workers):
    train_tf = transforms.Compose([
        transforms.RandomResizedCrop(224),
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

    train_dir = os.path.join(data_dir, "train")
    val_dir = os.path.join(data_dir, "val")

    has_train = os.path.isdir(train_dir)
    has_val = os.path.isdir(val_dir)

    train_dl, val_dl = None, None
    if has_train:
        train_ds = datasets.ImageFolder(train_dir, transform=train_tf)
        train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True,
                              num_workers=num_workers, pin_memory=True, drop_last=True)
        print(f"Train: {len(train_ds)} images, {len(train_ds.classes)} classes, {len(train_dl)} batches")
    else:
        print(f"WARN: {train_dir} not found — skipping train epoch")

    if has_val:
        val_ds = datasets.ImageFolder(val_dir, transform=val_tf)
        val_dl = DataLoader(val_ds, batch_size=batch_size, shuffle=False,
                            num_workers=num_workers, pin_memory=True)
        print(f"Val:   {len(val_ds)} images, {len(val_ds.classes)} classes, {len(val_dl)} batches")
    else:
        print(f"WARN: {val_dir} not found — skipping val epoch")

    return train_dl, val_dl


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct, total = 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        preds = model(images).argmax(dim=1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)
    return 100.0 * correct / total if total > 0 else 0.0


def main():
    parser = argparse.ArgumentParser(description="1-epoch ImageNet-100 wall-time benchmark")
    parser.add_argument("--arch", type=str, default="resnet50", choices=list(MODEL_REGISTRY.keys()))
    parser.add_argument("--optimizer", type=str, default="muon", choices=["muon", "adamw", "sgd"])
    parser.add_argument("--data-dir", type=str, default="/root/autodl-tmp/imagenet100_deduped")
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--num-workers", type=int, default=8)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--lr", type=float, default=None,
                        help="Learning rate (default: 0.02 for muon, 1e-3 for adamw)")
    parser.add_argument("--compile", action="store_true", help="torch.compile the model")
    parser.add_argument("--amp", action="store_true", help="Use AMP (bf16)")
    args = parser.parse_args()

    if args.lr is None:
        args.lr = {"muon": 0.02, "adamw": 1e-3, "sgd": 0.1}[args.optimizer]

    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    num_classes = 100

    timm_name = MODEL_REGISTRY[args.arch]
    model = timm.create_model(timm_name, pretrained=False, num_classes=num_classes).to(device)
    param_count = sum(p.numel() for p in model.parameters()) / 1e6

    if args.compile and hasattr(torch, "compile"):
        model = torch.compile(model)
        print("torch.compile enabled")

    if args.optimizer == "muon":
        muon_params, adam_params = partition_params(model, args.arch)
        optimizer = SingleGPUMuon(muon_params, lr=args.lr, momentum=0.95)
        aux_optimizer = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)
        print(f"Muon: {len(muon_params)} params, AdamW aux: {len(adam_params)} params")
    elif args.optimizer == "adamw":
        optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.05)
        aux_optimizer = None
        print(f"AdamW: lr={args.lr}")
    else:
        optimizer = torch.optim.SGD(model.parameters(), lr=args.lr, momentum=0.9, weight_decay=1e-4)
        aux_optimizer = None
        print(f"SGD: lr={args.lr}")

    criterion = nn.CrossEntropyLoss()
    scaler = torch.amp.GradScaler("cuda", enabled=args.amp)
    train_dl, val_dl = build_dataloaders(args.data_dir, args.batch_size, args.num_workers)

    print(f"\n{'='*60}")
    print(f"Benchmark: {args.arch} ({timm_name}), {param_count:.1f}M params")
    print(f"Optimizer: {args.optimizer}, lr={args.lr}")
    print(f"Device: {device}, AMP: {args.amp}, Compile: {args.compile}")
    print(f"Batch size: {args.batch_size}, Workers: {args.num_workers}")
    print(f"{'='*60}\n")

    # --- Train 1 epoch ---
    if train_dl is not None:
        model.train()
        torch.cuda.synchronize()
        t_train_start = time.perf_counter()
        total_images = 0
        running_loss = 0.0
        n_batches = len(train_dl)

        for i, (images, labels) in enumerate(train_dl):
            images, labels = images.to(device, non_blocking=True), labels.to(device, non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            if aux_optimizer:
                aux_optimizer.zero_grad(set_to_none=True)

            with torch.amp.autocast("cuda", enabled=args.amp):
                loss = criterion(model(images), labels)

            scaler.scale(loss).backward()
            scaler.step(optimizer)
            if aux_optimizer:
                scaler.step(aux_optimizer)
            scaler.update()

            total_images += images.size(0)
            running_loss += loss.item()

            if (i + 1) % max(1, n_batches // 5) == 0:
                elapsed = time.perf_counter() - t_train_start
                print(f"  [{i+1}/{n_batches}] loss={loss.item():.4f} "
                      f"throughput={total_images/elapsed:.0f} img/s elapsed={elapsed:.1f}s")

        torch.cuda.synchronize()
        t_train_end = time.perf_counter()
        train_wall = t_train_end - t_train_start
        train_throughput = total_images / train_wall
        train_loss = running_loss / n_batches
        print(f"\nTRAIN: wall_time={train_wall:.2f}s, throughput={train_throughput:.0f} img/s, "
              f"loss={train_loss:.4f}, images={total_images}")
    else:
        train_wall, train_throughput, train_loss = 0, 0, 0
        print("TRAIN: skipped (no train data)")

    # --- Val 1 epoch ---
    if val_dl is not None:
        torch.cuda.synchronize()
        t_val_start = time.perf_counter()
        val_acc = evaluate(model, val_dl, device)
        torch.cuda.synchronize()
        t_val_end = time.perf_counter()
        val_wall = t_val_end - t_val_start
        val_images = len(val_dl.dataset)
        val_throughput = val_images / val_wall
        print(f"VAL:   wall_time={val_wall:.2f}s, throughput={val_throughput:.0f} img/s, "
              f"acc={val_acc:.2f}%, images={val_images}")
    else:
        val_wall, val_throughput, val_acc = 0, 0, 0
        print("VAL: skipped (no val data)")

    # --- Summary ---
    total_wall = train_wall + val_wall
    print(f"\n{'='*60}")
    print(f"SUMMARY: {args.arch} + {args.optimizer}")
    print(f"  Train:      {train_wall:.2f}s  ({train_throughput:.0f} img/s)")
    print(f"  Val:        {val_wall:.2f}s  ({val_throughput:.0f} img/s)")
    print(f"  Total:      {total_wall:.2f}s")
    print(f"  Train loss: {train_loss:.4f}")
    print(f"  Val acc:    {val_acc:.2f}%")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
