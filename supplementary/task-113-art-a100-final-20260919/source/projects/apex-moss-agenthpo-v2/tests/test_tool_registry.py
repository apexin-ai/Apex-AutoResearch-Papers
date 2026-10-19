from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from optimization_lab.harness_builder.tool_registry import (
    BoundTool,
    ToolBudgetError,
    ToolOutputLimitError,
    ToolPolicy,
    ToolRegistry,
    ToolTimeoutError,
)


def _read(arguments: dict[str, object]) -> str:
    return Path(str(arguments["path"])).read_text(encoding="utf-8")


def _echo(arguments: dict[str, object]) -> object:
    return arguments.get("text")


def _registry(tmp_path: Path, *, receipt_path: Path | None = None) -> ToolRegistry:
    return ToolRegistry(
        root=tmp_path,
        tools={
            "echo": _echo,
            "read_text": BoundTool.read_only(_read),
        },
        receipt_path=receipt_path,
    )


def _policy(**overrides: object) -> ToolPolicy:
    values: dict[str, object] = {
        "allow": ("echo", "read_text"),
        "deny": (),
        "max_calls": 2,
    }
    values.update(overrides)
    return ToolPolicy(**values)  # type: ignore[arg-type]


def test_registry_rejects_a_tool_outside_the_harness_allowlist(tmp_path: Path) -> None:
    registry = ToolRegistry(root=tmp_path, tools={"read_text": BoundTool.read_only(_read)})
    session = registry.bind(ToolPolicy(allow=("candidate_contract",), deny=(), max_calls=2))
    with pytest.raises(PermissionError, match="not allowed"):
        session.call("read_text", {"path": "task.txt"}, operation_id="r1-tool-0000")


def test_registry_deny_list_overrides_allow_list(tmp_path: Path) -> None:
    session = _registry(tmp_path).bind(_policy(allow=("echo",), deny=("echo",)))
    with pytest.raises(PermissionError, match="not allowed"):
        session.call("echo", {"text": "x"}, operation_id="r1-tool-0000")


@pytest.mark.parametrize(
    "kwargs",
    [
        {"allow": ("echo", 1), "deny": (), "max_calls": 1},
        {"allow": ("echo",), "deny": ("echo", "echo"), "max_calls": 1},
        {"allow": ("echo",), "deny": (), "max_calls": 0},
        {"allow": ("echo",), "deny": (), "max_calls": True},
        {"allow": ("echo",), "deny": (), "max_calls": 1, "max_output_bytes": 0},
        {"allow": ("echo",), "deny": (), "max_calls": 1, "timeout_seconds": 0},
    ],
)
def test_tool_policy_strictly_validates_budget_and_names(kwargs: dict[str, object]) -> None:
    with pytest.raises((TypeError, ValueError)):
        ToolPolicy(**kwargs)  # type: ignore[arg-type]


def test_tool_policy_is_immutable_and_canonicalizes_sequences() -> None:
    policy = ToolPolicy(allow=["echo"], deny=[], max_calls=1)  # type: ignore[arg-type]
    assert policy.allow == ("echo",)
    with pytest.raises((AttributeError, TypeError)):
        policy.max_calls = 2  # type: ignore[misc]


def test_registry_stops_at_the_declared_call_budget(tmp_path: Path) -> None:
    session = _registry(tmp_path).bind(ToolPolicy(allow=("echo",), deny=(), max_calls=1))
    session.call("echo", {"text": "one"}, operation_id="r1-tool-0000")
    with pytest.raises(ToolBudgetError, match="call budget"):
        session.call("echo", {"text": "two"}, operation_id="r1-tool-0001")


def test_registry_budget_is_reset_for_each_bound_session(tmp_path: Path) -> None:
    registry = _registry(tmp_path)
    policy = ToolPolicy(allow=("echo",), deny=(), max_calls=1)
    registry.bind(policy).call("echo", {"text": "one"}, operation_id="r1-tool-0000")
    registry.bind(policy).call("echo", {"text": "two"}, operation_id="r2-tool-0000")


def test_registry_requires_strictly_json_copyable_arguments(tmp_path: Path) -> None:
    session = _registry(tmp_path).bind(_policy())
    with pytest.raises(TypeError, match="JSON"):
        session.call("echo", {"text": object()}, operation_id="r1-tool-0000")
    with pytest.raises(TypeError, match="JSON"):
        session.call("echo", {1: "not a string key"}, operation_id="r1-tool-0001")
    with pytest.raises(TypeError, match="JSON"):
        session.call("echo", {"text": float("nan")}, operation_id="r1-tool-0002")


