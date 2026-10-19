from __future__ import annotations

import json

import pytest

from optimization_lab.harness_builder.meta_evolution import (
    COMPONENT_AXES,
    HarnessArchiveNode,
    HarnessArchiveSnapshot,
    MetaCheckpointV2,
    MetaPolicySnapshot,
    TrustedMetaPolicyRegistry,
)
from optimization_lab.harness_builder.meta_prior import BuilderMetaPrior
from optimization_lab.harness_builder.operators import HarnessContext, TrustedOperatorRegistry
from optimization_lab.harness_builder.runtime import HarnessRuntime
from optimization_lab.harness_builder.schema import BuilderVariant, HarnessDecision
from optimization_lab.generation import FakeGenerator


def _selection() -> dict[str, tuple[str, ...]]:
    return {
        "role_graph": ("task_analyst", "generator", "verifier"),
        "memory_views": ("current",),
        "tools": ("task_semantics",),
        "parent_strategy": ("reference",),
        "workflow": ("analyze", "generate", "verify_contract"),
        "scheduler_mode": ("single_candidate",),
        "recovery_mode": ("preserve_failure",),
    }


def _checkpoint(
    registry: TrustedMetaPolicyRegistry,
    *,
    memory_sha: str,
    policy_sha: str,
    archive_sha: str,
) -> MetaCheckpointV2:
    return MetaCheckpointV2(
        checkpoint_id="checkpoint-v001",
        parent_checkpoint_sha256="1" * 64,
        trusted_meta_registry_sha256=registry.sha256,
        next_stream_index=1,
        learned_through_instance_id="suite:source-000",
        memory_sha256=memory_sha,
        meta_policy_sha256=policy_sha,
        harness_archive_sha256=archive_sha,
    )


def _variant() -> BuilderVariant:
    return BuilderVariant(
        variant_id="B-online-typed-prior",
        description="typed meta-prior fixture",
        freeze_after_initial=False,
        continual_update=True,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("discipline",),
        experience_sources=(),
        excluded_task_ids=(),
    )


def _decision(**updates: object) -> HarnessDecision:
    payload: dict[str, object] = {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["task_analyst", "generator", "verifier"],
        "memory_views": ["current"],
        "tools": ["task_semantics"],
        "parent_strategy": "reference",
        "workflow": ["analyze", "generate", "verify_contract"],
        "scheduler_mode": "single_candidate",
        "recovery_mode": "preserve_failure",
        "kernel_directive": "Follow the frozen task contract.",
    }
    payload.update(updates)
    return HarnessDecision.from_dict(payload)


def _context(prior: BuilderMetaPrior) -> HarnessContext:
    return HarnessContext(
        instance_id="suite:target-001",
        suite="suite",
        round_index=1,
        task_card="Solve the target using only public benchmark feedback.",
        reference_artifact_id="reference",
        reference_artifact="reference artifact",
        stream_index=1,
        builder_meta_prior=prior,
    )


def _policy_prior() -> tuple[BuilderMetaPrior, MetaPolicySnapshot]:
    registry = TrustedMetaPolicyRegistry.default()
    candidates = dict(registry.components)
    candidates.update(_selection())
    policy = MetaPolicySnapshot.create(
        policy_id="policy-v001",
        registry=registry,
        component_candidates=candidates,
    )
    checkpoint = _checkpoint(
        registry,
        memory_sha="b" * 64,
        policy_sha=policy.sha256,
        archive_sha="c" * 64,
    )
    return (
        BuilderMetaPrior.from_policy(
            policy=policy,
            checkpoint=checkpoint,
            registry=registry,
            target_instance_id="suite:target-001",
        ),
        policy,
    )


