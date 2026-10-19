from __future__ import annotations

import hashlib
import json
import sys
import types
import zipfile
from types import SimpleNamespace
from pathlib import Path

import pytest

from scripts import run_moss_experiment_one as cli
from optimization_lab.harness_builder import experiment_one_production as production
from optimization_lab.harness_builder.dual_harness import (
    HarnessWorkspace,
    TaskHarnessArtifact,
    TaskHarnessRuntime,
)
from optimization_lab.harness_builder.dual_runtime import EvaluationResult, PublicEvaluation
from optimization_lab.harness_builder.experiment_one import (
    LineageRoundRequest,
    ModelConfiguration,
    TargetBinding,
)
from optimization_lab.harness_builder.official_solutions import OfficialSolutionArchive
from optimization_lab.harness_builder.experiment_one_production import (
    ALEBenchPublicTaskLoader,
    EdgeBenchPublicTaskLoader,
    create_responses_generators,
)
from optimization_lab.harness_builder.builder_memory import BuilderMemoryConfig
from optimization_lab.harness_builder.tool_registry import BoundTool, ToolRegistry
from optimization_lab.harness_builder.experiment_one_tools import (
    CONTRACT_CHECK_TOOL_ID,
    ExperimentOneToolPack,
    allowed_experiment_one_tool_ids,
    build_experiment_one_tool_pack,
)


class _Responses:
    def __init__(self, outputs: list[str]) -> None:
        self.outputs = outputs
        self.calls: list[dict[str, object]] = []

    def create(self, **request: object) -> object:
        self.calls.append(request)
        return types.SimpleNamespace(output_text=self.outputs.pop(0), usage=None)


class _Client:
    def __init__(self, outputs: list[str]) -> None:
        self.responses = _Responses(outputs)


class _EdgeAdapter:
    def __init__(self, evidence_root: Path) -> None:
        self.evidence_root = evidence_root
        self.calls: list[tuple[object, str]] = []

    def evaluate(self, artifact: object, *, operation_id: str) -> EvaluationResult:
        self.calls.append((artifact, operation_id))
        evidence = self.evidence_root / f"{operation_id}.json"
        evidence.parent.mkdir(parents=True, exist_ok=True)
        evidence.write_text(json.dumps({"report": {"valid": True}}), encoding="utf-8")
        return EvaluationResult(
            public=PublicEvaluation(score=12.5, feedback="official public feedback"),
            private={
                "evidence_path": str(evidence),
                "evidence_sha256": _sha256(evidence),
            },
        )


class _ALEAdapter:
    def __init__(self, evidence_root: Path) -> None:
        self.evidence_root = evidence_root
        self.calls: list[tuple[object, str]] = []

    def evaluate_public(self, artifact: object, *, operation_id: str) -> EvaluationResult:
        self.calls.append((artifact, operation_id))
        evidence = self.evidence_root / f"{operation_id}.json"
        evidence.parent.mkdir(parents=True, exist_ok=True)
        evidence.write_text(json.dumps({"phase": "public", "valid": True}), encoding="utf-8")
        return EvaluationResult(
            public=PublicEvaluation(score=321.0, feedback="official ALE public feedback"),
            private={
                "evidence_path": str(evidence),
                "evidence_sha256": _sha256(evidence),
            },
        )


class _RaisingEdgeAdapter:
    def __init__(self) -> None:
        self.calls = 0

    def evaluate(self, artifact: object, *, operation_id: str) -> EvaluationResult:
        self.calls += 1
        raise RuntimeError("official evaluator unavailable")


class _ForbiddenEdgeAdapter:
    def __init__(self) -> None:
        self.calls = 0

    def evaluate(self, artifact: object, *, operation_id: str) -> EvaluationResult:
        self.calls += 1
        raise AssertionError("replay must not call the evaluator")


def _frozen_h0() -> dict[str, object]:
    return {
        "schema_version": 1,
        "version": 1,
        "parent_sha256": None,
        "spec": {
            "schema_version": 1,
            "nodes": [
                {
                    "node_id": "solve",
                    "kind": "model_call",
                    "role": "solver",
                    "prompt": "Solve this public task.\n\n{task}",
                },
                {"node_id": "emit", "kind": "emit", "input_key": "latest_output"},
            ],
        },
    }


