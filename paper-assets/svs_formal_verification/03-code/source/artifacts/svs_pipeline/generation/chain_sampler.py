"""Chain sampler — generates multiple CoT reasoning chains per problem via LLM.

Calls an OpenAI-compatible API (DeepSeek by default) to produce step-by-step
reasoning chains, then extracts the final True/False/Unknown answer from each.

Dependencies: openai
"""

from __future__ import annotations

import logging
import re
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from openai import OpenAI

from ..config import APIConfig, SamplingConfig
from ..cost_tracker import get_tracker
from ..types import Problem, Chain

logger = logging.getLogger(__name__)

_SYSTEM_PROMPT = (
    "You are a logical reasoning expert. Given a set of premises and a hypothesis, "
    "determine whether the hypothesis is True, False, or Unknown based solely on the premises.\n\n"
    "Think step by step. At the end of your reasoning, state your final answer on a new line "
    "in exactly this format:\n"
    "The answer is: <True/False/Unknown>"
)

_ANSWER_PATTERN = re.compile(
    r"(?:the\s+answer\s+is|therefore|conclusion|verdict|final\s+answer)\s*[:\-]?\s*(True|False|Unknown)",
    re.IGNORECASE,
)


class ChainSampler:
    """Samples multiple CoT reasoning chains for a given problem."""

    def __init__(self, api_config: APIConfig, sampling_config: SamplingConfig):
        from openai import OpenAI as _OpenAI

        self.client = _OpenAI(
            base_url=api_config.base_url,
            api_key=[REDACTED],
            timeout=api_config.timeout,
        )
        self.model = api_config.model
        self.max_retries = api_config.max_retries
        self.temperature = sampling_config.temperature
        self.max_tokens = sampling_config.max_tokens

    def sample(self, problem: Problem, num_chains: int) -> list[Chain]:
        """Sample num_chains reasoning chains for the given problem."""
        user_prompt = self._build_prompt(problem)
        chains = []

        for chain_id in range(num_chains):
            result = self._call_llm(user_prompt, chain_id)
            if result is None:
                logger.warning("Chain %d failed for problem %s, skipping", chain_id, problem.id)
                continue

            reasoning, token_logprobs = result
            answer = self._extract_answer(reasoning)
            chains.append(Chain(
                problem_id=problem.id,
                chain_id=chain_id,
                answer=answer,
                reasoning=reasoning,
                logprobs=token_logprobs,
            ))

        logger.info("Sampled %d/%d chains for problem %s", len(chains), num_chains, problem.id)
        return chains

    def _build_prompt(self, problem: Problem) -> str:
        premises_text = "\n".join(f"- {p}" for p in problem.premises)
        return (
            f"Premises:\n{premises_text}\n\n"
            f"Hypothesis: {problem.hypothesis}\n\n"
            f"Based on the premises above, is the hypothesis True, False, or Unknown? "
            f"Think step by step."
        )

    def _call_llm(self, user_prompt: str, chain_id: int) -> tuple[str, list[float] | None] | None:
        """Call the LLM API with retries. Returns (content, logprobs) or None."""
        for attempt in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": _SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    logprobs=True,
                    top_logprobs=1,
                )
                if hasattr(response, 'usage') and response.usage:
                    get_tracker().record(
                        model=self.model,
                        prompt_tokens=response.usage.prompt_tokens or 0,
                        completion_tokens=response.usage.completion_tokens or 0,
                        module="chain_sampler",
                    )
                content = response.choices[0].message.content
                token_logprobs = None
                choice_logprobs = getattr(response.choices[0], 'logprobs', None)
                if choice_logprobs and hasattr(choice_logprobs, 'content') and choice_logprobs.content:
                    token_logprobs = [t.logprob for t in choice_logprobs.content]
                return content, token_logprobs
            except Exception as e:
                logger.warning("API call failed (chain=%d, attempt=%d/%d): %s",
                               chain_id, attempt + 1, self.max_retries, e)
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)

        return None

    @staticmethod
    def _extract_answer(reasoning: str) -> str:
        """Extract True/False/Unknown from reasoning text."""
        match = _ANSWER_PATTERN.search(reasoning)
        if match:
            raw = match.group(1).strip().lower()
            return {"true": "True", "false": "False", "unknown": "Unknown"}.get(raw, "Unknown")

        for line in reversed(reasoning.strip().splitlines()):
            line_clean = line.strip().lower()
            for label in ("true", "false", "unknown"):
                if label in line_clean:
                    return label.capitalize()

        return "Unknown"
