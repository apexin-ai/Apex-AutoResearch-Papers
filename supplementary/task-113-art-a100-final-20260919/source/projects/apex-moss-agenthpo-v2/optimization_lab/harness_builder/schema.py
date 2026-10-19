from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


_SHA256 = re.compile(r"[0-9a-f]{64}")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_PRIVATE_DIRECTIVE = re.compile(
    r"(?:/home/|/data\d*/|private[_ -](?:evaluator|log)|secret[_ -]?(?:key|token))",
    re.IGNORECASE,
)


def _read_json(path: Path) -> Any:
    value = json.loads(path.read_text(encoding="utf-8"))
    return value


def _require_keys(payload: dict[str, Any], expected: set[str], label: str) -> None:
    actual = set(payload)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ValueError(f"{label} keys differ: missing={missing}, extra={extra}")


def _safe_id(value: str, label: str) -> str:
    if not isinstance(value, str) or not _SAFE_ID.fullmatch(value):
        raise ValueError(f"unsafe {label}")
    return value


def _sha(value: str, label: str) -> str:
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise ValueError(f"invalid {label}")
    return value


@dataclass(frozen=True)
class CandidateInstance:
    task_id: str
    category: str
    source_path: str
    source_sha256: str
    selection_digest: str
    eligible: bool

    @classmethod
    def from_dict(
        cls, payload: dict[str, Any], *, suite: str, selection_seed: str
    ) -> "CandidateInstance":
        _require_keys(
            payload,
            {
                "task_id",
                "category",
                "source_path",
                "source_sha256",
                "selection_digest",
                "eligible",
            },
            "candidate instance",
        )
        item = cls(
            task_id=_safe_id(payload["task_id"], "task id"),
            category=_safe_id(payload["category"], "category"),
            source_path=payload["source_path"],
            source_sha256=_sha(payload["source_sha256"], "source sha256"),
            selection_digest=_sha(payload["selection_digest"], "selection digest"),
            eligible=payload["eligible"],
        )
        if not isinstance(item.source_path, str) or item.source_path.startswith("/"):
            raise ValueError("candidate source path must be relative or a benchmark URI")
        if not isinstance(item.eligible, bool):
            raise ValueError("candidate eligibility must be boolean")
        expected = hashlib.sha256(
            f"{selection_seed}|{suite}|{item.task_id}".encode("utf-8")
        ).hexdigest()
        if item.selection_digest != expected:
            raise ValueError("candidate selection digest does not match frozen seed")
        return item


@dataclass(frozen=True)
class BenchmarkPool:
    suite: str
    repository: str
    repository_commit: str
    dataset_commit: str
    evaluator: str
    candidates: tuple[CandidateInstance, ...]
    selected_heldout: tuple[str, ...]

    @classmethod
    def from_dict(
        cls, payload: dict[str, Any], *, selection_seed: str
    ) -> "BenchmarkPool":
        _require_keys(
            payload,
            {
                "suite",
                "repository",
                "repository_commit",
                "dataset_commit",
                "evaluator",
                "candidates",
                "selected_heldout",
            },
            "benchmark pool",
        )
        suite = _safe_id(payload["suite"], "suite")
        commit = payload["repository_commit"]
        if not isinstance(commit, str) or not _COMMIT.fullmatch(commit):
            raise ValueError("repository commit must be pinned")
        dataset_commit = payload["dataset_commit"]
        if not isinstance(dataset_commit, str) or not _COMMIT.fullmatch(dataset_commit):
            raise ValueError("dataset commit must be pinned")
        candidates = tuple(
            CandidateInstance.from_dict(
                item, suite=suite, selection_seed=selection_seed
            )
            for item in payload["candidates"]
        )
        selected = tuple(payload["selected_heldout"])
        item = cls(
            suite=suite,
            repository=payload["repository"],
            repository_commit=commit,
            dataset_commit=dataset_commit,
            evaluator=_safe_id(payload["evaluator"], "evaluator"),
            candidates=candidates,
            selected_heldout=selected,
        )
        if not item.repository.startswith("https://github.com/"):
            raise ValueError("benchmark repository must be a GitHub HTTPS URL")
        if len(candidates) != len({candidate.task_id for candidate in candidates}):
            raise ValueError("candidate task ids must be unique within a suite")
        expected = tuple(candidate.task_id for candidate in candidates if candidate.eligible)
        if selected != expected:
            raise ValueError("held-out selection must contain every frozen eligible instance")
        return item


