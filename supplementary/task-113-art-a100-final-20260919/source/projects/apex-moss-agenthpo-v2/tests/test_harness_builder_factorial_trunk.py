from __future__ import annotations

import hashlib
import json
import os
from dataclasses import replace
from pathlib import Path

import pytest

from optimization_lab.harness_builder.factorial_trunk import (
    FACTORIAL_ARMS,
    ZERO_SHA256,
    FactorialTrunkArchive,
    TaskSeedKey,
    V001ArmForkReceipt,
    V001CanonicalCompileContract,
    V001CompileEquivalenceReceipt,
    V001TrunkIntent,
    V001TrunkReceipt,
    compiled_harness_semantic_sha256,
)
from optimization_lab.harness_builder.compile_receipts import HarnessCompileReceipt
from optimization_lab.harness_builder.operators import (
    CompiledHarness,
    HarnessContext,
    TrustedOperatorRegistry,
)
from optimization_lab.harness_builder.schema import BuilderVariant, HarnessDecision


def _sha(label: str) -> str:
    return hashlib.sha256(label.encode()).hexdigest()


def _context() -> HarnessContext:
    return HarnessContext(
        instance_id="agenthpobench:task-01",
        suite="agenthpobench",
        round_index=1,
        task_card="Optimize the frozen public task.",
        reference_artifact_id="reference",
        reference_artifact="reference artifact",
        public_observations={
            "artifact_contract": {"schema_version": 1, "kind": "public"}
        },
    )


def _key() -> TaskSeedKey:
    return TaskSeedKey(
        suite="agenthpobench",
        instance_id="agenthpobench:task-01",
        seed=2026081201,
        task_binding_sha256=_sha("task"),
        factorial_contract_sha256=_sha("factorial"),
        context_binding_sha256=TrustedOperatorRegistry.context_binding_sha256(
            _context()
        ),
    )


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
            "kernel_directive": "Respect the frozen public contract.",
        }
    )


def _compiled(*, policy: str = "conditional_any_v1", prompt: str = "solve") -> CompiledHarness:
    decision = _decision()
    variant = BuilderVariant(
        variant_id="fixture",
        description="shared v001 fixture",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("contract_compatibility",),
        experience_sources=(),
        excluded_task_ids=(),
        adaptation_policy=policy,
    )
    compiled = TrustedOperatorRegistry(rule_registry_sha256="a" * 64).compile(
        decision,
        variant=variant,
        context=_context(),
    )
    return compiled if prompt == compiled.solution_prompt else replace(
        compiled, solution_prompt=prompt
    )


def _arm_compilations() -> dict[str, CompiledHarness]:
    return {
        arm: _compiled(
            policy={
                "A-fixed-feedback": "conditional_any_v1",
                "S-reflection-skill": "conditional_any_v1",
                "B-targeted": "targeted_any_change_v1",
                "B-frozen-wide": "wide_all_fields_recompile_v1",
            }[arm]
        )
        for arm in FACTORIAL_ARMS
    }


def _arm_compile_receipts(
    key: TaskSeedKey,
    decision: HarnessDecision,
    arm_compiled: dict[str, CompiledHarness],
) -> dict[str, HarnessCompileReceipt]:
    return {
        arm: HarnessCompileReceipt.create(
            cell_id=key.arm_cell_id(arm),
            suite=key.suite,
            instance_id=key.instance_id,
            variant_id=arm,
            version="v001",
            adaptation_policy=compiled.adaptation_policy,
            previous_receipt_sha256=ZERO_SHA256,
            previous_decision_sha256=ZERO_SHA256,
            compiled=compiled,
            decision=decision,
        )
        for arm, compiled in arm_compiled.items()
    }


