from __future__ import annotations

import json

import pytest

from optimization_lab.generation import FakeGenerator
from optimization_lab.harness_builder import operators
from optimization_lab.harness_builder.operators import (
    HarnessContext,
    PublicAttempt,
    TrustedOperatorRegistry,
)
from optimization_lab.harness_builder.runtime import HarnessRuntime
from optimization_lab.harness_builder.schema import BuilderVariant, HarnessDecision


def _decision(**updates: object) -> HarnessDecision:
    payload: dict[str, object] = {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["task_analyst", "generator", "verifier"],
        "memory_views": ["current", "best"],
        "tools": ["task_semantics", "score_history"],
        "parent_strategy": "reference",
        "workflow": ["analyze", "generate", "verify_contract"],
        "scheduler_mode": "single_candidate",
        "recovery_mode": "preserve_failure",
        "kernel_directive": "Preserve the contract and improve one candidate.",
    }
    payload.update(updates)
    return HarnessDecision.from_dict(payload)


def _wide_decision(**updates: object) -> HarnessDecision:
    payload: dict[str, object] = {
        "role_graph": ["task_analyst", "critic", "generator", "verifier"],
        "memory_views": ["current", "failures"],
        "tools": ["task_semantics", "code_diff"],
        "parent_strategy": "incumbent",
        "workflow": ["analyze", "criticize", "generate", "verify_contract"],
        "scheduler_mode": "repair_first",
        "recovery_mode": "repair_then_reset",
        "kernel_directive": "Rebuild every Harness axis under the trusted contract.",
    }
    payload.update(updates)
    return _decision(**payload)


def _variant() -> BuilderVariant:
    return BuilderVariant(
        variant_id="B-frozen-wide",
        description="fresh per-instance Builder with mandatory wide recompilation",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("discipline",),
        experience_sources=(),
        excluded_task_ids=(),
        adaptation_policy="wide_all_fields_recompile_v1",
    )


def _context() -> HarnessContext:
    return HarnessContext(
        instance_id="suite:task-001",
        suite="suite",
        round_index=2,
        task_card="Optimize one public task under a frozen evaluator contract.",
        reference_artifact_id="reference",
        reference_artifact="reference artifact",
        attempts=(
            PublicAttempt(
                attempt_id="v001",
                artifact_sha256="1" * 64,
                artifact_text="valid first artifact",
                correct=True,
                score=1.0,
                outcome="valid",
                structural_signature="family-a",
                public_summary="valid score 1.0",
            ),
        ),
    )


def test_wide_change_map_treats_component_sets_as_sets_but_workflow_as_ordered() -> None:
    previous = _decision()
    reordered = _decision(
        role_graph=list(reversed(previous.role_graph)),
        memory_views=list(reversed(previous.memory_views)),
        tools=list(reversed(previous.tools)),
        workflow=list(reversed(previous.workflow)),
    )

    changes = reordered.operational_change_map_from(previous)

    assert changes["role_graph"] is False
    assert changes["memory_views"] is False
    assert changes["tools"] is False
    assert changes["workflow"] is True
    set_only_reordered = _decision(
        role_graph=list(reversed(previous.role_graph)),
        memory_views=list(reversed(previous.memory_views)),
        tools=list(reversed(previous.tools)),
    )
    assert (
        set_only_reordered.operational_fingerprint
        == previous.operational_fingerprint
    )

    variant = BuilderVariant(
        variant_id="targeted",
        description="canonical set semantics",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("discipline",),
        experience_sources=(),
        excluded_task_ids=(),
    )
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    context = HarnessContext(**{**_context().__dict__, "round_index": 1, "attempts": ()})
    original_compile = registry.compile(previous, variant=variant, context=context)
    reordered_compile = registry.compile(
        set_only_reordered, variant=variant, context=context
    )
    assert [
        (item.axis, item.component_id, item.ordinal)
        for item in original_compile.component_instances
    ] == [
        (item.axis, item.component_id, item.ordinal)
        for item in reordered_compile.component_instances
    ]
    assert original_compile.axis_effect_sha256s == reordered_compile.axis_effect_sha256s


