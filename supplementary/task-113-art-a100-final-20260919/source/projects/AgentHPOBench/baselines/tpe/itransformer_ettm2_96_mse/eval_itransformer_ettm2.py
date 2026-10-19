#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path


ROOT = Path(".")
REPO = ROOT / "repositories/iTransformer"
DATA_ROOT = ROOT / "data/formal/ett_diverse/ETT-small"
PAPER_ANCHOR_MSE = 0.180
PAPER_ANCHOR_MAE = 0.264


def parse_metric(text: str) -> dict[str, float | int | None]:
    metric_matches = re.findall(r"mse:([0-9.eE+-]+), mae:([0-9.eE+-]+)", text)
    if not metric_matches:
        raise RuntimeError("Could not parse final mse/mae from iTransformer output")
    mse, mae = map(float, metric_matches[-1])
    train_losses = [float(x) for x in re.findall(r"Train Loss:\s*([0-9.eE+-]+)", text)]
    val_losses = [float(x) for x in re.findall(r"Vali Loss:\s*([0-9.eE+-]+)", text)]
    test_losses = [float(x) for x in re.findall(r"Test Loss:\s*([0-9.eE+-]+)", text)]
    epochs_ran = len(train_losses)
    return {
        "test_mse": mse,
        "test_mae": mae,
        "train_loss_final": train_losses[-1] if train_losses else None,
        "val_loss_final": val_losses[-1] if val_losses else None,
        "test_loss_epoch_final": test_losses[-1] if test_losses else None,
        "epochs_ran": epochs_ran,
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    args.results_dir.mkdir(parents=True, exist_ok=True)
    ckpt_dir = args.results_dir / "checkpoints"
    if args.clean and ckpt_dir.exists():
        shutil.rmtree(ckpt_dir)
    cmd = [
        "python",
        "-u",
        "run.py",
        "--is_training",
        "1",
        "--root_path",
        str(DATA_ROOT),
        "--data_path",
        "ETTm2.csv",
        "--model_id",
        f"autorep_ETTm2_96_96_{args.run_name}",
        "--model",
        "iTransformer",
        "--data",
        "ETTm2",
        "--features",
        "M",
        "--seq_len",
        "96",
        "--pred_len",
        "96",
        "--e_layers",
        str(args.e_layers),
        "--enc_in",
        "7",
        "--dec_in",
        "7",
        "--c_out",
        "7",
        "--des",
        "AgentHPOBench",
        "--d_model",
        str(args.d_model),
        "--d_ff",
        str(args.d_ff),
        "--n_heads",
        str(args.n_heads),
        "--dropout",
        str(args.dropout),
        "--itr",
        "1",
        "--train_epochs",
        str(args.epochs),
        "--batch_size",
        str(args.batch_size),
        "--patience",
        str(args.patience),
        "--learning_rate",
        str(args.learning_rate),
        "--num_workers",
        "0",
        "--checkpoints",
        str(ckpt_dir),
    ]
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = os.environ.get("ITRANSFORMER_CUDA_VISIBLE_DEVICES", env.get("CUDA_VISIBLE_DEVICES", "1"))
    env["PYTHONPATH"] = f"{REPO}:{ROOT / '.python_deps'}"
    start = time.time()
    proc = subprocess.run(cmd, cwd=str(REPO), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    text = proc.stdout.decode("utf-8", errors="replace")
    (args.results_dir / "eval.log").write_text(text)
    if proc.returncode != 0:
        print(text, flush=True)
        raise RuntimeError(f"iTransformer run failed rc={proc.returncode}")
    metrics = parse_metric(text)
    payload = {
        "task": "iTransformer ETTm2 multivariate forecasting",
        "repo": "iTransformer",
        "dataset": "ETTm2",
        "metric": "mse",
        "paper_anchor_mse": PAPER_ANCHOR_MSE,
        "paper_anchor_mae": PAPER_ANCHOR_MAE,
        "paper_anchor_source": "iTransformer ICLR 2024 official long-term forecasting results for ETTm2 pred_len=96: MSE=0.180, MAE=0.264.",
        "seq_len": 96,
        "pred_len": 96,
        "d_model": args.d_model,
        "d_ff": args.d_ff,
        "n_heads": args.n_heads,
        "e_layers": args.e_layers,
        "dropout": args.dropout,
        "learning_rate": args.learning_rate,
        "batch_size": args.batch_size,
        "epochs": args.epochs,
        "patience": args.patience,
        "seconds": round(time.time() - start, 3),
        "cuda_visible_devices": env.get("CUDA_VISIBLE_DEVICES"),
        **metrics,
    }
    (args.results_dir / "results.json").write_text(json.dumps(payload, indent=2))
    print("RESULT_JSON " + json.dumps(payload, sort_keys=True), flush=True)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--run-name", default="run")
    parser.add_argument("--d-model", type=int, default=64)
    parser.add_argument("--d-ff", type=int, default=64)
    parser.add_argument("--n-heads", type=int, default=4)
    parser.add_argument("--e-layers", type=int, default=1)
    parser.add_argument("--dropout", type=float, default=0.1)
    parser.add_argument("--learning-rate", type=float, default=0.001)
    parser.add_argument("--batch-size", type=int, default=512)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--patience", type=int, default=2)
    parser.add_argument("--clean", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()
    run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
