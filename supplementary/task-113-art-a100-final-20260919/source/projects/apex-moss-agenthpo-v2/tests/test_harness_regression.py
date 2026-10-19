"""Regression tests for generated harness state-machine failures."""

import copy
import importlib.util
from pathlib import Path
from types import SimpleNamespace


def _load_v005():
    path = (
        Path(__file__).resolve().parent.parent
        / "harnesses/tddgen_hidden/v005/harness.py"
    )
    spec = importlib.util.spec_from_file_location("tdd_v005", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_v005_returns_tool_result_when_response_has_tool_use():
    module = _load_v005()
    module.MAX_STEPS = 3
    calls = []

    tool = SimpleNamespace(
        type="tool_use",
        name="write_file",
        input={"path": "/work/solution.py", "content": "pass\n"},
        id="tool-1",
    )
    responses = iter([
        SimpleNamespace(
            # The gateway can report end_turn despite returning a tool block.
            stop_reason="end_turn",
            content=[tool],
            usage=SimpleNamespace(input_tokens=1, output_tokens=1),
        ),
        SimpleNamespace(
            stop_reason="end_turn",
            content=[],
            usage=SimpleNamespace(input_tokens=1, output_tokens=1),
        ),
    ])

    class FakeMessages:
        def create(self, **kwargs):
            calls.append(copy.deepcopy(kwargs["messages"]))
            return next(responses)

    module.anthropic.Anthropic = lambda **kwargs: SimpleNamespace(
        messages=FakeMessages()
    )

    def read_file(_input):
        return "def task_func():\n    pass\n"

    def write_file(_input):
        return "ok"

    def run_tests(_input):
        return {"passed": False, "stdout": "", "stderr": ""}

    module.run(
        "/work",
        [],
        {
            "read_file": read_file,
            "write_file": write_file,
            "run_tests": run_tests,
        },
    )

    assert calls[1][-1]["role"] == "user"
    result = calls[1][-1]["content"]
    assert result[0]["type"] == "tool_result"
    assert result[0]["tool_use_id"] == "tool-1"
