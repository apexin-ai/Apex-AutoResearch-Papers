from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import pytest

from optimization_lab.harness_builder.factorial_outcomes import (
    FactorialOutcomeArchive,
    V001AttemptOutcomeReceipt,
    V001EnvironmentCheckReceipt,
    V001EvaluationOperationReceipt,
    V001ExecutionAttemptIntent,
    V001ExecutionAttemptReceipt,
    V001SolutionOperationReceipt,
    V001StageInterruptionReceipt,
)
from optimization_lab.harness_builder.factorial_trunk import (
    ZERO_SHA256,
    TaskSeedKey,
    V001TrunkIntent,
)


def _sha(label: str) -> str:
    return hashlib.sha256(label.encode()).hexdigest()


def _key() -> TaskSeedKey:
    return TaskSeedKey(
        suite="agenthpobench",
        instance_id="agenthpobench:task-01",
        seed=2026081201,
        task_binding_sha256=_sha("task"),
        factorial_contract_sha256=_sha("factorial"),
        context_binding_sha256=_sha("context"),
    )


class _TrunkArchiveStub:
    def __init__(self, key: TaskSeedKey) -> None:
        self.intent = V001TrunkIntent.create(key)
        self.contract = SimpleNamespace(
            sha256=_sha("compile-contract"),
            task_seed_key_sha256=key.sha256,
            context_binding_sha256=key.context_binding_sha256,
            decision_sha256=_sha("decision"),
            operational_fingerprint=_sha("fingerprint"),
            compiled_harness_semantic_sha256=_sha("semantic"),
            solution_prompt_sha256=_sha("prompt"),
        )
        self.equivalence = SimpleNamespace(
            sha256=_sha("equivalence"),
            task_seed_key_sha256=key.sha256,
            canonical_compile_contract_sha256=self.contract.sha256,
            canonical_compiled_harness_semantic_sha256=(
                self.contract.compiled_harness_semantic_sha256
            ),
        )

    def load_intent(self, key_sha256: str):
        assert key_sha256 == self.intent.task_seed_key_sha256
        return self.intent

    def load_canonical_compile(self, key_sha256: str):
        assert key_sha256 == self.intent.task_seed_key_sha256
        return self.contract

    def load_equivalence(self, key_sha256: str):
        assert key_sha256 == self.intent.task_seed_key_sha256
        return self.equivalence


def _attempt_intent(
    stub: _TrunkArchiveStub,
    *,
    attempt_index: int = 1,
    previous: str = ZERO_SHA256,
    environment: str = "environment-1",
) -> V001ExecutionAttemptIntent:
    return V001ExecutionAttemptIntent.create(
        trunk_intent=stub.intent,
        canonical_compile_contract=stub.contract,
        compile_equivalence_receipt=stub.equivalence,
        attempt_index=attempt_index,
        previous_attempt_receipt_sha256=previous,
        environment_binding_sha256=_sha(environment),
    )


def _valid_environment(
    intent: V001ExecutionAttemptIntent,
) -> V001EnvironmentCheckReceipt:
    return V001EnvironmentCheckReceipt.create(
        attempt_intent=intent,
        status="VALID",
        evidence_artifact_sha256=_sha(f"env-valid:{intent.attempt_index}"),
    )


def _successful_attempt(
    intent: V001ExecutionAttemptIntent,
) -> V001ExecutionAttemptReceipt:
    environment = _valid_environment(intent)
    solution = V001SolutionOperationReceipt.create(
        attempt_intent=intent,
        operation_record_sha256=_sha(f"solution-op:{intent.attempt_index}"),
        raw_response_artifact_sha256=_sha(f"raw:{intent.attempt_index}"),
        solution_artifact_sha256=_sha(f"solution:{intent.attempt_index}"),
    )
    candidate = V001AttemptOutcomeReceipt.create(
        attempt_intent=intent,
        solution_receipt=solution,
        status="ACCEPTED",
        attempt_artifact_sha256=_sha(f"attempt:{intent.attempt_index}"),
        contract_evidence_sha256=_sha(f"contract:{intent.attempt_index}"),
        candidate_artifact_sha256=_sha(f"candidate:{intent.attempt_index}"),
    )
    evaluation = V001EvaluationOperationReceipt.create(
        attempt_intent=intent,
        candidate_attempt_receipt=candidate,
        status="VALID",
        operation_record_sha256=_sha(f"evaluation-op:{intent.attempt_index}"),
        evaluation_artifact_sha256=_sha(f"evaluation:{intent.attempt_index}"),
        score_observation_sha256=_sha(f"score:{intent.attempt_index}"),
    )
    return V001ExecutionAttemptReceipt.create(
        attempt_intent=intent,
        trunk_status="SUCCESS",
        environment_check=environment,
        solution=solution,
        candidate_attempt=candidate,
        evaluation=evaluation,
    )


