"""Typed self-evolution for the upper Builder.

This module is deliberately narrower than HyperAgents' arbitrary repository
editing.  A Builder child may replace the typed policies that drive Task
Harness proposals, while the external controller remains the authority for
evaluation, budgets, gates, and safety boundaries.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_./:+-]{0,127}")

_META_POLICY_KEYS = {
    "schema_version",
    "diagnostic_focus",
    "memory_views",
    "mutation_families",
    "search_mode",
    "parent_selection",
    "stagnation_window",
    "exploration_rate",
    "proposal_budget",
    "failure_recovery",
}
_TASK_POLICY_KEYS = {
    "schema_version",
    "rule_id",
    "role_graph",
    "memory_views",
    "tools",
    "parent_strategy",
    "workflow",
    "scheduler_mode",
    "recovery_mode",
    "directive",
    "execution_mode",
}
_PROPOSAL_KEYS = {
    "schema_version",
    "base_builder_sha256",
    "changed_meta_components",
    "reason",
    "expected_effect",
    "meta_policy",
    "task_harness_policy",
}

_META_FOCUS = frozenset(
    {"failures", "score_trend", "structure", "cost", "reliability", "lineage"}
)
_META_MEMORY = frozenset(
    {"current", "best", "failures", "structural_diverse", "builder_history"}
)
_MUTATION_FAMILIES = frozenset(
    {"repair", "discipline", "restart", "recombine", "workflow"}
)
_SEARCH_MODES = frozenset({"explore", "exploit", "explore_then_exploit"})
_PARENT_SELECTION = frozenset({"best", "lineage_diverse", "score_child_balanced"})
_RECOVERY = frozenset({"preserve", "repair", "reset"})

_ROLE_IDS = frozenset(
    {
        "task_analyst",
        "performance_analyst",
        "compiler_analyst",
        "critic",
        "generator",
        "verifier",
    }
)
_TASK_MEMORY = frozenset(
    {"current", "best", "failures", "structural_diverse", "cross_instance_records"}
)
_TASK_TOOLS = frozenset(
    {
        "task_semantics",
        "score_history",
        "static_structure",
        "public_profile",
        "compiler_observation",
        "code_diff",
    }
)
_WORKFLOW = frozenset(
    {
        "analyze",
        "select_parent",
        "inspect",
        "hypothesize",
        "criticize",
        "generate",
        "verify_contract",
    }
)
_PARENT_STRATEGIES = frozenset(
    {"reference", "incumbent", "stable_best", "restart", "recombine"}
)
_SCHEDULERS = frozenset({"single_candidate", "repair_first", "explore_then_exploit"})
_TASK_RECOVERY = frozenset({"repair_then_reset", "reset_immediately", "preserve_failure"})
_EXECUTION_MODES = frozenset({"single_solution", "multi_step"})
_TASK_RULES = frozenset(
    {
        "contract_compatibility",
        "discipline",
        "dream",
        "law_inversion",
        "recombination",
        "correctness_recovery",
    }
)

_IMMUTABLE_BOUNDARY = frozenset(
    {
        "evaluator",
        "hidden_labels",
        "budget",
        "ledger",
        "gate",
        "promotion",
        "sandbox",
        "task_split",
    }
)


def _canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _safe_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not _SAFE_ID.fullmatch(value):
        raise ValueError(f"unsafe {label}")
    return value


def _strict_keys(payload: Mapping[str, Any], expected: set[str], label: str) -> None:
    actual = set(payload)
    if actual != expected:
        raise ValueError(
            f"{label} keys differ: missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}"
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _unique_ids(values: Any, allowed: frozenset[str], label: str) -> tuple[str, ...]:
    if not isinstance(values, list) or not values:
        raise ValueError(f"{label} must be a non-empty list")
    result = tuple(_safe_id(item, f"{label} item") for item in values)
    if len(result) != len(set(result)):
        raise ValueError(f"{label} contains duplicates")
    unknown = set(result) - allowed
    if unknown:
        raise ValueError(f"unknown {label}: {sorted(unknown)}")
    return result


@dataclass(frozen=True)
class MetaPolicy:
    schema_version: int
    diagnostic_focus: tuple[str, ...]
    memory_views: tuple[str, ...]
    mutation_families: tuple[str, ...]
    search_mode: str
    parent_selection: str
    stagnation_window: int
    exploration_rate: float
    proposal_budget: int
    failure_recovery: str

    @classmethod
    def default(cls) -> "MetaPolicy":
        return cls(
            schema_version=1,
            diagnostic_focus=("failures", "score_trend", "structure"),
            memory_views=("current", "best", "failures"),
            mutation_families=("repair", "discipline", "restart"),
            search_mode="explore_then_exploit",
            parent_selection="score_child_balanced",
            stagnation_window=3,
            exploration_rate=0.35,
            proposal_budget=1,
            failure_recovery="repair",
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "MetaPolicy":
        _strict_keys(payload, _META_POLICY_KEYS, "meta policy")
        schema_version = payload["schema_version"]
        if schema_version != 1:
            raise ValueError("unsupported meta policy schema")
        focus = _unique_ids(payload["diagnostic_focus"], _META_FOCUS, "diagnostic focus")
        memory = _unique_ids(payload["memory_views"], _META_MEMORY, "meta memory views")
        mutations = _unique_ids(
            payload["mutation_families"], _MUTATION_FAMILIES, "mutation families"
        )
        search_mode = payload["search_mode"]
        parent_selection = payload["parent_selection"]
        failure_recovery = payload["failure_recovery"]
        if search_mode not in _SEARCH_MODES:
            raise ValueError("unsupported meta search mode")
        if parent_selection not in _PARENT_SELECTION:
            raise ValueError("unsupported meta parent selection")
        if failure_recovery not in _RECOVERY:
            raise ValueError("unsupported meta recovery")
        stagnation_window = payload["stagnation_window"]
        proposal_budget = payload["proposal_budget"]
        exploration_rate = payload["exploration_rate"]
        if type(stagnation_window) is not int or not 1 <= stagnation_window <= 12:
            raise ValueError("stagnation window must be an integer in 1..12")
        if type(proposal_budget) is not int or not 1 <= proposal_budget <= 4:
            raise ValueError("proposal budget must be an integer in 1..4")
        if type(exploration_rate) not in (int, float) or not math.isfinite(exploration_rate):
            raise ValueError("exploration rate must be finite")
        if not 0.0 <= float(exploration_rate) <= 1.0:
            raise ValueError("exploration rate must be in 0..1")
        return cls(
            schema_version=1,
            diagnostic_focus=focus,
            memory_views=memory,
            mutation_families=mutations,
            search_mode=search_mode,
            parent_selection=parent_selection,
            stagnation_window=stagnation_window,
            exploration_rate=float(exploration_rate),
            proposal_budget=proposal_budget,
            failure_recovery=failure_recovery,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "diagnostic_focus": list(self.diagnostic_focus),
            "memory_views": list(self.memory_views),
            "mutation_families": list(self.mutation_families),
            "search_mode": self.search_mode,
            "parent_selection": self.parent_selection,
            "stagnation_window": self.stagnation_window,
            "exploration_rate": self.exploration_rate,
            "proposal_budget": self.proposal_budget,
            "failure_recovery": self.failure_recovery,
        }


@dataclass(frozen=True)
class TaskHarnessPolicy:
    """The typed lower-Harness decision that a Builder is allowed to produce."""

    schema_version: int
    rule_id: str
    role_graph: tuple[str, ...]
    memory_views: tuple[str, ...]
    tools: tuple[str, ...]
    parent_strategy: str
    workflow: tuple[str, ...]
    scheduler_mode: str
    recovery_mode: str
    directive: str
    execution_mode: str = "single_solution"

    @classmethod
    def default(cls) -> "TaskHarnessPolicy":
        return cls(
            schema_version=1,
            rule_id="discipline",
            role_graph=("task_analyst", "generator", "verifier"),
            memory_views=("current",),
            tools=("task_semantics",),
            parent_strategy="reference",
            workflow=("analyze", "generate", "verify_contract"),
            scheduler_mode="single_candidate",
            recovery_mode="preserve_failure",
            directive="Produce one complete candidate that satisfies the task contract.",
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "TaskHarnessPolicy":
        expected = set(_TASK_POLICY_KEYS)
        actual = set(payload)
        if actual not in (expected, expected - {"execution_mode"}):
            _strict_keys(payload, expected, "task Harness policy")
        if payload["schema_version"] != 1:
            raise ValueError("unsupported task Harness policy schema")
        rule_id = payload["rule_id"]
        if rule_id not in _TASK_RULES:
            raise ValueError("unsupported task Harness rule")
        role_graph = _unique_ids(payload["role_graph"], _ROLE_IDS, "role graph")
        memory_views = _unique_ids(payload["memory_views"], _TASK_MEMORY, "task memory views")
        tools = _unique_ids(payload["tools"], _TASK_TOOLS, "task tools")
        workflow = _unique_ids(payload["workflow"], _WORKFLOW, "task workflow")
        if "generator" not in role_graph or "verifier" not in role_graph:
            raise ValueError("task role graph requires generator and verifier")
        if "generate" not in workflow or "verify_contract" not in workflow:
            raise ValueError("task workflow requires generate and verify_contract")
        if workflow.index("generate") > workflow.index("verify_contract"):
            raise ValueError("task verification must follow generation")
        parent_strategy = payload["parent_strategy"]
        scheduler_mode = payload["scheduler_mode"]
        recovery_mode = payload["recovery_mode"]
        execution_mode = payload.get("execution_mode", "single_solution")
        if parent_strategy not in _PARENT_STRATEGIES:
            raise ValueError("unsupported task parent strategy")
        if scheduler_mode not in _SCHEDULERS:
            raise ValueError("unsupported task scheduler")
        if recovery_mode not in _TASK_RECOVERY:
            raise ValueError("unsupported task recovery")
        if execution_mode not in _EXECUTION_MODES:
            raise ValueError("unsupported execution mode")
        directive = payload["directive"]
        if not isinstance(directive, str) or not directive.strip() or len(directive) > 8_000:
            raise ValueError("task directive is invalid")
        return cls(
            schema_version=1,
            rule_id=rule_id,
            role_graph=role_graph,
            memory_views=memory_views,
            tools=tools,
            parent_strategy=parent_strategy,
            workflow=workflow,
            scheduler_mode=scheduler_mode,
            recovery_mode=recovery_mode,
            directive=directive,
            execution_mode=execution_mode,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "rule_id": self.rule_id,
            "role_graph": list(self.role_graph),
            "memory_views": list(self.memory_views),
            "tools": list(self.tools),
            "parent_strategy": self.parent_strategy,
            "workflow": list(self.workflow),
            "scheduler_mode": self.scheduler_mode,
            "recovery_mode": self.recovery_mode,
            "directive": self.directive,
            "execution_mode": self.execution_mode,
        }

    def to_harness_decision(self) -> Any:
        """Convert into v1's lower-Harness schema without widening its API."""
        from .schema import HarnessDecision

        payload = {
            "schema_version": self.schema_version,
            "rule_id": self.rule_id,
            "role_graph": self.role_graph,
            "memory_views": self.memory_views,
            "tools": self.tools,
            "parent_strategy": self.parent_strategy,
            "workflow": self.workflow,
            "scheduler_mode": self.scheduler_mode,
            "recovery_mode": self.recovery_mode,
            "kernel_directive": self.directive,
        }
        try:
            return HarnessDecision(**payload, execution_mode=self.execution_mode)
        except TypeError:
            # Older v1 HarnessDecision has no execution_mode field.
            return HarnessDecision(**payload)


