from __future__ import annotations

import hashlib
import json
import sys
import textwrap
from dataclasses import replace
from pathlib import Path

import pytest

from optimization_lab.adapters.base import EvaluationStatus
from optimization_lab.harness_builder.adapters.kernelbench_meta import (
    KERNELBENCH_META_EVALUATOR_ID,
    KERNELBENCH_META_PROTOCOL_SHA256,
    KERNELBENCH_META_REPOSITORY_COMMIT,
    KERNELBENCH_META_TASK_HASHES,
    KernelBenchMetaAdapter,
    KernelBenchMetaTask,
    MetaProcessOutcome,
    MetaSnapshotIdentity,
    MetaSupervisorCommand,
    MetaSupervisorEvidenceError,
    parse_meta_supervisor_evidence,
)
from optimization_lab.harness_builder.evaluation import (
    KernelBenchMetaEvaluationBackend,
)
from optimization_lab.harness_builder.meta_train import (
    MetaTrainContract,
    bind_kernelbench_meta_tasks,
)
from optimization_lab.harness_builder.adapters import kernelbench_meta as meta_module


TASK_ID = "level1/21_Sigmoid.py"
ROOT = Path(__file__).resolve().parents[1]
SAFE_CANDIDATE = """import torch
import torch.nn as nn

class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid(x)
"""


