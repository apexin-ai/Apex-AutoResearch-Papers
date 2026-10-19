"""Production Docker boundary for the HB-GEN-1 SWE-Perf adapter.

This module owns container lifecycle and the private result channel only.  The
digest-pinned image owns the frozen SWE-Perf stage supervisor.  Isolation is
considered present only after ``docker image inspect`` proves the frozen image
contract; a missing/unlabelled wrapper fails closed.  For a verified wrapper,
candidate output is discarded by Docker's ``none`` log driver and is never
parsed as control data.  The outer :class:`~.sweperf.SWEPerfAdapter` accepts only
the root-owned, nonce-bound result copied out of the private Docker volume after
the candidate process has stopped.

No image pull is performed here.  A missing pinned image is an environment
failure, never permission to resolve a mutable tag or fetch a replacement.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import shutil
import stat
import subprocess
import threading
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Mapping, Protocol, Sequence

from .sweperf import (
    DATASET_COMMIT,
    DATASET_PARQUET_SHA256,
    EVALUATOR_COMMIT,
    FROZEN_TASKS,
    MAX_PATCH_BYTES,
    PATCH_APPLY_MODE,
    PRIVATE_RESULT_SCHEMA_VERSION,
    SWEPERF_EVALUATOR_ID,
    AttemptBinding,
    DockerWorkspace,
    EvaluationStage,
    StageRequest,
    StageRun,
    parse_correctness_result,
    parse_performance_result,
    validate_unified_diff,
)


TRUSTED_STAGE_COMMAND = "/opt/hb-sweperf/bin/evaluate-stage"
CONTAINER_REQUEST_PATH = "/run/hb-private/request.json"
CONTAINER_WORK_PATH = "/hb/work"
CONTAINER_CACHE_PATH = "/hb/cache"
CANDIDATE_WORKER_UID = 65534
IMAGE_CONTRACT_NAME = "apex-moss.hb-gen1.sweperf-supervisor"
IMAGE_CONTRACT_VERSION = "1"
IMAGE_CONTRACT_LABEL = "org.apex-moss.hb-gen1.sweperf.contract"
IMAGE_CONTRACT_VERSION_LABEL = "org.apex-moss.hb-gen1.sweperf.contract-version"
IMAGE_CONTRACT_SHA256_LABEL = "org.apex-moss.hb-gen1.sweperf.contract-sha256"
IMAGE_ENTRYPOINT_LABEL = "org.apex-moss.hb-gen1.sweperf.entrypoint"
IMAGE_SUPERVISOR_UID_LABEL = "org.apex-moss.hb-gen1.sweperf.supervisor-uid"
IMAGE_WORKER_UID_LABEL = "org.apex-moss.hb-gen1.sweperf.worker-uid"
IMAGE_WORKER_CAPABILITIES_LABEL = (
    "org.apex-moss.hb-gen1.sweperf.worker-capabilities"
)
IMAGE_PRIVATE_CHANNEL_LABEL = "org.apex-moss.hb-gen1.sweperf.private-channel"
IMAGE_EVALUATOR_COMMIT_LABEL = "org.apex-moss.hb-gen1.sweperf.evaluator-commit"
IMAGE_DATASET_COMMIT_LABEL = "org.apex-moss.hb-gen1.sweperf.dataset-commit"
IMAGE_TASK_MANIFEST_SHA256_LABEL = (
    "org.apex-moss.hb-gen1.sweperf.task-manifest-sha256"
)
IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL = (
    "org.apex-moss.hb-gen1.sweperf.supervisor-bundle-sha256"
)
IMAGE_UPSTREAM_REF_SHA256_LABEL = (
    "org.apex-moss.hb-gen1.sweperf.upstream-ref-sha256"
)
IMAGE_RESOURCE_LIMITS_SHA256_LABEL = (
    "org.apex-moss.hb-gen1.sweperf.resource-limits-sha256"
)
IMAGE_INSTANCE_ID_LABEL = "org.apex-moss.hb-gen1.sweperf.instance-id"
IMAGE_TASK_SHA256_LABEL = "org.apex-moss.hb-gen1.sweperf.task-sha256"
_IMAGE_CONTRACT_CORE = {
    "contract": IMAGE_CONTRACT_NAME,
    "version": IMAGE_CONTRACT_VERSION,
    "entrypoint": TRUSTED_STAGE_COMMAND,
    "supervisor_uid": "0",
    "worker_uid": str(CANDIDATE_WORKER_UID),
    "worker_capabilities": "none",
    "private_channel": "root-0700-files-0600-v1",
    "evaluator_commit": EVALUATOR_COMMIT,
    "dataset_commit": DATASET_COMMIT,
}
IMAGE_CONTRACT_SHA256 = hashlib.sha256(
    json.dumps(
        _IMAGE_CONTRACT_CORE,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("ascii")
).hexdigest()
_EXPECTED_IMAGE_LABELS = {
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
_IMAGE_INSPECT_FORMAT = (
    '{"id":{{json .Id}},"repo_digests":{{json .RepoDigests}},'
    '"entrypoint":{{json .Config.Entrypoint}},"labels":{{json .Config.Labels}}}'
)
_MAX_DOCKER_OUTPUT_BYTES = 64 * 1024
_MAX_PRIVATE_RESULT_BYTES = 1024 * 1024
_IMAGE_REF = re.compile(r"[^\s@]+@sha256:[0-9a-f]{64}\Z")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:+-]{0,159}\Z")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_CONTAINER_ID = re.compile(rb"[0-9a-f]{12,64}\n?\Z")
_EXIT_CODE = re.compile(rb"(?:0|[1-9][0-9]{0,2})\n?\Z")


class DockerCLIError(RuntimeError):
    """The trusted Docker control plane violated its frozen contract."""


class ImageContractNotVerifiedError(DockerCLIError):
    """The local digest-pinned image lacks the frozen supervisor contract."""


@dataclass(frozen=True)
class WrapperImageIdentity:
    """Content identity generated with the offline wrapper build context."""

    instance_id: str
    task_sha256: str
    task_manifest_sha256: str
    supervisor_bundle_sha256: str
    upstream_ref_sha256: str
    resource_limits_sha256: str

    def __post_init__(self) -> None:
        if not _SAFE_ID.fullmatch(self.instance_id):
            raise ValueError("unsafe wrapper image instance id")
        for field_name in (
            "task_sha256",
            "task_manifest_sha256",
            "supervisor_bundle_sha256",
            "upstream_ref_sha256",
            "resource_limits_sha256",
        ):
            if not _SHA256.fullmatch(getattr(self, field_name)):
                raise ValueError(f"invalid wrapper image identity: {field_name}")

    def labels(self) -> dict[str, str]:
        return {
            IMAGE_TASK_MANIFEST_SHA256_LABEL: self.task_manifest_sha256,
            IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL: self.supervisor_bundle_sha256,
            IMAGE_UPSTREAM_REF_SHA256_LABEL: self.upstream_ref_sha256,
            IMAGE_RESOURCE_LIMITS_SHA256_LABEL: self.resource_limits_sha256,
            IMAGE_INSTANCE_ID_LABEL: self.instance_id,
            IMAGE_TASK_SHA256_LABEL: self.task_sha256,
        }


@dataclass(frozen=True)
class DockerCommandResult:
    returncode: int
    stdout: bytes = b""
    stderr: bytes = b""

    def __post_init__(self) -> None:
        if isinstance(self.returncode, bool) or not isinstance(self.returncode, int):
            raise ValueError("Docker returncode must be an integer")
        if not isinstance(self.stdout, bytes) or not isinstance(self.stderr, bytes):
            raise ValueError("Docker command output must be bytes")
        if len(self.stdout) > _MAX_DOCKER_OUTPUT_BYTES or len(
            self.stderr
        ) > _MAX_DOCKER_OUTPUT_BYTES:
            raise ValueError("Docker command output exceeds the control-plane bound")


class DockerCommandRunner(Protocol):
    def run(
        self, argv: Sequence[str], *, timeout_seconds: float
    ) -> DockerCommandResult: ...


class SubprocessDockerRunner:
    """Small no-shell Docker CLI transport used by the production executor."""

    _ENV_ALLOWLIST = (
        "PATH",
        "DOCKER_HOST",
        "DOCKER_CONTEXT",
        "DOCKER_TLS_VERIFY",
        "DOCKER_CERT_PATH",
        "XDG_RUNTIME_DIR",
    )

    def __init__(self, *, environment: Mapping[str, str] | None = None):
        source = os.environ if environment is None else environment
        self._environment = {
            key: source[key]
            for key in self._ENV_ALLOWLIST
            if key in source and isinstance(source[key], str)
        }

    def run(
        self, argv: Sequence[str], *, timeout_seconds: float
    ) -> DockerCommandResult:
        if not argv or any(
            not isinstance(item, str) or not item or "\x00" in item for item in argv
        ):
            raise ValueError("Docker argv must be non-empty safe strings")
        if not math.isfinite(timeout_seconds) or timeout_seconds <= 0:
            raise ValueError("Docker command timeout must be finite and positive")
        completed = subprocess.run(
            list(argv),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=timeout_seconds,
            env=self._environment,
        )
        return DockerCommandResult(
            returncode=completed.returncode,
            stdout=completed.stdout[:_MAX_DOCKER_OUTPUT_BYTES],
            stderr=completed.stderr[:_MAX_DOCKER_OUTPUT_BYTES],
        )


@dataclass(frozen=True)
class SecurityLimits:
    # SWE-Perf's upstream evaluator documents five CPU nodes per worker.  The
    # HB-GEN-1 wrapper freezes a larger, non-transferable per-container envelope
    # so the paired reference/candidate subprocesses cannot be starved by a
    # host-specific default.  These are Docker safety caps, not a scheduler
    # entitlement and not permission to borrow another experiment cell's time.
    pids: int = 512
    cpus: float = 10.0
    memory_bytes: int = 32 * 1024**3
    tmpfs_bytes: int = 512 * 1024**2
    correctness_timeout_seconds: float = 300.0
    performance_timeout_seconds: float = 3300.0
    docker_control_timeout_seconds: float = 60.0
    cleanup_timeout_seconds: float = 30.0

    def __post_init__(self) -> None:
        for label, value in (
            ("pids", self.pids),
            ("memory_bytes", self.memory_bytes),
            ("tmpfs_bytes", self.tmpfs_bytes),
        ):
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"{label} must be a positive integer")
        for label, value in (
            ("cpus", self.cpus),
            ("correctness_timeout_seconds", self.correctness_timeout_seconds),
            ("performance_timeout_seconds", self.performance_timeout_seconds),
            ("docker_control_timeout_seconds", self.docker_control_timeout_seconds),
            ("cleanup_timeout_seconds", self.cleanup_timeout_seconds),
        ):
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(float(value))
                or value <= 0
            ):
                raise ValueError(f"{label} must be finite and positive")
        if (self.pids, float(self.cpus), self.memory_bytes) != (
            512,
            10.0,
            32 * 1024**3,
        ):
            raise ValueError(
                "SWE-Perf CPU/memory/PID resource envelope is frozen"
            )
        if self.pids > 4096:
            raise ValueError("pids limit is unexpectedly broad")
        if self.cpus > 64:
            raise ValueError("CPU limit is unexpectedly broad")
        if self.memory_bytes > 256 * 1024**3:
            raise ValueError("memory limit is unexpectedly broad")


@dataclass
class _WorkspaceState:
    workspace: DockerWorkspace
    binding: AttemptBinding
    root: Path
    scratch: Path
    cache: Path
    private: Path
    private_volume: str
    container_name: str
    container_id: str
    candidate_copied: bool = False
    current_request: StageRequest | None = None
    run_result: StageRun | None = None
    private_results: dict[EvaluationStage, bytes] = field(default_factory=dict)
    correctness_receipt: str | None = None
    destroyed: bool = False


def _format_cpu(value: float) -> str:
    return format(float(value), ".12g")


def _safe_mount_source(path: Path, label: str) -> str:
    value = str(path)
    if not path.is_absolute() or any(
        character in value for character in (",", "\n", "\r", "\x00")
    ):
        raise ValueError(f"{label} cannot be represented as a Docker bind source")
    return value


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _atomic_owner_only_write(path: Path, payload: bytes) -> None:
    if not isinstance(payload, bytes):
        raise TypeError("atomic payload must be bytes")
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    flags |= getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(temporary, flags, 0o600)
    try:
        with os.fdopen(descriptor, "wb", closefd=True) as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, 0o600, follow_symlinks=False)
        os.replace(temporary, path)
        _fsync_directory(path.parent)
    except Exception:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass
        raise


class ProductionSWEPerfDockerExecutor:
    """Capability-minimal implementation of :class:`sweperf.DockerExecutor`.

    One stopped/restartable container is created for each attempt.  Correctness
    and performance restart that same attempt container against the same isolated
    work/cache directories.  The performance restart is impossible until the
    owner-only correctness result has been read and its receipt validated.
    """

    def __init__(
        self,
        *,
        workspace_root: Path,
        image_ref: str,
        wrapper_identity: WrapperImageIdentity,
        seccomp_profile: Path,
        runner: DockerCommandRunner | None = None,
        limits: SecurityLimits | None = None,
        docker_binary: str = "docker",
    ):
        if not isinstance(image_ref, str) or not _IMAGE_REF.fullmatch(image_ref):
            raise ValueError("SWE-Perf image must be pinned by sha256 digest")
        if not isinstance(wrapper_identity, WrapperImageIdentity):
            raise ValueError("SWE-Perf wrapper image identity must be frozen")
        if (
            not isinstance(docker_binary, str)
            or not docker_binary
            or any(character.isspace() for character in docker_binary)
            or "\x00" in docker_binary
        ):
            raise ValueError("Docker binary must be one safe argv element")
        self.workspace_root = Path(workspace_root).resolve()
        _safe_mount_source(self.workspace_root, "workspace root")
        self.workspace_root.mkdir(parents=True, exist_ok=True, mode=0o700)
        metadata = self.workspace_root.lstat()
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
            raise ValueError("workspace root must be a real directory")
        os.chmod(self.workspace_root, 0o700)

        profile = Path(seccomp_profile)
        try:
            profile_metadata = profile.lstat()
        except OSError as exc:
            raise ValueError("seccomp profile is missing") from exc
        if stat.S_ISLNK(profile_metadata.st_mode) or not stat.S_ISREG(
            profile_metadata.st_mode
        ):
            raise ValueError("seccomp profile must be a regular non-symlink file")
        self.seccomp_profile = profile.resolve(strict=True)
        _safe_mount_source(self.seccomp_profile, "seccomp profile")
        self._seccomp_sha256 = hashlib.sha256(
            self.seccomp_profile.read_bytes()
        ).hexdigest()
        self.image_ref = image_ref
        self.wrapper_identity = wrapper_identity
        self.limits = limits or SecurityLimits()
        self.docker_binary = docker_binary
        self.runner = runner or SubprocessDockerRunner()
        self._lock = threading.RLock()
        self._states: dict[str, _WorkspaceState] = {}
        self._attempt_ids: set[str] = set()

    def _run(self, argv: Sequence[str], *, timeout: float) -> DockerCommandResult:
        result = self.runner.run(argv, timeout_seconds=timeout)
        if not isinstance(result, DockerCommandResult):
            raise DockerCLIError("Docker runner returned an invalid result")
        return result

    def _validate_binding(self, binding: AttemptBinding) -> None:
        if not isinstance(binding, AttemptBinding):
            raise TypeError("binding must be AttemptBinding")
        frozen = FROZEN_TASKS.get(binding.instance_id)
        if frozen is None or (
            binding.repository,
            binding.base_commit,
            binding.task_sha256,
        ) != (frozen.repository, frozen.base_commit, frozen.task_sha256):
            raise ValueError("attempt differs from the frozen SWE-Perf task")
        if (
            binding.instance_id != self.wrapper_identity.instance_id
            or binding.task_sha256 != self.wrapper_identity.task_sha256
        ):
            raise ValueError("attempt differs from the wrapper image identity")
        expected = {
            "evaluator": SWEPERF_EVALUATOR_ID,
            "evaluator_commit": EVALUATOR_COMMIT,
            "dataset_commit": DATASET_COMMIT,
            "dataset_parquet_sha256": DATASET_PARQUET_SHA256,
            "image_ref": self.image_ref,
            "patch_apply_mode": PATCH_APPLY_MODE,
        }
        for field_name, expected_value in expected.items():
            if getattr(binding, field_name) != expected_value:
                raise ValueError(f"attempt binding mismatch: {field_name}")
        if not _SAFE_ID.fullmatch(binding.attempt_id):
            raise ValueError("unsafe attempt id")
        if not _SHA256.fullmatch(binding.patch_sha256):
            raise ValueError("invalid patch hash")

    def _verify_image_contract(self) -> None:
        try:
            inspected = self._run(
                [
                    self.docker_binary,
                    "image",
                    "inspect",
                    "--format",
                    _IMAGE_INSPECT_FORMAT,
                    self.image_ref,
                ],
                timeout=self.limits.docker_control_timeout_seconds,
            )
            if inspected.returncode != 0:
                raise ValueError("pinned wrapper image is unavailable")
            payload = json.loads(inspected.stdout.decode("utf-8"))
            if not isinstance(payload, dict) or set(payload) != {
                "id",
                "repo_digests",
                "entrypoint",
                "labels",
            }:
                raise ValueError("image inspect schema differs")
            image_id = payload["id"]
            if (
                not isinstance(image_id, str)
                or not re.fullmatch(r"sha256:[0-9a-f]{64}", image_id)
            ):
                raise ValueError("image id is not content-addressed")
            repo_digests = payload["repo_digests"]
            if (
                not isinstance(repo_digests, list)
                or not all(isinstance(item, str) for item in repo_digests)
                or self.image_ref not in repo_digests
            ):
                raise ValueError("requested manifest digest is not installed")
            if payload["entrypoint"] != [TRUSTED_STAGE_COMMAND]:
                raise ValueError("image entrypoint differs from the frozen supervisor")
            labels = payload["labels"]
            if not isinstance(labels, dict):
                raise ValueError("image labels are unavailable")
            expected_labels = {
                **_EXPECTED_IMAGE_LABELS,
                **self.wrapper_identity.labels(),
            }
            for label, expected in expected_labels.items():
                if labels.get(label) != expected:
                    raise ValueError(f"image label differs: {label}")
        except ImageContractNotVerifiedError:
            raise
        except Exception as exc:
            raise ImageContractNotVerifiedError(
                "SWE-Perf image-contract not verified"
            ) from exc

    def _state(self, workspace: DockerWorkspace) -> _WorkspaceState:
        if not isinstance(workspace, DockerWorkspace):
            raise TypeError("workspace must be DockerWorkspace")
        with self._lock:
            state = self._states.get(workspace.workspace_id)
            if (
                state is None
                or state.workspace != workspace
                or state.destroyed
                or workspace.attempt_id != state.binding.attempt_id
            ):
                raise RuntimeError("unknown or destroyed SWE-Perf workspace")
            return state

    def _check_seccomp_snapshot(self) -> None:
        try:
            current = self.seccomp_profile.lstat()
            digest = hashlib.sha256(self.seccomp_profile.read_bytes()).hexdigest()
        except OSError as exc:
            raise RuntimeError("seccomp profile became unavailable") from exc
        if (
            stat.S_ISLNK(current.st_mode)
            or not stat.S_ISREG(current.st_mode)
            or digest != self._seccomp_sha256
        ):
            raise RuntimeError("seccomp profile changed after executor construction")

    def _container_command(
        self,
        *,
        state_root: Path,
        scratch: Path,
        cache: Path,
        private_volume: str,
        container_name: str,
    ) -> list[str]:
        del state_root  # Kept explicit to emphasize all mounts are attempt-local.
        tmpfs = f"rw,noexec,nosuid,nodev,size={self.limits.tmpfs_bytes}"
        return [
            self.docker_binary,
            "create",
            "--name",
            container_name,
            "--pull=never",
            "--network=none",
            "--read-only",
            "--cap-drop=ALL",
            "--cap-add=SETUID",
            "--cap-add=SETGID",
            "--security-opt=no-new-privileges=true",
            f"--security-opt=seccomp={self.seccomp_profile}",
            f"--pids-limit={self.limits.pids}",
            f"--cpus={_format_cpu(self.limits.cpus)}",
            f"--memory={self.limits.memory_bytes}",
            f"--memory-swap={self.limits.memory_bytes}",
            "--ulimit=nofile=1024:1024",
            "--log-driver=none",
            "--stop-timeout=5",
            "--ipc=none",
            "--user=0:0",
            f"--tmpfs=/tmp:{tmpfs}",
            f"--tmpfs=/var/tmp:{tmpfs}",
            (
                "--mount=type=bind,src="
                f"{_safe_mount_source(scratch, 'scratch')},"
                f"dst={CONTAINER_WORK_PATH},rw,bind-propagation=rprivate"
            ),
            (
                "--mount=type=bind,src="
                f"{_safe_mount_source(cache, 'cache')},"
                f"dst={CONTAINER_CACHE_PATH},rw,bind-propagation=rprivate"
            ),
            (
                "--mount=type=volume,src="
                f"{private_volume},dst=/run/hb-private,volume-nocopy"
            ),
            f"--workdir={CONTAINER_WORK_PATH}",
            "--entrypoint",
            TRUSTED_STAGE_COMMAND,
            self.image_ref,
        ]

    def create_workspace(self, binding: AttemptBinding) -> DockerWorkspace:
        self._validate_binding(binding)
        self._check_seccomp_snapshot()
        self._verify_image_contract()
        with self._lock:
            if binding.attempt_id in self._attempt_ids:
                raise RuntimeError("attempt id was already assigned a workspace")
            self._attempt_ids.add(binding.attempt_id)
            while True:
                workspace_id = f"swe-{uuid.uuid4().hex}"
                root = self.workspace_root / workspace_id
                if not root.exists():
                    break
            root.mkdir(mode=0o700)
            scratch = root / "scratch"
            cache = root / "cache"
            private = root / "private"
            for path in (scratch, cache, private):
                path.mkdir(mode=0o700)
            # Scratch/cache are candidate-controlled but hidden below the
            # controller-owned 0700 attempt root.  They must be accessible to
            # the fixed uid-65534 worker after the root supervisor drops uid.
            os.chmod(scratch, 0o777)
            os.chmod(cache, 0o777)
            os.chmod(private, 0o700)
            os.chmod(root, 0o700)
            container_name = f"hb-sweperf-{workspace_id}"
            private_volume = f"hb-sweperf-private-{workspace_id}"

        try:
            volume = self._run(
                [
                    self.docker_binary,
                    "volume",
                    "create",
                    "--label=org.apex-moss.hb-gen1.private=true",
                    private_volume,
                ],
                timeout=self.limits.docker_control_timeout_seconds,
            )
            if volume.returncode != 0 or volume.stdout.strip().decode(
                "utf-8", errors="strict"
            ) != private_volume:
                raise DockerCLIError("Docker did not create the private result volume")
            command = self._container_command(
                state_root=root,
                scratch=scratch,
                cache=cache,
                private_volume=private_volume,
                container_name=container_name,
            )
            created = self._run(
                command, timeout=self.limits.docker_control_timeout_seconds
            )
            if created.returncode != 0 or not _CONTAINER_ID.fullmatch(created.stdout):
                raise DockerCLIError("Docker did not create the pinned attempt container")
            container_id = created.stdout.strip().decode("ascii")
        except Exception:
            try:
                self._run(
                    [
                        self.docker_binary,
                        "rm",
                        "--force",
                        "--volumes",
                        container_name,
                    ],
                    timeout=self.limits.cleanup_timeout_seconds,
                )
            except Exception:
                pass
            try:
                self._run(
                    [self.docker_binary, "volume", "rm", "--force", private_volume],
                    timeout=self.limits.cleanup_timeout_seconds,
                )
            except Exception:
                pass
            shutil.rmtree(root, ignore_errors=True)
            with self._lock:
                self._attempt_ids.discard(binding.attempt_id)
            raise

        workspace = DockerWorkspace(
            workspace_id=workspace_id,
            attempt_id=binding.attempt_id,
            fresh=True,
        )
        state = _WorkspaceState(
            workspace=workspace,
            binding=binding,
            root=root,
            scratch=scratch,
            cache=cache,
            private=private,
            private_volume=private_volume,
            container_name=container_name,
            container_id=container_id,
        )
        with self._lock:
            self._states[workspace_id] = state
        return workspace

    def copy_candidate(self, workspace: DockerWorkspace, patch: bytes) -> None:
        state = self._state(workspace)
        if not isinstance(patch, bytes):
            raise TypeError("candidate patch must be bytes")
        if len(patch) > MAX_PATCH_BYTES:
            raise ValueError("candidate patch exceeds the frozen bound")
        summary = validate_unified_diff(patch)
        if summary.sha256 != state.binding.patch_sha256:
            raise ValueError("candidate patch hash differs from the attempt binding")
        with self._lock:
            if state.candidate_copied:
                raise RuntimeError("candidate patch was already copied")
            candidate = state.scratch / "candidate.patch"
            _atomic_owner_only_write(candidate, patch)
            os.chmod(candidate, 0o444, follow_symlinks=False)
            state.candidate_copied = True

    @staticmethod
    def _request_payload(request: StageRequest) -> bytes:
        payload = {
            "schema_version": PRIVATE_RESULT_SCHEMA_VERSION,
            "binding": asdict(request.binding),
            "stage": request.stage.value,
            "result_nonce": request.result_nonce,
            "correctness_receipt": request.correctness_receipt,
            "candidate_path": f"{CONTAINER_WORK_PATH}/candidate.patch",
            "scratch_path": CONTAINER_WORK_PATH,
            "cache_path": CONTAINER_CACHE_PATH,
        }
        return json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        ).encode("ascii")

    def _validate_stage_request(
        self, state: _WorkspaceState, request: StageRequest
    ) -> None:
        if not isinstance(request, StageRequest) or request.binding != state.binding:
            raise ValueError("stage request is not bound to this workspace")
        if not _SHA256.fullmatch(request.result_nonce):
            raise ValueError("result nonce must be 64 lowercase hex characters")
        if not state.candidate_copied:
            raise RuntimeError("candidate must be copied before evaluator execution")
        if state.current_request is not None:
            raise RuntimeError("the current evaluator stage has already run")
        if request.stage is EvaluationStage.CORRECTNESS:
            if request.correctness_receipt is not None or state.correctness_receipt:
                raise RuntimeError("correctness may run only once and without a receipt")
        elif request.stage is EvaluationStage.PERFORMANCE:
            if state.correctness_receipt is None:
                raise RuntimeError("performance requires a read passing correctness result")
            if request.correctness_receipt != state.correctness_receipt:
                raise RuntimeError("performance correctness receipt differs")
        else:
            raise ValueError("contract is not a runnable Docker stage")
        if request.stage in state.private_results:
            raise RuntimeError("evaluator stage may run only once")

    def _finish_timed_out_stage(
        self, state: _WorkspaceState, request: StageRequest, elapsed: float
    ) -> StageRun:
        try:
            self._run(
                [self.docker_binary, "kill", state.container_name],
                timeout=self.limits.cleanup_timeout_seconds,
            )
        except Exception:
            pass
        result = StageRun(
            returncode=124,
            elapsed_seconds=elapsed,
            timed_out=True,
            stdout="",
            stderr="",
        )
        with self._lock:
            state.current_request = request
            state.run_result = result
        return result

    def run_stage(
        self, workspace: DockerWorkspace, request: StageRequest
    ) -> StageRun:
        state = self._state(workspace)
        with self._lock:
            self._validate_stage_request(state, request)
            result_path = state.private / f"result-{request.result_nonce}.json"
            if result_path.exists() or result_path.is_symlink():
                raise RuntimeError("nonce result path already exists")
            _atomic_owner_only_write(
                state.private / "request.json", self._request_payload(request)
            )
            # Reserve the one-shot stage before the first Docker side effect so
            # concurrent/reentrant callers cannot restart the same container.
            state.current_request = request
            state.run_result = None

        copied = self._run(
            [
                self.docker_binary,
                "cp",
                str(state.private / "request.json"),
                f"{state.container_name}:{CONTAINER_REQUEST_PATH}",
            ],
            timeout=self.limits.docker_control_timeout_seconds,
        )
        if copied.returncode != 0:
            raise DockerCLIError(
                "SWE-Perf image-contract request channel was not writable"
            )

        started_at = time.monotonic()
        start_result = self._run(
            [self.docker_binary, "start", state.container_name],
            timeout=self.limits.docker_control_timeout_seconds,
        )
        if start_result.returncode != 0:
            result = StageRun(
                returncode=start_result.returncode,
                elapsed_seconds=time.monotonic() - started_at,
                stdout="",
                stderr="",
            )
        else:
            stage_timeout = (
                self.limits.correctness_timeout_seconds
                if request.stage is EvaluationStage.CORRECTNESS
                else self.limits.performance_timeout_seconds
            )
            try:
                waited = self._run(
                    [self.docker_binary, "wait", state.container_name],
                    timeout=stage_timeout,
                )
            except subprocess.TimeoutExpired:
                return self._finish_timed_out_stage(
                    state, request, time.monotonic() - started_at
                )
            if waited.returncode != 0 or not _EXIT_CODE.fullmatch(waited.stdout):
                raise DockerCLIError("Docker wait did not return one trusted exit code")
            exit_code = int(waited.stdout.strip())
            if exit_code > 255:
                raise DockerCLIError("container exit code is outside the process range")
            result = StageRun(
                returncode=exit_code,
                elapsed_seconds=time.monotonic() - started_at,
                stdout="",
                stderr="",
            )
        with self._lock:
            state.current_request = request
            state.run_result = result
        return result

    @staticmethod
    def _read_owner_only_file(path: Path) -> bytes:
        try:
            metadata = path.lstat()
        except OSError as exc:
            raise RuntimeError("private result is not available") from exc
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise RuntimeError("private result must be a regular non-symlink file")
        if metadata.st_uid != os.getuid() or stat.S_IMODE(metadata.st_mode) != 0o600:
            raise RuntimeError("private result permissions are not owner-only")
        if metadata.st_size <= 0 or metadata.st_size > _MAX_PRIVATE_RESULT_BYTES:
            raise RuntimeError("private result size is outside the frozen bound")
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            opened = os.fstat(stream.fileno())
            if (
                not stat.S_ISREG(opened.st_mode)
                or opened.st_uid != os.getuid()
                or stat.S_IMODE(opened.st_mode) != 0o600
            ):
                raise RuntimeError("private result changed while opening")
            raw = stream.read(_MAX_PRIVATE_RESULT_BYTES + 1)
        if len(raw) > _MAX_PRIVATE_RESULT_BYTES:
            raise RuntimeError("private result exceeds the frozen bound")
        return raw

    def read_private_result(
        self, workspace: DockerWorkspace, request: StageRequest
    ) -> bytes:
        state = self._state(workspace)
        with self._lock:
            if request.stage in state.private_results:
                return state.private_results[request.stage]
            if state.current_request != request or state.run_result is None:
                raise RuntimeError("private result was not produced by this stage")
            if state.run_result.timed_out:
                raise RuntimeError("private result is not available after timeout")
        path = state.private / f"result-{request.result_nonce}.json"
        if path.exists() or path.is_symlink():
            raise RuntimeError("private result staging path already exists")
        copied = self._run(
            [
                self.docker_binary,
                "cp",
                (
                    f"{state.container_name}:/run/hb-private/"
                    f"result-{request.result_nonce}.json"
                ),
                str(path),
            ],
            timeout=self.limits.docker_control_timeout_seconds,
        )
        if copied.returncode != 0:
            raise RuntimeError("private result is not available")
        raw = self._read_owner_only_file(path)
        if request.stage is EvaluationStage.CORRECTNESS:
            parsed = parse_correctness_result(raw, request)
            receipt = (
                parsed.correctness_receipt if parsed.status == "passed" else None
            )
        else:
            parse_performance_result(raw, request)
            receipt = state.correctness_receipt
        with self._lock:
            state.private_results[request.stage] = raw
            if request.stage is EvaluationStage.CORRECTNESS:
                state.correctness_receipt = receipt
            state.current_request = None
            state.run_result = None
        return raw

    def destroy_workspace(self, workspace: DockerWorkspace) -> None:
        state = self._state(workspace)
        docker_failure: Exception | None = None
        try:
            removed = self._run(
                [
                    self.docker_binary,
                    "rm",
                    "--force",
                    "--volumes",
                    state.container_name,
                ],
                timeout=self.limits.cleanup_timeout_seconds,
            )
            if removed.returncode != 0:
                docker_failure = DockerCLIError("Docker did not remove the attempt container")
        except Exception as exc:
            docker_failure = exc
        try:
            removed_volume = self._run(
                [
                    self.docker_binary,
                    "volume",
                    "rm",
                    "--force",
                    state.private_volume,
                ],
                timeout=self.limits.cleanup_timeout_seconds,
            )
            if removed_volume.returncode != 0 and docker_failure is None:
                docker_failure = DockerCLIError(
                    "Docker did not remove the private result volume"
                )
        except Exception as exc:
            if docker_failure is None:
                docker_failure = exc

        local_failure: Exception | None = None
        try:
            resolved = state.root.resolve(strict=False)
            if resolved.parent != self.workspace_root or resolved.name != workspace.workspace_id:
                raise RuntimeError("refusing to remove an unexpected workspace path")
            shutil.rmtree(resolved)
        except Exception as exc:
            local_failure = exc
        with self._lock:
            state.destroyed = True
            self._states.pop(workspace.workspace_id, None)

        if docker_failure is not None:
            raise RuntimeError("SWE-Perf container cleanup failed") from docker_failure
        if local_failure is not None:
            raise RuntimeError("SWE-Perf local workspace cleanup failed") from local_failure


SWEPerfDockerExecutor = ProductionSWEPerfDockerExecutor


__all__ = [
    "CANDIDATE_WORKER_UID",
    "CONTAINER_CACHE_PATH",
    "CONTAINER_REQUEST_PATH",
    "CONTAINER_WORK_PATH",
    "DockerCLIError",
    "DockerCommandResult",
    "DockerCommandRunner",
    "IMAGE_CONTRACT_LABEL",
    "IMAGE_CONTRACT_NAME",
    "IMAGE_CONTRACT_SHA256",
    "IMAGE_CONTRACT_SHA256_LABEL",
    "IMAGE_CONTRACT_VERSION",
    "IMAGE_CONTRACT_VERSION_LABEL",
    "IMAGE_DATASET_COMMIT_LABEL",
    "IMAGE_ENTRYPOINT_LABEL",
    "IMAGE_EVALUATOR_COMMIT_LABEL",
    "IMAGE_PRIVATE_CHANNEL_LABEL",
    "IMAGE_SUPERVISOR_UID_LABEL",
    "IMAGE_WORKER_CAPABILITIES_LABEL",
    "IMAGE_WORKER_UID_LABEL",
    "IMAGE_INSTANCE_ID_LABEL",
    "IMAGE_RESOURCE_LIMITS_SHA256_LABEL",
    "IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL",
    "IMAGE_TASK_MANIFEST_SHA256_LABEL",
    "IMAGE_TASK_SHA256_LABEL",
    "IMAGE_UPSTREAM_REF_SHA256_LABEL",
    "ImageContractNotVerifiedError",
    "ProductionSWEPerfDockerExecutor",
    "SWEPerfDockerExecutor",
    "SecurityLimits",
    "SubprocessDockerRunner",
    "TRUSTED_STAGE_COMMAND",
    "WrapperImageIdentity",
]
