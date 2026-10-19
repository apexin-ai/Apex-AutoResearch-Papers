"""Small dependency-free API client for AgentHPOBench decision agents."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class APIResponse:
    text: str
    metadata: dict[str, Any]


def _load_env_file() -> None:
    root = Path(__file__).resolve().parents[2]
    candidates = []
    if os.environ.get("AGENTHPOBENCH_ENV_FILE"):
        candidates.append(Path(os.environ["AGENTHPOBENCH_ENV_FILE"]))
    candidates.append(root / ".env")
    for path in candidates:
        if not path.exists():
            continue
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[len("export ") :].strip()
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'\"")
            if key and value and key not in os.environ:
                os.environ[key] = value


def api_backend_enabled() -> bool:
    _load_env_file()
    value = os.environ.get("AUTOREP_AGENT_BACKEND") or os.environ.get("AUTOREP_DECISION_BACKEND")
    return str(value or "").strip().lower() in {
        "api",
        "openai",
        "openai-compatible",
        "anthropic",
        "glm",
        "claude_code",
        "claude-code",
        "codex",
        "codex_cli",
        "codex-cli",
    }


def api_model_name(default: str = "api-model") -> str:
    _load_env_file()
    return os.environ.get("AUTOREP_API_MODEL") or os.environ.get("OPENAI_MODEL") or default


def _read_timeout() -> float:
    return float(os.environ.get("AUTOREP_API_TIMEOUT", "120"))


def _temperature(default: float) -> float:
    return float(os.environ.get("AUTOREP_API_TEMPERATURE", str(default)))


def _max_tokens(default: int) -> int:
    return int(os.environ.get("AUTOREP_API_MAX_TOKENS", str(default)))


def _request_retries() -> int:
    return max(1, int(os.environ.get("AUTOREP_API_RETRIES", "5")))


def _env_flag(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on", "enabled", "enable"}


def _message_content_text(message: dict[str, Any]) -> str:
    content = message.get("content", "")
    if not content and message.get("reasoning_content"):
        content = message.get("reasoning_content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
            else:
                parts.append(str(item))
        return "".join(parts)
    return str(content or "")


def _request_json(url: str, headers: dict[str, str], payload: dict[str, Any]) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    try:
        import requests as requests_client
    except Exception:
        requests_client = None

    last_exc: BaseException | None = None
    for attempt in range(_request_retries()):
        try:
            if requests_client is not None:
                resp = requests_client.post(url, headers=headers, json=payload, timeout=_read_timeout())
                raw = resp.text
                if resp.status_code >= 400:
                    raise RuntimeError(f"API HTTP {resp.status_code}: {raw[:2000]}")
                return resp.json()

            req = urllib.request.Request(url, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=_read_timeout()) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
            return json.loads(raw)
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"API HTTP {exc.code}: {raw[:2000]}") from exc
        except RuntimeError as exc:
            text = str(exc)
            if text.startswith("API HTTP "):
                code_text = text.split(":", 1)[0].split()[-1]
                code = int(code_text) if code_text.isdigit() else 0
                if code not in {408, 409, 429, 500, 502, 503, 504}:
                    raise
            last_exc = exc
        except Exception as exc:
            last_exc = exc
        if attempt + 1 < _request_retries():
            time.sleep(min(2.0 * (attempt + 1), 10.0))
    raise RuntimeError(f"API connection error after {_request_retries()} attempts: {last_exc}") from last_exc

def _provider() -> str:
    _load_env_file()
    value = os.environ.get("AUTOREP_API_PROVIDER") or os.environ.get("AUTOREP_AGENT_BACKEND") or "openai"
    value = value.strip().lower()
    if value in {"api", "openai-compatible"}:
        return "openai"
    return value


def _openai_compatible(prompt: str, *, temperature: float, max_tokens: int) -> APIResponse:
    _load_env_file()
    provider = _provider()
    api_key = [REDACTED]
        os.environ.get("AUTOREP_API_KEY")
        or os.environ.get("OPENAI_API_KEY")
        or (os.environ.get("ZHIPUAI_API_KEY") if provider == "glm" else None)
    )
    if not api_key:
        if provider == "glm":
            raise RuntimeError("Missing ZHIPUAI_API_KEY, OPENAI_API_KEY, or AUTOREP_API_KEY")
        raise RuntimeError("Missing OPENAI_API_KEY or AUTOREP_API_KEY")
    if provider == "glm":
        default_base_url = "https://open.bigmodel.cn/api/paas/v4"
        base_url = (
            os.environ.get("AUTOREP_API_BASE_URL")
            or os.environ.get("ZHIPUAI_BASE_URL")
            or os.environ.get("OPENAI_BASE_URL")
            or default_base_url
        ).rstrip("/")
        model = api_model_name("glm-4-flash")
    else:
        base_url = (os.environ.get("AUTOREP_API_BASE_URL") or os.environ.get("OPENAI_BASE_URL") or "https://api.openai.com/v1").rstrip("/")
        model = api_model_name()
    url = f"{base_url}/chat/completions"
    payload: dict[str, Any] = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if provider == "glm" and not _env_flag("AUTOREP_API_GLM_THINKING", default=False):
        payload["thinking"] = {"type": "disabled"}
    if os.environ.get("AUTOREP_API_EXTRA_BODY"):
        payload.update(json.loads(os.environ["AUTOREP_API_EXTRA_BODY"]))
    headers = {
        "Content-Type": "application/json",
        "Authorization": [REDACTED]"Bearer {api_key}",
    }
    started = time.time()
    data = _request_json(url, headers, payload)
    message = data["choices"][0].get("message") or {}
    text = _message_content_text(message).strip()
    return APIResponse(
        text=text,
        metadata={
            "provider": "openai",
            "api_provider": provider,
            "model": model,
            "base_url": base_url,
            "usage": data.get("usage"),
            "api_seconds": round(time.time() - started, 3),
        },
    )


def _anthropic(prompt: str, *, temperature: float, max_tokens: int) -> APIResponse:
    _load_env_file()
    api_key = [REDACTED]"AUTOREP_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("Missing ANTHROPIC_API_KEY or AUTOREP_API_KEY")
    base_url = (os.environ.get("AUTOREP_API_BASE_URL") or os.environ.get("ANTHROPIC_BASE_URL") or "https://api.anthropic.com").rstrip("/")
    url = f"{base_url}/v1/messages"
    model = api_model_name("claude-3-5-sonnet-latest")
    payload: dict[str, Any] = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    headers = {
        "Content-Type": "application/json",
        "x-api-key": [REDACTED],
        "anthropic-version": os.environ.get("ANTHROPIC_VERSION", "2023-06-01"),
    }
    started = time.time()
    data = _request_json(url, headers, payload)
    parts = data.get("content") or []
    text = "\n".join(part.get("text", "") for part in parts if part.get("type") == "text").strip()
    return APIResponse(
        text=text,
        metadata={
            "provider": "anthropic",
            "model": model,
            "base_url": base_url,
            "usage": data.get("usage"),
            "api_seconds": round(time.time() - started, 3),
        },
    )


def _redact_secret(text: str) -> str:
    for key in (
        "ANTHROPIC_AUTH_TOKEN",
        "ANTHROPIC_API_KEY",
        "AUTOREP_API_KEY",
        "OPENAI_API_KEY",
        "OPENAI_BASE_URL",
        "AUTOREP_API_BASE_URL",
        "ZHIPUAI_API_KEY",
    ):
        value = os.environ.get(key)
        if value:
            text = text.replace(value, "[REDACTED]")
    return text


def _codex_cli(prompt: str, *, temperature: float, max_tokens: int) -> APIResponse:
    """Call Codex CLI as a decision harness and return its final message.

    We keep the experiment execution in AgentHPOBench and use Codex only for the
    intervention decision. This mirrors the Claude Code path while isolating
    results under a separate harness-ablation slug.
    """

    _load_env_file()
    root = Path(__file__).resolve().parents[1]
    api_key = [REDACTED]"OPENAI_API_KEY") or os.environ.get("AUTOREP_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY or AUTOREP_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL") or os.environ.get("AUTOREP_API_BASE_URL")
    codex_bin = (
        os.environ.get("AUTOREP_CODEX_BIN")
        or shutil.which("codex")
        or str(root / "external" / "npm-global" / "bin" / "codex")
    )
    if not codex_bin or not Path(codex_bin).exists():
        raise RuntimeError("Codex CLI not found; install @openai/codex or set AUTOREP_CODEX_BIN")

    env = os.environ.copy()
    env["OPENAI_API_KEY"] = api_key
    if base_url:
        env["OPENAI_BASE_URL"] = base_url
    node_bin = root / "external" / "node-v20.11.1-linux-x64" / "bin"
    npm_bin = root / "external" / "npm-global" / "bin"
    env["PATH"] = f"{node_bin}:{npm_bin}:{env.get('PATH', '')}"

    model = api_model_name(os.environ.get("CODEX_MODEL", "gpt-5.1-codex"))
    timeout = float(os.environ.get("AUTOREP_CODEX_TIMEOUT", str(_read_timeout())))
    retries = max(1, int(os.environ.get("AUTOREP_CODEX_RETRIES", str(_request_retries()))))
    started = time.time()
    last_error = ""
    harness_prompt = (
        "You are acting as an AgentHPOBench intervention decision harness. "
        "Do not modify files, do not run commands, and do not explain outside JSON. "
        "Return exactly one JSON object containing only proposed hyperparameter keys and values.\n\n"
        + prompt
    )

    with tempfile.TemporaryDirectory(prefix="autorep_codex_") as tmp:
        out_path = Path(tmp) / "last_message.txt"
        for attempt in range(retries):
            cmd = [
                codex_bin,
                "exec",
                "--skip-git-repo-check",
                "--ephemeral",
                "--ignore-rules",
                "--sandbox",
                "read-only",
                "--cd",
                str(root),
                "--output-last-message",
                str(out_path),
                "--color",
                "never",
                "--model",
                model,
                "-",
            ]
            try:
                proc = subprocess.run(
                    cmd,
                    cwd=str(root),
                    env=env,
                    input=harness_prompt.encode("utf-8"),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=timeout,
                    check=False,
                )
            except subprocess.TimeoutExpired as exc:
                stdout = (exc.stdout or b"").decode("utf-8", errors="replace")
                stderr = (exc.stderr or b"").decode("utf-8", errors="replace")
                last_error = f"Codex CLI timed out after {timeout}s: {_redact_secret(stdout + stderr)[-2000:]}"
                if attempt + 1 < retries:
                    time.sleep(min(10.0 * (attempt + 1), 30.0))
                    continue
                raise RuntimeError(last_error)

            stdout = proc.stdout.decode("utf-8", errors="replace")
            stderr = proc.stderr.decode("utf-8", errors="replace")
            text = out_path.read_text(errors="replace").strip() if out_path.exists() else stdout.strip()
            if proc.returncode == 0 and text:
                return APIResponse(
                    text=text,
                    metadata={
                        "provider": "codex",
                        "model": model,
                        "base_url": base_url,
                        "api_seconds": round(time.time() - started, 3),
                    },
                )
            last_error = f"Codex CLI failed rc={proc.returncode}: {_redact_secret((stdout + stderr)[-2000:])}"
            if attempt + 1 < retries:
                time.sleep(min(10.0 * (attempt + 1), 30.0))
                continue
            raise RuntimeError(last_error)
    raise RuntimeError(last_error or "Codex CLI failed without response")


def _claude_code_cli(prompt: str, *, temperature: float, max_tokens: int) -> APIResponse:
    """Call Claude Code CLI for Claude-Code OAuth/token gateways.

    Claude Code tokens such as sk-ant-oat... are not regular Anthropic API keys.
    The official CLI handles the required auth path, so this backend shells out
    to `claude -p` and returns the printed result as the decision text.
    """

    _load_env_file()
    token = os.environ.get("ANTHROPIC_AUTH_TOKEN") or os.environ.get("AUTOREP_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not token:
        raise RuntimeError("Missing ANTHROPIC_AUTH_TOKEN, ANTHROPIC_API_KEY, or AUTOREP_API_KEY")
    base_url = (os.environ.get("AUTOREP_API_BASE_URL") or os.environ.get("ANTHROPIC_BASE_URL") or "").rstrip("/")
    if not base_url:
        raise RuntimeError("Missing AUTOREP_API_BASE_URL or ANTHROPIC_BASE_URL")

    root = Path(__file__).resolve().parents[1]
    node_bin = root / "external" / "node-v20.11.1-linux-x64" / "bin"
    npm_bin = root / "external" / "npm-global" / "bin"
    env = os.environ.copy()
    env["ANTHROPIC_BASE_URL"] = base_url
    env["ANTHROPIC_AUTH_TOKEN"] = token
    env.pop("ANTHROPIC_API_KEY", None)
    env["DISABLE_TELEMETRY"] = "1"
    env["DISABLE_ERROR_REPORTING"] = "1"
    env["CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"] = "1"
    env["CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR"] = "1"
    env["PATH"] = f"{node_bin}:{npm_bin}:{env.get('PATH', '')}"

    model = api_model_name("sonnet")
    budget = os.environ.get("AUTOREP_CLAUDE_CODE_MAX_BUDGET_USD", "1.00")
    started = time.time()
    retries = max(1, int(os.environ.get("AUTOREP_CLAUDE_CODE_RETRIES", str(_request_retries()))))
    timeout = float(os.environ.get("AUTOREP_CLAUDE_CODE_TIMEOUT", str(_read_timeout())))
    data: dict[str, Any] | None = None
    last_error = ""
    for attempt in range(retries):
        cmd = [
            "claude",
            "-p",
            prompt,
            "--model",
            model,
            "--output-format",
            "json",
            "--max-budget-usd",
            budget,
            "--tools",
            "",
        ]
        try:
            proc = subprocess.run(
                cmd,
                cwd=str(root),
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            stdout = (exc.stdout or b"").decode("utf-8", errors="replace")
            stderr = (exc.stderr or b"").decode("utf-8", errors="replace")
            last_error = f"Claude Code timed out after {timeout}s: {_redact_secret(stdout + stderr)[-2000:]}"
            if attempt + 1 < retries:
                time.sleep(min(10.0 * (attempt + 1), 30.0))
                continue
            raise RuntimeError(last_error)

        stdout = proc.stdout.decode("utf-8", errors="replace")
        stderr = proc.stderr.decode("utf-8", errors="replace")
        try:
            data = json.loads(stdout)
        except json.JSONDecodeError as exc:
            last_error = f"Claude Code returned non-JSON output: {_redact_secret((stdout + stderr)[-2000:])}"
            if attempt + 1 < retries:
                time.sleep(min(10.0 * (attempt + 1), 30.0))
                continue
            raise RuntimeError(last_error) from exc
        if proc.returncode == 0 and not data.get("is_error"):
            break
        last_error = f"Claude Code failed rc={proc.returncode}: {_redact_secret(json.dumps(data, ensure_ascii=False)[:2000])}"
        if attempt + 1 < retries and any(token in last_error for token in ("ECONNRESET", "Unable to connect", "timed out", "ETIMEDOUT", "ECONNREFUSED")):
            time.sleep(min(10.0 * (attempt + 1), 30.0))
            continue
        raise RuntimeError(last_error)
    if data is None:
        raise RuntimeError(last_error or "Claude Code failed without response")
    text = str(data.get("result") or "").strip()
    return APIResponse(
        text=text,
        metadata={
            "provider": "claude_code",
            "model": model,
            "base_url": base_url,
            "usage": data.get("usage"),
            "api_seconds": round(time.time() - started, 3),
            "total_cost_usd": data.get("total_cost_usd"),
        },
    )


def call_decision_api(prompt: str, *, temperature: float = 0.0, max_tokens: int = 384) -> APIResponse:
    _load_env_file()
    provider = _provider()
    temperature = _temperature(temperature)
    max_tokens = _max_tokens(max_tokens)
    if provider in {"codex", "codex_cli", "codex-cli"}:
        return _codex_cli(prompt, temperature=temperature, max_tokens=max_tokens)
    if provider in {"claude_code", "claude-code"}:
        return _claude_code_cli(prompt, temperature=temperature, max_tokens=max_tokens)
    if provider == "anthropic":
        return _anthropic(prompt, temperature=temperature, max_tokens=max_tokens)
    return _openai_compatible(prompt, temperature=temperature, max_tokens=max_tokens)
