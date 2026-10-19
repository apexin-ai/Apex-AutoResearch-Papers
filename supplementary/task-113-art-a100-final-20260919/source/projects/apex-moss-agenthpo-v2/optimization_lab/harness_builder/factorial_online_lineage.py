"""Zero-call lineage contracts for the factorial B-online pilot.

The artifacts here bind the exact logical plan to sixteen isolated
``benchmark x seed x mechanism`` lanes and to terminal update facts.  They
neither resolve the referenced source/operation receipts nor expose an
execution interface, so authority and entitlements remain fail-closed.
"""

from __future__ import annotations

from dataclasses import dataclass, fields as dataclass_fields
import hashlib
import json
from pathlib import PurePosixPath
import re
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from .factorial_trunk import compiled_harness_semantic_sha256
from .factorial_online_plan import (
    FactorialOnlineZeroCallPlan,
    ONLINE_MECHANISMS,
    OnlineAttemptSlot,
    OnlineMechanismUpdateSlot,
)
from .learning import ExperienceBankSnapshot
from .meta_evolution import (
    HarnessArchiveSnapshot,
    MetaCheckpointV2,
    MetaPolicySnapshot,
    MetaUpdateProposal,
    TrustedMetaPolicyRegistry,
    validate_memory_snapshot,
)
from .meta_prior import BuilderMetaPrior
from .operators import CompiledHarness, HarnessContext, TrustedOperatorRegistry
from .schema import BuilderVariant, HarnessDecision


ZERO_SHA256 = "0" * 64
LINEAGE_READINESS = "SOURCE_TERMINAL_AND_OPERATION_LEDGER_REPLAY_NOT_READY"
HELDOUT_BINDING_READINESS = (
    "TYPED_STATE_AND_PLANNER_CONTEXT_BOUND_SOURCE_TERMINAL_AND_OPERATION_"
    "LEDGER_REPLAY_NOT_READY"
)
HELDOUT_PROJECTIONS = ("NONE", "BUILDER_META_PRIOR")
STATE_KINDS = MappingProxyType(
    {
        "O0": "NONE",
        "OM": "CONTENT_ADDRESSED_META_MEMORY",
        "OP": "TYPED_VERSIONED_META_POLICY",
        "OA": "TYPED_HARNESS_POPULATION_ARCHIVE",
    }
)
TERMINAL_UPDATE_OUTCOMES = (
    "APPLIED",
    "CONTRACT_REJECTED",
    "OPERATION_INTERRUPTED",
)
_SHA = re.compile(r"[0-9a-f]{64}")
_SAFE = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_PATH = re.compile(r"[A-Za-z0-9][A-Za-z0-9._+-]{0,127}")


class FactorialOnlineLineageError(ValueError):
    pass


def _canonical(payload: object) -> bytes:
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
        ).encode()
    except (TypeError, ValueError, UnicodeError) as exc:
        raise FactorialOnlineLineageError("lineage is not canonical JSON") from exc


def _digest(payload: object) -> str:
    return hashlib.sha256(_canonical(payload)).hexdigest()


def _sha(value: object, label: str, *, zero: bool = False) -> str:
    if not isinstance(value, str) or _SHA.fullmatch(value) is None:
        raise FactorialOnlineLineageError(f"invalid {label}")
    if not zero and value == ZERO_SHA256:
        raise FactorialOnlineLineageError(f"empty {label}")
    return value


def _safe(value: object, label: str) -> str:
    if not isinstance(value, str) or _SAFE.fullmatch(value) is None:
        raise FactorialOnlineLineageError(f"unsafe {label}")
    return value


def _public_text_tuple(
    values: Sequence[str], label: str, *, maximum: int = 64
) -> tuple[str, ...]:
    if isinstance(values, (str, bytes)) or not isinstance(values, Sequence):
        raise FactorialOnlineLineageError(f"{label} is not a text sequence")
    result = tuple(values)
    if not 1 <= len(result) <= maximum or any(
        not isinstance(item, str)
        or not item.strip()
        or len(item) > 4_000
        or "/home/" in item
        or "/data" in item
        for item in result
    ):
        raise FactorialOnlineLineageError(f"{label} contains unsafe public text")
    return result


