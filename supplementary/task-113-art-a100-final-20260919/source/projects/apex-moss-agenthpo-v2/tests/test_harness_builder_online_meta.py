from __future__ import annotations

from pathlib import Path

import pytest

from optimization_lab.harness_builder.experience import ExperienceRecord
from optimization_lab.harness_builder.learning import ExperienceBankSnapshot
from optimization_lab.harness_builder.meta_evolution import (
    HarnessArchiveNode,
    HarnessArchiveSnapshot,
    MetaCheckpointV2,
    MetaPolicySnapshot,
    MetaUpdateProposal,
    TrustedMetaPolicyRegistry,
)
from optimization_lab.harness_builder.online_meta import (
    MetaLaneBinding,
    OnlineMetaController,
    SealedMetaSourceEvidence,
    validate_meta_lane_cohort,
)


def _resolved_genesis() -> tuple[
    MetaCheckpointV2,
    TrustedMetaPolicyRegistry,
    ExperienceBankSnapshot,
    MetaPolicySnapshot,
    HarnessArchiveSnapshot,
]:
    registry = TrustedMetaPolicyRegistry.default()
    memory = ExperienceBankSnapshot.create(
        bank_id="bank-v000",
        parent_sha256=None,
        records=(),
    )
    policy = MetaPolicySnapshot.create(
        policy_id="policy-v000",
        registry=registry,
    )
    archive = HarnessArchiveSnapshot.create(
        archive_id="archive-v000",
        registry=registry,
    )
    checkpoint = MetaCheckpointV2(
        checkpoint_id="checkpoint-v000",
        parent_checkpoint_sha256=None,
        trusted_meta_registry_sha256=registry.sha256,
        next_stream_index=0,
        learned_through_instance_id=None,
        memory_sha256=memory.sha256,
        meta_policy_sha256=policy.sha256,
        harness_archive_sha256=archive.sha256,
    )
    return checkpoint, registry, memory, policy, archive


def _genesis() -> MetaCheckpointV2:
    return _resolved_genesis()[0]


def _evidence(index: int) -> SealedMetaSourceEvidence:
    return SealedMetaSourceEvidence(
        source_suite="suite-a",
        source_instance_id=f"suite-a:task-{index}",
        source_stream_index=index,
        sealed_arm_receipt_sha256=hex(index + 1)[2:] * 64,
        public_metrics={"mean_score": 0.25 + index / 10, "valid_rounds": 8},
        public_tags=("contract-valid",),
        provenance_event_ids=(f"sealed-event-{index}",),
    )


def _bindings(
    genesis: MetaCheckpointV2,
    evidence: tuple[SealedMetaSourceEvidence, ...],
    *,
    seed: int = 7,
) -> dict[str, MetaLaneBinding]:
    common = {
        "experiment_id": "online-mechanism-canary-v1",
        "seed": seed,
        "source_instance_ids": tuple(item.source_instance_id for item in evidence),
        "source_evidence_sha256s": tuple(item.sha256 for item in evidence),
        "genesis_checkpoint_sha256": genesis.sha256,
        "trusted_meta_registry_sha256": genesis.trusted_meta_registry_sha256,
    }
    return {
        mechanism: MetaLaneBinding(mechanism_id=mechanism, **common)
        for mechanism in ("O0", "OM", "OP", "OA")
    }


def _proposal(
    before: MetaCheckpointV2,
    *,
    mechanism: str,
    index: int,
    salt: str = "d",
) -> tuple[MetaUpdateProposal, MetaCheckpointV2]:
    after = dict(before.mechanism_sha256s)
    after[mechanism] = salt * 64
    proposal = MetaUpdateProposal(
        proposal_id=f"proposal-{mechanism}-{index}-{salt}",
        result_checkpoint_id=f"checkpoint-{mechanism}-{index + 1}-{salt}",
        mechanism=mechanism,
        parent_checkpoint_sha256=before.sha256,
        trusted_meta_registry_sha256=before.trusted_meta_registry_sha256,
        source_instance_id=f"suite-a:task-{index}",
        source_stream_index=index,
        target_stream_index=index + 1,
        before_sha256s=before.mechanism_sha256s,
        after_sha256s=after,
        provenance_event_ids=(f"distilled-event-{index}",),
    )
    return proposal, before.apply(
        proposal, sealed_source_instance_ids=(f"suite-a:task-{index}",)
    )


