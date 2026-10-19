from __future__ import annotations

import json
from pathlib import Path

from optimization_lab.generation import GenerationResult
from optimization_lab.harness_builder.builder_harness import BuilderHarness
from optimization_lab.harness_builder.dual_harness import (
    HarnessWorkspace,
    TaskHarnessRuntime,
)
from optimization_lab.harness_builder.dual_runtime import EvaluationResult, PublicEvaluation
from optimization_lab.harness_builder.evolution import (
    CallbackEvaluatorRunner,
    TaskHarnessEvolutionCampaign,
    summarize_harness_change,
)
from test_dual_harness import artifact


class Generator:
    def __init__(self) -> None:
        self.builder_calls = 0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        if "You are the Builder inside a fixed Builder Harness" not in prompt:
            return GenerationResult(raw_response="solver candidate", provider="fixture")
        self.builder_calls += 1
        payload = json.loads(prompt.rsplit("\n\n", 1)[1])
        current = payload["current_harness_and_public_runs"]["current_artifact"]
        current["spec"]["nodes"][0]["prompt"] += f" mutation-{self.builder_calls}"
        proposal = {
            "schema_version": 1,
            "base_sha256": payload["current_harness_and_public_runs"]["current_sha256"],
            "reason": "explore a task-local workflow change",
            "expected_effect": "preserve execution while testing a different workflow",
            "artifact": current["spec"],
        }
        return GenerationResult(raw_response=json.dumps(proposal), provider="fixture")


class Adapter:
    contract_sha256 = "a" * 64
    solver_model = "fixture-solver"
    task = "task-1"

    def __init__(self) -> None:
        self.scores = iter((0.5, 0.4, 0.3))

    def task_prompt(self, task: str) -> str:
        return task

    def tools(self, task: str):
        return {"verify": lambda value: value}

    def evaluator(self, task: str):
        return CallbackEvaluatorRunner(self.evaluate)

    def evaluate(self, candidate: str) -> EvaluationResult:
        return EvaluationResult(PublicEvaluation(next(self.scores), "public feedback"))

    def probe(self, task: str, artifact):
        return True

    def preserves_capability(self, task: str, previous, current):
        return True, "fixture capability contract preserved"


def test_generic_evolution_runner_keeps_best_and_stops_on_patience(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    generator = Generator()
    builder = BuilderHarness(workspace=workspace, generator=generator, model="fixture-builder")
    result = TaskHarnessEvolutionCampaign(
        workspace=workspace,
        adapter=Adapter(),
        task_runtime=TaskHarnessRuntime(generator=generator),
        builder=builder,
    ).run(run_id="generic-lineage", max_rounds=3, patience=2)

    assert len(result.rounds) == 3
    assert result.stop_reason == "patience_exhausted"
    assert result.best_score == 0.5
    assert result.assessments[0].disposition == "accepted_improvement"
    assert result.assessments[1].disposition == "accepted_exploration"
    assert result.assessments[1].score_delta_vs_best == -0.1
    assert all(item.verifiable for item in result.assessments)
    assert all(item.attributable for item in result.assessments)
    assert all(item.rollbackable for item in result.assessments)
    assert workspace.champion().sha256 == result.best_harness_sha256
    assessment = workspace.load_round_assessment("generic-lineage-round-002")
    assert assessment is not None
    assert assessment["change_summary"]["changed"] is True
    assert assessment["assessment"]["disposition"] == "accepted_exploration"


def test_callback_evaluator_runner_rejects_untyped_results() -> None:
    runner = CallbackEvaluatorRunner(lambda candidate: EvaluationResult(PublicEvaluation(0.1, "ok")))
    assert runner.evaluate("candidate").public.score == 0.1


def test_change_summary_attributes_v2_state_changes() -> None:
    previous = artifact()
    payload = previous.to_dict()
    payload["spec"] = {
        "schema_version": 2,
        "nodes": payload["spec"]["nodes"],
        "interface": {},
        "memory": {},
        "capabilities": {"tools": [], "skills": [{"id": "diagnose", "prompt": "one"}]},
        "router": {},
    }
    current = type(previous).from_dict(
        {
            **payload,
            "version": 2,
            "parent_sha256": previous.sha256,
        }
    )
    summary = summarize_harness_change(previous, current)
    assert summary["changed"] is True
    assert summary["changed_components"] == ["capabilities"]
