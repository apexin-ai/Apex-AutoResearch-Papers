from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from optimization_lab.adapters.base import (
    BenchmarkAdapter,
    EvaluationStatus,
)
from optimization_lab.task_spec import TaskSpec

from .dual_harness import (
    HarnessWorkspace,
    TaskHarnessArtifact,
    TaskHarnessRuntime,
    TaskHarnessSpec,
)
from .dual_runtime import (
    DualHarnessRoundResult,
    DualHarnessRuntime,
    EvaluationResult,
    PublicEvaluation,
)
from .solutions import (
    KernelBenchSolutionCodec,
    SolutionArchive,
    SolutionContractError,
)


_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")


def _canonical_json(payload: object) -> str:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _safe_id(value: str, label: str) -> str:
    if not isinstance(value, str) or not _SAFE_ID.fullmatch(value) or ".." in value:
        raise ValueError(f"{label} is unsafe")
    return value


def initial_kernelbench_harness() -> TaskHarnessArtifact:
    """Return the common, parentless H0 used for every KernelBench instance."""

    spec = TaskHarnessSpec.from_dict(
        {
            "schema_version": 1,
            "nodes": [
                {
                    "id": "draft",
                    "kind": "model_call",
                    "role": "KernelBench solver",
                    "prompt": (
                        "Solve the following public KernelBench task. Produce only one "
                        "complete ModelNew Python candidate, with no explanation or "
                        "extra text.\n\nTask source:\n{task}"
                    ),
                },
                {
                    "id": "contract_report",
                    "kind": "tool_call",
                    "tool": "candidate_contract",
                    "input_key": "draft",
                },
                {
                    "id": "final",
                    "kind": "model_call",
                    "role": "KernelBench candidate finalizer",
                    "prompt": (
                        "Return the final answer for this public KernelBench task. "
                        "Output only one complete ModelNew Python candidate, with no "
                        "explanation or extra text. The final response is the submitted "
                        "candidate.\n\nTask source:\n{task}\n\nDraft candidate:\n"
                        "{draft}\n\nDeterministic contract report:\n{contract_report}"
                    ),
                },
                {"id": "emit", "kind": "emit", "input_key": "final"},
            ],
        }
    )
    return TaskHarnessArtifact(
        schema_version=1,
        version=1,
        parent_sha256=None,
        spec=spec,
    )


def candidate_contract_tool(raw: object) -> dict[str, object]:
    """Check a proposed candidate without allowing contract errors to escape."""

    try:
        if not isinstance(raw, str):
            raise SolutionContractError("candidate must be text")
        artifact = KernelBenchSolutionCodec().parse(raw)
    except Exception as exc:
        reason = " ".join(str(exc).split())[:512] or type(exc).__name__
        return {"accepted": False, "reason": reason}
    return {
        "accepted": True,
        "hash": artifact.sha256,
        "signature": artifact.structural_signature,
    }


