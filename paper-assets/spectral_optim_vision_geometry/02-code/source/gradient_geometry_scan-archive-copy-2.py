"""Gradient geometry scan for spectral optimizer prediction.

Trains ResNet-50 or DeiT-S on CIFAR-100 and computes per-layer gradient
geometry metrics (stable rank, nuclear/Frobenius norm ratio) at selected
epochs to predict whether spectral optimizers would be beneficial.

Inputs:  CIFAR-100 (auto-downloaded), model weights from timm
Outputs: gradient_geometry_results.csv, terminal summaries
Deps:    torch, torchvision, timm, numpy
"""

import sys
for _mod in ['numpy', 'torch', 'torchvision', 'timm']:
    try:
        __import__(_mod)
    except ImportError:
        print(f"FATAL: {_mod} not found. Run: pip install {_mod}")
        sys.exit(1)

import argparse
import csv
import math
import os
import random
import signal
import time
from collections import defaultdict
from contextlib import contextmanager

import numpy as np
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import timm


# ---------------------------------------------------------------------------
# Timeout utility
# ---------------------------------------------------------------------------

class SVDTimeout(Exception):
    pass


@contextmanager
def svd_timeout(seconds=30):
    """Context manager that raises SVDTimeout after `seconds`."""
    def _handler(signum, frame):
        raise SVDTimeout()
    old = signal.signal(signal.SIGALRM, _handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


# ---------------------------------------------------------------------------
# Seed
# ---------------------------------------------------------------------------

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

def get_dataloader(batch_size, num_workers=4):
    """CIFAR-100 train loader with resize to 224x224."""
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.5071, 0.4867, 0.4408),
                             (0.2675, 0.2565, 0.2761)),
    ])
    dataset = torchvision.datasets.CIFAR100(
        root="/root/spectral_optim_vision_geometry/data",
        train=True, download=True, transform=transform,
    )
    return torch.utils.data.DataLoader(
        dataset, batch_size=batch_size, shuffle=True,
        num_workers=num_workers, pin_memory=True, drop_last=True,
    )


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------

def get_model(name, num_classes=100):
    """Load model via timm, reset classifier head to num_classes."""
    if name == "resnet50":
        model = timm.create_model("resnet50", pretrained=False, num_classes=num_classes)
    elif name == "deit_small":
        model = timm.create_model("deit_small_patch16_224", pretrained=False, num_classes=num_classes)
    else:
        raise ValueError(f"Unknown model: {name}")
    return model


# ---------------------------------------------------------------------------
# Layer collection
# ---------------------------------------------------------------------------

def collect_target_layers(model):
    """Return dict of {name: module} for all Conv2d and Linear layers."""
    layers = {}
    for name, mod in model.named_modules():
        if isinstance(mod, (nn.Conv2d, nn.Linear)):
            layers[name] = mod
    return layers


# ---------------------------------------------------------------------------
# Activation hook
# ---------------------------------------------------------------------------

class ActivationRecorder:
    """Registers forward hooks to capture input activations."""

    def __init__(self, layers):
        self.activations = {}
        self.hooks = []
        for name, mod in layers.items():
            h = mod.register_forward_hook(self._make_hook(name))
            self.hooks.append(h)

    def _make_hook(self, name):
        def hook(module, inp, out):
            self.activations[name] = inp[0].detach()
        return hook

    def clear(self):
        self.activations.clear()

    def remove(self):
        for h in self.hooks:
            h.remove()
        self.hooks.clear()


# ---------------------------------------------------------------------------
# Gradient geometry metrics
# ---------------------------------------------------------------------------

def compute_stable_rank(X):
    """Stable rank sr(X) = ||X||_F^2 / ||X||_2^2."""
    fro_sq = torch.sum(X ** 2).item()
    s0 = torch.linalg.svdvals(X)[0].item()
    spec_sq = s0 ** 2
    if spec_sq < 1e-12:
        return float("nan")
    return fro_sq / spec_sq


