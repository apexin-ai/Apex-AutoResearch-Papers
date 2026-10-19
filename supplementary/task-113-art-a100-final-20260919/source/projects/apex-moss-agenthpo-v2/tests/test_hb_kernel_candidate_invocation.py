from __future__ import annotations

import hashlib
from dataclasses import dataclass

import pytest

from optimization_lab.harness_builder.adapters.kernel_candidate_invocation import (
    InvocationRuntime,
    TrustedKernelInvocationRunner,
)
from optimization_lab.harness_builder.adapters.kernel_candidate_policy import (
    RestrictedKernelCandidatePolicy,
)


SOURCE = """import torch
import torch.nn as nn

class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid(x)
"""
TASK_ID = "level1/21_Sigmoid.py"


@dataclass
class FakeHandle:
    calls: int = 0


class FakeRuntime(InvocationRuntime):
    def __init__(
        self,
        *,
        wrong_after: int | None = None,
        quiescent: bool = True,
        trusted_state: bool = True,
    ):
        self.events: list[str] = []
        self.inputs: list[int] = []
        self.wrong_after = wrong_after
        self.quiescent = quiescent
        self.trusted_state = trusted_state
        self.clock = 0

    def capture_trusted_primitives(self):
        self.events.append("captured")

        def monotonic_ns() -> int:
            self.clock += 1_000_000
            return self.clock

        return {
            "monotonic_ns": monotonic_ns,
            "synchronize": lambda: self.events.append("synchronize"),
            "clone_inputs": lambda value: tuple(value),
            "reference": lambda value: value[0] + 1,
            "outputs_close": lambda expected, actual: expected == actual,
            "inputs_unchanged": lambda before, after: before == after,
            "input_commitment": lambda value: hashlib.sha256(
                str(tuple(value)).encode()
            ).hexdigest(),
            "seal_output": lambda value: value,
            "trusted_state_unchanged": lambda: self.trusted_state,
        }

    def load_candidate(self, source: bytes, policy_sha256: str) -> FakeHandle:
        assert source == SOURCE.encode()
        assert policy_sha256 == RestrictedKernelCandidatePolicy().policy_sha256
        assert self.events[0] == "captured"
        self.events.append("loaded")
        return FakeHandle()

    def fresh_inputs(self, *, phase: str, ordinal: int) -> tuple[int]:
        value = len(self.inputs) + 10
        self.inputs.append(value)
        self.events.append(f"input:{phase}:{ordinal}:{value}")
        return (value,)

    def invoke_candidate(self, handle: FakeHandle, inputs: tuple[int]):
        handle.calls += 1
        if self.wrong_after is not None and handle.calls > self.wrong_after:
            return -1
        return inputs[0] + 1

    def close_candidate(self, handle: FakeHandle) -> None:
        self.events.append("closed")

    def assert_quiescent(self) -> None:
        self.events.append("quiescence_checked")
        if not self.quiescent:
            raise RuntimeError("candidate process group or GPU context remains active")


def test_trusted_runner_captures_primitives_before_import_and_checks_all_timings() -> None:
    runtime = FakeRuntime()
    result = TrustedKernelInvocationRunner(runtime=runtime, task_id=TASK_ID).run(
        SOURCE.encode()
    )

    assert result.status == "valid"
    assert result.compiled is True
    assert result.correct is True
    assert result.correctness_passed == 5
    assert result.timing_trials_completed == 100
    assert result.timing_outputs_correct == 100
    assert result.candidate_runtime_ms == pytest.approx(1.0)
    assert result.reference_runtime_ms == pytest.approx(1.0)
    assert len(runtime.inputs) == 106  # one compile, five correctness, one hundred timed
    assert len(set(runtime.inputs)) == 106
    assert runtime.events.index("captured") < runtime.events.index("loaded")
    assert runtime.events[-2:] == ["closed", "quiescence_checked"]


def test_first_five_correct_then_fast_wrong_is_caught_during_timing() -> None:
    # One compile + five correctness calls pass.  The first measured output is
    # deliberately wrong even though its fake timing is otherwise fast.
    runtime = FakeRuntime(wrong_after=6)
    result = TrustedKernelInvocationRunner(runtime=runtime, task_id=TASK_ID).run(
        SOURCE.encode()
    )

    assert result.status == "incorrect"
    assert result.compiled is True
    assert result.correct is False
    assert result.correctness_passed == 5
    assert result.timing_trials_completed == 1
    assert result.timing_outputs_correct == 0
    assert result.candidate_runtime_ms is None
    assert result.reference_runtime_ms is None
    assert runtime.events[-2:] == ["closed", "quiescence_checked"]


def test_input_mutation_is_a_candidate_failure() -> None:
    runtime = FakeRuntime()
    primitives = runtime.capture_trusted_primitives()
    primitives["inputs_unchanged"] = lambda before, after: False
    runtime.capture_trusted_primitives = lambda: primitives  # type: ignore[method-assign]

    result = TrustedKernelInvocationRunner(runtime=runtime, task_id=TASK_ID).run(
        SOURCE.encode()
    )

    assert result.status == "incorrect"
    assert result.correct is False
    assert "mutated" in result.error_summary


def test_result_is_withheld_until_process_group_and_gpu_context_are_quiescent() -> None:
    result = TrustedKernelInvocationRunner(
        runtime=FakeRuntime(quiescent=False), task_id=TASK_ID
    ).run(SOURCE.encode())

    assert result.status == "environment_invalid"
    assert result.correct is False
    assert result.candidate_runtime_ms is None
    assert "quiescent" in result.error_summary


def test_reference_state_tamper_is_a_candidate_failure() -> None:
    result = TrustedKernelInvocationRunner(
        runtime=FakeRuntime(trusted_state=False), task_id=TASK_ID
    ).run(SOURCE.encode())

    assert result.status == "incorrect"
    assert result.correct is False
    assert "trusted reference state" in result.error_summary