def _contracts():
    key = _key()
    intent = V001TrunkIntent.create(key)
    decision = _decision()
    canonical_compiled = _compiled()
    arm_compiled = _arm_compilations()
    arm_compile_receipts = _arm_compile_receipts(key, decision, arm_compiled)
    contract = V001CanonicalCompileContract.create(key, decision, canonical_compiled)
    equivalence = V001CompileEquivalenceReceipt.create(
        key=key,
        decision=decision,
        canonical_compiled=canonical_compiled,
        arm_compiled=arm_compiled,
        arm_compile_receipts=arm_compile_receipts,
    )
    trunk = V001TrunkReceipt.create(
        intent=intent,
        trunk_status="SUCCESS",
        canonical_compile_contract=contract,
        compile_equivalence_receipt=equivalence,
        solution_artifact_sha256=_sha("solution"),
        attempt_artifact_sha256=_sha("attempt"),
        evaluation_artifact_sha256=_sha("evaluation"),
    )
    return key, intent, contract, equivalence, trunk, arm_compile_receipts


def _populate(
    archive: FactorialTrunkArchive,
    *,
    arm_variant_sha256s: dict[str, str] | None = None,
    arm_contract_sha256: str | None = None,
):
    key, intent, contract, equivalence, trunk, arm_receipts = _contracts()
    variants = arm_variant_sha256s or {
        arm: _sha(f"variant:{arm}") for arm in FACTORIAL_ARMS
    }
    bound_contract = arm_contract_sha256 or _sha("factorial")
    archive.store_intent(intent)
    archive.store_canonical_compile(key, contract)
    archive.store_equivalence(key, equivalence)
    archive.store_trunk(trunk)
    forks = {}
    for arm in FACTORIAL_ARMS:
        fork = V001ArmForkReceipt.create(
            key=key,
            trunk=trunk,
            arm_id=arm,
            arm_variant_sha256=variants[arm],
            arm_contract_sha256=bound_contract,
            arm_compile_receipt_sha256=arm_receipts[arm].sha256,
        )
        archive.store_fork(fork)
        forks[arm] = fork
    return key, intent, contract, equivalence, trunk, forks


@pytest.mark.parametrize("field", ("arm_variant_sha256", "arm_contract_sha256"))
def test_formal_bound_archive_rejects_arbitrary_nonzero_fork_digest_on_store(
    tmp_path: Path,
    field: str,
) -> None:
    variants = {arm: _sha(f"formal-variant:{arm}") for arm in FACTORIAL_ARMS}
    archive = FactorialTrunkArchive(
        tmp_path / "archive",
        expected_factorial_contract_sha256=_sha("factorial"),
        expected_arm_variant_sha256s=variants,
    )
    key, intent, contract, equivalence, trunk, arm_receipts = _contracts()
    archive.store_intent(intent)
    archive.store_canonical_compile(key, contract)
    archive.store_equivalence(key, equivalence)
    archive.store_trunk(trunk)
    kwargs = {
        "arm_variant_sha256": variants[FACTORIAL_ARMS[0]],
        "arm_contract_sha256": key.factorial_contract_sha256,
    }
    kwargs[field] = _sha(f"arbitrary-nonzero:{field}")
    fork = V001ArmForkReceipt.create(
        key=key,
        trunk=trunk,
        arm_id=FACTORIAL_ARMS[0],
        arm_compile_receipt_sha256=arm_receipts[FACTORIAL_ARMS[0]].sha256,
        **kwargs,
    )
    with pytest.raises(ValueError, match="fork variant/contract binding differs"):
        archive.store_fork(fork)


@pytest.mark.parametrize("field", ("arm_variant_sha256", "arm_contract_sha256"))
def test_formal_bound_archive_rejects_fully_rehashed_fork_digest_on_load(
    tmp_path: Path,
    field: str,
) -> None:
    variants = {arm: _sha(f"formal-variant:{arm}") for arm in FACTORIAL_ARMS}
    archive = FactorialTrunkArchive(
        tmp_path / "archive",
        expected_factorial_contract_sha256=_sha("factorial"),
        expected_arm_variant_sha256s=variants,
    )
    key, _intent, _contract, _equivalence, _trunk, forks = _populate(
        archive,
        arm_variant_sha256s=variants,
        arm_contract_sha256=_sha("factorial"),
    )
    assert key.factorial_contract_sha256 == _sha("factorial")
    arm_id = FACTORIAL_ARMS[0]
    payload = json.loads(forks[arm_id].canonical_bytes)
    payload[field] = _sha(f"fully-rehashed-arbitrary:{field}")
    forged = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    forged_sha = hashlib.sha256(forged).hexdigest()
    object_path = archive.root / "objects" / "forks" / f"{forged_sha}.json"
    object_path.write_bytes(forged)
    binding_path = archive.root / "bindings" / "forks" / key.sha256 / f"{arm_id}.json"
    binding = json.loads(binding_path.read_bytes())
    binding["object_sha256"] = forged_sha
    binding_path.write_bytes(
        (json.dumps(binding, sort_keys=True, separators=(",", ":")) + "\n").encode()
    )
    with pytest.raises(ValueError, match="fork variant/contract binding differs"):
        archive.load_fork(key.sha256, arm_id)


