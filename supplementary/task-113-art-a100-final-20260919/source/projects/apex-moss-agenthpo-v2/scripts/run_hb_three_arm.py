#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.harness_builder.three_arm import ThreeArmCampaignContract
from optimization_lab.harness_builder.three_arm_runtime import (
    build_three_arm_runner,
    result_payload,
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run/recover the three-arm 24-task campaign")
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--staging-plan", type=Path, required=True)
    parser.add_argument("--rule-registry", type=Path, required=True)
    parser.add_argument("--source", action="append", default=[], metavar="NAME=PATH")
    parser.add_argument("--lcbench-canary", type=Path, required=True)
    parser.add_argument("--lcbench-data-root", type=Path, required=True)
    parser.add_argument("--lcbench-settings", type=Path, required=True)
    parser.add_argument("--lcbench-python", type=Path, required=True)
    parser.add_argument("--compilergym-canary", type=Path, required=True)
    parser.add_argument("--compilergym-python", type=Path, required=True)
    parser.add_argument("--compilergym-site-data-root", type=Path, required=True)
    parser.add_argument("--compilergym-cache-root", type=Path, required=True)
    parser.add_argument("--compilergym-compatibility-library-root", type=Path, required=True)
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
    parser.add_argument("--max-new-arm-cells", type=int)
    parser.add_argument("--execute", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    contract = ThreeArmCampaignContract.from_staging_path(args.staging_plan)
    if not args.execute:
        print(
            json.dumps(
                {
                    "schema_version": 1,
                    "phase": contract.phase_id,
                    "execution_ready": contract.execution_ready,
                    "staging_plan_sha256": contract.staging_plan_sha256,
                    "stream_instances": len(contract.stream),
                    "arms": list(contract.arms),
                    "model_calls_started": 0,
                    "evaluator_transactions_started": 0,
                    "no_next_phase": True,
                },
                sort_keys=True,
            )
        )
        return 0
    runner = build_three_arm_runner(
        artifact_root=args.artifact_root,
        staging_path=args.staging_plan,
        project_root=args.project_root,
        rule_registry_path=args.rule_registry,
        source_paths=_sources(args.source),
        lcbench_canary_summary=args.lcbench_canary,
        lcbench_data_root=args.lcbench_data_root,
        lcbench_settings=args.lcbench_settings,
        lcbench_python=args.lcbench_python,
        compilergym_canary_summary=args.compilergym_canary,
        compilergym_python=args.compilergym_python,
        compilergym_site_data_root=args.compilergym_site_data_root,
        compilergym_cache_root=args.compilergym_cache_root,
        compilergym_compatibility_library_root=args.compilergym_compatibility_library_root,
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
                "phase": contract.phase_id,
                "staging_plan_sha256": contract.staging_plan_sha256,
                "result": result_payload(result),
                "no_next_phase": True,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
