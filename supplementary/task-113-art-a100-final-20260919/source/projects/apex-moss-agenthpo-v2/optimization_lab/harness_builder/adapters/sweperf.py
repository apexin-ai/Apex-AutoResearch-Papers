from __future__ import annotations

import hashlib
import json
import math
import os
import re
import secrets
import stat
import threading
import time
import uuid
from dataclasses import dataclass
from enum import Enum
from pathlib import Path, PurePosixPath
from types import MappingProxyType
from typing import Any, Callable, Mapping, Protocol, Sequence


SWEPERF_EVALUATOR_ID = "swe-perf-docker"
SWEPERF_EVALUATOR_COMMIT = "9e8fed285ed640b51baaf66b13773706dc95aa45"
SWEPERF_DATASET_COMMIT = "6298f128c550e92ac25af17653cf092224046516"
SWEPERF_DATASET_PARQUET_SHA256 = (
    "7c682ebdc080078ad936b6ddcb2b802227e5c91b933bd812077bce7ad6d70253"
)
EVALUATOR_COMMIT = SWEPERF_EVALUATOR_COMMIT
DATASET_COMMIT = SWEPERF_DATASET_COMMIT
DATASET_PARQUET_SHA256 = SWEPERF_DATASET_PARQUET_SHA256
PATCH_APPLY_MODE = "git-apply-check-v1"
PRIVATE_RESULT_SCHEMA_VERSION = 1
PERFORMANCE_REPETITIONS = 20
MAX_PATCH_BYTES = 1_048_576
MAX_PATCH_FILES = 64
MAX_PATCH_HUNKS = 1_024
ADVERSARIAL_CANARY_IDS = (
    "no_op",
    "adversarial_stdout",
    "correctness_regression",
)

_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:+-]{0,159}\Z")
_REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
_IMAGE_REF = re.compile(r"[^\s@]+@sha256:[0-9a-f]{64}\Z")
_DIFF_HEADER = re.compile(r"diff --git a/([^\s]+) b/([^\s]+)\Z")
_INDEX = re.compile(
    r"index ([0-9a-f]{7,64})\.\.([0-9a-f]{7,64})(?: (100644|100755))?\Z"
)
_HUNK = re.compile(
    r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(?: .*)?\Z"
)
_ALLOWED_PATH = re.compile(r"[A-Za-z0-9_+@.,=-]+\Z")


class PatchContractError(ValueError):
    """The candidate is not one canonical, bounded Git unified diff."""


class PrivateResultError(ValueError):
    """Trusted evaluator evidence is absent, malformed, or bound to another run."""


@dataclass(frozen=True)
class PatchSummary:
    sha256: str
    byte_count: int
    file_paths: tuple[str, ...]
    hunk_count: int
    added_lines: int
    deleted_lines: int


def _candidate_bytes(candidate: str | bytes | Path) -> bytes:
    if isinstance(candidate, Path):
        try:
            metadata = candidate.lstat()
            if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
                raise PatchContractError("candidate path must be a regular file")
            descriptor = os.open(
                candidate,
                os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0),
            )
            with os.fdopen(descriptor, "rb") as stream:
                opened = os.fstat(stream.fileno())
                if not stat.S_ISREG(opened.st_mode):
                    raise PatchContractError("candidate path must be a regular file")
                return stream.read(MAX_PATCH_BYTES + 1)
        except PatchContractError:
            raise
        except OSError as exc:
            raise PatchContractError("candidate patch could not be read safely") from exc
    if isinstance(candidate, str):
        return candidate.encode("utf-8")
    if isinstance(candidate, bytes):
        return candidate
    raise TypeError("candidate must be unified-diff text, bytes, or a Path")


def _validate_repo_path(value: str) -> str:
    if not value or len(value) > 240 or "\\" in value or "\x00" in value:
        raise PatchContractError("invalid repository-relative path")
    path = PurePosixPath(value)
    parts = path.parts
    if value != path.as_posix() or path.is_absolute() or not parts or any(
        part in {"", ".", ".."} or part.lower() == ".git" for part in parts
    ):
        raise PatchContractError("unsafe repository-relative path")
    if any(not _ALLOWED_PATH.fullmatch(part) for part in parts):
        raise PatchContractError("patch paths must use the canonical unquoted subset")
    return value


def _range_count(value: str | None) -> int:
    return 1 if value is None else int(value)


