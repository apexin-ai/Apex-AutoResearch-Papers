#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agenthpobench.evaluation.result_integrity import (
    decision_count,
    fallback_count,
    intervention_trace as trace_items,
    local_model_integrity_issues,
    protocol_integrity_issues,
)
from agenthpobench.evaluation.metrics import METRIC_ALIASES, metric_value


DEFAULT_MANIFEST = ROOT / "configs" / "multiseed_runs.json"
DEFAULT_MODELS = ROOT / "configs" / "models.json"
DEFAULT_REFERENCE = ROOT / "configs" / "scoring_reference.tsv"
DEFAULT_RAW_ROOT = ROOT / "experiments" / "results"
DEFAULT_OUTPUT_DIR = ROOT / "results" / "summary" / "multiseed"
WIN_REL_TOL = 1e-9
WIN_ABS_TOL = 1e-12

CATEGORY_ORDER = ["NLP", "CV", "TS", "Graph", "RL", "LLM", "SL"]
FORMAL_AGGREGATION_ORDER = (
    "score each task and seed, aggregate tasks within each seed, "
    "then average seed-level summaries"
)


def mean(values: list[float]) -> float:
    return statistics.fmean(values)


def sample_sd(values: list[float]) -> float:
    return statistics.stdev(values) if len(values) > 1 else 0.0


def load_reference(path: Path) -> dict[str, dict[str, Any]]:
    result = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            result[row["task"]] = {
                "category": row["category"],
                "direction": row["direction"],
                "baseline": float(row["baseline"]),
                "anchor": float(row["anchor"]),
            }
    if set(result) != set(METRIC_ALIASES):
        missing = sorted(set(METRIC_ALIASES) - set(result))
        extra = sorted(set(result) - set(METRIC_ALIASES))
        raise ValueError(f"scoring reference mismatch: missing={missing}, extra={extra}")
    return result


def locate_result(
    raw_root: Path, sources: list[str], task: str
) -> tuple[Path | None, str | None]:
    for source in sources:
        task_dir = raw_root / source / task
        primary = task_dir / f"{task}_QwenLocal_results.json"
        if primary.exists():
            return primary, source
        candidates = sorted(task_dir.glob("*_results.json")) if task_dir.exists() else []
        if candidates:
            return candidates[0], source
    return None, None


def score(value: float, reference: dict[str, Any]) -> dict[str, float | int]:
    baseline = float(reference["baseline"])
    anchor = float(reference["anchor"])
    denominator = abs(anchor - baseline)
    if math.isclose(denominator, 0.0, rel_tol=0.0, abs_tol=1e-15):
        raise ValueError("baseline equals anchor")
    if reference["direction"] == "higher":
        normalized = (value - baseline) / denominator
        attainment = value / anchor
        win = int(
            value > baseline
            and not math.isclose(
                value, baseline, rel_tol=WIN_REL_TOL, abs_tol=WIN_ABS_TOL
            )
        )
    else:
        normalized = (baseline - value) / denominator
        attainment = anchor / value
        win = int(
            value < baseline
            and not math.isclose(
                value, baseline, rel_tol=WIN_REL_TOL, abs_tol=WIN_ABS_TOL
            )
        )
    return {
        "normalized_score": normalized,
        "bounded_normalized_score": min(1.0, max(-1.0, normalized)),
        "baseline_win": win,
        "anchor_attainment": attainment,
    }


