from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from optimization_lab.generation import GenerationResult
from optimization_lab.harness_builder.dual_harness import (
    HarnessWorkspace,
    TaskHarnessArtifact,
    TaskHarnessRuntime,
)
from optimization_lab.harness_builder.contract_compatibility import (
    codec_capability_payload,
)
from optimization_lab.harness_builder.official_solutions import ALEBenchCodeCodec
from optimization_lab.harness_builder.tool_registry import BoundTool, ToolRegistry


class SequenceGenerator:
    def __init__(self, *responses: str) -> None:
        self.responses = list(responses)
        self.calls: list[tuple[str, str]] = []

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append((prompt, model))
        return GenerationResult(raw_response=self.responses.pop(0), provider="fixture")


def artifact(*, parent_sha256: str | None = None) -> TaskHarnessArtifact:
    return TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1 if parent_sha256 is None else 2,
            "parent_sha256": parent_sha256,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {"id": "inspect", "kind": "model_call", "role": "analyst", "prompt": "Inspect {task}"},
                    {"id": "verify", "kind": "tool_call", "tool": "verify", "input_key": "latest_output"},
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )


def test_task_harness_executes_model_tool_and_emit_nodes(tmp_path: Path) -> None:
    generator = SequenceGenerator("candidate-v1")
    runtime = TaskHarnessRuntime(generator=generator)
    current = artifact()

    result = runtime.run(
        current,
        task="public task",
        model="fixture-solver",
        tools={"verify": lambda value: {"passed": value == "candidate-v1"}},
    )

    assert result.candidate == "candidate-v1"
    assert [event.node_id for event in result.events] == ["inspect", "verify", "emit"]
    assert result.events[1].output == {"passed": True}
    assert generator.calls[0][1] == "fixture-solver"
    assert "public task" in generator.calls[0][0]


def test_v2_task_harness_solver_can_choose_allowlisted_tools_at_runtime(
    tmp_path: Path,
) -> None:
    generator = SequenceGenerator(
        '{"action":"tool","tool":"inspect","arguments":{"value":"candidate"}}',
        '{"action":"emit","candidate":"final-answer"}',
    )
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": ["inspect"],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 8,
                        "max_tool_calls": 4,
                    },
                },
                "router": {},
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Solve {task}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    observed: list[str] = []

    def inspect(arguments: dict[str, object]) -> dict[str, object]:
        observed.append(str(arguments["value"]))
        return {"ok": True}

    registry = ToolRegistry(
        tmp_path / "registry",
        {"inspect": BoundTool.callable(inspect)},
    )
    result = TaskHarnessRuntime(generator=generator).run(
        current,
        task="public task",
        model="solver",
        tools={},
        tool_registry=registry,
        tool_workspace=tmp_path / "registry" / "workspace",
        operation_scope="round-1",
    )

    assert result.candidate == "final-answer"
    assert observed == ["candidate"]
    assert result.model_call_scopes == ("solve.agent.0000", "solve.agent.0001")
    assert [event.kind for event in result.events] == [
        "model_call",
        "tool_call",
        "model_call",
        "emit",
    ]
    assert [event.index for event in result.events] == [0, 1, 2, 3]
    assert result.events[1].output["receipt"]["operation_id"] == (
        "round-1-solve-tool-0000"
    )
    assert "inspect" in generator.calls[0][0]


