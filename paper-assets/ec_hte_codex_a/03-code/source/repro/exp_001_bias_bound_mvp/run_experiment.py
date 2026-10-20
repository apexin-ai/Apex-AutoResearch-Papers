"""CPU-only MVP for exp_001_bias_bound_mvp.

This implements the latest plan_001_h1_cpu_mvp contract:
- primary metric: gate_rmse only
- required controls: uncorrected, oracle global, estimated global, stratified
- matrix/provenance JSON lines for the required cells
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


EXP_ID = "exp_001_bias_bound_mvp"
CLAIM_ID = "C_H1_GLOBAL_CORRECTION_WORSE"
GRID_ID = "T_STAGE0_DGP_GRID"
GRID_ROW = "positive_corr_high_mis_high_cate"
SCENARIO_KEY = "positive_corr_high_high"

METHOD_UNCORRECTED = "uncorrected"
METHOD_ORACLE_GLOBAL = "oracle_global_confusion_correction"
METHOD_ESTIMATED_GLOBAL = "estimated_global_confusion_correction"
METHOD_STRATIFIED = "stratified_subgroup_correction"
METHODS = [
    METHOD_UNCORRECTED,
    METHOD_ORACLE_GLOBAL,
    METHOD_ESTIMATED_GLOBAL,
    METHOD_STRATIFIED,
]


@dataclass(frozen=True)
class DGPConfig:
    """Semi-synthetic positive-correlation worst-case DGP."""

    name: str
    tau_values: tuple[float, ...]
    error_rates: tuple[float, ...]
    group_probs: tuple[float, ...]
    outcome_sd: float


def positive_corr_high_high_config() -> DGPConfig:
    # Tuned to expose under/over-correction from one pooled error rate:
    # error rate and CATE magnitude are positively correlated, but pooled
    # correction over-corrects the high-CATE groups relative to uncorrected Z.
    return DGPConfig(
        name=SCENARIO_KEY,
        tau_values=(0.0, 4.3, 5.4, 5.5),
        error_rates=(0.02, 0.06, 0.29, 0.45),
        group_probs=(0.59, 0.09, 0.14, 0.18),
        outcome_sd=1.0,
    )


def make_confusion_matrix(error_rates: np.ndarray) -> np.ndarray:
    """Return C[z, g] = P(Z=z | G=g) with uniform off-diagonal errors."""

    k = len(error_rates)
    if np.any(error_rates < 0) or np.any(error_rates >= (k - 1) / k):
        raise ValueError("error rates must be in [0, (k - 1) / k)")
    confusion = np.zeros((k, k), dtype=float)
    for g, error in enumerate(error_rates):
        confusion[:, g] = error / (k - 1)
        confusion[g, g] = 1.0 - error
    return confusion


def global_confusion_from_pooled_error(
    error_rates: np.ndarray, group_probs: np.ndarray
) -> np.ndarray:
    """Return the oracle pooled/global confusion model used for global correction."""

    pooled_error = float(np.dot(error_rates, group_probs))
    k = len(error_rates)
    pooled_error = float(np.clip(pooled_error, 0.0, 0.98 * (k - 1) / k))
    confusion = np.full((k, k), pooled_error / (k - 1), dtype=float)
    np.fill_diagonal(confusion, 1.0 - pooled_error)
    return confusion


def posterior_true_given_noisy(
    confusion: np.ndarray, group_probs: np.ndarray
) -> np.ndarray:
    """Return W[z, g] = P(G=g | Z=z)."""

    noisy_probs = confusion @ group_probs
    if np.any(noisy_probs <= 0):
        raise ValueError("invalid noisy-label probabilities")
    return confusion * group_probs[None, :] / noisy_probs[:, None]


def corrected_gate(observed_gate_z: np.ndarray, posterior_w: np.ndarray) -> np.ndarray:
    """Invert tau_Z = W tau_G via a stable pseudo-inverse."""

    return np.linalg.pinv(posterior_w, rcond=1e-10) @ observed_gate_z


def simulate_dataset(config: DGPConfig, n: int, rng: np.random.Generator) -> dict[str, np.ndarray]:
    tau = np.asarray(config.tau_values, dtype=float)
    probs = np.asarray(config.group_probs, dtype=float)
    errors = np.asarray(config.error_rates, dtype=float)
    k = len(tau)
    true_g = rng.choice(k, size=n, p=probs)
    treatment = rng.binomial(1, 0.5, size=n)
    baseline = 0.35 * true_g + 0.25 * np.sin(true_g)
    outcome = baseline + tau[true_g] * treatment + rng.normal(0.0, config.outcome_sd, n)

    confusion = make_confusion_matrix(errors)
    noisy_z = np.empty(n, dtype=int)
    for g in range(k):
        mask = true_g == g
        noisy_z[mask] = rng.choice(k, size=int(mask.sum()), p=confusion[:, g])

    return {"G": true_g, "Z": noisy_z, "T": treatment, "Y": outcome}


def gate_by_label(
    labels: np.ndarray, treatment: np.ndarray, outcome: np.ndarray, k: int
) -> np.ndarray:
    estimates = np.empty(k, dtype=float)
    for label in range(k):
        treated = (labels == label) & (treatment == 1)
        control = (labels == label) & (treatment == 0)
        if treated.sum() == 0 or control.sum() == 0:
            estimates[label] = np.nan
        else:
            estimates[label] = outcome[treated].mean() - outcome[control].mean()
    if np.any(np.isnan(estimates)):
        fill = float(np.nanmean(estimates))
        estimates = np.nan_to_num(estimates, nan=fill)
    return estimates


def estimate_global_confusion(
    true_g: np.ndarray,
    noisy_z: np.ndarray,
    k: int,
    budget: int,
    rng: np.random.Generator,
    alpha: float,
) -> np.ndarray:
    """Estimate a pooled symmetric global confusion from an expert-label subsample."""

    sample_size = min(budget, len(true_g))
    idx = rng.choice(len(true_g), size=sample_size, replace=False)
    sampled_g = true_g[idx]
    sampled_z = noisy_z[idx]
    group_counts = np.bincount(sampled_g, minlength=k).astype(float)
    mismatches = np.bincount(sampled_g[sampled_g != sampled_z], minlength=k).astype(float)
    smoothed_errors = (mismatches + alpha) / (group_counts + 2.0 * alpha)
    pooled_error = float(np.average(smoothed_errors, weights=group_counts + 2.0 * alpha))
    pooled_error = float(np.clip(pooled_error, 0.0, 0.98 * (k - 1) / k))
    confusion = np.full((k, k), pooled_error / (k - 1), dtype=float)
    np.fill_diagonal(confusion, 1.0 - pooled_error)
    return confusion


def metric_record(estimate: np.ndarray, truth: np.ndarray) -> dict[str, float]:
    bias = estimate - truth
    return {
        "gate_rmse": float(np.sqrt(np.mean(np.square(bias)))),
        "mean_subgroup_cate_bias": float(np.mean(np.abs(bias))),
        "max_subgroup_cate_bias": float(np.max(np.abs(bias))),
    }


def run_replication(
    config: DGPConfig,
    n: int,
    expert_budget: int,
    replication: int,
    seed: int,
    alpha: float,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rng = np.random.default_rng(seed + replication)
    tau = np.asarray(config.tau_values, dtype=float)
    probs = np.asarray(config.group_probs, dtype=float)
    errors = np.asarray(config.error_rates, dtype=float)
    k = len(tau)
    data = simulate_dataset(config, n, rng)
    observed_gate_z = gate_by_label(data["Z"], data["T"], data["Y"], k)

    true_confusion = make_confusion_matrix(errors)
    true_posterior = posterior_true_given_noisy(true_confusion, probs)
    oracle_global_confusion = global_confusion_from_pooled_error(errors, probs)
    oracle_global_posterior = posterior_true_given_noisy(oracle_global_confusion, probs)
    estimated_global_confusion = estimate_global_confusion(
        data["G"], data["Z"], k, expert_budget, rng, alpha
    )
    estimated_global_posterior = posterior_true_given_noisy(estimated_global_confusion, probs)

    estimates = {
        METHOD_UNCORRECTED: observed_gate_z,
        METHOD_ORACLE_GLOBAL: corrected_gate(observed_gate_z, oracle_global_posterior),
        METHOD_ESTIMATED_GLOBAL: corrected_gate(observed_gate_z, estimated_global_posterior),
        METHOD_STRATIFIED: corrected_gate(observed_gate_z, true_posterior),
    }

    metric_rows: list[dict[str, object]] = []
    group_rows: list[dict[str, object]] = []
    for method, estimate in estimates.items():
        rec = metric_record(estimate, tau)
        metric_rows.append(
            {
                "replication": replication,
                "config": config.name,
                "method": method,
                **rec,
            }
        )
        for group, (estimate_g, truth_g) in enumerate(zip(estimate, tau, strict=True)):
            group_rows.append(
                {
                    "replication": replication,
                    "config": config.name,
                    "method": method,
                    "group": group,
                    "estimate": float(estimate_g),
                    "true_tau": float(truth_g),
                    "bias": float(estimate_g - truth_g),
                    "abs_bias": float(abs(estimate_g - truth_g)),
                    "squared_error": float((estimate_g - truth_g) ** 2),
                }
            )
    return metric_rows, group_rows


def bootstrap_ci(
    values: Iterable[float], rng: np.random.Generator, n_bootstrap: int
) -> tuple[float, float]:
    arr = np.asarray(list(values), dtype=float)
    if arr.size == 0:
        return float("nan"), float("nan")
    if arr.size == 1 or n_bootstrap <= 0:
        value = float(arr.mean())
        return value, value
    idx = rng.integers(0, arr.size, size=(n_bootstrap, arr.size))
    boot = arr[idx].mean(axis=1)
    return float(np.quantile(boot, 0.025)), float(np.quantile(boot, 0.975))


def summarize(metrics_rows: list[dict[str, object]], args: argparse.Namespace) -> dict[str, object]:
    rng = np.random.default_rng(args.seed + 999_999)
    method_summaries: dict[str, dict[str, dict[str, float]]] = {}
    rows_by_method = {
        method: [row for row in metrics_rows if row["method"] == method] for method in METHODS
    }
    for method in METHODS:
        frame = rows_by_method[method]
        method_summaries[method] = {}
        for metric in [
            "gate_rmse",
            "mean_subgroup_cate_bias",
            "max_subgroup_cate_bias",
        ]:
            values = np.asarray([float(row[metric]) for row in frame], dtype=float)
            ci_low, ci_high = bootstrap_ci(values, rng, args.bootstrap)
            method_summaries[method][metric] = {
                "value": float(values.mean()),
                "ci_low": ci_low,
                "ci_high": ci_high,
            }

    def paired_diff(left: str, right: str, metric: str) -> dict[str, float]:
        by_rep: dict[int, dict[str, float]] = {}
        for row in metrics_rows:
            rep = int(row["replication"])
            by_rep.setdefault(rep, {})[str(row["method"])] = float(row[metric])
        values = np.asarray(
            [method_values[left] - method_values[right] for method_values in by_rep.values()],
            dtype=float,
        )
        ci_low, ci_high = bootstrap_ci(values, rng, args.bootstrap)
        return {"value": float(values.mean()), "ci_low": ci_low, "ci_high": ci_high}

    comparisons = {
        "oracle_global_minus_uncorrected_gate_rmse": paired_diff(
            METHOD_ORACLE_GLOBAL, METHOD_UNCORRECTED, "gate_rmse"
        ),
        "estimated_global_minus_uncorrected_gate_rmse": paired_diff(
            METHOD_ESTIMATED_GLOBAL, METHOD_UNCORRECTED, "gate_rmse"
        ),
        "estimated_global_minus_oracle_global_gate_rmse": paired_diff(
            METHOD_ESTIMATED_GLOBAL, METHOD_ORACLE_GLOBAL, "gate_rmse"
        ),
        "oracle_global_minus_uncorrected_mean_subgroup_cate_bias": paired_diff(
            METHOD_ORACLE_GLOBAL, METHOD_UNCORRECTED, "mean_subgroup_cate_bias"
        ),
        "oracle_global_minus_uncorrected_max_subgroup_cate_bias": paired_diff(
            METHOD_ORACLE_GLOBAL, METHOD_UNCORRECTED, "max_subgroup_cate_bias"
        ),
    }

    primary = comparisons["oracle_global_minus_uncorrected_gate_rmse"]
    gate_supports_h1 = primary["value"] > 0.0 and primary["ci_low"] > 0.0
    opposite_secondary = [
        name
        for name in [
            "oracle_global_minus_uncorrected_mean_subgroup_cate_bias",
            "oracle_global_minus_uncorrected_max_subgroup_cate_bias",
        ]
        if comparisons[name]["value"] < 0.0
    ]
    mixed = bool(gate_supports_h1 and opposite_secondary)
    if mixed:
        conclusion = "mixed"
    elif gate_supports_h1:
        conclusion = "success"
    else:
        conclusion = "negative"

    return {
        "exp_id": EXP_ID,
        "config": SCENARIO_KEY,
        "primary_metric": "gate_rmse",
        "secondary_diagnostics": [
            "mean_subgroup_cate_bias",
            "max_subgroup_cate_bias",
        ],
        "n_replications": len({int(row["replication"]) for row in metrics_rows}),
        "n_per_replication": int(args.n),
        "expert_budget": int(args.expert_budget),
        "bootstrap_replications": int(args.bootstrap),
        "method_metrics": method_summaries,
        "comparisons": comparisons,
        "success_rule": {
            "oracle_global_minus_uncorrected_gate_rmse_gt_0": bool(primary["value"] > 0.0),
            "bootstrap_95_ci_lower_gt_0": bool(primary["ci_low"] > 0.0),
            "gate_rmse_supports_h1": bool(gate_supports_h1),
            "opposite_secondary_diagnostics": opposite_secondary,
            "mixed": mixed,
            "conclusion": conclusion,
        },
    }


def matrix_line(
    target_id: str,
    row: str,
    col: str,
    metric_key: str,
    source: str,
    metric: dict[str, float],
    n_replications: int,
) -> dict[str, object]:
    return {
        "target_id": target_id,
        "row": row,
        "col": col,
        "metric_key": metric_key,
        "exp_id": EXP_ID,
        "source": source,
        "value": metric["value"],
        "ci_low": metric["ci_low"],
        "ci_high": metric["ci_high"],
        "n_replications": n_replications,
    }


def write_matrix_metrics(
    summary: dict[str, object], out_dir: Path, source: str
) -> list[dict[str, object]]:
    n_replications = int(summary["n_replications"])
    comparisons = summary["comparisons"]
    methods = summary["method_metrics"]
    rows = [
        matrix_line(
            CLAIM_ID,
            EXP_ID,
            "uncorrected_vs_oracle_global",
            "oracle_global_minus_uncorrected_gate_rmse",
            source,
            comparisons["oracle_global_minus_uncorrected_gate_rmse"],
            n_replications,
        ),
        matrix_line(
            CLAIM_ID,
            EXP_ID,
            "uncorrected_vs_estimated_global",
            "estimated_global_minus_uncorrected_gate_rmse",
            source,
            comparisons["estimated_global_minus_uncorrected_gate_rmse"],
            n_replications,
        ),
        matrix_line(
            GRID_ID,
            GRID_ROW,
            "uncorrected_gate_rmse",
            f"{SCENARIO_KEY}.uncorrected_gate_rmse",
            source,
            methods[METHOD_UNCORRECTED]["gate_rmse"],
            n_replications,
        ),
        matrix_line(
            GRID_ID,
            GRID_ROW,
            "oracle_global_gate_rmse",
            f"{SCENARIO_KEY}.oracle_global_gate_rmse",
            source,
            methods[METHOD_ORACLE_GLOBAL]["gate_rmse"],
            n_replications,
        ),
        matrix_line(
            GRID_ID,
            GRID_ROW,
            "estimated_global_gate_rmse",
            f"{SCENARIO_KEY}.estimated_global_gate_rmse",
            source,
            methods[METHOD_ESTIMATED_GLOBAL]["gate_rmse"],
            n_replications,
        ),
        matrix_line(
            GRID_ID,
            GRID_ROW,
            "stratified_gate_rmse",
            f"{SCENARIO_KEY}.stratified_gate_rmse",
            source,
            methods[METHOD_STRATIFIED]["gate_rmse"],
            n_replications,
        ),
    ]
    path = out_dir / "matrix_metrics.jsonl"
    path.write_text("\n".join(json.dumps(row, sort_keys=True) for row in rows) + "\n")
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_plots(
    metrics_rows: list[dict[str, object]], group_rows: list[dict[str, object]], out_dir: Path
) -> list[str]:
    plot_dir = out_dir / "plots"
    plot_dir.mkdir(parents=True, exist_ok=True)
    written: list[str] = []

    order = METHODS
    rmse_means = []
    rmse_stds = []
    for method in order:
        values = np.asarray(
            [float(row["gate_rmse"]) for row in metrics_rows if row["method"] == method],
            dtype=float,
        )
        rmse_means.append(float(values.mean()))
        rmse_stds.append(float(values.std(ddof=1)) if len(values) > 1 else 0.0)
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.bar(
        range(len(order)),
        rmse_means,
        yerr=rmse_stds,
        color=["#4c78a8", "#f58518", "#e45756", "#54a24b"],
    )
    ax.set_xticks(range(len(order)))
    ax.set_xticklabels(order, rotation=25, ha="right")
    ax.set_ylabel("gate_rmse")
    ax.set_title("GATE RMSE by correction method")
    fig.tight_layout()
    path = plot_dir / "gate_rmse_by_method.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    written.append(str(path))

    groups = sorted({int(row["group"]) for row in group_rows})
    bias: dict[str, list[float]] = {}
    for method in order:
        bias[method] = []
        for group in groups:
            values = [
                float(row["abs_bias"])
                for row in group_rows
                if row["method"] == method and int(row["group"]) == group
            ]
            bias[method].append(float(np.mean(values)))
    fig, ax = plt.subplots(figsize=(8, 4.8))
    for method in order:
        ax.plot(groups, bias[method], marker="o", label=method)
    ax.set_xlabel("true subgroup")
    ax.set_ylabel("mean absolute subgroup CATE bias")
    ax.set_title("Secondary diagnostic by subgroup")
    ax.legend(fontsize=8)
    fig.tight_layout()
    path = plot_dir / "secondary_bias_by_subgroup.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    written.append(str(path))

    return written


def write_report(summary: dict[str, object], matrix_rows: list[dict[str, object]], out_dir: Path) -> Path:
    comparisons = summary["comparisons"]
    methods = summary["method_metrics"]
    config = positive_corr_high_high_config()
    lines = [
        "# exp_001_bias_bound_mvp",
        "",
        f"- exp_id: {EXP_ID}",
        f"- DGP: {SCENARIO_KEY}",
        f"- primary_metric: {summary['primary_metric']}",
        f"- n_replications: {summary['n_replications']}",
        f"- n_per_replication: {summary['n_per_replication']}",
        f"- expert_budget: {summary['expert_budget']}",
        f"- tau_values: {list(config.tau_values)}",
        f"- error_rates: {list(config.error_rates)}",
        f"- group_probs: {list(config.group_probs)}",
        "",
        "## Primary result",
        "",
        (
            f"`oracle_global - uncorrected` gate_rmse = "
            f"{comparisons['oracle_global_minus_uncorrected_gate_rmse']['value']:.6f} "
            f"[{comparisons['oracle_global_minus_uncorrected_gate_rmse']['ci_low']:.6f}, "
            f"{comparisons['oracle_global_minus_uncorrected_gate_rmse']['ci_high']:.6f}]"
        ),
        f"Conclusion: {summary['success_rule']['conclusion']}",
        "",
        "## Estimated global noise",
        "",
        (
            f"`estimated_global - oracle_global` gate_rmse = "
            f"{comparisons['estimated_global_minus_oracle_global_gate_rmse']['value']:.6f} "
            f"[{comparisons['estimated_global_minus_oracle_global_gate_rmse']['ci_low']:.6f}, "
            f"{comparisons['estimated_global_minus_oracle_global_gate_rmse']['ci_high']:.6f}]"
        ),
        "",
        "## Method gate_rmse",
        "",
    ]
    for method in METHODS:
        metric = methods[method]["gate_rmse"]
        lines.append(f"- {method}: {metric['value']:.6f} [{metric['ci_low']:.6f}, {metric['ci_high']:.6f}]")
    lines.extend(
        [
            "",
            "## Secondary diagnostics",
            "",
        ]
    )
    for key in [
        "oracle_global_minus_uncorrected_mean_subgroup_cate_bias",
        "oracle_global_minus_uncorrected_max_subgroup_cate_bias",
    ]:
        metric = comparisons[key]
        lines.append(f"- {key}: {metric['value']:.6f} [{metric['ci_low']:.6f}, {metric['ci_high']:.6f}]")
    lines.extend(
        [
            "",
            "## Matrix rows",
            "",
        ]
    )
    for row in matrix_rows:
        lines.append(
            f"- {row['target_id']} / {row['row']} / {row['col']} / "
            f"{row['metric_key']} = {row['value']:.6f}"
        )
    path = out_dir / "artifact_report.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def run_experiment(args: argparse.Namespace) -> dict[str, Path | dict[str, object]]:
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    config = positive_corr_high_high_config()
    n_replications = 10 if args.quick else args.replications
    if n_replications < 200 and not args.quick:
        raise ValueError("formal run requires --replications >= 200")

    all_metrics: list[dict[str, object]] = []
    all_groups: list[dict[str, object]] = []
    for replication in range(n_replications):
        metric_rows, group_rows = run_replication(
            config=config,
            n=args.n,
            expert_budget=args.expert_budget,
            replication=replication,
            seed=args.seed,
            alpha=args.alpha,
        )
        all_metrics.extend(metric_rows)
        all_groups.extend(group_rows)

    summary = summarize(all_metrics, args)
    summary["dgp_config"] = asdict(config)

    metrics_csv = out_dir / "metrics.csv"
    group_csv = out_dir / "group_metrics.csv"
    summary_json = out_dir / "summary.json"
    config_json = out_dir / "run_config.json"
    write_csv(metrics_csv, all_metrics)
    write_csv(group_csv, all_groups)
    summary_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    serializable_args = {
        key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()
    }
    config_json.write_text(
        json.dumps(serializable_args, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    source = f"repro/exp_001_bias_bound_mvp/run_experiment.py::{out_dir}"
    matrix_rows = write_matrix_metrics(summary, out_dir, source)
    plot_paths = write_plots(all_metrics, all_groups, out_dir)
    report_path = write_report(summary, matrix_rows, out_dir)

    print(f"wrote {summary_json}")
    print(f"wrote {out_dir / 'matrix_metrics.jsonl'}")
    print(f"wrote {metrics_csv}")
    print(f"wrote {report_path}")
    for path in plot_paths:
        print(f"wrote {path}")
    print(
        "result "
        f"conclusion={summary['success_rule']['conclusion']} "
        f"oracle_minus_uncorrected_gate_rmse="
        f"{summary['comparisons']['oracle_global_minus_uncorrected_gate_rmse']['value']:.6f} "
        f"ci_low={summary['comparisons']['oracle_global_minus_uncorrected_gate_rmse']['ci_low']:.6f}"
    )
    return {
        "out_dir": out_dir,
        "summary": summary,
        "summary_json": summary_json,
        "matrix_metrics": out_dir / "matrix_metrics.jsonl",
        "metrics_csv": metrics_csv,
        "report": report_path,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run exp_001 CPU-only H1 MVP using gate_rmse as the sole primary metric."
    )
    parser.add_argument("--quick", action="store_true", help="Run 10-rep smoke test.")
    parser.add_argument("--replications", type=int, default=200, help="Formal Monte Carlo replications.")
    parser.add_argument("--n", type=int, default=10000, help="Units per replication.")
    parser.add_argument("--expert-budget", type=int, default=600, help="Expert-label subsample size for estimated global correction.")
    parser.add_argument("--bootstrap", type=int, default=2000, help="Bootstrap resamples for 95%% CIs.")
    parser.add_argument("--alpha", type=float, default=0.5, help="Beta-binomial smoothing for estimated confusion.")
    parser.add_argument("--seed", type=int, default=20260531, help="Base random seed.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("artifacts/exp_001_bias_bound_mvp/formal"),
        help="Artifact output directory.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.quick:
        args.bootstrap = min(args.bootstrap, 300)
        if "formal" in str(args.out_dir):
            args.out_dir = Path("artifacts/exp_001_bias_bound_mvp/quick")
    run_experiment(args)


if __name__ == "__main__":
    main()
