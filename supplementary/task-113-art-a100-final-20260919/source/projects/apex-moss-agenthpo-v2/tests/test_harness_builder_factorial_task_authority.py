from __future__ import annotations

from dataclasses import replace
import hashlib
import json
import os
from pathlib import Path

import pytest

from optimization_lab.harness_builder.factorial_contract import (
    factorial_main_matrix_projection,
    verify_factorial_contract,
)
from optimization_lab.harness_builder.factorial_precheck import (
    FactorialFormalZeroCallPlan,
)
from optimization_lab.harness_builder.factorial_task_authority import (
    FactorialTaskArtifactAuthority,
    FactorialTaskAuthorityError,
)
from optimization_lab.harness_builder.operators import (
    HarnessContext,
    TrustedOperatorRegistry,
)


_AGENT_ROOT = Path(
    os.environ.get(
        "MOSS_TEST_AGENTHPO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/agenthpobench",
    )
)
_GDPEVO_ROOT = Path(
    os.environ.get(
        "MOSS_TEST_GDPEVO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/gdpevo",
    )
)


@pytest.fixture(scope="module")
def authority() -> FactorialTaskArtifactAuthority:
    if not _AGENT_ROOT.is_dir() or not _GDPEVO_ROOT.is_dir():
        pytest.skip("pinned benchmark qualification checkouts are unavailable")
    return FactorialTaskArtifactAuthority(
        agenthpo_checkout=_AGENT_ROOT,
        gdpevo_checkout=_GDPEVO_ROOT,
    )


def test_exact_source_derived_matrix_builds_formal_zero_call_plan(
    authority: FactorialTaskArtifactAuthority,
) -> None:
    contexts = authority.derived_contexts()
    bundle = authority.authorize_exact_matrix(contexts)
    assert type(bundle).from_canonical_bytes(
        bundle.canonical_bytes, expected_sha256=bundle.sha256
    ) == bundle
    verified = verify_factorial_contract()
    expected = factorial_main_matrix_projection(verified)

    assert bundle.execution_authority == "NOT_GRANTED"
    assert bundle.model_call_entitlement == 0
    assert bundle.evaluator_transaction_entitlement == 0
    assert bundle.factorial_contract_sha256 == verified["contract_digest"]
    assert len(bundle.task_seed_keys) == len(expected) == 126
    assert len(bundle.task_artifacts) == len(contexts) == 42
    assert [
        (key.suite, key.instance_id, key.seed) for key in bundle.task_seed_keys
    ] == [
        (item["benchmark_id"], item["instance_id"], item["seed"])
        for item in expected
    ]

    plan = authority.build_formal_zero_call_plan(contexts)
    assert isinstance(plan, FactorialFormalZeroCallPlan)
    assert len(plan.schedules) == 126
    assert plan.execution_authority == "NOT_GRANTED"
    assert plan.execution_entitlement == {
        "cpu_evaluator_seconds": 0,
        "evaluator_transactions": 0,
        "gpu_exclusive_seconds": 0,
        "model_calls": 0,
    }
    assert plan.task_authority_bundle_sha256 == bundle.sha256


def test_formal_plan_and_barrier_cannot_accept_self_consistent_raw_keys(
    authority: FactorialTaskArtifactAuthority,
) -> None:
    bundle = authority.rederive_exact_bundle()
    forged_keys = tuple(
        replace(
            key,
            task_binding_sha256="a" * 64,
            context_binding_sha256="b" * 64,
        )
        for key in bundle.task_seed_keys
    )
    with pytest.raises(
        FactorialTaskAuthorityError, match="source-locked artifact"
    ):
        replace(bundle, task_seed_keys=forged_keys)


def test_authority_rejects_caller_context_and_task_hash_forgery(
    authority: FactorialTaskArtifactAuthority,
) -> None:
    contexts = authority.derived_contexts()
    identity = ("agenthpobench", "hyperboliccv_cifar100_accuracy")
    original = contexts[identity]

    forged_contexts = dict(contexts)
    forged_contexts[identity] = replace(
        original,
        task_card=original.task_card + "\ncaller supplied drift",
    )
    with pytest.raises(FactorialTaskAuthorityError, match="task card differs"):
        authority.authorize_exact_matrix(forged_contexts)

    bundle = authority.authorize_exact_matrix(contexts)
    keys = list(bundle.task_seed_keys)
    keys[0] = replace(
        keys[0],
        task_binding_sha256=hashlib.sha256(b"caller-controlled-task").hexdigest(),
    )
    # Generic plan construction used to accept any self-consistent digest.
    # The source authority never accepts keys, so the only public path is to
    # rerun authorize_exact_matrix and obtain the original mechanical binding.
    replay = authority.authorize_exact_matrix(contexts)
    assert replay.task_seed_keys[0] == bundle.task_seed_keys[0]
    assert replay.task_seed_keys[0] != keys[0]


