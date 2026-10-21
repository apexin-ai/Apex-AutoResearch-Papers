#!/usr/bin/env python3
"""GPU smoke test: verify DCGRPOTrainer components with real Qwen3-8B model.

Tests without TRL dependency:
  1. ActivationCache hook registration and capture
  2. Position computation (tokenize-based) vs extract_activations_v2.py
  3. R1 reward computation and distribution across layers 19-35
"""
import json
import sys
import types
import logging
from dataclasses import dataclass, field

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Mock trl module so dcgrpo_trainer can be imported without TRL installed
_trl = types.ModuleType("trl")

@dataclass
class _GRPOConfig:
    output_dir: str = "/tmp/grpo_dummy"

class _GRPOTrainer:
    pass

_trl.GRPOConfig = _GRPOConfig
_trl.GRPOTrainer = _GRPOTrainer
sys.modules["trl"] = _trl

sys.path.insert(0, "/root/mvp_v2_1_expanded/training")
sys.path.insert(0, "/root/mvp_v2")

from dcgrpo_trainer import ActivationCache, _resolve_transformer_layers
from extract_activations_v2 import find_critical_positions

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
DIRECTION_PATH = "/root/mvp_v2/results_v2/directions.pt"
DATA_PATH = "/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl"
REWARD_LAYERS = list(range(19, 36))


def load_data(n=8):
    data = []
    with open(DATA_PATH) as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            data.append(json.loads(line))
    return data


def _apply_template(tokenizer, messages, **kwargs):
    try:
        return tokenizer.apply_chat_template(
            messages, enable_thinking=False, tokenize=True, return_dict=False, **kwargs
        )
    except TypeError:
        return tokenizer.apply_chat_template(messages, tokenize=True, return_dict=False, **kwargs)


def test_activation_cache(model, tokenizer, samples):
    print("\n" + "=" * 60)
    print("TEST 1: ActivationCache hook registration")
    print("=" * 60)

    cache = ActivationCache(REWARD_LAYERS)
    cache.register(model)
    print(f"  Hooks registered: {len(cache.hooks)}")
    print(f"  Target layers: {sorted(cache.target_layers)}")
    assert len(cache.hooks) == len(REWARD_LAYERS), (
        f"Expected {len(REWARD_LAYERS)} hooks, got {len(cache.hooks)}"
    )

    sample = samples[0]
    msgs = [{"role": t["role"], "content": t["content"]} for t in sample["turns"]]
    ids = _apply_template(tokenizer, msgs, add_generation_prompt=True)
    input_ids = torch.tensor([ids], device=model.device)
    attention_mask = torch.ones_like(input_ids)

    cache.clear()
    with torch.no_grad():
        model(input_ids=input_ids, attention_mask=attention_mask)

    print(f"  Cached layers: {sorted(cache.cache.keys())}")
    assert len(cache.cache) == len(REWARD_LAYERS), (
        f"Expected {len(REWARD_LAYERS)} cached layers, got {len(cache.cache)}"
    )

    for layer_idx in REWARD_LAYERS:
        h = cache.cache[layer_idx]
        assert h.shape == (1, input_ids.shape[1], 4096), (
            f"Layer {layer_idx}: expected shape (1, {input_ids.shape[1]}, 4096), got {h.shape}"
        )

    print("  PASSED: all hooks fire, shapes correct")
    cache.remove()
    return True


def test_position_computation(tokenizer, samples):
    print("\n" + "=" * 60)
    print("TEST 2: Position computation (trainer vs extract_activations_v2)")
    print("=" * 60)

    all_match = True
    for i, sample in enumerate(samples):
        msgs = [{"role": t["role"], "content": t["content"]} for t in sample["turns"]]
        ids_with_gen = _apply_template(tokenizer, msgs, add_generation_prompt=True)
        prompt_length = len(ids_with_gen)
        trainer_pos = prompt_length - 1

        _, v2_asst_pos, v2_ids = find_critical_positions(tokenizer, sample["turns"])

        match = trainer_pos == v2_asst_pos
        all_match = all_match and match
        status = "OK" if match else "MISMATCH"
        print(
            f"  Sample {i} ({sample['condition'][:5]}): "
            f"trainer={trainer_pos}, v2={v2_asst_pos}, "
            f"prompt_len={prompt_length}, v2_len={len(v2_ids)} [{status}]"
        )

    if all_match:
        print("  PASSED: all positions match")
    else:
        print("  FAILED: position mismatch detected")
    return all_match


