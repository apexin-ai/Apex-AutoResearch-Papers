# Phase 1 baseline trainer for spectral_optim_vision_geometry
# Trains {ResNet-50, DeiT-S} with AdamW/SGD on CIFAR-100 (224x224)
# Usage: python3 baseline_train.py --model resnet50 --gpu 0 --seed 42
#        python3 baseline_train.py --model deit_small --optimizer sgd --gpu 0 --seed 42
# Output: checkpoint at <output_dir>/<model>_<optimizer>_s<seed>_lr<lr>.pt
# Deps: torch, torchvision, timm
# checkpoint path: project-local ./checkpoints by default
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
from torch.optim import Optimizer
from torch.optim.lr_scheduler import LinearLR, CosineAnnealingLR, SequentialLR
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import RandAugment
import timm
from timm.data import Mixup
from timm.loss import SoftTargetCrossEntropy
from gpu_utils import check_gpu_whitelist

os.environ.setdefault("TMPDIR", "/tmp")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_ROOT = os.path.join(_SCRIPT_DIR, "data")
# Remove broken symlinks left from AutoDL migration
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


class Lion(Optimizer):
    def __init__(self, params, lr=1e-4, betas=(0.9, 0.99), weight_decay=0.0):
        defaults = dict(lr=lr, betas=betas, weight_decay=weight_decay)
        super().__init__(params, defaults)

    @torch.no_grad()
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()
        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue
                grad = p.grad
                state = self.state[p]
                if len(state) == 0:
                    state['exp_avg'] = torch.zeros_like(p)
                exp_avg = state['exp_avg']
                beta1, beta2 = group['betas']
                if group['weight_decay'] != 0:
                    p.data.mul_(1 - group['lr'] * group['weight_decay'])
                update = exp_avg * beta1 + grad * (1 - beta1)
                p.add_(torch.sign(update), alpha=-group['lr'])
                exp_avg.mul_(beta2).add_(grad, alpha=1 - beta2)
        return loss


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



# --- Parameter partition for two-group optimizers (mirrors muon_train.py routing) ---
_HEAD_PREFIXES = {"resnet50": ("fc.",), "resnet50_ln": ("fc.",), "deit_small": ("head.",), "convnext_tiny": ("head.",)}
_EMBED_PREFIXES = {
    "resnet50": (),
    "resnet50_ln": (),
    "deit_small": ("cls_token", "pos_embed", "dist_token", "patch_embed."),
    "convnext_tiny": ("stem.",),
}

def _norm_param_names(model):
    names = set()
    for mname, mod in model.named_modules():
        if isinstance(mod, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.GroupNorm)):
            for pname, _ in mod.named_parameters():
                names.add(f"{mname}.{pname}" if mname else pname)
    return names

