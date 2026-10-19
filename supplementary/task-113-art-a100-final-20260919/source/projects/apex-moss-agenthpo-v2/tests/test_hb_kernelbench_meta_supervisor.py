from __future__ import annotations

import json
import hashlib
import subprocess
import sys
from pathlib import Path

import pytest

from optimization_lab.harness_builder.meta_train import MetaTrainContract
from scripts.run_harness_builder_meta_train import _preflight
from scripts import hb_gen1_kernelbench_meta_supervisor as supervisor_module
from optimization_lab.harness_builder.adapters.kernelbench_meta import (
    KERNELBENCH_META_CANARY_TASKS,
    KERNELBENCH_META_EVALUATOR_ID,
    KERNELBENCH_META_PROTOCOL_SHA256,
    KERNELBENCH_META_REPOSITORY_COMMIT,
    KERNELBENCH_META_TASK_HASHES,
    KERNELBENCH_META_TASK_SET_SHA256,
    KernelBenchMetaAdapter,
    KernelBenchMetaTask,
    MetaSnapshotIdentity,
)
from optimization_lab.harness_builder.adapters.kernelbench_meta_isolation import (
    kernelbench_meta_scorer_bundle_sha256,
)
from optimization_lab.harness_builder.adapters.kernel_candidate_invocation import (
    KERNEL_INVOCATION_SCHEDULE_SHA256,
)
from optimization_lab.harness_builder.adapters.kernel_candidate_policy import (
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
)


ROOT = Path(__file__).resolve().parents[1]
SUPERVISOR = ROOT / "scripts/hb_gen1_kernelbench_meta_supervisor.py"


def _safe_candidate() -> str:
    return """import torch
import torch.nn as nn

class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid(x)
"""


def test_production_supervisor_reports_and_enforces_the_fail_closed_boundary(
    tmp_path: Path,
) -> None:
    private_result = tmp_path / "private-result.json"
    candidate_marker = tmp_path / "candidate-ran"
    candidate = tmp_path / "candidate.py"
    candidate.write_text(
        f"from pathlib import Path\nPath({str(candidate_marker)!r}).touch()\n",
        encoding="utf-8",
    )

    process = subprocess.run(
        (
            sys.executable,
            "-I",
            str(SUPERVISOR),
            "--capability-report",
            "--candidate",
            str(candidate),
            "--private-result",
            str(private_result),
            "--gpu",
            "4",
        ),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=10,
        check=False,
    )

    assert process.returncode == 78
    report = json.loads(process.stdout)
    assert report["execution_ready"] is False
    assert report["candidate_invocation_abi"] == "restricted_torch_cuda_runtime_v1"
    assert report["trusted_invocation_loop_implemented"] is True
    assert report["production_runtime_implemented"] is True
    assert report["candidate_policy_check"] == "rejected"
    assert len(report["candidate_policy_sha256"]) == 64
    assert report["legacy_stdout_parser_allowed"] is False
    assert report["legacy_same_process_scorer_allowed"] is False
    assert report["gpu_or_candidate_execution"] is False
    assert not candidate_marker.exists()
    assert not private_result.exists()


def test_production_supervisor_independently_checks_candidate_policy(
    tmp_path: Path,
) -> None:
    candidate = tmp_path / "candidate.py"
    candidate.write_text(_safe_candidate(), encoding="utf-8")
    process = subprocess.run(
        (
            sys.executable,
            "-I",
            str(SUPERVISOR),
            "--capability-report",
            "--candidate",
            str(candidate),
            "--task-id",
            "level1/21_Sigmoid.py",
        ),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=10,
        check=False,
    )

    assert process.returncode == 78
    report = json.loads(process.stdout)
    assert report["candidate_invocation_abi"] == "restricted_torch_cuda_runtime_v1"
    assert report["candidate_policy_check"] == "accepted"
    assert report["execution_ready"] is False
    assert report["blocker"] == "kernelbench_meta_canary_pending"


