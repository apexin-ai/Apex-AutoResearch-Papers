from __future__ import annotations

import fcntl
import hashlib
import json
import math
import os
import re
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping


_ZERO_SHA256 = "0" * 64
_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/+-]{0,255}")
_SAFE_CELL_IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_EVENT_TYPES = {
    "operation_reserved",
    "operation_started",
    "operation_completed",
    "operation_failed",
}
_RESOURCE_FIELDS = (
    "model_calls",
    "evaluator_transactions",
    "gpu_exclusive_seconds",
    "cpu_evaluator_seconds",
)


class JournalIntegrityError(RuntimeError):
    """The persisted journal or its independently stored head is invalid."""


class OperationStateError(RuntimeError):
    """An operation transition conflicts with its append-only history."""


class ResourceCapExceeded(RuntimeError):
    """A reservation would exceed a frozen global or per-cell entitlement."""


class UnsafeIdentifierError(ValueError):
    """An identifier is unsuitable for an auditable operation journal."""


def _safe_identifier(value: str, label: str) -> str:
    if (
        not isinstance(value, str)
        or not _SAFE_IDENTIFIER.fullmatch(value)
        or ".." in value
        or "//" in value
        or value.endswith("/")
    ):
        raise UnsafeIdentifierError(f"unsafe {label}")
    return value


def _safe_cell_identifier(value: str) -> str:
    if (
        not isinstance(value, str)
        or not _SAFE_CELL_IDENTIFIER.fullmatch(value)
        or ".." in value
        or "//" in value
        or value.endswith("/")
    ):
        raise UnsafeIdentifierError("unsafe cell id")
    return value


def _sha256(value: str, label: str) -> str:
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise JournalIntegrityError(f"invalid {label}")
    return value


def _require_exact_keys(payload: Mapping[str, Any], expected: set[str], label: str) -> None:
    actual = set(payload)
    if actual != expected:
        raise JournalIntegrityError(
            f"{label} keys differ: missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}"
        )


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


@dataclass(frozen=True)
class ResourceVector:
    model_calls: int = 0
    evaluator_transactions: int = 0
    gpu_exclusive_seconds: float = 0.0
    cpu_evaluator_seconds: float = 0.0

    def __post_init__(self) -> None:
        for field in ("model_calls", "evaluator_transactions"):
            value = getattr(self, field)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"{field} must be a non-negative integer")
        for field in ("gpu_exclusive_seconds", "cpu_evaluator_seconds"):
            value = getattr(self, field)
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or value < 0
            ):
                raise ValueError(f"{field} must be a finite non-negative number")
            object.__setattr__(self, field, float(value))

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "ResourceVector":
        _require_exact_keys(payload, set(_RESOURCE_FIELDS), "resource vector")
        try:
            return cls(**{field: payload[field] for field in _RESOURCE_FIELDS})
        except (TypeError, ValueError) as exc:
            raise JournalIntegrityError(f"invalid resource vector: {exc}") from exc

    def to_dict(self) -> dict[str, int | float]:
        return {
            "model_calls": self.model_calls,
            "evaluator_transactions": self.evaluator_transactions,
            "gpu_exclusive_seconds": self.gpu_exclusive_seconds,
            "cpu_evaluator_seconds": self.cpu_evaluator_seconds,
        }

    def __add__(self, other: "ResourceVector") -> "ResourceVector":
        if not isinstance(other, ResourceVector):
            return NotImplemented
        return ResourceVector(
            model_calls=self.model_calls + other.model_calls,
            evaluator_transactions=(
                self.evaluator_transactions + other.evaluator_transactions
            ),
            gpu_exclusive_seconds=(
                self.gpu_exclusive_seconds + other.gpu_exclusive_seconds
            ),
            cpu_evaluator_seconds=(
                self.cpu_evaluator_seconds + other.cpu_evaluator_seconds
            ),
        )


@dataclass(frozen=True)
class ResourceCaps(ResourceVector):
    """A hard resource envelope. Per-cell instances are non-transferable."""