def test_registry_rejects_paths_outside_the_run_root(tmp_path: Path) -> None:
    session = _registry(tmp_path).bind(ToolPolicy(allow=("read_text",), deny=(), max_calls=1))
    with pytest.raises(PermissionError, match="workspace root"):
        session.call("read_text", {"path": "../secret"}, operation_id="r1-tool-0000")


def test_registry_rejects_absolute_and_symlink_escape_paths(tmp_path: Path) -> None:
    outside = tmp_path.parent / "outside-secret.txt"
    outside.write_text("secret", encoding="utf-8")
    link = tmp_path / "link.txt"
    try:
        link.symlink_to(outside)
    except (OSError, NotImplementedError):
        pytest.skip("symlinks are unavailable on this platform")
    session = _registry(tmp_path).bind(ToolPolicy(allow=("read_text",), deny=(), max_calls=2))
    with pytest.raises(PermissionError, match="workspace root"):
        session.call("read_text", {"path": str(outside)}, operation_id="r1-tool-0000")
    with pytest.raises(PermissionError, match="workspace root"):
        session.call("read_text", {"path": "link.txt"}, operation_id="r1-tool-0001")


def test_registry_receipt_contains_hashes_not_file_contents(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipts.jsonl"
    result = _registry(tmp_path, receipt_path=receipt_path).bind(_policy()).call(
        "echo", {"text": "secret"}, operation_id="r1-tool-0000"
    )
    payload = result.receipt.to_dict()
    assert payload["request_sha256"]
    assert payload["result_sha256"]
    assert "secret" not in json.dumps(payload)
    assert "secret" not in receipt_path.read_text(encoding="utf-8")
    statuses = [json.loads(line)["status"] for line in receipt_path.read_text(encoding="utf-8").splitlines()]
    assert statuses == ["started", "success"]


def test_registry_replays_an_operation_without_invoking_the_tool_twice(tmp_path: Path) -> None:
    calls: list[dict[str, object]] = []

    def counting_echo(arguments: dict[str, object]) -> object:
        calls.append(arguments)
        return arguments["text"]

    registry = ToolRegistry(root=tmp_path, tools={"echo": counting_echo})
    session = registry.bind(ToolPolicy(allow=("echo",), deny=(), max_calls=2))
    first = session.call("echo", {"text": "one"}, operation_id="r1-tool-0000")
    replay = session.call("echo", {"text": "one"}, operation_id="r1-tool-0000")
    assert first.value == replay.value == "one"
    assert len(calls) == 1
    assert session.calls_used == 1


def test_registry_appends_an_error_receipt_without_storing_error_details(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipts.jsonl"

    def fail(_arguments: dict[str, object]) -> object:
        raise RuntimeError("secret error detail")

    session = ToolRegistry(root=tmp_path, tools={"fail": fail}, receipt_path=receipt_path).bind(
        ToolPolicy(allow=("fail",), deny=(), max_calls=1)
    )
    with pytest.raises(RuntimeError, match="secret error detail"):
        session.call("fail", {}, operation_id="r1-tool-0000")
    text = receipt_path.read_text(encoding="utf-8")
    assert "secret error detail" not in text
    assert json.loads(text.splitlines()[-1])["status"] == "error"
    assert json.loads(text.splitlines()[-1])["error_type"] == "RuntimeError"


def test_registry_rejects_output_larger_than_policy_limit(tmp_path: Path) -> None:
    session = _registry(tmp_path).bind(
        ToolPolicy(allow=("echo",), deny=(), max_calls=1, max_output_bytes=8)
    )
    with pytest.raises(ToolOutputLimitError, match="output"):
        session.call("echo", {"text": "this is too large"}, operation_id="r1-tool-0000")


def test_subprocess_tool_is_terminated_when_timeout_expires(tmp_path: Path) -> None:
    tool = BoundTool.subprocess(
        [sys.executable, "-c", "import time; time.sleep(10); print('done')"],
    )
    session = ToolRegistry(root=tmp_path, tools={"sleep": tool}).bind(
        ToolPolicy(allow=("sleep",), deny=(), max_calls=1, timeout_seconds=1)
    )
    with pytest.raises(ToolTimeoutError, match="timed out"):
        session.call("sleep", {}, operation_id="r1-tool-0000")
