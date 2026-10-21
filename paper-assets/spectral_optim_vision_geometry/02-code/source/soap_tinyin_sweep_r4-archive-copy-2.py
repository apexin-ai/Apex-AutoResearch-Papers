# Tiny-ImageNet (200 classes, 64x64) cross-architecture optimizer comparison
# Models: resnet50, deit_small (timm)
# Optimizers: adamw, sgd, muon (SingleGPUMuon with Newton-Schulz orthogonalization)
#
# Usage:
#   python3 tiny_imagenet_train.py --model resnet50 --optimizer adamw --seed 42 --gpu 0
#   python3 tiny_imagenet_train.py --model deit_small --optimizer muon --seed 42 --gpu 0
#
# Data: auto-downloads Tiny-ImageNet to data/tiny-imagenet-200/ if missing.
#       Val directory is reorganized into ImageFolder-compatible layout on first run.
#
# Deps: torch, torchvision, timm, muon (site-package with muon_update)

# checkpoint path migrated to /root/autodl-tmp (root partition is ~30G; checkpoints filled it).
import argparse
import os
import random
import shutil
import time
import urllib.request
from gpu_utils import check_gpu_whitelist

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm
from muon import muon_update
from heavyball import SOAP as SoapOptimizer


DATA_ROOT = "/root/spectral_optim_vision_geometry/data"
TINYIMAGENET_DIR = os.path.join(DATA_ROOT, "tiny-imagenet-200")
TINYIMAGENET_URL = "http://cs231n.stanford.edu/tiny-imagenet-200.zip"

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


# --------------- Tiny-ImageNet download & val restructure ---------------

def download_tiny_imagenet():
    if os.path.isdir(TINYIMAGENET_DIR) and os.path.isdir(os.path.join(TINYIMAGENET_DIR, "train")):
        print(f"Tiny-ImageNet already exists at {TINYIMAGENET_DIR}")
        return
    os.makedirs(DATA_ROOT, exist_ok=True)
    zip_path = os.path.join(DATA_ROOT, "tiny-imagenet-200.zip")
    if not os.path.exists(zip_path):
        print(f"Downloading Tiny-ImageNet from {TINYIMAGENET_URL} ...")
        urllib.request.urlretrieve(TINYIMAGENET_URL, zip_path)
        print("Download complete.")
    print("Extracting ...")
    import zipfile
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(DATA_ROOT)
    print("Extraction complete.")


def restructure_val_dir():
    """Reorganize val/ into class subdirectories for ImageFolder compatibility."""
    val_dir = os.path.join(TINYIMAGENET_DIR, "val")
    val_img_dir = os.path.join(val_dir, "images")
    val_ann_file = os.path.join(val_dir, "val_annotations.txt")
    if not os.path.isdir(val_img_dir):
        return
    if not os.path.isfile(val_ann_file):
        return

    print("Restructuring val directory for ImageFolder ...")
    with open(val_ann_file, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            img_name, class_id = parts[0], parts[1]
            class_dir = os.path.join(val_dir, class_id)
            os.makedirs(class_dir, exist_ok=True)
            src = os.path.join(val_img_dir, img_name)
            dst = os.path.join(class_dir, img_name)
            if os.path.exists(src):
                shutil.move(src, dst)

    if os.path.isdir(val_img_dir) and len(os.listdir(val_img_dir)) == 0:
        os.rmdir(val_img_dir)
    print("Val directory restructured.")


# --------------- Data loaders ---------------

IMAGENET_MEAN = (0.4802, 0.4481, 0.3975)
IMAGENET_STD = (0.2770, 0.2691, 0.2821)


def get_dataloaders(batch_size):
    download_tiny_imagenet()
    restructure_val_dir()

    train_tf = transforms.Compose([
        transforms.Resize(224),
        transforms.RandomCrop(224, padding=8),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])
    val_tf = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])

    train_ds = datasets.ImageFolder(os.path.join(TINYIMAGENET_DIR, "train"), transform=train_tf)
    val_ds = datasets.ImageFolder(os.path.join(TINYIMAGENET_DIR, "val"), transform=val_tf)
    train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True,
                          num_workers=4, pin_memory=True, drop_last=True)
    val_dl = DataLoader(val_ds, batch_size=batch_size, shuffle=False,
                        num_workers=4, pin_memory=True)
    return train_dl, val_dl


