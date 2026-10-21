"""Ontology Schema -> Constraint Specification Compiler.

Compiles an IE ontology schema (entity types, relation types, domain/range pairs)
into two constraint artifacts:
  1. EBNF grammar for XGrammar — enforces valid JSON structure + type vocabulary
  2. TypeConstraintSpec — semantic-level constraints for the LogitsProcessor

Input:  ontology_constraints.json (entity types, relation types, valid head/tail pairs)
Output: ConstraintSpec (for TypeConstraintProcessor) + CompiledGrammar (for XGrammar)
Depends: xgrammar, transformers (tokenizer)

Architecture: HF transformers + XGrammar (standalone).
- XGrammar handles structural constraints via EBNF grammar
- Custom LogitsProcessor handles semantic constraints (domain/range masking)
- Composed via LogitsProcessorList in model.generate()
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class RelationConstraint:
    """Domain/range constraint for a single relation type."""
    relation_type: str
    valid_pairs: list[tuple[str, str]]  # [(head_type, tail_type), ...]

    def valid_head_types(self) -> set[str]:
        return {h for h, _ in self.valid_pairs}

    def valid_tail_types(self) -> set[str]:
        return {t for _, t in self.valid_pairs}

    def valid_tail_types_for_head(self, head_type: str) -> set[str]:
        return {t for h, t in self.valid_pairs if h == head_type}

    def valid_head_types_for_tail(self, tail_type: str) -> set[str]:
        return {h for h, t in self.valid_pairs if t == tail_type}


@dataclass
class ConstraintSpec:
    """Complete constraint specification compiled from an ontology schema.

    Used by both the EBNF grammar generator and the TypeConstraintProcessor.
    """
    entity_types: list[str]
    relation_types: list[str]
    relation_constraints: dict[str, RelationConstraint]

    # Token-level mappings (populated by compile_for_tokenizer)
    entity_type_token_ids: dict[str, list[int]] = field(default_factory=dict)
    relation_type_token_ids: dict[str, list[int]] = field(default_factory=dict)
    # First-token mapping (populated by compile_type_constraints)
    entity_type_first_token: dict[str, int] = field(default_factory=dict)

    def get_constraint(self, relation_type: str) -> Optional[RelationConstraint]:
        return self.relation_constraints.get(relation_type)


class OntologyCompiler:
    """Compiles ontology_constraints.json into constraint artifacts."""

    def __init__(self, constraints_path: str | Path):
        with open(constraints_path) as f:
            self.raw = json.load(f)
        self.spec = self._build_spec()

    def _build_spec(self) -> ConstraintSpec:
        entity_types = self.raw["entity_types"]
        raw_rtypes = self.raw["relation_types"]

        # SciERC: list of strings; DocRED: dict of code->name
        if isinstance(raw_rtypes, dict):
            relation_types = list(raw_rtypes.keys())
        else:
            relation_types = raw_rtypes

        relation_constraints = {}
        for rtype, rdata in self.raw["relation_constraints"].items():
            relation_constraints[rtype] = RelationConstraint(
                relation_type=rtype,
                valid_pairs=[(h, t) for h, t in rdata["valid_pairs"]],
            )

        return ConstraintSpec(
            entity_types=entity_types,
            relation_types=relation_types,
            relation_constraints=relation_constraints,
        )

    # ── EBNF Grammar Generation ──────────────────────────────────────────

    def compile_ebnf(self) -> str:
        """Generate EBNF grammar for XGrammar.

        Enforces:
        - Valid JSON structure (object with "entities" and "relations" arrays)
        - Entity type must be one of the defined types (enum constraint)
        - Relation type must be one of the defined types (enum constraint)
        - head_type / tail_type must be valid entity types

        Does NOT enforce (handled by TypeConstraintProcessor at decode time):
        - Domain/range consistency (head_type, tail_type must match relation's valid_pairs)
        - Cross-reference consistency (entity mentioned in relation must exist in entities list)
        """
        entity_type_rule = " | ".join(
            f'"\\\"" "{etype}" "\\\"" ' for etype in self.spec.entity_types
        )
        relation_type_rule = " | ".join(
            f'"\\\"" "{rtype}" "\\\"" ' for rtype in self.spec.relation_types
        )

        ebnf = f'''root ::= "{{" ws entities-field "," ws relations-field ws "}}"

entities-field ::= "\\"entities\\"" ws ":" ws "[" ws entity-list? ws "]"
entity-list ::= entity ("," ws entity)*
entity ::= "{{" ws "\\"text\\"" ws ":" ws json-string "," ws "\\"type\\"" ws ":" ws entity-type ws "}}"

relations-field ::= "\\"relations\\"" ws ":" ws "[" ws relation-list? ws "]"
relation-list ::= relation ("," ws relation)*
relation ::= "{{" ws "\\"head\\"" ws ":" ws json-string "," ws "\\"tail\\"" ws ":" ws json-string "," ws "\\"type\\"" ws ":" ws relation-type "," ws "\\"head_type\\"" ws ":" ws entity-type "," ws "\\"tail_type\\"" ws ":" ws entity-type ws "}}"

entity-type ::= {entity_type_rule}
relation-type ::= {relation_type_rule}

json-string ::= "\\"" json-char* "\\""
json-char ::= [^"\\\\] | "\\\\" ["\\\\/bfnrt] | "\\\\u" [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F]

ws ::= [ \\t\\n]*
'''
        return ebnf

    # ── JSON Schema Generation ───────────────────────────────────────────

    def compile_json_schema(self) -> dict:
        """Generate JSON Schema for XGrammar's from_json_schema.

        XGrammar 2.0 can compile JSON Schema directly, often more
        efficiently. Uses enum constraints for type fields.
        """
        entity_schema = {
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "type": {"type": "string", "enum": self.spec.entity_types},
            },
            "required": ["text", "type"],
            "additionalProperties": False,
        }

        relation_schema = {
            "type": "object",
            "properties": {
                "head": {"type": "string"},
                "tail": {"type": "string"},
                "type": {"type": "string", "enum": self.spec.relation_types},
                "head_type": {"type": "string", "enum": self.spec.entity_types},
                "tail_type": {"type": "string", "enum": self.spec.entity_types},
            },
            "required": ["head", "tail", "type", "head_type", "tail_type"],
            "additionalProperties": False,
        }

        return {
            "type": "object",
            "properties": {
                "entities": {"type": "array", "items": entity_schema},
                "relations": {"type": "array", "items": relation_schema},
            },
            "required": ["entities", "relations"],
            "additionalProperties": False,
        }

    # ── XGrammar Integration ─────────────────────────────────────────────

    def compile_xgrammar(self, tokenizer) -> "xgrammar.CompiledGrammar":
        """Compile grammar for use with XGrammar's LogitsProcessor."""
        import xgrammar as xgr

        tokenizer_info = xgr.TokenizerInfo.from_huggingface(
            tokenizer, vocab_size=tokenizer.vocab_size
        )
        compiler = xgr.GrammarCompiler(tokenizer_info)

        schema_str = json.dumps(self.compile_json_schema())
        grammar = xgr.Grammar.from_json_schema(schema_str)
        return compiler.compile_grammar(grammar)

    # ── Tokenizer Alignment ──────────────────────────────────────────────

    def compile_for_tokenizer(self, tokenizer) -> ConstraintSpec:
        """Populate token-level mappings in the ConstraintSpec.

        Maps each entity/relation type string to its full token ID sequence.
        """
        for etype in self.spec.entity_types:
            token_ids = tokenizer.encode(etype, add_special_tokens=False)
            self.spec.entity_type_token_ids[etype] = token_ids

        for rtype in self.spec.relation_types:
            token_ids = tokenizer.encode(rtype, add_special_tokens=False)
            self.spec.relation_type_token_ids[rtype] = token_ids

        return self.spec

    # ── Type Constraint Compilation ──────────────────────────────────────

    def compile_type_constraints(self, tokenizer) -> dict[str, int]:
        """Build entity_type -> first_token_id mapping from tokenizer.

        Validates uniqueness: raises ValueError if two types share a first token.
        Pre-condition verified for Qwen3-8B on both SciERC and DocRED.
        """
        if not self.spec.entity_type_token_ids:
            self.compile_for_tokenizer(tokenizer)

        first_tokens_seen: dict[int, str] = {}

        for etype in self.spec.entity_types:
            token_ids = self.spec.entity_type_token_ids[etype]
            first_id = token_ids[0]

            if first_id in first_tokens_seen:
                raise ValueError(
                    f"First-token collision: '{etype}' and "
                    f"'{first_tokens_seen[first_id]}' share first token ID {first_id}"
                )
            first_tokens_seen[first_id] = etype
            self.spec.entity_type_first_token[etype] = first_id

        return dict(self.spec.entity_type_first_token)

    def build_processor(
        self,
        tokenizer,
        prompt_length: int = 0,
    ) -> list:
        """Assemble complete LogitsProcessor stack: [XGrammar, TypeConstraint].

        Returns list suitable for model.generate(logits_processor=...).
        """
        from .type_mask_processor import TypeConstraintProcessor

        self.compile_type_constraints(tokenizer)
        compiled_grammar = self.compile_xgrammar(tokenizer)

        import xgrammar as xgr

        processors = []
        processors.append(xgr.contrib.hf.LogitsProcessor(compiled_grammar))
        processors.append(TypeConstraintProcessor(self.spec, tokenizer, prompt_length))
        return processors


# ── Convenience ──────────────────────────────────────────────────────────

def compile_ontology(
    constraints_path: str | Path,
    tokenizer=None,
) -> tuple[ConstraintSpec, Optional["xgrammar.CompiledGrammar"]]:
    """One-call compilation: ontology JSON -> (ConstraintSpec, CompiledGrammar)."""
    compiler = OntologyCompiler(constraints_path)
    compiled_grammar = None

    if tokenizer is not None:
        compiler.compile_type_constraints(tokenizer)
        compiled_grammar = compiler.compile_xgrammar(tokenizer)

    return compiler.spec, compiled_grammar
