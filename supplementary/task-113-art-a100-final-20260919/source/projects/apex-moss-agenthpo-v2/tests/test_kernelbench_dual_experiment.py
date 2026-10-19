from __future__ import annotations

import hashlib
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from pathlib import Path

import pytest

from optimization_lab.adapters.base import EvaluationResult as AdapterResult
from optimization_lab.adapters.base import EvaluationStatus
from optimization_lab.generation import GenerationResult
from optimization_lab.harness_builder.dual_config import (
    DualHarnessModelConfig,
    create_dual_harness_runtime,
)
from optimization_lab.harness_builder.dual_harness import HarnessWorkspace, TaskHarnessRuntime
from optimization_lab.harness_builder.dual_runtime import (
    DualHarnessRoundResult,
    EvaluationResult,
    PublicEvaluation,
)
from optimization_lab.harness_builder.kernelbench_dual_experiment import (
    KernelBenchPublicEvaluator,
    _write_json_once,
    candidate_contract_tool,
    cross_test_frozen_harness,
    evolve_instance,
    initial_kernelbench_harness,
)
from optimization_lab.task_spec import TaskSpec


VALID_CANDIDATE = """```python
import torch
import torch.nn as nn

class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.cumsum(x, dim=1) - x
```"""


def task() -> TaskSpec:
    return TaskSpec(
        task_id="level1/92_cumsum_exclusive.py",
        display_name="Cumsum Exclusive",
        level=1,
        problem_id=92,
        task_path="KernelBench/level1/92_cumsum_exclusive.py",
        task_sha256="a" * 64,
        repository_commit="b" * 40,
        target_gpu="H200",
        gpu_arch="Hopper",
    )


class RecordingAdapter:
    def __init__(self, result: AdapterResult) -> None:
        self.result = result
        self.calls: list[tuple[TaskSpec, Path, Path]] = []

    def evaluate(
        self, task_spec: TaskSpec, candidate_path: Path, private_log_dir: Path
    ) -> AdapterResult:
        self.calls.append((task_spec, candidate_path, private_log_dir))
        private_log_dir.mkdir(parents=True, exist_ok=True)
        raw_log_path = private_log_dir / "raw.log"
        raw_log_path.write_text("PRIVATE EVALUATOR LOG", encoding="utf-8")
        return replace(
            self.result,
            raw_log_path=str(raw_log_path),
            hardware=self.result.hardware or "NVIDIA H200",
        )


def make_evaluator(
    tmp_path: Path, adapter: RecordingAdapter
) -> KernelBenchPublicEvaluator:
    return KernelBenchPublicEvaluator(
        task=task(),
        adapter=adapter,
        archive_root=tmp_path / "archive",
        cell_id="p0:cumsum:A",
        private_log_root=tmp_path / "private",
        gpu_uuid="GPU-fixed",
    )


def test_initial_harness_is_draft_contract_final_emit() -> None:
    artifact = initial_kernelbench_harness()
    assert artifact.version == 1
    assert artifact.parent_sha256 is None
    assert [(node.node_id, node.kind) for node in artifact.spec.nodes] == [
        ("draft", "model_call"),
        ("contract_report", "tool_call"),
        ("final", "model_call"),
        ("emit", "emit"),
    ]
    assert artifact.spec.nodes[1].tool == "candidate_contract"
    assert artifact.spec.nodes[-1].input_key == "final"
    assert "{contract_report}" in (artifact.spec.nodes[2].prompt or "")


def test_candidate_contract_tool_never_raises() -> None:
    accepted = candidate_contract_tool(VALID_CANDIDATE)
    rejected = candidate_contract_tool(object())
    assert accepted["accepted"] is True
    assert len(str(accepted["hash"])) == 64
    assert rejected["accepted"] is False
    json.dumps([accepted, rejected])


