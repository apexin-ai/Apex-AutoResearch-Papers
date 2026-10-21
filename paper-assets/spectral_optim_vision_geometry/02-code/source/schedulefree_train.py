# Schedule-Free AdamW trainer for spectral_optim_vision_geometry
# Based on baseline_train.py, replaces optimizer with schedulefree.AdamWScheduleFree
# Usage: python schedulefree_train.py --model resnet50 --epochs 20 --gpu 0 --seed 42
import argparse
import time
import os
os.environ["TORCHDYNAMO_DISABLE"] = "1"
import shutil
import sys
import random

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import RandAugment
import timm
from timm.data import Mixup
from timm.loss import SoftTargetCrossEntropy
from schedulefree import AdamWScheduleFree
from gpu_utils import check_gpu_whitelist

os.environ.setdefault("TMPDIR", "/tmp")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_ROOT = os.path.join(_SCRIPT_DIR, "data")
if os.path.islink(DATA_ROOT) and not os.path.exists(DATA_ROOT):
    os.remove(DATA_ROOT)
os.makedirs(DATA_ROOT, exist_ok=True)


def check_disk_space(path='/', min_gb=2.0):
    os.makedirs(path, exist_ok=True)
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')


def format_lr(lr):
    s = f"{lr:.0e}"
    base, exp = s.split('e')
    return f"{base}e{int(exp)}"


MODEL_REGISTRY = {
    "convnext_tiny": "convnext_tiny",
    "resnet50": "resnet50",
    "resnet50_ln": "resnet50",
    "deit_small": "deit_small_patch16_224",
}


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def replace_bn_with_gn(module, num_groups=1):
    for name, child in module.named_children():
        if isinstance(child, nn.BatchNorm2d):
            setattr(module, name, nn.GroupNorm(num_groups, child.num_features))
        else:
            replace_bn_with_gn(child, num_groups)


