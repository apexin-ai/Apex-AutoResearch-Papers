#!/usr/bin/env python3
"""Seal or re-verify the read-only SWE-bench remote deployment receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Sequence

from optimization_lab.harness_builder.swebench_remote_deployment import (
    prepare_swebench_remote_deployment_receipt,
    verify_swebench_remote_deployment_receipt,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--expected-code-revision", required=True)
    parser.add_argument("--host-alias", default="a100jump")
    parser.add_argument("--remote-project-root", required=True)
    parser.add_argument("--remote-python", required=True)
    parser.add_argument("--remote-swebench-source-root", required=True)
    parser.add_argument("--ssh-executable", default="ssh")
    parser.add_argument("--execute", action="store_true")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare or verify a content-addressed remote SWE-bench "
            "deployment receipt without model/evaluator authority"
        )
    )
    commands = parser.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser("prepare")
    _common(prepare)
    prepare.add_argument("--output-root", type=Path, required=True)
    verify = commands.add_parser("verify")
    _common(verify)
    verify.add_argument("--receipt", type=Path, required=True)
    verify.add_argument("--reprobe", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.execute:
        parser.error("remote deployment preparation requires explicit --execute")
    common = {
        "project_root": args.project_root,
        "expected_code_revision": args.expected_code_revision,
        "host_alias": args.host_alias,
        "remote_project_root": args.remote_project_root,
        "remote_python": args.remote_python,
        "remote_swebench_source_root": args.remote_swebench_source_root,
        "ssh_executable": args.ssh_executable,
    }
    if args.command == "prepare":
        path = prepare_swebench_remote_deployment_receipt(
            output_root=args.output_root,
            **common,
        )
        receipt = json.loads(path.read_text(encoding="utf-8"))
    else:
        path = args.receipt.resolve(strict=True)
        receipt = verify_swebench_remote_deployment_receipt(
            path,
            reprobe=args.reprobe,
            **common,
        )
    print(
        json.dumps(
            {
                "schema_version": 1,
                "receipt_path": str(path),
                "receipt_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "moss_clean_revision": receipt["moss_clean_revision"],
                "worker_sha256": receipt["worker_sha256"],
                "swebench_source_commit": receipt["swebench_source_commit"],
                "remote_python": receipt["remote_python"],
                "model_calls_started": 0,
                "evaluator_transactions_started": 0,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
