from __future__ import annotations

import hashlib
import json
from collections import deque
from pathlib import Path

import pytest

from optimization_lab.generation import FakeGenerator
from optimization_lab.harness_builder.evaluation import NormalizedEvaluation
from optimization_lab.harness_builder.events import (
    OperationJournal,
    OperationStateError,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
)
from optimization_lab.harness_builder.model_gateway import IsolatedModelGateway
from optimization_lab.harness_builder.operators import TrustedOperatorRegistry
from optimization_lab.harness_builder.runner import HarnessBuilderCellRunner, _write_once
from optimization_lab.harness_builder.schema import BuilderVariant
from optimization_lab.harness_builder.solutions import SolutionArtifact


def _decision(round_index: int) -> str:
    explore = round_index % 2 == 1
    payload = {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["task_analyst", "performance_analyst", "generator", "verifier"],
        "memory_views": ["current", "best", "failures"],
        "tools": ["task_semantics", "score_history", "static_structure"],
        "parent_strategy": "incumbent" if explore else "stable_best",
        "workflow": ["analyze", "select_parent", "inspect", "generate", "verify_contract"],
        "scheduler_mode": "single_candidate" if explore else "explore_then_exploit",
        "recovery_mode": "preserve_failure",
        "kernel_directive": f"Generate candidate {round_index}.",
    }
    return json.dumps(payload)


def _multi_step_decision() -> str:
    payload = json.loads(_decision(1))
    payload["workflow"] = ["analyze", "generate", "verify_contract"]
    payload["execution_mode"] = "multi_step"
    return json.dumps(payload)


class TextCodec:
    output_mode = "plain_text"

    def parse(self, raw_response: str) -> SolutionArtifact:
        text = raw_response.strip() + "\n"
        digest = hashlib.sha256(text.encode()).hexdigest()
        return SolutionArtifact(
            raw_response=raw_response,
            text=text,
            sha256=digest,
            structural_signature=hashlib.sha256(
                ("structure:" + text).encode()
            ).hexdigest(),
            extension=".txt",
            artifact_kind="fixture",
        )


class FakeEvaluationBackend:
    reservation = ResourceVector(
        evaluator_transactions=1, cpu_evaluator_seconds=10.0
    )

    def __init__(self) -> None:
        self.calls: list[Path] = []

    def evaluate(self, artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        self.calls.append(artifact_path)
        private_dir.mkdir(parents=True, exist_ok=True)
        score = 1.0 + len(self.calls) / 100.0
        return NormalizedEvaluation(
            status="valid",
            correct=True,
            score=score,
            public_feedback={"status": "valid", "score": score},
            actual_usage=ResourceVector(
                evaluator_transactions=1, cpu_evaluator_seconds=2.0
            ),
        )


class InterruptingGenerator:
    def generate(self, _prompt: str, *, model: str):
        raise KeyboardInterrupt(f"fixture {model} interruption")


class FailingGenerator:
    def generate(self, _prompt: str, *, model: str):
        raise RuntimeError(f"fixture {model} failure")


def test_sealed_round_write_rejects_symlink_target_and_parent(tmp_path: Path) -> None:
    outside_file = tmp_path / "outside.json"
    outside_file.write_bytes(b"original\n")
    rounds = tmp_path / "rounds"
    rounds.mkdir()
    target = rounds / "v001.json"
    target.symlink_to(outside_file)
    with pytest.raises(ValueError, match="unsafe sealed round target"):
        _write_once(target, b"sealed\n")
    assert outside_file.read_bytes() == b"original\n"

    outside_dir = tmp_path / "outside-rounds"
    outside_dir.mkdir()
    linked_parent = tmp_path / "linked-rounds"
    linked_parent.symlink_to(outside_dir, target_is_directory=True)
    with pytest.raises(ValueError, match="unsafe sealed round path"):
        _write_once(linked_parent / "v002.json", b"sealed\n")
    assert list(outside_dir.iterdir()) == []

    non_directory = tmp_path / "not-a-directory"
    non_directory.write_text("ordinary file")
    with pytest.raises(ValueError, match="unsafe sealed round path"):
        _write_once(non_directory / "v003.json", b"sealed\n")


def _variant() -> BuilderVariant:
    return BuilderVariant(
        variant_id="B0",
        description="fixture",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("discipline",),
        experience_sources=(),
        excluded_task_ids=(),
    )


def _governor(tmp_path: Path) -> ResourceGovernor:
    caps = ResourceCaps(
        model_calls=16,
        evaluator_transactions=11,
        gpu_exclusive_seconds=0,
        cpu_evaluator_seconds=80,
    )
    return ResourceGovernor(
        journal=OperationJournal(
            tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
        ),
        global_caps=caps,
        cell_caps={"formal:suite:task:B0": caps},
    )


def test_cell_runner_executes_and_recovers_eight_system_harness_rounds(
    tmp_path: Path,
) -> None:
    responses: deque[str] = deque(
        value
        for round_index in range(1, 9)
        for value in (_decision(round_index), f"solution-{round_index}")
    )
    transport_calls: list[Path] = []

    def factory(work_root: Path, _output_mode: str) -> FakeGenerator:
        transport_calls.append(work_root)
        return FakeGenerator(responses.popleft())

    governor = _governor(tmp_path)
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=governor,
        transport_factory=factory,
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    evaluator = FakeEvaluationBackend()
    runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=gateway,
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=evaluator,
    )

    result = runner.run()

    assert result.sealed is True
    assert len(result.attempts) == 8
    assert len(transport_calls) == 16
    assert len(evaluator.calls) == 8
    assert result.best_score == 1.08
    assert governor.snapshot().global_committed == ResourceVector(
        model_calls=16,
        evaluator_transactions=8,
        cpu_evaluator_seconds=16.0,
    )
    assert len(list((tmp_path / "campaign" / "rounds").glob("v*.json"))) == 8

    restored_evaluator = FakeEvaluationBackend()
    restored_gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=ResourceGovernor(
            journal=OperationJournal(
                tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
            ),
            global_caps=governor.global_caps,
            cell_caps=governor.cell_caps,
        ),
        transport_factory=lambda _root, _mode: FakeGenerator("must not run"),
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    restored = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=restored_gateway,
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=restored_evaluator,
    ).run()

    assert restored == result
    assert restored_evaluator.calls == []


