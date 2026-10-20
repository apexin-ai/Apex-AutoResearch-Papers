"""Test F1 gate in CED reward: no gold-matching triple → CED = 0."""
import json
from unittest.mock import MagicMock

import pytest

from freige.training.grpo_trainer import CEDRewardWrapper


GOLD = [{"head": "John", "relation": "born in", "tail": "London",
         "evidence": [0, 1], "hard_negative_sent_ids": [2]}]
SENTS = ["John was born in London.", "He grew up there.", "Mary lives in Paris."]


@pytest.fixture
def ced_wrapper():
    w = CEDRewardWrapper.__new__(CEDRewardWrapper)
    w.__name__ = "ced_reward"
    w.mode = "ced"
    w._call_count = 0
    w.tau_start = 0.3
    w.tau_end = 0.5
    w.total_steps = 100
    w.recall_penalty = False
    mock_rm = MagicMock()
    mock_rm.compute_ced_reward.return_value = {
        "reward": 0.8, "p_pos": 0.9, "p_neg": 0.1, "margin": 0.8,
    }
    w.reward_model = mock_rm
    w.verbalize = lambda h, r, t: f"{h} {r} {t}"
    return w


def test_empty_output_returns_zero(ced_wrapper):
    """Case 1: empty output / no triple -> CED = 0."""
    rewards = ced_wrapper(
        completions=[""],
        all_sents=[json.dumps(SENTS)],
        gold_triples=[json.dumps(GOLD)],
    )
    assert rewards == [0.0]


def test_correct_triple_returns_positive(ced_wrapper):
    """Case 2: correct triple -> CED > 0."""
    pred = [{"head": "John", "relation": "born in", "tail": "London", "evidence": [0]}]
    rewards = ced_wrapper(
        completions=[json.dumps(pred)],
        all_sents=[json.dumps(SENTS)],
        gold_triples=[json.dumps(GOLD)],
    )
    assert rewards[0] > 0.0


def test_nonsense_output_returns_zero(ced_wrapper):
    """Case 3: text without triples (nonsense) -> CED = 0."""
    rewards = ced_wrapper(
        completions=["This is just random text without any JSON triples at all."],
        all_sents=[json.dumps(SENTS)],
        gold_triples=[json.dumps(GOLD)],
    )
    assert rewards == [0.0]
