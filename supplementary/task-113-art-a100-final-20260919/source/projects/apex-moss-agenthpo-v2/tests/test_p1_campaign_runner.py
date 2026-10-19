from pathlib import Path

import pytest

from optimization_lab.adapters.base import EvaluationResult, EvaluationStatus
from optimization_lab.adapters.fake import FakeAdapter
from optimization_lab.campaign import CampaignPlan
from optimization_lab.dashboard import Dashboard
from optimization_lab.generation import FakeGenerator
from optimization_lab.feedback import FeedbackCard
from optimization_lab.p1_runner import P1CampaignRunner, P1EnvironmentBlocked
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec


VALID_RESPONSE = """```python
class ModelNew:
    pass
```
"""


def _task(task_id: str, level: int, problem_id: int) -> TaskSpec:
    return TaskSpec(
        task_id=task_id,
        display_name=task_id,
        level=level,
        problem_id=problem_id,
        task_path=f"KernelBench/level{level}/task.py",
        task_sha256="a" * 64,
        repository_commit="b" * 40,
        target_gpu="A100",
        gpu_arch="Ampere",
    )


def test_p1_runner_executes_frozen_six_lane_schedule_and_never_enters_p2(
    tmp_path: Path,
) -> None:
    plan = CampaignPlan.build(
        project_root=Path(__file__).parents[1],
        artifact_root=tmp_path / "artifacts",
        executor_model="fixed-model",
        model_call_cap_per_lane=15,
        gpu_seconds_cap_per_lane=3600.0,
        api_dollar_cap=100.0,
        gpu_dollar_cap=100.0,
        p0_clean_confirmed=True,
    )
    registry = ExperimentRegistry(Path(plan.artifact_root))
    plan.write(Path(plan.artifact_root) / "campaign_plan.json")
    generator = FakeGenerator(VALID_RESPONSE)
    adapter = FakeAdapter(
        EvaluationResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=1.0,
            reference_runtime_ms=2.0,
            gpu_seconds=3.0,
            hardware="fake A100",
        )
    )
    tasks = {
        "kernelbench_layernorm": _task("kernelbench_layernorm", 1, 40),
        "kernelbench_matmul_sigmoid_sum": _task(
            "kernelbench_matmul_sigmoid_sum", 2, 56
        ),
    }
    runner = P1CampaignRunner(
        plan=plan,
        project_root=Path(__file__).parents[1],
        registry=registry,
        dashboard=Dashboard(Path(plan.artifact_root) / "dashboard.html"),
        generator=generator,
        adapter=adapter,
        tasks=tasks,
        task_cards={task_id: "task card" for task_id in tasks},
        reference_sources={task_id: "class Model: pass" for task_id in tasks},
    )

    summary = runner.run()

    assert summary["candidate_count"] == 22
    assert summary["lane_count"] == 6
    assert len(generator.calls) == 22
    assert len(adapter.calls) == 22
    events = registry.read_events()
    assert events[-1]["event_type"] == "phase_changed"
    assert events[-1]["payload"] == {
        "phase": "P1",
        "status": "completed",
        "detail": "六组冻结基线已完成",
    }
    assert not any(event["event_type"].startswith("p2") for event in events)
    page = (Path(plan.artifact_root) / "dashboard.html").read_text(encoding="utf-8")
    assert "当前阶段：P1 已完成，P2 待授权" in page
    assert "<td>P1</td><td>固定 Harness 对照（含同预算组）</td><td>已完成</td>" in page
    assert page.count("已完成 1/1") == 2
    assert page.count("已完成 8/8") == 2
    assert page.count("已完成 2/2") == 2
    assert "模型调用：22 次" in page

    resumed_generator = FakeGenerator(VALID_RESPONSE)
    resumed_adapter = FakeAdapter(adapter.result)
    resumed = P1CampaignRunner(
        plan=plan,
        project_root=Path(__file__).parents[1],
        registry=registry,
        dashboard=Dashboard(Path(plan.artifact_root) / "dashboard.html"),
        generator=resumed_generator,
        adapter=resumed_adapter,
        tasks=tasks,
        task_cards={task_id: "task card" for task_id in tasks},
        reference_sources={task_id: "class Model: pass" for task_id in tasks},
    )
    assert resumed.run()["candidate_count"] == 22
    assert resumed_generator.calls == []
    assert resumed_adapter.calls == []


