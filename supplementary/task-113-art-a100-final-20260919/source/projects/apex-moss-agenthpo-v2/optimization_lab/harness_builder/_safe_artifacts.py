from __future__ import annotations

import errno
import os
import secrets
import stat
from pathlib import Path


_DIRECTORY_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC | os.O_NOFOLLOW
_FILE_FLAGS = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW


def lexical_absolute(path: Path) -> Path:
    """Return an absolute path without resolving any symbolic links."""

    return Path(os.path.abspath(os.fspath(path)))


def _unsafe(label: str) -> ValueError:
    return ValueError(f"unsafe {label} path: symlink or non-directory parent")


def _open_parent(
    path: Path,
    *,
    create: bool,
    label: str,
) -> tuple[int, str, Path]:
    absolute = lexical_absolute(path)
    if absolute == Path(absolute.anchor) or not absolute.name:
        raise ValueError(f"unsafe {label} target")
    descriptor = os.open(absolute.anchor, _DIRECTORY_FLAGS)
    try:
        for component in absolute.parts[1:-1]:
            try:
                child = os.open(component, _DIRECTORY_FLAGS, dir_fd=descriptor)
            except FileNotFoundError:
                if not create:
                    raise
                try:
                    os.mkdir(component, mode=0o700, dir_fd=descriptor)
                except FileExistsError:
                    # A concurrent creator is acceptable only if it created a
                    # real directory; the no-follow open below is authoritative.
                    pass
                try:
                    child = os.open(component, _DIRECTORY_FLAGS, dir_fd=descriptor)
                except OSError as exc:
                    raise _unsafe(label) from exc
            except OSError as exc:
                if exc.errno in {errno.ELOOP, errno.ENOTDIR}:
                    raise _unsafe(label) from exc
                raise
            os.close(descriptor)
            descriptor = child
        return descriptor, absolute.name, absolute
    except Exception:
        os.close(descriptor)
        raise


def ensure_safe_directory(path: Path, *, label: str) -> Path:
    """Create a directory tree while rejecting every symlink component."""

    absolute = lexical_absolute(path)
    marker = absolute / ".moss-safe-directory-check"
    descriptor, _marker_name, _ = _open_parent(marker, create=True, label=label)
    os.close(descriptor)
    return absolute


def safe_regular_file_exists(path: Path, *, label: str) -> bool:
    """Return existence while rejecting links and non-regular targets."""

    try:
        descriptor, name, _ = _open_parent(path, create=False, label=label)
    except FileNotFoundError:
        return False
    try:
        try:
            metadata = os.stat(name, dir_fd=descriptor, follow_symlinks=False)
        except FileNotFoundError:
            return False
        if not stat.S_ISREG(metadata.st_mode):
            raise ValueError(f"unsafe {label} target: expected a regular file")
        return True
    finally:
        os.close(descriptor)


def read_safe_regular_file(path: Path, *, label: str) -> bytes:
    """Read a regular file without following target or parent symlinks."""

    try:
        parent, name, _ = _open_parent(path, create=False, label=label)
    except FileNotFoundError as exc:
        raise ValueError(f"{label} is missing") from exc
    try:
        try:
            metadata = os.stat(name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError as exc:
            raise ValueError(f"{label} is missing") from exc
        if not stat.S_ISREG(metadata.st_mode):
            raise ValueError(f"unsafe {label} target: expected a regular file")
        try:
            descriptor = os.open(name, _FILE_FLAGS, dir_fd=parent)
        except FileNotFoundError as exc:
            raise ValueError(f"{label} is missing") from exc
        except OSError as exc:
            if exc.errno in {errno.ELOOP, errno.ENOTDIR}:
                raise ValueError(
                    f"unsafe {label} target: expected a regular file"
                ) from exc
            raise
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                raise ValueError(
                    f"unsafe {label} target: expected a regular file"
                )
            with os.fdopen(descriptor, "rb", closefd=False) as handle:
                return handle.read()
        finally:
            os.close(descriptor)
    finally:
        os.close(parent)


def write_once_safe_regular_file(
    path: Path,
    content: bytes,
    *,
    label: str,
    temporary_suffix: str,
) -> Path:
    """Atomically bind immutable bytes without following or replacing links."""

    if not isinstance(content, bytes):
        raise TypeError("sealed artifact content must be bytes")
    parent, name, absolute = _open_parent(path, create=True, label=label)
    temporary_name = f".{name}.{secrets.token_hex(16)}{temporary_suffix}"
    temporary_descriptor: int | None = None
    temporary_created = False
    try:
        try:
            metadata = os.stat(name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            metadata = None
        if metadata is not None:
            if not stat.S_ISREG(metadata.st_mode):
                raise ValueError(
                    f"unsafe {label} target: expected a regular file"
                )
            try:
                existing_descriptor = os.open(name, _FILE_FLAGS, dir_fd=parent)
            except OSError as exc:
                if exc.errno in {errno.ELOOP, errno.ENOTDIR}:
                    raise ValueError(
                        f"unsafe {label} target: expected a regular file"
                    ) from exc
                raise
            try:
                if not stat.S_ISREG(os.fstat(existing_descriptor).st_mode):
                    raise ValueError(
                        f"unsafe {label} target: expected a regular file"
                    )
                with os.fdopen(existing_descriptor, "rb", closefd=False) as handle:
                    existing_content = handle.read()
            finally:
                os.close(existing_descriptor)
            if existing_content != content:
                raise ValueError(f"refusing to overwrite a different {label}")
            return absolute

        temporary_descriptor = os.open(
            temporary_name,
            os.O_WRONLY
            | os.O_CREAT
            | os.O_EXCL
            | os.O_CLOEXEC
            | os.O_NOFOLLOW,
            0o600,
            dir_fd=parent,
        )
        temporary_created = True
        with os.fdopen(temporary_descriptor, "wb", closefd=False) as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.close(temporary_descriptor)
        temporary_descriptor = None
        try:
            # link(2) provides the no-replace property missing from os.replace:
            # if another writer or a symlink appeared, this fails closed.
            os.link(
                temporary_name,
                name,
                src_dir_fd=parent,
                dst_dir_fd=parent,
                follow_symlinks=False,
            )
        except FileExistsError:
            metadata = os.stat(name, dir_fd=parent, follow_symlinks=False)
            if not stat.S_ISREG(metadata.st_mode):
                raise ValueError(
                    f"unsafe {label} target: expected a regular file"
                )
            try:
                existing_descriptor = os.open(name, _FILE_FLAGS, dir_fd=parent)
            except OSError as exc:
                if exc.errno in {errno.ELOOP, errno.ENOTDIR}:
                    raise ValueError(
                        f"unsafe {label} target: expected a regular file"
                    ) from exc
                raise
            try:
                if not stat.S_ISREG(os.fstat(existing_descriptor).st_mode):
                    raise ValueError(
                        f"unsafe {label} target: expected a regular file"
                    )
                with os.fdopen(existing_descriptor, "rb", closefd=False) as handle:
                    existing_content = handle.read()
            finally:
                os.close(existing_descriptor)
            if existing_content != content:
                raise ValueError(f"refusing to overwrite a different {label}")
        os.fsync(parent)
        return absolute
    finally:
        if temporary_descriptor is not None:
            os.close(temporary_descriptor)
        if temporary_created:
            try:
                os.unlink(temporary_name, dir_fd=parent)
            except FileNotFoundError:
                pass
        os.close(parent)
