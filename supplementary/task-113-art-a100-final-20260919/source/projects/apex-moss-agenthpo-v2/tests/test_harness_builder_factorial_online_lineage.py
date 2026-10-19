from __future__ import annotations

from dataclasses import replace
import json
from typing import Any

import pytest

from optimization_lab.harness_builder.factorial_online_lineage import (
    FactorialOnlineLineageBundle,
    FactorialOnlineLineageError,
    OnlineHeldoutCompileProjectionReceipt,
    OnlineHeldoutStateBindingReceipt,
    ResolvedOnlineState,
    ResolvedOnlineTransition,
    OnlineUpdateLineageReceipt,
    ZERO_SHA256,
    attempt_slot_sha256,
    factorial_online_genesis_state,
    update_slot_sha256,
    validate_heldout_state_binding_cohort,
)
from optimization_lab.harness_builder.factorial_online_plan import (
    FactorialOnlineZeroCallPlan,
)
from optimization_lab.harness_builder.experience import ExperienceRecord
from optimization_lab.harness_builder.meta_evolution import (
    HarnessArchiveNode,
    MetaPolicySnapshot,
    MetaUpdateProposal,
)
from optimization_lab.harness_builder.meta_prior import BuilderMetaPrior
from optimization_lab.harness_builder.operators import HarnessContext, TrustedOperatorRegistry
from optimization_lab.harness_builder.schema import BuilderVariant, HarnessDecision


def _bundle() -> FactorialOnlineLineageBundle:
    return FactorialOnlineLineageBundle.from_verified_plan(
        FactorialOnlineZeroCallPlan.from_verified_contract()
    )


def _canonical(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n"
    ).encode()


def _first_update(
    bundle: FactorialOnlineLineageBundle,
    *,
    benchmark: str = "agenthpobench",
    seed: int = 2026081201,
    mechanism: str = "OM",
    outcome: str = "APPLIED",
) -> OnlineUpdateLineageReceipt:
    lane = bundle.lane(benchmark, seed, mechanism)
    slot = bundle.update_slots(lane)[0]
    applied = outcome == "APPLIED"
    return bundle.create_update(
        lane=lane,
        slot=slot,
        source_terminal_receipt_sha256="1" * 64,
        parent_state_sha256="2" * 64,
        parent_checkpoint_sha256="3" * 64,
        output_state_sha256=("4" if applied else "2") * 64,
        output_checkpoint_sha256=("5" if applied else "3") * 64,
        operation_record_sha256="6" * 64,
        outcome=outcome,
        previous=None,
    )


def _context(
    *,
    slot: Any,
    stream_index: int,
    prior: BuilderMetaPrior | None = None,
) -> HarnessContext:
    return HarnessContext(
        instance_id=slot.instance_id,
        suite=slot.benchmark_id,
        round_index=slot.version,
        task_card="Solve the frozen public held-out task.",
        reference_artifact_id="reference",
        reference_artifact="reference artifact",
        public_observations={
            "artifact_contract": {"schema_version": 1, "kind": "public"}
        },
        stream_index=stream_index,
        builder_meta_prior=prior,
    )


