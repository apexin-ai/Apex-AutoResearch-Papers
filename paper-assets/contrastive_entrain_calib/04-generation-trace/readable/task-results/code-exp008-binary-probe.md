# code exp008 binary probe

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008-binary-probe_20260518T164612_result.json`
- **Structured JSON:** [`962dbd75b90c60187304.json`](../../sessions/96/962dbd75b90c60187304.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Syntax verified. Summary of what was written:

**`run_exp008_binary_probe_penalty.py`** — self-contained SFT-style training script for the binary probe penalty baseline.

**Architecture:**
- Qwen3-8B + LoRA (rank=16, alpha=32, target: q/k/v/o_proj)
- Gradient checkpointing (`use_reentrant=False`) for memory efficiency
- `output_hidden_states=True` to extract differentiable hidden states for the probe penalty

**Pipeline (3 phases before training):**
1. Load dataset from `calibration_data.jsonl` (640 samples, 4-turn conversations with target responses, condition mapping handled automatically)
2. Train/load frozen `LinearProbe` from `activations.pt` (exp-001 pre-extracted hidden states)
3. Precompute R3 scores using DeBERTa NLI model (freed after precomputation to save GPU memory)

**Training loop:**
- `L = L_sft + lambda_reward * lambda_probe * S(t) - lambda_reward * R3`
- S(t) is differentiable through hidden states at asst_first position (averaged across layers [19,20,24,27,32,33,35])
- R3 is precomputed (constant per sample, doesn't affect gradients, used for monitoring)
- AdamW + cosine schedule with warmup, grad accumulation=16, logging every 10 steps, checkpoints every 500 steps
- Key hyperparams exposed via argparse: `--lr`, `--lambda_reward`, `--lambda_probe`, `--max_steps`, etc.

---
