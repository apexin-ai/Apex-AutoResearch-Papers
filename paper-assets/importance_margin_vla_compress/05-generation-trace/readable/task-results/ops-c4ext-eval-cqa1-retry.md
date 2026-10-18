# ops c4ext eval cqa1 retry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4ext-eval-cqa1-retry_20260520T102758_result.json`
- **Structured JSON:** [`261c52996a9da1d638f2.json`](../../sessions/26/261c52996a9da1d638f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full eval is running. Here's the status report:

---

**C4-ext 20K Eval Report — OpenVLA Smart Compress M=128 VTC-only (step 20000)**

**Checkpoint**: `checkpoints/openvla_sc_m128/checkpoint_step20000.pt` (19GB, eval_loss=2.7768)
- Loaded with strict match, VTC compressor 403M params

**Dry-run result**: PASS (no crash/segfault)
- Task 0, 2 episodes: 0/2 SR, 280 steps each (~48s/episode)
- Pipeline fully functional

**Full eval launched**: PID 858901 on cqa1-33015 GPU 0
- Suite: libero_object (10 tasks × 50 episodes = 500 total)
- Seed: 42
- Output: `eval_results/eval_openvla_sc_m128_vtconly_20k_seed42_full.json`
- Log: `/tmp/eval_full_openvla_sc_m128.log`

**ETA**: ~6.7 hours worst case (500 episodes × ~48s), likely less if some episodes succeed early. Expected ~01:30 CST (May 21).

**Fixes applied to eval script** (5 total):
1. `map_location=device` → `"cpu"` — OOM fix (checkpoint was loaded to GPU alongside model)
2. `obs["pixels"][key]` fallback — lerobot LiberoEnv observation format
3. `isinstance(result, (tuple, list))` — timm 1.x returns list instead of tuple
4. `generate()` output slicing — transformers 4.53 returns only new tokens with `inputs_embeds`
5. Cached `image_token_id` — was creating 403M-param wrapper per step

---
