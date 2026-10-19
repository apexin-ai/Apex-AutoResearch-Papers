from __future__ import annotations

import json

import pytest

from optimization_lab.generation import FakeGenerator
from optimization_lab.harness_builder.builder_evolution import (
    BuilderArtifact,
    BuilderPublicState,
    MetaPolicy,
    TaskHarnessPolicy,
)
from optimization_lab.harness_builder.operators import (
    CrossInstanceMemoryGrant,
    HarnessContext,
    PublicAttempt,
    TrustedOperatorRegistry,
)
from optimization_lab.harness_builder.runtime import (
    HarnessRuntime,
    parse_harness_decision,
)
from optimization_lab.harness_builder.schema import BuilderVariant, HarnessDecision


def _variant(
    variant_id: str = "B*",
    *,
    freeze: bool = False,
    sources: tuple[str, ...] = ("meta-v1",),
    adaptation_policy: str = "conditional_any_v1",
) -> BuilderVariant:
    return BuilderVariant(
        variant_id=variant_id,
        description="fixture",
        freeze_after_initial=freeze,
        continual_update=False,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=(
            "discipline",
            "dream",
            "law_inversion",
            "recombination",
            "correctness_recovery",
        ),
        experience_sources=sources,
        excluded_task_ids=("suite:heldout",),
        adaptation_policy=adaptation_policy,
    )


def _decision(**updates: object) -> HarnessDecision:
    payload: dict[str, object] = {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["task_analyst", "performance_analyst", "generator", "verifier"],
        "memory_views": ["current", "best", "failures"],
        "tools": ["task_semantics", "score_history", "static_structure"],
        "parent_strategy": "incumbent",
        "workflow": ["analyze", "select_parent", "inspect", "generate", "verify_contract"],
        "scheduler_mode": "single_candidate",
        "recovery_mode": "preserve_failure",
        "kernel_directive": "Change one measured bottleneck and preserve correctness.",
    }
    payload.update(updates)
    return HarnessDecision.from_dict(payload)


@pytest.mark.parametrize(
    ("field", "value"),
    (
        ("role_graph", [["generator"], "verifier"]),
        ("memory_views", {"current": True}),
        ("tools", ["task_semantics", 3]),
        ("workflow", "generate"),
    ),
)
def test_harness_decision_rejects_non_string_component_arrays(
    field: str, value: object
) -> None:
    with pytest.raises(ValueError, match=field):
        _decision(**{field: value})


@pytest.mark.parametrize(
    "directive",
    ("x" * 8_001, "read /home/ubuntu/private evaluator", "secret_token=abc"),
)
def test_harness_decision_rejects_unsafe_or_unbounded_directive(
    directive: str,
) -> None:
    with pytest.raises(ValueError, match="unsafe|too long"):
        _decision(kernel_directive=directive)


def _context(*, with_experience: bool = True) -> HarnessContext:
    records = (
        {
            "record_id": "meta-001",
            "source_instance_id": "kernelbench:train-001",
            "scope": "single_instance_observation",
            "summary": "A reduction task benefited from an architecture reset.",
        },
    ) if with_experience else ()
    grant = CrossInstanceMemoryGrant.issue(
        stream_index=4,
        checkpoint_sha256="b" * 64,
        experience_bank_sha256="c" * 64,
        records=records,
        eligible_source_instance_ids=("kernelbench:train-001",),
    ) if records else None
    return HarnessContext(
        instance_id="suite:task-001",
        suite="suite",
        round_index=4,
        task_card="Optimize the public task under the frozen correctness contract.",
        reference_artifact_id="reference",
        reference_artifact="reference solution",
        attempts=(
            PublicAttempt(
                attempt_id="v001",
                artifact_sha256="1" * 64,
                artifact_text="bad solution",
                correct=False,
                score=None,
                outcome="incorrect",
                structural_signature="family-a",
                public_summary="correctness failed",
            ),
            PublicAttempt(
                attempt_id="v002",
                artifact_sha256="2" * 64,
                artifact_text="correct solution a",
                correct=True,
                score=1.10,
                outcome="valid",
                structural_signature="family-a",
                public_summary="correct and 1.10 normalized score",
            ),
            PublicAttempt(
                attempt_id="v003",
                artifact_sha256="3" * 64,
                artifact_text="correct solution b",
                correct=True,
                score=1.20,
                outcome="valid",
                structural_signature="family-b",
                public_summary="correct and 1.20 normalized score",
            ),
        ),
        cross_instance_records=records,
        cross_instance_memory_grant=grant,
    )


