from __future__ import annotations

import hashlib
import json
import os
import posixpath
import re
import subprocess
import zipfile
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Callable, Mapping

from optimization_lab.openai_generator import OpenAIResponsesGenerator

from .dual_harness import TaskHarnessArtifact, TaskHarnessRun, TaskHarnessRuntime
from .dual_runtime import DualHarnessRuntime, EvaluationResult
from .experiment_one import (
    CallLedgerEvidence,
    CrossMatrixRunner,
    EvaluationRequest,
    ExperimentOneManifest,
    FreezeReceipt,
    HarnessTransferProvenance,
    LineageRoundRequest,
    LineageRoundResult,
    LineageRunner,
    ModelConfiguration,
    OfficialEvaluationResult,
    TaskExecutionRequest,
    TaskExecutionResult,
    TargetBinding,
    _load_once,
)
from .adapters.edgebench_official import (
    EDGE_BENCH_DATASET_REVISION,
    EDGE_BENCH_SOURCE_COMMIT,
    EdgeBenchContract,
    EdgeBenchOfficialAdapter,
)
from .adapters.alebench_official import (
    ALE_BENCH_DATASET_REVISION,
    ALE_BENCH_SOURCE_COMMIT,
    ALEBenchContract,
    ALEBenchOfficialAdapter,
    _ALE_TASK_LIMITS,
    _ALE_TASK_ZIP_SHA256,
    _DOCKER_IMAGE_DIGEST as _ALE_DOCKER_IMAGE_DIGEST,
    _DOCKER_IMAGE_REFERENCE as _ALE_DOCKER_IMAGE_REFERENCE,
    _JUDGE_VERSION as _ALE_JUDGE_VERSION,
    _PRIVATE_EVALUATOR_COMMAND as _ALE_PRIVATE_EVALUATOR_COMMAND,
    _PUBLIC_EVALUATOR_COMMAND as _ALE_PUBLIC_EVALUATOR_COMMAND,
)
from .experiment_one_audit import (
    AuditedGenerator,
    ScopedOperationIdFactory,
    assemble_experiment_one,
)
from .builder_memory import BuilderMemoryConfig
from .contract_compatibility import codec_capability_payload
from .official_solutions import ALEBenchCodeCodec, EdgeBenchBundleCodec, OfficialSolutionArchive
from .solutions import SolutionArtifact
from .experiment_one_tools import (
    FORBIDDEN_EVALUATOR_TOOL_IDS,
    ExperimentOneToolPack,
    build_experiment_one_tool_pack,
)
from .tool_registry import ToolRegistry
from .workflows import WorkflowRegistry

_SAFE_TASK_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_SHA256 = re.compile(r"[0-9a-f]{64}")

_EDGE_WORK_IMAGE_TAGS = {
    "apple_incremental_game": "d3c6ed381c59",
    "molecular_self_assembly": "6459dea01a82",
    "treant_forest": "e05dfd5d2463",
}
_EDGE_JUDGE_IMAGE_TAGS = {
    "apple_incremental_game": "16968d8ec7f2",
    "molecular_self_assembly": "96df6463f5e6",
    "treant_forest": "d47dc1a7da74",
}
_EDGE_JUDGE_IMAGE_REFERENCES = {
    "apple_incremental_game": "seededge/edgebench.judge.apple_incremental_game:16968d8ec7f2",
    "molecular_self_assembly": "seededge/edgebench.judge.molecular_self_assembly:96df6463f5e6",
    "treant_forest": "seededge/edgebench.judge.treant_forest:d47dc1a7da74",
}
_EDGE_JUDGE_IMAGE_DIGESTS = {
    "apple_incremental_game": "sha256:ca50e0754abb5dd1efd8387714206b8958fa7a4902ffadc03abad63139e26051",
    "molecular_self_assembly": "sha256:4aa576558cb93ea2df285440cecc6481ed06fcd0c7ba68745bfbaba876f32478",
    "treant_forest": "sha256:fcf625d92ea20623b9f998c5911de05fe5e32e9a5babbbe58fab6d4b2cdd1434",
}
_EDGE_TIMEOUTS = {
    "apple_incremental_game": 600,
    "molecular_self_assembly": 600,
    "treant_forest": 870,
}


def _canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _solver_call_count(run: TaskHarnessRun) -> int:
    count = len(run.model_call_scopes)
    if count < 1:
        raise ValueError("Task Harness execution recorded no Solver model calls")
    return count


