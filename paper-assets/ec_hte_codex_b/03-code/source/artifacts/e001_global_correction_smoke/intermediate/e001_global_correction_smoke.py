"""Run the first EC-HTE mechanism smoke test.

Inputs:
    Command line flags for sample size, replications, seed, and output path.

Outputs:
    A JSON file containing aggregate subgroup CATE bias metrics for three
    estimators: uncorrected, pooled/global correction, and oracle
    subgroup-specific correction.

Key dependency:
    numpy. The script intentionally avoids heavier causal-forest dependencies so
    the mechanism test can run on CPU before GPU/server allocation is ready.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, Tuple

import numpy as np


METHODS = ("uncorrected", "global_corrected", "subgroup_corrected")


def transition_matrix(error_rates: np.ndarray) -> np.ndarray:
    """Return P(observed subgroup | true subgroup) for symmetric off-diagonal error."""

    k = len(error_rates)
    matrix = np.zeros((k, k), dtype=float)
    for g, error in enumerate(error_rates):
        matrix[g, :] = error / (k - 1)
        matrix[g, g] = 1.0 - error
    return matrix


def difference_in_means(y: np.ndarray, treatment: np.ndarray, groups: np.ndarray, k: int) -> np.ndarray:
    """Estimate subgroup treatment effects by observed group difference in means."""

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
    """Recover true subgroup effects from observed subgroup effects using a correction matrix."""

    rhs = observed_probs * observed_tau
    try:
        weighted_tau = np.linalg.solve(correction_matrix.T, rhs)
    except np.linalg.LinAlgError:
        weighted_tau = np.linalg.pinv(correction_matrix.T) @ rhs
    return weighted_tau / true_probs


def simulate_once(
    rng: np.random.Generator,
    n: int,
    true_probs: np.ndarray,
    true_tau: np.ndarray,
    error_rates: np.ndarray,
    outcome_sd: float,
) -> Dict[str, np.ndarray]:
    """Generate one synthetic dataset and return CATE estimates from each method."""

    k = len(true_probs)
    true_groups = rng.choice(k, size=n, p=true_probs)
    true_transition = transition_matrix(error_rates)
    observed_groups = np.array(
        [rng.choice(k, p=true_transition[g]) for g in true_groups],
        dtype=int,
    )

    treatment = rng.binomial(1, 0.5, size=n)
    baseline = np.linspace(0.0, 0.2, k)
    y = baseline[true_groups] + true_tau[true_groups] * treatment + rng.normal(0.0, outcome_sd, size=n)

    observed_tau = difference_in_means(y, treatment, observed_groups, k)
    observed_probs = np.bincount(observed_groups, minlength=k) / n

    pooled_error = float(np.dot(true_probs, error_rates))
    global_transition = transition_matrix(np.full(k, pooled_error))

    return {
        "uncorrected": observed_tau,
        "global_corrected": corrected_tau(observed_tau, observed_probs, true_probs, global_transition),
        "subgroup_corrected": corrected_tau(observed_tau, observed_probs, true_probs, true_transition),
    }


def summarize(estimates: Dict[str, Iterable[np.ndarray]], true_tau: np.ndarray) -> Dict[str, Dict[str, float]]:
    """Aggregate RMSE and absolute-bias metrics across replications."""

    summary: Dict[str, Dict[str, float]] = {}
    method_rmse = {}
    for method, values in estimates.items():
        arr = np.vstack(list(values))
        bias = arr - true_tau
        per_rep_rmse = np.sqrt(np.mean(np.square(bias), axis=1))
        method_rmse[method] = per_rep_rmse
        summary[method] = {
            "cate_rmse_mean": float(per_rep_rmse.mean()),
            "cate_rmse_sd": float(per_rep_rmse.std(ddof=1)),
            "mean_abs_subgroup_bias": float(np.abs(bias).mean()),
            "max_abs_subgroup_bias_mean": float(np.abs(bias).max(axis=1).mean()),
        }

    summary["comparisons"] = {
        "global_minus_uncorrected_rmse": float(
            method_rmse["global_corrected"].mean() - method_rmse["uncorrected"].mean()
        ),
        "subgroup_minus_global_rmse": float(
            method_rmse["subgroup_corrected"].mean() - method_rmse["global_corrected"].mean()
        ),
        "global_worse_than_uncorrected_rate": float(
            np.mean(method_rmse["global_corrected"] > method_rmse["uncorrected"])
        ),
    }
    return summary


def run_config(
    rng: np.random.Generator,
    name: str,
    n: int,
    reps: int,
    true_probs: np.ndarray,
    true_tau: np.ndarray,
    error_rates: np.ndarray,
    outcome_sd: float,
) -> Dict[str, object]:
    """Run all replications for one DGP configuration."""

    estimates = {method: [] for method in METHODS}
    for _ in range(reps):
        rep_estimates = simulate_once(rng, n, true_probs, true_tau, error_rates, outcome_sd)
        for method in METHODS:
            estimates[method].append(rep_estimates[method])

    heterogeneity_product = float(np.std(error_rates, ddof=0) * np.std(true_tau, ddof=0))
    corr = float(np.corrcoef(error_rates, true_tau)[0, 1])
    return {
        "name": name,
        "n": n,
        "reps": reps,
        "true_probs": true_probs.tolist(),
        "true_tau": true_tau.tolist(),
        "error_rates": error_rates.tolist(),
        "misclassification_cate_corr": corr,
        "heterogeneity_product": heterogeneity_product,
        "metrics": summarize(estimates, true_tau),
    }


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=5000)
    parser.add_argument("--reps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=20260531)
    parser.add_argument("--out", type=Path, default=Path("docs/results/e001_global_correction_smoke.json"))
    return parser.parse_args()


def main() -> None:
    """Run the experiment and write a JSON result file."""

    args = parse_args()
    rng = np.random.default_rng(args.seed)

    true_probs = np.array([0.34, 0.33, 0.33], dtype=float)
    true_tau = np.array([0.08, 0.25, 0.55], dtype=float)

    configs = [
        ("positive_corr", np.array([0.05, 0.15, 0.30], dtype=float)),
        ("negative_corr", np.array([0.30, 0.15, 0.05], dtype=float)),
    ]

    result = {
        "exp_id": "e001_global_correction_smoke",
        "hypothesis": (
            "When subgroup misclassification rates are positively aligned with true CATE magnitude, "
            "a pooled global correction matrix can increase subgroup CATE RMSE relative to using noisy "
            "LLM subgroup labels directly, while subgroup-specific correction reduces that bias."
        ),
        "seed": args.seed,
        "configs": [
            run_config(rng, name, args.n, args.reps, true_probs, true_tau, error_rates, outcome_sd=1.0)
            for name, error_rates in configs
        ],
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
