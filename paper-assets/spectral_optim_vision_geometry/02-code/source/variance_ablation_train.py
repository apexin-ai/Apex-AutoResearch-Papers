import argparse
import os
import shutil
import random
import time
import json

import numpy as np
import torch
import torch.nn as nn
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm
from gpu_utils import check_gpu_whitelist


def check_disk_space(path='/', min_gb=2.0):
    os.makedirs(path, exist_ok=True)
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')


MODEL_REGISTRY = {
    "resnet50": "resnet50",
    "deit_small": "deit_small_patch16_224",
}

_HEAD_PREFIXES = {"resnet50": ("fc.",), "deit_small": ("head.",)}
_EMBED_PREFIXES = {
    "resnet50": (),
    "deit_small": ("cls_token", "pos_embed", "dist_token", "patch_embed."),
}


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


# ── Newton-Schulz orthogonalization (standard Muon) ──

def zeropower_via_newtonschulz5(G, steps=5):
    a, b, c = (3.4445, -4.7750, 2.0315)
    X = G.bfloat16()
    X = X / (X.norm() + 1e-7)
    transposed = False
    if X.size(0) > X.size(1):
        X = X.T
        transposed = True
    for _ in range(steps):
        A = X @ X.T
        B = b * A + c * A @ A
        X = a * X + B @ X
    if transposed:
        X = X.T
    return X


def muon_update(grad, buf, beta=0.95):
    buf.mul_(beta).add_(grad)
    if buf.ndim < 2:
        return buf
    g = buf.view(buf.shape[0], -1)
    return zeropower_via_newtonschulz5(g).to(buf.dtype).view(buf.shape)


def muon_update_no_ns(grad, buf, beta=0.95):
    """Momentum only — skip Newton-Schulz, just normalize by Frobenius norm."""
    buf.mul_(beta).add_(grad)
    if buf.ndim < 2:
        return buf
    g = buf.view(buf.shape[0], -1)
    return (g / (g.norm() + 1e-7)).to(buf.dtype).view(buf.shape)


# ── Optimizers ──

class SingleGPUMuon(torch.optim.Optimizer):
    def __init__(self, params, lr=0.02, momentum=0.95, weight_decay=0, use_ns=True):
        defaults = dict(lr=lr, momentum=momentum, weight_decay=weight_decay)
        super().__init__(params, defaults)
        self.use_ns = use_ns

    @torch.no_grad()
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()
        update_fn = muon_update if self.use_ns else muon_update_no_ns
        for group in self.param_groups:
            for p in group["params"]:
                if p.grad is None:
                    continue
                state = self.state[p]
                if len(state) == 0:
                    state["momentum_buffer"] = torch.zeros_like(p)
                g = p.grad.clone()
                update = update_fn(g, state["momentum_buffer"], beta=group["momentum"])
                p.mul_(1 - group["lr"] * group["weight_decay"])
                p.add_(update.reshape(p.shape), alpha=-group["lr"])
        return loss


def spectral_normalize_weights(model, model_name):
    """Post-hoc spectral normalization: scale each >=2D weight to unit spectral norm."""
    norm_names = _norm_param_names(model)
    head_pf = _HEAD_PREFIXES[model_name]
    embed_pf = _EMBED_PREFIXES[model_name]
    with torch.no_grad():
        for name, param in model.named_parameters():
            if param.ndim < 2:
                continue
            if any(name.startswith(p) for p in head_pf):
                continue
            if any(name.startswith(p) or name == p.rstrip(".") for p in embed_pf):
                continue
            if name in norm_names or name.endswith(".bias"):
                continue
            W = param.view(param.shape[0], -1)
            sigma = torch.linalg.svdvals(W.float())[0]
            if sigma > 1e-7:
                param.div_(sigma)


# ── Data ──

def get_dataloaders(batch_size):
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


@torch.no_grad()
def compute_gradient_stats(model, model_name):
    """Compute stable rank and spectral norm for >=2D Muon-eligible params."""
    norm_names = _norm_param_names(model)
    head_pf = _HEAD_PREFIXES[model_name]
    embed_pf = _EMBED_PREFIXES[model_name]
    stats = {}
    for name, param in model.named_parameters():
        if param.ndim < 2:
            continue
        if any(name.startswith(p) for p in head_pf):
            continue
        if any(name.startswith(p) or name == p.rstrip(".") for p in embed_pf):
            continue
        if name in norm_names or name.endswith(".bias"):
            continue
        W = param.view(param.shape[0], -1).float()
        svs = torch.linalg.svdvals(W)
        spectral_norm = svs[0].item()
        frob_sq = (svs ** 2).sum().item()
        stable_rank = frob_sq / (spectral_norm ** 2 + 1e-12)
        stats[name] = {"spectral_norm": round(spectral_norm, 6), "stable_rank": round(stable_rank, 4)}
    return stats


