"""Run budgeted confusion-estimation experiments for EC-HTE.

Inputs:
    Synthetic DGP controls, expert-label budgets, replication count, and output
    path supplied via command line flags.

Outputs:
    A JSON file with budget curves for CATE RMSE, subgroup bias, and confusion
    matrix recovery error for global, independent subgroup, and partial-pooling
    confusion estimators.

Key dependencies:
    numpy for simulation. torch is optional and used only to touch the assigned
    GPU so the submitted job verifies CUDA visibility when available.
"""

from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import numpy as np


METHODS = ("global", "independent", "partial_pooling")


def transition_matrix(error_rates: np.ndarray) -> np.ndarray:
    """Build P(observed subgroup | true subgroup) from row-specific error rates."""

    k = len(error_rates)
    matrix = np.zeros((k, k), dtype=float)
    for g, error in enumerate(error_rates):
        error = float(np.clip(error, 1e-4, 0.60))
        matrix[g, :] = error / (k - 1)
        matrix[g, g] = 1.0 - error
    return matrix


def simulate_observed_groups(
    rng: np.random.Generator,
    true_groups: np.ndarray,
    error_rates: np.ndarray,
) -> np.ndarray:
    """Sample noisy observed subgroup labels using row-specific symmetric errors."""

    k = len(error_rates)
    observed = true_groups.copy()
    for g, error in enumerate(error_rates):
        idx = np.flatnonzero(true_groups == g)
        flips = rng.random(len(idx)) < error
        if flips.any():
            offsets = rng.integers(1, k, size=int(flips.sum()))
            observed[idx[flips]] = (g + offsets) % k
    return observed


def difference_in_means(y: np.ndarray, treatment: np.ndarray, groups: np.ndarray, k: int) -> np.ndarray:
    """Estimate subgroup CATE values by treatment-control difference in means."""

    estimates = np.zeros(k, dtype=float)
    for g in range(k):
        mask = groups == g
        treated = mask & (treatment == 1)
        control = mask & (treatment == 0)
        if treated.sum() == 0 or control.sum() == 0:
            estimates[g] = np.nan
        else:
            estimates[g] = y[treated].mean() - y[control].mean()
    return estimates


def corrected_tau(
    observed_tau: np.ndarray,
    observed_probs: np.ndarray,
    true_probs: np.ndarray,
    correction_matrix: np.ndarray,
) -> np.ndarray:
    """Recover true subgroup effects from observed subgroup effects."""

    rhs = observed_probs * observed_tau
    try:
        weighted_tau = np.linalg.solve(correction_matrix.T, rhs)
    except np.linalg.LinAlgError:
        weighted_tau = np.linalg.pinv(correction_matrix.T) @ rhs
    return weighted_tau / true_probs


def estimate_error_rates(
    true_expert: np.ndarray,
    observed_expert: np.ndarray,
    k: int,
    method: str,
    shrinkage_strength: float,
) -> np.ndarray:
    """Estimate row-specific misclassification error rates from expert labels."""

    row_n = np.bincount(true_expert, minlength=k).astype(float)
    row_errors = np.zeros(k, dtype=float)
    for g in range(k):
        mask = true_expert == g
        row_errors[g] = float(np.sum(observed_expert[mask] != g))

    total_errors = float(np.sum(true_expert != observed_expert))
    global_error = (total_errors + 0.5) / (len(true_expert) + 1.0)

    if method == "global":
        return np.full(k, global_error, dtype=float)

    independent = (row_errors + 0.5) / (row_n + 1.0)
    if method == "independent":
        return np.clip(independent, 1e-4, 0.60)

    if method == "partial_pooling":
        weights = row_n / (row_n + shrinkage_strength)
        pooled = weights * independent + (1.0 - weights) * global_error
        return np.clip(pooled, 1e-4, 0.60)

    raise ValueError(f"Unknown method: {method}")


def confusion_recovery_rmse(estimated: np.ndarray, truth: np.ndarray) -> float:
    """Compute RMSE between estimated and true confusion matrices."""

    return float(np.sqrt(np.mean(np.square(estimated - truth))))


def simulate_dataset(
    rng: np.random.Generator,
    n: int,
    true_probs: np.ndarray,
    true_tau: np.ndarray,
    error_rates: np.ndarray,
    outcome_sd: float,
) -> Dict[str, np.ndarray]:
    """Generate one full noisy-label HTE dataset."""

    k = len(true_probs)
    true_groups = rng.choice(k, size=n, p=true_probs)
    observed_groups = simulate_observed_groups(rng, true_groups, error_rates)
    treatment = rng.binomial(1, 0.5, size=n)
    baseline = np.linspace(0.0, 0.2, k)
    y = baseline[true_groups] + true_tau[true_groups] * treatment + rng.normal(0.0, outcome_sd, size=n)
    return {
        "true_groups": true_groups,
        "observed_groups": observed_groups,
        "treatment": treatment,
        "y": y,
    }


