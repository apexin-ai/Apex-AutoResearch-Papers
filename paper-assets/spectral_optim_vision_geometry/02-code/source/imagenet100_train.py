# Dataset: mini-ImageNet 100-class subset (Vinyals et al., 2016)
# Source: ModelScope tany0699/mini_imagenet100
# 100 classes × 600 train + 100 val per class, 224×224
# Paper citation: Vinyals, O., Blundell, C., Lillicrap, T., Kavukciglu, K., & Wiegand, D. (2016). Matching Networks for One Shot Learning.
# ImageNet-100 (100 classes, 224x224) cross-architecture optimizer comparison
# Adapted from tiny_imagenet_train.py for B6 experiments.
#
# Key differences vs Tiny-ImageNet version:
#   - Data: ImageFolder from /root/autodl-tmp/imagenet100/{train,val} (no auto-download)
#   - Transforms: standard ImageNet recipe (RandomResizedCrop(224), Resize(256)+CenterCrop(224))
#   - Normalization: ImageNet standard mean/std (not Tiny-ImageNet specific values)
#   - num_classes: 100 (not 200)
#
# Models: resnet50, deit_small (timm)
# Optimizers: adamw, sgd, muon (SingleGPUMuon with Newton-Schulz orthogonalization), lion
#
# Usage:
#   python3 imagenet100_train.py --arch resnet50 --optimizer adamw --seed 42 --gpu 0
#   python3 imagenet100_train.py --arch deit_small --optimizer muon --seed 42 --gpu 0
#   python3 imagenet100_train.py --arch resnet50 --optimizer adamw --dry-run  # validate setup
#
# Deps: torch, torchvision, timm, muon (site-package with muon_update)

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
from lion_pytorch import Lion
from gpu_utils import check_gpu_whitelist


# ImageNet standard normalization (differs from Tiny-ImageNet values used in tiny_imagenet_train.py)
IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)

MODEL_REGISTRY = {
    "resnet50": "resnet50",
    "deit_small": "deit_small_patch16_224",
    "convnext_tiny": "convnext_tiny",
}

_HEAD_PREFIXES = {"resnet50": ("fc.",), "deit_small": ("head.",), "convnext_tiny": ("head.",)}
_EMBED_PREFIXES = {
    "resnet50": (),
    "deit_small": ("cls_token", "pos_embed", "dist_token", "patch_embed."),
    "convnext_tiny": ("stem.",),
}


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


# --------------- Data loaders ---------------

def get_dataloaders(data_dir, batch_size, num_workers=4):
    """Load ImageNet-100 from ImageFolder layout.

    Expects data_dir/{train,val}/ with class subdirectories.
    Uses standard ImageNet augmentation (RandomResizedCrop, not Resize+RandomCrop
    as in Tiny-ImageNet where images need upscaling from 64x64).
    """
    train_dir = os.path.join(data_dir, "train")
    val_dir = os.path.join(data_dir, "val")

    if not os.path.isdir(train_dir):
        raise FileNotFoundError(
            f"Train directory not found: {train_dir}\n"
            f"Ensure ImageNet-100 data is prepared at {data_dir}/{{train,val}}/")
    if not os.path.isdir(val_dir):
        raise FileNotFoundError(
            f"Val directory not found: {val_dir}\n"
            f"Ensure ImageNet-100 data is prepared at {data_dir}/{{train,val}}/")

    # Standard ImageNet recipe: RandomResizedCrop for native 224x224 images
    # (Tiny-ImageNet used Resize(224)+RandomCrop because source is 64x64)
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

    train_ds = datasets.ImageFolder(train_dir, transform=train_tf)
    val_ds = datasets.ImageFolder(val_dir, transform=val_tf)

    n_classes = len(train_ds.classes)
    print(f"ImageNet-100 loaded: train={len(train_ds)}, val={len(val_ds)}, classes={n_classes}",
          flush=True)
    if n_classes != 100:
        print(f"WARNING: expected 100 classes but found {n_classes}", flush=True)

    train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True,
                          num_workers=num_workers, pin_memory=True, drop_last=True)
    val_dl = DataLoader(val_ds, batch_size=batch_size, shuffle=False,
                        num_workers=num_workers, pin_memory=True)
    return train_dl, val_dl


# --------------- Muon param partition ---------------

def _norm_param_names(model):
    names = set()
    for mname, mod in model.named_modules():
        if isinstance(mod, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.GroupNorm)):
            for pname, _ in mod.named_parameters():
                names.add(f"{mname}.{pname}" if mname else pname)
    return names


def partition_params(model, arch_name):
    """Split parameters into Muon-eligible (≥2D weight matrices) and AdamW (head/embed/norm/bias)."""
    head_pf = _HEAD_PREFIXES[arch_name]
    embed_pf = _EMBED_PREFIXES[arch_name]
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


# --------------- SingleGPUMuon ---------------

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


# --------------- Evaluate ---------------

@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct, total = 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        correct += (model(images).argmax(1) == labels).sum().item()
        total += labels.size(0)
    return 100.0 * correct / total


# --------------- Train ---------------

