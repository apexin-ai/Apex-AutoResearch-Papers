from __future__ import annotations

import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.agent_runtime import (
    AgentAction,
    AgentProtocolError,
    AgentRuntime,
)
from optimization_lab.harness_builder.tool_registry import (
    BoundTool,
    ToolBudgetError,
    ToolPolicy,
    ToolRegistry,
)


def _runtime(tmp_path: Path, *, max_calls: int = 2) -> tuple[AgentRuntime, list[str]]:
    seen: list[str] = []

    def inspect(arguments: dict[str, object]) -> dict[str, object]:
        seen.append(str(arguments["value"]))
        return {"observed": arguments["value"]}

    registry = ToolRegistry(
        tmp_path,
        {"inspect": BoundTool.callable(inspect)},
        receipt_path=tmp_path / "receipts.jsonl",
    )
    session = registry.bind(
        ToolPolicy(allow=("inspect",), deny=(), max_calls=max_calls),
        workspace=tmp_path,
    )
    return AgentRuntime(session, operation_scope="round-1-solver"), seen


def test_parse_emit_action() -> None:
    action = AgentAction.from_model_text('{"action":"emit","candidate":"final"}')
    assert action.kind == "emit"
    assert action.candidate == "final"


def test_parse_workflow_action() -> None:
    action = AgentAction.from_model_text(
        '{"action":"workflow","workflow":"diagnose_generate_verify"}'
    )
    assert action.kind == "workflow"
    assert action.workflow == "diagnose_generate_verify"


def test_tool_action_is_executed_and_emit_ends_loop(tmp_path: Path) -> None:
    runtime, seen = _runtime(tmp_path)
    outputs = iter(
        [
            '{"action":"tool","tool":"inspect","arguments":{"value":"x"}}',
            '{"action":"emit","candidate":"answer"}',
        ]
    )
    result = runtime.run(lambda _: next(outputs))
    assert result.candidate == "answer"
    assert seen == ["x"]
    assert [turn.action.kind for turn in result.turns] == ["tool", "emit"]
    assert result.turns[0].tool_result is not None
    assert result.turns[0].tool_result.receipt.operation_id == "round-1-solver-tool-0000"


def test_unknown_tool_and_malformed_json_fail_closed(tmp_path: Path) -> None:
    runtime, _ = _runtime(tmp_path)
    with pytest.raises(AgentProtocolError, match="JSON"):
        runtime.run(lambda _: "not-json")

    runtime, _ = _runtime(tmp_path)
    with pytest.raises(AgentProtocolError, match="not allowed"):
        runtime.run(
            lambda _: json.dumps(
                {
                    "action": "tool",
                    "tool": "missing",
                    "arguments": {},
                }
            )
        )


def test_budget_error_is_not_converted_to_a_candidate(tmp_path: Path) -> None:
    runtime, _ = _runtime(tmp_path, max_calls=1)
    outputs = iter(
        [
            '{"action":"tool","tool":"inspect","arguments":{"value":"x"}}',
            '{"action":"tool","tool":"inspect","arguments":{"value":"y"}}',
        ]
    )
    with pytest.raises(ToolBudgetError):
        runtime.run(lambda _: next(outputs))


def test_emit_requires_non_empty_candidate(tmp_path: Path) -> None:
    runtime, _ = _runtime(tmp_path)
    with pytest.raises(AgentProtocolError, match="candidate"):
        runtime.run(lambda _: '{"action":"emit","candidate":" "}')


def test_model_cannot_choose_or_rebind_operation_id(tmp_path: Path) -> None:
    runtime, _ = _runtime(tmp_path)
    with pytest.raises(AgentProtocolError, match="unexpected"):
        runtime.run(
            lambda _: '{"action":"tool","tool":"inspect","arguments":{},"operation_id":"chosen"}'
        )
