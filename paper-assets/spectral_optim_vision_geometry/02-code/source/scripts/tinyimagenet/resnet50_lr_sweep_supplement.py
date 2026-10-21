# ResNet-50 supplemental lr sweep on Tiny-ImageNet-200.
# Extends resnet50_lr_sweep_tinyimagenet.py with higher lr points:
#   Muon lr=0.06 (5ep), AdamW lr=3e-3 (5ep). seed=42.
import re
import subprocess
import sys
import time

SWEEP_CONFIGS = [
    {"optimizer": "muon", "lr_flag": "--muon-lr", "lr": 0.06},
    {"optimizer": "adamw", "lr_flag": "--lr", "lr": 3e-3},
]

TRAIN_SCRIPT = "/root/spectral_optim_vision_geometry/tiny_imagenet_train.py"
EPOCHS = 5
SEED = 42
BATCH_SIZE = 128
MODEL = "resnet50"


def run_one(cfg, gpu=0):
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
    final_loss = None
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
        m2 = re.search(r"epoch=\d+, train_loss=([\d.]+), val_acc=", line)
        if m2:
            final_loss = float(m2.group(1))
    proc.wait()
    elapsed = time.time() - t0

    if proc.returncode != 0:
        print(f"[SWEEP] {tag} FAILED (exit={proc.returncode})", flush=True)
        return None

    print(f"\n--- METRICS SUMMARY ---", flush=True)
    print(f"  optimizer={cfg['optimizer']}, lr={cfg['lr']}", flush=True)
    print(f"  best_val_acc={best_acc}%", flush=True)
    print(f"  final_train_loss={final_loss}", flush=True)
    print(f"  time={elapsed:.0f}s", flush=True)
    print(f"-----------------------", flush=True)

    return {"optimizer": cfg["optimizer"], "lr": cfg["lr"],
            "best_val_acc": best_acc, "final_train_loss": final_loss, "time": elapsed}


def main():
    print(f"=== ResNet-50 Tiny-ImageNet LR Sweep SUPPLEMENT ===", flush=True)
    print(f"GPU: cuda:0, Seed: {SEED}, Epochs: {EPOCHS}", flush=True)

    results = []
    for i, cfg in enumerate(SWEEP_CONFIGS, 1):
        print(f"\n[{i}/{len(SWEEP_CONFIGS)}]", flush=True)
        r = run_one(cfg)
        if r:
            results.append(r)

    print(f"\n{'='*60}", flush=True)
    print(f"=== SUPPLEMENT SWEEP SUMMARY ===", flush=True)
    print(f"{'Optimizer':<10} {'LR':<10} {'Val Acc':>10} {'Train Loss':>12} {'Time':>8}", flush=True)
    print(f"{'-'*52}", flush=True)
    for r in results:
        acc = f"{r['best_val_acc']:.2f}%" if r['best_val_acc'] else "N/A"
        loss = f"{r['final_train_loss']:.4f}" if r['final_train_loss'] else "N/A"
        print(f"{r['optimizer']:<10} {r['lr']:<10} {acc:>10} {loss:>12} {r['time']:>7.0f}s", flush=True)
    print(f"{'='*60}", flush=True)


if __name__ == "__main__":
    main()
