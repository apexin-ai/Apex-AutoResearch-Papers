from __future__ import annotations

import hashlib
import json
import math
import os
import re
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


KERNELBENCHX_REPOSITORY_COMMIT = "fd4192293bf9a8c645327a9d46aa1e807f1f9cf2"
KERNELBENCHX_DATASET_COMMIT = KERNELBENCHX_REPOSITORY_COMMIT
KERNELBENCHX_EVALUATOR_ID = "kernelbenchx-call-exe-perf"
KERNELBENCHX_TIMEOUT_SECONDS = 600.0

KERNELBENCHX_TASK_HASHES: Mapping[str, str] = MappingProxyType(
    {
        "Quantization/conv2d_w8a8.py": (
            "00d90f42cda63efccb071216a8084cbf2cfbe34b217fe538fddc878b1741e5e9"
        ),
        "Quantization/layernorm_w8a8.py": (
            "890ae6a77880dd4004f6d5adc40b910c691807b0d1ced8e1372cc4d243687c8c"
        ),
        "Quantization/bmm_w8a8.py": (
            "e8dff9a694fa8a52eb9a126496c219758cbeacb775ef7c82eb3e10178cc3286f"
        ),
        "Quantization/attention_w8a8.py": (
            "d217a9d784c631a30680dfffa3c5b2b97a7d481aa00b572555f13344c6752b9d"
        ),
        "Quantization/matmul_w8a8.py": (
            "5e92b4e481fe508415b6d5e054cd534fc39df1fcc700656a9a21ccae61f641d9"
        ),
        "Quantization/linear_w4a16.py": (
            "ff6cb752a497289e8966e69dfc5ca2add1612d2d161df461a781043671de7e1d"
        ),
        "Fusion/fused_relu_max_pool2d_conv2d.py": (
            "99fddc19b0e1987f7e64ef4e8711590696f9f15f469a3b887f1cf7bcda638177"
        ),
        "MatrixMultiply/matmul_fp16.py": (
            "99c47c251e7ee8cc0b25ea7dd84acdc725f7f36251ca72e0833ea427897d4570"
        ),
    }
)

ADVERSARIAL_CANARY_IDS = ("wrong", "noop", "fake_stdout")

_COMMIT = re.compile(r"[0-9a-f]{40}")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ATTEMPT_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
_MAX_PRIVATE_RESULT_BYTES = 64 * 1024
_PRIVATE_RESULT_KEYS = {
    "schema_version",
    "evaluator",
    "attempt_id",
    "repository_commit",
    "dataset_commit",
    "task_id",
    "task_sha256",
    "candidate_sha256",
    "status",
    "compiled",
    "correct",
    "candidate_runtime_ms",
    "reference_runtime_ms",
    "reference_compile_runtime_ms",
    "error_summary",
    "elapsed_seconds",
    "gpu_seconds",
    "hardware",
}


class SnapshotMismatchError(RuntimeError):
    """The local evaluator checkout does not match the frozen HB-GEN-1 pins."""


class SupervisorEvidenceError(ValueError):
    """The trusted supervisor result is missing, malformed, or not fully bound."""


@dataclass(frozen=True)
class KernelBenchXTask:
    task_id: str
    source_path: str
    task_sha256: str
    repository_commit: str = KERNELBENCHX_REPOSITORY_COMMIT
    dataset_commit: str = KERNELBENCHX_DATASET_COMMIT

    def __post_init__(self) -> None:
        expected_hash = KERNELBENCHX_TASK_HASHES.get(self.task_id)
        if expected_hash is None:
            raise ValueError(f"KernelBenchX task is not frozen for HB-GEN-1: {self.task_id}")
        expected_path = f"data/kernelbenchx/{self.task_id}"
        if (
            self.source_path != expected_path
            or self.task_sha256 != expected_hash
            or self.repository_commit != KERNELBENCHX_REPOSITORY_COMMIT
            or self.dataset_commit != KERNELBENCHX_DATASET_COMMIT
        ):
            raise ValueError("KernelBenchX task differs from the frozen HB-GEN-1 contract")

    @classmethod
    def from_task_id(cls, task_id: str) -> "KernelBenchXTask":
        task_hash = KERNELBENCHX_TASK_HASHES.get(task_id)
        if task_hash is None:
            raise ValueError(f"KernelBenchX task is not frozen for HB-GEN-1: {task_id}")
        return cls(
            task_id=task_id,
            source_path=f"data/kernelbenchx/{task_id}",
            task_sha256=task_hash,
        )