@dataclass(frozen=True)
class JournalEvent:
    schema_version: int
    sequence: int
    event_id: str
    event_type: str
    operation_id: str
    cell_id: str
    operation_kind: str
    recorded_at: str
    prev_event_sha256: str
    payload: dict[str, Any]
    event_sha256: str

    def core_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "sequence": self.sequence,
            "event_id": self.event_id,
            "event_type": self.event_type,
            "operation_id": self.operation_id,
            "cell_id": self.cell_id,
            "operation_kind": self.operation_kind,
            "recorded_at": self.recorded_at,
            "prev_event_sha256": self.prev_event_sha256,
            "payload": self.payload,
        }

    def to_dict(self) -> dict[str, Any]:
        return {**self.core_dict(), "event_sha256": self.event_sha256}


@dataclass(frozen=True)
class OperationRecord:
    operation_id: str
    cell_id: str
    operation_kind: str
    reservation: ResourceVector
    state: str
    committed_usage: ResourceVector
    events: tuple[JournalEvent, ...]

    def event_for(self, event_type: str) -> JournalEvent:
        return next(event for event in self.events if event.event_type == event_type)


@dataclass(frozen=True)
class JournalReplay:
    events: tuple[JournalEvent, ...]
    operations: dict[str, OperationRecord]
    event_count: int
    head_sha256: str


@dataclass(frozen=True)
class ResourceSnapshot:
    global_committed: ResourceVector
    cell_committed: dict[str, ResourceVector]
    abandoned_operation_ids: tuple[str, ...]
    reserved_operation_ids: tuple[str, ...]


def _parse_timestamp(value: Any) -> str:
    if not isinstance(value, str):
        raise JournalIntegrityError("recorded_at must be a timestamp")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as exc:
        raise JournalIntegrityError("recorded_at must be an ISO timestamp") from exc
    if parsed.tzinfo is None:
        raise JournalIntegrityError("recorded_at must include a timezone")
    return value


def _terminal_usage(
    payload: Mapping[str, Any], reservation: ResourceVector, *, event_type: str
) -> ResourceVector:
    expected = {"actual_usage", "usage_known", "artifact_sha256"}
    if event_type == "operation_failed":
        expected.add("reason_code")
    _require_exact_keys(payload, expected, f"{event_type} payload")
    if not isinstance(payload["usage_known"], bool):
        raise JournalIntegrityError("usage_known must be boolean")
    artifact_sha = payload["artifact_sha256"]
    if artifact_sha is not None:
        _sha256(artifact_sha, "artifact sha256")
    if event_type == "operation_failed":
        try:
            _safe_identifier(payload["reason_code"], "reason code")
        except UnsafeIdentifierError as exc:
            raise JournalIntegrityError(str(exc)) from exc
    usage = ResourceVector.from_dict(payload["actual_usage"])
    if usage.model_calls != reservation.model_calls:
        raise JournalIntegrityError("started model-call reservations cannot be released")
    if usage.evaluator_transactions != reservation.evaluator_transactions:
        raise JournalIntegrityError(
            "started evaluator-transaction reservations cannot be released"
        )
    if usage.gpu_exclusive_seconds > reservation.gpu_exclusive_seconds:
        raise JournalIntegrityError("GPU usage exceeded its reservation")
    if usage.cpu_evaluator_seconds > reservation.cpu_evaluator_seconds:
        raise JournalIntegrityError("CPU evaluator usage exceeded its reservation")
    if not payload["usage_known"] and usage != reservation:
        raise JournalIntegrityError("unknown terminal usage must charge the reservation")
    return usage