def _configuration() -> ModelConfiguration:
    return ModelConfiguration(
        provider="openai-compatible",
        api_family="responses",
        transport="https",
        model="gpt-5.6-sol",
        reasoning_effort="high",
        max_output_tokens=4096,
        sampling_parameters={},
        tool_permission_policy={"mode": "allowlist", "tools": []},
    )


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_production_factory_wires_edge_controller_without_external_calls(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """The production entry point must be constructible before execution."""
    h0 = production.task_harness_from_frozen_schema(_frozen_h0())
    config = _configuration()
    targets = tuple(
        SimpleNamespace(
            position=position,
            task_id=task_id,
            submission_path="solution.py",
            evaluator_timeout_seconds=870 if task_id == "treant_forest" else 600,
        )
        for position, task_id in (
            ("A", "apple_incremental_game"),
            ("B", "molecular_self_assembly"),
            ("C", "treant_forest"),
        )
    )
    manifest = SimpleNamespace(
        suite="edgebench",
        benchmark="EdgeBench",
        h0=h0.to_dict(),
        targets=targets,
        builder_model=config,
        solver_model=config,
        official=SimpleNamespace(
            source_repository="/official",
            source_revision="a87350ab80eeb320b13cb71d1b0c3ffcc20a670f",
            task_data_revision="6cc5a7f1b3288ce52484ad828177b8cc86b05b75",
            evolution_evaluator="sforge eval",
            cross_test_evaluator="sforge eval",
            score_direction="maximize",
        ),
        sha256="a" * 64,
    )
    context = SimpleNamespace(
        manifest=manifest,
        artifact_root=tmp_path,
        seed_id="S1",
        canary_suite_root=tmp_path / "canary",
        formal_seed_root=tmp_path / "formal" / "edgebench" / "S1",
    )
    monkeypatch.setattr(
        production,
        "create_responses_generators",
        lambda **_: (object(), object()),
    )
    monkeypatch.setattr(
        production,
        "EdgeBenchPublicTaskLoader",
        lambda **_: SimpleNamespace(
            load=lambda task_id, submission_path: "PUBLIC TASK"
        ),
    )
    monkeypatch.setattr(production, "EdgeBenchOfficialAdapter", lambda **_: object())

    controller = production.build_production_controller(context)

    assert all(callable(getattr(controller, name)) for name in (
        "run_canary", "evolve", "freeze", "cross_test", "resume"
    ))
    assert controller.manifest.h0.sha256 == h0.sha256


def test_production_factory_accepts_real_cli_frozen_model_records(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    manifest = cli.load_frozen_manifest(cli.DEFAULT_MANIFESTS["edgebench"])
    context = cli.ExecutionContext(manifest=manifest, artifact_root=tmp_path, seed_id="S1")
    monkeypatch.setattr(
        production,
        "create_responses_generators",
        lambda **_: (object(), object()),
    )
    monkeypatch.setattr(
        production,
        "EdgeBenchPublicTaskLoader",
        lambda **_: SimpleNamespace(
            load=lambda task_id, submission_path: "PUBLIC TASK"
        ),
    )

    controller = production.build_production_controller(context)

    assert controller.manifest.builder_model_configuration.model == "gpt-5.6-sol"
    assert controller.manifest.solver_model_configuration.reasoning_effort == "high"


def test_round_executor_passes_builder_memory_config_to_assembly(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    config = _configuration()
    builder = production.OpenAIResponsesGenerator(
        client=_Client(["{}"]), max_output_tokens=4096, reasoning_effort="high"
    )
    solver = production.OpenAIResponsesGenerator(
        client=_Client(["candidate"]), max_output_tokens=4096, reasoning_effort="high"
    )
    memory = BuilderMemoryConfig()
    captured: list[BuilderMemoryConfig] = []

    def fake_assembly(**kwargs: object) -> object:
        captured.append(kwargs["builder_memory_config"])  # type: ignore[arg-type]
        raise AssertionError("stop after checking memory wiring")

    monkeypatch.setattr(production, "assemble_experiment_one", fake_assembly)
    executor = production.EdgeLineageRoundExecutor(
        builder_generator=builder,
        solver_generator=solver,
        adapter=object(),
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
        builder_memory_config=memory,
    )
    workspace = HarnessWorkspace(tmp_path / "workspace")
    target = TargetBinding("A", "task", "PUBLIC TASK", "solution.py", "e" * 64)
    with pytest.raises(AssertionError, match="checking memory wiring"):
        executor(
            LineageRoundRequest(
                manifest_sha256="a" * 64,
                benchmark="edgebench",
                seed_id="S1",
                position="A",
                round_index=1,
                operation_id="S1-A-round-01",
                lineage_root=tmp_path,
                workspace=workspace,
                target=target,
                builder_model_configuration=config,
                solver_model_configuration=config,
            )
        )
    assert captured == [memory]


def test_production_factory_wires_ale_controller_without_external_calls(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    h0 = production.task_harness_from_frozen_schema(_frozen_h0())
    config = _configuration()
    targets = tuple(
        SimpleNamespace(
            position=position,
            task_id=task_id,
            submission_path="main.cpp",
            evaluator_timeout_seconds=600,
        )
        for position, task_id in (("A", "ahc024"), ("B", "ahc026"), ("C", "ahc011"))
    )
    manifest = SimpleNamespace(
        suite="alebench",
        benchmark="ALE-Bench",
        h0=h0.to_dict(),
        targets=targets,
        builder_model=config,
        solver_model=config,
        official=SimpleNamespace(
            source_repository="/official/ale",
            source_revision="f7d927906dc1dcd860ee086e4560d576438b1354",
            task_data_revision="0f426173b4e4e73b09b2b3631ae0490f66b75f99",
            evolution_evaluator="public_eval",
            cross_test_evaluator="public_eval",
            score_direction="maximize",
        ),
        sha256="b" * 64,
    )
    context = SimpleNamespace(
        manifest=manifest,
        artifact_root=tmp_path,
        seed_id="S1",
        canary_suite_root=tmp_path / "canary" / "alebench",
        formal_seed_root=tmp_path / "formal" / "alebench" / "S1",
    )
    monkeypatch.setenv("MOSS_ALEBENCH_DATASET_ROOT", str(tmp_path / "ale-dataset"))
    monkeypatch.setenv("MOSS_ALEBENCH_PYTHON", str(tmp_path / "ale-python"))
    monkeypatch.setattr(
        production, "create_responses_generators", lambda **_: (object(), object())
    )
    monkeypatch.setattr(
        production,
        "ALEBenchPublicTaskLoader",
        lambda **_: SimpleNamespace(load=lambda task_id: f"PUBLIC ALE TASK {task_id}"),
    )

    controller = production.build_production_controller(context)

    assert all(
        callable(getattr(controller, name))
        for name in ("run_canary", "evolve", "freeze", "cross_test", "resume")
    )
    assert controller.manifest.h0.sha256 == h0.sha256
    assert [controller.manifest.target(position).task_id for position in ("A", "B", "C")] == [
        "ahc024",
        "ahc026",
        "ahc011",
    ]
    assert context.canary_suite_root not in context.formal_seed_root.parents


def test_load_freeze_receipt_accepts_integrity_envelope(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    payload = {"position": "A", "official_score": 12.5}
    path = tmp_path / "freeze_receipt.json"
    path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "payload": payload,
                "payload_sha256": hashlib.sha256(
                    json.dumps(
                        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
                    ).encode("utf-8")
                ).hexdigest(),
            }
        ),
        encoding="utf-8",
    )
    sentinel = object()
    observed: list[object] = []

    def parse(value: object) -> object:
        observed.append(value)
        return sentinel

    monkeypatch.setattr(production.FreezeReceipt, "from_dict", parse)

    assert production._load_freeze_receipt(path) is sentinel
    assert observed == [payload]


def test_factory_uses_explicit_openai_client_and_responses_for_both_layers(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[dict[str, str]] = []
    client = object()

    def openai(**kwargs: str) -> object:
        calls.append(kwargs)
        return client

    monkeypatch.setitem(sys.modules, "openai", types.SimpleNamespace(OpenAI=openai))
    monkeypatch.setenv("LLM_API_KEY", "test-key")
    monkeypatch.setenv("LLM_BASE_URL", "https://models.example/v1")
    builder, solver = create_responses_generators(builder_max_output_tokens=111, solver_max_output_tokens=222)
    assert calls == [{"api_key": "[REDACTED]", "base_url": "https://models.example/v1", "max_retries": 0}]
    assert builder.client is client and solver.client is client
    assert (builder.max_output_tokens, solver.max_output_tokens) == (111, 222)
    assert builder.reasoning_effort == solver.reasoning_effort == "high"
    assert builder.request_config.max_attempts == solver.request_config.max_attempts == 1
    assert builder.request_config.stream is solver.request_config.stream is True


def test_ale_public_binding_reads_only_fixed_snapshot_public_files(tmp_path: Path) -> None:
    revision = "0f426173b4e4e73b09b2b3631ae0490f66b75f99"
    snapshot = tmp_path / "snapshots" / revision / "ahc024.zip"
    snapshot.parent.mkdir(parents=True)
    with zipfile.ZipFile(snapshot, "w") as archive:
        archive.writestr("statement_en.md", "# Public ALE statement\nFULL_STATEMENT")
        archive.writestr("examples/02.txt", "EXAMPLE_TWO")
        archive.writestr("examples/01.txt", "EXAMPLE_ONE")
        archive.writestr("tools/README.md", "PUBLIC_TOOLS_README")
        archive.writestr("judge/private.txt", "PRIVATE_JUDGE_EVIDENCE")
    task = ALEBenchPublicTaskLoader(dataset_root=tmp_path, dataset_revision=revision, expected_zip_sha256={"ahc024": _sha256(snapshot)}).load("ahc024")
    assert all(marker in task for marker in ("FULL_STATEMENT", "EXAMPLE_ONE", "EXAMPLE_TWO", "PUBLIC_TOOLS_README"))
    assert task.index("examples/01.txt") < task.index("examples/02.txt")
    assert "PRIVATE_JUDGE_EVIDENCE" not in task
    assert "Return exactly one fenced source file" in task
    assert "```cpp23" in task
    assert "Do not include Markdown outside the fence" in task


def test_ale_public_binding_accepts_task_directory_prefix_in_snapshot(tmp_path: Path) -> None:
    revision = "0f426173b4e4e73b09b2b3631ae0490f66b75f99"
    snapshot = tmp_path / "snapshots" / revision / "ahc024.zip"
    snapshot.parent.mkdir(parents=True)
    with zipfile.ZipFile(snapshot, "w") as archive:
        archive.writestr("ahc024/statement_en.md", "# Public ALE statement\nPREFIXED_STATEMENT")
        archive.writestr("ahc024/examples/01.txt", "PREFIXED_EXAMPLE")
        archive.writestr("ahc024/tools/README.md", "PREFIXED_TOOLS_README")
        archive.writestr("ahc024/judge/private.txt", "PRIVATE_JUDGE_EVIDENCE")
    task = ALEBenchPublicTaskLoader(
        dataset_root=tmp_path,
        dataset_revision=revision,
        expected_zip_sha256={"ahc024": _sha256(snapshot)},
    ).load("ahc024")
    assert all(marker in task for marker in ("PREFIXED_STATEMENT", "PREFIXED_EXAMPLE", "PREFIXED_TOOLS_README"))
    assert "PRIVATE_JUDGE_EVIDENCE" not in task


def test_edge_public_binding_uses_fixed_work_image_public_readmes(tmp_path: Path) -> None:
    task_json = tmp_path / "apple_incremental_game.json"
    payload = {"task_id": "apple_incremental_game", "cwd": "/home/workspace/apple_incremental_game", "submit_paths": ["solution.py"], "work": {"image_tag": "d3c6ed381c59", "specs_dir": "/home/workspace/apple_incremental_game", "agent_query": "Read README.md and tools/README.md"}, "judge": {"image_tag": "16968d8ec7f2", "eval_timeout": 600, "score_direction": "maximize", "private": "PRIVATE_JUDGE_EVIDENCE"}}
    task_json.write_text(json.dumps(payload), encoding="utf-8")
    calls: list[tuple[str, str]] = []

    def read_image_file(image: str, path: str) -> tuple[str, str]:
        calls.append((image, path))
        return ({"/home/workspace/apple_incremental_game/README.md": "FULL_EDGE_README", "/home/workspace/apple_incremental_game/tools/README.md": "EDGE_TOOLS_README"}[path], "sha256:" + "a" * 64)

    task = EdgeBenchPublicTaskLoader(dataset_root=tmp_path, expected_task_json_sha256={"apple_incremental_game": _sha256(task_json)}, expected_work_image_tags={"apple_incremental_game": "d3c6ed381c59"}, expected_judge_image_tags={"apple_incremental_game": "16968d8ec7f2"}, expected_timeouts={"apple_incremental_game": 600}, image_file_reader=read_image_file).load("apple_incremental_game", submission_path="solution.py")
    image = "seededge/edgebench.work.apple_incremental_game:d3c6ed381c59"
    assert calls == [(image, "/home/workspace/apple_incremental_game/README.md"), (image, "/home/workspace/apple_incremental_game/tools/README.md")]
    assert all(marker in task for marker in ("FULL_EDGE_README", "EDGE_TOOLS_README", image))
    assert "PRIVATE_JUDGE_EVIDENCE" not in task
    assert "Return exactly one JSON object and no Markdown" in task
    assert "```" not in task
    assert '"schema_version": 1' in task
    assert '"files"' in task
    assert '"path": "solution.py"' in task
    assert '"type": "file"' in task
    assert '"content"' in task


def test_cli_loads_the_separate_production_module(monkeypatch: pytest.MonkeyPatch) -> None:
    from scripts import run_moss_experiment_one as cli
    imported: list[str] = []
    sentinel = object()

    def import_module(name: str) -> object:
        imported.append(name)
        return types.SimpleNamespace(build_production_controller=lambda context: sentinel)

    monkeypatch.setattr(cli.importlib, "import_module", import_module)
    assert cli.create_production_controller(object()) is sentinel  # type: ignore[arg-type]
    assert imported == ["optimization_lab.harness_builder.experiment_one_production"]


def test_edge_single_round_executes_solver_evaluator_and_builder_once(tmp_path: Path) -> None:
    h0 = production.task_harness_from_frozen_schema(_frozen_h0())
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(h0)
    candidate = json.dumps(
        {
            "schema_version": 1,
            "files": [
                {"path": "solution.py", "type": "file", "content": "print('PUBLIC_CANDIDATE')\n"}
            ],
        }
    )
    proposal = json.dumps(
        {
            "schema_version": 1,
            "base_sha256": h0.sha256,
            "reason": "make the public-task instruction more explicit",
            "expected_effect": "improve official public score",
            "artifact": {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Solve and verify the supplied public task.\n\n{task}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )
    builder_client = _Client([proposal])
    solver_client = _Client([candidate])
    builder = production.OpenAIResponsesGenerator(client=builder_client, max_output_tokens=4096, reasoning_effort="high")
    solver = production.OpenAIResponsesGenerator(client=solver_client, max_output_tokens=4096, reasoning_effort="high")
    adapter = _EdgeAdapter(tmp_path / "private")
    executor = production.EdgeLineageRoundExecutor(
        builder_generator=builder,
        solver_generator=solver,
        adapter=adapter,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
    )
    config = _configuration()
    target = TargetBinding("A", "apple_incremental_game", "FULL PUBLIC TASK", "solution.py", "e" * 64)
    result = executor(
        LineageRoundRequest(
            manifest_sha256="a" * 64,
            benchmark="edgebench",
            seed_id="S1",
            position="A",
            round_index=1,
            operation_id="S1-A-round-01",
            lineage_root=tmp_path,
            workspace=workspace,
            target=target,
            builder_model_configuration=config,
            solver_model_configuration=config,
        )
    )

    assert len(solver_client.responses.calls) == 1
    assert len(adapter.calls) == 1
    assert len(builder_client.responses.calls) == 1
    assert result.evaluated_harness_sha256 == h0.sha256
    assert result.next_harness_sha256 == workspace.current().sha256
    assert workspace.current().version == 2
    assert result.official_score == 12.5
    assert result.official_score_valid is True
    receipt_path = tmp_path / "evaluator_receipts" / "S1-A-round-01.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert receipt == {
        "schema_version": 1,
        "operation_id": "S1-A-round-01",
        "task_id": "apple_incremental_game",
        "target_binding_sha256": target.sha256,
        "candidate_sha256": result.candidate_sha256,
        "official_score": 12.5,
        "official_score_valid": True,
        "public_feedback": "official public feedback",
        "private_evidence_sha256": result.private_evidence_sha256,
        "evaluator_contract_sha256": "e" * 64,
        "evaluator_call_count": 1,
    }
    assert result.evaluator_receipt_sha256 == _sha256(receipt_path)
    assert "PUBLIC_CANDIDATE" not in str(builder_client.responses.calls[0]["input"])
    solver_prompt = str(solver_client.responses.calls[0]["input"])
    assert "AUTHORITATIVE OUTPUT CONTRACT" in solver_prompt
    assert "one complete JSON object and no prose" in solver_prompt
    assert "solution.py" in solver_prompt


def test_two_solver_nodes_receive_distinct_audit_operation_ids(tmp_path: Path) -> None:
    h0 = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "draft",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Draft a solution for {task}",
                    },
                    {
                        "id": "repair",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Repair {latest_output}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(h0)
    candidate = json.dumps(
        {
            "schema_version": 1,
            "files": [
                {"path": "solution.py", "type": "file", "content": "print('PUBLIC_CANDIDATE')\n"}
            ],
        }
    )
    proposal = json.dumps(
        {
            "schema_version": 1,
            "base_sha256": h0.sha256,
            "reason": "retain the two-stage public solver",
            "expected_effect": "preserve public score",
            "artifact": h0.spec.to_dict(),
        }
    )
    config = _configuration()
    target = TargetBinding(
        "B", "apple_incremental_game", "FULL PUBLIC TASK", "solution.py", "e" * 64
    )
    request = LineageRoundRequest(
        "a" * 64,
        "edgebench",
        "S1",
        "B",
        2,
        "S1-B-round-02",
        tmp_path,
        workspace,
        target,
        config,
        config,
    )
    solver_client = _Client(["draft response", candidate])
    first = production.EdgeLineageRoundExecutor(
        builder_generator=production.OpenAIResponsesGenerator(
            client=_Client([proposal]),
            max_output_tokens=4096,
            reasoning_effort="high",
        ),
        solver_generator=production.OpenAIResponsesGenerator(
            client=solver_client,
            max_output_tokens=4096,
            reasoning_effort="high",
        ),
        adapter=_EdgeAdapter(tmp_path / "private"),
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
    )(request)

    events = [
        json.loads(line)
        for line in (tmp_path / "audit" / "solver_model_calls.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]
    operation_ids = [
        event["operation_id"] for event in events if event["event"] == "start"
    ]
    assert operation_ids == [
        "S1-B-round-02-solver-draft-0000",
        "S1-B-round-02-solver-repair-0001",
    ]

    replay_builder = _Client([])
    replay_solver = _Client([])
    replay = production.EdgeLineageRoundExecutor(
        builder_generator=production.OpenAIResponsesGenerator(
            client=replay_builder,
            max_output_tokens=4096,
            reasoning_effort="high",
        ),
        solver_generator=production.OpenAIResponsesGenerator(
            client=replay_solver,
            max_output_tokens=4096,
            reasoning_effort="high",
        ),
        adapter=_ForbiddenEdgeAdapter(),
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
    )(request)

    assert replay == first
    assert replay_solver.responses.calls == []
    assert replay_builder.responses.calls == []


def test_schema_two_router_execution_order_binds_audit_ids_to_executed_nodes(
    tmp_path: Path,
) -> None:
    artifact = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "nodes": [
                    {
                        "id": "first",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "First step for {task}",
                    },
                    {
                        "id": "second",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Second step for {task}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
                "interface": {},
                "memory": {},
                "capabilities": {},
                "router": {"execution_order": ["second", "first", "emit"]},
            },
        }
    )
    client = _Client(["second response", "first response"])
    audited = production.AuditedGenerator(
        generator=production.OpenAIResponsesGenerator(
            client=client,
            max_output_tokens=4096,
            reasoning_effort="high",
        ),
        audit_path=tmp_path / "solver_model_calls.jsonl",
        operation_id_factory=production.ScopedOperationIdFactory(
            "S1-B-round-02", "solver"
        ),
        layer="solver",
        reasoning_effort="high",
    )
    target = TargetBinding(
        "B", "apple_incremental_game", "FULL PUBLIC TASK", "solution.py", "e" * 64
    )
    runtime = production._task_runtime_for_target(
        generator=audited,
        benchmark="edgebench",
        target=target,
    )

    run = runtime.run(
        artifact,
        task="FULL PUBLIC TASK",
        model="gpt-5.6-sol",
        tools={},
    )

    events = [
        json.loads(line)
        for line in audited.audit_path.read_text(encoding="utf-8").splitlines()
    ]
    assert [event.node_id for event in run.events] == ["second", "first", "emit"]
    assert [event["operation_id"] for event in events if event["event"] == "start"] == [
        "S1-B-round-02-solver-second-0000",
        "S1-B-round-02-solver-first-0001",
    ]


def test_agent_turns_receive_distinct_formal_solver_audit_ids(tmp_path: Path) -> None:
    artifact = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "{task}"},
                    {"id": "emit", "kind": "emit", "input_key": "solve"},
                ],
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
            },
        }
    )
    client = _Client(
        [
            '{"action":"tool","tool":"inspect","arguments":{"value":"x"}}',
            '{"action":"emit","candidate":"answer"}',
        ]
    )
    audited = production.AuditedGenerator(
        generator=production.OpenAIResponsesGenerator(
            client=client,
            max_output_tokens=4096,
            reasoning_effort="high",
        ),
        audit_path=tmp_path / "solver_model_calls.jsonl",
        operation_id_factory=production.ScopedOperationIdFactory(
            "S1-B-round-02", "solver"
        ),
        layer="solver",
        reasoning_effort="high",
    )
    target = TargetBinding(
        "B", "apple_incremental_game", "FULL PUBLIC TASK", "solution.py", "e" * 64
    )
    runtime = production._task_runtime_for_target(
        generator=audited,
        benchmark="edgebench",
        target=target,
    )
    registry = ToolRegistry(
        tmp_path / "tools",
        {"inspect": BoundTool.callable(lambda arguments: {"ok": arguments["value"] == "x"})},
    )

    run = runtime.run(
        artifact,
        task="FULL PUBLIC TASK",
        model="gpt-5.6-sol",
        tools={},
        tool_registry=registry,
        tool_workspace=tmp_path / "tools" / "workspace",
        operation_scope="S1-B-round-02",
    )

    events = [
        json.loads(line)
        for line in audited.audit_path.read_text(encoding="utf-8").splitlines()
    ]
    assert run.model_call_scopes == ("solve.agent.0000", "solve.agent.0001")
    assert [event["operation_id"] for event in events if event["event"] == "start"] == [
        "S1-B-round-02-solver-solve.agent.0000-0000",
        "S1-B-round-02-solver-solve.agent.0001-0001",
    ]


