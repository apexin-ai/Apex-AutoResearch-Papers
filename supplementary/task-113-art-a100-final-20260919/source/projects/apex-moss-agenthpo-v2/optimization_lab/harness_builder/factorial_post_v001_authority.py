"""Zero-call provenance authority for adaptive post-v001 factorial rounds.

This module joins a post-v001 Builder decision and an already trusted compile
receipt to the exact pinned-source task, formal plan, and scoring slot.  It has
no provider, evaluator, resource governor, callback, or execution entry point.
Consequently every object below keeps execution authority and entitlement at
zero; validating evidence here is not permission to execute a round.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import re
from typing import Any, Mapping, Sequence, TypeVar

from .compile_receipts import HarnessCompileReceipt
from .factorial_coverage import (
    AttemptCoverageRow,
    ExactFactorialAttemptMatrix,
    FactorialScoringSlot,
    TYPED_SCORE_UNBOUND,
)
from .factorial_formal_dispatch import FactorialV001FormalCompileOrchestrator
from .factorial_policies import B_FROZEN_WIDE, B_TARGETED
from .factorial_precheck import FactorialFormalZeroCallPlan
from .factorial_task_authority import (
    ExactTaskSeedAuthorityBundle,
    FactorialTaskArtifactAuthority,
)
from .factorial_trunk import TaskSeedKey, V001ArmForkReceipt, ZERO_SHA256
from .operators import HarnessContext
from .runtime import parse_harness_decision
from .schema import HarnessDecision


EXECUTION_AUTHORITY = "NOT_GRANTED"
_ARMS = {B_TARGETED, B_FROZEN_WIDE}
_POLICIES = {
    B_TARGETED: "targeted_any_change_v1",
    B_FROZEN_WIDE: "wide_all_fields_recompile_v1",
}
_AXES = (
    "role_graph",
    "memory_views",
    "tools",
    "parent_strategy",
    "workflow",
    "scheduler_mode",
    "recovery_mode",
)
_SHA = re.compile(r"[0-9a-f]{64}")
_SAFE = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_T = TypeVar("_T")


class FactorialPostV001AuthorityError(ValueError):
    """Post-v001 evidence differs from the frozen factorial experiment."""


def _canonical(payload: object) -> bytes:
    try:
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
    except (TypeError, ValueError, UnicodeError) as exc:
        raise FactorialPostV001AuthorityError("payload is not canonical JSON") from exc


def _sha(value: object, label: str, *, allow_zero: bool = False) -> str:
    if not isinstance(value, str) or _SHA.fullmatch(value) is None:
        raise FactorialPostV001AuthorityError(f"invalid {label}")
    if not allow_zero and value == ZERO_SHA256:
        raise FactorialPostV001AuthorityError(f"empty {label}")
    return value


def _safe(value: object, label: str) -> str:
    if not isinstance(value, str) or _SAFE.fullmatch(value) is None:
        raise FactorialPostV001AuthorityError(f"unsafe {label}")
    return value


def _read_canonical(raw: bytes, *, expected_sha256: str, label: str) -> dict[str, Any]:
    _sha(expected_sha256, f"expected {label} sha256")
    if not isinstance(raw, bytes) or not raw:
        raise FactorialPostV001AuthorityError(f"{label} bytes are empty")
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FactorialPostV001AuthorityError(f"{label} is not strict JSON") from exc
    if not isinstance(payload, dict) or _canonical(payload) != raw:
        raise FactorialPostV001AuthorityError(f"{label} is not canonical")
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise FactorialPostV001AuthorityError(f"{label} hash differs")
    return payload


def _planner_result(
    raw: bytes, *, slot: FactorialScoringSlot
) -> tuple[bytes, str]:
    """Parse an exact completed model-gateway result artifact."""

    artifact_sha = hashlib.sha256(raw).hexdigest() if isinstance(raw, bytes) else ""
    payload = _read_canonical(
        raw, expected_sha256=artifact_sha, label="planner operation result"
    )
    expected = {
        "schema_version",
        "operation_id",
        "cell_id",
        "operation_kind",
        "prompt_sha256",
        "model",
        "output_mode",
        "raw_response",
        "api_cost_usd",
        "provider",
        "usage",
        "audit_log_name",
    }
    if (
        set(payload) != expected
        or payload["schema_version"] != 1
        or payload["operation_id"] != slot.update_operation_id
        or payload["cell_id"] != slot.cell_id
        or payload["operation_kind"] != "planner_call"
        or payload["output_mode"] != "plain_text"
        or not isinstance(payload["raw_response"], str)
        or not payload["raw_response"].strip()
        or not isinstance(payload["usage"], dict)
        or not isinstance(payload["audit_log_name"], str)
    ):
        raise FactorialPostV001AuthorityError("planner operation result binding differs")
    _sha(payload["prompt_sha256"], "planner prompt sha256")
    for field in ("model", "provider"):
        if not isinstance(payload[field], str) or not payload[field].strip():
            raise FactorialPostV001AuthorityError("planner operation result fields differ")
    return payload["raw_response"].encode("utf-8"), artifact_sha


class _Artifact:
    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        for name in ("accepted_operational_fingerprints",):
            if name in payload:
                payload[name] = list(payload[name])
        return payload

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class PostV001PlannerDecisionReceipt(_Artifact):
    matrix_sha256: str
    slot_sha256: str
    task_seed_key_sha256: str
    arm_id: str
    version: str
    cell_id: str
    operation_id: str
    operation_record_sha256: str
    operation_result_artifact_sha256: str
    raw_response_sha256: str
    context_binding_sha256: str
    decision_sha256: str
    execution_authority: str = EXECUTION_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    schema_version: int = 1
    receipt_kind: str = "factorial_post_v001_planner_decision_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "factorial_post_v001_planner_decision_receipt_v1"
        ):
            raise FactorialPostV001AuthorityError("planner receipt schema differs")
        if self.arm_id not in _ARMS:
            raise FactorialPostV001AuthorityError("planner receipt arm differs")
        for value, label in (
            (self.matrix_sha256, "planner matrix sha256"),
            (self.slot_sha256, "planner slot sha256"),
            (self.task_seed_key_sha256, "planner task/seed sha256"),
            (self.operation_record_sha256, "planner operation record sha256"),
            (self.operation_result_artifact_sha256, "planner result artifact sha256"),
            (self.raw_response_sha256, "planner raw response sha256"),
            (self.context_binding_sha256, "planner context binding sha256"),
            (self.decision_sha256, "planner decision sha256"),
        ):
            _sha(value, label)
        for value, label in (
            (self.version, "planner version"),
            (self.cell_id, "planner cell id"),
            (self.operation_id, "planner operation id"),
        ):
            _safe(value, label)
        if self.execution_authority != EXECUTION_AUTHORITY or (
            self.model_call_entitlement != 0
            or self.evaluator_transaction_entitlement != 0
        ):
            raise FactorialPostV001AuthorityError("planner receipt grants authority")

    @classmethod
    def create(
        cls,
        *,
        matrix: ExactFactorialAttemptMatrix,
        slot: FactorialScoringSlot,
        operation_record_sha256: str,
        operation_result_artifact: bytes,
        context_binding_sha256: str,
    ) -> tuple["PostV001PlannerDecisionReceipt", HarnessDecision]:
        raw_response, result_sha256 = _planner_result(
            operation_result_artifact, slot=slot
        )
        try:
            decision = parse_harness_decision(raw_response.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as exc:
            raise FactorialPostV001AuthorityError("planner decision parsing failed") from exc
        return (
            cls(
                matrix_sha256=matrix.sha256,
                slot_sha256=slot.sha256,
                task_seed_key_sha256=slot.task_seed_key_sha256,
                arm_id=slot.arm_id,
                version=slot.version,
                cell_id=slot.cell_id,
                operation_id=slot.update_operation_id,
                operation_record_sha256=operation_record_sha256,
                operation_result_artifact_sha256=result_sha256,
                raw_response_sha256=hashlib.sha256(raw_response).hexdigest(),
                context_binding_sha256=context_binding_sha256,
                decision_sha256=decision.sha256,
            ),
            decision,
        )

    def verify(
        self,
        *,
        matrix: ExactFactorialAttemptMatrix,
        slot: FactorialScoringSlot,
        operation_result_artifact: bytes,
    ) -> HarnessDecision:
        expected, decision = type(self).create(
            matrix=matrix,
            slot=slot,
            operation_record_sha256=self.operation_record_sha256,
            operation_result_artifact=operation_result_artifact,
            context_binding_sha256=self.context_binding_sha256,
        )
        if expected != self or expected.canonical_bytes != self.canonical_bytes:
            raise FactorialPostV001AuthorityError("planner decision receipt replay differs")
        return decision

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_sha256: str
    ) -> "PostV001PlannerDecisionReceipt":
        payload = _read_canonical(
            raw, expected_sha256=expected_sha256, label="planner decision receipt"
        )
        try:
            item = cls(**payload)
        except TypeError as exc:
            raise FactorialPostV001AuthorityError("planner receipt fields differ") from exc
        if item.canonical_bytes != raw:
            raise FactorialPostV001AuthorityError("planner receipt replay differs")
        return item


@dataclass(frozen=True)
class PostV001TransitionIntent(_Artifact):
    factorial_plan_sha256: str
    task_authority_bundle_sha256: str
    matrix_sha256: str
    slot_sha256: str
    task_seed_key_sha256: str
    task_binding_sha256: str
    benchmark_id: str
    instance_id: str
    seed: int
    arm_id: str
    version: str
    cell_id: str
    previous_physical_terminal_sha256: str
    previous_accepted_compile_receipt_sha256: str
    previous_accepted_decision_sha256: str
    accepted_operational_fingerprints: tuple[str, ...]
    planner_decision_receipt_sha256: str
    context_binding_sha256: str
    decision_sha256: str
    execution_authority: str = EXECUTION_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    schema_version: int = 1
    intent_kind: str = "factorial_post_v001_transition_intent_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.intent_kind != (
            "factorial_post_v001_transition_intent_v1"
        ):
            raise FactorialPostV001AuthorityError("transition intent schema differs")
        if self.arm_id not in _ARMS:
            raise FactorialPostV001AuthorityError("transition intent arm differs")
        for value, label in (
            (self.factorial_plan_sha256, "intent plan sha256"),
            (self.task_authority_bundle_sha256, "intent authority sha256"),
            (self.matrix_sha256, "intent matrix sha256"),
            (self.slot_sha256, "intent slot sha256"),
            (self.task_seed_key_sha256, "intent task/seed sha256"),
            (self.task_binding_sha256, "intent task binding sha256"),
            (self.previous_physical_terminal_sha256, "previous physical terminal sha256"),
            (self.previous_accepted_compile_receipt_sha256, "previous compile sha256"),
            (self.previous_accepted_decision_sha256, "previous decision sha256"),
            (self.planner_decision_receipt_sha256, "planner receipt sha256"),
            (self.context_binding_sha256, "intent context binding sha256"),
            (self.decision_sha256, "intent decision sha256"),
        ):
            _sha(value, label)
        for value, label in (
            (self.benchmark_id, "intent benchmark"),
            (self.instance_id, "intent instance"),
            (self.version, "intent version"),
            (self.cell_id, "intent cell"),
        ):
            _safe(value, label)
        if type(self.seed) is not int or self.seed < 0:
            raise FactorialPostV001AuthorityError("intent seed differs")
        if not isinstance(self.accepted_operational_fingerprints, tuple) or not (
            self.accepted_operational_fingerprints
        ):
            raise FactorialPostV001AuthorityError("accepted lineage is empty")
        if len(set(self.accepted_operational_fingerprints)) != len(
            self.accepted_operational_fingerprints
        ):
            raise FactorialPostV001AuthorityError("accepted lineage repeats a fingerprint")
        for value in self.accepted_operational_fingerprints:
            _sha(value, "accepted operational fingerprint")
        if self.execution_authority != EXECUTION_AUTHORITY or (
            self.model_call_entitlement != 0
            or self.evaluator_transaction_entitlement != 0
        ):
            raise FactorialPostV001AuthorityError("transition intent grants authority")

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_sha256: str
    ) -> "PostV001TransitionIntent":
        payload = _read_canonical(raw, expected_sha256=expected_sha256, label="intent")
        payload["accepted_operational_fingerprints"] = tuple(
            payload.get("accepted_operational_fingerprints", ())
        )
        try:
            item = cls(**payload)
        except TypeError as exc:
            raise FactorialPostV001AuthorityError("intent fields differ") from exc
        if item.canonical_bytes != raw:
            raise FactorialPostV001AuthorityError("intent replay differs")
        return item


@dataclass(frozen=True)
class PostV001CompileValidationReceipt(_Artifact):
    transition_intent_sha256: str
    matrix_sha256: str
    slot_sha256: str
    compile_receipt_sha256: str
    decision_sha256: str
    operational_fingerprint: str
    lineage_prefix_sha256: str
    validation_status: str = "SUPPLIED_TRUSTED_COMPILE_RECEIPT_VALIDATED"
    execution_authority: str = EXECUTION_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    schema_version: int = 1
    receipt_kind: str = "factorial_post_v001_compile_validation_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "factorial_post_v001_compile_validation_receipt_v1"
        ):
            raise FactorialPostV001AuthorityError("compile validation schema differs")
        for value, label in (
            (self.transition_intent_sha256, "compile intent sha256"),
            (self.matrix_sha256, "compile matrix sha256"),
            (self.slot_sha256, "compile slot sha256"),
            (self.compile_receipt_sha256, "compile receipt sha256"),
            (self.decision_sha256, "compile decision sha256"),
            (self.operational_fingerprint, "compile fingerprint"),
            (self.lineage_prefix_sha256, "compile lineage prefix sha256"),
        ):
            _sha(value, label)
        if self.validation_status != "SUPPLIED_TRUSTED_COMPILE_RECEIPT_VALIDATED":
            raise FactorialPostV001AuthorityError("compile validation status differs")
        if self.execution_authority != EXECUTION_AUTHORITY or (
            self.model_call_entitlement != 0
            or self.evaluator_transaction_entitlement != 0
        ):
            raise FactorialPostV001AuthorityError("compile validation grants authority")

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_sha256: str
    ) -> "PostV001CompileValidationReceipt":
        payload = _read_canonical(
            raw, expected_sha256=expected_sha256, label="compile validation receipt"
        )
        try:
            item = cls(**payload)
        except TypeError as exc:
            raise FactorialPostV001AuthorityError(
                "compile validation fields differ"
            ) from exc
        if item.canonical_bytes != raw:
            raise FactorialPostV001AuthorityError("compile validation replay differs")
        return item


@dataclass(frozen=True)
class PostV001RoundTerminalReceipt(_Artifact):
    matrix_sha256: str
    slot_sha256: str
    task_seed_key_sha256: str
    arm_id: str
    version: str
    cell_id: str
    previous_physical_terminal_sha256: str
    transition_intent_sha256: str
    compile_validation_receipt_sha256: str
    attempt_coverage_row_sha256: str
    terminal_status: str
    lineage_head_compile_receipt_sha256: str
    lineage_head_decision_sha256: str
    accepted_operational_fingerprints: tuple[str, ...]
    reason_code: str
    execution_authority: str = EXECUTION_AUTHORITY
    schema_version: int = 1
    receipt_kind: str = "factorial_post_v001_round_terminal_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "factorial_post_v001_round_terminal_receipt_v1"
        ):
            raise FactorialPostV001AuthorityError("terminal receipt schema differs")
        if self.arm_id not in _ARMS or self.terminal_status not in {
            "ACCEPTED_HARNESS",
            "REJECTED_HARNESS",
        }:
            raise FactorialPostV001AuthorityError("terminal receipt state differs")
        for value, label in (
            (self.matrix_sha256, "terminal matrix sha256"),
            (self.slot_sha256, "terminal slot sha256"),
            (self.task_seed_key_sha256, "terminal task/seed sha256"),
            (self.previous_physical_terminal_sha256, "terminal previous physical sha256"),
            (self.transition_intent_sha256, "terminal intent sha256"),
            (self.attempt_coverage_row_sha256, "terminal coverage row sha256"),
            (self.lineage_head_compile_receipt_sha256, "terminal compile head"),
            (self.lineage_head_decision_sha256, "terminal decision head"),
        ):
            _sha(value, label)
        _sha(
            self.compile_validation_receipt_sha256,
            "terminal compile validation sha256",
            allow_zero=self.terminal_status == "REJECTED_HARNESS",
        )
        for value, label in (
            (self.version, "terminal version"),
            (self.cell_id, "terminal cell"),
            (self.reason_code, "terminal reason"),
        ):
            _safe(value, label)
        if not isinstance(self.accepted_operational_fingerprints, tuple) or not (
            self.accepted_operational_fingerprints
        ):
            raise FactorialPostV001AuthorityError("terminal lineage is empty")
        if len(set(self.accepted_operational_fingerprints)) != len(
            self.accepted_operational_fingerprints
        ):
            raise FactorialPostV001AuthorityError("terminal lineage repeats")
        for value in self.accepted_operational_fingerprints:
            _sha(value, "terminal fingerprint")
        if self.terminal_status == "ACCEPTED_HARNESS":
            if (
                self.compile_validation_receipt_sha256 == ZERO_SHA256
                or self.reason_code != "NONE"
            ):
                raise FactorialPostV001AuthorityError(
                    "accepted terminal compile/reason binding differs"
                )
        elif (
            self.compile_validation_receipt_sha256 != ZERO_SHA256
            or self.reason_code == "NONE"
        ):
            raise FactorialPostV001AuthorityError(
                "rejected terminal compile/reason binding differs"
            )
        if self.execution_authority != EXECUTION_AUTHORITY:
            raise FactorialPostV001AuthorityError("terminal receipt grants authority")

    @staticmethod
    def _verify_coverage_row(
        *,
        intent: PostV001TransitionIntent,
        slot: FactorialScoringSlot,
        coverage_row: AttemptCoverageRow,
        rejected_reason_code: str | None,
    ) -> None:
        if type(slot) is not FactorialScoringSlot or type(
            coverage_row
        ) is not AttemptCoverageRow:
            raise TypeError("exact slot and typed attempt coverage row are required")
        if (
            slot.sha256 != intent.slot_sha256
            or slot.task_seed_key_sha256 != intent.task_seed_key_sha256
            or slot.arm_id != intent.arm_id
            or slot.version != intent.version
            or slot.cell_id != intent.cell_id
        ):
            raise FactorialPostV001AuthorityError(
                "terminal coverage slot differs from intent"
            )
        try:
            coverage_row.verify_against_slot(
                matrix_sha256=intent.matrix_sha256, slot=slot
            )
        except (TypeError, ValueError) as exc:
            raise FactorialPostV001AuthorityError(
                "terminal coverage row binding differs"
            ) from exc
        if coverage_row.coverage_state != TYPED_SCORE_UNBOUND:
            raise FactorialPostV001AuthorityError(
                "terminal requires a typed ITT score row"
            )
        if rejected_reason_code is not None and (
            coverage_row.valid is not False
            or coverage_row.floor_imputed is not True
            or coverage_row.invalid_reason != rejected_reason_code
        ):
            raise FactorialPostV001AuthorityError(
                "rejected terminal requires its exact ITT-floor reason"
            )

    @classmethod
    def accepted(
        cls,
        *,
        intent: PostV001TransitionIntent,
        validation: PostV001CompileValidationReceipt,
        compile_receipt: HarnessCompileReceipt,
        slot: FactorialScoringSlot,
        coverage_row: AttemptCoverageRow,
    ) -> "PostV001RoundTerminalReceipt":
        if (
            type(validation) is not PostV001CompileValidationReceipt
            or type(compile_receipt) is not HarnessCompileReceipt
            or validation.transition_intent_sha256 != intent.sha256
            or validation.matrix_sha256 != intent.matrix_sha256
            or validation.slot_sha256 != intent.slot_sha256
            or validation.compile_receipt_sha256 != compile_receipt.sha256
            or validation.decision_sha256 != compile_receipt.decision_sha256
        ):
            raise FactorialPostV001AuthorityError("terminal compile binding differs")
        cls._verify_coverage_row(
            intent=intent,
            slot=slot,
            coverage_row=coverage_row,
            rejected_reason_code=None,
        )
        return cls(
            matrix_sha256=intent.matrix_sha256,
            slot_sha256=intent.slot_sha256,
            task_seed_key_sha256=intent.task_seed_key_sha256,
            arm_id=intent.arm_id,
            version=intent.version,
            cell_id=intent.cell_id,
            previous_physical_terminal_sha256=intent.previous_physical_terminal_sha256,
            transition_intent_sha256=intent.sha256,
            compile_validation_receipt_sha256=validation.sha256,
            attempt_coverage_row_sha256=coverage_row.sha256,
            terminal_status="ACCEPTED_HARNESS",
            lineage_head_compile_receipt_sha256=compile_receipt.sha256,
            lineage_head_decision_sha256=compile_receipt.decision_sha256,
            accepted_operational_fingerprints=tuple(
                compile_receipt.lineage_operational_fingerprints
            ),
            reason_code="NONE",
        )

    @classmethod
    def rejected(
        cls,
        *,
        intent: PostV001TransitionIntent,
        slot: FactorialScoringSlot,
        coverage_row: AttemptCoverageRow,
        reason_code: str,
    ) -> "PostV001RoundTerminalReceipt":
        """Seal one failed Harness transition without advancing its lineage.

        The supplied score row must already be the typed benchmark-native ITT
        floor for the same exact slot and reason.  No compile, solution, or
        evaluator authority is created here.
        """

        _safe(reason_code, "rejected terminal reason")
        if reason_code == "NONE":
            raise FactorialPostV001AuthorityError(
                "rejected terminal lacks a failure reason"
            )
        cls._verify_coverage_row(
            intent=intent,
            slot=slot,
            coverage_row=coverage_row,
            rejected_reason_code=reason_code,
        )
        return cls(
            matrix_sha256=intent.matrix_sha256,
            slot_sha256=intent.slot_sha256,
            task_seed_key_sha256=intent.task_seed_key_sha256,
            arm_id=intent.arm_id,
            version=intent.version,
            cell_id=intent.cell_id,
            previous_physical_terminal_sha256=(
                intent.previous_physical_terminal_sha256
            ),
            transition_intent_sha256=intent.sha256,
            compile_validation_receipt_sha256=ZERO_SHA256,
            attempt_coverage_row_sha256=coverage_row.sha256,
            terminal_status="REJECTED_HARNESS",
            lineage_head_compile_receipt_sha256=(
                intent.previous_accepted_compile_receipt_sha256
            ),
            lineage_head_decision_sha256=intent.previous_accepted_decision_sha256,
            accepted_operational_fingerprints=(
                intent.accepted_operational_fingerprints
            ),
            reason_code=reason_code,
        )

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_sha256: str
    ) -> "PostV001RoundTerminalReceipt":
        payload = _read_canonical(raw, expected_sha256=expected_sha256, label="terminal")
        payload["accepted_operational_fingerprints"] = tuple(
            payload.get("accepted_operational_fingerprints", ())
        )
        try:
            item = cls(**payload)
        except TypeError as exc:
            raise FactorialPostV001AuthorityError("terminal fields differ") from exc
        if item.canonical_bytes != raw:
            raise FactorialPostV001AuthorityError("terminal replay differs")
        return item


class FactorialPostV001Authority:
    """Replays exact sources and validates one adaptive post-v001 transition."""

    def __init__(
        self,
        *,
        task_authority: FactorialTaskArtifactAuthority,
        task_authority_bundle: ExactTaskSeedAuthorityBundle,
        plan: FactorialFormalZeroCallPlan,
    ) -> None:
        if type(task_authority) is not FactorialTaskArtifactAuthority:
            raise FactorialPostV001AuthorityError("pinned task authority is required")
        self.task_authority = task_authority
        self.bundle = task_authority.verify_exact_bundle(task_authority_bundle)
        self.plan = FactorialFormalZeroCallPlan.from_bytes(
            plan.canonical_bytes,
            task_authority=task_authority,
            task_authority_bundle=self.bundle,
            expected_sha256=plan.sha256,
        )
        self.matrix = ExactFactorialAttemptMatrix.from_verified_sources(
            plan=self.plan, bundle=self.bundle, task_authority=task_authority
        )
        self._compiler = FactorialV001FormalCompileOrchestrator(
            task_authority=task_authority,
            task_authority_bundle=self.bundle,
            plan=self.plan,
        )

    def _replay(self) -> tuple[ExactTaskSeedAuthorityBundle, ExactFactorialAttemptMatrix]:
        bundle = self.task_authority.verify_exact_bundle(self.bundle)
        plan = FactorialFormalZeroCallPlan.from_bytes(
            self.plan.canonical_bytes,
            task_authority=self.task_authority,
            task_authority_bundle=bundle,
            expected_sha256=self.plan.sha256,
        )
        matrix = ExactFactorialAttemptMatrix.from_verified_sources(
            plan=plan, bundle=bundle, task_authority=self.task_authority
        )
        if bundle != self.bundle or plan != self.plan or matrix != self.matrix:
            raise FactorialPostV001AuthorityError("source/plan/matrix replay differs")
        return bundle, matrix

    @staticmethod
    def _canonical_decision(decision: HarnessDecision) -> HarnessDecision:
        if type(decision) is not HarnessDecision:
            raise FactorialPostV001AuthorityError("exact decision is required")
        canonical = HarnessDecision.from_dict(asdict(decision))
        if canonical != decision:
            raise FactorialPostV001AuthorityError("decision canonicalization differs")
        return canonical

    def _slot(
        self, matrix: ExactFactorialAttemptMatrix, *, key: TaskSeedKey, arm_id: str, version: str
    ) -> FactorialScoringSlot:
        if arm_id not in _ARMS or type(key) is not TaskSeedKey:
            raise FactorialPostV001AuthorityError("adaptive key or arm differs")
        candidates = tuple(
            slot
            for slot in matrix.slots
            if slot.task_seed_key_sha256 == key.sha256
            and slot.arm_id == arm_id
            and slot.version == version
            and not slot.shared_v001
        )
        if len(candidates) != 1:
            raise FactorialPostV001AuthorityError(
                "version is outside the exact formal AgentHPO v006/GDPevo v003 slots"
            )
        return candidates[0]

    def create_intent(
        self,
        *,
        key: TaskSeedKey,
        arm_id: str,
        version: str,
        planner_receipt: PostV001PlannerDecisionReceipt,
        planner_operation_result_artifact: bytes,
        v001_fork: V001ArmForkReceipt | None,
        previous_terminal: PostV001RoundTerminalReceipt | None,
        prior_compile_receipts: Sequence[HarnessCompileReceipt],
        prior_decisions: Sequence[HarnessDecision],
    ) -> tuple[PostV001TransitionIntent, HarnessDecision]:
        bundle, matrix = self._replay()
        verified_key = next(
            (item for item in bundle.task_seed_keys if item.sha256 == key.sha256), None
        )
        if verified_key != key:
            raise FactorialPostV001AuthorityError("key is outside source authority")
        slot = self._slot(matrix, key=key, arm_id=arm_id, version=version)
        decision = planner_receipt.verify(
            matrix=matrix,
            slot=slot,
            operation_result_artifact=planner_operation_result_artifact,
        )
        receipts = tuple(prior_compile_receipts)
        decisions = tuple(self._canonical_decision(item) for item in prior_decisions)
        if not receipts or len(receipts) != len(decisions):
            raise FactorialPostV001AuthorityError("accepted compile lineage differs")
        policy = _POLICIES[arm_id]
        accepted_versions: list[int] = []
        for index, (receipt, prior_decision) in enumerate(
            zip(receipts, decisions, strict=True)
        ):
            receipt_version = int(receipt.version[1:])
            accepted_versions.append(receipt_version)
            expected_lineage = (
                tuple(
                    item.operational_fingerprint
                    for item in decisions[: index + 1]
                )
                if arm_id == B_FROZEN_WIDE
                else (prior_decision.operational_fingerprint,)
            )
            if (
                type(receipt) is not HarnessCompileReceipt
                or receipt.cell_id != slot.cell_id
                or receipt.suite != key.suite
                or receipt.instance_id != key.instance_id
                or receipt.variant_id != arm_id
                or receipt.adaptation_policy != policy
                or receipt.decision_sha256 != prior_decision.sha256
                or receipt.operational_fingerprint
                != prior_decision.operational_fingerprint
                or receipt.lineage_operational_fingerprints != expected_lineage
                or (
                    index > 0
                    and (
                        receipt.previous_receipt_sha256
                        != receipts[index - 1].sha256
                        or receipt.previous_decision_sha256
                        != decisions[index - 1].sha256
                    )
                )
            ):
                raise FactorialPostV001AuthorityError("accepted compile lineage binding differs")
        current_index = int(version[1:])
        if (
            accepted_versions[0] != 1
            or accepted_versions != sorted(set(accepted_versions))
            or any(item >= current_index for item in accepted_versions)
        ):
            raise FactorialPostV001AuthorityError(
                "accepted lineage versions are not a strict physical-round prefix"
            )
        fingerprints = (
            tuple(item.operational_fingerprint for item in decisions)
            if arm_id == B_FROZEN_WIDE
            else (decisions[-1].operational_fingerprint,)
        )
        if arm_id == B_FROZEN_WIDE and len(set(fingerprints)) != len(fingerprints):
            raise FactorialPostV001AuthorityError("accepted lineage repeats a fingerprint")
        if current_index == 2:
            if previous_terminal is not None or v001_fork is None:
                raise FactorialPostV001AuthorityError("v002 requires exactly its v001 fork")
            if (
                v001_fork.arm_variant_sha256
                != dict(self.plan.arm_variant_sha256s)[arm_id]
                or v001_fork.arm_contract_sha256
                != self.plan.factorial_contract_sha256
                or v001_fork.task_seed_key_sha256 != key.sha256
                or v001_fork.arm_id != arm_id
                or v001_fork.arm_cell_id != slot.cell_id
                or v001_fork.arm_compile_receipt_sha256 != receipts[-1].sha256
                or v001_fork.shared_decision_sha256 != decisions[-1].sha256
                or v001_fork.shared_operational_fingerprint
                != decisions[-1].operational_fingerprint
            ):
                raise FactorialPostV001AuthorityError("v001 fork lineage binding differs")
            previous_physical_sha = v001_fork.sha256
        else:
            if v001_fork is not None or previous_terminal is None:
                raise FactorialPostV001AuthorityError("post-v002 requires its prior terminal")
            expected_previous = f"v{current_index - 1:03d}"
            if (
                previous_terminal.matrix_sha256 != matrix.sha256
                or previous_terminal.task_seed_key_sha256 != key.sha256
                or previous_terminal.arm_id != arm_id
                or previous_terminal.version != expected_previous
                or previous_terminal.cell_id != slot.cell_id
                or previous_terminal.lineage_head_compile_receipt_sha256
                != receipts[-1].sha256
                or previous_terminal.lineage_head_decision_sha256
                != decisions[-1].sha256
                or previous_terminal.accepted_operational_fingerprints != fingerprints
            ):
                raise FactorialPostV001AuthorityError("adjacent terminal lineage differs")
            previous_physical_sha = previous_terminal.sha256
        return (
            PostV001TransitionIntent(
                factorial_plan_sha256=self.plan.sha256,
                task_authority_bundle_sha256=bundle.sha256,
                matrix_sha256=matrix.sha256,
                slot_sha256=slot.sha256,
                task_seed_key_sha256=key.sha256,
                task_binding_sha256=key.task_binding_sha256,
                benchmark_id=key.suite,
                instance_id=key.instance_id,
                seed=key.seed,
                arm_id=arm_id,
                version=version,
                cell_id=slot.cell_id,
                previous_physical_terminal_sha256=previous_physical_sha,
                previous_accepted_compile_receipt_sha256=receipts[-1].sha256,
                previous_accepted_decision_sha256=decisions[-1].sha256,
                accepted_operational_fingerprints=fingerprints,
                planner_decision_receipt_sha256=planner_receipt.sha256,
                context_binding_sha256=planner_receipt.context_binding_sha256,
                decision_sha256=decision.sha256,
            ),
            decision,
        )

    def validate_compile(
        self,
        *,
        intent: PostV001TransitionIntent,
        decision: HarnessDecision,
        compile_receipt: HarnessCompileReceipt,
        prior_compile_receipts: Sequence[HarnessCompileReceipt],
        prior_decisions: Sequence[HarnessDecision],
        context: HarnessContext,
    ) -> PostV001CompileValidationReceipt:
        bundle, matrix = self._replay()
        decision = self._canonical_decision(decision)
        slot = next((item for item in matrix.slots if item.sha256 == intent.slot_sha256), None)
        key = next(
            (
                item
                for item in bundle.task_seed_keys
                if item.sha256 == intent.task_seed_key_sha256
            ),
            None,
        )
        if slot is None or any(
            (
                intent.factorial_plan_sha256 != self.plan.sha256,
                intent.task_authority_bundle_sha256 != bundle.sha256,
                intent.matrix_sha256 != matrix.sha256,
                intent.task_seed_key_sha256 != slot.task_seed_key_sha256,
                key is None,
                intent.task_binding_sha256
                != (ZERO_SHA256 if key is None else key.task_binding_sha256),
                intent.benchmark_id != slot.benchmark_id,
                intent.instance_id != slot.instance_id,
                intent.seed != slot.seed,
                intent.arm_id != slot.arm_id,
                intent.version != slot.version,
                intent.cell_id != slot.cell_id,
                intent.decision_sha256 != decision.sha256,
            )
        ):
            raise FactorialPostV001AuthorityError("compile intent exact-slot binding differs")
        receipts = tuple(prior_compile_receipts)
        decisions = tuple(self._canonical_decision(item) for item in prior_decisions)
        if not receipts or len(receipts) != len(decisions):
            raise FactorialPostV001AuthorityError("compile prior lineage differs")
        parent_receipt, parent_decision = receipts[-1], decisions[-1]
        policy = _POLICIES[intent.arm_id]
        if (
            type(compile_receipt) is not HarnessCompileReceipt
            or compile_receipt.cell_id != intent.cell_id
            or compile_receipt.suite != intent.benchmark_id
            or compile_receipt.instance_id != intent.instance_id
            or compile_receipt.variant_id != intent.arm_id
            or compile_receipt.version != intent.version
            or compile_receipt.adaptation_policy != policy
            or compile_receipt.context_binding_sha256 != intent.context_binding_sha256
            or compile_receipt.previous_receipt_sha256 != parent_receipt.sha256
            or compile_receipt.previous_decision_sha256 != parent_decision.sha256
            or compile_receipt.decision_sha256 != decision.sha256
            or compile_receipt.operational_fingerprint != decision.operational_fingerprint
            or compile_receipt.change_map
            != decision.operational_change_map_from(parent_decision)
        ):
            raise FactorialPostV001AuthorityError("trusted compile receipt binding differs")
        expected_fingerprints = (*intent.accepted_operational_fingerprints, decision.operational_fingerprint)
        if intent.arm_id == B_FROZEN_WIDE:
            if (
                not all(compile_receipt.change_map.get(axis) is True for axis in _AXES)
                or tuple(compile_receipt.lineage_operational_fingerprints)
                != expected_fingerprints
                or len(set(expected_fingerprints)) != len(expected_fingerprints)
            ):
                raise FactorialPostV001AuthorityError("wide compile seven-axis lineage differs")
            unchanged = [
                axis
                for axis in _AXES
                if compile_receipt.axis_configuration_sha256s[axis]
                == parent_receipt.axis_configuration_sha256s[axis]
            ]
            if unchanged:
                raise FactorialPostV001AuthorityError(
                    "wide compile axis configuration is unchanged: " + ",".join(unchanged)
                )
        else:
            if not any(compile_receipt.change_map.values()):
                raise FactorialPostV001AuthorityError("targeted compile has no material change")

        if type(context) is not HarnessContext:
            raise TypeError("exact post-v001 Harness context is required")
        source_context = self.task_authority.derived_contexts().get(
            (intent.benchmark_id, intent.instance_id)
        )
        if source_context is None:
            raise FactorialPostV001AuthorityError(
                "post-v001 context task is outside source authority"
            )
        expected_public_task = (
            source_context.instance_id,
            source_context.suite,
            source_context.task_card,
            source_context.reference_artifact_id,
            source_context.reference_artifact,
            source_context.public_observations,
        )
        actual_public_task = (
            context.instance_id,
            context.suite,
            context.task_card,
            context.reference_artifact_id,
            context.reference_artifact,
            context.public_observations,
        )
        if (
            actual_public_task != expected_public_task
            or context.round_index != int(intent.version[1:])
            or context.cross_instance_records
            or context.cross_instance_memory_grant is not None
            or context.stream_index is not None
            or context.builder_meta_prior is not None
            or len(context.attempts) != int(intent.version[1:]) - 1
            or tuple(item.attempt_id for item in context.attempts)
            != tuple(f"v{index:03d}" for index in range(1, int(intent.version[1:])))
            or context.accepted_harness_count != len(receipts)
        ):
            raise FactorialPostV001AuthorityError(
                "post-v001 trusted compile context differs"
            )
        trusted_registry = self._compiler.operator_registry
        trusted_variant = self._compiler.variants[intent.arm_id]
        try:
            compiled = trusted_registry.compile(
                decision,
                variant=trusted_variant,
                context=context,
                previous_decision=parent_decision,
                prior_operational_fingerprints=(
                    intent.accepted_operational_fingerprints
                ),
            )
            trusted_receipt = HarnessCompileReceipt.create(
                cell_id=intent.cell_id,
                suite=intent.benchmark_id,
                instance_id=intent.instance_id,
                variant_id=intent.arm_id,
                version=intent.version,
                adaptation_policy=policy,
                previous_receipt_sha256=parent_receipt.sha256,
                previous_decision_sha256=parent_decision.sha256,
                compiled=compiled,
                decision=decision,
                previous_decision=parent_decision,
                prior_operational_fingerprints=(
                    intent.accepted_operational_fingerprints
                ),
            )
        except (TypeError, ValueError) as exc:
            raise FactorialPostV001AuthorityError(
                "trusted Registry post-v001 compilation failed"
            ) from exc
        if trusted_receipt != compile_receipt or (
            trusted_receipt.canonical_bytes != compile_receipt.canonical_bytes
        ):
            raise FactorialPostV001AuthorityError(
                "supplied compile receipt differs from trusted recompilation"
            )
        prior_nonces = {
            item["instance_nonce_sha256"]
            for receipt in receipts
            for item in receipt.component_instances
        }
        prior_configs = {
            item["config_sha256"]
            for receipt in receipts
            for item in receipt.component_instances
        }
        if any(
            item["instance_nonce_sha256"] in prior_nonces
            or item["config_sha256"] in prior_configs
            for item in compile_receipt.component_instances
        ):
            raise FactorialPostV001AuthorityError("compile component instance was reused")
        return PostV001CompileValidationReceipt(
            transition_intent_sha256=intent.sha256,
            matrix_sha256=matrix.sha256,
            slot_sha256=slot.sha256,
            compile_receipt_sha256=compile_receipt.sha256,
            decision_sha256=decision.sha256,
            operational_fingerprint=decision.operational_fingerprint,
            lineage_prefix_sha256=compile_receipt.lineage_prefix_sha256,
        )


__all__ = [
    "FactorialPostV001Authority",
    "FactorialPostV001AuthorityError",
    "PostV001CompileValidationReceipt",
    "PostV001PlannerDecisionReceipt",
    "PostV001RoundTerminalReceipt",
    "PostV001TransitionIntent",
]
