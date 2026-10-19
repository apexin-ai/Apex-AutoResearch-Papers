from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import pytest

from optimization_lab.harness_builder.experiment_one_tools import (
    ALE_CPP_SYNTAX_CHECK_TOOL_ID,
    CONTRACT_CHECK_TOOL_ID,
    EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID,
    ExperimentOneToolPack,
    FORBIDDEN_EVALUATOR_TOOL_IDS,
    allowed_experiment_one_tool_ids,
    build_experiment_one_tool_pack,
)
from optimization_lab.harness_builder.tool_registry import ToolPolicy, ToolRegistry


def _edge_candidate(source: str, *, path: str = "solution.py") -> str:
    return json.dumps(
        {
            "schema_version": 1,
            "files": [{"path": path, "type": "file", "content": source}],
        }
    )


@dataclass(frozen=True)
class Target:
    task_id: str
    submission_path: str


def _session(
    target: str,
    tmp_path: Path,
    *,
    compiler_runner=None,
):
    root = tmp_path / "root"
    pack = build_experiment_one_tool_pack(
        benchmark=target,
        target=Target("public-task", "solution.py" if target == "edgebench" else "main.cpp"),
        root=root,
        compiler_runner=compiler_runner,
    )
    policy = ToolPolicy(
        allow=allowed_experiment_one_tool_ids(target),
        deny=tuple(FORBIDDEN_EVALUATOR_TOOL_IDS),
        max_calls=8,
        max_output_bytes=16_384,
        timeout_seconds=2,
    )
    return pack, pack.bind(policy)


@pytest.mark.parametrize(
    ("target", "expected"),
    [
        ("edgebench", {CONTRACT_CHECK_TOOL_ID, EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID}),
        ("alebench", {CONTRACT_CHECK_TOOL_ID, ALE_CPP_SYNTAX_CHECK_TOOL_ID}),
    ],
)
def test_factory_builds_fixed_public_only_registries(
    target: str, expected: set[str], tmp_path: Path
) -> None:
    pack, _session_value = _session(target, tmp_path)
    assert isinstance(pack, ExperimentOneToolPack)
    assert isinstance(pack.registry, ToolRegistry)
    assert set(pack.registry.definitions) == expected
    assert set(pack.allowed_tool_ids) == expected
    assert not set(pack.registry.definitions) & FORBIDDEN_EVALUATOR_TOOL_IDS


@pytest.mark.parametrize("target", ["edgebench", "alebench"])
def test_allowed_ids_never_include_evaluator_tools(target: str) -> None:
    ids = set(allowed_experiment_one_tool_ids(target))
    assert not ids & FORBIDDEN_EVALUATOR_TOOL_IDS
    for forbidden in ("evaluator", "public_eval", "private_eval"):
        assert forbidden not in ids


def test_edge_contract_check_accepts_a_public_bundle_without_returning_source(tmp_path: Path) -> None:
    secret = "[REDACTED]"
    _registry_value, session = _session("edgebench", tmp_path)
    result = session.call(
        CONTRACT_CHECK_TOOL_ID,
        {"candidate": _edge_candidate(f"print('{secret}')\n")},
        operation_id="edge-contract-0000",
    ).value
    assert result["valid"] is True
    assert result["artifact_kind"] == "edgebench_file_bundle_v1"
    assert "compatibility_trace" in result
    assert secret not in json.dumps(result, sort_keys=True)


def test_contract_check_rejects_invalid_shape_and_sanitizes_format_errors(tmp_path: Path) -> None:
    _registry_value, session = _session("edgebench", tmp_path)
    with pytest.raises(TypeError, match="candidate"):
        session.call(
            CONTRACT_CHECK_TOOL_ID,
            {"candidate": "x", "extra": "no"},
            operation_id="edge-contract-0000",
        )
    result = session.call(
        CONTRACT_CHECK_TOOL_ID,
        {"candidate": "PRIVATE_BODY_NOT_JSON"},
        operation_id="edge-contract-0001",
    ).value
    assert result["valid"] is False
    assert result["status"] == "invalid_contract"
    assert result["error_type"] == "SolutionContractError"
    assert "PRIVATE_BODY_NOT_JSON" not in json.dumps(result, sort_keys=True)


