"""Append-only control plane for isolated, bounded B-online mechanisms.

This module intentionally contains no model gateway and no evaluator adapter.  A
caller must supply a :class:`MetaUpdateProposal`, its typed before/after
checkpoints, and the resolved parent/child M/P/A objects.  Learned lanes validate
those objects inside the controller before recording a transition.  The controller
also enforces lane isolation, stream order, exactly-once accounting, and
content-addressed recovery.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import math
import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from .learning import ExperienceBankSnapshot
from .meta_evolution import (
    HarnessArchiveSnapshot,
    MetaCheckpointV2,
    MetaPolicySnapshot,
    MetaUpdateProposal,
    TrustedMetaPolicyRegistry,
)


ONLINE_MECHANISMS = ("O0", "OM", "OP", "OA")
_LEARNED_MECHANISM = MappingProxyType({"OM": "M", "OP": "P", "OA": "A"})
_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_NON_PUBLIC_ID = re.compile(
    r"(?:/home/|/data\d*/|(?:^|[/:_.+\-])(?:private|hidden|future|secret)"
    r"(?:$|[/:_.+\-]))",
    re.IGNORECASE,
)


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
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


def _sha(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"invalid {label} sha256")
    return value


def _public_id(value: object, label: str) -> str:
    if (
        not isinstance(value, str)
        or _SAFE_ID.fullmatch(value) is None
        or _NON_PUBLIC_ID.search(value)
    ):
        raise ValueError(f"unsafe or non-public {label}")
    return value


def _strict_fields(payload: Mapping[str, Any], expected: set[str], label: str) -> None:
    if not isinstance(payload, Mapping) or set(payload) != expected:
        raise ValueError(f"{label} fields differ")


def _write_once(path: Path, content: bytes) -> None:
    if path.is_symlink():
        raise ValueError("refusing to write through a symlink")
    if path.exists():
        if not path.is_file() or path.read_bytes() != content:
            raise ValueError("write-once artifact conflicts with existing bytes")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, suffix=".online-meta.tmp")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


class _Addressed:
    def core_payload(self) -> dict[str, Any]:  # pragma: no cover - interface guard
        raise NotImplementedError

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.core_payload())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    def store(self, directory: Path) -> Path:
        path = directory / f"{self.sha256}.json"
        _write_once(path, self.canonical_bytes)
        return path


@dataclass(frozen=True)
class SealedMetaSourceEvidence(_Addressed):
    """Small public projection of one fully sealed source instance.

    Free-form traces, prompts, patches and evaluator details have no field in this
    schema.  Only finite public aggregate metrics and public identifiers survive.
    """

    source_suite: str
    source_instance_id: str
    source_stream_index: int
    sealed_arm_receipt_sha256: str
    public_metrics: Mapping[str, float]
    public_tags: tuple[str, ...]
    provenance_event_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "source_suite", _public_id(self.source_suite, "suite"))
        object.__setattr__(
            self,
            "source_instance_id",
            _public_id(self.source_instance_id, "source instance id"),
        )
        if type(self.source_stream_index) is not int or not 0 <= self.source_stream_index <= 999_999:
            raise ValueError("source stream index is out of range")
        object.__setattr__(
            self,
            "sealed_arm_receipt_sha256",
            _sha(self.sealed_arm_receipt_sha256, "sealed arm receipt"),
        )
        if not isinstance(self.public_metrics, Mapping) or not 1 <= len(self.public_metrics) <= 32:
            raise ValueError("public metrics must be a bounded non-empty object")
        metrics: dict[str, float] = {}
        for key, value in self.public_metrics.items():
            public_key = _public_id(key, "public metric name")
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("public metric values must be numeric")
            number = float(value)
            if not math.isfinite(number):
                raise ValueError("public metric values must be finite")
            metrics[public_key] = number
        object.__setattr__(self, "public_metrics", MappingProxyType(metrics))
        for label, values, minimum, maximum in (
            ("public tag", self.public_tags, 0, 32),
            ("provenance event id", self.provenance_event_ids, 1, 256),
        ):
            if (
                not isinstance(values, (tuple, list))
                or not minimum <= len(values) <= maximum
            ):
                raise ValueError(f"{label}s must be a bounded list")
            normalized = tuple(_public_id(item, label) for item in values)
            if len(set(normalized)) != len(normalized):
                raise ValueError(f"{label}s must be unique")
            object.__setattr__(
                self,
                "public_tags" if label == "public tag" else "provenance_event_ids",
                normalized,
            )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "SealedMetaSourceEvidence":
        _strict_fields(
            payload,
            {
                "schema_version",
                "object_kind",
                "source_suite",
                "source_instance_id",
                "source_stream_index",
                "sealed_arm_receipt_sha256",
                "public_metrics",
                "public_tags",
                "provenance_event_ids",
            },
            "sealed meta source evidence",
        )
        if payload["schema_version"] != 1 or payload["object_kind"] != "sealed_meta_source_evidence":
            raise ValueError("unsupported sealed meta source evidence schema")
        return cls(
            source_suite=payload["source_suite"],
            source_instance_id=payload["source_instance_id"],
            source_stream_index=payload["source_stream_index"],
            sealed_arm_receipt_sha256=payload["sealed_arm_receipt_sha256"],
            public_metrics=payload["public_metrics"],
            public_tags=tuple(payload["public_tags"]),
            provenance_event_ids=tuple(payload["provenance_event_ids"]),
        )

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "object_kind": "sealed_meta_source_evidence",
            "source_suite": self.source_suite,
            "source_instance_id": self.source_instance_id,
            "source_stream_index": self.source_stream_index,
            "sealed_arm_receipt_sha256": self.sealed_arm_receipt_sha256,
            "public_metrics": dict(self.public_metrics),
            "public_tags": list(self.public_tags),
            "provenance_event_ids": list(self.provenance_event_ids),
        }


@dataclass(frozen=True)
class MetaLaneBinding(_Addressed):
    experiment_id: str
    mechanism_id: str
    seed: int
    source_instance_ids: tuple[str, ...]
    source_evidence_sha256s: tuple[str, ...]
    genesis_checkpoint_sha256: str
    trusted_meta_registry_sha256: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "experiment_id", _public_id(self.experiment_id, "experiment id"))
        if self.mechanism_id not in ONLINE_MECHANISMS:
            raise ValueError("online mechanism must be O0, OM, OP, or OA")
        if type(self.seed) is not int or not 0 <= self.seed <= 2**31 - 1:
            raise ValueError("seed is out of range")
        if not isinstance(self.source_instance_ids, (tuple, list)) or not self.source_instance_ids:
            raise ValueError("source order must be non-empty")
        source_ids = tuple(_public_id(item, "source instance id") for item in self.source_instance_ids)
        evidence = tuple(_sha(item, "source evidence") for item in self.source_evidence_sha256s)
        if (
            len(source_ids) != len(evidence)
            or len(set(source_ids)) != len(source_ids)
            or len(set(evidence)) != len(evidence)
        ):
            raise ValueError("source order/evidence lengths differ or sources repeat")
        object.__setattr__(self, "source_instance_ids", source_ids)
        object.__setattr__(self, "source_evidence_sha256s", evidence)
        object.__setattr__(
            self, "genesis_checkpoint_sha256", _sha(self.genesis_checkpoint_sha256, "genesis checkpoint")
        )
        object.__setattr__(
            self,
            "trusted_meta_registry_sha256",
            _sha(self.trusted_meta_registry_sha256, "trusted meta registry"),
        )

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "object_kind": "meta_lane_binding",
            "experiment_id": self.experiment_id,
            "mechanism_id": self.mechanism_id,
            "seed": self.seed,
            "source_instance_ids": list(self.source_instance_ids),
            "source_evidence_sha256s": list(self.source_evidence_sha256s),
            "genesis_checkpoint_sha256": self.genesis_checkpoint_sha256,
            "trusted_meta_registry_sha256": self.trusted_meta_registry_sha256,
        }


@dataclass(frozen=True)
class MetaUpdateReceipt(_Addressed):
    lane_binding_sha256: str
    mechanism_id: str
    seed: int
    source_instance_id: str
    source_stream_index: int
    source_evidence_sha256: str
    previous_receipt_sha256: str | None
    action_kind: str
    proposal_sha256: str | None
    before_checkpoint_sha256: str
    after_checkpoint_sha256: str
    mechanism_update_count: int
    controller_model_calls: int = 0
    controller_evaluator_calls: int = 0

    def __post_init__(self) -> None:
        _sha(self.lane_binding_sha256, "lane binding")
        if self.mechanism_id not in ONLINE_MECHANISMS:
            raise ValueError("receipt mechanism differs")
        if type(self.seed) is not int or not 0 <= self.seed <= 2**31 - 1:
            raise ValueError("receipt seed differs")
        _public_id(self.source_instance_id, "receipt source instance id")
        if (
            type(self.source_stream_index) is not int
            or not 0 <= self.source_stream_index <= 999_999
        ):
            raise ValueError("receipt source index differs")
        _sha(self.source_evidence_sha256, "receipt evidence")
        if self.previous_receipt_sha256 is not None:
            _sha(self.previous_receipt_sha256, "previous receipt")
        _sha(self.before_checkpoint_sha256, "before checkpoint")
        _sha(self.after_checkpoint_sha256, "after checkpoint")
        if self.proposal_sha256 is not None:
            _sha(self.proposal_sha256, "proposal")
        if (
            type(self.controller_model_calls) is not int
            or type(self.controller_evaluator_calls) is not int
            or self.controller_model_calls != 0
            or self.controller_evaluator_calls != 0
        ):
            raise ValueError("online control plane cannot claim model/evaluator calls")
        if type(self.mechanism_update_count) is not int:
            raise ValueError("mechanism update count must be an integer")
        if self.mechanism_id == "O0":
            if (
                self.action_kind != "no_update"
                or self.proposal_sha256 is not None
                or self.before_checkpoint_sha256 != self.after_checkpoint_sha256
                or self.mechanism_update_count != 0
            ):
                raise ValueError("O0 must record a zero-call no-update fact")
        elif (
            self.action_kind != "typed_update"
            or self.proposal_sha256 is None
            or self.before_checkpoint_sha256 == self.after_checkpoint_sha256
            or self.mechanism_update_count != 1
        ):
            raise ValueError("learned lane must record exactly one typed update")

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "object_kind": "meta_update_receipt",
            "lane_binding_sha256": self.lane_binding_sha256,
            "mechanism_id": self.mechanism_id,
            "seed": self.seed,
            "source_instance_id": self.source_instance_id,
            "source_stream_index": self.source_stream_index,
            "source_evidence_sha256": self.source_evidence_sha256,
            "previous_receipt_sha256": self.previous_receipt_sha256,
            "action_kind": self.action_kind,
            "proposal_sha256": self.proposal_sha256,
            "before_checkpoint_sha256": self.before_checkpoint_sha256,
            "after_checkpoint_sha256": self.after_checkpoint_sha256,
            "mechanism_update_count": self.mechanism_update_count,
            "controller_model_calls": self.controller_model_calls,
            "controller_evaluator_calls": self.controller_evaluator_calls,
        }

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "MetaUpdateReceipt":
        _strict_fields(
            payload,
            {
                "schema_version",
                "object_kind",
                "lane_binding_sha256",
                "mechanism_id",
                "seed",
                "source_instance_id",
                "source_stream_index",
                "source_evidence_sha256",
                "previous_receipt_sha256",
                "action_kind",
                "proposal_sha256",
                "before_checkpoint_sha256",
                "after_checkpoint_sha256",
                "mechanism_update_count",
                "controller_model_calls",
                "controller_evaluator_calls",
            },
            "meta update receipt",
        )
        if payload["schema_version"] != 1 or payload["object_kind"] != "meta_update_receipt":
            raise ValueError("unsupported meta update receipt schema")
        return cls(
            lane_binding_sha256=payload["lane_binding_sha256"],
            mechanism_id=payload["mechanism_id"],
            seed=payload["seed"],
            source_instance_id=payload["source_instance_id"],
            source_stream_index=payload["source_stream_index"],
            source_evidence_sha256=payload["source_evidence_sha256"],
            previous_receipt_sha256=payload["previous_receipt_sha256"],
            action_kind=payload["action_kind"],
            proposal_sha256=payload["proposal_sha256"],
            before_checkpoint_sha256=payload["before_checkpoint_sha256"],
            after_checkpoint_sha256=payload["after_checkpoint_sha256"],
            mechanism_update_count=payload["mechanism_update_count"],
            controller_model_calls=payload["controller_model_calls"],
            controller_evaluator_calls=payload["controller_evaluator_calls"],
        )


@dataclass(frozen=True)
class SourceSnapshotSeal(_Addressed):
    lane_binding_sha256: str
    mechanism_id: str
    seed: int
    source_instance_ids: tuple[str, ...]
    source_evidence_sha256s: tuple[str, ...]
    update_receipt_sha256s: tuple[str, ...]
    final_checkpoint_sha256: str
    ledger_head_sha256: str

    def __post_init__(self) -> None:
        _sha(self.lane_binding_sha256, "seal lane binding")
        if self.mechanism_id not in ONLINE_MECHANISMS:
            raise ValueError("seal mechanism differs")
        if type(self.seed) is not int or not 0 <= self.seed <= 2**31 - 1:
            raise ValueError("seal seed differs")
        source_ids = tuple(_public_id(item, "sealed source id") for item in self.source_instance_ids)
        evidence = tuple(_sha(item, "sealed source evidence") for item in self.source_evidence_sha256s)
        receipts = tuple(_sha(item, "sealed update receipt") for item in self.update_receipt_sha256s)
        if (
            not source_ids
            or not (len(source_ids) == len(evidence) == len(receipts))
            or len(set(source_ids)) != len(source_ids)
            or len(set(evidence)) != len(evidence)
            or len(set(receipts)) != len(receipts)
        ):
            raise ValueError("source snapshot seal is incomplete")
        object.__setattr__(self, "source_instance_ids", source_ids)
        object.__setattr__(self, "source_evidence_sha256s", evidence)
        object.__setattr__(self, "update_receipt_sha256s", receipts)
        _sha(self.final_checkpoint_sha256, "final checkpoint")
        _sha(self.ledger_head_sha256, "ledger head")

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "object_kind": "source_snapshot_seal",
            "lane_binding_sha256": self.lane_binding_sha256,
            "mechanism_id": self.mechanism_id,
            "seed": self.seed,
            "source_instance_ids": list(self.source_instance_ids),
            "source_evidence_sha256s": list(self.source_evidence_sha256s),
            "update_receipt_sha256s": list(self.update_receipt_sha256s),
            "final_checkpoint_sha256": self.final_checkpoint_sha256,
            "ledger_head_sha256": self.ledger_head_sha256,
        }


def _read_addressed(path: Path, expected_sha256: str, parser: Any) -> Any:
    _sha(expected_sha256, "expected artifact")
    if path.name != f"{expected_sha256}.json" or path.is_symlink() or not path.is_file():
        raise ValueError("content-addressed artifact path differs")
    content = path.read_bytes()
    if hashlib.sha256(content).hexdigest() != expected_sha256:
        raise ValueError("content-addressed artifact digest differs")
    try:
        payload = json.loads(content.decode("utf-8"), parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("content-addressed artifact is not strict JSON") from exc
    if not isinstance(payload, Mapping) or _canonical_bytes(payload) != content:
        raise ValueError("content-addressed artifact is not canonical")
    item = parser(payload)
    if item.sha256 != expected_sha256:
        raise ValueError("parsed content-addressed artifact differs")
    return item


def validate_meta_lane_cohort(bindings: Sequence[MetaLaneBinding]) -> None:
    """Require a four-mechanism seed cohort to consume identical public sources."""

    if not isinstance(bindings, (tuple, list)) or len(bindings) != len(ONLINE_MECHANISMS):
        raise ValueError("meta lane cohort must contain exactly O0, OM, OP, and OA")
    if not all(isinstance(binding, MetaLaneBinding) for binding in bindings):
        raise TypeError("meta lane cohort contains a non-binding object")
    by_mechanism = {binding.mechanism_id: binding for binding in bindings}
    if set(by_mechanism) != set(ONLINE_MECHANISMS):
        raise ValueError("meta lane cohort mechanism coverage differs")
    reference = by_mechanism["O0"]
    for mechanism in ONLINE_MECHANISMS[1:]:
        candidate = by_mechanism[mechanism]
        if (
            candidate.experiment_id != reference.experiment_id
            or candidate.seed != reference.seed
            or candidate.source_instance_ids != reference.source_instance_ids
            or candidate.source_evidence_sha256s != reference.source_evidence_sha256s
            or candidate.genesis_checkpoint_sha256 != reference.genesis_checkpoint_sha256
            or candidate.trusted_meta_registry_sha256 != reference.trusted_meta_registry_sha256
        ):
            raise ValueError("meta lane cohort source/checkpoint bytes differ")


class OnlineMetaController:
    """Recoverable exactly-once recorder for one mechanism/seed lane."""

    def __init__(
        self,
        *,
        root: Path,
        binding: MetaLaneBinding,
        genesis_checkpoint: MetaCheckpointV2,
    ) -> None:
        if not isinstance(binding, MetaLaneBinding) or not isinstance(genesis_checkpoint, MetaCheckpointV2):
            raise TypeError("typed lane binding and genesis checkpoint are required")
        if genesis_checkpoint.sha256 != binding.genesis_checkpoint_sha256:
            raise ValueError("genesis checkpoint differs from lane binding")
        if genesis_checkpoint.next_stream_index != 0 or genesis_checkpoint.parent_checkpoint_sha256 is not None:
            raise ValueError("lane must begin at a true genesis checkpoint")
        if genesis_checkpoint.trusted_meta_registry_sha256 != binding.trusted_meta_registry_sha256:
            raise ValueError("lane registry differs from genesis checkpoint")
        self.binding = binding
        self.lane_root = (
            Path(os.path.abspath(os.fspath(root)))
            / binding.mechanism_id
            / f"seed-{binding.seed}"
            / binding.sha256
        )
        self.ledger_path = self.lane_root / "ledger.jsonl"
        self.lock_path = self.lane_root / "lane.lock"
        self.lane_root.mkdir(parents=True, exist_ok=True)
        _write_once(self.lane_root / "binding.json", binding.canonical_bytes)
        _write_once(
            self.lane_root / "checkpoints" / f"{genesis_checkpoint.sha256}.json",
            genesis_checkpoint.canonical_bytes,
        )

    def _ledger(self) -> list[dict[str, Any]]:
        if not self.ledger_path.exists():
            return []
        if self.ledger_path.is_symlink() or not self.ledger_path.is_file():
            raise ValueError("lane ledger path is unsafe")
        entries: list[dict[str, Any]] = []
        previous: str | None = None
        for ordinal, line in enumerate(self.ledger_path.read_bytes().splitlines(keepends=True)):
            try:
                payload = json.loads(line.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise ValueError("lane ledger contains invalid JSON") from exc
            _strict_fields(
                payload,
                {"schema_version", "object_kind", "ordinal", "lane_binding_sha256", "previous_event_sha256", "receipt_sha256", "event_sha256"},
                "lane ledger event",
            )
            core = {key: value for key, value in payload.items() if key != "event_sha256"}
            event_sha = hashlib.sha256(_canonical_bytes(core)).hexdigest()
            if (
                _canonical_bytes(payload) != line
                or payload["schema_version"] != 1
                or payload["object_kind"] != "meta_lane_event"
                or payload["ordinal"] != ordinal
                or payload["lane_binding_sha256"] != self.binding.sha256
                or payload["previous_event_sha256"] != previous
                or payload["event_sha256"] != event_sha
            ):
                raise ValueError("lane ledger hash chain differs")
            _sha(payload["receipt_sha256"], "ledger receipt")
            entries.append(payload)
            previous = event_sha
        return entries

    def _receipts(self, entries: Sequence[Mapping[str, Any]]) -> tuple[MetaUpdateReceipt, ...]:
        receipts: list[MetaUpdateReceipt] = []
        previous: str | None = None
        for ordinal, entry in enumerate(entries):
            digest = entry["receipt_sha256"]
            receipt = _read_addressed(
                self.lane_root / "receipts" / f"{digest}.json",
                digest,
                MetaUpdateReceipt.from_dict,
            )
            if (
                receipt.lane_binding_sha256 != self.binding.sha256
                or receipt.mechanism_id != self.binding.mechanism_id
                or receipt.seed != self.binding.seed
                or receipt.source_stream_index != ordinal
                or receipt.previous_receipt_sha256 != previous
            ):
                raise ValueError("lane receipt chain differs")
            receipts.append(receipt)
            previous = receipt.sha256
        return tuple(receipts)

    def _append_event(self, ordinal: int, receipt_sha256: str, previous: str | None) -> None:
        core = {
            "schema_version": 1,
            "object_kind": "meta_lane_event",
            "ordinal": ordinal,
            "lane_binding_sha256": self.binding.sha256,
            "previous_event_sha256": previous,
            "receipt_sha256": receipt_sha256,
        }
        payload = dict(core, event_sha256=hashlib.sha256(_canonical_bytes(core)).hexdigest())
        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
        descriptor = os.open(self.ledger_path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
        try:
            os.write(descriptor, _canonical_bytes(payload))
            os.fsync(descriptor)
        finally:
            os.close(descriptor)

    def update_once(
        self,
        evidence: SealedMetaSourceEvidence,
        *,
        before_checkpoint: MetaCheckpointV2,
        after_checkpoint: MetaCheckpointV2,
        proposal: MetaUpdateProposal | None,
        parent_memory: ExperienceBankSnapshot | None = None,
        memory: ExperienceBankSnapshot | None = None,
        parent_meta_policy: MetaPolicySnapshot | None = None,
        meta_policy: MetaPolicySnapshot | None = None,
        parent_harness_archive: HarnessArchiveSnapshot | None = None,
        harness_archive: HarnessArchiveSnapshot | None = None,
        registry: TrustedMetaPolicyRegistry | None = None,
    ) -> MetaUpdateReceipt:
        if not isinstance(evidence, SealedMetaSourceEvidence):
            raise TypeError("typed sealed public evidence is required")
        if not isinstance(before_checkpoint, MetaCheckpointV2) or not isinstance(after_checkpoint, MetaCheckpointV2):
            raise TypeError("typed before/after checkpoints are required")
        self.lock_path.touch(mode=0o600, exist_ok=True)
        with self.lock_path.open("r+b") as lock_handle:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
            entries = self._ledger()
            receipts = self._receipts(entries)
            index = evidence.source_stream_index
            if index >= len(self.binding.source_instance_ids):
                raise ValueError("source index is outside the frozen lane stream")
            if (
                evidence.source_instance_id != self.binding.source_instance_ids[index]
                or evidence.sha256 != self.binding.source_evidence_sha256s[index]
            ):
                raise ValueError("source identity or byte-identical evidence binding differs")
            if index > len(receipts):
                raise ValueError("source updates must follow the frozen stream order")
            expected_before = (
                self.binding.genesis_checkpoint_sha256
                if index == 0
                else receipts[index - 1].after_checkpoint_sha256
            )
            if before_checkpoint.sha256 != expected_before:
                raise ValueError("before checkpoint is not the lane checkpoint for this source")
            previous_receipt = None if index == 0 else receipts[index - 1].sha256

            if self.binding.mechanism_id == "O0":
                if proposal is not None or after_checkpoint.sha256 != before_checkpoint.sha256:
                    raise ValueError("O0 forbids proposals and checkpoint updates")
                receipt = MetaUpdateReceipt(
                    lane_binding_sha256=self.binding.sha256,
                    mechanism_id="O0",
                    seed=self.binding.seed,
                    source_instance_id=evidence.source_instance_id,
                    source_stream_index=index,
                    source_evidence_sha256=evidence.sha256,
                    previous_receipt_sha256=previous_receipt,
                    action_kind="no_update",
                    proposal_sha256=None,
                    before_checkpoint_sha256=before_checkpoint.sha256,
                    after_checkpoint_sha256=after_checkpoint.sha256,
                    mechanism_update_count=0,
                )
            else:
                if not isinstance(proposal, MetaUpdateProposal):
                    raise TypeError("learned lane requires a typed meta update proposal")
                if proposal.mechanism != _LEARNED_MECHANISM[self.binding.mechanism_id]:
                    raise ValueError("proposal mechanism differs from isolated lane")
                if (
                    proposal.source_instance_id != evidence.source_instance_id
                    or proposal.source_stream_index != index
                ):
                    raise ValueError("proposal source differs from sealed evidence")
                if not isinstance(parent_memory, ExperienceBankSnapshot) or not isinstance(
                    memory, ExperienceBankSnapshot
                ):
                    raise TypeError(
                        "learned lane requires resolved parent/child Experience Bank snapshots"
                    )
                if not isinstance(parent_meta_policy, MetaPolicySnapshot) or not isinstance(
                    meta_policy, MetaPolicySnapshot
                ):
                    raise TypeError(
                        "learned lane requires resolved parent/child meta-policy snapshots"
                    )
                if not isinstance(
                    parent_harness_archive, HarnessArchiveSnapshot
                ) or not isinstance(harness_archive, HarnessArchiveSnapshot):
                    raise TypeError(
                        "learned lane requires resolved parent/child Harness archives"
                    )
                if not isinstance(registry, TrustedMetaPolicyRegistry):
                    raise TypeError("learned lane requires a resolved trusted meta registry")
                expected_after = before_checkpoint.apply_verified(
                    proposal,
                    sealed_source_instance_ids=(evidence.source_instance_id,),
                    parent_memory=parent_memory,
                    memory=memory,
                    parent_meta_policy=parent_meta_policy,
                    meta_policy=meta_policy,
                    parent_harness_archive=parent_harness_archive,
                    harness_archive=harness_archive,
                    registry=registry,
                )
                if expected_after != after_checkpoint:
                    raise ValueError("after checkpoint is not the verified proposal result")
                receipt = MetaUpdateReceipt(
                    lane_binding_sha256=self.binding.sha256,
                    mechanism_id=self.binding.mechanism_id,
                    seed=self.binding.seed,
                    source_instance_id=evidence.source_instance_id,
                    source_stream_index=index,
                    source_evidence_sha256=evidence.sha256,
                    previous_receipt_sha256=previous_receipt,
                    action_kind="typed_update",
                    proposal_sha256=proposal.sha256,
                    before_checkpoint_sha256=before_checkpoint.sha256,
                    after_checkpoint_sha256=after_checkpoint.sha256,
                    mechanism_update_count=1,
                )

            if index < len(receipts):
                if receipts[index] != receipt:
                    raise ValueError("source was already recorded with conflicting content")
                return receipts[index]
            if index != len(receipts):
                raise ValueError("source updates must follow the frozen stream order")

            evidence.store(self.lane_root / "evidence")
            _write_once(
                self.lane_root / "checkpoints" / f"{before_checkpoint.sha256}.json",
                before_checkpoint.canonical_bytes,
            )
            _write_once(
                self.lane_root / "checkpoints" / f"{after_checkpoint.sha256}.json",
                after_checkpoint.canonical_bytes,
            )
            if proposal is not None:
                proposal.store(self.lane_root / "proposals")
                _write_once(
                    self.lane_root
                    / "resolved"
                    / "registries"
                    / f"{registry.sha256}.json",
                    registry.canonical_bytes,
                )
                for mechanism_root, parent, child in (
                    ("memory", parent_memory, memory),
                    ("meta_policies", parent_meta_policy, meta_policy),
                    (
                        "harness_archives",
                        parent_harness_archive,
                        harness_archive,
                    ),
                ):
                    for item in (parent, child):
                        _write_once(
                            self.lane_root
                            / "resolved"
                            / mechanism_root
                            / f"{item.sha256}.json",
                            item.canonical_bytes,
                        )
            receipt.store(self.lane_root / "receipts")
            previous_event = entries[-1]["event_sha256"] if entries else None
            self._append_event(index, receipt.sha256, previous_event)
            return receipt

    def seal_source_snapshot(self) -> SourceSnapshotSeal:
        self.lock_path.touch(mode=0o600, exist_ok=True)
        with self.lock_path.open("r+b") as lock_handle:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
            entries = self._ledger()
            receipts = self._receipts(entries)
            if len(receipts) != len(self.binding.source_instance_ids):
                raise ValueError("cannot seal before every frozen source is complete")
            seal = SourceSnapshotSeal(
                lane_binding_sha256=self.binding.sha256,
                mechanism_id=self.binding.mechanism_id,
                seed=self.binding.seed,
                source_instance_ids=self.binding.source_instance_ids,
                source_evidence_sha256s=self.binding.source_evidence_sha256s,
                update_receipt_sha256s=tuple(receipt.sha256 for receipt in receipts),
                final_checkpoint_sha256=receipts[-1].after_checkpoint_sha256,
                ledger_head_sha256=entries[-1]["event_sha256"],
            )
            seal.store(self.lane_root / "source_snapshots")
            return seal


__all__ = [
    "ONLINE_MECHANISMS",
    "MetaLaneBinding",
    "MetaUpdateReceipt",
    "OnlineMetaController",
    "SealedMetaSourceEvidence",
    "SourceSnapshotSeal",
    "validate_meta_lane_cohort",
]
