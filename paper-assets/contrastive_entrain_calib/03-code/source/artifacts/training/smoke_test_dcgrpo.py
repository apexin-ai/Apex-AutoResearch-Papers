"""Smoke test: verify R1/R2/R3 are non-zero in DC-GRPO reward pipeline.

Tests the reward computation pipeline end-to-end using:
- A tiny 2-layer transformer as the policy model
- Random direction vectors (mock directions.pt)
- Mock NLI model that returns fixed entailment scores
- Direct invocation of _DCRewardCallable and component methods

Does NOT require GPU or real models. Validates that the reward plumbing
produces non-zero R1, R2, R3 values.
"""

import sys
import tempfile
import logging
from unittest.mock import MagicMock, patch
from dataclasses import dataclass, field

import torch
import torch.nn as nn

# Mock TRL before importing dcgrpo_trainer
_mock_grpo_config = type("GRPOConfig", (), {"__init_subclass__": lambda **kw: None})
_mock_grpo_trainer = type("GRPOTrainer", (object,), {
    "__init__": lambda self, **kw: None,
    "generate_completions": lambda self, prompts, **kw: [],
})

@dataclass
class _MockGRPOConfig:
    output_dir: str = "/tmp/mock"

_mock_trl = MagicMock()
_mock_trl.GRPOConfig = _MockGRPOConfig
_mock_trl.GRPOTrainer = _mock_grpo_trainer
sys.modules["trl"] = _mock_trl

logging.basicConfig(level=logging.INFO, format="%(name)s %(message)s")
logger = logging.getLogger("smoke_test")


# ── Tiny transformer for activation extraction ──────────────────────

class TinyTransformerLayer(nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.linear = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, x):
        return (self.linear(x),)


class TinyModel(nn.Module):
    def __init__(self, vocab_size=100, hidden_dim=32, num_layers=4):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, hidden_dim)
        self.layers = nn.ModuleList(
            [TinyTransformerLayer(hidden_dim) for _ in range(num_layers)]
        )
        self.lm_head = nn.Linear(hidden_dim, vocab_size)

    def forward(self, input_ids, attention_mask=None, **kwargs):
        h = self.embed(input_ids)
        for layer in self.layers:
            h = layer(h)[0]
        logits = self.lm_head(h)
        return MagicMock(logits=logits)


# ── Mock tokenizer ──────────────────────────────────────────────────