def test_cell_runner_journals_each_multi_step_model_node_separately(
    tmp_path: Path,
) -> None:
    responses = deque(
        [_multi_step_decision(), "analysis", "candidate", "verification"]
    )
    governor = _governor(tmp_path)
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=governor,
        transport_factory=lambda _root, _mode: FakeGenerator(responses.popleft()),
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    evaluator = FakeEvaluationBackend()
    runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=gateway,
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=evaluator,
        rounds=1,
    )

    result = runner.run()

    assert result.sealed is True
    assert result.attempts[0].artifact_text == "candidate\n"
    replay = governor.journal.replay()
    assert set(replay.operations) == {
        "formal:suite:task:B0:planner_call:v001",
        "formal:suite:task:B0:solution_call:v001:analyze",
        "formal:suite:task:B0:solution_call:v001:generate",
        "formal:suite:task:B0:solution_call:v001:verify_contract",
        "formal:suite:task:B0:evaluator:v001",
    }
    receipt = json.loads(
        (tmp_path / "campaign" / "rounds" / "v001.json").read_text()
    )
    assert [item["stage_id"] for item in receipt["solution_stage_results"]] == [
        "analyze",
        "generate",
        "verify_contract",
    ]


def test_cell_runner_preserves_contract_reject_in_attempt_denominator(
    tmp_path: Path,
) -> None:
    class RejectingCodec(TextCodec):
        def parse(self, raw_response: str) -> SolutionArtifact:
            from optimization_lab.harness_builder.solutions import SolutionContractError

            raise SolutionContractError(
                "fixture reject", reason_code="fixture_reject"
            )

    responses = deque([_decision(1), "invalid solution"])
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=_governor(tmp_path),
        transport_factory=lambda _root, _mode: FakeGenerator(responses.popleft()),
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    evaluator = FakeEvaluationBackend()
    runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=gateway,
        model="fixture-model",
        solution_codec=RejectingCodec(),
        evaluator=evaluator,
        rounds=1,
    )

    result = runner.run()

    assert len(result.attempts) == 1
    assert result.attempts[0].outcome == "contract_rejected"
    assert result.attempts[0].correct is False
    assert "fixture_reject" in result.attempts[0].public_summary
    assert evaluator.calls == []


