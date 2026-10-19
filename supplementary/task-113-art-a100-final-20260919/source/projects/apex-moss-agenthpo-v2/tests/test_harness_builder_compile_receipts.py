from __future__ import annotations

import hashlib
import json
from dataclasses import replace

import pytest

from optimization_lab.harness_builder.compile_receipts import (
    CompileReceiptArchive,
    HarnessCompileReceipt,
)
from optimization_lab.harness_builder.operators import (
    HarnessContext,
    PublicAttempt,
    TrustedOperatorRegistry,
)
from optimization_lab.harness_builder.schema import BuilderVariant, HarnessDecision


def _variant() -> BuilderVariant:
    return BuilderVariant(
        variant_id="B-frozen-wide",
        description="fixture",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("discipline",),
        experience_sources=(),
        excluded_task_ids=(),
        adaptation_policy="wide_all_fields_recompile_v1",
    )


def _targeted_variant() -> BuilderVariant:
    return BuilderVariant(
        variant_id="B-targeted",
        description="targeted fixture",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("discipline",),
        experience_sources=(),
        excluded_task_ids=(),
        adaptation_policy="targeted_any_change_v1",
    )


def _conditional_variant() -> BuilderVariant:
    return BuilderVariant(
        variant_id="conditional-fixture",
        description="conditional fixture",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("discipline",),
        experience_sources=(),
        excluded_task_ids=(),
        adaptation_policy="conditional_any_v1",
    )


def _decision(second: bool = False) -> HarnessDecision:
    return HarnessDecision.from_dict(
        {
            "schema_version": 1,
            "rule_id": "discipline",
            "role_graph": (
                ["task_analyst", "critic", "generator", "verifier"]
                if second
                else ["task_analyst", "generator", "verifier"]
            ),
            "memory_views": ["current", "failures"] if second else ["current", "best"],
            "tools": ["task_semantics", "code_diff"] if second else ["task_semantics", "score_history"],
            "parent_strategy": "incumbent" if second else "reference",
            "workflow": (
                ["analyze", "criticize", "generate", "verify_contract"]
                if second
                else ["analyze", "generate", "verify_contract"]
            ),
            "scheduler_mode": "repair_first" if second else "single_candidate",
            "recovery_mode": "repair_then_reset" if second else "preserve_failure",
            "kernel_directive": "build a valid candidate",
        }
    )


def _third_decision() -> HarnessDecision:
    return HarnessDecision.from_dict(
        {
            "schema_version": 1,
            "rule_id": "discipline",
            "role_graph": ["compiler_analyst", "critic", "generator", "verifier"],
            "memory_views": ["best", "structural_diverse"],
            "tools": ["compiler_observation", "score_history"],
            "parent_strategy": "stable_best",
            "workflow": ["hypothesize", "criticize", "generate", "verify_contract"],
            "scheduler_mode": "explore_then_exploit",
            "recovery_mode": "reset_immediately",
            "kernel_directive": "build a third valid candidate",
        }
    )


def _role_only_decision() -> HarnessDecision:
    return HarnessDecision.from_dict(
        {
            "schema_version": 1,
            "rule_id": "discipline",
            "role_graph": ["task_analyst", "critic", "generator", "verifier"],
            "memory_views": ["current", "best"],
            "tools": ["task_semantics", "score_history"],
            "parent_strategy": "reference",
            "workflow": ["analyze", "generate", "verify_contract"],
            "scheduler_mode": "single_candidate",
            "recovery_mode": "preserve_failure",
            "kernel_directive": "build a role-only candidate",
        }
    )


def _context() -> HarnessContext:
    return HarnessContext(
        instance_id="suite:task",
        suite="suite",
        round_index=2,
        task_card="One task card.",
        reference_artifact_id="reference",
        reference_artifact="reference artifact",
        attempts=(
            PublicAttempt(
                attempt_id="v001",
                artifact_sha256="1" * 64,
                artifact_text="first artifact",
                correct=True,
                score=1.0,
                outcome="valid",
                structural_signature="family-a",
                public_summary="score 1",
            ),
        ),
    )


