#!/usr/bin/env python3
"""GPU-vectorized DGP grid for EC-HTE H1.

This script is designed to support a pending-only proposal and a short dry run.
The formal run must wait for Director approval and GPU allocation.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torch


EXP_ID = "exp_002_gpu_dgp_grid"


@dataclass(frozen=True)
class Condition:
    condition_id: str
    correlation_direction: str
    misclassification_heterogeneity: str
    cate_heterogeneity: str
    k: int
    n: int
    expert_budget: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--device", default="cuda", choices=["cuda", "cpu"])
    parser.add_argument("--max-replications", type=int, default=None)
    parser.add_argument("--limit-conditions", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def load_config(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def condition_grid(config: dict[str, Any]) -> list[Condition]:
    conditions: list[Condition] = []
    keys = [
        config["misclassification_heterogeneity"],
        config["cate_heterogeneity"],
        config["subgroup_counts"],
        config["n_values"],
        config["expert_budgets"],
        config["correlation_directions"],
    ]
    for mis_h, cate_h, k, n, budget, direction in itertools.product(*keys):
        condition_id = (
            f"corr={direction}|mis={mis_h}|cate={cate_h}|k={k}|"
            f"N={n}|B={budget}"
        )
        conditions.append(
            Condition(
                condition_id=condition_id,
                correlation_direction=direction,
                misclassification_heterogeneity=mis_h,
                cate_heterogeneity=cate_h,
                k=int(k),
                n=int(n),
                expert_budget=int(budget),
            )
        )
    return conditions


def evenly_spaced(items: list[Condition], count: int) -> list[Condition]:
    if count <= 0:
        return []
    if count >= len(items):
        return items
    if count == 1:
        return [items[0]]
    step = (len(items) - 1) / (count - 1)
    return [items[int(round(i * step))] for i in range(count)]


def balanced_limit_conditions(conditions: list[Condition], limit: int) -> list[Condition]:
    positives = [c for c in conditions if c.correlation_direction == "positive"]
    negatives = [c for c in conditions if c.correlation_direction == "negative"]
    pos_count = (limit + 1) // 2
    neg_count = limit // 2
    selected = evenly_spaced(positives, pos_count) + evenly_spaced(negatives, neg_count)
    return selected[:limit]


def cate_values(k: int, heterogeneity: str, device: torch.device) -> torch.Tensor:
    if heterogeneity == "high":
        vals = torch.linspace(0.15, 1.15, k, device=device)
    else:
        vals = torch.linspace(0.35, 0.65, k, device=device)
    return vals - vals.mean() + 0.5


def error_rates(
    k: int,
    mis_heterogeneity: str,
    cate: torch.Tensor,
    direction: str,
    device: torch.device,
) -> torch.Tensor:
    if mis_heterogeneity == "high":
        low, high = 0.04, 0.36
    else:
        low, high = 0.10, 0.18
    ordered = torch.linspace(low, high, k, device=device)
    order = torch.argsort(torch.abs(cate), descending=False)
    rates = torch.empty(k, device=device)
    if direction == "positive":
        rates[order] = ordered
    else:
        rates[order] = torch.flip(ordered, dims=[0])
    return rates


def transition_matrix_from_rates(rates: torch.Tensor) -> torch.Tensor:
    k = int(rates.numel())
    matrix = torch.zeros((k, k), device=rates.device)
    off_diag = rates / max(k - 1, 1)
    matrix[:] = off_diag[:, None]
    diag_idx = torch.arange(k, device=rates.device)
    matrix[diag_idx, diag_idx] = 1.0 - rates
    return matrix


def global_transition_matrix(p_error: torch.Tensor, k: int, device: torch.device) -> torch.Tensor:
    rates = torch.full((k,), p_error.clamp(0.0, 0.95), device=device)
    return transition_matrix_from_rates(rates)


def sample_noisy_labels(z_true: torch.Tensor, rates: torch.Tensor) -> torch.Tensor:
    k = int(rates.numel())
    device = z_true.device
    error = torch.rand_like(z_true.float()) < rates[z_true]
    shift = torch.randint(1, k, z_true.shape, device=device)
    z_alt = (z_true + shift) % k
    return torch.where(error, z_alt, z_true)


def observed_gate(y: torch.Tensor, treatment: torch.Tensor, labels: torch.Tensor, k: int) -> torch.Tensor:
    estimates = []
    for group in range(k):
        mask = labels == group
        treated = mask & (treatment == 1)
        control = mask & (treatment == 0)
        if treated.any() and control.any():
            estimates.append(y[treated].mean() - y[control].mean())
        else:
            estimates.append(torch.tensor(float("nan"), device=y.device))
    out = torch.stack(estimates)
    if torch.isnan(out).any():
        global_ate = y[treatment == 1].mean() - y[treatment == 0].mean()
        out = torch.where(torch.isnan(out), global_ate, out)
    return out


def correct_gate(observed: torch.Tensor, transition: torch.Tensor, ridge: float) -> torch.Tensor:
    k = transition.shape[0]
    lhs = transition.T + ridge * torch.eye(k, device=transition.device)
    return torch.linalg.solve(lhs, observed)


def gate_rmse(estimate: torch.Tensor, truth: torch.Tensor) -> torch.Tensor:
    return torch.sqrt(torch.mean((estimate - truth) ** 2))


def bias_bound_score(rates: torch.Tensor, cate: torch.Tensor) -> torch.Tensor:
    centered_rate = rates - rates.mean()
    centered_cate = torch.abs(cate) - torch.abs(cate).mean()
    return torch.mean(torch.abs(centered_rate * centered_cate))


def rankdata(values: torch.Tensor) -> torch.Tensor:
    order = torch.argsort(values)
    ranks = torch.empty_like(values, dtype=torch.float32)
    ranks[order] = torch.arange(values.numel(), device=values.device, dtype=torch.float32)
    return ranks


def spearman(x: torch.Tensor, y: torch.Tensor) -> float:
    if x.numel() < 2 or torch.std(x) == 0 or torch.std(y) == 0:
        return float("nan")
    rx = rankdata(x.float())
    ry = rankdata(y.float())
    rx = rx - rx.mean()
    ry = ry - ry.mean()
    denom = torch.sqrt(torch.sum(rx**2) * torch.sum(ry**2))
    if denom == 0:
        return float("nan")
    return float(torch.sum(rx * ry) / denom)


def quantile(values: list[float], q: float) -> float:
    if not values:
        return float("nan")
    sorted_values = sorted(values)
    idx = min(max(int(math.floor(q * (len(sorted_values) - 1))), 0), len(sorted_values) - 1)
    return float(sorted_values[idx])


def bootstrap_metrics(
    condition_rows: list[dict[str, Any]],
    iterations: int,
    seed: int,
    device: torch.device,
) -> dict[str, float]:
    pos = [r for r in condition_rows if r["correlation_direction"] == "positive"]
    neg = [r for r in condition_rows if r["correlation_direction"] == "negative"]
    if not pos or not neg:
        return {
            "primary_ci_lower": float("nan"),
            "primary_ci_upper": float("nan"),
            "spearman_ci_lower": float("nan"),
            "spearman_ci_upper": float("nan"),
        }

    generator = torch.Generator(device=device)
    generator.manual_seed(seed)
    primary_samples: list[float] = []
    spearman_samples: list[float] = []
    rows = condition_rows
    for _ in range(iterations):
        pos_idx = torch.randint(0, len(pos), (len(pos),), generator=generator, device=device)
        neg_idx = torch.randint(0, len(neg), (len(neg),), generator=generator, device=device)
        row_idx = torch.randint(0, len(rows), (len(rows),), generator=generator, device=device)
        pos_rate = torch.tensor(
            [pos[int(i)]["oracle_global_worse_rate"] for i in pos_idx],
            device=device,
        ).mean()
        neg_rate = torch.tensor(
            [neg[int(i)]["oracle_global_worse_rate"] for i in neg_idx],
            device=device,
        ).mean()
        primary_samples.append(float(pos_rate - neg_rate))
        x = torch.tensor([rows[int(i)]["bias_bound_score"] for i in row_idx], device=device)
        y = torch.tensor([rows[int(i)]["oracle_global_worse_rate"] for i in row_idx], device=device)
        rho = spearman(x, y)
        if not math.isnan(rho):
            spearman_samples.append(rho)

    return {
        "primary_ci_lower": quantile(primary_samples, 0.025),
        "primary_ci_upper": quantile(primary_samples, 0.975),
        "spearman_ci_lower": quantile(spearman_samples, 0.025),
        "spearman_ci_upper": quantile(spearman_samples, 0.975),
    }


def run_condition(
    condition: Condition,
    replications: int,
    config: dict[str, Any],
    device: torch.device,
    seed: int,
) -> dict[str, Any]:
    torch.manual_seed(seed)
    k = condition.k
    n = condition.n
    budget = min(condition.expert_budget, n)
    ridge = float(config["global_correction_ridge"])
    cate = cate_values(k, condition.cate_heterogeneity, device)
    rates = error_rates(
        k,
        condition.misclassification_heterogeneity,
        cate,
        condition.correlation_direction,
        device,
    )
    subgroup_transition = transition_matrix_from_rates(rates)
    oracle_global_transition = global_transition_matrix(rates.mean(), k, device)
    true_gate = cate
    metrics = {
        "uncorrected_gate_rmse": [],
        "oracle_global_gate_rmse": [],
        "estimated_global_gate_rmse": [],
        "stratified_subgroup_gate_rmse": [],
        "oracle_global_worse": [],
        "estimated_global_minus_oracle_global_gate_rmse": [],
    }

    for _ in range(replications):
        z_true = torch.randint(0, k, (n,), device=device)
        z_noisy = sample_noisy_labels(z_true, rates)
        treatment = (
            torch.rand(n, device=device) < float(config["treatment_probability"])
        ).long()
        y = (
            0.2
            + true_gate[z_true] * treatment.float()
            + torch.randn(n, device=device) * float(config["noise_sd"])
        )
        obs_gate = observed_gate(y, treatment, z_noisy, k)
        uncorrected = obs_gate
        oracle_global = correct_gate(obs_gate, oracle_global_transition, ridge)

        validation_idx = torch.randperm(n, device=device)[:budget]
        estimated_error = (z_true[validation_idx] != z_noisy[validation_idx]).float().mean()
        estimated_global_transition = global_transition_matrix(estimated_error, k, device)
        estimated_global = correct_gate(obs_gate, estimated_global_transition, ridge)
        stratified_subgroup = correct_gate(obs_gate, subgroup_transition, ridge)

        uncorrected_rmse = gate_rmse(uncorrected, true_gate)
        oracle_global_rmse = gate_rmse(oracle_global, true_gate)
        estimated_global_rmse = gate_rmse(estimated_global, true_gate)
        stratified_rmse = gate_rmse(stratified_subgroup, true_gate)

        metrics["uncorrected_gate_rmse"].append(uncorrected_rmse)
        metrics["oracle_global_gate_rmse"].append(oracle_global_rmse)
        metrics["estimated_global_gate_rmse"].append(estimated_global_rmse)
        metrics["stratified_subgroup_gate_rmse"].append(stratified_rmse)
        metrics["oracle_global_worse"].append((oracle_global_rmse > uncorrected_rmse).float())
        metrics["estimated_global_minus_oracle_global_gate_rmse"].append(
            estimated_global_rmse - oracle_global_rmse
        )

    reduced = {key: float(torch.stack(vals).mean()) for key, vals in metrics.items()}
    reduced["oracle_global_worse_rate"] = reduced.pop("oracle_global_worse")
    reduced.update(
        {
            "condition_id": condition.condition_id,
            "correlation_direction": condition.correlation_direction,
            "misclassification_heterogeneity": condition.misclassification_heterogeneity,
            "cate_heterogeneity": condition.cate_heterogeneity,
            "k": condition.k,
            "n": condition.n,
            "expert_budget": condition.expert_budget,
            "replications": replications,
            "bias_bound_score": float(bias_bound_score(rates, cate)),
        }
    )
    return reduced


def planned_metrics(
    config: dict[str, Any],
    condition_rows: list[dict[str, Any]],
    output_dir: Path,
    device: torch.device,
) -> list[dict[str, Any]]:
    pos = [r["oracle_global_worse_rate"] for r in condition_rows if r["correlation_direction"] == "positive"]
    neg = [r["oracle_global_worse_rate"] for r in condition_rows if r["correlation_direction"] == "negative"]
    primary = float(torch.tensor(pos, device=device).mean() - torch.tensor(neg, device=device).mean()) if pos and neg else float("nan")
    x = torch.tensor([r["bias_bound_score"] for r in condition_rows], device=device)
    y = torch.tensor([r["oracle_global_worse_rate"] for r in condition_rows], device=device)
    rho = spearman(x, y)
    gap = float(
        torch.tensor(
            [r["estimated_global_minus_oracle_global_gate_rmse"] for r in condition_rows],
            device=device,
        ).mean()
    )
    cis = bootstrap_metrics(
        condition_rows,
        int(config["bootstrap_iterations"]),
        int(config["bootstrap_seed"]),
        device,
    )
    source = str(output_dir / "condition_metrics.jsonl")
    return [
        {
            "target_id": "C_H1_GLOBAL_CORRECTION_WORSE",
            "row": "exp_002_gpu_dgp_grid",
            "col": "grid_oracle_vs_estimated_mechanism_split",
            "metric_key": "bias_bound_predicts_global_worse_rate_by_correction_type",
            "exp_id": EXP_ID,
            "source": source,
            "value": {
                "global_worse_rate_difference_positive_minus_negative": primary,
                "bootstrap_95_ci": [cis["primary_ci_lower"], cis["primary_ci_upper"]],
                "oracle_global_reported_separately": True,
                "estimated_global_reported_separately": True,
            },
        },
        {
            "target_id": "T_STAGE0_DGP_GRID",
            "row": "grid_all_conditions",
            "col": "bias_bound_auc_or_rank_corr",
            "metric_key": "bias_bound_vs_global_worse_rank_corr",
            "exp_id": EXP_ID,
            "source": source,
            "value": {
                "bias_bound_vs_global_worse_spearman": rho,
                "bootstrap_95_ci": [cis["spearman_ci_lower"], cis["spearman_ci_upper"]],
            },
        },
        {
            "target_id": "T_STAGE0_DGP_GRID",
            "row": "grid_all_conditions",
            "col": "oracle_estimated_gap",
            "metric_key": "estimated_global_minus_oracle_global_gate_rmse",
            "exp_id": EXP_ID,
            "source": source,
            "value": gap,
        },
    ]


def write_json(path: Path, payload: Any) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def main() -> None:
    args = parse_args()
    start = time.time()
    config = load_config(args.config)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but torch.cuda.is_available() is false")
    device = torch.device(args.device)
    conditions = condition_grid(config)
    if args.limit_conditions is not None:
        conditions = balanced_limit_conditions(conditions, args.limit_conditions)
    replications = int(config["replications_per_condition"])
    if args.max_replications is not None:
        replications = min(replications, args.max_replications)

    condition_rows = []
    for idx, condition in enumerate(conditions):
        row = run_condition(
            condition,
            replications,
            config,
            device,
            seed=int(config["seed"]) + idx,
        )
        condition_rows.append(row)

    metrics_path = output_dir / "condition_metrics.jsonl"
    with open(metrics_path, "w", encoding="utf-8") as handle:
        for row in condition_rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")

    planned = planned_metrics(config, condition_rows, output_dir, device)
    write_json(output_dir / "planned_metrics.json", planned)
    summary = {
        "exp_id": EXP_ID,
        "dry_run": bool(args.dry_run),
        "device": str(device),
        "torch": torch.__version__,
        "cuda_available": torch.cuda.is_available(),
        "cuda_version": torch.version.cuda,
        "conditions": len(condition_rows),
        "replications_per_condition": replications,
        "elapsed_seconds": round(time.time() - start, 3),
        "methods": config["methods"],
        "primary_metric": config["output_contract"]["primary_metric"],
        "secondary_metrics": config["output_contract"]["secondary_metrics"],
        "planned_metric_paths": {
            "condition_metrics": str(metrics_path),
            "planned_metrics": str(output_dir / "planned_metrics.json"),
        },
        "operational_criteria": config["operational_criteria"],
    }
    write_json(output_dir / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