def test_trusted_operator_registry_executes_system_level_decision() -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    decision = _decision(
        rule_id="recombination",
        memory_views=["current", "best", "failures", "structural_diverse", "cross_instance_records"],
        parent_strategy="recombine",
        scheduler_mode="explore_then_exploit",
    )

    compiled = registry.compile(decision, variant=_variant(), context=_context())

    assert compiled.selected_parent_ids == ("v003", "v002")
    assert set(compiled.memory) == {
        "current",
        "best",
        "failures",
        "structural_diverse",
        "cross_instance_records",
    }
    assert compiled.memory["best"][0]["attempt_id"] == "v003"
    assert compiled.tool_outputs["score_history"]["best_score"] == 1.2
    assert compiled.scheduler_phase == "explore"
    assert compiled.execution_steps[-1].step_id == "verify_contract"
    assert "correct solution b" in compiled.solution_prompt
    assert "correct solution a" in compiled.solution_prompt


def test_compiled_solver_prompt_contains_explicit_contract_skill() -> None:
    context = HarnessContext(
        **{
            **_context(with_experience=False).__dict__,
            "round_index": 1,
            "attempts": (),
            "public_observations": {
                "artifact_contract": {
                    "schema_version": 1,
                    "policy_id": "edgebench-file-bundle-v1",
                    "artifact_kind": "edgebench_file_bundle_v1",
                    "response_boundary": "one complete JSON object and no prose",
                    "literal_template": '{"schema_version":1,"files":[...]}' ,
                    "safe_normalizations": [],
                    "forbidden_transformations": ["markdown_fence"],
                    "public_failure_stages": ["response_boundary", "json_schema"],
                }
            },
        }
    )
    decision = _decision(
        rule_id="contract_compatibility",
        parent_strategy="reference",
        tools=["task_semantics"],
    )
    variant = BuilderVariant(
        **{
            **_variant(sources=()).__dict__,
            "allowed_rule_ids": ("contract_compatibility",),
        }
    )

    compiled = TrustedOperatorRegistry(rule_registry_sha256="a" * 64).compile(
        decision, variant=variant, context=context
    )

    assert "BENCHMARK CONTRACT SKILL" in compiled.solution_prompt
    assert "one complete JSON object and no prose" in compiled.solution_prompt
    assert "FINAL OUTPUT CHECKLIST" in compiled.solution_prompt


def test_operator_registry_fail_closed_on_unimplemented_or_leaking_components() -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)

    with pytest.raises(ValueError, match="tool"):
        registry.compile(
            _decision(tools=["score_history", "shell"]),
            variant=_variant(),
            context=_context(),
        )

    with pytest.raises(ValueError, match="cross-instance"):
        registry.compile(
            _decision(memory_views=["current", "cross_instance_records"]),
            variant=_variant(variant_id="B0", sources=()),
            context=_context(),
        )

    with pytest.raises(ValueError, match="same-instance"):
        HarnessContext(
            **{
                **_context(with_experience=False).__dict__,
                "cross_instance_records": (
                    {
                        "record_id": "leak",
                        "source_instance_id": "suite:task-001",
                        "scope": "single_instance_observation",
                        "summary": "same-instance result",
                    },
                ),
            }
        )