def validate_unified_diff(candidate: str | bytes | Path) -> PatchSummary:
    """Validate the exact candidate boundary used by HB-GEN-1.

    The accepted subset is a canonical ``git diff`` over regular repository files.
    Renames, copies, mode-only changes, binary patches, quoted paths, preambles, and
    fuzzy/plain ``patch`` input fail closed.  New and deleted regular files are
    supported, but every file section must contain at least one internally
    consistent hunk.
    """

    raw = _candidate_bytes(candidate)
    digest = hashlib.sha256(raw).hexdigest()
    if not raw:
        raise PatchContractError("empty/no-op patches are forbidden")
    if len(raw) > MAX_PATCH_BYTES:
        raise PatchContractError("patch exceeds the byte limit")
    if b"\x00" in raw or b"\r" in raw:
        raise PatchContractError("patch must be NUL-free UTF-8 with LF endings")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise PatchContractError("patch is not valid UTF-8") from exc
    if not text.endswith("\n"):
        raise PatchContractError("patch must end with one LF")
    if text.startswith("\ufeff") or not text.startswith("diff --git "):
        raise PatchContractError("patch must start with a diff --git header")

    lines = text[:-1].split("\n")
    index = 0
    paths: list[str] = []
    total_hunks = 0
    total_added = 0
    total_deleted = 0

    while index < len(lines):
        if len(paths) >= MAX_PATCH_FILES:
            raise PatchContractError("patch changes too many files")
        header = _DIFF_HEADER.fullmatch(lines[index])
        if header is None:
            raise PatchContractError("expected canonical diff --git header")
        old_path = _validate_repo_path(header.group(1))
        new_path = _validate_repo_path(header.group(2))
        if old_path != new_path:
            raise PatchContractError("renames and copies are outside the patch contract")
        if old_path in paths:
            raise PatchContractError("a file may appear in only one diff section")
        paths.append(old_path)
        index += 1

        change_kind = "modify"
        if index < len(lines) and lines[index].startswith("new file mode "):
            if lines[index] not in {"new file mode 100644", "new file mode 100755"}:
                raise PatchContractError("only regular new files are allowed")
            change_kind = "new"
            index += 1
        elif index < len(lines) and lines[index].startswith("deleted file mode "):
            if lines[index] not in {
                "deleted file mode 100644",
                "deleted file mode 100755",
            }:
                raise PatchContractError("only regular deleted files are allowed")
            change_kind = "delete"
            index += 1

        if index >= len(lines):
            raise PatchContractError("truncated diff section")
        index_line = _INDEX.fullmatch(lines[index])
        if index_line is None:
            raise PatchContractError("each diff section requires one canonical index line")
        old_object, new_object = index_line.group(1), index_line.group(2)
        if len(old_object) != len(new_object):
            raise PatchContractError("index object ids must use the same width")
        old_is_zero = set(old_object) == {"0"}
        new_is_zero = set(new_object) == {"0"}
        if change_kind == "new" and (not old_is_zero or new_is_zero):
            raise PatchContractError("new-file index line is inconsistent")
        if change_kind == "delete" and (old_is_zero or not new_is_zero):
            raise PatchContractError("deleted-file index line is inconsistent")
        if change_kind == "modify" and (old_is_zero or new_is_zero):
            raise PatchContractError("modified-file index line is inconsistent")
        index += 1

        expected_old = "/dev/null" if change_kind == "new" else f"a/{old_path}"
        expected_new = "/dev/null" if change_kind == "delete" else f"b/{new_path}"
        if index >= len(lines) or lines[index] != f"--- {expected_old}":
            raise PatchContractError("old-file header does not match diff path")
        index += 1
        if index >= len(lines) or lines[index] != f"+++ {expected_new}":
            raise PatchContractError("new-file header does not match diff path")
        index += 1

        section_hunks = 0
        section_changes = 0
        while index < len(lines) and not lines[index].startswith("diff --git "):
            hunk = _HUNK.fullmatch(lines[index])
            if hunk is None:
                raise PatchContractError("unexpected metadata or malformed hunk header")
            section_hunks += 1
            total_hunks += 1
            if total_hunks > MAX_PATCH_HUNKS:
                raise PatchContractError("patch contains too many hunks")
            expected_old_count = _range_count(hunk.group(2))
            expected_new_count = _range_count(hunk.group(4))
            index += 1

            old_count = 0
            new_count = 0
            old_content: list[str] = []
            new_content: list[str] = []
            previous_was_content = False
            while index < len(lines):
                line = lines[index]
                if line.startswith("diff --git ") or _HUNK.fullmatch(line):
                    break
                if line == r"\ No newline at end of file":
                    if not previous_was_content:
                        raise PatchContractError("misplaced no-newline marker")
                    previous_was_content = False
                    index += 1
                    continue
                if not line or line[0] not in {" ", "+", "-"}:
                    raise PatchContractError("hunk body line lacks a unified-diff prefix")
                prefix = line[0]
                if prefix in {" ", "-"}:
                    old_count += 1
                    old_content.append(line[1:])
                if prefix in {" ", "+"}:
                    new_count += 1
                    new_content.append(line[1:])
                if prefix == "+":
                    total_added += 1
                    section_changes += 1
                elif prefix == "-":
                    total_deleted += 1
                    section_changes += 1
                previous_was_content = True
                index += 1
            if old_count != expected_old_count or new_count != expected_new_count:
                raise PatchContractError("hunk line counts do not match its header")
            if old_content == new_content:
                raise PatchContractError("semantic no-op hunks are forbidden")

        if section_hunks == 0 or section_changes == 0:
            raise PatchContractError("every diff section must contain a real text change")

    return PatchSummary(
        sha256=digest,
        byte_count=len(raw),
        file_paths=tuple(paths),
        hunk_count=total_hunks,
        added_lines=total_added,
        deleted_lines=total_deleted,
    )


_FROZEN_TASK_DATA: Mapping[str, tuple[str, str, str]] = MappingProxyType(
    {
        "astropy__astropy-13817": (
            "astropy/astropy",
            "d4fc9d9b96f0879c363a8183842e5cf6067fae37",
            "55aa75150fd32ebadac1ad0e761433ec090e0be0ca583974f2736f5e637a8da4",
        ),
        "matplotlib__matplotlib-24250": (
            "matplotlib/matplotlib",
            "f6e75121e11b6ba918c5f6e5c2cc1b9f4fccc8b0",
            "cdcfe6b5ae76b9465a1ae4bc4936ef08e2a7500f43a7f89d502474aa0c2f540f",
        ),
        "mwaskom__seaborn-2313": (
            "mwaskom/seaborn",
            "211cabb09bb9228635bdd80f74f7591d36d7b2a7",
            "73cfff1738eb9f2bf70e361f0447a39b0a55392ac51efed65920149793ac2bde",
        ),
        "pydata__xarray-9407": (
            "pydata/xarray",
            "12d8cfa317b1a08748cb6a0a1b10a6efe3a7d3d2",
            "78b882de62ff00e4bf8bd59569ac93295b2f3900102477ba57d708b97708d4f5",
        ),
        "pylint-dev__pylint-7747": (
            "pylint-dev/pylint",
            "a29a2ab06cc454867aa89d52c11c4f6fa99d2522",
            "49ba6257464e75a359d4a544b6ace2ab828a3672efdc641c462146f055faadb5",
        ),
        "scikit-learn__scikit-learn-12625": (
            "scikit-learn/scikit-learn",
            "ac327c5ad66fa3d4eb607d007e3684dec872d49a",
            "acdee06d2c84af9b54da38bf2e2bd092e6a23f3a057e7e75836f7c3cc3ae0d7c",
        ),
        "sphinx-doc__sphinx-12615": (
            "sphinx-doc/sphinx",
            "e61f56950d624f5fa540a1c8d4e3baedd2889bd0",
            "d844e21bace7675514c9c189e78a390d9d799752f78d4e4972d433547b11f9cd",
        ),
        "sympy__sympy-25205": (
            "sympy/sympy",
            "ffb5a3f062b8a4ed7125f863f9a254775da6eb46",
            "18e0ee00241cd7de259b54cd52eabe87c82e3f871e9849d155e76dc9cf20018e",
        ),
    }
)


