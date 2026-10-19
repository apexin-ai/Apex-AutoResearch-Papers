from __future__ import annotations

from pathlib import Path
import json
import hashlib

import pytest

from optimization_lab.generation import GenerationResult
from optimization_lab.harness_builder.builder_harness import BuilderHarness
from optimization_lab.harness_builder.dual_harness import (
    HarnessWorkspace,
    TaskHarnessArtifact,
    TaskHarnessRuntime,
)
from optimization_lab.harness_builder.dual_runtime import (
    DualHarnessRuntime,
    EvaluationResult,
    IncompleteRoundError,
    PublicEvaluation,
)
from optimization_lab.harness_builder.tool_registry import BoundTool, ToolRegistry
from test_builder_harness import SequenceGenerator, proposal
from test_dual_harness import artifact


def test_dual_runtime_passes_fixed_agent_tools_with_round_scoped_receipts(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": ["inspect"],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 4,
                        "max_tool_calls": 2,
                    },
                },
                "router": {},
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "Solve {task}"},
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    workspace.commit(current)
    solver = SequenceGenerator(
        '{"action":"tool","tool":"inspect","arguments":{}}',
        '{"action":"emit","candidate":"candidate-v1"}',
    )
    registry = ToolRegistry(
        tmp_path / "tools",
        {"inspect": BoundTool.callable(lambda _: {"ok": True})},
    )
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=solver),
        builder=BuilderHarness(
            workspace=workspace,
            generator=SequenceGenerator(proposal(current.sha256)),
            model="builder-model",
        ),
        solver_model="solver-model",
    )

    result = pipeline.run_round(
        run_id="round-agent",
        execution_contract_sha256="c" * 64,
        task="public task",
        tools={},
        tool_registry=registry,
        tool_workspace=tmp_path / "tools" / "workspace",
        evaluator=lambda candidate: EvaluationResult(
            public=PublicEvaluation(0.5, "public feedback")
        ),
        evolve_builder=False,
    )

    assert result.candidate == "candidate-v1"
    receipts = (tmp_path / "tools" / ".tool_receipts.jsonl").read_text(
        encoding="utf-8"
    )
    assert "round-agent-solver-solve-tool-0000" in receipts


def test_dual_runtime_runs_solver_then_builder_with_separate_models(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    solver = SequenceGenerator("candidate-v1")
    builder_generator = SequenceGenerator(proposal(current.sha256))
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=solver),
        builder=BuilderHarness(
            workspace=workspace,
            generator=builder_generator,
            model="builder-model",
        ),
        solver_model="solver-model",
    )

    result = pipeline.run_round(
        run_id="round-1",
        execution_contract_sha256="c" * 64,
        task="public task",
        tools={"verify": lambda value: {"passed": True}},
        evaluator=lambda candidate: EvaluationResult(
            public=PublicEvaluation(0.5, f"needs verification: {candidate}"),
        ),
    )

    assert result.candidate == "candidate-v1"
    assert result.builder_status == "committed"
    assert solver.calls[0][1] == "solver-model"
    assert builder_generator.calls[0][1] == "builder-model"
    assert "needs verification" in builder_generator.calls[0][0]
    assert workspace.current().version == 2
    trace = workspace.load_builder_trace("round-1")
    assert trace["status"] == "committed"
    assert [event["step"] for event in trace["events"]] == [
        "inspect",
        "propose",
        "validate",
        "probe",
        "commit_or_rollback",
    ]


def test_private_evaluator_details_never_reach_trace_or_builder(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    solver = SequenceGenerator("candidate-v1")
    builder_generator = SequenceGenerator(proposal(current.sha256))
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=solver),
        builder=BuilderHarness(
            workspace=workspace,
            generator=builder_generator,
            model="builder-model",
        ),
        solver_model="solver-model",
    )

    pipeline.run_round(
        run_id="round-private",
        execution_contract_sha256="c" * 64,
        task="public task",
        tools={"verify": lambda value: {"passed": True}},
        evaluator=lambda candidate: EvaluationResult(
            public=PublicEvaluation(0.5, "public failure code: format"),
            private={"gold_answer": "PRIVATE_GOLD=answer-42", "candidate": candidate},
        ),
    )

    assert "PRIVATE_GOLD" not in builder_generator.calls[0][0]
    persisted = "\n".join(
        path.read_text(encoding="utf-8") for path in workspace.root.rglob("*.json")
    )
    assert "PRIVATE_GOLD" not in persisted


