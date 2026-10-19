"""Bounded, content-addressed mechanisms for B-online meta evolution.

This module deliberately does *not* execute generated code or store natural-language
instructions.  It is a small trusted state machine inspired by self-modifying agent
systems: a sealed task may advance exactly one of three independently addressable
mechanisms:

``M``
    The existing Experience Bank / memory object.
``P``
    A typed policy for selecting trusted Harness components and archive parents.
``A``
    A public-metric-only archive graph of previously compiled Harnesses.

The model may propose values accepted by these schemas, but it cannot add executable
components, prompts, evaluators, scorers, budgets, private observations, or code.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import stat
import tempfile
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence, TypeVar

from .experience import ExperienceRecord
from .learning import ExperienceBankSnapshot


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_PRIVATE_OR_FUTURE = re.compile(
    r"(?:/home/|/data\d*/|(?:^|[/:_.+\-])(?:private|hidden|future)"
    r"(?:$|[/:_.+\-]))",
    re.IGNORECASE,
)
_FORBIDDEN_COMPONENT_CONTROL = re.compile(
    r"(?:^|[/:_.+\-])(?:code|prompt|evaluator|scorer|budget|private|hidden|future)"
    r"(?:$|[/:_.+\-])",
    re.IGNORECASE,
)

MECHANISMS = ("M", "P", "A")
COMPONENT_AXES = (
    "role_graph",
    "memory_views",
    "tools",
    "parent_strategy",
    "workflow",
    "scheduler_mode",
    "recovery_mode",
)
METRIC_NAMES = ("quality", "novelty", "recovery", "efficiency")

_DEFAULT_COMPONENTS: Mapping[str, tuple[str, ...]] = MappingProxyType(
    {
        "role_graph": (
            "task_analyst",
            "performance_analyst",
            "compiler_analyst",
            "critic",
            "generator",
            "verifier",
        ),
        "memory_views": (
            "current",
            "best",
            "failures",
            "structural_diverse",
            "cross_instance_records",
        ),
        "tools": (
            "task_semantics",
            "score_history",
            "static_structure",
            "public_profile",
            "compiler_observation",
            "code_diff",
        ),
        "parent_strategy": (
            "reference",
            "incumbent",
            "stable_best",
            "restart",
            "recombine",
        ),
        "workflow": (
            "analyze",
            "select_parent",
            "inspect",
            "hypothesize",
            "criticize",
            "generate",
            "verify_contract",
        ),
        "scheduler_mode": (
            "single_candidate",
            "repair_first",
            "explore_then_exploit",
        ),
        "recovery_mode": (
            "repair_then_reset",
            "reset_immediately",
            "preserve_failure",
        ),
    }
)

_SELECTION_MODES = frozenset(
    {"weighted_rank_v1", "failure_directed_v1", "pareto_diverse_v1"}
)
_RETRIEVAL_MODES = frozenset(
    {"descriptor_overlap_v1", "failure_match_v1", "cross_benchmark_v1"}
)
_ARCHIVE_MODES = frozenset(
    {"score_frontier_v1", "lineage_diverse_v1", "best_per_structure_v1"}
)

_MAX_CONTENT_ADDRESSED_BYTES = 64 * 1024 * 1024
_ContentAddressedT = TypeVar("_ContentAddressedT", bound="_ContentAddressed")


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _require_fields(
    payload: Mapping[str, Any], expected: frozenset[str], label: str
) -> None:
    if not isinstance(payload, Mapping):
        raise ValueError(f"{label} must be an object")
    actual = frozenset(payload)
    if actual != expected:
        raise ValueError(
            f"{label} fields differ: "
            f"missing={sorted(expected - actual)}, extra={sorted(actual - expected)}"
        )


def _public_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not _SAFE_ID.fullmatch(value):
        raise ValueError(f"unsafe {label}")
    if _PRIVATE_OR_FUTURE.search(value):
        raise ValueError(f"{label} contains private or future-only text")
    return value


def _sha(value: Any, label: str, *, optional: bool = False) -> str | None:
    if optional and value is None:
        return None
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise ValueError(f"invalid {label} sha256")
    return value


def _bounded_int(value: Any, label: str, minimum: int, maximum: int) -> int:
    if (
        not isinstance(value, int)
        or isinstance(value, bool)
        or value < minimum
        or value > maximum
    ):
        raise ValueError(f"{label} must be between {minimum} and {maximum}")
    return value


def _unit_float(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be numeric")
    normalized = float(value)
    if not math.isfinite(normalized) or not 0.0 <= normalized <= 1.0:
        raise ValueError(f"{label} must be finite and between zero and one")
    return normalized


def _id_tuple(
    value: Any,
    label: str,
    *,
    minimum: int = 1,
    maximum: int = 256,
) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        raise ValueError(f"{label} must be a list")
    if not minimum <= len(value) <= maximum:
        raise ValueError(f"{label} count must be between {minimum} and {maximum}")
    result = tuple(_public_id(item, label) for item in value)
    if len(result) != len(set(result)):
        raise ValueError(f"{label} must not contain duplicates")
    return result


def _normalize_axis_mapping(
    value: Any, label: str
) -> Mapping[str, tuple[str, ...]]:
    if not isinstance(value, Mapping) or frozenset(value) != frozenset(COMPONENT_AXES):
        raise ValueError(f"{label} must contain exactly the trusted component axes")
    normalized = {
        axis: _id_tuple(value[axis], f"{label} {axis}", maximum=32)
        for axis in COMPONENT_AXES
    }
    for axis, component_ids in normalized.items():
        if any(
            item != "code_diff" and _FORBIDDEN_COMPONENT_CONTROL.search(item)
            for item in component_ids
        ):
            raise ValueError(
                f"{label} {axis} attempts to control code, prompt, evaluator, "
                "scorer, budget, or private state"
            )
    return MappingProxyType(normalized)


def _normalize_metric_mapping(
    value: Any, label: str, *, require_sum_one: bool
) -> Mapping[str, float]:
    if not isinstance(value, Mapping) or frozenset(value) != frozenset(METRIC_NAMES):
        raise ValueError(f"{label} must contain exactly {METRIC_NAMES}")
    result = {
        metric: _unit_float(value[metric], f"{label} {metric}")
        for metric in METRIC_NAMES
    }
    if require_sum_one and not math.isclose(
        sum(result.values()), 1.0, rel_tol=0.0, abs_tol=1e-9
    ):
        raise ValueError(f"{label} must sum to one")
    return MappingProxyType(result)


def _normalize_mechanism_hashes(value: Any, label: str) -> Mapping[str, str]:
    if not isinstance(value, Mapping) or frozenset(value) != frozenset(MECHANISMS):
        raise ValueError(f"{label} must contain exactly M, P, and A")
    return MappingProxyType(
        {
            mechanism: str(_sha(value[mechanism], f"{label} {mechanism}"))
            for mechanism in MECHANISMS
        }
    )


def _write_once(path: Path, content: bytes) -> None:
    if path.is_symlink():
        raise ValueError("refusing to write through a symbolic link")
    if path.exists():
        if not path.is_file():
            raise ValueError("content-addressed artifact is not a regular file")
        if path.read_bytes() != content:
            raise ValueError("refusing to overwrite a different content-addressed artifact")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(
        dir=path.parent, suffix=".moss-meta-evolution.tmp"
    )
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary_name).replace(path)
    except Exception:
        Path(temporary_name).unlink(missing_ok=True)
        raise


def _read_regular_file_without_symlinks(path: Path) -> bytes:
    """Read one file while rejecting symlinks in every path component.

    Walking with directory file descriptors and ``O_NOFOLLOW`` avoids both a
    final-component symlink and a parent-directory swap between validation and
    open.  Content-addressed state is small and bounded before parsing.
    """

    absolute = Path(os.path.abspath(os.fspath(path)))
    parts = absolute.parts
    if not parts or parts[0] != os.path.sep or len(parts) == 1:
        raise ValueError("content-addressed artifact path must name a file")
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    directory_flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | nofollow
    descriptor = os.open(os.path.sep, directory_flags)
    try:
        for component in parts[1:-1]:
            next_descriptor = os.open(
                component, directory_flags, dir_fd=descriptor
            )
            os.close(descriptor)
            descriptor = next_descriptor
        file_descriptor = os.open(
            parts[-1],
            os.O_RDONLY | getattr(os, "O_NONBLOCK", 0) | nofollow,
            dir_fd=descriptor,
        )
        try:
            metadata = os.fstat(file_descriptor)
            if not stat.S_ISREG(metadata.st_mode):
                raise ValueError("content-addressed artifact is not a regular file")
            if metadata.st_size > _MAX_CONTENT_ADDRESSED_BYTES:
                raise ValueError("content-addressed artifact exceeds the size bound")
            chunks: list[bytes] = []
            remaining = _MAX_CONTENT_ADDRESSED_BYTES + 1
            while remaining:
                chunk = os.read(file_descriptor, min(1024 * 1024, remaining))
                if not chunk:
                    break
                chunks.append(chunk)
                remaining -= len(chunk)
            content = b"".join(chunks)
            if len(content) > _MAX_CONTENT_ADDRESSED_BYTES:
                raise ValueError("content-addressed artifact exceeds the size bound")
            return content
        finally:
            os.close(file_descriptor)
    except OSError as exc:
        raise ValueError("content-addressed artifact path is missing or unsafe") from exc
    finally:
        os.close(descriptor)


def _reject_json_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON constant is forbidden: {value}")


def _load_content_addressed_payload(
    path: Path,
    *,
    expected_sha256: str,
    label: str,
) -> tuple[Mapping[str, Any], bytes]:
    expected = str(_sha(expected_sha256, f"expected {label}"))
    if path.name != f"{expected}.json":
        raise ValueError(f"{label} filename is not bound to the expected sha256")
    content = _read_regular_file_without_symlinks(path)
    if hashlib.sha256(content).hexdigest() != expected:
        raise ValueError(f"{label} content sha256 differs")
    try:
        payload = json.loads(
            content.decode("utf-8"),
            parse_constant=_reject_json_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} is not strict UTF-8 JSON") from exc
    if not isinstance(payload, Mapping):
        raise ValueError(f"{label} must contain a JSON object")
    if _canonical_bytes(payload) != content:
        raise ValueError(f"{label} bytes are not canonical")
    return payload, content


class _ContentAddressed:
    def core_payload(self) -> dict[str, Any]:  # pragma: no cover - interface guard
        raise NotImplementedError

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.core_payload())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    def store(self, root: Path) -> Path:
        """Write under its digest; a conflicting existing object fails closed."""

        path = root.resolve() / f"{self.sha256}.json"
        _write_once(path, self.canonical_bytes)
        return path

    @classmethod
    def load(
        cls: type[_ContentAddressedT],
        path: Path,
        *,
        expected_sha256: str,
    ) -> _ContentAddressedT:
        """Load a canonical, digest-bound object of exactly ``cls``'s type."""

        payload, content = _load_content_addressed_payload(
            path,
            expected_sha256=expected_sha256,
            label=cls.__name__,
        )
        parser = getattr(cls, "from_dict", None)
        if parser is None:
            raise TypeError(f"{cls.__name__} does not implement typed loading")
        item = parser(payload)
        if type(item) is not cls:
            raise ValueError(f"{cls.__name__} parser returned the wrong type")
        if item.canonical_bytes != content or item.sha256 != expected_sha256:
            raise ValueError(f"{cls.__name__} canonical object differs from stored bytes")
        return item