@dataclass(frozen=True)
class PilotManifest:
    schema_version: int
    phase_id: str
    selection_seed: str
    rounds: int
    executor_model: str
    reasoning_effort: str
    model_transport: str
    client_version: str
    model_call_cap: int
    evaluator_transaction_cap: int
    gpu_exclusive_seconds_cap: float
    cpu_evaluator_seconds_cap: float
    benchmarks: tuple[BenchmarkPool, ...]

    @classmethod
    def from_json(cls, path: Path) -> "PilotManifest":
        payload = _read_json(path)
        if not isinstance(payload, dict):
            raise ValueError("pilot manifest must be an object")
        _require_keys(
            payload,
            {
                "schema_version",
                "phase_id",
                "selection_seed",
                "rounds",
                "executor_model",
                "reasoning_effort",
                "model_transport",
                "client_version",
                "model_call_cap",
                "evaluator_transaction_cap",
                "gpu_exclusive_seconds_cap",
                "cpu_evaluator_seconds_cap",
                "benchmarks",
            },
            "pilot manifest",
        )
        item = cls(
            schema_version=payload["schema_version"],
            phase_id=_safe_id(payload["phase_id"], "phase id"),
            selection_seed=_safe_id(payload["selection_seed"], "selection seed"),
            rounds=payload["rounds"],
            executor_model=_safe_id(payload["executor_model"], "executor model"),
            reasoning_effort=_safe_id(
                payload["reasoning_effort"], "reasoning effort"
            ),
            model_transport=_safe_id(payload["model_transport"], "model transport"),
            client_version=_safe_id(payload["client_version"], "client version"),
            model_call_cap=payload["model_call_cap"],
            evaluator_transaction_cap=payload["evaluator_transaction_cap"],
            gpu_exclusive_seconds_cap=payload["gpu_exclusive_seconds_cap"],
            cpu_evaluator_seconds_cap=payload["cpu_evaluator_seconds_cap"],
            benchmarks=(),
        )
        object.__setattr__(
            item,
            "benchmarks",
            tuple(
                BenchmarkPool.from_dict(
                    benchmark, selection_seed=item.selection_seed
                )
                for benchmark in payload["benchmarks"]
            ),
        )
        if item.schema_version != 1 or item.rounds != 8:
            raise ValueError("HB-GEN-1 requires schema v1 and eight rounds")
        if (
            item.executor_model != "gpt-5.6-sol"
            or item.reasoning_effort != "high"
            or item.model_transport != "codex-exec-chatgpt-login"
            or item.client_version != "codex-cli-0.144.6"
        ):
            raise ValueError("HB-GEN-1 model route or reasoning configuration changed")
        if item.model_call_cap != 1700 or item.evaluator_transaction_cap != 1140:
            raise ValueError("HB-GEN-1 call/evaluator caps changed")
        if item.gpu_exclusive_seconds_cap != 250000:
            raise ValueError("HB-GEN-1 GPU cap changed")
        if item.cpu_evaluator_seconds_cap != 1450000:
            raise ValueError("HB-GEN-1 CPU evaluator cap changed")
        if len(item.benchmarks) != len({pool.suite for pool in item.benchmarks}):
            raise ValueError("benchmark suite names must be unique")
        return item

    @property
    def heldout_ids(self) -> tuple[str, ...]:
        return tuple(
            f"{pool.suite}:{task_id}"
            for pool in self.benchmarks
            for task_id in pool.selected_heldout
        )