def _prefix() -> tuple[str, ...]:
    return (_decision(False).operational_fingerprint,)


def _store_initial(
    archive: CompileReceiptArchive,
    registry: TrustedOperatorRegistry,
) -> HarnessCompileReceipt:
    decision = _decision(False)
    context = HarnessContext(
        **{**_context().__dict__, "round_index": 1, "attempts": ()}
    )
    compiled = registry.compile(decision, variant=_variant(), context=context)
    receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v001",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256="0" * 64,
        previous_decision_sha256="0" * 64,
        compiled=compiled,
        decision=decision,
    )
    archive.store_version(receipt=receipt, decision=decision, fixture_only=True)
    return receipt


def test_compile_receipt_is_content_addressed_chained_and_replayable(tmp_path) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    archive = CompileReceiptArchive(tmp_path)
    initial_receipt = _store_initial(archive, registry)
    compiled = registry.compile(
        _decision(True),
        variant=_variant(),
        context=_context(),
        previous_decision=_decision(False),
        prior_operational_fingerprints=_prefix(),
    )
    receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v002",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256=initial_receipt.sha256,
        previous_decision_sha256=_decision(False).sha256,
        compiled=compiled,
        decision=_decision(True),
        previous_decision=_decision(False),
        prior_operational_fingerprints=_prefix(),
    )

    path = archive.store(receipt)
    index_path = archive.store_version(
        receipt=receipt, decision=_decision(True), fixture_only=True
    )
    assert path.name == f"{receipt.sha256}.json"
    assert archive.load(receipt.sha256) == receipt
    assert index_path.name == "v002.json"
    assert archive.load_version(
        "v002",
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
    ) == (receipt, _decision(True))
    assert all(receipt.change_map.values())
    assert receipt.component_catalog_sha256 == compiled.component_catalog_sha256
    assert all(
        receipt.axis_configuration_sha256s[axis]
        != initial_receipt.axis_configuration_sha256s[axis]
        for axis in receipt.axis_configuration_sha256s
    )
    forged_configurations = dict(receipt.axis_configuration_sha256s)
    forged_configurations["tools"] = initial_receipt.axis_configuration_sha256s[
        "tools"
    ]
    forged = replace(
        receipt, axis_configuration_sha256s=forged_configurations
    )
    with pytest.raises(ValueError, match="axis configurations unchanged"):
        archive.store_version(
            receipt=forged, decision=_decision(True), fixture_only=True
        )


def test_compile_receipt_archive_rejects_tamper_and_index_rebind(tmp_path) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    compiled = registry.compile(
        _decision(True),
        variant=_variant(),
        context=_context(),
        previous_decision=_decision(False),
        prior_operational_fingerprints=_prefix(),
    )
    archive = CompileReceiptArchive(tmp_path)
    receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v002",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256="0" * 64,
        previous_decision_sha256=_decision(False).sha256,
        compiled=compiled,
        decision=_decision(True),
        previous_decision=_decision(False),
        prior_operational_fingerprints=_prefix(),
    )
    path = archive.store(receipt)
    payload = json.loads(path.read_text())
    payload["suite"] = "other"
    path.write_text(json.dumps(payload))
    with pytest.raises(ValueError, match="canonical|hash"):
        archive.load(receipt.sha256)