@dataclass(frozen=True)
class BuilderArtifact:
    schema_version: int
    builder_id: str
    parent_builder_sha256: str | None
    task_harness_policy: TaskHarnessPolicy
    meta_policy: MetaPolicy

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported Builder artifact schema")
        _safe_id(self.builder_id, "builder id")
        if self.parent_builder_sha256 is not None and not _SHA256.fullmatch(
            self.parent_builder_sha256
        ):
            raise ValueError("invalid parent Builder sha256")

    @classmethod
    def initial(cls, builder_id: str = "builder-v001") -> "BuilderArtifact":
        return cls(
            schema_version=1,
            builder_id=builder_id,
            parent_builder_sha256=None,
            task_harness_policy=TaskHarnessPolicy.default(),
            meta_policy=MetaPolicy.default(),
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "BuilderArtifact":
        _strict_keys(
            payload,
            {
                "schema_version",
                "builder_id",
                "parent_builder_sha256",
                "task_harness_policy",
                "meta_policy",
            },
            "Builder artifact",
        )
        parent = payload["parent_builder_sha256"]
        if parent is not None and not isinstance(parent, str):
            raise ValueError("parent Builder sha256 must be null or a string")
        return cls(
            schema_version=payload["schema_version"],
            builder_id=_safe_id(payload["builder_id"], "builder id"),
            parent_builder_sha256=parent,
            task_harness_policy=TaskHarnessPolicy.from_dict(payload["task_harness_policy"]),
            meta_policy=MetaPolicy.from_dict(payload["meta_policy"]),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "builder_id": self.builder_id,
            "parent_builder_sha256": self.parent_builder_sha256,
            "task_harness_policy": self.task_harness_policy.to_dict(),
            "meta_policy": self.meta_policy.to_dict(),
        }

    @property
    def sha256(self) -> str:
        return _sha256(self.to_dict())


@dataclass(frozen=True)
class BuilderPublicState:
    """Public, task-bound input to the fixed Builder scaffold compiler."""

    schema_version: int
    task_id: str
    round_index: int
    scores: tuple[float | None, ...]
    feedback: str
    diagnostics: Mapping[str, Any]
    memory: Mapping[str, Any]

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported Builder public state schema")
        _safe_id(self.task_id, "Builder public task id")
        if type(self.round_index) is not int or self.round_index < 1:
            raise ValueError("Builder public round index is invalid")
        for score in self.scores:
            if score is not None and (
                type(score) not in (int, float) or not math.isfinite(float(score))
            ):
                raise ValueError("Builder public score is invalid")
        if not isinstance(self.feedback, str) or len(self.feedback) > 32_000:
            raise ValueError("Builder public feedback is invalid")
        if not isinstance(self.diagnostics, Mapping) or not isinstance(
            self.memory, Mapping
        ):
            raise ValueError("Builder public projections must be mappings")
        _canonical_bytes(self.to_dict())

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "task_id": self.task_id,
            "round_index": self.round_index,
            "scores": list(self.scores),
            "feedback": self.feedback,
            "diagnostics": dict(self.diagnostics),
            "memory": dict(self.memory),
        }