class TrustedMetaPolicyRegistry(_ContentAddressed):
    """The only component namespace that a meta-policy may select from."""

    def __init__(
        self, trusted_components: Mapping[str, Sequence[str]] | None = None
    ) -> None:
        supplied: Mapping[str, Sequence[str]] = (
            _DEFAULT_COMPONENTS if trusted_components is None else trusted_components
        )
        self._components = _normalize_axis_mapping(
            supplied, "trusted component registry"
        )

    @classmethod
    def default(cls) -> "TrustedMetaPolicyRegistry":
        return cls()

    @property
    def components(self) -> Mapping[str, tuple[str, ...]]:
        return self._components

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "TrustedMetaPolicyRegistry":
        _require_fields(
            payload,
            frozenset({"schema_version", "object_kind", "components"}),
            "trusted meta-policy registry",
        )
        if (
            payload["schema_version"] != 1
            or payload["object_kind"] != "trusted_meta_policy_registry"
        ):
            raise ValueError("unsupported trusted meta-policy registry schema")
        return cls(payload["components"])

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "object_kind": "trusted_meta_policy_registry",
            "components": {
                axis: list(self._components[axis]) for axis in COMPONENT_AXES
            },
        }

    def validate_candidates(self, candidates: Any, *, label: str) -> None:
        normalized = _normalize_axis_mapping(candidates, label)
        for axis, component_ids in normalized.items():
            unknown = set(component_ids) - set(self._components[axis])
            if unknown:
                raise ValueError(
                    f"{label} contains unknown trusted component(s) for {axis}: "
                    + ",".join(sorted(unknown))
                )

    def validate_harness(self, selection: Any, *, label: str) -> None:
        normalized = _normalize_axis_mapping(selection, label)
        self.validate_candidates(normalized, label=label)
        for singleton_axis in (
            "parent_strategy",
            "scheduler_mode",
            "recovery_mode",
        ):
            if len(normalized[singleton_axis]) != 1:
                raise ValueError(f"{label} {singleton_axis} must select exactly one")
        if len(normalized["role_graph"]) < 2:
            raise ValueError(f"{label} role_graph must select at least two roles")
        if len(normalized["workflow"]) < 3:
            raise ValueError(f"{label} workflow must select at least three steps")

    def validate_policy(self, policy: "MetaPolicySnapshot") -> None:
        if policy.trusted_meta_registry_sha256 != self.sha256:
            raise ValueError("meta-policy registry binding differs")
        self.validate_candidates(
            policy.component_candidates, label="meta-policy component candidates"
        )

    def validate_policy_transition(
        self, parent: "MetaPolicySnapshot", child: "MetaPolicySnapshot"
    ) -> None:
        self.validate_policy(parent)
        self.validate_policy(child)
        if child.parent_sha256 != parent.sha256:
            raise ValueError("meta-policy parent chain differs")
        if child.sha256 == parent.sha256:
            raise ValueError("meta-policy update did not change content")

    def select_nodes(
        self,
        *,
        policy: "MetaPolicySnapshot",
        archive: "HarnessArchiveSnapshot",
        target_stream_index: int,
        limit: int | None = None,
    ) -> tuple["HarnessArchiveNode", ...]:
        """Select public, strictly prior nodes with deterministic tie breaking."""

        self.validate_policy(policy)
        if archive.trusted_meta_registry_sha256 != self.sha256:
            raise ValueError("Harness archive registry binding differs")
        target = _bounded_int(
            target_stream_index, "target stream index", 1, 1_000_000
        )
        selected_limit = policy.retrieval_limit if limit is None else _bounded_int(
            limit, "selection limit", 1, policy.candidate_pool_limit
        )
        selected_limit = min(selected_limit, policy.candidate_pool_limit)
        candidates = [
            node
            for node in archive.nodes
            if node.source_stream_index < target
            and node.metrics["quality"] >= policy.minimum_quality
        ]

        def score(node: HarnessArchiveNode) -> float:
            value = sum(
                policy.objective_weights[metric] * node.metrics[metric]
                for metric in METRIC_NAMES
            )
            if policy.selection_mode == "failure_directed_v1":
                value += policy.exploration_rate * node.metrics["recovery"]
            elif policy.selection_mode == "pareto_diverse_v1":
                value += policy.exploration_rate * node.metrics["novelty"]
            return value

        ranked = sorted(candidates, key=lambda node: (-score(node), node.sha256))
        if policy.selection_mode != "pareto_diverse_v1":
            return tuple(ranked[:selected_limit])

        # Greedily keep different component fingerprints before filling remaining
        # seats.  Both passes are deterministically ordered.
        result: list[HarnessArchiveNode] = []
        seen_fingerprints: set[str] = set()
        deferred: list[HarnessArchiveNode] = []
        for node in ranked:
            if node.component_fingerprint in seen_fingerprints:
                deferred.append(node)
            else:
                result.append(node)
                seen_fingerprints.add(node.component_fingerprint)
            if len(result) == selected_limit:
                return tuple(result)
        result.extend(deferred[: selected_limit - len(result)])
        return tuple(result)


