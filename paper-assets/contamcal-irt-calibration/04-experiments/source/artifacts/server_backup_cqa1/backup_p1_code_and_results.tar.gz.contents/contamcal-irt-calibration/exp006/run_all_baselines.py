#!/usr/bin/env python3
"""Run all baseline calibration methods and compare results.

Usage:
    python run_all_baselines.py --dry-run                    # synthetic data, skip Stan
    python run_all_baselines.py --dry-run --with-stan        # synthetic data, include Stan
    python run_all_baselines.py --data-dir <path>            # real data
"""
import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baselines import ALL_BASELINES, run_all_baselines
from evaluate_calibration import evaluate_method, format_text_table

log = logging.getLogger(__name__)


def generate_synthetic_data(n_models=5, n_items=10, dosages=None, seed=42):
    rng = np.random.default_rng(seed)
    if dosages is None:
        dosages = [0, 25, 50, 75, 100]
    assert len(dosages) == n_models

    true_theta = rng.normal(0, 1, n_models)
    true_b = rng.normal(0, 1, n_items)
    true_a = np.abs(rng.normal(1, 0.3, n_items))
    true_gamma = 1.5

    all_y = np.zeros((n_models, n_items), dtype=int)
    all_exposure = np.zeros((n_models, n_items))
    true_clean_acc = np.zeros(n_models)

    for i in range(n_models):
        dose_frac = dosages[i] / 100.0
        n_contam = int(dose_frac * n_items)
        contam_items = rng.choice(n_items, n_contam, replace=False) if n_contam > 0 else []

        for j in range(n_items):
            eta_clean = true_a[j] * (true_theta[i] - true_b[j])
            p_clean = 1.0 / (1.0 + np.exp(-eta_clean))

            if j in contam_items:
                exposure = rng.uniform(0.5, 1.0)
                all_exposure[i, j] = exposure
                eta_contam = eta_clean + true_gamma * exposure
                p_contam = 1.0 / (1.0 + np.exp(-eta_contam))
                all_y[i, j] = int(rng.random() < p_contam)
            else:
                all_exposure[i, j] = rng.uniform(0, 0.1)
                all_y[i, j] = int(rng.random() < p_clean)

            true_clean_acc[i] += p_clean
        true_clean_acc[i] /= n_items

    model_names = [f"model_{d}pct" for d in dosages]
    return {
        "all_y": all_y,
        "all_exposure": all_exposure,
        "true_clean_acc": true_clean_acc,
        "dosages": dosages,
        "model_names": model_names,
        "benchmark": "synthetic",
        "true_gamma": true_gamma,
    }


def main():
    parser = argparse.ArgumentParser(description="Run all baseline calibration methods")
    parser.add_argument("--dry-run", action="store_true", help="Use synthetic data")
    parser.add_argument("--data-dir", type=str, help="Directory with real data")
    parser.add_argument("--skip-stan", action="store_true", help="Skip Stan-based baselines")
    parser.add_argument("--with-stan", action="store_true", help="Include Stan baselines in dry-run")
    parser.add_argument("--output", type=str, default=None, help="Output JSON path")
    parser.add_argument("--n-models", type=int, default=5, help="Number of synthetic models")
    parser.add_argument("--n-items", type=int, default=10, help="Number of synthetic items")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    if args.dry_run:
        print("=== DRY RUN with synthetic data ===")
        data = generate_synthetic_data(n_models=args.n_models, n_items=args.n_items)
        skip_stan = not args.with_stan
    elif args.data_dir:
        data_path = Path(args.data_dir)
        all_y = np.load(data_path / "all_y.npy")
        all_exposure = np.load(data_path / "all_exposure.npy")
        with open(data_path / "metadata.json") as f:
            meta = json.load(f)
        data = {
            "all_y": all_y,
            "all_exposure": all_exposure,
            "model_names": meta["model_names"],
            "benchmark": meta["benchmark"],
            "true_clean_acc": np.array(meta.get("true_clean_acc", [np.nan] * all_y.shape[0])),
            "dosages": meta.get("dosages", [0] * all_y.shape[0]),
        }
        skip_stan = args.skip_stan
    else:
        parser.error("Specify --dry-run or --data-dir")

    y = data["all_y"]
    exposure = data["all_exposure"]
    dosages = data["dosages"]
    true_clean_acc = data["true_clean_acc"]

    print(f"Data: {y.shape[0]} models x {y.shape[1]} items")
    print(f"Dosages: {dosages}")
    print(f"True clean acc: {[f'{a:.4f}' for a in true_clean_acc]}")
    print(f"Observed acc:   {[f'{a:.4f}' for a in y.mean(axis=1)]}")

    # Run baselines via unified interface
    results = run_all_baselines(y, exposure, skip_stan=skip_stan)

    # Evaluate
    all_metrics = []
    for bname, bdata in results.items():
        if "error" in bdata:
            log.warning("Skipping %s: %s", bname, bdata["error"])
            continue
        m = evaluate_method(
            method_name=bname,
            scores=bdata["calibrated_scores"],
            ground_truth=true_clean_acc.tolist(),
            ci_lower=bdata.get("ci_lower"),
            ci_upper=bdata.get("ci_upper"),
            ci_80_lower=bdata.get("ci_80_lower"),
            ci_80_upper=bdata.get("ci_80_upper"),
            ci_50_lower=bdata.get("ci_50_lower"),
            ci_50_upper=bdata.get("ci_50_upper"),
            dosages=dosages,
        )
        all_metrics.append(m)

    print(f"\n{'='*80}")
    print(format_text_table(all_metrics))

    if args.output:
        out = {
            "metrics": all_metrics,
            "baseline_results": {k: v for k, v in results.items() if "error" not in v},
            "data_info": {
                "n_models": int(y.shape[0]),
                "n_items": int(y.shape[1]),
                "dosages": list(dosages) if isinstance(dosages, np.ndarray) else dosages,
                "true_clean_acc": true_clean_acc.tolist(),
            },
        }
        with open(args.output, "w") as f:
            json.dump(out, f, indent=2, default=str)
        print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
