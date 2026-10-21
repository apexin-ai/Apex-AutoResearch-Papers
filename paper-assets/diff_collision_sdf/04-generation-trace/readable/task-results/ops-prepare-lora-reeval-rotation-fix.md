# ops prepare lora reeval rotation fix

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_lora_reeval_rotation_fix_20260526T070923_result.json`
- **Structured JSON:** [`63a27cce7c0906862160.json`](../../sessions/63/63a27cce7c0906862160.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LoRA re-eval is running — model loaded successfully, now evaluating Task 0. Everything looks good:

- **tmux session**: `lora_reeval`
- **Checkpoint**: `.../pi05_lora_baseline_object_pudding_seed0/30000/model.safetensors`
- **LoRA injected**: PaliGemma rank=16 (19.6M params), Expert rank=32 (13.9M params)
- **Norm stats**: loaded from checkpoint assets
- **Log**: `/tmp/lora_reeval.log`
- **Output**: `/root/autodl-tmp/eval_results/lora_baseline_s0_reeval_safelibero_object_levelII_seed7.json`

Pi0.5 baseline re-eval result for reference: **TSR=71.5%, CAR=28.5%**. LoRA s0 re-eval will show whether the TSR collapse was real or an eval bug artifact.

---
