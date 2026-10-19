from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Protocol

from optimization_lab.generation import GenerationResult
from optimization_lab.registry import ExperimentRegistry

from ._safe_artifacts import (
    ensure_safe_directory,
    lexical_absolute,
    read_safe_regular_file,
    safe_regular_file_exists,
    write_once_safe_regular_file,
)
from .compile_receipts import CompileReceiptArchive, HarnessCompileReceipt
from .evaluation import EvaluationBackend, NormalizedEvaluation, environment_invalid
from .events import OperationStateError, ResourceVector
from .model_gateway import GatewayGenerator, IsolatedModelGateway
from .meta_prior import BuilderMetaPrior
from .contract_compatibility import codec_capability_payload
from .operators import (
    CrossInstanceMemoryGrant,
    HarnessContext,
    PublicAttempt,
    TrustedOperatorRegistry,
)
from .runtime import HarnessRuntime
from .schema import BuilderVariant, HarnessDecision
from .solutions import (
    SolutionArchive,
    SolutionArtifact,
    SolutionContractError,
)


class SolutionCodec(Protocol):
    output_mode: str

    def parse(self, raw_response: str) -> SolutionArtifact: ...


class EnvironmentInvalid(RuntimeError):
    """The candidate remains undecided because trusted evaluation is unavailable."""


@dataclass(frozen=True)
class CellRunResult:
    cell_id: str
    attempts: tuple[PublicAttempt, ...]
    decisions: tuple[HarnessDecision | None, ...]
    sealed: bool

    @property
    def best_score(self) -> float | None:
        scores = [attempt.score for attempt in self.attempts if attempt.correct]
        return max(scores) if scores else None


def _canonical_bytes(payload: dict[str, object]) -> bytes:
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


def _value_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


_PLANNER_REJECTION_REASONS = {
    "invalid_harness_decision",
    "no_operational_change",
    "harness_compile_rejected",
    "missing_frozen_initial_harness",
    "wide_harness_previous_receipt_missing",
    "wide_harness_change_incomplete",
    "wide_harness_lineage_history_missing",
    "wide_harness_fingerprint_reused",
    "targeted_harness_previous_decision_missing",
    "targeted_harness_change_missing",
    "initial_contract_compatibility_required",
    "contract_failure_compatibility_recovery_required",
    "artifact_contract_capability_missing",
    "contract_compatibility_tool_missing",
    "contract_compatibility_reference_required",
    "cross_instance_memory_not_authorized",
    "cross_instance_memory_empty",
    "cross_instance_memory_source_excluded",
    "builder_meta_prior_not_authorized",
    "meta_policy_component_contract_invalid",
    "meta_policy_component_out_of_bounds",
}


def _write_once(path: Path, content: bytes) -> None:
    write_once_safe_regular_file(
        path,
        content,
        label="sealed round",
        temporary_suffix=".round.tmp",
    )


