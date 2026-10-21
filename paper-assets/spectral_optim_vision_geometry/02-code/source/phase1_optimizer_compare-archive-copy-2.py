"""Phase 1: Optimizer comparison experiment.

# checkpoint path migrated to /root/autodl-tmp (root partition is ~30G; checkpoints filled it).
Trains {ResNet-50, DeiT-S} × {AdamW, Muon} on CIFAR-100 (224×224) for 20 epochs,
then performs layer-wise weight swap ablation and F1 comparison against Phase 0
gradient geometry predictions.

Inputs:
  - CIFAR-100 dataset (auto-downloaded to data/)
  - Phase 0 results: results/gradient_geometry_{model}.csv (for F1 stage only)

Outputs:
  - results/phase1_training_log.csv            — per-epoch training metrics
  - results/checkpoints/{model}_{optimizer}.pt  — model + optimizer checkpoints
  - results/weight_swap_results.csv             — per-layer ablation ΔAcc
  - results/phase1_f1_comparison.csv            — F1: Davis vs FCSB vs ground truth

Deps: torch, torchvision, timm, muon (pip install git+https://github.com/KellerJordan/Muon)
"""

import argparse
import csv
import math
import os
import shutil
import random
import time
from collections import defaultdict

import numpy as np
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import timm


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DATA_ROOT = "/root/spectral_optim_vision_geometry/data"
RESULTS_DIR = "/root/spectral_optim_vision_geometry/results"
CKPT_DIR = "/root/autodl-tmp/checkpoints/spectral_optim"

CIFAR100_MEAN = (0.5071, 0.4867, 0.4408)
CIFAR100_STD = (0.2675, 0.2565, 0.2761)

# ΔAcc > τ → ground truth positive for "benefits from spectral optimizer"
DELTA_ACC_THRESHOLD = 0.5  # percentage points


def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

def get_train_loader(batch_size=128, num_workers=4):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
    ])
    ds = torchvision.datasets.CIFAR100(
        root=DATA_ROOT, train=True, download=True, transform=transform)
    return torch.utils.data.DataLoader(
        ds, batch_size=batch_size, shuffle=True,
        num_workers=num_workers, pin_memory=True, drop_last=True)


def get_val_loader(batch_size=256, num_workers=4):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
    ])
    ds = torchvision.datasets.CIFAR100(
        root=DATA_ROOT, train=False, download=True, transform=transform)
    return torch.utils.data.DataLoader(
        ds, batch_size=batch_size, shuffle=False,
        num_workers=num_workers, pin_memory=True)


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------

def get_model(name, num_classes=100):
    if name == "resnet50":
        return timm.create_model("resnet50", pretrained=False, num_classes=num_classes)
    elif name == "deit_small":
        return timm.create_model(
            "deit_small_patch16_224", pretrained=False, num_classes=num_classes)
    raise ValueError(f"Unknown model: {name}")


# Classifier head prefixes — these get AdamW even in Muon mode
_HEAD_PREFIXES = {"resnet50": ("fc.",), "deit_small": ("head.",)}

# Embedding prefixes — DeiT learnable position/class tokens
_EMBED_PREFIXES = {
    "resnet50": (),
    "deit_small": ("cls_token", "pos_embed", "dist_token", "patch_embed."),
}


def _norm_param_names(model):
    """Collect parameter names belonging to normalization layers."""
    names = set()
    for mname, mod in model.named_modules():
        if isinstance(mod, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.GroupNorm)):
            for pname, _ in mod.named_parameters():
                names.add(f"{mname}.{pname}" if mname else pname)
    return names


def partition_params(model, model_name):
    """Split params into (muon_eligible, adam_only).

    Muon-eligible: ≥2D .weight from Conv2d/Linear, excluding classifier head,
    embedding, and normalization layers. Everything else → AdamW.
    """
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


# ---------------------------------------------------------------------------
# Optimizer
# ---------------------------------------------------------------------------

def build_optimizer(model, model_name, opt_name, epochs):
    """Build optimizer + cosine LR scheduler."""
    if opt_name == "adamw":
        opt = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.05)
        sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=epochs)
        return opt, sched

    if opt_name == "muon":
        from muon import SingleDeviceMuonWithAuxAdam as Muon
        muon_params, adam_params = partition_params(model, model_name)
        print(f"  Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW")
        opt = Muon([
            {"params": muon_params, "use_muon": True, "lr": 0.02, "momentum": 0.95},
            {"params": adam_params, "use_muon": False, "lr": 3e-4, "weight_decay": 0.05},
        ])
        sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=epochs)
        return opt, sched

    raise ValueError(f"Unknown optimizer: {opt_name}")


