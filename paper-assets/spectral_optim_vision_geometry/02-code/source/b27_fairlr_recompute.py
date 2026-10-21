"""B2.7: Weight Swap + Correlation recomputation with optimal-lr checkpoints."""
import csv
import json
import os
import sys
import time

import numpy as np
from scipy import stats

# --- Step 1 & 2: Run weight swap scripts ---
def run_weight_swaps():
    """Run both ResNet and DeiT weight swaps via subprocess."""
    import subprocess
    base = "/root/spectral_optim_vision_geometry"
    out_dir = f"{base}/results/fairlr"
    os.makedirs(out_dir, exist_ok=True)

    # ResNet-50
    print("=" * 60)
    print("STEP 1: ResNet-50 Weight Swap (optimal-lr)")
    print("=" * 60, flush=True)
    cmd_resnet = [
        sys.executable, f"{base}/weight_swap_ablation.py",
        "--model", "resnet50",
        "--muon-ckpt", f"{base}/checkpoints/resnet50_muon_s42.pt",
        "--adamw-ckpt", f"{base}/checkpoints/resnet50_adamw_lr0.001_wd0.05_s42_ep20.pt",
        "--gpu", "0",
        "--output-dir", out_dir,
    ]
    t0 = time.time()
    r = subprocess.run(cmd_resnet, capture_output=False)
    print(f"\nResNet done in {time.time()-t0:.0f}s, exit={r.returncode}", flush=True)
    if r.returncode != 0:
        print("ERROR: ResNet weight swap failed!")
        return False

    # DeiT-S
    print("\n" + "=" * 60)
    print("STEP 2: DeiT-S Weight Swap (optimal-lr)")
    print("=" * 60, flush=True)
    cmd_deit = [
        sys.executable, f"{base}/deit_weight_swap.py",
        "--muon-ckpt", f"{base}/checkpoints/deit_small_muon_lr0003_s42_ep20.pt",
        "--adamw-ckpt", f"{base}/checkpoints/deit_small_adamw_lr0.0001_wd0.05_s42_ep20.pt",
        "--gpu", "0",
        "--output", f"{out_dir}/deit_weight_swap.csv",
    ]
    t0 = time.time()
    r = subprocess.run(cmd_deit, capture_output=False)
    print(f"\nDeiT done in {time.time()-t0:.0f}s, exit={r.returncode}", flush=True)
    if r.returncode != 0:
        print("ERROR: DeiT weight swap failed!")
        return False

    return True


# --- Step 3: Correlation ---
def load_csv(path):
    with open(path) as f:
        return list(csv.DictReader(f))

def normalize_layer_name(name):
    """Normalize layer names for matching between swap CSV and FCSB CSV."""
    return name.strip()

