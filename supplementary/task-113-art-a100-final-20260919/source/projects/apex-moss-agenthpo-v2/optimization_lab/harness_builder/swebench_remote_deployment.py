"""Content-addressed evidence for the remote SWE-bench deployment.

This module is deliberately outside the evaluator path.  It performs one
read-only SSH probe, starts no model or evaluator operation, and seals the
observed deployment identity into an immutable content-addressed receipt.
The probe verifies every Git-tracked path from the clean local Moss revision,
not merely the revision-shaped name of the remote directory.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shlex
import stat
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Mapping, Sequence

from .adapters.swebench_verified_worker import SWEBENCH_SOURCE_COMMIT
from .three_arm_prepare import resolve_clean_revision


REMOTE_DEPLOYMENT_KIND = "swebench_remote_deployment_receipt"
REMOTE_DEPLOYMENT_SCHEMA_VERSION = 1
SWEBENCH_WORKER_RELATIVE_PATH = (
    "optimization_lab/harness_builder/adapters/swebench_verified_worker.py"
)

_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_SHA1 = re.compile(r"[0-9a-f]{40}\Z")
_HOST_ALIAS = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}\Z")
_TRACKED_PATH = re.compile(r"[A-Za-z0-9._/@+ -]+\Z")
_MAX_RECEIPT_BYTES = 1024 * 1024
_RECEIPT_FIELDS = {
    "schema_version",
    "kind",
    "host_alias",
    "observed_remote_hostname",
    "remote_project_root",
    "remote_swebench_source_root",
    "moss_clean_revision",
    "moss_git_tree_sha1",
    "moss_tracked_manifest_sha256",
    "moss_tracked_file_count",
    "worker_relative_path",
    "worker_sha256",
    "swebench_source_commit",
    "swebench_source_clean",
    "remote_python",
    "probe_protocol_sha256",
    "model_calls_started",
    "evaluator_transactions_started",
}
_PYTHON_IDENTITY_FIELDS = {
    "requested_path",
    "sys_executable",
    "real_executable",
    "executable_sha256",
    "implementation",
    "python_version",
    "version_info",
    "cache_tag",
    "prefix",
    "base_prefix",
    "byteorder",
}
_PROBE_RESPONSE_FIELDS = {
    "schema_version",
    "kind",
    "remote_hostname",
    "remote_project_root",
    "remote_swebench_source_root",
    "moss_tracked_manifest_sha256",
    "moss_tracked_file_count",
    "worker_sha256",
    "swebench_source_commit",
    "swebench_source_clean",
    "remote_python",
}


def _canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            allow_nan=False,
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _strict_json(raw: bytes, *, label: str) -> dict[str, Any]:
    if not raw or len(raw) > _MAX_RECEIPT_BYTES:
        raise ValueError(f"{label} size differs")

    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"{label} contains a duplicate key")
            result[key] = value
        return result

    try:
        payload = json.loads(raw.decode("utf-8"), object_pairs_hook=unique)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} is not strict UTF-8 JSON") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{label} must be one object")
    return payload


def _absolute_remote_path(value: str, *, label: str) -> str:
    if (
        not isinstance(value, str)
        or not value.startswith("/")
        or value == "/"
        or value.endswith("/")
        or "//" in value
        or any(ord(character) < 32 or character.isspace() for character in value)
        or any(part in {"", ".", ".."} for part in value.split("/")[1:])
    ):
        raise ValueError(f"{label} is not a normalized absolute path")
    return value


def _git(
    project_root: Path,
    arguments: Sequence[str],
    *,
    binary: bool = False,
) -> bytes | str:
    process = subprocess.run(
        ["git", *arguments],
        cwd=project_root,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=not binary,
        check=False,
        timeout=60,
    )
    if process.returncode != 0:
        raise ValueError("unable to inspect the clean Moss revision")
    return process.stdout


def _tracked_manifest(
    project_root: Path,
    revision: str,
) -> tuple[list[dict[str, str]], str, str]:
    raw = _git(
        project_root,
        ["ls-tree", "-r", "-z", "--full-tree", revision],
        binary=True,
    )
    assert isinstance(raw, bytes)
    entries: list[dict[str, str]] = []
    seen: set[str] = set()
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            metadata, path_raw = record.split(b"\t", 1)
            mode_raw, object_type, object_id_raw = metadata.split(b" ", 2)
            path = path_raw.decode("utf-8")
            mode = mode_raw.decode("ascii")
            object_id = object_id_raw.decode("ascii")
        except (UnicodeDecodeError, ValueError) as exc:
            raise ValueError("Moss Git tree contains an unsupported entry") from exc
        if (
            object_type != b"blob"
            or mode not in {"100644", "100755", "120000"}
            or _SHA1.fullmatch(object_id) is None
            or _TRACKED_PATH.fullmatch(path) is None
            or path.startswith("/")
            or "//" in path
            or any(part in {"", ".", ".."} for part in path.split("/"))
            or path in seen
        ):
            raise ValueError("Moss Git tree contains an unsupported entry")
        seen.add(path)
        entries.append({"mode": mode, "oid": object_id, "path": path})
    if not entries:
        raise ValueError("Moss Git tree is empty")
    entries.sort(key=lambda item: item["path"])
    if SWEBENCH_WORKER_RELATIVE_PATH not in seen:
        raise ValueError("SWE-bench worker is not tracked by the Moss revision")
    manifest_sha256 = _sha256(_canonical_bytes(entries))
    tree = _git(project_root, ["rev-parse", f"{revision}^{{tree}}"])
    assert isinstance(tree, str)
    tree_sha1 = tree.strip()
    if _SHA1.fullmatch(tree_sha1) is None:
        raise ValueError("Moss Git tree object differs")
    return entries, manifest_sha256, tree_sha1


def _git_blob_bytes(project_root: Path, revision: str, relative_path: str) -> bytes:
    raw = _git(
        project_root,
        ["show", f"{revision}:{relative_path}"],
        binary=True,
    )
    assert isinstance(raw, bytes)
    return raw


# The script is sent as the argument to ``python -I -c`` and receives only a
# canonical public manifest on stdin.  It neither imports Moss nor starts the
# official SWE-bench harness, so it cannot consume a formal evaluator seat.
_REMOTE_PROBE_SCRIPT = r'''
import hashlib
import json
import os
import platform
import socket
import stat
import subprocess
import sys

def canonical(value):
    return (json.dumps(value, allow_nan=False, ensure_ascii=True,
                       separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")

def git_blob_oid(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()

request = json.load(sys.stdin)
required = {"schema_version", "kind", "remote_project_root",
            "remote_swebench_source_root", "remote_python", "swebench_source_commit",
            "moss_clean_revision", "moss_tracked_manifest_sha256", "tracked_entries",
            "worker_relative_path"}
if not isinstance(request, dict) or set(request) != required:
    raise SystemExit("probe request schema differs")
if request["schema_version"] != 1 or request["kind"] != "swebench_remote_deployment_probe":
    raise SystemExit("probe request identity differs")
root = request["remote_project_root"]
swe_root = request["remote_swebench_source_root"]
if (os.path.realpath(root) != root or not os.path.isdir(root)
        or os.path.realpath(swe_root) != swe_root or not os.path.isdir(swe_root)):
    raise SystemExit("remote roots are missing, relative, or symlinked")
entries = request["tracked_entries"]
if (not isinstance(entries, list) or not entries
        or hashlib.sha256(canonical(entries)).hexdigest()
        != request["moss_tracked_manifest_sha256"]):
    raise SystemExit("tracked manifest differs")
seen = set()
worker_sha256 = None
for item in entries:
    if not isinstance(item, dict) or set(item) != {"mode", "oid", "path"}:
        raise SystemExit("tracked entry schema differs")
    mode, expected_oid, relative = item["mode"], item["oid"], item["path"]
    if (mode not in {"100644", "100755", "120000"}
            or not isinstance(relative, str) or relative in seen
            or relative.startswith("/") or "//" in relative
            or any(part in {"", ".", ".."} for part in relative.split("/"))):
        raise SystemExit("tracked entry differs")
    seen.add(relative)
    target = os.path.join(root, *relative.split("/"))
    parent = os.path.dirname(target)
    if os.path.realpath(parent) != parent:
        raise SystemExit("tracked entry parent traverses a symlink")
    metadata = os.lstat(target)
    if mode == "120000":
        if not stat.S_ISLNK(metadata.st_mode):
            raise SystemExit("tracked symlink mode differs")
        raw = os.readlink(target).encode("utf-8")
    else:
        if not stat.S_ISREG(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
            raise SystemExit("tracked file mode differs")
        executable = bool(metadata.st_mode & 0o111)
        if executable != (mode == "100755"):
            raise SystemExit("tracked executable bit differs")
        with open(target, "rb") as stream:
            raw = stream.read()
    if git_blob_oid(raw) != expected_oid:
        raise SystemExit("tracked Git blob differs")
    if relative == request["worker_relative_path"]:
        if mode == "120000":
            raise SystemExit("SWE-bench worker cannot be a symlink")
        worker_sha256 = hashlib.sha256(raw).hexdigest()
if worker_sha256 is None:
    raise SystemExit("SWE-bench worker is absent")

revision = subprocess.run(
    ["git", "-C", swe_root, "rev-parse", "HEAD"],
    stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    text=True, timeout=30, check=False,
)
status = subprocess.run(
    ["git", "-C", swe_root, "status", "--porcelain", "--untracked-files=no"],
    stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    text=True, timeout=30, check=False,
)
swe_commit = revision.stdout.strip()
swe_clean = status.returncode == 0 and status.stdout == ""
if (revision.returncode != 0 or swe_commit != request["swebench_source_commit"]
        or not swe_clean):
    raise SystemExit("SWE-bench source revision differs or is dirty")

requested_python = request["remote_python"]
sys_executable = os.path.abspath(sys.executable)
if sys_executable != requested_python:
    raise SystemExit("remote Python executable path differs")
real_executable = os.path.realpath(sys_executable)
with open(real_executable, "rb") as stream:
    executable_sha256 = hashlib.sha256(stream.read()).hexdigest()
python_identity = {
    "requested_path": requested_python,
    "sys_executable": sys_executable,
    "real_executable": real_executable,
    "executable_sha256": executable_sha256,
    "implementation": sys.implementation.name,
    "python_version": platform.python_version(),
    "version_info": list(sys.version_info),
    "cache_tag": sys.implementation.cache_tag,
    "prefix": os.path.abspath(sys.prefix),
    "base_prefix": os.path.abspath(sys.base_prefix),
    "byteorder": sys.byteorder,
}
response = {
    "schema_version": 1,
    "kind": "swebench_remote_deployment_probe_result",
    "remote_hostname": socket.gethostname(),
    "remote_project_root": root,
    "remote_swebench_source_root": swe_root,
    "moss_tracked_manifest_sha256": request["moss_tracked_manifest_sha256"],
    "moss_tracked_file_count": len(entries),
    "worker_sha256": worker_sha256,
    "swebench_source_commit": swe_commit,
    "swebench_source_clean": swe_clean,
    "remote_python": python_identity,
}
sys.stdout.buffer.write(canonical(response))
'''.strip()

REMOTE_DEPLOYMENT_PROBE_PROTOCOL_SHA256 = _sha256(
    _REMOTE_PROBE_SCRIPT.encode("utf-8")
)


def _probe_request(
    *,
    entries: Sequence[Mapping[str, str]],
    manifest_sha256: str,
    revision: str,
    remote_project_root: str,
    remote_python: str,
    remote_swebench_source_root: str,
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "kind": "swebench_remote_deployment_probe",
        "remote_project_root": remote_project_root,
        "remote_swebench_source_root": remote_swebench_source_root,
        "remote_python": remote_python,
        "swebench_source_commit": SWEBENCH_SOURCE_COMMIT,
        "moss_clean_revision": revision,
        "moss_tracked_manifest_sha256": manifest_sha256,
        "tracked_entries": list(entries),
        "worker_relative_path": SWEBENCH_WORKER_RELATIVE_PATH,
    }


def _run_remote_probe(
    *,
    host_alias: str,
    remote_python: str,
    request: Mapping[str, object],
    ssh_executable: str,
) -> dict[str, Any]:
    remote_command = shlex.join(
        [remote_python, "-I", "-c", _REMOTE_PROBE_SCRIPT]
    )
    process = subprocess.run(
        [
            ssh_executable,
            "-o",
            "BatchMode=yes",
            "-o",
            "ConnectTimeout=15",
            "--",
            host_alias,
            remote_command,
        ],
        input=_canonical_bytes(request),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=180,
    )
    if process.returncode != 0:
        summary = process.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            "remote SWE-bench deployment probe failed"
            + (f": {summary[:500]}" if summary else "")
        )
    response = _strict_json(
        process.stdout, label="remote deployment probe response"
    )
    if _canonical_bytes(response) != process.stdout:
        raise ValueError("remote deployment probe response is not canonical")
    return response


def _validate_python_identity(identity: object, *, remote_python: str) -> None:
    if not isinstance(identity, dict) or set(identity) != _PYTHON_IDENTITY_FIELDS:
        raise ValueError("remote Python identity schema differs")
    paths = (
        identity.get("requested_path"),
        identity.get("sys_executable"),
        identity.get("real_executable"),
        identity.get("prefix"),
        identity.get("base_prefix"),
    )
    if (
        identity.get("requested_path") != remote_python
        or identity.get("sys_executable") != remote_python
        or any(
            not isinstance(value, str)
            or not value.startswith("/")
            or any(ord(character) < 32 for character in value)
            for value in paths
        )
        or not isinstance(identity.get("implementation"), str)
        or not identity["implementation"]
        or not isinstance(identity.get("python_version"), str)
        or re.fullmatch(r"\d+\.\d+\.\d+", identity["python_version"]) is None
        or not isinstance(identity.get("version_info"), list)
        or len(identity["version_info"]) != 5
        or not all(
            isinstance(value, int) and not isinstance(value, bool)
            for value in identity["version_info"][:3]
        )
        or not isinstance(identity["version_info"][3], str)
        or not isinstance(identity["version_info"][4], int)
        or not isinstance(identity.get("cache_tag"), str)
        or not identity["cache_tag"]
        or identity.get("byteorder") not in {"little", "big"}
        or not isinstance(identity.get("executable_sha256"), str)
        or _SHA256.fullmatch(identity["executable_sha256"]) is None
    ):
        raise ValueError("remote Python identity differs")


def _validate_probe_response(
    response: Mapping[str, Any],
    *,
    remote_project_root: str,
    remote_python: str,
    remote_swebench_source_root: str,
    manifest_sha256: str,
    tracked_file_count: int,
    worker_sha256: str,
) -> None:
    if (
        not isinstance(response, dict)
        or set(response) != _PROBE_RESPONSE_FIELDS
        or type(response.get("schema_version")) is not int
        or response["schema_version"] != 1
        or response.get("kind") != "swebench_remote_deployment_probe_result"
        or not isinstance(response.get("remote_hostname"), str)
        or not response["remote_hostname"]
        or any(ord(character) < 32 for character in response["remote_hostname"])
        or response.get("remote_project_root") != remote_project_root
        or response.get("remote_swebench_source_root")
        != remote_swebench_source_root
        or response.get("moss_tracked_manifest_sha256") != manifest_sha256
        or type(response.get("moss_tracked_file_count")) is not int
        or response["moss_tracked_file_count"] != tracked_file_count
        or response.get("worker_sha256") != worker_sha256
        or response.get("swebench_source_commit") != SWEBENCH_SOURCE_COMMIT
        or response.get("swebench_source_clean") is not True
    ):
        raise ValueError("remote SWE-bench deployment binding differs")
    _validate_python_identity(response.get("remote_python"), remote_python=remote_python)


def _content_addressed_write(output_root: Path, raw: bytes) -> Path:
    unresolved_root = Path(output_root)
    if unresolved_root.is_symlink():
        raise ValueError("remote deployment receipt root is unsafe")
    output_root = unresolved_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    if output_root.is_symlink() or not output_root.is_dir():
        raise ValueError("remote deployment receipt root is unsafe")
    digest = _sha256(raw)
    path = output_root / f"{digest}.json"
    if path.exists() or path.is_symlink():
        if path.is_symlink() or not path.is_file() or path.read_bytes() != raw:
            raise ValueError("remote deployment receipt path is already rebound")
        return path
    descriptor, name = tempfile.mkstemp(
        prefix=".remote-deployment-", suffix=".tmp", dir=output_root
    )
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, 0o444)
        os.replace(temporary, path)
        directory = os.open(output_root, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return path


def _local_deployment_contract(
    *,
    project_root: Path,
    expected_code_revision: str,
) -> tuple[list[dict[str, str]], str, str, str]:
    project_root = project_root.resolve(strict=True)
    observed_revision = resolve_clean_revision(project_root)
    if observed_revision != expected_code_revision:
        raise ValueError("remote deployment expected code revision differs")
    entries, manifest_sha256, tree_sha1 = _tracked_manifest(
        project_root, observed_revision
    )
    worker_sha256 = _sha256(
        _git_blob_bytes(
            project_root,
            observed_revision,
            SWEBENCH_WORKER_RELATIVE_PATH,
        )
    )
    return entries, manifest_sha256, tree_sha1, worker_sha256


def prepare_swebench_remote_deployment_receipt(
    *,
    project_root: Path,
    output_root: Path,
    expected_code_revision: str,
    host_alias: str,
    remote_project_root: str,
    remote_python: str,
    remote_swebench_source_root: str,
    ssh_executable: str = "ssh",
) -> Path:
    """Probe and seal one immutable deployment receipt.

    The operation is read-only and has no model/evaluator authority.
    """

    if _SHA1.fullmatch(expected_code_revision) is None:
        raise ValueError("remote deployment requires a full Moss revision")
    if _HOST_ALIAS.fullmatch(host_alias) is None:
        raise ValueError("remote deployment host alias differs")
    remote_project_root = _absolute_remote_path(
        remote_project_root, label="remote Moss project root"
    )
    remote_python = _absolute_remote_path(remote_python, label="remote Python")
    remote_swebench_source_root = _absolute_remote_path(
        remote_swebench_source_root, label="remote SWE-bench source root"
    )
    entries, manifest_sha256, tree_sha1, worker_sha256 = (
        _local_deployment_contract(
            project_root=project_root,
            expected_code_revision=expected_code_revision,
        )
    )
    request = _probe_request(
        entries=entries,
        manifest_sha256=manifest_sha256,
        revision=expected_code_revision,
        remote_project_root=remote_project_root,
        remote_python=remote_python,
        remote_swebench_source_root=remote_swebench_source_root,
    )
    response = _run_remote_probe(
        host_alias=host_alias,
        remote_python=remote_python,
        request=request,
        ssh_executable=ssh_executable,
    )
    _validate_probe_response(
        response,
        remote_project_root=remote_project_root,
        remote_python=remote_python,
        remote_swebench_source_root=remote_swebench_source_root,
        manifest_sha256=manifest_sha256,
        tracked_file_count=len(entries),
        worker_sha256=worker_sha256,
    )
    receipt = {
        "schema_version": REMOTE_DEPLOYMENT_SCHEMA_VERSION,
        "kind": REMOTE_DEPLOYMENT_KIND,
        "host_alias": host_alias,
        "observed_remote_hostname": response["remote_hostname"],
        "remote_project_root": remote_project_root,
        "remote_swebench_source_root": remote_swebench_source_root,
        "moss_clean_revision": expected_code_revision,
        "moss_git_tree_sha1": tree_sha1,
        "moss_tracked_manifest_sha256": manifest_sha256,
        "moss_tracked_file_count": len(entries),
        "worker_relative_path": SWEBENCH_WORKER_RELATIVE_PATH,
        "worker_sha256": worker_sha256,
        "swebench_source_commit": SWEBENCH_SOURCE_COMMIT,
        "swebench_source_clean": True,
        "remote_python": response["remote_python"],
        "probe_protocol_sha256": REMOTE_DEPLOYMENT_PROBE_PROTOCOL_SHA256,
        "model_calls_started": 0,
        "evaluator_transactions_started": 0,
    }
    return _content_addressed_write(output_root, _canonical_bytes(receipt))


def verify_swebench_remote_deployment_receipt(
    receipt_path: Path,
    *,
    project_root: Path,
    expected_code_revision: str,
    host_alias: str,
    remote_project_root: str,
    remote_python: str,
    remote_swebench_source_root: str,
    reprobe: bool = False,
    ssh_executable: str = "ssh",
) -> dict[str, Any]:
    """Verify a receipt, optionally re-running the same read-only probe."""

    unresolved_path = Path(receipt_path)
    metadata = unresolved_path.lstat()
    if unresolved_path.is_symlink() or not stat.S_ISREG(metadata.st_mode):
        raise ValueError("remote deployment receipt must be a regular file")
    path = unresolved_path.resolve(strict=True)
    raw = path.read_bytes()
    digest = _sha256(raw)
    if path.name != f"{digest}.json":
        raise ValueError("remote deployment receipt is not content-addressed")
    receipt = _strict_json(raw, label="remote deployment receipt")
    if _canonical_bytes(receipt) != raw:
        raise ValueError("remote deployment receipt is not canonical")
    if _SHA1.fullmatch(expected_code_revision) is None:
        raise ValueError("remote deployment requires a full Moss revision")
    if _HOST_ALIAS.fullmatch(host_alias) is None:
        raise ValueError("remote deployment host alias differs")
    remote_project_root = _absolute_remote_path(
        remote_project_root, label="remote Moss project root"
    )
    remote_python = _absolute_remote_path(remote_python, label="remote Python")
    remote_swebench_source_root = _absolute_remote_path(
        remote_swebench_source_root, label="remote SWE-bench source root"
    )
    entries, manifest_sha256, tree_sha1, worker_sha256 = (
        _local_deployment_contract(
            project_root=project_root,
            expected_code_revision=expected_code_revision,
        )
    )
    if (
        set(receipt) != _RECEIPT_FIELDS
        or type(receipt.get("schema_version")) is not int
        or receipt["schema_version"] != REMOTE_DEPLOYMENT_SCHEMA_VERSION
        or receipt.get("kind") != REMOTE_DEPLOYMENT_KIND
        or receipt.get("host_alias") != host_alias
        or receipt.get("remote_project_root") != remote_project_root
        or receipt.get("remote_swebench_source_root")
        != remote_swebench_source_root
        or receipt.get("moss_clean_revision") != expected_code_revision
        or receipt.get("moss_git_tree_sha1") != tree_sha1
        or receipt.get("moss_tracked_manifest_sha256") != manifest_sha256
        or type(receipt.get("moss_tracked_file_count")) is not int
        or receipt["moss_tracked_file_count"] != len(entries)
        or receipt.get("worker_relative_path") != SWEBENCH_WORKER_RELATIVE_PATH
        or receipt.get("worker_sha256") != worker_sha256
        or receipt.get("swebench_source_commit") != SWEBENCH_SOURCE_COMMIT
        or receipt.get("swebench_source_clean") is not True
        or receipt.get("probe_protocol_sha256")
        != REMOTE_DEPLOYMENT_PROBE_PROTOCOL_SHA256
        or type(receipt.get("model_calls_started")) is not int
        or receipt["model_calls_started"] != 0
        or type(receipt.get("evaluator_transactions_started")) is not int
        or receipt["evaluator_transactions_started"] != 0
        or not isinstance(receipt.get("observed_remote_hostname"), str)
        or not receipt["observed_remote_hostname"]
    ):
        raise ValueError("remote deployment receipt binding differs")
    _validate_python_identity(receipt.get("remote_python"), remote_python=remote_python)
    if reprobe:
        request = _probe_request(
            entries=entries,
            manifest_sha256=manifest_sha256,
            revision=expected_code_revision,
            remote_project_root=remote_project_root,
            remote_python=remote_python,
            remote_swebench_source_root=remote_swebench_source_root,
        )
        response = _run_remote_probe(
            host_alias=host_alias,
            remote_python=remote_python,
            request=request,
            ssh_executable=ssh_executable,
        )
        _validate_probe_response(
            response,
            remote_project_root=remote_project_root,
            remote_python=remote_python,
            remote_swebench_source_root=remote_swebench_source_root,
            manifest_sha256=manifest_sha256,
            tracked_file_count=len(entries),
            worker_sha256=worker_sha256,
        )
        if (
            response["remote_hostname"] != receipt["observed_remote_hostname"]
            or response["remote_python"] != receipt["remote_python"]
        ):
            raise ValueError("live remote deployment identity differs from its receipt")
    return receipt


__all__ = [
    "REMOTE_DEPLOYMENT_KIND",
    "REMOTE_DEPLOYMENT_PROBE_PROTOCOL_SHA256",
    "REMOTE_DEPLOYMENT_SCHEMA_VERSION",
    "SWEBENCH_WORKER_RELATIVE_PATH",
    "prepare_swebench_remote_deployment_receipt",
    "verify_swebench_remote_deployment_receipt",
]