def compute_nuclear_frobenius_ratio(grad_2d):
    """R = (sum(s))^2 / sum(s^2) where s are singular values of grad."""
    s = torch.linalg.svdvals(grad_2d)
    nuc = s.sum().item()
    fro_sq = (s ** 2).sum().item()
    if fro_sq < 1e-12:
        return float("nan")
    return (nuc ** 2) / fro_sq


# ---------------------------------------------------------------------------
# Delta definitions
# ---------------------------------------------------------------------------

def compute_delta_theory(kernel_size):
    return math.sqrt(kernel_size) if kernel_size > 0 else 1.0


def compute_delta_grishina(kernel_size):
    return float(kernel_size) if kernel_size > 0 else 1.0


def compute_delta_empirical(grad_4d):
    """Empirical delta via Hu (2015) mode-0/mode-1 unfolding nuclear norms.

    tensor_nuc_approx = min(nuc_0, nuc_1); delta = approx / nuc_0, clamped >= 1.
    """
    c_out, c_in, kh, kw = grad_4d.shape

    # Mode-0 unfolding (Muon flatten): (c_out, c_in*kh*kw)
    t_mode0 = grad_4d.reshape(c_out, -1)
    nuc_0 = torch.linalg.svdvals(t_mode0).sum().item()

    # Mode-1 unfolding: (c_in, c_out*kh*kw)
    t_mode1 = grad_4d.permute(1, 0, 2, 3).reshape(c_in, -1)
    nuc_1 = torch.linalg.svdvals(t_mode1).sum().item()

    # Hu (2015): min of mode unfolding nuclear norms as tensor nuclear norm approx
    tensor_nuc_approx = min(nuc_0, nuc_1)

    return max(1.0, tensor_nuc_approx / nuc_0) if nuc_0 > 0 else 1.0


# ---------------------------------------------------------------------------
# Per-layer scan
# ---------------------------------------------------------------------------

def scan_layer(name, module, activation, timeout_sec=30):
    """Compute all gradient geometry metrics for one layer.

    Returns dict with keys for R, sr_X, three deltas, three FCSB predictions,
    and davis_pred.  On timeout returns None.
    """
    is_conv = isinstance(module, nn.Conv2d)
    layer_type = "conv2d" if is_conv else "linear"
    shape = tuple(module.weight.shape)
    kernel_size = module.kernel_size[0] if is_conv else 0

    try:
        with svd_timeout(timeout_sec):
            X = activation.float()
            if is_conv:
                b, c, h, w = X.shape
                X_2d = X.permute(0, 2, 3, 1).reshape(-1, c)
            else:
                X_2d = X.reshape(-1, X.shape[-1]) if X.dim() > 2 else X
            sr_X = compute_stable_rank(X_2d)

            grad = module.weight.grad.detach().float()
            if is_conv:
                c_out, c_in, k1, k2 = grad.shape
                grad_2d = grad.reshape(c_out, c_in * k1 * k2)
            else:
                grad_2d = grad
            R = compute_nuclear_frobenius_ratio(grad_2d)

            delta_theory = compute_delta_theory(kernel_size)
            delta_grishina = compute_delta_grishina(kernel_size)
            delta_empirical = compute_delta_empirical(grad) if is_conv else 1.0

            davis_pred = bool(R > sr_X)
            fcsb_theory_pred = bool(R > delta_theory ** 2 * sr_X)
            fcsb_grishina_pred = bool(R > delta_grishina ** 2 * sr_X)
            fcsb_empirical_pred = bool(R > delta_empirical ** 2 * sr_X)

            return {
                "layer_name": name,
                "layer_type": layer_type,
                "shape": str(shape),
                "kernel_size": kernel_size,
                "R": R,
                "sr_X": sr_X,
                "delta_theory": delta_theory,
                "delta_grishina": delta_grishina,
                "delta_empirical": delta_empirical,
                "davis_pred": davis_pred,
                "fcsb_theory_pred": fcsb_theory_pred,
                "fcsb_grishina_pred": fcsb_grishina_pred,
                "fcsb_empirical_pred": fcsb_empirical_pred,
            }
    except SVDTimeout:
        return None