def test_task_seed_key_binds_complete_identity_and_deterministic_operations() -> None:
    key = _key()
    assert TaskSeedKey.from_bytes(key.canonical_bytes, expected_sha256=key.sha256) == key
    assert key.operation_id("builder") != key.operation_id("solution")
    assert key.arm_cell_id(FACTORIAL_ARMS[0]).endswith(FACTORIAL_ARMS[0])
    assert replace(key, context_binding_sha256=_sha("other")).sha256 != key.sha256
    with pytest.raises(ValueError, match="uint64"):
        replace(key, seed=-1)
    with pytest.raises(ValueError, match="uint64"):
        replace(key, seed=1 << 64)
    with pytest.raises(ValueError, match="uint64"):
        replace(key, seed=True)


def test_task_seed_key_factory_revalidates_typed_v001_context_and_source() -> None:
    context = _context()
    key = TaskSeedKey.create(
        context=context,
        seed=2026081201,
        task_binding_sha256=_sha("task"),
        factorial_contract_sha256=_sha("factorial"),
    )
    assert key == _key()
    key.verify_against_context(
        context=context,
        seed=2026081201,
        task_binding_sha256=_sha("task"),
        factorial_contract_sha256=_sha("factorial"),
    )
    with pytest.raises(ValueError, match="context binding differs"):
        key.verify_against_context(
            context=replace(context, task_card="different public task"),
            seed=2026081201,
            task_binding_sha256=_sha("task"),
            factorial_contract_sha256=_sha("factorial"),
        )
    with pytest.raises(ValueError, match="context binding differs"):
        key.verify_against_context(
            context=context,
            seed=2026081201,
            task_binding_sha256=_sha("different-task-source"),
            factorial_contract_sha256=_sha("factorial"),
        )
    with pytest.raises(ValueError, match="context binding differs"):
        key.verify_against_context(
            context=context,
            seed=2026081202,
            task_binding_sha256=_sha("task"),
            factorial_contract_sha256=_sha("factorial"),
        )
    with pytest.raises(ValueError, match="empty factorial trunk task binding"):
        TaskSeedKey.create(
            context=context,
            seed=key.seed,
            task_binding_sha256=ZERO_SHA256,
            factorial_contract_sha256=_sha("factorial"),
        )
    with pytest.raises(ValueError, match="requires a v001 context"):
        TaskSeedKey.create(
            context=replace(context, round_index=2),
            seed=key.seed,
            task_binding_sha256=_sha("task"),
            factorial_contract_sha256=_sha("factorial"),
        )


def test_intent_rejects_non_deterministic_operation_id() -> None:
    intent = V001TrunkIntent.create(_key())
    with pytest.raises(ValueError, match="operation ids"):
        replace(intent, evaluator_operation_id="different")


def test_semantic_projection_excludes_only_policy_and_hashes_prompt() -> None:
    baseline = _compiled()
    wide = replace(baseline, adaptation_policy="wide_all_fields_recompile_v1")
    changed_prompt = replace(baseline, solution_prompt="different prompt")
    changed_memory = replace(baseline, memory={"current": ({"round": 1},)})
    assert compiled_harness_semantic_sha256(baseline) == compiled_harness_semantic_sha256(wide)
    assert compiled_harness_semantic_sha256(baseline) != compiled_harness_semantic_sha256(changed_prompt)
    assert compiled_harness_semantic_sha256(baseline) != compiled_harness_semantic_sha256(changed_memory)
    assert "solve" not in V001CanonicalCompileContract.create(
        _key(), _decision(), baseline
    ).canonical_bytes.decode()