def test_gdpevo_solver_projection_contains_only_public_input(
    authority: FactorialTaskArtifactAuthority,
) -> None:
    contexts = authority.derived_contexts()
    context = contexts[("gdpevo", "task_group_003:test_1")]
    artifact = next(
        item
        for item in authority.task_artifacts()
        if item.suite == "gdpevo" and item.instance_id == context.instance_id
    )

    lowered = context.task_card.lower()
    assert '"prompt"' in lowered
    assert '"payloads"' in lowered
    assert "ticket_batch.csv" in lowered
    assert "tck-6101" in lowered
    for private_marker in (
        "scoring.json",
        "output/answer.json",
        "notes.md",
        '"rubric"',
        '"weight"',
        '"goal"',
    ):
        assert private_marker not in lowered
    assert context.reference_artifact_id == "answer-template"
    assert "ticket_decisions" in context.reference_artifact
    assert artifact.controller_source_binding_sha256 not in context.task_card
    artifact.verify_context(context)


def test_agenthpo_free_form_fails_closed_and_nullable_space_is_exact(
    authority: FactorialTaskArtifactAuthority,
) -> None:
    contexts = authority.derived_contexts()
    room = contexts[("agenthpobench", "agent_lightning_room_selector")]
    nullable = contexts[("agenthpobench", "binary_diffusion_adult_rf")]

    assert "AGENTHPO_FREE_FORM_PROMPT_TEMPLATE_V1" in room.task_card
    assert "FREE_FORM_CODEC_REQUIRED_FAIL_CLOSED" in room.task_card
    assert "EXACT_ORIGINAL_DISCRETE_SPACE" not in room.task_card
    assert room.reference_artifact_id == "baseline-prompt-template"
    assert "{attendees}" in room.reference_artifact

    assert "AGENTHPO_DISCRETE_HYPERPARAMETER_V1" in nullable.task_card
    assert "STRICT_NULLABLE_DISCRETE_CODEC_DERIVABLE" in nullable.task_card
    assert '"max_depth"' in nullable.task_card
    assert nullable.reference_artifact_id == "baseline-config"


def test_exact_v001_context_has_only_source_derived_capability_and_is_bound(
    authority: FactorialTaskArtifactAuthority,
) -> None:
    contexts = authority.derived_contexts()
    identity = ("agenthpobench", "llm_c_fineweb10b")
    context = contexts[identity]
    bundle = authority.authorize_exact_matrix(contexts)
    key = next(
        item
        for item in bundle.task_seed_keys
        if item.suite == identity[0]
        and item.instance_id == identity[1]
        and item.seed == 2026081201
    )
    assert key.context_binding_sha256 == (
        TrustedOperatorRegistry.context_binding_sha256(context)
    )
    assert set(context.public_observations) == {"artifact_contract"}
    capability = context.public_observations["artifact_contract"]
    assert capability["suite"] == identity[0]
    assert capability["instance_id"] == identity[1]
    assert capability["task_card_sha256"] == hashlib.sha256(
        context.task_card.encode("utf-8")
    ).hexdigest()
    artifact = next(
        item
        for item in bundle.task_artifacts
        if item.suite == identity[0] and item.instance_id == identity[1]
    )
    assert artifact.schema_version == 2
    assert artifact.artifact_contract_sha256 == hashlib.sha256(
        (
            json.dumps(
                capability,
                allow_nan=False,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
    ).hexdigest()

    forged = dict(contexts)
    forged[identity] = HarnessContext(
        **{
            **context.__dict__,
            "public_observations": {
                **context.public_observations,
                "caller": "injected",
            },
        }
    )
    with pytest.raises(
        FactorialTaskAuthorityError, match="artifact contract differs"
    ):
        authority.authorize_exact_matrix(forged)

    forged_capability = dict(context.public_observations["artifact_contract"])
    forged_capability["candidate_kind"] = "CALLER_SELECTED_CODEC"
    forged[identity] = HarnessContext(
        **{
            **context.__dict__,
            "public_observations": {"artifact_contract": forged_capability},
        }
    )
    with pytest.raises(
        FactorialTaskAuthorityError, match="artifact contract differs"
    ):
        authority.authorize_exact_matrix(forged)


def test_incomplete_or_extra_context_coverage_is_rejected(
    authority: FactorialTaskArtifactAuthority,
) -> None:
    contexts = authority.derived_contexts()
    missing = dict(contexts)
    missing.pop(next(iter(missing)))
    with pytest.raises(FactorialTaskAuthorityError, match="coverage differs"):
        authority.authorize_exact_matrix(missing)

    extra = dict(contexts)
    sample = next(iter(contexts.values()))
    extra[("agenthpobench", "unexpected")] = replace(
        sample, instance_id="unexpected"
    )
    with pytest.raises(FactorialTaskAuthorityError, match="coverage differs"):
        authority.authorize_exact_matrix(extra)