@pytest.mark.parametrize("artifact_kind", ("receipt", "index"))
def test_compile_archive_rejects_symlink_artifact_targets(
    tmp_path: Path, artifact_kind: str
) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    archive = CompileReceiptArchive(tmp_path / "archive")
    decision = _decision(False)
    context = HarnessContext(
        **{**_context().__dict__, "round_index": 1, "attempts": ()}
    )
    compiled = registry.compile(decision, variant=_variant(), context=context)
    receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v001",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256="0" * 64,
        previous_decision_sha256="0" * 64,
        compiled=compiled,
        decision=decision,
    )
    outside = tmp_path / "outside.json"
    outside.write_bytes(
        receipt.canonical_bytes if artifact_kind == "receipt" else b"outside\n"
    )
    if artifact_kind == "receipt":
        target = archive.root / "receipts" / f"{receipt.sha256}.json"
    else:
        archive.store(receipt)
        target = archive.root / "index" / "v001.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.symlink_to(outside)

    with pytest.raises(ValueError, match="unsafe .*target"):
        if artifact_kind == "receipt":
            archive.store(receipt)
        else:
            archive.store_version(
                receipt=receipt, decision=decision, fixture_only=True
            )
    assert target.is_symlink()
    assert outside.read_bytes() == (
        receipt.canonical_bytes if artifact_kind == "receipt" else b"outside\n"
    )


@pytest.mark.parametrize("parent_name", ("receipts", "index"))
def test_compile_archive_rejects_symlink_parent_directories(
    tmp_path: Path, parent_name: str
) -> None:
    archive_root = tmp_path / "archive"
    archive_root.mkdir()
    archive = CompileReceiptArchive(archive_root)
    outside = tmp_path / "outside"
    outside.mkdir()
    (archive_root / parent_name).symlink_to(outside, target_is_directory=True)
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    decision = _decision(False)
    context = HarnessContext(
        **{**_context().__dict__, "round_index": 1, "attempts": ()}
    )
    compiled = registry.compile(decision, variant=_variant(), context=context)
    receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v001",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256="0" * 64,
        previous_decision_sha256="0" * 64,
        compiled=compiled,
        decision=decision,
    )

    with pytest.raises(ValueError, match="unsafe compile .* path"):
        if parent_name == "receipts":
            archive.store(receipt)
        else:
            archive.store_version(
                receipt=receipt, decision=decision, fixture_only=True
            )
    assert list(outside.iterdir()) == []


