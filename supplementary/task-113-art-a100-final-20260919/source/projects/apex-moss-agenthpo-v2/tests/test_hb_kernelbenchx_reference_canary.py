from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path
from types import MappingProxyType

import pytest

import optimization_lab.harness_builder.adapters.kernelbenchx as kernelbenchx
from optimization_lab.adapters.base import EvaluationStatus
from optimization_lab.harness_builder.adapters.kernelbenchx import (
    ADVERSARIAL_CANARY_IDS,
    KernelBenchXAdapter,
    KernelBenchXTask,
    ProcessOutcome,
    SnapshotIdentity,
    parse_supervisor_evidence,
)
from optimization_lab.harness_builder.kernelbenchx_reference import (
    load_kernelbenchx_reference_canary,
    prepare_kernelbenchx_reference_canary,
)


TASK_ID = "Quantization/matmul_w8a8.py"
SEPARATOR = "#" * 146
TASK_SOURCE = (
    "import torch\n\n"
    "def matmul_w8a8(input, weight):\n"
    "    return torch.matmul(input, weight)\n\n"
    f"{SEPARATOR}\n\n"
    "def test_matmul_w8a8():\n"
    "    return matmul_w8a8(1, 1)\n\n"
    "test_results = test_matmul_w8a8()\n"
)