class KernelBenchPublicEvaluator:
    """Archive a candidate, run the official adapter, and expose public fields only."""

    def __init__(
        self,
        *,
        task: TaskSpec,
        adapter: BenchmarkAdapter,
        archive_root: Path,
        cell_id: str,
        private_log_root: Path,
        gpu_uuid: str,
    ) -> None:
        self.task = task
        self.adapter = adapter
        self.archive = SolutionArchive(archive_root, cell_id=cell_id)
        self.private_log_root = private_log_root.resolve()
        if not isinstance(gpu_uuid, str) or not gpu_uuid.strip():
            raise ValueError("GPU UUID is required for evaluator audit")
        self.gpu_uuid = gpu_uuid.strip()
        self.codec = KernelBenchSolutionCodec(task_id=task.task_id)

    def __call__(self, candidate: str, candidate_id: str) -> EvaluationResult:
        candidate_id = _safe_id(candidate_id, "candidate id")
        private_dir = (self.private_log_root / candidate_id).resolve()
        if self.private_log_root not in private_dir.parents:
            raise ValueError("candidate private log directory escapes its root")
        raw_candidate_sha256 = hashlib.sha256(candidate.encode("utf-8")).hexdigest()
        started_at_unix_ns = time.time_ns()

        try:
            artifact = self.codec.parse(candidate)
        except SolutionContractError as exc:
            common = self._receipt_common(
                candidate_id=candidate_id,
                candidate_sha256=raw_candidate_sha256,
                started_at_unix_ns=started_at_unix_ns,
            )
            _write_json_once(
                private_dir / "evaluation_started.json",
                {**common, "phase": "started", "adapter_called": False},
            )
            reason = " ".join(str(exc).split())[:512]
            _write_json_once(
                private_dir / "evaluation_completed.json",
                {
                    **common,
                    "phase": "completed",
                    "completed_at_unix_ns": time.time_ns(),
                    "adapter_called": False,
                    "status": "contract_rejected",
                    "compiled": False,
                    "correct": False,
                    "elapsed_seconds": 0.0,
                    "gpu_seconds": 0.0,
                    "hardware": "",
                    "raw_log_sha256": None,
                },
            )
            feedback = _canonical_json(
                {"status": "contract_rejected", "error_summary": reason}
            )
            return EvaluationResult(
                public=PublicEvaluation(0.0, feedback),
                private=type(exc).__name__,
            )

        self.archive.store(candidate_id, artifact)
        canonical_path = (
            self.archive.cell_root
            / "content"
            / f"{artifact.sha256}{artifact.extension}"
        )
        _write_bytes_once(canonical_path, artifact.text.encode("utf-8"))
        common = self._receipt_common(
            candidate_id=candidate_id,
            candidate_sha256=artifact.sha256,
            started_at_unix_ns=started_at_unix_ns,
        )
        _write_json_once(
            private_dir / "evaluation_started.json",
            {**common, "phase": "started", "adapter_called": True},
        )
        try:
            adapter_result = self.adapter.evaluate(
                self.task,
                canonical_path,
                private_dir,
            )
        except Exception as exc:
            _write_json_once(
                private_dir / "evaluation_failed.json",
                {
                    **common,
                    "phase": "failed",
                    "completed_at_unix_ns": time.time_ns(),
                    "adapter_called": True,
                    "error_type": type(exc).__name__,
                },
            )
            raise

        raw_log_sha256 = self._raw_log_sha256(adapter_result.raw_log_path, private_dir)
        _write_json_once(
            private_dir / "evaluation_completed.json",
            {
                **common,
                "phase": "completed",
                "completed_at_unix_ns": time.time_ns(),
                "adapter_called": True,
                "status": adapter_result.status.value,
                "compiled": adapter_result.compiled,
                "correct": adapter_result.correct,
                "elapsed_seconds": adapter_result.elapsed_seconds,
                "gpu_seconds": adapter_result.gpu_seconds,
                "hardware": adapter_result.hardware,
                "raw_log_sha256": raw_log_sha256,
            },
        )
        if adapter_result.status is EvaluationStatus.ENVIRONMENT_INVALID:
            raise RuntimeError("KernelBench evaluation environment invalid")

        feedback_payload: dict[str, object] = {
            "status": adapter_result.status.value,
            "compiled": adapter_result.compiled,
            "correct": adapter_result.correct,
            "speedup": adapter_result.speedup_vs_eager,
        }
        score = 0.0
        if adapter_result.correct:
            speedup = adapter_result.speedup_vs_eager
            if speedup is None:
                raise RuntimeError("correct KernelBench result lacks a speedup")
            score = speedup
        elif adapter_result.error_summary:
            feedback_payload["error_summary"] = (
                f"official evaluator reported {adapter_result.status.value}"
            )

        return EvaluationResult(
            public=PublicEvaluation(score, _canonical_json(feedback_payload)),
            private=adapter_result,
        )

    def _receipt_common(
        self,
        *,
        candidate_id: str,
        candidate_sha256: str,
        started_at_unix_ns: int,
    ) -> dict[str, object]:
        return {
            "schema_version": 1,
            "candidate_id": candidate_id,
            "candidate_sha256": candidate_sha256,
            "task_id": self.task.task_id,
            "task_sha256": self.task.task_sha256,
            "gpu_uuid": self.gpu_uuid,
            "started_at_unix_ns": started_at_unix_ns,
        }

    @staticmethod
    def _raw_log_sha256(raw_log_path: str, private_dir: Path) -> str:
        if not isinstance(raw_log_path, str) or not raw_log_path.strip():
            raise RuntimeError("official evaluator did not persist a raw log")
        path = Path(raw_log_path).resolve()
        if private_dir not in path.parents or not path.is_file():
            raise RuntimeError("official evaluator raw log is outside the private receipt root")
        return hashlib.sha256(path.read_bytes()).hexdigest()


def _candidate_contract_probe(artifact: TaskHarnessArtifact) -> bool:
    return all(
        node.kind != "tool_call" or node.tool == "candidate_contract"
        for node in artifact.spec.nodes
    )


