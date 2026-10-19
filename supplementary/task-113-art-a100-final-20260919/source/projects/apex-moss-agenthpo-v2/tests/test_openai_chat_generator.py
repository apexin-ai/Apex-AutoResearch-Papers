from __future__ import annotations

import io
import json

import pytest

from optimization_lab.openai_chat_generator import (
    OpenAIChatError,
    OpenAIChatRequestConfig,
    OpenAICompatibleChatGenerator,
)


class Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return None


def sse(*events: object, done: bool = True) -> Response:
    lines = [f"data: {json.dumps(event)}\n\n" for event in events]
    if done:
        lines.append("data: [DONE]\n\n")
    return Response("".join(lines).encode("utf-8"))


def test_chat_generator_streams_without_timeout_and_assembles_chunks(monkeypatch) -> None:
    captured: dict[str, object] = {}

    def fake_urlopen(request, timeout):
        captured["request"] = request
        captured["timeout"] = timeout
        return sse(
            {"choices": [{"index": 0, "delta": {"content": "candi"}}]},
            {"choices": [{"index": 0, "delta": {"content": "date"}}]},
            {
                "choices": [],
                "usage": {"prompt_tokens": 3, "completion_tokens": 7},
            },
        )

    monkeypatch.setattr("optimization_lab.openai_chat_generator.urlopen", fake_urlopen)
    generator = OpenAICompatibleChatGenerator(
        OpenAIChatRequestConfig(base_url="https://api.example/v1", api_key="[REDACTED]")
    )

    result = generator.generate("solve", model="gpt-oss-120b")

    payload = json.loads(captured["request"].data)
    assert captured["timeout"] is None
    assert captured["request"].headers["Accept"] == "text/event-stream"
    assert payload["stream"] is True
    assert payload["stream_options"] == {"include_usage": True}
    assert result.raw_response == "candidate"
    assert result.usage == {"prompt_tokens": 3, "completion_tokens": 7}


@pytest.mark.parametrize(
    ("response", "message"),
    [
        (Response(b"{}\n"), "not SSE"),
        (sse({"choices": []}, done=False), "without \\[DONE\\]"),
        (sse({"error": {"message": "private"}}), "reported an error"),
    ],
)
def test_chat_generator_rejects_invalid_or_incomplete_stream(
    monkeypatch, response: Response, message: str
) -> None:
    monkeypatch.setattr(
        "optimization_lab.openai_chat_generator.urlopen",
        lambda request, timeout: response,
    )
    generator = OpenAICompatibleChatGenerator(
        OpenAIChatRequestConfig(base_url="https://api.example/v1", api_key="[REDACTED]")
    )

    with pytest.raises(OpenAIChatError, match=message):
        generator.generate("solve", model="gpt-oss-120b")


def test_chat_generator_allows_only_secure_or_loopback_transport() -> None:
    OpenAIChatRequestConfig(base_url="http://127.0.0.1:18000/v1", api_key="[REDACTED]")
    with pytest.raises(ValueError, match="HTTPS or loopback"):
        OpenAIChatRequestConfig(base_url="http://api.example/v1", api_key="[REDACTED]")
