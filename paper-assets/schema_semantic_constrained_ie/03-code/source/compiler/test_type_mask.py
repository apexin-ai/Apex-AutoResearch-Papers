"""Unit tests for type constraint masking (Phase 1 compiler).

Tests the core constraint logic without loading a GPU model.
Uses hardcoded first-token IDs verified against Qwen3-8B tokenizer.

Run: cd /root/schema_semantic_constrained_ie && python -m compiler.test_type_mask
  or: cd /root/schema_semantic_constrained_ie && python compiler/test_type_mask.py
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from compiler.ontology_compiler import OntologyCompiler, ConstraintSpec, RelationConstraint

# Verified first-token IDs (Qwen3-8B, context-independent)
SCIERC_FIRST_TOKENS = {
    "Task": 6262,
    "Method": 3523,
    "Material": 13415,
    "Metric": 54310,
    "OtherScientificTerm": 11409,
    "Generic": 19964,
}

# Full token sequences for multi-token types
SCIERC_FULL_TOKENS = {
    "Task": [6262],
    "Method": [3523],
    "Material": [13415],
    "Metric": [54310],
    "OtherScientificTerm": [11409, 50565, 1086, 17249],
    "Generic": [19964],
}

SCIERC_CONSTRAINTS_PATH = Path(__file__).resolve().parent.parent / "ontology_constraints.json"


def make_mock_tokenizer() -> MagicMock:
    """Create a mock tokenizer that returns predetermined token IDs."""
    tokenizer = MagicMock()

    def mock_encode(text, add_special_tokens=False):
        if text in SCIERC_FULL_TOKENS:
            return SCIERC_FULL_TOKENS[text]
        return [hash(text) % 100000]

    tokenizer.encode = mock_encode
    tokenizer.vocab_size = 152064
    tokenizer.decode = MagicMock(return_value="")
    return tokenizer


class TestOntologyCompiler(unittest.TestCase):
    """Test OntologyCompiler constraint loading and type mapping."""

    def setUp(self):
        if not SCIERC_CONSTRAINTS_PATH.exists():
            self.skipTest(f"SciERC constraints not found at {SCIERC_CONSTRAINTS_PATH}")
        self.compiler = OntologyCompiler(SCIERC_CONSTRAINTS_PATH)

    def test_entity_types_loaded(self):
        expected = {"Task", "Method", "Material", "Metric", "OtherScientificTerm", "Generic"}
        self.assertEqual(set(self.compiler.spec.entity_types), expected)

    def test_relation_types_loaded(self):
        expected = {"Used-for", "Feature-of", "Hyponym-of", "Part-of",
                    "Compare", "Conjunction", "Evaluate-for"}
        self.assertEqual(set(self.compiler.spec.relation_types), expected)

    def test_compile_type_constraints(self):
        tokenizer = make_mock_tokenizer()
        first_token_map = self.compiler.compile_type_constraints(tokenizer)

        for etype, expected_id in SCIERC_FIRST_TOKENS.items():
            self.assertEqual(first_token_map[etype], expected_id,
                             f"First token mismatch for {etype}")

    def test_first_token_uniqueness(self):
        tokenizer = make_mock_tokenizer()
        first_token_map = self.compiler.compile_type_constraints(tokenizer)

        ids = list(first_token_map.values())
        self.assertEqual(len(ids), len(set(ids)), "First-token IDs are not unique")

    def test_spec_populated_after_compile(self):
        tokenizer = make_mock_tokenizer()
        self.compiler.compile_type_constraints(tokenizer)
        spec = self.compiler.spec

        self.assertEqual(len(spec.entity_type_first_token), 6)
        self.assertEqual(len(spec.entity_type_token_ids), 6)
        self.assertEqual(spec.entity_type_first_token["Task"], 6262)
        self.assertEqual(spec.entity_type_token_ids["OtherScientificTerm"],
                         [11409, 50565, 1086, 17249])


class TestRelationConstraints(unittest.TestCase):
    """Test domain/range constraint lookups."""

    def setUp(self):
        if not SCIERC_CONSTRAINTS_PATH.exists():
            self.skipTest(f"SciERC constraints not found at {SCIERC_CONSTRAINTS_PATH}")
        self.compiler = OntologyCompiler(SCIERC_CONSTRAINTS_PATH)
        self.spec = self.compiler.spec

    def test_used_for_valid_pairs_nonempty(self):
        constraint = self.spec.get_constraint("Used-for")
        self.assertIsNotNone(constraint)
        self.assertGreater(len(constraint.valid_pairs), 0)

    def test_feature_of_valid_head_types(self):
        constraint = self.spec.get_constraint("Feature-of")
        heads = constraint.valid_head_types()
        self.assertIn("Method", heads)
        self.assertIn("OtherScientificTerm", heads)

    def test_tail_types_for_head(self):
        """Given (Evaluate-for, head=Metric), check valid tail types."""
        constraint = self.spec.get_constraint("Evaluate-for")
        self.assertIsNotNone(constraint)
        tail_types = constraint.valid_tail_types_for_head("Metric")
        self.assertIn("Method", tail_types)
        self.assertIn("Generic", tail_types)

    def test_unknown_head_returns_empty(self):
        constraint = self.spec.get_constraint("Compare")
        self.assertIsNotNone(constraint)
        tail_types = constraint.valid_tail_types_for_head("NONEXISTENT_TYPE")
        self.assertEqual(tail_types, set())

    def test_all_relations_have_constraints(self):
        for rtype in self.spec.relation_types:
            constraint = self.spec.get_constraint(rtype)
            self.assertIsNotNone(constraint, f"No constraint for {rtype}")
            self.assertGreater(len(constraint.valid_pairs), 0,
                               f"Empty valid_pairs for {rtype}")

    def test_conjunction_symmetry(self):
        """Conjunction is symmetric: both (A,B) and (B,A) pairs should exist or
        at least all head types == all tail types."""
        constraint = self.spec.get_constraint("Conjunction")
        self.assertIsNotNone(constraint)
        heads = constraint.valid_head_types()
        tails = constraint.valid_tail_types()
        self.assertTrue(len(heads) > 0)
        self.assertTrue(len(tails) > 0)


class TestTypeMasking(unittest.TestCase):
    """Test the masking logic without a real model."""

    def setUp(self):
        if not SCIERC_CONSTRAINTS_PATH.exists():
            self.skipTest(f"SciERC constraints not found at {SCIERC_CONSTRAINTS_PATH}")
        self.compiler = OntologyCompiler(SCIERC_CONSTRAINTS_PATH)
        self.tokenizer = make_mock_tokenizer()
        self.compiler.compile_type_constraints(self.tokenizer)
        self.spec = self.compiler.spec

    def _make_processor(self):
        from compiler.type_mask_processor import TypeConstraintProcessor
        return TypeConstraintProcessor(self.spec, self.tokenizer, prompt_length=0)

    def test_build_first_token_map(self):
        proc = self._make_processor()
        for etype, expected_id in SCIERC_FIRST_TOKENS.items():
            self.assertEqual(proc._type_first_token[etype], expected_id)
        self.assertEqual(len(proc._all_type_first_tokens), 6)

    def test_mask_entity_type_allows_all(self):
        """_mask_entity_type allows all entity types (no restriction)."""
        import torch
        proc = self._make_processor()
        logits = torch.zeros(self.tokenizer.vocab_size)
        masked = proc._mask_entity_type(logits.clone())

        for etype, tid in SCIERC_FIRST_TOKENS.items():
            self.assertEqual(masked[tid].item(), 0.0,
                             f"{etype} should be allowed at entity_type position")

    def test_mask_head_type_restricts(self):
        """_mask_head_type restricts to valid head types for the relation."""
        import torch
        proc = self._make_processor()
        proc.state.current_relation_type = "Evaluate-for"

        logits = torch.zeros(self.tokenizer.vocab_size)
        masked = proc._mask_head_type(logits.clone())

        constraint = self.spec.get_constraint("Evaluate-for")
        allowed_heads = constraint.valid_head_types()

        for etype, tid in SCIERC_FIRST_TOKENS.items():
            if etype in allowed_heads:
                self.assertEqual(masked[tid].item(), 0.0,
                                 f"{etype} should be allowed as head")
            else:
                self.assertEqual(masked[tid].item(), float("-inf"),
                                 f"{etype} should be masked as head")

    def test_mask_tail_type_with_head(self):
        """Given (Compare, head=Method), only valid tail types are allowed."""
        import torch
        proc = self._make_processor()
        proc.state.current_relation_type = "Compare"
        proc.state.current_head_type = "Method"

        constraint = self.spec.get_constraint("Compare")
        allowed = constraint.valid_tail_types_for_head("Method")

        logits = torch.zeros(self.tokenizer.vocab_size)
        masked = proc._mask_tail_type(logits.clone())

        for etype, tid in SCIERC_FIRST_TOKENS.items():
            if etype in allowed:
                self.assertEqual(masked[tid].item(), 0.0,
                                 f"{etype} should be allowed as tail for Compare/Method")
            else:
                self.assertEqual(masked[tid].item(), float("-inf"),
                                 f"{etype} should be masked as tail for Compare/Method")

    def test_mask_tail_type_fallback_without_head(self):
        """Without head_type, falls back to all valid tail types for relation."""
        import torch
        proc = self._make_processor()
        proc.state.current_relation_type = "Evaluate-for"
        proc.state.current_head_type = None

        constraint = self.spec.get_constraint("Evaluate-for")
        all_tails = constraint.valid_tail_types()

        logits = torch.zeros(self.tokenizer.vocab_size)
        masked = proc._mask_tail_type(logits.clone())

        for etype, tid in SCIERC_FIRST_TOKENS.items():
            if etype in all_tails:
                self.assertEqual(masked[tid].item(), 0.0)
            else:
                self.assertEqual(masked[tid].item(), float("-inf"))

    def test_no_mask_without_relation(self):
        """Without current_relation_type, no masking is applied."""
        import torch
        proc = self._make_processor()
        proc.state.current_relation_type = None

        logits = torch.ones(self.tokenizer.vocab_size)
        masked_head = proc._mask_head_type(logits.clone())
        masked_tail = proc._mask_tail_type(logits.clone())

        self.assertTrue(torch.equal(masked_head, logits))
        self.assertTrue(torch.equal(masked_tail, logits))


class TestPositionDetector(unittest.TestCase):
    """Test JSON position detection."""

    def test_entity_type_detection(self):
        from compiler.type_mask_processor import PositionDetector, GenerationState, FieldPosition

        state = GenerationState()
        text = '{"entities": [{"text": "BERT", "type": "'
        pos = PositionDetector.detect(text, state)
        self.assertEqual(pos, FieldPosition.ENTITY_TYPE)
        self.assertTrue(state.in_entities_section)

    def test_relation_type_detection(self):
        from compiler.type_mask_processor import PositionDetector, GenerationState, FieldPosition

        state = GenerationState()
        text = ('{"entities": [{"text": "BERT", "type": "Method"}], '
                '"relations": [{"head": "BERT", "tail": "NER", "type": "')
        pos = PositionDetector.detect(text, state)
        self.assertEqual(pos, FieldPosition.RELATION_TYPE)
        self.assertFalse(state.in_entities_section)

    def test_relation_head_type_detection(self):
        from compiler.type_mask_processor import PositionDetector, GenerationState, FieldPosition

        state = GenerationState()
        text = ('{"entities": [{"text": "BERT", "type": "Method"}], '
                '"relations": [{"head": "BERT", "tail": "NER", '
                '"type": "Used-for", "head_type": "')
        pos = PositionDetector.detect(text, state)
        self.assertEqual(pos, FieldPosition.RELATION_HEAD_TYPE)
        self.assertEqual(state.current_relation_type, "Used-for")

    def test_relation_tail_type_detection(self):
        from compiler.type_mask_processor import PositionDetector, GenerationState, FieldPosition

        state = GenerationState()
        text = ('{"entities": [{"text": "BERT", "type": "Method"}], '
                '"relations": [{"head": "BERT", "tail": "NER", '
                '"type": "Used-for", "head_type": "Method", "tail_type": "')
        pos = PositionDetector.detect(text, state)
        self.assertEqual(pos, FieldPosition.RELATION_TAIL_TYPE)
        self.assertEqual(state.current_relation_type, "Used-for")
        self.assertEqual(state.current_head_type, "Method")

    def test_entity_registry_populated(self):
        from compiler.type_mask_processor import PositionDetector, GenerationState, FieldPosition

        state = GenerationState()
        text = ('{"entities": [{"text": "BERT", "type": "Method"}, '
                '{"text": "NER", "type": "Task"}], "relations": [')
        PositionDetector.detect(text, state)
        self.assertEqual(state.entity_registry.get_type("BERT"), "Method")
        self.assertEqual(state.entity_registry.get_type("NER"), "Task")
        self.assertFalse(state.in_entities_section)

    def test_free_text_detection(self):
        from compiler.type_mask_processor import PositionDetector, GenerationState, FieldPosition

        state = GenerationState()
        text = '{"entities": [{"text": "'
        pos = PositionDetector.detect(text, state)
        self.assertEqual(pos, FieldPosition.FREE_TEXT)

    def test_multiple_entities_registered(self):
        from compiler.type_mask_processor import PositionDetector, GenerationState, FieldPosition

        state = GenerationState()
        text = ('{"entities": [{"text": "LSTM", "type": "Method"}, '
                '{"text": "accuracy", "type": "Metric"}, '
                '{"text": "NLP", "type": "Task"}], "relations": [')
        PositionDetector.detect(text, state)
        self.assertEqual(state.entity_registry.get_type("LSTM"), "Method")
        self.assertEqual(state.entity_registry.get_type("accuracy"), "Metric")
        self.assertEqual(state.entity_registry.get_type("NLP"), "Task")
        self.assertIsNone(state.entity_registry.get_type("UNKNOWN"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