def train(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    timm_name = MODEL_REGISTRY[args.arch]
    # ImageNet-100: 100 classes (Tiny-ImageNet uses 200)
    model = timm.create_model(timm_name, pretrained=False, num_classes=100).to(device)

    if args.optimizer == "muon":
        muon_params, adam_params = partition_params(model, args.arch)
        print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)
        muon_opt = SingleGPUMuon(muon_params, lr=args.muon_lr, momentum=0.95, weight_decay=args.weight_decay)
        adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=args.weight_decay)
        muon_sched = torch.optim.lr_scheduler.CosineAnnealingLR(muon_opt, T_max=args.epochs)
        adam_sched = torch.optim.lr_scheduler.CosineAnnealingLR(adam_opt, T_max=args.epochs)
    elif args.optimizer == "adamw":
        lr = args.lr if args.lr is not None else 3e-4
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=args.weight_decay)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    elif args.optimizer == "sgd":
        lr = args.lr if args.lr is not None else 0.1
        optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=1e-4)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    elif args.optimizer == "lion":
        lr = args.lr if args.lr is not None else 1e-4
        optimizer = Lion(model.parameters(), lr=lr, weight_decay=args.weight_decay)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    elif args.optimizer == "soap":
        import os as _os
        _os.environ["TORCHDYNAMO_DISABLE"] = "1"
        from heavyball import SOAP
        lr = args.soap_lr if args.soap_lr is not None else (args.lr if args.lr is not None else 3e-3)
        wd = args.weight_decay
        optimizer = SOAP(model.parameters(), lr=lr, weight_decay=wd)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    elif args.optimizer == "shampoo":
        import os as _os
        _os.environ["TORCHDYNAMO_DISABLE"] = "1"
        from heavyball import KLShampoo
        lr = args.lr if args.lr is not None else 3e-3
        wd = args.weight_decay
        optimizer = KLShampoo(model.parameters(), lr=lr, weight_decay=wd)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    criterion = nn.CrossEntropyLoss(label_smoothing=args.label_smoothing)
    train_dl, val_dl = get_dataloaders(args.data_dir, args.batch_size, args.num_workers)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(f"model={args.arch} ({timm_name}), params={param_count:.1f}M, "
          f"optimizer={args.optimizer}, device={device}, batches/epoch={n_batches_total}", flush=True)

    # --dry-run: validate data loading + model forward/backward on 1 batch, then exit
    if args.dry_run:
        images, labels = next(iter(train_dl))
        images, labels = images.to(device), labels.to(device)
        out = model(images)
        loss = criterion(out, labels)
        loss.backward()
        print(f"DRY_RUN_OK: batch_shape={list(images.shape)}, loss={loss.item():.4f}, "
              f"output_shape={list(out.shape)}", flush=True)
        return

    best_acc = 0.0
    ckpt_name = f"imagenet100_{args.arch}_{args.optimizer}_s{args.seed}.pt"
    os.makedirs(args.output_dir, exist_ok=True)

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()

        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)

            if args.optimizer == "muon":
                muon_opt.zero_grad()
                adam_opt.zero_grad()
            else:
                optimizer.zero_grad()

            loss = criterion(model(images), labels)
            loss.backward()

            if args.optimizer == "muon":
                muon_opt.step()
                adam_opt.step()
            else:
                optimizer.step()

            running_loss += loss.item()
            n_batches += 1

            if n_batches % 50 == 0:
                elapsed = time.time() - t0
                print(f"  batch {n_batches}/{n_batches_total}, loss={loss.item():.4f}, "
                      f"elapsed={elapsed:.1f}s", flush=True)

        if args.optimizer == "muon":
            muon_sched.step()
            adam_sched.step()
        else:
            scheduler.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, "
              f"time={epoch_time:.1f}s", flush=True)

        if val_acc > best_acc:
            best_acc = val_acc
            save_dict = {
                "state_dict": model.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "model": args.arch,
                "optimizer": args.optimizer,
            }
            if args.optimizer == "muon":
                save_dict["muon_optimizer_state"] = muon_opt.state_dict()
                save_dict["adam_optimizer_state"] = adam_opt.state_dict()
            else:
                save_dict["optimizer_state"] = optimizer.state_dict()
            _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space on data disk: {_save_free_gb:.1f}G free", flush=True)
            torch.save(save_dict, os.path.join(args.output_dir, ckpt_name))

    print(f"TRAINING_COMPLETE val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ImageNet-100 cross-architecture optimizer comparison (B6)")
    parser.add_argument("--arch", type=str, default="resnet50",
                        choices=list(MODEL_REGISTRY.keys()),
                        help="Model architecture")
    parser.add_argument("--optimizer", type=str, default="adamw",
                        choices=["adamw", "sgd", "muon", "lion", "soap", "shampoo"])
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--num-workers", type=int, default=4)
    parser.add_argument("--muon-lr", type=float, default=0.02)
    parser.add_argument("--lr", type=float, default=None,
                        help="Override default lr for adamw/sgd")
    parser.add_argument("--weight-decay", type=float, default=0.01,
                        help="Weight decay (default: 0.01)")
    parser.add_argument("--soap-lr", type=float, default=None,
                        help="SOAP learning rate (overrides --lr when optimizer=soap)")
    parser.add_argument("--data-dir", type=str,
                        default="/root/autodl-tmp/imagenet100_deduped",
                        help="ImageNet-100 root with train/ and val/ subdirs")
    parser.add_argument("--output-dir", type=str,
                        default="/root/autodl-tmp/checkpoints/spectral_optim/")
    parser.add_argument("--label-smoothing", type=float, default=0.0,
                        help="Label smoothing factor (default: 0.0)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run 1 batch to validate setup, then exit")
    args = parser.parse_args()
    check_gpu_whitelist(args.gpu)

    _disk_free_gb = shutil.disk_usage('/').free / (1024**3)
    if _disk_free_gb < 2.0:
        raise RuntimeError(
            f"Disk space critically low: {_disk_free_gb:.1f}G free on /. "
            f"Need >= 2G. Clean up checkpoints or use /root/autodl-tmp/."
        )
    train(args)
