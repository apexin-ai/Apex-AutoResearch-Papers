from pathlib import Path

import pytest

from optimization_lab.adapters.base import EvaluationResult, EvaluationStatus
from optimization_lab.adapters.fake import FakeAdapter
from optimization_lab.campaign import CampaignPlan
from optimization_lab.dashboard import Dashboard
from optimization_lab.generation import FakeGenerator
from optimization_lab.p2_runner import P2CampaignRunner
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec


CANDIDATE_RESPONSE = """```python
class ModelNew:
    pass
```
"""
HARNESS_RESPONSE = """# Revised task-specialist Harness

1. Read this lineage's compact feedback.
2. Preserve correctness before changing one optimization idea.
3. Keep the fixed model, evaluator, GPU, and budget unchanged.
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


def test_p2_runner_evolves_six_isolated_harness_lineages_and_stops_before_p3(
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
    artifact_root = Path(plan.artifact_root)
    plan.write(artifact_root / "campaign_plan.json")
    registry = ExperimentRegistry(artifact_root)
    registry.append(
        "phase_changed",
        {"phase": "P1", "status": "completed", "detail": "fixture"},
        event_id="phase:P1:completed",
    )
    candidate_generator = FakeGenerator(CANDIDATE_RESPONSE)
    harness_generator = FakeGenerator(HARNESS_RESPONSE)
    adapter = FakeAdapter(
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
        "dashboard": Dashboard(artifact_root / "dashboard.html"),
        "candidate_generator": candidate_generator,
        "harness_generator": harness_generator,
        "adapter": adapter,
        "tasks": tasks,
        "task_cards": {task_id: "task card" for task_id in tasks},
        "reference_sources": {task_id: "class Model: pass" for task_id in tasks},
    }

    summary = P2CampaignRunner(**common).run()

    assert summary == {
        "lineage_count": 6,
        "candidate_count": 24,
        "correct_count": 24,
        "harness_model_calls": 18,
    }
    assert len(candidate_generator.calls) == 24
    assert len(harness_generator.calls) == 18
    assert len(adapter.calls) == 24
    events = registry.read_events()
    assert events[-1]["event_type"] == "phase_changed"
    assert events[-1]["payload"] == {
        "phase": "P2",
        "status": "completed",
        "detail": "六条任务专用 Harness 谱系已停止并冻结",
    }
    assert not any(event["event_type"].startswith("p3") for event in events)
    completed = [e for e in events if e["event_type"] == "p2_lineage_completed"]
    assert len(completed) == 6
    assert {e["payload"]["valid_rounds"] for e in completed} == {4}
    assert {e["payload"]["stop_reason"] for e in completed} == {
        "three_rounds_without_speed_improvement"
    }

    seed_hashes = set()
    for lineage in plan.lineages:
        scope = artifact_root / lineage.history_scope
        seed = scope / "harnesses/v001.md"
        assert seed.is_file()
        seed_hashes.add(seed.read_bytes())
        assert (scope / "harnesses/v004.md").is_file()
        assert len(list((scope / "candidates").glob("*.py"))) == 4
    assert len(seed_hashes) == 1

    page = (artifact_root / "dashboard.html").read_text(encoding="utf-8")
    assert "当前阶段：P2 已完成，P3 待授权" in page
    assert page.count("已停止 4/8") == 6
    assert page.count("Harness v004") == 6
    assert "模型调用：42 次" in page

    resumed_candidate_generator = FakeGenerator(CANDIDATE_RESPONSE)
    resumed_harness_generator = FakeGenerator(HARNESS_RESPONSE)
    resumed_adapter = FakeAdapter(adapter.result)
    resumed = P2CampaignRunner(
        **{
            **common,
            "candidate_generator": resumed_candidate_generator,
            "harness_generator": resumed_harness_generator,
            "adapter": resumed_adapter,
        }
    )

    assert resumed.run() == summary
    assert resumed_candidate_generator.calls == []
    assert resumed_harness_generator.calls == []
    assert resumed_adapter.calls == []


def test_p2_harness_optimizer_prompt_is_lineage_local(tmp_path: Path) -> None:
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
    artifact_root = Path(plan.artifact_root)
    registry = ExperimentRegistry(artifact_root)
    registry.append(
        "phase_changed",
        {"phase": "P1", "status": "completed", "detail": "fixture"},
        event_id="phase:P1:completed",
    )
    candidate_generator = FakeGenerator(CANDIDATE_RESPONSE)
    harness_generator = FakeGenerator(HARNESS_RESPONSE)
    tasks = {
        "kernelbench_layernorm": _task("kernelbench_layernorm", 1, 40),
        "kernelbench_matmul_sigmoid_sum": _task(
            "kernelbench_matmul_sigmoid_sum", 2, 56
        ),
    }
    runner = P2CampaignRunner(
        plan=plan,
        project_root=Path(__file__).parents[1],
        registry=registry,
        dashboard=Dashboard(artifact_root / "dashboard.html"),
        candidate_generator=candidate_generator,
        harness_generator=harness_generator,
        adapter=FakeAdapter(
            EvaluationResult(
                status=EvaluationStatus.VALID,
                compiled=True,
                correct=True,
                candidate_runtime_ms=1.0,
                reference_runtime_ms=2.0,
                gpu_seconds=1.0,
            )
        ),
        tasks=tasks,
        task_cards={task_id: "task card" for task_id in tasks},
        reference_sources={task_id: "class Model: pass" for task_id in tasks},
    )

    runner.run()

    first_prompt = harness_generator.calls[0]["prompt"]
    assert "p2-layernorm-r00-v001" in first_prompt
    assert "p2-layernorm-r01" not in first_prompt
    assert "kernelbench_matmul_sigmoid_sum" not in first_prompt
    assert "private_evaluator" not in first_prompt


def test_p2_resume_safely_stops_lineage_after_interrupted_harness_call(
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
    artifact_root = Path(plan.artifact_root)
    registry = ExperimentRegistry(artifact_root)
    registry.append(
        "phase_changed",
        {"phase": "P1", "status": "completed", "detail": "fixture"},
        event_id="phase:P1:completed",
    )
    lane_id = "p2:kernelbench_layernorm:r00"
    registry.append(
        "generation_started",
        {
            "lane_id": lane_id,
            "task_id": "kernelbench_layernorm",
            "candidate_id": "p2-layernorm-r00-harness-v002",
            "generation_kind": "harness",
            "harness_version_id": "v002",
            "executor_model": "fixed-model",
            "prompt_sha256": "c" * 64,
            "reserved_api_cost_usd": 0.0,
        },
        event_id="fixture:interrupted-harness-v002",
    )
    tasks = {
        "kernelbench_layernorm": _task("kernelbench_layernorm", 1, 40),
        "kernelbench_matmul_sigmoid_sum": _task(
            "kernelbench_matmul_sigmoid_sum", 2, 56
        ),
    }
    candidate_generator = FakeGenerator(CANDIDATE_RESPONSE)
    harness_generator = FakeGenerator(HARNESS_RESPONSE)
    runner = P2CampaignRunner(
        plan=plan,
        project_root=Path(__file__).parents[1],
        registry=registry,
        dashboard=Dashboard(artifact_root / "dashboard.html"),
        candidate_generator=candidate_generator,
        harness_generator=harness_generator,
        adapter=FakeAdapter(
            EvaluationResult(
                status=EvaluationStatus.VALID,
                compiled=True,
                correct=True,
                candidate_runtime_ms=1.0,
                reference_runtime_ms=2.0,
                gpu_seconds=1.0,
            )
        ),
        tasks=tasks,
        task_cards={task_id: "task card" for task_id in tasks},
        reference_sources={task_id: "class Model: pass" for task_id in tasks},
    )

    summary = runner.run()

    assert summary["lineage_count"] == 6
    assert summary["candidate_count"] == 21
    assert len(candidate_generator.calls) == 21
    assert len(harness_generator.calls) == 15
    stopped = [
        event
        for event in registry.read_events()
        if event["event_type"] == "p2_lineage_recovery_stopped"
    ]
    assert len(stopped) == 1
    assert stopped[0]["payload"]["lane_id"] == lane_id
    completed = [
        event
        for event in registry.read_events()
        if event["event_type"] == "p2_lineage_completed"
        and event["payload"]["lane_id"] == lane_id
    ]
    assert completed[0]["payload"]["valid_rounds"] == 1
    assert completed[0]["payload"]["stop_reason"] == (
        "incomplete_harness_generation_preserved"
    )


def test_p2_refuses_to_start_without_audited_p1_completion(tmp_path: Path) -> None:
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
    task = _task("kernelbench_layernorm", 1, 40)
    other = _task("kernelbench_matmul_sigmoid_sum", 2, 56)
    tasks = {task.task_id: task, other.task_id: other}

    with pytest.raises(ValueError, match="P1 completion"):
        P2CampaignRunner(
            plan=plan,
            project_root=Path(__file__).parents[1],
            registry=ExperimentRegistry(Path(plan.artifact_root)),
            dashboard=Dashboard(Path(plan.artifact_root) / "dashboard.html"),
            candidate_generator=FakeGenerator(CANDIDATE_RESPONSE),
            harness_generator=FakeGenerator(HARNESS_RESPONSE),
            adapter=FakeAdapter(
                EvaluationResult(
                    status=EvaluationStatus.VALID,
                    compiled=True,
                    correct=True,
                    candidate_runtime_ms=1.0,
                    reference_runtime_ms=2.0,
                )
            ),
            tasks=tasks,
            task_cards={task_id: "card" for task_id in tasks},
            reference_sources={task_id: "class Model: pass" for task_id in tasks},
        )