def extract_run(
    *,
    method: dict[str, Any],
    seed: int,
    task: str,
    reference: dict[str, Any],
    raw_root: Path,
    require_local_artifacts: bool = False,
) -> dict[str, Any]:
    sources = method["runs"][str(seed)]
    path, selected_source = locate_result(raw_root, sources, task)
    row = {
        "method": method["id"],
        "display_name": method["display_name"],
        "method_type": method["type"],
        "seed": seed,
        "task": task,
        **reference,
        "source": selected_source or "",
        "result_path": "",
        "valid": False,
        "error": "missing result",
    }
    if path is None:
        return row
    row["result_path"] = str(path.relative_to(raw_root))
    try:
        payload = json.loads(path.read_text())
        trace, trace_schema = trace_items(payload)
        decisions, decision_inferred = decision_count(payload, trace)
        fallbacks = fallback_count(payload)
        if method["type"] in {"open_weight", "ablation"}:
            integrity_issues = local_model_integrity_issues(
                path,
                payload,
                expected_seed=seed,
                expected_model=(
                    method.get("expected_model")
                    if require_local_artifacts
                    else None
                ),
                require_seed=require_local_artifacts,
                require_raw_responses=require_local_artifacts,
                check_artifacts=require_local_artifacts,
            )
        else:
            integrity_issues = protocol_integrity_issues(
                payload,
                expected_seed=seed,
                require_seed=False,
            )
        final, metric_key = metric_value(task, trace[-1])
        if final is None:
            raise ValueError("final metric missing")
        if integrity_issues:
            raise ValueError("; ".join(integrity_issues))
        row.update(
            {
                "final": final,
                "metric_key": metric_key,
                "trace_schema": trace_schema,
                "trace_length": len(trace),
                "decision_count": decisions,
                "decision_count_inferred": decision_inferred,
                "fallback_decision_count": fallbacks,
                **score(final, reference),
                "valid": True,
                "error": "",
            }
        )
    except Exception as exc:
        row["error"] = str(exc)
    return row


def summarize_seed(rows: list[dict[str, Any]]) -> dict[str, float]:
    return {
        "mbns": mean([float(row["bounded_normalized_score"]) for row in rows]),
        "bwr_percent": 100.0 * mean([float(row["baseline_win"]) for row in rows]),
        "maa_percent": 100.0 * mean([float(row["anchor_attainment"]) for row in rows]),
    }


