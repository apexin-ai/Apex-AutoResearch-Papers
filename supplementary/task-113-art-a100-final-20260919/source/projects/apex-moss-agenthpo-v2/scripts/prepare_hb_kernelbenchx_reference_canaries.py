#!/usr/bin/env python3
"""Pure-offline preparation of content-addressed KernelBenchX canary candidates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.harness_builder.adapters.kernelbenchx import (
    KERNELBENCHX_TASK_HASHES,
    KernelBenchXTask,
)
from optimization_lab.harness_builder.kernelbenchx_reference import (
    prepare_kernelbenchx_reference_canary,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--task-id", action="append", default=[])
    args = parser.parse_args()
    task_ids = tuple(args.task_id) or tuple(KERNELBENCHX_TASK_HASHES)
    if len(task_ids) != len(set(task_ids)):
        raise SystemExit("duplicate --task-id")
    rows = []
    for task_id in task_ids:
        prepared = prepare_kernelbenchx_reference_canary(
            repository=args.repository,
            task=KernelBenchXTask.from_task_id(task_id),
            output_root=args.output_root,
        )
        rows.append(
            {
                "task_id": prepared.task_id,
                "task_sha256": prepared.task_sha256,
                "candidate_sha256": prepared.candidate_sha256,
                "manifest_sha256": prepared.manifest_sha256,
                "manifest_path": str(prepared.manifest_path),
            }
        )
    print(json.dumps({"schema_version": 1, "prepared": rows}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
