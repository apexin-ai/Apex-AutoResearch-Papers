"""Trusted Torch/CUDA worker for the HB-GEN-1 KernelBench meta evaluator.

The file is staged into a tiny read-only runtime bundle and executed inside the
one-GPU bubblewrap namespace.  Candidate Python is first accepted by the
task-bound restricted-language policy, then executed in a namespace containing
only the imports and builtins required by that language.  The candidate never
receives this module's result descriptor, trusted reference object, timer, input
schedule, or state seals.

The module deliberately imports Torch and Triton only inside the production
runtime constructor.  Unit tests therefore exercise the complete request/result
contract with a fake runtime without probing CUDA.
"""

from __future__ import annotations

import argparse
import builtins
import copy
import hashlib
import hmac
import importlib
import json
import math
import os
import re
import stat
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence


_RUNTIME_ROOT = Path(__file__).resolve().parents[3]
if str(_RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(_RUNTIME_ROOT))

from optimization_lab.harness_builder.adapters.kernel_candidate_invocation import (  # noqa: E402
    KERNEL_INVOCATION_SCHEDULE_SHA256,
    InvocationRuntime,
    KernelInvocationResult,
    TrustedKernelInvocationRunner,
)
from optimization_lab.harness_builder.adapters.kernel_candidate_policy import (  # noqa: E402
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
    RESTRICTED_KERNEL_TASK_IDS,
    RestrictedKernelCandidatePolicy,
)


_SHA256 = re.compile(r"[0-9a-f]{64}")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
_MAX_SOURCE_BYTES = 2 * 1024 * 1024
_MAX_RESULT_BYTES = 32 * 1024
_TOLERANCE = 1e-2

_WORKER_RESULT_KEYS = {
    "schema_version",
    "evaluator",
    "protocol_sha256",
    "scorer_sha256",
    "attempt_id",
    "result_nonce",
    "repository_commit",
    "task_id",
    "task_sha256",
    "candidate_sha256",
    "candidate_policy_sha256",
    "schedule_sha256",
    "input_schedule_sha256",
    "status",
    "health_probe",
    "compiled",
    "correct",
    "correctness_trials",
    "correctness_passed",
    "timing_trials",
    "timing_trials_completed",
    "timing_outputs_correct",
    "candidate_runtime_ms",
    "reference_runtime_ms",
    "error_summary",
    "hardware",
}


class WorkerContractError(ValueError):
    """The immutable request or candidate/result binding differs."""


@dataclass(frozen=True)
class WorkerRequest:
    repository: Path
    repository_commit: str
    task_id: str
    task_sha256: str
    candidate: Path
    candidate_sha256: str
    candidate_policy_sha256: str
    schedule_sha256: str
    protocol_sha256: str
    scorer_sha256: str
    evaluator: str
    attempt_id: str
    result_nonce: str
    input_seed_nonce: str
    result_fd: int


@dataclass(frozen=True)
class _InputBatch:
    values: tuple[Any, ...]
    commitment: str
    phase: str
    ordinal: int


@dataclass
class _CandidateHandle:
    model: Any | None