# ---------------------------------------------------------------------------
# Train / Eval
# ---------------------------------------------------------------------------

@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct = total = 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        correct += (model(images).argmax(1) == labels).sum().item()
        total += labels.size(0)
    return 100.0 * correct / total


def train_one_config(model_name, opt_name, device, epochs=20):
    """Train one (model, optimizer) pair. Returns (model, optimizer, log)."""
    set_seed(42)
    model = get_model(model_name).to(device)
    train_loader = get_train_loader()
    val_loader = get_val_loader()
    opt, sched = build_optimizer(model, model_name, opt_name, epochs)
    criterion = nn.CrossEntropyLoss()

    log = []
    for epoch in range(1, epochs + 1):
        model.train()
        running_loss = 0.0
        n_batches = 0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            opt.zero_grad()
            loss = criterion(model(images), labels)
            loss.backward()
            opt.step()
            running_loss += loss.item()
            n_batches += 1

        sched.step()
        avg_loss = running_loss / n_batches
        val_acc = evaluate(model, val_loader, device)

        log.append({
            "epoch": epoch, "model": model_name, "optimizer": opt_name,
            "train_loss": f"{avg_loss:.4f}", "val_acc": f"{val_acc:.2f}",
        })
        print(f"  [{model_name}+{opt_name}] epoch {epoch}/{epochs} "
              f"loss={avg_loss:.4f} val_acc={val_acc:.2f}%")

    return model, opt, log


# ---------------------------------------------------------------------------
# CSV helper
# ---------------------------------------------------------------------------

def _update_csv(path, fieldnames, new_rows, key_field="model", key_value=None):
    """Write CSV: replace rows matching key_value in key_field, keep others."""
    existing = []
    if os.path.exists(path) and key_value is not None:
        with open(path, "r") as f:
            existing = [r for r in csv.DictReader(f) if r.get(key_field) != key_value]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing + new_rows)


# ---------------------------------------------------------------------------
# Training stage
# ---------------------------------------------------------------------------

def run_training(model_name, device, epochs=20):
    """Train AdamW and Muon for one architecture. Save checkpoints + log."""
    os.makedirs(CKPT_DIR, exist_ok=True)
    all_logs = []

    for opt_name in ["adamw", "muon"]:
        print(f"\n{'='*60}")
        print(f"Training {model_name} + {opt_name}")
        print(f"{'='*60}")

        t0 = time.time()
        model, opt, log = train_one_config(model_name, opt_name, device, epochs)
        print(f"  Completed in {time.time() - t0:.0f}s")

        ckpt_path = os.path.join(CKPT_DIR, f"{model_name}_{opt_name}.pt")
        # _DISK_CHECK_SAVE_INJECTED_
        _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
        if _save_free_gb < 1.0:
            print(f"WARNING: Low disk space on data disk: {_save_free_gb:.1f}G free", flush=True)
        torch.save({
            "state_dict": model.state_dict(),
            "optimizer_state_dict": opt.state_dict(),
            "model_name": model_name,
            "optimizer_name": opt_name,
            "epoch": epochs,
        }, ckpt_path)
        print(f"  Checkpoint: {ckpt_path}")

        all_logs.extend(log)

    log_fields = ["epoch", "model", "optimizer", "train_loss", "val_acc"]
    _update_csv(os.path.join(RESULTS_DIR, "phase1_training_log.csv"),
                log_fields, all_logs, "model", model_name)
    print(f"\nTraining log saved.")


# ---------------------------------------------------------------------------
# Weight Swap Ablation
# ---------------------------------------------------------------------------

def _swappable_layers(model):
    """Return {name: module} for all Conv2d and Linear layers."""
    return {n: m for n, m in model.named_modules()
            if isinstance(m, (nn.Conv2d, nn.Linear))}


