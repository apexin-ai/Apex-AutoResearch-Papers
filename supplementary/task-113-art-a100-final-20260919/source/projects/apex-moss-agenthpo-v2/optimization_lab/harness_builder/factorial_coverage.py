"""Zero-call exact attempt and coverage foundation for the factorial study.

The objects in this module enumerate the complete scoring population from the
pinned-source task authority and the exact formal zero-call plan.  They do not
own a provider, evaluator, resource governor, or execution entitlement.

The coverage seal deliberately remains ``NOT_READY``: typed score artifacts can
be checked here, but the sole transport, evaluator dispatch, reservation ledger,
and report writer are not yet connected end to end.  In particular, an exact
slot set is not represented as proof that any slot was actually executed.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping, Sequence

from .events import (
    JournalReplay,
    OperationRecord,
    ResourceVector,
    verify_operation_journal,
)
from .factorial_itt import (
    FactorialITTPolicy,
    FactorialITTScore,
    VerifiedITTReportRow,
)
from .factorial_policies import ARM_IDS, ARM_POLICY_SPECS, A_FIXED_FEEDBACK
from .factorial_precheck import FactorialFormalZeroCallPlan
from .factorial_score import (
    EvaluationScoreObservation,
    EvaluationScoreReceipt,
    ScoreContractError,
    score_contract_for,
)
from .factorial_task_authority import (
    ExactTaskSeedAuthorityBundle,
    FactorialTaskArtifactAuthority,
)


ZERO_SHA256 = "0" * 64
SHARED_V001_ARM_ID = "SHARED_V001"
EXECUTION_AUTHORITY = "NOT_GRANTED"
FORMAL_DISPATCH_STATUS = (
    "EXACT_SLOT_SET_READY_OPERATION_LEDGER_PROVIDER_EVALUATOR_"
    "AND_REPORT_DISPATCH_NOT_READY"
)
UNEXECUTED = "UNEXECUTED_NOT_AUTHORIZED"
TYPED_SCORE_UNBOUND = "TYPED_SCORE_CHAIN_OPERATION_LEDGER_NOT_BOUND"

_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_VERSION = re.compile(r"v([0-9]{3})")
_COVERAGE_STATES = {UNEXECUTED, TYPED_SCORE_UNBOUND}


class FactorialCoverageError(ValueError):
    """An exact attempt, native result, or coverage proof differs."""


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
        raise FactorialCoverageError("coverage payload is not canonical JSON") from exc


def _sha(value: object, label: str, *, allow_zero: bool = False) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise FactorialCoverageError(f"invalid {label}")
    if not allow_zero and value == ZERO_SHA256:
        raise FactorialCoverageError(f"empty {label}")
    return value


def _safe(value: object, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise FactorialCoverageError(f"unsafe {label}")
    return value


def _finite(value: object, label: str) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
    ):
        raise FactorialCoverageError(f"{label} must be finite")
    normalized = float(value)
    return 0.0 if normalized == 0.0 else normalized


def _hash(payload: object) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


@lru_cache(maxsize=2)
def _verified_itt_policy(benchmark_id: str) -> FactorialITTPolicy:
    return FactorialITTPolicy.from_verified_manifest(benchmark_id=benchmark_id)


def _shared_variant_sha256(plan: FactorialFormalZeroCallPlan) -> str:
    return _hash(
        {
            "kind": "shared_v001_all_arm_variants",
            "variant_sha256s": dict(plan.arm_variant_sha256s),
        }
    )


def _post_prefix(task_seed_key_sha256: str, arm_id: str, version: str) -> str:
    return f"factorial-round:{task_seed_key_sha256}:{arm_id}:{version}"


@dataclass(frozen=True)
class FactorialScoringSlot:
    """One and only one preregistered ITT scoring position."""

    factorial_plan_sha256: str
    task_authority_bundle_sha256: str
    factorial_contract_sha256: str
    task_seed_key_sha256: str
    benchmark_id: str
    instance_id: str
    seed: int
    arm_id: str
    arm_variant_sha256: str
    arm_update_policy: str
    version: str
    shared_v001: bool
    cell_id: str
    attempt_id: str
    update_operation_id: str
    solution_operation_id: str
    evaluator_operation_id: str
    update_operation_expected: bool
    score_contract_sha256: str
    itt_policy_sha256: str
    schema_version: int = 1
    slot_kind: str = "factorial_exact_scoring_slot_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.slot_kind != (
            "factorial_exact_scoring_slot_v1"
        ):
            raise FactorialCoverageError("unsupported scoring-slot schema")
        for value, label in (
            (self.factorial_plan_sha256, "factorial plan sha256"),
            (self.task_authority_bundle_sha256, "task authority bundle sha256"),
            (self.factorial_contract_sha256, "factorial contract sha256"),
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.arm_variant_sha256, "arm variant sha256"),
            (self.score_contract_sha256, "score contract sha256"),
            (self.itt_policy_sha256, "ITT policy sha256"),
        ):
            _sha(value, label)
        for value, label in (
            (self.benchmark_id, "benchmark id"),
            (self.instance_id, "instance id"),
            (self.cell_id, "cell id"),
            (self.attempt_id, "attempt id"),
            (self.update_operation_id, "update operation id"),
            (self.solution_operation_id, "solution operation id"),
            (self.evaluator_operation_id, "evaluator operation id"),
        ):
            _safe(value, label)
        if type(self.seed) is not int or self.seed < 0:
            raise FactorialCoverageError("scoring-slot seed differs")
        if type(self.shared_v001) is not bool or type(
            self.update_operation_expected
        ) is not bool:
            raise FactorialCoverageError("scoring-slot boolean binding differs")
        match = _VERSION.fullmatch(self.version)
        if match is None or int(match.group(1)) < 1:
            raise FactorialCoverageError("scoring-slot version differs")
        contract = score_contract_for(self.benchmark_id)
        if self.score_contract_sha256 != contract.sha256:
            raise FactorialCoverageError("scoring-slot score contract differs")
        policy = _verified_itt_policy(self.benchmark_id)
        if (
            self.itt_policy_sha256 != policy.sha256
            or self.factorial_contract_sha256
            != policy.factorial_contract_sha256
        ):
            raise FactorialCoverageError("scoring-slot ITT policy differs")

        key_sha = self.task_seed_key_sha256
        if self.shared_v001:
            if (
                self.arm_id != SHARED_V001_ARM_ID
                or self.version != "v001"
                or self.arm_update_policy != "shared_v001_common_trunk_v1"
                or not self.update_operation_expected
                or self.cell_id != f"factorial-v001-cell:{key_sha}"
                or self.attempt_id != f"factorial-attempt:{key_sha}:shared-v001"
                or self.update_operation_id
                != f"factorial-v001:{key_sha}:builder"
                or self.solution_operation_id
                != f"factorial-v001:{key_sha}:solution"
                or self.evaluator_operation_id
                != f"factorial-v001:{key_sha}:evaluator"
            ):
                raise FactorialCoverageError("shared-v001 scoring identity differs")
        else:
            if self.arm_id not in ARM_IDS or int(match.group(1)) < 2:
                raise FactorialCoverageError("post-v001 arm/version differs")
            spec = ARM_POLICY_SPECS[self.arm_id]
            prefix = _post_prefix(key_sha, self.arm_id, self.version)
            if (
                self.arm_update_policy != spec.update_policy
                or self.update_operation_expected
                != (self.arm_id != A_FIXED_FEEDBACK)
                or self.cell_id != f"factorial-cell:{key_sha}:{self.arm_id}"
                or self.attempt_id != prefix + ":attempt"
                or self.update_operation_id != prefix + ":update"
                or self.solution_operation_id != prefix + ":solution"
                or self.evaluator_operation_id != prefix + ":evaluator"
            ):
                raise FactorialCoverageError("post-v001 scoring identity differs")

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_id": self.arm_id,
            "arm_update_policy": self.arm_update_policy,
            "arm_variant_sha256": self.arm_variant_sha256,
            "attempt_id": self.attempt_id,
            "benchmark_id": self.benchmark_id,
            "cell_id": self.cell_id,
            "evaluator_operation_id": self.evaluator_operation_id,
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "factorial_plan_sha256": self.factorial_plan_sha256,
            "instance_id": self.instance_id,
            "itt_policy_sha256": self.itt_policy_sha256,
            "schema_version": self.schema_version,
            "score_contract_sha256": self.score_contract_sha256,
            "seed": self.seed,
            "shared_v001": self.shared_v001,
            "slot_kind": self.slot_kind,
            "solution_operation_id": self.solution_operation_id,
            "task_authority_bundle_sha256": self.task_authority_bundle_sha256,
            "task_seed_key_sha256": self.task_seed_key_sha256,
            "update_operation_expected": self.update_operation_expected,
            "update_operation_id": self.update_operation_id,
            "version": self.version,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class ExactFactorialAttemptMatrix:
    """The exact 1,566-slot ITT population, with no execution authority."""

    slots: tuple[FactorialScoringSlot, ...]
    factorial_plan_sha256: str
    task_authority_bundle_sha256: str
    factorial_contract_sha256: str
    execution_authority: str = EXECUTION_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    schema_version: int = 1
    matrix_kind: str = "factorial_exact_attempt_matrix_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.matrix_kind != (
            "factorial_exact_attempt_matrix_v1"
        ):
            raise FactorialCoverageError("unsupported exact-attempt matrix schema")
        if self.execution_authority != EXECUTION_AUTHORITY:
            raise FactorialCoverageError("attempt matrix cannot grant execution")
        if self.model_call_entitlement != 0 or self.evaluator_transaction_entitlement != 0:
            raise FactorialCoverageError("attempt matrix entitlement must be zero")
        for value, label in (
            (self.factorial_plan_sha256, "factorial plan sha256"),
            (self.task_authority_bundle_sha256, "task authority bundle sha256"),
            (self.factorial_contract_sha256, "factorial contract sha256"),
        ):
            _sha(value, label)
        if not isinstance(self.slots, tuple) or any(
            type(slot) is not FactorialScoringSlot for slot in self.slots
        ):
            raise FactorialCoverageError("attempt matrix slots are not exact typed")
        if len(self.slots) != 1566:
            raise FactorialCoverageError("attempt matrix must contain 1,566 slots")
        attempt_ids = tuple(slot.attempt_id for slot in self.slots)
        slot_hashes = tuple(slot.sha256 for slot in self.slots)
        if len(set(attempt_ids)) != len(attempt_ids) or len(set(slot_hashes)) != len(
            slot_hashes
        ):
            raise FactorialCoverageError("attempt matrix repeats a scoring slot")
        if any(
            slot.factorial_plan_sha256 != self.factorial_plan_sha256
            or slot.task_authority_bundle_sha256
            != self.task_authority_bundle_sha256
            or slot.factorial_contract_sha256 != self.factorial_contract_sha256
            for slot in self.slots
        ):
            raise FactorialCoverageError("attempt matrix member binding differs")
        counts = self.counts
        if counts != {
            "agenthpobench_post_v001": 720,
            "gdpevo_post_v001": 720,
            "post_v001": 1440,
            "shared_v001": 126,
            "total": 1566,
        }:
            raise FactorialCoverageError("attempt matrix benchmark/version counts differ")

    @classmethod
    def from_verified_sources(
        cls,
        *,
        plan: FactorialFormalZeroCallPlan,
        bundle: ExactTaskSeedAuthorityBundle,
        task_authority: FactorialTaskArtifactAuthority,
    ) -> "ExactFactorialAttemptMatrix":
        if type(plan) is not FactorialFormalZeroCallPlan:
            raise FactorialCoverageError("exact formal plan is required")
        if type(bundle) is not ExactTaskSeedAuthorityBundle:
            raise FactorialCoverageError("exact task authority bundle is required")
        if type(task_authority) is not FactorialTaskArtifactAuthority:
            raise FactorialCoverageError("pinned-source task authority is required")
        try:
            verified_bundle = task_authority.verify_exact_bundle(bundle)
            verified_plan = FactorialFormalZeroCallPlan.from_bytes(
                plan.canonical_bytes,
                task_authority=task_authority,
                task_authority_bundle=verified_bundle,
                expected_sha256=plan.sha256,
            )
        except (TypeError, ValueError) as exc:
            raise FactorialCoverageError("exact source/plan replay failed") from exc
        if verified_plan != plan or tuple(
            schedule.key for schedule in verified_plan.schedules
        ) != verified_bundle.task_seed_keys:
            raise FactorialCoverageError("formal plan and task authority differ")

        variants = dict(verified_plan.arm_variant_sha256s)
        shared_variant = _shared_variant_sha256(verified_plan)
        plan_sha256 = verified_plan.sha256
        bundle_sha256 = verified_bundle.sha256
        factorial_contract_sha256 = verified_plan.factorial_contract_sha256
        slots: list[FactorialScoringSlot] = []
        for schedule in verified_plan.schedules:
            key = schedule.key
            contract = score_contract_for(key.suite)
            policy = _verified_itt_policy(key.suite)
            slots.append(
                FactorialScoringSlot(
                    factorial_plan_sha256=plan_sha256,
                    task_authority_bundle_sha256=bundle_sha256,
                    factorial_contract_sha256=factorial_contract_sha256,
                    task_seed_key_sha256=key.sha256,
                    benchmark_id=key.suite,
                    instance_id=key.instance_id,
                    seed=key.seed,
                    arm_id=SHARED_V001_ARM_ID,
                    arm_variant_sha256=shared_variant,
                    arm_update_policy="shared_v001_common_trunk_v1",
                    version="v001",
                    shared_v001=True,
                    cell_id=f"factorial-v001-cell:{key.sha256}",
                    attempt_id=f"factorial-attempt:{key.sha256}:shared-v001",
                    update_operation_id=key.operation_id("builder"),
                    solution_operation_id=key.operation_id("solution"),
                    evaluator_operation_id=key.operation_id("evaluator"),
                    update_operation_expected=True,
                    score_contract_sha256=contract.sha256,
                    itt_policy_sha256=policy.sha256,
                )
            )
            for version_number in range(2, schedule.final_version + 1):
                version = f"v{version_number:03d}"
                for arm_id in schedule.arm_order:
                    prefix = _post_prefix(key.sha256, arm_id, version)
                    slots.append(
                        FactorialScoringSlot(
                            factorial_plan_sha256=plan_sha256,
                            task_authority_bundle_sha256=bundle_sha256,
                            factorial_contract_sha256=factorial_contract_sha256,
                            task_seed_key_sha256=key.sha256,
                            benchmark_id=key.suite,
                            instance_id=key.instance_id,
                            seed=key.seed,
                            arm_id=arm_id,
                            arm_variant_sha256=variants[arm_id],
                            arm_update_policy=ARM_POLICY_SPECS[
                                arm_id
                            ].update_policy,
                            version=version,
                            shared_v001=False,
                            cell_id=key.arm_cell_id(arm_id),
                            attempt_id=prefix + ":attempt",
                            update_operation_id=prefix + ":update",
                            solution_operation_id=prefix + ":solution",
                            evaluator_operation_id=prefix + ":evaluator",
                            update_operation_expected=(
                                arm_id != A_FIXED_FEEDBACK
                            ),
                            score_contract_sha256=contract.sha256,
                            itt_policy_sha256=policy.sha256,
                        )
                    )
        return cls(
            slots=tuple(slots),
            factorial_plan_sha256=plan_sha256,
            task_authority_bundle_sha256=bundle_sha256,
            factorial_contract_sha256=factorial_contract_sha256,
        )

    @property
    def counts(self) -> dict[str, int]:
        shared = sum(slot.shared_v001 for slot in self.slots)
        agent_post = sum(
            not slot.shared_v001 and slot.benchmark_id == "agenthpobench"
            for slot in self.slots
        )
        gdpevo_post = sum(
            not slot.shared_v001 and slot.benchmark_id == "gdpevo"
            for slot in self.slots
        )
        return {
            "agenthpobench_post_v001": agent_post,
            "gdpevo_post_v001": gdpevo_post,
            "post_v001": agent_post + gdpevo_post,
            "shared_v001": shared,
            "total": len(self.slots),
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "counts": self.counts,
            "evaluator_transaction_entitlement": (
                self.evaluator_transaction_entitlement
            ),
            "execution_authority": self.execution_authority,
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "factorial_plan_sha256": self.factorial_plan_sha256,
            "matrix_kind": self.matrix_kind,
            "model_call_entitlement": self.model_call_entitlement,
            "schema_version": self.schema_version,
            "slots": [slot.to_dict() for slot in self.slots],
            "task_authority_bundle_sha256": self.task_authority_bundle_sha256,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class NativeEvaluationResult:
    """Factorial-native result; validity is independent of positive score."""

    benchmark_id: str
    valid: bool
    raw_score: float | None
    invalid_reason: str | None
    evidence_artifact_sha256: str
    actual_usage: ResourceVector
    schema_version: int = 1
    result_kind: str = "factorial_native_evaluation_result_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.result_kind != (
            "factorial_native_evaluation_result_v1"
        ):
            raise FactorialCoverageError("unsupported native-evaluation schema")
        _safe(self.benchmark_id, "native-evaluation benchmark")
        _sha(self.evidence_artifact_sha256, "native-evaluation evidence sha256")
        if type(self.actual_usage) is not ResourceVector:
            raise FactorialCoverageError("native evaluation requires exact ResourceVector")
        if self.actual_usage.evaluator_transactions != 1:
            raise FactorialCoverageError(
                "native evaluation must charge one evaluator transaction"
            )
        if self.actual_usage.model_calls != 0:
            raise FactorialCoverageError(
                "native evaluator result cannot charge solution or Builder calls"
            )
        if type(self.valid) is not bool:
            raise FactorialCoverageError("native-evaluation validity differs")
        contract = score_contract_for(self.benchmark_id)
        if self.valid:
            if self.raw_score is None or self.invalid_reason is not None:
                raise FactorialCoverageError("valid native evaluation fields differ")
            raw = _finite(self.raw_score, "native raw score")
            try:
                contract.utility_from_raw(raw)
            except ScoreContractError as exc:
                raise FactorialCoverageError("native raw score is outside contract") from exc
            object.__setattr__(self, "raw_score", raw)
        elif (
            self.raw_score is not None
            or not isinstance(self.invalid_reason, str)
            or not self.invalid_reason.strip()
            or len(self.invalid_reason) > 256
        ):
            raise FactorialCoverageError("invalid native evaluation fields differ")

    def to_score_receipt(self, *, evaluation_id: str) -> EvaluationScoreReceipt:
        _safe(evaluation_id, "native evaluation id")
        observation = EvaluationScoreObservation.create(
            benchmark_id=self.benchmark_id,
            valid=self.valid,
            raw_score=self.raw_score,
            invalid_reason=self.invalid_reason,
            evaluation_evidence_sha256=self.evidence_artifact_sha256,
        )
        return EvaluationScoreReceipt.seal(
            evaluation_id=evaluation_id, observation=observation
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "actual_usage": self.actual_usage.to_dict(),
            "benchmark_id": self.benchmark_id,
            "evidence_artifact_sha256": self.evidence_artifact_sha256,
            "invalid_reason": self.invalid_reason,
            "raw_score": self.raw_score,
            "result_kind": self.result_kind,
            "schema_version": self.schema_version,
            "valid": self.valid,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


def _canonical_operation_record_sha256(
    *, replay: JournalReplay, record: OperationRecord
) -> str:
    """Hash one record already owned by an independently verified replay.

    This is deliberately private: a ``JournalReplay`` is a plain DTO and can be
    constructed by arbitrary Python code.  The public trusted boundary below
    accepts only ledger/head paths and calls :func:`verify_operation_journal`
    itself.  Object identity here is a second check against swapping a record
    after that independent replay, not a substitute for provenance.
    """

    if type(replay) is not JournalReplay or type(record) is not OperationRecord:
        raise FactorialCoverageError("exact replay-derived OperationRecord required")
    if replay.operations.get(record.operation_id) is not record:
        raise FactorialCoverageError("OperationRecord is not owned by the replay")
    expected_events = tuple(
        event for event in replay.events if event.operation_id == record.operation_id
    )
    if expected_events != record.events or not expected_events:
        raise FactorialCoverageError("OperationRecord event coverage differs")
    projection = {
        "cell_id": record.cell_id,
        "committed_usage": record.committed_usage.to_dict(),
        "event_sha256s": [event.event_sha256 for event in record.events],
        "operation_id": record.operation_id,
        "operation_kind": record.operation_kind,
        "reservation": record.reservation.to_dict(),
        "schema_version": 1,
        "state": record.state,
    }
    return _hash(projection)


def canonical_operation_record_sha256_from_journal(
    *, ledger_path: Path, anchor_path: Path, operation_id: str
) -> str:
    """Independently replay a journal before canonicalizing one operation."""

    _safe(operation_id, "operation id")
    replay = verify_operation_journal(ledger_path, anchor_path=anchor_path)
    record = replay.operations.get(operation_id)
    if record is None:
        raise FactorialCoverageError("operation is absent from verified journal")
    return _canonical_operation_record_sha256(replay=replay, record=record)


@dataclass(frozen=True)
class AttemptCoverageRow:
    """Strict slot identity plus either no execution or an unbound score chain."""

    matrix_sha256: str
    slot_sha256: str
    attempt_id: str
    benchmark_id: str
    task_seed_key_sha256: str
    arm_id: str
    version: str
    cell_id: str
    update_operation_id: str
    solution_operation_id: str
    evaluator_operation_id: str
    coverage_state: str
    update_operation_record_sha256: str
    solution_operation_record_sha256: str
    evaluator_operation_record_sha256: str
    score_receipt_sha256: str
    itt_score_sha256: str
    report_row_sha256: str
    valid: bool | None
    floor_imputed: bool | None
    invalid_reason: str | None
    itt_raw_score: float | None
    schema_version: int = 1
    row_kind: str = "factorial_attempt_coverage_row_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.row_kind != (
            "factorial_attempt_coverage_row_v1"
        ):
            raise FactorialCoverageError("unsupported coverage-row schema")
        for value, label in (
            (self.matrix_sha256, "coverage matrix sha256"),
            (self.slot_sha256, "coverage slot sha256"),
            (self.task_seed_key_sha256, "coverage task/seed sha256"),
        ):
            _sha(value, label)
        for value, label in (
            (self.attempt_id, "coverage attempt id"),
            (self.benchmark_id, "coverage benchmark id"),
            (self.cell_id, "coverage cell id"),
            (self.update_operation_id, "coverage update operation id"),
            (self.solution_operation_id, "coverage solution operation id"),
            (self.evaluator_operation_id, "coverage evaluator operation id"),
        ):
            _safe(value, label)
        if self.arm_id not in (*ARM_IDS, SHARED_V001_ARM_ID):
            raise FactorialCoverageError("coverage row arm differs")
        if _VERSION.fullmatch(self.version) is None:
            raise FactorialCoverageError("coverage row version differs")
        if self.coverage_state not in _COVERAGE_STATES:
            raise FactorialCoverageError("coverage row state differs")
        chain_hashes = (
            self.update_operation_record_sha256,
            self.solution_operation_record_sha256,
            self.evaluator_operation_record_sha256,
            self.score_receipt_sha256,
            self.itt_score_sha256,
            self.report_row_sha256,
        )
        for value in chain_hashes:
            _sha(value, "coverage artifact sha256", allow_zero=True)
        if self.coverage_state == UNEXECUTED:
            if any(value != ZERO_SHA256 for value in chain_hashes) or any(
                value is not None
                for value in (
                    self.valid,
                    self.floor_imputed,
                    self.invalid_reason,
                    self.itt_raw_score,
                )
            ):
                raise FactorialCoverageError("unexecuted row carries result evidence")
        else:
            if any(
                value == ZERO_SHA256
                for value in (
                    self.score_receipt_sha256,
                    self.itt_score_sha256,
                    self.report_row_sha256,
                )
            ):
                raise FactorialCoverageError("typed score row lacks score-chain hashes")
            # The operation record fields intentionally remain empty until the
            # reservation/evaluator dispatcher is connected.
            if any(value != ZERO_SHA256 for value in chain_hashes[:3]):
                raise FactorialCoverageError(
                    "unbound score row cannot claim operation-ledger evidence"
                )
            if type(self.valid) is not bool or type(self.floor_imputed) is not bool:
                raise FactorialCoverageError("typed score row validity differs")
            raw = _finite(self.itt_raw_score, "coverage ITT raw score")
            contract = score_contract_for(self.benchmark_id)
            try:
                contract.utility_from_raw(raw)
            except ScoreContractError as exc:
                raise FactorialCoverageError("coverage raw score is outside contract") from exc
            if self.valid:
                if self.floor_imputed or self.invalid_reason is not None:
                    raise FactorialCoverageError("valid coverage row is imputed")
            elif (
                not self.floor_imputed
                or not isinstance(self.invalid_reason, str)
                or not self.invalid_reason.strip()
                or raw != contract.raw_min
            ):
                raise FactorialCoverageError(
                    "invalid coverage row must use benchmark-native floor"
                )
            object.__setattr__(self, "itt_raw_score", raw)

    @classmethod
    def unexecuted(
        cls, *, matrix_sha256: str, slot: FactorialScoringSlot
    ) -> "AttemptCoverageRow":
        if type(slot) is not FactorialScoringSlot:
            raise FactorialCoverageError("exact scoring slot is required")
        return cls(
            **cls._slot_fields(matrix_sha256=matrix_sha256, slot=slot),
            coverage_state=UNEXECUTED,
            update_operation_record_sha256=ZERO_SHA256,
            solution_operation_record_sha256=ZERO_SHA256,
            evaluator_operation_record_sha256=ZERO_SHA256,
            score_receipt_sha256=ZERO_SHA256,
            itt_score_sha256=ZERO_SHA256,
            report_row_sha256=ZERO_SHA256,
            valid=None,
            floor_imputed=None,
            invalid_reason=None,
            itt_raw_score=None,
        )

    @classmethod
    def from_typed_score_chain(
        cls,
        *,
        matrix_sha256: str,
        slot: FactorialScoringSlot,
        policy: FactorialITTPolicy,
        score_receipt: EvaluationScoreReceipt,
        itt_score: FactorialITTScore,
        report_row: VerifiedITTReportRow,
    ) -> "AttemptCoverageRow":
        if type(slot) is not FactorialScoringSlot:
            raise FactorialCoverageError("exact scoring slot is required")
        if type(policy) is not FactorialITTPolicy:
            raise FactorialCoverageError("exact ITT policy is required")
        if type(score_receipt) is not EvaluationScoreReceipt:
            raise FactorialCoverageError("exact score receipt is required")
        if score_receipt.evaluation_id != slot.attempt_id:
            raise FactorialCoverageError("score receipt attempt binding differs")
        if (
            score_receipt.benchmark_id != slot.benchmark_id
            or score_receipt.score_contract_sha256 != slot.score_contract_sha256
            or policy.sha256 != slot.itt_policy_sha256
            or policy.factorial_contract_sha256 != slot.factorial_contract_sha256
        ):
            raise FactorialCoverageError("score chain slot policy differs")
        verified_score = FactorialITTScore.from_canonical_bytes(
            itt_score.canonical_bytes(), policy=policy, score_receipt=score_receipt
        )
        verified_report = VerifiedITTReportRow.from_canonical_bytes(
            report_row.canonical_bytes(),
            policy=policy,
            score_receipt=score_receipt,
            itt_score=verified_score,
        )
        return cls(
            **cls._slot_fields(matrix_sha256=matrix_sha256, slot=slot),
            coverage_state=TYPED_SCORE_UNBOUND,
            update_operation_record_sha256=ZERO_SHA256,
            solution_operation_record_sha256=ZERO_SHA256,
            evaluator_operation_record_sha256=ZERO_SHA256,
            score_receipt_sha256=score_receipt.sha256,
            itt_score_sha256=verified_score.sha256,
            report_row_sha256=verified_report.sha256,
            valid=verified_score.valid,
            floor_imputed=verified_score.floor_imputed,
            invalid_reason=verified_score.invalid_reason,
            itt_raw_score=verified_score.raw_itt_score,
        )

    @staticmethod
    def _slot_fields(
        *, matrix_sha256: str, slot: FactorialScoringSlot
    ) -> dict[str, Any]:
        return {
            "matrix_sha256": matrix_sha256,
            "slot_sha256": slot.sha256,
            "attempt_id": slot.attempt_id,
            "benchmark_id": slot.benchmark_id,
            "task_seed_key_sha256": slot.task_seed_key_sha256,
            "arm_id": slot.arm_id,
            "version": slot.version,
            "cell_id": slot.cell_id,
            "update_operation_id": slot.update_operation_id,
            "solution_operation_id": slot.solution_operation_id,
            "evaluator_operation_id": slot.evaluator_operation_id,
        }

    def verify_against_slot(
        self, *, matrix_sha256: str, slot: FactorialScoringSlot
    ) -> None:
        if type(self) is not AttemptCoverageRow:
            raise FactorialCoverageError("exact coverage row is required")
        expected = self._slot_fields(matrix_sha256=matrix_sha256, slot=slot)
        if any(getattr(self, field) != value for field, value in expected.items()):
            raise FactorialCoverageError("coverage row slot binding differs")

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_id": self.arm_id,
            "attempt_id": self.attempt_id,
            "benchmark_id": self.benchmark_id,
            "cell_id": self.cell_id,
            "coverage_state": self.coverage_state,
            "evaluator_operation_id": self.evaluator_operation_id,
            "evaluator_operation_record_sha256": (
                self.evaluator_operation_record_sha256
            ),
            "floor_imputed": self.floor_imputed,
            "invalid_reason": self.invalid_reason,
            "itt_raw_score": self.itt_raw_score,
            "itt_score_sha256": self.itt_score_sha256,
            "matrix_sha256": self.matrix_sha256,
            "report_row_sha256": self.report_row_sha256,
            "row_kind": self.row_kind,
            "schema_version": self.schema_version,
            "score_receipt_sha256": self.score_receipt_sha256,
            "slot_sha256": self.slot_sha256,
            "solution_operation_id": self.solution_operation_id,
            "solution_operation_record_sha256": (
                self.solution_operation_record_sha256
            ),
            "task_seed_key_sha256": self.task_seed_key_sha256,
            "update_operation_id": self.update_operation_id,
            "update_operation_record_sha256": self.update_operation_record_sha256,
            "valid": self.valid,
            "version": self.version,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class FactorialCoverageSeal:
    """Exact-set audit receipt that explicitly grants no formal authority."""

    matrix_sha256: str
    factorial_plan_sha256: str
    task_authority_bundle_sha256: str
    planned_scoring_slot_count: int
    submitted_row_count: int
    unexecuted_row_count: int
    typed_score_unbound_row_count: int
    ordered_row_set_sha256: str
    formal_dispatch_status: str = FORMAL_DISPATCH_STATUS
    exact_slot_set_complete: bool = True
    all_reserved_attempts_covered: bool = False
    formal_execution_ready: bool = False
    execution_authority: str = EXECUTION_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    operation_journal_event_count: int = 0
    operation_journal_head_sha256: str = ZERO_SHA256
    schema_version: int = 1
    seal_kind: str = "factorial_zero_call_coverage_seal_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.seal_kind != (
            "factorial_zero_call_coverage_seal_v1"
        ):
            raise FactorialCoverageError("unsupported coverage-seal schema")
        for value, label, allow_zero in (
            (self.matrix_sha256, "coverage matrix sha256", False),
            (self.factorial_plan_sha256, "coverage plan sha256", False),
            (
                self.task_authority_bundle_sha256,
                "coverage authority bundle sha256",
                False,
            ),
            (self.ordered_row_set_sha256, "coverage row-set sha256", False),
            (self.operation_journal_head_sha256, "operation journal head", True),
        ):
            _sha(value, label, allow_zero=allow_zero)
        counts = (
            self.planned_scoring_slot_count,
            self.submitted_row_count,
            self.unexecuted_row_count,
            self.typed_score_unbound_row_count,
            self.operation_journal_event_count,
        )
        if any(type(value) is not int or value < 0 for value in counts):
            raise FactorialCoverageError("coverage seal counts differ")
        if (
            self.planned_scoring_slot_count != 1566
            or self.submitted_row_count != 1566
            or self.unexecuted_row_count + self.typed_score_unbound_row_count
            != 1566
        ):
            raise FactorialCoverageError("coverage seal slot counts differ")
        if (
            self.formal_dispatch_status != FORMAL_DISPATCH_STATUS
            or self.exact_slot_set_complete is not True
            or self.all_reserved_attempts_covered is not False
            or self.formal_execution_ready is not False
            or self.execution_authority != EXECUTION_AUTHORITY
            or self.model_call_entitlement != 0
            or self.evaluator_transaction_entitlement != 0
            or self.operation_journal_event_count != 0
            or self.operation_journal_head_sha256 != ZERO_SHA256
        ):
            raise FactorialCoverageError(
                "zero-call coverage seal cannot claim formal execution readiness"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "all_reserved_attempts_covered": self.all_reserved_attempts_covered,
            "evaluator_transaction_entitlement": (
                self.evaluator_transaction_entitlement
            ),
            "exact_slot_set_complete": self.exact_slot_set_complete,
            "execution_authority": self.execution_authority,
            "factorial_plan_sha256": self.factorial_plan_sha256,
            "formal_dispatch_status": self.formal_dispatch_status,
            "formal_execution_ready": self.formal_execution_ready,
            "matrix_sha256": self.matrix_sha256,
            "model_call_entitlement": self.model_call_entitlement,
            "operation_journal_event_count": self.operation_journal_event_count,
            "operation_journal_head_sha256": self.operation_journal_head_sha256,
            "ordered_row_set_sha256": self.ordered_row_set_sha256,
            "planned_scoring_slot_count": self.planned_scoring_slot_count,
            "schema_version": self.schema_version,
            "seal_kind": self.seal_kind,
            "submitted_row_count": self.submitted_row_count,
            "task_authority_bundle_sha256": self.task_authority_bundle_sha256,
            "typed_score_unbound_row_count": self.typed_score_unbound_row_count,
            "unexecuted_row_count": self.unexecuted_row_count,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


class FactorialCoverageVerifier:
    """Verify exact row coverage without treating rows as execution evidence."""

    def __init__(
        self,
        matrix: ExactFactorialAttemptMatrix,
        *,
        _verified_source_replay: ExactFactorialAttemptMatrix | None = None,
    ) -> None:
        if (
            type(matrix) is not ExactFactorialAttemptMatrix
            or type(_verified_source_replay) is not ExactFactorialAttemptMatrix
            or matrix != _verified_source_replay
            or matrix.canonical_bytes != _verified_source_replay.canonical_bytes
            or matrix.sha256 != _verified_source_replay.sha256
        ):
            raise FactorialCoverageError(
                "coverage verifier requires a matrix replayed from verified sources"
            )
        self.matrix = matrix

    @classmethod
    def from_verified_sources(
        cls,
        *,
        matrix: ExactFactorialAttemptMatrix,
        plan: FactorialFormalZeroCallPlan,
        bundle: ExactTaskSeedAuthorityBundle,
        task_authority: FactorialTaskArtifactAuthority,
    ) -> "FactorialCoverageVerifier":
        """Rebuild the entire slot population at the coverage trust boundary."""

        if type(matrix) is not ExactFactorialAttemptMatrix:
            raise FactorialCoverageError("exact attempt matrix is required")
        expected = ExactFactorialAttemptMatrix.from_verified_sources(
            plan=plan,
            bundle=bundle,
            task_authority=task_authority,
        )
        if (
            matrix != expected
            or matrix.canonical_bytes != expected.canonical_bytes
            or matrix.sha256 != expected.sha256
        ):
            raise FactorialCoverageError(
                "attempt matrix differs from pinned source replay"
            )
        return cls(matrix, _verified_source_replay=expected)

    def seal(self, rows: Sequence[AttemptCoverageRow]) -> FactorialCoverageSeal:
        if isinstance(rows, (str, bytes)) or not isinstance(rows, Sequence):
            raise FactorialCoverageError("coverage rows must be a sequence")
        if any(type(row) is not AttemptCoverageRow for row in rows):
            raise FactorialCoverageError("coverage rows must be exact typed")
        attempt_ids = [row.attempt_id for row in rows]
        if len(attempt_ids) != len(set(attempt_ids)):
            raise FactorialCoverageError("coverage rows contain duplicate attempts")
        expected = {slot.attempt_id: slot for slot in self.matrix.slots}
        actual = set(attempt_ids)
        missing = set(expected) - actual
        extra = actual - set(expected)
        if missing or extra:
            raise FactorialCoverageError(
                "coverage row exact set differs: "
                f"missing={len(missing)}, extra={len(extra)}"
            )
        by_id = {row.attempt_id: row for row in rows}
        ordered: list[AttemptCoverageRow] = []
        matrix_sha256 = self.matrix.sha256
        for slot in self.matrix.slots:
            row = by_id[slot.attempt_id]
            row.verify_against_slot(matrix_sha256=matrix_sha256, slot=slot)
            ordered.append(row)
        row_set_sha = _hash([row.sha256 for row in ordered])
        return FactorialCoverageSeal(
            matrix_sha256=matrix_sha256,
            factorial_plan_sha256=self.matrix.factorial_plan_sha256,
            task_authority_bundle_sha256=(
                self.matrix.task_authority_bundle_sha256
            ),
            planned_scoring_slot_count=len(self.matrix.slots),
            submitted_row_count=len(ordered),
            unexecuted_row_count=sum(
                row.coverage_state == UNEXECUTED for row in ordered
            ),
            typed_score_unbound_row_count=sum(
                row.coverage_state == TYPED_SCORE_UNBOUND for row in ordered
            ),
            ordered_row_set_sha256=row_set_sha,
        )


__all__ = [
    "AttemptCoverageRow",
    "ExactFactorialAttemptMatrix",
    "FactorialCoverageError",
    "FactorialCoverageSeal",
    "FactorialCoverageVerifier",
    "FactorialScoringSlot",
    "FORMAL_DISPATCH_STATUS",
    "NativeEvaluationResult",
    "SHARED_V001_ARM_ID",
    "TYPED_SCORE_UNBOUND",
    "UNEXECUTED",
    "canonical_operation_record_sha256_from_journal",
]
