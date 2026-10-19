#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
import random
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch


ROOT = Path(".")
REPO = ROOT / "repositories/chronos-forecasting"
MODEL = ROOT / "models/amazon/chronos-t5-tiny"
DATA = ROOT / "data/formal/chronos_monash_weather/monash_weather/train-00000-of-00001.parquet"
QUANTILES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
PAPER_ANCHOR_WQL = 0.14787595319625085


def weighted_quantile_loss(y_true: np.ndarray, q_forecast: np.ndarray, quantiles: list[float]) -> float:
    denom = float(np.sum(np.abs(y_true)))
    if denom <= 1e-12:
        denom = float(len(y_true))
    losses = []
    for q_idx, q in enumerate(quantiles):
        pred = q_forecast[:, q_idx]
        diff = y_true - pred
        losses.append(2.0 * float(np.sum(np.maximum(q * diff, (q - 1.0) * diff))) / denom)
    return float(np.mean(losses))


def load_rows(args: argparse.Namespace) -> pd.DataFrame:
    if not DATA.exists():
        raise FileNotFoundError(f"missing {DATA}; run dataset_download.sh first")
    df = pd.read_parquet(DATA)
    if args.subset != "all":
        df = df[df["subset"] == args.subset].copy()
    if args.max_series > 0 and len(df) > args.max_series:
        # Deterministic stratified cap for smoke runs; formal runs keep max_series=0.
        per_subset = max(1, math.ceil(args.max_series / max(1, df["subset"].nunique())))
        parts = []
        for _, group in df.sort_values("id").groupby("subset", sort=True):
            parts.append(group.head(per_subset))
        df = pd.concat(parts, ignore_index=True).sort_values("id").head(args.max_series)
    return df.reset_index(drop=True)


def seasonal_forecast(context: np.ndarray, prediction_length: int, seasonality: int) -> np.ndarray:
    if len(context) < seasonality:
        values = np.repeat(context[-1], prediction_length)
    else:
        tail = context[-seasonality:]
        reps = int(math.ceil(prediction_length / len(tail)))
        values = np.tile(tail, reps)[:prediction_length]
    return np.repeat(values[:, None], len(QUANTILES), axis=1)


def chronos_forecast(args: argparse.Namespace, contexts: list[np.ndarray]) -> np.ndarray:
    sys.path.insert(0, str(REPO / "src"))
    from chronos import ChronosPipeline

    dtype = torch.bfloat16 if args.torch_dtype == "bfloat16" else torch.float32
    pipeline = ChronosPipeline.from_pretrained(
        str(MODEL),
        device_map=args.device,
        torch_dtype=dtype,
        local_files_only=True,
    )
    outputs = []
    for start in range(0, len(contexts), args.chunk_size):
        chunk = contexts[start : start + args.chunk_size]
        tensors = [torch.tensor(context, dtype=torch.float32) for context in chunk]
        quantiles, _ = pipeline.predict_quantiles(
            tensors,
            prediction_length=args.prediction_length,
            quantile_levels=QUANTILES,
            num_samples=args.num_samples,
            temperature=args.temperature,
            top_k=args.top_k,
            top_p=args.top_p,
        )
        outputs.append(quantiles.detach().cpu().numpy())
    del pipeline
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    return np.concatenate(outputs, axis=0)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)

    df = load_rows(args)
    if df.empty:
        raise ValueError(f"empty monash_weather selection for subset={args.subset}")

    contexts: list[np.ndarray] = []
    y_trues: list[np.ndarray] = []
    row_meta: list[tuple[str, str, int]] = []
    for row in df.itertuples(index=False):
        series = np.asarray(row.target, dtype=np.float32)
        if len(series) <= args.prediction_length + 1:
            continue
        y_true = series[-args.prediction_length :]
        history = series[: -args.prediction_length]
        context_len = len(history) if args.context_length <= 0 else min(args.context_length, len(history))
        contexts.append(history[-context_len:])
        y_trues.append(y_true)
        row_meta.append((str(row.id), str(row.subset), context_len))
    if not contexts:
        raise ValueError("no usable time series after filtering")

    started = time.time()
    if args.method == "seasonal_naive":
        forecasts = np.stack([seasonal_forecast(context, args.prediction_length, args.seasonality) for context in contexts])
    else:
        forecasts = chronos_forecast(args, contexts)

    per_subset: dict[str, list[float]] = {}
    per_series_sample = {}
    wql_values = []
    mae_values = []
    for idx, ((series_id, subset, context_len), y_true, forecast) in enumerate(zip(row_meta, y_trues, forecasts)):
        wql = weighted_quantile_loss(y_true, forecast, QUANTILES)
        median_mae = float(np.mean(np.abs(y_true - forecast[:, QUANTILES.index(0.5)])))
        per_subset.setdefault(subset, []).append(wql)
        wql_values.append(wql)
        mae_values.append(median_mae)
        if idx < 16:
            per_series_sample[series_id] = {
                "subset": subset,
                "WQL": wql,
                "median_mae": median_mae,
                "context_length": context_len,
            }

    return {
        "task": "Chronos-T5-Tiny monash_weather zero-shot forecasting",
        "repo": "chronos-forecasting",
        "dataset": "monash_weather",
        "metric": "WQL",
        "lower_is_better": True,
        "WQL": float(np.mean(wql_values)),
        "median_mae": float(np.mean(mae_values)),
        "per_subset_WQL": {name: float(np.mean(values)) for name, values in sorted(per_subset.items())},
        "per_series_sample": per_series_sample,
        "num_series": len(wql_values),
        "seconds": round(time.time() - started, 3),
        "config": {
            "method": args.method,
            "subset": args.subset,
            "prediction_length": args.prediction_length,
            "context_length": args.context_length,
            "num_samples": args.num_samples,
            "temperature": args.temperature,
            "top_k": args.top_k,
            "top_p": args.top_p,
            "seasonality": args.seasonality,
            "max_series": args.max_series,
            "chunk_size": args.chunk_size,
            "seed": args.seed,
        },
        "paper_anchor_WQL": PAPER_ANCHOR_WQL,
        "paper_anchor_source": "chronos-t5-tiny-zero-shot.csv monash_weather row",
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--method", choices=["chronos", "seasonal_naive"], default="chronos")
    parser.add_argument("--subset", choices=["all", "rain", "solar", "mintemp", "maxtemp"], default="all")
    parser.add_argument("--prediction-length", type=int, default=30)
    parser.add_argument("--context-length", type=int, default=512)
    parser.add_argument("--num-samples", type=int, default=20)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top-k", type=int, default=50)
    parser.add_argument("--top-p", type=float, default=1.0)
    parser.add_argument("--seasonality", type=int, default=365)
    parser.add_argument("--max-series", type=int, default=0)
    parser.add_argument("--chunk-size", type=int, default=64)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--torch-dtype", choices=["bfloat16", "float32"], default="bfloat16")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    args.results_dir.mkdir(parents=True, exist_ok=True)
    payload = evaluate(args)
    (args.results_dir / "results.json").write_text(json.dumps(payload, indent=2))
    print("RESULT_JSON " + json.dumps(payload, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
