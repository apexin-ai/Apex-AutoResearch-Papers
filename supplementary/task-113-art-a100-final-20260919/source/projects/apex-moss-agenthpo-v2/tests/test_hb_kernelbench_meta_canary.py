from __future__ import annotations

import fcntl
import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.adapters.kernel_candidate_policy import (
    RestrictedKernelCandidateError,
    RestrictedKernelCandidatePolicy,
)
from optimization_lab.harness_builder.adapters.kernelbench_meta import (
    KERNELBENCH_META_CANARY_TASKS,
    MetaCanaryEvaluation,
)
from optimization_lab.harness_builder.kernelbench_meta_canary import (
    KernelBenchMetaCanaryController,
    KernelBenchMetaCanaryError,
    adversarial_candidate,
    prepare_kernelbench_meta_canary,
    reference_candidate_from_task_source,
    verify_kernelbench_meta_canary,
)
from optimization_lab.harness_builder.events import JournalIntegrityError
from optimization_lab.adapters.base import EvaluationResult, EvaluationStatus


PINNED_KERNELBENCH = Path(
    "/home/ubuntu/.cache/ccm/login-tmp/tmp.HheEwEGwQK/KernelBench"
)
EXPECTED_CANDIDATE_SHA256 = {
    "adversarial-fake-stdout": "2cb425149fb40858fde392fe72fc2b234f2d555451cb320e7a58f1aff3edc3cd",
    "adversarial-private-overwrite": "6721e1e7e8316ab36c746ad30fab26d36a0a0d72fbfd6d0dffcd65492baece2b",
    "adversarial-wrong": "daab023a4a9db45f30db0d2817618d230aa441342a44d62cda0edba2e6aac96b",
    "adversarial-first5-timing-wrong": "2e6deee4236e6d68ee9f5e104df9bed67fa5ebb8974772ce7c79fd152e9dc021",
    "reference-gemm-sigmoid-logsumexp": "c56d8589234f4a39ad8ce9efa7d68294f7e6d69a6b26556528fabb3334d57627",
    "reference-conv-relu-hardswish": "8f587e1e73664db6ab8034435a3269166e5b695e74e90ea2293e2caf4a83b3d7",
    "reference-conv-gelu-gap": "91a75ace3a19b20f53e59ca0c150ba75e7290c62902b20cce08d00f803ebd926",
    "reference-sdpa": "72ce7ed754b8a7e295ce3253772e7fd4f9832165c00895f85640f96d1e6bc062",
    "reference-cumsum": "3863bb5e78d2af2e582a5e782caf7fbd7ef7471b3d480e86b7fc59c146c89ec1",
    "reference-sigmoid": "4d8fcd67649400c86bfae5762bde28576e89809ff910fff85bfe2445a31d89dd",
}


def test_reference_extraction_omits_input_generators_and_normalizes_functional() -> None:
    task_source = """import torch
import torch.nn as nn

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()

    def forward(self, q, k, v):
        return torch.nn.functional.scaled_dot_product_attention(q, k, v)

BATCH = 1
def get_inputs():
    raise RuntimeError('trusted worker only')
"""

    candidate = reference_candidate_from_task_source(
        task_source, task_id="level1/97_ScaledDotProductAttention.py"
    )

    assert "class ModelNew(nn.Module)" in candidate
    assert "super().__init__()" in candidate
    assert "import torch.nn.functional as F" in candidate
    assert "F.scaled_dot_product_attention" in candidate
    assert "get_inputs" not in candidate
    assert "BATCH" not in candidate


@pytest.mark.parametrize(
    ("canary_id", "accepted"),
    (
        ("adversarial-wrong", True),
        ("adversarial-first5-timing-wrong", True),
        ("adversarial-fake-stdout", False),
        ("adversarial-private-overwrite", False),
    ),
)
def test_adversarial_canaries_have_the_frozen_policy_stage(
    canary_id: str, accepted: bool
) -> None:
    source = adversarial_candidate(canary_id)
    if accepted:
        RestrictedKernelCandidatePolicy().validate(
            source, task_id="level1/21_Sigmoid.py"
        )
    else:
        with pytest.raises(RestrictedKernelCandidateError):
            RestrictedKernelCandidatePolicy().validate(
                source, task_id="level1/21_Sigmoid.py"
            )


