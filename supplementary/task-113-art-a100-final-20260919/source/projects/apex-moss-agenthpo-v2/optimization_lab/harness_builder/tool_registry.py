"""A small, bounded and auditable tool registry for Task Harness runs.

The registry deliberately keeps the V1 surface small: tools are either pure
callables accepting one JSON object or explicit subprocess commands.  Every
bound session owns its call budget while the registry owns replay state and
the append-only receipt log.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import threading
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from queue import Empty, Queue
from typing import Any, Callable, Mapping, Sequence


class ToolBudgetError(RuntimeError):
    """The bound session has exhausted its reserved call budget."""


class ToolOutputLimitError(ValueError):
    """A tool returned more JSON bytes than the policy permits."""


class ToolTimeoutError(TimeoutError):
    """A tool did not finish within the policy timeout."""


class ToolReplayError(RuntimeError):
    """A receipt exists for an operation whose result is not replayable here."""


def _json_bytes(value: Any, label: str) -> bytes:
    _validate_json_value(value, label)
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError, OverflowError) as exc:
        raise TypeError(f"{label} must be strictly JSON copyable") from exc


def _validate_json_value(value: Any, label: str) -> None:
    if value is None or isinstance(value, (str, int, bool)):
        return
    if isinstance(value, float):
        if value != value or value in (float("inf"), float("-inf")):
            raise TypeError(f"{label} must be strictly JSON copyable")
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise TypeError(f"{label} must be strictly JSON copyable")
            _validate_json_value(item, label)
        return
    if isinstance(value, (list, tuple)):
        for item in value:
            _validate_json_value(item, label)
        return
    raise TypeError(f"{label} must be strictly JSON copyable")


def _strict_json_copy(value: Any, label: str) -> Any:
    return json.loads(_json_bytes(value, label).decode("utf-8"))


def _sha256(value: Any, label: str) -> str:
    return hashlib.sha256(_json_bytes(value, label)).hexdigest()


@dataclass(frozen=True)
class ToolPolicy:
    """Immutable per-run permissions and resource limits."""

    allow: tuple[str, ...]
    deny: tuple[str, ...]
    max_calls: int
    max_output_bytes: int = 1_048_576
    timeout_seconds: int = 120

    def __post_init__(self) -> None:
        for field_name in ("allow", "deny"):
            value = getattr(self, field_name)
            if isinstance(value, (str, bytes)):
                raise TypeError(f"{field_name} must be a sequence of tool names")
            try:
                names = tuple(value)
            except TypeError as exc:
                raise TypeError(f"{field_name} must be a sequence of tool names") from exc
            if any(not isinstance(name, str) or not name.strip() for name in names):
                raise TypeError(f"{field_name} must contain non-empty string names")
            if len(set(names)) != len(names):
                raise ValueError(f"{field_name} must not contain duplicate names")
            object.__setattr__(self, field_name, names)
        for field_name in ("max_calls", "max_output_bytes", "timeout_seconds"):
            value = getattr(self, field_name)
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{field_name} must be a positive integer")
            if value <= 0:
                raise ValueError(f"{field_name} must be a positive integer")


@dataclass(frozen=True)
class ToolContext:
    """The only filesystem context exposed to a tool."""

    root: Path
    workspace: Path

    def resolve_path(self, path: str | os.PathLike[str]) -> Path:
        return _resolve_workspace_path(self.workspace, path)


@dataclass(frozen=True)
class BoundTool:
    """A callable tool definition with optional path or subprocess semantics."""

    function: Callable[[Mapping[str, Any]], Any] | None = None
    path_arguments: tuple[str, ...] = ()
    command: tuple[str, ...] | None = None

    def __post_init__(self) -> None:
        if (self.function is None) == (self.command is None):
            raise ValueError("a BoundTool must have exactly one function or command")
        if any(not isinstance(name, str) or not name for name in self.path_arguments):
            raise TypeError("path argument names must be non-empty strings")
        object.__setattr__(self, "path_arguments", tuple(self.path_arguments))
        if self.command is not None:
            command = tuple(self.command)
            if not command or any(not isinstance(item, str) or not item for item in command):
                raise TypeError("subprocess command must contain non-empty strings")
            object.__setattr__(self, "command", command)

    @classmethod
    def callable(
        cls,
        function: Callable[[Mapping[str, Any]], Any],
        *,
        path_arguments: Sequence[str] = (),
    ) -> "BoundTool":
        if not callable(function):
            raise TypeError("function must be callable")
        return cls(function=function, path_arguments=tuple(path_arguments))

    @classmethod
    def read_only(cls, function: Callable[[Mapping[str, Any]], Any], *, path_key: str = "path") -> "BoundTool":
        return cls.callable(function, path_arguments=(path_key,))

    @classmethod
    def subprocess(cls, command: Sequence[str]) -> "BoundTool":
        return cls(command=tuple(command))

    def invoke(self, context: ToolContext, arguments: Mapping[str, Any], timeout_seconds: int) -> Any:
        if self.command is not None:
            try:
                completed = subprocess.run(
                    list(self.command),
                    cwd=str(context.workspace),
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    check=False,
                    timeout=timeout_seconds,
                    shell=False,
                )
            except subprocess.TimeoutExpired as exc:
                raise ToolTimeoutError("subprocess tool timed out") from exc
            if completed.returncode != 0:
                raise subprocess.CalledProcessError(
                    completed.returncode, list(self.command), output=completed.stdout, stderr=completed.stderr
                )
            return completed.stdout
        assert self.function is not None
        return _invoke_callable_with_timeout(self.function, arguments, timeout_seconds)


@dataclass(frozen=True)
class ToolCallReceipt:
    operation_id: str
    tool: str
    request_sha256: str
    result_sha256: str | None
    call_index: int
    status: str
    error_type: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "operation_id": self.operation_id,
            "tool": self.tool,
            "request_sha256": self.request_sha256,
            "result_sha256": self.result_sha256,
            "call_index": self.call_index,
            "status": self.status,
            "error_type": self.error_type,
        }


@dataclass(frozen=True)
class ToolCallResult:
    value: Any
    receipt: ToolCallReceipt


class _ReceiptStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = threading.RLock()
        self._final: dict[str, ToolCallReceipt] = {}
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return
        try:
            lines = self.path.read_text(encoding="utf-8").splitlines()
        except OSError:
            return
        for line in lines:
            try:
                payload = json.loads(line)
                if payload.get("status") in {"success", "error"}:
                    receipt = ToolCallReceipt(
                        operation_id=str(payload["operation_id"]),
                        tool=str(payload["tool"]),
                        request_sha256=str(payload["request_sha256"]),
                        result_sha256=payload.get("result_sha256"),
                        call_index=int(payload["call_index"]),
                        status=str(payload["status"]),
                        error_type=payload.get("error_type"),
                    )
                    self._final[receipt.operation_id] = receipt
            except (KeyError, TypeError, ValueError, json.JSONDecodeError):
                continue

    def append(self, payload: Mapping[str, Any]) -> None:
        line = json.dumps(dict(payload), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        with self._lock:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("a", encoding="utf-8", newline="\n") as handle:
                handle.write(line + "\n")

    def start(self, operation_id: str, tool: str, request_sha256: str, call_index: int) -> None:
        self.append(
            {
                "operation_id": operation_id,
                "tool": tool,
                "request_sha256": request_sha256,
                "result_sha256": None,
                "call_index": call_index,
                "status": "started",
                "error_type": None,
            }
        )

    def finish_success(self, operation_id: str, tool: str, request_sha256: str, result_sha256: str, call_index: int) -> ToolCallReceipt:
        receipt = ToolCallReceipt(operation_id, tool, request_sha256, result_sha256, call_index, "success")
        self.append(receipt.to_dict())
        with self._lock:
            self._final[operation_id] = receipt
        return receipt

    def finish_error(self, operation_id: str, tool: str, request_sha256: str, call_index: int, exc: BaseException) -> ToolCallReceipt:
        receipt = ToolCallReceipt(operation_id, tool, request_sha256, None, call_index, "error", type(exc).__name__)
        self.append(receipt.to_dict())
        with self._lock:
            self._final[operation_id] = receipt
        return receipt

    def final(self, operation_id: str) -> ToolCallReceipt | None:
        with self._lock:
            return self._final.get(operation_id)


class ToolRegistry:
    """Registry adapting legacy ``Mapping[str, Callable]`` tools safely."""

    def __init__(
        self,
        root: str | os.PathLike[str],
        tools: Mapping[str, BoundTool | Callable[[Mapping[str, Any]], Any]] | None = None,
        *,
        definitions: Mapping[str, BoundTool | Callable[[Mapping[str, Any]], Any]] | None = None,
        receipt_path: str | os.PathLike[str] | None = None,
    ) -> None:
        if tools is not None and definitions is not None:
            raise TypeError("provide tools or definitions, not both")
        source = tools if tools is not None else definitions
        if source is None:
            source = {}
        self.root = _canonical_root(root)
        self.definitions: dict[str, BoundTool] = {}
        for name, definition in source.items():
            if not isinstance(name, str) or not name:
                raise TypeError("tool names must be non-empty strings")
            if isinstance(definition, BoundTool):
                bound = definition
            elif callable(definition):
                bound = BoundTool.callable(definition)
            else:
                raise TypeError(f"tool definition for {name!r} must be callable or BoundTool")
            self.definitions[name] = bound
        log_path = Path(receipt_path) if receipt_path is not None else self.root / ".tool_receipts.jsonl"
        self._receipts = _ReceiptStore(log_path)
        self._lock = threading.RLock()
        self._replay_results: dict[str, ToolCallResult] = {}

    def bind(
        self,
        policy: ToolPolicy,
        *,
        root: str | os.PathLike[str] | None = None,
        workspace: str | os.PathLike[str] | None = None,
    ) -> "ToolSession":
        if not isinstance(policy, ToolPolicy):
            raise TypeError("policy must be a ToolPolicy")
        session_root = _canonical_root(root if root is not None else self.root)
        if not _is_within(self.root, session_root):
            raise PermissionError("session root must be inside registry root")
        session_workspace = _canonical_root(workspace if workspace is not None else session_root)
        if not _is_within(session_root, session_workspace):
            raise PermissionError("workspace root must be inside session root")
        return ToolSession(self, policy, ToolContext(session_root, session_workspace))


class ToolSession:
    def __init__(self, registry: ToolRegistry, policy: ToolPolicy, context: ToolContext) -> None:
        self._registry = registry
        self.policy = policy
        self.context = context
        self.calls_used = 0

    def call(self, name: str, arguments: Mapping[str, Any], *, operation_id: str) -> ToolCallResult:
        if not isinstance(operation_id, str) or not operation_id or any(char in operation_id for char in "\r\n"):
            raise ValueError("operation_id must be a non-empty single-line string")
        definition = self._registry.definitions.get(name)
        if definition is None or name not in self.policy.allow or name in self.policy.deny:
            raise PermissionError(f"Harness tool is not allowed: {name}")

        copied = _strict_json_copy(arguments, "tool arguments")
        if not isinstance(copied, dict):
            raise TypeError("tool arguments must be a JSON object")
        for key in definition.path_arguments:
            if key not in copied:
                raise TypeError(f"missing path argument: {key}")
            copied[key] = str(_resolve_workspace_path(self.context.workspace, copied[key]))
        request_sha256 = _sha256(copied, "tool arguments")

        with self._registry._lock:
            cached = self._registry._replay_results.get(operation_id)
            if cached is not None:
                if cached.receipt.tool != name or cached.receipt.request_sha256 != request_sha256:
                    raise ToolReplayError("operation_id already belongs to a different request")
                return ToolCallResult(copy.deepcopy(cached.value), cached.receipt)
            existing = self._registry._receipts.final(operation_id)
            if existing is not None:
                if existing.tool != name or existing.request_sha256 != request_sha256:
                    raise ToolReplayError("operation_id already belongs to a different request")
                raise ToolReplayError("operation_id has already completed and cannot be replayed")
            if self.calls_used >= self.policy.max_calls:
                raise ToolBudgetError("Task Harness tool call budget exhausted")
            self.calls_used += 1
            call_index = self.calls_used
            self._registry._receipts.start(operation_id, name, request_sha256, call_index)

        try:
            value = definition.invoke(self.context, copied, self.policy.timeout_seconds)
            bounded = _strict_json_copy(value, "tool output")
            output_bytes = _json_bytes(bounded, "tool output")
            if len(output_bytes) > self.policy.max_output_bytes:
                raise ToolOutputLimitError(
                    f"tool output exceeds {self.policy.max_output_bytes} output bytes"
                )
        except BaseException as exc:
            self._registry._receipts.finish_error(operation_id, name, request_sha256, call_index, exc)
            raise
        result_sha256 = hashlib.sha256(output_bytes).hexdigest()
        receipt = self._registry._receipts.finish_success(
            operation_id, name, request_sha256, result_sha256, call_index
        )
        result = ToolCallResult(bounded, receipt)
        with self._registry._lock:
            self._registry._replay_results[operation_id] = result
        return result


def _canonical_root(value: str | os.PathLike[str]) -> Path:
    path = Path(value).expanduser()
    path.mkdir(parents=True, exist_ok=True)
    return path.resolve()


def _is_within(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _resolve_workspace_path(workspace: Path, value: Any) -> Path:
    if not isinstance(value, str) or not value:
        raise TypeError("path arguments must be non-empty strings")
    candidate = Path(value)
    if candidate.is_absolute():
        resolved = candidate.resolve(strict=False)
    else:
        if ".." in candidate.parts:
            raise PermissionError("path escapes the workspace root")
        resolved = (workspace / candidate).resolve(strict=False)
    if not _is_within(workspace, resolved):
        raise PermissionError("path escapes the workspace root")
    return resolved


def _invoke_callable_with_timeout(
    function: Callable[[Mapping[str, Any]], Any], arguments: Mapping[str, Any], timeout_seconds: int
) -> Any:
    """Run a pure callable on a daemon thread; timeout does not leak a join."""
    result_queue: Queue[tuple[bool, Any]] = Queue(maxsize=1)

    def worker() -> None:
        try:
            result_queue.put((True, function(arguments)))
        except BaseException as exc:
            result_queue.put((False, exc))

    thread = threading.Thread(target=worker, name=f"tool-{uuid.uuid4().hex}", daemon=True)
    thread.start()
    try:
        ok, value = result_queue.get(timeout=timeout_seconds)
    except Empty as exc:
        raise ToolTimeoutError("callable tool timed out") from exc
    if ok:
        return value
    raise value


__all__ = [
    "BoundTool",
    "ToolBudgetError",
    "ToolCallReceipt",
    "ToolCallResult",
    "ToolContext",
    "ToolOutputLimitError",
    "ToolPolicy",
    "ToolRegistry",
    "ToolReplayError",
    "ToolSession",
    "ToolTimeoutError",
]