def _authorization_receipt(
    root: Path, *, authorization_type: str = "test-receipt"
) -> Path:
    raw = json.dumps(
        {"authorization_type": authorization_type},
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    path = root / "authorization" / f"{hashlib.sha256(raw).hexdigest()}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    path.chmod(0o600)
    return path


def _task() -> KernelBenchMetaTask:
    return KernelBenchMetaTask.from_task_id(TASK_ID)


def _snapshot(task: KernelBenchMetaTask | None = None) -> MetaSnapshotIdentity:
    task = task or _task()
    return MetaSnapshotIdentity(
        repository_commit=task.repository_commit,
        task_sha256=task.task_sha256,
    )


def _payload(
    command: MetaSupervisorCommand,
    *,
    status: str = "valid",
    compiled: bool = True,
    correct: bool = True,
) -> dict[str, object]:
    valid = status == "valid"
    return {
        "schema_version": 1,
        "evaluator": KERNELBENCH_META_EVALUATOR_ID,
        "protocol_sha256": KERNELBENCH_META_PROTOCOL_SHA256,
        "scorer_sha256": command.scorer_sha256,
        "attempt_id": command.attempt_id,
        "result_nonce": command.result_nonce,
        "repository_commit": command.task.repository_commit,
        "task_id": command.task.task_id,
        "task_sha256": command.task.task_sha256,
        "candidate_sha256": command.candidate_sha256,
        "candidate_policy_sha256": command.candidate_policy_sha256,
        "schedule_sha256": meta_module.KERNEL_INVOCATION_SCHEDULE_SHA256,
        "input_schedule_sha256": "7" * 64,
        "status": status,
        "health_probe": "passed",
        "compiled": compiled,
        "correct": correct,
        "correctness_trials": 5,
        "correctness_passed": 5 if valid else 2,
        "timing_trials": 100,
        "timing_trials_completed": 100 if valid else 0,
        "timing_outputs_correct": 100 if valid else 0,
        "candidate_runtime_ms": 1.0 if valid else None,
        "reference_runtime_ms": 2.0 if valid else None,
        "error_summary": "" if valid else "candidate output differs",
        "elapsed_seconds": 3.0,
        "gpu_seconds": 2.5,
        "hardware": "fake-a100",
    }


def _adapter(tmp_path: Path, runner, *, authorization_receipt: Path | None = None):
    repository = tmp_path / "KernelBench"
    repository.mkdir(parents=True, exist_ok=True)
    supervisor = tmp_path / "trusted-meta-supervisor.py"
    supervisor.write_text("# frozen fake supervisor\n", encoding="utf-8")
    scorer_sha = hashlib.sha256(supervisor.read_bytes()).hexdigest()
    candidate = tmp_path / "candidate.py"
    candidate.write_text(SAFE_CANDIDATE, encoding="utf-8")
    adapter = KernelBenchMetaAdapter(
        repository=repository,
        supervisor=supervisor,
        scorer_sha256=scorer_sha,
        scratch_root=tmp_path / "attempts",
        authorization_receipt=(
            authorization_receipt or _authorization_receipt(tmp_path)
        ),
        gpu="4",
        runner=runner,
        snapshot_inspector=lambda _repository, task: _snapshot(task),
        attempt_id_factory=iter(("attempt-a", "attempt-b", "attempt-c")).__next__,
        nonce_factory=iter(("1" * 64, "2" * 64, "3" * 64)).__next__,
    )
    return adapter, candidate


def test_contract_pins_the_six_new_meta_train_tasks() -> None:
    assert KERNELBENCH_META_REPOSITORY_COMMIT == (
        "423217d9fda91e0c2d67e4a43bf62f96f6d104f1"
    )
    assert tuple(KERNELBENCH_META_TASK_HASHES) == (
        "level1/21_Sigmoid.py",
        "level1/92_cumsum_exclusive.py",
        "level1/97_ScaledDotProductAttention.py",
        "level2/45_Gemm_Sigmoid_LogSumExp.py",
        "level2/57_Conv2d_ReLU_HardSwish.py",
        "level2/67_Conv2d_GELU_GlobalAvgPool.py",
    )
    for task_id, task_sha in KERNELBENCH_META_TASK_HASHES.items():
        task = KernelBenchMetaTask.from_task_id(task_id)
        assert task.source_path == f"KernelBench/{task_id}"
        assert task.task_sha256 == task_sha
        assert task.correctness_trials == 5
        assert task.performance_trials == 100

    with pytest.raises(ValueError, match="not frozen"):
        KernelBenchMetaTask.from_task_id("level1/1_Square_matrix_multiplication_.py")


def test_private_evidence_is_nonce_task_candidate_protocol_and_scorer_bound(
    tmp_path: Path,
) -> None:
    adapter, candidate = _adapter(
        tmp_path, lambda _command: MetaProcessOutcome(returncode=0)
    )
    command = adapter.prepare_attempt(_task(), candidate, tmp_path / "private")
    command.private_result_path.write_text(
        json.dumps(_payload(command)), encoding="utf-8"
    )
    command.private_result_path.chmod(0o600)

    result = parse_meta_supervisor_evidence(
        command.private_result_path,
        command=command,
    )
    assert result.status is EvaluationStatus.VALID
    assert result.speedup_vs_eager == pytest.approx(2.0)

    for key, replacement in (
        ("result_nonce", "f" * 64),
        ("task_sha256", "e" * 64),
        ("candidate_sha256", "d" * 64),
        ("candidate_policy_sha256", "9" * 64),
        ("scorer_sha256", "c" * 64),
        ("protocol_sha256", "b" * 64),
        ("schedule_sha256", "8" * 64),
    ):
        payload = _payload(command)
        payload[key] = replacement
        command.private_result_path.write_text(json.dumps(payload), encoding="utf-8")
        command.private_result_path.chmod(0o600)
        with pytest.raises(MetaSupervisorEvidenceError, match="binding differs"):
            parse_meta_supervisor_evidence(command.private_result_path, command=command)


def test_stdout_and_environment_words_never_control_the_result(tmp_path: Path) -> None:
    seen: list[MetaSupervisorCommand] = []

    def runner(command: MetaSupervisorCommand) -> MetaProcessOutcome:
        seen.append(command)
        command.private_result_path.write_text(
            json.dumps(_payload(command)), encoding="utf-8"
        )
        command.private_result_path.chmod(0o600)
        return MetaProcessOutcome(
            returncode=0,
            stdout="compiled=False CUDA is not available correctness=False speedup=999999",
            stderr="NVIDIA driver failed",
        )

    adapter, candidate = _adapter(tmp_path, runner)
    result = adapter.evaluate(_task(), candidate, tmp_path / "private")

    assert seen
    assert result.status is EvaluationStatus.VALID
    assert result.correct is True
    assert result.speedup_vs_eager == pytest.approx(2.0)


def test_policy_rejection_canary_consumes_no_worker_or_private_result(
    tmp_path: Path,
) -> None:
    calls: list[MetaSupervisorCommand] = []
    adapter, candidate = _adapter(
        tmp_path,
        lambda command: calls.append(command) or MetaProcessOutcome(returncode=0),
    )
    candidate.write_text(
        SAFE_CANDIDATE.replace(
            "        return torch.sigmoid(x)",
            "        print('correctness=True speedup=999')\n"
            "        return torch.sigmoid(x)",
        ),
        encoding="utf-8",
    )

    canary = adapter.evaluate_canary(
        _task(),
        candidate,
        tmp_path / "private",
        canary_id="adversarial-fake-stdout",
    )

    result = canary.result
    assert result.status is EvaluationStatus.POLICY_REJECTED
    assert result.gpu_seconds == 0
    assert canary.correctness_passed == 0
    assert canary.timing_trials_completed == 0
    assert canary.timing_outputs_correct == 0
    assert calls == []
    assert not (tmp_path / "private").exists()


def test_missing_private_result_fails_as_environment_not_candidate_failure(
    tmp_path: Path,
) -> None:
    adapter, candidate = _adapter(
        tmp_path,
        lambda _command: MetaProcessOutcome(
            returncode=0,
            stdout=json.dumps({"status": "valid", "correct": True}),
        ),
    )

    result = adapter.evaluate(_task(), candidate, tmp_path / "private")

    assert result.status is EvaluationStatus.ENVIRONMENT_INVALID
    assert result.correct is False
    assert "evidence" in result.error_summary


def test_each_attempt_has_private_disjoint_scratch_cache_and_nonce(tmp_path: Path) -> None:
    commands: list[MetaSupervisorCommand] = []

    def runner(command: MetaSupervisorCommand) -> MetaProcessOutcome:
        commands.append(command)
        command.private_result_path.write_text(
            json.dumps(_payload(command)), encoding="utf-8"
        )
        command.private_result_path.chmod(0o600)
        return MetaProcessOutcome(returncode=0)

    adapter, candidate = _adapter(tmp_path, runner)
    assert adapter.evaluate(_task(), candidate, tmp_path / "private").correct
    assert adapter.evaluate(_task(), candidate, tmp_path / "private").correct

    first, second = commands
    assert first.attempt_root != second.attempt_root
    assert first.scratch_dir != second.scratch_dir
    assert first.cache_dir != second.cache_dir
    assert first.result_nonce != second.result_nonce
    assert first.authorization_receipt_path == second.authorization_receipt_path
    assert first.authorization_receipt_sha256 == second.authorization_receipt_sha256
    assert first.authorization_receipt_path.name == (
        f"{first.authorization_receipt_sha256}.json"
    )
    receipt_flag = first.argv.index("--authorization-receipt")
    assert first.argv[receipt_flag + 1] == str(first.authorization_receipt_path)
    assert first.private_result_path.parent not in first.attempt_root.parents
    serialized = "\0".join(first.worker_visible_argv)
    assert first.result_nonce not in serialized
    assert str(first.private_result_path) not in serialized
    assert str(first.authorization_receipt_path) not in serialized
    assert first.authorization_receipt_sha256 not in serialized
    environment = first.environment
    assert environment["CUDA_VISIBLE_DEVICES"] == "4"
    assert "LD_LIBRARY_PATH" not in environment
    assert all("TOKEN" not in name and "KEY" not in name for name in environment)
    for name in (
        "XDG_CACHE_HOME",
        "UV_CACHE_DIR",
        "TRITON_CACHE_DIR",
        "TORCH_EXTENSIONS_DIR",
        "TORCHINDUCTOR_CACHE_DIR",
        "CUDA_CACHE_PATH",
        "PYTHONPYCACHEPREFIX",
    ):
        assert Path(environment[name]).is_relative_to(first.cache_dir)


@pytest.mark.parametrize(
    ("canary_id", "authorization_type"),
    (
        ("adversarial-fake-stdout", "hb-gen1-kernelbench-meta-canary-v1"),
        ("formal", "hb-gen1-kernelbench-meta-formal-v1"),
    ),
)
def test_canary_and_formal_commands_consume_bound_receipt_without_candidate_visibility(
    tmp_path: Path, canary_id: str, authorization_type: str
) -> None:
    receipt = _authorization_receipt(
        tmp_path, authorization_type=authorization_type
    )
    adapter, candidate = _adapter(
        tmp_path,
        lambda _command: MetaProcessOutcome(returncode=0),
        authorization_receipt=receipt,
    )

    command = adapter.prepare_attempt(
        _task(), candidate, tmp_path / "private", canary_id=canary_id
    )

    receipt_flag = command.argv.index("--authorization-receipt")
    assert command.argv[receipt_flag + 1] == str(receipt.resolve())
    assert command.authorization_receipt_sha256 == receipt.stem
    assert str(receipt.resolve()) not in "\0".join(command.worker_visible_argv)
    assert str(receipt.resolve()) not in "\0".join(command.environment.values())


def test_adapter_fails_closed_for_missing_unsealed_or_worker_visible_receipt(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "KernelBench"
    repository.mkdir()
    supervisor = tmp_path / "trusted-meta-supervisor.py"
    supervisor.write_text("# fixed\n", encoding="utf-8")
    common = {
        "repository": repository,
        "supervisor": supervisor,
        "scorer_sha256": hashlib.sha256(supervisor.read_bytes()).hexdigest(),
        "gpu": "4",
    }

    with pytest.raises(ValueError, match="authorization receipt"):
        KernelBenchMetaAdapter(
            **common,
            scratch_root=tmp_path / "attempts-missing",
            authorization_receipt=tmp_path / "missing.json",
        )

    unsealed = tmp_path / "authorization" / "not-content-addressed.json"
    unsealed.parent.mkdir()
    unsealed.write_text("{}", encoding="utf-8")
    unsealed.chmod(0o600)
    with pytest.raises(ValueError, match="content addressed"):
        KernelBenchMetaAdapter(
            **common,
            scratch_root=tmp_path / "attempts-unsealed",
            authorization_receipt=unsealed,
        )

    repository_receipt = _authorization_receipt(repository)
    with pytest.raises(ValueError, match="worker-visible"):
        KernelBenchMetaAdapter(
            **common,
            scratch_root=tmp_path / "attempts-repository",
            authorization_receipt=repository_receipt,
        )

    scratch_root = tmp_path / "attempts-receipt"
    scratch_receipt = _authorization_receipt(scratch_root)
    with pytest.raises(ValueError, match="worker-visible"):
        KernelBenchMetaAdapter(
            **common,
            scratch_root=scratch_root,
            authorization_receipt=scratch_receipt,
        )

    drift_root = tmp_path / "drift"
    receipt = _authorization_receipt(drift_root)
    adapter, candidate = _adapter(
        drift_root,
        lambda _command: MetaProcessOutcome(returncode=0),
        authorization_receipt=receipt,
    )
    receipt.write_text('{"authorization_type":"changed"}', encoding="utf-8")
    receipt.chmod(0o600)
    with pytest.raises(ValueError, match="content addressed"):
        adapter.prepare_attempt(
            _task(), candidate, drift_root / "private", canary_id="formal"
        )


def test_protocol_requires_five_correctness_and_one_hundred_bound_timings(
    tmp_path: Path,
) -> None:
    adapter, candidate = _adapter(
        tmp_path, lambda _command: MetaProcessOutcome(returncode=0)
    )
    command = adapter.prepare_attempt(_task(), candidate, tmp_path / "private")
    for key, value in (
        ("correctness_passed", 4),
        ("timing_trials_completed", 99),
        ("timing_outputs_correct", 99),
    ):
        payload = _payload(command)
        payload[key] = value
        command.private_result_path.write_text(json.dumps(payload), encoding="utf-8")
        command.private_result_path.chmod(0o600)
        with pytest.raises(MetaSupervisorEvidenceError, match="protocol counts"):
            parse_meta_supervisor_evidence(command.private_result_path, command=command)

    payload = _payload(command)
    payload["input_schedule_sha256"] = None
    command.private_result_path.write_text(json.dumps(payload), encoding="utf-8")
    command.private_result_path.chmod(0o600)
    with pytest.raises(MetaSupervisorEvidenceError, match="protocol counts"):
        parse_meta_supervisor_evidence(command.private_result_path, command=command)


def test_candidate_failure_and_environment_health_are_not_interchangeable(
    tmp_path: Path,
) -> None:
    adapter, candidate = _adapter(
        tmp_path, lambda _command: MetaProcessOutcome(returncode=0)
    )
    command = adapter.prepare_attempt(_task(), candidate, tmp_path / "private")

    environment = _payload(
        command, status="environment_invalid", compiled=False, correct=False
    )
    environment["correctness_passed"] = 0
    command.private_result_path.write_text(json.dumps(environment), encoding="utf-8")
    command.private_result_path.chmod(0o600)
    with pytest.raises(MetaSupervisorEvidenceError, match="health evidence"):
        parse_meta_supervisor_evidence(command.private_result_path, command=command)

    candidate_failure = _payload(
        command, status="incorrect", compiled=True, correct=False
    )
    candidate_failure["health_probe"] = "failed"
    command.private_result_path.write_text(
        json.dumps(candidate_failure), encoding="utf-8"
    )
    command.private_result_path.chmod(0o600)
    with pytest.raises(MetaSupervisorEvidenceError, match="candidate failure"):
        parse_meta_supervisor_evidence(command.private_result_path, command=command)


def test_meta_train_backend_normalizes_only_private_evidence(tmp_path: Path) -> None:
    def runner(command: MetaSupervisorCommand) -> MetaProcessOutcome:
        command.private_result_path.write_text(
            json.dumps(_payload(command)), encoding="utf-8"
        )
        command.private_result_path.chmod(0o600)
        return MetaProcessOutcome(returncode=0)

    adapter, candidate = _adapter(tmp_path, runner)
    backend = KernelBenchMetaEvaluationBackend(adapter=adapter, task=_task())
    result = backend.evaluate(candidate, tmp_path / "private")

    assert result.status == "valid"
    assert result.correct is True
    assert result.score == pytest.approx(2.0)
    assert result.actual_usage.evaluator_transactions == 1
    assert result.actual_usage.gpu_exclusive_seconds == pytest.approx(2.5)


def test_six_meta_train_tasks_bind_the_strict_backend(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    contract = MetaTrainContract.from_json(
        ROOT / "optimization_lab/harness_builder/data/experience_bank_v1.json"
    )
    repository = tmp_path / "KernelBench"
    fake_hashes: dict[str, str] = {}
    sources = []
    for source in contract.sources:
        if source in contract.historical_sources:
            sources.append(source)
            continue
        content = f"# frozen fixture for {source.task_id}\n"
        path = repository / source.source_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        source_sha = hashlib.sha256(content.encode("utf-8")).hexdigest()
        fake_hashes[source.task_id] = source_sha
        sources.append(replace(source, source_sha256=source_sha))
    fixture_contract = replace(contract, sources=tuple(sources))
    monkeypatch.setattr(meta_module, "KERNELBENCH_META_TASK_HASHES", fake_hashes)
    adapter, _candidate = _adapter(
        tmp_path, lambda _command: MetaProcessOutcome(returncode=0)
    )

    tasks = bind_kernelbench_meta_tasks(
        contract=fixture_contract,
        repository=repository,
        adapter=adapter,
    )

    assert len(tasks) == 6
    assert tuple(task.source.task_id for task in tasks) == tuple(fake_hashes)
    assert all(
        isinstance(task.evaluator, KernelBenchMetaEvaluationBackend) for task in tasks
    )
    assert all(task.evaluator.adapter is adapter for task in tasks)


def test_fake_supervisor_subprocess_e2e_uses_only_the_private_channel(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "KernelBench"
    repository.mkdir()
    supervisor = tmp_path / "fake-supervisor.py"
    supervisor.write_text(
        textwrap.dedent(
            f"""
            import argparse, json, os
            parser = argparse.ArgumentParser()
            for name in (
                "repository", "repository-commit", "task-id", "task-path",
                "task-sha256", "candidate", "candidate-sha256", "scratch-dir",
                "candidate-policy-sha256", "invocation-schedule-sha256",
                "cache-dir", "private-result", "attempt-id", "result-nonce",
                "canary-id", "gpu", "evaluator", "protocol-sha256", "scorer-sha256",
                "authorization-receipt",
            ):
                parser.add_argument("--" + name, required=True)
            args = parser.parse_args()
            payload = {{
                "schema_version": 1,
                "evaluator": args.evaluator,
                "protocol_sha256": args.protocol_sha256,
                "scorer_sha256": args.scorer_sha256,
                "attempt_id": args.attempt_id,
                "result_nonce": args.result_nonce,
                "repository_commit": args.repository_commit,
                "task_id": args.task_id,
                "task_sha256": args.task_sha256,
                "candidate_sha256": args.candidate_sha256,
                "candidate_policy_sha256": args.candidate_policy_sha256,
                "schedule_sha256": args.invocation_schedule_sha256,
                "input_schedule_sha256": "7" * 64,
                "status": "valid",
                "health_probe": "passed",
                "compiled": True,
                "correct": True,
                "correctness_trials": 5,
                "correctness_passed": 5,
                "timing_trials": 100,
                "timing_trials_completed": 100,
                "timing_outputs_correct": 100,
                "candidate_runtime_ms": 1.0,
                "reference_runtime_ms": 2.0,
                "error_summary": "",
                "elapsed_seconds": 3.0,
                "gpu_seconds": 2.5,
                "hardware": "fake-a100",
            }}
            result = args.private_result
            descriptor = os.open(result, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                json.dump(payload, stream, sort_keys=True)
            print("CUDA is not available correctness=False speedup=999999")
            """
        ).lstrip(),
        encoding="utf-8",
    )
    scorer_sha = hashlib.sha256(supervisor.read_bytes()).hexdigest()
    candidate = tmp_path / "candidate.py"
    candidate.write_text(SAFE_CANDIDATE, encoding="utf-8")
    adapter = KernelBenchMetaAdapter(
        repository=repository,
        supervisor=supervisor,
        scorer_sha256=scorer_sha,
        scratch_root=tmp_path / "attempts",
        authorization_receipt=_authorization_receipt(tmp_path),
        gpu="4",
        python_executable=sys.executable,
        snapshot_inspector=lambda _repository, task: _snapshot(task),
        attempt_id_factory=lambda: "fake-e2e",
        nonce_factory=lambda: "a" * 64,
    )

    result = adapter.evaluate(_task(), candidate, tmp_path / "private")

    assert result.status is EvaluationStatus.VALID
    assert result.correct is True
    assert result.speedup_vs_eager == pytest.approx(2.0)
