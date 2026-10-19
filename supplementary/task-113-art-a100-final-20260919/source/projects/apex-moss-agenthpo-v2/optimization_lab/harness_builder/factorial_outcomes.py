"""Typed, attempt-scoped execution evidence for the shared v001 trunk.

The shared v001 solution/evaluation may execute only after the common compile
has been sealed.  This module records each completed stage without inventing a
later-stage artifact.  In particular, an invalid environment is a retryable
*attempt* outcome and is never installed as the terminal task/seed outcome.

This is an archival/state-validation layer.  It has no provider, model,
subprocess, or evaluator entry point.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ._safe_artifacts import (
    lexical_absolute,
    read_safe_regular_file,
    safe_regular_file_exists,
    write_once_safe_regular_file,
)
from .factorial_trunk import (
    ZERO_SHA256,
    TaskSeedKey,
    V001TrunkIntent,
    V001TrunkReceipt,
    _ContentAddressed,
    _canonical_bytes,
    _decode,
    _exact_fields,
    _safe,
    _sha,
)


_ENVIRONMENT_STATUSES = {"VALID", "ENVIRONMENT_INVALID"}
_CANDIDATE_STATUSES = {"ACCEPTED", "CONTRACT_REJECTED"}
_EVALUATION_STATUSES = {"VALID", "INVALID"}
_INTERRUPTION_STAGES = {"solution", "attempt_validation", "evaluation"}
_INTERRUPTION_KINDS = {
    "STARTED_WITHOUT_ARTIFACT",
    "TERMINAL_FAILED",
    "ARTIFACT_VALIDATION_FAILED",
}
_ATTEMPT_STATUSES = {
    "SUCCESS",
    "SOLUTION_CONTRACT_REJECTED",
    "OPERATION_INTERRUPTED",
    "COMMON_TRUNK_FAILURE",
    "ENVIRONMENT_INVALID",
}
_TERMINAL_ATTEMPT_STATUSES = _ATTEMPT_STATUSES - {"ENVIRONMENT_INVALID"}
_MAX_ATTEMPT_INDEX = 1024


def _typed_from_bytes(
    cls: type[Any], encoded: bytes, *, expected_sha256: str
) -> Any:
    _sha(expected_sha256, "expected outcome sha256", allow_zero=False)
    payload = _decode(encoded, label=cls.__name__)
    _exact_fields(
        payload,
        {"schema_version", *(field.name for field in cls.__dataclass_fields__.values())},
        cls.__name__,
    )
    if payload.pop("schema_version") != 1:
        raise ValueError(f"{cls.__name__} schema differs")
    item = cls.from_payload(payload)
    if item.canonical_bytes != encoded:
        raise ValueError(f"{cls.__name__} is not canonical")
    if item.sha256 != expected_sha256:
        raise ValueError(f"{cls.__name__} hash differs")
    return item


def _optional_payload(value: Any, cls: type[Any], label: str) -> Any:
    if value is None or isinstance(value, cls):
        return value
    if not isinstance(value, dict):
        raise ValueError(f"{label} differs")
    return cls.from_payload(value)


@dataclass(frozen=True)
class V001ExecutionAttemptIntent(_ContentAddressed):
    task_seed_key_sha256: str
    trunk_intent_sha256: str
    canonical_compile_contract_sha256: str
    compile_equivalence_receipt_sha256: str
    attempt_index: int
    previous_attempt_receipt_sha256: str
    environment_binding_sha256: str
    solution_operation_id: str
    attempt_validation_operation_id: str
    evaluator_operation_id: str

    def __post_init__(self) -> None:
        for value, label, allow_zero in (
            (self.task_seed_key_sha256, "task/seed key sha256", False),
            (self.trunk_intent_sha256, "trunk intent sha256", False),
            (
                self.canonical_compile_contract_sha256,
                "canonical compile contract sha256",
                False,
            ),
            (
                self.compile_equivalence_receipt_sha256,
                "compile equivalence receipt sha256",
                False,
            ),
            (
                self.previous_attempt_receipt_sha256,
                "previous attempt receipt sha256",
                True,
            ),
            (self.environment_binding_sha256, "environment binding sha256", False),
        ):
            _sha(value, label, allow_zero=allow_zero)
        if (
            type(self.attempt_index) is not int
            or not 1 <= self.attempt_index <= _MAX_ATTEMPT_INDEX
        ):
            raise ValueError("v001 execution attempt index differs")
        if (self.attempt_index == 1) != (
            self.previous_attempt_receipt_sha256 == ZERO_SHA256
        ):
            raise ValueError("v001 execution attempt parent differs")
        expected_prefix = f"factorial-v001:{self.task_seed_key_sha256}:"
        if (
            self.solution_operation_id != expected_prefix + "solution"
            or self.attempt_validation_operation_id
            != expected_prefix + "attempt-validation"
            or self.evaluator_operation_id != expected_prefix + "evaluator"
        ):
            raise ValueError("v001 execution operation identity differs")

    @classmethod
    def create(
        cls,
        *,
        trunk_intent: V001TrunkIntent,
        canonical_compile_contract: Any,
        compile_equivalence_receipt: Any,
        attempt_index: int,
        previous_attempt_receipt_sha256: str,
        environment_binding_sha256: str,
    ) -> "V001ExecutionAttemptIntent":
        if not isinstance(trunk_intent, V001TrunkIntent):
            raise TypeError("typed v001 trunk intent is required")
        key = trunk_intent.task_seed_key
        if (
            canonical_compile_contract.task_seed_key_sha256 != key.sha256
            or canonical_compile_contract.context_binding_sha256
            != key.context_binding_sha256
            or compile_equivalence_receipt.task_seed_key_sha256 != key.sha256
            or compile_equivalence_receipt.canonical_compile_contract_sha256
            != canonical_compile_contract.sha256
            or compile_equivalence_receipt.canonical_compiled_harness_semantic_sha256
            != canonical_compile_contract.compiled_harness_semantic_sha256
        ):
            raise ValueError("v001 execution attempt compile binding differs")
        return cls(
            task_seed_key_sha256=key.sha256,
            trunk_intent_sha256=trunk_intent.sha256,
            canonical_compile_contract_sha256=canonical_compile_contract.sha256,
            compile_equivalence_receipt_sha256=compile_equivalence_receipt.sha256,
            attempt_index=attempt_index,
            previous_attempt_receipt_sha256=previous_attempt_receipt_sha256,
            environment_binding_sha256=environment_binding_sha256,
            solution_operation_id=trunk_intent.solution_operation_id,
            attempt_validation_operation_id=(
                f"factorial-v001:{key.sha256}:attempt-validation"
            ),
            evaluator_operation_id=trunk_intent.evaluator_operation_id,
        )

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "V001ExecutionAttemptIntent":
        return cls(**payload)

    @classmethod
    def from_bytes(
        cls, encoded: bytes, *, expected_sha256: str
    ) -> "V001ExecutionAttemptIntent":
        return _typed_from_bytes(cls, encoded, expected_sha256=expected_sha256)


@dataclass(frozen=True)
class V001EnvironmentCheckReceipt(_ContentAddressed):
    task_seed_key_sha256: str
    attempt_intent_sha256: str
    attempt_index: int
    environment_binding_sha256: str
    status: str
    evidence_artifact_sha256: str
    reason_code: str

    def __post_init__(self) -> None:
        _sha(self.task_seed_key_sha256, "task/seed key sha256", allow_zero=False)
        _sha(self.attempt_intent_sha256, "attempt intent sha256", allow_zero=False)
        _sha(self.environment_binding_sha256, "environment binding sha256", allow_zero=False)
        _sha(self.evidence_artifact_sha256, "environment evidence sha256", allow_zero=False)
        if type(self.attempt_index) is not int or self.attempt_index < 1:
            raise ValueError("environment check attempt index differs")
        if self.status not in _ENVIRONMENT_STATUSES:
            raise ValueError("environment check status differs")
        if self.status == "VALID":
            if self.reason_code != "NONE":
                raise ValueError("valid environment check carries a failure reason")
        else:
            _safe(self.reason_code, "environment invalid reason code")
            if self.reason_code == "NONE":
                raise ValueError("environment-invalid check lacks a reason")

    @classmethod
    def create(
        cls,
        *,
        attempt_intent: V001ExecutionAttemptIntent,
        status: str,
        evidence_artifact_sha256: str,
        reason_code: str = "NONE",
    ) -> "V001EnvironmentCheckReceipt":
        return cls(
            task_seed_key_sha256=attempt_intent.task_seed_key_sha256,
            attempt_intent_sha256=attempt_intent.sha256,
            attempt_index=attempt_intent.attempt_index,
            environment_binding_sha256=attempt_intent.environment_binding_sha256,
            status=status,
            evidence_artifact_sha256=evidence_artifact_sha256,
            reason_code=reason_code,
        )

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "V001EnvironmentCheckReceipt":
        return cls(**payload)

    @classmethod
    def from_bytes(
        cls, encoded: bytes, *, expected_sha256: str
    ) -> "V001EnvironmentCheckReceipt":
        return _typed_from_bytes(cls, encoded, expected_sha256=expected_sha256)


@dataclass(frozen=True)
class V001SolutionOperationReceipt(_ContentAddressed):
    task_seed_key_sha256: str
    attempt_intent_sha256: str
    attempt_index: int
    operation_id: str
    operation_record_sha256: str
    raw_response_artifact_sha256: str
    solution_artifact_sha256: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.attempt_intent_sha256, "attempt intent sha256"),
            (self.operation_record_sha256, "solution operation record sha256"),
            (self.raw_response_artifact_sha256, "raw solution response sha256"),
            (self.solution_artifact_sha256, "solution artifact sha256"),
        ):
            _sha(value, label, allow_zero=False)
        if type(self.attempt_index) is not int or self.attempt_index < 1:
            raise ValueError("solution operation attempt index differs")
        _safe(self.operation_id, "solution operation id")
        expected = f"factorial-v001:{self.task_seed_key_sha256}:solution"
        if self.operation_id != expected:
            raise ValueError("solution operation id differs")

    @classmethod
    def create(
        cls,
        *,
        attempt_intent: V001ExecutionAttemptIntent,
        operation_record_sha256: str,
        raw_response_artifact_sha256: str,
        solution_artifact_sha256: str,
    ) -> "V001SolutionOperationReceipt":
        return cls(
            task_seed_key_sha256=attempt_intent.task_seed_key_sha256,
            attempt_intent_sha256=attempt_intent.sha256,
            attempt_index=attempt_intent.attempt_index,
            operation_id=attempt_intent.solution_operation_id,
            operation_record_sha256=operation_record_sha256,
            raw_response_artifact_sha256=raw_response_artifact_sha256,
            solution_artifact_sha256=solution_artifact_sha256,
        )

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "V001SolutionOperationReceipt":
        return cls(**payload)

    @classmethod
    def from_bytes(
        cls, encoded: bytes, *, expected_sha256: str
    ) -> "V001SolutionOperationReceipt":
        return _typed_from_bytes(cls, encoded, expected_sha256=expected_sha256)


@dataclass(frozen=True)
class V001AttemptOutcomeReceipt(_ContentAddressed):
    task_seed_key_sha256: str
    attempt_intent_sha256: str
    attempt_index: int
    solution_receipt_sha256: str
    status: str
    attempt_artifact_sha256: str
    contract_evidence_sha256: str
    candidate_artifact_sha256: str

    def __post_init__(self) -> None:
        for value, label, allow_zero in (
            (self.task_seed_key_sha256, "task/seed key sha256", False),
            (self.attempt_intent_sha256, "attempt intent sha256", False),
            (self.solution_receipt_sha256, "solution receipt sha256", False),
            (self.attempt_artifact_sha256, "attempt artifact sha256", False),
            (self.contract_evidence_sha256, "contract evidence sha256", False),
            (self.candidate_artifact_sha256, "candidate artifact sha256", True),
        ):
            _sha(value, label, allow_zero=allow_zero)
        if type(self.attempt_index) is not int or self.attempt_index < 1:
            raise ValueError("candidate attempt index differs")
        if self.status not in _CANDIDATE_STATUSES:
            raise ValueError("candidate attempt status differs")
        if (self.status == "ACCEPTED") != (
            self.candidate_artifact_sha256 != ZERO_SHA256
        ):
            raise ValueError("candidate attempt artifact presence differs")

    @classmethod
    def create(
        cls,
        *,
        attempt_intent: V001ExecutionAttemptIntent,
        solution_receipt: V001SolutionOperationReceipt,
        status: str,
        attempt_artifact_sha256: str,
        contract_evidence_sha256: str,
        candidate_artifact_sha256: str = ZERO_SHA256,
    ) -> "V001AttemptOutcomeReceipt":
        _verify_stage_identity(attempt_intent, solution_receipt, "solution")
        return cls(
            task_seed_key_sha256=attempt_intent.task_seed_key_sha256,
            attempt_intent_sha256=attempt_intent.sha256,
            attempt_index=attempt_intent.attempt_index,
            solution_receipt_sha256=solution_receipt.sha256,
            status=status,
            attempt_artifact_sha256=attempt_artifact_sha256,
            contract_evidence_sha256=contract_evidence_sha256,
            candidate_artifact_sha256=candidate_artifact_sha256,
        )

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "V001AttemptOutcomeReceipt":
        return cls(**payload)

    @classmethod
    def from_bytes(
        cls, encoded: bytes, *, expected_sha256: str
    ) -> "V001AttemptOutcomeReceipt":
        return _typed_from_bytes(cls, encoded, expected_sha256=expected_sha256)


@dataclass(frozen=True)
class V001EvaluationOperationReceipt(_ContentAddressed):
    task_seed_key_sha256: str
    attempt_intent_sha256: str
    attempt_index: int
    candidate_attempt_receipt_sha256: str
    status: str
    operation_id: str
    operation_record_sha256: str
    evaluation_artifact_sha256: str
    score_observation_sha256: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.attempt_intent_sha256, "attempt intent sha256"),
            (self.candidate_attempt_receipt_sha256, "candidate attempt receipt sha256"),
            (self.operation_record_sha256, "evaluation operation record sha256"),
            (self.evaluation_artifact_sha256, "evaluation artifact sha256"),
            (self.score_observation_sha256, "score observation sha256"),
        ):
            _sha(value, label, allow_zero=False)
        if type(self.attempt_index) is not int or self.attempt_index < 1:
            raise ValueError("evaluation operation attempt index differs")
        if self.status not in _EVALUATION_STATUSES:
            raise ValueError("evaluation operation status differs")
        _safe(self.operation_id, "evaluation operation id")
        expected = f"factorial-v001:{self.task_seed_key_sha256}:evaluator"
        if self.operation_id != expected:
            raise ValueError("evaluation operation id differs")

    @classmethod
    def create(
        cls,
        *,
        attempt_intent: V001ExecutionAttemptIntent,
        candidate_attempt_receipt: V001AttemptOutcomeReceipt,
        status: str,
        operation_record_sha256: str,
        evaluation_artifact_sha256: str,
        score_observation_sha256: str,
    ) -> "V001EvaluationOperationReceipt":
        _verify_stage_identity(attempt_intent, candidate_attempt_receipt, "candidate")
        if candidate_attempt_receipt.status != "ACCEPTED":
            raise ValueError("contract-rejected candidate cannot be evaluated")
        return cls(
            task_seed_key_sha256=attempt_intent.task_seed_key_sha256,
            attempt_intent_sha256=attempt_intent.sha256,
            attempt_index=attempt_intent.attempt_index,
            candidate_attempt_receipt_sha256=candidate_attempt_receipt.sha256,
            status=status,
            operation_id=attempt_intent.evaluator_operation_id,
            operation_record_sha256=operation_record_sha256,
            evaluation_artifact_sha256=evaluation_artifact_sha256,
            score_observation_sha256=score_observation_sha256,
        )

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "V001EvaluationOperationReceipt":
        return cls(**payload)

    @classmethod
    def from_bytes(
        cls, encoded: bytes, *, expected_sha256: str
    ) -> "V001EvaluationOperationReceipt":
        return _typed_from_bytes(cls, encoded, expected_sha256=expected_sha256)


@dataclass(frozen=True)
class V001StageInterruptionReceipt(_ContentAddressed):
    task_seed_key_sha256: str
    attempt_intent_sha256: str
    attempt_index: int
    stage: str
    interruption_kind: str
    operation_id: str
    operation_record_sha256: str
    evidence_artifact_sha256: str
    reason_code: str
    completed_solution_receipt_sha256: str
    completed_candidate_attempt_receipt_sha256: str

    def __post_init__(self) -> None:
        for value, label, allow_zero in (
            (self.task_seed_key_sha256, "task/seed key sha256", False),
            (self.attempt_intent_sha256, "attempt intent sha256", False),
            (self.operation_record_sha256, "interrupted operation record sha256", False),
            (self.evidence_artifact_sha256, "interruption evidence sha256", False),
            (
                self.completed_solution_receipt_sha256,
                "completed solution receipt sha256",
                True,
            ),
            (
                self.completed_candidate_attempt_receipt_sha256,
                "completed candidate receipt sha256",
                True,
            ),
        ):
            _sha(value, label, allow_zero=allow_zero)
        if type(self.attempt_index) is not int or self.attempt_index < 1:
            raise ValueError("interruption attempt index differs")
        if self.stage not in _INTERRUPTION_STAGES:
            raise ValueError("interruption stage differs")
        if self.interruption_kind not in _INTERRUPTION_KINDS:
            raise ValueError("interruption kind differs")
        _safe(self.operation_id, "interrupted operation id")
        _safe(self.reason_code, "interruption reason code")
        expected_operation = {
            "solution": f"factorial-v001:{self.task_seed_key_sha256}:solution",
            "attempt_validation": (
                f"factorial-v001:{self.task_seed_key_sha256}:attempt-validation"
            ),
            "evaluation": f"factorial-v001:{self.task_seed_key_sha256}:evaluator",
        }[self.stage]
        if self.operation_id != expected_operation:
            raise ValueError("interruption operation id differs")
        expected_prefix = {
            "solution": (False, False),
            "attempt_validation": (True, False),
            "evaluation": (True, True),
        }[self.stage]
        actual_prefix = (
            self.completed_solution_receipt_sha256 != ZERO_SHA256,
            self.completed_candidate_attempt_receipt_sha256 != ZERO_SHA256,
        )
        if actual_prefix != expected_prefix:
            raise ValueError("interruption completed stage prefix differs")

    @classmethod
    def create(
        cls,
        *,
        attempt_intent: V001ExecutionAttemptIntent,
        stage: str,
        interruption_kind: str,
        operation_record_sha256: str,
        evidence_artifact_sha256: str,
        reason_code: str,
        solution_receipt: V001SolutionOperationReceipt | None = None,
        candidate_attempt_receipt: V001AttemptOutcomeReceipt | None = None,
    ) -> "V001StageInterruptionReceipt":
        if solution_receipt is not None:
            _verify_stage_identity(attempt_intent, solution_receipt, "solution")
        if candidate_attempt_receipt is not None:
            _verify_stage_identity(attempt_intent, candidate_attempt_receipt, "candidate")
            if solution_receipt is None or (
                candidate_attempt_receipt.solution_receipt_sha256
                != solution_receipt.sha256
            ):
                raise ValueError("interruption candidate prefix differs")
        operation_id = {
            "solution": attempt_intent.solution_operation_id,
            "attempt_validation": attempt_intent.attempt_validation_operation_id,
            "evaluation": attempt_intent.evaluator_operation_id,
        }.get(stage, "invalid")
        return cls(
            task_seed_key_sha256=attempt_intent.task_seed_key_sha256,
            attempt_intent_sha256=attempt_intent.sha256,
            attempt_index=attempt_intent.attempt_index,
            stage=stage,
            interruption_kind=interruption_kind,
            operation_id=operation_id,
            operation_record_sha256=operation_record_sha256,
            evidence_artifact_sha256=evidence_artifact_sha256,
            reason_code=reason_code,
            completed_solution_receipt_sha256=(
                ZERO_SHA256 if solution_receipt is None else solution_receipt.sha256
            ),
            completed_candidate_attempt_receipt_sha256=(
                ZERO_SHA256
                if candidate_attempt_receipt is None
                else candidate_attempt_receipt.sha256
            ),
        )

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "V001StageInterruptionReceipt":
        return cls(**payload)

    @classmethod
    def from_bytes(
        cls, encoded: bytes, *, expected_sha256: str
    ) -> "V001StageInterruptionReceipt":
        return _typed_from_bytes(cls, encoded, expected_sha256=expected_sha256)


def _verify_stage_identity(
    intent: V001ExecutionAttemptIntent, stage: Any, label: str
) -> None:
    if (
        stage.task_seed_key_sha256 != intent.task_seed_key_sha256
        or stage.attempt_intent_sha256 != intent.sha256
        or stage.attempt_index != intent.attempt_index
    ):
        raise ValueError(f"{label} receipt execution attempt binding differs")


@dataclass(frozen=True)
class V001ExecutionAttemptReceipt(_ContentAddressed):
    attempt_intent: V001ExecutionAttemptIntent
    trunk_status: str
    environment_check: V001EnvironmentCheckReceipt
    solution: V001SolutionOperationReceipt | None
    candidate_attempt: V001AttemptOutcomeReceipt | None
    evaluation: V001EvaluationOperationReceipt | None
    interruption: V001StageInterruptionReceipt | None

    def __post_init__(self) -> None:
        if not isinstance(self.attempt_intent, V001ExecutionAttemptIntent):
            raise TypeError("typed execution attempt intent is required")
        if not isinstance(self.environment_check, V001EnvironmentCheckReceipt):
            raise TypeError("typed environment check is required")
        if self.trunk_status not in _ATTEMPT_STATUSES:
            raise ValueError("execution attempt status differs")
        for value, cls, label in (
            (self.solution, V001SolutionOperationReceipt, "solution"),
            (self.candidate_attempt, V001AttemptOutcomeReceipt, "candidate attempt"),
            (self.evaluation, V001EvaluationOperationReceipt, "evaluation"),
            (self.interruption, V001StageInterruptionReceipt, "interruption"),
        ):
            if value is not None and not isinstance(value, cls):
                raise TypeError(f"typed {label} receipt is required")
        intent = self.attempt_intent
        _verify_stage_identity(intent, self.environment_check, "environment")
        for value, label in (
            (self.solution, "solution"),
            (self.candidate_attempt, "candidate"),
            (self.evaluation, "evaluation"),
            (self.interruption, "interruption"),
        ):
            if value is not None:
                _verify_stage_identity(intent, value, label)
        if self.candidate_attempt is not None and (
            self.solution is None
            or self.candidate_attempt.solution_receipt_sha256 != self.solution.sha256
        ):
            raise ValueError("candidate attempt solution binding differs")
        if self.evaluation is not None and (
            self.candidate_attempt is None
            or self.evaluation.candidate_attempt_receipt_sha256
            != self.candidate_attempt.sha256
        ):
            raise ValueError("evaluation candidate binding differs")
        if self.solution is not None and (
            self.solution.operation_id != intent.solution_operation_id
        ):
            raise ValueError("solution operation id differs from execution intent")
        if self.evaluation is not None and (
            self.evaluation.operation_id != intent.evaluator_operation_id
        ):
            raise ValueError("evaluation operation id differs from execution intent")
        if self.interruption is not None:
            expected_interrupted_operation_id = {
                "solution": intent.solution_operation_id,
                "attempt_validation": intent.attempt_validation_operation_id,
                "evaluation": intent.evaluator_operation_id,
            }[self.interruption.stage]
            if (
                self.interruption.operation_id != expected_interrupted_operation_id
                or self.interruption.completed_solution_receipt_sha256
                != (ZERO_SHA256 if self.solution is None else self.solution.sha256)
                or self.interruption.completed_candidate_attempt_receipt_sha256
                != (
                    ZERO_SHA256
                    if self.candidate_attempt is None
                    else self.candidate_attempt.sha256
                )
            ):
                raise ValueError("interruption completed stage binding differs")
        expected = {
            "SUCCESS": ("VALID", True, "ACCEPTED", True, False),
            "SOLUTION_CONTRACT_REJECTED": (
                "VALID",
                True,
                "CONTRACT_REJECTED",
                False,
                False,
            ),
            "ENVIRONMENT_INVALID": (
                "ENVIRONMENT_INVALID",
                False,
                None,
                False,
                False,
            ),
        }
        if self.trunk_status in expected:
            env, has_solution, candidate_status, has_evaluation, has_interruption = expected[
                self.trunk_status
            ]
            observed = (
                self.environment_check.status,
                self.solution is not None,
                None if self.candidate_attempt is None else self.candidate_attempt.status,
                self.evaluation is not None,
                self.interruption is not None,
            )
            if observed != (
                env,
                has_solution,
                candidate_status,
                has_evaluation,
                has_interruption,
            ):
                raise ValueError("execution attempt stage artifacts differ")
        else:
            if (
                self.environment_check.status != "VALID"
                or self.evaluation is not None
                or self.interruption is None
            ):
                raise ValueError("execution attempt stage artifacts differ")

    @classmethod
    def create(
        cls,
        *,
        attempt_intent: V001ExecutionAttemptIntent,
        trunk_status: str,
        environment_check: V001EnvironmentCheckReceipt,
        solution: V001SolutionOperationReceipt | None = None,
        candidate_attempt: V001AttemptOutcomeReceipt | None = None,
        evaluation: V001EvaluationOperationReceipt | None = None,
        interruption: V001StageInterruptionReceipt | None = None,
    ) -> "V001ExecutionAttemptReceipt":
        return cls(
            attempt_intent=attempt_intent,
            trunk_status=trunk_status,
            environment_check=environment_check,
            solution=solution,
            candidate_attempt=candidate_attempt,
            evaluation=evaluation,
            interruption=interruption,
        )

    @property
    def task_seed_key_sha256(self) -> str:
        return self.attempt_intent.task_seed_key_sha256

    @property
    def attempt_index(self) -> int:
        return self.attempt_intent.attempt_index

    def to_trunk_receipt(
        self,
        *,
        trunk_intent: V001TrunkIntent,
        canonical_compile_contract: Any,
        compile_equivalence_receipt: Any,
    ) -> V001TrunkReceipt:
        if self.trunk_status == "ENVIRONMENT_INVALID":
            raise ValueError("environment-invalid attempt cannot seal a final shared trunk")
        if (
            trunk_intent.sha256 != self.attempt_intent.trunk_intent_sha256
            or canonical_compile_contract.sha256
            != self.attempt_intent.canonical_compile_contract_sha256
            or compile_equivalence_receipt.sha256
            != self.attempt_intent.compile_equivalence_receipt_sha256
        ):
            raise ValueError("execution outcome trunk parent binding differs")
        # Partial evidence remains in this typed receipt.  The legacy broad trunk
        # status intentionally contains no fabricated result hashes.
        solution_sha = (
            self.solution.solution_artifact_sha256
            if self.trunk_status in {"SUCCESS", "SOLUTION_CONTRACT_REJECTED"}
            else ZERO_SHA256
        )
        attempt_sha = (
            self.candidate_attempt.attempt_artifact_sha256
            if self.trunk_status in {"SUCCESS", "SOLUTION_CONTRACT_REJECTED"}
            else ZERO_SHA256
        )
        evaluation_sha = (
            self.evaluation.evaluation_artifact_sha256
            if self.trunk_status == "SUCCESS"
            else ZERO_SHA256
        )
        return V001TrunkReceipt.create(
            intent=trunk_intent,
            trunk_status=self.trunk_status,
            canonical_compile_contract=canonical_compile_contract,
            compile_equivalence_receipt=compile_equivalence_receipt,
            solution_artifact_sha256=solution_sha,
            attempt_artifact_sha256=attempt_sha,
            evaluation_artifact_sha256=evaluation_sha,
        )

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "V001ExecutionAttemptReceipt":
        payload = dict(payload)
        payload["attempt_intent"] = V001ExecutionAttemptIntent.from_payload(
            payload["attempt_intent"]
        )
        payload["environment_check"] = V001EnvironmentCheckReceipt.from_payload(
            payload["environment_check"]
        )
        payload["solution"] = _optional_payload(
            payload["solution"], V001SolutionOperationReceipt, "solution receipt"
        )
        payload["candidate_attempt"] = _optional_payload(
            payload["candidate_attempt"],
            V001AttemptOutcomeReceipt,
            "candidate attempt receipt",
        )
        payload["evaluation"] = _optional_payload(
            payload["evaluation"],
            V001EvaluationOperationReceipt,
            "evaluation receipt",
        )
        payload["interruption"] = _optional_payload(
            payload["interruption"],
            V001StageInterruptionReceipt,
            "interruption receipt",
        )
        return cls(**payload)

    @classmethod
    def from_bytes(
        cls, encoded: bytes, *, expected_sha256: str
    ) -> "V001ExecutionAttemptReceipt":
        return _typed_from_bytes(cls, encoded, expected_sha256=expected_sha256)


class FactorialOutcomeArchive:
    """Write-once attempt chain and terminal binding for shared v001 execution."""

    def __init__(self, root: Path, *, trunk_archive: Any) -> None:
        self.root = lexical_absolute(root)
        self.trunk_archive = trunk_archive

    def _object_path(self, sha256: str) -> Path:
        return self.root / "objects" / "attempts" / f"{sha256}.json"

    def _attempt_binding_path(self, key_sha256: str, attempt_index: int) -> Path:
        return self.root / "bindings" / "attempts" / key_sha256 / f"{attempt_index:04d}.json"

    def _terminal_binding_path(self, key_sha256: str) -> Path:
        return self.root / "bindings" / "terminal" / f"{key_sha256}.json"

    @staticmethod
    def _binding_bytes(
        *, key_sha256: str, attempt_index: int, receipt_sha256: str, terminal: bool
    ) -> bytes:
        return _canonical_bytes(
            {
                "schema_version": 1,
                "kind": "terminal" if terminal else "attempt",
                "task_seed_key_sha256": key_sha256,
                "attempt_index": attempt_index,
                "receipt_sha256": receipt_sha256,
            }
        )

    def _validate_trunk_parents(self, receipt: V001ExecutionAttemptReceipt) -> None:
        key_sha = receipt.task_seed_key_sha256
        intent = self.trunk_archive.load_intent(key_sha)
        contract = self.trunk_archive.load_canonical_compile(key_sha)
        equivalence = self.trunk_archive.load_equivalence(key_sha)
        attempt_intent = receipt.attempt_intent
        if (
            attempt_intent.trunk_intent_sha256 != intent.sha256
            or attempt_intent.canonical_compile_contract_sha256 != contract.sha256
            or attempt_intent.compile_equivalence_receipt_sha256 != equivalence.sha256
            or contract.task_seed_key_sha256 != key_sha
            or equivalence.task_seed_key_sha256 != key_sha
        ):
            raise ValueError("v001 execution outcome trunk parent binding differs")

    def store_attempt(self, receipt: V001ExecutionAttemptReceipt) -> Path:
        if not isinstance(receipt, V001ExecutionAttemptReceipt):
            raise TypeError("typed v001 execution attempt receipt is required")
        if self.has_terminal_outcome(receipt.task_seed_key_sha256):
            raise ValueError("v001 task/seed outcome is already terminal")
        self._validate_trunk_parents(receipt)
        if receipt.attempt_index == 1:
            if receipt.attempt_intent.previous_attempt_receipt_sha256 != ZERO_SHA256:
                raise ValueError("first v001 execution attempt parent differs")
        else:
            previous = self.load_attempt(
                receipt.task_seed_key_sha256, receipt.attempt_index - 1
            )
            if (
                receipt.attempt_intent.previous_attempt_receipt_sha256
                != previous.sha256
            ):
                raise ValueError("v001 execution retry parent differs")
            if previous.trunk_status != "ENVIRONMENT_INVALID":
                raise ValueError("only environment-invalid attempt may be retried")
            if (
                previous.attempt_intent.environment_binding_sha256
                == receipt.attempt_intent.environment_binding_sha256
            ):
                raise ValueError("retry environment binding must change")
        try:
            write_once_safe_regular_file(
                self._object_path(receipt.sha256),
                receipt.canonical_bytes,
                label="factorial outcome attempt object",
                temporary_suffix=".attempt.tmp",
            )
            return write_once_safe_regular_file(
                self._attempt_binding_path(
                    receipt.task_seed_key_sha256, receipt.attempt_index
                ),
                self._binding_bytes(
                    key_sha256=receipt.task_seed_key_sha256,
                    attempt_index=receipt.attempt_index,
                    receipt_sha256=receipt.sha256,
                    terminal=False,
                ),
                label="factorial outcome attempt binding",
                temporary_suffix=".attempt-binding.tmp",
            )
        except ValueError as exc:
            if "refusing to overwrite" in str(exc):
                raise ValueError("factorial outcome attempt identity binding differs") from exc
            raise

    def _load_bound(self, path: Path, *, terminal: bool) -> V001ExecutionAttemptReceipt:
        encoded = read_safe_regular_file(path, label="factorial outcome binding")
        payload = _decode(encoded, label="factorial outcome binding")
        _exact_fields(
            payload,
            {
                "schema_version",
                "kind",
                "task_seed_key_sha256",
                "attempt_index",
                "receipt_sha256",
            },
            "factorial outcome binding",
        )
        if payload["schema_version"] != 1 or payload["kind"] != (
            "terminal" if terminal else "attempt"
        ):
            raise ValueError("factorial outcome binding differs")
        receipt_sha = _sha(
            payload["receipt_sha256"], "outcome receipt sha256", allow_zero=False
        )
        receipt = V001ExecutionAttemptReceipt.from_bytes(
            read_safe_regular_file(
                self._object_path(receipt_sha), label="factorial outcome attempt object"
            ),
            expected_sha256=receipt_sha,
        )
        if (
            receipt.task_seed_key_sha256 != payload["task_seed_key_sha256"]
            or receipt.attempt_index != payload["attempt_index"]
        ):
            raise ValueError("factorial outcome object binding differs")
        self._validate_trunk_parents(receipt)
        return receipt

    def load_attempt(
        self, key_sha256: str, attempt_index: int
    ) -> V001ExecutionAttemptReceipt:
        _sha(key_sha256, "task/seed key sha256", allow_zero=False)
        if type(attempt_index) is not int or not 1 <= attempt_index <= _MAX_ATTEMPT_INDEX:
            raise ValueError("v001 execution attempt index differs")
        receipt = self._load_bound(
            self._attempt_binding_path(key_sha256, attempt_index), terminal=False
        )
        if (
            receipt.task_seed_key_sha256 != key_sha256
            or receipt.attempt_index != attempt_index
        ):
            raise ValueError("factorial outcome requested attempt binding differs")
        if attempt_index > 1:
            previous = self.load_attempt(key_sha256, attempt_index - 1)
            if (
                receipt.attempt_intent.previous_attempt_receipt_sha256
                != previous.sha256
                or previous.trunk_status != "ENVIRONMENT_INVALID"
                or previous.attempt_intent.environment_binding_sha256
                == receipt.attempt_intent.environment_binding_sha256
            ):
                raise ValueError("factorial outcome retry chain differs")
        elif receipt.attempt_intent.previous_attempt_receipt_sha256 != ZERO_SHA256:
            raise ValueError("factorial outcome first attempt parent differs")
        return receipt

    def has_terminal_outcome(self, key_sha256: str) -> bool:
        _sha(key_sha256, "task/seed key sha256", allow_zero=False)
        return safe_regular_file_exists(
            self._terminal_binding_path(key_sha256),
            label="factorial outcome terminal binding",
        )

    def next_attempt_index(self, key_sha256: str) -> int:
        if self.has_terminal_outcome(key_sha256):
            raise ValueError("v001 task/seed outcome is already terminal")
        index = 1
        while safe_regular_file_exists(
            self._attempt_binding_path(key_sha256, index),
            label="factorial outcome attempt binding",
        ):
            index += 1
            if index > _MAX_ATTEMPT_INDEX:
                raise ValueError("v001 execution attempt limit exceeded")
        if index > 1 and self.load_attempt(key_sha256, index - 1).trunk_status != (
            "ENVIRONMENT_INVALID"
        ):
            raise ValueError("last v001 execution attempt is terminal")
        return index

    def seal_terminal(self, receipt: V001ExecutionAttemptReceipt) -> Path:
        if receipt.trunk_status not in _TERMINAL_ATTEMPT_STATUSES:
            raise ValueError("environment-invalid attempt cannot seal terminal outcome")
        stored = self.load_attempt(receipt.task_seed_key_sha256, receipt.attempt_index)
        if stored != receipt:
            raise ValueError("terminal outcome attempt differs from stored attempt")
        try:
            return write_once_safe_regular_file(
                self._terminal_binding_path(receipt.task_seed_key_sha256),
                self._binding_bytes(
                    key_sha256=receipt.task_seed_key_sha256,
                    attempt_index=receipt.attempt_index,
                    receipt_sha256=receipt.sha256,
                    terminal=True,
                ),
                label="factorial outcome terminal binding",
                temporary_suffix=".terminal-binding.tmp",
            )
        except ValueError as exc:
            if "refusing to overwrite" in str(exc):
                raise ValueError("factorial outcome terminal binding differs") from exc
            raise

    def load_terminal(self, key_sha256: str) -> V001ExecutionAttemptReceipt:
        receipt = self._load_bound(
            self._terminal_binding_path(key_sha256), terminal=True
        )
        if (
            receipt.task_seed_key_sha256 != key_sha256
            or receipt.trunk_status not in _TERMINAL_ATTEMPT_STATUSES
        ):
            raise ValueError("factorial outcome terminal status differs")
        stored = self.load_attempt(key_sha256, receipt.attempt_index)
        if stored != receipt:
            raise ValueError("factorial outcome terminal attempt binding differs")
        return receipt


__all__ = [
    "FactorialOutcomeArchive",
    "V001AttemptOutcomeReceipt",
    "V001EnvironmentCheckReceipt",
    "V001EvaluationOperationReceipt",
    "V001ExecutionAttemptIntent",
    "V001ExecutionAttemptReceipt",
    "V001SolutionOperationReceipt",
    "V001StageInterruptionReceipt",
]
