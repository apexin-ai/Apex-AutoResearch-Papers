#!/usr/bin/env python3
"""ConvNeXt-T SGD lr sweep: 5 epochs each, lr in {0.01, 0.05, 0.1}"""
import subprocess, sys, re, json, os
import shutil

os.environ.setdefault("TMPDIR", "/root/autodl-tmp/tmp")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)

LRS = [0.01, 0.05, 0.1]
EPOCHS = 5
GPU = 0
SEED = 42
SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "convnext_t_sgd_train.py")


def check_disk_space(path='/', min_gb=2.0):
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')


check_disk_space('/')
check_disk_space('/root/autodl-tmp', min_gb=5.0)

results = []

for lr in LRS:
    print(f"\n{'='*60}")
    print(f"Running ConvNeXt-T SGD lr={lr}, epochs={EPOCHS}")
    print(f"{'='*60}", flush=True)

    cmd = [
        sys.executable, SCRIPT,
        "--gpu", str(GPU),
        "--seed", str(SEED),
        "--epochs", str(EPOCHS),
        "--lr", str(lr),
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    output = proc.stdout + proc.stderr
    print(output[-3000:], flush=True)

    val_accs = re.findall(r'val_acc=([\d.]+)%', output)
    train_losses = re.findall(r'train_loss=([\d.]+)', output)

    result = {
        "lr": lr,
        "val_accs": [float(v) for v in val_accs],
        "train_losses": [float(v) for v in train_losses],
        "best_val_acc": max(float(v) for v in val_accs) if val_accs else 0,
        "final_val_acc": float(val_accs[-1]) if val_accs else 0,
    }
    results.append(result)

print(f"\n{'='*60}")
print("SGD LR SWEEP SUMMARY (ConvNeXt-T, 5 epochs)")
print(f"{'='*60}")
print(f"{'LR':>8} | {'Best Val Acc':>12} | {'Final Val Acc':>13} | Trajectory")
print(f"{'-'*8}-+-{'-'*12}-+-{'-'*13}-+-{'-'*30}")
for r in results:
    accs_str = " -> ".join(f"{a:.1f}" for a in r["val_accs"])
    print(f"{r['lr']:>8} | {r['best_val_acc']:>11.2f}% | {r['final_val_acc']:>12.2f}% | {accs_str}")

best = max(results, key=lambda x: x["best_val_acc"])
print(f"\nBest LR: {best['lr']} with val_acc={best['best_val_acc']:.2f}%")
print(json.dumps(results, indent=2))
print("SWEEP_COMPLETE")
