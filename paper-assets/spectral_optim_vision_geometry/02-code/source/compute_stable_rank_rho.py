# Compute stable rank divergence profile (rho) and leave-one-out validation
# Uses power iteration for spectral norm (fast, no full SVD needed)

import torch
import json
import numpy as np
from pathlib import Path

CKPT_DIR = Path("/root/autodl-tmp/checkpoints/spectral_optim")

CONFIGS = {
    "R50-BN": {
        "Muon": "resnet50_muon_s42_best.pt",
        "SOAP": "resnet50_soap_s42_lr1e-2_best.pt",
        "Shampoo": "resnet50_shampoo_s42_lr5e-2_best.pt",
        "AdamW": "resnet50_adamw_s42_lr1e-3_best.pt",
    },
    "R50-LN": {
        "Muon": "resnet50_ln_muon_s42_best.pt",
        "AdamW": "resnet50_ln_adamw_s42_lr1e-3_best.pt",
    },
    "ConvNeXt-T": {
        "Muon": "convnext_tiny_muon_s42_best.pt",
        "SOAP": "convnext_tiny_soap_s42_lr1e-2_best.pt",
        "Shampoo": "convnext_tiny_shampoo_s42_lr7e-3_best.pt",
        "AdamW": "convnext_tiny_adamw_s42_lr1e-3_best.pt",
    },
    "DeiT-S": {
        "Muon": "deit_small_muon_s42_best.pt",
        "SOAP": "deit_small_soap_s42_lr5e-3_best.pt",
        "Shampoo": "deit_small_shampoo_s42_lr5e-3_best.pt",
        "AdamW": "deit_small_adamw_s42_lr1e-3_best.pt",
    },
}

def spectral_norm_power_iter(W, n_iter=20):
    """Fast spectral norm via power iteration."""
    v = torch.randn(W.shape[1], device=W.device)
    v = v / v.norm()
    for _ in range(n_iter):
        u = W @ v
        u = u / (u.norm() + 1e-12)
        v = W.t() @ u
        v = v / (v.norm() + 1e-12)
    return (W @ v).norm().item()

def compute_stable_ranks(state_dict):
    """Compute per-layer stable rank for all 2D+ weight matrices."""
    stable_ranks = {}
    for name, param in state_dict.items():
        if param.dim() < 2 or 'weight' not in name:
            continue
        W = param.reshape(param.shape[0], -1).float()
        frob_sq = torch.sum(W ** 2).item()
        spec = spectral_norm_power_iter(W)
        spec_sq = spec ** 2
        stable_ranks[name] = frob_sq / spec_sq if spec_sq > 1e-12 else 1.0
    return stable_ranks

def load_checkpoint_and_compute(filepath):
    """Load checkpoint, extract val_acc, compute stable ranks."""
    ckpt = torch.load(filepath, map_location='cpu', weights_only=False)
    val_acc = None
    if isinstance(ckpt, dict):
        val_acc = ckpt.get('val_acc') or ckpt.get('best_acc') or ckpt.get('acc')
        state_dict = ckpt.get('model_state_dict') or ckpt.get('state_dict') or ckpt.get('model')
        if state_dict is None:
            state_dict = {k: v for k, v in ckpt.items() if isinstance(v, torch.Tensor)}
    else:
        state_dict = ckpt
    stable_ranks = compute_stable_ranks(state_dict)
    return val_acc, stable_ranks

def compute_rho(sr_spectral, sr_baseline):
    """Compute rho: mean relative stable rank change across matched layers."""
    common = set(sr_spectral.keys()) & set(sr_baseline.keys())
    if not common:
        return None
    changes = [(sr_spectral[l] - sr_baseline[l]) / sr_baseline[l] 
               for l in common if sr_baseline[l] > 0]
    return float(np.mean(changes)) if changes else None

# Verify one checkpoint first
print("Verifying: resnet50_muon_s42_best.pt")
val_acc, srs = load_checkpoint_and_compute(CKPT_DIR / "resnet50_muon_s42_best.pt")
print(f"  acc={val_acc}, n_layers={len(srs)}, mean_SR={np.mean(list(srs.values())):.3f}")
print()