def test_cell_runner_seals_planner_contract_reject_and_continues(
    tmp_path: Path,
) -> None:
    class RejectFirstCodec(TextCodec):
        def parse(self, raw_response: str) -> SolutionArtifact:
            if raw_response == "solution-1":
                from optimization_lab.harness_builder.solutions import (
                    SolutionContractError,
                )

                raise SolutionContractError("fixture first-round reject")
            return super().parse(raw_response)

    first = json.loads(_decision(1))
    repeated = {
        **first,
        "kernel_directive": "Only the wording and rule label changed.",
    }
    third = json.loads(_decision(2))
    third["kernel_directive"] = "Generate candidate 3 after a real system change."
    responses = deque(
        [
            json.dumps(first),
            "solution-1",
            json.dumps(repeated),
            json.dumps(third),
            "solution-3",
        ]
    )
    transport_calls: list[Path] = []

    def factory(work_root: Path, _output_mode: str) -> FakeGenerator:
        transport_calls.append(work_root)
        return FakeGenerator(responses.popleft())

    governor = _governor(tmp_path)
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=governor,
        transport_factory=factory,
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    evaluator = FakeEvaluationBackend()
    runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=gateway,
        model="fixture-model",
        solution_codec=RejectFirstCodec(),
        evaluator=evaluator,
        rounds=3,
    )

    result = runner.run()

    assert result.sealed is True
    assert [attempt.outcome for attempt in result.attempts] == [
        "contract_rejected",
        "planner_contract_rejected",
        "valid",
    ]
    assert result.decisions[0] is not None
    assert result.decisions[1] is None
    assert result.decisions[2] is not None
    assert len(transport_calls) == 5
    assert len(evaluator.calls) == 1
    assert governor.snapshot().global_committed == ResourceVector(
        model_calls=5,
        evaluator_transactions=1,
        cpu_evaluator_seconds=2.0,
    )
    rejected = json.loads(
        (tmp_path / "campaign/rounds/v002.json").read_text(encoding="utf-8")
    )
    assert rejected["schema_version"] == 2
    assert rejected["decision"] is None
    assert rejected["compiled"] is None
    assert rejected["planner_rejection"]["reason_code"] == "no_operational_change"
    assert not any(
        operation.operation_id.endswith("solution_call:v002")
        for operation in governor.journal.replay().operations.values()
    )

    restored_evaluator = FakeEvaluationBackend()
    restored = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=ResourceGovernor(
                journal=OperationJournal(
                    tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
                ),
                global_caps=governor.global_caps,
                cell_caps=governor.cell_caps,
            ),
            transport_factory=lambda _root, _mode: pytest.fail(
                "recovery called model transport"
            ),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=RejectFirstCodec(),
        evaluator=restored_evaluator,
        rounds=3,
    ).run()

    assert restored == result
    assert restored_evaluator.calls == []


def test_cell_runner_seals_compile_receipt_before_solution_and_replays_it(
    tmp_path: Path,
) -> None:
    governor = _governor(tmp_path)
    transports = deque([FakeGenerator(_decision(1)), InterruptingGenerator()])
    runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=governor,
            transport_factory=lambda _root, _mode: transports.popleft(),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=FakeEvaluationBackend(),
        rounds=1,
    )

    with pytest.raises(KeyboardInterrupt, match="fixture-model interruption"):
        runner.run()

    index = json.loads(
        (tmp_path / "campaign/compiled/index/v001.json").read_text()
    )
    receipt_sha = index["receipt_sha256"]
    assert (
        tmp_path / f"campaign/compiled/receipts/{receipt_sha}.json"
    ).is_file()
    compile_events = [
        event
        for event in runner.registry.read_events()
        if event["event_type"] == "hb_harness_compiled"
    ]
    assert len(compile_events) == 1

    restored = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=ResourceGovernor(
                journal=OperationJournal(
                    tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
                ),
                global_caps=governor.global_caps,
                cell_caps=governor.cell_caps,
            ),
            transport_factory=lambda _root, _mode: pytest.fail(
                "recovery called model transport"
            ),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=FakeEvaluationBackend(),
        rounds=1,
    ).run()

    assert restored.sealed is True
    assert restored.attempts[0].outcome == "solution_operation_abandoned"
    assert restored.decisions[0] is not None
    sealed = json.loads(
        (tmp_path / "campaign/rounds/v001.json").read_text()
    )
    assert sealed["schema_version"] == 4
    assert sealed["compile_receipt_sha256"] == receipt_sha


