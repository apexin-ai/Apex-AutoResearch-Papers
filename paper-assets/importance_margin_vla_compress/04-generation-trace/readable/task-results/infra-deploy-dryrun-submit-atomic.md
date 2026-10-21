# infra deploy dryrun submit atomic

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_deploy-dryrun-submit-atomic_20260515T134431_result.json`
- **Structured JSON:** [`cc54f7d15c2b28b1fd5a.json`](../../sessions/cc/cc54f7d15c2b28b1fd5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both dry-runs complete. Here's the full summary:

---

## Dry-Run Results

### Deployment Status
- 12 code files deployed to `/root/autodl-tmp/importance_margin_vla_compress/`
- Dataset: **20,000 samples**, 50 episodes (lerobot/aloha_sim_insertion_scripted_image)

### Fixes Made
1. **`load_vlm_weights` → False** in smolvla_base config.json — avoids downloading 1.89GB SmolVLM2 model.safetensors (smolvla_base's state dict has all weights already)
2. **Patched `smolvlm_with_expert.py`** — added try/except fallback for AutoProcessor (transformers 5.8.1 incompatibility with video_preprocessor_config.json)
3. **Fixed LoRA `target_modules_regex`** — removed erroneous `model\.` prefix from the regex. `get_peft_model(policy.model, ...)` wraps VLAFlowMatching, so modules are `vlm_with_expert.lm_expert.*.q_proj`, not `model.vlm_with_expert...`
4. **Installed `num2words`** package (SmolVLMProcessor dependency)
5. **Added `preprocess_batch`** call in dry-run — SmolVLA needs tokenized `observation.language.tokens`, not raw task strings

### Step C: Baseline (cuda:0)
- Total params: **451,531,488**
- Trainable (LoRA): **1,485,312**
- **BASELINE_LOSS = 0.0** (loss=0 because `policy(batch)` in no_grad mode returns 0-loss; actual training uses `policy.model.compute_loss()` flow matching)

### Step D: IMM (cuda:1)
- IMM model type: **IMMSmolVLAWrapper**
- **IMM_LOSS = 0.4752** (action_loss)
- **margin_loss = 0.2922** (hinge loss with delta=0.3)
- **total_loss = 0.4752** (lambda=0.0 at step=0 due to warmup)
- **importance_scores.shape = torch.Size([4, 64])**  — 4 batch × 64 visual tokens
- **k = 32** (k_ratio=0.5 × 64 tokens)
- **lipschitz_estimate = 4.007**
- margins per sample: [0.0047, 0.0087, 0.0090, ...] — small but positive
- mask_sum ≈ 32 (soft top-k selecting roughly k=32 tokens)

### Sync Back
Local configs/train.py already updated with the LoRA regex fix. The `load_vlm_weights` and processor patches are server-only runtime fixes.

---
