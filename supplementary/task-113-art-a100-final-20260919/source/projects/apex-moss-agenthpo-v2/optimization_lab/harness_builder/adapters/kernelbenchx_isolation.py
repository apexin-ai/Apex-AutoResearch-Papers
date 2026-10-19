"""Executable isolation boundary for the HB-GEN-1 KernelBenchX worker.

The trusted supervisor remains outside this module.  The official KernelBenchX
pipeline and candidate are deliberately treated as one hostile worker.  The
worker receives only an immutable staged evaluator snapshot, an immutable
candidate, three per-attempt writable mounts, and the selected GPU devices.
It never receives the host repository, the supervisor result directory, the
parent environment, the host network namespace, or the host PID namespace.

There is intentionally no direct-subprocess fallback.  If a root-owned,
non-writable bubblewrap binary or the required namespace boundary is not
available, formal evaluation fails closed.
"""

from __future__ import annotations

import io
import hashlib
import os
import re
import shutil
import signal
import stat
import subprocess
import tarfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Mapping, Sequence


WORKER_UID = 65_534
WORKER_GID = 65_534
_SAFE_GPU = re.compile(r"[0-9]+")
_SAFE_CANDIDATE_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}\.py")
_SAFE_COMMIT = re.compile(r"[0-9a-f]{40}")
_ALLOWED_SYSTEM_ROOTS = frozenset(
    {"/bin", "/sbin", "/lib", "/lib64", "/usr", "/usr/local"}
)
_WORKER_CC = "/usr/bin/x86_64-linux-gnu-gcc-12"
_WORKER_CXX = "/usr/bin/x86_64-linux-gnu-g++-12"


class SandboxContractError(RuntimeError):
    """The mandatory worker sandbox cannot be established exactly."""


def hash_immutable_tree(root: Path) -> str:
    """Hash one small regular-file tree with path and type domain separation."""

    root = root.absolute()
    try:
        root_metadata = root.lstat()
    except OSError as exc:
        raise SandboxContractError("immutable header snapshot is missing") from exc
    if stat.S_ISLNK(root_metadata.st_mode) or not stat.S_ISDIR(root_metadata.st_mode):
        raise SandboxContractError("immutable header snapshot must be a real directory")
    try:
        entries = sorted(
            root.rglob("*"), key=lambda path: path.relative_to(root).as_posix()
        )
    except OSError as exc:
        raise SandboxContractError("cannot enumerate immutable header snapshot") from exc
    if not entries or len(entries) > 4_096:
        raise SandboxContractError("immutable header snapshot size is invalid")
    digest = hashlib.sha256()
    total_bytes = 0
    for path in entries:
        relative = path.relative_to(root).as_posix().encode("utf-8")
        try:
            metadata = path.lstat()
        except OSError as exc:
            raise SandboxContractError("cannot inspect immutable header snapshot") from exc
        if stat.S_ISDIR(metadata.st_mode):
            digest.update(b"D\0" + relative + b"\0")
            continue
        if not stat.S_ISREG(metadata.st_mode):
            raise SandboxContractError("immutable header snapshot has a special file")
        if metadata.st_size > 4 * 1024 * 1024:
            raise SandboxContractError("immutable header snapshot file is too large")
        try:
            descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
            with os.fdopen(descriptor, "rb") as stream:
                if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                    raise SandboxContractError(
                        "immutable header snapshot file changed type"
                    )
                content = stream.read(4 * 1024 * 1024 + 1)
        except OSError as exc:
            raise SandboxContractError("cannot read immutable header snapshot") from exc
        if len(content) != metadata.st_size:
            raise SandboxContractError("immutable header snapshot file changed size")
        total_bytes += len(content)
        if total_bytes > 16 * 1024 * 1024:
            raise SandboxContractError("immutable header snapshot is too large")
        digest.update(b"F\0" + relative + b"\0" + hashlib.sha256(content).digest())
    return digest.hexdigest()


