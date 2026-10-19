#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.harness_builder.swebench_contract_qualification import (
    run_swebench_contract_qualification,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _sources(values: list[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        name, separator, raw_path = value.partition("=")
        if not separator or not name or name in result:
            raise ValueError(f"invalid or duplicate source binding: {value}")
        result[name] = Path(raw_path)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Qualify the v1r8 Harness contract fix on the failed SWE task"
    )
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--staging-plan", type=Path, required=True)
    parser.add_argument("--rule-registry", type=Path, required=True)
    parser.add_argument("--source", action="append", default=[], metavar="NAME=PATH")
    parser.add_argument("--swebench-canary", type=Path, required=True)
    parser.add_argument("--swebench-dataset", type=Path, required=True)
    parser.add_argument("--swebench-selection", type=Path, required=True)
    parser.add_argument("--swebench-image-lock", type=Path, required=True)
    parser.add_argument("--swebench-host-alias", default="a100jump")
    parser.add_argument("--swebench-remote-python", required=True)
    parser.add_argument("--swebench-remote-project-root", required=True)
    parser.add_argument("--swebench-remote-source-root", required=True)
    parser.add_argument("--swebench-remote-attempt-root", required=True)
    parser.add_argument("--codex-executable", default="codex")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if not args.execute:
        parser.error("qualification requires explicit --execute")
    summary = run_swebench_contract_qualification(
        project_root=args.project_root,
        artifact_root=args.artifact_root,
        staging_path=args.staging_plan,
        rule_registry_path=args.rule_registry,
        source_paths=_sources(args.source),
        canary_summary_path=args.swebench_canary,
        dataset_path=args.swebench_dataset,
        selection_path=args.swebench_selection,
        image_lock_path=args.swebench_image_lock,
        host_alias=args.swebench_host_alias,
        remote_python=args.swebench_remote_python,
        remote_project_root=args.swebench_remote_project_root,
        remote_swebench_source_root=args.swebench_remote_source_root,
        remote_attempt_root=args.swebench_remote_attempt_root,
        codex_executable=args.codex_executable,
    )
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0 if summary["may_start_formal_stream"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
