from __future__ import annotations

import hashlib
import json
import math
import os
import re
import site
import subprocess
import sys
from contextlib import contextmanager, nullcontext
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from ..dual_runtime import EvaluationResult, PublicEvaluation
from ..experiment_one import FreezeReceipt
from ..solutions import SolutionArtifact


ALE_BENCH_SOURCE_COMMIT = "f7d927906dc1dcd860ee086e4560d576438b1354"
ALE_BENCH_DATASET_REVISION = "0f426173b4e4e73b09b2b3631ae0490f66b75f99"

_ALE_TASK_LIMITS = {
    "ahc024": (2, 1 << 30),
    "ahc026": (2, 1 << 30),
    "ahc011": (3, 1 << 30),
}
_ALE_TASK_ZIP_SHA256 = {
    "ahc024": "b4f02d3cbcea3200d3e7d29dcf27b1e0bcce1fb566ed249541683114f7986585",
    "ahc026": "c9acb296ceff4948df2cb000459d8153af4ba8ddb60c987b565e19b628dd845a",
    "ahc011": "6d26e9ea3dbd8b97616d9727bdbe0db270d0df9ab54efd44c71f1c03379a03fb",
}
_DOCKER_IMAGE_REFERENCE = "ale-bench:cpp23-202301"
_DOCKER_IMAGE_DIGEST = "sha256:e0ec0e015b3e11fda1ecdd0df270f83cee12136b37bbac438e8c861b4dfd420e"
_JUDGE_VERSION = "202301"
_PUBLIC_EVALUATOR_COMMAND = ("ale_bench.Session", "public_eval")
_PRIVATE_EVALUATOR_COMMAND = ("ale_bench.Session", "private_eval")
_IMAGE_DIGEST = re.compile(r"sha256:[0-9a-f]{64}")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_OPERATION_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")


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


def _numeric_score(value: object, *, label: str) -> float:
    if (
        not isinstance(value, (int, float))
        or isinstance(value, bool)
        or not math.isfinite(float(value))
    ):
        raise RuntimeError(f"ALE-Bench {label} score is invalid")
    return float(value)


def _judge_name(value: object) -> str:
    if isinstance(value, Enum):
        value = value.value
    if not isinstance(value, str) or not value:
        raise RuntimeError("ALE-Bench judge result is invalid")
    return value


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sha256_json(payload: object) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True)
class ALEBenchContract:
    source_root: Path
    dataset_root: Path
    python_executable: Path
    source_commit: str
    dataset_revision: str
    task_id: str
    docker_image_reference: str
    docker_image_digest: str
    judge_version: str
    time_limit_seconds: int
    memory_limit_bytes: int
    score_direction: str
    public_evaluator_command: tuple[str, str]
    private_evaluator_command: tuple[str, str]

    def __post_init__(self) -> None:
        object.__setattr__(self, "source_root", Path(self.source_root).resolve())
        object.__setattr__(self, "dataset_root", Path(self.dataset_root).resolve())
        # Keep the virtual-environment entry point intact. ``bin/python`` is
        # commonly a symlink to the system interpreter; resolving it here
        # would silently discard the ALE-Bench environment and make the
        # identity probe import a different Python installation.
        object.__setattr__(self, "python_executable", Path(self.python_executable).absolute())
        if self.source_commit != ALE_BENCH_SOURCE_COMMIT:
            raise ValueError("ALE-Bench source commit differs")
        if self.dataset_revision != ALE_BENCH_DATASET_REVISION:
            raise ValueError("ALE-Bench dataset revision differs")
        if self.task_id not in _ALE_TASK_LIMITS:
            raise ValueError("ALE-Bench task ID is outside the frozen experiment")
        expected_time, expected_memory = _ALE_TASK_LIMITS[self.task_id]
        if type(self.time_limit_seconds) is not int or self.time_limit_seconds != expected_time:
            raise ValueError("ALE-Bench time limit differs")
        if type(self.memory_limit_bytes) is not int or self.memory_limit_bytes != expected_memory:
            raise ValueError("ALE-Bench memory limit differs")
        if self.docker_image_reference != _DOCKER_IMAGE_REFERENCE:
            raise ValueError("ALE-Bench Docker image reference differs")
        if self.docker_image_digest != _DOCKER_IMAGE_DIGEST:
            raise ValueError("ALE-Bench Docker image digest differs")
        if self.judge_version != _JUDGE_VERSION:
            raise ValueError("ALE-Bench judge version differs")
        if self.score_direction != "maximize":
            raise ValueError("ALE-Bench score direction differs")
        if self.public_evaluator_command != _PUBLIC_EVALUATOR_COMMAND:
            raise ValueError("ALE-Bench public evaluator command differs")
        if self.private_evaluator_command != _PRIVATE_EVALUATOR_COMMAND:
            raise ValueError("ALE-Bench private evaluator command differs")