def _write_once(path: Path, content: bytes, *, label: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    try:
        descriptor = os.open(path, flags, 0o600)
    except FileExistsError:
        if path.read_bytes() != content:
            raise ValueError(f"{label} differs from durable evidence")
        return path
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    except Exception:
        path.unlink(missing_ok=True)
        raise
    return path


def task_harness_from_frozen_schema(payload: Mapping[str, object]) -> TaskHarnessArtifact:
    """Mechanically translate manifest node_id fields into runtime id fields."""
    copied = json.loads(json.dumps(payload, ensure_ascii=False, allow_nan=False))
    spec = copied.get("spec")
    nodes = spec.get("nodes") if isinstance(spec, dict) else None
    if not isinstance(nodes, list):
        raise ValueError("frozen Harness nodes are invalid")
    for node in nodes:
        if not isinstance(node, dict):
            raise ValueError("frozen Harness node identity is invalid")
        if "node_id" in node and "id" in node:
            raise ValueError("frozen Harness node identity is invalid")
        if "node_id" in node and "id" not in node:
            node["id"] = node.pop("node_id")
        elif "id" not in node:
            raise ValueError("frozen Harness node identity is invalid")
    return TaskHarnessArtifact.from_dict(copied)


def production_harness_probe(
    artifact: TaskHarnessArtifact,
    *,
    allowed_tools: Mapping[str, Callable[[Any], Any]],
    tool_registry: ToolRegistry | None = None,
    tool_workspace: str | os.PathLike[str] | None = None,
    operation_scope: str | None = None,
) -> bool:
    """Apply the production-safe structural gate to a proposed Task Harness.

    The probe deliberately checks only public, execution-relevant structure.
    It never evaluates a candidate.  V1 artifacts retain their historical
    compatibility; V2 Agent capabilities additionally have to match the
    supplied public tool registry and fixed workflow catalog.
    """

    nodes = artifact.spec.nodes
    if not nodes or not any(node.kind == "model_call" for node in nodes):
        return False
    if nodes[-1].kind != "emit":
        return False

    declared_tools: set[str] | None = None
    if artifact.spec.schema_version == 2:
        raw_capabilities = artifact.spec.capabilities
        raw_tools = raw_capabilities.get("tools", [])
        if not isinstance(raw_tools, list) or any(
            not isinstance(tool, str) or not _SAFE_TASK_ID.fullmatch(tool)
            for tool in raw_tools
        ):
            return False
        declared_tools = set(raw_tools)
        # The evaluator is deliberately outside the Task Harness Agent loop.
        # Keep this invariant here as a second line of defense even when a
        # caller accidentally supplies an unsafe registry or allowed-tools
        # mapping.
        if declared_tools & FORBIDDEN_EVALUATOR_TOOL_IDS:
            return False
        if not declared_tools.issubset(set(allowed_tools)):
            return False
        if tool_registry is not None and not declared_tools.issubset(
            set(tool_registry.definitions)
        ):
            return False

        raw_agent = raw_capabilities.get("agent")
        if raw_agent is not None:
            if not isinstance(raw_agent, Mapping):
                return False
            if set(raw_agent) != {"node_id", "max_turns", "max_tool_calls", "workflows"}:
                return False
            if tool_registry is None:
                return False
            node_id = raw_agent.get("node_id")
            matching = [node for node in nodes if node.node_id == node_id]
            if len(matching) != 1 or matching[0].kind != "model_call":
                return False
            if tool_workspace is None or operation_scope is None:
                return False
            for key in ("max_turns", "max_tool_calls"):
                value = raw_agent.get(key)
                if (
                    not isinstance(value, int)
                    or isinstance(value, bool)
                    or value < 1
                    or value > 128
                ):
                    return False
            workflows = raw_agent.get("workflows")
            if not isinstance(workflows, list) or any(
                not isinstance(workflow, str) or not _SAFE_TASK_ID.fullmatch(workflow)
                for workflow in workflows
            ):
                return False
            if len(set(workflows)) != len(workflows):
                return False
            registry = WorkflowRegistry.standard()
            try:
                for workflow in workflows:
                    registry.require(workflow)
            except (KeyError, ValueError):
                return False

    for node in nodes:
        if node.kind == "tool_call":
            if artifact.spec.schema_version == 2:
                if tool_registry is None or tool_workspace is None or operation_scope is None:
                    return False
            if node.tool not in allowed_tools:
                return False
            if declared_tools is not None and node.tool not in declared_tools:
                return False
    return True


class _NodeScopedGenerator:
    def __init__(self, generator: AuditedGenerator) -> None:
        self.generator = generator
        self.scopes: list[str] = []

    def generate(self, prompt: str, *, model: str) -> Any:
        return self.generate_scoped(prompt, model=model, scope="call")

    def generate_scoped(self, prompt: str, *, model: str, scope: str) -> Any:
        self.scopes.append(scope)
        return self.generator.generate(prompt, model=model, scope=scope)


class _NodeScopedTaskHarnessRuntime(TaskHarnessRuntime):
    def run(
        self,
        artifact: TaskHarnessArtifact,
        *,
        task: str,
        model: str,
        tools: Mapping[str, Callable[[Any], Any]],
        initial_state: Mapping[str, Any] | None = None,
        tool_registry: Any | None = None,
        tool_workspace: str | os.PathLike[str] | None = None,
        operation_scope: str | None = None,
    ) -> TaskHarnessRun:
        if not isinstance(self.generator, AuditedGenerator):
            return super().run(
                artifact,
                task=task,
                model=model,
                tools=tools,
                initial_state=initial_state,
                tool_registry=tool_registry,
                tool_workspace=tool_workspace,
                operation_scope=operation_scope,
            )
        scoped_generator = _NodeScopedGenerator(self.generator)
        runtime = TaskHarnessRuntime(
            generator=scoped_generator,
            output_contract=self.output_contract,
        )
        result = runtime.run(
            artifact,
            task=task,
            model=model,
            tools=tools,
            initial_state=initial_state,
            tool_registry=tool_registry,
            tool_workspace=tool_workspace,
            operation_scope=operation_scope,
        )
        if result.model_call_scopes != tuple(scoped_generator.scopes):
            raise RuntimeError("Solver audit operation scopes do not match execution trace")
        return result


def _task_runtime_for_target(
    *,
    generator: Any,
    benchmark: str,
    target: TargetBinding,
) -> TaskHarnessRuntime:
    """Bind one public benchmark output contract to every Solver execution phase."""

    normalized = re.sub(r"[^a-z0-9]", "", benchmark.lower())
    if normalized == "edgebench":
        codec: object = EdgeBenchBundleCodec(
            required_submit_path=target.submission_path
        )
    elif normalized == "alebench":
        if target.submission_path != "main.cpp":
            raise ValueError("ALE-Bench submission path must be main.cpp")
        codec = ALEBenchCodeCodec()
    else:
        raise ValueError("Experiment One benchmark contract is unsupported")
    return _NodeScopedTaskHarnessRuntime(
        generator=generator,
        output_contract=codec_capability_payload(codec),
    )


class EdgeLineageRoundExecutor:
    """Execute one durable official-evaluator lineage round through the shared runtime."""

    benchmark_label = "Edge"

    def __init__(
        self,
        *,
        builder_generator: OpenAIResponsesGenerator,
        solver_generator: OpenAIResponsesGenerator,
        adapter: object,
        solution_archive: OfficialSolutionArchive,
        audit_directory: Path,
        evaluator_receipt_directory: Path,
        allowed_tools: Mapping[str, Callable[[Any], Any]],
        tool_pack_factory: Callable[[TargetBinding, Path], ExperimentOneToolPack]
        | None = None,
        builder_memory_config: BuilderMemoryConfig | None = None,
    ) -> None:
        self.builder_generator = builder_generator
        self.solver_generator = solver_generator
        self.adapter = adapter
        self.solution_archive = solution_archive
        self.audit_directory = Path(audit_directory).resolve()
        self.evaluator_receipt_directory = Path(evaluator_receipt_directory).resolve()
        self.allowed_tools = dict(allowed_tools)
        self.tool_pack_factory = tool_pack_factory
        self.builder_memory_config = builder_memory_config or BuilderMemoryConfig()
        if not isinstance(self.builder_memory_config, BuilderMemoryConfig):
            raise TypeError("Builder memory config must be a BuilderMemoryConfig")

    def __call__(self, request: LineageRoundRequest) -> LineageRoundResult:
        assembly = assemble_experiment_one(
            workspace=request.workspace,
            builder_generator=self.builder_generator,
            solver_generator=self.solver_generator,
            builder_model=request.builder_model_configuration.model,
            audit_directory=self.audit_directory,
            builder_operation_id_factory=ScopedOperationIdFactory(
                request.operation_id, "builder"
            ),
            solver_operation_id_factory=ScopedOperationIdFactory(
                request.operation_id, "solver"
            ),
            builder_reasoning_effort=request.builder_model_configuration.reasoning_effort,
            solver_reasoning_effort=request.solver_model_configuration.reasoning_effort,
            builder_memory_config=self.builder_memory_config,
        )
        runtime = DualHarnessRuntime(
            workspace=request.workspace,
            task_runtime=_task_runtime_for_target(
                generator=assembly.solver_generator,
                benchmark=request.benchmark,
                target=request.target,
            ),
            builder=assembly.builder,
            solver_model=request.solver_model_configuration.model,
        )

        def evaluate(raw_candidate: str) -> EvaluationResult:
            artifact = self._parse_candidate(raw_candidate, request)
            self.solution_archive.store(artifact)
            result = self._evaluate_official(artifact, operation_id=request.operation_id)
            if not isinstance(result, EvaluationResult):
                raise TypeError(
                    f"{self.benchmark_label} official adapter must return EvaluationResult"
                )
            private = result.private
            if not isinstance(private, Mapping):
                raise ValueError("Edge official private evidence binding is invalid")
            private_sha = private.get("evidence_sha256")
            if not isinstance(private_sha, str) or _SHA256.fullmatch(private_sha) is None:
                raise ValueError("Edge official private evidence hash is invalid")
            valid = self._official_validity(private, result)
            receipt = {
                "schema_version": 1,
                "operation_id": request.operation_id,
                "task_id": request.target.task_id,
                "target_binding_sha256": request.target.sha256,
                "candidate_sha256": artifact.sha256,
                "official_score": result.public.score,
                "official_score_valid": valid,
                "public_feedback": result.public.feedback,
                "private_evidence_sha256": private_sha,
                "evaluator_contract_sha256": request.target.evaluator_contract_sha256,
                "evaluator_call_count": 1,
            }
            _write_once(
                self._receipt_path(request.operation_id),
                _canonical_bytes(receipt),
                label=f"{self.benchmark_label} evaluator receipt",
            )
            return result

        tool_pack = None
        if self.tool_pack_factory is not None:
            tool_pack = self.tool_pack_factory(
                request.target,
                Path(request.lineage_root) / "tools" / request.operation_id,
            )
        runtime_tools = (
            tool_pack.legacy_operations(request.operation_id)
            if tool_pack is not None
            else self.allowed_tools
        )
        result = runtime.run_round(
            run_id=request.operation_id,
            execution_contract_sha256=request.target.evaluator_contract_sha256,
            task=request.target.task,
            tools=runtime_tools,
            tool_registry=tool_pack.registry if tool_pack is not None else None,
            tool_workspace=tool_pack.workspace if tool_pack is not None else None,
            evaluator=evaluate,
            probe=lambda artifact: production_harness_probe(
                artifact,
                allowed_tools=(
                    {tool_id: (lambda _value: None) for tool_id in tool_pack.allowed_tool_ids}
                    if tool_pack is not None
                    else self.allowed_tools
                ),
                tool_registry=tool_pack.registry if tool_pack is not None else None,
                tool_workspace=tool_pack.workspace if tool_pack is not None else None,
                operation_scope=f"{request.operation_id}-solver",
            ),
        )
        receipt_path = self._receipt_path(request.operation_id)
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        self._validate_receipt(receipt, request, result.harness_sha256)
        return LineageRoundResult(
            evaluated_harness_sha256=result.harness_sha256,
            next_harness_sha256=result.next_harness_sha256,
            candidate_sha256=receipt["candidate_sha256"],
            official_score=receipt["official_score"],
            official_score_valid=receipt["official_score_valid"],
            public_feedback=receipt["public_feedback"],
            evaluator_receipt_sha256=_sha256_file(receipt_path),
            private_evidence_sha256=receipt["private_evidence_sha256"],
            audit_ledger_sha256=self._audit_ledger_sha256(request.operation_id),
        )

    def _parse_candidate(
        self, raw_candidate: str, request: LineageRoundRequest
    ) -> SolutionArtifact:
        return EdgeBenchBundleCodec(
            required_submit_path=request.target.submission_path
        ).parse(raw_candidate)

    def _evaluate_official(
        self, artifact: SolutionArtifact, *, operation_id: str
    ) -> EvaluationResult:
        return self.adapter.evaluate(artifact, operation_id=operation_id)

    def _receipt_path(self, operation_id: str) -> Path:
        return self.evaluator_receipt_directory / f"{operation_id}.json"

    @staticmethod
    def _official_validity(private: Mapping[str, object], result: EvaluationResult) -> bool:
        direct = private.get("valid")
        if type(direct) is bool:
            return direct
        evidence_path = private.get("evidence_path")
        if isinstance(evidence_path, str):
            payload = json.loads(Path(evidence_path).read_text(encoding="utf-8"))
            report = payload.get("report") if isinstance(payload, dict) else None
            if isinstance(report, dict) and type(report.get("valid")) is bool:
                return report["valid"]
        return result.public.score is not None

    def _validate_receipt(
        self,
        receipt: object,
        request: LineageRoundRequest,
        harness_sha256: str,
    ) -> None:
        if not isinstance(receipt, dict):
            raise ValueError("Edge evaluator receipt is invalid")
        expected = {
            "schema_version",
            "operation_id",
            "task_id",
            "target_binding_sha256",
            "candidate_sha256",
            "official_score",
            "official_score_valid",
            "public_feedback",
            "private_evidence_sha256",
            "evaluator_contract_sha256",
            "evaluator_call_count",
        }
        if set(receipt) != expected:
            raise ValueError("Edge evaluator receipt fields differ")
        if (
            receipt["schema_version"] != 1
            or receipt["operation_id"] != request.operation_id
            or receipt["task_id"] != request.target.task_id
            or receipt["target_binding_sha256"] != request.target.sha256
            or receipt["evaluator_contract_sha256"]
            != request.target.evaluator_contract_sha256
            or receipt["evaluator_call_count"] != 1
            or not isinstance(harness_sha256, str)
        ):
            raise ValueError("Edge evaluator receipt binding differs")
        for field in ("candidate_sha256", "private_evidence_sha256"):
            if not isinstance(receipt[field], str) or _SHA256.fullmatch(receipt[field]) is None:
                raise ValueError("Edge evaluator receipt hash is invalid")
        if type(receipt["official_score_valid"]) is not bool:
            raise ValueError("Edge evaluator receipt validity is invalid")

    def _audit_ledger_sha256(self, operation_id: str | None = None) -> str:
        prefix = None if operation_id is None else f"{operation_id}-"
        evidence = []
        for name in ("builder_model_calls.jsonl", "solver_model_calls.jsonl"):
            path = self.audit_directory / name
            if not path.is_file():
                raise ValueError("model audit ledger is incomplete")
            if operation_id is None:
                digest = _sha256_file(path)
            else:
                selected: list[bytes] = []
                for raw_line in path.read_bytes().splitlines():
                    if not raw_line:
                        continue
                    try:
                        record = json.loads(raw_line.decode("utf-8"))
                    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                        raise ValueError("model audit ledger contains invalid JSON") from exc
                    record_operation_id = (
                        record.get("operation_id") if isinstance(record, dict) else None
                    )
                    if isinstance(record_operation_id, str) and (
                        record_operation_id == operation_id
                        or (prefix is not None and record_operation_id.startswith(prefix))
                    ):
                        selected.append(_canonical_bytes(record))
                digest = hashlib.sha256(
                    b"".join(item + b"\n" for item in selected)
                ).hexdigest()
            evidence.append({"path": name, "sha256": digest})
        return hashlib.sha256(_canonical_bytes(evidence)).hexdigest()


class ALELineageRoundExecutor(EdgeLineageRoundExecutor):
    """Execute one ALE lineage round using only the official public evaluator."""

    benchmark_label = "ALE"

    def _parse_candidate(
        self, raw_candidate: str, request: LineageRoundRequest
    ) -> SolutionArtifact:
        if request.target.submission_path != "main.cpp":
            raise ValueError("ALE-Bench submission path must be main.cpp")
        artifact = ALEBenchCodeCodec().parse(raw_candidate)
        if artifact.artifact_kind != "alebench_source_cpp23":
            raise ValueError("ALE-Bench production candidate must use cpp23")
        return artifact

    def _evaluate_official(
        self, artifact: SolutionArtifact, *, operation_id: str
    ) -> EvaluationResult:
        return self.adapter.evaluate_public(artifact, operation_id=operation_id)


def _require_task_id(task_id: str) -> str:
    if not isinstance(task_id, str) or _SAFE_TASK_ID.fullmatch(task_id) is None:
        raise ValueError("task ID is unsafe")
    return task_id


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_freeze_receipt(path: Path) -> FreezeReceipt:
    """Load a persisted FreezeReceipt through its integrity envelope."""
    payload, _ = _load_once(path, label="FreezeReceipt authorization")
    return FreezeReceipt.from_dict(payload)


def _expected_sha256(mapping: Mapping[str, str], task_id: str, label: str) -> str:
    try:
        value = mapping[task_id]
    except KeyError as exc:
        raise ValueError(f"{label} is not frozen for task") from exc
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"{label} must be a sha256")
    return value