def test_exact_pinned_canary_plan_is_content_addressed_and_idempotent(
    tmp_path: Path,
) -> None:
    if not (PINNED_KERNELBENCH / ".git").exists():
        pytest.skip("exact pinned KernelBench checkout is unavailable")

    first = prepare_kernelbench_meta_canary(
        repository=PINNED_KERNELBENCH, artifact_root=tmp_path
    )
    second = prepare_kernelbench_meta_canary(
        repository=PINNED_KERNELBENCH, artifact_root=tmp_path
    )

    assert first == second
    assert first.plan_path.name == f"{first.plan_sha256}.json"
    assert hashlib.sha256(first.plan_path.read_bytes()).hexdigest() == first.plan_sha256
    assert len(first.payload["cases"]) == 10
    assert [case["canary_id"] for case in first.payload["cases"]] == list(
        KERNELBENCH_META_CANARY_TASKS
    )
    assert sum(
        case["expected_stage"] == "trusted_gpu_evaluator"
        for case in first.payload["cases"]
    ) == 8
    assert sum(
        case["expected_stage"] == "policy_preflight"
        for case in first.payload["cases"]
    ) == 2
    for case in first.payload["cases"]:
        path = first.plan_path.parent.parent / case["candidate_object"]
        assert case["candidate_sha256"] == EXPECTED_CANDIDATE_SHA256[
            case["canary_id"]
        ]
        assert path.name == f"{case['candidate_sha256']}.py"
        assert hashlib.sha256(path.read_bytes()).hexdigest() == case["candidate_sha256"]


class _FakeCanaryEvaluator:
    def __init__(
        self,
        *,
        authorization_receipt_sha256: str,
        crash_on: str | None = None,
        gpu_overrun_on: str | None = None,
    ) -> None:
        self.authorization_receipt_sha256 = authorization_receipt_sha256
        self.crash_on = crash_on
        self.gpu_overrun_on = gpu_overrun_on
        self.calls: list[str] = []

    def evaluate_canary(
        self, task, candidate_path, private_log_dir, *, canary_id
    ) -> MetaCanaryEvaluation:
        del task, candidate_path, private_log_dir
        self.calls.append(canary_id)
        if canary_id == self.crash_on:
            raise RuntimeError("simulated process loss after operation_started")
        if canary_id.startswith("reference-"):
            return MetaCanaryEvaluation(
                result=EvaluationResult(
                    status=EvaluationStatus.VALID,
                    compiled=True,
                    correct=True,
                    candidate_runtime_ms=1.0,
                    reference_runtime_ms=2.0,
                    elapsed_seconds=2.0,
                    gpu_seconds=(
                        601.0 if canary_id == self.gpu_overrun_on else 2.0
                    ),
                    hardware="NVIDIA A100-SXM4-80GB",
                ),
                correctness_passed=5,
                timing_trials_completed=100,
                timing_outputs_correct=100,
            )
        if canary_id in {
            "adversarial-fake-stdout",
            "adversarial-private-overwrite",
        }:
            return MetaCanaryEvaluation(
                result=EvaluationResult(
                    status=EvaluationStatus.POLICY_REJECTED,
                    compiled=False,
                    correct=False,
                    error_summary="expected static rejection",
                ),
                correctness_passed=0,
                timing_trials_completed=0,
                timing_outputs_correct=0,
            )
        counts = (5, 1, 0) if canary_id.endswith("first5-timing-wrong") else (0, 0, 0)
        return MetaCanaryEvaluation(
            result=EvaluationResult(
                status=EvaluationStatus.INCORRECT,
                compiled=True,
                correct=False,
                error_summary="expected wrong output",
                elapsed_seconds=1.0,
                gpu_seconds=(601.0 if canary_id == self.gpu_overrun_on else 1.0),
                hardware="NVIDIA A100-SXM4-80GB",
            ),
            correctness_passed=counts[0],
            timing_trials_completed=counts[1],
            timing_outputs_correct=counts[2],
        )


def _staging(path: Path, *, code_revision: str) -> Path:
    payload = {
        "schema_version": 1,
        "code_revision": code_revision,
        "cell_entitlements": {
            "canary:kernelbench-meta": {
                "model_calls": 0,
                "evaluator_transactions": 10,
                "gpu_exclusive_seconds": 6000.0,
                "cpu_evaluator_seconds": 0.0,
            }
        },
    }
    path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    return path


