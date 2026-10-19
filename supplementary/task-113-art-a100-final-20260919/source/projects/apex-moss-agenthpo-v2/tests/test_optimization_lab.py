import json
import hashlib
import subprocess
from pathlib import Path

import pytest

from optimization_lab.adapters.base import EvaluationResult, EvaluationStatus
from optimization_lab.adapters.fake import FakeAdapter
from optimization_lab.adapters.kernelbench import KernelBenchAdapter
from optimization_lab.budget import BudgetExceeded, ExperimentBudget
from optimization_lab.dashboard import Dashboard
from optimization_lab.feedback import FeedbackCard
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.runner import ExperimentRunner
from optimization_lab.task_spec import TaskSpec


def _task() -> TaskSpec:
    return TaskSpec(
        task_id="kernelbench_layernorm",
        display_name="LayerNorm",
        level=1,
        problem_id=40,
        task_path="KernelBench/level1/40_LayerNorm.py",
        task_sha256="8d975d7cee6946513dcfb6ba84c971e53a890f9d9c6f0a4fb828904941f25975",
        repository_commit="423217d9fda91e0c2d67e4a43bf62f96f6d104f1",
        target_gpu="L40S",
        gpu_arch="Ada",
        backend="triton",
    )


def test_feedback_card_stops_after_compile_failure() -> None:
    result = EvaluationResult(
        status=EvaluationStatus.COMPILE_FAILED,
        compiled=False,
        correct=False,
        error_summary="syntax error near tl.load",
        elapsed_seconds=3.2,
    )

    card = FeedbackCard.from_result(_task(), "cand-1", result)

    assert card.stage_reached == "compile"
    assert card.speedup_vs_eager is None
    assert "syntax error" in card.next_action


def test_evaluation_result_rejects_speed_for_incorrect_candidate() -> None:
    with pytest.raises(ValueError, match="correct candidate"):
        EvaluationResult(
            status=EvaluationStatus.INCORRECT,
            compiled=True,
            correct=False,
            candidate_runtime_ms=1.0,
            reference_runtime_ms=2.0,
        )


def test_budget_fails_before_crossing_a_hard_cap() -> None:
    budget = ExperimentBudget(max_gpu_seconds=100.0, max_model_calls=4)
    budget.reserve(gpu_seconds=60.0, model_calls=2)

    with pytest.raises(BudgetExceeded):
        budget.reserve(gpu_seconds=41.0, model_calls=0)

    assert budget.gpu_seconds_used == 60.0
    assert budget.model_calls_used == 2


def test_registry_is_append_only_and_idempotent(tmp_path: Path) -> None:
    registry = ExperimentRegistry(tmp_path)
    first = registry.append(
        "resource_checked",
        {"name": "model_api", "status": "ready"},
        event_id="resource:model-api",
    )
    second = registry.append(
        "resource_checked",
        {"name": "model_api", "status": "ready"},
        event_id="resource:model-api",
    )

    assert first == second
    assert len(registry.read_events()) == 1
    assert json.loads(registry.ledger_path.read_text().splitlines()[0]) == first


def test_registry_rejects_an_event_id_content_rebind(tmp_path: Path) -> None:
    registry = ExperimentRegistry(tmp_path)
    registry.append(
        "resource_checked",
        {"name": "model_api", "status": "ready"},
        event_id="resource:model-api",
    )

    with pytest.raises(ValueError, match="different registry content"):
        registry.append(
            "resource_checked",
            {"name": "model_api", "status": "blocked"},
            event_id="resource:model-api",
        )
    assert len(registry.read_events()) == 1


def test_trusted_registry_hash_chain_and_head_detect_tampering(tmp_path: Path) -> None:
    registry = ExperimentRegistry(tmp_path, integrity_mode="hash_chain_v1")
    first = registry.append(
        "harness_compiled", {"round": 1}, event_id="compile:v001"
    )
    registry.append("round_sealed", {"round": 1}, event_id="seal:v001")

    assert first["schema_version"] == 2
    assert registry.head_path.is_file()
    assert len(ExperimentRegistry(tmp_path).read_events()) == 2

    lines = registry.ledger_path.read_text(encoding="utf-8").splitlines()
    tampered = json.loads(lines[0])
    tampered["payload"]["round"] = 2
    lines[0] = json.dumps(tampered, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    registry.ledger_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="hash/canonical"):
        registry.read_events()


def test_trusted_registry_refuses_legacy_adoption(tmp_path: Path) -> None:
    ExperimentRegistry(tmp_path).append(
        "legacy", {"round": 1}, event_id="legacy:v001"
    )

    with pytest.raises(ValueError, match="cannot adopt"):
        ExperimentRegistry(tmp_path, integrity_mode="hash_chain_v1").read_events()