def aggregate_method(
    method: dict[str, Any],
    rows: list[dict[str, Any]],
    seeds: list[int],
    task_order: list[str],
) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    valid_rows = [row for row in rows if row["valid"]]
    by_seed = {
        seed: [row for row in valid_rows if row["seed"] == seed] for seed in seeds
    }
    seed_protocol_counts = {str(seed): len(by_seed[seed]) for seed in seeds}
    protocol_valid = all(len(by_seed[seed]) == len(task_order) for seed in seeds)
    errors = [
        {
            "seed": row["seed"],
            "task": row["task"],
            "error": row["error"],
            "result_path": row["result_path"],
        }
        for row in rows
        if not row["valid"]
    ]
    summary: dict[str, Any] = {
        "method": method["id"],
        "display_name": method["display_name"],
        "method_type": method["type"],
        "protocol_valid": protocol_valid,
        "valid_tasks_by_seed": seed_protocol_counts,
        "errors": errors,
    }
    complete_seeds = [seed for seed in seeds if len(by_seed[seed]) == len(task_order)]
    summary["complete_seeds"] = complete_seeds
    if complete_seeds:
        complete_seed_summaries = {
            seed: summarize_seed(by_seed[seed]) for seed in complete_seeds
        }
        summary["available_complete_seed_summaries"] = {
            str(seed): complete_seed_summaries[seed] for seed in complete_seeds
        }
        summary["available_complete_seed_summary"] = {
            metric: {
                "mean": mean(
                    [complete_seed_summaries[seed][metric] for seed in complete_seeds]
                ),
                "sd": sample_sd(
                    [complete_seed_summaries[seed][metric] for seed in complete_seeds]
                ),
            }
            for metric in ("mbns", "bwr_percent", "maa_percent")
        }
    task_rows: list[dict[str, Any]] = []
    category_rows: list[dict[str, Any]] = []
    if not protocol_valid:
        return summary, task_rows, category_rows

    seed_summaries = {seed: summarize_seed(by_seed[seed]) for seed in seeds}
    across_seed_summary = {
        metric: {
            "mean": mean([seed_summaries[seed][metric] for seed in seeds]),
            "sd": sample_sd([seed_summaries[seed][metric] for seed in seeds]),
        }
        for metric in ("mbns", "bwr_percent", "maa_percent")
    }
    by_task_seed = {
        (row["task"], row["seed"]): row
        for row in valid_rows
    }
    for task in task_order:
        selected = [by_task_seed[(task, seed)] for seed in seeds]
        raw_values = [float(row["final"]) for row in selected]
        raw_mean = mean(raw_values)
        aggregate_scores = score(raw_mean, selected[0])
        seed_bns_values = [
            float(row["bounded_normalized_score"]) for row in selected
        ]
        seed_wins = [int(row["baseline_win"]) for row in selected]
        seed_attainment_values = [
            float(row["anchor_attainment"]) for row in selected
        ]
        task_rows.append(
            {
                "method": method["id"],
                "display_name": method["display_name"],
                "method_type": method["type"],
                "task": task,
                "category": selected[0]["category"],
                "direction": selected[0]["direction"],
                "baseline": selected[0]["baseline"],
                "anchor": selected[0]["anchor"],
                "seed0_final": raw_values[0],
                "seed1_final": raw_values[1],
                "seed42_final": raw_values[2],
                "final_mean": raw_mean,
                "final_sd": sample_sd(raw_values),
                "seed_bns_mean": mean(seed_bns_values),
                "seed_bns_sd": sample_sd(seed_bns_values),
                "seed_baseline_win_mean": mean(seed_wins),
                "seed_baseline_win_sd": sample_sd(seed_wins),
                "seed_anchor_attainment_mean": mean(seed_attainment_values),
                "seed_anchor_attainment_sd": sample_sd(seed_attainment_values),
                "seed_win_agreement": len(set(seed_wins)) == 1,
                "raw_mean_then_score_normalized_score": aggregate_scores[
                    "normalized_score"
                ],
                "raw_mean_then_score_bounded_normalized_score": aggregate_scores[
                    "bounded_normalized_score"
                ],
                "raw_mean_then_score_baseline_win": aggregate_scores[
                    "baseline_win"
                ],
                "raw_mean_then_score_anchor_attainment": aggregate_scores[
                    "anchor_attainment"
                ],
            }
        )

    summary.update(
        {
            "paper_aggregate": {
                "ordering": FORMAL_AGGREGATION_ORDER,
                "mbns": across_seed_summary["mbns"]["mean"],
                "bwr_percent": across_seed_summary["bwr_percent"]["mean"],
                "maa_percent": across_seed_summary["maa_percent"]["mean"],
            },
            "raw_mean_then_score_diagnostic": {
                "ordering": "mean raw metric across seeds per task, then score",
                "mbns": mean(
                    [
                        float(
                            row[
                                "raw_mean_then_score_bounded_normalized_score"
                            ]
                        )
                        for row in task_rows
                    ]
                ),
                "bwr_percent": 100.0
                * mean(
                    [
                        float(row["raw_mean_then_score_baseline_win"])
                        for row in task_rows
                    ]
                ),
                "maa_percent": 100.0
                * mean(
                    [
                        float(row["raw_mean_then_score_anchor_attainment"])
                        for row in task_rows
                    ]
                ),
            },
            "seed_summaries": {str(seed): seed_summaries[seed] for seed in seeds},
            "across_seed_summary": across_seed_summary,
            "task_win_sign_agreement_percent": 100.0
            * mean([float(row["seed_win_agreement"]) for row in task_rows]),
        }
    )

    categories = sorted({row["category"] for row in task_rows})
    for category in categories:
        selected = [row for row in task_rows if row["category"] == category]
        seed_category_summaries = {}
        for seed in seeds:
            seed_selected = [
                by_task_seed[(row["task"], seed)]
                for row in selected
            ]
            seed_category_summaries[seed] = summarize_seed(seed_selected)
        category_rows.append(
            {
                "method": method["id"],
                "display_name": method["display_name"],
                "category": category,
                "task_count": len(selected),
                "mbns": mean(
                    [seed_category_summaries[seed]["mbns"] for seed in seeds]
                ),
                "bwr_percent": mean(
                    [
                        seed_category_summaries[seed]["bwr_percent"]
                        for seed in seeds
                    ]
                ),
                "maa_percent": mean(
                    [
                        seed_category_summaries[seed]["maa_percent"]
                        for seed in seeds
                    ]
                ),
                "seed_mbns_mean": mean(
                    [seed_category_summaries[seed]["mbns"] for seed in seeds]
                ),
                "seed_mbns_sd": sample_sd(
                    [seed_category_summaries[seed]["mbns"] for seed in seeds]
                ),
                "seed_bwr_mean": mean(
                    [
                        seed_category_summaries[seed]["bwr_percent"]
                        for seed in seeds
                    ]
                ),
                "seed_bwr_sd": sample_sd(
                    [
                        seed_category_summaries[seed]["bwr_percent"]
                        for seed in seeds
                    ]
                ),
                "seed_maa_mean": mean(
                    [
                        seed_category_summaries[seed]["maa_percent"]
                        for seed in seeds
                    ]
                ),
                "seed_maa_sd": sample_sd(
                    [
                        seed_category_summaries[seed]["maa_percent"]
                        for seed in seeds
                    ]
                ),
                "raw_mean_then_score_mbns": mean(
                    [
                        float(
                            row[
                                "raw_mean_then_score_bounded_normalized_score"
                            ]
                        )
                        for row in selected
                    ]
                ),
                "raw_mean_then_score_bwr_percent": 100.0
                * mean(
                    [
                        float(row["raw_mean_then_score_baseline_win"])
                        for row in selected
                    ]
                ),
                "raw_mean_then_score_maa_percent": 100.0
                * mean(
                    [
                        float(row["raw_mean_then_score_anchor_attainment"])
                        for row in selected
                    ]
                ),
            }
        )
    return summary, task_rows, category_rows


