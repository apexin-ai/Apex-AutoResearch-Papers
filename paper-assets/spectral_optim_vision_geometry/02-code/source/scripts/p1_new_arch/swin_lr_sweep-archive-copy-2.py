#!/usr/bin/env python3
"""Swin-T lr sweep: 5 lr points x 5 epochs on CIFAR-100.
Supports --optimizer adamw|muon. No checkpoint saving.
Usage:
  python swin_lr_sweep.py --optimizer muon --gpu 0 --seed 42
  python swin_lr_sweep.py --optimizer adamw --gpu 0 --seed 42
Deps: torch, torchvision, timm
"""
import argparse
import os
import sys
import time

sys.path.insert(0, "/root/spectral_optim_vision_geometry")

import torch
import torch.nn as nn
import timm
from muon import muon_update
from muon_train import SingleGPUMuon, set_seed, get_dataloaders, evaluate
import shutil

os.environ.setdefault("TMPDIR", "/root/autodl-tmp/tmp")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)



def check_disk_space(path='/', min_gb=2.0):
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')


LR_POINTS = [0.001, 0.003, 0.006, 0.02, 0.06]


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
            name.startswith("head.") or name.startswith("patch_embed.")
            or name in norm_names
            or name.endswith(".bias")
            or param.ndim < 2
            or "relative_position_bias_table" in name
        )
        (adam_params if is_adam else muon_params).append(param)
    return muon_params, adam_params


def train_one_lr(lr, optimizer_name, epochs, batch_size, device, seed):
    set_seed(seed)
    model = timm.create_model("swin_tiny_patch4_window7_224", pretrained=False, num_classes=100).to(device)
    criterion = nn.CrossEntropyLoss()
    train_dl, val_dl = get_dataloaders(batch_size)

    if optimizer_name == "muon":
        muon_params, adam_params = partition_params(model)
        muon_opt = SingleGPUMuon(muon_params, lr=lr, momentum=0.95)
        adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)
        muon_sched = torch.optim.lr_scheduler.CosineAnnealingLR(muon_opt, T_max=epochs)
        adam_sched = torch.optim.lr_scheduler.CosineAnnealingLR(adam_opt, T_max=epochs)
    else:
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.05)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)

    val_accs, train_losses = [], []
    for epoch in range(1, epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            if optimizer_name == "muon":
                muon_opt.zero_grad()
                adam_opt.zero_grad()
            else:
                optimizer.zero_grad()
            loss = criterion(model(images), labels)
            loss.backward()
            if optimizer_name == "muon":
                muon_opt.step()
                adam_opt.step()
            else:
                optimizer.step()
            running_loss += loss.item()
            n_batches += 1
        if optimizer_name == "muon":
            muon_sched.step()
            adam_sched.step()
        else:
            scheduler.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        val_accs.append(val_acc)
        train_losses.append(avg_loss)
        print(f"  ep{epoch}: train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, time={time.time()-t0:.1f}s", flush=True)

    return val_accs, train_losses


def main():
    parser = argparse.ArgumentParser(description="Swin-T lr sweep on CIFAR-100")
    parser.add_argument("--optimizer", type=str, default="muon", choices=["adamw", "muon"])
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch-size", type=int, default=128)
    args = parser.parse_args()

    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    print(f"Swin-T lr sweep: optimizer={args.optimizer}, device={device}, seed={args.seed}, epochs={args.epochs}", flush=True)
    check_disk_space('/')
    check_disk_space('/root/autodl-tmp', min_gb=5.0)

    results = {}
    for lr in LR_POINTS:
        print(f"\n{'='*60}")
        print(f"lr={lr}, optimizer={args.optimizer}")
        print(f"{'='*60}", flush=True)
        val_accs, train_losses = train_one_lr(lr, args.optimizer, args.epochs, args.batch_size, device, args.seed)
        results[str(lr)] = {
            "val_accs": val_accs,
            "train_losses": train_losses,
            "best_val_acc": max(val_accs),
            "final_val_acc": val_accs[-1],
        }

    print(f"\n{'='*60}")
    print(f"LR SWEEP RESULTS (Swin-T {args.optimizer}, {args.epochs} epochs)")
    print(f"{'='*60}")
    print(f"{'LR':<10} {'Best Val%':<12} {'Final Val%':<12} {'Epoch Accs'}")
    print(f"{'-'*60}")
    for lr_str, r in results.items():
        accs_str = " -> ".join(f"{a:.1f}" for a in r["val_accs"])
        print(f"{lr_str:<10} {r['best_val_acc']:<12.2f} {r['final_val_acc']:<12.2f} {accs_str}")

    best_lr = max(results, key=lambda k: results[k]["best_val_acc"])
    print(f"\nBest lr: {best_lr} (val_acc={results[best_lr]['best_val_acc']:.2f}%)")
    print("SWEEP_COMPLETE")


if __name__ == "__main__":
    main()