@dataclass(frozen=True)
class MetaPolicySnapshot(_ContentAddressed):
    policy_id: str
    parent_sha256: str | None
    trusted_meta_registry_sha256: str
    selection_mode: str
    retrieval_mode: str
    archive_mode: str
    objective_weights: Mapping[str, float]
    exploration_rate: float
    minimum_quality: float
    retrieval_limit: int
    candidate_pool_limit: int
    component_candidates: Mapping[str, tuple[str, ...]]

    _FIELDS = frozenset(
        {
            "schema_version",
            "object_kind",
            "policy_id",
            "parent_sha256",
            "trusted_meta_registry_sha256",
            "selection_mode",
            "retrieval_mode",
            "archive_mode",
            "objective_weights",
            "exploration_rate",
            "minimum_quality",
            "retrieval_limit",
            "candidate_pool_limit",
            "component_candidates",
        }
    )

    def __post_init__(self) -> None:
        object.__setattr__(self, "policy_id", _public_id(self.policy_id, "policy id"))
        object.__setattr__(
            self,
            "parent_sha256",
            _sha(self.parent_sha256, "parent meta-policy", optional=True),
        )
        object.__setattr__(
            self,
            "trusted_meta_registry_sha256",
            _sha(self.trusted_meta_registry_sha256, "trusted meta registry"),
        )
        if self.selection_mode not in _SELECTION_MODES:
            raise ValueError("unknown meta-policy selection mode")
        if self.retrieval_mode not in _RETRIEVAL_MODES:
            raise ValueError("unknown meta-policy retrieval mode")
        if self.archive_mode not in _ARCHIVE_MODES:
            raise ValueError("unknown meta-policy archive mode")
        object.__setattr__(
            self,
            "objective_weights",
            _normalize_metric_mapping(
                self.objective_weights, "objective weights", require_sum_one=True
            ),
        )
        object.__setattr__(
            self,
            "exploration_rate",
            _unit_float(self.exploration_rate, "exploration rate"),
        )
        object.__setattr__(
            self,
            "minimum_quality",
            _unit_float(self.minimum_quality, "minimum quality"),
        )
        object.__setattr__(
            self,
            "retrieval_limit",
            _bounded_int(self.retrieval_limit, "retrieval limit", 1, 32),
        )
        object.__setattr__(
            self,
            "candidate_pool_limit",
            _bounded_int(self.candidate_pool_limit, "candidate pool limit", 1, 64),
        )
        if self.retrieval_limit > self.candidate_pool_limit:
            raise ValueError("retrieval limit cannot exceed candidate pool limit")
        object.__setattr__(
            self,
            "component_candidates",
            _normalize_axis_mapping(
                self.component_candidates, "meta-policy component candidates"
            ),
        )

    @classmethod
    def create(
        cls,
        *,
        policy_id: str,
        registry: TrustedMetaPolicyRegistry,
        parent_sha256: str | None = None,
        selection_mode: str = "weighted_rank_v1",
        retrieval_mode: str = "descriptor_overlap_v1",
        archive_mode: str = "score_frontier_v1",
        objective_weights: Mapping[str, float] | None = None,
        exploration_rate: float = 0.2,
        minimum_quality: float = 0.0,
        retrieval_limit: int = 8,
        candidate_pool_limit: int = 16,
        component_candidates: Mapping[str, Sequence[str]] | None = None,
    ) -> "MetaPolicySnapshot":
        item = cls(
            policy_id=policy_id,
            parent_sha256=parent_sha256,
            trusted_meta_registry_sha256=registry.sha256,
            selection_mode=selection_mode,
            retrieval_mode=retrieval_mode,
            archive_mode=archive_mode,
            objective_weights=(
                {
                    "quality": 0.55,
                    "novelty": 0.15,
                    "recovery": 0.20,
                    "efficiency": 0.10,
                }
                if objective_weights is None
                else objective_weights
            ),
            exploration_rate=exploration_rate,
            minimum_quality=minimum_quality,
            retrieval_limit=retrieval_limit,
            candidate_pool_limit=candidate_pool_limit,
            component_candidates=(
                registry.components
                if component_candidates is None
                else component_candidates
            ),
        )
        registry.validate_policy(item)
        return item

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "MetaPolicySnapshot":
        _require_fields(payload, cls._FIELDS, "meta-policy snapshot")
        if payload["schema_version"] != 1 or payload["object_kind"] != "meta_policy":
            raise ValueError("unsupported meta-policy schema")
        return cls(
            policy_id=payload["policy_id"],
            parent_sha256=payload["parent_sha256"],
            trusted_meta_registry_sha256=payload["trusted_meta_registry_sha256"],
            selection_mode=payload["selection_mode"],
            retrieval_mode=payload["retrieval_mode"],
            archive_mode=payload["archive_mode"],
            objective_weights=payload["objective_weights"],
            exploration_rate=payload["exploration_rate"],
            minimum_quality=payload["minimum_quality"],
            retrieval_limit=payload["retrieval_limit"],
            candidate_pool_limit=payload["candidate_pool_limit"],
            component_candidates=payload["component_candidates"],
        )

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "object_kind": "meta_policy",
            "policy_id": self.policy_id,
            "parent_sha256": self.parent_sha256,
            "trusted_meta_registry_sha256": self.trusted_meta_registry_sha256,
            "selection_mode": self.selection_mode,
            "retrieval_mode": self.retrieval_mode,
            "archive_mode": self.archive_mode,
            "objective_weights": dict(self.objective_weights),
            "exploration_rate": self.exploration_rate,
            "minimum_quality": self.minimum_quality,
            "retrieval_limit": self.retrieval_limit,
            "candidate_pool_limit": self.candidate_pool_limit,
            "component_candidates": {
                axis: list(self.component_candidates[axis]) for axis in COMPONENT_AXES
            },
        }


