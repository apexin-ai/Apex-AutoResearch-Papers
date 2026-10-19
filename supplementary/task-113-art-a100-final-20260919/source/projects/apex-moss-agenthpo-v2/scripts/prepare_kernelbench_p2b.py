#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.p2b_plan import (
    P2bPlan,
    frozen_candidates_from_p2_artifacts,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Freeze the independent KernelBench P2b plan and source frontier"
    )
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument(
        "--source-artifact-root",
        type=Path,
        default=Path(
            "/home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-pilot"
        ),
    )
    parser.add_argument("--executor-model", default="gpt-5.6-sol")
    args = parser.parse_args()

    artifact_root = args.artifact_root.resolve()
    path = artifact_root / "p2b_plan.json"
    if path.exists():
        plan = P2bPlan.read(path)
        if not plan.execution_ready:
            raise RuntimeError("existing P2b plan inputs are incomplete or changed")
    else:
        frozen = frozen_candidates_from_p2_artifacts(
            args.source_artifact_root.resolve()
        )
        plan = P2bPlan.build(
            artifact_root=artifact_root,
            source_artifact_root=args.source_artifact_root,
            executor_model=args.executor_model,
            frozen_candidates=frozen,
        )
        plan.write(path)
    print(
        json.dumps(
            {
                "artifact_root": plan.artifact_root,
                "execution_ready": plan.execution_ready,
                "lane_count": len(plan.lanes),
                "frozen_candidate_count": len(plan.frozen_candidates),
                "model_call_cap": plan.global_model_call_cap,
                "gpu_seconds_cap": plan.global_gpu_seconds_cap,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
