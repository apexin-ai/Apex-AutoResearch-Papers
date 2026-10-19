import json

import pytest

from optimization_lab.harness_builder.builder_evolution import (
    BuilderArchive,
    BuilderArtifact,
    BuilderBoundaryError,
    BuilderPublicState,
    BuilderScaffoldCompiler,
    SelfEvolvingBuilder,
    BuilderImpK,
    BuilderSelfModificationProposal,
    ImmutableBuilderController,
    MetaPolicy,
    TaskHarnessPolicy,
)


def _proposal(parent: BuilderArtifact, *, task_policy=None, meta_policy=None):
    task = task_policy or parent.task_harness_policy
    meta = meta_policy or parent.meta_policy
    before_meta = parent.meta_policy.to_dict()
    after_meta = meta.to_dict()
    changed = [key for key in before_meta if before_meta[key] != after_meta[key]]
    if task.to_dict() != parent.task_harness_policy.to_dict():
        changed.append("task_harness_policy")
    return json.dumps(
        {
            "schema_version": 1,
            "base_builder_sha256": parent.sha256,
            "changed_meta_components": changed,
            "reason": "use public failure history to avoid repeating a failed search family",
            "expected_effect": "more reliable improvement within the fixed opportunity budget",
            "meta_policy": meta.to_dict(),
            "task_harness_policy": task.to_dict(),
        }
    )


def test_initial_artifact_is_typed_and_converts_to_v1_decision():
    artifact = BuilderArtifact.initial()
    decision = artifact.task_harness_policy.to_harness_decision()
    assert artifact.parent_builder_sha256 is None
    assert decision.role_graph == ("task_analyst", "generator", "verifier")
    assert decision.rule_id == "discipline"
    assert decision.workflow[-1] == "verify_contract"


def test_self_modification_materializes_child_and_binds_parent():
    parent = BuilderArtifact.initial()
    policy = MetaPolicy.from_dict({**parent.meta_policy.to_dict(), "search_mode": "explore"})
    proposal = BuilderSelfModificationProposal.from_response(
        _proposal(parent, meta_policy=policy)
    )
    child = ImmutableBuilderController().materialize_child(
        parent, proposal, child_id="builder-v002"
    )
    assert child.parent_builder_sha256 == parent.sha256
    assert child.meta_policy.search_mode == "explore"
    assert child.sha256 != parent.sha256


def test_noop_proposal_is_rejected():
    parent = BuilderArtifact.initial()
    with pytest.raises(ValueError, match="changed meta components must be a non-empty list"):
        BuilderSelfModificationProposal.from_response(
            _proposal(parent, meta_policy=parent.meta_policy)
        )


def test_unknown_or_immutable_fields_cannot_enter_proposal():
    parent = BuilderArtifact.initial()
    raw = json.loads(_proposal(parent, meta_policy=MetaPolicy.from_dict({**parent.meta_policy.to_dict(), "search_mode": "explore"})))
    raw["changed_meta_components"] = ["evaluator"]
    with pytest.raises(ValueError, match="unknown changed meta components"):
        BuilderSelfModificationProposal.from_response(json.dumps(raw))


def test_parent_binding_is_fail_closed():
    parent = BuilderArtifact.initial()
    other = BuilderArtifact.initial("other-builder")
    meta = MetaPolicy.from_dict({**parent.meta_policy.to_dict(), "search_mode": "exploit"})
    raw = json.loads(_proposal(parent, meta_policy=meta))
    raw["base_builder_sha256"] = other.sha256
    proposal = BuilderSelfModificationProposal.from_response(json.dumps(raw))
    with pytest.raises(BuilderBoundaryError, match="current Builder parent"):
        ImmutableBuilderController().validate_proposal(parent, proposal)


def test_archive_is_content_addressed_and_replayable(tmp_path):
    archive = BuilderArchive(tmp_path / "archive")
    artifact = BuilderArtifact.initial()
    stored = archive.store(artifact)
    archive.set_head(artifact.sha256)
    assert stored.name == f"{artifact.sha256}.json"
    assert archive.load(artifact.sha256) == artifact
    assert archive.head() == artifact
    assert archive.hashes() == (artifact.sha256,)


def test_builder_imp_k_ignores_invalid_scores_and_uses_baseline_floor():
    artifact = BuilderArtifact.initial()
    result = BuilderImpK.from_scores(
        builder_sha256=artifact.sha256,
        baseline_score=0.4,
        scores=[None, 0.35, 0.55, float("nan"), 0.5],
        k=4,
    )
    assert result.valid_attempts == 2
    assert result.best_score == 0.55
    assert result.improvement == pytest.approx(0.15)


