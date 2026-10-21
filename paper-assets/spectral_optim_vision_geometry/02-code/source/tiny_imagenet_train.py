# Tiny-ImageNet (200 classes, 64x64) cross-architecture optimizer comparison
# Models: resnet50, deit_small (timm)
# Optimizers: adamw, sgd, muon, soap (SOAP from heavyball), shampoo (KLShampoo from heavyball)
#
# Usage:
#   python3 tiny_imagenet_train.py --model resnet50 --optimizer adamw --seed 42 --gpu 0
#   python3 tiny_imagenet_train.py --model deit_small --optimizer muon --seed 42 --gpu 0
#
# Data: loads from local HuggingFace dataset directory (parquet format).
#
# Deps: torch, torchvision, timm, muon (site-package with muon_update), datasets

# checkpoint path migrated to /root/autodl-tmp (root partition is ~30G; checkpoints filled it).
import os
os.environ.setdefault("PYTHONUNBUFFERED", "1")

import argparse
import random
import shutil
import sys
import time
from gpu_utils import check_gpu_whitelist

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
import timm
from muon import muon_update
from heavyball import SOAP, KLShampoo


TINYIMAGENET_DIR = "/root/autodl-tmp/data/tiny-imagenet-200"

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


# --------------- Data loaders (HuggingFace parquet) ---------------

IMAGENET_MEAN = (0.4802, 0.4481, 0.3975)
IMAGENET_STD = (0.2770, 0.2691, 0.2821)


class HFImageDataset(Dataset):
    """Wraps a HuggingFace dataset split for use with PyTorch DataLoader."""

    def __init__(self, hf_dataset, transform=None):
        self.dataset = hf_dataset
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        item = self.dataset[idx]
        image = item["image"].convert("RGB")
        label = item["label"]
        if self.transform:
            image = self.transform(image)
        return image, label


def get_dataloaders(batch_size, data_dir):
    if not os.path.isdir(data_dir):
        print(f"ERROR: Data directory not found: {data_dir}", flush=True)
        print("Please ensure TinyImageNet HuggingFace dataset is available at this path.", flush=True)
        sys.exit(1)

    from datasets import load_dataset
    ds = load_dataset(data_dir)

    train_tf = transforms.Compose([
        transforms.Resize(224),
        transforms.RandomCrop(224, padding=16),
        transforms.RandomHorizontalFlip(),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])
    val_tf = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])

    train_dataset = HFImageDataset(ds["train"], transform=train_tf)
    val_dataset = HFImageDataset(ds["valid"], transform=val_tf)

    train_dl = DataLoader(train_dataset, batch_size=batch_size, shuffle=True,
                          num_workers=4, pin_memory=True, drop_last=True)
    val_dl = DataLoader(val_dataset, batch_size=batch_size, shuffle=False,
                        num_workers=4, pin_memory=True)
    return train_dl, val_dl


# --------------- Training logic ---------------

def evaluate(model, val_dl, device):
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for images, labels in val_dl:
            images, labels = images.to(device), labels.to(device)
            preds = model(images).argmax(dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    return 100.0 * correct / total


def build_model(model_key, num_classes=200):
    timm_name = MODEL_REGISTRY[model_key]
    model = timm.create_model(timm_name, pretrained=False, num_classes=num_classes)
    return model


def train(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    print(f"device={device}, model={args.model}, optimizer={args.optimizer}, seed={args.seed}",
          flush=True)

    model = build_model(args.model).to(device)
    train_dl, val_dl = get_dataloaders(args.batch_size, args.data_dir)
    n_batches_total = len(train_dl)
    print(f"train_batches={n_batches_total}, train_samples={len(train_dl.dataset)}, "
          f"val_samples={len(val_dl.dataset)}", flush=True)

    criterion = nn.CrossEntropyLoss()

    # ----- optimizer setup -----
    head_prefixes = _HEAD_PREFIXES[args.model]
    embed_prefixes = _EMBED_PREFIXES[args.model]

    head_params = []
    embed_params = []
    body_params = []
    for name, p in model.named_parameters():
        if any(name.startswith(pfx) for pfx in head_prefixes):
            head_params.append(p)
        elif any(name.startswith(pfx) for pfx in embed_prefixes):
            embed_params.append(p)
        else:
            body_params.append(p)

    if args.optimizer == "muon":
        muon_params = [p for p in body_params if p.ndim >= 2]
        adam_params = [p for p in body_params if p.ndim < 2] + head_params + embed_params
        muon_opt = torch.optim.SGD(muon_params, lr=args.muon_lr, momentum=0.95)
        adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.01)
        muon_sched = torch.optim.lr_scheduler.CosineAnnealingLR(muon_opt, T_max=args.epochs)
        adam_sched = torch.optim.lr_scheduler.CosineAnnealingLR(adam_opt, T_max=args.epochs)
    elif args.optimizer == "adamw":
        lr = args.lr if args.lr else 1e-3
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.01)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    elif args.optimizer == "sgd":
        lr = args.lr if args.lr else 0.1
        optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=1e-4)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    elif args.optimizer == "soap":
        lr = args.lr if args.lr else 1e-3
        optimizer = SOAP(model.parameters(), lr=lr, weight_decay=0.01)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    elif args.optimizer == "shampoo":
        lr = args.lr if args.lr else 1e-3
        optimizer = KLShampoo(model.parameters(), lr=lr, weight_decay=0.01)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    else:
        raise ValueError(f"Unknown optimizer: {args.optimizer}")

    best_acc = 0.0
    ckpt_name = f"{args.model}_{args.optimizer}_s{args.seed}.pt"
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
                        choices=["adamw", "sgd", "muon", "soap", "shampoo"])
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--muon-lr", type=float, default=0.02)
    parser.add_argument("--lr", type=float, default=None,
                        help="Override default lr for adamw/sgd")
    parser.add_argument("--data-dir", type=str, default=TINYIMAGENET_DIR,
                        help="HuggingFace dataset directory for TinyImageNet")
    parser.add_argument("--output-dir", type=str,
                        default="/root/autodl-tmp/checkpoints/spectral_optim/")
    args = parser.parse_args()
    check_gpu_whitelist(args.gpu)
    # _DISK_CHECK_STARTUP_INJECTED_
    _disk_free_gb = shutil.disk_usage('/').free / (1024**3)
    if _disk_free_gb < 2.0:
        raise RuntimeError(
            f"Disk space critically low: {_disk_free_gb:.1f}G free on /. "
            f"Need >= 2G. Clean up checkpoints or use /root/autodl-tmp/."
        )
    train(args)
