"""Investigate the source of rho=0.34 / -0.66 claimed in the paper.

Computes Spearman rho(metric, weight_swap) for every possible metric:
1. delta_stable_rank from spectral_metrics.csv
2. delta_spectral_gap
3. delta_condition_number
4. delta_effective_rank
5. delta_spectral_decay
6. FCSB_margin from gradient_geometry (reproducing old code)
7. spectral_response_ratio R_l = sigma_1/sr from checkpoints (paper definition)
"""

import csv
import json
import os
import sys
import numpy as np
from scipy import stats

BASE = "/root/spectral_optim_vision_geometry"
CKPT_DIR = "/root/autodl-tmp/checkpoints/spectral_optim"

# ============================================================
# Part 1: Load spectral_metrics.csv
# ============================================================
def load_spectral_metrics(path):
    """Returns dict: model_name -> {layer_name -> {metric: value}}"""
    data = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            model = row["model_name"]
            layer = row["layer_name"]
            if model not in data:
                data[model] = {}
            data[model][layer] = {
                "condition_number": float(row["condition_number"]),
                "effective_rank": float(row["effective_rank"]),
                "stable_rank": float(row["stable_rank"]),
                "spectral_gap": float(row["spectral_gap"]),
                "spectral_decay_exponent": float(row["spectral_decay_exponent"]),
                "layer_type": row["layer_type"],
            }
    return data

# ============================================================
# Part 2: Load weight swap CSVs
# ============================================================
def load_resnet_swap(path):
    """layer_name -> muon_drop_pp"""
    data = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            # muon_drop_pp = how much accuracy drops when replacing muon layer with adamw
            data[row["layer_name"]] = float(row["muon_drop_pp"])
    return data

def load_deit_swap(path):
    """group_name -> muon_drop_pp (component level only)"""
    data = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            if row["group_type"] == "component":
                data[row["group_name"]] = float(row["muon_drop_pp"])
    return data

def deit_swap_to_spectral(swap_name):
    """Convert DeiT swap group_name (block_X.Y) to spectral_metrics layer_name (blocks.X.Y.weight)"""
    if swap_name.startswith("block_"):
        parts = swap_name.split(".", 1)
        block_part = parts[0].replace("block_", "blocks.")
        if len(parts) > 1:
            return f"{block_part}.{parts[1]}.weight"
        return f"{block_part}.weight"
    if swap_name == "patch_embed":
        return "patch_embed.proj.weight"
    return swap_name + ".weight"

