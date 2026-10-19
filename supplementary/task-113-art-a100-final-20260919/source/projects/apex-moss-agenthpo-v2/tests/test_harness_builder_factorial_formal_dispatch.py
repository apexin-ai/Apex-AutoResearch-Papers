from __future__ import annotations

from dataclasses import replace
import inspect
import json
import os
from pathlib import Path

import pytest

import optimization_lab.harness_builder.factorial_formal_dispatch as dispatch_module
from optimization_lab.harness_builder.factorial_formal_dispatch import (
    FactorialV001FormalCompileOrchestrator,
    FactorialV001RuntimeContract,
)
from optimization_lab.harness_builder.factorial_policies import ARM_IDS
from optimization_lab.harness_builder.factorial_precheck import (
    FactorialFormalZeroCallPlan,
)
from optimization_lab.harness_builder.factorial_task_authority import (
    FactorialTaskArtifactAuthority,
)
from optimization_lab.harness_builder.schema import HarnessDecision


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
def exact_inputs():
    if not _AGENT_ROOT.is_dir() or not _GDPEVO_ROOT.is_dir():
        pytest.skip("pinned benchmark qualification checkouts are unavailable")
    authority = FactorialTaskArtifactAuthority(
        agenthpo_checkout=_AGENT_ROOT,
        gdpevo_checkout=_GDPEVO_ROOT,
    )
    bundle = authority.rederive_exact_bundle()
    plan = FactorialFormalZeroCallPlan.from_authority_bundle(
        bundle, task_authority=authority
    )
    return authority, bundle, plan


def _decision() -> HarnessDecision:
    return HarnessDecision.from_dict(
        {
            "schema_version": 1,
            "rule_id": "contract_compatibility",
            "role_graph": ["task_analyst", "generator", "verifier"],
            "memory_views": ["current"],
            "tools": ["task_semantics"],
            "parent_strategy": "reference",
            "workflow": ["analyze", "generate", "verify_contract"],
            "scheduler_mode": "single_candidate",
            "recovery_mode": "repair_then_reset",
            "kernel_directive": "Respect the source-derived public artifact contract.",
        }
    )


