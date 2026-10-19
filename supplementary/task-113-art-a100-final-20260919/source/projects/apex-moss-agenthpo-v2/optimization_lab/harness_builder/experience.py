from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from typing import Any


_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_PRIVATE_TEXT = re.compile(
    r"(?:/home/|/data\d*/|private[_ -]evaluator|private[_ -]log)", re.IGNORECASE
)
_FIELDS = {
    "record_id",
    "source_instance_id",
    "builder_version",
    "instance_descriptor",
    "initial_harness_structure",
    "evolution_rule",
    "trigger_evidence",
    "outcome_delta",
    "correctness",
    "resource_cost",
    "counterexamples",
    "scope",
    "provenance_event_ids",
    "sealed",
}


def _text_tuple(value: Any, label: str) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or not value:
        raise ValueError(f"{label} must be a non-empty list")
    result = tuple(value)
    if not all(isinstance(item, str) and item.strip() for item in result):
        raise ValueError(f"{label} contains invalid text")
    if _PRIVATE_TEXT.search(json.dumps(result)):
        raise ValueError(f"{label} contains a private path")
    return result


@dataclass(frozen=True)
class ExperienceRecord:
    record_id: str
    source_instance_id: str
    builder_version: str
    instance_descriptor: tuple[str, ...]
    initial_harness_structure: tuple[str, ...]
    evolution_rule: str
    trigger_evidence: tuple[str, ...]
    outcome_delta: float
    correctness: bool
    resource_cost: dict[str, float]
    counterexamples: tuple[str, ...]
    scope: str
    provenance_event_ids: tuple[str, ...]
    sealed: bool

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ExperienceRecord":
        if set(payload) != _FIELDS:
            raise ValueError("Experience Record fields differ from the frozen schema")
        for name in (
            "record_id",
            "source_instance_id",
            "builder_version",
            "evolution_rule",
            "scope",
        ):
            if not isinstance(payload[name], str) or not _SAFE_ID.fullmatch(payload[name]):
                raise ValueError(f"unsafe Experience Record {name}")
        if payload["sealed"] is not True:
            raise ValueError("only a sealed first-encounter trajectory may become experience")
        if not isinstance(payload["correctness"], bool):
            raise ValueError("Experience Record correctness must be boolean")
        if not isinstance(payload["outcome_delta"], (int, float)):
            raise ValueError("Experience Record outcome delta must be numeric")
        costs = payload["resource_cost"]
        if not isinstance(costs, dict) or not costs:
            raise ValueError("Experience Record resource cost must be non-empty")
        normalized_costs: dict[str, float] = {}
        for key, value in costs.items():
            if not isinstance(key, str) or not _SAFE_ID.fullmatch(key):
                raise ValueError("unsafe resource cost key")
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError("resource costs must be non-negative")
            normalized_costs[key] = float(value)
        return cls(
            record_id=payload["record_id"],
            source_instance_id=payload["source_instance_id"],
            builder_version=payload["builder_version"],
            instance_descriptor=_text_tuple(
                payload["instance_descriptor"], "instance descriptor"
            ),
            initial_harness_structure=_text_tuple(
                payload["initial_harness_structure"], "initial Harness structure"
            ),
            evolution_rule=payload["evolution_rule"],
            trigger_evidence=_text_tuple(payload["trigger_evidence"], "trigger evidence"),
            outcome_delta=float(payload["outcome_delta"]),
            correctness=payload["correctness"],
            resource_cost=normalized_costs,
            counterexamples=_text_tuple(payload["counterexamples"], "counterexamples"),
            scope=payload["scope"],
            provenance_event_ids=_text_tuple(
                payload["provenance_event_ids"], "provenance event ids"
            ),
            sealed=True,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def promotion_level(*, instance_count: int, benchmark_count: int) -> str:
    if instance_count < 1 or benchmark_count < 1 or benchmark_count > instance_count:
        raise ValueError("invalid support counts")
    if benchmark_count >= 3 and instance_count >= 6:
        return "trusted_default_prior"
    if benchmark_count >= 2:
        return "cross_benchmark_replicated"
    if instance_count >= 2:
        return "within_benchmark_replicated"
    return "single_instance_observation"
