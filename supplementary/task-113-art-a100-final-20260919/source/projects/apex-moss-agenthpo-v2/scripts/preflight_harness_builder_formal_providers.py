#!/usr/bin/env python3
"""Pure-offline HB-GEN-1 formal suite-provider composition preflight."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from optimization_lab.harness_builder.formal_providers import (
    FormalProviderCompositionConfig,
    preflight_formal_providers,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Verify the frozen HB-GEN-1 staging/manifest, suite canary journals, "
            "and SWE-Perf source-lock receipt without starting any runtime"
        )
    )
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--kernelbenchx-repository", type=Path, required=True)
    parser.add_argument("--kernelbenchx-supervisor", type=Path, required=True)
    parser.add_argument("--kernelbenchx-scratch-root", type=Path, required=True)
    parser.add_argument("--kernelbenchx-gpu", default="4")
    parser.add_argument("--sweperf-source-lock-receipt", type=Path, required=True)
    parser.add_argument(
        "--component-rebind-root",
        type=Path,
        help="Defaults to ARTIFACT_ROOT/component-rebinds",
    )
    parser.add_argument(
        "--staging-plan",
        type=Path,
        help="Defaults to ARTIFACT_ROOT/staging_plan.json",
    )
    parser.add_argument(
        "--kernelbenchx-canary-root",
        type=Path,
        help="Defaults to ARTIFACT_ROOT/evaluator-canaries/kernelbenchx",
    )
    parser.add_argument(
        "--compilergym-canary-root",
        type=Path,
        help="Defaults to ARTIFACT_ROOT/evaluator-canaries/compilergym-cbench",
    )
    parser.add_argument("--sweperf-canary-root", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    artifact_root = args.artifact_root.resolve()
    config = FormalProviderCompositionConfig(
        project_root=args.project_root.resolve(),
        staging_plan_path=(
            args.staging_plan.resolve()
            if args.staging_plan is not None
            else artifact_root / "staging_plan.json"
        ),
        manifest_path=args.manifest.resolve(),
        kernelbenchx_repository=args.kernelbenchx_repository.resolve(),
        kernelbenchx_supervisor=args.kernelbenchx_supervisor.absolute(),
        kernelbenchx_scratch_root=args.kernelbenchx_scratch_root.resolve(),
        kernelbenchx_gpu=args.kernelbenchx_gpu,
        kernelbenchx_canary_root=(
            args.kernelbenchx_canary_root.resolve()
            if args.kernelbenchx_canary_root is not None
            else artifact_root / "evaluator-canaries" / "kernelbenchx"
        ),
        compilergym_canary_root=(
            args.compilergym_canary_root.resolve()
            if args.compilergym_canary_root is not None
            else artifact_root / "evaluator-canaries" / "compilergym-cbench"
        ),
        sweperf_source_lock_receipt=args.sweperf_source_lock_receipt.resolve(),
        component_rebind_root=(
            args.component_rebind_root.resolve()
            if args.component_rebind_root is not None
            else artifact_root / "component-rebinds"
        ),
        sweperf_canary_root=(
            args.sweperf_canary_root.resolve()
            if args.sweperf_canary_root is not None
            else None
        ),
    )
    report = preflight_formal_providers(config)
    print(json.dumps(report.to_dict(), ensure_ascii=False, sort_keys=True))
    # A blocked preflight is an auditable result, not a failed command.  The
    # formal execute path separately refuses to construct the provider factory.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
