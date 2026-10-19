"""Trusted correctness-bound timing loop for CandidateInvocationABI-v1.

The loop owns protocol state and accepts only a narrow injected runtime.  The
production runtime must place the candidate in its isolated process/GPU context;
offline tests use a fake runtime to prove ordering, per-trial correctness and
quiescence semantics without importing Torch or touching a GPU.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from typing import Any, Callable, Mapping, Protocol

from .kernel_candidate_policy import (
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
    RestrictedKernelCandidateError,
    RestrictedKernelCandidatePolicy,
)


_SHA256 = re.compile(r"[0-9a-f]{64}")
_PRIMITIVE_KEYS = {
    "clone_inputs",
    "input_commitment",
    "inputs_unchanged",
    "monotonic_ns",
    "outputs_close",
    "reference",
    "seal_output",
    "synchronize",
    "trusted_state_unchanged",
}
_SCHEDULE = tuple("reference_first" if index % 2 == 0 else "candidate_first" for index in range(100))
KERNEL_INVOCATION_SCHEDULE_SHA256 = hashlib.sha256(
    json.dumps(_SCHEDULE, separators=(",", ":")).encode()
).hexdigest()


class InvocationRuntime(Protocol):
    """Minimal capability surface held by the trusted invocation loop."""

    def capture_trusted_primitives(self) -> Mapping[str, Callable[..., Any]]: ...

    def load_candidate(self, source: bytes, policy_sha256: str) -> Any: ...

    def fresh_inputs(self, *, phase: str, ordinal: int) -> Any: ...

    def invoke_candidate(self, handle: Any, inputs: Any) -> Any: ...

    def close_candidate(self, handle: Any) -> None: ...

    def assert_quiescent(self) -> None: ...


@dataclass(frozen=True)
class KernelInvocationResult:
    status: str
    compiled: bool
    correct: bool
    correctness_trials: int
    correctness_passed: int
    timing_trials: int
    timing_trials_completed: int
    timing_outputs_correct: int
    candidate_runtime_ms: float | None
    reference_runtime_ms: float | None
    error_summary: str
    candidate_policy_sha256: str
    schedule_sha256: str
    input_schedule_sha256: str | None

    def __post_init__(self) -> None:
        if self.correctness_trials != 5 or self.timing_trials != 100:
            raise ValueError("CandidateInvocationABI protocol counts differ")
        if not 0 <= self.correctness_passed <= 5:
            raise ValueError("invalid correctness count")
        if not 0 <= self.timing_outputs_correct <= self.timing_trials_completed <= 100:
            raise ValueError("invalid timing counts")
        if self.correct:
            if (
                self.status != "valid"
                or not self.compiled
                or self.correctness_passed != 5
                or self.timing_trials_completed != 100
                or self.timing_outputs_correct != 100
                or self.candidate_runtime_ms is None
                or self.reference_runtime_ms is None
                or self.input_schedule_sha256 is None
            ):
                raise ValueError("valid invocation result is incomplete")
        elif self.candidate_runtime_ms is not None or self.reference_runtime_ms is not None:
            raise ValueError("failed invocation cannot expose timing")
        if self.candidate_policy_sha256 != RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256:
            raise ValueError("candidate policy hash differs")
        if self.schedule_sha256 != KERNEL_INVOCATION_SCHEDULE_SHA256:
            raise ValueError("timing schedule hash differs")
        if self.input_schedule_sha256 is not None and not _SHA256.fullmatch(
            self.input_schedule_sha256
        ):
            raise ValueError("input schedule hash is invalid")


def _failure(
    status: str,
    summary: str,
    *,
    compiled: bool = False,
    correctness_passed: int = 0,
    timing_completed: int = 0,
    timing_correct: int = 0,
    input_schedule_sha256: str | None = None,
) -> KernelInvocationResult:
    return KernelInvocationResult(
        status=status,
        compiled=compiled,
        correct=False,
        correctness_trials=5,
        correctness_passed=correctness_passed,
        timing_trials=100,
        timing_trials_completed=timing_completed,
        timing_outputs_correct=timing_correct,
        candidate_runtime_ms=None,
        reference_runtime_ms=None,
        error_summary=" ".join(summary.split())[:500],
        candidate_policy_sha256=RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
        schedule_sha256=KERNEL_INVOCATION_SCHEDULE_SHA256,
        input_schedule_sha256=input_schedule_sha256,
    )


class TrustedKernelInvocationRunner:
    """Run compile -> 5 correctness -> 100 correctness-bound timings.

    Trusted callables are captured before ``load_candidate``.  Every invocation
    receives a distinct committed input.  A candidate timing is produced only
    after its same-trial output and input immutability pass, and no result is
    returned before candidate teardown plus process/GPU quiescence succeeds.
    """

    def __init__(
        self,
        *,
        runtime: InvocationRuntime,
        task_id: str,
        policy: RestrictedKernelCandidatePolicy | None = None,
    ) -> None:
        self.runtime = runtime
        self.task_id = task_id
        self.policy = policy or RestrictedKernelCandidatePolicy()

    def run(self, source: bytes) -> KernelInvocationResult:
        try:
            policy_report = self.policy.validate(source, task_id=self.task_id)
        except RestrictedKernelCandidateError as exc:
            return _failure("policy_rejected", str(exc))
        try:
            primitives = dict(self.runtime.capture_trusted_primitives())
        except Exception:
            return _failure("environment_invalid", "trusted primitives are unavailable")
        if set(primitives) != _PRIMITIVE_KEYS or not all(
            callable(item) for item in primitives.values()
        ):
            return _failure("environment_invalid", "trusted primitive surface differs")

        commitments: list[str] = []
        handle: Any | None = None
        result: KernelInvocationResult | None = None
        candidate_times: list[float] = []
        reference_times: list[float] = []

        def schedule_sha() -> str | None:
            if not commitments:
                return None
            return hashlib.sha256(
                json.dumps(commitments, separators=(",", ":")).encode()
            ).hexdigest()

        def fresh(phase: str, ordinal: int) -> Any:
            inputs = self.runtime.fresh_inputs(phase=phase, ordinal=ordinal)
            commitment = primitives["input_commitment"](inputs)
            if not isinstance(commitment, str) or not _SHA256.fullmatch(commitment):
                raise RuntimeError("trusted input commitment is invalid")
            if commitment in commitments:
                raise RuntimeError("fresh input commitment was reused")
            commitments.append(commitment)
            return inputs

        def measured(callable_: Callable[[], Any]) -> tuple[Any, float]:
            primitives["synchronize"]()
            started = primitives["monotonic_ns"]()
            output = callable_()
            primitives["synchronize"]()
            stopped = primitives["monotonic_ns"]()
            if type(started) is not int or type(stopped) is not int or stopped <= started:
                raise RuntimeError("trusted monotonic timer is invalid")
            milliseconds = (stopped - started) / 1_000_000.0
            if not math.isfinite(milliseconds) or milliseconds <= 0:
                raise RuntimeError("trusted timing is invalid")
            return output, milliseconds

        try:
            handle = self.runtime.load_candidate(source, policy_report.policy_sha256)
            compile_inputs = fresh("compile", 0)
            self.runtime.invoke_candidate(handle, compile_inputs)
            primitives["synchronize"]()
        except Exception:
            result = _failure(
                "compile_failed",
                "candidate failed during isolated compile invocation",
                input_schedule_sha256=schedule_sha(),
            )

        if result is None:
            for ordinal in range(5):
                try:
                    inputs = fresh("correctness", ordinal)
                    reference_inputs = primitives["clone_inputs"](inputs)
                    candidate_inputs = primitives["clone_inputs"](inputs)
                    before = primitives["clone_inputs"](candidate_inputs)
                    expected = primitives["seal_output"](
                        primitives["reference"](reference_inputs)
                    )
                    actual = self.runtime.invoke_candidate(handle, candidate_inputs)
                    primitives["synchronize"]()
                    actual = primitives["seal_output"](actual)
                    if not primitives["trusted_state_unchanged"]():
                        result = _failure(
                            "incorrect",
                            "candidate modified trusted reference state",
                            compiled=True,
                            correctness_passed=ordinal,
                            input_schedule_sha256=schedule_sha(),
                        )
                        break
                    if not primitives["inputs_unchanged"](before, candidate_inputs):
                        result = _failure(
                            "incorrect",
                            "candidate mutated a correctness input",
                            compiled=True,
                            correctness_passed=ordinal,
                            input_schedule_sha256=schedule_sha(),
                        )
                        break
                    if not primitives["outputs_close"](expected, actual):
                        result = _failure(
                            "incorrect",
                            "candidate correctness output differs",
                            compiled=True,
                            correctness_passed=ordinal,
                            input_schedule_sha256=schedule_sha(),
                        )
                        break
                except Exception:
                    result = _failure(
                        "incorrect",
                        "candidate correctness invocation failed",
                        compiled=True,
                        correctness_passed=ordinal,
                        input_schedule_sha256=schedule_sha(),
                    )
                    break

        if result is None:
            for ordinal, order in enumerate(_SCHEDULE):
                try:
                    inputs = fresh("timing", ordinal)
                    reference_inputs = primitives["clone_inputs"](inputs)
                    candidate_inputs = primitives["clone_inputs"](inputs)
                    before = primitives["clone_inputs"](candidate_inputs)

                    def run_reference() -> Any:
                        return primitives["reference"](reference_inputs)

                    def run_candidate() -> Any:
                        return self.runtime.invoke_candidate(handle, candidate_inputs)

                    if order == "reference_first":
                        expected, reference_ms = measured(run_reference)
                        expected = primitives["seal_output"](expected)
                        actual, candidate_ms = measured(run_candidate)
                        actual = primitives["seal_output"](actual)
                    else:
                        actual, candidate_ms = measured(run_candidate)
                        actual = primitives["seal_output"](actual)
                        expected, reference_ms = measured(run_reference)
                        expected = primitives["seal_output"](expected)
                    if not primitives["trusted_state_unchanged"]():
                        result = _failure(
                            "incorrect",
                            "candidate modified trusted reference state",
                            compiled=True,
                            correctness_passed=5,
                            timing_completed=ordinal + 1,
                            timing_correct=ordinal,
                            input_schedule_sha256=schedule_sha(),
                        )
                        break
                    if not primitives["inputs_unchanged"](before, candidate_inputs):
                        result = _failure(
                            "incorrect",
                            "candidate mutated a measured input",
                            compiled=True,
                            correctness_passed=5,
                            timing_completed=ordinal + 1,
                            timing_correct=ordinal,
                            input_schedule_sha256=schedule_sha(),
                        )
                        break
                    if not primitives["outputs_close"](expected, actual):
                        result = _failure(
                            "incorrect",
                            "candidate measured output differs",
                            compiled=True,
                            correctness_passed=5,
                            timing_completed=ordinal + 1,
                            timing_correct=ordinal,
                            input_schedule_sha256=schedule_sha(),
                        )
                        break
                    candidate_times.append(candidate_ms)
                    reference_times.append(reference_ms)
                except Exception:
                    result = _failure(
                        "incorrect",
                        "candidate measured invocation failed",
                        compiled=True,
                        correctness_passed=5,
                        timing_completed=ordinal + 1,
                        timing_correct=ordinal,
                        input_schedule_sha256=schedule_sha(),
                    )
                    break

        if result is None:
            result = KernelInvocationResult(
                status="valid",
                compiled=True,
                correct=True,
                correctness_trials=5,
                correctness_passed=5,
                timing_trials=100,
                timing_trials_completed=100,
                timing_outputs_correct=100,
                candidate_runtime_ms=sum(candidate_times) / 100,
                reference_runtime_ms=sum(reference_times) / 100,
                error_summary="",
                candidate_policy_sha256=policy_report.policy_sha256,
                schedule_sha256=KERNEL_INVOCATION_SCHEDULE_SHA256,
                input_schedule_sha256=schedule_sha(),
            )

        try:
            if handle is not None:
                self.runtime.close_candidate(handle)
            self.runtime.assert_quiescent()
        except Exception:
            result = _failure(
                "environment_invalid",
                "candidate process group or GPU context is not quiescent",
                input_schedule_sha256=schedule_sha(),
            )
        return result


__all__ = [
    "InvocationRuntime",
    "KERNEL_INVOCATION_SCHEDULE_SHA256",
    "KernelInvocationResult",
    "TrustedKernelInvocationRunner",
]