def _record(index: int, salt: str) -> ExperienceRecord:
    return ExperienceRecord.from_dict(
        {
            "record_id": f"experience-{index}-{salt}",
            "source_instance_id": f"suite-a:task-{index}",
            "builder_version": "builder-v001",
            "instance_descriptor": ["public-descriptor"],
            "initial_harness_structure": ["task_analyst", "generator"],
            "evolution_rule": "discipline",
            "trigger_evidence": ["public-evidence"],
            "outcome_delta": 0.1,
            "correctness": True,
            "resource_cost": {"model_calls": 1.0},
            "counterexamples": ["none-observed"],
            "scope": "single_instance_observation",
            "provenance_event_ids": [f"sealed-event-{index}"],
            "sealed": True,
        }
    )


def _selection() -> dict[str, tuple[str, ...]]:
    return {
        "role_graph": ("task_analyst", "generator", "verifier"),
        "memory_views": ("current", "best"),
        "tools": ("task_semantics", "score_history"),
        "parent_strategy": ("incumbent",),
        "workflow": ("analyze", "select_parent", "generate", "verify_contract"),
        "scheduler_mode": ("single_candidate",),
        "recovery_mode": ("repair_then_reset",),
    }


def _verified_transition(
    before: MetaCheckpointV2,
    *,
    mechanism: str,
    index: int,
    salt: str,
    registry: TrustedMetaPolicyRegistry,
    parent_memory: ExperienceBankSnapshot,
    parent_meta_policy: MetaPolicySnapshot,
    parent_harness_archive: HarnessArchiveSnapshot,
) -> tuple[
    MetaUpdateProposal,
    MetaCheckpointV2,
    ExperienceBankSnapshot,
    MetaPolicySnapshot,
    HarnessArchiveSnapshot,
]:
    memory = parent_memory
    meta_policy = parent_meta_policy
    harness_archive = parent_harness_archive
    if mechanism == "M":
        memory = parent_memory.extend(
            (_record(index, salt),),
            bank_id=f"bank-v{index + 1:03d}-{salt}",
        )
    elif mechanism == "P":
        meta_policy = MetaPolicySnapshot.create(
            policy_id=f"policy-v{index + 1:03d}-{salt}",
            registry=registry,
            parent_sha256=parent_meta_policy.sha256,
            selection_mode=(
                "failure_directed_v1" if index % 2 == 0 else "pareto_diverse_v1"
            ),
        )
    elif mechanism == "A":
        node = HarnessArchiveNode.create(
            node_id=f"node-v{index + 1:03d}-{salt}",
            registry=registry,
            source_suite="suite-a",
            source_instance_id=f"suite-a:task-{index}",
            source_stream_index=index,
            harness_decision_sha256=hex(index + 10)[2:] * 64,
            component_selection=_selection(),
            metrics={
                "quality": 0.6,
                "novelty": 0.4,
                "recovery": 0.5,
                "efficiency": 0.7,
            },
            provenance_event_ids=(f"sealed-event-{index}",),
            parent_node_sha256=(
                None
                if not parent_harness_archive.nodes
                else parent_harness_archive.nodes[-1].sha256
            ),
        )
        harness_archive = parent_harness_archive.extend(
            node,
            archive_id=f"archive-v{index + 1:03d}-{salt}",
            registry=registry,
        )
    else:  # pragma: no cover - test helper guard
        raise AssertionError(f"unknown mechanism: {mechanism}")

    proposal = MetaUpdateProposal(
        proposal_id=f"proposal-{mechanism}-{index}-{salt}",
        result_checkpoint_id=f"checkpoint-{mechanism}-{index + 1}-{salt}",
        mechanism=mechanism,
        parent_checkpoint_sha256=before.sha256,
        trusted_meta_registry_sha256=before.trusted_meta_registry_sha256,
        source_instance_id=f"suite-a:task-{index}",
        source_stream_index=index,
        target_stream_index=index + 1,
        before_sha256s=before.mechanism_sha256s,
        after_sha256s={
            "M": memory.sha256,
            "P": meta_policy.sha256,
            "A": harness_archive.sha256,
        },
        provenance_event_ids=(f"distilled-event-{index}",),
    )
    after = before.apply_verified(
        proposal,
        sealed_source_instance_ids=(f"suite-a:task-{index}",),
        parent_memory=parent_memory,
        memory=memory,
        parent_meta_policy=parent_meta_policy,
        meta_policy=meta_policy,
        parent_harness_archive=parent_harness_archive,
        harness_archive=harness_archive,
        registry=registry,
    )
    return proposal, after, memory, meta_policy, harness_archive