@dataclass(frozen=True)
class RuleSource:
    source_id: str
    repository: str
    commit: str
    path: str
    symbol: str
    line_span: tuple[int, int]
    sha256: str
    kind: str

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "RuleSource":
        _require_keys(
            payload,
            {
                "source_id",
                "repository",
                "commit",
                "path",
                "symbol",
                "line_span",
                "sha256",
                "kind",
            },
            "rule source",
        )
        commit = payload["commit"]
        if not isinstance(commit, str) or not _COMMIT.fullmatch(commit):
            raise ValueError("rule source commit is invalid")
        path = payload["path"]
        if (
            not isinstance(path, str)
            or not path
            or path.startswith("/")
            or "\\" in path
            or ".." in Path(path).parts
        ):
            raise ValueError("rule source path is invalid")
        span = payload["line_span"]
        if (
            not isinstance(span, list)
            or len(span) != 2
            or any(type(value) is not int or value <= 0 for value in span)
            or span[0] > span[1]
        ):
            raise ValueError("rule source line span is invalid")
        repository = payload["repository"]
        symbol = payload["symbol"]
        if not isinstance(repository, str) or not repository.strip():
            raise ValueError("rule source repository is invalid")
        if not isinstance(symbol, str) or not symbol.strip():
            raise ValueError("rule source symbol is invalid")
        kind = payload["kind"]
        if kind not in {"implementation", "test", "documentation", "evidence"}:
            raise ValueError("rule source kind is invalid")
        return cls(
            source_id=_safe_id(payload["source_id"], "rule source id"),
            repository=repository,
            commit=commit,
            path=path,
            symbol=symbol,
            line_span=(span[0], span[1]),
            sha256=_sha(payload["sha256"], "rule source sha256"),
            kind=kind,
        )


@dataclass(frozen=True)
class RuleConfidence:
    implementation: str
    empirical_scope: str
    transfer: str

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "RuleConfidence":
        _require_keys(
            payload,
            {"implementation", "empirical_scope", "transfer"},
            "rule confidence",
        )
        implementation = payload["implementation"]
        empirical_scope = payload["empirical_scope"]
        transfer = payload["transfer"]
        if implementation not in {
            "wired_tested",
            "wired_untested",
            "callable_not_wired",
            "prompt_only",
            "documented_only",
        }:
            raise ValueError("rule confidence implementation is invalid")
        if empirical_scope not in {
            "none",
            "single_campaign",
            "single_task_replicated",
            "multi_task_replicated",
        }:
            raise ValueError("rule confidence empirical scope is invalid")
        if transfer not in {
            "not_applicable",
            "unvalidated",
            "partially_validated",
            "validated",
        }:
            raise ValueError("rule confidence transfer is invalid")
        return cls(
            implementation=implementation,
            empirical_scope=empirical_scope,
            transfer=transfer,
        )


@dataclass(frozen=True)
class RuleRelations:
    requires: tuple[str, ...]
    excludes: tuple[str, ...]
    overrides: tuple[str, ...]
    fallback_rule_id: str | None
    on_same_write: str

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "RuleRelations":
        _require_keys(
            payload,
            {
                "requires",
                "excludes",
                "overrides",
                "fallback_rule_id",
                "on_same_write",
            },
            "rule relations",
        )
        for key in ("requires", "excludes", "overrides"):
            if not isinstance(payload[key], list):
                raise ValueError("rule relation list is invalid")
        fallback = payload["fallback_rule_id"]
        if fallback is not None:
            fallback = _safe_id(fallback, "fallback rule id")
        on_same_write = payload["on_same_write"]
        if on_same_write not in {"reject", "explicit_override", "merge_disjoint"}:
            raise ValueError("rule same-write policy is invalid")
        return cls(
            requires=tuple(
                _safe_id(value, "required rule id") for value in payload["requires"]
            ),
            excludes=tuple(
                _safe_id(value, "excluded rule id") for value in payload["excludes"]
            ),
            overrides=tuple(
                _safe_id(value, "overridden rule id") for value in payload["overrides"]
            ),
            fallback_rule_id=fallback,
            on_same_write=on_same_write,
        )


@dataclass(frozen=True)
class Rule:
    rule_id: str
    trigger: tuple[str, ...]
    action: tuple[str, ...]
    guardrails: tuple[str, ...]
    maturity: str
    provenance: tuple[str, ...]
    availability: str
    decision_plane: str
    enforcement: str
    operator_ref: str | None
    writes: tuple[str, ...]
    source_refs: tuple[str, ...]
    derivation_kind: str
    semantic_change_note: str
    confidence: RuleConfidence
    relations: RuleRelations

    @property
    def public_card(self) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "trigger": list(self.trigger),
            "action": list(self.action),
            "guardrails": list(self.guardrails),
            "availability": self.availability,
            "decision_plane": self.decision_plane,
            "enforcement": self.enforcement,
            "operator_ref": self.operator_ref,
            "writes": list(self.writes),
            "source_refs": list(self.source_refs),
            "confidence": {
                "implementation": self.confidence.implementation,
                "empirical_scope": self.confidence.empirical_scope,
                "transfer": self.confidence.transfer,
            },
        }


