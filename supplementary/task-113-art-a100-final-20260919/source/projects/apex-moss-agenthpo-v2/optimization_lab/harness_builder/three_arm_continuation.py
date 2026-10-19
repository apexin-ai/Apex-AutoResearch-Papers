"""Fail-closed source binding for a three-arm successor continuation.

The historical source segment is never edited or copied.  A continuation first
captures the exact immutable prefix, operation debit, online checkpoint/Bank,
and explicitly excluded consumed tail into two content-addressed objects.  A
schema-v6 staging plan may then entitle only the still-unseen suffix.

This module deliberately contains no provider, evaluator, process, or service
control.  Quiescing the old writer is an external prerequisite; double-reading
the source here makes a concurrent or later mutation fail closed.
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

from .events import ResourceCaps, ResourceVector, verify_operation_journal
from .experience import ExperienceRecord
from .formal import _resource_caps, _safe_id
from .learning import BuilderCheckpoint, ExperienceBankSnapshot
from .three_arm import (
    THREE_ARMS,
    THREE_ARM_VALIDITY_POLICY,
    ThreeArmCampaignContract,
    ThreeArmStreamItem,
    _stream_item,
)


_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_SAFE_OPERATION = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,511}\Z")
_RESOURCE_FIELDS = (
    "model_calls",
    "evaluator_transactions",
    "gpu_exclusive_seconds",
    "cpu_evaluator_seconds",
)
_ARTIFACT_FIELDS = {"relative_path", "sha256"}
_PREFIX_RECEIPT_FIELDS = _ARTIFACT_FIELDS | {"stream_index", "instance_id"}
_JOURNAL_FIELDS = _ARTIFACT_FIELDS | {"event_count", "head_sha256"}
_TAIL_FIELDS = {
    "operation_id",
    "cell_id",
    "operation_kind",
    "state",
    "start_event_sha256",
    "charged_usage",
    "operation_artifacts",
    "result_relative_path",
    "result_absent",
    "learning_import",
    "performance_import",
}
_SNAPSHOT_FIELDS = {
    "schema_version",
    "kind",
    "source_manifest_sha256",
    "source_staging_plan_sha256",
    "source_code_revision",
    "prefix_length",
    "last_prefix_stream_index",
    "next_stream_index",
    "prefix_instance_receipts",
    "operation_journal",
    "formal_ledger",
    "online_checkpoint",
    "online_bank",
    "rule_registry_sha256",
    "learned_through_instance",
    "record_source_instance_ids",
    "source_committed_usage",
    "excluded_instance_id",
    "excluded_consumed_tail",
}
_MANIFEST_FIELDS = {
    "schema_version",
    "kind",
    "source_staging_plan",
    "operation_journal",
    "operation_anchor",
    "formal_ledger",
    "formal_state",
    "prefix_instance_receipts",
    "online_checkpoint",
    "online_bank",
    "excluded_tail_artifacts",
}
_V6_STAGING_FIELDS = {
    "schema_version",
    "phase_id",
    "code_revision",
    "model_signature",
    "execution_ready",
    "blockers",
    "source_hashes",
    "budgets",
    "resource_entitlement_totals",
    "cell_entitlements",
    "rule_ids",
    "variant_ids",
    "stream_policy",
    "stream",
    "experience_initialization",
    "online_instances_per_suite",
    "sealed_instances_per_suite",
    "validity_policy",
    "continuation",
    "qualification_transfer",
    "no_next_phase",
    "no_paid_provider_fallback",
}
_CONTINUATION_FIELDS = {
    "source_manifest_sha256",
    "source_snapshot_sha256",
    "source_staging_plan_sha256",
    "prefix_length",
    "execution_window",
    "input_online_checkpoint_sha256",
    "input_online_bank_sha256",
    "source_committed_usage",
    "composite_hard_caps",
    "excluded_consumed_tail_operation_ids",
}
_V2_INSTANCE_RECEIPT_FIELDS = {
    "schema_version",
    "phase_id",
    "staging_plan_sha256",
    "stream_item",
    "arm_order",
    "task_binding_sha256",
    "first_encounter",
    "same_instance_rerun_policy",
    "learning_mode",
    "input_online_checkpoint_sha256",
    "input_online_bank_sha256",
    "arm_receipt_sha256s",
    "trajectory_sha256",
    "distillation_operation_id",
    "output_online_checkpoint_sha256",
    "output_online_bank_sha256",
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


def _require_sha(value: str, label: str) -> str:
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise ValueError(f"invalid {label} sha256")
    return value


def _relative(value: str, label: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"invalid {label} relative path")
    parsed = PurePosixPath(value)
    if parsed.is_absolute() or ".." in parsed.parts or "." in parsed.parts:
        raise ValueError(f"invalid {label} relative path")
    return parsed.as_posix()


def _exact_object(payload: Any, fields: set[str], label: str) -> dict[str, Any]:
    if not isinstance(payload, dict) or set(payload) != fields:
        raise ValueError(f"{label} fields differ")
    return payload


def _sum_resources(values: tuple[ResourceVector, ...]) -> ResourceVector:
    result = ResourceVector()
    for value in values:
        result = result + value
    return result


def _within(proposed: ResourceVector, caps: ResourceVector, *, label: str) -> None:
    for field in _RESOURCE_FIELDS:
        if getattr(proposed, field) > getattr(caps, field):
            raise ValueError(f"{label} {field} exceeds its hard cap")


@dataclass(frozen=True)
class ArtifactBinding:
    relative_path: str
    sha256: str

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "relative_path", _relative(self.relative_path, "artifact")
        )
        _require_sha(self.sha256, "artifact")

    @classmethod
    def from_dict(cls, payload: Any) -> "ArtifactBinding":
        raw = _exact_object(payload, _ARTIFACT_FIELDS, "artifact binding")
        return cls(relative_path=raw["relative_path"], sha256=raw["sha256"])

    def to_dict(self) -> dict[str, Any]:
        return {"relative_path": self.relative_path, "sha256": self.sha256}


@dataclass(frozen=True)
class PrefixReceiptBinding(ArtifactBinding):
    stream_index: int
    instance_id: str

    def __post_init__(self) -> None:
        super().__post_init__()
        if (
            isinstance(self.stream_index, bool)
            or not isinstance(self.stream_index, int)
            or self.stream_index < 0
        ):
            raise ValueError("prefix receipt stream index is invalid")
        _safe_id(self.instance_id, "prefix receipt instance id")

    @classmethod
    def from_dict(cls, payload: Any) -> "PrefixReceiptBinding":
        raw = _exact_object(payload, _PREFIX_RECEIPT_FIELDS, "prefix receipt binding")
        return cls(
            relative_path=raw["relative_path"],
            sha256=raw["sha256"],
            stream_index=raw["stream_index"],
            instance_id=raw["instance_id"],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "stream_index": self.stream_index,
            "instance_id": self.instance_id,
        }


@dataclass(frozen=True)
class OperationJournalBinding(ArtifactBinding):
    event_count: int
    head_sha256: str

    def __post_init__(self) -> None:
        super().__post_init__()
        if (
            isinstance(self.event_count, bool)
            or not isinstance(self.event_count, int)
            or self.event_count < 1
        ):
            raise ValueError("operation journal event count is invalid")
        _require_sha(self.head_sha256, "operation journal head")

    @classmethod
    def from_dict(cls, payload: Any) -> "OperationJournalBinding":
        raw = _exact_object(payload, _JOURNAL_FIELDS, "operation journal binding")
        return cls(
            relative_path=raw["relative_path"],
            sha256=raw["sha256"],
            event_count=raw["event_count"],
            head_sha256=raw["head_sha256"],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "event_count": self.event_count,
            "head_sha256": self.head_sha256,
        }


@dataclass(frozen=True)
class ExcludedTailExpectation:
    operation_id: str
    state: str
    start_event_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.operation_id, str) or not _SAFE_OPERATION.fullmatch(
            self.operation_id
        ):
            raise ValueError("excluded tail operation id is unsafe")
        if self.state not in {"completed", "failed", "started"}:
            raise ValueError("excluded tail operation state is invalid")
        _require_sha(self.start_event_sha256, "excluded tail start event")


@dataclass(frozen=True)
class ExcludedTailBinding:
    operation_id: str
    cell_id: str
    operation_kind: str
    state: str
    start_event_sha256: str
    charged_usage: ResourceVector
    operation_artifacts: tuple[ArtifactBinding, ...]
    result_relative_path: str
    result_absent: bool
    learning_import: bool = False
    performance_import: bool = False

    def __post_init__(self) -> None:
        ExcludedTailExpectation(
            operation_id=self.operation_id,
            state=self.state,
            start_event_sha256=self.start_event_sha256,
        )
        _safe_id(self.cell_id, "excluded tail cell id")
        _safe_id(self.operation_kind, "excluded tail operation kind")
        object.__setattr__(
            self,
            "result_relative_path",
            _relative(self.result_relative_path, "excluded tail result"),
        )
        if not isinstance(self.result_absent, bool):
            raise ValueError("excluded tail result absence must be boolean")
        if self.state == "started" and not self.result_absent:
            raise ValueError("started tail result must remain absent")
        if self.state != "started" and self.result_absent:
            raise ValueError("terminal tail result must be present")
        if self.learning_import is not False or self.performance_import is not False:
            raise ValueError("excluded tail cannot enter learning or performance")
        if len({item.relative_path for item in self.operation_artifacts}) != len(
            self.operation_artifacts
        ):
            raise ValueError("excluded tail artifact path is duplicated")

    @classmethod
    def from_dict(cls, payload: Any) -> "ExcludedTailBinding":
        raw = _exact_object(payload, _TAIL_FIELDS, "excluded tail binding")
        artifacts = raw["operation_artifacts"]
        if not isinstance(artifacts, list):
            raise ValueError("excluded tail artifacts must be a list")
        return cls(
            operation_id=raw["operation_id"],
            cell_id=raw["cell_id"],
            operation_kind=raw["operation_kind"],
            state=raw["state"],
            start_event_sha256=raw["start_event_sha256"],
            charged_usage=ResourceVector.from_dict(raw["charged_usage"]),
            operation_artifacts=tuple(
                ArtifactBinding.from_dict(item) for item in artifacts
            ),
            result_relative_path=raw["result_relative_path"],
            result_absent=raw["result_absent"],
            learning_import=raw["learning_import"],
            performance_import=raw["performance_import"],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "operation_id": self.operation_id,
            "cell_id": self.cell_id,
            "operation_kind": self.operation_kind,
            "state": self.state,
            "start_event_sha256": self.start_event_sha256,
            "charged_usage": self.charged_usage.to_dict(),
            "operation_artifacts": [item.to_dict() for item in self.operation_artifacts],
            "result_relative_path": self.result_relative_path,
            "result_absent": self.result_absent,
            "learning_import": False,
            "performance_import": False,
        }


@dataclass(frozen=True)
class ContinuationSourceSpec:
    """Expected facts audited before the old source is allowed to become a prefix."""

    source_staging_plan_sha256: str
    source_code_revision: str
    prefix_instance_ids: tuple[str, ...]
    prefix_receipt_sha256s: tuple[str, ...]
    online_checkpoint_sha256: str
    online_bank_sha256: str
    rule_registry_sha256: str
    operation_event_count: int
    operation_head_sha256: str
    operation_journal_sha256: str
    operation_anchor_sha256: str
    formal_ledger_sha256: str
    formal_state_sha256: str
    source_committed_usage: ResourceVector
    excluded_instance_id: str
    excluded_tail_operations: tuple[ExcludedTailExpectation, ...]

    def __post_init__(self) -> None:
        for value, label in (
            (self.source_staging_plan_sha256, "source staging plan"),
            (self.online_checkpoint_sha256, "online checkpoint"),
            (self.online_bank_sha256, "online Bank"),
            (self.rule_registry_sha256, "Rule Registry"),
            (self.operation_head_sha256, "operation head"),
            (self.operation_journal_sha256, "operation journal"),
            (self.operation_anchor_sha256, "operation anchor"),
            (self.formal_ledger_sha256, "formal ledger"),
            (self.formal_state_sha256, "formal state"),
        ):
            _require_sha(value, label)
        if not _COMMIT.fullmatch(self.source_code_revision):
            raise ValueError("source code revision must be a full commit")
        if len(self.prefix_instance_ids) != 6:
            raise ValueError("continuation source requires exactly six prefix instances")
        if len(set(self.prefix_instance_ids)) != 6:
            raise ValueError("continuation prefix instances must be unique")
        for instance_id in self.prefix_instance_ids:
            _safe_id(instance_id, "continuation prefix instance")
        if len(self.prefix_receipt_sha256s) != 6:
            raise ValueError("continuation source requires six prefix receipts")
        for digest in self.prefix_receipt_sha256s:
            _require_sha(digest, "prefix receipt")
        if (
            isinstance(self.operation_event_count, bool)
            or not isinstance(self.operation_event_count, int)
            or self.operation_event_count < 1
        ):
            raise ValueError("source operation event count is invalid")
        _safe_id(self.excluded_instance_id, "excluded instance id")
        if not self.excluded_tail_operations:
            raise ValueError("continuation source must bind its consumed excluded tail")
        operation_ids = tuple(item.operation_id for item in self.excluded_tail_operations)
        if len(set(operation_ids)) != len(operation_ids):
            raise ValueError("excluded tail operation id is duplicated")


@dataclass(frozen=True)
class ThreeArmContinuationSourceSnapshot:
    source_manifest_sha256: str
    source_staging_plan_sha256: str
    source_code_revision: str
    prefix_instance_receipts: tuple[PrefixReceiptBinding, ...]
    operation_journal: OperationJournalBinding
    formal_ledger: ArtifactBinding
    online_checkpoint: ArtifactBinding
    online_bank: ArtifactBinding
    rule_registry_sha256: str
    learned_through_instance: str
    record_source_instance_ids: tuple[str, ...]
    source_committed_usage: ResourceVector
    excluded_instance_id: str
    excluded_consumed_tail: tuple[ExcludedTailBinding, ...]

    def __post_init__(self) -> None:
        for value, label in (
            (self.source_manifest_sha256, "source manifest"),
            (self.source_staging_plan_sha256, "source staging plan"),
            (self.rule_registry_sha256, "Rule Registry"),
        ):
            _require_sha(value, label)
        if not _COMMIT.fullmatch(self.source_code_revision):
            raise ValueError("source snapshot code revision must be a full commit")
        if len(self.prefix_instance_receipts) != 6:
            raise ValueError("source snapshot requires exactly six prefix receipts")
        if tuple(item.stream_index for item in self.prefix_instance_receipts) != tuple(
            range(6)
        ):
            raise ValueError("source snapshot prefix receipt order differs")
        prefix_ids = tuple(item.instance_id for item in self.prefix_instance_receipts)
        if self.learned_through_instance != prefix_ids[-1]:
            raise ValueError("source checkpoint learned-through binding differs")
        if self.record_source_instance_ids != prefix_ids:
            raise ValueError("source online Bank record sources differ from prefix")
        _safe_id(self.excluded_instance_id, "excluded instance id")
        if not self.excluded_consumed_tail:
            raise ValueError("source snapshot excluded tail cannot be empty")
        if any(
            not item.cell_id.startswith(f"formal:{self.excluded_instance_id}:")
            for item in self.excluded_consumed_tail
        ):
            raise ValueError("source excluded tail instance binding differs")

    @property
    def prefix_length(self) -> int:
        return len(self.prefix_instance_receipts)

    @property
    def last_prefix_stream_index(self) -> int:
        return self.prefix_length - 1

    @property
    def next_stream_index(self) -> int:
        return self.prefix_length

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "kind": "three_arm_successor_source_snapshot",
            "source_manifest_sha256": self.source_manifest_sha256,
            "source_staging_plan_sha256": self.source_staging_plan_sha256,
            "source_code_revision": self.source_code_revision,
            "prefix_length": self.prefix_length,
            "last_prefix_stream_index": self.last_prefix_stream_index,
            "next_stream_index": self.next_stream_index,
            "prefix_instance_receipts": [
                item.to_dict() for item in self.prefix_instance_receipts
            ],
            "operation_journal": self.operation_journal.to_dict(),
            "formal_ledger": self.formal_ledger.to_dict(),
            "online_checkpoint": self.online_checkpoint.to_dict(),
            "online_bank": self.online_bank.to_dict(),
            "rule_registry_sha256": self.rule_registry_sha256,
            "learned_through_instance": self.learned_through_instance,
            "record_source_instance_ids": list(self.record_source_instance_ids),
            "source_committed_usage": self.source_committed_usage.to_dict(),
            "excluded_instance_id": self.excluded_instance_id,
            "excluded_consumed_tail": [
                item.to_dict() for item in self.excluded_consumed_tail
            ],
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return _sha256(self.canonical_bytes)

    @classmethod
    def from_bytes(cls, encoded: bytes) -> "ThreeArmContinuationSourceSnapshot":
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("continuation source snapshot is invalid JSON") from exc
        raw = _exact_object(payload, _SNAPSHOT_FIELDS, "continuation source snapshot")
        if raw["schema_version"] != 1 or raw["kind"] != (
            "three_arm_successor_source_snapshot"
        ):
            raise ValueError("continuation source snapshot schema differs")
        receipts = raw["prefix_instance_receipts"]
        tails = raw["excluded_consumed_tail"]
        sources = raw["record_source_instance_ids"]
        if not isinstance(receipts, list) or not isinstance(tails, list):
            raise ValueError("continuation source snapshot arrays are invalid")
        if not isinstance(sources, list) or not all(isinstance(x, str) for x in sources):
            raise ValueError("continuation source record sources are invalid")
        result = cls(
            source_manifest_sha256=raw["source_manifest_sha256"],
            source_staging_plan_sha256=raw["source_staging_plan_sha256"],
            source_code_revision=raw["source_code_revision"],
            prefix_instance_receipts=tuple(
                PrefixReceiptBinding.from_dict(item) for item in receipts
            ),
            operation_journal=OperationJournalBinding.from_dict(
                raw["operation_journal"]
            ),
            formal_ledger=ArtifactBinding.from_dict(raw["formal_ledger"]),
            online_checkpoint=ArtifactBinding.from_dict(raw["online_checkpoint"]),
            online_bank=ArtifactBinding.from_dict(raw["online_bank"]),
            rule_registry_sha256=raw["rule_registry_sha256"],
            learned_through_instance=raw["learned_through_instance"],
            record_source_instance_ids=tuple(sources),
            source_committed_usage=ResourceVector.from_dict(
                raw["source_committed_usage"]
            ),
            excluded_instance_id=raw["excluded_instance_id"],
            excluded_consumed_tail=tuple(
                ExcludedTailBinding.from_dict(item) for item in tails
            ),
        )
        if (
            raw["prefix_length"] != result.prefix_length
            or raw["last_prefix_stream_index"] != result.last_prefix_stream_index
            or raw["next_stream_index"] != result.next_stream_index
        ):
            raise ValueError("continuation source prefix cursor differs")
        if result.canonical_bytes != encoded:
            raise ValueError("continuation source snapshot is not canonical")
        return result


@dataclass(frozen=True)
class ThreeArmContinuationPrepareOutcome:
    manifest_sha256: str
    manifest_path: Path
    snapshot: ThreeArmContinuationSourceSnapshot
    snapshot_path: Path


@dataclass(frozen=True)
class ThreeArmContinuationSourceGuard:
    """No-argument guard suitable for ``ResourceGovernor.pre_reserve_guard``.

    It intentionally replays and double-reads the frozen source on every call;
    callers must prefer a hard failure over accepting a post-start source drift.
    """

    source_root: Path
    manifest_path: Path
    snapshot_path: Path
    expected_snapshot_sha256: str

    def __post_init__(self) -> None:
        _require_sha(self.expected_snapshot_sha256, "expected source snapshot")
        object.__setattr__(self, "source_root", Path(self.source_root).resolve())
        object.__setattr__(self, "manifest_path", Path(self.manifest_path).resolve())
        object.__setattr__(self, "snapshot_path", Path(self.snapshot_path).resolve())

    def __call__(self) -> None:
        snapshot = verify_three_arm_continuation_source(
            source_root=self.source_root,
            manifest_path=self.manifest_path,
            snapshot_path=self.snapshot_path,
        )
        if snapshot.sha256 != self.expected_snapshot_sha256:
            raise ValueError("continuation source guard snapshot binding differs")


def _read_regular(root: Path, relative: str, *, max_bytes: int = 128 << 20) -> bytes:
    relative = _relative(relative, "source artifact")
    root = root.resolve()
    path = root.joinpath(*PurePosixPath(relative).parts)
    try:
        resolved = path.resolve(strict=True)
    except OSError as exc:
        raise ValueError(f"source artifact is unavailable: {relative}") from exc
    if not resolved.is_relative_to(root):
        raise ValueError("source artifact escapes the source root")
    current = path
    while current != root:
        if current.is_symlink():
            raise ValueError(f"source artifact uses a symlink: {relative}")
        current = current.parent
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            metadata = os.fstat(stream.fileno())
            if not stat.S_ISREG(metadata.st_mode):
                raise ValueError(f"source artifact is not regular: {relative}")
            raw = stream.read(max_bytes + 1)
    except ValueError:
        raise
    except OSError as exc:
        raise ValueError(f"source artifact is unavailable: {relative}") from exc
    if len(raw) > max_bytes:
        raise ValueError(f"source artifact is too large: {relative}")
    return raw


def _artifact(root: Path, relative: str, *, expected_sha: str | None = None) -> ArtifactBinding:
    raw = _read_regular(root, relative)
    digest = _sha256(raw)
    if expected_sha is not None and digest != expected_sha:
        raise ValueError(f"source artifact content hash differs: {relative}")
    return ArtifactBinding(relative_path=relative, sha256=digest)


def _parse_checkpoint(raw: bytes) -> BuilderCheckpoint:
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("source online checkpoint is invalid") from exc
    if not isinstance(payload, dict) or set(payload) != {
        "schema_version",
        "parent_checkpoint_sha256",
        "experience_bank_sha256",
        "rule_registry_sha256",
        "learned_through_instance",
        "stream_index",
    } or payload["schema_version"] != 1:
        raise ValueError("source online checkpoint schema differs")
    checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256=payload["parent_checkpoint_sha256"],
        experience_bank_sha256=payload["experience_bank_sha256"],
        rule_registry_sha256=payload["rule_registry_sha256"],
        learned_through_instance=payload["learned_through_instance"],
        stream_index=payload["stream_index"],
    )
    if checkpoint.canonical_bytes != raw:
        raise ValueError("source online checkpoint is not canonical")
    return checkpoint


def _parse_bank(raw: bytes) -> ExperienceBankSnapshot:
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("source online Bank is invalid") from exc
    if not isinstance(payload, dict) or set(payload) != {
        "schema_version",
        "bank_id",
        "parent_sha256",
        "records",
    } or payload["schema_version"] != 1 or not isinstance(payload["records"], list):
        raise ValueError("source online Bank schema differs")
    bank = ExperienceBankSnapshot.create(
        bank_id=payload["bank_id"],
        parent_sha256=payload["parent_sha256"],
        records=tuple(ExperienceRecord.from_dict(item) for item in payload["records"]),
    )
    if bank.canonical_bytes != raw:
        raise ValueError("source online Bank is not canonical")
    return bank


def _validate_prefix_receipt(
    payload: Any,
    *,
    item: ThreeArmStreamItem,
    source_contract: ThreeArmCampaignContract,
    staging_sha256: str,
) -> None:
    if not isinstance(payload, dict):
        raise ValueError("source prefix receipt must be an object")
    if payload.get("schema_version") == 1:
        if set(payload) != {
            "schema_version",
            "sealed",
            "stream_index",
            "instance_id",
            "staging_plan_sha256",
            "output_online_checkpoint_sha256",
            "output_online_bank_sha256",
        }:
            raise ValueError("source legacy prefix receipt fields differ")
        if (
            payload["sealed"] is not True
            or payload["stream_index"] != item.stream_index
            or payload["instance_id"] != item.instance_id
            or payload["staging_plan_sha256"] != staging_sha256
        ):
            raise ValueError("source prefix receipt semantic binding differs")
        return
    if payload.get("schema_version") != 2 or set(payload) != (
        _V2_INSTANCE_RECEIPT_FIELDS
    ):
        raise ValueError("source prefix receipt schema differs")
    if payload["stream_item"] != item.to_dict():
        raise ValueError("source prefix receipt nested stream item differs")
    if (
        payload["phase_id"] != source_contract.phase_id
        or payload["staging_plan_sha256"] != staging_sha256
        or payload["arm_order"] != list(item.arm_order)
        or payload["learning_mode"] != item.learning_mode
        or payload["first_encounter"] is not True
        or payload["same_instance_rerun_policy"]
        != "replay_only_no_formal_update"
        or payload["sealed"] is not True
        or payload["no_next_phase"] is not True
    ):
        raise ValueError("source prefix receipt semantic binding differs")
    for field in (
        "task_binding_sha256",
        "trajectory_sha256",
        "input_online_checkpoint_sha256",
        "input_online_bank_sha256",
        "output_online_checkpoint_sha256",
        "output_online_bank_sha256",
    ):
        _require_sha(payload[field], f"source prefix receipt {field}")
    arms = payload["arm_receipt_sha256s"]
    if not isinstance(arms, dict) or set(arms) != set(THREE_ARMS):
        raise ValueError("source prefix receipt arm bindings differ")
    for arm, digest in arms.items():
        _require_sha(digest, f"source prefix receipt {arm} arm")
    if item.learning_mode == "online":
        expected_distill = (
            f"distill:{item.stream_index:03d}:{item.instance_id}:distillation_call"
        )
        if payload["distillation_operation_id"] != expected_distill:
            raise ValueError("source prefix receipt distillation binding differs")
    elif payload["distillation_operation_id"] is not None:
        raise ValueError("source sealed receipt cannot bind distillation")


def _tail_artifacts(root: Path, operation_id: str) -> tuple[ArtifactBinding, ...]:
    relative_root = PurePosixPath("model-gateway/operations") / (
        "op-" + hashlib.sha256(operation_id.encode("utf-8")).hexdigest()
    )
    absolute = root.joinpath(*relative_root.parts)
    if not absolute.is_dir() or absolute.is_symlink():
        raise ValueError("excluded tail operation artifact directory is unavailable")
    result: list[ArtifactBinding] = []
    for path in sorted(absolute.rglob("*")):
        if path.is_symlink() or not path.is_file():
            if path.is_dir() and not path.is_symlink():
                continue
            raise ValueError("excluded tail operation artifacts contain an unsafe entry")
        relative = path.relative_to(root).as_posix()
        result.append(_artifact(root, relative))
    if not result:
        raise ValueError("excluded tail operation has no bound artifacts")
    return tuple(result)


def _manifest_payload(
    *,
    staging: ArtifactBinding,
    operation_journal: OperationJournalBinding,
    operation_anchor: ArtifactBinding,
    formal_ledger: ArtifactBinding,
    formal_state: ArtifactBinding,
    receipts: tuple[PrefixReceiptBinding, ...],
    checkpoint: ArtifactBinding,
    bank: ArtifactBinding,
    tails: tuple[ExcludedTailBinding, ...],
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "kind": "three_arm_successor_source_manifest",
        "source_staging_plan": staging.to_dict(),
        "operation_journal": operation_journal.to_dict(),
        "operation_anchor": operation_anchor.to_dict(),
        "formal_ledger": formal_ledger.to_dict(),
        "formal_state": formal_state.to_dict(),
        "prefix_instance_receipts": [item.to_dict() for item in receipts],
        "online_checkpoint": checkpoint.to_dict(),
        "online_bank": bank.to_dict(),
        "excluded_tail_artifacts": [
            {
                "operation_id": tail.operation_id,
                "artifacts": [item.to_dict() for item in tail.operation_artifacts],
            }
            for tail in tails
        ],
    }


@dataclass(frozen=True)
class _CapturedSource:
    manifest: dict[str, Any]
    source_code_revision: str
    checkpoint: BuilderCheckpoint
    bank: ExperienceBankSnapshot
    receipts: tuple[PrefixReceiptBinding, ...]
    operation_journal: OperationJournalBinding
    formal_ledger: ArtifactBinding
    checkpoint_binding: ArtifactBinding
    bank_binding: ArtifactBinding
    tails: tuple[ExcludedTailBinding, ...]


def _capture_source(source_root: Path, spec: ContinuationSourceSpec) -> _CapturedSource:
    source_root = Path(source_root).resolve()
    staging_raw = _read_regular(source_root, "staging_plan.json")
    staging_binding = ArtifactBinding("staging_plan.json", _sha256(staging_raw))
    if staging_binding.sha256 != spec.source_staging_plan_sha256:
        raise ValueError("source staging plan content hash differs")
    source_contract = ThreeArmCampaignContract.from_staging_bytes(staging_raw)
    if source_contract.stream[:6] and tuple(
        item.instance_id for item in source_contract.stream[:6]
    ) != spec.prefix_instance_ids:
        raise ValueError("source staging prefix differs")
    staging_payload = json.loads(staging_raw)
    if staging_payload["code_revision"] != spec.source_code_revision:
        raise ValueError("source code revision differs")

    instance_root = source_root / "formal/instances"
    receipt_paths = tuple(sorted(instance_root.glob("*/instance_receipt.json")))
    if len(receipt_paths) != 6:
        raise ValueError("source must contain exactly six sealed instance receipts")
    receipts: list[PrefixReceiptBinding] = []
    for index, (instance_id, expected_sha) in enumerate(
        zip(spec.prefix_instance_ids, spec.prefix_receipt_sha256s, strict=True)
    ):
        matches = tuple(instance_root.glob(f"{index:03d}-*/instance_receipt.json"))
        if len(matches) != 1:
            raise ValueError("source prefix receipt path is ambiguous")
        path = matches[0]
        relative = path.relative_to(source_root).as_posix()
        raw = _read_regular(source_root, relative)
        digest = _sha256(raw)
        if digest != expected_sha:
            raise ValueError("source prefix receipt content hash differs")
        try:
            payload = json.loads(raw)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("source prefix receipt is invalid") from exc
        _validate_prefix_receipt(
            payload,
            item=source_contract.stream[index],
            source_contract=source_contract,
            staging_sha256=spec.source_staging_plan_sha256,
        )
        receipts.append(
            PrefixReceiptBinding(
                relative_path=relative,
                sha256=digest,
                stream_index=index,
                instance_id=instance_id,
            )
        )

    checkpoint_relative = (
        f"formal/builder_checkpoints/{spec.online_checkpoint_sha256}.json"
    )
    checkpoint_raw = _read_regular(source_root, checkpoint_relative)
    if _sha256(checkpoint_raw) != spec.online_checkpoint_sha256:
        raise ValueError("source online checkpoint content hash differs")
    checkpoint = _parse_checkpoint(checkpoint_raw)
    checkpoint_binding = ArtifactBinding(checkpoint_relative, checkpoint.sha256)
    if (
        checkpoint.stream_index != 5
        or checkpoint.learned_through_instance != spec.prefix_instance_ids[-1]
        or checkpoint.experience_bank_sha256 != spec.online_bank_sha256
        or checkpoint.rule_registry_sha256 != spec.rule_registry_sha256
    ):
        raise ValueError("source online checkpoint semantic binding differs")

    bank_relative = f"formal/experience_banks/{spec.online_bank_sha256}.json"
    bank_raw = _read_regular(source_root, bank_relative)
    if _sha256(bank_raw) != spec.online_bank_sha256:
        raise ValueError("source online Bank content hash differs")
    bank = _parse_bank(bank_raw)
    bank_binding = ArtifactBinding(bank_relative, bank.sha256)
    record_sources = tuple(record.source_instance_id for record in bank.records)
    if record_sources != spec.prefix_instance_ids:
        raise ValueError("source online Bank must contain exactly the six prefix sources")

    final_receipt = json.loads(
        _read_regular(source_root, receipts[-1].relative_path)
    )
    if (
        final_receipt.get("output_online_checkpoint_sha256") != checkpoint.sha256
        or final_receipt.get("output_online_bank_sha256") != bank.sha256
    ):
        raise ValueError("source final receipt online state differs")

    ledger_relative = "control/operations/operation_ledger.jsonl"
    anchor_relative = "control/trusted-operation-head.json"
    ledger_raw = _read_regular(source_root, ledger_relative)
    anchor_raw = _read_regular(source_root, anchor_relative)
    if _sha256(ledger_raw) != spec.operation_journal_sha256:
        raise ValueError("source operation journal content hash differs")
    if _sha256(anchor_raw) != spec.operation_anchor_sha256:
        raise ValueError("source operation anchor content hash differs")
    replay = verify_operation_journal(
        source_root / ledger_relative,
        anchor_path=source_root / anchor_relative,
    )
    if (
        replay.event_count != spec.operation_event_count
        or replay.head_sha256 != spec.operation_head_sha256
    ):
        raise ValueError("source operation trusted head differs")
    usage = _sum_resources(
        tuple(operation.committed_usage for operation in replay.operations.values())
    )
    if usage != spec.source_committed_usage:
        raise ValueError("source committed usage differs")

    prefix_cells = {
        f"formal:{instance_id}:{arm}"
        for instance_id in spec.prefix_instance_ids
        for arm in THREE_ARMS
    } | {
        f"distill:{index:03d}:{instance_id}"
        for index, instance_id in enumerate(spec.prefix_instance_ids)
    }
    expected_tail_ids = {
        item.operation_id for item in spec.excluded_tail_operations
    }
    actual_tail_ids = {
        operation.operation_id
        for operation in replay.operations.values()
        if operation.cell_id.startswith(f"formal:{spec.excluded_instance_id}:")
    }
    if actual_tail_ids != expected_tail_ids:
        raise ValueError("source excluded tail operation set differs")
    for operation in replay.operations.values():
        if operation.operation_id not in expected_tail_ids and operation.cell_id not in prefix_cells:
            raise ValueError("source contains an operation outside prefix and excluded tail")

    tails: list[ExcludedTailBinding] = []
    for expectation in spec.excluded_tail_operations:
        operation = replay.operations[expectation.operation_id]
        start_events = tuple(
            event for event in operation.events if event.event_type == "operation_started"
        )
        if (
            operation.state != expectation.state
            or len(start_events) != 1
            or start_events[0].event_sha256 != expectation.start_event_sha256
        ):
            raise ValueError("source excluded tail operation binding differs")
        artifacts = _tail_artifacts(source_root, operation.operation_id)
        result_relative = (
            "model-gateway/operations/op-"
            + hashlib.sha256(operation.operation_id.encode("utf-8")).hexdigest()
            + "/result.json"
        )
        result_path = source_root.joinpath(*PurePosixPath(result_relative).parts)
        result_absent = not result_path.exists()
        if operation.state == "started" and not result_absent:
            raise ValueError("started tail result must remain absent")
        if operation.state != "started" and result_absent:
            raise ValueError("terminal tail result must remain present")
        if not result_absent:
            terminal_sha = operation.events[-1].payload.get("artifact_sha256")
            if _sha256(_read_regular(source_root, result_relative)) != terminal_sha:
                raise ValueError("excluded tail result hash differs from its terminal event")
        tails.append(
            ExcludedTailBinding(
                operation_id=operation.operation_id,
                cell_id=operation.cell_id,
                operation_kind=operation.operation_kind,
                state=operation.state,
                start_event_sha256=start_events[0].event_sha256,
                charged_usage=operation.committed_usage,
                operation_artifacts=artifacts,
                result_relative_path=result_relative,
                result_absent=result_absent,
            )
        )

    formal_relative = "formal/ledger.jsonl"
    formal_state_relative = "formal/state.json"
    formal_raw = _read_regular(source_root, formal_relative)
    formal_state_raw = _read_regular(source_root, formal_state_relative)
    if _sha256(formal_raw) != spec.formal_ledger_sha256:
        raise ValueError("source formal ledger content hash differs")
    if _sha256(formal_state_raw) != spec.formal_state_sha256:
        raise ValueError("source formal state content hash differs")
    try:
        formal_events = tuple(
            json.loads(line) for line in formal_raw.decode("utf-8").splitlines()
        )
        formal_state = json.loads(formal_state_raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("source formal ledger or state is invalid") from exc
    if not formal_events or not all(isinstance(event, dict) for event in formal_events):
        raise ValueError("source formal ledger is empty or malformed")
    if any(
        isinstance(event.get("payload"), dict)
        and isinstance(event["payload"].get("stream_index"), int)
        and event["payload"]["stream_index"] >= 6
        for event in formal_events
    ):
        raise ValueError("source formal ledger extends beyond the accepted prefix")
    last_event = formal_events[-1]
    if (
        formal_state.get("event_count") != len(formal_events)
        or formal_state.get("last_event") != last_event
        or last_event.get("event_type") != "hb_gen1_formal_instance_sealed"
        or last_event.get("payload", {}).get("stream_index") != 5
        or last_event.get("payload", {}).get("instance_receipt_sha256")
        != receipts[-1].sha256
        or last_event.get("payload", {}).get("output_online_checkpoint_sha256")
        != checkpoint.sha256
        or last_event.get("payload", {}).get("output_online_bank_sha256") != bank.sha256
    ):
        raise ValueError("source formal terminal prefix binding differs")

    journal_binding = OperationJournalBinding(
        relative_path=ledger_relative,
        sha256=_sha256(ledger_raw),
        event_count=replay.event_count,
        head_sha256=replay.head_sha256,
    )
    formal_binding = ArtifactBinding(formal_relative, _sha256(formal_raw))
    manifest = _manifest_payload(
        staging=staging_binding,
        operation_journal=journal_binding,
        operation_anchor=ArtifactBinding(anchor_relative, _sha256(anchor_raw)),
        formal_ledger=formal_binding,
        formal_state=ArtifactBinding(formal_state_relative, _sha256(formal_state_raw)),
        receipts=tuple(receipts),
        checkpoint=checkpoint_binding,
        bank=bank_binding,
        tails=tuple(tails),
    )
    return _CapturedSource(
        manifest=manifest,
        source_code_revision=spec.source_code_revision,
        checkpoint=checkpoint,
        bank=bank,
        receipts=tuple(receipts),
        operation_journal=journal_binding,
        formal_ledger=formal_binding,
        checkpoint_binding=checkpoint_binding,
        bank_binding=bank_binding,
        tails=tuple(tails),
    )


def _snapshot_from_capture(
    capture: _CapturedSource,
    *,
    manifest_sha256: str,
    source_committed_usage: ResourceVector,
    excluded_instance_id: str,
) -> ThreeArmContinuationSourceSnapshot:
    return ThreeArmContinuationSourceSnapshot(
        source_manifest_sha256=manifest_sha256,
        source_staging_plan_sha256=capture.manifest["source_staging_plan"]["sha256"],
        source_code_revision=capture.source_code_revision,
        prefix_instance_receipts=capture.receipts,
        operation_journal=capture.operation_journal,
        formal_ledger=capture.formal_ledger,
        online_checkpoint=capture.checkpoint_binding,
        online_bank=capture.bank_binding,
        rule_registry_sha256=capture.checkpoint.rule_registry_sha256,
        learned_through_instance=capture.checkpoint.learned_through_instance,
        record_source_instance_ids=tuple(
            record.source_instance_id for record in capture.bank.records
        ),
        source_committed_usage=source_committed_usage,
        excluded_instance_id=excluded_instance_id,
        excluded_consumed_tail=capture.tails,
    )


def _write_content_addressed(directory: Path, raw: bytes) -> Path:
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError("continuation output directory is unsafe")
    path = directory / f"{_sha256(raw)}.json"
    if path.exists() or path.is_symlink():
        if path.is_symlink() or _read_regular(directory, path.name) != raw:
            raise ValueError("continuation content-addressed output is already rebound")
        return path
    descriptor, name = tempfile.mkstemp(
        prefix=".three-arm-continuation-", suffix=".tmp", dir=directory
    )
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, 0o444)
        os.replace(temporary, path)
        directory_fd = os.open(
            directory, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
        )
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return path


def prepare_three_arm_continuation_source(
    *,
    source_root: Path,
    output_root: Path,
    spec: ContinuationSourceSpec,
) -> ThreeArmContinuationPrepareOutcome:
    """Capture a stable historical prefix without modifying or copying its files."""

    source_root = Path(source_root).resolve()
    output_root = Path(output_root).resolve()
    if (
        source_root == output_root
        or output_root.is_relative_to(source_root)
        or source_root.is_relative_to(output_root)
    ):
        raise ValueError("continuation output must not overlap its frozen source")
    first = _capture_source(source_root, spec)
    second = _capture_source(source_root, spec)
    if _canonical_bytes(first.manifest) != _canonical_bytes(second.manifest):
        raise ValueError("continuation source changed between double reads")
    manifest_raw = _canonical_bytes(first.manifest)
    manifest_sha = _sha256(manifest_raw)
    snapshot = _snapshot_from_capture(
        first,
        manifest_sha256=manifest_sha,
        source_committed_usage=spec.source_committed_usage,
        excluded_instance_id=spec.excluded_instance_id,
    )
    manifest_path = _write_content_addressed(
        output_root / "source_manifests", manifest_raw
    )
    snapshot_path = _write_content_addressed(
        output_root / "source_snapshots", snapshot.canonical_bytes
    )
    return ThreeArmContinuationPrepareOutcome(
        manifest_sha256=manifest_sha,
        manifest_path=manifest_path,
        snapshot=snapshot,
        snapshot_path=snapshot_path,
    )


def _read_cas(path: Path, label: str) -> bytes:
    path = Path(path)
    if not _SHA256.fullmatch(path.stem) or path.suffix != ".json":
        raise ValueError(f"{label} filename is not content addressed")
    raw = _read_regular(path.parent, path.name)
    if _sha256(raw) != path.stem:
        raise ValueError(f"{label} filename hash differs")
    return raw


def _spec_from_snapshot_and_manifest(
    snapshot: ThreeArmContinuationSourceSnapshot, manifest: dict[str, Any]
) -> ContinuationSourceSpec:
    anchor = ArtifactBinding.from_dict(manifest["operation_anchor"])
    formal_state = ArtifactBinding.from_dict(manifest["formal_state"])
    tails = tuple(
        ExcludedTailExpectation(
            operation_id=item.operation_id,
            state=item.state,
            start_event_sha256=item.start_event_sha256,
        )
        for item in snapshot.excluded_consumed_tail
    )
    return ContinuationSourceSpec(
        source_staging_plan_sha256=snapshot.source_staging_plan_sha256,
        source_code_revision=snapshot.source_code_revision,
        prefix_instance_ids=tuple(
            item.instance_id for item in snapshot.prefix_instance_receipts
        ),
        prefix_receipt_sha256s=tuple(
            item.sha256 for item in snapshot.prefix_instance_receipts
        ),
        online_checkpoint_sha256=snapshot.online_checkpoint.sha256,
        online_bank_sha256=snapshot.online_bank.sha256,
        rule_registry_sha256=snapshot.rule_registry_sha256,
        operation_event_count=snapshot.operation_journal.event_count,
        operation_head_sha256=snapshot.operation_journal.head_sha256,
        operation_journal_sha256=snapshot.operation_journal.sha256,
        operation_anchor_sha256=anchor.sha256,
        formal_ledger_sha256=snapshot.formal_ledger.sha256,
        formal_state_sha256=formal_state.sha256,
        source_committed_usage=snapshot.source_committed_usage,
        excluded_instance_id=snapshot.excluded_instance_id,
        excluded_tail_operations=tails,
    )


def verify_three_arm_continuation_source(
    *,
    source_root: Path,
    manifest_path: Path,
    snapshot_path: Path,
) -> ThreeArmContinuationSourceSnapshot:
    """Re-verify both CAS objects and double-read every bound source artifact."""

    manifest_raw = _read_cas(manifest_path, "continuation source manifest")
    snapshot_raw = _read_cas(snapshot_path, "continuation source snapshot")
    try:
        manifest = json.loads(manifest_raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("continuation source manifest is invalid JSON") from exc
    raw_manifest = _exact_object(
        manifest, _MANIFEST_FIELDS, "continuation source manifest"
    )
    if (
        raw_manifest["schema_version"] != 1
        or raw_manifest["kind"] != "three_arm_successor_source_manifest"
        or _canonical_bytes(raw_manifest) != manifest_raw
    ):
        raise ValueError("continuation source manifest schema or encoding differs")
    snapshot = ThreeArmContinuationSourceSnapshot.from_bytes(snapshot_raw)
    if snapshot.source_manifest_sha256 != _sha256(manifest_raw):
        raise ValueError("continuation source snapshot does not bind its manifest")
    spec = _spec_from_snapshot_and_manifest(snapshot, raw_manifest)
    first = _capture_source(Path(source_root).resolve(), spec)
    second = _capture_source(Path(source_root).resolve(), spec)
    if _canonical_bytes(first.manifest) != _canonical_bytes(second.manifest):
        raise ValueError("continuation source changed between double reads")
    if _canonical_bytes(first.manifest) != manifest_raw:
        raise ValueError("continuation source differs from its frozen manifest")
    rebuilt = _snapshot_from_capture(
        first,
        manifest_sha256=snapshot.source_manifest_sha256,
        source_committed_usage=snapshot.source_committed_usage,
        excluded_instance_id=snapshot.excluded_instance_id,
    )
    if rebuilt != snapshot:
        raise ValueError("continuation source differs from its frozen snapshot")
    return snapshot


@dataclass(frozen=True)
class ThreeArmContinuationContract:
    staging_plan_sha256: str
    phase_id: str
    model: str
    execution_ready: bool
    blockers: tuple[str, ...]
    stream: tuple[ThreeArmStreamItem, ...]
    execution_start_index: int
    execution_stop_index: int
    suffix_global_caps: ResourceCaps
    suffix_entitlement_totals: ResourceCaps
    cell_entitlements: dict[str, ResourceCaps]
    source_snapshot_sha256: str
    source_manifest_sha256: str
    source_staging_plan_sha256: str
    input_online_checkpoint_sha256: str
    input_online_bank_sha256: str
    source_committed_usage: ResourceVector
    composite_hard_caps: ResourceCaps
    excluded_consumed_tail_operation_ids: tuple[str, ...]
    qualification_transfer_sha256: str
    arms: tuple[str, ...] = THREE_ARMS
    no_next_phase: bool = True

    @property
    def active_stream(self) -> tuple[ThreeArmStreamItem, ...]:
        return self.stream[self.execution_start_index : self.execution_stop_index]

    @property
    def global_caps(self) -> ResourceCaps:
        """Compatibility alias: the new ledger may consume only the suffix cap."""

        return self.suffix_global_caps

    @classmethod
    def from_staging_bytes(
        cls,
        encoded: bytes,
        *,
        source_snapshot: ThreeArmContinuationSourceSnapshot,
    ) -> "ThreeArmContinuationContract":
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("three-arm continuation staging is invalid JSON") from exc
        raw = _exact_object(payload, _V6_STAGING_FIELDS, "three-arm continuation staging")
        if raw["schema_version"] != 6:
            raise ValueError("unsupported three-arm continuation staging schema")
        if raw["validity_policy"] != THREE_ARM_VALIDITY_POLICY:
            raise ValueError("three-arm continuation validity policy differs")
        if not isinstance(raw["code_revision"], str) or not _COMMIT.fullmatch(
            raw["code_revision"]
        ):
            raise ValueError("three-arm continuation requires a full code revision")
        execution_ready = raw["execution_ready"]
        blockers = raw["blockers"]
        if not isinstance(execution_ready, bool):
            raise ValueError("three-arm continuation execution_ready must be boolean")
        if not isinstance(blockers, list) or not all(
            isinstance(value, str) and value for value in blockers
        ):
            raise ValueError("three-arm continuation blockers must be text")
        if execution_ready and blockers:
            raise ValueError("executable three-arm continuation cannot retain blockers")
        if raw["no_next_phase"] is not True or raw["no_paid_provider_fallback"] is not True:
            raise ValueError("three-arm continuation must remain fail-closed")
        if raw["experience_initialization"] != "successor_continuation":
            raise ValueError("three-arm continuation experience initialization differs")
        qualification = _exact_object(
            raw["qualification_transfer"],
            {
                "receipt_sha256",
                "passed",
                "model_calls_started",
                "evaluator_transactions_started",
                "formal_score_reuse",
            },
            "three-arm continuation qualification transfer",
        )
        if (
            not isinstance(qualification["receipt_sha256"], str)
            or not _SHA256.fullmatch(qualification["receipt_sha256"])
            or qualification["passed"] is not True
            or qualification["model_calls_started"] != 0
            or qualification["evaluator_transactions_started"] != 0
            or qualification["formal_score_reuse"] is not False
        ):
            raise ValueError("three-arm continuation qualification transfer differs")
        if raw["variant_ids"] != list(THREE_ARMS):
            raise ValueError("three-arm continuation variant order differs")
        if raw["stream_policy"] != "balanced_interleaved":
            raise ValueError("three-arm continuation stream policy differs")

        signature = raw["model_signature"]
        if not isinstance(signature, dict) or set(signature) != {
            "executor_model",
            "reasoning_effort",
            "transport",
            "client_version",
        } or not all(isinstance(value, str) and value for value in signature.values()):
            raise ValueError("three-arm continuation model signature is invalid")
        source_hashes = raw["source_hashes"]
        if not isinstance(source_hashes, dict) or not source_hashes or any(
            not isinstance(name, str)
            or not name
            or not isinstance(value, str)
            or not _SHA256.fullmatch(value)
            for name, value in source_hashes.items()
        ):
            raise ValueError("three-arm continuation source hashes are invalid")
        rules = raw["rule_ids"]
        if (
            not isinstance(rules, list)
            or len(rules) != len(set(rules))
            or "cross_instance_distillation" not in rules
        ):
            raise ValueError("three-arm continuation rule ids are incomplete")
        for rule in rules:
            _safe_id(rule, "three-arm continuation rule id")
        if (
            raw["online_instances_per_suite"],
            raw["sealed_instances_per_suite"],
        ) != (6, 2):
            raise ValueError("three-arm continuation requires six online and two sealed")

        stream_payload = raw["stream"]
        if not isinstance(stream_payload, list) or len(stream_payload) != 24:
            raise ValueError("three-arm continuation requires a full 24-task stream")
        stream = tuple(
            _stream_item(item, expected_index=index)
            for index, item in enumerate(stream_payload)
        )
        if len({item.instance_id for item in stream}) != 24:
            raise ValueError("three-arm continuation instances must be unique")
        suites = tuple(dict.fromkeys(item.suite for item in stream))
        if len(suites) != 3:
            raise ValueError("three-arm continuation requires three suites")
        for suite in suites:
            selected = tuple(item for item in stream if item.suite == suite)
            if len(selected) != 8 or tuple(item.block_index for item in selected) != tuple(
                range(8)
            ):
                raise ValueError("three-arm continuation suite task positions differ")
            if tuple(item.learning_mode for item in selected) != (
                ("online",) * 6 + ("sealed",) * 2
            ):
                raise ValueError("three-arm continuation learning modes differ")
        for block_index in range(8):
            block = stream[block_index * 3 : (block_index + 1) * 3]
            offset = block_index % 3
            if tuple(item.suite for item in block) != suites[offset:] + suites[:offset]:
                raise ValueError("three-arm continuation interleaving differs")
            if any(item.block_index != block_index for item in block):
                raise ValueError("three-arm continuation block binding differs")
        prefix_ids = tuple(item.instance_id for item in stream[:6])
        snapshot_prefix = tuple(
            item.instance_id for item in source_snapshot.prefix_instance_receipts
        )
        if prefix_ids != snapshot_prefix:
            raise ValueError("three-arm continuation source prefix differs")

        continuation = _exact_object(
            raw["continuation"], _CONTINUATION_FIELDS, "three-arm continuation binding"
        )
        window = _exact_object(
            continuation["execution_window"],
            {"start_index", "stop_index"},
            "three-arm continuation execution window",
        )
        if window != {"start_index": 6, "stop_index": 24}:
            raise ValueError("three-arm continuation execution window must be [6,24)")
        if continuation["prefix_length"] != 6:
            raise ValueError("three-arm continuation prefix length differs")
        if continuation["source_snapshot_sha256"] != source_snapshot.sha256:
            raise ValueError("three-arm continuation source snapshot differs")
        if continuation["source_manifest_sha256"] != source_snapshot.source_manifest_sha256:
            raise ValueError("three-arm continuation source manifest differs")
        if continuation["source_staging_plan_sha256"] != (
            source_snapshot.source_staging_plan_sha256
        ):
            raise ValueError("three-arm continuation source staging differs")
        if continuation["input_online_checkpoint_sha256"] != (
            source_snapshot.online_checkpoint.sha256
        ):
            raise ValueError("three-arm continuation input online checkpoint differs")
        if continuation["input_online_bank_sha256"] != source_snapshot.online_bank.sha256:
            raise ValueError("three-arm continuation input online Bank differs")
        source_usage = ResourceVector.from_dict(continuation["source_committed_usage"])
        if source_usage != source_snapshot.source_committed_usage:
            raise ValueError("three-arm continuation source committed usage differs")
        tail_ids = continuation["excluded_consumed_tail_operation_ids"]
        expected_tail_ids = [
            item.operation_id for item in source_snapshot.excluded_consumed_tail
        ]
        if tail_ids != expected_tail_ids:
            raise ValueError("three-arm continuation excluded tail differs")

        cells_payload = raw["cell_entitlements"]
        if not isinstance(cells_payload, dict):
            raise ValueError("three-arm continuation cell entitlements must be an object")
        cells = {
            _safe_id(cell_id, "three-arm continuation cell id"): _resource_caps(
                value, f"three-arm continuation cell {cell_id}"
            )
            for cell_id, value in cells_payload.items()
        }
        expected_cells: set[str] = set()
        for item in stream[6:24]:
            for arm in THREE_ARMS:
                cell_id = f"formal:{item.suite}:{item.task_id}:{arm}"
                expected_cells.add(cell_id)
                cap = cells.get(cell_id)
                if cap is None or cap.model_calls != 16 or cap.evaluator_transactions != 8:
                    raise ValueError("three-arm continuation arm entitlement differs")
            distill_id = f"distill:{item.stream_index:03d}:{item.instance_id}"
            if item.learning_mode == "online":
                expected_cells.add(distill_id)
                if cells.get(distill_id) != ResourceCaps(model_calls=1):
                    raise ValueError("three-arm continuation online entitlement differs")
            elif distill_id in cells:
                raise ValueError("three-arm continuation sealed instance cannot distill")
        if set(cells) != expected_cells:
            raise ValueError("three-arm continuation entitlements must cover active suffix only")
        computed = ResourceCaps(
            model_calls=sum(value.model_calls for value in cells.values()),
            evaluator_transactions=sum(
                value.evaluator_transactions for value in cells.values()
            ),
            gpu_exclusive_seconds=sum(
                value.gpu_exclusive_seconds for value in cells.values()
            ),
            cpu_evaluator_seconds=sum(
                value.cpu_evaluator_seconds for value in cells.values()
            ),
        )
        declared = _resource_caps(
            raw["resource_entitlement_totals"], "three-arm continuation total"
        )
        suffix_caps = _resource_caps(raw["budgets"], "three-arm continuation suffix")
        if declared != computed or suffix_caps != declared:
            raise ValueError("three-arm continuation suffix budget must equal exact entitlements")
        if (computed.model_calls, computed.evaluator_transactions) != (876, 432):
            raise ValueError("three-arm continuation formal suffix totals differ")
        composite = _resource_caps(
            continuation["composite_hard_caps"], "three-arm composite"
        )
        combined = source_usage + computed
        _within(combined, composite, label="three-arm composite")

        return cls(
            staging_plan_sha256=_sha256(encoded),
            phase_id=_safe_id(raw["phase_id"], "three-arm continuation phase id"),
            model=signature["executor_model"],
            execution_ready=execution_ready,
            blockers=tuple(blockers),
            stream=stream,
            execution_start_index=6,
            execution_stop_index=24,
            suffix_global_caps=suffix_caps,
            suffix_entitlement_totals=computed,
            cell_entitlements=cells,
            source_snapshot_sha256=source_snapshot.sha256,
            source_manifest_sha256=source_snapshot.source_manifest_sha256,
            source_staging_plan_sha256=source_snapshot.source_staging_plan_sha256,
            input_online_checkpoint_sha256=source_snapshot.online_checkpoint.sha256,
            input_online_bank_sha256=source_snapshot.online_bank.sha256,
            source_committed_usage=source_usage,
            composite_hard_caps=composite,
            excluded_consumed_tail_operation_ids=tuple(tail_ids),
            qualification_transfer_sha256=qualification["receipt_sha256"],
        )

    @classmethod
    def from_staging_path(
        cls,
        path: Path,
        *,
        source_snapshot: ThreeArmContinuationSourceSnapshot,
    ) -> "ThreeArmContinuationContract":
        return cls.from_staging_bytes(
            Path(path).read_bytes(), source_snapshot=source_snapshot
        )

    def require_executable(self) -> None:
        if not self.execution_ready:
            suffix = ", ".join(self.blockers) or "execution_ready=false"
            raise RuntimeError(f"three-arm continuation staging is blocked: {suffix}")


__all__ = [
    "ArtifactBinding",
    "ContinuationSourceSpec",
    "ExcludedTailBinding",
    "ExcludedTailExpectation",
    "OperationJournalBinding",
    "PrefixReceiptBinding",
    "ThreeArmContinuationContract",
    "ThreeArmContinuationPrepareOutcome",
    "ThreeArmContinuationSourceGuard",
    "ThreeArmContinuationSourceSnapshot",
    "prepare_three_arm_continuation_source",
    "verify_three_arm_continuation_source",
]
