import json
from pathlib import Path

import pytest

from optimization_lab.campaign import (
    ACTIVE_TASK_IDS,
    BASELINE_KINDS,
    CampaignPlan,
)
from optimization_lab.budget import BudgetExceeded, ExperimentBudget
from optimization_lab.cli import prepare_campaign
from optimization_lab.dashboard import Dashboard
from optimization_lab.feedback import FeedbackCard
from optimization_lab.optimizer import LineageTracker
from optimization_lab.registry import ExperimentRegistry


def _feedback(
    *,
    candidate_id: str,
    correct: bool,
    speedup: float | None = None,
    valid_run: bool = True,
    outcome: str | None = None,
) -> FeedbackCard:
    if outcome is None:
        outcome = "valid" if correct else "incorrect"
    return FeedbackCard(
        task_id="kernelbench_layernorm",
        candidate_id=candidate_id,
        outcome=outcome,
        valid_run=valid_run,
        stage_reached=("performance" if correct else "correctness"),
        compiled=valid_run,
        correct=correct,
        speedup_vs_eager=speedup,
        candidate_runtime_ms=(1.0 if correct else None),
        reference_runtime_ms=(speedup if correct else None),
        error_summary="",
        next_action="",
        gpu_seconds=10.0 if valid_run else 0.0,
        hardware="A100",
    )


def test_campaign_has_three_fair_baselines_and_three_isolated_lineages_per_task(
    tmp_path: Path,
) -> None:
    plan = CampaignPlan.build(
        project_root=Path(__file__).parents[1],
        artifact_root=tmp_path,
        executor_model="fixed-model",
        model_call_cap_per_lane=8,
        gpu_seconds_cap_per_lane=3600.0,
        api_dollar_cap=100.0,
        gpu_dollar_cap=100.0,
        p0_clean_confirmed=True,
    )

    assert plan.execution_ready is True
    for task_id in ACTIVE_TASK_IDS:
        baselines = [lane for lane in plan.baselines if lane.task_id == task_id]
        assert {lane.kind for lane in baselines} == set(BASELINE_KINDS)
        assert {lane.model_call_cap for lane in baselines} == {8}
        assert {lane.gpu_seconds_cap for lane in baselines} == {3600.0}
        assert all(lane.allow_harness_mutation is False for lane in baselines)

        lineages = [lane for lane in plan.lineages if lane.task_id == task_id]
        assert len(lineages) == 3
        assert len({lane.seed_sha256 for lane in lineages}) == 1
        assert len({lane.history_scope for lane in lineages}) == 3
        assert {lane.max_rounds for lane in lineages} == {8}

    output = tmp_path / "campaign.json"
    plan.write(output)
    assert CampaignPlan.read(output) == plan


def test_draft_campaign_is_not_executable_without_p0_model_and_hard_caps(
    tmp_path: Path,
) -> None:
    plan = CampaignPlan.build(
        project_root=Path(__file__).parents[1],
        artifact_root=tmp_path,
    )

    assert plan.execution_ready is False
    assert set(plan.blockers) == {
        "p0_clean_confirmation_missing",
        "executor_model_missing",
        "model_call_cap_missing",
        "gpu_seconds_cap_missing",
        "api_dollar_cap_missing",
        "gpu_dollar_cap_missing",
    }

    output = tmp_path / "campaign_plan.json"
    plan.write(output)
    saved = json.loads(output.read_text(encoding="utf-8"))
    assert saved["execution_ready"] is False
    assert saved["model_calls_consumed"] == 0
    assert saved["gpu_seconds_consumed"] == 0.0


def test_campaign_rejects_artifact_paths_inside_worktree(tmp_path: Path) -> None:
    worktree_artifacts = (
        Path(__file__).parents[1]
        / ".claude-manager"
        / "worktrees"
        / "unsafe-results"
    )

    with pytest.raises(ValueError, match="worktree"):
        CampaignPlan.build(
            project_root=Path(__file__).parents[1],
            artifact_root=worktree_artifacts,
        )


