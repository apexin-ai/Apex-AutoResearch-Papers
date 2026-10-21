"""DeiT-S per-layer spectral analysis: Muon vs AdamW."""
import torch
import numpy as np
import csv
import sys
from collections import defaultdict

MUON_PATH = "/root/autodl-tmp/checkpoints/spectral_optim/deit_small_muon_s2_best.pt"
ADAMW_PATH = "/root/autodl-tmp/checkpoints/spectral_optim/deit_small_adamw_s2_lr3e-4_best.pt"
OUTPUT_CSV = "/root/spectral_optim_vision_geometry/analysis/deit_spectral_results.csv"

SKIP_PREFIXES = ("cls_token", "pos_embed", "patch_embed", "head", "norm.")


def classify_layer(name):
    if "attn.qkv" in name:
        return "attn_qkv"
    elif "attn.proj" in name:
        return "attn_proj"
    elif "mlp.fc1" in name:
        return "mlp_fc1"
    elif "mlp.fc2" in name:
        return "mlp_fc2"
    return "other"


def get_block_idx(name):
    parts = name.split(".")
    for i, p in enumerate(parts):
        if p == "blocks" and i + 1 < len(parts):
            return int(parts[i + 1])
    return -1


def spectral_metrics(W):
    if W.dim() == 1:
        return None
    if W.dim() > 2:
        W = W.reshape(W.shape[0], -1)
    S = torch.linalg.svdvals(W.float())
    s = S.numpy()

    sigma_max = s[0]
    sigma_min = s[-1]
    frob_sq = np.sum(s ** 2)

    stable_rank = frob_sq / (sigma_max ** 2) if sigma_max > 0 else 0.0
    condition = sigma_max / sigma_min if sigma_min > 1e-12 else float("inf")

    # Effective rank via Shannon entropy
    p = s / np.sum(s) if np.sum(s) > 0 else s
    p = p[p > 1e-12]
    entropy = -np.sum(p * np.log(p))
    effective_rank = np.exp(entropy)

    top10 = s[:10].tolist()
    while len(top10) < 10:
        top10.append(0.0)

    return {
        "shape": f"{W.shape[0]}x{W.shape[1]}",
        "stable_rank": stable_rank,
        "condition_number": condition,
        "effective_rank": effective_rank,
        "sigma_max": sigma_max,
        "sigma_min": sigma_min,
        "top10_sv": top10,
    }


def load_state_dict(path):
    ckpt = torch.load(path, map_location="cpu")
    for key in ("state_dict", "model_state_dict", "model"):
        if key in ckpt:
            return ckpt[key]
    return ckpt


def analyze_checkpoint(sd, label):
    rows = []
    for name, param in sorted(sd.items()):
        if any(name.startswith(p) for p in SKIP_PREFIXES):
            continue
        if not name.endswith(".weight"):
            continue
        if "norm" in name:
            continue

        layer_type = classify_layer(name)
        block_idx = get_block_idx(name)
        if layer_type == "other":
            continue

        # For qkv, split into Q, K, V
        if layer_type == "attn_qkv":
            W = param
            dim = W.shape[0] // 3
            for sub_name, sub_w in [("Q", W[:dim]), ("K", W[dim:2*dim]), ("V", W[2*dim:])]:
                m = spectral_metrics(sub_w)
                if m:
                    rows.append({
                        "optimizer": label,
                        "block": block_idx,
                        "layer": f"blocks.{block_idx}.attn.{sub_name}",
                        "layer_type": f"attn_{sub_name}",
                        **m,
                    })
        else:
            m = spectral_metrics(param)
            if m:
                rows.append({
                    "optimizer": label,
                    "block": block_idx,
                    "layer": name.replace(".weight", ""),
                    "layer_type": layer_type,
                    **m,
                })
    return rows


