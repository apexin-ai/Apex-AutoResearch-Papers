from __future__ import annotations

import json
import os
import re
import subprocess
import uuid
from pathlib import Path
from typing import Any

from optimization_lab.generation import GenerationResult


class CodexExecError(RuntimeError):
    pass


class CodexExecGenerator:
    """Generate one candidate through a fresh, isolated ChatGPT-auth Codex run."""

    def __init__(
        self,
        *,
        work_root: Path,
        executable: str = "codex",
        reasoning_effort: str = "medium",
        output_mode: str = "python_candidate",
    ):
        if output_mode not in {"python_candidate", "plain_text"}:
            raise ValueError("unsupported Codex output mode")
        self.work_root = work_root.resolve()
        self.work_root.mkdir(parents=True, exist_ok=True)
        self.executable = executable
        self.reasoning_effort = reasoning_effort
        self.output_mode = output_mode

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        if not prompt.strip() or not model.strip():
            raise ValueError("Codex prompt and model are required")
        run_id = uuid.uuid4().hex
        field = "code" if self.output_mode == "python_candidate" else "text"
        schema_path = self.work_root / "candidate.schema.json"
        output_path = self.work_root / f"{run_id}.final.json"
        audit_path = self.work_root / f"{run_id}.events.jsonl"
        schema_path.write_text(
            json.dumps(
                {
                    "type": "object",
                    "properties": {field: {"type": "string"}},
                    "required": [field],
                    "additionalProperties": False,
                },
                sort_keys=True,
            ),
            encoding="utf-8",
        )
        command = [
            self.executable,
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--ignore-rules",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--model",
            model,
            "--config",
            f'model_reasoning_effort="{self.reasoning_effort}"',
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
            "--json",
            "-",
        ]
        process = subprocess.run(
            command,
            cwd=self.work_root,
            input=prompt,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            env=self._safe_environment(),
        )
        audit_path.write_text(process.stdout, encoding="utf-8")
        if process.returncode != 0:
            detail = (process.stderr or process.stdout or "Codex exec failed").strip()
            raise CodexExecError(detail[-1200:])
        if not output_path.is_file():
            raise CodexExecError("Codex exec did not produce a final structured output")
        try:
            final = json.loads(output_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise CodexExecError("Codex final output was not valid JSON") from exc
        text = final.get(field) if isinstance(final, dict) else None
        if not isinstance(text, str) or not text.strip():
            raise CodexExecError(f"Codex final output did not contain {field}")
        if self.output_mode == "python_candidate":
            text = self._plain_code(text)
            raw_response = f"```python\n{text.rstrip()}\n```\n"
        else:
            raw_response = text.strip() + "\n"
        return GenerationResult(
            raw_response=raw_response,
            api_cost_usd=0.0,
            provider="codex_chatgpt",
            usage=self._usage(process.stdout),
            audit_log_path=str(audit_path),
        )

    @staticmethod
    def _plain_code(code: str) -> str:
        match = re.fullmatch(r"\s*```(?:python|py)?\s*\n(.*?)```\s*", code, re.DOTALL)
        return match.group(1) if match else code

    @staticmethod
    def _usage(stream: str) -> dict[str, int]:
        for line in reversed(stream.splitlines()):
            try:
                event: Any = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(event, dict) and event.get("type") == "turn.completed":
                usage = event.get("usage")
                if isinstance(usage, dict):
                    return {
                        str(key): int(value)
                        for key, value in usage.items()
                        if isinstance(value, int) and not isinstance(value, bool)
                    }
        return {}

    @staticmethod
    def _safe_environment() -> dict[str, str]:
        allowed = {
            "PATH",
            "HOME",
            "CODEX_HOME",
            "LANG",
            "LC_ALL",
            "SSL_CERT_FILE",
            "SSL_CERT_DIR",
            "HTTP_PROXY",
            "HTTPS_PROXY",
            "ALL_PROXY",
            "NO_PROXY",
            "RUST_LOG",
        }
        return {key: value for key, value in os.environ.items() if key in allowed}