def test_cell_runner_replays_completed_evaluator_before_round_seal(
    tmp_path: Path,
) -> None:
    responses = deque([_decision(1), "solution-1"])
    governor = _governor(tmp_path)
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=governor,
        transport_factory=lambda _root, _mode: FakeGenerator(responses.popleft()),
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    evaluator = FakeEvaluationBackend()
    runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=gateway,
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=evaluator,
        rounds=1,
    )
    runner._seal_round = lambda **_kwargs: (_ for _ in ()).throw(  # type: ignore[method-assign]
        RuntimeError("fixture crash after evaluator completion")
    )

    with pytest.raises(RuntimeError, match="fixture crash"):
        runner.run()
    assert len(evaluator.calls) == 1
    assert not (tmp_path / "campaign/rounds/v001.json").exists()

    restored_evaluator = FakeEvaluationBackend()
    restored = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=ResourceGovernor(
                journal=OperationJournal(
                    tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
                ),
                global_caps=governor.global_caps,
                cell_caps=governor.cell_caps,
            ),
            transport_factory=lambda _root, _mode: pytest.fail(
                "recovery called model transport"
            ),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=restored_evaluator,
        rounds=1,
    ).run()

    assert restored.sealed is True
    assert restored_evaluator.calls == []


def test_cell_runner_seals_abandoned_planner_and_continues(
    tmp_path: Path,
) -> None:
    governor = _governor(tmp_path)
    first_runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=governor,
            transport_factory=lambda _root, _mode: InterruptingGenerator(),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=FakeEvaluationBackend(),
        rounds=2,
    )
    with pytest.raises(KeyboardInterrupt, match="fixture-model interruption"):
        first_runner.run()

    responses = deque([_decision(2), "solution-2"])
    restored_evaluator = FakeEvaluationBackend()
    restored = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=ResourceGovernor(
                journal=OperationJournal(
                    tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
                ),
                global_caps=governor.global_caps,
                cell_caps=governor.cell_caps,
            ),
            transport_factory=lambda _root, _mode: FakeGenerator(responses.popleft()),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=restored_evaluator,
        rounds=2,
    ).run()

    assert restored.sealed is True
    assert [item.outcome for item in restored.attempts] == [
        "planner_operation_abandoned",
        "valid",
    ]
    assert restored.decisions[0] is None
    assert len(restored_evaluator.calls) == 1

    replay_evaluator = FakeEvaluationBackend()
    replayed = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=ResourceGovernor(
                journal=OperationJournal(
                    tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
                ),
                global_caps=governor.global_caps,
                cell_caps=governor.cell_caps,
            ),
            transport_factory=lambda _root, _mode: pytest.fail(
                "sealed interruption replay called model transport"
            ),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=replay_evaluator,
        rounds=2,
    ).run()
    assert replayed == restored
    assert replay_evaluator.calls == []


def test_cell_runner_seals_abandoned_solution_and_continues(
    tmp_path: Path,
) -> None:
    governor = _governor(tmp_path)
    first_transports = deque(
        [FakeGenerator(_decision(1)), InterruptingGenerator()]
    )
    first_runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=governor,
            transport_factory=lambda _root, _mode: first_transports.popleft(),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=FakeEvaluationBackend(),
        rounds=2,
    )
    with pytest.raises(KeyboardInterrupt, match="fixture-model interruption"):
        first_runner.run()

    responses = deque([_decision(2), "solution-2"])
    restored_evaluator = FakeEvaluationBackend()
    restored = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=ResourceGovernor(
                journal=OperationJournal(
                    tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
                ),
                global_caps=governor.global_caps,
                cell_caps=governor.cell_caps,
            ),
            transport_factory=lambda _root, _mode: FakeGenerator(responses.popleft()),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=restored_evaluator,
        rounds=2,
    ).run()

    assert restored.sealed is True
    assert [item.outcome for item in restored.attempts] == [
        "solution_operation_abandoned",
        "valid",
    ]
    assert restored.decisions[0] is not None
    assert len(restored_evaluator.calls) == 1


