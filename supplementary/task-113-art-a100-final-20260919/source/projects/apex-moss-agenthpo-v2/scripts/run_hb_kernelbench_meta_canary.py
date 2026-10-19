#!/usr/bin/env python3
"""Preflight or explicitly run the frozen HB-GEN-1 KernelBench meta canary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.harness_builder.adapters.kernelbench_meta import (
    KernelBenchMetaAdapter,
)
from optimization_lab.harness_builder.adapters.kernelbench_meta_isolation import (
    kernelbench_meta_scorer_bundle_sha256,
)
from optimization_lab.harness_builder.kernelbench_meta_canary import (
    KernelBenchMetaCanaryController,
    KernelBenchMetaCanaryError,
    prepare_kernelbench_meta_canary,
)
from optimization_lab.harness_builder.prepare import resolve_clean_code_revision


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--canary-plan", type=Path)
    parser.add_argument(
        "--authorization-receipt",
        type=Path,
        help=(
            "Externally issued, content-addressed evaluator capability receipt. "
            "The controller consumes this file and never creates it."
        ),
    )
    parser.add_argument("--gpu", default="4")
    parser.add_argument(
        "--execute",
        action="store_true",
        help=(
            "Consume the ten-seat evaluator entitlement. Without this flag the "
            "command only performs offline validation."
        ),
    )
    args = parser.parse_args()
    project_root = args.project_root.resolve()
    artifact_root = args.artifact_root.resolve()
    repository = args.repository.resolve()
    if args.canary_plan is None:
        canary_plan = prepare_kernelbench_meta_canary(
            repository=repository,
            artifact_root=artifact_root / "kernelbench-meta-canary-prepared",
        ).plan_path
    else:
        canary_plan = args.canary_plan.resolve()
    code_revision = resolve_clean_code_revision(project_root)
    scorer_sha = kernelbench_meta_scorer_bundle_sha256(project_root)
    try:
        controller = KernelBenchMetaCanaryController(
            artifact_root=artifact_root,
            staging_plan=artifact_root / "staging_plan.json",
            canary_plan=canary_plan,
            code_revision=code_revision,
            scorer_bundle_sha256=scorer_sha,
            authorization_receipt=args.authorization_receipt,
        )
    except KernelBenchMetaCanaryError as exc:
        print(
            json.dumps(
                {
                    "schema_version": 1,
                    "status": "blocked",
                    "blockers": [" ".join(str(exc).split())],
                    "gpu_or_model_execution": False,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 2
    if not args.execute:
        print(json.dumps(controller.preflight(), ensure_ascii=False, sort_keys=True))
        return 0
    if controller.authorization_receipt is None:
        print(json.dumps(controller.preflight(), ensure_ascii=False, sort_keys=True))
        return 2
    adapter = KernelBenchMetaAdapter(
        repository=repository,
        supervisor=project_root / "scripts/hb_gen1_kernelbench_meta_supervisor.py",
        scorer_sha256=scorer_sha,
        scratch_root=artifact_root / "kernelbench-meta-canary" / "worker-attempts",
        authorization_receipt=controller.authorization_receipt,
        gpu=args.gpu,
    )
    evidence = controller.execute(adapter)
    print(
        json.dumps(
            {
                "schema_version": 1,
                "status": evidence.payload["status"],
                "evidence_path": str(evidence.evidence_path),
                "evidence_sha256": evidence.evidence_sha256,
                "formal_activation_minted": False,
                "formal_execution_started": False,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
