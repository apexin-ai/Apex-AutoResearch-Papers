from __future__ import annotations

from pathlib import Path

import pytest

from optimization_lab.harness_builder.agent_runtime import AgentProtocolError, AgentRuntime
from optimization_lab.harness_builder.tool_registry import ToolPolicy, ToolRegistry
from optimization_lab.harness_builder.workflows import WorkflowRegistry


def _runtime(tmp_path: Path, *outputs: str) -> tuple[AgentRuntime, object]:
    registry = ToolRegistry(tmp_path / "tools")
    session = registry.bind(
        ToolPolicy(allow=(), deny=(), max_calls=4),
        workspace=tmp_path / "tools" / "workspace",
    )
    iterator = iter(outputs)
    runtime = AgentRuntime(
        session,
        operation_scope="round-1-solver",
        workflow_registry=WorkflowRegistry.standard(),
        allowed_workflows=("diagnose_generate_verify",),
    )
    return runtime, iterator


def test_solver_can_select_fixed_workflow_before_emitting(tmp_path: Path) -> None:
    runtime, outputs = _runtime(
        tmp_path,
        '{"action":"workflow","workflow":"diagnose_generate_verify"}',
        '{"action":"emit","candidate":"answer"}',
    )
    prompts: list[str] = []

    def model_step(prompt: str) -> str:
        prompts.append(prompt)
        return next(outputs)

    result = runtime.run(model_step, initial_prompt="solve")
    assert result.candidate == "answer"
    assert [turn.action.kind for turn in result.turns] == ["workflow", "emit"]
    assert "solve" in prompts[1]
    assert "Diagnose the current failure" in prompts[1]
    assert "Generate one complete candidate" in prompts[1]
    assert "Verify the public output contract" in prompts[1]


def test_solver_cannot_select_unapproved_or_repeat_workflow(tmp_path: Path) -> None:
    runtime, _ = _runtime(tmp_path)
    with pytest.raises(AgentProtocolError, match="not allowed"):
        runtime.run(
            lambda _: '{"action":"workflow","workflow":"compare_repair_verify"}'
        )

    runtime, outputs = _runtime(
        tmp_path,
        '{"action":"workflow","workflow":"diagnose_generate_verify"}',
        '{"action":"workflow","workflow":"diagnose_generate_verify"}',
    )
    with pytest.raises(AgentProtocolError, match="already selected"):
        runtime.run(lambda _: next(outputs))


def test_standard_workflow_registry_is_fixed_and_public() -> None:
    registry = WorkflowRegistry.standard()
    payload = registry.public_catalog(("diagnose_generate_verify",))
    assert payload == [
        {
            "id": "diagnose_generate_verify",
            "steps": [
                "Diagnose the current failure using only public task evidence.",
                "Generate one complete candidate that addresses the diagnosis.",
                "Verify the public output contract before emitting.",
            ],
        }
    ]
    with pytest.raises(KeyError):
        registry.require("arbitrary_python")


def test_workflow_registry_rejects_duplicate_allowlist(tmp_path: Path) -> None:
    registry = ToolRegistry(tmp_path / "tools")
    session = registry.bind(
        ToolPolicy(allow=(), deny=(), max_calls=4),
        workspace=tmp_path / "tools" / "workspace",
    )
    with pytest.raises(ValueError, match="duplicates"):
        AgentRuntime(
            session,
            operation_scope="round-1-solver",
            workflow_registry=WorkflowRegistry.standard(),
            allowed_workflows=(
                "diagnose_generate_verify",
                "diagnose_generate_verify",
            ),
        )