class HarnessBuilderCellRunner:
    """Execute or recover one fixed instance/arm cell for v001-v008."""

    def __init__(
        self,
        *,
        artifact_root: Path,
        cell_id: str,
        instance_id: str,
        suite: str,
        task_card: str,
        reference_artifact: str,
        variant: BuilderVariant,
        operator_registry: TrustedOperatorRegistry,
        model_gateway: IsolatedModelGateway,
        model: str,
        solution_codec: SolutionCodec,
        evaluator: EvaluationBackend,
        cross_instance_records: tuple[dict[str, object], ...] = (),
        cross_instance_memory_grant: CrossInstanceMemoryGrant | None = None,
        stream_index: int | None = None,
        builder_meta_prior: BuilderMetaPrior | None = None,
        rounds: int = 8,
        operation_prefix: str | None = None,
    ) -> None:
        if not 1 <= rounds <= 8:
            raise ValueError("cell runner rounds must be between one and eight")
        self.artifact_root = ensure_safe_directory(
            lexical_absolute(artifact_root), label="Harness cell artifact root"
        )
        self.rounds_root = self.artifact_root / "rounds"
        self.cell_id = cell_id
        self.instance_id = instance_id
        self.suite = suite
        self.task_card = task_card
        self.reference_artifact = reference_artifact
        self.variant = variant
        self.operator_registry = operator_registry
        self.model_gateway = model_gateway
        self.model = model
        self.solution_codec = solution_codec
        self.evaluator = evaluator
        self.cross_instance_records = cross_instance_records
        self.cross_instance_memory_grant = cross_instance_memory_grant
        self.stream_index = stream_index
        self.builder_meta_prior = builder_meta_prior
        self.rounds = rounds
        self.operation_prefix = operation_prefix or cell_id
        self.solutions = SolutionArchive(
            self.artifact_root / "solutions", cell_id=cell_id
        )
        self.compile_receipts = CompileReceiptArchive(
            self.artifact_root / "compiled"
        )
        self.registry = ExperimentRegistry(
            self.artifact_root,
            integrity_mode=(
                "hash_chain_v1"
                if variant.adaptation_policy
                in {"targeted_any_change_v1", "wide_all_fields_recompile_v1"}
                else "legacy"
            ),
        )

    def run(self) -> CellRunResult:
        attempts: list[PublicAttempt] = []
        decisions: list[HarnessDecision | None] = []
        for round_index in range(1, self.rounds + 1):
            version = f"v{round_index:03d}"
            restored = self._load_round(version)
            if restored is not None:
                decision, attempt = restored
                decisions.append(decision)
                attempts.append(attempt)
                continue

            accepted_decisions = [decision for decision in decisions if decision is not None]
            accepted_prefix = self.compile_receipts.verified_prefix_before(
                version,
                cell_id=self.cell_id,
                suite=self.suite,
                instance_id=self.instance_id,
                variant_id=self.variant.variant_id,
                adaptation_policy=self.variant.adaptation_policy,
            )
            if accepted_decisions and (
                not accepted_prefix
                or accepted_prefix[-1]
                != accepted_decisions[-1].operational_fingerprint
            ):
                raise ValueError("accepted Harness lineage differs from its receipt prefix")
            previous_receipt_sha256, previous_receipt_decision = (
                self._latest_compile_binding(round_index)
            )
            previous_decision = (
                accepted_decisions[-1] if accepted_decisions else None
            )
            if (
                previous_receipt_decision is not None
                and previous_decision != previous_receipt_decision
            ):
                raise ValueError("previous compile receipt decision binding differs")

            context = HarnessContext(
                instance_id=self.instance_id,
                suite=self.suite,
                round_index=round_index,
                task_card=self.task_card,
                reference_artifact_id="reference",
                reference_artifact=self.reference_artifact,
                attempts=tuple(attempts),
                cross_instance_records=self.cross_instance_records,
                cross_instance_memory_grant=self.cross_instance_memory_grant,
                stream_index=self.stream_index,
                builder_meta_prior=self.builder_meta_prior,
                public_observations={
                    "artifact_contract": codec_capability_payload(self.solution_codec)
                },
            )
            planner_kind = (
                "sham_planner_call"
                if self.variant.freeze_after_initial and round_index > 1
                else "planner_call"
            )
            interruption = self._operation_interruption(
                version=version,
                planner_kind=planner_kind,
            )
            if interruption is not None:
                phase = interruption["phase"]
                state = interruption["state"]
                encoded_interruption = _canonical_bytes(interruption)
                attempt = PublicAttempt(
                    attempt_id=version,
                    artifact_sha256=hashlib.sha256(encoded_interruption).hexdigest(),
                    artifact_text=f"{phase} operation {state}",
                    correct=False,
                    score=None,
                    outcome=f"{phase}_operation_{state}",
                    structural_signature=hashlib.sha256(
                        f"operation_interruption:{phase}:{state}".encode("utf-8")
                    ).hexdigest(),
                    public_summary=(
                        f"trusted {phase} operation is {state}; its committed budget "
                        "remains charged and the operation was not retried"
                    ),
                )
                interruption_receipt: HarnessCompileReceipt | None = None
                interruption_decision: HarnessDecision | None = None
                if phase in {"solution", "evaluator"}:
                    interruption_receipt, interruption_decision = (
                        self._verify_compile_version(
                            version=version,
                            attempts=tuple(attempts),
                            prior_operational_fingerprints=accepted_prefix,
                        )
                    )
                self._seal_round(
                    version=version,
                    decision=interruption_decision,
                    attempt=attempt,
                    compiled=None,
                    compile_receipt_sha256=(
                        None
                        if interruption_receipt is None
                        else interruption_receipt.sha256
                    ),
                    evaluation=None,
                    planner_rejection=None,
                    operation_interruption=interruption,
                )
                decisions.append(interruption_decision)
                attempts.append(attempt)
                continue
            planner = GatewayGenerator(
                gateway=self.model_gateway,
                operation_id=f"{self.operation_prefix}:{planner_kind}:{version}",
                cell_id=self.cell_id,
                operation_kind=planner_kind,
                output_mode="plain_text",
            )
            solution_generator = GatewayGenerator(
                gateway=self.model_gateway,
                operation_id=f"{self.operation_prefix}:solution_call:{version}",
                cell_id=self.cell_id,
                operation_kind="solution_call",
                output_mode=self.solution_codec.output_mode,
            )

            def solution_generator_factory(stage_id: str) -> GatewayGenerator:
                return GatewayGenerator(
                    gateway=self.model_gateway,
                    operation_id=(
                        f"{self.operation_prefix}:solution_call:{version}:{stage_id}"
                    ),
                    cell_id=self.cell_id,
                    operation_kind="solution_call",
                    output_mode=self.solution_codec.output_mode,
                )

            runtime = HarnessRuntime(
                operator_registry=self.operator_registry,
                planner=planner,
                solution_generator=solution_generator,
                model=self.model,
                solution_generator_factory=solution_generator_factory,
            )
            planned = runtime.plan_and_compile(
                variant=self.variant,
                context=context,
                previous_decision=previous_decision,
                previous_compile_receipt_sha256=previous_receipt_sha256,
                prior_operational_fingerprints=tuple(
                    decision.operational_fingerprint
                    for decision in accepted_decisions
                ),
                frozen_decision=decisions[0] if decisions and decisions[0] is not None else None,
            )
            if planned.planner_rejection_reason is not None:
                raw_planner = planned.planner_result.raw_response
                raw_sha = hashlib.sha256(raw_planner.encode("utf-8")).hexdigest()
                reason = planned.planner_rejection_reason
                attempt = PublicAttempt(
                    attempt_id=version,
                    artifact_sha256=raw_sha,
                    artifact_text="planner-contract-rejected Harness decision",
                    correct=False,
                    score=None,
                    outcome="planner_contract_rejected",
                    structural_signature=hashlib.sha256(
                        f"planner_contract_rejected:{reason}".encode("utf-8")
                    ).hexdigest(),
                    public_summary=(
                        "planner decision failed the public Harness contract: " + reason
                    ),
                )
                self._seal_round(
                    version=version,
                    decision=None,
                    attempt=attempt,
                    compiled=None,
                    compile_receipt_sha256=None,
                    evaluation=None,
                    planner_rejection={
                        "reason_code": reason,
                        "raw_response_sha256": raw_sha,
                    },
                    operation_interruption=None,
                )
                decisions.append(None)
                attempts.append(attempt)
                continue
            decision = planned.decision
            compiled = planned.compiled_harness
            if decision is None or compiled is None:
                raise RuntimeError("accepted Harness round is missing runtime artifacts")
            receipt = HarnessCompileReceipt.create(
                cell_id=self.cell_id,
                suite=self.suite,
                instance_id=self.instance_id,
                variant_id=self.variant.variant_id,
                version=version,
                adaptation_policy=self.variant.adaptation_policy,
                previous_receipt_sha256=previous_receipt_sha256,
                previous_decision_sha256=(
                    "0" * 64 if previous_decision is None else previous_decision.sha256
                ),
                compiled=compiled,
                decision=decision,
                previous_decision=previous_decision,
                prior_operational_fingerprints=accepted_prefix,
            )
            self.compile_receipts.store_trusted_version(
                receipt=receipt,
                decision=decision,
                compiled=compiled,
                previous_decision=previous_decision,
                prior_operational_fingerprints=accepted_prefix,
            )
            self.registry.append(
                "hb_harness_compiled",
                {
                    "cell_id": self.cell_id,
                    "instance_id": self.instance_id,
                    "variant_id": self.variant.variant_id,
                    "version": version,
                    "receipt_sha256": receipt.sha256,
                    "decision_sha256": decision.sha256,
                    "component_catalog_sha256": receipt.component_catalog_sha256,
                    "adaptation_policy": receipt.adaptation_policy,
                    "builder_meta_prior_sha256": receipt.builder_meta_prior_sha256,
                },
                event_id=(
                    "hb-harness-compiled:"
                    + hashlib.sha256((self.cell_id + ":" + version).encode()).hexdigest()
                ),
            )
            solution_result, solution_stage_results = (
                runtime.generate_solution_with_stages(compiled)
            )
            raw_solution = solution_result.raw_response
            try:
                artifact = self.solution_codec.parse(raw_solution)
            except SolutionContractError as exc:
                raw_sha = hashlib.sha256(raw_solution.encode("utf-8")).hexdigest()
                reason = exc.reason_code
                attempt = PublicAttempt(
                    attempt_id=version,
                    artifact_sha256=raw_sha,
                    artifact_text="contract-rejected candidate",
                    correct=False,
                    score=None,
                    outcome="contract_rejected",
                    structural_signature=hashlib.sha256(
                        f"contract_rejected:{reason}".encode("utf-8")
                    ).hexdigest(),
                    public_summary=(
                        "candidate artifact failed the public solution contract: "
                        + reason
                    ),
                )
                evaluation = None
            else:
                stored = self.solutions.store(version, artifact)
                evaluation = self._evaluate(version, stored.artifact_path)
                if environment_invalid(evaluation):
                    raise EnvironmentInvalid(
                        "trusted evaluator returned environment_invalid; round remains unsealed"
                    )
                attempt = PublicAttempt(
                    attempt_id=version,
                    artifact_sha256=artifact.sha256,
                    artifact_text=artifact.text,
                    correct=evaluation.correct,
                    score=evaluation.score if evaluation.correct else None,
                    outcome=evaluation.status,
                    structural_signature=artifact.structural_signature,
                    public_summary=json.dumps(
                        evaluation.public_feedback,
                        ensure_ascii=False,
                        sort_keys=True,
                    )[:4000],
                )

            self._seal_round(
                version=version,
                decision=decision,
                attempt=attempt,
                compiled=compiled,
                compile_receipt_sha256=receipt.sha256,
                evaluation=evaluation,
                planner_rejection=None,
                operation_interruption=None,
                solution_stage_results=solution_stage_results,
            )
            decisions.append(decision)
            attempts.append(attempt)
        return CellRunResult(
            cell_id=self.cell_id,
            attempts=tuple(attempts),
            decisions=tuple(decisions),
            sealed=len(attempts) == self.rounds,
        )

    def _latest_compile_binding(
        self, round_index: int
    ) -> tuple[str, HarnessDecision | None]:
        for prior_index in range(round_index - 1, 0, -1):
            version = f"v{prior_index:03d}"
            path = self.compile_receipts.root / "index" / f"{version}.json"
            if not path.is_file():
                continue
            receipt, decision = self.compile_receipts.load_version(
                version,
                cell_id=self.cell_id,
                suite=self.suite,
                instance_id=self.instance_id,
                variant_id=self.variant.variant_id,
                adaptation_policy=self.variant.adaptation_policy,
            )
            return receipt.sha256, decision
        return "0" * 64, None

    def _verify_compile_version(
        self,
        *,
        version: str,
        attempts: tuple[PublicAttempt, ...],
        prior_operational_fingerprints: tuple[str, ...],
    ) -> tuple[HarnessCompileReceipt, HarnessDecision]:
        """Recompile one sealed version from trusted inputs before it is reused."""

        receipt, decision = self.compile_receipts.load_version(
            version,
            cell_id=self.cell_id,
            suite=self.suite,
            instance_id=self.instance_id,
            variant_id=self.variant.variant_id,
            adaptation_policy=self.variant.adaptation_policy,
        )
        previous_sha, previous_decision = self._latest_compile_binding(
            int(version[1:])
        )
        if (
            receipt.previous_receipt_sha256 != previous_sha
            or receipt.previous_decision_sha256
            != ("0" * 64 if previous_decision is None else previous_decision.sha256)
        ):
            raise ValueError("sealed compile receipt parent chain differs")
        context = HarnessContext(
            instance_id=self.instance_id,
            suite=self.suite,
            round_index=int(version[1:]),
            task_card=self.task_card,
            reference_artifact_id="reference",
            reference_artifact=self.reference_artifact,
            attempts=attempts,
            cross_instance_records=self.cross_instance_records,
            cross_instance_memory_grant=self.cross_instance_memory_grant,
            stream_index=self.stream_index,
            builder_meta_prior=self.builder_meta_prior,
            public_observations={
                "artifact_contract": codec_capability_payload(self.solution_codec)
            },
        )
        compiled = self.operator_registry.compile(
            decision,
            variant=self.variant,
            context=context,
            previous_decision=previous_decision,
            prior_operational_fingerprints=prior_operational_fingerprints,
        )
        self.compile_receipts.verify_against_compilation(
            receipt=receipt,
            decision=decision,
            compiled=compiled,
            previous_decision=previous_decision,
            prior_operational_fingerprints=prior_operational_fingerprints,
        )
        return receipt, decision

    def _operation_interruption(
        self,
        *,
        version: str,
        planner_kind: str,
    ) -> dict[str, object] | None:
        replay = self.model_gateway.governor.journal.replay()
        candidates = (
            (
                "planner",
                f"{self.operation_prefix}:{planner_kind}:{version}",
                planner_kind,
            ),
            (
                "solution",
                f"{self.operation_prefix}:solution_call:{version}",
                "solution_call",
            ),
            (
                "evaluator",
                f"{self.operation_prefix}:evaluator:{version}",
                "evaluator_transaction",
            ),
        )
        interruptions: list[dict[str, object]] = []
        for phase, operation_id, operation_kind in candidates:
            operation = replay.operations.get(operation_id)
            if operation is None:
                continue
            if (
                operation.cell_id != self.cell_id
                or operation.operation_kind != operation_kind
            ):
                raise OperationStateError("round operation binding differs")
            if operation.state == "failed":
                event = operation.event_for("operation_failed")
                interruptions.append(
                    {
                        "schema_version": 1,
                        "operation_id": operation_id,
                        "operation_kind": operation_kind,
                        "phase": phase,
                        "state": "failed",
                        "event_sha256": event.event_sha256,
                        "reason_code": str(event.payload["reason_code"]),
                    }
                )
                continue
            if operation.state != "started":
                continue
            if phase == "evaluator":
                has_artifact = (
                    self.artifact_root
                    / "private_evaluator"
                    / version
                    / "controller-result.json"
                ).is_file()
            else:
                has_artifact = self.model_gateway.result_artifact_exists(operation_id)
            if has_artifact:
                continue
            event = operation.event_for("operation_started")
            interruptions.append(
                {
                    "schema_version": 1,
                    "operation_id": operation_id,
                    "operation_kind": operation_kind,
                    "phase": phase,
                    "state": "abandoned",
                    "event_sha256": event.event_sha256,
                    "reason_code": None,
                }
            )
        if len(interruptions) > 1:
            raise OperationStateError("round has multiple interrupted operations")
        return interruptions[0] if interruptions else None

    def _evaluate(self, version: str, artifact_path: Path) -> NormalizedEvaluation:
        operation_id = f"{self.operation_prefix}:evaluator:{version}"
        governor = self.model_gateway.governor
        private_dir = self.artifact_root / "private_evaluator" / version
        result_path = private_dir / "controller-result.json"
        artifact_sha256 = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
        operation = governor.journal.replay().operations.get(operation_id)

        if operation is None:
            if result_path.exists():
                raise OperationStateError(
                    "evaluator result exists without a reserved operation"
                )
            governor.reserve(
                operation_id=operation_id,
                cell_id=self.cell_id,
                operation_kind="evaluator_transaction",
                reservation=self.evaluator.reservation,
            )
            operation = governor.journal.replay().operations[operation_id]
        elif (
            operation.cell_id != self.cell_id
            or operation.operation_kind != "evaluator_transaction"
            or operation.reservation != self.evaluator.reservation
        ):
            raise OperationStateError("evaluator operation binding differs")

        if operation.state == "completed":
            evaluation, result_sha256 = self._load_evaluation_result(
                result_path=result_path,
                operation_id=operation_id,
                version=version,
                artifact_sha256=artifact_sha256,
            )
            completed = operation.event_for("operation_completed")
            if completed.payload.get("artifact_sha256") != result_sha256:
                raise OperationStateError(
                    "completed evaluator operation is not bound to its result artifact"
                )
            return evaluation
        if operation.state == "failed":
            raise OperationStateError("evaluator operation is already terminal: failed")
        if operation.state == "started":
            if not result_path.is_file():
                raise OperationStateError(
                    "started evaluator operation is abandoned without a trusted artifact"
                )
            evaluation, result_sha256 = self._load_evaluation_result(
                result_path=result_path,
                operation_id=operation_id,
                version=version,
                artifact_sha256=artifact_sha256,
            )
            governor.complete(
                operation_id,
                actual_usage=evaluation.actual_usage,
                artifact_sha256=result_sha256,
            )
            return evaluation
        if operation.state != "reserved":
            raise OperationStateError("unknown evaluator operation state")
        if result_path.exists():
            raise OperationStateError(
                "evaluator result exists before its operation was started"
            )

        governor.start(operation_id)
        try:
            evaluation = self.evaluator.evaluate(
                artifact_path,
                private_dir,
            )
        except Exception:
            governor.fail(operation_id, reason_code="evaluator_error")
            raise

        result_payload: dict[str, object] = {
            "schema_version": 1,
            "operation_id": operation_id,
            "cell_id": self.cell_id,
            "instance_id": self.instance_id,
            "version": version,
            "artifact_sha256": artifact_sha256,
            "evaluation": {
                "status": evaluation.status,
                "correct": evaluation.correct,
                "score": evaluation.score,
                "public_feedback": evaluation.public_feedback,
                "actual_usage": evaluation.actual_usage.to_dict(),
                "evidence_sha256": evaluation.evidence_sha256,
            },
        }
        encoded = _canonical_bytes(result_payload)
        _write_once(result_path, encoded)
        result_sha256 = hashlib.sha256(encoded).hexdigest()
        # Completion is deliberately separate from evaluator execution and artifact
        # persistence. A crash here leaves a replayable started+artifact operation;
        # a crash before the artifact leaves an abandoned operation that is never run
        # again.
        governor.complete(
            operation_id,
            actual_usage=evaluation.actual_usage,
            artifact_sha256=result_sha256,
        )
        return evaluation

    def _load_evaluation_result(
        self,
        *,
        result_path: Path,
        operation_id: str,
        version: str,
        artifact_sha256: str,
    ) -> tuple[NormalizedEvaluation, str]:
        if not result_path.is_file():
            raise OperationStateError("trusted evaluator result artifact is missing")
        encoded = result_path.read_bytes()
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise OperationStateError("trusted evaluator result JSON is invalid") from exc
        if not isinstance(payload, dict):
            raise OperationStateError("trusted evaluator result must be an object")
        expected = {
            "schema_version",
            "operation_id",
            "cell_id",
            "instance_id",
            "version",
            "artifact_sha256",
            "evaluation",
        }
        try:
            is_canonical = _canonical_bytes(payload) == encoded
        except (TypeError, ValueError):
            is_canonical = False
        if set(payload) != expected or not is_canonical:
            raise OperationStateError("trusted evaluator result is not canonical")
        if (
            payload["schema_version"] != 1
            or payload["operation_id"] != operation_id
            or payload["cell_id"] != self.cell_id
            or payload["instance_id"] != self.instance_id
            or payload["version"] != version
            or payload["artifact_sha256"] != artifact_sha256
            or not re.fullmatch(r"[0-9a-f]{64}", str(payload["artifact_sha256"]))
        ):
            raise OperationStateError("trusted evaluator result binding differs")
        raw_evaluation = payload["evaluation"]
        evaluation_keys = {
            "status",
            "correct",
            "score",
            "public_feedback",
            "actual_usage",
            "evidence_sha256",
        }
        if (
            not isinstance(raw_evaluation, dict)
            or set(raw_evaluation) != evaluation_keys
        ):
            raise OperationStateError("trusted evaluator payload schema differs")
        status = raw_evaluation["status"]
        correct = raw_evaluation["correct"]
        score = raw_evaluation["score"]
        feedback = raw_evaluation["public_feedback"]
        evidence_sha256 = raw_evaluation["evidence_sha256"]
        if not isinstance(status, str) or not status:
            raise OperationStateError("trusted evaluator status is invalid")
        if not isinstance(correct, bool):
            raise OperationStateError("trusted evaluator correctness is invalid")
        if score is not None and (
            isinstance(score, bool)
            or not isinstance(score, (int, float))
            or not math.isfinite(score)
        ):
            raise OperationStateError("trusted evaluator score is invalid")
        if not isinstance(feedback, dict):
            raise OperationStateError("trusted evaluator feedback is invalid")
        if evidence_sha256 is not None and (
            not isinstance(evidence_sha256, str)
            or re.fullmatch(r"[0-9a-f]{64}", evidence_sha256) is None
        ):
            raise OperationStateError("trusted evaluator evidence hash is invalid")
        try:
            actual_usage = ResourceVector.from_dict(raw_evaluation["actual_usage"])
            evaluation = NormalizedEvaluation(
                status=status,
                correct=correct,
                score=score,
                public_feedback=feedback,
                actual_usage=actual_usage,
                evidence_sha256=evidence_sha256,
            )
        except (TypeError, ValueError) as exc:
            raise OperationStateError(
                "trusted evaluator result values are invalid"
            ) from exc
        return evaluation, hashlib.sha256(encoded).hexdigest()

    def _seal_round(
        self,
        *,
        version: str,
        decision: HarnessDecision | None,
        attempt: PublicAttempt,
        compiled,
        compile_receipt_sha256: str | None,
        evaluation: NormalizedEvaluation | None,
        planner_rejection: dict[str, str] | None,
        operation_interruption: dict[str, object] | None,
        solution_stage_results: tuple[tuple[str, GenerationResult], ...] = (),
    ) -> None:
        if planner_rejection is not None and operation_interruption is not None:
            raise ValueError("round cannot contain two rejection records")
        if compiled is not None and compile_receipt_sha256 is None:
            raise ValueError("accepted round lacks its compile receipt")
        if compile_receipt_sha256 is not None and re.fullmatch(
            r"[0-9a-f]{64}", compile_receipt_sha256
        ) is None:
            raise ValueError("round compile receipt hash is invalid")
        payload: dict[str, object] = {
            "schema_version": (
                (4 if compile_receipt_sha256 is not None else 3)
                if operation_interruption is not None
                else 2 if planner_rejection is not None else 4
            ),
            "cell_id": self.cell_id,
            "instance_id": self.instance_id,
            "suite": self.suite,
            "variant_id": self.variant.variant_id,
            "version": version,
            "decision": None if decision is None else asdict(decision),
            "compiled": None if compiled is None else {
                "decision_sha256": compiled.decision_sha256,
                "operational_fingerprint": compiled.operational_fingerprint,
                "rule_decision_trace": compiled.rule_decision_trace,
                "selected_parent_ids": list(compiled.selected_parent_ids),
                "memory": compiled.memory,
                "tool_outputs": compiled.tool_outputs,
                "execution_steps": [asdict(step) for step in compiled.execution_steps],
                "execution_mode": compiled.execution_mode,
                "scheduler_phase": compiled.scheduler_phase,
                "solution_prompt_sha256": hashlib.sha256(
                    compiled.solution_prompt.encode("utf-8")
                ).hexdigest(),
                "builder_meta_prior_sha256": compiled.builder_meta_prior_sha256,
                "axis_effect_sha256s": compiled.axis_effect_sha256s,
                "axis_configuration_sha256s": compiled.axis_configuration_sha256s,
            },
            "solution_stage_results": [
                {
                    "stage_id": stage_id,
                    "raw_response_sha256": hashlib.sha256(
                        result.raw_response.encode("utf-8")
                    ).hexdigest(),
                    "provider": result.provider,
                    "usage": dict(result.usage),
                }
                for stage_id, result in solution_stage_results
            ],
            "attempt": asdict(attempt),
            "evaluation": None
            if evaluation is None
            else {
                "status": evaluation.status,
                "correct": evaluation.correct,
                "score": evaluation.score,
                "public_feedback": evaluation.public_feedback,
                "actual_usage": evaluation.actual_usage.to_dict(),
                "evidence_sha256": evaluation.evidence_sha256,
            },
        }
        if compile_receipt_sha256 is not None:
            payload["compile_receipt_sha256"] = compile_receipt_sha256
        if planner_rejection is not None:
            payload["planner_rejection"] = {
                "schema_version": 1,
                **planner_rejection,
            }
        if operation_interruption is not None:
            payload["operation_interruption"] = {
                **operation_interruption,
                "schema_version": 1,
            }
        encoded = _canonical_bytes(payload)
        path = self.rounds_root / f"{version}.json"
        _write_once(path, encoded)
        round_sha = hashlib.sha256(encoded).hexdigest()
        self.registry.append(
            "hb_gen1_round_sealed",
            {
                "cell_id": self.cell_id,
                "instance_id": self.instance_id,
                "variant_id": self.variant.variant_id,
                "version": version,
                "round_sha256": round_sha,
            },
            event_id=f"hb-gen1-round:{hashlib.sha256((self.cell_id + ':' + version).encode()).hexdigest()}",
        )

    def _load_round(
        self, version: str
    ) -> tuple[HarnessDecision | None, PublicAttempt] | None:
        path = self.rounds_root / f"{version}.json"
        if not safe_regular_file_exists(path, label="sealed round"):
            return None
        encoded = read_safe_regular_file(path, label="sealed round")
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("sealed round JSON is invalid") from exc
        if (
            not isinstance(payload, dict)
            or payload.get("schema_version") not in {1, 2, 3, 4}
            or payload.get("cell_id") != self.cell_id
            or payload.get("instance_id") != self.instance_id
            or payload.get("variant_id") != self.variant.variant_id
            or payload.get("version") != version
        ):
            raise ValueError("sealed round binding differs")
        if (
            self.variant.adaptation_policy
            in {"targeted_any_change_v1", "wide_all_fields_recompile_v1"}
            and (
                payload["schema_version"] == 1
                or (
                    payload["schema_version"] == 3
                    and payload.get("operation_interruption", {}).get("phase")
                    != "planner"
                )
            )
        ):
            raise ValueError(
                "structural Harness campaign cannot restore an accepted legacy round without a compile receipt"
            )
        round_sha = hashlib.sha256(encoded).hexdigest()
        event = next(
            (
                event
                for event in self.registry.read_events()
                if event["event_type"] == "hb_gen1_round_sealed"
                and event["payload"].get("cell_id") == self.cell_id
                and event["payload"].get("version") == version
            ),
            None,
        )
        if event is None or event["payload"].get("round_sha256") != round_sha:
            raise ValueError("sealed round is not bound to the append-only fact ledger")
        raw_decision = payload.get("decision")
        if payload["schema_version"] == 1:
            if not isinstance(raw_decision, dict):
                raise ValueError("sealed accepted round lacks its Harness decision")
            decision = HarnessDecision.from_dict(raw_decision)
        elif payload["schema_version"] == 2:
            rejection = payload.get("planner_rejection")
            if (
                raw_decision is not None
                or payload.get("compiled") is not None
                or payload.get("evaluation") is not None
                or not isinstance(rejection, dict)
                or set(rejection)
                != {"schema_version", "reason_code", "raw_response_sha256"}
                or rejection.get("schema_version") != 1
                or rejection.get("reason_code") not in _PLANNER_REJECTION_REASONS
                or re.fullmatch(
                    r"[0-9a-f]{64}", str(rejection.get("raw_response_sha256"))
                )
                is None
            ):
                raise ValueError("sealed planner rejection schema differs")
            decision = None
        elif payload["schema_version"] == 3:
            interruption = payload.get("operation_interruption")
            if (
                raw_decision is not None
                or payload.get("compiled") is not None
                or payload.get("evaluation") is not None
                or not isinstance(interruption, dict)
                or set(interruption)
                != {
                    "schema_version",
                    "operation_id",
                    "operation_kind",
                    "phase",
                    "state",
                    "event_sha256",
                    "reason_code",
                }
                or interruption.get("schema_version") != 1
                or interruption.get("phase")
                not in {"planner", "solution", "evaluator"}
                or interruption.get("state") not in {"abandoned", "failed"}
                or re.fullmatch(
                    r"[0-9a-f]{64}", str(interruption.get("event_sha256"))
                )
                is None
            ):
                raise ValueError("sealed operation interruption schema differs")
            self._validate_interruption_binding(
                interruption=interruption,
                version=version,
                allowed_phases={"planner", "solution", "evaluator"},
            )
            decision = None
        else:
            compile_sha = payload.get("compile_receipt_sha256")
            interruption = payload.get("operation_interruption")
            accepted = interruption is None
            if (
                re.fullmatch(r"[0-9a-f]{64}", str(compile_sha)) is None
                or not isinstance(raw_decision, dict)
                or payload.get("compiled") is None and accepted
                or payload.get("evaluation") is not None and not accepted
            ):
                raise ValueError("sealed compile receipt round schema differs")
            decision = HarnessDecision.from_dict(raw_decision)
            receipt, indexed_decision = self.compile_receipts.load_version(
                version,
                cell_id=self.cell_id,
                suite=self.suite,
                instance_id=self.instance_id,
                variant_id=self.variant.variant_id,
                adaptation_policy=self.variant.adaptation_policy,
            )
            if receipt.sha256 != compile_sha or indexed_decision != decision:
                raise ValueError("sealed round compile receipt binding differs")
            replay_context = HarnessContext(
                instance_id=self.instance_id,
                suite=self.suite,
                round_index=int(version[1:]),
                task_card=self.task_card,
                reference_artifact_id="reference",
                reference_artifact=self.reference_artifact,
                attempts=tuple(),
                cross_instance_records=self.cross_instance_records,
                cross_instance_memory_grant=self.cross_instance_memory_grant,
                stream_index=self.stream_index,
                builder_meta_prior=self.builder_meta_prior,
                public_observations={
                    "artifact_contract": codec_capability_payload(self.solution_codec)
                },
            )
            if int(version[1:]) > 1:
                replay_attempts: list[PublicAttempt] = []
                for prior_index in range(1, int(version[1:])):
                    prior_path = self.rounds_root / f"v{prior_index:03d}.json"
                    if not safe_regular_file_exists(
                        prior_path, label="sealed prior round"
                    ):
                        raise ValueError("compile receipt replay history is incomplete")
                    prior_payload = json.loads(
                        read_safe_regular_file(
                            prior_path, label="sealed prior round"
                        )
                    )
                    replay_attempts.append(PublicAttempt(**prior_payload["attempt"]))
                replay_context = HarnessContext(
                    **{**replay_context.__dict__, "attempts": tuple(replay_attempts)}
                )
            previous_sha, previous_decision = self._latest_compile_binding(
                int(version[1:])
            )
            if (
                receipt.previous_receipt_sha256 != previous_sha
                or receipt.previous_decision_sha256
                != ("0" * 64 if previous_decision is None else previous_decision.sha256)
            ):
                raise ValueError("sealed compile receipt parent chain differs")
            replayed_compiled = self.operator_registry.compile(
                decision,
                variant=self.variant,
                context=replay_context,
                previous_decision=previous_decision,
                prior_operational_fingerprints=tuple(
                    receipt.lineage_operational_fingerprints[:-1]
                ),
            )
            self.compile_receipts.verify_against_compilation(
                receipt=receipt,
                decision=decision,
                compiled=replayed_compiled,
                previous_decision=previous_decision,
                prior_operational_fingerprints=tuple(
                    receipt.lineage_operational_fingerprints[:-1]
                ),
            )
            compile_event = next(
                (
                    event
                    for event in self.registry.read_events()
                    if event.get("event_type") == "hb_harness_compiled"
                    and event.get("payload", {}).get("cell_id") == self.cell_id
                    and event.get("payload", {}).get("version") == version
                ),
                None,
            )
            if compile_event is None or compile_event.get("payload") != {
                "cell_id": self.cell_id,
                "instance_id": self.instance_id,
                "variant_id": self.variant.variant_id,
                "version": version,
                "receipt_sha256": receipt.sha256,
                "decision_sha256": decision.sha256,
                "component_catalog_sha256": receipt.component_catalog_sha256,
                "adaptation_policy": receipt.adaptation_policy,
                "builder_meta_prior_sha256": receipt.builder_meta_prior_sha256,
            }:
                raise ValueError("sealed compile receipt ledger binding differs")
            raw_compiled = payload.get("compiled")
            if raw_compiled is not None:
                expected_compiled_fields = {
                    "decision_sha256",
                    "operational_fingerprint",
                    "rule_decision_trace",
                    "selected_parent_ids",
                    "memory",
                    "tool_outputs",
                    "execution_steps",
                    "execution_mode",
                    "scheduler_phase",
                    "solution_prompt_sha256",
                    "builder_meta_prior_sha256",
                    "axis_effect_sha256s",
                    "axis_configuration_sha256s",
                }
                if (
                    not isinstance(raw_compiled, dict)
                    or set(raw_compiled) != expected_compiled_fields
                    or raw_compiled["decision_sha256"] != receipt.decision_sha256
                    or raw_compiled["operational_fingerprint"]
                    != receipt.operational_fingerprint
                    or tuple(raw_compiled["selected_parent_ids"])
                    != receipt.selected_parent_ids
                    or _value_sha256(raw_compiled["memory"])
                    != receipt.memory_sha256
                    or _value_sha256(raw_compiled["tool_outputs"])
                    != receipt.tool_outputs_sha256
                    or _value_sha256(raw_compiled["execution_steps"])
                    != receipt.workflow_sha256
                    or raw_compiled["execution_mode"] != decision.execution_mode
                    or _value_sha256(raw_compiled["scheduler_phase"])
                    != receipt.scheduler_sha256
                    or raw_compiled["solution_prompt_sha256"]
                    != receipt.solution_prompt_sha256
                    or raw_compiled["builder_meta_prior_sha256"]
                    != receipt.builder_meta_prior_sha256
                    or raw_compiled["axis_effect_sha256s"]
                    != receipt.axis_effect_sha256s
                    or raw_compiled["axis_configuration_sha256s"]
                    != receipt.axis_configuration_sha256s
                    or not isinstance(raw_compiled["rule_decision_trace"], dict)
                    or raw_compiled["rule_decision_trace"].get(
                        "rule_registry_sha256"
                    )
                    != receipt.rule_registry_sha256
                ):
                    raise ValueError("sealed round compiled Harness binding differs")
            if interruption is not None:
                self._validate_interruption_binding(
                    interruption=interruption,
                    version=version,
                    allowed_phases={"solution", "evaluator"},
                )
        raw_attempt = payload["attempt"]
        attempt = PublicAttempt(**raw_attempt)
        if payload["schema_version"] == 2 and (
            attempt.outcome != "planner_contract_rejected"
            or attempt.artifact_sha256
            != payload["planner_rejection"]["raw_response_sha256"]
        ):
            raise ValueError("sealed planner rejection attempt binding differs")
        if payload["schema_version"] in {3, 4} and payload.get("operation_interruption") is not None:
            interruption = payload["operation_interruption"]
            if (
                attempt.outcome
                != f"{interruption['phase']}_operation_{interruption['state']}"
                or attempt.artifact_sha256
                != hashlib.sha256(_canonical_bytes(interruption)).hexdigest()
            ):
                raise ValueError("sealed operation interruption attempt binding differs")
        return decision, attempt

    def _validate_interruption_binding(
        self,
        *,
        interruption: object,
        version: str,
        allowed_phases: set[str],
    ) -> None:
        expected_fields = {
            "schema_version",
            "operation_id",
            "operation_kind",
            "phase",
            "state",
            "event_sha256",
            "reason_code",
        }
        if (
            not isinstance(interruption, dict)
            or set(interruption) != expected_fields
            or interruption.get("schema_version") != 1
            or interruption.get("phase") not in allowed_phases
            or interruption.get("state") not in {"abandoned", "failed"}
            or re.fullmatch(
                r"[0-9a-f]{64}", str(interruption.get("event_sha256"))
            )
            is None
        ):
            raise ValueError("sealed operation interruption schema differs")
        operation_id = str(interruption["operation_id"])
        round_index = int(version[1:])
        expected_planner_kind = (
            "sham_planner_call"
            if self.variant.freeze_after_initial and round_index > 1
            else "planner_call"
        )
        expected_operations = {
            "planner": (
                f"{self.operation_prefix}:{expected_planner_kind}:{version}",
                expected_planner_kind,
            ),
            "solution": (
                f"{self.operation_prefix}:solution_call:{version}",
                "solution_call",
            ),
            "evaluator": (
                f"{self.operation_prefix}:evaluator:{version}",
                "evaluator_transaction",
            ),
        }
        phase = str(interruption["phase"])
        expected_operation_id, expected_operation_kind = expected_operations[phase]
        operation = self.model_gateway.governor.journal.replay().operations.get(
            operation_id
        )
        event_type = (
            "operation_started"
            if interruption["state"] == "abandoned"
            else "operation_failed"
        )
        if (
            operation is None
            or operation_id != expected_operation_id
            or interruption["operation_kind"] != expected_operation_kind
            or operation.cell_id != self.cell_id
            or operation.operation_kind != interruption["operation_kind"]
            or operation.state
            != ("started" if interruption["state"] == "abandoned" else "failed")
            or operation.event_for(event_type).event_sha256
            != interruption["event_sha256"]
            or (
                interruption["state"] == "failed"
                and operation.event_for(event_type).payload.get("reason_code")
                != interruption["reason_code"]
            )
            or (
                interruption["state"] == "abandoned"
                and interruption["reason_code"] is not None
            )
            or (
                interruption["state"] == "abandoned"
                and (
                    (
                        phase == "evaluator"
                        and (
                            self.artifact_root
                            / "private_evaluator"
                            / version
                            / "controller-result.json"
                        ).is_file()
                    )
                    or (
                        phase in {"planner", "solution"}
                        and self.model_gateway.result_artifact_exists(operation_id)
                    )
                )
            )
        ):
            raise ValueError("sealed operation interruption binding differs")
