#!/usr/bin/env python3
"""Audit literal intervention spaces shared by agents and HPO baselines."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
METHOD_ROOTS = {
    "agent": ROOT / "tasks/main",
    "tpe": ROOT / "baselines/tpe",
    "bohb": ROOT / "baselines/bohb",
}
EXPECTED_NONLITERAL_TASKS = {"agent_lightning_room_selector"}


def task_ids() -> list[str]:
    payload = json.loads((ROOT / "configs/tasks.json").read_text())
    return [task["id"] for task in payload["tasks"]]


def runner_path(method_root: Path, task_id: str) -> Path:
    candidates = sorted((method_root / task_id).glob("run_formal*.py"))
    if len(candidates) != 1:
        raise ValueError(
            f"Expected one Python runner for {task_id} under {method_root}, "
            f"found {len(candidates)}"
        )
    return candidates[0]


def literal_search_space(path: Path) -> dict[str, Any] | None:
    tree = ast.parse(path.read_text(), filename=str(path))
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if not any(isinstance(target, ast.Name) and target.id == "SEARCH_SPACE" for target in targets):
            continue
        try:
            value = ast.literal_eval(node.value)
        except (ValueError, TypeError):
            continue
        if isinstance(value, dict):
            return value
    return None


def audit() -> dict[str, Any]:
    mismatches: list[dict[str, Any]] = []
    nonliteral: list[str] = []
    comparable = 0

    for task_id in task_ids():
        spaces = {
            method: literal_search_space(runner_path(root, task_id))
            for method, root in METHOD_ROOTS.items()
        }
        if any(space is None for space in spaces.values()):
            nonliteral.append(task_id)
            continue
        comparable += 1
        reference = spaces["agent"]
        differing = [method for method, space in spaces.items() if space != reference]
        if differing:
            mismatches.append(
                {
                    "task": task_id,
                    "differing_methods": differing,
                    "spaces": spaces,
                }
            )

    unexpected_nonliteral = sorted(set(nonliteral) ^ EXPECTED_NONLITERAL_TASKS)
    return {
        "task_count": len(task_ids()),
        "literal_space_task_count": comparable,
        "nonliteral_tasks": sorted(nonliteral),
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "unexpected_nonliteral_tasks": unexpected_nonliteral,
        "passed": not mismatches and not unexpected_nonliteral,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = audit()
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n")
    print(rendered)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
