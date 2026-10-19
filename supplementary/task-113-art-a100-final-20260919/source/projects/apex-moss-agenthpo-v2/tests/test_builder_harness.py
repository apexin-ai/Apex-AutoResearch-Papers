from __future__ import annotations

import json
from pathlib import Path

import pytest

from optimization_lab.generation import GenerationResult
from optimization_lab.harness_builder.builder_harness import BuilderHarness, BuilderHarnessSpec
from optimization_lab.harness_builder.dual_harness import HarnessWorkspace
from optimization_lab.harness_builder.experiment_one_audit import (
    experiment_one_builder_view,
)
from test_dual_harness import artifact


class SequenceGenerator:
    def __init__(self, *responses: str) -> None:
        self.responses = list(responses)
        self.calls: list[tuple[str, str]] = []

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append((prompt, model))
        return GenerationResult(raw_response=self.responses.pop(0), provider="fixture")


def proposal(base_sha256: str, *, nodes: list[dict[str, object]] | None = None) -> str:
    current = artifact()
    payload = json.loads(current.to_json())
    if nodes is None:
        payload["spec"]["nodes"][0]["prompt"] = "Inspect failures in {task}"
    else:
        payload["spec"]["nodes"] = nodes
    return json.dumps(
        {
            "schema_version": 1,
            "base_sha256": base_sha256,
            "reason": "add verification",
            "expected_effect": "fewer invalid candidates",
            "artifact": payload["spec"],
        }
    )


def branch_proposal(source_sha256: str, *, prompt: str) -> str:
    current = artifact()
    payload = json.loads(current.to_json())
    payload["spec"]["nodes"][0]["prompt"] = prompt
    return json.dumps(
        {
            "schema_version": 2,
            "source_sha256": source_sha256,
            "base_sha256": source_sha256,
            "reason": "restart from a stable historical Harness",
            "expected_effect": "recover a known-good execution path",
            "artifact": payload["spec"],
        }
    )


def test_builder_inspects_trace_proposes_and_commits(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    workspace.record_trace(
        run_id="round-1",
        harness_sha256=current.sha256,
        candidate="candidate-v1",
        task_sha256="a" * 64,
        request_sha256="e" * 64,
        solver_model="solver-model",
        events=(),
        score=0.2,
        feedback="invalid",
    )
    generator = SequenceGenerator(proposal(current.sha256))
    builder = BuilderHarness(workspace=workspace, generator=generator, model="builder-model")

    result = builder.evolve_once(score=0.2, feedback="invalid")

    assert result.status == "committed"
    assert workspace.current().version == 2
    assert workspace.current().parent_sha256 == current.sha256
    assert "invalid" in generator.calls[0][0]
    assert generator.calls[0][1] == "builder-model"


def test_builder_harness_has_hashed_executable_step_spec(tmp_path: Path) -> None:
    spec = BuilderHarnessSpec.default()
    assert spec.steps == ("inspect", "propose", "validate", "probe", "commit_or_rollback")
    assert len(spec.sha256) == 64

    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(proposal(current.sha256)),
        model="builder-model",
        spec=spec,
    )
    assert (workspace.root / "builder_harnesses" / f"{spec.sha256}.json").is_file()
    result = builder.evolve_once(score=0.2, feedback="invalid", probe=lambda _: True)
    assert tuple(event.step for event in result.events) == spec.steps
    assert result.builder_harness_sha256 == spec.sha256


def test_builder_rejects_version_only_change(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    unchanged_nodes = json.loads(current.to_json())["spec"]["nodes"]
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(proposal(current.sha256, nodes=unchanged_nodes)),
        model="builder-model",
    )

    result = builder.evolve_once(score=0.2, feedback="invalid")

    assert result.status == "rejected"
    assert "no executable change" in result.reason
    assert workspace.current().sha256 == current.sha256


def test_builder_can_select_a_historical_source_branch(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    root = workspace.commit(artifact())
    first = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(proposal(root.sha256)),
        model="builder-model",
    ).evolve_once(score=0.2, feedback="explore")
    assert first.status == "committed"
    active = workspace.current()
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(
            branch_proposal(root.sha256, prompt="Restart from {task}")
        ),
        model="builder-model",
    )

    result = builder.evolve_once(score=0.1, feedback="regressed")

    assert result.status == "committed"
    assert result.source_sha256 == root.sha256
    assert workspace.current().parent_sha256 == root.sha256
    assert workspace.current().version == root.version + 1
    assert workspace.current().sha256 != active.sha256
    assert workspace.same_lineage(root.sha256, workspace.current().sha256)
    trace = workspace.load_builder_trace("unused", missing_ok=True)
    assert trace is None


def test_builder_rejects_same_lineage_source_not_visible_in_experiment_history(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = workspace.commit(artifact())
    hidden = workspace.store_artifact(
        artifact(parent_sha256=current.sha256)
    )
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(
            branch_proposal(hidden.sha256, prompt="Use hidden source for {task}")
        ),
        model="builder-model",
    )

    result = builder.evolve_once(score=0.1, feedback="regressed")

    assert result.status == "rejected"
    assert result.reason == "proposal source is not available in this experiment line"
    assert workspace.current().sha256 == current.sha256


