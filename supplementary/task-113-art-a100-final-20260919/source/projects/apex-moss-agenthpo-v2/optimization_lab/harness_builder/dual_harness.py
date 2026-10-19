from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping

from optimization_lab.generation import CandidateGenerator

from .agent_runtime import AgentRuntime
from .experiment_one_tools import FORBIDDEN_EVALUATOR_TOOL_IDS
from .tool_registry import ToolPolicy, ToolRegistry
from .workflows import WorkflowRegistry


_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_NODE_KINDS = {"model_call", "tool_call", "skill_call", "emit"}
_MAX_TRACE_BYTES = 8 * 1024 * 1024
_PROMPT_PLACEHOLDER = re.compile(
    r"(?<!\{)\{([A-Za-z_][A-Za-z0-9_]*)\}(?!\})"
)
_STANDARD_WORKFLOWS = WorkflowRegistry.standard()


def _strict_keys(payload: Mapping[str, Any], allowed: set[str], label: str) -> None:
    unexpected = set(payload) - allowed
    if unexpected:
        raise ValueError(f"{label} contains unexpected keys: {sorted(unexpected)}")


def _safe_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not _SAFE_ID.fullmatch(value) or ".." in value:
        raise ValueError(f"{label} is unsafe")
    return value


def _canonical_json(payload: Any) -> str:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


@dataclass(frozen=True)
class TaskHarnessNode:
    node_id: str
    kind: str
    role: str | None = None
    prompt: str | None = None
    tool: str | None = None
    skill: str | None = None
    input_key: str = "latest_output"

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "TaskHarnessNode":
        if not isinstance(payload, Mapping):
            raise ValueError("Harness node must be an object")
        _strict_keys(
            payload,
            {"id", "kind", "role", "prompt", "tool", "skill", "input_key"},
            "Harness node",
        )
        node_id = _safe_id(payload.get("id"), "Harness node id")
        kind = payload.get("kind")
        if kind not in _NODE_KINDS:
            raise ValueError("unsupported Harness node kind")
        role = payload.get("role")
        prompt = payload.get("prompt")
        tool = payload.get("tool")
        skill = payload.get("skill")
        input_key = payload.get("input_key", "latest_output")
        if not isinstance(input_key, str) or not input_key.strip():
            raise ValueError("Harness node input key is invalid")
        if kind == "model_call":
            if not isinstance(role, str) or not role.strip():
                raise ValueError("model_call node requires a role")
            if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 32_000:
                raise ValueError("model_call node requires a bounded prompt")
            if tool is not None:
                raise ValueError("model_call node cannot declare a tool")
            if skill is not None:
                raise ValueError("model_call node cannot declare a skill")
        elif kind == "tool_call":
            tool = _safe_id(tool, "Harness tool")
            if role is not None or prompt is not None or skill is not None:
                raise ValueError("tool_call node cannot declare role or prompt")
        elif kind == "skill_call":
            skill = _safe_id(skill, "Harness skill")
            if role is not None or prompt is not None or tool is not None:
                raise ValueError("skill_call node cannot declare role, prompt, or tool")
        elif role is not None or prompt is not None or tool is not None or skill is not None:
            raise ValueError("emit node can only declare an input key")
        return cls(
            node_id=node_id,
            kind=kind,
            role=role,
            prompt=prompt,
            tool=tool,
            skill=skill,
            input_key=input_key,
        )

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {"id": self.node_id, "kind": self.kind}
        if self.role is not None:
            payload["role"] = self.role
        if self.prompt is not None:
            payload["prompt"] = self.prompt
        if self.tool is not None:
            payload["tool"] = self.tool
        if self.skill is not None:
            payload["skill"] = self.skill
        if self.input_key != "latest_output" or self.kind in {"tool_call", "emit"}:
            payload["input_key"] = self.input_key
        return payload


