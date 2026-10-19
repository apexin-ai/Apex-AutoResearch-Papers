"""Pure-offline, content-addressed KernelBenchX reference canary preparation."""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
from dataclasses import dataclass
from pathlib import Path

from .adapters.kernelbenchx import (
    KernelBenchXTask,
    SnapshotInspector,
    inspect_local_snapshot,
)
from .solutions import KernelBenchXSolutionCodec, SolutionContractError


REFERENCE_CANARY_SCHEMA_VERSION = 1
REFERENCE_CANARY_ARTIFACT_KIND = "kernelbenchx_reference_canary_candidate"
REFERENCE_CANARY_CODEC_ID = "KernelBenchXSolutionCodec-v1"

_SHA256 = re.compile(r"[0-9a-f]{64}")
_MANIFEST_KEYS = {
    "schema_version",
    "artifact_kind",
    "solution_codec",
    "repository_commit",
    "dataset_commit",
    "task_id",
    "task_source_path",
    "task_sha256",
    "source_segment",
    "candidate_sha256",
    "candidate_structural_signature",
    "candidate_object",
}


@dataclass(frozen=True)
class PreparedKernelBenchXReferenceCanary:
    manifest_path: Path
    manifest_sha256: str
    candidate_path: Path
    candidate_sha256: str
    task_id: str
    task_sha256: str


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


def _strict_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate reference manifest key: {key}")
        result[key] = value
    return result


