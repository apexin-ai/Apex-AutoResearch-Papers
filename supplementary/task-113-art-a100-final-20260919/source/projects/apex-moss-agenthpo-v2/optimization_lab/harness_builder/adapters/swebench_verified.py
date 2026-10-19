from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

from .swebench_verified_worker import (
    SWEBENCH_SOURCE_COMMIT,
    SWEBENCH_VERIFIED_EVALUATOR_ID,
)
from .sweperf import validate_unified_diff


SWEBENCH_VERIFIED_DATASET_SHA256 = (
    "43ed5a3d1d98da36472c1ade65ddd2085d7b4ff694fcaf6a023a07c5c1f32f21"
)
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:+-]{0,191}\Z")
_IMAGE = re.compile(r"[^\s@]+@sha256:[0-9a-f]{64}\Z")
_INSTANCE_FIELDS = {
    "repo",
    "instance_id",
    "base_commit",
    "patch",
    "test_patch",
    "problem_statement",
    "hints_text",
    "created_at",
    "version",
    "FAIL_TO_PASS",
    "PASS_TO_PASS",
    "environment_setup_commit",
    "difficulty",
}
_RESULT_FIELDS = {
    "schema_version",
    "evaluator_id",
    "swebench_source_commit",
    "attempt_id",
    "instance_id",
    "candidate_sha256",
    "dataset_sha256",
    "task_sha256",
    "image_manifest_sha256",
    "status",
    "valid_scored",
    "resolved",
    "fail_to_pass_passed",
    "fail_to_pass_total",
    "pass_to_pass_passed",
    "pass_to_pass_total",
    "score",
    "evaluator_seconds",
    "error_type",
    "error_summary",
    "trust_grade",
}


