"""Source-locked task authority for the exact four-arm factorial matrix.

This module closes one narrow provenance gap: callers cannot choose the
``task_binding_sha256`` or ``context_binding_sha256`` stored in a
:class:`~optimization_lab.harness_builder.factorial_trunk.TaskSeedKey`.
Instead, a trusted controller opens the two pinned Git object databases,
derives a solver-visible task projection, requires the supplied v001
``HarnessContext`` to equal that projection, and creates all 126 keys itself.

The authority is deliberately zero-call and ephemeral.  It reads committed
Git objects only; it cannot invoke a model, benchmark process, evaluator, or
resource allocator.  Its receipts do not grant execution authority.  A formal
controller must instantiate it from the real pinned checkouts immediately
before constructing the exact zero-call plan.

GDPevo's solver projection is restricted to ``test_tasks/NNN/input`` and
explicitly excludes ``eval``, ``output``, ``notes``, and answer/gold artifacts.
Controller-private Git tree identities still bind the complete task group, so
an evaluator/environment change invalidates the key without exposing those
contents to the solver.  AgentHPOBench's room-selector task is represented as
an explicit free-form prompt task rather than pretending it has a discrete
hyperparameter space.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import stat
import string
import subprocess
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from .agenthpo_qualification import verify_agenthpo_qualification
from .factorial_contract import (
    factorial_main_matrix_projection,
    verify_factorial_contract,
)
from .factorial_trunk import TaskSeedKey
from .gdpevo_qualification import verify_gdpevo_qualification
from .operators import HarnessContext, TrustedOperatorRegistry


_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_GIT_OID = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_ZERO_SHA256 = "0" * 64
_MAX_GIT_OUTPUT_BYTES = 2 * 1024 * 1024
_MAX_PUBLIC_TASK_BYTES = 256 * 1024
_AGENTHPO_SPACE_PATH = "tasks/main/space_manifest.json"
_AGENTHPO_SCORING_PATH = "configs/scoring_reference.tsv"
_AGENTHPO_FREE_FORM_TASK = "agent_lightning_room_selector"
_GDPEVO_FORBIDDEN_COMPONENTS = frozenset(
    {"eval", "output", "notes", "answer.json", "scoring.json"}
)


class FactorialTaskAuthorityError(ValueError):
    """A source checkout, public task projection, or context has drifted."""


def _canonical_bytes(payload: object) -> bytes:
    try:
        return (
            json.dumps(
                payload,
                allow_nan=False,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeError) as exc:
        raise FactorialTaskAuthorityError(
            "task authority payload is not canonical JSON"
        ) from exc


def _canonical_text(payload: object) -> str:
    return _canonical_bytes(payload).decode("utf-8")


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _safe_id(value: object, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise FactorialTaskAuthorityError(f"unsafe {label}")
    return value


def _sha(value: object, label: str, *, allow_zero: bool = False) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise FactorialTaskAuthorityError(f"invalid {label}")
    if not allow_zero and value == _ZERO_SHA256:
        raise FactorialTaskAuthorityError(f"empty {label}")
    return value


def _git_oid(value: object, label: str) -> str:
    if not isinstance(value, str) or _GIT_OID.fullmatch(value) is None:
        raise FactorialTaskAuthorityError(f"invalid {label}")
    return value


def _strict_json(raw: bytes, *, label: str) -> Any:
    def reject_constant(value: str) -> None:
        raise FactorialTaskAuthorityError(f"{label} contains {value}")

    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise FactorialTaskAuthorityError(
                    f"{label} repeats field {key!r}"
                )
            result[key] = value
        return result

    try:
        return json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=reject_duplicates,
            parse_constant=reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FactorialTaskAuthorityError(f"{label} is not strict JSON") from exc


def _typed_public_scalar(value: object, *, label: str) -> object:
    if value is None or isinstance(value, (bool, str)):
        if isinstance(value, str) and (not value or "\x00" in value):
            raise FactorialTaskAuthorityError(f"{label} string is unsafe")
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float) and math.isfinite(value):
        return 0.0 if value == 0.0 else value
    raise FactorialTaskAuthorityError(f"{label} is not a JSON scalar")


def _same_typed_scalar(left: object, right: object) -> bool:
    return type(left) is type(right) and left == right


def _safe_source_root(value: str | Path, *, label: str) -> Path:
    root = Path(value)
    if not root.is_absolute():
        raise FactorialTaskAuthorityError(f"{label} must be absolute")
    try:
        resolved = root.resolve(strict=True)
    except OSError as exc:
        raise FactorialTaskAuthorityError(f"{label} does not resolve: {exc}") from exc
    if resolved != root or not root.is_dir():
        raise FactorialTaskAuthorityError(
            f"{label} must be its explicit real directory"
        )
    current = root
    while True:
        try:
            metadata = os.lstat(current)
        except OSError as exc:
            raise FactorialTaskAuthorityError(
                f"cannot inspect {label} path component: {exc}"
            ) from exc
        if stat.S_ISLNK(metadata.st_mode):
            raise FactorialTaskAuthorityError(f"{label} may not contain symlinks")
        if current.parent == current:
            break
        current = current.parent
    return root


@dataclass(frozen=True)
class _GitEntry:
    mode: str
    object_type: str
    oid: str
    path: str


class _PinnedGitCheckout:
    """Read exact committed objects while ignoring the mutable worktree."""

    def __init__(
        self,
        root: Path,
        *,
        expected_commit: str,
        expected_root_tree: str,
        label: str,
    ) -> None:
        self.root = _safe_source_root(root, label=label)
        self.label = label
        self._git_dir = self._resolve_git_dir()
        self.expected_commit = _git_oid(expected_commit, f"{label} commit")
        self.expected_root_tree = _git_oid(
            expected_root_tree, f"{label} root tree"
        )
        commit = self._text("rev-parse", "--verify", "HEAD^{commit}")
        if commit != self.expected_commit:
            raise FactorialTaskAuthorityError(f"{label} source commit drifted")
        tree = self._text(
            "rev-parse", "--verify", f"{self.expected_commit}^{{tree}}"
        )
        if tree != self.expected_root_tree:
            raise FactorialTaskAuthorityError(f"{label} source tree drifted")

    def _resolve_git_dir(self) -> Path:
        try:
            raw = subprocess.run(
                ["git", "-C", str(self.root), "rev-parse", "--absolute-git-dir"],
                check=False,
                capture_output=True,
                env=self._environment(),
                timeout=15,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise FactorialTaskAuthorityError(
                f"cannot locate {self.label} Git object database: {exc}"
            ) from exc
        if raw.returncode != 0:
            raise FactorialTaskAuthorityError(
                f"cannot locate {self.label} Git object database"
            )
        try:
            git_dir = Path(raw.stdout.decode("utf-8", errors="strict").strip())
            resolved = git_dir.resolve(strict=True)
        except (UnicodeDecodeError, OSError) as exc:
            raise FactorialTaskAuthorityError(
                f"{self.label} Git object database does not resolve"
            ) from exc
        if not resolved.is_dir():
            raise FactorialTaskAuthorityError(
                f"{self.label} Git object database is not a directory"
            )
        return resolved

    def _environment(self) -> dict[str, str]:
        environment = {
            key: value
            for key, value in os.environ.items()
            if not key.startswith("GIT_")
        }
        environment.update(
            {
                "GIT_CONFIG_GLOBAL": os.devnull,
                "GIT_CONFIG_NOSYSTEM": "1",
                "GIT_NO_REPLACE_OBJECTS": "1",
                "GIT_OPTIONAL_LOCKS": "0",
            }
        )
        return environment

    def _run(self, *arguments: str) -> bytes:
        try:
            completed = subprocess.run(
                ["git", "-C", str(self.root), *arguments],
                check=False,
                capture_output=True,
                env=self._environment(),
                timeout=15,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise FactorialTaskAuthorityError(
                f"cannot read {self.label} Git objects: {exc}"
            ) from exc
        if completed.returncode != 0:
            detail = completed.stderr.decode("utf-8", errors="replace")[:500]
            raise FactorialTaskAuthorityError(
                f"cannot read {self.label} Git objects: {detail}"
            )
        if len(completed.stdout) > _MAX_GIT_OUTPUT_BYTES:
            raise FactorialTaskAuthorityError(
                f"{self.label} Git object output is too large"
            )
        return completed.stdout

    def _text(self, *arguments: str) -> str:
        try:
            return self._run(*arguments).decode("ascii", errors="strict").strip()
        except UnicodeDecodeError as exc:
            raise FactorialTaskAuthorityError(
                f"{self.label} Git identity is not ASCII"
            ) from exc

    @staticmethod
    def _validate_path(path: str) -> str:
        try:
            pure = PurePosixPath(path)
        except (TypeError, ValueError) as exc:
            raise FactorialTaskAuthorityError("Git path is invalid") from exc
        if (
            not path
            or pure.is_absolute()
            or ".." in pure.parts
            or any(not part or "\x00" in part for part in pure.parts)
        ):
            raise FactorialTaskAuthorityError("Git path is unsafe")
        return path

    def tree_oid(self, path: str) -> str:
        path = self._validate_path(path)
        oid = self._text(
            "rev-parse", "--verify", f"{self.expected_commit}:{path}"
        )
        _git_oid(oid, f"{self.label} tree oid")
        if self._text("cat-file", "-t", oid) != "tree":
            raise FactorialTaskAuthorityError(
                f"{self.label} path is not a committed tree: {path}"
            )
        return oid

    def entries(self, prefix: str) -> tuple[_GitEntry, ...]:
        prefix = self._validate_path(prefix).rstrip("/")
        raw = self._run(
            "ls-tree",
            "-r",
            "-z",
            "--full-tree",
            self.expected_commit,
            "--",
            prefix,
        )
        result: list[_GitEntry] = []
        for encoded in raw.split(b"\0"):
            if not encoded:
                continue
            try:
                metadata, raw_path = encoded.split(b"\t", 1)
                mode, object_type, oid = metadata.decode("ascii").split(" ")
                path = raw_path.decode("utf-8", errors="strict")
            except (ValueError, UnicodeDecodeError) as exc:
                raise FactorialTaskAuthorityError(
                    f"{self.label} Git tree entry is malformed"
                ) from exc
            self._validate_path(path)
            if not path.startswith(prefix + "/"):
                raise FactorialTaskAuthorityError(
                    f"{self.label} Git tree escaped its prefix"
                )
            _git_oid(oid, f"{self.label} object oid")
            result.append(_GitEntry(mode, object_type, oid, path))
        if not result:
            raise FactorialTaskAuthorityError(
                f"{self.label} committed tree is empty: {prefix}"
            )
        return tuple(result)

    def blob(self, path: str) -> bytes:
        path = self._validate_path(path)
        matches = [item for item in self.entries(str(PurePosixPath(path).parent)) if item.path == path]
        if len(matches) != 1:
            raise FactorialTaskAuthorityError(
                f"{self.label} committed blob is missing or repeated: {path}"
            )
        entry = matches[0]
        if entry.object_type != "blob" or entry.mode not in {"100644", "100755"}:
            raise FactorialTaskAuthorityError(
                f"{self.label} public input is not a regular committed blob: {path}"
            )
        return self._run("cat-file", "blob", entry.oid)

    def assert_stable(self) -> None:
        if self._resolve_git_dir() != self._git_dir:
            raise FactorialTaskAuthorityError(
                f"{self.label} Git object database changed during authority derivation"
            )
        if self._text("rev-parse", "--verify", "HEAD^{commit}") != self.expected_commit:
            raise FactorialTaskAuthorityError(
                f"{self.label} source HEAD changed during authority derivation"
            )


@dataclass(frozen=True)
class SourceLockedTaskArtifact:
    """Controller receipt whose public fields are safe for solver binding.

    ``controller_source_binding_sha256`` commits to Git identities, including
    the complete GDPevo group tree, but the private paths and contents behind
    those identities are intentionally absent from this artifact.
    """

    suite: str
    instance_id: str
    task_kind: str
    controller_source_binding_sha256: str
    task_card_sha256: str
    artifact_contract_sha256: str
    reference_artifact_id: str
    reference_artifact_sha256: str
    schema_version: int = 2
    artifact_kind: str = "moss_source_locked_solver_task_artifact_v2"

    def __post_init__(self) -> None:
        if self.schema_version != 2 or self.artifact_kind != (
            "moss_source_locked_solver_task_artifact_v2"
        ):
            raise FactorialTaskAuthorityError("unsupported task artifact schema")
        for value, label in (
            (self.suite, "task artifact suite"),
            (self.instance_id, "task artifact instance"),
            (self.task_kind, "task artifact kind"),
            (self.reference_artifact_id, "reference artifact id"),
        ):
            _safe_id(value, label)
        for value, label in (
            (self.controller_source_binding_sha256, "controller source binding"),
            (self.task_card_sha256, "task card sha256"),
            (self.artifact_contract_sha256, "artifact contract sha256"),
            (self.reference_artifact_sha256, "reference artifact sha256"),
        ):
            _sha(value, label)

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_kind": self.artifact_kind,
            "artifact_contract_sha256": self.artifact_contract_sha256,
            "controller_source_binding_sha256": (
                self.controller_source_binding_sha256
            ),
            "instance_id": self.instance_id,
            "reference_artifact_id": self.reference_artifact_id,
            "reference_artifact_sha256": self.reference_artifact_sha256,
            "schema_version": self.schema_version,
            "suite": self.suite,
            "task_card_sha256": self.task_card_sha256,
            "task_kind": self.task_kind,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return _sha256(self.canonical_bytes)

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "SourceLockedTaskArtifact":
        expected = {
            "artifact_kind",
            "artifact_contract_sha256",
            "controller_source_binding_sha256",
            "instance_id",
            "reference_artifact_id",
            "reference_artifact_sha256",
            "schema_version",
            "suite",
            "task_card_sha256",
            "task_kind",
        }
        if not isinstance(payload, Mapping) or set(payload) != expected:
            raise FactorialTaskAuthorityError("task artifact fields differ")
        return cls(**dict(payload))

    def verify_context(self, context: HarnessContext) -> None:
        if not isinstance(context, HarnessContext):
            raise FactorialTaskAuthorityError("typed HarnessContext is required")
        if context.suite != self.suite or context.instance_id != self.instance_id:
            raise FactorialTaskAuthorityError("HarnessContext task identity differs")
        if context.round_index != 1:
            raise FactorialTaskAuthorityError("task authority requires a v001 context")
        if _sha256(context.task_card.encode("utf-8")) != self.task_card_sha256:
            raise FactorialTaskAuthorityError("HarnessContext task card differs")
        if context.reference_artifact_id != self.reference_artifact_id:
            raise FactorialTaskAuthorityError(
                "HarnessContext reference artifact id differs"
            )
        if (
            _sha256(context.reference_artifact.encode("utf-8"))
            != self.reference_artifact_sha256
        ):
            raise FactorialTaskAuthorityError(
                "HarnessContext reference artifact differs"
            )
        artifact_contract = context.public_observations.get("artifact_contract")
        if (
            set(context.public_observations) != {"artifact_contract"}
            or not isinstance(artifact_contract, dict)
            or _sha256(_canonical_bytes(artifact_contract))
            != self.artifact_contract_sha256
        ):
            raise FactorialTaskAuthorityError(
                "HarnessContext artifact contract differs"
            )
        if (
            context.attempts
            or context.cross_instance_records
            or context.cross_instance_memory_grant is not None
            or context.stream_index is not None
            or context.builder_meta_prior is not None
        ):
            raise FactorialTaskAuthorityError(
                "v001 task authority context contains non-task state"
            )


@dataclass(frozen=True)
class ExactTaskSeedAuthorityBundle:
    """All source-derived keys for the exact 126-cell zero-call matrix."""

    task_seed_keys: tuple[TaskSeedKey, ...]
    task_artifacts: tuple[SourceLockedTaskArtifact, ...]
    factorial_contract_sha256: str
    agenthpo_source_binding_sha256: str
    gdpevo_source_binding_sha256: str
    execution_authority: str = "NOT_GRANTED"
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    schema_version: int = 1
    bundle_kind: str = "moss_exact_factorial_task_seed_authority_bundle_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.bundle_kind != (
            "moss_exact_factorial_task_seed_authority_bundle_v1"
        ):
            raise FactorialTaskAuthorityError("unsupported authority bundle schema")
        if self.execution_authority != "NOT_GRANTED":
            raise FactorialTaskAuthorityError("task authority cannot grant execution")
        if self.model_call_entitlement != 0 or self.evaluator_transaction_entitlement != 0:
            raise FactorialTaskAuthorityError("task authority entitlement must be zero")
        if len(self.task_seed_keys) != 126:
            raise FactorialTaskAuthorityError("task authority matrix is not 126 cells")
        identities = {
            (key.suite, key.instance_id, key.seed) for key in self.task_seed_keys
        }
        if len(identities) != 126:
            raise FactorialTaskAuthorityError("task authority matrix repeats a cell")
        if not isinstance(self.task_artifacts, tuple) or any(
            type(item) is not SourceLockedTaskArtifact for item in self.task_artifacts
        ):
            raise FactorialTaskAuthorityError("task authority artifacts are not exact typed")
        if not isinstance(self.task_seed_keys, tuple) or any(
            type(item) is not TaskSeedKey for item in self.task_seed_keys
        ):
            raise FactorialTaskAuthorityError("task authority keys are not exact typed")
        artifact_by_identity = {
            (item.suite, item.instance_id): item for item in self.task_artifacts
        }
        artifact_identities = set(artifact_by_identity)
        if len(self.task_artifacts) != 42 or len(artifact_identities) != 42:
            raise FactorialTaskAuthorityError(
                "task authority does not contain 42 unique task artifacts"
            )
        _sha(self.factorial_contract_sha256, "factorial contract sha256")
        _sha(self.agenthpo_source_binding_sha256, "AgentHPO source binding")
        _sha(self.gdpevo_source_binding_sha256, "GDPevo source binding")
        if any(
            key.factorial_contract_sha256 != self.factorial_contract_sha256
            for key in self.task_seed_keys
        ):
            raise FactorialTaskAuthorityError("task key contract binding differs")
        key_task_identities = {
            (key.suite, key.instance_id) for key in self.task_seed_keys
        }
        if key_task_identities != artifact_identities:
            raise FactorialTaskAuthorityError("task key/artifact coverage differs")
        for key in self.task_seed_keys:
            artifact = artifact_by_identity[(key.suite, key.instance_id)]
            if key.task_binding_sha256 != artifact.sha256:
                raise FactorialTaskAuthorityError(
                    "task key does not bind its source-locked artifact"
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            "agenthpo_source_binding_sha256": self.agenthpo_source_binding_sha256,
            "bundle_kind": self.bundle_kind,
            "evaluator_transaction_entitlement": (
                self.evaluator_transaction_entitlement
            ),
            "execution_authority": self.execution_authority,
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "gdpevo_source_binding_sha256": self.gdpevo_source_binding_sha256,
            "model_call_entitlement": self.model_call_entitlement,
            "schema_version": self.schema_version,
            "task_artifact_sha256s": [item.sha256 for item in self.task_artifacts],
            "task_artifacts": [item.to_dict() for item in self.task_artifacts],
            "task_seed_key_sha256s": [item.sha256 for item in self.task_seed_keys],
            "task_seed_keys": [item.core_payload() for item in self.task_seed_keys],
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return _sha256(self.canonical_bytes)

    @classmethod
    def from_canonical_bytes(
        cls, raw: bytes, *, expected_sha256: str | None = None
    ) -> "ExactTaskSeedAuthorityBundle":
        if not isinstance(raw, bytes) or not raw:
            raise FactorialTaskAuthorityError("task authority bundle bytes are empty")
        payload = _strict_json(raw, label="task authority bundle")
        if not isinstance(payload, dict) or _canonical_bytes(payload) != raw:
            raise FactorialTaskAuthorityError("task authority bundle is not canonical")
        expected = {
            "agenthpo_source_binding_sha256",
            "bundle_kind",
            "evaluator_transaction_entitlement",
            "execution_authority",
            "factorial_contract_sha256",
            "gdpevo_source_binding_sha256",
            "model_call_entitlement",
            "schema_version",
            "task_artifact_sha256s",
            "task_artifacts",
            "task_seed_key_sha256s",
            "task_seed_keys",
        }
        if set(payload) != expected:
            raise FactorialTaskAuthorityError("task authority bundle fields differ")
        raw_artifacts = payload["task_artifacts"]
        artifact_hashes = payload["task_artifact_sha256s"]
        raw_keys = payload["task_seed_keys"]
        key_hashes = payload["task_seed_key_sha256s"]
        if not all(
            isinstance(value, list)
            for value in (raw_artifacts, artifact_hashes, raw_keys, key_hashes)
        ) or len(raw_artifacts) != len(artifact_hashes) or len(raw_keys) != len(
            key_hashes
        ):
            raise FactorialTaskAuthorityError("task authority bundle members differ")
        artifacts = tuple(
            SourceLockedTaskArtifact.from_dict(item) for item in raw_artifacts
        )
        if [item.sha256 for item in artifacts] != artifact_hashes:
            raise FactorialTaskAuthorityError("task authority artifact hashes differ")
        keys: list[TaskSeedKey] = []
        for item, item_sha256 in zip(raw_keys, key_hashes, strict=True):
            if not isinstance(item, dict):
                raise FactorialTaskAuthorityError("task authority key differs")
            try:
                key = TaskSeedKey.from_bytes(
                    _canonical_bytes(item), expected_sha256=item_sha256
                )
            except (TypeError, ValueError) as exc:
                raise FactorialTaskAuthorityError(
                    "task authority key replay failed"
                ) from exc
            keys.append(key)
        bundle = cls(
            task_seed_keys=tuple(keys),
            task_artifacts=artifacts,
            factorial_contract_sha256=payload["factorial_contract_sha256"],
            agenthpo_source_binding_sha256=payload[
                "agenthpo_source_binding_sha256"
            ],
            gdpevo_source_binding_sha256=payload["gdpevo_source_binding_sha256"],
            execution_authority=payload["execution_authority"],
            model_call_entitlement=payload["model_call_entitlement"],
            evaluator_transaction_entitlement=payload[
                "evaluator_transaction_entitlement"
            ],
            schema_version=payload["schema_version"],
            bundle_kind=payload["bundle_kind"],
        )
        if bundle.canonical_bytes != raw:
            raise FactorialTaskAuthorityError("task authority bundle replay differs")
        if expected_sha256 is not None:
            _sha(expected_sha256, "expected task authority bundle sha256")
            if bundle.sha256 != expected_sha256:
                raise FactorialTaskAuthorityError("task authority bundle hash differs")
        return bundle


@dataclass(frozen=True)
class _DerivedTask:
    artifact: SourceLockedTaskArtifact
    context: HarnessContext


def _artifact_contract_capability(
    *,
    suite: str,
    instance_id: str,
    task_kind: str,
    task_card: str,
    reference_artifact_id: str,
    reference_artifact: str,
    candidate_kind: str,
    formal_dispatch_status: str,
) -> dict[str, Any]:
    """Build the only public v001 artifact capability card.

    Every field is derived from the pinned public task projection.  The card
    intentionally contains no evaluator path, gold answer, private rubric, or
    caller-provided value.  Binding both public artifact hashes makes a card
    unusable for another task even when the two suites share a candidate kind.
    """

    for value, label in (
        (suite, "artifact contract suite"),
        (instance_id, "artifact contract instance"),
        (task_kind, "artifact contract task kind"),
        (reference_artifact_id, "artifact contract reference id"),
        (candidate_kind, "artifact contract candidate kind"),
        (formal_dispatch_status, "artifact contract dispatch status"),
    ):
        _safe_id(value, label)
    return {
        "candidate_kind": candidate_kind,
        "capability_kind": "MOSS_FACTORIAL_ARTIFACT_CONTRACT_V1",
        "formal_dispatch_status": formal_dispatch_status,
        "instance_id": instance_id,
        "reference_artifact_id": reference_artifact_id,
        "reference_artifact_sha256": _sha256(reference_artifact.encode("utf-8")),
        "schema_version": 1,
        "suite": suite,
        "task_card_sha256": _sha256(task_card.encode("utf-8")),
        "task_kind": task_kind,
    }


def _parse_scoring_table(raw: bytes) -> dict[str, dict[str, object]]:
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise FactorialTaskAuthorityError(
            "AgentHPO scoring table is not UTF-8"
        ) from exc
    lines = text.splitlines()
    if not lines or lines[0] != "task\tcategory\tdirection\tbaseline\tanchor":
        raise FactorialTaskAuthorityError("AgentHPO scoring table header differs")
    result: dict[str, dict[str, object]] = {}
    for line in lines[1:]:
        fields = line.split("\t")
        if len(fields) != 5:
            raise FactorialTaskAuthorityError("AgentHPO scoring row differs")
        task_id, category, direction, baseline, anchor = fields
        _safe_id(task_id, "AgentHPO score task")
        _safe_id(category, "AgentHPO category")
        if direction not in {"higher", "lower"}:
            raise FactorialTaskAuthorityError("AgentHPO score direction differs")
        try:
            baseline_value = float(baseline)
            anchor_value = float(anchor)
        except ValueError as exc:
            raise FactorialTaskAuthorityError(
                "AgentHPO score value is not numeric"
            ) from exc
        if not math.isfinite(baseline_value) or not math.isfinite(anchor_value):
            raise FactorialTaskAuthorityError("AgentHPO score value is not finite")
        if task_id in result:
            raise FactorialTaskAuthorityError("AgentHPO scoring task repeats")
        result[task_id] = {
            "anchor": anchor_value,
            "baseline": baseline_value,
            "category": category,
            "direction": direction,
        }
    return result


def _agenthpo_parameter_projection(
    task_id: str, raw_task: object
) -> tuple[dict[str, Any], str]:
    if not isinstance(raw_task, dict) or set(raw_task) != {"nested", "parameters"}:
        raise FactorialTaskAuthorityError(
            f"AgentHPO task {task_id} does not expose a typed discrete space"
        )
    if raw_task["nested"] is not True or not isinstance(
        raw_task["parameters"], dict
    ) or not raw_task["parameters"]:
        raise FactorialTaskAuthorityError(
            f"AgentHPO task {task_id} discrete space differs"
        )
    projected: dict[str, Any] = {}
    nullable = False
    for name, declaration in sorted(raw_task["parameters"].items()):
        _safe_id(name, "AgentHPO parameter")
        if not isinstance(declaration, dict) or set(declaration) != {
            "baseline",
            "narrow",
            "nested",
            "original",
            "wide",
        }:
            raise FactorialTaskAuthorityError(
                f"AgentHPO parameter declaration differs: {name}"
            )
        if declaration["nested"] is not True or not isinstance(
            declaration["original"], list
        ) or not declaration["original"]:
            raise FactorialTaskAuthorityError(
                f"AgentHPO original parameter space differs: {name}"
            )
        baseline = _typed_public_scalar(
            declaration["baseline"], label=f"AgentHPO {name} baseline"
        )
        original = [
            _typed_public_scalar(value, label=f"AgentHPO {name} value")
            for value in declaration["original"]
        ]
        if len({(type(value).__name__, repr(value)) for value in original}) != len(
            original
        ):
            raise FactorialTaskAuthorityError(
                f"AgentHPO original parameter values repeat: {name}"
            )
        if not any(_same_typed_scalar(baseline, value) for value in original):
            raise FactorialTaskAuthorityError(
                f"AgentHPO baseline is outside original space: {name}"
            )
        nullable = nullable or baseline is None or any(value is None for value in original)
        projected[name] = {"allowed_values": original, "baseline": baseline}
    return projected, (
        "STRICT_NULLABLE_DISCRETE_CODEC_DERIVABLE"
        if nullable
        else "STRICT_DISCRETE_CODEC_DERIVABLE"
    )


def _extract_free_form_baseline(raw: bytes) -> tuple[str, tuple[str, ...]]:
    try:
        tree = ast.parse(raw.decode("utf-8", errors="strict"))
    except (UnicodeDecodeError, SyntaxError) as exc:
        raise FactorialTaskAuthorityError(
            "AgentHPO free-form task source is invalid"
        ) from exc
    assignments = [
        node
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        and (
            (
                isinstance(node, ast.Assign)
                and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id == "BASELINE_TEMPLATE"
            )
            or (
                isinstance(node, ast.AnnAssign)
                and isinstance(node.target, ast.Name)
                and node.target.id == "BASELINE_TEMPLATE"
            )
        )
    ]
    if len(assignments) != 1:
        raise FactorialTaskAuthorityError(
            "AgentHPO free-form baseline template is missing or repeated"
        )
    node = assignments[0]
    value_node = node.value
    try:
        baseline = ast.literal_eval(value_node)
    except (ValueError, TypeError) as exc:
        raise FactorialTaskAuthorityError(
            "AgentHPO free-form baseline is not a static string"
        ) from exc
    if not isinstance(baseline, str) or not baseline.strip() or len(baseline) > 16_384:
        raise FactorialTaskAuthorityError(
            "AgentHPO free-form baseline string is unsafe"
        )
    try:
        placeholders = tuple(
            sorted(
                {
                    field_name
                    for _literal, field_name, _format_spec, _conversion in (
                        string.Formatter().parse(baseline)
                    )
                    if field_name is not None
                }
            )
        )
    except ValueError as exc:
        raise FactorialTaskAuthorityError(
            "AgentHPO free-form baseline placeholders are invalid"
        ) from exc
    if not placeholders or any(_SAFE_ID.fullmatch(item) is None for item in placeholders):
        raise FactorialTaskAuthorityError(
            "AgentHPO free-form baseline placeholders differ"
        )
    return baseline, placeholders


def _utf8_public_blob(raw: bytes, *, label: str) -> str:
    if not raw or len(raw) > _MAX_PUBLIC_TASK_BYTES or b"\x00" in raw:
        raise FactorialTaskAuthorityError(f"{label} byte content is unsafe")
    try:
        return raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise FactorialTaskAuthorityError(f"{label} is not UTF-8") from exc


class FactorialTaskArtifactAuthority:
    """Mechanically derive and validate the complete formal task matrix."""

    def __init__(
        self,
        *,
        agenthpo_checkout: str | Path,
        gdpevo_checkout: str | Path,
    ) -> None:
        factorial = verify_factorial_contract()
        agent_qualification = verify_agenthpo_qualification()
        gdp_qualification = verify_gdpevo_qualification()
        agent_lock = agent_qualification["source_lock"]
        gdp_lock = gdp_qualification["source_lock"]
        if not isinstance(agent_lock, dict) or not isinstance(gdp_lock, dict):
            raise FactorialTaskAuthorityError("qualification source lock differs")
        self._factorial_contract_sha256 = _sha(
            factorial["contract_digest"], "factorial contract sha256"
        )
        self._matrix = factorial_main_matrix_projection(factorial)
        self._agent = _PinnedGitCheckout(
            Path(agenthpo_checkout),
            expected_commit=agent_lock["git_commit"],
            expected_root_tree=agent_lock["root_tree"],
            label="AgentHPOBench checkout",
        )
        self._gdp = _PinnedGitCheckout(
            Path(gdpevo_checkout),
            expected_commit=gdp_lock["git_commit"],
            expected_root_tree=gdp_lock["root_tree"],
            label="GDPevo checkout",
        )
        self._agent_lock = dict(agent_lock)
        self._gdp_lock = dict(gdp_lock)
        self._agent_source_binding_sha256 = _sha256(
            _canonical_bytes(self._agent_lock)
        )
        self._gdp_source_binding_sha256 = _sha256(
            _canonical_bytes(self._gdp_lock)
        )
        self._derived = self._derive_all_tasks()
        self._agent.assert_stable()
        self._gdp.assert_stable()

    @property
    def factorial_contract_sha256(self) -> str:
        return self._factorial_contract_sha256

    def _derive_all_tasks(self) -> Mapping[tuple[str, str], _DerivedTask]:
        identities: list[tuple[str, str, str, int]] = []
        seen: set[tuple[str, str]] = set()
        for item in self._matrix:
            identity = (item["benchmark_id"], item["instance_id"])
            if identity not in seen:
                identities.append(
                    (
                        item["benchmark_id"],
                        item["instance_id"],
                        item["task_unit"],
                        item["task_ordinal"],
                    )
                )
                seen.add(identity)
        if len(identities) != 42:
            raise FactorialTaskAuthorityError(
                "factorial contract does not contain 42 unique tasks"
            )

        raw_space = self._agent.blob(_AGENTHPO_SPACE_PATH)
        raw_scoring = self._agent.blob(_AGENTHPO_SCORING_PATH)
        expected_control = self._agent_lock.get("control_file_sha256")
        if not isinstance(expected_control, dict):
            raise FactorialTaskAuthorityError(
                "AgentHPO qualification control-file lock differs"
            )
        for path, raw in (
            (_AGENTHPO_SPACE_PATH, raw_space),
            (_AGENTHPO_SCORING_PATH, raw_scoring),
        ):
            if expected_control.get(path) != _sha256(raw):
                raise FactorialTaskAuthorityError(
                    f"AgentHPO source-locked control file drifted: {path}"
                )
        space_manifest = _strict_json(raw_space, label="AgentHPO space manifest")
        if (
            not isinstance(space_manifest, dict)
            or set(space_manifest) != {"all_nested", "definition", "task_count", "tasks"}
            or space_manifest["all_nested"] is not True
            or space_manifest["task_count"] != 30
            or not isinstance(space_manifest["tasks"], dict)
            or len(space_manifest["tasks"]) != 30
        ):
            raise FactorialTaskAuthorityError("AgentHPO space manifest differs")
        scores = _parse_scoring_table(raw_scoring)

        result: dict[tuple[str, str], _DerivedTask] = {}
        for suite, instance_id, task_unit, task_ordinal in identities:
            if suite == "agenthpobench":
                result[(suite, instance_id)] = self._derive_agent_task(
                    instance_id, space_manifest["tasks"], scores
                )
            elif suite == "gdpevo":
                result[(suite, instance_id)] = self._derive_gdpevo_task(
                    instance_id, task_unit=task_unit, task_ordinal=task_ordinal
                )
            else:
                raise FactorialTaskAuthorityError(
                    f"unsupported factorial benchmark: {suite}"
                )
        return MappingProxyType(result)

    def _derive_agent_task(
        self,
        task_id: str,
        tasks: Mapping[str, object],
        scores: Mapping[str, Mapping[str, object]],
    ) -> _DerivedTask:
        if task_id not in tasks or task_id not in scores:
            raise FactorialTaskAuthorityError(
                f"AgentHPO formal task is absent from public source: {task_id}"
            )
        task_tree = self._agent.tree_oid(f"tasks/main/{task_id}")
        raw_task = tasks[task_id]
        if task_id == _AGENTHPO_FREE_FORM_TASK:
            expected_special = {
                "ablation_policy": (
                    "held constant because the task does not expose a scalar SEARCH_SPACE"
                ),
                "nested": True,
                "special_space": "free-form prompt intervention",
            }
            if raw_task != expected_special:
                raise FactorialTaskAuthorityError(
                    "AgentHPO room-selector special task contract differs"
                )
            script_path = (
                "tasks/main/agent_lightning_room_selector/"
                "run_formal_agent_lightning_room_selector.py"
            )
            baseline, placeholders = _extract_free_form_baseline(
                self._agent.blob(script_path)
            )
            task_kind = "AGENTHPO_FREE_FORM_PROMPT_TEMPLATE_V1"
            action_contract: dict[str, Any] = {
                "baseline_placeholders": list(placeholders),
                "formal_dispatch_status": "FREE_FORM_CODEC_REQUIRED_FAIL_CLOSED",
                "proposal_type": "UTF8_PROMPT_TEMPLATE",
                "space_kind": "FREE_FORM_PROMPT_INTERVENTION",
            }
            reference_id = "baseline-prompt-template"
            reference = baseline
        else:
            parameters, compatibility = _agenthpo_parameter_projection(
                task_id, raw_task
            )
            task_kind = "AGENTHPO_DISCRETE_HYPERPARAMETER_V1"
            action_contract = {
                "formal_dispatch_status": compatibility,
                "parameters": parameters,
                "space_kind": "EXACT_ORIGINAL_DISCRETE_SPACE",
            }
            reference_id = "baseline-config"
            reference = _canonical_text(
                {
                    name: declaration["baseline"]
                    for name, declaration in parameters.items()
                }
            )
        task_card = _canonical_text(
            {
                "action_contract": action_contract,
                "benchmark_id": "agenthpobench",
                "instance_id": task_id,
                "objective": dict(scores[task_id]),
                "schema_version": 1,
                "task_kind": task_kind,
            }
        )
        capability = _artifact_contract_capability(
            suite="agenthpobench",
            instance_id=task_id,
            task_kind=task_kind,
            task_card=task_card,
            reference_artifact_id=reference_id,
            reference_artifact=reference,
            candidate_kind=(
                "UTF8_PROMPT_TEMPLATE"
                if task_id == _AGENTHPO_FREE_FORM_TASK
                else "EXACT_DISCRETE_INTERVENTION"
            ),
            formal_dispatch_status=action_contract["formal_dispatch_status"],
        )
        source_binding = _sha256(
            _canonical_bytes(
                {
                    "benchmark_source_lock_sha256": (
                        self._agent_source_binding_sha256
                    ),
                    "public_scoring_blob_sha256": _sha256(
                        self._agent.blob(_AGENTHPO_SCORING_PATH)
                    ),
                    "public_space_manifest_blob_sha256": _sha256(
                        self._agent.blob(_AGENTHPO_SPACE_PATH)
                    ),
                    "task_id": task_id,
                    "task_tree_oid": task_tree,
                }
            )
        )
        artifact = SourceLockedTaskArtifact(
            suite="agenthpobench",
            instance_id=task_id,
            task_kind=task_kind,
            controller_source_binding_sha256=source_binding,
            task_card_sha256=_sha256(task_card.encode("utf-8")),
            artifact_contract_sha256=_sha256(_canonical_bytes(capability)),
            reference_artifact_id=reference_id,
            reference_artifact_sha256=_sha256(reference.encode("utf-8")),
        )
        context = HarnessContext(
            instance_id=task_id,
            suite="agenthpobench",
            round_index=1,
            task_card=task_card,
            reference_artifact_id=reference_id,
            reference_artifact=reference,
            public_observations={"artifact_contract": capability},
        )
        artifact.verify_context(context)
        return _DerivedTask(artifact, context)

    def _derive_gdpevo_task(
        self, instance_id: str, *, task_unit: str, task_ordinal: int
    ) -> _DerivedTask:
        expected_instance = f"{task_unit}:test_{task_ordinal}"
        if instance_id != expected_instance or not 1 <= task_ordinal <= 5:
            raise FactorialTaskAuthorityError("GDPevo formal task identity differs")
        group_prefix = f"data/task_groups/{task_unit}"
        task_prefix = f"{group_prefix}/test_tasks/{task_ordinal:03d}"
        input_prefix = f"{task_prefix}/input"
        group_tree = self._gdp.tree_oid(group_prefix)
        task_tree = self._gdp.tree_oid(task_prefix)
        input_tree = self._gdp.tree_oid(input_prefix)
        entries = self._gdp.entries(input_prefix)
        files: dict[str, str] = {}
        file_digests: dict[str, str] = {}
        total_bytes = 0
        for entry in entries:
            if entry.object_type != "blob" or entry.mode not in {"100644", "100755"}:
                raise FactorialTaskAuthorityError(
                    "GDPevo public task input is not a regular committed blob"
                )
            relative = entry.path.removeprefix(input_prefix + "/")
            parts = PurePosixPath(relative).parts
            if (
                not parts
                or any(part.lower() in _GDPEVO_FORBIDDEN_COMPONENTS for part in parts)
                or (
                    relative != "prompt.txt"
                    and not relative.startswith("payloads/")
                )
            ):
                raise FactorialTaskAuthorityError(
                    f"GDPevo solver projection contains a forbidden path: {relative}"
                )
            raw = self._gdp._run("cat-file", "blob", entry.oid)
            total_bytes += len(raw)
            if total_bytes > _MAX_PUBLIC_TASK_BYTES:
                raise FactorialTaskAuthorityError(
                    "GDPevo public task projection is too large"
                )
            files[relative] = _utf8_public_blob(
                raw, label=f"GDPevo public task input {relative}"
            )
            file_digests[relative] = _sha256(raw)
        if "prompt.txt" not in files or "payloads/answer_template.json" not in files:
            raise FactorialTaskAuthorityError(
                "GDPevo task lacks its prompt or public answer template"
            )
        payloads = [
            {
                "path": path.removeprefix("payloads/"),
                "sha256": file_digests[path],
                "text": files[path],
            }
            for path in sorted(files)
            if path.startswith("payloads/") and path != "payloads/answer_template.json"
        ]
        task_kind = "GDPEVO_STRUCTURED_ENVIRONMENT_TASK_V1"
        task_card = _canonical_text(
            {
                "benchmark_id": "gdpevo",
                "instance_id": instance_id,
                "payloads": payloads,
                "prompt": files["prompt.txt"],
                "schema_version": 1,
                "task_kind": task_kind,
            }
        )
        reference_id = "answer-template"
        reference = files["payloads/answer_template.json"]
        capability = _artifact_contract_capability(
            suite="gdpevo",
            instance_id=instance_id,
            task_kind=task_kind,
            task_card=task_card,
            reference_artifact_id=reference_id,
            reference_artifact=reference,
            candidate_kind="STRICT_ANSWER_TEMPLATE_JSON",
            formal_dispatch_status="STRICT_STRUCTURED_CODEC_REQUIRED",
        )
        source_binding = _sha256(
            _canonical_bytes(
                {
                    "benchmark_source_lock_sha256": self._gdp_source_binding_sha256,
                    "complete_group_tree_oid": group_tree,
                    "input_tree_oid": input_tree,
                    "instance_id": instance_id,
                    "public_input_file_sha256s": file_digests,
                    "test_task_tree_oid": task_tree,
                }
            )
        )
        artifact = SourceLockedTaskArtifact(
            suite="gdpevo",
            instance_id=instance_id,
            task_kind=task_kind,
            controller_source_binding_sha256=source_binding,
            task_card_sha256=_sha256(task_card.encode("utf-8")),
            artifact_contract_sha256=_sha256(_canonical_bytes(capability)),
            reference_artifact_id=reference_id,
            reference_artifact_sha256=_sha256(reference.encode("utf-8")),
        )
        context = HarnessContext(
            instance_id=instance_id,
            suite="gdpevo",
            round_index=1,
            task_card=task_card,
            reference_artifact_id=reference_id,
            reference_artifact=reference,
            public_observations={"artifact_contract": capability},
        )
        artifact.verify_context(context)
        return _DerivedTask(artifact, context)

    def derived_contexts(self) -> dict[tuple[str, str], HarnessContext]:
        """Return the exact 42 solver-visible v001 contexts.

        Formal orchestration should pass the contexts it intends to execute
        back to :meth:`authorize_exact_matrix`; silently substituting another
        task card or reference artifact is rejected before a plan exists.
        """

        return {identity: item.context for identity, item in self._derived.items()}

    def task_artifacts(self) -> tuple[SourceLockedTaskArtifact, ...]:
        return tuple(item.artifact for item in self._derived.values())

    def authorize_exact_matrix(
        self, contexts: Mapping[tuple[str, str], HarnessContext]
    ) -> ExactTaskSeedAuthorityBundle:
        """Create all keys without accepting any caller-provided digest."""

        if not isinstance(contexts, Mapping):
            raise FactorialTaskAuthorityError("HarnessContext mapping is required")
        if set(contexts) != set(self._derived):
            raise FactorialTaskAuthorityError(
                "HarnessContext coverage differs from the exact 42-task matrix"
            )
        for identity, expected in self._derived.items():
            context = contexts[identity]
            expected.artifact.verify_context(context)
            if context != expected.context:
                raise FactorialTaskAuthorityError(
                    f"HarnessContext public projection differs: {identity}"
                )

        keys: list[TaskSeedKey] = []
        for item in self._matrix:
            identity = (item["benchmark_id"], item["instance_id"])
            derived = self._derived[identity]
            context = contexts[identity]
            key = TaskSeedKey.create(
                context=context,
                seed=item["seed"],
                task_binding_sha256=derived.artifact.sha256,
                factorial_contract_sha256=self._factorial_contract_sha256,
            )
            if key.context_binding_sha256 != (
                TrustedOperatorRegistry.context_binding_sha256(context)
            ):
                raise FactorialTaskAuthorityError(
                    "mechanical HarnessContext binding differs"
                )
            keys.append(key)
        self._agent.assert_stable()
        self._gdp.assert_stable()
        return ExactTaskSeedAuthorityBundle(
            task_seed_keys=tuple(keys),
            task_artifacts=self.task_artifacts(),
            factorial_contract_sha256=self._factorial_contract_sha256,
            agenthpo_source_binding_sha256=self._agent_source_binding_sha256,
            gdpevo_source_binding_sha256=self._gdp_source_binding_sha256,
        )

    def rederive_exact_bundle(self) -> ExactTaskSeedAuthorityBundle:
        """Re-read the pinned identities and reproduce the complete bundle."""

        return self.authorize_exact_matrix(self.derived_contexts())

    def verify_exact_bundle(
        self, bundle: ExactTaskSeedAuthorityBundle
    ) -> ExactTaskSeedAuthorityBundle:
        """Reject a self-consistent bundle that was not derived by this authority."""

        if type(bundle) is not ExactTaskSeedAuthorityBundle:
            raise FactorialTaskAuthorityError(
                "exact typed task authority bundle is required"
            )
        replayed = ExactTaskSeedAuthorityBundle.from_canonical_bytes(
            bundle.canonical_bytes, expected_sha256=bundle.sha256
        )
        expected = self.rederive_exact_bundle()
        if replayed != expected or replayed.sha256 != expected.sha256:
            raise FactorialTaskAuthorityError(
                "task authority bundle differs from pinned source derivation"
            )
        return expected

    def build_formal_zero_call_plan(
        self, contexts: Mapping[tuple[str, str], HarnessContext]
    ) -> Any:
        """Feed only mechanically authorized keys to the exact plan factory."""

        # Local import avoids making the task authority part of the generic
        # fixture precheck dependency surface.
        from .factorial_precheck import FactorialFormalZeroCallPlan

        bundle = self.authorize_exact_matrix(contexts)
        return FactorialFormalZeroCallPlan.from_authority_bundle(
            bundle, task_authority=self
        )


__all__ = [
    "ExactTaskSeedAuthorityBundle",
    "FactorialTaskArtifactAuthority",
    "FactorialTaskAuthorityError",
    "SourceLockedTaskArtifact",
]
