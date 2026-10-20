"""Auto-formalizer: convert natural language atomic claims to FOL (Z3 syntax).

Takes an AtomicClaim (text) + a shared vocabulary and produces a Z3-parseable
FOL formula string. Uses an LLM for translation, then validates the output
by actually constructing Z3 objects from the vocabulary and evaluating
the expression string.

Input:  AtomicClaim + vocab dict
Output: AtomicClaim with fol, z3_parseable, fol_error fields populated
"""

import logging
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

from openai import OpenAI

from ..types import AtomicClaim
from ..config import APIConfig
from ..cost_tracker import get_tracker

logger = logging.getLogger(__name__)

_FORMALIZE_PROMPT = """\
You are a first-order logic formalization expert. Convert the given natural language claim \
into a Z3 Python expression string using ONLY the provided vocabulary.

**Vocabulary:**
{vocab_section}

**Available Z3 constructs:**
- Quantifiers: `ForAll([x], body)`, `Exists([x], body)`
- Connectives: `And(a, b)`, `Or(a, b)`, `Not(a)`, `Implies(a, b)`
- Variables for quantifiers: use `x`, `y`, `z` (these are Int-sorted)
- Constants: refer by name directly, e.g. `cat`, `dog`
- Unary predicates: `Green(cat)`, `ForAll([x], Implies(Green(x), Big(x)))`
- Binary predicates: `Likes(cat, dog)`, `ForAll([x], Exists([y], Chases(x, y)))`

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

**Rules:**
- Output ONLY the Z3 expression string, nothing else.
- Use ONLY predicates and constants from the vocabulary above.
- Do NOT define new symbols.
- Do NOT include `import` statements or variable declarations.
- For universal statements like "All green things are big", use: `ForAll([x], Implies(Green(x), Big(x)))`
- For negation "X is not green", use: `Not(Green(x))` where x is the constant for X.

**Claim:** {claim}

**Z3 expression:**"""


class AutoFormalizer:

    def __init__(self, api_config: APIConfig):
        self._api = api_config
        self._client = OpenAI(
            base_url=api_config.formalization_base_url,
            api_key=[REDACTED],
            timeout=api_config.timeout,
        )

    def formalize(self, claim: AtomicClaim, vocab: dict) -> AtomicClaim:
        """Formalize a single atomic claim using LLM + Z3 validation."""
        vocab_section = self._format_vocab(vocab)

        last_error = None
        for attempt in range(self._api.max_retries):
            try:
                fol_str = self._call_llm(claim.text, vocab_section)
                fol_str = self._clean_fol(fol_str)
                valid, err = self.validate_z3_syntax(fol_str, vocab)
                claim.fol = fol_str
                claim.z3_parseable = valid
                claim.fol_error = err
                if valid:
                    logger.debug(
                        "Formalized claim %d of chain %d: %s -> %s",
                        claim.claim_index,
                        claim.chain_id,
                        claim.text[:60],
                        fol_str,
                    )
                    return claim
                last_error = err
                logger.debug(
                    "Z3 validation failed (attempt %d) for '%s': %s",
                    attempt + 1,
                    claim.text[:60],
                    err,
                )
            except Exception as e:
                last_error = str(e)
                logger.warning(
                    "Formalize attempt %d failed for claim %d of chain %d: %s",
                    attempt + 1,
                    claim.claim_index,
                    claim.chain_id,
                    e,
                )

        # Exhausted retries — keep last result
        claim.fol = claim.fol or ""
        claim.z3_parseable = False
        claim.fol_error = str(last_error) if last_error else "unknown error"
        logger.warning(
            "Failed to formalize claim %d of chain %d after %d attempts: %s",
            claim.claim_index,
            claim.chain_id,
            self._api.max_retries,
            claim.text[:80],
        )
        return claim

    def formalize_batch(
        self, claims: list[AtomicClaim], vocab: dict, max_workers: int = 8
    ) -> list[AtomicClaim]:
        """Formalize a list of claims with concurrent API calls."""
        if not claims:
            return claims

        results = [None] * len(claims)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.formalize, c, vocab): i
                for i, c in enumerate(claims)
            }
            for future in as_completed(futures):
                idx = futures[future]
                try:
                    results[idx] = future.result()
                except Exception as e:
                    logger.warning("Formalization failed for claim %d: %s", idx, e)
                    results[idx] = claims[idx]

        success = sum(1 for r in results if r and r.z3_parseable)
        logger.info(
            "Batch formalization: %d/%d claims successfully formalized",
            success,
            len(claims),
        )
        return results

    def validate_z3_syntax(
        self, fol_str: str, vocab: dict | None = None
    ) -> tuple[bool, str | None]:
        """Validate a FOL string via Z3 subprocess sandbox.

        The eval() runs in a persistent child process. If Z3's C++ layer
        crashes (SIGABRT), the child dies and is auto-restarted — the main
        pipeline process survives.

        Returns (True, None) on success, (False, error_message) on failure.
        """
        if not fol_str or not fol_str.strip():
            return False, "empty formula"

        from ..z3_sandbox import get_sandbox
        return get_sandbox().validate(fol_str, vocab or {"predicates": {}, "constants": {}})

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _format_vocab(vocab: dict) -> str:
        """Format vocab dict as a readable string for the LLM prompt."""
        lines = []
        preds = vocab.get("predicates", {})
        consts = vocab.get("constants", {})

        if preds:
            lines.append("Predicates:")
            for name, info in preds.items():
                arity = info.get("arity", 1)
                desc = info.get("description", "")
                if arity == 1:
                    sig = f"{name}(x)"
                elif arity == 2:
                    sig = f"{name}(x, y)"
                else:
                    args = ", ".join(f"x{i}" for i in range(arity))
                    sig = f"{name}({args})"
                lines.append(f"  - {sig}: {desc}")

        if consts:
            lines.append("Constants:")
            for name, info in consts.items():
                desc = info.get("description", name)
                lines.append(f"  - {name}: {desc}")

        return "\n".join(lines)

    def _call_llm(self, claim_text: str, vocab_section: str) -> str:
        prompt = _FORMALIZE_PROMPT.format(
            vocab_section=vocab_section, claim=claim_text
        )
        resp = self._client.chat.completions.create(
            model=self._api.formalization_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=256,
        )
        if hasattr(resp, 'usage') and resp.usage:
            get_tracker().record(
                model=self._api.formalization_model,
                prompt_tokens=resp.usage.prompt_tokens or 0,
                completion_tokens=resp.usage.completion_tokens or 0,
                module="autoformalize",
            )
        return resp.choices[0].message.content.strip()

    @staticmethod
    def _clean_fol(text: str) -> str:
        """Strip markdown fences, backticks, and stray formatting from LLM output."""
        text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
        text = re.sub(r"```(?:python)?\s*", "", text).strip()
        text = text.strip("`").strip()
        text = re.sub(r"^(?:Z3 expression:\s*|Output:\s*|Answer:\s*)", "", text, flags=re.IGNORECASE).strip()
        lines = [l.strip() for l in text.splitlines() if l.strip() and not l.strip().startswith("#")]
        if lines:
            return " ".join(lines)
        return text