@dataclass(frozen=True)
class CompiledBuilderScaffold:
    """Deterministic executable projection of one BuilderArtifact."""

    schema_version: int
    builder_sha256: str
    public_state_sha256: str
    task_id: str
    round_index: int
    search_phase: str
    mutation_family: str
    recovery_action: str
    diagnostic_projection: Mapping[str, Any]
    memory_projection: Mapping[str, Any]
    proposal_slots: tuple[str, ...]
    task_harness_decision: Mapping[str, Any]

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported compiled Builder scaffold schema")
        if not _SHA256.fullmatch(self.builder_sha256) or not _SHA256.fullmatch(
            self.public_state_sha256
        ):
            raise ValueError("compiled Builder scaffold hash binding is invalid")
        _safe_id(self.task_id, "compiled Builder task id")
        if self.search_phase not in {"explore", "exploit"}:
            raise ValueError("compiled Builder search phase is invalid")
        if self.mutation_family not in _MUTATION_FAMILIES:
            raise ValueError("compiled Builder mutation family is invalid")
        if self.recovery_action not in _RECOVERY:
            raise ValueError("compiled Builder recovery action is invalid")
        if not self.proposal_slots or len(self.proposal_slots) > 4:
            raise ValueError("compiled Builder proposal slots are invalid")
        if len(self.proposal_slots) != len(set(self.proposal_slots)):
            raise ValueError("compiled Builder proposal slots contain duplicates")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "builder_sha256": self.builder_sha256,
            "public_state_sha256": self.public_state_sha256,
            "task_id": self.task_id,
            "round_index": self.round_index,
            "search_phase": self.search_phase,
            "mutation_family": self.mutation_family,
            "recovery_action": self.recovery_action,
            "diagnostic_projection": dict(self.diagnostic_projection),
            "memory_projection": dict(self.memory_projection),
            "proposal_slots": list(self.proposal_slots),
            "task_harness_decision": dict(self.task_harness_decision),
        }

    @property
    def sha256(self) -> str:
        return _sha256(self.to_dict())

    def harness_decision(self) -> Any:
        from .schema import HarnessDecision

        return HarnessDecision.from_dict(dict(self.task_harness_decision))