def test_v2_static_tool_call_uses_registry_and_writes_receipt(tmp_path: Path) -> None:
    generator = SequenceGenerator("candidate-v1", "candidate-v2")
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {"tools": ["contract_check"], "skills": []},
                "router": {},
                "nodes": [
                    {"id": "draft", "kind": "model_call", "role": "solver", "prompt": "Solve {task}"},
                    {"id": "check", "kind": "tool_call", "tool": "contract_check", "input_key": "draft"},
                    {"id": "final", "kind": "model_call", "role": "solver", "prompt": "Return the final answer after {check}"},
                    {"id": "emit", "kind": "emit", "input_key": "final"},
                ],
            },
        }
    )
    calls: list[dict[str, object]] = []

    def contract_check(arguments: dict[str, object]) -> dict[str, object]:
        calls.append(arguments)
        return {"valid": True}

    registry = ToolRegistry(
        tmp_path / "registry",
        {"contract_check": BoundTool.callable(contract_check)},
    )
    result = TaskHarnessRuntime(generator=generator).run(
        current,
        task="public task",
        model="solver",
        tools={},
        tool_registry=registry,
        tool_workspace=tmp_path / "registry" / "workspace",
        operation_scope="round-1",
    )

    assert result.candidate == "candidate-v2"
    assert calls == [{"candidate": "candidate-v1"}]
    receipt = result.events[1].output["receipt"]
    assert receipt["tool"] == "contract_check"
    assert receipt["status"] == "success"
    assert receipt["operation_id"] == "round-1.check.0000"
    assert (tmp_path / "registry" / ".tool_receipts.jsonl").is_file()


def test_v2_static_tool_call_fails_closed_without_registry(tmp_path: Path) -> None:
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {"tools": ["contract_check"], "skills": []},
                "router": {},
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "Solve {task}"},
                    {"id": "check", "kind": "tool_call", "tool": "contract_check", "input_key": "solve"},
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )

    with pytest.raises(ValueError, match="fixed ToolRegistry"):
        TaskHarnessRuntime(generator=SequenceGenerator("candidate")).run(
            current,
            task="public task",
            model="solver",
            tools={"contract_check": lambda _value: {"valid": True}},
        )


def test_v2_static_evaluator_tool_is_rejected_by_registry(tmp_path: Path) -> None:
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {"tools": ["private_eval"], "skills": []},
                "router": {},
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "Solve {task}"},
                    {"id": "eval", "kind": "tool_call", "tool": "private_eval", "input_key": "solve"},
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    registry = ToolRegistry(tmp_path / "registry", {"private_eval": lambda _args: {"score": 1}})

    with pytest.raises(ValueError, match="evaluator tools are forbidden"):
        TaskHarnessRuntime(generator=SequenceGenerator("candidate")).run(
            current,
            task="public task",
            model="solver",
            tools={},
            tool_registry=registry,
            tool_workspace=tmp_path / "registry" / "workspace",
            operation_scope="round-1",
        )


def test_agent_operation_scope_starts_at_zero_after_a_prior_model_node(
    tmp_path: Path,
) -> None:
    generator = SequenceGenerator(
        "preparation",
        '{"action":"emit","candidate":"final-answer"}',
    )
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": [],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 4,
                        "max_tool_calls": 1,
                        "workflows": [],
                    },
                },
                "router": {},
                "nodes": [
                    {"id": "prepare", "kind": "model_call", "role": "analyst", "prompt": "Prepare {task}"},
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "Solve {task}"},
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    registry = ToolRegistry(tmp_path / "registry", {})
    result = TaskHarnessRuntime(generator=generator).run(
        current,
        task="public task",
        model="solver",
        tools={},
        tool_registry=registry,
        tool_workspace=tmp_path / "registry" / "workspace",
        operation_scope="round-1",
    )

    assert result.model_call_scopes == ("prepare", "solve.agent.0000")
    assert result.events[1].node_id == "solve.agent.0000"


def test_agent_mode_requires_fixed_registry_and_operation_scope(tmp_path: Path) -> None:
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": ["inspect"],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 8,
                        "max_tool_calls": 4,
                    },
                },
                "router": {},
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "{task}"},
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    with pytest.raises(ValueError, match="ToolRegistry"):
        TaskHarnessRuntime(generator=SequenceGenerator("unused")).run(
            current, task="task", model="solver", tools={}
        )


def test_agent_mode_rejects_unknown_agent_node() -> None:
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": [],
                    "skills": [],
                    "agent": {
                        "node_id": "missing",
                        "max_turns": 8,
                        "max_tool_calls": 4,
                    },
                },
                "router": {},
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "{task}"},
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    with pytest.raises(ValueError, match="agent node"):
        TaskHarnessRuntime(generator=SequenceGenerator("unused")).run(
            current, task="task", model="solver", tools={}
        )