def _state_and_transitions(
    bundle: FactorialOnlineLineageBundle,
    *,
    lane: Any,
    terminal_hashes: tuple[str, ...],
) -> tuple[ResolvedOnlineState, tuple[ResolvedOnlineTransition, ...]]:
    before = factorial_online_genesis_state()
    resolved: list[ResolvedOnlineTransition] = []
    previous = None
    slots = bundle.update_slots(lane)
    modes = ("failure_directed_v1", "pareto_diverse_v1")
    for index, update_slot in enumerate(slots):
        memory = before.memory
        policy = before.meta_policy
        archive = before.harness_archive
        mechanism_code = {"OM": "M", "OP": "P", "OA": "A"}[
            lane.mechanism_id
        ]
        if lane.mechanism_id == "OM":
            record = ExperienceRecord.from_dict(
                {
                    "record_id": f"factorial-online-record-{index + 1:03d}",
                    "source_instance_id": update_slot.source_instance_id,
                    "builder_version": "builder-v001",
                    "instance_descriptor": ["public-task"],
                    "initial_harness_structure": ["task_analyst", "generator"],
                    "evolution_rule": "discipline",
                    "trigger_evidence": ["public-evidence"],
                    "outcome_delta": 0.1,
                    "correctness": True,
                    "resource_cost": {"model_calls": 1.0},
                    "counterexamples": ["none-observed"],
                    "scope": "single_instance_observation",
                    "provenance_event_ids": [f"sealed-source-event-{index}"],
                    "sealed": True,
                }
            )
            memory = before.memory.extend(
                (record,),
                bank_id=f"factorial-online-memory-v{index + 1:03d}",
            )
        elif lane.mechanism_id == "OP":
            policy = MetaPolicySnapshot.create(
                policy_id=f"factorial-online-op-policy-v{index + 1:03d}",
                registry=before.registry,
                parent_sha256=before.meta_policy.sha256,
                selection_mode=modes[index % len(modes)],
                exploration_rate=min(0.9, 0.21 + index / 100),
            )
        else:
            node = HarnessArchiveNode.create(
                node_id=f"factorial-online-node-v{index + 1:03d}",
                registry=before.registry,
                source_suite=lane.benchmark_id,
                source_instance_id=update_slot.source_instance_id,
                source_stream_index=index,
                harness_decision_sha256=f"{index + 100:064x}",
                component_selection={
                    "role_graph": ("task_analyst", "generator", "verifier"),
                    "memory_views": ("current",),
                    "tools": ("task_semantics",),
                    "parent_strategy": ("reference",),
                    "workflow": ("analyze", "generate", "verify_contract"),
                    "scheduler_mode": ("single_candidate",),
                    "recovery_mode": ("preserve_failure",),
                },
                metrics={
                    "quality": 0.6,
                    "novelty": 0.4,
                    "recovery": 0.5,
                    "efficiency": 0.7,
                },
                provenance_event_ids=(f"sealed-source-event-{index}",),
                parent_node_sha256=(
                    None
                    if not before.harness_archive.nodes
                    else before.harness_archive.nodes[-1].sha256
                ),
            )
            archive = before.harness_archive.extend(
                node,
                archive_id=f"factorial-online-archive-v{index + 1:03d}",
                registry=before.registry,
            )
        proposal = MetaUpdateProposal(
            proposal_id=(
                f"factorial-online-{lane.mechanism_id.lower()}-proposal-"
                f"v{index + 1:03d}"
            ),
            result_checkpoint_id=(
                f"factorial-online-{lane.mechanism_id.lower()}-checkpoint-"
                f"v{index + 1:03d}"
            ),
            mechanism=mechanism_code,
            parent_checkpoint_sha256=before.checkpoint.sha256,
            trusted_meta_registry_sha256=before.registry.sha256,
            source_instance_id=update_slot.source_instance_id,
            source_stream_index=index,
            target_stream_index=index + 1,
            before_sha256s=before.checkpoint.mechanism_sha256s,
            after_sha256s={
                "M": memory.sha256,
                "P": policy.sha256,
                "A": archive.sha256,
            },
            provenance_event_ids=(f"sealed-source-event-{index}",),
        )
        checkpoint = before.checkpoint.apply_verified(
            proposal,
            sealed_source_instance_ids=(update_slot.source_instance_id,),
            parent_memory=before.memory,
            memory=memory,
            parent_meta_policy=before.meta_policy,
            meta_policy=policy,
            parent_harness_archive=before.harness_archive,
            harness_archive=archive,
            registry=before.registry,
        )
        after = ResolvedOnlineState(
            checkpoint=checkpoint,
            memory=memory,
            meta_policy=policy,
            harness_archive=archive,
            registry=before.registry,
        )
        receipt = bundle.create_update(
            lane=lane,
            slot=update_slot,
            source_terminal_receipt_sha256=terminal_hashes[index],
            parent_state_sha256=before.mechanism_state_sha256(lane.mechanism_id),
            parent_checkpoint_sha256=before.checkpoint.sha256,
            output_state_sha256=after.mechanism_state_sha256(lane.mechanism_id),
            output_checkpoint_sha256=after.checkpoint.sha256,
            operation_record_sha256=f"{index + 10:064x}",
            outcome="APPLIED",
            previous=previous,
        )
        resolved.append(
            ResolvedOnlineTransition(
                receipt=receipt,
                proposal=proposal,
                before_state=before,
                after_state=after,
            )
        )
        before = after
        previous = receipt
    return before, tuple(resolved)


