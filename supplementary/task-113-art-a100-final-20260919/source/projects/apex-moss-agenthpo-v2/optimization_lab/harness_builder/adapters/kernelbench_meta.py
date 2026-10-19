from __future__ import annotations

import hashlib
import json
import math
import os
import re
import secrets
import stat
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Callable, Mapping

from optimization_lab.adapters.base import EvaluationResult, EvaluationStatus
from optimization_lab.task_spec import TaskSpec

from .kernel_candidate_invocation import KERNEL_INVOCATION_SCHEDULE_SHA256
from .kernel_candidate_policy import (
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
    RestrictedKernelCandidateError,
    RestrictedKernelCandidatePolicy,
)
from .kernelbench_meta_isolation import kernelbench_meta_scorer_bundle_sha256


KERNELBENCH_META_REPOSITORY_COMMIT = (
    "423217d9fda91e0c2d67e4a43bf62f96f6d104f1"
)
KERNELBENCH_META_EVALUATOR_ID = "hb-gen1-kernelbench-candidate-invocation-abi-v1"
KERNELBENCH_META_TIMEOUT_SECONDS = 600.0
KERNELBENCH_META_TRUSTED_INVOCATION_LOOP_IMPLEMENTED = True
KERNELBENCH_META_PRODUCTION_RUNTIME_IMPLEMENTED = True
# The restricted Torch/CUDA backend is implemented and CPU/fake-red-teamed, but
# formal scoring remains disabled until its independent ten-seat GPU canary is
# granted and passes on the exact frozen revision.
KERNELBENCH_META_PRODUCTION_READY = False
KERNELBENCH_META_PRODUCTION_BLOCKER = "kernelbench_meta_canary_pending"
KERNELBENCH_META_TASK_HASHES: Mapping[str, str] = MappingProxyType(
    {
        "level1/21_Sigmoid.py": (
            "8f3ae78284ddd70b5c2fff66e066e967780245dee262fbf8cd2432498833796a"
        ),
        "level1/92_cumsum_exclusive.py": (
            "ec1551c196130f5d7fae707f0750016c35b988e76aa3f1657da4347f463ced86"
        ),
        "level1/97_ScaledDotProductAttention.py": (
            "a07ca5135657c2ea29f7b7a66ec1815560858ad69fa88221bfc0f82bd5648091"
        ),
        "level2/45_Gemm_Sigmoid_LogSumExp.py": (
            "c206fcec5ac6b6253fb2f86992a865ea2f560fe54ebfd7a7bf542fc9852cd2c4"
        ),
        "level2/57_Conv2d_ReLU_HardSwish.py": (
            "6c3068e8639d0fce90e78d72027434237594eafe9e1c0919b56c30edeae9ff88"
        ),
        "level2/67_Conv2d_GELU_GlobalAvgPool.py": (
            "3a9572034d80dd060bb523e1d265aa941113a8044ecd30c614e764fdf029d94a"
        ),
    }
)
KERNELBENCH_META_CANARY_TASKS: Mapping[str, str] = MappingProxyType(
    {
        # Static rejections and early incorrect exits run before expensive
        # positive references.  The largest 6+ GiB Sigmoid case is last, so an
        # earlier contract failure cannot waste its full canary reservation.
        "adversarial-fake-stdout": "level1/21_Sigmoid.py",
        "adversarial-private-overwrite": "level1/21_Sigmoid.py",
        "adversarial-wrong": "level1/21_Sigmoid.py",
        "adversarial-first5-timing-wrong": "level1/21_Sigmoid.py",
        "reference-gemm-sigmoid-logsumexp": "level2/45_Gemm_Sigmoid_LogSumExp.py",
        "reference-conv-relu-hardswish": "level2/57_Conv2d_ReLU_HardSwish.py",
        "reference-conv-gelu-gap": "level2/67_Conv2d_GELU_GlobalAvgPool.py",
        "reference-sdpa": "level1/97_ScaledDotProductAttention.py",
        "reference-cumsum": "level1/92_cumsum_exclusive.py",
        "reference-sigmoid": "level1/21_Sigmoid.py",
    }
)
KERNELBENCH_META_TASK_SET_SHA256 = hashlib.sha256(
    json.dumps(
        dict(KERNELBENCH_META_TASK_HASHES),
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
).hexdigest()

_PROTOCOL = {
    "candidate_policy_sha256": RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
    "candidate_result_channel": "anonymous_inherited_fd3_cloexec_before_candidate",
    "compile_attempts": 1,
    "correctness_trials": 5,
    "evaluator": KERNELBENCH_META_EVALUATOR_ID,
    "environment_health": "out_of_band",
    "private_result": "nonce_hash_bound_json",
    "seed_schedule": "private_result_nonce_hmac_domain_separated",
    "timer": "captured_host_monotonic_ns_with_cuda_synchronize",
    "timing_outputs_correctness_bound": True,
    "timing_trials": 100,
    "timing_schedule_sha256": KERNEL_INVOCATION_SCHEDULE_SHA256,
    "worker_gpu_namespace": "one_physical_to_logical_zero",
    "worker_stdout": "untrusted_ignored",
}
KERNELBENCH_META_PROTOCOL_SHA256 = hashlib.sha256(
    json.dumps(_PROTOCOL, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

_TASK_ID = re.compile(r"level([12])/(\d+)_([^/]+)\.py")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
_MAX_CANDIDATE_BYTES = 2 * 1024 * 1024
_MAX_RESULT_BYTES = 64 * 1024
_RESULT_KEYS = {
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
    "elapsed_seconds",
    "gpu_seconds",
    "hardware",
}


class MetaSnapshotMismatchError(RuntimeError):
    """The KernelBench checkout or trusted scorer differs from its frozen pin."""


class MetaSupervisorEvidenceError(ValueError):
    """The private result is malformed, incomplete, or rebound."""


@dataclass(frozen=True)
class KernelBenchMetaTask:
    task_id: str
    source_path: str
    task_sha256: str
    level: int
    problem_id: int
    repository_commit: str = KERNELBENCH_META_REPOSITORY_COMMIT
    correctness_trials: int = 5
    performance_trials: int = 100
    precision: str = "fp32"
    backend: str = "triton"
    gpu_arch: str = "Ampere"
    target_gpu: str = "A100"
    timeout_seconds: int = 300

    def __post_init__(self) -> None:
        expected = KERNELBENCH_META_TASK_HASHES.get(self.task_id)
        match = _TASK_ID.fullmatch(self.task_id)
        if expected is None or match is None:
            raise ValueError(
                f"KernelBench meta-train task is not frozen: {self.task_id}"
            )
        if (
            self.source_path != f"KernelBench/{self.task_id}"
            or self.task_sha256 != expected
            or self.level != int(match.group(1))
            or self.problem_id != int(match.group(2))
            or self.repository_commit != KERNELBENCH_META_REPOSITORY_COMMIT
            or self.correctness_trials != 5
            or self.performance_trials != 100
            or self.precision != "fp32"
            or self.backend != "triton"
            or self.gpu_arch != "Ampere"
            or self.target_gpu != "A100"
            or self.timeout_seconds != 300
        ):
            raise ValueError("KernelBench meta-train task differs from the frozen contract")

    @classmethod
    def from_task_id(cls, task_id: str) -> "KernelBenchMetaTask":
        expected = KERNELBENCH_META_TASK_HASHES.get(task_id)
        match = _TASK_ID.fullmatch(task_id)
        if expected is None or match is None:
            raise ValueError(f"KernelBench meta-train task is not frozen: {task_id}")
        return cls(
            task_id=task_id,
            source_path=f"KernelBench/{task_id}",
            task_sha256=expected,
            level=int(match.group(1)),
            problem_id=int(match.group(2)),
        )

    @property
    def task_spec(self) -> TaskSpec:
        return TaskSpec(
            task_id=f"kernelbench:{self.task_id}",
            display_name=f"KernelBench meta-train {Path(self.task_id).stem}",
            level=self.level,
            problem_id=self.problem_id,
            task_path=self.source_path,
            task_sha256=self.task_sha256,
            repository_commit=self.repository_commit,
            target_gpu=self.target_gpu,
            gpu_arch=self.gpu_arch,
            backend=self.backend,
            precision=self.precision,
            correctness_trials=self.correctness_trials,
            performance_trials=self.performance_trials,
            timeout_seconds=self.timeout_seconds,
        )


@dataclass(frozen=True)
class MetaSnapshotIdentity:
    repository_commit: str
    task_sha256: str

    def __post_init__(self) -> None:
        if not _COMMIT.fullmatch(self.repository_commit):
            raise ValueError("invalid KernelBench repository commit")
        if not _SHA256.fullmatch(self.task_sha256):
            raise ValueError("invalid KernelBench task sha256")


@dataclass(frozen=True)
class MetaProcessOutcome:
    """Process streams are audit-only and never participate in the verdict."""

    returncode: int
    stdout: str = ""
    stderr: str = ""


@dataclass(frozen=True)
class MetaCanaryEvaluation:
    """Trusted protocol counts retained only for evaluator qualification."""

    result: EvaluationResult
    correctness_passed: int
    timing_trials_completed: int
    timing_outputs_correct: int

    def __post_init__(self) -> None:
        for value, maximum in (
            (self.correctness_passed, 5),
            (self.timing_trials_completed, 100),
            (self.timing_outputs_correct, 100),
        ):
            if type(value) is not int or not 0 <= value <= maximum:
                raise ValueError("invalid KernelBench meta canary protocol count")
        if self.timing_outputs_correct > self.timing_trials_completed:
            raise ValueError("KernelBench meta canary timing counts differ")
        if self.result.correct and (
            self.correctness_passed != 5
            or self.timing_trials_completed != 100
            or self.timing_outputs_correct != 100
        ):
            raise ValueError("correct canary result lacks full protocol counts")


@dataclass(frozen=True)
class MetaSupervisorCommand:
    attempt_id: str
    result_nonce: str
    scorer_sha256: str
    task: KernelBenchMetaTask
    candidate_sha256: str
    candidate_policy_sha256: str
    authorization_receipt_path: Path
    authorization_receipt_sha256: str
    argv: tuple[str, ...]
    worker_visible_argv: tuple[str, ...]
    cwd: Path
    environment_items: tuple[tuple[str, str], ...]
    timeout_seconds: float
    attempt_root: Path
    scratch_dir: Path
    cache_dir: Path
    candidate_path: Path
    private_result_path: Path

    @property
    def environment(self) -> dict[str, str]:
        return dict(self.environment_items)


SnapshotInspector = Callable[[Path, KernelBenchMetaTask], MetaSnapshotIdentity]
MetaCommandRunner = Callable[[MetaSupervisorCommand], MetaProcessOutcome]


def _strict_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise MetaSupervisorEvidenceError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> object:
    raise MetaSupervisorEvidenceError(f"non-finite JSON constant: {value}")


def _number(payload: Mapping[str, object], key: str, *, optional: bool) -> float | None:
    value = payload[key]
    if value is None and optional:
        return None
    if type(value) not in (int, float) or not math.isfinite(float(value)):
        raise MetaSupervisorEvidenceError(f"{key} must be a finite number")
    number = float(value)
    if number < 0 or (optional and number <= 0):
        raise MetaSupervisorEvidenceError(f"{key} is out of range")
    return number


def _read_private_json(path: Path) -> dict[str, object]:
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise MetaSupervisorEvidenceError("private supervisor evidence is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise MetaSupervisorEvidenceError("private supervisor evidence must be regular")
    if metadata.st_uid != os.geteuid():
        raise MetaSupervisorEvidenceError("private supervisor evidence owner differs")
    if stat.S_IMODE(metadata.st_mode) != 0o600:
        raise MetaSupervisorEvidenceError("private supervisor evidence mode must be 0600")
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise MetaSupervisorEvidenceError(
                    "private supervisor evidence must remain regular"
                )
            raw = stream.read(_MAX_RESULT_BYTES + 1)
    except MetaSupervisorEvidenceError:
        raise
    except OSError as exc:
        raise MetaSupervisorEvidenceError("private supervisor evidence is unreadable") from exc
    if len(raw) > _MAX_RESULT_BYTES:
        raise MetaSupervisorEvidenceError("private supervisor evidence is too large")
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_strict_object,
            parse_constant=_reject_constant,
        )
    except MetaSupervisorEvidenceError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise MetaSupervisorEvidenceError("private supervisor evidence is not exact JSON") from exc
    if not isinstance(payload, dict):
        raise MetaSupervisorEvidenceError("private supervisor evidence must be one object")
    return payload


def parse_meta_supervisor_evidence(
    path: Path,
    *,
    command: MetaSupervisorCommand,
) -> EvaluationResult:
    payload = _read_private_json(path)
    if set(payload) != _RESULT_KEYS:
        raise MetaSupervisorEvidenceError("private supervisor evidence keys differ")
    if type(payload["schema_version"]) is not int or payload["schema_version"] != 1:
        raise MetaSupervisorEvidenceError("unsupported private supervisor schema")
    bindings = {
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
        "schedule_sha256": KERNEL_INVOCATION_SCHEDULE_SHA256,
    }
    for key, expected in bindings.items():
        if type(payload[key]) is not str or payload[key] != expected:
            raise MetaSupervisorEvidenceError(f"{key} binding differs")
    input_schedule = payload["input_schedule_sha256"]
    if input_schedule is not None and (
        type(input_schedule) is not str or not _SHA256.fullmatch(input_schedule)
    ):
        raise MetaSupervisorEvidenceError("input schedule binding is invalid")
    if payload["health_probe"] not in {"passed", "failed"}:
        raise MetaSupervisorEvidenceError("unknown out-of-band health probe state")
    if type(payload["compiled"]) is not bool or type(payload["correct"]) is not bool:
        raise MetaSupervisorEvidenceError("compiled and correct must be booleans")
    for key, expected in (("correctness_trials", 5), ("timing_trials", 100)):
        if type(payload[key]) is not int or payload[key] != expected:
            raise MetaSupervisorEvidenceError("frozen protocol counts differ")
    for key, maximum in (
        ("correctness_passed", 5),
        ("timing_trials_completed", 100),
        ("timing_outputs_correct", 100),
    ):
        value = payload[key]
        if type(value) is not int or not 0 <= value <= maximum:
            raise MetaSupervisorEvidenceError("protocol counts are invalid")
    for key, limit in (("error_summary", 2_000), ("hardware", 256)):
        if type(payload[key]) is not str or len(payload[key]) > limit:
            raise MetaSupervisorEvidenceError(f"{key} must be bounded text")
    try:
        raw_status = payload["status"]
        if type(raw_status) is not str:
            raise ValueError
        status = EvaluationStatus(raw_status)
    except ValueError as exc:
        raise MetaSupervisorEvidenceError("unknown evaluation status") from exc

    compiled = payload["compiled"]
    correct = payload["correct"]
    correctness_passed = payload["correctness_passed"]
    timings_completed = payload["timing_trials_completed"]
    timings_correct = payload["timing_outputs_correct"]
    if timings_correct > timings_completed:
        raise MetaSupervisorEvidenceError("protocol counts are inconsistent")
    candidate_ms = _number(payload, "candidate_runtime_ms", optional=True)
    reference_ms = _number(payload, "reference_runtime_ms", optional=True)
    elapsed = _number(payload, "elapsed_seconds", optional=False)
    gpu_seconds = _number(payload, "gpu_seconds", optional=False)

    if status is EvaluationStatus.VALID:
        if (
            payload["health_probe"] != "passed"
            or not compiled
            or not correct
            or correctness_passed != 5
            or timings_completed != 100
            or timings_correct != 100
            or candidate_ms is None
            or reference_ms is None
            or input_schedule is None
        ):
            raise MetaSupervisorEvidenceError("valid result violates protocol counts")
    else:
        if correct:
            raise MetaSupervisorEvidenceError("only valid evidence may be correct")
        if candidate_ms is not None or reference_ms is not None:
            raise MetaSupervisorEvidenceError("only valid evidence may expose timing")
        if status is EvaluationStatus.ENVIRONMENT_INVALID:
            if payload["health_probe"] != "failed":
                raise MetaSupervisorEvidenceError(
                    "environment failure lacks out-of-band health evidence"
                )
        elif payload["health_probe"] != "passed":
            raise MetaSupervisorEvidenceError(
                "candidate failure cannot be inferred from environment failure"
            )
        if status is EvaluationStatus.COMPILE_FAILED and (compiled or correct):
            raise MetaSupervisorEvidenceError("compile failure flags differ")
        if status is EvaluationStatus.POLICY_REJECTED and (compiled or correct):
            raise MetaSupervisorEvidenceError("policy rejection flags differ")
        if status is EvaluationStatus.INCORRECT and (not compiled or correct):
            raise MetaSupervisorEvidenceError("incorrect result flags differ")

    try:
        return EvaluationResult(
            status=status,
            compiled=compiled,
            correct=correct,
            candidate_runtime_ms=candidate_ms,
            reference_runtime_ms=reference_ms,
            error_summary=payload["error_summary"],
            elapsed_seconds=elapsed or 0.0,
            gpu_seconds=gpu_seconds or 0.0,
            hardware=payload["hardware"],
            raw_log_path=str(path),
        )
    except ValueError as exc:
        raise MetaSupervisorEvidenceError("private evidence violates result contract") from exc


def inspect_meta_snapshot(
    repository: Path, task: KernelBenchMetaTask
) -> MetaSnapshotIdentity:
    try:
        process = subprocess.run(
            ("git", "-C", str(repository), "rev-parse", "HEAD"),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise MetaSnapshotMismatchError("cannot inspect KernelBench commit") from exc
    commit = process.stdout.strip() if process.returncode == 0 else ""
    try:
        source = (repository / task.source_path).read_bytes()
    except OSError as exc:
        raise MetaSnapshotMismatchError("cannot read frozen KernelBench task") from exc
    return MetaSnapshotIdentity(
        repository_commit=commit,
        task_sha256=hashlib.sha256(source).hexdigest(),
    )


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _read_regular(path: Path, *, limit: int, label: str) -> bytes:
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise ValueError(f"{label} is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise ValueError(f"{label} must be a regular non-symlink file")
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            raw = stream.read(limit + 1)
    except OSError as exc:
        raise ValueError(f"{label} cannot be read") from exc
    if len(raw) > limit:
        raise ValueError(f"{label} is too large")
    return raw


def _bind_authorization_receipt(path: Path) -> tuple[Path, str]:
    """Return the immutable private receipt path and its content identity."""

    absolute = path.absolute()
    try:
        metadata = absolute.lstat()
    except OSError as exc:
        raise ValueError("KernelBench meta authorization receipt is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise ValueError(
            "KernelBench meta authorization receipt must be a regular non-symlink file"
        )
    raw = _read_regular(
        absolute,
        limit=64 * 1024,
        label="KernelBench meta authorization receipt",
    )
    try:
        bound = absolute.resolve(strict=True)
        bound_metadata = bound.stat()
    except OSError as exc:
        raise ValueError("KernelBench meta authorization receipt is missing") from exc
    if (
        bound_metadata.st_uid != os.geteuid()
        or stat.S_IMODE(bound_metadata.st_mode) != 0o600
    ):
        raise ValueError(
            "KernelBench meta authorization receipt must be owned by the controller with mode 0600"
        )
    receipt_sha256 = hashlib.sha256(raw).hexdigest()
    if bound.name != f"{receipt_sha256}.json":
        raise ValueError(
            "KernelBench meta authorization receipt must be content addressed"
        )
    return bound, receipt_sha256


class KernelBenchMetaAdapter:
    """Strict outer adapter for the HB-GEN-1 KernelBench training scorer.

    The injected trusted supervisor, not this adapter, owns the candidate worker
    and the one-device bubblewrap namespace.  Process streams are discarded.  A
    verdict exists only when a mode-0600 private object binds every immutable
    identity and all 5 + 100 correctness-bound protocol counts.
    """

    def __init__(
        self,
        *,
        repository: Path,
        supervisor: Path,
        scorer_sha256: str,
        scratch_root: Path,
        authorization_receipt: Path,
        gpu: str,
        python_executable: str = sys.executable,
        timeout_seconds: float = KERNELBENCH_META_TIMEOUT_SECONDS,
        runner: MetaCommandRunner | None = None,
        snapshot_inspector: SnapshotInspector | None = None,
        attempt_id_factory: Callable[[], str] | None = None,
        nonce_factory: Callable[[], str] | None = None,
        base_environment: Mapping[str, str] | None = None,
    ) -> None:
        if not _SHA256.fullmatch(scorer_sha256):
            raise ValueError("KernelBench meta scorer sha256 is invalid")
        if not re.fullmatch(r"[0-9]+", gpu):
            raise ValueError("KernelBench meta GPU must be one numeric device")
        if timeout_seconds <= 0 or not math.isfinite(timeout_seconds):
            raise ValueError("KernelBench meta timeout must be positive and finite")
        self.repository = repository.resolve()
        self.supervisor = supervisor.absolute()
        self.scorer_sha256 = scorer_sha256
        self.scratch_root = scratch_root.resolve()
        (
            self.authorization_receipt_path,
            self.authorization_receipt_sha256,
        ) = _bind_authorization_receipt(authorization_receipt)
        if any(
            self.authorization_receipt_path == root
            or _is_relative_to(self.authorization_receipt_path, root)
            for root in (self.repository, self.scratch_root)
        ):
            raise ValueError(
                "KernelBench meta authorization receipt overlaps worker-visible state"
            )
        self.gpu = gpu
        self.python_executable = python_executable
        self.timeout_seconds = float(timeout_seconds)
        self._runner = runner or self._run_subprocess
        self._snapshot_inspector = snapshot_inspector or inspect_meta_snapshot
        self._attempt_id_factory = attempt_id_factory or (lambda: uuid.uuid4().hex)
        self._nonce_factory = nonce_factory or (lambda: secrets.token_hex(32))
        if base_environment is None:
            base_environment = {
                "LANG": "C.UTF-8",
                "LC_ALL": "C.UTF-8",
                "PATH": "/usr/bin:/bin",
            }
        if any(
            not isinstance(key, str)
            or not isinstance(value, str)
            or "\x00" in key
            or "\x00" in value
            for key, value in base_environment.items()
        ):
            raise ValueError("invalid trusted supervisor environment")
        self._base_environment = dict(base_environment)

    def _verify_frozen_inputs(self, task: KernelBenchMetaTask) -> None:
        actual = self._snapshot_inspector(self.repository, task)
        if actual.repository_commit != task.repository_commit:
            raise MetaSnapshotMismatchError("KernelBench repository commit differs")
        if actual.task_sha256 != task.task_sha256:
            raise MetaSnapshotMismatchError("KernelBench task sha256 differs")
        supervisor = _read_regular(
            self.supervisor, limit=2 * 1024 * 1024, label="trusted supervisor"
        )
        direct_sha = hashlib.sha256(supervisor).hexdigest()
        if direct_sha != self.scorer_sha256:
            project_root = self.supervisor.parent.parent
            if (
                self.supervisor.name != "hb_gen1_kernelbench_meta_supervisor.py"
                or kernelbench_meta_scorer_bundle_sha256(project_root)
                != self.scorer_sha256
            ):
                raise MetaSnapshotMismatchError(
                    "KernelBench meta scorer bundle sha256 differs"
                )
        receipt_path, receipt_sha256 = _bind_authorization_receipt(
            self.authorization_receipt_path
        )
        if (
            receipt_path != self.authorization_receipt_path
            or receipt_sha256 != self.authorization_receipt_sha256
        ):
            raise MetaSnapshotMismatchError(
                "KernelBench meta authorization receipt binding differs"
            )

    def prepare_attempt(
        self,
        task: KernelBenchMetaTask,
        candidate_path: Path,
        private_log_dir: Path,
        *,
        canary_id: str = "formal",
    ) -> MetaSupervisorCommand:
        self._verify_frozen_inputs(task)
        if not _SAFE_ID.fullmatch(canary_id):
            raise ValueError("unsafe KernelBench meta canary id")
        candidate_bytes = _read_regular(
            candidate_path.absolute(),
            limit=_MAX_CANDIDATE_BYTES,
            label="KernelBench candidate",
        )
        policy_report = RestrictedKernelCandidatePolicy().validate(
            candidate_bytes, task_id=task.task_id
        )
        candidate_sha = hashlib.sha256(candidate_bytes).hexdigest()
        if policy_report.source_sha256 != candidate_sha:
            raise RestrictedKernelCandidateError("candidate policy source binding differs")
        attempt_id = self._attempt_id_factory()
        nonce = self._nonce_factory()
        if not isinstance(attempt_id, str) or not _SAFE_ID.fullmatch(attempt_id):
            raise ValueError("unsafe KernelBench meta attempt id")
        if not isinstance(nonce, str) or not _SHA256.fullmatch(nonce):
            raise ValueError("unsafe KernelBench meta result nonce")

        self.scratch_root.mkdir(parents=True, exist_ok=True, mode=0o700)
        if stat.S_IMODE(self.scratch_root.stat().st_mode) != 0o700:
            raise ValueError("KernelBench meta scratch root mode must be 0700")
        attempt_root = self.scratch_root / attempt_id
        attempt_root.mkdir(mode=0o700)
        scratch_dir = attempt_root / "scratch"
        cache_dir = attempt_root / "cache"
        scratch_dir.mkdir(mode=0o700)
        cache_dir.mkdir(mode=0o700)
        for name in (
            "cuda",
            "pycache",
            "torch_extensions",
            "torchinductor",
            "triton",
            "uv",
            "xdg",
        ):
            (cache_dir / name).mkdir(mode=0o700)
        candidate_dir = attempt_root / "candidate"
        candidate_dir.mkdir(mode=0o700)
        candidate_snapshot = candidate_dir / "candidate.py"
        descriptor = os.open(
            candidate_snapshot,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
            0o400,
        )
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(candidate_bytes)
        candidate_dir.chmod(0o500)

        private_log_dir = private_log_dir.resolve()
        if (
            private_log_dir == self.scratch_root
            or _is_relative_to(private_log_dir, self.scratch_root)
            or _is_relative_to(self.scratch_root, private_log_dir)
        ):
            raise ValueError("private result root must be disjoint from worker state")
        private_log_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
        if stat.S_IMODE(private_log_dir.stat().st_mode) != 0o700:
            raise ValueError("private result root mode must be 0700")
        private_attempt = private_log_dir / attempt_id
        private_attempt.mkdir(mode=0o700)
        private_result = private_attempt / f"result-{nonce}.json"

        environment = dict(self._base_environment)
        environment.update(
            {
                "CUDA_VISIBLE_DEVICES": self.gpu,
                "PYTHONNOUSERSITE": "1",
                "TMP": str(scratch_dir),
                "TEMP": str(scratch_dir),
                "TMPDIR": str(scratch_dir),
                "XDG_CACHE_HOME": str(cache_dir / "xdg"),
                "UV_CACHE_DIR": str(cache_dir / "uv"),
                "TRITON_CACHE_DIR": str(cache_dir / "triton"),
                "TORCH_EXTENSIONS_DIR": str(cache_dir / "torch_extensions"),
                "TORCHINDUCTOR_CACHE_DIR": str(cache_dir / "torchinductor"),
                "CUDA_CACHE_PATH": str(cache_dir / "cuda"),
                "PYTHONPYCACHEPREFIX": str(cache_dir / "pycache"),
            }
        )
        argv = (
            self.python_executable,
            "-I",
            str(self.supervisor),
            "--repository",
            str(self.repository),
            "--repository-commit",
            task.repository_commit,
            "--task-id",
            task.task_id,
            "--task-path",
            task.source_path,
            "--task-sha256",
            task.task_sha256,
            "--candidate",
            str(candidate_snapshot),
            "--candidate-sha256",
            candidate_sha,
            "--candidate-policy-sha256",
            policy_report.policy_sha256,
            "--invocation-schedule-sha256",
            KERNEL_INVOCATION_SCHEDULE_SHA256,
            "--scratch-dir",
            str(scratch_dir),
            "--cache-dir",
            str(cache_dir),
            "--private-result",
            str(private_result),
            "--attempt-id",
            attempt_id,
            "--result-nonce",
            nonce,
            "--canary-id",
            canary_id,
            "--gpu",
            self.gpu,
            "--evaluator",
            KERNELBENCH_META_EVALUATOR_ID,
            "--protocol-sha256",
            KERNELBENCH_META_PROTOCOL_SHA256,
            "--scorer-sha256",
            self.scorer_sha256,
            "--authorization-receipt",
            str(self.authorization_receipt_path),
        )
        # This is the only shape the untrusted worker may see.  Physical GPU 4
        # is intentionally exposed as logical GPU 0 by the bubblewrap broker;
        # neither the nonce nor the private result endpoint crosses that edge.
        worker_visible_argv = (
            "/sandbox/repository",
            "/sandbox/input/candidate.py",
            "/sandbox/work",
            "/sandbox/cache",
            "0",
        )
        return MetaSupervisorCommand(
            attempt_id=attempt_id,
            result_nonce=nonce,
            scorer_sha256=self.scorer_sha256,
            task=task,
            candidate_sha256=candidate_sha,
            candidate_policy_sha256=policy_report.policy_sha256,
            authorization_receipt_path=self.authorization_receipt_path,
            authorization_receipt_sha256=self.authorization_receipt_sha256,
            argv=argv,
            worker_visible_argv=worker_visible_argv,
            cwd=self.repository,
            environment_items=tuple(sorted(environment.items())),
            timeout_seconds=self.timeout_seconds,
            attempt_root=attempt_root,
            scratch_dir=scratch_dir,
            cache_dir=cache_dir,
            candidate_path=candidate_snapshot,
            private_result_path=private_result,
        )

    def evaluate(
        self,
        task: KernelBenchMetaTask,
        candidate_path: Path,
        private_log_dir: Path,
    ) -> EvaluationResult:
        command = self.prepare_attempt(task, candidate_path, private_log_dir)
        return self._evaluate_prepared(command)

    def evaluate_canary(
        self,
        task: KernelBenchMetaTask,
        candidate_path: Path,
        private_log_dir: Path,
        *,
        canary_id: str,
    ) -> MetaCanaryEvaluation:
        """Evaluate one frozen canary, including expected static rejections.

        Static policy canaries still consume their controller-owned evaluator
        opportunity, but they never start the GPU supervisor.  Their rejection
        cannot be inferred from candidate stdout or a worker-written result.
        """

        try:
            command = self.prepare_attempt(
                task, candidate_path, private_log_dir, canary_id=canary_id
            )
        except RestrictedKernelCandidateError as exc:
            return MetaCanaryEvaluation(
                result=EvaluationResult(
                    status=EvaluationStatus.POLICY_REJECTED,
                    compiled=False,
                    correct=False,
                    error_summary=" ".join(str(exc).split())[:2_000],
                    elapsed_seconds=0.0,
                    gpu_seconds=0.0,
                ),
                correctness_passed=0,
                timing_trials_completed=0,
                timing_outputs_correct=0,
            )
        result = self._evaluate_prepared(command)
        correctness_passed = 0
        timing_completed = 0
        timing_correct = 0
        if result.status in {
            EvaluationStatus.VALID,
            EvaluationStatus.COMPILE_FAILED,
            EvaluationStatus.INCORRECT,
            EvaluationStatus.POLICY_REJECTED,
        }:
            payload = _read_private_json(command.private_result_path)
            correctness_passed = int(payload["correctness_passed"])
            timing_completed = int(payload["timing_trials_completed"])
            timing_correct = int(payload["timing_outputs_correct"])
        return MetaCanaryEvaluation(
            result=result,
            correctness_passed=correctness_passed,
            timing_trials_completed=timing_completed,
            timing_outputs_correct=timing_correct,
        )

    def _evaluate_prepared(
        self, command: MetaSupervisorCommand
    ) -> EvaluationResult:
        started = time.monotonic()
        try:
            outcome = self._runner(command)
        except (subprocess.TimeoutExpired, TimeoutError):
            return self._infrastructure_result(
                EvaluationStatus.TIMEOUT,
                "trusted KernelBench meta supervisor timed out",
                time.monotonic() - started,
                command.private_result_path,
            )
        except OSError:
            return self._infrastructure_result(
                EvaluationStatus.ENVIRONMENT_INVALID,
                "trusted KernelBench meta supervisor could not start",
                time.monotonic() - started,
                command.private_result_path,
            )
        elapsed = time.monotonic() - started
        if not isinstance(outcome, MetaProcessOutcome) or outcome.returncode != 0:
            return self._infrastructure_result(
                EvaluationStatus.ENVIRONMENT_INVALID,
                "trusted KernelBench meta supervisor exited unsuccessfully",
                elapsed,
                command.private_result_path,
            )
        try:
            return parse_meta_supervisor_evidence(
                command.private_result_path,
                command=command,
            )
        except MetaSupervisorEvidenceError:
            return self._infrastructure_result(
                EvaluationStatus.ENVIRONMENT_INVALID,
                "trusted KernelBench meta supervisor evidence is invalid",
                elapsed,
                command.private_result_path,
            )

    @staticmethod
    def _infrastructure_result(
        status: EvaluationStatus,
        summary: str,
        elapsed: float,
        result_path: Path,
    ) -> EvaluationResult:
        return EvaluationResult(
            status=status,
            compiled=False,
            correct=False,
            error_summary=summary,
            elapsed_seconds=elapsed,
            gpu_seconds=elapsed,
            raw_log_path=str(result_path),
        )

    @staticmethod
    def _run_subprocess(command: MetaSupervisorCommand) -> MetaProcessOutcome:
        process = subprocess.run(
            command.argv,
            cwd=command.cwd,
            env=command.environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=command.timeout_seconds,
            check=False,
        )
        return MetaProcessOutcome(returncode=process.returncode)
