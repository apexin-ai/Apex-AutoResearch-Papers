from pathlib import Path

import pytest

from optimization_lab.adapters.base import EvaluationResult, EvaluationStatus
from optimization_lab.adapters.fake import FakeAdapter
from optimization_lab.campaign import CampaignPlan
from optimization_lab.controller import CampaignController, CampaignNotReady
from optimization_lab.dashboard import Dashboard
from optimization_lab.generation import FakeGenerator
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec


VALID_RESPONSE = """A compact candidate follows.
```python
import torch
import torch.nn as nn

class ModelNew(nn.Module):
    def forward(self, x):
        return x
```
"""


def _task() -> TaskSpec:
    return TaskSpec(
        task_id="kernelbench_layernorm",
        display_name="LayerNorm",
        level=1,
        problem_id=40,
        task_path="KernelBench/level1/40_LayerNorm.py",
        task_sha256="a" * 64,
        repository_commit="b" * 40,
        target_gpu="A100 80GB",
        gpu_arch="Ampere",
    )


def _plan(tmp_path: Path, *, ready: bool) -> CampaignPlan:
    kwargs = {}
    if ready:
        kwargs = {
            "executor_model": "fake-fixed-model",
            "model_call_cap_per_lane": 2,
            "gpu_seconds_cap_per_lane": 30.0,
            "api_dollar_cap": 1.0,
            "gpu_dollar_cap": 1.0,
            "p0_clean_confirmed": True,
        }
    return CampaignPlan.build(
        project_root=Path(__file__).parents[1],
        artifact_root=tmp_path / "artifacts",
        **kwargs,
    )


def _adapter() -> FakeAdapter:
    return FakeAdapter(
        EvaluationResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=1.0,
            reference_runtime_ms=2.0,
            gpu_seconds=4.0,
            hardware="fake A100",
        )
    )


def _controller(
    tmp_path: Path,
    *,
    plan: CampaignPlan,
    generator: FakeGenerator,
    adapter: FakeAdapter,
) -> CampaignController:
    root = Path(plan.artifact_root)
    return CampaignController(
        plan=plan,
        project_root=Path(__file__).parents[1],
        registry=ExperimentRegistry(root),
        dashboard=Dashboard(root / "dashboard.html"),
        generator=generator,
        adapter=adapter,
    )


def test_draft_campaign_never_calls_generator_or_adapter(tmp_path: Path) -> None:
    plan = _plan(tmp_path, ready=False)
    generator = FakeGenerator(VALID_RESPONSE, api_cost_usd=0.10)
    adapter = _adapter()
    controller = _controller(
        tmp_path, plan=plan, generator=generator, adapter=adapter
    )

    with pytest.raises(CampaignNotReady, match="execution_ready"):
        controller.run_p1_candidate(
            lane_id="p1:kernelbench_layernorm:generic_zero_shot",
            task=_task(),
            task_card="# LayerNorm task",
            reference_source="class Model: pass",
            candidate_id="generic-v001",
        )

    assert generator.calls == []
    assert adapter.calls == []
    assert controller.budget.model_calls_used == 0
    assert controller.budget.gpu_seconds_used == 0.0


def test_ready_p1_lane_runs_generation_archive_evaluation_feedback_and_ledger(
    tmp_path: Path,
) -> None:
    plan = _plan(tmp_path, ready=True)
    generator = FakeGenerator(VALID_RESPONSE, api_cost_usd=0.10)
    adapter = _adapter()
    controller = _controller(
        tmp_path, plan=plan, generator=generator, adapter=adapter
    )

    card = controller.run_p1_candidate(
        lane_id="p1:kernelbench_layernorm:generic_zero_shot",
        task=_task(),
        task_card="# LayerNorm task",
        reference_source="class Model: pass",
        candidate_id="generic-v001",
    )

    assert card.correct is True
    assert card.speedup_vs_eager == pytest.approx(2.0)
    assert len(generator.calls) == 1
    assert generator.calls[0]["model"] == "fake-fixed-model"
    assert "# LayerNorm task" in generator.calls[0]["prompt"]
    assert len(adapter.calls) == 1
    assert controller.budget.model_calls_used == 1
    assert controller.budget.api_cost_usd_used == pytest.approx(0.10)
    assert controller.budget.gpu_seconds_used == pytest.approx(4.0)

    scope = Path(plan.artifact_root) / "baselines/kernelbench_layernorm/generic_zero_shot"
    assert (scope / "candidates/generic-v001.py").is_file()
    assert (scope / "raw_responses/generic-v001.txt").read_text() == VALID_RESPONSE
    assert (scope / "metadata/generic-v001.json").is_file()

    events = controller.registry.read_events()
    assert [event["event_type"] for event in events] == [
        "generation_started",
        "candidate_generated",
        "candidate_started",
        "candidate_evaluated",
        "lane_candidate_completed",
    ]
    completed = events[-1]["payload"]
    assert completed["lane_id"] == "p1:kernelbench_layernorm:generic_zero_shot"
    assert completed["feedback"]["candidate_id"] == "generic-v001"
    assert completed["budget"]["model_calls_used"] == 1


def test_p1_revision_receives_only_its_lane_feedback_and_previous_candidate(
    tmp_path: Path,
) -> None:
    plan = _plan(tmp_path, ready=True)
    generator = FakeGenerator(VALID_RESPONSE, api_cost_usd=0.10)
    controller = _controller(
        tmp_path, plan=plan, generator=generator, adapter=_adapter()
    )
    first = controller.run_p1_candidate(
        lane_id="p1:kernelbench_layernorm:equal_budget_general",
        task=_task(),
        task_card="# LayerNorm task",
        reference_source="class Model: pass",
        candidate_id="general-v001",
    )

    controller.run_p1_candidate(
        lane_id="p1:kernelbench_layernorm:equal_budget_general",
        task=_task(),
        task_card="# LayerNorm task",
        reference_source="class Model: pass",
        candidate_id="general-v002",
        feedback_history=(first,),
        previous_candidate="class ModelNew: pass",
    )

    second_prompt = generator.calls[1]["prompt"]
    assert "general-v001" in second_prompt
    assert "class ModelNew: pass" in second_prompt
    assert "private_evaluator" not in second_prompt


