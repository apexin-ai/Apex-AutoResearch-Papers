from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path

import pytest

from optimization_lab.harness_builder.adapters.kernelbenchx import (
    KERNELBENCHX_EVALUATOR_ID as ADAPTER_EVALUATOR_ID,
    KERNELBENCHX_REPOSITORY_COMMIT as ADAPTER_REPOSITORY_COMMIT,
    KERNELBENCHX_TASK_HASHES as ADAPTER_TASK_HASHES,
)
from optimization_lab.harness_builder.adapters.kernelbenchx_isolation import (
    BubblewrapCommand,
    IsolatedProcessOutcome,
    SandboxContractError,
    StagedWorkerInputs,
    hash_immutable_tree,
)
from scripts.hb_gen1_kernelbenchx_supervisor import (
    KERNELBENCHX_EVALUATOR_ID,
    KERNELBENCHX_REPOSITORY_COMMIT,
    KERNELBENCHX_TASK_HASHES,
    OfficialPipelineOutcome,
    SupervisorRequest,
    build_official_command,
    run_supervisor,
)


TASK_ID = "Quantization/matmul_w8a8.py"


def test_supervisor_contract_matches_outer_adapter_exactly() -> None:
    assert KERNELBENCHX_EVALUATOR_ID == ADAPTER_EVALUATOR_ID
    assert KERNELBENCHX_REPOSITORY_COMMIT == ADAPTER_REPOSITORY_COMMIT
    assert dict(KERNELBENCHX_TASK_HASHES) == dict(ADAPTER_TASK_HASHES)


def _repository(tmp_path: Path) -> Path:
    repository = tmp_path / "KernelBenchX"
    task_path = repository / "data/kernelbenchx" / TASK_ID
    task_path.parent.mkdir(parents=True)
    task_path.write_bytes(b"frozen task")
    (repository / "scripts").mkdir()
    (repository / "scripts/run_eval_from_files.sh").write_text(
        "#!/bin/sh\nexit 0\n", encoding="utf-8"
    )
    golden = repository / "metrics/golden_results/a100/matmul_w8a8.json"
    golden.parent.mkdir(parents=True)
    golden.write_text(
        json.dumps([{"ms": 1.25}, {"ms": 2.75}]), encoding="utf-8"
    )
    return repository


def _request(tmp_path: Path) -> SupervisorRequest:
    repository = _repository(tmp_path)
    attempt = tmp_path / "attempt"
    scratch = attempt / "scratch"
    cache = attempt / "cache"
    scratch.mkdir(parents=True)
    cache.mkdir()
    candidate = scratch / "candidate/matmul_w8a8.py"
    candidate.parent.mkdir()
    candidate.write_text(
        "def matmul_w8a8(input, weight):\n    return input @ weight\n",
        encoding="utf-8",
    )
    private_result = tmp_path / "private/supervisor-result.json"
    private_result.parent.mkdir()
    return SupervisorRequest(
        repository=repository,
        repository_commit=KERNELBENCHX_REPOSITORY_COMMIT,
        dataset_commit=KERNELBENCHX_REPOSITORY_COMMIT,
        task_id=TASK_ID,
        task_path=f"data/kernelbenchx/{TASK_ID}",
        task_sha256=KERNELBENCHX_TASK_HASHES[TASK_ID],
        candidate=candidate,
        candidate_sha256=hashlib.sha256(candidate.read_bytes()).hexdigest(),
        scratch_dir=scratch,
        cache_dir=cache,
        private_result=private_result,
        attempt_id="attempt-001",
        canary_id="formal",
        gpu="4",
        evaluator=KERNELBENCHX_EVALUATOR_ID,
    )


def _metrics(*, call_ok: bool = True, exe_ok: bool = True, perf_ok: bool = True):
    return {
        TASK_ID: {
            "file": TASK_ID,
            "call_ok": call_ok,
            "exe_ok": exe_ok,
            "perf_ok": perf_ok,
            "runtime_ms": 2.0 if perf_ok else "N/A",
            "speedup": 999999.0 if perf_ok else "N/A",
            "performance": ([{"ms": 0.75}, {"ms": 1.25}] if perf_ok else []),
            "error": "" if perf_ok else "candidate rejected",
            "code": "untrusted and ignored",
        }
    }


