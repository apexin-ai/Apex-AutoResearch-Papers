"""Evaluate uncertainty estimates for partial-pooling EC-HTE correction.

Inputs:
    Synthetic DGP controls, expert-label budget, replication count, bootstrap
    count, and output path supplied via command line flags.

Outputs:
    A JSON file summarizing CI coverage, interval width, and CATE RMSE for
    naive delta, sandwich-style, and paired-bootstrap intervals.

Key dependencies:
    numpy for simulation. The e002 experiment module supplies the shared DGP,
    correction, and GPU probe utilities.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from experiments.e002_budgeted_confusion_estimation import (
    corrected_tau,
    difference_in_means,
    estimate_error_rates,
    simulate_dataset,
    summarize,
    touch_gpu,
    transition_matrix,
)


METHOD = "partial_pooling"
CI_METHODS = ("naive_delta", "sandwich_delta", "paired_bootstrap")


def difference_in_means_with_se(
    y: np.ndarray,
    treatment: np.ndarray,
    groups: np.ndarray,
    k: int,
) -> Tuple[np.ndarray, np.ndarray]:
    """Estimate observed-group treatment effects and their plug-in SEs."""

    tau = np.zeros(k, dtype=float)
    se = np.zeros(k, dtype=float)
    for g in range(k):
        mask = groups == g
        treated = mask & (treatment == 1)
        control = mask & (treatment == 0)
        y_t = y[treated]
        y_c = y[control]
        tau[g] = y_t.mean() - y_c.mean()
        se[g] = np.sqrt(y_t.var(ddof=1) / len(y_t) + y_c.var(ddof=1) / len(y_c))
    return tau, se


def corrected_delta_se(
    observed_tau_se: np.ndarray,
    observed_probs: np.ndarray,
    true_probs: np.ndarray,
    correction_matrix: np.ndarray,
) -> np.ndarray:
    """Delta-method SE after linear EC correction, ignoring matrix uncertainty."""

    transform = np.diag(1.0 / true_probs) @ np.linalg.pinv(correction_matrix.T) @ np.diag(observed_probs)
    covariance = transform @ np.diag(np.square(observed_tau_se)) @ transform.T
    return np.sqrt(np.clip(np.diag(covariance), 0.0, None))


def estimate_partial_pooling_matrix(
    true_expert: np.ndarray,
    observed_expert: np.ndarray,
    k: int,
    shrinkage_strength: float,
) -> np.ndarray:
    """Estimate the partial-pooling transition matrix from expert labels."""

    errors = estimate_error_rates(
        true_expert=true_expert,
        observed_expert=observed_expert,
        k=k,
        method=METHOD,
        shrinkage_strength=shrinkage_strength,
    )
    return transition_matrix(errors)


def ci_from_center_se(center: np.ndarray, se: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Build symmetric 95% normal intervals."""

    return center - 1.96 * se, center + 1.96 * se


def paired_bootstrap_ci(
    rng: np.random.Generator,
    data: Dict[str, np.ndarray],
    budget: int,
    true_probs: np.ndarray,
    shrinkage_strength: float,
    bootstrap: int,
) -> Tuple[np.ndarray, np.ndarray]:
    """Compute percentile CIs by resampling rows and expert annotations."""

    n = len(data["y"])
    k = len(true_probs)
    draws: List[np.ndarray] = []
    for _ in range(bootstrap):
        row_idx = rng.integers(0, n, size=n)
        true_groups = data["true_groups"][row_idx]
        observed_groups = data["observed_groups"][row_idx]
        treatment = data["treatment"][row_idx]
        y = data["y"][row_idx]
        observed_tau = difference_in_means(y, treatment, observed_groups, k)
        observed_probs = np.bincount(observed_groups, minlength=k) / n
        expert_idx = rng.choice(n, size=budget, replace=False)
        matrix = estimate_partial_pooling_matrix(
            true_expert=true_groups[expert_idx],
            observed_expert=observed_groups[expert_idx],
            k=k,
            shrinkage_strength=shrinkage_strength,
        )
        draws.append(corrected_tau(observed_tau, observed_probs, true_probs, matrix))

    boot = np.asarray(draws, dtype=float)
    return np.quantile(boot, 0.025, axis=0), np.quantile(boot, 0.975, axis=0)


