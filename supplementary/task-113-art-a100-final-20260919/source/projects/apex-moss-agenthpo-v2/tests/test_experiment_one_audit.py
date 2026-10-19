from __future__ import annotations

import copy
import errno
import hashlib
import importlib
import json
import multiprocessing
import os
import re
import stat
import subprocess
import traceback
from datetime import datetime
from pathlib import Path
from queue import Empty
from threading import BrokenBarrierError
from types import SimpleNamespace
from typing import Any

import pytest

from optimization_lab.generation import GenerationResult
from optimization_lab.harness_builder.builder_harness import BuilderHarness
from optimization_lab.harness_builder.dual_harness import (
    HarnessTraceEvent,
    HarnessWorkspace,
)
from optimization_lab.harness_builder.builder_memory import (
    BuilderMemoryConfig,
    CrossTaskMemoryRecord,
)
from optimization_lab.openai_generator import (
    OpenAIResponsesGenerator,
    OpenAIResponsesRequestConfig,
)
from test_builder_harness import SequenceGenerator, proposal
from test_dual_harness import artifact


def _audit_api() -> tuple[object, object]:
    from optimization_lab.harness_builder.experiment_one_audit import (
        AuditedGenerator,
        experiment_one_builder_view,
    )

    return AuditedGenerator, experiment_one_builder_view


def test_scoped_operation_id_factory_assigns_distinct_deterministic_ids() -> None:
    from optimization_lab.harness_builder.experiment_one_audit import (
        ScopedOperationIdFactory,
    )

    ids = ScopedOperationIdFactory("S1-B-round-02", "solver")

    assert ids.next("solve") == "S1-B-round-02-solver-solve-0000"
    assert ids.next("repair") == "S1-B-round-02-solver-repair-0001"


def test_scoped_operation_id_factory_bounds_and_hashes_long_valid_ids() -> None:
    from optimization_lab.harness_builder.experiment_one_audit import (
        ScopedOperationIdFactory,
    )

    round_id = "r" * 128
    first_scope = "s" * 128
    second_scope = "s" * 127 + "t"

    first = ScopedOperationIdFactory(round_id, "solver").next(first_scope)
    replay = ScopedOperationIdFactory(round_id, "solver").next(first_scope)
    distinct = ScopedOperationIdFactory(round_id, "solver").next(second_scope)

    assert first == replay
    assert first != distinct
    assert len(first) <= 256
    assert len(distinct) <= 256
    assert re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/+-]{0,255}", first)
    assert re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/+-]{0,255}", distinct)


class RecordingGenerator:
    def __init__(self, *responses: str, reasoning_effort: str = "high") -> None:
        self.responses = list(responses)
        self.calls: list[tuple[str, str]] = []
        self.reasoning_effort = reasoning_effort

    def estimated_api_cost_usd(self) -> float:
        return 1.25

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append((prompt, model))
        return GenerationResult(
            raw_response=self.responses.pop(0),
            api_cost_usd=0.75,
            provider="fixture-provider",
            usage={"input_tokens": 11, "output_tokens": 7, "total_tokens": 18},
            audit_log_path="https://secret.example/v1?key=PRIVATE_KEY",
        )


def test_audited_generator_factory_assigns_unique_ids_to_repeated_builder_calls(
    tmp_path: Path,
) -> None:
    from optimization_lab.harness_builder.experiment_one_audit import (
        AuditedGenerator,
        ScopedOperationIdFactory,
    )

    audited = AuditedGenerator(
        generator=RecordingGenerator("first", "second"),
        audit_path=tmp_path / "builder_model_calls.jsonl",
        operation_id_factory=ScopedOperationIdFactory("S1-B-round-02", "builder"),
        layer="builder",
        reasoning_effort="high",
    )

    audited.generate("first prompt", model="gpt-5")
    audited.generate("second prompt", model="gpt-5")

    events = [
        json.loads(line)
        for line in audited.audit_path.read_text(encoding="utf-8").splitlines()
    ]
    assert [event["operation_id"] for event in events if event["event"] == "start"] == [
        "S1-B-round-02-builder-call-0000",
        "S1-B-round-02-builder-call-0001",
    ]


def test_audited_generator_preserves_legacy_callable_with_next_attribute(
    tmp_path: Path,
) -> None:
    from optimization_lab.harness_builder.experiment_one_audit import AuditedGenerator

    class LegacyCallableFactory:
        def __init__(self) -> None:
            self.call_count = 0
            self.next_count = 0

        def __call__(self) -> str:
            self.call_count += 1
            return "legacy-callable-v001"

        def next(self) -> str:
            self.next_count += 1
            return "unrelated-next-v001"

    operation_ids = LegacyCallableFactory()
    audited = AuditedGenerator(
        generator=RecordingGenerator("response"),
        audit_path=tmp_path / "solver_model_calls.jsonl",
        operation_id_factory=operation_ids,
        layer="solver",
        reasoning_effort="high",
    )

    audited.generate("prompt", model="gpt-5")

    start = json.loads(audited.audit_path.read_text(encoding="utf-8").splitlines()[0])
    assert start["operation_id"] == "legacy-callable-v001"
    assert operation_ids.call_count == 1
    assert operation_ids.next_count == 0


class MultiprocessRecordingGenerator:
    def __init__(self, calls_path: Path, delegate_barrier: Any) -> None:
        self.calls_path = calls_path
        self.delegate_barrier = delegate_barrier
        self.reasoning_effort = "high"

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        (self.calls_path / f"{os.getpid()}.call").write_text(
            "called\n", encoding="utf-8"
        )
        try:
            self.delegate_barrier.wait(timeout=1.0)
        except BrokenBarrierError:
            pass
        return GenerationResult(
            raw_response="multiprocess response",
            api_cost_usd=0.0,
            provider="fixture-provider",
            usage={"input_tokens": 1, "output_tokens": 1, "total_tokens": 2},
            audit_log_path="",
        )


class BurstMultiprocessRecordingGenerator:
    def __init__(self, calls_path: Path, first_call_barrier: Any) -> None:
        self.calls_path = calls_path
        self.first_call_barrier = first_call_barrier
        self.call_index = 0
        self.reasoning_effort = "high"

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        call_index = self.call_index
        self.call_index += 1
        if call_index == 0:
            try:
                self.first_call_barrier.wait(timeout=10.0)
            except BrokenBarrierError:
                pass
        (self.calls_path / f"{os.getpid()}-{call_index:03d}.call").write_text(
            "called\n", encoding="utf-8"
        )
        return GenerationResult(
            raw_response=f"multiprocess response {os.getpid()} {call_index}",
            api_cost_usd=0.0,
            provider="fixture-provider",
            usage={f"metric_{index:03d}": index for index in range(256)},
            audit_log_path="",
        )


class CrashingGenerator:
    def __init__(self, call_marker: Path) -> None:
        self.call_marker = call_marker
        self.reasoning_effort = "high"

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.call_marker.write_text("called\n", encoding="utf-8")
        os._exit(23)


class FailingGenerator:
    reasoning_effort = "high"

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        raise RuntimeError("PRIVATE FAILURE MESSAGE")


class LedgerReplacementGenerator:
    reasoning_effort = "high"

    def __init__(self, audit_path: Path, moved_path: Path) -> None:
        self.audit_path = audit_path
        self.moved_path = moved_path
        self.replacement_error: OSError | None = None

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        try:
            os.replace(self.audit_path, self.moved_path)
        except OSError as exc:
            self.replacement_error = exc
        return GenerationResult(
            raw_response="replacement attack response",
            provider="fixture-provider",
            usage={},
        )


class ReboundLowTransport:
    reasoning_effort = "low"

    def __init__(self) -> None:
        self.calls: list[tuple[str, str, OpenAIResponsesRequestConfig]] = []

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate_with_request_config(
        self,
        prompt: str,
        *,
        model: str,
        request_config: OpenAIResponsesRequestConfig,
    ) -> GenerationResult:
        self.calls.append((prompt, model, request_config))
        return GenerationResult(
            raw_response="low transport response",
            provider="spoofed-low-transport",
            usage={},
        )