class BuilderScaffoldCompiler:
    """Compile typed Builder policy into executable, model-external control flow."""

    _FAILURE_MARKERS = (
        "fail",
        "error",
        "invalid",
        "incorrect",
        "contract",
        "format",
        "timeout",
    )

    def compile(
        self,
        artifact: BuilderArtifact,
        public_state: BuilderPublicState,
    ) -> CompiledBuilderScaffold:
        policy = artifact.meta_policy
        diagnostic_projection = self._diagnostic_projection(policy, public_state)
        memory_projection = {
            key: public_state.memory[key]
            for key in policy.memory_views
            if key in public_state.memory
        }
        search_phase = self._search_phase(artifact, public_state)
        mutation_family = self._mutation_family(
            artifact, public_state, search_phase=search_phase
        )
        decision = self._task_harness_decision(
            artifact, public_state, mutation_family=mutation_family
        )
        slots = tuple(
            f"proposal-{index:03d}" for index in range(1, policy.proposal_budget + 1)
        )
        return CompiledBuilderScaffold(
            schema_version=1,
            builder_sha256=artifact.sha256,
            public_state_sha256=_sha256(public_state.to_dict()),
            task_id=public_state.task_id,
            round_index=public_state.round_index,
            search_phase=search_phase,
            mutation_family=mutation_family,
            recovery_action=policy.failure_recovery,
            diagnostic_projection=diagnostic_projection,
            memory_projection=memory_projection,
            proposal_slots=slots,
            task_harness_decision=decision.to_dict(),
        )

    def _diagnostic_projection(
        self,
        policy: MetaPolicy,
        state: BuilderPublicState,
    ) -> dict[str, Any]:
        projection = {
            key: state.diagnostics[key]
            for key in policy.diagnostic_focus
            if key in state.diagnostics
        }
        valid_scores = [float(score) for score in state.scores if score is not None]
        if "failures" in policy.diagnostic_focus:
            projection["latest_feedback"] = state.feedback
        if "score_trend" in policy.diagnostic_focus:
            projection["score_trend"] = {
                "valid_scores": valid_scores,
                "latest": valid_scores[-1] if valid_scores else None,
                "best": max(valid_scores) if valid_scores else None,
            }
        if "reliability" in policy.diagnostic_focus:
            projection["reliability"] = {
                "valid": len(valid_scores),
                "invalid": len(state.scores) - len(valid_scores),
            }
        return projection

    def _search_phase(
        self,
        artifact: BuilderArtifact,
        state: BuilderPublicState,
    ) -> str:
        mode = artifact.meta_policy.search_mode
        if mode in {"explore", "exploit"}:
            return mode
        digest = hashlib.sha256(
            f"{artifact.sha256}|{state.task_id}|{state.round_index}".encode("utf-8")
        ).digest()
        draw = int.from_bytes(digest[:8], "big") / float(2**64)
        if draw < artifact.meta_policy.exploration_rate:
            return "explore"
        valid = [float(score) for score in state.scores if score is not None]
        window = artifact.meta_policy.stagnation_window
        if len(valid) >= 2:
            recent = valid[-window:]
            earlier = valid[:-len(recent)]
            if earlier and max(recent) <= max(earlier):
                return "explore"
        return "exploit"

    def _mutation_family(
        self,
        artifact: BuilderArtifact,
        state: BuilderPublicState,
        *,
        search_phase: str,
    ) -> str:
        families = artifact.meta_policy.mutation_families
        feedback = state.feedback.lower()
        failed = any(marker in feedback for marker in self._FAILURE_MARKERS)
        if failed and artifact.meta_policy.failure_recovery == "reset" and "restart" in families:
            return "restart"
        if failed and artifact.meta_policy.failure_recovery == "repair" and "repair" in families:
            return "repair"
        if search_phase == "exploit":
            for preferred in ("discipline", "workflow", "repair", "recombine", "restart"):
                if preferred in families:
                    return preferred
        digest = hashlib.sha256(
            f"mutation|{artifact.sha256}|{state.task_id}|{state.round_index}".encode(
                "utf-8"
            )
        ).digest()
        return families[int.from_bytes(digest[:8], "big") % len(families)]

    @staticmethod
    def _task_harness_decision(
        artifact: BuilderArtifact,
        state: BuilderPublicState,
        *,
        mutation_family: str,
    ) -> Any:
        from .schema import HarnessDecision

        policy = artifact.task_harness_policy
        payload = {
            "schema_version": policy.schema_version,
            "rule_id": policy.rule_id,
            "role_graph": list(policy.role_graph),
            "memory_views": list(policy.memory_views),
            "tools": list(policy.tools),
            "parent_strategy": policy.parent_strategy,
            "workflow": list(policy.workflow),
            "scheduler_mode": policy.scheduler_mode,
            "recovery_mode": policy.recovery_mode,
            "kernel_directive": policy.directive,
            "execution_mode": policy.execution_mode,
        }
        feedback = state.feedback.lower()
        if mutation_family == "repair":
            payload["rule_id"] = (
                "contract_compatibility"
                if "contract" in feedback or "format" in feedback
                else "correctness_recovery"
            )
            payload["recovery_mode"] = "repair_then_reset"
        elif mutation_family == "discipline":
            payload["rule_id"] = "discipline"
        elif mutation_family == "restart":
            payload["rule_id"] = "dream"
            payload["parent_strategy"] = "restart"
            payload["recovery_mode"] = "reset_immediately"
        elif mutation_family == "recombine":
            payload["rule_id"] = "recombination"
            payload["parent_strategy"] = "recombine"
        elif mutation_family == "workflow":
            payload["scheduler_mode"] = "explore_then_exploit"
            payload["execution_mode"] = "multi_step"
        return HarnessDecision.from_dict(payload)


