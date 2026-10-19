from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Sequence

from .adapters.lcbench import LCBenchAdapter, LCBenchQueryBatch, LCBenchTask


LCBENCH_SELECTED_INSTANCES = (
    "167168",
    "168331",
    "168910",
    "189866",
    "167181",
    "167190",
    "34539",
    "189908",
)
LCBENCH_ONLINE_INSTANCES = LCBENCH_SELECTED_INSTANCES[:6]
LCBENCH_SEALED_INSTANCES = LCBENCH_SELECTED_INSTANCES[6:]
LCBENCH_DATA_COMMIT = "efdab9072f63bd680396cd4b78b927c4a0caaad3"
LCBENCH_SOURCE_HASHES = {
    "model.onnx": "b45c0d85ae39abf8820c8bea5ac82f415763afcbaf3b725e36af452b09cb6dcd",
    "config_space.json": "4d1c78a91429b4a37628e13f286cf1abe15f778a09722a4c01714f2d72a8200d",
    "encoding.json": "d8af928f412bbeb07e58ecd69877fcab35fbc595333d1c1c3f76120d2f2508da",
}
LCBENCH_SELECTION_SEED = "hb-three-arm-v1"


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
            raise RuntimeError(f"refusing to overwrite LCBench canary artifact: {path.name}")
        return
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, suffix=".lcbench-canary")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary).replace(path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def _canary_batch(instance_id: str) -> LCBenchQueryBatch:
    # The canary covers every boundary and every field without using a score to
    # choose a formal query.  Formal model batches remain first encounters.
    queries = []
    for index in range(16):
        fraction = index / 15
        queries.append(
            {
                "batch_size": 16 + index * 31,
                "learning_rate": min(
                    0.10000000000000002,
                    0.00010000000000000009 * (1000 ** fraction),
                ),
                "max_dropout": fraction,
                "max_units": 64 + index * 64,
                "momentum": 0.1 + 0.89 * fraction,
                "num_layers": 1 + index % 5,
                "weight_decay": 0.00001 * (10000 ** fraction),
            }
        )
    return LCBenchQueryBatch.from_bytes(
        _canonical_bytes(
            {
                "schema_version": 1,
                "instance_id": instance_id,
                "queries": queries,
            }
        ),
        expected_instance_id=instance_id,
    )


def run_lcbench_canary(
    *,
    artifact_root: Path,
    data_root: Path,
    settings_path: Path,
    python_executable: Path,
) -> Path:
    artifact_root = artifact_root.resolve()
    data_root = data_root.resolve(strict=True)
    settings_path = settings_path.resolve(strict=True)
    # Keep the venv launcher path rather than resolving its symlink to the base
    # interpreter, otherwise Python will not activate the pinned site-packages.
    python_executable = python_executable.absolute()
    if not python_executable.is_file():
        raise RuntimeError("LCBench pinned Python executable is missing")
    actual_hashes = {name: _sha(data_root / name) for name in LCBENCH_SOURCE_HASHES}
    if actual_hashes != LCBENCH_SOURCE_HASHES:
        raise RuntimeError("LCBench canary source hashes differ from the frozen data")
    selected = sorted(
        LCBENCH_SELECTED_INSTANCES,
        key=lambda instance_id: hashlib.sha256(
            f"{LCBENCH_SELECTION_SEED}|yahpo-lcbench|{instance_id}".encode("utf-8")
        ).hexdigest(),
    )
    if tuple(selected) != LCBENCH_SELECTED_INSTANCES:
        raise RuntimeError("LCBench selected instance order differs")

    rows: list[dict[str, object]] = []
    for instance_id in LCBENCH_SELECTED_INSTANCES:
        instance_root = artifact_root / "instances" / instance_id
        candidate_path = instance_root / "candidate.json"
        result_path = instance_root / "private-result.json"
        batch = _canary_batch(instance_id)
        _write_once(candidate_path, _canonical_bytes(batch.to_dict()))
        task = LCBenchTask(
            instance_id=instance_id,
            data_root=data_root,
            settings_path=settings_path,
            python_executable=python_executable,
            model_sha256=LCBENCH_SOURCE_HASHES["model.onnx"],
            config_space_sha256=LCBENCH_SOURCE_HASHES["config_space.json"],
            encoding_sha256=LCBENCH_SOURCE_HASHES["encoding.json"],
            settings_sha256=_sha(settings_path),
        )
        result = LCBenchAdapter(task=task).evaluate(candidate_path, result_path)
        if not result.correct or result.status != "valid":
            raise RuntimeError(f"LCBench canary failed for instance {instance_id}")
        rows.append(
            {
                "instance_id": instance_id,
                "candidate_sha256": result.candidate_sha256,
                "private_result_sha256": _sha(result_path),
                "query_count": result.query_count,
                "best_validation_score": result.best_validation_score,
                "status": result.status,
            }
        )

    summary = {
        "schema_version": 1,
        "suite": "yahpo-lcbench",
        "data_commit": LCBENCH_DATA_COMMIT,
        "source_hashes": LCBENCH_SOURCE_HASHES,
        "settings_sha256": _sha(settings_path),
        "python_executable": str(python_executable),
        "selection_seed": LCBENCH_SELECTION_SEED,
        "online_instances": list(LCBENCH_ONLINE_INSTANCES),
        "sealed_instances": list(LCBENCH_SEALED_INSTANCES),
        "results": rows,
        "passed": True,
    }
    summary_path = artifact_root / "summary.json"
    _write_once(summary_path, _canonical_bytes(summary))
    return summary_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the pinned LCBench no-model canary")
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--settings", type=Path, required=True)
    parser.add_argument("--python", type=Path, required=True)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    if not args.execute:
        parser.error("LCBench canary requires explicit --execute")
    summary_path = run_lcbench_canary(
        artifact_root=args.artifact_root,
        data_root=args.data_root,
        settings_path=args.settings,
        python_executable=args.python,
    )
    print(summary_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "LCBENCH_DATA_COMMIT",
    "LCBENCH_ONLINE_INSTANCES",
    "LCBENCH_SEALED_INSTANCES",
    "LCBENCH_SELECTED_INSTANCES",
    "LCBENCH_SELECTION_SEED",
    "LCBENCH_SOURCE_HASHES",
    "run_lcbench_canary",
]
