"""Teacher LLM scoring for trace segment relevance.

Uses DeepSeek (OpenAI-compatible API) to label each TraceSegment as "keep" or "drop"
based on its diagnostic value for bug fixing.

Dependencies: openai
"""
from __future__ import annotations

import json
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Optional

from dtd_types import TraceSegment, ScoredSegment, serialize_event

logger = logging.getLogger(__name__)

SCORING_PROMPT_TEMPLATE = """\
You are an expert debugger analyzing execution traces.

## Bug Report
{issue_description}

## Buggy Code
```python
{buggy_code}
```

## Trace Segment ({segment_type})
{formatted_segment}

## Task
Does this trace segment contain diagnostic information useful for fixing the bug?
Consider: Does it show the buggy behavior? Does it reveal the root cause? Does it show relevant state changes?

Respond in JSON: {{"label": "keep" or "drop", "confidence": 0.0-1.0, "reasoning": "..."}}
"""


class TeacherScorer:
    def __init__(
        self,
        api_key: [REDACTED] = None,
        model: str = "deepseek/deepseek-v4-flash",
        base_url: str = "http://47.94.22.126/v1",
        max_concurrent: int = 5,
        temperature: float = 0.1,
    ):
        self.api_key = [REDACTED] or os.environ.get("DEEPSEEK_API_KEY", "")
        self.model = model
        self.base_url = base_url
        self.max_concurrent = max_concurrent
        self.temperature = temperature
        self._client = None

    def _get_client(self):
        if self._client is None:
            from openai import OpenAI
            self._client = OpenAI(api_key=[REDACTED], base_url=self.base_url)
        return self._client

    def format_segment_for_prompt(self, segment: TraceSegment) -> str:
        lines = []
        for ev in segment.events[:50]:
            parts = [f"[{ev.event_type:9s}]", f"{ev.function_name}:{ev.lineno}", f"depth={ev.call_depth}"]
            key_locals = {k: v for k, v in list(ev.locals_snapshot.items())[:5]}
            if key_locals:
                parts.append(f"locals={key_locals}")
            if ev.return_value is not None:
                parts.append(f"-> {repr(ev.return_value)[:100]}")
            if ev.exception_info:
                parts.append(f"EXCEPTION: {ev.exception_info[0]}: {ev.exception_info[1]}")
            lines.append(" ".join(parts))
        if len(segment.events) > 50:
            lines.append(f"... ({len(segment.events) - 50} more events)")
        return "\n".join(lines)

    def score_segment(
        self, issue_description: str, buggy_code: str, segment: TraceSegment
    ) -> ScoredSegment:
        formatted = self.format_segment_for_prompt(segment)
        prompt = SCORING_PROMPT_TEMPLATE.format(
            issue_description=issue_description,
            buggy_code=buggy_code,
            segment_type=segment.segment_type,
            formatted_segment=formatted,
        )

        max_attempts = 3
        result = None
        for attempt in range(max_attempts):
            try:
                client = self._get_client()
                response = client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=self.temperature,
                    max_tokens=256,
                )
                raw = response.choices[0].message.content
                content = raw.strip() if raw else ""
                if not content:
                    if attempt < max_attempts - 1:
                        logger.warning("Empty response for segment %d-%d, retrying (%d/%d)",
                                       segment.start_idx, segment.end_idx, attempt + 1, max_attempts)
                        time.sleep(1.0 * (attempt + 1))
                        continue
                    result = {"label": "error", "confidence": 0.0, "reasoning": "EMPTY_RESPONSE"}
                else:
                    result = self._parse_response(content)
                break
            except Exception as e:
                if attempt < max_attempts - 1:
                    logger.warning("API call failed for segment %d-%d (attempt %d/%d): %s",
                                   segment.start_idx, segment.end_idx, attempt + 1, max_attempts, e)
                    time.sleep(1.0 * (attempt + 1))
                else:
                    logger.warning("API call failed for segment %d-%d after %d attempts: %s",
                                   segment.start_idx, segment.end_idx, max_attempts, e)
                    result = {"label": "error", "confidence": 0.0, "reasoning": f"API_FAILURE: {e}"}

        return ScoredSegment(
            segment=segment,
            label=result["label"],
            confidence=result["confidence"],
            reasoning=result["reasoning"],
        )

    def _parse_response(self, content: str) -> dict:
        try:
            start = content.find("{")
            end = content.rfind("}") + 1
            if start >= 0 and end > start:
                data = json.loads(content[start:end])
                label = data.get("label", "drop")
                confidence = float(data.get("confidence", 0.0))
                reasoning = data.get("reasoning", "")
                if label not in ("keep", "drop"):
                    label = "drop"
                return {
                    "label": label,
                    "confidence": confidence,
                    "reasoning": reasoning,
                }
        except (json.JSONDecodeError, ValueError, KeyError):
            pass
        return {"label": "error", "confidence": 0.0, "reasoning": f"PARSE_FAILURE: {content[:100]}"}

    def score_batch(
        self,
        issue_description: str,
        buggy_code: str,
        segments: List[TraceSegment],
        max_concurrent: Optional[int] = None,
    ) -> List[ScoredSegment]:
        concurrency = max_concurrent or self.max_concurrent
        results: List[Optional[ScoredSegment]] = [None] * len(segments)

        with ThreadPoolExecutor(max_workers=concurrency) as executor:
            future_to_idx = {}
            for i, seg in enumerate(segments):
                future = executor.submit(self.score_segment, issue_description, buggy_code, seg)
                future_to_idx[future] = i
                if (i + 1) % concurrency == 0:
                    time.sleep(0.5)

            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    results[idx] = future.result()
                except Exception as e:
                    logger.error("Scoring failed for segment %d: %s", idx, e)
                    results[idx] = ScoredSegment(
                        segment=segments[idx],
                        label="drop",
                        confidence=0.0,
                        reasoning=f"Scoring error: {e}",
                    )

        return [r for r in results if r is not None]

    def filter_segments(
        self, scored: List[ScoredSegment], threshold: float = 0.5
    ) -> List[ScoredSegment]:
        return [s for s in scored if s.label == "keep" and s.confidence >= threshold]