def test_op_prior_is_planner_only_and_hard_compile_allowlist() -> None:
    prior, _policy = _policy_prior()
    context = _context(prior)
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    runtime = HarnessRuntime(
        operator_registry=registry,
        planner=FakeGenerator("unused"),
        solution_generator=FakeGenerator("unused"),
        model="fixture-model",
    )

    prompt = runtime._planner_prompt(_variant(), context, None)
    planner_payload = json.loads(prompt.split("\n\n", 1)[1])
    assert planner_payload["current_context"]["builder_meta_prior"]["mechanism_id"] == "OP"
    assert planner_payload["component_contract"]["allowed_tool_ids"] == [
        "task_semantics"
    ]
    compiled = registry.compile(_decision(), variant=_variant(), context=context)
    assert compiled.builder_meta_prior_sha256 == prior.sha256
    assert prior.sha256 not in compiled.solution_prompt
    assert "builder_meta_prior" not in compiled.solution_prompt

    with pytest.raises(ValueError, match="meta-policy constraints"):
        registry.compile(
            _decision(tools=["task_semantics", "code_diff"]),
            variant=_variant(),
            context=context,
        )


def test_meta_prior_target_mechanism_and_private_fields_fail_closed() -> None:
    prior, _policy = _policy_prior()
    with pytest.raises(ValueError, match="target binding"):
        HarnessContext(
            **{**_context(prior).__dict__, "instance_id": "suite:other-target"}
        )
    with pytest.raises(ValueError, match="target binding"):
        HarnessContext(**{**_context(prior).__dict__, "stream_index": 2})
    with pytest.raises(ValueError, match="payload schema"):
        BuilderMetaPrior(
            **{**prior.__dict__, "payload": {**dict(prior.payload), "prompt": "x"}}
        )


def test_oa_prior_selects_only_prior_typed_recipes() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    policy = MetaPolicySnapshot.create(
        policy_id="fixed-selector-v001", registry=registry
    )
    node = HarnessArchiveNode.create(
        node_id="node-v001",
        registry=registry,
        source_suite="suite",
        source_instance_id="suite:source-000",
        source_stream_index=0,
        harness_decision_sha256="d" * 64,
        component_selection=_selection(),
        metrics={
            "quality": 0.8,
            "novelty": 0.5,
            "recovery": 0.4,
            "efficiency": 0.7,
        },
        provenance_event_ids=("sealed-source-event",),
    )
    archive = HarnessArchiveSnapshot.create(
        archive_id="archive-v001", registry=registry, nodes=(node,)
    )
    checkpoint = _checkpoint(
        registry,
        memory_sha="b" * 64,
        policy_sha=policy.sha256,
        archive_sha=archive.sha256,
    )
    prior = BuilderMetaPrior.from_archive(
        archive=archive,
        policy=policy,
        checkpoint=checkpoint,
        registry=registry,
        target_instance_id="suite:target-001",
    )
    selected = prior.planner_payload()["payload"]["selected_nodes"]
    assert selected[0]["node_sha256"] == node.sha256
    assert set(selected[0]["component_selection"]) == set(COMPONENT_AXES)
    assert selected[0]["source_stream_index"] < prior.target_stream_index


def test_prior_payload_is_deeply_immutable_and_code_diff_is_trusted() -> None:
    prior, policy = _policy_prior()
    assert "code_diff" not in prior.payload["component_candidates"]["tools"]
    full_policy = MetaPolicySnapshot.create(
        policy_id="policy-full-v001",
        registry=TrustedMetaPolicyRegistry.default(),
    )
    checkpoint = _checkpoint(
        TrustedMetaPolicyRegistry.default(),
        memory_sha="b" * 64,
        policy_sha=full_policy.sha256,
        archive_sha="c" * 64,
    )
    full_prior = BuilderMetaPrior.from_policy(
        policy=full_policy,
        checkpoint=checkpoint,
        registry=TrustedMetaPolicyRegistry.default(),
        target_instance_id="suite:target-001",
    )
    assert "code_diff" in full_prior.payload["component_candidates"]["tools"]
    with pytest.raises(TypeError):
        full_prior.payload["component_candidates"]["tools"] = ("task_semantics",)
    assert policy.sha256 == prior.source_snapshot_sha256
