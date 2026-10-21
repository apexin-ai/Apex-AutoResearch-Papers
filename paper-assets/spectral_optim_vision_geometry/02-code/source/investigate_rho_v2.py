"""Try all available AdamW checkpoint combinations to find rho=0.34/-0.66."""
import csv, json, os, numpy as np, torch, timm
from scipy import stats

BASE = "/root/spectral_optim_vision_geometry"
CKPT_DIR = "/root/autodl-tmp/checkpoints/spectral_optim"

def load_resnet_swap(path):
    data = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            data[row["layer_name"]] = float(row["muon_drop_pp"])
    return data

def load_deit_swap(path):
    data = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            if row["group_type"] == "component":
                data[row["group_name"]] = float(row["muon_drop_pp"])
    return data

def compute_per_layer_R(ckpt_path, timm_name):
    model = timm.create_model(timm_name, pretrained=False, num_classes=100)
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    sd = ckpt.get("state_dict", ckpt.get("model_state_dict", ckpt))
    model.load_state_dict(sd)
    metrics = {}
    for name, param in model.named_parameters():
        if "weight" not in name:
            continue
        w = param.data
        if w.ndim == 4:
            W = w.reshape(w.shape[0], -1)
        elif w.ndim == 2:
            W = w
        else:
            continue
        if min(W.shape) < 2:
            continue
        S = torch.linalg.svdvals(W.float())
        s1 = S[0].item()
        if s1 == 0:
            continue
        sr = (S**2).sum().item() / (s1**2)
        metrics[name] = {"sigma_1": s1, "stable_rank": sr, "R_l": s1/sr}
    return metrics

def correlate(muon_m, adamw_m, swap_data, swap_to_spec_fn):
    dr, dsr, drops, names = [], [], [], []
    for swap_name, drop in sorted(swap_data.items()):
        spec_name = swap_to_spec_fn(swap_name)
        if spec_name in muon_m and spec_name in adamw_m:
            dr.append(muon_m[spec_name]["R_l"] - adamw_m[spec_name]["R_l"])
            dsr.append(muon_m[spec_name]["stable_rank"] - adamw_m[spec_name]["stable_rank"])
            drops.append(drop)
            names.append(swap_name)
    dr, dsr, drops = np.array(dr), np.array(dsr), np.array(drops)
    rho_R, p_R = stats.spearmanr(dr, drops)
    rho_sr, p_sr = stats.spearmanr(dsr, drops)
    return {
        "n": len(drops),
        "delta_R": {"rho": round(float(rho_R), 4), "p": round(float(p_R), 6)},
        "delta_sr": {"rho": round(float(rho_sr), 4), "p": round(float(p_sr), 6)},
    }

def resnet_spec(swap_name):
    return swap_name + ".weight"

def deit_spec(swap_name):
    if swap_name.startswith("block_"):
        parts = swap_name.split(".", 1)
        block = parts[0].replace("block_", "blocks.")
        return f"{block}.{parts[1]}.weight" if len(parts) > 1 else f"{block}.weight"
    if swap_name == "patch_embed":
        return "patch_embed.proj.weight"
    return swap_name + ".weight"

# Muon checkpoints (only one set)
resnet_muon = compute_per_layer_R(f"{CKPT_DIR}/resnet50_muon_s42_best.pt", "resnet50")
deit_muon = compute_per_layer_R(f"{CKPT_DIR}/deit_small_muon_s42_best.pt", "deit_small_patch16_224")

# Weight swap data - both old and fairlr
resnet_swap_old = load_resnet_swap(f"{BASE}/results/resnet50_weight_swap.csv")
deit_swap_old = load_deit_swap(f"{BASE}/results/deit_weight_swap.csv")

# Try all available ResNet AdamW checkpoints
resnet_adamw_ckpts = [f for f in os.listdir(CKPT_DIR) if f.startswith("resnet50_adamw") and f.endswith("_best.pt")]
deit_adamw_ckpts = [f for f in os.listdir(CKPT_DIR) if f.startswith("deit_small_adamw") and f.endswith("_best.pt")]

