from __future__ import annotations

import errno
import hashlib
import json
import os
import re
import stat
import threading
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping, Sequence

if os.name == "nt":
    import ctypes
    import msvcrt
    from ctypes import wintypes
else:
    import fcntl

from optimization_lab.generation import CandidateGenerator, GenerationResult
from optimization_lab.openai_generator import (
    OpenAIResponsesGenerator,
    OpenAIResponsesRequestConfig,
)
from optimization_lab.harness_builder.builder_harness import (
    BuilderHarness,
    BuilderHarnessSpec,
)
from optimization_lab.harness_builder.builder_memory import BuilderMemoryConfig
from optimization_lab.harness_builder.dual_harness import HarnessWorkspace


_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/+-]{0,255}")
_AUDIT_REQUEST_FIELDS = {
    "schema_version",
    "event",
    "operation_id",
    "layer",
    "transport",
    "model",
    "reasoning_effort",
    "prompt_sha256",
    "created_at_utc",
}
_AUDIT_SUCCESS_FIELDS = _AUDIT_REQUEST_FIELDS | {
    "provider",
    "response_sha256",
    "usage",
}
_AUDIT_ERROR_FIELDS = _AUDIT_REQUEST_FIELDS | {"error_type"}
_PROCESS_LOCKS_GUARD = threading.Lock()
_PROCESS_LOCKS: dict[str, threading.Lock] = {}


def _required(payload: Mapping[str, Any], key: str, label: str) -> Any:
    if key not in payload:
        raise ValueError(f"{label} is missing {key}")
    return payload[key]


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise TypeError(f"{label} must be a Mapping")
    return value


def _sequence(value: Any, label: str) -> Sequence[Any]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        raise TypeError(f"{label} must be a sequence")
    return value


def _nonempty_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value


def _json_copy(value: Any, label: str) -> Any:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        return json.loads(encoded)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be JSON serializable") from exc


def experiment_one_builder_view(
    inspection: Mapping[str, Any],
    *,
    builder_memory: BuilderMemoryConfig | None = None,
) -> dict[str, Any]:
    """Project a workspace inspection onto experiment one's Builder allowlist."""

    inspection = _mapping(inspection, "Builder inspection")
    current_sha256 = _nonempty_string(
        _required(inspection, "current_sha256", "Builder inspection"),
        "current Harness sha256",
    )
    current_artifact = _mapping(
        _required(inspection, "current_artifact", "Builder inspection"),
        "current Harness artifact",
    )
    runs = _sequence(
        _required(inspection, "runs", "Builder inspection"), "Builder runs"
    )
    available_harnesses = _sequence(
        _required(inspection, "available_harnesses", "Builder inspection"),
        "available Harnesses",
    )

    public_runs: list[dict[str, Any]] = []
    for run_index, raw_run in enumerate(runs):
        run_label = f"Builder run {run_index}"
        run = _mapping(raw_run, run_label)
        candidate = _nonempty_string(
            _required(run, "candidate", run_label),
            f"{run_label} candidate",
        )
        events = _sequence(_required(run, "events", run_label), f"{run_label} events")
        public_events: list[dict[str, Any]] = []
        for event_index, raw_event in enumerate(events):
            event_label = f"{run_label} event {event_index}"
            event = _mapping(raw_event, event_label)
            public_events.append(
                {
                    "index": _required(event, "index", event_label),
                    "node_id": _required(event, "node_id", event_label),
                    "kind": _required(event, "kind", event_label),
                }
            )
        public_runs.append(
            {
                "run_id": _required(run, "run_id", run_label),
                "harness_sha256": _required(run, "harness_sha256", run_label),
                "candidate": {
                    "sha256": hashlib.sha256(candidate.encode("utf-8")).hexdigest(),
                    "length": len(candidate),
                },
                "score": _required(run, "score", run_label),
                "feedback": _required(run, "feedback", run_label),
                "events": public_events,
            }
        )

    public_harnesses: list[dict[str, Any]] = []
    for harness_index, raw_harness in enumerate(available_harnesses):
        label = f"available Harness {harness_index}"
        harness = _mapping(raw_harness, label)
        harness_runs = _sequence(_required(harness, "runs", label), f"{label} runs")
        harness_decisions = _sequence(
            _required(harness, "decisions", label), f"{label} decisions"
        )
        adoption = _mapping(_required(harness, "adoption", label), f"{label} adoption")
        projected_runs: list[dict[str, Any]] = []
        for harness_run_index, raw_harness_run in enumerate(harness_runs):
            run_label = f"{label} run {harness_run_index}"
            harness_run = _mapping(raw_harness_run, run_label)
            run_events = _sequence(
                _required(harness_run, "events", run_label), f"{run_label} events"
            )
            projected_events: list[dict[str, Any]] = []
            for event_index, raw_event in enumerate(run_events):
                event_label = f"{run_label} event {event_index}"
                event = _mapping(raw_event, event_label)
                projected_events.append(
                    {
                        "index": _required(event, "index", event_label),
                        "node_id": _required(event, "node_id", event_label),
                        "kind": _required(event, "kind", event_label),
                    }
                )
            projected_runs.append(
                {
                    "run_id": _required(harness_run, "run_id", run_label),
                    "score": _required(harness_run, "score", run_label),
                    "feedback": _required(harness_run, "feedback", run_label),
                    "status": _required(harness_run, "status", run_label),
                    "events": projected_events,
                }
            )

        projected_decisions: list[dict[str, Any]] = []
        for decision_index, raw_decision in enumerate(harness_decisions):
            decision_label = f"{label} decision {decision_index}"
            decision = _mapping(raw_decision, decision_label)
            projected_decisions.append(
                {
                    key: _required(decision, key, decision_label)
                    for key in (
                        "run_id",
                        "status",
                        "reason",
                        "previous_harness_sha256",
                        "source_sha256",
                        "base_sha256",
                        "candidate_harness_sha256",
                        "next_harness_sha256",
                        "changed_components",
                    )
                }
            )
        public_harnesses.append(
            {
                "sha256": _required(harness, "sha256", label),
                "schema_version": _required(harness, "schema_version", label),
                "version": _required(harness, "version", label),
                "parent_sha256": _required(harness, "parent_sha256", label),
                "spec": _mapping(_required(harness, "spec", label), f"{label} spec"),
                "is_current": _required(harness, "is_current", label),
                "runs": projected_runs,
                "decisions": projected_decisions,
                "adoption": {
                    "used": _required(adoption, "used", f"{label} adoption"),
                    "run_ids": _required(adoption, "run_ids", f"{label} adoption"),
                },
            }
        )

    if builder_memory is None:
        builder_memory = BuilderMemoryConfig()
    if not isinstance(builder_memory, BuilderMemoryConfig):
        raise TypeError("Builder memory must be a BuilderMemoryConfig")
    projected = {
        "current_sha256": current_sha256,
        "current_artifact": current_artifact,
        "runs": public_runs,
        "available_harnesses": public_harnesses,
        "builder_memory": builder_memory.public_payload(),
    }
    copied = _json_copy(projected, "experiment-one Builder view")
    if not isinstance(copied, dict):
        raise TypeError("experiment-one Builder view must be a JSON object")
    return copied


