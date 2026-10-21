# checkpoint path migrated to /root/autodl-tmp (root partition is ~30G; checkpoints filled it).
import argparse
import os
import shutil
import random
import time

import numpy as np
import torch
import torch.nn as nn
from torch.optim.lr_scheduler import LinearLR, CosineAnnealingLR, SequentialLR
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import RandAugment
import timm
from timm.data import Mixup
from timm.loss import SoftTargetCrossEntropy
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


def replace_bn_with_gn(module, num_groups=1):
    for name, child in module.named_children():
        if isinstance(child, nn.BatchNorm2d):
            setattr(module, name, nn.GroupNorm(num_groups, child.num_features))
        else:
            replace_bn_with_gn(child, num_groups)


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
    """Non-distributed Muon optimizer for single-GPU training."""

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
    train_ds = datasets.CIFAR100(root="/root/spectral_optim_vision_geometry/data", train=True, download=True, transform=train_tf)
    val_ds = datasets.CIFAR100(root="/root/spectral_optim_vision_geometry/data", train=False, download=True, transform=val_tf)
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


def train(args):
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

    muon_params, adam_params = partition_params(model, args.model)
    print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)

    muon_opt = SingleGPUMuon(muon_params, lr=args.muon_lr, momentum=0.95)
    adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)

    # Scheduler
    if args.enhanced:
        warmup_epochs = 5
        muon_warmup = LinearLR(muon_opt, start_factor=0.01, total_iters=warmup_epochs)
        muon_cosine = CosineAnnealingLR(muon_opt, T_max=max(1, args.epochs - warmup_epochs))
        muon_sched = SequentialLR(muon_opt, schedulers=[muon_warmup, muon_cosine], milestones=[warmup_epochs])
        adam_warmup = LinearLR(adam_opt, start_factor=0.01, total_iters=warmup_epochs)
        adam_cosine = CosineAnnealingLR(adam_opt, T_max=max(1, args.epochs - warmup_epochs))
        adam_sched = SequentialLR(adam_opt, schedulers=[adam_warmup, adam_cosine], milestones=[warmup_epochs])
    else:
        muon_sched = CosineAnnealingLR(muon_opt, T_max=args.epochs)
        adam_sched = CosineAnnealingLR(adam_opt, T_max=args.epochs)

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
    val_criterion = nn.CrossEntropyLoss()

    train_dl, val_dl = get_dataloaders(args.batch_size, enhanced=args.enhanced)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(f"model={args.model} ({timm_name}), params={param_count:.1f}M, device={device}, optimizer=muon, batches/epoch={n_batches_total}", flush=True)

    best_acc = 0.0
    os.makedirs(args.output_dir, exist_ok=True)
    norm_suffix = "" if args.norm_type == "default" else f"_{args.norm_type}"
    ckpt_name = f"{args.model}{norm_suffix}_muon_s{args.seed}_best.pt"
    save_epochs = set(range(5, args.epochs + 1, 5)) | {1, args.epochs}
    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            if mixup_fn is not None:
                images, labels = mixup_fn(images, labels)
            muon_opt.zero_grad()
            adam_opt.zero_grad()
            loss = train_criterion(model(images), labels)
            loss.backward()
            muon_opt.step()
            adam_opt.step()
            running_loss += loss.item()
            n_batches += 1
            if n_batches % 50 == 0:
                elapsed = time.time() - t0
                print(f"  batch {n_batches}/{n_batches_total}, loss={loss.item():.4f}, elapsed={elapsed:.1f}s", flush=True)
        muon_sched.step()
        adam_sched.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, time={epoch_time:.1f}s", flush=True)

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

        if epoch in save_epochs:
            milestone_name = f"{args.model}{norm_suffix}_muon_s{args.seed}_ep{epoch}.pt"
            _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space on data disk: {_save_free_gb:.1f}G free", flush=True)
            torch.save({
                "state_dict": model.state_dict(),
                "muon_optimizer_state": muon_opt.state_dict(),
                "adam_optimizer_state": adam_opt.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
            }, os.path.join(args.output_dir, milestone_name))

    print(f"TRAINING_COMPLETE val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 1 Muon trainer (ResNet-50 / DeiT-S)")
    parser.add_argument("--model", type=str, default="resnet50", choices=list(MODEL_REGISTRY.keys()))
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--muon-lr", type=float, default=0.02)
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    parser.add_argument("--enhanced", action="store_true", help="Enable enhanced recipe: warmup+cosine, mixup+cutmix, RandAugment, label smoothing")
    parser.add_argument("--norm-type", type=str, default="default", choices=["default", "ln", "gn32"], help="Normalization: default (BN), ln (GroupNorm g=1), gn32 (GroupNorm g=32)")
    args = parser.parse_args()
    check_gpu_whitelist(args.gpu)
    check_disk_space('/')
    check_disk_space('/root/autodl-tmp', min_gb=5.0)
    train(args)