@dataclass(frozen=True)
class BuilderSelfModificationProposal:
    schema_version: int
    base_builder_sha256: str
    changed_meta_components: tuple[str, ...]
    reason: str
    expected_effect: str
    meta_policy: MetaPolicy
    task_harness_policy: TaskHarnessPolicy

    @classmethod
    def from_response(cls, raw_response: str) -> "BuilderSelfModificationProposal":
        if not isinstance(raw_response, str) or not raw_response.strip():
            raise ValueError("Builder self-modification response cannot be empty")
        if len(raw_response) > 128_000:
            raise ValueError("Builder self-modification response is too large")
        try:
            payload = json.loads(raw_response, object_pairs_hook=_unique_object)
        except json.JSONDecodeError as exc:
            raise ValueError("Builder self-modification response is not strict JSON") from exc
        if not isinstance(payload, dict):
            raise ValueError("Builder self-modification proposal must be one object")
        _strict_keys(payload, _PROPOSAL_KEYS, "Builder self-modification proposal")
        if payload["schema_version"] != 1:
            raise ValueError("unsupported self-modification proposal schema")
        base = payload["base_builder_sha256"]
        if not isinstance(base, str) or not _SHA256.fullmatch(base):
            raise ValueError("invalid proposal base Builder sha256")
        changed = _unique_ids(
            payload["changed_meta_components"],
            frozenset(
                {
                    "diagnostic_focus",
                    "memory_views",
                    "mutation_families",
                    "search_mode",
                    "parent_selection",
                    "stagnation_window",
                    "exploration_rate",
                    "proposal_budget",
                    "failure_recovery",
                    "task_harness_policy",
                }
            ),
            "changed meta components",
        )
        reason = payload["reason"]
        expected = payload["expected_effect"]
        if not isinstance(reason, str) or not reason.strip() or len(reason) > 4_000:
            raise ValueError("proposal reason is invalid")
        if not isinstance(expected, str) or not expected.strip() or len(expected) > 4_000:
            raise ValueError("proposal expected effect is invalid")
        return cls(
            schema_version=1,
            base_builder_sha256=base,
            changed_meta_components=changed,
            reason=reason,
            expected_effect=expected,
            meta_policy=MetaPolicy.from_dict(payload["meta_policy"]),
            task_harness_policy=TaskHarnessPolicy.from_dict(payload["task_harness_policy"]),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "base_builder_sha256": self.base_builder_sha256,
            "changed_meta_components": list(self.changed_meta_components),
            "reason": self.reason,
            "expected_effect": self.expected_effect,
            "meta_policy": self.meta_policy.to_dict(),
            "task_harness_policy": self.task_harness_policy.to_dict(),
        }