@dataclass(frozen=True)
class HarnessArchiveNode(_ContentAddressed):
    node_id: str
    parent_node_sha256: str | None
    trusted_meta_registry_sha256: str
    source_suite: str
    source_instance_id: str
    source_stream_index: int
    harness_decision_sha256: str
    component_selection: Mapping[str, tuple[str, ...]]
    metrics: Mapping[str, float]
    provenance_event_ids: tuple[str, ...]

    _FIELDS = frozenset(
        {
            "schema_version",
            "object_kind",
            "node_id",
            "parent_node_sha256",
            "trusted_meta_registry_sha256",
            "source_suite",
            "source_instance_id",
            "source_stream_index",
            "harness_decision_sha256",
            "component_selection",
            "metrics",
            "provenance_event_ids",
        }
    )

    def __post_init__(self) -> None:
        object.__setattr__(self, "node_id", _public_id(self.node_id, "archive node id"))
        object.__setattr__(
            self,
            "parent_node_sha256",
            _sha(self.parent_node_sha256, "parent archive node", optional=True),
        )
        object.__setattr__(
            self,
            "trusted_meta_registry_sha256",
            _sha(self.trusted_meta_registry_sha256, "trusted meta registry"),
        )
        object.__setattr__(
            self, "source_suite", _public_id(self.source_suite, "source suite")
        )
        object.__setattr__(
            self,
            "source_instance_id",
            _public_id(self.source_instance_id, "source instance id"),
        )
        object.__setattr__(
            self,
            "source_stream_index",
            _bounded_int(self.source_stream_index, "source stream index", 0, 999_999),
        )
        object.__setattr__(
            self,
            "harness_decision_sha256",
            _sha(self.harness_decision_sha256, "Harness decision"),
        )
        object.__setattr__(
            self,
            "component_selection",
            _normalize_axis_mapping(self.component_selection, "Harness component selection"),
        )
        object.__setattr__(
            self,
            "metrics",
            _normalize_metric_mapping(self.metrics, "public metrics", require_sum_one=False),
        )
        object.__setattr__(
            self,
            "provenance_event_ids",
            _id_tuple(
                self.provenance_event_ids,
                "provenance event ids",
                maximum=256,
            ),
        )

    @classmethod
    def create(
        cls,
        *,
        node_id: str,
        registry: TrustedMetaPolicyRegistry,
        source_suite: str,
        source_instance_id: str,
        source_stream_index: int,
        harness_decision_sha256: str,
        component_selection: Mapping[str, Sequence[str]],
        metrics: Mapping[str, float],
        provenance_event_ids: Sequence[str],
        parent_node_sha256: str | None = None,
    ) -> "HarnessArchiveNode":
        item = cls(
            node_id=node_id,
            parent_node_sha256=parent_node_sha256,
            trusted_meta_registry_sha256=registry.sha256,
            source_suite=source_suite,
            source_instance_id=source_instance_id,
            source_stream_index=source_stream_index,
            harness_decision_sha256=harness_decision_sha256,
            component_selection=component_selection,
            metrics=metrics,
            provenance_event_ids=tuple(provenance_event_ids),
        )
        registry.validate_harness(item.component_selection, label="Harness archive node")
        return item

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "HarnessArchiveNode":
        _require_fields(payload, cls._FIELDS, "Harness archive node")
        if payload["schema_version"] != 1 or payload["object_kind"] != "harness_archive_node":
            raise ValueError("unsupported Harness archive node schema")
        return cls(
            node_id=payload["node_id"],
            parent_node_sha256=payload["parent_node_sha256"],
            trusted_meta_registry_sha256=payload["trusted_meta_registry_sha256"],
            source_suite=payload["source_suite"],
            source_instance_id=payload["source_instance_id"],
            source_stream_index=payload["source_stream_index"],
            harness_decision_sha256=payload["harness_decision_sha256"],
            component_selection=payload["component_selection"],
            metrics=payload["metrics"],
            provenance_event_ids=payload["provenance_event_ids"],
        )

    @property
    def component_fingerprint(self) -> str:
        payload = {
            axis: list(self.component_selection[axis]) for axis in COMPONENT_AXES
        }
        return hashlib.sha256(_canonical_bytes(payload)).hexdigest()

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "object_kind": "harness_archive_node",
            "node_id": self.node_id,
            "parent_node_sha256": self.parent_node_sha256,
            "trusted_meta_registry_sha256": self.trusted_meta_registry_sha256,
            "source_suite": self.source_suite,
            "source_instance_id": self.source_instance_id,
            "source_stream_index": self.source_stream_index,
            "harness_decision_sha256": self.harness_decision_sha256,
            "component_selection": {
                axis: list(self.component_selection[axis]) for axis in COMPONENT_AXES
            },
            "metrics": dict(self.metrics),
            "provenance_event_ids": list(self.provenance_event_ids),
        }