def _snapshot(request: SupervisorRequest) -> None:
    assert request.repository_commit == KERNELBENCHX_REPOSITORY_COMMIT
    assert request.task_sha256 == KERNELBENCHX_TASK_HASHES[TASK_ID]
    assert (request.repository / request.task_path).read_bytes() == b"frozen task"


def _execute_with(metrics):
    def execute(request: SupervisorRequest, output_dir: Path) -> OfficialPipelineOutcome:
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "metrics.json").write_text(
            json.dumps(metrics), encoding="utf-8"
        )
        return OfficialPipelineOutcome(
            returncode=0,
            elapsed_seconds=3.25,
            hardware="NVIDIA A100-SXM4-80GB",
            metrics_path=output_dir / "metrics.json",
            error_summary="candidate printed correctness=True speedup=999999",
        )

    return execute


def test_valid_result_is_recomputed_from_bound_perf_rows_and_golden_reference(
    tmp_path: Path,
) -> None:
    request = _request(tmp_path)
    result = run_supervisor(
        request,
        snapshot_verifier=_snapshot,
        pipeline_executor=_execute_with(_metrics()),
    )

    assert result["status"] == "valid"
    assert result["compiled"] is True
    assert result["correct"] is True
    assert result["candidate_runtime_ms"] == pytest.approx(2.0)
    assert result["reference_runtime_ms"] == pytest.approx(4.0)
    # The official summary's self-reported 999999x is not trusted.
    assert result["reference_runtime_ms"] / result["candidate_runtime_ms"] == 2.0
    assert result["candidate_sha256"] == request.candidate_sha256
    assert result["task_sha256"] == request.task_sha256
    assert json.loads(request.private_result.read_text()) == result


@pytest.mark.parametrize(
    ("metrics", "status", "compiled"),
    [
        (_metrics(call_ok=False, exe_ok=False, perf_ok=False), "compile_failed", False),
        (_metrics(exe_ok=False, perf_ok=False), "incorrect", True),
    ],
)
def test_candidate_failures_are_structured_and_stdout_does_not_drive_state(
    tmp_path: Path, metrics, status: str, compiled: bool
) -> None:
    request = _request(tmp_path)
    result = run_supervisor(
        request,
        snapshot_verifier=_snapshot,
        pipeline_executor=_execute_with(metrics),
    )
    assert result["status"] == status
    assert result["compiled"] is compiled
    assert result["correct"] is False
    assert result["candidate_runtime_ms"] is None
    assert result["reference_runtime_ms"] is None
    assert "999999" not in result["error_summary"]


def test_private_result_path_is_never_delegated_to_official_candidate_pipeline(
    tmp_path: Path,
) -> None:
    request = _request(tmp_path)
    staged_repository = tmp_path / "staged-repository"
    staged_repository.mkdir()
    (staged_repository / "scripts").mkdir()
    (staged_repository / "scripts/run_eval_from_files.sh").write_text(
        "#!/bin/sh\nexit 0\n", encoding="utf-8"
    )
    staged_candidate = tmp_path / Path(request.task_id).name
    staged_candidate.write_bytes(request.candidate.read_bytes())
    python_prefix = tmp_path / "python-prefix"
    (python_prefix / "bin").mkdir(parents=True)
    python_executable = python_prefix / "bin/python"
    python_executable.write_text("fake\n", encoding="utf-8")
    python_executable.chmod(0o755)
    python_include = tmp_path / "python-include"
    (python_include / "python3.10").mkdir(parents=True)
    (python_include / "x86_64-linux-gnu/python3.10").mkdir(parents=True)
    (python_include / "python3.10/Python.h").write_text(
        "/* frozen */\n", encoding="utf-8"
    )
    (python_include / "x86_64-linux-gnu/python3.10/pyconfig.h").write_text(
        "/* frozen multiarch */\n", encoding="utf-8"
    )
    command, environment, output_dir = build_official_command(
        request,
        staged_inputs=StagedWorkerInputs(staged_repository, staged_candidate),
        bwrap_path=Path("/usr/bin/bwrap"),
        python_prefix=python_prefix,
        python_executable=python_executable,
        python_include=python_include,
        python_include_sha256=hash_immutable_tree(python_include),
        system_roots=(Path("/usr"),),
        gpu_devices=(Path("/dev/nvidia4"), Path("/dev/nvidiactl")),
    )
    private = str(request.private_result)

    assert private not in command
    assert all(private not in value for value in environment.values())
    assert output_dir.is_relative_to(request.scratch_dir)
    assert str(request.repository) not in command
    assert str(request.candidate) not in command
    assert str(staged_repository) in command
    assert str(staged_candidate) in command
    assert "--unshare-net" in command
    assert "--clearenv" in command
    assert environment == {
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "PATH": "/usr/bin:/bin",
    }