class BuilderBoundaryError(ValueError):
    """A typed rejection caused by crossing the immutable Controller boundary."""

    def __init__(self, message: str, *, reason_code: str) -> None:
        super().__init__(message)
        self.reason_code = reason_code


class ImmutableBuilderController:
    """Validate and materialize Builder children while owning outer authority."""

    def validate_proposal(
        self,
        parent: BuilderArtifact,
        proposal: BuilderSelfModificationProposal,
    ) -> None:
        if proposal.base_builder_sha256 != parent.sha256:
            raise BuilderBoundaryError(
                "proposal does not bind the current Builder parent",
                reason_code="builder_parent_binding_mismatch",
            )
        before_meta = parent.meta_policy.to_dict()
        after_meta = proposal.meta_policy.to_dict()
        before_task = parent.task_harness_policy.to_dict()
        after_task = proposal.task_harness_policy.to_dict()
        changed = {
            key
            for key in _META_POLICY_KEYS
            if before_meta.get(key) != after_meta.get(key)
        }
        if before_task != after_task:
            changed.add("task_harness_policy")
        declared = set(proposal.changed_meta_components)
        if not changed:
            raise BuilderBoundaryError(
                "self-modification proposal contains no effective change",
                reason_code="no_builder_operational_change",
            )
        if changed != declared:
            raise BuilderBoundaryError(
                "declared Builder changes differ from the typed artifact",
                reason_code="builder_change_set_mismatch",
            )
        illegal = declared & _IMMUTABLE_BOUNDARY
        if illegal:
            raise BuilderBoundaryError(
                f"proposal attempts to modify Controller-owned fields: {sorted(illegal)}",
                reason_code="immutable_controller_boundary",
            )

    def materialize_child(
        self,
        parent: BuilderArtifact,
        proposal: BuilderSelfModificationProposal,
        *,
        child_id: str,
    ) -> BuilderArtifact:
        self.validate_proposal(parent, proposal)
        child = BuilderArtifact(
            schema_version=1,
            builder_id=_safe_id(child_id, "child Builder id"),
            parent_builder_sha256=parent.sha256,
            task_harness_policy=proposal.task_harness_policy,
            meta_policy=proposal.meta_policy,
        )
        if child.sha256 == parent.sha256:
            raise BuilderBoundaryError(
                "materialized Builder child is identical to its parent",
                reason_code="duplicate_builder_artifact",
            )
        return child