def test_repeated_candidate_id_never_consumes_generator_or_gpu_twice(
    tmp_path: Path,
) -> None:
    plan = _plan(tmp_path, ready=True)
    generator = FakeGenerator(VALID_RESPONSE, api_cost_usd=0.10)
    adapter = _adapter()
    controller = _controller(
        tmp_path, plan=plan, generator=generator, adapter=adapter
    )
    kwargs = {
        "lane_id": "p1:kernelbench_layernorm:generic_zero_shot",
        "task": _task(),
        "task_card": "# LayerNorm task",
        "reference_source": "class Model: pass",
        "candidate_id": "generic-v001",
    }

    first = controller.run_p1_candidate(**kwargs)
    event_count = len(controller.registry.read_events())
    second = controller.run_p1_candidate(**kwargs)

    assert second == first
    assert len(generator.calls) == 1
    assert len(adapter.calls) == 1
    assert controller.budget.model_calls_used == 1
    assert controller.budget.api_cost_usd_used == pytest.approx(0.10)
    assert controller.budget.gpu_seconds_used == pytest.approx(4.0)
    assert len(controller.registry.read_events()) == event_count

    resumed_generator = FakeGenerator(VALID_RESPONSE, api_cost_usd=0.10)
    resumed_adapter = _adapter()
    resumed = _controller(
        tmp_path,
        plan=plan,
        generator=resumed_generator,
        adapter=resumed_adapter,
    )
    assert resumed.run_p1_candidate(**kwargs) == first
    assert resumed_generator.calls == []
    assert resumed_adapter.calls == []


def test_lane_scoped_controller_restores_budget_before_resume(tmp_path: Path) -> None:
    plan = _plan(tmp_path, ready=True)
    lane_id = "p1:kernelbench_layernorm:equal_budget_general"
    first_generator = FakeGenerator(VALID_RESPONSE, api_cost_usd=0.10)
    first = CampaignController(
        plan=plan,
        project_root=Path(__file__).parents[1],
        registry=ExperimentRegistry(Path(plan.artifact_root)),
        dashboard=Dashboard(Path(plan.artifact_root) / "dashboard.html"),
        generator=first_generator,
        adapter=_adapter(),
        budget_scope_lane_id=lane_id,
    )
    first.run_p1_candidate(
        lane_id=lane_id,
        task=_task(),
        task_card="card",
        reference_source="class Model: pass",
        candidate_id="resume-v001",
    )

    resumed_generator = FakeGenerator(VALID_RESPONSE, api_cost_usd=0.10)
    resumed = CampaignController(
        plan=plan,
        project_root=Path(__file__).parents[1],
        registry=ExperimentRegistry(Path(plan.artifact_root)),
        dashboard=Dashboard(Path(plan.artifact_root) / "dashboard.html"),
        generator=resumed_generator,
        adapter=_adapter(),
        budget_scope_lane_id=lane_id,
    )
    assert resumed.budget.model_calls_used == 1
    assert resumed.budget.gpu_seconds_used == pytest.approx(4.0)
    resumed.run_p1_candidate(
        lane_id=lane_id,
        task=_task(),
        task_card="card",
        reference_source="class Model: pass",
        candidate_id="resume-v002",
    )

    with pytest.raises(RuntimeError, match="model-call"):
        resumed.run_p1_candidate(
            lane_id=lane_id,
            task=_task(),
            task_card="card",
            reference_source="class Model: pass",
            candidate_id="resume-v003",
        )
    assert len(resumed_generator.calls) == 1


def test_api_cap_is_reserved_before_calling_generator(tmp_path: Path) -> None:
    plan = _plan(tmp_path, ready=True)
    generator = FakeGenerator(VALID_RESPONSE, api_cost_usd=1.50)
    adapter = _adapter()
    controller = _controller(
        tmp_path, plan=plan, generator=generator, adapter=adapter
    )

    with pytest.raises(RuntimeError, match="API cost"):
        controller.run_p1_candidate(
            lane_id="p1:kernelbench_layernorm:generic_zero_shot",
            task=_task(),
            task_card="# LayerNorm task",
            reference_source="class Model: pass",
            candidate_id="generic-v001",
        )

    assert generator.calls == []
    assert adapter.calls == []


def test_invalid_generation_is_archived_in_ledger_and_never_reaches_adapter(
    tmp_path: Path,
) -> None:
    plan = _plan(tmp_path, ready=True)
    generator = FakeGenerator("no code block", api_cost_usd=0.10)
    adapter = _adapter()
    controller = _controller(
        tmp_path, plan=plan, generator=generator, adapter=adapter
    )

    with pytest.raises(ValueError, match="one fenced code block"):
        controller.run_p1_candidate(
            lane_id="p1:kernelbench_layernorm:generic_zero_shot",
            task=_task(),
            task_card="# LayerNorm task",
            reference_source="class Model: pass",
            candidate_id="generic-v001",
        )

    assert len(generator.calls) == 1
    assert adapter.calls == []
    assert controller.budget.model_calls_used == 1
    assert [
        event["event_type"] for event in controller.registry.read_events()
    ] == ["generation_started", "candidate_generation_rejected"]
