from __future__ import annotations

import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.builder_harness import BuilderHarness
from optimization_lab.harness_builder.champion_archive import (
    ChampionArchivePolicy,
    GateDecision,
    PortfolioEvolutionPolicy,
    harness_distance,
    retain_diverse_pareto,
)
from optimization_lab.harness_builder.dual_harness import (
    HarnessWorkspace,
    TaskHarnessArtifact,
    TaskHarnessSpec,
)
from test_builder_harness import SequenceGenerator
from test_dual_harness import artifact


CONTRACT = "d" * 64


def changed(
    parent: TaskHarnessArtifact,
    *,
    prompt: str,
    second_prompt: str | None = None,
) -> TaskHarnessArtifact:
    nodes = [node.to_dict() for node in parent.spec.nodes]
    nodes[0]["prompt"] = prompt
    if second_prompt is not None:
        nodes.insert(
            1,
            {
                "id": f"extra-{len(nodes)}",
                "kind": "model_call",
                "role": "critic",
                "prompt": second_prompt,
            },
        )
    return TaskHarnessArtifact(
        schema_version=1,
        version=parent.version + 1,
        parent_sha256=parent.sha256,
        spec=TaskHarnessSpec.from_dict({"schema_version": 1, "nodes": nodes}),
    )


def proposal(candidate: TaskHarnessArtifact) -> str:
    return json.dumps(
        {
            "schema_version": 1,
            "base_sha256": candidate.parent_sha256,
            "reason": "target the public failure",
            "expected_effect": "improve the external Gate score",
            "artifact": candidate.spec.to_dict(),
        }
    )


def gate(
    incumbent: TaskHarnessArtifact,
    candidate: TaskHarnessArtifact,
    *,
    utility: float,
    passed: bool = True,
    credible: bool = True,
    scores: tuple[tuple[str, float], ...] | None = None,
    failure_class: str | None = None,
) -> GateDecision:
    return GateDecision(
        evaluator_contract_sha256=CONTRACT,
        incumbent_sha256=incumbent.sha256,
        candidate_sha256=candidate.sha256,
        passed=passed,
        credible_improvement=credible,
        utility=utility,
        benchmark_scores=scores or (("bench-a", utility), ("bench-b", utility)),
        failure_class=failure_class,
        reason="credible improvement" if credible else "same correctness failure",
    )


def record_decision(
    workspace: HarnessWorkspace,
    *,
    proposal_id: str,
    candidate: TaskHarnessArtifact,
    attempt_index: int,
    mutation_family: str,
    decision: GateDecision,
    forced_restart: bool = False,
) -> None:
    workspace.store_artifact(candidate)
    workspace.record_archived_candidate(
        proposal_id=proposal_id,
        payload={
            "candidate_sha256": candidate.sha256,
            "parent_sha256": candidate.parent_sha256,
            "attempt_index": attempt_index,
            "mutation_family": mutation_family,
            "forced_restart": forced_restart,
        },
    )
    workspace.record_gate_decision(proposal_id=proposal_id, payload=decision.to_dict())