def train(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    num_classes = 100
    timm_name = MODEL_REGISTRY[args.model]
    model = timm.create_model(timm_name, pretrained=False, num_classes=num_classes).to(device)

    muon_params, adam_params = partition_params(model, args.model)
    print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)

    ablation = args.ablation
    use_adamw_specnorm = (ablation == "adamw_specnorm")

    if use_adamw_specnorm:
        all_params = list(model.parameters())
        optimizer = torch.optim.AdamW(all_params, lr=3e-4, weight_decay=0.05)
        scheduler = CosineAnnealingLR(optimizer, T_max=args.epochs)
        print(f"Ablation=adamw_specnorm: AdamW on all params + post-step spectral normalization", flush=True)
    else:
        use_ns = (ablation == "none")
        muon_opt = SingleGPUMuon(muon_params, lr=args.muon_lr, momentum=0.95, use_ns=use_ns)
        adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)
        muon_sched = CosineAnnealingLR(muon_opt, T_max=args.epochs)
        adam_sched = CosineAnnealingLR(adam_opt, T_max=args.epochs)
        print(f"Ablation={ablation}: Muon (NS={'ON' if use_ns else 'OFF'}) + AdamW", flush=True)

    train_criterion = nn.CrossEntropyLoss()
    train_dl, val_dl = get_dataloaders(args.batch_size)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(f"model={args.model} ({timm_name}), params={param_count:.1f}M, device={device}, ablation={ablation}, batches/epoch={n_batches_total}", flush=True)

    best_acc = 0.0
    os.makedirs(args.output_dir, exist_ok=True)
    log_path = os.path.join(args.output_dir, f"{args.model}_ablation_{ablation}_s{args.seed}_log.jsonl")

    stat_epochs = set(range(5, args.epochs + 1, 5)) | {1}

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)

            if use_adamw_specnorm:
                optimizer.zero_grad()
                loss = train_criterion(model(images), labels)
                loss.backward()
                optimizer.step()
                spectral_normalize_weights(model, args.model)
            else:
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

        if use_adamw_specnorm:
            scheduler.step()
        else:
            muon_sched.step()
            adam_sched.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, time={epoch_time:.1f}s", flush=True)

        log_entry = {
            "epoch": epoch,
            "train_loss": round(avg_loss, 6),
            "val_acc": round(val_acc, 4),
            "epoch_time": round(epoch_time, 1),
            "ablation": ablation,
        }

        if epoch in stat_epochs:
            grad_stats = compute_gradient_stats(model, args.model)
            spectral_norms = [v["spectral_norm"] for v in grad_stats.values()]
            stable_ranks = [v["stable_rank"] for v in grad_stats.values()]
            log_entry["mean_spectral_norm"] = round(np.mean(spectral_norms), 6)
            log_entry["mean_stable_rank"] = round(np.mean(stable_ranks), 4)
            log_entry["median_stable_rank"] = round(np.median(stable_ranks), 4)
            print(f"  grad_stats: mean_spectral_norm={log_entry['mean_spectral_norm']}, mean_stable_rank={log_entry['mean_stable_rank']}, median_stable_rank={log_entry['median_stable_rank']}", flush=True)

        with open(log_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

        if val_acc > best_acc:
            best_acc = val_acc
            ckpt_name = f"{args.model}_ablation_{ablation}_s{args.seed}_best.pt"
            _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space: {_save_free_gb:.1f}G free", flush=True)
            torch.save({
                "state_dict": model.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "ablation": ablation,
            }, os.path.join(args.output_dir, ckpt_name))

    print(f"TRAINING_COMPLETE val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Variance adaptation ablation: Muon NS variants")
    parser.add_argument("--model", type=str, default="resnet50", choices=list(MODEL_REGISTRY.keys()))
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--muon-lr", type=float, default=0.02)
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    parser.add_argument("--ablation", type=str, default="none",
                        choices=["none", "no_ns", "adamw_specnorm"],
                        help="none=full Muon, no_ns=skip Newton-Schulz, adamw_specnorm=AdamW+spectral norm")
    args = parser.parse_args()
    check_gpu_whitelist(args.gpu)
    check_disk_space('/')
    check_disk_space('/root/autodl-tmp', min_gb=5.0)
    train(args)
