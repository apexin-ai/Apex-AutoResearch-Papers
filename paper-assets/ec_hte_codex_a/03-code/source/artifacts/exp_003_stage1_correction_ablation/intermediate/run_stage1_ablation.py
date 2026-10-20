#!/usr/bin/env python3
"""Stage 1 correction ablation skeleton for plan_003.

This script prepares the H2 ablation interface and provenance contract. Formal
experiments must wait until exp_002 completes and Director approval is granted.
Tiny smoke runs are allowed for I/O and method-path validation only.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np


EXP_ID = "exp_003_stage1_correction_ablation"
PLAN_ID = "plan_003_stage1_correction_ablation"
CLAIM_ID = "C_PARTIAL_POOLING_BETTER_LOW_BUDGET"
TABLE_ID = "T_STAGE1_CORRECTION_ABLATION"

METHOD_GLOBAL = "global"
METHOD_ARM_SPECIFIC = "arm_specific"
METHOD_PER_SUBGROUP = "per_subgroup_independent"
METHOD_PARTIAL_POOLING = "partial_pooling"
METHODS = [
    METHOD_GLOBAL,
    METHOD_ARM_SPECIFIC,
    METHOD_PER_SUBGROUP,
    METHOD_PARTIAL_POOLING,
]


@dataclass(frozen=True)
class Condition:
    condition_id: str
    budget_label: str
    expert_budget: int
    n: int
    k: int
    misclassification_heterogeneity: str
    cate_heterogeneity: str
    correlation_direction: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare/run Stage1 H2 correction ablation. Use --smoke for tiny "
            "engineering checks; formal runs require exp_002 completion."
        )
    )
    parser.add_argument("--config", required=True, help="Path to JSON config.")
    parser.add_argument("--output-dir", required=True, help="Directory for artifacts.")
    parser.add_argument("--max-replications", type=int, default=None)
    parser.add_argument("--limit-conditions", type=int, default=None)
    parser.add_argument("--smoke", action="store_true", help="Tiny non-conclusive smoke run.")
    parser.add_argument(
        "--allow-formal",
        action="store_true",
        help="Allow formal-scale execution after exp_002 is complete and approved.",
    )
    parser.add_argument(
        "--confirm-exp002-done",
        action="store_true",
        help="Confirm exp_002_gpu_dgp_grid is DONE and Director-approved for Stage1 launch.",
    )
    return parser.parse_args()


def load_config(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def condition_grid(config: dict[str, Any]) -> list[Condition]:
    conditions: list[Condition] = []
    budgets = config["budget_tiers"]
    for budget_label, n, k, mis_h, cate_h, direction in itertools.product(
        budgets.keys(),
        config["n_values"],
        config["subgroup_counts"],
        config["misclassification_heterogeneity"],
        config["cate_heterogeneity"],
        config["correlation_directions"],
    ):
        budget = int(budgets[budget_label]["expert_budget"])
        condition_id = (
            f"budget={budget_label}|B={budget}|N={n}|k={k}|mis={mis_h}|"
            f"cate={cate_h}|corr={direction}"
        )
        conditions.append(
            Condition(
                condition_id=condition_id,
                budget_label=budget_label,
                expert_budget=budget,
                n=int(n),
                k=int(k),
                misclassification_heterogeneity=str(mis_h),
                cate_heterogeneity=str(cate_h),
                correlation_direction=str(direction),
            )
        )
    return conditions


def balanced_limit_conditions(conditions: list[Condition], limit: int) -> list[Condition]:
    if limit <= 0:
        return []
    if limit >= len(conditions):
        return conditions
    by_budget: dict[str, list[Condition]] = {}
    for condition in conditions:
        by_budget.setdefault(condition.budget_label, []).append(condition)
    selected: list[Condition] = []
    labels = list(by_budget)
    idx = 0
    while len(selected) < limit:
        label = labels[idx % len(labels)]
        bucket = by_budget[label]
        if bucket:
            selected.append(bucket.pop(0))
        idx += 1
        if idx > limit * max(len(labels), 1) * 4:
            break
    return selected[:limit]


def cate_values(k: int, heterogeneity: str) -> np.ndarray:
    if heterogeneity == "high":
        values = np.linspace(0.1, 1.25, k)
    else:
        values = np.linspace(0.35, 0.7, k)
    return values - values.mean() + 0.55


def error_rates(
    k: int,
    misclassification_heterogeneity: str,
    cate: np.ndarray,
    direction: str,
) -> np.ndarray:
    if misclassification_heterogeneity == "high":
        low, high = 0.04, 0.38
    else:
        low, high = 0.08, 0.18
    ordered = np.linspace(low, high, k)
    order = np.argsort(np.abs(cate))
    rates = np.empty(k, dtype=float)
    if direction == "positive":
        rates[order] = ordered
    else:
        rates[order] = ordered[::-1]
    return rates


def transition_from_rates(rates: np.ndarray) -> np.ndarray:
    k = len(rates)
    transition = np.zeros((k, k), dtype=float)
    for g, error in enumerate(rates):
        clipped = float(np.clip(error, 0.0, 0.98 * (k - 1) / k))
        transition[:, g] = clipped / max(k - 1, 1)
        transition[g, g] = 1.0 - clipped
    return transition


def posterior_true_given_noisy(transition: np.ndarray, priors: np.ndarray) -> np.ndarray:
    noisy_probs = transition @ priors
    noisy_probs = np.clip(noisy_probs, 1e-12, None)
    return transition * priors[None, :] / noisy_probs[:, None]


def correct_vector(observed_by_noisy: np.ndarray, transition: np.ndarray, priors: np.ndarray) -> np.ndarray:
    posterior = posterior_true_given_noisy(transition, priors)
    return np.linalg.pinv(posterior, rcond=1e-8) @ observed_by_noisy


def sample_noisy_labels(true_g: np.ndarray, rates: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    k = len(rates)
    noisy = true_g.copy()
    error = rng.random(len(true_g)) < rates[true_g]
    shifts = rng.integers(1, k, size=len(true_g))
    noisy[error] = (true_g[error] + shifts[error]) % k
    return noisy


def simulate_dataset(
    condition: Condition,
    config: dict[str, Any],
    rng: np.random.Generator,
) -> dict[str, np.ndarray]:
    k = condition.k
    cate = cate_values(k, condition.cate_heterogeneity)
    rates = error_rates(
        k,
        condition.misclassification_heterogeneity,
        cate,
        condition.correlation_direction,
    )
    probs = np.asarray(config["group_probs"].get(str(k), [1.0 / k] * k), dtype=float)
    probs = probs / probs.sum()
    true_g = rng.choice(k, size=condition.n, p=probs)
    treatment = rng.binomial(1, float(config["treatment_probability"]), size=condition.n)
    arm_delta = float(config["arm_specific_error_delta"])
    arm_rates = np.clip(
        rates[true_g] + arm_delta * (treatment - treatment.mean()),
        0.0,
        0.98 * (k - 1) / k,
    )
    noisy = true_g.copy()
    error = rng.random(condition.n) < arm_rates
    shifts = rng.integers(1, k, size=condition.n)
    noisy[error] = (true_g[error] + shifts[error]) % k
    baseline = 0.15 * true_g + 0.2 * np.cos(true_g)
    outcome = (
        baseline
        + cate[true_g] * treatment
        + rng.normal(0.0, float(config["noise_sd"]), condition.n)
    )
    return {
        "G": true_g,
        "Z": noisy,
        "T": treatment,
        "Y": outcome,
        "tau": cate,
        "base_rates": rates,
    }


def mean_by_label(
    values: np.ndarray,
    labels: np.ndarray,
    k: int,
    fallback: float,
) -> np.ndarray:
    means = np.empty(k, dtype=float)
    for label in range(k):
        mask = labels == label
        means[label] = float(values[mask].mean()) if np.any(mask) else fallback
    return means


def gate_by_noisy_label(data: dict[str, np.ndarray], k: int) -> np.ndarray:
    estimates = np.empty(k, dtype=float)
    global_ate = float(data["Y"][data["T"] == 1].mean() - data["Y"][data["T"] == 0].mean())
    for label in range(k):
        treated = (data["Z"] == label) & (data["T"] == 1)
        control = (data["Z"] == label) & (data["T"] == 0)
        if np.any(treated) and np.any(control):
            estimates[label] = float(data["Y"][treated].mean() - data["Y"][control].mean())
        else:
            estimates[label] = global_ate
    return estimates


def validation_sample(
    data: dict[str, np.ndarray],
    budget: int,
    rng: np.random.Generator,
) -> np.ndarray:
    size = min(int(budget), len(data["G"]))
    return rng.choice(len(data["G"]), size=size, replace=False)


def estimate_global_transition(
    data: dict[str, np.ndarray],
    idx: np.ndarray,
    k: int,
    alpha: float,
) -> np.ndarray:
    mismatch = (data["G"][idx] != data["Z"][idx]).astype(float)
    error = float((mismatch.sum() + alpha) / (len(idx) + 2.0 * alpha))
    return transition_from_rates(np.full(k, error, dtype=float))


def estimate_column_rates(
    data: dict[str, np.ndarray],
    idx: np.ndarray,
    k: int,
    alpha: float,
) -> tuple[np.ndarray, np.ndarray]:
    counts = np.bincount(data["G"][idx], minlength=k).astype(float)
    mismatches = np.bincount(
        data["G"][idx][data["G"][idx] != data["Z"][idx]],
        minlength=k,
    ).astype(float)
    rates = (mismatches + alpha) / (counts + 2.0 * alpha)
    return np.clip(rates, 0.0, 0.98 * (k - 1) / k), counts


def estimate_per_subgroup_transition(
    data: dict[str, np.ndarray],
    idx: np.ndarray,
    k: int,
    alpha: float,
) -> np.ndarray:
    rates, _ = estimate_column_rates(data, idx, k, alpha)
    return transition_from_rates(rates)


def estimate_partial_pooling_transition(
    data: dict[str, np.ndarray],
    idx: np.ndarray,
    k: int,
    alpha: float,
    shrinkage_strength: float,
) -> np.ndarray:
    rates, counts = estimate_column_rates(data, idx, k, alpha)
    pooled = float(np.average(rates, weights=counts + 2.0 * alpha))
    shrink = shrinkage_strength / (counts + shrinkage_strength)
    pooled_rates = (1.0 - shrink) * rates + shrink * pooled
    return transition_from_rates(pooled_rates)


def estimate_arm_specific_gate(
    data: dict[str, np.ndarray],
    idx: np.ndarray,
    k: int,
    alpha: float,
) -> np.ndarray:
    priors = np.bincount(data["G"], minlength=k).astype(float)
    priors = (priors + alpha) / (priors.sum() + alpha * k)
    corrected_means: dict[int, np.ndarray] = {}
    for arm in (0, 1):
        arm_mask = data["T"] == arm
        fallback = float(data["Y"][arm_mask].mean())
        observed = mean_by_label(data["Y"][arm_mask], data["Z"][arm_mask], k, fallback)
        arm_idx = idx[data["T"][idx] == arm]
        if len(arm_idx) < max(2, k):
            transition = estimate_global_transition(data, idx, k, alpha)
        else:
            transition = estimate_global_transition(data, arm_idx, k, alpha)
        corrected_means[arm] = correct_vector(observed, transition, priors)
    return corrected_means[1] - corrected_means[0]


def method_estimates(
    data: dict[str, np.ndarray],
    idx: np.ndarray,
    condition: Condition,
    config: dict[str, Any],
) -> dict[str, np.ndarray]:
    k = condition.k
    alpha = float(config["smoothing_alpha"])
    priors = np.bincount(data["G"], minlength=k).astype(float)
    priors = (priors + alpha) / (priors.sum() + alpha * k)
    observed_gate = gate_by_noisy_label(data, k)
    global_transition = estimate_global_transition(data, idx, k, alpha)
    per_subgroup_transition = estimate_per_subgroup_transition(data, idx, k, alpha)
    partial_transition = estimate_partial_pooling_transition(
        data,
        idx,
        k,
        alpha,
        float(config["partial_pooling_shrinkage_strength"]),
    )
    return {
        METHOD_GLOBAL: correct_vector(observed_gate, global_transition, priors),
        METHOD_ARM_SPECIFIC: estimate_arm_specific_gate(data, idx, k, alpha),
        METHOD_PER_SUBGROUP: correct_vector(observed_gate, per_subgroup_transition, priors),
        METHOD_PARTIAL_POOLING: correct_vector(observed_gate, partial_transition, priors),
    }


def metric_record(
    estimate: np.ndarray,
    truth: np.ndarray,
    true_g: np.ndarray,
) -> dict[str, float]:
    bias = estimate - truth
    ite_error = estimate[true_g] - truth[true_g]
    return {
        "gate_rmse": float(np.sqrt(np.mean(np.square(bias)))),
        "pehe": float(np.sqrt(np.mean(np.square(ite_error)))),
        "mean_subgroup_cate_bias": float(np.mean(np.abs(bias))),
    }


def run_replication(
    condition: Condition,
    config: dict[str, Any],
    replication: int,
    seed: int,
) -> list[dict[str, Any]]:
    rng = np.random.default_rng(seed + replication)
    data = simulate_dataset(condition, config, rng)
    idx = validation_sample(data, condition.expert_budget, rng)
    estimates = method_estimates(data, idx, condition, config)
    rows: list[dict[str, Any]] = []
    for method, estimate in estimates.items():
        rec = metric_record(estimate, data["tau"], data["G"])
        rows.append(
            {
                "condition_id": condition.condition_id,
                "budget_label": condition.budget_label,
                "expert_budget": condition.expert_budget,
                "n": condition.n,
                "k": condition.k,
                "misclassification_heterogeneity": condition.misclassification_heterogeneity,
                "cate_heterogeneity": condition.cate_heterogeneity,
                "correlation_direction": condition.correlation_direction,
                "replication": replication,
                "method": method,
                **rec,
            }
        )
    return rows


def bootstrap_ci(values: Iterable[float], rng: np.random.Generator, n_bootstrap: int) -> tuple[float, float]:
    arr = np.asarray(list(values), dtype=float)
    if arr.size == 0:
        return float("nan"), float("nan")
    if arr.size == 1 or n_bootstrap <= 0:
        value = float(arr.mean())
        return value, value
    idx = rng.integers(0, arr.size, size=(n_bootstrap, arr.size))
    boot = arr[idx].mean(axis=1)
    return float(np.quantile(boot, 0.025)), float(np.quantile(boot, 0.975))


def summarize(rows: list[dict[str, Any]], config: dict[str, Any], smoke: bool) -> dict[str, Any]:
    rng = np.random.default_rng(int(config["bootstrap_seed"]))
    bootstrap = int(config["bootstrap_iterations"])
    metric_keys = ["gate_rmse", "pehe", "mean_subgroup_cate_bias"]
    method_metrics: dict[str, dict[str, dict[str, dict[str, float]]]] = {}
    for budget_label in sorted({str(row["budget_label"]) for row in rows}):
        method_metrics[budget_label] = {}
        for method in METHODS:
            subset = [row for row in rows if row["budget_label"] == budget_label and row["method"] == method]
            method_metrics[budget_label][method] = {}
            for metric in metric_keys:
                values = [float(row[metric]) for row in subset]
                ci_low, ci_high = bootstrap_ci(values, rng, bootstrap)
                method_metrics[budget_label][method][metric] = {
                    "value": float(np.mean(values)) if values else float("nan"),
                    "ci_low": ci_low,
                    "ci_high": ci_high,
                }

    def paired_values(budget_label: str, left: str, right: str, metric: str) -> list[float]:
        by_key: dict[tuple[str, int], dict[str, float]] = {}
        for row in rows:
            if row["budget_label"] != budget_label:
                continue
            key = (str(row["condition_id"]), int(row["replication"]))
            by_key.setdefault(key, {})[str(row["method"])] = float(row[metric])
        return [
            vals[left] - vals[right]
            for vals in by_key.values()
            if left in vals and right in vals
        ]

    comparisons: dict[str, dict[str, float]] = {}
    low_label = str(config["low_budget_label"])
    diff_pg = paired_values(low_label, METHOD_PARTIAL_POOLING, METHOD_GLOBAL, "gate_rmse")
    diff_pi = paired_values(low_label, METHOD_PARTIAL_POOLING, METHOD_PER_SUBGROUP, "gate_rmse")
    per_subgroup_values = [
        float(row["gate_rmse"])
        for row in rows
        if row["budget_label"] == low_label and row["method"] == METHOD_PER_SUBGROUP
    ]
    rel_margin = float(config["noninferiority_relative_margin"])
    rel_diff = [
        diff / max(base, 1e-12)
        for diff, base in zip(diff_pi, per_subgroup_values, strict=False)
    ]
    for key, values in [
        ("low_budget.partial_pooling_minus_global_gate_rmse", diff_pg),
        ("low_budget.partial_pooling_minus_per_subgroup_gate_rmse", diff_pi),
        ("low_budget.partial_pooling_relative_to_per_subgroup_gate_rmse", rel_diff),
    ]:
        ci_low, ci_high = bootstrap_ci(values, rng, bootstrap)
        comparisons[key] = {
            "value": float(np.mean(values)) if values else float("nan"),
            "ci_low": ci_low,
            "ci_high": ci_high,
        }
    formal_success = (
        comparisons["low_budget.partial_pooling_minus_global_gate_rmse"]["ci_high"] < 0.0
        and comparisons["low_budget.partial_pooling_relative_to_per_subgroup_gate_rmse"]["ci_high"]
        <= rel_margin
    )
    return {
        "exp_id": EXP_ID,
        "plan_id": PLAN_ID,
        "smoke": smoke,
        "conclusion": "smoke_only_no_formal_conclusion" if smoke else ("success" if formal_success else "negative"),
        "primary_metric": "gate_rmse",
        "secondary_diagnostics": ["pehe", "mean_subgroup_cate_bias"],
        "n_conditions": len({str(row["condition_id"]) for row in rows}),
        "n_replications": len({(str(row["condition_id"]), int(row["replication"])) for row in rows}),
        "methods": METHODS,
        "method_metrics": method_metrics,
        "comparisons": comparisons,
        "operational_criteria": config["operational_criteria"],
        "noninferiority_relative_margin": rel_margin,
    }


def matrix_row(
    target_id: str,
    row: str,
    col: str,
    metric_key: str,
    source: str,
    value: Any,
) -> dict[str, Any]:
    return {
        "target_id": target_id,
        "row": row,
        "col": col,
        "metric_key": metric_key,
        "exp_id": EXP_ID,
        "source": source,
        "value": value,
    }


def write_matrix_metrics(summary: dict[str, Any], output_dir: Path) -> list[dict[str, Any]]:
    source = str(output_dir / "metrics.csv")
    comparisons = summary["comparisons"]
    methods = summary["method_metrics"]
    rows = [
        matrix_row(
            CLAIM_ID,
            "low_budget",
            "partial_pooling_vs_global",
            "low_budget.partial_pooling_minus_global_gate_rmse",
            source,
            comparisons["low_budget.partial_pooling_minus_global_gate_rmse"],
        ),
        matrix_row(
            CLAIM_ID,
            "low_budget",
            "partial_pooling_vs_per_subgroup",
            "low_budget.partial_pooling_minus_per_subgroup_gate_rmse",
            source,
            {
                "absolute": comparisons["low_budget.partial_pooling_minus_per_subgroup_gate_rmse"],
                "relative": comparisons[
                    "low_budget.partial_pooling_relative_to_per_subgroup_gate_rmse"
                ],
                "noninferiority_margin": summary["noninferiority_relative_margin"],
            },
        ),
        matrix_row(
            CLAIM_ID,
            "low_budget",
            "secondary_pehe_bias_diagnostics",
            "low_budget.partial_pooling_secondary_diagnostics",
            source,
            {
                "pehe": methods.get("low", {}).get(METHOD_PARTIAL_POOLING, {}).get("pehe"),
                "mean_subgroup_cate_bias": methods.get("low", {})
                .get(METHOD_PARTIAL_POOLING, {})
                .get("mean_subgroup_cate_bias"),
            },
        ),
    ]
    for budget_label in ["low", "mid"]:
        if budget_label not in methods:
            continue
        for method in METHODS:
            rows.append(
                matrix_row(
                    TABLE_ID,
                    f"budget_{budget_label}",
                    method,
                    f"budget_{budget_label}.{method}.gate_rmse",
                    source,
                    methods[budget_label][method]["gate_rmse"],
                )
            )
    path = output_dir / "matrix_metrics.jsonl"
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: Any) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def main() -> None:
    args = parse_args()
    start = time.time()
    config = load_config(args.config)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    replications = int(config["replications_per_condition"])
    if args.max_replications is not None:
        replications = min(replications, args.max_replications)
    if not args.smoke and not args.allow_formal:
        raise RuntimeError("formal execution is disabled without --allow-formal")
    if (
        not args.smoke
        and bool(config.get("requires_exp002_done", True))
        and not args.confirm_exp002_done
    ):
        raise RuntimeError("formal execution requires --confirm-exp002-done")
    if not args.smoke and replications < int(config["minimum_formal_replications"]):
        raise ValueError("formal Stage1 run requires at least minimum_formal_replications")

    conditions = condition_grid(config)
    if args.limit_conditions is not None:
        conditions = balanced_limit_conditions(conditions, args.limit_conditions)

    rows: list[dict[str, Any]] = []
    seed = int(config["seed"])
    for condition_index, condition in enumerate(conditions):
        for replication in range(replications):
            rows.extend(
                run_replication(
                    condition,
                    config,
                    replication=replication,
                    seed=seed + condition_index * 100_000,
                )
            )

    summary = summarize(rows, config, bool(args.smoke))
    summary["elapsed_seconds"] = round(time.time() - start, 3)
    summary["replications_per_condition"] = replications
    summary["output_contract"] = config["output_contract"]
    summary["matrix_metric_path"] = str(output_dir / "matrix_metrics.jsonl")
    write_csv(output_dir / "metrics.csv", rows)
    write_json(output_dir / "summary.json", summary)
    matrix_rows = write_matrix_metrics(summary, output_dir)
    write_json(
        output_dir / "run_config.json",
        {"args": vars(args), "config": config, "conditions": [c.__dict__ for c in conditions]},
    )
    print(
        json.dumps(
            {
                "exp_id": EXP_ID,
                "smoke": bool(args.smoke),
                "conclusion": summary["conclusion"],
                "conditions": len(conditions),
                "replications_per_condition": replications,
                "methods": METHODS,
                "matrix_rows": len(matrix_rows),
                "summary": str(output_dir / "summary.json"),
                "matrix_metrics": str(output_dir / "matrix_metrics.jsonl"),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