def test_canonical_compile_rejects_decision_or_fingerprint_mismatch() -> None:
    with pytest.raises(ValueError, match="decision binding"):
        V001CanonicalCompileContract.create(
            _key(), _decision(), replace(_compiled(), decision_sha256=_sha("wrong"))
        )
    with pytest.raises(ValueError, match="fingerprint"):
        V001CanonicalCompileContract.create(
            _key(),
            _decision(),
            replace(_compiled(), operational_fingerprint=_sha("wrong")),
        )


def test_equivalence_requires_all_four_arm_compiles_and_five_way_identity() -> None:
    key = _key()
    decision = _decision()
    compiled = _compiled()
    arm_compiled = _arm_compilations()
    receipts = _arm_compile_receipts(key, decision, arm_compiled)
    receipt = V001CompileEquivalenceReceipt.create(
        key=key,
        decision=decision,
        canonical_compiled=compiled,
        arm_compiled=arm_compiled,
        arm_compile_receipts=receipts,
    )
    assert set(receipt.arm_compiled_harness_semantic_sha256s.values()) == {
        receipt.canonical_compiled_harness_semantic_sha256
    }
    arm_compiled["B-targeted"] = replace(
        arm_compiled["B-targeted"], scheduler_phase="explore"
    )
    with pytest.raises(ValueError, match="semantics differ"):
        V001CompileEquivalenceReceipt.create(
            key=key,
            decision=decision,
            canonical_compiled=compiled,
            arm_compiled=arm_compiled,
            arm_compile_receipts=receipts,
        )
    with pytest.raises(ValueError, match="coverage"):
        V001CompileEquivalenceReceipt.create(
            key=key,
            decision=decision,
            canonical_compiled=compiled,
            arm_compiled={arm: arm_compiled[arm] for arm in FACTORIAL_ARMS[:-1]},
            arm_compile_receipts=receipts,
        )


def test_equivalence_rejects_arbitrary_or_rebound_typed_compile_receipt() -> None:
    key = _key()
    decision = _decision()
    compiled = _arm_compilations()
    receipts = _arm_compile_receipts(key, decision, compiled)
    with pytest.raises(TypeError, match="typed arm compile receipt"):
        V001CompileEquivalenceReceipt.create(
            key=key,
            decision=decision,
            canonical_compiled=_compiled(),
            arm_compiled=compiled,
            arm_compile_receipts={
                **receipts,
                "A-fixed-feedback": _sha("arbitrary caller hash"),
            },
        )
    rebound = replace(receipts["B-targeted"], variant_id="A-fixed-feedback")
    with pytest.raises(ValueError, match="differs from trusted compilation"):
        V001CompileEquivalenceReceipt.create(
            key=key,
            decision=decision,
            canonical_compiled=_compiled(),
            arm_compiled=compiled,
            arm_compile_receipts={**receipts, "B-targeted": rebound},
        )


def test_equivalence_mappings_are_immutable_and_round_trip_canonically() -> None:
    _key_value, _intent, _contract, receipt, _trunk, _receipts = _contracts()
    encoded = receipt.canonical_bytes
    restored = V001CompileEquivalenceReceipt.from_bytes(
        encoded, expected_sha256=receipt.sha256
    )
    assert restored == receipt
    assert restored.canonical_bytes == encoded
    with pytest.raises(TypeError):
        restored.arm_compile_receipt_sha256s[FACTORIAL_ARMS[0]] = _sha("mutate")
    with pytest.raises(TypeError):
        restored.arm_compile_receipt_canonical_jsons[FACTORIAL_ARMS[0]] = "{}\n"