@pytest.mark.parametrize(
    "unchanged_axis",
    (
        "role_graph",
        "memory_views",
        "tools",
        "parent_strategy",
        "workflow",
        "scheduler_mode",
        "recovery_mode",
    ),
)
def test_wide_policy_rejects_each_single_unchanged_axis(unchanged_axis: str) -> None:
    previous = _decision()
    candidate = _wide_decision(
        **{unchanged_axis: getattr(previous, unchanged_axis)}
    )

    with pytest.raises(ValueError, match=unchanged_axis):
        candidate.require_wide_change_from(previous)


def test_runtime_rejects_wide_round_without_previous_accepted_harness() -> None:
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=FakeGenerator(json.dumps(_wide_decision().__dict__)),
        solution_generator=FakeGenerator("candidate"),
        model="fixture-model",
    )

    result = runtime.run_round(variant=_variant(), context=_context())

    assert result.planner_rejection_reason == "wide_harness_previous_receipt_missing"
    assert result.solution_result is None


def test_runtime_rejects_partial_change_even_when_normal_policy_would_allow_it() -> None:
    previous = _decision()
    partial = _decision(parent_strategy="incumbent")
    planner = FakeGenerator(json.dumps(partial.__dict__))
    solution = FakeGenerator("candidate")
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=planner,
        solution_generator=solution,
        model="fixture-model",
    )

    result = runtime.run_round(
        variant=_variant(),
        context=_context(),
        previous_decision=previous,
        previous_compile_receipt_sha256="1" * 64,
        prior_operational_fingerprints=(previous.operational_fingerprint,),
    )

    assert result.planner_rejection_reason == "wide_harness_change_incomplete"
    assert result.solution_result is None


def test_wide_planner_receives_complete_forbidden_lineage_fingerprints() -> None:
    previous = _decision()
    prior = ("1" * 64, previous.operational_fingerprint)
    planner = FakeGenerator(json.dumps(_wide_decision().__dict__))
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=planner,
        solution_generator=FakeGenerator("candidate"),
        model="fixture-model",
    )

    runtime.plan_and_compile(
        variant=_variant(),
        context=_context(),
        previous_decision=previous,
        previous_compile_receipt_sha256="1" * 64,
        prior_operational_fingerprints=prior,
    )

    assert planner.calls
    payload = json.loads(planner.calls[0]["prompt"].split("\n\n", 1)[1])
    assert payload["forbidden_lineage_operational_fingerprints"] == list(prior)


