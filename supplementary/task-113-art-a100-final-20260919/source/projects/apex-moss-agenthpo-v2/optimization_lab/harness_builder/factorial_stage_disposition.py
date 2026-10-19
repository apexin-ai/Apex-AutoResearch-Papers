"""Semantic-only exact stage dispositions for the factorial experiment.

This module closes one zero-call accounting gap: it aligns one semantic replay
of a journal with the pinned 4,338-stage potential-operation schedule and can
prove either a terminal ``completed``/``failed`` record or an immediate-parent
short circuit.  It deliberately does *not* make the journal formal authority.

The current v1 journal reader is not descriptor-relative, has no frozen storage
grant or crash-WAL protocol, and the logical-to-physical retry identity is not
yet frozen.  Consequently every artifact here remains ``NOT_READY`` and
``NOT_GRANTED`` even when all 4,338 semantic dispositions form an exact set.
There is no writer, governor, provider, evaluator, or execution callback here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import re
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from .events import (
    JournalEvent,
    JournalIntegrityError,
    JournalReplay,
    OperationRecord,
    ResourceVector,
    _event_from_raw,
    _replay_events,
    verify_operation_journal,
)
from .factorial_coverage import (
    ExactFactorialAttemptMatrix,
)
from .factorial_operation_schedule import (
    ExactFactorialOperationSchedule,
    FactorialPotentialOperation,
)
from .factorial_precheck import FactorialFormalZeroCallPlan
from .factorial_task_authority import (
    ExactTaskSeedAuthorityBundle,
    FactorialTaskArtifactAuthority,
)


EXECUTION_AUTHORITY = "NOT_GRANTED"
FORMAL_READINESS = "NOT_READY"
CLAIM_SCOPE = "SEMANTIC_REPLAY_OR_FIXTURE_ONLY_NOT_FORMAL_EXECUTION_EVIDENCE"
JOURNAL_STORAGE_STATUS = "HARDENED_DESCRIPTOR_RELATIVE_JOURNAL_PENDING"
PHYSICAL_OPERATION_BINDING_STATUS = (
    "LOGICAL_OPERATION_ID_ONLY_PHYSICAL_RETRY_BINDING_PENDING"
)
STANDALONE_VIEW_STATUS = (
    "STRUCTURAL_VIEW_ONLY_VERIFY_WITH_PINNED_SOURCE_AND_JOURNAL_REPLAY_API"
)
VERIFICATION_CONTRACT = (
    "ONLY_ACCEPT_RETURN_VALUE_OF_VERIFY_SERIALIZED_EXACT_SEMANTIC_ARTIFACT;"
    "TYPE_IDENTITY_PRIVATE_FACTORY_AND_CONTENT_HASH_ARE_NOT_PROVENANCE"
)
_ARTIFACT_KIND = "factorial_exact_semantic_stage_disposition_artifact_v1"
_MAX_ARTIFACT_BYTES = 32 * 1024 * 1024
BLOCKERS = (
    "BOUNDED_DESCRIPTOR_REPLAY_PENDING",
    "CRASH_RECOVERY_PROTOCOL_PENDING",
    "FORMAL_SCHEDULER_BARRIER_ORDER_REPLAY_PENDING",
    "HARDENED_JOURNAL_AND_ANCHOR_PATH_REPLAY_PENDING",
    "PARENT_ARTIFACT_TRUSTED_REPLAY_PENDING",
    "PHYSICAL_RETRY_SCHEMA_PENDING",
    "PROVIDER_EVALUATOR_DISPATCH_PENDING",
    "RESOURCE_GRANT_AND_PHYSICAL_OPERATION_BINDING_PENDING",
    "TRUSTED_STORAGE_GRANT_PENDING",
    "TYPED_GATE_REJECTION_AND_ABANDONMENT_RECEIPTS_PENDING",
)

_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_TERMINAL_STATES = {"completed", "failed"}
_PROOF_KINDS = {"PARENT_OPERATION_FAILED", "PARENT_SKIPPED_BY_PARENT"}


class FactorialStageDispositionError(ValueError):
    """A semantic disposition differs from pinned schedule or journal facts."""


def _canonical_bytes(payload: object) -> bytes:
    try:
        return (
            json.dumps(
                payload,
                allow_nan=False,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeError) as exc:
        raise FactorialStageDispositionError(
            "stage disposition is not canonical JSON"
        ) from exc


def _sha(value: object, label: str, *, allow_zero: bool = False) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise FactorialStageDispositionError(f"invalid {label}")
    if not allow_zero and value == "0" * 64:
        raise FactorialStageDispositionError(f"empty {label}")
    return value


def _safe(value: object, label: str) -> str:
    if (
        not isinstance(value, str)
        or _SAFE_ID.fullmatch(value) is None
        or ".." in value
        or "//" in value
        or value.endswith("/")
    ):
        raise FactorialStageDispositionError(f"unsafe {label}")
    return value


@dataclass(frozen=True)
class _FrozenOperationRecord:
    """Private immutable projection of one independently reduced record."""

    operation_id: str
    cell_id: str
    operation_kind: str
    reservation: ResourceVector
    state: str
    committed_usage: ResourceVector
    event_sha256s: tuple[str, ...]
    first_sequence: int
    started_sequence: int | None
    terminal_sequence: int
    terminal_event_type: str
    terminal_event_sha256: str
    usage_known: bool | None
    artifact_sha256: str | None
    failure_reason_code: str | None


@dataclass(frozen=True)
class _FrozenSemanticReplay:
    """A deep, immutable snapshot; it never retains a mutable event payload."""

    operations: Mapping[str, _FrozenOperationRecord]
    event_count: int
    head_sha256: str


def _resource_copy(value: ResourceVector) -> ResourceVector:
    if type(value) is not ResourceVector:
        raise FactorialStageDispositionError(
            "semantic operation resource projection differs"
        )
    return ResourceVector.from_dict(value.to_dict())


def _operation_record_sha256(record: OperationRecord | _FrozenOperationRecord) -> str:
    """Hash one record without retaining caller-owned nested payloads."""

    if type(record) is OperationRecord:
        if not record.events:
            raise FactorialStageDispositionError(
                "semantic operation record projection differs"
            )
        event_sha256s = tuple(event.event_sha256 for event in record.events)
    elif type(record) is _FrozenOperationRecord:
        event_sha256s = record.event_sha256s
        if not event_sha256s:
            raise FactorialStageDispositionError(
                "semantic operation record projection differs"
            )
    else:
        raise FactorialStageDispositionError(
            "semantic operation record projection differs"
        )
    return hashlib.sha256(
        _canonical_bytes(
            {
                "cell_id": record.cell_id,
                "committed_usage": record.committed_usage.to_dict(),
                "event_sha256s": list(event_sha256s),
                "operation_id": record.operation_id,
                "operation_kind": record.operation_kind,
                "reservation": record.reservation.to_dict(),
                "schema_version": 1,
                "state": record.state,
            }
        )
    ).hexdigest()


def _freeze_verified_replay(replay: JournalReplay) -> _FrozenSemanticReplay:
    """Reparse and reduce one canonical copy of a v1 replay.

    ``JournalEvent`` is frozen but its historical ``payload`` field is a mutable
    ``dict``.  Merely wrapping ``operations`` in ``MappingProxyType`` would
    therefore leave artifact and usage facts mutable after verifier creation.
    This boundary serializes each event exactly once, reparses its hash chain,
    independently reduces the copied events, and retains only primitive fields
    plus freshly constructed immutable ``ResourceVector`` values.
    """

    if type(replay) is not JournalReplay:
        raise FactorialStageDispositionError(
            "semantic verifier requires one v1 journal replay"
        )
    copied_events: list[JournalEvent] = []
    previous = "0" * 64
    try:
        for expected_sequence, source_event in enumerate(replay.events, start=1):
            if type(source_event) is not JournalEvent:
                raise FactorialStageDispositionError(
                    "semantic journal event projection differs"
                )
            # JSON round-trip is the deep-copy boundary.  The event parser then
            # recomputes the content hash over that exact copied payload.
            raw = json.loads(
                json.dumps(
                    source_event.to_dict(),
                    allow_nan=False,
                    ensure_ascii=False,
                    separators=(",", ":"),
                    sort_keys=True,
                )
            )
            copied = _event_from_raw(
                raw,
                expected_sequence=expected_sequence,
                previous_sha=previous,
            )
            copied_events.append(copied)
            previous = copied.event_sha256
        rebuilt = _replay_events(copied_events)
    except (JournalIntegrityError, TypeError, ValueError, UnicodeError) as exc:
        raise FactorialStageDispositionError(
            "semantic journal changed after verified replay"
        ) from exc
    if (
        type(replay.event_count) is not int
        or replay.event_count != len(copied_events)
        or replay.head_sha256 != previous
        or set(replay.operations) != set(rebuilt)
    ):
        raise FactorialStageDispositionError(
            "semantic replay count, head, or operation set differs"
        )
    for operation_id, original in replay.operations.items():
        if (
            type(original) is not OperationRecord
            or _operation_record_sha256(original)
            != _operation_record_sha256(rebuilt[operation_id])
        ):
            raise FactorialStageDispositionError(
                "semantic replay operation projection differs"
            )

    frozen: dict[str, _FrozenOperationRecord] = {}
    for operation_id, record in rebuilt.items():
        terminal = record.events[-1]
        is_terminal = record.state in _TERMINAL_STATES
        payload = terminal.payload if is_terminal else {}
        frozen[operation_id] = _FrozenOperationRecord(
            operation_id=record.operation_id,
            cell_id=record.cell_id,
            operation_kind=record.operation_kind,
            reservation=_resource_copy(record.reservation),
            state=record.state,
            committed_usage=_resource_copy(record.committed_usage),
            event_sha256s=tuple(event.event_sha256 for event in record.events),
            first_sequence=record.events[0].sequence,
            started_sequence=next(
                (
                    event.sequence
                    for event in record.events
                    if event.event_type == "operation_started"
                ),
                None,
            ),
            terminal_sequence=terminal.sequence,
            terminal_event_type=terminal.event_type,
            terminal_event_sha256=terminal.event_sha256,
            usage_known=payload.get("usage_known"),
            artifact_sha256=payload.get("artifact_sha256"),
            failure_reason_code=(
                payload.get("reason_code") if record.state == "failed" else None
            ),
        )
    return _FrozenSemanticReplay(
        operations=MappingProxyType(frozen),
        event_count=len(copied_events),
        head_sha256=previous,
    )


@dataclass(frozen=True)
class SemanticJournalOperationReceipt:
    """Structural terminal view; persisted trust requires full replay verification."""

    schedule_sha256: str
    potential_operation_sha256: str
    matrix_sha256: str
    slot_sha256: str
    task_seed_key_sha256: str
    logical_operation_id: str
    observed_journal_operation_id: str
    cell_id: str
    stage: str
    journal_operation_kind: str
    semantic_snapshot_event_count: int
    semantic_snapshot_head_sha256: str
    operation_record_sha256: str
    journal_state: str
    terminal_event_sha256: str
    reservation: ResourceVector
    committed_usage: ResourceVector
    usage_known: bool
    terminal_artifact_sha256: str | None
    terminal_failure_reason_code: str | None
    disposition: str = "executed"
    execution_authority: str = EXECUTION_AUTHORITY
    formal_readiness: str = FORMAL_READINESS
    claim_scope: str = CLAIM_SCOPE
    journal_storage_status: str = JOURNAL_STORAGE_STATUS
    physical_operation_binding_status: str = PHYSICAL_OPERATION_BINDING_STATUS
    standalone_view_status: str = STANDALONE_VIEW_STATUS
    schema_version: int = 1
    receipt_kind: str = "factorial_semantic_journal_operation_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "factorial_semantic_journal_operation_receipt_v1"
        ):
            raise FactorialStageDispositionError(
                "unsupported semantic operation receipt schema"
            )
        for value, label in (
            (self.schedule_sha256, "schedule sha256"),
            (self.potential_operation_sha256, "potential operation sha256"),
            (self.matrix_sha256, "matrix sha256"),
            (self.slot_sha256, "slot sha256"),
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.semantic_snapshot_head_sha256, "semantic snapshot head sha256"),
            (self.operation_record_sha256, "operation record sha256"),
            (self.terminal_event_sha256, "terminal event sha256"),
        ):
            _sha(value, label)
        for value, label in (
            (self.logical_operation_id, "logical operation id"),
            (self.observed_journal_operation_id, "observed journal operation id"),
            (self.cell_id, "cell id"),
            (self.stage, "stage"),
            (self.journal_operation_kind, "journal operation kind"),
        ):
            _safe(value, label)
        if self.logical_operation_id != self.observed_journal_operation_id:
            raise FactorialStageDispositionError(
                "logical/physical retry binding is not frozen"
            )
        if (
            type(self.semantic_snapshot_event_count) is not int
            or self.semantic_snapshot_event_count < 3
            or self.journal_state not in _TERMINAL_STATES
            or type(self.reservation) is not ResourceVector
            or type(self.committed_usage) is not ResourceVector
            or type(self.usage_known) is not bool
        ):
            raise FactorialStageDispositionError(
                "semantic operation terminal projection differs"
            )
        if self.terminal_artifact_sha256 is not None:
            _sha(self.terminal_artifact_sha256, "terminal artifact sha256")
        if self.journal_state == "completed":
            if (
                self.terminal_artifact_sha256 is None
                or self.terminal_failure_reason_code is not None
            ):
                raise FactorialStageDispositionError(
                    "completed operation requires an artifact and no failure reason"
                )
        else:
            _safe(self.terminal_failure_reason_code, "terminal failure reason")
        if (
            self.disposition != "executed"
            or self.execution_authority != EXECUTION_AUTHORITY
            or self.formal_readiness != FORMAL_READINESS
            or self.claim_scope != CLAIM_SCOPE
            or self.journal_storage_status != JOURNAL_STORAGE_STATUS
            or self.physical_operation_binding_status
            != PHYSICAL_OPERATION_BINDING_STATUS
            or self.standalone_view_status != STANDALONE_VIEW_STATUS
        ):
            raise FactorialStageDispositionError(
                "semantic receipt overstates execution authority"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "cell_id": self.cell_id,
            "claim_scope": self.claim_scope,
            "committed_usage": self.committed_usage.to_dict(),
            "disposition": self.disposition,
            "execution_authority": self.execution_authority,
            "formal_readiness": self.formal_readiness,
            "journal_operation_kind": self.journal_operation_kind,
            "journal_state": self.journal_state,
            "journal_storage_status": self.journal_storage_status,
            "logical_operation_id": self.logical_operation_id,
            "matrix_sha256": self.matrix_sha256,
            "observed_journal_operation_id": self.observed_journal_operation_id,
            "operation_record_sha256": self.operation_record_sha256,
            "physical_operation_binding_status": (
                self.physical_operation_binding_status
            ),
            "potential_operation_sha256": self.potential_operation_sha256,
            "receipt_kind": self.receipt_kind,
            "reservation": self.reservation.to_dict(),
            "schedule_sha256": self.schedule_sha256,
            "schema_version": self.schema_version,
            "semantic_snapshot_event_count": self.semantic_snapshot_event_count,
            "semantic_snapshot_head_sha256": self.semantic_snapshot_head_sha256,
            "slot_sha256": self.slot_sha256,
            "standalone_view_status": self.standalone_view_status,
            "stage": self.stage,
            "task_seed_key_sha256": self.task_seed_key_sha256,
            "terminal_artifact_sha256": self.terminal_artifact_sha256,
            "terminal_event_sha256": self.terminal_event_sha256,
            "terminal_failure_reason_code": self.terminal_failure_reason_code,
            "usage_known": self.usage_known,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class SemanticSkippedByParentReceipt:
    """Structural skip view; persisted trust requires full replay verification."""

    schedule_sha256: str
    child_potential_operation_sha256: str
    child_logical_operation_id: str
    child_stage: str
    parent_potential_operation_sha256: str
    parent_logical_operation_id: str
    parent_stage: str
    parent_disposition_sha256: str
    proof_kind: str
    matrix_sha256: str
    slot_sha256: str
    task_seed_key_sha256: str
    attempt_id: str
    semantic_snapshot_event_count: int
    semantic_snapshot_head_sha256: str
    disposition: str = "skipped-by-parent"
    execution_authority: str = EXECUTION_AUTHORITY
    formal_readiness: str = FORMAL_READINESS
    claim_scope: str = CLAIM_SCOPE
    journal_storage_status: str = JOURNAL_STORAGE_STATUS
    physical_operation_binding_status: str = PHYSICAL_OPERATION_BINDING_STATUS
    standalone_view_status: str = STANDALONE_VIEW_STATUS
    schema_version: int = 1
    receipt_kind: str = "factorial_semantic_skipped_by_parent_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "factorial_semantic_skipped_by_parent_receipt_v1"
        ):
            raise FactorialStageDispositionError(
                "unsupported semantic skip receipt schema"
            )
        for value, label in (
            (self.schedule_sha256, "schedule sha256"),
            (self.child_potential_operation_sha256, "child operation sha256"),
            (self.parent_potential_operation_sha256, "parent operation sha256"),
            (self.parent_disposition_sha256, "parent disposition sha256"),
            (self.matrix_sha256, "matrix sha256"),
            (self.slot_sha256, "slot sha256"),
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.semantic_snapshot_head_sha256, "semantic snapshot head sha256"),
        ):
            _sha(value, label)
        for value, label in (
            (self.child_logical_operation_id, "child operation id"),
            (self.child_stage, "child stage"),
            (self.parent_logical_operation_id, "parent operation id"),
            (self.parent_stage, "parent stage"),
            (self.attempt_id, "attempt id"),
        ):
            _safe(value, label)
        if (
            self.proof_kind not in _PROOF_KINDS
            or type(self.semantic_snapshot_event_count) is not int
            or self.semantic_snapshot_event_count < 3
            or self.disposition != "skipped-by-parent"
            or self.execution_authority != EXECUTION_AUTHORITY
            or self.formal_readiness != FORMAL_READINESS
            or self.claim_scope != CLAIM_SCOPE
            or self.journal_storage_status != JOURNAL_STORAGE_STATUS
            or self.physical_operation_binding_status
            != PHYSICAL_OPERATION_BINDING_STATUS
            or self.standalone_view_status != STANDALONE_VIEW_STATUS
        ):
            raise FactorialStageDispositionError(
                "semantic skip receipt overstates authority or proof"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_id": self.attempt_id,
            "child_logical_operation_id": self.child_logical_operation_id,
            "child_potential_operation_sha256": (
                self.child_potential_operation_sha256
            ),
            "child_stage": self.child_stage,
            "claim_scope": self.claim_scope,
            "disposition": self.disposition,
            "execution_authority": self.execution_authority,
            "formal_readiness": self.formal_readiness,
            "journal_storage_status": self.journal_storage_status,
            "matrix_sha256": self.matrix_sha256,
            "parent_disposition_sha256": self.parent_disposition_sha256,
            "parent_logical_operation_id": self.parent_logical_operation_id,
            "parent_potential_operation_sha256": (
                self.parent_potential_operation_sha256
            ),
            "parent_stage": self.parent_stage,
            "physical_operation_binding_status": (
                self.physical_operation_binding_status
            ),
            "proof_kind": self.proof_kind,
            "receipt_kind": self.receipt_kind,
            "schedule_sha256": self.schedule_sha256,
            "schema_version": self.schema_version,
            "semantic_snapshot_event_count": self.semantic_snapshot_event_count,
            "semantic_snapshot_head_sha256": self.semantic_snapshot_head_sha256,
            "slot_sha256": self.slot_sha256,
            "standalone_view_status": self.standalone_view_status,
            "task_seed_key_sha256": self.task_seed_key_sha256,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


SemanticDisposition = SemanticJournalOperationReceipt | SemanticSkippedByParentReceipt


@dataclass(frozen=True, init=False)
class ExactSemanticDispositionSeal:
    """A structural view produced by a verifier, never standalone provenance.

    Persisted bytes are meaningful only after
    :func:`verify_serialized_exact_semantic_artifact` rederives them from the
    pinned sources and current ledger/head.  Disabling public dataclass
    construction also prevents ``dataclasses.replace`` from carrying an
    apparent private token into a forged copy.
    """

    schedule_sha256: str
    matrix_sha256: str
    factorial_plan_sha256: str
    task_authority_bundle_sha256: str
    semantic_snapshot_event_count: int
    semantic_snapshot_head_sha256: str
    potential_stage_count: int
    submitted_disposition_count: int
    executed_count: int
    terminal_completed_count: int
    terminal_failed_count: int
    skipped_by_parent_count: int
    disposition_sha256s: tuple[str, ...]
    exact_disposition_set_complete: bool = True
    semantic_journal_operation_set_exact: bool = True
    formal_execution_ready: bool = False
    blockers: tuple[str, ...] = BLOCKERS
    execution_authority: str = EXECUTION_AUTHORITY
    formal_readiness: str = FORMAL_READINESS
    claim_scope: str = CLAIM_SCOPE
    journal_storage_status: str = JOURNAL_STORAGE_STATUS
    physical_operation_binding_status: str = PHYSICAL_OPERATION_BINDING_STATUS
    standalone_view_status: str = STANDALONE_VIEW_STATUS
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    gpu_exclusive_second_entitlement: int = 0
    cpu_evaluator_second_entitlement: int = 0
    schema_version: int = 1
    seal_kind: str = "factorial_exact_semantic_stage_disposition_seal_v1"
    def __init__(self, *_args: object, **_kwargs: object) -> None:
        raise FactorialStageDispositionError(
            "semantic disposition seal requires pinned replay derivation"
        )

    @classmethod
    def _from_derived(
        cls,
        *,
        schedule_sha256: str,
        matrix_sha256: str,
        factorial_plan_sha256: str,
        task_authority_bundle_sha256: str,
        semantic_snapshot_event_count: int,
        semantic_snapshot_head_sha256: str,
        potential_stage_count: int,
        submitted_disposition_count: int,
        executed_count: int,
        terminal_completed_count: int,
        terminal_failed_count: int,
        skipped_by_parent_count: int,
        disposition_sha256s: tuple[str, ...],
    ) -> "ExactSemanticDispositionSeal":
        instance = object.__new__(cls)
        values: dict[str, object] = {
            "schedule_sha256": schedule_sha256,
            "matrix_sha256": matrix_sha256,
            "factorial_plan_sha256": factorial_plan_sha256,
            "task_authority_bundle_sha256": task_authority_bundle_sha256,
            "semantic_snapshot_event_count": semantic_snapshot_event_count,
            "semantic_snapshot_head_sha256": semantic_snapshot_head_sha256,
            "potential_stage_count": potential_stage_count,
            "submitted_disposition_count": submitted_disposition_count,
            "executed_count": executed_count,
            "terminal_completed_count": terminal_completed_count,
            "terminal_failed_count": terminal_failed_count,
            "skipped_by_parent_count": skipped_by_parent_count,
            "disposition_sha256s": disposition_sha256s,
            "exact_disposition_set_complete": True,
            "semantic_journal_operation_set_exact": True,
            "formal_execution_ready": False,
            "blockers": BLOCKERS,
            "execution_authority": EXECUTION_AUTHORITY,
            "formal_readiness": FORMAL_READINESS,
            "claim_scope": CLAIM_SCOPE,
            "journal_storage_status": JOURNAL_STORAGE_STATUS,
            "physical_operation_binding_status": (
                PHYSICAL_OPERATION_BINDING_STATUS
            ),
            "standalone_view_status": STANDALONE_VIEW_STATUS,
            "model_call_entitlement": 0,
            "evaluator_transaction_entitlement": 0,
            "gpu_exclusive_second_entitlement": 0,
            "cpu_evaluator_second_entitlement": 0,
            "schema_version": 1,
            "seal_kind": "factorial_exact_semantic_stage_disposition_seal_v1",
        }
        for name, value in values.items():
            object.__setattr__(instance, name, value)
        instance._validate()
        return instance

    def _validate(self) -> None:
        if self.schema_version != 1 or self.seal_kind != (
            "factorial_exact_semantic_stage_disposition_seal_v1"
        ):
            raise FactorialStageDispositionError(
                "unsupported semantic disposition seal schema"
            )
        for value, label in (
            (self.schedule_sha256, "schedule sha256"),
            (self.matrix_sha256, "matrix sha256"),
            (self.factorial_plan_sha256, "plan sha256"),
            (self.task_authority_bundle_sha256, "authority bundle sha256"),
            (self.semantic_snapshot_head_sha256, "semantic snapshot head sha256"),
        ):
            _sha(value, label)
        counts = (
            self.potential_stage_count,
            self.submitted_disposition_count,
            self.executed_count,
            self.terminal_completed_count,
            self.terminal_failed_count,
            self.skipped_by_parent_count,
        )
        if any(type(value) is not int or value < 0 for value in counts) or (
            self.potential_stage_count != 4338
            or self.submitted_disposition_count != 4338
            or type(self.disposition_sha256s) is not tuple
            or len(self.disposition_sha256s) != 4338
            or len(set(self.disposition_sha256s)) != 4338
            or self.executed_count
            != self.terminal_completed_count + self.terminal_failed_count
            or self.executed_count + self.skipped_by_parent_count != 4338
        ):
            raise FactorialStageDispositionError(
                "semantic exact-set disposition counts differ"
            )
        for value in self.disposition_sha256s:
            _sha(value, "disposition sha256")
        if (
            type(self.semantic_snapshot_event_count) is not int
            or self.semantic_snapshot_event_count < 3
            or self.exact_disposition_set_complete is not True
            or self.semantic_journal_operation_set_exact is not True
            or self.formal_execution_ready is not False
            or self.blockers != BLOCKERS
            or self.execution_authority != EXECUTION_AUTHORITY
            or self.formal_readiness != FORMAL_READINESS
            or self.claim_scope != CLAIM_SCOPE
            or self.journal_storage_status != JOURNAL_STORAGE_STATUS
            or self.physical_operation_binding_status
            != PHYSICAL_OPERATION_BINDING_STATUS
            or self.standalone_view_status != STANDALONE_VIEW_STATUS
            or any(
                type(value) is not int or value != 0
                for value in (
                    self.model_call_entitlement,
                    self.evaluator_transaction_entitlement,
                    self.gpu_exclusive_second_entitlement,
                    self.cpu_evaluator_second_entitlement,
                )
            )
        ):
            raise FactorialStageDispositionError(
                "semantic exact-set seal overstates formal readiness"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "blockers": list(self.blockers),
            "claim_scope": self.claim_scope,
            "disposition_sha256s": list(self.disposition_sha256s),
            "evaluator_transaction_entitlement": (
                self.evaluator_transaction_entitlement
            ),
            "exact_disposition_set_complete": self.exact_disposition_set_complete,
            "executed_count": self.executed_count,
            "execution_authority": self.execution_authority,
            "factorial_plan_sha256": self.factorial_plan_sha256,
            "formal_execution_ready": self.formal_execution_ready,
            "formal_readiness": self.formal_readiness,
            "gpu_exclusive_second_entitlement": (
                self.gpu_exclusive_second_entitlement
            ),
            "cpu_evaluator_second_entitlement": (
                self.cpu_evaluator_second_entitlement
            ),
            "journal_storage_status": self.journal_storage_status,
            "matrix_sha256": self.matrix_sha256,
            "model_call_entitlement": self.model_call_entitlement,
            "physical_operation_binding_status": (
                self.physical_operation_binding_status
            ),
            "potential_stage_count": self.potential_stage_count,
            "schema_version": self.schema_version,
            "seal_kind": self.seal_kind,
            "standalone_view_status": self.standalone_view_status,
            "semantic_journal_operation_set_exact": (
                self.semantic_journal_operation_set_exact
            ),
            "semantic_snapshot_event_count": self.semantic_snapshot_event_count,
            "semantic_snapshot_head_sha256": self.semantic_snapshot_head_sha256,
            "schedule_sha256": self.schedule_sha256,
            "skipped_by_parent_count": self.skipped_by_parent_count,
            "submitted_disposition_count": self.submitted_disposition_count,
            "task_authority_bundle_sha256": self.task_authority_bundle_sha256,
            "terminal_completed_count": self.terminal_completed_count,
            "terminal_failed_count": self.terminal_failed_count,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


class FactorialSemanticDispositionVerifier:
    """One-replay semantic verifier over the exact pinned operation schedule."""

    def __init__(
        self,
        *,
        schedule: ExactFactorialOperationSchedule,
        replay: JournalReplay,
        _trusted_source_replay: object | None = None,
    ) -> None:
        if _trusted_source_replay is not _TRUSTED_SOURCE_REPLAY:
            raise FactorialStageDispositionError(
                "semantic verifier requires pinned source and journal replay"
            )
        if type(schedule) is not ExactFactorialOperationSchedule or type(
            replay
        ) is not JournalReplay:
            raise FactorialStageDispositionError(
                "exact schedule and semantic journal replay are required"
            )
        # Freeze and independently reduce a deep canonical copy.  The v1 DTO's
        # nested payload dicts are mutable despite the outer frozen dataclasses.
        frozen_replay = _freeze_verified_replay(replay)
        self._schedule = schedule
        self._schedule_sha256 = schedule.sha256
        self._replay = frozen_replay
        self._operations = {
            item.logical_operation_id: item for item in schedule.operations
        }
        extras = set(frozen_replay.operations) - set(self._operations)
        if extras:
            raise FactorialStageDispositionError(
                "journal contains an operation outside the exact schedule"
            )
        self._operation_record_sha256s = {
            operation_id: _operation_record_sha256(record)
            for operation_id, record in frozen_replay.operations.items()
        }
        by_attempt: dict[str, list[FactorialPotentialOperation]] = {}
        for operation in schedule.operations:
            by_attempt.setdefault(operation.attempt_id, []).append(operation)
        self._immediate_parent: dict[str, FactorialPotentialOperation] = {}
        for attempt_operations in by_attempt.values():
            for parent, child in zip(attempt_operations, attempt_operations[1:]):
                if child.stage_ordinal != parent.stage_ordinal + 1:
                    raise FactorialStageDispositionError(
                        "exact schedule contains a non-immediate stage edge"
                    )
                self._immediate_parent[child.logical_operation_id] = parent
        self._issued: dict[str, SemanticDisposition] = {}
        self._issued_by_operation: dict[str, SemanticDisposition] = {}

    @property
    def potential_operations(self) -> tuple[FactorialPotentialOperation, ...]:
        return self._schedule.operations

    @property
    def schedule_sha256(self) -> str:
        return self._schedule_sha256

    @classmethod
    def from_verified_sources(
        cls,
        *,
        matrix: ExactFactorialAttemptMatrix,
        plan: FactorialFormalZeroCallPlan,
        bundle: ExactTaskSeedAuthorityBundle,
        task_authority: FactorialTaskArtifactAuthority,
        ledger_path: Path,
        anchor_path: Path,
    ) -> "FactorialSemanticDispositionVerifier":
        schedule = ExactFactorialOperationSchedule.from_verified_sources(
            matrix=matrix,
            plan=plan,
            bundle=bundle,
            task_authority=task_authority,
        )
        # Exactly one semantic replay is held for every receipt and the final
        # seal.  It is intentionally not called a hardened/formal replay.
        replay = verify_operation_journal(
            Path(ledger_path), anchor_path=Path(anchor_path)
        )
        return cls(
            schedule=schedule,
            replay=replay,
            _trusted_source_replay=_TRUSTED_SOURCE_REPLAY,
        )

    def _operation(self, logical_operation_id: str) -> FactorialPotentialOperation:
        _safe(logical_operation_id, "logical operation id")
        try:
            return self._operations[logical_operation_id]
        except KeyError as exc:
            raise FactorialStageDispositionError(
                "operation is absent from the exact schedule"
            ) from exc

    def _expected_executed(
        self, operation: FactorialPotentialOperation
    ) -> SemanticJournalOperationReceipt:
        record = self._replay.operations.get(operation.logical_operation_id)
        if record is None:
            raise FactorialStageDispositionError(
                "executed operation is absent from semantic journal snapshot"
            )
        if type(record) is not _FrozenOperationRecord or record.state not in _TERMINAL_STATES:
            raise FactorialStageDispositionError(
                "reserved/started operation cannot be semantically sealed"
            )
        if (
            record.operation_id != operation.logical_operation_id
            or record.cell_id != operation.cell_id
            or record.operation_kind != operation.journal_operation_kind
            or record.reservation != operation.full_path_reservation
        ):
            raise FactorialStageDispositionError(
                "journal operation identity, kind, or reservation differs"
            )
        immediate_parent = self._immediate_parent.get(operation.logical_operation_id)
        if immediate_parent is not None:
            parent_record = self._replay.operations.get(
                immediate_parent.logical_operation_id
            )
            if (
                parent_record is None
                or parent_record.state != "completed"
                or parent_record.artifact_sha256 is None
            ):
                raise FactorialStageDispositionError(
                    "executed stage follows an absent, failed, or nonterminal parent"
                )
            if (
                record.started_sequence is None
                or record.started_sequence <= parent_record.terminal_sequence
            ):
                raise FactorialStageDispositionError(
                    "child operation was started before parent terminal"
                )
        expected_terminal_type = (
            "operation_completed"
            if record.state == "completed"
            else "operation_failed"
        )
        if record.terminal_event_type != expected_terminal_type:
            raise FactorialStageDispositionError(
                "journal terminal event and record state differ"
            )
        if record.state == "completed" and record.artifact_sha256 is None:
            raise FactorialStageDispositionError(
                "completed operation without an artifact cannot advance"
            )
        return SemanticJournalOperationReceipt(
            schedule_sha256=self._schedule_sha256,
            potential_operation_sha256=operation.sha256,
            matrix_sha256=operation.matrix_sha256,
            slot_sha256=operation.slot_sha256,
            task_seed_key_sha256=operation.task_seed_key_sha256,
            logical_operation_id=operation.logical_operation_id,
            observed_journal_operation_id=record.operation_id,
            cell_id=operation.cell_id,
            stage=operation.stage,
            journal_operation_kind=operation.journal_operation_kind,
            semantic_snapshot_event_count=self._replay.event_count,
            semantic_snapshot_head_sha256=self._replay.head_sha256,
            operation_record_sha256=self._operation_record_sha256s[
                record.operation_id
            ],
            journal_state=record.state,
            terminal_event_sha256=record.terminal_event_sha256,
            reservation=record.reservation,
            committed_usage=record.committed_usage,
            usage_known=record.usage_known,
            terminal_artifact_sha256=record.artifact_sha256,
            terminal_failure_reason_code=record.failure_reason_code,
        )

    def executed(self, logical_operation_id: str) -> SemanticJournalOperationReceipt:
        operation = self._operation(logical_operation_id)
        existing = self._issued_by_operation.get(operation.logical_operation_id)
        if existing is not None:
            if isinstance(existing, SemanticJournalOperationReceipt):
                return existing
            raise FactorialStageDispositionError(
                "operation was already issued as a skipped disposition"
            )
        immediate_parent = self._immediate_parent.get(operation.logical_operation_id)
        if immediate_parent is not None:
            parent = self._issued_by_operation.get(
                immediate_parent.logical_operation_id
            )
            if parent is not None and (
                isinstance(parent, SemanticSkippedByParentReceipt)
                or (
                    isinstance(parent, SemanticJournalOperationReceipt)
                    and parent.journal_state == "failed"
                )
            ):
                raise FactorialStageDispositionError(
                    "executed stage follows a failed or skipped parent"
                )
        receipt = self._expected_executed(operation)
        self._issued[receipt.sha256] = receipt
        self._issued_by_operation[operation.logical_operation_id] = receipt
        return receipt

    def _expected_skip(
        self,
        *,
        child: FactorialPotentialOperation,
        parent: SemanticDisposition,
    ) -> SemanticSkippedByParentReceipt:
        expected_parent = self._immediate_parent.get(child.logical_operation_id)
        if expected_parent is None:
            raise FactorialStageDispositionError(
                "root stage cannot be skipped by a parent"
            )
        parent_operation_id = (
            parent.logical_operation_id
            if isinstance(parent, SemanticJournalOperationReceipt)
            else parent.child_logical_operation_id
        )
        parent_operation_sha256 = (
            parent.potential_operation_sha256
            if isinstance(parent, SemanticJournalOperationReceipt)
            else parent.child_potential_operation_sha256
        )
        if (
            parent_operation_id != expected_parent.logical_operation_id
            or parent_operation_sha256 != expected_parent.sha256
            or child.attempt_id != expected_parent.attempt_id
        ):
            raise FactorialStageDispositionError(
                "skip proof is not the immediate same-attempt parent"
            )
        if self._replay.operations.get(child.logical_operation_id) is not None:
            raise FactorialStageDispositionError(
                "skipped child has a journal operation record"
            )
        if isinstance(parent, SemanticJournalOperationReceipt):
            if parent.journal_state != "failed":
                raise FactorialStageDispositionError(
                    "completed parent needs a typed gate rejection receipt"
                )
            proof_kind = "PARENT_OPERATION_FAILED"
        elif isinstance(parent, SemanticSkippedByParentReceipt):
            proof_kind = "PARENT_SKIPPED_BY_PARENT"
        else:  # pragma: no cover - the public annotation is already exact.
            raise FactorialStageDispositionError("unsupported parent disposition")
        return SemanticSkippedByParentReceipt(
            schedule_sha256=self._schedule_sha256,
            child_potential_operation_sha256=child.sha256,
            child_logical_operation_id=child.logical_operation_id,
            child_stage=child.stage,
            parent_potential_operation_sha256=expected_parent.sha256,
            parent_logical_operation_id=expected_parent.logical_operation_id,
            parent_stage=expected_parent.stage,
            parent_disposition_sha256=parent.sha256,
            proof_kind=proof_kind,
            matrix_sha256=child.matrix_sha256,
            slot_sha256=child.slot_sha256,
            task_seed_key_sha256=child.task_seed_key_sha256,
            attempt_id=child.attempt_id,
            semantic_snapshot_event_count=self._replay.event_count,
            semantic_snapshot_head_sha256=self._replay.head_sha256,
        )

    def skipped_by_parent(
        self,
        child_logical_operation_id: str,
        *,
        parent: SemanticDisposition,
    ) -> SemanticSkippedByParentReceipt:
        if not isinstance(
            parent, (SemanticJournalOperationReceipt, SemanticSkippedByParentReceipt)
        ) or self._issued.get(parent.sha256) is not parent:
            raise FactorialStageDispositionError(
                "skip parent was not issued by this semantic snapshot verifier"
            )
        child = self._operation(child_logical_operation_id)
        existing = self._issued_by_operation.get(child.logical_operation_id)
        if existing is not None:
            if not isinstance(existing, SemanticSkippedByParentReceipt):
                raise FactorialStageDispositionError(
                    "operation was already issued as an executed disposition"
                )
            expected = self._expected_skip(child=child, parent=parent)
            if existing != expected or existing.canonical_bytes != expected.canonical_bytes:
                raise FactorialStageDispositionError(
                    "existing skip disposition differs from immediate parent"
                )
            return existing
        receipt = self._expected_skip(child=child, parent=parent)
        self._issued[receipt.sha256] = receipt
        self._issued_by_operation[child.logical_operation_id] = receipt
        return receipt

    def seal(
        self, dispositions: Sequence[SemanticDisposition]
    ) -> ExactSemanticDispositionSeal:
        if isinstance(dispositions, (str, bytes)) or not isinstance(
            dispositions, Sequence
        ):
            raise FactorialStageDispositionError(
                "semantic dispositions must be an exact sequence"
            )
        submitted = tuple(dispositions)
        if len(submitted) != len(self._schedule.operations):
            raise FactorialStageDispositionError(
                "semantic dispositions do not cover the exact 4,338-stage set"
            )
        by_operation: dict[str, SemanticDisposition] = {}
        for receipt in submitted:
            if not isinstance(
                receipt,
                (SemanticJournalOperationReceipt, SemanticSkippedByParentReceipt),
            ):
                raise FactorialStageDispositionError(
                    "semantic disposition type differs"
                )
            operation_id = (
                receipt.logical_operation_id
                if isinstance(receipt, SemanticJournalOperationReceipt)
                else receipt.child_logical_operation_id
            )
            if self._issued.get(receipt.sha256) is not receipt:
                raise FactorialStageDispositionError(
                    "semantic disposition was not issued by this snapshot verifier"
                )
            if operation_id in by_operation:
                raise FactorialStageDispositionError(
                    "semantic dispositions repeat an operation"
                )
            by_operation[operation_id] = receipt
        expected_ids = {
            item.logical_operation_id for item in self._schedule.operations
        }
        if set(by_operation) != expected_ids:
            raise FactorialStageDispositionError(
                "semantic disposition operation set differs from exact schedule"
            )

        validated: dict[str, SemanticDisposition] = {}
        ordered: list[SemanticDisposition] = []
        completed = failed = skipped = 0
        for operation in self._schedule.operations:
            supplied = by_operation[operation.logical_operation_id]
            if isinstance(supplied, SemanticJournalOperationReceipt):
                immediate_parent = self._immediate_parent.get(
                    operation.logical_operation_id
                )
                if immediate_parent is not None:
                    parent_disposition = validated.get(
                        immediate_parent.logical_operation_id
                    )
                    if parent_disposition is None or isinstance(
                        parent_disposition, SemanticSkippedByParentReceipt
                    ) or (
                        isinstance(
                            parent_disposition, SemanticJournalOperationReceipt
                        )
                        and parent_disposition.journal_state == "failed"
                    ):
                        raise FactorialStageDispositionError(
                            "executed stage follows a failed or skipped parent"
                        )
                expected = self._expected_executed(operation)
                if supplied != expected or supplied.canonical_bytes != expected.canonical_bytes:
                    raise FactorialStageDispositionError(
                        "executed disposition differs from semantic journal replay"
                    )
                if expected.journal_state == "completed":
                    completed += 1
                else:
                    failed += 1
            else:
                immediate_parent = self._immediate_parent.get(
                    operation.logical_operation_id
                )
                if immediate_parent is None or (
                    immediate_parent.logical_operation_id not in validated
                ):
                    raise FactorialStageDispositionError(
                        "skip disposition lacks its verified immediate parent"
                    )
                expected = self._expected_skip(
                    child=operation,
                    parent=validated[immediate_parent.logical_operation_id],
                )
                if supplied != expected or supplied.canonical_bytes != expected.canonical_bytes:
                    raise FactorialStageDispositionError(
                        "skip disposition differs from immediate-parent replay"
                    )
                skipped += 1
            validated[operation.logical_operation_id] = expected
            ordered.append(expected)

        executed_ids = {
            receipt.logical_operation_id
            for receipt in ordered
            if isinstance(receipt, SemanticJournalOperationReceipt)
        }
        if set(self._replay.operations) != executed_ids:
            raise FactorialStageDispositionError(
                "semantic journal operation set differs from executed dispositions"
            )
        return ExactSemanticDispositionSeal._from_derived(
            schedule_sha256=self._schedule_sha256,
            matrix_sha256=self._schedule.matrix_sha256,
            factorial_plan_sha256=self._schedule.factorial_plan_sha256,
            task_authority_bundle_sha256=(
                self._schedule.task_authority_bundle_sha256
            ),
            semantic_snapshot_event_count=self._replay.event_count,
            semantic_snapshot_head_sha256=self._replay.head_sha256,
            potential_stage_count=len(self._schedule.operations),
            submitted_disposition_count=len(submitted),
            executed_count=completed + failed,
            terminal_completed_count=completed,
            terminal_failed_count=failed,
            skipped_by_parent_count=skipped,
            disposition_sha256s=tuple(item.sha256 for item in ordered),
        )

    def derive_exact_artifact(self) -> "VerifiedExactSemanticArtifact":
        """Automatically derive all dispositions from this one frozen snapshot."""

        ordered: list[SemanticDisposition] = []
        by_operation: dict[str, SemanticDisposition] = {}
        for operation in self._schedule.operations:
            record = self._replay.operations.get(operation.logical_operation_id)
            if record is not None:
                receipt = self.executed(operation.logical_operation_id)
            else:
                immediate_parent = self._immediate_parent.get(
                    operation.logical_operation_id
                )
                if immediate_parent is None:
                    raise FactorialStageDispositionError(
                        "root stage is absent from semantic journal snapshot"
                    )
                parent = by_operation.get(immediate_parent.logical_operation_id)
                if parent is None:
                    raise FactorialStageDispositionError(
                        "absent stage lacks its immediate parent disposition"
                    )
                receipt = self.skipped_by_parent(
                    operation.logical_operation_id,
                    parent=parent,
                )
            by_operation[operation.logical_operation_id] = receipt
            ordered.append(receipt)
        seal = self.seal(ordered)
        return VerifiedExactSemanticArtifact._from_derived(
            receipts=tuple(ordered),
            seal=seal,
        )


_TRUSTED_SOURCE_REPLAY = object()


@dataclass(frozen=True, init=False)
class VerifiedExactSemanticArtifact:
    """Canonical v1 semantic artifact verified only by full pinned replay."""

    receipts: tuple[SemanticDisposition, ...]
    seal: ExactSemanticDispositionSeal
    schema_version: int
    artifact_kind: str
    verification_contract: str

    def __init__(self, *_args: object, **_kwargs: object) -> None:
        raise FactorialStageDispositionError(
            "verified semantic artifact requires pinned replay derivation"
        )

    @classmethod
    def _from_derived(
        cls,
        *,
        receipts: tuple[SemanticDisposition, ...],
        seal: ExactSemanticDispositionSeal,
    ) -> "VerifiedExactSemanticArtifact":
        if (
            len(receipts) != 4338
            or type(seal) is not ExactSemanticDispositionSeal
            or tuple(receipt.sha256 for receipt in receipts)
            != seal.disposition_sha256s
        ):
            raise FactorialStageDispositionError(
                "verified semantic artifact exact set differs"
            )
        instance = object.__new__(cls)
        object.__setattr__(instance, "receipts", receipts)
        object.__setattr__(instance, "seal", seal)
        object.__setattr__(instance, "schema_version", 1)
        object.__setattr__(instance, "artifact_kind", _ARTIFACT_KIND)
        object.__setattr__(instance, "verification_contract", VERIFICATION_CONTRACT)
        return instance

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_kind": self.artifact_kind,
            "receipts": [receipt.to_dict() for receipt in self.receipts],
            "schema_version": self.schema_version,
            "seal": self.seal.to_dict(),
            "verification_contract": self.verification_contract,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


def derive_exact_semantic_artifact(
    *,
    matrix: ExactFactorialAttemptMatrix,
    plan: FactorialFormalZeroCallPlan,
    bundle: ExactTaskSeedAuthorityBundle,
    task_authority: FactorialTaskArtifactAuthority,
    ledger_path: Path,
    anchor_path: Path,
) -> VerifiedExactSemanticArtifact:
    """Derive one candidate v1 semantic artifact without caller-supplied rows."""

    verifier = FactorialSemanticDispositionVerifier.from_verified_sources(
        matrix=matrix,
        plan=plan,
        bundle=bundle,
        task_authority=task_authority,
        ledger_path=ledger_path,
        anchor_path=anchor_path,
    )
    return verifier.derive_exact_artifact()


def verify_serialized_exact_semantic_artifact(
    raw: bytes,
    *,
    matrix: ExactFactorialAttemptMatrix,
    plan: FactorialFormalZeroCallPlan,
    bundle: ExactTaskSeedAuthorityBundle,
    task_authority: FactorialTaskArtifactAuthority,
    ledger_path: Path,
    anchor_path: Path,
    expected_sha256: str | None = None,
) -> VerifiedExactSemanticArtifact:
    """Rederive persisted bytes from pinned source and current v1 journal/head.

    Parsing the supplied JSON is deliberately unnecessary: the only accepted
    bytes are the exact canonical bytes freshly rederived from trusted inputs.
    This gives extra/missing/duplicate keys no interpretation and avoids a
    caller-controlled 4,338-row construction surface.
    """

    if type(raw) is not bytes or not raw or len(raw) > _MAX_ARTIFACT_BYTES:
        raise FactorialStageDispositionError(
            "serialized semantic artifact size or type differs"
        )
    if expected_sha256 is not None:
        _sha(expected_sha256, "expected semantic artifact sha256")
        if hashlib.sha256(raw).hexdigest() != expected_sha256:
            raise FactorialStageDispositionError(
                "serialized semantic artifact hash differs"
            )
    expected = derive_exact_semantic_artifact(
        matrix=matrix,
        plan=plan,
        bundle=bundle,
        task_authority=task_authority,
        ledger_path=ledger_path,
        anchor_path=anchor_path,
    )
    if raw != expected.canonical_bytes:
        raise FactorialStageDispositionError(
            "serialized semantic artifact differs from pinned replay"
        )
    return expected


__all__ = [
    "BLOCKERS",
    "CLAIM_SCOPE",
    "EXECUTION_AUTHORITY",
    "ExactSemanticDispositionSeal",
    "FORMAL_READINESS",
    "FactorialSemanticDispositionVerifier",
    "FactorialStageDispositionError",
    "JOURNAL_STORAGE_STATUS",
    "PHYSICAL_OPERATION_BINDING_STATUS",
    "STANDALONE_VIEW_STATUS",
    "VERIFICATION_CONTRACT",
    "SemanticJournalOperationReceipt",
    "SemanticSkippedByParentReceipt",
    "VerifiedExactSemanticArtifact",
    "derive_exact_semantic_artifact",
    "verify_serialized_exact_semantic_artifact",
]
