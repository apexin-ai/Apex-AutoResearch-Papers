from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from optimization_lab.generation import GenerationResult


class OpenAIChatError(RuntimeError):
    pass


@dataclass(frozen=True)
class OpenAIChatRequestConfig:
    base_url: str
    api_key: [REDACTED]
    temperature: float = 0.7
    max_tokens: int = 32_768
    reasoning_effort: str = "medium"

    def __post_init__(self) -> None:
        parsed = urlparse(self.base_url)
        loopback_http = parsed.scheme == "http" and parsed.hostname in {
            "127.0.0.1",
            "localhost",
            "::1",
        }
        if parsed.scheme != "https" and not loopback_http:
            raise ValueError("OpenAI-compatible base URL must use HTTPS or loopback HTTP")
        if not self.api_key:
            raise ValueError("OpenAI-compatible API key is required")
        if not 0 <= self.temperature <= 2:
            raise ValueError("OpenAI-compatible temperature is invalid")
        if self.max_tokens < 1:
            raise ValueError("OpenAI-compatible request limits are invalid")
        if self.reasoning_effort not in {"low", "medium", "high"}:
            raise ValueError("OpenAI-compatible reasoning effort is invalid")


class OpenAICompatibleChatGenerator:
    """No-retry streaming Chat Completions transport with no client timeout."""

    def __init__(self, config: OpenAIChatRequestConfig) -> None:
        self.config = config

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        if not prompt.strip() or not model.strip():
            raise ValueError("OpenAI-compatible prompt and model are required")
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
            "reasoning_effort": self.config.reasoning_effort,
            "stream": True,
            "stream_options": {"include_usage": True},
        }
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        request = Request(
            self.config.base_url.rstrip("/") + "/chat/completions",
            data=body,
            headers={
                "Authorization": "[REDACTED] " + self.config.api_key,
                "Accept": "text/event-stream",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urlopen(request, timeout=None) as response:
                content, normalized_usage = self._read_sse(response)
        except HTTPError as exc:
            try:
                detail = exc.read().decode("utf-8", errors="replace")
            except Exception:
                detail = ""
            detail = " ".join(detail.split())
            detail = re.sub(r"(?i)(Authorization\s*:\s*Bearer)\s+\S+", r"\1 <redacted>", detail)
            detail = re.sub(r"(?i)\bsk-[A-Za-z0-9_-]{8,}\b", "<redacted>", detail)
            if len(detail) > 400:
                detail = detail[:397] + "..."
            suffix = f": {detail}" if detail else ""
            raise OpenAIChatError(f"chat completion HTTP {exc.code}{suffix}") from exc
        except (URLError, TimeoutError) as exc:
            raise OpenAIChatError(
                f"chat completion transport failed: {type(exc).__name__}"
            ) from exc
        return GenerationResult(
            raw_response=content.strip(),
            provider="openai_compatible_chat",
            usage=normalized_usage,
        )

    @staticmethod
    def _read_sse(response: Any) -> tuple[str, dict[str, int]]:
        parts: list[str] = []
        usage: dict[str, int] = {}
        terminal = False
        try:
            lines = iter(response)
        except TypeError as exc:
            raise OpenAIChatError("chat completion stream is not iterable") from exc
        for raw_line in lines:
            if not isinstance(raw_line, (bytes, bytearray)):
                raise OpenAIChatError("chat completion stream line is invalid")
            try:
                line = bytes(raw_line).decode("utf-8", errors="strict").strip()
            except UnicodeDecodeError as exc:
                raise OpenAIChatError(
                    "chat completion stream is not valid UTF-8"
                ) from exc
            if not line or line.startswith(":"):
                continue
            if not line.startswith("data:"):
                raise OpenAIChatError("chat completion stream is not SSE")
            data = line[5:].strip()
            if data == "[DONE]":
                terminal = True
                break
            try:
                event: Any = json.loads(data)
            except json.JSONDecodeError as exc:
                raise OpenAIChatError("chat completion stream event is invalid JSON") from exc
            if not isinstance(event, dict) or "error" in event:
                raise OpenAIChatError("chat completion stream reported an error")
            event_usage = event.get("usage")
            if isinstance(event_usage, dict):
                usage = {
                    str(key): int(value)
                    for key, value in event_usage.items()
                    if isinstance(value, int)
                    and not isinstance(value, bool)
                    and value >= 0
                }
            choices = event.get("choices", [])
            if not isinstance(choices, list):
                raise OpenAIChatError("chat completion stream choices are invalid")
            for choice in choices:
                if not isinstance(choice, dict) or choice.get("index", 0) != 0:
                    continue
                delta = choice.get("delta", {})
                if not isinstance(delta, dict):
                    raise OpenAIChatError("chat completion stream delta is invalid")
                text = delta.get("content")
                if isinstance(text, str):
                    parts.append(text)
        if not terminal:
            raise OpenAIChatError("chat completion stream ended without [DONE]")
        content = "".join(parts)
        if not content.strip():
            raise OpenAIChatError("chat completion response is empty")
        return content, usage