def evolve_instance(
    *,
    runtime: DualHarnessRuntime,
    workspace: HarnessWorkspace,
    task: TaskSpec,
    task_source: str,
    evaluator: Callable[[str, str], EvaluationResult],
    rounds: int,
    execution_contract_sha256: str,
    run_prefix: str,
) -> tuple[DualHarnessRoundResult, ...]:
    """Evolve one instance lineage without constructing either model client."""

    if runtime.workspace.root != workspace.root:
        raise ValueError("runtime and experiment workspace differ")
    if not isinstance(rounds, int) or isinstance(rounds, bool) or rounds < 1:
        raise ValueError("rounds must be a positive integer")
    if not isinstance(task_source, str) or not task_source.strip():
        raise ValueError("public task source is required")
    run_prefix = _safe_id(run_prefix, "run prefix")
    if not workspace.current_path.exists():
        workspace.commit(initial_kernelbench_harness())

    results: list[DualHarnessRoundResult] = []
    for round_index in range(1, rounds + 1):
        run_id = _safe_id(f"{run_prefix}-r{round_index:03d}", "run id")

        def evaluate(
            candidate: str, *, _candidate_id: str = run_id
        ) -> EvaluationResult:
            return evaluator(candidate, _candidate_id)

        result = runtime.run_round(
            run_id=run_id,
            execution_contract_sha256=execution_contract_sha256,
            task=task_source,
            tools={"candidate_contract": candidate_contract_tool},
            evaluator=evaluate,
            probe=_candidate_contract_probe,
        )
        results.append(result)
    return tuple(results)


@dataclass(frozen=True)
class FrozenHarnessCrossTestResult:
    cross_test_id: str
    task_id: str
    harness_sha256: str
    candidate: str
    score: float | None
    feedback: str
    receipt_path: Path


def cross_test_frozen_harness(
    *,
    workspace: HarnessWorkspace,
    task_runtime: TaskHarnessRuntime,
    task: TaskSpec,
    task_source: str,
    solver_model: str,
    harness_sha256: str,
    evaluator: Callable[[str, str], EvaluationResult],
    cross_test_id: str,
    receipt_root: Path,
) -> FrozenHarnessCrossTestResult:
    """Run an explicit frozen Harness SHA without constructing a Builder."""

    cross_test_id = _safe_id(cross_test_id, "cross-test id")
    artifact = workspace.load_artifact(harness_sha256)
    task_run = task_runtime.run(
        artifact=artifact,
        task=task_source,
        model=solver_model,
        tools={"candidate_contract": candidate_contract_tool},
    )
    evaluation = evaluator(task_run.candidate, cross_test_id)
    if not isinstance(evaluation, EvaluationResult):
        raise TypeError("evaluator must return EvaluationResult")

    payload = {
        "schema_version": 1,
        "cross_test_id": cross_test_id,
        "task_id": task.task_id,
        "task_sha256": task.task_sha256,
        "task_source_sha256": hashlib.sha256(task_source.encode("utf-8")).hexdigest(),
        "solver_model": solver_model,
        "harness_sha256": task_run.harness_sha256,
        "candidate": task_run.candidate,
        "candidate_sha256": hashlib.sha256(
            task_run.candidate.encode("utf-8")
        ).hexdigest(),
        "score": evaluation.public.score,
        "feedback": evaluation.public.feedback,
    }
    receipt_path = receipt_root.resolve() / f"{cross_test_id}.json"
    _write_json_once(receipt_path, payload)
    return FrozenHarnessCrossTestResult(
        cross_test_id=cross_test_id,
        task_id=task.task_id,
        harness_sha256=task_run.harness_sha256,
        candidate=task_run.candidate,
        score=evaluation.public.score,
        feedback=evaluation.public.feedback,
        receipt_path=receipt_path,
    )


def _write_json_once(path: Path, payload: object) -> None:
    encoded = (_canonical_json(payload) + "\n").encode("utf-8")
    _write_bytes_once(path, encoded)


def _write_bytes_once(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    file_descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        suffix=".publish.tmp",
    )
    try:
        with os.fdopen(file_descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary_name, path)
        except FileExistsError:
            if path.read_bytes() != content:
                raise ValueError("refusing to overwrite different content")
    except Exception:
        raise
    finally:
        Path(temporary_name).unlink(missing_ok=True)


__all__ = [
    "FrozenHarnessCrossTestResult",
    "KernelBenchPublicEvaluator",
    "candidate_contract_tool",
    "cross_test_frozen_harness",
    "evolve_instance",
    "initial_kernelbench_harness",
]
