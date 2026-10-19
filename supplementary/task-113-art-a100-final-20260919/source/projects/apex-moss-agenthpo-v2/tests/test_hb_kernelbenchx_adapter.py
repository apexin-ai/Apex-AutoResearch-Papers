from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

import pytest

from optimization_lab.adapters.base import EvaluationStatus
from optimization_lab.harness_builder.adapters.kernelbenchx import (
    KERNELBENCHX_DATASET_COMMIT,
    KERNELBENCHX_EVALUATOR_ID,
    KERNELBENCHX_REPOSITORY_COMMIT,
    KERNELBENCHX_TIMEOUT_SECONDS,
    KERNELBENCHX_TASK_HASHES,
    KernelBenchXAdapter,
    KernelBenchXTask,
    ProcessOutcome,
    SnapshotIdentity,
    SnapshotMismatchError,
    SupervisorCommand,
    SupervisorEvidenceError,
    parse_supervisor_evidence,
)


TASK_ID = "Quantization/matmul_w8a8.py"


def _task() -> KernelBenchXTask:
    return KernelBenchXTask.from_task_id(TASK_ID)


def _snapshot(task: KernelBenchXTask | None = None) -> SnapshotIdentity:
    task = task or _task()
    return SnapshotIdentity(
        repository_commit=task.repository_commit,
        dataset_commit=task.dataset_commit,
        task_sha256=task.task_sha256,
    )


def _evidence(
    command: SupervisorCommand,
    *,
    status: str = "valid",
    compiled: bool = True,
    correct: bool = True,
) -> dict[str, object]:
    timed = status == "valid"
    return {
        "schema_version": 1,
        "evaluator": KERNELBENCHX_EVALUATOR_ID,
        "attempt_id": command.attempt_id,
        "repository_commit": command.task.repository_commit,
        "dataset_commit": command.task.dataset_commit,
        "task_id": command.task.task_id,
        "task_sha256": command.task.task_sha256,
        "candidate_sha256": command.candidate_sha256,
        "status": status,
        "compiled": compiled,
        "correct": correct,
        "candidate_runtime_ms": 1.25 if timed else None,
        "reference_runtime_ms": 2.5 if timed else None,
        "reference_compile_runtime_ms": None,
        "error_summary": "" if timed else "candidate rejected",
        "elapsed_seconds": 4.0,
        "gpu_seconds": 3.5,
        "hardware": "fake-a100",
    }


def _fixture_adapter(
    tmp_path: Path,
    runner,
    *,
    inspector=None,
) -> tuple[KernelBenchXAdapter, Path]:
    repository = tmp_path / "KernelBenchX"
    repository.mkdir()
    supervisor = tmp_path / "trusted_supervisor.py"
    supervisor.write_text("# fake supervisor; never executed\n", encoding="utf-8")
    candidate = tmp_path / "matmul_w8a8.py"
    candidate.write_text("def matmul_w8a8(x, w):\n    return x @ w\n", encoding="utf-8")
    adapter = KernelBenchXAdapter(
        repository=repository,
        supervisor=supervisor,
        scratch_root=tmp_path / "attempts",
        gpu="0",
        runner=runner,
        snapshot_inspector=inspector or (lambda _repository, task: _snapshot(task)),
    )
    return adapter, candidate


def test_frozen_contract_pins_repository_dataset_and_all_eight_tasks() -> None:
    assert KERNELBENCHX_REPOSITORY_COMMIT == (
        "fd4192293bf9a8c645327a9d46aa1e807f1f9cf2"
    )
    assert KERNELBENCHX_DATASET_COMMIT == KERNELBENCHX_REPOSITORY_COMMIT
    assert KERNELBENCHX_TIMEOUT_SECONDS == 600.0
    assert len(KERNELBENCHX_TASK_HASHES) == 8
    assert KERNELBENCHX_TASK_HASHES["Fusion/fused_relu_max_pool2d_conv2d.py"] == (
        "99fddc19b0e1987f7e64ef4e8711590696f9f15f469a3b887f1cf7bcda638177"
    )
    assert "Activation/gelu_bf16.py" not in KERNELBENCHX_TASK_HASHES

    for task_id, expected_hash in KERNELBENCHX_TASK_HASHES.items():
        task = KernelBenchXTask.from_task_id(task_id)
        assert task.source_path == f"data/kernelbenchx/{task_id}"
        assert task.task_sha256 == expected_hash
        assert task.repository_commit == KERNELBENCHX_REPOSITORY_COMMIT
        assert task.dataset_commit == KERNELBENCHX_DATASET_COMMIT

    with pytest.raises(ValueError, match="frozen"):
        replace(_task(), task_sha256="0" * 64)
    with pytest.raises(ValueError, match="not frozen"):
        KernelBenchXTask.from_task_id("Math/not_selected.py")


