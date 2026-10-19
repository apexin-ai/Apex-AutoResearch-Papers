from __future__ import annotations

from pathlib import Path
import json

import pytest

from optimization_lab.generation import FakeGenerator, GenerationResult, InvalidCandidate
from optimization_lab.harness_builder.dual_harness import HarnessWorkspace, TaskHarnessArtifact
from optimization_lab.harness_builder.dual_runtime import IncompleteRoundError
from optimization_lab.harness_builder.simpletes_scaling import (
    ClaimedGenerator,
    SIMPLETES_MODEL,
    SIMPLETES_MODEL_REVISION,
    SIMPLETES_TASKS,
    SimpleTESProgram,
    SimpleTESEvaluation,
    HarnessScore,
    SimpleTESHarnessEvolutionRound,
    SimpleTESPortfolioCampaign,
    SimpleTESHarnessEvolutionCampaign,
    SimpleTESScalingContract,
    initial_simpletes_harness,
)


VALID = """```python
import numpy as np

def scaling_law_func(data_points, params):
    return np.zeros(len(data_points)) + params[0]

def fit_scaling_law(data_points, loss_values):
    return np.array([np.mean(loss_values)])
```"""


def test_simpletes_contract_freezes_paper_model_budget_and_four_tasks() -> None:
    contract = SimpleTESScalingContract()

    assert contract.model == SIMPLETES_MODEL == "gpt-oss-120b"
    assert contract.model_revision == SIMPLETES_MODEL_REVISION
    assert contract.model_revision == "b5c939de8f754692c1647ca79fbf85e8c1e70f8a"
    assert (contract.official_c, contract.official_l, contract.official_k) == (16, 20, 16)
    assert contract.first_round_harnesses == 8
    assert {task.label for task in SIMPLETES_TASKS} == {
        "parallel",
        "domain_mix",
        "lr_bsz",
        "u_shape",
    }
    assert len(contract.sha256) == 64


def test_scaling_program_codec_requires_functions_and_denies_io() -> None:
    program = SimpleTESProgram.from_response(VALID)
    assert "fit_scaling_law" in program.code

    with pytest.raises(InvalidCandidate, match="both"):
        SimpleTESProgram.from_response("```python\ndef scaling_law_func(x, p): return x\n```")
    with pytest.raises(InvalidCandidate, match="denied"):
        SimpleTESProgram.from_response(
            "```python\nimport os\ndef scaling_law_func(x,p): return x\n"
            "def fit_scaling_law(x,y): return y\n```"
        )


