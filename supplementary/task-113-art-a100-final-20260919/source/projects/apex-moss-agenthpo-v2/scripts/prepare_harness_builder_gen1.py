from __future__ import annotations

import argparse
import json
from pathlib import Path

from optimization_lab.harness_builder.prepare import (
    prepare_hb_gen1,
    resolve_clean_code_revision,
    resolve_model_client_version,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare the blocked, zero-model, zero-evaluator HB-GEN-1 staging plan"
    )
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--artifact-root", type=Path, required=True)
    args = parser.parse_args()
    payload = prepare_hb_gen1(
        project_root=args.project_root,
        artifact_root=args.artifact_root,
        code_revision=resolve_clean_code_revision(args.project_root),
        observed_client_version=resolve_model_client_version(),
    )
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
