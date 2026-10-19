from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.meta_evolution import (
    COMPONENT_AXES,
    HarnessArchiveNode,
    HarnessArchiveSnapshot,
    MetaCheckpointV2,
    MetaPolicySnapshot,
    MetaUpdateProposal,
    TrustedMetaPolicyRegistry,
    validate_archive_transition,
    validate_memory_transition,
)
from optimization_lab.harness_builder.experience import ExperienceRecord
from optimization_lab.harness_builder.learning import ExperienceBankSnapshot


def _selection(**overrides: tuple[str, ...]) -> dict[str, tuple[str, ...]]:
    result = {
        "role_graph": ("task_analyst", "generator", "verifier"),
        "memory_views": ("current", "best"),
        "tools": ("task_semantics", "score_history"),
        "parent_strategy": ("incumbent",),
        "workflow": ("analyze", "select_parent", "generate", "verify_contract"),
        "scheduler_mode": ("single_candidate",),
        "recovery_mode": ("repair_then_reset",),
    }
    result.update(overrides)
    return result


def _metrics(
    *, quality: float = 0.6, novelty: float = 0.4, recovery: float = 0.5
) -> dict[str, float]:
    return {
        "quality": quality,
        "novelty": novelty,
        "recovery": recovery,
        "efficiency": 0.7,
    }


def _policy(
    registry: TrustedMetaPolicyRegistry,
    *,
    policy_id: str = "policy-v001",
    parent_sha256: str | None = None,
    selection_mode: str = "weighted_rank_v1",
    retrieval_limit: int = 4,
) -> MetaPolicySnapshot:
    return MetaPolicySnapshot.create(
        policy_id=policy_id,
        registry=registry,
        parent_sha256=parent_sha256,
        selection_mode=selection_mode,
        retrieval_limit=retrieval_limit,
        candidate_pool_limit=8,
    )


def _node(
    registry: TrustedMetaPolicyRegistry,
    *,
    node_id: str = "node-v001",
    source_stream_index: int = 0,
    parent_node_sha256: str | None = None,
    metrics: dict[str, float] | None = None,
    selection: dict[str, tuple[str, ...]] | None = None,
) -> HarnessArchiveNode:
    return HarnessArchiveNode.create(
        node_id=node_id,
        registry=registry,
        source_suite="suite-a",
        source_instance_id=f"suite-a:task-{source_stream_index}",
        source_stream_index=source_stream_index,
        harness_decision_sha256=hex(source_stream_index + 1)[2:] * 64,
        component_selection=_selection() if selection is None else selection,
        metrics=_metrics() if metrics is None else metrics,
        provenance_event_ids=(f"event-{node_id}",),
        parent_node_sha256=parent_node_sha256,
    )


def _genesis(
    registry: TrustedMetaPolicyRegistry,
    *,
    memory_sha256: str = "a" * 64,
    policy_sha256: str = "b" * 64,
    archive_sha256: str = "c" * 64,
) -> MetaCheckpointV2:
    return MetaCheckpointV2(
        checkpoint_id="checkpoint-v000",
        parent_checkpoint_sha256=None,
        trusted_meta_registry_sha256=registry.sha256,
        next_stream_index=0,
        learned_through_instance_id=None,
        memory_sha256=memory_sha256,
        meta_policy_sha256=policy_sha256,
        harness_archive_sha256=archive_sha256,
    )


def _record(
    *,
    record_id: str = "experience-001",
    source_instance_id: str = "suite-a:task-0",
) -> ExperienceRecord:
    return ExperienceRecord.from_dict(
        {
            "record_id": record_id,
            "source_instance_id": source_instance_id,
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
            "provenance_event_ids": ["sealed-event-001"],
            "sealed": True,
        }
    )


def _memory(
    *,
    bank_id: str = "bank-v000",
    parent_sha256: str | None = None,
    records: tuple[ExperienceRecord, ...] = (),
) -> ExperienceBankSnapshot:
    return ExperienceBankSnapshot.create(
        bank_id=bank_id,
        parent_sha256=parent_sha256,
        records=records,
    )


