"""Run inference coverage ablations for EC-HTE.

Inputs:
    Synthetic DGP controls, expert-label budgets, replication count, and output
    path supplied via command line flags.

Outputs:
    A JSON file with empirical 95% coverage, mean CI width, coverage-width
    tradeoff, and subgroup CATE bias for naive, bootstrap, and
    sandwich-adjusted confidence intervals.

Key dependencies:
    numpy for simulation. torch is optional and used only to verify CUDA
    visibility for submitted GPU jobs.
"""

from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import numpy as np


INTERVAL_METHODS = ("naive", "bootstrap", "sandwich_adjusted")


def transition_matrix(error_rates: np.ndarray) -> np.ndarray:
    """Build P(observed subgroup | true subgroup) from row-specific error rates."""

    k = len(error_rates)
    matrix = np.zeros((k, k), dtype=float)
    for group, error in enumerate(error_rates):
        error = float(np.clip(error, 1e-4, 0.60))
        matrix[group, :] = error / (k - 1)
        matrix[group, group] = 1.0 - error
    return matrix


def simulate_observed_groups(
    rng: np.random.Generator,
    true_groups: np.ndarray,
    error_rates: np.ndarray,
) -> np.ndarray:
    """Sample noisy observed subgroup labels using row-specific symmetric errors."""

    k = len(error_rates)
    observed = true_groups.copy()
    for group, error in enumerate(error_rates):
        idx = np.flatnonzero(true_groups == group)
        flips = rng.random(len(idx)) < error
        if flips.any():
            offsets = rng.integers(1, k, size=int(flips.sum()))
            observed[idx[flips]] = (group + offsets) % k
    return observed


def simulate_dataset(
    rng: np.random.Generator,
    n: int,
    true_probs: np.ndarray,
    true_tau: np.ndarray,
    error_rates: np.ndarray,
    outcome_sd: float,
) -> Dict[str, np.ndarray]:
    """Generate one synthetic HTE dataset with noisy observed subgroup labels."""

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


def difference_in_means_with_se(
    y: np.ndarray,
    treatment: np.ndarray,
    groups: np.ndarray,
    k: int,
) -> Tuple[np.ndarray, np.ndarray]:
    """Estimate observed-group treatment effects and their plug-in standard errors."""

    estimates = np.zeros(k, dtype=float)
    variances = np.zeros(k, dtype=float)
    for group in range(k):
        treated = (groups == group) & (treatment == 1)
        control = (groups == group) & (treatment == 0)
        y_treated = y[treated]
        y_control = y[control]
        if len(y_treated) < 2 or len(y_control) < 2:
            estimates[group] = np.nan
            variances[group] = np.inf
            continue
        estimates[group] = y_treated.mean() - y_control.mean()
        variances[group] = y_treated.var(ddof=1) / len(y_treated) + y_control.var(ddof=1) / len(y_control)
    return estimates, variances


