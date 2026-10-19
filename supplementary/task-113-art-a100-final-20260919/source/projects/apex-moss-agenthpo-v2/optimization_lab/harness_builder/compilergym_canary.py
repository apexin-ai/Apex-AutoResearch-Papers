from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Sequence

from .adapters.compilergym_subprocess import CompilerGymSubprocessAdapter
from .three_arm_providers import COMPILERGYM_SELECTED_TASKS


CANARY_ACTIONS = (
    "-mem2reg",
    "-instcombine",
    "-simplifycfg",
    "-reassociate",
    "-gvn",
    "-dce",
)


def _canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_once(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != content:
            raise RuntimeError(f"refusing to overwrite CompilerGym canary artifact: {path.name}")
        return
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, suffix=".cbench-canary")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary).replace(path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def run_compilergym_canary(
    *,
    artifact_root: Path,
    python_executable: Path,
    project_root: Path,
    site_data_root: Path,
    cache_root: Path,
    compatibility_library_root: Path,
) -> Path:
    artifact_root = artifact_root.resolve()
    rows: list[dict[str, object]] = []
    for task_id in COMPILERGYM_SELECTED_TASKS:
        uri = f"benchmark://cbench-v1/{task_id}"
        task_root = artifact_root / "instances" / task_id
        candidate_path = task_root / "candidate.json"
        result_path = task_root / "supervisor.json"
        _write_once(
            candidate_path,
            _canonical_bytes(
                {
                    "schema_version": 1,
                    "benchmark_uri": uri,
                    "actions": list(CANARY_ACTIONS),
                }
            ),
        )
        adapter = CompilerGymSubprocessAdapter(
            benchmark_uri=uri,
            python_executable=python_executable,
            project_root=project_root,
            site_data_root=site_data_root,
            cache_root=cache_root,
            compatibility_library_root=compatibility_library_root,
        )
        if result_path.is_file():
            # The adapter deliberately refuses an existing private result.  A
            # completed canary is replayed from the immutable summary instead.
            raise RuntimeError("CompilerGym canary has an incomplete prior attempt")
        result = adapter.evaluate(candidate_path, result_path)
        if not result.correct or result.status != "valid":
            raise RuntimeError(f"CompilerGym canary failed for {task_id}")
        rows.append(
            {
                "task_id": task_id,
                "benchmark_uri": uri,
                "candidate_sha256": result.candidate_sha256,
                "supervisor_sha256": _sha(result_path),
                "normalized_score": result.normalized_score,
                "replay_verified": result.replay_verified,
                "reward_validated": result.reward_validated,
                "semantics_validated": result.semantics_validated,
            }
        )
    summary = {
        "schema_version": 1,
        "suite": "compilergym-cbench",
        "selected_instances": list(COMPILERGYM_SELECTED_TASKS),
        "candidate_policy": "fixed_six_pass_no_model",
        "results": rows,
        "passed": True,
    }
    summary_path = artifact_root / "summary.json"
    _write_once(summary_path, _canonical_bytes(summary))
    return summary_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the pinned CompilerGym cBench canary")
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--python", type=Path, required=True)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--site-data-root", type=Path, required=True)
    parser.add_argument("--cache-root", type=Path, required=True)
    parser.add_argument("--compatibility-library-root", type=Path, required=True)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    if not args.execute:
        parser.error("CompilerGym canary requires explicit --execute")
    path = run_compilergym_canary(
        artifact_root=args.artifact_root,
        python_executable=args.python,
        project_root=args.project_root,
        site_data_root=args.site_data_root,
        cache_root=args.cache_root,
        compatibility_library_root=args.compatibility_library_root,
    )
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