@dataclass(frozen=True)
class HarnessArchiveSnapshot(_ContentAddressed):
    archive_id: str
    parent_sha256: str | None
    trusted_meta_registry_sha256: str
    nodes: tuple[HarnessArchiveNode, ...]

    _FIELDS = frozenset(
        {
            "schema_version",
            "object_kind",
            "archive_id",
            "parent_sha256",
            "trusted_meta_registry_sha256",
            "nodes",
        }
    )

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "archive_id", _public_id(self.archive_id, "Harness archive id")
        )
        object.__setattr__(
            self,
            "parent_sha256",
            _sha(self.parent_sha256, "parent Harness archive", optional=True),
        )
        object.__setattr__(
            self,
            "trusted_meta_registry_sha256",
            _sha(self.trusted_meta_registry_sha256, "trusted meta registry"),
        )
        if not isinstance(self.nodes, (list, tuple)) or len(self.nodes) > 4096:
            raise ValueError("Harness archive nodes must be a bounded list")
        nodes = tuple(self.nodes)
        if not all(isinstance(node, HarnessArchiveNode) for node in nodes):
            raise ValueError("Harness archive contains a non-node object")
        object.__setattr__(self, "nodes", nodes)
        if len({node.node_id for node in nodes}) != len(nodes):
            raise ValueError("Harness archive node ids must be unique")
        if len({node.sha256 for node in nodes}) != len(nodes):
            raise ValueError("Harness archive node contents must be unique")
        known: set[str] = set()
        previous_stream_index = -1
        for ordinal, node in enumerate(nodes):
            if node.trusted_meta_registry_sha256 != self.trusted_meta_registry_sha256:
                raise ValueError("Harness archive node registry binding differs")
            if ordinal == 0:
                if node.parent_node_sha256 is not None:
                    raise ValueError("first Harness archive node must be a root")
            elif node.parent_node_sha256 not in known:
                raise ValueError("Harness archive node parent is absent or forward-referenced")
            if node.source_stream_index < previous_stream_index:
                raise ValueError("Harness archive nodes must be appended in stream order")
            previous_stream_index = node.source_stream_index
            known.add(node.sha256)

    @classmethod
    def create(
        cls,
        *,
        archive_id: str,
        registry: TrustedMetaPolicyRegistry,
        parent_sha256: str | None = None,
        nodes: Sequence[HarnessArchiveNode] = (),
    ) -> "HarnessArchiveSnapshot":
        item = cls(
            archive_id=archive_id,
            parent_sha256=parent_sha256,
            trusted_meta_registry_sha256=registry.sha256,
            nodes=tuple(nodes),
        )
        for node in item.nodes:
            registry.validate_harness(node.component_selection, label="Harness archive node")
        return item

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "HarnessArchiveSnapshot":
        _require_fields(payload, cls._FIELDS, "Harness archive snapshot")
        if payload["schema_version"] != 1 or payload["object_kind"] != "harness_archive":
            raise ValueError("unsupported Harness archive schema")
        if not isinstance(payload["nodes"], list):
            raise ValueError("Harness archive nodes must be a list")
        return cls(
            archive_id=payload["archive_id"],
            parent_sha256=payload["parent_sha256"],
            trusted_meta_registry_sha256=payload["trusted_meta_registry_sha256"],
            nodes=tuple(HarnessArchiveNode.from_dict(node) for node in payload["nodes"]),
        )

    def extend(
        self,
        node: HarnessArchiveNode,
        *,
        archive_id: str,
        registry: TrustedMetaPolicyRegistry,
    ) -> "HarnessArchiveSnapshot":
        if node.trusted_meta_registry_sha256 != registry.sha256:
            raise ValueError("new Harness node registry binding differs")
        registry.validate_harness(node.component_selection, label="new Harness archive node")
        if self.nodes:
            if node.parent_node_sha256 not in {item.sha256 for item in self.nodes}:
                raise ValueError("new Harness archive node must name an existing parent")
            if node.source_stream_index < self.nodes[-1].source_stream_index:
                raise ValueError("new Harness archive node moves backward in the stream")
        elif node.parent_node_sha256 is not None:
            raise ValueError("first Harness archive node must be a root")
        return self.create(
            archive_id=archive_id,
            parent_sha256=self.sha256,
            registry=registry,
            nodes=self.nodes + (node,),
        )

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "object_kind": "harness_archive",
            "archive_id": self.archive_id,
            "parent_sha256": self.parent_sha256,
            "trusted_meta_registry_sha256": self.trusted_meta_registry_sha256,
            "nodes": [node.core_payload() for node in self.nodes],
        }