def test_prepare_campaign_records_a_draft_without_consuming_resources(
    tmp_path: Path,
) -> None:
    artifact_root = tmp_path / "artifacts"

    result = prepare_campaign(
        artifact_root=artifact_root,
        project_root=Path(__file__).parents[1],
        executor_model=None,
        model_call_cap_per_lane=None,
        gpu_seconds_cap_per_lane=None,
        api_dollar_cap=None,
        gpu_dollar_cap=None,
    )

    assert result == 0
    plan = json.loads((artifact_root / "campaign_plan.json").read_text())
    assert plan["execution_ready"] is False
    assert plan["model_calls_consumed"] == 0
    ledger = [
        json.loads(line)
        for line in (artifact_root / "ledger.jsonl").read_text().splitlines()
    ]
    assert ledger[-1]["event_type"] == "campaign_prepared"
    assert ledger[-1]["payload"]["status"] == "blocked_pending_approval"


def test_dashboard_explains_the_frozen_campaign_without_reporting_scores(
    tmp_path: Path,
) -> None:
    artifact_root = tmp_path / "artifacts"
    plan = CampaignPlan.build(
        project_root=Path(__file__).parents[1],
        artifact_root=artifact_root,
    )
    plan.write(artifact_root / "campaign_plan.json")
    registry = ExperimentRegistry(artifact_root)
    registry.append(
        "resource_checked",
        {
            "name": "evaluator_log",
            "status": "ready",
            "detail": "/data3/private_evaluator/candidate/raw.log",
        },
        event_id="resource:private-log",
    )

    Dashboard(artifact_root / "dashboard.html").render(registry)

    page = (artifact_root / "dashboard.html").read_text(encoding="utf-8")
    assert "尚未获准执行" in page
    assert "尚缺全新 GPU 容器中的 P0 复现确认" in page
    assert "P1：固定 Harness 对照（6 条，其中两条为同预算通用流程）" in page
    assert "P2：专用 Harness 独立进化（6 条）" in page
    assert page.count("待运行 0/") == 12
    assert page.count("固定，不迭代") == 6
    assert "模型调用：0 次" in page
    assert "GPU 计时消耗：0 秒" in page
    assert str(artifact_root) not in page
    assert "private_evaluator" not in page
    assert "/data3/" not in page
    assert "raw.log" not in page


def test_dashboard_marks_p0_complete_after_clean_environment_confirmation(
    tmp_path: Path,
) -> None:
    artifact_root = tmp_path / "artifacts"
    registry = ExperimentRegistry(artifact_root)
    registry.append(
        "p0_clean_environment_confirmed",
        {"status": "ready", "detail": "clean container rerun passed"},
        event_id="p0-clean-confirmed:test",
    )
    plan = CampaignPlan.build(
        project_root=Path(__file__).parents[1],
        artifact_root=artifact_root,
        p0_clean_confirmed=True,
    )
    plan.write(artifact_root / "campaign_plan.json")

    Dashboard(artifact_root / "dashboard.html").render(registry)

    page = (artifact_root / "dashboard.html").read_text(encoding="utf-8")
    assert "当前阶段：P0 已通过，P1 待授权" in page
    assert "<td>P0</td><td>评分器与环境门禁</td><td>已完成</td>" in page
    assert (
        "<td>P1</td><td>固定 Harness 对照（含同预算组）</td><td>等待授权</td>"
        in page
    )


def test_prepare_campaign_only_accepts_clean_confirmation_from_the_ledger(
    tmp_path: Path,
) -> None:
    artifact_root = tmp_path / "artifacts"
    ExperimentRegistry(artifact_root).append(
        "p0_clean_environment_confirmed",
        {"status": "ready", "detail": "automated clean-environment rerun passed"},
        event_id="p0-clean-confirmed:test",
    )

    prepare_campaign(
        artifact_root=artifact_root,
        project_root=Path(__file__).parents[1],
        executor_model="fixed-model",
        model_call_cap_per_lane=8,
        gpu_seconds_cap_per_lane=3600.0,
        api_dollar_cap=100.0,
        gpu_dollar_cap=100.0,
    )

    plan = json.loads((artifact_root / "campaign_plan.json").read_text())
    assert plan["p0_clean_confirmed"] is True
    assert plan["execution_ready"] is True