def _forge_embedded_compile_receipt_field(
    equivalence: V001CompileEquivalenceReceipt,
    *,
    arm_id: str,
    field: str,
    value: object,
) -> bytes:
    outer = json.loads(equivalence.canonical_bytes)
    embedded = json.loads(outer["arm_compile_receipt_canonical_jsons"][arm_id])
    embedded[field] = value
    embedded_bytes = (
        json.dumps(embedded, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    outer["arm_compile_receipt_canonical_jsons"][arm_id] = embedded_bytes.decode()
    outer["arm_compile_receipt_sha256s"][arm_id] = hashlib.sha256(
        embedded_bytes
    ).hexdigest()
    return (json.dumps(outer, sort_keys=True, separators=(",", ":")) + "\n").encode()


@pytest.mark.parametrize(
    "field",
    (
        "memory_sha256",
        "tool_outputs_sha256",
        "workflow_sha256",
        "scheduler_sha256",
        "axis_effect_sha256s",
        "selected_parent_ids",
    ),
)
def test_equivalence_rejects_fully_rehashed_embedded_receipt_semantic_forgery(
    field: str,
) -> None:
    _key_value, _intent, _contract, equivalence, _trunk, _receipts = _contracts()
    arm_id = "A-fixed-feedback"
    value: object = _sha(f"forged:{field}")
    if field == "axis_effect_sha256s":
        embedded = json.loads(
            equivalence.arm_compile_receipt_canonical_jsons[arm_id]
        )
        value = {**embedded[field], "role_graph": _sha("forged:role-effect")}
    elif field == "selected_parent_ids":
        value = ["forged-parent"]
    forged = _forge_embedded_compile_receipt_field(
        equivalence,
        arm_id=arm_id,
        field=field,
        value=value,
    )
    with pytest.raises(ValueError, match="semantic projection differs"):
        V001CompileEquivalenceReceipt.from_bytes(
            forged,
            expected_sha256=hashlib.sha256(forged).hexdigest(),
        )


def test_archive_store_rejects_rehashed_embedded_receipt_semantic_forgery(
    tmp_path: Path,
) -> None:
    key, intent, contract, equivalence, _trunk, _receipts = _contracts()
    archive = FactorialTrunkArchive(tmp_path / "archive")
    archive.store_intent(intent)
    archive.store_canonical_compile(key, contract)
    forged_bytes = _forge_embedded_compile_receipt_field(
        equivalence,
        arm_id="A-fixed-feedback",
        field="memory_sha256",
        value=_sha("forged-memory"),
    )
    forged_payload = json.loads(forged_bytes)
    object.__setattr__(
        equivalence,
        "arm_compile_receipt_canonical_jsons",
        forged_payload["arm_compile_receipt_canonical_jsons"],
    )
    object.__setattr__(
        equivalence,
        "arm_compile_receipt_sha256s",
        forged_payload["arm_compile_receipt_sha256s"],
    )
    with pytest.raises(ValueError, match="semantic projection differs"):
        archive.store_equivalence(key, equivalence)


def test_archive_load_rejects_rehashed_embedded_receipt_semantic_forgery(
    tmp_path: Path,
) -> None:
    archive = FactorialTrunkArchive(tmp_path / "archive")
    key, _intent, _contract, equivalence, _trunk, _forks = _populate(archive)
    forged_bytes = _forge_embedded_compile_receipt_field(
        equivalence,
        arm_id="A-fixed-feedback",
        field="memory_sha256",
        value=_sha("forged-memory"),
    )
    forged_sha = hashlib.sha256(forged_bytes).hexdigest()
    forged_path = archive.root / "objects" / "equivalence" / f"{forged_sha}.json"
    forged_path.write_bytes(forged_bytes)
    binding_path = archive.root / "bindings" / "equivalence" / f"{key.sha256}.json"
    binding = json.loads(binding_path.read_bytes())
    binding["object_sha256"] = forged_sha
    binding_path.write_bytes(
        (json.dumps(binding, sort_keys=True, separators=(",", ":")) + "\n").encode()
    )
    with pytest.raises(ValueError, match="semantic projection differs"):
        archive.load_equivalence(key.sha256)


@pytest.mark.parametrize(
    ("status", "kwargs"),
    (
        (
            "SOLUTION_CONTRACT_REJECTED",
            {
                "solution_artifact_sha256": _sha("rejected-solution"),
                "attempt_artifact_sha256": _sha("rejected-attempt"),
            },
        ),
        ("OPERATION_INTERRUPTED", {}),
        ("COMMON_TRUNK_FAILURE", {}),
        ("ENVIRONMENT_INVALID", {}),
    ),
)
def test_trunk_supports_explicit_terminal_statuses(status: str, kwargs: dict[str, str]) -> None:
    key, intent, contract, equivalence, _trunk, _receipts = _contracts()
    compile_kwargs = (
        {}
        if status == "ENVIRONMENT_INVALID"
        else {
            "canonical_compile_contract": contract,
            "compile_equivalence_receipt": equivalence,
        }
    )
    receipt = V001TrunkReceipt.create(
        intent=intent, trunk_status=status, **compile_kwargs, **kwargs
    )
    assert receipt.trunk_status == status
    if status == "ENVIRONMENT_INVALID":
        with pytest.raises(ValueError, match="cannot fork"):
            V001ArmForkReceipt.create(
                key=key,
                trunk=receipt,
                arm_id=FACTORIAL_ARMS[0],
                arm_variant_sha256=_sha("variant"),
                arm_contract_sha256=_sha("contract"),
                arm_compile_receipt_sha256=_sha("compile"),
            )


def test_success_requires_all_common_artifacts() -> None:
    _key_value, intent, contract, equivalence, _trunk, _receipts = _contracts()
    with pytest.raises(ValueError, match="terminal artifacts differ"):
        V001TrunkReceipt.create(
            intent=intent,
            trunk_status="SUCCESS",
            canonical_compile_contract=contract,
            compile_equivalence_receipt=equivalence,
            solution_artifact_sha256=_sha("solution"),
            attempt_artifact_sha256=_sha("attempt"),
        )


def test_four_forks_are_distinct_but_share_exact_trunk_artifacts(tmp_path: Path) -> None:
    key, _intent, _contract, _equivalence, trunk, forks = _populate(
        FactorialTrunkArchive(tmp_path / "archive")
    )
    assert len({fork.sha256 for fork in forks.values()}) == 4
    shared = {
        (
            fork.shared_decision_sha256,
            fork.shared_operational_fingerprint,
            fork.shared_compiled_harness_semantic_sha256,
            fork.shared_solution_prompt_sha256,
            fork.shared_solution_artifact_sha256,
            fork.shared_attempt_artifact_sha256,
            fork.shared_evaluation_artifact_sha256,
        )
        for fork in forks.values()
    }
    assert len(shared) == 1
    assert next(iter(shared))[0] == trunk.decision_sha256
    assert all(fork.arm_cell_id == key.arm_cell_id(arm) for arm, fork in forks.items())


def test_archive_round_trip_fully_revalidates_every_parent(tmp_path: Path) -> None:
    archive = FactorialTrunkArchive(tmp_path / "archive")
    key, intent, contract, equivalence, trunk, forks = _populate(archive)
    assert archive.load_intent(key.sha256) == intent
    assert archive.load_canonical_compile(key.sha256) == contract
    assert archive.load_equivalence(key.sha256) == equivalence
    assert archive.load_trunk(key.sha256) == trunk
    assert archive.load_fork(key.sha256, FACTORIAL_ARMS[-1]) == forks[FACTORIAL_ARMS[-1]]


def test_archive_rejects_canonical_compile_for_another_task_seed(
    tmp_path: Path,
) -> None:
    archive = FactorialTrunkArchive(tmp_path / "archive")
    key = _key()
    archive.store_intent(V001TrunkIntent.create(key))
    other = replace(key, seed=key.seed + 1)
    other_contract = V001CanonicalCompileContract.create(
        other, _decision(), _compiled()
    )
    with pytest.raises(ValueError, match="canonical compile task/seed identity"):
        archive.store_canonical_compile(key, other_contract)


def test_archive_is_write_once_for_task_seed_identity(tmp_path: Path) -> None:
    archive = FactorialTrunkArchive(tmp_path / "archive")
    key = _key()
    first = V001TrunkIntent.create(key)
    archive.store_intent(first)
    changed_key = replace(key, context_binding_sha256=_sha("changed-context"))
    forged = replace(
        V001TrunkIntent.create(changed_key),
        task_seed_key_sha256=key.sha256,
        suite=key.suite,
        instance_id=key.instance_id,
        seed=key.seed,
        task_binding_sha256=key.task_binding_sha256,
        factorial_contract_sha256=key.factorial_contract_sha256,
        context_binding_sha256=key.context_binding_sha256,
        builder_operation_id=key.operation_id("builder"),
        solution_operation_id=key.operation_id("solution"),
        evaluator_operation_id=key.operation_id("evaluator"),
    )
    # The replacement normalizes back to the same semantic identity.
    assert forged == first
    assert archive.store_intent(first) == archive.store_intent(forged)


def test_from_bytes_rejects_tamper_wrong_hash_and_noncanonical_json() -> None:
    key = _key()
    payload = json.loads(key.canonical_bytes)
    payload["seed"] += 1
    tampered = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with pytest.raises(ValueError, match="hash differs"):
        TaskSeedKey.from_bytes(tampered, expected_sha256=key.sha256)
    noncanonical = json.dumps(json.loads(key.canonical_bytes), indent=2).encode()
    with pytest.raises(ValueError, match="not canonical"):
        TaskSeedKey.from_bytes(
            noncanonical, expected_sha256=hashlib.sha256(noncanonical).hexdigest()
        )
    duplicate = key.canonical_bytes.replace(b'{"', b'{"suite":"evil","', 1)
    with pytest.raises(ValueError, match="repeats field"):
        TaskSeedKey.from_bytes(
            duplicate, expected_sha256=hashlib.sha256(duplicate).hexdigest()
        )


def test_archive_detects_object_tampering_even_when_binding_is_unchanged(tmp_path: Path) -> None:
    archive = FactorialTrunkArchive(tmp_path / "archive")
    key, _intent, _contract, _equivalence, trunk, _forks = _populate(archive)
    path = archive.root / "objects" / "trunks" / f"{trunk.sha256}.json"
    payload = json.loads(path.read_bytes())
    payload["evaluation_artifact_sha256"] = _sha("tampered-evaluation")
    path.write_bytes((json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode())
    with pytest.raises(ValueError, match="hash differs"):
        archive.load_trunk(key.sha256)


def test_archive_rejects_symlink_target_and_symlink_parent(tmp_path: Path) -> None:
    key, intent, _contract, _equivalence, _trunk, _receipts = _contracts()
    target_archive = FactorialTrunkArchive(tmp_path / "target-archive")
    target = tmp_path / "outside.json"
    target.write_text("outside", encoding="utf-8")
    binding = (
        target_archive.root
        / "bindings"
        / "intents"
        / f"{key.sha256}.json"
    )
    binding.parent.mkdir(parents=True)
    binding.symlink_to(target)
    with pytest.raises(ValueError, match="unsafe"):
        target_archive.store_intent(intent)
    assert target.read_text(encoding="utf-8") == "outside"

    parent_archive = FactorialTrunkArchive(tmp_path / "parent-archive")
    outside_dir = tmp_path / "outside-dir"
    outside_dir.mkdir()
    (parent_archive.root / "objects").mkdir(parents=True)
    os.symlink(outside_dir, parent_archive.root / "objects" / "intents")
    with pytest.raises(ValueError, match="unsafe"):
        parent_archive.store_intent(intent)
    assert list(outside_dir.iterdir()) == []


def test_archive_revalidates_compile_receipt_binding_on_fork_load(tmp_path: Path) -> None:
    archive = FactorialTrunkArchive(tmp_path / "archive")
    key, _intent, _contract, _equivalence, _trunk, forks = _populate(archive)
    arm = FACTORIAL_ARMS[0]
    fork = forks[arm]
    object_path = archive.root / "objects" / "forks" / f"{fork.sha256}.json"
    payload = json.loads(object_path.read_bytes())
    payload["arm_compile_receipt_sha256"] = _sha("forged-compile-receipt")
    forged_bytes = (
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    forged_sha = hashlib.sha256(forged_bytes).hexdigest()
    forged_path = archive.root / "objects" / "forks" / f"{forged_sha}.json"
    forged_path.write_bytes(forged_bytes)
    binding_path = archive.root / "bindings" / "forks" / key.sha256 / f"{arm}.json"
    binding = json.loads(binding_path.read_bytes())
    binding["object_sha256"] = forged_sha
    binding_path.write_bytes(
        (json.dumps(binding, sort_keys=True, separators=(",", ":")) + "\n").encode()
    )
    with pytest.raises(ValueError, match="compile receipt binding"):
        archive.load_fork(key.sha256, arm)


def test_zero_sha_constant_is_exact_digest_width() -> None:
    assert ZERO_SHA256 == "0" * 64