def test_p1_runner_resumes_from_append_only_evaluation_correction(
    tmp_path: Path,
) -> None:
    plan = CampaignPlan.build(
        project_root=Path(__file__).parents[1],
        artifact_root=tmp_path / "artifacts",
        executor_model="fixed-model",
        model_call_cap_per_lane=15,
        gpu_seconds_cap_per_lane=3600.0,
        api_dollar_cap=100.0,
        gpu_dollar_cap=100.0,
        p0_clean_confirmed=True,
    )
    registry = ExperimentRegistry(Path(plan.artifact_root))
    tasks = {
        "kernelbench_layernorm": _task("kernelbench_layernorm", 1, 40),
        "kernelbench_matmul_sigmoid_sum": _task(
            "kernelbench_matmul_sigmoid_sum", 2, 56
        ),
    }
    common = {
        "plan": plan,
        "project_root": Path(__file__).parents[1],
        "registry": registry,
        "dashboard": Dashboard(Path(plan.artifact_root) / "dashboard.html"),
        "tasks": tasks,
        "task_cards": {task_id: "task card" for task_id in tasks},
        "reference_sources": {task_id: "class Model: pass" for task_id in tasks},
    }
    first_generator = FakeGenerator(VALID_RESPONSE)
    first = P1CampaignRunner(
        **common,
        generator=first_generator,
        adapter=FakeAdapter(
            EvaluationResult(
                status=EvaluationStatus.ENVIRONMENT_INVALID,
                compiled=False,
                correct=False,
                error_summary="misclassified static policy rejection",
            )
        ),
    )

    with pytest.raises(P1EnvironmentBlocked):
        first.run()

    evaluated = next(
        event
        for event in registry.read_events()
        if event["event_type"] == "candidate_evaluated"
    )
    corrected_result = EvaluationResult(
        status=EvaluationStatus.POLICY_REJECTED,
        compiled=False,
        correct=False,
        error_summary="Missing @triton.jit",
        elapsed_seconds=2.0,
        gpu_seconds=2.0,
        hardware="A100",
    )
    corrected_card = FeedbackCard.from_result(
        tasks["kernelbench_layernorm"],
        "p1-layernorm-zero-shot-v001",
        corrected_result,
    )
    registry.append(
        "candidate_evaluation_corrected",
        {
            "lane_id": "p1:kernelbench_layernorm:generic_zero_shot",
            "task_id": "kernelbench_layernorm",
            "candidate_id": "p1-layernorm-zero-shot-v001",
            "candidate_sha256": evaluated["payload"]["candidate_sha256"],
            "evaluation": corrected_result.to_dict(),
            "feedback": corrected_card.to_dict(),
            "detail": "parser bug corrected without rerunning the candidate",
            "supersedes_event_id": evaluated["event_id"],
        },
        event_id="candidate-evaluation-corrected:test",
    )

    resumed_generator = FakeGenerator(VALID_RESPONSE)
    resumed_adapter = FakeAdapter(
        EvaluationResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=1.0,
            reference_runtime_ms=2.0,
            gpu_seconds=3.0,
            hardware="fake A100",
        )
    )
    resumed = P1CampaignRunner(
        **common,
        generator=resumed_generator,
        adapter=resumed_adapter,
    )

    summary = resumed.run()

    assert summary["candidate_count"] == 22
    assert len(first_generator.calls) == 1
    assert len(resumed_generator.calls) == 21
    assert len(resumed_adapter.calls) == 21
    page = (Path(plan.artifact_root) / "dashboard.html").read_text(encoding="utf-8")
    assert "<td>LayerNorm</td><td>11</td><td>11</td><td>10</td>" in page
    assert "environment_invalid" not in page
