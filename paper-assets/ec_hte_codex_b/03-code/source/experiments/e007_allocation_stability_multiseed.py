"""Run multi-seed allocation stability diagnostics for EC-HTE.

Inputs:
    Synthetic DGP controls, expert-label budgets, seed-block count, reps per
    seed block, and output path supplied by command line flags.

Outputs:
    A JSON file reporting per-seed and aggregate stability for targeted,
    capped, and hybrid expert-label allocation strategies. Metrics include
    mean/std and sign consistency for group5 coverage delta, group5 bias delta,
    overall CATE RMSE delta versus uniform, plus target pass rates.

Key dependencies:
    numpy for aggregation. The same local e006 module supplies the DGP,
    allocation methods, CATE correction, and optional CUDA visibility probe.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

import numpy as np


METHODS = (
    "uniform",
    "cate_error_product",
    "capped_cate_error_25pct",
    "capped_cate_error_35pct",
    "hybrid_50_50_uniform_cate_error",
    "hybrid_70_30_uniform_cate_error",
)

E005_RMSE_COST = {
    100: 0.004509780302770841,
    500: 0.0015425285997547195,
    1000: 0.0021752546377083737,
    2000: 0.0024976760819066385,
}


def load_e006_module() -> Any:
    """Load the e006 implementation so e007 uses the same DGP and estimators."""

    module_path = Path(__file__).with_name("e006_capped_hybrid_allocation.py")
    spec = importlib.util.spec_from_file_location("e006_capped_hybrid_allocation", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load e006 module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def summarize(values: Iterable[float]) -> Dict[str, float]:
    """Summarize a list of seed-level scalar values."""

    arr = np.asarray(list(values), dtype=float)
    return {
        "mean": float(arr.mean()),
        "sd": float(arr.std(ddof=1)) if len(arr) > 1 else 0.0,
        "min": float(arr.min()),
        "p25": float(np.quantile(arr, 0.25)),
        "p50": float(np.quantile(arr, 0.50)),
        "p75": float(np.quantile(arr, 0.75)),
        "max": float(arr.max()),
    }


def sign_summary(values: Iterable[float]) -> Dict[str, Any]:
    """Return sign consistency counts and rates for seed-level deltas."""

    arr = np.asarray(list(values), dtype=float)
    positive = int(np.sum(arr > 0.0))
    negative = int(np.sum(arr < 0.0))
    zero = int(np.sum(arr == 0.0))
    return {
        "positive_count": positive,
        "negative_count": negative,
        "zero_count": zero,
        "positive_rate": float(positive / len(arr)),
        "negative_rate": float(negative / len(arr)),
        "sign_changing": bool(positive > 0 and negative > 0),
    }


def seed_block_summary(
    e006: Any,
    seed: int,
    n: int,
    reps: int,
    budgets: List[int],
    shrinkage_strength: float,
) -> Dict[str, Any]:
    """Run one independent seed block and return budget/method summaries."""

    rng = np.random.default_rng(seed)
    true_probs = np.array([0.30, 0.22, 0.18, 0.13, 0.10, 0.07], dtype=float)
    true_tau = np.array([0.05, 0.12, 0.20, 0.32, 0.45, 0.60], dtype=float)
    error_rates = np.array([0.04, 0.08, 0.12, 0.18, 0.26, 0.35], dtype=float)

    raw: Dict[int, Dict[str, Dict[str, List[float]]]] = {
        budget: {method: {} for method in METHODS} for budget in budgets
    }
    for _ in range(reps):
        rep = e006.run_replication(
            rng=rng,
            n=n,
            budgets=budgets,
            true_probs=true_probs,
            true_tau=true_tau,
            error_rates=error_rates,
            shrinkage_strength=shrinkage_strength,
            outcome_sd=1.0,
        )
        for budget in budgets:
            for method in METHODS:
                for metric, value in rep[budget][method].items():
                    if metric in {
                        "group5_empirical_95_coverage",
                        "group5_cate_bias",
                        "overall_cate_rmse",
                    }:
                        raw[budget][method].setdefault(metric, []).append(float(value))

    block: Dict[str, Any] = {"seed": seed, "budgets": {}}
    for budget in budgets:
        budget_key = str(budget)
        block["budgets"][budget_key] = {}
        for method in METHODS:
            method_metrics = {
                metric: float(np.mean(values)) for metric, values in raw[budget][method].items()
            }
            block["budgets"][budget_key][method] = method_metrics

        uniform = block["budgets"][budget_key]["uniform"]
        block["budgets"][budget_key]["deltas_vs_uniform"] = {}
        for method in METHODS:
            if method == "uniform":
                continue
            current = block["budgets"][budget_key][method]
            cov_delta = current["group5_empirical_95_coverage"] - uniform["group5_empirical_95_coverage"]
            bias_delta = current["group5_cate_bias"] - uniform["group5_cate_bias"]
            rmse_delta = current["overall_cate_rmse"] - uniform["overall_cate_rmse"]
            block["budgets"][budget_key]["deltas_vs_uniform"][method] = {
                "group5_coverage_delta": float(cov_delta),
                "group5_bias_delta": float(bias_delta),
                "overall_cate_rmse_delta": float(rmse_delta),
                "target_pass": bool(cov_delta > 0.0 and rmse_delta <= E005_RMSE_COST[budget]),
            }
    return block


def aggregate_seed_blocks(seed_blocks: List[Dict[str, Any]], budgets: List[int]) -> Dict[str, Any]:
    """Aggregate seed-block deltas into stability metrics by budget and method."""

    aggregate: Dict[str, Any] = {}
    for budget in budgets:
        budget_key = str(budget)
        aggregate[budget_key] = {}
        for method in METHODS:
            if method == "uniform":
                continue
            deltas = [
                block["budgets"][budget_key]["deltas_vs_uniform"][method]
                for block in seed_blocks
            ]
            coverage = [d["group5_coverage_delta"] for d in deltas]
            bias = [d["group5_bias_delta"] for d in deltas]
            rmse = [d["overall_cate_rmse_delta"] for d in deltas]
            target_pass = [float(d["target_pass"]) for d in deltas]
            aggregate[budget_key][method] = {
                "group5_coverage_delta": summarize(coverage),
                "group5_coverage_delta_sign": sign_summary(coverage),
                "group5_bias_delta": summarize(bias),
                "group5_bias_delta_sign": sign_summary(bias),
                "overall_cate_rmse_delta": summarize(rmse),
                "overall_cate_rmse_delta_sign": sign_summary(rmse),
                "target_pass_rate": float(np.mean(target_pass)),
                "target_pass_count": int(np.sum(target_pass)),
                "target_definition": "group5 coverage delta > 0 and RMSE delta <= e005 cate_error_product cost for the same B",
            }
    return aggregate


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=5000)
    parser.add_argument("--reps-per-seed", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260531)
    parser.add_argument("--num-seeds", type=int, default=10)
    parser.add_argument("--budgets", type=int, nargs="+", default=[1000, 2000])
    parser.add_argument("--shrinkage-strength", type=float, default=80.0)
    parser.add_argument("--out", type=Path, default=Path("docs/results/e007_allocation_stability_multiseed.json"))
    return parser.parse_args()


def main() -> None:
    """Run the multi-seed stability diagnostic and write JSON output."""

    args = parse_args()
    e006 = load_e006_module()
    seed_values = [int(args.seed + 1009 * i) for i in range(args.num_seeds)]
    seed_blocks = [
        seed_block_summary(
            e006=e006,
            seed=seed,
            n=args.n,
            reps=args.reps_per_seed,
            budgets=args.budgets,
            shrinkage_strength=args.shrinkage_strength,
        )
        for seed in seed_values
    ]
    aggregate = aggregate_seed_blocks(seed_blocks, args.budgets)
    result = {
        "exp_id": "e007_allocation_stability_multiseed",
        "parent": "e006_capped_hybrid_allocation",
        "hypothesis": (
            "If targeted allocation is a robust Stage 1 mitigation, cate_error_product "
            "and capped/hybrid variants should show positive mean group5 coverage/bias "
            "gains over uniform across independent random seeds, with bounded overall "
            "CATE RMSE penalty; if gains change sign across seeds, the e005 claim must "
            "be weakened to seed-sensitive tradeoff."
        ),
        "n": args.n,
        "reps_per_seed": args.reps_per_seed,
        "num_seeds": args.num_seeds,
        "seed_values": seed_values,
        "budgets": args.budgets,
        "methods": list(METHODS),
        "dgp_family": "same true_probs, true_tau, error_rates, partial-pooling Stage 1 estimator, and interval construction as e005/e006",
        "runtime_scope_note": "B={1000,2000} only: D008 asks to focus on stability at the budgets where e005/e006 direction diverged; lower budgets omitted to keep the 10-seed diagnostic fast on the single allocated GPU.",
        "comparison_notes": {
            "e005": "single seed=20260531, n=5000, reps=200, B={100,500,1000,2000}, methods uniform/error_proportional/cate_error_product/oracle_targeted; cate_error_product B2000 coverage=0.950 vs uniform=0.925.",
            "e006": "single seed=20260531, n=5000, reps=200, B={100,500,1000,2000}, methods uniform/cate_error_product/capped/hybrid; B2000 target checks false and cate_error_product/capped coverage=0.940 vs uniform=0.945.",
            "e007": "independent seed blocks generated as base_seed + 1009*i; each seed block reports within-seed deltas vs uniform before aggregate sign-consistency checks.",
        },
        "e005_rmse_cost_reference": {str(k): v for k, v in E005_RMSE_COST.items()},
        "gpu_probe": e006.touch_gpu(),
        "seed_blocks": seed_blocks,
        "aggregate": aggregate,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