def test_online_memory_grant_authorizes_only_bound_prior_records() -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    online = BuilderVariant(
        **{
            **_variant(variant_id="B-online", sources=()).__dict__,
            "continual_update": True,
        }
    )
    decision = _decision(memory_views=["current", "cross_instance_records"])

    compiled = registry.compile(decision, variant=online, context=_context())

    assert compiled.memory["cross_instance_records"][0]["record_id"] == "meta-001"

    future_record = {
        "record_id": "future-001",
        "source_instance_id": "suite:future-task",
        "scope": "single_instance_observation",
        "summary": "Future evidence must never be visible.",
    }
    with pytest.raises(ValueError, match="grant"):
        HarnessContext(
            **{
                **_context().__dict__,
                "cross_instance_records": (future_record,),
            }
        )


def test_planner_prompt_exposes_exact_dynamic_component_contract() -> None:
    context = _context()
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=FakeGenerator("unused"),
        solution_generator=FakeGenerator("unused"),
        model="fixture-model",
    )
    online = BuilderVariant(
        **{
            **_variant(variant_id="B-online", sources=()).__dict__,
            "continual_update": True,
        }
    )

    prompt = runtime._planner_prompt(online, context, None)

    assert '"harness_decision_template"' in prompt
    assert '"eligible_memory_views"' in prompt
    assert '"cross_instance_records"' in prompt
    assert '"allowed_role_ids"' in prompt
    assert "correct solution b" in prompt
    assert "pre_decision_tool_outputs" in prompt


def test_v001_requires_contract_grounded_initial_harness_when_rule_is_enabled() -> None:
    context = HarnessContext(
        **{
            **_context(with_experience=False).__dict__,
            "round_index": 1,
            "attempts": (),
            "public_observations": {
                "artifact_contract": {
                    "policy_id": "fixture-contract-v1",
                    "literal_template": "one exact artifact",
                }
            },
        }
    )
    variant = BuilderVariant(
        **{
            **_variant(sources=()).__dict__,
            "allowed_rule_ids": (
                "contract_compatibility",
                "discipline",
                "correctness_recovery",
            ),
        }
    )
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)

    with pytest.raises(ValueError, match="artifact contract"):
        registry.compile(
            _decision(rule_id="discipline", parent_strategy="reference"),
            variant=variant,
            context=context,
        )

    compiled = registry.compile(
        _decision(
            rule_id="contract_compatibility",
            parent_strategy="reference",
            tools=["task_semantics", "static_structure"],
        ),
        variant=variant,
        context=context,
    )
    assert compiled.rule_decision_trace["rule_id"] == "contract_compatibility"
    capability = context.public_observations["artifact_contract"]
    assert compiled.tool_outputs["task_semantics"]["artifact_contract"] == capability
    assert compiled.tool_outputs["task_semantics"]["artifact_contract"] is not capability
    solution_payload = json.loads(compiled.solution_prompt.split("\n\n", 1)[1])
    assert (
        solution_payload["tool_outputs"]["task_semantics"]["artifact_contract"]
        == capability
    )

    runtime = HarnessRuntime(
        operator_registry=registry,
        planner=FakeGenerator("unused"),
        solution_generator=FakeGenerator("unused"),
        model="fixture-model",
    )
    prompt = runtime._planner_prompt(variant, context, None)
    assert '"required_rule_id": "contract_compatibility"' in prompt


def test_task_semantics_exposes_only_the_bound_artifact_contract() -> None:
    context = HarnessContext(
        **{
            **_context(with_experience=False).__dict__,
            "round_index": 1,
            "attempts": (),
            "public_observations": {
                "artifact_contract": {
                    "policy_id": "fixture-contract-v1",
                    "literal_template": "one exact artifact",
                },
                "unrelated_public_observation": "sentinel-must-not-reach-solver",
            },
        }
    )
    variant = BuilderVariant(
        **{
            **_variant(sources=()).__dict__,
            "allowed_rule_ids": ("contract_compatibility",),
        }
    )
    compiled = TrustedOperatorRegistry(rule_registry_sha256="a" * 64).compile(
        _decision(
            rule_id="contract_compatibility",
            parent_strategy="reference",
            tools=["task_semantics"],
        ),
        variant=variant,
        context=context,
    )

    assert "unrelated_public_observation" not in compiled.solution_prompt
    assert "sentinel-must-not-reach-solver" not in compiled.solution_prompt
    assert set(compiled.tool_outputs["task_semantics"]) == {
        "artifact_contract",
        "instance_id",
        "suite",
        "task_card",
    }