@dataclass(frozen=True)
class SnapshotIdentity:
    repository_commit: str
    dataset_commit: str
    task_sha256: str

    def __post_init__(self) -> None:
        if not _COMMIT.fullmatch(self.repository_commit):
            raise ValueError("invalid repository commit")
        if not _COMMIT.fullmatch(self.dataset_commit):
            raise ValueError("invalid dataset commit")
        if not _SHA256.fullmatch(self.task_sha256):
            raise ValueError("invalid task sha256")


@dataclass(frozen=True)
class ProcessOutcome:
    """Minimal process DTO; stdout/stderr are retained only for caller-side audit.

    The adapter deliberately never inspects either stream when deciding an outcome.
    """

    returncode: int
    stdout: str = ""
    stderr: str = ""


@dataclass(frozen=True)
class SupervisorCommand:
    attempt_id: str
    canary_id: str
    task: KernelBenchXTask
    candidate_sha256: str
    argv: tuple[str, ...]
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


@dataclass(frozen=True)
class PreflightCommandPlan:
    canary_id: str
    expected_statuses: frozenset[EvaluationStatus]
    command: SupervisorCommand

    def passed_by(self, result: EvaluationResult) -> bool:
        if result.status not in self.expected_statuses:
            return False
        if self.canary_id == "reference":
            return result.status is EvaluationStatus.VALID and result.correct
        return not result.correct


SnapshotInspector = Callable[[Path, KernelBenchXTask], SnapshotIdentity]
CommandRunner = Callable[[SupervisorCommand], ProcessOutcome]


def _strict_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise SupervisorEvidenceError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def _reject_json_constant(value: str) -> object:
    raise SupervisorEvidenceError(f"non-finite JSON number: {value}")


def _number(
    payload: Mapping[str, object],
    key: str,
    *,
    optional: bool,
) -> float | None:
    value = payload[key]
    if value is None and optional:
        return None
    if type(value) not in (int, float) or not math.isfinite(float(value)):
        raise SupervisorEvidenceError(f"{key} must be a finite number")
    return float(value)


