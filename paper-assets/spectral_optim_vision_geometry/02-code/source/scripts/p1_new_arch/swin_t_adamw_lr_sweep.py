#!/usr/bin/env python3
"""Swin-T AdamW baseline: 5 epochs with lr=0.001 on CIFAR-100"""
import subprocess, sys, re, json, os
import shutil

os.environ.setdefault("TMPDIR", "/root/autodl-tmp/tmp")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)

LR = 0.001
EPOCHS = 5
GPU = 0
SEED = 42
SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "swin_t_adamw_train.py")


def check_disk_space(path='/', min_gb=2.0):
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')


check_disk_space('/')
check_disk_space('/root/autodl-tmp', min_gb=5.0)

print(f"{'='*60}")
print(f"Running Swin-T AdamW lr={LR}, epochs={EPOCHS}")
print(f"{'='*60}", flush=True)

cmd = [
    sys.executable, SCRIPT,
    "--gpu", str(GPU),
    "--seed", str(SEED),
    "--epochs", str(EPOCHS),
    "--lr", str(LR),
]

proc = subprocess.run(cmd, capture_output=True, text=True)
output = proc.stdout + proc.stderr
print(output[-3000:], flush=True)

val_accs = re.findall(r'val_acc=([\d.]+)%', output)
train_losses = re.findall(r'train_loss=([\d.]+)', output)

result = {
    "lr": LR,
    "val_accs": [float(v) for v in val_accs],
    "train_losses": [float(v) for v in train_losses],
    "best_val_acc": max(float(v) for v in val_accs) if val_accs else 0,
    "final_val_acc": float(val_accs[-1]) if val_accs else 0,
}

print(f"\n{'='*60}")
print(f"AdamW BASELINE (Swin-T, 5 epochs, lr={LR})")
print(f"{'='*60}")
accs_str = " -> ".join(f"{a:.1f}" for a in result["val_accs"])
print(f"Val acc trajectory: {accs_str}")
print(f"Best: {result['best_val_acc']:.2f}%, Final: {result['final_val_acc']:.2f}%")
print(json.dumps(result, indent=2))
print("BASELINE_COMPLETE")
