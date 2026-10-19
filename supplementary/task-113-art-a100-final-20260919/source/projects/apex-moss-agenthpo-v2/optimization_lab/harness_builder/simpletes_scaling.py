from __future__ import annotations

import ast
import hashlib
import json
import math
import re
import subprocess
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

from optimization_lab.generation import GenerationResult, InvalidCandidate

from .builder_harness import (
    BuilderEvolutionResult,
    BuilderHarness,
    BuilderStepEvent,
    PortfolioEvolutionResult,
)
from .champion_archive import GateDecision
from .dual_harness import (
    HarnessTraceEvent,
    HarnessWorkspace,
    TaskHarnessArtifact,
    TaskHarnessSpec,
)
from .dual_harness import TaskHarnessRuntime
from .dual_runtime import EvaluationResult, IncompleteRoundError, PublicEvaluation


SIMPLETES_REPOSITORY = "https://github.com/wq-will/SimpleTES.git"
SIMPLETES_PAPER_COMMIT = "df00a9e11d20246d1fd5adfb60293f9c9370740f"
SLDBENCH_REPOSITORY = "pkuHaowei/sldbench"
SLDBENCH_REVISION = "721b846056f031737ff7fa72572c021324e3ec0e"
SIMPLETES_MODEL = "gpt-oss-120b"
SIMPLETES_MODEL_REVISION = "b5c939de8f754692c1647ca79fbf85e8c1e70f8a"
SIMPLETES_PAPER_SCORES = {
    "parallel": 1.000,
    "domain_mix": 0.991,
    "lr_bsz": 0.712,
    "u_shape": -0.008,
}

_DENIED_IMPORT_ROOTS = {
    "asyncio",
    "ctypes",
    "datasets",
    "http",
    "multiprocessing",
    "os",
    "pathlib",
    "requests",
    "shutil",
    "socket",
    "subprocess",
    "sys",
    "urllib",
}
_DENIED_CALLS = {"compile", "eval", "exec", "globals", "input", "locals", "open"}


def _canonical_json(payload: Any) -> str:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


@dataclass(frozen=True)
class SimpleTESScalingTask:
    label: str
    dataset_config: str
    directory: str
    feature_names: tuple[str, ...]
    target_names: tuple[str, ...]
    max_param_count: int
    paper_score: float
    published_best: str


SIMPLETES_TASKS = (
    SimpleTESScalingTask(
        "parallel",
        "parallel_scaling_law",
        "parallel_scaling_law",
        ("num_params", "parallel_size"),
        ("loss",),
        4,
        1.000,
        "best_results/data_science/parallel_scaling_law/parallel_scaling_law_best.py",
    ),
    SimpleTESScalingTask(
        "domain_mix",
        "domain_mixture_scaling_law",
        "domain_mixture_scaling_law",
        tuple(f"proportion_domain_{index}" for index in range(1, 6)),
        tuple(f"loss_domain_{index}" for index in range(1, 6)),
        35,
        0.991,
        "best_results/data_science/domain_mixture_scaling_law/domain_mixture_scaling_law_best.py",
    ),
    SimpleTESScalingTask(
        "lr_bsz",
        "lr_bsz_scaling_law",
        "lr_bsz_scaling_law",
        ("lr", "bsz", "data_size", "non_embedding_param_size"),
        ("lm_loss",),
        26,
        0.712,
        "best_results/data_science/learning_rate_and_batch_size_scaling_law/learning_rate_and_batch_size_scaling_law_best.py",
    ),
    SimpleTESScalingTask(
        "u_shape",
        "easy_question_scaling_law",
        "easy_question_scaling_law",
        ("log_flops",),
        ("brier_score",),
        6,
        -0.008,
        "best_results/data_science/easy_question_u_shaped_scaling_law/easy_question_u_shaped_scaling_law_best.py",
    ),
)


@dataclass(frozen=True)
class SimpleTESScalingContract:
    schema_version: int = 1
    simpletes_commit: str = SIMPLETES_PAPER_COMMIT
    sldbench_revision: str = SLDBENCH_REVISION
    model: str = SIMPLETES_MODEL
    model_revision: str = SIMPLETES_MODEL_REVISION
    temperature: float = 0.7
    max_tokens: int = 32_768
    reasoning_effort: str = "medium"
    official_c: int = 16
    official_l: int = 20
    official_k: int = 16
    official_seeds: int = 5
    first_round_harnesses: int = 8

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "simpletes_repository": SIMPLETES_REPOSITORY,
            "simpletes_commit": self.simpletes_commit,
            "sldbench_repository": SLDBENCH_REPOSITORY,
            "sldbench_revision": self.sldbench_revision,
            "model": self.model,
            "model_revision": self.model_revision,
            "generation": {
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
                "reasoning_effort": self.reasoning_effort,
                "web_access": False,
            },
            "official_search": {
                "C": self.official_c,
                "L": self.official_l,
                "K": self.official_k,
                "seeds": self.official_seeds,
            },
            "first_round_harnesses": self.first_round_harnesses,
            "solver_starting_point": "published_best_at_pinned_simpletes_commit",
            "metric": "mean clipped test R2 across the four paper tasks",
            "paper_scores": dict(SIMPLETES_PAPER_SCORES),
        }

    @property
    def sha256(self) -> str:
        return hashlib.sha256(_canonical_json(self.to_dict()).encode()).hexdigest()


@dataclass(frozen=True)
class SimpleTESTaskLineageContract:
    schema_version: int
    task: str
    base_contract_sha256: str
    solver_rounds: int = 8

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported SimpleTES task lineage contract schema")
        if self.task not in {item.label for item in SIMPLETES_TASKS}:
            raise ValueError("lineage task is outside the pinned SimpleTES tasks")
        if not re.fullmatch(r"[0-9a-f]{64}", self.base_contract_sha256):
            raise ValueError("lineage base contract hash is invalid")
        if (
            isinstance(self.solver_rounds, bool)
            or not isinstance(self.solver_rounds, int)
            or not 1 <= self.solver_rounds <= 32
        ):
            raise ValueError("lineage solver rounds must be between one and 32")

    @property
    def builder_updates(self) -> int:
        return self.solver_rounds - 1

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "kind": "simpletes_task_lineage",
            "task": self.task,
            "base_contract_sha256": self.base_contract_sha256,
            "solver_rounds": self.solver_rounds,
            "builder_updates": self.builder_updates,
            "round_order": "solver_then_evaluator_then_builder",
            "cross_task_history": "forbidden",
        }

    @property
    def sha256(self) -> str:
        return hashlib.sha256(_canonical_json(self.to_dict()).encode()).hexdigest()