def test_typed_success_round_trips_and_projects_to_shared_trunk() -> None:
    key = _key()
    stub = _TrunkArchiveStub(key)
    attempt = _successful_attempt(_attempt_intent(stub))

    restored = V001ExecutionAttemptReceipt.from_bytes(
        attempt.canonical_bytes, expected_sha256=attempt.sha256
    )
    assert restored == attempt
    trunk = restored.to_trunk_receipt(
        trunk_intent=stub.intent,
        canonical_compile_contract=stub.contract,
        compile_equivalence_receipt=stub.equivalence,
    )
    assert trunk.trunk_status == "SUCCESS"
    assert trunk.solution_artifact_sha256 == restored.solution.solution_artifact_sha256
    assert trunk.attempt_artifact_sha256 == restored.candidate_attempt.attempt_artifact_sha256
    assert trunk.evaluation_artifact_sha256 == restored.evaluation.evaluation_artifact_sha256


def test_environment_invalid_is_attempt_scoped_and_retryable(tmp_path: Path) -> None:
    key = _key()
    stub = _TrunkArchiveStub(key)
    archive = FactorialOutcomeArchive(tmp_path / "outcomes", trunk_archive=stub)
    first_intent = _attempt_intent(stub)
    environment = V001EnvironmentCheckReceipt.create(
        attempt_intent=first_intent,
        status="ENVIRONMENT_INVALID",
        evidence_artifact_sha256=_sha("missing-runtime"),
        reason_code="provider_runtime_unavailable",
    )
    invalid = V001ExecutionAttemptReceipt.create(
        attempt_intent=first_intent,
        trunk_status="ENVIRONMENT_INVALID",
        environment_check=environment,
    )
    archive.store_attempt(invalid)

    assert archive.load_attempt(key.sha256, 1) == invalid
    assert archive.has_terminal_outcome(key.sha256) is False
    assert archive.next_attempt_index(key.sha256) == 2
    with pytest.raises(ValueError, match="cannot seal"):
        archive.seal_terminal(invalid)

    second_intent = _attempt_intent(
        stub,
        attempt_index=2,
        previous=invalid.sha256,
        environment="environment-2",
    )
    success = _successful_attempt(second_intent)
    archive.store_attempt(success)
    archive.seal_terminal(success)
    assert archive.load_terminal(key.sha256) == success
    assert archive.load_attempt(key.sha256, 1) == invalid


def test_environment_retry_requires_new_environment_binding(tmp_path: Path) -> None:
    key = _key()
    stub = _TrunkArchiveStub(key)
    archive = FactorialOutcomeArchive(tmp_path / "outcomes", trunk_archive=stub)
    first_intent = _attempt_intent(stub)
    invalid = V001ExecutionAttemptReceipt.create(
        attempt_intent=first_intent,
        trunk_status="ENVIRONMENT_INVALID",
        environment_check=V001EnvironmentCheckReceipt.create(
            attempt_intent=first_intent,
            status="ENVIRONMENT_INVALID",
            evidence_artifact_sha256=_sha("invalid"),
            reason_code="runtime_invalid",
        ),
    )
    archive.store_attempt(invalid)
    repeated = _successful_attempt(
        _attempt_intent(
            stub,
            attempt_index=2,
            previous=invalid.sha256,
            environment="environment-1",
        )
    )
    with pytest.raises(ValueError, match="environment binding must change"):
        archive.store_attempt(repeated)


def test_stage_interruption_preserves_completed_prefix_without_fake_outputs() -> None:
    key = _key()
    stub = _TrunkArchiveStub(key)
    intent = _attempt_intent(stub)
    environment = _valid_environment(intent)
    solution = V001SolutionOperationReceipt.create(
        attempt_intent=intent,
        operation_record_sha256=_sha("solution-operation"),
        raw_response_artifact_sha256=_sha("raw"),
        solution_artifact_sha256=_sha("solution"),
    )
    candidate = V001AttemptOutcomeReceipt.create(
        attempt_intent=intent,
        solution_receipt=solution,
        status="ACCEPTED",
        attempt_artifact_sha256=_sha("attempt"),
        contract_evidence_sha256=_sha("contract"),
        candidate_artifact_sha256=_sha("candidate"),
    )
    interruption = V001StageInterruptionReceipt.create(
        attempt_intent=intent,
        stage="evaluation",
        interruption_kind="STARTED_WITHOUT_ARTIFACT",
        operation_record_sha256=_sha("abandoned-evaluator-operation"),
        evidence_artifact_sha256=_sha("interruption-evidence"),
        reason_code="session_terminated",
        solution_receipt=solution,
        candidate_attempt_receipt=candidate,
    )
    interrupted = V001ExecutionAttemptReceipt.create(
        attempt_intent=intent,
        trunk_status="OPERATION_INTERRUPTED",
        environment_check=environment,
        solution=solution,
        candidate_attempt=candidate,
        interruption=interruption,
    )

    assert interrupted.solution is not None
    assert interrupted.candidate_attempt is not None
    assert interrupted.evaluation is None
    assert interrupted.interruption.stage == "evaluation"
    trunk = interrupted.to_trunk_receipt(
        trunk_intent=stub.intent,
        canonical_compile_contract=stub.contract,
        compile_equivalence_receipt=stub.equivalence,
    )
    # The typed receipt retains the completed prefix.  The legacy broad trunk
    # projection does not pretend those prefix artifacts are a completed result.
    assert trunk.trunk_status == "OPERATION_INTERRUPTED"
    assert trunk.solution_artifact_sha256 == ZERO_SHA256
    assert trunk.attempt_artifact_sha256 == ZERO_SHA256
    assert trunk.evaluation_artifact_sha256 == ZERO_SHA256