def test_campaign_budget_enforces_separate_api_and_gpu_dollar_caps() -> None:
    budget = ExperimentBudget(
        max_gpu_seconds=100.0,
        max_model_calls=8,
        max_api_cost_usd=10.0,
        max_gpu_cost_usd=5.0,
    )
    budget.reserve(model_calls=1, api_cost_usd=9.0, gpu_cost_usd=4.0)

    with pytest.raises(BudgetExceeded, match="API cost"):
        budget.reserve(api_cost_usd=2.0)
    with pytest.raises(BudgetExceeded, match="GPU cost"):
        budget.reserve(gpu_cost_usd=2.0)

    assert budget.api_cost_usd_used == 9.0
    assert budget.gpu_cost_usd_used == 4.0


def test_lineage_preserves_best_candidate_and_stops_after_three_no_improvements() -> None:
    tracker = LineageTracker(task_id="kernelbench_layernorm", max_rounds=8)
    tracker.record(_feedback(candidate_id="c1", correct=True, speedup=1.20))
    tracker.record(_feedback(candidate_id="c2", correct=True, speedup=1.10))
    tracker.record(_feedback(candidate_id="c3", correct=False))
    tracker.record(_feedback(candidate_id="c4", correct=True, speedup=1.20))

    assert tracker.best_candidate_id == "c1"
    assert tracker.best_speedup == pytest.approx(1.20)
    assert tracker.should_stop is True
    assert tracker.stop_reason == "three_rounds_without_speed_improvement"


def test_lineage_stops_after_three_rounds_without_a_correct_candidate() -> None:
    tracker = LineageTracker(task_id="kernelbench_layernorm", max_rounds=8)
    for number in range(3):
        tracker.record(_feedback(candidate_id=f"bad-{number}", correct=False))

    assert tracker.valid_rounds == 3
    assert tracker.should_stop is True
    assert tracker.stop_reason == "three_rounds_without_correct_candidate"


def test_environment_failure_does_not_consume_a_lineage_round() -> None:
    tracker = LineageTracker(task_id="kernelbench_layernorm", max_rounds=8)
    tracker.record(
        _feedback(
            candidate_id="infra",
            correct=False,
            valid_run=False,
            outcome="environment_invalid",
        )
    )

    assert tracker.valid_rounds == 0
    assert tracker.should_stop is False
    assert tracker.invalid_environment_runs == 1


def test_lineage_rejects_feedback_from_another_task() -> None:
    tracker = LineageTracker(task_id="kernelbench_layernorm", max_rounds=8)
    card = _feedback(candidate_id="foreign", correct=True, speedup=1.5)
    card = FeedbackCard(**{**card.to_dict(), "task_id": "another_task"})

    with pytest.raises(ValueError, match="task"):
        tracker.record(card)


def test_lineage_tracker_round_trips_for_resume_without_losing_best() -> None:
    tracker = LineageTracker(task_id="kernelbench_layernorm", max_rounds=8)
    tracker.record(_feedback(candidate_id="best", correct=True, speedup=1.3))
    tracker.record(_feedback(candidate_id="worse", correct=True, speedup=1.1))

    restored = LineageTracker.from_dict(tracker.to_dict())
    restored.record(_feedback(candidate_id="new", correct=False))

    assert restored.valid_rounds == 3
    assert restored.best_candidate_id == "best"
    assert restored.best_speedup == pytest.approx(1.3)
    assert restored.should_stop is False

    with pytest.raises(ValueError, match="already exists"):
        restored.record(_feedback(candidate_id="worse", correct=True, speedup=2.0))