def get_dataloaders(batch_size, enhanced=False):
    mean, std = (0.5071, 0.4867, 0.4408), (0.2675, 0.2565, 0.2761)
    train_transforms = [
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
    ]
    if enhanced:
        train_transforms.append(RandAugment(num_ops=2, magnitude=9))
    train_transforms.extend([
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    train_tf = transforms.Compose(train_transforms)
    val_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    train_ds = datasets.CIFAR100(root=DATA_ROOT, train=True, download=True, transform=train_tf)
    val_ds = datasets.CIFAR100(root=DATA_ROOT, train=False, download=True, transform=val_tf)
    train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True,
                          num_workers=4, pin_memory=True, drop_last=True)
    val_dl = DataLoader(val_ds, batch_size=batch_size, shuffle=False,
                        num_workers=4, pin_memory=True)
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
    os.makedirs(args.output_dir, exist_ok=True)
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    num_classes = 100
    timm_name = MODEL_REGISTRY[args.model]
    model = timm.create_model(timm_name, pretrained=False, num_classes=num_classes)
    norm_type = getattr(args, 'norm_type', 'default')
    if args.model == "resnet50_ln" or norm_type == 'ln':
        replace_bn_with_gn(model, num_groups=1)
    elif norm_type == 'gn32':
        replace_bn_with_gn(model, num_groups=32)
    model = model.to(device)

    train_dl, val_dl = get_dataloaders(args.batch_size, enhanced=args.enhanced)

    # Warmup: 5 epochs worth of steps
    steps_per_epoch = len(train_dl)
    warmup_steps = 5 * steps_per_epoch

    lr = args.lr if args.lr is not None else 1e-3
    wd = args.weight_decay if args.weight_decay is not None else 0.01
    optimizer = AdamWScheduleFree(model.parameters(), lr=lr, weight_decay=wd, warmup_steps=warmup_steps)

    # Criterion and Mixup
    if args.enhanced:
        mixup_fn = Mixup(
            mixup_alpha=0.2,
            cutmix_alpha=1.0,
            prob=1.0,
            switch_prob=0.5,
            mode='batch',
            label_smoothing=0.1,
            num_classes=num_classes,
        )
        train_criterion = SoftTargetCrossEntropy()
    else:
        mixup_fn = None
        train_criterion = nn.CrossEntropyLoss()

    lr_str = format_lr(lr)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    enhanced_str = " [ENHANCED]" if args.enhanced else ""
    print(f"model={args.model} ({timm_name}), params={param_count:.1f}M, optimizer=schedulefree_adamw, lr={lr}, wd={wd}, warmup_steps={warmup_steps}, device={device}{enhanced_str}")

    best_acc = 0.0
    norm_suffix = "" if getattr(args, 'norm_type', 'default') == "default" else f"_{args.norm_type}"
    ckpt_name = f"{args.model}{norm_suffix}_schedulefree_s{args.seed}_lr{lr_str}_best.pt"
    save_epochs = set(range(5, args.epochs + 1, 5)) | {1, args.epochs}

    for epoch in range(1, args.epochs + 1):
        model.train()
        optimizer.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            if mixup_fn is not None:
                images, labels = mixup_fn(images, labels)
            optimizer.zero_grad()
            loss = train_criterion(model(images), labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            n_batches += 1

        # Switch to eval mode for validation
        optimizer.eval()
        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, time={epoch_time:.1f}s")

        if val_acc > best_acc:
            best_acc = val_acc
            check_disk_space(args.output_dir, min_gb=1.0)
            _ckpt_path = os.path.join(args.output_dir, ckpt_name)
            try:
                torch.save({
                    "state_dict": model.state_dict(),
                    "optimizer_state": optimizer.state_dict(),
                    "epoch": epoch,
                    "val_acc": val_acc,
                }, _ckpt_path)
            except Exception as e:
                try:
                    _u = shutil.disk_usage(os.path.dirname(_ckpt_path))
                    print(f"[SAVE FAILED] path={_ckpt_path}, error={e}, disk_free={_u.free/1024**3:.1f}GB", flush=True)
                except OSError:
                    print(f"[SAVE FAILED] path={_ckpt_path}, error={e}", flush=True)
                raise

        if epoch in save_epochs:
            milestone_name = f"{args.model}{norm_suffix}_schedulefree_s{args.seed}_lr{lr_str}_ep{epoch}.pt"
            check_disk_space(args.output_dir, min_gb=1.0)
            _ckpt_path = os.path.join(args.output_dir, milestone_name)
            try:
                torch.save({
                    "state_dict": model.state_dict(),
                    "optimizer_state": optimizer.state_dict(),
                    "epoch": epoch,
                    "val_acc": val_acc,
                }, _ckpt_path)
            except Exception as e:
                try:
                    _u = shutil.disk_usage(os.path.dirname(_ckpt_path))
                    print(f"[SAVE FAILED] path={_ckpt_path}, error={e}, disk_free={_u.free/1024**3:.1f}GB", flush=True)
                except OSError:
                    print(f"[SAVE FAILED] path={_ckpt_path}, error={e}", flush=True)
                raise

        # Switch back to train mode for next epoch
        optimizer.train()

    print(f"TRAINING_COMPLETE val_acc={best_acc:.2f}%")

    # Clean up intermediate checkpoints, keep best and final
    final_ckpt = f"{args.model}{norm_suffix}_schedulefree_s{args.seed}_lr{lr_str}_ep{args.epochs}.pt"
    for fname in os.listdir(args.output_dir):
        if fname.startswith(f"{args.model}{norm_suffix}_schedulefree_s{args.seed}_lr{lr_str}_ep") and fname != final_ckpt:
            fpath = os.path.join(args.output_dir, fname)
            os.remove(fpath)
            print(f"Removed intermediate checkpoint: {fpath}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Schedule-Free AdamW trainer")
    parser.add_argument("--model", type=str, default="resnet50", choices=list(MODEL_REGISTRY.keys()))
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    parser.add_argument("--lr", type=float, default=None)
    parser.add_argument("--weight-decay", type=float, default=None)
    parser.add_argument("--enhanced", action="store_true")
    parser.add_argument("--norm-type", type=str, default="default", choices=["default", "ln", "gn32"])
    args = parser.parse_args()

    check_gpu_whitelist(args.gpu)
    check_disk_space('/')
    check_disk_space(args.output_dir, min_gb=5.0)
    train(args)
