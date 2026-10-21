"""Gradient direction cosine similarity analysis (D215a supplement).

Analyzes gradient direction consistency and Newton-Schulz update alignment across
Muon/AdamW/SOAP x ResNet50-BN/LN checkpoints on CIFAR-100 validation set.

Method:
  1. Load trained checkpoint, compute per-layer gradients over N mini-batches
  2. Pairwise cosine similarity between batch gradients (direction consistency)
  3. Cosine similarity between raw gradient and Newton-Schulz orthogonalized gradient
     (quantifies how much Muon's core operation changes the gradient direction)
  4. Aggregate by depth group (stem/layer1-4/head), compare BN vs LN

Key hypothesis under test:
  Muon's advantage may come from gradient direction orthogonalization rather than
  amplitude correction. If true, NS alignment and gradient consistency should differ
  systematically across BN/LN in a way that explains performance gaps.
"""

import json
import os
import random
from collections import defaultdict

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import timm

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CKPT_DIR = "/root/autodl-tmp/checkpoints/spectral_optim"
DATA_ROOT = "/root/spectral_optim_vision_geometry/data"
OUTPUT_DIR = "/root/spectral_optim_vision_geometry"
DEVICE = "cuda:0"
N_BATCHES = 15
BATCH_SIZE = 64
SEED = 42

CHECKPOINTS = [
    ("resnet50",    "muon",  "resnet50_muon_s42_best.pt"),
    ("resnet50",    "adamw", "resnet50_adamw_s42_lr1e-3_best.pt"),
    ("resnet50",    "soap",  "resnet50_soap_s42_lr1e-2_best.pt"),
    ("resnet50_ln", "muon",  "resnet50_ln_muon_s42_best.pt"),
    ("resnet50_ln", "adamw", "resnet50_ln_adamw_s42_lr1e-3_best.pt"),
]

CIFAR100_MEAN = (0.5071, 0.4867, 0.4408)
CIFAR100_STD  = (0.2675, 0.2565, 0.2761)

DEPTH_ORDER = ["stem", "layer1", "layer2", "layer3", "layer4", "head"]


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def replace_bn_with_gn(module, num_groups=1):
    """Replace all BatchNorm2d with GroupNorm(1, C) -- equivalent to LayerNorm."""
    for name, child in module.named_children():
        if isinstance(child, nn.BatchNorm2d):
            setattr(module, name, nn.GroupNorm(num_groups, child.num_features))
        else:
            replace_bn_with_gn(child, num_groups)


def load_checkpoint(ckpt_path, model_name, device):
    """Load checkpoint and build matching model architecture."""
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    sd = ckpt["state_dict"] if "state_dict" in ckpt else ckpt
    needs_gn = not any("running_mean" in k for k in sd.keys())
    model = timm.create_model("resnet50", pretrained=False, num_classes=100)
    if needs_gn or model_name == "resnet50_ln":
        replace_bn_with_gn(model, num_groups=1)
    model = model.to(device)
    model.load_state_dict(sd)
    model.eval()
    return model, ckpt.get("val_acc", None)


def get_val_loader(batch_size, num_workers=4):
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
    ])
    ds = torchvision.datasets.CIFAR100(
        root=DATA_ROOT, train=False, download=True, transform=transform)
    return torch.utils.data.DataLoader(
        ds, batch_size=batch_size, shuffle=True,
        num_workers=num_workers, pin_memory=True, drop_last=True)


def get_depth_group(name):
    """Map layer name to depth group."""
    if name.startswith("conv1"):
        return "stem"
    for i in range(1, 5):
        if name.startswith("layer%d" % i):
            return "layer%d" % i
    if name.startswith("fc"):
        return "head"
    return "other"


def collect_weight_layers(model):
    """Return {name: module} for Conv2d and Linear layers."""
    layers = {}
    for name, mod in model.named_modules():
        if isinstance(mod, (nn.Conv2d, nn.Linear)):
            layers[name] = mod
    return layers


# ---------------------------------------------------------------------------
# Newton-Schulz orthogonalization (Muon's core operation)
# ---------------------------------------------------------------------------

def newton_schulz_5(G):
    """Quintic Newton-Schulz iteration for polar decomposition.

    For G = U Sigma V^T, converges to U V^T (closest orthogonal matrix).
    Uses the same polynomial coefficients as the Muon optimizer.
    """
    a, b, c = 3.4445, -4.7750, 2.0315
    X = G.float() / (G.float().norm() + 1e-7)
    transposed = False
    if X.shape[0] > X.shape[1]:
        X = X.T
        transposed = True
    for _ in range(5):
        A = X @ X.T
        B = A @ A
        X = a * X + b * (A @ X) + c * (B @ X)
    if transposed:
        X = X.T
    return X


