#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Sequence

from optimization_lab.harness_builder.swebench_qualification_transfer import (
    prepare_swebench_qualification_transfer,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Prepare the zero-call v1r8-to-v1r9 SWE qualification transfer"
    )
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--old-qualification-root", type=Path, required=True)
    parser.add_argument("--old-staging-plan", type=Path, required=True)
    parser.add_argument("--selection", type=Path, required=True)
    parser.add_argument("--task-lock", type=Path, required=True)
    parser.add_argument("--image-lock", type=Path, required=True)
    parser.add_argument("--gold-canary", type=Path, required=True)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    if not args.execute:
        parser.error("qualification transfer preparation requires explicit --execute")
    project_root = args.project_root.resolve(strict=True)
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout.strip()
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout.strip()
    if status:
        raise ValueError("qualification transfer requires a clean committed revision")
    path = prepare_swebench_qualification_transfer(
        project_root=project_root,
        output_root=args.artifact_root,
        new_code_revision=revision,
        old_qualification_root=args.old_qualification_root,
        old_staging_path=args.old_staging_plan,
        selection_path=args.selection,
        task_lock_path=args.task_lock,
        image_lock_path=args.image_lock,
        gold_canary_summary_path=args.gold_canary,
    )
    print(
        json.dumps(
            {
                "schema_version": 1,
                "receipt_path": str(path),
                "receipt_sha256": path.stem,
                "model_calls_started": 0,
                "evaluator_transactions_started": 0,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