print("=== Testing all ResNet-50 AdamW checkpoints ===")
for ckpt_name in sorted(resnet_adamw_ckpts):
    path = f"{CKPT_DIR}/{ckpt_name}"
    adamw = compute_per_layer_R(path, "resnet50")
    result = correlate(resnet_muon, adamw, resnet_swap_old, resnet_spec)
    print(f"  {ckpt_name}: ΔR rho={result['delta_R']['rho']:+.4f} (p={result['delta_R']['p']:.4f}), Δsr rho={result['delta_sr']['rho']:+.4f}")

# Also try fairlr swap data
if os.path.exists(f"{BASE}/results/fairlr/resnet50_weight_swap.csv"):
    resnet_swap_fairlr = load_resnet_swap(f"{BASE}/results/fairlr/resnet50_weight_swap.csv")
    print("\n=== With fairlr weight swap data ===")
    for ckpt_name in sorted(resnet_adamw_ckpts):
        path = f"{CKPT_DIR}/{ckpt_name}"
        adamw = compute_per_layer_R(path, "resnet50")
        result = correlate(resnet_muon, adamw, resnet_swap_fairlr, resnet_spec)
        print(f"  {ckpt_name}: ΔR rho={result['delta_R']['rho']:+.4f} (p={result['delta_R']['p']:.4f}), Δsr rho={result['delta_sr']['rho']:+.4f}")

print("\n=== Testing all DeiT-S AdamW checkpoints ===")
for ckpt_name in sorted(deit_adamw_ckpts):
    path = f"{CKPT_DIR}/{ckpt_name}"
    adamw = compute_per_layer_R(path, "deit_small_patch16_224")
    result = correlate(deit_muon, adamw, deit_swap_old, deit_spec)
    print(f"  {ckpt_name}: ΔR rho={result['delta_R']['rho']:+.4f} (p={result['delta_R']['p']:.4f}), Δsr rho={result['delta_sr']['rho']:+.4f}")

# Also try fairlr DeiT swap
if os.path.exists(f"{BASE}/results/fairlr/deit_weight_swap.csv"):
    deit_swap_fairlr = load_deit_swap(f"{BASE}/results/fairlr/deit_weight_swap.csv")
    print("\n=== DeiT with fairlr weight swap data ===")
    for ckpt_name in sorted(deit_adamw_ckpts):
        path = f"{CKPT_DIR}/{ckpt_name}"
        adamw = compute_per_layer_R(path, "deit_small_patch16_224")
        result = correlate(deit_muon, adamw, deit_swap_fairlr, deit_spec)
        print(f"  {ckpt_name}: ΔR rho={result['delta_R']['rho']:+.4f} (p={result['delta_R']['p']:.4f}), Δsr rho={result['delta_sr']['rho']:+.4f}")

# Also output per-layer data for the best-matching combination
print("\n=== Per-layer data for primary analysis (muon_best vs adamw_lr1e-3_best, old swap) ===")
resnet_adamw = compute_per_layer_R(f"{CKPT_DIR}/resnet50_adamw_s42_lr1e-3_best.pt", "resnet50")
deit_adamw = compute_per_layer_R(f"{CKPT_DIR}/deit_small_adamw_s42_lr1e-4_best.pt", "deit_small_patch16_224")

print("\nResNet-50 per-layer (ΔR_l, Δa_l):")
resnet_data = []
for swap_name in sorted(resnet_swap_old.keys()):
    spec_name = resnet_spec(swap_name)
    if spec_name in resnet_muon and spec_name in resnet_adamw:
        dr = resnet_muon[spec_name]["R_l"] - resnet_adamw[spec_name]["R_l"]
        da = resnet_swap_old[swap_name]
        resnet_data.append({"layer": swap_name, "delta_R": round(dr, 6), "delta_a": da})
        
print(json.dumps(resnet_data, indent=2))

print("\nDeiT-S per-layer (ΔR_l, Δa_l):")
deit_data = []
for swap_name in sorted(deit_swap_old.keys()):
    spec_name = deit_spec(swap_name)
    if spec_name in deit_muon and spec_name in deit_adamw:
        dr = deit_muon[spec_name]["R_l"] - deit_adamw[spec_name]["R_l"]
        da = deit_swap_old[swap_name]
        deit_data.append({"layer": swap_name, "delta_R": round(dr, 6), "delta_a": da})

print(json.dumps(deit_data, indent=2))