def test_invalid_candidate_scores_zero_without_gpu(tmp_path: Path) -> None:
    adapter = RecordingAdapter(
        AdapterResult(status=EvaluationStatus.INCORRECT, compiled=True, correct=False)
    )
    result = make_evaluator(tmp_path, adapter)("not Python", "round-001")
    assert result.public.score == 0.0
    assert "contract_rejected" in result.public.feedback
    assert adapter.calls == []


def test_valid_candidate_is_content_addressed_and_reused(tmp_path: Path) -> None:
    adapter = RecordingAdapter(
        AdapterResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=2.0,
            reference_runtime_ms=5.0,
        )
    )
    evaluator = make_evaluator(tmp_path, adapter)
    first = evaluator(VALID_CANDIDATE, "round-001")
    equivalent_response = VALID_CANDIDATE.replace("```python", "```py", 1)
    second = evaluator(equivalent_response, "round-002")

    assert first.public.score == second.public.score == 2.5
    first_path = adapter.calls[0][1]
    second_path = adapter.calls[1][1]
    expected_sha = hashlib.sha256(first_path.read_bytes()).hexdigest()
    assert first_path == second_path
    assert first_path.stem == expected_sha
    assert adapter.calls[0][2].name == "round-001"
    assert adapter.calls[1][2].name == "round-002"


def test_evaluator_writes_private_gpu_receipt_without_log_contents(
    tmp_path: Path,
) -> None:
    adapter = RecordingAdapter(
        AdapterResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=2.0,
            reference_runtime_ms=5.0,
            elapsed_seconds=12.5,
            gpu_seconds=12.5,
            hardware="NVIDIA H200 141GB",
        )
    )

    result = make_evaluator(tmp_path, adapter)(VALID_CANDIDATE, "round-001")

    private_dir = tmp_path / "private" / "round-001"
    started = json.loads(
        (private_dir / "evaluation_started.json").read_text(encoding="utf-8")
    )
    completed_path = private_dir / "evaluation_completed.json"
    completed = json.loads(completed_path.read_text(encoding="utf-8"))
    raw_log_path = private_dir / "raw.log"
    candidate_path = adapter.calls[0][1]
    assert started["phase"] == "started"
    assert started["gpu_uuid"] == "GPU-fixed"
    assert completed["phase"] == "completed"
    assert completed["candidate_sha256"] == hashlib.sha256(
        candidate_path.read_bytes()
    ).hexdigest()
    assert completed["raw_log_sha256"] == hashlib.sha256(
        raw_log_path.read_bytes()
    ).hexdigest()
    assert completed["elapsed_seconds"] == 12.5
    assert completed["gpu_seconds"] == 12.5
    assert completed["hardware"] == "NVIDIA H200 141GB"
    assert completed["gpu_uuid"] == "GPU-fixed"
    assert "PRIVATE EVALUATOR LOG" not in completed_path.read_text(encoding="utf-8")
    assert "raw_log_sha256" not in result.public.feedback


def test_environment_invalid_stops_learning(tmp_path: Path) -> None:
    adapter = RecordingAdapter(
        AdapterResult(
            status=EvaluationStatus.ENVIRONMENT_INVALID,
            compiled=False,
            correct=False,
            error_summary="SSH unavailable",
        )
    )
    with pytest.raises(RuntimeError, match="environment invalid"):
        make_evaluator(tmp_path, adapter)(VALID_CANDIDATE, "round-001")


