"""
Constraint extractor: extract structured math constraints from LLM reasoning traces.
Input: reasoning trace string
Output: list of constraint dicts with type, expression, z3_formula, source_step
Dependencies: json, re, openai (optional)
"""
from __future__ import annotations

import asyncio
import json
import logging
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

EXTRACTION_PROMPT = '''You are a mathematical constraint extractor. Given a step-by-step reasoning trace for a math problem, extract all mathematical constraints (equations, inequalities, predicates) that appear in the reasoning.

**Variable naming rules:**
- Use standard variable names: x, y, z, a, b, c, n, m, k
- If the problem names specific quantities (e.g., "length", "width"), use descriptive short names (e.g., l, w)
- Be consistent: the same quantity must use the same variable name across all constraints
- Use the SAME variable names that appear in the reasoning trace

**Output format:** Return a JSON object with this exact structure:
```json
{{
  "constraints": [
    {{
      "type": "equation|inequality|predicate",
      "expression": "human-readable expression, e.g. x + y == 14",
      "z3_formula": "Z3-compatible Python expression, e.g. x + y == 14",
      "source_step": 3
    }}
  ],
  "answer": "the final numerical answer from this trace",
  "variables": ["x", "y"]
}}
```

**Constraint types:**
- equation: equality (==), e.g. "x + y == 14"
- inequality: <, >, <=, >=, e.g. "x > 0"
- predicate: logical assertion, e.g. "x % 2 == 0" (x is even)

**Z3 formula rules:**
- Use Python syntax: ==, !=, <, >, <=, >=, +, -, *, /, **
- Division: use / (Z3 Real division)
- Integer modulo: use %
- All variables are Real by default

**Example 1:**
Trace: "Let the two numbers be x and y. We know x + y = 14 and x * y = 48. From x + y = 14, y = 14 - x. Substituting: x(14-x) = 48, 14x - x^2 = 48, x^2 - 14x + 48 = 0. Factoring: (x-6)(x-8) = 0. So x = 6 or x = 8. The answer is \\\\boxed{{6}}."

Output:
```json
{{
  "constraints": [
    {{"type": "equation", "expression": "x + y == 14", "z3_formula": "x + y == 14", "source_step": 1}},
    {{"type": "equation", "expression": "x * y == 48", "z3_formula": "x * y == 48", "source_step": 1}},
    {{"type": "equation", "expression": "y == 14 - x", "z3_formula": "y == 14 - x", "source_step": 2}},
    {{"type": "equation", "expression": "x**2 - 14*x + 48 == 0", "z3_formula": "x**2 - 14*x + 48 == 0", "source_step": 3}}
  ],
  "answer": "6",
  "variables": ["x", "y"]
}}
```

**Example 2:**
Trace: "A rectangle has perimeter 30 and area 50. Let length = l, width = w. Then 2(l+w) = 30, so l+w = 15. Also l*w = 50. We need l - w. (l-w)^2 = (l+w)^2 - 4lw = 225 - 200 = 25. So l-w = 5. The answer is \\\\boxed{{5}}."

Output:
```json
{{
  "constraints": [
    {{"type": "equation", "expression": "2*(l + w) == 30", "z3_formula": "2*(l + w) == 30", "source_step": 1}},
    {{"type": "equation", "expression": "l + w == 15", "z3_formula": "l + w == 15", "source_step": 2}},
    {{"type": "equation", "expression": "l * w == 50", "z3_formula": "l * w == 50", "source_step": 2}},
    {{"type": "equation", "expression": "(l - w)**2 == 25", "z3_formula": "(l - w)**2 == 25", "source_step": 3}}
  ],
  "answer": "5",
  "variables": ["l", "w"]
}}
```

Now extract constraints from this trace:

{trace}

Return ONLY the JSON object, no other text.'''


class LLMBackend(ABC):
    """LLM 调用抽象基类"""
    @abstractmethod
    def call(self, prompt: str) -> str:
        ...