def test_rule_guards_and_recovery_change_actual_parent_selection() -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    context = _context()

    dream = registry.compile(
        _decision(rule_id="dream", parent_strategy="restart"),
        variant=_variant(),
        context=context,
    )
    assert dream.selected_parent_ids == ("reference",)

    recombine_without_two_families = HarnessContext(
        **{
            **context.__dict__,
            "attempts": context.attempts[:2],
        }
    )
    with pytest.raises(ValueError, match="two correct structural families"):
        registry.compile(
            _decision(rule_id="recombination", parent_strategy="recombine"),
            variant=_variant(),
            context=recombine_without_two_families,
        )

    latest_failed = HarnessContext(
        **{
            **context.__dict__,
            "attempts": context.attempts
            + (
                PublicAttempt(
                    attempt_id="v004",
                    artifact_sha256="4" * 64,
                    artifact_text="latest broken solution",
                    correct=False,
                    score=None,
                    outcome="compile_failed",
                    structural_signature="family-c",
                    public_summary="compile failed",
                ),
            ),
        }
    )
    repaired = registry.compile(
        _decision(
            rule_id="correctness_recovery",
            recovery_mode="repair_then_reset",
        ),
        variant=_variant(),
        context=latest_failed,
    )
    assert repaired.selected_parent_ids == ("v004",)


def test_strict_decision_parser_rejects_salvage_and_duplicate_keys() -> None:
    payload = {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["task_analyst", "generator", "verifier"],
        "memory_views": ["current"],
        "tools": ["task_semantics"],
        "parent_strategy": "reference",
        "workflow": ["analyze", "generate", "verify_contract"],
        "scheduler_mode": "single_candidate",
        "recovery_mode": "preserve_failure",
        "kernel_directive": "Build one correct candidate.",
    }
    decision = parse_harness_decision(json.dumps(payload))
    assert decision.rule_id == "discipline"
    fenced = parse_harness_decision(f"```json\n{json.dumps(payload)}\n```")
    assert fenced == decision

    with pytest.raises(ValueError, match="whole response"):
        parse_harness_decision(f"Here is the decision: {json.dumps(payload)}")
    duplicate = json.dumps(payload)[:-1] + ',"rule_id":"dream"}'
    with pytest.raises(ValueError, match="duplicate"):
        parse_harness_decision(duplicate)


def test_runtime_uses_frozen_A_decision_but_still_consumes_sham_planner_call() -> None:
    frozen = _decision(parent_strategy="reference")
    sham_output = json.dumps(
        {
            "schema_version": 1,
            "rule_id": "dream",
            "role_graph": ["task_analyst", "generator", "verifier"],
            "memory_views": ["current"],
            "tools": ["task_semantics"],
            "parent_strategy": "restart",
            "workflow": ["analyze", "generate", "verify_contract"],
            "scheduler_mode": "single_candidate",
            "recovery_mode": "reset_immediately",
            "kernel_directive": "This sham output must not change the frozen Harness.",
        }
    )
    planner = FakeGenerator(sham_output)
    solution = FakeGenerator("candidate artifact")
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=planner,
        solution_generator=solution,
        model="fixture-model",
    )

    result = runtime.run_round(
        variant=_variant(variant_id="A", freeze=True, sources=()),
        context=_context(with_experience=False),
        frozen_decision=frozen,
        previous_decision=frozen,
    )

    assert len(planner.calls) == 1
    assert len(solution.calls) == 1
    assert result.used_sham_planner is True
    assert result.decision == frozen
    assert "Sham planner" in planner.calls[0]["prompt"]
    assert "full strict HarnessDecision JSON" in planner.calls[0]["prompt"]