def test_source_schedule_is_exactly_60_30_10_when_pools_exist(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    incumbent = workspace.commit(artifact())
    pareto = changed(incumbent, prompt="Pareto {task}")
    record_decision(
        workspace,
        proposal_id="seed-pareto",
        candidate=pareto,
        attempt_index=0,
        mutation_family="failure_repair",
        decision=gate(incumbent, pareto, utility=1.0),
    )
    controller = ChampionArchivePolicy(
        workspace=workspace,
        evaluator_contract_sha256=CONTRACT,
    )

    sources = [
        controller.next_directive(attempt_index=index).source for index in range(10, 20)
    ]

    assert sources.count("champion") == 6
    assert sources.count("pareto") == 3
    assert sources.count("restart") == 1


def test_three_same_gate_failures_rotate_family_and_six_stagnant_force_restart(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    incumbent = workspace.commit(artifact())
    for index in range(6):
        candidate = changed(incumbent, prompt=f"Failure {index} {{task}}")
        record_decision(
            workspace,
            proposal_id=f"failure-{index}",
            candidate=candidate,
            attempt_index=index,
            mutation_family="failure_repair",
            decision=gate(
                incumbent,
                candidate,
                utility=0.0,
                passed=False,
                credible=False,
                failure_class="compile_error",
            ),
        )
    controller = ChampionArchivePolicy(
        workspace=workspace,
        evaluator_contract_sha256=CONTRACT,
    )

    directive = controller.next_directive(attempt_index=6)

    assert directive.mutation_family == "workflow_reorder"
    assert directive.forced_restart is True
    assert directive.source == "restart"
    assert directive.parent_sha256 == incumbent.sha256


def test_pareto_source_prefers_structurally_different_candidate(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    incumbent = workspace.commit(artifact())
    near = changed(incumbent, prompt="Near {task}")
    far = changed(incumbent, prompt="Far {task}", second_prompt="Critique {task}")
    record_decision(
        workspace,
        proposal_id="near",
        candidate=near,
        attempt_index=0,
        mutation_family="failure_repair",
        decision=gate(
            incumbent,
            near,
            utility=1.0,
            scores=(("bench-a", 2.0), ("bench-b", 1.0)),
        ),
    )
    record_decision(
        workspace,
        proposal_id="far",
        candidate=far,
        attempt_index=1,
        mutation_family="failure_repair",
        decision=gate(
            incumbent,
            far,
            utility=1.0,
            scores=(("bench-a", 1.0), ("bench-b", 2.0)),
        ),
    )
    controller = ChampionArchivePolicy(
        workspace=workspace,
        evaluator_contract_sha256=CONTRACT,
    )

    directive = controller.next_directive(attempt_index=11)

    assert directive.scheduled_source == "pareto"
    assert directive.parent_sha256 == far.sha256
    assert harness_distance(far.spec, incumbent.spec) > harness_distance(
        near.spec, incumbent.spec
    )
    retained = retain_diverse_pareto(
        workspace=workspace,
        evaluator_contract_sha256=CONTRACT,
        limit=2,
    )
    assert {item.sha256 for item in retained} == {near.sha256, far.sha256}


def test_builder_archives_all_candidates_and_promotes_only_gate_winner(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    incumbent = workspace.commit(artifact())
    first = changed(incumbent, prompt="Candidate one {task}")
    second = changed(first, prompt="Candidate two {task}")
    third = changed(incumbent, prompt="Candidate three {task}")
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(proposal(first), proposal(second), proposal(third)),
        model="builder-model",
    )
    utilities = {first.sha256: 1.0, second.sha256: 3.0, third.sha256: 2.0}

    result = builder.evolve_portfolio(
        run_id="portfolio-round",
        score=0.2,
        feedback="public compile failure",
        candidate_count=3,
        evaluator_contract_sha256=CONTRACT,
        gate_evaluator=lambda champion, candidate: gate(
            champion,
            candidate,
            utility=utilities[candidate.sha256],
        ),
    )

    assert result.previous_champion_sha256 == incumbent.sha256
    assert result.next_champion_sha256 == second.sha256
    assert result.promoted_proposal_id == "portfolio-round-candidate-002"
    assert len(workspace.archived_candidates()) == 3
    assert len(workspace.gate_decisions()) == 3
    assert workspace.load_artifact(first.sha256) == first
    assert workspace.load_artifact(third.sha256) == third
    receipt = workspace.load_promotion_receipt("portfolio-round")
    assert receipt["previous_champion_sha256"] == incumbent.sha256
    assert receipt["candidate_parent_sha256"] == first.sha256


def test_oversized_mutation_is_archived_neither_gated_nor_promoted(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    incumbent = workspace.commit(artifact())
    oversized = changed(
        incumbent,
        prompt="Changed once {task}",
        second_prompt="Changed twice {task}",
    )
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(proposal(oversized)),
        model="builder-model",
    )
    gate_calls: list[str] = []

    result = builder.evolve_portfolio(
        run_id="oversized-round",
        score=0.0,
        feedback="failure",
        candidate_count=1,
        evaluator_contract_sha256=CONTRACT,
        gate_evaluator=lambda champion, candidate: (
            gate_calls.append(candidate.sha256)
            or gate(champion, candidate, utility=1.0)
        ),
        policy=PortfolioEvolutionPolicy(max_changed_nodes=1),
    )

    assert result.candidates[0].status == "proposal_rejected"
    assert gate_calls == []
    assert workspace.archived_candidates() == ()
    assert workspace.champion().sha256 == incumbent.sha256


def test_portfolio_can_use_extra_proposals_to_fill_valid_candidate_target(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    incumbent = workspace.commit(artifact())
    candidate = changed(incumbent, prompt="Valid fallback {task}")
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator("not-json", proposal(candidate)),
        model="builder-model",
    )

    result = builder.evolve_portfolio(
        run_id="fill-round",
        score=0.0,
        feedback="format failure",
        candidate_count=1,
        proposal_attempt_limit=2,
        evaluator_contract_sha256=CONTRACT,
        gate_evaluator=lambda champion, challenger: gate(
            champion,
            challenger,
            utility=0.5,
            credible=False,
        ),
    )

    assert [item.status for item in result.candidates] == [
        "proposal_rejected",
        "archived",
    ]
    assert len(workspace.archived_candidates()) == 1


def test_owned_promotion_is_idempotent_and_recovers_pointer_update(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    incumbent = workspace.commit(artifact())
    candidate = changed(incumbent, prompt="Recovered {task}")
    record_decision(
        workspace,
        proposal_id="recover-candidate",
        candidate=candidate,
        attempt_index=0,
        mutation_family="failure_repair",
        decision=gate(incumbent, candidate, utility=2.0),
    )
    promoted = workspace.promote_archived_candidate(
        proposal_id="recover-candidate",
        owner_run_id="recover-round",
    )
    assert promoted.sha256 == candidate.sha256
    assert (
        workspace.promote_archived_candidate(
            proposal_id="recover-candidate",
            owner_run_id="recover-round",
        ).sha256
        == candidate.sha256
    )

    workspace._replace_json(workspace.current_path, {"sha256": incumbent.sha256})

    assert workspace.recover_owned_promotion("recover-round").sha256 == candidate.sha256
    assert workspace.champion().sha256 == candidate.sha256


def test_portfolio_rejects_non_contiguous_attempt_cursor_before_model_call(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    incumbent = workspace.commit(artifact())
    generator = SequenceGenerator(proposal(changed(incumbent, prompt="Unused {task}")))
    builder = BuilderHarness(
        workspace=workspace,
        generator=generator,
        model="builder-model",
    )

    with pytest.raises(ValueError, match="continue Gate history"):
        builder.evolve_portfolio(
            run_id="cursor-round",
            score=0.0,
            feedback="failure",
            candidate_count=1,
            evaluator_contract_sha256=CONTRACT,
            gate_evaluator=lambda champion, candidate: gate(
                champion, candidate, utility=1.0
            ),
            attempt_start=1,
        )

    assert generator.calls == []
