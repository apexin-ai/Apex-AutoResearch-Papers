"""CPU-only semi-synthetic MVP for EC-HTE.

This script simulates a categorical effect modifier whose LLM-observed label is
misclassified at group-dependent rates. It compares three CATE/GATE estimators:
uncorrected observed-label grouping, pooled/global confusion correction, and
subgroup-specific EC-HTE-lite confusion correction.

Inputs are CLI parameters controlling sample size, replications, expert-label
budget, and random seed. Outputs are JSON/CSV summaries plus the exact config
and command needed to reproduce the run.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone

import numpy as np


Z975 = 1.959963984540054


@dataclass
class Scenario:
    name: str
    error_rates: list[float]
    true_cate: list[float]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run EC-HTE semi-synthetic MVP.")
    parser.add_argument("--reps", type=int, default=10)
    parser.add_argument("--n", type=int, default=5000)
    parser.add_argument("--budget", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260531)
    parser.add_argument("--out-dir", required=True)
    return parser.parse_args()


def confusion_from_error_rates(error_rates: np.ndarray) -> np.ndarray:
    """Build P(observed_label | true_group) with errors split over other groups."""
    k = len(error_rates)
    c = np.zeros((k, k), dtype=float)
    for g, err in enumerate(error_rates):
        c[g, :] = err / (k - 1)
        c[g, g] = 1.0 - err
    return c


def sample_observed_labels(rng: np.random.Generator, true_groups: np.ndarray, c: np.ndarray) -> np.ndarray:
    observed = np.empty_like(true_groups)
    for g in range(c.shape[0]):
        idx = np.flatnonzero(true_groups == g)
        if idx.size:
            observed[idx] = rng.choice(c.shape[1], size=idx.size, p=c[g])
    return observed


def estimate_observed_cate(y: np.ndarray, t: np.ndarray, z: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray]:
    """Estimate label-conditional treatment effects and diagonal sampling variance."""
    tau = np.zeros(k, dtype=float)
    var = np.zeros(k, dtype=float)
    for label in range(k):
        mask = z == label
        treated = mask & (t == 1)
        control = mask & (t == 0)
        if treated.sum() < 2 or control.sum() < 2:
            tau[label] = np.nan
            var[label] = np.inf
            continue
        y1 = y[treated]
        y0 = y[control]
        tau[label] = float(y1.mean() - y0.mean())
        var[label] = float(y1.var(ddof=1) / y1.size + y0.var(ddof=1) / y0.size)
    return tau, var


def estimate_confusion_from_expert(
    true_groups: np.ndarray,
    observed: np.ndarray,
    budget: int,
    rng: np.random.Generator,
    k: int,
    alpha: float = 1.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Estimate group proportions and row-specific confusion from expert labels."""
    idx = rng.choice(true_groups.size, size=min(budget, true_groups.size), replace=False)
    counts_g = np.bincount(true_groups[idx], minlength=k).astype(float)
    pi_hat = (counts_g + alpha) / (counts_g.sum() + alpha * k)
    counts = np.full((k, k), alpha, dtype=float)
    for g, z in zip(true_groups[idx], observed[idx]):
        counts[g, z] += 1.0
    c_hat = counts / counts.sum(axis=1, keepdims=True)
    return pi_hat, c_hat


def posterior_true_given_observed(pi: np.ndarray, c: np.ndarray) -> np.ndarray:
    """Convert P(Z|G) and P(G) into B[g,z] = P(G=g|Z=z)."""
    joint = pi[:, None] * c
    denom = joint.sum(axis=0, keepdims=True)
    return joint / np.maximum(denom, 1e-12)


