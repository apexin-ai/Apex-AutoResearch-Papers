"""Strict Builder Memory boundaries for frozen and online Moss experiments."""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, Mapping, Sequence


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_WINDOWS_ABSOLUTE_PATH = re.compile(r"(?i)(?:^|\s)[A-Z]:\\")
_UNIX_ABSOLUTE_PATH = re.compile(
    r"(?:^|\s)/(?:home|root|tmp|var|etc|mnt|workspace|private|Users)/"
)
_FORBIDDEN_RULE_MARKERS = (
    "candidate answer",
    "candidate_answer",
    "candidate content",
    "candidate_content",
    "raw trace",
    "raw_trace",
    "hidden test",
    "hidden_test",
    "private evaluator",
    "private_evaluator",
    "private gold",
    "private_gold",
    "task_id=",
    "instance_id=",
    "benchmark_private",
)
_SENSITIVE_RULE_TERMS = (
    "candidate",
    "trace",
    "hidden",
    "private",
    "evaluator",
    "taskid",
    "instanceid",
)
_ALLOWED_RULE_PUNCTUATION = frozenset(" .,;:!?()'\"-")
_RECORD_FIELDS = {
    "record_id",
    "rule",
    "source_benchmark",
    "source_instance_hash",
    "source_lineage_hash",
    "source_round",
    "source_order",
    "distiller_version",
    "sanitizer_version",
    "record_sha256",
}