def grad_to_2d(grad, module):
    """Reshape gradient to 2D for NS computation."""
    if isinstance(module, nn.Conv2d):
        return grad.reshape(grad.shape[0], -1)
    return grad


# ---------------------------------------------------------------------------
# Gradient computation
# ---------------------------------------------------------------------------

def compute_batch_gradients(model, loader, device, n_batches):
    """Compute per-layer gradients for n_batches.

    Returns:
        grads: {layer_name: [grad_cpu_tensor, ...]}
        layers: {layer_name: module}
    """
    criterion = nn.CrossEntropyLoss()
    layers = collect_weight_layers(model)
    all_grads = defaultdict(list)

    batch_iter = iter(loader)
    for _ in range(n_batches):
        try:
            images, labels = next(batch_iter)
        except StopIteration:
            batch_iter = iter(loader)
            images, labels = next(batch_iter)

        images, labels = images.to(device), labels.to(device)
        model.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()

        for name, mod in layers.items():
            if mod.weight.grad is not None:
                all_grads[name].append(
                    mod.weight.grad.detach().float().cpu().clone())

        del images, labels, outputs, loss
        torch.cuda.empty_cache()

    return dict(all_grads), layers


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def pairwise_cosine(grads):
    """Mean and std of pairwise cosine similarity for a list of gradient tensors."""
    n = len(grads)
    if n < 2:
        return float("nan"), float("nan")
    flat = [g.flatten() for g in grads]
    sims = []
    for i in range(n):
        for j in range(i + 1, n):
            cos = F.cosine_similarity(
                flat[i].unsqueeze(0), flat[j].unsqueeze(0)).item()
            sims.append(cos)
    return float(np.mean(sims)), float(np.std(sims))


def ns_alignment(grad, module):
    """Cosine similarity between raw gradient and its NS-orthogonalized version."""
    grad_2d = grad_to_2d(grad, module)
    if grad_2d.ndim != 2:
        return float("nan")
    ns = newton_schulz_5(grad_2d)
    return F.cosine_similarity(
        grad_2d.flatten().unsqueeze(0), ns.flatten().unsqueeze(0)).item()


# ---------------------------------------------------------------------------
# Per-checkpoint analysis
# ---------------------------------------------------------------------------

