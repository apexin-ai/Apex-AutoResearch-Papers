from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Sequence

from .dual_harness import HarnessWorkspace, TaskHarnessArtifact, TaskHarnessSpec


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_LABEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_SOURCE_SCHEDULE = (
    "champion",
    "pareto",
    "champion",
    "restart",
    "champion",
    "pareto",
    "champion",
    "champion",
    "pareto",
    "champion",
)


def _canonical_json(payload: Any) -> str:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def harness_distance(left: TaskHarnessSpec, right: TaskHarnessSpec) -> int:
    """Count changed node positions, including insertions and removals."""

    left_nodes = [node.to_dict() for node in left.nodes]
    right_nodes = [node.to_dict() for node in right.nodes]
    common = min(len(left_nodes), len(right_nodes))
    return sum(left_nodes[index] != right_nodes[index] for index in range(common)) + abs(
        len(left_nodes) - len(right_nodes)
    )


@dataclass(frozen=True)
class PortfolioEvolutionPolicy:
    """Deterministic source, restart, and mutation-family policy."""

    schema_version: int = 1
    mutation_families: tuple[str, ...] = (
        "failure_repair",
        "workflow_reorder",
        "tool_strategy",
        "role_decomposition",
    )
    same_failure_limit: int = 3
    stagnation_limit: int = 6
    max_changed_nodes: int = 1
    early_stable_limit: int = 3

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported portfolio evolution policy schema")
        if not self.mutation_families or len(set(self.mutation_families)) != len(
            self.mutation_families
        ):
            raise ValueError("mutation families must be non-empty and unique")
        if any(_SAFE_LABEL.fullmatch(item) is None for item in self.mutation_families):
            raise ValueError("mutation family is invalid")
        if self.same_failure_limit < 1 or self.stagnation_limit < 1:
            raise ValueError("portfolio policy limits must be positive")
        if self.max_changed_nodes < 1 or self.early_stable_limit < 1:
            raise ValueError("portfolio mutation and restart limits must be positive")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "source_weights": {"champion": 0.6, "pareto": 0.3, "restart": 0.1},
            "source_schedule": list(_SOURCE_SCHEDULE),
            "mutation_families": list(self.mutation_families),
            "same_failure_limit": self.same_failure_limit,
            "stagnation_limit": self.stagnation_limit,
            "max_changed_nodes": self.max_changed_nodes,
            "early_stable_limit": self.early_stable_limit,
        }

    @property
    def sha256(self) -> str:
        return hashlib.sha256(_canonical_json(self.to_dict()).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class GateDecision:
    """Typed public output from an evaluator outside the mutable Harness."""

    evaluator_contract_sha256: str
    incumbent_sha256: str
    candidate_sha256: str
    passed: bool
    credible_improvement: bool
    utility: float
    benchmark_scores: tuple[tuple[str, float], ...]
    failure_class: str | None
    reason: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.evaluator_contract_sha256, "evaluator contract"),
            (self.incumbent_sha256, "incumbent"),
            (self.candidate_sha256, "candidate"),
        ):
            if _SHA256.fullmatch(value) is None:
                raise ValueError(f"Gate {label} hash is invalid")
        if type(self.passed) is not bool or type(self.credible_improvement) is not bool:
            raise ValueError("Gate booleans are invalid")
        if self.credible_improvement and not self.passed:
            raise ValueError("a rejected Gate result cannot claim credible improvement")
        if isinstance(self.utility, bool) or not math.isfinite(float(self.utility)):
            raise ValueError("Gate utility is invalid")
        labels = [label for label, _ in self.benchmark_scores]
        if not labels or len(set(labels)) != len(labels) or any(
            _SAFE_LABEL.fullmatch(label) is None for label in labels
        ):
            raise ValueError("Gate benchmark score labels are invalid")
        if any(
            isinstance(score, bool) or not math.isfinite(float(score))
            for _, score in self.benchmark_scores
        ):
            raise ValueError("Gate benchmark score is invalid")
        if self.failure_class is not None and _SAFE_LABEL.fullmatch(self.failure_class) is None:
            raise ValueError("Gate failure class is invalid")
        if not isinstance(self.reason, str) or not self.reason.strip() or len(self.reason) > 4_000:
            raise ValueError("Gate reason is invalid")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "evaluator_contract_sha256": self.evaluator_contract_sha256,
            "incumbent_sha256": self.incumbent_sha256,
            "candidate_sha256": self.candidate_sha256,
            "passed": self.passed,
            "credible_improvement": self.credible_improvement,
            "utility": float(self.utility),
            "benchmark_scores": {
                label: float(score) for label, score in self.benchmark_scores
            },
            "failure_class": self.failure_class,
            "reason": self.reason,
        }

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "GateDecision":
        required = {
            "schema_version",
            "evaluator_contract_sha256",
            "incumbent_sha256",
            "candidate_sha256",
            "passed",
            "credible_improvement",
            "utility",
            "benchmark_scores",
            "failure_class",
            "reason",
        }
        if not isinstance(payload, Mapping) or set(payload) != required:
            raise ValueError("Gate decision keys differ from the contract")
        if payload["schema_version"] != 1:
            raise ValueError("unsupported Gate decision schema")
        raw_scores = payload["benchmark_scores"]
        if not isinstance(raw_scores, Mapping):
            raise ValueError("Gate benchmark scores must be an object")
        return cls(
            evaluator_contract_sha256=payload["evaluator_contract_sha256"],
            incumbent_sha256=payload["incumbent_sha256"],
            candidate_sha256=payload["candidate_sha256"],
            passed=payload["passed"],
            credible_improvement=payload["credible_improvement"],
            utility=payload["utility"],
            benchmark_scores=tuple(sorted(raw_scores.items())),
            failure_class=payload["failure_class"],
            reason=payload["reason"],
        )


