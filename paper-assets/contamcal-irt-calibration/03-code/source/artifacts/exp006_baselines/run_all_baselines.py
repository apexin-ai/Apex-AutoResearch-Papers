#!/usr/bin/env python3
"""Run all baseline calibration methods and compare results.

Usage:
    python run_all_baselines.py --dry-run           # synthetic data validation
    python run_all_baselines.py --data-dir <path>    # real data
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baselines import ALL_BASELINES


# ---------------------------------------------------------------------------
# Synthetic data generation
# ---------------------------------------------------------------------------

def generate_synthetic_data(n_models=5, n_items=10, dosages=None, seed=42):
    """Generate synthetic IRT data with known contamination effect.

    Returns dict with keys: all_y, all_exposure, true_theta, true_clean_acc,
    dosages, model_names, benchmark.
    """
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
        "true_theta": true_theta,
        "true_clean_acc": true_clean_acc,
        "dosages": dosages,
        "model_names": model_names,
        "benchmark": "synthetic",
        "true_gamma": true_gamma,
    }


# ---------------------------------------------------------------------------
# Evaluation metrics
# ---------------------------------------------------------------------------

def compute_metrics(results, true_clean_acc, dosages):
    """Compute 5 evaluation metrics across all baselines.

    Returns dict: {method_name: {metric: value}}.
    """
    metrics = {}
    for method, method_results in results.items():
        cal_accs = [r["calibrated_accuracy"] for r in method_results]
        ci_los = [r["ci_lower"] for r in method_results]
        ci_his = [r["ci_upper"] for r in method_results]

        valid = [i for i in range(len(cal_accs)) if not np.isnan(cal_accs[i])]
        if not valid:
            metrics[method] = {
                "mae": np.nan, "coverage_95": np.nan, "sharpness": np.nan,
                "kendall_tau": np.nan, "dose_monotonicity": np.nan,
            }
            continue

        # 1. MAE
        mae = np.mean([abs(cal_accs[i] - true_clean_acc[i]) for i in valid])

        # 2. Coverage (95% CI)
        covered = sum(1 for i in valid
                       if ci_los[i] <= true_clean_acc[i] <= ci_his[i])
        coverage = covered / len(valid)

        # 3. Sharpness (CI width)
        widths = [ci_his[i] - ci_los[i] for i in valid]
        sharpness = np.mean(widths)

        # 4. Kendall tau (rank correlation of calibrated vs true)
        cal_valid = [cal_accs[i] for i in valid]
        true_valid = [true_clean_acc[i] for i in valid]
        if len(valid) >= 3:
            tau, _ = stats.kendalltau(cal_valid, true_valid)
        else:
            tau = np.nan

        # 5. Dose-response monotonicity
        dose_valid = [(dosages[i], cal_accs[i] - true_clean_acc[i]) for i in valid]
        dose_valid.sort(key=lambda x: x[0])
        if len(dose_valid) >= 3:
            dose_vals = [d[0] for d in dose_valid]
            effect_vals = [d[1] for d in dose_valid]
            mono_tau, _ = stats.kendalltau(dose_vals, effect_vals)
        else:
            mono_tau = np.nan

        metrics[method] = {
            "mae": float(mae),
            "coverage_95": float(coverage),
            "sharpness": float(sharpness),
            "kendall_tau": float(tau) if not np.isnan(tau) else np.nan,
            "dose_monotonicity": float(mono_tau) if not np.isnan(mono_tau) else np.nan,
        }
    return metrics


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_baselines(data, skip_stan=False):
    """Run all baselines on the given data.

    Returns: {method_name: [result_per_model]}.
    """
    all_y = data["all_y"]
    all_exposure = data["all_exposure"]
    model_names = data["model_names"]
    benchmark = data["benchmark"]
    n_models = all_y.shape[0]

    methods_to_run = dict(ALL_BASELINES)
    if skip_stan:
        methods_to_run.pop("vanilla_4pl", None)
        methods_to_run.pop("single_signal_2pl_gamma", None)

    results = {}
    for method_name, calibrate_fn in methods_to_run.items():
        print(f"  Running {method_name}...", end=" ", flush=True)
        t0 = time.time()
        method_results = []

        for i in range(n_models):
            kwargs = {}
            if method_name in ("vanilla_4pl", "single_signal_2pl_gamma"):
                kwargs.update({
                    "all_y": all_y,
                    "all_exposure": all_exposure,
                    "model_idx": i,
                })
            try:
                r = calibrate_fn(
                    model_name=model_names[i],
                    benchmark=benchmark,
                    item_scores=all_y[i],
                    exposure_scores=all_exposure[i],
                    **kwargs,
                )
            except Exception as e:
                r = {
                    "calibrated_accuracy": np.nan,
                    "ci_lower": np.nan,
                    "ci_upper": np.nan,
                    "method_name": method_name,
                    "details": {"error": str(e)},
                }
            method_results.append(r)
        elapsed = time.time() - t0
        print(f"done ({elapsed:.1f}s)")
        results[method_name] = method_results

    return results


def print_comparison_table(results, data, metrics):
    """Print formatted comparison table."""
    model_names = data["model_names"]
    true_clean_acc = data["true_clean_acc"]
    dosages = data["dosages"]
    n_models = len(model_names)

    print("\n" + "=" * 100)
    print("BASELINE COMPARISON TABLE")
    print("=" * 100)

    # Per-model results
    header = f"{'Method':<25} "
    for i in range(n_models):
        header += f"{'D=' + str(dosages[i]) + '%':>14} "
    print(header)
    print("-" * 100)

    # True clean accuracy
    row = f"{'TRUE_CLEAN':<25} "
    for i in range(n_models):
        row += f"{true_clean_acc[i]:>14.4f} "
    print(row)

    # Raw observed accuracy
    row = f"{'OBSERVED':<25} "
    for i in range(n_models):
        row += f"{np.mean(data['all_y'][i]):>14.4f} "
    print(row)
    print("-" * 100)

    for method, method_results in results.items():
        row = f"{method:<25} "
        for i in range(n_models):
            r = method_results[i]
            acc = r["calibrated_accuracy"]
            if np.isnan(acc):
                row += f"{'NaN':>14} "
            else:
                row += f"{acc:>14.4f} "
        print(row)

    # Metrics table
    print("\n" + "=" * 80)
    print("EVALUATION METRICS")
    print("=" * 80)
    print(f"{'Method':<25} {'MAE':>8} {'Cov95':>8} {'Sharp':>8} {'KTau':>8} {'DoseMon':>8}")
    print("-" * 80)
    for method, m in metrics.items():
        print(f"{method:<25} "
              f"{m['mae']:>8.4f} "
              f"{m['coverage_95']:>8.2f} "
              f"{m['sharpness']:>8.4f} "
              f"{m['kendall_tau']:>8.4f} "
              f"{m['dose_monotonicity']:>8.4f}")


def main():
    parser = argparse.ArgumentParser(description="Run all baseline calibration methods")
    parser.add_argument("--dry-run", action="store_true", help="Use synthetic data")
    parser.add_argument("--data-dir", type=str, help="Directory with real data")
    parser.add_argument("--skip-stan", action="store_true", help="Skip Stan-based baselines")
    parser.add_argument("--output", type=str, default=None, help="Output JSON path")
    parser.add_argument("--n-models", type=int, default=5, help="Number of synthetic models")
    parser.add_argument("--n-items", type=int, default=10, help="Number of synthetic items")
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN with synthetic data ===")
        data = generate_synthetic_data(n_models=args.n_models, n_items=args.n_items)
        print(f"Generated: {data['all_y'].shape[0]} models × {data['all_y'].shape[1]} items")
        print(f"Dosages: {data['dosages']}")
        print(f"True clean accuracies: {[f'{a:.4f}' for a in data['true_clean_acc']]}")
        print()
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
    else:
        parser.error("Specify --dry-run or --data-dir")

    results = run_baselines(data, skip_stan=args.skip_stan)
    metrics = compute_metrics(results, data["true_clean_acc"], data["dosages"])
    print_comparison_table(results, data, metrics)

    if args.output:
        out = {
            "results": {},
            "metrics": metrics,
            "data_info": {
                "n_models": int(data["all_y"].shape[0]),
                "n_items": int(data["all_y"].shape[1]),
                "dosages": data["dosages"],
                "true_clean_acc": data["true_clean_acc"].tolist(),
            },
        }
        for method, mr in results.items():
            out["results"][method] = []
            for r in mr:
                r_copy = dict(r)
                r_copy["details"] = {k: (v if not isinstance(v, float) or not np.isnan(v) else None)
                                     for k, v in r.get("details", {}).items()}
                out["results"][method].append(r_copy)
        with open(args.output, "w") as f:
            json.dump(out, f, indent=2, default=str)
        print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
