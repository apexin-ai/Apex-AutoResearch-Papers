from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from .contract_compatibility import alebench_capability, edgebench_capability
from .solutions import SolutionArtifact, SolutionContractError


_SHA256 = re.compile(r"[0-9a-f]{64}")
_WINDOWS_DRIVE = re.compile(r"[A-Za-z]:")
_EDGE_FIELDS = {"schema_version", "files"}
_EDGE_FILE_FIELDS = {"path", "type", "content"}
_ALE_LANGUAGES = {
    "cpp": ("cpp", ".cpp"),
    "cpp17": ("cpp17", ".cpp"),
    "cpp20": ("cpp20", ".cpp"),
    "cpp23": ("cpp23", ".cpp"),
    "python": ("python", ".py"),
    "py": ("python", ".py"),
    "rust": ("rust", ".rs"),
}
_ALE_FENCE = re.compile(
    r"```(?P<label>[a-z0-9]+)[ \t]*\r?\n(?P<source>.*?)```\r?\n?",
    re.DOTALL,
)


def _canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _summary_sha(summary: dict[str, Any]) -> str:
    return hashlib.sha256(_canonical_bytes(summary)).hexdigest()


def _positive_limit(value: int, label: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(f"{label} must be a positive integer")
    return value


def _safe_bundle_path(value: object, *, label: str = "bundle path") -> str:
    if not isinstance(value, str) or not value:
        raise SolutionContractError(f"{label} is invalid")
    if (
        value.startswith("/")
        or value.startswith("//")
        or value.startswith("\\\\")
        or _WINDOWS_DRIVE.match(value)
        or "\\" in value
    ):
        raise SolutionContractError(f"{label} must be a relative POSIX path")
    components = value.split("/")
    if any(component in {"", ".", ".."} for component in components):
        raise SolutionContractError(f"{label} contains an invalid path component")
    return value


def _strict_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise SolutionContractError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_json_constant(value: str) -> None:
    raise SolutionContractError(f"invalid JSON constant: {value}")


class EdgeBenchBundleCodec:
    """Parse one complete EdgeBench file-bundle response without writing files."""

    output_mode = "plain_text"

    def __init__(
        self,
        *,
        required_submit_path: str = "solution.py",
        max_files: int = 64,
        max_file_bytes: int = 1_000_000,
        max_total_bytes: int = 2_000_000,
        max_response_bytes: int = 4_000_000,
    ) -> None:
        self.required_submit_path = _safe_bundle_path(
            required_submit_path, label="required submit path"
        )
        self.capability_card = edgebench_capability(self.required_submit_path)
        self.max_files = _positive_limit(max_files, "max files")
        self.max_file_bytes = _positive_limit(max_file_bytes, "max file bytes")
        self.max_total_bytes = _positive_limit(max_total_bytes, "max total bytes")
        self.max_response_bytes = _positive_limit(
            max_response_bytes, "max response bytes"
        )

    def parse(self, raw_response: str) -> SolutionArtifact:
        if not isinstance(raw_response, str):
            raise SolutionContractError("EdgeBench response must be text")
        if len(raw_response.encode("utf-8")) > self.max_response_bytes:
            raise SolutionContractError("EdgeBench response size exceeds the limit")
        try:
            payload = json.loads(
                raw_response,
                object_pairs_hook=_strict_object,
                parse_constant=_reject_json_constant,
            )
        except SolutionContractError:
            raise
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise SolutionContractError(
                "EdgeBench response must be one complete JSON value"
            ) from exc
        if not isinstance(payload, dict) or set(payload) != _EDGE_FIELDS:
            raise SolutionContractError("EdgeBench bundle fields differ")
        if type(payload["schema_version"]) is not int or payload["schema_version"] != 1:
            raise SolutionContractError("EdgeBench bundle schema version differs")
        raw_files = payload["files"]
        if (
            not isinstance(raw_files, list)
            or not raw_files
            or len(raw_files) > self.max_files
        ):
            raise SolutionContractError("EdgeBench bundle file count is invalid")

        normalized_files: list[dict[str, str]] = []
        seen: set[str] = set()
        seen_casefolded: set[str] = set()
        total_bytes = 0
        for raw_file in raw_files:
            if not isinstance(raw_file, dict) or set(raw_file) != _EDGE_FILE_FIELDS:
                raise SolutionContractError("EdgeBench file fields differ")
            path = _safe_bundle_path(raw_file["path"])
            if path in seen:
                raise SolutionContractError("EdgeBench bundle has a duplicate path")
            casefolded_path = path.casefold()
            if casefolded_path in seen_casefolded:
                raise SolutionContractError("EdgeBench bundle paths conflict")
            if raw_file["type"] != "file":
                raise SolutionContractError("EdgeBench bundle file type must be file")
            content = raw_file["content"]
            if not isinstance(content, str):
                raise SolutionContractError("EdgeBench file content must be text")
            content = content.replace("\r\n", "\n")
            byte_length = len(content.encode("utf-8"))
            if byte_length > self.max_file_bytes:
                raise SolutionContractError("EdgeBench file size exceeds the limit")
            total_bytes += byte_length
            if total_bytes > self.max_total_bytes:
                raise SolutionContractError("EdgeBench total size exceeds the limit")
            seen.add(path)
            seen_casefolded.add(casefolded_path)
            normalized_files.append(
                {"path": path, "type": "file", "content": content}
            )

        if self.required_submit_path not in seen:
            raise SolutionContractError(
                f"EdgeBench bundle is missing required submit path: "
                f"{self.required_submit_path}"
            )
        for path in seen_casefolded:
            components = path.split("/")
            if any(
                "/".join(components[:index]) in seen_casefolded
                for index in range(1, len(components))
            ):
                raise SolutionContractError("EdgeBench bundle paths conflict")

        normalized_files.sort(key=lambda item: item["path"])
        canonical = _canonical_bytes(
            {"schema_version": 1, "files": normalized_files}
        )
        summary = {
            "schema_version": 1,
            "file_count": len(normalized_files),
            "paths": [item["path"] for item in normalized_files],
            "extensions": [
                PurePosixPath(item["path"]).suffix for item in normalized_files
            ],
            "byte_lengths": [
                len(item["content"].encode("utf-8")) for item in normalized_files
            ],
            "content_sha256s": [
                hashlib.sha256(item["content"].encode("utf-8")).hexdigest()
                for item in normalized_files
            ],
        }
        return SolutionArtifact(
            raw_response=raw_response,
            text=canonical.decode("utf-8"),
            sha256=hashlib.sha256(canonical).hexdigest(),
            structural_signature=_summary_sha(summary),
            extension=".json",
            artifact_kind="edgebench_file_bundle_v1",
            compatibility_trace=summary,
        )


class ALEBenchCodeCodec:
    """Parse one complete ALE-Bench fenced source-code response."""

    output_mode = "plain_text"

    def __init__(self, *, max_source_bytes: int = 1_000_000) -> None:
        self.max_source_bytes = _positive_limit(
            max_source_bytes, "max source bytes"
        )
        self.capability_card = alebench_capability()

    def parse(self, raw_response: str) -> SolutionArtifact:
        if not isinstance(raw_response, str):
            raise SolutionContractError("ALE-Bench response must be text")
        match = _ALE_FENCE.fullmatch(raw_response)
        if match is None or "```" in (match.group("source") if match else ""):
            raise SolutionContractError(
                "ALE-Bench response must be exactly one fenced source file"
            )
        label = match.group("label")
        language = _ALE_LANGUAGES.get(label)
        if language is None:
            raise SolutionContractError("ALE-Bench language label is unsupported")
        source = match.group("source").replace("\r\n", "\n").rstrip("\n") + "\n"
        if source == "\n":
            raise SolutionContractError("ALE-Bench source is empty")
        encoded = source.encode("utf-8")
        if len(encoded) > self.max_source_bytes:
            raise SolutionContractError("ALE-Bench source size exceeds the limit")
        canonical_language, extension = language
        sha256 = hashlib.sha256(encoded).hexdigest()
        summary = {
            "schema_version": 1,
            "language": canonical_language,
            "byte_length": len(encoded),
            "source_sha256": sha256,
        }
        return SolutionArtifact(
            raw_response=raw_response,
            text=source,
            sha256=sha256,
            structural_signature=_summary_sha(summary),
            extension=extension,
            artifact_kind=f"alebench_source_{canonical_language}",
            compatibility_trace=summary,
        )


@dataclass(frozen=True)
class ArchivedOfficialSolution:
    artifact_sha256: str
    artifact_path: Path
    receipt_path: Path


def _write_once(path: Path, content: bytes, *, label: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    try:
        descriptor = os.open(path, flags, 0o600)
    except FileExistsError:
        try:
            existing = path.read_bytes()
        except OSError as exc:
            raise ValueError(f"{label} content-address collision") from exc
        if existing != content:
            raise ValueError(f"{label} content-address collision")
        return path
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    except Exception:
        path.unlink(missing_ok=True)
        raise
    return path


class OfficialSolutionArchive:
    """Write-once content-addressed archive for official benchmark candidates."""

    def __init__(self, root: Path) -> None:
        self.root = Path(root).resolve()

    def store(self, artifact: SolutionArtifact) -> ArchivedOfficialSolution:
        encoded = self._validated_artifact_bytes(artifact)
        artifact_path = (
            self.root / "artifacts" / f"{artifact.sha256}{artifact.extension}"
        )
        receipt_path = self.root / "receipts" / f"{artifact.sha256}.json"
        receipt = {
            "schema_version": 1,
            "artifact_kind": artifact.artifact_kind,
            "artifact_sha256": artifact.sha256,
            "structural_signature": artifact.structural_signature,
            "extension": artifact.extension,
            "byte_length": len(encoded),
            "structural_summary": artifact.compatibility_trace,
        }
        try:
            _write_once(
                artifact_path,
                encoded,
                label="official solution artifact",
            )
            _write_once(
                receipt_path,
                _canonical_bytes(receipt),
                label="official solution receipt",
            )
        except ValueError as exc:
            if "content-address collision" in str(exc):
                raise ValueError("official solution content-address collision") from exc
            raise
        return ArchivedOfficialSolution(
            artifact_sha256=artifact.sha256,
            artifact_path=artifact_path,
            receipt_path=receipt_path,
        )

    def materialize_edge_bundle(
        self, artifact_sha256: str, attempt_root: Path
    ) -> Path:
        if not isinstance(artifact_sha256, str) or not _SHA256.fullmatch(
            artifact_sha256
        ):
            raise ValueError("invalid official solution sha256")
        root = Path(attempt_root).resolve()
        if os.path.lexists(root):
            raise ValueError("EdgeBench attempt root already exists")

        receipt_path = self.root / "receipts" / f"{artifact_sha256}.json"
        try:
            receipt_bytes = receipt_path.read_bytes()
            receipt = json.loads(receipt_bytes)
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise ValueError("official solution receipt is unavailable") from exc
        expected_receipt_fields = {
            "schema_version",
            "artifact_kind",
            "artifact_sha256",
            "structural_signature",
            "extension",
            "byte_length",
            "structural_summary",
        }
        if (
            not isinstance(receipt, dict)
            or set(receipt) != expected_receipt_fields
            or type(receipt.get("schema_version")) is not int
            or receipt.get("schema_version") != 1
            or receipt.get("artifact_kind") != "edgebench_file_bundle_v1"
            or receipt.get("artifact_sha256") != artifact_sha256
            or receipt.get("extension") != ".json"
            or _canonical_bytes(receipt) != receipt_bytes
        ):
            raise ValueError("official EdgeBench receipt differs")

        artifact_path = self.root / "artifacts" / f"{artifact_sha256}.json"
        try:
            artifact_bytes = artifact_path.read_bytes()
        except OSError as exc:
            raise ValueError("official EdgeBench artifact is unavailable") from exc
        if (
            hashlib.sha256(artifact_bytes).hexdigest() != artifact_sha256
            or len(artifact_bytes) != receipt["byte_length"]
        ):
            raise ValueError("official EdgeBench artifact hash differs")
        try:
            canonical_artifact = EdgeBenchBundleCodec().parse(
                artifact_bytes.decode("utf-8")
            )
        except (UnicodeError, SolutionContractError) as exc:
            raise ValueError("official EdgeBench artifact is invalid") from exc
        if (
            canonical_artifact.text.encode("utf-8") != artifact_bytes
            or canonical_artifact.structural_signature
            != receipt["structural_signature"]
            or canonical_artifact.compatibility_trace
            != receipt["structural_summary"]
        ):
            raise ValueError("official EdgeBench artifact receipt binding differs")

        payload = json.loads(artifact_bytes)
        root.parent.mkdir(parents=True, exist_ok=True)
        staging_root = Path(
            tempfile.mkdtemp(prefix=f".{root.name}.", dir=root.parent)
        )
        published = False
        try:
            for item in payload["files"]:
                destination = staging_root.joinpath(*item["path"].split("/"))
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open("xb") as handle:
                    handle.write(item["content"].encode("utf-8"))
            if os.path.lexists(root):
                raise ValueError("EdgeBench attempt root already exists")
            staging_root.rename(root)
            published = True
        finally:
            if not published:
                shutil.rmtree(staging_root, ignore_errors=True)
        return root

    @staticmethod
    def _validated_artifact_bytes(artifact: SolutionArtifact) -> bytes:
        if not isinstance(artifact, SolutionArtifact):
            raise TypeError("official solution archive requires a SolutionArtifact")
        encoded = artifact.text.encode("utf-8")
        if (
            not _SHA256.fullmatch(artifact.sha256)
            or hashlib.sha256(encoded).hexdigest() != artifact.sha256
            or not isinstance(artifact.compatibility_trace, dict)
            or _summary_sha(artifact.compatibility_trace)
            != artifact.structural_signature
        ):
            raise ValueError("official solution artifact binding differs")
        expected_extension: str | None = None
        codec: EdgeBenchBundleCodec | ALEBenchCodeCodec | None = None
        canonical_response: str | None = None
        if artifact.artifact_kind == "edgebench_file_bundle_v1":
            expected_extension = ".json"
            codec = EdgeBenchBundleCodec()
            canonical_response = artifact.text
        elif artifact.artifact_kind in {
            "alebench_source_cpp",
            "alebench_source_cpp17",
            "alebench_source_cpp20",
            "alebench_source_cpp23",
        }:
            expected_extension = ".cpp"
            language = artifact.artifact_kind.removeprefix("alebench_source_")
            codec = ALEBenchCodeCodec()
            canonical_response = f"```{language}\n{artifact.text}```"
        elif artifact.artifact_kind == "alebench_source_python":
            expected_extension = ".py"
            codec = ALEBenchCodeCodec()
            canonical_response = f"```python\n{artifact.text}```"
        elif artifact.artifact_kind == "alebench_source_rust":
            expected_extension = ".rs"
            codec = ALEBenchCodeCodec()
            canonical_response = f"```rust\n{artifact.text}```"
        if (
            expected_extension is None
            or codec is None
            or canonical_response is None
            or artifact.extension != expected_extension
        ):
            raise ValueError("unsupported official solution artifact kind")

        try:
            canonical = codec.parse(canonical_response)
        except SolutionContractError as exc:
            raise ValueError("official solution artifact is not canonical") from exc
        if (
            canonical.text != artifact.text
            or canonical.sha256 != artifact.sha256
            or canonical.extension != artifact.extension
            or canonical.artifact_kind != artifact.artifact_kind
        ):
            raise ValueError("official solution artifact is not canonical")
        if (
            canonical.compatibility_trace != artifact.compatibility_trace
            or canonical.structural_signature != artifact.structural_signature
        ):
            raise ValueError("official solution structural summary differs")

        try:
            parsed_raw = codec.parse(artifact.raw_response)
        except SolutionContractError as exc:
            raise ValueError("official solution raw response binding differs") from exc
        if (
            parsed_raw.text != artifact.text
            or parsed_raw.sha256 != artifact.sha256
            or parsed_raw.structural_signature != artifact.structural_signature
            or parsed_raw.extension != artifact.extension
            or parsed_raw.artifact_kind != artifact.artifact_kind
            or parsed_raw.compatibility_trace != artifact.compatibility_trace
        ):
            raise ValueError("official solution raw response binding differs")
        return encoded
