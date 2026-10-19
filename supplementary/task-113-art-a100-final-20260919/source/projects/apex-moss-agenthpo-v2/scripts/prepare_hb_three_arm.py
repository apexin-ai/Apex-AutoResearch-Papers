#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from optimization_lab.harness_builder.three_arm_prepare import (
    prepare_three_arm_campaign,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _mapping(values: list[str], label: str) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        name, separator, raw_path = value.partition("=")
        if not separator or not name or name in result:
            raise ValueError(f"invalid or duplicate {label}: {value}")
        result[name] = Path(raw_path)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Freeze the three-arm 24-task campaign")
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--rule-registry", type=Path, required=True)
    parser.add_argument("--gate", action="append", default=[], metavar="SUITE=PATH")
    parser.add_argument("--source", action="append", default=[], metavar="NAME=PATH")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if not args.execute:
        parser.error("staging preparation requires explicit --execute")
    project_root = args.project_root.resolve(strict=True)
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.strip()
    payload = prepare_three_arm_campaign(
        project_root=project_root,
        artifact_root=args.artifact_root,
        code_revision=revision,
        rule_registry_path=args.rule_registry,
        suite_gate_summaries=_mapping(args.gate, "gate"),
        source_paths=_mapping(args.source, "source"),
    )
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
