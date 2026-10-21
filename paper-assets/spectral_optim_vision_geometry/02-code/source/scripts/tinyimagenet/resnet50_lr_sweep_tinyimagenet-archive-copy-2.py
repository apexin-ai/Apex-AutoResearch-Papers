"""ResNet-50 lr sweep on Tiny-ImageNet-200: Muon vs AdamW lr fairness validation.

Purpose: NeurIPS reviewer requested independent lr sweep on Tiny-ImageNet to
confirm that the CIFAR-100 optimal lrs transfer fairly. This runs 6 sequential
5-epoch trials (3 Muon lrs + 3 AdamW lrs) and prints a summary table.

Configs:
  Muon  : lr in {0.01, 0.02, 0.04}
  AdamW : lr in {5e-4, 1e-3, 2e-3}
  All runs: ResNet-50, seed=42, 5 epochs, batch_size=128

Output: Each run ends with:
  [SWEEP] optimizer=X lr=Y best_val_acc=Z%

Usage:
  python resnet50_lr_sweep_tinyimagenet.py            # default gpu=0
  python resnet50_lr_sweep_tinyimagenet.py --gpu 2    # use gpu 2
"""
import argparse
import re
import subprocess
import sys
import time

SWEEP_CONFIGS = [
    {"optimizer": "muon", "lr_flag": "--muon-lr", "lr": 0.01},
    {"optimizer": "muon", "lr_flag": "--muon-lr", "lr": 0.02},
    {"optimizer": "muon", "lr_flag": "--muon-lr", "lr": 0.04},
    {"optimizer": "adamw", "lr_flag": "--lr", "lr": 5e-4},
    {"optimizer": "adamw", "lr_flag": "--lr", "lr": 1e-3},
    {"optimizer": "adamw", "lr_flag": "--lr", "lr": 2e-3},
]

TRAIN_SCRIPT = "/root/spectral_optim_vision_geometry/tiny_imagenet_train.py"
EPOCHS = 5
SEED = 42
BATCH_SIZE = 128
MODEL = "resnet50"


def run_one(cfg, gpu):
    cmd = [
        sys.executable, TRAIN_SCRIPT,
        "--model", MODEL,
        "--optimizer", cfg["optimizer"],
        "--gpu", str(gpu),
        "--seed", str(SEED),
        "--epochs", str(EPOCHS),
        "--batch-size", str(BATCH_SIZE),
        cfg["lr_flag"], str(cfg["lr"]),
    ]
    tag = f"{cfg['optimizer']} lr={cfg['lr']}"
    print(f"\n{'='*60}", flush=True)
    print(f">>> [{tag}] Starting", flush=True)
    print(f"    cmd: {' '.join(cmd)}", flush=True)
    print(f"{'='*60}", flush=True)

    t0 = time.time()
    best_acc = None
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, bufsize=1,
    )
    for line in proc.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()
        m = re.search(r"TRAINING_COMPLETE.*val_acc=([\d.]+)%", line)
        if m:
            best_acc = float(m.group(1))
    proc.wait()
    elapsed = time.time() - t0

    if proc.returncode != 0:
        print(f"[SWEEP] optimizer={cfg['optimizer']} lr={cfg['lr']} FAILED (exit={proc.returncode})", flush=True)
        return None

    if best_acc is not None:
        print(f"[SWEEP] optimizer={cfg['optimizer']} lr={cfg['lr']} best_val_acc={best_acc:.2f}%", flush=True)
    else:
        print(f"[SWEEP] optimizer={cfg['optimizer']} lr={cfg['lr']} best_val_acc=UNKNOWN (no TRAINING_COMPLETE line found)", flush=True)

    return {"optimizer": cfg["optimizer"], "lr": cfg["lr"], "best_val_acc": best_acc, "time": elapsed}


def main():
    parser = argparse.ArgumentParser(description="ResNet-50 Muon/AdamW lr sweep on Tiny-ImageNet")
    parser.add_argument("--gpu", type=int, default=0)
    args = parser.parse_args()

    print(f"=== ResNet-50 Tiny-ImageNet LR Sweep ===", flush=True)
    print(f"GPU: cuda:{args.gpu}, Seed: {SEED}, Epochs: {EPOCHS}", flush=True)
    print(f"Configs: {len(SWEEP_CONFIGS)} runs", flush=True)

    total_t0 = time.time()
    results = []
    for i, cfg in enumerate(SWEEP_CONFIGS, 1):
        print(f"\n[{i}/{len(SWEEP_CONFIGS)}]", flush=True)
        r = run_one(cfg, args.gpu)
        if r:
            results.append(r)

    total_elapsed = time.time() - total_t0

    print(f"\n{'='*60}", flush=True)
    print(f"=== SWEEP SUMMARY (total_time={total_elapsed:.0f}s) ===", flush=True)
    print(f"{'Optimizer':<10} {'LR':<10} {'Val Acc':>10} {'Time':>8}", flush=True)
    print(f"{'-'*40}", flush=True)
    for r in results:
        acc_str = f"{r['best_val_acc']:.2f}%" if r['best_val_acc'] is not None else "N/A"
        print(f"{r['optimizer']:<10} {r['lr']:<10} {acc_str:>10} {r['time']:>7.0f}s", flush=True)
    print(f"{'='*60}", flush=True)


if __name__ == "__main__":
    main()
