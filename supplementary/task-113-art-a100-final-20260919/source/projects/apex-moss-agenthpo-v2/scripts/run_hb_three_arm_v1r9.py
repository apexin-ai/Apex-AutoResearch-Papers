#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path
from typing import Sequence

from optimization_lab.harness_builder.three_arm_v1r9_runtime import (
    build_three_arm_v1r9_runner,
    preflight_three_arm_v1r9,
    v1r9_dry_run_payload,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _sources(values: Sequence[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        name, separator, raw_path = value.partition("=")
        if not separator or not name or not raw_path or name in result:
            raise ValueError(f"invalid or duplicate source binding: {value}")
        result[name] = Path(raw_path)
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Preflight or run/recover the v1r9 successor continuation"
    )
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--staging-plan", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--source-manifest", type=Path, required=True)
    parser.add_argument("--source-snapshot", type=Path, required=True)
    parser.add_argument("--expected-source-snapshot-sha256", required=True)
    parser.add_argument("--rule-registry", type=Path, required=True)
    parser.add_argument("--qualification-transfer", type=Path, required=True)
    parser.add_argument("--remote-deployment-receipt", type=Path, required=True)
    parser.add_argument("--swebench-task-lock", type=Path, required=True)
    parser.add_argument("--source", action="append", default=[], metavar="NAME=PATH")
    parser.add_argument("--lcbench-canary", type=Path, required=True)
    parser.add_argument("--lcbench-data-root", type=Path)
    parser.add_argument("--lcbench-settings", type=Path)
    parser.add_argument("--lcbench-python", type=Path)
    parser.add_argument("--compilergym-canary", type=Path, required=True)
    parser.add_argument("--compilergym-python", type=Path)
    parser.add_argument("--compilergym-site-data-root", type=Path)
    parser.add_argument("--compilergym-cache-root", type=Path)
    parser.add_argument("--compilergym-compatibility-library-root", type=Path)
    parser.add_argument("--swebench-canary", type=Path, required=True)
    parser.add_argument("--swebench-dataset", type=Path)
    parser.add_argument("--swebench-selection", type=Path, required=True)
    parser.add_argument("--swebench-image-lock", type=Path, required=True)
    parser.add_argument("--swebench-host-alias", default="a100jump")
    parser.add_argument("--swebench-remote-python", required=True)
    parser.add_argument("--swebench-remote-project-root", required=True)
    parser.add_argument("--swebench-remote-source-root", required=True)
    parser.add_argument("--swebench-remote-attempt-root")
    parser.add_argument("--codex-executable", default="codex")
    parser.add_argument("--max-new-arm-cells", type=int)
    parser.add_argument("--execute", action="store_true")
    return parser


def _require_execute_arguments(parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    required = (
        "lcbench_canary",
        "lcbench_data_root",
        "lcbench_settings",
        "lcbench_python",
        "compilergym_canary",
        "compilergym_python",
        "compilergym_site_data_root",
        "compilergym_cache_root",
        "compilergym_compatibility_library_root",
        "swebench_canary",
        "swebench_dataset",
        "swebench_selection",
        "swebench_image_lock",
        "swebench_remote_python",
        "swebench_remote_project_root",
        "swebench_remote_source_root",
        "swebench_remote_attempt_root",
    )
    missing = [name.replace("_", "-") for name in required if getattr(args, name) is None]
    if missing:
        parser.error("--execute requires: " + ", ".join(f"--{name}" for name in missing))


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        sources = _sources(args.source)
    except ValueError as exc:
        parser.error(str(exc))
    preflight = preflight_three_arm_v1r9(
        source_root=args.source_root,
        source_manifest_path=args.source_manifest,
        source_snapshot_path=args.source_snapshot,
        staging_path=args.staging_plan,
        expected_source_snapshot_sha256=args.expected_source_snapshot_sha256,
        rule_registry_path=args.rule_registry,
        lcbench_gate_summary_path=args.lcbench_canary,
        compilergym_gate_summary_path=args.compilergym_canary,
        project_root=args.project_root,
        source_paths=sources,
        qualification_transfer_receipt_path=args.qualification_transfer,
        remote_deployment_receipt_path=args.remote_deployment_receipt,
        swebench_task_lock_path=args.swebench_task_lock,
        swebench_selection_path=args.swebench_selection,
        swebench_image_lock_path=args.swebench_image_lock,
        swebench_gold_canary_summary_path=args.swebench_canary,
        swebench_host_alias=args.swebench_host_alias,
        swebench_remote_python=args.swebench_remote_python,
        swebench_remote_project_root=args.swebench_remote_project_root,
        swebench_remote_source_root=args.swebench_remote_source_root,
        codex_executable=args.codex_executable,
    )
    if not args.execute:
        print(
            json.dumps(
                v1r9_dry_run_payload(
                    contract=preflight.contract,
                    source_snapshot=preflight.source_snapshot,
                ),
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 0

    _require_execute_arguments(parser, args)
    runner = build_three_arm_v1r9_runner(
        artifact_root=args.artifact_root,
        staging_path=args.staging_plan,
        project_root=args.project_root,
        source_root=args.source_root,
        source_manifest_path=args.source_manifest,
        source_snapshot_path=args.source_snapshot,
        expected_source_snapshot_sha256=args.expected_source_snapshot_sha256,
        rule_registry_path=args.rule_registry,
        source_paths=sources,
        qualification_transfer_receipt_path=args.qualification_transfer,
        remote_deployment_receipt_path=args.remote_deployment_receipt,
        swebench_task_lock_path=args.swebench_task_lock,
        lcbench_canary_summary=args.lcbench_canary,
        lcbench_data_root=args.lcbench_data_root,
        lcbench_settings=args.lcbench_settings,
        lcbench_python=args.lcbench_python,
        compilergym_canary_summary=args.compilergym_canary,
        compilergym_python=args.compilergym_python,
        compilergym_site_data_root=args.compilergym_site_data_root,
        compilergym_cache_root=args.compilergym_cache_root,
        compilergym_compatibility_library_root=(
            args.compilergym_compatibility_library_root
        ),
        swebench_canary_summary=args.swebench_canary,
        swebench_dataset=args.swebench_dataset,
        swebench_selection=args.swebench_selection,
        swebench_image_lock=args.swebench_image_lock,
        swebench_host_alias=args.swebench_host_alias,
        swebench_remote_python=args.swebench_remote_python,
        swebench_remote_project_root=args.swebench_remote_project_root,
        swebench_remote_source_root=args.swebench_remote_source_root,
        swebench_remote_attempt_root=args.swebench_remote_attempt_root,
        codex_executable=args.codex_executable,
    )
    result = runner.run(max_new_arm_cells=args.max_new_arm_cells)
    print(
        json.dumps(
            {
                "schema_version": 1,
                "phase": preflight.contract.phase_id,
                "staging_plan_sha256": preflight.contract.staging_plan_sha256,
                "source_snapshot_sha256": preflight.source_snapshot.sha256,
                "result": asdict(result),
                "no_next_phase": True,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
