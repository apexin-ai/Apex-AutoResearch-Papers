# code d154 8b fix and pilot

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d154-8b-fix-and-pilot_20260520T060050_result.json`
- **Structured JSON:** [`2c139903ad6fd6dc0b71.json`](../../sessions/2c/2c139903ad6fd6dc0b71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Step 2 completed successfully.** Training is progressing:

| Step | Reward | Prove Rate | ISR | Loss | Time |
|------|--------|-----------|-----|------|------|
| 1 | 0.156 | 15.6% | 0.101 | 0.1709 | 06:16:18 |
| 2 | 0.156 | 15.6% | 0.123 | -0.0649 | 06:17:14 |

~56 seconds between steps. Memory stable at 53.9 GiB. OOM is definitively resolved.

## Summary

1. **Config changes**:
   - `grpo_exec_only_8b.yaml`: `max_completion_length` 512→384, `gradient_accumulation_steps` 16→32
   - Created `grpo_isr_b01_8b.yaml`: same params, `reward_mode=additive_bonus`, `beta=0.1`

2. **Root cause**: TRL's `create_model_from_path()` defaults `dtype="float32"`, loading the 8B model in fp32 (~32 GiB params) instead of bf16 (~16 GiB). Combined with optimizer states and gradients, this pushed peak memory to 93.95 GiB, exceeding the 94.97 GiB GPU capacity by ~1.16 GiB at the lm_head forward pass.

3. **Fix**: Added `model_init_kwargs={"dtype": "bfloat16"}` to `GRPOConfig` in `scripts/train_grpo.py` (line 606). This halved model parameter memory and reduced peak GPU usage from 93.9 GiB → 53.9 GiB.

4. **Model path**: `/root/autodl-tmp/models/Qwen3-8B/` — confirmed complete (5 safetensors shards, ~16.4 GiB total)

5. **Training status**: Running successfully. Step 2 completed, ~56s/step. ETA for 500 steps: ~7.8 hours. Exp ID: `d154-8b-exec-s42-r3`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "dtype": "bfloat16"
  }
}
```

</details>

---
