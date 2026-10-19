from __future__ import annotations

import hashlib
import json
import math
import os
import re
import stat
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from ..adapters.sweperf import (
    DATASET_COMMIT,
    DATASET_PARQUET_SHA256,
    EVALUATOR_COMMIT,
    FROZEN_TASKS,
    PATCH_APPLY_MODE,
    PERFORMANCE_REPETITIONS,
    SWEPERF_EVALUATOR_ID,
)
from ..adapters.sweperf_docker import (
    CANDIDATE_WORKER_UID,
    IMAGE_CONTRACT_LABEL,
    IMAGE_CONTRACT_NAME,
    IMAGE_CONTRACT_SHA256,
    IMAGE_CONTRACT_SHA256_LABEL,
    IMAGE_CONTRACT_VERSION,
    IMAGE_CONTRACT_VERSION_LABEL,
    IMAGE_DATASET_COMMIT_LABEL,
    IMAGE_ENTRYPOINT_LABEL,
    IMAGE_EVALUATOR_COMMIT_LABEL,
    IMAGE_INSTANCE_ID_LABEL,
    IMAGE_PRIVATE_CHANNEL_LABEL,
    IMAGE_RESOURCE_LIMITS_SHA256_LABEL,
    IMAGE_SUPERVISOR_UID_LABEL,
    IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL,
    IMAGE_TASK_MANIFEST_SHA256_LABEL,
    IMAGE_TASK_SHA256_LABEL,
    IMAGE_UPSTREAM_REF_SHA256_LABEL,
    IMAGE_WORKER_CAPABILITIES_LABEL,
    IMAGE_WORKER_UID_LABEL,
    TRUSTED_STAGE_COMMAND,
    WrapperImageIdentity,
)


_IMAGE_REF = re.compile(r"[^\s@]+@sha256:[0-9a-f]{64}\Z")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:+-]{0,159}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
_FORBIDDEN_EXECUTABLES = {
    "bash",
    "busybox",
    "curl",
    "ftp",
    "nc",
    "netcat",
    "scp",
    "sh",
    "socat",
    "ssh",
    "wget",
    "zsh",
}
_URL_MARKERS = ("http://", "https://", "ftp://")
_FROZEN_LIMITS = MappingProxyType(
    {"cpus": 10, "memory_bytes": 32 * 1024**3, "pids": 512}
)
_ASSET_DIRECTORY = Path(__file__).with_name("assets")
_DOCKERFILE_TEMPLATE = _ASSET_DIRECTORY / "Dockerfile.template"
_ENTRYPOINT_ASSET = _ASSET_DIRECTORY / "evaluate-stage"
_SUPERVISOR_SOURCE = Path(__file__).with_name("supervisor.py")
_TRUSTED_RESULT_SOURCE = Path(__file__).with_name("trusted_result.py")


def _require_exact_keys(
    payload: Mapping[str, Any], expected: set[str], label: str
) -> None:
    if not isinstance(payload, Mapping) or set(payload) != expected:
        raise ValueError(f"{label} fields differ")


def _canonical_bytes(value: Mapping[str, Any]) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("ascii")