def _read_regular(path: Path, *, limit: int, label: str) -> bytes:
    path = path.absolute()
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise ValueError(f"{label} is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise ValueError(f"{label} must be a regular non-symlink file")
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise ValueError(f"{label} changed type")
            content = stream.read(limit + 1)
    except OSError as exc:
        raise ValueError(f"cannot read {label}") from exc
    if len(content) > limit:
        raise ValueError(f"{label} is too large")
    return content


def _write_immutable(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.exists():
        existing = _read_regular(path, limit=len(content), label="content-addressed object")
        if existing != content:
            raise ValueError("content-addressed object already has different content")
        return
    try:
        descriptor = os.open(
            path,
            os.O_WRONLY
            | os.O_CREAT
            | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0),
            0o400,
        )
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        path.chmod(0o400)
    except FileExistsError:
        existing = _read_regular(path, limit=len(content), label="content-addressed object")
        if existing != content:
            raise ValueError("content-addressed object already has different content")


def _verify_snapshot(
    repository: Path,
    task: KernelBenchXTask,
    inspector: SnapshotInspector,
) -> None:
    identity = inspector(repository, task)
    if identity.repository_commit != task.repository_commit:
        raise ValueError("KernelBenchX repository commit differs")
    if identity.dataset_commit != task.dataset_commit:
        raise ValueError("KernelBenchX dataset commit differs")
    if identity.task_sha256 != task.task_sha256:
        raise ValueError("KernelBenchX task sha256 differs")


def prepare_kernelbenchx_reference_canary(
    *,
    repository: Path,
    task: KernelBenchXTask,
    output_root: Path,
    snapshot_inspector: SnapshotInspector = inspect_local_snapshot,
) -> PreparedKernelBenchXReferenceCanary:
    """Materialize one implementation-only canary without executing candidate code."""

    repository = repository.resolve()
    _verify_snapshot(repository, task, snapshot_inspector)
    source_bytes = _read_regular(
        repository / task.source_path,
        limit=1_048_576,
        label="frozen KernelBenchX task source",
    )
    try:
        task_source = source_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("frozen KernelBenchX task source is not UTF-8") from exc
    if hashlib.sha256(source_bytes).hexdigest() != task.task_sha256:
        raise ValueError("KernelBenchX task sha256 differs")
    try:
        artifact = KernelBenchXSolutionCodec(
            task_id=task.task_id
        ).reference_canary_from_frozen_task_source(
            task_source,
            expected_task_sha256=task.task_sha256,
        )
    except SolutionContractError as exc:
        raise ValueError("frozen task cannot produce a formal reference canary") from exc

    output_root = output_root.resolve()
    candidate_bytes = artifact.text.encode("utf-8")
    candidate_object = f"candidates/{artifact.sha256}.py"
    candidate_path = output_root / candidate_object
    _write_immutable(candidate_path, candidate_bytes)
    manifest = {
        "schema_version": REFERENCE_CANARY_SCHEMA_VERSION,
        "artifact_kind": REFERENCE_CANARY_ARTIFACT_KIND,
        "solution_codec": REFERENCE_CANARY_CODEC_ID,
        "repository_commit": task.repository_commit,
        "dataset_commit": task.dataset_commit,
        "task_id": task.task_id,
        "task_source_path": task.source_path,
        "task_sha256": task.task_sha256,
        "source_segment": "implementation_before_146_hash_separator",
        "candidate_sha256": artifact.sha256,
        "candidate_structural_signature": artifact.structural_signature,
        "candidate_object": candidate_object,
    }
    manifest_bytes = _canonical_bytes(manifest)
    manifest_sha256 = hashlib.sha256(manifest_bytes).hexdigest()
    manifest_path = output_root / "manifests" / f"{manifest_sha256}.json"
    _write_immutable(manifest_path, manifest_bytes)
    return load_kernelbenchx_reference_canary(manifest_path, task=task)


def load_kernelbenchx_reference_canary(
    manifest_path: Path,
    *,
    task: KernelBenchXTask,
) -> PreparedKernelBenchXReferenceCanary:
    """Verify one exact manifest and its formal candidate object."""

    manifest_path = manifest_path.absolute()
    raw = _read_regular(
        manifest_path,
        limit=64 * 1024,
        label="KernelBenchX reference canary manifest",
    )
    manifest_sha256 = hashlib.sha256(raw).hexdigest()
    if manifest_path.name != f"{manifest_sha256}.json":
        raise ValueError("reference manifest filename is not content-addressed")
    try:
        payload = json.loads(raw.decode("utf-8"), object_pairs_hook=_strict_object)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("reference manifest is not exact JSON") from exc
    if not isinstance(payload, dict) or set(payload) != _MANIFEST_KEYS:
        raise ValueError("reference manifest schema differs")
    if _canonical_bytes(payload) != raw:
        raise ValueError("reference manifest is not canonical JSON")
    expected = {
        "schema_version": REFERENCE_CANARY_SCHEMA_VERSION,
        "artifact_kind": REFERENCE_CANARY_ARTIFACT_KIND,
        "solution_codec": REFERENCE_CANARY_CODEC_ID,
        "repository_commit": task.repository_commit,
        "dataset_commit": task.dataset_commit,
        "task_id": task.task_id,
        "task_source_path": task.source_path,
        "task_sha256": task.task_sha256,
        "source_segment": "implementation_before_146_hash_separator",
    }
    for key, value in expected.items():
        if payload[key] != value:
            raise ValueError(f"reference manifest {key} binding differs")
    candidate_sha256 = payload["candidate_sha256"]
    structural_signature = payload["candidate_structural_signature"]
    candidate_object = payload["candidate_object"]
    if (
        type(candidate_sha256) is not str
        or not _SHA256.fullmatch(candidate_sha256)
        or type(structural_signature) is not str
        or not _SHA256.fullmatch(structural_signature)
        or candidate_object != f"candidates/{candidate_sha256}.py"
    ):
        raise ValueError("reference manifest candidate binding is invalid")
    output_root = manifest_path.parent.parent
    if manifest_path.parent.name != "manifests":
        raise ValueError("reference manifest is outside the prepared layout")
    candidate_path = output_root / candidate_object
    candidate_bytes = _read_regular(
        candidate_path,
        limit=1_048_576,
        label="KernelBenchX reference canary candidate",
    )
    if hashlib.sha256(candidate_bytes).hexdigest() != candidate_sha256:
        raise ValueError("reference candidate sha256 binding differs")
    try:
        candidate_source = candidate_bytes.decode("utf-8")
        artifact = KernelBenchXSolutionCodec(task_id=task.task_id).parse(
            f"```python\n{candidate_source.rstrip()}\n```"
        )
    except (UnicodeDecodeError, SolutionContractError) as exc:
        raise ValueError("reference candidate violates the formal solution contract") from exc
    if (
        artifact.sha256 != candidate_sha256
        or artifact.structural_signature != structural_signature
    ):
        raise ValueError("reference candidate canonical binding differs")
    return PreparedKernelBenchXReferenceCanary(
        manifest_path=manifest_path,
        manifest_sha256=manifest_sha256,
        candidate_path=candidate_path,
        candidate_sha256=candidate_sha256,
        task_id=task.task_id,
        task_sha256=task.task_sha256,
    )


__all__ = [
    "PreparedKernelBenchXReferenceCanary",
    "load_kernelbenchx_reference_canary",
    "prepare_kernelbenchx_reference_canary",
]