def run_replication(
    rng: np.random.Generator,
    n: int,
    budget: int,
    true_probs: np.ndarray,
    true_tau: np.ndarray,
    error_rates: np.ndarray,
    shrinkage_strength: float,
    outcome_sd: float,
    bootstrap: int,
) -> Dict[str, Dict[str, float]]:
    """Run one CI-coverage replication for all interval methods."""

    k = len(true_probs)
    data = simulate_dataset(rng, n, true_probs, true_tau, error_rates, outcome_sd)
    observed_tau, observed_tau_se = difference_in_means_with_se(
        data["y"], data["treatment"], data["observed_groups"], k
    )
    observed_probs = np.bincount(data["observed_groups"], minlength=k) / n

    expert_idx = rng.choice(n, size=budget, replace=False)
    matrix = estimate_partial_pooling_matrix(
        true_expert=data["true_groups"][expert_idx],
        observed_expert=data["observed_groups"][expert_idx],
        k=k,
        shrinkage_strength=shrinkage_strength,
    )
    tau_hat = corrected_tau(observed_tau, observed_probs, true_probs, matrix)
    naive_se = corrected_delta_se(observed_tau_se, observed_probs, true_probs, matrix)
    naive_lo, naive_hi = ci_from_center_se(tau_hat, naive_se)

    # The sandwich-style interval adds correction-matrix uncertainty estimated
    # from the fixed expert-label sample to the outcome delta variance.
    expert_draws: List[np.ndarray] = []
    true_expert = data["true_groups"][expert_idx]
    observed_expert = data["observed_groups"][expert_idx]
    for _ in range(bootstrap):
        boot_idx = rng.integers(0, budget, size=budget)
        boot_matrix = estimate_partial_pooling_matrix(
            true_expert=true_expert[boot_idx],
            observed_expert=observed_expert[boot_idx],
            k=k,
            shrinkage_strength=shrinkage_strength,
        )
        expert_draws.append(corrected_tau(observed_tau, observed_probs, true_probs, boot_matrix))
    expert_var = np.var(np.asarray(expert_draws, dtype=float), axis=0, ddof=1)
    sandwich_se = np.sqrt(np.square(naive_se) + expert_var)
    sandwich_lo, sandwich_hi = ci_from_center_se(tau_hat, sandwich_se)

    paired_lo, paired_hi = paired_bootstrap_ci(
        rng=rng,
        data=data,
        budget=budget,
        true_probs=true_probs,
        shrinkage_strength=shrinkage_strength,
        bootstrap=bootstrap,
    )

    intervals = {
        "naive_delta": (naive_lo, naive_hi),
        "sandwich_delta": (sandwich_lo, sandwich_hi),
        "paired_bootstrap": (paired_lo, paired_hi),
    }
    out: Dict[str, Dict[str, float]] = {}
    for method, (lo, hi) in intervals.items():
        covered = (lo <= true_tau) & (true_tau <= hi)
        out[method] = {
            "coverage": float(covered.mean()),
            "mean_width": float(np.mean(hi - lo)),
            "max_miss_distance": float(np.max(np.maximum(lo - true_tau, true_tau - hi).clip(min=0.0))),
            "cate_rmse": float(np.sqrt(np.mean(np.square(tau_hat - true_tau)))),
        }
    return out


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=5000)
    parser.add_argument("--reps", type=int, default=120)
    parser.add_argument("--budget", type=int, default=1000)
    parser.add_argument("--bootstrap", type=int, default=80)
    parser.add_argument("--seed", type=int, default=20260531)
    parser.add_argument("--shrinkage-strength", type=float, default=80.0)
    parser.add_argument("--outcome-sd", type=float, default=1.0)
    parser.add_argument("--out", type=Path, default=Path("docs/results/e003_inference_coverage_ablation.json"))
    return parser.parse_args()


def main() -> None:
    """Run the CI experiment and write JSON output."""

    args = parse_args()
    rng = np.random.default_rng(args.seed)
    true_probs = np.array([0.30, 0.22, 0.18, 0.13, 0.10, 0.07], dtype=float)
    true_tau = np.array([0.05, 0.12, 0.20, 0.32, 0.45, 0.60], dtype=float)
    error_rates = np.array([0.04, 0.08, 0.12, 0.18, 0.26, 0.35], dtype=float)
    metric_values: Dict[str, Dict[str, List[float]]] = {
        method: {"coverage": [], "mean_width": [], "max_miss_distance": [], "cate_rmse": []}
        for method in CI_METHODS
    }

    gpu_probe = touch_gpu()
    for _ in range(args.reps):
        rep = run_replication(
            rng=rng,
            n=args.n,
            budget=args.budget,
            true_probs=true_probs,
            true_tau=true_tau,
            error_rates=error_rates,
            shrinkage_strength=args.shrinkage_strength,
            outcome_sd=args.outcome_sd,
            bootstrap=args.bootstrap,
        )
        for method, metrics in rep.items():
            for key, value in metrics.items():
                metric_values[method][key].append(value)

    summary = {
        method: {metric: summarize(values) for metric, values in metrics.items()}
        for method, metrics in metric_values.items()
    }
    result = {
        "exp_id": "e003_inference_coverage_ablation",
        "parent": "e002_budgeted_confusion_estimation_r1",
        "hypothesis": (
            "For finite-budget partial-pooling EC-HTE, accounting for confusion-matrix "
            "estimation uncertainty with sandwich or paired bootstrap intervals improves "
            "subgroup CATE CI coverage relative to a naive outcome-only delta interval."
        ),
        "seed": args.seed,
        "n": args.n,
        "reps": args.reps,
        "budget": args.budget,
        "bootstrap": args.bootstrap,
        "true_probs": true_probs.tolist(),
        "true_tau": true_tau.tolist(),
        "error_rates": error_rates.tolist(),
        "gpu_probe": gpu_probe,
        "summary": summary,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