def test_builder_records_declared_changed_components(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = workspace.commit(artifact())
    payload = json.loads(proposal(current.sha256))
    payload["schema_version"] = 2
    payload["source_sha256"] = current.sha256
    payload["changed_components"] = ["interface", "router"]
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(json.dumps(payload)),
        model="builder-model",
    )
    result = builder.evolve_once(score=0.1, feedback="change direction", run_id="components")
    assert result.status == "committed"
    assert {"interface", "router"}.issubset(
        set(next(event.output["changed_components"] for event in result.events if event.step == "propose"))
    )


def test_builder_rolls_back_invalid_base_and_probe_failure(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    wrong_base = "f" * 64
    generator = SequenceGenerator(proposal(wrong_base), proposal(current.sha256))
    builder = BuilderHarness(workspace=workspace, generator=generator, model="builder-model")

    rejected = builder.evolve_once(score=0.2, feedback="invalid")
    assert rejected.status == "rejected"
    assert workspace.current().sha256 == current.sha256

    failed_probe = builder.evolve_once(score=0.2, feedback="invalid", probe=lambda _: False)
    assert failed_probe.status == "rolled_back"
    assert workspace.current().sha256 == current.sha256


def test_probe_rollback_retains_source_and_changed_components(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    source = workspace.commit(artifact())
    active = workspace.commit(artifact(parent_sha256=source.sha256))
    workspace.record_trace(
        run_id="historical-source",
        harness_sha256=source.sha256,
        candidate="candidate",
        task_sha256="a" * 64,
        request_sha256="e" * 64,
        solver_model="solver-model",
        events=(),
        score=0.4,
        feedback="historical public evidence",
    )
    payload = json.loads(
        branch_proposal(source.sha256, prompt="Probe historical branch {task}")
    )
    payload["changed_components"] = ["router"]
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(json.dumps(payload)),
        model="builder-model",
    )

    result = builder.evolve_once(
        score=0.1,
        feedback="probe failed",
        probe=lambda _: False,
    )

    assert result.status == "rolled_back"
    assert result.source_sha256 == source.sha256
    assert result.changed_components == ("router",)
    workspace.record_builder_trace(
        run_id="rollback-provenance",
        builder_harness_sha256=result.builder_harness_sha256,
        status=result.status,
        events=result.events,
        previous_harness_sha256=result.previous_sha256,
        candidate_harness_sha256=result.candidate_sha256,
        next_harness_sha256=active.sha256,
        reason=result.reason,
        source_sha256=result.source_sha256,
        changed_components=result.changed_components,
    )
    view = experiment_one_builder_view(workspace.inspect())
    candidate = next(
        item
        for item in view["available_harnesses"]
        if item["sha256"] == result.candidate_sha256
    )
    decision = candidate["decisions"][0]
    assert decision["source_sha256"] == source.sha256
    assert decision["base_sha256"] == source.sha256
    assert decision["changed_components"] == ["router"]


def test_builder_rejects_non_object_json(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator("[]"),
        model="builder-model",
    )
    result = builder.evolve_once(score=0.1, feedback="failed")
    assert result.status == "rejected"
    assert tuple(event.step for event in result.events) == BuilderHarnessSpec.default().steps
    assert result.events[1].output == {
        "accepted": False,
        "error": "ValueError: Builder proposal must be one JSON object",
    }
    assert result.reason == (
        "Builder proposal failed: ValueError: "
        "Builder proposal must be one JSON object"
    )


def test_builder_rejection_redacts_secret_like_error_text(tmp_path: Path) -> None:
    class RaisingGenerator:
        def generate(self, prompt: str, *, model: str) -> GenerationResult:
            del prompt, model
            raise RuntimeError(
                "provider rejected Authorization: [REDACTED] "
                "api_key=[REDACTED]"
            )

    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    builder = BuilderHarness(
        workspace=workspace,
        generator=RaisingGenerator(),
        model="builder-model",
    )

    result = builder.evolve_once(score=0.1, feedback="failed")

    assert result.status == "rejected"
    assert "secret-token-123" not in result.reason
    assert "another-secret" not in result.reason
    assert result.events[1].output["error"] == (
        "RuntimeError: provider rejected Authorization: [REDACTED] "
        "api_key=[REDACTED]"
    )


def test_builder_rejects_non_hex_base_hash() -> None:
    with pytest.raises(ValueError, match="base hash"):
        from optimization_lab.harness_builder.builder_harness import HarnessChangeProposal

        HarnessChangeProposal.from_response(proposal("z" * 64))


def test_probe_exception_rolls_back_with_complete_step_trace(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(proposal(current.sha256)),
        model="builder-model",
    )

    def failed_probe(_: object) -> bool:
        raise RuntimeError("probe infrastructure failed")

    result = builder.evolve_once(score=0.1, feedback="failed", probe=failed_probe)

    assert result.status == "rolled_back"
    assert tuple(event.step for event in result.events) == BuilderHarnessSpec.default().steps
    assert workspace.current().sha256 == current.sha256


def test_non_boolean_probe_result_rolls_back_and_preserves_candidate(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = artifact()
    workspace.commit(current)
    builder = BuilderHarness(
        workspace=workspace,
        generator=SequenceGenerator(proposal(current.sha256)),
        model="builder-model",
    )

    result = builder.evolve_once(
        score=0.1,
        feedback="failed",
        probe=lambda _: {"passed": False},  # type: ignore[return-value]
    )

    assert result.status == "rolled_back"
    assert result.candidate_sha256 is not None
    assert workspace.artifact_path(result.candidate_sha256).is_file()
    assert workspace.current().sha256 == current.sha256