def test_v2_task_harness_can_route_into_a_fixed_workflow(tmp_path: Path) -> None:
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": [],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 8,
                        "max_tool_calls": 4,
                        "workflows": ["diagnose_generate_verify"],
                    },
                },
                "router": {},
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "{task}"},
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    generator = SequenceGenerator(
        '{"action":"workflow","workflow":"diagnose_generate_verify"}',
        '{"action":"emit","candidate":"answer"}',
    )
    registry = ToolRegistry(tmp_path / "registry")

    result = TaskHarnessRuntime(generator=generator).run(
        current,
        task="task",
        model="solver",
        tools={},
        tool_registry=registry,
        tool_workspace=tmp_path / "registry" / "workspace",
        operation_scope="round-1",
    )

    assert result.candidate == "answer"
    assert [event.kind for event in result.events] == [
        "model_call",
        "workflow_select",
        "model_call",
        "emit",
    ]
    assert result.events[1].output["id"] == "diagnose_generate_verify"
    assert "diagnose_generate_verify" in generator.calls[0][0]


def test_agent_mode_preserves_task_and_output_contract_after_tool_call(
    tmp_path: Path,
) -> None:
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": ["inspect"],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 8,
                        "max_tool_calls": 4,
                    },
                },
                "router": {},
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Solve UNIQUE_PUBLIC_TASK",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    generator = SequenceGenerator(
        '{"action":"tool","tool":"inspect","arguments":{}}',
        '{"action":"emit","candidate":"answer"}',
    )
    registry = ToolRegistry(
        tmp_path / "registry",
        {"inspect": BoundTool.callable(lambda _: {"ok": True})},
    )
    runtime = TaskHarnessRuntime(
        generator=generator,
        output_contract={"format": "UNIQUE_OUTPUT_CONTRACT"},
    )

    runtime.run(
        current,
        task="public task",
        model="solver",
        tools={},
        tool_registry=registry,
        tool_workspace=tmp_path / "registry" / "workspace",
        operation_scope="round-1",
    )

    assert len(generator.calls) == 2
    assert "UNIQUE_PUBLIC_TASK" in generator.calls[1][0]
    assert "UNIQUE_OUTPUT_CONTRACT" in generator.calls[1][0]


@pytest.mark.parametrize(
    ("workflows", "message"),
    [
        (["missing_workflow"], "not registered"),
        (
            ["diagnose_generate_verify", "diagnose_generate_verify"],
            "must be unique",
        ),
    ],
)
def test_agent_mode_rejects_invalid_harness_workflow_allowlist(
    tmp_path: Path,
    workflows: list[str],
    message: str,
) -> None:
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": [],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 8,
                        "max_tool_calls": 4,
                        "workflows": workflows,
                    },
                },
                "router": {},
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "Solve {task}"},
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )

    with pytest.raises(ValueError, match=message):
        TaskHarnessRuntime(generator=SequenceGenerator("unused")).run(
            current,
            task="task",
            model="solver",
            tools={},
            tool_registry=ToolRegistry(tmp_path / "registry"),
            tool_workspace=tmp_path / "registry" / "workspace",
            operation_scope="round-1",
        )


def test_task_harness_preserves_source_braces_and_replaces_only_known_placeholders() -> None:
    generator = SequenceGenerator("candidate-v1")
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "analyst",
                        "prompt": (
                            "Solve {task}. Preserve JSON {'value': 1} and "
                            "Python f-string f'{P}'."
                        ),
                    },
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )

    TaskHarnessRuntime(generator=generator).run(
        current,
        task="public task",
        model="fixture-solver",
        tools={},
    )

    rendered = generator.calls[0][0]
    assert "Solve public task." in rendered
    assert "{'value': 1}" in rendered
    assert "f'{P}'" in rendered