def _prior(
    *,
    mechanism: str,
    state: ResolvedOnlineState,
    slot: Any,
    target_index: int,
) -> BuilderMetaPrior:
    if mechanism == "OM":
        return BuilderMetaPrior.from_memory(
            bank=state.memory,
            checkpoint=state.checkpoint,
            target_instance_descriptors=("optimization", "public-task"),
            target_instance_id=slot.instance_id,
            target_stream_index=target_index,
        )
    if mechanism == "OP":
        return BuilderMetaPrior.from_policy(
            policy=state.meta_policy,
            checkpoint=state.checkpoint,
            registry=state.registry,
            target_instance_id=slot.instance_id,
            target_stream_index=target_index,
        )
    return BuilderMetaPrior.from_archive(
        archive=state.harness_archive,
        policy=state.meta_policy,
        checkpoint=state.checkpoint,
        registry=state.registry,
        target_instance_id=slot.instance_id,
        target_stream_index=target_index,
    )


def _decision_and_variant(mechanism: str) -> tuple[HarnessDecision, BuilderVariant]:
    decision = HarnessDecision.from_dict(
        {
            "schema_version": 1,
            "rule_id": "contract_compatibility",
            "role_graph": ["task_analyst", "generator", "verifier"],
            "memory_views": ["current"],
            "tools": ["task_semantics"],
            "parent_strategy": "reference",
            "workflow": ["analyze", "generate", "verify_contract"],
            "scheduler_mode": "single_candidate",
            "recovery_mode": "preserve_failure",
            "kernel_directive": "Respect the frozen public task contract.",
        }
    )
    variant = BuilderVariant(
        variant_id=f"factorial-online-{mechanism.lower()}",
        description=f"typed {mechanism} held-out fixture",
        freeze_after_initial=False,
        continual_update=mechanism != "O0",
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("contract_compatibility",),
        experience_sources=(),
        excluded_task_ids=(),
    )
    return decision, variant


def test_exact_sixteen_lanes_have_unique_trusted_roots_and_exact_slots() -> None:
    bundle = _bundle()

    assert bundle.execution_authority == "NOT_GRANTED"
    assert bundle.model_call_entitlement == 0
    assert bundle.evaluator_transaction_entitlement == 0
    assert len(bundle.lanes) == 16
    assert {
        (lane.benchmark_id, lane.seed, lane.mechanism_id)
        for lane in bundle.lanes
    } == {
        (benchmark, seed, mechanism)
        for benchmark in ("agenthpobench", "gdpevo")
        for seed in (2026081201, 2026081202)
        for mechanism in ("O0", "OM", "OP", "OA")
    }
    assert len({lane.trusted_relative_root for lane in bundle.lanes}) == 16
    for lane in bundle.lanes:
        assert lane.trusted_relative_root.startswith(
            f"factorial-online-lineage/{bundle.plan_sha256}/benchmarks/"
        )
        if lane.mechanism_id == "O0":
            assert lane.state_kind == "NONE"
            assert lane.source_update_slot_sha256s == ()
        else:
            slots = bundle.update_slots(lane)
            assert tuple(update_slot_sha256(item) for item in slots) == (
                lane.source_update_slot_sha256s
            )


def test_bundle_canonical_replay_rederives_plan_and_rejects_self_rehash() -> None:
    bundle = _bundle()
    assert (
        FactorialOnlineLineageBundle.from_bytes(
            bundle.canonical_bytes, expected_sha256=bundle.sha256
        )
        == bundle
    )

    payload = json.loads(bundle.canonical_bytes)
    payload["lanes"][0]["seed"] = 7
    forged = _canonical(payload)
    with pytest.raises(FactorialOnlineLineageError, match="replay differs"):
        FactorialOnlineLineageBundle.from_bytes(
            forged,
            expected_sha256=__import__("hashlib").sha256(forged).hexdigest(),
        )


