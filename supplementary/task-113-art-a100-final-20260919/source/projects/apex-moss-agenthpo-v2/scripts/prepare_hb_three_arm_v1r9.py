#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Sequence

from optimization_lab.harness_builder.events import ResourceVector
from optimization_lab.harness_builder.three_arm_continuation import (
    ContinuationSourceSpec,
    ExcludedTailExpectation,
    prepare_three_arm_continuation_source,
)
from optimization_lab.harness_builder.three_arm_v1r9_prepare import (
    prepare_three_arm_v1r9_campaign,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _mapping(values: Sequence[str], label: str) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        name, separator, raw_path = value.partition("=")
        if not separator or not name or not raw_path or name in result:
            raise ValueError(f"invalid or duplicate {label}: {value}")
        result[name] = Path(raw_path)
    return result


def _source_spec(path: Path) -> ContinuationSourceSpec:
    payload = json.loads(path.resolve(strict=True).read_text(encoding="utf-8"))
    fields = {
        "schema_version",
        "kind",
        "source_staging_plan_sha256",
        "source_code_revision",
        "prefix_instance_ids",
        "prefix_receipt_sha256s",
        "online_checkpoint_sha256",
        "online_bank_sha256",
        "rule_registry_sha256",
        "operation_event_count",
        "operation_head_sha256",
        "operation_journal_sha256",
        "operation_anchor_sha256",
        "formal_ledger_sha256",
        "formal_state_sha256",
        "source_committed_usage",
        "excluded_instance_id",
        "excluded_tail_operations",
    }
    if (
        not isinstance(payload, dict)
        or set(payload) != fields
        or payload["schema_version"] != 1
        or payload["kind"] != "three_arm_continuation_source_spec"
        or not isinstance(payload["prefix_instance_ids"], list)
        or not isinstance(payload["prefix_receipt_sha256s"], list)
        or not isinstance(payload["excluded_tail_operations"], list)
    ):
        raise ValueError("v1r9 source spec schema differs")
    return ContinuationSourceSpec(
        source_staging_plan_sha256=payload["source_staging_plan_sha256"],
        source_code_revision=payload["source_code_revision"],
        prefix_instance_ids=tuple(payload["prefix_instance_ids"]),
        prefix_receipt_sha256s=tuple(payload["prefix_receipt_sha256s"]),
        online_checkpoint_sha256=payload["online_checkpoint_sha256"],
        online_bank_sha256=payload["online_bank_sha256"],
        rule_registry_sha256=payload["rule_registry_sha256"],
        operation_event_count=payload["operation_event_count"],
        operation_head_sha256=payload["operation_head_sha256"],
        operation_journal_sha256=payload["operation_journal_sha256"],
        operation_anchor_sha256=payload["operation_anchor_sha256"],
        formal_ledger_sha256=payload["formal_ledger_sha256"],
        formal_state_sha256=payload["formal_state_sha256"],
        source_committed_usage=ResourceVector.from_dict(
            payload["source_committed_usage"]
        ),
        excluded_instance_id=payload["excluded_instance_id"],
        excluded_tail_operations=tuple(
            ExcludedTailExpectation(
                operation_id=item["operation_id"],
                state=item["state"],
                start_event_sha256=item["start_event_sha256"],
            )
            for item in payload["excluded_tail_operations"]
        ),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Capture v1r8 and prepare the v1r9 continuation staging plan"
    )
    commands = parser.add_subparsers(dest="command", required=True)
    capture = commands.add_parser("capture-source")
    capture.add_argument("--source-root", type=Path, required=True)
    capture.add_argument("--artifact-root", type=Path, required=True)
    capture.add_argument("--source-spec", type=Path, required=True)
    capture.add_argument("--execute", action="store_true")

    prepare = commands.add_parser("prepare-staging")
    prepare.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    prepare.add_argument("--artifact-root", type=Path, required=True)
    prepare.add_argument("--source-root", type=Path, required=True)
    prepare.add_argument("--source-manifest", type=Path, required=True)
    prepare.add_argument("--source-snapshot", type=Path, required=True)
    prepare.add_argument("--rule-registry", type=Path, required=True)
    prepare.add_argument("--qualification-transfer", type=Path, required=True)
    prepare.add_argument("--remote-deployment-receipt", type=Path, required=True)
    prepare.add_argument("--swebench-task-lock", type=Path, required=True)
    prepare.add_argument("--swebench-selection", type=Path, required=True)
    prepare.add_argument("--swebench-image-lock", type=Path, required=True)
    prepare.add_argument("--swebench-gold-canary", type=Path, required=True)
    prepare.add_argument("--swebench-host-alias", default="a100jump")
    prepare.add_argument("--swebench-remote-python", required=True)
    prepare.add_argument("--swebench-remote-project-root", required=True)
    prepare.add_argument("--swebench-remote-source-root", required=True)
    prepare.add_argument("--gate", action="append", default=[], metavar="SUITE=PATH")
    prepare.add_argument("--source", action="append", default=[], metavar="NAME=PATH")
    prepare.add_argument("--codex-executable", default="codex")
    prepare.add_argument("--execute", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.execute:
        parser.error("continuation preparation requires explicit --execute")
    if args.command == "capture-source":
        outcome = prepare_three_arm_continuation_source(
            source_root=args.source_root,
            output_root=args.artifact_root,
            spec=_source_spec(args.source_spec),
        )
        print(
            json.dumps(
                {
                    "schema_version": 1,
                    "manifest_path": str(outcome.manifest_path),
                    "manifest_sha256": outcome.manifest_sha256,
                    "snapshot_path": str(outcome.snapshot_path),
                    "snapshot_sha256": outcome.snapshot.sha256,
                    "next_stream_index": outcome.snapshot.next_stream_index,
                    "model_calls_started": 0,
                    "evaluator_transactions_started": 0,
                },
                sort_keys=True,
            )
        )
        return 0

    project_root = args.project_root.resolve(strict=True)
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout.strip()
    payload = prepare_three_arm_v1r9_campaign(
        project_root=project_root,
        artifact_root=args.artifact_root,
        code_revision=revision,
        source_root=args.source_root,
        source_manifest_path=args.source_manifest,
        source_snapshot_path=args.source_snapshot,
        rule_registry_path=args.rule_registry,
        suite_gate_summaries=_mapping(args.gate, "gate"),
        source_paths=_mapping(args.source, "source"),
        qualification_transfer_receipt_path=args.qualification_transfer,
        remote_deployment_receipt_path=args.remote_deployment_receipt,
        swebench_task_lock_path=args.swebench_task_lock,
        swebench_selection_path=args.swebench_selection,
        swebench_image_lock_path=args.swebench_image_lock,
        swebench_gold_canary_summary_path=args.swebench_gold_canary,
        swebench_host_alias=args.swebench_host_alias,
        swebench_remote_python=args.swebench_remote_python,
        swebench_remote_project_root=args.swebench_remote_project_root,
        swebench_remote_source_root=args.swebench_remote_source_root,
        codex_executable=args.codex_executable,
    )
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