def _event_from_raw(raw: Any, *, expected_sequence: int, previous_sha: str) -> JournalEvent:
    if not isinstance(raw, dict):
        raise JournalIntegrityError("journal events must be JSON objects")
    _require_exact_keys(
        raw,
        {
            "schema_version",
            "sequence",
            "event_id",
            "event_type",
            "operation_id",
            "cell_id",
            "operation_kind",
            "recorded_at",
            "prev_event_sha256",
            "payload",
            "event_sha256",
        },
        "journal event",
    )
    if raw["schema_version"] != 1:
        raise JournalIntegrityError("unsupported journal schema")
    if isinstance(raw["sequence"], bool) or raw["sequence"] != expected_sequence:
        raise JournalIntegrityError("journal sequence is not contiguous")
    try:
        event_id = _safe_identifier(raw["event_id"], "event id")
        operation_id = _safe_identifier(raw["operation_id"], "operation id")
        cell_id = _safe_cell_identifier(raw["cell_id"])
        operation_kind = _safe_identifier(raw["operation_kind"], "operation kind")
    except UnsafeIdentifierError as exc:
        raise JournalIntegrityError(str(exc)) from exc
    event_type = raw["event_type"]
    if event_type not in _EVENT_TYPES:
        raise JournalIntegrityError("unknown event type")
    prev = _sha256(raw["prev_event_sha256"], "previous event sha256")
    if prev != previous_sha:
        raise JournalIntegrityError("journal hash chain is broken")
    event_sha = _sha256(raw["event_sha256"], "event sha256")
    if not isinstance(raw["payload"], dict):
        raise JournalIntegrityError("event payload must be an object")
    event = JournalEvent(
        schema_version=1,
        sequence=raw["sequence"],
        event_id=event_id,
        event_type=event_type,
        operation_id=operation_id,
        cell_id=cell_id,
        operation_kind=operation_kind,
        recorded_at=_parse_timestamp(raw["recorded_at"]),
        prev_event_sha256=prev,
        payload=raw["payload"],
        event_sha256=event_sha,
    )
    expected_sha = hashlib.sha256(_canonical_bytes(event.core_dict())).hexdigest()
    if event.event_sha256 != expected_sha:
        raise JournalIntegrityError("event content hash does not match")
    return event


def _replay_events(events: list[JournalEvent]) -> dict[str, OperationRecord]:
    records: dict[str, OperationRecord] = {}
    event_ids: set[str] = set()
    for event in events:
        if event.event_id in event_ids:
            raise JournalIntegrityError("duplicate event id")
        event_ids.add(event.event_id)
        prior = records.get(event.operation_id)
        if event.event_type == "operation_reserved":
            if prior is not None:
                raise JournalIntegrityError("operation was reserved more than once")
            _require_exact_keys(
                event.payload, {"reservation"}, "operation_reserved payload"
            )
            reservation = ResourceVector.from_dict(event.payload["reservation"])
            records[event.operation_id] = OperationRecord(
                operation_id=event.operation_id,
                cell_id=event.cell_id,
                operation_kind=event.operation_kind,
                reservation=reservation,
                state="reserved",
                committed_usage=reservation,
                events=(event,),
            )
            continue
        if prior is None:
            raise JournalIntegrityError("operation transition occurred before reservation")
        if event.cell_id != prior.cell_id or event.operation_kind != prior.operation_kind:
            raise JournalIntegrityError("operation identity was rebound")
        if event.event_type == "operation_started":
            if prior.state != "reserved":
                raise JournalIntegrityError("operation start is out of order")
            _require_exact_keys(event.payload, set(), "operation_started payload")
            state = "started"
            usage = prior.reservation
        elif event.event_type in {"operation_completed", "operation_failed"}:
            if prior.state != "started":
                raise JournalIntegrityError("operation terminal event is out of order")
            usage = _terminal_usage(
                event.payload, prior.reservation, event_type=event.event_type
            )
            state = "completed" if event.event_type == "operation_completed" else "failed"
        else:  # pragma: no cover - _event_from_raw has already constrained the value.
            raise JournalIntegrityError("unknown event type")
        records[event.operation_id] = OperationRecord(
            operation_id=prior.operation_id,
            cell_id=prior.cell_id,
            operation_kind=prior.operation_kind,
            reservation=prior.reservation,
            state=state,
            committed_usage=usage,
            events=prior.events + (event,),
        )
    return records