def test_interruption_rejects_a_fake_evaluation_artifact() -> None:
    key = _key()
    stub = _TrunkArchiveStub(key)
    successful = _successful_attempt(_attempt_intent(stub))
    with pytest.raises(ValueError, match="stage artifacts differ"):
        V001ExecutionAttemptReceipt.create(
            attempt_intent=successful.attempt_intent,
            trunk_status="OPERATION_INTERRUPTED",
            environment_check=successful.environment_check,
            solution=successful.solution,
            candidate_attempt=successful.candidate_attempt,
            evaluation=successful.evaluation,
            interruption=V001StageInterruptionReceipt.create(
                attempt_intent=successful.attempt_intent,
                stage="evaluation",
                interruption_kind="STARTED_WITHOUT_ARTIFACT",
                operation_record_sha256=_sha("interrupted-op"),
                evidence_artifact_sha256=_sha("interruption"),
                reason_code="lost_result",
                solution_receipt=successful.solution,
                candidate_attempt_receipt=successful.candidate_attempt,
            ),
        )


def test_contract_rejection_is_typed_and_has_no_evaluator() -> None:
    key = _key()
    stub = _TrunkArchiveStub(key)
    intent = _attempt_intent(stub)
    environment = _valid_environment(intent)
    solution = V001SolutionOperationReceipt.create(
        attempt_intent=intent,
        operation_record_sha256=_sha("solution-op"),
        raw_response_artifact_sha256=_sha("raw"),
        solution_artifact_sha256=_sha("solution"),
    )
    rejected = V001AttemptOutcomeReceipt.create(
        attempt_intent=intent,
        solution_receipt=solution,
        status="CONTRACT_REJECTED",
        attempt_artifact_sha256=_sha("rejection-receipt"),
        contract_evidence_sha256=_sha("contract-evidence"),
    )
    outcome = V001ExecutionAttemptReceipt.create(
        attempt_intent=intent,
        trunk_status="SOLUTION_CONTRACT_REJECTED",
        environment_check=environment,
        solution=solution,
        candidate_attempt=rejected,
    )
    assert outcome.evaluation is None
    assert outcome.to_trunk_receipt(
        trunk_intent=stub.intent,
        canonical_compile_contract=stub.contract,
        compile_equivalence_receipt=stub.equivalence,
    ).trunk_status == "SOLUTION_CONTRACT_REJECTED"


def test_archive_revalidates_requested_identity_and_retry_chain(tmp_path: Path) -> None:
    key = _key()
    stub = _TrunkArchiveStub(key)
    archive = FactorialOutcomeArchive(tmp_path / "outcomes", trunk_archive=stub)
    intent = _attempt_intent(stub)
    invalid = V001ExecutionAttemptReceipt.create(
        attempt_intent=intent,
        trunk_status="ENVIRONMENT_INVALID",
        environment_check=V001EnvironmentCheckReceipt.create(
            attempt_intent=intent,
            status="ENVIRONMENT_INVALID",
            evidence_artifact_sha256=_sha("invalid"),
            reason_code="runtime_invalid",
        ),
    )
    archive.store_attempt(invalid)

    binding = archive.root / "bindings" / "attempts" / key.sha256 / "0001.json"
    payload = json.loads(binding.read_bytes())
    payload["attempt_index"] = 2
    binding.write_bytes(
        (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    )
    with pytest.raises(ValueError, match="object binding"):
        archive.load_attempt(key.sha256, 1)


def test_success_rejects_mismatched_operation_identity() -> None:
    key = _key()
    stub = _TrunkArchiveStub(key)
    successful = _successful_attempt(_attempt_intent(stub))
    with pytest.raises(ValueError, match="operation id differs"):
        replace(
            successful.solution,
            operation_id=f"factorial-v001:{key.sha256}:another-solution",
        )