def test_trusted_v001_recompile_is_four_arm_semantic_equivalence_and_zero_call(
    exact_inputs,
) -> None:
    authority, bundle, plan = exact_inputs
    orchestrator = FactorialV001FormalCompileOrchestrator(
        task_authority=authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    key = plan.schedules[0].key
    result = orchestrator.compile_shared_v001(key=key, decision=_decision())

    assert result.receipt.execution_authority == "NOT_GRANTED"
    assert result.receipt.execution_entitlement == {
        "cpu_evaluator_seconds": 0,
        "evaluator_transactions": 0,
        "gpu_exclusive_seconds": 0,
        "model_calls": 0,
    }
    assert tuple(arm for arm, _ in result.arm_compile_receipts) == ARM_IDS
    assert len({item.sha256 for _, item in result.arm_compile_receipts}) == 4
    assert set(
        result.compile_equivalence_receipt.arm_compiled_harness_semantic_sha256s.values()
    ) == {result.canonical_compile_contract.compiled_harness_semantic_sha256}
    semantic_evidence = json.loads(
        result.compile_equivalence_receipt.
        canonical_compiled_harness_semantic_canonical_json
    )
    capability = authority.derived_contexts()[
        (key.suite, key.instance_id)
    ].public_observations["artifact_contract"]
    assert (
        semantic_evidence["tool_outputs"]["task_semantics"]["artifact_contract"]
        == capability
    )
    assert orchestrator.runtime_contract.rule_registry_sha256 == (
        dispatch_module.RULE_REGISTRY_V3_SHA256
    )
    assert "provider" not in inspect.signature(
        FactorialV001FormalCompileOrchestrator
    ).parameters
    assert "evaluator" not in inspect.signature(
        FactorialV001FormalCompileOrchestrator
    ).parameters
    assert "provider" not in inspect.signature(
        orchestrator.compile_shared_v001
    ).parameters
    assert "evaluator" not in inspect.signature(
        orchestrator.compile_shared_v001
    ).parameters


def test_compile_rederives_authority_and_rejects_forged_bundle(
    exact_inputs,
) -> None:
    authority, bundle, plan = exact_inputs
    forged = replace(
        bundle,
        agenthpo_source_binding_sha256="f" * 64,
    )
    with pytest.raises(ValueError, match="pinned source derivation"):
        FactorialV001FormalCompileOrchestrator(
            task_authority=authority,
            task_authority_bundle=forged,
            plan=plan,
        )


def test_compile_rejects_key_and_context_drift(exact_inputs) -> None:
    authority, bundle, plan = exact_inputs
    orchestrator = FactorialV001FormalCompileOrchestrator(
        task_authority=authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    key = plan.schedules[0].key
    with pytest.raises(ValueError, match="outside the exact formal factorial plan"):
        orchestrator.compile_shared_v001(
            key=replace(key, seed=key.seed + 999),
            decision=_decision(),
        )

    original = authority.derived_contexts

    def drifted_contexts():
        contexts = original()
        identity = (key.suite, key.instance_id)
        context = contexts[identity]
        capability = dict(context.public_observations["artifact_contract"])
        capability["candidate_kind"] = "CALLER_SELECTED_CODEC"
        contexts[identity] = replace(
            context,
            public_observations={"artifact_contract": capability},
        )
        return contexts

    authority.derived_contexts = drifted_contexts  # type: ignore[method-assign]
    try:
        with pytest.raises(ValueError, match="artifact contract differs"):
            orchestrator.compile_shared_v001(key=key, decision=_decision())
    finally:
        authority.derived_contexts = original  # type: ignore[method-assign]


def test_runtime_contract_rejects_registry_variant_or_manifest_drift(
    exact_inputs,
) -> None:
    authority, bundle, plan = exact_inputs
    orchestrator = FactorialV001FormalCompileOrchestrator(
        task_authority=authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    contract = orchestrator.runtime_contract
    with pytest.raises(
        ValueError,
        match="runtime (?:source contract|Builder semantics) differ(?:s)?",
    ):
        replace(contract, rule_registry_sha256="e" * 64)
    variants = list(contract.builder_variants)
    variants[-1] = replace(variants[-1], allowed_rule_ids=("contract_compatibility",))
    with pytest.raises(ValueError, match="runtime Builder semantics differ"):
        replace(contract, builder_variants=tuple(variants))
    hashes = list(contract.manifest_arm_variant_sha256s)
    hashes[-1] = (hashes[-1][0], "d" * 64)
    with pytest.raises(ValueError, match="runtime source contract differs"):
        replace(contract, manifest_arm_variant_sha256s=tuple(hashes))


def test_registry_byte_drift_fails_before_any_external_callback(
    exact_inputs,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    authority, bundle, plan = exact_inputs
    real_read = dispatch_module.read_safe_regular_file
    calls = {"external": 0}

    def drifted_read(path: Path, *, label: str) -> bytes:
        raw = real_read(path, label=label)
        if path == dispatch_module.DEFAULT_RULE_REGISTRY_V3:
            return raw + b" "
        calls["external"] += 1
        return raw

    monkeypatch.setattr(dispatch_module, "read_safe_regular_file", drifted_read)
    with pytest.raises(ValueError, match="bytes drifted"):
        FactorialV001FormalCompileOrchestrator(
            task_authority=authority,
            task_authority_bundle=bundle,
            plan=plan,
        )
    assert calls["external"] == 0


def test_registry_drift_after_orchestrator_construction_fails_at_compile(
    exact_inputs,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    authority, bundle, plan = exact_inputs
    orchestrator = FactorialV001FormalCompileOrchestrator(
        task_authority=authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    real_read = dispatch_module.read_safe_regular_file

    def drifted_read(path: Path, *, label: str) -> bytes:
        raw = real_read(path, label=label)
        return raw + b" " if path == dispatch_module.DEFAULT_RULE_REGISTRY_V3 else raw

    monkeypatch.setattr(dispatch_module, "read_safe_regular_file", drifted_read)
    with pytest.raises(ValueError, match="bytes drifted"):
        orchestrator.compile_shared_v001(
            key=plan.schedules[0].key, decision=_decision()
        )


def test_runtime_contract_is_not_constructible_from_a_partial_variant(
    exact_inputs,
) -> None:
    authority, bundle, plan = exact_inputs
    orchestrator = FactorialV001FormalCompileOrchestrator(
        task_authority=authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    contract = orchestrator.runtime_contract
    assert isinstance(contract, FactorialV001RuntimeContract)
    with pytest.raises(ValueError, match="coverage or order differs"):
        replace(
            contract,
            manifest_arm_variant_sha256s=contract.manifest_arm_variant_sha256s[:-1],
        )


def test_compile_canonicalizes_directly_constructed_decision(exact_inputs) -> None:
    authority, bundle, plan = exact_inputs
    orchestrator = FactorialV001FormalCompileOrchestrator(
        task_authority=authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    valid = _decision()
    unsafe = HarnessDecision(
        **{
            **valid.__dict__,
            "schema_version": 999,
            "kernel_directive": "read /home/ubuntu/private evaluator\x00",
        }
    )

    with pytest.raises(ValueError, match="schema|unsafe"):
        orchestrator.compile_shared_v001(
            key=plan.schedules[0].key,
            decision=unsafe,
        )


def test_trusted_result_requires_current_source_registry_recompilation(
    exact_inputs,
) -> None:
    authority, bundle, plan = exact_inputs
    orchestrator = FactorialV001FormalCompileOrchestrator(
        task_authority=authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    key = plan.schedules[0].key
    decision = _decision()
    result = orchestrator.compile_shared_v001(key=key, decision=decision)
    forged = replace(
        result,
        receipt=replace(
            result.receipt,
            formal_plan_sha256="e" * 64,
            task_authority_bundle_sha256="f" * 64,
        ),
    )

    with pytest.raises(ValueError, match="trusted recompilation"):
        orchestrator.verify_trusted_result(
            key=key,
            decision=decision,
            candidate=forged,
        )
    assert (
        orchestrator.verify_trusted_result(
            key=key,
            decision=decision,
            candidate=result,
        )
        == result
    )


def test_structurally_self_rehashed_result_is_not_provenance(exact_inputs) -> None:
    authority, bundle, plan = exact_inputs
    orchestrator = FactorialV001FormalCompileOrchestrator(
        task_authority=authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    key = plan.schedules[0].key
    decision = _decision()
    result = orchestrator.compile_shared_v001(key=key, decision=decision)

    # This replacement is internally well formed and rehashes its changed
    # child into the outer receipt.  Structural DTO checks cannot establish
    # that the new plan digest came from the current pinned trust roots.
    forged_receipt = replace(result.receipt, formal_plan_sha256="e" * 64)
    forged = replace(result, receipt=forged_receipt)
    assert forged.receipt.sha256 != result.receipt.sha256

    with pytest.raises(ValueError, match="trusted recompilation"):
        orchestrator.verify_trusted_result(
            key=key,
            decision=decision,
            candidate=forged,
        )
