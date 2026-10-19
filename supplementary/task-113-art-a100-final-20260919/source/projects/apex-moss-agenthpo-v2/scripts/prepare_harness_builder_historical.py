#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.harness_builder.historical_import import (
    HistoricalImportContract,
    prepare_historical_trajectories,
)
from optimization_lab.harness_builder.meta_train import MetaTrainContract


PROJECT_ROOT = Path(__file__).resolve().parents[1]
META_TRAIN_CONTRACT = Path(
    "optimization_lab/harness_builder/data/experience_bank_v1.json"
)
SOURCE_CONTRACT = Path(
    "optimization_lab/harness_builder/data/historical_trajectory_sources_v1.json"
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Offline, fail-closed import of the two frozen all-lanes KernelBench "
            "historical meta-train trajectories"
        )
    )
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--pilot-root", type=Path, required=True)
    parser.add_argument("--p2b-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--meta-train-contract", type=Path)
    parser.add_argument("--source-contract", type=Path)
    args = parser.parse_args()
    project_root = args.project_root.resolve()
    meta_path = (
        args.meta_train_contract.resolve()
        if args.meta_train_contract
        else project_root / META_TRAIN_CONTRACT
    )
    source_path = (
        args.source_contract.resolve()
        if args.source_contract
        else project_root / SOURCE_CONTRACT
    )
    outcome = prepare_historical_trajectories(
        project_root=project_root,
        pilot_root=args.pilot_root.resolve(),
        p2b_root=args.p2b_root.resolve(),
        output_root=args.output_root.resolve(),
        meta_train_contract=MetaTrainContract.from_json(meta_path),
        source_contract=HistoricalImportContract.from_json(source_path),
    )
    response = {
        **outcome.report,
        "prepare_sha256": outcome.report_sha256,
        "prepare_artifact": outcome.report_relative_path,
    }
    print(json.dumps(response, ensure_ascii=False, sort_keys=True))
    return 0 if outcome.report["status"] == "ready" else 2


if __name__ == "__main__":
    raise SystemExit(main())