@dataclass(frozen=True)
class MutationDirective:
    attempt_index: int
    scheduled_source: str
    source: str
    parent_sha256: str
    mutation_family: str
    max_changed_nodes: int
    target_failure_class: str | None
    target_failure_reason: str | None
    forced_restart: bool
    fallback_reason: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_index": self.attempt_index,
            "scheduled_source": self.scheduled_source,
            "source": self.source,
            "parent_sha256": self.parent_sha256,
            "mutation_family": self.mutation_family,
            "max_changed_nodes": self.max_changed_nodes,
            "target_failure_class": self.target_failure_class,
            "target_failure_reason": self.target_failure_reason,
            "forced_restart": self.forced_restart,
            "fallback_reason": self.fallback_reason,
        }


def _dominates(left: GateDecision, right: GateDecision) -> bool:
    left_scores = dict(left.benchmark_scores)
    right_scores = dict(right.benchmark_scores)
    if set(left_scores) != set(right_scores) or not left_scores:
        return False
    return all(left_scores[key] >= right_scores[key] for key in left_scores) and any(
        left_scores[key] > right_scores[key] for key in left_scores
    )


class ChampionArchivePolicy:
    """Select mutation parents from champion, Pareto archive, or stable history."""

    def __init__(
        self,
        *,
        workspace: HarnessWorkspace,
        evaluator_contract_sha256: str,
        policy: PortfolioEvolutionPolicy | None = None,
    ) -> None:
        if _SHA256.fullmatch(evaluator_contract_sha256) is None:
            raise ValueError("portfolio evaluator contract hash is invalid")
        self.workspace = workspace
        self.evaluator_contract_sha256 = evaluator_contract_sha256
        self.policy = policy or PortfolioEvolutionPolicy()

    def next_directive(self, *, attempt_index: int) -> MutationDirective:
        if (
            not isinstance(attempt_index, int)
            or isinstance(attempt_index, bool)
            or attempt_index < 0
        ):
            raise ValueError("portfolio attempt index is invalid")
        decisions = self._history()
        scheduled = _SOURCE_SCHEDULE[attempt_index % len(_SOURCE_SCHEDULE)]
        forced_restart = self._stagnation_count(decisions) >= self.policy.stagnation_limit
        requested = "restart" if forced_restart else scheduled
        family = self._mutation_family(decisions)
        parent, actual, fallback = self._select_parent(
            requested=requested,
            attempt_index=attempt_index,
            decisions=decisions,
        )
        latest_failure = next(
            (decision for decision, _ in reversed(decisions) if not decision.passed),
            None,
        )
        return MutationDirective(
            attempt_index=attempt_index,
            scheduled_source=scheduled,
            source=actual,
            parent_sha256=parent.sha256,
            mutation_family=family,
            max_changed_nodes=self.policy.max_changed_nodes,
            target_failure_class=(
                latest_failure.failure_class if latest_failure is not None else None
            ),
            target_failure_reason=(
                latest_failure.reason if latest_failure is not None else None
            ),
            forced_restart=forced_restart,
            fallback_reason=fallback,
        )

    def next_attempt_index(self) -> int:
        history = self._history()
        if not history:
            return 0
        return max(int(record["attempt_index"]) for _, record in history) + 1

    def pareto_sha256s(self) -> tuple[str, ...]:
        history = self._history()
        passed = [(decision, record) for decision, record in history if decision.passed]
        frontier: list[str] = []
        for decision, _ in passed:
            if any(
                other.candidate_sha256 != decision.candidate_sha256
                and _dominates(other, decision)
                for other, _ in passed
            ):
                continue
            if decision.candidate_sha256 not in frontier:
                frontier.append(decision.candidate_sha256)
        return tuple(sorted(frontier))

    def _history(self) -> list[tuple[GateDecision, Mapping[str, Any]]]:
        records = {record["proposal_id"]: record for record in self.workspace.archived_candidates()}
        history: list[tuple[GateDecision, Mapping[str, Any]]] = []
        for payload in self.workspace.gate_decisions():
            if payload.get("evaluator_contract_sha256") != self.evaluator_contract_sha256:
                continue
            record = records.get(payload.get("proposal_id"))
            if record is None:
                raise ValueError("Gate history refers to a missing archive record")
            decision_payload = dict(payload)
            decision_payload.pop("proposal_id", None)
            history.append((GateDecision.from_dict(decision_payload), record))
        return sorted(history, key=lambda item: int(item[1]["attempt_index"]))

    def _mutation_family(
        self, history: Sequence[tuple[GateDecision, Mapping[str, Any]]]
    ) -> str:
        if not history:
            return self.policy.mutation_families[0]
        last_decision, last_record = history[-1]
        current = last_record["mutation_family"]
        trailing = 0
        if not last_decision.passed and last_decision.failure_class is not None:
            for decision, record in reversed(history):
                if (
                    decision.passed
                    or decision.failure_class != last_decision.failure_class
                    or record["mutation_family"] != current
                ):
                    break
                trailing += 1
        if trailing < self.policy.same_failure_limit:
            return current
        index = self.policy.mutation_families.index(current)
        return self.policy.mutation_families[(index + 1) % len(self.policy.mutation_families)]

    @staticmethod
    def _stagnation_count(
        history: Sequence[tuple[GateDecision, Mapping[str, Any]]]
    ) -> int:
        count = 0
        for decision, record in reversed(history):
            if decision.credible_improvement or record.get("forced_restart") is True:
                break
            count += 1
        return count

    def _select_parent(
        self,
        *,
        requested: str,
        attempt_index: int,
        decisions: Sequence[tuple[GateDecision, Mapping[str, Any]]],
    ) -> tuple[TaskHarnessArtifact, str, str | None]:
        champion = self.workspace.champion()
        if requested == "champion":
            return champion, "champion", None
        if requested == "pareto":
            choices = [
                self.workspace.load_artifact(sha256)
                for sha256 in self.pareto_sha256s()
                if sha256 != champion.sha256
            ]
            if choices:
                choices.sort(
                    key=lambda item: (
                        -harness_distance(item.spec, champion.spec),
                        item.sha256,
                    )
                )
                return choices[0], "pareto", None
            return champion, "champion", "pareto_archive_empty"
        stable = self._stable_restart_pool(decisions)
        if stable:
            chosen = stable[attempt_index % len(stable)]
            return chosen, "restart", None
        return champion, "champion", "stable_restart_pool_empty"

    def _stable_restart_pool(
        self, decisions: Sequence[tuple[GateDecision, Mapping[str, Any]]]
    ) -> list[TaskHarnessArtifact]:
        del decisions  # reserved for future stability-window evidence
        receipts = self.workspace.promotion_receipts()
        hashes: list[str] = []
        if receipts:
            hashes.append(receipts[0]["previous_champion_sha256"])
            hashes.extend(receipt["candidate_sha256"] for receipt in receipts)
        else:
            parentless = []
            for path in self.workspace.artifacts_root.glob("*.json"):
                artifact = self.workspace.load_artifact(path.stem)
                if artifact.parent_sha256 is None:
                    parentless.append(artifact.sha256)
            hashes.extend(sorted(parentless))
        unique = list(dict.fromkeys(hashes))[: self.policy.early_stable_limit]
        return [self.workspace.load_artifact(sha256) for sha256 in unique]