@dataclass(frozen=True)
class RuleRegistry:
    schema_version: int
    registry_id: str
    sources: tuple[RuleSource, ...]
    rules: tuple[Rule, ...]
    source_sha256: str

    @classmethod
    def from_json(cls, path: Path) -> "RuleRegistry":
        payload = _read_json(path)
        _require_keys(
            payload,
            {"schema_version", "registry_id", "sources", "rules"},
            "rule registry",
        )
        if payload["schema_version"] != 2:
            raise ValueError("unsupported rule registry schema")
        if not isinstance(payload["sources"], list) or not payload["sources"]:
            raise ValueError("rule registry sources are incomplete")
        sources = tuple(RuleSource.from_dict(raw) for raw in payload["sources"])
        if len(sources) != len({source.source_id for source in sources}):
            raise ValueError("rule source ids must be unique")
        source_ids = {source.source_id for source in sources}
        rules: list[Rule] = []
        for raw in payload["rules"]:
            _require_keys(
                raw,
                {
                    "rule_id",
                    "trigger",
                    "action",
                    "guardrails",
                    "maturity",
                    "provenance",
                    "availability",
                    "decision_plane",
                    "enforcement",
                    "operator_ref",
                    "writes",
                    "source_refs",
                    "derivation",
                    "confidence",
                    "relations",
                },
                "rule",
            )
            if not isinstance(raw["derivation"], dict):
                raise ValueError("rule derivation is invalid")
            _require_keys(
                raw["derivation"],
                {"kind", "semantic_change_note"},
                "rule derivation",
            )
            derivation_kind = raw["derivation"]["kind"]
            if derivation_kind not in {
                "verbatim",
                "parameterized_port",
                "composed",
                "moss_native",
            }:
                raise ValueError("rule derivation kind is invalid")
            note = raw["derivation"]["semantic_change_note"]
            if not isinstance(note, str) or not note.strip():
                raise ValueError("rule derivation note is invalid")
            availability = raw["availability"]
            if availability not in {"executable", "advisory", "external"}:
                raise ValueError("rule availability is invalid")
            plane = raw["decision_plane"]
            if plane not in {
                "guard",
                "recovery",
                "stop_restart",
                "forced_control",
                "schedule",
                "selection",
                "context_hint",
                "external_post_seal",
            }:
                raise ValueError("rule decision plane is invalid")
            enforcement = raw["enforcement"]
            if enforcement not in {
                "deterministic_guard",
                "typed_proposal",
                "prompt_context",
                "evidence_only",
                "external_post_seal",
            }:
                raise ValueError("rule enforcement is invalid")
            operator_ref = raw["operator_ref"]
            if operator_ref is not None:
                operator_ref = _safe_id(operator_ref, "rule operator ref")
            if availability == "executable" and operator_ref is None:
                raise ValueError("executable rule lacks an operator ref")
            if availability != "executable" and operator_ref is not None:
                raise ValueError("non-executable rule cannot bind an operator")
            if not isinstance(raw["writes"], list) or any(
                not isinstance(value, str) or not value.startswith("/")
                for value in raw["writes"]
            ):
                raise ValueError("rule write paths are invalid")
            if not isinstance(raw["source_refs"], list) or not raw["source_refs"]:
                raise ValueError("rule source references are invalid")
            source_refs = tuple(
                _safe_id(value, "rule source reference")
                for value in raw["source_refs"]
            )
            if not set(source_refs) <= source_ids:
                raise ValueError("rule source reference is unknown")
            rule = Rule(
                rule_id=_safe_id(raw["rule_id"], "rule id"),
                trigger=tuple(raw["trigger"]),
                action=tuple(raw["action"]),
                guardrails=tuple(raw["guardrails"]),
                maturity=_safe_id(raw["maturity"], "rule maturity"),
                provenance=tuple(raw["provenance"]),
                availability=availability,
                decision_plane=plane,
                enforcement=enforcement,
                operator_ref=operator_ref,
                writes=tuple(raw["writes"]),
                source_refs=source_refs,
                derivation_kind=derivation_kind,
                semantic_change_note=note,
                confidence=RuleConfidence.from_dict(raw["confidence"]),
                relations=RuleRelations.from_dict(raw["relations"]),
            )
            if not all(rule.trigger + rule.action + rule.guardrails + rule.provenance):
                raise ValueError("rule lists cannot contain empty text")
            rules.append(rule)
        registry = cls(
            schema_version=payload["schema_version"],
            registry_id=_safe_id(payload["registry_id"], "registry id"),
            sources=sources,
            rules=tuple(rules),
            source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        )
        if len(registry.rules) < 4:
            raise ValueError("rule registry is incomplete")
        if len(registry.rules) != len(set(registry.rule_ids)):
            raise ValueError("rule ids must be unique")
        registry._validate_relations()
        serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        for forbidden in ("0.9109", "50M", "300s", "B200", "WTE", "Zipf"):
            if forbidden in serialized:
                raise ValueError("rule registry contains task-specific payload")
        return registry

    def _validate_relations(self) -> None:
        rule_ids = set(self.rule_ids)
        graph: dict[str, set[str]] = {}
        for rule in self.rules:
            related = {
                *rule.relations.requires,
                *rule.relations.excludes,
                *rule.relations.overrides,
            }
            if rule.relations.fallback_rule_id is not None:
                related.add(rule.relations.fallback_rule_id)
            if rule.rule_id in related or not related <= rule_ids:
                raise ValueError("rule relation references are invalid")
            graph[rule.rule_id] = {
                *rule.relations.requires,
                *rule.relations.overrides,
                *(
                    (rule.relations.fallback_rule_id,)
                    if rule.relations.fallback_rule_id is not None
                    else ()
                ),
            }
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(rule_id: str) -> None:
            if rule_id in visiting:
                raise ValueError("rule relation graph contains a cycle")
            if rule_id in visited:
                return
            visiting.add(rule_id)
            for child in graph[rule_id]:
                visit(child)
            visiting.remove(rule_id)
            visited.add(rule_id)

        for rule_id in graph:
            visit(rule_id)

    @property
    def rule_ids(self) -> tuple[str, ...]:
        return tuple(rule.rule_id for rule in self.rules)

    @property
    def executable_rule_ids(self) -> tuple[str, ...]:
        return tuple(
            rule.rule_id for rule in self.rules if rule.availability == "executable"
        )

    @property
    def advisory_rule_ids(self) -> tuple[str, ...]:
        return tuple(
            rule.rule_id for rule in self.rules if rule.availability == "advisory"
        )

    @property
    def external_rule_ids(self) -> tuple[str, ...]:
        return tuple(
            rule.rule_id for rule in self.rules if rule.availability == "external"
        )

    def rule_for(self, rule_id: str) -> Rule:
        for rule in self.rules:
            if rule.rule_id == rule_id:
                return rule
        raise ValueError("unknown Rule Registry rule id")

    def planner_payload(self, allowed_rule_ids: tuple[str, ...]) -> dict[str, Any]:
        if not set(allowed_rule_ids) <= set(self.executable_rule_ids):
            raise ValueError("Builder allowlist contains a non-executable rule")
        return {
            "registry_id": self.registry_id,
            "rule_registry_sha256": self.source_sha256,
            "resolved_rule_cards": [
                self.rule_for(rule_id).public_card for rule_id in allowed_rule_ids
            ],
            "advisory_rule_cards": [
                self.rule_for(rule_id).public_card for rule_id in self.advisory_rule_ids
            ],
        }


