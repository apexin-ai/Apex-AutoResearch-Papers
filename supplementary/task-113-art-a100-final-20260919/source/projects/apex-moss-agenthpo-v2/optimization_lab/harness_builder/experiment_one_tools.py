"""Public-only bounded tools for the Experiment 1 Task Harnesses.

The pack performs output-contract and compiler-front-end checks only.  It does
not expose official/public/private evaluators and never executes candidates.
"""

from __future__ import annotations

import ast
import json
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol

from .official_solutions import ALEBenchCodeCodec, EdgeBenchBundleCodec
from .solutions import SolutionContractError
from .tool_registry import ToolPolicy, ToolRegistry, ToolSession


CONTRACT_CHECK_TOOL_ID = "contract_check"
EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID = "python_syntax_check"
ALE_CPP_SYNTAX_CHECK_TOOL_ID = "cpp_syntax_check"

EDGE_PUBLIC_TOOL_IDS = (
    CONTRACT_CHECK_TOOL_ID,
    EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID,
)
ALE_PUBLIC_TOOL_IDS = (
    CONTRACT_CHECK_TOOL_ID,
    ALE_CPP_SYNTAX_CHECK_TOOL_ID,
)

FORBIDDEN_EVALUATOR_TOOL_IDS = frozenset(
    {
        "eval",
        "evaluator",
        "public_eval",
        "private_eval",
        "official_eval",
        "official_evaluator",
        "benchmark_evaluator",
    }
)


class TargetBinding(Protocol):
    task_id: str
    submission_path: str


CompilerRunner = Callable[..., Mapping[str, Any]]


@dataclass(frozen=True)
class ExperimentOneToolPack:
    registry: ToolRegistry
    workspace: Path
    allowed_tool_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        workspace = Path(self.workspace).resolve()
        if not workspace.is_relative_to(self.registry.root):
            raise PermissionError("tool workspace must stay inside root")
        if set(self.allowed_tool_ids) != set(self.registry.definitions):
            raise ValueError("allowed tool IDs must exactly match registry definitions")
        if set(self.allowed_tool_ids) & FORBIDDEN_EVALUATOR_TOOL_IDS:
            raise PermissionError("evaluator tools are forbidden")
        object.__setattr__(self, "workspace", workspace)
        object.__setattr__(self, "allowed_tool_ids", tuple(self.allowed_tool_ids))

    def bind(self, policy: ToolPolicy) -> ToolSession:
        if not set(policy.allow).issubset(self.allowed_tool_ids):
            raise PermissionError("policy contains a tool outside the public tool pack")
        return self.registry.bind(policy, workspace=self.workspace)

    def legacy_operations(
        self, operation_scope: str
    ) -> dict[str, Callable[[Any], Any]]:
        """Expose the same public tools to legacy static ``tool_call`` nodes.

        Schema-2 Agent nodes call :class:`ToolSession` directly. Older V1
        Harnesses, however, receive a callable mapping from
        ``TaskHarnessRuntime``. Returning closures backed by one bounded
        session keeps those historical Harnesses on the public registry, with
        the same receipts and replay policy, instead of silently falling back
        to an unaudited dictionary.
        """

        if not isinstance(operation_scope, str) or not operation_scope.strip():
            raise ValueError("legacy tool operation scope is required")
        session = self.bind(
            ToolPolicy(
                allow=self.allowed_tool_ids,
                deny=(),
                max_calls=128,
            )
        )
        next_call = 0
        operations: dict[str, Callable[[Any], Any]] = {}

        for tool_id in self.allowed_tool_ids:
            def invoke(value: Any, *, _tool_id: str = tool_id) -> Any:
                nonlocal next_call
                call_index = next_call
                next_call += 1
                arguments = (
                    dict(value)
                    if isinstance(value, Mapping)
                    else {"candidate": value}
                )
                result = session.call(
                    _tool_id,
                    arguments,
                    operation_id=f"{operation_scope}.legacy.{call_index:04d}",
                )
                return result.value

            operations[tool_id] = invoke
        return operations


