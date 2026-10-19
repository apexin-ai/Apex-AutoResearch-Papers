from __future__ import annotations

import hashlib
import json
import math
import os
import re
import subprocess
import tarfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from ..dual_runtime import EvaluationResult, PublicEvaluation
from ..official_solutions import OfficialSolutionArchive
from ..solutions import SolutionArtifact


EDGE_BENCH_SOURCE_COMMIT = "a87350ab80eeb320b13cb71d1b0c3ffcc20a670f"
EDGE_BENCH_DATASET_REVISION = "6cc5a7f1b3288ce52484ad828177b8cc86b05b75"

_EDGE_TASK_TIMEOUTS = {
    "apple_incremental_game": 600,
    "molecular_self_assembly": 600,
    "treant_forest": 870,
}
_EDGE_TASK_IDENTITIES = {
    "apple_incremental_game": ("19021ddcbcaf966d7d43300b439862290a5c6c283aa6e6641f96efa07b34a25c", "16968d8ec7f2", "seededge/edgebench.judge.apple_incremental_game:16968d8ec7f2", "sha256:ca50e0754abb5dd1efd8387714206b8958fa7a4902ffadc03abad63139e26051"),
    "molecular_self_assembly": ("e8569e3a42da7c685fc93367701d844aefe2d4d9e541919fca298501efa41717", "96df6463f5e6", "seededge/edgebench.judge.molecular_self_assembly:96df6463f5e6", "sha256:4aa576558cb93ea2df285440cecc6481ed06fcd0c7ba68745bfbaba876f32478"),
    "treant_forest": ("2fdb98ce1166a1fea4743c2ae1613479bdf9eaf755cab190bfd931bc547a615e", "d47dc1a7da74", "seededge/edgebench.judge.treant_forest:d47dc1a7da74", "sha256:fcf625d92ea20623b9f998c5911de05fe5e32e9a5babbbe58fab6d4b2cdd1434"),
}
_SHA256 = re.compile(r"[0-9a-f]{64}")
_IMAGE_DIGEST = re.compile(r"sha256:[0-9a-f]{64}")
_OPERATION_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_EVALUATOR_COMMAND = ("sforge", "eval")


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


