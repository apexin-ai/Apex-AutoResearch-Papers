from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from optimization_lab.feedback import FeedbackCard
from optimization_lab.generation import _sanitize_private_paths
from optimization_lab.profiling import ProfileSummary, ProfilerCapabilities


P2B_MODES = {
    "profile_exploit",
    "architecture_reset",
    "counterfactual",
    "recombinant_frontier",
}
P2B_DIAGNOSTIC_LEVELS = {"light", "full"}
P2B_MUTATION_SCOPES = {
    "kernel_count",
    "fusion_boundary",
    "reduction_structure",
    "thread_mapping",
    "memory_layout",
    "tiling",
    "pipeline",
    "compiler_schedule",
    "math_formulation",
    "launch_geometry",
    "register_pressure",
    "shared_memory",
    "vectorization",
    "numerical_method",
    "recombination",
}
P2B_SKILLS = {
    "task_semantics",
    "score_trend",
    "code_diff",
    "timeline_analysis",
    "compiler_resource_analysis",
    "memory_access_analysis",
    "occupancy_reasoning",
    "counterfactual_generation",
    "architecture_rebuild",
    "frontier_recombination",
    "numerical_correctness",
    "novelty_check",
    "stability_check",
}
P2B_TOOLS = {
    "score",
    "static_structure",
    "nsys_timeline",
    "triton_compiler_metadata",
    "ptx_sass_summary",
    "hardware_counters",
}
P2B_MEMORY_VIEWS = {
    "starting_point",
    "previous",
    "recent",
    "historical_best",
    "stable_frontier",
    "structurally_novel",
    "frozen_frontier",
    "disproved_ideas",
}
_FIELDS = {
    "mode",
    "base_candidate_id",
    "diagnostic_level",
    "observed_evidence",
    "primary_hypothesis",
    "score_assessment",
    "direction_change_reason",
    "mutation_scope",
    "enabled_skills",
    "tool_plan",
    "memory_views",
    "workflow_steps",
    "avoid_repeats",
    "kernel_instructions",
    "force_restart",
    "structural_change",
}


class InvalidP2bPolicy(ValueError):
    pass