def run_ablation(model_name, device):
    """Per-layer weight swap: replace each AdamW layer with Muon's, measure ΔAcc."""
    print(f"\n{'='*60}")
    print(f"Weight Swap Ablation: {model_name}")
    print(f"{'='*60}")

    adamw_ckpt = os.path.join(CKPT_DIR, f"{model_name}_adamw.pt")
    muon_ckpt = os.path.join(CKPT_DIR, f"{model_name}_muon.pt")
    for p in [adamw_ckpt, muon_ckpt]:
        if not os.path.exists(p):
            print(f"ERROR: checkpoint missing: {p}")
            return []

    adamw_sd = torch.load(adamw_ckpt, map_location=device, weights_only=True)["state_dict"]
    muon_sd = torch.load(muon_ckpt, map_location=device, weights_only=True)["state_dict"]

    model = get_model(model_name).to(device)
    model.load_state_dict(adamw_sd)
    val_loader = get_val_loader()
    baseline_acc = evaluate(model, val_loader, device)
    print(f"  AdamW baseline: {baseline_acc:.2f}%")

    layers = _swappable_layers(model)
    print(f"  Layers to test: {len(layers)}")

    param_dict = dict(model.named_parameters())
    results = []

    for i, (layer_name, layer_mod) in enumerate(layers.items(), 1):
        # Save originals, swap in Muon weights
        originals = {}
        swapped_any = False
        for suffix in ("weight", "bias"):
            key = f"{layer_name}.{suffix}"
            if key in muon_sd and key in param_dict:
                originals[key] = param_dict[key].data.clone()
                param_dict[key].data.copy_(muon_sd[key])
                swapped_any = True

        if not swapped_any:
            continue

        swapped_acc = evaluate(model, val_loader, device)
        delta = swapped_acc - baseline_acc

        # Restore originals
        for key, orig_data in originals.items():
            param_dict[key].data.copy_(orig_data)

        ltype = "conv" if isinstance(layer_mod, nn.Conv2d) else "linear"
        gt_pos = 1 if delta >= DELTA_ACC_THRESHOLD else 0

        results.append({
            "model": model_name,
            "layer_name": layer_name,
            "layer_type": ltype,
            "delta_acc": f"{delta:.2f}",
            "ground_truth_positive": gt_pos,
        })
        tag = " ** POSITIVE" if gt_pos else ""
        print(f"  [{i}/{len(layers)}] {layer_name} ({ltype}): "
              f"ΔAcc={delta:+.2f}%{tag}")

    csv_path = os.path.join(RESULTS_DIR, "weight_swap_results.csv")
    fields = ["model", "layer_name", "layer_type", "delta_acc", "ground_truth_positive"]
    _update_csv(csv_path, fields, results, "model", model_name)
    print(f"\n  Results: {csv_path}")

    n_pos = sum(r["ground_truth_positive"] for r in results)
    print(f"  Positives: {n_pos}/{len(results)} (τ={DELTA_ACC_THRESHOLD}%)")
    return results


# ---------------------------------------------------------------------------
# F1 Comparison
# ---------------------------------------------------------------------------

def _f1(y_true, y_pred):
    """Binary F1 score, returned as percentage (0–100)."""
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    prec = tp / (tp + fp) if (tp + fp) else 0
    rec = tp / (tp + fn) if (tp + fn) else 0
    return 200 * prec * rec / (prec + rec) if (prec + rec) else 0


# ---------------------------------------------------------------------------
# F1 Comparison (per-epoch)
# ---------------------------------------------------------------------------

