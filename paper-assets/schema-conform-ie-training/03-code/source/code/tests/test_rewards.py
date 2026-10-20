# Boundary tests for 5-component reward functions.
# Usage: cd code && python -m pytest tests/test_rewards.py -v

import json
import pytest

from src.rewards import (
    compute_all_rewards,
    f1_correctness_reward,
    structural_validity_reward,
    type_conformance_reward,
    relational_constraint_reward,
    structural_completeness_reward,
    REWARD_NAMES,
)

ACE_SCHEMA = {
    "entity_types": ["PER", "ORG", "GPE", "LOC", "FAC", "VEH", "WEA"],
    "relation_types": [
        {"name": "PHYS", "arg1_types": ["PER", "GPE", "ORG", "LOC", "FAC"], "arg2_types": ["GPE", "LOC", "FAC"]},
        {"name": "PART-WHOLE", "arg1_types": ["GPE", "ORG", "LOC", "FAC", "VEH", "WEA"], "arg2_types": ["GPE", "ORG", "LOC", "FAC", "VEH", "WEA"]},
        {"name": "PER-SOC", "arg1_types": ["PER"], "arg2_types": ["PER"]},
        {"name": "ORG-AFF", "arg1_types": ["PER", "ORG", "GPE"], "arg2_types": ["ORG", "GPE"]},
        {"name": "ART", "arg1_types": ["PER", "ORG", "GPE"], "arg2_types": ["FAC", "VEH", "WEA"]},
        {"name": "GEN-AFF", "arg1_types": ["PER", "ORG", "GPE"], "arg2_types": ["PER", "ORG", "GPE", "LOC"]},
    ],
}

GOLD_ANNOTATIONS = {
    "entities": [
        {"type": "PER", "text": "John Smith"},
        {"type": "ORG", "text": "Acme Corp"},
        {"type": "GPE", "text": "New York"},
    ],
    "relations": [
        {
            "type": "ORG-AFF",
            "arg1": {"type": "PER", "text": "John Smith"},
            "arg2": {"type": "ORG", "text": "Acme Corp"},
        }
    ],
}


class TestPerfectMatch:
    """Case 1: Perfect match output -> all rewards ~ 1.0."""

    def test_all_rewards_near_one(self):
        output = json.dumps({
            "entities": [
                {"type": "PER", "text": "John Smith"},
                {"type": "ORG", "text": "Acme Corp"},
                {"type": "GPE", "text": "New York"},
            ],
            "relations": [
                {
                    "type": "ORG-AFF",
                    "arg1": {"type": "PER", "text": "John Smith"},
                    "arg2": {"type": "ORG", "text": "Acme Corp"},
                }
            ],
        })
        rewards = compute_all_rewards(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        for name in REWARD_NAMES:
            assert rewards[name] >= 0.95, f"{name}={rewards[name]:.4f}, expected >= 0.95"


class TestEmptyJSON:
    """Case 2: Empty JSON {} -> valid JSON but nothing extracted. All non-validity rewards = 0."""

    def test_structural_validity_is_one(self):
        output = "{}"
        assert structural_validity_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS) == 1.0

    def test_f1_is_zero(self):
        output = "{}"
        assert f1_correctness_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS) == 0.0

    def test_type_conformance_zero_on_empty(self):
        output = "{}"
        assert type_conformance_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS) == 0.0

    def test_relational_constraint_zero_on_empty(self):
        output = "{}"
        assert relational_constraint_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS) == 0.0

    def test_completeness_zero_on_empty(self):
        output = "{}"
        assert structural_completeness_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS) == 0.0

    def test_empty_lists_also_zero(self):
        output = json.dumps({"entities": [], "relations": []})
        rewards = compute_all_rewards(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        assert rewards["structural_validity"] == 1.0
        assert rewards["type_conformance"] == 0.0
        assert rewards["relational_constraint"] == 0.0
        assert rewards["structural_completeness"] == 0.0
        assert rewards["f1_correctness"] == 0.0


class TestInvalidJSON:
    """Case 3: Unparseable output -> all rewards 0.0."""

    @pytest.mark.parametrize("bad_output", [
        "this is not json",
        "{entities: [broken}",
        "",
        "```json\n{}\n```",
    ])
    def test_all_rewards_zero(self, bad_output):
        rewards = compute_all_rewards(bad_output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        for name in REWARD_NAMES:
            assert rewards[name] == 0.0, f"{name}={rewards[name]:.4f} for input={bad_output!r}"


class TestCorrectTypeWrongSpan:
    """Case 4: Correct entity types but wrong text -> type_conformance=1.0, F1<1.0."""

    def test_type_conformance_perfect(self):
        output = json.dumps({
            "entities": [
                {"type": "PER", "text": "Alice Johnson"},
                {"type": "ORG", "text": "Beta Inc"},
                {"type": "GPE", "text": "Los Angeles"},
            ],
            "relations": [],
        })
        assert type_conformance_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS) == 1.0

    def test_f1_below_one(self):
        output = json.dumps({
            "entities": [
                {"type": "PER", "text": "Alice Johnson"},
                {"type": "ORG", "text": "Beta Inc"},
                {"type": "GPE", "text": "Los Angeles"},
            ],
            "relations": [],
        })
        assert f1_correctness_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS) < 1.0