def test_wide_compile_archive_rejects_a_truncated_ancestry_prefix(tmp_path) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    archive = CompileReceiptArchive(tmp_path)
    initial = _decision(False)
    initial_receipt = _store_initial(archive, registry)
    second = _decision(True)
    second_compiled = registry.compile(
        second,
        variant=_variant(),
        context=_context(),
        previous_decision=initial,
        prior_operational_fingerprints=(initial.operational_fingerprint,),
    )
    second_receipt = HarnessCompileReceipt.create(
        cell_id=initial_receipt.cell_id,
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v002",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256=initial_receipt.sha256,
        previous_decision_sha256=initial.sha256,
        compiled=second_compiled,
        decision=second,
        previous_decision=initial,
        prior_operational_fingerprints=(initial.operational_fingerprint,),
    )
    archive.store_version(
        receipt=second_receipt, decision=second, fixture_only=True
    )

    second_attempt = PublicAttempt(
        attempt_id="v002",
        artifact_sha256="2" * 64,
        artifact_text="second artifact",
        correct=True,
        score=1.1,
        outcome="valid",
        structural_signature="family-b",
        public_summary="score 1.1",
    )
    context = HarnessContext(
        **{
            **_context().__dict__,
            "round_index": 3,
            "attempts": (*_context().attempts, second_attempt),
        }
    )
    third = _third_decision()
    prefix = (
        initial.operational_fingerprint,
        second.operational_fingerprint,
    )
    third_compiled = registry.compile(
        third,
        variant=_variant(),
        context=context,
        previous_decision=second,
        prior_operational_fingerprints=prefix,
    )
    third_receipt = HarnessCompileReceipt.create(
        cell_id=initial_receipt.cell_id,
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v003",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256=second_receipt.sha256,
        previous_decision_sha256=second.sha256,
        compiled=third_compiled,
        decision=third,
        previous_decision=second,
        prior_operational_fingerprints=prefix,
    )
    truncated = (
        second.operational_fingerprint,
        third.operational_fingerprint,
    )
    forged = replace(
        third_receipt,
        lineage_operational_fingerprints=truncated,
        lineage_prefix_sha256=hashlib.sha256(
            json.dumps(list(truncated), sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
    )
    with pytest.raises(ValueError, match="truncates its parent prefix"):
        archive.store_version(receipt=forged, decision=third, fixture_only=True)


def test_wide_archive_recomputes_all_changes_from_its_sealed_parent(tmp_path) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    archive = CompileReceiptArchive(tmp_path)
    initial = _decision(False)
    initial_receipt = _store_initial(archive, registry)
    role_only = _role_only_decision()

    # Compile a legitimate one-axis transition under the conditional policy,
    # then forge every receipt-only assertion used by the wide archive.  The
    # resulting object is canonical and receives a fresh content hash, but the
    # sealed parent decision proves that six executable axes did not change.
    compiled = registry.compile(
        role_only,
        variant=_conditional_variant(),
        context=_context(),
        previous_decision=initial,
    )
    conditional_receipt = HarnessCompileReceipt.create(
        cell_id=initial_receipt.cell_id,
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v002",
        adaptation_policy="conditional_any_v1",
        previous_receipt_sha256=initial_receipt.sha256,
        previous_decision_sha256=initial.sha256,
        compiled=compiled,
        decision=role_only,
        previous_decision=initial,
    )
    lineage = (
        initial.operational_fingerprint,
        role_only.operational_fingerprint,
    )
    forged = replace(
        conditional_receipt,
        adaptation_policy="wide_all_fields_recompile_v1",
        lineage_operational_fingerprints=lineage,
        lineage_prefix_sha256=hashlib.sha256(
            json.dumps(list(lineage), sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        change_map={axis: True for axis in conditional_receipt.change_map},
        axis_configuration_sha256s={
            axis: hashlib.sha256(f"forged:{axis}".encode()).hexdigest()
            for axis in conditional_receipt.axis_configuration_sha256s
        },
    )
    assert forged.sha256 != conditional_receipt.sha256

    with pytest.raises(ValueError, match="change map is not decision-derived"):
        archive.store_version(
            receipt=forged, decision=role_only, fixture_only=True
        )


def test_trusted_store_rejects_fully_rehashed_wide_semantics_before_writing(
    tmp_path,
) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    archive = CompileReceiptArchive(tmp_path)
    initial = _decision(False)
    initial_receipt = _store_initial(archive, registry)
    decision = _decision(True)
    compiled = registry.compile(
        decision,
        variant=_variant(),
        context=_context(),
        previous_decision=initial,
        prior_operational_fingerprints=_prefix(),
    )
    receipt = HarnessCompileReceipt.create(
        cell_id=initial_receipt.cell_id,
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v002",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256=initial_receipt.sha256,
        previous_decision_sha256=initial.sha256,
        compiled=compiled,
        decision=decision,
        previous_decision=initial,
        prior_operational_fingerprints=_prefix(),
    )
    forged = replace(
        receipt,
        memory_sha256="b" * 64,
        tool_outputs_sha256="c" * 64,
        axis_effect_sha256s={
            axis: hashlib.sha256(f"forged:{axis}".encode()).hexdigest()
            for axis in receipt.axis_effect_sha256s
        },
    )

    with pytest.raises(ValueError, match="trusted recompilation"):
        archive.store_trusted_version(
            receipt=forged,
            decision=decision,
            compiled=compiled,
            previous_decision=initial,
            prior_operational_fingerprints=_prefix(),
        )

    assert not (archive.root / "receipts" / f"{forged.sha256}.json").exists()
    assert not (archive.root / "index" / "v002.json").exists()


def test_generic_version_store_requires_explicit_fixture_only_opt_in(tmp_path) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    decision = _decision(False)
    context = HarnessContext(
        **{**_context().__dict__, "round_index": 1, "attempts": ()}
    )
    compiled = registry.compile(decision, variant=_variant(), context=context)
    receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v001",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256="0" * 64,
        previous_decision_sha256="0" * 64,
        compiled=compiled,
        decision=decision,
    )
    archive = CompileReceiptArchive(tmp_path)

    with pytest.raises(ValueError, match="fixture-only"):
        archive.store_version(receipt=receipt, decision=decision)

    assert not (archive.root / "receipts" / f"{receipt.sha256}.json").exists()
    assert not (archive.root / "index" / "v001.json").exists()


def test_compile_version_index_rejects_a_decision_rebind(tmp_path) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    archive = CompileReceiptArchive(tmp_path)
    initial_receipt = _store_initial(archive, registry)
    decision = _decision(True)
    compiled = registry.compile(
        decision,
        variant=_variant(),
        context=_context(),
        previous_decision=_decision(False),
        prior_operational_fingerprints=_prefix(),
    )
    receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v002",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256=initial_receipt.sha256,
        previous_decision_sha256=_decision(False).sha256,
        compiled=compiled,
        decision=decision,
        previous_decision=_decision(False),
        prior_operational_fingerprints=_prefix(),
    )
    path = archive.store_version(
        receipt=receipt, decision=decision, fixture_only=True
    )
    payload = json.loads(path.read_text())
    payload["decision"]["kernel_directive"] = "rebound"
    path.write_text(json.dumps(payload))
    with pytest.raises(ValueError, match="canonical|binding"):
        archive.load_version(
            "v002",
            cell_id="formal:suite:task:B-frozen-wide",
            suite="suite",
            instance_id="suite:task",
            variant_id="B-frozen-wide",
        )


def test_wide_compile_receipt_rejects_incomplete_change_map() -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    with pytest.raises(ValueError, match="axes unchanged"):
        registry.compile(
            _decision(False),
            variant=_variant(),
            context=_context(),
            previous_decision=_decision(False),
        )


def test_compile_receipt_cannot_rebind_the_compiled_adaptation_policy() -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    decision = _decision(True)
    previous = _decision(False)
    compiled = registry.compile(
        decision,
        variant=_variant(),
        context=_context(),
        previous_decision=previous,
        prior_operational_fingerprints=(previous.operational_fingerprint,),
    )

    with pytest.raises(ValueError, match="adaptation policy differs"):
        HarnessCompileReceipt.create(
            cell_id="formal:suite:task:B-frozen-wide",
            suite="suite",
            instance_id="suite:task",
            variant_id="B-frozen-wide",
            version="v002",
            adaptation_policy="conditional_any_v1",
            previous_receipt_sha256="1" * 64,
            previous_decision_sha256=previous.sha256,
            compiled=compiled,
            decision=decision,
            previous_decision=previous,
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        (
            lambda payload: payload["change_map"].update({"tools": 1}),
            "change map",
        ),
        (
            lambda payload: payload["component_instances"].pop(),
            "coverage",
        ),
        (
            lambda payload: payload["component_instances"][0].update(
                {"implementation_ref": "moss.harness.untrusted.code.v1"}
            ),
            "implementation",
        ),
        (
            lambda payload: payload["component_instances"][0].update(
                {"config_sha256": "not-a-hash"}
            ),
            "config sha256",
        ),
        (
            lambda payload: payload["component_instances"][0].update(
                {"instance_nonce_sha256": "0" * 64}
            ),
            "instance binding",
        ),
        (
            lambda payload: payload["axis_effect_sha256s"].pop("tools"),
            "effect coverage",
        ),
        (
            lambda payload: payload["axis_configuration_sha256s"].pop("tools"),
            "configuration coverage",
        ),
    ),
)
def test_compile_receipt_revalidates_forged_canonical_payload(
    mutation, message: str
) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    decision = _decision(True)
    compiled = registry.compile(
        decision,
        variant=_variant(),
        context=_context(),
        previous_decision=_decision(False),
        prior_operational_fingerprints=_prefix(),
    )
    receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v002",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256="1" * 64,
        previous_decision_sha256=_decision(False).sha256,
        compiled=compiled,
        decision=decision,
        previous_decision=_decision(False),
        prior_operational_fingerprints=_prefix(),
    )
    payload = json.loads(receipt.canonical_bytes)
    mutation(payload)
    encoded = (
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    forged_sha = hashlib.sha256(encoded).hexdigest()

    with pytest.raises(ValueError, match=message):
        HarnessCompileReceipt.from_bytes(encoded, expected_sha256=forged_sha)


def test_compile_receipt_v2_requires_context_binding() -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    decision = _decision(True)
    previous = _decision(False)
    compiled = registry.compile(
        decision,
        variant=_variant(),
        context=_context(),
        previous_decision=previous,
        prior_operational_fingerprints=_prefix(),
    )
    receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-frozen-wide",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-frozen-wide",
        version="v002",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256="1" * 64,
        previous_decision_sha256=previous.sha256,
        compiled=compiled,
        decision=decision,
        previous_decision=previous,
        prior_operational_fingerprints=_prefix(),
    )
    payload = json.loads(receipt.canonical_bytes)
    assert payload["schema_version"] == 2
    payload["schema_version"] = 1
    encoded = (
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()

    with pytest.raises(ValueError, match="schema differs"):
        HarnessCompileReceipt.from_bytes(
            encoded,
            expected_sha256=hashlib.sha256(encoded).hexdigest(),
        )


def test_targeted_archive_recomputes_change_map_from_its_sealed_parent(tmp_path) -> None:
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    archive = CompileReceiptArchive(tmp_path)
    decision = _decision(False)
    initial_context = HarnessContext(
        **{**_context().__dict__, "round_index": 1, "attempts": ()}
    )
    initial_compiled = registry.compile(
        decision,
        variant=_targeted_variant(),
        context=initial_context,
    )
    initial_receipt = HarnessCompileReceipt.create(
        cell_id="formal:suite:task:B-targeted",
        suite="suite",
        instance_id="suite:task",
        variant_id="B-targeted",
        version="v001",
        adaptation_policy="targeted_any_change_v1",
        previous_receipt_sha256="0" * 64,
        previous_decision_sha256="0" * 64,
        compiled=initial_compiled,
        decision=decision,
    )
    archive.store_version(
        receipt=initial_receipt, decision=decision, fixture_only=True
    )

    # A conditional compile may legitimately keep the exact same decision.  An
    # attacker then changes only the receipt policy and rehashes a forged true
    # change_map.  The archive must derive the map from its sealed v001 decision
    # instead of trusting that self-consistent, content-addressed assertion.
    unchanged_compiled = registry.compile(
        decision,
        variant=_conditional_variant(),
        context=_context(),
        previous_decision=decision,
    )
    forged_compiled = replace(
        unchanged_compiled,
        adaptation_policy="targeted_any_change_v1",
        change_map={
            **unchanged_compiled.change_map,
            "role_graph": True,
        },
    )
    with pytest.raises(ValueError, match="lacks its previous decision"):
        HarnessCompileReceipt.create(
            cell_id=initial_receipt.cell_id,
            suite="suite",
            instance_id="suite:task",
            variant_id="B-targeted",
            version="v002",
            adaptation_policy="targeted_any_change_v1",
            previous_receipt_sha256=initial_receipt.sha256,
            previous_decision_sha256=decision.sha256,
            compiled=forged_compiled,
            decision=decision,
        )

    conditional_receipt = HarnessCompileReceipt.create(
        cell_id=initial_receipt.cell_id,
        suite="suite",
        instance_id="suite:task",
        variant_id="B-targeted",
        version="v002",
        adaptation_policy="conditional_any_v1",
        previous_receipt_sha256=initial_receipt.sha256,
        previous_decision_sha256=decision.sha256,
        compiled=unchanged_compiled,
        decision=decision,
        previous_decision=decision,
    )
    forged_receipt = replace(
        conditional_receipt,
        adaptation_policy="targeted_any_change_v1",
        change_map={
            **conditional_receipt.change_map,
            "role_graph": True,
        },
    )
    with pytest.raises(ValueError, match="change map is not decision-derived"):
        archive.store_version(
            receipt=forged_receipt, decision=decision, fixture_only=True
        )
