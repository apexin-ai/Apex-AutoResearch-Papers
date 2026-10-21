"""
Constraint extractor: extract structured math constraints from LLM reasoning traces.
Input: reasoning trace string
Output: list of constraint dicts with type, expression, z3_formula, source_step
Dependencies: json, re, openai (optional)
"""
from __future__ import annotations

import json
import logging
import re
import time
import random
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

EXTRACTION_PROMPT = '''Extract mathematical constraints from this reasoning trace as a JSON object.

Rules:
- type: "equation", "inequality", or "predicate"
- expression: human-readable, e.g. "x + y == 14"
- z3_formula: Python Z3 syntax (==, !=, <, >, +, -, *, /, **)
- source_step: step number where the constraint appears
- Use variable names from the trace

Output ONLY the JSON below, nothing else:
{{"constraints": [{{"type": "equation", "expression": "x + y == 14", "z3_formula": "x + y == 14", "source_step": 1}}], "answer": "final_answer", "variables": ["x", "y"]}}

Trace:
{trace}'''

LOGIC_EXTRACTION_PROMPT = '''Extract logical constraints from this reasoning trace about a logic problem.

The problem has facts (base assertions), rules (grounded implications), and derived conclusions.
Convert each into a Z3 boolean formula.

Variable naming:
- Unary property: property_entity (e.g., kind_anne, red_charlie, round_fiona)
- Binary relation: relation_subject_object (e.g., eats_bear_squirrel, likes_lion_cat)
- Use lowercase with underscores only, no spaces or special characters

Constraint types:
- "fact": a given assertion, e.g., kind_anne == True
- "rule": a grounded implication over specific entities, e.g., Implies(kind_anne, nice_anne)
- "derived": an inferred conclusion from facts + rules, e.g., nice_anne == True

Z3 operators:
- Implies(a, b) for if-then rules
- And(a, b, ...) for conjunctive conditions
- Or(a, b, ...) for disjunctive conditions
- Not(a) for negation
- == True / == False for boolean assertions

Output ONLY the JSON below, nothing else:
{{"constraints": [{{"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1}}], "answer": "True or False or Unknown", "variables": ["kind_anne"]}}

Example 1:
Trace: "Anne is kind. Kind things are nice. Therefore Anne is nice. The answer is True."
Output:
{{"constraints": [
  {{"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1}},
  {{"type": "rule", "expression": "kind(X) -> nice(X)", "z3_formula": "Implies(kind_anne, nice_anne)", "source_step": 2}},
  {{"type": "derived", "expression": "nice(anne)", "z3_formula": "nice_anne == True", "source_step": 3}}
], "answer": "True", "variables": ["kind_anne", "nice_anne"]}}

Example 2:
Trace: "The bear eats the squirrel. If someone eats the squirrel then the squirrel is red. So the squirrel is red. The answer is True."
Output:
{{"constraints": [
  {{"type": "fact", "expression": "eats(bear, squirrel)", "z3_formula": "eats_bear_squirrel == True", "source_step": 1}},
  {{"type": "rule", "expression": "eats(X, squirrel) -> red(squirrel)", "z3_formula": "Implies(eats_bear_squirrel, red_squirrel)", "source_step": 2}},
  {{"type": "derived", "expression": "red(squirrel)", "z3_formula": "red_squirrel == True", "source_step": 3}}
], "answer": "True", "variables": ["eats_bear_squirrel", "red_squirrel"]}}

Example 3 (multi-condition rule):
Trace: "Gary is big. Gary is quiet. Big things are smart. Quiet, cold things are white. Gary is smart. But Gary is not cold. So we cannot determine if Gary is furry. The answer is Unknown."
Output:
{{"constraints": [
  {{"type": "fact", "expression": "big(gary)", "z3_formula": "big_gary == True", "source_step": 1}},
  {{"type": "fact", "expression": "quiet(gary)", "z3_formula": "quiet_gary == True", "source_step": 2}},
  {{"type": "rule", "expression": "big(X) -> smart(X)", "z3_formula": "Implies(big_gary, smart_gary)", "source_step": 3}},
  {{"type": "rule", "expression": "quiet(X) & cold(X) -> white(X)", "z3_formula": "Implies(And(quiet_gary, cold_gary), white_gary)", "source_step": 4}},
  {{"type": "derived", "expression": "smart(gary)", "z3_formula": "smart_gary == True", "source_step": 5}}
], "answer": "Unknown", "variables": ["big_gary", "quiet_gary", "smart_gary", "cold_gary", "white_gary"]}}

Trace:
{trace}'''