def test_cell_runner_seals_failed_planner_without_retry(tmp_path: Path) -> None:
    governor = _governor(tmp_path)
    first_runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=governor,
            transport_factory=lambda _root, _mode: FailingGenerator(),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=FakeEvaluationBackend(),
        rounds=1,
    )
    with pytest.raises(RuntimeError, match="fixture-model failure"):
        first_runner.run()

    restored_evaluator = FakeEvaluationBackend()
    restored = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=ResourceGovernor(
                journal=OperationJournal(
                    tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
                ),
                global_caps=governor.global_caps,
                cell_caps=governor.cell_caps,
            ),
            transport_factory=lambda _root, _mode: pytest.fail(
                "recovery called model transport"
            ),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=restored_evaluator,
        rounds=1,
    ).run()

    assert restored.sealed is True
    assert restored.attempts[0].outcome == "planner_operation_failed"
    assert restored.decisions[0] is None
    assert restored_evaluator.calls == []


def test_cell_runner_seals_started_evaluator_without_artifact_without_retry(
    tmp_path: Path,
) -> None:
    class InterruptedEvaluationBackend(FakeEvaluationBackend):
        def evaluate(
            self, artifact_path: Path, private_dir: Path
        ) -> NormalizedEvaluation:
            self.calls.append(artifact_path)
            raise KeyboardInterrupt("fixture evaluator interruption")

    responses = deque([_decision(1), "solution-1"])
    governor = _governor(tmp_path)
    first_evaluator = InterruptedEvaluationBackend()
    runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=governor,
            transport_factory=lambda _root, _mode: FakeGenerator(responses.popleft()),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=first_evaluator,
        rounds=1,
    )
    with pytest.raises(KeyboardInterrupt, match="fixture evaluator interruption"):
        runner.run()
    assert len(first_evaluator.calls) == 1

    restored_evaluator = FakeEvaluationBackend()
    restored_runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=ResourceGovernor(
                journal=OperationJournal(
                    tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
                ),
                global_caps=governor.global_caps,
                cell_caps=governor.cell_caps,
            ),
            transport_factory=lambda _root, _mode: pytest.fail(
                "recovery called model transport"
            ),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=restored_evaluator,
        rounds=1,
    )

    result = restored_runner.run()
    assert result.sealed is True
    assert result.attempts[0].outcome == "evaluator_operation_abandoned"
    assert result.decisions[0] is not None
    assert restored_evaluator.calls == []


def test_cell_runner_completes_started_evaluator_from_sealed_artifact(
    tmp_path: Path,
) -> None:
    responses = deque([_decision(1), "solution-1"])
    governor = _governor(tmp_path)
    evaluator = FakeEvaluationBackend()
    original_complete = governor.complete

    def interrupt_evaluator_completion(operation_id: str, **kwargs):
        if ":evaluator:" in operation_id:
            raise KeyboardInterrupt("fixture crash after evaluator artifact")
        return original_complete(operation_id, **kwargs)

    governor.complete = interrupt_evaluator_completion  # type: ignore[method-assign]
    runner = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=governor,
            transport_factory=lambda _root, _mode: FakeGenerator(responses.popleft()),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=evaluator,
        rounds=1,
    )
    with pytest.raises(KeyboardInterrupt, match="fixture crash"):
        runner.run()
    assert len(evaluator.calls) == 1
    assert (
        tmp_path / "campaign/private_evaluator/v001/controller-result.json"
    ).is_file()

    restored_evaluator = FakeEvaluationBackend()
    restored_governor = ResourceGovernor(
        journal=OperationJournal(
            tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
        ),
        global_caps=governor.global_caps,
        cell_caps=governor.cell_caps,
    )
    result = HarnessBuilderCellRunner(
        artifact_root=tmp_path / "campaign",
        cell_id="formal:suite:task:B0",
        instance_id="suite:task",
        suite="suite",
        task_card="Optimize the public task.",
        reference_artifact="reference solution",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / "models",
            governor=restored_governor,
            transport_factory=lambda _root, _mode: pytest.fail(
                "recovery called model transport"
            ),
            signing_key=b"fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=TextCodec(),
        evaluator=restored_evaluator,
        rounds=1,
    ).run()

    assert result.sealed is True
    assert restored_evaluator.calls == []
    operation = restored_governor.journal.replay().operations[
        "formal:suite:task:B0:evaluator:v001"
    ]
    assert operation.state == "completed"