def test_runtime_rejects_prompt_only_update_after_a_flat_round() -> None:
    decision = _decision()
    planner = FakeGenerator(
        json.dumps(
            {
                "schema_version": decision.schema_version,
                "rule_id": decision.rule_id,
                "role_graph": list(decision.role_graph),
                "memory_views": list(decision.memory_views),
                "tools": list(decision.tools),
                "parent_strategy": decision.parent_strategy,
                "workflow": list(decision.workflow),
                "scheduler_mode": decision.scheduler_mode,
                "recovery_mode": decision.recovery_mode,
                "kernel_directive": "Only the wording changed.",
            }
        )
    )
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=planner,
        solution_generator=FakeGenerator("candidate"),
        model="fixture-model",
    )

    flat = HarnessContext(
        **{
            **_context().__dict__,
            "round_index": 5,
            "attempts": _context().attempts
            + (
                PublicAttempt(
                    attempt_id="v004",
                    artifact_sha256="4" * 64,
                    artifact_text="flat solution",
                    correct=True,
                    score=1.201,
                    outcome="valid",
                    structural_signature="family-b",
                    public_summary="less than two percent improvement",
                ),
            ),
        }
    )
    rejected = runtime.run_round(
        variant=_variant(),
        context=flat,
        previous_decision=decision,
    )

    assert rejected.planner_rejection_reason == "no_operational_change"
    assert rejected.decision is None
    assert rejected.compiled_harness is None
    assert rejected.solution_result is None


def test_targeted_policy_requires_real_change_even_after_improvement() -> None:
    previous = _decision()
    prompt_only = _decision(kernel_directive="Only the wording changed.")
    improved = HarnessContext(
        **{
            **_context().__dict__,
            "round_index": 5,
            "attempts": _context().attempts
            + (
                PublicAttempt(
                    attempt_id="v004",
                    artifact_sha256="4" * 64,
                    artifact_text="improved solution",
                    correct=True,
                    score=1.50,
                    outcome="valid",
                    structural_signature="family-c",
                    public_summary="large public improvement",
                ),
            ),
        }
    )
    planner = FakeGenerator(json.dumps(prompt_only.__dict__))
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=planner,
        solution_generator=FakeGenerator("must not run"),
        model="fixture-model",
    )

    rejected = runtime.run_round(
        variant=_variant(
            variant_id="B-targeted",
            sources=(),
            adaptation_policy="targeted_any_change_v1",
        ),
        context=improved,
        previous_decision=previous,
    )

    assert rejected.planner_rejection_reason == "no_operational_change"
    assert rejected.solution_result is None
    assert '"requires_operational_change": true' in planner.calls[0]["prompt"]


def test_b0_and_trained_builder_prompts_differ_only_through_bound_experience() -> None:
    context = _context(with_experience=False)
    b0 = _variant(variant_id="B0", sources=())
    trained = _variant(variant_id="B*", sources=("meta-v1",))
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=FakeGenerator("unused"),
        solution_generator=FakeGenerator("unused"),
        model="fixture-model",
    )

    assert runtime._planner_prompt(b0, context, None) == runtime._planner_prompt(
        trained, context, None
    )


def test_runtime_executes_opt_in_multi_step_harness_with_stage_results() -> None:
    decision = _decision(
        execution_mode="multi_step",
        workflow=["analyze", "generate", "verify_contract"],
    )
    planner = FakeGenerator(json.dumps(decision.__dict__))
    stage_generators = {
        "analyze": FakeGenerator("analysis"),
        "generate": FakeGenerator("candidate artifact"),
        "verify_contract": FakeGenerator("verification"),
    }
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=planner,
        solution_generator=FakeGenerator("unused"),
        solution_generator_factory=stage_generators.__getitem__,
        model="fixture-model",
    )

    result = runtime.run_round(
        variant=_variant(),
        context=_context(),
    )

    assert result.decision is not None
    assert result.decision.execution_mode == "multi_step"
    assert result.solution_result is not None
    assert result.solution_result.raw_response == "candidate artifact"
    assert [stage_id for stage_id, _ in result.solution_stage_results] == [
        "analyze",
        "generate",
        "verify_contract",
    ]
    assert all(len(generator.calls) == 1 for generator in stage_generators.values())
    assert "analysis" in stage_generators["generate"].calls[0]["prompt"]
    assert "candidate artifact" in stage_generators["verify_contract"].calls[0]["prompt"]


