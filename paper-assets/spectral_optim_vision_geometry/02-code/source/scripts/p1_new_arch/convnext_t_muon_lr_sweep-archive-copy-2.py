#!/usr/bin/env python3
"""ConvNeXt-T Muon lr sweep: 5 lr points x 5 epochs on CIFAR-100"""
import subprocess, sys, re, json, os
import shutil

os.environ.setdefault("TMPDIR", "/root/autodl-tmp/tmp")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)

LR_POINTS = [0.001, 0.003, 0.006, 0.01, 0.02]
EPOCHS = 5
GPU = 0
SEED = 42
SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "convnext_t_muon_train.py")


def check_disk_space(path='/', min_gb=2.0):
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')


check_disk_space('/')
check_disk_space('/root/autodl-tmp', min_gb=5.0)

results = {}
for lr in LR_POINTS:
    print(f"\n{'='*60}")
    print(f"Running ConvNeXt-T Muon lr={lr}, epochs={EPOCHS}")
    print(f"{'='*60}", flush=True)

    cmd = [
        sys.executable, SCRIPT,
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
print("LR SWEEP RESULTS (ConvNeXt-T Muon, 5 epochs)")
print(f"{'='*60}")
print(f"{'LR':<10} {'Best Val%':<12} {'Final Val%':<12} {'Epoch Accs'}")
print(f"{'-'*60}")
for lr_str, r in results.items():
    accs_str = " -> ".join(f"{a:.1f}" for a in r["val_accs"])
    print(f"{lr_str:<10} {r['best_val_acc']:<12.2f} {r['final_val_acc']:<12.2f} {accs_str}")

best_lr = max(results, key=lambda k: results[k]["best_val_acc"])
print(f"\nBest lr: {best_lr} (val_acc={results[best_lr]['best_val_acc']:.2f}%)")
print(f"\nFull results JSON:")
print(json.dumps(results, indent=2))
print("SWEEP_COMPLETE")