def test_wide_runtime_accepts_all_axis_change_and_reinstantiates_components() -> None:
    previous = _decision()
    candidate = _wide_decision()
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    runtime = HarnessRuntime(
        operator_registry=registry,
        planner=FakeGenerator(json.dumps(candidate.__dict__)),
        solution_generator=FakeGenerator("candidate"),
        model="fixture-model",
    )

    result = runtime.run_round(
        variant=_variant(),
        context=_context(),
        previous_decision=previous,
        previous_compile_receipt_sha256="1" * 64,
        prior_operational_fingerprints=(previous.operational_fingerprint,),
    )
    assert result.planner_rejection_reason is None
    assert result.compiled_harness is not None
    assert set(result.compiled_harness.change_map) == {
        "role_graph",
        "memory_views",
        "tools",
        "parent_strategy",
        "workflow",
        "scheduler_mode",
        "recovery_mode",
    }
    assert all(result.compiled_harness.change_map.values())
    initial_context = HarnessContext(
        **{**_context().__dict__, "round_index": 1, "attempts": ()}
    )
    initial_compiled = registry.compile(
        previous,
        variant=_variant(),
        context=initial_context,
    )
    assert all(
        result.compiled_harness.axis_configuration_sha256s[axis]
        != initial_compiled.axis_configuration_sha256s[axis]
        for axis in TrustedOperatorRegistry._operational_axes()
    )

    first = registry.compile(
        candidate,
        variant=_variant(),
        context=_context(),
        previous_decision=previous,
        prior_operational_fingerprints=(previous.operational_fingerprint,),
    )
    second = registry.compile(
        candidate,
        variant=_variant(),
        context=_context(),
        previous_decision=previous,
        prior_operational_fingerprints=(previous.operational_fingerprint,),
    )
    assert first.component_catalog_sha256 == second.component_catalog_sha256
    assert first.component_instances == second.component_instances
    assert len(first.component_instances) > 7
    assert all(
        left is not right
        for left, right in zip(first.component_instances, second.component_instances)
    )

    # A later physical round can follow a planner rejection, so its complete
    # accepted prefix still contains one Harness even though round_index is 3.
    next_context = HarnessContext(
        **{
            **_context().__dict__,
            "round_index": 3,
            "attempts": (
                *_context().attempts,
                PublicAttempt(
                    attempt_id="v002",
                    artifact_sha256="2" * 64,
                    artifact_text="rejected planner artifact",
                    correct=False,
                    score=None,
                    outcome="planner_contract_rejected",
                    structural_signature="planner-rejected",
                    public_summary="planner rejected",
                ),
            ),
        }
    )
    next_round = registry.compile(
        candidate,
        variant=_variant(),
        context=next_context,
        previous_decision=previous,
        prior_operational_fingerprints=(previous.operational_fingerprint,),
    )
    shared = {
        (item.axis, item.component_id): item.config_sha256
        for item in first.component_instances
    }
    assert all(
        shared[(item.axis, item.component_id)] != item.config_sha256
        for item in next_round.component_instances
        if (item.axis, item.component_id) in shared
    )
    assert (
        first.axis_configuration_sha256s
        == next_round.axis_configuration_sha256s
    )
    assert (
        first.axis_effect_sha256s["memory_views"]
        != next_round.axis_effect_sha256s["memory_views"]
    )


def test_parent_strategy_is_a_stable_configuration_and_visible_runtime_input() -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    context = HarnessContext(
        **{**_context().__dict__, "round_index": 1, "attempts": ()}
    )
    reference = registry.compile(
        _decision(parent_strategy="reference"),
        variant=_variant(),
        context=context,
    )
    restart = registry.compile(
        _decision(parent_strategy="restart"),
        variant=_variant(),
        context=context,
    )

    reference_payload = json.loads(reference.solution_prompt.split("\n\n", 1)[1])
    restart_payload = json.loads(restart.solution_prompt.split("\n\n", 1)[1])
    assert reference_payload["parent_strategy"] == "reference"
    assert restart_payload["parent_strategy"] == "restart"
    assert (
        reference.axis_configuration_sha256s["parent_strategy"]
        != restart.axis_configuration_sha256s["parent_strategy"]
    )


def test_registry_rejects_same_name_custom_tool_implementations() -> None:
    tools = dict(TrustedOperatorRegistry._default_tools())
    tools["task_semantics"] = lambda _context, _parents, _memory: {
        "forged": True
    }

    with pytest.raises(ValueError, match="custom tool implementations are forbidden"):
        TrustedOperatorRegistry(rule_registry_sha256="a" * 64, tools=tools)


def test_each_compile_builds_fresh_runtime_objects_with_deterministic_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    decision = _wide_decision()
    assemblies: list[object] = []
    original = registry._instantiate_components

    def capture(
        selected: HarnessDecision, context: HarnessContext
    ) -> object:
        assembly = original(selected, context)
        assemblies.append(assembly)
        return assembly

    monkeypatch.setattr(registry, "_instantiate_components", capture)
    kwargs = {
        "variant": _variant(),
        "context": _context(),
        "previous_decision": _decision(),
        "prior_operational_fingerprints": (_decision().operational_fingerprint,),
    }

    first = registry.compile(decision, **kwargs)
    second = registry.compile(decision, **kwargs)

    assert first == second
    assert assemblies[0] is not assemblies[1]
    first_objects = assemblies[0].all_components()  # type: ignore[union-attr]
    second_objects = assemblies[1].all_components()  # type: ignore[union-attr]
    assert len(first_objects) == len(second_objects)
    assert all(left is not right for left, right in zip(first_objects, second_objects))