def test_public_failure_feedback_removes_all_absolute_paths(tmp_path: Path) -> None:
    local_secret = str(tmp_path / "private" / "Jane Doe" / "raw log.txt")
    posix_secret = "/data/moss-p0/private/My Candidate.py"
    windows_secret = r"C:\private\Jane Doe\raw log.txt"
    unc_secret = r"\\server\private share\secret log.txt"
    drive_root = "C:\\"
    adapter = RecordingAdapter(
        AdapterResult(
            status=EvaluationStatus.COMPILE_FAILED,
            compiled=False,
            correct=False,
            error_summary=(
                f"compile failed at {local_secret}; source {posix_secret}; "
                f"details {windows_secret}; unc {unc_secret}; root {drive_root}"
            ),
        )
    )
    result = make_evaluator(tmp_path, adapter)(VALID_CANDIDATE, "round-001")
    assert result.public.score == 0.0
    for secret in (
        local_secret,
        posix_secret,
        windows_secret,
        unc_secret,
        drive_root,
    ):
        assert secret not in result.public.feedback
    for leaked_tail in ("Doe", "Candidate.py", "secret log.txt"):
        assert leaked_tail not in result.public.feedback
    assert json.loads(result.public.feedback)["error_summary"] == (
        "official evaluator reported compile_failed"
    )


class RecordingDualRuntime:
    def __init__(self, workspace: HarnessWorkspace) -> None:
        self.workspace = workspace
        self.calls: list[dict[str, object]] = []

    def run_round(self, **kwargs: object) -> DualHarnessRoundResult:
        self.calls.append(kwargs)
        run_id = str(kwargs["run_id"])
        evaluation = kwargs["evaluator"](VALID_CANDIDATE)
        return DualHarnessRoundResult(
            run_id=run_id,
            harness_sha256=self.workspace.current().sha256,
            candidate=VALID_CANDIDATE,
            score=evaluation.public.score,
            feedback=evaluation.public.feedback,
            builder_status="rejected",
            next_harness_sha256=self.workspace.current().sha256,
        )


