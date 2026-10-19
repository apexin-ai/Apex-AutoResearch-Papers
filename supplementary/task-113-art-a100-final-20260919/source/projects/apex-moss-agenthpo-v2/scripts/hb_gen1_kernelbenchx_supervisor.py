#!/usr/bin/env python3
"""Trusted, stdout-independent KernelBenchX supervisor for HB-GEN-1.

The outer adapter invokes this file with ``python -I``.  Candidate stdout and
stderr are written only below the per-attempt scratch directory.  The sole
machine-readable result is atomically written by this supervisor to a private
path that is never delegated to the official candidate pipeline.

This is intentionally a narrow wrapper around the frozen KernelBenchX
``call -> execution -> performance`` pipeline.  It recomputes the score from
the exact performance rows and the pinned A100 golden rows, and accepts timing
only when the same candidate/task binding passed call and execution checks.
"""

from __future__ import annotations

import argparse
import ast
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
from typing import Callable, Mapping, Sequence


# ``python -I`` deliberately removes the checkout from sys.path.  Add only the
# immutable parent of this trusted script; never add cwd, PYTHONPATH, candidate
# roots, or worker output roots.
_TRUSTED_PROJECT_ROOT = Path(__file__).resolve(strict=True).parent.parent
if str(_TRUSTED_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_TRUSTED_PROJECT_ROOT))

from optimization_lab.harness_builder.adapters.kernelbenchx_isolation import (  # noqa: E402
    BubblewrapCommand,
    BubblewrapSpec,
    SandboxContractError,
    StagedWorkerInputs,
    build_bubblewrap_command,
    discover_gpu_devices,
    discover_system_roots,
    resolve_trusted_bwrap,
    run_bubblewrap_process,
    stage_git_worker_inputs,
)