def test_output_contract_is_bound_only_to_the_model_node_that_feeds_emit() -> None:
    generator = SequenceGenerator("analysis", "```cpp23\nint main() {}\n```")
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "analyze",
                        "kind": "model_call",
                        "role": "analyst",
                        "prompt": "Analyze {task} without producing a final answer.",
                    },
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": (
                            "Turn {analyze} into the final answer. Do not use markdown fences."
                        ),
                    },
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    contract = codec_capability_payload(ALEBenchCodeCodec())

    result = TaskHarnessRuntime(
        generator=generator,
        output_contract=contract,
    ).run(current, task="public ALE task", model="fixture-solver", tools={})

    analysis_prompt, final_prompt = (call[0] for call in generator.calls)
    assert "AUTHORITATIVE OUTPUT CONTRACT" not in analysis_prompt
    assert "AUTHORITATIVE OUTPUT CONTRACT" in final_prompt
    assert contract["skill_sha256"] in final_prompt
    assert "one complete fenced source file and no prose" in final_prompt
    assert "higher priority" in final_prompt
    assert result.output_contract_sha256 == contract["skill_sha256"]


def test_agent_output_contract_targets_emit_candidate_not_action_wrapper() -> None:
    contract = {"artifact_kind": "alebench_source_file", "format": "complete_cpp23"}

    block = TaskHarnessRuntime._output_contract_block(contract, "c" * 64)

    assert (
        "Apply this benchmark contract only to the string inside the final "
        "emit.candidate field" in block
    )
    assert "Apply it only to the entire final response" not in block


def test_task_harness_rejects_unknown_node_and_tool(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="node kind"):
        TaskHarnessArtifact.from_dict(
            {
                "schema_version": 1,
                "version": 1,
                "parent_sha256": None,
                "spec": {"schema_version": 1, "nodes": [{"id": "x", "kind": "python"}]},
            }
        )

    runtime = TaskHarnessRuntime(generator=SequenceGenerator("candidate"))
    bad = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
                "spec": {
                    "schema_version": 1,
                    "nodes": [
                        {"id": "x", "kind": "tool_call", "tool": "run_shell"},
                        {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                    ],
                },
            }
        )
    with pytest.raises(ValueError, match="not allowlisted"):
        runtime.run(bad, task="task", model="model", tools={})


def test_v2_task_harness_runs_roles_skill_memory_and_router() -> None:
    generator = SequenceGenerator("analysis", "strategy", "```python\nanswer\n```")
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {
                    "task_template": "Task: {task}",
                    "constraints": {"budget": 4},
                },
                "memory": {
                    "abstract": ["avoid unstable interpolation"],
                    "raw_refs": ["trace-001"],
                },
                "capabilities": {
                    "skills": [
                        {"id": "diagnose", "prompt": "Identify one failure mode."}
                    ]
                },
                "router": {
                    "directive": "prefer stable extrapolation",
                    "execution_order": ["analysis", "skill", "strategy", "emit"],
                },
                "nodes": [
                    {"id": "analysis", "kind": "model_call", "role": "analyst", "prompt": "{task}"},
                    {"id": "skill", "kind": "skill_call", "skill": "diagnose", "input_key": "analysis"},
                    {"id": "strategy", "kind": "model_call", "role": "designer", "prompt": "{analysis}\n{skill}"},
                    {"id": "emit", "kind": "emit", "input_key": "strategy"},
                ],
            },
        }
    )

    result = TaskHarnessRuntime(generator=generator).run(
        current, task="public task", model="solver", tools={}
    )

    assert result.candidate == "strategy"
    assert [event.node_id for event in result.events] == ["analysis", "skill", "strategy", "emit"]
    assert "avoid unstable interpolation" in generator.calls[0][0]
    assert "prefer stable extrapolation" in generator.calls[0][0]
    assert "Role: analyst" in generator.calls[0][0]
    assert "Role: designer" in generator.calls[1][0]


