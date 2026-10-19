from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.harness_builder.sweperf_wrapper import (
    WrapperSourceLock,
    prepare_wrapper_build_contexts,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare deterministic offline HB-GEN-1 SWE-Perf wrapper build "
            "contexts; this command never invokes Docker or the evaluator"
        )
    )
    parser.add_argument("--source-lock", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    source_lock = WrapperSourceLock.from_json(args.source_lock)
    contexts = prepare_wrapper_build_contexts(
        source_lock=source_lock,
        output_root=args.output_root,
    )
    payload = {
        "schema_version": 1,
        "docker_invoked": False,
        "network_used": False,
        "contexts": [
            {
                "instance_id": item.instance_id,
                "context_dir": str(item.context_dir),
                "task_manifest_sha256": item.task_manifest_sha256,
                "supervisor_bundle_sha256": item.supervisor_bundle_sha256,
                "context_sha256": item.context_sha256,
                "wrapper_identity": {
                    "instance_id": item.wrapper_identity.instance_id,
                    "task_sha256": item.wrapper_identity.task_sha256,
                    "task_manifest_sha256": (
                        item.wrapper_identity.task_manifest_sha256
                    ),
                    "supervisor_bundle_sha256": (
                        item.wrapper_identity.supervisor_bundle_sha256
                    ),
                    "upstream_ref_sha256": item.wrapper_identity.upstream_ref_sha256,
                    "resource_limits_sha256": (
                        item.wrapper_identity.resource_limits_sha256
                    ),
                },
            }
            for item in contexts
        ],
        "build_required": True,
        "canary_required": True,
    }
    print(json.dumps(payload, ensure_ascii=True, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
