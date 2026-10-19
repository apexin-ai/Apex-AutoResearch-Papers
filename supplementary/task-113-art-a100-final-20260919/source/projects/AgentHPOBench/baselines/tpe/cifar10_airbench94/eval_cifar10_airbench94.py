#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import random
import shutil
import time
from pathlib import Path

import numpy as np
import torch


ROOT = Path(".")
REPO_DIR = ROOT / "repositories/cifar10-airbench"
RAW_CIFAR_ROOT = ROOT / "data/paper_exact/torch_conv_kan_cifar10"


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def prepare_airbench_data(data_dir: Path, raw_root: Path) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    if (data_dir / "train.pt").exists() and (data_dir / "test.pt").exists():
        return

    import torchvision

    for train, name in [(True, "train.pt"), (False, "test.pt")]:
        dataset = torchvision.datasets.CIFAR10(str(raw_root), train=train, download=False)
        payload = {
            "images": torch.tensor(dataset.data),
            "labels": torch.tensor(dataset.targets),
            "classes": dataset.classes,
        }
        torch.save(payload, data_dir / name)


def safe_symlink(src: Path, dst: Path) -> None:
    if dst.is_symlink() or dst.exists():
        if dst.is_dir() and not dst.is_symlink():
            shutil.rmtree(dst)
        else:
            dst.unlink()
    dst.symlink_to(src, target_is_directory=True)


def run(args: argparse.Namespace) -> dict[str, object]:
    if not torch.cuda.is_available() and not args.cpu:
        raise RuntimeError("Airbench requires CUDA in this benchmark harness.")

    set_seed(args.seed)
    prepare_airbench_data(args.data_dir, args.raw_root)

    import sys

    sys.path.insert(0, str(REPO_DIR))
    from airbench import CifarLoader, evaluate, train94

    work_dir = args.results_dir / "work"
    work_dir.mkdir(parents=True, exist_ok=True)
    safe_symlink(args.data_dir, work_dir / "cifar10")

    old_cwd = Path.cwd()
    os.chdir(work_dir)
    started = time.time()
    try:
        train_loader = CifarLoader(
            str(args.data_dir),
            train=True,
            batch_size=args.batch_size,
            aug={"flip": True, "translate": args.translate},
            altflip=True,
        )
        model = train94(
            train_loader=train_loader,
            epochs=args.epochs,
            label_smoothing=args.label_smoothing,
            learning_rate=args.learning_rate,
            bias_scaler=args.bias_scaler,
            momentum=args.momentum,
            weight_decay=args.weight_decay,
            whiten_bias_epochs=args.whiten_bias_epochs,
            tta_level=args.tta_level,
            run=args.seed,
            verbose=args.verbose,
        )
        test_loader = CifarLoader(str(args.data_dir), train=False, batch_size=args.eval_batch_size)
        no_tta_acc = evaluate(model, test_loader, tta_level=0)
        tta_acc = evaluate(model, test_loader, tta_level=args.tta_level)
    finally:
        os.chdir(old_cwd)

    result = {
        "task": "cifar10_airbench94",
        "repo": "cifar10-airbench",
        "dataset": "CIFAR-10",
        "data_dir": str(args.data_dir),
        "epochs": args.epochs,
        "batch_size": args.batch_size,
        "learning_rate": args.learning_rate,
        "weight_decay": args.weight_decay,
        "momentum": args.momentum,
        "label_smoothing": args.label_smoothing,
        "bias_scaler": args.bias_scaler,
        "translate": args.translate,
        "tta_level": args.tta_level,
        "whiten_bias_epochs": args.whiten_bias_epochs,
        "seed": args.seed,
        "accuracy": tta_acc,
        "accuracy_percent": 100.0 * tta_acc,
        "no_tta_accuracy": no_tta_acc,
        "no_tta_accuracy_percent": 100.0 * no_tta_acc,
        "seconds": round(time.time() - started, 3),
        "device": "cuda" if torch.cuda.is_available() and not args.cpu else "cpu",
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    (args.results_dir / "results.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data/paper_exact/cifar10_airbench")
    parser.add_argument("--raw-root", type=Path, default=RAW_CIFAR_ROOT)
    parser.add_argument("--epochs", type=float, default=3.0)
    parser.add_argument("--batch-size", type=int, default=1024)
    parser.add_argument("--eval-batch-size", type=int, default=2000)
    parser.add_argument("--learning-rate", type=float, default=11.5)
    parser.add_argument("--weight-decay", type=float, default=0.0153)
    parser.add_argument("--momentum", type=float, default=0.85)
    parser.add_argument("--label-smoothing", type=float, default=0.2)
    parser.add_argument("--bias-scaler", type=float, default=64.0)
    parser.add_argument("--translate", type=int, default=2)
    parser.add_argument("--tta-level", type=int, default=2)
    parser.add_argument("--whiten-bias-epochs", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--verbose", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--cpu", action="store_true")
    args = parser.parse_args()
    run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
