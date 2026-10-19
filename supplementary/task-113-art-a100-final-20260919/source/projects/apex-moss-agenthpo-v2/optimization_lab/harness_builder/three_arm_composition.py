"""Content-addressed composition of a frozen v1r8 prefix and v1r9 suffix.

The composition contains references only.  It never copies historical receipts,
and it refuses to materialize until all 24 referenced instances and their 72 arm
receipts are sealed and content-bound.
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

from .three_arm import THREE_ARMS, ThreeArmStreamItem
from .three_arm_continuation import (
    ThreeArmContinuationContract,
    ThreeArmContinuationSourceSnapshot,
    verify_three_arm_continuation_source,
)


COMPOSITION_SCHEMA_VERSION = 1
COMPOSITION_KIND = "three_arm_composition_manifest"
COMPOSITION_PREFIX_LENGTH = 6
COMPOSITION_INSTANCE_COUNT = 24
SOURCE_PREFIX_SEGMENT_ID = "v1r8-prefix"
SUCCESSOR_SUFFIX_SEGMENT_ID = "v1r9-successor"

_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_SEGMENT_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._+-]{0,127}\Z")
_INSTANCE_RECEIPT_FIELDS = {
    "schema_version",
    "phase_id",
    "staging_plan_sha256",
    "stream_item",
    "learning_mode",
    "first_encounter",
    "same_instance_rerun_policy",
    "task_binding_sha256",
    "input_online_checkpoint_sha256",
    "input_online_bank_sha256",
    "arm_order",
    "arm_receipt_sha256s",
    "trajectory_sha256",
    "distillation_operation_id",
    "output_online_bank_sha256",
    "output_online_checkpoint_sha256",
    "sealed",
    "no_next_phase",
}


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _require_sha(value: object, label: str) -> str:
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise ValueError(f"invalid {label} sha256")
    return value


def _relative(value: str, label: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"invalid {label} relative path")
    parsed = PurePosixPath(value)
    if parsed.is_absolute() or "." in parsed.parts or ".." in parsed.parts:
        raise ValueError(f"invalid {label} relative path")
    return parsed


def _regular_file(root: Path, relative_path: str, *, label: str) -> Path:
    relative = _relative(relative_path, label)
    resolved_root = Path(root).resolve(strict=True)
    candidate = resolved_root.joinpath(*relative.parts)
    try:
        metadata = candidate.lstat()
    except FileNotFoundError as exc:
        raise ValueError(f"missing {label}") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise ValueError(f"{label} must be a regular non-symlink file")
    try:
        candidate.resolve(strict=True).relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"{label} escapes its segment root") from exc
    return candidate


def _read_json_object(path: Path, *, label: str) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} is invalid JSON") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{label} must be a JSON object")
    return payload, raw


def _read_canonical_json(path: Path, *, label: str) -> tuple[dict[str, Any], bytes]:
    payload, raw = _read_json_object(path, label=label)
    if _canonical_bytes(payload) != raw:
        raise ValueError(f"{label} is not canonical")
    return payload, raw


def _validate_arm_receipts(
    receipt_path: Path,
    *,
    item: ThreeArmStreamItem,
    staging_plan_sha256: str,
    expected_hashes: object,
) -> None:
    if not isinstance(expected_hashes, dict) or set(expected_hashes) != set(THREE_ARMS):
        raise ValueError("instance receipt must bind exactly three arm receipts")
    for arm in THREE_ARMS:
        expected_sha = _require_sha(expected_hashes[arm], f"{arm} arm receipt")
        arm_path = receipt_path.parent / "arms" / f"{arm}.json"
        try:
            metadata = arm_path.lstat()
        except FileNotFoundError as exc:
            raise ValueError(f"missing {arm} arm receipt") from exc
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise ValueError(f"{arm} arm receipt must be a regular non-symlink file")
        try:
            arm_path.resolve(strict=True).relative_to(
                receipt_path.parent.resolve(strict=True)
            )
        except ValueError as exc:
            raise ValueError(f"{arm} arm receipt escapes its instance root") from exc
        arm_payload, arm_raw = _read_canonical_json(
            arm_path, label=f"{arm} arm receipt"
        )
        if _sha256(arm_raw) != expected_sha:
            raise ValueError(f"{arm} arm receipt hash differs")
        curve = arm_payload.get("curve")
        rounds = curve.get("rounds") if isinstance(curve, dict) else None
        if (
            arm_payload.get("schema_version") != 1
            or arm_payload.get("staging_plan_sha256") != staging_plan_sha256
            or arm_payload.get("stream_index") != item.stream_index
            or arm_payload.get("instance_id") != item.instance_id
            or arm_payload.get("arm") != arm
            or arm_payload.get("sealed") is not True
            or not isinstance(rounds, list)
            or len(rounds) != 8
            or not all(isinstance(point, dict) for point in rounds)
        ):
            raise ValueError(f"{arm} arm receipt is not a sealed eight-round receipt")


def _validate_instance_receipt(
    receipt_path: Path,
    *,
    expected_item: ThreeArmStreamItem,
    phase_id: str,
    staging_plan_sha256: str,
    expected_receipt_sha256: str | None = None,
) -> tuple[str, str]:
    payload, raw = _read_canonical_json(receipt_path, label="instance receipt")
    digest = _sha256(raw)
    if expected_receipt_sha256 is not None and digest != expected_receipt_sha256:
        raise ValueError(
            f"instance receipt hash differs at stream index {expected_item.stream_index}"
        )
    if set(payload) != _INSTANCE_RECEIPT_FIELDS or (
        payload.get("schema_version") != 2
        or payload.get("phase_id") != phase_id
        or payload.get("staging_plan_sha256") != staging_plan_sha256
        or payload.get("stream_item") != expected_item.to_dict()
        or payload.get("learning_mode") != expected_item.learning_mode
        or payload.get("first_encounter") is not True
        or payload.get("same_instance_rerun_policy")
        != "replay_only_no_formal_update"
        or payload.get("arm_order") != list(expected_item.arm_order)
        or payload.get("sealed") is not True
        or payload.get("no_next_phase") is not True
    ):
        raise ValueError(
            f"instance receipt is not sealed or is rebound at stream index "
            f"{expected_item.stream_index}"
        )
    for field in (
        "task_binding_sha256",
        "trajectory_sha256",
        "input_online_checkpoint_sha256",
        "input_online_bank_sha256",
        "output_online_checkpoint_sha256",
        "output_online_bank_sha256",
    ):
        _require_sha(payload.get(field), f"instance receipt {field}")
    expected_distillation = (
        f"distill:{expected_item.stream_index:03d}:"
        f"{expected_item.instance_id}:distillation_call"
    )
    if expected_item.learning_mode == "online":
        if payload.get("distillation_operation_id") != expected_distillation:
            raise ValueError("online instance receipt distillation binding differs")
    elif payload.get("distillation_operation_id") is not None:
        raise ValueError("sealed instance receipt cannot bind distillation")
    _validate_arm_receipts(
        receipt_path,
        item=expected_item,
        staging_plan_sha256=staging_plan_sha256,
        expected_hashes=payload.get("arm_receipt_sha256s"),
    )
    return receipt_path.as_posix(), digest


def _prefix_entries(
    *,
    source_root: Path,
    snapshot: ThreeArmContinuationSourceSnapshot,
    contract: ThreeArmContinuationContract,
    segment_id: str,
) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    if len(snapshot.prefix_instance_receipts) != COMPOSITION_PREFIX_LENGTH:
        raise ValueError("composition source must bind exactly six prefix receipts")
    staging_path = _regular_file(
        source_root, "staging_plan.json", label="source staging plan"
    )
    staging_payload, staging_raw = _read_json_object(
        staging_path, label="source staging plan"
    )
    if _sha256(staging_raw) != snapshot.source_staging_plan_sha256:
        raise ValueError("source staging plan hash differs")
    source_phase_id = staging_payload.get("phase_id")
    if not isinstance(source_phase_id, str) or not source_phase_id:
        raise ValueError("source staging plan phase is invalid")
    for expected_index, binding in enumerate(snapshot.prefix_instance_receipts):
        if binding.stream_index != expected_index:
            raise ValueError("composition source prefix is not contiguous")
        path = _regular_file(
            source_root, binding.relative_path, label="source prefix instance receipt"
        )
        _path, digest = _validate_instance_receipt(
            path,
            expected_item=contract.stream[expected_index],
            phase_id=source_phase_id,
            staging_plan_sha256=snapshot.source_staging_plan_sha256,
            expected_receipt_sha256=binding.sha256,
        )
        entries.append(
            {
                "stream_index": expected_index,
                "source_segment": segment_id,
                "instance_receipt": {
                    "relative_path": binding.relative_path,
                    "sha256": digest,
                },
            }
        )
    return entries


def _discover_successor_entries(
    *,
    successor_root: Path,
    contract: ThreeArmContinuationContract,
    segment_id: str,
) -> list[dict[str, object]]:
    resolved_root = Path(successor_root).resolve(strict=True)
    instance_root = resolved_root / "formal" / "instances"
    if not instance_root.is_dir() or instance_root.is_symlink():
        raise ValueError("successor instance receipt root is missing or unsafe")
    discovered: dict[int, tuple[Path, str]] = {}
    receipt_paths = tuple(instance_root.glob("*/instance_receipt.json"))
    for path in receipt_paths:
        try:
            metadata = path.lstat()
        except FileNotFoundError as exc:
            raise ValueError("successor instance receipt disappeared") from exc
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise ValueError("successor instance receipt must be a regular file")
        try:
            path.resolve(strict=True).relative_to(instance_root.resolve(strict=True))
        except ValueError as exc:
            raise ValueError("successor instance receipt escapes its segment") from exc
        payload, _raw = _read_canonical_json(path, label="successor instance receipt")
        stream_item = payload.get("stream_item")
        stream_index = stream_item.get("stream_index") if isinstance(stream_item, dict) else None
        if (
            isinstance(stream_index, bool)
            or not isinstance(stream_index, int)
            or not COMPOSITION_PREFIX_LENGTH <= stream_index < COMPOSITION_INSTANCE_COUNT
        ):
            raise ValueError("successor receipt nested stream index is outside [6,24)")
        if stream_index in discovered:
            raise ValueError(f"duplicate successor receipt stream index {stream_index}")
        _path, digest = _validate_instance_receipt(
            path,
            expected_item=contract.stream[stream_index],
            phase_id=contract.phase_id,
            staging_plan_sha256=contract.staging_plan_sha256,
        )
        relative = path.relative_to(resolved_root).as_posix()
        discovered[stream_index] = (path, digest)
    expected_indices = set(range(COMPOSITION_PREFIX_LENGTH, COMPOSITION_INSTANCE_COUNT))
    if set(discovered) != expected_indices:
        missing = sorted(expected_indices - set(discovered))
        extra = sorted(set(discovered) - expected_indices)
        raise ValueError(
            f"successor sealed receipt set differs: missing={missing}, extra={extra}"
        )
    return [
        {
            "stream_index": stream_index,
            "source_segment": segment_id,
            "instance_receipt": {
                "relative_path": discovered[stream_index][0]
                .relative_to(resolved_root)
                .as_posix(),
                "sha256": discovered[stream_index][1],
            },
        }
        for stream_index in sorted(discovered)
    ]


def _audit_excluded_tail(
    snapshot: ThreeArmContinuationSourceSnapshot, *, source_segment_id: str
) -> list[dict[str, object]]:
    if "scikit-learn-14983" not in snapshot.excluded_instance_id:
        raise ValueError("composition excluded source tail is not scikit-learn-14983")
    if not snapshot.excluded_consumed_tail:
        raise ValueError("composition must audit the consumed scikit-learn tail")
    return [
        {
            "source_segment": source_segment_id,
            "instance_id": snapshot.excluded_instance_id,
            "reason": "excluded_consumed_scikit_tail",
            **tail.to_dict(),
            "learning_import": False,
            "performance_import": False,
        }
        for tail in snapshot.excluded_consumed_tail
    ]


def build_three_arm_composition_payload(
    *,
    source_root: Path,
    successor_root: Path,
    source_snapshot: ThreeArmContinuationSourceSnapshot,
    successor_contract: ThreeArmContinuationContract,
    source_segment_id: str = SOURCE_PREFIX_SEGMENT_ID,
    successor_segment_id: str = SUCCESSOR_SUFFIX_SEGMENT_ID,
) -> dict[str, object]:
    """Build and double-read a references-only composition from verified inputs."""

    if (
        not _SEGMENT_ID.fullmatch(source_segment_id)
        or not _SEGMENT_ID.fullmatch(successor_segment_id)
        or source_segment_id == successor_segment_id
    ):
        raise ValueError("composition segment IDs are invalid or duplicated")
    if (
        successor_contract.source_snapshot_sha256 != source_snapshot.sha256
        or successor_contract.source_manifest_sha256
        != source_snapshot.source_manifest_sha256
        or successor_contract.execution_start_index != COMPOSITION_PREFIX_LENGTH
        or successor_contract.execution_stop_index != COMPOSITION_INSTANCE_COUNT
        or len(successor_contract.stream) != COMPOSITION_INSTANCE_COUNT
    ):
        raise ValueError("composition successor contract/source boundary differs")

    def capture() -> dict[str, object]:
        prefix = _prefix_entries(
            source_root=source_root,
            snapshot=source_snapshot,
            contract=successor_contract,
            segment_id=source_segment_id,
        )
        suffix = _discover_successor_entries(
            successor_root=successor_root,
            contract=successor_contract,
            segment_id=successor_segment_id,
        )
        return {
            "schema_version": COMPOSITION_SCHEMA_VERSION,
            "kind": COMPOSITION_KIND,
            "prefix_length": COMPOSITION_PREFIX_LENGTH,
            "segments": [
                {"segment_id": source_segment_id, "role": "source_prefix"},
                {"segment_id": successor_segment_id, "role": "successor_suffix"},
            ],
            "instances": prefix + suffix,
            "excluded_consumed_tail": _audit_excluded_tail(
                source_snapshot, source_segment_id=source_segment_id
            ),
        }

    first = capture()
    second = capture()
    if _canonical_bytes(first) != _canonical_bytes(second):
        raise ValueError("composition source or successor changed between double reads")
    return first


def _write_content_addressed(directory: Path, raw: bytes) -> Path:
    directory = Path(directory).resolve()
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError("composition output directory is unsafe")
    path = directory / f"{_sha256(raw)}.json"
    if path.exists() or path.is_symlink():
        if path.is_symlink() or path.read_bytes() != raw:
            raise ValueError("composition content-addressed output is already rebound")
        return path
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=".three-arm-composition-", suffix=".tmp", dir=directory
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, 0o444)
        os.replace(temporary, path)
        directory_fd = os.open(directory, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return path


@dataclass(frozen=True)
class ThreeArmCompositionOutcome:
    manifest_sha256: str
    manifest_path: Path
    payload: dict[str, object]
    segment_roots: dict[str, Path]


def prepare_verified_three_arm_composition_manifest(
    *,
    source_root: Path,
    successor_root: Path,
    source_snapshot: ThreeArmContinuationSourceSnapshot,
    successor_contract: ThreeArmContinuationContract,
    output_root: Path,
    source_segment_id: str = SOURCE_PREFIX_SEGMENT_ID,
    successor_segment_id: str = SUCCESSOR_SUFFIX_SEGMENT_ID,
) -> ThreeArmCompositionOutcome:
    payload = build_three_arm_composition_payload(
        source_root=source_root,
        successor_root=successor_root,
        source_snapshot=source_snapshot,
        successor_contract=successor_contract,
        source_segment_id=source_segment_id,
        successor_segment_id=successor_segment_id,
    )
    raw = _canonical_bytes(payload)
    path = _write_content_addressed(Path(output_root) / "composition_manifests", raw)
    return ThreeArmCompositionOutcome(
        manifest_sha256=_sha256(raw),
        manifest_path=path,
        payload=payload,
        segment_roots={
            source_segment_id: Path(source_root).resolve(strict=True),
            successor_segment_id: Path(successor_root).resolve(strict=True),
        },
    )


def prepare_three_arm_composition_manifest(
    *,
    source_root: Path,
    successor_root: Path,
    source_manifest_path: Path,
    source_snapshot_path: Path,
    successor_staging_path: Path,
    output_root: Path,
    source_segment_id: str = SOURCE_PREFIX_SEGMENT_ID,
    successor_segment_id: str = SUCCESSOR_SUFFIX_SEGMENT_ID,
) -> ThreeArmCompositionOutcome:
    """Verify both segment contracts, then write one immutable CAS manifest."""

    snapshot = verify_three_arm_continuation_source(
        source_root=source_root,
        manifest_path=source_manifest_path,
        snapshot_path=source_snapshot_path,
    )
    staging = Path(successor_staging_path).resolve(strict=True)
    successor = Path(successor_root).resolve(strict=True)
    if staging != successor / "staging_plan.json":
        raise ValueError("successor staging plan must be rooted in its artifact segment")
    contract = ThreeArmContinuationContract.from_staging_path(
        staging, source_snapshot=snapshot
    )
    contract.require_executable()
    return prepare_verified_three_arm_composition_manifest(
        source_root=source_root,
        successor_root=successor_root,
        source_snapshot=snapshot,
        successor_contract=contract,
        output_root=output_root,
        source_segment_id=source_segment_id,
        successor_segment_id=successor_segment_id,
    )


__all__ = [
    "COMPOSITION_KIND",
    "COMPOSITION_PREFIX_LENGTH",
    "COMPOSITION_SCHEMA_VERSION",
    "SOURCE_PREFIX_SEGMENT_ID",
    "SUCCESSOR_SUFFIX_SEGMENT_ID",
    "ThreeArmCompositionOutcome",
    "build_three_arm_composition_payload",
    "prepare_three_arm_composition_manifest",
    "prepare_verified_three_arm_composition_manifest",
]