if __name__ == "__main__":
    import time as _time
    from dtd_types import TraceEvent, TraceSegment

    events = [
        TraceEvent("call", "divide", "math_utils.py", 10, {"a": 6, "b": 0}, 2, _time.time()),
        TraceEvent("exception", "divide", "math_utils.py", 11, {}, 2, _time.time(),
                   exception_info=("ZeroDivisionError", "division by zero", "")),
        TraceEvent("return", "divide", "math_utils.py", 11, {}, 2, _time.time()),
    ]
    seg = TraceSegment(
        segment_type="exception_chain",
        events=events,
        start_idx=5,
        end_idx=7,
        metadata={"exception_type": "ZeroDivisionError", "raise_line": 11, "catch_line": 15},
    )

    scorer = TeacherScorer()
    formatted = scorer.format_segment_for_prompt(seg)
    print("=== Formatted segment ===")
    print(formatted)

    prompt = SCORING_PROMPT_TEMPLATE.format(
        issue_description="Division by zero when input list contains value 3",
        buggy_code="def divide(a, b):\n    return a / b",
        segment_type=seg.segment_type,
        formatted_segment=formatted,
    )
    print("\n=== Full prompt ===")
    print(prompt)

    if scorer.api_key:
        print("\n=== API call ===")
        result = scorer.score_segment(
            "Division by zero when input list contains value 3",
            "def divide(a, b):\n    return a / b",
            seg,
        )
        print(f"Label: {result.label}, Confidence: {result.confidence}")
        print(f"Reasoning: {result.reasoning}")
    else:
        print("\nNo API key set, skipping live scoring demo.")