# ============================================================
# Part 3: Compute deltas and correlations from spectral_metrics
# ============================================================
def compute_deltas_from_csv():
    spec = load_spectral_metrics(f"{BASE}/results/spectral_analysis/spectral_metrics.csv")
    
    metrics_to_test = ["stable_rank", "spectral_gap", "condition_number", 
                       "effective_rank", "spectral_decay_exponent"]
    
    results = {}
    
    # --- ResNet-50 ---
    resnet_swap = load_resnet_swap(f"{BASE}/results/resnet50_weight_swap.csv")
    resnet_muon = spec.get("resnet50_muon", {})
    resnet_adamw = spec.get("resnet50_adamw", {})
    
    matched_resnet = sorted(set(resnet_muon.keys()) & set(resnet_adamw.keys()))
    # Match with swap data (swap uses names without .weight suffix)
    swap_matched_resnet = []
    for layer in matched_resnet:
        swap_name = layer.replace(".weight", "")
        if swap_name in resnet_swap:
            swap_matched_resnet.append((layer, swap_name))
    
    print(f"ResNet-50: {len(matched_resnet)} spectral layers, {len(swap_matched_resnet)} matched with swap")
    
    resnet_results = {"n_matched": len(swap_matched_resnet)}
    for metric in metrics_to_test:
        deltas = []
        drops = []
        layer_names = []
        for spec_name, swap_name in swap_matched_resnet:
            delta = resnet_muon[spec_name][metric] - resnet_adamw[spec_name][metric]
            drop = resnet_swap[swap_name]
            deltas.append(delta)
            drops.append(drop)
            layer_names.append(swap_name)
        
        deltas = np.array(deltas)
        drops = np.array(drops)
        rho, p = stats.spearmanr(deltas, drops)
        resnet_results[f"delta_{metric}"] = {
            "rho": round(float(rho), 4),
            "p": round(float(p), 6),
        }
        print(f"  ResNet delta_{metric}: rho={rho:+.4f}, p={p:.6f}")
    
    results["resnet50_csv_metrics"] = resnet_results
    
    # --- DeiT-S ---
    deit_swap = load_deit_swap(f"{BASE}/results/deit_weight_swap.csv")
    deit_muon = spec.get("deit_small_muon", {})
    deit_adamw = spec.get("deit_small_adamw", {})
    
    matched_deit_spec = sorted(set(deit_muon.keys()) & set(deit_adamw.keys()))
    
    # Match with swap data
    swap_matched_deit = []
    for swap_name in sorted(deit_swap.keys()):
        spec_name = deit_swap_to_spectral(swap_name)
        if spec_name in deit_muon and spec_name in deit_adamw:
            swap_matched_deit.append((spec_name, swap_name))
    
    print(f"\nDeiT-S: {len(matched_deit_spec)} spectral layers, {len(swap_matched_deit)} matched with swap")
    
    deit_results = {"n_matched": len(swap_matched_deit)}
    for metric in metrics_to_test:
        deltas = []
        drops = []
        layer_names = []
        for spec_name, swap_name in swap_matched_deit:
            delta = deit_muon[spec_name][metric] - deit_adamw[spec_name][metric]
            drop = deit_swap[swap_name]
            deltas.append(delta)
            drops.append(drop)
            layer_names.append(swap_name)
        
        deltas = np.array(deltas)
        drops = np.array(drops)
        rho, p = stats.spearmanr(deltas, drops)
        deit_results[f"delta_{metric}"] = {
            "rho": round(float(rho), 4),
            "p": round(float(p), 6),
        }
        print(f"  DeiT delta_{metric}: rho={rho:+.4f}, p={p:.6f}")
    
    results["deit_s_csv_metrics"] = deit_results
    return results, swap_matched_resnet, swap_matched_deit

# ============================================================
# Part 4: FCSB margin correlation (reproduce old code)
# ============================================================
def compute_fcsb_correlation():
    print("\n--- FCSB margin correlation (reproducing old code) ---")
    
    results = {}
    
    # ResNet-50
    scan_data = {}
    with open(f"{BASE}/results/gradient_geometry_resnet50.csv") as f:
        for row in csv.DictReader(f):
            scan_data[(int(row["epoch"]), row["layer_name"])] = {
                "R": float(row["R"]),
                "sr_X": float(row["sr_X"]),
                "delta_grishina": float(row["delta_grishina"]),
            }
    
    resnet_swap = load_resnet_swap(f"{BASE}/results/resnet50_weight_swap.csv")
    
    for epoch in [1, 3, 5]:
        margins, drops = [], []
        for layer, drop in resnet_swap.items():
            key = (epoch, layer)
            if key in scan_data:
                row = scan_data[key]
                m = row["R"] / (row["delta_grishina"] ** 2 * row["sr_X"])
                if np.isfinite(m):
                    margins.append(m)
                    drops.append(drop)
        
        margins = np.array(margins)
        drops = np.array(drops)
        rho, p = stats.spearmanr(margins, drops)
        results[f"resnet50_fcsb_ep{epoch}"] = {"rho": round(float(rho), 4), "p": round(float(p), 6), "n": len(margins)}
        print(f"  ResNet FCSB_grishina ep{epoch}: rho={rho:+.4f}, p={p:.6f}, n={len(margins)}")
    
    # DeiT-S
    deit_scan = {}
    with open(f"{BASE}/results/gradient_geometry_deit_small.csv") as f:
        for row in csv.DictReader(f):
            deit_scan[(int(row["epoch"]), row["layer_name"])] = {
                "R": float(row["R"]),
                "sr_X": float(row["sr_X"]),
                "delta_grishina": float(row["delta_grishina"]),
            }
    
    deit_swap = load_deit_swap(f"{BASE}/results/deit_weight_swap.csv")
    
    def deit_swap_to_scan(swap_name):
        import re
        m = re.match(r"block_(\d+)\.(.*)", swap_name)
        if m:
            return f"blocks.{m.group(1)}.{m.group(2)}"
        if swap_name == "patch_embed":
            return "patch_embed.proj"
        return swap_name
    
    for epoch in [1, 3, 5]:
        margins, drops = [], []
        for swap_name, drop in deit_swap.items():
            scan_name = deit_swap_to_scan(swap_name)
            key = (epoch, scan_name)
            if key in deit_scan:
                row = deit_scan[key]
                m = row["R"] / (row["delta_grishina"] ** 2 * row["sr_X"])
                if np.isfinite(m):
                    margins.append(m)
                    drops.append(drop)
        
        margins = np.array(margins)
        drops = np.array(drops)
        rho, p = stats.spearmanr(margins, drops)
        results[f"deit_fcsb_ep{epoch}"] = {"rho": round(float(rho), 4), "p": round(float(p), 6), "n": len(margins)}
        print(f"  DeiT FCSB_grishina ep{epoch}: rho={rho:+.4f}, p={p:.6f}, n={len(margins)}")
    
    return results

