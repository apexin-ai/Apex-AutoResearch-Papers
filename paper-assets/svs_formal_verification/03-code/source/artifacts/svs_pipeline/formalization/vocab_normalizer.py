"""Vocabulary normalizer: extract shared predicate/constant vocabularies from problems.

Ensures all chains for a problem use the same predicate and constant names,
which is critical for cross-chain logical coherence (CCLC) — without shared
vocabulary, Z3 treats different symbol names as independent and the conjunction
becomes trivially satisfiable.

Input: Problem (premises + hypothesis)
Output: dict with "predicates" and "constants" mappings
"""

import logging
import json
import re

from openai import OpenAI

from ..types import Problem
from ..config import APIConfig
from ..cost_tracker import get_tracker

logger = logging.getLogger(__name__)

# Regex patterns for ProofWriter's stylized English
_ENTITY_PAT = re.compile(
    r"\b(?:The\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b"
    r"(?=\s+(?:is|likes|chases|sees|visits|eats|needs|does))"
)
_UNARY_IS_PAT = re.compile(
    r"\b(?:[Tt]he\s+)?(\w+(?:\s+\w+)?)\s+is\s+(?:not\s+)?(\w+)\b"
)
_BINARY_VERB_PAT = re.compile(
    r"\b(?:[Tt]he\s+)?(\w+(?:\s+\w+)?)\s+(likes|chases|sees|visits|eats|needs|does\s+not\s+\w+|does\s+\w+)\s+(?:the\s+)?(\w+(?:\s+\w+)?)\b",
    re.IGNORECASE,
)

# Pronouns and function words that regex mistakenly captures as constants
_CONSTANT_STOPWORDS = {
    "something", "someone", "it", "they", "them", "he", "she",
    "everything", "nothing", "anything", "everyone", "no one",
    "this", "that", "these", "those", "who", "what", "which",
}


def _filter_constants(constants: dict) -> dict:
    """Remove pronouns, connective residue, and single-char noise from constants."""
    filtered = {}
    for name, info in constants.items():
        lower = name.lower().strip()
        if lower in _CONSTANT_STOPWORDS:
            continue
        if lower.startswith(("if_", "then_", "and_", "or_")):
            continue
        if any(lower.endswith(s) for s in ("_then", "_and", "_or", "_not", "_if")):
            continue
        if '_' in lower:
            parts = lower.split('_')
            if parts[-1] in ('then', 'and', 'or', 'not', 'if', 'but'):
                continue
        if len(lower) <= 1:
            continue
        filtered[name] = info
    return filtered


def _normalize_predicate(name: str) -> str:
    """Strip third-person -s to get verb stem: Needs→Need, Chases→Chase."""
    if name.endswith("s") and not name.endswith("ss") and len(name) > 2:
        return name[:-1]
    return name


def _predicate_description(stem: str, arity: int) -> str:
    """Generate readable description from predicate stem."""
    lower = stem.lower()
    if arity == 1:
        return f"is {lower}"
    return f"{lower}s (relation)"


def _normalize_predicates(predicates: dict) -> dict:
    """Merge inflected variants (Need/Needs) into a single canonical predicate."""
    merged: dict[str, dict] = {}
    for name, info in predicates.items():
        canonical = _normalize_predicate(name) if info["arity"] == 2 else name
        if canonical not in merged:
            merged[canonical] = {
                "arity": info["arity"],
                "description": _predicate_description(canonical, info["arity"]),
            }
    return merged

_LLM_VOCAB_PROMPT = """\
You are a logic formalization assistant. Given a set of natural language premises and a hypothesis, \
extract a shared vocabulary of predicates and constants for first-order logic formalization.

**Rules:**
- Predicates are properties (unary) or relations (binary). Use CamelCase names.
- Constants are named entities. Use lowercase snake_case.
- Every predicate and constant that appears in the premises or hypothesis must be included.
- Do NOT invent predicates/constants not grounded in the text.

**Output format (strict JSON, no extra text):**
```json
{
  "predicates": {
    "PredicateName": {"arity": 1, "description": "short description"},
    ...
  },
  "constants": {
    "entity_name": {"sort": "entity", "description": "short description"},
    ...
  }
}
```

Premises:
{premises}

Hypothesis:
{hypothesis}

Extract the vocabulary now. Output only the JSON object."""


