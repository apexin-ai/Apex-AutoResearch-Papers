from __future__ import annotations

import json
import sys
import types

import pytest

from optimization_lab.openai_generator import (
    OpenAIResponsesError,
    OpenAIResponsesGenerator,
    OpenAIResponsesRequestConfig,
)


class Usage:
    input_tokens = 11
    output_tokens = 7
    total_tokens = 18


class Response:
    output_text = "strict model output"
    usage = Usage()


class Event:
    def __init__(self, event_type: str, response: object | None = None) -> None:
        self.type = event_type
        self.response = response


class Stream:
    def __init__(self, *events: object) -> None:
        self.events = list(events)
        self.closed = False

    def __iter__(self):
        for event in self.events:
            if isinstance(event, BaseException):
                raise event
            yield event

    def close(self) -> None:
        self.closed = True


class Responses:
    def __init__(self, *streams: object) -> None:
        self.streams = list(streams)
        self.calls: list[dict[str, object]] = []

    def create(self, **kwargs: object) -> object:
        self.calls.append(kwargs)
        return self.streams.pop(0)


class Client:
    def __init__(self, *streams: object) -> None:
        self.responses = Responses(*streams)


def completed_stream(response: object | None = None) -> Stream:
    return Stream(Event("response.created"), Event("response.completed", response or Response()))


def test_responses_generator_always_streams_and_closes_stream() -> None:
    stream = completed_stream()
    client = Client(stream)
    generator = OpenAIResponsesGenerator(
        client=client,
        max_output_tokens=2048,
        reasoning_effort="high",
    )

    result = generator.generate("public prompt", model="api-model")

    assert result.raw_response == "strict model output"
    assert result.usage == {"input_tokens": 11, "output_tokens": 7, "total_tokens": 18}
    assert client.responses.calls == [
        {
            "model": "api-model",
            "input": "public prompt",
            "max_output_tokens": 2048,
            "timeout": None,
            "reasoning": {"effort": "high", "summary": "auto"},
            "stream": True,
        }
    ]
    assert stream.closed is True


def test_responses_generator_accepts_materialized_response_from_injected_client() -> None:
    client = Client(Response())
    generator = OpenAIResponsesGenerator(client=client)

    result = generator.generate("public prompt", model="api-model")

    assert result.raw_response == "strict model output"
    assert client.responses.calls[0]["stream"] is True
    assert client.responses.calls[0]["timeout"] is None


def test_responses_generator_rejects_nonstreaming_configuration() -> None:
    with pytest.raises(ValueError, match="must use streaming"):
        OpenAIResponsesRequestConfig(
            max_output_tokens=2048,
            reasoning_effort="high",
            stream=False,
        )
    with pytest.raises(ValueError, match="must use streaming"):
        OpenAIResponsesGenerator(client=Client(), stream=False)


def test_responses_generator_disables_timeout_for_internal_sdk_client(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    seen: list[dict[str, object]] = []
    client = Client(completed_stream())

    def openai(**kwargs: object) -> object:
        seen.append(kwargs)
        return client

    monkeypatch.setitem(sys.modules, "openai", types.SimpleNamespace(OpenAI=openai))

    generator = OpenAIResponsesGenerator()
    generator.generate("public prompt", model="api-model")

    assert seen == [{"timeout": None}]


def test_responses_generator_streams_structured_output() -> None:
    client = Client(completed_stream())
    generator = OpenAIResponsesGenerator(client=client)

    generator.generate_structured(
        "return a proposal",
        model="api-model",
        schema_name="builder_proposal",
        schema={"type": "object", "additionalProperties": False},
    )

    request = client.responses.calls[0]
    assert request["stream"] is True
    assert request["timeout"] is None
    assert request["text"] == {
        "format": {
            "type": "json_schema",
            "name": "builder_proposal",
            "strict": True,
            "schema": {"type": "object", "additionalProperties": False},
        }
    }


def test_responses_generator_fails_closed_without_terminal_event() -> None:
    generator = OpenAIResponsesGenerator(
        client=Client(Stream(Event("response.created"))),
        max_attempts=1,
    )

    with pytest.raises(OpenAIResponsesError, match="output text"):
        generator.generate("public prompt", model="api-model")


def test_responses_generator_retries_stream_iteration_server_error() -> None:
    class HTTPFailure(RuntimeError):
        status_code = 504

    failed = Stream(HTTPFailure("gateway timeout"))
    succeeded = completed_stream()
    client = Client(failed, succeeded)
    generator = OpenAIResponsesGenerator(
        client=client,
        max_attempts=2,
        retry_delay_seconds=0,
        sleeper=lambda _: None,
    )

    result = generator.generate("public prompt", model="api-model")

    assert result.usage["provider_attempts"] == 2
    assert all(call["stream"] is True for call in client.responses.calls)
    assert failed.closed is True and succeeded.closed is True


def test_responses_generator_audit_records_streaming_contract(tmp_path) -> None:
    generator = OpenAIResponsesGenerator(
        client=Client(completed_stream()),
        audit_root=tmp_path / "audit",
    )

    generator.generate("public prompt", model="api-model")

    call_root = next((tmp_path / "audit" / "calls").iterdir())
    started = json.loads((call_root / "started.json").read_text(encoding="utf-8"))
    assert started["request"]["stream"] is True
