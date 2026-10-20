"""Run capped and hybrid expert-allocation diagnostics for EC-HTE.

Inputs:
    Synthetic DGP controls, expert-label budgets, replication count, and output
    path supplied via command line flags.

Outputs:
    A JSON file comparing uniform allocation, uncapped CATE-error allocation,
    capped CATE-error allocation, and hybrid uniform/CATE-error allocation.
    Metrics include group5 coverage and bias, overall CATE RMSE, allocation
    counts, coverage gain per RMSE cost, and B=2000 target indicators.

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
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np


METHODS = (
    "uniform",
    "cate_error_product",
    "capped_cate_error_25pct",
    "capped_cate_error_35pct",
    "hybrid_50_50_uniform_cate_error",
    "hybrid_70_30_uniform_cate_error",
)


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
    return {"true_groups": true_groups, "observed_groups": observed_groups, "treatment": treatment, "y": y}


def difference_in_means_with_se(
    y: np.ndarray,
    treatment: np.ndarray,
    groups: np.ndarray,
    k: int,
) -> Tuple[np.ndarray, np.ndarray]:
    """Estimate observed-group CATE values and plug-in variances."""

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
    """Delta-method SE that treats the estimated correction matrix as fixed."""

    linear = correction_linear_map(observed_probs, true_probs, correction_matrix)
    covariance = linear @ np.diag(observed_var) @ linear.T
    return np.sqrt(np.maximum(np.diag(covariance), 0.0))


def allocate_counts(
    budget: int,
    group_sizes: np.ndarray,
    weights: np.ndarray,
    max_share: Optional[float] = None,
    min_per_group: int = 1,
) -> np.ndarray:
    """Convert weights to integer counts with an optional per-subgroup share cap.

    max_share is a single-subgroup expert-label allocation share cap: for
    example, 0.25 means no subgroup may receive more than 25% of the total
    expert-label budget, subject to available rows in that subgroup.
    """

    k = len(group_sizes)
    counts = np.zeros(k, dtype=int)
    available = group_sizes.astype(int).copy()
    cap_counts = np.full(k, budget, dtype=int)
    if max_share is not None:
        cap_counts = np.minimum(cap_counts, np.floor(max_share * budget).astype(int))
        cap_counts = np.maximum(cap_counts, min_per_group)
    cap_counts = np.minimum(cap_counts, available + counts)

    if budget >= k * min_per_group:
        for group in range(k):
            take = min(min_per_group, available[group], cap_counts[group])
            counts[group] += take
            available[group] -= take
    remaining = budget - int(counts.sum())

    positive = np.maximum(weights, 0.0)
    if positive.sum() <= 0:
        positive = np.ones(k, dtype=float)
    while remaining > 0 and np.any((available > 0) & (counts < cap_counts)):
        eligible = (available > 0) & (counts < cap_counts)
        eligible_weights = positive * eligible
        if eligible_weights.sum() <= 0:
            eligible_weights = eligible.astype(float)
        quotas = remaining * eligible_weights / eligible_weights.sum()
        add = np.floor(quotas).astype(int)
        add = np.minimum(add, available)
        add = np.minimum(add, cap_counts - counts)
        if add.sum() == 0:
            fractions = quotas - np.floor(quotas)
            for group in np.argsort(-fractions):
                if eligible[group]:
                    add[group] = 1
                    break
        counts += add
        available -= add
        remaining = budget - int(counts.sum())
    return counts


def estimate_partial_pooling_errors(
    true_expert: np.ndarray,
    observed_expert: np.ndarray,
    k: int,
    shrinkage_strength: float,
) -> np.ndarray:
    """Estimate partial-pooling row errors from allocated expert labels."""

    row_n = np.bincount(true_expert, minlength=k).astype(float)
    row_errors = np.zeros(k, dtype=float)
    for group in range(k):
        mask = true_expert == group
        row_errors[group] = float(np.sum(observed_expert[mask] != group))
    global_error = (float(np.sum(true_expert != observed_expert)) + 0.5) / (len(true_expert) + 1.0)
    independent = (row_errors + 0.5) / (row_n + 1.0)
    weights = row_n / (row_n + shrinkage_strength)
    pooled = weights * independent + (1.0 - weights) * global_error
    return np.clip(pooled, 1e-4, 0.60)


def sample_expert_indices(
    rng: np.random.Generator,
    true_groups: np.ndarray,
    counts: np.ndarray,
) -> np.ndarray:
    """Sample expert-label indices according to subgroup counts."""

    pieces = []
    for group, count in enumerate(counts):
        group_idx = np.flatnonzero(true_groups == group)
        if count > 0:
            pieces.append(rng.choice(group_idx, size=count, replace=False))
    expert_idx = np.concatenate(pieces) if pieces else np.array([], dtype=int)
    rng.shuffle(expert_idx)
    return expert_idx


def interval_metrics(tau_hat: np.ndarray, se: np.ndarray, true_tau: np.ndarray) -> Dict[str, object]:
    """Compute coverage, bias, width, and RMSE for corrected subgroup CATE."""

    lower = tau_hat - 1.96 * se
    upper = tau_hat + 1.96 * se
    covered = (lower <= true_tau) & (true_tau <= upper)
    width = upper - lower
    bias = tau_hat - true_tau
    return {
        "empirical_95_coverage": float(np.mean(covered)),
        "group5_empirical_95_coverage": float(covered[5]),
        "group5_cate_bias": float(bias[5]),
        "overall_cate_rmse": float(np.sqrt(np.mean(np.square(bias)))),
        "mean_abs_subgroup_cate_bias": float(np.mean(np.abs(bias))),
        "group5_ci_width": float(width[5]),
        "subgroup_empirical_95_coverage": covered.astype(float).tolist(),
        "subgroup_cate_bias": bias.tolist(),
        "subgroup_ci_width": width.tolist(),
    }


def method_weights(
    method: str,
    uniform_weights: np.ndarray,
    cate_error_weights: np.ndarray,
) -> Tuple[np.ndarray, Optional[float]]:
    """Return allocation weights and optional cap for one method."""

    if method == "uniform":
        return uniform_weights, None
    if method == "cate_error_product":
        return cate_error_weights, None
    if method == "capped_cate_error_25pct":
        return cate_error_weights, 0.25
    if method == "capped_cate_error_35pct":
        return cate_error_weights, 0.35
    if method == "hybrid_50_50_uniform_cate_error":
        return 0.50 * uniform_weights + 0.50 * cate_error_weights, None
    if method == "hybrid_70_30_uniform_cate_error":
        return 0.70 * uniform_weights + 0.30 * cate_error_weights, None
    raise ValueError(f"Unknown method: {method}")


def run_replication(
    rng: np.random.Generator,
    n: int,
    budgets: Iterable[int],
    true_probs: np.ndarray,
    true_tau: np.ndarray,
    error_rates: np.ndarray,
    shrinkage_strength: float,
    outcome_sd: float,
) -> Dict[int, Dict[str, Dict[str, object]]]:
    """Run all budget/allocation combinations for one synthetic replication."""

    k = len(true_probs)
    data = simulate_dataset(rng, n, true_probs, true_tau, error_rates, outcome_sd)
    observed_tau, observed_var = difference_in_means_with_se(data["y"], data["treatment"], data["observed_groups"], k)
    observed_probs = np.bincount(data["observed_groups"], minlength=k) / n
    group_sizes = np.bincount(data["true_groups"], minlength=k)

    pilot_budget = min(max(60, k * 8), n)
    pilot_idx = rng.choice(n, size=pilot_budget, replace=False)
    pilot_errors = estimate_partial_pooling_errors(
        data["true_groups"][pilot_idx],
        data["observed_groups"][pilot_idx],
        k,
        shrinkage_strength,
    )
    uniform_weights = true_probs / true_probs.sum()
    cate_error_weights = true_probs * np.clip(pilot_errors, 1e-4, None) * np.maximum(np.abs(observed_tau), 1e-4)
    cate_error_weights = cate_error_weights / cate_error_weights.sum()

    results: Dict[int, Dict[str, Dict[str, object]]] = {}
    for budget in budgets:
        results[budget] = {}
        for method in METHODS:
            weights, cap = method_weights(method, uniform_weights, cate_error_weights)
            counts = allocate_counts(budget, group_sizes, weights, max_share=cap, min_per_group=1)
            expert_idx = sample_expert_indices(rng, data["true_groups"], counts)
            estimated_errors = estimate_partial_pooling_errors(
                data["true_groups"][expert_idx],
                data["observed_groups"][expert_idx],
                k,
                shrinkage_strength,
            )
            correction = transition_matrix(estimated_errors)
            tau_hat = corrected_tau(observed_tau, observed_probs, true_probs, correction)
            se = naive_standard_errors(observed_var, observed_probs, true_probs, correction)
            metrics = interval_metrics(tau_hat, se, true_tau)
            metrics["allocation_counts_by_subgroup"] = counts.astype(float).tolist()
            metrics["allocation_share_by_subgroup"] = (counts / max(float(counts.sum()), 1.0)).tolist()
            results[budget][method] = metrics
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
    """Summarize subgroup vector metrics across replications."""

    arr = np.asarray(values, dtype=float)
    return {
        "mean": arr.mean(axis=0).tolist(),
        "sd": arr.std(axis=0, ddof=1).tolist() if len(arr) > 1 else np.zeros(arr.shape[1]).tolist(),
    }


def touch_gpu() -> Dict[str, object]:
    """Return CUDA visibility information and briefly exercise the GPU if torch exists."""

    info: Dict[str, object] = {"cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES", ""), "torch_available": False, "cuda_available": False}
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
    parser.add_argument("--out", type=Path, default=Path("docs/results/e006_capped_hybrid_allocation.json"))
    return parser.parse_args()


def main() -> None:
    """Run the capped/hybrid allocation experiment and write JSON output."""

    args = parse_args()
    rng = np.random.default_rng(args.seed)
    true_probs = np.array([0.30, 0.22, 0.18, 0.13, 0.10, 0.07], dtype=float)
    true_tau = np.array([0.05, 0.12, 0.20, 0.32, 0.45, 0.60], dtype=float)
    error_rates = np.array([0.04, 0.08, 0.12, 0.18, 0.26, 0.35], dtype=float)

    raw: Dict[int, Dict[str, Dict[str, List[object]]]] = {
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

    scalar_metrics = {
        "empirical_95_coverage",
        "group5_empirical_95_coverage",
        "group5_cate_bias",
        "overall_cate_rmse",
        "mean_abs_subgroup_cate_bias",
        "group5_ci_width",
    }
    vector_metrics = {
        "subgroup_empirical_95_coverage",
        "subgroup_cate_bias",
        "subgroup_ci_width",
        "allocation_counts_by_subgroup",
        "allocation_share_by_subgroup",
    }

    e005_rmse_cost = {100: 0.004509780302770841, 500: 0.0015425285997547195, 1000: 0.0021752546377083737, 2000: 0.0024976760819066385}
    budget_curve: Dict[str, Dict[str, Dict[str, object]]] = {}
    for budget in args.budgets:
        budget_curve[str(budget)] = {}
        for method in METHODS:
            budget_curve[str(budget)][method] = {}
            for metric, values in raw[budget][method].items():
                if metric in scalar_metrics:
                    budget_curve[str(budget)][method][metric] = summarize_scalar(values)  # type: ignore[arg-type]
                elif metric in vector_metrics:
                    budget_curve[str(budget)][method][metric] = summarize_vector(values)  # type: ignore[arg-type]

        uniform = budget_curve[str(budget)]["uniform"]
        cate_error = budget_curve[str(budget)]["cate_error_product"]
        budget_curve[str(budget)]["strategy_deltas_vs_uniform"] = {}
        e005_cost_for_budget = e005_rmse_cost.get(int(budget))
        for method in METHODS:
            if method == "uniform":
                continue
            current = budget_curve[str(budget)][method]
            coverage_gain = float(current["group5_empirical_95_coverage"]["mean"] - uniform["group5_empirical_95_coverage"]["mean"])
            rmse_cost = float(current["overall_cate_rmse"]["mean"] - uniform["overall_cate_rmse"]["mean"])
            budget_curve[str(budget)]["strategy_deltas_vs_uniform"][method] = {
                "group5_coverage_delta": coverage_gain,
                "group5_bias_delta": float(current["group5_cate_bias"]["mean"] - uniform["group5_cate_bias"]["mean"]),
                "overall_cate_rmse_delta": rmse_cost,
                "coverage_gain_per_rmse_cost": float(coverage_gain / rmse_cost) if rmse_cost > 0 else math.inf,
                "rmse_delta_vs_e005_cate_error_product": (
                    None if e005_cost_for_budget is None else float(rmse_cost - e005_cost_for_budget)
                ),
            }
        b2000 = int(budget) == 2000
        budget_curve[str(budget)]["target_checks"] = {}
        for method in METHODS:
            if method == "uniform":
                continue
            current = budget_curve[str(budget)][method]
            rmse_cost = float(current["overall_cate_rmse"]["mean"] - uniform["overall_cate_rmse"]["mean"])
            coverage = float(current["group5_empirical_95_coverage"]["mean"])
            budget_curve[str(budget)]["target_checks"][method] = {
                "b2000_group5_coverage_ge_095_and_rmse_cost_below_e005": bool(
                    b2000 and coverage >= 0.95 and rmse_cost < e005_rmse_cost[2000]
                )
            }

    result = {
        "exp_id": "e006_capped_hybrid_allocation",
        "parent": "e005_targeted_expert_allocation",
        "hypothesis": (
            "A capped or hybrid uniform+cate-error allocation can retain most group5 coverage/bias "
            "improvement from cate_error_product while reducing the overall CATE RMSE penalty relative "
            "to uncapped targeted allocation."
        ),
        "seed": args.seed,
        "n": args.n,
        "reps": args.reps,
        "budgets": args.budgets,
        "true_probs": true_probs.tolist(),
        "true_tau": true_tau.tolist(),
        "error_rates": error_rates.tolist(),
        "methods": list(METHODS),
        "cap_definition": "Single subgroup expert-label allocation share cap: capped_cate_error_25pct/35pct limit each subgroup to at most 25%/35% of total B.",
        "stage1_estimator": "partial_pooling",
        "gpu_probe": touch_gpu(),
        "budget_curve": budget_curve,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