def test_frozen_arm_preserves_failed_v001_instead_of_reinitializing() -> None:
    context = HarnessContext(
        **{
            **_context().__dict__,
            "round_index": 2,
            "attempts": (
                PublicAttempt(
                    attempt_id="v001",
                    artifact_sha256="1" * 64,
                    artifact_text="planner-contract-rejected Harness decision",
                    correct=False,
                    score=None,
                    outcome="planner_contract_rejected",
                    structural_signature="planner-rejected",
                    public_summary="v001 planner contract rejected",
                ),
            ),
        }
    )
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=FakeGenerator(json.dumps(_decision().__dict__)),
        solution_generator=FakeGenerator("must not run"),
        model="fixture-model",
    )

    result = runtime.run_round(
        variant=_variant(variant_id="A", freeze=True, sources=()),
        context=context,
        previous_decision=None,
        frozen_decision=None,
    )

    assert result.used_sham_planner is True
    assert result.planner_rejection_reason == "missing_frozen_initial_harness"
    assert result.decision is None
    assert result.solution_result is None


def test_runtime_executes_builder_artifact_scaffold_without_planner_code_change() -> None:
    parent = BuilderArtifact.initial()
    task_policy = TaskHarnessPolicy.from_dict(
        {
            **parent.task_harness_policy.to_dict(),
            "role_graph": ["task_analyst", "critic", "generator", "verifier"],
            "workflow": ["analyze", "criticize", "generate", "verify_contract"],
            "execution_mode": "multi_step",
        }
    )
    artifact = BuilderArtifact(
        schema_version=1,
        builder_id="builder-runtime",
        parent_builder_sha256=parent.sha256,
        task_harness_policy=task_policy,
        meta_policy=MetaPolicy.from_dict(
            {
                **parent.meta_policy.to_dict(),
                "mutation_families": ["discipline"],
                "search_mode": "exploit",
                "proposal_budget": 2,
            }
        ),
    )
    planner = FakeGenerator("must not run")
    stage_generators = {
        "analyze": FakeGenerator("analysis"),
        "criticize": FakeGenerator("critique"),
        "generate": FakeGenerator("candidate artifact"),
        "verify_contract": FakeGenerator("verified"),
    }
    runtime = HarnessRuntime(
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        planner=planner,
        solution_generator=FakeGenerator("unused"),
        solution_generator_factory=stage_generators.__getitem__,
        model="fixture-model",
    )
    context = _context()
    public_state = BuilderPublicState(
        schema_version=1,
        task_id=context.instance_id,
        round_index=context.round_index,
        scores=(None, 1.1, 1.2),
        feedback="valid improvement",
        diagnostics={"score_trend": "improving", "structure": "family-b"},
        memory={"current": {"attempt_id": "v003"}},
    )

    result = runtime.run_round(
        variant=_variant(),
        context=context,
        builder_artifact=artifact,
        builder_public_state=public_state,
    )

    assert planner.calls == []
    assert result.planner_result.provider == "builder-artifact-runtime"
    assert result.compiled_builder_scaffold is not None
    assert result.compiled_builder_scaffold.proposal_slots == (
        "proposal-001",
        "proposal-002",
    )
    assert result.decision is not None
    assert result.decision.role_graph == task_policy.role_graph
    assert result.decision.workflow == task_policy.workflow
    assert result.solution_result is not None
    assert result.solution_result.raw_response == "candidate artifact"
    assert all(len(generator.calls) == 1 for generator in stage_generators.values())