def test_task_policy_rejects_missing_required_generation_contract():
    payload = TaskHarnessPolicy.default().to_dict()
    payload["workflow"] = ["analyze", "generate"]
    with pytest.raises(ValueError, match="requires generate and verify_contract"):
        TaskHarnessPolicy.from_dict(payload)


def test_self_evolving_builder_accepts_child_and_advances_head(tmp_path):
    archive = BuilderArchive(tmp_path / "archive")
    builder = SelfEvolvingBuilder(archive=archive)
    parent = builder.current
    policy = MetaPolicy.from_dict({**parent.meta_policy.to_dict(), "search_mode": "exploit"})
    child, result = builder.evolve_from_response(
        _proposal(parent, meta_policy=policy), child_id="builder-v002"
    )
    assert result.status == "accepted"
    assert archive.head() == child
    assert child.parent_builder_sha256 == parent.sha256
    assert (archive.root / "transitions" / f"{child.sha256}.json").is_file()


def test_builder_scaffold_compiles_policy_into_executable_controls():
    parent = BuilderArtifact.initial()
    meta = MetaPolicy.from_dict(
        {
            **parent.meta_policy.to_dict(),
            "diagnostic_focus": ["failures", "score_trend", "reliability"],
            "memory_views": ["current", "failures"],
            "mutation_families": ["repair", "restart"],
            "search_mode": "exploit",
            "proposal_budget": 3,
            "failure_recovery": "repair",
        }
    )
    artifact = BuilderArtifact(
        schema_version=1,
        builder_id="builder-executable",
        parent_builder_sha256=parent.sha256,
        task_harness_policy=parent.task_harness_policy,
        meta_policy=meta,
    )
    state = BuilderPublicState(
        schema_version=1,
        task_id="suite:task-001",
        round_index=2,
        scores=(None, 0.4),
        feedback="contract format invalid",
        diagnostics={"failures": ["format"], "cost": {"calls": 2}},
        memory={"current": {"id": "v002"}, "failures": ["format"], "best": {"id": "v001"}},
    )

    compiled = BuilderScaffoldCompiler().compile(artifact, state)

    assert compiled.mutation_family == "repair"
    assert compiled.recovery_action == "repair"
    assert compiled.proposal_slots == (
        "proposal-001",
        "proposal-002",
        "proposal-003",
    )
    assert set(compiled.memory_projection) == {"current", "failures"}
    assert "cost" not in compiled.diagnostic_projection
    assert compiled.task_harness_decision["rule_id"] == "contract_compatibility"
    assert compiled.task_harness_decision["recovery_mode"] == "repair_then_reset"
    assert BuilderScaffoldCompiler().compile(artifact, state).sha256 == compiled.sha256


def test_builder_scaffold_reset_changes_lower_harness_architecture():
    parent = BuilderArtifact.initial()
    artifact = BuilderArtifact(
        schema_version=1,
        builder_id="builder-reset",
        parent_builder_sha256=parent.sha256,
        task_harness_policy=parent.task_harness_policy,
        meta_policy=MetaPolicy.from_dict(
            {
                **parent.meta_policy.to_dict(),
                "mutation_families": ["restart"],
                "failure_recovery": "reset",
            }
        ),
    )
    state = BuilderPublicState(
        schema_version=1,
        task_id="suite:task-001",
        round_index=3,
        scores=(0.5, None),
        feedback="incorrect candidate",
        diagnostics={},
        memory={},
    )

    decision = BuilderScaffoldCompiler().compile(artifact, state).harness_decision()

    assert decision.rule_id == "dream"
    assert decision.parent_strategy == "restart"
    assert decision.recovery_mode == "reset_immediately"


def test_next_builder_process_loads_child_head_and_compiles_its_scaffold(tmp_path):
    archive = BuilderArchive(tmp_path / "archive")
    first = SelfEvolvingBuilder(archive=archive)
    parent = first.current
    task_policy = TaskHarnessPolicy.from_dict(
        {
            **parent.task_harness_policy.to_dict(),
            "role_graph": ["task_analyst", "critic", "generator", "verifier"],
            "workflow": ["analyze", "criticize", "generate", "verify_contract"],
            "execution_mode": "multi_step",
        }
    )
    child, result = first.evolve_from_response(
        _proposal(parent, task_policy=task_policy), child_id="builder-v002"
    )
    assert result.status == "accepted"

    next_task_builder = SelfEvolvingBuilder(archive=archive)
    compiled = next_task_builder.compile_current(
        BuilderPublicState(
            schema_version=1,
            task_id="suite:next-task",
            round_index=1,
            scores=(0.4,),
            feedback="valid",
            diagnostics={},
            memory={},
        )
    )

    assert next_task_builder.current.sha256 == child.sha256
    assert compiled.builder_sha256 == child.sha256
    assert compiled.harness_decision().role_graph == task_policy.role_graph
    assert compiled.harness_decision().workflow == task_policy.workflow
