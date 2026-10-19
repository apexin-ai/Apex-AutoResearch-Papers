from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

import pytest

from optimization_lab.generation import GenerationResult
from optimization_lab.harness_builder.events import (
    OperationJournal,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
)
from optimization_lab.harness_builder.model_route_canary import (
    EXPECTED_HARNESS_DECISION,
    FROZEN_CLIENT_VERSION,
    FROZEN_MODEL,
    ModelRouteCanaryBlocked,
    ModelRouteCanaryRunner,
)
from optimization_lab.harness_builder.prepare import prepare_hb_gen1
from scripts.run_harness_builder_model_route_canary import build_parser


ROOT = Path(__file__).resolve().parents[1]
REVISION_A = "a" * 40
REVISION_B = "b" * 40
USAGE = {
    "cached_input_tokens": 0,
    "input_tokens": 40,
    "output_tokens": 20,
    "reasoning_output_tokens": 0,
}


def test_cli_defaults_to_preflight_and_requires_explicit_execute() -> None:
    parsed = build_parser().parse_args(["--artifact-root", "/tmp/hb-gen1"])
    assert parsed.execute is False
    parsed = build_parser().parse_args(
        ["--artifact-root", "/tmp/hb-gen1", "--execute"]
    )
    assert parsed.execute is True


class RecordingTransport:
    def __init__(
        self,
        *,
        response: str,
        provider: str = "codex_chatgpt",
        usage: dict[str, int] | None = None,
    ) -> None:
        self.response = response
        self.provider = provider
        self.usage = dict(USAGE if usage is None else usage)
        self.calls: list[dict[str, str]] = []

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append({"prompt": prompt, "model": model})
        return GenerationResult(
            raw_response=self.response,
            provider=self.provider,
            usage=self.usage,
        )


class Factory:
    def __init__(self, transport: RecordingTransport) -> None:
        self.transport = transport
        self.roots: list[tuple[Path, str]] = []

    def __call__(self, work_root: Path, output_mode: str) -> RecordingTransport:
        self.roots.append((work_root, output_mode))
        return self.transport


def _response(**updates: object) -> str:
    payload = asdict(EXPECTED_HARNESS_DECISION)
    payload.update(updates)
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def _stage(tmp_path: Path, *, revision: str = REVISION_A) -> Path:
    artifact_root = tmp_path / "hb-gen1"
    prepare_hb_gen1(
        project_root=ROOT,
        artifact_root=artifact_root,
        code_revision=revision,
        observed_client_version=FROZEN_CLIENT_VERSION,
    )
    return artifact_root


def _runner(
    artifact_root: Path,
    factory: Factory,
    *,
    revision: str = REVISION_A,
    prior_roots: tuple[Path, ...] = (),
) -> ModelRouteCanaryRunner:
    return ModelRouteCanaryRunner(
        project_root=ROOT,
        artifact_root=artifact_root,
        observed_code_revision=revision,
        observed_client_version=FROZEN_CLIENT_VERSION,
        transport_factory=factory,
        signing_key=b"model-route-canary-test-signing-key",
        prior_canary_artifact_roots=prior_roots,
    )