def verify_operation_journal(
    ledger_path: Path, *, anchor_path: Path | None = None
) -> JournalReplay:
    """Independently replay a journal without trusting a materialized controller state."""

    ledger_path = Path(ledger_path)
    raw_lines = []
    if ledger_path.exists():
        try:
            raw_lines = ledger_path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError as exc:
            raise JournalIntegrityError("journal is not valid UTF-8") from exc
    events: list[JournalEvent] = []
    previous_sha = _ZERO_SHA256
    for index, line in enumerate(raw_lines, start=1):
        if not line.strip():
            raise JournalIntegrityError("journal contains an empty record")
        try:
            raw = json.loads(line)
        except json.JSONDecodeError as exc:
            raise JournalIntegrityError("journal contains invalid JSON") from exc
        event = _event_from_raw(raw, expected_sequence=index, previous_sha=previous_sha)
        events.append(event)
        previous_sha = event.event_sha256
    records = _replay_events(events)
    replay = JournalReplay(
        events=tuple(events),
        operations=records,
        event_count=len(events),
        head_sha256=previous_sha,
    )
    if anchor_path is not None:
        anchor_path = Path(anchor_path)
        if not anchor_path.is_file():
            if events:
                raise JournalIntegrityError("external head anchor is missing")
        else:
            try:
                anchor = json.loads(anchor_path.read_text(encoding="utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise JournalIntegrityError("external head anchor is invalid") from exc
            if not isinstance(anchor, dict):
                raise JournalIntegrityError("external head anchor must be an object")
            _require_exact_keys(
                anchor,
                {"schema_version", "event_count", "head_sha256"},
                "external head anchor",
            )
            if (
                anchor["schema_version"] != 1
                or isinstance(anchor["event_count"], bool)
                or anchor["event_count"] != replay.event_count
                or anchor["head_sha256"] != replay.head_sha256
            ):
                raise JournalIntegrityError("external head anchor does not match journal")
            _sha256(anchor["head_sha256"], "anchor head sha256")
    return replay


class OperationJournal:
    """Append-only operation facts with a content hash chain and optional head anchor."""

    def __init__(self, root: Path, *, anchor_path: Path | None = None):
        self.root = Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.ledger_path = self.root / "operation_ledger.jsonl"
        self.lock_path = self.root / ".operation_ledger.lock"
        self.anchor_path = Path(anchor_path).resolve() if anchor_path is not None else None

    def replay(self) -> JournalReplay:
        return verify_operation_journal(
            self.ledger_path,
            anchor_path=self.anchor_path,
        )

    def _write_anchor(self, *, event_count: int, head_sha256: str) -> None:
        if self.anchor_path is None:
            return
        self.anchor_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": 1,
            "event_count": event_count,
            "head_sha256": head_sha256,
        }
        content = _canonical_bytes(payload) + b"\n"
        fd, name = tempfile.mkstemp(dir=self.anchor_path.parent, suffix=".head.tmp")
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            Path(name).replace(self.anchor_path)
        except Exception:
            Path(name).unlink(missing_ok=True)
            raise

    def _append(
        self,
        *,
        event_type: str,
        operation_id: str,
        cell_id: str,
        operation_kind: str,
        payload: dict[str, Any],
    ) -> JournalEvent:
        operation_id = _safe_identifier(operation_id, "operation id")
        cell_id = _safe_cell_identifier(cell_id)
        operation_kind = _safe_identifier(operation_kind, "operation kind")
        if event_type not in _EVENT_TYPES:
            raise ValueError("unknown event type")
        event_id = "evt:" + hashlib.sha256(
            f"{operation_id}|{event_type}".encode("utf-8")
        ).hexdigest()
        with self.lock_path.open("a+", encoding="utf-8") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                replay = self.replay()
                for existing in replay.events:
                    if existing.event_id == event_id:
                        if (
                            existing.event_type == event_type
                            and existing.operation_id == operation_id
                            and existing.cell_id == cell_id
                            and existing.operation_kind == operation_kind
                            and existing.payload == payload
                        ):
                            return existing
                        raise OperationStateError(
                            "event id is already bound to different content"
                        )
                recorded_at = datetime.now(timezone.utc).isoformat()
                core = {
                    "schema_version": 1,
                    "sequence": replay.event_count + 1,
                    "event_id": event_id,
                    "event_type": event_type,
                    "operation_id": operation_id,
                    "cell_id": cell_id,
                    "operation_kind": operation_kind,
                    "recorded_at": recorded_at,
                    "prev_event_sha256": replay.head_sha256,
                    "payload": payload,
                }
                event = JournalEvent(
                    **core,
                    event_sha256=hashlib.sha256(_canonical_bytes(core)).hexdigest(),
                )
                # Validate the proposed transition with the same independent reducer used
                # by recovery before any bytes are appended.
                _replay_events(list(replay.events) + [event])
                encoded = _canonical_bytes(event.to_dict()) + b"\n"
                with self.ledger_path.open("ab") as ledger:
                    ledger.write(encoded)
                    ledger.flush()
                    os.fsync(ledger.fileno())
                self._write_anchor(
                    event_count=event.sequence, head_sha256=event.event_sha256
                )
                return event
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)


