"""Root-owned stage supervisor embedded in each HB-GEN-1 SWE-Perf image.

This module intentionally uses only the Python standard library.  The image
entrypoint runs it as uid 0; repository test commands run as the fixed uid
65534 worker.  Worker stdout/stderr are connected to ``/dev/null`` and never
participate in a verdict.  The only controller-visible verdict is an atomic,
owner-only JSON file in the private Docker volume.

The currently frozen upstream topology is not runnable: arbitrary candidate
Python and the pytest JSON reporter share one uid-65534 process, so neither the
report nor its exit status can be trusted.  ``require_trusted_result_channel``
therefore rejects every stage before spawning a worker.  The remaining code is
retained only as the frozen legacy control-flow specification for a future,
separately authorized out-of-process oracle; it cannot mint a score today.

The supervisor is deliberately strict and generic.  Task-specific command
argv, expected test ids and the digest-pinned upstream image are supplied by the
baked ``task-manifest.json``.  A wrapper image is not runnable until that
manifest has been generated from the private, frozen SWE-Perf row and the image
has passed the external adapter canaries.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path, PurePosixPath
from statistics import median
from typing import Any, Callable, Mapping, Sequence

if __package__:
    from .trusted_result import (
        UnattestableCandidateOutcome,
        require_trusted_result_channel,
    )
else:  # Embedded image import: /opt/hb-sweperf/lib is placed on sys.path.
    from trusted_result import (  # type: ignore[no-redef]
        UnattestableCandidateOutcome,
        require_trusted_result_channel,
    )


MANIFEST_PATH = Path("/opt/hb-sweperf/task-manifest.json")
MANIFEST_SHA256_PATH = Path("/opt/hb-sweperf/task-manifest.sha256")
REQUEST_PATH = Path("/run/hb-private/request.json")
PRIVATE_ROOT = Path("/run/hb-private")
WORK_ROOT = Path("/hb/work")
CACHE_ROOT = Path("/hb/cache")
WORKER_UID = 65534
RESULT_SCHEMA_VERSION = 1
PERFORMANCE_REPETITIONS = 20
MAX_JSON_BYTES = 1024 * 1024
MAX_PATCH_BYTES = 1024 * 1024

_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:+-]{0,159}\Z")
_IMAGE_REF = re.compile(r"[^\s@]+@sha256:[0-9a-f]{64}\Z")
_BINDING_KEYS = {
    "attempt_id",
    "instance_id",
    "repository",
    "evaluator",
    "evaluator_commit",
    "dataset_commit",
    "dataset_parquet_sha256",
    "base_commit",
    "task_sha256",
    "image_ref",
    "patch_apply_mode",
    "patch_sha256",
}
_REQUEST_KEYS = {
    "schema_version",
    "binding",
    "stage",
    "result_nonce",
    "correctness_receipt",
    "candidate_path",
    "scratch_path",
    "cache_path",
}
_TASK_KEYS = {
    "schema_version",
    "instance_id",
    "repository",
    "base_commit",
    "task_sha256",
    "evaluator",
    "evaluator_commit",
    "dataset_commit",
    "dataset_parquet_sha256",
    "patch_apply_mode",
    "upstream_image_ref",
    "repository_path",
    "allowed_patch_paths",
    "correctness",
    "performance",
    "worker_uid",
    "resource_limits",
}


class SupervisorContractError(RuntimeError):
    """Trusted image/request/state does not satisfy the frozen schema."""


class CandidatePolicyViolation(RuntimeError):
    """Candidate-controlled bytes or processes crossed a declared boundary."""


class QuiescenceViolation(CandidatePolicyViolation):
    """A worker process remained alive after its bounded command returned."""


class PatchApplyFailure(CandidatePolicyViolation):
    """The canonical patch cannot be applied exactly at the frozen base."""


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON value {value!r}")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _canonical_bytes(value: Mapping[str, Any]) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("ascii")


def canonical_sha256(value: Mapping[str, Any]) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _load_json(path: Path, *, max_bytes: int = MAX_JSON_BYTES) -> dict[str, Any]:
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise SupervisorContractError(f"missing JSON contract: {path}") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise SupervisorContractError("JSON contract must be a regular non-symlink")
    if metadata.st_size <= 0 or metadata.st_size > max_bytes:
        raise SupervisorContractError("JSON contract size is outside the bound")
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    with os.fdopen(descriptor, "rb") as stream:
        raw = stream.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise SupervisorContractError("JSON contract exceeds the byte bound")
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise SupervisorContractError("JSON contract is not strict UTF-8 JSON") from exc
    if not isinstance(payload, dict):
        raise SupervisorContractError("JSON contract must be an object")
    return payload


def _atomic_bytes(path: Path, payload: bytes, *, mode: int) -> None:
    if not path.parent.exists():
        path.parent.mkdir(parents=True, mode=0o700)
    if not path.parent.is_dir() or path.parent.is_symlink():
        raise SupervisorContractError("private result parent is unavailable")
    if path.exists() or path.is_symlink():
        raise SupervisorContractError("private result path already exists")
    descriptor, name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, mode, follow_symlinks=False)
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def atomic_private_result(path: Path, payload: Mapping[str, Any]) -> str:
    """Write one canonical root-only verdict and return its canonical digest."""

    digest = canonical_sha256(payload)
    _atomic_bytes(path, _canonical_bytes(payload) + b"\n", mode=0o600)
    return digest


def correctness_receipt(
    *,
    task_manifest_sha256: str,
    request_binding: Mapping[str, Any],
    correctness_nonce: str,
    patch_sha256: str,
    candidate_state_sha256: str,
    correctness_evidence_sha256: str,
) -> str:
    values = (
        task_manifest_sha256,
        correctness_nonce,
        patch_sha256,
        candidate_state_sha256,
        correctness_evidence_sha256,
    )
    if any(not isinstance(value, str) or not _SHA256.fullmatch(value) for value in values):
        raise ValueError("correctness receipt inputs must be SHA-256 values")
    if not isinstance(request_binding, Mapping) or not request_binding:
        raise ValueError("correctness receipt requires a request binding")
    return canonical_sha256(
        {
            "schema_version": 1,
            "domain": "hb-gen1-sweperf-correctness-receipt",
            "task_manifest_sha256": task_manifest_sha256,
            "request_binding": dict(request_binding),
            "correctness_nonce": correctness_nonce,
            "patch_sha256": patch_sha256,
            "candidate_state_sha256": candidate_state_sha256,
            "correctness_evidence_sha256": correctness_evidence_sha256,
        }
    )


def enforce_worker_quiescence(
    *,
    worker_pids: Callable[[], Sequence[int]],
    kill_pid: Callable[[int], None],
    wait_once: Callable[[], None],
    max_rounds: int = 5,
) -> None:
    """Require true worker quiescence; observing a leftover is itself a failure.

    Residual processes are killed before returning control, but the stage still
    fails closed even when cleanup succeeds.  This prevents a candidate from
    gaining a timing advantage by leaving work behind for a later stage.
    """

    if isinstance(max_rounds, bool) or not isinstance(max_rounds, int) or max_rounds <= 0:
        raise ValueError("max_rounds must be a positive integer")
    observed = False
    for _ in range(max_rounds):
        values = tuple(worker_pids())
        if not values:
            if observed:
                raise QuiescenceViolation("worker was not quiescent at command exit")
            return
        observed = True
        for pid in values:
            if isinstance(pid, bool) or not isinstance(pid, int) or pid <= 0:
                raise SupervisorContractError("worker process table returned an unsafe pid")
            try:
                kill_pid(pid)
            except ProcessLookupError:
                pass
        wait_once()
    raise QuiescenceViolation("worker was not quiescent after forced cleanup")


def exact_apply_argv(
    *, git_binary: str, patch_path: str, check: bool
) -> tuple[str, ...]:
    if not PurePosixPath(git_binary).is_absolute() or not PurePosixPath(
        patch_path
    ).is_absolute():
        raise ValueError("git and patch paths must be absolute")
    common = (git_binary, "apply")
    if check:
        return (*common, "--check", "--whitespace=error-all", patch_path)
    return (*common, "--whitespace=error-all", patch_path)


def _worker_pids() -> tuple[int, ...]:
    values: list[int] = []
    own_pid = os.getpid()
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        if pid == own_pid:
            continue
        try:
            status = (entry / "status").read_text(encoding="ascii")
        except (OSError, UnicodeDecodeError):
            continue
        match = re.search(r"^Uid:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)$", status, re.M)
        if match is not None and int(match.group(2)) == WORKER_UID:
            values.append(pid)
    return tuple(sorted(values))


def _kill_worker(pid: int) -> None:
    os.kill(pid, signal.SIGKILL)


def _wait_for_kill() -> None:
    time.sleep(0.05)


def _require_keys(payload: Mapping[str, Any], expected: set[str], label: str) -> None:
    if set(payload) != expected:
        raise SupervisorContractError(f"{label} fields differ")


def _load_manifest() -> tuple[dict[str, Any], str]:
    manifest = _load_json(MANIFEST_PATH)
    _require_keys(manifest, _TASK_KEYS, "task manifest")
    raw = MANIFEST_PATH.read_bytes()
    observed = hashlib.sha256(raw).hexdigest()
    try:
        expected = MANIFEST_SHA256_PATH.read_text(encoding="ascii").strip()
    except OSError as exc:
        raise SupervisorContractError("task manifest digest file is unavailable") from exc
    if not _SHA256.fullmatch(expected) or observed != expected:
        raise SupervisorContractError("task manifest content hash differs")
    if manifest.get("schema_version") != 1:
        raise SupervisorContractError("task manifest schema changed")
    if manifest.get("worker_uid") != WORKER_UID:
        raise SupervisorContractError("task manifest worker uid changed")
    if manifest.get("repository_path") != "/testbed":
        raise SupervisorContractError("task manifest repository path changed")
    if manifest.get("resource_limits") != {
        "cpus": 10,
        "memory_bytes": 32 * 1024**3,
        "pids": 512,
    }:
        raise SupervisorContractError("task manifest resource limits changed")
    return manifest, observed


def _load_request(manifest: Mapping[str, Any]) -> dict[str, Any]:
    request = _load_json(REQUEST_PATH)
    _require_keys(request, _REQUEST_KEYS, "stage request")
    if request.get("schema_version") != RESULT_SCHEMA_VERSION:
        raise SupervisorContractError("stage request schema changed")
    binding = request.get("binding")
    if not isinstance(binding, dict):
        raise SupervisorContractError("stage request binding must be an object")
    _require_keys(binding, _BINDING_KEYS, "attempt binding")
    expected = {
        "instance_id": manifest["instance_id"],
        "repository": manifest["repository"],
        "evaluator": manifest["evaluator"],
        "evaluator_commit": manifest["evaluator_commit"],
        "dataset_commit": manifest["dataset_commit"],
        "dataset_parquet_sha256": manifest["dataset_parquet_sha256"],
        "base_commit": manifest["base_commit"],
        "task_sha256": manifest["task_sha256"],
        "patch_apply_mode": manifest["patch_apply_mode"],
    }
    if any(binding.get(key) != value for key, value in expected.items()):
        raise SupervisorContractError("stage request differs from the task manifest")
    if not isinstance(binding.get("attempt_id"), str) or not _SAFE_ID.fullmatch(
        binding["attempt_id"]
    ):
        raise SupervisorContractError("unsafe attempt id")
    if not isinstance(binding.get("image_ref"), str) or not _IMAGE_REF.fullmatch(
        binding["image_ref"]
    ):
        raise SupervisorContractError("wrapper image is not digest pinned")
    if not isinstance(binding.get("patch_sha256"), str) or not _SHA256.fullmatch(
        binding["patch_sha256"]
    ):
        raise SupervisorContractError("patch hash is invalid")
    if request.get("stage") not in {"correctness", "performance"}:
        raise SupervisorContractError("unknown evaluator stage")
    if not isinstance(request.get("result_nonce"), str) or not _SHA256.fullmatch(
        request["result_nonce"]
    ):
        raise SupervisorContractError("result nonce is invalid")
    if request.get("candidate_path") != "/hb/work/candidate.patch":
        raise SupervisorContractError("candidate path changed")
    if request.get("scratch_path") != "/hb/work" or request.get("cache_path") != "/hb/cache":
        raise SupervisorContractError("scratch/cache path changed")
    receipt = request.get("correctness_receipt")
    if request["stage"] == "correctness":
        if receipt is not None:
            raise SupervisorContractError("correctness request cannot carry a receipt")
    elif not isinstance(receipt, str) or not _SHA256.fullmatch(receipt):
        raise SupervisorContractError("performance request lacks a correctness receipt")
    return request


def _read_frozen_patch(request: Mapping[str, Any], manifest: Mapping[str, Any]) -> Path:
    source = Path(request["candidate_path"])
    try:
        metadata = source.lstat()
    except OSError as exc:
        raise CandidatePolicyViolation("candidate patch is unavailable") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise CandidatePolicyViolation("candidate patch must be a regular file")
    if metadata.st_size <= 0 or metadata.st_size > MAX_PATCH_BYTES:
        raise CandidatePolicyViolation("candidate patch size is outside the bound")
    descriptor = os.open(source, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    with os.fdopen(descriptor, "rb") as stream:
        raw = stream.read(MAX_PATCH_BYTES + 1)
    if hashlib.sha256(raw).hexdigest() != request["binding"]["patch_sha256"]:
        raise CandidatePolicyViolation("candidate patch changed after binding")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise CandidatePolicyViolation("candidate patch is not UTF-8") from exc
    if not text.startswith("diff --git ") or not text.endswith("\n"):
        raise CandidatePolicyViolation("candidate patch is not canonical unified diff")
    paths: list[str] = []
    for line in text.splitlines():
        if not line.startswith("diff --git "):
            continue
        match = re.fullmatch(r"diff --git a/([^\s]+) b/([^\s]+)", line)
        if match is None or match.group(1) != match.group(2):
            raise CandidatePolicyViolation("candidate patch contains an unsafe file header")
        paths.append(match.group(1))
    allowed = set(manifest["allowed_patch_paths"])
    if not paths or len(paths) != len(set(paths)) or not set(paths).issubset(allowed):
        raise CandidatePolicyViolation("candidate patch exceeds the allowed file set")
    destination = PRIVATE_ROOT / f"candidate-{request['binding']['patch_sha256']}.patch"
    if destination.exists():
        current = destination.read_bytes()
        if current != raw:
            raise SupervisorContractError("private candidate snapshot differs")
    else:
        _atomic_bytes(destination, raw, mode=0o400)
    return destination


def _run_trusted(
    argv: Sequence[str], *, cwd: Path, timeout: float, check: bool = False
) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(
        tuple(argv),
        cwd=cwd,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
        env={"PATH": "/usr/bin:/bin"},
    )
    if check and result.returncode != 0:
        raise SupervisorContractError("trusted repository operation failed")
    return result


def _chown_tree(path: Path, uid: int) -> None:
    for root, directories, files in os.walk(path, topdown=False, followlinks=False):
        for name in files:
            candidate = Path(root) / name
            if not candidate.is_symlink():
                os.chown(candidate, uid, uid, follow_symlinks=False)
        for name in directories:
            candidate = Path(root) / name
            if not candidate.is_symlink():
                os.chown(candidate, uid, uid, follow_symlinks=False)
    os.chown(path, uid, uid, follow_symlinks=False)


def _freeze_tree(path: Path) -> None:
    """Make the pristine reference readable/executable but never worker-writable."""

    for root, directories, files in os.walk(path, topdown=False, followlinks=False):
        for name in files:
            candidate = Path(root) / name
            if candidate.is_symlink():
                continue
            executable = bool(candidate.stat(follow_symlinks=False).st_mode & 0o111)
            os.chown(candidate, 0, 0, follow_symlinks=False)
            os.chmod(candidate, 0o555 if executable else 0o444, follow_symlinks=False)
        for name in directories:
            candidate = Path(root) / name
            if not candidate.is_symlink():
                os.chown(candidate, 0, 0, follow_symlinks=False)
                os.chmod(candidate, 0o555, follow_symlinks=False)
    os.chown(path, 0, 0, follow_symlinks=False)
    os.chmod(path, 0o555, follow_symlinks=False)


def _prepare_repositories(manifest: Mapping[str, Any], patch_path: Path) -> tuple[Path, Path]:
    source = Path(manifest["repository_path"])
    if source.resolve(strict=True) != Path("/testbed"):
        raise SupervisorContractError("upstream repository path changed")
    runtime = WORK_ROOT / "runtime"
    if runtime.exists() or runtime.is_symlink():
        raise SupervisorContractError("attempt runtime already exists")
    runtime.mkdir(mode=0o700)
    reference = runtime / "reference"
    candidate = runtime / "candidate"
    shutil.copytree(source, reference, symlinks=True)
    shutil.copytree(source, candidate, symlinks=True)
    for repository in (reference, candidate):
        observed = _run_trusted(
            ("/usr/bin/git", "rev-parse", "HEAD"),
            cwd=repository,
            timeout=30,
            check=True,
        ).stdout.decode("ascii", errors="strict").strip()
        if observed != manifest["base_commit"]:
            raise SupervisorContractError("upstream repository HEAD differs")
    checked = _run_trusted(
        exact_apply_argv(
            git_binary="/usr/bin/git", patch_path=str(patch_path), check=True
        ),
        cwd=candidate,
        timeout=30,
    )
    if checked.returncode != 0:
        raise PatchApplyFailure("git apply --check rejected the candidate")
    applied = _run_trusted(
        exact_apply_argv(
            git_binary="/usr/bin/git", patch_path=str(patch_path), check=False
        ),
        cwd=candidate,
        timeout=30,
    )
    if applied.returncode != 0:
        raise PatchApplyFailure("exact git apply rejected the candidate")
    # The candidate uid can execute the reference workload but cannot mutate the
    # reference tree to manufacture a larger speedup denominator.
    _freeze_tree(reference)
    _chown_tree(candidate, WORKER_UID)
    os.chmod(runtime, 0o555)
    return reference, candidate


def _candidate_state_sha256(candidate: Path, manifest_sha256: str) -> str:
    diff = _run_trusted(
        ("/usr/bin/git", "diff", "--binary", "--no-ext-diff", "--full-index"),
        cwd=candidate,
        timeout=30,
        check=True,
    ).stdout
    return canonical_sha256(
        {
            "manifest_sha256": manifest_sha256,
            "base_commit": _run_trusted(
                ("/usr/bin/git", "rev-parse", "HEAD"),
                cwd=candidate,
                timeout=30,
                check=True,
            ).stdout.decode("ascii", errors="strict").strip(),
            "tracked_diff_sha256": hashlib.sha256(diff).hexdigest(),
        }
    )


def _drop_to_worker() -> None:
    os.setgroups([])
    os.setgid(WORKER_UID)
    os.setuid(WORKER_UID)
    os.umask(0o077)
    os.setsid()


def _render_command(argv: Sequence[str], report_path: Path) -> tuple[str, ...]:
    rendered = tuple(item.replace("{report_path}", str(report_path)) for item in argv)
    if any("{" in item or "}" in item for item in rendered):
        raise SupervisorContractError("stage command contains an unresolved placeholder")
    return rendered


def _run_worker_command(
    command: Mapping[str, Any], *, repository: Path, report_path: Path
) -> tuple[int, dict[str, tuple[str, float]]]:
    # The current upstream pytest process both executes arbitrary candidate
    # Python and authors the JSON/exit status.  Parsing those bytes under uid 0
    # after process exit does not attest them.  Keep the legacy implementation
    # below unreachable until a separately frozen trusted oracle replaces it.
    require_trusted_result_channel()
    report_path.unlink(missing_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True, mode=0o777)
    os.chmod(report_path.parent, 0o777)
    environment = {
        "HOME": str(CACHE_ROOT / "home"),
        "PATH": "/opt/miniconda3/bin:/usr/local/bin:/usr/bin:/bin",
        "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
        "TMPDIR": str(CACHE_ROOT / "tmp"),
        "NO_PROXY": "*",
        "no_proxy": "*",
    }
    for directory in (Path(environment["HOME"]), Path(environment["TMPDIR"])):
        directory.mkdir(parents=True, exist_ok=True, mode=0o777)
        os.chmod(directory, 0o777)
    try:
        result = subprocess.run(
            _render_command(command["argv"], report_path),
            cwd=repository,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=float(command["timeout_seconds"]),
            check=False,
            env=environment,
            preexec_fn=_drop_to_worker,
        )
    finally:
        enforce_worker_quiescence(
            worker_pids=_worker_pids,
            kill_pid=_kill_worker,
            wait_once=_wait_for_kill,
        )
    report = _load_json(report_path)
    if "tests" not in report or not isinstance(report["tests"], list):
        raise CandidatePolicyViolation("test report schema differs")
    tests: dict[str, tuple[str, float]] = {}
    for item in report["tests"]:
        if not isinstance(item, dict):
            raise CandidatePolicyViolation("test report item is not an object")
        try:
            nodeid = item["nodeid"]
            outcome = item["outcome"]
            duration = item["call"]["duration"]
        except (KeyError, TypeError) as exc:
            raise CandidatePolicyViolation("test report item fields differ") from exc
        if (
            not isinstance(nodeid, str)
            or not nodeid
            or nodeid in tests
            or outcome not in {"passed", "failed", "error", "skipped"}
            or isinstance(duration, bool)
            or not isinstance(duration, (int, float))
            or not math.isfinite(float(duration))
            or duration <= 0
        ):
            raise CandidatePolicyViolation("test report item is invalid")
        tests[nodeid] = (outcome, float(duration))
    expected = tuple(command["expected_test_ids"])
    if set(tests) != set(expected) or len(tests) != len(expected):
        raise CandidatePolicyViolation("test report ids differ from the frozen manifest")
    return result.returncode, tests


def _common_result(request: Mapping[str, Any], *, elapsed: float) -> dict[str, Any]:
    return {
        "schema_version": RESULT_SCHEMA_VERSION,
        **dict(request["binding"]),
        "result_nonce": request["result_nonce"],
        "stage": request["stage"],
        "status": "error",
        "failure_kind": "evaluator_error",
        "elapsed_seconds": max(0.0, float(elapsed)),
    }


def _write_correctness(
    request: Mapping[str, Any], manifest: Mapping[str, Any], manifest_sha: str
) -> dict[str, Any]:
    started = time.monotonic()
    common = _common_result(request, elapsed=0.0)
    try:
        patch = _read_frozen_patch(request, manifest)
        reference, candidate = _prepare_repositories(manifest, patch)
    except PatchApplyFailure:
        return {
            **common,
            "status": "failed",
            "failure_kind": "patch_apply_failed",
            "elapsed_seconds": time.monotonic() - started,
            "patch_applied": False,
            "tests_passed": 0,
            "tests_total": 0,
            "correctness_receipt": None,
        }
    except CandidatePolicyViolation:
        return {
            **common,
            "status": "failed",
            "failure_kind": "policy_violation",
            "elapsed_seconds": time.monotonic() - started,
            "patch_applied": False,
            "tests_passed": 0,
            "tests_total": 0,
            "correctness_receipt": None,
        }

    state_before = _candidate_state_sha256(candidate, manifest_sha)
    try:
        returncode, report = _run_worker_command(
            manifest["correctness"],
            repository=candidate,
            report_path=CACHE_ROOT / "reports" / "correctness.json",
        )
    except CandidatePolicyViolation:
        return {
            **common,
            "status": "failed",
            "failure_kind": "policy_violation",
            "elapsed_seconds": time.monotonic() - started,
            "patch_applied": False,
            "tests_passed": 0,
            "tests_total": 0,
            "correctness_receipt": None,
        }
    if _candidate_state_sha256(candidate, manifest_sha) != state_before:
        return {
            **common,
            "status": "failed",
            "failure_kind": "policy_violation",
            "elapsed_seconds": time.monotonic() - started,
            "patch_applied": False,
            "tests_passed": 0,
            "tests_total": 0,
            "correctness_receipt": None,
        }
    expected = tuple(manifest["correctness"]["expected_test_ids"])
    passed = sum(report[item][0] == "passed" for item in expected)
    if returncode != 0 or passed != len(expected):
        return {
            **common,
            "status": "failed",
            "failure_kind": "tests_failed",
            "elapsed_seconds": time.monotonic() - started,
            "patch_applied": True,
            "tests_passed": passed,
            "tests_total": len(expected),
            "correctness_receipt": None,
        }
    state_sha = state_before
    evidence_sha = canonical_sha256(
        {
            "expected_test_ids": list(expected),
            "outcomes": {item: report[item][0] for item in expected},
        }
    )
    receipt = correctness_receipt(
        task_manifest_sha256=manifest_sha,
        request_binding=request["binding"],
        correctness_nonce=request["result_nonce"],
        patch_sha256=request["binding"]["patch_sha256"],
        candidate_state_sha256=state_sha,
        correctness_evidence_sha256=evidence_sha,
    )
    state = {
        "schema_version": 1,
        "correctness_receipt": receipt,
        "task_manifest_sha256": manifest_sha,
        "request_binding": request["binding"],
        "correctness_nonce": request["result_nonce"],
        "patch_sha256": request["binding"]["patch_sha256"],
        "candidate_state_sha256": state_sha,
        "correctness_evidence_sha256": evidence_sha,
        "reference_path": str(reference),
        "candidate_path": str(candidate),
    }
    atomic_private_result(PRIVATE_ROOT / f"receipt-{receipt}.json", state)
    return {
        **common,
        "status": "passed",
        "failure_kind": None,
        "elapsed_seconds": time.monotonic() - started,
        "patch_applied": True,
        "tests_passed": len(expected),
        "tests_total": len(expected),
        "correctness_receipt": receipt,
    }


def _load_receipt_state(
    request: Mapping[str, Any], manifest_sha: str
) -> dict[str, Any]:
    receipt = request["correctness_receipt"]
    state = _load_json(PRIVATE_ROOT / f"receipt-{receipt}.json")
    if (
        state.get("correctness_receipt") != receipt
        or state.get("task_manifest_sha256") != manifest_sha
        or state.get("request_binding") != request["binding"]
        or state.get("patch_sha256") != request["binding"]["patch_sha256"]
    ):
        raise SupervisorContractError("correctness receipt state differs")
    expected = correctness_receipt(
        task_manifest_sha256=state["task_manifest_sha256"],
        request_binding=state["request_binding"],
        correctness_nonce=state["correctness_nonce"],
        patch_sha256=state["patch_sha256"],
        candidate_state_sha256=state["candidate_state_sha256"],
        correctness_evidence_sha256=state["correctness_evidence_sha256"],
    )
    if expected != receipt:
        raise SupervisorContractError("correctness receipt preimage differs")
    return state


def _performance_result(
    request: Mapping[str, Any], manifest: Mapping[str, Any], manifest_sha: str
) -> dict[str, Any]:
    started = time.monotonic()
    common = _common_result(request, elapsed=0.0)
    state = _load_receipt_state(request, manifest_sha)
    reference = Path(state["reference_path"])
    candidate = Path(state["candidate_path"])
    if (
        not reference.is_dir()
        or not candidate.is_dir()
        or _candidate_state_sha256(candidate, manifest_sha)
        != state["candidate_state_sha256"]
    ):
        raise SupervisorContractError("candidate state changed after correctness")
    command = manifest["performance"]
    expected = tuple(command["expected_test_ids"])
    reference_state = _candidate_state_sha256(reference, manifest_sha)
    candidate_state = state["candidate_state_sha256"]

    def run_checked(label: str, repository: Path, report_path: Path):
        if (
            _candidate_state_sha256(reference, manifest_sha) != reference_state
            or _candidate_state_sha256(candidate, manifest_sha) != candidate_state
        ):
            raise CandidatePolicyViolation("performance repository state changed")
        observed = _run_worker_command(
            command,
            repository=repository,
            report_path=report_path,
        )
        if (
            _candidate_state_sha256(reference, manifest_sha) != reference_state
            or _candidate_state_sha256(candidate, manifest_sha) != candidate_state
        ):
            raise CandidatePolicyViolation(
                f"{label} performance invocation changed repository state"
            )
        return observed

    measurements = {
        item: {
            "test_id": item,
            "reference_seconds": [],
            "candidate_seconds": [],
            "candidate_correct": [],
        }
        for item in expected
    }
    try:
        for warmup in range(command["warmup_repetitions"]):
            for label, repository in (("reference", reference), ("candidate", candidate)):
                returncode, report = run_checked(
                    label,
                    repository,
                    CACHE_ROOT / "reports" / f"warmup-{warmup}-{label}.json",
                )
                if returncode != 0 or any(report[item][0] != "passed" for item in expected):
                    raise CandidatePolicyViolation("performance warmup was not correct")
        for repetition in range(command["measurement_repetitions"]):
            order = (
                (("reference", reference), ("candidate", candidate))
                if repetition % 2 == 0
                else (("candidate", candidate), ("reference", reference))
            )
            observed: dict[str, dict[str, tuple[str, float]]] = {}
            returncodes: dict[str, int] = {}
            for label, repository in order:
                returncode, report = run_checked(
                    label,
                    repository,
                    CACHE_ROOT
                    / "reports"
                    / f"measure-{repetition}-{label}.json",
                )
                observed[label] = report
                returncodes[label] = returncode
            if returncodes["reference"] != 0 or any(
                observed["reference"][item][0] != "passed" for item in expected
            ):
                raise SupervisorContractError("reference performance invocation failed")
            for item in expected:
                measurements[item]["reference_seconds"].append(
                    observed["reference"][item][1]
                )
                measurements[item]["candidate_seconds"].append(
                    observed["candidate"][item][1]
                )
                measurements[item]["candidate_correct"].append(
                    returncodes["candidate"] == 0
                    and observed["candidate"][item][0] == "passed"
                )
    except CandidatePolicyViolation:
        return {
            **common,
            "status": "failed",
            "failure_kind": "insufficient_measurements",
            "elapsed_seconds": time.monotonic() - started,
            "correctness_receipt": request["correctness_receipt"],
            "measurements": [],
            "score": None,
        }
    ordered = [measurements[item] for item in expected]
    if not all(all(item["candidate_correct"]) for item in ordered):
        return {
            **common,
            "status": "failed",
            "failure_kind": "measurements_incorrect",
            "elapsed_seconds": time.monotonic() - started,
            "correctness_receipt": request["correctness_receipt"],
            "measurements": ordered,
            "score": None,
        }
    ratios = [
        median(item["reference_seconds"]) / median(item["candidate_seconds"])
        for item in ordered
    ]
    if any(not math.isfinite(value) or value <= 0 for value in ratios):
        raise SupervisorContractError("performance ratio is invalid")
    score = math.exp(sum(math.log(value) for value in ratios) / len(ratios))
    return {
        **common,
        "status": "passed",
        "failure_kind": None,
        "elapsed_seconds": time.monotonic() - started,
        "correctness_receipt": request["correctness_receipt"],
        "measurements": ordered,
        "score": score,
    }


def _error_result(request: Mapping[str, Any], started: float) -> dict[str, Any]:
    common = _common_result(request, elapsed=time.monotonic() - started)
    if request["stage"] == "correctness":
        return {
            **common,
            "patch_applied": False,
            "tests_passed": 0,
            "tests_total": 0,
            "correctness_receipt": None,
        }
    return {
        **common,
        "correctness_receipt": request["correctness_receipt"],
        "measurements": [],
        "score": None,
    }


def run_once() -> int:
    if os.geteuid() != 0:
        raise SupervisorContractError("stage supervisor must start as uid 0")
    if len(sys.argv) != 1:
        raise SupervisorContractError("stage supervisor accepts no argv")
    os.umask(0o077)
    manifest, manifest_sha = _load_manifest()
    request = _load_request(manifest)
    started = time.monotonic()
    try:
        require_trusted_result_channel()
        if request["stage"] == "correctness":
            result = _write_correctness(request, manifest, manifest_sha)
        else:
            result = _performance_result(request, manifest, manifest_sha)
    except Exception:
        result = _error_result(request, started)
    result_path = PRIVATE_ROOT / f"result-{request['result_nonce']}.json"
    atomic_private_result(result_path, result)
    return 0


def main() -> int:
    try:
        return run_once()
    except Exception:
        # No request-derived filename or candidate-controlled text is emitted.
        # The outer adapter treats a missing private result as environment-invalid.
        return 70


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "CandidatePolicyViolation",
    "PatchApplyFailure",
    "QuiescenceViolation",
    "SupervisorContractError",
    "UnattestableCandidateOutcome",
    "atomic_private_result",
    "canonical_sha256",
    "correctness_receipt",
    "enforce_worker_quiescence",
    "exact_apply_argv",
    "main",
    "run_once",
]