def _pretty_bytes(value: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=True,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("ascii")


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _safe_repo_path(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value or len(value) > 240:
        raise ValueError(f"invalid {label}")
    if "\\" in value or "\x00" in value or any(ord(ch) < 32 for ch in value):
        raise ValueError(f"invalid {label}")
    path = PurePosixPath(value)
    if (
        path.is_absolute()
        or path.as_posix() != value
        or not path.parts
        or any(part in {"", ".", ".."} or part.lower() == ".git" for part in path.parts)
    ):
        raise ValueError(f"unsafe {label}")
    return value


def _safe_strings(values: Any, label: str) -> tuple[str, ...]:
    if not isinstance(values, list) or not values:
        raise ValueError(f"{label} must be a non-empty array")
    result: list[str] = []
    for value in values:
        if (
            not isinstance(value, str)
            or not value
            or len(value) > 1024
            or "\x00" in value
            or "\n" in value
            or "\r" in value
        ):
            raise ValueError(f"unsafe {label}")
        result.append(value)
    if len(result) != len(set(result)):
        raise ValueError(f"{label} values must be unique")
    return tuple(result)


@dataclass(frozen=True)
class FrozenResourceLimits:
    cpus: int
    memory_bytes: int
    pids: int

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "FrozenResourceLimits":
        _require_exact_keys(payload, set(_FROZEN_LIMITS), "resource limits")
        if dict(payload) != dict(_FROZEN_LIMITS):
            raise ValueError("resource limits differ from the frozen envelope")
        return cls(**dict(_FROZEN_LIMITS))

    def to_dict(self) -> dict[str, int]:
        return {
            "cpus": self.cpus,
            "memory_bytes": self.memory_bytes,
            "pids": self.pids,
        }


@dataclass(frozen=True)
class StageCommand:
    argv: tuple[str, ...]
    timeout_seconds: float
    expected_test_ids: tuple[str, ...]

    @classmethod
    def from_dict(
        cls, payload: Mapping[str, Any], *, label: str
    ) -> "StageCommand":
        _require_exact_keys(
            payload, {"argv", "timeout_seconds", "expected_test_ids"}, label
        )
        argv_value = payload["argv"]
        if not isinstance(argv_value, list) or not argv_value:
            raise ValueError(f"{label} argv must be non-empty")
        argv: list[str] = []
        for value in argv_value:
            if (
                not isinstance(value, str)
                or not value
                or "\x00" in value
                or "\n" in value
                or "\r" in value
            ):
                raise ValueError(f"unsafe {label} argv")
            if any(marker in value.lower() for marker in _URL_MARKERS):
                raise ValueError(f"{label} network access is forbidden")
            unknown_placeholders = re.findall(r"\{[^{}]+\}", value)
            if any(item != "{report_path}" for item in unknown_placeholders):
                raise ValueError(f"{label} uses an unknown placeholder")
            argv.append(value)
        executable = PurePosixPath(argv[0])
        if not executable.is_absolute():
            raise ValueError(f"{label} executable must be absolute")
        if executable.name.lower() in _FORBIDDEN_EXECUTABLES:
            category = (
                "network"
                if executable.name.lower()
                in {"curl", "ftp", "nc", "netcat", "scp", "socat", "ssh", "wget"}
                else "shell"
            )
            raise ValueError(f"{label} {category} executable is forbidden")
        if sum(value.count("{report_path}") for value in argv) != 1:
            raise ValueError(f"{label} must bind exactly one report_path")

        timeout = payload["timeout_seconds"]
        if (
            isinstance(timeout, bool)
            or not isinstance(timeout, (int, float))
            or not math.isfinite(float(timeout))
            or timeout <= 0
            or timeout > 300
        ):
            raise ValueError(f"{label} timeout is outside the frozen bound")
        return cls(
            argv=tuple(argv),
            timeout_seconds=float(timeout),
            expected_test_ids=_safe_strings(
                payload["expected_test_ids"], f"{label} expected test ids"
            ),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "argv": list(self.argv),
            "timeout_seconds": self.timeout_seconds,
            "expected_test_ids": list(self.expected_test_ids),
        }


@dataclass(frozen=True)
class PerformanceCommand:
    command: StageCommand
    warmup_repetitions: int
    measurement_repetitions: int
    score_formula: str

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "PerformanceCommand":
        expected = {
            "argv",
            "timeout_seconds",
            "expected_test_ids",
            "warmup_repetitions",
            "measurement_repetitions",
            "score_formula",
        }
        _require_exact_keys(payload, expected, "performance")
        command = StageCommand.from_dict(
            {key: payload[key] for key in ("argv", "timeout_seconds", "expected_test_ids")},
            label="performance",
        )
        warmups = payload["warmup_repetitions"]
        repetitions = payload["measurement_repetitions"]
        if isinstance(warmups, bool) or not isinstance(warmups, int) or warmups != 3:
            raise ValueError("performance warmup repetition count changed")
        if (
            isinstance(repetitions, bool)
            or not isinstance(repetitions, int)
            or repetitions != PERFORMANCE_REPETITIONS
        ):
            raise ValueError("performance measurement repetition count changed")
        if payload["score_formula"] != "geomean-median-speedup-v1":
            raise ValueError("performance score formula changed")
        return cls(
            command=command,
            warmup_repetitions=warmups,
            measurement_repetitions=repetitions,
            score_formula=payload["score_formula"],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **self.command.to_dict(),
            "warmup_repetitions": self.warmup_repetitions,
            "measurement_repetitions": self.measurement_repetitions,
            "score_formula": self.score_formula,
        }


@dataclass(frozen=True)
class WrapperTaskManifest:
    schema_version: int
    instance_id: str
    repository: str
    base_commit: str
    task_sha256: str
    evaluator: str
    evaluator_commit: str
    dataset_commit: str
    dataset_parquet_sha256: str
    patch_apply_mode: str
    upstream_image_ref: str
    repository_path: str
    allowed_patch_paths: tuple[str, ...]
    correctness: StageCommand
    performance: PerformanceCommand
    worker_uid: int
    resource_limits: FrozenResourceLimits

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "WrapperTaskManifest":
        expected = {
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
        _require_exact_keys(payload, expected, "wrapper task manifest")
        if payload["schema_version"] != 1:
            raise ValueError("wrapper task manifest schema changed")
        instance_id = payload["instance_id"]
        if not isinstance(instance_id, str) or not _SAFE_ID.fullmatch(instance_id):
            raise ValueError("unsafe SWE-Perf instance id")
        try:
            task = FROZEN_TASKS[instance_id]
        except KeyError as exc:
            raise ValueError("task is outside the frozen SWE-Perf set") from exc
        if (
            payload["repository"],
            payload["base_commit"],
            payload["task_sha256"],
        ) != (task.repository, task.base_commit, task.task_sha256):
            raise ValueError("task binding differs from the frozen SWE-Perf set")
        if not _REPOSITORY.fullmatch(payload["repository"]):
            raise ValueError("invalid repository")
        if not _COMMIT.fullmatch(payload["base_commit"]):
            raise ValueError("base commit must be pinned")
        if not _SHA256.fullmatch(payload["task_sha256"]):
            raise ValueError("task hash must be pinned")
        frozen_evaluator = {
            "evaluator": SWEPERF_EVALUATOR_ID,
            "evaluator_commit": EVALUATOR_COMMIT,
            "dataset_commit": DATASET_COMMIT,
            "dataset_parquet_sha256": DATASET_PARQUET_SHA256,
            "patch_apply_mode": PATCH_APPLY_MODE,
        }
        if any(payload[key] != value for key, value in frozen_evaluator.items()):
            raise ValueError("evaluator binding differs from HB-GEN-1")
        if (
            not isinstance(payload["upstream_image_ref"], str)
            or not _IMAGE_REF.fullmatch(payload["upstream_image_ref"])
        ):
            raise ValueError("upstream image must be pinned by digest")
        if payload["repository_path"] != "/testbed":
            raise ValueError("repository path differs from the upstream image contract")
        paths_value = payload["allowed_patch_paths"]
        if not isinstance(paths_value, list) or not paths_value:
            raise ValueError("allowed patch paths must be non-empty")
        paths = tuple(_safe_repo_path(item, "allowed patch path") for item in paths_value)
        if len(paths) != len(set(paths)):
            raise ValueError("allowed patch paths must be unique")
        if payload["worker_uid"] != CANDIDATE_WORKER_UID:
            raise ValueError("worker uid differs from the image contract")
        return cls(
            schema_version=1,
            instance_id=instance_id,
            repository=task.repository,
            base_commit=task.base_commit,
            task_sha256=task.task_sha256,
            evaluator=SWEPERF_EVALUATOR_ID,
            evaluator_commit=EVALUATOR_COMMIT,
            dataset_commit=DATASET_COMMIT,
            dataset_parquet_sha256=DATASET_PARQUET_SHA256,
            patch_apply_mode=PATCH_APPLY_MODE,
            upstream_image_ref=payload["upstream_image_ref"],
            repository_path="/testbed",
            allowed_patch_paths=paths,
            correctness=StageCommand.from_dict(
                payload["correctness"], label="correctness"
            ),
            performance=PerformanceCommand.from_dict(payload["performance"]),
            worker_uid=CANDIDATE_WORKER_UID,
            resource_limits=FrozenResourceLimits.from_dict(payload["resource_limits"]),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "instance_id": self.instance_id,
            "repository": self.repository,
            "base_commit": self.base_commit,
            "task_sha256": self.task_sha256,
            "evaluator": self.evaluator,
            "evaluator_commit": self.evaluator_commit,
            "dataset_commit": self.dataset_commit,
            "dataset_parquet_sha256": self.dataset_parquet_sha256,
            "patch_apply_mode": self.patch_apply_mode,
            "upstream_image_ref": self.upstream_image_ref,
            "repository_path": self.repository_path,
            "allowed_patch_paths": list(self.allowed_patch_paths),
            "correctness": self.correctness.to_dict(),
            "performance": self.performance.to_dict(),
            "worker_uid": self.worker_uid,
            "resource_limits": self.resource_limits.to_dict(),
        }


@dataclass(frozen=True)
class WrapperSourceLock:
    schema_version: int
    evaluator_commit: str
    dataset_commit: str
    dataset_parquet_sha256: str
    tasks: tuple[WrapperTaskManifest, ...]

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "WrapperSourceLock":
        _require_exact_keys(
            payload,
            {
                "schema_version",
                "evaluator_commit",
                "dataset_commit",
                "dataset_parquet_sha256",
                "tasks",
            },
            "wrapper source lock",
        )
        if payload["schema_version"] != 1:
            raise ValueError("wrapper source lock schema changed")
        if (
            payload["evaluator_commit"],
            payload["dataset_commit"],
            payload["dataset_parquet_sha256"],
        ) != (EVALUATOR_COMMIT, DATASET_COMMIT, DATASET_PARQUET_SHA256):
            raise ValueError("wrapper source lock evaluator binding changed")
        values = payload["tasks"]
        if not isinstance(values, list):
            raise ValueError("wrapper source lock tasks must be an array")
        tasks = tuple(WrapperTaskManifest.from_dict(item) for item in values)
        if tuple(item.instance_id for item in tasks) != tuple(FROZEN_TASKS):
            raise ValueError("wrapper source lock must contain the exact frozen SWE-Perf task set")
        return cls(
            schema_version=1,
            evaluator_commit=EVALUATOR_COMMIT,
            dataset_commit=DATASET_COMMIT,
            dataset_parquet_sha256=DATASET_PARQUET_SHA256,
            tasks=tasks,
        )

    @classmethod
    def from_json(cls, path: Path) -> "WrapperSourceLock":
        raw = Path(path).read_bytes()
        if not raw or len(raw) > 8 * 1024 * 1024:
            raise ValueError("wrapper source lock size is outside the bound")
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("wrapper source lock must be UTF-8 JSON") from exc
        if not isinstance(payload, dict):
            raise ValueError("wrapper source lock must be an object")
        return cls.from_dict(payload)


@dataclass(frozen=True)
class PreparedWrapperContext:
    instance_id: str
    context_dir: Path
    task_manifest_sha256: str
    supervisor_bundle_sha256: str
    context_sha256: str
    labels: Mapping[str, str]

    @property
    def wrapper_identity(self) -> WrapperImageIdentity:
        return WrapperImageIdentity(
            instance_id=self.instance_id,
            task_sha256=self.labels[IMAGE_TASK_SHA256_LABEL],
            task_manifest_sha256=self.task_manifest_sha256,
            supervisor_bundle_sha256=self.supervisor_bundle_sha256,
            upstream_ref_sha256=self.labels[IMAGE_UPSTREAM_REF_SHA256_LABEL],
            resource_limits_sha256=self.labels[IMAGE_RESOURCE_LIMITS_SHA256_LABEL],
        )


def _base_labels() -> dict[str, str]:
    return {
        IMAGE_CONTRACT_LABEL: IMAGE_CONTRACT_NAME,
        IMAGE_CONTRACT_VERSION_LABEL: IMAGE_CONTRACT_VERSION,
        IMAGE_CONTRACT_SHA256_LABEL: IMAGE_CONTRACT_SHA256,
        IMAGE_ENTRYPOINT_LABEL: TRUSTED_STAGE_COMMAND,
        IMAGE_SUPERVISOR_UID_LABEL: "0",
        IMAGE_WORKER_UID_LABEL: str(CANDIDATE_WORKER_UID),
        IMAGE_WORKER_CAPABILITIES_LABEL: "none",
        IMAGE_PRIVATE_CHANNEL_LABEL: "root-0700-files-0600-v1",
        IMAGE_EVALUATOR_COMMIT_LABEL: EVALUATOR_COMMIT,
        IMAGE_DATASET_COMMIT_LABEL: DATASET_COMMIT,
    }


def _wrapper_labels(
    task: WrapperTaskManifest,
    *,
    manifest_sha256: str,
    supervisor_bundle_sha256: str,
) -> dict[str, str]:
    limits_sha = _sha256(_canonical_bytes(task.resource_limits.to_dict()))
    return {
        **_base_labels(),
        IMAGE_TASK_MANIFEST_SHA256_LABEL: manifest_sha256,
        IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL: supervisor_bundle_sha256,
        IMAGE_UPSTREAM_REF_SHA256_LABEL: _sha256(
            task.upstream_image_ref.encode("ascii")
        ),
        IMAGE_RESOURCE_LIMITS_SHA256_LABEL: limits_sha,
        IMAGE_INSTANCE_ID_LABEL: task.instance_id,
        IMAGE_TASK_SHA256_LABEL: task.task_sha256,
    }


def _docker_quote(value: str) -> str:
    if "\n" in value or "\r" in value or "\x00" in value:
        raise ValueError("Docker label value contains a control character")
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _render_dockerfile(task: WrapperTaskManifest, labels: Mapping[str, str]) -> bytes:
    template = _DOCKERFILE_TEMPLATE.read_text(encoding="utf-8")
    label_lines = " \\\n      ".join(
        f"{_docker_quote(key)}={_docker_quote(value)}"
        for key, value in sorted(labels.items())
    )
    rendered = template.replace("@@UPSTREAM_IMAGE@@", task.upstream_image_ref).replace(
        "@@LABELS@@", label_lines
    )
    if "@@" in rendered:
        raise ValueError("Dockerfile template contains an unresolved placeholder")
    return rendered.encode("utf-8")


def _write_once(path: Path, content: bytes, *, mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.exists() or path.is_symlink():
        metadata = path.lstat()
        if (
            stat.S_ISLNK(metadata.st_mode)
            or not stat.S_ISREG(metadata.st_mode)
            or path.read_bytes() != content
        ):
            raise ValueError(f"refusing to overwrite different wrapper asset: {path.name}")
        os.chmod(path, mode, follow_symlinks=False)
        return
    descriptor, name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, mode, follow_symlinks=False)
        os.replace(temporary, path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def prepare_wrapper_build_contexts(
    *, source_lock: WrapperSourceLock, output_root: Path
) -> tuple[PreparedWrapperContext, ...]:
    """Prepare eight deterministic contexts without invoking Docker or networking."""

    if not isinstance(source_lock, WrapperSourceLock):
        raise TypeError("source_lock must be a validated WrapperSourceLock")
    output_root = Path(output_root).resolve()
    output_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    if output_root.is_symlink() or not output_root.is_dir():
        raise ValueError("wrapper output root must be a real directory")

    entrypoint = _ENTRYPOINT_ASSET.read_bytes()
    supervisor = _SUPERVISOR_SOURCE.read_bytes()
    trusted_result = _TRUSTED_RESULT_SOURCE.read_bytes()
    supervisor_bundle = _canonical_bytes(
        {
            "evaluate-stage": _sha256(entrypoint),
            "supervisor.py": _sha256(supervisor),
            "trusted_result.py": _sha256(trusted_result),
        }
    )
    supervisor_sha = _sha256(supervisor_bundle)

    prepared: list[PreparedWrapperContext] = []
    for task in source_lock.tasks:
        context_dir = output_root / task.instance_id
        context_dir.mkdir(mode=0o700, exist_ok=True)
        manifest = _pretty_bytes(task.to_dict())
        manifest_sha = _sha256(manifest)
        labels = _wrapper_labels(
            task,
            manifest_sha256=manifest_sha,
            supervisor_bundle_sha256=supervisor_sha,
        )
        files = {
            "Dockerfile": _render_dockerfile(task, labels),
            "evaluate-stage": entrypoint,
            "supervisor.py": supervisor,
            "trusted_result.py": trusted_result,
            "task-manifest.json": manifest,
            "task-manifest.sha256": (manifest_sha + "\n").encode("ascii"),
        }
        for name, content in files.items():
            _write_once(
                context_dir / name,
                content,
                mode=0o555 if name == "evaluate-stage" else 0o444,
            )
        receipt = {
            "schema_version": 1,
            "instance_id": task.instance_id,
            "upstream_image_ref": task.upstream_image_ref,
            "network_mode": "none",
            "pull_policy": "never",
            "task_manifest_sha256": manifest_sha,
            "supervisor_bundle_sha256": supervisor_sha,
            "labels": dict(sorted(labels.items())),
            "file_sha256": {name: _sha256(content) for name, content in sorted(files.items())},
            "build_required": True,
            "wrapper_image_ref": None,
        }
        receipt_bytes = _pretty_bytes(receipt)
        _write_once(context_dir / "build-context.json", receipt_bytes, mode=0o444)
        prepared.append(
            PreparedWrapperContext(
                instance_id=task.instance_id,
                context_dir=context_dir,
                task_manifest_sha256=manifest_sha,
                supervisor_bundle_sha256=supervisor_sha,
                context_sha256=_sha256(_canonical_bytes(receipt)),
                labels=MappingProxyType(dict(labels)),
            )
        )
    return tuple(prepared)
