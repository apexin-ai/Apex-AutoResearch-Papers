"""Fail-closed namespace and runtime bundle for KernelBench meta-train.

The already-tested KernelBenchX namespace implementation supplies the common
mount, header-snapshot and process-quiescence machinery.  This module deliberately
exports the boundary prefix plus a builder for the restricted trusted worker.
The worker returns evidence only over one inherited pipe descriptor; candidate
stdout, writable paths and cache contents never become a result channel.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from .kernelbenchx_isolation import (
    BubblewrapCommand,
    BubblewrapSpec,
    SandboxContractError,
    build_bubblewrap_command,
)


_RUNTIME_FILES = (
    "optimization_lab/harness_builder/adapters/kernel_candidate_policy.py",
    "optimization_lab/harness_builder/adapters/kernel_candidate_invocation.py",
    "optimization_lab/harness_builder/adapters/kernelbench_meta_worker.py",
)
_SCORER_FILES = (
    *_RUNTIME_FILES,
    "optimization_lab/harness_builder/adapters/kernelbench_meta.py",
    "optimization_lab/harness_builder/adapters/kernelbench_meta_isolation.py",
    "optimization_lab/harness_builder/adapters/kernelbenchx_isolation.py",
    "scripts/hb_gen1_kernelbench_meta_supervisor.py",
)
_RUNTIME_MOUNT = "/opt/hb-kernelbench-meta-runtime"
_WORKER_RELATIVE = (
    "optimization_lab/harness_builder/adapters/kernelbench_meta_worker.py"
)


@dataclass(frozen=True)
class KernelBenchMetaNamespace:
    argv_prefix: tuple[str, ...]
    cwd: Path
    host_environment_items: tuple[tuple[str, str], ...]
    repository_mount: str
    candidate_mount: str
    untrusted_output_mount: str
    worker_uid: int
    worker_gid: int

    @property
    def host_environment(self) -> dict[str, str]:
        return dict(self.host_environment_items)


@dataclass(frozen=True)
class StagedKernelBenchMetaRuntime:
    root: Path
    bundle_sha256: str


@dataclass(frozen=True)
class KernelBenchMetaWorkerCommand:
    launch: BubblewrapCommand
    result_fd: int
    runtime_bundle_sha256: str


def _read_trusted_file(path: Path) -> bytes:
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise SandboxContractError("trusted meta runtime file is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise SandboxContractError("trusted meta runtime file must be regular")
    if metadata.st_size > 2 * 1024 * 1024:
        raise SandboxContractError("trusted meta runtime file is too large")
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            raw = stream.read(2 * 1024 * 1024 + 1)
    except OSError as exc:
        raise SandboxContractError("trusted meta runtime file is unreadable") from exc
    if len(raw) != metadata.st_size:
        raise SandboxContractError("trusted meta runtime file changed size")
    return raw


def kernelbench_meta_runtime_bundle_sha256(project_root: Path) -> str:
    root = project_root.absolute()
    digest = hashlib.sha256(b"HB-GEN-1-KERNELBENCH-META-RUNTIME-V1\0")
    for relative in _RUNTIME_FILES:
        raw = _read_trusted_file(root / relative)
        digest.update(relative.encode("utf-8") + b"\0" + hashlib.sha256(raw).digest())
    return digest.hexdigest()


def kernelbench_meta_scorer_bundle_sha256(project_root: Path) -> str:
    root = project_root.absolute()
    digest = hashlib.sha256(b"HB-GEN-1-KERNELBENCH-META-SCORER-V1\0")
    for relative in _SCORER_FILES:
        raw = _read_trusted_file(root / relative)
        digest.update(relative.encode("utf-8") + b"\0" + hashlib.sha256(raw).digest())
    return digest.hexdigest()


def stage_kernelbench_meta_runtime(
    *, project_root: Path, staging_root: Path
) -> StagedKernelBenchMetaRuntime:
    """Copy only the three trusted runtime modules into an immutable tree."""

    project_root = project_root.absolute()
    staging_root = staging_root.absolute()
    if staging_root.exists():
        raise SandboxContractError("trusted meta runtime staging root already exists")
    bundle_sha = kernelbench_meta_runtime_bundle_sha256(project_root)
    try:
        staging_root.mkdir(parents=True, mode=0o700)
        directories = {staging_root}
        for relative in _RUNTIME_FILES:
            destination = staging_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            directories.update(destination.parents)
            raw = _read_trusted_file(project_root / relative)
            descriptor = os.open(
                destination,
                os.O_WRONLY
                | os.O_CREAT
                | os.O_EXCL
                | getattr(os, "O_NOFOLLOW", 0),
                0o400,
            )
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(raw)
            destination.chmod(0o444)
        for package in (
            "optimization_lab/__init__.py",
            "optimization_lab/harness_builder/__init__.py",
            "optimization_lab/harness_builder/adapters/__init__.py",
        ):
            destination = staging_root / package
            if destination.exists():
                continue
            destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            descriptor = os.open(
                destination,
                os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
                0o400,
            )
            os.close(descriptor)
            destination.chmod(0o444)
        for directory in sorted(
            (path for path in staging_root.rglob("*") if path.is_dir()),
            key=lambda path: len(path.parts),
            reverse=True,
        ):
            directory.chmod(0o555)
        # The tree is mounted read-only, but the remapped non-root worker must
        # still be able to traverse its mount root.
        staging_root.chmod(0o555)
    except Exception:
        try:
            staging_root.chmod(0o700)
            for root, directories, files in os.walk(staging_root):
                Path(root).chmod(0o700)
                for name in directories:
                    (Path(root) / name).chmod(0o700)
                for name in files:
                    (Path(root) / name).chmod(0o600)
            shutil.rmtree(staging_root)
        except OSError:
            pass
        raise
    return StagedKernelBenchMetaRuntime(staging_root, bundle_sha)


def build_kernelbench_meta_namespace(spec: BubblewrapSpec) -> KernelBenchMetaNamespace:
    """Validate and compile the common namespace without choosing a scorer.

    The returned prefix ends immediately before the worker executable.  This is
    intentional: appending the legacy same-process scorer would weaken the
    candidate/result separation.  Only the canaried CandidateInvocationABI-v1
    worker may be appended by the production supervisor.
    """

    launch: BubblewrapCommand = build_bubblewrap_command(spec)
    try:
        executable_index = launch.argv.index("/bin/bash")
    except ValueError as exc:  # pragma: no cover - protects a shared ABI change
        raise SandboxContractError("shared bubblewrap command shape changed") from exc
    prefix = launch.argv[:executable_index]
    if not prefix or prefix[-2:] != ("--chdir", launch.repository_mount):
        raise SandboxContractError("shared bubblewrap namespace prefix changed")
    return KernelBenchMetaNamespace(
        argv_prefix=prefix,
        cwd=launch.cwd,
        host_environment_items=launch.host_environment_items,
        repository_mount=launch.repository_mount,
        candidate_mount=launch.candidate_mount,
        untrusted_output_mount=launch.output_mount,
        worker_uid=launch.worker_uid,
        worker_gid=launch.worker_gid,
    )


def build_kernelbench_meta_worker_command(
    *,
    spec: BubblewrapSpec,
    runtime: StagedKernelBenchMetaRuntime,
    result_fd: int,
    worker_arguments: Sequence[str],
) -> KernelBenchMetaWorkerCommand:
    """Attach the trusted worker and one anonymous result descriptor."""

    if result_fd != 3:
        raise SandboxContractError("trusted result descriptor must be canonical fd 3")
    root = runtime.root.absolute()
    if not root.is_dir() or root.is_symlink():
        raise SandboxContractError("trusted meta runtime root must be a real directory")
    if kernelbench_meta_runtime_bundle_sha256(root) != runtime.bundle_sha256:
        raise SandboxContractError("trusted meta runtime bundle digest differs")
    namespace = build_kernelbench_meta_namespace(spec)
    python_relative = spec.python_executable.relative_to(spec.python_prefix).as_posix()
    python_inside = f"/opt/hb-python/{python_relative}"
    worker_inside = f"{_RUNTIME_MOUNT}/{_WORKER_RELATIVE}"
    prefix = namespace.argv_prefix
    if prefix[-2:] != ("--chdir", namespace.repository_mount):
        raise SandboxContractError("meta namespace prefix shape changed")
    argv = (
        *prefix[:-2],
        "--ro-bind",
        str(root),
        _RUNTIME_MOUNT,
        "--preserve-fds",
        "1",
        *prefix[-2:],
        python_inside,
        "-I",
        worker_inside,
        *tuple(worker_arguments),
        "--result-fd",
        str(result_fd),
    )
    launch = BubblewrapCommand(
        argv=tuple(argv),
        cwd=namespace.cwd,
        host_environment_items=namespace.host_environment_items,
        repository_mount=namespace.repository_mount,
        candidate_mount=namespace.candidate_mount,
        output_mount=namespace.untrusted_output_mount,
        worker_uid=namespace.worker_uid,
        worker_gid=namespace.worker_gid,
    )
    return KernelBenchMetaWorkerCommand(
        launch=launch,
        result_fd=result_fd,
        runtime_bundle_sha256=runtime.bundle_sha256,
    )


__all__ = [
    "KernelBenchMetaNamespace",
    "KernelBenchMetaWorkerCommand",
    "StagedKernelBenchMetaRuntime",
    "build_kernelbench_meta_namespace",
    "build_kernelbench_meta_worker_command",
    "kernelbench_meta_runtime_bundle_sha256",
    "kernelbench_meta_scorer_bundle_sha256",
    "stage_kernelbench_meta_runtime",
]