def create_responses_generators(
    *,
    builder_max_output_tokens: int = 16_384,
    solver_max_output_tokens: int = 32_768,
) -> tuple[OpenAIResponsesGenerator, OpenAIResponsesGenerator]:
    """Create the two text-only Responses transports used by Experiment One."""
    try:
        from openai import OpenAI
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("the openai package is required for production execution") from exc
    client = OpenAI(
        api_key=[REDACTED]"LLM_API_KEY"],
        base_url=os.environ["LLM_BASE_URL"],
        max_retries=0,
    )
    effort = os.environ.get("LLM_REASONING_EFFORT", "high")
    return (
        OpenAIResponsesGenerator(
            client=client,
            max_output_tokens=builder_max_output_tokens,
            reasoning_effort=effort,
            max_attempts=1,
            stream=True,
        ),
        OpenAIResponsesGenerator(
            client=client,
            max_output_tokens=solver_max_output_tokens,
            reasoning_effort=effort,
            max_attempts=1,
            stream=True,
        ),
    )


class ALEBenchPublicTaskLoader:
    """Bind a Solver prompt only to public files in one frozen ALE snapshot."""

    def __init__(
        self,
        *,
        dataset_root: Path,
        dataset_revision: str,
        expected_zip_sha256: Mapping[str, str],
    ) -> None:
        self.dataset_root = Path(dataset_root).resolve()
        self.dataset_revision = dataset_revision
        self.expected_zip_sha256 = dict(expected_zip_sha256)

    def load(self, task_id: str) -> str:
        task_id = _require_task_id(task_id)
        archive_path = self.dataset_root / "snapshots" / self.dataset_revision / f"{task_id}.zip"
        expected = _expected_sha256(
            self.expected_zip_sha256, task_id, "ALE snapshot digest"
        )
        try:
            observed = _sha256_file(archive_path)
        except OSError as exc:
            raise RuntimeError("ALE public task snapshot is unavailable") from exc
        if observed != expected:
            raise RuntimeError("ALE public task snapshot digest differs")
        try:
            with zipfile.ZipFile(archive_path) as archive:
                # ALE's published archives are not fully flat: some revisions
                # store files under ``<task_id>/...`` while others store them
                # at the archive root.  Bind both layouts to one logical,
                # public-only namespace without ever accepting path traversal.
                logical_to_raw: dict[str, str] = {}
                for raw_name in archive.namelist():
                    if raw_name.endswith("/"):
                        continue
                    normalized = posixpath.normpath(raw_name)
                    if normalized in {".", ".."} or normalized.startswith("../"):
                        raise RuntimeError("ALE public task archive contains unsafe path")
                    logical_name = normalized
                    prefix = f"{task_id}/"
                    if logical_name.startswith(prefix):
                        logical_name = logical_name[len(prefix):]
                    if logical_name in logical_to_raw and logical_to_raw[logical_name] != raw_name:
                        raise RuntimeError("ALE public task archive contains duplicate logical path")
                    logical_to_raw[logical_name] = raw_name

                selected = ["statement_en.md"]
                selected.extend(sorted(
                    name for name in logical_to_raw
                    if name.startswith("examples/") and name.endswith(".txt")
                ))
                selected.append("tools/README.md")
                if not {"statement_en.md", "tools/README.md"}.issubset(logical_to_raw):
                    raise RuntimeError("ALE public task files are incomplete")
                sections = []
                for logical_name in selected:
                    try:
                        text = archive.read(logical_to_raw[logical_name]).decode("utf-8")
                    except (KeyError, UnicodeError) as exc:
                        raise RuntimeError("ALE public task file is unreadable") from exc
                    sections.append(f"## {logical_name}\n\n{text.strip()}")
        except (OSError, zipfile.BadZipFile) as exc:
            raise RuntimeError("ALE public task snapshot is invalid") from exc
        return (
            f"# ALE-Bench public task: {task_id}\n\n"
            + "\n\n".join(sections)
            + "\n\n"
            "## Required submission format\n\n"
            "Return exactly one fenced source file and nothing else. "
            "Use a `cpp23` fence, with the complete source between the opening "
            "and closing fences:\n\n"
            "```cpp23\n"
            "<complete source code>\n"
            "```\n\n"
            "Do not include Markdown outside the fence. Do not include a second "
            "fence or explanatory text.\n"
        )


