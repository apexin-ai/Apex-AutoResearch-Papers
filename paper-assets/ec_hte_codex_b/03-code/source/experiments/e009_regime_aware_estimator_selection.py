"""Evaluate regime-aware Stage 1 confusion-estimator selection for EC-HTE.

Inputs:
    Synthetic DGP grid controls, expert-label budgets, replication count, and an
    output path supplied by command line flags.

Outputs:
    A JSON file with per-grid-cell CATE RMSE and selector diagnostics for fixed
    global, independent, partial-pooling, an oracle selector, and deployable
    pilot-proxy selectors.

Key dependencies:
    numpy for simulation. The e002 module supplies the original Stage 1 data
    generation and confusion-correction helpers so this experiment preserves the
    core estimator semantics used by e002/e008.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import numpy as np


BASE_METHODS = ("global", "independent", "partial_pooling")
METHODS = (
    "global",
    "independent",
    "partial_pooling",
    "oracle_regime_selector",
    "pilot_corr_selector",
    "pilot_corr_severity_selector",
)
SUBGROUP_COUNTS = (4, 6, 8)
SEVERITIES = ("low", "medium", "high")
CORRELATIONS = ("positive", "zero", "negative")


def load_e002_module() -> Any:
    """Load e002 functions to preserve Stage 1 estimator semantics."""

    module_path = Path(__file__).with_name("e002_budgeted_confusion_estimation.py")
    spec = importlib.util.spec_from_file_location("e002_budgeted_confusion_estimation", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load e002 module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dgp_parameters(k: int, severity: str, correlation: str) -> Dict[str, np.ndarray]:
    """Create the same heterogeneous DGP family as e008."""

    raw_probs = np.exp(-0.24 * np.arange(k, dtype=float))
    true_probs = raw_probs / raw_probs.sum()
    true_tau = np.linspace(0.08, 0.62, k, dtype=float)

    severity_ranges = {
        "low": (0.03, 0.12),
        "medium": (0.06, 0.30),
        "high": (0.12, 0.50),
    }
    lo, hi = severity_ranges[severity]
    increasing = np.linspace(lo, hi, k, dtype=float)
    if correlation == "positive":
        error_rates = increasing
    elif correlation == "negative":
        error_rates = increasing[::-1]
    elif correlation == "zero":
        order = np.ravel([np.arange(0, k, 2), np.arange(1, k, 2)])
        error_rates = np.empty(k, dtype=float)
        error_rates[order] = increasing
    else:
        raise ValueError(f"Unknown correlation regime: {correlation}")

    return {"true_probs": true_probs, "true_tau": true_tau, "error_rates": error_rates}


def summarize(values: Iterable[float]) -> Dict[str, float]:
    """Summarize scalar replication metrics."""

    arr = np.asarray(list(values), dtype=float)
    return {
        "mean": float(arr.mean()),
        "sd": float(arr.std(ddof=1)) if len(arr) > 1 else 0.0,
        "p10": float(np.quantile(arr, 0.10)),
        "p50": float(np.quantile(arr, 0.50)),
        "p90": float(np.quantile(arr, 0.90)),
    }


def safe_corr(x: np.ndarray, y: np.ndarray) -> float:
    """Return Pearson correlation, falling back to zero for degenerate inputs."""

    if len(x) < 2 or float(np.std(x)) < 1e-12 or float(np.std(y)) < 1e-12:
        return 0.0
    corr = float(np.corrcoef(x, y)[0, 1])
    if not np.isfinite(corr):
        return 0.0
    return corr


def selector_decision(
    selector: str,
    proxy_corr: float,
    severity_proxy: float,
    corr_threshold: float,
    strong_negative_threshold: float,
    high_severity_threshold: float,
) -> str:
    """Choose a base estimator using only finite expert-label proxy statistics.

    The deployable proxy estimates row-wise error rates from expert-labeled
    samples and compares them with absolute preliminary subgroup CATE estimates
    from observed noisy labels. If the proxy correlation is clearly negative,
    the rule chooses independent estimation; otherwise it chooses partial
    pooling. The severity-aware variant is more conservative: it only switches
    to independent for strongly negative proxy correlation, or for moderately
    negative correlation when estimated error severity is not high. High
    severity with nonnegative proxy correlation is explicitly kept on
    partial-pooling to preserve the high-severity positive-regime gain observed
    in e008.
    """

    if selector == "pilot_corr_selector":
        return "independent" if proxy_corr < corr_threshold else "partial_pooling"

    if selector == "pilot_corr_severity_selector":
        if proxy_corr < strong_negative_threshold:
            return "independent"
        if proxy_corr < corr_threshold and severity_proxy < high_severity_threshold:
            return "independent"
        return "partial_pooling"

    raise ValueError(selector)


def metric_from_tau(
    tau_hat: np.ndarray,
    true_tau: np.ndarray,
    estimated_transition: np.ndarray,
    true_transition: np.ndarray,
    confusion_rmse_fn: Any,
) -> Dict[str, float]:
    """Compute downstream CATE and confusion-recovery metrics."""

    bias = tau_hat - true_tau
    return {
        "cate_rmse": float(np.sqrt(np.mean(np.square(bias)))),
        "mean_abs_subgroup_bias": float(np.mean(np.abs(bias))),
        "max_abs_subgroup_bias": float(np.max(np.abs(bias))),
        "confusion_recovery_rmse": confusion_rmse_fn(estimated_transition, true_transition),
    }


def run_replication(
    e002: Any,
    rng: np.random.Generator,
    n: int,
    budget: int,
    true_probs: np.ndarray,
    true_tau: np.ndarray,
    error_rates: np.ndarray,
    shrinkage_strength: float,
    corr_threshold: float,
    strong_negative_threshold: float,
    high_severity_threshold: float,
) -> Dict[str, Dict[str, float]]:
    """Run one replication for fixed estimators and regime-aware selectors."""

    k = len(true_probs)
    data = e002.simulate_dataset(
        rng=rng,
        n=n,
        true_probs=true_probs,
        true_tau=true_tau,
        error_rates=error_rates,
        outcome_sd=1.0,
    )
    observed_tau = e002.difference_in_means(data["y"], data["treatment"], data["observed_groups"], k)
    observed_probs = np.bincount(data["observed_groups"], minlength=k) / n
    true_transition = e002.transition_matrix(error_rates)

    if budget > n:
        raise ValueError(f"Budget B={budget} exceeds n={n}")
    expert_idx = rng.choice(n, size=budget, replace=False)
    true_expert = data["true_groups"][expert_idx]
    observed_expert = data["observed_groups"][expert_idx]

    base_metrics: Dict[str, Dict[str, float]] = {}
    base_tau: Dict[str, np.ndarray] = {}
    base_transition: Dict[str, np.ndarray] = {}
    for method in BASE_METHODS:
        estimated_errors = e002.estimate_error_rates(
            true_expert=true_expert,
            observed_expert=observed_expert,
            k=k,
            method=method,
            shrinkage_strength=shrinkage_strength,
        )
        estimated_transition = e002.transition_matrix(estimated_errors)
        tau_hat = e002.corrected_tau(observed_tau, observed_probs, true_probs, estimated_transition)
        base_tau[method] = tau_hat
        base_transition[method] = estimated_transition
        base_metrics[method] = metric_from_tau(
            tau_hat=tau_hat,
            true_tau=true_tau,
            estimated_transition=estimated_transition,
            true_transition=true_transition,
            confusion_rmse_fn=e002.confusion_recovery_rmse,
        )

    independent_error_proxy = e002.estimate_error_rates(
        true_expert=true_expert,
        observed_expert=observed_expert,
        k=k,
        method="independent",
        shrinkage_strength=shrinkage_strength,
    )
    proxy_corr = safe_corr(independent_error_proxy, np.abs(observed_tau))
    severity_proxy = float(np.max(independent_error_proxy))

    oracle_choice = "partial_pooling"
    if base_metrics["independent"]["cate_rmse"] < base_metrics["partial_pooling"]["cate_rmse"]:
        oracle_choice = "independent"

    results = dict(base_metrics)
    results["oracle_regime_selector"] = dict(base_metrics[oracle_choice])
    results["oracle_regime_selector"].update({
        "selected_independent": float(oracle_choice == "independent"),
        "selected_partial_pooling": float(oracle_choice == "partial_pooling"),
        "proxy_corr": proxy_corr,
        "severity_proxy": severity_proxy,
    })

    for selector in ("pilot_corr_selector", "pilot_corr_severity_selector"):
        choice = selector_decision(
            selector=selector,
            proxy_corr=proxy_corr,
            severity_proxy=severity_proxy,
            corr_threshold=corr_threshold,
            strong_negative_threshold=strong_negative_threshold,
            high_severity_threshold=high_severity_threshold,
        )
        results[selector] = dict(base_metrics[choice])
        results[selector].update({
            "selected_independent": float(choice == "independent"),
            "selected_partial_pooling": float(choice == "partial_pooling"),
            "proxy_corr": proxy_corr,
            "severity_proxy": severity_proxy,
            "oracle_choice_match": float(choice == oracle_choice),
        })

    fixed_best = min(
        base_metrics["partial_pooling"]["cate_rmse"],
        base_metrics["independent"]["cate_rmse"],
    )
    for method in METHODS:
        results[method]["regret_vs_oracle_best_pi"] = float(results[method]["cate_rmse"] - fixed_best)
        results[method]["delta_vs_fixed_partial"] = float(
            results[method]["cate_rmse"] - base_metrics["partial_pooling"]["cate_rmse"]
        )
        results[method]["delta_vs_fixed_independent"] = float(
            results[method]["cate_rmse"] - base_metrics["independent"]["cate_rmse"]
        )
    return results


def run_cell(
    e002: Any,
    rng: np.random.Generator,
    n: int,
    reps: int,
    budgets: List[int],
    k: int,
    severity: str,
    correlation: str,
    shrinkage_strength: float,
    corr_threshold: float,
    strong_negative_threshold: float,
    high_severity_threshold: float,
) -> Dict[str, Any]:
    """Run one DGP grid cell across budgets and selector methods."""

    params = dgp_parameters(k, severity, correlation)
    raw: Dict[int, Dict[str, Dict[str, List[float]]]] = {
        budget: {method: defaultdict(list) for method in METHODS} for budget in budgets
    }
    for _ in range(reps):
        for budget in budgets:
            rep = run_replication(
                e002=e002,
                rng=rng,
                n=n,
                budget=budget,
                true_probs=params["true_probs"],
                true_tau=params["true_tau"],
                error_rates=params["error_rates"],
                shrinkage_strength=shrinkage_strength,
                corr_threshold=corr_threshold,
                strong_negative_threshold=strong_negative_threshold,
                high_severity_threshold=high_severity_threshold,
            )
            for method in METHODS:
                for metric, value in rep[method].items():
                    raw[budget][method][metric].append(float(value))

    cell: Dict[str, Any] = {
        "subgroup_count": k,
        "misclassification_severity": severity,
        "cate_error_correlation": correlation,
        "true_probs": params["true_probs"].tolist(),
        "true_tau": params["true_tau"].tolist(),
        "error_rates": params["error_rates"].tolist(),
        "budgets": {},
    }
    for budget in budgets:
        budget_key = str(budget)
        cell["budgets"][budget_key] = {}
        for method in METHODS:
            cell["budgets"][budget_key][method] = {
                metric: summarize(values) for metric, values in raw[budget][method].items()
            }

        method_rmse = {
            method: cell["budgets"][budget_key][method]["cate_rmse"]["mean"]
            for method in METHODS
        }
        fixed_best = min(method_rmse["partial_pooling"], method_rmse["independent"])
        all_winner = min(method_rmse, key=method_rmse.get)
        fixed_winner = "partial_pooling"
        if method_rmse["independent"] < method_rmse["partial_pooling"]:
            fixed_winner = "independent"

        cell["budgets"][budget_key]["summary"] = {
            "winner_by_cate_rmse": all_winner,
            "fixed_best_winner": fixed_winner,
            "fixed_best_cate_rmse": fixed_best,
            "pilot_corr_selector_ties_or_beats_fixed_best": bool(
                method_rmse["pilot_corr_selector"] <= fixed_best + 1e-12
            ),
            "pilot_corr_severity_selector_ties_or_beats_fixed_best": bool(
                method_rmse["pilot_corr_severity_selector"] <= fixed_best + 1e-12
            ),
            "oracle_regime_selector_ties_or_beats_fixed_best": bool(
                method_rmse["oracle_regime_selector"] <= fixed_best + 1e-12
            ),
            "pilot_corr_selector_delta_vs_partial": float(
                method_rmse["pilot_corr_selector"] - method_rmse["partial_pooling"]
            ),
            "pilot_corr_selector_delta_vs_independent": float(
                method_rmse["pilot_corr_selector"] - method_rmse["independent"]
            ),
            "pilot_corr_severity_selector_delta_vs_partial": float(
                method_rmse["pilot_corr_severity_selector"] - method_rmse["partial_pooling"]
            ),
            "pilot_corr_severity_selector_delta_vs_independent": float(
                method_rmse["pilot_corr_severity_selector"] - method_rmse["independent"]
            ),
        }
    return cell


def aggregate_results(cells: List[Dict[str, Any]], budgets: List[int]) -> Dict[str, Any]:
    """Aggregate selector win counts, regrets, and regime diagnostics."""

    total_tests = len(cells) * len(budgets)
    method_win_counts = {method: 0 for method in METHODS}
    selector_tie_counts = {
        "oracle_regime_selector": 0,
        "pilot_corr_selector": 0,
        "pilot_corr_severity_selector": 0,
    }
    negative_tests = 0
    high_positive_tests = 0
    failure_slices: List[Dict[str, Any]] = []
    metric_buckets: Dict[str, Dict[str, List[float]]] = {
        method: defaultdict(list) for method in METHODS
    }

    for cell in cells:
        is_negative = cell["cate_error_correlation"] == "negative"
        is_high_positive = (
            cell["misclassification_severity"] == "high"
            and cell["cate_error_correlation"] == "positive"
        )
        for budget in budgets:
            budget_key = str(budget)
            summary = cell["budgets"][budget_key]["summary"]
            winner = summary["winner_by_cate_rmse"]
            method_win_counts[winner] += 1
            negative_tests += int(is_negative)
            high_positive_tests += int(is_high_positive)

            for selector in selector_tie_counts:
                if summary[f"{selector}_ties_or_beats_fixed_best"]:
                    selector_tie_counts[selector] += 1

            for method in METHODS:
                method_metrics = cell["budgets"][budget_key][method]
                metric_buckets[method]["cate_rmse"].append(method_metrics["cate_rmse"]["mean"])
                metric_buckets[method]["regret_vs_oracle_best_pi"].append(
                    method_metrics["regret_vs_oracle_best_pi"]["mean"]
                )
                metric_buckets[method]["delta_vs_fixed_partial"].append(
                    method_metrics["delta_vs_fixed_partial"]["mean"]
                )
                metric_buckets[method]["delta_vs_fixed_independent"].append(
                    method_metrics["delta_vs_fixed_independent"]["mean"]
                )
                if method in ("pilot_corr_selector", "pilot_corr_severity_selector"):
                    metric_buckets[method]["selected_independent"].append(
                        method_metrics["selected_independent"]["mean"]
                    )
                    metric_buckets[method]["oracle_choice_match"].append(
                        method_metrics["oracle_choice_match"]["mean"]
                    )
                    if is_negative:
                        metric_buckets[method]["negative_selected_independent"].append(
                            method_metrics["selected_independent"]["mean"]
                        )
                    if is_high_positive:
                        metric_buckets[method]["high_positive_delta_vs_partial"].append(
                            summary[f"{method}_delta_vs_partial"]
                        )

            for selector in ("pilot_corr_selector", "pilot_corr_severity_selector"):
                if not summary[f"{selector}_ties_or_beats_fixed_best"]:
                    failure_slices.append({
                        "selector": selector,
                        "subgroup_count": cell["subgroup_count"],
                        "misclassification_severity": cell["misclassification_severity"],
                        "cate_error_correlation": cell["cate_error_correlation"],
                        "budget": budget,
                        "winner_by_cate_rmse": winner,
                        "fixed_best_winner": summary["fixed_best_winner"],
                        "selector_delta_vs_partial": summary[f"{selector}_delta_vs_partial"],
                        "selector_delta_vs_independent": summary[f"{selector}_delta_vs_independent"],
                    })

    method_summary: Dict[str, Dict[str, Any]] = {}
    for method, buckets in metric_buckets.items():
        method_summary[method] = {
            "win_count": method_win_counts[method],
            "win_rate": float(method_win_counts[method] / total_tests),
            "cate_rmse": summarize(buckets["cate_rmse"]),
            "regret_vs_oracle_best_pi": summarize(buckets["regret_vs_oracle_best_pi"]),
            "delta_vs_fixed_partial": summarize(buckets["delta_vs_fixed_partial"]),
            "delta_vs_fixed_independent": summarize(buckets["delta_vs_fixed_independent"]),
        }
        if method in selector_tie_counts:
            method_summary[method]["ties_or_beats_fixed_best_count"] = selector_tie_counts[method]
            method_summary[method]["ties_or_beats_fixed_best_rate"] = float(
                selector_tie_counts[method] / total_tests
            )
        if "selected_independent" in buckets:
            method_summary[method]["selected_independent_rate"] = float(np.mean(buckets["selected_independent"]))
            method_summary[method]["oracle_choice_match_rate"] = float(np.mean(buckets["oracle_choice_match"]))
            method_summary[method]["negative_cell_selected_independent_rate"] = float(
                np.mean(buckets["negative_selected_independent"])
            ) if buckets["negative_selected_independent"] else 0.0
            method_summary[method]["high_positive_delta_vs_partial_mean"] = float(
                np.mean(buckets["high_positive_delta_vs_partial"])
            ) if buckets["high_positive_delta_vs_partial"] else 0.0

    return {
        "total_cell_budget_tests": total_tests,
        "negative_correlation_tests": negative_tests,
        "high_severity_positive_tests": high_positive_tests,
        "method_summary": method_summary,
        "failure_slices": failure_slices,
    }


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=5000)
    parser.add_argument("--reps", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260531)
    parser.add_argument("--budgets", type=int, nargs="+", default=[500, 2000])
    parser.add_argument("--subgroup-counts", type=int, nargs="+", default=list(SUBGROUP_COUNTS))
    parser.add_argument("--severities", nargs="+", default=list(SEVERITIES))
    parser.add_argument("--correlations", nargs="+", default=list(CORRELATIONS))
    parser.add_argument("--shrinkage-strength", type=float, default=80.0)
    parser.add_argument("--corr-threshold", type=float, default=-0.10)
    parser.add_argument("--strong-negative-threshold", type=float, default=-0.20)
    parser.add_argument("--high-severity-threshold", type=float, default=0.25)
    parser.add_argument("--out", type=Path, default=Path("docs/results/e009_regime_aware_estimator_selection.json"))
    return parser.parse_args()


def main() -> None:
    """Run regime-aware selector experiment and write JSON output."""

    args = parse_args()
    e002 = load_e002_module()
    rng = np.random.default_rng(args.seed)
    cells = []
    for k in args.subgroup_counts:
        for severity in args.severities:
            for correlation in args.correlations:
                cells.append(run_cell(
                    e002=e002,
                    rng=rng,
                    n=args.n,
                    reps=args.reps,
                    budgets=args.budgets,
                    k=int(k),
                    severity=str(severity),
                    correlation=str(correlation),
                    shrinkage_strength=args.shrinkage_strength,
                    corr_threshold=args.corr_threshold,
                    strong_negative_threshold=args.strong_negative_threshold,
                    high_severity_threshold=args.high_severity_threshold,
                ))

    result = {
        "exp_id": "e009_regime_aware_estimator_selection",
        "parent": "e008_stage1_dgp_robustness",
        "hypothesis": (
            "A pilot-proxy regime-aware selector that chooses independent estimation "
            "in negative CATE-error correlation regimes and partial-pooling otherwise "
            "can improve downstream CATE RMSE win rate over fixed partial-pooling and "
            "fixed independent across the e008 DGP grid, while retaining partial-pooling "
            "gains in high-severity positive-correlation cells."
        ),
        "seed": args.seed,
        "n": args.n,
        "reps": args.reps,
        "budgets": args.budgets,
        "subgroup_counts": args.subgroup_counts,
        "misclassification_severities": args.severities,
        "cate_error_correlations": args.correlations,
        "methods": list(METHODS),
        "selector_rules": {
            "pilot_corr_selector": (
                "Estimate independent row-wise error rates from finite expert labels; "
                "estimate preliminary subgroup CATE magnitudes from observed noisy labels; "
                "choose independent if corr(error_proxy, abs(observed_tau)) < -0.10, "
                "otherwise choose partial_pooling."
            ),
            "pilot_corr_severity_selector": (
                "Use the same proxy correlation plus max estimated row error as severity proxy; "
                "choose independent if proxy corr < -0.20, or if proxy corr < -0.10 and max "
                "estimated row error < 0.25; otherwise choose partial_pooling, preserving "
                "high-severity nonnegative-correlation partial-pooling behavior."
            ),
            "oracle_regime_selector": (
                "Upper bound that chooses the lower realized CATE RMSE between partial_pooling "
                "and independent within each replication; it is not deployable."
            ),
        },
        "thresholds": {
            "corr_threshold": args.corr_threshold,
            "strong_negative_threshold": args.strong_negative_threshold,
            "high_severity_threshold": args.high_severity_threshold,
        },
        "dgp_grid_size": len(cells),
        "gpu_probe": e002.touch_gpu(),
        "cells": cells,
        "aggregate": aggregate_results(cells, args.budgets),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
