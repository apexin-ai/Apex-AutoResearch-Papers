"""Builder source extraction and contract validation (no API calls)."""

from pathlib import Path
from types import SimpleNamespace

import pytest

import builder
import proposer
from harness_source import (
    InvalidHarness,
    parse_generated_harness,
    validate_sandbox_contract,
)

VALID_CODE = '''import anthropic
import json
import os

MODEL = "claude-haiku-4-5"

def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})
    return {"steps": 1, "tokens": 0, "messages": []}
'''


def response(code: str, mechanism: str = "test workflow") -> str:
    return f"MECHANISM: {mechanism}\n```python\n{code}```"


def test_nested_markdown_fence_does_not_truncate_source():
    code = VALID_CODE.replace(
        'tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
        'prompt = """Example:\n```python\npass\n```"""\n'
        '    tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
    )
    parsed, mechanism = parse_generated_harness(response(code))
    assert parsed == code
    assert mechanism == "test workflow"
    compile(parsed, "<generated harness>", "exec")


def test_keyword_dispatch_call_is_rejected():
    invalid = VALID_CODE.replace(
        'tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
        'tool_dispatch["read_file"](**{"path": work_dir + "/solution.py"})',
    )
    with pytest.raises(InvalidHarness, match="one input dict"):
        parse_generated_harness(response(invalid))


def test_string_method_on_run_tests_dict_is_rejected():
    invalid = VALID_CODE.replace(
        'tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
        'def run_tests(path):\n'
        '        return tool_dispatch["run_tests"]({"test_path": path})\n'
        '    test_result = run_tests(work_dir + "/test_solution.py")\n'
        '    test_result.lower()',
    )
    with pytest.raises(InvalidHarness, match="dict returned by run_tests"):
        parse_generated_harness(response(invalid))


def test_wrong_run_tests_input_key_is_rejected():
    invalid = VALID_CODE.replace(
        'tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
        'tool_dispatch["run_tests"]({"path": '
        'work_dir + "/test_solution.py"})',
    )
    with pytest.raises(InvalidHarness, match="test_path"):
        parse_generated_harness(response(invalid))


def test_prompt_cannot_name_extra_python_file():
    invalid = VALID_CODE.replace(
        'tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
        'prompt = "Write a self-test to /tmp/selftest.py"\n'
        '    tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
    )
    with pytest.raises(InvalidHarness, match="selftest.py"):
        parse_generated_harness(response(invalid))


def test_existing_harnesses_satisfy_sandbox_contract():
    root = Path(__file__).resolve().parent.parent
    harnesses = sorted((root / "harnesses").glob("*/*/harness.py"))
    existing = {
        str(path.relative_to(root))
        for path in harnesses
    }
    assert {
        "harnesses/bugfix/v001/harness.py",
        "harnesses/bugfix/builder0/harness.py",
        "harnesses/tddgen/v001/harness.py",
        "harnesses/tddgen/builder0/harness.py",
    } <= existing
    for harness in harnesses:
        validate_sandbox_contract(harness.read_text())


@pytest.mark.parametrize(
    ("replacement", "message"),
    [
        ("import subprocess", "import"),
        ("open(work_dir + '/solution.py')", "open"),
        ("eval('1 + 1')", "eval"),
        ("getattr(os, 'system')('true')", "getattr"),
        ("os.system('true')", "os.system"),
        ("os.path.exists(work_dir)", "os.path.exists"),
    ],
)
def test_sandbox_contract_rejects_unsafe_source(replacement, message):
    invalid = VALID_CODE.replace("import json", replacement)
    with pytest.raises(InvalidHarness, match=message):
        validate_sandbox_contract(invalid)