ImageFileReader = Callable[[str, str], tuple[str, str]]


def _read_docker_image_file(image: str, path: str) -> tuple[str, str]:
    completed = subprocess.run(
        ("docker", "run", "--rm", "--entrypoint", "cat", image, path),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=120,
    )
    if completed.returncode != 0:
        raise RuntimeError("EdgeBench public file could not be read from work image")
    try:
        content = completed.stdout.decode("utf-8")
    except UnicodeError as exc:
        raise RuntimeError("EdgeBench public file is not UTF-8") from exc
    inspected = subprocess.run(
        ("docker", "image", "inspect", "--format", "{{.Id}}", image),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
        timeout=30,
    )
    if inspected.returncode != 0:
        raise RuntimeError("EdgeBench work image identity is unavailable")
    return content, inspected.stdout.strip()


class EdgeBenchPublicTaskLoader:
    """Bind a Solver prompt to public README files in a frozen Edge work image."""

    def __init__(
        self,
        *,
        dataset_root: Path,
        expected_task_json_sha256: Mapping[str, str],
        expected_work_image_tags: Mapping[str, str],
        expected_judge_image_tags: Mapping[str, str],
        expected_timeouts: Mapping[str, int],
        image_file_reader: ImageFileReader = _read_docker_image_file,
    ) -> None:
        self.dataset_root = Path(dataset_root).resolve()
        self.expected_task_json_sha256 = dict(expected_task_json_sha256)
        self.expected_work_image_tags = dict(expected_work_image_tags)
        self.expected_judge_image_tags = dict(expected_judge_image_tags)
        self.expected_timeouts = dict(expected_timeouts)
        self.image_file_reader = image_file_reader

    def load(self, task_id: str, *, submission_path: str) -> str:
        task_id = _require_task_id(task_id)
        task_path = self.dataset_root / f"{task_id}.json"
        expected_digest = _expected_sha256(
            self.expected_task_json_sha256, task_id, "Edge task JSON digest"
        )
        try:
            if _sha256_file(task_path) != expected_digest:
                raise RuntimeError("Edge task JSON digest differs")
            payload = json.loads(task_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise RuntimeError("Edge task JSON is unavailable or invalid") from exc
        if not isinstance(payload, dict) or payload.get("task_id") != task_id:
            raise RuntimeError("Edge task JSON identity differs")
        work = payload.get("work")
        judge = payload.get("judge")
        submit_paths = payload.get("submit_paths")
        if not isinstance(work, dict) or not isinstance(judge, dict):
            raise RuntimeError("Edge task contract is incomplete")
        if not isinstance(submit_paths, list) or submission_path not in submit_paths:
            raise ValueError("submission path is outside the public task contract")
        try:
            expected_work_tag = self.expected_work_image_tags[task_id]
            expected_judge_tag = self.expected_judge_image_tags[task_id]
            expected_timeout = self.expected_timeouts[task_id]
        except KeyError as exc:
            raise ValueError("Edge task contract is not frozen") from exc
        if work.get("image_tag") != expected_work_tag:
            raise RuntimeError("Edge work image tag differs")
        if judge.get("image_tag") != expected_judge_tag:
            raise RuntimeError("Edge judge image tag differs")
        if judge.get("eval_timeout") != expected_timeout:
            raise RuntimeError("Edge evaluator timeout differs")
        cwd = payload.get("cwd")
        specs_dir = work.get("specs_dir")
        if not isinstance(cwd, str) or not cwd.startswith("/"):
            raise RuntimeError("Edge public working directory is invalid")
        if not isinstance(specs_dir, str) or not specs_dir.startswith("/"):
            raise RuntimeError("Edge public specs directory is invalid")
        readme_path = posixpath.join(cwd, "README.md")
        tools_path = posixpath.join(specs_dir, "tools", "README.md")
        image = f"seededge/edgebench.work.{task_id}:{expected_work_tag}"
        readme, readme_digest = self.image_file_reader(image, readme_path)
        tools, tools_digest = self.image_file_reader(image, tools_path)
        if not all(isinstance(value, str) and value.strip() for value in (readme, tools)):
            raise RuntimeError("Edge public task files are empty")
        if readme_digest != tools_digest:
            raise RuntimeError("Edge public files came from different work images")
        return (
            f"# EdgeBench public task: {task_id}\n\n"
            f"Work image: {image}\n"
            f"Observed work image digest: {readme_digest}\n"
            f"Required submission path: {submission_path}\n\n"
            f"## {readme_path}\n\n{readme.strip()}\n\n"
            f"## {tools_path}\n\n{tools.strip()}\n\n"
            "## Required submission format\n\n"
            "Return exactly one JSON object and no Markdown: do not add a code "
            "fence, explanation, or any text before or after the JSON. Use this "
            "shape:\n\n"
            "{\n"
            '  "schema_version": 1,\n'
            '  "files": [\n'
            f'    {{"path": "{submission_path}", "type": "file", '
            '"content": "<complete UTF-8 file>"}}\n'
            "  ]\n"
            "}\n\n"
            f"The files array must include `{submission_path}` with the complete "
            "file contents. JSON escaping is required inside the content string.\n"
        )


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _model_configuration(frozen: object) -> ModelConfiguration:
    """Convert the CLI's frozen model record to the runtime model record."""
    payload = frozen.to_dict() if hasattr(frozen, "to_dict") else (asdict(frozen) if is_dataclass(frozen) else frozen)
    if not isinstance(payload, Mapping):
        raise TypeError("frozen model configuration is invalid")
    return ModelConfiguration.from_dict(payload)


def _runtime_manifest(context: object, *, tasks: tuple[TargetBinding, ...]) -> ExperimentOneManifest:
    frozen = context.manifest
    builder = _model_configuration(frozen.builder_model)
    solver = _model_configuration(frozen.solver_model)
    h0_payload = frozen.h0
    h0 = task_harness_from_frozen_schema(h0_payload if isinstance(h0_payload, Mapping) else h0_payload.to_dict())
    official = frozen.official
    return ExperimentOneManifest(
        schema_version=1,
        experiment_id="moss-experiment-one",
        benchmark=str(frozen.suite),
        seed_id=str(context.seed_id),
        rounds=8,
        h0=h0,
        targets=tasks,
        builder_model_configuration=builder,
        solver_model_configuration=solver,
        moss_revision_sha256=_sha256_text("moss-revision:" + str(frozen.sha256)),
        tracked_tree_sha256=_sha256_text("tracked-tree:" + str(frozen.sha256)),
        source_revision_sha256=_sha256_text(str(official.source_revision)),
        task_data_revision_sha256=_sha256_text(str(official.task_data_revision)),
        image_digest_sha256=_sha256_text(
            str(getattr(context.manifest, "suite", "")) + ":pinned-images"
        ),
        api_base_host_sha256=_sha256_text(
            os.environ.get("LLM_BASE_URL", "").split("/v1", 1)[0]
        ),
    )


class _EdgeProductionController:
    """Small production facade used by the CLI after its explicit execute gate."""

    round_executor_class = EdgeLineageRoundExecutor

    def __init__(self, context: object) -> None:
        self.context = context
        self.builder_memory_config = getattr(
            context, "builder_memory_config", BuilderMemoryConfig()
        )
        if not isinstance(self.builder_memory_config, BuilderMemoryConfig):
            raise TypeError("production Builder memory config is invalid")
        self.builder_generator, self.solver_generator = create_responses_generators()
        frozen = context.manifest
        official = frozen.official
        source_root = Path(official.source_repository)
        dataset_root = Path(
            os.environ.get(
                "MOSS_EDGEBENCH_DATASET_ROOT",
                "/home/ubuntu/Projects/moss-exp1-official/edgebench/tasks",
            )
        )
        sforge = Path(
            os.environ.get("MOSS_EDGEBENCH_SFORGE", "/home/ubuntu/venvs/edgebench-official/bin/sforge")
        )
        loader = EdgeBenchPublicTaskLoader(
            dataset_root=dataset_root,
            expected_task_json_sha256={
                "apple_incremental_game": "19021ddcbcaf966d7d43300b439862290a5c6c283aa6e6641f96efa07b34a25c",
                "molecular_self_assembly": "e8569e3a42da7c685fc93367701d844aefe2d4d9e541919fca298501efa41717",
                "treant_forest": "2fdb98ce1166a1fea4743c2ae1613479bdf9eaf755cab190bfd931bc547a615e",
            },
            expected_work_image_tags=_EDGE_WORK_IMAGE_TAGS,
            expected_judge_image_tags=_EDGE_JUDGE_IMAGE_TAGS,
            expected_timeouts=_EDGE_TIMEOUTS,
        )
        targets: list[TargetBinding] = []
        for position in ("A", "B", "C"):
            target_lookup = getattr(frozen, "target", None)
            if callable(target_lookup):
                frozen_target = target_lookup(position)
            else:
                frozen_target = next(
                    item for item in frozen.targets if item.position == position
                )
            task = loader.load(frozen_target.task_id, submission_path=frozen_target.submission_path)
            contract = EdgeBenchContract(
                source_root=source_root,
                dataset_root=dataset_root,
                sforge_executable=sforge,
                source_commit=str(official.source_revision),
                dataset_revision=str(official.task_data_revision),
                task_id=frozen_target.task_id,
                docker_image_reference=_EDGE_JUDGE_IMAGE_REFERENCES[frozen_target.task_id],
                docker_image_digest=_EDGE_JUDGE_IMAGE_DIGESTS[frozen_target.task_id],
                timeout_seconds=frozen_target.evaluator_timeout_seconds,
                score_direction="maximize",
                evaluator_command=("sforge", "eval"),
            )
            contract_sha = _sha256_text(json.dumps({
                "task_id": contract.task_id,
                "source_commit": contract.source_commit,
                "dataset_revision": contract.dataset_revision,
                "docker_image_digest": contract.docker_image_digest,
                "timeout_seconds": contract.timeout_seconds,
                "evaluator_command": list(contract.evaluator_command),
            }, sort_keys=True, separators=(",", ":")))
            targets.append(TargetBinding(
                position=position,
                task_id=frozen_target.task_id,
                task=task,
                submission_path=frozen_target.submission_path,
                evaluator_contract_sha256=contract_sha,
                score_direction="maximize",
            ))
        self.manifest = _runtime_manifest(context, tasks=tuple(targets))

    def _runner(self, position: str, *, root_override: Path | None = None) -> LineageRunner:
        target = self.manifest.target(position)

        def factory(_position: str, root: Path) -> Callable[[LineageRoundRequest], LineageRoundResult]:
            archive = OfficialSolutionArchive(root / "solutions")
            adapter = self._adapter_for(target, root)

            def tool_pack_factory(
                request_target: TargetBinding, tool_root: Path
            ) -> ExperimentOneToolPack:
                return build_experiment_one_tool_pack(
                    benchmark=self.manifest.benchmark,
                    target=request_target,
                    root=tool_root,
                )

            return self.round_executor_class(
                builder_generator=self.builder_generator,
                solver_generator=self.solver_generator,
                adapter=adapter,
                solution_archive=archive,
                audit_directory=root / "audit",
                evaluator_receipt_directory=root / "evaluator_receipts",
                allowed_tools={},
                tool_pack_factory=tool_pack_factory,
                builder_memory_config=self.builder_memory_config,
            )

        return LineageRunner(
            manifest=self.manifest,
            position=position,
            root=(root_override or (self.context.formal_seed_root / "lineages" / position)),
            round_executor_factory=factory,
        )

    def run_canary(self, position: str) -> object:
        if position not in ("A", "B", "C"):
            raise ValueError("canary position must be A, B, or C")
        # Canary intentionally uses a separate root and exactly one round.
        root = self.context.canary_suite_root / self.manifest.seed_id / position
        runner = self._runner(position, root_override=root)
        request = LineageRoundRequest(
            manifest_sha256=self.manifest.sha256,
            benchmark=self.manifest.benchmark,
            seed_id=self.manifest.seed_id,
            position=position,
            round_index=1,
            operation_id=f"canary-{self.manifest.seed_id}-{position}",
            lineage_root=root,
            workspace=runner.workspace,
            target=self.manifest.target(position),
            builder_model_configuration=self.manifest.builder_model_configuration,
            solver_model_configuration=self.manifest.solver_model_configuration,
        )
        result = runner.round_executor(request)
        return {"status": "completed", "position": position, "rounds_completed": 1, "result": result}

    def evolve(self, position: str) -> object:
        receipts = self._runner(position).run()
        return {
            "status": "completed" if all(r.status == "completed" for r in receipts) else "invalid",
            "position": position,
            "rounds_completed": sum(r.status == "completed" for r in receipts),
            "rounds_terminal": len(receipts),
        }

    def resume(self, position: str | None) -> object:
        if position is None:
            return {"status": "completed", "resumed": False}
        return self.evolve(position) | {"resumed": True}

    def freeze(self, position: str) -> object:
        receipt = self._runner(position).freeze()
        return {
            "status": "completed",
            "position": position,
            "freeze_receipt_sha256": receipt.sha256,
            "selected_round": receipt.selected_round,
            "official_score": receipt.official_score,
            "harness_sha256": receipt.harness_sha256,
        }

    def cross_test(self) -> object:
        freeze_receipts: dict[str, FreezeReceipt] = {}
        frozen_harnesses: dict[str, TaskHarnessArtifact] = {}
        freeze_paths: dict[str, Path] = {}
        provenance: dict[str, HarnessTransferProvenance] = {}
        for position in ("A", "B", "C"):
            runner = self._runner(position)
            path = runner.root / "freeze_receipt.json"
            if not path.is_file():
                raise RuntimeError(f"Edge freeze receipt missing for {position}; run evolve and freeze first")
            receipt = _load_freeze_receipt(path)
            freeze_receipts[position] = receipt
            frozen_harnesses[position] = runner.workspace.load_artifact(receipt.harness_sha256)
            freeze_paths[position] = path
            provenance[position] = HarnessTransferProvenance.cleared(
                source_position=position, harness=frozen_harnesses[position]
            )

        def task_executor_factory(cell_root: Path, operation_id: str):
            def execute(request: TaskExecutionRequest) -> TaskExecutionResult:
                tool_pack = build_experiment_one_tool_pack(
                    benchmark=self.manifest.benchmark,
                    target=request.target,
                    root=cell_root / "tools",
                )
                audit_path = cell_root / "audit" / "solver_model_calls.jsonl"
                audited_solver = AuditedGenerator(
                    generator=self.solver_generator,
                    audit_path=audit_path,
                    operation_id_factory=ScopedOperationIdFactory(
                        operation_id, "solver"
                    ),
                    layer="solver",
                    reasoning_effort=request.model_configuration.reasoning_effort,
                    transport_config=self.solver_generator.request_config,
                )
                runtime = _task_runtime_for_target(
                    generator=audited_solver,
                    benchmark=self.manifest.benchmark,
                    target=request.target,
                )
                run = runtime.run(
                    request.harness,
                    task=request.task,
                    model=request.model_configuration.model,
                    tools=tool_pack.legacy_operations(operation_id),
                    tool_registry=tool_pack.registry,
                    tool_workspace=tool_pack.workspace,
                    operation_scope=f"{operation_id}-solver",
                )
                artifact = self._parse_candidate(run.candidate, request.target)
                archive = OfficialSolutionArchive(cell_root / "solutions")
                stored = archive.store(artifact)
                ledger_path = cell_root / "audit" / "cross_solver.json"
                ledger_path.parent.mkdir(parents=True, exist_ok=True)
                solver_call_count = _solver_call_count(run)
                _write_once(ledger_path, _canonical_bytes({"operation_id": operation_id, "solver_calls": solver_call_count, "trace": [e.__dict__ for e in run.events]}), label="cross solver audit")
                return TaskExecutionResult(
                    candidate=artifact,
                    candidate_sha256=artifact.sha256,
                    candidate_archive_sha256=_sha256_file(stored.receipt_path),
                    call_ledger=CallLedgerEvidence(
                        operation_id=operation_id,
                        builder_constructed_count=0,
                        builder_call_count=0,
                        solver_call_count=solver_call_count,
                        memory_read_count=0,
                        audit_ledger_sha256=_sha256_file(ledger_path),
                    ),
                )
            return execute

        def evaluator_factory(cell_root: Path, operation_id: str):
            def evaluate(request: EvaluationRequest) -> OfficialEvaluationResult:
                result = self._evaluate_adapter(
                    self._adapter_for(request.target, cell_root),
                    request.candidate.candidate,
                    operation_id=operation_id,
                )
                if not isinstance(result, EvaluationResult):
                    raise TypeError(
                        f"{self.manifest.benchmark} official adapter must return EvaluationResult"
                    )
                private = result.private
                private_sha = private.get("evidence_sha256") if isinstance(private, Mapping) else None
                if not isinstance(private_sha, str) or _SHA256.fullmatch(private_sha) is None:
                    raise ValueError("Edge official private evidence hash is invalid")
                receipt_path = cell_root / "official_evaluation.json"
                _write_once(receipt_path, _canonical_bytes({
                    "schema_version": 1, "operation_id": operation_id,
                    "task_id": request.target.task_id, "candidate_sha256": request.candidate.candidate_sha256,
                    "score": result.public.score, "feedback": result.public.feedback,
                    "private_evidence_sha256": private_sha,
                }), label="cross evaluator receipt")
                return OfficialEvaluationResult(
                    score=result.public.score,
                    valid=True,
                    public_feedback=result.public.feedback,
                    evaluator_receipt_sha256=_sha256_file(receipt_path),
                    private_evidence_sha256=private_sha,
                )
            return evaluate

        runner = CrossMatrixRunner(
            manifest=self.manifest,
            root=self.context.formal_seed_root,
            task_executor_factory=task_executor_factory,
            evaluator_factory=evaluator_factory,
        )
        baselines = runner.run_h0_baselines()
        receipts = runner.run(
            freeze_receipts=freeze_receipts,
            frozen_harnesses=frozen_harnesses,
            freeze_receipt_paths=freeze_paths,
            transfer_provenance=provenance,
        )
        return {
            "status": "completed",
            "h0_baselines": len(baselines),
            "cross_cells": len(receipts),
            "completed_cells": sum(r.status == "completed" for r in receipts),
        }

    def _parse_candidate(
        self, raw_candidate: str, target: TargetBinding
    ) -> SolutionArtifact:
        return EdgeBenchBundleCodec(
            required_submit_path=target.submission_path
        ).parse(raw_candidate)

    @staticmethod
    def _evaluate_adapter(
        adapter: object, artifact: SolutionArtifact, *, operation_id: str
    ) -> EvaluationResult:
        return adapter.evaluate(artifact, operation_id=operation_id)

    def _adapter_for(self, target: TargetBinding, root: Path) -> EdgeBenchOfficialAdapter:
        official = self.context.manifest.official
        contract = EdgeBenchContract(
            source_root=Path(official.source_repository),
            dataset_root=Path(os.environ.get("MOSS_EDGEBENCH_DATASET_ROOT", "/home/ubuntu/Projects/moss-exp1-official/edgebench/tasks")),
            sforge_executable=Path(os.environ.get("MOSS_EDGEBENCH_SFORGE", "/home/ubuntu/venvs/edgebench-official/bin/sforge")),
            source_commit=str(official.source_revision), dataset_revision=str(official.task_data_revision),
            task_id=target.task_id, docker_image_reference=_EDGE_JUDGE_IMAGE_REFERENCES[target.task_id],
            docker_image_digest=_EDGE_JUDGE_IMAGE_DIGESTS[target.task_id], timeout_seconds=_EDGE_TIMEOUTS[target.task_id],
            score_direction="maximize", evaluator_command=("sforge", "eval"),
        )
        archive = OfficialSolutionArchive(root / "solutions")
        return EdgeBenchOfficialAdapter(contract=contract, solution_archive=archive,
            attempt_root=root / "evaluator_attempts", private_evidence_root=root / "private_evidence")


class _ALEProductionController(_EdgeProductionController):
    """ALE production facade restricted to official public_eval before/after freeze."""

    round_executor_class = ALELineageRoundExecutor

    def __init__(self, context: object) -> None:
        self.context = context
        self.builder_memory_config = getattr(
            context, "builder_memory_config", BuilderMemoryConfig()
        )
        if not isinstance(self.builder_memory_config, BuilderMemoryConfig):
            raise TypeError("production Builder memory config is invalid")
        self.builder_generator, self.solver_generator = create_responses_generators()
        frozen = context.manifest
        official = frozen.official
        if (
            str(official.evolution_evaluator) != "public_eval"
            or str(official.cross_test_evaluator) != "public_eval"
        ):
            raise ValueError("ALE-Bench production execution must use public_eval")
        dataset_value = os.environ.get("MOSS_ALEBENCH_DATASET_ROOT")
        python_value = os.environ.get("MOSS_ALEBENCH_PYTHON")
        if not dataset_value or not python_value:
            raise RuntimeError(
                "ALE-Bench production requires MOSS_ALEBENCH_DATASET_ROOT and "
                "MOSS_ALEBENCH_PYTHON"
            )
        self.dataset_root = Path(dataset_value)
        self.python_executable = Path(python_value)
        loader = ALEBenchPublicTaskLoader(
            dataset_root=self.dataset_root,
            dataset_revision=str(official.task_data_revision),
            expected_zip_sha256=_ALE_TASK_ZIP_SHA256,
        )
        targets: list[TargetBinding] = []
        for position in ("A", "B", "C"):
            target_lookup = getattr(frozen, "target", None)
            if callable(target_lookup):
                frozen_target = target_lookup(position)
            else:
                frozen_target = next(
                    item for item in frozen.targets if item.position == position
                )
            task = loader.load(frozen_target.task_id)
            contract = self._contract_for_task(frozen_target.task_id)
            contract_sha = ALEBenchOfficialAdapter(
                contract=contract,
                private_evidence_root=Path(context.artifact_root)
                / "contract_probes"
                / frozen_target.task_id,
            ).execution_contract_sha256
            targets.append(
                TargetBinding(
                    position=position,
                    task_id=frozen_target.task_id,
                    task=task,
                    submission_path=frozen_target.submission_path,
                    evaluator_contract_sha256=contract_sha,
                    score_direction="maximize",
                )
            )
        self.manifest = _runtime_manifest(context, tasks=tuple(targets))

    def _contract_for_task(self, task_id: str) -> ALEBenchContract:
        try:
            time_limit_seconds, memory_limit_bytes = _ALE_TASK_LIMITS[task_id]
        except KeyError as exc:
            raise ValueError("ALE-Bench task contract is not frozen") from exc
        official = self.context.manifest.official
        return ALEBenchContract(
            source_root=Path(official.source_repository),
            dataset_root=self.dataset_root,
            python_executable=self.python_executable,
            source_commit=str(official.source_revision),
            dataset_revision=str(official.task_data_revision),
            task_id=task_id,
            docker_image_reference=_ALE_DOCKER_IMAGE_REFERENCE,
            docker_image_digest=_ALE_DOCKER_IMAGE_DIGEST,
            judge_version=_ALE_JUDGE_VERSION,
            time_limit_seconds=time_limit_seconds,
            memory_limit_bytes=memory_limit_bytes,
            score_direction="maximize",
            public_evaluator_command=_ALE_PUBLIC_EVALUATOR_COMMAND,
            private_evaluator_command=_ALE_PRIVATE_EVALUATOR_COMMAND,
        )

    def _parse_candidate(
        self, raw_candidate: str, target: TargetBinding
    ) -> SolutionArtifact:
        if target.submission_path != "main.cpp":
            raise ValueError("ALE-Bench submission path must be main.cpp")
        artifact = ALEBenchCodeCodec().parse(raw_candidate)
        if artifact.artifact_kind != "alebench_source_cpp23":
            raise ValueError("ALE-Bench production candidate must use cpp23")
        return artifact

    @staticmethod
    def _evaluate_adapter(
        adapter: object, artifact: SolutionArtifact, *, operation_id: str
    ) -> EvaluationResult:
        return adapter.evaluate_public(artifact, operation_id=operation_id)

    def _adapter_for(self, target: TargetBinding, root: Path) -> ALEBenchOfficialAdapter:
        return ALEBenchOfficialAdapter(
            contract=self._contract_for_task(target.task_id),
            private_evidence_root=root / "private_evidence",
        )


def build_production_controller(context: object) -> object:
    """Build the suite-specific production controller without running a model/evaluator."""
    if context.manifest.suite == "edgebench":
        return _EdgeProductionController(context)
    if context.manifest.suite == "alebench":
        return _ALEProductionController(context)
    raise ValueError("Experiment One production suite is unsupported")


__all__ = [
    "ALEBenchPublicTaskLoader",
    "EdgeBenchPublicTaskLoader",
    "create_responses_generators",
    "EdgeLineageRoundExecutor",
    "ALELineageRoundExecutor",
    "build_production_controller",
]
