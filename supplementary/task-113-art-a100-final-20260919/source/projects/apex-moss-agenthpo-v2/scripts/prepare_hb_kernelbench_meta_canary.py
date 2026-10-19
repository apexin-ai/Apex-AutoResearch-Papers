#!/usr/bin/env python3
"""Prepare the frozen ten-seat KernelBench meta canary without GPU execution."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.harness_builder.kernelbench_meta_canary import (
    prepare_kernelbench_meta_canary,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--artifact-root", type=Path, required=True)
    args = parser.parse_args()
    prepared = prepare_kernelbench_meta_canary(
        repository=args.repository.resolve(),
        artifact_root=args.artifact_root.resolve(),
    )
    print(
        json.dumps(
            {
                "schema_version": 1,
                "status": "prepared",
                "gpu_or_model_execution": False,
                "plan_path": str(prepared.plan_path),
                "plan_sha256": prepared.plan_sha256,
                "case_count": len(prepared.payload["cases"]),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