def partition_params(model, model_name):
    """Split params into 2D weight matrices vs 1D/special params (same logic as Muon)."""
    head_pf = _HEAD_PREFIXES.get(model_name, ())
    embed_pf = _EMBED_PREFIXES.get(model_name, ())
    norm_names = _norm_param_names(model)
    params_2d, params_1d = [], []
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        is_1d = (
            any(name.startswith(p) for p in head_pf)
            or any(name.startswith(p) or name == p.rstrip(".") for p in embed_pf)
            or name in norm_names
            or name.endswith(".bias")
            or param.ndim < 2
        )
        (params_1d if is_1d else params_2d).append(param)
    return params_2d, params_1d


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

    if args.optimizer == "adamw":
        lr = args.lr if args.lr is not None else 3e-4
        wd = args.weight_decay if args.weight_decay is not None else 0.05
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=wd)
    elif args.optimizer == "sgd":
        lr = args.lr if args.lr is not None else 0.1
        wd = args.weight_decay if args.weight_decay is not None else 1e-4
        optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=wd)
    elif args.optimizer == "lion":
        lr = args.lr if args.lr is not None else 1e-4
        wd = args.weight_decay if args.weight_decay is not None else 1e-2
        optimizer = Lion(model.parameters(), lr=lr, weight_decay=wd)
    elif args.optimizer == "soap":
        from heavyball import SOAP
        lr = args.soap_lr if args.soap_lr is not None else (args.lr if args.lr is not None else 3e-3)
        wd = args.weight_decay if args.weight_decay is not None else 0.01
        optimizer = SOAP(model.parameters(), lr=lr, weight_decay=wd)
    elif args.optimizer == "shampoo":
        from heavyball import KLShampoo
        lr = args.lr if args.lr is not None else 3e-3
        wd = args.weight_decay if args.weight_decay is not None else 0.01
        optimizer = KLShampoo(model.parameters(), lr=lr, weight_decay=wd)
    elif args.optimizer == "adamw_twogroup":
        lr = args.lr if args.lr is not None else 1e-3
        wd = args.weight_decay if args.weight_decay is not None else 0.05
        params_2d, params_1d = partition_params(model, args.model)
        companion_lr = 3e-4
        optimizer = torch.optim.AdamW([
            {"params": params_2d, "lr": lr, "weight_decay": wd},
            {"params": params_1d, "lr": companion_lr, "weight_decay": wd},
        ])
        print(f"adamw_twogroup: 2D group={len(params_2d)} tensors (lr={lr}), 1D group={len(params_1d)} tensors (lr={companion_lr})")

    # Scheduler
    if args.enhanced:
        warmup_epochs = 5
        warmup_scheduler = LinearLR(optimizer, start_factor=0.01, total_iters=warmup_epochs)
        cosine_scheduler = CosineAnnealingLR(optimizer, T_max=max(1, args.epochs - warmup_epochs))
        scheduler = SequentialLR(optimizer, schedulers=[warmup_scheduler, cosine_scheduler], milestones=[warmup_epochs])
    else:
        scheduler = CosineAnnealingLR(optimizer, T_max=args.epochs)

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

    lr_str = format_lr(lr)

    train_dl, val_dl = get_dataloaders(args.batch_size, enhanced=args.enhanced)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    enhanced_str = " [ENHANCED]" if args.enhanced else ""
    print(f"model={args.model} ({timm_name}), params={param_count:.1f}M, optimizer={args.optimizer}, lr={lr}, wd={wd}, device={device}{enhanced_str}")

    best_acc = 0.0
    os.makedirs(args.output_dir, exist_ok=True)
    norm_suffix = "" if getattr(args, 'norm_type', 'default') == "default" else f"_{args.norm_type}"
    ckpt_name = f"{args.model}{norm_suffix}_{args.optimizer}_s{args.seed}_lr{lr_str}_best.pt"
    save_epochs = set(range(5, args.epochs + 1, 5)) | {1, args.epochs}
    for epoch in range(1, args.epochs + 1):
        model.train()
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
        scheduler.step()

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
            milestone_name = f"{args.model}{norm_suffix}_{args.optimizer}_s{args.seed}_lr{lr_str}_ep{epoch}.pt"
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

    print(f"TRAINING_COMPLETE val_acc={best_acc:.2f}%")

    # Clean up intermediate checkpoints, keep best and final
    final_ckpt = f"{args.model}{norm_suffix}_{args.optimizer}_s{args.seed}_lr{lr_str}_ep{args.epochs}.pt"
    for fname in os.listdir(args.output_dir):
        if fname.startswith(f"{args.model}{norm_suffix}_{args.optimizer}_s{args.seed}_lr{lr_str}_ep") and fname != final_ckpt:
            fpath = os.path.join(args.output_dir, fname)
            os.remove(fpath)
            print(f"Removed intermediate checkpoint: {fpath}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 1 baseline trainer (ResNet-50 / DeiT-S)")
    parser.add_argument("--model", type=str, default="resnet50", choices=list(MODEL_REGISTRY.keys()), help='Model: resnet50, resnet50_ln, deit_small, convnext_tiny')
    parser.add_argument("--optimizer", type=str, default="adamw", choices=["adamw", "sgd", "lion", "soap", "shampoo", "adamw_twogroup"])
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    parser.add_argument("--lr", type=float, default=None, help="Learning rate (default: 3e-4 for AdamW, 0.1 for SGD)")
    parser.add_argument("--weight-decay", type=float, default=None, help="Weight decay (default: 0.05 for AdamW, 1e-4 for SGD)")
    parser.add_argument("--soap-lr", type=float, default=None, help="SOAP learning rate (overrides --lr when optimizer=soap)")
    parser.add_argument("--enhanced", action="store_true", help="Enable enhanced recipe: warmup+cosine, mixup+cutmix, RandAugment, label smoothing")
    parser.add_argument("--norm-type", type=str, default="default", choices=["default", "ln", "gn32"], help="Normalization: default (BN), ln (GroupNorm g=1), gn32 (GroupNorm g=32)")
    args = parser.parse_args()

    check_gpu_whitelist(args.gpu)

    check_disk_space('/')
    check_disk_space(args.output_dir, min_gb=5.0)
    train(args)