def test_completed_run_id_replays_without_paid_calls(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    solver = SequenceGenerator("candidate-v1", "must-not-run")
    builder_generator = SequenceGenerator(proposal(current.sha256), "must-not-run")
    evaluator_calls: list[str] = []
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=solver),
        builder=BuilderHarness(
            workspace=workspace,
            generator=builder_generator,
            model="builder-model",
        ),
        solver_model="solver-model",
    )

    def evaluator(candidate: str) -> EvaluationResult:
        evaluator_calls.append(candidate)
        return EvaluationResult(public=PublicEvaluation(0.5, "public feedback"))

    first = pipeline.run_round(
        run_id="round-replay",
        execution_contract_sha256="c" * 64,
        task="public task",
        tools={"verify": lambda value: {"passed": True}},
        evaluator=evaluator,
    )
    replay = pipeline.run_round(
        run_id="round-replay",
        execution_contract_sha256="c" * 64,
        task="public task",
        tools={"verify": lambda value: {"passed": True}},
        evaluator=evaluator,
    )

    assert replay == first
    assert len(solver.calls) == 1
    assert len(builder_generator.calls) == 1
    assert evaluator_calls == ["candidate-v1"]


def test_malformed_builder_output_is_recorded_as_rollback(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=SequenceGenerator("candidate-v1")),
        builder=BuilderHarness(
            workspace=workspace,
            generator=SequenceGenerator("not-json"),
            model="builder-model",
        ),
        solver_model="solver-model",
    )

    result = pipeline.run_round(
        run_id="round-malformed",
        execution_contract_sha256="c" * 64,
        task="public task",
        tools={"verify": lambda value: {"passed": True}},
        evaluator=lambda candidate: EvaluationResult(
            public=PublicEvaluation(0.0, "public parse failure")
        ),
    )

    assert result.builder_status == "rejected"
    trace = workspace.load_builder_trace("round-malformed")
    assert [event["step"] for event in trace["events"]] == [
        "inspect",
        "propose",
        "validate",
        "probe",
        "commit_or_rollback",
    ]
    assert trace["events"][-1]["output"] == "rollback"


def test_replay_rejects_changed_execution_contract(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=SequenceGenerator("candidate-v1")),
        builder=BuilderHarness(
            workspace=workspace,
            generator=SequenceGenerator(proposal(current.sha256)),
            model="builder-model",
        ),
        solver_model="solver-model",
    )
    evaluator = lambda candidate: EvaluationResult(  # noqa: E731
        public=PublicEvaluation(0.5, "public feedback")
    )
    pipeline.run_round(
        run_id="round-contract",
        execution_contract_sha256="c" * 64,
        task="public task",
        tools={"verify": lambda value: {"passed": True}},
        evaluator=evaluator,
    )

    with pytest.raises(ValueError, match="different round request"):
        pipeline.run_round(
            run_id="round-contract",
            execution_contract_sha256="d" * 64,
            task="public task",
            tools={"verify": lambda value: {"passed": True}},
            evaluator=evaluator,
        )


def test_interrupted_solver_call_is_not_repeated_automatically(tmp_path: Path) -> None:
    class FailingGenerator:
        def __init__(self) -> None:
            self.calls = 0

        def generate(self, prompt: str, *, model: str) -> GenerationResult:
            self.calls += 1
            raise RuntimeError("transport interrupted")

    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    solver = FailingGenerator()
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=solver),
        builder=BuilderHarness(
            workspace=workspace,
            generator=SequenceGenerator(proposal(current.sha256)),
            model="builder-model",
        ),
        solver_model="solver-model",
    )
    kwargs = {
        "run_id": "round-interrupted",
        "execution_contract_sha256": "c" * 64,
        "task": "public task",
        "tools": {"verify": lambda value: {"passed": True}},
        "evaluator": lambda candidate: EvaluationResult(
            public=PublicEvaluation(0.5, "public feedback")
        ),
    }

    with pytest.raises(RuntimeError, match="transport interrupted"):
        pipeline.run_round(**kwargs)
    with pytest.raises(IncompleteRoundError, match="solver"):
        pipeline.run_round(**kwargs)
    assert solver.calls == 1


