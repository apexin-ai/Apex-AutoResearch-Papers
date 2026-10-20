"""Test seed and threshold sensitivity of the e009 deployable selector.

Inputs:
    The e009 DGP grid, independent seed blocks, selector threshold grids, expert
    label budgets, replication count, and output path from command line flags.

Outputs:
    A JSON file with per seed/threshold win/tie/loss versus the best fixed
    partial-pooling-or-independent estimator, negative-correlation failure rates,
    high-positive loss counts, delta summaries, worst cells, and global stability
    summaries for both deployable e009 selector rules.

Key dependencies:
    numpy for simulation. e002 supplies the original Stage 1 estimator helpers;
    e009 supplies the DGP family and selector decision rule.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import numpy as np


SUBGROUP_COUNTS = (4, 6, 8)
SEVERITIES = ("low", "medium", "high")
CORRELATIONS = ("positive", "zero", "negative")
SELECTORS = ("pilot_corr_selector", "pilot_corr_severity_selector")


def load_module(filename: str, module_name: str) -> Any:
    """Load a sibling experiment module by filename."""

    module_path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {module_name} from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def summarize(values: Iterable[float]) -> Dict[str, float]:
    """Summarize scalar metrics with robust defaults for singletons."""

    arr = np.asarray(list(values), dtype=float)
    return {
        "mean": float(arr.mean()),
        "median": float(np.median(arr)),
        "sd": float(arr.std(ddof=1)) if len(arr) > 1 else 0.0,
        "min": float(arr.min()),
        "max": float(arr.max()),
        "p10": float(np.quantile(arr, 0.10)),
        "p90": float(np.quantile(arr, 0.90)),
    }


def compute_base_record(
    e002: Any,
    e009: Any,
    rng: np.random.Generator,
    n: int,
    budget: int,
    true_probs: np.ndarray,
    true_tau: np.ndarray,
    error_rates: np.ndarray,
    shrinkage_strength: float,
) -> Dict[str, float]:
    """Run one replication and cache threshold-independent selector inputs."""

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

    cate_rmse: Dict[str, float] = {}
    for method in ("partial_pooling", "independent"):
        estimated_errors = e002.estimate_error_rates(
            true_expert=true_expert,
            observed_expert=observed_expert,
            k=k,
            method=method,
            shrinkage_strength=shrinkage_strength,
        )
        estimated_transition = e002.transition_matrix(estimated_errors)
        tau_hat = e002.corrected_tau(observed_tau, observed_probs, true_probs, estimated_transition)
        cate_rmse[method] = e009.metric_from_tau(
            tau_hat=tau_hat,
            true_tau=true_tau,
            estimated_transition=estimated_transition,
            true_transition=true_transition,
            confusion_rmse_fn=e002.confusion_recovery_rmse,
        )["cate_rmse"]

    independent_error_proxy = e002.estimate_error_rates(
        true_expert=true_expert,
        observed_expert=observed_expert,
        k=k,
        method="independent",
        shrinkage_strength=shrinkage_strength,
    )
    proxy_corr = e009.safe_corr(independent_error_proxy, np.abs(observed_tau))
    severity_proxy = float(np.max(independent_error_proxy))
    fixed_best = min(cate_rmse["partial_pooling"], cate_rmse["independent"])
    return {
        "partial_pooling_rmse": cate_rmse["partial_pooling"],
        "independent_rmse": cate_rmse["independent"],
        "fixed_best_rmse": fixed_best,
        "proxy_corr": proxy_corr,
        "severity_proxy": severity_proxy,
    }


def evaluate_records(
    e009: Any,
    records: List[Dict[str, Any]],
    corr_threshold: float,
    severity_threshold: float,
    strong_negative_threshold: float,
) -> Dict[str, Any]:
    """Evaluate both deployable selectors over cached base records."""

    result: Dict[str, Any] = {}
    for selector in SELECTORS:
        win = tie = loss = 0
        neg_loss = 0
        hp_loss = 0
        deltas_best: List[float] = []
        deltas_partial: List[float] = []
        deltas_independent: List[float] = []
        worst: Dict[str, Any] | None = None
        for rec in records:
            choice = e009.selector_decision(
                selector=selector,
                proxy_corr=rec["proxy_corr"],
                severity_proxy=rec["severity_proxy"],
                corr_threshold=corr_threshold,
                strong_negative_threshold=strong_negative_threshold,
                high_severity_threshold=severity_threshold,
            )
            selector_rmse = rec[f"{choice}_rmse"]
            delta_best = selector_rmse - rec["fixed_best_rmse"]
            delta_partial = selector_rmse - rec["partial_pooling_rmse"]
            delta_independent = selector_rmse - rec["independent_rmse"]
            deltas_best.append(float(delta_best))
            deltas_partial.append(float(delta_partial))
            deltas_independent.append(float(delta_independent))
            if delta_best < -1e-12:
                win += 1
            elif abs(delta_best) <= 1e-12:
                tie += 1
            else:
                loss += 1
                neg_loss += int(rec["cate_error_correlation"] == "negative")
                hp_loss += int(
                    rec["cate_error_correlation"] == "positive"
                    and rec["misclassification_severity"] == "high"
                )
            if worst is None or delta_best > worst["delta_vs_best_fixed"]:
                worst = {
                    "seed": rec["seed"],
                    "subgroup_count": rec["subgroup_count"],
                    "misclassification_severity": rec["misclassification_severity"],
                    "cate_error_correlation": rec["cate_error_correlation"],
                    "budget": rec["budget"],
                    "rep": rec["rep"],
                    "choice": choice,
                    "delta_vs_best_fixed": float(delta_best),
                    "delta_vs_fixed_partial": float(delta_partial),
                    "delta_vs_fixed_independent": float(delta_independent),
                    "proxy_corr": float(rec["proxy_corr"]),
                    "severity_proxy": float(rec["severity_proxy"]),
                }

        negative_tests = sum(1 for r in records if r["cate_error_correlation"] == "negative")
        high_positive_tests = sum(
            1 for r in records
            if r["cate_error_correlation"] == "positive" and r["misclassification_severity"] == "high"
        )
        result[selector] = {
            "win": win,
            "tie": tie,
            "loss": loss,
            "win_tie": win + tie,
            "total": len(records),
            "win_tie_rate": float((win + tie) / len(records)),
            "loss_rate": float(loss / len(records)),
            "negative_failure_count": neg_loss,
            "negative_failure_rate": float(neg_loss / negative_tests) if negative_tests else 0.0,
            "high_positive_loss_count": hp_loss,
            "high_positive_loss_rate": float(hp_loss / high_positive_tests) if high_positive_tests else 0.0,
            "delta_vs_best_fixed": summarize(deltas_best),
            "delta_vs_fixed_partial": summarize(deltas_partial),
            "delta_vs_fixed_independent": summarize(deltas_independent),
            "worst_cell": worst,
        }
    return result


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=5000)
    parser.add_argument("--reps", type=int, default=100)
    parser.add_argument("--base-seed", type=int, default=20260531)
    parser.add_argument("--num-seeds", type=int, default=5)
    parser.add_argument("--seed-step", type=int, default=1009)
    parser.add_argument("--budgets", type=int, nargs="+", default=[500, 2000])
    parser.add_argument("--subgroup-counts", type=int, nargs="+", default=list(SUBGROUP_COUNTS))
    parser.add_argument("--severities", nargs="+", default=list(SEVERITIES))
    parser.add_argument("--correlations", nargs="+", default=list(CORRELATIONS))
    parser.add_argument("--corr-thresholds", type=float, nargs="+", default=[-0.05, -0.10, -0.20])
    parser.add_argument("--severity-thresholds", type=float, nargs="+", default=[0.20, 0.25, 0.30])
    parser.add_argument("--strong-negative-threshold", type=float, default=-0.20)
    parser.add_argument("--shrinkage-strength", type=float, default=80.0)
    parser.add_argument("--out", type=Path, default=Path("docs/results/e010_selector_seed_threshold_sensitivity.json"))
    return parser.parse_args()


def main() -> None:
    """Run the sensitivity grid and write JSON output."""

    args = parse_args()
    e002 = load_module("e002_budgeted_confusion_estimation.py", "e002_budgeted_confusion_estimation")
    e009 = load_module("e009_regime_aware_estimator_selection.py", "e009_regime_aware_estimator_selection")
    seed_values = [args.base_seed + args.seed_step * i for i in range(args.num_seeds)]

    per_seed: List[Dict[str, Any]] = []
    all_threshold_summaries: List[Dict[str, Any]] = []
    for seed in seed_values:
        rng = np.random.default_rng(seed)
        records: List[Dict[str, Any]] = []
        for k in args.subgroup_counts:
            for severity in args.severities:
                for correlation in args.correlations:
                    params = e009.dgp_parameters(int(k), str(severity), str(correlation))
                    for budget in args.budgets:
                        for rep in range(args.reps):
                            rec = compute_base_record(
                                e002=e002,
                                e009=e009,
                                rng=rng,
                                n=args.n,
                                budget=int(budget),
                                true_probs=params["true_probs"],
                                true_tau=params["true_tau"],
                                error_rates=params["error_rates"],
                                shrinkage_strength=args.shrinkage_strength,
                            )
                            rec.update({
                                "seed": seed,
                                "subgroup_count": int(k),
                                "misclassification_severity": str(severity),
                                "cate_error_correlation": str(correlation),
                                "budget": int(budget),
                                "rep": rep,
                            })
                            records.append(rec)

        seed_entry = {"seed": seed, "records": len(records), "thresholds": []}
        for corr_threshold in args.corr_thresholds:
            for severity_threshold in args.severity_thresholds:
                summary = evaluate_records(
                    e009=e009,
                    records=records,
                    corr_threshold=float(corr_threshold),
                    severity_threshold=float(severity_threshold),
                    strong_negative_threshold=args.strong_negative_threshold,
                )
                entry = {
                    "seed": seed,
                    "corr_threshold": float(corr_threshold),
                    "severity_threshold": float(severity_threshold),
                    "selectors": summary,
                }
                seed_entry["thresholds"].append(entry)
                all_threshold_summaries.append(entry)
        per_seed.append(seed_entry)

    aggregate: Dict[str, Any] = {}
    for selector in SELECTORS:
        totals = [entry["selectors"][selector] for entry in all_threshold_summaries]
        aggregate[selector] = {
            "threshold_seed_combinations": len(totals),
            "win_tie_rate": summarize(t["win_tie_rate"] for t in totals),
            "loss_rate": summarize(t["loss_rate"] for t in totals),
            "negative_failure_rate": summarize(t["negative_failure_rate"] for t in totals),
            "negative_failure_count": summarize(t["negative_failure_count"] for t in totals),
            "high_positive_loss_count": summarize(t["high_positive_loss_count"] for t in totals),
            "high_positive_loss_rate": summarize(t["high_positive_loss_rate"] for t in totals),
            "mean_delta_vs_best_fixed": summarize(t["delta_vs_best_fixed"]["mean"] for t in totals),
            "median_delta_vs_best_fixed": summarize(t["delta_vs_best_fixed"]["median"] for t in totals),
            "mean_delta_vs_fixed_partial": summarize(t["delta_vs_fixed_partial"]["mean"] for t in totals),
            "mean_delta_vs_fixed_independent": summarize(t["delta_vs_fixed_independent"]["mean"] for t in totals),
            "worst_seed_threshold": max(
                (
                    {
                        "seed": entry["seed"],
                        "corr_threshold": entry["corr_threshold"],
                        "severity_threshold": entry["severity_threshold"],
                        "selector": selector,
                        "loss_rate": entry["selectors"][selector]["loss_rate"],
                        "negative_failure_rate": entry["selectors"][selector]["negative_failure_rate"],
                        "high_positive_loss_count": entry["selectors"][selector]["high_positive_loss_count"],
                        "worst_cell": entry["selectors"][selector]["worst_cell"],
                    }
                    for entry in all_threshold_summaries
                ),
                key=lambda x: (
                    x["high_positive_loss_count"],
                    x["negative_failure_rate"],
                    x["loss_rate"],
                    x["worst_cell"]["delta_vs_best_fixed"],
                ),
            ),
        }

    result = {
        "exp_id": "e010_selector_seed_threshold_sensitivity",
        "parent": "e009_regime_aware_estimator_selection",
        "hypothesis": (
            "If the e009 deployable regime-aware selector is a stable Stage 1 rule "
            "rather than threshold/seed overfit, then across independent seeds and "
            "reasonable pilot threshold perturbations it should retain near-best "
            "fixed-estimator RMSE, keep negative-correlation failures rare, and "
            "preserve zero or near-zero loss in high-severity positive-correlation cells."
        ),
        "n": args.n,
        "reps": args.reps,
        "budgets": args.budgets,
        "seed_values": seed_values,
        "threshold_grid": {
            "corr": args.corr_thresholds,
            "severity": args.severity_thresholds,
            "strong_negative": args.strong_negative_threshold,
        },
        "subgroup_counts": args.subgroup_counts,
        "misclassification_severities": args.severities,
        "cate_error_correlations": args.correlations,
        "selectors": list(SELECTORS),
        "selector_rules": {
            "pilot_corr_selector": (
                "choose independent if corr(error_proxy, abs(observed_tau)) < corr_threshold; "
                "otherwise partial_pooling"
            ),
            "pilot_corr_severity_selector": (
                "choose independent if corr < strong_negative_threshold, or if corr < "
                "corr_threshold and max row error proxy < severity_threshold; otherwise "
                "partial_pooling"
            ),
        },
        "tests_per_seed_threshold": (
            len(args.subgroup_counts) * len(args.severities) * len(args.correlations)
            * len(args.budgets) * args.reps
        ),
        "per_seed": per_seed,
        "aggregate": aggregate,
        "gpu_probe": e002.touch_gpu(),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
