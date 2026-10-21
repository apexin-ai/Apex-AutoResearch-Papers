"""End-to-end integration tests for TypeConstraintProcessor.

Tests the full constraint pipeline with real Qwen3-8B tokenizer and SciERC
ontology constraints. Simulates JSON generation sequences token-by-token
and verifies logit masking at entity_type, head_type, tail_type positions.

Data: SciERC ontology_constraints.json (6 entity types, 7 relation types)
Tokenizer: Qwen3-8B (CPU only, no model weights loaded)
"""

import sys
import unittest
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from compiler.ontology_compiler import OntologyCompiler
from compiler.type_mask_processor import (
    FieldPosition,
    GenerationState,
    PositionDetector,
    TypeConstraintProcessor,
)

TOKENIZER_PATH = "/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B"
CONSTRAINTS_PATH = Path(__file__).resolve().parent.parent.parent / "ontology_constraints.json"


def _load_tokenizer():
    from transformers import AutoTokenizer
    return AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)


class TestE2ETypeConstraint(unittest.TestCase):
    """End-to-end tests with real Qwen3-8B tokenizer and SciERC constraints."""

    @classmethod
    def setUpClass(cls):
        if not CONSTRAINTS_PATH.exists():
            raise unittest.SkipTest(f"Constraints not found: {CONSTRAINTS_PATH}")
        cls.tokenizer = _load_tokenizer()
        cls.compiler = OntologyCompiler(CONSTRAINTS_PATH)
        cls.compiler.compile_type_constraints(cls.tokenizer)
        cls.spec = cls.compiler.spec

    def _make_processor(self, prompt_length=0):
        return TypeConstraintProcessor(self.spec, self.tokenizer, prompt_length=prompt_length)

    def _tokenize(self, text):
        """Tokenize text, return [1, seq_len] LongTensor."""
        ids = self.tokenizer.encode(text, add_special_tokens=False)
        return torch.tensor([ids], dtype=torch.long)

    def _make_scores(self):
        """Zero scores tensor [1, vocab_size]."""
        return torch.zeros(1, self.tokenizer.vocab_size)

    # ── Entity Type Position ────────────────────────────────────────────

    def test_entity_type_masking(self):
        """At entity type position, all 6 entity type first tokens stay unmasked."""
        proc = self._make_processor()
        input_ids = self._tokenize('{"entities": [{"text": "BERT", "type": "')
        scores = self._make_scores()

        result = proc(input_ids, scores)

        for etype in self.spec.entity_types:
            tid = self.spec.entity_type_first_token[etype]
            self.assertEqual(
                result[0, tid].item(), 0.0,
                f"{etype} (token {tid}) should be unmasked at entity_type position",
            )

    # ── Head Type Position ──────────────────────────────────────────────

    def test_head_type_constraint(self):
        """At head_type position, only valid head types for the relation are unmasked."""
        proc = self._make_processor()
        partial = (
            '{"entities": [{"text": "BLEU", "type": "Metric"}, '
            '{"text": "parsing", "type": "Task"}], '
            '"relations": [{"head": "BLEU", "tail": "parsing", '
            '"type": "Evaluate-for", "head_type": "'
        )
        input_ids = self._tokenize(partial)
        scores = self._make_scores()

        result = proc(input_ids, scores)

        constraint = self.spec.get_constraint("Evaluate-for")
        allowed = constraint.valid_head_types()

        for etype in self.spec.entity_types:
            tid = self.spec.entity_type_first_token[etype]
            if etype in allowed:
                self.assertEqual(result[0, tid].item(), 0.0,
                                 f"{etype} should be allowed as head for Evaluate-for")
            else:
                self.assertEqual(result[0, tid].item(), float("-inf"),
                                 f"{etype} should be masked as head for Evaluate-for")

    # ── Tail Type Position ──────────────────────────────────────────────

    def test_tail_type_constraint(self):
        """At tail_type with head=Metric, only valid (Evaluate-for, Metric, T) tails unmasked."""
        proc = self._make_processor()
        partial = (
            '{"entities": [{"text": "BLEU", "type": "Metric"}, '
            '{"text": "parsing", "type": "Task"}], '
            '"relations": [{"head": "BLEU", "tail": "parsing", '
            '"type": "Evaluate-for", "head_type": "Metric", "tail_type": "'
        )
        input_ids = self._tokenize(partial)
        scores = self._make_scores()

        result = proc(input_ids, scores)

        constraint = self.spec.get_constraint("Evaluate-for")
        allowed = constraint.valid_tail_types_for_head("Metric")
        self.assertGreater(len(allowed), 0)

        masked_count = 0
        for etype in self.spec.entity_types:
            tid = self.spec.entity_type_first_token[etype]
            if etype in allowed:
                self.assertEqual(result[0, tid].item(), 0.0,
                                 f"{etype} should be allowed as tail for (Evaluate-for, Metric)")
            else:
                self.assertEqual(result[0, tid].item(), float("-inf"),
                                 f"{etype} should be masked as tail for (Evaluate-for, Metric)")
                masked_count += 1

        self.assertGreater(masked_count, 0, "At least one type should be masked")

    # ── Entity Registry ─────────────────────────────────────────────────

    def test_entity_registry_tracking(self):
        """After generating entities, EntityRegistry records text->type mappings."""
        proc = self._make_processor()
        partial = (
            '{"entities": [{"text": "BERT", "type": "Method"}, '
            '{"text": "NER", "type": "Task"}, '
            '{"text": "F1", "type": "Metric"}], "relations": ['
        )
        input_ids = self._tokenize(partial)
        scores = self._make_scores()
        proc(input_ids, scores)

        reg = proc.state.entity_registry
        self.assertEqual(reg.get_type("BERT"), "Method")
        self.assertEqual(reg.get_type("NER"), "Task")
        self.assertEqual(reg.get_type("F1"), "Metric")
        self.assertIsNone(reg.get_type("UNKNOWN"))

    # ── Semantic Mask Non-Empty ──────────────────────────────────────────

    def test_semantic_mask_nonempty_for_all_relations(self):
        """For every (relation, head_type) pair, at least one tail type is allowed."""
        for rtype in self.spec.relation_types:
            constraint = self.spec.get_constraint(rtype)
            self.assertIsNotNone(constraint, f"Missing constraint for {rtype}")

            for head_type in constraint.valid_head_types():
                allowed = constraint.valid_tail_types_for_head(head_type)
                self.assertGreater(
                    len(allowed), 0,
                    f"No valid tail types for ({rtype}, head={head_type})",
                )
                for t in allowed:
                    self.assertIn(t, self.spec.entity_types,
                                  f"Tail type '{t}' not in entity_types for {rtype}")

    def test_semantic_mask_intersection_with_grammar(self):
        """At tail_type position, semantic-masked tokens are a subset of type first tokens.

        Ensures the semantic mask only touches type tokens, never arbitrary vocab tokens.
        """
        proc = self._make_processor()
        partial = (
            '{"entities": [{"text": "X", "type": "Method"}], '
            '"relations": [{"head": "X", "tail": "Y", '
            '"type": "Used-for", "head_type": "Method", "tail_type": "'
        )
        input_ids = self._tokenize(partial)
        scores = torch.randn(1, self.tokenizer.vocab_size)
        original = scores.clone()

        result = proc(input_ids, scores)

        type_tids = set(self.spec.entity_type_first_token.values())
        mask = torch.ones(self.tokenizer.vocab_size, dtype=torch.bool)
        mask[list(type_tids)] = False
        # Non-type tokens must be completely untouched
        torch.testing.assert_close(result[0, mask], original[0, mask])

    # ── Full Triple Generation ──────────────────────────────────────────

    def test_full_triple_generation(self):
        """Simulate generating a full relation triple, verify masking at each stage."""
        entities = (
            '{"entities": [{"text": "BERT", "type": "Method"}, '
            '{"text": "NER", "type": "Task"}], "relations": ['
        )

        # Stage 1: relation type position -- no masking (handled by XGrammar)
        proc = self._make_processor()
        text1 = entities + '{"head": "BERT", "tail": "NER", "type": "'
        result = proc(self._tokenize(text1), self._make_scores())
        self.assertTrue(torch.all(result == 0.0),
                        "Relation type position should not mask")

        # Stage 2: head_type position
        proc = self._make_processor()
        text2 = entities + '{"head": "BERT", "tail": "NER", "type": "Used-for", "head_type": "'
        result = proc(self._tokenize(text2), self._make_scores())

        constraint = self.spec.get_constraint("Used-for")
        allowed_heads = constraint.valid_head_types()
        for etype in self.spec.entity_types:
            tid = self.spec.entity_type_first_token[etype]
            if etype in allowed_heads:
                self.assertEqual(result[0, tid].item(), 0.0)
            else:
                self.assertEqual(result[0, tid].item(), float("-inf"))

        # Stage 3: tail_type position with head=Method
        proc = self._make_processor()
        text3 = (entities +
                 '{"head": "BERT", "tail": "NER", "type": "Used-for", '
                 '"head_type": "Method", "tail_type": "')
        result = proc(self._tokenize(text3), self._make_scores())

        allowed_tails = constraint.valid_tail_types_for_head("Method")
        for etype in self.spec.entity_types:
            tid = self.spec.entity_type_first_token[etype]
            if etype in allowed_tails:
                self.assertEqual(result[0, tid].item(), 0.0,
                                 f"{etype} should be allowed as tail for (Used-for, Method)")
            else:
                self.assertEqual(result[0, tid].item(), float("-inf"),
                                 f"{etype} should be masked as tail for (Used-for, Method)")

    # ── Prompt Offset ───────────────────────────────────────────────────

    def test_prompt_offset(self):
        """prompt_length correctly separates prompt from generated output."""
        prompt = "Extract entities and relations from the text:\n"
        prompt_ids = self.tokenizer.encode(prompt, add_special_tokens=False)

        proc = self._make_processor(prompt_length=len(prompt_ids))

        gen_json = '{"entities": [{"text": "BERT", "type": "'
        gen_ids = self.tokenizer.encode(gen_json, add_special_tokens=False)

        full_ids = torch.tensor([prompt_ids + gen_ids], dtype=torch.long)
        scores = self._make_scores()

        result = proc(full_ids, scores)

        for etype in self.spec.entity_types:
            tid = self.spec.entity_type_first_token[etype]
            self.assertEqual(result[0, tid].item(), 0.0,
                             f"{etype} should be unmasked with prompt offset")

    # ── Free Text ───────────────────────────────────────────────────────

    def test_free_text_no_masking(self):
        """At free text positions (entity text), no type masking is applied."""
        proc = self._make_processor()
        input_ids = self._tokenize('{"entities": [{"text": "')
        scores = self._make_scores()

        result = proc(input_ids, scores)
        self.assertTrue(torch.all(result == 0.0),
                        "Free text position should not mask anything")

    # ── Multiple Relations ──────────────────────────────────────────────

    def test_multiple_relations_independent_state(self):
        """Second relation uses its own constraint, independent of the first."""
        proc = self._make_processor()
        partial = (
            '{"entities": [{"text": "BERT", "type": "Method"}, '
            '{"text": "F1", "type": "Metric"}, '
            '{"text": "NER", "type": "Task"}], '
            '"relations": [{"head": "BERT", "tail": "NER", '
            '"type": "Used-for", "head_type": "Method", "tail_type": "Task"}, '
            '{"head": "F1", "tail": "BERT", '
            '"type": "Evaluate-for", "head_type": "Metric", "tail_type": "'
        )
        input_ids = self._tokenize(partial)
        scores = self._make_scores()
        result = proc(input_ids, scores)

        constraint = self.spec.get_constraint("Evaluate-for")
        allowed = constraint.valid_tail_types_for_head("Metric")

        for etype in self.spec.entity_types:
            tid = self.spec.entity_type_first_token[etype]
            if etype in allowed:
                self.assertEqual(result[0, tid].item(), 0.0,
                                 f"{etype} should be allowed for 2nd relation (Evaluate-for/Metric)")
            else:
                self.assertEqual(result[0, tid].item(), float("-inf"),
                                 f"{etype} should be masked for 2nd relation (Evaluate-for/Metric)")

    # ── First Token ID Verification ─────────────────────────────────────

    def test_first_token_ids_match_tokenizer(self):
        """Compiled first-token IDs match direct tokenizer.encode() results."""
        for etype in self.spec.entity_types:
            expected = self.tokenizer.encode(etype, add_special_tokens=False)[0]
            actual = self.spec.entity_type_first_token[etype]
            self.assertEqual(actual, expected,
                             f"First token mismatch for {etype}: compiled={actual}, tokenizer={expected}")

    def test_first_token_uniqueness(self):
        """All entity type first tokens are unique (required for simple masking)."""
        tids = list(self.spec.entity_type_first_token.values())
        self.assertEqual(len(tids), len(set(tids)), "First-token IDs must be unique")


if __name__ == "__main__":
    unittest.main(verbosity=2)