# --------------- Muon param partition ---------------

def _norm_param_names(model):
    names = set()
    for mname, mod in model.named_modules():
        if isinstance(mod, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.GroupNorm)):
            for pname, _ in mod.named_parameters():
                names.add(f"{mname}.{pname}" if mname else pname)
    return names


def partition_params(model, model_name):
    head_pf = _HEAD_PREFIXES[model_name]
    embed_pf = _EMBED_PREFIXES[model_name]
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

    timm_name = MODEL_REGISTRY[args.model]
    model = timm.create_model(timm_name, pretrained=False, num_classes=200).to(device)

    if args.optimizer == "muon":
        muon_params, adam_params = partition_params(model, args.model)
        print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)
        muon_opt = SingleGPUMuon(muon_params, lr=args.muon_lr, momentum=0.95)
        adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)
        muon_sched = torch.optim.lr_scheduler.CosineAnnealingLR(muon_opt, T_max=args.epochs)
        adam_sched = torch.optim.lr_scheduler.CosineAnnealingLR(adam_opt, T_max=args.epochs)
    elif args.optimizer == "adamw":
        lr = args.lr if args.lr is not None else 3e-4
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.05)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    elif args.optimizer == "soap":
        optimizer = SoapOptimizer(model.parameters(), lr=args.lr, weight_decay=0.01)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    elif args.optimizer == "sgd":
        lr = args.lr if args.lr is not None else 0.1
        optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=1e-4)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    criterion = nn.CrossEntropyLoss()
    train_dl, val_dl = get_dataloaders(args.batch_size)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(f"model={args.model} ({timm_name}), params={param_count:.1f}M, "
          f"optimizer={args.optimizer}, device={device}, batches/epoch={n_batches_total}", flush=True)

    best_acc = 0.0
    ckpt_name = f"tinyimagenet_{args.model}_{args.optimizer}_s{args.seed}.pt"
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
                "model": args.model,
                "optimizer": args.optimizer,
            }
            if args.optimizer == "muon":
                save_dict["muon_optimizer_state"] = muon_opt.state_dict()
                save_dict["adam_optimizer_state"] = adam_opt.state_dict()
            else:
                save_dict["optimizer_state"] = optimizer.state_dict()
            # _DISK_CHECK_SAVE_INJECTED_
            _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space on data disk: {_save_free_gb:.1f}G free", flush=True)
            torch.save(save_dict, os.path.join(args.output_dir, ckpt_name))

    print(f"TRAINING_COMPLETE val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tiny-ImageNet cross-architecture optimizer comparison")
    parser.add_argument("--model", type=str, default="resnet50",
                        choices=list(MODEL_REGISTRY.keys()))
    parser.add_argument("--optimizer", type=str, default="adamw",
                        choices=["adamw", "sgd", "muon", "soap"])
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--muon-lr", type=float, default=0.02)
    parser.add_argument("--lr", type=float, default=None,
                        help="Override default lr for adamw/sgd")
    parser.add_argument("--data-dir", type=str, default=None,
                        help="Override Tiny-ImageNet data directory")
    parser.add_argument("--output-dir", type=str,
                        default="/root/autodl-tmp/checkpoints/spectral_optim/")
    args = parser.parse_args()
    check_gpu_whitelist(args.gpu)
    if args.data_dir:
        TINYIMAGENET_DIR = args.data_dir
        DATA_ROOT = os.path.dirname(args.data_dir)
    # _DISK_CHECK_STARTUP_INJECTED_
    _disk_free_gb = shutil.disk_usage('/').free / (1024**3)
    if _disk_free_gb < 2.0:
        raise RuntimeError(
            f"Disk space critically low: {_disk_free_gb:.1f}G free on /. "
            f"Need >= 2G. Clean up checkpoints or use /root/autodl-tmp/."
        )
    train(args)
