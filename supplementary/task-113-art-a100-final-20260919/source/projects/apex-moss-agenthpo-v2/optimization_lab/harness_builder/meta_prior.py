"""Controller-issued, Builder-only priors for isolated B-online mechanisms.

The prior is a bounded projection of exactly one content-addressed mechanism
snapshot.  It may influence the next task's Harness planner, but it is never
included in the compiled solution prompt.  This preserves a clean distinction
between meta-level Harness adaptation and direct solver hints.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from .learning import ExperienceBankSnapshot
from .meta_evolution import (
    COMPONENT_AXES,
    HarnessArchiveSnapshot,
    MetaCheckpointV2,
    MetaPolicySnapshot,
    TrustedMetaPolicyRegistry,
)


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_MECHANISM_IDS = ("OM", "OP", "OA")
_STATE_KINDS = {
    "OM": "CONTENT_ADDRESSED_META_MEMORY",
    "OP": "TYPED_VERSIONED_META_POLICY",
    "OA": "TYPED_HARNESS_POPULATION_ARCHIVE",
}
_PAYLOAD_KEYS = {
    "OM": {"records"},
    "OP": {
        "archive_mode",
        "candidate_pool_limit",
        "component_candidates",
        "exploration_rate",
        "minimum_quality",
        "objective_weights",
        "retrieval_limit",
        "retrieval_mode",
        "selection_mode",
    },
    "OA": {"selected_nodes"},
}
_FORBIDDEN_TEXT = re.compile(
    r"(?:/home/|/data\d*/|(?:^|[/:_.+\-])"
    r"(?:private|hidden|future|evaluator|scorer|budget|prompt|code)"
    r"(?:$|[/:_.+\-]))",
    re.IGNORECASE,
)
_RECORD_FIELDS = {"record_id", "source_instance_id", "scope", "summary"}
_ARCHIVE_NODE_FIELDS = {
    "node_sha256",
    "source_suite",
    "source_instance_id",
    "source_stream_index",
    "component_fingerprint",
    "component_selection",
    "metrics",
}


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(
            payload,
            allow_nan=False,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _safe_id(value: object, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise ValueError(f"unsafe meta-prior {label}")
    return value


def _sha(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"invalid meta-prior {label} sha256")
    return value


def _public_value(value: object, *, depth: int = 0) -> None:
    if depth > 8:
        raise ValueError("meta-prior payload is too deeply nested")
    if value is None or type(value) in {bool, int, float}:
        return
    if isinstance(value, str):
        if len(value) > 4_000 or (
            value != "code_diff" and _FORBIDDEN_TEXT.search(value)
        ):
            raise ValueError("meta-prior payload contains forbidden control or private text")
        return
    if isinstance(value, (list, tuple)):
        if len(value) > 256:
            raise ValueError("meta-prior payload list is too large")
        for item in value:
            _public_value(item, depth=depth + 1)
        return
    if isinstance(value, Mapping):
        if len(value) > 64:
            raise ValueError("meta-prior payload object is too large")
        for key, item in value.items():
            _safe_id(key, "payload key")
            _public_value(item, depth=depth + 1)
        return
    raise ValueError("meta-prior payload contains an unsupported value")


def _freeze(value: object) -> object:
    if isinstance(value, Mapping):
        return MappingProxyType({str(key): _freeze(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_freeze(item) for item in value)
    return value


def _thaw(value: object) -> object:
    if isinstance(value, Mapping):
        return {str(key): _thaw(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw(item) for item in value]
    return value


@dataclass(frozen=True)
class BuilderMetaPrior:
    mechanism_id: str
    state_kind: str
    trusted_meta_registry_sha256: str
    source_snapshot_sha256: str
    parent_checkpoint_sha256: str
    source_stream_index: int
    target_stream_index: int
    learned_through_instance_id: str
    target_instance_id: str
    payload: Mapping[str, Any]

    def __post_init__(self) -> None:
        if self.mechanism_id not in _MECHANISM_IDS:
            raise ValueError("meta-prior mechanism must be OM, OP, or OA")
        if self.state_kind != _STATE_KINDS[self.mechanism_id]:
            raise ValueError("meta-prior state kind differs from its mechanism")
        _sha(self.trusted_meta_registry_sha256, "trusted meta registry")
        if (
            self.trusted_meta_registry_sha256
            != TrustedMetaPolicyRegistry.default().sha256
        ):
            raise ValueError("meta-prior trusted component registry differs")
        _sha(self.source_snapshot_sha256, "source snapshot")
        _sha(self.parent_checkpoint_sha256, "parent checkpoint")
        if (
            type(self.source_stream_index) is not int
            or type(self.target_stream_index) is not int
            or self.source_stream_index < 0
            or self.target_stream_index <= self.source_stream_index
        ):
            raise ValueError("meta-prior stream boundary differs")
        learned = _safe_id(
            self.learned_through_instance_id, "learned-through instance id"
        )
        target = _safe_id(self.target_instance_id, "target instance id")
        if learned == target:
            raise ValueError("meta-prior cannot target its own source instance")
        if not isinstance(self.payload, Mapping) or set(self.payload) != _PAYLOAD_KEYS[
            self.mechanism_id
        ]:
            raise ValueError("meta-prior payload schema differs")
        try:
            canonical_payload = json.loads(_canonical_bytes(_thaw(self.payload)))
        except (TypeError, ValueError) as exc:
            raise ValueError("meta-prior payload is not canonical JSON") from exc
        _public_value(canonical_payload)
        object.__setattr__(self, "payload", _freeze(canonical_payload))
        self._validate_mechanism_payload(target)

    def _validate_mechanism_payload(self, target: str) -> None:
        if self.mechanism_id == "OM":
            records = self.payload["records"]
            if not isinstance(records, (list, tuple)) or not 1 <= len(records) <= 8:
                raise ValueError("meta-memory prior requires one to eight records")
            record_ids: set[str] = set()
            for record in records:
                if not isinstance(record, Mapping) or set(record) != _RECORD_FIELDS:
                    raise ValueError("meta-memory record fields differ")
                record_id = _safe_id(record["record_id"], "memory record id")
                source_id = _safe_id(
                    record["source_instance_id"], "memory source instance id"
                )
                if record_id in record_ids or source_id == target:
                    raise ValueError("meta-memory prior contains duplicate or target evidence")
                record_ids.add(record_id)
                if not isinstance(record["scope"], str) or not record["scope"].strip():
                    raise ValueError("meta-memory record scope is empty")
                if not isinstance(record["summary"], str) or not record["summary"].strip():
                    raise ValueError("meta-memory record summary is empty")
            return
        if self.mechanism_id == "OP":
            candidates = self.payload["component_candidates"]
            TrustedMetaPolicyRegistry.default().validate_candidates(
                candidates, label="Builder meta-policy component candidates"
            )
            for axis in COMPONENT_AXES:
                if not candidates[axis]:
                    raise ValueError("meta-policy candidate axes cannot be empty")
            if not {"generator", "verifier"} <= set(candidates["role_graph"]):
                raise ValueError("meta-policy must retain generator and verifier")
            workflow = set(candidates["workflow"])
            if not {"generate", "verify_contract"} <= workflow:
                raise ValueError("meta-policy must retain generation and verification")
            return
        nodes = self.payload["selected_nodes"]
        if not isinstance(nodes, (list, tuple)) or not 1 <= len(nodes) <= 32:
            raise ValueError("Harness archive prior requires one to 32 nodes")
        node_hashes: set[str] = set()
        registry = TrustedMetaPolicyRegistry.default()
        for node in nodes:
            if not isinstance(node, Mapping) or set(node) != _ARCHIVE_NODE_FIELDS:
                raise ValueError("Harness archive prior node fields differ")
            node_sha = _sha(node["node_sha256"], "archive node")
            _sha(node["component_fingerprint"], "archive component fingerprint")
            source_id = _safe_id(
                node["source_instance_id"], "archive source instance id"
            )
            _safe_id(node["source_suite"], "archive source suite")
            source_index = node["source_stream_index"]
            if (
                node_sha in node_hashes
                or source_id == target
                or type(source_index) is not int
                or source_index < 0
                or source_index >= self.target_stream_index
            ):
                raise ValueError("Harness archive prior contains duplicate or non-prior evidence")
            node_hashes.add(node_sha)
            registry.validate_harness(
                node["component_selection"], label="Builder archive prior selection"
            )
            metrics = node["metrics"]
            if not isinstance(metrics, Mapping) or set(metrics) != {
                "quality",
                "novelty",
                "recovery",
                "efficiency",
            }:
                raise ValueError("Harness archive prior metrics differ")

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "object_kind": "builder_meta_prior",
            "mechanism_id": self.mechanism_id,
            "state_kind": self.state_kind,
            "trusted_meta_registry_sha256": self.trusted_meta_registry_sha256,
            "source_snapshot_sha256": self.source_snapshot_sha256,
            "parent_checkpoint_sha256": self.parent_checkpoint_sha256,
            "source_stream_index": self.source_stream_index,
            "target_stream_index": self.target_stream_index,
            "learned_through_instance_id": self.learned_through_instance_id,
            "target_instance_id": self.target_instance_id,
            "payload": _thaw(self.payload),
        }

    @property
    def sha256(self) -> str:
        return hashlib.sha256(_canonical_bytes(self.core_payload())).hexdigest()

    def planner_payload(self) -> dict[str, Any]:
        return {**self.core_payload(), "prior_sha256": self.sha256}

    @classmethod
    def from_memory(
        cls,
        *,
        bank: ExperienceBankSnapshot,
        checkpoint: MetaCheckpointV2,
        target_instance_descriptors: Sequence[str],
        target_instance_id: str,
        target_stream_index: int | None = None,
        limit: int = 8,
    ) -> "BuilderMetaPrior":
        if checkpoint.memory_sha256 != bank.sha256:
            raise ValueError("meta-memory snapshot differs from checkpoint")
        if checkpoint.next_stream_index < 1 or checkpoint.learned_through_instance_id is None:
            raise ValueError("meta-memory prior requires a learned source checkpoint")
        records = bank.retrieve(
            instance_id=target_instance_id,
            instance_descriptors=tuple(target_instance_descriptors),
            limit=limit,
        )
        if not records:
            raise ValueError("meta-memory prior cannot be empty")
        return cls(
            mechanism_id="OM",
            state_kind=_STATE_KINDS["OM"],
            trusted_meta_registry_sha256=checkpoint.trusted_meta_registry_sha256,
            source_snapshot_sha256=bank.sha256,
            parent_checkpoint_sha256=checkpoint.sha256,
            source_stream_index=checkpoint.next_stream_index - 1,
            target_stream_index=(
                checkpoint.next_stream_index
                if target_stream_index is None
                else target_stream_index
            ),
            learned_through_instance_id=str(checkpoint.learned_through_instance_id),
            target_instance_id=target_instance_id,
            payload={"records": [dict(record) for record in records]},
        )

    @classmethod
    def from_policy(
        cls,
        *,
        policy: MetaPolicySnapshot,
        checkpoint: MetaCheckpointV2,
        registry: TrustedMetaPolicyRegistry,
        target_instance_id: str,
        target_stream_index: int | None = None,
    ) -> "BuilderMetaPrior":
        if checkpoint.meta_policy_sha256 != policy.sha256:
            raise ValueError("meta-policy snapshot differs from checkpoint")
        if checkpoint.next_stream_index < 1 or checkpoint.learned_through_instance_id is None:
            raise ValueError("meta-policy prior requires a learned source checkpoint")
        registry.validate_policy(policy)
        payload = policy.core_payload()
        for key in (
            "schema_version",
            "object_kind",
            "policy_id",
            "parent_sha256",
            "trusted_meta_registry_sha256",
        ):
            payload.pop(key)
        return cls(
            mechanism_id="OP",
            state_kind=_STATE_KINDS["OP"],
            trusted_meta_registry_sha256=checkpoint.trusted_meta_registry_sha256,
            source_snapshot_sha256=policy.sha256,
            parent_checkpoint_sha256=checkpoint.sha256,
            source_stream_index=checkpoint.next_stream_index - 1,
            target_stream_index=(
                checkpoint.next_stream_index
                if target_stream_index is None
                else target_stream_index
            ),
            learned_through_instance_id=str(checkpoint.learned_through_instance_id),
            target_instance_id=target_instance_id,
            payload=payload,
        )

    @classmethod
    def from_archive(
        cls,
        *,
        archive: HarnessArchiveSnapshot,
        policy: MetaPolicySnapshot,
        checkpoint: MetaCheckpointV2,
        registry: TrustedMetaPolicyRegistry,
        target_instance_id: str,
        target_stream_index: int | None = None,
    ) -> "BuilderMetaPrior":
        if checkpoint.harness_archive_sha256 != archive.sha256:
            raise ValueError("Harness archive snapshot differs from checkpoint")
        if checkpoint.next_stream_index < 1 or checkpoint.learned_through_instance_id is None:
            raise ValueError("Harness archive prior requires a learned source checkpoint")
        if checkpoint.meta_policy_sha256 != policy.sha256:
            raise ValueError("fixed archive selector differs from checkpoint")
        target_index = (
            checkpoint.next_stream_index
            if target_stream_index is None
            else target_stream_index
        )
        nodes = registry.select_nodes(
            policy=policy,
            archive=archive,
            target_stream_index=target_index,
        )
        if not nodes:
            raise ValueError("Harness archive prior cannot be empty")
        selected = [
            {
                "node_sha256": node.sha256,
                "source_suite": node.source_suite,
                "source_instance_id": node.source_instance_id,
                "source_stream_index": node.source_stream_index,
                "component_fingerprint": node.component_fingerprint,
                "component_selection": {
                    axis: list(node.component_selection[axis])
                    for axis in COMPONENT_AXES
                },
                "metrics": dict(node.metrics),
            }
            for node in nodes
        ]
        return cls(
            mechanism_id="OA",
            state_kind=_STATE_KINDS["OA"],
            trusted_meta_registry_sha256=checkpoint.trusted_meta_registry_sha256,
            source_snapshot_sha256=archive.sha256,
            parent_checkpoint_sha256=checkpoint.sha256,
            source_stream_index=checkpoint.next_stream_index - 1,
            target_stream_index=target_index,
            learned_through_instance_id=str(checkpoint.learned_through_instance_id),
            target_instance_id=target_instance_id,
            payload={"selected_nodes": selected},
        )


__all__ = ["BuilderMetaPrior"]
