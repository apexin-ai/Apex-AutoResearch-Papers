"""Claim decomposer: split a CoT reasoning chain into atomic logical claims.

Takes a Chain (full CoT text) and produces a list of AtomicClaim objects,
each representing a single independent logical assertion that can be
independently formalized and verified.

Input:  Chain + Problem context
Output: list[AtomicClaim]
"""

import json
import logging
import re

from openai import OpenAI

from ..types import AtomicClaim, Chain, Problem
from ..config import APIConfig
from ..cost_tracker import get_tracker

logger = logging.getLogger(__name__)

_DECOMPOSE_PROMPT = """\
You are a logical reasoning analyst. Given a problem's premises, hypothesis, and a chain-of-thought \
reasoning trace, decompose the reasoning into a list of **atomic claims**.

**What is an atomic claim?**
- A single, self-contained logical assertion (e.g., "The cat is green", "If X is kind then X is round").
- NOT a meta-statement about the reasoning process (skip phrases like "Let me think...", "Therefore the answer is...").
- Each claim should be understandable on its own without the surrounding text.
- Preserve the logical order from the reasoning chain.

**Output format (strict JSON array, no extra text):**
```json
["claim 1 text", "claim 2 text", ...]
```

---
**Premises:**
{premises}

**Hypothesis:** {hypothesis}

**Reasoning chain:**
{reasoning}

---
Decompose into atomic claims now. Output only the JSON array."""


class ClaimDecomposer:
    def __init__(self, api_config: APIConfig):
        self._api = api_config
        self._client = OpenAI(
            base_url=api_config.formalization_base_url,
            api_key=[REDACTED],
            timeout=api_config.timeout,
        )

    def decompose(self, chain: Chain, problem: Problem) -> list[AtomicClaim]:
        """Decompose a single chain into atomic claims via LLM."""
        premises_text = "\n".join(
            f"{i+1}. {p}" for i, p in enumerate(problem.premises)
        )
        prompt = _DECOMPOSE_PROMPT.format(
            premises=premises_text,
            hypothesis=problem.hypothesis,
            reasoning=chain.reasoning,
        )

        last_error = None
        for attempt in range(self._api.max_retries):
            try:
                resp = self._client.chat.completions.create(
                    model=self._api.formalization_model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.0,
                    max_tokens=1024,
                )
                if hasattr(resp, 'usage') and resp.usage:
                    get_tracker().record(
                        model=self._api.formalization_model,
                        prompt_tokens=resp.usage.prompt_tokens or 0,
                        completion_tokens=resp.usage.completion_tokens or 0,
                        module="claim_decomposer",
                    )
                text = resp.choices[0].message.content.strip()
                claims = self._parse_claims(text)
                if claims:
                    logger.info(
                        "Decomposed chain %d of problem %s into %d claims (attempt %d)",
                        chain.chain_id,
                        chain.problem_id,
                        len(claims),
                        attempt + 1,
                    )
                    return [
                        AtomicClaim(
                            chain_id=chain.chain_id,
                            problem_id=chain.problem_id,
                            claim_index=i,
                            text=c,
                        )
                        for i, c in enumerate(claims)
                    ]
            except Exception as e:
                last_error = e
                logger.warning(
                    "Decompose attempt %d failed for chain %d of %s: %s",
                    attempt + 1,
                    chain.chain_id,
                    chain.problem_id,
                    e,
                )

        logger.warning(
            "All LLM attempts failed for chain %d of %s (%s), using sentence-split fallback",
            chain.chain_id,
            chain.problem_id,
            last_error,
        )
        return self._fallback_split(chain)

    def decompose_batch(
        self, chains: list[Chain], problem: Problem
    ) -> dict[int, list[AtomicClaim]]:
        """Decompose multiple chains, keyed by chain_id."""
        results: dict[int, list[AtomicClaim]] = {}
        for chain in chains:
            results[chain.chain_id] = self.decompose(chain, problem)
        return results

    # ------------------------------------------------------------------
    # Parsing helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_claims(text: str) -> list[str] | None:
        """Parse LLM output as a JSON string array. Returns None on failure."""
        # Strip markdown code fences
        text = re.sub(r"```(?:json)?\s*", "", text).strip()
        text = text.rstrip("`").strip()

        try:
            data = json.loads(text)
            if isinstance(data, list) and all(isinstance(x, str) for x in data):
                cleaned = [s.strip() for s in data if s.strip()]
                return cleaned if cleaned else None
        except json.JSONDecodeError:
            pass

        # Try to find a JSON array embedded in the response
        match = re.search(r"\[.*\]", text, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group())
                if isinstance(data, list):
                    return [str(s).strip() for s in data if str(s).strip()]
            except json.JSONDecodeError:
                pass

        return None

    @staticmethod
    def _fallback_split(chain: Chain) -> list[AtomicClaim]:
        """Split reasoning by sentences as a last-resort fallback."""
        sentences = re.split(r"(?<=[.!?])\s+", chain.reasoning.strip())
        # Filter out meta-reasoning filler
        skip_patterns = re.compile(
            r"^(therefore|thus|so|hence|in conclusion|the answer is|let me|let's|we know)",
            re.IGNORECASE,
        )
        claims = []
        for s in sentences:
            s = s.strip().rstrip(".")
            if not s or len(s) < 5 or skip_patterns.match(s):
                continue
            claims.append(s)

        logger.info(
            "Fallback split for chain %d of %s: %d claims",
            chain.chain_id,
            chain.problem_id,
            len(claims),
        )
        return [
            AtomicClaim(
                chain_id=chain.chain_id,
                problem_id=chain.problem_id,
                claim_index=i,
                text=c,
            )
            for i, c in enumerate(claims)
        ]