def test_builder_repairs_invalid_candidate_without_benchmark_feedback(
        tmp_path, monkeypatch):
    (tmp_path / "family_cards").mkdir()
    (tmp_path / "family_cards" / "demo.md").write_text("A task description only.")

    invalid = response(VALID_CODE.replace(
        'tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
        'tool_dispatch["read_file"](**{"path": work_dir + "/solution.py"})',
    ))
    replies = iter([invalid, response(VALID_CODE, "repaired workflow")])
    seen_messages = []

    class FakeMessages:
        def create(self, **kwargs):
            seen_messages.append(kwargs["messages"])
            return SimpleNamespace(
                content=[SimpleNamespace(text=next(replies))]
            )

    fake_client = SimpleNamespace(messages=FakeMessages())
    monkeypatch.setattr(builder, "HERE", tmp_path)
    monkeypatch.setattr(builder.config, "load_env", lambda: {})
    monkeypatch.setattr(
        builder.anthropic, "Anthropic", lambda: fake_client
    )

    output = builder.build("demo")

    assert (tmp_path / "harnesses/demo/builder0/harness.py").read_text() == VALID_CODE
    assert (tmp_path / "harnesses/demo/builder0/MECHANISM.txt").read_text() == (
        "repaired workflow"
    )
    assert output.endswith("harnesses/demo/builder0/harness.py")
    assert len(seen_messages) == 2
    repair_prompt = seen_messages[1][-1]["content"]
    assert "one input dict" in repair_prompt
    assert "benchmark" not in repair_prompt.lower()
    assert len(list(
        (tmp_path / "results/generator_raw/proposer/demo").glob("*.txt")
    )) == 2


def test_proposer_repairs_invalid_candidate_from_contract_error_only(
        tmp_path, monkeypatch):
    family = tmp_path / "demo"
    version = family / "v001"
    version.mkdir(parents=True)
    (version / "harness.py").write_text(VALID_CODE)
    invalid_code = VALID_CODE.replace(
        'tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
        'open(work_dir + "/solution.py")\n'
        '    tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
    )
    replies = iter([
        response(invalid_code),
        response(VALID_CODE, "repaired proposer workflow"),
    ])
    seen_messages = []
    client_options = {}

    class FakeMessages:
        def create(self, **kwargs):
            seen_messages.append(kwargs["messages"])
            return SimpleNamespace(
                content=[SimpleNamespace(text=next(replies))]
            )

    monkeypatch.setattr(proposer.config, "load_env", lambda: {})

    def fake_client(**kwargs):
        client_options.update(kwargs)
        return SimpleNamespace(messages=FakeMessages())

    monkeypatch.setattr(
        proposer.anthropic,
        "Anthropic",
        fake_client,
    )

    code, mechanism = proposer.propose(str(family), "Demo family")

    assert code == VALID_CODE
    assert mechanism == "repaired proposer workflow"
    assert len(seen_messages) == 2
    repair_prompt = seen_messages[1][-1]["content"]
    assert "call to open()" in repair_prompt
    assert "new benchmark information" in repair_prompt
    assert client_options == {"timeout": 300.0, "max_retries": 0}


def test_explicit_candidate_repair_uses_only_candidate_and_contract_error(
        tmp_path, monkeypatch):
    family = tmp_path / "demo"
    family.mkdir()
    candidate = response(
        VALID_CODE.replace(
            'tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
            'prompt = "Write /tmp/selftest.py"\n'
            '    tool_dispatch["read_file"]({"path": work_dir + "/solution.py"})',
        ),
        "invalid self-test workflow",
    )
    repaired = response(VALID_CODE, "contract-only repair")
    seen_messages = []

    class FakeMessages:
        def create(self, **kwargs):
            seen_messages.append(kwargs["messages"])
            return SimpleNamespace(
                content=[SimpleNamespace(text=repaired)]
            )

    monkeypatch.setattr(proposer.config, "load_env", lambda: {})
    monkeypatch.setattr(
        proposer.anthropic,
        "Anthropic",
        lambda **kwargs: SimpleNamespace(messages=FakeMessages()),
    )

    code, mechanism, raw = proposer.repair_candidate(
        str(family), candidate, "selftest.py is forbidden"
    )

    assert code == VALID_CODE
    assert mechanism == "contract-only repair"
    assert raw == repaired
    prompt = seen_messages[0][0]["content"]
    assert candidate in prompt
    assert "selftest.py is forbidden" in prompt
    assert "scores, or traces" in prompt
    assert list((tmp_path / "results/generator_raw/proposer/demo").glob("*.txt"))