class VLLMBackend(LLMBackend):
    """通过 OpenAI-compatible API 调用本地 vLLM"""

    def __init__(self, base_url: str = "http://localhost:8000/v1", model: str | None = None):
        from openai import OpenAI, AsyncOpenAI
        self.client = OpenAI(base_url=base_url, api_key="[REDACTED]")
        self.async_client = AsyncOpenAI(base_url=base_url, api_key="[REDACTED]")
        if model is None:
            models = self.client.models.list()
            self.model = models.data[0].id
        else:
            self.model = model

    def call(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=2048,
        )
        return response.choices[0].message.content or ""

    async def async_call(self, prompt: str) -> str:
        response = await self.async_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=2048,
        )
        return response.choices[0].message.content or ""

    def batch_call(self, prompts: list[str]) -> list[str]:
        """批量调用，用 asyncio 并发"""
        async def _run():
            tasks = [self.async_call(p) for p in prompts]
            return await asyncio.gather(*tasks)
        try:
            loop = asyncio.get_running_loop()
            import nest_asyncio
            nest_asyncio.apply()
            return loop.run_until_complete(_run())
        except RuntimeError:
            return asyncio.run(_run())


class MockLLM(LLMBackend):
    """Returns pre-set responses for testing."""

    def __init__(self, responses: list[str] | None = None):
        self._responses = responses or []
        self._idx = 0

    def call(self, prompt: str) -> str:
        if self._responses:
            resp = self._responses[self._idx % len(self._responses)]
            self._idx += 1
            return resp
        return json.dumps({"constraints": [
            {"type": "equation", "expression": "x - 7", "z3_formula": "x == 7", "source_step": 1},
            {"type": "equation", "expression": "x + 5 - 12", "z3_formula": "x + 5 == 12", "source_step": 2},
        ], "answer": "7", "variables": ["x"]})


class APIBasedLLM(LLMBackend):
    """LLM backend using OpenAI-compatible API (e.g. vLLM server)."""

    def __init__(self, base_url: str = "http://localhost:8000/v1",
                 api_key: [REDACTED] = "EMPTY", model: str | None = None,
                 temperature: float = 0.1, max_tokens: int = 2048):
        import openai
        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
        self.temperature = temperature
        self.max_tokens = max_tokens
        if model:
            self.model = model
        else:
            models = self.client.models.list()
            self.model = models.data[0].id

    def call(self, prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return resp.choices[0].message.content or ""


@dataclass
class ExtractionStats:
    success: int = 0
    fail_json_parse: int = 0
    fail_empty: int = 0
    fail_invalid_expr: int = 0

    @property
    def total_fail(self) -> int:
        return self.fail_json_parse + self.fail_empty + self.fail_invalid_expr


class ConstraintExtractor:
    def __init__(self, llm: LLMBackend | None = None):
        self.llm = llm or MockLLM()
        self.stats = ExtractionStats()

    def _build_prompt(self, trace: str) -> str:
        return EXTRACTION_PROMPT.format(trace=trace)

    def _parse_response(self, raw: str, trace: str) -> list[dict]:
        """Parse a raw LLM response into constraint list."""
        json_str = raw.strip()
        m = re.search(r'```(?:json)?\s*(.*?)```', json_str, re.DOTALL)
        if m:
            json_str = m.group(1).strip()

        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            logger.warning("JSON parse failed for trace: %s...", trace[:80])
            self.stats.fail_json_parse += 1
            return []

        constraints = data.get("constraints", [])
        if not constraints:
            self.stats.fail_empty += 1
            return []

        valid = []
        for c in constraints:
            if not all(k in c for k in ("type", "expression", "z3_formula", "source_step")):
                continue
            if c["type"] not in ("equation", "inequality", "predicate"):
                continue
            valid.append(c)

        if not valid:
            self.stats.fail_invalid_expr += 1
            return []

        self.stats.success += 1
        return valid

    def extract(self, trace: str) -> list[dict]:
        """Extract structured constraints from a reasoning trace."""
        prompt = self._build_prompt(trace)
        raw = self.llm.call(prompt)
        return self._parse_response(raw, trace)

    def extract_batch(self, traces: list[str]) -> list[list[dict]]:
        """批量提取约束，如果 LLM 后端支持 batch_call 则并发执行"""
        if hasattr(self.llm, 'batch_call'):
            prompts = [self._build_prompt(t) for t in traces]
            raw_results = self.llm.batch_call(prompts)
            return [self._parse_response(raw, trace)
                    for raw, trace in zip(raw_results, traces)]
        return [self.extract(t) for t in traces]