def allowed_experiment_one_tool_ids(benchmark: str) -> tuple[str, ...]:
    normalized = _normalize_benchmark(benchmark)
    return EDGE_PUBLIC_TOOL_IDS if normalized == "edgebench" else ALE_PUBLIC_TOOL_IDS


def build_experiment_one_tool_pack(
    *,
    benchmark: str,
    target: TargetBinding,
    root: Path,
    compiler_runner: CompilerRunner | None = None,
) -> ExperimentOneToolPack:
    """Build a fixed registry rooted wholly beneath the caller's run root."""
    normalized = _normalize_benchmark(benchmark)
    task_id, submission_path = _target_fields(target)
    del task_id  # Validated identity is intentionally not included in tool output.

    root_path = Path(root).expanduser().resolve(strict=False)
    root_path.mkdir(parents=True, exist_ok=True)
    (root_path / "registry").mkdir(parents=True, exist_ok=True)
    workspace = root_path / "workspace"
    workspace.mkdir(parents=True, exist_ok=True)
    receipt_path = root_path / "receipts" / "tool_calls.jsonl"

    if normalized == "edgebench":
        codec = EdgeBenchBundleCodec(required_submit_path=submission_path)
        definitions = {
            CONTRACT_CHECK_TOOL_ID: _contract_check(codec),
            EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID: _python_syntax_check(codec),
        }
    else:
        codec = ALEBenchCodeCodec()
        definitions = {
            CONTRACT_CHECK_TOOL_ID: _contract_check(codec),
            ALE_CPP_SYNTAX_CHECK_TOOL_ID: _cpp_syntax_check(
                codec,
                compiler_runner or _default_cpp_compiler_runner,
                workspace=workspace.resolve(),
            ),
        }
    if set(definitions) & FORBIDDEN_EVALUATOR_TOOL_IDS:
        raise RuntimeError("public tool pack unexpectedly contains an evaluator")
    registry = ToolRegistry(
        root=root_path,
        definitions=definitions,
        receipt_path=receipt_path,
    )
    return ExperimentOneToolPack(
        registry=registry,
        workspace=workspace,
        allowed_tool_ids=allowed_experiment_one_tool_ids(normalized),
    )