def _decode(raw: bytes, *, label: str) -> dict[str, Any]:
    def duplicate(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        value: dict[str, Any] = {}
        for key, item in pairs:
            if key in value:
                raise FactorialOnlineLineageError(f"{label} repeats {key}")
            value[key] = item
        return value

    def constant(value: str) -> None:
        raise FactorialOnlineLineageError(f"{label} contains {value}")

    try:
        payload = json.loads(
            raw.decode(errors="strict"),
            object_pairs_hook=duplicate,
            parse_constant=constant,
        )
    except (AttributeError, UnicodeError, json.JSONDecodeError) as exc:
        raise FactorialOnlineLineageError(f"{label} is invalid") from exc
    if not isinstance(payload, dict) or _canonical(payload) != raw:
        raise FactorialOnlineLineageError(f"{label} is not canonical")
    return payload


def _fields(payload: Mapping[str, Any], fields: set[str], label: str) -> None:
    if not isinstance(payload, Mapping) or set(payload) != fields:
        raise FactorialOnlineLineageError(f"{label} fields differ")


def attempt_slot_sha256(slot: OnlineAttemptSlot) -> str:
    if type(slot) is not OnlineAttemptSlot:
        raise TypeError("typed attempt slot required")
    return _digest(slot.to_dict())


def update_slot_sha256(slot: OnlineMechanismUpdateSlot) -> str:
    if type(slot) is not OnlineMechanismUpdateSlot:
        raise TypeError("typed update slot required")
    return _digest(slot.to_dict())


@dataclass(frozen=True)
class OnlineLaneBinding:
    plan_sha256: str
    contract_sha256: str
    benchmark_id: str
    seed: int
    mechanism_id: str
    state_kind: str
    source_attempt_slot_sha256s: tuple[str, ...]
    source_update_slot_sha256s: tuple[str, ...]
    schema_version: int = 1

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise FactorialOnlineLineageError("lane schema differs")
        _sha(self.plan_sha256, "lane plan")
        _sha(self.contract_sha256, "lane contract")
        if not isinstance(self.benchmark_id, str) or _PATH.fullmatch(
            self.benchmark_id
        ) is None:
            raise FactorialOnlineLineageError("unsafe lane benchmark")
        if type(self.seed) is not int or not 0 <= self.seed <= 2**31 - 1:
            raise FactorialOnlineLineageError("lane seed differs")
        if self.mechanism_id not in ONLINE_MECHANISMS:
            raise FactorialOnlineLineageError("lane mechanism differs")
        if self.state_kind != STATE_KINDS[self.mechanism_id]:
            raise FactorialOnlineLineageError("lane state kind differs")
        if not isinstance(self.source_attempt_slot_sha256s, tuple) or not (
            self.source_attempt_slot_sha256s
        ):
            raise FactorialOnlineLineageError("lane source attempts differ")
        if not isinstance(self.source_update_slot_sha256s, tuple):
            raise FactorialOnlineLineageError("lane source updates differ")
        for digest in self.source_attempt_slot_sha256s:
            _sha(digest, "lane source attempt slot")
        for digest in self.source_update_slot_sha256s:
            _sha(digest, "lane source update slot")
        if len(set(self.source_attempt_slot_sha256s)) != len(
            self.source_attempt_slot_sha256s
        ) or len(set(self.source_update_slot_sha256s)) != len(
            self.source_update_slot_sha256s
        ):
            raise FactorialOnlineLineageError("lane repeats a source slot")
        if (self.mechanism_id == "O0") != (
            self.state_kind == "NONE" and not self.source_update_slot_sha256s
        ):
            raise FactorialOnlineLineageError("O0/learned lane state differs")

    def to_dict(self) -> dict[str, Any]:
        return {
            "benchmark_id": self.benchmark_id,
            "contract_sha256": self.contract_sha256,
            "mechanism_id": self.mechanism_id,
            "plan_sha256": self.plan_sha256,
            "schema_version": self.schema_version,
            "seed": self.seed,
            "source_attempt_slot_sha256s": list(
                self.source_attempt_slot_sha256s
            ),
            "source_update_slot_sha256s": list(self.source_update_slot_sha256s),
            "state_kind": self.state_kind,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @property
    def trusted_relative_root(self) -> str:
        parts = (
            "factorial-online-lineage",
            self.plan_sha256,
            "benchmarks",
            self.benchmark_id,
            "seeds",
            f"seed-{self.seed}",
            "mechanisms",
            self.mechanism_id,
            self.sha256,
        )
        if any(_PATH.fullmatch(item) is None for item in parts):
            raise FactorialOnlineLineageError("unsafe trusted lane root")
        path = PurePosixPath(*parts)
        if path.is_absolute() or ".." in path.parts:
            raise FactorialOnlineLineageError("trusted lane root is not relative")
        return path.as_posix()

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "OnlineLaneBinding":
        expected = {
            "benchmark_id",
            "contract_sha256",
            "mechanism_id",
            "plan_sha256",
            "schema_version",
            "seed",
            "source_attempt_slot_sha256s",
            "source_update_slot_sha256s",
            "state_kind",
        }
        _fields(payload, expected, "lane")
        if not isinstance(payload["source_attempt_slot_sha256s"], list) or not (
            isinstance(payload["source_update_slot_sha256s"], list)
        ):
            raise FactorialOnlineLineageError("lane slot arrays differ")
        return cls(
            **{
                **dict(payload),
                "source_attempt_slot_sha256s": tuple(
                    payload["source_attempt_slot_sha256s"]
                ),
                "source_update_slot_sha256s": tuple(
                    payload["source_update_slot_sha256s"]
                ),
            }
        )


@dataclass(frozen=True)
class ResolvedOnlineState:
    """All four typed objects resolved behind one meta checkpoint.

    A digest supplied by a proposer is never enough: this object validates the
    memory, policy and Harness archive bytes against the checkpoint and the
    immutable trusted Registry before a held-out task may see a meta-prior.
    """

    checkpoint: MetaCheckpointV2
    memory: ExperienceBankSnapshot
    meta_policy: MetaPolicySnapshot
    harness_archive: HarnessArchiveSnapshot
    registry: TrustedMetaPolicyRegistry

    def __post_init__(self) -> None:
        if type(self.checkpoint) is not MetaCheckpointV2:
            raise TypeError("typed meta checkpoint required")
        if type(self.memory) is not ExperienceBankSnapshot:
            raise TypeError("typed Experience Bank snapshot required")
        if type(self.meta_policy) is not MetaPolicySnapshot:
            raise TypeError("typed meta-policy snapshot required")
        if type(self.harness_archive) is not HarnessArchiveSnapshot:
            raise TypeError("typed Harness archive snapshot required")
        if type(self.registry) is not TrustedMetaPolicyRegistry:
            raise TypeError("typed trusted meta Registry required")
        if self.registry.sha256 != TrustedMetaPolicyRegistry.default().sha256:
            raise FactorialOnlineLineageError("online Registry is not the frozen default")
        try:
            validate_memory_snapshot(self.memory)
            self.registry.validate_policy(self.meta_policy)
            if self.harness_archive.trusted_meta_registry_sha256 != self.registry.sha256:
                raise ValueError("Harness archive Registry differs")
            for node in self.harness_archive.nodes:
                self.registry.validate_harness(
                    node.component_selection,
                    label="resolved online Harness archive node",
                )
        except (TypeError, ValueError) as exc:
            raise FactorialOnlineLineageError(
                "resolved online state contains an invalid typed object"
            ) from exc
        expected = {
            "M": self.memory.sha256,
            "P": self.meta_policy.sha256,
            "A": self.harness_archive.sha256,
        }
        if (
            self.checkpoint.trusted_meta_registry_sha256 != self.registry.sha256
            or dict(self.checkpoint.mechanism_sha256s) != expected
        ):
            raise FactorialOnlineLineageError(
                "online checkpoint hashes do not resolve to supplied objects"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "checkpoint_sha256": self.checkpoint.sha256,
            "harness_archive_sha256": self.harness_archive.sha256,
            "memory_sha256": self.memory.sha256,
            "meta_policy_sha256": self.meta_policy.sha256,
            "trusted_meta_registry_sha256": self.registry.sha256,
        }

    @property
    def sha256(self) -> str:
        return _digest(self.to_dict())

    def mechanism_state_sha256(self, mechanism_id: str) -> str:
        mapping = {
            "OM": self.memory.sha256,
            "OP": self.meta_policy.sha256,
            "OA": self.harness_archive.sha256,
        }
        if mechanism_id not in mapping:
            raise FactorialOnlineLineageError(
                "O0 has no learned mechanism state snapshot"
            )
        return mapping[mechanism_id]


def factorial_online_genesis_state() -> ResolvedOnlineState:
    """Return the one byte-stable empty state shared by all online lanes."""

    registry = TrustedMetaPolicyRegistry.default()
    memory = ExperienceBankSnapshot.create(
        bank_id="factorial-online-memory-v000",
        parent_sha256=None,
        records=(),
    )
    policy = MetaPolicySnapshot.create(
        policy_id="factorial-online-policy-v000",
        registry=registry,
    )
    archive = HarnessArchiveSnapshot.create(
        archive_id="factorial-online-archive-v000",
        registry=registry,
    )
    checkpoint = MetaCheckpointV2(
        checkpoint_id="factorial-online-checkpoint-v000",
        parent_checkpoint_sha256=None,
        trusted_meta_registry_sha256=registry.sha256,
        next_stream_index=0,
        learned_through_instance_id=None,
        memory_sha256=memory.sha256,
        meta_policy_sha256=policy.sha256,
        harness_archive_sha256=archive.sha256,
    )
    return ResolvedOnlineState(
        checkpoint=checkpoint,
        memory=memory,
        meta_policy=policy,
        harness_archive=archive,
        registry=registry,
    )


@dataclass(frozen=True)
class OnlineUpdateLineageReceipt:
    lane_binding_sha256: str
    ordinal: int
    update_slot_sha256: str
    updater_operation_id: str
    source_terminal_receipt_sha256: str
    parent_state_sha256: str
    parent_checkpoint_sha256: str
    output_state_sha256: str
    output_checkpoint_sha256: str
    operation_record_sha256: str
    previous_transition_sha256: str
    outcome: str
    schema_version: int = 1

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise FactorialOnlineLineageError("transition schema differs")
        for value, label, zero in (
            (self.lane_binding_sha256, "transition lane", False),
            (self.update_slot_sha256, "transition update slot", False),
            (self.source_terminal_receipt_sha256, "source terminal", False),
            (self.parent_state_sha256, "parent state", False),
            (self.parent_checkpoint_sha256, "parent checkpoint", False),
            (self.output_state_sha256, "output state", False),
            (self.output_checkpoint_sha256, "output checkpoint", False),
            (self.operation_record_sha256, "operation record", False),
            (self.previous_transition_sha256, "previous transition", True),
        ):
            _sha(value, label, zero=zero)
        _safe(self.updater_operation_id, "updater operation id")
        if type(self.ordinal) is not int or self.ordinal < 1:
            raise FactorialOnlineLineageError("transition ordinal differs")
        if (self.ordinal == 1) != (
            self.previous_transition_sha256 == ZERO_SHA256
        ):
            raise FactorialOnlineLineageError("transition parent digest differs")
        if self.outcome not in TERMINAL_UPDATE_OUTCOMES:
            raise FactorialOnlineLineageError("transition is not terminal")
        changed = (
            self.parent_state_sha256 != self.output_state_sha256,
            self.parent_checkpoint_sha256 != self.output_checkpoint_sha256,
        )
        if self.outcome == "APPLIED" and changed != (True, True):
            raise FactorialOnlineLineageError(
                "applied update must change state and checkpoint"
            )
        if self.outcome != "APPLIED" and changed != (False, False):
            raise FactorialOnlineLineageError(
                "terminal failure must explicitly carry state forward"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "lane_binding_sha256": self.lane_binding_sha256,
            "operation_record_sha256": self.operation_record_sha256,
            "ordinal": self.ordinal,
            "outcome": self.outcome,
            "output_checkpoint_sha256": self.output_checkpoint_sha256,
            "output_state_sha256": self.output_state_sha256,
            "parent_checkpoint_sha256": self.parent_checkpoint_sha256,
            "parent_state_sha256": self.parent_state_sha256,
            "previous_transition_sha256": self.previous_transition_sha256,
            "schema_version": self.schema_version,
            "source_terminal_receipt_sha256": (
                self.source_terminal_receipt_sha256
            ),
            "update_slot_sha256": self.update_slot_sha256,
            "updater_operation_id": self.updater_operation_id,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_sha256: str
    ) -> "OnlineUpdateLineageReceipt":
        payload = _decode(raw, label="transition")
        _fields(
            payload,
            {
                "lane_binding_sha256",
                "operation_record_sha256",
                "ordinal",
                "outcome",
                "output_checkpoint_sha256",
                "output_state_sha256",
                "parent_checkpoint_sha256",
                "parent_state_sha256",
                "previous_transition_sha256",
                "schema_version",
                "source_terminal_receipt_sha256",
                "update_slot_sha256",
                "updater_operation_id",
            },
            "transition",
        )
        item = cls(**payload)
        _sha(expected_sha256, "expected transition")
        if item.canonical_bytes != raw or item.sha256 != expected_sha256:
            raise FactorialOnlineLineageError("transition replay differs")
        return item


@dataclass(frozen=True)
class ResolvedOnlineTransition:
    """Typed objects required to independently replay one applied M/P/A update."""

    receipt: OnlineUpdateLineageReceipt
    proposal: MetaUpdateProposal
    before_state: ResolvedOnlineState
    after_state: ResolvedOnlineState

    def __post_init__(self) -> None:
        if type(self.receipt) is not OnlineUpdateLineageReceipt:
            raise TypeError("typed online transition receipt required")
        if type(self.proposal) is not MetaUpdateProposal:
            raise TypeError("typed meta update proposal required")
        if type(self.before_state) is not ResolvedOnlineState or type(
            self.after_state
        ) is not ResolvedOnlineState:
            raise TypeError("typed before/after online states required")

    def to_dict(self) -> dict[str, Any]:
        return {
            "after_state_sha256": self.after_state.sha256,
            "before_state_sha256": self.before_state.sha256,
            "lineage_receipt_sha256": self.receipt.sha256,
            "proposal_sha256": self.proposal.sha256,
        }

    @property
    def sha256(self) -> str:
        return _digest(self.to_dict())


@dataclass(frozen=True)
class OnlineHeldoutStateBindingReceipt:
    """Zero-authority proof of the state visible to one held-out Builder call."""

    plan_sha256: str
    contract_sha256: str
    lane_binding_sha256: str
    benchmark_id: str
    seed: int
    mechanism_id: str
    state_kind: str
    stage: str
    instance_id: str
    version: int
    attempt_slot_sha256: str
    builder_operation_id: str
    target_stream_index: int
    source_final_attempt_slot_sha256s: tuple[str, ...]
    source_terminal_receipt_sha256s: tuple[str, ...]
    genesis_state_sha256: str
    genesis_checkpoint_sha256: str
    resolved_state_sha256: str
    final_checkpoint_sha256: str
    memory_sha256: str
    meta_policy_sha256: str
    harness_archive_sha256: str
    trusted_meta_registry_sha256: str
    mechanism_state_sha256: str
    transition_receipt_sha256s: tuple[str, ...]
    transition_head_sha256: str
    builder_meta_prior_sha256: str
    target_descriptors_sha256: str
    immutable_task_context_sha256: str
    task_local_history_sha256: str
    planner_context_sha256: str
    context_binding_sha256: str
    state_projection: str
    readiness: str = HELDOUT_BINDING_READINESS
    execution_authority: str = "NOT_GRANTED"
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    schema_version: int = 1

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise FactorialOnlineLineageError("held-out binding schema differs")
        for value, label, zero in (
            (self.plan_sha256, "held-out plan", False),
            (self.contract_sha256, "held-out contract", False),
            (self.lane_binding_sha256, "held-out lane", False),
            (self.attempt_slot_sha256, "held-out attempt slot", False),
            (self.genesis_state_sha256, "held-out genesis state", False),
            (self.genesis_checkpoint_sha256, "held-out genesis checkpoint", False),
            (self.resolved_state_sha256, "held-out resolved state", False),
            (self.final_checkpoint_sha256, "held-out final checkpoint", False),
            (self.memory_sha256, "held-out memory", False),
            (self.meta_policy_sha256, "held-out meta-policy", False),
            (self.harness_archive_sha256, "held-out Harness archive", False),
            (self.trusted_meta_registry_sha256, "held-out Registry", False),
            (self.mechanism_state_sha256, "held-out mechanism state", True),
            (self.transition_head_sha256, "held-out transition head", True),
            (self.builder_meta_prior_sha256, "held-out Builder prior", True),
            (self.target_descriptors_sha256, "held-out target descriptors", False),
            (
                self.immutable_task_context_sha256,
                "held-out immutable task context",
                False,
            ),
            (self.task_local_history_sha256, "held-out task-local history", False),
            (self.planner_context_sha256, "held-out planner context", False),
            (self.context_binding_sha256, "held-out compile context", False),
        ):
            _sha(value, label, zero=zero)
        if not isinstance(self.benchmark_id, str) or _PATH.fullmatch(
            self.benchmark_id
        ) is None:
            raise FactorialOnlineLineageError("unsafe held-out benchmark")
        _safe(self.instance_id, "held-out instance id")
        _safe(self.builder_operation_id, "held-out Builder operation id")
        if type(self.seed) is not int or not 0 <= self.seed <= 2**31 - 1:
            raise FactorialOnlineLineageError("held-out seed differs")
        if self.mechanism_id not in ONLINE_MECHANISMS:
            raise FactorialOnlineLineageError("held-out mechanism differs")
        if self.state_kind != STATE_KINDS[self.mechanism_id]:
            raise FactorialOnlineLineageError("held-out state kind differs")
        if self.stage not in {"O1", "O2"}:
            raise FactorialOnlineLineageError("held-out stage differs")
        if type(self.version) is not int or (
            (self.stage == "O1") != (self.version == 1)
        ) or (self.stage == "O2" and self.version < 2):
            raise FactorialOnlineLineageError("held-out stage/version differs")
        if type(self.target_stream_index) is not int or self.target_stream_index < 1:
            raise FactorialOnlineLineageError("held-out target stream index differs")
        for values, label, allow_empty in (
            (
                self.source_final_attempt_slot_sha256s,
                "source final attempt slot",
                False,
            ),
            (self.source_terminal_receipt_sha256s, "source terminal receipt", False),
            (self.transition_receipt_sha256s, "transition receipt", True),
        ):
            if not isinstance(values, tuple) or (not allow_empty and not values):
                raise FactorialOnlineLineageError(f"held-out {label} array differs")
            for digest in values:
                _sha(digest, label)
            if len(set(values)) != len(values):
                raise FactorialOnlineLineageError(f"held-out {label} repeats")
        if len(self.source_final_attempt_slot_sha256s) != len(
            self.source_terminal_receipt_sha256s
        ):
            raise FactorialOnlineLineageError(
                "held-out source final/terminal cardinality differs"
            )
        if self.state_projection not in HELDOUT_PROJECTIONS:
            raise FactorialOnlineLineageError("held-out state projection differs")
        if self.mechanism_id == "O0":
            if (
                self.state_projection != "NONE"
                or self.mechanism_state_sha256 != ZERO_SHA256
                or self.builder_meta_prior_sha256 != ZERO_SHA256
                or self.transition_receipt_sha256s
                or self.transition_head_sha256 != ZERO_SHA256
                or self.final_checkpoint_sha256 != self.genesis_checkpoint_sha256
                or self.resolved_state_sha256 != self.genesis_state_sha256
            ):
                raise FactorialOnlineLineageError("O0 received learned online state")
        elif (
            self.state_projection != "BUILDER_META_PRIOR"
            or self.mechanism_state_sha256 == ZERO_SHA256
            or self.builder_meta_prior_sha256 == ZERO_SHA256
            or not self.transition_receipt_sha256s
            or self.transition_head_sha256
            != self.transition_receipt_sha256s[-1]
            or self.final_checkpoint_sha256 == self.genesis_checkpoint_sha256
            or self.resolved_state_sha256 == self.genesis_state_sha256
        ):
            raise FactorialOnlineLineageError(
                "learned lane is missing a resolved projected state"
            )
        if self.readiness != HELDOUT_BINDING_READINESS:
            raise FactorialOnlineLineageError("held-out readiness was upgraded")
        if self.execution_authority != "NOT_GRANTED":
            raise FactorialOnlineLineageError("held-out binding cannot grant execution")
        if (
            type(self.model_call_entitlement) is not int
            or type(self.evaluator_transaction_entitlement) is not int
            or self.model_call_entitlement != 0
            or self.evaluator_transaction_entitlement != 0
        ):
            raise FactorialOnlineLineageError(
                "held-out binding entitlement is not zero"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_slot_sha256": self.attempt_slot_sha256,
            "benchmark_id": self.benchmark_id,
            "builder_meta_prior_sha256": self.builder_meta_prior_sha256,
            "builder_operation_id": self.builder_operation_id,
            "context_binding_sha256": self.context_binding_sha256,
            "contract_sha256": self.contract_sha256,
            "evaluator_transaction_entitlement": (
                self.evaluator_transaction_entitlement
            ),
            "execution_authority": self.execution_authority,
            "final_checkpoint_sha256": self.final_checkpoint_sha256,
            "genesis_checkpoint_sha256": self.genesis_checkpoint_sha256,
            "genesis_state_sha256": self.genesis_state_sha256,
            "harness_archive_sha256": self.harness_archive_sha256,
            "instance_id": self.instance_id,
            "lane_binding_sha256": self.lane_binding_sha256,
            "mechanism_id": self.mechanism_id,
            "mechanism_state_sha256": self.mechanism_state_sha256,
            "memory_sha256": self.memory_sha256,
            "meta_policy_sha256": self.meta_policy_sha256,
            "model_call_entitlement": self.model_call_entitlement,
            "plan_sha256": self.plan_sha256,
            "planner_context_sha256": self.planner_context_sha256,
            "immutable_task_context_sha256": (
                self.immutable_task_context_sha256
            ),
            "readiness": self.readiness,
            "resolved_state_sha256": self.resolved_state_sha256,
            "schema_version": self.schema_version,
            "seed": self.seed,
            "source_final_attempt_slot_sha256s": list(
                self.source_final_attempt_slot_sha256s
            ),
            "source_terminal_receipt_sha256s": list(
                self.source_terminal_receipt_sha256s
            ),
            "stage": self.stage,
            "state_kind": self.state_kind,
            "state_projection": self.state_projection,
            "target_descriptors_sha256": self.target_descriptors_sha256,
            "target_stream_index": self.target_stream_index,
            "task_local_history_sha256": self.task_local_history_sha256,
            "transition_head_sha256": self.transition_head_sha256,
            "transition_receipt_sha256s": list(
                self.transition_receipt_sha256s
            ),
            "trusted_meta_registry_sha256": (
                self.trusted_meta_registry_sha256
            ),
            "version": self.version,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_sha256: str
    ) -> "OnlineHeldoutStateBindingReceipt":
        payload = _decode(raw, label="held-out state binding")
        _fields(
            payload,
            {item.name for item in dataclass_fields(cls)},
            "held-out state binding",
        )
        for name in (
            "source_final_attempt_slot_sha256s",
            "source_terminal_receipt_sha256s",
            "transition_receipt_sha256s",
        ):
            if not isinstance(payload[name], list):
                raise FactorialOnlineLineageError(
                    "held-out state binding array differs"
                )
            payload[name] = tuple(payload[name])
        item = cls(**payload)
        _sha(expected_sha256, "expected held-out state binding")
        if item.canonical_bytes != raw or item.sha256 != expected_sha256:
            raise FactorialOnlineLineageError(
                "held-out state binding replay differs"
            )
        return item


@dataclass(frozen=True)
class OnlineHeldoutCompileProjectionReceipt:
    """Bind a state receipt to an actual trusted compile without solver leakage."""

    state_binding_receipt_sha256: str
    attempt_slot_sha256: str
    context_binding_sha256: str
    decision_sha256: str
    compiled_harness_semantic_sha256: str
    solution_prompt_sha256: str
    builder_meta_prior_sha256: str
    state_projection: str
    prior_direct_solution_injection: bool = False
    readiness: str = HELDOUT_BINDING_READINESS
    execution_authority: str = "NOT_GRANTED"
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    schema_version: int = 1

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise FactorialOnlineLineageError("online compile projection schema differs")
        for value, label, zero in (
            (self.state_binding_receipt_sha256, "state binding receipt", False),
            (self.attempt_slot_sha256, "projection attempt slot", False),
            (self.context_binding_sha256, "projection context", False),
            (self.decision_sha256, "projection decision", False),
            (self.compiled_harness_semantic_sha256, "projection Harness", False),
            (self.solution_prompt_sha256, "projection solution prompt", False),
            (self.builder_meta_prior_sha256, "projection Builder prior", True),
        ):
            _sha(value, label, zero=zero)
        if self.state_projection not in HELDOUT_PROJECTIONS:
            raise FactorialOnlineLineageError("compile state projection differs")
        if self.prior_direct_solution_injection is not False:
            raise FactorialOnlineLineageError(
                "Builder meta-prior cannot enter the solution prompt directly"
            )
        if (self.state_projection == "NONE") != (
            self.builder_meta_prior_sha256 == ZERO_SHA256
        ):
            raise FactorialOnlineLineageError("compile prior projection differs")
        if (
            self.readiness != HELDOUT_BINDING_READINESS
            or self.execution_authority != "NOT_GRANTED"
            or self.model_call_entitlement != 0
            or self.evaluator_transaction_entitlement != 0
        ):
            raise FactorialOnlineLineageError(
                "compile projection cannot upgrade readiness or entitlement"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_slot_sha256": self.attempt_slot_sha256,
            "builder_meta_prior_sha256": self.builder_meta_prior_sha256,
            "compiled_harness_semantic_sha256": (
                self.compiled_harness_semantic_sha256
            ),
            "context_binding_sha256": self.context_binding_sha256,
            "decision_sha256": self.decision_sha256,
            "evaluator_transaction_entitlement": (
                self.evaluator_transaction_entitlement
            ),
            "execution_authority": self.execution_authority,
            "model_call_entitlement": self.model_call_entitlement,
            "prior_direct_solution_injection": (
                self.prior_direct_solution_injection
            ),
            "readiness": self.readiness,
            "schema_version": self.schema_version,
            "solution_prompt_sha256": self.solution_prompt_sha256,
            "state_binding_receipt_sha256": (
                self.state_binding_receipt_sha256
            ),
            "state_projection": self.state_projection,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_sha256: str
    ) -> "OnlineHeldoutCompileProjectionReceipt":
        payload = _decode(raw, label="online compile projection")
        _fields(
            payload,
            {item.name for item in dataclass_fields(cls)},
            "online compile projection",
        )
        item = cls(**payload)
        _sha(expected_sha256, "expected online compile projection")
        if item.canonical_bytes != raw or item.sha256 != expected_sha256:
            raise FactorialOnlineLineageError(
                "online compile projection replay differs"
            )
        return item


@dataclass(frozen=True)
class FactorialOnlineLineageBundle:
    plan_sha256: str
    contract_sha256: str
    lanes: tuple[OnlineLaneBinding, ...]
    readiness: str = LINEAGE_READINESS
    execution_authority: str = "NOT_GRANTED"
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    schema_version: int = 1

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise FactorialOnlineLineageError("bundle schema differs")
        _sha(self.plan_sha256, "bundle plan")
        _sha(self.contract_sha256, "bundle contract")
        if self.readiness != LINEAGE_READINESS:
            raise FactorialOnlineLineageError("bundle readiness was upgraded")
        if self.execution_authority != "NOT_GRANTED":
            raise FactorialOnlineLineageError("bundle cannot grant execution")
        if (
            type(self.model_call_entitlement) is not int
            or type(self.evaluator_transaction_entitlement) is not int
            or self.model_call_entitlement != 0
            or self.evaluator_transaction_entitlement != 0
        ):
            raise FactorialOnlineLineageError("bundle entitlement is not zero")
        if not isinstance(self.lanes, tuple) or len(self.lanes) != 16 or any(
            type(item) is not OnlineLaneBinding for item in self.lanes
        ):
            raise FactorialOnlineLineageError("bundle must have 16 typed lanes")
        identities = tuple(
            (item.benchmark_id, item.seed, item.mechanism_id) for item in self.lanes
        )
        roots = tuple(item.trusted_relative_root for item in self.lanes)
        if len(set(identities)) != 16 or len(set(roots)) != 16:
            raise FactorialOnlineLineageError("lane identity/root isolation differs")
        if any(
            item.plan_sha256 != self.plan_sha256
            or item.contract_sha256 != self.contract_sha256
            for item in self.lanes
        ):
            raise FactorialOnlineLineageError("lane parent binding differs")

    def to_dict(self) -> dict[str, Any]:
        return {
            "contract_sha256": self.contract_sha256,
            "evaluator_transaction_entitlement": (
                self.evaluator_transaction_entitlement
            ),
            "execution_authority": self.execution_authority,
            "lanes": [item.to_dict() for item in self.lanes],
            "model_call_entitlement": self.model_call_entitlement,
            "plan_sha256": self.plan_sha256,
            "readiness": self.readiness,
            "schema_version": self.schema_version,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_verified_plan(
        cls, plan: FactorialOnlineZeroCallPlan
    ) -> "FactorialOnlineLineageBundle":
        if type(plan) is not FactorialOnlineZeroCallPlan:
            raise TypeError("typed online plan required")
        trusted = FactorialOnlineZeroCallPlan.from_canonical_bytes(
            plan.canonical_bytes, expected_sha256=plan.sha256
        )
        source_identities: list[tuple[str, int]] = []
        for slot in trusted.attempt_slots:
            identity = (slot.benchmark_id, slot.seed)
            if slot.stage == "source" and identity not in source_identities:
                source_identities.append(identity)
        if len(source_identities) != 4:
            raise FactorialOnlineLineageError("source identity coverage differs")
        lanes: list[OnlineLaneBinding] = []
        for benchmark, seed in source_identities:
            attempts = tuple(
                item
                for item in trusted.attempt_slots
                if item.stage == "source"
                and item.benchmark_id == benchmark
                and item.seed == seed
            )
            source_order: list[str] = []
            versions: dict[str, list[int]] = {}
            for item in attempts:
                if item.instance_id not in source_order:
                    source_order.append(item.instance_id)
                versions.setdefault(item.instance_id, []).append(item.version)
            if any(
                observed != list(range(1, max(observed) + 1))
                for observed in versions.values()
            ):
                raise FactorialOnlineLineageError("source attempt order differs")
            for mechanism in ONLINE_MECHANISMS:
                updates = tuple(
                    item
                    for item in trusted.update_slots
                    if item.benchmark_id == benchmark
                    and item.seed == seed
                    and item.mechanism_id == mechanism
                )
                if mechanism == "O0" and updates:
                    raise FactorialOnlineLineageError("O0 has an update")
                if mechanism != "O0" and tuple(
                    item.source_instance_id for item in updates
                ) != tuple(source_order):
                    raise FactorialOnlineLineageError("source update order differs")
                if any(
                    item.source_final_version
                    != max(versions[item.source_instance_id])
                    for item in updates
                ):
                    raise FactorialOnlineLineageError("update precedes source terminal")
                lanes.append(
                    OnlineLaneBinding(
                        plan_sha256=trusted.sha256,
                        contract_sha256=trusted.factorial_contract_sha256,
                        benchmark_id=benchmark,
                        seed=seed,
                        mechanism_id=mechanism,
                        state_kind=STATE_KINDS[mechanism],
                        source_attempt_slot_sha256s=tuple(
                            attempt_slot_sha256(item) for item in attempts
                        ),
                        source_update_slot_sha256s=tuple(
                            update_slot_sha256(item) for item in updates
                        ),
                    )
                )
        return cls(
            plan_sha256=trusted.sha256,
            contract_sha256=trusted.factorial_contract_sha256,
            lanes=tuple(lanes),
        )

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_sha256: str
    ) -> "FactorialOnlineLineageBundle":
        payload = _decode(raw, label="lineage bundle")
        _fields(
            payload,
            {
                "contract_sha256",
                "evaluator_transaction_entitlement",
                "execution_authority",
                "lanes",
                "model_call_entitlement",
                "plan_sha256",
                "readiness",
                "schema_version",
            },
            "lineage bundle",
        )
        if not isinstance(payload["lanes"], list):
            raise FactorialOnlineLineageError("lane array differs")
        item = cls(
            **{
                **dict(payload),
                "lanes": tuple(
                    OnlineLaneBinding.from_dict(value) for value in payload["lanes"]
                ),
            }
        )
        _sha(expected_sha256, "expected lineage bundle")
        trusted = cls.from_verified_plan(
            FactorialOnlineZeroCallPlan.from_verified_contract()
        )
        if (
            item.canonical_bytes != raw
            or item.sha256 != expected_sha256
            or item != trusted
            or item.sha256 != trusted.sha256
        ):
            raise FactorialOnlineLineageError("lineage bundle replay differs")
        return item

    def lane(self, benchmark: str, seed: int, mechanism: str) -> OnlineLaneBinding:
        trusted = type(self).from_verified_plan(
            FactorialOnlineZeroCallPlan.from_verified_contract()
        )
        if self != trusted or self.sha256 != trusted.sha256:
            raise FactorialOnlineLineageError("bundle is not trusted replay")
        found = tuple(
            item
            for item in self.lanes
            if (item.benchmark_id, item.seed, item.mechanism_id)
            == (benchmark, seed, mechanism)
        )
        if len(found) != 1:
            raise FactorialOnlineLineageError("lane is not exact")
        return found[0]

    def source_final_slots(
        self, lane: OnlineLaneBinding
    ) -> tuple[OnlineAttemptSlot, ...]:
        expected = self.lane(lane.benchmark_id, lane.seed, lane.mechanism_id)
        if lane != expected or lane.sha256 != expected.sha256:
            raise FactorialOnlineLineageError("lane differs from trusted plan")
        plan = FactorialOnlineZeroCallPlan.from_verified_contract()
        attempts = tuple(
            item
            for item in plan.attempt_slots
            if item.stage == "source"
            and item.benchmark_id == lane.benchmark_id
            and item.seed == lane.seed
        )
        order: list[str] = []
        versions: dict[str, list[OnlineAttemptSlot]] = {}
        for item in attempts:
            if item.instance_id not in order:
                order.append(item.instance_id)
            versions.setdefault(item.instance_id, []).append(item)
        finals = tuple(
            max(versions[instance_id], key=lambda item: item.version)
            for instance_id in order
        )
        if not finals or any(
            attempt_slot_sha256(item) not in lane.source_attempt_slot_sha256s
            for item in finals
        ):
            raise FactorialOnlineLineageError("source final attempt slots drifted")
        updates = self.update_slots(lane) if lane.mechanism_id != "O0" else ()
        if updates and tuple(item.source_instance_id for item in updates) != tuple(
            item.instance_id for item in finals
        ):
            raise FactorialOnlineLineageError("source final/update order differs")
        return finals

    def heldout_slots(
        self, lane: OnlineLaneBinding
    ) -> tuple[OnlineAttemptSlot, ...]:
        expected = self.lane(lane.benchmark_id, lane.seed, lane.mechanism_id)
        if lane != expected or lane.sha256 != expected.sha256:
            raise FactorialOnlineLineageError("lane differs from trusted plan")
        plan = FactorialOnlineZeroCallPlan.from_verified_contract()
        slots = tuple(
            item
            for item in plan.attempt_slots
            if item.stage in {"O1", "O2"}
            and item.benchmark_id == lane.benchmark_id
            and item.seed == lane.seed
            and item.mechanism_id == lane.mechanism_id
        )
        if not slots:
            raise FactorialOnlineLineageError("held-out lane is empty")
        return slots

    def heldout_target_stream_index(
        self, lane: OnlineLaneBinding, slot: OnlineAttemptSlot
    ) -> int:
        slots = self.heldout_slots(lane)
        if type(slot) is not OnlineAttemptSlot or slot not in slots:
            raise FactorialOnlineLineageError("held-out slot is outside the lane")
        order: list[str] = []
        for item in slots:
            if item.instance_id not in order:
                order.append(item.instance_id)
        return len(self.source_final_slots(lane)) + order.index(slot.instance_id)

    def update_slots(
        self, lane: OnlineLaneBinding
    ) -> tuple[OnlineMechanismUpdateSlot, ...]:
        expected = self.lane(lane.benchmark_id, lane.seed, lane.mechanism_id)
        if lane != expected or lane.sha256 != expected.sha256:
            raise FactorialOnlineLineageError("lane differs from trusted plan")
        plan = FactorialOnlineZeroCallPlan.from_verified_contract()
        slots = tuple(
            item
            for item in plan.update_slots
            if (item.benchmark_id, item.seed, item.mechanism_id)
            == (lane.benchmark_id, lane.seed, lane.mechanism_id)
        )
        if tuple(update_slot_sha256(item) for item in slots) != (
            lane.source_update_slot_sha256s
        ):
            raise FactorialOnlineLineageError("lane update slots drifted")
        return slots

    def create_update(
        self,
        *,
        lane: OnlineLaneBinding,
        slot: OnlineMechanismUpdateSlot,
        source_terminal_receipt_sha256: str,
        parent_state_sha256: str,
        parent_checkpoint_sha256: str,
        output_state_sha256: str,
        output_checkpoint_sha256: str,
        operation_record_sha256: str,
        outcome: str,
        previous: OnlineUpdateLineageReceipt | None,
    ) -> OnlineUpdateLineageReceipt:
        slots = self.update_slots(lane)
        if lane.mechanism_id == "O0":
            raise FactorialOnlineLineageError("O0 cannot have an update receipt")
        matches = tuple(index for index, item in enumerate(slots) if item == slot)
        if len(matches) != 1:
            raise FactorialOnlineLineageError("slot is outside the lane")
        ordinal = matches[0] + 1
        receipt = OnlineUpdateLineageReceipt(
            lane_binding_sha256=lane.sha256,
            ordinal=ordinal,
            update_slot_sha256=update_slot_sha256(slot),
            updater_operation_id=slot.updater_operation_id,
            source_terminal_receipt_sha256=source_terminal_receipt_sha256,
            parent_state_sha256=parent_state_sha256,
            parent_checkpoint_sha256=parent_checkpoint_sha256,
            output_state_sha256=output_state_sha256,
            output_checkpoint_sha256=output_checkpoint_sha256,
            operation_record_sha256=operation_record_sha256,
            previous_transition_sha256=(
                ZERO_SHA256 if previous is None else previous.sha256
            ),
            outcome=outcome,
        )
        return self.verify_update(receipt, previous=previous)

    def verify_update(
        self,
        receipt: OnlineUpdateLineageReceipt,
        *,
        previous: OnlineUpdateLineageReceipt | None,
    ) -> OnlineUpdateLineageReceipt:
        if type(receipt) is not OnlineUpdateLineageReceipt:
            raise TypeError("typed update receipt required")
        lanes = tuple(
            item for item in self.lanes if item.sha256 == receipt.lane_binding_sha256
        )
        if len(lanes) != 1:
            raise FactorialOnlineLineageError("transition lane is foreign")
        lane = lanes[0]
        slots = self.update_slots(lane)
        if lane.mechanism_id == "O0":
            raise FactorialOnlineLineageError("O0 cannot have an update receipt")
        if not 1 <= receipt.ordinal <= len(slots):
            raise FactorialOnlineLineageError("transition ordinal is outside lane")
        slot = slots[receipt.ordinal - 1]
        if (
            receipt.update_slot_sha256 != update_slot_sha256(slot)
            or receipt.updater_operation_id != slot.updater_operation_id
        ):
            raise FactorialOnlineLineageError("transition slot/operation differs")
        if receipt.ordinal == 1:
            if previous is not None:
                raise FactorialOnlineLineageError("first transition has a parent")
        elif (
            type(previous) is not OnlineUpdateLineageReceipt
            or previous.lane_binding_sha256 != lane.sha256
            or previous.ordinal != receipt.ordinal - 1
            or receipt.previous_transition_sha256 != previous.sha256
            or receipt.parent_state_sha256 != previous.output_state_sha256
            or receipt.parent_checkpoint_sha256
            != previous.output_checkpoint_sha256
        ):
            raise FactorialOnlineLineageError("transition parent differs")
        return receipt

    def replay_chain(
        self, receipts: tuple[OnlineUpdateLineageReceipt, ...]
    ) -> tuple[OnlineUpdateLineageReceipt, ...]:
        if not isinstance(receipts, tuple) or not receipts:
            raise FactorialOnlineLineageError("transition chain is empty/untyped")
        previous = None
        for item in receipts:
            self.verify_update(item, previous=previous)
            previous = item
        return receipts

    def create_heldout_state_binding(
        self,
        *,
        lane: OnlineLaneBinding,
        slot: OnlineAttemptSlot,
        context: HarnessContext,
        source_terminal_receipt_sha256s: tuple[str, ...],
        target_instance_descriptors: Sequence[str],
        transitions: tuple[ResolvedOnlineTransition, ...] = (),
        prior: BuilderMetaPrior | None = None,
    ) -> OnlineHeldoutStateBindingReceipt:
        """Bind one exact held-out planner context to isolated typed state.

        This is deliberately a zero-authority receipt.  In particular, source
        terminal and operation-record digests remain unresolved until the formal
        journal/provider dispatcher exists.
        """

        expected_lane = self.lane(
            lane.benchmark_id, lane.seed, lane.mechanism_id
        )
        if lane != expected_lane or lane.sha256 != expected_lane.sha256:
            raise FactorialOnlineLineageError("held-out lane is not trusted replay")
        heldout = self.heldout_slots(lane)
        if type(slot) is not OnlineAttemptSlot or slot not in heldout:
            raise FactorialOnlineLineageError("held-out slot is outside exact plan")
        if type(context) is not HarnessContext:
            raise TypeError("typed held-out Harness context required")
        target_index = self.heldout_target_stream_index(lane, slot)
        if (
            context.instance_id != slot.instance_id
            or context.suite != slot.benchmark_id
            or context.round_index != slot.version
            or context.stream_index != target_index
            or context.cross_instance_records
            or context.cross_instance_memory_grant is not None
        ):
            raise FactorialOnlineLineageError(
                "held-out Harness context differs from exact target slot"
            )
        descriptors = _public_text_tuple(
            target_instance_descriptors, "target instance descriptors"
        )
        finals = self.source_final_slots(lane)
        if not isinstance(source_terminal_receipt_sha256s, tuple) or len(
            source_terminal_receipt_sha256s
        ) != len(finals):
            raise FactorialOnlineLineageError(
                "source terminal receipt cardinality differs"
            )
        for digest in source_terminal_receipt_sha256s:
            _sha(digest, "source terminal receipt")
        if len(set(source_terminal_receipt_sha256s)) != len(
            source_terminal_receipt_sha256s
        ):
            raise FactorialOnlineLineageError("source terminal receipts repeat")

        genesis = factorial_online_genesis_state()
        state = genesis
        mechanism_state_sha256 = ZERO_SHA256
        prior_sha256 = ZERO_SHA256
        transition_sha256s: tuple[str, ...] = ()
        transition_head_sha256 = ZERO_SHA256
        if lane.mechanism_id == "O0":
            if transitions or prior is not None:
                raise FactorialOnlineLineageError("O0 forbids learned state inputs")
            if context.builder_meta_prior is not None:
                raise FactorialOnlineLineageError("O0 context contains a meta-prior")
        else:
            if type(prior) is not BuilderMetaPrior:
                raise TypeError("learned lane requires a typed Builder meta-prior")
            if not isinstance(transitions, tuple) or len(transitions) != len(finals):
                raise FactorialOnlineLineageError(
                    "learned source transition chain is incomplete"
                )
            if any(type(item) is not ResolvedOnlineTransition for item in transitions):
                raise TypeError("learned lane requires typed resolved transitions")
            chain = self.replay_chain(tuple(item.receipt for item in transitions))
            if any(
                item.lane_binding_sha256 != lane.sha256
                or item.outcome != "APPLIED"
                for item in chain
            ):
                raise FactorialOnlineLineageError(
                    "sealed learned snapshot requires every source update applied"
                )
            relevant_genesis = genesis.mechanism_state_sha256(lane.mechanism_id)
            mechanism_code = {"OM": "M", "OP": "P", "OA": "A"}[
                lane.mechanism_id
            ]
            update_slots = self.update_slots(lane)
            previous_state = genesis
            for ordinal, resolved in enumerate(transitions):
                receipt = resolved.receipt
                proposal = resolved.proposal
                expected_slot = update_slots[ordinal]
                before = resolved.before_state
                after = resolved.after_state
                if before.to_dict() != previous_state.to_dict():
                    raise FactorialOnlineLineageError(
                        "resolved transition before-state chain differs"
                    )
                if (
                    proposal.mechanism != mechanism_code
                    or proposal.parent_checkpoint_sha256
                    != before.checkpoint.sha256
                    or proposal.source_instance_id
                    != expected_slot.source_instance_id
                    or proposal.source_stream_index != ordinal
                    or proposal.target_stream_index != ordinal + 1
                    or receipt.parent_state_sha256
                    != before.mechanism_state_sha256(lane.mechanism_id)
                    or receipt.parent_checkpoint_sha256
                    != before.checkpoint.sha256
                    or receipt.output_state_sha256
                    != after.mechanism_state_sha256(lane.mechanism_id)
                    or receipt.output_checkpoint_sha256
                    != after.checkpoint.sha256
                ):
                    raise FactorialOnlineLineageError(
                        "resolved transition identity/state projection differs"
                    )
                allowed_sources = {
                    item.instance_id for item in finals[: ordinal + 1]
                }
                if any(
                    record.source_instance_id not in allowed_sources
                    for record in after.memory.records
                ) or any(
                    node.source_instance_id not in allowed_sources
                    or node.source_stream_index >= ordinal + 1
                    for node in after.harness_archive.nodes
                ):
                    raise FactorialOnlineLineageError(
                        "resolved transition contains foreign or future source state"
                    )
                try:
                    expected_after = before.checkpoint.apply_verified(
                        proposal,
                        sealed_source_instance_ids=(
                            expected_slot.source_instance_id,
                        ),
                        parent_memory=before.memory,
                        memory=after.memory,
                        parent_meta_policy=before.meta_policy,
                        meta_policy=after.meta_policy,
                        parent_harness_archive=before.harness_archive,
                        harness_archive=after.harness_archive,
                        registry=before.registry,
                    )
                except (TypeError, ValueError) as exc:
                    raise FactorialOnlineLineageError(
                        "resolved transition fails trusted typed replay"
                    ) from exc
                if expected_after != after.checkpoint:
                    raise FactorialOnlineLineageError(
                        "resolved transition checkpoint differs after replay"
                    )
                previous_state = after
            state = transitions[-1].after_state
            mechanism_state_sha256 = state.mechanism_state_sha256(
                lane.mechanism_id
            )
            if (
                chain[0].parent_state_sha256 != relevant_genesis
                or chain[0].parent_checkpoint_sha256
                != genesis.checkpoint.sha256
                or chain[-1].output_state_sha256 != mechanism_state_sha256
                or chain[-1].output_checkpoint_sha256 != state.checkpoint.sha256
                or tuple(
                    item.source_terminal_receipt_sha256 for item in chain
                )
                != source_terminal_receipt_sha256s
            ):
                raise FactorialOnlineLineageError(
                    "typed final state differs from its exact source transition chain"
                )
            if (
                state.checkpoint.next_stream_index != len(finals)
                or state.checkpoint.learned_through_instance_id
                != finals[-1].instance_id
            ):
                raise FactorialOnlineLineageError(
                    "final checkpoint stream boundary differs from frozen sources"
                )
            genesis_hashes = dict(genesis.checkpoint.mechanism_sha256s)
            final_hashes = dict(state.checkpoint.mechanism_sha256s)
            changed = {
                key
                for key in ("M", "P", "A")
                if genesis_hashes[key] != final_hashes[key]
            }
            expected_changed = {mechanism_code}
            if changed != expected_changed:
                raise FactorialOnlineLineageError(
                    "learned final state changed outside its isolated mechanism"
                )
            if lane.mechanism_id == "OM":
                expected_prior = BuilderMetaPrior.from_memory(
                    bank=state.memory,
                    checkpoint=state.checkpoint,
                    target_instance_descriptors=descriptors,
                    target_instance_id=slot.instance_id,
                    target_stream_index=target_index,
                )
            elif lane.mechanism_id == "OP":
                expected_prior = BuilderMetaPrior.from_policy(
                    policy=state.meta_policy,
                    checkpoint=state.checkpoint,
                    registry=state.registry,
                    target_instance_id=slot.instance_id,
                    target_stream_index=target_index,
                )
            else:
                expected_prior = BuilderMetaPrior.from_archive(
                    archive=state.harness_archive,
                    policy=state.meta_policy,
                    checkpoint=state.checkpoint,
                    registry=state.registry,
                    target_instance_id=slot.instance_id,
                    target_stream_index=target_index,
                )
            if prior != expected_prior or context.builder_meta_prior != expected_prior:
                raise FactorialOnlineLineageError(
                    "held-out context does not contain the rederived mechanism prior"
                )
            prior_sha256 = expected_prior.sha256
            transition_sha256s = tuple(item.sha256 for item in chain)
            transition_head_sha256 = transition_sha256s[-1]

        planner_payload = context.planner_payload()
        artifact_contract = context.public_observations.get("artifact_contract")
        if not isinstance(artifact_contract, dict):
            raise FactorialOnlineLineageError(
                "held-out context lacks its task-bound artifact capability"
            )
        dynamic_observations = {
            key: value
            for key, value in context.public_observations.items()
            if key != "artifact_contract"
        }
        immutable_task_payload = {
            "artifact_contract": artifact_contract,
            "instance_id": context.instance_id,
            "reference_artifact_id": context.reference_artifact_id,
            "reference_artifact_sha256": hashlib.sha256(
                context.reference_artifact.encode("utf-8")
            ).hexdigest(),
            "stream_index": context.stream_index,
            "suite": context.suite,
            "target_descriptors_sha256": _digest(list(descriptors)),
            "task_card_sha256": hashlib.sha256(
                context.task_card.encode("utf-8")
            ).hexdigest(),
        }
        task_local_history_payload = {
            "attempts": planner_payload["attempts"],
            "dynamic_public_observations": dynamic_observations,
            "round_index": context.round_index,
        }
        if slot.stage == "O1" and (
            context.attempts or dynamic_observations
        ):
            raise FactorialOnlineLineageError(
                "O1 cold-start context cannot contain task-local outcome history"
            )
        receipt = OnlineHeldoutStateBindingReceipt(
            plan_sha256=self.plan_sha256,
            contract_sha256=self.contract_sha256,
            lane_binding_sha256=lane.sha256,
            benchmark_id=lane.benchmark_id,
            seed=lane.seed,
            mechanism_id=lane.mechanism_id,
            state_kind=lane.state_kind,
            stage=slot.stage,
            instance_id=slot.instance_id,
            version=slot.version,
            attempt_slot_sha256=attempt_slot_sha256(slot),
            builder_operation_id=slot.builder_operation_id,
            target_stream_index=target_index,
            source_final_attempt_slot_sha256s=tuple(
                attempt_slot_sha256(item) for item in finals
            ),
            source_terminal_receipt_sha256s=source_terminal_receipt_sha256s,
            genesis_state_sha256=genesis.sha256,
            genesis_checkpoint_sha256=genesis.checkpoint.sha256,
            resolved_state_sha256=state.sha256,
            final_checkpoint_sha256=state.checkpoint.sha256,
            memory_sha256=state.memory.sha256,
            meta_policy_sha256=state.meta_policy.sha256,
            harness_archive_sha256=state.harness_archive.sha256,
            trusted_meta_registry_sha256=state.registry.sha256,
            mechanism_state_sha256=mechanism_state_sha256,
            transition_receipt_sha256s=transition_sha256s,
            transition_head_sha256=transition_head_sha256,
            builder_meta_prior_sha256=prior_sha256,
            target_descriptors_sha256=_digest(list(descriptors)),
            immutable_task_context_sha256=_digest(immutable_task_payload),
            task_local_history_sha256=_digest(task_local_history_payload),
            planner_context_sha256=_digest(planner_payload),
            context_binding_sha256=(
                TrustedOperatorRegistry.context_binding_sha256(context)
            ),
            state_projection=(
                "NONE" if lane.mechanism_id == "O0" else "BUILDER_META_PRIOR"
            ),
        )
        return receipt

    def create_compile_projection(
        self,
        *,
        binding: OnlineHeldoutStateBindingReceipt,
        lane: OnlineLaneBinding,
        slot: OnlineAttemptSlot,
        context: HarnessContext,
        source_terminal_receipt_sha256s: tuple[str, ...],
        target_instance_descriptors: Sequence[str],
        transitions: tuple[ResolvedOnlineTransition, ...] = (),
        prior: BuilderMetaPrior | None = None,
        decision: HarnessDecision,
        variant: BuilderVariant,
        operator_registry: TrustedOperatorRegistry,
        compiled: CompiledHarness | None = None,
        previous_decision: HarnessDecision | None = None,
        prior_operational_fingerprints: tuple[str, ...] = (),
    ) -> OnlineHeldoutCompileProjectionReceipt:
        if type(binding) is not OnlineHeldoutStateBindingReceipt:
            raise TypeError("typed held-out state binding required")
        if type(context) is not HarnessContext:
            raise TypeError("typed held-out Harness context required")
        if type(decision) is not HarnessDecision or type(variant) is not BuilderVariant:
            raise TypeError("typed held-out decision and Builder variant required")
        if type(operator_registry) is not TrustedOperatorRegistry:
            raise TypeError("typed trusted operator Registry required")
        trusted_binding = self.create_heldout_state_binding(
            lane=lane,
            slot=slot,
            context=context,
            source_terminal_receipt_sha256s=source_terminal_receipt_sha256s,
            target_instance_descriptors=target_instance_descriptors,
            transitions=transitions,
            prior=prior,
        )
        if binding != trusted_binding or binding.sha256 != trusted_binding.sha256:
            raise FactorialOnlineLineageError(
                "held-out state binding differs from trusted replay"
            )
        lane = self.lane(binding.benchmark_id, binding.seed, binding.mechanism_id)
        slots = tuple(
            item
            for item in self.heldout_slots(lane)
            if attempt_slot_sha256(item) == binding.attempt_slot_sha256
        )
        if (
            len(slots) != 1
            or binding.plan_sha256 != self.plan_sha256
            or binding.contract_sha256 != self.contract_sha256
            or binding.lane_binding_sha256 != lane.sha256
            or binding.context_binding_sha256
            != TrustedOperatorRegistry.context_binding_sha256(context)
        ):
            raise FactorialOnlineLineageError(
                "held-out state binding differs from exact planner context"
            )
        try:
            trusted_compiled = operator_registry.compile(
                decision,
                variant=variant,
                context=context,
                previous_decision=previous_decision,
                prior_operational_fingerprints=prior_operational_fingerprints,
            )
        except (TypeError, ValueError) as exc:
            raise FactorialOnlineLineageError(
                "held-out decision failed trusted compilation"
            ) from exc
        if compiled is not None and (
            type(compiled) is not CompiledHarness or compiled != trusted_compiled
        ):
            raise FactorialOnlineLineageError(
                "caller CompiledHarness differs from trusted recompilation"
            )
        compiled = trusted_compiled
        if (
            compiled.context_binding_sha256 != binding.context_binding_sha256
            or compiled.builder_meta_prior_sha256
            != binding.builder_meta_prior_sha256
        ):
            raise FactorialOnlineLineageError(
                "compiled Harness differs from held-out state binding"
            )
        if (
            "builder_meta_prior" in compiled.solution_prompt
            or (
                binding.builder_meta_prior_sha256 != ZERO_SHA256
                and binding.builder_meta_prior_sha256 in compiled.solution_prompt
            )
        ):
            raise FactorialOnlineLineageError(
                "Builder meta-prior leaked directly into solution prompt"
            )
        return OnlineHeldoutCompileProjectionReceipt(
            state_binding_receipt_sha256=binding.sha256,
            attempt_slot_sha256=binding.attempt_slot_sha256,
            context_binding_sha256=binding.context_binding_sha256,
            decision_sha256=compiled.decision_sha256,
            compiled_harness_semantic_sha256=(
                compiled_harness_semantic_sha256(compiled)
            ),
            solution_prompt_sha256=hashlib.sha256(
                compiled.solution_prompt.encode("utf-8")
            ).hexdigest(),
            builder_meta_prior_sha256=binding.builder_meta_prior_sha256,
            state_projection=binding.state_projection,
        )


def validate_heldout_state_binding_cohort(
    receipts: tuple[OnlineHeldoutStateBindingReceipt, ...]
) -> None:
    """Require one fair O0/OM/OP/OA cohort for the same held-out attempt."""

    if not isinstance(receipts, tuple) or len(receipts) != 4 or any(
        type(item) is not OnlineHeldoutStateBindingReceipt for item in receipts
    ):
        raise TypeError("held-out state cohort requires four typed receipts")
    by_mechanism = {item.mechanism_id: item for item in receipts}
    if set(by_mechanism) != set(ONLINE_MECHANISMS):
        raise FactorialOnlineLineageError(
            "held-out state cohort mechanism coverage differs"
        )
    bundle = FactorialOnlineLineageBundle.from_verified_plan(
        FactorialOnlineZeroCallPlan.from_verified_contract()
    )
    for mechanism, receipt in by_mechanism.items():
        lane = bundle.lane(receipt.benchmark_id, receipt.seed, mechanism)
        slots = tuple(
            slot
            for slot in bundle.heldout_slots(lane)
            if attempt_slot_sha256(slot) == receipt.attempt_slot_sha256
        )
        if len(slots) != 1:
            raise FactorialOnlineLineageError(
                "held-out cohort receipt references a foreign attempt"
            )
        slot = slots[0]
        if (
            receipt.plan_sha256 != bundle.plan_sha256
            or receipt.contract_sha256 != bundle.contract_sha256
            or receipt.lane_binding_sha256 != lane.sha256
            or receipt.benchmark_id != slot.benchmark_id
            or receipt.seed != slot.seed
            or receipt.stage != slot.stage
            or receipt.instance_id != slot.instance_id
            or receipt.version != slot.version
            or receipt.builder_operation_id != slot.builder_operation_id
            or receipt.target_stream_index
            != bundle.heldout_target_stream_index(lane, slot)
            or receipt.source_final_attempt_slot_sha256s
            != tuple(
                attempt_slot_sha256(item)
                for item in bundle.source_final_slots(lane)
            )
        ):
            raise FactorialOnlineLineageError(
                "held-out cohort receipt differs from exact plan"
            )
    reference = by_mechanism["O0"]
    common_fields = (
        "plan_sha256",
        "contract_sha256",
        "benchmark_id",
        "seed",
        "stage",
        "instance_id",
        "version",
        "target_stream_index",
        "source_final_attempt_slot_sha256s",
        "source_terminal_receipt_sha256s",
        "genesis_state_sha256",
        "genesis_checkpoint_sha256",
        "target_descriptors_sha256",
        "immutable_task_context_sha256",
        "trusted_meta_registry_sha256",
    )
    for mechanism in ONLINE_MECHANISMS[1:]:
        candidate = by_mechanism[mechanism]
        if any(
            getattr(candidate, field) != getattr(reference, field)
            for field in common_fields
        ):
            raise FactorialOnlineLineageError(
                "held-out cohort source/public-context fairness differs"
            )
    if len({item.lane_binding_sha256 for item in receipts}) != 4:
        raise FactorialOnlineLineageError("held-out cohort lane isolation differs")


__all__ = [
    "FactorialOnlineLineageBundle",
    "FactorialOnlineLineageError",
    "HELDOUT_BINDING_READINESS",
    "HELDOUT_PROJECTIONS",
    "LINEAGE_READINESS",
    "OnlineHeldoutCompileProjectionReceipt",
    "OnlineHeldoutStateBindingReceipt",
    "OnlineLaneBinding",
    "OnlineUpdateLineageReceipt",
    "ResolvedOnlineState",
    "ResolvedOnlineTransition",
    "STATE_KINDS",
    "TERMINAL_UPDATE_OUTCOMES",
    "ZERO_SHA256",
    "attempt_slot_sha256",
    "factorial_online_genesis_state",
    "update_slot_sha256",
    "validate_heldout_state_binding_cohort",
]