@dataclass(frozen=True)
class ScoreTrend:
    current_score: float | None
    previous_score: float | None
    historical_best: float | None
    starting_score: float
    delta_vs_previous_pct: float | None
    delta_vs_best_pct: float | None
    delta_vs_start_pct: float | None
    in_noise_band: bool
    significant_improvement: bool

    @classmethod
    def build(
        cls,
        *,
        current_score: float | None,
        previous_score: float | None,
        historical_best: float | None,
        starting_score: float,
    ) -> "ScoreTrend":
        if starting_score <= 0:
            raise ValueError("starting score must be positive")
        for value in (current_score, previous_score, historical_best):
            if value is not None and value <= 0:
                raise ValueError("observed scores must be positive")

        def delta(value: float | None, baseline: float | None) -> float | None:
            if value is None or baseline is None:
                return None
            return (value / baseline - 1.0) * 100.0

        vs_previous = delta(current_score, previous_score)
        vs_best = delta(current_score, historical_best)
        vs_start = delta(current_score, starting_score)
        return cls(
            current_score=current_score,
            previous_score=previous_score,
            historical_best=historical_best,
            starting_score=starting_score,
            delta_vs_previous_pct=vs_previous,
            delta_vs_best_pct=vs_best,
            delta_vs_start_pct=vs_start,
            in_noise_band=vs_previous is not None and abs(vs_previous) < 2.0,
            significant_improvement=(
                current_score is not None
                and historical_best is not None
                and current_score >= historical_best * 1.02
            ),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class P2bPolicy:
    mode: str
    base_candidate_id: str
    diagnostic_level: str
    observed_evidence: tuple[str, ...]
    primary_hypothesis: str
    score_assessment: str
    direction_change_reason: str
    mutation_scope: tuple[str, ...]
    enabled_skills: tuple[str, ...]
    tool_plan: tuple[str, ...]
    memory_views: tuple[str, ...]
    workflow_steps: tuple[str, ...]
    avoid_repeats: tuple[str, ...]
    kernel_instructions: tuple[str, ...]
    force_restart: bool
    structural_change: bool

    def __post_init__(self) -> None:
        if self.mode not in P2B_MODES:
            raise InvalidP2bPolicy("unsupported P2b policy mode")
        if self.diagnostic_level not in P2B_DIAGNOSTIC_LEVELS:
            raise InvalidP2bPolicy("unsupported P2b diagnostic level")
        if not re.fullmatch(
            r"(?:reference|[A-Za-z0-9][A-Za-z0-9._-]{0,127})",
            self.base_candidate_id,
        ):
            raise InvalidP2bPolicy("unsafe policy base candidate")
        if not self.mutation_scope or not set(self.mutation_scope).issubset(
            P2B_MUTATION_SCOPES
        ):
            raise InvalidP2bPolicy("policy mutation scope is empty or unsupported")
        if len(set(self.mutation_scope)) != len(self.mutation_scope):
            raise InvalidP2bPolicy("policy mutation scope contains duplicates")
        for values, allowed, label in (
            (self.enabled_skills, P2B_SKILLS, "enabled skills"),
            (self.tool_plan, P2B_TOOLS, "tool plan"),
            (self.memory_views, P2B_MEMORY_VIEWS, "memory views"),
        ):
            if not values or not set(values).issubset(allowed):
                raise InvalidP2bPolicy(f"policy {label} is empty or unsupported")
            if len(set(values)) != len(values):
                raise InvalidP2bPolicy(f"policy {label} contains duplicates")
        if "score" not in self.tool_plan:
            raise InvalidP2bPolicy("every P2b policy must keep the score tool enabled")
        if "score_trend" not in self.enabled_skills:
            raise InvalidP2bPolicy("every P2b policy must inspect score trend")
        if len(self.workflow_steps) < 3 or len(self.workflow_steps) > 10:
            raise InvalidP2bPolicy("policy workflow must contain 3 to 10 steps")
        for step in self.workflow_steps:
            _validate_text(step, "workflow step", maximum=600)
        for values, label, maximum in (
            (self.observed_evidence, "observed evidence", 8),
            (self.avoid_repeats, "avoid repeats", 8),
            (self.kernel_instructions, "kernel instructions", 10),
        ):
            if not values or len(values) > maximum:
                raise InvalidP2bPolicy(f"policy {label} has an invalid item count")
            for value in values:
                _validate_text(value, label, maximum=800)
        for value, label in (
            (self.primary_hypothesis, "primary hypothesis"),
            (self.score_assessment, "score assessment"),
            (self.direction_change_reason, "direction change reason"),
        ):
            _validate_text(value, label, maximum=1200)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_harness_text(self) -> str:
        evidence = "\n".join(f"- {item}" for item in self.observed_evidence)
        avoid = "\n".join(f"- {item}" for item in self.avoid_repeats)
        actions = "\n".join(f"{index}. {item}" for index, item in enumerate(self.kernel_instructions, 1))
        scopes = ", ".join(self.mutation_scope)
        skills = ", ".join(self.enabled_skills)
        tools = ", ".join(self.tool_plan)
        memory = ", ".join(self.memory_views)
        workflow = "\n".join(
            f"{index}. {item}" for index, item in enumerate(self.workflow_steps, 1)
        )
        return f"""# P2B task-specialist Harness

Mode: {self.mode}
Base candidate: {self.base_candidate_id}
Diagnostic level: {self.diagnostic_level}
Structural change required: {str(self.structural_change).lower()}
Forced restart: {str(self.force_restart).lower()}

## Observed evidence
{evidence}

## Score assessment
{self.score_assessment}

## Primary hypothesis
{self.primary_hypothesis}

## Why this direction
{self.direction_change_reason}

## Allowed structural scope
{scopes}

## Enabled task skills
{skills}

## Tool plan
{tools}

## Memory views
{memory}

## Workflow
{workflow}

## Do not repeat
{avoid}

## Kernel-generation actions
{actions}

Always preserve the official task semantics. Produce one complete ModelNew candidate.
Do not change the benchmark, scorer, model, GPU, precision, or correctness gate.
"""


@dataclass(frozen=True)
class P2bPolicyVersion:
    version_id: str
    parent_version_id: str | None
    policy: P2bPolicy
    sha256: str

    @classmethod
    def create(
        cls,
        *,
        version_id: str,
        parent_version_id: str | None,
        policy: P2bPolicy,
    ) -> "P2bPolicyVersion":
        _validate_version(version_id)
        if parent_version_id is not None:
            _validate_version(parent_version_id)
        canonical = json.dumps(
            policy.to_dict(), ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )
        return cls(
            version_id=version_id,
            parent_version_id=parent_version_id,
            policy=policy,
            sha256=hashlib.sha256(canonical.encode()).hexdigest(),
        )

    @classmethod
    def from_response(
        cls,
        *,
        version_id: str,
        parent: "P2bPolicyVersion",
        response: str,
        allowed_base_candidate_ids: set[str],
        available_tools: set[str] | None = None,
        require_direction_change: bool = False,
        require_structural_change: bool = False,
        require_restart: bool = False,
    ) -> "P2bPolicyVersion":
        _validate_version(version_id)
        expected = int(parent.version_id[1:]) + 1
        if version_id != f"v{expected:03d}":
            raise InvalidP2bPolicy("P2b policy versions must advance exactly one step")
        if len(response) > 10_000 or "\x00" in response:
            raise InvalidP2bPolicy("P2b policy response exceeds its content boundary")
        if _contains_absolute_path(response):
            raise InvalidP2bPolicy("P2b policy must not contain an absolute path")
        data = _load_response_object(response)
        if not isinstance(data, dict) or set(data) != _FIELDS:
            raise InvalidP2bPolicy("P2b policy JSON fields do not match the frozen schema")
        try:
            policy = P2bPolicy(
                mode=str(data["mode"]),
                base_candidate_id=str(data["base_candidate_id"]),
                diagnostic_level=str(data["diagnostic_level"]),
                observed_evidence=_string_tuple(data["observed_evidence"]),
                primary_hypothesis=str(data["primary_hypothesis"]),
                score_assessment=str(data["score_assessment"]),
                direction_change_reason=str(data["direction_change_reason"]),
                mutation_scope=_string_tuple(data["mutation_scope"]),
                enabled_skills=_string_tuple(data["enabled_skills"]),
                tool_plan=_string_tuple(data["tool_plan"]),
                memory_views=_string_tuple(data["memory_views"]),
                workflow_steps=_string_tuple(data["workflow_steps"]),
                avoid_repeats=_string_tuple(data["avoid_repeats"]),
                kernel_instructions=_string_tuple(data["kernel_instructions"]),
                force_restart=_strict_bool(data["force_restart"]),
                structural_change=_strict_bool(data["structural_change"]),
            )
        except (TypeError, ValueError) as exc:
            if isinstance(exc, InvalidP2bPolicy):
                raise
            raise InvalidP2bPolicy(f"invalid P2b policy value: {exc}") from exc
        if policy.base_candidate_id not in allowed_base_candidate_ids | {"reference"}:
            raise InvalidP2bPolicy("policy base candidate is outside the frozen lane")
        if available_tools is not None and not set(policy.tool_plan).issubset(
            available_tools
        ):
            raise InvalidP2bPolicy("policy requested an unavailable profiler tool")
        changed = (
            policy.mode != parent.policy.mode
            or policy.base_candidate_id != parent.policy.base_candidate_id
            or policy.mutation_scope != parent.policy.mutation_scope
            or policy.enabled_skills != parent.policy.enabled_skills
            or policy.tool_plan != parent.policy.tool_plan
            or policy.memory_views != parent.policy.memory_views
            or policy.workflow_steps != parent.policy.workflow_steps
        )
        if require_direction_change and not changed:
            raise InvalidP2bPolicy(
                "score did not improve, so the next policy must change direction"
            )
        if require_structural_change and not policy.structural_change:
            raise InvalidP2bPolicy("this round requires a structural change")
        if require_restart:
            if not policy.force_restart:
                raise InvalidP2bPolicy("this round requires a forced restart")
            if policy.base_candidate_id == parent.policy.base_candidate_id:
                raise InvalidP2bPolicy("forced restart must select a different base")
        return cls.create(
            version_id=version_id,
            parent_version_id=parent.version_id,
            policy=policy,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "version_id": self.version_id,
            "parent_version_id": self.parent_version_id,
            "policy": self.policy.to_dict(),
            "sha256": self.sha256,
        }


@dataclass(frozen=True)
class P2bPolicyEvolutionRequest:
    task_id: str
    lane_id: str
    strategy: str
    target_version_id: str
    current: P2bPolicyVersion
    task_card: str
    feedback_history: tuple[FeedbackCard, ...]
    current_trend: ScoreTrend
    profile_history: tuple[ProfileSummary, ...]
    allowed_base_candidate_ids: tuple[str, ...]
    require_direction_change: bool
    require_structural_change: bool
    require_restart: bool
    capabilities: ProfilerCapabilities

    def to_prompt(self) -> str:
        feedback = [
            {
                "candidate_id": card.candidate_id,
                "outcome": card.outcome,
                "compiled": card.compiled,
                "correct": card.correct,
                "candidate_runtime_ms": card.candidate_runtime_ms,
                "reference_runtime_ms": card.reference_runtime_ms,
                "speedup": card.speedup_vs_eager,
                "error_summary": _sanitize_private_paths(card.error_summary)[:800],
            }
            for card in self.feedback_history
        ]
        profiles = [profile.to_public_dict() for profile in self.profile_history]
        available_tools = sorted(
            tool
            for tool in P2B_TOOLS
            if tool != "hardware_counters" or self.capabilities.hardware_counters
        )
        constraints = {
            "task_id": self.task_id,
            "lane_id": self.lane_id,
            "strategy": self.strategy,
            "target_version_id": self.target_version_id,
            "current_policy": self.current.policy.to_dict(),
            "allowed_base_candidate_ids": list(self.allowed_base_candidate_ids),
            "allowed_modes": sorted(P2B_MODES),
            "allowed_mutation_scopes": sorted(P2B_MUTATION_SCOPES),
            "allowed_skills": sorted(P2B_SKILLS),
            "allowed_tools": available_tools,
            "allowed_memory_views": sorted(P2B_MEMORY_VIEWS),
            "require_direction_change": self.require_direction_change,
            "require_structural_change": self.require_structural_change,
            "require_restart": self.require_restart,
        }
        return f"""You are the optimizer of a task-specific KernelBench Harness, not the Kernel generator.
Return exactly one JSON object with the same fields as current_policy. No Markdown.

The Harness may change its input base, task skills, analysis tools, memory views,
workflow, bottleneck hypothesis, and legal Kernel mutation scope. Every selection must
affect the next action. The score gate is mandatory and cannot be disabled.

Always inspect the current score, the previous score, the historical best, and the
frozen starting score. If the score did not improve by at least two percent, change
at least one real search dimension. Do not merely rewrite prose or retune num_warps.
If require_restart is true, select a different base and rebuild the main structure.
Never fabricate unavailable profiler counters; missing means unavailable.

## Task card
{self.task_card}

## Current score trend
{json.dumps(self.current_trend.to_dict(), ensure_ascii=False, indent=2)}

## This lane's scored history
{json.dumps(feedback, ensure_ascii=False, indent=2)}

## This lane's public profiler evidence
{json.dumps(profiles, ensure_ascii=False, indent=2)}

## Profiler capabilities
{json.dumps(self.capabilities.to_dict(), ensure_ascii=False, indent=2)}

MACHINE_CONSTRAINTS_JSON
```json
{json.dumps(constraints, ensure_ascii=False, sort_keys=True)}
```
"""


class P2bPolicyArchive:
    """Immutable structured Harness versions for exactly one P2b lane."""

    def __init__(self, scope_root: Path):
        self.scope_root = scope_root.resolve()

    def store_seed(self, version: P2bPolicyVersion) -> P2bPolicyVersion:
        if version.version_id != "v001" or version.parent_version_id is not None:
            raise ValueError("P2b seed policy must be v001 without a parent")
        return self._store(
            version,
            raw_response=json.dumps(version.policy.to_dict(), ensure_ascii=False),
            source="frozen_seed",
            prompt_sha256=None,
        )

    def store_generated(
        self,
        version: P2bPolicyVersion,
        *,
        raw_response: str,
        prompt_sha256: str,
    ) -> P2bPolicyVersion:
        if not re.fullmatch(r"[0-9a-f]{64}", prompt_sha256):
            raise ValueError("P2b policy prompt hash is invalid")
        return self._store(
            version,
            raw_response=raw_response,
            source="optimizer",
            prompt_sha256=prompt_sha256,
        )

    def load(self, version_id: str) -> P2bPolicyVersion:
        _validate_version(version_id)
        metadata_path = self.scope_root / "policy_metadata" / f"{version_id}.json"
        policy_path = self.scope_root / "policies" / f"{version_id}.json"
        if not metadata_path.is_file() or not policy_path.is_file():
            raise ValueError(f"P2b policy version is not archived: {version_id}")
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        data = json.loads(policy_path.read_text(encoding="utf-8"))
        version = P2bPolicyVersion.create(
            version_id=version_id,
            parent_version_id=metadata.get("parent_version_id"),
            policy=_policy_from_dict(data),
        )
        if version.sha256 != metadata.get("policy_sha256"):
            raise ValueError("archived P2b policy content changed")
        return version

    def _store(
        self,
        version: P2bPolicyVersion,
        *,
        raw_response: str,
        source: str,
        prompt_sha256: str | None,
    ) -> P2bPolicyVersion:
        policy_path = self.scope_root / "policies" / f"{version.version_id}.json"
        raw_path = self.scope_root / "raw_policy_responses" / f"{version.version_id}.txt"
        metadata_path = (
            self.scope_root / "policy_metadata" / f"{version.version_id}.json"
        )
        if metadata_path.exists():
            existing = self.load(version.version_id)
            if existing != version:
                raise ValueError("P2b policy id is bound to different content")
            return existing
        _write_atomic(
            policy_path,
            json.dumps(version.policy.to_dict(), ensure_ascii=False, indent=2, sort_keys=True)
            + "\n",
        )
        _write_atomic(raw_path, raw_response.strip() + "\n")
        _write_atomic(
            metadata_path,
            json.dumps(
                {
                    "schema_version": 1,
                    "version_id": version.version_id,
                    "parent_version_id": version.parent_version_id,
                    "policy_sha256": version.sha256,
                    "source": source,
                    "prompt_sha256": prompt_sha256,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            + "\n",
        )
        return version


def initial_policy(*, strategy: str, starting_candidate_id: str) -> P2bPolicyVersion:
    if strategy not in P2B_MODES:
        raise InvalidP2bPolicy("unknown initial P2b strategy")
    templates = {
        "profile_exploit": (
            "full",
            ("register_pressure", "memory_layout", "compiler_schedule"),
            (
                "task_semantics",
                "score_trend",
                "timeline_analysis",
                "compiler_resource_analysis",
                "memory_access_analysis",
                "novelty_check",
            ),
            (
                "score",
                "static_structure",
                "nsys_timeline",
                "triton_compiler_metadata",
                "ptx_sass_summary",
            ),
            "Use measured timeline and compiler evidence to improve a frozen strong solution.",
        ),
        "architecture_reset": (
            "full",
            ("kernel_count", "fusion_boundary", "reduction_structure", "thread_mapping"),
            (
                "task_semantics",
                "score_trend",
                "architecture_rebuild",
                "numerical_correctness",
                "novelty_check",
            ),
            ("score", "static_structure", "nsys_timeline"),
            "Discard inherited Kernel structure and derive a new implementation from task semantics.",
        ),
        "counterfactual": (
            "light",
            ("math_formulation", "memory_layout", "thread_mapping"),
            (
                "task_semantics",
                "score_trend",
                "counterfactual_generation",
                "code_diff",
                "novelty_check",
            ),
            ("score", "static_structure"),
            "Test a structure that contradicts the strongest inherited bottleneck assumption.",
        ),
        "recombinant_frontier": (
            "full",
            ("recombination", "fusion_boundary", "tiling", "numerical_method"),
            (
                "task_semantics",
                "score_trend",
                "frontier_recombination",
                "code_diff",
                "compiler_resource_analysis",
                "novelty_check",
            ),
            (
                "score",
                "static_structure",
                "nsys_timeline",
                "triton_compiler_metadata",
            ),
            "Compare frozen frontier candidates and recombine only complementary structures.",
        ),
    }
    diagnostic, scopes, skills, tools, instruction = templates[strategy]
    policy = P2bPolicy(
        mode=strategy,
        base_candidate_id=starting_candidate_id,
        diagnostic_level=diagnostic,
        observed_evidence=("No P2b candidate has been evaluated in this lane yet.",),
        primary_hypothesis="The initial hypothesis is unconfirmed until a correct candidate is scored.",
        score_assessment="Use the frozen starting score as the baseline for the first candidate.",
        direction_change_reason="Begin the lane with its preregistered, distinct search responsibility.",
        mutation_scope=scopes,
        enabled_skills=skills,
        tool_plan=tools,
        memory_views=(
            "starting_point",
            "historical_best",
            "structurally_novel",
            "disproved_ideas",
        ),
        workflow_steps=(
            "Read the current score trend before choosing any change.",
            "Use the enabled evidence tools and separate observations from hypotheses.",
            "Select the code base and a structurally meaningful mutation scope.",
            "Generate exactly one complete candidate, then pass correctness and score gates.",
        ),
        avoid_repeats=("Do not spend the round only changing num_warps or num_stages.",),
        kernel_instructions=(
            instruction,
            "Make a meaningful structural choice before tuning launch parameters.",
            "Preserve correctness for every frozen input shape and dtype.",
        ),
        force_restart=False,
        structural_change=True,
    )
    return P2bPolicyVersion.create(
        version_id="v001", parent_version_id=None, policy=policy
    )


def _validate_version(version_id: str) -> None:
    if not re.fullmatch(r"v\d{3}", version_id):
        raise InvalidP2bPolicy("P2b policy version must use vNNN")


def _string_tuple(value: object) -> tuple[str, ...]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise InvalidP2bPolicy("P2b policy list fields must contain strings")
    return tuple(value)


def _strict_bool(value: object) -> bool:
    if not isinstance(value, bool):
        raise InvalidP2bPolicy("P2b policy boolean fields must be booleans")
    return value


def _contains_absolute_path(text: str) -> bool:
    return bool(re.search(r"(?<![A-Za-z0-9])/(?:[^\s:|]+/)+[^\s:|]+", text))


def _load_response_object(response: str) -> Any:
    stripped = response.strip()
    match = re.fullmatch(r"```(?:json)?\s*\n(.*?)\n```", stripped, re.DOTALL)
    if match:
        stripped = match.group(1).strip()
    try:
        return json.loads(stripped)
    except json.JSONDecodeError as exc:
        raise InvalidP2bPolicy("P2b policy response must be one JSON object") from exc


def _validate_text(value: str, label: str, *, maximum: int) -> None:
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise InvalidP2bPolicy(f"policy {label} is empty or too long")
    if "\x00" in value:
        raise InvalidP2bPolicy(f"policy {label} contains a NUL byte")
    if _contains_absolute_path(value):
        raise InvalidP2bPolicy("P2b policy must not contain an absolute path")


def _policy_from_dict(data: dict[str, Any]) -> P2bPolicy:
    if not isinstance(data, dict) or set(data) != _FIELDS:
        raise InvalidP2bPolicy("archived P2b policy fields do not match the schema")
    return P2bPolicy(
        mode=str(data["mode"]),
        base_candidate_id=str(data["base_candidate_id"]),
        diagnostic_level=str(data["diagnostic_level"]),
        observed_evidence=_string_tuple(data["observed_evidence"]),
        primary_hypothesis=str(data["primary_hypothesis"]),
        score_assessment=str(data["score_assessment"]),
        direction_change_reason=str(data["direction_change_reason"]),
        mutation_scope=_string_tuple(data["mutation_scope"]),
        enabled_skills=_string_tuple(data["enabled_skills"]),
        tool_plan=_string_tuple(data["tool_plan"]),
        memory_views=_string_tuple(data["memory_views"]),
        workflow_steps=_string_tuple(data["workflow_steps"]),
        avoid_repeats=_string_tuple(data["avoid_repeats"]),
        kernel_instructions=_string_tuple(data["kernel_instructions"]),
        force_restart=_strict_bool(data["force_restart"]),
        structural_change=_strict_bool(data["structural_change"]),
    )


def _write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise
