from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.generation import FakeGenerator
from optimization_lab.harness_builder.events import (
    OperationJournal,
    OperationStateError,
    ResourceCaps,
    ResourceGovernor,
)
from optimization_lab.harness_builder.model_gateway import (
    CapabilityError,
    IsolatedModelGateway,
)


def _governor(tmp_path: Path) -> ResourceGovernor:
    caps = ResourceCaps(
        model_calls=4,
        evaluator_transactions=0,
        gpu_exclusive_seconds=0,
        cpu_evaluator_seconds=0,
    )
    return ResourceGovernor(
        journal=OperationJournal(
            tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
        ),
        global_caps=caps,
        cell_caps={"suite:task:A": caps},
    )


def test_capability_is_one_shot_holder_bound_and_prompt_bound(tmp_path: Path) -> None:
    calls: list[tuple[Path, str, FakeGenerator]] = []

    def factory(work_root: Path, output_mode: str) -> FakeGenerator:
        generator = FakeGenerator("one strict response")
        calls.append((work_root, output_mode, generator))
        return generator

    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "model",
        governor=_governor(tmp_path),
        transport_factory=factory,
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    prompt = "public prompt"
    capability = gateway.issue_capability(
        holder="trusted_controller",
        operation_id="suite:task:A:planner:v001",
        cell_id="suite:task:A",
        operation_kind="planner_call",
        prompt=prompt,
        model="fixture-model",
        output_mode="plain_text",
    )

    with pytest.raises(CapabilityError, match="holder"):
        gateway.invoke(capability, prompt=prompt, presented_by="solution_model")
    with pytest.raises(CapabilityError, match="prompt"):
        gateway.invoke(
            capability, prompt="different prompt", presented_by="trusted_controller"
        )

    result = gateway.invoke(
        capability, prompt=prompt, presented_by="trusted_controller"
    )
    assert result.raw_response == "one strict response"
    assert len(calls) == 1
    work_root, output_mode, generator = calls[0]
    assert output_mode == "plain_text"
    assert work_root.parent == (tmp_path / "model" / "operations")
    assert generator.calls == [{"prompt": prompt, "model": "fixture-model"}]
    assert (work_root / "prompt.txt").read_text(encoding="utf-8") == prompt
    metadata = json.loads((work_root / "result.json").read_text(encoding="utf-8"))
    assert metadata["prompt_sha256"] == hashlib.sha256(prompt.encode()).hexdigest()
    assert "capability" not in json.dumps(metadata).lower()

    with pytest.raises(CapabilityError, match="already used"):
        gateway.invoke(capability, prompt=prompt, presented_by="trusted_controller")


def test_each_operation_uses_a_disjoint_transport_directory(tmp_path: Path) -> None:
    roots: list[Path] = []

    def factory(work_root: Path, _output_mode: str) -> FakeGenerator:
        roots.append(work_root)
        return FakeGenerator("response")

    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "model",
        governor=_governor(tmp_path),
        transport_factory=factory,
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    for version in ("v001", "v002"):
        prompt = f"prompt {version}"
        capability = gateway.issue_capability(
            holder="trusted_controller",
            operation_id=f"suite:task:A:planner:{version}",
            cell_id="suite:task:A",
            operation_kind="planner_call",
            prompt=prompt,
            model="fixture-model",
            output_mode="plain_text",
        )
        gateway.invoke(capability, prompt=prompt, presented_by="trusted_controller")

    assert len(set(roots)) == 2
    assert all(root.is_dir() for root in roots)


def test_provider_failure_is_terminal_and_charged_without_secret_error_log(
    tmp_path: Path,
) -> None:
    class FailedGenerator:
        def estimated_api_cost_usd(self) -> float:
            return 0.0

        def generate(self, prompt: str, *, model: str):
            raise RuntimeError("Bearer [REDACTED] provider exploded")

    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "model",
        governor=_governor(tmp_path),
        transport_factory=lambda _root, _mode: FailedGenerator(),
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    capability = gateway.issue_capability(
        holder="trusted_controller",
        operation_id="suite:task:A:solution:v001",
        cell_id="suite:task:A",
        operation_kind="solution_call",
        prompt="public prompt",
        model="fixture-model",
        output_mode="plain_text",
    )

    with pytest.raises(RuntimeError, match="SECRET"):
        gateway.invoke(
            capability, prompt="public prompt", presented_by="trusted_controller"
        )

    replay = gateway.governor.journal.replay()
    record = replay.operations["suite:task:A:solution:v001"]
    assert record.state == "failed"
    assert record.committed_usage.model_calls == 1
    assert "SECRET" not in gateway.governor.journal.ledger_path.read_text(
        encoding="utf-8"
    )


def test_completed_result_can_be_replayed_after_process_restart(tmp_path: Path) -> None:
    calls: list[str] = []

    def factory(_root: Path, _mode: str) -> FakeGenerator:
        calls.append("called")
        return FakeGenerator("persisted response")

    signing_key = b"fixture-signing-key-with-enough-entropy"
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "model",
        governor=_governor(tmp_path),
        transport_factory=factory,
        signing_key=signing_key,
    )
    prompt = "public prompt"
    fields = dict(
        holder="trusted_controller",
        operation_id="suite:task:A:planner:v001",
        cell_id="suite:task:A",
        operation_kind="planner_call",
        prompt=prompt,
        model="fixture-model",
        output_mode="plain_text",
    )
    capability = gateway.issue_capability(**fields)
    first = gateway.invoke(capability, prompt=prompt, presented_by="trusted_controller")

    restored = IsolatedModelGateway(
        artifact_root=tmp_path / "model",
        governor=ResourceGovernor(
            journal=OperationJournal(
                tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
            ),
            global_caps=gateway.governor.global_caps,
            cell_caps=gateway.governor.cell_caps,
        ),
        transport_factory=factory,
        signing_key=signing_key,
    )
    replayed = restored.replay_completed(
        operation_id=fields["operation_id"],
        expected_prompt_sha256=hashlib.sha256(prompt.encode()).hexdigest(),
    )
    assert replayed == first
    assert calls == ["called"]


def test_started_without_result_is_not_silently_retried(tmp_path: Path) -> None:
    governor = _governor(tmp_path)
    operation_id = "suite:task:A:planner:abandoned"
    from optimization_lab.harness_builder.events import ResourceVector

    governor.reserve(
        operation_id=operation_id,
        cell_id="suite:task:A",
        operation_kind="planner_call",
        reservation=ResourceVector(model_calls=1),
    )
    governor.start(operation_id)
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "model",
        governor=governor,
        transport_factory=lambda _root, _mode: FakeGenerator("must not run"),
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    capability = gateway.issue_capability(
        holder="trusted_controller",
        operation_id=operation_id,
        cell_id="suite:task:A",
        operation_kind="planner_call",
        prompt="public prompt",
        model="fixture-model",
        output_mode="plain_text",
    )

    with pytest.raises(OperationStateError, match="abandoned"):
        gateway.invoke(
            capability, prompt="public prompt", presented_by="trusted_controller"
        )


def test_started_with_bound_result_is_completed_without_reissuing_provider(
    tmp_path: Path,
) -> None:
    signing_key = b"fixture-signing-key-with-enough-entropy"
    governor = _governor(tmp_path)
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "model",
        governor=governor,
        transport_factory=lambda _root, _mode: FakeGenerator("sealed response"),
        signing_key=signing_key,
    )
    prompt = "public prompt"
    fields = dict(
        holder="trusted_controller",
        operation_id="suite:task:A:planner:recoverable",
        cell_id="suite:task:A",
        operation_kind="planner_call",
        prompt=prompt,
        model="fixture-model",
        output_mode="plain_text",
    )
    original_complete = governor.complete

    def interrupt_completion(operation_id: str, **_kwargs):
        raise KeyboardInterrupt(f"crash after artifact for {operation_id}")

    governor.complete = interrupt_completion  # type: ignore[method-assign]
    with pytest.raises(KeyboardInterrupt, match="crash after artifact"):
        gateway.invoke(
            gateway.issue_capability(**fields),
            prompt=prompt,
            presented_by="trusted_controller",
        )
    governor.complete = original_complete  # type: ignore[method-assign]

    provider_calls: list[str] = []
    restored = IsolatedModelGateway(
        artifact_root=tmp_path / "model",
        governor=ResourceGovernor(
            journal=OperationJournal(
                tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
            ),
            global_caps=governor.global_caps,
            cell_caps=governor.cell_caps,
        ),
        transport_factory=lambda _root, _mode: provider_calls.append("called"),
        signing_key=signing_key,
    )
    result = restored.invoke(
        restored.issue_capability(**fields),
        prompt=prompt,
        presented_by="trusted_controller",
    )

    assert result.raw_response == "sealed response"
    assert provider_calls == []
    assert restored.governor.journal.replay().operations[
        fields["operation_id"]
    ].state == "completed"