_MATH_TYPES = {"equation", "inequality", "predicate"}
_LOGIC_TYPES = {"fact", "rule", "derived"}

COMMONSENSE_EXTRACTION_PROMPT = '''Extract logical constraints from this reasoning trace about a commonsense Yes/No question.

The trace reasons about factual claims and causal relationships to reach a Yes or No conclusion.
Convert each reasoning step into a Z3 boolean formula.

Variable naming:
- Use descriptive snake_case names for propositions (e.g., cats_are_mammals, paris_is_capital_of_france)
- For causal/conditional claims, use Implies()

Constraint types:
- "claim": a factual assertion used in reasoning, e.g., cats_are_mammals == True
- "causal": a causal or conditional relationship, e.g., Implies(it_rains, ground_is_wet)
- "conclusion": the final answer derived from reasoning, e.g., answer_yes == True

Z3 operators:
- Implies(a, b) for if-then relationships
- And(a, b, ...) for conjunctive conditions
- Or(a, b, ...) for disjunctive conditions
- Not(a) for negation
- == True / == False for boolean assertions

Output ONLY the JSON below, nothing else:
{{"constraints": [{{"type": "claim", "expression": "cats are mammals", "z3_formula": "cats_are_mammals == True", "source_step": 1}}], "answer": "Yes or No", "variables": ["cats_are_mammals"]}}

Example:
Trace: "The question asks if the CEO of Twitter has ever been to space. The CEO of Twitter was Elon Musk. Elon Musk founded SpaceX. However, Elon Musk has not personally traveled to space. The answer is No."
Output:
{{"constraints": [
  {{"type": "claim", "expression": "CEO of Twitter is Elon Musk", "z3_formula": "twitter_ceo_is_musk == True", "source_step": 1}},
  {{"type": "claim", "expression": "Elon Musk founded SpaceX", "z3_formula": "musk_founded_spacex == True", "source_step": 2}},
  {{"type": "claim", "expression": "Musk has not traveled to space", "z3_formula": "musk_been_to_space == False", "source_step": 3}},
  {{"type": "causal", "expression": "CEO is Musk and Musk not in space implies CEO not in space", "z3_formula": "Implies(And(twitter_ceo_is_musk, Not(musk_been_to_space)), Not(twitter_ceo_been_to_space))", "source_step": 4}},
  {{"type": "conclusion", "expression": "answer is No", "z3_formula": "answer_yes == False", "source_step": 5}}
], "answer": "No", "variables": ["twitter_ceo_is_musk", "musk_founded_spacex", "musk_been_to_space", "twitter_ceo_been_to_space", "answer_yes"]}}

Trace:
{trace}'''

_COMMONSENSE_TYPES = {"claim", "causal", "conclusion"}




def _retry_with_backoff(func, max_retries=2, base_delay=0.5):
    for attempt in range(max_retries + 1):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries:
                raise
            delay = base_delay * (2 ** attempt) + random.uniform(0, 0.5)
            logger.warning("Retry %d/%d after %.1fs: %s", attempt + 1, max_retries, delay, e)
            time.sleep(delay)


class LLMBackend(ABC):
    """LLM abstract base class"""
    @abstractmethod
    def call(self, prompt: str) -> str:
        ...


