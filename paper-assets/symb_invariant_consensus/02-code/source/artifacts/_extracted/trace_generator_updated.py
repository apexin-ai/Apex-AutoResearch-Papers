"""
Reasoning trace generator. Supports vLLM API, external API, and mock mode.
Input: math problem string, K (number of traces)
Output: list of {"trace": str, "answer": str} dicts
Dependencies: openai, re, asyncio
"""
from __future__ import annotations

import asyncio
import re
import time
import random
import logging
from abc import ABC, abstractmethod
from typing import Optional

logger = logging.getLogger(__name__)

SOLVE_PROMPT = """Solve the following math problem step by step. Show all your reasoning.
At the end, put your final answer in \\boxed{{}}.

Problem: {problem}"""

LOGIC_PROMPT = """You are given a set of facts and rules, followed by a question about whether a statement is true, false, or unknown.

Think step by step, applying the rules to the facts to determine whether the statement can be proven true, proven false, or neither (unknown).

At the end, state your conclusion as exactly one of: True, False, or Unknown.
Put your final answer in \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}.

{problem}"""


FOLIO_PROMPT = """You are given a list of premises (facts and rules expressed in natural language), followed by a conclusion.

Determine whether the conclusion logically follows from the premises (True), is contradicted by the premises (False), or cannot be determined from the premises alone (Unknown).

Think step by step, carefully applying the premises to reason about the conclusion.

At the end, state your conclusion as exactly one of: True, False, or Unknown.
Put your final answer in \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}.

{problem}"""

PROMPT_TEMPLATES = {
    "math": SOLVE_PROMPT,
    "logic": LOGIC_PROMPT,
    "folio": FOLIO_PROMPT,
}


def normalize_logic_answer(answer: str) -> str:
    if not answer:
        return ""
    normalized = answer.strip().lower()
    if normalized in ("true", "yes", "proved", "proven"):
        return "True"
    if normalized in ("false", "no", "disproved", "disproven"):
        return "False"
    if normalized in ("unknown", "uncertain", "undetermined", "cannot be determined"):
        return "Unknown"
    return answer.strip()


def extract_boxed_answer(text: str) -> str:
    """Extract the last \\boxed{...} content from text, handling nested braces."""
    idx = text.rfind('\\boxed{')
    if idx == -1:
        return ""
    start = idx + len('\\boxed{')
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
        i += 1
    return text[start:i-1].strip()


def extract_answer_fallback(text: str) -> Optional[str]:
    """Fallback answer extraction when \\boxed{} is missing (e.g., truncated traces)."""
    patterns = [
        # "the answer is X" / "the final answer is X"
        r'(?:the\s+)?(?:final\s+)?answer\s+is\s*[:\s]*\$?\\?boxed\{([^}]+)\}',
        r'(?:the\s+)?(?:final\s+)?(?:answer|conclusion|statement)\s+is\s*[:\s]*(True|False|Unknown|Yes|No)',
        r'(?:the\s+)?(?:final\s+)?answer\s+is\s*[:\s]*\$?\*?\*?([+-]?\d+(?:\.\d+)?)\*?\*?\$?',
        # "therefore/thus/hence ... = X"
        r'(?:therefore|thus|hence|so)\s*,?\s*[^=\n]{0,80}?=\s*\$?\*?\*?([+-]?\d+(?:\.\d+)?)\*?\*?\$?',
        # "= X" near end (last 500 chars)
        r'=\s*\$?\*?\*?([+-]?\d+(?:\.\d+)?)\*?\*?\$?\s*$',
    ]

    # Try last 1000 chars first (final answer more likely near end), then full text
    for search_text in [text[-1000:], text]:
        for pattern in patterns:
            matches = re.findall(pattern, search_text, re.IGNORECASE | re.MULTILINE)
            if matches:
                return matches[-1].strip()
    # Bare Yes/No/True/False response (model gave single-word answer)
    stripped = text.strip().lower()
    if stripped in ("yes", "no", "true", "false"):
        return text.strip()
    return None


def extract_answer(text: str) -> tuple[str, str]:
    """
    Extract answer from trace text. Returns (answer, method).
    method is one of: "boxed", "fallback", "none".
    """
    boxed = extract_boxed_answer(text)
    if boxed:
        return boxed, "boxed"
    fb = extract_answer_fallback(text)
    if fb:
        logger.info("Fallback extraction matched: %s", fb)
        return fb, "fallback"
    return "", "none"


def retry_with_backoff(func, max_retries=3, base_delay=1.0):
    """Simple exponential backoff retry."""
    for attempt in range(max_retries + 1):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries:
                raise
            delay = base_delay * (2 ** attempt) + random.uniform(0, 0.5)
            logger.warning("Retry %d/%d after %.1fs: %s", attempt + 1, max_retries, delay, e)
            time.sleep(delay)


class TraceGenerator(ABC):
    @abstractmethod
    def generate(self, problem: str, k: int = 12, task_type: str = "math") -> list[dict]:
        """Generate K reasoning traces. Returns list of {"trace": str, "answer": str}."""
        ...