def test_all_seven_axes_execute_through_fresh_typed_components(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = {axis: 0 for axis in TrustedOperatorRegistry._operational_axes()}
    wrapped = (
        (operators._RoleRuntimeComponent, "instruction", "role_graph"),
        (operators._MemoryRuntimeComponent, "resolve", "memory_views"),
        (operators._ToolRuntimeComponent, "execute", "tools"),
        (operators._ParentRuntimeComponent, "select", "parent_strategy"),
        (operators._WorkflowRuntimeComponent, "compile", "workflow"),
        (operators._SchedulerRuntimeComponent, "phase", "scheduler_mode"),
        (
            operators._RecoveryRuntimeComponent,
            "failed_parent_override",
            "recovery_mode",
        ),
    )
    for component_type, method_name, axis in wrapped:
        original = getattr(component_type, method_name)

        def spy(self: object, *args: object, _original=original, _axis=axis) -> object:
            calls[_axis] += 1
            return _original(self, *args)

        monkeypatch.setattr(component_type, method_name, spy)

    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    compiled = registry.compile(
        _wide_decision(),
        variant=_variant(),
        context=_context(),
        previous_decision=_decision(),
        prior_operational_fingerprints=(_decision().operational_fingerprint,),
    )

    assert all(count > 0 for count in calls.values())
    assert {item.axis for item in compiled.component_instances} == set(calls)


def test_wide_runtime_rejects_reusing_any_earlier_lineage_fingerprint() -> None:
    first = _decision()
    second = _wide_decision()
    third = first
    second_attempt = PublicAttempt(
        attempt_id="v002",
        artifact_sha256="2" * 64,
        artifact_text="valid second artifact",
        correct=True,
        score=1.1,
        outcome="valid",
        structural_signature="family-b",
        public_summary="valid score 1.1",
    )
    context = HarnessContext(
        **{
            **_context().__dict__,
            "round_index": 3,
            "attempts": (*_context().attempts, second_attempt),
        }
    )
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=FakeGenerator(json.dumps(third.__dict__)),
        solution_generator=FakeGenerator("candidate"),
        model="fixture-model",
    )

    result = runtime.run_round(
        variant=_variant(),
        context=context,
        previous_decision=second,
        previous_compile_receipt_sha256="2" * 64,
        prior_operational_fingerprints=(
            first.operational_fingerprint,
            second.operational_fingerprint,
        ),
    )

    assert result.planner_rejection_reason == "wide_harness_fingerprint_reused"
    assert result.solution_result is None


def test_trusted_compiler_rejects_v1_v2_v1_lineage_reuse_without_runtime() -> None:
    first = _decision()
    second = _wide_decision()
    second_attempt = PublicAttempt(
        attempt_id="v002",
        artifact_sha256="2" * 64,
        artifact_text="valid second artifact",
        correct=True,
        score=1.1,
        outcome="valid",
        structural_signature="family-b",
        public_summary="valid score 1.1",
    )
    context = HarnessContext(
        **{
            **_context().__dict__,
            "round_index": 3,
            "attempts": (*_context().attempts, second_attempt),
        }
    )
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)

    with pytest.raises(ValueError, match="reuse an earlier lineage fingerprint"):
        registry.compile(
            first,
            variant=_variant(),
            context=context,
            previous_decision=second,
            prior_operational_fingerprints=(
                first.operational_fingerprint,
                second.operational_fingerprint,
            ),
        )


def test_wide_runtime_rejects_round_three_without_complete_lineage_history() -> None:
    first = _decision()
    second = _wide_decision()
    context = HarnessContext(**{**_context().__dict__, "round_index": 3})
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=FakeGenerator(json.dumps(first.__dict__)),
        solution_generator=FakeGenerator("candidate"),
        model="fixture-model",
    )

    result = runtime.run_round(
        variant=_variant(),
        context=context,
        previous_decision=second,
        previous_compile_receipt_sha256="2" * 64,
    )

    assert (
        result.planner_rejection_reason
        == "wide_harness_lineage_history_missing"
    )
    assert result.solution_result is None
