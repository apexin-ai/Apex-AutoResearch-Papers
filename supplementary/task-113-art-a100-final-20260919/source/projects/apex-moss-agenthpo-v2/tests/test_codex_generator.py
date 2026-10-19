import json
import subprocess
from pathlib import Path

import pytest

from optimization_lab.codex_generator import CodexExecGenerator, CodexExecError


def test_codex_exec_generator_uses_isolated_structured_ephemeral_run(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    seen: dict[str, object] = {}

    def fake_run(command, **kwargs):
        seen["command"] = command
        seen["kwargs"] = kwargs
        output_path = Path(command[command.index("--output-last-message") + 1])
        output_path.write_text(
            json.dumps({"code": "class ModelNew:\n    pass\n"}), encoding="utf-8"
        )
        return subprocess.CompletedProcess(
            command,
            0,
            stdout=(
                '{"type":"turn.completed","usage":{"input_tokens":12,'
                '"cached_input_tokens":2,"output_tokens":3}}\n'
            ),
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setenv("TOKENROUTER_API_KEY", "must-not-leak")
    monkeypatch.setenv("OPENAI_API_KEY", "must-not-leak")
    generator = CodexExecGenerator(work_root=tmp_path / "isolated")

    result = generator.generate("write one candidate", model="gpt-5.6-sol")

    assert "class ModelNew" in result.raw_response
    assert result.provider == "codex_chatgpt"
    assert result.usage == {
        "input_tokens": 12,
        "cached_input_tokens": 2,
        "output_tokens": 3,
    }
    command = seen["command"]
    assert "--ephemeral" in command
    assert "--ignore-user-config" in command
    assert "--ignore-rules" in command
    assert command[command.index("--sandbox") + 1] == "read-only"
    assert command[command.index("--model") + 1] == "gpt-5.6-sol"
    kwargs = seen["kwargs"]
    assert kwargs["cwd"] == tmp_path / "isolated"
    assert kwargs["input"] == "write one candidate"
    assert "timeout" not in kwargs
    assert "TOKENROUTER_API_KEY" not in kwargs["env"]
    assert "OPENAI_API_KEY" not in kwargs["env"]
    assert Path(result.audit_log_path).is_file()


def test_codex_exec_generator_fails_closed_on_cli_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda command, **kwargs: subprocess.CompletedProcess(
            command, 1, stdout="", stderr="rate limit reached"
        ),
    )
    generator = CodexExecGenerator(work_root=tmp_path / "isolated")

    with pytest.raises(CodexExecError, match="rate limit"):
        generator.generate("write one candidate", model="gpt-5.6-sol")


def test_codex_exec_generator_can_return_plain_harness_text(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def fake_run(command, **kwargs):
        output_path = Path(command[command.index("--output-last-message") + 1])
        output_path.write_text(
            json.dumps({"text": "# Harness v002\n\n1. Inspect feedback.\n"}),
            encoding="utf-8",
        )
        return subprocess.CompletedProcess(
            command,
            0,
            stdout='{"type":"turn.completed","usage":{"input_tokens":5}}\n',
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)
    generator = CodexExecGenerator(
        work_root=tmp_path / "isolated",
        output_mode="plain_text",
    )

    result = generator.generate("revise harness", model="gpt-5.6-sol")

    assert result.raw_response == "# Harness v002\n\n1. Inspect feedback.\n"
    schema = json.loads(
        (tmp_path / "isolated/candidate.schema.json").read_text(encoding="utf-8")
    )
    assert schema["required"] == ["text"]
