from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.operators import (
    HarnessContext,
    TrustedOperatorRegistry,
)
from optimization_lab.harness_builder.runtime import HarnessRuntime
from optimization_lab.harness_builder.schema import (
    BuilderVariant,
    HarnessDecision,
    RuleRegistry,
)
from optimization_lab.generation import FakeGenerator


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "optimization_lab/harness_builder/data"
V2 = DATA / "rule_registry_v2.json"
V3 = DATA / "rule_registry_v3.json"


def _decision(rule_id: str = "discipline") -> HarnessDecision:
    return HarnessDecision.from_dict(
        {
            "schema_version": 1,
            "rule_id": rule_id,
            "role_graph": ["task_analyst", "generator", "verifier"],
            "memory_views": ["current"],
            "tools": ["task_semantics"],
            "parent_strategy": "reference",
            "workflow": ["analyze", "generate", "verify_contract"],
            "scheduler_mode": "single_candidate",
            "recovery_mode": "preserve_failure",
            "kernel_directive": "Produce one bounded correctness-preserving change.",
        }
    )


def _variant(registry: RuleRegistry, *, allowed: tuple[str, ...]) -> BuilderVariant:
    return BuilderVariant(
        variant_id="B0",
        description="fixture",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256=registry.source_sha256,
        allowed_rule_ids=allowed,
        experience_sources=(),
        excluded_task_ids=(),
    )


def _context() -> HarnessContext:
    return HarnessContext(
        instance_id="suite:task",
        suite="suite",
        round_index=1,
        task_card="Optimize the public task.",
        reference_artifact_id="reference",
        reference_artifact="reference candidate",
    )


def test_v2_registry_is_provenance_bound_and_separates_execution_authority() -> None:
    registry = RuleRegistry.from_json(V2)

    assert registry.schema_version == 2
    assert registry.registry_id == "hb-rule-registry-v2"
    assert registry.source_sha256 == hashlib.sha256(V2.read_bytes()).hexdigest()
    assert registry.executable_rule_ids == (
        "discipline",
        "dream",
        "law_inversion",
        "recombination",
        "correctness_recovery",
    )
    assert "successor_followup" in registry.advisory_rule_ids
    assert "cross_instance_distillation" in registry.external_rule_ids
    apex_sources = tuple(
        source for source in registry.sources if source.repository.endswith("Apex-Tune")
    )
    assert apex_sources
    assert all(
        source.commit == "17223eec6f7c29490888a278c86122e9f9f070ad"
        for source in apex_sources
    )
    assert all(len(source.sha256) == 64 for source in registry.sources)


def test_v3_registry_makes_contract_compatibility_an_executable_initial_rule() -> None:
    registry = RuleRegistry.from_json(V3)

    assert registry.registry_id == "hb-rule-registry-v3"
    assert registry.executable_rule_ids[0] == "contract_compatibility"
    assert "cross_instance_distillation" in registry.external_rule_ids
    rule = registry.rule_for("contract_compatibility")
    assert rule.operator_ref == "moss.rule.contract_compatibility.v1"
    assert rule.enforcement == "deterministic_guard"

    context = HarnessContext(
        **{
            **_context().__dict__,
            "public_observations": {
                "artifact_contract": {
                    "policy_id": "fixture-contract-v1",
                    "literal_template": "one exact artifact",
                }
            },
        }
    )
    compiled = TrustedOperatorRegistry(
        rule_registry_sha256=registry.source_sha256,
        rule_registry=registry,
    ).compile(
        _decision("contract_compatibility"),
        variant=_variant(registry, allowed=registry.executable_rule_ids),
        context=context,
    )
    assert compiled.rule_decision_trace["rule_id"] == "contract_compatibility"