def _read_regular(path: Path, *, limit: int, label: str) -> bytes:
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise WorkerContractError(f"{label} is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise WorkerContractError(f"{label} must be a regular non-symlink file")
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise WorkerContractError(f"{label} changed type")
            raw = stream.read(limit + 1)
    except WorkerContractError:
        raise
    except OSError as exc:
        raise WorkerContractError(f"{label} is unreadable") from exc
    if not raw or len(raw) > limit:
        raise WorkerContractError(f"{label} size is invalid")
    return raw


def validate_worker_request(request: WorkerRequest) -> bytes:
    if request.task_id not in RESTRICTED_KERNEL_TASK_IDS:
        raise WorkerContractError("task is outside the frozen six-task set")
    if request.candidate_policy_sha256 != RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256:
        raise WorkerContractError("candidate policy binding differs")
    if request.schedule_sha256 != KERNEL_INVOCATION_SCHEDULE_SHA256:
        raise WorkerContractError("invocation schedule binding differs")
    for value, label in (
        (request.task_sha256, "task sha256"),
        (request.candidate_sha256, "candidate sha256"),
        (request.protocol_sha256, "protocol sha256"),
        (request.scorer_sha256, "scorer sha256"),
        (request.result_nonce, "result nonce"),
        (request.input_seed_nonce, "input seed nonce"),
    ):
        if not _SHA256.fullmatch(value):
            raise WorkerContractError(f"{label} is invalid")
    if not _COMMIT.fullmatch(request.repository_commit):
        raise WorkerContractError("repository commit is invalid")
    if not _SAFE_ID.fullmatch(request.attempt_id) or not request.evaluator:
        raise WorkerContractError("worker identity is invalid")
    if request.result_fd < 3 or request.result_fd > 1024:
        raise WorkerContractError("private result descriptor is invalid")

    task_path = request.repository / "KernelBench" / request.task_id
    task_source = _read_regular(task_path, limit=_MAX_SOURCE_BYTES, label="task source")
    if hashlib.sha256(task_source).hexdigest() != request.task_sha256:
        raise WorkerContractError("task source binding differs")
    candidate_source = _read_regular(
        request.candidate, limit=_MAX_SOURCE_BYTES, label="candidate source"
    )
    if hashlib.sha256(candidate_source).hexdigest() != request.candidate_sha256:
        raise WorkerContractError("candidate source binding differs")
    RestrictedKernelCandidatePolicy().validate(
        candidate_source, task_id=request.task_id
    )
    return candidate_source


def _seed_for(secret_nonce: str, task_id: str, phase: str, ordinal: int) -> int:
    if not _SHA256.fullmatch(secret_nonce):
        raise WorkerContractError("input seed nonce is invalid")
    message = (
        f"HB-GEN-1-KERNELBENCH-SEED-V1\0{task_id}\0{phase}\0{ordinal}"
    ).encode("utf-8")
    digest = hmac.new(bytes.fromhex(secret_nonce), message, hashlib.sha256).digest()
    return int.from_bytes(digest[:4], "big")


def _safe_builtins(importer: Callable[..., Any]) -> Mapping[str, object]:
    return {
        "__build_class__": builtins.__build_class__,
        "__import__": importer,
        "abs": abs,
        "float": float,
        "int": int,
        "len": len,
        "max": max,
        "min": min,
        "object": object,
        "range": range,
        "super": super,
        "tuple": tuple,
    }


class TorchCudaInvocationRuntime(InvocationRuntime):
    """Concrete task-bound runtime used only inside the GPU namespace."""

    def __init__(self, request: WorkerRequest) -> None:
        self.request = request
        self.torch = importlib.import_module("torch")
        self.nn = importlib.import_module("torch.nn")
        self.functional = importlib.import_module("torch.nn.functional")
        self.triton = importlib.import_module("triton")
        self.tl = importlib.import_module("triton.language")
        self.math = importlib.import_module("math")
        self._trusted_import = builtins.__import__
        self._compile = builtins.compile
        self._exec = builtins.exec
        self._perf_counter_ns = time.perf_counter_ns
        self._candidate_handle: _CandidateHandle | None = None

        hardware = self._probe_cuda()
        self.hardware = hardware
        task_path = request.repository / "KernelBench" / request.task_id
        task_source = _read_regular(task_path, limit=_MAX_SOURCE_BYTES, label="task source")
        task_namespace: dict[str, Any] = {
            "__builtins__": builtins.__dict__,
            "__name__": "hb_gen1_frozen_task",
        }
        self._exec(
            self._compile(task_source, str(task_path), "exec"),
            task_namespace,
            task_namespace,
        )
        try:
            self._reference_type = task_namespace["Model"]
            self._get_inputs = task_namespace["get_inputs"]
            self._get_init_inputs = task_namespace["get_init_inputs"]
        except KeyError as exc:
            raise WorkerContractError("frozen task ABI is incomplete") from exc
        if not all(
            callable(value)
            for value in (
                self._reference_type,
                self._get_inputs,
                self._get_init_inputs,
            )
        ):
            raise WorkerContractError("frozen task ABI is not callable")

        init_seed = _seed_for(request.input_seed_nonce, request.task_id, "weights", 0)
        self._set_seed(init_seed)
        self._init_inputs = tuple(self._get_init_inputs())
        self._set_seed(init_seed)
        with self.torch.no_grad():
            self._reference_model = self._reference_type(*self._init_inputs)
            self.nn.Module.to(
                self._reference_model, device=self.torch.device("cuda:0"), dtype=self.torch.float32
            )
        self._reference_state = tuple(
            (name, value.detach().cpu().clone())
            for name, value in self._reference_model.state_dict().items()
        )

    def _probe_cuda(self) -> str:
        torch = self.torch
        if not torch.cuda.is_available() or torch.cuda.device_count() != 1:
            raise WorkerContractError("worker must see exactly one CUDA device")
        torch.cuda.set_device(0)
        hardware = " ".join(torch.cuda.get_device_name(0).split())[:256]
        if "A100" not in hardware:
            raise WorkerContractError("worker GPU is not the frozen A100 class")
        with torch.no_grad():
            sentinel = torch.ones((1,), device="cuda:0", dtype=torch.float32)
            if float((sentinel + 1).item()) != 2.0:
                raise WorkerContractError("CUDA health sentinel differs")
        torch.cuda.synchronize(0)
        return hardware

    def _set_seed(self, seed: int) -> None:
        self.torch.manual_seed(seed)
        self.torch.cuda.manual_seed_all(seed)

    def _to_device(self, value: Any) -> Any:
        if isinstance(value, self.torch.Tensor):
            return value.to(device="cuda:0", dtype=self.torch.float32)
        return copy.deepcopy(value)

    def _clone_value(self, value: Any) -> Any:
        if isinstance(value, self.torch.Tensor):
            return value.detach().clone()
        if isinstance(value, tuple):
            return tuple(self._clone_value(item) for item in value)
        if isinstance(value, list):
            return [self._clone_value(item) for item in value]
        return copy.deepcopy(value)

    def _seal_output(self, value: Any) -> Any:
        # GPU clones keep the 6+ GiB Sigmoid output off host memory while
        # removing all aliases known to the candidate.  Full reference state is
        # separately compared against CPU seals after every candidate call.
        return self._clone_value(value)

    def _values_equal(self, left: Any, right: Any) -> bool:
        if isinstance(left, self.torch.Tensor) and isinstance(right, self.torch.Tensor):
            return bool(self.torch.equal(left, right))
        if isinstance(left, (tuple, list)) and isinstance(right, (tuple, list)):
            return len(left) == len(right) and all(
                self._values_equal(a, b) for a, b in zip(left, right)
            )
        return type(left) is type(right) and left == right

    def _outputs_close(self, expected: Any, actual: Any) -> bool:
        if isinstance(expected, self.torch.Tensor) and isinstance(actual, self.torch.Tensor):
            return expected.shape == actual.shape and bool(
                self.torch.allclose(
                    expected, actual, atol=_TOLERANCE, rtol=_TOLERANCE
                )
            )
        if isinstance(expected, (tuple, list)) and isinstance(actual, (tuple, list)):
            return len(expected) == len(actual) and all(
                self._outputs_close(a, b) for a, b in zip(expected, actual)
            )
        return False

    def _trusted_state_unchanged(self) -> bool:
        current = self._reference_model.state_dict()
        if tuple(current) != tuple(name for name, _ in self._reference_state):
            return False
        for name, sealed in self._reference_state:
            value = current[name]
            if value.shape != sealed.shape or value.dtype != sealed.dtype:
                return False
            if not self.torch.equal(value.detach().cpu(), sealed):
                return False
        return True

    def capture_trusted_primitives(self) -> Mapping[str, Callable[..., Any]]:
        torch = self.torch
        synchronize = torch.cuda.synchronize
        reference_model = self._reference_model
        monotonic_ns = self._perf_counter_ns
        clone = self._clone_value

        def clone_inputs(batch: _InputBatch) -> _InputBatch:
            return _InputBatch(
                tuple(clone(value) for value in batch.values),
                batch.commitment,
                batch.phase,
                batch.ordinal,
            )

        def reference(batch: _InputBatch) -> Any:
            with torch.no_grad():
                return reference_model(*batch.values)

        return {
            "monotonic_ns": monotonic_ns,
            "synchronize": lambda: synchronize(0),
            "clone_inputs": clone_inputs,
            "reference": reference,
            "outputs_close": self._outputs_close,
            "inputs_unchanged": lambda before, after: self._values_equal(
                before.values, after.values
            ),
            "input_commitment": lambda batch: batch.commitment,
            "seal_output": self._seal_output,
            "trusted_state_unchanged": self._trusted_state_unchanged,
        }

    def _candidate_import(
        self,
        name: str,
        globals_: Mapping[str, object] | None = None,
        locals_: Mapping[str, object] | None = None,
        fromlist: Sequence[str] = (),
        level: int = 0,
    ) -> Any:
        del globals_, locals_
        if level != 0 or name not in {
            "math",
            "torch",
            "torch.nn",
            "torch.nn.functional",
            "triton",
            "triton.language",
        }:
            raise ImportError("candidate import is outside the restricted runtime")
        return self._trusted_import(name, {}, {}, fromlist, 0)

    def load_candidate(self, source: bytes, policy_sha256: str) -> _CandidateHandle:
        if policy_sha256 != RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256:
            raise WorkerContractError("candidate policy binding differs at load")
        RestrictedKernelCandidatePolicy().validate(source, task_id=self.request.task_id)
        namespace: dict[str, Any] = {
            "__builtins__": _safe_builtins(self._candidate_import),
            "__name__": "hb_gen1_restricted_candidate",
        }
        self._exec(
            self._compile(source, "/sandbox/input/candidate.py", "exec"),
            namespace,
            namespace,
        )
        model_type = namespace.get("ModelNew")
        if not isinstance(model_type, type) or not issubclass(model_type, self.nn.Module):
            raise WorkerContractError("candidate ModelNew type differs")
        self._set_seed(
            _seed_for(
                self.request.input_seed_nonce,
                self.request.task_id,
                "weights",
                0,
            )
        )
        with self.torch.no_grad():
            model = model_type(*self._init_inputs)
            self.nn.Module.to(
                model, device=self.torch.device("cuda:0"), dtype=self.torch.float32
            )
        handle = _CandidateHandle(model=model)
        self._candidate_handle = handle
        return handle

    def fresh_inputs(self, *, phase: str, ordinal: int) -> _InputBatch:
        seed = _seed_for(
            self.request.input_seed_nonce,
            self.request.task_id,
            phase,
            ordinal,
        )
        self._set_seed(seed)
        with self.torch.no_grad():
            values = tuple(self._to_device(item) for item in self._get_inputs())
        metadata = []
        for value in values:
            if isinstance(value, self.torch.Tensor):
                metadata.append(
                    {
                        "shape": list(value.shape),
                        "dtype": str(value.dtype),
                        "device": "cuda:0",
                    }
                )
            else:
                metadata.append({"type": type(value).__name__, "repr": repr(value)[:128]})
        commitment = hashlib.sha256(
            json.dumps(
                {
                    "task_id": self.request.task_id,
                    "phase": phase,
                    "ordinal": ordinal,
                    "seed": seed,
                    "metadata": metadata,
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        return _InputBatch(values, commitment, phase, ordinal)

    def invoke_candidate(self, handle: _CandidateHandle, inputs: _InputBatch) -> Any:
        if handle is not self._candidate_handle or handle.model is None:
            raise WorkerContractError("candidate handle is not live")
        with self.torch.no_grad():
            return handle.model(*inputs.values)

    def close_candidate(self, handle: _CandidateHandle) -> None:
        if handle is self._candidate_handle:
            handle.model = None
            self._candidate_handle = None
        self.torch.cuda.synchronize(0)
        self.torch.cuda.empty_cache()

    def assert_quiescent(self) -> None:
        # The outer supervisor additionally kills/proves disappearance of the
        # complete bubblewrap process group.  This inner gate proves all work in
        # this CUDA context completed before evidence is serialized.
        self.torch.cuda.synchronize(0)


def health_probe() -> Mapping[str, object]:
    """Run the independent namespace health sentinel without candidate bytes."""

    torch = importlib.import_module("torch")
    if not torch.cuda.is_available() or torch.cuda.device_count() != 1:
        raise WorkerContractError("health worker must see exactly one CUDA device")
    torch.cuda.set_device(0)
    hardware = " ".join(torch.cuda.get_device_name(0).split())[:256]
    if "A100" not in hardware:
        raise WorkerContractError("health worker GPU is not A100")
    with torch.no_grad():
        value = torch.arange(4, device="cuda:0", dtype=torch.float32).sum().item()
    torch.cuda.synchronize(0)
    if float(value) != 6.0:
        raise WorkerContractError("health worker CUDA sentinel differs")
    return {"schema_version": 1, "status": "passed", "hardware": hardware}


def worker_result_payload(
    request: WorkerRequest,
    result: KernelInvocationResult,
    *,
    hardware: str,
) -> dict[str, object]:
    payload: dict[str, object] = {
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
        "candidate_policy_sha256": result.candidate_policy_sha256,
        "schedule_sha256": result.schedule_sha256,
        "input_schedule_sha256": result.input_schedule_sha256,
        "status": result.status,
        "health_probe": "passed",
        "compiled": result.compiled,
        "correct": result.correct,
        "correctness_trials": result.correctness_trials,
        "correctness_passed": result.correctness_passed,
        "timing_trials": result.timing_trials,
        "timing_trials_completed": result.timing_trials_completed,
        "timing_outputs_correct": result.timing_outputs_correct,
        "candidate_runtime_ms": result.candidate_runtime_ms,
        "reference_runtime_ms": result.reference_runtime_ms,
        "error_summary": result.error_summary,
        "hardware": " ".join(hardware.split())[:256],
    }
    if set(payload) != _WORKER_RESULT_KEYS:
        raise AssertionError("worker result schema drift")
    return payload


RuntimeFactory = Callable[[WorkerRequest], InvocationRuntime]


def run_worker(
    request: WorkerRequest,
    *,
    runtime_factory: RuntimeFactory = TorchCudaInvocationRuntime,
) -> dict[str, object]:
    source = validate_worker_request(request)
    runtime = runtime_factory(request)
    result = TrustedKernelInvocationRunner(
        runtime=runtime,
        task_id=request.task_id,
    ).run(source)
    hardware = getattr(runtime, "hardware", "")
    return worker_result_payload(request, result, hardware=hardware)


def write_result_fd(fd: int, payload: Mapping[str, object]) -> None:
    if fd < 3 or fd > 1024:
        raise WorkerContractError("private result descriptor is invalid")
    encoded = json.dumps(
        payload,
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    if len(encoded) > _MAX_RESULT_BYTES:
        raise WorkerContractError("private worker evidence is too large")
    view = memoryview(encoded)
    while view:
        written = os.write(fd, view)
        if written <= 0:
            raise WorkerContractError("private result descriptor did not advance")
        view = view[written:]
    os.close(fd)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--health-only", action="store_true")
    parser.add_argument("--repository", type=Path)
    parser.add_argument("--repository-commit")
    parser.add_argument("--task-id")
    parser.add_argument("--task-sha256")
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--candidate-sha256")
    parser.add_argument("--candidate-policy-sha256")
    parser.add_argument("--schedule-sha256")
    parser.add_argument("--protocol-sha256")
    parser.add_argument("--scorer-sha256")
    parser.add_argument("--evaluator")
    parser.add_argument("--attempt-id")
    parser.add_argument("--result-nonce")
    parser.add_argument("--input-seed-nonce")
    parser.add_argument("--result-fd", type=int, required=True)
    return parser


def _request(namespace: argparse.Namespace) -> WorkerRequest:
    required = {
        "repository": namespace.repository,
        "repository_commit": namespace.repository_commit,
        "task_id": namespace.task_id,
        "task_sha256": namespace.task_sha256,
        "candidate": namespace.candidate,
        "candidate_sha256": namespace.candidate_sha256,
        "candidate_policy_sha256": namespace.candidate_policy_sha256,
        "schedule_sha256": namespace.schedule_sha256,
        "protocol_sha256": namespace.protocol_sha256,
        "scorer_sha256": namespace.scorer_sha256,
        "evaluator": namespace.evaluator,
        "attempt_id": namespace.attempt_id,
        "result_nonce": namespace.result_nonce,
        "input_seed_nonce": namespace.input_seed_nonce,
    }
    if any(value is None for value in required.values()):
        raise WorkerContractError("candidate worker arguments are incomplete")
    return WorkerRequest(result_fd=namespace.result_fd, **required)  # type: ignore[arg-type]


def main(argv: Sequence[str] | None = None) -> int:
    namespace = _parser().parse_args(argv)
    result_fd = namespace.result_fd
    try:
        # bubblewrap must inherit fd 3, but no compiler/helper process spawned
        # while importing Triton or executing a candidate may inherit it.
        os.set_inheritable(result_fd, False)
        if namespace.health_only:
            payload = health_probe()
        else:
            payload = run_worker(_request(namespace))
        write_result_fd(result_fd, payload)
        result_fd = -1
    except Exception:
        # stdout/stderr are audit-only.  Raw candidate/runtime errors never
        # become a control channel and never reveal trusted bindings.
        return 2
    finally:
        if result_fd >= 3:
            try:
                os.close(result_fd)
            except OSError:
                pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "TorchCudaInvocationRuntime",
    "WorkerContractError",
    "WorkerRequest",
    "health_probe",
    "run_worker",
    "validate_worker_request",
    "worker_result_payload",
    "write_result_fd",
]