@dataclass(frozen=True)
class TaskHarnessSpec:
    schema_version: int
    nodes: tuple[TaskHarnessNode, ...]
    interface: Mapping[str, Any] = field(default_factory=dict)
    memory: Mapping[str, Any] = field(default_factory=dict)
    capabilities: Mapping[str, Any] = field(default_factory=dict)
    router: Mapping[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "TaskHarnessSpec":
        if not isinstance(payload, Mapping):
            raise ValueError("Task Harness spec must be an object")
        _strict_keys(
            payload,
            {"schema_version", "nodes", "interface", "memory", "capabilities", "router"},
            "Task Harness spec",
        )
        schema_version = payload.get("schema_version")
        if schema_version not in {1, 2}:
            raise ValueError("unsupported Task Harness spec schema")
        raw_nodes = payload.get("nodes")
        if not isinstance(raw_nodes, list) or not raw_nodes or len(raw_nodes) > 32:
            raise ValueError("Task Harness requires between one and 32 nodes")
        nodes = tuple(TaskHarnessNode.from_dict(item) for item in raw_nodes)
        if len({node.node_id for node in nodes}) != len(nodes):
            raise ValueError("Task Harness node ids must be unique")
        if sum(node.kind == "emit" for node in nodes) != 1:
            raise ValueError("Task Harness requires exactly one emit node")
        if nodes[-1].kind != "emit":
            raise ValueError("Task Harness emit node must be last")
        extras = {}
        for key in ("interface", "memory", "capabilities", "router"):
            value = payload.get(key, {})
            if not isinstance(value, Mapping):
                raise ValueError(f"Task Harness {key} must be an object")
            extras[key] = dict(value)
        if schema_version == 1 and any(extras.values()):
            raise ValueError("schema 1 Task Harness cannot declare v2 state")
        return cls(schema_version=schema_version, nodes=nodes, **extras)

    def to_dict(self) -> dict[str, Any]:
        payload = {
            "schema_version": self.schema_version,
            "nodes": [node.to_dict() for node in self.nodes],
        }
        if self.schema_version == 2:
            payload.update(
                {
                    "interface": dict(self.interface),
                    "memory": dict(self.memory),
                    "capabilities": dict(self.capabilities),
                    "router": dict(self.router),
                }
            )
        return payload


@dataclass(frozen=True)
class TaskHarnessArtifact:
    schema_version: int
    version: int
    parent_sha256: str | None
    spec: TaskHarnessSpec

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "TaskHarnessArtifact":
        if not isinstance(payload, Mapping):
            raise ValueError("Task Harness artifact must be an object")
        _strict_keys(
            payload,
            {"schema_version", "version", "parent_sha256", "spec"},
            "Task Harness artifact",
        )
        if payload.get("schema_version") != 1:
            raise ValueError("unsupported Task Harness artifact schema")
        version = payload.get("version")
        if not isinstance(version, int) or isinstance(version, bool) or version < 1:
            raise ValueError("Task Harness artifact version is invalid")
        parent = payload.get("parent_sha256")
        if parent is not None and (
            not isinstance(parent, str) or _SHA256.fullmatch(parent) is None
        ):
            raise ValueError("Task Harness parent hash is invalid")
        return cls(
            schema_version=1,
            version=version,
            parent_sha256=parent,
            spec=TaskHarnessSpec.from_dict(payload.get("spec")),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "version": self.version,
            "parent_sha256": self.parent_sha256,
            "spec": self.spec.to_dict(),
        }

    def to_json(self) -> str:
        return _canonical_json(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.to_json().encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class HarnessTraceEvent:
    index: int
    node_id: str
    kind: str
    input: Any
    output: Any


@dataclass(frozen=True)
class TaskHarnessRun:
    harness_sha256: str
    candidate: str
    events: tuple[HarnessTraceEvent, ...]
    output_contract_sha256: str | None = None
    model_call_scopes: tuple[str, ...] = ()


class _PromptState(dict[str, Any]):
    def __missing__(self, key: str) -> str:
        raise ValueError(f"Task Harness prompt references unknown state: {key}")


def _render_prompt(
    template: str,
    state: Mapping[str, Any],
    *,
    allowed_keys: set[str] | frozenset[str] | None = None,
) -> str:
    """Substitute only explicit bare state placeholders.

    Harness prompts commonly contain source code, JSON, and Python f-strings.
    ``str.format_map`` treats every pair of braces as a template expression,
    so a candidate containing ``{P}`` could make the next Solver fail before
    it was called. Unknown or doubled braces are therefore literal text.
    """

    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if allowed_keys is not None:
            if key not in allowed_keys:
                return match.group(0)
            if key not in state:
                raise ValueError(f"Task Harness prompt references unknown state: {key}")
            return str(state[key])
        return str(state[key]) if key in state else match.group(0)

    return _PROMPT_PLACEHOLDER.sub(replace, template)


class TaskHarnessRuntime:
    """Execute a typed Task Harness as real model/tool control flow."""

    def __init__(
        self,
        *,
        generator: CandidateGenerator,
        output_contract: Mapping[str, Any] | None = None,
    ) -> None:
        self.generator = generator
        self.output_contract = self._validated_output_contract(output_contract)
        self.output_contract_sha256 = self._output_contract_sha256(self.output_contract)

    def run(
        self,
        artifact: TaskHarnessArtifact,
        *,
        task: str,
        model: str,
        tools: Mapping[str, Callable[[Any], Any]],
        initial_state: Mapping[str, Any] | None = None,
        tool_registry: ToolRegistry | None = None,
        tool_workspace: str | os.PathLike[str] | None = None,
        operation_scope: str | None = None,
    ) -> TaskHarnessRun:
        if not task.strip() or not model.strip():
            raise ValueError("Task Harness task and model are required")
        state = _PromptState(task=task, latest_output="")
        interface = dict(artifact.spec.interface)
        memory = dict(artifact.spec.memory)
        capabilities = dict(artifact.spec.capabilities)
        router = dict(artifact.spec.router)
        agent_config: dict[str, Any] | None = None
        static_tool_session = None
        static_tool_call_index = 0
        if artifact.spec.schema_version == 2:
            task_template = interface.get("task_template")
            if task_template is not None:
                if not isinstance(task_template, str) or not task_template.strip():
                    raise ValueError("Harness interface task_template is invalid")
                task = _render_prompt(task_template, {"task": task}, allowed_keys={"task"})
                state["task"] = task
            constraints = interface.get("constraints", {})
            if not isinstance(constraints, Mapping):
                raise ValueError("Harness interface constraints are invalid")
            state["constraints"] = dict(constraints)
            abstract_memory = memory.get("abstract", [])
            if not isinstance(abstract_memory, list) or not all(
                isinstance(item, str) for item in abstract_memory
            ):
                raise ValueError("Harness abstract memory is invalid")
            state["memory"] = "\n".join(abstract_memory)
            raw_refs = memory.get("raw_refs", [])
            if not isinstance(raw_refs, list) or not all(isinstance(item, str) for item in raw_refs):
                raise ValueError("Harness raw memory references are invalid")
            state["memory_refs"] = tuple(raw_refs)
            declared_tools = capabilities.get("tools", [])
            if not isinstance(declared_tools, list) or not all(
                isinstance(item, str) and _SAFE_ID.fullmatch(item) for item in declared_tools
            ):
                raise ValueError("Harness capabilities.tools is invalid")
            node_tools = {node.tool for node in artifact.spec.nodes if node.tool is not None}
            if not node_tools.issubset(set(declared_tools)):
                raise ValueError("Harness tool node is not declared in capabilities.tools")
            if set(declared_tools) & FORBIDDEN_EVALUATOR_TOOL_IDS:
                raise ValueError("evaluator tools are forbidden inside the Task Harness")
            raw_agent = capabilities.get("agent")
            if raw_agent is not None:
                if not isinstance(raw_agent, Mapping):
                    raise ValueError("Harness agent configuration is invalid")
                _strict_keys(
                    raw_agent,
                    {"node_id", "max_turns", "max_tool_calls", "workflows"},
                    "Harness agent configuration",
                )
                agent_node_id = _safe_id(raw_agent.get("node_id"), "Harness agent node")
                max_turns = raw_agent.get("max_turns")
                max_tool_calls = raw_agent.get("max_tool_calls")
                for label, value, upper_bound in (
                    ("max_turns", max_turns, 128),
                    ("max_tool_calls", max_tool_calls, 128),
                ):
                    if (
                        not isinstance(value, int)
                        or isinstance(value, bool)
                        or value < 1
                        or value > upper_bound
                    ):
                        raise ValueError(f"Harness agent {label} is invalid")
                matching = [node for node in artifact.spec.nodes if node.node_id == agent_node_id]
                if len(matching) != 1 or matching[0].kind != "model_call":
                    raise ValueError("Harness agent node must name one model_call node")
                if tool_registry is None:
                    raise ValueError("Harness agent mode requires a fixed ToolRegistry")
                if tool_workspace is None or operation_scope is None:
                    raise ValueError(
                        "Harness agent mode requires tool_workspace and operation_scope"
                    )
                missing_tools = set(declared_tools) - set(tool_registry.definitions)
                if missing_tools:
                    raise ValueError(
                        f"Harness agent tools are absent from ToolRegistry: {sorted(missing_tools)}"
                    )
                workflows = raw_agent.get("workflows", [])
                if not isinstance(workflows, list) or any(
                    not isinstance(item, str) or _SAFE_ID.fullmatch(item) is None
                    for item in workflows
                ):
                    raise ValueError("Harness agent workflows are invalid")
                if len(set(workflows)) != len(workflows):
                    raise ValueError("Harness agent workflows must be unique")
                try:
                    _STANDARD_WORKFLOWS.public_catalog(workflows)
                except KeyError as exc:
                    raise ValueError("Harness agent workflow is not registered") from exc
                agent_config = {
                    "node_id": agent_node_id,
                    "max_turns": max_turns,
                    "max_tool_calls": max_tool_calls,
                    "declared_tools": tuple(declared_tools),
                    "workflows": tuple(workflows),
                }
            static_nodes = [node for node in artifact.spec.nodes if node.kind == "tool_call"]
            if static_nodes:
                if tool_registry is None:
                    raise ValueError("schema 2 static tool nodes require a fixed ToolRegistry")
                missing_tools = {
                    node.tool for node in static_nodes if node.tool not in tool_registry.definitions
                }
                if missing_tools:
                    raise ValueError(
                        f"Harness static tools are absent from ToolRegistry: {sorted(missing_tools)}"
                    )
                if tool_workspace is None or operation_scope is None:
                    raise ValueError(
                        "schema 2 static tool nodes require tool_workspace and operation_scope"
                    )
                static_tool_session = tool_registry.bind(
                    ToolPolicy(
                        allow=tuple(declared_tools),
                        deny=(),
                        max_calls=max(1, len(static_nodes)),
                    ),
                    workspace=tool_workspace,
                )
            skills = capabilities.get("skills", [])
            if not isinstance(skills, list):
                raise ValueError("Harness skills must be a list")
            skill_map: dict[str, str] = {}
            for entry in skills:
                if not isinstance(entry, Mapping):
                    raise ValueError("Harness skill entry is invalid")
                skill_id = _safe_id(entry.get("id"), "Harness skill")
                prompt = entry.get("prompt")
                if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 16_000:
                    raise ValueError("Harness skill prompt is invalid")
                if skill_id in skill_map:
                    raise ValueError("Harness skill ids must be unique")
                skill_map[skill_id] = prompt
            state["skills"] = skill_map
            directive = router.get("directive", "")
            if not isinstance(directive, str) or len(directive) > 16_000:
                raise ValueError("Harness router directive is invalid")
            state["search_directive"] = directive
            order = router.get("execution_order")
            if order is not None:
                if not isinstance(order, list) or not all(isinstance(item, str) for item in order):
                    raise ValueError("Harness router execution_order is invalid")
                if len(order) != len(artifact.spec.nodes) or set(order) != {
                    node.node_id for node in artifact.spec.nodes
                }:
                    raise ValueError("Harness router execution_order must cover every node")
                if order[-1] != artifact.spec.nodes[-1].node_id:
                    raise ValueError("Harness router must leave emit node last")
                nodes_by_id = {node.node_id: node for node in artifact.spec.nodes}
                execution_nodes = [nodes_by_id[node_id] for node_id in order]
            else:
                execution_nodes = list(artifact.spec.nodes)
        else:
            execution_nodes = list(artifact.spec.nodes)
        state.update(initial_state or {})
        events: list[HarnessTraceEvent] = []
        model_call_scopes: list[str] = []
        candidate: str | None = None
        final_model_node_id = self._final_model_node_id(execution_nodes)
        for index, node in enumerate(execution_nodes):
            if node.kind == "model_call":
                assert node.prompt is not None and node.role is not None
                allowed_keys = {"task"} | {item.node_id for item in execution_nodes}
                rendered = _render_prompt(node.prompt, state, allowed_keys=allowed_keys)
                context = ""
                if artifact.spec.schema_version == 2:
                    context = (
                        "\n\nHarness context:\n"
                        f"Constraints: {json.dumps(state.get('constraints', {}), sort_keys=True)}\n"
                        f"Search directive: {state.get('search_directive', '')}\n"
                        f"Reusable memory:\n{state.get('memory', '')}\n"
                        f"Memory references: {json.dumps(state.get('memory_refs', ()), sort_keys=True)}\n"
                        f"Available skills: {json.dumps(sorted(state.get('skills', {})), sort_keys=True)}"
                    )
                prompt = f"Role: {node.role}\n\n{rendered}{context}"
                if node.node_id == final_model_node_id and self.output_contract is not None:
                    prompt += self._output_contract_block(
                        self.output_contract, self.output_contract_sha256
                    )
                if agent_config is not None and node.node_id == agent_config["node_id"]:
                    assert tool_registry is not None
                    session = tool_registry.bind(
                        ToolPolicy(
                            allow=agent_config["declared_tools"],
                            deny=(),
                            max_calls=agent_config["max_tool_calls"],
                        ),
                        workspace=tool_workspace,
                    )
                    agent_prompt = self._agent_protocol_block(
                        prompt,
                        agent_config["declared_tools"],
                        agent_config["workflows"],
                    )

                    # Agent call numbering is local to the Agent node.  The
                    # surrounding Harness may already have called another
                    # model node, but that must not shift the durable
                    # ``solve.agent.0000`` identity used for replay/audit.
                    agent_call_index = 0

                    def model_step(turn_prompt: str) -> str:
                        nonlocal agent_call_index
                        scope = f"{node.node_id}.agent.{agent_call_index:04d}"
                        agent_call_index += 1
                        model_call_scopes.append(scope)
                        return self._generate(turn_prompt, model=model, scope=scope)

                    agent_run = AgentRuntime(
                        session,
                        operation_scope=f"{operation_scope}-{node.node_id}",
                        max_turns=agent_config["max_turns"],
                        workflow_registry=_STANDARD_WORKFLOWS,
                        allowed_workflows=agent_config["workflows"],
                    ).run(model_step, initial_prompt=agent_prompt)
                    for turn in agent_run.turns:
                        events.append(
                            HarnessTraceEvent(
                                index=len(events),
                                node_id=f"{node.node_id}.agent.{turn.index:04d}",
                                kind="model_call",
                                input=turn.model_input,
                                output=turn.model_output,
                            )
                        )
                        if turn.tool_result is not None:
                            events.append(
                                HarnessTraceEvent(
                                    index=len(events),
                                    node_id=f"{node.node_id}.tool.{turn.index:04d}",
                                    kind="tool_call",
                                    input=dict(turn.action.arguments or {}),
                                    output={
                                        "value": turn.tool_result.value,
                                        "receipt": turn.tool_result.receipt.to_dict(),
                                    },
                                )
                            )
                        elif turn.action.kind == "workflow":
                            assert turn.action.workflow is not None
                            events.append(
                                HarnessTraceEvent(
                                    index=len(events),
                                    node_id=f"{node.node_id}.workflow.{turn.index:04d}",
                                    kind="workflow_select",
                                    input=turn.action.workflow,
                                    output=_STANDARD_WORKFLOWS.require(
                                        turn.action.workflow
                                    ).public_payload(),
                                )
                            )
                    response = agent_run.candidate
                    state[node.node_id] = response
                    state["latest_output"] = response
                    continue
                scope = node.node_id
                model_call_scopes.append(scope)
                response = self._generate(prompt, model=model, scope=scope)
                state[node.node_id] = response
                state["latest_output"] = response
                event_input = prompt
                output = response
            elif node.kind == "tool_call":
                assert node.tool is not None
                if node.input_key not in state:
                    raise ValueError(f"Harness tool input is unavailable: {node.input_key}")
                event_input = state[node.input_key]
                if static_tool_session is not None:
                    arguments = (
                        dict(event_input)
                        if isinstance(event_input, Mapping)
                        else {"candidate": event_input}
                    )
                    operation_id = (
                        f"{operation_scope}.{node.node_id}.{static_tool_call_index:04d}"
                        if operation_scope is not None
                        else f"task.{node.node_id}.{static_tool_call_index:04d}"
                    )
                    static_tool_call_index += 1
                    tool_result = static_tool_session.call(
                        node.tool,
                        arguments,
                        operation_id=operation_id,
                    )
                    output = {
                        "value": tool_result.value,
                        "receipt": tool_result.receipt.to_dict(),
                    }
                else:
                    operation = tools.get(node.tool)
                    if operation is None:
                        raise ValueError(f"Harness tool is not allowlisted: {node.tool}")
                    output = operation(event_input)
                state[node.node_id] = output
            elif node.kind == "skill_call":
                skill_map = state.get("skills", {})
                if not isinstance(skill_map, Mapping) or node.skill not in skill_map:
                    raise ValueError(f"Harness skill is not allowlisted: {node.skill}")
                event_input = state[node.input_key]
                output = f"{skill_map[node.skill]}\nInput: {event_input}"
                state[node.node_id] = output
            else:
                if node.input_key not in state:
                    raise ValueError(f"Harness emit input is unavailable: {node.input_key}")
                event_input = state[node.input_key]
                if not isinstance(event_input, str) or not event_input.strip():
                    raise ValueError("Harness emit value must be non-empty text")
                candidate = event_input
                output = candidate
            events.append(
                HarnessTraceEvent(
                    index=len(events),
                    node_id=node.node_id,
                    kind=node.kind,
                    input=event_input,
                    output=output,
                )
            )
        if candidate is None:
            raise RuntimeError("Task Harness completed without a candidate")
        return TaskHarnessRun(
            harness_sha256=artifact.sha256,
            candidate=candidate,
            events=tuple(events),
            output_contract_sha256=self.output_contract_sha256,
            model_call_scopes=tuple(model_call_scopes),
        )

    def _generate(self, prompt: str, *, model: str, scope: str) -> str:
        scoped = getattr(self.generator, "generate_scoped", None)
        if callable(scoped):
            result = scoped(prompt, model=model, scope=scope)
        else:
            result = self.generator.generate(prompt, model=model)
        return result.raw_response.strip()

    @staticmethod
    def _agent_protocol_block(
        prompt: str,
        tools: tuple[str, ...],
        workflows: tuple[str, ...],
    ) -> str:
        return (
            f"{prompt}\n\n"
            "--- TASK HARNESS AGENT ACTION CONTRACT ---\n"
            "You may either call one allowed tool or emit the final benchmark candidate. "
            "Return exactly one JSON object and no markdown. Python assigns operation ids; "
            "do not include one.\n"
            f"Allowed tools: {json.dumps(list(tools), sort_keys=True)}\n"
            f"Allowed fixed workflows: {json.dumps(_STANDARD_WORKFLOWS.public_catalog(workflows), sort_keys=True)}\n"
            'Tool action: {"action":"tool","tool":"TOOL_ID","arguments":{...}}\n'
            'Workflow action: {"action":"workflow","workflow":"WORKFLOW_ID"}\n'
            'Final action: {"action":"emit","candidate":"COMPLETE FINAL CANDIDATE"}\n'
            "The official evaluator is not a tool and cannot be called from this loop.\n"
            "--- END TASK HARNESS AGENT ACTION CONTRACT ---"
        )

    @staticmethod
    def _validated_output_contract(
        value: Mapping[str, Any] | None,
    ) -> dict[str, Any] | None:
        if value is None:
            return None
        if not isinstance(value, Mapping):
            raise TypeError("Task Harness output contract must be a mapping")
        try:
            payload = json.loads(_canonical_json(dict(value)))
        except (TypeError, ValueError) as exc:
            raise ValueError("Task Harness output contract must be JSON serializable") from exc
        if not isinstance(payload, dict) or not payload:
            raise ValueError("Task Harness output contract must be a non-empty object")
        declared = payload.get("skill_sha256")
        if declared is not None:
            if not isinstance(declared, str) or _SHA256.fullmatch(declared) is None:
                raise ValueError("Task Harness output contract skill hash is invalid")
            public_payload = dict(payload)
            del public_payload["skill_sha256"]
            actual = hashlib.sha256(_canonical_json(public_payload).encode("utf-8")).hexdigest()
            if actual != declared:
                raise ValueError("Task Harness output contract skill hash differs")
        return payload

    @staticmethod
    def _output_contract_sha256(value: Mapping[str, Any] | None) -> str | None:
        if value is None:
            return None
        declared = value.get("skill_sha256")
        if isinstance(declared, str):
            return declared
        return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()

    @staticmethod
    def _final_model_node_id(nodes: list[TaskHarnessNode]) -> str | None:
        source_by_key: dict[str, str | None] = {"latest_output": None}
        for node in nodes:
            if node.kind == "model_call":
                source_by_key[node.node_id] = node.node_id
                source_by_key["latest_output"] = node.node_id
            elif node.kind in {"tool_call", "skill_call"}:
                source_by_key[node.node_id] = source_by_key.get(node.input_key)
            else:
                return source_by_key.get(node.input_key)
        return None

    @staticmethod
    def _output_contract_block(
        contract: Mapping[str, Any], contract_sha256: str | None
    ) -> str:
        assert contract_sha256 is not None
        return (
            "\n\n--- AUTHORITATIVE OUTPUT CONTRACT ---\n"
            "This public contract is bound by Python and the benchmark evaluator. "
            "It is higher priority than any conflicting output-format instruction "
            "inside the mutable Harness. Apply this benchmark contract only to the "
            "string inside the final emit.candidate field. It does not constrain the "
            "Agent action JSON wrapper and does not apply to intermediate "
            "tool/workflow actions.\n"
            f"contract_skill_sha256: {contract_sha256}\n"
            f"contract: {_canonical_json(contract)}\n"
            "Before returning, check the response boundary and literal template exactly.\n"
            "--- END AUTHORITATIVE OUTPUT CONTRACT ---"
        )


class HarnessWorkspace:
    """Content-addressed artifact lineage and queryable public run traces."""

    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.artifacts_root = self.root / "artifacts"
        self.harness_history_bindings_root = self.root / "harness_history_bindings"
        self.runs_root = self.root / "runs"
        self.run_bindings_root = self.root / "run_bindings"
        self.builder_harnesses_root = self.root / "builder_harnesses"
        self.builder_runs_root = self.root / "builder_runs"
        self.builder_run_bindings_root = self.root / "builder_run_bindings"
        self.round_receipts_root = self.root / "round_receipts"
        self.round_receipt_bindings_root = self.root / "round_receipt_bindings"
        self.round_assessments_root = self.root / "round_assessments"
        self.round_assessment_bindings_root = self.root / "round_assessment_bindings"
        self.solver_results_root = self.root / "solver_results"
        self.solver_result_bindings_root = self.root / "solver_result_bindings"
        self.operation_claims_root = self.root / "operation_claims"
        self.operation_claim_bindings_root = self.root / "operation_claim_bindings"
        self.operation_results_root = self.root / "operation_results"
        self.operation_result_bindings_root = self.root / "operation_result_bindings"
        self.commit_receipts_root = self.root / "commit_receipts"
        self.commit_receipt_bindings_root = self.root / "commit_receipt_bindings"
        self.candidate_archive_root = self.root / "candidate_archive"
        self.candidate_archive_bindings_root = self.root / "candidate_archive_bindings"
        self.gate_decisions_root = self.root / "gate_decisions"
        self.gate_decision_bindings_root = self.root / "gate_decision_bindings"
        self.promotion_receipts_root = self.root / "promotion_receipts"
        self.promotion_receipt_bindings_root = self.root / "promotion_receipt_bindings"
        self.abandoned_rounds_root = self.root / "abandoned_rounds"
        self.abandoned_round_bindings_root = self.root / "abandoned_round_bindings"
        self.locks_root = self.root / "locks"
        self.binding_sequence_path = self.root / "binding_sequence.json"
        self.task_identity_path = self.root / "task_identity.json"
        self.current_path = self.root / "current.json"
        self.champion_path = self.root / "champion.json"
        self._content_binding_roots = (
            self.harness_history_bindings_root,
            self.run_bindings_root,
            self.builder_run_bindings_root,
            self.round_receipt_bindings_root,
            self.round_assessment_bindings_root,
            self.solver_result_bindings_root,
            self.operation_claim_bindings_root,
            self.operation_result_bindings_root,
            self.commit_receipt_bindings_root,
            self.candidate_archive_bindings_root,
            self.gate_decision_bindings_root,
            self.promotion_receipt_bindings_root,
            self.abandoned_round_bindings_root,
        )
        self.artifacts_root.mkdir(parents=True, exist_ok=True)
        self.harness_history_bindings_root.mkdir(parents=True, exist_ok=True)
        self.runs_root.mkdir(parents=True, exist_ok=True)
        self.run_bindings_root.mkdir(parents=True, exist_ok=True)
        self.builder_harnesses_root.mkdir(parents=True, exist_ok=True)
        self.builder_runs_root.mkdir(parents=True, exist_ok=True)
        self.builder_run_bindings_root.mkdir(parents=True, exist_ok=True)
        self.round_receipts_root.mkdir(parents=True, exist_ok=True)
        self.round_receipt_bindings_root.mkdir(parents=True, exist_ok=True)
        self.round_assessments_root.mkdir(parents=True, exist_ok=True)
        self.round_assessment_bindings_root.mkdir(parents=True, exist_ok=True)
        self.solver_results_root.mkdir(parents=True, exist_ok=True)
        self.solver_result_bindings_root.mkdir(parents=True, exist_ok=True)
        self.operation_claims_root.mkdir(parents=True, exist_ok=True)
        self.operation_claim_bindings_root.mkdir(parents=True, exist_ok=True)
        self.operation_results_root.mkdir(parents=True, exist_ok=True)
        self.operation_result_bindings_root.mkdir(parents=True, exist_ok=True)
        self.commit_receipts_root.mkdir(parents=True, exist_ok=True)
        self.commit_receipt_bindings_root.mkdir(parents=True, exist_ok=True)
        self.candidate_archive_root.mkdir(parents=True, exist_ok=True)
        self.candidate_archive_bindings_root.mkdir(parents=True, exist_ok=True)
        self.gate_decisions_root.mkdir(parents=True, exist_ok=True)
        self.gate_decision_bindings_root.mkdir(parents=True, exist_ok=True)
        self.promotion_receipts_root.mkdir(parents=True, exist_ok=True)
        self.promotion_receipt_bindings_root.mkdir(parents=True, exist_ok=True)
        self.abandoned_rounds_root.mkdir(parents=True, exist_ok=True)
        self.abandoned_round_bindings_root.mkdir(parents=True, exist_ok=True)
        self.locks_root.mkdir(parents=True, exist_ok=True)

    def artifact_path(self, sha256: str) -> Path:
        if _SHA256.fullmatch(sha256) is None:
            raise ValueError("artifact hash is invalid")
        return self.artifacts_root / f"{sha256}.json"

    def store_artifact(self, artifact: TaskHarnessArtifact) -> TaskHarnessArtifact:
        validated = TaskHarnessArtifact.from_dict(artifact.to_dict())
        self._write_json(self.artifact_path(validated.sha256), validated.to_dict())
        return validated

    def commit(
        self,
        artifact: TaskHarnessArtifact,
        *,
        owner_run_id: str | None = None,
        update_champion: bool = True,
        allow_branch: bool = False,
    ) -> TaskHarnessArtifact:
        validated = self.store_artifact(artifact)
        if owner_run_id is not None:
            owner_run_id = _safe_id(owner_run_id, "commit owner run id")
        with self._exclusive_lock(self.locks_root / "current.lock"):
            if self.current_path.exists():
                current = self.current()
                if not allow_branch and validated.parent_sha256 != current.sha256:
                    raise ValueError("new Harness parent does not match current artifact")
                if not allow_branch and validated.version != current.version + 1:
                    raise ValueError("new Harness version is not sequential")
            elif validated.parent_sha256 is not None or validated.version != 1:
                raise ValueError("initial Harness must be parentless version one")
            self._store_content_addressed(
                payload=validated.to_dict(),
                objects_root=self.artifacts_root,
                bindings_root=self.harness_history_bindings_root,
                binding_id=validated.sha256,
                label="committed Harness history",
            )
            if owner_run_id is not None:
                self._record_commit_receipt(
                    run_id=owner_run_id,
                    previous_sha256=validated.parent_sha256,
                    candidate_sha256=validated.sha256,
                    update_champion=update_champion,
                )
            self._replace_json(self.current_path, {"sha256": validated.sha256})
            if update_champion or not hasattr(self, "champion_path"):
                self._replace_json(self.champion_path, {"sha256": validated.sha256})
        return validated

    def same_lineage(self, first_sha256: str, second_sha256: str) -> bool:
        """Return whether two artifacts share the same root in the immutable DAG."""

        def root(sha256: str) -> str:
            seen: set[str] = set()
            current = self.load_artifact(sha256)
            while current.parent_sha256 is not None:
                if current.sha256 in seen:
                    raise ValueError("Harness artifact lineage contains a cycle")
                seen.add(current.sha256)
                current = self.load_artifact(current.parent_sha256)
            return current.sha256

        return root(first_sha256) == root(second_sha256)

    def recover_owned_commit(self, run_id: str) -> TaskHarnessArtifact:
        receipt = self.load_commit_receipt(run_id)
        assert receipt is not None
        candidate = self.load_artifact(receipt["candidate_sha256"])
        if candidate.parent_sha256 != receipt["previous_sha256"]:
            raise ValueError("commit receipt lineage is invalid")
        with self._exclusive_lock(self.locks_root / "current.lock"):
            current = self.current()
            if current.sha256 == candidate.sha256:
                return candidate
            if (
                current.sha256 != candidate.parent_sha256
                and not self.same_lineage(current.sha256, candidate.parent_sha256)
            ):
                raise RuntimeError("owned commit cannot be recovered over a different Harness")
            self._replace_json(self.current_path, {"sha256": candidate.sha256})
            if receipt.get("update_champion", True):
                self._replace_json(self.champion_path, {"sha256": candidate.sha256})
        return candidate

    def current(self) -> TaskHarnessArtifact:
        if not self.current_path.is_file():
            raise ValueError("Harness workspace has no current artifact")
        binding = json.loads(self.current_path.read_text(encoding="utf-8"))
        sha256 = binding.get("sha256") if isinstance(binding, dict) else None
        return self.load_artifact(sha256)

    def champion(self) -> TaskHarnessArtifact:
        """Return the incumbent Harness.

        ``current`` remains as a compatibility alias for historical linear
        lineages.  New portfolio evolution code uses the explicit champion
        term so an archived challenger is never confused with the incumbent.
        """

        if self.champion_path.is_file():
            binding = json.loads(self.champion_path.read_text(encoding="utf-8"))
            sha256 = binding.get("sha256") if isinstance(binding, dict) else None
            return self.load_artifact(sha256)
        return self.current()

    def set_champion(self, sha256: str) -> TaskHarnessArtifact:
        """Promote an already stored artifact without changing the active pointer."""

        artifact = self.load_artifact(sha256)
        with self._exclusive_lock(self.locks_root / "champion.lock"):
            self._replace_json(self.champion_path, {"sha256": artifact.sha256})
        return artifact

    def load_artifact(self, sha256: str) -> TaskHarnessArtifact:
        path = self.artifact_path(sha256)
        artifact = TaskHarnessArtifact.from_dict(json.loads(path.read_text(encoding="utf-8")))
        if artifact.sha256 != sha256:
            raise ValueError("current Harness binding failed content verification")
        return artifact

    def record_trace(
        self,
        *,
        run_id: str,
        harness_sha256: str,
        candidate: str,
        task_sha256: str,
        request_sha256: str,
        solver_model: str,
        events: tuple[HarnessTraceEvent, ...],
        score: float | None,
        feedback: str,
    ) -> Path:
        run_id = _safe_id(run_id, "run id")
        if _SHA256.fullmatch(harness_sha256) is None:
            raise ValueError("run Harness hash is invalid")
        if _SHA256.fullmatch(task_sha256) is None:
            raise ValueError("run task hash is invalid")
        if _SHA256.fullmatch(request_sha256) is None:
            raise ValueError("run request hash is invalid")
        if not isinstance(candidate, str) or not candidate.strip():
            raise ValueError("run candidate is invalid")
        if not isinstance(solver_model, str) or not solver_model.strip():
            raise ValueError("run solver model is invalid")
        if score is not None and (not isinstance(score, (int, float)) or isinstance(score, bool)):
            raise ValueError("run score is invalid")
        if not isinstance(feedback, str):
            raise ValueError("run feedback is invalid")
        payload = {
            "schema_version": 1,
            "run_id": run_id,
            "harness_sha256": harness_sha256,
            "candidate": candidate,
            "task_sha256": task_sha256,
            "request_sha256": request_sha256,
            "solver_model": solver_model,
            "events": [asdict(event) for event in events],
            "score": score,
            "feedback": feedback,
        }
        with self._exclusive_lock(self.locks_root / "task-identity.lock"):
            existing_runs = [
                self.load_trace(path.stem)
                for path in self.run_bindings_root.glob("*.json")
            ]
            identity = self._validated_task_identity(existing_runs)
            if identity is not None and identity != task_sha256:
                raise ValueError("run task identity differs from this workspace")
            if not self.task_identity_path.is_file():
                self._write_json(
                    self.task_identity_path, {"task_sha256": task_sha256}
                )
            return self._store_content_addressed(
                payload=payload,
                objects_root=self.runs_root,
                bindings_root=self.run_bindings_root,
                binding_id=run_id,
                label="run trace",
            )

    def load_trace(self, run_id: str, *, missing_ok: bool = False) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.runs_root,
            bindings_root=self.run_bindings_root,
            binding_id=run_id,
            label="run trace",
            missing_ok=missing_ok,
        )

    def inspect(self) -> dict[str, Any]:
        current = self.current()
        evidence_paths = self._binding_paths_in_evidence_order(
            self.harness_history_bindings_root,
            self.run_bindings_root,
            self.builder_run_bindings_root,
            self.commit_receipt_bindings_root,
            self.candidate_archive_bindings_root,
        )
        harness_artifacts_by_path: dict[Path, TaskHarnessArtifact] = {}
        for path in evidence_paths:
            if path.parent != self.harness_history_bindings_root:
                continue
            payload = self._load_content_addressed(
                objects_root=self.artifacts_root,
                bindings_root=self.harness_history_bindings_root,
                binding_id=path.stem,
                label="committed Harness history",
                missing_ok=False,
            )
            assert payload is not None
            artifact = TaskHarnessArtifact.from_dict(payload)
            if artifact.sha256 != path.stem:
                raise ValueError("committed Harness history binding is invalid")
            harness_artifacts_by_path[path] = artifact
        runs_by_path = {
            path: self.load_trace(path.stem)
            for path in evidence_paths
            if path.parent == self.run_bindings_root
        }
        runs = list(runs_by_path.values())
        self._validated_task_identity(runs)
        builder_traces_by_path = {
            path: self.load_builder_trace(path.stem)
            for path in evidence_paths
            if path.parent == self.builder_run_bindings_root
        }
        commit_receipts_by_path = {
            path: self.load_commit_receipt(path.stem)
            for path in evidence_paths
            if path.parent == self.commit_receipt_bindings_root
        }
        archives_by_path = {
            path: self.load_archived_candidate(path.stem)
            for path in evidence_paths
            if path.parent == self.candidate_archive_bindings_root
        }
        traced_decision_ids = {
            trace["run_id"]
            for trace in builder_traces_by_path.values()
            if trace is not None
        }
        promotions_by_proposal = {
            receipt["proposal_id"]: receipt for receipt in self.promotion_receipts()
        }

        referenced: list[str] = []
        referenced_set: set[str] = set()
        public_runs: dict[str, list[dict[str, Any]]] = {}
        decisions: dict[str, list[dict[str, Any]]] = {}

        def reference(sha256: str | None) -> None:
            if sha256 is not None and sha256 not in referenced_set:
                referenced_set.add(sha256)
                referenced.append(sha256)

        for path in evidence_paths:
            if path.parent == self.harness_history_bindings_root:
                reference(harness_artifacts_by_path[path].sha256)
            elif path.parent == self.run_bindings_root:
                run = runs_by_path[path]
                assert run is not None
                harness_sha256 = run["harness_sha256"]
                reference(harness_sha256)
                public_runs.setdefault(harness_sha256, []).append(
                    {
                        "run_id": run["run_id"],
                        "score": run["score"],
                        "feedback": run["feedback"],
                        "status": (
                            "scored" if run["score"] is not None else "completed"
                        ),
                        "events": [
                            {
                                "index": event["index"],
                                "node_id": event["node_id"],
                                "kind": event["kind"],
                            }
                            for event in run["events"]
                        ],
                    }
                )
            elif path.parent == self.builder_run_bindings_root:
                trace = builder_traces_by_path[path]
                assert trace is not None
                for key in (
                    "previous_harness_sha256",
                    "candidate_harness_sha256",
                    "next_harness_sha256",
                    "source_sha256",
                ):
                    reference(trace.get(key))
                candidate_sha256 = trace.get("candidate_harness_sha256")
                if candidate_sha256 is not None:
                    decisions.setdefault(candidate_sha256, []).append(
                        {
                            "run_id": trace["run_id"],
                            "status": trace["status"],
                            "reason": trace["reason"],
                            "previous_harness_sha256": trace[
                                "previous_harness_sha256"
                            ],
                            "source_sha256": trace.get("source_sha256"),
                            "base_sha256": trace.get("source_sha256"),
                            "candidate_harness_sha256": candidate_sha256,
                            "next_harness_sha256": trace["next_harness_sha256"],
                            "changed_components": list(
                                trace.get("changed_components", ())
                            ),
                        }
                    )
            elif path.parent == self.commit_receipt_bindings_root:
                receipt = commit_receipts_by_path[path]
                assert receipt is not None
                reference(receipt["previous_sha256"])
                reference(receipt["candidate_sha256"])
                if receipt["run_id"] not in traced_decision_ids:
                    decisions.setdefault(receipt["candidate_sha256"], []).append(
                        {
                            "run_id": receipt["run_id"],
                            "status": "committed",
                            "reason": "owned Harness commit",
                            "previous_harness_sha256": receipt["previous_sha256"],
                            "source_sha256": receipt["previous_sha256"],
                            "base_sha256": receipt["previous_sha256"],
                            "candidate_harness_sha256": receipt[
                                "candidate_sha256"
                            ],
                            "next_harness_sha256": receipt["candidate_sha256"],
                            "changed_components": [],
                        }
                    )
            else:
                archive = archives_by_path[path]
                assert archive is not None
                candidate_sha256 = archive["candidate_sha256"]
                reference(archive["parent_sha256"])
                reference(candidate_sha256)
                gate = self.load_gate_decision(
                    archive["proposal_id"], missing_ok=True
                )
                promotion = promotions_by_proposal.get(archive["proposal_id"])
                if promotion is not None:
                    status = "committed"
                    reason = (
                        gate["reason"]
                        if gate is not None
                        else "promoted by public Gate"
                    )
                    next_sha256 = candidate_sha256
                elif gate is not None:
                    status = "rejected"
                    reason = gate["reason"]
                    next_sha256 = gate["incumbent_sha256"]
                else:
                    status = "proposed"
                    reason = archive["reason"]
                    next_sha256 = archive["parent_sha256"]
                decisions.setdefault(candidate_sha256, []).append(
                    {
                        "run_id": archive["proposal_id"],
                        "status": status,
                        "reason": reason,
                        "previous_harness_sha256": archive["parent_sha256"],
                        "source_sha256": archive["parent_sha256"],
                        "base_sha256": archive["parent_sha256"],
                        "candidate_harness_sha256": candidate_sha256,
                        "next_harness_sha256": next_sha256,
                        "changed_components": [],
                    }
                )

        reference(current.sha256)

        lineage_artifacts: dict[str, TaskHarnessArtifact] = {}

        def include_with_ancestors(sha256: str) -> None:
            seen: set[str] = set()
            while sha256 not in lineage_artifacts:
                if sha256 in seen:
                    raise ValueError("Harness artifact lineage contains a cycle")
                seen.add(sha256)
                artifact = self.load_artifact(sha256)
                lineage_artifacts[sha256] = artifact
                if artifact.parent_sha256 is None:
                    break
                sha256 = artifact.parent_sha256

        for sha256 in referenced:
            include_with_ancestors(sha256)
        for sha256 in lineage_artifacts:
            if not self.same_lineage(sha256, current.sha256):
                raise ValueError(
                    "experiment evidence references a different Harness lineage"
                )

        public_harness_sha256s = set(referenced)

        def public_artifact(artifact: TaskHarnessArtifact) -> dict[str, Any]:
            payload = artifact.to_dict()
            if artifact.parent_sha256 not in public_harness_sha256s:
                payload["parent_sha256"] = None
            return payload

        available_harnesses = []
        for sha256 in referenced:
            artifact = lineage_artifacts[sha256]
            harness_runs = public_runs.get(artifact.sha256, [])
            artifact_view = public_artifact(artifact)
            available_harnesses.append(
                {
                    "sha256": artifact.sha256,
                    "schema_version": artifact.schema_version,
                    "version": artifact.version,
                    "parent_sha256": artifact_view["parent_sha256"],
                    "spec": artifact_view["spec"],
                    "is_current": artifact.sha256 == current.sha256,
                    "runs": harness_runs,
                    "decisions": decisions.get(artifact.sha256, []),
                    "adoption": {
                        "used": bool(harness_runs),
                        "run_ids": [run["run_id"] for run in harness_runs],
                    },
                }
            )
        return {
            "current_sha256": current.sha256,
            "current_artifact": public_artifact(current),
            "runs": runs,
            "available_harnesses": available_harnesses,
        }

    def _validated_task_identity(
        self, runs: Sequence[Mapping[str, Any] | None]
    ) -> str | None:
        identities: set[str] = set()
        if self.task_identity_path.is_file():
            payload = json.loads(self.task_identity_path.read_text(encoding="utf-8"))
            identity = payload.get("task_sha256") if isinstance(payload, dict) else None
            if not isinstance(identity, str) or _SHA256.fullmatch(identity) is None:
                raise ValueError("workspace task identity is invalid")
            identities.add(identity)
        for run in runs:
            assert run is not None
            task_sha256 = run.get("task_sha256")
            if not isinstance(task_sha256, str) or _SHA256.fullmatch(task_sha256) is None:
                raise ValueError("run task identity is invalid")
            identities.add(task_sha256)
        if len(identities) > 1:
            raise ValueError("run task identity differs within this workspace")
        return next(iter(identities), None)

    def record_archived_candidate(
        self,
        *,
        proposal_id: str,
        payload: Mapping[str, Any],
    ) -> Path:
        """Append one immutable Builder proposal to the candidate archive."""

        proposal_id = _safe_id(proposal_id, "candidate archive proposal id")
        candidate_sha256 = payload.get("candidate_sha256")
        parent_sha256 = payload.get("parent_sha256")
        attempt_index = payload.get("attempt_index")
        mutation_family = payload.get("mutation_family")
        forced_restart = payload.get("forced_restart")
        if (
            not isinstance(candidate_sha256, str)
            or _SHA256.fullmatch(candidate_sha256) is None
        ):
            raise ValueError("archived candidate hash is invalid")
        if (
            not isinstance(parent_sha256, str)
            or _SHA256.fullmatch(parent_sha256) is None
        ):
            raise ValueError("archived candidate parent hash is invalid")
        if (
            not isinstance(attempt_index, int)
            or isinstance(attempt_index, bool)
            or attempt_index < 0
        ):
            raise ValueError("archived candidate attempt index is invalid")
        if (
            not isinstance(mutation_family, str)
            or _SAFE_ID.fullmatch(mutation_family) is None
        ):
            raise ValueError("archived candidate mutation family is invalid")
        if type(forced_restart) is not bool:
            raise ValueError("archived candidate restart flag is invalid")
        candidate = self.load_artifact(candidate_sha256)
        if candidate.parent_sha256 != parent_sha256:
            raise ValueError("archived candidate lineage is invalid")
        archive_payload = dict(payload)
        archive_payload.update(
            {
                "schema_version": 1,
                "proposal_id": proposal_id,
                "candidate_sha256": candidate_sha256,
                "parent_sha256": parent_sha256,
            }
        )
        return self._store_content_addressed(
            payload=archive_payload,
            objects_root=self.candidate_archive_root,
            bindings_root=self.candidate_archive_bindings_root,
            binding_id=proposal_id,
            label="candidate archive record",
        )

    def load_archived_candidate(
        self, proposal_id: str, *, missing_ok: bool = False
    ) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.candidate_archive_root,
            bindings_root=self.candidate_archive_bindings_root,
            binding_id=proposal_id,
            label="candidate archive record",
            missing_ok=missing_ok,
        )

    def archived_candidates(self) -> tuple[dict[str, Any], ...]:
        records: list[dict[str, Any]] = []
        for path in self._binding_paths_in_evidence_order(
            self.candidate_archive_bindings_root
        ):
            record = self.load_archived_candidate(path.stem)
            assert record is not None
            records.append(record)
        return tuple(records)

    def record_gate_decision(
        self,
        *,
        proposal_id: str,
        payload: Mapping[str, Any],
    ) -> Path:
        """Persist the typed public projection of an external Gate decision."""

        proposal_id = _safe_id(proposal_id, "Gate proposal id")
        archive = self.load_archived_candidate(proposal_id)
        assert archive is not None
        if payload.get("candidate_sha256") != archive["candidate_sha256"]:
            raise ValueError("Gate decision candidate differs from the archive")
        incumbent_sha256 = payload.get("incumbent_sha256")
        evaluator_contract_sha256 = payload.get("evaluator_contract_sha256")
        if (
            not isinstance(evaluator_contract_sha256, str)
            or _SHA256.fullmatch(evaluator_contract_sha256) is None
        ):
            raise ValueError("Gate evaluator contract hash is invalid")
        if (
            not isinstance(incumbent_sha256, str)
            or _SHA256.fullmatch(incumbent_sha256) is None
        ):
            raise ValueError("Gate incumbent hash is invalid")
        if type(payload.get("passed")) is not bool or type(
            payload.get("credible_improvement")
        ) is not bool:
            raise ValueError("Gate decision booleans are invalid")
        if (
            payload.get("credible_improvement") is True
            and payload.get("passed") is not True
        ):
            raise ValueError("rejected Gate decision cannot claim credible improvement")
        gate_payload = dict(payload)
        gate_payload.update({"schema_version": 1, "proposal_id": proposal_id})
        return self._store_content_addressed(
            payload=gate_payload,
            objects_root=self.gate_decisions_root,
            bindings_root=self.gate_decision_bindings_root,
            binding_id=proposal_id,
            label="Gate decision",
        )

    def load_gate_decision(
        self, proposal_id: str, *, missing_ok: bool = False
    ) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.gate_decisions_root,
            bindings_root=self.gate_decision_bindings_root,
            binding_id=proposal_id,
            label="Gate decision",
            missing_ok=missing_ok,
        )

    def gate_decisions(self) -> tuple[dict[str, Any], ...]:
        decisions: list[dict[str, Any]] = []
        for path in sorted(self.gate_decision_bindings_root.glob("*.json")):
            decision = self.load_gate_decision(path.stem)
            assert decision is not None
            decisions.append(decision)
        return tuple(decisions)

    def promote_archived_candidate(
        self,
        *,
        proposal_id: str,
        owner_run_id: str,
    ) -> TaskHarnessArtifact:
        """Promote a Gate-approved archive entry without deleting the incumbent.

        A challenger may originate from the champion, a Pareto branch, or an
        early stable version.  Promotion therefore moves the champion pointer
        across the immutable artifact DAG instead of requiring a direct child
        of the current champion.
        """

        proposal_id = _safe_id(proposal_id, "promotion proposal id")
        owner_run_id = _safe_id(owner_run_id, "promotion owner run id")
        existing = self.load_promotion_receipt(owner_run_id, missing_ok=True)
        if existing is not None:
            if existing.get("proposal_id") != proposal_id:
                raise ValueError("promotion owner is bound to a different proposal")
            return self.recover_owned_promotion(owner_run_id)
        archive = self.load_archived_candidate(proposal_id)
        gate = self.load_gate_decision(proposal_id)
        assert archive is not None and gate is not None
        if (
            gate.get("passed") is not True
            or gate.get("credible_improvement") is not True
        ):
            raise ValueError("only a credibly improved Gate-approved candidate may be promoted")
        candidate = self.load_artifact(archive["candidate_sha256"])
        if gate.get("candidate_sha256") != candidate.sha256:
            raise ValueError("promotion Gate binding is invalid")
        with self._exclusive_lock(self.locks_root / "current.lock"):
            incumbent = self.champion()
            if gate.get("incumbent_sha256") != incumbent.sha256:
                raise ValueError("promotion Gate was not evaluated against the current champion")
            receipt = {
                "schema_version": 1,
                "owner_run_id": owner_run_id,
                "proposal_id": proposal_id,
                "promotion_index": len(
                    tuple(self.promotion_receipt_bindings_root.glob("*.json"))
                )
                + 1,
                "previous_champion_sha256": incumbent.sha256,
                "candidate_sha256": candidate.sha256,
                "candidate_parent_sha256": candidate.parent_sha256,
                "evaluator_contract_sha256": gate["evaluator_contract_sha256"],
            }
            self._store_content_addressed(
                payload=receipt,
                objects_root=self.promotion_receipts_root,
                bindings_root=self.promotion_receipt_bindings_root,
                binding_id=owner_run_id,
                label="promotion receipt",
            )
            self._replace_json(self.current_path, {"sha256": candidate.sha256})
            self._replace_json(self.champion_path, {"sha256": candidate.sha256})
        return candidate

    def recover_owned_promotion(self, owner_run_id: str) -> TaskHarnessArtifact:
        """Finish or replay a promotion whose receipt was durably written."""

        owner_run_id = _safe_id(owner_run_id, "promotion owner run id")
        receipt = self.load_promotion_receipt(owner_run_id)
        assert receipt is not None
        candidate = self.load_artifact(receipt["candidate_sha256"])
        if candidate.parent_sha256 != receipt["candidate_parent_sha256"]:
            raise ValueError("promotion receipt candidate lineage is invalid")
        with self._exclusive_lock(self.locks_root / "current.lock"):
            current = self.current()
            if current.sha256 == candidate.sha256:
                self._replace_json(self.champion_path, {"sha256": candidate.sha256})
                return candidate
            champion = self.champion()
            if (
                current.sha256 != receipt["previous_champion_sha256"]
                and champion.sha256 != receipt["previous_champion_sha256"]
            ):
                raise RuntimeError("owned promotion cannot replace a different champion")
            self._replace_json(self.current_path, {"sha256": candidate.sha256})
            self._replace_json(self.champion_path, {"sha256": candidate.sha256})
        return candidate

    def load_promotion_receipt(
        self, owner_run_id: str, *, missing_ok: bool = False
    ) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.promotion_receipts_root,
            bindings_root=self.promotion_receipt_bindings_root,
            binding_id=owner_run_id,
            label="promotion receipt",
            missing_ok=missing_ok,
        )

    def promotion_receipts(self) -> tuple[dict[str, Any], ...]:
        receipts: list[dict[str, Any]] = []
        for path in self.promotion_receipt_bindings_root.glob("*.json"):
            receipt = self.load_promotion_receipt(path.stem)
            assert receipt is not None
            receipts.append(receipt)
        return tuple(sorted(receipts, key=lambda item: item["promotion_index"]))

    def store_builder_harness(self, *, sha256: str, payload: Mapping[str, Any]) -> Path:
        if _SHA256.fullmatch(sha256) is None:
            raise ValueError("Builder Harness hash is invalid")
        if hashlib.sha256(_canonical_json(payload).encode("utf-8")).hexdigest() != sha256:
            raise ValueError("Builder Harness content does not match its hash")
        path = self.builder_harnesses_root / f"{sha256}.json"
        self._write_json(path, dict(payload))
        return path

    def record_builder_trace(
        self,
        *,
        run_id: str,
        builder_harness_sha256: str,
        status: str,
        events: tuple[Any, ...],
        previous_harness_sha256: str,
        candidate_harness_sha256: str | None,
        next_harness_sha256: str,
        reason: str,
        source_sha256: str | None = None,
        changed_components: tuple[str, ...] = (),
    ) -> Path:
        run_id = _safe_id(run_id, "Builder run id")
        if _SHA256.fullmatch(builder_harness_sha256) is None:
            raise ValueError("Builder Harness hash is invalid")
        if _SHA256.fullmatch(next_harness_sha256) is None:
            raise ValueError("next Harness hash is invalid")
        if _SHA256.fullmatch(previous_harness_sha256) is None:
            raise ValueError("previous Harness hash is invalid")
        if candidate_harness_sha256 is not None and (
            _SHA256.fullmatch(candidate_harness_sha256) is None
        ):
            raise ValueError("candidate Harness hash is invalid")
        if source_sha256 is not None and _SHA256.fullmatch(source_sha256) is None:
            raise ValueError("source Harness hash is invalid")
        if not isinstance(changed_components, tuple) or not all(
            isinstance(item, str) and _SAFE_ID.fullmatch(item) for item in changed_components
        ):
            raise ValueError("changed Harness components are invalid")
        payload = {
            "schema_version": 1,
            "run_id": run_id,
            "builder_harness_sha256": builder_harness_sha256,
            "status": status,
            "events": [asdict(event) for event in events],
            "previous_harness_sha256": previous_harness_sha256,
            "candidate_harness_sha256": candidate_harness_sha256,
            "next_harness_sha256": next_harness_sha256,
            "reason": reason,
            "source_sha256": source_sha256,
            "changed_components": list(changed_components),
        }
        return self._store_content_addressed(
            payload=payload,
            objects_root=self.builder_runs_root,
            bindings_root=self.builder_run_bindings_root,
            binding_id=run_id,
            label="Builder trace",
        )

    def load_builder_trace(
        self, run_id: str, *, missing_ok: bool = False
    ) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.builder_runs_root,
            bindings_root=self.builder_run_bindings_root,
            binding_id=run_id,
            label="Builder trace",
            missing_ok=missing_ok,
        )

    def record_round_receipt(self, *, run_id: str, payload: Mapping[str, Any]) -> Path:
        run_id = _safe_id(run_id, "round receipt id")
        return self._store_content_addressed(
            payload=dict(payload),
            objects_root=self.round_receipts_root,
            bindings_root=self.round_receipt_bindings_root,
            binding_id=run_id,
            label="round receipt",
        )

    def record_round_assessment(self, *, run_id: str, payload: Mapping[str, Any]) -> Path:
        """Persist controller-derived per-round evidence separately from the receipt."""

        run_id = _safe_id(run_id, "round assessment id")
        return self._store_content_addressed(
            payload=dict(payload),
            objects_root=self.round_assessments_root,
            bindings_root=self.round_assessment_bindings_root,
            binding_id=run_id,
            label="round assessment",
        )

    def load_round_assessment(
        self, run_id: str, *, missing_ok: bool = False
    ) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.round_assessments_root,
            bindings_root=self.round_assessment_bindings_root,
            binding_id=run_id,
            label="round assessment",
            missing_ok=missing_ok,
        )

    def load_round_receipt(
        self, run_id: str, *, missing_ok: bool = False
    ) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.round_receipts_root,
            bindings_root=self.round_receipt_bindings_root,
            binding_id=run_id,
            label="round receipt",
            missing_ok=missing_ok,
        )

    def record_solver_result(self, *, run_id: str, payload: Mapping[str, Any]) -> Path:
        run_id = _safe_id(run_id, "solver result id")
        return self._store_content_addressed(
            payload=dict(payload),
            objects_root=self.solver_results_root,
            bindings_root=self.solver_result_bindings_root,
            binding_id=run_id,
            label="solver result",
        )

    def load_solver_result(
        self, run_id: str, *, missing_ok: bool = False
    ) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.solver_results_root,
            bindings_root=self.solver_result_bindings_root,
            binding_id=run_id,
            label="solver result",
            missing_ok=missing_ok,
        )

    def claim_operation(
        self,
        *,
        run_id: str,
        stage: str,
        request_sha256: str,
    ) -> Path:
        run_id = _safe_id(run_id, "operation run id")
        stage = _safe_id(stage, "operation stage")
        if _SHA256.fullmatch(request_sha256) is None:
            raise ValueError("operation request hash is invalid")
        return self._store_content_addressed(
            payload={
                "schema_version": 1,
                "run_id": run_id,
                "stage": stage,
                "request_sha256": request_sha256,
            },
            objects_root=self.operation_claims_root,
            bindings_root=self.operation_claim_bindings_root,
            binding_id=f"{run_id}-{stage}",
            label="operation claim",
        )

    def load_operation_claim(
        self,
        *,
        run_id: str,
        stage: str,
        missing_ok: bool = False,
    ) -> dict[str, Any] | None:
        run_id = _safe_id(run_id, "operation run id")
        stage = _safe_id(stage, "operation stage")
        return self._load_content_addressed(
            objects_root=self.operation_claims_root,
            bindings_root=self.operation_claim_bindings_root,
            binding_id=f"{run_id}-{stage}",
            label="operation claim",
            missing_ok=missing_ok,
        )

    def record_operation_result(
        self,
        *,
        run_id: str,
        stage: str,
        request_sha256: str,
        payload: Mapping[str, Any],
    ) -> Path:
        """Bind one durable external result to its prior stage claim.

        This generic result channel is used by portfolio runs, where a single
        round contains multiple Builder, Solver, and evaluator operations.  It
        deliberately does not imply entitlement or retry permission.
        """

        run_id = _safe_id(run_id, "operation result run id")
        stage = _safe_id(stage, "operation result stage")
        if _SHA256.fullmatch(request_sha256) is None:
            raise ValueError("operation result request hash is invalid")
        claim = self.load_operation_claim(run_id=run_id, stage=stage)
        assert claim is not None
        if claim.get("request_sha256") != request_sha256:
            raise ValueError("operation result differs from its claim")
        result = {
            "schema_version": 1,
            "run_id": run_id,
            "stage": stage,
            "request_sha256": request_sha256,
            "payload": dict(payload),
        }
        return self._store_content_addressed(
            payload=result,
            objects_root=self.operation_results_root,
            bindings_root=self.operation_result_bindings_root,
            binding_id=f"{run_id}-{stage}",
            label="operation result",
        )

    def load_operation_result(
        self,
        *,
        run_id: str,
        stage: str,
        missing_ok: bool = False,
    ) -> dict[str, Any] | None:
        run_id = _safe_id(run_id, "operation result run id")
        stage = _safe_id(stage, "operation result stage")
        result = self._load_content_addressed(
            objects_root=self.operation_results_root,
            bindings_root=self.operation_result_bindings_root,
            binding_id=f"{run_id}-{stage}",
            label="operation result",
            missing_ok=missing_ok,
        )
        if result is None:
            return None
        claim = self.load_operation_claim(run_id=run_id, stage=stage)
        assert claim is not None
        if result.get("request_sha256") != claim.get("request_sha256"):
            raise ValueError("operation result claim binding is invalid")
        return result

    def _record_commit_receipt(
        self,
        *,
        run_id: str,
        previous_sha256: str | None,
        candidate_sha256: str,
        update_champion: bool = True,
    ) -> Path:
        if previous_sha256 is None or _SHA256.fullmatch(previous_sha256) is None:
            raise ValueError("owned commit requires a valid parent")
        return self._store_content_addressed(
            payload={
                "schema_version": 1,
                "run_id": run_id,
                "previous_sha256": previous_sha256,
                "candidate_sha256": candidate_sha256,
                "update_champion": update_champion,
            },
            objects_root=self.commit_receipts_root,
            bindings_root=self.commit_receipt_bindings_root,
            binding_id=run_id,
            label="commit receipt",
        )

    def load_commit_receipt(
        self, run_id: str, *, missing_ok: bool = False
    ) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.commit_receipts_root,
            bindings_root=self.commit_receipt_bindings_root,
            binding_id=run_id,
            label="commit receipt",
            missing_ok=missing_ok,
        )

    def abandon_round(self, run_id: str, *, reason: str) -> Path:
        run_id = _safe_id(run_id, "abandoned round id")
        if not isinstance(reason, str) or not reason.strip() or len(reason) > 4_000:
            raise ValueError("abandoned round reason is invalid")
        with self.evolution_lock():
            if self.load_round_receipt(run_id, missing_ok=True) is not None:
                raise ValueError("completed round cannot be abandoned")
            if self.load_commit_receipt(run_id, missing_ok=True) is not None:
                raise ValueError("round with an owned Harness commit must be recovered")
            if self.load_abandoned_round(run_id, missing_ok=True) is not None:
                raise ValueError("round is already abandoned")
            if run_id not in self.pending_run_ids():
                raise ValueError("only a pending round can be abandoned")
            return self._store_content_addressed(
                payload={
                    "schema_version": 1,
                    "run_id": run_id,
                    "reason": reason,
                },
                objects_root=self.abandoned_rounds_root,
                bindings_root=self.abandoned_round_bindings_root,
                binding_id=run_id,
                label="abandoned round",
            )

    def load_abandoned_round(
        self, run_id: str, *, missing_ok: bool = False
    ) -> dict[str, Any] | None:
        return self._load_content_addressed(
            objects_root=self.abandoned_rounds_root,
            bindings_root=self.abandoned_round_bindings_root,
            binding_id=run_id,
            label="abandoned round",
            missing_ok=missing_ok,
        )

    def pending_run_ids(self) -> tuple[str, ...]:
        claimed: set[str] = set()
        for path in sorted(self.operation_claim_bindings_root.glob("*.json")):
            claim = self._load_content_addressed(
                objects_root=self.operation_claims_root,
                bindings_root=self.operation_claim_bindings_root,
                binding_id=path.stem,
                label="operation claim",
                missing_ok=False,
            )
            assert claim is not None
            run_id = claim.get("run_id")
            stage = claim.get("stage")
            if not isinstance(run_id, str) or not isinstance(stage, str):
                raise ValueError("operation claim has an invalid run id")
            # A multi-step Harness may use one operation run id for several
            # stages. Completed claims are not pending rounds; only a claim
            # without its bound durable result blocks recovery.
            if self.load_operation_result(
                run_id=run_id, stage=stage, missing_ok=True
            ) is not None:
                continue
            claimed.add(run_id)
        return tuple(
            run_id
            for run_id in sorted(claimed)
            if self.load_round_receipt(run_id, missing_ok=True) is None
            and self.load_abandoned_round(run_id, missing_ok=True) is None
        )

    @contextmanager
    def round_lock(self, run_id: str) -> Iterator[None]:
        run_id = _safe_id(run_id, "round lock id")
        with self._exclusive_lock(self.locks_root / f"round-{run_id}.lock"):
            yield

    @contextmanager
    def evolution_lock(self) -> Iterator[None]:
        with self._exclusive_lock(self.locks_root / "evolution.lock"):
            yield

    def _store_content_addressed(
        self,
        *,
        payload: Mapping[str, Any],
        objects_root: Path,
        bindings_root: Path,
        binding_id: str,
        label: str,
    ) -> Path:
        encoded = (_canonical_json(payload) + "\n").encode("utf-8")
        if len(encoded) > _MAX_TRACE_BYTES:
            raise ValueError(f"{label} exceeds the storage limit")
        sha256 = hashlib.sha256(encoded.rstrip(b"\n")).hexdigest()
        object_path = objects_root / f"{sha256}.json"
        self._write_json(object_path, dict(payload))
        binding_path = bindings_root / f"{binding_id}.json"
        with self._exclusive_lock(self.locks_root / "binding-sequence.lock"):
            if binding_path.is_file():
                binding = self._read_binding(binding_path, label=label)
                if binding["sha256"] != sha256:
                    raise ValueError("refusing to overwrite different content")
                return object_path
            sequence = self._next_binding_sequence()
            self._write_json(
                binding_path,
                {"sha256": sha256, "sequence": sequence},
            )
        return object_path

    def _next_binding_sequence(self) -> int:
        existing_sequences: list[int] = []
        for root in self._content_binding_roots:
            for path in root.glob("*.json"):
                binding = self._read_binding(path, label="content-addressed")
                sequence = binding.get("sequence")
                if sequence is not None:
                    existing_sequences.append(sequence)
        minimum_next = max(existing_sequences, default=0) + 1
        if self.binding_sequence_path.is_file():
            state = json.loads(self.binding_sequence_path.read_text(encoding="utf-8"))
            next_sequence = state.get("next_sequence") if isinstance(state, dict) else None
            if (
                not isinstance(next_sequence, int)
                or isinstance(next_sequence, bool)
                or next_sequence < minimum_next
            ):
                raise ValueError("workspace binding sequence state is invalid")
        else:
            next_sequence = minimum_next
        self._replace_json(
            self.binding_sequence_path,
            {"next_sequence": next_sequence + 1},
        )
        return next_sequence

    def _binding_paths_in_evidence_order(self, *roots: Path) -> tuple[Path, ...]:
        entries: list[tuple[tuple[Any, ...], Path]] = []
        seen_sequences: set[int] = set()
        for root in roots:
            for path in root.glob("*.json"):
                binding = self._read_binding(path, label="content-addressed")
                sequence = binding.get("sequence")
                if sequence is None:
                    # Legacy bindings predate sequence allocation. Their filesystem
                    # write time is the best available first-seen evidence.
                    key = (0, path.stat().st_mtime_ns, root.name, path.name)
                else:
                    if sequence in seen_sequences:
                        raise ValueError("workspace binding sequence is duplicated")
                    seen_sequences.add(sequence)
                    key = (1, sequence, root.name, path.name)
                entries.append((key, path))
        entries.sort(key=lambda item: item[0])
        return tuple(path for _, path in entries)

    @staticmethod
    def _read_binding(path: Path, *, label: str) -> dict[str, Any]:
        binding = json.loads(path.read_text(encoding="utf-8"))
        sha256 = binding.get("sha256") if isinstance(binding, dict) else None
        if not isinstance(sha256, str) or _SHA256.fullmatch(sha256) is None:
            raise ValueError(f"{label} binding failed integrity verification")
        sequence = binding.get("sequence")
        if sequence is not None and (
            not isinstance(sequence, int)
            or isinstance(sequence, bool)
            or sequence < 1
        ):
            raise ValueError(f"{label} binding sequence is invalid")
        return binding

    def _load_content_addressed(
        self,
        *,
        objects_root: Path,
        bindings_root: Path,
        binding_id: str,
        label: str,
        missing_ok: bool,
    ) -> dict[str, Any] | None:
        binding_id = _safe_id(binding_id, f"{label} id")
        binding_path = bindings_root / f"{binding_id}.json"
        if not binding_path.is_file():
            if missing_ok:
                return None
            raise ValueError(f"{label} does not exist")
        binding = self._read_binding(binding_path, label=label)
        sha256 = binding["sha256"]
        object_path = objects_root / f"{sha256}.json"
        raw = object_path.read_text(encoding="utf-8")
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{label} failed integrity verification") from exc
        actual = hashlib.sha256(_canonical_json(payload).encode("utf-8")).hexdigest()
        if actual != sha256 or not isinstance(payload, dict):
            raise ValueError(f"{label} failed integrity verification")
        return payload

    @staticmethod
    @contextmanager
    def _exclusive_lock(path: Path) -> Iterator[None]:
        path.parent.mkdir(parents=True, exist_ok=True)
        handle = path.open("a+b")
        try:
            if path.stat().st_size == 0:
                handle.write(b"\0")
                handle.flush()
            handle.seek(0)
            if os.name == "nt":
                import msvcrt

                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl

                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            handle.close()
            raise RuntimeError(f"workspace operation is already active: {path.name}") from exc
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                import msvcrt

                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl

                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
            handle.close()

    @staticmethod
    def _write_json(path: Path, payload: Any) -> None:
        encoded = (_canonical_json(payload) + "\n").encode("utf-8")
        if path.exists():
            if path.read_bytes() != encoded:
                raise ValueError("refusing to overwrite different content")
            return
        HarnessWorkspace._atomic_write(path, encoded)

    @staticmethod
    def _replace_json(path: Path, payload: Any) -> None:
        encoded = (_canonical_json(payload) + "\n").encode("utf-8")
        HarnessWorkspace._atomic_write(path, encoded)

    @staticmethod
    def _atomic_write(path: Path, content: bytes) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, name = tempfile.mkstemp(dir=path.parent, suffix=".harness.tmp")
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            Path(name).replace(path)
        except Exception:
            Path(name).unlink(missing_ok=True)
            raise