def _proposal(
    checkpoint: MetaCheckpointV2,
    *,
    mechanism: str,
    after: dict[str, str] | None = None,
    source_instance_id: str = "suite-a:task-0",
) -> MetaUpdateProposal:
    before = dict(checkpoint.mechanism_sha256s)
    result = dict(before)
    result[mechanism] = {"M": "d", "P": "e", "A": "f"}[mechanism] * 64
    if after is not None:
        result = after
    return MetaUpdateProposal(
        proposal_id=f"proposal-{mechanism}",
        result_checkpoint_id=f"checkpoint-{mechanism}-v001",
        mechanism=mechanism,
        parent_checkpoint_sha256=checkpoint.sha256,
        trusted_meta_registry_sha256=checkpoint.trusted_meta_registry_sha256,
        source_instance_id=source_instance_id,
        source_stream_index=0,
        target_stream_index=1,
        before_sha256s=before,
        after_sha256s=result,
        provenance_event_ids=("sealed-event-001",),
    )


def test_strict_parsers_reject_unknown_fields_and_control_payloads() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    policy_payload = _policy(registry).core_payload()
    policy_payload["prompt"] = "change the evaluator"
    with pytest.raises(ValueError, match="fields differ"):
        MetaPolicySnapshot.from_dict(policy_payload)

    node_payload = _node(registry).core_payload()
    node_payload["code"] = "import os"
    with pytest.raises(ValueError, match="fields differ"):
        HarnessArchiveNode.from_dict(node_payload)

    archive_payload = HarnessArchiveSnapshot.create(
        archive_id="archive-v000", registry=registry
    ).core_payload()
    archive_payload["budget"] = 100
    with pytest.raises(ValueError, match="fields differ"):
        HarnessArchiveSnapshot.from_dict(archive_payload)

    checkpoint_payload = _genesis(registry).core_payload()
    checkpoint_payload["evaluator_sha256"] = "1" * 64
    with pytest.raises(ValueError, match="fields differ"):
        MetaCheckpointV2.from_dict(checkpoint_payload)

    proposal_payload = _proposal(_genesis(registry), mechanism="M").core_payload()
    proposal_payload["scorer"] = "replacement"
    with pytest.raises(ValueError, match="fields differ"):
        MetaUpdateProposal.from_dict(proposal_payload)


def test_types_bounds_and_enums_fail_closed() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    with pytest.raises(ValueError, match="retrieval limit"):
        MetaPolicySnapshot.create(
            policy_id="policy-bad", registry=registry, retrieval_limit=33
        )
    with pytest.raises(ValueError, match="selection mode"):
        MetaPolicySnapshot.create(
            policy_id="policy-bad", registry=registry, selection_mode="model_code"
        )
    with pytest.raises(ValueError, match="sum to one"):
        MetaPolicySnapshot.create(
            policy_id="policy-bad",
            registry=registry,
            objective_weights={
                "quality": 1.0,
                "novelty": 1.0,
                "recovery": 0.0,
                "efficiency": 0.0,
            },
        )
    with pytest.raises(ValueError, match="finite"):
        _node(registry, metrics=_metrics(quality=float("nan")))
    with pytest.raises(ValueError, match="source stream index"):
        _node(registry, source_stream_index=-1)
    with pytest.raises(ValueError, match="mechanism"):
        MetaUpdateProposal(
            proposal_id="bad-mechanism",
            result_checkpoint_id="checkpoint-bad",
            mechanism="X",
            parent_checkpoint_sha256="1" * 64,
            trusted_meta_registry_sha256=registry.sha256,
            source_instance_id="suite-a:task-0",
            source_stream_index=0,
            target_stream_index=1,
            before_sha256s={"M": "a" * 64, "P": "b" * 64, "A": "c" * 64},
            after_sha256s={"M": "d" * 64, "P": "b" * 64, "A": "c" * 64},
            provenance_event_ids=("event-1",),
        )