def build_paper_table_rows(
    summaries: list[dict[str, Any]],
    category_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    categories = {
        (row["method"], row["category"]): row for row in category_rows
    }
    rows = []
    for summary in summaries:
        if (
            not summary["protocol_valid"]
            or summary["method_type"] not in {"conventional_hpo", "open_weight"}
        ):
            continue
        across = summary["across_seed_summary"]
        row = {
            "method": summary["method"],
            "display_name": summary["display_name"],
            "method_type": summary["method_type"],
            "aggregation_order": FORMAL_AGGREGATION_ORDER,
        }
        for category in CATEGORY_ORDER:
            category_row = categories[(summary["method"], category)]
            key = category.lower()
            row[f"{key}_mbns_mean"] = category_row["seed_mbns_mean"]
            row[f"{key}_mbns_sd"] = category_row["seed_mbns_sd"]
        for metric in ("mbns", "bwr_percent", "maa_percent"):
            row[f"overall_{metric}_mean"] = across[metric]["mean"]
            row[f"overall_{metric}_sd"] = across[metric]["sd"]
        rows.append(row)
    return rows


def write_csv(
    path: Path,
    rows: list[dict[str, Any]],
    *,
    fieldnames: list[str] | None = None,
) -> None:
    if not rows and fieldnames is None:
        path.unlink(missing_ok=True)
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames or list(rows[0]),
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(rows)


def fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "-"
    return f"{float(value):.{digits}f}"


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# AgentHPOBench Multiseed Summary",
        "",
        "Seeds: 0, 1, and 42. The formal paper aggregate scores bounded "
        "normalized score, baseline win, and anchor attainment independently "
        "for every task and seed. It then aggregates tasks within each seed "
        "and reports the arithmetic mean across seed-level summaries.",
        "",
        "| Method | Status | MBNS | BWR (%) | MAA (%) | Seed MBNS mean +/- SD | "
        "Seed BWR mean +/- SD | Seed MAA mean +/- SD | Win-sign agreement (%) |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for summary in payload["methods"]:
        if not summary["protocol_valid"]:
            count_text = ", ".join(
                f"s{seed}={count}/30"
                for seed, count in summary["valid_tasks_by_seed"].items()
            )
            lines.append(
                f"| {summary['display_name']} | protocol-invalid ({count_text}) | "
                "- | - | - | - | - | - | - |"
            )
            continue
        paper = summary["paper_aggregate"]
        across = summary["across_seed_summary"]
        lines.append(
            f"| {summary['display_name']} | valid | {fmt(paper['mbns'])} | "
            f"{fmt(paper['bwr_percent'], 1)} | {fmt(paper['maa_percent'], 1)} | "
            f"{fmt(across['mbns']['mean'])} +/- {fmt(across['mbns']['sd'])} | "
            f"{fmt(across['bwr_percent']['mean'], 1)} +/- "
            f"{fmt(across['bwr_percent']['sd'], 1)} | "
            f"{fmt(across['maa_percent']['mean'], 1)} +/- "
            f"{fmt(across['maa_percent']['sd'], 1)} | "
            f"{fmt(summary['task_win_sign_agreement_percent'], 1)} |"
        )

    summaries = {item["method"]: item for item in payload["methods"]}
    main = summaries.get("qwen3_32b")
    ablation = summaries.get("qwen3_32b_no_feedback")
    if main and ablation and main["protocol_valid"] and ablation["protocol_valid"]:
        lines.extend(
            [
                "",
                "## No-Feedback Ablation",
                "",
                "| Comparison | Delta MBNS | Delta BWR (pp) | Delta MAA (pp) |",
                "|---|---:|---:|---:|",
                "| No feedback - full feedback | "
                f"{ablation['paper_aggregate']['mbns'] - main['paper_aggregate']['mbns']:+.3f} | "
                f"{ablation['paper_aggregate']['bwr_percent'] - main['paper_aggregate']['bwr_percent']:+.1f} | "
                f"{ablation['paper_aggregate']['maa_percent'] - main['paper_aggregate']['maa_percent']:+.1f} |",
            ]
        )

    invalid = [item for item in payload["methods"] if not item["protocol_valid"]]
    if invalid:
        lines.extend(
            [
                "",
                "## Protocol Audit",
                "",
                "Protocol-invalid methods are excluded from the formal comparison. "
                "Their result directories are retained in the source audit so the "
                "missing strict five-intervention runs can be reproduced.",
                "",
            ]
        )
        for item in invalid:
            lines.append(
                f"- **{item['display_name']}**: "
                + ", ".join(
                    f"seed {seed}: {count}/30 valid tasks"
                    for seed, count in item["valid_tasks_by_seed"].items()
                )
                + "."
            )
            complete = item.get("available_complete_seed_summary")
            if complete:
                lines.append(
                    "  Complete-seed subset "
                    f"{item['complete_seeds']}: MBNS "
                    f"{complete['mbns']['mean']:.3f} +/- "
                    f"{complete['mbns']['sd']:.3f}, BWR "
                    f"{complete['bwr_percent']['mean']:.1f} +/- "
                    f"{complete['bwr_percent']['sd']:.1f}%, MAA "
                    f"{complete['maa_percent']['mean']:.1f} +/- "
                    f"{complete['maa_percent']['sd']:.1f}%."
                )
    path.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit and aggregate AgentHPOBench seed 0/1/42 results."
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--models", type=Path, default=DEFAULT_MODELS)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--raw-results-root", type=Path, default=DEFAULT_RAW_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if any method not explicitly allowed as invalid misses the protocol.",
    )
    parser.add_argument(
        "--require-local-artifacts",
        action="store_true",
        help=(
            "For open-weight and ablation runs, also require retained raw "
            "responses and explicit replicate_seed metadata. This implies --strict."
        ),
    )
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text())
    configured_models = json.loads(args.models.read_text())["agent_models"]
    references = load_reference(args.reference)
    task_order = list(METRIC_ALIASES)
    seeds = [int(seed) for seed in manifest["seeds"]]
    if seeds != [0, 1, 42]:
        raise ValueError(f"expected seeds [0, 1, 42], got {seeds}")

    run_rows = []
    summaries = []
    task_rows = []
    category_rows = []
    strict_failures = []
    for manifest_method in manifest["methods"]:
        method = dict(manifest_method)
        model_id = method.get("model_id")
        if model_id:
            if model_id not in configured_models:
                raise ValueError(f"unknown model_id for {method['id']}: {model_id}")
            method["expected_model"] = Path(configured_models[model_id]).name
        if set(method["runs"]) != {"0", "1", "42"}:
            raise ValueError(f"incomplete seed mapping: {method['id']}")
        method_rows = [
            extract_run(
                method=method,
                seed=seed,
                task=task,
                reference=references[task],
                raw_root=args.raw_results_root,
                require_local_artifacts=args.require_local_artifacts,
            )
            for seed in seeds
            for task in task_order
        ]
        summary, method_task_rows, method_category_rows = aggregate_method(
            method, method_rows, seeds, task_order
        )
        if (
            (args.strict or args.require_local_artifacts)
            and not summary["protocol_valid"]
            and not method.get("allow_protocol_invalid")
        ):
            details = "; ".join(
                f"seed {item['seed']} {item['task']}: {item['error']}"
                for item in summary["errors"]
            )
            strict_failures.append(
                f"{method['id']} failed protocol audit: {details}"
            )
        run_rows.extend(method_rows)
        summaries.append(summary)
        task_rows.extend(method_task_rows)
        category_rows.extend(method_category_rows)

    payload = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "seeds": seeds,
        "aggregation_order": FORMAL_AGGREGATION_ORDER,
        "score_bounds": [-1.0, 1.0],
        "local_artifact_validation_required": args.require_local_artifacts,
        "methods": summaries,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "multiseed_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    write_csv(args.output_dir / "multiseed_per_run.csv", run_rows)
    repair_fields = [
        "method",
        "display_name",
        "method_type",
        "seed",
        "task",
        "error",
        "fallback_decision_count",
        "trace_length",
        "decision_count",
        "source",
        "result_path",
    ]
    write_csv(
        args.output_dir / "multiseed_repair_plan.csv",
        [
            {field: row.get(field, "") for field in repair_fields}
            for row in run_rows
            if not row["valid"]
        ],
        fieldnames=repair_fields,
    )
    write_csv(args.output_dir / "multiseed_per_task.csv", task_rows)
    write_csv(args.output_dir / "multiseed_category_summary.csv", category_rows)
    write_csv(
        args.output_dir / "multiseed_paper_table.csv",
        build_paper_table_rows(summaries, category_rows),
    )
    write_csv(
        args.output_dir / "multiseed_method_summary.csv",
        [
            {
                "method": item["method"],
                "display_name": item["display_name"],
                "method_type": item["method_type"],
                "protocol_valid": item["protocol_valid"],
                "mbns": item.get("paper_aggregate", {}).get("mbns"),
                "bwr_percent": item.get("paper_aggregate", {}).get("bwr_percent"),
                "maa_percent": item.get("paper_aggregate", {}).get("maa_percent"),
                "aggregation_order": item.get("paper_aggregate", {}).get(
                    "ordering"
                ),
                "raw_mean_then_score_mbns": item.get(
                    "raw_mean_then_score_diagnostic", {}
                ).get("mbns"),
                "raw_mean_then_score_bwr_percent": item.get(
                    "raw_mean_then_score_diagnostic", {}
                ).get("bwr_percent"),
                "raw_mean_then_score_maa_percent": item.get(
                    "raw_mean_then_score_diagnostic", {}
                ).get("maa_percent"),
                "seed_mbns_mean": item.get("across_seed_summary", {})
                .get("mbns", {})
                .get("mean"),
                "seed_mbns_sd": item.get("across_seed_summary", {})
                .get("mbns", {})
                .get("sd"),
                "seed_bwr_mean": item.get("across_seed_summary", {})
                .get("bwr_percent", {})
                .get("mean"),
                "seed_bwr_sd": item.get("across_seed_summary", {})
                .get("bwr_percent", {})
                .get("sd"),
                "seed_maa_mean": item.get("across_seed_summary", {})
                .get("maa_percent", {})
                .get("mean"),
                "seed_maa_sd": item.get("across_seed_summary", {})
                .get("maa_percent", {})
                .get("sd"),
                "task_win_sign_agreement_percent": item.get(
                    "task_win_sign_agreement_percent"
                ),
                "complete_seeds": " ".join(map(str, item["complete_seeds"])),
                "available_seed_mbns_mean": item.get(
                    "available_complete_seed_summary", {}
                )
                .get("mbns", {})
                .get("mean"),
                "available_seed_mbns_sd": item.get(
                    "available_complete_seed_summary", {}
                )
                .get("mbns", {})
                .get("sd"),
                "available_seed_bwr_mean": item.get(
                    "available_complete_seed_summary", {}
                )
                .get("bwr_percent", {})
                .get("mean"),
                "available_seed_maa_mean": item.get(
                    "available_complete_seed_summary", {}
                )
                .get("maa_percent", {})
                .get("mean"),
            }
            for item in summaries
        ],
    )
    write_markdown(args.output_dir / "multiseed_summary.md", payload)

    print(args.output_dir / "multiseed_summary.json")
    print(args.output_dir / "multiseed_method_summary.csv")
    print(args.output_dir / "multiseed_paper_table.csv")
    print(args.output_dir / "multiseed_per_task.csv")
    print(args.output_dir / "multiseed_per_run.csv")
    print(args.output_dir / "multiseed_repair_plan.csv")
    print(args.output_dir / "multiseed_category_summary.csv")
    print(args.output_dir / "multiseed_summary.md")
    if strict_failures:
        raise RuntimeError("\n".join(strict_failures))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