@pytest.mark.parametrize(
    ("field", "value"),
    (
        ("benchmark_id", "gdpevo"),
        ("seed", 2026081202),
        ("mechanism_id", "OP"),
        ("source_update_slot_sha256s", ("f" * 64,)),
    ),
)
def test_lane_drift_cannot_enter_trusted_bundle(field: str, value: object) -> None:
    bundle = _bundle()
    lane = bundle.lane("agenthpobench", 2026081201, "OM")
    changes = {field: value}
    if field == "mechanism_id":
        changes["state_kind"] = "TYPED_VERSIONED_META_POLICY"
    drifted = replace(lane, **changes)
    with pytest.raises(FactorialOnlineLineageError):
        bundle.update_slots(drifted)


def test_applied_and_terminal_carry_forward_bind_exact_slot_and_operation() -> None:
    bundle = _bundle()
    applied = _first_update(bundle)
    assert applied.outcome == "APPLIED"
    assert applied.parent_state_sha256 != applied.output_state_sha256
    assert (
        OnlineUpdateLineageReceipt.from_bytes(
            applied.canonical_bytes, expected_sha256=applied.sha256
        )
        == applied
    )

    rejected = _first_update(bundle, outcome="CONTRACT_REJECTED")
    assert rejected.parent_state_sha256 == rejected.output_state_sha256
    assert (
        rejected.parent_checkpoint_sha256 == rejected.output_checkpoint_sha256
    )

    with pytest.raises(FactorialOnlineLineageError, match="source terminal"):
        replace(applied, source_terminal_receipt_sha256=ZERO_SHA256)
    with pytest.raises(FactorialOnlineLineageError, match="must change"):
        replace(
            applied,
            output_state_sha256=applied.parent_state_sha256,
            output_checkpoint_sha256=applied.parent_checkpoint_sha256,
        )
    with pytest.raises(FactorialOnlineLineageError, match="carry state"):
        replace(rejected, output_state_sha256="9" * 64)


def test_o0_has_audit_root_but_cannot_create_an_update() -> None:
    bundle = _bundle()
    lane = bundle.lane("agenthpobench", 2026081201, "O0")
    foreign_slot = bundle.update_slots(
        bundle.lane("agenthpobench", 2026081201, "OM")
    )[0]
    with pytest.raises(FactorialOnlineLineageError, match="O0 cannot"):
        bundle.create_update(
            lane=lane,
            slot=foreign_slot,
            source_terminal_receipt_sha256="1" * 64,
            parent_state_sha256="2" * 64,
            parent_checkpoint_sha256="3" * 64,
            output_state_sha256="4" * 64,
            output_checkpoint_sha256="5" * 64,
            operation_record_sha256="6" * 64,
            outcome="APPLIED",
            previous=None,
        )


def test_chain_rejects_cross_lane_slot_parent_and_ordinal() -> None:
    bundle = _bundle()
    lane = bundle.lane("agenthpobench", 2026081201, "OM")
    slots = bundle.update_slots(lane)
    first = _first_update(bundle)
    second = bundle.create_update(
        lane=lane,
        slot=slots[1],
        source_terminal_receipt_sha256="7" * 64,
        parent_state_sha256=first.output_state_sha256,
        parent_checkpoint_sha256=first.output_checkpoint_sha256,
        output_state_sha256="8" * 64,
        output_checkpoint_sha256="9" * 64,
        operation_record_sha256="a" * 64,
        outcome="APPLIED",
        previous=first,
    )
    assert bundle.replay_chain((first, second)) == (first, second)

    with pytest.raises(FactorialOnlineLineageError, match="slot/operation"):
        bundle.verify_update(
            replace(second, updater_operation_id=slots[0].updater_operation_id),
            previous=first,
        )
    with pytest.raises(FactorialOnlineLineageError, match="parent differs"):
        bundle.verify_update(
            replace(second, parent_state_sha256="b" * 64), previous=first
        )
    with pytest.raises(FactorialOnlineLineageError, match="parent differs"):
        bundle.verify_update(second, previous=_first_update(bundle, mechanism="OP"))
    with pytest.raises(FactorialOnlineLineageError, match="outside lane"):
        bundle.verify_update(replace(second, ordinal=99), previous=first)