@dataclass(frozen=True)
class SWEPerfTask:
    instance_id: str
    repository: str
    base_commit: str
    task_sha256: str

    def __post_init__(self) -> None:
        if not _SAFE_ID.fullmatch(self.instance_id):
            raise ValueError("unsafe SWE-Perf instance id")
        if not _REPOSITORY.fullmatch(self.repository):
            raise ValueError("invalid SWE-Perf repository")
        if not _COMMIT.fullmatch(self.base_commit):
            raise ValueError("SWE-Perf base commit must be pinned")
        if not _SHA256.fullmatch(self.task_sha256):
            raise ValueError("SWE-Perf task hash must be pinned")
        expected = _FROZEN_TASK_DATA.get(self.instance_id)
        if expected is None:
            raise ValueError("SWE-Perf task is not frozen for HB-GEN-1")
        if (self.repository, self.base_commit, self.task_sha256) != expected:
            raise ValueError("SWE-Perf task differs from the frozen HB-GEN-1 contract")

    @classmethod
    def from_instance_id(cls, instance_id: str) -> "SWEPerfTask":
        return frozen_task(instance_id)


_TASKS = tuple(
    SWEPerfTask(instance_id, repository, base_commit, task_sha256)
    for instance_id, (repository, base_commit, task_sha256) in _FROZEN_TASK_DATA.items()
)

FROZEN_TASKS: Mapping[str, SWEPerfTask] = MappingProxyType(
    {task.instance_id: task for task in _TASKS}
)
SWEPERF_TASK_HASHES: Mapping[str, str] = MappingProxyType(
    {task.instance_id: task.task_sha256 for task in _TASKS}
)
SWEPERF_BASE_COMMITS: Mapping[str, str] = MappingProxyType(
    {task.instance_id: task.base_commit for task in _TASKS}
)


def frozen_task(instance_id: str) -> SWEPerfTask:
    try:
        return FROZEN_TASKS[instance_id]
    except KeyError as exc:
        raise ValueError("instance is not in the frozen HB-GEN-1 SWE-Perf set") from exc


class EvaluationStatus(str, Enum):
    VALID = "valid"
    CONTRACT_REJECTED = "contract_rejected"
    INCORRECT = "incorrect"
    TIMEOUT = "timeout"
    ENVIRONMENT_INVALID = "environment_invalid"


class EvaluationStage(str, Enum):
    CONTRACT = "contract"
    CORRECTNESS = "correctness"
    PERFORMANCE = "performance"


@dataclass(frozen=True)
class AttemptBinding:
    attempt_id: str
    instance_id: str
    repository: str
    evaluator: str
    evaluator_commit: str
    dataset_commit: str
    dataset_parquet_sha256: str
    base_commit: str
    task_sha256: str
    image_ref: str
    patch_apply_mode: str
    patch_sha256: str


@dataclass(frozen=True)
class DockerWorkspace:
    workspace_id: str
    attempt_id: str
    fresh: bool


@dataclass(frozen=True)
class StageRequest:
    binding: AttemptBinding
    stage: EvaluationStage
    result_nonce: str
    correctness_receipt: str | None = None


@dataclass(frozen=True)
class StageRun:
    """Untrusted process output plus trusted process-control metadata.

    ``stdout`` and ``stderr`` are intentionally never inspected by the adapter.
    The verdict comes only from ``DockerExecutor.read_private_result``.
    """

    returncode: int
    elapsed_seconds: float
    timed_out: bool = False
    stdout: str = ""
    stderr: str = ""

    def __post_init__(self) -> None:
        if isinstance(self.returncode, bool) or not isinstance(self.returncode, int):
            raise ValueError("returncode must be an integer")
        if (
            isinstance(self.elapsed_seconds, bool)
            or not isinstance(self.elapsed_seconds, (int, float))
            or not math.isfinite(float(self.elapsed_seconds))
            or self.elapsed_seconds < 0
        ):
            raise ValueError("stage elapsed time must be finite and non-negative")
        if not isinstance(self.timed_out, bool):
            raise ValueError("timed_out must be boolean")


class DockerExecutor(Protocol):
    """Trusted Docker boundary; implementations keep result channels private.

    ``create_workspace`` creates a new container/worktree/cache namespace at the
    pinned base commit with networking disabled. The candidate cannot write the
    supervisor result channel. Correctness uses exact ``git apply --check`` then
    ``git apply`` semantics (never a fuzzy ``patch`` fallback), and performance
    runs only with the receipt produced by correctness.
    """

    def create_workspace(self, binding: AttemptBinding) -> DockerWorkspace: ...

    def copy_candidate(self, workspace: DockerWorkspace, patch: bytes) -> None: ...

    def run_stage(
        self, workspace: DockerWorkspace, request: StageRequest
    ) -> StageRun: ...

    def read_private_result(
        self, workspace: DockerWorkspace, request: StageRequest
    ) -> bytes: ...

    def destroy_workspace(self, workspace: DockerWorkspace) -> None: ...


