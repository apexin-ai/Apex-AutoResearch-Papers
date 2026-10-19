from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from optimization_lab.harness_builder.adapters.kernel_candidate_invocation import (
    InvocationRuntime,
)
from optimization_lab.harness_builder.adapters.kernel_candidate_policy import (
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
)
from optimization_lab.harness_builder.adapters import kernelbench_meta_worker as worker


TASK_ID = "level1/21_Sigmoid.py"
SOURCE = b"""import torch
import torch.nn as nn

class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid(x)
"""


@dataclass
class _Handle:
    calls: int = 0


class _FakeRuntime(InvocationRuntime):
    hardware = "NVIDIA A100-SXM4-80GB"

    def __init__(self, _request: worker.WorkerRequest) -> None:
        self.clock = 0

    def capture_trusted_primitives(self):
        def clock() -> int:
            self.clock += 1_000_000
            return self.clock

        return {
            "clone_inputs": lambda value: tuple(value),
            "input_commitment": lambda value: hashlib.sha256(
                repr(tuple(value)).encode()
            ).hexdigest(),
            "inputs_unchanged": lambda before, after: before == after,
            "monotonic_ns": clock,
            "outputs_close": lambda expected, actual: expected == actual,
            "reference": lambda value: value[0] + 1,
            "seal_output": lambda value: value,
            "synchronize": lambda: None,
            "trusted_state_unchanged": lambda: True,
        }

    def load_candidate(self, source: bytes, policy_sha256: str):
        assert source == SOURCE
        assert policy_sha256 == RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256
        return _Handle()

    def fresh_inputs(self, *, phase: str, ordinal: int):
        return (hash((phase, ordinal)) & 0x7FFFFFFF,)

    def invoke_candidate(self, handle: _Handle, inputs):
        handle.calls += 1
        return inputs[0] + 1

    def close_candidate(self, handle: _Handle) -> None:
        pass

    def assert_quiescent(self) -> None:
        pass


def _request(tmp_path: Path, *, input_seed_nonce: str = "2" * 64) -> worker.WorkerRequest:
    repository = tmp_path / "repository"
    task = repository / "KernelBench" / TASK_ID
    task.parent.mkdir(parents=True)
    task.write_text("# frozen fake task\n", encoding="utf-8")
    candidate = tmp_path / "candidate.py"
    candidate.write_bytes(SOURCE)
    return worker.WorkerRequest(
        repository=repository,
        repository_commit="4" * 40,
        task_id=TASK_ID,
        task_sha256=hashlib.sha256(task.read_bytes()).hexdigest(),
        candidate=candidate,
        candidate_sha256=hashlib.sha256(SOURCE).hexdigest(),
        candidate_policy_sha256=RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
        schedule_sha256=worker.KERNEL_INVOCATION_SCHEDULE_SHA256,
        protocol_sha256="5" * 64,
        scorer_sha256="6" * 64,
        evaluator="fake-meta-evaluator",
        attempt_id="attempt-a",
        result_nonce="1" * 64,
        input_seed_nonce=input_seed_nonce,
        result_fd=3,
    )


def test_fake_worker_runs_all_bound_trials_without_torch_or_cuda(tmp_path: Path) -> None:
    request = _request(tmp_path)
    payload = worker.run_worker(request, runtime_factory=_FakeRuntime)

    assert payload["status"] == "valid"
    assert payload["correctness_passed"] == 5
    assert payload["timing_trials_completed"] == 100
    assert payload["timing_outputs_correct"] == 100
    assert payload["candidate_policy_sha256"] == (
        RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256
    )
    assert payload["input_schedule_sha256"]
    serialized = json.dumps(payload, sort_keys=True)
    assert request.input_seed_nonce not in serialized
    assert '"seed"' not in serialized


def test_private_nonce_seed_schedule_is_repeatable_but_not_publicly_fixed() -> None:
    first = [worker._seed_for("1" * 64, TASK_ID, "timing", index) for index in range(5)]
    replay = [worker._seed_for("1" * 64, TASK_ID, "timing", index) for index in range(5)]
    other = [worker._seed_for("2" * 64, TASK_ID, "timing", index) for index in range(5)]

    assert first == replay
    assert first != other
    assert len(set(first)) == len(first)


def test_worker_marks_result_fd_cloexec_before_any_runtime_action(monkeypatch) -> None:
    events: list[str] = []
    request = object()
    monkeypatch.setattr(worker, "_request", lambda _namespace: request)
    monkeypatch.setattr(
        worker,
        "run_worker",
        lambda value: events.append("runtime") or {"status": "valid"},
    )
    def fake_write(fd, payload):
        events.append(f"write:{fd}:{payload['status']}")
        events.append(f"close:{fd}")

    monkeypatch.setattr(worker, "write_result_fd", fake_write)
    monkeypatch.setattr(
        worker.os,
        "set_inheritable",
        lambda fd, value: events.append(f"cloexec:{fd}:{value}"),
    )
    monkeypatch.setattr(worker.os, "close", lambda fd: events.append(f"close:{fd}"))

    assert worker.main(["--result-fd", "9"]) == 0
    assert events[:2] == ["cloexec:9:False", "runtime"]
    assert events[-2:] == ["write:9:valid", "close:9"]


def test_runtime_exception_writes_no_terminal_payload_and_closes_fd(monkeypatch) -> None:
    events: list[str] = []
    monkeypatch.setattr(worker, "_request", lambda _namespace: object())
    monkeypatch.setattr(
        worker,
        "run_worker",
        lambda _request: (_ for _ in ()).throw(RuntimeError("candidate crash")),
    )
    monkeypatch.setattr(
        worker,
        "write_result_fd",
        lambda _fd, _payload: events.append("wrote"),
    )
    monkeypatch.setattr(worker.os, "set_inheritable", lambda _fd, _value: None)
    monkeypatch.setattr(worker.os, "close", lambda fd: events.append(f"close:{fd}"))

    assert worker.main(["--result-fd", "9"]) == 2
    assert events == ["close:9"]
