"""Strict AgentHPOBench intervention and provider-request accounting contracts.

The upstream AgentHPOBench helper accepts aliases, ignores unknown keys,
clamps out-of-range values, falls back to the current configuration, and may
retry one apparent API call several times.  Those behaviours are useful for a
general benchmark runner but would confound the Moss factorial experiment.

This module is deliberately incapable of calling a provider or evaluator.  It
parses one already-produced response against a controller-supplied, frozen
discrete search space and seals typed receipts for *every* provider request.
A future formal gateway must use these artifacts and must not call the
upstream retrying client.
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import re
import stat
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_ZERO_SHA256 = "0" * 64
_MAX_RESPONSE_BYTES = 64 * 1024
_TERMINAL_REQUEST_STATUSES = frozenset({"COMPLETED", "FAILED"})
_PINNED_AGENTHPO_COMMIT = "6d8d90071cdb16b06f0db866480ecaae48880fba"
_PINNED_AGENTHPO_ROOT_TREE = "1acedca0a63252deea57a51878b4ddfd002aa507"
_PINNED_SPACE_MANIFEST_PATH = "tasks/main/space_manifest.json"
_PINNED_SPACE_MANIFEST_SHA256 = (
    "68d466bc0069908ad178f9a5921e618077545b7aa44d5f64f65cb77cbb88f7de"
)
_PINNED_SPACE_BACKEND_PATH = "tasks/main/space_ablation_backend_full30.py"
_PINNED_SPACE_BACKEND_SHA256 = (
    "2e9ebff9833731e28ce22f47f2d591947e0b668051dfd2b60e2741f980a13998"
)
_SPACE_VARIANTS = frozenset({"original", "narrow", "wide"})
_MANIFEST_TOP_FIELDS = {"all_nested", "definition", "task_count", "tasks"}
_MANIFEST_PARAMETER_FIELDS = {"baseline", "narrow", "nested", "original", "wide"}


class AgentHPOInterventionError(ValueError):
    """An intervention or request-accounting artifact is unsafe or ambiguous."""


def _reject_constant(value: str) -> None:
    raise AgentHPOInterventionError(f"intervention JSON contains {value}")


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise AgentHPOInterventionError(
                f"intervention JSON repeats field {key!r}"
            )
        result[key] = value
    return result


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
        raise AgentHPOInterventionError(
            "intervention payload is not canonical JSON"
        ) from exc


def _sha(value: object, label: str, *, allow_zero: bool = False) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise AgentHPOInterventionError(f"invalid {label}")
    if not allow_zero and value == _ZERO_SHA256:
        raise AgentHPOInterventionError(f"empty {label}")
    return value


def _safe(value: object, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise AgentHPOInterventionError(f"unsafe {label}")
    return value


def _typed_scalar(value: object, label: str) -> None | bool | int | float | str:
    # ``None`` is an exact, meaningful sentinel in two pinned AgentHPO spaces
    # (for example RandomForest ``max_depth``).  It is accepted only when the
    # pinned allowlist also contains JSON null; it is never a fallback marker.
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise AgentHPOInterventionError(f"{label} must be finite")
        return 0.0 if value == 0.0 else value
    if (
        isinstance(value, str)
        and value
        and len(value) <= 512
        and "\x00" not in value
    ):
        return value
    raise AgentHPOInterventionError(
        f"{label} must be null or a bounded JSON string, boolean, integer, "
        "or finite float"
    )


def _same_typed_scalar(left: object, right: object) -> bool:
    # Python considers True == 1 and 1 == 1.0.  Hyperparameter types are part
    # of the contract, so those values must not be interchangeable.
    return type(left) is type(right) and left == right


def _parse_one_object(raw: bytes) -> dict[str, Any]:
    if not isinstance(raw, bytes) or not raw or len(raw) > _MAX_RESPONSE_BYTES:
        raise AgentHPOInterventionError("raw intervention byte length is invalid")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise AgentHPOInterventionError("raw intervention is not UTF-8") from exc
    decoder = json.JSONDecoder(
        object_pairs_hook=_reject_duplicates,
        parse_constant=_reject_constant,
    )
    leading = len(text) - len(text.lstrip())
    try:
        payload, end = decoder.raw_decode(text, idx=leading)
    except json.JSONDecodeError as exc:
        raise AgentHPOInterventionError(
            "raw intervention is not one strict JSON object"
        ) from exc
    if text[end:].strip():
        raise AgentHPOInterventionError(
            "raw intervention contains data after its JSON object"
        )
    if not isinstance(payload, dict):
        raise AgentHPOInterventionError("raw intervention must be a JSON object")
    return payload


def _parse_canonical_object(raw: bytes, *, label: str) -> dict[str, Any]:
    payload = _parse_one_object(raw)
    if _canonical_bytes(payload) != raw:
        raise AgentHPOInterventionError(f"{label} is not canonical")
    return payload


def _exact_fields(
    payload: Mapping[str, Any], expected: set[str], *, label: str
) -> None:
    if set(payload) != expected:
        raise AgentHPOInterventionError(f"{label} fields differ")


def _path_has_symlink(path: Path) -> bool:
    current = path
    while True:
        try:
            if stat.S_ISLNK(os.lstat(current).st_mode):
                return True
        except OSError as exc:
            raise AgentHPOInterventionError(
                f"cannot inspect AgentHPO source path component {current}"
            ) from exc
        parent = current.parent
        if parent == current:
            return False
        current = parent


def _read_bound_source_file(root: Path, relative: str) -> bytes:
    if not isinstance(relative, str) or Path(relative).is_absolute() or ".." in Path(
        relative
    ).parts:
        raise AgentHPOInterventionError("unsafe AgentHPO source-relative path")
    candidate = root / relative
    if _path_has_symlink(candidate):
        raise AgentHPOInterventionError("AgentHPO source input may not contain symlinks")
    try:
        resolved = candidate.resolve(strict=True)
    except OSError as exc:
        raise AgentHPOInterventionError(
            f"required AgentHPO source input is missing: {relative}"
        ) from exc
    if resolved != candidate or not resolved.is_file():
        raise AgentHPOInterventionError(
            f"AgentHPO source input is not an explicit regular file: {relative}"
        )
    return resolved.read_bytes()


def _git_output(root: Path, *arguments: str) -> str:
    environment = dict(os.environ)
    environment["GIT_OPTIONAL_LOCKS"] = "0"
    try:
        completed = subprocess.run(
            ("git", "-C", os.fspath(root), *arguments),
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=15,
            env=environment,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise AgentHPOInterventionError("cannot verify pinned AgentHPO git source") from exc
    return completed.stdout.strip()


def _require_clean_tracked_source(root: Path) -> None:
    environment = dict(os.environ)
    environment["GIT_OPTIONAL_LOCKS"] = "0"
    try:
        completed = subprocess.run(
            (
                "git",
                "-C",
                os.fspath(root),
                "status",
                "--porcelain=v1",
                "--untracked-files=no",
            ),
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=15,
            env=environment,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise AgentHPOInterventionError("cannot audit pinned AgentHPO worktree") from exc
    if completed.stdout:
        raise AgentHPOInterventionError("pinned AgentHPO tracked worktree is dirty")


def _typed_manifest_scalar(
    value: object, label: str
) -> None | bool | int | float | str:
    if value is None:
        return None
    return _typed_scalar(value, label)


def _same_manifest_scalar(left: object, right: object) -> bool:
    return type(left) is type(right) and left == right


def _manifest_scalar_list(value: object, label: str) -> list[object]:
    if not isinstance(value, list) or not value or len(value) > 256:
        raise AgentHPOInterventionError(f"{label} must be a bounded non-empty list")
    result = [_typed_manifest_scalar(item, label) for item in value]
    identities = {(type(item).__name__, repr(item)) for item in result}
    if len(identities) != len(result):
        raise AgentHPOInterventionError(f"{label} contains duplicate typed values")
    return result


def _extract_runner_literals(
    runner_raw: bytes,
) -> tuple[dict[str, object], dict[str, object]]:
    try:
        tree = ast.parse(runner_raw)
    except (SyntaxError, ValueError) as exc:
        raise AgentHPOInterventionError("AgentHPO task runner is not valid Python") from exc
    literals: dict[str, dict[str, object]] = {}
    counts = {"BASE_CONFIG": 0, "SEARCH_SPACE": 0}
    for statement in tree.body:
        if not isinstance(statement, ast.Assign):
            continue
        for target in statement.targets:
            if not isinstance(target, ast.Name) or target.id not in counts:
                continue
            counts[target.id] += 1
            if target.id in literals:
                # The pinned runners reassign SEARCH_SPACE exactly once through
                # the source-locked ablation backend.  Only the first literal
                # definition describes the independently checkable original
                # space; every other reassignment must be non-literal.
                try:
                    ast.literal_eval(statement.value)
                except (ValueError, TypeError, SyntaxError):
                    continue
                raise AgentHPOInterventionError(
                    f"AgentHPO task runner repeats literal {target.id}"
                )
            try:
                value = ast.literal_eval(statement.value)
            except (ValueError, TypeError, SyntaxError) as exc:
                raise AgentHPOInterventionError(
                    f"AgentHPO task runner {target.id} is not a literal mapping"
                ) from exc
            if not isinstance(value, dict):
                raise AgentHPOInterventionError(
                    f"AgentHPO task runner {target.id} is not a mapping"
                )
            literals[target.id] = value
    if set(literals) != set(counts) or counts["BASE_CONFIG"] != 1:
        raise AgentHPOInterventionError(
            "AgentHPO task runner lacks one literal BASE_CONFIG/SEARCH_SPACE pair"
        )
    return literals["BASE_CONFIG"], literals["SEARCH_SPACE"]


def _runner_choices(search_space: Mapping[str, object]) -> dict[str, list[object]]:
    choices: dict[str, list[object]] = {}
    for key, raw_spec in search_space.items():
        _safe(key, "AgentHPO runner search-space key")
        if isinstance(raw_spec, dict):
            if set(raw_spec) != {"choices"}:
                raise AgentHPOInterventionError(
                    f"AgentHPO runner search-space spec for {key} differs"
                )
            raw_values = raw_spec["choices"]
        else:
            raw_values = raw_spec
        choices[key] = _manifest_scalar_list(
            raw_values, f"AgentHPO runner choices for {key}"
        )
    if not choices:
        raise AgentHPOInterventionError("AgentHPO runner search space is empty")
    return choices


def _task_runner_path(root: Path, task_id: str) -> str:
    task_root = root / "tasks" / "main" / task_id
    if _path_has_symlink(task_root):
        raise AgentHPOInterventionError("AgentHPO task directory may not contain symlinks")
    try:
        task_root = task_root.resolve(strict=True)
    except OSError as exc:
        raise AgentHPOInterventionError("AgentHPO task directory is missing") from exc
    if task_root != root / "tasks" / "main" / task_id or not task_root.is_dir():
        raise AgentHPOInterventionError("AgentHPO task directory differs")
    candidates = sorted(
        path
        for path in task_root.glob("run_formal_*.py")
        if "agent" in path.name and path.is_file() and not path.is_symlink()
    )
    if len(candidates) != 1:
        raise AgentHPOInterventionError(
            "AgentHPO task must have exactly one formal agent runner"
        )
    return candidates[0].relative_to(root).as_posix()


@dataclass(frozen=True)
class AgentHPOSpaceSourceReceipt:
    """Zero-call evidence for one mechanically derived scalar search space.

    The receipt names the exact upstream git tree, ``space_manifest.json``,
    ablation backend, task runner, selected variant, and the two independently
    derived projections.  It grants no model/evaluator entitlement.
    """

    task_id: str
    space_variant: str
    source_git_commit: str
    source_root_tree: str
    source_manifest_path: str
    source_manifest_sha256: str
    space_backend_path: str
    space_backend_sha256: str
    task_runner_path: str
    task_runner_sha256: str
    task_source_sha256: str
    task_space_projection_sha256: str
    intervention_space_sha256: str
    current_config_sha256: str
    previous_outcome_sha256: str
    derivation_status: str = "MECHANICALLY_DERIVED_ZERO_CALL"
    execution_authority: str = "NOT_GRANTED"
    schema_version: int = 1
    artifact_kind: str = "agenthpobench_space_source_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.artifact_kind != (
            "agenthpobench_space_source_receipt_v1"
        ):
            raise AgentHPOInterventionError("unsupported space-source receipt")
        _safe(self.task_id, "space-source task id")
        if self.space_variant not in _SPACE_VARIANTS:
            raise AgentHPOInterventionError("unsupported AgentHPO space variant")
        if (
            self.source_git_commit != _PINNED_AGENTHPO_COMMIT
            or self.source_root_tree != _PINNED_AGENTHPO_ROOT_TREE
            or self.source_manifest_path != _PINNED_SPACE_MANIFEST_PATH
            or self.source_manifest_sha256 != _PINNED_SPACE_MANIFEST_SHA256
            or self.space_backend_path != _PINNED_SPACE_BACKEND_PATH
            or self.space_backend_sha256 != _PINNED_SPACE_BACKEND_SHA256
        ):
            raise AgentHPOInterventionError("space-source pin differs")
        if not re.fullmatch(r"[0-9a-f]{40}", self.source_git_commit) or not re.fullmatch(
            r"[0-9a-f]{40}", self.source_root_tree
        ):
            raise AgentHPOInterventionError("invalid AgentHPO git source identity")
        if (
            Path(self.task_runner_path).is_absolute()
            or ".." in Path(self.task_runner_path).parts
            or self.task_runner_path
            != f"tasks/main/{self.task_id}/{Path(self.task_runner_path).name}"
        ):
            raise AgentHPOInterventionError("space-source task runner path differs")
        for value, label, allow_zero in (
            (self.task_runner_sha256, "task runner sha256", False),
            (self.task_source_sha256, "task source sha256", False),
            (self.task_space_projection_sha256, "task space projection sha256", False),
            (self.intervention_space_sha256, "intervention-space sha256", False),
            (self.current_config_sha256, "current configuration sha256", False),
            (self.previous_outcome_sha256, "previous outcome sha256", True),
        ):
            _sha(value, label, allow_zero=allow_zero)
        if (
            self.derivation_status != "MECHANICALLY_DERIVED_ZERO_CALL"
            or self.execution_authority != "NOT_GRANTED"
        ):
            raise AgentHPOInterventionError(
                "space-source receipt may not grant execution authority"
            )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_canonical_bytes(cls, raw: bytes) -> "AgentHPOSpaceSourceReceipt":
        payload = _parse_canonical_object(raw, label="space-source receipt")
        _exact_fields(
            payload,
            {field.name for field in cls.__dataclass_fields__.values()},
            label="space-source receipt",
        )
        item = cls(**payload)
        if item.canonical_bytes != raw:
            raise AgentHPOInterventionError("space-source receipt replay differs")
        return item


def _verify_manifest_and_project(
    manifest_raw: bytes,
    *,
    task_id: str,
    space_variant: str,
) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    try:
        payload = json.loads(
            manifest_raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicates,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AgentHPOInterventionError(
            "pinned AgentHPO space manifest is not strict JSON"
        ) from exc
    if not isinstance(payload, dict) or set(payload) != _MANIFEST_TOP_FIELDS:
        raise AgentHPOInterventionError("pinned AgentHPO space manifest fields differ")
    if payload["all_nested"] is not True or payload["task_count"] != 30:
        raise AgentHPOInterventionError("pinned AgentHPO space manifest summary differs")
    tasks = payload["tasks"]
    if not isinstance(tasks, dict) or len(tasks) != 30 or task_id not in tasks:
        raise AgentHPOInterventionError("AgentHPO task is absent from pinned space manifest")
    task_node = tasks[task_id]
    if not isinstance(task_node, dict):
        raise AgentHPOInterventionError("AgentHPO task-space manifest entry differs")
    if "special_space" in task_node:
        # ``agent_lightning_room_selector`` is a free-form prompt intervention.
        # Converting it into a scalar allowlist would alter the benchmark action
        # semantics, so this scalar codec must fail before any request/evaluation.
        raise AgentHPOInterventionError(
            "AgentHPO task uses an unsupported free-form prompt intervention"
        )
    if set(task_node) != {"nested", "parameters"} or task_node["nested"] is not True:
        raise AgentHPOInterventionError("AgentHPO scalar task-space fields differ")
    parameters = task_node["parameters"]
    if not isinstance(parameters, dict) or not parameters:
        raise AgentHPOInterventionError("AgentHPO scalar task space is empty")
    baseline: dict[str, object] = {}
    original: dict[str, object] = {}
    selected: dict[str, object] = {}
    for key in sorted(parameters):
        _safe(key, "AgentHPO manifest parameter key")
        parameter = parameters[key]
        if not isinstance(parameter, dict) or set(parameter) != (
            _MANIFEST_PARAMETER_FIELDS
        ):
            raise AgentHPOInterventionError(
                f"AgentHPO manifest parameter fields differ for {key}"
            )
        if parameter["nested"] is not True:
            raise AgentHPOInterventionError(
                f"AgentHPO manifest parameter is not nested for {key}"
            )
        base = _typed_manifest_scalar(parameter["baseline"], f"baseline {key}")
        original_values = _manifest_scalar_list(
            parameter["original"], f"original {key}"
        )
        selected_values = _manifest_scalar_list(
            parameter[space_variant], f"{space_variant} {key}"
        )
        if not any(_same_manifest_scalar(base, item) for item in original_values):
            raise AgentHPOInterventionError(
                f"AgentHPO manifest baseline is outside original space for {key}"
            )
        if not any(_same_manifest_scalar(base, item) for item in selected_values):
            raise AgentHPOInterventionError(
                f"AgentHPO manifest baseline is outside selected space for {key}"
            )
        if space_variant != "original" and not all(
            any(_same_manifest_scalar(item, candidate) for candidate in selected_values)
            for item in original_values
        ) and space_variant == "wide":
            raise AgentHPOInterventionError(
                f"AgentHPO wide space does not contain original values for {key}"
            )
        baseline[key] = base
        original[key] = original_values
        selected[key] = selected_values
    return baseline, original, selected


def derive_pinned_discrete_intervention_space(
    source_root: str | Path,
    *,
    task_id: str,
    space_variant: str,
    current_config: Mapping[str, object] | None,
    previous_outcome_sha256: str,
) -> tuple[
    DiscreteInterventionSpace, InterventionSpaceBinding, AgentHPOSpaceSourceReceipt
]:
    """Derive an exact scalar space from the frozen AgentHPO git checkout.

    This is a zero-call, read-only operation.  It hashes and parses the pinned
    upstream manifest and task runner; the caller supplies neither a projection
    digest nor an allowlist.  For v001, pass ``current_config=None`` and the
    all-zero previous-outcome digest.  A later round must pass the complete
    previous accepted ``StrictIntervention.resulting_config`` together with the
    content hash of that immutable previous outcome.

    ``agent_lightning_room_selector`` deliberately fails here because its
    upstream action is a free-form prompt intervention, not a scalar discrete
    configuration.  It needs a separately preregistered codec or a fresh split.
    """

    _safe(task_id, "AgentHPO task id")
    if space_variant not in _SPACE_VARIANTS:
        raise AgentHPOInterventionError("unsupported AgentHPO space variant")
    _sha(previous_outcome_sha256, "previous outcome sha256", allow_zero=True)
    root = Path(source_root)
    if not root.is_absolute():
        raise AgentHPOInterventionError("AgentHPO source root must be absolute")
    if _path_has_symlink(root):
        raise AgentHPOInterventionError("AgentHPO source root may not contain symlinks")
    try:
        resolved = root.resolve(strict=True)
    except OSError as exc:
        raise AgentHPOInterventionError("AgentHPO source root does not resolve") from exc
    if resolved != root or not resolved.is_dir():
        raise AgentHPOInterventionError(
            "AgentHPO source root is not its explicit real directory"
        )
    if _git_output(root, "rev-parse", "HEAD^{commit}") != _PINNED_AGENTHPO_COMMIT:
        raise AgentHPOInterventionError("pinned AgentHPO source commit drifted")
    if _git_output(root, "rev-parse", "HEAD^{tree}") != _PINNED_AGENTHPO_ROOT_TREE:
        raise AgentHPOInterventionError("pinned AgentHPO source tree drifted")
    _require_clean_tracked_source(root)

    manifest_raw = _read_bound_source_file(root, _PINNED_SPACE_MANIFEST_PATH)
    if hashlib.sha256(manifest_raw).hexdigest() != _PINNED_SPACE_MANIFEST_SHA256:
        raise AgentHPOInterventionError("pinned AgentHPO space manifest hash drifted")
    backend_raw = _read_bound_source_file(root, _PINNED_SPACE_BACKEND_PATH)
    if hashlib.sha256(backend_raw).hexdigest() != _PINNED_SPACE_BACKEND_SHA256:
        raise AgentHPOInterventionError("pinned AgentHPO space backend hash drifted")
    try:
        ast.parse(backend_raw)
    except (SyntaxError, ValueError) as exc:
        raise AgentHPOInterventionError("pinned AgentHPO space backend is invalid") from exc

    manifest_baseline, manifest_original, selected = _verify_manifest_and_project(
        manifest_raw,
        task_id=task_id,
        space_variant=space_variant,
    )
    runner_path = _task_runner_path(root, task_id)
    runner_raw = _read_bound_source_file(root, runner_path)
    runner_blob_sha1 = _git_output(root, "rev-parse", f"HEAD:{runner_path}")
    observed_blob_sha1 = _git_output(root, "hash-object", runner_path)
    if (
        not re.fullmatch(r"[0-9a-f]{40}", runner_blob_sha1)
        or observed_blob_sha1 != runner_blob_sha1
    ):
        raise AgentHPOInterventionError("pinned AgentHPO task runner hash drifted")
    runner_baseline, runner_search_space = _extract_runner_literals(runner_raw)
    runner_original = _runner_choices(runner_search_space)
    if set(runner_original) != set(manifest_original):
        raise AgentHPOInterventionError(
            "AgentHPO runner and manifest parameter fields differ"
        )
    for key in sorted(manifest_original):
        runner_values = runner_original[key]
        manifest_values = manifest_original[key]
        if len(runner_values) != len(manifest_values) or any(
            not _same_manifest_scalar(left, right)
            for left, right in zip(runner_values, manifest_values)
        ):
            raise AgentHPOInterventionError(
                f"AgentHPO runner original space differs from manifest for {key}"
            )
        if key not in runner_baseline or not _same_manifest_scalar(
            runner_baseline[key], manifest_baseline[key]
        ):
            raise AgentHPOInterventionError(
                f"AgentHPO runner baseline differs from manifest for {key}"
            )

    # Runner configs may contain fixed, non-search fields.  They are not part
    # of the intervention action and therefore cannot be silently introduced
    # into the derived mutable configuration.
    if current_config is None:
        if previous_outcome_sha256 != _ZERO_SHA256:
            raise AgentHPOInterventionError(
                "initial AgentHPO space cannot reference a previous outcome"
            )
        effective_current = manifest_baseline
    else:
        if previous_outcome_sha256 == _ZERO_SHA256:
            raise AgentHPOInterventionError(
                "later AgentHPO space requires its previous outcome hash"
            )
        if not isinstance(current_config, Mapping) or set(current_config) != set(
            selected
        ):
            raise AgentHPOInterventionError(
                "current AgentHPO configuration fields differ from derived space"
            )
        effective_current = {
            key: _typed_manifest_scalar(current_config[key], f"current {key}")
            for key in sorted(current_config)
        }
        for key, value in effective_current.items():
            if not any(
                _same_manifest_scalar(value, candidate)
                for candidate in selected[key]  # type: ignore[index]
            ):
                raise AgentHPOInterventionError(
                    f"current AgentHPO value is outside derived space for {key}"
                )

    typed_allowed: dict[
        str, tuple[None | bool | int | float | str, ...]
    ] = {}
    for key, values in selected.items():
        typed_allowed[key] = tuple(values)
    typed_current = dict(effective_current)  # type: ignore[arg-type]

    runner_sha = hashlib.sha256(runner_raw).hexdigest()
    task_source_projection = {
        "source_git_commit": _PINNED_AGENTHPO_COMMIT,
        "source_root_tree": _PINNED_AGENTHPO_ROOT_TREE,
        "space_backend_path": _PINNED_SPACE_BACKEND_PATH,
        "space_backend_sha256": _PINNED_SPACE_BACKEND_SHA256,
        "source_manifest_path": _PINNED_SPACE_MANIFEST_PATH,
        "source_manifest_sha256": _PINNED_SPACE_MANIFEST_SHA256,
        "task_id": task_id,
        "task_runner_path": runner_path,
        "task_runner_sha256": runner_sha,
    }
    task_source_sha256 = hashlib.sha256(
        _canonical_bytes(task_source_projection)
    ).hexdigest()
    task_space_projection = {
        "baseline": manifest_baseline,
        "original": manifest_original,
        "selected": selected,
        "space_variant": space_variant,
        "task_id": task_id,
        "task_source_sha256": task_source_sha256,
    }
    task_space_projection_sha256 = hashlib.sha256(
        _canonical_bytes(task_space_projection)
    ).hexdigest()
    space = DiscreteInterventionSpace(
        task_id=task_id,
        task_source_sha256=task_source_sha256,
        current_config=typed_current,
        allowed_values=typed_allowed,
    )
    binding = InterventionSpaceBinding.create(
        space=space,
        expected_task_id=task_id,
        expected_task_source_sha256=task_source_sha256,
        expected_source_manifest_sha256=_PINNED_SPACE_MANIFEST_SHA256,
        expected_task_space_projection_sha256=task_space_projection_sha256,
        previous_outcome_sha256=previous_outcome_sha256,
    )
    receipt = AgentHPOSpaceSourceReceipt(
        task_id=task_id,
        space_variant=space_variant,
        source_git_commit=_PINNED_AGENTHPO_COMMIT,
        source_root_tree=_PINNED_AGENTHPO_ROOT_TREE,
        source_manifest_path=_PINNED_SPACE_MANIFEST_PATH,
        source_manifest_sha256=_PINNED_SPACE_MANIFEST_SHA256,
        space_backend_path=_PINNED_SPACE_BACKEND_PATH,
        space_backend_sha256=_PINNED_SPACE_BACKEND_SHA256,
        task_runner_path=runner_path,
        task_runner_sha256=runner_sha,
        task_source_sha256=task_source_sha256,
        task_space_projection_sha256=task_space_projection_sha256,
        intervention_space_sha256=space.sha256,
        current_config_sha256=hashlib.sha256(
            _canonical_bytes(dict(sorted(space.current_config.items())))
        ).hexdigest(),
        previous_outcome_sha256=previous_outcome_sha256,
    )
    return space, binding, receipt


@dataclass(frozen=True)
class DiscreteInterventionSpace:
    """Controller-derived exact discrete action space for one task and round."""

    task_id: str
    task_source_sha256: str
    current_config: Mapping[str, None | bool | int | float | str]
    allowed_values: Mapping[str, tuple[None | bool | int | float | str, ...]]
    schema_version: int = 1
    contract_kind: str = "agenthpobench_discrete_intervention_space_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.contract_kind != (
            "agenthpobench_discrete_intervention_space_v1"
        ):
            raise AgentHPOInterventionError("unsupported intervention-space schema")
        _safe(self.task_id, "AgentHPOBench task id")
        _sha(self.task_source_sha256, "task source sha256")
        if not isinstance(self.current_config, Mapping) or not isinstance(
            self.allowed_values, Mapping
        ):
            raise AgentHPOInterventionError("intervention space mappings are required")
        if not self.current_config or set(self.current_config) != set(
            self.allowed_values
        ):
            raise AgentHPOInterventionError(
                "current configuration and allowed-value fields differ"
            )
        current: dict[str, None | bool | int | float | str] = {}
        allowed: dict[str, tuple[None | bool | int | float | str, ...]] = {}
        for key in sorted(self.current_config):
            _safe(key, "hyperparameter key")
            value = _typed_scalar(self.current_config[key], f"current {key}")
            candidates = self.allowed_values[key]
            if (
                not isinstance(candidates, tuple)
                or not candidates
                or len(candidates) > 256
            ):
                raise AgentHPOInterventionError(
                    f"allowed values for {key} must be a non-empty bounded tuple"
                )
            normalized = tuple(
                _typed_scalar(item, f"allowed {key}") for item in candidates
            )
            concrete_types = {type(item) for item in normalized if item is not None}
            if len(concrete_types) > 1:
                raise AgentHPOInterventionError(
                    f"allowed values for {key} change the baseline scalar type"
                )
            if len({(type(item).__name__, repr(item)) for item in normalized}) != len(
                normalized
            ):
                raise AgentHPOInterventionError(
                    f"allowed values for {key} contain duplicates"
                )
            if not any(_same_typed_scalar(value, item) for item in normalized):
                raise AgentHPOInterventionError(
                    f"current value for {key} is outside its allowed set"
                )
            current[key] = value
            allowed[key] = normalized
        object.__setattr__(self, "current_config", MappingProxyType(current))
        object.__setattr__(self, "allowed_values", MappingProxyType(allowed))

    def to_dict(self) -> dict[str, Any]:
        return {
            "allowed_values": {
                key: list(self.allowed_values[key]) for key in sorted(self.allowed_values)
            },
            "contract_kind": self.contract_kind,
            "current_config": dict(sorted(self.current_config.items())),
            "schema_version": self.schema_version,
            "task_id": self.task_id,
            "task_source_sha256": self.task_source_sha256,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_canonical_bytes(cls, raw: bytes) -> "DiscreteInterventionSpace":
        payload = _parse_canonical_object(raw, label="intervention space")
        _exact_fields(
            payload,
            {
                "allowed_values",
                "contract_kind",
                "current_config",
                "schema_version",
                "task_id",
                "task_source_sha256",
            },
            label="intervention space",
        )
        allowed = payload["allowed_values"]
        if not isinstance(allowed, dict):
            raise AgentHPOInterventionError("intervention allowed values differ")
        item = cls(
            task_id=payload["task_id"],
            task_source_sha256=payload["task_source_sha256"],
            current_config=payload["current_config"],
            allowed_values={key: tuple(values) for key, values in allowed.items()},
            schema_version=payload["schema_version"],
            contract_kind=payload["contract_kind"],
        )
        if item.canonical_bytes != raw:
            raise AgentHPOInterventionError("intervention-space replay differs")
        return item


@dataclass(frozen=True)
class InterventionSpaceBinding:
    """Pinned provenance for a mechanically derived AgentHPO search space.

    This does not derive a space by itself.  A future formal provider must
    verify the checked-in AgentHPO source/space manifest and then seal this
    binding before the strict codec is usable.  The explicit previous outcome
    link prevents a caller from silently replacing the current configuration
    in later rounds.
    """

    task_id: str
    task_source_sha256: str
    source_manifest_sha256: str
    task_space_projection_sha256: str
    intervention_space_sha256: str
    current_config_sha256: str
    previous_outcome_sha256: str
    derivation_kind: str = "agenthpobench_pinned_discrete_space_projection_v1"
    schema_version: int = 1

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.derivation_kind != (
            "agenthpobench_pinned_discrete_space_projection_v1"
        ):
            raise AgentHPOInterventionError("unsupported space-binding schema")
        _safe(self.task_id, "space-binding task id")
        for value, label, allow_zero in (
            (self.task_source_sha256, "task source sha256", False),
            (self.source_manifest_sha256, "source manifest sha256", False),
            (self.task_space_projection_sha256, "task space projection sha256", False),
            (self.intervention_space_sha256, "intervention-space sha256", False),
            (self.current_config_sha256, "current configuration sha256", False),
            (self.previous_outcome_sha256, "previous outcome sha256", True),
        ):
            _sha(value, label, allow_zero=allow_zero)

    @classmethod
    def create(
        cls,
        *,
        space: DiscreteInterventionSpace,
        expected_task_id: str,
        expected_task_source_sha256: str,
        expected_source_manifest_sha256: str,
        expected_task_space_projection_sha256: str,
        previous_outcome_sha256: str,
    ) -> "InterventionSpaceBinding":
        if not isinstance(space, DiscreteInterventionSpace):
            raise AgentHPOInterventionError("typed intervention space is required")
        if space.task_id != expected_task_id:
            raise AgentHPOInterventionError("space task id differs from trusted source")
        if space.task_source_sha256 != expected_task_source_sha256:
            raise AgentHPOInterventionError(
                "space task source differs from trusted source"
            )
        return cls(
            task_id=space.task_id,
            task_source_sha256=space.task_source_sha256,
            source_manifest_sha256=expected_source_manifest_sha256,
            task_space_projection_sha256=expected_task_space_projection_sha256,
            intervention_space_sha256=space.sha256,
            current_config_sha256=hashlib.sha256(
                _canonical_bytes(dict(sorted(space.current_config.items())))
            ).hexdigest(),
            previous_outcome_sha256=previous_outcome_sha256,
        )

    def verify_space(
        self,
        space: DiscreteInterventionSpace,
        *,
        expected_task_id: str,
        expected_task_source_sha256: str,
        expected_source_manifest_sha256: str,
        expected_task_space_projection_sha256: str,
        expected_previous_outcome_sha256: str,
    ) -> None:
        expected = type(self).create(
            space=space,
            expected_task_id=expected_task_id,
            expected_task_source_sha256=expected_task_source_sha256,
            expected_source_manifest_sha256=expected_source_manifest_sha256,
            expected_task_space_projection_sha256=(
                expected_task_space_projection_sha256
            ),
            previous_outcome_sha256=expected_previous_outcome_sha256,
        )
        if self != expected:
            raise AgentHPOInterventionError(
                "intervention space binding differs from trusted derivation"
            )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class StrictIntervention:
    """Accepted exact proposal and the complete resulting configuration."""

    task_id: str
    intervention_space_sha256: str
    raw_response_sha256: str
    proposed_changes: Mapping[str, None | bool | int | float | str]
    resulting_config: Mapping[str, None | bool | int | float | str]
    schema_version: int = 1
    artifact_kind: str = "agenthpobench_strict_intervention_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.artifact_kind != (
            "agenthpobench_strict_intervention_v1"
        ):
            raise AgentHPOInterventionError("unsupported strict-intervention schema")
        _safe(self.task_id, "AgentHPOBench task id")
        _sha(self.intervention_space_sha256, "intervention-space sha256")
        _sha(self.raw_response_sha256, "raw response sha256")
        if not self.proposed_changes:
            raise AgentHPOInterventionError("strict intervention has no changes")
        proposed = {
            _safe(key, "proposed hyperparameter key"): _typed_scalar(
                value, f"proposed {key}"
            )
            for key, value in self.proposed_changes.items()
        }
        resulting = {
            _safe(key, "resulting hyperparameter key"): _typed_scalar(
                value, f"resulting {key}"
            )
            for key, value in self.resulting_config.items()
        }
        object.__setattr__(self, "proposed_changes", MappingProxyType(proposed))
        object.__setattr__(self, "resulting_config", MappingProxyType(resulting))

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_kind": self.artifact_kind,
            "intervention_space_sha256": self.intervention_space_sha256,
            "proposed_changes": dict(sorted(self.proposed_changes.items())),
            "raw_response_sha256": self.raw_response_sha256,
            "resulting_config": dict(sorted(self.resulting_config.items())),
            "schema_version": self.schema_version,
            "task_id": self.task_id,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_canonical_bytes(cls, raw: bytes) -> "StrictIntervention":
        payload = _parse_canonical_object(raw, label="strict intervention")
        _exact_fields(
            payload,
            {
                "artifact_kind",
                "intervention_space_sha256",
                "proposed_changes",
                "raw_response_sha256",
                "resulting_config",
                "schema_version",
                "task_id",
            },
            label="strict intervention",
        )
        item = cls(**payload)
        if item.canonical_bytes != raw:
            raise AgentHPOInterventionError("strict-intervention replay differs")
        return item


def parse_strict_intervention(
    raw_response: bytes,
    *,
    space: DiscreteInterventionSpace,
    allow_explicit_keep: bool = False,
) -> StrictIntervention:
    """Accept a subset proposal only when every value is exact and changes state.

    There are no aliases, nearest-value conversion, unknown-key filtering, or
    keep-current fallback. A valid unchanged proposal may be accepted as an
    explicit keep when ``allow_explicit_keep`` is enabled; parser failures are
    never converted into keeps.
    """

    if not isinstance(space, DiscreteInterventionSpace):
        raise AgentHPOInterventionError("typed intervention space is required")
    payload = _parse_one_object(raw_response)
    if not payload:
        raise AgentHPOInterventionError("strict intervention is empty")
    unknown = set(payload) - set(space.allowed_values)
    if unknown:
        raise AgentHPOInterventionError(
            "strict intervention contains unknown keys: " + ",".join(sorted(unknown))
        )
    proposed: dict[str, None | bool | int | float | str] = {}
    for key in sorted(payload):
        value = _typed_scalar(payload[key], f"proposed {key}")
        current = space.current_config[key]
        if not any(
            _same_typed_scalar(value, candidate)
            for candidate in space.allowed_values[key]
        ):
            if (
                value is not None
                and current is not None
                and type(value) is not type(current)
            ):
                raise AgentHPOInterventionError(
                    f"strict intervention changes the scalar type for {key}"
                )
            raise AgentHPOInterventionError(
                f"strict intervention value for {key} is outside the allowlist"
            )
        proposed[key] = value
    resulting = dict(space.current_config)
    resulting.update(proposed)
    if not allow_explicit_keep and all(
        _same_typed_scalar(resulting[key], space.current_config[key])
        for key in resulting
    ):
        raise AgentHPOInterventionError(
            "strict intervention makes no operational configuration change"
        )
    return StrictIntervention(
        task_id=space.task_id,
        intervention_space_sha256=space.sha256,
        raw_response_sha256=hashlib.sha256(raw_response).hexdigest(),
        proposed_changes=proposed,
        resulting_config=resulting,
    )


@dataclass(frozen=True)
class ProviderRequestReceipt:
    """One actual provider request; one receipt consumes one request entitlement."""

    decision_operation_id: str
    request_index: int
    provider: str
    model: str
    request_payload_sha256: str
    response_artifact_sha256: str
    usage_artifact_sha256: str
    terminal_status: str
    provider_request_debit: int = 1
    schema_version: int = 1
    receipt_kind: str = "agenthpobench_provider_request_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "agenthpobench_provider_request_receipt_v1"
        ):
            raise AgentHPOInterventionError("unsupported provider-request receipt")
        for value, label in (
            (self.decision_operation_id, "decision operation id"),
            (self.provider, "provider"),
            (self.model, "model"),
        ):
            _safe(value, label)
        if type(self.request_index) is not int or self.request_index < 1:
            raise AgentHPOInterventionError("provider request index must be positive")
        if self.provider_request_debit != 1:
            raise AgentHPOInterventionError(
                "every actual provider request must debit exactly one request"
            )
        _sha(self.request_payload_sha256, "request payload sha256")
        if self.terminal_status not in _TERMINAL_REQUEST_STATUSES:
            raise AgentHPOInterventionError("provider request status is not terminal")
        if self.terminal_status == "COMPLETED":
            _sha(self.response_artifact_sha256, "response artifact sha256")
            _sha(self.usage_artifact_sha256, "usage artifact sha256")
        else:
            _sha(
                self.response_artifact_sha256,
                "failed response artifact sha256",
                allow_zero=True,
            )
            _sha(
                self.usage_artifact_sha256,
                "failed usage artifact sha256",
                allow_zero=True,
            )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_canonical_bytes(cls, raw: bytes) -> "ProviderRequestReceipt":
        payload = _parse_canonical_object(raw, label="provider-request receipt")
        _exact_fields(
            payload,
            {field.name for field in cls.__dataclass_fields__.values()},
            label="provider-request receipt",
        )
        item = cls(**payload)
        if item.canonical_bytes != raw:
            raise AgentHPOInterventionError("provider-request receipt replay differs")
        return item


@dataclass(frozen=True)
class DecisionOperationReceipt:
    """Terminal one-logical-call receipt with exact underlying request count."""

    decision_operation_id: str
    intervention_space_sha256: str
    provider_request_receipt_sha256s: tuple[str, ...]
    terminal_status: str
    intervention_sha256: str
    logical_model_call_debit: int = 1
    provider_request_debit: int = 1
    schema_version: int = 1
    receipt_kind: str = "agenthpobench_decision_operation_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "agenthpobench_decision_operation_receipt_v1"
        ):
            raise AgentHPOInterventionError("unsupported decision-operation receipt")
        _safe(self.decision_operation_id, "decision operation id")
        _sha(self.intervention_space_sha256, "intervention-space sha256")
        if self.terminal_status not in _TERMINAL_REQUEST_STATUSES:
            raise AgentHPOInterventionError("decision operation status is not terminal")
        if self.logical_model_call_debit != 1 or self.provider_request_debit != 1:
            raise AgentHPOInterventionError(
                "decision operation debit must be one logical and one provider call"
            )
        if len(self.provider_request_receipt_sha256s) != 1:
            raise AgentHPOInterventionError(
                "decision operation must bind exactly one provider request"
            )
        _sha(
            self.provider_request_receipt_sha256s[0],
            "provider request receipt sha256",
        )
        _sha(
            self.intervention_sha256,
            "intervention sha256",
            allow_zero=self.terminal_status == "FAILED",
        )
        if self.terminal_status == "FAILED":
            if self.intervention_sha256 != _ZERO_SHA256:
                raise AgentHPOInterventionError(
                    "failed decision operation cannot bind an intervention"
                )
        elif self.intervention_sha256 == _ZERO_SHA256:
            raise AgentHPOInterventionError(
                "completed decision operation requires an intervention"
            )

    @classmethod
    def seal(
        cls,
        *,
        request: ProviderRequestReceipt,
        space: DiscreteInterventionSpace,
        raw_response: bytes | None,
        intervention: StrictIntervention | None,
        allow_explicit_keep: bool = False,
    ) -> "DecisionOperationReceipt":
        if not isinstance(request, ProviderRequestReceipt):
            raise AgentHPOInterventionError("typed provider-request receipt is required")
        if not isinstance(space, DiscreteInterventionSpace):
            raise AgentHPOInterventionError("typed intervention space is required")
        if request.request_index != 1:
            raise AgentHPOInterventionError(
                "decision operation must begin with provider request index one"
            )
        if request.terminal_status == "COMPLETED":
            if not isinstance(intervention, StrictIntervention):
                raise AgentHPOInterventionError(
                    "completed provider request requires a strict intervention"
                )
            if not isinstance(raw_response, bytes):
                raise AgentHPOInterventionError(
                    "completed provider request requires raw response bytes"
                )
            replayed = parse_strict_intervention(
                raw_response,
                space=space,
                allow_explicit_keep=allow_explicit_keep,
            )
            if replayed != intervention:
                raise AgentHPOInterventionError(
                    "strict intervention differs from trusted codec replay"
                )
            if replayed.raw_response_sha256 != request.response_artifact_sha256:
                raise AgentHPOInterventionError(
                    "intervention response differs from the provider receipt"
                )
            intervention_sha256 = intervention.sha256
        else:
            if intervention is not None or raw_response is not None:
                raise AgentHPOInterventionError(
                    "failed provider request cannot produce response or intervention"
                )
            intervention_sha256 = _ZERO_SHA256
        return cls(
            decision_operation_id=request.decision_operation_id,
            intervention_space_sha256=space.sha256,
            provider_request_receipt_sha256s=(request.sha256,),
            terminal_status=request.terminal_status,
            intervention_sha256=intervention_sha256,
        )

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["provider_request_receipt_sha256s"] = list(
            self.provider_request_receipt_sha256s
        )
        return payload

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_canonical_bytes(cls, raw: bytes) -> "DecisionOperationReceipt":
        payload = _parse_canonical_object(raw, label="decision-operation receipt")
        _exact_fields(
            payload,
            {field.name for field in cls.__dataclass_fields__.values()},
            label="decision-operation receipt",
        )
        values = dict(payload)
        values["provider_request_receipt_sha256s"] = tuple(
            values["provider_request_receipt_sha256s"]
        )
        item = cls(**values)
        if item.canonical_bytes != raw:
            raise AgentHPOInterventionError("decision-operation receipt replay differs")
        return item


def verify_decision_operation(
    *,
    operation: DecisionOperationReceipt,
    request_receipts: Sequence[ProviderRequestReceipt],
    space: DiscreteInterventionSpace,
    raw_response: bytes | None,
    intervention: StrictIntervention | None,
    allow_explicit_keep: bool = False,
) -> None:
    """Replay submitted request/operation artifacts.

    Sequence cardinality prevents a caller from *submitting* multiple requests
    as one logical call.  It cannot prove that a request was omitted.  Formal
    execution therefore remains blocked until the sole trusted transport owns
    an append-only reserve/start/terminal ledger and disables provider/SDK
    internal retries.
    """

    if not isinstance(operation, DecisionOperationReceipt):
        raise AgentHPOInterventionError("typed decision-operation receipt is required")
    if (
        not isinstance(request_receipts, Sequence)
        or isinstance(request_receipts, (str, bytes))
        or len(request_receipts) != 1
        or not isinstance(request_receipts[0], ProviderRequestReceipt)
    ):
        raise AgentHPOInterventionError(
            "formal decision replay requires exactly one provider-request receipt"
        )
    request = request_receipts[0]
    if request.request_index != 1:
        raise AgentHPOInterventionError(
            "formal decision replay starts with provider request index one"
        )
    expected = DecisionOperationReceipt.seal(
        request=request,
        space=space,
        raw_response=raw_response,
        intervention=intervention,
        allow_explicit_keep=allow_explicit_keep,
    )
    if expected != operation:
        raise AgentHPOInterventionError("decision-operation replay differs")


__all__ = [
    "AgentHPOSpaceSourceReceipt",
    "AgentHPOInterventionError",
    "DecisionOperationReceipt",
    "DiscreteInterventionSpace",
    "InterventionSpaceBinding",
    "ProviderRequestReceipt",
    "StrictIntervention",
    "derive_pinned_discrete_intervention_space",
    "parse_strict_intervention",
    "verify_decision_operation",
]