def estimate_partial_pooling_errors(
    true_expert: np.ndarray,
    observed_expert: np.ndarray,
    k: int,
    shrinkage_strength: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Estimate partial-pooling row errors and return components for uncertainty."""

    row_n = np.bincount(true_expert, minlength=k).astype(float)
    row_errors = np.zeros(k, dtype=float)
    for group in range(k):
        mask = true_expert == group
        row_errors[group] = float(np.sum(observed_expert[mask] != group))

    total_errors = float(np.sum(true_expert != observed_expert))
    global_error = (total_errors + 0.5) / (len(true_expert) + 1.0)
    independent = (row_errors + 0.5) / (row_n + 1.0)
    weights = row_n / (row_n + shrinkage_strength)
    pooled = weights * independent + (1.0 - weights) * global_error
    return np.clip(pooled, 1e-4, 0.60), row_n, independent, global_error


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


def correction_linear_map(
    observed_probs: np.ndarray,
    true_probs: np.ndarray,
    correction_matrix: np.ndarray,
) -> np.ndarray:
    """Return the linear map from observed subgroup CATE to corrected CATE."""

    try:
        inverse_t = np.linalg.inv(correction_matrix.T)
    except np.linalg.LinAlgError:
        inverse_t = np.linalg.pinv(correction_matrix.T)
    return np.diag(1.0 / true_probs) @ inverse_t @ np.diag(observed_probs)


def naive_standard_errors(
    observed_var: np.ndarray,
    observed_probs: np.ndarray,
    true_probs: np.ndarray,
    correction_matrix: np.ndarray,
) -> np.ndarray:
    """Delta-method SE that treats the estimated confusion matrix as fixed."""

    linear = correction_linear_map(observed_probs, true_probs, correction_matrix)
    covariance = linear @ np.diag(observed_var) @ linear.T
    return np.sqrt(np.maximum(np.diag(covariance), 0.0))


def sandwich_standard_errors(
    tau_hat: np.ndarray,
    observed_tau: np.ndarray,
    observed_probs: np.ndarray,
    true_probs: np.ndarray,
    error_rates: np.ndarray,
    row_n: np.ndarray,
    independent_errors: np.ndarray,
    global_error: float,
    shrinkage_strength: float,
    naive_se: np.ndarray,
) -> np.ndarray:
    """Add a finite-expert-label uncertainty term for confusion estimation."""

    k = len(error_rates)
    gradients = np.zeros((k, k), dtype=float)
    step = 1e-4
    for group in range(k):
        up = error_rates.copy()
        down = error_rates.copy()
        up[group] = min(0.60, up[group] + step)
        down[group] = max(1e-4, down[group] - step)
        tau_up = corrected_tau(observed_tau, observed_probs, true_probs, transition_matrix(up))
        tau_down = corrected_tau(observed_tau, observed_probs, true_probs, transition_matrix(down))
        gradients[:, group] = (tau_up - tau_down) / (up[group] - down[group])

    weights = row_n / (row_n + shrinkage_strength)
    row_var = independent_errors * (1.0 - independent_errors) / np.maximum(row_n + 1.0, 1.0)
    global_var = global_error * (1.0 - global_error) / max(float(row_n.sum()) + 1.0, 1.0)
    # Partial-pooling errors combine row-level and global estimates. The shared
    # global component induces covariance across rows, which this sandwich term
    # keeps instead of collapsing to an independent diagonal approximation.
    error_cov = np.diag(np.square(weights) * row_var)
    error_cov += np.outer(1.0 - weights, 1.0 - weights) * global_var
    confusion_cov = gradients @ error_cov @ gradients.T
    total_var = np.square(naive_se) + np.maximum(np.diag(confusion_cov), 0.0)
    return np.sqrt(np.maximum(total_var, 0.0))


def bootstrap_standard_errors(
    rng: np.random.Generator,
    data: Dict[str, np.ndarray],
    expert_idx: np.ndarray,
    true_probs: np.ndarray,
    shrinkage_strength: float,
    n_bootstrap: int,
) -> np.ndarray:
    """Estimate SE by resampling outcome rows and expert labels."""

    n = len(data["y"])
    k = len(true_probs)
    estimates = np.zeros((n_bootstrap, k), dtype=float)
    for draw in range(n_bootstrap):
        row_idx = rng.integers(0, n, size=n)
        expert_draw = rng.choice(expert_idx, size=len(expert_idx), replace=True)
        obs_tau, _ = difference_in_means_with_se(
            data["y"][row_idx],
            data["treatment"][row_idx],
            data["observed_groups"][row_idx],
            k,
        )
        obs_probs = np.bincount(data["observed_groups"][row_idx], minlength=k) / len(row_idx)
        errors, _, _, _ = estimate_partial_pooling_errors(
            true_expert=data["true_groups"][expert_draw],
            observed_expert=data["observed_groups"][expert_draw],
            k=k,
            shrinkage_strength=shrinkage_strength,
        )
        estimates[draw] = corrected_tau(obs_tau, obs_probs, true_probs, transition_matrix(errors))
    return estimates.std(axis=0, ddof=1)


def interval_stats(tau_hat: np.ndarray, se: np.ndarray, true_tau: np.ndarray) -> Dict[str, object]:
    """Compute coverage, width, and bias summaries for one CI method."""

    lower = tau_hat - 1.96 * se
    upper = tau_hat + 1.96 * se
    covered = (lower <= true_tau) & (true_tau <= upper)
    width = upper - lower
    bias = tau_hat - true_tau
    mean_width = float(np.mean(width))
    empirical_coverage = float(np.mean(covered))
    coverage_gap = abs(empirical_coverage - 0.95)
    return {
        "empirical_95_coverage": empirical_coverage,
        "mean_ci_width": mean_width,
        "coverage_width_tradeoff": float(coverage_gap / mean_width) if mean_width > 0 else math.inf,
        "mean_subgroup_cate_bias": float(np.mean(bias)),
        "mean_abs_subgroup_cate_bias": float(np.mean(np.abs(bias))),
        "max_abs_subgroup_cate_bias": float(np.max(np.abs(bias))),
        "subgroup_cate_bias": bias.tolist(),
        "subgroup_covered": covered.astype(float).tolist(),
        "subgroup_ci_width": width.tolist(),
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
    n_bootstrap: int,
) -> Dict[int, Dict[str, Dict[str, object]]]:
    """Run all budget/method CI ablations for one synthetic replication."""

    k = len(true_probs)
    data = simulate_dataset(rng, n, true_probs, true_tau, error_rates, outcome_sd)
    observed_tau, observed_var = difference_in_means_with_se(
        data["y"], data["treatment"], data["observed_groups"], k
    )
    observed_probs = np.bincount(data["observed_groups"], minlength=k) / n

    results: Dict[int, Dict[str, Dict[str, object]]] = {}
    for budget in budgets:
        if budget > n:
            raise ValueError(f"Budget B={budget} exceeds n={n}")

        expert_idx = rng.choice(n, size=budget, replace=False)
        errors, row_n, independent_errors, global_error = estimate_partial_pooling_errors(
            true_expert=data["true_groups"][expert_idx],
            observed_expert=data["observed_groups"][expert_idx],
            k=k,
            shrinkage_strength=shrinkage_strength,
        )
        correction = transition_matrix(errors)
        tau_hat = corrected_tau(observed_tau, observed_probs, true_probs, correction)
        naive_se = naive_standard_errors(observed_var, observed_probs, true_probs, correction)
        sandwich_se = sandwich_standard_errors(
            tau_hat=tau_hat,
            observed_tau=observed_tau,
            observed_probs=observed_probs,
            true_probs=true_probs,
            error_rates=errors,
            row_n=row_n,
            independent_errors=independent_errors,
            global_error=global_error,
            shrinkage_strength=shrinkage_strength,
            naive_se=naive_se,
        )
        bootstrap_se = bootstrap_standard_errors(
            rng=rng,
            data=data,
            expert_idx=expert_idx,
            true_probs=true_probs,
            shrinkage_strength=shrinkage_strength,
            n_bootstrap=n_bootstrap,
        )
        results[budget] = {
            "naive": interval_stats(tau_hat, naive_se, true_tau),
            "bootstrap": interval_stats(tau_hat, bootstrap_se, true_tau),
            "sandwich_adjusted": interval_stats(tau_hat, sandwich_se, true_tau),
        }

    return results


def summarize_scalar(values: List[float]) -> Dict[str, float]:
    """Summarize scalar metric values across replications."""

    arr = np.asarray(values, dtype=float)
    return {
        "mean": float(arr.mean()),
        "sd": float(arr.std(ddof=1)) if len(arr) > 1 else 0.0,
        "p10": float(np.quantile(arr, 0.10)),
        "p50": float(np.quantile(arr, 0.50)),
        "p90": float(np.quantile(arr, 0.90)),
    }


def summarize_vector(values: List[List[float]]) -> Dict[str, object]:
    """Summarize subgroup-level vector metrics across replications."""

    arr = np.asarray(values, dtype=float)
    return {
        "mean": arr.mean(axis=0).tolist(),
        "sd": arr.std(axis=0, ddof=1).tolist() if len(arr) > 1 else np.zeros(arr.shape[1]).tolist(),
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
            x = torch.randn((256, 256), device="cuda")
            torch.cuda.synchronize()
            info["gpu_name"] = torch.cuda.get_device_name(0)
            info["gpu_probe_sum"] = float(torch.sum(x * x).detach().cpu().item())
    except Exception as exc:  # pragma: no cover - environment diagnostic only.
        info["gpu_probe_error"] = repr(exc)
    return info


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=5000)
    parser.add_argument("--reps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=20260531)
    parser.add_argument("--budgets", type=int, nargs="+", default=[100, 500, 1000, 2000])
    parser.add_argument("--shrinkage-strength", type=float, default=80.0)
    parser.add_argument("--bootstrap-draws", type=int, default=60)
    parser.add_argument("--out", type=Path, default=Path("docs/results/e003_inference_coverage_ablation.json"))
    return parser.parse_args()


def main() -> None:
    """Run the inference coverage ablation and write JSON output."""

    args = parse_args()
    rng = np.random.default_rng(args.seed)

    true_probs = np.array([0.30, 0.22, 0.18, 0.13, 0.10, 0.07], dtype=float)
    true_tau = np.array([0.05, 0.12, 0.20, 0.32, 0.45, 0.60], dtype=float)
    error_rates = np.array([0.04, 0.08, 0.12, 0.18, 0.26, 0.35], dtype=float)

    raw: Dict[int, Dict[str, Dict[str, List[object]]]] = {
        budget: {method: {} for method in INTERVAL_METHODS} for budget in args.budgets
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
            n_bootstrap=args.bootstrap_draws,
        )
        for budget in args.budgets:
            for method in INTERVAL_METHODS:
                for metric, value in rep[budget][method].items():
                    raw[budget][method].setdefault(metric, []).append(value)

    scalar_metrics = {
        "empirical_95_coverage",
        "mean_ci_width",
        "coverage_width_tradeoff",
        "mean_subgroup_cate_bias",
        "mean_abs_subgroup_cate_bias",
        "max_abs_subgroup_cate_bias",
    }
    vector_metrics = {"subgroup_cate_bias", "subgroup_covered", "subgroup_ci_width"}
    budget_curve: Dict[str, Dict[str, Dict[str, object]]] = {}
    for budget in args.budgets:
        budget_curve[str(budget)] = {}
        for method in INTERVAL_METHODS:
            budget_curve[str(budget)][method] = {}
            for metric, values in raw[budget][method].items():
                if metric in scalar_metrics:
                    budget_curve[str(budget)][method][metric] = summarize_scalar(values)  # type: ignore[arg-type]
                elif metric in vector_metrics:
                    budget_curve[str(budget)][method][metric] = summarize_vector(values)  # type: ignore[arg-type]

    result = {
        "exp_id": "e003_inference_coverage_ablation",
        "parent": "e002_budgeted_confusion_estimation",
        "hypothesis": (
            "Propagating Stage 1 confusion-estimation uncertainty via bootstrap or sandwich-style "
            "adjustment improves empirical 95% subgroup CATE coverage relative to naive intervals, "
            "while maintaining narrower intervals than a conservative full bootstrap at moderate "
            "and large expert-label budgets."
        ),
        "seed": args.seed,
        "n": args.n,
        "reps": args.reps,
        "budgets": args.budgets,
        "bootstrap_draws": args.bootstrap_draws,
        "true_probs": true_probs.tolist(),
        "true_tau": true_tau.tolist(),
        "error_rates": error_rates.tolist(),
        "interval_methods": list(INTERVAL_METHODS),
        "stage1_confusion_estimator": "partial_pooling",
        "gpu_probe": touch_gpu(),
        "budget_curve": budget_curve,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