# ============================================================
# Part 5: Compute R_l = sigma_1 / stable_rank from checkpoints
# ============================================================
def compute_spectral_response_from_checkpoints():
    print("\n--- Computing spectral_response_ratio from checkpoints ---")
    
    import torch
    import timm
    
    # Map to actual checkpoint files
    models = {
        "resnet50_muon": {
            "ckpt": f"{CKPT_DIR}/resnet50_muon_s42_best.pt",
            "timm_name": "resnet50",
        },
        "resnet50_adamw": {
            "ckpt": f"{CKPT_DIR}/resnet50_adamw_s42_lr1e-3_best.pt",
            "timm_name": "resnet50",
        },
        "deit_small_muon": {
            "ckpt": f"{CKPT_DIR}/deit_small_muon_s42_best.pt",
            "timm_name": "deit_small_patch16_224",
        },
        "deit_small_adamw": {
            "ckpt": f"{CKPT_DIR}/deit_small_adamw_s42_lr1e-4_best.pt",
            "timm_name": "deit_small_patch16_224",
        },
    }
    
    # Also try the old checkpoint naming
    old_ckpt_dir = "/root/autodl-tmp/checkpoints/spectral_optim"
    
    all_metrics = {}
    
    for model_name, config in models.items():
        ckpt_path = config["ckpt"]
        if not os.path.exists(ckpt_path):
            print(f"  WARNING: {ckpt_path} not found, trying alternatives...")
            # Try alternative names
            alt_names = [
                ckpt_path.replace("_best.pt", "_ep20.pt"),
                ckpt_path.replace("_s42_lr1e-3_best.pt", "_s42.pt"),
                ckpt_path.replace("_s42_lr1e-4_best.pt", "_s42.pt"),
            ]
            found = False
            for alt in alt_names:
                if os.path.exists(alt):
                    ckpt_path = alt
                    found = True
                    break
            if not found:
                print(f"  SKIP: no checkpoint found for {model_name}")
                continue
        
        print(f"  Loading {model_name} from {ckpt_path}...")
        model = timm.create_model(config["timm_name"], pretrained=False, num_classes=100)
        ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
        state_dict = ckpt.get("state_dict", ckpt.get("model_state_dict", ckpt))
        model.load_state_dict(state_dict)
        
        layer_metrics = {}
        for name, param in model.named_parameters():
            if "weight" not in name:
                continue
            w = param.data
            if w.ndim == 4:  # conv
                W_2d = w.reshape(w.shape[0], -1)
            elif w.ndim == 2:
                W_2d = w
            else:
                continue
            
            if min(W_2d.shape) < 2:
                continue
            
            with torch.no_grad():
                S = torch.linalg.svdvals(W_2d.float())
            
            sigma_1 = S[0].item()
            if sigma_1 == 0:
                continue
            
            fro_sq = (S ** 2).sum().item()
            stable_rank = fro_sq / (sigma_1 ** 2)
            R_l = sigma_1 / stable_rank  # Paper's spectral response ratio
            
            layer_metrics[name] = {
                "sigma_1": sigma_1,
                "stable_rank": stable_rank,
                "R_l": R_l,
                "fro_norm_sq": fro_sq,
            }
        
        all_metrics[model_name] = layer_metrics
        print(f"    {len(layer_metrics)} layers analyzed")
    
    return all_metrics