def test_old_lower_trace_cannot_evolve_an_unrelated_current_harness(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    first = artifact()
    workspace.commit(first)
    builder_generator = SequenceGenerator(proposal(first.sha256))
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=SequenceGenerator("must-not-run")),
        builder=BuilderHarness(
            workspace=workspace,
            generator=builder_generator,
            model="builder-model",
        ),
        solver_model="solver-model",
    )
    task = "public task"
    task_sha256 = hashlib.sha256(task.encode()).hexdigest()
    request_sha256 = pipeline._request_sha256(
        task_sha256=task_sha256,
        execution_contract_sha256="c" * 64,
    )
    workspace.record_trace(
        run_id="round-stale",
        harness_sha256=first.sha256,
        candidate="candidate-v1",
        task_sha256=task_sha256,
        request_sha256=request_sha256,
        solver_model="solver-model",
        events=(),
        score=0.5,
        feedback="public feedback",
    )
    next_artifact = type(first)(
        schema_version=1,
        version=2,
        parent_sha256=first.sha256,
        spec=type(first.spec).from_dict(
            {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Different {task}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            }
        ),
    )
    workspace.commit(next_artifact, owner_run_id="another-round")

    with pytest.raises(IncompleteRoundError, match="advanced"):
        pipeline.run_round(
            run_id="round-stale",
            execution_contract_sha256="c" * 64,
            task=task,
            tools={"verify": lambda value: {"passed": True}},
            evaluator=lambda candidate: EvaluationResult(
                public=PublicEvaluation(0.5, "public feedback")
            ),
        )
    assert builder_generator.calls == []


def test_new_round_cannot_advance_past_pending_owned_commit(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    first = artifact()
    workspace.commit(first)
    workspace.claim_operation(
        run_id="round-pending",
        stage="builder",
        request_sha256="e" * 64,
    )
    second = type(first)(
        schema_version=1,
        version=2,
        parent_sha256=first.sha256,
        spec=type(first.spec).from_dict(
            {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Second {task}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            }
        ),
    )
    workspace.commit(second, owner_run_id="round-pending")
    solver = SequenceGenerator("must-not-run")
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=solver),
        builder=BuilderHarness(
            workspace=workspace,
            generator=SequenceGenerator(proposal(second.sha256)),
            model="builder-model",
        ),
        solver_model="solver-model",
    )

    with pytest.raises(IncompleteRoundError, match="round-pending"):
        pipeline.run_round(
            run_id="round-new",
            execution_contract_sha256="c" * 64,
            task="public task",
            tools={"verify": lambda value: {"passed": True}},
            evaluator=lambda candidate: EvaluationResult(
                public=PublicEvaluation(0.5, "public feedback")
            ),
        )
    assert solver.calls == []


def test_abandoned_round_is_terminal_and_cannot_resume(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    builder_generator = SequenceGenerator(proposal(current.sha256))
    pipeline = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=SequenceGenerator("must-not-run")),
        builder=BuilderHarness(
            workspace=workspace,
            generator=builder_generator,
            model="builder-model",
        ),
        solver_model="solver-model",
    )
    task = "public task"
    task_sha256 = hashlib.sha256(task.encode()).hexdigest()
    request_sha256 = pipeline._request_sha256(
        task_sha256=task_sha256,
        execution_contract_sha256="c" * 64,
    )
    workspace.claim_operation(
        run_id="round-abandoned",
        stage="solver",
        request_sha256=request_sha256,
    )
    workspace.record_solver_result(
        run_id="round-abandoned",
        payload={
            "schema_version": 1,
            "run_id": "round-abandoned",
            "request_sha256": request_sha256,
            "task_sha256": task_sha256,
            "solver_model": "solver-model",
            "harness_sha256": current.sha256,
            "candidate": "candidate-v1",
            "events": [],
        },
    )
    workspace.abandon_round("round-abandoned", reason="provider audit closed")
    evaluator_calls: list[str] = []

    with pytest.raises(IncompleteRoundError, match="abandoned"):
        pipeline.run_round(
            run_id="round-abandoned",
            execution_contract_sha256="c" * 64,
            task=task,
            tools={"verify": lambda value: {"passed": True}},
            evaluator=lambda candidate: (
                evaluator_calls.append(candidate)
                or EvaluationResult(public=PublicEvaluation(0.5, "public feedback"))
            ),
        )
    assert evaluator_calls == []
    assert builder_generator.calls == []
    assert workspace.current().sha256 == current.sha256