def test_registry_rejects_unknown_and_forbidden_components() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    with pytest.raises(ValueError, match="unknown trusted component"):
        _node(registry, selection=_selection(tools=("shell_plugin",)))

    forbidden = dict(registry.components)
    forbidden["tools"] = forbidden["tools"] + ("generated_code",)
    with pytest.raises(ValueError, match="attempts to control"):
        TrustedMetaPolicyRegistry(forbidden)

    candidates = dict(registry.components)
    candidates["workflow"] = candidates["workflow"] + ("replacement_prompt",)
    with pytest.raises(ValueError, match="attempts to control"):
        MetaPolicySnapshot.create(
            policy_id="policy-forbidden",
            registry=registry,
            component_candidates=candidates,
        )


def test_objects_are_canonical_content_addressed_and_write_once(tmp_path: Path) -> None:
    registry = TrustedMetaPolicyRegistry.default()
    policy = _policy(registry)
    encoded = policy.canonical_bytes
    assert encoded.endswith(b"\n")
    assert json.loads(encoded) == policy.core_payload()
    assert MetaPolicySnapshot.from_dict(json.loads(encoded)).sha256 == policy.sha256

    path = policy.store(tmp_path / "policies")
    assert path.name == f"{policy.sha256}.json"
    assert policy.store(tmp_path / "policies") == path
    path.write_bytes(b"tampered\n")
    with pytest.raises(ValueError, match="overwrite"):
        policy.store(tmp_path / "policies")


@pytest.mark.parametrize(
    "object_factory",
    (
        lambda registry: registry,
        lambda registry: _policy(registry),
        lambda registry: HarnessArchiveSnapshot.create(
            archive_id="archive-load", registry=registry
        ),
        lambda registry: _genesis(registry),
        lambda registry: _proposal(_genesis(registry), mechanism="M"),
    ),
)
def test_typed_load_requires_canonical_digest_bound_regular_file(
    tmp_path: Path, object_factory
) -> None:
    registry = TrustedMetaPolicyRegistry.default()
    item = object_factory(registry)
    path = item.store(tmp_path / "objects")
    loaded = type(item).load(path, expected_sha256=item.sha256)
    assert loaded.canonical_bytes == item.canonical_bytes

    pretty = json.dumps(item.core_payload(), indent=2, sort_keys=True).encode()
    noncanonical_sha = hashlib.sha256(pretty).hexdigest()
    noncanonical = tmp_path / "objects" / f"{noncanonical_sha}.json"
    noncanonical.write_bytes(pretty)
    with pytest.raises(ValueError, match="not canonical"):
        type(item).load(noncanonical, expected_sha256=noncanonical_sha)


def test_typed_load_rejects_wrong_name_hash_and_symlinks(tmp_path: Path) -> None:
    registry = TrustedMetaPolicyRegistry.default()
    policy = _policy(registry)
    root = tmp_path / "objects"
    path = policy.store(root)
    with pytest.raises(ValueError, match="filename"):
        MetaPolicySnapshot.load(path, expected_sha256="9" * 64)

    link = tmp_path / f"{policy.sha256}.json"
    link.symlink_to(path)
    with pytest.raises(ValueError, match="missing or unsafe"):
        MetaPolicySnapshot.load(link, expected_sha256=policy.sha256)

    linked_parent = tmp_path / "linked-parent"
    linked_parent.symlink_to(root, target_is_directory=True)
    with pytest.raises(ValueError, match="missing or unsafe"):
        MetaPolicySnapshot.load(
            linked_parent / path.name,
            expected_sha256=policy.sha256,
        )