def _fixture(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> tuple[Path, KernelBenchXTask, KernelBenchXAdapter]:
    task_sha256 = hashlib.sha256(TASK_SOURCE.encode("utf-8")).hexdigest()
    monkeypatch.setattr(
        kernelbenchx,
        "KERNELBENCHX_TASK_HASHES",
        MappingProxyType({TASK_ID: task_sha256}),
    )
    task = KernelBenchXTask.from_task_id(TASK_ID)
    repository = tmp_path / "KernelBenchX"
    source = repository / task.source_path
    source.parent.mkdir(parents=True)
    source.write_text(TASK_SOURCE, encoding="utf-8")
    supervisor = tmp_path / "supervisor.py"
    supervisor.write_text("# trusted fixture\n", encoding="utf-8")

    def inspect(_repository: Path, current: KernelBenchXTask) -> SnapshotIdentity:
        return SnapshotIdentity(
            repository_commit=current.repository_commit,
            dataset_commit=current.dataset_commit,
            task_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        )

    adapter = KernelBenchXAdapter(
        repository=repository,
        supervisor=supervisor,
        scratch_root=tmp_path / "attempts",
        gpu="0",
        runner=lambda _command: ProcessOutcome(returncode=0),
        snapshot_inspector=inspect,
    )
    return repository, task, adapter


def test_prepare_is_content_addressed_idempotent_and_consumed_by_plan(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository, task, adapter = _fixture(tmp_path, monkeypatch)
    output_root = tmp_path / "prepared-reference"
    prepared = prepare_kernelbenchx_reference_canary(
        repository=repository,
        task=task,
        output_root=output_root,
        snapshot_inspector=adapter._snapshot_inspector,
    )
    restored = load_kernelbenchx_reference_canary(prepared.manifest_path, task=task)
    repeated = prepare_kernelbenchx_reference_canary(
        repository=repository,
        task=task,
        output_root=output_root,
        snapshot_inspector=adapter._snapshot_inspector,
    )

    assert repeated == restored == prepared
    assert prepared.candidate_path.name == f"{prepared.candidate_sha256}.py"
    assert prepared.manifest_path.name == f"{prepared.manifest_sha256}.json"
    assert SEPARATOR not in prepared.candidate_path.read_text(encoding="utf-8")
    assert "def test_" not in prepared.candidate_path.read_text(encoding="utf-8")

    adversarial = {}
    for canary_id in ADVERSARIAL_CANARY_IDS:
        path = tmp_path / f"{canary_id}.py"
        path.write_text(f"print({canary_id!r})\n", encoding="utf-8")
        adversarial[canary_id] = path
    plan = adapter.build_preflight_command_plan(
        task,
        reference_candidate_manifest=prepared.manifest_path,
        adversarial_candidates=adversarial,
        private_log_dir=tmp_path / "private",
    )
    assert plan[0].command.candidate_sha256 == prepared.candidate_sha256
    assert [item.canary_id for item in plan] == ["reference", *ADVERSARIAL_CANARY_IDS]
    assert len({item.command.attempt_root for item in plan}) == 4
    assert len({item.command.cache_dir for item in plan}) == 4
    for item in plan:
        assert "--repository-commit" in item.command.argv
        assert task.repository_commit in item.command.argv
        assert "--task-sha256" in item.command.argv
        assert task.task_sha256 in item.command.argv
        assert "--private-result" in item.command.argv

    reference_command = plan[0].command
    reference_payload = {
        "schema_version": 1,
        "evaluator": kernelbenchx.KERNELBENCHX_EVALUATOR_ID,
        "attempt_id": reference_command.attempt_id,
        "repository_commit": task.repository_commit,
        "dataset_commit": task.dataset_commit,
        "task_id": task.task_id,
        "task_sha256": task.task_sha256,
        "candidate_sha256": reference_command.candidate_sha256,
        "status": "valid",
        "compiled": True,
        "correct": True,
        "candidate_runtime_ms": 1.0,
        "reference_runtime_ms": 2.0,
        "reference_compile_runtime_ms": None,
        "error_summary": "",
        "elapsed_seconds": 3.0,
        "gpu_seconds": 3.0,
        "hardware": "fake-a100",
    }
    reference_command.private_result_path.write_text(
        json.dumps(reference_payload), encoding="utf-8"
    )
    valid = parse_supervisor_evidence(
        reference_command.private_result_path,
        task=task,
        attempt_id=reference_command.attempt_id,
        candidate_sha256=reference_command.candidate_sha256,
    )
    assert plan[0].passed_by(valid)
    assert not plan[1].passed_by(valid)
    assert not plan[1].passed_by(
        replace(
            valid,
            status=EvaluationStatus.ENVIRONMENT_INVALID,
            compiled=False,
            correct=False,
            candidate_runtime_ms=None,
            reference_runtime_ms=None,
        )
    )

    with pytest.raises(ValueError, match="exactly"):
        adapter.build_preflight_command_plan(
            task,
            reference_candidate_manifest=prepared.manifest_path,
            adversarial_candidates={"fake_stdout": adversarial["fake_stdout"]},
            private_log_dir=tmp_path / "incomplete-private",
        )
    with pytest.raises(ValueError, match="formal solution contract"):
        adapter.build_preflight_command_plan(
            task,
            reference_candidate_manifest=repository / task.source_path,
            adversarial_candidates=adversarial,
            private_log_dir=tmp_path / "raw-task-private",
        )


def test_prepare_fails_closed_on_source_drift_and_object_overwrite(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository, task, adapter = _fixture(tmp_path, monkeypatch)
    output_root = tmp_path / "prepared-reference"
    prepared = prepare_kernelbenchx_reference_canary(
        repository=repository,
        task=task,
        output_root=output_root,
        snapshot_inspector=adapter._snapshot_inspector,
    )
    prepared.candidate_path.chmod(0o600)
    prepared.candidate_path.write_text("different\n", encoding="utf-8")

    with pytest.raises(ValueError, match="different content"):
        prepare_kernelbenchx_reference_canary(
            repository=repository,
            task=task,
            output_root=output_root,
            snapshot_inspector=adapter._snapshot_inspector,
        )

    source = repository / task.source_path
    source.write_text(TASK_SOURCE + "# drift\n", encoding="utf-8")
    with pytest.raises(ValueError, match="task sha256"):
        prepare_kernelbenchx_reference_canary(
            repository=repository,
            task=task,
            output_root=tmp_path / "drifted",
            snapshot_inspector=adapter._snapshot_inspector,
        )