@dataclass(frozen=True)
class PerformanceMeasurement:
    test_id: str
    reference_seconds: tuple[float, ...]
    candidate_seconds: tuple[float, ...]
    candidate_correct: tuple[bool, ...]


@dataclass(frozen=True)
class PrivateCorrectnessResult:
    status: str
    patch_applied: bool
    tests_passed: int
    tests_total: int
    correctness_receipt: str | None
    failure_kind: str | None
    elapsed_seconds: float


@dataclass(frozen=True)
class PrivatePerformanceResult:
    status: str
    correctness_receipt: str
    measurements: tuple[PerformanceMeasurement, ...]
    score: float | None
    failure_kind: str | None
    elapsed_seconds: float


@dataclass(frozen=True)
class SWEPerfEvaluation:
    status: EvaluationStatus
    stage_reached: EvaluationStage
    correct: bool
    score: float | None
    attempt_id: str
    patch_sha256: str
    failure_kind: str | None
    evaluator_seconds: float

    def __post_init__(self) -> None:
        if self.status is EvaluationStatus.VALID:
            if not self.correct or self.score is None:
                raise ValueError("a valid SWE-Perf result must be correct and scored")
        elif self.score is not None:
            raise ValueError("only a valid SWE-Perf result may expose a score")
        if self.evaluator_seconds < 0 or not math.isfinite(self.evaluator_seconds):
            raise ValueError("evaluator time must be finite and non-negative")

    def public_feedback(self) -> dict[str, Any]:
        """Return the only evaluator fields that Builder/solution code may see."""

        return {
            "status": self.status.value,
            "stage_reached": self.stage_reached.value,
            "correct": self.correct,
            "score": self.score,
            "failure_kind": self.failure_kind,
            "evaluator_seconds": self.evaluator_seconds,
        }


_COMMON_RESULT_KEYS = {
    "schema_version",
    "attempt_id",
    "result_nonce",
    "stage",
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
    "status",
    "failure_kind",
    "elapsed_seconds",
}
_CORRECTNESS_KEYS = _COMMON_RESULT_KEYS | {
    "patch_applied",
    "tests_passed",
    "tests_total",
    "correctness_receipt",
}
_PERFORMANCE_KEYS = _COMMON_RESULT_KEYS | {
    "correctness_receipt",
    "measurements",
    "score",
}
_CORRECTNESS_FAILURES = {
    "patch_apply_failed",
    "tests_failed",
    "policy_violation",
    "evaluator_error",
}
_PERFORMANCE_FAILURES = {
    "measurements_incorrect",
    "insufficient_measurements",
    "evaluator_error",
}


def _reject_constant(value: str) -> None:
    raise PrivateResultError(f"non-finite JSON number {value!r}")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise PrivateResultError("private result contains a duplicate key")
        result[key] = value
    return result


def _load_private_json(raw: bytes) -> dict[str, Any]:
    if not isinstance(raw, bytes) or not raw or len(raw) > 1_048_576:
        raise PrivateResultError("private result must be bounded non-empty bytes")
    try:
        text = raw.decode("utf-8", errors="strict")
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PrivateResultError("private result is not strict UTF-8 JSON") from exc
    if not isinstance(value, dict):
        raise PrivateResultError("private result must be a JSON object")
    return value


def _require_exact_keys(payload: Mapping[str, Any], expected: set[str]) -> None:
    if set(payload) != expected:
        raise PrivateResultError("private result fields differ from the frozen schema")


