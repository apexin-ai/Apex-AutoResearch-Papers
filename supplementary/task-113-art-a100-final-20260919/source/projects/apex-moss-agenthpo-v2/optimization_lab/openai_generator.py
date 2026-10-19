from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import time
from collections.abc import Mapping
from typing import Any, Callable
from uuid import uuid4

from optimization_lab.generation import GenerationResult


class OpenAIResponsesError(RuntimeError):
    pass


@dataclass(frozen=True)
class OpenAIResponsesRequestConfig:
    max_output_tokens: int
    reasoning_effort: str | None
    max_attempts: int = 2
    retry_delay_seconds: float = 1.0
    stream: bool = True

    def __post_init__(self) -> None:
        if self.max_output_tokens < 1:
            raise ValueError("OpenAI max output tokens must be positive")
        if self.max_attempts < 1:
            raise ValueError("OpenAI max attempts must be positive")
        if self.retry_delay_seconds < 0:
            raise ValueError("OpenAI retry delay cannot be negative")
        if self.stream is not True:
            raise ValueError("OpenAI Responses transport must use streaming")
        if self.reasoning_effort is not None and self.reasoning_effort not in {
            "none",
            "minimal",
            "low",
            "medium",
            "high",
            "xhigh",
            "max",
            "ultra",
        }:
            raise ValueError("unsupported OpenAI reasoning effort")