def test_meta_policy_archive_and_checkpoint_parent_chains() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    parent_policy = _policy(registry)
    child_policy = MetaPolicySnapshot.create(
        policy_id="policy-v002",
        registry=registry,
        parent_sha256=parent_policy.sha256,
        selection_mode="failure_directed_v1",
    )
    registry.validate_policy_transition(parent_policy, child_policy)
    wrong_parent = MetaPolicySnapshot.create(
        policy_id="policy-v003",
        registry=registry,
        parent_sha256="9" * 64,
        selection_mode="pareto_diverse_v1",
    )
    with pytest.raises(ValueError, match="parent chain"):
        registry.validate_policy_transition(parent_policy, wrong_parent)

    empty = HarnessArchiveSnapshot.create(archive_id="archive-v000", registry=registry)
    root = _node(registry)
    first = empty.extend(root, archive_id="archive-v001", registry=registry)
    assert first.parent_sha256 == empty.sha256
    child = _node(
        registry,
        node_id="node-v002",
        source_stream_index=1,
        parent_node_sha256=root.sha256,
    )
    second = first.extend(child, archive_id="archive-v002", registry=registry)
    assert second.parent_sha256 == first.sha256
    orphan = _node(
        registry,
        node_id="node-orphan",
        source_stream_index=2,
        parent_node_sha256="8" * 64,
    )
    with pytest.raises(ValueError, match="existing parent"):
        second.extend(orphan, archive_id="archive-bad", registry=registry)

    checkpoint = _genesis(
        registry,
        policy_sha256=parent_policy.sha256,
        archive_sha256=empty.sha256,
    )
    next_checkpoint = checkpoint.apply(
        _proposal(checkpoint, mechanism="M"),
        sealed_source_instance_ids=("suite-a:task-0",),
    )
    assert next_checkpoint.parent_checkpoint_sha256 == checkpoint.sha256
    assert next_checkpoint.next_stream_index == 1


def test_selection_is_deterministic_and_excludes_current_or_future_nodes() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    policy = _policy(registry, selection_mode="pareto_diverse_v1", retrieval_limit=2)
    root = _node(
        registry,
        node_id="node-alpha",
        source_stream_index=0,
        metrics=_metrics(quality=0.8, novelty=0.2),
    )
    peer = _node(
        registry,
        node_id="node-beta",
        source_stream_index=0,
        parent_node_sha256=root.sha256,
        selection=_selection(parent_strategy=("stable_best",)),
        metrics=_metrics(quality=0.8, novelty=0.8),
    )
    future = _node(
        registry,
        node_id="node-later-index",
        source_stream_index=2,
        parent_node_sha256=peer.sha256,
        metrics=_metrics(quality=1.0, novelty=1.0),
    )
    archive = HarnessArchiveSnapshot.create(
        archive_id="archive-selection",
        registry=registry,
        nodes=(root, peer, future),
    )
    first = registry.select_nodes(
        policy=policy, archive=archive, target_stream_index=2
    )
    second = registry.select_nodes(
        policy=policy, archive=archive, target_stream_index=2
    )
    assert tuple(item.sha256 for item in first) == tuple(item.sha256 for item in second)
    assert {item.node_id for item in first} == {"node-alpha", "node-beta"}
    assert all(item.source_stream_index < 2 for item in first)


def test_private_and_future_identifiers_are_rejected() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    with pytest.raises(ValueError, match="private or future"):
        MetaPolicySnapshot.create(policy_id="future:policy", registry=registry)
    with pytest.raises(ValueError, match="private or future"):
        HarnessArchiveNode.create(
            node_id="node-private",
            registry=registry,
            source_suite="suite-a",
            source_instance_id="suite-a:hidden-task",
            source_stream_index=0,
            harness_decision_sha256="1" * 64,
            component_selection=_selection(),
            metrics=_metrics(),
            provenance_event_ids=("event-1",),
        )
    with pytest.raises(ValueError, match="private or future"):
        _proposal(
            _genesis(registry), mechanism="M", source_instance_id="suite-a:private-task"
        )