@dataclass(frozen=True)
class BuilderVariant:
    variant_id: str
    description: str
    freeze_after_initial: bool
    continual_update: bool
    rule_registry_sha256: str
    allowed_rule_ids: tuple[str, ...]
    experience_sources: tuple[str, ...]
    excluded_task_ids: tuple[str, ...]
    adaptation_policy: str = "conditional_any_v1"

    def __post_init__(self) -> None:
        if self.adaptation_policy not in {
            "conditional_any_v1",
            "targeted_any_change_v1",
            "wide_all_fields_recompile_v1",
        }:
            raise ValueError("unsupported Builder adaptation policy")
        if self.freeze_after_initial and self.adaptation_policy != "conditional_any_v1":
            raise ValueError("a frozen Builder cannot require structural adaptation")

    @classmethod
    def list_from_json(cls, path: Path) -> tuple["BuilderVariant", ...]:
        payload = _read_json(path)
        if not isinstance(payload, list):
            raise ValueError("builder variants must be a list")
        values: list[BuilderVariant] = []
        for raw in payload:
            legacy_fields = {
                "variant_id",
                "description",
                "freeze_after_initial",
                "continual_update",
                "rule_registry_sha256",
                "allowed_rule_ids",
                "experience_sources",
                "excluded_task_ids",
            }
            if set(raw) not in {
                frozenset(legacy_fields),
                frozenset(legacy_fields | {"adaptation_policy"}),
            }:
                raise ValueError("builder variant keys differ")
            values.append(
                cls(
                    variant_id=_safe_id(raw["variant_id"], "variant id"),
                    description=raw["description"],
                    freeze_after_initial=raw["freeze_after_initial"],
                    continual_update=raw["continual_update"],
                    rule_registry_sha256=_sha(
                        raw["rule_registry_sha256"], "rule registry sha256"
                    ),
                    allowed_rule_ids=tuple(raw["allowed_rule_ids"]),
                    experience_sources=tuple(raw["experience_sources"]),
                    excluded_task_ids=tuple(raw["excluded_task_ids"]),
                    adaptation_policy=raw.get(
                        "adaptation_policy", "conditional_any_v1"
                    ),
                )
            )
        if len(values) != len({value.variant_id for value in values}):
            raise ValueError("builder variant ids must be unique")
        if any(
            value.adaptation_policy
            not in {
                "conditional_any_v1",
                "targeted_any_change_v1",
                "wide_all_fields_recompile_v1",
            }
            for value in values
        ):
            raise ValueError("unsupported Builder adaptation policy")
        return tuple(values)