def test_edge_python_syntax_check_uses_required_submission_source_only(tmp_path: Path) -> None:
    secret = "[REDACTED]"
    _registry_value, session = _session("edgebench", tmp_path)
    valid = session.call(
        EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID,
        {"candidate": _edge_candidate(f"VALUE = '{secret}'\n")},
        operation_id="edge-syntax-0000",
    ).value
    invalid = session.call(
        EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID,
        {"candidate": _edge_candidate("def broken(:\n    pass\n")},
        operation_id="edge-syntax-0001",
    ).value
    assert valid == {"valid": True, "status": "success", "language": "python"}
    assert invalid["valid"] is False
    assert invalid["status"] == "syntax_error"
    assert invalid["error_type"] == "SyntaxError"
    assert "def broken" not in json.dumps(invalid, sort_keys=True)
    assert secret not in json.dumps(valid, sort_keys=True)


def test_ale_contract_check_accepts_fenced_cpp_without_returning_source(tmp_path: Path) -> None:
    secret = "[REDACTED]"
    _registry_value, session = _session("alebench", tmp_path)
    result = session.call(
        CONTRACT_CHECK_TOOL_ID,
        {"candidate": f"```cpp23\n// {secret}\nint main() {{}}\n```"},
        operation_id="ale-contract-0000",
    ).value
    assert result["valid"] is True
    assert result["artifact_kind"] == "alebench_source_cpp23"
    assert result["compatibility_trace"]["language"] == "cpp23"
    assert secret not in json.dumps(result, sort_keys=True)


@pytest.mark.parametrize(
    ("compiler_result", "expected"),
    [
        ({"status": "success"}, {"valid": True, "status": "success", "language": "cpp23"}),
        ({"status": "failure", "error_type": "CompileError"}, {"valid": False, "status": "compile_error", "language": "cpp23", "error_type": "CompileError"}),
        ({"status": "unavailable"}, {"valid": None, "status": "unavailable", "language": "cpp23"}),
    ],
)
def test_ale_cpp_syntax_check_reports_success_failure_or_unavailable(
    compiler_result: dict[str, object], expected: dict[str, object], tmp_path: Path
) -> None:
    calls: list[tuple[str, Path, int]] = []

    def runner(source: str, *, workspace: Path, timeout_seconds: int) -> dict[str, object]:
        calls.append((source, workspace, timeout_seconds))
        return compiler_result

    root = tmp_path / "root"
    _registry_value, session = _session("alebench", tmp_path, compiler_runner=runner)
    candidate = "```cpp23\nint main() { return 0; }\n```"
    result = session.call(
        ALE_CPP_SYNTAX_CHECK_TOOL_ID,
        {"candidate": candidate},
        operation_id=f"ale-compile-{compiler_result['status']}",
    ).value
    assert result == expected
    assert calls == [("int main() { return 0; }\n", (root / "workspace").resolve(), 10)]
    assert candidate not in json.dumps(result, sort_keys=True)


def test_receipts_and_compiler_workspace_stay_inside_caller_root(tmp_path: Path) -> None:
    root = tmp_path / "root"
    pack = build_experiment_one_tool_pack(
        benchmark="edgebench",
        target=Target("public-task", "solution.py"),
        root=root,
    )
    session = pack.bind(
        ToolPolicy(
            allow=allowed_experiment_one_tool_ids("edgebench"), deny=(), max_calls=1
        )
    )
    session.call(
        CONTRACT_CHECK_TOOL_ID,
        {"candidate": _edge_candidate("pass\n")},
        operation_id="edge-contract-0000",
    )
    receipt_path = root / "receipts" / "tool_calls.jsonl"
    assert receipt_path.is_file()
    assert pack.workspace == (root / "workspace").resolve()
    assert (root / "registry").is_dir()
    assert receipt_path.resolve().is_relative_to(root.resolve())


def test_legacy_operations_use_the_public_registry_and_write_receipts(
    tmp_path: Path,
) -> None:
    pack, _session_value = _session("edgebench", tmp_path)
    operations = pack.legacy_operations("cross-cell-0000-solver")

    result = operations[CONTRACT_CHECK_TOOL_ID](_edge_candidate("pass\n"))

    assert result["valid"] is True
    receipt_path = tmp_path / "root" / "receipts" / "tool_calls.jsonl"
    receipt_text = receipt_path.read_text(encoding="utf-8")
    assert "cross-cell-0000-solver.legacy.0000" in receipt_text