def analyze_one(model_name, opt_name, ckpt_file, loader, device, n_batches):
    """Full gradient direction analysis for one checkpoint."""
    ckpt_path = os.path.join(CKPT_DIR, ckpt_file)
    print("\n" + "=" * 70)
    print("%s / %s  (%s)" % (model_name, opt_name, ckpt_file))

    model, val_acc = load_checkpoint(ckpt_path, model_name, device)
    print("  val_acc=%s  |  computing %d batch gradients ..." % (val_acc, n_batches))

    grads, layers = compute_batch_gradients(model, loader, device, n_batches)

    layer_results = {}
    for name in sorted(grads.keys()):
        gs = grads[name]
        mod = layers[name]

        mean_cos, std_cos = pairwise_cosine(gs)
        ns_vals = [ns_alignment(g, mod) for g in gs]
        mean_ns = float(np.mean(ns_vals))
        std_ns = float(np.std(ns_vals))

        mean_grad = torch.stack(gs).mean(0)
        ns_of_mean = ns_alignment(mean_grad, mod)

        gnorms = [g.flatten().norm().item() for g in gs]

        layer_results[name] = {
            "depth": get_depth_group(name),
            "shape": list(gs[0].shape),
            "n_params": int(gs[0].numel()),
            "grad_consistency_mean": mean_cos,
            "grad_consistency_std": std_cos,
            "ns_alignment_mean": mean_ns,
            "ns_alignment_std": std_ns,
            "ns_alignment_of_mean_grad": ns_of_mean,
            "grad_norm_mean": float(np.mean(gnorms)),
            "grad_norm_cv": float(np.std(gnorms) / (np.mean(gnorms) + 1e-12)),
        }

    del grads, model
    torch.cuda.empty_cache()

    # --- Depth aggregation ---
    depth_data = defaultdict(
        lambda: {"cons": [], "ns": [], "norm": [], "n_params": 0})
    for name, r in layer_results.items():
        d = r["depth"]
        depth_data[d]["cons"].append(r["grad_consistency_mean"])
        depth_data[d]["ns"].append(r["ns_alignment_mean"])
        depth_data[d]["norm"].append(r["grad_norm_mean"])
        depth_data[d]["n_params"] += r["n_params"]

    depth_summary = {}
    print("\n  %-8s %4s %12s %10s %12s" % ("Depth", "#Ly", "Consistency", "NS-align", "GradNorm"))
    print("  " + "-" * 50)
    for d in DEPTH_ORDER:
        if d not in depth_data:
            continue
        dd = depth_data[d]
        depth_summary[d] = {
            "n_layers": len(dd["cons"]),
            "n_params": dd["n_params"],
            "consistency_mean": float(np.mean(dd["cons"])),
            "consistency_std": float(np.std(dd["cons"])),
            "ns_alignment_mean": float(np.mean(dd["ns"])),
            "ns_alignment_std": float(np.std(dd["ns"])),
            "grad_norm_mean": float(np.mean(dd["norm"])),
        }
        s = depth_summary[d]
        print("  %-8s %4d %12.4f %10.4f %12.6f" % (
            d, s["n_layers"], s["consistency_mean"],
            s["ns_alignment_mean"], s["grad_norm_mean"]))

    all_cons = [r["grad_consistency_mean"] for r in layer_results.values()]
    all_ns = [r["ns_alignment_mean"] for r in layer_results.values()]
    oc = float(np.mean(all_cons))
    on = float(np.mean(all_ns))
    print("\n  Overall: consistency=%.4f  NS-align=%.4f" % (oc, on))

    return {
        "model": model_name,
        "optimizer": opt_name,
        "val_acc": val_acc,
        "overall_consistency": oc,
        "overall_ns_alignment": on,
        "depth_summary": depth_summary,
        "per_layer": layer_results,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    set_seed(SEED)
    device = torch.device(DEVICE)
    print("Device: %s" % device)
    print("Config: N_BATCHES=%d, BATCH_SIZE=%d, SEED=%d" % (N_BATCHES, BATCH_SIZE, SEED))

    loader = get_val_loader(BATCH_SIZE)
    print("CIFAR-100 val: %d images, %d batches" % (len(loader.dataset), len(loader)))

    results = {}
    for model_name, opt_name, ckpt_file in CHECKPOINTS:
        key = "%s_%s" % (model_name, opt_name)
        results[key] = analyze_one(
            model_name, opt_name, ckpt_file, loader, device, N_BATCHES)

    # === Comparative summary ===
    print("\n" + "=" * 70)
    print("COMPARATIVE SUMMARY")
    print("=" * 70)

    print("\n%-25s %6s %12s %10s" % ("Config", "Acc", "Consistency", "NS-align"))
    print("-" * 55)
    for key, r in results.items():
        print("%-25s %6.2f %12.4f %10.4f" % (
            key, r["val_acc"], r["overall_consistency"], r["overall_ns_alignment"]))

    # --- BN vs LN delta ---
    print("\n--- BN vs LN Delta ---")
    for opt in ["muon", "adamw"]:
        bk = "resnet50_%s" % opt
        lk = "resnet50_ln_%s" % opt
        if bk not in results or lk not in results:
            continue
        bn, ln = results[bk], results[lk]
        dc = ln["overall_consistency"] - bn["overall_consistency"]
        dn = ln["overall_ns_alignment"] - bn["overall_ns_alignment"]
        print("\n  %s: consistency D(LN-BN)=%+.4f  NS-align D(LN-BN)=%+.4f" % (
            opt.upper(), dc, dn))

        print("    %-8s %8s %8s %7s | %7s %7s %7s" % (
            "Depth", "BN_cons", "LN_cons", "D", "BN_NS", "LN_NS", "D"))
        for d in DEPTH_ORDER:
            if d in bn["depth_summary"] and d in ln["depth_summary"]:
                bc = bn["depth_summary"][d]["consistency_mean"]
                lc = ln["depth_summary"][d]["consistency_mean"]
                bns = bn["depth_summary"][d]["ns_alignment_mean"]
                lns = ln["depth_summary"][d]["ns_alignment_mean"]
                print("    %-8s %8.4f %8.4f %+7.4f | %7.4f %7.4f %+7.4f" % (
                    d, bc, lc, lc - bc, bns, lns, lns - bns))

    # --- Cross-optimizer comparison within same norm ---
    print("\n--- Cross-optimizer comparison (same norm) ---")
    for norm in ["resnet50", "resnet50_ln"]:
        norm_keys = [k for k in results
                     if results[k]["model"] == norm]
        if len(norm_keys) < 2:
            continue
        print("\n  %s:" % norm)
        print("    %-10s %6s %12s %10s" % ("Optimizer", "Acc", "Consistency", "NS-align"))
        for k in sorted(norm_keys):
            r = results[k]
            print("    %-10s %6.2f %12.4f %10.4f" % (
                r["optimizer"], r["val_acc"],
                r["overall_consistency"], r["overall_ns_alignment"]))

    # Save JSON
    out_path = os.path.join(OUTPUT_DIR, "gradient_direction_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print("\nResults saved to %s" % out_path)


if __name__ == "__main__":
    main()