class TestTypeNotInSchema:
    """Case 5: Entity type not in schema -> type_conformance < 1.0."""

    def test_unknown_type_lowers_conformance(self):
        output = json.dumps({
            "entities": [
                {"type": "PER", "text": "John Smith"},
                {"type": "DISEASE", "text": "flu"},
            ],
            "relations": [],
        })
        tc = type_conformance_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        assert tc < 1.0
        assert tc == 0.5  # 1 valid out of 2

    def test_all_unknown_types(self):
        output = json.dumps({
            "entities": [
                {"type": "DISEASE", "text": "flu"},
                {"type": "CHEMICAL", "text": "aspirin"},
            ],
            "relations": [],
        })
        tc = type_conformance_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        assert tc == 0.0


class TestRelationalConstraintViolation:
    """Case 6: Relation with arg types violating schema constraints -> relational_constraint < 1.0."""

    def test_invalid_arg_types(self):
        output = json.dumps({
            "entities": [
                {"type": "PER", "text": "John Smith"},
                {"type": "VEH", "text": "Toyota"},
            ],
            "relations": [
                {
                    "type": "PER-SOC",
                    "arg1": {"type": "PER", "text": "John Smith"},
                    "arg2": {"type": "VEH", "text": "Toyota"},
                }
            ],
        })
        rc = relational_constraint_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        assert rc < 1.0

    def test_valid_relation_passes(self):
        output = json.dumps({
            "entities": [
                {"type": "PER", "text": "John"},
                {"type": "PER", "text": "Jane"},
            ],
            "relations": [
                {
                    "type": "PER-SOC",
                    "arg1": {"type": "PER", "text": "John"},
                    "arg2": {"type": "PER", "text": "Jane"},
                }
            ],
        })
        rc = relational_constraint_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        assert rc == 1.0


class TestMissingRequiredFields:
    """Case 7: Missing required fields -> structural_completeness < 1.0."""

    def test_entity_missing_text(self):
        output = json.dumps({
            "entities": [{"type": "PER"}],
            "relations": [],
        })
        sc = structural_completeness_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        assert sc < 1.0

    def test_entity_missing_type(self):
        output = json.dumps({
            "entities": [{"text": "John"}],
            "relations": [],
        })
        sc = structural_completeness_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        assert sc < 1.0

    def test_relation_missing_arg(self):
        output = json.dumps({
            "entities": [
                {"type": "PER", "text": "John"},
            ],
            "relations": [
                {"type": "PER-SOC", "arg1": {"type": "PER", "text": "John"}},
            ],
        })
        sc = structural_completeness_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        assert sc < 1.0

    def test_complete_output_is_one(self):
        output = json.dumps({
            "entities": [
                {"type": "PER", "text": "John Smith"},
            ],
            "relations": [
                {
                    "type": "PER-SOC",
                    "arg1": {"type": "PER", "text": "John"},
                    "arg2": {"type": "PER", "text": "Jane"},
                }
            ],
        })
        sc = structural_completeness_reward(output, ACE_SCHEMA, GOLD_ANNOTATIONS)
        assert sc == 1.0


class TestRewardBounds:
    """All rewards must be in [0, 1]."""

    @pytest.mark.parametrize("output_str", [
        "not json",
        "{}",
        json.dumps({"entities": [], "relations": []}),
        json.dumps({"entities": [{"type": "PER", "text": "x"}], "relations": []}),
        json.dumps({"entities": [{"type": "UNKNOWN", "text": "x"}], "relations": []}),
    ])
    def test_rewards_in_unit_interval(self, output_str):
        rewards = compute_all_rewards(output_str, ACE_SCHEMA, GOLD_ANNOTATIONS)
        for name, val in rewards.items():
            assert 0.0 <= val <= 1.0, f"{name}={val} out of [0,1] for {output_str[:50]}"