class BuilderArchive:
    """Content-addressed, write-once Builder archive for replay and transfer."""

    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.builders_root = self.root / "builders"
        self.head_path = self.root / "head.json"
        self.builders_root.mkdir(parents=True, exist_ok=True)

    def store(self, artifact: BuilderArtifact) -> Path:
        if artifact.parent_builder_sha256 is not None:
            parent_path = self.builders_root / f"{artifact.parent_builder_sha256}.json"
            if not parent_path.is_file() or parent_path.is_symlink():
                raise ValueError("Builder child parent is not present in the archive")
        path = self.builders_root / f"{artifact.sha256}.json"
        content = _canonical_bytes(artifact.to_dict())
        if path.exists():
            if path.is_symlink() or path.read_bytes() != content:
                raise ValueError("Builder archive refuses to overwrite a different artifact")
            return path
        fd, temp_name = tempfile.mkstemp(dir=self.builders_root, suffix=".tmp")
        try:
            with open(fd, "wb", closefd=True) as handle:
                handle.write(content)
                handle.flush()
            Path(temp_name).replace(path)
        except Exception:
            Path(temp_name).unlink(missing_ok=True)
            raise
        return path

    def record_transition(
        self,
        *,
        parent: BuilderArtifact,
        proposal: BuilderSelfModificationProposal,
        child: BuilderArtifact,
    ) -> Path:
        if child.parent_builder_sha256 != parent.sha256:
            raise ValueError("Builder transition parent binding differs")
        payload = {
            "schema_version": 1,
            "parent_builder_sha256": parent.sha256,
            "child_builder_sha256": child.sha256,
            "proposal": proposal.to_dict(),
        }
        path = self.root / "transitions" / f"{child.sha256}.json"
        content = _canonical_bytes(payload)
        if path.exists():
            if path.is_symlink() or path.read_bytes() != content:
                raise ValueError("Builder transition refuses to overwrite a different receipt")
            return path
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, temp_name = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
        try:
            with open(fd, "wb", closefd=True) as handle:
                handle.write(content)
                handle.flush()
            Path(temp_name).replace(path)
        except Exception:
            Path(temp_name).unlink(missing_ok=True)
            raise
        return path

    def load(self, sha256: str) -> BuilderArtifact:
        if not _SHA256.fullmatch(sha256):
            raise ValueError("invalid Builder archive hash")
        path = self.builders_root / f"{sha256}.json"
        if not path.is_file() or path.is_symlink():
            raise FileNotFoundError(sha256)
        artifact = BuilderArtifact.from_dict(json.loads(path.read_text(encoding="utf-8")))
        if artifact.sha256 != sha256:
            raise ValueError("Builder archive artifact hash mismatch")
        return artifact

    def set_head(self, sha256: str) -> None:
        self.load(sha256)
        content = _canonical_bytes({"schema_version": 1, "head_builder_sha256": sha256})
        # The artifact files are write-once; the head is a mutable controller
        # pointer that advances only to an already stored, content-addressed child.
        if self.head_path.is_symlink():
            raise ValueError("Builder archive head cannot be a symlink")
        fd, temp_name = tempfile.mkstemp(dir=self.root, suffix=".head.tmp")
        try:
            with open(fd, "wb", closefd=True) as handle:
                handle.write(content)
                handle.flush()
            Path(temp_name).replace(self.head_path)
        except Exception:
            Path(temp_name).unlink(missing_ok=True)
            raise

    def head(self) -> BuilderArtifact:
        if not self.head_path.is_file():
            raise FileNotFoundError("Builder archive head")
        payload = json.loads(self.head_path.read_text(encoding="utf-8"))
        return self.load(payload["head_builder_sha256"])

    def hashes(self) -> tuple[str, ...]:
        return tuple(sorted(path.stem for path in self.builders_root.glob("*.json")))