def run_replication(
    rng: np.random.Generator,
    n: int,
    budgets: Iterable[int],
    true_probs: np.ndarray,
    true_tau: np.ndarray,
    error_rates: np.ndarray,
    shrinkage_strength: float,
    outcome_sd: float,
) -> Dict[int, Dict[str, Dict[str, float]]]:
    """Run all budget/method combinations for one synthetic replication."""

    k = len(true_probs)
    data = simulate_dataset(rng, n, true_probs, true_tau, error_rates, outcome_sd)
    observed_tau = difference_in_means(data["y"], data["treatment"], data["observed_groups"], k)
    observed_probs = np.bincount(data["observed_groups"], minlength=k) / n
    true_transition = transition_matrix(error_rates)

    results: Dict[int, Dict[str, Dict[str, float]]] = {}
    for budget in budgets:
        if budget > n:
            raise ValueError(f"Budget B={budget} exceeds n={n}")

        expert_idx = rng.choice(n, size=budget, replace=False)
        true_expert = data["true_groups"][expert_idx]
        observed_expert = data["observed_groups"][expert_idx]
        results[budget] = {}

        for method in METHODS:
            estimated_errors = estimate_error_rates(
                true_expert=true_expert,
                observed_expert=observed_expert,
                k=k,
                method=method,
                shrinkage_strength=shrinkage_strength,
            )
            estimated_transition = transition_matrix(estimated_errors)
            tau_hat = corrected_tau(observed_tau, observed_probs, true_probs, estimated_transition)
            bias = tau_hat - true_tau
            results[budget][method] = {
                "cate_rmse": float(np.sqrt(np.mean(np.square(bias)))),
                "mean_abs_subgroup_bias": float(np.mean(np.abs(bias))),
                "max_abs_subgroup_bias": float(np.max(np.abs(bias))),
                "confusion_recovery_rmse": confusion_recovery_rmse(estimated_transition, true_transition),
            }

    return results


def summarize(metric_values: List[float]) -> Dict[str, float]:
    """Summarize one metric across replications."""

    arr = np.asarray(metric_values, dtype=float)
    return {
        "mean": float(arr.mean()),
        "sd": float(arr.std(ddof=1)) if len(arr) > 1 else 0.0,
        "p10": float(np.quantile(arr, 0.10)),
        "p50": float(np.quantile(arr, 0.50)),
        "p90": float(np.quantile(arr, 0.90)),
    }


def touch_gpu() -> Dict[str, object]:
    """Return CUDA visibility information and briefly exercise the GPU if torch exists."""

    info: Dict[str, object] = {
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES", ""),
        "torch_available": False,
        "cuda_available": False,
    }
    try:
        import torch

        info["torch_available"] = True
        info["torch_version"] = torch.__version__
        info["cuda_available"] = bool(torch.cuda.is_available())
        if torch.cuda.is_available():
            device_name = torch.cuda.get_device_name(0)
            x = torch.randn((1024, 1024), device="cuda")
            for _ in range(8):
                x = x @ x.T / math.sqrt(x.shape[0])
            torch.cuda.synchronize()
            info["gpu_name"] = device_name
            info["gpu_probe_sum"] = float(x[:2, :2].sum().detach().cpu().item())
    except Exception as exc:  # pragma: no cover - environment diagnostic only.
        info["gpu_probe_error"] = repr(exc)
    return info


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=10000)
    parser.add_argument("--reps", type=int, default=300)
    parser.add_argument("--seed", type=int, default=20260531)
    parser.add_argument("--budgets", type=int, nargs="+", default=[100, 500, 1000, 2000])
    parser.add_argument("--shrinkage-strength", type=float, default=80.0)
    parser.add_argument("--out", type=Path, default=Path("docs/results/e002_budgeted_confusion_estimation.json"))
    return parser.parse_args()


def main() -> None:
    """Run the budgeted confusion-estimation experiment and write JSON output."""

    args = parse_args()
    rng = np.random.default_rng(args.seed)

    # Six imbalanced groups make B=100 genuinely sparse for rare subgroups,
    # matching the small-budget CATE setting where partial pooling should help.
    true_probs = np.array([0.30, 0.22, 0.18, 0.13, 0.10, 0.07], dtype=float)
    true_tau = np.array([0.05, 0.12, 0.20, 0.32, 0.45, 0.60], dtype=float)
    error_rates = np.array([0.04, 0.08, 0.12, 0.18, 0.26, 0.35], dtype=float)

    raw: Dict[int, Dict[str, Dict[str, List[float]]]] = {
        budget: {method: {} for method in METHODS} for budget in args.budgets
    }
    for _ in range(args.reps):
        rep = run_replication(
            rng=rng,
            n=args.n,
            budgets=args.budgets,
            true_probs=true_probs,
            true_tau=true_tau,
            error_rates=error_rates,
            shrinkage_strength=args.shrinkage_strength,
            outcome_sd=1.0,
        )
        for budget in args.budgets:
            for method in METHODS:
                for metric, value in rep[budget][method].items():
                    raw[budget][method].setdefault(metric, []).append(value)

    budget_curve: Dict[str, Dict[str, Dict[str, Dict[str, float]]]] = {}
    for budget in args.budgets:
        budget_curve[str(budget)] = {}
        for method in METHODS:
            budget_curve[str(budget)][method] = {
                metric: summarize(values) for metric, values in raw[budget][method].items()
            }

    result = {
        "exp_id": "e002_budgeted_confusion_estimation",
        "parent": "e001_global_correction_smoke",
        "hypothesis": (
            "Under finite expert annotation budgets, hierarchical/partial-pooling confusion estimation "
            "reduces subgroup CATE RMSE more than global pooled correction and is more stable than "
            "independent subgroup estimation when B is small."
        ),
        "seed": args.seed,
        "n": args.n,
        "reps": args.reps,
        "budgets": args.budgets,
        "true_probs": true_probs.tolist(),
        "true_tau": true_tau.tolist(),
        "error_rates": error_rates.tolist(),
        "methods": list(METHODS),
        "gpu_probe": touch_gpu(),
        "budget_curve": budget_curve,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
