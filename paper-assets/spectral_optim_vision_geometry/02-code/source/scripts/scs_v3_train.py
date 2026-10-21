#!/usr/bin/env python3
"""SCS v3: CIFAR-100 ConvNeXt-T training with Muon/AdamW/SGD.

Key fix from v2: T_max = epochs (cosine schedule resets properly).
"""
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
from muon import muon_update


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
    """ConvNeXt-T: stem/head/norm/bias/1D -> Adam, rest -> Muon."""
    norm_names = _norm_param_names(model)
    muon_params, adam_params = [], []
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        is_adam = (
            name.startswith("head.") or name.startswith("stem.")
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


def get_dataloaders(batch_size, data_dir="/root/spectral_optim_vision_geometry/data"):
    mean, std = (0.5071, 0.4867, 0.4408), (0.2675, 0.2565, 0.2761)
    train_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    val_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    train_ds = datasets.CIFAR100(root=data_dir, train=True, download=True, transform=train_tf)
    val_ds = datasets.CIFAR100(root=data_dir, train=False, download=True, transform=val_tf)
    train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True, drop_last=True)
    val_dl = DataLoader(val_ds, batch_size=batch_size, shuffle=False, num_workers=4, pin_memory=True)
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


def make_optimizers(model, optimizer_name, lr, epochs):
    if optimizer_name == "muon":
        muon_params, adam_params = partition_params(model)
        print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)
        muon_opt = SingleGPUMuon(muon_params, lr=lr, momentum=0.95)
        adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)
        muon_sched = torch.optim.lr_scheduler.CosineAnnealingLR(muon_opt, T_max=epochs)
        adam_sched = torch.optim.lr_scheduler.CosineAnnealingLR(adam_opt, T_max=epochs)
        return [muon_opt, adam_opt], [muon_sched, adam_sched]
    elif optimizer_name == "adamw":
        opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.05)
        sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=epochs)
        return [opt], [sched]
    elif optimizer_name == "sgd":
        opt = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=1e-4)
        sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=epochs)
        return [opt], [sched]
    else:
        raise ValueError(f"Unknown optimizer: {optimizer_name}")


def train(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    model = timm.create_model("convnext_tiny", pretrained=False, num_classes=100).to(device)
    optimizers, schedulers = make_optimizers(model, args.optimizer, args.lr, args.epochs)
    criterion = nn.CrossEntropyLoss()

    train_dl, val_dl = get_dataloaders(args.batch_size)
    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    lr_tag = f"{args.lr}".replace(".", "")
    print(f"model=convnext_tiny, params={param_count:.1f}M, device={device}, "
          f"optimizer={args.optimizer}, lr={args.lr}, epochs={args.epochs}, "
          f"T_max={args.epochs}, batches/epoch={n_batches_total}", flush=True)

    os.makedirs(args.output_dir, exist_ok=True)
    best_acc = 0.0
    best_epoch = 0

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            for opt in optimizers:
                opt.zero_grad()
            loss = criterion(model(images), labels)
            loss.backward()
            for opt in optimizers:
                opt.step()
            running_loss += loss.item()
            n_batches += 1
            if n_batches % 50 == 0:
                elapsed = time.time() - t0
                print(f"  batch {n_batches}/{n_batches_total}, loss={loss.item():.4f}, elapsed={elapsed:.1f}s", flush=True)
        for sched in schedulers:
            sched.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        cur_lrs = [s.get_last_lr()[0] for s in schedulers]
        print(f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, "
              f"time={epoch_time:.1f}s, lr={cur_lrs}", flush=True)

        if val_acc > best_acc:
            best_acc = val_acc
            best_epoch = epoch
            best_path = os.path.join(
                args.output_dir,
                f"convnext_t_{args.optimizer}_lr{lr_tag}_s{args.seed}_tmax{args.epochs}_best.pt"
            )
            torch.save({
                "state_dict": model.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "train_loss": avg_loss,
                "optimizer": args.optimizer,
                "lr": args.lr,
                "T_max": args.epochs,
            }, best_path)
            print(f"  best checkpoint saved: {best_path}", flush=True)

        if epoch == args.epochs:
            final_path = os.path.join(
                args.output_dir,
                f"convnext_t_{args.optimizer}_lr{lr_tag}_s{args.seed}_tmax{args.epochs}_ep{epoch}.pt"
            )
            torch.save({
                "state_dict": model.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "train_loss": avg_loss,
                "optimizer": args.optimizer,
                "lr": args.lr,
                "T_max": args.epochs,
            }, final_path)
            print(f"  final checkpoint saved: {final_path}", flush=True)

    print(f"TRAINING_COMPLETE optimizer={args.optimizer} best_val_acc={best_acc:.2f}% (ep{best_epoch})", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SCS v3: CIFAR-100 ConvNeXt-T training")
    parser.add_argument("--optimizer", type=str, required=True, choices=["muon", "adamw", "sgd"])
    parser.add_argument("--lr", type=float, required=True)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output-dir", type=str, default="/root/spectral_optim_vision_geometry/checkpoints/scs_v3/")
    args = parser.parse_args()
    train(args)