def test_snapshot_and_hashes_are_checked_before_and_after_candidate_execution(
    tmp_path: Path,
) -> None:
    request = _request(tmp_path)
    checks: list[str] = []

    def verifier(current: SupervisorRequest) -> None:
        checks.append("snapshot")
        _snapshot(current)

    def mutate_task(
        current: SupervisorRequest, output_dir: Path
    ) -> OfficialPipelineOutcome:
        outcome = _execute_with(_metrics())(current, output_dir)
        (current.repository / current.task_path).write_text("tampered", encoding="utf-8")
        return outcome

    with pytest.raises(ValueError, match="snapshot changed"):
        run_supervisor(
            request,
            snapshot_verifier=verifier,
            pipeline_executor=mutate_task,
        )
    assert checks == ["snapshot", "snapshot"]
    assert not request.private_result.exists()


def test_rejects_overlapping_private_result_and_candidate_controlled_roots(
    tmp_path: Path,
) -> None:
    request = _request(tmp_path)
    unsafe = replace(
        request,
        private_result=request.scratch_dir / "candidate-can-write.json",
    )
    with pytest.raises(ValueError, match="private result"):
        run_supervisor(
            unsafe,
            snapshot_verifier=_snapshot,
            pipeline_executor=_execute_with(_metrics()),
        )


def test_cli_contract_is_exact_and_candidate_failure_still_exits_zero(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = _request(tmp_path)
    argv = request.to_argv()
    assert "--canary-id" in argv
    assert "--private-result" in argv

    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.verify_frozen_snapshot",
        _snapshot,
    )
    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.execute_official_pipeline",
        _execute_with(_metrics(call_ok=False, exe_ok=False, perf_ok=False)),
    )
    from scripts.hb_gen1_kernelbenchx_supervisor import main

    assert main(argv) == 0
    assert json.loads(request.private_result.read_text())["status"] == "compile_failed"


def test_default_snapshot_verifier_requires_clean_pinned_checkout(tmp_path: Path) -> None:
    request = _request(tmp_path)
    with pytest.raises(ValueError, match="repository"):
        run_supervisor(
            request,
            pipeline_executor=_execute_with(_metrics()),
        )


@pytest.mark.parametrize(
    ("source", "status"),
    [
        ("print('correctness=True speedup=999999')\n", "policy_rejected"),
        ("def matmul_w8a8(:\n", "compile_failed"),
    ],
)
def test_static_candidate_rejections_are_score_bearing_canary_outcomes(
    tmp_path: Path, source: str, status: str
) -> None:
    request = _request(tmp_path)
    request.candidate.chmod(0o600)
    request.candidate.write_text(source, encoding="utf-8")
    request.candidate.chmod(0o400)
    request = replace(
        request,
        candidate_sha256=hashlib.sha256(request.candidate.read_bytes()).hexdigest(),
    )
    calls: list[str] = []

    def must_not_execute(
        _request: SupervisorRequest, _output: Path
    ) -> OfficialPipelineOutcome:
        calls.append("executed")
        raise AssertionError("static rejection must not execute candidate code")

    result = run_supervisor(
        request,
        snapshot_verifier=_snapshot,
        pipeline_executor=must_not_execute,
    )
    assert result["status"] == status
    assert result["correct"] is False
    assert calls == []