def compute_spectral_response_correlation(all_metrics):
    print("\n--- Spectral response ratio ΔR_l correlation ---")
    
    results = {}
    
    # ResNet-50
    resnet_swap = load_resnet_swap(f"{BASE}/results/resnet50_weight_swap.csv")
    muon_m = all_metrics.get("resnet50_muon", {})
    adamw_m = all_metrics.get("resnet50_adamw", {})
    
    deltas_R = []
    deltas_sr = []
    drops = []
    layer_names = []
    per_layer_data = []
    
    for swap_name, drop in sorted(resnet_swap.items()):
        spec_name = swap_name + ".weight"
        if spec_name in muon_m and spec_name in adamw_m:
            delta_R = muon_m[spec_name]["R_l"] - adamw_m[spec_name]["R_l"]
            delta_sr = muon_m[spec_name]["stable_rank"] - adamw_m[spec_name]["stable_rank"]
            deltas_R.append(delta_R)
            deltas_sr.append(delta_sr)
            drops.append(drop)
            layer_names.append(swap_name)
            per_layer_data.append({
                "layer": swap_name,
                "R_muon": round(muon_m[spec_name]["R_l"], 6),
                "R_adamw": round(adamw_m[spec_name]["R_l"], 6),
                "delta_R": round(delta_R, 6),
                "sr_muon": round(muon_m[spec_name]["stable_rank"], 4),
                "sr_adamw": round(adamw_m[spec_name]["stable_rank"], 4),
                "delta_sr": round(delta_sr, 4),
                "sigma1_muon": round(muon_m[spec_name]["sigma_1"], 6),
                "sigma1_adamw": round(adamw_m[spec_name]["sigma_1"], 6),
                "muon_drop_pp": drop,
            })
    
    deltas_R = np.array(deltas_R)
    deltas_sr = np.array(deltas_sr)
    drops = np.array(drops)
    
    rho_R, p_R = stats.spearmanr(deltas_R, drops)
    rho_sr, p_sr = stats.spearmanr(deltas_sr, drops)
    
    results["resnet50"] = {
        "n_matched": len(drops),
        "spectral_response_ratio": {"rho": round(float(rho_R), 4), "p": round(float(p_R), 6)},
        "delta_stable_rank": {"rho": round(float(rho_sr), 4), "p": round(float(p_sr), 6)},
        "per_layer": per_layer_data,
    }
    print(f"  ResNet-50 (n={len(drops)}):")
    print(f"    ΔR_l (paper's spectral response ratio): rho={rho_R:+.4f}, p={p_R:.6f}")
    print(f"    Δstable_rank:                           rho={rho_sr:+.4f}, p={p_sr:.6f}")
    
    # DeiT-S
    deit_swap = load_deit_swap(f"{BASE}/results/deit_weight_swap.csv")
    muon_m = all_metrics.get("deit_small_muon", {})
    adamw_m = all_metrics.get("deit_small_adamw", {})
    
    deltas_R = []
    deltas_sr = []
    drops = []
    layer_names = []
    per_layer_data = []
    
    for swap_name, drop in sorted(deit_swap.items()):
        spec_name = deit_swap_to_spectral(swap_name)
        if spec_name in muon_m and spec_name in adamw_m:
            delta_R = muon_m[spec_name]["R_l"] - adamw_m[spec_name]["R_l"]
            delta_sr = muon_m[spec_name]["stable_rank"] - adamw_m[spec_name]["stable_rank"]
            deltas_R.append(delta_R)
            deltas_sr.append(delta_sr)
            drops.append(drop)
            layer_names.append(swap_name)
            per_layer_data.append({
                "layer": swap_name,
                "R_muon": round(muon_m[spec_name]["R_l"], 6),
                "R_adamw": round(adamw_m[spec_name]["R_l"], 6),
                "delta_R": round(delta_R, 6),
                "sr_muon": round(muon_m[spec_name]["stable_rank"], 4),
                "sr_adamw": round(adamw_m[spec_name]["stable_rank"], 4),
                "delta_sr": round(delta_sr, 4),
                "sigma1_muon": round(muon_m[spec_name]["sigma_1"], 6),
                "sigma1_adamw": round(adamw_m[spec_name]["sigma_1"], 6),
                "muon_drop_pp": drop,
            })
    
    deltas_R = np.array(deltas_R)
    deltas_sr = np.array(deltas_sr)
    drops = np.array(drops)
    
    rho_R, p_R = stats.spearmanr(deltas_R, drops)
    rho_sr, p_sr = stats.spearmanr(deltas_sr, drops)
    
    results["deit_s"] = {
        "n_matched": len(drops),
        "spectral_response_ratio": {"rho": round(float(rho_R), 4), "p": round(float(p_R), 6)},
        "delta_stable_rank": {"rho": round(float(rho_sr), 4), "p": round(float(p_sr), 6)},
        "per_layer": per_layer_data,
    }
    print(f"  DeiT-S (n={len(drops)}):")
    print(f"    ΔR_l (paper's spectral response ratio): rho={rho_R:+.4f}, p={p_R:.6f}")
    print(f"    Δstable_rank:                           rho={rho_sr:+.4f}, p={p_sr:.6f}")
    
    return results

# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("INVESTIGATION: Source of rho=+0.34 (ResNet) / rho=-0.66 (DeiT)")
    print("=" * 70)
    
    # Part A: CSV-derived metrics
    print("\n### Part A: Delta metrics from spectral_metrics.csv ###")
    csv_results, resnet_matched, deit_matched = compute_deltas_from_csv()
    
    # Part B: FCSB margin
    print("\n### Part B: FCSB margin (from gradient_geometry) ###")
    fcsb_results = compute_fcsb_correlation()
    
    # Part C: Paper's spectral response ratio from checkpoints
    print("\n### Part C: Paper's spectral response ratio (from checkpoints) ###")
    all_metrics = compute_spectral_response_from_checkpoints()
    sr_results = compute_spectral_response_correlation(all_metrics)
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"\nPaper claims: ResNet ρ=+0.34 (p=0.011), DeiT ρ=-0.66 (p<0.001)")
    print(f"\nActual computed values:")
    print(f"\n  From spectral_metrics.csv (old checkpoints):")
    for m in ["stable_rank", "spectral_gap", "condition_number", "effective_rank", "spectral_decay_exponent"]:
        r_rho = csv_results["resnet50_csv_metrics"][f"delta_{m}"]["rho"]
        d_rho = csv_results["deit_s_csv_metrics"][f"delta_{m}"]["rho"]
        print(f"    delta_{m:25s}: ResNet={r_rho:+.4f}, DeiT={d_rho:+.4f}")
    
    print(f"\n  FCSB margin (gradient geometry):")
    for ep in [1, 3, 5]:
        r = fcsb_results[f"resnet50_fcsb_ep{ep}"]
        d = fcsb_results[f"deit_fcsb_ep{ep}"]
        print(f"    epoch {ep}: ResNet={r['rho']:+.4f} (n={r['n']}), DeiT={d['rho']:+.4f} (n={d['n']})")
    
    print(f"\n  Paper's R_l = σ_1/sr (new checkpoints):")
    for arch in ["resnet50", "deit_s"]:
        if arch in sr_results:
            sr = sr_results[arch]["spectral_response_ratio"]
            ds = sr_results[arch]["delta_stable_rank"]
            print(f"    {arch}: ΔR_l rho={sr['rho']:+.4f} (p={sr['p']:.6f}), Δsr rho={ds['rho']:+.4f} (p={ds['p']:.6f})")
    
    # Save all results
    output = {
        "paper_claims": {
            "resnet50": {"rho": 0.34, "p": 0.011},
            "deit_s": {"rho": -0.66, "p_lt": 0.001},
        },
        "csv_metrics": csv_results,
        "fcsb_margin": fcsb_results,
        "spectral_response_ratio": sr_results,
    }
    
    out_path = f"{BASE}/results/rho_investigation.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nFull results saved to {out_path}")