def test_prompt_rendering_preserves_braces_from_initial_state() -> None:
    generator = SequenceGenerator("```python\nvalue = f'{P}'\n```")
    current = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {"tools": [], "skills": []},
                "router": {},
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Write JSON {\"P\": 1}; keep f'{P}' literal. {task}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
            },
        }
    )
    TaskHarnessRuntime(generator=generator).run(
        current,
        task="task",
        model="solver",
        tools={},
        initial_state={"P": "must-not-render"},
    )
    assert '{"P": 1}' in generator.calls[0][0]
    assert "f'{P}'" in generator.calls[0][0]
    assert "must-not-render" not in generator.calls[0][0]


def test_v2_router_rejects_duplicate_execution_nodes() -> None:
    artifact_payload = {
        "schema_version": 1,
        "version": 1,
        "parent_sha256": None,
        "spec": {
            "schema_version": 2,
            "interface": {},
            "memory": {},
            "capabilities": {"tools": [], "skills": []},
            "router": {"execution_order": ["solve", "emit", "emit"]},
            "nodes": [
                {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "{task}"},
                {"id": "emit", "kind": "emit", "input_key": "solve"},
            ],
        },
    }
    current = TaskHarnessArtifact.from_dict(artifact_payload)
    with pytest.raises(ValueError, match="execution_order"):
        TaskHarnessRuntime(generator=SequenceGenerator("candidate")).run(
            current, task="task", model="solver", tools={}
        )