class VLLMBackend(LLMBackend):
    """OpenAI-compatible API backend for local vLLM"""

    def __init__(self, base_url: str = "http://localhost:8000/v1", model: str | None = None,
                 temperature: float = 0.3,
                 max_tokens: int = 4096):
        from openai import OpenAI
        self.client = OpenAI(base_url=base_url, api_key="[REDACTED]")
        self.max_tokens = max_tokens
        self.temperature = temperature
        if model is None:
            models = self.client.models.list()
            self.model = models.data[0].id
        else:
            self.model = model

    def call(self, prompt: str) -> str:
        return _retry_with_backoff(lambda: self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        ).choices[0].message.content or "")

    def batch_call(self, prompts: list[str], max_workers: int = 4) -> list[str]:
        results = [None] * len(prompts)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_idx = {executor.submit(self.call, p): i for i, p in enumerate(prompts)}
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    results[idx] = future.result()
                except Exception as e:
                    logger.error("Extraction %d failed: %s", idx, e)
                    results[idx] = ""
        return results


class MockLLM(LLMBackend):
    """Returns pre-set responses for testing."""

    def __init__(self, responses: list[str] | None = None, domain: str = "math"):
        self._responses = responses or []
        self._idx = 0
        self._domain = domain

    def call(self, prompt: str) -> str:
        if self._responses:
            resp = self._responses[self._idx % len(self._responses)]
            self._idx += 1
            return resp
        if self._domain == "logic":
            return json.dumps({"constraints": [
                {"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1},
                {"type": "rule", "expression": "kind(X) -> nice(X)", "z3_formula": "Implies(kind_anne, nice_anne)", "source_step": 2},
                {"type": "derived", "expression": "nice(anne)", "z3_formula": "nice_anne == True", "source_step": 3},
            ], "answer": "True", "variables": ["kind_anne", "nice_anne"]})
        return json.dumps({"constraints": [
            {"type": "equation", "expression": "x - 7", "z3_formula": "x == 7", "source_step": 1},
            {"type": "equation", "expression": "x + 5 - 12", "z3_formula": "x + 5 == 12", "source_step": 2},
        ], "answer": "7", "variables": ["x"]})


class APIBasedLLM(LLMBackend):
    """LLM backend using OpenAI-compatible API (e.g. vLLM server)."""

    def __init__(self, base_url: str = "http://localhost:8000/v1",
                 api_key: [REDACTED] = "EMPTY", model: str | None = None,
                 temperature: float = 0.1, max_tokens: int = 4096,
                 extra_body: dict | None = None):
        import openai
        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.extra_body = extra_body or {}
        if model:
            self.model = model
        else:
            models = self.client.models.list()
            self.model = models.data[0].id

    def call(self, prompt: str) -> str:
        kwargs = {}
        if self.extra_body:
            kwargs["extra_body"] = self.extra_body
        return _retry_with_backoff(lambda: self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            **kwargs,
        ).choices[0].message.content or "")

    def batch_call(self, prompts: list[str], max_workers: int = 4) -> list[str]:
        results = [None] * len(prompts)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_idx = {executor.submit(self.call, p): i for i, p in enumerate(prompts)}
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    results[idx] = future.result()
                except Exception as e:
                    logger.error("Extraction %d failed: %s", idx, e)
                    results[idx] = ""
        return results


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
    def __init__(self, llm: LLMBackend | None = None, parse_retries: int = 1,
                 domain: str = "math"):
        self.llm = llm or MockLLM()
        self.stats = ExtractionStats()
        self.parse_retries = parse_retries
        self.domain = domain

    def _build_prompt(self, trace: str) -> str:
        if self.domain == "logic":
            template = LOGIC_EXTRACTION_PROMPT
        elif self.domain == "commonsense":
            template = COMMONSENSE_EXTRACTION_PROMPT
        else:
            template = EXTRACTION_PROMPT
        return template.format(trace=trace)

    @staticmethod
    def _strip_thinking(text: str) -> str:
        """Remove <think>...</think> blocks, handling truncated tags."""
        idx = text.find('</think>')
        if idx != -1:
            return text[idx + len('</think>'):].strip()
        # Truncated thinking: <think> present but no </think>
        idx = text.find('<think>')
        if idx != -1:
            return ''
        return text

    @staticmethod
    def _extract_json_str(text: str) -> str | None:
        """Try multiple strategies to extract a JSON object string."""
        # Strategy 1: fenced code block
        m = re.search(r'```(?:json)?\s*(.*?)```', text, re.DOTALL)
        if m:
            return m.group(1).strip()
        # Strategy 2: find outermost { ... } braces
        start = text.find('{')
        if start != -1:
            depth = 0
            for i in range(start, len(text)):
                if text[i] == '{':
                    depth += 1
                elif text[i] == '}':
                    depth -= 1
                    if depth == 0:
                        return text[start:i + 1]
        return None

    @staticmethod
    def _repair_json(s: str) -> str:
        """Fix common JSON errors from LLMs."""
        # Remove trailing commas before } or ]
        s = re.sub(r',\s*([}\]])', r'\1', s)
        # Replace single quotes with double quotes
        s = s.replace("'", '"')
        return s

    def _parse_response(self, raw: str, trace: str) -> list[dict]:
        text = self._strip_thinking(raw.strip())
        if not text:
            logger.warning("Empty after stripping thinking for trace: %s...", trace[:80])
            self.stats.fail_json_parse += 1
            return []

        json_str = self._extract_json_str(text)
        if json_str is None:
            logger.warning("No JSON found in response for trace: %s...", trace[:80])
            self.stats.fail_json_parse += 1
            return []

        data = None
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            try:
                data = json.loads(self._repair_json(json_str))
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
            if self.domain == "logic":
                valid_types = _LOGIC_TYPES
            elif self.domain == "commonsense":
                valid_types = _COMMONSENSE_TYPES
            else:
                valid_types = _MATH_TYPES
            if c["type"] not in valid_types:
                continue
            valid.append(c)

        if not valid:
            self.stats.fail_invalid_expr += 1
            return []

        self.stats.success += 1
        return valid

    def extract(self, trace: str) -> list[dict]:
        prompt = self._build_prompt(trace)
        for attempt in range(self.parse_retries + 1):
            raw = self.llm.call(prompt)
            result = self._parse_response(raw, trace)
            if result or attempt == self.parse_retries:
                return result
            logger.info("Re-extracting constraints (attempt %d/%d)", attempt + 1, self.parse_retries)
        return []

    def extract_batch(self, traces: list[str]) -> list[list[dict]]:
        if hasattr(self.llm, 'batch_call'):
            prompts = [self._build_prompt(t) for t in traces]
            raw_results = self.llm.batch_call(prompts)
            return [self._parse_response(raw, trace)
                    for raw, trace in zip(raw_results, traces)]
        return [self.extract(t) for t in traces]