# Process all
results = {}
for arch, opts in CONFIGS.items():
    results[arch] = {}
    for opt_name, filename in opts.items():
        fp = CKPT_DIR / filename
        if not fp.exists():
            print(f"  MISSING: {fp.name}")
            continue
        val_acc, stable_ranks = load_checkpoint_and_compute(fp)
        results[arch][opt_name] = {
            "val_acc": val_acc,
            "stable_ranks": stable_ranks,
            "mean_sr": float(np.mean(list(stable_ranks.values()))),
            "n_layers": len(stable_ranks),
        }
        print(f"  {arch}/{opt_name}: acc={val_acc}, mean_SR={results[arch][opt_name]['mean_sr']:.3f}")

# Compute rho
print("\n--- Rho values ---")
rho_data = []
for arch, opts in results.items():
    if "AdamW" not in opts:
        continue
    baseline = opts["AdamW"]
    for opt_name, data in opts.items():
        if opt_name == "AdamW":
            continue
        rho = compute_rho(data["stable_ranks"], baseline["stable_ranks"])
        if rho is not None and data["val_acc"] is not None and baseline["val_acc"] is not None:
            delta_acc = data["val_acc"] - baseline["val_acc"]
            rho_data.append({
                "arch": arch, "optimizer": opt_name, "rho": rho,
                "delta_acc": delta_acc, "spec_acc": data["val_acc"],
                "base_acc": baseline["val_acc"],
            })
            print(f"  {arch}/{opt_name}: rho={rho:.4f}, delta_acc={delta_acc:+.2f}%")

# Leave-one-out
print("\n--- Leave-one-architecture-out ---")
rhos = np.array([d["rho"] for d in rho_data])
deltas = np.array([d["delta_acc"] for d in rho_data])
archs_list = [d["arch"] for d in rho_data]
unique_archs = sorted(set(archs_list))

loo_results = []
for leave_out in unique_archs:
    train_idx = [i for i, a in enumerate(archs_list) if a != leave_out]
    test_idx = [i for i, a in enumerate(archs_list) if a == leave_out]
    if len(train_idx) < 2:
        continue
    X_tr, y_tr = rhos[train_idx], deltas[train_idx]
    # Simple linear regression: y = a*x + b
    A = np.vstack([X_tr, np.ones(len(X_tr))]).T
    slope, intercept = np.linalg.lstsq(A, y_tr, rcond=None)[0]
    for i in test_idx:
        pred = slope * rhos[i] + intercept
        err = pred - deltas[i]
        loo_results.append({
            "arch": leave_out, "optimizer": rho_data[i]["optimizer"],
            "rho": float(rhos[i]), "predicted": float(pred),
            "actual": float(deltas[i]), "error": float(err),
        })
        print(f"  Leave-out {leave_out}/{rho_data[i]['optimizer']}: pred={pred:+.2f}, actual={deltas[i]:+.2f}, err={err:+.2f}")

# Overall fit
A_all = np.vstack([rhos, np.ones(len(rhos))]).T
slope_all, intercept_all = np.linalg.lstsq(A_all, deltas, rcond=None)[0]
ss_res = np.sum((deltas - (slope_all * rhos + intercept_all))**2)
ss_tot = np.sum((deltas - np.mean(deltas))**2)
r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

print(f"\n--- Overall fit ---")
print(f"  slope={slope_all:.2f}, intercept={intercept_all:.2f}, R²={r2:.3f}")
if loo_results:
    mae = np.mean([abs(r["error"]) for r in loo_results])
    print(f"  LOO MAE={mae:.2f}%")

# Summary table
print(f"\n{'Arch':<12} {'Opt':<10} {'ρ':>8} {'Δacc':>8} {'Spec':>6} {'Base':>6}")
print("-" * 56)
for d in sorted(rho_data, key=lambda x: (x['arch'], x['optimizer'])):
    print(f"{d['arch']:<12} {d['optimizer']:<10} {d['rho']:>8.4f} {d['delta_acc']:>+7.2f}% {d['spec_acc']:>6.2f} {d['base_acc']:>6.2f}")

# Save
output = {"rho_table": rho_data, "loo_results": loo_results,
          "linear_fit": {"slope": float(slope_all), "intercept": float(intercept_all), "r_squared": float(r2)}}
out_path = Path("/root/spectral_optim_vision_geometry/artifacts/svd_analysis/stable_rank_divergence.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved: {out_path}")
