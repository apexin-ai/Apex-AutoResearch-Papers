"""Pure-offline, fail-closed SWE-Perf source-lock preparation.

This preparer deliberately cannot mint :class:`WrapperSourceLock`.  It verifies
the pinned public sources and records the exact blockers that must be closed by
a later, separately authorized evaluator redesign and image preflight.  The
current in-process pytest result topology is mechanically unattestable; an
image rebuild alone cannot clear it.  In particular,
Parquet gold columns are never requested from Arrow.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from ..adapters.sweperf import (
    DATASET_COMMIT,
    DATASET_PARQUET_SHA256,
    EVALUATOR_COMMIT,
    FROZEN_TASKS,
    SWEPERF_EVALUATOR_ID,
)
from ..schema import PilotManifest
from .trusted_result import (
    RESULT_CHANNEL_REASON_CODE,
    result_channel_capability_verdict,
)


PUBLIC_DATASET_COLUMNS = (
    "repo",
    "instance_id",
    "base_commit",
    "version",
    "efficiency_test",
    "test_functions",
    "problem_statement_realistic",
)
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_MAX_PARQUET_BYTES = 256 * 1024 * 1024
_DEFAULT_MANIFEST = (
    Path(__file__).resolve().parents[1] / "data" / "hb_gen1_candidates.json"
)


@dataclass(frozen=True)
class BlockedSourceLockPrepare:
    status: str
    runnable_wrapper_source_lock: bool
    content_id: str
    report_path: Path


def _canonical_bytes(value: Mapping[str, Any]) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("ascii")


def _pretty_bytes(value: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=True,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("ascii")


def _fixed_blocker(code: str, scope: str) -> dict[str, str]:
    return {"code": code, "scope": scope}


def _detached_head(path: Path) -> str | None:
    try:
        if path.is_symlink() or not path.is_dir():
            return None
        git_dir = path / ".git"
        head = git_dir / "HEAD"
        if git_dir.is_symlink() or not git_dir.is_dir():
            return None
        metadata = head.lstat()
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            return None
        if metadata.st_size != 41:
            return None
        descriptor = os.open(head, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            raw = stream.read(42)
        value = raw.decode("ascii", errors="strict").strip()
    except (OSError, UnicodeDecodeError):
        return None
    return value if _COMMIT.fullmatch(value) else None


def _parquet_digest(path: Path, dataset_repo: Path) -> str | None:
    try:
        if path.is_symlink():
            return None
        metadata = path.lstat()
        if (
            not stat.S_ISREG(metadata.st_mode)
            or metadata.st_size <= 0
            or metadata.st_size > _MAX_PARQUET_BYTES
        ):
            return None
        resolved_repo = dataset_repo.resolve(strict=True)
        resolved_path = path.resolve(strict=True)
        if not resolved_path.is_relative_to(resolved_repo):
            return None
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        digest = hashlib.sha256()
        with os.fdopen(descriptor, "rb") as stream:
            while chunk := stream.read(1024 * 1024):
                digest.update(chunk)
        return digest.hexdigest()
    except OSError:
        return None


def _validate_manifest(path: Path) -> str | None:
    try:
        manifest = PilotManifest.from_json(path)
        pool = next(item for item in manifest.benchmarks if item.suite == "swe-perf")
    except (
        OSError,
        ValueError,
        TypeError,
        KeyError,
        StopIteration,
        json.JSONDecodeError,
    ):
        return "frozen_task_hash_mismatch"
    expected_ids = tuple(FROZEN_TASKS)
    if (
        pool.repository_commit != EVALUATOR_COMMIT
        or pool.dataset_commit != DATASET_COMMIT
        or pool.evaluator != SWEPERF_EVALUATOR_ID
        or pool.selected_heldout != expected_ids
        or tuple(item.task_id for item in pool.candidates) != expected_ids
    ):
        return "frozen_task_hash_mismatch"
    for item in pool.candidates:
        task = FROZEN_TASKS[item.task_id]
        if (
            item.source_sha256 != task.task_sha256
            or item.source_path != f"dataset://SWE-Perf/test/{item.task_id}"
            or not item.eligible
        ):
            return "frozen_task_hash_mismatch"
    return None


def _safe_repo_path(value: str) -> str:
    if not isinstance(value, str) or not value or len(value) > 240:
        raise ValueError("unsafe public test_functions path")
    if "\\" in value or "\x00" in value or any(ord(ch) < 32 for ch in value):
        raise ValueError("unsafe public test_functions path")
    path = PurePosixPath(value)
    if (
        path.is_absolute()
        or path.as_posix() != value
        or not path.parts
        or any(part in {"", ".", ".."} or part.lower() == ".git" for part in path.parts)
    ):
        raise ValueError("unsafe public test_functions path")
    return value


def _strict_object(raw: str) -> dict[str, Any]:
    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate public test_functions key")
            result[key] = value
        return result

    value = json.loads(raw, object_pairs_hook=unique)
    if not isinstance(value, dict) or not value:
        raise ValueError("public test_functions must be a non-empty object")
    return value


def _public_tasks(parquet_path: Path) -> tuple[list[dict[str, Any]], int]:
    # Import lazily so absence of the pinned offline reader becomes a blocker,
    # not an implicit package install or network action.
    import pyarrow.parquet as parquet  # type: ignore[import-not-found]

    parquet_file = parquet.ParquetFile(parquet_path)
    if any(column not in parquet_file.schema_arrow.names for column in PUBLIC_DATASET_COLUMNS):
        raise ValueError("public dataset schema differs")
    table = parquet_file.read(columns=list(PUBLIC_DATASET_COLUMNS))
    rows = table.to_pylist()
    selected = [row for row in rows if row.get("instance_id") in FROZEN_TASKS]
    if tuple(row.get("instance_id") for row in selected) != tuple(FROZEN_TASKS):
        raise ValueError("frozen dataset row order differs")
    if len(selected) != len(FROZEN_TASKS):
        raise ValueError("frozen dataset rows differ")

    result: list[dict[str, Any]] = []
    for row, task in zip(selected, FROZEN_TASKS.values(), strict=True):
        if (
            row.get("repo") != task.repository
            or row.get("base_commit") != task.base_commit
            or not isinstance(row.get("version"), str)
            or not row["version"]
        ):
            raise ValueError("frozen public row binding differs")
        efficiency = row.get("efficiency_test")
        if (
            not isinstance(efficiency, list)
            or not efficiency
            or any(
                not isinstance(item, str)
                or not item
                or len(item) > 4096
                or "\x00" in item
                or "\n" in item
                for item in efficiency
            )
            or len(efficiency) != len(set(efficiency))
        ):
            raise ValueError("public efficiency tests differ")
        raw_functions = row.get("test_functions")
        if not isinstance(raw_functions, str) or len(raw_functions) > 2 * 1024 * 1024:
            raise ValueError("public test_functions differs")
        functions = _strict_object(raw_functions)
        normalized: dict[str, list[str]] = {}
        for path, names in sorted(functions.items()):
            safe_path = _safe_repo_path(path)
            if (
                not isinstance(names, list)
                or not names
                or any(
                    not isinstance(name, str)
                    or not name
                    or len(name) > 1024
                    or "\x00" in name
                    or "\n" in name
                    for name in names
                )
            ):
                raise ValueError("public test_functions values differ")
            normalized[safe_path] = list(names)
        problem = row.get("problem_statement_realistic")
        if not isinstance(problem, str) or not problem or len(problem) > 1024 * 1024:
            raise ValueError("public realistic problem differs")
        result.append(
            {
                "instance_id": task.instance_id,
                "repository": task.repository,
                "base_commit": task.base_commit,
                "version": row["version"],
                "task_sha256": task.task_sha256,
                "efficiency_test": list(efficiency),
                "test_functions": normalized,
                "allowed_patch_paths": list(normalized),
                "realistic_problem_sha256": hashlib.sha256(
                    problem.encode("utf-8")
                ).hexdigest(),
            }
        )
    return result, len(rows)


def _write_once(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.parent.is_symlink() or not path.parent.is_dir():
        raise ValueError("source-lock output root is unsafe")
    if path.exists() or path.is_symlink():
        if path.is_symlink() or path.read_bytes() != raw:
            raise ValueError("refusing to overwrite a different source-lock report")
        return
    descriptor, name = tempfile.mkstemp(prefix=".sweperf-source-lock-", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, 0o444)
        os.replace(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def prepare_sweperf_source_lock(
    *,
    evaluator_repo: Path,
    dataset_repo: Path,
    parquet_path: Path,
    output_root: Path,
    pilot_manifest_path: Path = _DEFAULT_MANIFEST,
) -> BlockedSourceLockPrepare:
    """Verify public pinned inputs and emit only a content-addressed blocker report."""

    evaluator_head = _detached_head(Path(evaluator_repo))
    dataset_head = _detached_head(Path(dataset_repo))
    observed_parquet = _parquet_digest(Path(parquet_path), Path(dataset_repo))
    blockers: list[dict[str, str]] = []
    if evaluator_head != EVALUATOR_COMMIT:
        blockers.append(_fixed_blocker("evaluator_commit_mismatch", "evaluator_source"))
    if dataset_head != DATASET_COMMIT:
        blockers.append(_fixed_blocker("dataset_commit_mismatch", "dataset_source"))
    if observed_parquet != DATASET_PARQUET_SHA256:
        blockers.append(
            _fixed_blocker("dataset_parquet_sha256_mismatch", "dataset_source")
        )
    manifest_error = _validate_manifest(Path(pilot_manifest_path))
    if manifest_error is not None:
        blockers.append(_fixed_blocker(manifest_error, "frozen_task_manifest"))

    tasks: list[dict[str, Any]] = []
    total_rows: int | None = None
    rows_loaded = False
    source_valid = not blockers
    if source_valid:
        try:
            tasks, total_rows = _public_tasks(Path(parquet_path))
            # Detect local replacement during the projected-column read.
            if _parquet_digest(Path(parquet_path), Path(dataset_repo)) != observed_parquet:
                tasks = []
                total_rows = None
                blockers.append(
                    _fixed_blocker("dataset_changed_during_prepare", "dataset_source")
                )
            else:
                rows_loaded = True
        except (ImportError, OSError, ValueError, TypeError):
            tasks = []
            total_rows = None
            blockers.append(_fixed_blocker("public_dataset_projection_invalid", "dataset_source"))

    # These are hard blockers in the current revision.  This command does not
    # invoke Docker to manufacture local RepoDigest evidence, and the current
    # wrapper lets arbitrary candidate Python and the pytest reporter share one
    # uid-65534 process.  Root ownership after exit cannot attest either the
    # per-test outcome or the pytest call duration.
    blockers.extend(
        (
            _fixed_blocker("local_repo_digest_unverified", "all_frozen_tasks"),
            _fixed_blocker(
                RESULT_CHANNEL_REASON_CODE, "wrapper_result_channel"
            ),
        )
    )
    core: dict[str, Any] = {
        "schema_version": 1,
        "artifact_kind": "hb-gen1-sweperf-source-lock-prepare",
        "status": "blocked",
        "runnable_wrapper_source_lock": False,
        "source_binding": {
            "evaluator_commit": EVALUATOR_COMMIT,
            "dataset_commit": DATASET_COMMIT,
            "dataset_parquet_sha256": DATASET_PARQUET_SHA256,
        },
        "source_observations": {
            "evaluator_commit": evaluator_head,
            "dataset_commit": dataset_head,
            "dataset_parquet_sha256": observed_parquet,
        },
        "loaded_dataset_columns": list(PUBLIC_DATASET_COLUMNS),
        "dataset_rows_loaded": rows_loaded,
        "dataset_total_rows": total_rows,
        "frozen_task_order": list(FROZEN_TASKS),
        "tasks": tasks,
        "upstream_images": {
            "status": "unverified",
            "repo_digests": {},
            "docker_inspect_invoked": False,
        },
        "command_trust": {
            "status": "blocked",
            "report_writer": "candidate_worker_uid_65534",
            "report_consumer": "root_supervisor",
            "reason_code": RESULT_CHANNEL_REASON_CODE,
            "capability_verdict": result_channel_capability_verdict().to_dict(),
        },
        "blockers": sorted(blockers, key=lambda item: (item["code"], item["scope"])),
        "external_actions": {
            "docker_invoked": False,
            "evaluator_invoked": False,
            "gpu_used": False,
            "model_invoked": False,
            "network_used": False,
        },
    }
    content_id = hashlib.sha256(_canonical_bytes(core)).hexdigest()
    payload = {**core, "content_id": content_id}
    report_path = Path(output_root) / f"{content_id}.json"
    _write_once(report_path, _pretty_bytes(payload))
    return BlockedSourceLockPrepare(
        status="blocked",
        runnable_wrapper_source_lock=False,
        content_id=content_id,
        report_path=report_path.resolve(),
    )


__all__ = [
    "BlockedSourceLockPrepare",
    "PUBLIC_DATASET_COLUMNS",
    "prepare_sweperf_source_lock",
]
