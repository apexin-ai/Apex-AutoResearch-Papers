import csv
import os
import random
import time
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms
import timm
from scipy import stats

CIFAR100_MEAN = (0.5071, 0.4867, 0.4408)
CIFAR100_STD = (0.2675, 0.2565, 0.2761)

MUON_CKPT = "/root/autodl-tmp/checkpoints/spectral_optim/resnet50_muon_s42_best.pt"
ADAMW_CKPT = "/root/autodl-tmp/checkpoints/spectral_optim/resnet50_adamw_s42_lr1e-3_best.pt"
DATA_DIR = "/root/spectral_optim_vision_geometry/data"
OUTPUT_DIR = "/root/spectral_optim_vision_geometry/results"


def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def get_val_loader(data_dir, batch_size=256, num_workers=4):
    tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
    ])
    ds = datasets.CIFAR100(root=data_dir, train=False, download=True, transform=tf)
    return DataLoader(ds, batch_size=batch_size, shuffle=False,
                      num_workers=num_workers, pin_memory=True)


def get_train_loader_for_bn(data_dir, n_samples=10000, batch_size=128, num_workers=4):
    tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(CIFAR100_MEAN, CIFAR100_STD),
    ])
    ds = datasets.CIFAR100(root=data_dir, train=True, download=True, transform=tf)
    indices = list(range(min(n_samples, len(ds))))
    subset = Subset(ds, indices)
    return DataLoader(subset, batch_size=batch_size, shuffle=False,
                      num_workers=num_workers, pin_memory=True)


def load_state_dict(ckpt_path):
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    if isinstance(ckpt, dict) and "state_dict" in ckpt:
        return ckpt["state_dict"]
    return ckpt


def create_model(num_classes=100):
    return timm.create_model("resnet50", pretrained=False, num_classes=num_classes)


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct, total = 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        correct += (model(images).argmax(1) == labels).sum().item()
        total += labels.size(0)
    return 100.0 * correct / total


def recalibrate_bn(model, train_loader, device):
    for m in model.modules():
        if isinstance(m, (nn.BatchNorm2d, nn.BatchNorm1d)):
            m.reset_running_stats()
    model.train()
    with torch.no_grad():
        for images, _ in train_loader:
            images = images.to(device)
            model(images)
    model.eval()


def stable_rank(weight):
    W = weight.float()
    if W.dim() > 2:
        W = W.reshape(W.shape[0], -1)
    fro_sq = torch.sum(W ** 2).item()
    s = torch.linalg.svdvals(W)
    spec_sq = (s[0] ** 2).item()
    if spec_sq == 0:
        return 0.0
    return fro_sq / spec_sq


def get_swappable_modules(model):
    modules = {}
    for name, mod in model.named_modules():
        if isinstance(mod, nn.Conv2d):
            modules[name] = (mod, "conv")
        elif isinstance(mod, nn.Linear):
            modules[name] = (mod, "linear")
    return modules


