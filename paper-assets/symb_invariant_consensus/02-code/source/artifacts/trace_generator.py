"""
Reasoning trace generator. Supports vLLM API, external API, and mock mode.
Input: math problem string, K (number of traces)
Output: list of {"trace": str, "answer": str} dicts
Dependencies: openai, re, asyncio
"""
from __future__ import annotations

import asyncio
import re
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

SOLVE_PROMPT = """Solve the following math problem step by step. Show all your reasoning.
At the end, put your final answer in \\boxed{{}}.

Problem: {problem}"""


def extract_boxed_answer(text: str) -> str:
    """Extract the last \\boxed{...} content from text."""
    matches = re.findall(r'\\boxed\{([^}]*(?:\{[^}]*\}[^}]*)*)\}', text)
    return matches[-1].strip() if matches else ""


class TraceGenerator(ABC):
    @abstractmethod
    def generate(self, problem: str, k: int = 12) -> list[dict]:
        """Generate K reasoning traces. Returns list of {"trace": str, "answer": str}."""
        ...


class VLLMGenerator(TraceGenerator):
    """vLLM server inference via OpenAI-compatible API with async concurrency."""

    def __init__(self, base_url: str = "http://localhost:8000/v1",
                 api_key: [REDACTED] = "EMPTY", model: str | None = None,
                 temperature: float = 0.7, top_p: float = 0.95,
                 max_tokens: int = 4096):
        import openai
        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
        self.async_client = openai.AsyncOpenAI(base_url=base_url, api_key=[REDACTED]
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
        if model:
            self.model = model
        else:
            models = self.client.models.list()
            self.model = models.data[0].id
            logger.info("Auto-detected model: %s", self.model)

    def _build_prompt(self, problem: str) -> str:
        return SOLVE_PROMPT.format(problem=problem)

    async def _generate_single(self, prompt: str, trace_idx: int) -> dict:
        response = await self.async_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            top_p=self.top_p,
            max_tokens=self.max_tokens,
        )
        text = response.choices[0].message.content or ""
        answer = extract_boxed_answer(text)
        return {"trace": text, "answer": answer, "trace_idx": trace_idx}

    def generate(self, problem: str, k: int = 12) -> list[dict]:
        """并发生成 K 条 traces"""
        prompt = self._build_prompt(problem)

        async def _run():
            tasks = [self._generate_single(prompt, i) for i in range(k)]
            return await asyncio.gather(*tasks)

        try:
            loop = asyncio.get_running_loop()
            import nest_asyncio
            nest_asyncio.apply()
            return loop.run_until_complete(_run())
        except RuntimeError:
            return asyncio.run(_run())


class APIGenerator(TraceGenerator):
    """Generic OpenAI-compatible API inference."""

    def __init__(self, base_url: str, api_key: [REDACTED], model: str,
                 temperature: float = 0.7, top_p: float = 0.95,
                 max_tokens: int = 4096):
        import openai
        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens

    def generate(self, problem: str, k: int = 12) -> list[dict]:
        prompt = SOLVE_PROMPT.format(problem=problem)
        results = []
        for i in range(k):
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
            )
            text = resp.choices[0].message.content or ""
            answer = extract_boxed_answer(text)
            results.append({"trace": text, "answer": answer, "trace_idx": i})
        return results


class MockGenerator(TraceGenerator):
    """Mock generator for testing. Returns preset traces."""

    def __init__(self, preset_traces: list[dict] | None = None):
        self._presets = preset_traces

    def generate(self, problem: str, k: int = 12) -> list[dict]:
        if self._presets:
            return [
                {**t, "trace_idx": i}
                for i, t in enumerate(self._presets[:k])
            ]
        results = []
        for i in range(k):
            if i < k // 2:
                trace = (f"Step 1: Let x be the answer.\n"
                         f"Step 2: From the problem, x + 5 = 12.\n"
                         f"Step 3: Therefore x = 7.\n"
                         f"The answer is \\boxed{{7}}")
                answer = "7"
            elif i < k * 3 // 4:
                trace = (f"Step 1: Define x as the unknown.\n"
                         f"Step 2: We have x + 5 = 12, so x = 7.\n"
                         f"Step 3: Check: 7 + 5 = 12. Correct.\n"
                         f"The answer is \\boxed{{7}}")
                answer = "7"
            else:
                trace = (f"Step 1: Let x be the value.\n"
                         f"Step 2: x + 5 = 13 (misread).\n"
                         f"Step 3: x = 8.\n"
                         f"The answer is \\boxed{{8}}")
                answer = "8"
            results.append({"trace": trace, "answer": answer, "trace_idx": i})
        return results
