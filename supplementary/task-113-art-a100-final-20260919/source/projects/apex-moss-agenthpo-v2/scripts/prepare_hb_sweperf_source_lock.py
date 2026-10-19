from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.harness_builder.sweperf_wrapper import (
    prepare_sweperf_source_lock,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Verify pinned public SWE-Perf sources and write a content-addressed "
            "fail-closed prepare report; never invokes Docker, network, evaluator, or model"
        )
    )
    parser.add_argument("--evaluator-repo", type=Path, required=True)
    parser.add_argument("--dataset-repo", type=Path, required=True)
    parser.add_argument("--parquet", type=Path, required=True)
    parser.add_argument("--pilot-manifest", type=Path)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    kwargs = {
        "evaluator_repo": args.evaluator_repo,
        "dataset_repo": args.dataset_repo,
        "parquet_path": args.parquet,
        "output_root": args.output_root,
    }
    if args.pilot_manifest is not None:
        kwargs["pilot_manifest_path"] = args.pilot_manifest
    prepared = prepare_sweperf_source_lock(**kwargs)
    print(
        json.dumps(
            {
                "status": prepared.status,
                "runnable_wrapper_source_lock": prepared.runnable_wrapper_source_lock,
                "content_id": prepared.content_id,
                "report_path": str(prepared.report_path),
            },
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