def test_runner_records_valid_score_and_refreshes_dashboard(tmp_path: Path) -> None:
    registry = ExperimentRegistry(tmp_path)
    dashboard = Dashboard(tmp_path / "dashboard.html")
    adapter = FakeAdapter(
        EvaluationResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=1.0,
            reference_runtime_ms=2.5,
            elapsed_seconds=12.0,
            gpu_seconds=10.0,
            hardware="NVIDIA L40S",
        )
    )
    runner = ExperimentRunner(
        registry=registry,
        adapter=adapter,
        dashboard=dashboard,
        budget=ExperimentBudget(max_gpu_seconds=100.0, max_model_calls=5),
    )
    candidate = tmp_path / "candidate.py"
    candidate.write_text("class ModelNew: pass\n", encoding="utf-8")

    card = runner.evaluate(_task(), candidate, candidate_id="layernorm-r001")

    assert card.speedup_vs_eager == pytest.approx(2.5)
    events = registry.read_events()
    assert [event["event_type"] for event in events] == [
        "candidate_started",
        "candidate_evaluated",
    ]
    html = dashboard.path.read_text(encoding="utf-8")
    assert "layernorm-r001" in html
    assert "2.50×" in html
    assert 'http-equiv="refresh" content="5"' in html


def test_runner_does_not_rescore_an_existing_candidate_id(tmp_path: Path) -> None:
    registry = ExperimentRegistry(tmp_path)
    adapter = FakeAdapter(
        EvaluationResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=1.0,
            reference_runtime_ms=2.0,
            gpu_seconds=4.0,
        )
    )
    runner = ExperimentRunner(
        registry=registry,
        adapter=adapter,
        dashboard=Dashboard(tmp_path / "dashboard.html"),
        budget=ExperimentBudget(max_gpu_seconds=100.0, max_model_calls=5),
    )
    candidate = tmp_path / "candidate.py"
    candidate.write_text("class ModelNew: pass\n", encoding="utf-8")

    first = runner.evaluate(_task(), candidate, candidate_id="same-candidate")
    second = runner.evaluate(_task(), candidate, candidate_id="same-candidate")

    assert first == second
    assert len(adapter.calls) == 1
    assert runner.budget.gpu_seconds_used == 4.0

    candidate.write_text("class ModelNew: changed = True\n", encoding="utf-8")
    with pytest.raises(ValueError, match="different content"):
        runner.evaluate(_task(), candidate, candidate_id="same-candidate")


def test_runner_rejects_candidate_ids_that_escape_private_log_directory(
    tmp_path: Path,
) -> None:
    runner = ExperimentRunner(
        registry=ExperimentRegistry(tmp_path),
        adapter=FakeAdapter(
            EvaluationResult(
                status=EvaluationStatus.COMPILE_FAILED,
                compiled=False,
                correct=False,
            )
        ),
        dashboard=Dashboard(tmp_path / "dashboard.html"),
        budget=ExperimentBudget(max_gpu_seconds=100.0, max_model_calls=5),
    )
    candidate = tmp_path / "candidate.py"
    candidate.write_text("class ModelNew: pass\n", encoding="utf-8")

    with pytest.raises(ValueError, match="candidate id"):
        runner.evaluate(_task(), candidate, candidate_id="../../outside")


def test_runner_marks_environment_failure_invalid_not_candidate_failure(
    tmp_path: Path,
) -> None:
    registry = ExperimentRegistry(tmp_path)
    runner = ExperimentRunner(
        registry=registry,
        adapter=FakeAdapter(
            EvaluationResult(
                status=EvaluationStatus.ENVIRONMENT_INVALID,
                compiled=False,
                correct=False,
                error_summary="CUDA device unavailable",
            )
        ),
        dashboard=Dashboard(tmp_path / "dashboard.html"),
        budget=ExperimentBudget(max_gpu_seconds=100.0, max_model_calls=5),
    )
    candidate = tmp_path / "candidate.py"
    candidate.write_text("class ModelNew: pass\n", encoding="utf-8")

    card = runner.evaluate(_task(), candidate, candidate_id="infra-check")

    assert card.valid_run is False
    assert card.outcome == "environment_invalid"
    assert "环境" in card.next_action


def test_task_specs_are_frozen_and_loadable() -> None:
    root = Path(__file__).parents[1]
    layernorm = TaskSpec.from_json(
        root / "optimization_lab/protocols/kernelbench_layernorm.json"
    )
    fusion = TaskSpec.from_json(
        root / "optimization_lab/protocols/kernelbench_matmul_fusion.json"
    )
    replacement = TaskSpec.from_json(
        root / "optimization_lab/protocols/kernelbench_matmul_sigmoid_sum.json"
    )

    assert layernorm.repository_commit == fusion.repository_commit == replacement.repository_commit
    assert layernorm.problem_id == 40
    assert fusion.problem_id == 9
    assert replacement.problem_id == 56
    assert len({layernorm.task_sha256, fusion.task_sha256, replacement.task_sha256}) == 3


def test_kernelbench_parser_accepts_correct_timed_candidate(tmp_path: Path) -> None:
    adapter = KernelBenchAdapter(
        repository=tmp_path,
        mode="modal",
        uv_executable="uv",
    )
    output = """
[Eval] Kernel eval result: compiled=True correctness=True metadata={'hardware': 'NVIDIA L40S'} runtime=1.25
[Timing] PyTorch Reference Eager exec time: 3.0 ms
[Timing] PyTorch Reference torch.compile time: 1.8 ms
[Timing] Custom Kernel exec time: 1.25 ms
[Speedup] Speedup over eager: 2.40x
"""

    result = adapter.parse_result(
        output,
        returncode=0,
        elapsed_seconds=8.0,
        raw_log_path=tmp_path / "raw.log",
        task=_task(),
    )

    assert result.status is EvaluationStatus.VALID
    assert result.speedup_vs_eager == pytest.approx(2.4)
    assert result.hardware == "NVIDIA L40S"


def test_kernelbench_parser_separates_environment_and_candidate_failures(
    tmp_path: Path,
) -> None:
    adapter = KernelBenchAdapter(repository=tmp_path, mode="modal")

    environment = adapter.parse_result(
        "RuntimeError: GPU not attached to container",
        returncode=1,
        elapsed_seconds=2.0,
        raw_log_path=tmp_path / "environment.log",
        task=_task(),
    )
    compile_failure = adapter.parse_result(
        "[Eval] Kernel eval result: compiled=False correctness=False metadata={'other_error': 'syntax error'} runtime=-1.0",
        returncode=0,
        elapsed_seconds=2.0,
        raw_log_path=tmp_path / "compile.log",
        task=_task(),
    )
    policy_rejection = adapter.parse_result(
        "AssertionError: Static check failed. Errors: "
        "['Missing @triton.jit or @triton.autotune']. Warnings: []",
        returncode=1,
        elapsed_seconds=2.0,
        raw_log_path=tmp_path / "policy.log",
        task=_task(),
    )

    assert environment.status is EvaluationStatus.ENVIRONMENT_INVALID
    assert compile_failure.status is EvaluationStatus.COMPILE_FAILED
    assert policy_rejection.status is EvaluationStatus.POLICY_REJECTED


def test_kernelbench_preflight_checks_commit_and_task_hash(tmp_path: Path) -> None:
    repo = tmp_path / "KernelBench"
    task_path = repo / "KernelBench/level1/40_LayerNorm.py"
    task_path.parent.mkdir(parents=True)
    content = "# frozen task\n"
    task_path.write_text(content, encoding="utf-8")
    evaluator = repo / "scripts/run_and_check.py"
    evaluator.parent.mkdir(parents=True)
    evaluator.write_text("# evaluator fixture\n", encoding="utf-8")
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(repo),
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.com",
            "commit",
            "-qm",
            "fixture",
        ],
        check=True,
    )
    commit = subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()
    task = TaskSpec(
        **{
            **_task().to_dict(),
            "repository_commit": commit,
            "task_sha256": hashlib.sha256(content.encode()).hexdigest(),
        }
    )
    adapter = KernelBenchAdapter(
        repository=repo,
        mode="local",
        uv_executable="uv",
    )

    checks = adapter.preflight(task, check_executor=False)

    assert all(check.status == "ready" for check in checks)
    assert {check.name for check in checks} >= {"repository_commit", "task_hash", "uv"}


def test_dashboard_does_not_present_retired_task_score_as_a_best(tmp_path: Path) -> None:
    registry = ExperimentRegistry(tmp_path)
    registry.append(
        "candidate_evaluated",
        {
            "feedback": {
                "task_id": "bad_task",
                "candidate_id": "zero-output",
                "outcome": "valid",
                "valid_run": True,
                "correct": True,
                "speedup_vs_eager": 215.0,
            }
        },
        event_id="bad-score",
    )
    registry.append(
        "task_retired",
        {"task_id": "bad_task", "detail": "zero-output negative control passed"},
        event_id="retire-bad-task",
    )
    dashboard = Dashboard(tmp_path / "dashboard.html")

    dashboard.render(registry)

    page = dashboard.path.read_text(encoding="utf-8")
    assert "已淘汰，不计分" in page
    assert "215.00×" not in page
