#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agenthpobench.evaluation.result_integrity import (
    intervention_trace,
    local_model_integrity_issues,
    raw_response_count,
)
from agenthpobench.evaluation.metrics import metric_value


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def canonical_tasks(root: Path = ROOT) -> list[str]:
    payload = load_json(root / "configs" / "tasks.json")
    return [item["id"] for item in payload["tasks"]]


def locate_result(task_dir: Path, task: str) -> tuple[Path | None, str | None]:
    primary = task_dir / f"{task}_QwenLocal_results.json"
    if primary.exists():
        return primary, None
    candidates = sorted(task_dir.glob("*_results.json")) if task_dir.exists() else []
    if len(candidates) == 1:
        return candidates[0], None
    if len(candidates) > 1:
        return None, f"multiple result JSON files: {len(candidates)}"
    return None, "missing result JSON"


def validate_result(
    task: str,
    result_path: Path,
    payload: dict[str, Any],
    *,
    expected_interventions: int,
    expected_seed: int | None,
    expected_model: str | None,
) -> tuple[list[str], int, int]:
    issues = local_model_integrity_issues(
        result_path,
        payload,
        expected_interventions=expected_interventions,
        expected_seed=expected_seed,
        expected_model=expected_model,
    )
    trace_length = 0
    try:
        trace, _ = intervention_trace(payload, expected_interventions)
        trace_length = len(trace)
        final_metric, _ = metric_value(task, trace[-1])
    except ValueError:
        final_metric = None
    if final_metric is None:
        issues.append("final intervention metric missing")
    raw_count = raw_response_count(result_path, payload)
    return list(dict.fromkeys(issues)), trace_length, raw_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("result_root", help="Result directory containing one subdirectory per task")
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--target", type=int, default=5)
    parser.add_argument(
        "--expected-seed",
        type=int,
        help="Require this replicate_seed in every result JSON.",
    )
    parser.add_argument(
        "--expected-model",
        help="Require this model identifier in result metadata or run provenance.",
    )
    parser.add_argument("--non-strict", action="store_true")
    args = parser.parse_args()

    root = Path(args.root)
    result_root = Path(args.result_root)
    if not result_root.is_absolute():
        result_root = root / result_root
    slug = result_root.name

    rows: list[dict[str, Any]] = []
    failed = False
    for idx, task in enumerate(canonical_tasks(root), 1):
        result_path, locate_error = locate_result(result_root / task, task)
        row = {
            "idx": idx,
            "task": task,
            "exists": result_path is not None,
            "valid": False,
            "trace_length": 0,
            "raw_responses": 0,
            "seconds": None,
            "issues": [locate_error] if locate_error else [],
            "result": str(result_path) if result_path else "",
        }
        if result_path is not None:
            try:
                payload = load_json(result_path)
                issues, trace_length, raw_count = validate_result(
                    task,
                    result_path,
                    payload,
                    expected_interventions=args.target,
                    expected_seed=args.expected_seed,
                    expected_model=args.expected_model,
                )
                row["issues"] = issues
                row["trace_length"] = trace_length
                row["raw_responses"] = raw_count
                row["valid"] = not issues
                row["seconds"] = payload.get("pilot_wall_time_seconds") or payload.get("total_time")
            except Exception as exc:
                row["issues"] = [repr(exc)]
        if not row["valid"]:
            failed = True
        rows.append(row)

    print(f"# Strict {args.target}-intervention validation: {slug}")
    print("| # | task | result | valid | trace | raw | seconds | issues |")
    print("|---:|---|---|---:|---:|---:|---:|---|")
    for row in rows:
        result = "yes" if row["exists"] else "missing"
        valid = "yes" if row["valid"] else "no"
        seconds = "" if row["seconds"] is None else str(row["seconds"])
        issues = "; ".join(row["issues"])
        print(
            f"| {row['idx']} | `{row['task']}` | {result} | {valid} | "
            f"{row['trace_length']} | {row['raw_responses']} | {seconds} | {issues} |"
        )
    ok = sum(row["valid"] for row in rows)
    print(
        f"\nSummary: {ok}/{len(rows)} tasks passed exact trace, decision, "
        "fallback, artifact, metric, and requested provenance checks."
    )
    return 0 if args.non_strict or not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