def _normalize_benchmark(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("benchmark must be edgebench or alebench")
    normalized = value.strip().lower().replace("-", "")
    if normalized not in {"edgebench", "alebench"}:
        raise ValueError("benchmark must be edgebench or alebench")
    return normalized


def _target_fields(target: TargetBinding) -> tuple[str, str]:
    try:
        task_id = target.task_id
        submission_path = target.submission_path
    except AttributeError as exc:
        raise TypeError("target must provide task_id and submission_path") from exc
    if not isinstance(task_id, str) or not task_id:
        raise TypeError("target task_id must be a non-empty string")
    if not isinstance(submission_path, str) or not submission_path:
        raise TypeError("target submission_path must be a non-empty string")
    return task_id, submission_path


def _strict_candidate(arguments: Mapping[str, Any]) -> str:
    if not isinstance(arguments, Mapping) or set(arguments) != {"candidate"}:
        raise TypeError("tool arguments must contain exactly candidate")
    candidate = arguments["candidate"]
    if not isinstance(candidate, str):
        raise TypeError("candidate must be a string")
    return candidate


def _contract_check(
    codec: EdgeBenchBundleCodec | ALEBenchCodeCodec,
) -> Callable[[Mapping[str, Any]], dict[str, Any]]:
    def check(arguments: Mapping[str, Any]) -> dict[str, Any]:
        candidate = _strict_candidate(arguments)
        try:
            artifact = codec.parse(candidate)
        except SolutionContractError:
            return _invalid_contract()
        return {
            "valid": True,
            "status": "success",
            "artifact_kind": artifact.artifact_kind,
            "compatibility_trace": artifact.compatibility_trace,
        }

    return check


def _python_syntax_check(
    codec: EdgeBenchBundleCodec,
) -> Callable[[Mapping[str, Any]], dict[str, Any]]:
    def check(arguments: Mapping[str, Any]) -> dict[str, Any]:
        candidate = _strict_candidate(arguments)
        try:
            artifact = codec.parse(candidate)
        except SolutionContractError:
            return _invalid_contract()
        canonical_bundle = json.loads(artifact.text)
        source = next(
            entry["content"]
            for entry in canonical_bundle["files"]
            if entry["path"] == codec.required_submit_path
        )
        try:
            ast.parse(source, filename=codec.required_submit_path, mode="exec")
        except (SyntaxError, ValueError, TypeError, MemoryError) as exc:
            result: dict[str, Any] = {
                "valid": False,
                "status": "syntax_error",
                "language": "python",
                "error_type": type(exc).__name__,
            }
            if isinstance(exc, SyntaxError):
                if isinstance(exc.lineno, int):
                    result["line"] = exc.lineno
                if isinstance(exc.offset, int):
                    result["column"] = exc.offset
            return result
        return {"valid": True, "status": "success", "language": "python"}

    return check


def _cpp_syntax_check(
    codec: ALEBenchCodeCodec,
    runner: CompilerRunner,
    *,
    workspace: Path,
) -> Callable[[Mapping[str, Any]], dict[str, Any]]:
    def check(arguments: Mapping[str, Any]) -> dict[str, Any]:
        candidate = _strict_candidate(arguments)
        try:
            artifact = codec.parse(candidate)
        except SolutionContractError:
            return _invalid_contract()
        language = str(artifact.compatibility_trace["language"])
        if language not in {"cpp", "cpp17", "cpp20", "cpp23"}:
            return {
                "valid": False,
                "status": "unsupported_language",
                "language": language,
                "error_type": "UnsupportedLanguage",
            }
        raw_result = runner(
            artifact.text,
            workspace=workspace,
            timeout_seconds=10,
        )
        return _normalize_compiler_result(raw_result, language=language)

    return check


def _normalize_compiler_result(
    result: Mapping[str, Any], *, language: str
) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        raise TypeError("compiler runner must return a mapping")
    status = result.get("status")
    if status == "success":
        return {"valid": True, "status": "success", "language": language}
    if status == "unavailable":
        return {"valid": None, "status": "unavailable", "language": language}
    if status == "failure":
        error_type = result.get("error_type", "CompileError")
        if not isinstance(error_type, str) or not error_type:
            error_type = "CompileError"
        return {
            "valid": False,
            "status": "compile_error",
            "language": language,
            "error_type": error_type,
        }
    raise ValueError("compiler runner returned an unknown status")


def _default_cpp_compiler_runner(
    source: str, *, workspace: Path, timeout_seconds: int
) -> Mapping[str, Any]:
    executable = next(
        (path for name in ("c++", "g++", "clang++") if (path := shutil.which(name))),
        None,
    )
    if executable is None:
        return {"status": "unavailable"}
    try:
        with tempfile.TemporaryDirectory(prefix="cpp-syntax-", dir=workspace) as temporary:
            source_path = Path(temporary) / "candidate.cpp"
            source_path.write_text(source, encoding="utf-8", newline="\n")
            completed = subprocess.run(
                [executable, "-std=c++23", "-fsyntax-only", str(source_path)],
                cwd=temporary,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
                shell=False,
                check=False,
                timeout=timeout_seconds,
            )
    except subprocess.TimeoutExpired:
        return {"status": "failure", "error_type": "CompileTimeout"}
    except OSError:
        return {"status": "unavailable"}
    if completed.returncode == 0:
        return {"status": "success"}
    return {"status": "failure", "error_type": "CompileError"}


def _invalid_contract() -> dict[str, Any]:
    return {
        "valid": False,
        "status": "invalid_contract",
        "error_type": "SolutionContractError",
        "public_error": "candidate does not satisfy the public output contract",
    }


__all__ = [
    "ALE_CPP_SYNTAX_CHECK_TOOL_ID",
    "ALE_PUBLIC_TOOL_IDS",
    "CONTRACT_CHECK_TOOL_ID",
    "CompilerRunner",
    "EDGE_PUBLIC_TOOL_IDS",
    "EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID",
    "ExperimentOneToolPack",
    "FORBIDDEN_EVALUATOR_TOOL_IDS",
    "TargetBinding",
    "allowed_experiment_one_tool_ids",
    "build_experiment_one_tool_pack",
]