@dataclass(frozen=True)
class BuilderImpK:
    builder_sha256: str
    baseline_score: float
    best_score: float
    k: int
    valid_attempts: int
    improvement: float

    @classmethod
    def from_scores(
        cls,
        *,
        builder_sha256: str,
        baseline_score: float,
        scores: list[float | None] | tuple[float | None, ...],
        k: int,
    ) -> "BuilderImpK":
        if not _SHA256.fullmatch(builder_sha256):
            raise ValueError("invalid Builder score binding")
        if type(k) is not int or k <= 0:
            raise ValueError("BuilderImp@k requires a positive k")
        if not isinstance(baseline_score, (int, float)) or not math.isfinite(baseline_score):
            raise ValueError("baseline score must be finite")
        bounded = list(scores[:k])
        valid = [float(value) for value in bounded if isinstance(value, (int, float)) and math.isfinite(value)]
        best = max([float(baseline_score), *valid])
        return cls(
            builder_sha256=builder_sha256,
            baseline_score=float(baseline_score),
            best_score=best,
            k=k,
            valid_attempts=len(valid),
            improvement=best - float(baseline_score),
        )


@dataclass(frozen=True)
class BuilderEvolutionResult:
    status: str
    parent_builder_sha256: str
    child_builder_sha256: str | None
    reason_code: str | None


class SelfEvolvingBuilder:
    """Small orchestration shell for one Builder lineage.

    The shell deliberately accepts a completed model response instead of
    invoking a provider.  Provider claims, evaluator calls, and entitlements
    remain owned by the surrounding Moss controller.
    """

    def __init__(
        self,
        *,
        archive: BuilderArchive,
        controller: ImmutableBuilderController | None = None,
        initial: BuilderArtifact | None = None,
    ) -> None:
        self.archive = archive
        self.controller = controller or ImmutableBuilderController()
        if initial is not None:
            self.current = initial
            self.archive.store(initial)
            self.archive.set_head(initial.sha256)
        else:
            try:
                self.current = self.archive.head()
            except FileNotFoundError:
                self.current = BuilderArtifact.initial()
                self.archive.store(self.current)
                self.archive.set_head(self.current.sha256)

    def compile_current(
        self,
        public_state: BuilderPublicState,
        *,
        compiler: BuilderScaffoldCompiler | None = None,
    ) -> CompiledBuilderScaffold:
        """Compile the persisted head into the next task's executable scaffold."""
        return (compiler or BuilderScaffoldCompiler()).compile(
            self.current, public_state
        )

    def evolve_from_response(
        self,
        raw_response: str,
        *,
        child_id: str,
    ) -> tuple[BuilderArtifact, BuilderEvolutionResult]:
        parent = self.current
        try:
            proposal = BuilderSelfModificationProposal.from_response(raw_response)
            child = self.controller.materialize_child(parent, proposal, child_id=child_id)
            self.archive.store(child)
            self.archive.record_transition(parent=parent, proposal=proposal, child=child)
            self.archive.set_head(child.sha256)
        except (BuilderBoundaryError, ValueError) as exc:
            reason_code = getattr(exc, "reason_code", "invalid_builder_proposal")
            return parent, BuilderEvolutionResult(
                status="rejected",
                parent_builder_sha256=parent.sha256,
                child_builder_sha256=None,
                reason_code=reason_code,
            )
        self.current = child
        return child, BuilderEvolutionResult(
            status="accepted",
            parent_builder_sha256=parent.sha256,
            child_builder_sha256=child.sha256,
            reason_code=None,
        )