@dataclass(frozen=True)
class ObservedALEBenchIdentity:
    source_commit: str
    dataset_revision: str
    task_id: str
    docker_image_digest: str
    judge_version: str
    time_limit_seconds: int
    memory_limit_bytes: int
    score_direction: str
    public_evaluator_command: tuple[str, str]
    private_evaluator_command: tuple[str, str]
    task_zip_sha256: str = ""
    ale_module_path: str = ""
    direct_url_source: str = ""


@dataclass(frozen=True)
class FreezeAuthorization:
    freeze_receipt_path: Path
    freeze_receipt_bytes_sha256: str
    freeze_receipt_sha256: str
    evaluator_receipt_path: Path
    private_evidence_path: Path
    execution_contract_sha256: str
    harness_sha256: str
    ancestry_sha256s: tuple[str, ...]
    candidate_sha256: str
    benchmark: str
    target_id: str
    official_public_score: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "freeze_receipt_path", Path(self.freeze_receipt_path).resolve())
        object.__setattr__(self, "evaluator_receipt_path", Path(self.evaluator_receipt_path).resolve())
        object.__setattr__(self, "private_evidence_path", Path(self.private_evidence_path).resolve())
        for value in (
            self.freeze_receipt_bytes_sha256,
            self.freeze_receipt_sha256,
            self.execution_contract_sha256,
            self.harness_sha256,
            self.candidate_sha256,
        ):
            if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
                raise ValueError("ALE-Bench freeze authorization hash is invalid")
        if not self.ancestry_sha256s or self.ancestry_sha256s[-1] != self.harness_sha256:
            raise ValueError("ALE-Bench freeze authorization lineage differs")
        for value in self.ancestry_sha256s:
            if _SHA256.fullmatch(value) is None:
                raise ValueError("ALE-Bench freeze authorization lineage hash is invalid")
        if not self.freeze_receipt_path.is_file() or not self.evaluator_receipt_path.is_file() or not self.private_evidence_path.is_file():
            raise ValueError("ALE-Bench freeze authorization evidence is unavailable")
        if self.benchmark != "alebench":
            raise ValueError("ALE-Bench freeze authorization benchmark differs")
        if not isinstance(self.target_id, str) or not self.target_id:
            raise ValueError("ALE-Bench freeze authorization target is invalid")
        _numeric_score(self.official_public_score, label="authorized public")


SessionFactory = Callable[..., Any]
IdentityProbe = Callable[[ALEBenchContract], ObservedALEBenchIdentity]


