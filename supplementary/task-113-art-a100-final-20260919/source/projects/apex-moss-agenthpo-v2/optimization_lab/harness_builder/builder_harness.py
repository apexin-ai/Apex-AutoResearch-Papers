from __future__ import annotations

import json
import hashlib
import re
from dataclasses import dataclass
from typing import Any, Callable, Mapping

from optimization_lab.generation import CandidateGenerator

from .champion_archive import (
    ChampionArchivePolicy,
    GateDecision,
    MutationDirective,
    PortfolioEvolutionPolicy,
    sorted_gate_candidates,
    validate_mutation,
)
from .dual_harness import HarnessWorkspace, TaskHarnessArtifact, TaskHarnessSpec


_SHA256 = re.compile(r"[0-9a-f]{64}")
_COMPONENT_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_PORTFOLIO_RUN_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,109}")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate Builder proposal key: {key}")
        result[key] = value
    return result


@dataclass(frozen=True)
class BuilderHarnessSpec:
    schema_version: int
    steps: tuple[str, ...]
    tool_protocol: str

    @classmethod
    def default(cls) -> "BuilderHarnessSpec":
        return cls(
            schema_version=1,
            steps=("inspect", "propose", "validate", "probe", "commit_or_rollback"),
            tool_protocol="controller_json",
        )

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported Builder Harness schema")
        if self.steps != (
            "inspect",
            "propose",
            "validate",
            "probe",
            "commit_or_rollback",
        ):
            raise ValueError("unsupported Builder Harness step graph")
        if self.tool_protocol != "controller_json":
            raise ValueError("unsupported Builder Harness tool protocol")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "steps": list(self.steps),
            "tool_protocol": self.tool_protocol,
        }

    @property
    def sha256(self) -> str:
        encoded = json.dumps(self.to_dict(), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class BuilderStepEvent:
    step: str
    output: Any


@dataclass(frozen=True)
class HarnessChangeProposal:
    schema_version: int
    base_sha256: str
    source_sha256: str
    changed_components: tuple[str, ...]
    reason: str
    expected_effect: str
    spec: TaskHarnessSpec

    @classmethod
    def from_response(cls, raw_response: str) -> "HarnessChangeProposal":
        if not isinstance(raw_response, str) or not raw_response.strip():
            raise ValueError("Builder proposal cannot be empty")
        if len(raw_response) > 128_000:
            raise ValueError("Builder proposal is too large")
        try:
            payload = json.loads(raw_response, object_pairs_hook=_unique_object)
        except json.JSONDecodeError as exc:
            raise ValueError("Builder proposal is not strict JSON") from exc
        if not isinstance(payload, dict):
            raise ValueError("Builder proposal must be one JSON object")
        required_v1 = {
            "schema_version",
            "base_sha256",
            "reason",
            "expected_effect",
            "artifact",
        }
        required_v2 = required_v1 | {"source_sha256"}
        optional_v2 = required_v2 | {"changed_components"}
        if set(payload) not in (required_v1, required_v2, optional_v2):
            raise ValueError("Builder proposal keys differ from the contract")
        schema_version = payload["schema_version"]
        if schema_version not in {1, 2}:
            raise ValueError("unsupported Builder proposal schema")
        base = payload["base_sha256"]
        if not isinstance(base, str) or _SHA256.fullmatch(base) is None:
            raise ValueError("Builder proposal base hash is invalid")
        source = payload.get("source_sha256", base)
        if not isinstance(source, str) or _SHA256.fullmatch(source) is None:
            raise ValueError("Builder proposal source hash is invalid")
        if schema_version == 1 and set(payload) != required_v1:
            raise ValueError("schema 1 Builder proposal cannot include source_sha256")
        if schema_version == 2 and set(payload) != required_v2:
            if set(payload) != optional_v2:
                raise ValueError("schema 2 Builder proposal requires source_sha256")
        raw_components = payload.get("changed_components", ["execution"])
        if not isinstance(raw_components, list) or not raw_components or not all(
            isinstance(item, str) and _COMPONENT_ID.fullmatch(item) for item in raw_components
        ):
            raise ValueError("Builder proposal changed_components is invalid")
        reason = payload["reason"]
        expected = payload["expected_effect"]
        if not isinstance(reason, str) or not reason.strip() or len(reason) > 4_000:
            raise ValueError("Builder proposal reason is invalid")
        if not isinstance(expected, str) or not expected.strip() or len(expected) > 4_000:
            raise ValueError("Builder proposal expected effect is invalid")
        return cls(
            schema_version=schema_version,
            base_sha256=base,
            source_sha256=source,
            changed_components=tuple(raw_components),
            reason=reason,
            expected_effect=expected,
            spec=TaskHarnessSpec.from_dict(payload["artifact"]),
        )


@dataclass(frozen=True)
class BuilderEvolutionResult:
    status: str
    previous_sha256: str
    candidate_sha256: str | None
    reason: str
    builder_harness_sha256: str
    events: tuple[BuilderStepEvent, ...]
    source_sha256: str | None = None
    changed_components: tuple[str, ...] = ()


@dataclass(frozen=True)
class PortfolioCandidateEvolution:
    proposal_id: str
    directive: MutationDirective
    status: str
    candidate_sha256: str | None
    reason: str
    gate: GateDecision | None


@dataclass(frozen=True)
class PortfolioEvolutionResult:
    previous_champion_sha256: str
    next_champion_sha256: str
    promoted_proposal_id: str | None
    policy_sha256: str
    candidates: tuple[PortfolioCandidateEvolution, ...]


class BuilderHarness:
    """Fixed inspect/propose/validate/probe/commit Harness for Task Harness edits."""

    def __init__(
        self,
        *,
        workspace: HarnessWorkspace,
        generator: CandidateGenerator,
        model: str,
        spec: BuilderHarnessSpec | None = None,
        inspection_transform: (
            Callable[[Mapping[str, Any]], Mapping[str, Any]] | None
        ) = None,
    ) -> None:
        if not model.strip():
            raise ValueError("Builder Harness model is required")
        if inspection_transform is not None and not callable(inspection_transform):
            raise TypeError("Builder inspection transform must be callable")
        self.workspace = workspace
        self.generator = generator
        self.model = model
        self.spec = spec or BuilderHarnessSpec.default()
        self.inspection_transform = inspection_transform
        self.workspace.store_builder_harness(
            sha256=self.spec.sha256,
            payload=self.spec.to_dict(),
        )

    def inspect(self) -> Mapping[str, Any]:
        inspection = self.workspace.inspect()
        if self.inspection_transform is None:
            return inspection
        transformed = self.inspection_transform(inspection)
        if not isinstance(transformed, Mapping):
            raise TypeError("Builder inspection transform must return a Mapping")
        return transformed

    def propose(self, *, score: float | None, feedback: str) -> HarnessChangeProposal:
        inspection = self.inspect()
        return self._propose_from_inspection(
            inspection=inspection,
            score=score,
            feedback=feedback,
        )

    def _propose_from_inspection(
        self,
        *,
        inspection: Mapping[str, Any],
        score: float | None,
        feedback: str,
    ) -> HarnessChangeProposal:
        prompt = self._proposal_prompt(
            inspection=inspection,
            score=score,
            feedback=feedback,
        )
        result = self.generator.generate(prompt, model=self.model)
        return HarnessChangeProposal.from_response(result.raw_response)

    def evolve_once(
        self,
        *,
        score: float | None,
        feedback: str,
        probe: Callable[[TaskHarnessArtifact], bool] | None = None,
        run_id: str | None = None,
        update_champion: bool = True,
    ) -> BuilderEvolutionResult:
        current = self.workspace.current()
        events: list[BuilderStepEvent] = []
        inspection = self.inspect()
        events.append(
            BuilderStepEvent(
                step="inspect",
                output={
                    "current_sha256": inspection["current_sha256"],
                    "run_count": len(inspection["runs"]),
                },
            )
        )
        try:
            proposal = self._propose_from_inspection(
                inspection=inspection,
                score=score,
                feedback=feedback,
            )
        except Exception as exc:
            events.extend(
                (
                    BuilderStepEvent(
                        step="propose",
                        output={"accepted": False, "error": self._error_code(exc)},
                    ),
                    BuilderStepEvent(step="validate", output=False),
                    BuilderStepEvent(step="probe", output="skipped"),
                    BuilderStepEvent(step="commit_or_rollback", output="rollback"),
                )
            )
            return BuilderEvolutionResult(
                status="rejected",
                previous_sha256=current.sha256,
                candidate_sha256=None,
                reason=f"Builder proposal failed: {self._error_code(exc)}",
                builder_harness_sha256=self.spec.sha256,
                events=tuple(events),
            )
        events.append(
            BuilderStepEvent(
                step="propose",
                output={
                    "base_sha256": proposal.base_sha256,
                    "source_sha256": proposal.source_sha256,
                    "changed_components": list(proposal.changed_components),
                    "reason": proposal.reason,
                    "expected_effect": proposal.expected_effect,
                },
            )
        )
        available_source_hashes = {
            item["sha256"] for item in inspection.get("available_harnesses", ())
        }
        if proposal.source_sha256 not in available_source_hashes:
            events.extend(
                (
                    BuilderStepEvent(step="validate", output=False),
                    BuilderStepEvent(step="probe", output="skipped"),
                    BuilderStepEvent(step="commit_or_rollback", output="rollback"),
                )
            )
            return BuilderEvolutionResult(
                status="rejected",
                previous_sha256=current.sha256,
                candidate_sha256=None,
                reason="proposal source is not available in this experiment line",
                builder_harness_sha256=self.spec.sha256,
                events=tuple(events),
            )
        try:
            source = self.workspace.load_artifact(proposal.source_sha256)
        except (FileNotFoundError, ValueError):
            source = None
        if source is None or not self.workspace.same_lineage(source.sha256, current.sha256):
            events.extend(
                (
                    BuilderStepEvent(step="validate", output=False),
                    BuilderStepEvent(step="probe", output="skipped"),
                    BuilderStepEvent(step="commit_or_rollback", output="rollback"),
                )
            )
            return BuilderEvolutionResult(
                status="rejected",
                previous_sha256=current.sha256,
                candidate_sha256=None,
                reason="proposal source is not in the current Harness lineage",
                builder_harness_sha256=self.spec.sha256,
                events=tuple(events),
            )
        if proposal.base_sha256 != source.sha256:
            events.extend(
                (
                    BuilderStepEvent(step="validate", output=False),
                    BuilderStepEvent(step="probe", output="skipped"),
                    BuilderStepEvent(step="commit_or_rollback", output="rollback"),
                )
            )
            return BuilderEvolutionResult(
                status="rejected",
                previous_sha256=current.sha256,
                candidate_sha256=None,
                reason="proposal base must equal its selected source Harness",
                builder_harness_sha256=self.spec.sha256,
                events=tuple(events),
                source_sha256=source.sha256,
                changed_components=proposal.changed_components,
            )
        candidate_spec = proposal.spec
        if source.spec.schema_version == 2 and candidate_spec.schema_version == 1:
            # Preserve untouched v2 state when a legacy-shaped response only
            # returns nodes; the Builder must never erase memory or skills.
            candidate_spec = TaskHarnessSpec(
                schema_version=2,
                nodes=candidate_spec.nodes,
                interface=source.spec.interface,
                memory=source.spec.memory,
                capabilities=source.spec.capabilities,
                router=source.spec.router,
            )
        candidate = TaskHarnessArtifact(
            schema_version=1,
            version=source.version + 1,
            parent_sha256=source.sha256,
            spec=candidate_spec,
        )
        if candidate.spec.to_dict() == source.spec.to_dict():
            events.extend(
                (
                    BuilderStepEvent(step="validate", output=False),
                    BuilderStepEvent(step="probe", output="skipped"),
                    BuilderStepEvent(step="commit_or_rollback", output="rollback"),
                )
            )
            return BuilderEvolutionResult(
                status="rejected",
                previous_sha256=current.sha256,
                candidate_sha256=None,
                reason="proposal contains no executable change",
                builder_harness_sha256=self.spec.sha256,
                events=tuple(events),
                source_sha256=source.sha256,
                changed_components=proposal.changed_components,
            )
        candidate = self.workspace.store_artifact(candidate)
        events.append(BuilderStepEvent(step="validate", output=True))
        try:
            probe_passed = True if probe is None else probe(candidate)
            if type(probe_passed) is not bool:
                raise TypeError("public probe must return bool")
            probe_output: Any = probe_passed
        except Exception as exc:
            probe_passed = False
            probe_output = {"passed": False, "error": self._error_code(exc)}
        events.append(BuilderStepEvent(step="probe", output=probe_output))
        if not probe_passed:
            events.append(BuilderStepEvent(step="commit_or_rollback", output="rollback"))
            return BuilderEvolutionResult(
                status="rolled_back",
                previous_sha256=current.sha256,
                candidate_sha256=candidate.sha256,
                reason="candidate failed the public probe",
                builder_harness_sha256=self.spec.sha256,
                events=tuple(events),
                source_sha256=source.sha256,
                changed_components=proposal.changed_components,
            )
        self.workspace.commit(
            candidate,
            owner_run_id=run_id,
            update_champion=update_champion,
            allow_branch=source.sha256 != current.sha256,
        )
        events.append(BuilderStepEvent(step="commit_or_rollback", output="commit"))
        return BuilderEvolutionResult(
            status="committed",
            previous_sha256=current.sha256,
            candidate_sha256=candidate.sha256,
            reason=proposal.reason,
            builder_harness_sha256=self.spec.sha256,
            events=tuple(events),
            source_sha256=source.sha256,
            changed_components=proposal.changed_components,
        )

    def evolve_portfolio(
        self,
        *,
        run_id: str,
        score: float | None,
        feedback: str,
        candidate_count: int,
        evaluator_contract_sha256: str,
        gate_evaluator: Callable[
            [TaskHarnessArtifact, TaskHarnessArtifact], GateDecision
        ],
        attempt_start: int | None = None,
        policy: PortfolioEvolutionPolicy | None = None,
        proposal_attempt_limit: int | None = None,
    ) -> PortfolioEvolutionResult:
        """Generate sibling/branch challengers and promote only a Gate winner.

        Every valid proposal is archived before the external Gate runs.  The
        incumbent pointer remains unchanged until all candidates have durable,
        typed public Gate decisions and the best credible challenger is chosen.
        Formal callers must still wrap model/Gate callbacks in their operation
        journal; this method does not grant calls or evaluator entitlement.
        """

        if (
            not isinstance(run_id, str)
            or _PORTFOLIO_RUN_ID.fullmatch(run_id) is None
            or ".." in run_id
        ):
            raise ValueError("portfolio run id is invalid")
        if (
            not isinstance(candidate_count, int)
            or isinstance(candidate_count, bool)
            or not 1 <= candidate_count <= 16
        ):
            raise ValueError("portfolio candidate count must be between one and 16")
        if not callable(gate_evaluator):
            raise TypeError("portfolio Gate evaluator must be callable")
        if proposal_attempt_limit is None:
            proposal_attempt_limit = candidate_count
        if (
            not isinstance(proposal_attempt_limit, int)
            or isinstance(proposal_attempt_limit, bool)
            or not candidate_count <= proposal_attempt_limit <= 32
        ):
            raise ValueError(
                "portfolio proposal attempt limit must cover candidate count and be at most 32"
            )
        selected_policy = policy or PortfolioEvolutionPolicy()
        controller = ChampionArchivePolicy(
            workspace=self.workspace,
            evaluator_contract_sha256=evaluator_contract_sha256,
            policy=selected_policy,
        )
        expected_attempt_start = controller.next_attempt_index()
        if attempt_start is None:
            attempt_start = expected_attempt_start
        if (
            not isinstance(attempt_start, int)
            or isinstance(attempt_start, bool)
            or attempt_start != expected_attempt_start
        ):
            raise ValueError("portfolio attempt start does not continue Gate history")
        incumbent = self.workspace.champion()
        outcomes: list[PortfolioCandidateEvolution] = []
        gated: list[tuple[str, GateDecision]] = []
        archived_count = 0
        for offset in range(proposal_attempt_limit):
            if archived_count >= candidate_count:
                break
            attempt_index = attempt_start + offset
            proposal_id = f"{run_id}-candidate-{offset + 1:03d}"
            directive = controller.next_directive(attempt_index=attempt_index)
            parent = self.workspace.load_artifact(directive.parent_sha256)
            inspection = self.inspect()
            try:
                proposal = self._propose_portfolio_candidate(
                    inspection=inspection,
                    parent=parent,
                    directive=directive,
                    score=score,
                    feedback=feedback,
                )
                if proposal.base_sha256 != parent.sha256:
                    raise ValueError("proposal base does not match its selected parent")
                candidate = TaskHarnessArtifact(
                    schema_version=1,
                    version=parent.version + 1,
                    parent_sha256=parent.sha256,
                    spec=proposal.spec,
                )
                distance = validate_mutation(
                    parent=parent,
                    candidate=candidate,
                    directive=directive,
                )
                candidate = self.workspace.store_artifact(candidate)
                if any(
                    record["candidate_sha256"] == candidate.sha256
                    for record in self.workspace.archived_candidates()
                ):
                    raise ValueError("proposal duplicates an archived Harness")
                self.workspace.record_archived_candidate(
                    proposal_id=proposal_id,
                    payload={
                        "candidate_sha256": candidate.sha256,
                        "parent_sha256": parent.sha256,
                        "attempt_index": attempt_index,
                        "scheduled_source": directive.scheduled_source,
                        "source": directive.source,
                        "mutation_family": directive.mutation_family,
                        "mutation_distance": distance,
                        "forced_restart": directive.forced_restart,
                        "fallback_reason": directive.fallback_reason,
                        "target_failure_class": directive.target_failure_class,
                        "reason": proposal.reason,
                        "expected_effect": proposal.expected_effect,
                        "builder_harness_sha256": self.spec.sha256,
                        "portfolio_policy_sha256": selected_policy.sha256,
                    },
                )
                archived_count += 1
            except Exception as exc:
                outcomes.append(
                    PortfolioCandidateEvolution(
                        proposal_id=proposal_id,
                        directive=directive,
                        status="proposal_rejected",
                        candidate_sha256=None,
                        reason=f"portfolio proposal failed: {self._error_code(exc)}",
                        gate=None,
                    )
                )
                continue
            try:
                gate = gate_evaluator(incumbent, candidate)
                if not isinstance(gate, GateDecision):
                    raise TypeError("portfolio Gate must return GateDecision")
                if gate.evaluator_contract_sha256 != evaluator_contract_sha256:
                    raise ValueError("portfolio Gate evaluator contract differs")
                if gate.incumbent_sha256 != incumbent.sha256:
                    raise ValueError("portfolio Gate incumbent differs")
                if gate.candidate_sha256 != candidate.sha256:
                    raise ValueError("portfolio Gate candidate differs")
                self.workspace.record_gate_decision(
                    proposal_id=proposal_id,
                    payload=gate.to_dict(),
                )
            except Exception as exc:
                outcomes.append(
                    PortfolioCandidateEvolution(
                        proposal_id=proposal_id,
                        directive=directive,
                        status="gate_failed_closed",
                        candidate_sha256=candidate.sha256,
                        reason=f"external Gate failed: {self._error_code(exc)}",
                        gate=None,
                    )
                )
                continue
            gated.append((proposal_id, gate))
            outcomes.append(
                PortfolioCandidateEvolution(
                    proposal_id=proposal_id,
                    directive=directive,
                    status=(
                        "promotion_eligible"
                        if gate.passed and gate.credible_improvement
                        else "archived"
                    ),
                    candidate_sha256=candidate.sha256,
                    reason=gate.reason,
                    gate=gate,
                )
            )
        ranked = sorted_gate_candidates(gated)
        promoted_proposal_id: str | None = None
        if ranked:
            promoted_proposal_id = ranked[0][0]
            self.workspace.promote_archived_candidate(
                proposal_id=promoted_proposal_id,
                owner_run_id=run_id,
            )
        return PortfolioEvolutionResult(
            previous_champion_sha256=incumbent.sha256,
            next_champion_sha256=self.workspace.champion().sha256,
            promoted_proposal_id=promoted_proposal_id,
            policy_sha256=selected_policy.sha256,
            candidates=tuple(outcomes),
        )

    def _propose_portfolio_candidate(
        self,
        *,
        inspection: Mapping[str, Any],
        parent: TaskHarnessArtifact,
        directive: MutationDirective,
        score: float | None,
        feedback: str,
    ) -> HarnessChangeProposal:
        payload = {
            "champion_and_public_runs": inspection,
            "selected_parent": parent.to_dict(),
            "mutation_directive": directive.to_dict(),
            "latest_public_score": score,
            "latest_public_feedback": feedback,
        }
        prompt = (
            "You are the Builder inside a fixed portfolio Builder Harness. Propose "
            "one small, targeted Task Harness mutation from selected_parent. Bind "
            "base_sha256 to mutation_directive.parent_sha256, use exactly the "
            "specified mutation_family, and address only the public failure class. "
            "Do not include benchmark-private data or an answer. Return exactly one "
            "JSON object with keys schema_version, source_sha256, base_sha256, changed_components, reason, "
            "expected_effect, and artifact. artifact must contain only "
            "schema_version and nodes; for schema_version 2 also preserve interface, "
            "memory, capabilities, and router. The controller will reject a mutation larger "
            "than max_changed_nodes.\n\n"
            + json.dumps(payload, ensure_ascii=False, sort_keys=True)
        )
        result = self.generator.generate(prompt, model=self.model)
        return HarnessChangeProposal.from_response(result.raw_response)

    @staticmethod
    def _error_code(exc: Exception) -> str:
        error_type = type(exc).__name__
        detail = " ".join(str(exc).split())
        if not detail:
            return error_type
        detail = re.sub(
            r"(?i)(Authorization\s*:\s*Bearer)\s+\S+",
            r"\1 <redacted>",
            detail,
        )
        detail = re.sub(
            r"(?i)\b(api[_-]?key)\s*=\s*\S+",
            r"\1=<redacted>",
            detail,
        )
        detail = re.sub(r"(?i)\bsk-[A-Za-z0-9_-]{8,}\b", "<redacted>", detail)
        if len(detail) > 512:
            detail = detail[:509] + "..."
        return f"{error_type}: {detail}"

    @staticmethod
    def _proposal_prompt(
        *,
        inspection: Mapping[str, Any],
        score: float | None,
        feedback: str,
    ) -> str:
        current_sha256 = inspection.get("current_sha256")
        if (
            not isinstance(current_sha256, str)
            or _SHA256.fullmatch(current_sha256) is None
        ):
            raise ValueError("Builder inspection current hash is invalid")
        raw_available = inspection.get("available_harnesses")
        if not isinstance(raw_available, (list, tuple)):
            raise ValueError("Builder inspection available Harnesses are invalid")
        allowed_source_sha256: list[str] = []
        for item in raw_available:
            if not isinstance(item, Mapping):
                raise ValueError("Builder inspection available Harness is invalid")
            sha256 = item.get("sha256")
            if not isinstance(sha256, str) or _SHA256.fullmatch(sha256) is None:
                raise ValueError("Builder inspection available Harness hash is invalid")
            if sha256 not in allowed_source_sha256:
                allowed_source_sha256.append(sha256)
        if current_sha256 not in allowed_source_sha256:
            raise ValueError("current Harness is absent from available Harnesses")
        allowed_sources_json = json.dumps(
            allowed_source_sha256,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        payload = {
            "current_harness_and_public_runs": inspection,
            "latest_public_score": score,
            "latest_public_feedback": feedback,
        }
        return (
            "You are the Builder inside a fixed Builder Harness. Inspect the current "
            "Task Harness and public run traces, then propose one complete replacement "
            "Task Harness spec. Do not include benchmark-private data or an answer. "
            "Choose one exact source_sha256 from this allowed list: "
            f"{allowed_sources_json}. Prefer the current Harness "
            f'"{current_sha256}" unless public evidence supports branching from a '
            "historical Harness. Copy the chosen exact hash into both source_sha256 "
            "and base_sha256. Never return null, a placeholder, a shortened hash, or "
            "a hash outside the allowed list. Use proposal schema_version 2. "
            "Return exactly one JSON object with keys schema_version, source_sha256, base_sha256, "
            "changed_components, reason, expected_effect, and artifact. For a v2 source, artifact must contain "
            "schema_version, nodes, interface, memory, capabilities, and router. "
            "Return raw JSON only: no Markdown fence, prose, comments, or trailing text. "
            "A node may contain only id, kind, role, prompt, tool, skill, and input_key. "
            "Do not use output_key; every node output is already stored under its id, "
            "and model output is also stored as latest_output. Keep exactly one emit node "
            "last, and make its input_key name an existing node output or latest_output. "
            "After choosing source_sha256, locate the matching entry in available_harnesses. "
            "Use only that selected available_harnesses item's spec as the mutation basis. "
            "Do not use current_artifact.spec when a historical source is selected. Preserve "
            "every required v2 object and make at least one real executable change.\n\n"
            + json.dumps(payload, ensure_ascii=False, sort_keys=True)
        )