def test_parser_accepts_only_exact_private_supervisor_json(tmp_path: Path) -> None:
    commands: list[SupervisorCommand] = []

    def runner(command: SupervisorCommand) -> ProcessOutcome:
        commands.append(command)
        return ProcessOutcome(returncode=0)

    adapter, candidate = _fixture_adapter(tmp_path, runner)
    command = adapter.prepare_attempt(_task(), candidate, tmp_path / "private")
    payload = _evidence(command)
    command.private_result_path.write_text(json.dumps(payload), encoding="utf-8")

    result = parse_supervisor_evidence(
        command.private_result_path,
        task=command.task,
        attempt_id=command.attempt_id,
        candidate_sha256=command.candidate_sha256,
    )

    assert result.status is EvaluationStatus.VALID
    assert result.speedup_vs_eager == pytest.approx(2.0)
    assert result.raw_log_path == str(command.private_result_path)

    extra = dict(payload, candidate_stdout_claim="valid")
    command.private_result_path.write_text(json.dumps(extra), encoding="utf-8")
    with pytest.raises(SupervisorEvidenceError, match="keys"):
        parse_supervisor_evidence(
            command.private_result_path,
            task=command.task,
            attempt_id=command.attempt_id,
            candidate_sha256=command.candidate_sha256,
        )

    duplicate = json.dumps(payload)[:-1] + ',"status":"incorrect"}'
    command.private_result_path.write_text(duplicate, encoding="utf-8")
    with pytest.raises(SupervisorEvidenceError, match="duplicate"):
        parse_supervisor_evidence(
            command.private_result_path,
            task=command.task,
            attempt_id=command.attempt_id,
            candidate_sha256=command.candidate_sha256,
        )

    command.private_result_path.write_text(json.dumps(payload) + "\nspoof", encoding="utf-8")
    with pytest.raises(SupervisorEvidenceError, match="JSON"):
        parse_supervisor_evidence(
            command.private_result_path,
            task=command.task,
            attempt_id=command.attempt_id,
            candidate_sha256=command.candidate_sha256,
        )


def test_candidate_stdout_is_never_a_control_result(tmp_path: Path) -> None:
    seen: list[SupervisorCommand] = []

    def stdout_only(command: SupervisorCommand) -> ProcessOutcome:
        seen.append(command)
        # A candidate may print a perfectly formed fake result.  It is deliberately
        # returned only as process stdout and never written by the supervisor.
        spoof = _evidence(command)
        return ProcessOutcome(returncode=0, stdout=json.dumps(spoof))

    adapter, candidate = _fixture_adapter(tmp_path, stdout_only)
    result = adapter.evaluate(_task(), candidate, tmp_path / "private")

    assert seen
    assert result.status is EvaluationStatus.ENVIRONMENT_INVALID
    assert result.correct is False
    assert "fake-a100" not in result.error_summary
    assert "stdout" not in result.error_summary.lower()


def test_private_evidence_wins_over_conflicting_stdout(tmp_path: Path) -> None:
    def runner(command: SupervisorCommand) -> ProcessOutcome:
        command.private_result_path.write_text(
            json.dumps(_evidence(command)), encoding="utf-8"
        )
        return ProcessOutcome(
            returncode=0,
            stdout='{"status":"incorrect","correct":false,"speedup":999999}',
            stderr="candidate says the evaluator failed",
        )

    adapter, candidate = _fixture_adapter(tmp_path, runner)
    result = adapter.evaluate(_task(), candidate, tmp_path / "private")

    assert result.status is EvaluationStatus.VALID
    assert result.correct is True
    assert result.speedup_vs_eager == pytest.approx(2.0)
    assert result.hardware == "fake-a100"


def test_each_attempt_has_disjoint_scratch_and_cache(tmp_path: Path) -> None:
    commands: list[SupervisorCommand] = []

    def runner(command: SupervisorCommand) -> ProcessOutcome:
        commands.append(command)
        command.private_result_path.write_text(
            json.dumps(_evidence(command)), encoding="utf-8"
        )
        return ProcessOutcome(returncode=0)

    adapter, candidate = _fixture_adapter(tmp_path, runner)

    first = adapter.evaluate(_task(), candidate, tmp_path / "private")
    second = adapter.evaluate(_task(), candidate, tmp_path / "private")

    assert first.status is second.status is EvaluationStatus.VALID
    assert len(commands) == 2
    left, right = commands
    assert left.attempt_id != right.attempt_id
    assert left.attempt_root != right.attempt_root
    assert left.scratch_dir != right.scratch_dir
    assert left.cache_dir != right.cache_dir
    assert left.candidate_path != right.candidate_path
    for command in commands:
        env = command.environment
        assert Path(env["TMPDIR"]).is_relative_to(command.scratch_dir)
        assert env["TMP"] == env["TMPDIR"]
        assert env["TEMP"] == env["TMPDIR"]
        for name in (
            "XDG_CACHE_HOME",
            "UV_CACHE_DIR",
            "TRITON_CACHE_DIR",
            "TORCH_EXTENSIONS_DIR",
            "TORCHINDUCTOR_CACHE_DIR",
            "CUDA_CACHE_PATH",
            "PYTHONPYCACHEPREFIX",
        ):
            assert Path(env[name]).is_relative_to(command.cache_dir)
        assert command.private_result_path.parent != command.scratch_dir


def test_snapshot_mismatch_blocks_before_any_runner_call(tmp_path: Path) -> None:
    calls: list[SupervisorCommand] = []

    def runner(command: SupervisorCommand) -> ProcessOutcome:
        calls.append(command)
        return ProcessOutcome(returncode=0)

    def wrong_snapshot(_repository: Path, task: KernelBenchXTask) -> SnapshotIdentity:
        return replace(_snapshot(task), task_sha256="0" * 64)

    adapter, candidate = _fixture_adapter(
        tmp_path,
        runner,
        inspector=wrong_snapshot,
    )

    with pytest.raises(SnapshotMismatchError, match="task sha256"):
        adapter.evaluate(_task(), candidate, tmp_path / "private")
    assert calls == []