# ---------------------------------------------------------------------------
# Contrastive constraint extraction
# ---------------------------------------------------------------------------

CONTRASTIVE_EXTRACTION_PROMPT = '''Analyze this reasoning trace about a logic problem and extract discriminative constraints.

Question: {question}

This trace concludes with answer: "{answer_from_trace}"
Candidate answers: {candidates}

For EACH candidate answer, extract logical constraints from the trace that either SUPPORT or OPPOSE that answer being correct.

Constraint format:
- stance: "supporting" or "opposing"
- target: the candidate answer this constraint is about (e.g. "True", "False", "Unknown")
- expression: human-readable form
- z3_formula: Python Z3 syntax using Bool variables
- source_step: step number in the trace

Variable naming: property_entity (lowercase, underscores). E.g., kind_anne, eats_bear_squirrel.
Z3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False

Focus on DISCRIMINATIVE constraints: ones where the logical content genuinely differentiates between candidate answers. Avoid restating domain facts that hold regardless of which answer is correct.

A supporting constraint provides evidence that the target answer is correct.
An opposing constraint provides evidence that the target answer is incorrect.

Output ONLY the JSON below, nothing else:
{{"constraints": [
  {{"stance": "supporting", "target": "True", "expression": "nice(anne) derived from facts+rules", "z3_formula": "nice_anne == True", "source_step": 3}},
  {{"stance": "opposing", "target": "False", "expression": "nice(anne) contradicts False", "z3_formula": "nice_anne == True", "source_step": 3}}
], "variables": ["kind_anne", "nice_anne"]}}

Trace:
{trace}'''