def _terminal_payload(
    *,
    reservation: ResourceVector,
    actual_usage: ResourceVector | None,
    artifact_sha256: str | None,
    reason_code: str | None,
) -> dict[str, Any]:
    if artifact_sha256 is not None and not _SHA256.fullmatch(artifact_sha256):
        raise ValueError("invalid artifact sha256")
    usage_known = actual_usage is not None
    usage = actual_usage or reservation
    if usage.model_calls != reservation.model_calls:
        raise ValueError("started model-call reservations cannot be released")
    if usage.evaluator_transactions != reservation.evaluator_transactions:
        raise ValueError("started evaluator-transaction reservations cannot be released")
    if usage.gpu_exclusive_seconds > reservation.gpu_exclusive_seconds:
        raise ResourceCapExceeded("actual GPU usage exceeded its reservation")
    if usage.cpu_evaluator_seconds > reservation.cpu_evaluator_seconds:
        raise ResourceCapExceeded("actual CPU evaluator usage exceeded its reservation")
    payload: dict[str, Any] = {
        "actual_usage": usage.to_dict(),
        "usage_known": usage_known,
        "artifact_sha256": artifact_sha256,
    }
    if reason_code is not None:
        payload["reason_code"] = _safe_identifier(reason_code, "reason code")
    return payload


def _first_exceeded(
    proposed: ResourceVector, caps: ResourceVector
) -> str | None:
    for field in _RESOURCE_FIELDS:
        if getattr(proposed, field) > getattr(caps, field):
            return field
    return None