def parse_supervisor_evidence(
    path: Path,
    *,
    task: KernelBenchXTask,
    attempt_id: str,
    candidate_sha256: str,
) -> EvaluationResult:
    """Parse one exact, private supervisor object; never salvage process output."""

    try:
        metadata = path.lstat()
    except OSError as exc:
        raise SupervisorEvidenceError("private supervisor JSON is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise SupervisorEvidenceError("private supervisor JSON must be a regular file")
    try:
        descriptor = os.open(
            path,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0),
        )
        with os.fdopen(descriptor, "rb") as stream:
            opened_metadata = os.fstat(stream.fileno())
            if not stat.S_ISREG(opened_metadata.st_mode):
                raise SupervisorEvidenceError(
                    "private supervisor JSON must be a regular file"
                )
            raw_bytes = stream.read(_MAX_PRIVATE_RESULT_BYTES + 1)
        if len(raw_bytes) > _MAX_PRIVATE_RESULT_BYTES:
            raise SupervisorEvidenceError("private supervisor JSON is too large")
        raw = raw_bytes.decode("utf-8")
        payload = json.loads(
            raw,
            object_pairs_hook=_strict_json_object,
            parse_constant=_reject_json_constant,
        )
    except SupervisorEvidenceError:
        raise
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SupervisorEvidenceError("private supervisor result is not exact JSON") from exc
    if not isinstance(payload, dict):
        raise SupervisorEvidenceError("private supervisor JSON must be one object")
    actual_keys = set(payload)
    if actual_keys != _PRIVATE_RESULT_KEYS:
        missing = sorted(_PRIVATE_RESULT_KEYS - actual_keys)
        extra = sorted(actual_keys - _PRIVATE_RESULT_KEYS)
        raise SupervisorEvidenceError(
            f"private supervisor JSON keys differ: missing={missing}, extra={extra}"
        )

    if type(payload["schema_version"]) is not int or payload["schema_version"] != 1:
        raise SupervisorEvidenceError("unsupported supervisor schema version")
    exact_bindings = {
        "evaluator": KERNELBENCHX_EVALUATOR_ID,
        "attempt_id": attempt_id,
        "repository_commit": task.repository_commit,
        "dataset_commit": task.dataset_commit,
        "task_id": task.task_id,
        "task_sha256": task.task_sha256,
        "candidate_sha256": candidate_sha256,
    }
    for key, expected in exact_bindings.items():
        if type(payload[key]) is not str or payload[key] != expected:
            raise SupervisorEvidenceError(f"private supervisor {key} binding differs")
    if type(payload["compiled"]) is not bool or type(payload["correct"]) is not bool:
        raise SupervisorEvidenceError("compiled and correct must be booleans")
    for key, limit in (("error_summary", 2_000), ("hardware", 256)):
        if type(payload[key]) is not str or len(payload[key]) > limit:
            raise SupervisorEvidenceError(f"{key} must be a bounded string")

    try:
        status_value = payload["status"]
        if type(status_value) is not str:
            raise ValueError
        status_value = EvaluationStatus(status_value)
    except ValueError as exc:
        raise SupervisorEvidenceError("unknown evaluation status") from exc

    compiled = payload["compiled"]
    correct = payload["correct"]
    candidate_runtime_ms = _number(payload, "candidate_runtime_ms", optional=True)
    reference_runtime_ms = _number(payload, "reference_runtime_ms", optional=True)
    reference_compile_runtime_ms = _number(
        payload, "reference_compile_runtime_ms", optional=True
    )
    elapsed_seconds = _number(payload, "elapsed_seconds", optional=False)
    gpu_seconds = _number(payload, "gpu_seconds", optional=False)
    if status_value is not EvaluationStatus.VALID and any(
        value is not None
        for value in (
            candidate_runtime_ms,
            reference_runtime_ms,
            reference_compile_runtime_ms,
        )
    ):
        raise SupervisorEvidenceError("only a valid result may carry timing scores")
    if status_value is EvaluationStatus.COMPILE_FAILED and (compiled or correct):
        raise SupervisorEvidenceError("compile_failed flags are inconsistent")
    if status_value is EvaluationStatus.INCORRECT and (not compiled or correct):
        raise SupervisorEvidenceError("incorrect flags are inconsistent")
    if status_value is EvaluationStatus.POLICY_REJECTED and (compiled or correct):
        raise SupervisorEvidenceError("policy_rejected flags are inconsistent")

    try:
        return EvaluationResult(
            status=status_value,
            compiled=compiled,
            correct=correct,
            candidate_runtime_ms=candidate_runtime_ms,
            reference_runtime_ms=reference_runtime_ms,
            reference_compile_runtime_ms=reference_compile_runtime_ms,
            error_summary=payload["error_summary"],
            elapsed_seconds=elapsed_seconds,
            gpu_seconds=gpu_seconds,
            hardware=payload["hardware"],
            raw_log_path=str(path),
        )
    except ValueError as exc:
        raise SupervisorEvidenceError("supervisor result violates EvaluationResult") from exc


