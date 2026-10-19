#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import numpy as np
import pandas as pd


EPS = 1e-7
BOUNDARIES = (8640, 11520, 14400)


def parse_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    value = str(value).strip().lower()
    if value in {"1", "true", "yes", "y", "on"}:
        return True
    if value in {"0", "false", "no", "n", "off"}:
        return False
    raise argparse.ArgumentTypeError(f"invalid bool value: {value}")


def load_etth1(data_path: Path, normalize: bool) -> tuple[np.ndarray, list[str]]:
    df = pd.read_csv(data_path)
    ts_cols = [col for col in df.columns if col != "date"]
    data = df[ts_cols].to_numpy(dtype=np.float32).T[:, : BOUNDARIES[2]]
    if normalize:
        train = data[:, : BOUNDARIES[0]]
        mean = train.mean(axis=1, keepdims=True)
        std = train.std(axis=1, keepdims=True)
        std = np.where(std > EPS, std, 1.0)
        data = (data - mean) / std
    return data, ts_cols


def smape(y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
    abs_diff = np.abs(y_pred - y_true)
    abs_val = (np.abs(y_true) + np.abs(y_pred)) / 2
    abs_val = np.where(abs_val > EPS, abs_val, 1.0)
    abs_diff = np.where(abs_val > EPS, abs_diff, 0.0)
    return abs_diff / abs_val


def build_model(args: argparse.Namespace):
    import timesfm

    return timesfm.TimesFm(
        hparams=timesfm.TimesFmHparams(
            backend=args.backend,
            per_core_batch_size=args.per_core_batch_size,
            horizon_len=128,
            context_len=args.context_len,
        ),
        checkpoint=timesfm.TimesFmCheckpoint(path=str(args.model_path)),
    )


def run_eval(args: argparse.Namespace) -> dict[str, object]:
    import timesfm

    data, ts_cols = load_etth1(args.data_path, args.normalize)
    batch_size = min(args.batch_size, len(ts_cols))
    idxs = np.arange(BOUNDARIES[1], BOUNDARIES[2] - args.pred_len + 1, args.pred_len)
    if args.max_windows:
        idxs = idxs[: args.max_windows]

    model = build_model(args)
    int_freq = timesfm.freq_map("H")
    window_size = args.window_size if args.window_size > 0 else None

    mae_sum = 0.0
    mse_sum = 0.0
    smape_sum = 0.0
    abs_sum = 0.0
    num_elements = 0
    start = time.time()

    for idx in idxs:
        hist_start = idx - args.context_len
        if hist_start < 0:
            raise ValueError(f"context_len={args.context_len} exceeds available history at idx={idx}")
        for batch_start in range(0, len(ts_cols), batch_size):
            batch_end = min(batch_start + batch_size, len(ts_cols))
            past = data[batch_start:batch_end, hist_start:idx]
            actuals = data[batch_start:batch_end, idx : idx + args.pred_len]
            freqs = [int_freq] * past.shape[0]
            _, full_forecast = model.forecast(
                list(past),
                freqs,
                window_size=window_size,
                forecast_context_len=args.context_len,
            )
            if full_forecast.shape[-1] > 5:
                forecasts = full_forecast[:, : actuals.shape[1], 5]
            else:
                forecasts = full_forecast[:, : actuals.shape[1], 0]
            diff = forecasts - actuals
            mae_sum += np.abs(diff).sum()
            mse_sum += np.square(diff).sum()
            smape_sum += smape(forecasts, actuals).sum()
            abs_sum += np.abs(actuals).sum()
            num_elements += actuals.shape[0] * actuals.shape[1]

    mse = mse_sum / num_elements
    result = {
        "dataset": "etth1",
        "pred_len": args.pred_len,
        "context_len": args.context_len,
        "normalize": args.normalize,
        "window_size": args.window_size,
        "per_core_batch_size": args.per_core_batch_size,
        "batch_size": batch_size,
        "num_windows": int(len(idxs)),
        "num_elements": int(num_elements),
        "mse": float(mse),
        "mae": float(mae_sum / num_elements),
        "smape": float(smape_sum / num_elements),
        "wape": float(mae_sum / abs_sum),
        "nrmse": float(np.sqrt(mse) / (abs_sum / num_elements)),
        "abs_sum": float(abs_sum),
        "seconds": round(time.time() - start, 3),
        "model_path": str(args.model_path),
        "data_path": str(args.data_path),
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    (args.results_dir / "results.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-path", type=Path, required=True)
    parser.add_argument("--model-path", type=Path, required=True)
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--context-len", type=int, default=512)
    parser.add_argument("--pred-len", type=int, default=96)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--per-core-batch-size", type=int, default=32)
    parser.add_argument("--normalize", type=parse_bool, default=True)
    parser.add_argument("--window-size", type=int, default=0)
    parser.add_argument("--backend", choices=["cpu", "gpu"], default="gpu")
    parser.add_argument("--max-windows", type=int, default=0)
    args = parser.parse_args()
    run_eval(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
