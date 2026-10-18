# ops pi05 official checkpoint

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pi05-official-checkpoint_20260521T044154_result.json`
- **Structured JSON:** [`8d42c091b77703db35bc.json`](../../sessions/8d/8d42c091b77703db35bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All cleaned up. Here's the summary:

---

## Report

### Bug Found & Fixed
**Root cause of 0% SR**: `patched_embed_image` in `eval_pi05_pruning_libero.py` line 93 had an erroneous `features = features * self.paligemma.config.text_config.hidden_size**0.5` (~45.25x scaling) that the original `embed_image` doesn't have. This completely distorted image embeddings.

**Fix**: Removed the scaling line from the original script.

### Checkpoint
Using `/root/autodl-tmp/pi05_libero_finetuned` — confirmed identical to `lerobot/pi05_libero` (same model.safetensors, 7,473,096,344 bytes). No separate download needed.

### 5-Episode Quick Test Results (seed=42, libero_object)

| Task | SR |
|------|-----|
| 0 | 80% (4/5) |
| 1 | 100% (5/5) |
| 2 | 100% (5/5) |
| 3 | 100% (5/5) |
| 4 | 100% (5/5) |
| 5 | 100% (5/5) |
| 6 | 100% (5/5) |
| 7 | 80% (4/5) |
| 8 | 100% (5/5) |
| 9 | 100% (5/5) |
| **Overall** | **96.0% (48/50)** |

### Full 50-Episode Eval
- **PID**: 818531 (python process)
- **GPU**: cuda:1 (CUDA_VISIBLE_DEVICES=1)
- **Log**: `logs/eval_pi05_baseline_object_seed42_official.log`
- **Command**: `python -u eval_pi05_pruning_libero.py --suite libero_object --prune_mode none --seed 42 --n_episodes 50 --gpu 1`
- **Status**: Running, Task 0 ep10: 10/10=100%
- **ETA**: ~1 hour

---
