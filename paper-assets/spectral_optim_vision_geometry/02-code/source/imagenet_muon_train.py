# ImageNet-1K trainer with Muon optimizer (NewtonSchulz + companion AdamW)
# Usage: python3 imagenet_muon_train.py --model resnet50 --gpu 0
# Data:  /root/autodl-tmp/imagenet/{train,val}/ (ImageFolder format)
import argparse
import os
import shutil
import random
import time

import numpy as np
import torch
import torch.nn as nn
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm
from muon import muon_update
from gpu_utils import check_gpu_whitelist


def check_disk_space(path='/', min_gb=2.0):
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')


MODEL_REGISTRY = {
    "resnet50": "resnet50",
    "resnet50_ln": "resnet50",
    "deit_small": "deit_small_patch16_224",
    "convnext_tiny": "convnext_tiny",
    "swin_tiny": "swin_tiny_patch4_window7_224",
}

_HEAD_PREFIXES = {"resnet50": ("fc.",), "resnet50_ln": ("fc.",), "deit_small": ("head.",), "convnext_tiny": ("head.",), "swin_tiny": ("head.",)}
_EMBED_PREFIXES = {
    "resnet50": (),
    "resnet50_ln": (),
    "deit_small": ("cls_token", "pos_embed", "dist_token", "patch_embed."),
    "convnext_tiny": ("stem.",),
    "swin_tiny": ("patch_embed.",),
}
_SPECIAL_ADAM_PATTERNS = {
    "resnet50": (),
    "resnet50_ln": (),
    "deit_small": (),
    "convnext_tiny": (),
    "swin_tiny": ("relative_position_bias_table",),
}


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def replace_bn_with_gn(module):
    for name, child in module.named_children():
        if isinstance(child, nn.BatchNorm2d):
            setattr(module, name, nn.GroupNorm(1, child.num_features))
        else:
            replace_bn_with_gn(child)


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
    special_pats = _SPECIAL_ADAM_PATTERNS.get(model_name, ())
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
            or any(pat in name for pat in special_pats)
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


IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)


def get_dataloaders(data_dir, batch_size):
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
    train_ds = datasets.ImageFolder(os.path.join(data_dir, "train"), transform=train_tf)
    val_ds = datasets.ImageFolder(os.path.join(data_dir, "val"), transform=val_tf)
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
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    num_classes = 1000
    timm_name = MODEL_REGISTRY[args.model]
    model = timm.create_model(timm_name, pretrained=False, num_classes=num_classes)
    if args.model == "resnet50_ln":
        replace_bn_with_gn(model)
    model = model.to(device)

    muon_params, adam_params = partition_params(model, args.model)
    print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)

    muon_opt = SingleGPUMuon(muon_params, lr=args.muon_lr, momentum=0.95)
    adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)

    muon_sched = CosineAnnealingLR(muon_opt, T_max=args.epochs)
    adam_sched = CosineAnnealingLR(adam_opt, T_max=args.epochs)
    criterion = nn.CrossEntropyLoss()

    train_dl, val_dl = get_dataloaders(args.data_dir, args.batch_size)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(f"model={args.model} ({timm_name}), params={param_count:.1f}M, device={device}, "
          f"optimizer=muon, muon_lr={args.muon_lr}, batches/epoch={n_batches_total}", flush=True)

    best_acc = 0.0
    os.makedirs(args.output_dir, exist_ok=True)
    ckpt_name = f"{args.model}_muon_s{args.seed}_best.pt"

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
            if n_batches % 100 == 0:
                elapsed = time.time() - t0
                print(f"  batch {n_batches}/{n_batches_total}, loss={loss.item():.4f}, elapsed={elapsed:.1f}s", flush=True)
        muon_sched.step()
        adam_sched.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, best_val_acc={best_acc:.2f}%, time={epoch_time:.1f}s", flush=True)

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
            }, os.path.join(args.output_dir, ckpt_name))

    print(f"TRAINING_COMPLETE val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ImageNet-1K Muon trainer (NewtonSchulz + companion AdamW)")
    parser.add_argument("--model", type=str, default="resnet50", choices=list(MODEL_REGISTRY.keys()))
    parser.add_argument("--muon-lr", type=float, default=0.02)
    parser.add_argument("--epochs", type=int, default=90)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--data-dir", type=str, default="/root/autodl-tmp/imagenet/")
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    args = parser.parse_args()

    check_gpu_whitelist(args.gpu)
    check_disk_space('/')
    check_disk_space('/root/autodl-tmp', min_gb=5.0)
    train(args)