def _legacy_canary_root(tmp_path: Path) -> Path:
    root = _stage(tmp_path / "legacy", revision=REVISION_A)
    journal = OperationJournal(
        root / "model-canary" / "journal",
        anchor_path=root / "model-canary" / "trusted-head.json",
    )
    caps = ResourceCaps(model_calls=2)
    governor = ResourceGovernor(
        journal=journal,
        global_caps=caps,
        cell_caps={"canary:model-route": caps},
    )
    operation_id = "canary:model-route:planner:v001"
    governor.reserve(
        operation_id=operation_id,
        cell_id="canary:model-route",
        operation_kind="planner_call",
        reservation=ResourceVector(model_calls=1),
    )
    governor.start(operation_id)
    governor.complete(
        operation_id,
        actual_usage=ResourceVector(model_calls=1),
        artifact_sha256="c" * 64,
    )
    replay = journal.replay()
    summary = {
        "schema_version": 1,
        "status": "passed",
        "operation_id": operation_id,
        "operation_state": "completed",
        "operation_event_count": replay.event_count,
        "operation_journal_head_sha256": replay.head_sha256,
        "result_artifact_sha256": "c" * 64,
        "model": FROZEN_MODEL,
        "reasoning_effort": "high",
        "client_version": FROZEN_CLIENT_VERSION,
        "provider": "codex_chatgpt",
    }
    (root / "model-canary" / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return root


def test_canary_passes_and_replays_without_a_second_model_call(tmp_path: Path) -> None:
    artifact_root = _stage(tmp_path)
    transport = RecordingTransport(response=_response())
    factory = Factory(transport)
    runner = _runner(artifact_root, factory)

    preflight = runner.preflight()
    assert preflight["status"] == "ready"
    assert preflight["remaining_model_calls"] == 2
    assert preflight["model_signature"] == {
        "model": "gpt-5.6-sol",
        "reasoning_effort": "high",
        "client_version": "codex-cli-0.144.6",
        "transport": "codex-exec-chatgpt-login",
        "provider": "codex_chatgpt",
    }

    first = runner.execute()
    assert first["status"] == "passed"
    assert first["usage"] == USAGE
    assert first["prompt_sha256"] == runner.prompt_sha256
    assert first["staging_plan_sha256"] == runner.staging_plan_sha256
    assert first["code_revision"] == REVISION_A
    assert transport.calls == [{"prompt": runner.prompt, "model": FROZEN_MODEL}]
    assert factory.roots[0][1] == "plain_text"
    assert runner.result_path.is_file()

    no_call_transport = RecordingTransport(response="must not run")
    restored = _runner(artifact_root, Factory(no_call_transport))
    replayed = restored.execute()
    assert replayed == first
    assert no_call_transport.calls == []
    replay = restored.governor.journal.replay()
    assert replay.event_count == 3
    assert replay.operations[restored.operation_id].state == "completed"


def test_provider_or_model_signature_drift_fails_closed(tmp_path: Path) -> None:
    artifact_root = _stage(tmp_path)
    wrong_provider = RecordingTransport(
        response=_response(), provider="different_provider"
    )
    result = _runner(artifact_root, Factory(wrong_provider)).execute()
    assert result["status"] == "failed"
    assert result["reason_code"] == "provider_drift"
    assert wrong_provider.calls[0]["model"] == FROZEN_MODEL

    other_root = _stage(tmp_path / "other")
    staging_path = other_root / "staging_plan.json"
    staging = json.loads(staging_path.read_text(encoding="utf-8"))
    staging["model_signature"]["executor_model"] = "different-model"
    staging_path.write_text(
        json.dumps(staging, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(ModelRouteCanaryBlocked, match="model signature"):
        _runner(other_root, Factory(RecordingTransport(response=_response())))


@pytest.mark.parametrize(
    ("response", "reason_code"),
    [
        ("not a JSON object", "harness_decision_structure_drift"),
        (_response(kernel_directive="a different directive"), "harness_decision_mismatch"),
    ],
)
def test_structural_or_semantic_decision_drift_is_terminal(
    tmp_path: Path, response: str, reason_code: str
) -> None:
    artifact_root = _stage(tmp_path)
    result = _runner(
        artifact_root, Factory(RecordingTransport(response=response))
    ).execute()
    assert result["status"] == "failed"
    assert result["reason_code"] == reason_code


def test_started_without_artifact_is_abandoned_and_never_resent(tmp_path: Path) -> None:
    artifact_root = _stage(tmp_path)
    transport = RecordingTransport(response=_response())
    runner = _runner(artifact_root, Factory(transport))
    runner.governor.reserve(
        operation_id=runner.operation_id,
        cell_id="canary:model-route",
        operation_kind="planner_call",
        reservation=ResourceVector(model_calls=1),
    )
    runner.governor.start(runner.operation_id)

    report = runner.preflight()
    assert report["status"] == "blocked"
    assert "started_without_artifact_is_abandoned" in report["blockers"]
    with pytest.raises(ModelRouteCanaryBlocked, match="abandoned"):
        runner.execute()
    assert transport.calls == []


def test_missing_call_entitlement_blocks_without_invocation(tmp_path: Path) -> None:
    artifact_root = _stage(tmp_path)
    transport = RecordingTransport(response=_response())
    runner = _runner(artifact_root, Factory(transport))
    for index in range(2):
        operation_id = f"canary:model-route:old:{index}"
        runner.governor.reserve(
            operation_id=operation_id,
            cell_id="canary:model-route",
            operation_kind="planner_call",
            reservation=ResourceVector(model_calls=1),
        )
        runner.governor.start(operation_id)
        runner.governor.fail(operation_id, reason_code="old_segment_failed")

    report = runner.preflight()
    assert report["remaining_model_calls"] == 0
    assert "model_route_canary_call_entitlement_exhausted" in report["blockers"]
    with pytest.raises(ModelRouteCanaryBlocked, match="entitlement"):
        runner.execute()
    assert transport.calls == []


def test_obsolete_canary_is_charged_but_never_reused(tmp_path: Path) -> None:
    legacy_root = _legacy_canary_root(tmp_path)
    artifact_root = _stage(tmp_path / "current", revision=REVISION_B)
    transport = RecordingTransport(response=_response())
    runner = _runner(
        artifact_root,
        Factory(transport),
        revision=REVISION_B,
        prior_roots=(legacy_root,),
    )

    preflight = runner.preflight()
    assert preflight["prior_segment_model_calls"] == 1
    assert preflight["remaining_model_calls"] == 1
    result = runner.execute()
    assert result["status"] == "passed"
    assert len(transport.calls) == 1
    assert runner.binding["prior_canary_segments"][0]["reusable"] is False
    assert runner.preflight()["remaining_model_calls"] == 0


def test_changed_code_revision_creates_a_new_segment_and_preserves_old(
    tmp_path: Path,
) -> None:
    artifact_root = _stage(tmp_path, revision=REVISION_A)
    transport = RecordingTransport(response=_response())
    first_runner = _runner(artifact_root, Factory(transport), revision=REVISION_A)
    first = first_runner.execute()
    first_result = first_runner.result_path.read_bytes()

    staging_path = artifact_root / "staging_plan.json"
    staging = json.loads(staging_path.read_text(encoding="utf-8"))
    staging["code_revision"] = REVISION_B
    staging_path.write_text(
        json.dumps(staging, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    second_runner = _runner(artifact_root, Factory(transport), revision=REVISION_B)
    second = second_runner.execute()

    assert first["segment_id"] != second["segment_id"]
    assert first_runner.result_path.read_bytes() == first_result
    assert first_runner.result_path != second_runner.result_path
    assert len(transport.calls) == 2
    assert second_runner.preflight()["remaining_model_calls"] == 0