def test_lane_cohort_requires_byte_identical_source_evidence() -> None:
    genesis = _genesis()
    evidence = (_evidence(0), _evidence(1))
    bindings = _bindings(genesis, evidence)
    validate_meta_lane_cohort(tuple(bindings.values()))

    drifted = MetaLaneBinding(
        experiment_id="online-mechanism-canary-v1",
        mechanism_id="OA",
        seed=7,
        source_instance_ids=tuple(item.source_instance_id for item in evidence),
        source_evidence_sha256s=(evidence[0].sha256, "f" * 64),
        genesis_checkpoint_sha256=genesis.sha256,
        trusted_meta_registry_sha256=genesis.trusted_meta_registry_sha256,
    )
    with pytest.raises(ValueError, match="source/checkpoint bytes differ"):
        validate_meta_lane_cohort(
            (bindings["O0"], bindings["OM"], bindings["OP"], drifted)
        )


def test_o0_records_exactly_once_zero_call_no_update_and_seals(tmp_path: Path) -> None:
    genesis = _genesis()
    evidence = (_evidence(0), _evidence(1))
    binding = _bindings(genesis, evidence)["O0"]
    controller = OnlineMetaController(
        root=tmp_path, binding=binding, genesis_checkpoint=genesis
    )

    first = controller.update_once(
        evidence[0],
        before_checkpoint=genesis,
        after_checkpoint=genesis,
        proposal=None,
    )
    replay = controller.update_once(
        evidence[0],
        before_checkpoint=genesis,
        after_checkpoint=genesis,
        proposal=None,
    )
    assert replay == first
    assert first.action_kind == "no_update"
    assert first.mechanism_update_count == 0
    assert first.controller_model_calls == first.controller_evaluator_calls == 0
    assert len(controller.ledger_path.read_text().splitlines()) == 1

    with pytest.raises(ValueError, match="cannot seal"):
        controller.seal_source_snapshot()
    second = controller.update_once(
        evidence[1],
        before_checkpoint=genesis,
        after_checkpoint=genesis,
        proposal=None,
    )
    seal = controller.seal_source_snapshot()
    assert seal.update_receipt_sha256s == (first.sha256, second.sha256)
    assert seal.final_checkpoint_sha256 == genesis.sha256
    assert (controller.lane_root / "source_snapshots" / f"{seal.sha256}.json").is_file()


@pytest.mark.parametrize(("lane", "mechanism"), (("OM", "M"), ("OP", "P"), ("OA", "A")))
def test_learned_lane_updates_in_order_and_is_idempotent(
    tmp_path: Path, lane: str, mechanism: str
) -> None:
    genesis, registry, memory, policy, archive = _resolved_genesis()
    evidence = (_evidence(0), _evidence(1))
    controller = OnlineMetaController(
        root=tmp_path,
        binding=_bindings(genesis, evidence)[lane],
        genesis_checkpoint=genesis,
    )
    proposal0, after0, memory0, policy0, archive0 = _verified_transition(
        genesis,
        mechanism=mechanism,
        index=0,
        salt="d",
        registry=registry,
        parent_memory=memory,
        parent_meta_policy=policy,
        parent_harness_archive=archive,
    )
    receipt0 = controller.update_once(
        evidence[0],
        before_checkpoint=genesis,
        after_checkpoint=after0,
        proposal=proposal0,
        parent_memory=memory,
        memory=memory0,
        parent_meta_policy=policy,
        meta_policy=policy0,
        parent_harness_archive=archive,
        harness_archive=archive0,
        registry=registry,
    )
    assert receipt0.mechanism_update_count == 1
    assert receipt0.controller_model_calls == receipt0.controller_evaluator_calls == 0
    assert (
        controller.update_once(
            evidence[0],
            before_checkpoint=genesis,
            after_checkpoint=after0,
            proposal=proposal0,
            parent_memory=memory,
            memory=memory0,
            parent_meta_policy=policy,
            meta_policy=policy0,
            parent_harness_archive=archive,
            harness_archive=archive0,
            registry=registry,
        )
        == receipt0
    )

    proposal1, after1, memory1, policy1, archive1 = _verified_transition(
        after0,
        mechanism=mechanism,
        index=1,
        salt="e",
        registry=registry,
        parent_memory=memory0,
        parent_meta_policy=policy0,
        parent_harness_archive=archive0,
    )
    receipt1 = controller.update_once(
        evidence[1],
        before_checkpoint=after0,
        after_checkpoint=after1,
        proposal=proposal1,
        parent_memory=memory0,
        memory=memory1,
        parent_meta_policy=policy0,
        meta_policy=policy1,
        parent_harness_archive=archive0,
        harness_archive=archive1,
        registry=registry,
    )
    assert receipt1.previous_receipt_sha256 == receipt0.sha256
    seal = controller.seal_source_snapshot()
    assert seal.final_checkpoint_sha256 == after1.sha256