def test_r1_computation(model, tokenizer, samples, directions):
    print("\n" + "=" * 60)
    print("TEST 3: R1 reward computation (layers 19-35, average)")
    print("=" * 60)

    d_syc = directions["d_syc"]
    pos_idx = 1  # asst_first

    cache = ActivationCache(REWARD_LAYERS)
    cache.register(model)

    r1_scores = []
    for i, sample in enumerate(samples):
        msgs = [{"role": t["role"], "content": t["content"]} for t in sample["turns"]]
        ids = _apply_template(tokenizer, msgs, add_generation_prompt=True)
        input_ids = torch.tensor([ids], device=model.device)
        attention_mask = torch.ones_like(input_ids)
        asst_pos = len(ids) - 1

        cache.clear()
        with torch.no_grad():
            model(input_ids=input_ids, attention_mask=attention_mask)

        sign = 1.0 if sample["condition"] == "valid_correction" else -1.0
        layer_scores = []
        for layer_idx in REWARD_LAYERS:
            h = cache.cache[layer_idx][0, asst_pos]
            d = d_syc[layer_idx, pos_idx].to(device=h.device, dtype=h.dtype)
            dot = sign * torch.dot(h, d).item()
            layer_scores.append(dot)

        r1 = sum(layer_scores) / len(layer_scores)
        r1_scores.append(r1)
        print(
            f"  Sample {i} [{sample['condition'][:5]}] pair={sample['pair_id']}: "
            f"R1={r1:.4f} (min_layer={min(layer_scores):.4f}, max_layer={max(layer_scores):.4f})"
        )

    cache.remove()

    valid_r1 = [s for s, d in zip(r1_scores, samples) if d["condition"] == "valid_correction"]
    invalid_r1 = [s for s, d in zip(r1_scores, samples) if d["condition"] == "invalid_pressure"]
    pos_valid = sum(1 for x in valid_r1 if x > 0) / len(valid_r1) if valid_r1 else 0
    pos_invalid = sum(1 for x in invalid_r1 if x > 0) / len(invalid_r1) if invalid_r1 else 0

    print(f"\n  Valid correction R1 > 0: {pos_valid:.0%} ({len(valid_r1)} samples)")
    print(f"  Invalid pressure R1 > 0: {pos_invalid:.0%} ({len(invalid_r1)} samples)")
    print(f"  Mean valid R1: {sum(valid_r1)/len(valid_r1):.4f}" if valid_r1 else "")
    print(f"  Mean invalid R1: {sum(invalid_r1)/len(invalid_r1):.4f}" if invalid_r1 else "")

    # R2 for pairs
    print("\n  R2 (contrastive consistency):")
    pair_r1 = {}
    for score, sample in zip(r1_scores, samples):
        pid = sample["pair_id"]
        cond = sample["condition"]
        pair_r1.setdefault(pid, {})[cond] = score

    for pid, conds in pair_r1.items():
        if "valid_correction" in conds and "invalid_pressure" in conds:
            r1_v = conds["valid_correction"]
            r1_i = conds["invalid_pressure"]
            r2 = torch.sigmoid(torch.tensor(r1_v - r1_i)).item() - 0.5
            print(f"    Pair {pid}: R1_v={r1_v:.4f}, R1_i={r1_i:.4f}, R2={r2:.4f}")

    print("  PASSED: R1/R2 computation complete")
    return True


def main():
    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    print(f"Model loaded: {type(model).__name__}, layers={len(model.model.layers)}")

    print("Loading directions...")
    directions = torch.load(DIRECTION_PATH, map_location="cpu", weights_only=True)
    print(f"d_syc shape: {directions['d_syc'].shape}")

    print("Loading data (8 records = 4 pairs)...")
    samples = load_data(8)
    print(f"Loaded {len(samples)} records")

    results = {}
    results["hooks"] = test_activation_cache(model, tokenizer, samples)
    results["positions"] = test_position_computation(tokenizer, samples)
    results["r1"] = test_r1_computation(model, tokenizer, samples, directions)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for name, passed in results.items():
        print(f"  {name}: {'PASSED' if passed else 'FAILED'}")

    if all(results.values()):
        print("\nAll tests passed.")
        sys.exit(0)
    else:
        print("\nSome tests failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