def compute_correlations():
    base = "/root/spectral_optim_vision_geometry"
    results_dir = f"{base}/results"
    fairlr_dir = f"{results_dir}/fairlr"

    print("\n" + "=" * 60)
    print("STEP 3: Correlation Computation")
    print("=" * 60, flush=True)

    output = {
        "experiment": "B2.7_fairlr_recompute",
        "description": "Weight swap + correlation with optimal-lr AdamW checkpoints",
        "old_baselines": {
            "resnet50": {"rho": 0.40, "p": 0.003, "note": "grishina_ep5, AdamW lr=3e-4"},
            "deit_s": {"rho": -0.51, "p": 0.000224, "note": "grishina_ep5, AdamW lr=3e-4"},
        },
    }

    for arch, swap_csv_name, fcsb_csv_name in [
        ("resnet50", "resnet50_weight_swap.csv", "gradient_geometry_resnet50.csv"),
        ("deit_s", "deit_weight_swap.csv", "gradient_geometry_deit_small.csv"),
    ]:
        print(f"\n--- {arch} ---", flush=True)
        swap_path = f"{fairlr_dir}/{swap_csv_name}"
        fcsb_path = f"{results_dir}/{fcsb_csv_name}"

        if not os.path.exists(swap_path):
            print(f"  MISSING: {swap_path}")
            output[arch] = {"error": f"swap CSV not found: {swap_path}"}
            continue
        if not os.path.exists(fcsb_path):
            print(f"  MISSING: {fcsb_path}")
            output[arch] = {"error": f"FCSB CSV not found: {fcsb_path}"}
            continue

        swap_rows = load_csv(swap_path)
        fcsb_rows = load_csv(fcsb_path)

        # Build FCSB lookup: layer_name -> {epoch -> metrics}
        # The FCSB CSV has columns: epoch, layer_name, R, sr_X, delta_grishina, fcsb_grishina_pred, etc.
        fcsb_by_layer = {}
        for row in fcsb_rows:
            ln = row["layer_name"]
            ep = int(row["epoch"])
            if ln not in fcsb_by_layer:
                fcsb_by_layer[ln] = {}
            fcsb_by_layer[ln][ep] = row

        # Build swap lookup
        # ResNet uses layer_name, DeiT uses group_name
        swap_key = "layer_name" if "layer_name" in swap_rows[0] else "group_name"
        swap_by_layer = {}
        for row in swap_rows:
            ln = row[swap_key]
            swap_by_layer[ln] = row

        # Match layers
        # For ResNet: direct name match
        # For DeiT: need to handle block_N.component -> blocks.N.component mapping
        def deit_swap_to_fcsb(swap_name):
            """Convert DeiT swap group names to FCSB layer names."""
            # block_N.attn.qkv -> blocks.N.attn.qkv
            if swap_name.startswith("block_"):
                parts = swap_name.split(".", 1)
                block_num = parts[0].replace("block_", "")
                if len(parts) > 1:
                    return f"blocks.{block_num}.{parts[1]}"
                else:
                    return f"blocks.{block_num}"
            return swap_name

        arch_results = {"baselines": {}, "correlations": {}}

        # Get baselines from swap CSV header info or first/last row context
        # Actually the baselines are printed to stdout, not in CSV. Let's just record what we have.

        # Try all epochs in FCSB data
        available_epochs = set()
        for layer_data in fcsb_by_layer.values():
            available_epochs.update(layer_data.keys())
        available_epochs = sorted(available_epochs)
        print(f"  Available FCSB epochs: {available_epochs}")

        for epoch in available_epochs:
            matched_fcsb = []
            matched_drop = []
            matched_names = []

            for swap_name, swap_row in swap_by_layer.items():
                fcsb_name = deit_swap_to_fcsb(swap_name) if arch == "deit_s" else swap_name
                if fcsb_name in fcsb_by_layer and epoch in fcsb_by_layer[fcsb_name]:
                    fcsb_row = fcsb_by_layer[fcsb_name][epoch]
                    # FCSB margin = R / sr_X * delta
                    R = float(fcsb_row["R"])
                    sr_X = float(fcsb_row["sr_X"])
                    delta_g = float(fcsb_row["delta_grishina"])
                    delta_t = float(fcsb_row["delta_theory"])
                    delta_e = float(fcsb_row["delta_empirical"])

                    fcsb_margin_g = R / sr_X * delta_g if sr_X > 0 else 0
                    fcsb_margin_t = R / sr_X * delta_t if sr_X > 0 else 0
                    fcsb_margin_e = R / sr_X * delta_e if sr_X > 0 else 0
                    davis_margin = R / sr_X if sr_X > 0 else 0

                    muon_drop = float(swap_row.get("muon_drop_pp", 0))

                    matched_fcsb.append({
                        "grishina": fcsb_margin_g,
                        "theory": fcsb_margin_t,
                        "empirical": fcsb_margin_e,
                        "davis": davis_margin,
                    })
                    matched_drop.append(muon_drop)
                    matched_names.append(swap_name)

            n = len(matched_drop)
            if n < 5:
                print(f"  epoch {epoch}: only {n} matched layers, skipping")
                continue

            drops = np.array(matched_drop)
            ep_results = {"n_matched": n}
            for metric in ["grishina", "theory", "empirical", "davis"]:
                vals = np.array([m[metric] for m in matched_fcsb])
                rho, p = stats.spearmanr(vals, drops)
                ep_results[f"fcsb_{metric}"] = {
                    "spearman_rho": round(float(rho), 4),
                    "spearman_p": round(float(p), 6),
                }
                if metric == "grishina":
                    print(f"  epoch {epoch}: ρ(FCSB_grishina, muon_drop) = {rho:+.4f} (p={p:.6f}, n={n})")

            arch_results["correlations"][f"epoch_{epoch}"] = ep_results

        output[arch] = arch_results

    # --- Kill/Confirm judgment ---
    print("\n" + "=" * 60)
    print("STEP 4: Kill/Confirm Judgment")
    print("=" * 60, flush=True)

    judgment = {}
    for arch, old_rho, expected_sign in [("resnet50", 0.40, "positive"), ("deit_s", -0.51, "negative")]:
        if arch not in output or "correlations" not in output[arch]:
            judgment[arch] = "INCONCLUSIVE - missing data"
            continue

        corrs = output[arch]["correlations"]
        # Use epoch 5 grishina as primary (matching old analysis)
        best_key = None
        for k in ["epoch_5", "epoch_3", "epoch_1"]:
            if k in corrs and "fcsb_grishina" in corrs[k]:
                best_key = k
                break

        if best_key is None:
            judgment[arch] = "INCONCLUSIVE - no matching epoch"
            continue

        new_rho = corrs[best_key]["fcsb_grishina"]["spearman_rho"]
        new_p = corrs[best_key]["fcsb_grishina"]["spearman_p"]

        sign_ok = (expected_sign == "positive" and new_rho > 0) or \
                  (expected_sign == "negative" and new_rho < 0)
        magnitude_ok = abs(new_rho) >= 0.2

        if sign_ok and magnitude_ok:
            verdict = "CONFIRMED"
        elif not sign_ok:
            verdict = "KILL - direction reversal disappeared"
        else:
            verdict = "KILL - |rho| < 0.2"

        judgment[arch] = {
            "epoch": best_key,
            "new_rho": new_rho,
            "new_p": new_p,
            "old_rho": old_rho,
            "expected_sign": expected_sign,
            "sign_preserved": sign_ok,
            "magnitude_sufficient": magnitude_ok,
            "verdict": verdict,
        }
        print(f"  {arch}: old ρ={old_rho:+.2f} → new ρ={new_rho:+.4f} (p={new_p:.6f}) → {verdict}")

    # Overall Claim 1
    resnet_ok = isinstance(judgment.get("resnet50"), dict) and judgment["resnet50"]["verdict"] == "CONFIRMED"
    deit_ok = isinstance(judgment.get("deit_s"), dict) and judgment["deit_s"]["verdict"] == "CONFIRMED"

    if resnet_ok and deit_ok:
        claim1 = "CONFIRMED - direction reversal survives optimal-lr"
    elif not resnet_ok and not deit_ok:
        claim1 = "KILL - both architectures fail"
    else:
        claim1 = "PARTIAL - one architecture fails"
        if not resnet_ok:
            claim1 += " (ResNet fails)"
        if not deit_ok:
            claim1 += " (DeiT fails)"

    output["judgment"] = judgment
    output["claim1_verdict"] = claim1
    print(f"\n  *** CLAIM 1: {claim1} ***")

    # Save
    out_path = f"{fairlr_dir}/correlation_fairlr.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")

    return output


if __name__ == "__main__":
    ok = run_weight_swaps()
    if not ok:
        print("\nWeight swap failed, attempting correlation with whatever data exists...")
    compute_correlations()
    print("\nB2.7 COMPLETE")