def main():
    print("Loading checkpoints...")
    sd_muon = load_state_dict(MUON_PATH)
    sd_adamw = load_state_dict(ADAMW_PATH)

    print("Analyzing Muon...")
    rows_muon = analyze_checkpoint(sd_muon, "Muon")
    print("Analyzing AdamW...")
    rows_adamw = analyze_checkpoint(sd_adamw, "AdamW")

    all_rows = rows_muon + rows_adamw

    # Write CSV
    fields = [
        "optimizer", "block", "layer", "layer_type", "shape",
        "stable_rank", "condition_number", "effective_rank",
        "sigma_max", "sigma_min",
    ] + [f"sv_{i}" for i in range(10)]

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in all_rows:
            flat = {k: row[k] for k in fields[:10]}
            for i in range(10):
                flat[f"sv_{i}"] = f"{row['top10_sv'][i]:.6f}"
            flat["stable_rank"] = f"{row['stable_rank']:.4f}"
            flat["condition_number"] = f"{row['condition_number']:.4f}" if row["condition_number"] != float("inf") else "inf"
            flat["effective_rank"] = f"{row['effective_rank']:.4f}"
            flat["sigma_max"] = f"{row['sigma_max']:.6f}"
            flat["sigma_min"] = f"{row['sigma_min']:.6f}"
            writer.writerow(flat)

    print(f"\nCSV saved to {OUTPUT_CSV}")

    # Print summary tables
    print("\n" + "=" * 120)
    print("PER-LAYER SPECTRAL COMPARISON: Muon vs AdamW (DeiT-S)")
    print("=" * 120)

    # Group by layer for side-by-side comparison
    muon_map = {r["layer"]: r for r in rows_muon}
    adamw_map = {r["layer"]: r for r in rows_adamw}

    print(f"\n{'Layer':<35} {'Type':<10} | {'Stable Rank':>11} {'Cond Num':>10} {'Eff Rank':>10} {'σ_max':>10} | {'Stable Rank':>11} {'Cond Num':>10} {'Eff Rank':>10} {'σ_max':>10}")
    print(f"{'':<35} {'':<10} | {'--- Muon ---':^43} | {'--- AdamW ---':^43}")
    print("-" * 160)

    for layer in sorted(muon_map.keys(), key=lambda x: (get_block_idx(x), x)):
        m = muon_map[layer]
        a = adamw_map.get(layer)
        if a is None:
            continue
        cond_m = f"{m['condition_number']:.1f}" if m['condition_number'] != float('inf') else 'inf'
        cond_a = f"{a['condition_number']:.1f}" if a['condition_number'] != float('inf') else 'inf'
        print(f"{layer:<35} {m['layer_type']:<10} | {m['stable_rank']:>11.2f} {cond_m:>10} {m['effective_rank']:>10.2f} {m['sigma_max']:>10.4f} | {a['stable_rank']:>11.2f} {cond_a:>10} {a['effective_rank']:>10.2f} {a['sigma_max']:>10.4f}")

    # Aggregate by layer type
    print("\n\n" + "=" * 100)
    print("AGGREGATED BY LAYER TYPE")
    print("=" * 100)

    for opt_label, rows in [("Muon", rows_muon), ("AdamW", rows_adamw)]:
        print(f"\n--- {opt_label} ---")
        by_type = defaultdict(list)
        for r in rows:
            by_type[r["layer_type"]].append(r)

        print(f"{'Type':<12} {'Count':>5} {'Stable Rank':>14} {'Cond Number':>14} {'Eff Rank':>12} {'σ_max':>12} {'σ_min':>12}")
        for lt in ["attn_Q", "attn_K", "attn_V", "attn_proj", "mlp_fc1", "mlp_fc2"]:
            layers = by_type.get(lt, [])
            if not layers:
                continue
            sr = np.mean([l["stable_rank"] for l in layers])
            cn = np.mean([l["condition_number"] for l in layers if l["condition_number"] != float("inf")])
            er = np.mean([l["effective_rank"] for l in layers])
            sm = np.mean([l["sigma_max"] for l in layers])
            sn = np.mean([l["sigma_min"] for l in layers])
            print(f"{lt:<12} {len(layers):>5} {sr:>14.2f} {cn:>14.1f} {er:>12.2f} {sm:>12.4f} {sn:>12.6f}")

    # Compute divergence metrics (Muon - AdamW ratios)
    print("\n\n" + "=" * 100)
    print("SPECTRAL DIVERGENCE: Muon / AdamW RATIOS (per layer type)")
    print("=" * 100)

    muon_by_type = defaultdict(list)
    adamw_by_type = defaultdict(list)
    for r in rows_muon:
        muon_by_type[r["layer_type"]].append(r)
    for r in rows_adamw:
        adamw_by_type[r["layer_type"]].append(r)

    print(f"{'Type':<12} {'SR ratio':>10} {'CN ratio':>10} {'ER ratio':>10} {'σ_max ratio':>12}")
    for lt in ["attn_Q", "attn_K", "attn_V", "attn_proj", "mlp_fc1", "mlp_fc2"]:
        m_layers = muon_by_type.get(lt, [])
        a_layers = adamw_by_type.get(lt, [])
        if not m_layers or not a_layers:
            continue
        sr_m = np.mean([l["stable_rank"] for l in m_layers])
        sr_a = np.mean([l["stable_rank"] for l in a_layers])
        cn_m = np.mean([l["condition_number"] for l in m_layers if l["condition_number"] != float("inf")])
        cn_a = np.mean([l["condition_number"] for l in a_layers if l["condition_number"] != float("inf")])
        er_m = np.mean([l["effective_rank"] for l in m_layers])
        er_a = np.mean([l["effective_rank"] for l in a_layers])
        sm_m = np.mean([l["sigma_max"] for l in m_layers])
        sm_a = np.mean([l["sigma_max"] for l in a_layers])
        print(f"{lt:<12} {sr_m/sr_a:>10.3f} {cn_m/cn_a:>10.3f} {er_m/er_a:>10.3f} {sm_m/sm_a:>12.3f}")

    # Per-block trend
    print("\n\n" + "=" * 100)
    print("PER-BLOCK STABLE RANK TREND (all weight layers averaged)")
    print("=" * 100)
    for opt_label, rows in [("Muon", rows_muon), ("AdamW", rows_adamw)]:
        by_block = defaultdict(list)
        for r in rows:
            by_block[r["block"]].append(r["stable_rank"])
        print(f"\n{opt_label}:")
        for b in range(12):
            vals = by_block.get(b, [])
            if vals:
                avg = np.mean(vals)
                bar = "█" * int(avg)
                print(f"  Block {b:>2}: {avg:>8.2f}  {bar}")


if __name__ == "__main__":
    main()
