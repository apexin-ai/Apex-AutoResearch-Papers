#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import stat
from pathlib import Path

from optimization_lab.harness_builder.adapters.kernelbench_meta import (
    KERNELBENCH_META_EVALUATOR_ID,
    KERNELBENCH_META_PRODUCTION_BLOCKER,
    KERNELBENCH_META_PRODUCTION_READY,
    KERNELBENCH_META_PRODUCTION_RUNTIME_IMPLEMENTED,
    KERNELBENCH_META_PROTOCOL_SHA256,
    KERNELBENCH_META_TRUSTED_INVOCATION_LOOP_IMPLEMENTED,
)
from optimization_lab.harness_builder.adapters.kernel_candidate_policy import (
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
)
from optimization_lab.harness_builder.adapters.kernelbench_meta_isolation import (
    kernelbench_meta_scorer_bundle_sha256,
)
from optimization_lab.harness_builder.meta_train import (
    MetaTrainContract,
    MetaTrainTrajectory,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONTRACT = Path("optimization_lab/harness_builder/data/experience_bank_v1.json")
TRUSTED_SUPERVISOR = Path("scripts/hb_gen1_kernelbench_meta_supervisor.py")


def _preflight(
    *,
    project_root: Path,
    artifact_root: Path,
    historical_paths: tuple[Path, ...],
) -> dict[str, object]:
    contract = MetaTrainContract.from_json(project_root / CONTRACT)
    staging_path = artifact_root / "staging_plan.json"
    blockers: list[str] = []
    if not staging_path.is_file():
        blockers.append("staging_plan_missing")
        staging = None
    else:
        staging = json.loads(staging_path.read_text(encoding="utf-8"))
        entitlements = staging.get("cell_entitlements", {}) if isinstance(staging, dict) else {}
        expected_cells = {source.cell_id for source in contract.new_sources}
        if not isinstance(entitlements, dict) or not expected_cells.issubset(entitlements):
            blockers.append("meta_train_cell_entitlements_missing")
        elif any(
            entitlements[cell_id]
            != {
                "model_calls": 16,
                "evaluator_transactions": 8,
                "gpu_exclusive_seconds": 4800.0,
                "cpu_evaluator_seconds": 0.0,
            }
            for cell_id in expected_cells
        ):
            blockers.append("meta_train_cell_entitlements_changed")
        if entitlements.get("meta:distillation") != {
            "model_calls": 8,
            "evaluator_transactions": 0,
            "gpu_exclusive_seconds": 0.0,
            "cpu_evaluator_seconds": 0.0,
        }:
            blockers.append("meta_train_distillation_entitlement_changed")

    historical: list[MetaTrainTrajectory] = []
    if len(historical_paths) != 2:
        blockers.append("two_historical_trajectory_artifacts_required")
    else:
        historical = [MetaTrainTrajectory.from_json(path) for path in historical_paths]
        expected = {source.instance_id for source in contract.historical_sources}
        if {item.source_instance_id for item in historical} != expected:
            blockers.append("historical_trajectory_sources_differ")
        by_source = {item.source_instance_id: item for item in historical}
        for source in contract.historical_sources:
            trajectory = by_source.get(source.instance_id)
            if trajectory is None or trajectory.source_sha256 != source.source_sha256:
                blockers.append("historical_trajectory_source_hash_differs")
                break

    supervisor_path = project_root / TRUSTED_SUPERVISOR
    supervisor_sha256: str | None = None
    try:
        supervisor_metadata = supervisor_path.lstat()
        if stat.S_ISLNK(supervisor_metadata.st_mode) or not stat.S_ISREG(
            supervisor_metadata.st_mode
        ):
            raise OSError
        supervisor_sha256 = hashlib.sha256(supervisor_path.read_bytes()).hexdigest()
    except OSError:
        blockers.append("trusted_kernelbench_meta_supervisor_missing")
    if not KERNELBENCH_META_PRODUCTION_READY:
        blockers.append(KERNELBENCH_META_PRODUCTION_BLOCKER)
    # The existing staging budget has canary cells only for the three formal
    # held-out benchmarks.  A new scorer cannot consume formal meta-train seats
    # for its safety qualification.
    if not isinstance(staging, dict) or "canary:kernelbench-meta" not in staging.get(
        "cell_entitlements", {}
    ):
        blockers.append("kernelbench_meta_canary_entitlement_missing")
    return {
        "schema_version": 1,
        "phase": "hb-gen1-meta-train",
        "artifact_root": str(artifact_root),
        "repository_commit": contract.repository_commit,
        "new_task_ids": [source.task_id for source in contract.new_sources],
        "historical_task_ids": [source.task_id for source in contract.historical_sources],
        "historical_artifacts_loaded": len(historical),
        "trusted_meta_evaluator": {
            "evaluator": KERNELBENCH_META_EVALUATOR_ID,
            "protocol_sha256": KERNELBENCH_META_PROTOCOL_SHA256,
            "candidate_policy_sha256": RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
            "supervisor_sha256": supervisor_sha256,
            "scorer_bundle_sha256": (
                kernelbench_meta_scorer_bundle_sha256(project_root)
                if supervisor_sha256 is not None
                else None
            ),
            "production_ready": KERNELBENCH_META_PRODUCTION_READY,
            "trusted_invocation_loop_implemented": (
                KERNELBENCH_META_TRUSTED_INVOCATION_LOOP_IMPLEMENTED
            ),
            "production_runtime_implemented": (
                KERNELBENCH_META_PRODUCTION_RUNTIME_IMPLEMENTED
            ),
            "legacy_stdout_parser_allowed": False,
            "legacy_same_process_scorer_allowed": False,
        },
        "execution_ready": not blockers,
        "blockers": sorted(set(blockers)),
        "model_calls_started": 0,
        "evaluator_transactions_started": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Preflight the six-task HB-GEN-1 meta-train runner without starting a model or GPU"
        )
    )
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument(
        "--historical-trajectory",
        type=Path,
        action="append",
        default=[],
        help="Exactly two frozen public historical trajectory artifacts",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Reserved for the future trusted evaluator binding; currently fail-closed",
    )
    args = parser.parse_args()
    report = _preflight(
        project_root=args.project_root.resolve(),
        artifact_root=args.artifact_root.resolve(),
        historical_paths=tuple(path.resolve() for path in args.historical_trajectory),
    )
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    if args.execute:
        raise RuntimeError(
            "HB-GEN-1 meta-train execution remains fail-closed: "
            + ", ".join(report["blockers"])
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