def _canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_once(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != content:
            raise RuntimeError("refusing to overwrite SWE-bench controller artifact")
        return
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, suffix=".swebench")
    try:
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary).replace(path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


@dataclass(frozen=True)
class SWEBenchVerifiedTask:
    instance: Mapping[str, Any]
    task_sha256: str
    locked_image_ref: str
    mutable_image_ref: str

    def __post_init__(self) -> None:
        if not isinstance(self.instance, Mapping) or set(self.instance) != _INSTANCE_FIELDS:
            raise ValueError("SWE-bench Verified task fields differ")
        instance_id = self.instance["instance_id"]
        if (
            not isinstance(instance_id, str)
            or _SAFE_ID.fullmatch(instance_id) is None
            or not isinstance(self.instance["base_commit"], str)
            or _COMMIT.fullmatch(self.instance["base_commit"]) is None
            or _SHA256.fullmatch(self.task_sha256) is None
            or self.task_sha256
            != hashlib.sha256(_canonical_bytes(dict(self.instance))).hexdigest()
            or not isinstance(self.locked_image_ref, str)
            or _IMAGE.fullmatch(self.locked_image_ref) is None
            or not isinstance(self.mutable_image_ref, str)
            or not self.mutable_image_ref.endswith(":latest")
        ):
            raise ValueError("SWE-bench Verified task binding differs")

    @property
    def instance_id(self) -> str:
        return str(self.instance["instance_id"])


@dataclass(frozen=True)
class SWEBenchVerifiedResult:
    schema_version: int
    evaluator_id: str
    swebench_source_commit: str
    attempt_id: str
    instance_id: str
    candidate_sha256: str
    dataset_sha256: str
    task_sha256: str
    image_manifest_sha256: str
    status: str
    valid_scored: bool
    resolved: bool
    fail_to_pass_passed: int
    fail_to_pass_total: int
    pass_to_pass_passed: int
    pass_to_pass_total: int
    score: float | None
    evaluator_seconds: float
    error_type: str
    error_summary: str
    trust_grade: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class SWEBenchVerifiedRemoteAdapter:
    """Invoke the pinned digest-locked SWE-bench worker behind an SSH boundary."""

    def __init__(
        self,
        *,
        task: SWEBenchVerifiedTask,
        host_alias: str,
        remote_python: str,
        remote_project_root: str,
        remote_swebench_source_root: str,
        remote_attempt_root: str,
        dataset_sha256: str = SWEBENCH_VERIFIED_DATASET_SHA256,
        timeout_seconds: int = 1800,
    ) -> None:
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", host_alias):
            raise ValueError("unsafe SWE-bench SSH host alias")
        for value in (
            remote_python,
            remote_project_root,
            remote_swebench_source_root,
            remote_attempt_root,
        ):
            if not value.startswith("/") or any(character.isspace() for character in value):
                raise ValueError("unsafe SWE-bench remote path")
        if _SHA256.fullmatch(dataset_sha256) is None:
            raise ValueError("invalid SWE-bench dataset sha256")
        if not isinstance(timeout_seconds, int) or not 60 <= timeout_seconds <= 3600:
            raise ValueError("SWE-bench timeout must be between 60 and 3600 seconds")
        self.task = task
        self.host_alias = host_alias
        self.remote_python = remote_python
        self.remote_project_root = remote_project_root.rstrip("/")
        self.remote_swebench_source_root = remote_swebench_source_root.rstrip("/")
        self.remote_attempt_root = remote_attempt_root.rstrip("/")
        self.dataset_sha256 = dataset_sha256
        self.timeout_seconds = timeout_seconds

    def evaluate(
        self, candidate_path: Path, private_result_path: Path
    ) -> SWEBenchVerifiedResult:
        candidate_path = candidate_path.resolve(strict=True)
        summary = validate_unified_diff(candidate_path)
        private_result_path = private_result_path.absolute()
        private_result_path.parent.mkdir(parents=True, exist_ok=True)
        attempt_id = self._attempt_id(
            instance_id=self.task.instance_id,
            candidate_sha256=summary.sha256,
            private_result_path=private_result_path,
        )
        request = {
            "schema_version": 1,
            "attempt_id": attempt_id,
            "instance_id": self.task.instance_id,
            "candidate_sha256": summary.sha256,
            "dataset_sha256": self.dataset_sha256,
            "task_sha256": self.task.task_sha256,
            "locked_image_ref": self.task.locked_image_ref,
            "mutable_image_ref": self.task.mutable_image_ref,
            "instance": dict(self.task.instance),
            "timeout_seconds": self.timeout_seconds,
        }
        request_path = private_result_path.parent / "controller-request.json"
        _write_once(request_path, _canonical_bytes(request))
        remote_dir = f"{self.remote_attempt_root}/{attempt_id}"
        remote_request = f"{remote_dir}/request.json"
        remote_candidate = f"{remote_dir}/candidate.patch"
        remote_result = f"{remote_dir}/supervisor.json"
        remote_work = f"{remote_dir}/work"
        self._run(("ssh", "-o", "BatchMode=yes", self.host_alias, "mkdir", "-p", remote_dir))
        self._run(("scp", "-q", str(request_path), f"{self.host_alias}:{remote_request}"))
        self._run(("scp", "-q", str(candidate_path), f"{self.host_alias}:{remote_candidate}"))
        worker_command = (
            "ssh",
            "-o",
            "BatchMode=yes",
            self.host_alias,
            "/usr/bin/env",
            f"PYTHONPATH={self.remote_project_root}:{self.remote_swebench_source_root}",
            self.remote_python,
            "-m",
            "optimization_lab.harness_builder.adapters.swebench_verified_worker",
            "--request",
            remote_request,
            "--candidate",
            remote_candidate,
            "--result",
            remote_result,
            "--work-root",
            remote_work,
        )
        completed = self._run(worker_command, accepted=(0, 2, 3), timeout=3700)
        temporary_result = private_result_path.parent / "remote-supervisor.json"
        self._run(("scp", "-q", f"{self.host_alias}:{remote_result}", str(temporary_result)))
        raw = temporary_result.read_bytes()
        result = self._parse_result(
            raw,
            expected_attempt_id=attempt_id,
            expected_candidate_sha256=summary.sha256,
        )
        expected_exit = 0 if result.status == "valid" else 2 if result.status == "contract_rejected" else 3
        if completed.returncode != expected_exit:
            raise RuntimeError("SWE-bench worker exit code and result disagree")
        _write_once(private_result_path, raw)
        return result

    @staticmethod
    def _attempt_id(
        *, instance_id: str, candidate_sha256: str, private_result_path: Path
    ) -> str:
        attempt_digest = hashlib.sha256(
            (
                instance_id
                + ":"
                + candidate_sha256
                + ":"
                + hashlib.sha256(str(private_result_path).encode()).hexdigest()
            ).encode()
        ).hexdigest()
        return f"swev-{attempt_digest}"

    @staticmethod
    def _run(
        argv: tuple[str, ...], *, accepted: tuple[int, ...] = (0,), timeout: int = 120
    ) -> subprocess.CompletedProcess[str]:
        completed = subprocess.run(
            argv,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=False,
        )
        if completed.returncode not in accepted:
            detail = " ".join((completed.stderr or completed.stdout).split())[-500:]
            raise RuntimeError(f"SWE-bench remote command failed: {detail}")
        return completed

    def _parse_result(
        self,
        raw: bytes,
        *,
        expected_attempt_id: str,
        expected_candidate_sha256: str,
    ) -> SWEBenchVerifiedResult:
        try:
            payload = json.loads(raw)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise RuntimeError("SWE-bench remote result is invalid JSON") from exc
        if (
            not isinstance(payload, dict)
            or set(payload) != _RESULT_FIELDS
            or _canonical_bytes(payload) != raw
        ):
            raise RuntimeError("SWE-bench remote result schema differs")
        result = SWEBenchVerifiedResult(**payload)
        if (
            result.schema_version != 1
            or result.evaluator_id != SWEBENCH_VERIFIED_EVALUATOR_ID
            or result.swebench_source_commit != SWEBENCH_SOURCE_COMMIT
            or result.attempt_id != expected_attempt_id
            or result.instance_id != self.task.instance_id
            or result.candidate_sha256 != expected_candidate_sha256
            or result.dataset_sha256 != self.dataset_sha256
            or result.task_sha256 != self.task.task_sha256
            or result.image_manifest_sha256
            != self.task.locked_image_ref.rsplit("@sha256:", 1)[1]
            or result.trust_grade
            != "official_standard_candidate_visible_test_process"
        ):
            raise RuntimeError("SWE-bench remote result binding differs")
        if result.valid_scored:
            if (
                result.status != "valid"
                or result.score is None
                or not 0 < result.score <= 1
                or result.resolved
                != (
                    result.fail_to_pass_passed == result.fail_to_pass_total
                    and result.pass_to_pass_passed == result.pass_to_pass_total
                )
            ):
                raise RuntimeError("SWE-bench scored result is inconsistent")
        elif result.score is not None or result.resolved:
            raise RuntimeError("unscored SWE-bench result exposed a score")
        return result


__all__ = [
    "SWEBENCH_VERIFIED_DATASET_SHA256",
    "SWEBenchVerifiedRemoteAdapter",
    "SWEBenchVerifiedResult",
    "SWEBenchVerifiedTask",
]
