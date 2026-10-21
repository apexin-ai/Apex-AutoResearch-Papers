#!/usr/bin/env python3
"""DeiT-S Muon lr sweep extension: lr=0.003, 0.001 x 5 epochs on CIFAR-100"""
import subprocess, sys, re, json

LR_POINTS = [0.003, 0.001]
EPOCHS = 5
GPU = 0
SEED = 42
MODEL = "deit_small"
SCRIPT = "/root/spectral_optim_vision_geometry/muon_train.py"

results = {}
for lr in LR_POINTS:
    print(f"\n{'='*60}")
    print(f"Running Muon lr={lr}, epochs={EPOCHS}")
    print(f"{'='*60}", flush=True)

    cmd = [
        sys.executable, SCRIPT,
        "--model", MODEL,
        "--gpu", str(GPU),
        "--seed", str(SEED),
        "--epochs", str(EPOCHS),
        "--muon-lr", str(lr),
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    output = proc.stdout + proc.stderr
    print(output[-3000:], flush=True)

    val_accs = re.findall(r'val_acc=([\d.]+)%', output)
    train_losses = re.findall(r'train_loss=([\d.]+)', output)

    results[str(lr)] = {
        "val_accs": [float(v) for v in val_accs],
        "train_losses": [float(v) for v in train_losses],
        "best_val_acc": max(float(v) for v in val_accs) if val_accs else 0,
        "final_val_acc": float(val_accs[-1]) if val_accs else 0,
    }

print(f"\n{'='*60}")
print("LR SWEEP EXT RESULTS (DeiT-S Muon, 5 epochs)")
print(f"{'='*60}")
print(f"{'LR':<10} {'Best Val%':<12} {'Final Val%':<12} {'Epoch Accs'}")
print(f"{'-'*60}")
for lr_str, r in results.items():
    accs_str = " -> ".join(f"{a:.1f}" for a in r["val_accs"])
    print(f"{lr_str:<10} {r['best_val_acc']:<12.2f} {r['final_val_acc']:<12.2f} {accs_str}")

print(f"\nPrevious sweep: lr=0.006→57.37%, lr=0.02→32.04%, lr=0.06→13.55%")
print(f"\nFull results JSON:")
print(json.dumps(results, indent=2))
print("SWEEP_COMPLETE")