class ResourceGovernor:
    """Replay-derived hard caps around every side-effect-bearing operation."""

    def __init__(
        self,
        *,
        journal: OperationJournal,
        global_caps: ResourceCaps,
        cell_caps: Mapping[str, ResourceCaps],
        pre_reserve_guard: Callable[[], None] | None = None,
    ):
        self.journal = journal
        self.global_caps = global_caps
        if pre_reserve_guard is not None and not callable(pre_reserve_guard):
            raise ValueError("pre-reserve guard must be callable")
        self.pre_reserve_guard = pre_reserve_guard
        if not cell_caps:
            raise ValueError("at least one cell entitlement is required")
        self.cell_caps = {
            _safe_cell_identifier(cell_id): caps
            for cell_id, caps in cell_caps.items()
        }
        for cell_id, caps in self.cell_caps.items():
            exceeded = _first_exceeded(caps, global_caps)
            if exceeded is not None:
                raise ValueError(f"{cell_id} {exceeded} cap exceeds global cap")
        self.resource_lock_path = self.journal.root / ".resource_governor.lock"
        # Fail closed immediately if an existing ledger was created under incompatible
        # caps or contains an unknown cell.
        self.snapshot()

    def snapshot(self) -> ResourceSnapshot:
        replay = self.journal.replay()
        by_cell = {cell_id: ResourceVector() for cell_id in self.cell_caps}
        global_usage = ResourceVector()
        abandoned: list[str] = []
        reserved: list[str] = []
        for operation in replay.operations.values():
            if operation.cell_id not in by_cell:
                raise ResourceCapExceeded(
                    f"journal operation belongs to unknown cell {operation.cell_id}"
                )
            # reserved holds the full envelope; started-without-terminal is treated as
            # abandoned and conservatively charges that same full envelope on recovery.
            usage = operation.committed_usage
            by_cell[operation.cell_id] = by_cell[operation.cell_id] + usage
            global_usage = global_usage + usage
            if operation.state == "started":
                abandoned.append(operation.operation_id)
            elif operation.state == "reserved":
                reserved.append(operation.operation_id)
        exceeded = _first_exceeded(global_usage, self.global_caps)
        if exceeded is not None:
            raise ResourceCapExceeded(f"global {exceeded} hard cap is exceeded")
        for cell_id, usage in by_cell.items():
            exceeded = _first_exceeded(usage, self.cell_caps[cell_id])
            if exceeded is not None:
                raise ResourceCapExceeded(f"{cell_id} {exceeded} hard cap is exceeded")
        return ResourceSnapshot(
            global_committed=global_usage,
            cell_committed=by_cell,
            abandoned_operation_ids=tuple(sorted(abandoned)),
            reserved_operation_ids=tuple(sorted(reserved)),
        )

    def _record(self, operation_id: str) -> OperationRecord | None:
        _safe_identifier(operation_id, "operation id")
        return self.journal.replay().operations.get(operation_id)

    def reserve(
        self,
        *,
        operation_id: str,
        cell_id: str,
        operation_kind: str,
        reservation: ResourceVector,
    ) -> JournalEvent:
        operation_id = _safe_identifier(operation_id, "operation id")
        cell_id = _safe_cell_identifier(cell_id)
        operation_kind = _safe_identifier(operation_kind, "operation kind")
        # This lock covers replay, both cap checks, and the ledger append. Without it,
        # two controller processes could each observe the same remaining entitlement.
        with self.resource_lock_path.open("a+", encoding="utf-8") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                if self.pre_reserve_guard is not None:
                    self.pre_reserve_guard()
                existing = self._record(operation_id)
                if existing is not None:
                    if (
                        existing.cell_id == cell_id
                        and existing.operation_kind == operation_kind
                        and existing.reservation == reservation
                    ):
                        return existing.event_for("operation_reserved")
                    raise OperationStateError(
                        "operation id is already bound to a different reservation"
                    )
                if cell_id not in self.cell_caps:
                    raise ResourceCapExceeded(
                        f"cell has no frozen entitlement: {cell_id}"
                    )
                snapshot = self.snapshot()
                proposed_global = snapshot.global_committed + reservation
                exceeded = _first_exceeded(proposed_global, self.global_caps)
                if exceeded is not None:
                    raise ResourceCapExceeded(
                        f"global {exceeded} hard cap would be exceeded"
                    )
                proposed_cell = snapshot.cell_committed[cell_id] + reservation
                exceeded = _first_exceeded(proposed_cell, self.cell_caps[cell_id])
                if exceeded is not None:
                    raise ResourceCapExceeded(
                        f"{cell_id} {exceeded} hard cap would be exceeded"
                    )
                return self.journal._append(
                    event_type="operation_reserved",
                    operation_id=operation_id,
                    cell_id=cell_id,
                    operation_kind=operation_kind,
                    payload={"reservation": reservation.to_dict()},
                )
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)

    def start(self, operation_id: str) -> JournalEvent:
        operation_id = _safe_identifier(operation_id, "operation id")
        operation = self._record(operation_id)
        if operation is None:
            raise OperationStateError("operation is not reserved")
        if operation.state == "started":
            return operation.event_for("operation_started")
        if operation.state in {"completed", "failed"}:
            raise OperationStateError("operation is already terminal")
        return self.journal._append(
            event_type="operation_started",
            operation_id=operation.operation_id,
            cell_id=operation.cell_id,
            operation_kind=operation.operation_kind,
            payload={},
        )

    def complete(
        self,
        operation_id: str,
        *,
        actual_usage: ResourceVector | None = None,
        artifact_sha256: str | None = None,
    ) -> JournalEvent:
        return self._terminal(
            operation_id,
            event_type="operation_completed",
            actual_usage=actual_usage,
            artifact_sha256=artifact_sha256,
            reason_code=None,
        )

    def fail(
        self,
        operation_id: str,
        *,
        reason_code: str,
        actual_usage: ResourceVector | None = None,
        artifact_sha256: str | None = None,
    ) -> JournalEvent:
        return self._terminal(
            operation_id,
            event_type="operation_failed",
            actual_usage=actual_usage,
            artifact_sha256=artifact_sha256,
            reason_code=reason_code,
        )

    def _terminal(
        self,
        operation_id: str,
        *,
        event_type: str,
        actual_usage: ResourceVector | None,
        artifact_sha256: str | None,
        reason_code: str | None,
    ) -> JournalEvent:
        operation_id = _safe_identifier(operation_id, "operation id")
        operation = self._record(operation_id)
        if operation is None:
            raise OperationStateError("operation is not reserved")
        payload = _terminal_payload(
            reservation=operation.reservation,
            actual_usage=actual_usage,
            artifact_sha256=artifact_sha256,
            reason_code=reason_code,
        )
        if operation.state in {"completed", "failed"}:
            expected_state = (
                "completed" if event_type == "operation_completed" else "failed"
            )
            if operation.state != expected_state:
                raise OperationStateError("operation is already terminal")
            event = operation.event_for(event_type)
            if event.payload != payload:
                raise OperationStateError(
                    "operation has different terminal result content"
                )
            return event
        if operation.state != "started":
            raise OperationStateError("operation must be started before a terminal event")
        return self.journal._append(
            event_type=event_type,
            operation_id=operation.operation_id,
            cell_id=operation.cell_id,
            operation_kind=operation.operation_kind,
            payload=payload,
        )