_PARENT_STRATEGIES = {"reference", "incumbent", "stable_best", "restart", "recombine"}
_SCHEDULER_MODES = {"single_candidate", "repair_first", "explore_then_exploit"}
_RECOVERY_MODES = {"repair_then_reset", "reset_immediately", "preserve_failure"}
_EXECUTION_MODES = {"single_solution", "multi_step"}


@dataclass(frozen=True)
class HarnessDecision:
    schema_version: int
    rule_id: str
    role_graph: tuple[str, ...]
    memory_views: tuple[str, ...]
    tools: tuple[str, ...]
    parent_strategy: str
    workflow: tuple[str, ...]
    scheduler_mode: str
    recovery_mode: str
    kernel_directive: str
    execution_mode: str = "single_solution"

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "HarnessDecision":
        expected = {
            "schema_version",
            "rule_id",
            "role_graph",
            "memory_views",
            "tools",
            "parent_strategy",
            "workflow",
            "scheduler_mode",
            "recovery_mode",
            "kernel_directive",
        }
        if set(payload) not in (expected, expected | {"execution_mode"}):
            _require_keys(payload, expected, "Harness decision")
        normalized_lists: dict[str, tuple[str, ...]] = {}
        for field_name in ("role_graph", "memory_views", "tools", "workflow"):
            raw = payload[field_name]
            if not isinstance(raw, (list, tuple)) or not raw:
                raise ValueError(
                    f"Harness decision {field_name} must be a non-empty string array"
                )
            normalized_lists[field_name] = tuple(
                _safe_id(value, f"{field_name} component") for value in raw
            )
        parent_strategy = _safe_id(payload["parent_strategy"], "parent strategy")
        scheduler_mode = _safe_id(payload["scheduler_mode"], "scheduler mode")
        recovery_mode = _safe_id(payload["recovery_mode"], "recovery mode")
        item = cls(
            schema_version=payload["schema_version"],
            rule_id=_safe_id(payload["rule_id"], "rule id"),
            role_graph=normalized_lists["role_graph"],
            memory_views=normalized_lists["memory_views"],
            tools=normalized_lists["tools"],
            parent_strategy=parent_strategy,
            workflow=normalized_lists["workflow"],
            scheduler_mode=scheduler_mode,
            recovery_mode=recovery_mode,
            kernel_directive=payload["kernel_directive"],
            execution_mode=payload.get("execution_mode", "single_solution"),
        )
        if item.schema_version != 1:
            raise ValueError("unsupported Harness decision schema")
        if not item.role_graph or not item.memory_views or not item.tools or not item.workflow:
            raise ValueError("Harness decision operational lists cannot be empty")
        if item.parent_strategy not in _PARENT_STRATEGIES:
            raise ValueError("unsupported parent strategy")
        if item.scheduler_mode not in _SCHEDULER_MODES:
            raise ValueError("unsupported scheduler mode")
        if item.recovery_mode not in _RECOVERY_MODES:
            raise ValueError("unsupported recovery mode")
        if item.execution_mode not in _EXECUTION_MODES:
            raise ValueError("unsupported execution mode")
        if (
            not isinstance(item.kernel_directive, str)
            or not item.kernel_directive.strip()
            or len(item.kernel_directive) > 8_000
            or "\x00" in item.kernel_directive
            or _PRIVATE_DIRECTIVE.search(item.kernel_directive)
        ):
            raise ValueError("kernel directive is empty, unsafe, or too long")
        return item

    @property
    def operational_fingerprint(self) -> str:
        payload = {
            # These three axes are declarative memberships. Their order is not
            # executable and therefore cannot manufacture a new lineage node.
            "role_graph": sorted(self.role_graph),
            "memory_views": sorted(self.memory_views),
            "tools": sorted(self.tools),
            "parent_strategy": self.parent_strategy,
            "workflow": self.workflow,
            "scheduler_mode": self.scheduler_mode,
            "recovery_mode": self.recovery_mode,
            "execution_mode": self.execution_mode,
        }
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()

    @property
    def sha256(self) -> str:
        """Content hash used to bind decisions to compilation receipts."""

        encoded = json.dumps(
            {
                "schema_version": self.schema_version,
                "rule_id": self.rule_id,
                "role_graph": self.role_graph,
                "memory_views": self.memory_views,
                "tools": self.tools,
                "parent_strategy": self.parent_strategy,
                "workflow": self.workflow,
                "scheduler_mode": self.scheduler_mode,
                "recovery_mode": self.recovery_mode,
                "kernel_directive": self.kernel_directive,
                "execution_mode": self.execution_mode,
            },
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()

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
            "kernel_directive": self.kernel_directive,
            "execution_mode": self.execution_mode,
        }

    def require_operational_change_from(self, previous: "HarnessDecision") -> None:
        if not any(self.operational_change_map_from(previous).values()):
            raise ValueError("next Harness must contain an operational system change")

    def operational_change_map_from(
        self, previous: "HarnessDecision"
    ) -> dict[str, bool]:
        """Describe real changes across all seven executable Harness axes.

        Role, memory and tool collections are declarative sets. Reordering them
        is not an architectural change. Workflow order, however, is executable
        control flow and therefore remains significant.
        """

        if not isinstance(previous, HarnessDecision):
            raise ValueError("previous Harness decision is required")
        return {
            "role_graph": frozenset(self.role_graph) != frozenset(previous.role_graph),
            "memory_views": frozenset(self.memory_views)
            != frozenset(previous.memory_views),
            "tools": frozenset(self.tools) != frozenset(previous.tools),
            "parent_strategy": self.parent_strategy != previous.parent_strategy,
            "workflow": self.workflow != previous.workflow,
            "scheduler_mode": self.scheduler_mode != previous.scheduler_mode,
            "recovery_mode": self.recovery_mode != previous.recovery_mode,
        }

    def require_wide_change_from(self, previous: "HarnessDecision") -> None:
        unchanged = [
            axis
            for axis, changed in self.operational_change_map_from(previous).items()
            if not changed
        ]
        if unchanged:
            raise ValueError(
                "wide Harness transition left axes unchanged: " + ",".join(unchanged)
            )