def test_learned_lane_rejects_unresolved_or_invented_mechanism_hashes(
    tmp_path: Path,
) -> None:
    genesis, registry, memory, policy, archive = _resolved_genesis()
    evidence = (_evidence(0),)
    controller = OnlineMetaController(
        root=tmp_path,
        binding=_bindings(genesis, evidence)["OP"],
        genesis_checkpoint=genesis,
    )
    invented, invented_after = _proposal(
        genesis, mechanism="P", index=0, salt="d"
    )

    with pytest.raises(TypeError, match="resolved parent/child Experience Bank"):
        controller.update_once(
            evidence[0],
            before_checkpoint=genesis,
            after_checkpoint=invented_after,
            proposal=invented,
        )

    with pytest.raises(ValueError, match="do not resolve"):
        controller.update_once(
            evidence[0],
            before_checkpoint=genesis,
            after_checkpoint=invented_after,
            proposal=invented,
            parent_memory=memory,
            memory=memory,
            parent_meta_policy=policy,
            meta_policy=policy,
            parent_harness_archive=archive,
            harness_archive=archive,
            registry=registry,
        )
    assert not controller.ledger_path.exists()


def test_learned_lane_persists_every_verified_resolved_object(tmp_path: Path) -> None:
    genesis, registry, memory, policy, archive = _resolved_genesis()
    evidence = (_evidence(0),)
    controller = OnlineMetaController(
        root=tmp_path,
        binding=_bindings(genesis, evidence)["OP"],
        genesis_checkpoint=genesis,
    )
    proposal, after, next_memory, next_policy, next_archive = _verified_transition(
        genesis,
        mechanism="P",
        index=0,
        salt="d",
        registry=registry,
        parent_memory=memory,
        parent_meta_policy=policy,
        parent_harness_archive=archive,
    )
    controller.update_once(
        evidence[0],
        before_checkpoint=genesis,
        after_checkpoint=after,
        proposal=proposal,
        parent_memory=memory,
        memory=next_memory,
        parent_meta_policy=policy,
        meta_policy=next_policy,
        parent_harness_archive=archive,
        harness_archive=next_archive,
        registry=registry,
    )

    expected = (
        ("registries", registry),
        ("memory", memory),
        ("meta_policies", policy),
        ("meta_policies", next_policy),
        ("harness_archives", archive),
    )
    for directory, item in expected:
        path = controller.lane_root / "resolved" / directory / f"{item.sha256}.json"
        assert path.read_bytes() == item.canonical_bytes