@pytest.mark.parametrize("mechanism", ("M", "P", "A"))
def test_m_p_a_updates_are_mechanically_isolated(mechanism: str) -> None:
    registry = TrustedMetaPolicyRegistry.default()
    checkpoint = _genesis(registry)
    proposal = _proposal(checkpoint, mechanism=mechanism)
    result = checkpoint.apply(
        proposal, sealed_source_instance_ids=("suite-a:task-0",)
    )
    changed = {
        axis
        for axis in ("M", "P", "A")
        if result.mechanism_sha256s[axis] != checkpoint.mechanism_sha256s[axis]
    }
    assert changed == {mechanism}

    after = dict(checkpoint.mechanism_sha256s)
    after[mechanism] = "7" * 64
    other = next(axis for axis in ("M", "P", "A") if axis != mechanism)
    after[other] = "8" * 64
    with pytest.raises(ValueError, match="exactly its declared"):
        _proposal(checkpoint, mechanism=mechanism, after=after)


def test_update_requires_sealed_immediately_prior_source() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    checkpoint = _genesis(registry)
    proposal = _proposal(checkpoint, mechanism="A")
    with pytest.raises(ValueError, match="not a sealed"):
        checkpoint.apply(proposal, sealed_source_instance_ids=("suite-a:other",))

    wrong_parent = MetaUpdateProposal(
        proposal_id="proposal-wrong-parent",
        result_checkpoint_id="checkpoint-wrong-parent",
        mechanism="A",
        parent_checkpoint_sha256="9" * 64,
        trusted_meta_registry_sha256=registry.sha256,
        source_instance_id="suite-a:task-0",
        source_stream_index=0,
        target_stream_index=1,
        before_sha256s=checkpoint.mechanism_sha256s,
        after_sha256s={
            **checkpoint.mechanism_sha256s,
            "A": "f" * 64,
        },
        provenance_event_ids=("event-1",),
    )
    with pytest.raises(ValueError, match="parent checkpoint"):
        checkpoint.apply(
            wrong_parent, sealed_source_instance_ids=("suite-a:task-0",)
        )


def test_verified_update_rejects_an_invented_unresolved_hash() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    policy = _policy(registry)
    memory = _memory()
    archive = HarnessArchiveSnapshot.create(
        archive_id="archive-v000", registry=registry
    )
    checkpoint = _genesis(
        registry,
        memory_sha256=memory.sha256,
        policy_sha256=policy.sha256,
        archive_sha256=archive.sha256,
    )
    proposal = _proposal(checkpoint, mechanism="P")
    with pytest.raises(ValueError, match="do not resolve"):
        checkpoint.apply_verified(
            proposal,
            sealed_source_instance_ids=("suite-a:task-0",),
            parent_memory=memory,
            memory=memory,
            parent_meta_policy=policy,
            meta_policy=policy,
            parent_harness_archive=archive,
            harness_archive=archive,
            registry=registry,
        )

    next_policy = MetaPolicySnapshot.create(
        policy_id="policy-v002",
        registry=registry,
        parent_sha256=policy.sha256,
        selection_mode="failure_directed_v1",
    )
    before = dict(checkpoint.mechanism_sha256s)
    after = {**before, "P": next_policy.sha256}
    valid = _proposal(checkpoint, mechanism="P", after=after)
    result = checkpoint.apply_verified(
        valid,
        sealed_source_instance_ids=("suite-a:task-0",),
        parent_memory=memory,
        memory=memory,
        parent_meta_policy=policy,
        meta_policy=next_policy,
        parent_harness_archive=archive,
        harness_archive=archive,
        registry=registry,
    )
    assert result.meta_policy_sha256 == next_policy.sha256


