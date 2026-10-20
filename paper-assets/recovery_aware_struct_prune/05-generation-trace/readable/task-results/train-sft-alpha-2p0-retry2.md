# train sft alpha 2p0 retry2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_sft-alpha-2p0-retry2_20260515T143806_result.json`
- **Structured JSON:** [`d5e59338035af23b7905.json`](../../sessions/d5/d5e59338035af23b7905.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed: **PID 43065 on cuda:1 using 50452MiB**, training actively at 98% GPU utilization.

## Summary

**1. α=0.0 post-SFT GSM8K accuracy: 64.0% (64/100)**
- eos_rate: 97% (3 truncated)
- avg_response_length: 257.9 tokens
- stderr: ±4.8%

**2. α=0.5, α=1.0 post-SFT eval results: NOT YET AVAILABLE**
- Only pre-SFT prune evals exist (`results/alpha_ablation/eval_prune_alpha_*.json`)
- An α=1.0 eval (PID 42535) is currently running on cuda:1 (started by another worker)

**3. α=2.0 SFT successfully launched:**
- PID: 43065 (parent nohup: 43060)
- GPU: cuda:1, 50452MiB allocated
- Progress: 2/1870 steps (~2s/step ≈ ~62 min ETA)
- Log: `/tmp/sft_alpha2_0.log`
- Output: `/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0`

**4. Issue found and fixed:** The `sft_recovery.py` script overrides `CUDA_VISIBLE_DEVICES` with `--gpu` value (line 21). The original command (`CUDA_VISIBLE_DEVICES=1 --gpu 0`) incorrectly placed the process on GPU 0. Fixed by using `--gpu 1` directly (no external `CUDA_VISIBLE_DEVICES`).

---
