from __future__ import annotations

import copy
import json
import re
from dataclasses import dataclass
from typing import Any, Callable, Mapping

from .tool_registry import ToolCallResult, ToolSession
from .workflows import WorkflowRegistry


_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")


class AgentProtocolError(ValueError):
    """The Solver returned an action outside the Task Harness protocol."""


@dataclass(frozen=True)
class AgentAction:
    kind: str
    tool: str | None = None
    arguments: Mapping[str, Any] | None = None
    candidate: str | None = None
    workflow: str | None = None

    @classmethod
    def from_model_text(cls, text: str) -> "AgentAction":
        if not isinstance(text, str) or not text.strip():
            raise AgentProtocolError("Agent action must be non-empty JSON text")
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as exc:
            raise AgentProtocolError("Agent action must be exactly one JSON object") from exc
        if not isinstance(payload, dict):
            raise AgentProtocolError("Agent action JSON must be an object")
        action = payload.get("action")
        if action == "tool":
            unexpected = set(payload) - {"action", "tool", "arguments"}
            if unexpected:
                raise AgentProtocolError(
                    f"tool action contains unexpected keys: {sorted(unexpected)}"
                )
            tool = payload.get("tool")
            arguments = payload.get("arguments")
            if not isinstance(tool, str) or _SAFE_ID.fullmatch(tool) is None:
                raise AgentProtocolError("tool action requires a safe tool id")
            if not isinstance(arguments, dict):
                raise AgentProtocolError("tool action arguments must be a JSON object")
            return cls(kind="tool", tool=tool, arguments=copy.deepcopy(arguments))
        if action == "emit":
            unexpected = set(payload) - {"action", "candidate"}
            if unexpected:
                raise AgentProtocolError(
                    f"emit action contains unexpected keys: {sorted(unexpected)}"
                )
            candidate = payload.get("candidate")
            if not isinstance(candidate, str) or not candidate.strip():
                raise AgentProtocolError("emit action requires a non-empty candidate")
            return cls(kind="emit", candidate=candidate)
        if action == "workflow":
            unexpected = set(payload) - {"action", "workflow"}
            if unexpected:
                raise AgentProtocolError(
                    f"workflow action contains unexpected keys: {sorted(unexpected)}"
                )
            workflow = payload.get("workflow")
            if not isinstance(workflow, str) or _SAFE_ID.fullmatch(workflow) is None:
                raise AgentProtocolError("workflow action requires a safe workflow id")
            return cls(kind="workflow", workflow=workflow)
        raise AgentProtocolError("Agent action must be tool, workflow, or emit")


@dataclass(frozen=True)
class AgentTurn:
    index: int
    action: AgentAction
    model_input: str
    model_output: str
    tool_result: ToolCallResult | None = None


@dataclass(frozen=True)
class AgentRun:
    candidate: str
    turns: tuple[AgentTurn, ...]


class AgentRuntime:
    """Execute a bounded Solver-selected tool loop outside the evaluator."""

    def __init__(
        self,
        tool_session: ToolSession,
        *,
        operation_scope: str,
        max_turns: int = 8,
        workflow_registry: WorkflowRegistry | None = None,
        allowed_workflows: tuple[str, ...] = (),
    ) -> None:
        if not isinstance(operation_scope, str) or not operation_scope or any(
            char in operation_scope for char in "\r\n"
        ):
            raise ValueError("operation_scope must be a non-empty single-line string")
        if not isinstance(max_turns, int) or isinstance(max_turns, bool) or max_turns < 1:
            raise ValueError("max_turns must be a positive integer")
        self.tool_session = tool_session
        self.operation_scope = operation_scope
        self.max_turns = max_turns
        self.workflow_registry = workflow_registry
        self.allowed_workflows = tuple(allowed_workflows)
        if len(set(self.allowed_workflows)) != len(self.allowed_workflows):
            raise ValueError("allowed_workflows must not contain duplicates")
        if self.allowed_workflows and workflow_registry is None:
            raise ValueError("allowed workflows require a WorkflowRegistry")
        if workflow_registry is not None:
            workflow_registry.public_catalog(self.allowed_workflows)

    def run(self, model_step: Callable[[str], str], *, initial_prompt: str = "") -> AgentRun:
        if not callable(model_step):
            raise TypeError("model_step must be callable")
        base_prompt = initial_prompt
        prompt = base_prompt
        turns: list[AgentTurn] = []
        observations: list[dict[str, Any]] = []
        selected_workflow: str | None = None
        for index in range(self.max_turns):
            model_input = prompt
            model_output = model_step(model_input)
            action = AgentAction.from_model_text(model_output)
            if action.kind == "emit":
                assert action.candidate is not None
                turns.append(
                    AgentTurn(
                        index=index,
                        action=action,
                        model_input=model_input,
                        model_output=model_output,
                    )
                )
                return AgentRun(candidate=action.candidate, turns=tuple(turns))
            if action.kind == "workflow":
                assert action.workflow is not None
                if selected_workflow is not None:
                    raise AgentProtocolError("Agent workflow was already selected")
                if action.workflow not in self.allowed_workflows:
                    raise AgentProtocolError(
                        f"Harness workflow is not allowed: {action.workflow}"
                    )
                assert self.workflow_registry is not None
                definition = self.workflow_registry.require(action.workflow)
                selected_workflow = action.workflow
                turns.append(
                    AgentTurn(
                        index=index,
                        action=action,
                        model_input=model_input,
                        model_output=model_output,
                    )
                )
                observations.append(
                    {
                        "kind": "workflow",
                        "selected_workflow": definition.public_payload(),
                    }
                )
                prompt = self._continuation_prompt(
                    base_prompt,
                    observations,
                    instruction=(
                        "Follow the selected fixed phases using strict JSON tool or emit "
                        "actions. Do not select another workflow."
                    ),
                )
                continue
            assert action.tool is not None and action.arguments is not None
            operation_id = f"{self.operation_scope}-tool-{index:04d}"
            try:
                tool_result = self.tool_session.call(
                    action.tool,
                    action.arguments,
                    operation_id=operation_id,
                )
            except PermissionError as exc:
                raise AgentProtocolError(str(exc)) from exc
            turns.append(
                AgentTurn(
                    index=index,
                    action=action,
                    model_input=model_input,
                    model_output=model_output,
                    tool_result=tool_result,
                )
            )
            observations.append(
                {
                    "kind": "tool",
                    "tool": action.tool,
                    "result": tool_result.value,
                    "receipt": tool_result.receipt.to_dict(),
                }
            )
            prompt = self._continuation_prompt(
                base_prompt,
                observations,
                instruction="Return the next strict JSON tool, workflow, or emit action.",
            )
        raise AgentProtocolError("Agent reached max_turns without emit")

    @staticmethod
    def _continuation_prompt(
        base_prompt: str,
        observations: list[dict[str, Any]],
        *,
        instruction: str,
    ) -> str:
        state = json.dumps(
            {
                "observations": observations,
                "instruction": instruction,
            },
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        return (
            f"{base_prompt}\n\n"
            "--- TASK HARNESS AGENT LOOP STATE ---\n"
            f"{state}\n"
            "--- END TASK HARNESS AGENT LOOP STATE ---"
        )


__all__ = [
    "AgentAction",
    "AgentProtocolError",
    "AgentRun",
    "AgentRuntime",
    "AgentTurn",
]