def _safe_operation_id(value: Any) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None or ".." in value:
        raise ValueError("audit operation id is unsafe")
    return value


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _canonical_line(payload: Mapping[str, Any]) -> bytes:
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


def _process_lock(path: Path) -> threading.Lock:
    key = os.path.normcase(os.path.abspath(os.fspath(path)))
    with _PROCESS_LOCKS_GUARD:
        return _PROCESS_LOCKS.setdefault(key, threading.Lock())


def _reject_unsafe_path(path: Path, message: str) -> None:
    candidates = (path, *path.parents)
    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    for candidate in reversed(candidates):
        try:
            metadata = os.lstat(candidate)
        except FileNotFoundError:
            continue
        except OSError as exc:
            raise ValueError(message) from exc
        if stat.S_ISLNK(metadata.st_mode) or (
            reparse_point
            and getattr(metadata, "st_file_attributes", 0) & reparse_point
        ):
            raise ValueError(message)


if os.name == "nt":
    _KERNEL32 = ctypes.WinDLL("kernel32", use_last_error=True)
    _INVALID_HANDLE_VALUE = wintypes.HANDLE(-1).value
    _GENERIC_READ = 0x80000000
    _GENERIC_WRITE = 0x40000000
    _FILE_SHARE_READ = 0x00000001
    _FILE_SHARE_WRITE = 0x00000002
    _CREATE_NEW = 1
    _OPEN_ALWAYS = 4
    _OPEN_EXISTING = 3
    _FILE_ATTRIBUTE_NORMAL = 0x00000080
    _FILE_ATTRIBUTE_DIRECTORY = 0x00000010
    _FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400
    _FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
    _FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
    _ERROR_ALREADY_EXISTS = 183

    class _ByHandleFileInformation(ctypes.Structure):
        _fields_ = [
            ("file_attributes", wintypes.DWORD),
            ("creation_time", wintypes.FILETIME),
            ("last_access_time", wintypes.FILETIME),
            ("last_write_time", wintypes.FILETIME),
            ("volume_serial_number", wintypes.DWORD),
            ("file_size_high", wintypes.DWORD),
            ("file_size_low", wintypes.DWORD),
            ("number_of_links", wintypes.DWORD),
            ("file_index_high", wintypes.DWORD),
            ("file_index_low", wintypes.DWORD),
        ]

    _KERNEL32.CreateFileW.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.HANDLE,
    ]
    _KERNEL32.CreateFileW.restype = wintypes.HANDLE
    _KERNEL32.GetFileInformationByHandle.argtypes = [
        wintypes.HANDLE,
        ctypes.POINTER(_ByHandleFileInformation),
    ]
    _KERNEL32.GetFileInformationByHandle.restype = wintypes.BOOL
    _KERNEL32.GetFinalPathNameByHandleW.argtypes = [
        wintypes.HANDLE,
        wintypes.LPWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
    ]
    _KERNEL32.GetFinalPathNameByHandleW.restype = wintypes.DWORD
    _KERNEL32.FlushFileBuffers.argtypes = [wintypes.HANDLE]
    _KERNEL32.FlushFileBuffers.restype = wintypes.BOOL
    _KERNEL32.CloseHandle.argtypes = [wintypes.HANDLE]
    _KERNEL32.CloseHandle.restype = wintypes.BOOL


