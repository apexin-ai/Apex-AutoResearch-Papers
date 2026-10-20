"""Run Stage 1 DGP robustness checks for EC-HTE confusion estimation.

Inputs:
    Synthetic DGP grid controls, expert-label budgets, replication count, and
    output path supplied by command line flags.

Outputs:
    A JSON file with per-grid-cell metrics for global, independent, and
    partial-pooling confusion estimators. Metrics include downstream subgroup
    CATE RMSE, mean/max subgroup bias, confusion recovery RMSE, pairwise deltas,
    win counts, failure slices, and interaction summaries.

Key dependencies:
    numpy for simulation. The e002 module supplies the original Stage 1
    estimator implementation so this robustness check preserves e002 semantics.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import numpy as np


METHODS = ("global", "independent", "partial_pooling")
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
    """Create one DGP with heterogeneous subgroup sizes, CATEs, and errors."""

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
        # Alternating ranks keep misclassification heterogeneous without a
        # monotone relationship to the increasing true CATE vector.
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
) -> Dict[str, Any]:
    """Run one DGP grid cell across budgets and estimators."""

    params = dgp_parameters(k, severity, correlation)
    raw: Dict[int, Dict[str, Dict[str, List[float]]]] = {
        budget: {method: defaultdict(list) for method in METHODS} for budget in budgets
    }
    for _ in range(reps):
        rep = e002.run_replication(
            rng=rng,
            n=n,
            budgets=budgets,
            true_probs=params["true_probs"],
            true_tau=params["true_tau"],
            error_rates=params["error_rates"],
            shrinkage_strength=shrinkage_strength,
            outcome_sd=1.0,
        )
        for budget in budgets:
            for method in METHODS:
                for metric, value in rep[budget][method].items():
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
        winner = min(method_rmse, key=method_rmse.get)
        partial = cell["budgets"][budget_key]["partial_pooling"]
        global_m = cell["budgets"][budget_key]["global"]
        independent = cell["budgets"][budget_key]["independent"]
        cell["budgets"][budget_key]["deltas"] = {
            "partial_minus_global_cate_rmse": float(partial["cate_rmse"]["mean"] - global_m["cate_rmse"]["mean"]),
            "partial_minus_independent_cate_rmse": float(partial["cate_rmse"]["mean"] - independent["cate_rmse"]["mean"]),
            "partial_minus_global_confusion_rmse": float(partial["confusion_recovery_rmse"]["mean"] - global_m["confusion_recovery_rmse"]["mean"]),
            "partial_minus_independent_confusion_rmse": float(partial["confusion_recovery_rmse"]["mean"] - independent["confusion_recovery_rmse"]["mean"]),
            "winner_by_cate_rmse": winner,
            "partial_best": bool(winner == "partial_pooling"),
        }
    return cell


def interaction_key(cell: Dict[str, Any], axis: str) -> str:
    """Return grouping key for interaction summaries."""

    if axis == "severity":
        return str(cell["misclassification_severity"])
    if axis == "correlation":
        return str(cell["cate_error_correlation"])
    if axis == "subgroup_count":
        return str(cell["subgroup_count"])
    raise ValueError(axis)


def aggregate_results(cells: List[Dict[str, Any]], budgets: List[int]) -> Dict[str, Any]:
    """Aggregate wins, failures, and interaction summaries across grid cells."""

    total_tests = len(cells) * len(budgets)
    partial_wins = 0
    high_positive_tests = 0
    high_positive_wins = 0
    failure_slices: List[Dict[str, Any]] = []
    deltas_by_budget: Dict[str, Dict[str, List[float]]] = {
        str(b): {"partial_minus_global": [], "partial_minus_independent": []} for b in budgets
    }
    interaction_buckets: Dict[str, Dict[str, Dict[str, List[float]]]] = {
        "severity": defaultdict(lambda: {"wins": [], "partial_minus_global": [], "partial_minus_independent": []}),
        "correlation": defaultdict(lambda: {"wins": [], "partial_minus_global": [], "partial_minus_independent": []}),
        "subgroup_count": defaultdict(lambda: {"wins": [], "partial_minus_global": [], "partial_minus_independent": []}),
    }

    for cell in cells:
        for budget in budgets:
            budget_key = str(budget)
            deltas = cell["budgets"][budget_key]["deltas"]
            partial_best = bool(deltas["partial_best"])
            partial_wins += int(partial_best)
            if cell["misclassification_severity"] == "high" and cell["cate_error_correlation"] == "positive":
                high_positive_tests += 1
                high_positive_wins += int(partial_best)
            if not partial_best:
                failure_slices.append({
                    "subgroup_count": cell["subgroup_count"],
                    "misclassification_severity": cell["misclassification_severity"],
                    "cate_error_correlation": cell["cate_error_correlation"],
                    "budget": budget,
                    "winner_by_cate_rmse": deltas["winner_by_cate_rmse"],
                    "partial_minus_global_cate_rmse": deltas["partial_minus_global_cate_rmse"],
                    "partial_minus_independent_cate_rmse": deltas["partial_minus_independent_cate_rmse"],
                })
            deltas_by_budget[budget_key]["partial_minus_global"].append(deltas["partial_minus_global_cate_rmse"])
            deltas_by_budget[budget_key]["partial_minus_independent"].append(deltas["partial_minus_independent_cate_rmse"])
            for axis in interaction_buckets:
                key = interaction_key(cell, axis)
                interaction_buckets[axis][key]["wins"].append(float(partial_best))
                interaction_buckets[axis][key]["partial_minus_global"].append(deltas["partial_minus_global_cate_rmse"])
                interaction_buckets[axis][key]["partial_minus_independent"].append(deltas["partial_minus_independent_cate_rmse"])

    budget_summary = {}
    for budget, values in deltas_by_budget.items():
        budget_summary[budget] = {
            "partial_minus_global_cate_rmse": summarize(values["partial_minus_global"]),
            "partial_minus_independent_cate_rmse": summarize(values["partial_minus_independent"]),
        }

    interaction_summary: Dict[str, Dict[str, Any]] = {}
    for axis, buckets in interaction_buckets.items():
        interaction_summary[axis] = {}
        for key, values in buckets.items():
            interaction_summary[axis][key] = {
                "tests": len(values["wins"]),
                "partial_win_count": int(np.sum(values["wins"])),
                "partial_win_rate": float(np.mean(values["wins"])),
                "partial_minus_global_cate_rmse_mean": float(np.mean(values["partial_minus_global"])),
                "partial_minus_independent_cate_rmse_mean": float(np.mean(values["partial_minus_independent"])),
            }

    return {
        "total_cell_budget_tests": total_tests,
        "partial_win_count": partial_wins,
        "partial_win_rate": float(partial_wins / total_tests),
        "high_severity_positive_tests": high_positive_tests,
        "high_severity_positive_partial_win_count": high_positive_wins,
        "high_severity_positive_partial_win_rate": float(high_positive_wins / high_positive_tests) if high_positive_tests else 0.0,
        "budget_summary": budget_summary,
        "interaction_summary": interaction_summary,
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
    parser.add_argument("--out", type=Path, default=Path("docs/results/e008_stage1_dgp_robustness.json"))
    return parser.parse_args()


def main() -> None:
    """Run Stage 1 robustness grid and write JSON output."""

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
                ))

    aggregate = aggregate_results(cells, args.budgets)
    result = {
        "exp_id": "e008_stage1_dgp_robustness",
        "parent": "e002_budgeted_confusion_estimation",
        "hypothesis": (
            "Hierarchical/partial-pooling confusion estimation reduces downstream subgroup "
            "CATE RMSE relative to global pooled and independent per-subgroup estimation "
            "across DGP regimes with heterogeneous subgroup misclassification; the advantage "
            "should be strongest under high misclassification severity and positive CATE-error "
            "correlation, and may shrink under low severity or weak heterogeneity."
        ),
        "seed": args.seed,
        "n": args.n,
        "reps": args.reps,
        "budgets": args.budgets,
        "subgroup_counts": args.subgroup_counts,
        "misclassification_severities": args.severities,
        "cate_error_correlations": args.correlations,
        "methods": list(METHODS),
        "dgp_grid_size": len(cells),
        "low_heterogeneity_slice_included": False,
        "low_heterogeneity_note": "Not included: D009 required nonzero CATE heterogeneity and the minimum 27-cell grid already covers subgroup count, severity, and correlation regimes.",
        "gpu_probe": e002.touch_gpu(),
        "cells": cells,
        "aggregate": aggregate,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