# ---------------------------------------------------------------------------
# Full scan at one epoch
# ---------------------------------------------------------------------------

_TIMEOUT_ROW_KEYS = [
    "R", "sr_X", "delta_theory", "delta_grishina", "delta_empirical",
    "davis_pred", "fcsb_theory_pred", "fcsb_grishina_pred", "fcsb_empirical_pred",
]


def run_scan(model, layers, recorder, device, epoch):
    """Run gradient geometry scan on all target layers. Returns list of row dicts."""
    rows = []
    timeouts = 0
    for name, mod in layers.items():
        act = recorder.activations.get(name)
        if act is None:
            continue
        result = scan_layer(name, mod, act)
        if result is None:
            timeouts += 1
            row = {
                "layer_name": name,
                "layer_type": "conv2d" if isinstance(mod, nn.Conv2d) else "linear",
                "shape": str(tuple(mod.weight.shape)),
                "kernel_size": mod.kernel_size[0] if isinstance(mod, nn.Conv2d) else 0,
                "epoch": epoch,
            }
            for k in _TIMEOUT_ROW_KEYS:
                row[k] = "TIMEOUT"
            rows.append(row)
        else:
            result["epoch"] = epoch
            rows.append(result)

    conv_rows = [r for r in rows if r["layer_type"] == "conv2d" and r["R"] != "TIMEOUT"]
    lin_rows = [r for r in rows if r["layer_type"] == "linear" and r["R"] != "TIMEOUT"]

    conv_davis = sum(1 for r in conv_rows if r["davis_pred"])
    lin_davis = sum(1 for r in lin_rows if r["davis_pred"])

    conv_reclass_theory = sum(1 for r in conv_rows if r["davis_pred"] and not r["fcsb_theory_pred"])
    conv_reclass_grishina = sum(1 for r in conv_rows if r["davis_pred"] and not r["fcsb_grishina_pred"])
    conv_reclass_empirical = sum(1 for r in conv_rows if r["davis_pred"] and not r["fcsb_empirical_pred"])
    lin_reclass_theory = sum(1 for r in lin_rows if r["davis_pred"] and not r["fcsb_theory_pred"])
    lin_reclass_grishina = sum(1 for r in lin_rows if r["davis_pred"] and not r["fcsb_grishina_pred"])
    lin_reclass_empirical = sum(1 for r in lin_rows if r["davis_pred"] and not r["fcsb_empirical_pred"])

    nc, nl = len(conv_rows), len(lin_rows)
    print(f"\n=== Epoch {epoch} Summary ===")
    if nc:
        print(f"Conv layers: {nc} total, Davis=True: {conv_davis} ({100*conv_davis/nc:.1f}%)")
        print(f"  Reclass theory:   {conv_reclass_theory}/{conv_davis} ({100*conv_reclass_theory/conv_davis:.1f}%)" if conv_davis else "")
        print(f"  Reclass grishina: {conv_reclass_grishina}/{conv_davis} ({100*conv_reclass_grishina/conv_davis:.1f}%)" if conv_davis else "")
        print(f"  Reclass empirical:{conv_reclass_empirical}/{conv_davis} ({100*conv_reclass_empirical/conv_davis:.1f}%)" if conv_davis else "")
    else:
        print("Conv layers: 0 total")
    if nl:
        print(f"Linear layers: {nl} total, Davis=True: {lin_davis} ({100*lin_davis/nl:.1f}%)")
    else:
        print("Linear layers: 0 total")
    print(f"Timeouts: {timeouts}")

    return rows, {
        "conv_total": nc, "lin_total": nl,
        "conv_davis": conv_davis, "lin_davis": lin_davis,
        "conv_reclass_theory": conv_reclass_theory,
        "conv_reclass_grishina": conv_reclass_grishina,
        "conv_reclass_empirical": conv_reclass_empirical,
        "lin_reclass_theory": lin_reclass_theory,
        "lin_reclass_grishina": lin_reclass_grishina,
        "lin_reclass_empirical": lin_reclass_empirical,
        "timeouts": timeouts,
    }