def test_claimed_generator_replays_result_and_fails_closed_on_orphan(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    underlying = FakeGenerator("response")
    wrapped = ClaimedGenerator(
        workspace=workspace,
        generator=underlying,
        run_id="portfolio-001",
        stage="builder-001",
        contract_sha256="c" * 64,
    )

    first = wrapped.generate("prompt", model="gpt-oss-120b")
    replay = wrapped.generate("prompt", model="gpt-oss-120b")

    assert first.raw_response == replay.raw_response == "response"
    assert len(underlying.calls) == 1

    workspace.claim_operation(
        run_id="portfolio-002",
        stage="solver-001",
        request_sha256="d" * 64,
    )
    orphan = ClaimedGenerator(
        workspace=workspace,
        generator=underlying,
        run_id="portfolio-002",
        stage="solver-001",
        contract_sha256="c" * 64,
    )
    with pytest.raises((IncompleteRoundError, ValueError)):
        orphan.generate("prompt", model="gpt-oss-120b")


def test_initial_harness_is_content_addressed_and_emits_solver_output() -> None:
    harness = initial_simpletes_harness()

    assert harness.version == 1
    assert harness.parent_sha256 is None
    assert harness.spec.nodes[-1].kind == "emit"
    assert len(harness.sha256) == 64


def test_portfolio_campaign_generates_and_gates_a_new_harness(tmp_path: Path) -> None:
    initial = initial_simpletes_harness()
    changed = initial.spec.to_dict()
    changed["nodes"][0]["prompt"] = "Use asymptotic structure first.\n\n{task}"
    builder_response = json.dumps(
        {
            "schema_version": 1,
            "base_sha256": initial.sha256,
            "reason": "focus on asymptotic structure",
            "expected_effect": "improve extrapolation",
            "artifact": changed,
        }
    )

    class RoutingGenerator:
        def __init__(self) -> None:
            self.calls = []

        def estimated_api_cost_usd(self) -> float:
            return 0.0

        def generate(self, prompt: str, *, model: str) -> GenerationResult:
            self.calls.append((prompt, model))
            response = builder_response if "fixed portfolio Builder" in prompt else VALID
            return GenerationResult(raw_response=response, provider="fixture")

    class Evaluator:
        worker_path = Path(__file__)

        def evaluate(self, *, task, program):
            return SimpleTESEvaluation(task.label, 0.25, True, None, "ok")

    source = tmp_path / "simpletes"
    for task in SIMPLETES_TASKS:
        root = source / "datasets" / "scaling_law" / task.directory
        root.mkdir(parents=True)
        (root / f"{task.directory}.txt").write_text("instruction", encoding="utf-8")
        (root / "init_program.py").write_text("# seed", encoding="utf-8")
        published = source / task.published_best
        published.parent.mkdir(parents=True, exist_ok=True)
        published.write_text(VALID.removeprefix("```python\n").removesuffix("```"), encoding="utf-8")
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(initial)
    generator = RoutingGenerator()
    campaign = SimpleTESPortfolioCampaign(
        workspace=workspace,
        source_root=source,
        generator=generator,
        evaluator=Evaluator(),
        contract=SimpleTESScalingContract(first_round_harnesses=1),
        reporter=lambda message: None,
    )

    result = campaign.run(run_id="simpletes-test")

    assert len(result.scores) == 1
    assert len(workspace.archived_candidates()) == 1
    assert len(workspace.gate_decisions()) == 1
    assert result.portfolio.next_champion_sha256 == initial.sha256
    assert len(generator.calls) == 9


def test_task_lineage_scores_then_builds_sequentially(tmp_path: Path) -> None:
    source = tmp_path / "simpletes"
    for task in SIMPLETES_TASKS:
        root = source / "datasets" / "scaling_law" / task.directory
        root.mkdir(parents=True)
        (root / f"{task.directory}.txt").write_text(
            f"instruction for {task.label}", encoding="utf-8"
        )
        (root / "init_program.py").write_text("# seed", encoding="utf-8")
        published = source / task.published_best
        published.parent.mkdir(parents=True, exist_ok=True)
        published.write_text(
            VALID.removeprefix("```python\n").removesuffix("```"),
            encoding="utf-8",
        )

    initial = initial_simpletes_harness()
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(initial)

    class SequentialGenerator:
        def __init__(self) -> None:
            self.calls: list[tuple[str, str]] = []
            self.solver_calls = 0
            self.builder_calls = 0

        def estimated_api_cost_usd(self) -> float:
            return 0.0

        def generate(self, prompt: str, *, model: str) -> GenerationResult:
            self.calls.append((prompt, model))
            if "You are the Builder inside a fixed Builder Harness" not in prompt:
                self.solver_calls += 1
                return GenerationResult(raw_response=VALID, provider="fixture")
            self.builder_calls += 1
            payload = json.loads(prompt.rsplit("\n\n", 1)[1])
            inspection = payload["current_harness_and_public_runs"]
            current = inspection["current_artifact"]
            changed = json.loads(json.dumps(current))
            changed["spec"]["nodes"][0]["prompt"] += f"\nlineage mutation {self.builder_calls}"
            return GenerationResult(
                raw_response=json.dumps(
                    {
                        "schema_version": 1,
                        "base_sha256": inspection["current_sha256"],
                        "reason": f"task-local mutation {self.builder_calls}",
                        "expected_effect": "use the prior task trace",
                        "artifact": {
                            "schema_version": 1,
                            "nodes": changed["spec"]["nodes"],
                        },
                    }
                ),
                provider="fixture",
            )

    class Evaluator:
        worker_path = Path(__file__)

        def __init__(self) -> None:
            self.calls: list[str] = []

        def evaluate(self, *, task, program):
            self.calls.append(task.label)
            return SimpleTESEvaluation(task.label, 0.25, True, None, "ok")

    generator = SequentialGenerator()
    evaluator = Evaluator()
    task = next(item for item in SIMPLETES_TASKS if item.label == "lr_bsz")
    campaign = SimpleTESHarnessEvolutionCampaign(
        workspace=workspace,
        source_root=source,
        generator=generator,
        evaluator=evaluator,
        task=task,
        reporter=lambda message: None,
    )

    # The Builder probe executes the proposed Harness with a fixture model,
    # including prompts that contain Python f-string braces.
    probe_artifact = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 2,
            "parent_sha256": initial.sha256,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Generate code for {task}; preserve f'{P}' literally.",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    assert campaign._probe_harness(probe_artifact) is True

    result = campaign.run(run_id="simpletes-task-lineage")

    assert len(result.rounds) == 8
    assert generator.solver_calls == 8
    assert generator.builder_calls == 7
    assert [
        "builder" if "You are the Builder inside a fixed Builder Harness" in prompt else "solver"
        for prompt, _ in generator.calls
    ] == ["solver", "builder"] * 7 + ["solver"]
    assert evaluator.calls == ["lr_bsz"] * 8
    trace = workspace.load_trace("simpletes-task-lineage-round-001-trace")
    assert trace is not None
    assert trace["score"] == 0.25
    assert trace["feedback"] == "ok"
    assert len(workspace.promotion_receipts()) == 0
    assert result.rounds[-1].builder is None
    assert result.rounds[0].score.task_scores[0].task == "lr_bsz"
    assert result.final_champion_sha256 != initial.sha256

    # Rebuilding the lineage receipt from sealed rounds must not re-dispatch calls.
    workspace.round_receipt_bindings_root.joinpath("simpletes-task-lineage.json").unlink()
    replay_generator = SequentialGenerator()
    replay = SimpleTESHarnessEvolutionCampaign(
        workspace=workspace,
        source_root=source,
        generator=replay_generator,
        evaluator=evaluator,
        task=task,
        reporter=lambda message: None,
    ).run(run_id="simpletes-task-lineage")
    assert len(replay.rounds) == 8
    assert replay_generator.calls == []


def test_task_lineage_restores_best_harness_after_score_regression(tmp_path: Path) -> None:
    source = tmp_path / "simpletes"
    task = next(item for item in SIMPLETES_TASKS if item.label == "lr_bsz")
    initial = initial_simpletes_harness()
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(initial)

    class Evaluator:
        worker_path = Path(__file__)

    campaign = SimpleTESHarnessEvolutionCampaign(
        workspace=workspace,
        source_root=source,
        generator=FakeGenerator("unused"),
        evaluator=Evaluator(),
        task=task,
        reporter=lambda message: None,
    )
    regressed = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 2,
            "parent_sha256": initial.sha256,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Changed {task}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    workspace.commit(regressed)
    prior = SimpleTESHarnessEvolutionRound(
        round_index=1,
        run_id="lineage-round-001",
        task=task.label,
        score=HarnessScore(
            harness_sha256=initial.sha256,
            task_scores=(SimpleTESEvaluation(task.label, 0.9, True, None, "ok"),),
        ),
        builder=None,
    )

    restore = campaign._restore_to_historical_best(
        round_id="lineage-round-002",
        current=regressed,
        score=HarnessScore(
            harness_sha256=regressed.sha256,
            task_scores=(SimpleTESEvaluation(task.label, 0.2, True, None, "ok"),),
        ),
        prior_rounds=[prior],
    )

    assert restore is not None
    assert restore["historical_best_sha256"] == initial.sha256
    assert workspace.current().parent_sha256 == regressed.sha256
    assert workspace.current().spec == initial.spec