class VocabNormalizer:
    def __init__(self, api_config: APIConfig | None = None):
        self._api = api_config
        if api_config:
            self._client = OpenAI(
                base_url=api_config.formalization_base_url,
                api_key=[REDACTED],
                timeout=api_config.timeout,
            )

    def extract_vocab(self, problem: Problem) -> dict:
        """Auto-select extraction mode: regex for ProofWriter, LLM for others."""
        if problem.dataset == "proofwriter":
            vocab = self.normalize_vocab_regex(problem)
            if vocab["predicates"] or vocab["constants"]:
                logger.info(
                    "Regex extraction for %s: %d predicates, %d constants",
                    problem.id,
                    len(vocab["predicates"]),
                    len(vocab["constants"]),
                )
                return vocab
            logger.warning(
                "Regex extraction empty for %s, falling back to LLM", problem.id
            )
        return self.normalize_vocab_llm(problem)

    # ------------------------------------------------------------------
    # Regex-based extraction (ProofWriter)
    # ------------------------------------------------------------------

    def normalize_vocab_regex(self, problem: Problem) -> dict:
        predicates: dict[str, dict] = {}
        constants: dict[str, dict] = {}

        all_text = problem.premises + [problem.hypothesis]

        for sent in all_text:
            self._extract_unary(sent, predicates, constants)
            self._extract_binary(sent, predicates, constants)

        # second pass: pick up entity names that only appeared as objects
        for sent in all_text:
            for m in _ENTITY_PAT.finditer(sent):
                name = m.group(1).lower().replace(" ", "_")
                if name not in constants and name not in {
                    p.lower() for p in predicates
                }:
                    constants[name] = {"sort": "entity", "description": name}

        constants = _filter_constants(constants)
        predicates = _normalize_predicates(predicates)
        return {"predicates": predicates, "constants": constants}

    @staticmethod
    def _extract_unary(
        sent: str, predicates: dict, constants: dict
    ) -> None:
        for m in _UNARY_IS_PAT.finditer(sent):
            subj = m.group(1).lower().replace(" ", "_")
            prop = m.group(2).capitalize()
            if prop.lower() in ("not", "a", "an", "the"):
                continue
            predicates.setdefault(
                prop, {"arity": 1, "description": f"is {prop.lower()}"}
            )
            constants.setdefault(
                subj, {"sort": "entity", "description": subj}
            )

    @staticmethod
    def _extract_binary(
        sent: str, predicates: dict, constants: dict
    ) -> None:
        for m in _BINARY_VERB_PAT.finditer(sent):
            subj = m.group(1).lower().replace(" ", "_")
            verb = m.group(2).strip().split()[0].capitalize()
            obj = m.group(3).lower().replace(" ", "_")
            pred_name = verb
            # "does not chase" → "Chase" (negation handled at FOL level)
            if verb.lower() == "does":
                parts = m.group(2).strip().split()
                if len(parts) >= 2:
                    pred_name = parts[-1].capitalize()
            predicates.setdefault(
                pred_name, {"arity": 2, "description": f"{pred_name.lower()} (relation)"}
            )
            constants.setdefault(
                subj, {"sort": "entity", "description": subj}
            )
            constants.setdefault(
                obj, {"sort": "entity", "description": obj}
            )

    # ------------------------------------------------------------------
    # LLM-based extraction (FOLIO and fallback)
    # ------------------------------------------------------------------

    def normalize_vocab_llm(self, problem: Problem) -> dict:
        if not self._api:
            raise ValueError("LLM vocab extraction requires an APIConfig")

        premises_text = "\n".join(
            f"{i+1}. {p}" for i, p in enumerate(problem.premises)
        )
        prompt = _LLM_VOCAB_PROMPT.format(
            premises=premises_text, hypothesis=problem.hypothesis
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
                        module="vocab_normalizer",
                    )
                text = resp.choices[0].message.content.strip()
                vocab = self._parse_vocab_json(text)
                logger.info(
                    "LLM vocab extraction for %s (attempt %d): %d predicates, %d constants",
                    problem.id,
                    attempt + 1,
                    len(vocab["predicates"]),
                    len(vocab["constants"]),
                )
                return vocab
            except Exception as e:
                last_error = e
                logger.warning(
                    "LLM vocab extraction attempt %d failed for %s: %s",
                    attempt + 1,
                    problem.id,
                    e,
                )

        logger.error(
            "LLM vocab extraction failed for %s after %d attempts: %s",
            problem.id,
            self._api.max_retries,
            last_error,
        )
        return {"predicates": {}, "constants": {}}

    @staticmethod
    def _parse_vocab_json(text: str) -> dict:
        # Strip markdown code fences if present
        text = re.sub(r"```(?:json)?\s*", "", text).strip()
        text = text.rstrip("`").strip()

        data = json.loads(text)
        vocab: dict = {"predicates": {}, "constants": {}}

        for name, info in data.get("predicates", {}).items():
            vocab["predicates"][name] = {
                "arity": int(info.get("arity", 1)),
                "description": str(info.get("description", "")),
            }
        for name, info in data.get("constants", {}).items():
            vocab["constants"][name] = {
                "sort": str(info.get("sort", "entity")),
                "description": str(info.get("description", name)),
            }
        return vocab