# ---------------------------------------------------------------------------
# Main training + scan loop
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Gradient geometry scan for spectral optimizer prediction")
    parser.add_argument("--model", type=str, default="resnet50", choices=["resnet50", "deit_small"])
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--scan-epochs", type=str, default="1,3,5",
                        help="Comma-separated epoch numbers to run scan")
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--weight-decay", type=float, default=0.05)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output-dir", type=str,
                        default="/root/spectral_optim_vision_geometry/results/")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    scan_epochs = set(int(x) for x in args.scan_epochs.split(","))
    set_seed(args.seed)

    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    # --- model ---
    model = get_model(args.model)
    model = model.to(device)
    print(f"Model: {args.model}, params: {sum(p.numel() for p in model.parameters())/1e6:.1f}M")

    # --- data ---
    loader = get_dataloader(args.batch_size)
    num_batches = len(loader)
    print(f"CIFAR-100 train: {len(loader.dataset)} images, {num_batches} batches")

    # --- optimizer ---
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    criterion = nn.CrossEntropyLoss()

    # --- target layers & hooks ---
    layers = collect_target_layers(model)
    print(f"Target layers: {len(layers)} (conv2d + linear)")
    recorder = ActivationRecorder(layers)

    # --- CSV setup ---
    os.makedirs(args.output_dir, exist_ok=True)
    csv_path = os.path.join(args.output_dir, f"gradient_geometry_{args.model}.csv")
    csv_fields = ["epoch", "layer_name", "layer_type", "shape", "kernel_size",
                  "R", "sr_X", "delta_theory", "delta_grishina", "delta_empirical",
                  "davis_pred", "fcsb_theory_pred", "fcsb_grishina_pred", "fcsb_empirical_pred"]
    all_rows = []
    all_stats = []

    # --- training loop ---
    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for batch_idx, (images, labels) in enumerate(loader, 1):
            images, labels = images.to(device), labels.to(device)

            is_scan_batch = (epoch in scan_epochs) and (batch_idx == num_batches)

            if is_scan_batch:
                recorder.clear()

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()

            if batch_idx % 50 == 0:
                print(f"  Epoch {epoch}/{args.epochs} [{batch_idx}/{num_batches}] "
                      f"loss={running_loss/batch_idx:.4f} acc={100.*correct/total:.1f}%")

            if is_scan_batch:
                print(f"\n--- Running gradient geometry scan at epoch {epoch} ---")
                t0 = time.time()
                rows, stats = run_scan(model, layers, recorder, device, epoch)
                elapsed = time.time() - t0
                print(f"Scan completed in {elapsed:.1f}s")
                all_rows.extend(rows)
                all_stats.append(stats)

        acc = 100. * correct / total
        avg_loss = running_loss / num_batches
        print(f"Epoch {epoch}/{args.epochs}: loss={avg_loss:.4f}, acc={acc:.1f}%")

    # --- write CSV ---
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"\nResults saved to {csv_path}")

    # --- final summary / pass-fail ---
    total_layers = sum(s["conv_total"] + s["lin_total"] for s in all_stats)
    total_timeouts = sum(s["timeouts"] for s in all_stats)
    total_computed = total_layers

    agg_conv_davis = sum(s["conv_davis"] for s in all_stats)
    agg_lin_davis = sum(s["lin_davis"] for s in all_stats)

    agg_conv_reclass_theory = sum(s["conv_reclass_theory"] for s in all_stats)
    agg_conv_reclass_grishina = sum(s["conv_reclass_grishina"] for s in all_stats)
    agg_conv_reclass_empirical = sum(s["conv_reclass_empirical"] for s in all_stats)

    agg_lin_reclass_theory = sum(s["lin_reclass_theory"] for s in all_stats)
    agg_lin_reclass_grishina = sum(s["lin_reclass_grishina"] for s in all_stats)
    agg_lin_reclass_empirical = sum(s["lin_reclass_empirical"] for s in all_stats)

    def pct(num, den):
        return (100. * num / den) if den > 0 else 0.0

    conv_pct_theory = pct(agg_conv_reclass_theory, agg_conv_davis)
    conv_pct_grishina = pct(agg_conv_reclass_grishina, agg_conv_davis)
    conv_pct_empirical = pct(agg_conv_reclass_empirical, agg_conv_davis)

    lin_pct_theory = pct(agg_lin_reclass_theory, agg_lin_davis)
    lin_pct_grishina = pct(agg_lin_reclass_grishina, agg_lin_davis)
    lin_pct_empirical = pct(agg_lin_reclass_empirical, agg_lin_davis)

    p1 = total_computed > 0 and total_timeouts < total_computed * 0.1

    p2_theory = conv_pct_theory >= 20.0
    p2_grishina = conv_pct_grishina >= 20.0
    p2_empirical = conv_pct_empirical >= 20.0
    p2 = p2_theory or p2_grishina or p2_empirical

    p3_theory = lin_pct_theory < 5.0
    p3_grishina = lin_pct_grishina < 5.0
    p3_empirical = lin_pct_empirical < 5.0
    p3 = p3_theory and p3_grishina and p3_empirical

    print(f"\n{'='*60}")
    print(f"=== Pass/Fail Criteria ===")
    print(f"P1 (SVD computable): {'PASS' if p1 else 'FAIL'} - "
          f"{total_computed}/{total_computed + total_timeouts} layers computed, "
          f"{total_timeouts} timeouts")

    print(f"\nP2 (>=20% conv reclassification, any delta):")
    print(f"  P2_theory   (d=sqrt(k)): {'PASS' if p2_theory else 'FAIL'} - "
          f"{agg_conv_reclass_theory}/{agg_conv_davis} ({conv_pct_theory:.1f}%)")
    print(f"  P2_grishina (d=k):       {'PASS' if p2_grishina else 'FAIL'} - "
          f"{agg_conv_reclass_grishina}/{agg_conv_davis} ({conv_pct_grishina:.1f}%)")
    print(f"  P2_empirical (d=emp):    {'PASS' if p2_empirical else 'FAIL'} - "
          f"{agg_conv_reclass_empirical}/{agg_conv_davis} ({conv_pct_empirical:.1f}%)")
    print(f"  P2 overall: {'PASS' if p2 else 'FAIL'}")

    passed_variants = []
    if p2_theory:
        passed_variants.append("theory(sqrt(k))")
    if p2_grishina:
        passed_variants.append("grishina(k)")
    if p2_empirical:
        passed_variants.append("empirical")
    if passed_variants:
        print(f"  >>> Passed via: {', '.join(passed_variants)}")

    print(f"\nP3 (<5% linear reclassification, all deltas):")
    print(f"  theory:    {'PASS' if p3_theory else 'FAIL'} ({lin_pct_theory:.1f}%)")
    print(f"  grishina:  {'PASS' if p3_grishina else 'FAIL'} ({lin_pct_grishina:.1f}%)")
    print(f"  empirical: {'PASS' if p3_empirical else 'FAIL'} ({lin_pct_empirical:.1f}%)")
    print(f"  P3 overall: {'PASS' if p3 else 'FAIL'}")
    print(f"{'='*60}")

    recorder.remove()


if __name__ == "__main__":
    main()