@dataclass(frozen=True)
class BubblewrapSpec:
    bwrap_path: Path
    repository_snapshot: Path
    candidate_snapshot: Path
    output_dir: Path
    worker_tmp_dir: Path
    cache_dir: Path
    python_prefix: Path
    python_executable: Path
    python_include: Path
    python_include_sha256: str
    gpu: str
    system_roots: tuple[Path, ...]
    gpu_devices: tuple[Path, ...]
    worker_uid: int = WORKER_UID
    worker_gid: int = WORKER_GID


@dataclass(frozen=True)
class BubblewrapCommand:
    argv: tuple[str, ...]
    cwd: Path
    host_environment_items: tuple[tuple[str, str], ...]
    repository_mount: str
    candidate_mount: str
    output_mount: str
    worker_uid: int
    worker_gid: int

    @property
    def host_environment(self) -> dict[str, str]:
        return dict(self.host_environment_items)


@dataclass(frozen=True)
class StagedWorkerInputs:
    repository_snapshot: Path
    candidate_snapshot: Path


@dataclass(frozen=True)
class IsolatedProcessOutcome:
    returncode: int
    timed_out: bool
    quiescent: bool
    elapsed_seconds: float


def _read_regular_candidate(candidate: Path, *, limit: int = 2 * 1024 * 1024) -> bytes:
    try:
        metadata = candidate.lstat()
    except OSError as exc:
        raise SandboxContractError("candidate input is missing") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise SandboxContractError("candidate input must be a regular file")
    try:
        descriptor = os.open(candidate, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise SandboxContractError("candidate input must remain regular")
            raw = stream.read(limit + 1)
    except OSError as exc:
        raise SandboxContractError("candidate input cannot be read") from exc
    if len(raw) > limit:
        raise SandboxContractError("candidate input is too large")
    return raw


def _safe_archive_name(name: str) -> Path:
    if not name or name.startswith("/") or "\x00" in name:
        raise SandboxContractError("git archive contains an unsafe path")
    parts = name.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise SandboxContractError("git archive contains an unsafe path")
    return Path(*parts)


def stage_git_worker_inputs(
    *,
    repository: Path,
    commit: str,
    candidate: Path,
    staging_root: Path,
) -> StagedWorkerInputs:
    """Materialize only the pinned Git tree and candidate into immutable inputs.

    The original checkout is never mounted.  In particular, ignored and
    untracked files (including a poisoned ``sitecustomize.py``) cannot enter the
    worker namespace.
    """

    if not _SAFE_COMMIT.fullmatch(commit):
        raise SandboxContractError("invalid repository commit")
    repository = repository.absolute()
    staging_root = staging_root.absolute()
    if not repository.is_dir() or repository.is_symlink():
        raise SandboxContractError("host repository must be a real directory")
    if staging_root.exists():
        raise SandboxContractError("worker staging root already exists")
    candidate_bytes = _read_regular_candidate(candidate.absolute())
    if not _SAFE_CANDIDATE_NAME.fullmatch(candidate.name):
        raise SandboxContractError("candidate input has an unsafe filename")
    try:
        archive_process = subprocess.run(
            (
                "git",
                "-C",
                str(repository),
                "archive",
                "--format=tar",
                commit,
            ),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=60,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise SandboxContractError("cannot materialize frozen Git tree") from exc
    if archive_process.returncode != 0:
        raise SandboxContractError("cannot materialize frozen Git tree")
    if len(archive_process.stdout) > 256 * 1024 * 1024:
        raise SandboxContractError("frozen Git tree exceeds the staging limit")

    repository_snapshot = staging_root / "repository"
    candidate_dir = staging_root / "candidate"
    candidate_snapshot = candidate_dir / candidate.name
    try:
        staging_root.mkdir(parents=True, mode=0o700)
        repository_snapshot.mkdir(mode=0o700)
        candidate_dir.mkdir(mode=0o700)
        directories = {repository_snapshot}
        with tarfile.open(fileobj=io.BytesIO(archive_process.stdout), mode="r:") as archive:
            members = archive.getmembers()
            if len(members) > 10_000:
                raise SandboxContractError("frozen Git tree has too many entries")
            total_size = 0
            for member in members:
                relative = _safe_archive_name(member.name.rstrip("/"))
                destination = repository_snapshot / relative
                if member.isdir():
                    destination.mkdir(parents=True, exist_ok=True, mode=0o700)
                    directories.add(destination)
                    continue
                if member.issym() or member.islnk():
                    raise SandboxContractError(
                        "frozen Git tree contains a forbidden symlink"
                    )
                if not member.isreg():
                    raise SandboxContractError(
                        "frozen Git tree contains a special file"
                    )
                total_size += member.size
                if total_size > 256 * 1024 * 1024:
                    raise SandboxContractError("frozen Git tree exceeds the staging limit")
                destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
                directories.add(destination.parent)
                source = archive.extractfile(member)
                if source is None:
                    raise SandboxContractError("cannot read frozen Git member")
                data = source.read(member.size + 1)
                if len(data) != member.size:
                    raise SandboxContractError("frozen Git member size differs")
                descriptor = os.open(
                    destination,
                    os.O_WRONLY
                    | os.O_CREAT
                    | os.O_EXCL
                    | getattr(os, "O_NOFOLLOW", 0),
                    0o500 if member.mode & 0o111 else 0o400,
                )
                with os.fdopen(descriptor, "wb") as stream:
                    stream.write(data)
                destination.chmod(0o555 if member.mode & 0o111 else 0o444)
        descriptor = os.open(
            candidate_snapshot,
            os.O_WRONLY
            | os.O_CREAT
            | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0),
            0o400,
        )
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(candidate_bytes)
        candidate_snapshot.chmod(0o444)
        candidate_dir.chmod(0o555)
        for directory in sorted(directories, key=lambda path: len(path.parts), reverse=True):
            directory.chmod(0o555)
        staging_root.chmod(0o500)
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
    return StagedWorkerInputs(
        repository_snapshot=repository_snapshot,
        candidate_snapshot=candidate_snapshot,
    )


def resolve_trusted_bwrap(
    *, candidates: Sequence[Path] = (Path("/usr/bin/bwrap"), Path("/bin/bwrap"))
) -> Path:
    """Return a system-owned bubblewrap binary or fail closed.

    A user-controlled executable is not an isolation boundary.  PATH lookup is
    intentionally avoided for the formal path.
    """

    for candidate in candidates:
        try:
            metadata = candidate.lstat()
        except OSError:
            continue
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            continue
        if metadata.st_uid != 0 or metadata.st_mode & 0o022:
            continue
        if not os.access(candidate, os.X_OK):
            continue
        return candidate
    raise SandboxContractError(
        "a root-owned, non-writable bubblewrap binary is required"
    )


def discover_system_roots() -> tuple[Path, ...]:
    """Return the narrow host runtime roots permitted in the worker namespace."""

    roots: list[Path] = []
    for value in ("/usr", "/bin", "/sbin", "/lib", "/lib64"):
        path = Path(value)
        if path.exists():
            roots.append(path)
    return tuple(roots)


def discover_gpu_devices(gpu: str) -> tuple[Path, ...]:
    if not _SAFE_GPU.fullmatch(gpu):
        raise SandboxContractError("GPU must be one numeric device id")
    required = (Path(f"/dev/nvidia{gpu}"), Path("/dev/nvidiactl"))
    optional = (Path("/dev/nvidia-uvm"), Path("/dev/nvidia-uvm-tools"))
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise SandboxContractError("selected GPU device boundary is unavailable")
    devices = [*required, *(path for path in optional if path.exists())]
    for path in devices:
        try:
            metadata = path.stat()
        except OSError as exc:
            raise SandboxContractError("cannot inspect selected GPU device") from exc
        if not stat.S_ISCHR(metadata.st_mode):
            raise SandboxContractError("GPU boundary contains a non-device path")
    return tuple(devices)


def _absolute(path: Path, label: str) -> Path:
    if not path.is_absolute():
        raise SandboxContractError(f"{label} must be absolute")
    return path


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _validate_spec(spec: BubblewrapSpec) -> None:
    _absolute(spec.bwrap_path, "bubblewrap path")
    if not _SAFE_GPU.fullmatch(spec.gpu):
        raise SandboxContractError("GPU must be one numeric device id")
    if spec.worker_uid <= 0 or spec.worker_gid <= 0:
        raise SandboxContractError("worker uid/gid must be non-root")
    if spec.worker_uid > 2**31 - 1 or spec.worker_gid > 2**31 - 1:
        raise SandboxContractError("worker uid/gid is out of range")

    repository = _absolute(spec.repository_snapshot, "repository snapshot")
    candidate = _absolute(spec.candidate_snapshot, "candidate snapshot")
    python_prefix = _absolute(spec.python_prefix, "Python prefix")
    python_executable = _absolute(spec.python_executable, "Python executable")
    python_include = _absolute(spec.python_include, "Python include snapshot")
    if not repository.is_dir() or repository.is_symlink():
        raise SandboxContractError("repository snapshot must be a real directory")
    if not candidate.is_file() or candidate.is_symlink():
        raise SandboxContractError("candidate snapshot must be a regular file")
    if not _SAFE_CANDIDATE_NAME.fullmatch(candidate.name):
        raise SandboxContractError("candidate snapshot has an unsafe filename")
    if not python_prefix.is_dir() or python_prefix.is_symlink():
        raise SandboxContractError("Python prefix must be a real directory")
    if not python_executable.is_file():
        raise SandboxContractError("Python executable must be a regular file")
    if not _is_relative_to(python_executable, python_prefix):
        raise SandboxContractError("Python executable must be within its prefix")
    try:
        resolved_python = python_executable.resolve(strict=True)
    except OSError as exc:
        raise SandboxContractError("Python executable cannot be resolved") from exc
    safe_python_targets = (python_prefix.resolve(), Path("/usr"), Path("/bin"))
    if not any(
        resolved_python == root or _is_relative_to(resolved_python, root)
        for root in safe_python_targets
    ):
        raise SandboxContractError("Python executable symlink escapes trusted roots")
    if not re.fullmatch(r"[0-9a-f]{64}", spec.python_include_sha256):
        raise SandboxContractError("invalid Python header snapshot digest")
    if hash_immutable_tree(python_include) != spec.python_include_sha256:
        raise SandboxContractError("Python header snapshot digest differs")
    for relative in (
        "python3.10/Python.h",
        "x86_64-linux-gnu/python3.10/pyconfig.h",
    ):
        try:
            metadata = (python_include / relative).lstat()
        except OSError as exc:
            raise SandboxContractError("required Python header is missing") from exc
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise SandboxContractError("required Python header must be regular")

    writable = (
        _absolute(spec.output_dir, "output directory"),
        _absolute(spec.worker_tmp_dir, "worker tmp directory"),
        _absolute(spec.cache_dir, "cache directory"),
    )
    for path in writable:
        if not path.is_dir() or path.is_symlink():
            raise SandboxContractError("worker writable roots must be real directories")
    for index, left in enumerate(writable):
        for right in writable[index + 1 :]:
            if left == right or _is_relative_to(left, right) or _is_relative_to(
                right, left
            ):
                raise SandboxContractError("worker writable roots must be disjoint")
    for immutable in (repository, candidate, python_prefix, python_include):
        if any(
            immutable == root
            or _is_relative_to(immutable, root)
            or _is_relative_to(root, immutable)
            for root in writable
        ):
            raise SandboxContractError(
                "immutable worker inputs must not overlap writable roots"
            )

    for root in spec.system_roots:
        value = str(_absolute(root, "runtime root"))
        if value not in _ALLOWED_SYSTEM_ROOTS:
            raise SandboxContractError("runtime root is outside the narrow allowlist")
    for device in spec.gpu_devices:
        value = str(_absolute(device, "GPU device"))
        if value not in {
            f"/dev/nvidia{spec.gpu}",
            "/dev/nvidiactl",
            "/dev/nvidia-uvm",
            "/dev/nvidia-uvm-tools",
        }:
            raise SandboxContractError("GPU device is outside the narrow allowlist")


def _minimal_system_roots(roots: Sequence[Path]) -> tuple[Path, ...]:
    result: list[Path] = []
    for root in roots:
        if any(root != parent and _is_relative_to(root, parent) for parent in roots):
            continue
        if root not in result:
            result.append(root)
    return tuple(result)


def _worker_environment(spec: BubblewrapSpec, python_mount: str) -> Mapping[str, str]:
    python_relative = spec.python_executable.relative_to(spec.python_prefix).as_posix()
    python_inside = f"{python_mount}/{python_relative}"
    python_bin = str(Path(python_inside).parent)
    return {
        # Avoid /usr/bin/{cc,gcc} because those symlinks escape through the
        # deliberately unmounted /etc/alternatives tree.  These frozen host
        # paths are covered by the read-only /usr mount and runtime canary.
        "CC": _WORKER_CC,
        "CXX": _WORKER_CXX,
        "CPATH": "/opt/hb-python-include/python3.10:/opt/hb-python-include",
        # Only the selected physical device node is mounted.  CUDA therefore
        # renumbers it to logical device zero inside the namespace.  Reusing
        # the host ordinal (for example ``4``) hides that sole visible device.
        "CUDA_VISIBLE_DEVICES": "0",
        "HOME": "/sandbox/work/home",
        "KERNELBENCHX_GOLDEN_MACHINE": "a100",
        "KERNELBENCHX_GPU_COUNT": "1",
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "PATH": f"{python_bin}:/usr/local/bin:/usr/bin:/bin",
        "PYTHONNOUSERSITE": "1",
        "PYTHONPATH": "/sandbox/repository/data:/sandbox/repository",
        "PYTHONPYCACHEPREFIX": "/sandbox/cache/pycache",
        "PYTHON_BIN": python_inside,
        "TEMP": "/sandbox/work/tmp",
        "TMP": "/sandbox/work/tmp",
        "TMPDIR": "/sandbox/work/tmp",
        "TORCHINDUCTOR_CACHE_DIR": "/sandbox/cache/torchinductor",
        "TORCH_EXTENSIONS_DIR": "/sandbox/cache/torch_extensions",
        "TRITON_CACHE_DIR": "/sandbox/cache/triton",
        "CUDA_CACHE_PATH": "/sandbox/cache/cuda",
        "UV_CACHE_DIR": "/sandbox/cache/uv",
        "XDG_CACHE_HOME": "/sandbox/cache/xdg",
    }


def build_bubblewrap_command(spec: BubblewrapSpec) -> BubblewrapCommand:
    """Compile one explicit bubblewrap command; never infer a weaker fallback."""

    _validate_spec(spec)
    repository_mount = "/sandbox/repository"
    candidate_mount = f"/sandbox/input/{spec.candidate_snapshot.name}"
    output_mount = "/sandbox/output"
    python_mount = "/opt/hb-python"
    python_include_mount = "/opt/hb-python-include"

    argv: list[str] = [
        str(spec.bwrap_path),
        "--die-with-parent",
        "--new-session",
        "--unshare-all",
        # Keep this explicit even though --unshare-all includes it: the command
        # is itself an auditable security artifact.
        "--unshare-net",
        "--uid",
        str(spec.worker_uid),
        "--gid",
        str(spec.worker_gid),
        "--cap-drop",
        "ALL",
        "--clearenv",
        "--proc",
        "/proc",
        "--dev",
        "/dev",
        "--tmpfs",
        "/tmp",
        "--dir",
        "/sandbox",
        "--dir",
        "/sandbox/input",
        "--dir",
        "/opt",
        "--dir",
        "/etc",
    ]
    for root in _minimal_system_roots(spec.system_roots):
        argv.extend(("--ro-bind", str(root), str(root)))
    for path in (Path("/etc/ld.so.cache"), Path("/etc/passwd"), Path("/etc/group")):
        if path.is_file():
            argv.extend(("--ro-bind", str(path), str(path)))
    if Path("/sys").is_dir():
        argv.extend(("--ro-bind", "/sys", "/sys"))
    argv.extend(
        (
            "--ro-bind",
            str(spec.python_prefix),
            python_mount,
            "--ro-bind",
            str(spec.python_include),
            python_include_mount,
            "--ro-bind",
            str(spec.repository_snapshot),
            repository_mount,
            "--ro-bind",
            str(spec.candidate_snapshot),
            candidate_mount,
            "--bind",
            str(spec.output_dir),
            output_mount,
            "--bind",
            str(spec.worker_tmp_dir),
            "/sandbox/work",
            "--bind",
            str(spec.cache_dir),
            "/sandbox/cache",
        )
    )
    for device in spec.gpu_devices:
        argv.extend(("--dev-bind", str(device), str(device)))
    for key, value in sorted(_worker_environment(spec, python_mount).items()):
        argv.extend(("--setenv", key, value))
    argv.extend(
        (
            "--chdir",
            repository_mount,
            "/bin/bash",
            f"{repository_mount}/scripts/run_eval_from_files.sh",
            "--bench-timeout",
            "480",
            candidate_mount,
            output_mount,
            # The official pipeline runs inside the one-device namespace, so
            # its GPU argument is the worker-local ordinal rather than the
            # host's physical device number.
            "0",
        )
    )
    host_environment = (
        ("LANG", "C.UTF-8"),
        ("LC_ALL", "C.UTF-8"),
        ("PATH", "/usr/bin:/bin"),
    )
    return BubblewrapCommand(
        argv=tuple(argv),
        cwd=spec.worker_tmp_dir,
        host_environment_items=host_environment,
        repository_mount=repository_mount,
        candidate_mount=candidate_mount,
        output_mount=output_mount,
        worker_uid=spec.worker_uid,
        worker_gid=spec.worker_gid,
    )


def _group_exists(pgid: int) -> bool:
    try:
        os.killpg(pgid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        # A surviving group outside our authority is still non-quiescent.
        return True
    return True


def ensure_process_group_quiescent(
    pgid: int,
    *,
    killpg: Callable[[int, int], None] = os.killpg,
    group_exists: Callable[[int], bool] = _group_exists,
    sleep: Callable[[float], None] = time.sleep,
    timeout_seconds: float = 2.0,
) -> bool:
    """Kill the complete worker group and prove that the group disappeared."""

    if pgid <= 0 or timeout_seconds < 0:
        return False
    try:
        killpg(pgid, signal.SIGKILL)
    except ProcessLookupError:
        return True
    except (PermissionError, OSError):
        return False
    deadline = time.monotonic() + timeout_seconds
    while group_exists(pgid):
        if time.monotonic() >= deadline:
            return False
        sleep(0.01)
    return True


def run_bubblewrap_process(
    launch: BubblewrapCommand,
    *,
    stdout_path: Path,
    stderr_path: Path,
    timeout_seconds: float,
    popen: Callable[..., object] = subprocess.Popen,
    quiesce: Callable[[int], bool] = ensure_process_group_quiescent,
    pass_fds: tuple[int, ...] = (),
) -> IsolatedProcessOutcome:
    """Run one sandbox and fail closed unless its whole process group is gone."""

    if timeout_seconds <= 0:
        raise SandboxContractError("worker timeout must be positive")
    if any(fd < 3 for fd in pass_fds) or len(set(pass_fds)) != len(pass_fds):
        raise SandboxContractError("worker inherited descriptors are invalid")
    stdout_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    stderr_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    started = time.monotonic()
    process = None
    returncode = 125
    timed_out = False
    quiescent = True
    with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
        try:
            process = popen(
                launch.argv,
                cwd=launch.cwd,
                env=launch.host_environment,
                stdin=subprocess.DEVNULL,
                stdout=stdout,
                stderr=stderr,
                start_new_session=True,
                close_fds=True,
                pass_fds=pass_fds,
            )
            try:
                returncode = int(process.wait(timeout=timeout_seconds))
            except subprocess.TimeoutExpired:
                timed_out = True
                returncode = 124
            finally:
                quiescent = bool(quiesce(int(process.pid)))
                try:
                    process.wait()
                except (ChildProcessError, OSError):
                    pass
        except OSError:
            returncode = 125
            quiescent = process is None
    if not quiescent:
        returncode = 125
    return IsolatedProcessOutcome(
        returncode=returncode,
        timed_out=timed_out,
        quiescent=quiescent,
        elapsed_seconds=time.monotonic() - started,
    )