def corrected_estimate(observed_tau: np.ndarray, observed_var: np.ndarray, pi: np.ndarray, c: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Invert observed-label CATE mixing to recover true-group CATE estimates."""
    b = posterior_true_given_observed(pi, c)
    # Solve observed_tau ~= B.T @ true_tau. A tiny ridge prevents singular smoke-test failures.
    m = b.T
    ridge = 1e-6 * np.eye(m.shape[0])
    a = np.linalg.inv(m + ridge)
    tau = a @ observed_tau
    cov_obs = np.diag(observed_var)
    cov = a @ cov_obs @ a.T
    se = np.sqrt(np.maximum(np.diag(cov), 0.0))
    return tau, se


def global_confusion_from_expert(pi_hat: np.ndarray, c_hat: np.ndarray) -> np.ndarray:
    """Build a pooled symmetric global correction that ignores row heterogeneity."""
    k = c_hat.shape[0]
    pooled_error = float(np.sum(pi_hat[:, None] * c_hat * (1.0 - np.eye(k))))
    c_global = np.full((k, k), pooled_error / (k - 1), dtype=float)
    np.fill_diagonal(c_global, 1.0 - pooled_error)
    return c_global


def summarize_method(rows: list[dict], method: str, true_cate: np.ndarray) -> dict:
    vals = [r for r in rows if r["method"] == method]
    est = np.array([v["estimate"] for v in vals], dtype=float)
    err = est - true_cate[None, :]
    return {
        "method": method,
        "pehe_mean": float(np.mean(np.sqrt(np.mean(err**2, axis=1)))),
        "gate_bias_mean": float(np.mean(np.abs(err))),
        "gate_rmse_mean": float(np.sqrt(np.mean(err**2))),
        "coverage_mean": float(np.mean([v["coverage"] for v in vals])),
        "ci_width_mean": float(np.mean([v["ci_width"] for v in vals])),
        "subgroup_cate_bias_mean": [float(x) for x in np.mean(np.abs(err), axis=0)],
    }


def run_scenario(args: argparse.Namespace, scenario: Scenario, rng: np.random.Generator) -> dict:
    k = 3
    pi = np.array([0.34, 0.33, 0.33], dtype=float)
    true_cate = np.array(scenario.true_cate, dtype=float)
    true_c = confusion_from_error_rates(np.array(scenario.error_rates, dtype=float))
    rep_rows = []

    for rep in range(args.reps):
        g = rng.choice(k, size=args.n, p=pi)
        t = rng.binomial(1, 0.5, size=args.n)
        y = true_cate[g] * t + rng.normal(0.0, 1.0, size=args.n)
        z = sample_observed_labels(rng, g, true_c)

        observed_tau, observed_var = estimate_observed_cate(y, t, z, k)
        if np.any(~np.isfinite(observed_tau)):
            raise RuntimeError("Observed-label cell too small; increase n.")

        pi_hat, c_hat = estimate_confusion_from_expert(g, z, args.budget, rng, k)
        c_global = global_confusion_from_expert(pi_hat, c_hat)

        methods = {
            "uncorrected": (observed_tau, np.sqrt(observed_var)),
            "global_correction": corrected_estimate(observed_tau, observed_var, pi_hat, c_global),
            "subgroup_ec_hte_lite": corrected_estimate(observed_tau, observed_var, pi_hat, c_hat),
        }
        for method, (est, se) in methods.items():
            lower = est - Z975 * se
            upper = est + Z975 * se
            rep_rows.append(
                {
                    "scenario": scenario.name,
                    "rep": rep,
                    "method": method,
                    "estimate": [float(x) for x in est],
                    "coverage": float(np.mean((lower <= true_cate) & (true_cate <= upper))),
                    "ci_width": float(np.mean(2.0 * Z975 * se)),
                }
            )

    summaries = [summarize_method(rep_rows, m, true_cate) for m in ["uncorrected", "global_correction", "subgroup_ec_hte_lite"]]
    return {"scenario": asdict(scenario), "summaries": summaries, "rep_rows": rep_rows}


def pass_fail(results: list[dict]) -> dict:
    by_name = {r["scenario"]["name"]: {s["method"]: s for s in r["summaries"]} for r in results}
    pos = by_name["positive_worst_case"]
    sanity = by_name["negative_sanity_case"]
    global_worse_than_uncorrected = (
        pos["global_correction"]["pehe_mean"] > pos["uncorrected"]["pehe_mean"]
        or pos["global_correction"]["gate_bias_mean"] > pos["uncorrected"]["gate_bias_mean"]
    )
    improvement = (
        pos["global_correction"]["pehe_mean"] - pos["subgroup_ec_hte_lite"]["pehe_mean"]
    ) / max(pos["global_correction"]["pehe_mean"], 1e-12)
    coverage_gain = abs(pos["global_correction"]["coverage_mean"] - 0.95) - abs(
        pos["subgroup_ec_hte_lite"]["coverage_mean"] - 0.95
    )
    sanity_degradation = (
        sanity["subgroup_ec_hte_lite"]["pehe_mean"]
        / max(min(s["pehe_mean"] for s in sanity.values()), 1e-12)
        - 1.0
    )
    passed = bool(global_worse_than_uncorrected and (improvement >= 0.20 or coverage_gain > 0.0) and sanity_degradation < 0.10)
    return {
        "passed": passed,
        "global_worse_than_uncorrected_positive": bool(global_worse_than_uncorrected),
        "subgroup_pehe_improvement_vs_global_positive": float(improvement),
        "subgroup_coverage_gain_toward_095_positive": float(coverage_gain),
        "sanity_subgroup_pehe_degradation_vs_best": float(sanity_degradation),
    }


def write_outputs(args: argparse.Namespace, payload: dict) -> None:
    os.makedirs(args.out_dir, exist_ok=True)
    with open(os.path.join(args.out_dir, "results.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    rows = []
    for result in payload["results"]:
        for summary in result["summaries"]:
            row = {"scenario": result["scenario"]["name"], **summary}
            row["subgroup_cate_bias_mean"] = json.dumps(row["subgroup_cate_bias_mean"])
            rows.append(row)
    with open(os.path.join(args.out_dir, "summary.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    with open(os.path.join(args.out_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump(payload["config"], f, indent=2, ensure_ascii=False)


def main() -> int:
    args = parse_args()
    rng = np.random.default_rng(args.seed)
    scenarios = [
        Scenario("positive_worst_case", [0.30, 0.15, 0.05], [0.50, 0.25, 0.05]),
        Scenario("negative_sanity_case", [0.05, 0.15, 0.30], [0.50, 0.25, 0.05]),
    ]
    results = [run_scenario(args, scenario, rng) for scenario in scenarios]
    config = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "command": " ".join(sys.argv),
        "seed": args.seed,
        "n": args.n,
        "reps": args.reps,
        "budget": args.budget,
        "dependency_policy": "numpy-only CPU run; no GPU and no scipy/sklearn required",
    }
    payload = {"config": config, "results": results, "pass_fail": pass_fail(results)}
    write_outputs(args, payload)
    print(json.dumps({"out_dir": args.out_dir, "pass_fail": payload["pass_fail"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