def _strict_nonnegative_float(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise PrivateResultError(f"{label} must be numeric")
    converted = float(value)
    if not math.isfinite(converted) or converted < 0:
        raise PrivateResultError(f"{label} must be finite and non-negative")
    return converted


def _strict_positive_float(value: Any, label: str) -> float:
    converted = _strict_nonnegative_float(value, label)
    if converted <= 0:
        raise PrivateResultError(f"{label} must be positive")
    return converted


def _strict_int(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise PrivateResultError(f"{label} must be a non-negative integer")
    return value


def _validate_common_result(
    payload: Mapping[str, Any], request: StageRequest
) -> tuple[str, str | None, float]:
    binding = request.binding
    expected = {
        "schema_version": PRIVATE_RESULT_SCHEMA_VERSION,
        "attempt_id": binding.attempt_id,
        "result_nonce": request.result_nonce,
        "stage": request.stage.value,
        "instance_id": binding.instance_id,
        "repository": binding.repository,
        "evaluator": binding.evaluator,
        "evaluator_commit": binding.evaluator_commit,
        "dataset_commit": binding.dataset_commit,
        "dataset_parquet_sha256": binding.dataset_parquet_sha256,
        "base_commit": binding.base_commit,
        "task_sha256": binding.task_sha256,
        "image_ref": binding.image_ref,
        "patch_apply_mode": binding.patch_apply_mode,
        "patch_sha256": binding.patch_sha256,
    }
    for key, value in expected.items():
        if payload.get(key) != value or type(payload.get(key)) is not type(value):
            raise PrivateResultError(f"private result binding mismatch: {key}")
    status = payload.get("status")
    if status not in {"passed", "failed", "error"}:
        raise PrivateResultError("unknown private result status")
    failure_kind = payload.get("failure_kind")
    if failure_kind is not None and not isinstance(failure_kind, str):
        raise PrivateResultError("failure_kind must be a string or null")
    elapsed = _strict_nonnegative_float(payload.get("elapsed_seconds"), "elapsed_seconds")
    return status, failure_kind, elapsed


def parse_correctness_result(
    raw: bytes, request: StageRequest
) -> PrivateCorrectnessResult:
    if request.stage is not EvaluationStage.CORRECTNESS:
        raise PrivateResultError("correctness parser received another stage")
    payload = _load_private_json(raw)
    _require_exact_keys(payload, _CORRECTNESS_KEYS)
    status, failure_kind, elapsed = _validate_common_result(payload, request)
    if not isinstance(payload["patch_applied"], bool):
        raise PrivateResultError("patch_applied must be boolean")
    patch_applied = payload["patch_applied"]
    tests_passed = _strict_int(payload["tests_passed"], "tests_passed")
    tests_total = _strict_int(payload["tests_total"], "tests_total")
    if tests_passed > tests_total:
        raise PrivateResultError("tests_passed exceeds tests_total")
    receipt = payload["correctness_receipt"]
    if receipt is not None and (
        not isinstance(receipt, str) or not _SHA256.fullmatch(receipt)
    ):
        raise PrivateResultError("invalid correctness receipt")

    if status == "passed":
        if (
            not patch_applied
            or tests_total == 0
            or tests_passed != tests_total
            or receipt is None
            or failure_kind is not None
        ):
            raise PrivateResultError("inconsistent passing correctness result")
    elif status == "failed":
        if receipt is not None or failure_kind not in _CORRECTNESS_FAILURES:
            raise PrivateResultError("failed correctness result lacks a known failure")
        if failure_kind == "evaluator_error":
            raise PrivateResultError("evaluator errors must use error status")
        if failure_kind in {"patch_apply_failed", "policy_violation"} and (
            patch_applied or tests_passed != 0 or tests_total != 0
        ):
            raise PrivateResultError("pre-test failure has inconsistent test evidence")
        if failure_kind == "tests_failed" and (
            not patch_applied
            or tests_total == 0
            or tests_passed >= tests_total
        ):
            raise PrivateResultError("test failure has inconsistent counts")
        if not patch_applied and (tests_passed != 0 or tests_total != 0):
            raise PrivateResultError("tests cannot run before the patch is applied")
    elif (
        receipt is not None
        or failure_kind != "evaluator_error"
        or tests_passed > tests_total
    ):
        raise PrivateResultError("inconsistent evaluator error result")

    return PrivateCorrectnessResult(
        status=status,
        patch_applied=patch_applied,
        tests_passed=tests_passed,
        tests_total=tests_total,
        correctness_receipt=receipt,
        failure_kind=failure_kind,
        elapsed_seconds=elapsed,
    )


def _parse_measurement(value: Any) -> PerformanceMeasurement:
    if not isinstance(value, dict) or set(value) != {
        "test_id",
        "reference_seconds",
        "candidate_seconds",
        "candidate_correct",
    }:
        raise PrivateResultError("performance measurement fields differ")
    test_id = value["test_id"]
    if (
        not isinstance(test_id, str)
        or not test_id
        or len(test_id) > 512
        or any(ord(character) < 32 for character in test_id)
    ):
        raise PrivateResultError("unsafe performance test id")
    reference = value["reference_seconds"]
    candidate = value["candidate_seconds"]
    correct = value["candidate_correct"]
    if not all(isinstance(item, list) for item in (reference, candidate, correct)):
        raise PrivateResultError("measurement samples must be arrays")
    if not (
        len(reference)
        == len(candidate)
        == len(correct)
        == PERFORMANCE_REPETITIONS
    ):
        raise PrivateResultError("measurement repetition count changed")
    if not all(isinstance(item, bool) for item in correct):
        raise PrivateResultError("candidate_correct samples must be booleans")
    return PerformanceMeasurement(
        test_id=test_id,
        reference_seconds=tuple(
            _strict_positive_float(item, "reference_seconds") for item in reference
        ),
        candidate_seconds=tuple(
            _strict_positive_float(item, "candidate_seconds") for item in candidate
        ),
        candidate_correct=tuple(correct),
    )


def parse_performance_result(
    raw: bytes, request: StageRequest
) -> PrivatePerformanceResult:
    if request.stage is not EvaluationStage.PERFORMANCE:
        raise PrivateResultError("performance parser received another stage")
    payload = _load_private_json(raw)
    _require_exact_keys(payload, _PERFORMANCE_KEYS)
    status, failure_kind, elapsed = _validate_common_result(payload, request)
    receipt = payload["correctness_receipt"]
    if (
        not isinstance(receipt, str)
        or not _SHA256.fullmatch(receipt)
        or receipt != request.correctness_receipt
    ):
        raise PrivateResultError("performance result is not bound to correctness")
    values = payload["measurements"]
    if not isinstance(values, list):
        raise PrivateResultError("measurements must be an array")
    measurements = tuple(_parse_measurement(item) for item in values)
    if len({item.test_id for item in measurements}) != len(measurements):
        raise PrivateResultError("performance test ids must be unique")
    score_value = payload["score"]

    if status == "passed":
        if not measurements or failure_kind is not None or score_value is None:
            raise PrivateResultError("incomplete passing performance result")
        if not all(all(item.candidate_correct) for item in measurements):
            raise PrivateResultError("timed invocations must each remain correct")
        score = _strict_positive_float(score_value, "score")
    elif status == "failed":
        if (
            score_value is not None
            or failure_kind not in _PERFORMANCE_FAILURES
            or failure_kind == "evaluator_error"
        ):
            raise PrivateResultError("failed performance result lacks a known failure")
        if failure_kind == "measurements_incorrect" and (
            not measurements
            or all(all(item.candidate_correct) for item in measurements)
        ):
            raise PrivateResultError("incorrect measurement failure lacks evidence")
        score = None
    else:
        if score_value is not None or failure_kind != "evaluator_error":
            raise PrivateResultError("inconsistent performance evaluator error")
        score = None

    return PrivatePerformanceResult(
        status=status,
        correctness_receipt=receipt,
        measurements=measurements,
        score=score,
        failure_kind=failure_kind,
        elapsed_seconds=elapsed,
    )


class CanaryKind(str, Enum):
    REFERENCE = "reference"
    NO_OP = "no_op"
    ADVERSARIAL_STDOUT = "adversarial_stdout"
    CORRECTNESS_REGRESSION = "correctness_regression"


@dataclass(frozen=True)
class CanaryCase:
    case_id: str
    instance_id: str
    kind: CanaryKind
    opaque_candidate_ref: str
    expected_status: EvaluationStatus
    reaches_evaluator: bool
    run_performance: bool
    stdout_must_be_ignored: bool


def canary_plan(instance_ids: Sequence[str] | None = None) -> tuple[CanaryCase, ...]:
    """Return one reference per task plus one family-level adversarial trio."""

    selected = tuple(FROZEN_TASKS) if instance_ids is None else tuple(instance_ids)
    if not selected or len(selected) != len(set(selected)):
        raise ValueError("SWE-Perf canary tasks must be non-empty and unique")
    cases: list[CanaryCase] = []
    for instance_id in selected:
        task = frozen_task(instance_id)
        private_prefix = hashlib.sha256(
            f"{DATASET_COMMIT}|{task.task_sha256}".encode("utf-8")
        ).hexdigest()
        cases.append(
            CanaryCase(
                case_id=f"{instance_id}:reference",
                instance_id=instance_id,
                kind=CanaryKind.REFERENCE,
                opaque_candidate_ref=f"private://sweperf/{private_prefix}/reference",
                expected_status=EvaluationStatus.VALID,
                reaches_evaluator=True,
                run_performance=True,
                stdout_must_be_ignored=True,
            )
        )

    anchor_id = selected[0]
    anchor = frozen_task(anchor_id)
    private_prefix = hashlib.sha256(
        f"{DATASET_COMMIT}|{anchor.task_sha256}".encode("utf-8")
    ).hexdigest()
    cases.extend(
        (
            CanaryCase(
                case_id=f"{anchor_id}:no-op",
                instance_id=anchor_id,
                kind=CanaryKind.NO_OP,
                opaque_candidate_ref="builtin://empty-diff",
                expected_status=EvaluationStatus.CONTRACT_REJECTED,
                reaches_evaluator=False,
                run_performance=False,
                stdout_must_be_ignored=True,
            ),
            CanaryCase(
                case_id=f"{anchor_id}:adversarial-stdout",
                instance_id=anchor_id,
                kind=CanaryKind.ADVERSARIAL_STDOUT,
                opaque_candidate_ref=(
                    f"private://sweperf/{private_prefix}/forged-stdout"
                ),
                expected_status=EvaluationStatus.INCORRECT,
                reaches_evaluator=True,
                run_performance=False,
                stdout_must_be_ignored=True,
            ),
            CanaryCase(
                case_id=f"{anchor_id}:correctness-regression",
                instance_id=anchor_id,
                kind=CanaryKind.CORRECTNESS_REGRESSION,
                opaque_candidate_ref=(
                    f"private://sweperf/{private_prefix}/correctness-regression"
                ),
                expected_status=EvaluationStatus.INCORRECT,
                reaches_evaluator=True,
                run_performance=False,
                stdout_must_be_ignored=True,
            ),
        )
    )
    return tuple(cases)


class SWEPerfAdapter:
    """HB-GEN-1 orchestration around a trusted, private Docker evaluator.

    Docker mechanics are injected so the contract is unit-testable without a
    daemon.  The executor is responsible for implementing the pinned official
    evaluator inside the supplied digest-pinned image; this class controls
    attempt freshness, stage order, binding validation, and public disclosure.
    """

    def __init__(
        self,
        *,
        task: SWEPerfTask | str,
        image_ref: str,
        executor: DockerExecutor,
        attempt_id_factory: Callable[[], str] | None = None,
        nonce_factory: Callable[[], str] | None = None,
    ):
        resolved = frozen_task(task) if isinstance(task, str) else task
        expected = FROZEN_TASKS.get(resolved.instance_id)
        if expected is None or resolved != expected:
            raise ValueError("task binding differs from the frozen HB-GEN-1 manifest")
        if not isinstance(image_ref, str) or not _IMAGE_REF.fullmatch(image_ref):
            raise ValueError("SWE-Perf image must be pinned by sha256 digest")
        self.task = resolved
        self.image_ref = image_ref
        self.executor = executor
        self._attempt_id_factory = attempt_id_factory or (lambda: uuid.uuid4().hex)
        self._nonce_factory = nonce_factory or (lambda: secrets.token_hex(32))
        self._state_lock = threading.Lock()
        self._attempt_ids: set[str] = set()
        self._workspace_ids: set[str] = set()

    def public_task_context(
        self,
        *,
        problem_statement: str,
        allowed_repository_files: Sequence[str],
    ) -> dict[str, Any]:
        """Build an allowlisted view; private dataset row fields are not accepted."""

        if (
            not isinstance(problem_statement, str)
            or not problem_statement.strip()
            or "\x00" in problem_statement
        ):
            raise ValueError("problem statement must be non-empty public text")
        try:
            files = tuple(_validate_repo_path(item) for item in allowed_repository_files)
        except (PatchContractError, TypeError) as exc:
            raise ValueError("allowed repository file is unsafe") from exc
        if not files or len(files) != len(set(files)):
            raise ValueError("allowed repository files must be non-empty and unique")
        return {
            "suite": "swe-perf",
            "instance_id": self.task.instance_id,
            "repository": self.task.repository,
            "base_commit": self.task.base_commit,
            "task_sha256": self.task.task_sha256,
            "evaluator": SWEPERF_EVALUATOR_ID,
            "evaluator_commit": EVALUATOR_COMMIT,
            "dataset_commit": DATASET_COMMIT,
            "problem_statement": problem_statement,
            "allowed_repository_files": files,
        }

    def canary_plan(self) -> tuple[CanaryCase, ...]:
        return canary_plan((self.task.instance_id,))

    def _new_token(self, factory: Callable[[], str], label: str) -> str:
        value = factory()
        if not isinstance(value, str) or not _SHA256.fullmatch(value):
            raise ValueError(f"{label} factory must return 64 lowercase hex characters")
        return value

    def _new_attempt_id(self) -> str:
        value = self._attempt_id_factory()
        if not isinstance(value, str) or not _SAFE_ID.fullmatch(value):
            raise ValueError("attempt id factory returned an unsafe id")
        with self._state_lock:
            if value in self._attempt_ids:
                raise ValueError("attempt id factory reused an id")
            self._attempt_ids.add(value)
        return value

    def _accept_fresh_workspace(
        self, workspace: DockerWorkspace, attempt_id: str
    ) -> None:
        if (
            not isinstance(workspace, DockerWorkspace)
            or workspace.fresh is not True
            or workspace.attempt_id != attempt_id
            or not _SAFE_ID.fullmatch(workspace.workspace_id)
        ):
            raise RuntimeError("executor did not create a bound fresh Docker workspace")
        with self._state_lock:
            if workspace.workspace_id in self._workspace_ids:
                raise RuntimeError("executor reused a Docker workspace")
            self._workspace_ids.add(workspace.workspace_id)

    @staticmethod
    def _evaluation(
        *,
        status: EvaluationStatus,
        stage: EvaluationStage,
        correct: bool,
        score: float | None,
        binding: AttemptBinding,
        failure_kind: str | None,
        evaluator_seconds: float,
    ) -> SWEPerfEvaluation:
        return SWEPerfEvaluation(
            status=status,
            stage_reached=stage,
            correct=correct,
            score=score,
            attempt_id=binding.attempt_id,
            patch_sha256=binding.patch_sha256,
            failure_kind=failure_kind,
            evaluator_seconds=evaluator_seconds,
        )

    def evaluate(self, candidate: str | bytes | Path) -> SWEPerfEvaluation:
        attempt_id = self._new_attempt_id()
        try:
            raw = _candidate_bytes(candidate)
        except PatchContractError:
            raw = b""
        patch_sha256 = hashlib.sha256(raw).hexdigest()
        binding = AttemptBinding(
            attempt_id=attempt_id,
            instance_id=self.task.instance_id,
            repository=self.task.repository,
            evaluator=SWEPERF_EVALUATOR_ID,
            evaluator_commit=EVALUATOR_COMMIT,
            dataset_commit=DATASET_COMMIT,
            dataset_parquet_sha256=DATASET_PARQUET_SHA256,
            base_commit=self.task.base_commit,
            task_sha256=self.task.task_sha256,
            image_ref=self.image_ref,
            patch_apply_mode=PATCH_APPLY_MODE,
            patch_sha256=patch_sha256,
        )
        try:
            validate_unified_diff(raw)
        except PatchContractError:
            return self._evaluation(
                status=EvaluationStatus.CONTRACT_REJECTED,
                stage=EvaluationStage.CONTRACT,
                correct=False,
                score=None,
                binding=binding,
                failure_kind="invalid_unified_diff",
                evaluator_seconds=0.0,
            )

        workspace: DockerWorkspace | None = None
        result: SWEPerfEvaluation | None = None
        elapsed = 0.0
        wall_started = time.monotonic()
        cleanup_failed = False
        current_stage = EvaluationStage.CORRECTNESS
        try:
            workspace = self.executor.create_workspace(binding)
            self._accept_fresh_workspace(workspace, attempt_id)
            self.executor.copy_candidate(workspace, raw)

            correctness_request = StageRequest(
                binding=binding,
                stage=EvaluationStage.CORRECTNESS,
                result_nonce=self._new_token(self._nonce_factory, "nonce"),
            )
            correctness_run = self.executor.run_stage(workspace, correctness_request)
            if not isinstance(correctness_run, StageRun):
                raise RuntimeError("executor returned invalid stage metadata")
            if correctness_run.timed_out:
                result = self._evaluation(
                    status=EvaluationStatus.TIMEOUT,
                    stage=EvaluationStage.CORRECTNESS,
                    correct=False,
                    score=None,
                    binding=binding,
                    failure_kind="correctness_timeout",
                    evaluator_seconds=correctness_run.elapsed_seconds,
                )
            else:
                correctness = parse_correctness_result(
                    self.executor.read_private_result(workspace, correctness_request),
                    correctness_request,
                )
                elapsed += correctness.elapsed_seconds
                if correctness.status == "error":
                    result = self._evaluation(
                        status=EvaluationStatus.ENVIRONMENT_INVALID,
                        stage=EvaluationStage.CORRECTNESS,
                        correct=False,
                        score=None,
                        binding=binding,
                        failure_kind=correctness.failure_kind,
                        evaluator_seconds=elapsed,
                    )
                elif correctness.status == "failed":
                    result = self._evaluation(
                        status=EvaluationStatus.INCORRECT,
                        stage=EvaluationStage.CORRECTNESS,
                        correct=False,
                        score=None,
                        binding=binding,
                        failure_kind=correctness.failure_kind,
                        evaluator_seconds=elapsed,
                    )
                elif correctness_run.returncode != 0:
                    result = self._evaluation(
                        status=EvaluationStatus.ENVIRONMENT_INVALID,
                        stage=EvaluationStage.CORRECTNESS,
                        correct=False,
                        score=None,
                        binding=binding,
                        failure_kind="stage_exit_mismatch",
                        evaluator_seconds=elapsed,
                    )
                else:
                    current_stage = EvaluationStage.PERFORMANCE
                    performance_request = StageRequest(
                        binding=binding,
                        stage=EvaluationStage.PERFORMANCE,
                        result_nonce=self._new_token(self._nonce_factory, "nonce"),
                        correctness_receipt=correctness.correctness_receipt,
                    )
                    performance_run = self.executor.run_stage(
                        workspace, performance_request
                    )
                    if not isinstance(performance_run, StageRun):
                        raise RuntimeError("executor returned invalid stage metadata")
                    if performance_run.timed_out:
                        result = self._evaluation(
                            status=EvaluationStatus.TIMEOUT,
                            stage=EvaluationStage.PERFORMANCE,
                            correct=True,
                            score=None,
                            binding=binding,
                            failure_kind="performance_timeout",
                            evaluator_seconds=elapsed
                            + performance_run.elapsed_seconds,
                        )
                    else:
                        performance = parse_performance_result(
                            self.executor.read_private_result(
                                workspace, performance_request
                            ),
                            performance_request,
                        )
                        elapsed += performance.elapsed_seconds
                        if performance.status == "error":
                            result = self._evaluation(
                                status=EvaluationStatus.ENVIRONMENT_INVALID,
                                stage=EvaluationStage.PERFORMANCE,
                                correct=True,
                                score=None,
                                binding=binding,
                                failure_kind=performance.failure_kind,
                                evaluator_seconds=elapsed,
                            )
                        elif performance.status == "failed":
                            result = self._evaluation(
                                status=EvaluationStatus.INCORRECT,
                                stage=EvaluationStage.PERFORMANCE,
                                correct=False,
                                score=None,
                                binding=binding,
                                failure_kind=performance.failure_kind,
                                evaluator_seconds=elapsed,
                            )
                        elif performance_run.returncode != 0:
                            result = self._evaluation(
                                status=EvaluationStatus.ENVIRONMENT_INVALID,
                                stage=EvaluationStage.PERFORMANCE,
                                correct=True,
                                score=None,
                                binding=binding,
                                failure_kind="stage_exit_mismatch",
                                evaluator_seconds=elapsed,
                            )
                        else:
                            result = self._evaluation(
                                status=EvaluationStatus.VALID,
                                stage=EvaluationStage.PERFORMANCE,
                                correct=True,
                                score=performance.score,
                                binding=binding,
                                failure_kind=None,
                                evaluator_seconds=elapsed,
                            )
        except Exception:
            result = self._evaluation(
                status=EvaluationStatus.ENVIRONMENT_INVALID,
                stage=current_stage if result is None else result.stage_reached,
                correct=False,
                score=None,
                binding=binding,
                failure_kind="private_evaluator_contract_failure",
                evaluator_seconds=max(elapsed, time.monotonic() - wall_started),
            )
        finally:
            if workspace is not None:
                try:
                    self.executor.destroy_workspace(workspace)
                except Exception:
                    cleanup_failed = True

        if cleanup_failed:
            return self._evaluation(
                status=EvaluationStatus.ENVIRONMENT_INVALID,
                stage=result.stage_reached if result else EvaluationStage.CORRECTNESS,
                correct=False,
                score=None,
                binding=binding,
                failure_kind="workspace_cleanup_failed",
                evaluator_seconds=max(elapsed, time.monotonic() - wall_started),
            )
        if result is None:  # Defensive: every branch above must assign a result.
            return self._evaluation(
                status=EvaluationStatus.ENVIRONMENT_INVALID,
                stage=current_stage,
                correct=False,
                score=None,
                binding=binding,
                failure_kind="private_evaluator_contract_failure",
                evaluator_seconds=max(elapsed, time.monotonic() - wall_started),
            )
        return result


SWEPerfDockerAdapter = SWEPerfAdapter
build_canary_plan = canary_plan


__all__ = [
    "ADVERSARIAL_CANARY_IDS",
    "AttemptBinding",
    "CanaryCase",
    "CanaryKind",
    "DATASET_COMMIT",
    "DATASET_PARQUET_SHA256",
    "DockerExecutor",
    "DockerWorkspace",
    "EVALUATOR_COMMIT",
    "EvaluationStage",
    "EvaluationStatus",
    "FROZEN_TASKS",
    "MAX_PATCH_BYTES",
    "PATCH_APPLY_MODE",
    "PERFORMANCE_REPETITIONS",
    "PatchContractError",
    "PatchSummary",
    "PerformanceMeasurement",
    "PrivateCorrectnessResult",
    "PrivatePerformanceResult",
    "PrivateResultError",
    "SWEPerfAdapter",
    "SWEPerfDockerAdapter",
    "SWEPerfEvaluation",
    "SWEPerfTask",
    "SWEPERF_BASE_COMMITS",
    "SWEPERF_DATASET_COMMIT",
    "SWEPERF_DATASET_PARQUET_SHA256",
    "SWEPERF_EVALUATOR_COMMIT",
    "SWEPERF_EVALUATOR_ID",
    "SWEPERF_TASK_HASHES",
    "StageRequest",
    "StageRun",
    "canary_plan",
    "build_canary_plan",
    "frozen_task",
    "parse_correctness_result",
    "parse_performance_result",
    "validate_unified_diff",
]