def _controller(tmp_path: Path) -> KernelBenchMetaCanaryController:
    if not (PINNED_KERNELBENCH / ".git").exists():
        pytest.skip("exact pinned KernelBench checkout is unavailable")
    prepared = prepare_kernelbench_meta_canary(
        repository=PINNED_KERNELBENCH,
        artifact_root=tmp_path / "prepared",
    )
    revision = "a" * 40
    arguments = {
        "artifact_root": tmp_path / "run",
        "staging_plan": _staging(
            tmp_path / "staging_plan.json", code_revision=revision
        ),
        "canary_plan": prepared.plan_path,
        "code_revision": revision,
        "scorer_bundle_sha256": "b" * 64,
    }
    request = KernelBenchMetaCanaryController(**arguments)
    raw = json.dumps(
        request.expected_authorization_payload(),
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    receipt = tmp_path / "external-authority" / f"{hashlib.sha256(raw).hexdigest()}.json"
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_bytes(raw)
    receipt.chmod(0o600)
    return KernelBenchMetaCanaryController(
        **arguments,
        authorization_receipt=receipt,
    )


def _evaluator(
    controller: KernelBenchMetaCanaryController, **kwargs
) -> _FakeCanaryEvaluator:
    assert controller.authorization_receipt_sha256 is not None
    return _FakeCanaryEvaluator(
        authorization_receipt_sha256=controller.authorization_receipt_sha256,
        **kwargs,
    )


def test_controller_requires_an_externally_supplied_authorization_receipt(
    tmp_path: Path,
) -> None:
    controller = _controller(tmp_path)
    unbound = KernelBenchMetaCanaryController(
        artifact_root=tmp_path / "run",
        staging_plan=controller.staging_path,
        canary_plan=controller.plan_path,
        code_revision=controller.code_revision,
        scorer_bundle_sha256="b" * 64,
    )

    report = unbound.preflight()

    assert report["status"] == "blocked"
    assert report["blockers"] == ["authorization_receipt_missing"]
    assert report["authorization_receipt_present"] is False
    assert "authorization_receipt" not in report


def test_controller_runs_all_ten_once_and_independent_replay_mints_only_evidence(
    tmp_path: Path,
) -> None:
    controller = _controller(tmp_path)
    evaluator = _evaluator(controller)

    evidence = controller.execute(evaluator)
    replay = controller.execute(evaluator)

    assert evidence == replay
    assert evidence.payload["status"] == "passed"
    assert evidence.payload["formal_activation_minted"] is False
    assert evidence.payload["evaluator_transactions"] == 10
    assert len(evidence.payload["results"]) == 10
    assert evaluator.calls == list(KERNELBENCH_META_CANARY_TASKS)
    assert controller.preflight()["status"] == "passed"
    assert controller.authorization_receipt.stat().st_mode & 0o777 == 0o600


def test_started_without_artifact_is_terminally_abandoned_and_never_resent(
    tmp_path: Path,
) -> None:
    controller = _controller(tmp_path)
    evaluator = _evaluator(controller, crash_on="adversarial-wrong")

    with pytest.raises(RuntimeError, match="simulated process loss"):
        controller.execute(evaluator)
    calls_after_crash = tuple(evaluator.calls)

    with pytest.raises(KernelBenchMetaCanaryError, match="abandoned"):
        controller.execute(evaluator)
    assert tuple(evaluator.calls) == calls_after_crash
    assert controller.preflight()["blockers"] == ["abandoned:adversarial-wrong"]


def test_independent_replay_rejects_a_changed_external_head_anchor(
    tmp_path: Path,
) -> None:
    controller = _controller(tmp_path)
    controller.execute(_evaluator(controller))
    anchor = controller.root / "trusted-head.json"
    payload = json.loads(anchor.read_text())
    payload["head_sha256"] = "0" * 64
    anchor.write_text(json.dumps(payload))

    with pytest.raises(JournalIntegrityError, match="anchor"):
        verify_kernelbench_meta_canary(
            root=controller.root,
            staging_plan_sha256=controller.staging_sha256,
            canary_plan=controller.plan_path,
            code_revision=controller.code_revision,
            scorer_bundle_sha256=controller.scorer_bundle_sha256,
            authorization_receipt=controller.authorization_receipt,
        )


def test_execute_lock_prevents_a_second_controller_from_reaching_evaluator(
    tmp_path: Path,
) -> None:
    controller = _controller(tmp_path)
    evaluator = _evaluator(controller)
    lock_path = controller.root / ".execute.lock"
    descriptor = lock_path.open("a+")
    fcntl.flock(descriptor.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    try:
        with pytest.raises(KernelBenchMetaCanaryError, match="execute lock"):
            controller.execute(evaluator)
    finally:
        descriptor.close()

    assert evaluator.calls == []


def test_gpu_overrun_is_not_clamped_and_leaves_a_terminal_abandoned_attempt(
    tmp_path: Path,
) -> None:
    controller = _controller(tmp_path)
    evaluator = _evaluator(controller, gpu_overrun_on="adversarial-wrong")

    with pytest.raises(KernelBenchMetaCanaryError, match="exceeded reservation"):
        controller.execute(evaluator)

    assert controller.preflight()["blockers"] == ["abandoned:adversarial-wrong"]