def _canonical_json(value: object) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _sha256(value: object) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _safe_id(value: object, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise ValueError(f"{label} is invalid")
    return value


def _hash(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"{label} is invalid")
    return value


def _validate_rule(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("cross-task rule is not sanitized")
    rule = " ".join(unicodedata.normalize("NFKC", value).split())
    if not rule or len(rule) > 2_000:
        raise ValueError("cross-task rule is not sanitized")
    if any(ord(character) >= 128 for character in rule):
        raise ValueError("cross-task rule is not sanitized")
    lowered = rule.casefold()
    if any(
        not (character.isalnum() or character.isspace() or character in _ALLOWED_RULE_PUNCTUATION)
        for character in rule
    ):
        raise ValueError("cross-task rule is not sanitized")
    compact = re.sub(r"[^0-9a-z]+", "", lowered)
    if (
        any(term in compact for term in _SENSITIVE_RULE_TERMS)
        or "```" in rule
        or "../" in rule
        or "..\\" in rule
        or _WINDOWS_ABSOLUTE_PATH.search(rule)
        or _UNIX_ABSOLUTE_PATH.search(rule)
        or _SHA256.search(lowered)
        or any(marker in lowered for marker in _FORBIDDEN_RULE_MARKERS)
    ):
        raise ValueError("cross-task rule is not sanitized")
    if (
        '"schema_version"' in lowered
        and '"nodes"' in lowered
        and ('"interface"' in lowered or '"spec"' in lowered)
    ):
        raise ValueError("cross-task rule is not sanitized")
    return rule


@dataclass(frozen=True)
class CrossTaskMemoryRecord:
    record_id: str
    rule: str
    source_benchmark: str
    source_instance_hash: str
    source_lineage_hash: str
    source_round: int
    source_order: int
    distiller_version: str
    sanitizer_version: str
    record_sha256: str

    @classmethod
    def create(
        cls,
        *,
        record_id: str,
        rule: str,
        source_benchmark: str,
        source_instance_hash: str,
        source_lineage_hash: str,
        source_round: int,
        source_order: int,
        distiller_version: str,
        sanitizer_version: str,
    ) -> "CrossTaskMemoryRecord":
        payload = cls._validated_payload(
            {
                "record_id": record_id,
                "rule": rule,
                "source_benchmark": source_benchmark,
                "source_instance_hash": source_instance_hash,
                "source_lineage_hash": source_lineage_hash,
                "source_round": source_round,
                "source_order": source_order,
                "distiller_version": distiller_version,
                "sanitizer_version": sanitizer_version,
            }
        )
        return cls(**payload, record_sha256=_sha256(payload))

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "CrossTaskMemoryRecord":
        if not isinstance(payload, Mapping) or set(payload) != _RECORD_FIELDS:
            raise ValueError("cross-task memory record fields are invalid")
        public = cls._validated_payload(
            {key: payload[key] for key in _RECORD_FIELDS - {"record_sha256"}}
        )
        expected = _sha256(public)
        actual = _hash(payload.get("record_sha256"), "cross-task record hash")
        if actual != expected:
            raise ValueError("cross-task record hash does not match provenance")
        return cls(**public, record_sha256=actual)

    @staticmethod
    def _validated_payload(payload: Mapping[str, Any]) -> dict[str, Any]:
        record_id = _safe_id(payload.get("record_id"), "cross-task record id")
        source_benchmark = _safe_id(
            payload.get("source_benchmark"), "cross-task source benchmark"
        )
        distiller_version = _safe_id(
            payload.get("distiller_version"), "cross-task distiller version"
        )
        sanitizer_version = _safe_id(
            payload.get("sanitizer_version"), "cross-task sanitizer version"
        )
        source_round = payload.get("source_round")
        source_order = payload.get("source_order")
        for value, label in (
            (source_round, "cross-task source round"),
            (source_order, "cross-task source order"),
        ):
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError(f"{label} is invalid")
        return {
            "record_id": record_id,
            "rule": _validate_rule(payload.get("rule")),
            "source_benchmark": source_benchmark,
            "source_instance_hash": _hash(
                payload.get("source_instance_hash"),
                "cross-task source instance hash",
            ),
            "source_lineage_hash": _hash(
                payload.get("source_lineage_hash"),
                "cross-task source lineage hash",
            ),
            "source_round": source_round,
            "source_order": source_order,
            "distiller_version": distiller_version,
            "sanitizer_version": sanitizer_version,
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "record_id": self.record_id,
            "rule": self.rule,
            "source_benchmark": self.source_benchmark,
            "source_instance_hash": self.source_instance_hash,
            "source_lineage_hash": self.source_lineage_hash,
            "source_round": self.source_round,
            "source_order": self.source_order,
            "distiller_version": self.distiller_version,
            "sanitizer_version": self.sanitizer_version,
            "record_sha256": self.record_sha256,
        }


@dataclass(frozen=True)
class CrossTaskMemorySnapshot:
    before_order: int
    records: tuple[CrossTaskMemoryRecord, ...]

    def __post_init__(self) -> None:
        if (
            not isinstance(self.before_order, int)
            or isinstance(self.before_order, bool)
            or self.before_order < 0
        ):
            raise ValueError("cross-task snapshot order is invalid")
        if any(record.source_order >= self.before_order for record in self.records):
            raise ValueError("cross-task snapshot includes current or future records")

    @property
    def sha256(self) -> str:
        return _sha256(
            {
                "before_order": self.before_order,
                "records": [record.to_dict() for record in self.records],
            }
        )

    def public_payload(self) -> dict[str, Any]:
        return {
            "before_order": self.before_order,
            "records": [record.to_dict() for record in self.records],
            "snapshot_sha256": self.sha256,
        }


@dataclass(frozen=True)
class BuilderMemoryConfig:
    mode: Literal["instance_only", "cross_task_online"] = "instance_only"
    cross_task_records: tuple[CrossTaskMemoryRecord, ...] = ()
    snapshot_sha256: str | None = None

    def __post_init__(self) -> None:
        if self.mode not in {"instance_only", "cross_task_online"}:
            raise ValueError("Builder memory mode is invalid")
        normalized: list[CrossTaskMemoryRecord] = []
        for record in self.cross_task_records:
            if isinstance(record, CrossTaskMemoryRecord):
                normalized.append(CrossTaskMemoryRecord.from_dict(record.to_dict()))
            elif isinstance(record, Mapping):
                normalized.append(CrossTaskMemoryRecord.from_dict(record))
            else:
                raise ValueError("cross-task memory record is invalid")
        if self.mode == "instance_only" and normalized:
            raise ValueError("instance-only Builder memory cannot contain cross-task records")
        if self.snapshot_sha256 is not None:
            _hash(self.snapshot_sha256, "Builder memory snapshot hash")
        if self.mode == "instance_only" and self.snapshot_sha256 is not None:
            raise ValueError("instance-only Builder memory cannot bind a snapshot")
        object.__setattr__(self, "cross_task_records", tuple(normalized))

    @classmethod
    def from_snapshot(
        cls, snapshot: CrossTaskMemorySnapshot
    ) -> "BuilderMemoryConfig":
        if not isinstance(snapshot, CrossTaskMemorySnapshot):
            raise TypeError("Builder memory snapshot is invalid")
        return cls(
            mode="cross_task_online",
            cross_task_records=snapshot.records,
            snapshot_sha256=snapshot.sha256,
        )

    def public_payload(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "cross_task_records": [
                record.to_dict() for record in self.cross_task_records
            ],
            "snapshot_sha256": self.snapshot_sha256,
        }

    def receipt_payload(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "snapshot_sha256": self.snapshot_sha256,
            "record_count": len(self.cross_task_records),
            "provenance": [
                {
                    "record_id": record.record_id,
                    "record_sha256": record.record_sha256,
                    "source_benchmark": record.source_benchmark,
                    "source_instance_hash": record.source_instance_hash,
                    "source_lineage_hash": record.source_lineage_hash,
                    "source_round": record.source_round,
                    "source_order": record.source_order,
                    "distiller_version": record.distiller_version,
                    "sanitizer_version": record.sanitizer_version,
                }
                for record in self.cross_task_records
            ],
        }


class CrossTaskMemoryStore:
    """Content-addressed, append-only storage for sanitized cross-task rules."""

    def __init__(self, root: Path) -> None:
        self.root = Path(os.path.abspath(os.fspath(root)))
        self.objects_root = self.root / "objects"
        self.bindings_root = self.root / "bindings"
        self._writable = True
        self.objects_root.mkdir(parents=True, exist_ok=True)
        self.bindings_root.mkdir(parents=True, exist_ok=True)

    @classmethod
    def open_existing(cls, root: Path) -> "CrossTaskMemoryStore":
        """Open an existing memory root without creating or following symlinks."""
        normalized = Path(os.path.abspath(os.fspath(root)))
        if not normalized.exists() or not normalized.is_dir():
            raise ValueError("cross-task memory root must be an existing directory")
        resolved = normalized.resolve(strict=True)
        if normalized.is_symlink() or resolved != normalized:
            raise ValueError("cross-task memory root must not be a symlink")
        objects_root = normalized / "objects"
        bindings_root = normalized / "bindings"
        for child in (objects_root, bindings_root):
            if child.is_symlink() or (child.exists() and not child.is_dir()):
                raise ValueError("cross-task memory storage directories must be real directories")
        store = cls.__new__(cls)
        store.root = normalized
        store.objects_root = objects_root
        store.bindings_root = bindings_root
        store._writable = False
        return store

    @staticmethod
    def _write_once(path: Path, payload: Mapping[str, Any], *, label: str) -> None:
        encoded = _canonical_json(payload) + "\n"
        if path.is_symlink() or path.is_dir():
            raise ValueError(f"{label} is append-only")
        if path.is_file():
            existing = path.read_text(encoding="utf-8")
            if existing != encoded:
                raise ValueError(f"{label} is append-only")
            return

        path.parent.mkdir(parents=True, exist_ok=True)
        fd, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent)
        )
        temporary = Path(temporary_name)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
                stream.write(encoded)
                stream.flush()
                os.fsync(stream.fileno())
            try:
                # Hard-link publication is atomic and never overwrites a competing
                # append, while ensuring readers see only the fully fsynced file.
                os.link(temporary, path)
            except FileExistsError:
                existing = path.read_text(encoding="utf-8")
                if existing != encoded:
                    raise ValueError(f"{label} is append-only")
        finally:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass

    def append(self, record: CrossTaskMemoryRecord) -> CrossTaskMemoryRecord:
        if not self._writable:
            raise ValueError("cross-task memory store is read-only")
        record = CrossTaskMemoryRecord.from_dict(record.to_dict())
        object_path = self.objects_root / f"{record.record_sha256}.json"
        self._write_once(object_path, record.to_dict(), label="cross-task memory object")
        binding_path = self.bindings_root / f"{record.record_id}.json"
        self._write_once(
            binding_path,
            {
                "record_id": record.record_id,
                "record_sha256": record.record_sha256,
            },
            label="cross-task memory binding",
        )
        return record

    def _load_binding(self, path: Path) -> CrossTaskMemoryRecord:
        if path.is_symlink():
            raise ValueError("cross-task memory binding must be a real file")
        binding = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(binding, Mapping) or set(binding) != {
            "record_id",
            "record_sha256",
        }:
            raise ValueError("cross-task memory binding is invalid")
        record_id = _safe_id(binding.get("record_id"), "cross-task binding record id")
        if path.name != f"{record_id}.json":
            raise ValueError("cross-task memory binding identity is invalid")
        record_sha256 = _hash(
            binding.get("record_sha256"), "cross-task binding record hash"
        )
        object_path = self.objects_root / f"{record_sha256}.json"
        if object_path.is_symlink() or not object_path.is_file():
            raise ValueError("cross-task memory object is missing")
        record = CrossTaskMemoryRecord.from_dict(
            json.loads(object_path.read_text(encoding="utf-8"))
        )
        if record.record_id != record_id or record.record_sha256 != record_sha256:
            raise ValueError("cross-task memory binding does not match object")
        return record

    def records(self) -> tuple[CrossTaskMemoryRecord, ...]:
        records = [
            self._load_binding(path)
            for path in self.bindings_root.glob("*.json")
        ]
        records.sort(key=lambda item: (item.source_order, item.record_id))
        return tuple(records)

    def snapshot(self, *, before_order: int) -> CrossTaskMemorySnapshot:
        if (
            not isinstance(before_order, int)
            or isinstance(before_order, bool)
            or before_order < 0
        ):
            raise ValueError("cross-task snapshot order is invalid")
        visible = tuple(
            record for record in self.records() if record.source_order < before_order
        )
        return CrossTaskMemorySnapshot(before_order=before_order, records=visible)


__all__ = [
    "BuilderMemoryConfig",
    "CrossTaskMemoryRecord",
    "CrossTaskMemorySnapshot",
    "CrossTaskMemoryStore",
]
