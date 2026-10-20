"""Premise formalizer — translate problem premises into FOL for PCV.

Premises are formalized once per problem and shared across all chains.
ProofWriter premises are near-formal ("If something is green then it is big"),
so frontier model formalization should be highly reliable.
"""

import logging
import re

from openai import OpenAI
from ..types import Problem
from ..config import APIConfig
from ..cost_tracker import get_tracker

logger = logging.getLogger(__name__)

_PREMISE_PROMPT = """\
You are a logic formalization assistant. Convert each premise into a Z3 Python expression.

**Rules:**
- Use the provided vocabulary (predicates and constants) for consistency.
- Each premise should become one Z3 expression.
- Use ForAll/Exists for quantified statements.

**CRITICAL RULES for quantifiers:**
1. "If someone/something X, then they/it Y" → ForAll([x], Implies(X(x), Y(x)))
   NOT Exists. "someone...they" refers to the SAME variable universally quantified.
2. "If someone needs the tiger then they do not visit the eagle"
   → ForAll([x], Implies(Need(x, tiger), Not(Visit(x, eagle))))
   WRONG: Implies(Exists([x], Need(x, tiger)), ForAll([y], Not(Visit(y, eagle))))
   WRONG: Exists([x], Implies(Need(x, tiger), Not(Visit(x, eagle))))
3. Use Exists ONLY for explicit existential claims: "There exists...", "Some X is Y"
4. Co-reference: "someone...they/them" = same variable x, use ForAll with single variable
5. "Everything that X is Y" → ForAll([x], Implies(X(x), Y(x)))
6. "If X then Y" where X and Y are about a generic subject → ForAll, not Exists

- Use Implies for conditional statements ("if X then Y").
- Output one Z3 expression per line, numbered to match the premise.

**Vocabulary:**
{vocab_json}

**Premises:**
{premises}

**Output format (strict, one expression per line):**
1. ForAll([x], Implies(Green(x), Big(x)))
2. Cold(cat)
...

Output only the numbered Z3 expressions, nothing else."""


class PremiseFormalizer:
    def __init__(self, api_config: APIConfig):
        self._api = api_config
        self._client = OpenAI(
            base_url=api_config.formalization_base_url,
            api_key=[REDACTED],
            timeout=api_config.timeout,
        )
        self._cache: dict[str, list[str]] = {}

    def formalize_premises(self, problem: Problem, vocab: dict) -> list[str]:
        """Formalize all premises for a problem. Results are cached."""
        if problem.id in self._cache:
            return self._cache[problem.id]

        import json
        vocab_json = json.dumps(vocab, indent=2)
        premises_text = "\n".join(f"{i+1}. {p}" for i, p in enumerate(problem.premises))

        prompt = _PREMISE_PROMPT.format(vocab_json=vocab_json, premises=premises_text)

        fol_list = []
        last_error = None
        for attempt in range(self._api.max_retries):
            try:
                resp = self._client.chat.completions.create(
                    model=self._api.formalization_model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.0,
                    max_tokens=512,
                )
                if hasattr(resp, 'usage') and resp.usage:
                    get_tracker().record(
                        model=self._api.formalization_model,
                        prompt_tokens=resp.usage.prompt_tokens or 0,
                        completion_tokens=resp.usage.completion_tokens or 0,
                        module="premise_formalizer",
                    )
                text = resp.choices[0].message.content.strip()
                fol_list = self._parse_numbered_fols(text)
                logger.info(
                    "Premise formalization for %s: %d/%d premises formalized",
                    problem.id, len(fol_list), len(problem.premises),
                )
                break
            except Exception as e:
                last_error = e
                logger.warning("Premise formalization attempt %d failed: %s", attempt + 1, e)

        if not fol_list and last_error:
            logger.error("Premise formalization failed for %s: %s", problem.id, last_error)

        self._cache[problem.id] = fol_list
        return fol_list

    @staticmethod
    def _parse_numbered_fols(text: str) -> list[str]:
        """Parse numbered FOL expressions from LLM output."""
        fols = []
        for line in text.strip().split("\n"):
            line = line.strip()
            match = re.match(r'^\d+\.\s*(.+)$', line)
            if match:
                fol = match.group(1).strip()
                if fol:
                    fols.append(fol)
        return fols