class OpenAIResponsesGenerator:
    """Pure Responses API transport with no model-native tools enabled.

    Moss executes allowlisted tools in its trusted controller. This adapter only
    obtains model text, which keeps model capability separate from Harness tools.
    """

    def __init__(
        self,
        *,
        client: Any | None = None,
        max_output_tokens: int = 16_384,
        reserved_api_cost_usd: float = 0.0,
        reasoning_effort: str | None = None,
        max_attempts: int = 2,
        retry_delay_seconds: float = 1.0,
        stream: bool = True,
        sleeper: Callable[[float], None] = time.sleep,
        audit_root: Path | None = None,
    ) -> None:
        if max_output_tokens < 1:
            raise ValueError("OpenAI max output tokens must be positive")
        if reserved_api_cost_usd < 0:
            raise ValueError("OpenAI reserved API cost cannot be negative")
        if max_attempts < 1:
            raise ValueError("OpenAI max attempts must be positive")
        if retry_delay_seconds < 0:
            raise ValueError("OpenAI retry delay cannot be negative")
        if stream is not True:
            raise ValueError("OpenAI Responses transport must use streaming")
        if not callable(sleeper):
            raise TypeError("OpenAI retry sleeper must be callable")
        if reasoning_effort is not None and reasoning_effort not in {
            "none",
            "minimal",
            "low",
            "medium",
            "high",
            "xhigh",
            "max",
            "ultra",
        }:
            raise ValueError("unsupported OpenAI reasoning effort")
        if client is None:
            try:
                from openai import OpenAI
            except ImportError as exc:
                raise OpenAIResponsesError(
                    "the openai package is required for the Responses API transport"
                ) from exc
            client = OpenAI(timeout=None)
        self.client = client
        self._request_config = OpenAIResponsesRequestConfig(
            max_output_tokens=max_output_tokens,
            reasoning_effort=reasoning_effort,
            max_attempts=max_attempts,
            retry_delay_seconds=retry_delay_seconds,
            stream=stream,
        )
        self.reserved_api_cost_usd = reserved_api_cost_usd
        self._sleeper = sleeper
        self.audit_root = audit_root.resolve() if audit_root is not None else None

    @property
    def request_config(self) -> OpenAIResponsesRequestConfig:
        return self._request_config

    @property
    def max_output_tokens(self) -> int:
        return self._request_config.max_output_tokens

    @property
    def reasoning_effort(self) -> str | None:
        return self._request_config.reasoning_effort

    def estimated_api_cost_usd(self) -> float:
        return self.reserved_api_cost_usd

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        if self.audit_root is None:
            return self.generate_with_request_config(
                prompt,
                model=model,
                request_config=self._request_config,
            )
        call_id = uuid4().hex
        call_root = self.audit_root / "calls" / call_id
        prompt_sha256 = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        started_at_unix_ns = time.time_ns()
        common = {
            "schema_version": 1,
            "call_id": call_id,
            "model": model,
            "prompt_sha256": prompt_sha256,
            "request": {
                "max_output_tokens": self._request_config.max_output_tokens,
                "reasoning_effort": self._request_config.reasoning_effort,
                "max_attempts": self._request_config.max_attempts,
                "stream": self._request_config.stream,
            },
            "started_at_unix_ns": started_at_unix_ns,
        }
        self._write_audit_once(call_root / "started.json", {**common, "phase": "started"})
        try:
            result = self.generate_with_request_config(
                prompt,
                model=model,
                request_config=self._request_config,
            )
        except Exception as exc:
            summary = str(exc)
            match = re.search(r"provider_attempts=(\d+)", summary)
            provider_attempts = int(match.group(1)) if match is not None else 1
            self._write_audit_once(
                call_root / "failed.json",
                {
                    **common,
                    "phase": "failed",
                    "completed_at_unix_ns": time.time_ns(),
                    "error_type": type(exc).__name__,
                    "error_summary_sha256": hashlib.sha256(
                        summary.encode("utf-8")
                    ).hexdigest(),
                    "provider_attempts": provider_attempts,
                },
            )
            raise

        completed_path = call_root / "completed.json"
        self._write_audit_once(
            completed_path,
            {
                **common,
                "phase": "completed",
                "completed_at_unix_ns": time.time_ns(),
                "output_sha256": hashlib.sha256(
                    result.raw_response.encode("utf-8")
                ).hexdigest(),
                "provider": result.provider,
                "usage": dict(result.usage),
                "provider_attempts": result.usage.get("provider_attempts", 1),
                "api_cost_usd": result.api_cost_usd,
            },
        )
        return GenerationResult(
            raw_response=result.raw_response,
            api_cost_usd=result.api_cost_usd,
            provider=result.provider,
            usage=dict(result.usage),
            audit_log_path=str(completed_path),
        )

    def generate_structured(
        self,
        prompt: str,
        *,
        model: str,
        schema_name: str,
        schema: Mapping[str, Any],
    ) -> GenerationResult:
        """Generate JSON constrained by the provider's Responses schema format."""
        if not isinstance(schema_name, str) or not schema_name.strip():
            raise ValueError("structured output schema name is required")
        if not isinstance(schema, Mapping):
            raise TypeError("structured output schema must be an object")
        return self.generate_with_request_config(
            prompt,
            model=model,
            request_config=self._request_config,
            text_format={
                "type": "json_schema",
                "name": schema_name,
                "strict": True,
                "schema": dict(schema),
            },
        )

    @staticmethod
    def _write_audit_once(path: Path, payload: Mapping[str, Any]) -> None:
        encoded = (
            json.dumps(
                dict(payload),
                ensure_ascii=False,
                allow_nan=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n"
        ).encode("utf-8")
        path.parent.mkdir(parents=True, exist_ok=True)
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
        descriptor = os.open(path, flags, 0o600)
        try:
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(encoded)
                handle.flush()
                os.fsync(handle.fileno())
        except Exception:
            path.unlink(missing_ok=True)
            raise

    def generate_with_request_config(
        self,
        prompt: str,
        *,
        model: str,
        request_config: OpenAIResponsesRequestConfig,
        text_format: Mapping[str, Any] | None = None,
    ) -> GenerationResult:
        if type(request_config) is not OpenAIResponsesRequestConfig:
            raise TypeError("unsupported OpenAI request configuration")
        if not prompt.strip() or not model.strip():
            raise ValueError("OpenAI prompt and model are required")
        request: dict[str, Any] = {
            "model": model,
            "input": prompt,
            "max_output_tokens": request_config.max_output_tokens,
            "timeout": None,
        }
        if request_config.reasoning_effort is not None:
            request["reasoning"] = {"effort": request_config.reasoning_effort, "summary": "auto"}
        if text_format is not None:
            request["text"] = {"format": dict(text_format)}
        request["stream"] = True

        cumulative_usage: dict[str, int] = {}
        for attempt in range(1, request_config.max_attempts + 1):
            try:
                response = self._create_response(request)
            except Exception as exc:
                if attempt < request_config.max_attempts and self._is_retryable_exception(exc):
                    self._sleeper(request_config.retry_delay_seconds)
                    continue
                raise OpenAIResponsesError(
                    self._request_failure_message(exc, provider_attempts=attempt)
                ) from exc

            cumulative_usage = self._add_usage(
                cumulative_usage,
                self._usage(self._field(response, "usage")),
            )
            text = self._output_text(response)
            if text is None:
                if attempt < request_config.max_attempts:
                    self._sleeper(request_config.retry_delay_seconds)
                    continue
                raise OpenAIResponsesError(
                    f"{self._textless_response_message(response)}; provider_attempts={attempt}"
                )

            if attempt > 1:
                cumulative_usage["provider_attempts"] = attempt
            return GenerationResult(
                raw_response=text,
                provider="openai_responses",
                usage=cumulative_usage,
            )
        raise AssertionError("unreachable OpenAI Responses retry state")

    def _create_response(self, request: Mapping[str, Any]) -> Any:
        response_or_stream = self.client.responses.create(**dict(request))
        try:
            events = iter(response_or_stream)
        except TypeError:
            # Some injected SDK-compatible clients materialize the terminal
            # response even when the request correctly requires stream=True.
            # Accept that already-complete object without issuing a second,
            # non-streaming request or changing the no-timeout contract.
            return response_or_stream
        terminal_response = None
        try:
            for event in events:
                if self._field(event, "type") in {
                    "response.completed",
                    "response.incomplete",
                    "response.failed",
                }:
                    terminal_response = self._field(event, "response")
        finally:
            close = self._field(response_or_stream, "close")
            if callable(close):
                close()
        return terminal_response

    @classmethod
    def _is_retryable_exception(cls, exc: Exception) -> bool:
        status_code = cls._status_code(exc)
        if status_code is not None:
            return status_code >= 500 or status_code in {408, 409, 429}
        return type(exc).__name__ in {
            "APIConnectionError",
            "APITimeoutError",
            "ConnectError",
            "ConnectTimeout",
            "ReadError",
            "ReadTimeout",
        }

    @classmethod
    def _request_failure_message(cls, exc: Exception, *, provider_attempts: int) -> str:
        metadata = [
            f"provider_attempts={provider_attempts}",
            f"error_type={type(exc).__name__}",
        ]
        status_code = cls._status_code(exc)
        if status_code is not None:
            metadata.append(f"status_code={status_code}")
        return f"OpenAI Responses request failed ({'; '.join(metadata)})"

    @classmethod
    def _status_code(cls, exc: Exception) -> int | None:
        value = cls._field(exc, "status_code")
        if not isinstance(value, int) or isinstance(value, bool):
            value = cls._field(cls._field(exc, "response"), "status_code")
        if isinstance(value, int) and not isinstance(value, bool) and 100 <= value <= 599:
            return value
        return None

    @classmethod
    def _output_text(cls, response: Any) -> str | None:
        output_text = cls._field(response, "output_text")
        if isinstance(output_text, str) and output_text.strip():
            return output_text.strip()

        parts: list[str] = []
        output = cls._field(response, "output")
        if not isinstance(output, (list, tuple)):
            return None
        for item in output:
            if cls._field(item, "type") != "message":
                continue
            content = cls._field(item, "content")
            if not isinstance(content, (list, tuple)):
                continue
            for part in content:
                if cls._field(part, "type") != "output_text":
                    continue
                text = cls._field(part, "text")
                if isinstance(text, str) and text.strip():
                    parts.append(text.strip())
        return "\n".join(parts) if parts else None

    @classmethod
    def _textless_response_message(cls, response: Any) -> str:
        metadata: list[str] = []
        response_id = cls._field(response, "id")
        status = cls._field(response, "status")
        incomplete_details = cls._field(response, "incomplete_details")
        incomplete_reason = cls._field(incomplete_details, "reason")
        for name, value in (
            ("response_id", response_id),
            ("status", status),
            ("incomplete_reason", incomplete_reason),
        ):
            if isinstance(value, (str, int, float)) and not isinstance(value, bool):
                metadata.append(f"{name}={value}")

        output = cls._field(response, "output")
        if isinstance(output, (list, tuple)):
            item_types = [
                value
                for item in output
                if isinstance((value := cls._field(item, "type")), str) and value
            ]
            if item_types:
                metadata.append(f"output_item_types={','.join(item_types)}")
            content_types: list[str] = []
            for item in output:
                if cls._field(item, "type") != "message":
                    continue
                content = cls._field(item, "content")
                if not isinstance(content, (list, tuple)):
                    continue
                content_types.extend(
                    value
                    for part in content
                    if isinstance((value := cls._field(part, "type")), str) and value
                )
            if content_types:
                metadata.append(f"message_content_types={','.join(content_types)}")

        metadata.extend(f"{name}={value}" for name, value in cls._usage(cls._field(response, "usage")).items())
        suffix = f" ({'; '.join(metadata)})" if metadata else ""
        return f"OpenAI response did not contain output text{suffix}"

    @staticmethod
    def _field(value: Any, name: str) -> Any:
        if isinstance(value, Mapping):
            return value.get(name)
        return getattr(value, name, None)

    @staticmethod
    def _add_usage(total: dict[str, int], current: dict[str, int]) -> dict[str, int]:
        return {
            name: total.get(name, 0) + current.get(name, 0)
            for name in total.keys() | current.keys()
        }

    @classmethod
    def _usage(cls, usage: Any) -> dict[str, int]:
        if usage is None:
            return {}
        names = ("input_tokens", "output_tokens", "total_tokens")
        result: dict[str, int] = {}
        for name in names:
            value = cls._field(usage, name)
            if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
                result[name] = value
        return result