def test_v2_preserves_v1_cards_but_does_not_promote_unwired_rules() -> None:
    legacy = json.loads((DATA / "rule_registry_v1.json").read_text(encoding="utf-8"))
    registry = RuleRegistry.from_json(V2)
    legacy_cards = {
        item["rule_id"]: (
            item["trigger"],
            item["action"],
            item["guardrails"],
        )
        for item in legacy["rules"]
    }

    assert tuple(legacy_cards) == registry.rule_ids
    for rule in registry.rules:
        assert legacy_cards[rule.rule_id] == (
            list(rule.trigger),
            list(rule.action),
            list(rule.guardrails),
        )
    assert not ({"successor_followup", "archive_reflection"} & set(registry.executable_rule_ids))


@pytest.mark.parametrize(
    ("mutate", "message"),
    (
        (lambda payload: payload["sources"][0].update(commit="bad"), "commit"),
        (lambda payload: payload["sources"][0].update(sha256="bad"), "sha256"),
        (lambda payload: payload["sources"][0].update(path="../escape.py"), "path"),
        (lambda payload: payload["sources"][0].update(line_span=[20, 10]), "line"),
        (
            lambda payload: payload["rules"][0].update(source_refs=["missing"]),
            "source",
        ),
        (
            lambda payload: payload["rules"][0]["confidence"].update(
                implementation="claimed"
            ),
            "confidence",
        ),
    ),
)
def test_v2_registry_fails_closed_on_invalid_provenance(
    tmp_path: Path, mutate, message: str
) -> None:
    payload = json.loads(V2.read_text(encoding="utf-8"))
    mutate(payload)
    path = tmp_path / "invalid.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        RuleRegistry.from_json(path)


def test_planner_receives_resolved_cards_but_cannot_select_advisory_rules() -> None:
    registry = RuleRegistry.from_json(V2)
    operator_registry = TrustedOperatorRegistry(
        rule_registry_sha256=registry.source_sha256,
    )
    assert operator_registry.rule_registry == registry
    planner = FakeGenerator(json.dumps(_decision().__dict__))
    runtime = HarnessRuntime(
        operator_registry=operator_registry,
        planner=planner,
        solution_generator=FakeGenerator("candidate"),
        model="fixture-model",
    )
    allowed = registry.executable_rule_ids
    runtime.run_round(
        variant=_variant(registry, allowed=allowed),
        context=_context(),
    )

    prompt = planner.calls[0]["prompt"]
    assert '"resolved_rule_cards"' in prompt
    assert '"advisory_rule_cards"' in prompt
    assert '"rule_registry_sha256"' in prompt
    assert "Apex-Tune" not in prompt
    for forbidden in ("0.9109", "50M", "300s", "B200", "WTE", "Zipf"):
        assert forbidden not in prompt

    advisory = _variant(registry, allowed=("successor_followup",))
    with pytest.raises(ValueError, match="not executable"):
        operator_registry.compile(
            _decision("successor_followup"),
            variant=advisory,
            context=_context(),
        )
    unknown = _variant(registry, allowed=("invented_rule",))
    with pytest.raises(ValueError, match="unknown"):
        operator_registry.compile(
            _decision("invented_rule"),
            variant=unknown,
            context=_context(),
        )


def test_rule_label_alone_is_not_an_operational_system_change() -> None:
    first = _decision("discipline")
    second = _decision("law_inversion")

    assert first.operational_fingerprint == second.operational_fingerprint
    with pytest.raises(ValueError, match="operational"):
        second.require_operational_change_from(first)


def test_compiled_harness_binds_a_rule_decision_trace() -> None:
    registry = RuleRegistry.from_json(V2)
    operator_registry = TrustedOperatorRegistry(
        rule_registry_sha256=registry.source_sha256,
        rule_registry=registry,
    )

    compiled = operator_registry.compile(
        _decision(),
        variant=_variant(registry, allowed=registry.executable_rule_ids),
        context=_context(),
    )

    assert compiled.rule_decision_trace["rule_id"] == "discipline"
    assert compiled.rule_decision_trace["rule_registry_sha256"] == registry.source_sha256
    assert compiled.rule_decision_trace["operator_ref"] == "moss.rule.discipline.v1"
    assert compiled.rule_decision_trace["availability"] == "executable"
    assert '"rule_effect"' in compiled.solution_prompt
    assert '"action"' in compiled.solution_prompt