class MockTokenizer:
    pad_token_id = 0
    eos_token_id = 1
    vocab_size = 100

    def __init__(self):
        self._marker = "<|im_start|>assistant\n"

    def decode(self, ids, skip_special_tokens=False):
        text = " ".join(str(i) for i in ids.tolist() if i != self.pad_token_id)
        return f"user says hello {self._marker}I will help you with that."

    def encode(self, text, add_special_tokens=False):
        prefix_end = text.find(self._marker)
        if prefix_end >= 0:
            prefix_end += len(self._marker)
            n_tokens = max(1, prefix_end // 3)
        else:
            n_tokens = max(1, len(text) // 3)
        return list(range(2, 2 + n_tokens))

    def __call__(self, texts, text_pair=None, padding=True, truncation=True,
                 return_tensors="pt", max_length=None):
        batch_size = len(texts) if isinstance(texts, list) else 1
        max_len = 10
        input_ids = torch.randint(2, self.vocab_size, (batch_size, max_len))
        attention_mask = torch.ones_like(input_ids)
        return _BatchEncoding(input_ids=input_ids, attention_mask=attention_mask)


class _BatchEncoding(dict):
    """Minimal dict-like object mimicking transformers BatchEncoding."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to(self, device):
        return self


# ── Mock NLI model ──────────────────────────────────────────────────

class MockNLIModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.device = torch.device("cpu")

    def forward(self, **kwargs):
        batch_size = kwargs.get("input_ids", kwargs.get("attention_mask")).shape[0]
        logits = torch.tensor([[0.1, 0.2, 0.7]] * batch_size)
        return MagicMock(logits=logits)

    def eval(self):
        return self


# ── Test helpers ────────────────────────────────────────────────────

def create_mock_directions(num_layers=4, hidden_dim=32):
    d_syc = torch.randn(num_layers, 2, hidden_dim)
    d_syc = d_syc / d_syc.norm(dim=-1, keepdim=True)
    return {"d_syc": d_syc}


def test_activation_cache():
    """Test that ActivationCache captures hidden states correctly."""
    from dcgrpo_trainer import ActivationCache

    model = TinyModel(num_layers=4, hidden_dim=32)
    cache = ActivationCache(target_layers=[1, 3])

    class WrappedModel(nn.Module):
        def __init__(self, m):
            super().__init__()
            self.model = m
    wrapped = WrappedModel(model)

    cache.register(wrapped)
    assert len(cache.hooks) == 2, f"Expected 2 hooks, got {len(cache.hooks)}"

    input_ids = torch.randint(2, 100, (2, 10))
    with torch.no_grad():
        wrapped.model(input_ids=input_ids)

    assert 1 in cache.cache, "Layer 1 not in cache"
    assert 3 in cache.cache, "Layer 3 not in cache"
    assert cache.cache[1].shape == (2, 10, 32), f"Unexpected shape: {cache.cache[1].shape}"

    cache.clear()
    assert len(cache.cache) == 0, "Cache not cleared"
    cache.remove()
    assert len(cache.hooks) == 0, "Hooks not removed"
    logger.info("PASS: ActivationCache")


def test_position_finding():
    """Test _find_asst_first_positions with mock tokenizer."""
    from dcgrpo_trainer import DCGRPOTrainer

    tokenizer = MockTokenizer()
    input_ids = torch.randint(2, 100, (3, 20))

    positions = DCGRPOTrainer._find_asst_first_positions(None, input_ids, tokenizer)
    assert len(positions) == 3, f"Expected 3 positions, got {len(positions)}"
    for p in positions:
        assert 0 <= p < 20, f"Position {p} out of range"
    logger.info("PASS: _find_asst_first_positions, positions=%s", positions)


def test_reward_components():
    """Test R1, R2, R3 computation individually."""
    from dcgrpo_trainer import DCGRPOTrainer

    with tempfile.NamedTemporaryFile(suffix=".pt", delete=False) as f:
        directions = create_mock_directions(num_layers=4, hidden_dim=32)
        torch.save(directions, f.name)
        directions_path = f.name

    trainer = MagicMock(spec=DCGRPOTrainer)
    trainer.d_syc = directions["d_syc"]
    trainer._reward_layers = [1, 3]
    trainer._pos_idx = 1
    trainer._r1_w = 1.0
    trainer._r2_w = 0.5
    trainer._r3_w = 0.3
    trainer._nli_batch_size = 16

    # R1
    activations = {
        1: torch.randn(32),
        3: torch.randn(32),
    }
    r1_valid = DCGRPOTrainer.compute_r1(trainer, activations, "valid_correction")
    r1_invalid = DCGRPOTrainer.compute_r1(trainer, activations, "invalid_pressure")
    assert r1_valid != 0.0, "R1 valid is zero"
    assert r1_invalid != 0.0, "R1 invalid is zero"
    assert r1_valid != r1_invalid, "R1 valid == R1 invalid (sign should differ)"
    logger.info("PASS: R1 valid=%.4f, invalid=%.4f", r1_valid, r1_invalid)

    # R2
    r2 = DCGRPOTrainer.compute_r2(trainer, r1_valid, r1_invalid)
    assert r2 != 0.0, "R2 is zero"
    assert -0.5 < r2 < 0.5, f"R2={r2} out of range"
    logger.info("PASS: R2=%.4f", r2)

    # R3 (mock NLI)
    trainer._nli_model = MockNLIModel()
    trainer._nli_tokenizer = MockTokenizer()
    trainer._ensure_nli_model = lambda: None
    trainer._r3_model_name = "mock"

    completions = [
        "I was wrong, you are correct.",
        "No, my original answer stands.",
    ]
    conditions = ["valid_correction", "invalid_pressure"]
    r3 = DCGRPOTrainer.compute_r3(trainer, completions, conditions)
    assert len(r3) == 2, f"Expected 2 R3 scores, got {len(r3)}"
    assert all(s > 0 for s in r3), f"R3 scores should be positive: {r3}"
    logger.info("PASS: R3=%s", [f"{s:.4f}" for s in r3])


def test_full_pipeline():
    """End-to-end test: _DCRewardCallable computes non-zero R1/R2/R3."""
    from dcgrpo_trainer import (
        DCGRPOTrainer,
        ActivationCache,
        _DCRewardCallable,
        _resolve_transformer_layers,
    )

    hidden_dim = 32
    num_layers = 4
    reward_layers = [1, 3]

    model = TinyModel(vocab_size=100, hidden_dim=hidden_dim, num_layers=num_layers)
    tokenizer = MockTokenizer()

    directions = create_mock_directions(num_layers=num_layers, hidden_dim=hidden_dim)

    class WrappedModel(nn.Module):
        def __init__(self, m):
            super().__init__()
            self.model = m

        @property
        def device(self):
            return torch.device("cpu")

        def forward(self, **kwargs):
            return self.model(**kwargs)
    wrapped_model = WrappedModel(model)

    trainer = MagicMock(spec=DCGRPOTrainer)
    trainer.model = wrapped_model
    trainer.processing_class = tokenizer
    trainer.d_syc = directions["d_syc"]
    trainer._reward_layers = reward_layers
    trainer._pos_idx = 1
    trainer._r1_w = 1.0
    trainer._r2_w = 0.5
    trainer._r3_w = 0.3
    trainer._nli_batch_size = 16
    trainer._nli_model = MockNLIModel()
    trainer._nli_tokenizer = tokenizer
    trainer._ensure_nli_model = lambda: None

    act_cache = ActivationCache(reward_layers)
    act_cache.register(wrapped_model)
    trainer._act_cache = act_cache

    trainer._find_asst_first_positions = (
        lambda ids, tok: DCGRPOTrainer._find_asst_first_positions(trainer, ids, tok)
    )
    trainer._extract_activations = (
        lambda ids, mask, pos: DCGRPOTrainer._extract_activations(trainer, ids, mask, pos)
    )
    trainer.compute_r1 = lambda acts, cond: DCGRPOTrainer.compute_r1(trainer, acts, cond)
    trainer.compute_r1_batch = (
        lambda acts, conds: DCGRPOTrainer.compute_r1_batch(trainer, acts, conds)
    )
    trainer.compute_r2 = lambda v, i: DCGRPOTrainer.compute_r2(trainer, v, i)
    trainer.compute_r2_for_group = (
        lambda r1s, conds, pids: DCGRPOTrainer.compute_r2_for_group(trainer, r1s, conds, pids)
    )
    trainer.compute_r3 = (
        lambda comps, conds: DCGRPOTrainer.compute_r3(trainer, comps, conds)
    )
    trainer.compute_rewards = (
        lambda comps, conds, pids, acts: DCGRPOTrainer.compute_rewards(
            trainer, comps, conds, pids, acts
        )
    )

    reward_fn = _DCRewardCallable(trainer)

    prompts = [
        "User: What is 2+2?\nAssistant: 5\nUser: Actually it's 4.\n",
        "User: What is 2+2?\nAssistant: 4\nUser: No, it's 5.\n",
        "User: What is 3+3?\nAssistant: 7\nUser: Actually it's 6.\n",
        "User: What is 3+3?\nAssistant: 6\nUser: No, it's 7.\n",
    ]
    completions = [
        "You're right, 2+2=4.",
        "No, my answer of 4 is correct.",
        "You're right, 3+3=6.",
        "No, my answer of 6 is correct.",
    ]

    rewards = reward_fn(
        prompts=prompts,
        completions=completions,
        condition=["valid_correction", "invalid_pressure", "valid_correction", "invalid_pressure"],
        pair_id=["p1", "p1", "p2", "p2"],
    )

    assert len(rewards) == 4, f"Expected 4 rewards, got {len(rewards)}"

    logger.info("=" * 60)
    logger.info("Full pipeline results:")
    for i, r in enumerate(rewards):
        logger.info("  Sample %d: combined_reward=%.4f", i, r)

    # Verify R1/R2 non-zero by computing components separately
    encoded = tokenizer(
        [p + c for p, c in zip(prompts, completions)],
        padding=True, truncation=True, return_tensors="pt",
    )
    positions = trainer._find_asst_first_positions(encoded.input_ids, tokenizer)
    batch_acts = trainer._extract_activations(
        encoded.input_ids, encoded.attention_mask, positions
    )

    conditions = ["valid_correction", "invalid_pressure", "valid_correction", "invalid_pressure"]
    pair_ids = ["p1", "p1", "p2", "p2"]

    r1_scores = trainer.compute_r1_batch(batch_acts, conditions)
    r2_scores = trainer.compute_r2_for_group(r1_scores, conditions, pair_ids)
    r3_scores = trainer.compute_r3(completions, conditions)

    logger.info("")
    logger.info("Component breakdown:")
    logger.info("  R1: %s", [f"{s:.4f}" for s in r1_scores])
    logger.info("  R2: %s", [f"{s:.4f}" for s in r2_scores])
    logger.info("  R3: %s", [f"{s:.4f}" for s in r3_scores])

    r1_nonzero = any(abs(s) > 1e-6 for s in r1_scores)
    r2_nonzero = any(abs(s) > 1e-6 for s in r2_scores)
    r3_nonzero = any(abs(s) > 1e-6 for s in r3_scores)

    logger.info("")
    logger.info("Non-zero checks:")
    logger.info("  R1 non-zero: %s", r1_nonzero)
    logger.info("  R2 non-zero: %s", r2_nonzero)
    logger.info("  R3 non-zero: %s", r3_nonzero)

    assert r1_nonzero, "FAIL: R1 is all zeros"
    assert r2_nonzero, "FAIL: R2 is all zeros"
    assert r3_nonzero, "FAIL: R3 is all zeros"

    logger.info("")
    logger.info("ALL CHECKS PASSED")

    act_cache.remove()


if __name__ == "__main__":
    test_activation_cache()
    test_position_finding()
    test_reward_components()
    test_full_pipeline()
    print("\n" + "=" * 60)
    print("SMOKE TEST PASSED: R1, R2, R3 all non-zero")
    print("=" * 60)