def test_non_quiescent_worker_can_never_produce_a_valid_score(tmp_path: Path) -> None:
    request = _request(tmp_path)

    def escaped_worker(
        current: SupervisorRequest, output_dir: Path
    ) -> OfficialPipelineOutcome:
        outcome = _execute_with(_metrics())(current, output_dir)
        return replace(outcome, quiescent=False)

    result = run_supervisor(
        request,
        snapshot_verifier=_snapshot,
        pipeline_executor=escaped_worker,
    )

    assert result["status"] == "environment_invalid"
    assert result["correct"] is False
    assert result["candidate_runtime_ms"] is None
    assert result["reference_runtime_ms"] is None


def test_default_pipeline_runs_only_the_isolated_staged_worker(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = _request(tmp_path)
    staged_repository = tmp_path / "staged-repository"
    staged_repository.mkdir()
    (staged_repository / "scripts").mkdir()
    (staged_repository / "scripts/run_eval_from_files.sh").write_text(
        "#!/bin/sh\nexit 0\n", encoding="utf-8"
    )
    staged_candidate = tmp_path / Path(request.task_id).name
    staged_candidate.write_bytes(request.candidate.read_bytes())
    python_prefix = tmp_path / "python-prefix"
    (python_prefix / "bin").mkdir(parents=True)
    python_executable = python_prefix / "bin/python"
    python_executable.write_text("fake\n", encoding="utf-8")
    python_executable.chmod(0o755)
    python_include = tmp_path / "python-include"
    (python_include / "python3.10").mkdir(parents=True)
    (python_include / "x86_64-linux-gnu/python3.10").mkdir(parents=True)
    (python_include / "python3.10/Python.h").write_text(
        "/* frozen */\n", encoding="utf-8"
    )
    (python_include / "x86_64-linux-gnu/python3.10/pyconfig.h").write_text(
        "/* frozen multiarch */\n", encoding="utf-8"
    )
    observed: list[BubblewrapCommand] = []

    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.stage_git_worker_inputs",
        lambda **_kwargs: StagedWorkerInputs(staged_repository, staged_candidate),
    )
    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.resolve_trusted_bwrap",
        lambda: Path("/usr/bin/bwrap"),
    )
    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.discover_system_roots",
        lambda: (Path("/usr"),),
    )
    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.discover_gpu_devices",
        lambda _gpu: (Path("/dev/nvidia4"), Path("/dev/nvidiactl")),
    )
    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor._python_runtime",
        lambda: (python_prefix, python_executable),
    )
    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.KERNELBENCHX_PYTHON_INCLUDE",
        python_include,
    )
    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.KERNELBENCHX_PYTHON_INCLUDE_SHA256",
        hash_immutable_tree(python_include),
    )

    def isolated_run(launch: BubblewrapCommand, **_kwargs) -> IsolatedProcessOutcome:
        observed.append(launch)
        return IsolatedProcessOutcome(
            returncode=0,
            timed_out=False,
            quiescent=True,
            elapsed_seconds=1.25,
        )

    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.run_bubblewrap_process",
        isolated_run,
    )
    from scripts.hb_gen1_kernelbenchx_supervisor import execute_official_pipeline

    outcome = execute_official_pipeline(request, request.scratch_dir / "official")

    assert outcome.returncode == 0
    assert outcome.quiescent is True
    assert len(observed) == 1
    serialized = "\0".join(observed[0].argv)
    assert str(request.repository) not in serialized
    assert str(request.private_result) not in serialized
    assert str(staged_repository) in serialized


def test_default_pipeline_fails_closed_without_trusted_sandbox(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = _request(tmp_path)
    monkeypatch.setattr(
        "scripts.hb_gen1_kernelbenchx_supervisor.resolve_trusted_bwrap",
        lambda: (_ for _ in ()).throw(SandboxContractError("missing sandbox")),
    )
    from scripts.hb_gen1_kernelbenchx_supervisor import execute_official_pipeline

    with pytest.raises(SandboxContractError, match="missing sandbox"):
        execute_official_pipeline(request, request.scratch_dir / "official")