@dataclass(frozen=True)
class SimpleTESProgram:
    code: str
    sha256: str

    @classmethod
    def from_response(cls, response: str) -> "SimpleTESProgram":
        blocks = re.findall(r"```([^\n]*)\n(.*?)```", response, flags=re.DOTALL)
        if len(blocks) != 1:
            raise InvalidCandidate("response must contain exactly one fenced code block")
        language, code = blocks[0]
        if language.strip().lower() not in {"", "py", "python"}:
            raise InvalidCandidate("scaling-law candidate must be Python")
        code = code.strip() + "\n"
        try:
            tree = ast.parse(code)
        except SyntaxError as exc:
            raise InvalidCandidate(f"candidate syntax error: {exc.msg}") from exc
        functions = {
            node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        if not {"fit_scaling_law", "scaling_law_func"} <= functions:
            raise InvalidCandidate("candidate must define both scaling-law functions")
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                roots = {alias.name.split(".", 1)[0] for alias in node.names}
                if roots & _DENIED_IMPORT_ROOTS:
                    raise InvalidCandidate("candidate imports a denied capability")
            if isinstance(node, ast.ImportFrom):
                root = (node.module or "").split(".", 1)[0]
                if root in _DENIED_IMPORT_ROOTS:
                    raise InvalidCandidate("candidate imports a denied capability")
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in _DENIED_CALLS or node.func.id == "__import__":
                    raise InvalidCandidate("candidate calls a denied capability")
            if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
                raise InvalidCandidate("candidate uses a denied reflective attribute")
        return cls(code=code, sha256=hashlib.sha256(code.encode()).hexdigest())


@dataclass(frozen=True)
class SimpleTESEvaluation:
    task: str
    score: float
    valid: bool
    failure_class: str | None
    feedback: str


class ClaimedGenerator:
    """Persist or replay one external generation, never retry an orphaned claim."""

    def __init__(
        self,
        *,
        workspace: HarnessWorkspace,
        generator: Any,
        run_id: str,
        stage: str,
        contract_sha256: str,
    ) -> None:
        self.workspace = workspace
        self.generator = generator
        self.run_id = run_id
        self.stage = stage
        self.contract_sha256 = contract_sha256

    def estimated_api_cost_usd(self) -> float:
        return self.generator.estimated_api_cost_usd()

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        request_sha = hashlib.sha256(
            _canonical_json(
                {
                    "contract_sha256": self.contract_sha256,
                    "model": model,
                    "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
                }
            ).encode()
        ).hexdigest()
        saved = self.workspace.load_operation_result(
            run_id=self.run_id,
            stage=self.stage,
            missing_ok=True,
        )
        if saved is not None:
            if saved.get("request_sha256") != request_sha:
                raise ValueError("operation id is bound to another generation request")
            payload = saved["payload"]
            return GenerationResult(
                raw_response=payload["raw_response"],
                api_cost_usd=float(payload.get("api_cost_usd", 0.0)),
                provider=payload.get("provider", "replayed"),
                usage=dict(payload.get("usage", {})),
            )
        claim = self.workspace.load_operation_claim(
            run_id=self.run_id,
            stage=self.stage,
            missing_ok=True,
        )
        if claim is not None:
            if claim.get("request_sha256") != request_sha:
                raise ValueError("operation id is bound to another generation request")
            raise IncompleteRoundError(
                f"{self.stage} started without a durable result; retry is disabled"
            )
        self.workspace.claim_operation(
            run_id=self.run_id,
            stage=self.stage,
            request_sha256=request_sha,
        )
        result = self.generator.generate(prompt, model=model)
        self.workspace.record_operation_result(
            run_id=self.run_id,
            stage=self.stage,
            request_sha256=request_sha,
            payload={
                "raw_response": result.raw_response,
                "api_cost_usd": result.api_cost_usd,
                "provider": result.provider,
                "usage": dict(result.usage),
            },
        )
        return result


class SequencedClaimedGenerator:
    def __init__(
        self,
        *,
        workspace: HarnessWorkspace,
        generator: Any,
        run_id: str,
        stage_prefix: str,
        contract_sha256: str,
    ) -> None:
        self.workspace = workspace
        self.generator = generator
        self.run_id = run_id
        self.stage_prefix = stage_prefix
        self.contract_sha256 = contract_sha256
        self.call_index = 0

    def bind_run_id(self, run_id: str) -> None:
        """Bind subsequent stage claims to the active formal round."""

        if not run_id.strip():
            raise ValueError("generator run id is required")
        self.run_id = run_id

    def estimated_api_cost_usd(self) -> float:
        return self.generator.estimated_api_cost_usd()

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.call_index += 1
        claimed = ClaimedGenerator(
            workspace=self.workspace,
            generator=self.generator,
            run_id=self.run_id,
            stage=f"{self.stage_prefix}-{self.call_index:03d}",
            contract_sha256=self.contract_sha256,
        )
        return claimed.generate(prompt, model=model)


def initial_simpletes_harness() -> TaskHarnessArtifact:
    spec = TaskHarnessSpec.from_dict(
        {
            "schema_version": 1,
            "nodes": [
                {
                    "id": "discover-law",
                    "kind": "model_call",
                    "role": "scaling-law researcher",
                    "prompt": (
                        "Improve the published-best program for the public scaling-law task "
                        "below. Preserve its complete working implementation unless you have "
                        "a concrete, ABI-safe improvement. Never replace a working baseline "
                        "with a speculative rewrite. Return exactly one complete Python code "
                        "block and no other code block.\n\n{task}"
                    ),
                },
                {"id": "emit", "kind": "emit", "input_key": "discover-law"},
            ],
        }
    )
    return TaskHarnessArtifact(
        schema_version=1,
        version=1,
        parent_sha256=None,
        spec=spec,
    )


def rich_simpletes_harness(*, parent: TaskHarnessArtifact | None = None) -> TaskHarnessArtifact:
    """Create the multi-role SimpleTES Harness used by new lineage runs."""

    version = 1 if parent is None else parent.version + 1
    parent_sha256 = None if parent is None else parent.sha256
    spec = TaskHarnessSpec.from_dict(
        {
            "schema_version": 2,
            "interface": {
                "task_template": "{task}",
                "constraints": {
                    "candidate_format": "one complete Python code block",
                    "dependencies": ["numpy", "scipy"],
                    "preserve_abi": True,
                },
            },
            "memory": {
                "abstract": [
                    "Prefer a narrow, testable algorithm change over a wholesale rewrite.",
                    "Treat evaluator failures as evidence about the search direction, not only the candidate.",
                ],
                "raw_refs": [],
            },
            "capabilities": {
                "tools": [],
                "skills": [
                    {
                        "id": "fit_diagnostics",
                        "prompt": "Summarize likely fitting failure modes and propose one falsifiable direction.",
                    }
                ],
            },
            "router": {
                "directive": "Diagnose first, choose one search direction, then implement it.",
                "execution_order": ["analyst", "diagnostics", "designer", "implementer", "emit"],
            },
            "nodes": [
                {
                    "id": "analyst",
                    "kind": "model_call",
                    "role": "scaling-law analyst",
                    "prompt": (
                        "Analyze the task, published baseline, and available Harness memory. "
                        "Identify one concrete algorithmic risk or opportunity.\n\n{task}"
                    ),
                },
                {
                    "id": "diagnostics",
                    "kind": "skill_call",
                    "skill": "fit_diagnostics",
                    "input_key": "analyst",
                },
                {
                    "id": "designer",
                    "kind": "model_call",
                    "role": "search strategist",
                    "prompt": (
                        "Turn the analysis into one falsifiable algorithm search direction. "
                        "Do not write the final program.\n\nAnalysis:\n{analyst}\n\nDiagnostics:\n{diagnostics}"
                    ),
                },
                {
                    "id": "implementer",
                    "kind": "model_call",
                    "role": "scaling-law implementer",
                    "prompt": (
                        "Implement the selected direction as one complete candidate program. "
                        "Return exactly one Python code block and no prose.\n\nTask:\n{task}\n\n"
                        "Analysis:\n{analyst}\n\nSearch direction:\n{designer}"
                    ),
                },
                {"id": "emit", "kind": "emit", "input_key": "implementer"},
            ],
        }
    )
    return TaskHarnessArtifact(
        schema_version=1,
        version=version,
        parent_sha256=parent_sha256,
        spec=spec,
    )


def task_prompt(source_root: Path, task: SimpleTESScalingTask) -> str:
    root = source_root.resolve() / "datasets" / "scaling_law" / task.directory
    instruction = (root / f"{task.directory}.txt").read_text(encoding="utf-8")
    seed = (source_root.resolve() / task.published_best).read_text(encoding="utf-8")
    output_shape = "(N, 5)" if len(task.target_names) == 5 else "(N,)"
    return (
        instruction.rstrip()
        + "\n\nRuntime and ABI contract (violations score as failures):\n"
        + "- Installed candidate dependencies are NumPy and SciPy only; sympy is NOT installed.\n"
        + f"- fit_scaling_law must return at most {task.max_param_count} total scalar values.\n"
        + f"- scaling_law_func must return exactly {output_shape}; do not add hypothesis axes.\n"
        + "- fit is called independently per group; scalar targets arrive as (N,), while the "
        + "domain-mixture target arrives as (N, 5).\n"
        + "- scaling_law_func may use only per-row input transformations, never statistics "
        + "computed across evaluation rows.\n"
        + "- The program below is the published best result at the pinned SimpleTES commit. "
        + "Keep it verbatim unless making a narrow, justified improvement.\n\n"
        + "Published-best program to improve:\n```python\n"
        + seed.rstrip()
        + "\n```\n"
    )


class SimpleTESScalingEvaluator:
    """Controller-side labels plus a label-blind, networkless candidate worker."""

    def __init__(self, *, source_root: Path, python_root: Path, site_packages: Path) -> None:
        self.source_root = source_root.resolve()
        self.python_root = python_root.resolve()
        self.site_packages = site_packages.resolve()
        self.worker_path = Path(__file__).with_name("simpletes_scaling_worker.py").resolve()

    def evaluate(self, *, task: SimpleTESScalingTask, program: SimpleTESProgram) -> SimpleTESEvaluation:
        try:
            import numpy as np
            from datasets import load_dataset

            train = load_dataset(
                SLDBENCH_REPOSITORY,
                name=task.dataset_config,
                split="train",
                revision=SLDBENCH_REVISION,
            )
            test = load_dataset(
                SLDBENCH_REPOSITORY,
                name=task.dataset_config,
                split="test",
                revision=SLDBENCH_REVISION,
            )
            groups = []
            true_parts = []
            for key in sorted(set(train["group"])):
                train_group = train.filter(lambda row: row["group"] == key)
                test_group = test.filter(lambda row: row["group"] == key)
                train_x = np.stack(
                    [np.asarray(train_group[name]) for name in task.feature_names], axis=1
                )
                train_y = np.stack(
                    [np.asarray(train_group[name]) for name in task.target_names], axis=1
                )
                if train_y.shape[1] == 1:
                    train_y = train_y.squeeze(axis=1)
                test_x = np.stack(
                    [np.asarray(test_group[name]) for name in task.feature_names], axis=1
                )
                test_y = np.stack(
                    [np.asarray(test_group[name]) for name in task.target_names], axis=1
                )
                if test_y.shape[1] == 1:
                    test_y = test_y.squeeze(axis=1)
                groups.append(
                    {
                        "key": str(key),
                        "train_x": train_x.tolist(),
                        "train_y": train_y.tolist(),
                        "test_x": test_x.tolist(),
                    }
                )
                true_parts.append(test_y)
            with tempfile.TemporaryDirectory(prefix="moss-simpletes-candidate-") as tmp:
                candidate_path = Path(tmp) / "candidate.py"
                candidate_path.write_text(program.code, encoding="utf-8")
                payload = _canonical_json(
                    {"groups": groups, "max_param_count": task.max_param_count}
                )
                command = self._sandbox_command(candidate_path)
                process = subprocess.run(
                    command,
                    input=payload,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=620,
                    check=False,
                )
            if process.returncode != 0:
                detail = process.stderr.strip().splitlines()[-1] if process.stderr.strip() else "worker_failed"
                return SimpleTESEvaluation(task.label, -1.0, False, "runtime_error", detail[:500])
            output = json.loads(process.stdout)
            predictions = [np.asarray(part, dtype=float) for part in output["predictions"]]
            pred = np.concatenate(predictions)
            true = np.concatenate(true_parts)
            if true.ndim == 1:
                true = true.reshape(-1, 1)
            if pred.ndim == 1:
                pred = pred.reshape(-1, 1)
            if pred.shape != true.shape or not np.isfinite(pred).all():
                raise ValueError("prediction shape or finiteness failed")
            mse = np.mean((true - pred) ** 2, axis=0)
            variance = np.var(true, axis=0)
            nmse = np.divide(
                mse,
                variance,
                out=np.full_like(mse, np.inf),
                where=variance > 1e-9,
            )
            raw_r2 = float(1.0 - np.mean(nmse))
            score = max(-1.0, min(1.0, raw_r2))
            return SimpleTESEvaluation(
                task.label,
                score,
                True,
                None,
                f"test_r2={score:.6f}",
            )
        except subprocess.TimeoutExpired:
            return SimpleTESEvaluation(task.label, -1.0, False, "timeout", "candidate timed out")
        except Exception as exc:
            return SimpleTESEvaluation(
                task.label,
                -1.0,
                False,
                "evaluation_error",
                f"{type(exc).__name__}:{str(exc)[:400]}",
            )

    def _sandbox_command(self, candidate_path: Path) -> list[str]:
        return [
            "bwrap",
            "--die-with-parent",
            "--new-session",
            "--unshare-all",
            "--ro-bind",
            "/usr",
            "/usr",
            "--ro-bind",
            "/lib",
            "/lib",
            "--ro-bind",
            "/lib64",
            "/lib64",
            "--ro-bind",
            str(self.python_root),
            "/python",
            "--ro-bind",
            str(self.site_packages),
            "/packages",
            "--ro-bind",
            str(self.worker_path),
            "/worker.py",
            "--ro-bind",
            str(candidate_path),
            "/candidate.py",
            "--proc",
            "/proc",
            "--dev",
            "/dev",
            "--tmpfs",
            "/tmp",
            "--dir",
            "/work",
            "--chdir",
            "/work",
            "--clearenv",
            "--setenv",
            "PATH",
            "/python/bin:/usr/bin",
            "--setenv",
            "PYTHONPATH",
            "/packages",
            "--setenv",
            "PYTHONNOUSERSITE",
            "1",
            "--setenv",
            "OPENBLAS_NUM_THREADS",
            "1",
            "/python/bin/python3.13",
            "/worker.py",
        ]


class SimpleTESLineageAdapter:
    """Bind SimpleTES task semantics to the benchmark-neutral lineage runner."""

    def __init__(
        self,
        *,
        source_root: Path,
        evaluator: SimpleTESScalingEvaluator,
        task: SimpleTESScalingTask,
        contract: SimpleTESScalingContract | None = None,
    ) -> None:
        if task not in SIMPLETES_TASKS:
            raise ValueError("task is not part of the pinned SimpleTES contract")
        self.source_root = source_root.resolve()
        self.evaluator_impl = evaluator
        self.task = task
        self.contract = contract or SimpleTESScalingContract()
        self.contract_sha256 = self.contract.sha256
        self.solver_model = self.contract.model

    def task_prompt(self, task: SimpleTESScalingTask) -> str:
        return task_prompt(self.source_root, task)

    def tools(self, task: SimpleTESScalingTask) -> Mapping[str, Any]:
        return {}

    def evaluator(self, task: SimpleTESScalingTask) -> Any:
        def evaluate(candidate: str) -> EvaluationResult:
            try:
                program = SimpleTESProgram.from_response(candidate)
            except InvalidCandidate as exc:
                return EvaluationResult(
                    PublicEvaluation(None, f"invalid_candidate:{str(exc)[:500]}"),
                    private=None,
                )
            item = self.evaluator_impl.evaluate(task=task, program=program)
            return EvaluationResult(
                PublicEvaluation(item.score if item.valid else None, item.feedback),
                private=item,
            )

        from .evolution import CallbackEvaluatorRunner

        return CallbackEvaluatorRunner(evaluate)

    def probe(self, task: SimpleTESScalingTask, artifact: TaskHarnessArtifact) -> bool:
        run = TaskHarnessRuntime(generator=_FixtureHarnessGenerator()).run(
            artifact,
            task=task_prompt(self.source_root, task),
            model=self.contract.model,
            tools={},
        )
        return bool(run.candidate.strip())

    def preserves_capability(
        self,
        task: SimpleTESScalingTask,
        previous: TaskHarnessArtifact,
        current: TaskHarnessArtifact,
    ) -> tuple[bool, str]:
        del task
        model_calls = sum(node.kind == "model_call" for node in current.spec.nodes)
        emits = [node for node in current.spec.nodes if node.kind == "emit"]
        if model_calls < 1 or len(emits) != 1 or current.spec.nodes[-1].kind != "emit":
            return False, "Harness lost required model-call/unique-final-emit capability"
        if previous.spec.nodes[-1].kind != "emit":
            return False, "previous Harness violated the final emit capability"
        return True, "required model-call and final emit capabilities preserved"


class _FixtureHarnessGenerator:
    """No-network generator used to execute a proposed Harness during probing."""

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        return GenerationResult(raw_response="fixture-harness-candidate", provider="fixture")


@dataclass(frozen=True)
class HarnessScore:
    harness_sha256: str
    task_scores: tuple[SimpleTESEvaluation, ...]

    @property
    def utility(self) -> float:
        return sum(item.score for item in self.task_scores) / len(self.task_scores)

    @property
    def all_valid(self) -> bool:
        return all(item.valid for item in self.task_scores)


@dataclass(frozen=True)
class SimpleTESPortfolioResult:
    run_id: str
    contract_sha256: str
    incumbent: HarnessScore
    portfolio: PortfolioEvolutionResult
    scores: tuple[HarnessScore, ...]


class SimpleTESPortfolioCampaign:
    """One eight-challenger Moss portfolio round on the four paper tasks."""

    def __init__(
        self,
        *,
        workspace: HarnessWorkspace,
        source_root: Path,
        generator: Any,
        evaluator: SimpleTESScalingEvaluator,
        contract: SimpleTESScalingContract | None = None,
        contract_sha256_override: str | None = None,
        reporter: Any = print,
    ) -> None:
        self.workspace = workspace
        self.source_root = source_root.resolve()
        self.generator = generator
        self.evaluator = evaluator
        self.contract = contract or SimpleTESScalingContract()
        if contract_sha256_override is not None and not re.fullmatch(
            r"[0-9a-f]{64}", contract_sha256_override
        ):
            raise ValueError("scaling contract hash override is invalid")
        self.contract_sha256 = contract_sha256_override or self.contract.sha256
        self.reporter = reporter

    def run(
        self,
        *,
        run_id: str,
        candidate_count: int | None = None,
        feedback: str | None = None,
    ) -> SimpleTESPortfolioResult:
        receipt = self.workspace.load_round_receipt(run_id, missing_ok=True)
        if receipt is not None:
            raise RuntimeError("portfolio round is already sealed; inspect its receipt")
        if candidate_count is None:
            candidate_count = self.contract.first_round_harnesses
        if (
            isinstance(candidate_count, bool)
            or not isinstance(candidate_count, int)
            or not 1 <= candidate_count <= 16
        ):
            raise ValueError("portfolio candidate count must be between one and 16")
        try:
            incumbent = self.workspace.champion()
        except ValueError:
            incumbent = self.workspace.commit(initial_simpletes_harness())
        incumbent_score = self._score_harness(run_id=run_id, harness=incumbent)
        self.reporter(
            f"INCUMBENT {incumbent.sha256[:12]} mean={incumbent_score.utility:.6f} "
            + self._score_line(incumbent_score)
        )
        builder_generator = SequencedClaimedGenerator(
            workspace=self.workspace,
            generator=self.generator,
            run_id=run_id,
            stage_prefix="builder",
            contract_sha256=self.contract_sha256,
        )
        builder = BuilderHarness(
            workspace=self.workspace,
            generator=builder_generator,
            model=self.contract.model,
            inspection_transform=self._portfolio_inspection,
        )
        candidate_scores: dict[str, HarnessScore] = {}

        def gate(
            gate_incumbent: TaskHarnessArtifact,
            candidate: TaskHarnessArtifact,
        ) -> GateDecision:
            if gate_incumbent.sha256 != incumbent.sha256:
                raise ValueError("campaign incumbent changed inside the Gate")
            archive = next(
                item
                for item in reversed(self.workspace.archived_candidates())
                if item["candidate_sha256"] == candidate.sha256
            )
            self.reporter(
                f"HARNESS_START {candidate.sha256[:12]} "
                f"parent={candidate.parent_sha256[:12]} "
                f"source={archive['source']} family={archive['mutation_family']} "
                f"distance={archive['mutation_distance']} "
                f"change={archive['reason'][:240]}"
            )
            score = self._score_harness(run_id=run_id, harness=candidate)
            candidate_scores[candidate.sha256] = score
            delta = score.utility - incumbent_score.utility
            passed = score.all_valid
            credible = passed and delta >= 0.01
            first_failure = next(
                (item for item in score.task_scores if not item.valid),
                None,
            )
            failure_class = (
                first_failure.failure_class
                if first_failure is not None
                else (None if credible else "no_credible_improvement")
            )
            reason = (
                f"mean={score.utility:.6f};delta={delta:+.6f};"
                + self._score_line(score)
            )
            self.reporter(
                f"HARNESS {candidate.sha256[:12]} parent={candidate.parent_sha256[:12]} "
                f"mean={score.utility:.6f} delta={delta:+.6f} "
                f"gate={'credible' if credible else ('passed' if passed else 'failed')} "
                + self._score_line(score)
            )
            return GateDecision(
                evaluator_contract_sha256=self.contract_sha256,
                incumbent_sha256=incumbent.sha256,
                candidate_sha256=candidate.sha256,
                passed=passed,
                credible_improvement=credible,
                utility=score.utility,
                benchmark_scores=tuple(
                    (item.task, item.score) for item in score.task_scores
                ),
                failure_class=failure_class,
                reason=reason[:4_000],
            )

        portfolio = builder.evolve_portfolio(
            run_id=run_id,
            score=incumbent_score.utility,
            feedback=(
                (feedback.strip() + "\n" if feedback and feedback.strip() else "")
                + "Four-task public score: " + self._score_line(incumbent_score)
                + ". Create a distinct one-node prompt/role mutation that preserves the "
                "pinned published-best starting program, the NumPy/SciPy-only runtime, exact "
                "output shapes, parameter budgets, and strict single-code-block output. "
                "Prefer a narrow improvement to the six-parameter U-shape extrapolation; "
                "never request sympy or a wholesale rewrite of a working baseline."
            ),
            candidate_count=candidate_count,
            evaluator_contract_sha256=self.contract_sha256,
            gate_evaluator=gate,
            proposal_attempt_limit=16,
        )
        if len(candidate_scores) != candidate_count:
            raise RuntimeError(
                "portfolio round did not produce the requested durably evaluated Harnesses"
            )
        result = SimpleTESPortfolioResult(
            run_id=run_id,
                contract_sha256=self.contract_sha256,
            incumbent=incumbent_score,
            portfolio=portfolio,
            scores=tuple(candidate_scores[key] for key in sorted(candidate_scores)),
        )
        self.workspace.record_round_receipt(
            run_id=run_id,
            payload={
                "schema_version": 1,
                "kind": "simpletes_scaling_portfolio",
                "run_id": run_id,
                "candidate_count": candidate_count,
                "contract": self.contract.to_dict(),
                "contract_sha256": self.contract_sha256,
                "incumbent": self._harness_score_payload(incumbent_score),
                "portfolio": {
                    "previous_champion_sha256": portfolio.previous_champion_sha256,
                    "next_champion_sha256": portfolio.next_champion_sha256,
                    "promoted_proposal_id": portfolio.promoted_proposal_id,
                    "policy_sha256": portfolio.policy_sha256,
                    "candidates": [
                        {
                            "proposal_id": item.proposal_id,
                            "directive": item.directive.to_dict(),
                            "status": item.status,
                            "candidate_sha256": item.candidate_sha256,
                            "reason": item.reason,
                            "gate": item.gate.to_dict() if item.gate is not None else None,
                        }
                        for item in portfolio.candidates
                    ],
                },
                "scores": [
                    self._harness_score_payload(item) for item in result.scores
                ],
            },
        )
        return result

    def _score_harness(
        self,
        *,
        run_id: str,
        harness: TaskHarnessArtifact,
        task_filter: SimpleTESScalingTask | None = None,
    ) -> HarnessScore:
        task_scores: list[SimpleTESEvaluation] = []
        tasks = (task_filter,) if task_filter is not None else SIMPLETES_TASKS
        for task in tasks:
            solver_id = f"{run_id}-{harness.sha256[:12]}-{task.label}"
            saved = self.workspace.load_solver_result(solver_id, missing_ok=True)
            if saved is None:
                solver_generator = SequencedClaimedGenerator(
                    workspace=self.workspace,
                    generator=self.generator,
                    run_id=run_id,
                    stage_prefix=f"solver-{harness.sha256[:10]}-{task.label}",
                    contract_sha256=self.contract_sha256,
                )
                try:
                    task_run = TaskHarnessRuntime(generator=solver_generator).run(
                        harness,
                        task=task_prompt(self.source_root, task),
                        model=self.contract.model,
                        tools={},
                    )
                except ValueError as exc:
                    task_scores.append(
                        SimpleTESEvaluation(
                            task.label,
                            -1.0,
                            False,
                            "harness_runtime",
                            f"{type(exc).__name__}:{str(exc)[:400]}",
                        )
                    )
                    continue
                self.workspace.record_solver_result(
                    run_id=solver_id,
                    payload={
                        "schema_version": 1,
                        "run_id": solver_id,
                        "contract_sha256": self.contract_sha256,
                        "harness_sha256": harness.sha256,
                        "task": task.label,
                        "candidate": task_run.candidate,
                        "events": [asdict(event) for event in task_run.events],
                    },
                )
                response = task_run.candidate
            else:
                if (
                    saved.get("contract_sha256") != self.contract_sha256
                    or saved.get("harness_sha256") != harness.sha256
                    or saved.get("task") != task.label
                ):
                    raise ValueError("saved scaling solver result binding differs")
                response = saved["candidate"]
            try:
                program = SimpleTESProgram.from_response(response)
            except InvalidCandidate as exc:
                task_scores.append(
                    SimpleTESEvaluation(
                        task.label,
                        -1.0,
                        False,
                        "candidate_contract",
                        str(exc)[:500],
                    )
                )
                continue
            task_scores.append(
                self._claimed_evaluate(
                    run_id=run_id,
                    harness=harness,
                    task=task,
                    program=program,
                )
            )
        return HarnessScore(harness.sha256, tuple(task_scores))

    def _claimed_evaluate(
        self,
        *,
        run_id: str,
        harness: TaskHarnessArtifact,
        task: SimpleTESScalingTask,
        program: SimpleTESProgram,
    ) -> SimpleTESEvaluation:
        stage = f"evaluator-{harness.sha256[:10]}-{task.label}"
        request_sha = hashlib.sha256(
            _canonical_json(
                {
                    "contract_sha256": self.contract_sha256,
                    "harness_sha256": harness.sha256,
                    "task": task.label,
                    "program_sha256": program.sha256,
                    "worker_sha256": hashlib.sha256(
                        self.evaluator.worker_path.read_bytes()
                    ).hexdigest(),
                }
            ).encode()
        ).hexdigest()
        saved = self.workspace.load_operation_result(
            run_id=run_id,
            stage=stage,
            missing_ok=True,
        )
        if saved is not None:
            if saved.get("request_sha256") != request_sha:
                raise ValueError("evaluator operation binding differs")
            return SimpleTESEvaluation(**saved["payload"])
        claim = self.workspace.load_operation_claim(
            run_id=run_id,
            stage=stage,
            missing_ok=True,
        )
        if claim is not None:
            raise IncompleteRoundError(
                f"{stage} started without a durable result; retry is disabled"
            )
        self.workspace.claim_operation(
            run_id=run_id,
            stage=stage,
            request_sha256=request_sha,
        )
        result = self.evaluator.evaluate(task=task, program=program)
        self.workspace.record_operation_result(
            run_id=run_id,
            stage=stage,
            request_sha256=request_sha,
            payload=asdict(result),
        )
        return result

    def _portfolio_inspection(self, inspection: Mapping[str, Any]) -> Mapping[str, Any]:
        public = dict(inspection)
        public["portfolio_archive"] = [
            {
                "candidate_sha256": item["candidate_sha256"],
                "parent_sha256": item["parent_sha256"],
                "mutation_family": item["mutation_family"],
                "reason": item.get("reason", ""),
                "expected_effect": item.get("expected_effect", ""),
            }
            for item in self.workspace.archived_candidates()
            if item.get("portfolio_policy_sha256") is not None
        ]
        return public

    @staticmethod
    def _score_line(score: HarnessScore) -> str:
        return " ".join(f"{item.task}={item.score:.6f}" for item in score.task_scores)

    @staticmethod
    def _harness_score_payload(score: HarnessScore) -> dict[str, Any]:
        return {
            "harness_sha256": score.harness_sha256,
            "utility": score.utility,
            "all_valid": score.all_valid,
            "task_scores": [asdict(item) for item in score.task_scores],
        }


@dataclass(frozen=True)
class SimpleTESHarnessEvolutionRound:
    """One task-specific solver score followed by an optional Builder update."""

    round_index: int
    run_id: str
    task: str
    score: HarnessScore
    builder: BuilderEvolutionResult | None


@dataclass(frozen=True)
class SimpleTESHarnessEvolutionResult:
    """Sealed result for a multi-round Harness lineage."""

    run_id: str
    contract_sha256: str
    rounds: tuple[SimpleTESHarnessEvolutionRound, ...]
    initial_champion_sha256: str
    final_champion_sha256: str
    best_harness_sha256: str
    best_utility: float


class SimpleTESHarnessEvolutionCampaign:
    """Run one task's lower Harness as a sequential eight-round lineage.

    The ordering is intentional: score exactly one solver for the current
    Harness, persist its public trace, then invoke the Builder once using that
    history.  The resulting Harness is scored only in the next round.  This
    prevents a task's eight solver calls from being generated as a batch.
    """

    def __init__(
        self,
        *,
        workspace: HarnessWorkspace,
        source_root: Path,
        generator: Any,
        evaluator: SimpleTESScalingEvaluator,
        task: SimpleTESScalingTask,
        contract: SimpleTESScalingContract | None = None,
        lineage_contract: SimpleTESTaskLineageContract | None = None,
        reporter: Any = print,
    ) -> None:
        self.workspace = workspace
        self.source_root = source_root.resolve()
        self.generator = generator
        self.evaluator = evaluator
        if task not in SIMPLETES_TASKS:
            raise ValueError("task is not part of the pinned SimpleTES contract")
        self.task = task
        self.contract = contract or SimpleTESScalingContract()
        self.lineage_contract = lineage_contract or SimpleTESTaskLineageContract(
            schema_version=1,
            task=task.label,
            base_contract_sha256=self.contract.sha256,
        )
        if self.lineage_contract.task != task.label:
            raise ValueError("lineage contract task differs from campaign task")
        self.reporter = reporter

    def run(
        self,
        *,
        run_id: str,
        round_count: int | None = None,
    ) -> SimpleTESHarnessEvolutionResult:
        if self.workspace.load_round_receipt(run_id, missing_ok=True) is not None:
            raise RuntimeError("Harness evolution is already sealed; inspect its receipt")
        if round_count is None:
            round_count = self.lineage_contract.solver_rounds
        if (
            isinstance(round_count, bool)
            or not isinstance(round_count, int)
            or not 1 <= round_count <= 32
        ):
            raise ValueError("Harness evolution round count must be between one and 32")

        existing_first = self.workspace.load_round_receipt(
            f"{run_id}-round-001", missing_ok=True
        )
        if existing_first is not None:
            initial_sha = str(existing_first.get("harness_sha256"))
        else:
            try:
                initial = self.workspace.champion()
            except ValueError:
                initial = self.workspace.commit(initial_simpletes_harness())
            initial_sha = initial.sha256
        lineage_rounds: list[SimpleTESHarnessEvolutionRound] = []
        feedback: str | None = None
        scorer = SimpleTESPortfolioCampaign(
            workspace=self.workspace,
            source_root=self.source_root,
            generator=self.generator,
            evaluator=self.evaluator,
            contract=self.contract,
            contract_sha256_override=self.lineage_contract.sha256,
            reporter=self.reporter,
        )

        for round_index in range(1, round_count + 1):
            round_id = f"{run_id}-round-{round_index:03d}"
            existing = self.workspace.load_round_receipt(round_id, missing_ok=True)
            if existing is not None:
                restored = self._restore_round(existing, round_id=round_id)
                lineage_rounds.append(restored)
                continue
            if lineage_rounds:
                expected_parent = str(
                    self.workspace.load_round_receipt(
                        lineage_rounds[-1].run_id
                    )["next_harness_sha256"]
                )
                if self.workspace.champion().sha256 != expected_parent:
                    raise ValueError("current Harness does not continue the sealed lineage")
            current = self.workspace.champion()
            self.reporter(
                f"EVOLUTION_ROUND_START {round_index}/{round_count} "
                f"task={self.task.label} harness={current.sha256[:12]}"
            )
            score = scorer._score_harness(
                run_id=round_id,
                harness=current,
                task_filter=self.task,
            )
            self._record_task_trace(round_id=round_id, harness=current, score=score)
            restore = self._restore_to_historical_best(
                round_id=round_id,
                current=current,
                score=score,
                prior_rounds=lineage_rounds,
            )
            task_score = score.task_scores[0]
            feedback = (
                f"Task {self.task.label} round {round_index} public result: "
                f"score={task_score.score:.6f}; valid={task_score.valid}; "
                f"failure_class={task_score.failure_class}; feedback={task_score.feedback}. "
                "Use the complete prior task trace and make one narrow executable Harness mutation."
            )
            if restore is not None:
                feedback += (
                    f" The scored Harness was restored to historical best "
                    f"{restore['restored_sha256']} before this Builder step; "
                    "do not continue from the regressed or invalid Harness."
                )
            builder_result: BuilderEvolutionResult | None = None
            if round_index < round_count:
                builder_generator = SequencedClaimedGenerator(
                    workspace=self.workspace,
                    generator=self.generator,
                    run_id=round_id,
                    stage_prefix="builder",
                    contract_sha256=self.lineage_contract.sha256,
                )
                builder = BuilderHarness(
                    workspace=self.workspace,
                    generator=builder_generator,
                    model=self.contract.model,
                    inspection_transform=self._task_inspection,
                )
                builder_result = builder.evolve_once(
                    score=score.utility,
                    feedback=feedback,
                    probe=self._probe_harness,
                    run_id=round_id,
                )
            round_payload = {
                "schema_version": 1,
                "kind": "simpletes_scaling_harness_evolution_round",
                "run_id": round_id,
                "lineage_run_id": run_id,
                "round_index": round_index,
                "task": self.task.label,
                "harness_sha256": current.sha256,
                "next_harness_sha256": self.workspace.champion().sha256,
                "pre_builder_restore": restore,
                "lineage_contract_sha256": self.lineage_contract.sha256,
                "score": scorer._harness_score_payload(score),
                "builder": (
                    {
                        "status": builder_result.status,
                        "previous_sha256": builder_result.previous_sha256,
                        "candidate_sha256": builder_result.candidate_sha256,
                        "reason": builder_result.reason,
                        "builder_harness_sha256": builder_result.builder_harness_sha256,
                        "events": [asdict(event) for event in builder_result.events],
                    }
                    if builder_result is not None
                    else None
                ),
            }
            self.workspace.record_round_receipt(run_id=round_id, payload=round_payload)
            lineage_rounds.append(
                SimpleTESHarnessEvolutionRound(
                    round_index=round_index,
                    run_id=round_id,
                    task=self.task.label,
                    score=score,
                    builder=builder_result,
                )
            )
            self.reporter(
                f"EVOLUTION_ROUND_END {round_index}/{round_count} task={self.task.label} "
                f"score={task_score.score:.6f} next_harness={self.workspace.champion().sha256[:12]}"
            )

        scored = [item.score for item in lineage_rounds]
        best_round = min(
            lineage_rounds,
            key=lambda item: (-item.score.utility, item.round_index, item.score.harness_sha256),
        )
        final = self.workspace.champion()
        result = SimpleTESHarnessEvolutionResult(
            run_id=run_id,
            contract_sha256=self.lineage_contract.sha256,
            rounds=tuple(lineage_rounds),
            initial_champion_sha256=initial_sha,
            final_champion_sha256=final.sha256,
            best_harness_sha256=best_round.score.harness_sha256,
            best_utility=best_round.score.utility,
        )
        self.workspace.record_round_receipt(
            run_id=run_id,
            payload={
                "schema_version": 1,
                "kind": "simpletes_scaling_harness_evolution",
                "run_id": run_id,
                "task": self.task.label,
                "contract": self.contract.to_dict(),
                "lineage_contract": self.lineage_contract.to_dict(),
                "contract_sha256": self.lineage_contract.sha256,
                "evolution": {
                    "round_count": round_count,
                    "solver_calls_per_round": 1,
                    "builder_calls": self.lineage_contract.builder_updates,
                    "initial_champion_sha256": initial_sha,
                    "final_champion_sha256": final.sha256,
                    "best_harness_sha256": best_round.score.harness_sha256,
                    "best_utility": best_round.score.utility,
                },
                "round_receipt_ids": [item.run_id for item in lineage_rounds],
                "scores": [scorer._harness_score_payload(item) for item in scored],
            },
        )
        return result

    def run_generic(
        self,
        *,
        run_id: str,
        max_rounds: int | None = None,
        patience: int = 3,
        promotion_margin: float = 0.0,
    ) -> Any:
        """Execute this compatibility entry through the reusable campaign core.

        ``run`` remains the sealed legacy receipt path.  New experiments can use
        this method to obtain the benchmark-neutral result and its per-round
        assessments without changing historical receipt semantics.
        """

        from .builder_harness import BuilderHarness
        from .evolution import TaskHarnessEvolutionCampaign

        if max_rounds is None:
            max_rounds = self.lineage_contract.solver_rounds
        adapter = SimpleTESLineageAdapter(
            source_root=self.source_root,
            evaluator=self.evaluator,
            task=self.task,
            contract=self.contract,
        )
        if not self.workspace.current_path.is_file():
            self.workspace.commit(rich_simpletes_harness())
        elif self.workspace.current().spec.schema_version == 1:
            # New generic lineages start with the complete multi-role Harness;
            # historical v1 artifacts remain immutable and replayable.
            self.workspace.commit(rich_simpletes_harness(parent=self.workspace.current()))
        solver_generator = SequencedClaimedGenerator(
            workspace=self.workspace,
            generator=self.generator,
            run_id=run_id,
            stage_prefix="solver",
            contract_sha256=self.lineage_contract.sha256,
        )
        builder_generator = SequencedClaimedGenerator(
            workspace=self.workspace,
            generator=self.generator,
            run_id=run_id,
            stage_prefix="builder",
            contract_sha256=self.lineage_contract.sha256,
        )
        builder = BuilderHarness(
            workspace=self.workspace,
            generator=builder_generator,
            model=self.contract.model,
            inspection_transform=self._task_inspection,
        )
        return TaskHarnessEvolutionCampaign(
            workspace=self.workspace,
            adapter=adapter,
            task_runtime=TaskHarnessRuntime(generator=solver_generator),
            builder=builder,
        ).run(
            run_id=run_id,
            max_rounds=max_rounds,
            patience=patience,
            promotion_margin=promotion_margin,
        )

    def _restore_to_historical_best(
        self,
        *,
        round_id: str,
        current: TaskHarnessArtifact,
        score: HarnessScore,
        prior_rounds: list[SimpleTESHarnessEvolutionRound],
    ) -> dict[str, str] | None:
        """Keep a regressed/invalid Harness from becoming the next parent.

        The scored round remains immutable evidence.  Restoration creates a
        new content-addressed artifact whose spec is byte-identical to the
        best prior valid Harness, with the regressed Harness as its parent.
        This preserves the full lineage while making the next Builder search
        start from a known-good incumbent.
        """

        prior_valid = [item for item in prior_rounds if item.score.all_valid]
        if not prior_valid:
            return None
        best_prior = min(
            prior_valid,
            key=lambda item: (
                -item.score.utility,
                item.round_index,
                item.score.harness_sha256,
            ),
        )
        if current.sha256 == best_prior.score.harness_sha256:
            return None
        if score.all_valid and score.utility >= best_prior.score.utility:
            return None
        restored = TaskHarnessArtifact(
            schema_version=1,
            version=current.version + 1,
            parent_sha256=current.sha256,
            spec=self.workspace.load_artifact(best_prior.score.harness_sha256).spec,
        )
        self.workspace.commit(
            restored,
            owner_run_id=f"{round_id}-restore-best",
        )
        return {
            "reason": "invalid_or_regressed_score",
            "from_sha256": current.sha256,
            "restored_sha256": restored.sha256,
            "historical_best_sha256": best_prior.score.harness_sha256,
        }

    def _task_inspection(self, inspection: Mapping[str, Any]) -> Mapping[str, Any]:
        public = dict(inspection)
        public["task_binding"] = {
            "task": self.task.label,
            "feature_names": list(self.task.feature_names),
            "target_names": list(self.task.target_names),
            "max_param_count": self.task.max_param_count,
        }
        return public

    def _probe_harness(self, candidate: TaskHarnessArtifact) -> bool:
        """Execute the complete proposed Harness without spending a model call."""

        task_text = task_prompt(self.source_root, self.task)
        run = TaskHarnessRuntime(generator=_FixtureHarnessGenerator()).run(
            candidate,
            task=task_text,
            model=self.contract.model,
            tools={},
        )
        return bool(run.candidate.strip())

    def _record_task_trace(
        self,
        *,
        round_id: str,
        harness: TaskHarnessArtifact,
        score: HarnessScore,
    ) -> None:
        solver_id = f"{round_id}-{harness.sha256[:12]}-{self.task.label}"
        solver_result = self.workspace.load_solver_result(solver_id, missing_ok=True)
        if solver_result is None:
            return
        trace_id = f"{round_id}-trace"
        if self.workspace.load_trace(trace_id, missing_ok=True) is not None:
            return
        task_text = task_prompt(self.source_root, self.task)
        task_sha = hashlib.sha256(task_text.encode()).hexdigest()
        request_sha = hashlib.sha256(
            _canonical_json(
                {
                    "contract_sha256": self.lineage_contract.sha256,
                    "harness_sha256": harness.sha256,
                    "task": self.task.label,
                    "solver_id": solver_id,
                }
            ).encode()
        ).hexdigest()
        events = tuple(
            HarnessTraceEvent(**event)
            for event in solver_result.get("events", [])
            if isinstance(event, Mapping)
        )
        item = score.task_scores[0]
        self.workspace.record_trace(
            run_id=trace_id,
            harness_sha256=harness.sha256,
            candidate=str(solver_result["candidate"]),
            task_sha256=task_sha,
            request_sha256=request_sha,
            solver_model=self.contract.model,
            events=events,
            score=item.score,
            feedback=item.feedback,
        )

    def _restore_round(
        self, payload: Mapping[str, Any], *, round_id: str
    ) -> SimpleTESHarnessEvolutionRound:
        if (
            payload.get("kind") != "simpletes_scaling_harness_evolution_round"
            or payload.get("run_id") != round_id
            or payload.get("task") != self.task.label
            or payload.get("lineage_contract_sha256") != self.lineage_contract.sha256
        ):
            raise ValueError("stored lineage round binding differs")
        raw_score = payload.get("score")
        if not isinstance(raw_score, Mapping):
            raise ValueError("stored lineage score is missing")
        score_items = tuple(
            SimpleTESEvaluation(**item)
            for item in raw_score.get("task_scores", [])
            if isinstance(item, Mapping)
        )
        if len(score_items) != 1 or score_items[0].task != self.task.label:
            raise ValueError("stored lineage score task differs")
        score = HarnessScore(
            harness_sha256=str(raw_score.get("harness_sha256")),
            task_scores=score_items,
        )
        current_harness = self.workspace.load_artifact(str(payload["harness_sha256"]))
        if current_harness.sha256 != score.harness_sha256:
            raise ValueError("stored lineage round Harness differs")
        raw_builder = payload.get("builder")
        builder: BuilderEvolutionResult | None = None
        if isinstance(raw_builder, Mapping):
            builder = BuilderEvolutionResult(
                status=str(raw_builder["status"]),
                previous_sha256=str(raw_builder["previous_sha256"]),
                candidate_sha256=raw_builder.get("candidate_sha256"),
                reason=str(raw_builder["reason"]),
                builder_harness_sha256=str(raw_builder["builder_harness_sha256"]),
                events=tuple(
                    BuilderStepEvent(**item)
                    for item in raw_builder.get("events", [])
                    if isinstance(item, Mapping)
                ),
            )
        return SimpleTESHarnessEvolutionRound(
            round_index=int(payload["round_index"]),
            run_id=round_id,
            task=self.task.label,
            score=score,
            builder=builder,
        )