def validate_memory_snapshot(snapshot: ExperienceBankSnapshot) -> None:
    """Validate the legacy Experience Bank as a bounded, public typed object.

    ``ExperienceBankSnapshot`` predates this state machine and exposes no strict
    loader.  Reconstructing its public records here prevents callers from using
    direct dataclass construction to smuggle an invalid or foreign source into an
    otherwise digest-shaped M update.
    """

    if not isinstance(snapshot, ExperienceBankSnapshot):
        raise ValueError("resolved memory must be an Experience Bank snapshot")
    if not isinstance(snapshot.bank_id, str) or not _SAFE_ID.fullmatch(snapshot.bank_id):
        raise ValueError("resolved memory has an unsafe bank id")
    _sha(snapshot.parent_sha256, "parent Experience Bank", optional=True)
    if not isinstance(snapshot.records, tuple) or len(snapshot.records) > 4096:
        raise ValueError("resolved memory records must be a bounded tuple")
    record_ids: set[str] = set()
    for record in snapshot.records:
        if not isinstance(record, ExperienceRecord):
            raise ValueError("resolved memory contains a non-record object")
        try:
            reparsed = ExperienceRecord.from_dict(record.to_dict())
        except Exception as exc:
            raise ValueError("resolved memory contains an invalid Experience Record") from exc
        if reparsed != record:
            raise ValueError("resolved memory record differs after strict normalization")
        _public_id(record.source_instance_id, "memory source instance id")
        if isinstance(record.outcome_delta, bool) or not math.isfinite(
            record.outcome_delta
        ):
            raise ValueError("resolved memory outcome delta must be finite")
        if any(
            isinstance(value, bool) or not math.isfinite(value)
            for value in record.resource_cost.values()
        ):
            raise ValueError("resolved memory resource costs must be finite")
        if record.record_id in record_ids:
            raise ValueError("resolved memory record ids must be unique")
        record_ids.add(record.record_id)
    # Also force JSON serialization now; this rejects values unsupported by the
    # legacy snapshot's canonical representation before the digest is trusted.
    try:
        json.loads(snapshot.canonical_bytes.decode("utf-8"))
    except (TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("resolved memory is not serializable canonical JSON") from exc


def validate_memory_transition(
    parent: ExperienceBankSnapshot,
    child: ExperienceBankSnapshot,
    *,
    source_instance_id: str,
) -> None:
    """Require an M update to append only records from its sealed source."""

    validate_memory_snapshot(parent)
    validate_memory_snapshot(child)
    source = _public_id(source_instance_id, "memory update source instance id")
    if child.parent_sha256 != parent.sha256:
        raise ValueError("Experience Bank parent chain differs")
    if len(child.records) <= len(parent.records):
        raise ValueError("Experience Bank update must append at least one record")
    if child.records[: len(parent.records)] != parent.records:
        raise ValueError("Experience Bank update must preserve the exact parent prefix")
    appended = child.records[len(parent.records) :]
    if any(record.source_instance_id != source for record in appended):
        raise ValueError("Experience Bank update contains a foreign source instance")


def validate_archive_transition(
    parent: HarnessArchiveSnapshot,
    child: HarnessArchiveSnapshot,
    *,
    proposal: "MetaUpdateProposal",
    registry: TrustedMetaPolicyRegistry,
) -> None:
    """Require an A update to append exactly the current sealed source node."""

    if parent.trusted_meta_registry_sha256 != registry.sha256:
        raise ValueError("parent Harness archive registry binding differs")
    if child.trusted_meta_registry_sha256 != registry.sha256:
        raise ValueError("child Harness archive registry binding differs")
    if child.parent_sha256 != parent.sha256:
        raise ValueError("Harness archive parent chain differs")
    if len(child.nodes) != len(parent.nodes) + 1:
        raise ValueError("Harness archive update must append exactly one node")
    if child.nodes[:-1] != parent.nodes:
        raise ValueError("Harness archive update must preserve the exact parent prefix")
    appended = child.nodes[-1]
    if (
        appended.source_instance_id != proposal.source_instance_id
        or appended.source_stream_index != proposal.source_stream_index
    ):
        raise ValueError("Harness archive update contains a foreign source instance")
    registry.validate_harness(
        appended.component_selection, label="appended Harness archive node"
    )


@dataclass(frozen=True)
class MetaUpdateProposal(_ContentAddressed):
    proposal_id: str
    result_checkpoint_id: str
    mechanism: str
    parent_checkpoint_sha256: str
    trusted_meta_registry_sha256: str
    source_instance_id: str
    source_stream_index: int
    target_stream_index: int
    before_sha256s: Mapping[str, str]
    after_sha256s: Mapping[str, str]
    provenance_event_ids: tuple[str, ...]

    _FIELDS = frozenset(
        {
            "schema_version",
            "object_kind",
            "proposal_id",
            "result_checkpoint_id",
            "mechanism",
            "parent_checkpoint_sha256",
            "trusted_meta_registry_sha256",
            "source_instance_id",
            "source_stream_index",
            "target_stream_index",
            "before_sha256s",
            "after_sha256s",
            "provenance_event_ids",
        }
    )

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "proposal_id", _public_id(self.proposal_id, "meta update proposal id")
        )
        object.__setattr__(
            self,
            "result_checkpoint_id",
            _public_id(self.result_checkpoint_id, "result checkpoint id"),
        )
        if self.mechanism not in MECHANISMS:
            raise ValueError("meta update mechanism must be one of M, P, or A")
        object.__setattr__(
            self,
            "parent_checkpoint_sha256",
            _sha(self.parent_checkpoint_sha256, "parent checkpoint"),
        )
        object.__setattr__(
            self,
            "trusted_meta_registry_sha256",
            _sha(self.trusted_meta_registry_sha256, "trusted meta registry"),
        )
        object.__setattr__(
            self,
            "source_instance_id",
            _public_id(self.source_instance_id, "source instance id"),
        )
        object.__setattr__(
            self,
            "source_stream_index",
            _bounded_int(self.source_stream_index, "source stream index", 0, 999_999),
        )
        object.__setattr__(
            self,
            "target_stream_index",
            _bounded_int(self.target_stream_index, "target stream index", 1, 1_000_000),
        )
        if self.target_stream_index != self.source_stream_index + 1:
            raise ValueError("meta update may affect only the next stream position")
        object.__setattr__(
            self,
            "before_sha256s",
            _normalize_mechanism_hashes(self.before_sha256s, "before hashes"),
        )
        object.__setattr__(
            self,
            "after_sha256s",
            _normalize_mechanism_hashes(self.after_sha256s, "after hashes"),
        )
        changed = {
            mechanism
            for mechanism in MECHANISMS
            if self.before_sha256s[mechanism] != self.after_sha256s[mechanism]
        }
        if changed != {self.mechanism}:
            raise ValueError("meta update must change exactly its declared M/P/A mechanism")
        object.__setattr__(
            self,
            "provenance_event_ids",
            _id_tuple(self.provenance_event_ids, "provenance event ids", maximum=256),
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "MetaUpdateProposal":
        _require_fields(payload, cls._FIELDS, "meta update proposal")
        if payload["schema_version"] != 2 or payload["object_kind"] != "meta_update":
            raise ValueError("unsupported meta update proposal schema")
        return cls(
            proposal_id=payload["proposal_id"],
            result_checkpoint_id=payload["result_checkpoint_id"],
            mechanism=payload["mechanism"],
            parent_checkpoint_sha256=payload["parent_checkpoint_sha256"],
            trusted_meta_registry_sha256=payload["trusted_meta_registry_sha256"],
            source_instance_id=payload["source_instance_id"],
            source_stream_index=payload["source_stream_index"],
            target_stream_index=payload["target_stream_index"],
            before_sha256s=payload["before_sha256s"],
            after_sha256s=payload["after_sha256s"],
            provenance_event_ids=tuple(payload["provenance_event_ids"]),
        )

    def assert_authorized(
        self,
        *,
        sealed_source_instance_ids: Sequence[str],
        expected_source_stream_index: int,
    ) -> None:
        sealed = {
            _public_id(item, "sealed source instance id")
            for item in sealed_source_instance_ids
        }
        if self.source_instance_id not in sealed:
            raise ValueError("meta update source is not a sealed prior instance")
        expected = _bounded_int(
            expected_source_stream_index, "expected source stream index", 0, 999_999
        )
        if self.source_stream_index != expected:
            raise ValueError("meta update source is from a future or stale stream position")

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 2,
            "object_kind": "meta_update",
            "proposal_id": self.proposal_id,
            "result_checkpoint_id": self.result_checkpoint_id,
            "mechanism": self.mechanism,
            "parent_checkpoint_sha256": self.parent_checkpoint_sha256,
            "trusted_meta_registry_sha256": self.trusted_meta_registry_sha256,
            "source_instance_id": self.source_instance_id,
            "source_stream_index": self.source_stream_index,
            "target_stream_index": self.target_stream_index,
            "before_sha256s": dict(self.before_sha256s),
            "after_sha256s": dict(self.after_sha256s),
            "provenance_event_ids": list(self.provenance_event_ids),
        }