def test_o0_heldout_binding_proves_zero_state_and_empty_cold_start() -> None:
    bundle = _bundle()
    lane = bundle.lane("agenthpobench", 2026081201, "O0")
    slot = bundle.heldout_slots(lane)[0]
    terminals = tuple(
        f"{index + 1:064x}"
        for index, _item in enumerate(bundle.source_final_slots(lane))
    )
    context = _context(
        slot=slot,
        stream_index=bundle.heldout_target_stream_index(lane, slot),
    )

    receipt = bundle.create_heldout_state_binding(
        lane=lane,
        slot=slot,
        context=context,
        source_terminal_receipt_sha256s=terminals,
        target_instance_descriptors=("optimization", "public-task"),
    )

    assert receipt.state_projection == "NONE"
    assert receipt.builder_meta_prior_sha256 == ZERO_SHA256
    assert receipt.final_checkpoint_sha256 == receipt.genesis_checkpoint_sha256
    assert (
        OnlineHeldoutStateBindingReceipt.from_bytes(
            receipt.canonical_bytes, expected_sha256=receipt.sha256
        )
        == receipt
    )
    with pytest.raises(FactorialOnlineLineageError, match="O0 forbids"):
        bundle.create_heldout_state_binding(
            lane=lane,
            slot=slot,
            context=context,
            source_terminal_receipt_sha256s=terminals,
            target_instance_descriptors=("optimization",),
            transitions=(object(),),  # type: ignore[arg-type]
        )


@pytest.mark.parametrize("mechanism", ("OM", "OP", "OA"))
def test_resolved_chain_rederives_prior_and_trusted_compile_projection(
    mechanism: str,
) -> None:
    bundle = _bundle()
    lane = bundle.lane("agenthpobench", 2026081201, mechanism)
    slot = bundle.heldout_slots(lane)[0]
    terminals = tuple(
        f"{index + 20:064x}"
        for index, _item in enumerate(bundle.source_final_slots(lane))
    )
    state, transitions = _state_and_transitions(
        bundle, lane=lane, terminal_hashes=terminals
    )
    target_index = bundle.heldout_target_stream_index(lane, slot)
    prior = _prior(
        mechanism=mechanism,
        state=state,
        slot=slot,
        target_index=target_index,
    )
    context = _context(slot=slot, stream_index=target_index, prior=prior)
    binding = bundle.create_heldout_state_binding(
        lane=lane,
        slot=slot,
        context=context,
        source_terminal_receipt_sha256s=terminals,
        target_instance_descriptors=("optimization", "public-task"),
        transitions=transitions,
        prior=prior,
    )
    decision, variant = _decision_and_variant(mechanism)
    projection = bundle.create_compile_projection(
        binding=binding,
        lane=lane,
        slot=slot,
        context=context,
        source_terminal_receipt_sha256s=terminals,
        target_instance_descriptors=("optimization", "public-task"),
        transitions=transitions,
        prior=prior,
        decision=decision,
        variant=variant,
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
    )

    assert projection.state_binding_receipt_sha256 == binding.sha256
    assert projection.builder_meta_prior_sha256 == prior.sha256
    assert projection.prior_direct_solution_injection is False
    assert (
        OnlineHeldoutCompileProjectionReceipt.from_bytes(
            projection.canonical_bytes, expected_sha256=projection.sha256
        )
        == projection
    )


def test_resolved_transition_rejects_forged_final_object_and_wrong_context_prior() -> None:
    bundle = _bundle()
    lane = bundle.lane("agenthpobench", 2026081201, "OP")
    slot = bundle.heldout_slots(lane)[0]
    terminals = tuple(
        f"{index + 30:064x}"
        for index, _item in enumerate(bundle.source_final_slots(lane))
    )
    state, transitions = _state_and_transitions(
        bundle, lane=lane, terminal_hashes=terminals
    )
    target_index = bundle.heldout_target_stream_index(lane, slot)
    prior = _prior(
        mechanism="OP",
        state=state,
        slot=slot,
        target_index=target_index,
    )
    wrong_context = _context(slot=slot, stream_index=target_index)
    with pytest.raises(FactorialOnlineLineageError, match="rederived mechanism prior"):
        bundle.create_heldout_state_binding(
            lane=lane,
            slot=slot,
            context=wrong_context,
            source_terminal_receipt_sha256s=terminals,
            target_instance_descriptors=("optimization",),
            transitions=transitions,
            prior=prior,
        )

    forged_policy = MetaPolicySnapshot.create(
        policy_id="foreign-policy",
        registry=state.registry,
    )
    with pytest.raises(FactorialOnlineLineageError, match="do not resolve"):
        ResolvedOnlineState(
            checkpoint=state.checkpoint,
            memory=state.memory,
            meta_policy=forged_policy,
            harness_archive=state.harness_archive,
            registry=state.registry,
        )