def test_workspace_versions_are_immutable_and_replayable(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    first = artifact()
    stored = workspace.commit(first)
    assert stored.sha256 == first.sha256
    assert workspace.current().sha256 == first.sha256

    workspace.record_trace(
        run_id="round-1",
        harness_sha256=first.sha256,
        candidate="candidate-v1",
        task_sha256="a" * 64,
        request_sha256="e" * 64,
        solver_model="solver-model",
        events=(),
        score=0.4,
        feedback="format failure",
    )
    inspection = workspace.inspect()
    assert inspection["current_sha256"] == first.sha256
    assert inspection["runs"][0]["feedback"] == "format failure"

    with pytest.raises(ValueError, match="different content"):
        workspace._write_json(workspace.artifact_path(first.sha256), {"changed": True})

    restored = TaskHarnessArtifact.from_dict(
        json.loads(workspace.artifact_path(first.sha256).read_text(encoding="utf-8"))
    )
    assert restored == first


def test_record_trace_binds_workspace_to_one_task_identity(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = workspace.commit(artifact())
    workspace.record_trace(
        run_id="round-a",
        harness_sha256=current.sha256,
        candidate="candidate-a",
        task_sha256="a" * 64,
        request_sha256="1" * 64,
        solver_model="solver-model",
        events=(),
        score=0.1,
        feedback="public feedback",
    )

    with pytest.raises(ValueError, match="task identity"):
        workspace.record_trace(
            run_id="round-b",
            harness_sha256=current.sha256,
            candidate="candidate-b",
            task_sha256="b" * 64,
            request_sha256="2" * 64,
            solver_model="solver-model",
            events=(),
            score=0.2,
            feedback="public feedback",
        )


def test_inspect_reads_uniform_legacy_tasks_but_rejects_mixed_legacy_tasks(
    tmp_path: Path,
) -> None:
    def write_legacy_trace(
        workspace: HarnessWorkspace,
        current: TaskHarnessArtifact,
        *,
        run_id: str,
        task_sha256: str,
    ) -> None:
        workspace._store_content_addressed(
            payload={
                "schema_version": 1,
                "run_id": run_id,
                "harness_sha256": current.sha256,
                "candidate": f"candidate-{run_id}",
                "task_sha256": task_sha256,
                "request_sha256": "e" * 64,
                "solver_model": "solver-model",
                "events": [],
                "score": 0.1,
                "feedback": "public feedback",
            },
            objects_root=workspace.runs_root,
            bindings_root=workspace.run_bindings_root,
            binding_id=run_id,
            label="run trace",
        )

    uniform = HarnessWorkspace(tmp_path / "uniform")
    uniform_current = uniform.commit(artifact())
    write_legacy_trace(
        uniform, uniform_current, run_id="round-1", task_sha256="a" * 64
    )
    write_legacy_trace(
        uniform, uniform_current, run_id="round-2", task_sha256="a" * 64
    )
    assert len(uniform.inspect()["runs"]) == 2

    mixed = HarnessWorkspace(tmp_path / "mixed")
    mixed_current = mixed.commit(artifact())
    write_legacy_trace(
        mixed, mixed_current, run_id="round-1", task_sha256="a" * 64
    )
    write_legacy_trace(
        mixed, mixed_current, run_id="round-2", task_sha256="b" * 64
    )
    with pytest.raises(ValueError, match="task identity"):
        mixed.inspect()


def test_inspect_keeps_branched_and_rejected_harnesses_but_hides_unobserved_artifacts(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    h0 = workspace.commit(artifact())

    def child(parent: TaskHarnessArtifact, prompt: str) -> TaskHarnessArtifact:
        payload = parent.to_dict()
        payload["version"] = parent.version + 1
        payload["parent_sha256"] = parent.sha256
        payload["spec"]["nodes"][0]["prompt"] = prompt
        return TaskHarnessArtifact.from_dict(payload)

    h1 = workspace.commit(child(h0, "H1 inspect {task}"), owner_run_id="build-h1")
    h2 = workspace.commit(child(h1, "H2 inspect {task}"), owner_run_id="build-h2")
    h3 = workspace.commit(
        child(h0, "H3 branch inspect {task}"),
        owner_run_id="build-h3",
        allow_branch=True,
    )
    h4 = workspace.store_artifact(child(h3, "H4 rejected inspect {task}"))
    hidden = workspace.store_artifact(child(h3, "hidden inspect {task}"))

    for index, harness in enumerate((h0, h1, h2, h3), start=0):
        workspace.record_trace(
            run_id=f"solve-h{index}",
            harness_sha256=harness.sha256,
            candidate=f"private-candidate-{index}",
            task_sha256="a" * 64,
            request_sha256=f"{index + 1:x}" * 64,
            solver_model="solver-model",
            events=(),
            score=index / 10,
            feedback=f"public-feedback-{index}",
        )

    workspace.record_builder_trace(
        run_id="build-h4",
        builder_harness_sha256="b" * 64,
        status="rolled_back",
        events=(),
        previous_harness_sha256=h3.sha256,
        candidate_harness_sha256=h4.sha256,
        next_harness_sha256=h3.sha256,
        reason="public probe failed",
        source_sha256=h3.sha256,
        changed_components=("router",),
    )

    inspection = workspace.inspect()
    available = {item["sha256"]: item for item in inspection["available_harnesses"]}

    assert set(available) == {h0.sha256, h1.sha256, h2.sha256, h3.sha256, h4.sha256}
    assert hidden.sha256 not in available
    assert available[h2.sha256]["runs"] == [
        {
            "run_id": "solve-h2",
            "score": 0.2,
            "feedback": "public-feedback-2",
            "status": "scored",
            "events": [],
        }
    ]
    assert available[h3.sha256]["is_current"] is True
    assert available[h3.sha256]["runs"][0]["run_id"] == "solve-h3"
    assert available[h4.sha256]["decisions"][0]["status"] == "rolled_back"
    assert available[h4.sha256]["decisions"][0]["reason"] == "public probe failed"
    assert available[h3.sha256]["adoption"] == {
        "used": True,
        "run_ids": ["solve-h3"],
    }
    assert available[h4.sha256]["adoption"] == {"used": False, "run_ids": []}


def test_inspect_uses_hidden_ancestors_only_for_lineage_validation(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    h0 = workspace.commit(artifact())

    def child(parent: TaskHarnessArtifact, prompt: str) -> TaskHarnessArtifact:
        payload = parent.to_dict()
        payload["version"] = parent.version + 1
        payload["parent_sha256"] = parent.sha256
        payload["spec"]["nodes"][0]["prompt"] = prompt
        return TaskHarnessArtifact.from_dict(payload)

    hidden_ancestor = workspace.store_artifact(
        child(h0, "internal-only ancestor {task}")
    )
    executed = workspace.store_artifact(
        child(hidden_ancestor, "directly evidenced execution {task}")
    )
    workspace.record_trace(
        run_id="executed-branch",
        harness_sha256=executed.sha256,
        candidate="candidate",
        task_sha256="a" * 64,
        request_sha256="e" * 64,
        solver_model="solver-model",
        events=(),
        score=0.3,
        feedback="public feedback",
    )

    inspection = workspace.inspect()
    available = {
        item["sha256"] for item in inspection["available_harnesses"]
    }

    assert available == {h0.sha256, executed.sha256}
    assert hidden_ancestor.sha256 not in available
    assert hidden_ancestor.sha256 not in json.dumps(inspection, sort_keys=True)
    executed_view = next(
        item
        for item in inspection["available_harnesses"]
        if item["sha256"] == executed.sha256
    )
    assert executed_view["parent_sha256"] is None
    assert inspection["current_artifact"]["parent_sha256"] is None


def test_inspect_preserves_append_only_first_seen_order(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    h0 = workspace.commit(artifact())

    def sibling(prompt: str) -> TaskHarnessArtifact:
        payload = h0.to_dict()
        payload["version"] = h0.version + 1
        payload["parent_sha256"] = h0.sha256
        payload["spec"]["nodes"][0]["prompt"] = prompt
        return workspace.store_artifact(TaskHarnessArtifact.from_dict(payload))

    high_hash, low_hash = sorted(
        (
            sibling("first evidenced sibling {task}"),
            sibling("second evidenced sibling {task}"),
        ),
        key=lambda item: item.sha256,
        reverse=True,
    )
    for run_id, request_sha256 in (("z-run", "e" * 64), ("a-run", "d" * 64)):
        workspace.record_trace(
            run_id=run_id,
            harness_sha256=high_hash.sha256,
            candidate=f"candidate-{run_id}",
            task_sha256="a" * 64,
            request_sha256=request_sha256,
            solver_model="solver-model",
            events=(),
            score=0.2,
            feedback=f"feedback-{run_id}",
        )
    for run_id in ("z-build", "a-build"):
        workspace.record_builder_trace(
            run_id=run_id,
            builder_harness_sha256="b" * 64,
            status="rolled_back",
            events=(),
            previous_harness_sha256=h0.sha256,
            candidate_harness_sha256=low_hash.sha256,
            next_harness_sha256=h0.sha256,
            reason=f"reason-{run_id}",
            source_sha256=h0.sha256,
            changed_components=("router",),
        )

    first_binding_path = workspace.run_bindings_root / "z-run.json"
    first_binding = json.loads(first_binding_path.read_text(encoding="utf-8"))
    workspace.record_trace(
        run_id="z-run",
        harness_sha256=high_hash.sha256,
        candidate="candidate-z-run",
        task_sha256="a" * 64,
        request_sha256="e" * 64,
        solver_model="solver-model",
        events=(),
        score=0.2,
        feedback="feedback-z-run",
    )
    assert json.loads(first_binding_path.read_text(encoding="utf-8")) == first_binding
    assert isinstance(first_binding["sequence"], int)

    inspection = workspace.inspect()
    assert [run["run_id"] for run in inspection["runs"]] == ["z-run", "a-run"]
    assert [
        item["sha256"] for item in inspection["available_harnesses"]
    ] == [h0.sha256, high_hash.sha256, low_hash.sha256]
    available = {
        item["sha256"]: item for item in inspection["available_harnesses"]
    }
    assert [run["run_id"] for run in available[high_hash.sha256]["runs"]] == [
        "z-run",
        "a-run",
    ]
    assert [
        decision["run_id"] for decision in available[low_hash.sha256]["decisions"]
    ] == ["z-build", "a-build"]


def test_inspect_reads_legacy_bindings_in_timestamp_order(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = workspace.commit(artifact())
    for run_id, request_sha256 in (("z-run", "e" * 64), ("a-run", "d" * 64)):
        workspace.record_trace(
            run_id=run_id,
            harness_sha256=current.sha256,
            candidate=f"candidate-{run_id}",
            task_sha256="a" * 64,
            request_sha256=request_sha256,
            solver_model="solver-model",
            events=(),
            score=0.2,
            feedback=f"feedback-{run_id}",
        )
    for index, run_id in enumerate(("z-run", "a-run"), start=1):
        path = workspace.run_bindings_root / f"{run_id}.json"
        binding = json.loads(path.read_text(encoding="utf-8"))
        path.write_text(
            json.dumps({"sha256": binding["sha256"]}, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        timestamp_ns = 1_700_000_000_000_000_000 + index * 1_000_000
        os.utime(path, ns=(timestamp_ns, timestamp_ns))

    inspection = workspace.inspect()

    assert [run["run_id"] for run in inspection["runs"]] == ["z-run", "a-run"]
    assert [
        run["run_id"] for run in inspection["available_harnesses"][0]["runs"]
    ] == ["z-run", "a-run"]


def test_commit_revalidates_directly_constructed_artifact(tmp_path: Path) -> None:
    from optimization_lab.harness_builder.dual_harness import TaskHarnessSpec

    workspace = HarnessWorkspace(tmp_path / "workspace")
    invalid = TaskHarnessArtifact(
        schema_version=99,
        version=1,
        parent_sha256=None,
        spec=TaskHarnessSpec(schema_version=1, nodes=()),
    )

    with pytest.raises(ValueError, match="schema"):
        workspace.commit(invalid)
    assert not workspace.current_path.exists()


def test_inspect_rejects_tampered_public_trace(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = workspace.commit(artifact())
    workspace.record_trace(
        run_id="round-tamper",
        harness_sha256=current.sha256,
        candidate="candidate-v1",
        task_sha256="b" * 64,
        request_sha256="e" * 64,
        solver_model="solver-model",
        events=(),
        score=0.4,
        feedback="public feedback",
    )
    binding = json.loads(
        (workspace.run_bindings_root / "round-tamper.json").read_text(encoding="utf-8")
    )
    trace_path = workspace.runs_root / f"{binding['sha256']}.json"
    trace_path.write_text(trace_path.read_text(encoding="utf-8").replace("0.4", "0.9"), encoding="utf-8")

    with pytest.raises(ValueError, match="integrity"):
        workspace.inspect()


def test_process_exit_releases_workspace_lock(tmp_path: Path) -> None:
    root = tmp_path / "workspace"
    script = (
        "import os, pathlib; "
        "from optimization_lab.harness_builder.dual_harness import HarnessWorkspace; "
        f"w=HarnessWorkspace(pathlib.Path({str(root)!r})); "
        "lock=w.evolution_lock(); lock.__enter__(); os._exit(0)"
    )
    subprocess.run([sys.executable, "-c", script], check=True)

    workspace = HarnessWorkspace(root)
    with workspace.evolution_lock():
        pass


def test_uncommitted_interrupted_round_can_be_explicitly_abandoned(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    workspace.claim_operation(
        run_id="round-abandon",
        stage="solver",
        request_sha256="e" * 64,
    )

    workspace.abandon_round("round-abandon", reason="provider result could not be audited")

    assert workspace.pending_run_ids() == ()
    abandoned = workspace.load_abandoned_round("round-abandon")
    assert abandoned["reason"] == "provider result could not be audited"


def test_generic_operation_result_is_content_addressed_and_claim_bound(
    tmp_path: Path,
) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.claim_operation(
        run_id="portfolio-001",
        stage="builder-001",
        request_sha256="a" * 64,
    )

    workspace.record_operation_result(
        run_id="portfolio-001",
        stage="builder-001",
        request_sha256="a" * 64,
        payload={"raw_response": "candidate", "usage": {"output_tokens": 7}},
    )

    result = workspace.load_operation_result(
        run_id="portfolio-001",
        stage="builder-001",
    )
    assert result["payload"]["raw_response"] == "candidate"
    assert workspace.pending_run_ids() == ()
    with pytest.raises(ValueError, match="differs from its claim"):
        workspace.record_operation_result(
            run_id="portfolio-001",
            stage="builder-001",
            request_sha256="b" * 64,
            payload={"raw_response": "changed"},
        )