class HardLinkingGenerator:
    reasoning_effort = "high"

    def __init__(self, source_path: Path, link_path: Path) -> None:
        self.source_path = source_path
        self.link_path = link_path
        self.calls: list[tuple[str, str]] = []

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append((prompt, model))
        os.link(self.source_path, self.link_path)
        return GenerationResult(
            raw_response="hard-link attack response",
            provider="fixture-provider",
            usage={},
        )


class OpenAIResponse:
    usage = None

    def __init__(self, output_text: str) -> None:
        self.output_text = output_text


class OpenAIResponses:
    def __init__(self, *output_texts: str) -> None:
        self.output_texts = list(output_texts)
        self.calls: list[dict[str, object]] = []

    def create(self, **kwargs: object) -> OpenAIResponse:
        self.calls.append(kwargs)
        return OpenAIResponse(self.output_texts.pop(0))


class OpenAIClient:
    def __init__(self, *output_texts: str) -> None:
        self.responses = OpenAIResponses(*output_texts)


def openai_generator(
    *responses: str, effort: str = "high"
) -> OpenAIResponsesGenerator:
    return OpenAIResponsesGenerator(
        client=OpenAIClient(*responses),
        reasoning_effort=effort,
    )


def _run_competing_audited_generator(
    audit_path: Path,
    calls_path: Path,
    start_barrier: Any,
    delegate_barrier: Any,
    outcomes: Any,
) -> None:
    AuditedGenerator, _ = _audit_api()
    audited = AuditedGenerator(
        generator=MultiprocessRecordingGenerator(calls_path, delegate_barrier),
        audit_path=audit_path,
        operation_id_factory=lambda: "shared-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )
    try:
        start_barrier.wait(timeout=10.0)
        audited.generate("shared prompt", model="gpt-5")
    except ValueError as exc:
        outcomes.put(("rejected", str(exc)))
    except BaseException as exc:
        outcomes.put(("unexpected", repr(exc)))
    else:
        outcomes.put(("completed", ""))


def _run_distinct_audited_generator_burst(
    audit_path: Path,
    calls_path: Path,
    start_barrier: Any,
    first_call_barrier: Any,
    outcomes: Any,
    process_index: int,
    call_count: int,
) -> None:
    AuditedGenerator, _ = _audit_api()
    operation_ids = iter(
        f"parallel-{process_index:02d}-{call_index:03d}"
        for call_index in range(call_count)
    )
    audited = AuditedGenerator(
        generator=BurstMultiprocessRecordingGenerator(
            calls_path, first_call_barrier
        ),
        audit_path=audit_path,
        operation_id_factory=lambda: next(operation_ids),
        layer="solver",
        reasoning_effort="high",
    )
    completed = 0
    try:
        start_barrier.wait(timeout=10.0)
        for call_index in range(call_count):
            audited.generate(
                f"parallel prompt {process_index} {call_index}", model="gpt-5"
            )
            completed += 1
    except BaseException as exc:
        outcomes.put(("failed", completed, traceback.format_exc()))
    else:
        outcomes.put(("completed", completed, ""))


def _run_crashing_audited_generator(audit_path: Path, call_marker: Path) -> None:
    AuditedGenerator, _ = _audit_api()
    audited = AuditedGenerator(
        generator=CrashingGenerator(call_marker),
        audit_path=audit_path,
        operation_id_factory=lambda: "crashed-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )
    audited.generate("crashing prompt", model="gpt-5")


def _private_inspection() -> dict[str, object]:
    return {
        "current_sha256": "a" * 64,
        "current_artifact": {
            "schema_version": 1,
            "version": 2,
            "parent_sha256": "b" * 64,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Solve {task}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        },
        "runs": [
            {
                "schema_version": 1,
                "run_id": "round-1",
                "harness_sha256": "c" * 64,
                "candidate": "RAW_CANDIDATE=\u79c1\u5bc6\u7b54\u6848",
                "task_sha256": "d" * 64,
                "request_sha256": "e" * 64,
                "solver_model": "private-model-routing-detail",
                "score": 0.625,
                "feedback": "public compile failure",
                "private": {"gold": "PRIVATE_GOLD"},
                "events": [
                    {
                        "index": 0,
                        "node_id": "solve",
                        "kind": "model_call",
                        "input": "RAW_TASK_AND_PROMPT",
                        "output": "RAW_MODEL_OUTPUT",
                        "private": "PRIVATE_EVENT",
                    }
                ],
            }
        ],
        "available_harnesses": [
            {
                "sha256": "a" * 64,
                "schema_version": 1,
                "version": 2,
                "parent_sha256": "b" * 64,
                "spec": {
                    "schema_version": 2,
                    "interface": {"output_contract": "public-contract"},
                    "memory": {"views": ["current", "best"]},
                    "capabilities": {"tools": ["public-tool"], "skills": []},
                    "router": {"execution_order": ["solve", "emit"]},
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
                "is_current": True,
                "runs": [
                    {
                        "run_id": "round-1",
                        "score": 0.625,
                        "feedback": "public compile failure",
                        "status": "scored",
                        "events": [
                            {
                                "index": 0,
                                "node_id": "solve",
                                "kind": "model_call",
                                "input": "PRIVATE_AVAILABLE_EVENT_INPUT",
                            }
                        ],
                        "candidate": "PRIVATE_HARNESS_CANDIDATE",
                    }
                ],
                "decisions": [
                    {
                        "run_id": "builder-1",
                        "status": "committed",
                        "reason": "public reason",
                        "previous_harness_sha256": "b" * 64,
                        "next_harness_sha256": "a" * 64,
                        "source_sha256": "b" * 64,
                        "base_sha256": "b" * 64,
                        "candidate_harness_sha256": "a" * 64,
                        "changed_components": ["router"],
                        "raw_builder_output": "PRIVATE_BUILDER_OUTPUT",
                    }
                ],
                "adoption": {
                    "used": True,
                    "run_ids": ["round-1"],
                    "private": "PRIVATE_ADOPTION_FIELD",
                },
                "private": "PRIVATE_HARNESS_FIELD",
            }
        ],
        "private": "PRIVATE_TOP_LEVEL",
        "task": "RAW_TASK",
    }


def test_experiment_one_builder_view_is_exact_public_projection_and_immutable() -> None:
    _, experiment_one_builder_view = _audit_api()
    inspection = _private_inspection()
    original = copy.deepcopy(inspection)

    view = experiment_one_builder_view(inspection)

    candidate = inspection["runs"][0]["candidate"]  # type: ignore[index]
    assert view == {
        "current_sha256": "a" * 64,
        "current_artifact": inspection["current_artifact"],
        "runs": [
            {
                "run_id": "round-1",
                "harness_sha256": "c" * 64,
                "candidate": {
                    "sha256": hashlib.sha256(candidate.encode("utf-8")).hexdigest(),
                    "length": len(candidate),
                },
                "score": 0.625,
                "feedback": "public compile failure",
                "events": [{"index": 0, "node_id": "solve", "kind": "model_call"}],
            }
        ],
        "available_harnesses": [
            {
                "sha256": "a" * 64,
                "schema_version": 1,
                "version": 2,
                "parent_sha256": "b" * 64,
                "spec": inspection["available_harnesses"][0]["spec"],  # type: ignore[index]
                "is_current": True,
                "runs": [
                    {
                        "run_id": "round-1",
                        "score": 0.625,
                            "feedback": "public compile failure",
                            "status": "scored",
                            "events": [
                                {"index": 0, "node_id": "solve", "kind": "model_call"}
                            ],
                    }
                ],
                "decisions": [
                    {
                        "run_id": "builder-1",
                        "status": "committed",
                        "reason": "public reason",
                        "previous_harness_sha256": "b" * 64,
                        "next_harness_sha256": "a" * 64,
                        "source_sha256": "b" * 64,
                        "base_sha256": "b" * 64,
                        "candidate_harness_sha256": "a" * 64,
                        "changed_components": ["router"],
                    }
                ],
                "adoption": {"used": True, "run_ids": ["round-1"]},
            }
        ],
        "builder_memory": {
            "mode": "instance_only",
            "cross_task_records": [],
            "snapshot_sha256": None,
        },
    }
    assert inspection == original
    assert view["current_artifact"] is not inspection["current_artifact"]
    encoded = json.dumps(view, allow_nan=False, sort_keys=True)
    for secret in (
        "RAW_CANDIDATE",
        "RAW_TASK_AND_PROMPT",
        "RAW_MODEL_OUTPUT",
        "PRIVATE_GOLD",
        "PRIVATE_EVENT",
        "PRIVATE_TOP_LEVEL",
        "PRIVATE_HARNESS_CANDIDATE",
        "PRIVATE_BUILDER_OUTPUT",
        "PRIVATE_HARNESS_FIELD",
        "PRIVATE_AVAILABLE_EVENT_INPUT",
        "PRIVATE_ADOPTION_FIELD",
    ):
        assert secret not in encoded


def test_experiment_one_builder_view_preserves_every_public_run() -> None:
    _, experiment_one_builder_view = _audit_api()
    inspection = _private_inspection()
    second = copy.deepcopy(inspection["runs"][0])  # type: ignore[index]
    second["run_id"] = "round-2"
    second["candidate"] = "SECOND_PRIVATE_CANDIDATE"
    inspection["runs"].append(second)  # type: ignore[union-attr]

    view = experiment_one_builder_view(inspection)

    assert [run["run_id"] for run in view["runs"]] == ["round-1", "round-2"]


def test_builder_default_inspection_is_backward_compatible(tmp_path: Path) -> None:
    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = workspace.commit(artifact())
    generator = SequenceGenerator(proposal(current.sha256))
    builder = BuilderHarness(
        workspace=workspace, generator=generator, model="builder-model"
    )

    assert builder.inspect() == workspace.inspect()


def test_builder_validates_transform_and_uses_it_in_proposal_prompt(
    tmp_path: Path,
) -> None:
    _, experiment_one_builder_view = _audit_api()
    workspace = HarnessWorkspace(tmp_path / "workspace")
    historical = workspace.commit(artifact())
    current = workspace.commit(artifact(parent_sha256=historical.sha256))
    workspace.record_trace(
        run_id="round-public",
        harness_sha256=current.sha256,
        candidate="RAW_CANDIDATE_MUST_NOT_REACH_BUILDER",
        task_sha256="d" * 64,
        request_sha256="e" * 64,
        solver_model="solver-model",
        events=(),
        score=0.4,
        feedback="PUBLIC_FEEDBACK_MARKER",
    )
    generator = SequenceGenerator(proposal(current.sha256))
    builder = BuilderHarness(
        workspace=workspace,
        generator=generator,
        model="builder-model",
        inspection_transform=experiment_one_builder_view,
    )

    builder.propose(score=0.4, feedback="latest public feedback")

    prompt = generator.calls[0][0]
    assert "PUBLIC_FEEDBACK_MARKER" in prompt
    assert current.sha256 in prompt
    assert "Choose one exact source_sha256 from this allowed list" in prompt
    assert json.dumps(
        [historical.sha256, current.sha256],
        ensure_ascii=False,
        separators=(",", ":"),
    ) in prompt
    assert "Copy the chosen exact hash into both source_sha256 and base_sha256" in prompt
    assert "Use only that selected available_harnesses item's spec as the mutation basis" in prompt
    assert "Start from current_artifact.spec" not in prompt
    assert "Do not use output_key" in prompt
    assert (
        "A node may contain only id, kind, role, prompt, tool, skill, and input_key"
        in prompt
    )
    assert "RAW_CANDIDATE_MUST_NOT_REACH_BUILDER" not in prompt
    assert hashlib.sha256(b"RAW_CANDIDATE_MUST_NOT_REACH_BUILDER").hexdigest() in prompt

    invalid = BuilderHarness(
        workspace=workspace,
        generator=generator,
        model="builder-model",
        inspection_transform=lambda _: [],  # type: ignore[arg-type,return-value]
    )
    with pytest.raises(TypeError, match="Mapping"):
        invalid.inspect()


def test_experiment_one_assembly_mandates_redacted_audited_wiring(
    tmp_path: Path,
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    assemble_experiment_one = getattr(audit_module, "assemble_experiment_one", None)
    assert callable(
        assemble_experiment_one
    ), "experiment one must expose a mandatory safe assembly entry"
    AuditedGenerator = audit_module.AuditedGenerator
    experiment_one_builder_view = audit_module.experiment_one_builder_view

    workspace = HarnessWorkspace(tmp_path / "workspace")
    current = workspace.commit(artifact())
    raw_candidate = "RAW_CANDIDATE_MUST_NOT_REACH_BUILDER"
    raw_event_input = "RAW_MODEL_EVENT_PROMPT_MUST_NOT_REACH_BUILDER"
    raw_event_output = "RAW_MODEL_EVENT_PAYLOAD_MUST_NOT_REACH_BUILDER"
    workspace.record_trace(
        run_id="round-public",
        harness_sha256=current.sha256,
        candidate=raw_candidate,
        task_sha256="d" * 64,
        request_sha256="e" * 64,
        solver_model="private-solver-routing",
        events=(
            HarnessTraceEvent(
                index=0,
                node_id="solve",
                kind="model_call",
                input=raw_event_input,
                output=raw_event_output,
            ),
        ),
        score=0.4,
        feedback="PUBLIC_FEEDBACK_MARKER",
    )
    builder_response = proposal(current.sha256)
    builder_delegate = openai_generator(builder_response)
    solver_response = "SOLVER_RESPONSE_MARKER"
    solver_delegate = openai_generator(solver_response)
    audit_directory = tmp_path / "audit"

    assembly = assemble_experiment_one(
        workspace=workspace,
        builder_generator=builder_delegate,
        solver_generator=solver_delegate,
        builder_model="builder-model",
        audit_directory=audit_directory,
        builder_operation_id_factory=lambda: "experiment-one.builder.v001",
        solver_operation_id_factory=lambda: "experiment-one.solver.v001",
        builder_reasoning_effort="high",
        solver_reasoning_effort="high",
    )

    assembly.builder.propose(score=0.4, feedback="latest public feedback")
    assembly.solver_generator.generate("solver prompt", model="solver-model")

    assert set(vars(assembly)) == {"builder", "solver_generator"}
    assert isinstance(assembly.builder.generator, AuditedGenerator)
    assert assembly.builder.inspection_transform is experiment_one_builder_view
    assert isinstance(assembly.solver_generator, AuditedGenerator)
    builder_call = builder_delegate.client.responses.calls[0]
    builder_prompt = builder_call["input"]
    builder_model = builder_call["model"]
    assert isinstance(builder_prompt, str)
    assert builder_model == "builder-model"
    assert "PUBLIC_FEEDBACK_MARKER" in builder_prompt
    assert current.sha256 in builder_prompt
    assert '"node_id": "solve"' in builder_prompt
    assert hashlib.sha256(raw_candidate.encode("utf-8")).hexdigest() in builder_prompt
    for private_marker in (raw_candidate, raw_event_input, raw_event_output):
        assert private_marker not in builder_prompt

    builder_audit_path = audit_directory / "builder_model_calls.jsonl"
    solver_audit_path = audit_directory / "solver_model_calls.jsonl"
    assert assembly.builder.generator.audit_path == builder_audit_path.resolve()
    assert assembly.solver_generator.audit_path == solver_audit_path.resolve()
    builder_entry = json.loads(
        builder_audit_path.read_text(encoding="utf-8").splitlines()[1]
    )
    solver_entry = json.loads(
        solver_audit_path.read_text(encoding="utf-8").splitlines()[1]
    )
    assert builder_entry["operation_id"] == "experiment-one.builder.v001"
    assert builder_entry["layer"] == "builder"
    assert builder_entry["model"] == "builder-model"
    assert builder_delegate.reasoning_effort == "high"
    assert solver_delegate.reasoning_effort == "high"
    assert builder_entry["reasoning_effort"] == "high"
    assert (
        builder_entry["prompt_sha256"]
        == hashlib.sha256(builder_prompt.encode("utf-8")).hexdigest()
    )
    assert (
        builder_entry["response_sha256"]
        == hashlib.sha256(builder_response.encode("utf-8")).hexdigest()
    )
    assert solver_entry["operation_id"] == "experiment-one.solver.v001"
    assert solver_entry["layer"] == "solver"
    assert solver_entry["model"] == "solver-model"
    assert solver_entry["reasoning_effort"] == "high"
    assert solver_entry["prompt_sha256"] == hashlib.sha256(b"solver prompt").hexdigest()
    assert (
        solver_entry["response_sha256"]
        == hashlib.sha256(solver_response.encode("utf-8")).hexdigest()
    )


@pytest.mark.parametrize(
    ("builder_effort", "solver_effort"),
    [("low", "high"), ("high", "low")],
)
def test_experiment_one_assembly_rejects_non_high_reasoning_effort(
    tmp_path: Path, builder_effort: str, solver_effort: str
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    audit_directory = tmp_path / "audit"

    with pytest.raises(ValueError, match="reasoning effort must be high"):
        audit_module.assemble_experiment_one(
            workspace=workspace,
            builder_generator=openai_generator("builder response"),
            solver_generator=openai_generator("solver response"),
            builder_model="builder-model",
            audit_directory=audit_directory,
            builder_operation_id_factory=lambda: "experiment-one.builder.v001",
            solver_operation_id_factory=lambda: "experiment-one.solver.v001",
            builder_reasoning_effort=builder_effort,
            solver_reasoning_effort=solver_effort,
        )
    assert not audit_directory.exists()


@pytest.mark.parametrize(
    ("builder_effort", "solver_effort"),
    [("low", "high"), ("high", "low")],
)
def test_experiment_one_assembly_rejects_non_high_delegate_reasoning_effort(
    tmp_path: Path, builder_effort: str, solver_effort: str
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    audit_directory = tmp_path / "audit"

    with pytest.raises(ValueError, match="delegate reasoning effort must be high"):
        audit_module.assemble_experiment_one(
            workspace=workspace,
            builder_generator=openai_generator(
                "builder response", effort=builder_effort
            ),
            solver_generator=openai_generator(
                "solver response", effort=solver_effort
            ),
            builder_model="builder-model",
            audit_directory=audit_directory,
            builder_operation_id_factory=lambda: "experiment-one.builder.v001",
            solver_operation_id_factory=lambda: "experiment-one.solver.v001",
            builder_reasoning_effort="high",
            solver_reasoning_effort="high",
        )
    assert not audit_directory.exists()


def test_experiment_one_assembly_rejects_duck_typed_effort_spoof(
    tmp_path: Path,
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )

    class SpoofedGenerator(RecordingGenerator):
        def __init__(self) -> None:
            super().__init__("must not run", reasoning_effort="high")
            self.internal_request_effort = "medium"

    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    spoofed = SpoofedGenerator()

    with pytest.raises(ValueError, match="supported transport"):
        audit_module.assemble_experiment_one(
            workspace=workspace,
            builder_generator=spoofed,
            solver_generator=spoofed,
            builder_model="builder-model",
            audit_directory=tmp_path / "audit",
            builder_operation_id_factory=lambda: "experiment-one.builder.v001",
            solver_operation_id_factory=lambda: "experiment-one.solver.v001",
            builder_reasoning_effort="high",
            solver_reasoning_effort="high",
        )
    assert spoofed.calls == []


def test_experiment_one_assembly_rejects_request_config_subclass(
    tmp_path: Path,
) -> None:
    class SpoofedRequestConfig(OpenAIResponsesRequestConfig):
        pass

    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    builder = openai_generator("builder response")
    solver = openai_generator("solver response")
    builder._request_config = SpoofedRequestConfig(
        max_output_tokens=builder.max_output_tokens,
        reasoning_effort="high",
    )

    with pytest.raises(ValueError, match="supported request configuration"):
        importlib.import_module(
            "optimization_lab.harness_builder.experiment_one_audit"
        ).assemble_experiment_one(
            workspace=workspace,
            builder_generator=builder,
            solver_generator=solver,
            builder_model="builder-model",
            audit_directory=tmp_path / "audit",
            builder_operation_id_factory=lambda: "experiment-one.builder.v001",
            solver_operation_id_factory=lambda: "experiment-one.solver.v001",
            builder_reasoning_effort="high",
            solver_reasoning_effort="high",
        )


def test_formal_audited_generator_rejects_public_delegate_rebind(
    tmp_path: Path,
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    original = openai_generator("original high response")
    assembly = audit_module.assemble_experiment_one(
        workspace=workspace,
        builder_generator=openai_generator("builder response"),
        solver_generator=original,
        builder_model="builder-model",
        audit_directory=tmp_path / "audit",
        builder_operation_id_factory=lambda: "experiment-one.builder.v001",
        solver_operation_id_factory=lambda: "experiment-one.solver.v001",
        builder_reasoning_effort="high",
        solver_reasoning_effort="high",
    )
    spoofed = ReboundLowTransport()

    try:
        assembly.solver_generator.generator = spoofed
    except (AttributeError, TypeError):
        pass
    else:
        with pytest.raises((TypeError, ValueError), match="transport|binding"):
            assembly.solver_generator.generate("solver prompt", model="solver-model")

    assert spoofed.calls == []
    assert original.client.responses.calls == []
    assert not (tmp_path / "audit" / "solver_model_calls.jsonl").exists()


def test_formal_audited_generator_rejects_private_delegate_binding_rebind(
    tmp_path: Path,
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    original = openai_generator("original high response")
    assembly = audit_module.assemble_experiment_one(
        workspace=workspace,
        builder_generator=openai_generator("builder response"),
        solver_generator=original,
        builder_model="builder-model",
        audit_directory=tmp_path / "audit",
        builder_operation_id_factory=lambda: "experiment-one.builder.v001",
        solver_operation_id_factory=lambda: "experiment-one.solver.v001",
        builder_reasoning_effort="high",
        solver_reasoning_effort="high",
    )
    spoofed = ReboundLowTransport()

    try:
        assembly.solver_generator._delegate_binding = spoofed
    except (AttributeError, TypeError):
        pass
    else:
        with pytest.raises((TypeError, ValueError), match="transport|binding"):
            assembly.solver_generator.generate("solver prompt", model="solver-model")

    assert spoofed.calls == []
    assert original.client.responses.calls == []
    assert not (tmp_path / "audit" / "solver_model_calls.jsonl").exists()


def test_audited_generator_writes_hash_only_jsonl_and_returns_original_result(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    audit_path = tmp_path / "audit" / "model_calls.jsonl"
    delegate = RecordingGenerator("RAW_RESPONSE SECRET_TOKEN")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "lineage-a.solver.v001",
        layer="solver",
        reasoning_effort="high",
    )

    result = audited.generate(
        "RAW_PROMPT PRIVATE_KEY https://api.secret.example", model="gpt-5"
    )

    assert result.raw_response == "RAW_RESPONSE SECRET_TOKEN"
    assert audited.estimated_api_cost_usd() == 1.25
    raw_line = audit_path.read_text(encoding="utf-8")
    assert raw_line.endswith("\n")
    assert "RAW_PROMPT" not in raw_line
    assert "RAW_RESPONSE" not in raw_line
    assert "PRIVATE_KEY" not in raw_line
    assert "secret.example" not in raw_line
    entries = [json.loads(line) for line in raw_line.splitlines()]
    assert [entry["event"] for entry in entries] == ["start", "success"]
    start, success = entries
    assert set(start) == {
        "schema_version",
        "event",
        "operation_id",
        "layer",
        "transport",
        "model",
        "reasoning_effort",
        "prompt_sha256",
        "created_at_utc",
    }
    assert set(success) == set(start) | {"provider", "response_sha256", "usage"}
    assert start == {
        "schema_version": 2,
        "event": "start",
        "operation_id": "lineage-a.solver.v001",
        "layer": "solver",
        "transport": "test_fixture",
        "model": "gpt-5",
        "reasoning_effort": "high",
        "prompt_sha256": hashlib.sha256(
            b"RAW_PROMPT PRIVATE_KEY https://api.secret.example"
        ).hexdigest(),
        "created_at_utc": start["created_at_utc"],
    }
    assert success == {
        **start,
        "event": "success",
        "provider": "fixture-provider",
        "response_sha256": hashlib.sha256(b"RAW_RESPONSE SECRET_TOKEN").hexdigest(),
        "usage": {"input_tokens": 11, "output_tokens": 7, "total_tokens": 18},
        "created_at_utc": success["created_at_utc"],
    }
    for entry in entries:
        created = datetime.fromisoformat(
            entry["created_at_utc"].replace("Z", "+00:00")
        )
        assert created.utcoffset().total_seconds() == 0


def test_audited_generator_rejects_delegate_reasoning_effort_mismatch(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    delegate = RecordingGenerator("must not run", reasoning_effort="low")
    audit_path = tmp_path / "model_calls.jsonl"
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "effort-mismatch-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    with pytest.raises(ValueError, match="reasoning effort does not match delegate"):
        audited.generate("prompt", model="gpt-5")
    assert delegate.calls == []
    assert not audit_path.exists()
    assert not (tmp_path / ".model_calls.jsonl.operations").exists()


def test_audited_generator_retries_short_ledger_writes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    AuditedGenerator = audit_module.AuditedGenerator
    delegate = RecordingGenerator("short write response")
    audit_path = tmp_path / "model_calls.jsonl"
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "short-write-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )
    real_write = audit_module.os.write
    write_sizes: list[int] = []

    def short_first_write(descriptor: int, payload: bytes) -> int:
        if not write_sizes:
            payload = payload[: max(1, len(payload) // 2)]
        written = real_write(descriptor, payload)
        write_sizes.append(written)
        return written

    monkeypatch.setattr(audit_module.os, "write", short_first_write)

    audited.generate("short write prompt", model="gpt-5")

    assert len(write_sizes) >= 2
    raw_ledger = audit_path.read_bytes()
    assert raw_ledger.endswith(b"\n")
    records = [json.loads(line) for line in raw_ledger.splitlines()]
    assert [record["event"] for record in records] == ["start", "success"]


def test_audited_generator_rejects_truncated_ledger_before_model_call(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    audit_path = tmp_path / "model_calls.jsonl"
    first = AuditedGenerator(
        generator=RecordingGenerator("first response"),
        audit_path=audit_path,
        operation_id_factory=lambda: "complete-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )
    first.generate("first prompt", model="gpt-5")
    complete_ledger = audit_path.read_bytes()
    assert complete_ledger.endswith(b"\n")
    truncated_ledger = complete_ledger[:-1]
    audit_path.write_bytes(truncated_ledger)
    claim_directory = tmp_path / ".model_calls.jsonl.operations"
    initial_claims = sorted(claim_directory.glob("*.claim"))

    delegate = RecordingGenerator("must not run")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "fresh-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    with pytest.raises(ValueError, match="end with a newline"):
        audited.generate("fresh prompt", model="gpt-5")
    assert delegate.calls == []
    assert audit_path.read_bytes() == truncated_ledger
    assert sorted(claim_directory.glob("*.claim")) == initial_claims


def test_audited_generator_rejects_reused_operation_id_before_model_call(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    delegate = RecordingGenerator("same response", "same response")
    audit_path = tmp_path / "model_calls.jsonl"
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "builder-v001",
        layer="builder",
        reasoning_effort="high",
    )

    audited.generate("same prompt", model="gpt-5")

    with pytest.raises(ValueError, match="already exists"):
        audited.generate("same prompt", model="gpt-5")
    assert len(delegate.calls) == 1
    assert len(audit_path.read_text(encoding="utf-8").splitlines()) == 2


@pytest.mark.skipif(os.name != "nt", reason="Windows junction behavior only")
def test_audited_generator_rejects_claim_directory_junction_before_model_call(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    audit_path = tmp_path / "model_calls.jsonl"
    claim_directory = tmp_path / ".model_calls.jsonl.operations"
    external_directory = tmp_path / "external_claims"
    external_directory.mkdir()
    creation = subprocess.run(
        [
            "cmd.exe",
            "/d",
            "/c",
            "mklink",
            "/J",
            os.fspath(claim_directory),
            os.fspath(external_directory),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if creation.returncode != 0:
        details = (creation.stdout + creation.stderr).strip()
        pytest.skip(f"Windows junction creation is unavailable: {details}")
    attributes = os.lstat(claim_directory).st_file_attributes
    assert attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT
    assert claim_directory.is_dir()
    assert not claim_directory.is_symlink()

    delegate = RecordingGenerator("must not run")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "junction-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )
    rejection = None
    try:
        audited.generate("junction prompt", model="gpt-5")
    except ValueError as exc:
        rejection = exc
    external_claims = list(external_directory.glob("*.claim"))

    assert rejection is not None, (
        "claim directory junction was followed: "
        f"delegate_calls={delegate.calls!r}, "
        f"external_claims={[path.name for path in external_claims]!r}"
    )
    assert "claim directory is unsafe" in str(rejection)
    assert delegate.calls == []
    assert external_claims == []


def test_audited_generator_rejects_unsafe_audit_path_ancestor_before_model_call(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    external_directory = tmp_path / "external_audit_target"
    external_directory.mkdir()
    unsafe_ancestor = tmp_path / "unsafe_audit_ancestor"
    if os.name == "nt":
        creation = subprocess.run(
            [
                "cmd.exe",
                "/d",
                "/s",
                "/c",
                "mklink",
                "/J",
                os.fspath(unsafe_ancestor),
                os.fspath(external_directory),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        assert creation.returncode == 0, creation.stderr or creation.stdout
        attributes = os.lstat(unsafe_ancestor).st_file_attributes
        assert attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT
    else:
        unsafe_ancestor.symlink_to(external_directory, target_is_directory=True)
        assert unsafe_ancestor.is_symlink()

    audit_path = unsafe_ancestor / "nested" / "model_calls.jsonl"
    delegate = RecordingGenerator("must not run")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "unsafe-ancestor-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    with pytest.raises(ValueError, match="path is unsafe"):
        audited.generate("prompt", model="gpt-5")
    assert delegate.calls == []
    assert not (external_directory / "nested").exists()


def test_audited_generator_claims_operation_once_across_processes(
    tmp_path: Path,
) -> None:
    context = multiprocessing.get_context("spawn")
    audit_path = tmp_path / "model_calls.jsonl"
    calls_path = tmp_path / "delegate_calls"
    calls_path.mkdir()
    start_barrier = context.Barrier(3)
    delegate_barrier = context.Barrier(2)
    outcomes = context.Queue()
    processes = [
        context.Process(
            target=_run_competing_audited_generator,
            args=(
                audit_path,
                calls_path,
                start_barrier,
                delegate_barrier,
                outcomes,
            ),
        )
        for _ in range(2)
    ]

    for process in processes:
        process.start()
    start_barrier.wait(timeout=10.0)
    for process in processes:
        process.join(timeout=15.0)
    stuck = [process for process in processes if process.is_alive()]
    for process in stuck:
        process.terminate()
        process.join(timeout=5.0)

    assert stuck == []
    assert [process.exitcode for process in processes] == [0, 0]
    try:
        observed = [outcomes.get(timeout=5.0) for _ in processes]
    except Empty:
        pytest.fail("competing audit process did not report an outcome")
    finally:
        outcomes.close()
        outcomes.join_thread()
    assert sorted(kind for kind, _ in observed) == ["completed", "rejected"]
    assert all(
        "already exists" in detail for kind, detail in observed if kind == "rejected"
    )
    assert len(list(calls_path.glob("*.call"))) == 1
    assert len(audit_path.read_text(encoding="utf-8").splitlines()) == 2


@pytest.mark.skipif(os.name != "nt", reason="Windows lock behavior only")
def test_windows_lock_retries_crt_contention_timeout(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    attempts: list[int] = []

    def simulated_locking(descriptor: int, mode: int, count: int) -> None:
        assert count == 1
        attempts.append(mode)
        if mode == audit_module.msvcrt.LK_LOCK and attempts.count(mode) == 1:
            raise OSError(errno.EDEADLK, os.strerror(errno.EDEADLK))

    monkeypatch.setattr(audit_module.msvcrt, "locking", simulated_locking)
    lock_path = tmp_path / "audit.lock"
    with lock_path.open("w+b") as stream:
        stream.write(b"\0")
        stream.flush()
        session = audit_module._PinnedAuditSession(SimpleNamespace())
        session.lock_descriptor = stream.fileno()

        with session.locked():
            pass

    assert attempts == [
        audit_module.msvcrt.LK_LOCK,
        audit_module.msvcrt.LK_LOCK,
        audit_module.msvcrt.LK_UNLCK,
    ]


def test_audited_generator_preserves_distinct_concurrent_process_records(
    tmp_path: Path,
) -> None:
    context = multiprocessing.get_context("spawn")
    process_count = 8
    calls_per_process = 12
    expected_calls = process_count * calls_per_process
    audit_path = tmp_path / "model_calls.jsonl"
    calls_path = tmp_path / "delegate_calls"
    calls_path.mkdir()
    start_barrier = context.Barrier(process_count)
    first_call_barrier = context.Barrier(process_count)
    outcomes = context.Queue()
    processes = [
        context.Process(
            target=_run_distinct_audited_generator_burst,
            args=(
                audit_path,
                calls_path,
                start_barrier,
                first_call_barrier,
                outcomes,
                process_index,
                calls_per_process,
            ),
        )
        for process_index in range(process_count)
    ]

    try:
        for process in processes:
            process.start()
        for process in processes:
            process.join(timeout=30.0)
        stuck_processes = [process for process in processes if process.is_alive()]
        for process in stuck_processes:
            process.terminate()
            process.join(timeout=5.0)

        observed = [outcomes.get(timeout=5.0) for _ in range(process_count)]
    finally:
        outcomes.close()
        outcomes.join_thread()

    assert stuck_processes == []
    assert all(process.exitcode == 0 for process in processes)
    failures = [
        detail for kind, _, detail in observed if kind == "failed"
    ]
    assert failures == [], "\n\n".join(failures)
    assert observed == [
        ("completed", calls_per_process, "")
        for _ in range(process_count)
    ]
    assert len(list(calls_path.glob("*.call"))) == expected_calls
    claim_directory = tmp_path / ".model_calls.jsonl.operations"
    assert len(list(claim_directory.glob("*.claim"))) == expected_calls

    raw_ledger = audit_path.read_bytes()
    assert raw_ledger.endswith(b"\n")
    records = [json.loads(line) for line in raw_ledger.splitlines()]
    assert len(records) == expected_calls * 2
    assert len({record["operation_id"] for record in records}) == expected_calls
    for operation_id in {record["operation_id"] for record in records}:
        assert [
            record["event"]
            for record in records
            if record["operation_id"] == operation_id
        ] == ["start", "success"]


def test_audited_generator_keeps_crashed_operation_id_claimed(tmp_path: Path) -> None:
    context = multiprocessing.get_context("spawn")
    audit_path = tmp_path / "model_calls.jsonl"
    call_marker = tmp_path / "crashing_delegate.call"
    process = context.Process(
        target=_run_crashing_audited_generator,
        args=(audit_path, call_marker),
    )

    process.start()
    process.join(timeout=10.0)
    if process.is_alive():
        process.terminate()
        process.join(timeout=5.0)

    assert process.exitcode == 23
    assert call_marker.is_file()
    records = [json.loads(line) for line in audit_path.read_text(encoding="utf-8").splitlines()]
    assert len(records) == 1
    assert records[0]["event"] == "start"
    assert records[0]["operation_id"] == "crashed-operation-v001"
    assert records[0]["prompt_sha256"] == hashlib.sha256(b"crashing prompt").hexdigest()

    AuditedGenerator, _ = _audit_api()
    delegate = RecordingGenerator("must not run")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "crashed-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )
    with pytest.raises(ValueError, match="already exists"):
        audited.generate("retry prompt", model="gpt-5")
    assert delegate.calls == []


def test_audited_generator_writes_terminal_error_for_delegate_exception(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    audit_path = tmp_path / "model_calls.jsonl"
    audited = AuditedGenerator(
        generator=FailingGenerator(),
        audit_path=audit_path,
        operation_id_factory=lambda: "failed-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    with pytest.raises(RuntimeError, match="PRIVATE FAILURE MESSAGE"):
        audited.generate("failed prompt", model="gpt-5")

    records = [json.loads(line) for line in audit_path.read_text(encoding="utf-8").splitlines()]
    assert [record["event"] for record in records] == ["start", "error"]
    assert records[1]["error_type"] == "RuntimeError"
    assert "PRIVATE FAILURE MESSAGE" not in audit_path.read_text(encoding="utf-8")


def test_audited_generator_rejects_hard_linked_ledger_before_model_call(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    external_path = tmp_path / "external.jsonl"
    external_path.write_bytes(b"")
    audit_path = tmp_path / "model_calls.jsonl"
    os.link(external_path, audit_path)
    assert os.stat(audit_path).st_nlink >= 2
    delegate = RecordingGenerator("must not run")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "hard-link-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    with pytest.raises(ValueError, match="ledger path is unsafe"):
        audited.generate("prompt", model="gpt-5")

    assert delegate.calls == []
    assert external_path.read_bytes() == b""


def test_audited_generator_rejects_hard_linked_lock_before_model_call(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    external_path = tmp_path / "external.lock"
    external_path.write_bytes(b"x")
    lock_path = tmp_path / ".model_calls.jsonl.lock"
    os.link(external_path, lock_path)
    delegate = RecordingGenerator("must not run")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=tmp_path / "model_calls.jsonl",
        operation_id_factory=lambda: "hard-link-lock-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    with pytest.raises(ValueError, match="ledger path is unsafe"):
        audited.generate("prompt", model="gpt-5")

    assert delegate.calls == []
    assert external_path.read_bytes() == b"x"


@pytest.mark.parametrize("target", ["ledger", "lock"])
def test_audited_generator_rejects_hard_link_created_during_dispatch(
    tmp_path: Path, target: str
) -> None:
    AuditedGenerator, _ = _audit_api()
    audit_path = tmp_path / "model_calls.jsonl"
    lock_path = tmp_path / ".model_calls.jsonl.lock"
    source_path = audit_path if target == "ledger" else lock_path
    link_path = tmp_path / f"external-{target}"
    delegate = HardLinkingGenerator(source_path, link_path)
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: f"dispatch-hard-link-{target}-v001",
        layer="solver",
        reasoning_effort="high",
    )

    with pytest.raises(ValueError, match="identity|unsafe"):
        audited.generate("prompt", model="gpt-5")

    assert delegate.calls == [("prompt", "gpt-5")]
    records = [
        json.loads(line)
        for line in audit_path.read_text(encoding="utf-8").splitlines()
    ]
    assert [record["event"] for record in records] == ["start"]
    assert os.stat(source_path).st_nlink >= 2


def test_posix_identity_check_rejects_authoritative_path_replacement() -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    pinned = SimpleNamespace(
        st_mode=stat.S_IFREG | 0o600,
        st_nlink=1,
        st_dev=7,
        st_ino=11,
    )
    replacement = SimpleNamespace(
        st_mode=stat.S_IFREG | 0o600,
        st_nlink=1,
        st_dev=7,
        st_ino=12,
    )

    with pytest.raises(ValueError, match="identity"):
        audit_module._verify_posix_file_identity(
            pinned,
            replacement,
            "audit ledger path is unsafe",
        )


def test_posix_identity_check_rejects_new_hard_link() -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    linked = SimpleNamespace(
        st_mode=stat.S_IFREG | 0o600,
        st_nlink=2,
        st_dev=7,
        st_ino=11,
    )

    with pytest.raises(ValueError, match="unsafe"):
        audit_module._verify_posix_file_identity(
            linked,
            linked,
            "audit ledger path is unsafe",
        )


@pytest.mark.skipif(os.name != "nt", reason="Windows handle sharing behavior only")
def test_audited_generator_pins_ledger_identity_across_dispatch(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    audit_path = tmp_path / "model_calls.jsonl"
    moved_path = tmp_path / "moved-model-calls.jsonl"
    delegate = LedgerReplacementGenerator(audit_path, moved_path)
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "replacement-attack-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    audited.generate("prompt", model="gpt-5")

    assert isinstance(delegate.replacement_error, PermissionError)
    assert not moved_path.exists()
    records = [
        json.loads(line)
        for line in audit_path.read_text(encoding="utf-8").splitlines()
    ]
    assert [record["event"] for record in records] == ["start", "success"]


@pytest.mark.skipif(os.name != "nt", reason="Windows directory flush behavior only")
def test_audited_generator_syncs_parent_directory_on_first_ledger_creation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    audit_path = tmp_path / "audit" / "model_calls.jsonl"
    real_flush = audit_module._windows_flush_handle
    flushed_paths: list[str] = []

    def recording_flush(handle: int) -> None:
        flushed_paths.append(audit_module._windows_final_path(handle))
        real_flush(handle)

    monkeypatch.setattr(audit_module, "_windows_flush_handle", recording_flush)
    audited = audit_module.AuditedGenerator(
        generator=RecordingGenerator("response"),
        audit_path=audit_path,
        operation_id_factory=lambda: "parent-sync-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    audited.generate("prompt", model="gpt-5")

    expected_parent = audit_module._normalize_windows_final_path(
        os.fspath(audit_path.parent)
    )
    assert flushed_paths.count(expected_parent) >= 2


@pytest.mark.skipif(os.name != "nt", reason="Windows directory flush behavior only")
def test_audited_generator_syncs_each_new_directory_containing_parent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    audit_path = tmp_path / "new-parent" / "audit" / "model_calls.jsonl"
    real_flush = audit_module._windows_flush_handle
    flushed_paths: list[str] = []

    def recording_flush(handle: int) -> None:
        flushed_paths.append(audit_module._windows_final_path(handle))
        real_flush(handle)

    monkeypatch.setattr(audit_module, "_windows_flush_handle", recording_flush)
    audited = audit_module.AuditedGenerator(
        generator=RecordingGenerator("response"),
        audit_path=audit_path,
        operation_id_factory=lambda: "nested-parent-sync-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    audited.generate("prompt", model="gpt-5")

    for containing_parent in (
        tmp_path,
        tmp_path / "new-parent",
        tmp_path / "new-parent" / "audit",
    ):
        expected = audit_module._normalize_windows_final_path(
            os.fspath(containing_parent)
        )
        assert expected in flushed_paths


@pytest.mark.skipif(os.name != "nt", reason="Windows directory flush behavior only")
def test_audited_generator_syncs_recreated_claim_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    audit_path = tmp_path / "audit" / "model_calls.jsonl"
    first = audit_module.AuditedGenerator(
        generator=RecordingGenerator("first response"),
        audit_path=audit_path,
        operation_id_factory=lambda: "claim-sync-first-v001",
        layer="solver",
        reasoning_effort="high",
    )
    first.generate("first prompt", model="gpt-5")
    claim_directory = audit_path.with_name(f".{audit_path.name}.operations")
    for claim in claim_directory.iterdir():
        claim.unlink()
    claim_directory.rmdir()
    real_flush = audit_module._windows_flush_handle
    flushed_paths: list[str] = []

    def recording_flush(handle: int) -> None:
        flushed_paths.append(audit_module._windows_final_path(handle))
        real_flush(handle)

    monkeypatch.setattr(audit_module, "_windows_flush_handle", recording_flush)
    second = audit_module.AuditedGenerator(
        generator=RecordingGenerator("second response"),
        audit_path=audit_path,
        operation_id_factory=lambda: "claim-sync-second-v001",
        layer="solver",
        reasoning_effort="high",
    )

    second.generate("second prompt", model="gpt-5")

    expected_parent = audit_module._normalize_windows_final_path(
        os.fspath(audit_path.parent)
    )
    assert expected_parent in flushed_paths


def test_posix_directory_creation_syncs_each_containing_parent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    next_descriptor = iter(range(100, 200))
    created_in: list[int] = []
    fsynced: list[int] = []

    def fake_open(*args: object, **kwargs: object) -> int:
        return next(next_descriptor)

    def fake_mkdir(
        path: object, mode: int = 0o777, *, dir_fd: int | None = None
    ) -> None:
        assert dir_fd is not None
        created_in.append(dir_fd)

    monkeypatch.setattr(audit_module.os, "O_DIRECTORY", 0x1000, raising=False)
    monkeypatch.setattr(audit_module.os, "O_NOFOLLOW", 0x2000, raising=False)
    monkeypatch.setattr(audit_module.os, "open", fake_open)
    monkeypatch.setattr(audit_module.os, "mkdir", fake_mkdir)
    monkeypatch.setattr(
        audit_module.os,
        "fstat",
        lambda descriptor: SimpleNamespace(st_mode=stat.S_IFDIR | 0o700),
    )
    monkeypatch.setattr(audit_module.os, "fsync", fsynced.append)
    monkeypatch.setattr(audit_module.os, "close", lambda descriptor: None)

    audit_module._PinnedAuditSession._open_posix_directory(
        tmp_path / "abstract-posix" / "audit"
    )

    assert created_in
    assert fsynced == created_in


@pytest.mark.parametrize("unsafe_errno", [errno.ENOTDIR, errno.ELOOP])
def test_posix_directory_traversal_normalizes_unsafe_component_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    unsafe_errno: int,
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    open_calls = 0
    closed: list[int] = []

    def fake_open(*args: object, **kwargs: object) -> int:
        nonlocal open_calls
        open_calls += 1
        if open_calls == 1:
            return 100
        raise OSError(unsafe_errno, "unsafe path component")

    def fake_mkdir(*args: object, **kwargs: object) -> None:
        raise FileExistsError

    monkeypatch.setattr(audit_module.os, "O_DIRECTORY", 0x1000, raising=False)
    monkeypatch.setattr(audit_module.os, "O_NOFOLLOW", 0x2000, raising=False)
    monkeypatch.setattr(audit_module.os, "open", fake_open)
    monkeypatch.setattr(audit_module.os, "mkdir", fake_mkdir)
    monkeypatch.setattr(audit_module.os, "close", closed.append)

    with pytest.raises(ValueError, match="path is unsafe") as rejection:
        audit_module._PinnedAuditSession._open_posix_directory(
            tmp_path / "unsafe-component" / "audit"
        )

    assert isinstance(rejection.value.__cause__, OSError)
    assert rejection.value.__cause__.errno == unsafe_errno
    assert closed == [100]


def test_posix_directory_traversal_preserves_unrelated_open_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    open_calls = 0
    closed: list[int] = []

    def fake_open(*args: object, **kwargs: object) -> int:
        nonlocal open_calls
        open_calls += 1
        if open_calls == 1:
            return 100
        raise OSError(errno.EACCES, "permission denied")

    def fake_mkdir(*args: object, **kwargs: object) -> None:
        raise FileExistsError

    monkeypatch.setattr(audit_module.os, "O_DIRECTORY", 0x1000, raising=False)
    monkeypatch.setattr(audit_module.os, "O_NOFOLLOW", 0x2000, raising=False)
    monkeypatch.setattr(audit_module.os, "open", fake_open)
    monkeypatch.setattr(audit_module.os, "mkdir", fake_mkdir)
    monkeypatch.setattr(audit_module.os, "close", closed.append)

    with pytest.raises(OSError) as rejection:
        audit_module._PinnedAuditSession._open_posix_directory(
            tmp_path / "unreadable-component" / "audit"
        )

    assert rejection.value.errno == errno.EACCES
    assert closed == [100]


def test_audited_generator_initializes_existing_empty_lock_file(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    lock_path = tmp_path / ".model_calls.jsonl.lock"
    lock_path.write_bytes(b"")
    audited = AuditedGenerator(
        generator=RecordingGenerator("response"),
        audit_path=tmp_path / "model_calls.jsonl",
        operation_id_factory=lambda: "empty-lock-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    audited.generate("prompt", model="gpt-5")

    assert lock_path.stat().st_size >= 1


@pytest.mark.skipif(os.name != "nt", reason="Windows last-error behavior only")
def test_windows_open_always_clears_stale_last_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    audit_module = importlib.import_module(
        "optimization_lab.harness_builder.experiment_one_audit"
    )
    observed_last_errors: list[int] = []

    class FakeKernel32:
        @staticmethod
        def CreateFileW(*args: object) -> int:
            observed_last_errors.append(audit_module.ctypes.get_last_error())
            audit_module.ctypes.set_last_error(0)
            return 123

    monkeypatch.setattr(audit_module, "_KERNEL32", FakeKernel32())
    audit_module.ctypes.set_last_error(audit_module._ERROR_ALREADY_EXISTS)

    handle, created = audit_module._windows_open_handle(
        tmp_path / "new.lock", directory=False, open_always=True
    )

    assert handle == 123
    assert created is True
    assert observed_last_errors == [0]


def test_audit_ledger_rejects_duplicate_operation_id_even_when_content_matches(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    audit_path = tmp_path / "model_calls.jsonl"
    first = AuditedGenerator(
        generator=RecordingGenerator("first response"),
        audit_path=audit_path,
        operation_id_factory=lambda: "duplicated-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )
    first.generate("first prompt", model="gpt-5")
    duplicated = json.loads(
        audit_path.read_text(encoding="utf-8").splitlines()[1]
    )
    duplicated["created_at_utc"] = "2000-01-01T00:00:00.000000Z"
    with audit_path.open("a", encoding="utf-8", newline="") as stream:
        stream.write(
            json.dumps(duplicated, sort_keys=True, separators=(",", ":")) + "\n"
        )

    delegate = RecordingGenerator("must not run")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "fresh-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )
    with pytest.raises(ValueError, match="duplicate operation id"):
        audited.generate("fresh prompt", model="gpt-5")
    assert delegate.calls == []


def test_audit_ledger_rejects_terminal_request_mismatch(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    audit_path = tmp_path / "model_calls.jsonl"
    first = AuditedGenerator(
        generator=RecordingGenerator("first response"),
        audit_path=audit_path,
        operation_id_factory=lambda: "first-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )
    first.generate("first prompt", model="gpt-5")
    records = [
        json.loads(line)
        for line in audit_path.read_text(encoding="utf-8").splitlines()
    ]
    records[1]["model"] = "tampered-model"
    audit_path.write_text(
        "".join(
            json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
            for record in records
        ),
        encoding="utf-8",
        newline="",
    )

    delegate = RecordingGenerator("must not run")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "fresh-operation-v001",
        layer="solver",
        reasoning_effort="high",
    )

    with pytest.raises(ValueError, match="terminal request does not match start"):
        audited.generate("fresh prompt", model="gpt-5")
    assert delegate.calls == []


def test_audited_generator_rejects_rebound_operation_id_fail_closed(
    tmp_path: Path,
) -> None:
    AuditedGenerator, _ = _audit_api()
    delegate = RecordingGenerator("first response", "different response")
    audit_path = tmp_path / "model_calls.jsonl"
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=audit_path,
        operation_id_factory=lambda: "builder-v002",
        layer="builder",
        reasoning_effort="high",
    )
    audited.generate("same prompt", model="gpt-5")

    with pytest.raises(ValueError, match="already exists"):
        audited.generate("same prompt", model="gpt-5")
    assert len(delegate.calls) == 1
    assert len(audit_path.read_text(encoding="utf-8").splitlines()) == 2


@pytest.mark.parametrize(
    "operation_id", ["", " space", "../escape", "contains newline\n"]
)
def test_audited_generator_rejects_unsafe_operation_id_before_model_call(
    operation_id: str, tmp_path: Path
) -> None:
    AuditedGenerator, _ = _audit_api()
    delegate = RecordingGenerator("must not run")
    audited = AuditedGenerator(
        generator=delegate,
        audit_path=tmp_path / "model_calls.jsonl",
        operation_id_factory=lambda: operation_id,
        layer="solver",
        reasoning_effort="high",
    )

    with pytest.raises(ValueError, match="operation id"):
        audited.generate("prompt", model="gpt-5")
    assert delegate.calls == []


def _cross_task_record() -> CrossTaskMemoryRecord:
    return CrossTaskMemoryRecord.create(
        record_id="prior-rule-001",
        rule="When public feedback reports a contract error, repair the emit path first.",
        source_benchmark="edgebench",
        source_instance_hash="a" * 64,
        source_lineage_hash="b" * 64,
        source_round=7,
        source_order=1,
        distiller_version="moss-memory-distiller-v1",
        sanitizer_version="moss-memory-sanitizer-v1",
    )


def test_experiment_one_builder_view_defaults_to_instance_only_memory() -> None:
    _, experiment_one_builder_view = _audit_api()
    inspection = {
        "current_sha256": "c" * 64,
        "current_artifact": {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {"schema_version": 1, "nodes": []},
        },
        "runs": [],
        "available_harnesses": [],
    }

    view = experiment_one_builder_view(inspection)

    assert view["builder_memory"] == {
        "mode": "instance_only",
        "cross_task_records": [],
        "snapshot_sha256": None,
    }


def test_experiment_one_builder_view_exposes_only_verified_online_memory() -> None:
    _, experiment_one_builder_view = _audit_api()
    inspection = {
        "current_sha256": "c" * 64,
        "current_artifact": {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {"schema_version": 1, "nodes": []},
        },
        "runs": [],
        "available_harnesses": [],
    }
    config = BuilderMemoryConfig(
        mode="cross_task_online", cross_task_records=(_cross_task_record(),)
    )

    view = experiment_one_builder_view(inspection, builder_memory=config)

    assert view["builder_memory"]["mode"] == "cross_task_online"
    assert view["builder_memory"]["cross_task_records"][0]["record_id"] == (
        "prior-rule-001"
    )
    assert view["builder_memory"]["snapshot_sha256"] is None
    assert "contract error" in view["builder_memory"]["cross_task_records"][0]["rule"]


def test_experiment_one_builder_view_rejects_unverified_memory_config() -> None:
    _, experiment_one_builder_view = _audit_api()
    inspection = {
        "current_sha256": "c" * 64,
        "current_artifact": {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {"schema_version": 1, "nodes": []},
        },
        "runs": [],
        "available_harnesses": [],
    }

    with pytest.raises(TypeError, match="Builder memory"):
        experiment_one_builder_view(
            inspection, builder_memory={"mode": "cross_task_online"}
        )
