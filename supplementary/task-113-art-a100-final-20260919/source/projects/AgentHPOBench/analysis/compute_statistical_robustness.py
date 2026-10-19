#!/usr/bin/env python3
"""Compute task-bootstrap and paired-difference robustness summaries.

The script consumes the strict final-step and best-so-far CSV exports. For
three-seed methods, task values are averaged across seeds before task
bootstrapping. Seed-level standard deviations are computed separately from
the 30-task aggregate for each seed.

The generated files map to the supplementary tables as follows:
``final_step_bootstrap.csv`` supports Table 6,
``best_so_far_bootstrap.csv`` and ``seed_level_summary.csv`` support Table 8,
and ``paired_differences.csv`` supports Table 9.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
import pandas as pd


N_BOOTSTRAP = 20_000
RNG_SEED = 20_260_731
CATEGORY_ORDER = ["NLP", "CV", "TS", "Graph", "RL", "LLM", "SL"]

METHOD_ORDER = [
    "random_search",
    "tpe",
    "bohb",
    "gemma2_2b",
    "deepseek_r1_qwen_14b",
    "qwen3_8b",
    "llama3_1_8b",
    "phi4_14b",
    "qwen3_32b",
    "glm5_1",
    "kimi2_6",
    "glm4_7",
    "deepseek_v4_pro",
    "gpt5_5",
    "claude_sonnet_4_6",
]

DISPLAY_NAMES = {
    "random_search": "Random search",
    "tpe": "TPE",
    "bohb": "BOHB variant",
    "gemma2_2b": "Gemma2-2B",
    "deepseek_r1_qwen_14b": "DeepSeek-R1-Qwen-14B",
    "qwen3_8b": "Qwen3-8B",
    "llama3_1_8b": "Llama-3.1-8B",
    "phi4_14b": "Phi-4-14B",
    "qwen3_32b": "Qwen3-32B",
    "glm5_1": "GLM-5.1",
    "kimi2_6": "Kimi-2.6",
    "glm4_7": "GLM-4.7",
    "deepseek_v4_pro": "DeepSeek-V4-Pro",
    "gpt5_5": "GPT-5.5",
    "claude_sonnet_4_6": "Claude Sonnet 4.6",
}

METHOD_TYPES = {
    "random_search": "conventional_hpo",
    "tpe": "conventional_hpo",
    "bohb": "conventional_hpo",
    "gemma2_2b": "open_weight",
    "deepseek_r1_qwen_14b": "open_weight",
    "qwen3_8b": "open_weight",
    "llama3_1_8b": "open_weight",
    "phi4_14b": "open_weight",
    "qwen3_32b": "open_weight",
    "glm5_1": "api",
    "kimi2_6": "api",
    "glm4_7": "api",
    "deepseek_v4_pro": "api",
    "gpt5_5": "api",
    "claude_sonnet_4_6": "api",
}

METRIC_COLUMNS = {
    "mbns": "bounded_normalized_score",
    "maa_percent": "anchor_attainment",
    "bwr_percent": "baseline_win",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-dir", type=Path)
    return parser.parse_args()


def _read_inputs(root: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    summary_dir = root / "results" / "summary"
    controlled = pd.read_csv(summary_dir / "multiseed" / "multiseed_per_run.csv")
    api = pd.read_csv(summary_dir / "multiseed" / "table1_api_per_run.csv")

    controlled = controlled[
        controlled["method"].isin(METHOD_ORDER)
        & controlled["valid"].astype(str).str.lower().eq("true")
    ].copy()
    api = api[api["method"].isin(METHOD_ORDER)].copy()
    api["seed"] = np.nan
    # The API export predates the numerical-tie tolerance used by the current
    # scoring summary. Reconstruct wins from BNS so tiny floating-point
    # deviations from the shared baseline are not counted as improvements.
    api["baseline_win"] = (
        api["bounded_normalized_score"].astype(float) > 1e-8
    ).astype(int)
    final = pd.concat(
        [
            controlled[
                [
                    "method",
                    "seed",
                    "task",
                    "category",
                    "bounded_normalized_score",
                    "baseline_win",
                    "anchor_attainment",
                ]
            ],
            api[
                [
                    "method",
                    "seed",
                    "task",
                    "category",
                    "bounded_normalized_score",
                    "baseline_win",
                    "anchor_attainment",
                ]
            ],
        ],
        ignore_index=True,
    )

    best = pd.read_csv(summary_dir / "best_so_far" / "best_so_far_detail.csv")
    best = best[best["method"].isin(METHOD_ORDER)].copy()
    category_map = (
        final[["task", "category"]].drop_duplicates().set_index("task")["category"]
    )
    best["category"] = best["task"].map(category_map)
    if best["category"].isna().any():
        missing = sorted(best.loc[best["category"].isna(), "task"].unique())
        raise ValueError(f"Missing categories for best-so-far tasks: {missing}")
    return final, best


def _validate_frame(frame: pd.DataFrame, label: str) -> None:
    for method in METHOD_ORDER:
        subset = frame[frame["method"].eq(method)]
        expected_rows = 30 if METHOD_TYPES[method] == "api" else 90
        if len(subset) != expected_rows:
            raise ValueError(
                f"{label}: {method} has {len(subset)} rows, expected {expected_rows}"
            )
        if subset["task"].nunique() != 30:
            raise ValueError(f"{label}: {method} does not cover exactly 30 tasks")
        if METHOD_TYPES[method] != "api":
            seeds = sorted(int(seed) for seed in subset["seed"].unique())
            if seeds != [0, 1, 42]:
                raise ValueError(f"{label}: {method} has seeds {seeds}")
        if subset[list(METRIC_COLUMNS.values())].isna().any().any():
            raise ValueError(f"{label}: {method} contains missing metric values")


def _task_categories(frame: pd.DataFrame) -> pd.Series:
    categories = frame[["task", "category"]].drop_duplicates()
    if categories["task"].nunique() != 30 or len(categories) != 30:
        raise ValueError("Task-to-category mapping is not one-to-one for 30 tasks")
    counts = categories["category"].value_counts().to_dict()
    expected = {"NLP": 3, "CV": 5, "TS": 7, "Graph": 2, "RL": 3, "LLM": 4, "SL": 6}
    if counts != expected:
        raise ValueError(f"Unexpected category counts: {counts}")
    return categories.set_index("task")["category"]


def _task_averages(frame: pd.DataFrame) -> pd.DataFrame:
    return (
        frame.groupby(["method", "task"], as_index=False)[list(METRIC_COLUMNS.values())]
        .mean()
        .sort_values(["method", "task"])
    )


def _seed_summary(frame: pd.DataFrame, estimand: str) -> pd.DataFrame:
    controlled = frame[frame["method"].map(METHOD_TYPES).ne("api")].copy()
    per_seed = (
        controlled.groupby(["method", "seed"], as_index=False)[
            list(METRIC_COLUMNS.values())
        ]
        .mean()
        .rename(columns={value: metric for metric, value in METRIC_COLUMNS.items()})
    )
    per_seed["maa_percent"] *= 100
    per_seed["bwr_percent"] *= 100

    rows = []
    for method in METHOD_ORDER:
        if METHOD_TYPES[method] == "api":
            continue
        subset = per_seed[per_seed["method"].eq(method)]
        row = {
            "estimand": estimand,
            "method": method,
            "display_name": DISPLAY_NAMES[method],
            "method_type": METHOD_TYPES[method],
        }
        for metric in METRIC_COLUMNS:
            row[f"{metric}_mean"] = subset[metric].mean()
            row[f"{metric}_sample_sd"] = subset[metric].std(ddof=1)
        rows.append(row)
    return pd.DataFrame(rows)


def _draw_matrix(tasks: list[str], categories: pd.Series) -> np.ndarray:
    task_to_index = {task: index for index, task in enumerate(tasks)}
    rng = np.random.default_rng(RNG_SEED)
    blocks = []
    for category in CATEGORY_ORDER:
        indices = np.array(
            [task_to_index[task] for task in tasks if categories.loc[task] == category],
            dtype=np.int64,
        )
        blocks.append(rng.choice(indices, size=(N_BOOTSTRAP, len(indices)), replace=True))
    return np.concatenate(blocks, axis=1)


def _bootstrap_summary(
    task_average: pd.DataFrame,
    tasks: list[str],
    draws: np.ndarray,
    estimand: str,
) -> tuple[pd.DataFrame, dict[str, dict[str, np.ndarray]]]:
    rows = []
    distributions: dict[str, dict[str, np.ndarray]] = {}
    for method in METHOD_ORDER:
        indexed = task_average[task_average["method"].eq(method)].set_index("task")
        indexed = indexed.loc[tasks]
        method_distributions = {}
        row = {
            "estimand": estimand,
            "method": method,
            "display_name": DISPLAY_NAMES[method],
            "method_type": METHOD_TYPES[method],
        }
        for metric, column in METRIC_COLUMNS.items():
            scale = 100.0 if metric.endswith("_percent") else 1.0
            values = indexed[column].to_numpy(dtype=float) * scale
            bootstrap = values[draws].mean(axis=1)
            method_distributions[metric] = bootstrap
            row[f"{metric}_point"] = values.mean()
            row[f"{metric}_ci_low"] = np.quantile(bootstrap, 0.025)
            row[f"{metric}_ci_high"] = np.quantile(bootstrap, 0.975)
        bns_values = indexed["bounded_normalized_score"].to_numpy(dtype=float)
        row["median_bns"] = np.median(bns_values)
        rows.append(row)
        distributions[method] = method_distributions
    return pd.DataFrame(rows), distributions


def _paired_differences(
    summary: pd.DataFrame,
    distributions: dict[str, dict[str, np.ndarray]],
    estimand: str,
) -> pd.DataFrame:
    summary = summary.set_index("method")
    rows = []
    for method_a, method_b in itertools.combinations(METHOD_ORDER, 2):
        for metric in METRIC_COLUMNS:
            point = (
                summary.loc[method_a, f"{metric}_point"]
                - summary.loc[method_b, f"{metric}_point"]
            )
            difference = (
                distributions[method_a][metric] - distributions[method_b][metric]
            )
            low = np.quantile(difference, 0.025)
            high = np.quantile(difference, 0.975)
            rows.append(
                {
                    "estimand": estimand,
                    "metric": metric,
                    "method_a": method_a,
                    "display_name_a": DISPLAY_NAMES[method_a],
                    "method_b": method_b,
                    "display_name_b": DISPLAY_NAMES[method_b],
                    "difference_a_minus_b": point,
                    "ci_low": low,
                    "ci_high": high,
                    "excludes_zero": bool(low > 0 or high < 0),
                }
            )
    return pd.DataFrame(rows)


def _write_latex_rows(
    output_dir: Path,
    final_summary: pd.DataFrame,
    best_summary: pd.DataFrame,
    best_seed: pd.DataFrame,
    pairwise: pd.DataFrame,
) -> None:
    sections = []
    final_index = final_summary.set_index("method")
    best_index = best_summary.set_index("method")
    seed_index = best_seed.set_index("method")

    sections.append("% Final-step task-bootstrap rows")
    for method in METHOD_ORDER:
        row = final_index.loc[method]
        sections.append(
            f"{DISPLAY_NAMES[method]} & "
            f"\\({row.mbns_point:.3f}~[{row.mbns_ci_low:.3f},\\,{row.mbns_ci_high:.3f}]\\) & "
            f"\\({row.maa_percent_point:.1f}~[{row.maa_percent_ci_low:.1f},\\,{row.maa_percent_ci_high:.1f}]\\) & "
            f"\\({row.median_bns:.3f}\\) & \\({row.bwr_percent_point:.1f}\\) \\\\"
        )

    sections.append("")
    sections.append("% Best-so-far compact robustness rows")
    for method in METHOD_ORDER:
        row = best_index.loc[method]
        if METHOD_TYPES[method] == "api":
            sd = "--"
        else:
            sd = f"{seed_index.loc[method, 'mbns_sample_sd']:.3f}"
        sections.append(
            f"{DISPLAY_NAMES[method]} & \\({row.mbns_point:.3f}\\) & "
            f"\\({sd}\\) & "
            f"\\([{row.mbns_ci_low:.3f},\\,{row.mbns_ci_high:.3f}]\\) \\\\"
        )

    selected = [
        ("final_step", "claude_sonnet_4_6", "gpt5_5"),
        ("final_step", "phi4_14b", "qwen3_32b"),
        ("final_step", "qwen3_32b", "bohb"),
        ("best_so_far", "claude_sonnet_4_6", "gpt5_5"),
        ("best_so_far", "gpt5_5", "random_search"),
        ("best_so_far", "random_search", "phi4_14b"),
        ("best_so_far", "random_search", "tpe"),
        ("best_so_far", "random_search", "bohb"),
        ("best_so_far", "phi4_14b", "qwen3_32b"),
    ]
    sections.append("")
    sections.append("% Selected paired MBNS difference rows")
    for estimand, method_a, method_b in selected:
        match = pairwise[
            pairwise["estimand"].eq(estimand)
            & pairwise["metric"].eq("mbns")
            & pairwise["method_a"].eq(method_a)
            & pairwise["method_b"].eq(method_b)
        ]
        sign = 1
        if match.empty:
            match = pairwise[
                pairwise["estimand"].eq(estimand)
                & pairwise["metric"].eq("mbns")
                & pairwise["method_a"].eq(method_b)
                & pairwise["method_b"].eq(method_a)
            ]
            sign = -1
        if len(match) != 1:
            raise ValueError(f"Missing selected comparison: {estimand} {method_a} {method_b}")
        row = match.iloc[0]
        point = sign * row["difference_a_minus_b"]
        low = row["ci_low"] if sign == 1 else -row["ci_high"]
        high = row["ci_high"] if sign == 1 else -row["ci_low"]
        label = "Final step" if estimand == "final_step" else "Best so far"
        sections.append(
            f"{label} & {DISPLAY_NAMES[method_a]} -- {DISPLAY_NAMES[method_b]} & "
            f"\\({point:.3f}~[{low:.3f},\\,{high:.3f}]\\) \\\\"
        )

    (output_dir / "latex_rows.tex").write_text("\n".join(sections) + "\n")


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    output_dir = (
        args.output_dir.resolve()
        if args.output_dir
        else root / "results" / "summary" / "statistical_robustness"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    final, best = _read_inputs(root)
    _validate_frame(final, "final_step")
    _validate_frame(best, "best_so_far")

    categories = _task_categories(final)
    tasks = sorted(categories.index.tolist())
    draws = _draw_matrix(tasks, categories)

    final_average = _task_averages(final)
    best_average = _task_averages(best)
    final_summary, final_distributions = _bootstrap_summary(
        final_average, tasks, draws, "final_step"
    )
    best_summary, best_distributions = _bootstrap_summary(
        best_average, tasks, draws, "best_so_far"
    )
    final_seed = _seed_summary(final, "final_step")
    best_seed = _seed_summary(best, "best_so_far")
    pairwise = pd.concat(
        [
            _paired_differences(final_summary, final_distributions, "final_step"),
            _paired_differences(best_summary, best_distributions, "best_so_far"),
        ],
        ignore_index=True,
    )

    final_summary.to_csv(output_dir / "final_step_bootstrap.csv", index=False)
    best_summary.to_csv(output_dir / "best_so_far_bootstrap.csv", index=False)
    pd.concat([final_seed, best_seed], ignore_index=True).to_csv(
        output_dir / "seed_level_summary.csv", index=False
    )
    pairwise.to_csv(output_dir / "paired_differences.csv", index=False)
    _write_latex_rows(output_dir, final_summary, best_summary, best_seed, pairwise)

    metadata = {
        "bootstrap_resamples": N_BOOTSTRAP,
        "rng_seed": RNG_SEED,
        "bootstrap": "category-stratified paired task bootstrap",
        "controlled_method_task_values": "mean across seeds 0, 1, and 42 before resampling",
        "api_method_task_values": "single evaluation",
        "best_so_far_candidates": "interventions 1 through 5; baseline excluded",
        "supplement_table_mapping": {
            "table_6": "final_step_bootstrap.csv",
            "table_8": [
                "best_so_far_bootstrap.csv",
                "seed_level_summary.csv",
            ],
            "table_9": "paired_differences.csv",
        },
        "method_order": METHOD_ORDER,
        "category_order": CATEGORY_ORDER,
    }
    (output_dir / "bootstrap_config.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )

    print(f"Wrote statistical robustness outputs to {output_dir}")
    print(
        final_summary[
            ["display_name", "mbns_point", "mbns_ci_low", "mbns_ci_high"]
        ].to_string(index=False)
    )
    print(
        best_summary[
            ["display_name", "mbns_point", "mbns_ci_low", "mbns_ci_high"]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