def test_meta_train_cli_gate_names_the_abi_and_canary_budget_blockers(
    tmp_path: Path,
) -> None:
    contract = MetaTrainContract.from_json(
        ROOT / "optimization_lab/harness_builder/data/experience_bank_v1.json"
    )
    entitlements = {
        source.cell_id: {
            "model_calls": 16,
            "evaluator_transactions": 8,
            "gpu_exclusive_seconds": 4800.0,
            "cpu_evaluator_seconds": 0.0,
        }
        for source in contract.new_sources
    }
    entitlements["meta:distillation"] = {
        "model_calls": 8,
        "evaluator_transactions": 0,
        "gpu_exclusive_seconds": 0.0,
        "cpu_evaluator_seconds": 0.0,
    }
    (tmp_path / "staging_plan.json").write_text(
        json.dumps({"cell_entitlements": entitlements}), encoding="utf-8"
    )

    report = _preflight(
        project_root=ROOT,
        artifact_root=tmp_path,
        historical_paths=(),
    )

    assert report["execution_ready"] is False
    assert "kernelbench_meta_canary_pending" in report["blockers"]
    assert "kernelbench_meta_canary_entitlement_missing" in report["blockers"]
    assert report["trusted_meta_evaluator"]["legacy_stdout_parser_allowed"] is False
    assert report["trusted_meta_evaluator"]["trusted_invocation_loop_implemented"] is True
    assert report["trusted_meta_evaluator"]["production_runtime_implemented"] is True
    assert report["trusted_meta_evaluator"]["supervisor_sha256"]


def _supervisor_request(tmp_path: Path, *, canary_id: str) -> supervisor_module.SupervisorRequest:
    task_id = "level1/21_Sigmoid.py"
    repository = tmp_path / "KernelBench"
    repository.mkdir(parents=True)
    attempt = tmp_path / "attempt"
    scratch = attempt / "scratch"
    cache = attempt / "cache"
    candidate_dir = attempt / "candidate"
    for path in (scratch, cache, candidate_dir):
        path.mkdir(parents=True)
    candidate = candidate_dir / "candidate.py"
    candidate.write_text(_safe_candidate(), encoding="utf-8")
    return supervisor_module.SupervisorRequest(
        repository=repository,
        repository_commit=KERNELBENCH_META_REPOSITORY_COMMIT,
        task_id=task_id,
        task_path=f"KernelBench/{task_id}",
        task_sha256=KERNELBENCH_META_TASK_HASHES[task_id],
        candidate=candidate,
        candidate_sha256=hashlib.sha256(candidate.read_bytes()).hexdigest(),
        candidate_policy_sha256=RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
        invocation_schedule_sha256=KERNEL_INVOCATION_SCHEDULE_SHA256,
        scratch_dir=scratch,
        cache_dir=cache,
        private_result=tmp_path / "private" / "result.json",
        attempt_id="attempt-a",
        result_nonce="1" * 64,
        canary_id=canary_id,
        gpu="4",
        evaluator=KERNELBENCH_META_EVALUATOR_ID,
        protocol_sha256=KERNELBENCH_META_PROTOCOL_SHA256,
        scorer_sha256=kernelbench_meta_scorer_bundle_sha256(ROOT),
        authorization_receipt=None,
    )


def test_formal_and_unregistered_canary_are_hard_closed_before_gpu(
    tmp_path: Path,
) -> None:
    formal = _supervisor_request(tmp_path / "formal", canary_id="formal")
    with pytest.raises(
        supervisor_module.SupervisorContractError, match="authorization receipt"
    ):
        supervisor_module.validate_request(formal)

    unknown = _supervisor_request(tmp_path / "unknown", canary_id="unregistered")
    with pytest.raises(
        supervisor_module.SupervisorContractError, match="canary id/task"
    ):
        supervisor_module.validate_request(unknown)


