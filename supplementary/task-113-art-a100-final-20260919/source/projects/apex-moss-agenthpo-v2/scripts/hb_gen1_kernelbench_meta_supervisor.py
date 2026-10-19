#!/usr/bin/env python3
"""Trusted production supervisor for HB-GEN-1 KernelBench meta scoring.

The supervisor never imports candidate code.  It stages the pinned KernelBench
Git tree and a three-file trusted runtime bundle, runs independent CUDA health
sentinels around one restricted candidate process, and accepts evidence only
from an inherited anonymous pipe.  Candidate stdout/stderr, writable output and
cache files are audit-only and never parsed.

The production path is implemented but remains unavailable to formal search
until the separately authorized ten-seat GPU canary passes on the exact code
revision.  ``--capability-report`` is always read-only and never opens a GPU.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
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


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from optimization_lab.harness_builder.adapters.kernel_candidate_invocation import (  # noqa: E402
    KERNEL_INVOCATION_SCHEDULE_SHA256,
)
from optimization_lab.harness_builder.adapters.kernel_candidate_policy import (  # noqa: E402
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
    RestrictedKernelCandidateError,
    RestrictedKernelCandidatePolicy,
)
from optimization_lab.harness_builder.adapters.kernelbench_meta import (  # noqa: E402
    KERNELBENCH_META_EVALUATOR_ID,
    KERNELBENCH_META_CANARY_TASKS,
    KERNELBENCH_META_PROTOCOL_SHA256,
    KERNELBENCH_META_REPOSITORY_COMMIT,
    KERNELBENCH_META_TASK_SET_SHA256,
    KERNELBENCH_META_TASK_HASHES,
)
from optimization_lab.harness_builder.adapters.kernelbench_meta_isolation import (  # noqa: E402
    StagedKernelBenchMetaRuntime,
    build_kernelbench_meta_worker_command,
    kernelbench_meta_scorer_bundle_sha256,
    stage_kernelbench_meta_runtime,
)
from optimization_lab.harness_builder.adapters.kernelbenchx_isolation import (  # noqa: E402
    BubblewrapSpec,
    SandboxContractError,
    StagedWorkerInputs,
    discover_gpu_devices,
    discover_system_roots,
    hash_immutable_tree,
    resolve_trusted_bwrap,
    run_bubblewrap_process,
    stage_git_worker_inputs,
)


KERNELBENCH_META_PYTHON_INCLUDE = Path(
    "/data3/chenzhuofan/moss-hb-gen1/runtime/python3.10-headers-v2"
)
KERNELBENCH_META_PYTHON_INCLUDE_SHA256 = (
    "0487df20daef0d136a9f0e06f48efd1c4bac5ede6cbcab44ed96c6beedfcaa67"
)
_WORKER_TIMEOUT_SECONDS = 560.0
_MAX_SOURCE_BYTES = 2 * 1024 * 1024
_MAX_WORKER_RESULT_BYTES = 32 * 1024
_SHA256 = re.compile(r"[0-9a-f]{64}")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
_AUTHORIZATION_KEYS = {
    "schema_version",
    "authorization_type",
    "scorer_bundle_sha256",
    "protocol_sha256",
    "repository_commit",
    "task_set_sha256",
    "code_revision",
    "ledger_head_sha256",
    "staging_plan_sha256",
    "canary_plan_sha256",
    "canary_ids",
    "max_evaluator_transactions",
    "max_gpu_exclusive_seconds",
    "canary_evidence_sha256",
}

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
_PRIVATE_RESULT_KEYS = {
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


class SupervisorContractError(ValueError):
    """The trusted request, snapshot, worker evidence or isolation differs."""


@dataclass(frozen=True)
class SupervisorRequest:
    repository: Path
    repository_commit: str
    task_id: str
    task_path: str
    task_sha256: str
    candidate: Path
    candidate_sha256: str
    candidate_policy_sha256: str
    invocation_schedule_sha256: str
    scratch_dir: Path
    cache_dir: Path
    private_result: Path
    attempt_id: str
    result_nonce: str
    canary_id: str
    gpu: str
    evaluator: str
    protocol_sha256: str
    scorer_sha256: str
    authorization_receipt: Path | None


@dataclass(frozen=True)
class TrustedWorkerOutcome:
    returncode: int
    timed_out: bool
    quiescent: bool
    elapsed_seconds: float
    evidence: bytes


SnapshotVerifier = Callable[[SupervisorRequest], None]
WorkerExecutor = Callable[[SupervisorRequest, str], TrustedWorkerOutcome]


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _read_regular(path: Path, *, limit: int, label: str) -> bytes:
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
                raise SupervisorContractError(f"{label} changed type")
            raw = stream.read(limit + 1)
    except SupervisorContractError:
        raise
    except OSError as exc:
        raise SupervisorContractError(f"{label} is unreadable") from exc
    if not raw or len(raw) > limit:
        raise SupervisorContractError(f"{label} size is invalid")
    return raw


def validate_request(request: SupervisorRequest) -> bytes:
    expected_task_sha = KERNELBENCH_META_TASK_HASHES.get(request.task_id)
    if (
        expected_task_sha is None
        or request.task_sha256 != expected_task_sha
        or request.task_path != f"KernelBench/{request.task_id}"
    ):
        raise SupervisorContractError("task is outside the frozen six-task binding")
    if (
        request.repository_commit != KERNELBENCH_META_REPOSITORY_COMMIT
        or not _COMMIT.fullmatch(request.repository_commit)
    ):
        raise SupervisorContractError("repository commit differs")
    if request.evaluator != KERNELBENCH_META_EVALUATOR_ID:
        raise SupervisorContractError("evaluator identity differs")
    if request.protocol_sha256 != KERNELBENCH_META_PROTOCOL_SHA256:
        raise SupervisorContractError("protocol binding differs")
    if request.candidate_policy_sha256 != RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256:
        raise SupervisorContractError("candidate policy binding differs")
    if request.invocation_schedule_sha256 != KERNEL_INVOCATION_SCHEDULE_SHA256:
        raise SupervisorContractError("invocation schedule binding differs")
    if request.scorer_sha256 != kernelbench_meta_scorer_bundle_sha256(PROJECT_ROOT):
        raise SupervisorContractError("scorer bundle binding differs")
    for value, label in (
        (request.task_sha256, "task sha256"),
        (request.candidate_sha256, "candidate sha256"),
        (request.result_nonce, "result nonce"),
    ):
        if not _SHA256.fullmatch(value):
            raise SupervisorContractError(f"{label} is invalid")
    if not _SAFE_ID.fullmatch(request.attempt_id) or not _SAFE_ID.fullmatch(
        request.canary_id
    ):
        raise SupervisorContractError("attempt or canary id is unsafe")
    if request.canary_id != "formal":
        expected_canary_task = KERNELBENCH_META_CANARY_TASKS.get(request.canary_id)
        if expected_canary_task is None or expected_canary_task != request.task_id:
            raise SupervisorContractError("canary id/task binding is not frozen")
    if not re.fullmatch(r"[0-9]+", request.gpu):
        raise SupervisorContractError("GPU must be one numeric physical device")

    repository = request.repository.resolve()
    scratch = request.scratch_dir.resolve()
    cache = request.cache_dir.resolve()
    candidate = request.candidate.resolve()
    private = request.private_result.resolve(strict=False)
    if not repository.is_dir() or repository.is_symlink():
        raise SupervisorContractError("repository must be a real directory")
    for path, label in ((scratch, "scratch"), (cache, "cache")):
        if not path.is_dir() or path.is_symlink():
            raise SupervisorContractError(f"{label} must be a real directory")
    if scratch.parent != cache.parent or scratch == cache:
        raise SupervisorContractError("scratch/cache attempt binding differs")
    attempt_root = scratch.parent
    if candidate.parent.parent != attempt_root or candidate.parent.name != "candidate":
        raise SupervisorContractError("candidate is outside the attempt snapshot")
    if any(
        private == root
        or _is_relative_to(private, root)
        or _is_relative_to(root, private.parent)
        for root in (attempt_root, repository)
    ):
        raise SupervisorContractError("private result overlaps worker-visible state")
    if private.exists():
        raise SupervisorContractError("private result already exists")
    if request.authorization_receipt is not None:
        receipt = request.authorization_receipt.resolve()
        if any(
            receipt == root or _is_relative_to(receipt, root)
            for root in (attempt_root, repository)
        ):
            raise SupervisorContractError(
                "authorization receipt overlaps worker-visible state"
            )
    source = _read_regular(candidate, limit=_MAX_SOURCE_BYTES, label="candidate")
    if hashlib.sha256(source).hexdigest() != request.candidate_sha256:
        raise SupervisorContractError("candidate sha256 binding differs")
    RestrictedKernelCandidatePolicy().validate(source, task_id=request.task_id)
    verify_authorization_receipt(request)
    return source


def _git_output(repository: Path, arguments: Sequence[str]) -> str:
    try:
        process = subprocess.run(
            ("git", "-C", str(repository), *arguments),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise SupervisorContractError("cannot inspect frozen KernelBench checkout") from exc
    if process.returncode != 0:
        raise SupervisorContractError("cannot inspect frozen KernelBench checkout")
    return process.stdout.strip()


def verify_authorization_receipt(request: SupervisorRequest) -> str:
    path = request.authorization_receipt
    if path is None:
        raise SupervisorContractError("external evaluator authorization receipt is missing")
    raw = _read_regular(path, limit=64 * 1024, label="authorization receipt")
    receipt_sha = hashlib.sha256(raw).hexdigest()
    if path.name != f"{receipt_sha}.json":
        raise SupervisorContractError("authorization receipt is not content addressed")
    payload = _json_object(raw, keys=_AUTHORIZATION_KEYS)
    canonical = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    if raw != canonical:
        raise SupervisorContractError("authorization receipt is not canonical JSON")
    expected = {
        "schema_version": 1,
        "scorer_bundle_sha256": request.scorer_sha256,
        "protocol_sha256": request.protocol_sha256,
        "repository_commit": request.repository_commit,
        "task_set_sha256": KERNELBENCH_META_TASK_SET_SHA256,
        "canary_ids": list(KERNELBENCH_META_CANARY_TASKS),
        "max_evaluator_transactions": 10,
        "max_gpu_exclusive_seconds": 6000,
    }
    for key, value in expected.items():
        if payload[key] != value or type(payload[key]) is not type(value):
            raise SupervisorContractError(f"authorization {key} binding differs")
    if type(payload["code_revision"]) is not str or not _COMMIT.fullmatch(
        payload["code_revision"]
    ):
        raise SupervisorContractError("authorization code_revision is invalid")
    if type(payload["ledger_head_sha256"]) is not str or not _SHA256.fullmatch(
        payload["ledger_head_sha256"]
    ):
        raise SupervisorContractError("authorization ledger_head_sha256 is invalid")
    for key in ("staging_plan_sha256", "canary_plan_sha256"):
        if type(payload[key]) is not str or not _SHA256.fullmatch(payload[key]):
            raise SupervisorContractError(f"authorization {key} is invalid")
    current_revision = _git_output(PROJECT_ROOT, ("rev-parse", "HEAD"))
    if payload["code_revision"] != current_revision:
        raise SupervisorContractError("authorization code revision differs")
    if _git_output(PROJECT_ROOT, ("status", "--porcelain", "--untracked-files=no")):
        raise SupervisorContractError("trusted scorer checkout is dirty")
    authorization_type = payload["authorization_type"]
    evidence = payload["canary_evidence_sha256"]
    if request.canary_id == "formal":
        if authorization_type != "hb-gen1-kernelbench-meta-formal-v1":
            raise SupervisorContractError("formal activation receipt type differs")
        if type(evidence) is not str or not _SHA256.fullmatch(evidence):
            raise SupervisorContractError("formal activation lacks canary evidence")
    else:
        if authorization_type != "hb-gen1-kernelbench-meta-canary-v1":
            raise SupervisorContractError("canary authorization receipt type differs")
        if evidence is not None:
            raise SupervisorContractError("canary authorization cannot preclaim evidence")
        if payload["ledger_head_sha256"] != "0" * 64:
            raise SupervisorContractError("canary authorization ledger head differs")
    return receipt_sha


def verify_frozen_snapshot(request: SupervisorRequest) -> None:
    repository = request.repository.resolve()
    if _git_output(repository, ("rev-parse", "HEAD")) != request.repository_commit:
        raise SupervisorContractError("KernelBench commit differs")
    if _git_output(repository, ("status", "--porcelain", "--untracked-files=no")):
        raise SupervisorContractError("KernelBench tracked checkout is dirty")
    task_source = _read_regular(
        repository / request.task_path,
        limit=_MAX_SOURCE_BYTES,
        label="frozen task",
    )
    if hashlib.sha256(task_source).hexdigest() != request.task_sha256:
        raise SupervisorContractError("frozen task sha256 differs")


def _prepare_worker_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=False, mode=0o700)
    # The host attempt root is 0700.  These child mounts must be writable by
    # uid 65534 only after entering its private user/mount namespace.
    path.chmod(0o777)


def _read_pipe(fd: int) -> bytes:
    chunks: list[bytes] = []
    total = 0
    while True:
        block = os.read(fd, min(4096, _MAX_WORKER_RESULT_BYTES + 1 - total))
        if not block:
            break
        chunks.append(block)
        total += len(block)
        if total > _MAX_WORKER_RESULT_BYTES:
            raise SupervisorContractError("private worker evidence is too large")
    return b"".join(chunks)


def _input_seed_nonce(request: SupervisorRequest) -> str:
    return hmac.new(
        bytes.fromhex(request.result_nonce),
        (
            "HB-GEN-1-KERNELBENCH-INPUT-SECRET-V1\0"
            + request.task_id
            + "\0"
            + request.candidate_sha256
        ).encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def _private_result_pipe() -> tuple[int, int]:
    """Return ``(read_fd, worker_fd3)`` without clobbering an existing fd 3."""

    try:
        os.fstat(3)
    except OSError:
        pass
    else:
        raise SupervisorContractError("trusted result descriptor 3 is unavailable")
    read_fd, write_fd = os.pipe2(getattr(os, "O_CLOEXEC", 0))
    if read_fd != 3:
        os.close(read_fd)
        os.close(write_fd)
        raise SupervisorContractError("trusted pipe allocation was not canonical")
    saved_read = os.dup(read_fd)
    os.close(read_fd)
    try:
        os.dup2(write_fd, 3, inheritable=True)
    finally:
        os.close(write_fd)
    return saved_read, 3


class ProductionWorkerExecutor:
    """Stage once, then run pre-health/candidate/post-health in isolated groups."""

    def __init__(self, request: SupervisorRequest) -> None:
        self.request = request
        self.inputs: StagedWorkerInputs = stage_git_worker_inputs(
            repository=request.repository.resolve(),
            commit=request.repository_commit,
            candidate=request.candidate.resolve(),
            staging_root=request.scratch_dir.resolve() / "supervisor-input",
        )
        self.runtime: StagedKernelBenchMetaRuntime = stage_kernelbench_meta_runtime(
            project_root=PROJECT_ROOT,
            staging_root=request.scratch_dir.resolve() / "trusted-runtime",
        )
        self.bwrap = resolve_trusted_bwrap()
        self.system_roots = discover_system_roots()
        self.gpu_devices = discover_gpu_devices(request.gpu)
        if hash_immutable_tree(KERNELBENCH_META_PYTHON_INCLUDE) != (
            KERNELBENCH_META_PYTHON_INCLUDE_SHA256
        ):
            raise SupervisorContractError("Python header snapshot digest differs")

    def __call__(self, request: SupervisorRequest, phase: str) -> TrustedWorkerOutcome:
        if request is not self.request or phase not in {
            "pre-health",
            "candidate",
            "post-health",
        }:
            raise SupervisorContractError("worker execution phase differs")
        phase_root = request.scratch_dir.resolve() / phase
        output = phase_root / "untrusted-output"
        work = phase_root / "work"
        cache = request.cache_dir.resolve() / phase
        for path in (output, work, cache):
            _prepare_worker_directory(path)
        for path in (
            work / "home",
            work / "tmp",
            cache / "xdg",
            cache / "uv",
            cache / "triton",
            cache / "torch_extensions",
            cache / "torchinductor",
            cache / "cuda",
            cache / "pycache",
        ):
            _prepare_worker_directory(path)

        read_fd, write_fd = _private_result_pipe()
        try:
            if phase == "candidate":
                arguments = (
                    "--repository",
                    "/sandbox/repository",
                    "--repository-commit",
                    request.repository_commit,
                    "--task-id",
                    request.task_id,
                    "--task-sha256",
                    request.task_sha256,
                    "--candidate",
                    "/sandbox/input/candidate.py",
                    "--candidate-sha256",
                    request.candidate_sha256,
                    "--candidate-policy-sha256",
                    request.candidate_policy_sha256,
                    "--schedule-sha256",
                    request.invocation_schedule_sha256,
                    "--protocol-sha256",
                    request.protocol_sha256,
                    "--scorer-sha256",
                    request.scorer_sha256,
                    "--evaluator",
                    request.evaluator,
                    "--attempt-id",
                    request.attempt_id,
                    "--result-nonce",
                    request.result_nonce,
                    "--input-seed-nonce",
                    _input_seed_nonce(request),
                )
            else:
                arguments = ("--health-only",)
            command = build_kernelbench_meta_worker_command(
                spec=BubblewrapSpec(
                    bwrap_path=self.bwrap,
                    repository_snapshot=self.inputs.repository_snapshot,
                    candidate_snapshot=self.inputs.candidate_snapshot,
                    output_dir=output,
                    worker_tmp_dir=work,
                    cache_dir=cache,
                    python_prefix=Path(sys.prefix).absolute(),
                    python_executable=Path(sys.executable).absolute(),
                    python_include=KERNELBENCH_META_PYTHON_INCLUDE,
                    python_include_sha256=KERNELBENCH_META_PYTHON_INCLUDE_SHA256,
                    gpu=request.gpu,
                    system_roots=tuple(self.system_roots),
                    gpu_devices=tuple(self.gpu_devices),
                ),
                runtime=self.runtime,
                result_fd=write_fd,
                worker_arguments=arguments,
            )
            isolated = run_bubblewrap_process(
                command.launch,
                stdout_path=phase_root / "worker.stdout",
                stderr_path=phase_root / "worker.stderr",
                timeout_seconds=_WORKER_TIMEOUT_SECONDS,
                pass_fds=(write_fd,),
            )
        finally:
            try:
                os.close(write_fd)
            except OSError:
                pass
        try:
            evidence = _read_pipe(read_fd)
        finally:
            os.close(read_fd)
        return TrustedWorkerOutcome(
            returncode=isolated.returncode,
            timed_out=isolated.timed_out,
            quiescent=isolated.quiescent,
            elapsed_seconds=isolated.elapsed_seconds,
            evidence=evidence,
        )


def _strict_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise SupervisorContractError(f"duplicate worker JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> object:
    raise SupervisorContractError(f"non-finite worker JSON constant: {value}")


def _json_object(raw: bytes, *, keys: set[str]) -> dict[str, object]:
    if not raw or len(raw) > _MAX_WORKER_RESULT_BYTES:
        raise SupervisorContractError("private worker evidence size is invalid")
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_strict_object,
            parse_constant=_reject_constant,
        )
    except SupervisorContractError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SupervisorContractError("private worker evidence is malformed") from exc
    if not isinstance(payload, dict) or set(payload) != keys:
        raise SupervisorContractError("private worker evidence schema differs")
    return payload


def _parse_health(outcome: TrustedWorkerOutcome) -> str:
    if outcome.timed_out or not outcome.quiescent or outcome.returncode != 0:
        raise SupervisorContractError("isolated health worker did not complete")
    payload = _json_object(
        outcome.evidence, keys={"schema_version", "status", "hardware"}
    )
    if payload["schema_version"] != 1 or payload["status"] != "passed":
        raise SupervisorContractError("isolated health result differs")
    hardware = payload["hardware"]
    if type(hardware) is not str or "A100" not in hardware or len(hardware) > 256:
        raise SupervisorContractError("isolated health hardware differs")
    return hardware


def _finite_optional(payload: Mapping[str, object], key: str) -> float | None:
    value = payload[key]
    if value is None:
        return None
    if type(value) not in (int, float):
        raise SupervisorContractError(f"{key} must be numeric")
    result = float(value)
    if not math.isfinite(result) or result <= 0:
        raise SupervisorContractError(f"{key} must be finite and positive")
    return result


def _parse_candidate(
    request: SupervisorRequest, outcome: TrustedWorkerOutcome
) -> dict[str, object]:
    if outcome.timed_out or not outcome.quiescent or outcome.returncode != 0:
        raise SupervisorContractError("isolated candidate worker did not complete")
    payload = _json_object(outcome.evidence, keys=_WORKER_RESULT_KEYS)
    expected = {
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
        "candidate_policy_sha256": request.candidate_policy_sha256,
        "schedule_sha256": request.invocation_schedule_sha256,
        "health_probe": "passed",
        "correctness_trials": 5,
        "timing_trials": 100,
    }
    for key, value in expected.items():
        if payload[key] != value or type(payload[key]) is not type(value):
            raise SupervisorContractError(f"worker {key} binding differs")
    if payload["input_schedule_sha256"] is not None and (
        type(payload["input_schedule_sha256"]) is not str
        or not _SHA256.fullmatch(payload["input_schedule_sha256"])
    ):
        raise SupervisorContractError("worker input schedule binding differs")
    if type(payload["compiled"]) is not bool or type(payload["correct"]) is not bool:
        raise SupervisorContractError("worker status flags differ")
    for key, maximum in (
        ("correctness_passed", 5),
        ("timing_trials_completed", 100),
        ("timing_outputs_correct", 100),
    ):
        value = payload[key]
        if type(value) is not int or not 0 <= value <= maximum:
            raise SupervisorContractError("worker protocol counts differ")
    if payload["timing_outputs_correct"] > payload["timing_trials_completed"]:
        raise SupervisorContractError("worker timing counts differ")
    candidate_ms = _finite_optional(payload, "candidate_runtime_ms")
    reference_ms = _finite_optional(payload, "reference_runtime_ms")
    status = payload["status"]
    if status not in {
        "valid",
        "compile_failed",
        "incorrect",
        "policy_rejected",
        "environment_invalid",
    }:
        raise SupervisorContractError("worker status differs")
    if status == "valid":
        if (
            not payload["compiled"]
            or not payload["correct"]
            or payload["correctness_passed"] != 5
            or payload["timing_trials_completed"] != 100
            or payload["timing_outputs_correct"] != 100
            or candidate_ms is None
            or reference_ms is None
            or payload["input_schedule_sha256"] is None
        ):
            raise SupervisorContractError("valid worker result is incomplete")
    elif payload["correct"] or candidate_ms is not None or reference_ms is not None:
        raise SupervisorContractError("failed worker result exposes a score")
    error = payload["error_summary"]
    hardware = payload["hardware"]
    if type(error) is not str or len(error) > 2_000:
        raise SupervisorContractError("worker error summary differs")
    if type(hardware) is not str or "A100" not in hardware or len(hardware) > 256:
        raise SupervisorContractError("worker hardware binding differs")
    return payload


def _payload(
    request: SupervisorRequest,
    *,
    status: str,
    health_probe: str,
    compiled: bool,
    correct: bool,
    correctness_passed: int,
    timing_completed: int,
    timing_correct: int,
    candidate_runtime_ms: float | None,
    reference_runtime_ms: float | None,
    error_summary: str,
    elapsed_seconds: float,
    hardware: str,
    input_schedule_sha256: str | None = None,
) -> dict[str, object]:
    elapsed = max(0.0, float(elapsed_seconds))
    result: dict[str, object] = {
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
        "candidate_policy_sha256": request.candidate_policy_sha256,
        "schedule_sha256": request.invocation_schedule_sha256,
        "input_schedule_sha256": input_schedule_sha256,
        "status": status,
        "health_probe": health_probe,
        "compiled": compiled,
        "correct": correct,
        "correctness_trials": 5,
        "correctness_passed": correctness_passed,
        "timing_trials": 100,
        "timing_trials_completed": timing_completed,
        "timing_outputs_correct": timing_correct,
        "candidate_runtime_ms": candidate_runtime_ms,
        "reference_runtime_ms": reference_runtime_ms,
        "error_summary": " ".join(error_summary.split())[:2_000],
        "elapsed_seconds": elapsed,
        "gpu_seconds": elapsed,
        "hardware": " ".join(hardware.split())[:256],
    }
    if set(result) != _PRIVATE_RESULT_KEYS:
        raise AssertionError("private result schema drift")
    return result


def _atomic_write_private(path: Path, payload: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.exists():
        raise SupervisorContractError("private result already exists")
    encoded = json.dumps(
        payload,
        allow_nan=False,
        ensure_ascii=False,
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
    worker_executor: WorkerExecutor | None = None,
) -> dict[str, object]:
    source = validate_request(request)
    del source
    snapshot_verifier(request)
    executor = worker_executor or ProductionWorkerExecutor(request)
    elapsed = 0.0
    try:
        pre = executor(request, "pre-health")
        elapsed += pre.elapsed_seconds
        hardware = _parse_health(pre)
    except Exception:
        payload = _payload(
            request,
            status="environment_invalid",
            health_probe="failed",
            compiled=False,
            correct=False,
            correctness_passed=0,
            timing_completed=0,
            timing_correct=0,
            candidate_runtime_ms=None,
            reference_runtime_ms=None,
            error_summary="isolated pre-execution health probe failed",
            elapsed_seconds=elapsed,
            hardware="",
        )
        _atomic_write_private(request.private_result, payload)
        return payload

    candidate = executor(request, "candidate")
    elapsed += candidate.elapsed_seconds
    try:
        snapshot_verifier(request)
    except Exception as exc:
        raise SupervisorContractError("frozen snapshot changed during evaluation") from exc
    post = executor(request, "post-health")
    elapsed += post.elapsed_seconds
    try:
        post_hardware = _parse_health(post)
    except Exception:
        payload = _payload(
            request,
            status="environment_invalid",
            health_probe="failed",
            compiled=False,
            correct=False,
            correctness_passed=0,
            timing_completed=0,
            timing_correct=0,
            candidate_runtime_ms=None,
            reference_runtime_ms=None,
            error_summary="isolated post-execution health probe failed",
            elapsed_seconds=elapsed,
            hardware=hardware,
        )
    else:
        if post_hardware != hardware:
            raise SupervisorContractError("pre/post health hardware differs")
        if candidate.timed_out:
            payload = _payload(
                request,
                status="timeout",
                health_probe="passed",
                compiled=False,
                correct=False,
                correctness_passed=0,
                timing_completed=0,
                timing_correct=0,
                candidate_runtime_ms=None,
                reference_runtime_ms=None,
                error_summary="isolated candidate worker timed out",
                elapsed_seconds=elapsed,
                hardware=hardware,
            )
        elif not candidate.quiescent:
            payload = _payload(
                request,
                status="environment_invalid",
                health_probe="failed",
                compiled=False,
                correct=False,
                correctness_passed=0,
                timing_completed=0,
                timing_correct=0,
                candidate_runtime_ms=None,
                reference_runtime_ms=None,
                error_summary="candidate process group did not become quiescent",
                elapsed_seconds=elapsed,
                hardware=hardware,
            )
        else:
            try:
                evidence = _parse_candidate(request, candidate)
            except SupervisorContractError:
                # Independent post-health succeeded: missing/forged evidence is
                # candidate-scoped and cannot pause peer cells as an environment
                # failure or mint any timing.
                payload = _payload(
                    request,
                    status="compile_failed",
                    health_probe="passed",
                    compiled=False,
                    correct=False,
                    correctness_passed=0,
                    timing_completed=0,
                    timing_correct=0,
                    candidate_runtime_ms=None,
                    reference_runtime_ms=None,
                    error_summary="candidate worker produced no trusted evidence",
                    elapsed_seconds=elapsed,
                    hardware=hardware,
                    input_schedule_sha256=None,
                )
            else:
                status = str(evidence["status"])
                if status == "environment_invalid":
                    status = "compile_failed"
                payload = _payload(
                    request,
                    status=status,
                    health_probe="passed",
                    compiled=bool(evidence["compiled"]) if status != "compile_failed" else False,
                    correct=bool(evidence["correct"]) if status == "valid" else False,
                    correctness_passed=int(evidence["correctness_passed"]),
                    timing_completed=int(evidence["timing_trials_completed"]),
                    timing_correct=int(evidence["timing_outputs_correct"]),
                    candidate_runtime_ms=(
                        float(evidence["candidate_runtime_ms"])
                        if status == "valid"
                        else None
                    ),
                    reference_runtime_ms=(
                        float(evidence["reference_runtime_ms"])
                        if status == "valid"
                        else None
                    ),
                    error_summary=str(evidence["error_summary"]),
                    elapsed_seconds=elapsed,
                    hardware=hardware,
                    input_schedule_sha256=(
                        str(evidence["input_schedule_sha256"])
                        if evidence["input_schedule_sha256"] is not None
                        else None
                    ),
                )
    _atomic_write_private(request.private_result, payload)
    return payload


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capability-report", action="store_true")
    parser.add_argument("--repository", type=Path)
    parser.add_argument("--repository-commit")
    parser.add_argument("--task-id")
    parser.add_argument("--task-path")
    parser.add_argument("--task-sha256")
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--candidate-sha256")
    parser.add_argument("--candidate-policy-sha256")
    parser.add_argument("--invocation-schedule-sha256")
    parser.add_argument("--scratch-dir", type=Path)
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--private-result", type=Path)
    parser.add_argument("--attempt-id")
    parser.add_argument("--result-nonce")
    parser.add_argument("--canary-id")
    parser.add_argument("--gpu")
    parser.add_argument("--evaluator")
    parser.add_argument("--protocol-sha256")
    parser.add_argument("--scorer-sha256")
    parser.add_argument("--authorization-receipt", type=Path)
    return parser


def _request(namespace: argparse.Namespace) -> SupervisorRequest:
    fields = {
        "repository": namespace.repository,
        "repository_commit": namespace.repository_commit,
        "task_id": namespace.task_id,
        "task_path": namespace.task_path,
        "task_sha256": namespace.task_sha256,
        "candidate": namespace.candidate,
        "candidate_sha256": namespace.candidate_sha256,
        "candidate_policy_sha256": namespace.candidate_policy_sha256,
        "invocation_schedule_sha256": namespace.invocation_schedule_sha256,
        "scratch_dir": namespace.scratch_dir,
        "cache_dir": namespace.cache_dir,
        "private_result": namespace.private_result,
        "attempt_id": namespace.attempt_id,
        "result_nonce": namespace.result_nonce,
        "canary_id": namespace.canary_id,
        "gpu": namespace.gpu,
        "evaluator": namespace.evaluator,
        "protocol_sha256": namespace.protocol_sha256,
        "scorer_sha256": namespace.scorer_sha256,
        "authorization_receipt": namespace.authorization_receipt,
    }
    if any(value is None for value in fields.values()):
        raise SupervisorContractError("supervisor arguments are incomplete")
    return SupervisorRequest(**fields)  # type: ignore[arg-type]


def capability_report(candidate: Path | None, task_id: str | None) -> dict[str, object]:
    policy_state = "not_requested"
    if candidate is not None:
        try:
            if task_id is None:
                raise RestrictedKernelCandidateError("task binding is required")
            RestrictedKernelCandidatePolicy().validate_path(candidate, task_id=task_id)
        except RestrictedKernelCandidateError:
            policy_state = "rejected"
        else:
            policy_state = "accepted"
    return {
        "schema_version": 1,
        "component": "hb-gen1-kernelbench-meta-supervisor",
        "repository_commit": KERNELBENCH_META_REPOSITORY_COMMIT,
        "candidate_invocation_abi": "restricted_torch_cuda_runtime_v1",
        "candidate_policy_sha256": RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
        "protocol_sha256": KERNELBENCH_META_PROTOCOL_SHA256,
        "scorer_bundle_sha256": kernelbench_meta_scorer_bundle_sha256(PROJECT_ROOT),
        "legacy_stdout_parser_allowed": False,
        "legacy_same_process_scorer_allowed": False,
        "trusted_invocation_loop_implemented": True,
        "production_runtime_implemented": True,
        "gpu_or_candidate_execution": False,
        "execution_ready": False,
        "blocker": "kernelbench_meta_canary_pending",
        "canary_authorization_receipt_required": True,
        "formal_activation_receipt_required": True,
        "frozen_canary_ids": list(KERNELBENCH_META_CANARY_TASKS),
        "candidate_policy_check": policy_state,
    }


def main(argv: Sequence[str] | None = None) -> int:
    namespace = _parser().parse_args(argv)
    if namespace.capability_report:
        print(
            json.dumps(
                capability_report(namespace.candidate, namespace.task_id),
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 78
    try:
        run_supervisor(_request(namespace))
    except (
        RestrictedKernelCandidateError,
        SandboxContractError,
        SupervisorContractError,
        OSError,
    ):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "ProductionWorkerExecutor",
    "SupervisorContractError",
    "SupervisorRequest",
    "TrustedWorkerOutcome",
    "capability_report",
    "run_supervisor",
    "validate_request",
    "verify_frozen_snapshot",
]
