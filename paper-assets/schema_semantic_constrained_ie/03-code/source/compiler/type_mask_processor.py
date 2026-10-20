"""LogitsProcessor for runtime domain/range type constraint enforcement.

Layered on top of XGrammar's structural constraints:
- XGrammar (Layer 1): Guarantees valid JSON, entity/relation type strings from enum
- TypeConstraintProcessor (Layer 2): Guarantees domain/range consistency

At each generation step:
1. Detect current JSON field position (entity type? relation head_type? tail_type?)
2. If at entity type position -> allow all entity type first tokens
3. If at head_type position -> mask to types valid for the current relation
4. If at tail_type position -> mask to types valid for (relation_type, head_type) pair
5. Apply mask: disallowed type tokens -> logits = -inf

Composition:
    grammar_processor = xgr.contrib.hf.LogitsProcessor(compiled_grammar)
    type_processor = TypeConstraintProcessor(spec, tokenizer)
    model.generate(logits_processor=[grammar_processor, type_processor])

Framework: HuggingFace transformers (API: __call__(input_ids, scores) -> scores)
Depends on: ontology_compiler.ConstraintSpec (type->token mappings + relation constraints)

Verified first-token IDs (Qwen3-8B tokenizer, context-independent):
  SciERC:
    Task=6262, Method=3523, Material=13415, Metric=54310,
    OtherScientificTerm=11409, Generic=19964
  DocRED:
    PER=9654, ORG=44927, LOC=12052, TIME=18129, NUM=17488, MISC=44
All first tokens are unique within each dataset -> simple first-token masking
is sufficient, no trie-based multi-token tracking needed.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional

import torch
from transformers import LogitsProcessor, PreTrainedTokenizerBase

from .ontology_compiler import ConstraintSpec


class FieldPosition(Enum):
    """Current position in the JSON output structure."""
    UNKNOWN = auto()
    ENTITY_TYPE = auto()        # Inside entity's "type" field value
    RELATION_TYPE = auto()      # Inside relation's "type" field value
    RELATION_HEAD_TYPE = auto()  # Inside relation's "head_type" field value
    RELATION_TAIL_TYPE = auto()  # Inside relation's "tail_type" field value
    FREE_TEXT = auto()           # Entity text, relation head/tail text, etc.


@dataclass
class EntityRegistry:
    """Runtime registry of generated entities and their types.

    Tracks text->type mappings from the entities list so that when a relation
    references an entity by text, we know its type for domain/range checking.
    """
    entities: dict[str, str] = field(default_factory=dict)

    def register(self, text: str, entity_type: str):
        self.entities[text] = entity_type

    def get_type(self, text: str) -> Optional[str]:
        return self.entities.get(text)

    def clear(self):
        self.entities.clear()


@dataclass
class GenerationState:
    """Tracks the state of JSON generation for constraint application."""
    position: FieldPosition = FieldPosition.UNKNOWN
    current_relation_type: Optional[str] = None
    current_head_type: Optional[str] = None
    current_head_text: Optional[str] = None
    current_tail_text: Optional[str] = None
    entity_registry: EntityRegistry = field(default_factory=EntityRegistry)
    in_entities_section: bool = True

    def reset(self):
        self.position = FieldPosition.UNKNOWN
        self.current_relation_type = None
        self.current_head_type = None
        self.current_head_text = None
        self.current_tail_text = None
        self.entity_registry.clear()
        self.in_entities_section = True


class PositionDetector:
    """Detects current field position by parsing generated text.

    Regex-based parsing of JSON text generated so far. Called at every
    decoding step, so only inspects the tail of the text.

    Future optimization: use XGrammar's GrammarMatcher state for O(1) per step
    instead of O(n) text parsing.
    """

    _RE_TAIL_TYPE = re.compile(r'"tail_type"\s*:\s*"[^"]*$')
    _RE_HEAD_TYPE = re.compile(r'"head_type"\s*:\s*"[^"]*$')
    _RE_TYPE_FIELD = re.compile(r'"type"\s*:\s*"[^"]*$')

    _RE_ENTITY = re.compile(r'"text"\s*:\s*"([^"]+)"\s*,\s*"type"\s*:\s*"([^"]+)"')

    _RE_REL_TYPE_VAL = re.compile(r'"type"\s*:\s*"([^"]+)"')
    _RE_HEAD_TYPE_VAL = re.compile(r'"head_type"\s*:\s*"([^"]+)"')
    _RE_HEAD_TEXT_VAL = re.compile(r'"head"\s*:\s*"([^"]+)"')
    _RE_TAIL_TEXT_VAL = re.compile(r'"tail"\s*:\s*"([^"]+)"')
    _RE_REL_START = re.compile(r'\{\s*"head"')

    @classmethod
    def detect(cls, generated_text: str, state: GenerationState) -> FieldPosition:
        """Determine which JSON field is currently being generated.

        Mutates state in place: updates entity registry, current relation type,
        current head type, etc.
        """
        if '"relations"' in generated_text:
            state.in_entities_section = False

        for match in cls._RE_ENTITY.finditer(generated_text):
            state.entity_registry.register(match.group(1), match.group(2))

        # Find the last relation object being generated
        last_rel_start = -1
        for m in cls._RE_REL_START.finditer(generated_text):
            last_rel_start = m.start()

        if last_rel_start >= 0:
            partial_rel = generated_text[last_rel_start:]

            m = cls._RE_REL_TYPE_VAL.search(partial_rel)
            if m:
                state.current_relation_type = m.group(1)

            m = cls._RE_HEAD_TYPE_VAL.search(partial_rel)
            if m:
                state.current_head_type = m.group(1)

            m = cls._RE_HEAD_TEXT_VAL.search(partial_rel)
            if m:
                state.current_head_text = m.group(1)

            m = cls._RE_TAIL_TEXT_VAL.search(partial_rel)
            if m:
                state.current_tail_text = m.group(1)

        # Determine position from last 100 chars
        tail = generated_text[-100:]

        if cls._RE_TAIL_TYPE.search(tail):
            return FieldPosition.RELATION_TAIL_TYPE

        if cls._RE_HEAD_TYPE.search(tail):
            return FieldPosition.RELATION_HEAD_TYPE

        if cls._RE_TYPE_FIELD.search(tail):
            if state.in_entities_section:
                return FieldPosition.ENTITY_TYPE
            else:
                return FieldPosition.RELATION_TYPE

        return FieldPosition.FREE_TEXT


class TypeConstraintProcessor(LogitsProcessor):
    """Enforces domain/range type constraints during autoregressive generation.

    Constraint logic:
    - ENTITY_TYPE: Allow all entity type first tokens (defense-in-depth with XGrammar)
    - RELATION_HEAD_TYPE: Given relation R, allow types T where exists T' s.t. (T,T') in R.valid_pairs
    - RELATION_TAIL_TYPE: Given relation R and head H, allow types T where (H,T) in R.valid_pairs
      <-- THIS IS THE KEY CONSTRAINT

    Usage:
        spec, compiled_grammar = compile_ontology("ontology_constraints.json", tokenizer)
        grammar_proc = xgr.contrib.hf.LogitsProcessor(compiled_grammar)
        type_proc = TypeConstraintProcessor(spec, tokenizer, prompt_length=len(input_ids[0]))
        output = model.generate(**inputs, logits_processor=[grammar_proc, type_proc])
    """

    def __init__(
        self,
        spec: ConstraintSpec,
        tokenizer: PreTrainedTokenizerBase,
        prompt_length: int = 0,
    ):
        self.spec = spec
        self.tokenizer = tokenizer
        self.prompt_length = prompt_length
        self.state = GenerationState()
        self.detector = PositionDetector()

        self._type_first_token, self._all_type_first_tokens = self._build_first_token_map()

    def _build_first_token_map(self) -> tuple[dict[str, int], set[int]]:
        """Build entity_type -> first_token_id mapping.

        Uses pre-computed token IDs from ConstraintSpec.entity_type_first_token
        (set by OntologyCompiler.compile_type_constraints) if available.
        Falls back to ConstraintSpec.entity_type_token_ids, then tokenizer.encode().

        All first tokens verified unique for Qwen3-8B on both SciERC and DocRED,
        so simple first-token masking is sufficient (no trie needed).
        """
        type_first_token: dict[str, int] = {}
        all_first_tokens: set[int] = set()

        for etype in self.spec.entity_types:
            # Priority: pre-compiled first token > full token list > tokenizer
            if etype in self.spec.entity_type_first_token:
                first_id = self.spec.entity_type_first_token[etype]
            else:
                token_ids = self.spec.entity_type_token_ids.get(etype)
                if token_ids is None:
                    token_ids = self.tokenizer.encode(etype, add_special_tokens=False)
                first_id = token_ids[0]

            type_first_token[etype] = first_id
            all_first_tokens.add(first_id)

        return type_first_token, all_first_tokens

    def _detect_position(self, generated_text: str) -> FieldPosition:
        """Detect current token's semantic position in the JSON structure.

        Delegates to PositionDetector.detect() which parses the generated text
        and updates self.state (relation type, head type, entity registry, etc.).
        """
        return self.detector.detect(generated_text, self.state)

    def __call__(
        self,
        input_ids: torch.LongTensor,
        scores: torch.FloatTensor,
    ) -> torch.FloatTensor:
        """Apply domain/range constraints to logits.

        Args:
            input_ids: [batch_size, seq_len] -- full sequence including prompt
            scores: [batch_size, vocab_size] -- logits for next token

        Returns:
            Modified scores with disallowed type tokens set to -inf
        """
        batch_size = input_ids.shape[0]

        for batch_idx in range(batch_size):
            generated_ids = input_ids[batch_idx, self.prompt_length:].tolist()
            generated_text = self.tokenizer.decode(
                generated_ids, skip_special_tokens=True
            )

            position = self._detect_position(generated_text)

            if position == FieldPosition.ENTITY_TYPE:
                scores[batch_idx] = self._mask_entity_type(scores[batch_idx])

            elif position == FieldPosition.RELATION_HEAD_TYPE:
                scores[batch_idx] = self._mask_head_type(scores[batch_idx])

            elif position == FieldPosition.RELATION_TAIL_TYPE:
                scores[batch_idx] = self._mask_tail_type(scores[batch_idx])

        return scores

    def _mask_entity_type(self, logits: torch.FloatTensor) -> torch.FloatTensor:
        """At entity type position, allow only valid entity type first tokens.

        XGrammar's enum constraint already restricts to valid types, but this
        provides defense-in-depth by masking at the logit level.
        All entity types are allowed here (no domain/range filtering at this stage).
        """
        return self._apply_type_mask(logits, set(self.spec.entity_types))

    def _mask_head_type(self, logits: torch.FloatTensor) -> torch.FloatTensor:
        """Mask entity types that cannot be head_type for the current relation.

        Strategy: intersect entity registry type with D/R-valid types.
        - If entity type known AND D/R-valid → force that single type
        - If entity type known but NOT D/R-valid → use D/R constraint
        - If entity type unknown → use D/R constraint
        """
        rel_type = self.state.current_relation_type
        constraint = self.spec.get_constraint(rel_type) if rel_type else None
        allowed_dr = constraint.valid_head_types() if constraint else None

        head_text = self.state.current_head_text
        if head_text:
            actual_type = self.state.entity_registry.get_type(head_text)
            if actual_type and actual_type in self._type_first_token:
                if allowed_dr is None or actual_type in allowed_dr:
                    return self._apply_type_mask(logits, {actual_type})

        if allowed_dr is not None:
            return self._apply_type_mask(logits, allowed_dr)
        return logits

    def _mask_tail_type(self, logits: torch.FloatTensor) -> torch.FloatTensor:
        """Mask entity types that cannot be tail_type for (relation, head_type).

        Strategy: intersect entity registry type with D/R-valid types.
        - If entity type known AND D/R-valid → force that single type
        - If entity type known but NOT D/R-valid → use D/R constraint
        - If entity type unknown → use D/R constraint
        """
        rel_type = self.state.current_relation_type
        head_type = self.state.current_head_type
        constraint = self.spec.get_constraint(rel_type) if rel_type else None

        if constraint is not None:
            if head_type is not None:
                allowed_dr = constraint.valid_tail_types_for_head(head_type)
            else:
                allowed_dr = constraint.valid_tail_types()
        else:
            allowed_dr = None

        tail_text = self.state.current_tail_text
        if tail_text:
            actual_type = self.state.entity_registry.get_type(tail_text)
            if actual_type and actual_type in self._type_first_token:
                if allowed_dr is None or actual_type in allowed_dr:
                    return self._apply_type_mask(logits, {actual_type})

        if allowed_dr is not None:
            return self._apply_type_mask(logits, allowed_dr)
        return logits

    def _apply_type_mask(
        self,
        logits: torch.FloatTensor,
        allowed_types: set[str],
    ) -> torch.FloatTensor:
        """Set logits of disallowed type first-tokens to -inf.

        Only masks the FIRST token of each type string. XGrammar's grammar
        ensures remaining tokens are forced once the first is selected.

        First-token uniqueness verified for Qwen3-8B:
          SciERC: Task(6262), Method(3523), Material(13415), Metric(54310),
                  OtherScientificTerm(11409), Generic(19964)
          DocRED: PER(9654), ORG(44927), LOC(12052), TIME(18129),
                  NUM(17488), MISC(44)
        """
        disallowed_first_tokens = [
            tid for etype, tid in self._type_first_token.items()
            if etype not in allowed_types
        ]

        if disallowed_first_tokens:
            logits[disallowed_first_tokens] = float("-inf")

        return logits

    def reset(self):
        """Reset state between generate() calls."""
        self.state.reset()


# ── Integration Helper ───────────────────────────────────────────────────

def build_constrained_processors(
    constraints_path: str,
    tokenizer: PreTrainedTokenizerBase,
    prompt_length: int,
) -> list[LogitsProcessor]:
    """Build the complete LogitsProcessor stack for constrained generation.

    Returns a list suitable for LogitsProcessorList:
        [xgrammar_processor, type_constraint_processor]

    Usage:
        processors = build_constrained_processors(
            "ontology_constraints.json", tokenizer, len(input_ids[0])
        )
        output = model.generate(**inputs, logits_processor=processors)
    """
    import xgrammar as xgr
    from .ontology_compiler import compile_ontology

    spec, compiled_grammar = compile_ontology(constraints_path, tokenizer)

    processors = []

    if compiled_grammar is not None:
        grammar_processor = xgr.contrib.hf.LogitsProcessor(compiled_grammar)
        processors.append(grammar_processor)

    type_processor = TypeConstraintProcessor(spec, tokenizer, prompt_length)
    processors.append(type_processor)

    return processors