KERNELBENCHX_REPOSITORY_COMMIT = "fd4192293bf9a8c645327a9d46aa1e807f1f9cf2"
KERNELBENCHX_DATASET_COMMIT = KERNELBENCHX_REPOSITORY_COMMIT
KERNELBENCHX_EVALUATOR_ID = "kernelbenchx-call-exe-perf"
KERNELBENCHX_PYTHON_INCLUDE = Path(
    "/data3/chenzhuofan/moss-hb-gen1/runtime/python3.10-headers-v2"
)
KERNELBENCHX_PYTHON_INCLUDE_SHA256 = (
    "0487df20daef0d136a9f0e06f48efd1c4bac5ede6cbcab44ed96c6beedfcaa67"
)
KERNELBENCHX_TASK_HASHES: Mapping[str, str] = {
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

_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_RESULT_KEYS = {
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
_MAX_CANDIDATE_BYTES = 2 * 1024 * 1024
_MAX_METRICS_BYTES = 16 * 1024 * 1024
_PIPELINE_TIMEOUT_SECONDS = 560.0


class SupervisorContractError(ValueError):
    """The trusted invocation or frozen evaluator snapshot is invalid."""


class OfficialEvidenceError(ValueError):
    """The official pipeline did not emit exact, internally consistent facts."""


@dataclass(frozen=True)
class SupervisorRequest:
    repository: Path
    repository_commit: str
    dataset_commit: str
    task_id: str
    task_path: str
    task_sha256: str
    candidate: Path
    candidate_sha256: str
    scratch_dir: Path
    cache_dir: Path
    private_result: Path
    attempt_id: str
    canary_id: str
    gpu: str
    evaluator: str

    def to_argv(self) -> list[str]:
        values = (
            ("--repository", self.repository),
            ("--repository-commit", self.repository_commit),
            ("--dataset-commit", self.dataset_commit),
            ("--task-id", self.task_id),
            ("--task-path", self.task_path),
            ("--task-sha256", self.task_sha256),
            ("--candidate", self.candidate),
            ("--candidate-sha256", self.candidate_sha256),
            ("--scratch-dir", self.scratch_dir),
            ("--cache-dir", self.cache_dir),
            ("--private-result", self.private_result),
            ("--attempt-id", self.attempt_id),
            ("--canary-id", self.canary_id),
            ("--gpu", self.gpu),
            ("--evaluator", self.evaluator),
        )
        argv: list[str] = []
        for flag, value in values:
            argv.extend((flag, str(value)))
        return argv


@dataclass(frozen=True)
class OfficialPipelineOutcome:
    returncode: int
    elapsed_seconds: float
    hardware: str
    metrics_path: Path
    error_summary: str = ""
    timed_out: bool = False
    quiescent: bool = True


@dataclass(frozen=True)
class BoundMetrics:
    call_ok: bool
    exe_ok: bool
    perf_ok: bool
    candidate_runtime_ms: float | None
    reference_runtime_ms: float | None


SnapshotVerifier = Callable[[SupervisorRequest], None]
PipelineExecutor = Callable[[SupervisorRequest, Path], OfficialPipelineOutcome]


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _regular_file_bytes(path: Path, *, limit: int, label: str) -> bytes:
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise SupervisorContractError(f"{label} is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise SupervisorContractError(f"{label} must be a regular non-symlink file")
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise SupervisorContractError(f"{label} must be a regular file")
            value = stream.read(limit + 1)
    except OSError as exc:
        raise SupervisorContractError(f"cannot read {label}") from exc
    if len(value) > limit:
        raise SupervisorContractError(f"{label} is too large")
    return value


def _strict_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise OfficialEvidenceError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> object:
    raise OfficialEvidenceError(f"non-finite JSON constant: {value}")


def _read_exact_json(path: Path, *, limit: int) -> object:
    try:
        raw = _regular_file_bytes(path, limit=limit, label="official JSON")
    except SupervisorContractError as exc:
        raise OfficialEvidenceError("official JSON is missing or unsafe") from exc
    try:
        return json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_strict_object,
            parse_constant=_reject_constant,
        )
    except OfficialEvidenceError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise OfficialEvidenceError("official JSON is malformed") from exc


def _finite_positive(value: object, label: str) -> float:
    if type(value) not in (int, float):
        raise OfficialEvidenceError(f"{label} must be numeric")
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise OfficialEvidenceError(f"{label} must be finite and positive")
    return number


def validate_request(request: SupervisorRequest) -> bytes:
    if request.repository_commit != KERNELBENCHX_REPOSITORY_COMMIT:
        raise SupervisorContractError("repository commit differs from the frozen pin")
    if request.dataset_commit != KERNELBENCHX_DATASET_COMMIT:
        raise SupervisorContractError("dataset commit differs from the frozen pin")
    if not _COMMIT.fullmatch(request.repository_commit) or not _COMMIT.fullmatch(
        request.dataset_commit
    ):
        raise SupervisorContractError("invalid frozen commit")
    expected_task_sha = KERNELBENCHX_TASK_HASHES.get(request.task_id)
    if expected_task_sha is None:
        raise SupervisorContractError("task is not in the frozen HB-GEN-1 set")
    if request.task_path != f"data/kernelbenchx/{request.task_id}":
        raise SupervisorContractError("task path differs from the frozen binding")
    if request.task_sha256 != expected_task_sha:
        raise SupervisorContractError("task sha256 differs from the frozen binding")
    if request.evaluator != KERNELBENCHX_EVALUATOR_ID:
        raise SupervisorContractError("evaluator identity differs")
    if not _SAFE_ID.fullmatch(request.attempt_id) or not _SAFE_ID.fullmatch(
        request.canary_id
    ):
        raise SupervisorContractError("unsafe attempt or canary id")
    if not re.fullmatch(r"[0-9]+", request.gpu):
        raise SupervisorContractError("GPU must be one numeric device id")
    if not _SHA256.fullmatch(request.candidate_sha256):
        raise SupervisorContractError("invalid candidate sha256")

    repository = request.repository.resolve()
    scratch = request.scratch_dir.resolve()
    cache = request.cache_dir.resolve()
    candidate = request.candidate.resolve()
    private_result = request.private_result.resolve(strict=False)
    if not repository.is_dir() or repository.is_symlink():
        raise SupervisorContractError("repository must be a real directory")
    for path, label in ((scratch, "scratch"), (cache, "cache")):
        if not path.is_dir() or path.is_symlink():
            raise SupervisorContractError(f"{label} must be a real directory")
    if scratch == cache or _is_relative_to(scratch, cache) or _is_relative_to(cache, scratch):
        raise SupervisorContractError("scratch and cache roots must be disjoint")
    if scratch.parent != cache.parent:
        raise SupervisorContractError("scratch and cache must share one attempt root")
    if not _is_relative_to(candidate, scratch / "candidate"):
        raise SupervisorContractError("candidate must be the frozen scratch snapshot")
    if (
        _is_relative_to(private_result, scratch)
        or _is_relative_to(private_result, cache)
        or _is_relative_to(scratch, private_result.parent)
        or _is_relative_to(cache, private_result.parent)
    ):
        raise SupervisorContractError(
            "private result must not overlap candidate-controlled roots"
        )
    if private_result.exists():
        raise SupervisorContractError("private result already exists")

    candidate_bytes = _regular_file_bytes(
        candidate, limit=_MAX_CANDIDATE_BYTES, label="candidate"
    )
    if hashlib.sha256(candidate_bytes).hexdigest() != request.candidate_sha256:
        raise SupervisorContractError("candidate sha256 binding differs")
    try:
        source = candidate_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SupervisorContractError("candidate is not UTF-8 Python") from exc
    return candidate_bytes


def _static_candidate_failure(
    request: SupervisorRequest, candidate_bytes: bytes
) -> tuple[str, str] | None:
    source = candidate_bytes.decode("utf-8")
    try:
        tree = ast.parse(source, filename=request.candidate.name)
    except SyntaxError:
        return "compile_failed", "candidate Python does not parse"
    entrypoint = Path(request.task_id).stem
    functions = {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    if not ({entrypoint, "kernel_function"} & functions):
        return "policy_rejected", "candidate lacks the frozen task entrypoint"
    return None


def _git_output(repository: Path, argv: Sequence[str]) -> str:
    try:
        process = subprocess.run(
            ["git", "-C", str(repository), *argv],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise SupervisorContractError("cannot inspect frozen repository") from exc
    if process.returncode != 0:
        raise SupervisorContractError("cannot inspect frozen repository")
    return process.stdout.strip()


def verify_frozen_snapshot(request: SupervisorRequest) -> None:
    repository = request.repository.resolve()
    commit = _git_output(repository, ("rev-parse", "HEAD"))
    if commit != request.repository_commit:
        raise SupervisorContractError("repository commit differs from the frozen pin")
    dirty = _git_output(
        repository, ("status", "--porcelain", "--untracked-files=no")
    )
    if dirty:
        raise SupervisorContractError("tracked KernelBenchX checkout is dirty")
    task_bytes = _regular_file_bytes(
        repository / request.task_path,
        limit=_MAX_CANDIDATE_BYTES,
        label="frozen task",
    )
    if hashlib.sha256(task_bytes).hexdigest() != request.task_sha256:
        raise SupervisorContractError("frozen task sha256 differs")
    required = (
        repository / "scripts/run_eval_from_files.sh",
        repository / "EVAL/0_call_acc.py",
        repository / "EVAL/1_exe_acc.py",
        repository / "EVAL/2_efficiency.py",
        repository / "EVAL/unified_results.py",
        repository / "metrics/run_bench/write_file.py",
        repository / "metrics/run_bench/multiprocess_gpu_run.py",
        repository
        / "metrics/golden_results/a100"
        / f"{Path(request.task_id).stem}.json",
    )
    for path in required:
        _regular_file_bytes(path, limit=_MAX_METRICS_BYTES, label="frozen evaluator file")


def _python_runtime() -> tuple[Path, Path]:
    return Path(sys.prefix).absolute(), Path(sys.executable).absolute()


def _prepare_worker_writable_directory(path: Path, *, create: bool) -> None:
    if create:
        path.mkdir(parents=True, exist_ok=False, mode=0o700)
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise SupervisorContractError("worker writable directory is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
        raise SupervisorContractError("worker writable root must be a real directory")
    # These roots are world-writable only behind the attempt root's 0700 host
    # boundary.  Inside the user namespace this permits uid 65534 to write.
    path.chmod(0o777)


def _prepare_official_launch(
    request: SupervisorRequest,
    *,
    staged_inputs: StagedWorkerInputs | None = None,
    bwrap_path: Path | None = None,
    python_prefix: Path | None = None,
    python_executable: Path | None = None,
    python_include: Path | None = None,
    python_include_sha256: str | None = None,
    system_roots: Sequence[Path] | None = None,
    gpu_devices: Sequence[Path] | None = None,
) -> tuple[BubblewrapCommand, Path]:
    if bwrap_path is None:
        bwrap_path = resolve_trusted_bwrap()
    if python_prefix is None or python_executable is None:
        default_prefix, default_executable = _python_runtime()
        python_prefix = python_prefix or default_prefix
        python_executable = python_executable or default_executable
    if python_include is None:
        python_include = KERNELBENCHX_PYTHON_INCLUDE
    if python_include_sha256 is None:
        python_include_sha256 = KERNELBENCHX_PYTHON_INCLUDE_SHA256
    if system_roots is None:
        system_roots = discover_system_roots()
    if gpu_devices is None:
        gpu_devices = discover_gpu_devices(request.gpu)
    sensitive_paths = (
        request.repository.resolve(),
        request.private_result.resolve(strict=False),
        request.private_result.parent.resolve(strict=False),
    )
    mounted_runtime_roots = tuple(path.resolve() for path in system_roots) + (
        python_prefix.resolve(),
        python_include.resolve(),
    )
    for sensitive in sensitive_paths:
        if any(
            sensitive == root
            or _is_relative_to(sensitive, root)
            or _is_relative_to(root, sensitive)
            for root in mounted_runtime_roots
        ):
            raise SupervisorContractError(
                "worker runtime mount overlaps a trusted host path"
            )

    output_dir = request.scratch_dir.resolve() / "official"
    worker_tmp_dir = request.scratch_dir.resolve() / "worker-tmp"
    _prepare_worker_writable_directory(output_dir, create=True)
    _prepare_worker_writable_directory(worker_tmp_dir, create=True)
    _prepare_worker_writable_directory(request.cache_dir.resolve(), create=False)
    for path in (
        worker_tmp_dir / "home",
        worker_tmp_dir / "tmp",
        request.cache_dir / "xdg",
        request.cache_dir / "uv",
        request.cache_dir / "triton",
        request.cache_dir / "torch_extensions",
        request.cache_dir / "torchinductor",
        request.cache_dir / "cuda",
        request.cache_dir / "pycache",
    ):
        if path.exists():
            _prepare_worker_writable_directory(path, create=False)
        else:
            _prepare_worker_writable_directory(path, create=True)

    if staged_inputs is None:
        staged_inputs = stage_git_worker_inputs(
            repository=request.repository.resolve(),
            commit=request.repository_commit,
            candidate=request.candidate.resolve(),
            staging_root=request.scratch_dir.resolve() / "supervisor-input",
        )
    launch = build_bubblewrap_command(
        BubblewrapSpec(
            bwrap_path=bwrap_path,
            repository_snapshot=staged_inputs.repository_snapshot.absolute(),
            candidate_snapshot=staged_inputs.candidate_snapshot.absolute(),
            output_dir=output_dir,
            worker_tmp_dir=worker_tmp_dir,
            cache_dir=request.cache_dir.resolve(),
            python_prefix=python_prefix.absolute(),
            python_executable=python_executable.absolute(),
            python_include=python_include.absolute(),
            python_include_sha256=python_include_sha256,
            gpu=request.gpu,
            system_roots=tuple(system_roots),
            gpu_devices=tuple(gpu_devices),
        )
    )
    return launch, output_dir


def build_official_command(
    request: SupervisorRequest,
    *,
    staged_inputs: StagedWorkerInputs | None = None,
    bwrap_path: Path | None = None,
    python_prefix: Path | None = None,
    python_executable: Path | None = None,
    python_include: Path | None = None,
    python_include_sha256: str | None = None,
    system_roots: Sequence[Path] | None = None,
    gpu_devices: Sequence[Path] | None = None,
) -> tuple[tuple[str, ...], dict[str, str], Path]:
    launch, output_dir = _prepare_official_launch(
        request,
        staged_inputs=staged_inputs,
        bwrap_path=bwrap_path,
        python_prefix=python_prefix,
        python_executable=python_executable,
        python_include=python_include,
        python_include_sha256=python_include_sha256,
        system_roots=system_roots,
        gpu_devices=gpu_devices,
    )
    return launch.argv, launch.host_environment, output_dir


def _hardware_probe(gpu: str, environment: Mapping[str, str]) -> str:
    try:
        process = subprocess.run(
            [
                "nvidia-smi",
                f"--id={gpu}",
                "--query-gpu=name",
                "--format=csv,noheader",
            ],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            env=dict(environment),
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return ""
    value = " ".join(process.stdout.split())[:256]
    return value if process.returncode == 0 else ""


def execute_official_pipeline(
    request: SupervisorRequest, output_dir: Path
) -> OfficialPipelineOutcome:
    launch, expected_output = _prepare_official_launch(request)
    if output_dir.resolve() != expected_output.resolve():
        raise SupervisorContractError("official output directory binding differs")
    stdout_path = request.scratch_dir / "candidate-pipeline.stdout"
    stderr_path = request.scratch_dir / "candidate-pipeline.stderr"
    hardware = _hardware_probe(request.gpu, launch.host_environment)
    isolated = run_bubblewrap_process(
        launch,
        stdout_path=stdout_path,
        stderr_path=stderr_path,
        timeout_seconds=_PIPELINE_TIMEOUT_SECONDS,
    )
    return OfficialPipelineOutcome(
        returncode=isolated.returncode,
        elapsed_seconds=isolated.elapsed_seconds,
        hardware=hardware,
        metrics_path=output_dir / "metrics.json",
        error_summary=(
            "official KernelBenchX pipeline timed out"
            if isolated.timed_out
            else (
                "official KernelBenchX worker did not become quiescent"
                if not isolated.quiescent
                else "official KernelBenchX pipeline did not complete"
            )
        ),
        timed_out=isolated.timed_out,
        quiescent=isolated.quiescent,
    )


def _golden_rows(request: SupervisorRequest) -> list[object]:
    golden_path = (
        request.repository
        / "metrics/golden_results/a100"
        / f"{Path(request.task_id).stem}.json"
    )
    payload = _read_exact_json(golden_path, limit=_MAX_METRICS_BYTES)
    if not isinstance(payload, list) or not payload:
        raise OfficialEvidenceError("A100 golden result must be a nonempty list")
    return payload


def parse_bound_metrics(
    request: SupervisorRequest, metrics_path: Path
) -> BoundMetrics:
    payload = _read_exact_json(metrics_path, limit=_MAX_METRICS_BYTES)
    if not isinstance(payload, dict) or set(payload) != {request.task_id}:
        raise OfficialEvidenceError("metrics must contain exactly the bound task")
    row = payload[request.task_id]
    if not isinstance(row, dict):
        raise OfficialEvidenceError("bound task metrics must be an object")
    for key in ("file", "call_ok", "exe_ok", "perf_ok", "runtime_ms", "performance"):
        if key not in row:
            raise OfficialEvidenceError(f"missing bound metric: {key}")
    if row["file"] != request.task_id:
        raise OfficialEvidenceError("metric task binding differs")
    for key in ("call_ok", "exe_ok", "perf_ok"):
        if type(row[key]) is not bool:
            raise OfficialEvidenceError(f"{key} must be boolean")
    call_ok = row["call_ok"]
    exe_ok = row["exe_ok"]
    perf_ok = row["perf_ok"]
    if exe_ok and not call_ok:
        raise OfficialEvidenceError("execution success without call success")
    if perf_ok and not (call_ok and exe_ok):
        raise OfficialEvidenceError("performance success without correctness")
    if not perf_ok:
        return BoundMetrics(call_ok, exe_ok, False, None, None)

    performance = row["performance"]
    golden = _golden_rows(request)
    if not isinstance(performance, list) or not performance:
        raise OfficialEvidenceError("successful timing requires performance rows")
    if len(performance) != len(golden):
        raise OfficialEvidenceError("candidate and A100 golden row counts differ")
    candidate_sum = 0.0
    reference_sum = 0.0
    for index, (candidate_row, reference_row) in enumerate(zip(performance, golden)):
        if not isinstance(candidate_row, dict) or not isinstance(reference_row, dict):
            raise OfficialEvidenceError("performance rows must be objects")
        candidate_sum += _finite_positive(candidate_row.get("ms"), f"candidate ms[{index}]")
        reference_sum += _finite_positive(reference_row.get("ms"), f"reference ms[{index}]")
        candidate_input = candidate_row.get("input_size")
        reference_input = reference_row.get("input_size")
        if (candidate_input is not None or reference_input is not None) and (
            candidate_input != reference_input
        ):
            raise OfficialEvidenceError("candidate and reference input rows differ")
    candidate_runtime = round(candidate_sum, 4)
    summary_runtime = _finite_positive(row["runtime_ms"], "runtime_ms")
    if not math.isclose(
        candidate_runtime, summary_runtime, rel_tol=1e-7, abs_tol=5e-5
    ):
        raise OfficialEvidenceError("summary runtime is not bound to performance rows")
    return BoundMetrics(
        call_ok=True,
        exe_ok=True,
        perf_ok=True,
        candidate_runtime_ms=candidate_runtime,
        reference_runtime_ms=reference_sum,
    )


def _result_payload(
    request: SupervisorRequest,
    *,
    status_value: str,
    compiled: bool,
    correct: bool,
    candidate_runtime_ms: float | None,
    reference_runtime_ms: float | None,
    error_summary: str,
    elapsed_seconds: float,
    hardware: str,
) -> dict[str, object]:
    elapsed = max(0.0, float(elapsed_seconds))
    payload: dict[str, object] = {
        "schema_version": 1,
        "evaluator": request.evaluator,
        "attempt_id": request.attempt_id,
        "repository_commit": request.repository_commit,
        "dataset_commit": request.dataset_commit,
        "task_id": request.task_id,
        "task_sha256": request.task_sha256,
        "candidate_sha256": request.candidate_sha256,
        "status": status_value,
        "compiled": compiled,
        "correct": correct,
        "candidate_runtime_ms": candidate_runtime_ms,
        "reference_runtime_ms": reference_runtime_ms,
        "reference_compile_runtime_ms": None,
        "error_summary": " ".join(error_summary.split())[:2_000],
        "elapsed_seconds": elapsed,
        "gpu_seconds": elapsed,
        "hardware": " ".join(hardware.split())[:256],
    }
    if set(payload) != _RESULT_KEYS:
        raise AssertionError("trusted result schema drift")
    return payload


def _atomic_write_private(path: Path, payload: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.exists():
        raise SupervisorContractError("private result already exists")
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    temporary = path.parent / f".{path.name}.{uuid.uuid4().hex}.tmp"
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        path.chmod(0o600)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def run_supervisor(
    request: SupervisorRequest,
    *,
    snapshot_verifier: SnapshotVerifier = verify_frozen_snapshot,
    pipeline_executor: PipelineExecutor = execute_official_pipeline,
) -> dict[str, object]:
    candidate_bytes = validate_request(request)
    snapshot_verifier(request)
    static_failure = _static_candidate_failure(request, candidate_bytes)
    if static_failure is not None:
        status_value, summary = static_failure
        payload = _result_payload(
            request,
            status_value=status_value,
            compiled=False,
            correct=False,
            candidate_runtime_ms=None,
            reference_runtime_ms=None,
            error_summary=summary,
            elapsed_seconds=0.0,
            hardware="",
        )
        _atomic_write_private(request.private_result, payload)
        return payload
    output_dir = request.scratch_dir.resolve() / "official"
    outcome = pipeline_executor(request, output_dir)
    try:
        snapshot_verifier(request)
    except Exception as exc:
        raise SupervisorContractError(
            "frozen snapshot changed during candidate execution"
        ) from exc
    if not isinstance(outcome, OfficialPipelineOutcome):
        raise SupervisorContractError("pipeline executor returned an invalid outcome")
    if not outcome.quiescent:
        payload = _result_payload(
            request,
            status_value="environment_invalid",
            compiled=False,
            correct=False,
            candidate_runtime_ms=None,
            reference_runtime_ms=None,
            error_summary="trusted KernelBenchX worker did not become quiescent",
            elapsed_seconds=outcome.elapsed_seconds,
            hardware=outcome.hardware,
        )
    elif outcome.timed_out:
        payload = _result_payload(
            request,
            status_value="timeout",
            compiled=False,
            correct=False,
            candidate_runtime_ms=None,
            reference_runtime_ms=None,
            error_summary="trusted KernelBenchX pipeline timed out",
            elapsed_seconds=outcome.elapsed_seconds,
            hardware=outcome.hardware,
        )
    elif outcome.returncode != 0:
        payload = _result_payload(
            request,
            status_value="environment_invalid",
            compiled=False,
            correct=False,
            candidate_runtime_ms=None,
            reference_runtime_ms=None,
            error_summary="trusted KernelBenchX pipeline failed out of band",
            elapsed_seconds=outcome.elapsed_seconds,
            hardware=outcome.hardware,
        )
    else:
        try:
            metrics = parse_bound_metrics(request, outcome.metrics_path)
        except OfficialEvidenceError:
            payload = _result_payload(
                request,
                status_value="environment_invalid",
                compiled=False,
                correct=False,
                candidate_runtime_ms=None,
                reference_runtime_ms=None,
                error_summary="trusted KernelBenchX metrics are missing or inconsistent",
                elapsed_seconds=outcome.elapsed_seconds,
                hardware=outcome.hardware,
            )
        else:
            if not metrics.call_ok:
                status_value, compiled, correct, error = (
                    "compile_failed",
                    False,
                    False,
                    "candidate failed the trusted call/compile stage",
                )
            elif not metrics.exe_ok:
                status_value, compiled, correct, error = (
                    "incorrect",
                    True,
                    False,
                    "candidate failed trusted execution correctness",
                )
            elif not metrics.perf_ok:
                status_value, compiled, correct, error = (
                    "environment_invalid",
                    False,
                    False,
                    "trusted performance evidence is unavailable",
                )
            else:
                status_value, compiled, correct, error = "valid", True, True, ""
            payload = _result_payload(
                request,
                status_value=status_value,
                compiled=compiled,
                correct=correct,
                candidate_runtime_ms=metrics.candidate_runtime_ms,
                reference_runtime_ms=metrics.reference_runtime_ms,
                error_summary=error,
                elapsed_seconds=outcome.elapsed_seconds,
                hardware=outcome.hardware,
            )
    _atomic_write_private(request.private_result, payload)
    return payload


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--repository-commit", required=True)
    parser.add_argument("--dataset-commit", required=True)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--task-path", required=True)
    parser.add_argument("--task-sha256", required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--candidate-sha256", required=True)
    parser.add_argument("--scratch-dir", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--private-result", type=Path, required=True)
    parser.add_argument("--attempt-id", required=True)
    parser.add_argument("--canary-id", required=True)
    parser.add_argument("--gpu", required=True)
    parser.add_argument("--evaluator", required=True)
    return parser


def _request_from_namespace(namespace: argparse.Namespace) -> SupervisorRequest:
    return SupervisorRequest(
        repository=namespace.repository,
        repository_commit=namespace.repository_commit,
        dataset_commit=namespace.dataset_commit,
        task_id=namespace.task_id,
        task_path=namespace.task_path,
        task_sha256=namespace.task_sha256,
        candidate=namespace.candidate,
        candidate_sha256=namespace.candidate_sha256,
        scratch_dir=namespace.scratch_dir,
        cache_dir=namespace.cache_dir,
        private_result=namespace.private_result,
        attempt_id=namespace.attempt_id,
        canary_id=namespace.canary_id,
        gpu=namespace.gpu,
        evaluator=namespace.evaluator,
    )


def main(argv: Sequence[str] | None = None) -> int:
    request = _request_from_namespace(_parser().parse_args(argv))
    try:
        run_supervisor(
            request,
            snapshot_verifier=verify_frozen_snapshot,
            pipeline_executor=execute_official_pipeline,
        )
    except (
        SupervisorContractError,
        OfficialEvidenceError,
        SandboxContractError,
        OSError,
    ):
        # No raw exception text is printed because this process is launched with
        # candidate-adjacent environment and the adapter treats nonzero as an
        # out-of-band environment failure.
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