class VLLMGenerator(TraceGenerator):
    """vLLM server inference via OpenAI-compatible API. Prefers n=K batch, falls back to async concurrency."""

    def __init__(self, base_url: str = "http://localhost:8000/v1",
                 api_key: [REDACTED] = "EMPTY", model: str | None = None,
                 temperature: float = 0.7, top_p: float = 0.95,
                 max_tokens: int = 4096, seed: int | None = None):
        import openai
        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED], timeout=600.0)
        self.async_client = openai.AsyncOpenAI(base_url=base_url, api_key=[REDACTED], timeout=600.0)
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.seed = seed
        if model:
            self.model = model
        else:
            models = self.client.models.list()
            self.model = models.data[0].id
            logger.info("Auto-detected model: %s", self.model)

    def _build_prompt(self, problem: str, task_type: str = "math") -> str:
        template = PROMPT_TEMPLATES.get(task_type, SOLVE_PROMPT)
        return template.format(problem=problem)

    def _generate_n_batch(self, prompt: str, k: int) -> list[dict]:
        batch_size = 4
        results = []
        for batch_start in range(0, k, batch_size):
            batch_n = min(batch_size, k - batch_start)
            logger.info("Generating traces %d-%d of %d", batch_start + 1, batch_start + batch_n, k)
            response = retry_with_backoff(lambda _n=batch_n: self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                n=_n,
                **({"seed": self.seed} if self.seed is not None else {}),
            ))
            for i, choice in enumerate(response.choices):
                text = choice.message.content or ""
                answer, method = extract_answer(text)
                finish_reason = choice.finish_reason or "unknown"
                if method != "boxed":
                    logger.warning("Trace %d: extraction_method=%s, finish_reason=%s, answer=%s",
                                   batch_start + i, method, finish_reason, answer[:50] if answer else "NONE")
                results.append({
                    "trace": text, "answer": answer, "trace_idx": batch_start + i,
                    "finish_reason": finish_reason, "extraction_method": method,
                })
        return results

    async def _generate_single(self, prompt: str, trace_idx: int) -> dict:
        response = await self.async_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            top_p=self.top_p,
            max_tokens=self.max_tokens,
            **({"seed": self.seed} if self.seed is not None else {}),
        )
        text = response.choices[0].message.content or ""
        answer, method = extract_answer(text)
        finish_reason = response.choices[0].finish_reason or "unknown"
        if method != "boxed":
            logger.warning("Trace %d: extraction_method=%s, finish_reason=%s, answer=%s",
                           trace_idx, method, finish_reason, answer[:50] if answer else "NONE")
        return {
            "trace": text, "answer": answer, "trace_idx": trace_idx,
            "finish_reason": finish_reason, "extraction_method": method,
        }

    def _generate_async_fallback(self, prompt: str, k: int) -> list[dict]:
        """Fallback: async concurrency when n parameter is not supported."""
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

    def generate(self, problem: str, k: int = 12, task_type: str = "math") -> list[dict]:
        """Generate K traces. Uses n=K batch first, falls back to async concurrency."""
        prompt = self._build_prompt(problem, task_type=task_type)
        try:
            results = self._generate_n_batch(prompt, k)
        except Exception as e:
            logger.warning("n=K batch failed (%s), falling back to async concurrency", e)
            results = self._generate_async_fallback(prompt, k)
        if task_type in ("logic", "folio"):
            for r in results:
                r["answer"] = normalize_logic_answer(r["answer"])
        return results


class APIGenerator(TraceGenerator):
    """Generic OpenAI-compatible API inference."""

    def __init__(self, base_url: str, api_key: [REDACTED], model: str,
                 temperature: float = 0.7, top_p: float = 0.95,
                 max_tokens: int = 4096, seed: int | None = None):
        import openai
        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED], timeout=600.0)
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.seed = seed

    def generate(self, problem: str, k: int = 12, task_type: str = "math") -> list[dict]:
        template = PROMPT_TEMPLATES.get(task_type, SOLVE_PROMPT)
        prompt = template.format(problem=problem)
        results = []
        for i in range(k):
            resp = retry_with_backoff(lambda: self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                **({"seed": self.seed} if self.seed is not None else {}),
            ))
            text = resp.choices[0].message.content or ""
            answer, method = extract_answer(text)
            finish_reason = resp.choices[0].finish_reason or "unknown"
            if method != "boxed":
                logger.warning("Trace %d: extraction_method=%s, finish_reason=%s, answer=%s",
                               i, method, finish_reason, answer[:50] if answer else "NONE")
            results.append({
                "trace": text, "answer": answer, "trace_idx": i,
                "finish_reason": finish_reason, "extraction_method": method,
            })
        if task_type in ("logic", "folio"):
            for r in results:
                r["answer"] = normalize_logic_answer(r["answer"])
        return results


class MockGenerator(TraceGenerator):
    """Mock generator for testing. Returns preset traces."""

    def __init__(self, preset_traces: list[dict] | None = None):
        self._presets = preset_traces

    def generate(self, problem: str, k: int = 12, task_type: str = "math") -> list[dict]:
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
            results.append({"trace": trace, "answer": answer, "trace_idx": i,
                            "finish_reason": "stop", "extraction_method": "boxed"})
        return results