def run_f1_comparison(model_name):
    """Compare Phase 0 predictions (Davis, FCSB_grishina) against weight swap ground truth, per epoch."""
    print(f"\n{'='*60}")
    print(f"F1 Comparison (per-epoch): {model_name}")
    print(f"{'='*60}")

    phase0_path = os.path.join(RESULTS_DIR, f"gradient_geometry_{model_name}.csv")
    swap_path = os.path.join(RESULTS_DIR, "weight_swap_results.csv")
    for p, label in [(phase0_path, "Phase 0"), (swap_path, "weight swap")]:
        if not os.path.exists(p):
            print(f"ERROR: {label} results missing: {p}")
            return None

    with open(phase0_path) as f:
        p0_all = list(csv.DictReader(f))

    if p0_all and "epoch" in p0_all[0]:
        epochs = sorted(set(int(r["epoch"]) for r in p0_all))
    else:
        epochs = [0]

    with open(swap_path) as f:
        swap_rows = [r for r in csv.DictReader(f) if r["model"] == model_name]
    if not swap_rows:
        print(f"ERROR: no weight swap data for {model_name}")
        return None

    all_f1_rows = []
    early_pass = False

    for ep in epochs:
        if ep > 0:
            p0_rows = [r for r in p0_all if int(r["epoch"]) == ep]
        else:
            p0_rows = p0_all
        p0_by_layer = {r["layer_name"]: r for r in p0_rows}

        by_type = defaultdict(lambda: {"gt": [], "davis": [], "fcsb": []})
        matched = 0
        for sr in swap_rows:
            if sr["layer_name"] not in p0_by_layer:
                continue
            p0 = p0_by_layer[sr["layer_name"]]
            ltype = sr["layer_type"]
            by_type[ltype]["gt"].append(int(sr["ground_truth_positive"]))
            by_type[ltype]["davis"].append(int(p0["davis_pred"] == "True"))
            by_type[ltype]["fcsb"].append(int(p0["fcsb_grishina_pred"] == "True"))
            matched += 1

        print(f"\n  --- Epoch {ep} (matched {matched} layers) ---")

        for ltype in ["conv", "linear"]:
            if ltype not in by_type:
                continue
            d = by_type[ltype]
            f1_d = _f1(d["gt"], d["davis"])
            f1_f = _f1(d["gt"], d["fcsb"])
            delta = f1_f - f1_d
            all_f1_rows.append({
                "model": model_name, "epoch": ep, "layer_type": ltype,
                "n_layers": len(d["gt"]), "n_positive": sum(d["gt"]),
                "f1_davis": f"{f1_d:.1f}", "f1_fcsb_grishina": f"{f1_f:.1f}",
                "delta_f1": f"{delta:.1f}",
            })
            print(f"  {ltype}: F1(Davis)={f1_d:.1f}  F1(FCSB_grishina)={f1_f:.1f}  "
                  f"\u0394={delta:+.1f}")

            if ltype == "conv" and ep <= 5 and delta >= 10.0:
                early_pass = True

    csv_path = os.path.join(RESULTS_DIR, "phase1_f1_comparison.csv")
    fields = ["model", "epoch", "layer_type", "n_layers", "n_positive",
              "f1_davis", "f1_fcsb_grishina", "delta_f1"]
    _update_csv(csv_path, fields, all_f1_rows, "model", model_name)
    print(f"\n  Per-epoch F1 comparison: {csv_path}")

    print(f"\n  PASS CRITERION: FCSB_grishina F1 - Davis F1 >= 10 pts "
          f"on conv layers at epoch <= 5")
    print(f"  Result: {'PASS' if early_pass else 'FAIL'}")
    return early_pass



def main():
    parser = argparse.ArgumentParser(
        description="Phase 1: {ResNet-50, DeiT-S} × {AdamW, Muon} on CIFAR-100",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  python phase1_optimizer_compare.py --model resnet50 --gpu 0
  python phase1_optimizer_compare.py --model resnet50 --gpu 0 --stage train
  python phase1_optimizer_compare.py --model resnet50 --gpu 0 --stage ablation
  python phase1_optimizer_compare.py --model deit_small --gpu 1 --stage f1
""")
    parser.add_argument("--model", required=True, choices=["resnet50", "deit_small"])
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--stage", default="all",
                        choices=["all", "train", "ablation", "f1"])
    parser.add_argument("--epochs", type=int, default=20)
    args = parser.parse_args()

    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    print(f"Model: {args.model}  Stage: {args.stage}  Epochs: {args.epochs}")

    os.makedirs(RESULTS_DIR, exist_ok=True)

    if args.stage in ("all", "train"):
        run_training(args.model, device, args.epochs)

    if args.stage in ("all", "ablation"):
        run_ablation(args.model, device)

    if args.stage in ("all", "f1"):
        run_f1_comparison(args.model)


if __name__ == "__main__":
    # _DISK_CHECK_STARTUP_INJECTED_
    _disk_free_gb = shutil.disk_usage('/').free / (1024**3)
    if _disk_free_gb < 2.0:
        raise RuntimeError(
            f"Disk space critically low: {_disk_free_gb:.1f}G free on /. "
            f"Need >= 2G. Clean up checkpoints or use /root/autodl-tmp/."
        )
    main()