def validate_mutation(
    *,
    parent: TaskHarnessArtifact,
    candidate: TaskHarnessArtifact,
    directive: MutationDirective,
) -> int:
    if candidate.parent_sha256 != parent.sha256:
        raise ValueError("portfolio candidate parent differs from its mutation source")
    if candidate.version != parent.version + 1:
        raise ValueError("portfolio candidate version is not sequential to its parent")
    distance = harness_distance(parent.spec, candidate.spec)
    if distance == 0:
        raise ValueError("portfolio candidate contains no executable change")
    if distance > directive.max_changed_nodes:
        raise ValueError("portfolio candidate exceeds the targeted mutation size")
    return distance


def retain_diverse_pareto(
    *,
    workspace: HarnessWorkspace,
    evaluator_contract_sha256: str,
    limit: int,
) -> tuple[TaskHarnessArtifact, ...]:
    """Return a greedy, structurally diverse view without deleting the archive."""

    if limit < 1:
        raise ValueError("Pareto retention limit must be positive")
    policy = ChampionArchivePolicy(
        workspace=workspace,
        evaluator_contract_sha256=evaluator_contract_sha256,
    )
    candidates = [workspace.load_artifact(item) for item in policy.pareto_sha256s()]
    if not candidates:
        return ()
    selected = [max(candidates, key=lambda item: (item.version, item.sha256))]
    remaining = [item for item in candidates if item.sha256 != selected[0].sha256]
    while remaining and len(selected) < limit:
        chosen = max(
            remaining,
            key=lambda item: (
                min(harness_distance(item.spec, kept.spec) for kept in selected),
                item.sha256,
            ),
        )
        selected.append(chosen)
        remaining = [item for item in remaining if item.sha256 != chosen.sha256]
    return tuple(selected)


def sorted_gate_candidates(
    candidates: Iterable[tuple[str, GateDecision]],
) -> tuple[tuple[str, GateDecision], ...]:
    """Rank promotable challengers; caller still performs the atomic promotion."""

    eligible = [
        item for item in candidates if item[1].passed and item[1].credible_improvement
    ]
    return tuple(
        sorted(
            eligible,
            key=lambda item: (-float(item[1].utility), item[1].candidate_sha256),
        )
    )


__all__ = [
    "ChampionArchivePolicy",
    "GateDecision",
    "MutationDirective",
    "PortfolioEvolutionPolicy",
    "harness_distance",
    "retain_diverse_pareto",
    "sorted_gate_candidates",
    "validate_mutation",
]
