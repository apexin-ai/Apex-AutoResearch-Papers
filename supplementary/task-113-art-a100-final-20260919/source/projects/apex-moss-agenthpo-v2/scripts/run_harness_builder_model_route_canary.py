#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import secrets
from pathlib import Path

from optimization_lab.codex_generator import CodexExecGenerator
from optimization_lab.harness_builder.model_route_canary import (
    FROZEN_REASONING_EFFORT,
    ModelRouteCanaryBlocked,
    ModelRouteCanaryRunner,
)
from optimization_lab.harness_builder.prepare import (
    resolve_clean_code_revision,
    resolve_model_client_version,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Preflight one signed HB-GEN-1 model-route canary. No model call is "
            "made unless --execute is supplied explicitly."
        )
    )
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--codex-executable", default="codex")
    parser.add_argument(
        "--prior-canary-artifact-root",
        type=Path,
        action="append",
        default=[],
        help=(
            "Obsolete HB-GEN-1 artifact root whose verified model canary counts "
            "against the same two-call entitlement but is never reused"
        ),
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Consume one frozen canary:model-route call if no replay is available",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    project_root = args.project_root.resolve()
    artifact_root = args.artifact_root.resolve()
    try:
        code_revision = resolve_clean_code_revision(project_root)
        client_version = resolve_model_client_version(args.codex_executable)
        prior_roots = tuple(path.resolve() for path in args.prior_canary_artifact_root)
        if not prior_roots:
            legacy_root = artifact_root.parent / "harness-builder-gen1"
            if (legacy_root / "model-canary" / "summary.json").is_file():
                prior_roots = (legacy_root.resolve(),)

        def transport_factory(work_root: Path, output_mode: str) -> CodexExecGenerator:
            return CodexExecGenerator(
                work_root=work_root,
                executable=args.codex_executable,
                reasoning_effort=FROZEN_REASONING_EFFORT,
                output_mode=output_mode,
            )

        runner = ModelRouteCanaryRunner(
            project_root=project_root,
            artifact_root=artifact_root,
            observed_code_revision=code_revision,
            observed_client_version=client_version,
            transport_factory=transport_factory,
            signing_key=secrets.token_bytes(32),
            prior_canary_artifact_roots=prior_roots,
        )
        report = runner.execute() if args.execute else runner.preflight()
    except (ModelRouteCanaryBlocked, ValueError, OSError) as exc:
        report = {
            "schema_version": 1,
            "status": "blocked",
            "blockers": [type(exc).__name__],
            "message": str(exc),
            "model_calls_started_by_this_command": 0 if not args.execute else None,
        }
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
        return 2
    except Exception:
        # Provider/authentication errors are deliberately not copied into a public
        # report because they may contain credentials or private endpoint details.
        report = {
            "schema_version": 1,
            "status": "blocked",
            "blockers": ["provider_or_transport_error"],
            "message": "model-route provider or transport failed",
            "model_calls_started_by_this_command": None,
        }
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
        return 2
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] in {"ready", "passed"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