def test_heldout_cohort_requires_identical_source_terminal_evidence() -> None:
    bundle = _bundle()
    o0_lane = bundle.lane("agenthpobench", 2026081201, "O0")
    o0_slot = bundle.heldout_slots(o0_lane)[0]
    terminals = tuple(
        f"{index + 40:064x}"
        for index, _item in enumerate(bundle.source_final_slots(o0_lane))
    )
    o0 = bundle.create_heldout_state_binding(
        lane=o0_lane,
        slot=o0_slot,
        context=_context(
            slot=o0_slot,
            stream_index=bundle.heldout_target_stream_index(o0_lane, o0_slot),
        ),
        source_terminal_receipt_sha256s=terminals,
        target_instance_descriptors=("optimization", "public-task"),
    )
    receipts = [o0]
    for ordinal, mechanism in enumerate(("OM", "OP", "OA"), start=1):
        lane = bundle.lane("agenthpobench", 2026081201, mechanism)
        slot = bundle.heldout_slots(lane)[0]
        receipts.append(
            replace(
                o0,
                lane_binding_sha256=lane.sha256,
                mechanism_id=mechanism,
                state_kind=lane.state_kind,
                attempt_slot_sha256=attempt_slot_sha256(slot),
                builder_operation_id=slot.builder_operation_id,
                resolved_state_sha256=f"{ordinal + 60:064x}",
                final_checkpoint_sha256=f"{ordinal + 70:064x}",
                mechanism_state_sha256=f"{ordinal + 80:064x}",
                transition_receipt_sha256s=(f"{ordinal + 90:064x}",),
                transition_head_sha256=f"{ordinal + 90:064x}",
                builder_meta_prior_sha256=f"{ordinal + 100:064x}",
                planner_context_sha256=f"{ordinal + 110:064x}",
                context_binding_sha256=f"{ordinal + 120:064x}",
                state_projection="BUILDER_META_PRIOR",
            )
        )
    validate_heldout_state_binding_cohort(tuple(receipts))

    forged = replace(
        receipts[1],
        source_terminal_receipt_sha256s=("f" * 64,) + terminals[1:],
    )
    with pytest.raises(FactorialOnlineLineageError, match="fairness differs"):
        validate_heldout_state_binding_cohort(
            (receipts[0], forged, receipts[2], receipts[3])
        )


def test_compile_projection_replays_and_rejects_forged_state_binding() -> None:
    bundle = _bundle()
    lane = bundle.lane("agenthpobench", 2026081201, "O0")
    slot = bundle.heldout_slots(lane)[0]
    target_index = bundle.heldout_target_stream_index(lane, slot)
    terminals = tuple(
        f"{index + 50:064x}"
        for index, _item in enumerate(bundle.source_final_slots(lane))
    )
    context = _context(slot=slot, stream_index=target_index)
    binding = bundle.create_heldout_state_binding(
        lane=lane,
        slot=slot,
        context=context,
        source_terminal_receipt_sha256s=terminals,
        target_instance_descriptors=("optimization", "public-task"),
    )
    forged = replace(
        binding,
        source_terminal_receipt_sha256s=("e" * 64,) + terminals[1:],
    )
    decision, variant = _decision_and_variant("O0")

    with pytest.raises(FactorialOnlineLineageError, match="trusted replay"):
        bundle.create_compile_projection(
            binding=forged,
            lane=lane,
            slot=slot,
            context=context,
            source_terminal_receipt_sha256s=terminals,
            target_instance_descriptors=("optimization", "public-task"),
            decision=decision,
            variant=variant,
            operator_registry=TrustedOperatorRegistry(
                rule_registry_sha256="a" * 64
            ),
        )