def main():
    set_seed(42)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}", flush=True)

    muon_sd = load_state_dict(MUON_CKPT)
    adamw_sd = load_state_dict(ADAMW_CKPT)
    print(f"Loaded: muon={len(muon_sd)} keys, adamw={len(adamw_sd)} keys", flush=True)

    val_loader = get_val_loader(DATA_DIR)
    train_loader_bn = get_train_loader_for_bn(DATA_DIR, n_samples=10000, batch_size=128)
    print(f"Val: {len(val_loader.dataset)}, BN recal: {len(train_loader_bn.dataset)}", flush=True)

    # Verify baselines
    muon_model = create_model().to(device)
    muon_model.load_state_dict(muon_sd)
    muon_baseline = evaluate(muon_model, val_loader, device)
    print(f"Muon baseline: {muon_baseline:.2f}%", flush=True)

    adamw_model = create_model().to(device)
    adamw_model.load_state_dict(adamw_sd)
    adamw_baseline = evaluate(adamw_model, val_loader, device)
    print(f"AdamW baseline: {adamw_baseline:.2f}%", flush=True)

    if muon_baseline < 70 or adamw_baseline < 60:
        print("ABORT: Baseline accuracy too low — checkpoint or model mismatch.", flush=True)
        return

    modules = get_swappable_modules(muon_model)
    n_modules = len(modules)
    print(f"Swappable modules: {n_modules}\n", flush=True)

    del muon_model, adamw_model
    torch.cuda.empty_cache()

    results = []
    t0 = time.time()

    for i, (module_name, (mod, ltype)) in enumerate(modules.items(), 1):
        weight_key = f"{module_name}.weight"
        sr_muon = stable_rank(muon_sd[weight_key])
        sr_adamw = stable_rank(adamw_sd[weight_key])
        sr_div = abs(sr_muon - sr_adamw)

        # --- Without BN recalibration ---
        model = create_model().to(device)
        model.load_state_dict(muon_sd)
        param_dict = dict(model.named_parameters())
        swapped = False
        for suffix in ("weight", "bias"):
            key = f"{module_name}.{suffix}"
            if key in adamw_sd and key in param_dict:
                param_dict[key].data.copy_(adamw_sd[key])
                swapped = True
        if not swapped:
            del model; torch.cuda.empty_cache()
            continue

        acc_no_recal = evaluate(model, val_loader, device)
        drop_no_recal = muon_baseline - acc_no_recal
        del model; torch.cuda.empty_cache()

        # --- With BN recalibration ---
        model = create_model().to(device)
        model.load_state_dict(muon_sd)
        param_dict = dict(model.named_parameters())
        for suffix in ("weight", "bias"):
            key = f"{module_name}.{suffix}"
            if key in adamw_sd and key in param_dict:
                param_dict[key].data.copy_(adamw_sd[key])

        recalibrate_bn(model, train_loader_bn, device)
        acc_recal = evaluate(model, val_loader, device)
        drop_recal = muon_baseline - acc_recal
        del model; torch.cuda.empty_cache()

        results.append({
            "layer_name": module_name,
            "layer_type": ltype,
            "sr_muon": sr_muon,
            "sr_adamw": sr_adamw,
            "sr_divergence": sr_div,
            "acc_no_recal": acc_no_recal,
            "drop_no_recal": drop_no_recal,
            "acc_recal": acc_recal,
            "drop_recal": drop_recal,
        })

        elapsed = time.time() - t0
        print(f"  [{i}/{n_modules}] {module_name} ({ltype}): "
              f"SR_div={sr_div:.2f}  drop_orig={drop_no_recal:+.2f}pp  "
              f"drop_recal={drop_recal:+.2f}pp  [{elapsed:.0f}s]", flush=True)

    # Spearman correlations
    sr_divs = [r["sr_divergence"] for r in results]
    drops_orig = [r["drop_no_recal"] for r in results]
    drops_recal = [r["drop_recal"] for r in results]

    rho_orig, p_orig = stats.spearmanr(sr_divs, drops_orig)
    rho_recal, p_recal = stats.spearmanr(sr_divs, drops_recal)

    print(f"\n{'='*60}")
    print(f"Muon baseline: {muon_baseline:.2f}%")
    print(f"AdamW baseline: {adamw_baseline:.2f}%")
    print(f"Layers: {len(results)}")
    print(f"\nSpearman rho (SR_divergence vs accuracy_drop):")
    print(f"  Original (no BN recal):  rho={rho_orig:.4f}  p={p_orig:.4e}")
    print(f"  After BN recalibration:  rho={rho_recal:.4f}  p={p_recal:.4e}")
    print(f"{'='*60}")

    # Save CSV
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    csv_path = os.path.join(OUTPUT_DIR, "resnet50_bn_recal_ablation.csv")
    fields = ["layer_name", "layer_type", "sr_muon", "sr_adamw", "sr_divergence",
              "acc_no_recal", "drop_no_recal", "acc_recal", "drop_recal"]
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in results:
            row = {k: (f"{v:.4f}" if isinstance(v, float) else v) for k, v in r.items()}
            writer.writerow(row)

    print(f"\nSaved: {csv_path}")
    print(f"Time: {time.time() - t0:.0f}s")
    print(f"BN_RECAL_COMPLETE n_layers={len(results)} rho_orig={rho_orig:.4f} rho_recal={rho_recal:.4f} p_recal={p_recal:.4e}")


if __name__ == "__main__":
    main()