def test_rejects_out_of_order_evidence_drift_wrong_mechanism_and_conflict(
    tmp_path: Path,
) -> None:
    genesis, registry, memory, policy, archive = _resolved_genesis()
    evidence = (_evidence(0), _evidence(1))
    binding = _bindings(genesis, evidence)["OM"]
    controller = OnlineMetaController(
        root=tmp_path, binding=binding, genesis_checkpoint=genesis
    )
    proposal0, after0, memory0, policy0, archive0 = _verified_transition(
        genesis,
        mechanism="M",
        index=0,
        salt="d",
        registry=registry,
        parent_memory=memory,
        parent_meta_policy=policy,
        parent_harness_archive=archive,
    )
    with pytest.raises(ValueError, match="stream order"):
        controller.update_once(
            evidence[1],
            before_checkpoint=genesis,
            after_checkpoint=after0,
            proposal=proposal0,
        )

    drifted = SealedMetaSourceEvidence(
        source_suite="suite-a",
        source_instance_id="suite-a:task-0",
        source_stream_index=0,
        sealed_arm_receipt_sha256="9" * 64,
        public_metrics={"mean_score": 0.25, "valid_rounds": 8},
        public_tags=("contract-valid",),
        provenance_event_ids=("sealed-event-0",),
    )
    with pytest.raises(ValueError, match="evidence binding differs"):
        controller.update_once(
            drifted,
            before_checkpoint=genesis,
            after_checkpoint=after0,
            proposal=proposal0,
        )

    wrong, wrong_after = _proposal(genesis, mechanism="P", index=0, salt="d")
    with pytest.raises(ValueError, match="mechanism differs"):
        controller.update_once(
            evidence[0],
            before_checkpoint=genesis,
            after_checkpoint=wrong_after,
            proposal=wrong,
        )

    controller.update_once(
        evidence[0],
        before_checkpoint=genesis,
        after_checkpoint=after0,
        proposal=proposal0,
        parent_memory=memory,
        memory=memory0,
        parent_meta_policy=policy,
        meta_policy=policy0,
        parent_harness_archive=archive,
        harness_archive=archive0,
        registry=registry,
    )
    (
        conflicting,
        conflicting_after,
        conflicting_memory,
        conflicting_policy,
        conflicting_archive,
    ) = _verified_transition(
        genesis,
        mechanism="M",
        index=0,
        salt="f",
        registry=registry,
        parent_memory=memory,
        parent_meta_policy=policy,
        parent_harness_archive=archive,
    )
    with pytest.raises(ValueError, match="conflicting content"):
        controller.update_once(
            evidence[0],
            before_checkpoint=genesis,
            after_checkpoint=conflicting_after,
            proposal=conflicting,
            parent_memory=memory,
            memory=conflicting_memory,
            parent_meta_policy=policy,
            meta_policy=conflicting_policy,
            parent_harness_archive=archive,
            harness_archive=conflicting_archive,
            registry=registry,
        )


def test_mechanisms_and_seeds_use_separate_roots_and_ledgers(tmp_path: Path) -> None:
    genesis = _genesis()
    evidence = (_evidence(0),)
    seed7 = _bindings(genesis, evidence, seed=7)
    seed8 = _bindings(genesis, evidence, seed=8)
    controllers = [
        OnlineMetaController(root=tmp_path, binding=seed7["O0"], genesis_checkpoint=genesis),
        OnlineMetaController(root=tmp_path, binding=seed7["OM"], genesis_checkpoint=genesis),
        OnlineMetaController(root=tmp_path, binding=seed8["OM"], genesis_checkpoint=genesis),
    ]
    assert len({item.lane_root for item in controllers}) == 3
    assert len({item.ledger_path for item in controllers}) == 3
    assert {item.lane_root.relative_to(tmp_path).parts[:2] for item in controllers} == {
        ("O0", "seed-7"),
        ("OM", "seed-7"),
        ("OM", "seed-8"),
    }


def test_public_evidence_rejects_private_ids_and_nonfinite_metrics() -> None:
    with pytest.raises(ValueError, match="non-public"):
        SealedMetaSourceEvidence(
            source_suite="suite-a",
            source_instance_id="suite-a:hidden-task",
            source_stream_index=0,
            sealed_arm_receipt_sha256="1" * 64,
            public_metrics={"mean_score": 0.2},
            public_tags=(),
            provenance_event_ids=("event-1",),
        )
    with pytest.raises(ValueError, match="finite"):
        SealedMetaSourceEvidence(
            source_suite="suite-a",
            source_instance_id="suite-a:task-0",
            source_stream_index=0,
            sealed_arm_receipt_sha256="1" * 64,
            public_metrics={"mean_score": float("nan")},
            public_tags=(),
            provenance_event_ids=("event-1",),
        )