def _timestamp_utc() -> str:
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z")
    )


def _write_all(descriptor: int, payload: bytes) -> None:
    remaining = memoryview(payload)
    while remaining:
        written = os.write(descriptor, remaining)
        if written <= 0:
            raise OSError("audit ledger write made no progress")
        remaining = remaining[written:]


def _normalize_windows_final_path(value: str) -> str:
    if value.startswith("\\\\?\\UNC\\"):
        value = "\\\\" + value[8:]
    elif value.startswith("\\\\?\\"):
        value = value[4:]
    return os.path.normcase(os.path.abspath(value))


def _windows_final_path(handle: int) -> str:
    size = 512
    while True:
        buffer = ctypes.create_unicode_buffer(size)
        written = _KERNEL32.GetFinalPathNameByHandleW(handle, buffer, size, 0)
        if written == 0:
            raise OSError(ctypes.get_last_error(), "cannot resolve audit handle")
        if written < size:
            return _normalize_windows_final_path(buffer.value)
        size = written + 1


def _windows_information(handle: int) -> Any:
    information = _ByHandleFileInformation()
    if not _KERNEL32.GetFileInformationByHandle(handle, ctypes.byref(information)):
        raise OSError(ctypes.get_last_error(), "cannot inspect audit handle")
    return information


def _windows_open_handle(
    path: Path,
    *,
    directory: bool,
    create_new: bool = False,
    open_always: bool = False,
) -> tuple[int, bool]:
    creation = _CREATE_NEW if create_new else (_OPEN_ALWAYS if open_always else _OPEN_EXISTING)
    flags = _FILE_FLAG_OPEN_REPARSE_POINT
    if directory:
        flags |= _FILE_FLAG_BACKUP_SEMANTICS
    else:
        flags |= _FILE_ATTRIBUTE_NORMAL
    ctypes.set_last_error(0)
    handle = _KERNEL32.CreateFileW(
        os.fspath(path),
        _GENERIC_READ | _GENERIC_WRITE,
        _FILE_SHARE_READ | _FILE_SHARE_WRITE,
        None,
        creation,
        flags,
        None,
    )
    if handle == _INVALID_HANDLE_VALUE:
        raise OSError(ctypes.get_last_error(), f"cannot open audit path {path}")
    created = open_always and ctypes.get_last_error() != _ERROR_ALREADY_EXISTS
    return int(handle), created


def _windows_verify_handle(handle: int, path: Path, *, directory: bool) -> None:
    information = _windows_information(handle)
    attributes = information.file_attributes
    if bool(attributes & _FILE_ATTRIBUTE_DIRECTORY) != directory:
        raise ValueError("audit path identity is unsafe")
    if attributes & _FILE_ATTRIBUTE_REPARSE_POINT:
        raise ValueError("audit path identity is unsafe")
    if not directory and information.number_of_links != 1:
        raise ValueError("audit ledger path is unsafe")
    if _windows_final_path(handle) != _normalize_windows_final_path(os.fspath(path)):
        raise ValueError("audit path identity is unsafe")


def _windows_close_handle(handle: int) -> None:
    if not _KERNEL32.CloseHandle(handle):
        raise OSError(ctypes.get_last_error(), "cannot close audit handle")


def _windows_flush_handle(handle: int) -> None:
    if not _KERNEL32.FlushFileBuffers(handle):
        raise OSError(ctypes.get_last_error(), "cannot synchronize audit metadata")


def _windows_open_directory_path(path: Path) -> int:
    path = Path(os.path.abspath(os.fspath(path)))
    missing_components: list[str] = []
    existing = path
    while True:
        try:
            os.lstat(existing)
            break
        except FileNotFoundError:
            if existing == existing.parent:
                raise
            missing_components.append(existing.name)
            existing = existing.parent

    handle, _ = _windows_open_handle(existing, directory=True)
    try:
        _windows_verify_handle(handle, existing, directory=True)
        current = existing
        for component in reversed(missing_components):
            child = current / component
            try:
                os.mkdir(child, mode=0o700)
                created = True
            except FileExistsError:
                created = False
            child_handle, _ = _windows_open_handle(child, directory=True)
            try:
                _windows_verify_handle(child_handle, child, directory=True)
                if created:
                    _windows_flush_handle(handle)
            except BaseException:
                _windows_close_handle(child_handle)
                raise
            _windows_close_handle(handle)
            handle = child_handle
            current = child
        return handle
    except BaseException:
        _windows_close_handle(handle)
        raise


def _windows_open_child_directory(parent_handle: int, path: Path) -> int:
    try:
        os.mkdir(path, mode=0o700)
        created = True
    except FileExistsError:
        created = False
    handle, _ = _windows_open_handle(path, directory=True)
    try:
        _windows_verify_handle(handle, path, directory=True)
        if created:
            _windows_flush_handle(parent_handle)
        return handle
    except BaseException:
        _windows_close_handle(handle)
        raise


