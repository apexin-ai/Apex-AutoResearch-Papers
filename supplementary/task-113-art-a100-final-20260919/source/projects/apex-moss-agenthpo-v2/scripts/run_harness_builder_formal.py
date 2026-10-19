#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path
from typing import Callable, Sequence

from optimization_lab.harness_builder.formal import (
    FormalCampaignContract,
    FormalCampaignRunner,
)


RunnerFactory = Callable[[FormalCampaignContract], FormalCampaignRunner]


def _preflight(
    staging_path: Path, *, require_full_stream: bool = True
) -> tuple[dict[str, object], FormalCampaignContract | None]:
    blockers: list[str] = []
    contract: FormalCampaignContract | None = None
    if not staging_path.is_file():
        blockers.append("staging_plan_missing")
    else:
        try:
            contract = FormalCampaignContract.from_staging_path(
                staging_path, require_full_stream=require_full_stream
            )
        except (OSError, ValueError) as exc:
            blockers.append(f"staging_plan_invalid:{type(exc).__name__}")
        else:
            if not contract.execution_ready:
                blockers.extend(contract.blockers or ("staging_execution_not_ready",))
    report: dict[str, object] = {
        "schema_version": 1,
        "phase": "hb-gen1-formal-prequential",
        "staging_plan": str(staging_path.resolve()),
        "staging_plan_sha256": (
            contract.staging_plan_sha256 if contract is not None else None
        ),
        "stream_instances": len(contract.stream) if contract is not None else 0,
        "staging_execution_ready": bool(
            contract is not None and contract.execution_ready
        ),
        "execution_ready": not blockers,
        "blockers": sorted(set(blockers)),
        "model_calls_started": 0,
        "evaluator_transactions_started": 0,
        "no_next_phase": True,
    }
    return report, contract


def main(
    argv: Sequence[str] | None = None,
    *,
    runner_factory: RunnerFactory | None = None,
    require_full_stream: bool = True,
) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Preflight or explicitly execute the frozen HB-GEN-1 formal "
            "prequential controller"
        )
    )
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument(
        "--staging-plan",
        type=Path,
        help="Defaults to ARTIFACT_ROOT/staging_plan.json",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Enter the injected formal runtime only when staging execution_ready=true",
    )
    args = parser.parse_args(argv)
    artifact_root = args.artifact_root.resolve()
    staging_path = (
        args.staging_plan.resolve()
        if args.staging_plan is not None
        else artifact_root / "staging_plan.json"
    )
    report, contract = _preflight(
        staging_path, require_full_stream=require_full_stream
    )
    if not args.execute:
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
        return 0
    if contract is None or not report["execution_ready"]:
        raise RuntimeError(
            "HB-GEN-1 formal execution remains blocked: "
            + ", ".join(report["blockers"])
        )
    contract.require_executable()
    if runner_factory is None:
        raise RuntimeError(
            "HB-GEN-1 formal runtime composition is not bound; preflight cannot "
            "construct or guess a suite evaluator/provider factory"
        )
    result = runner_factory(contract).run()
    print(
        json.dumps(
            {
                "schema_version": 1,
                "phase": "hb-gen1-formal-prequential",
                "staging_plan_sha256": contract.staging_plan_sha256,
                "result": asdict(result),
                "no_next_phase": True,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