@dataclass(frozen=True)
class MetaCheckpointV2(_ContentAddressed):
    checkpoint_id: str
    parent_checkpoint_sha256: str | None
    trusted_meta_registry_sha256: str
    next_stream_index: int
    learned_through_instance_id: str | None
    memory_sha256: str
    meta_policy_sha256: str
    harness_archive_sha256: str

    _FIELDS = frozenset(
        {
            "schema_version",
            "object_kind",
            "checkpoint_id",
            "parent_checkpoint_sha256",
            "trusted_meta_registry_sha256",
            "next_stream_index",
            "learned_through_instance_id",
            "memory_sha256",
            "meta_policy_sha256",
            "harness_archive_sha256",
        }
    )

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "checkpoint_id", _public_id(self.checkpoint_id, "meta checkpoint id")
        )
        object.__setattr__(
            self,
            "parent_checkpoint_sha256",
            _sha(self.parent_checkpoint_sha256, "parent checkpoint", optional=True),
        )
        object.__setattr__(
            self,
            "trusted_meta_registry_sha256",
            _sha(self.trusted_meta_registry_sha256, "trusted meta registry"),
        )
        object.__setattr__(
            self,
            "next_stream_index",
            _bounded_int(self.next_stream_index, "next stream index", 0, 1_000_000),
        )
        if self.learned_through_instance_id is not None:
            object.__setattr__(
                self,
                "learned_through_instance_id",
                _public_id(
                    self.learned_through_instance_id, "learned-through instance id"
                ),
            )
        if self.next_stream_index == 0:
            if self.learned_through_instance_id is not None:
                raise ValueError("genesis checkpoint cannot claim a learned instance")
        elif self.learned_through_instance_id is None:
            raise ValueError("non-genesis checkpoint must name its learned-through instance")
        object.__setattr__(
            self, "memory_sha256", _sha(self.memory_sha256, "memory")
        )
        object.__setattr__(
            self, "meta_policy_sha256", _sha(self.meta_policy_sha256, "meta-policy")
        )
        object.__setattr__(
            self,
            "harness_archive_sha256",
            _sha(self.harness_archive_sha256, "Harness archive"),
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "MetaCheckpointV2":
        _require_fields(payload, cls._FIELDS, "meta checkpoint v2")
        if payload["schema_version"] != 2 or payload["object_kind"] != "meta_checkpoint":
            raise ValueError("unsupported meta checkpoint schema")
        return cls(
            checkpoint_id=payload["checkpoint_id"],
            parent_checkpoint_sha256=payload["parent_checkpoint_sha256"],
            trusted_meta_registry_sha256=payload["trusted_meta_registry_sha256"],
            next_stream_index=payload["next_stream_index"],
            learned_through_instance_id=payload["learned_through_instance_id"],
            memory_sha256=payload["memory_sha256"],
            meta_policy_sha256=payload["meta_policy_sha256"],
            harness_archive_sha256=payload["harness_archive_sha256"],
        )

    @property
    def mechanism_sha256s(self) -> Mapping[str, str]:
        return MappingProxyType(
            {
                "M": self.memory_sha256,
                "P": self.meta_policy_sha256,
                "A": self.harness_archive_sha256,
            }
        )

    def apply(
        self,
        proposal: MetaUpdateProposal,
        *,
        sealed_source_instance_ids: Sequence[str],
    ) -> "MetaCheckpointV2":
        if not isinstance(proposal, MetaUpdateProposal):
            raise ValueError("a typed meta update proposal is required")
        if proposal.parent_checkpoint_sha256 != self.sha256:
            raise ValueError("meta update parent checkpoint differs")
        if proposal.trusted_meta_registry_sha256 != self.trusted_meta_registry_sha256:
            raise ValueError("meta update trusted registry binding differs")
        if dict(proposal.before_sha256s) != dict(self.mechanism_sha256s):
            raise ValueError("meta update before hashes differ from checkpoint")
        proposal.assert_authorized(
            sealed_source_instance_ids=sealed_source_instance_ids,
            expected_source_stream_index=self.next_stream_index,
        )
        return MetaCheckpointV2(
            checkpoint_id=proposal.result_checkpoint_id,
            parent_checkpoint_sha256=self.sha256,
            trusted_meta_registry_sha256=self.trusted_meta_registry_sha256,
            next_stream_index=proposal.target_stream_index,
            learned_through_instance_id=proposal.source_instance_id,
            memory_sha256=proposal.after_sha256s["M"],
            meta_policy_sha256=proposal.after_sha256s["P"],
            harness_archive_sha256=proposal.after_sha256s["A"],
        )

    def apply_verified(
        self,
        proposal: MetaUpdateProposal,
        *,
        sealed_source_instance_ids: Sequence[str],
        parent_memory: ExperienceBankSnapshot,
        memory: ExperienceBankSnapshot,
        parent_meta_policy: MetaPolicySnapshot,
        meta_policy: MetaPolicySnapshot,
        parent_harness_archive: HarnessArchiveSnapshot,
        harness_archive: HarnessArchiveSnapshot,
        registry: TrustedMetaPolicyRegistry,
    ) -> "MetaCheckpointV2":
        """Apply only after resolving every proposed digest to a typed object.

        The generic :meth:`apply` is the M/P/A transition validator.  Formal
        controllers should use this method so a proposer cannot invent an
        unresolvable digest for the new policy or archive.
        """

        if registry.sha256 != self.trusted_meta_registry_sha256:
            raise ValueError("checkpoint trusted registry binding differs")
        validate_memory_snapshot(parent_memory)
        validate_memory_snapshot(memory)
        registry.validate_policy(parent_meta_policy)
        registry.validate_policy(meta_policy)
        if parent_harness_archive.trusted_meta_registry_sha256 != registry.sha256:
            raise ValueError("parent Harness archive registry binding differs")
        if harness_archive.trusted_meta_registry_sha256 != registry.sha256:
            raise ValueError("resolved Harness archive registry binding differs")
        for node in parent_harness_archive.nodes + harness_archive.nodes:
            registry.validate_harness(
                node.component_selection, label="resolved Harness archive node"
            )
        resolved_parent = {
            "M": parent_memory.sha256,
            "P": parent_meta_policy.sha256,
            "A": parent_harness_archive.sha256,
        }
        if dict(self.mechanism_sha256s) != resolved_parent:
            raise ValueError("checkpoint hashes do not resolve to supplied parent objects")
        resolved = {
            "M": memory.sha256,
            "P": meta_policy.sha256,
            "A": harness_archive.sha256,
        }
        if dict(proposal.after_sha256s) != resolved:
            raise ValueError("meta update after hashes do not resolve to supplied objects")
        if proposal.mechanism == "M":
            validate_memory_transition(
                parent_memory,
                memory,
                source_instance_id=proposal.source_instance_id,
            )
        elif memory.sha256 != parent_memory.sha256:
            raise ValueError("non-M update changed resolved Experience Bank content")
        if proposal.mechanism == "P":
            registry.validate_policy_transition(parent_meta_policy, meta_policy)
        elif meta_policy.sha256 != parent_meta_policy.sha256:
            raise ValueError("non-P update changed resolved meta-policy content")
        if proposal.mechanism == "A":
            validate_archive_transition(
                parent_harness_archive,
                harness_archive,
                proposal=proposal,
                registry=registry,
            )
        elif harness_archive.sha256 != parent_harness_archive.sha256:
            raise ValueError("non-A update changed resolved Harness archive content")
        return self.apply(
            proposal,
            sealed_source_instance_ids=sealed_source_instance_ids,
        )

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 2,
            "object_kind": "meta_checkpoint",
            "checkpoint_id": self.checkpoint_id,
            "parent_checkpoint_sha256": self.parent_checkpoint_sha256,
            "trusted_meta_registry_sha256": self.trusted_meta_registry_sha256,
            "next_stream_index": self.next_stream_index,
            "learned_through_instance_id": self.learned_through_instance_id,
            "memory_sha256": self.memory_sha256,
            "meta_policy_sha256": self.meta_policy_sha256,
            "harness_archive_sha256": self.harness_archive_sha256,
        }


__all__ = [
    "COMPONENT_AXES",
    "MECHANISMS",
    "HarnessArchiveNode",
    "HarnessArchiveSnapshot",
    "MetaCheckpointV2",
    "MetaPolicySnapshot",
    "MetaUpdateProposal",
    "TrustedMetaPolicyRegistry",
    "validate_archive_transition",
    "validate_memory_snapshot",
    "validate_memory_transition",
]