def _write_once(path: Path, content: bytes, *, label: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    try:
        descriptor = os.open(path, flags, 0o600)
    except FileExistsError as exc:
        raise ValueError(f"{label} already exists") from exc
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    except Exception:
        path.unlink(missing_ok=True)
        raise
    return path


def _numeric_score(value: object) -> float:
    if (
        not isinstance(value, (int, float))
        or isinstance(value, bool)
        or not math.isfinite(float(value))
    ):
        raise RuntimeError("EdgeBench official report score is invalid")
    return float(value)


def _report_score(report: Mapping[str, object]) -> float:
    value = report.get("score")
    if value is not None:
        return _numeric_score(value)

    counts = tuple(report.get(key) for key in ("total_tests", "passed", "failed", "errors"))
    if (
        report.get("valid") is not True
        or report.get("timed_out") is not False
        or report.get("score_0_100") is not None
        or any(type(count) is not int or count < 0 for count in counts)
    ):
        raise RuntimeError("EdgeBench official report score is invalid")
    total_tests, passed, failed, errors = counts
    pass_rate = report.get("pass_rate")
    if (
        total_tests <= 0
        or passed + failed + errors != total_tests
        or failed + errors <= 0
        or not isinstance(pass_rate, (int, float))
        or isinstance(pass_rate, bool)
        or not math.isfinite(float(pass_rate))
        or not math.isclose(float(pass_rate), passed / total_tests, abs_tol=1e-12)
    ):
        raise RuntimeError("EdgeBench official report score is invalid")
    return 0.0


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sforge_path(contract: "EdgeBenchContract") -> Path:
    return contract.sforge_executable


@dataclass(frozen=True)
class EdgeBenchContract:
    source_root: Path
    dataset_root: Path
    sforge_executable: Path
    source_commit: str
    dataset_revision: str
    task_id: str
    docker_image_reference: str
    docker_image_digest: str
    timeout_seconds: int
    score_direction: str
    evaluator_command: tuple[str, str]

    def __post_init__(self) -> None:
        object.__setattr__(self, "source_root", Path(self.source_root).resolve())
        object.__setattr__(self, "dataset_root", Path(self.dataset_root).resolve())
        object.__setattr__(self, "sforge_executable", Path(self.sforge_executable).resolve())
        if self.source_commit != EDGE_BENCH_SOURCE_COMMIT:
            raise ValueError("EdgeBench source commit differs")
        if self.dataset_revision != EDGE_BENCH_DATASET_REVISION:
            raise ValueError("EdgeBench dataset revision differs")
        if self.task_id not in _EDGE_TASK_TIMEOUTS:
            raise ValueError("EdgeBench task ID is outside the frozen experiment")
        _, _, expected_reference, expected_digest = _EDGE_TASK_IDENTITIES[self.task_id]
        if self.docker_image_reference != expected_reference or self.docker_image_digest != expected_digest:
            raise ValueError("EdgeBench Docker image identity differs")
        if (
            type(self.timeout_seconds) is not int
            or self.timeout_seconds != _EDGE_TASK_TIMEOUTS[self.task_id]
        ):
            raise ValueError("EdgeBench evaluator timeout differs")
        if self.score_direction != "maximize":
            raise ValueError("EdgeBench score direction differs")
        if self.evaluator_command != _EVALUATOR_COMMAND:
            raise ValueError("EdgeBench evaluator command differs")
        if (
            not isinstance(self.docker_image_reference, str)
            or not self.docker_image_reference.strip()
            or _IMAGE_DIGEST.fullmatch(self.docker_image_digest) is None
        ):
            raise ValueError("EdgeBench Docker image identity is invalid")


@dataclass(frozen=True)
class ObservedEdgeBenchIdentity:
    source_commit: str
    dataset_revision: str
    task_id: str
    docker_image_digest: str
    timeout_seconds: int
    score_direction: str
    evaluator_command: tuple[str, str]
    task_json_sha256: str
    sforge_executable: str
    sforge_module_path: str
    direct_url_source: str


Runner = Callable[..., Any]
IdentityProbe = Callable[[EdgeBenchContract], ObservedEdgeBenchIdentity]


class EdgeBenchOfficialAdapter:
    """Evaluate one archived file bundle with the pinned SForge evaluator."""

    def __init__(
        self,
        *,
        contract: EdgeBenchContract,
        solution_archive: OfficialSolutionArchive,
        attempt_root: Path,
        private_evidence_root: Path,
        runner: Runner = subprocess.run,
        identity_probe: IdentityProbe | None = None,
    ) -> None:
        if not isinstance(contract, EdgeBenchContract):
            raise TypeError("contract must be EdgeBenchContract")
        if not isinstance(solution_archive, OfficialSolutionArchive):
            raise TypeError("solution_archive must be OfficialSolutionArchive")
        self.contract = contract
        self.solution_archive = solution_archive
        self.attempt_root = Path(attempt_root).resolve()
        self.private_evidence_root = Path(private_evidence_root).resolve()
        self.runner = runner
        self.identity_probe = identity_probe or _probe_identity

    def evaluate(
        self, artifact: SolutionArtifact, *, operation_id: str
    ) -> EvaluationResult:
        if not isinstance(artifact, SolutionArtifact):
            raise TypeError("artifact must be SolutionArtifact")
        if artifact.artifact_kind != "edgebench_file_bundle_v1":
            raise ValueError("EdgeBench artifact kind differs")
        if not isinstance(operation_id, str) or _OPERATION_ID.fullmatch(operation_id) is None:
            raise ValueError("EdgeBench operation ID is invalid")
        self._verify_identity()

        attempt = self.attempt_root / operation_id
        if os.path.lexists(attempt):
            raise ValueError("EdgeBench attempt already exists")
        attempt.mkdir(parents=True)
        archived = self.solution_archive.store(artifact)
        bundle_root = self.solution_archive.materialize_edge_bundle(
            archived.artifact_sha256, attempt / "bundle"
        )
        archive_path = attempt / "submission.tar.gz"
        _create_tar_archive(bundle_root, archive_path)
        log_root = attempt / "logs"

        command = [
            str(_sforge_path(self.contract)),
            "--silent",
            "eval",
            "--backend",
            "docker",
            "--task",
            self.contract.task_id,
            "--archive",
            str(archive_path),
            "--run-id",
            operation_id,
            "--timeout",
            str(self.contract.timeout_seconds),
            "--json",
        ]
        evaluator_env = os.environ.copy()
        evaluator_env["SFORGE_LOG_DIR"] = str(log_root)
        evaluator_env["SFORGE_TASKS_DIR"] = str(self.contract.dataset_root)
        try:
            completed = self.runner(
            command,
            cwd=self.contract.source_root,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=self.contract.timeout_seconds + 30,
            check=False,
            shell=False,
            env=evaluator_env,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError("EdgeBench evaluator infrastructure timeout") from exc
        report_path = (
            log_root
            / "runs"
            / operation_id
            / self.contract.task_id
            / "submissions"
            / "manual-1"
            / "report.json"
        )
        report = _read_report(report_path)
        if (
            getattr(completed, "returncode", None) != 0
            or report.get("task_id") != self.contract.task_id
            or report.get("submission_id") != operation_id
        ):
            raise RuntimeError("EdgeBench official report binding differs")
        valid = report.get("valid")
        timed_out = report.get("timed_out")
        if type(valid) is not bool or type(timed_out) is not bool:
            raise RuntimeError("EdgeBench official report validity differs")
        score = _report_score(report)

        private_payload = {
            "schema_version": 1,
            "benchmark": "edgebench",
            "operation_id": operation_id,
            "candidate_sha256": artifact.sha256,
            "contract": _contract_payload(self.contract),
            "command": command,
            "returncode": completed.returncode,
            "stdout": getattr(completed, "stdout", ""),
            "stderr": getattr(completed, "stderr", ""),
            "report_path": str(report_path),
            "report": report,
        }
        evidence_path = _write_once(
            self.private_evidence_root / f"{operation_id}.edgebench.json",
            _canonical_bytes(private_payload),
            label="EdgeBench private evidence",
        )
        evidence_sha256 = hashlib.sha256(evidence_path.read_bytes()).hexdigest()
        if timed_out:
            status = "TIMED_OUT"
            reason = "official_evaluation_timed_out"
        elif valid:
            status = "COMPLETED"
            reason = "official_evaluation_completed"
        else:
            status = "INVALID"
            reason = "official_evaluation_invalid"
        feedback = _canonical_feedback(
            status=status,
            reason=reason,
            score=score,
            validity=valid,
        )
        return EvaluationResult(
            public=PublicEvaluation(score=score, feedback=feedback),
            private={
                "evidence_path": str(evidence_path),
                "evidence_sha256": evidence_sha256,
            },
        )

    def _verify_identity(self) -> None:
        observed = self.identity_probe(self.contract)
        if not isinstance(observed, ObservedEdgeBenchIdentity):
            raise RuntimeError("EdgeBench identity probe result is invalid")
        expected = ObservedEdgeBenchIdentity(
            source_commit=self.contract.source_commit,
            dataset_revision=self.contract.dataset_revision,
            task_id=self.contract.task_id,
            docker_image_digest=self.contract.docker_image_digest,
            timeout_seconds=self.contract.timeout_seconds,
            score_direction=self.contract.score_direction,
            evaluator_command=self.contract.evaluator_command,
            task_json_sha256=_EDGE_TASK_IDENTITIES[self.contract.task_id][0],
            sforge_executable=_sforge_path(self.contract).as_posix(),
            sforge_module_path=observed.sforge_module_path,
            direct_url_source=self.contract.source_root.as_uri(),
        )
        if observed != expected:
            raise RuntimeError("EdgeBench evaluator identity differs")


def _contract_payload(contract: EdgeBenchContract) -> dict[str, object]:
    payload = asdict(contract)
    payload["source_root"] = str(contract.source_root)
    payload["dataset_root"] = str(contract.dataset_root)
    payload["sforge_executable"] = str(contract.sforge_executable)
    payload["evaluator_command"] = list(contract.evaluator_command)
    return payload


def _canonical_feedback(
    *, status: str, reason: str, score: float, validity: bool
) -> str:
    return _canonical_bytes(
        {
            "status": status,
            "reason": reason,
            "aggregate_score": score,
            "validity": validity,
        }
    ).decode("utf-8").rstrip("\n")


def _create_tar_archive(bundle_root: Path, archive_path: Path) -> None:
    with tarfile.open(archive_path, mode="w:gz") as archive:
        for path in sorted(bundle_root.rglob("*")):
            if not path.is_file() or path.is_symlink():
                raise RuntimeError("EdgeBench materialized bundle contains an invalid entry")
            archive.add(path, arcname=path.relative_to(bundle_root).as_posix())


def _read_report(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
        payload = json.loads(raw)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("EdgeBench official report is unavailable") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("EdgeBench official report schema differs")
    return payload


def _run_identity_command(command: Sequence[str], *, cwd: Path | None = None) -> str:
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=30,
        check=False,
        shell=False,
    )
    if completed.returncode != 0:
        raise RuntimeError("EdgeBench identity probe failed")
    return completed.stdout.strip()


def _probe_identity(contract: EdgeBenchContract) -> ObservedEdgeBenchIdentity:
    sforge_executable = _sforge_path(contract)
    if not sforge_executable.is_file():
        raise RuntimeError("EdgeBench sforge executable is unavailable")
    source_commit = _run_identity_command(
        ("git", "rev-parse", "HEAD"), cwd=contract.source_root
    )
    if _run_identity_command(("git", "status", "--porcelain=v1"), cwd=contract.source_root):
        raise RuntimeError("EdgeBench source checkout is dirty")
    python_executable = sforge_executable.parent / "python"
    identity_json = _run_identity_command((str(python_executable), "-c", "import importlib.metadata,json,sforge; print(json.dumps({'module':sforge.__file__,'direct_url':json.loads(importlib.metadata.distribution('sforge').read_text('direct_url.json'))['url']}))"))
    try:
        package_identity = json.loads(identity_json)
        sforge_module_path = Path(package_identity["module"]).resolve()
        direct_url_source = package_identity["direct_url"]
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise RuntimeError("EdgeBench sforge package identity is invalid") from exc
    if direct_url_source != contract.source_root.as_uri():
        raise RuntimeError("EdgeBench sforge package source differs")
    metadata_path = contract.dataset_root / ".cache" / "huggingface" / "download" / f"{contract.task_id}.json.metadata"
    try:
        dataset_revision = metadata_path.read_text(encoding="utf-8").splitlines()[0]
    except (OSError, UnicodeError, IndexError) as exc:
        raise RuntimeError("EdgeBench dataset revision metadata is unavailable") from exc
    task_path = contract.dataset_root / f"{contract.task_id}.json"
    expected_task_sha, expected_image_tag, _, _ = _EDGE_TASK_IDENTITIES[contract.task_id]
    try:
        task_json_sha256 = _sha256_file(task_path)
    except OSError as exc:
        raise RuntimeError("EdgeBench task identity is unavailable") from exc
    if task_json_sha256 != expected_task_sha:
        raise RuntimeError("EdgeBench task data digest differs")
    try:
        task = json.loads(task_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("EdgeBench task identity is unavailable") from exc
    judge = task.get("judge") if isinstance(task, Mapping) else None
    if not isinstance(judge, Mapping):
        raise RuntimeError("EdgeBench task identity is invalid")
    if judge.get("image_tag") != expected_image_tag:
        raise RuntimeError("EdgeBench judge image tag differs")
    docker_digest = _run_identity_command(
        (
            "docker",
            "image",
            "inspect",
            "--format",
            "{{.Id}}",
            contract.docker_image_reference,
        )
    )
    return ObservedEdgeBenchIdentity(
        source_commit=source_commit,
        dataset_revision=dataset_revision,
        task_id=task.get("task_id"),
        docker_image_digest=docker_digest,
        timeout_seconds=judge.get("eval_timeout"),
        score_direction=judge.get("score_direction"),
        evaluator_command=_EVALUATOR_COMMAND,
        task_json_sha256=task_json_sha256,
        sforge_executable=sforge_executable.as_posix(),
        sforge_module_path=sforge_module_path.as_posix(),
        direct_url_source=direct_url_source,
    )


__all__ = [
    "EDGE_BENCH_DATASET_REVISION",
    "EDGE_BENCH_SOURCE_COMMIT",
    "EdgeBenchContract",
    "EdgeBenchOfficialAdapter",
    "ObservedEdgeBenchIdentity",
]