_CONTRASTIVE_STANCES = {"supporting", "opposing"}


class ContrastiveConstraintExtractor:
    """Extract constraints with stance labels (supporting/opposing) per candidate answer.

    Input: trace string, question, answer from trace, list of candidate answers
    Output: list of contrastive constraint dicts with stance, target, expression,
            z3_formula, source_step fields
    """

    def __init__(self, llm: LLMBackend | None = None, parse_retries: int = 1):
        self.llm = llm or MockLLM()
        self.stats = ExtractionStats()
        self.parse_retries = parse_retries

    def _build_prompt(self, trace: str, question: str,
                      answer_from_trace: str, candidates: list[str]) -> str:
        return CONTRASTIVE_EXTRACTION_PROMPT.format(
            question=question,
            answer_from_trace=answer_from_trace,
            candidates=", ".join(candidates),
            trace=trace,
        )

    def _parse_response(self, raw: str, trace: str) -> list[dict]:
        text = ConstraintExtractor._strip_thinking(raw.strip())
        if not text:
            logger.warning("Contrastive: empty after strip for trace: %s...", trace[:80])
            self.stats.fail_json_parse += 1
            return []

        json_str = ConstraintExtractor._extract_json_str(text)
        if json_str is None:
            logger.warning("Contrastive: no JSON for trace: %s...", trace[:80])
            self.stats.fail_json_parse += 1
            return []

        data = None
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            try:
                data = json.loads(ConstraintExtractor._repair_json(json_str))
            except json.JSONDecodeError:
                logger.warning("Contrastive: JSON parse failed for trace: %s...", trace[:80])
                self.stats.fail_json_parse += 1
                return []

        constraints = data.get("constraints", [])
        if not constraints:
            self.stats.fail_empty += 1
            return []

        valid = []
        for c in constraints:
            if not all(k in c for k in ("stance", "target", "z3_formula")):
                continue
            if c["stance"] not in _CONTRASTIVE_STANCES:
                continue
            c.setdefault("expression", c.get("z3_formula", ""))
            c.setdefault("source_step", 0)
            valid.append(c)

        if not valid:
            self.stats.fail_invalid_expr += 1
            return []

        self.stats.success += 1
        return valid

    def extract(self, trace: str, question: str,
                answer_from_trace: str, candidates: list[str]) -> list[dict]:
        prompt = self._build_prompt(trace, question, answer_from_trace, candidates)
        for attempt in range(self.parse_retries + 1):
            raw = self.llm.call(prompt)
            result = self._parse_response(raw, trace)
            if result or attempt == self.parse_retries:
                return result
            logger.info("Contrastive re-extract (attempt %d/%d)", attempt + 1, self.parse_retries)
        return []

    def extract_batch(self, traces: list[dict], question: str,
                      candidates: list[str]) -> list[list[dict]]:
        """Extract contrastive constraints from a batch of trace dicts.

        Each trace dict must have 'trace' (str) and 'answer' (str) keys.
        """
        if hasattr(self.llm, 'batch_call'):
            prompts = [
                self._build_prompt(t["trace"], question, t["answer"], candidates)
                for t in traces
            ]
            raw_results = self.llm.batch_call(prompts)
            return [self._parse_response(raw, t["trace"])
                    for raw, t in zip(raw_results, traces)]
        return [self.extract(t["trace"], question, t["answer"], candidates)
                for t in traces]