def _verify_posix_file_identity(
    pinned: Any, authoritative: Any, message: str
) -> None:
    if (
        not stat.S_ISREG(pinned.st_mode)
        or not stat.S_ISREG(authoritative.st_mode)
        or pinned.st_nlink != 1
        or authoritative.st_nlink != 1
    ):
        raise ValueError(message)
    if (pinned.st_dev, pinned.st_ino) != (
        authoritative.st_dev,
        authoritative.st_ino,
    ):
        raise ValueError(f"{message}: identity changed")


def _verify_posix_directory_identity(
    pinned: Any, authoritative: Any, message: str
) -> None:
    if not stat.S_ISDIR(pinned.st_mode) or not stat.S_ISDIR(authoritative.st_mode):
        raise ValueError(message)
    if (pinned.st_dev, pinned.st_ino) != (
        authoritative.st_dev,
        authoritative.st_ino,
    ):
        raise ValueError(f"{message}: identity changed")


class _PinnedAuditSession:
    def __init__(self, owner: "AuditedGenerator") -> None:
        self.owner = owner
        self.parent_descriptor: int | None = None
        self.parent_handle: int | None = None
        self.lock_descriptor: int | None = None
        self.ledger_descriptor: int | None = None
        self.claim_directory_descriptor: int | None = None
        self.claim_directory_handle: int | None = None

    def __enter__(self) -> "_PinnedAuditSession":
        if os.name == "nt":
            self._open_windows()
        else:
            self._open_posix()
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        for descriptor_name in (
            "claim_directory_descriptor",
            "ledger_descriptor",
            "lock_descriptor",
            "parent_descriptor",
        ):
            descriptor = getattr(self, descriptor_name)
            if descriptor is not None:
                os.close(descriptor)
                setattr(self, descriptor_name, None)
        for handle_name in ("claim_directory_handle", "parent_handle"):
            handle = getattr(self, handle_name)
            if handle is not None:
                _windows_close_handle(handle)
                setattr(self, handle_name, None)

    def _open_windows(self) -> None:
        owner = self.owner
        owner._validate_paths()
        parent_handle = _windows_open_directory_path(owner.audit_path.parent)
        claim_handle = _windows_open_child_directory(
            parent_handle, owner._claim_directory
        )
        try:
            _windows_verify_handle(parent_handle, owner.audit_path.parent, directory=True)
            _windows_verify_handle(claim_handle, owner._claim_directory, directory=True)
            lock_handle, lock_created = _windows_open_handle(
                owner._lock_path, directory=False, open_always=True
            )
            try:
                _windows_verify_handle(lock_handle, owner._lock_path, directory=False)
                ledger_handle, ledger_created = _windows_open_handle(
                    owner.audit_path, directory=False, open_always=True
                )
                try:
                    _windows_verify_handle(ledger_handle, owner.audit_path, directory=False)
                    self.lock_descriptor = msvcrt.open_osfhandle(
                        lock_handle, os.O_RDWR | getattr(os, "O_BINARY", 0)
                    )
                    lock_handle = 0
                    self.ledger_descriptor = msvcrt.open_osfhandle(
                        ledger_handle, os.O_RDWR | getattr(os, "O_BINARY", 0)
                    )
                    ledger_handle = 0
                finally:
                    if ledger_handle:
                        _windows_close_handle(ledger_handle)
            finally:
                if lock_handle:
                    _windows_close_handle(lock_handle)
            self.parent_handle = parent_handle
            self.claim_directory_handle = claim_handle
            parent_handle = 0
            claim_handle = 0
            if os.fstat(self.lock_descriptor).st_size == 0:
                os.ftruncate(self.lock_descriptor, 1)
                os.fsync(self.lock_descriptor)
            if lock_created:
                _windows_flush_handle(self.parent_handle)
            if ledger_created:
                os.fsync(self.ledger_descriptor)
                _windows_flush_handle(self.parent_handle)
        finally:
            if claim_handle:
                _windows_close_handle(claim_handle)
            if parent_handle:
                _windows_close_handle(parent_handle)

    @staticmethod
    def _open_posix_directory(path: Path) -> int:
        path = Path(os.path.abspath(os.fspath(path)))
        root = Path(path.anchor)
        descriptor = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
        try:
            for component in path.parts[1:]:
                try:
                    os.mkdir(component, mode=0o700, dir_fd=descriptor)
                    os.fsync(descriptor)
                except FileExistsError:
                    pass
                try:
                    next_descriptor = os.open(
                        component,
                        os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                        dir_fd=descriptor,
                    )
                except OSError as exc:
                    if exc.errno in {errno.ELOOP, errno.ENOTDIR}:
                        raise ValueError("audit ledger path is unsafe") from exc
                    raise
                try:
                    if not stat.S_ISDIR(os.fstat(next_descriptor).st_mode):
                        raise ValueError("audit ledger path is unsafe")
                except BaseException:
                    os.close(next_descriptor)
                    raise
                try:
                    os.close(descriptor)
                except BaseException:
                    os.close(next_descriptor)
                    raise
                descriptor = next_descriptor
            return descriptor
        except BaseException:
            os.close(descriptor)
            raise

    def _open_posix_file(self, name: str) -> tuple[int, bool]:
        assert self.parent_descriptor is not None
        flags = os.O_RDWR | os.O_NOFOLLOW | getattr(os, "O_CLOEXEC", 0)
        try:
            descriptor = os.open(
                name,
                flags | os.O_CREAT | os.O_EXCL,
                0o600,
                dir_fd=self.parent_descriptor,
            )
            created = True
        except FileExistsError:
            descriptor = os.open(name, flags, dir_fd=self.parent_descriptor)
            created = False
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
            os.close(descriptor)
            raise ValueError("audit ledger path is unsafe")
        return descriptor, created

    def _open_posix(self) -> None:
        owner = self.owner
        self.parent_descriptor = self._open_posix_directory(owner.audit_path.parent)
        try:
            try:
                os.mkdir(owner._claim_directory.name, mode=0o700, dir_fd=self.parent_descriptor)
                os.fsync(self.parent_descriptor)
            except FileExistsError:
                pass
            self.claim_directory_descriptor = os.open(
                owner._claim_directory.name,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                dir_fd=self.parent_descriptor,
            )
            self.lock_descriptor, lock_created = self._open_posix_file(owner._lock_path.name)
            self.ledger_descriptor, ledger_created = self._open_posix_file(owner.audit_path.name)
            if os.fstat(self.lock_descriptor).st_size == 0:
                os.ftruncate(self.lock_descriptor, 1)
                os.fsync(self.lock_descriptor)
            if lock_created:
                os.fsync(self.parent_descriptor)
            if ledger_created:
                os.fsync(self.ledger_descriptor)
                os.fsync(self.parent_descriptor)
        except BaseException:
            self.__exit__(None, None, None)
            raise

    def verify_integrity(self) -> None:
        owner = self.owner
        owner._validate_paths()
        if os.name == "nt":
            assert self.parent_handle is not None
            assert self.claim_directory_handle is not None
            assert self.lock_descriptor is not None
            assert self.ledger_descriptor is not None
            _windows_verify_handle(
                self.parent_handle, owner.audit_path.parent, directory=True
            )
            _windows_verify_handle(
                self.claim_directory_handle,
                owner._claim_directory,
                directory=True,
            )
            _windows_verify_handle(
                msvcrt.get_osfhandle(self.lock_descriptor),
                owner._lock_path,
                directory=False,
            )
            _windows_verify_handle(
                msvcrt.get_osfhandle(self.ledger_descriptor),
                owner.audit_path,
                directory=False,
            )
            return

        assert self.parent_descriptor is not None
        assert self.claim_directory_descriptor is not None
        assert self.lock_descriptor is not None
        assert self.ledger_descriptor is not None
        try:
            authoritative_parent = os.stat(
                owner.audit_path.parent, follow_symlinks=False
            )
            authoritative_claim_directory = os.stat(
                owner._claim_directory.name,
                dir_fd=self.parent_descriptor,
                follow_symlinks=False,
            )
            authoritative_lock = os.stat(
                owner._lock_path.name,
                dir_fd=self.parent_descriptor,
                follow_symlinks=False,
            )
            authoritative_ledger = os.stat(
                owner.audit_path.name,
                dir_fd=self.parent_descriptor,
                follow_symlinks=False,
            )
        except OSError as exc:
            raise ValueError("audit path identity is unsafe") from exc
        _verify_posix_directory_identity(
            os.fstat(self.parent_descriptor),
            authoritative_parent,
            "audit path identity is unsafe",
        )
        _verify_posix_directory_identity(
            os.fstat(self.claim_directory_descriptor),
            authoritative_claim_directory,
            "audit claim directory is unsafe",
        )
        _verify_posix_file_identity(
            os.fstat(self.lock_descriptor),
            authoritative_lock,
            "audit ledger path is unsafe",
        )
        _verify_posix_file_identity(
            os.fstat(self.ledger_descriptor),
            authoritative_ledger,
            "audit ledger path is unsafe",
        )

    @contextmanager
    def locked(self) -> Iterator[None]:
        assert self.lock_descriptor is not None
        os.lseek(self.lock_descriptor, 0, os.SEEK_SET)
        if os.name == "nt":
            while True:
                try:
                    msvcrt.locking(self.lock_descriptor, msvcrt.LK_LOCK, 1)
                    break
                except OSError as exc:
                    if exc.errno != errno.EDEADLK:
                        raise
        else:
            fcntl.flock(self.lock_descriptor, fcntl.LOCK_EX)
        try:
            yield
        finally:
            if os.name == "nt":
                os.lseek(self.lock_descriptor, 0, os.SEEK_SET)
                msvcrt.locking(self.lock_descriptor, msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(self.lock_descriptor, fcntl.LOCK_UN)

    def read_ledger(self) -> bytes:
        assert self.ledger_descriptor is not None
        os.lseek(self.ledger_descriptor, 0, os.SEEK_SET)
        chunks: list[bytes] = []
        while True:
            chunk = os.read(self.ledger_descriptor, 1024 * 1024)
            if not chunk:
                return b"".join(chunks)
            chunks.append(chunk)

    def append(self, payload: Mapping[str, Any]) -> int:
        assert self.ledger_descriptor is not None
        offset = os.lseek(self.ledger_descriptor, 0, os.SEEK_END)
        _write_all(self.ledger_descriptor, _canonical_line(payload))
        os.fsync(self.ledger_descriptor)
        return offset

    def append_verified(self, payload: Mapping[str, Any]) -> None:
        self.verify_integrity()
        offset = self.append(payload)
        try:
            self.verify_integrity()
        except BaseException:
            assert self.ledger_descriptor is not None
            os.ftruncate(self.ledger_descriptor, offset)
            os.fsync(self.ledger_descriptor)
            raise

    def claim(self, operation_id: str) -> None:
        claim_name = f"{_sha256_text(operation_id)}.claim"
        if os.name == "nt":
            claim_path = self.owner._claim_directory / claim_name
            try:
                handle, _ = _windows_open_handle(
                    claim_path, directory=False, create_new=True
                )
            except OSError as exc:
                if getattr(exc, "winerror", exc.errno) in {80, 183}:
                    raise ValueError("audit operation id already exists") from exc
                raise ValueError("audit claim path is unsafe") from exc
            try:
                _windows_verify_handle(handle, claim_path, directory=False)
                _windows_flush_handle(handle)
                assert self.claim_directory_handle is not None
                _windows_flush_handle(self.claim_directory_handle)
            finally:
                _windows_close_handle(handle)
            return
        assert self.claim_directory_descriptor is not None
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
        try:
            descriptor = os.open(
                claim_name,
                flags,
                0o600,
                dir_fd=self.claim_directory_descriptor,
            )
        except FileExistsError as exc:
            raise ValueError("audit operation id already exists") from exc
        try:
            metadata = os.fstat(descriptor)
            if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
                raise ValueError("audit claim path is unsafe")
            os.fsync(descriptor)
            os.fsync(self.claim_directory_descriptor)
        finally:
            os.close(descriptor)


def _validate_timestamp(value: Any) -> None:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ValueError("audit ledger timestamp is invalid")
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise ValueError("audit ledger timestamp is invalid") from exc
    if parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise ValueError("audit ledger timestamp is not UTC")


@dataclass(frozen=True)
class _AuditedDelegateBinding:
    generator: CandidateGenerator
    transport_config: OpenAIResponsesRequestConfig | None


@dataclass
class ScopedOperationIdFactory:
    """Issue deterministic, per-call operation ids within one round and layer."""

    round_id: str
    layer: str
    counter: int = 0

    def next(self, scope: str = "call") -> str:
        round_id = _safe_operation_id(self.round_id)
        layer = _safe_operation_id(self.layer)
        scope = _safe_operation_id(scope)
        raw = f"{round_id}-{layer}-{scope}-{self.counter:04d}"
        if len(raw) <= 256:
            value = _safe_operation_id(raw)
        else:
            digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
            value = _safe_operation_id(f"{raw[:191]}-{digest}")
        self.counter += 1
        return value


class AuditedGenerator:
    """Record hash-only model-call evidence around a CandidateGenerator."""

    def __init__(
        self,
        *,
        generator: CandidateGenerator,
        audit_path: Path,
        operation_id_factory: ScopedOperationIdFactory | Callable[[], str],
        layer: str,
        reasoning_effort: str,
        transport_config: OpenAIResponsesRequestConfig | None = None,
    ) -> None:
        if not callable(operation_id_factory) and not callable(
            getattr(operation_id_factory, "next", None)
        ):
            raise TypeError("audit operation id factory must be callable")
        self.audit_path = Path(os.path.abspath(os.fspath(audit_path)))
        self._claim_directory = self.audit_path.with_name(
            f".{self.audit_path.name}.operations"
        )
        self._lock_path = self.audit_path.with_name(f".{self.audit_path.name}.lock")
        self.operation_id_factory = operation_id_factory
        self.layer = _nonempty_string(layer, "audit layer")
        self.reasoning_effort = _nonempty_string(
            reasoning_effort, "audit reasoning effort"
        )
        if transport_config is None and type(generator) is OpenAIResponsesGenerator:
            transport_config = generator.request_config
        if transport_config is not None and (
            type(generator) is not OpenAIResponsesGenerator
            or type(transport_config) is not OpenAIResponsesRequestConfig
        ):
            raise TypeError("unsupported audited transport configuration")
        self._delegate_binding = _AuditedDelegateBinding(generator, transport_config)
        self._lock = _process_lock(self.audit_path)

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "_delegate_binding" and hasattr(self, name):
            raise AttributeError("audited transport binding is immutable")
        super().__setattr__(name, value)

    @property
    def generator(self) -> CandidateGenerator:
        return self._delegate_binding.generator

    @property
    def _transport_config(self) -> OpenAIResponsesRequestConfig | None:
        return self._delegate_binding.transport_config

    def _validated_delegate_binding(self) -> _AuditedDelegateBinding:
        binding = self._delegate_binding
        if type(binding) is not _AuditedDelegateBinding:
            raise TypeError("audited transport binding is invalid")
        generator = binding.generator
        transport_config = binding.transport_config
        if transport_config is not None and (
            type(generator) is not OpenAIResponsesGenerator
            or type(transport_config) is not OpenAIResponsesRequestConfig
            or generator.request_config is not transport_config
        ):
            raise TypeError("audited transport binding is invalid")
        return binding

    def estimated_api_cost_usd(self) -> float:
        return self._validated_delegate_binding().generator.estimated_api_cost_usd()

    def _next_operation_id(self, scope: str) -> str:
        if isinstance(self.operation_id_factory, ScopedOperationIdFactory):
            return _safe_operation_id(self.operation_id_factory.next(scope))
        return _safe_operation_id(self.operation_id_factory())

    def generate(
        self, prompt: str, *, model: str, scope: str = "call"
    ) -> GenerationResult:
        prompt = _nonempty_string(prompt, "audit prompt")
        model = _nonempty_string(model, "audit model")
        binding = self._validated_delegate_binding()
        generator = binding.generator
        transport_config = binding.transport_config
        if transport_config is None:
            delegate_effort = _nonempty_string(
                getattr(generator, "reasoning_effort", None),
                "delegate reasoning effort",
            )
            transport = "test_fixture"
        else:
            delegate_effort = _nonempty_string(
                transport_config.reasoning_effort,
                "delegate reasoning effort",
            )
            transport = "openai_responses"
        if delegate_effort != self.reasoning_effort:
            raise ValueError(
                "audit reasoning effort does not match delegate configuration"
            )
        operation_id = self._next_operation_id(scope)
        request = {
            "operation_id": operation_id,
            "layer": self.layer,
            "transport": transport,
            "model": model,
            "reasoning_effort": self.reasoning_effort,
            "prompt_sha256": _sha256_text(prompt),
        }
        start_payload: dict[str, Any] = {
            "schema_version": 2,
            "event": "start",
            **request,
            "created_at_utc": _timestamp_utc(),
        }

        with _PinnedAuditSession(self) as session:
            with self._lock, session.locked():
                session.verify_integrity()
                existing = self._load_records(session.read_ledger()).get(operation_id)
                if existing is not None:
                    raise ValueError("audit operation id already exists")
                session.claim(operation_id)
                session.append_verified(start_payload)

            try:
                if transport_config is None:
                    result = generator.generate(prompt, model=model)
                else:
                    result = generator.generate_with_request_config(
                        prompt,
                        model=model,
                        request_config=transport_config,
                    )
                if not isinstance(result, GenerationResult):
                    raise TypeError("audited generator must return GenerationResult")
                provider = _nonempty_string(result.provider, "audit provider")
                terminal: dict[str, Any] = {
                    "schema_version": 2,
                    "event": "success",
                    **request,
                    "provider": provider,
                    "response_sha256": _sha256_text(result.raw_response),
                    "usage": _json_copy(result.usage, "audit usage"),
                    "created_at_utc": _timestamp_utc(),
                }
            except BaseException as exc:
                terminal = {
                    "schema_version": 2,
                    "event": "error",
                    **request,
                    "error_type": type(exc).__name__,
                    "created_at_utc": _timestamp_utc(),
                }
                with self._lock, session.locked():
                    session.verify_integrity()
                    self._require_started_operation(
                        self._load_records(session.read_ledger()), operation_id
                    )
                    session.append_verified(terminal)
                raise

            with self._lock, session.locked():
                session.verify_integrity()
                self._require_started_operation(
                    self._load_records(session.read_ledger()), operation_id
                )
                session.append_verified(terminal)
            return result

    def _validate_paths(self) -> None:
        _reject_unsafe_path(self.audit_path, "audit ledger path is unsafe")
        _reject_unsafe_path(
            self._claim_directory, "audit claim directory is unsafe"
        )
        _reject_unsafe_path(self._lock_path, "audit lock path is unsafe")

    @staticmethod
    def _require_started_operation(
        records: Mapping[str, Sequence[Mapping[str, Any]]], operation_id: str
    ) -> None:
        events = records.get(operation_id)
        if events is None or len(events) != 1 or events[0]["event"] != "start":
            raise ValueError("audit operation is not in started state")

    def _load_records(self, raw_ledger: bytes) -> dict[str, list[dict[str, Any]]]:
        if raw_ledger and not raw_ledger.endswith(b"\n"):
            raise ValueError("audit ledger must end with a newline")
        records: dict[str, list[dict[str, Any]]] = {}
        for line_number, raw_line in enumerate(raw_ledger.splitlines(), 1):
            if not raw_line:
                raise ValueError(f"audit ledger line {line_number} is empty")
            try:
                record = json.loads(raw_line.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise ValueError(
                    f"audit ledger line {line_number} is invalid JSON"
                ) from exc
            if not isinstance(record, dict):
                raise ValueError(f"audit ledger line {line_number} has invalid fields")
            event = record.get("event")
            expected_fields = {
                "start": _AUDIT_REQUEST_FIELDS,
                "success": _AUDIT_SUCCESS_FIELDS,
                "error": _AUDIT_ERROR_FIELDS,
            }.get(event)
            if expected_fields is None or set(record) != expected_fields:
                raise ValueError(f"audit ledger line {line_number} has invalid fields")
            if record["schema_version"] != 2:
                raise ValueError("audit ledger schema is unsupported")
            operation_id = _safe_operation_id(record["operation_id"])
            for field in ("layer", "transport", "model", "reasoning_effort"):
                _nonempty_string(record[field], f"audit ledger {field}")
            hash_fields = ["prompt_sha256"]
            if event == "success":
                hash_fields.append("response_sha256")
                _nonempty_string(record["provider"], "audit ledger provider")
                if not isinstance(record["usage"], dict):
                    raise ValueError("audit ledger usage is invalid")
                _json_copy(record["usage"], "audit ledger usage")
            elif event == "error":
                _nonempty_string(record["error_type"], "audit ledger error type")
            for field in hash_fields:
                value = record[field]
                if (
                    not isinstance(value, str)
                    or re.fullmatch(r"[0-9a-f]{64}", value) is None
                ):
                    raise ValueError(f"audit ledger {field} is invalid")
            _validate_timestamp(record["created_at_utc"])
            events = records.setdefault(operation_id, [])
            if not events:
                if event != "start":
                    raise ValueError("audit ledger operation is missing start event")
            elif len(events) != 1 or events[0]["event"] != "start" or event == "start":
                raise ValueError("audit ledger has duplicate operation id")
            else:
                start = events[0]
                for field in (
                    "layer",
                    "transport",
                    "model",
                    "reasoning_effort",
                    "prompt_sha256",
                ):
                    if record[field] != start[field]:
                        raise ValueError(
                            "audit ledger terminal request does not match start"
                        )
            events.append(record)
        return records


@dataclass(frozen=True)
class ExperimentOneAssembly:
    """Mandatory safe model-call wiring for experiment one."""

    builder: BuilderHarness
    solver_generator: AuditedGenerator


def assemble_experiment_one(
    *,
    workspace: HarnessWorkspace,
    builder_generator: CandidateGenerator,
    solver_generator: CandidateGenerator,
    builder_model: str,
    audit_directory: Path,
    builder_operation_id_factory: ScopedOperationIdFactory | Callable[[], str],
    solver_operation_id_factory: ScopedOperationIdFactory | Callable[[], str],
    builder_reasoning_effort: str,
    solver_reasoning_effort: str,
    builder_spec: BuilderHarnessSpec | None = None,
    builder_memory_config: BuilderMemoryConfig | None = None,
) -> ExperimentOneAssembly:
    """Assemble experiment one without exposing unsafe wiring choices."""

    if builder_reasoning_effort != "high" or solver_reasoning_effort != "high":
        raise ValueError("experiment-one reasoning effort must be high")
    if builder_memory_config is None:
        builder_memory_config = BuilderMemoryConfig()
    if not isinstance(builder_memory_config, BuilderMemoryConfig):
        raise TypeError("Builder memory config must be a BuilderMemoryConfig")
    transport_configs: list[OpenAIResponsesRequestConfig] = []
    for layer, generator in (
        ("Builder", builder_generator),
        ("Solver", solver_generator),
    ):
        if type(generator) is not OpenAIResponsesGenerator:
            raise ValueError(
                f"experiment-one {layer} delegate must use a supported transport"
            )
        transport_config = generator.request_config
        if type(transport_config) is not OpenAIResponsesRequestConfig:
            raise ValueError(
                f"experiment-one {layer} delegate must use a supported request configuration"
            )
        if transport_config.reasoning_effort != "high":
            raise ValueError(
                f"experiment-one {layer} delegate reasoning effort must be high"
            )
        transport_configs.append(transport_config)
    audit_directory = Path(os.path.abspath(os.fspath(audit_directory)))
    audited_builder = AuditedGenerator(
        generator=builder_generator,
        audit_path=audit_directory / "builder_model_calls.jsonl",
        operation_id_factory=builder_operation_id_factory,
        layer="builder",
        reasoning_effort=builder_reasoning_effort,
        transport_config=transport_configs[0],
    )
    audited_solver = AuditedGenerator(
        generator=solver_generator,
        audit_path=audit_directory / "solver_model_calls.jsonl",
        operation_id_factory=solver_operation_id_factory,
        layer="solver",
        reasoning_effort=solver_reasoning_effort,
        transport_config=transport_configs[1],
    )
    if builder_memory_config == BuilderMemoryConfig():
        inspection_transform = experiment_one_builder_view
    else:
        def inspection_transform(inspection: Mapping[str, Any]) -> dict[str, Any]:
            return experiment_one_builder_view(
                inspection, builder_memory=builder_memory_config
            )

    builder = BuilderHarness(
        workspace=workspace,
        generator=audited_builder,
        model=builder_model,
        spec=builder_spec,
        inspection_transform=inspection_transform,
    )
    return ExperimentOneAssembly(
        builder=builder,
        solver_generator=audited_solver,
    )


__all__ = [
    "AuditedGenerator",
    "ExperimentOneAssembly",
    "ScopedOperationIdFactory",
    "assemble_experiment_one",
    "experiment_one_builder_view",
]