def test_evolve_initializes_h0_and_uses_deterministic_round_ids(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    runtime = RecordingDualRuntime(workspace)
    ids: list[str] = []

    def evaluator(candidate: str, candidate_id: str) -> EvaluationResult:
        ids.append(candidate_id)
        return EvaluationResult(public=PublicEvaluation(1.0, "ok"))

    results = evolve_instance(
        runtime=runtime,
        workspace=workspace,
        task=task(),
        task_source="public source",
        evaluator=evaluator,
        rounds=2,
        execution_contract_sha256="c" * 64,
        run_prefix="cumsum-a",
    )
    assert [result.run_id for result in results] == [
        "cumsum-a-r001",
        "cumsum-a-r002",
    ]
    assert ids == ["cumsum-a-r001", "cumsum-a-r002"]
    assert all(set(call["tools"]) == {"candidate_contract"} for call in runtime.calls)


class ConstantGenerator:
    def __init__(self, response: str) -> None:
        self.response = response
        self.calls = 0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls += 1
        return GenerationResult(raw_response=self.response, provider="test")


def test_cross_test_uses_explicit_sha_and_does_not_change_current(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    h0 = workspace.commit(initial_kernelbench_harness())
    current_before = workspace.current().sha256
    generator = ConstantGenerator(VALID_CANDIDATE)
    result = cross_test_frozen_harness(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=generator),
        task=task(),
        task_source="public source",
        solver_model="gpt-5.6-sol",
        harness_sha256=h0.sha256,
        evaluator=lambda candidate, candidate_id: EvaluationResult(
            public=PublicEvaluation(1.25, "public")
        ),
        cross_test_id="h0-on-cumsum",
        receipt_root=tmp_path / "receipts",
    )
    assert result.harness_sha256 == h0.sha256
    assert result.score == 1.25
    assert generator.calls == 2
    assert workspace.current().sha256 == current_before


def test_identical_receipt_publishers_never_observe_partial_content(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    path = tmp_path / "receipt.json"
    payload = {"value": "same"}
    original_fdopen = os.fdopen
    first_entered = threading.Event()
    release_first = threading.Event()
    state_lock = threading.Lock()
    call_count = 0

    def blocking_fdopen(fd: int, mode: str):
        nonlocal call_count
        handle = original_fdopen(fd, mode)
        with state_lock:
            call_count += 1
            is_first = call_count == 1
        if not is_first:
            return handle

        class BlockedHandle:
            def __enter__(self):
                first_entered.set()
                assert release_first.wait(timeout=5)
                return handle

            def __exit__(self, exc_type, exc_value, traceback):
                return handle.__exit__(exc_type, exc_value, traceback)

        return BlockedHandle()

    monkeypatch.setattr(os, "fdopen", blocking_fdopen)
    with ThreadPoolExecutor(max_workers=2) as executor:
        first = executor.submit(_write_json_once, path, payload)
        assert first_entered.wait(timeout=5)
        second = executor.submit(_write_json_once, path, payload)
        second.result(timeout=5)
        release_first.set()
        first.result(timeout=5)

    assert json.loads(path.read_text(encoding="utf-8")) == payload


def test_receipt_never_overwrites_different_content(tmp_path: Path) -> None:
    path = tmp_path / "receipt.json"
    _write_json_once(path, {"value": "first"})
    with pytest.raises(ValueError, match="different content"):
        _write_json_once(path, {"value": "second"})
    assert json.loads(path.read_text(encoding="utf-8")) == {"value": "first"}


class _ScriptedStreamingClient:
    def __init__(self, *outputs: str) -> None:
        self.outputs = list(outputs)
        self.responses = self
        self.calls: list[dict[str, object]] = []

    def create(self, **kwargs: object) -> list[dict[str, object]]:
        self.calls.append(kwargs)
        output = self.outputs.pop(0)
        response = {
            "id": f"response-{len(self.calls)}",
            "status": "completed",
            "output_text": output,
            "usage": {"input_tokens": 1, "output_tokens": 1, "total_tokens": 2},
        }
        return [{"type": "response.completed", "response": response}]


def test_fake_round_persists_model_evaluator_and_round_evidence(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    h0 = workspace.commit(initial_kernelbench_harness())
    next_spec = h0.spec.to_dict()
    next_spec["nodes"][0]["prompt"] = "Draft a candidate and verify its contract for {task}"
    builder_proposal = json.dumps(
        {
            "schema_version": 1,
            "base_sha256": h0.sha256,
            "reason": "make contract verification explicit",
            "expected_effect": "reduce malformed candidate responses",
            "artifact": next_spec,
        }
    )
    client = _ScriptedStreamingClient(
        VALID_CANDIDATE,
        VALID_CANDIDATE,
        builder_proposal,
    )
    operations = tmp_path / "private_model_operations"
    runtime = create_dual_harness_runtime(
        DualHarnessModelConfig(
            builder_model="gpt-5.6-sol",
            solver_model="gpt-5.6-sol",
            builder_transport="openai_responses",
            solver_transport="openai_responses",
        ),
        workspace=workspace,
        operation_root=operations,
        openai_client=client,
    )
    adapter = RecordingAdapter(
        AdapterResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=2.0,
            reference_runtime_ms=5.0,
        )
    )
    evaluator = KernelBenchPublicEvaluator(
        task=task(),
        adapter=adapter,
        archive_root=tmp_path / "archive",
        cell_id="cumsum-gpu0",
        private_log_root=tmp_path / "private_evaluator",
        gpu_uuid="GPU-fixed",
    )

    (result,) = evolve_instance(
        runtime=runtime,
        workspace=workspace,
        task=task(),
        task_source="public source",
        evaluator=evaluator,
        rounds=1,
        execution_contract_sha256="c" * 64,
        run_prefix="cumsum-gpu0",
    )

    run_id = "cumsum-gpu0-r001"
    assert result.run_id == run_id
    assert len(list((operations / "solver" / "calls").glob("*/completed.json"))) == 2
    assert len(list((operations / "builder" / "calls").glob("*/completed.json"))) == 1
    assert (
        tmp_path / "private_evaluator" / run_id / "evaluation_completed.json"
    ).is_file()
    assert workspace.load_solver_result(run_id) is not None
    assert workspace.load_trace(run_id) is not None
    assert workspace.load_builder_trace(run_id) is not None
    assert workspace.load_round_receipt(run_id) is not None