def test_ale_single_round_executes_solver_public_evaluator_and_builder_once(tmp_path: Path) -> None:
    h0 = production.task_harness_from_frozen_schema(_frozen_h0())
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(h0)
    candidate = "```cpp23\n#include <iostream>\nint main() { std::cout << 1; }\n```\n"
    proposal = json.dumps(
        {
            "schema_version": 1,
            "base_sha256": h0.sha256,
            "reason": "make the public-task instruction more explicit",
            "expected_effect": "improve official ALE public score",
            "artifact": {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Solve and verify the supplied public ALE task.\n\n{task}",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )
    builder_client = _Client([proposal])
    solver_client = _Client([candidate])
    adapter = _ALEAdapter(tmp_path / "private")
    executor = production.ALELineageRoundExecutor(
        builder_generator=production.OpenAIResponsesGenerator(
            client=builder_client, max_output_tokens=4096, reasoning_effort="high"
        ),
        solver_generator=production.OpenAIResponsesGenerator(
            client=solver_client, max_output_tokens=4096, reasoning_effort="high"
        ),
        adapter=adapter,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
    )
    config = _configuration()
    target = TargetBinding("A", "ahc024", "FULL PUBLIC ALE TASK", "main.cpp", "f" * 64)
    result = executor(
        LineageRoundRequest(
            manifest_sha256="b" * 64,
            benchmark="alebench",
            seed_id="S1",
            position="A",
            round_index=1,
            operation_id="S1-A-round-01",
            lineage_root=tmp_path,
            workspace=workspace,
            target=target,
            builder_model_configuration=config,
            solver_model_configuration=config,
        )
    )

    assert len(solver_client.responses.calls) == 1
    assert len(adapter.calls) == 1
    artifact, operation_id = adapter.calls[0]
    assert getattr(artifact, "artifact_kind") == "alebench_source_cpp23"
    assert operation_id == "S1-A-round-01"
    assert len(builder_client.responses.calls) == 1
    assert result.evaluated_harness_sha256 == h0.sha256
    assert result.next_harness_sha256 == workspace.current().sha256
    assert result.official_score == 321.0
    receipt_path = tmp_path / "evaluator_receipts" / "S1-A-round-01.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert receipt["candidate_sha256"] == result.candidate_sha256
    assert receipt["official_score"] == 321.0
    assert receipt["evaluator_contract_sha256"] == "f" * 64
    assert receipt["evaluator_call_count"] == 1
    assert "int main" not in str(builder_client.responses.calls[0]["input"])
    solver_prompt = str(solver_client.responses.calls[0]["input"])
    assert "AUTHORITATIVE OUTPUT CONTRACT" in solver_prompt
    assert "one complete fenced source file and no prose" in solver_prompt
    assert "```<supported language label>" in solver_prompt


def test_production_task_runtime_uses_the_same_bound_contract_for_every_phase() -> None:
    generator = object()
    edge_target = TargetBinding(
        "A", "apple_incremental_game", "PUBLIC", "solution.py", "e" * 64
    )
    ale_target = TargetBinding("A", "ahc024", "PUBLIC", "main.cpp", "f" * 64)

    edge_evolution = production._task_runtime_for_target(
        generator=generator, benchmark="edgebench", target=edge_target
    )
    edge_cross = production._task_runtime_for_target(
        generator=generator, benchmark="edgebench", target=edge_target
    )
    ale_evolution = production._task_runtime_for_target(
        generator=generator, benchmark="alebench", target=ale_target
    )
    ale_cross = production._task_runtime_for_target(
        generator=generator, benchmark="alebench", target=ale_target
    )

    assert edge_evolution.output_contract_sha256 == edge_cross.output_contract_sha256
    assert ale_evolution.output_contract_sha256 == ale_cross.output_contract_sha256
    assert edge_evolution.output_contract["artifact_kind"] == "edgebench_file_bundle_v1"
    assert ale_evolution.output_contract["artifact_kind"] == "alebench_source_file"


def test_production_probe_rejects_agent_capability_outside_public_tool_pack(
    tmp_path: Path,
) -> None:
    candidate = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": ["private_eval"],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 4,
                        "max_tool_calls": 2,
                        "workflows": [],
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
    pack = build_experiment_one_tool_pack(
        benchmark="edgebench",
        target=SimpleNamespace(task_id="public", submission_path="solution.py"),
        root=tmp_path / "tools",
    )
    assert production.production_harness_probe(
        candidate,
        allowed_tools={name: lambda _value: None for name in pack.allowed_tool_ids},
        tool_registry=pack.registry,
    ) is False


def test_production_probe_requires_runtime_binding_for_v2_agent(
    tmp_path: Path,
) -> None:
    candidate = TaskHarnessArtifact.from_dict(
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
                        "max_turns": 4,
                        "max_tool_calls": 2,
                        "workflows": [],
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
    registry = ToolRegistry(
        tmp_path / "registry",
        {"inspect": BoundTool.callable(lambda _: {"ok": True})},
    )
    allowed = {"inspect": lambda _value: None}
    assert production.production_harness_probe(
        candidate, allowed_tools=allowed, tool_registry=registry
    ) is False
    assert production.production_harness_probe(
        candidate,
        allowed_tools=allowed,
        tool_registry=registry,
        tool_workspace=tmp_path / "workspace",
        operation_scope="round-solver",
    ) is True


def test_production_probe_rejects_duplicate_agent_workflows(
    tmp_path: Path,
) -> None:
    candidate = TaskHarnessArtifact.from_dict(
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
                        "max_turns": 4,
                        "max_tool_calls": 2,
                        "workflows": [
                            "diagnose_generate_verify",
                            "diagnose_generate_verify",
                        ],
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
    registry = ToolRegistry(
        tmp_path / "registry",
        {"inspect": BoundTool.callable(lambda _: {"ok": True})},
    )

    assert production.production_harness_probe(
        candidate,
        allowed_tools={"inspect": lambda _value: None},
        tool_registry=registry,
        tool_workspace=tmp_path / "workspace",
        operation_scope="round-solver",
    ) is False


def test_edge_round_runtime_receives_public_legacy_tools(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    h0 = production.task_harness_from_frozen_schema(_frozen_h0())
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(h0)
    (tmp_path / "audit").mkdir(parents=True, exist_ok=True)
    (tmp_path / "audit" / "builder_model_calls.jsonl").write_text("", encoding="utf-8")
    (tmp_path / "audit" / "solver_model_calls.jsonl").write_text("", encoding="utf-8")

    candidate = json.dumps(
        {
            "schema_version": 1,
            "files": [
                {"path": "solution.py", "type": "file", "content": "print('candidate')\n"}
            ],
        }
    )
    seen: dict[str, object] = {}

    class _CapturingRuntime:
        def __init__(self, **kwargs: object) -> None:
            pass

        def run_round(self, **kwargs: object) -> SimpleNamespace:
            tools = kwargs["tools"]
            assert isinstance(tools, dict)
            seen["tools"] = tools
            assert CONTRACT_CHECK_TOOL_ID in tools
            assert tools[CONTRACT_CHECK_TOOL_ID]({"candidate": candidate})["valid"] is True
            evaluation = kwargs["evaluator"](candidate)
            assert isinstance(evaluation, EvaluationResult)
            return SimpleNamespace(
                harness_sha256=h0.sha256,
                next_harness_sha256=h0.sha256,
            )

    monkeypatch.setattr(production, "DualHarnessRuntime", _CapturingRuntime)
    adapter = _EdgeAdapter(tmp_path / "private")
    executor = production.EdgeLineageRoundExecutor(
        builder_generator=production.OpenAIResponsesGenerator(
            client=_Client([]), max_output_tokens=4096, reasoning_effort="high"
        ),
        solver_generator=production.OpenAIResponsesGenerator(
            client=_Client([]), max_output_tokens=4096, reasoning_effort="high"
        ),
        adapter=adapter,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
        tool_pack_factory=lambda target, root: build_experiment_one_tool_pack(
            benchmark="edgebench", target=target, root=root
        ),
    )
    config = _configuration()
    target = TargetBinding(
        "A", "apple_incremental_game", "FULL PUBLIC TASK", "solution.py", "e" * 64
    )
    request = LineageRoundRequest(
        "a" * 64,
        "edgebench",
        "S1",
        "A",
        1,
        "S1-A-round-01",
        tmp_path,
        workspace,
        target,
        config,
        config,
    )

    result = executor(request)

    assert result.official_score == 12.5
    assert set(seen["tools"]) == set(allowed_experiment_one_tool_ids("edgebench"))


def test_round_audit_hash_is_stable_when_later_rounds_append(
    tmp_path: Path,
) -> None:
    executor = object.__new__(production.EdgeLineageRoundExecutor)
    executor.audit_directory = tmp_path / "audit"
    executor.audit_directory.mkdir(parents=True)
    builder_ledger = executor.audit_directory / "builder_model_calls.jsonl"
    solver_ledger = executor.audit_directory / "solver_model_calls.jsonl"
    round_one = json.dumps({"operation_id": "S1-A-round-01-builder-call"})
    round_two = json.dumps({"operation_id": "S1-A-round-02-builder-call"})
    builder_ledger.write_text(round_one + "\n", encoding="utf-8")
    solver_ledger.write_text(round_one + "\n", encoding="utf-8")

    before = executor._audit_ledger_sha256("S1-A-round-01")
    builder_ledger.write_text(round_one + "\n" + round_two + "\n", encoding="utf-8")
    solver_ledger.write_text(round_one + "\n" + round_two + "\n", encoding="utf-8")

    assert executor._audit_ledger_sha256("S1-A-round-01") == before
    assert executor._audit_ledger_sha256("S1-A-round-02") != before


def test_production_probe_rejects_declared_evaluator_tool_even_if_registry_contains_it(
    tmp_path: Path,
) -> None:
    candidate = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": ["private_eval"],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 4,
                        "max_tool_calls": 2,
                        "workflows": [],
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
    registry = ToolRegistry(tmp_path / "registry", {"private_eval": lambda _: {"score": 1}})
    assert production.production_harness_probe(
        candidate,
        allowed_tools={"private_eval": lambda _value: None},
        tool_registry=registry,
    ) is False


def test_agent_contract_explains_action_wrapper_vs_final_candidate() -> None:
    h0 = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 2,
                "interface": {},
                "memory": {},
                "capabilities": {
                    "tools": [CONTRACT_CHECK_TOOL_ID],
                    "skills": [],
                    "agent": {
                        "node_id": "solve",
                        "max_turns": 4,
                        "max_tool_calls": 2,
                        "workflows": [],
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
    assert "action JSON" in TaskHarnessRuntime._output_contract_block(
        {"artifact_kind": "edgebench_file_bundle_v1"}, "c" * 64
    )


def test_cross_test_solver_call_count_uses_actual_agent_model_turns() -> None:
    run = production.TaskHarnessRun(
        harness_sha256="a" * 64,
        candidate="candidate",
        events=(),
        model_call_scopes=("solve.agent.0000", "solve.agent.0001"),
    )

    assert production._solver_call_count(run) == 2


def test_edge_round_rolls_back_builder_proposal_with_unapproved_tool(tmp_path: Path) -> None:
    h0 = production.task_harness_from_frozen_schema(_frozen_h0())
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(h0)
    candidate = json.dumps(
        {
            "schema_version": 1,
            "files": [
                {"path": "solution.py", "type": "file", "content": "print('candidate')\n"}
            ],
        }
    )
    unsafe_proposal = json.dumps(
        {
            "schema_version": 1,
            "base_sha256": h0.sha256,
            "reason": "try an unavailable helper",
            "expected_effect": "should be rejected by the production probe",
            "artifact": {
                "schema_version": 1,
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "Solve {task}"},
                    {"id": "unsafe", "kind": "tool_call", "tool": "private_shell", "input_key": "latest_output"},
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )
    builder_client = _Client([unsafe_proposal])
    solver_client = _Client([candidate])
    adapter = _EdgeAdapter(tmp_path / "private")
    executor = production.EdgeLineageRoundExecutor(
        builder_generator=production.OpenAIResponsesGenerator(client=builder_client, max_output_tokens=4096, reasoning_effort="high"),
        solver_generator=production.OpenAIResponsesGenerator(client=solver_client, max_output_tokens=4096, reasoning_effort="high"),
        adapter=adapter,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
    )
    config = _configuration()
    target = TargetBinding("A", "apple_incremental_game", "FULL PUBLIC TASK", "solution.py", "e" * 64)
    request = LineageRoundRequest("a" * 64, "edgebench", "S1", "A", 1, "S1-A-round-01", tmp_path, workspace, target, config, config)

    result = executor(request)

    assert len(adapter.calls) == 1
    assert len(builder_client.responses.calls) == 1
    assert workspace.current().sha256 == h0.sha256
    assert result.next_harness_sha256 == h0.sha256
    builder_trace = workspace.load_builder_trace("S1-A-round-01")
    assert builder_trace is not None
    assert builder_trace["status"] == "rolled_back"


def test_edge_evaluator_exception_never_calls_builder_or_forges_score(tmp_path: Path) -> None:
    h0 = production.task_harness_from_frozen_schema(_frozen_h0())
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(h0)
    candidate = json.dumps(
        {
            "schema_version": 1,
            "files": [
                {"path": "solution.py", "type": "file", "content": "print('candidate')\n"}
            ],
        }
    )
    builder_client = _Client(["must not be consumed"])
    solver_client = _Client([candidate])
    adapter = _RaisingEdgeAdapter()
    executor = production.EdgeLineageRoundExecutor(
        builder_generator=production.OpenAIResponsesGenerator(client=builder_client, max_output_tokens=4096, reasoning_effort="high"),
        solver_generator=production.OpenAIResponsesGenerator(client=solver_client, max_output_tokens=4096, reasoning_effort="high"),
        adapter=adapter,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
    )
    config = _configuration()
    target = TargetBinding("A", "apple_incremental_game", "FULL PUBLIC TASK", "solution.py", "e" * 64)
    request = LineageRoundRequest("a" * 64, "edgebench", "S1", "A", 1, "S1-A-round-01", tmp_path, workspace, target, config, config)

    with pytest.raises(RuntimeError, match="official evaluator unavailable"):
        executor(request)

    assert adapter.calls == 1
    assert len(solver_client.responses.calls) == 1
    assert builder_client.responses.calls == []
    assert workspace.current().sha256 == h0.sha256
    assert workspace.load_trace("S1-A-round-01", missing_ok=True) is None
    assert workspace.load_builder_trace("S1-A-round-01", missing_ok=True) is None
    assert not (tmp_path / "evaluator_receipts" / "S1-A-round-01.json").exists()


def test_edge_round_replay_uses_durable_receipt_and_audit_without_external_calls(tmp_path: Path) -> None:
    h0 = production.task_harness_from_frozen_schema(_frozen_h0())
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(h0)
    candidate = json.dumps(
        {
            "schema_version": 1,
            "files": [
                {"path": "solution.py", "type": "file", "content": "print('candidate')\n"}
            ],
        }
    )
    proposal = json.dumps(
        {
            "schema_version": 1,
            "base_sha256": h0.sha256,
            "reason": "clarify public task",
            "expected_effect": "improve public score",
            "artifact": {
                "schema_version": 1,
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "Carefully solve {task}"},
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )
    config = _configuration()
    target = TargetBinding("A", "apple_incremental_game", "FULL PUBLIC TASK", "solution.py", "e" * 64)
    request = LineageRoundRequest("a" * 64, "edgebench", "S1", "A", 1, "S1-A-round-01", tmp_path, workspace, target, config, config)
    first_adapter = _EdgeAdapter(tmp_path / "private")
    first = production.EdgeLineageRoundExecutor(
        builder_generator=production.OpenAIResponsesGenerator(client=_Client([proposal]), max_output_tokens=4096, reasoning_effort="high"),
        solver_generator=production.OpenAIResponsesGenerator(client=_Client([candidate]), max_output_tokens=4096, reasoning_effort="high"),
        adapter=first_adapter,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
    )(request)

    replay_builder = _Client([])
    replay_solver = _Client([])
    replay_adapter = _ForbiddenEdgeAdapter()
    replay = production.EdgeLineageRoundExecutor(
        builder_generator=production.OpenAIResponsesGenerator(client=replay_builder, max_output_tokens=4096, reasoning_effort="high"),
        solver_generator=production.OpenAIResponsesGenerator(client=replay_solver, max_output_tokens=4096, reasoning_effort="high"),
        adapter=replay_adapter,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        audit_directory=tmp_path / "audit",
        evaluator_receipt_directory=tmp_path / "evaluator_receipts",
        allowed_tools={},
    )(request)

    assert replay == first
    assert replay_solver.responses.calls == []
    assert replay_builder.responses.calls == []
    assert replay_adapter.calls == 0
    assert len(first_adapter.calls) == 1


def test_frozen_h0_conversion_and_production_probe_enforce_model_and_tool_requirements() -> None:
    h0 = production.task_harness_from_frozen_schema(_frozen_h0())
    assert [node["id"] for node in h0.spec.to_dict()["nodes"]] == ["solve", "emit"]
    assert all("node_id" not in node for node in h0.spec.to_dict()["nodes"])
    assert production.production_harness_probe(h0, allowed_tools={}) is True

    with_tool = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 2,
            "parent_sha256": h0.sha256,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "Solve {task}"},
                    {"id": "check", "kind": "tool_call", "tool": "public_checker", "input_key": "latest_output"},
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )
    assert production.production_harness_probe(with_tool, allowed_tools={}) is False
    assert production.production_harness_probe(with_tool, allowed_tools={"public_checker": lambda value: value}) is True

    two_models = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 2,
            "parent_sha256": h0.sha256,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {"id": "draft", "kind": "model_call", "role": "solver", "prompt": "Draft {task}"},
                    {"id": "solve", "kind": "model_call", "role": "solver", "prompt": "Revise {latest_output}"},
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )
    assert production.production_harness_probe(two_models, allowed_tools={}) is True

    emit_only = TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 2,
            "parent_sha256": h0.sha256,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )
    assert production.production_harness_probe(emit_only, allowed_tools={}) is False

    duplicate_identity = _frozen_h0()
    duplicate_identity["spec"]["nodes"][0]["id"] = "also-solve"  # type: ignore[index]
    with pytest.raises(ValueError, match="node identity"):
        production.task_harness_from_frozen_schema(duplicate_identity)