def test_verified_policy_update_requires_exact_parent_policy() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    parent_policy = _policy(registry)
    memory = _memory()
    archive = HarnessArchiveSnapshot.create(archive_id="archive-v000", registry=registry)
    checkpoint = _genesis(
        registry,
        memory_sha256=memory.sha256,
        policy_sha256=parent_policy.sha256,
        archive_sha256=archive.sha256,
    )
    wrong_parent = MetaPolicySnapshot.create(
        policy_id="policy-wrong-parent",
        registry=registry,
        parent_sha256="9" * 64,
        selection_mode="failure_directed_v1",
    )
    proposal = _proposal(
        checkpoint,
        mechanism="P",
        after={**checkpoint.mechanism_sha256s, "P": wrong_parent.sha256},
    )
    with pytest.raises(ValueError, match="meta-policy parent chain"):
        checkpoint.apply_verified(
            proposal,
            sealed_source_instance_ids=("suite-a:task-0",),
            parent_memory=memory,
            memory=memory,
            parent_meta_policy=parent_policy,
            meta_policy=wrong_parent,
            parent_harness_archive=archive,
            harness_archive=archive,
            registry=registry,
        )


def test_verified_archive_update_rejects_foreign_appended_source() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    policy = _policy(registry)
    memory = _memory()
    root = _node(registry, node_id="node-root", source_stream_index=0)
    parent = HarnessArchiveSnapshot.create(
        archive_id="archive-parent", registry=registry, nodes=(root,)
    )
    checkpoint = _genesis(
        registry,
        memory_sha256=memory.sha256,
        policy_sha256=policy.sha256,
        archive_sha256=parent.sha256,
    )
    foreign = _node(
        registry,
        node_id="node-foreign",
        source_stream_index=0,
        parent_node_sha256=root.sha256,
    )
    object.__setattr__(foreign, "source_instance_id", "suite-a:other")
    child = HarnessArchiveSnapshot.create(
        archive_id="archive-foreign",
        parent_sha256=parent.sha256,
        registry=registry,
        nodes=parent.nodes + (foreign,),
    )
    proposal = _proposal(
        checkpoint,
        mechanism="A",
        after={**checkpoint.mechanism_sha256s, "A": child.sha256},
    )
    with pytest.raises(ValueError, match="foreign source"):
        checkpoint.apply_verified(
            proposal,
            sealed_source_instance_ids=("suite-a:task-0",),
            parent_memory=memory,
            memory=memory,
            parent_meta_policy=policy,
            meta_policy=policy,
            parent_harness_archive=parent,
            harness_archive=child,
            registry=registry,
        )


def test_verified_memory_update_rejects_foreign_appended_source() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    policy = _policy(registry)
    parent_memory = _memory()
    foreign = _record(source_instance_id="suite-a:other")
    memory = _memory(
        bank_id="bank-v001",
        parent_sha256=parent_memory.sha256,
        records=(foreign,),
    )
    archive = HarnessArchiveSnapshot.create(archive_id="archive-v000", registry=registry)
    checkpoint = _genesis(
        registry,
        memory_sha256=parent_memory.sha256,
        policy_sha256=policy.sha256,
        archive_sha256=archive.sha256,
    )
    proposal = _proposal(
        checkpoint,
        mechanism="M",
        after={**checkpoint.mechanism_sha256s, "M": memory.sha256},
    )
    with pytest.raises(ValueError, match="foreign source"):
        checkpoint.apply_verified(
            proposal,
            sealed_source_instance_ids=("suite-a:task-0",),
            parent_memory=parent_memory,
            memory=memory,
            parent_meta_policy=policy,
            meta_policy=policy,
            parent_harness_archive=archive,
            harness_archive=archive,
            registry=registry,
        )