def test_content_addressed_canary_receipt_binds_revision_budget_and_task_set(
    tmp_path: Path, monkeypatch
) -> None:
    request = _supervisor_request(tmp_path, canary_id="adversarial-fake-stdout")
    revision = "a" * 40
    payload = {
        "schema_version": 1,
        "authorization_type": "hb-gen1-kernelbench-meta-canary-v1",
        "scorer_bundle_sha256": request.scorer_sha256,
        "protocol_sha256": request.protocol_sha256,
        "repository_commit": request.repository_commit,
        "task_set_sha256": KERNELBENCH_META_TASK_SET_SHA256,
        "code_revision": revision,
        "ledger_head_sha256": "0" * 64,
        "staging_plan_sha256": "c" * 64,
        "canary_plan_sha256": "d" * 64,
        "canary_ids": list(KERNELBENCH_META_CANARY_TASKS),
        "max_evaluator_transactions": 10,
        "max_gpu_exclusive_seconds": 6000,
        "canary_evidence_sha256": None,
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    receipt = tmp_path / "authorization" / f"{hashlib.sha256(raw).hexdigest()}.json"
    receipt.parent.mkdir()
    receipt.write_bytes(raw)
    request = supervisor_module.SupervisorRequest(
        **{**request.__dict__, "authorization_receipt": receipt}
    )

    monkeypatch.setattr(
        supervisor_module,
        "_git_output",
        lambda _root, args: revision if tuple(args) == ("rev-parse", "HEAD") else "",
    )
    assert supervisor_module.validate_request(request) == request.candidate.read_bytes()

    receipt.write_bytes(raw + b"\n")
    with pytest.raises(
        supervisor_module.SupervisorContractError, match="content addressed"
    ):
        supervisor_module.validate_request(request)


@pytest.mark.parametrize(
    ("canary_id", "authorization_type", "canary_evidence"),
    (
        (
            "adversarial-fake-stdout",
            "hb-gen1-kernelbench-meta-canary-v1",
            None,
        ),
        ("formal", "hb-gen1-kernelbench-meta-formal-v1", "c" * 64),
    ),
)
def test_adapter_receipt_is_consumed_by_real_supervisor_contract_without_worker_access(
    tmp_path: Path,
    monkeypatch,
    canary_id: str,
    authorization_type: str,
    canary_evidence: str | None,
) -> None:
    revision = "a" * 40
    scorer_sha = kernelbench_meta_scorer_bundle_sha256(ROOT)
    payload = {
        "schema_version": 1,
        "authorization_type": authorization_type,
        "scorer_bundle_sha256": scorer_sha,
        "protocol_sha256": KERNELBENCH_META_PROTOCOL_SHA256,
        "repository_commit": KERNELBENCH_META_REPOSITORY_COMMIT,
        "task_set_sha256": KERNELBENCH_META_TASK_SET_SHA256,
        "code_revision": revision,
        "ledger_head_sha256": (
            "0" * 64 if canary_id != "formal" else "b" * 64
        ),
        "staging_plan_sha256": "d" * 64,
        "canary_plan_sha256": "e" * 64,
        "canary_ids": list(KERNELBENCH_META_CANARY_TASKS),
        "max_evaluator_transactions": 10,
        "max_gpu_exclusive_seconds": 6000,
        "canary_evidence_sha256": canary_evidence,
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    receipt = tmp_path / "authorization" / f"{hashlib.sha256(raw).hexdigest()}.json"
    receipt.parent.mkdir()
    receipt.write_bytes(raw)
    receipt.chmod(0o600)

    repository = tmp_path / "KernelBench"
    repository.mkdir()
    candidate = tmp_path / "candidate.py"
    candidate.write_text(_safe_candidate(), encoding="utf-8")
    task_id = "level1/21_Sigmoid.py"
    adapter = KernelBenchMetaAdapter(
        repository=repository,
        supervisor=SUPERVISOR,
        scorer_sha256=scorer_sha,
        scratch_root=tmp_path / "attempts",
        authorization_receipt=receipt,
        gpu="4",
        snapshot_inspector=lambda _repository, task: MetaSnapshotIdentity(
            repository_commit=task.repository_commit,
            task_sha256=task.task_sha256,
        ),
        attempt_id_factory=lambda: "adapter-bound",
        nonce_factory=lambda: "d" * 64,
    )
    command = adapter.prepare_attempt(
        KernelBenchMetaTask.from_task_id(task_id),
        candidate,
        tmp_path / "private",
        canary_id=canary_id,
    )
    namespace = supervisor_module._parser().parse_args(command.argv[3:])
    request = supervisor_module._request(namespace)
    monkeypatch.setattr(
        supervisor_module,
        "_git_output",
        lambda _root, args: revision if tuple(args) == ("rev-parse", "HEAD") else "",
    )

    assert supervisor_module.validate_request(request) == command.candidate_path.read_bytes()
    assert request.authorization_receipt == command.authorization_receipt_path
    assert str(receipt.resolve()) not in "\0".join(command.worker_visible_argv)


def _worker_outcome(payload: dict[str, object]) -> supervisor_module.TrustedWorkerOutcome:
    return supervisor_module.TrustedWorkerOutcome(
        returncode=0,
        timed_out=False,
        quiescent=True,
        elapsed_seconds=1.0,
        evidence=json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(),
    )


def _health_outcome() -> supervisor_module.TrustedWorkerOutcome:
    return _worker_outcome(
        {
            "schema_version": 1,
            "status": "passed",
            "hardware": "NVIDIA A100-SXM4-80GB",
        }
    )


def _valid_worker_payload(
    request: supervisor_module.SupervisorRequest,
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "evaluator": request.evaluator,
        "protocol_sha256": request.protocol_sha256,
        "scorer_sha256": request.scorer_sha256,
        "attempt_id": request.attempt_id,
        "result_nonce": request.result_nonce,
        "repository_commit": request.repository_commit,
        "task_id": request.task_id,
        "task_sha256": request.task_sha256,
        "candidate_sha256": request.candidate_sha256,
        "candidate_policy_sha256": request.candidate_policy_sha256,
        "schedule_sha256": request.invocation_schedule_sha256,
        "input_schedule_sha256": "d" * 64,
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
        "hardware": "NVIDIA A100-SXM4-80GB",
    }


def test_supervisor_preserves_schedule_bindings_in_outer_private_result(
    tmp_path: Path, monkeypatch
) -> None:
    request = _supervisor_request(tmp_path, canary_id="adversarial-fake-stdout")
    outcomes = iter(
        (
            _health_outcome(),
            _worker_outcome(_valid_worker_payload(request)),
            _health_outcome(),
        )
    )
    monkeypatch.setattr(supervisor_module, "validate_request", lambda _request: b"ok")

    result = supervisor_module.run_supervisor(
        request,
        snapshot_verifier=lambda _request: None,
        worker_executor=lambda _request, _phase: next(outcomes),
    )

    assert result["status"] == "valid"
    assert result["schedule_sha256"] == request.invocation_schedule_sha256
    assert result["input_schedule_sha256"] == "d" * 64
    assert json.loads(request.private_result.read_text()) == result


def test_malformed_worker_evidence_is_candidate_failure_not_control_channel(
    tmp_path: Path, monkeypatch
) -> None:
    request = _supervisor_request(tmp_path, canary_id="adversarial-fake-stdout")
    malformed = supervisor_module.TrustedWorkerOutcome(
        returncode=0,
        timed_out=False,
        quiescent=True,
        elapsed_seconds=1.0,
        evidence=b"{}",
    )
    outcomes = iter((_health_outcome(), malformed, _health_outcome()))
    monkeypatch.setattr(supervisor_module, "validate_request", lambda _request: b"ok")

    result = supervisor_module.run_supervisor(
        request,
        snapshot_verifier=lambda _request: None,
        worker_executor=lambda _request, _phase: next(outcomes),
    )

    assert result["status"] == "compile_failed"
    assert result["health_probe"] == "passed"
    assert result["input_schedule_sha256"] is None
    assert result["candidate_runtime_ms"] is None