def inspect_local_snapshot(repository: Path, task: KernelBenchXTask) -> SnapshotIdentity:
    """Read the trusted checkout identity without invoking any candidate code."""

    try:
        process = subprocess.run(
            ["git", "-C", str(repository), "rev-parse", "HEAD"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise SnapshotMismatchError("cannot read KernelBenchX repository commit") from exc
    commit = process.stdout.strip() if process.returncode == 0 else ""
    if not _COMMIT.fullmatch(commit):
        raise SnapshotMismatchError("cannot read KernelBenchX repository commit")
    task_path = repository / task.source_path
    try:
        task_bytes = task_path.read_bytes()
    except OSError as exc:
        raise SnapshotMismatchError(f"cannot read frozen task: {task.source_path}") from exc
    return SnapshotIdentity(
        repository_commit=commit,
        dataset_commit=commit,
        task_sha256=hashlib.sha256(task_bytes).hexdigest(),
    )


class KernelBenchXAdapter:
    """HB-GEN-1 adapter around a separately trusted KernelBenchX supervisor.

    The supervisor is responsible for process isolation and for writing the one
    private JSON object parsed above.  Candidate stdout and stderr are never an
    evaluator control channel.
    """

    def __init__(
        self,
        *,
        repository: Path,
        supervisor: Path,
        scratch_root: Path,
        gpu: str,
        python_executable: str = sys.executable,
        timeout_seconds: float = KERNELBENCHX_TIMEOUT_SECONDS,
        golden_machine: str = "a100",
        runner: CommandRunner | None = None,
        snapshot_inspector: SnapshotInspector | None = None,
        attempt_id_factory: Callable[[], str] | None = None,
        base_environment: Mapping[str, str] | None = None,
    ):
        if not re.fullmatch(r"[0-9]+", gpu):
            raise ValueError("KernelBenchX GPU must be one numeric device id")
        if timeout_seconds <= 0 or not math.isfinite(timeout_seconds):
            raise ValueError("KernelBenchX timeout must be positive and finite")
        if not re.fullmatch(r"[A-Za-z0-9._-]{1,64}", golden_machine):
            raise ValueError("unsafe KernelBenchX golden machine")
        self.repository = repository.resolve()
        # Keep the final path component unresolved so a supervisor symlink can
        # be rejected before execution.
        self.supervisor = supervisor.absolute()
        self.scratch_root = scratch_root.resolve()
        self.gpu = gpu
        self.python_executable = python_executable
        self.timeout_seconds = float(timeout_seconds)
        self.golden_machine = golden_machine
        self._runner = runner or self._run_subprocess
        self._snapshot_inspector = snapshot_inspector or inspect_local_snapshot
        self._attempt_id_factory = attempt_id_factory or (lambda: uuid.uuid4().hex)
        if base_environment is None:
            base_environment = {
                key: os.environ[key]
                for key in ("PATH", "LANG", "LC_ALL", "LD_LIBRARY_PATH")
                if key in os.environ
            }
        if not all(
            isinstance(key, str)
            and isinstance(value, str)
            and "\x00" not in key
            and "\x00" not in value
            for key, value in base_environment.items()
        ):
            raise ValueError("invalid base environment")
        self._base_environment = dict(base_environment)

    def _verify_snapshot(self, task: KernelBenchXTask) -> None:
        actual = self._snapshot_inspector(self.repository, task)
        if actual.repository_commit != task.repository_commit:
            raise SnapshotMismatchError(
                "KernelBenchX repository commit differs from the frozen pin"
            )
        if actual.dataset_commit != task.dataset_commit:
            raise SnapshotMismatchError(
                "KernelBenchX dataset commit differs from the frozen pin"
            )
        if actual.task_sha256 != task.task_sha256:
            raise SnapshotMismatchError(
                "KernelBenchX task sha256 differs from the frozen pin"
            )

    def prepare_attempt(
        self,
        task: KernelBenchXTask,
        candidate_path: Path,
        private_log_dir: Path,
        *,
        canary_id: str = "formal",
    ) -> SupervisorCommand:
        self._verify_snapshot(task)
        if not _SAFE_ATTEMPT_ID.fullmatch(canary_id):
            raise ValueError("unsafe KernelBenchX canary id")
        if not self.supervisor.is_file() or self.supervisor.is_symlink():
            raise SnapshotMismatchError("trusted KernelBenchX supervisor is missing")
        candidate_path = candidate_path.absolute()
        try:
            candidate_metadata = candidate_path.lstat()
        except OSError as exc:
            raise ValueError(
                "KernelBenchX candidate must be a regular non-symlink file"
            ) from exc
        if stat.S_ISLNK(candidate_metadata.st_mode) or not stat.S_ISREG(
            candidate_metadata.st_mode
        ):
            raise ValueError("KernelBenchX candidate must be a regular non-symlink file")
        try:
            descriptor = os.open(
                candidate_path,
                os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0),
            )
            with os.fdopen(descriptor, "rb") as stream:
                if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                    raise ValueError(
                        "KernelBenchX candidate must be a regular non-symlink file"
                    )
                candidate_bytes = stream.read()
        except OSError as exc:
            raise ValueError(
                "KernelBenchX candidate must be a regular non-symlink file"
            ) from exc
        candidate_sha256 = hashlib.sha256(candidate_bytes).hexdigest()

        attempt_id = self._attempt_id_factory()
        if not isinstance(attempt_id, str) or not _SAFE_ATTEMPT_ID.fullmatch(attempt_id):
            raise ValueError("unsafe KernelBenchX attempt id")
        self.scratch_root.mkdir(parents=True, exist_ok=True, mode=0o700)
        attempt_root = self.scratch_root / attempt_id
        attempt_root.mkdir(mode=0o700)
        scratch_dir = attempt_root / "scratch"
        cache_dir = attempt_root / "cache"
        scratch_dir.mkdir(mode=0o700)
        cache_dir.mkdir(mode=0o700)
        for relative in (
            "xdg",
            "uv",
            "triton",
            "torch_extensions",
            "torchinductor",
            "cuda",
            "pycache",
        ):
            (cache_dir / relative).mkdir(mode=0o700)

        candidate_dir = scratch_dir / "candidate"
        candidate_dir.mkdir(mode=0o700)
        candidate_snapshot = candidate_dir / Path(task.task_id).name
        candidate_snapshot.write_bytes(candidate_bytes)
        candidate_snapshot.chmod(0o400)

        private_log_dir = private_log_dir.resolve()
        private_log_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
        private_attempt_dir = private_log_dir / attempt_id
        private_attempt_dir.mkdir(mode=0o700)
        private_result_path = private_attempt_dir / "supervisor-result.json"

        environment = dict(self._base_environment)
        environment.update(
            {
                "CUDA_VISIBLE_DEVICES": self.gpu,
                "PYTHONNOUSERSITE": "1",
                "PYTHONPATH": str(self.repository / "data"),
                "TMPDIR": str(scratch_dir),
                "TMP": str(scratch_dir),
                "TEMP": str(scratch_dir),
                "XDG_CACHE_HOME": str(cache_dir / "xdg"),
                "UV_CACHE_DIR": str(cache_dir / "uv"),
                "TRITON_CACHE_DIR": str(cache_dir / "triton"),
                "TORCH_EXTENSIONS_DIR": str(cache_dir / "torch_extensions"),
                "TORCHINDUCTOR_CACHE_DIR": str(cache_dir / "torchinductor"),
                "CUDA_CACHE_PATH": str(cache_dir / "cuda"),
                "PYTHONPYCACHEPREFIX": str(cache_dir / "pycache"),
                "KERNELBENCHX_GOLDEN_MACHINE": self.golden_machine,
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
            "--dataset-commit",
            task.dataset_commit,
            "--task-id",
            task.task_id,
            "--task-path",
            task.source_path,
            "--task-sha256",
            task.task_sha256,
            "--candidate",
            str(candidate_snapshot),
            "--candidate-sha256",
            candidate_sha256,
            "--scratch-dir",
            str(scratch_dir),
            "--cache-dir",
            str(cache_dir),
            "--private-result",
            str(private_result_path),
            "--attempt-id",
            attempt_id,
            "--canary-id",
            canary_id,
            "--gpu",
            self.gpu,
            "--evaluator",
            KERNELBENCHX_EVALUATOR_ID,
        )
        return SupervisorCommand(
            attempt_id=attempt_id,
            canary_id=canary_id,
            task=task,
            candidate_sha256=candidate_sha256,
            argv=argv,
            cwd=self.repository,
            environment_items=tuple(sorted(environment.items())),
            timeout_seconds=self.timeout_seconds,
            attempt_root=attempt_root,
            scratch_dir=scratch_dir,
            cache_dir=cache_dir,
            candidate_path=candidate_snapshot,
            private_result_path=private_result_path,
        )

    def evaluate(
        self,
        task: KernelBenchXTask,
        candidate_path: Path,
        private_log_dir: Path,
    ) -> EvaluationResult:
        command = self.prepare_attempt(task, candidate_path, private_log_dir)
        started = time.monotonic()
        try:
            outcome = self._runner(command)
        except (subprocess.TimeoutExpired, TimeoutError):
            elapsed = time.monotonic() - started
            return self._infrastructure_result(
                EvaluationStatus.TIMEOUT,
                "trusted KernelBenchX supervisor timed out",
                elapsed,
                command.private_result_path,
            )
        except OSError:
            elapsed = time.monotonic() - started
            return self._infrastructure_result(
                EvaluationStatus.ENVIRONMENT_INVALID,
                "trusted KernelBenchX supervisor could not start",
                elapsed,
                command.private_result_path,
            )
        elapsed = time.monotonic() - started
        if not isinstance(outcome, ProcessOutcome) or outcome.returncode != 0:
            return self._infrastructure_result(
                EvaluationStatus.ENVIRONMENT_INVALID,
                "trusted KernelBenchX supervisor exited unsuccessfully",
                elapsed,
                command.private_result_path,
            )
        try:
            return parse_supervisor_evidence(
                command.private_result_path,
                task=task,
                attempt_id=command.attempt_id,
                candidate_sha256=command.candidate_sha256,
            )
        except SupervisorEvidenceError:
            return self._infrastructure_result(
                EvaluationStatus.ENVIRONMENT_INVALID,
                "trusted KernelBenchX supervisor evidence is invalid",
                elapsed,
                command.private_result_path,
            )

    def build_preflight_command_plan(
        self,
        task: KernelBenchXTask,
        *,
        reference_candidate_manifest: Path,
        adversarial_candidates: Mapping[str, Path],
        private_log_dir: Path,
    ) -> tuple[PreflightCommandPlan, ...]:
        expected_ids = set(ADVERSARIAL_CANARY_IDS)
        actual_ids = set(adversarial_candidates)
        if actual_ids != expected_ids:
            raise ValueError(
                "adversarial candidates must contain exactly wrong, noop, and fake_stdout"
            )
        try:
            from ..kernelbenchx_reference import (
                load_kernelbenchx_reference_canary,
            )

            prepared_reference = load_kernelbenchx_reference_canary(
                reference_candidate_manifest,
                task=task,
            )
        except ValueError as exc:
            raise ValueError(
                "KernelBenchX reference canary manifest violates the formal solution contract"
            ) from exc
        candidate_failures = frozenset(
            {
                EvaluationStatus.COMPILE_FAILED,
                EvaluationStatus.INCORRECT,
                EvaluationStatus.POLICY_REJECTED,
            }
        )
        plans = [
            PreflightCommandPlan(
                canary_id="reference",
                expected_statuses=frozenset({EvaluationStatus.VALID}),
                command=self.prepare_attempt(
                    task,
                    prepared_reference.candidate_path,
                    private_log_dir,
                    canary_id="reference",
                ),
            )
        ]
        for canary_id in ADVERSARIAL_CANARY_IDS:
            expected_statuses = (
                frozenset({EvaluationStatus.INCORRECT})
                if canary_id == "wrong"
                else candidate_failures
            )
            plans.append(
                PreflightCommandPlan(
                    canary_id=canary_id,
                    expected_statuses=expected_statuses,
                    command=self.prepare_attempt(
                        task,
                        adversarial_candidates[canary_id],
                        private_log_dir,
                        canary_id=canary_id,
                    ),
                )
            )
        return tuple(plans)

    @staticmethod
    def _infrastructure_result(
        status_value: EvaluationStatus,
        summary: str,
        elapsed_seconds: float,
        private_result_path: Path,
    ) -> EvaluationResult:
        return EvaluationResult(
            status=status_value,
            compiled=False,
            correct=False,
            error_summary=summary,
            elapsed_seconds=elapsed_seconds,
            gpu_seconds=elapsed_seconds,
            raw_log_path=str(private_result_path),
        )

    @staticmethod
    def _run_subprocess(command: SupervisorCommand) -> ProcessOutcome:
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
        return ProcessOutcome(returncode=process.returncode)