def test_archive_transition_requires_exact_prefix_one_current_node_and_parent() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    root = _node(registry, node_id="node-root", source_stream_index=0)
    parent = HarnessArchiveSnapshot.create(
        archive_id="archive-parent", registry=registry, nodes=(root,)
    )
    checkpoint = _genesis(registry, archive_sha256=parent.sha256)
    appended = _node(
        registry,
        node_id="node-current",
        source_stream_index=0,
        parent_node_sha256=root.sha256,
    )
    child = parent.extend(appended, archive_id="archive-child", registry=registry)
    proposal = _proposal(
        checkpoint,
        mechanism="A",
        after={**checkpoint.mechanism_sha256s, "A": child.sha256},
    )
    validate_archive_transition(parent, child, proposal=proposal, registry=registry)

    wrong_parent = HarnessArchiveSnapshot.create(
        archive_id="archive-wrong-parent",
        parent_sha256="9" * 64,
        registry=registry,
        nodes=child.nodes,
    )
    with pytest.raises(ValueError, match="parent chain"):
        validate_archive_transition(
            parent, wrong_parent, proposal=proposal, registry=registry
        )

    foreign = _node(
        registry,
        node_id="node-foreign",
        source_stream_index=0,
        parent_node_sha256=root.sha256,
    )
    object.__setattr__(foreign, "source_instance_id", "suite-a:other")
    foreign_child = HarnessArchiveSnapshot.create(
        archive_id="archive-foreign",
        parent_sha256=parent.sha256,
        registry=registry,
        nodes=parent.nodes + (foreign,),
    )
    with pytest.raises(ValueError, match="foreign source"):
        validate_archive_transition(
            parent, foreign_child, proposal=proposal, registry=registry
        )

    extra = _node(
        registry,
        node_id="node-extra",
        source_stream_index=0,
        parent_node_sha256=appended.sha256,
    )
    two_nodes = HarnessArchiveSnapshot.create(
        archive_id="archive-two-nodes",
        parent_sha256=parent.sha256,
        registry=registry,
        nodes=parent.nodes + (appended, extra),
    )
    with pytest.raises(ValueError, match="exactly one"):
        validate_archive_transition(
            parent, two_nodes, proposal=proposal, registry=registry
        )


def test_memory_transition_requires_exact_prefix_parent_and_current_source() -> None:
    original = _record(record_id="experience-parent", source_instance_id="suite-a:old")
    parent = _memory(records=(original,))
    current = _record(record_id="experience-current")
    child = _memory(
        bank_id="bank-v001",
        parent_sha256=parent.sha256,
        records=parent.records + (current,),
    )
    validate_memory_transition(
        parent, child, source_instance_id="suite-a:task-0"
    )

    wrong_parent = _memory(
        bank_id="bank-wrong-parent",
        parent_sha256="9" * 64,
        records=parent.records + (current,),
    )
    with pytest.raises(ValueError, match="parent chain"):
        validate_memory_transition(
            parent, wrong_parent, source_instance_id="suite-a:task-0"
        )

    foreign = _record(
        record_id="experience-foreign", source_instance_id="suite-a:other"
    )
    foreign_child = _memory(
        bank_id="bank-foreign",
        parent_sha256=parent.sha256,
        records=parent.records + (foreign,),
    )
    with pytest.raises(ValueError, match="foreign source"):
        validate_memory_transition(
            parent, foreign_child, source_instance_id="suite-a:task-0"
        )

    nonfinite = _record(record_id="experience-nonfinite")
    object.__setattr__(nonfinite, "outcome_delta", float("inf"))
    nonfinite_child = _memory(
        bank_id="bank-nonfinite",
        parent_sha256=parent.sha256,
        records=parent.records + (nonfinite,),
    )
    with pytest.raises(ValueError, match="finite"):
        validate_memory_transition(
            parent, nonfinite_child, source_instance_id="suite-a:task-0"
        )

    replaced_prefix = _memory(
        bank_id="bank-replaced",
        parent_sha256=parent.sha256,
        records=(
            _record(record_id="experience-replaced", source_instance_id="suite-a:old"),
            current,
        ),
    )
    with pytest.raises(ValueError, match="exact parent prefix"):
        validate_memory_transition(
            parent, replaced_prefix, source_instance_id="suite-a:task-0"
        )


def test_every_component_axis_is_present_in_registry_and_objects() -> None:
    registry = TrustedMetaPolicyRegistry.default()
    assert tuple(registry.components) == COMPONENT_AXES
    assert tuple(_selection()) == COMPONENT_AXES
