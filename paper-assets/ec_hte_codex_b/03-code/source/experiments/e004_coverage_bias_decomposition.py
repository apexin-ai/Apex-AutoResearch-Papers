"""Run coverage-bias decomposition diagnostics for EC-HTE.

Inputs:
    Synthetic DGP controls, expert-label budgets, replication count, and output
    path supplied via command line flags.

Outputs:
    A JSON file comparing estimated partial-pooling correction against oracle
    confusion correction, with and without explicit bootstrap bias correction.
    Metrics include subgroup coverage, CATE bias, CI width, miss distance, and
    oracle-vs-estimated confusion coverage gaps.

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


VARIANTS = (
    "estimated_partial_pooling_raw",
    "oracle_confusion_raw",
    "estimated_partial_pooling_bias_corrected",
    "oracle_confusion_bias_corrected",
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
    """Estimate observed-group treatment effects and plug-in variances."""

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
) -> np.ndarray:
    """Estimate partial-pooling row errors from expert labels."""

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
    """Delta-method SE that treats the correction matrix as fixed."""

    linear = correction_linear_map(observed_probs, true_probs, correction_matrix)
    covariance = linear @ np.diag(observed_var) @ linear.T
    return np.sqrt(np.maximum(np.diag(covariance), 0.0))


def estimate_tau_for_indices(
    y: np.ndarray,
    treatment: np.ndarray,
    observed_groups: np.ndarray,
    true_groups: np.ndarray,
    true_probs: np.ndarray,
    correction_matrix: np.ndarray,
    row_idx: np.ndarray,
) -> np.ndarray:
    """Compute corrected CATE for a resampled set of outcome rows."""

    k = len(true_probs)
    obs_tau, _ = difference_in_means_with_se(y[row_idx], treatment[row_idx], observed_groups[row_idx], k)
    obs_probs = np.bincount(observed_groups[row_idx], minlength=k) / len(row_idx)
    return corrected_tau(obs_tau, obs_probs, true_probs, correction_matrix)


def bootstrap_bias(
    rng: np.random.Generator,
    data: Dict[str, np.ndarray],
    expert_idx: np.ndarray,
    true_probs: np.ndarray,
    oracle_transition: np.ndarray,
    tau_hat: np.ndarray,
    shrinkage_strength: float,
    draws: int,
    use_oracle_confusion: bool,
) -> np.ndarray:
    """Estimate bootstrap bias for a corrected CATE estimator."""

    n = len(data["y"])
    k = len(true_probs)
    estimates = np.zeros((draws, k), dtype=float)
    for draw in range(draws):
        row_idx = rng.integers(0, n, size=n)
        if use_oracle_confusion:
            correction = oracle_transition
        else:
            expert_draw = rng.choice(expert_idx, size=len(expert_idx), replace=True)
            errors = estimate_partial_pooling_errors(
                data["true_groups"][expert_draw],
                data["observed_groups"][expert_draw],
                k,
                shrinkage_strength,
            )
            correction = transition_matrix(errors)
        estimates[draw] = estimate_tau_for_indices(
            data["y"],
            data["treatment"],
            data["observed_groups"],
            data["true_groups"],
            true_probs,
            correction,
            row_idx,
        )
    return estimates.mean(axis=0) - tau_hat


def interval_metrics(tau_center: np.ndarray, se: np.ndarray, true_tau: np.ndarray) -> Dict[str, object]:
    """Compute coverage, bias, width, and miss distance for one estimator."""

    lower = tau_center - 1.96 * se
    upper = tau_center + 1.96 * se
    covered = (lower <= true_tau) & (true_tau <= upper)
    miss_distance = np.maximum(lower - true_tau, true_tau - upper)
    miss_distance = np.where(covered, 0.0, miss_distance)
    width = upper - lower
    bias = tau_center - true_tau
    return {
        "empirical_95_coverage": float(np.mean(covered)),
        "mean_ci_width": float(np.mean(width)),
        "mean_abs_subgroup_cate_bias": float(np.mean(np.abs(bias))),
        "max_abs_subgroup_cate_bias": float(np.max(np.abs(bias))),
        "mean_miss_distance": float(np.mean(miss_distance)),
        "subgroup_empirical_95_coverage": covered.astype(float).tolist(),
        "subgroup_cate_bias": bias.tolist(),
        "subgroup_ci_width": width.tolist(),
        "miss_distance_by_subgroup": miss_distance.tolist(),
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
    bias_bootstrap_draws: int,
) -> Dict[int, Dict[str, Dict[str, object]]]:
    """Run all budget/variant combinations for one diagnostic replication."""

    k = len(true_probs)
    data = simulate_dataset(rng, n, true_probs, true_tau, error_rates, outcome_sd)
    observed_tau, observed_var = difference_in_means_with_se(
        data["y"], data["treatment"], data["observed_groups"], k
    )
    observed_probs = np.bincount(data["observed_groups"], minlength=k) / n
    oracle_transition = transition_matrix(error_rates)
    oracle_tau = corrected_tau(observed_tau, observed_probs, true_probs, oracle_transition)
    oracle_se = naive_standard_errors(observed_var, observed_probs, true_probs, oracle_transition)

    results: Dict[int, Dict[str, Dict[str, object]]] = {}
    for budget in budgets:
        if budget > n:
            raise ValueError(f"Budget B={budget} exceeds n={n}")
        expert_idx = rng.choice(n, size=budget, replace=False)
        estimated_errors = estimate_partial_pooling_errors(
            data["true_groups"][expert_idx],
            data["observed_groups"][expert_idx],
            k,
            shrinkage_strength,
        )
        estimated_transition = transition_matrix(estimated_errors)
        estimated_tau = corrected_tau(observed_tau, observed_probs, true_probs, estimated_transition)
        estimated_se = naive_standard_errors(observed_var, observed_probs, true_probs, estimated_transition)

        estimated_bias = bootstrap_bias(
            rng,
            data,
            expert_idx,
            true_probs,
            oracle_transition,
            estimated_tau,
            shrinkage_strength,
            bias_bootstrap_draws,
            use_oracle_confusion=False,
        )
        oracle_bias = bootstrap_bias(
            rng,
            data,
            expert_idx,
            true_probs,
            oracle_transition,
            oracle_tau,
            shrinkage_strength,
            bias_bootstrap_draws,
            use_oracle_confusion=True,
        )

        results[budget] = {
            "estimated_partial_pooling_raw": interval_metrics(estimated_tau, estimated_se, true_tau),
            "oracle_confusion_raw": interval_metrics(oracle_tau, oracle_se, true_tau),
            # Bias-corrected intervals intentionally reuse the raw delta-method
            # widths. This isolates point-estimate centering from pure variance
            # widening, matching the D004 diagnostic question.
            "estimated_partial_pooling_bias_corrected": interval_metrics(
                estimated_tau - estimated_bias, estimated_se, true_tau
            ),
            "oracle_confusion_bias_corrected": interval_metrics(oracle_tau - oracle_bias, oracle_se, true_tau),
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
    """Summarize subgroup vector metrics across replications."""

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
    parser.add_argument("--bias-bootstrap-draws", type=int, default=40)
    parser.add_argument("--out", type=Path, default=Path("docs/results/e004_coverage_bias_decomposition.json"))
    return parser.parse_args()


def main() -> None:
    """Run the coverage-bias decomposition diagnostic and write JSON output."""

    args = parse_args()
    rng = np.random.default_rng(args.seed)

    true_probs = np.array([0.30, 0.22, 0.18, 0.13, 0.10, 0.07], dtype=float)
    true_tau = np.array([0.05, 0.12, 0.20, 0.32, 0.45, 0.60], dtype=float)
    error_rates = np.array([0.04, 0.08, 0.12, 0.18, 0.26, 0.35], dtype=float)

    raw: Dict[int, Dict[str, Dict[str, List[object]]]] = {
        budget: {variant: {} for variant in VARIANTS} for budget in args.budgets
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
            bias_bootstrap_draws=args.bias_bootstrap_draws,
        )
        for budget in args.budgets:
            for variant in VARIANTS:
                for metric, value in rep[budget][variant].items():
                    raw[budget][variant].setdefault(metric, []).append(value)

    scalar_metrics = {
        "empirical_95_coverage",
        "mean_ci_width",
        "mean_abs_subgroup_cate_bias",
        "max_abs_subgroup_cate_bias",
        "mean_miss_distance",
    }
    vector_metrics = {
        "subgroup_empirical_95_coverage",
        "subgroup_cate_bias",
        "subgroup_ci_width",
        "miss_distance_by_subgroup",
    }
    budget_curve: Dict[str, Dict[str, Dict[str, object]]] = {}
    for budget in args.budgets:
        budget_curve[str(budget)] = {}
        for variant in VARIANTS:
            budget_curve[str(budget)][variant] = {}
            for metric, values in raw[budget][variant].items():
                if metric in scalar_metrics:
                    budget_curve[str(budget)][variant][metric] = summarize_scalar(values)  # type: ignore[arg-type]
                elif metric in vector_metrics:
                    budget_curve[str(budget)][variant][metric] = summarize_vector(values)  # type: ignore[arg-type]

        est_raw = budget_curve[str(budget)]["estimated_partial_pooling_raw"]
        oracle_raw = budget_curve[str(budget)]["oracle_confusion_raw"]
        est_bc = budget_curve[str(budget)]["estimated_partial_pooling_bias_corrected"]
        oracle_bc = budget_curve[str(budget)]["oracle_confusion_bias_corrected"]
        budget_curve[str(budget)]["diagnostic_gaps"] = {
            "oracle_minus_estimated_raw_coverage": float(
                oracle_raw["empirical_95_coverage"]["mean"] - est_raw["empirical_95_coverage"]["mean"]
            ),
            "oracle_minus_estimated_bias_corrected_coverage": float(
                oracle_bc["empirical_95_coverage"]["mean"] - est_bc["empirical_95_coverage"]["mean"]
            ),
            "estimated_bias_correction_minus_raw_coverage": float(
                est_bc["empirical_95_coverage"]["mean"] - est_raw["empirical_95_coverage"]["mean"]
            ),
            "oracle_bias_correction_minus_raw_coverage": float(
                oracle_bc["empirical_95_coverage"]["mean"] - oracle_raw["empirical_95_coverage"]["mean"]
            ),
            "group5_oracle_minus_estimated_raw_coverage": float(
                oracle_raw["subgroup_empirical_95_coverage"]["mean"][5]
                - est_raw["subgroup_empirical_95_coverage"]["mean"][5]
            ),
            "group5_estimated_bias_correction_minus_raw_coverage": float(
                est_bc["subgroup_empirical_95_coverage"]["mean"][5]
                - est_raw["subgroup_empirical_95_coverage"]["mean"][5]
            ),
        }

    result = {
        "exp_id": "e004_coverage_bias_decomposition",
        "parent": "e003_inference_coverage_ablation",
        "hypothesis": (
            "The e003 undercoverage is driven primarily by negative point-estimate bias in the high "
            "CATE/high annotation-error subgroup rather than missing variance alone; oracle confusion "
            "or explicit bias correction should improve group5 coverage more than variance-only "
            "interval widening."
        ),
        "seed": args.seed,
        "n": args.n,
        "reps": args.reps,
        "budgets": args.budgets,
        "bias_bootstrap_draws": args.bias_bootstrap_draws,
        "true_probs": true_probs.tolist(),
        "true_tau": true_tau.tolist(),
        "error_rates": error_rates.tolist(),
        "variants": list(VARIANTS),
        "gpu_probe": touch_gpu(),
        "budget_curve": budget_curve,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
