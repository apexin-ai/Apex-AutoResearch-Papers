# eval monitor baseline pertask v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_monitor_baseline_pertask_v2_20260528T003705_result.json`
- **Structured JSON:** [`3ed4c01edf4076d14f4b.json`](../../sessions/3e/3ed4c01edf4076d14f4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

While waiting for westd-35807, here's what I've collected from westd-45947:

**All reeval JSONs on westd-45947** (all are single-task: orange_juice, 50 episodes, level II, seed 7):

| File | Model | TSR | CAR |
|------|-------|-----|-----|
| `lora_baseline_s0_reeval_...` | LoRA baseline seed0 | 32% | **56%** |
| `pi05_base_reeval_...` | pi0 baseline | 74% | 16% |
| `reeval_lora_s1_30k` | LoRA baseline seed1 | 34% | 54% |
| `reeval_sdf_s0_l005_30k` | SDF seed0 λ=0.05 | 38% | 52% |
| `reeval_sdf_s0_l01_30k` | SDF seed0 λ=0.1 | 28% | 48% |
| `reeval_sdf_s1_l005_30k` | SDF seed1 λ=0.05 | 28% | 64% |
| `reeval_sdf_s1_l01_30k` | SDF seed1 λ=0.1 | 22% | 60% |
| `reeval_sdf_s2_l005_30k` | SDF seed2 λ=0.05 | 34% | 46% |
| `reeval_sdf_s2_l01_30k` | SDF seed2 λ=0.1 | 24% | 64% |

**LoRA s0 overall CAR = 56.0%** (not 56.5% or 57.0%). If the main table shows s0=57.0%, **MAIN_TABLE_NEEDS_UPDATE: yes**.

Polling westd-35807 PID 932512 in ~2 minutes...

---