class ALEBenchOfficialAdapter:
    """Run the official ALE-Bench public or authorized private evaluator."""

    def __init__(
        self,
        *,
        contract: ALEBenchContract,
        private_evidence_root: Path,
        session_factory: SessionFactory | None = None,
        identity_probe: IdentityProbe | None = None,
    ) -> None:
        if not isinstance(contract, ALEBenchContract):
            raise TypeError("contract must be ALEBenchContract")
        self.contract = contract
        self.private_evidence_root = Path(private_evidence_root).resolve()
        self.session_factory = session_factory or _start_session
        self.identity_probe = identity_probe or _probe_identity

    @property
    def execution_contract_sha256(self) -> str:
        return hashlib.sha256(_canonical_bytes(_contract_payload(self.contract))).hexdigest()

    def evaluate_public(
        self, artifact: SolutionArtifact, *, operation_id: str
    ) -> EvaluationResult:
        self._validate_artifact_and_operation(artifact, operation_id)
        self._verify_identity()
        environment = (
            _target_python_environment(self.contract)
            if self.session_factory is _start_session
            else nullcontext()
        )
        with environment:
            session = self._create_session(maximum_num_call_public_eval=1)
            self._verify_session(session)
            result = session.public_eval(
                code=artifact.text,
                code_language="cpp23",
                judge_version=self.contract.judge_version,
                skip_local_visualization=True,
                reuse_containers=False,
            )
        score = _numeric_score(
            getattr(result, "overall_absolute_score", None), label="public"
        )
        judge = _judge_name(getattr(result, "overall_judge_result", None))
        self._verify_resource_usage(result, public_calls=1, private_calls=0)
        evidence_path, evidence_sha256 = self._write_evidence(
            operation_id=operation_id,
            payload={
                "schema_version": 1,
                "benchmark": "alebench",
                "phase": "public",
                "operation_id": operation_id,
                "candidate_sha256": artifact.sha256,
                "contract": _contract_payload(self.contract),
                "result": _result_payload(result),
            },
        )
        feedback = _canonical_feedback(
            status=judge,
            reason="official_public_eval_completed",
            score=score,
            validity=True,
        )
        return EvaluationResult(
            public=PublicEvaluation(score=score, feedback=feedback),
            private={
                "evidence_path": str(evidence_path),
                "evidence_sha256": evidence_sha256,
            },
        )

    def evaluate_private(
        self,
        artifact: SolutionArtifact,
        *,
        operation_id: str,
        authorization: [REDACTED],
    ) -> EvaluationResult:
        if not isinstance(authorization, FreezeAuthorization):
            raise TypeError("authorization must be FreezeAuthorization")
        self._validate_artifact_and_operation(artifact, operation_id)
        if (
            authorization.benchmark != "alebench"
            or authorization.target_id != self.contract.task_id
            or authorization.candidate_sha256 != artifact.sha256
        ):
            raise ValueError("ALE-Bench freeze authorization binding differs")
        self._verify_freeze_authorization(authorization)
        self._verify_identity()
        environment = (
            _target_python_environment(self.contract)
            if self.session_factory is _start_session
            else nullcontext()
        )
        with environment:
            session = self._create_session(maximum_num_call_public_eval=0)
            self._verify_session(session)
            private_result = session.private_eval(
                code=artifact.text,
                code_language="cpp23",
                judge_version=self.contract.judge_version,
                reuse_containers=False,
            )
        if not isinstance(private_result, tuple) or len(private_result) != 3:
            raise RuntimeError("ALE-Bench private evaluator result is invalid")
        result, rank, performance = private_result
        _numeric_score(getattr(result, "overall_absolute_score", None), label="private")
        _judge_name(getattr(result, "overall_judge_result", None))
        self._verify_resource_usage(result, public_calls=0, private_calls=1)
        if type(rank) is not int or type(performance) is not int:
            raise RuntimeError("ALE-Bench private rank or performance is invalid")
        evidence_path, evidence_sha256 = self._write_evidence(
            operation_id=operation_id,
            payload={
                "schema_version": 1,
                "benchmark": "alebench",
                "phase": "private",
                "operation_id": operation_id,
                "candidate_sha256": artifact.sha256,
                "contract": _contract_payload(self.contract),
                "authorization": [REDACTED],
                "result": _result_payload(result),
                "rank": rank,
                "performance": performance,
            },
        )
        feedback = _canonical_feedback(
            status="WITHHELD",
            reason="official_private_eval_withheld",
            score=None,
            validity=True,
        )
        return EvaluationResult(
            public=PublicEvaluation(score=None, feedback=feedback),
            private={
                "evidence_path": str(evidence_path),
                "evidence_sha256": evidence_sha256,
            },
        )

    def _validate_artifact_and_operation(
        self, artifact: SolutionArtifact, operation_id: str
    ) -> None:
        if not isinstance(artifact, SolutionArtifact):
            raise TypeError("artifact must be SolutionArtifact")
        if artifact.artifact_kind != "alebench_source_cpp23":
            raise ValueError("ALE-Bench artifact kind differs")
        if not isinstance(operation_id, str) or _OPERATION_ID.fullmatch(operation_id) is None:
            raise ValueError("ALE-Bench operation ID is invalid")

    def _verify_identity(self) -> None:
        observed = self.identity_probe(self.contract)
        if not isinstance(observed, ObservedALEBenchIdentity):
            raise RuntimeError("ALE-Bench identity probe result is invalid")
        expected = ObservedALEBenchIdentity(
            source_commit=self.contract.source_commit,
            dataset_revision=self.contract.dataset_revision,
            task_id=self.contract.task_id,
            docker_image_digest=self.contract.docker_image_digest,
            judge_version=self.contract.judge_version,
            time_limit_seconds=self.contract.time_limit_seconds,
            memory_limit_bytes=self.contract.memory_limit_bytes,
            score_direction=self.contract.score_direction,
            public_evaluator_command=self.contract.public_evaluator_command,
            private_evaluator_command=self.contract.private_evaluator_command,
            task_zip_sha256=_ALE_TASK_ZIP_SHA256[self.contract.task_id],
            ale_module_path=observed.ale_module_path,
            direct_url_source=self.contract.source_root.as_uri(),
        )
        if observed != expected:
            raise RuntimeError("ALE-Bench evaluator identity differs")

    def _create_session(self, *, maximum_num_call_public_eval: int) -> Any:
        with _frozen_cache_environment(self.contract):
            return self.session_factory(
                problem_id=self.contract.task_id,
                lite_version=False,
                maximum_num_call_public_eval=maximum_num_call_public_eval,
                num_workers=1,
                run_visualization_server=False,
            )

    def _verify_freeze_authorization(self, authorization: [REDACTED] -> None:
        if _sha256_file(authorization.freeze_receipt_path) != authorization.freeze_receipt_bytes_sha256:
            raise ValueError("ALE-Bench freeze receipt bytes differ")
        try:
            envelope = json.loads(authorization.freeze_receipt_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise ValueError("ALE-Bench freeze receipt integrity differs") from exc
        if not isinstance(envelope, Mapping) or set(envelope) != {"schema_version", "payload", "payload_sha256"} or envelope.get("schema_version") != 1 or not isinstance(envelope.get("payload"), Mapping):
            raise ValueError("ALE-Bench freeze receipt integrity differs")
        if _sha256_json(envelope["payload"]) != envelope.get("payload_sha256"):
            raise ValueError("ALE-Bench freeze receipt integrity differs")
        receipt = FreezeReceipt.from_dict(envelope["payload"])
        if (
            receipt.sha256 != authorization.freeze_receipt_sha256
            or receipt.benchmark != authorization.benchmark
            or receipt.task_id != authorization.target_id
            or receipt.candidate_sha256 != authorization.candidate_sha256
            or receipt.harness_sha256 != authorization.harness_sha256
            or receipt.ancestry_sha256s != authorization.ancestry_sha256s
            or receipt.official_score != authorization.official_public_score
            or receipt.evaluator_contract_sha256 != authorization.execution_contract_sha256
            or authorization.execution_contract_sha256 != self.execution_contract_sha256
            or _sha256_file(authorization.evaluator_receipt_path) != receipt.evaluator_receipt_sha256
            or _sha256_file(authorization.private_evidence_path) != receipt.private_evidence_sha256
        ):
            raise ValueError("ALE-Bench freeze authorization binding differs")

    def _verify_session(self, session: Any) -> None:
        constraints = getattr(getattr(session, "problem", None), "constraints", None)
        if (
            getattr(session, "problem_id", None) != self.contract.task_id
            or getattr(constraints, "time_limit", None) != self.contract.time_limit_seconds
            or getattr(constraints, "memory_limit", None) != self.contract.memory_limit_bytes
        ):
            raise RuntimeError("ALE-Bench session identity differs")

    @staticmethod
    def _verify_resource_usage(
        result: Any, *, public_calls: int, private_calls: int
    ) -> None:
        usage = getattr(result, "resource_usage", None)
        if (
            getattr(usage, "num_call_public_eval", None) != public_calls
            or getattr(usage, "num_call_private_eval", None) != private_calls
        ):
            raise RuntimeError("ALE-Bench evaluator resource usage differs")

    def _write_evidence(
        self, *, operation_id: str, payload: Mapping[str, object]
    ) -> tuple[Path, str]:
        content = _canonical_bytes(payload)
        path = self.private_evidence_root / f"{operation_id}.json"
        _write_once(path, content, label="ALE-Bench private evidence")
        return path, hashlib.sha256(content).hexdigest()


def _contract_payload(contract: ALEBenchContract) -> dict[str, object]:
    payload = asdict(contract)
    payload["source_root"] = str(contract.source_root)
    payload["dataset_root"] = str(contract.dataset_root)
    payload["python_executable"] = str(contract.python_executable)
    payload["public_evaluator_command"] = list(contract.public_evaluator_command)
    payload["private_evaluator_command"] = list(contract.private_evaluator_command)
    return payload


def _authorization_payload(
    authorization: [REDACTED],
) -> dict[str, object]:
    payload = asdict(authorization)
    payload["freeze_receipt_path"] = str(authorization.freeze_receipt_path)
    payload["evaluator_receipt_path"] = str(authorization.evaluator_receipt_path)
    payload["private_evidence_path"] = str(authorization.private_evidence_path)
    payload["ancestry_sha256s"] = list(authorization.ancestry_sha256s)
    return payload


def _canonical_feedback(
    *, status: str, reason: str, score: float | None, validity: bool
) -> str:
    return _canonical_bytes(
        {
            "status": status,
            "reason": reason,
            "aggregate_score": score,
            "validity": validity,
        }
    ).decode("utf-8").rstrip("\n")


def _result_payload(result: Any) -> Mapping[str, object]:
    model_dump = getattr(result, "model_dump", None)
    if not callable(model_dump):
        raise RuntimeError("ALE-Bench evaluator result schema differs")
    payload = model_dump(mode="json")
    if not isinstance(payload, Mapping):
        raise RuntimeError("ALE-Bench evaluator result schema differs")
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
        raise RuntimeError("ALE-Bench identity probe failed")
    return completed.stdout.strip()


def _target_python_sys_path(python_executable: Path) -> tuple[Path, ...]:
    """Return usable package directories from the contract's interpreter."""

    raw = _run_identity_command(
        (
            str(python_executable),
            "-c",
            "import json,sys; print(json.dumps(sys.path))",
        )
    )
    try:
        values = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("ALE-Bench Python environment path is invalid") from exc
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        raise RuntimeError("ALE-Bench Python environment path is invalid")
    paths: list[Path] = []
    for value in values:
        if not value:
            continue
        candidate = Path(value)
        if not candidate.is_dir():
            continue
        # The official package and its dependencies live in site-packages (or
        # dist-packages).  Avoid replacing the controller's standard library.
        if candidate.name not in {"site-packages", "dist-packages"}:
            continue
        candidate = candidate.absolute()
        if candidate not in paths:
            paths.append(candidate)
    if not paths:
        raise RuntimeError("ALE-Bench Python environment has no package path")
    return tuple(paths)


@contextmanager
def _target_python_environment(contract: ALEBenchContract):
    """Temporarily make the frozen ALE package environment importable.

    ALE-Bench is installed in a dedicated virtualenv while Moss's controller
    runs in another one.  Running ``site.addsitedir`` is important here: it
    processes editable-install ``.pth`` files, which a plain ``sys.path``
    append would not do.  The original path is restored after the evaluator
    call so one adapter cannot contaminate another benchmark in the process.
    """

    original_sys_path = list(sys.path)
    try:
        for package_path in _target_python_sys_path(contract.python_executable):
            site.addsitedir(str(package_path))
            package_text = str(package_path)
            while package_text in sys.path:
                sys.path.remove(package_text)
            sys.path.insert(0, package_text)
        yield
    finally:
        sys.path[:] = original_sys_path


def _start_session(**kwargs: object) -> Any:
    try:
        from ale_bench import start
    except ImportError as exc:
        raise RuntimeError("ALE-Bench package is unavailable") from exc
    return start(**kwargs)


@contextmanager
def _frozen_cache_environment(contract: ALEBenchContract):
    previous_cache = os.environ.get("ALE_BENCH_CACHE")
    previous_offline = os.environ.get("HF_HUB_OFFLINE")
    os.environ["ALE_BENCH_CACHE"] = str(contract.dataset_root.parent)
    os.environ["HF_HUB_OFFLINE"] = "1"
    try:
        yield
    finally:
        if previous_cache is None:
            os.environ.pop("ALE_BENCH_CACHE", None)
        else:
            os.environ["ALE_BENCH_CACHE"] = previous_cache
        if previous_offline is None:
            os.environ.pop("HF_HUB_OFFLINE", None)
        else:
            os.environ["HF_HUB_OFFLINE"] = previous_offline


def _probe_identity(contract: ALEBenchContract) -> ObservedALEBenchIdentity:
    if not contract.python_executable.is_file():
        raise RuntimeError("ALE-Bench Python executable is unavailable")
    source_commit = _run_identity_command(
        ("git", "rev-parse", "HEAD"), cwd=contract.source_root
    )
    if _run_identity_command(("git", "status", "--porcelain=v1"), cwd=contract.source_root):
        raise RuntimeError("ALE-Bench source checkout is dirty")
    try:
        dataset_revision = (contract.dataset_root / "refs" / "main").read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError) as exc:
        raise RuntimeError("ALE-Bench dataset revision is unavailable") from exc
    task_zip = contract.dataset_root / "snapshots" / dataset_revision / f"{contract.task_id}.zip"
    try:
        task_zip_sha256 = _sha256_file(task_zip)
    except OSError as exc:
        raise RuntimeError("ALE-Bench task snapshot is unavailable") from exc
    if task_zip_sha256 != _ALE_TASK_ZIP_SHA256[contract.task_id]:
        raise RuntimeError("ALE-Bench task snapshot digest differs")
    package_json = _run_identity_command((str(contract.python_executable), "-c", "import ale_bench,importlib.metadata,json; print(json.dumps({'module':ale_bench.__file__,'direct_url':json.loads(importlib.metadata.distribution('ale-bench').read_text('direct_url.json'))['url']}))"))
    try:
        package_identity = json.loads(package_json)
        ale_module_path = Path(package_identity["module"]).resolve()
        direct_url_source = package_identity["direct_url"]
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise RuntimeError("ALE-Bench package identity is invalid") from exc
    if direct_url_source != contract.source_root.as_uri():
        raise RuntimeError("ALE-Bench package source differs")
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
    return ObservedALEBenchIdentity(
        source_commit=source_commit,
        dataset_revision=dataset_revision,
        task_id=contract.task_id,
        docker_image_digest=docker_digest,
        judge_version=contract.judge_version,
        time_limit_seconds=contract.time_limit_seconds,
        memory_limit_bytes=contract.memory_limit_bytes,
        score_direction=contract.score_direction,
        public_evaluator_command=contract.public_evaluator_command,
        private_evaluator_command=contract.private_evaluator_command,
        task_zip_sha256=task_zip_sha256,
        ale_module_path=ale_module_path.as_posix(),
        direct_url_source=direct_url_source,
    )


__all__ = [
    "ALE_BENCH_DATASET_REVISION",
    "ALE_BENCH_SOURCE_COMMIT",
    "ALEBenchContract",
    "ALEBenchOfficialAdapter",
    "FreezeAuthorization",
    "ObservedALEBenchIdentity",
]
