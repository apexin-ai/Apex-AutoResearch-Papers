# train c5 roboflamingo finetune

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_c5_roboflamingo_finetune_20260519T192920_result.json`
- **Structured JSON:** [`7b6b5c844ee262bf20a2.json`](../../sessions/7b/7b6b5c844ee262bf20a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 steps complete:

| Step | Status |
|------|--------|
| 1. Server confirmation | westd-41074, 4x RTX PRO 6000 (96 GB each) |
| 2. factory.py `from_config` fix | `AutoConfig.from_pretrained` + `from_config`, unfroze backbone, added `trust_remote_code=True` to tokenizer, CLIP local cache |
| 3. Dry-run (forward+backward+checkpoint) | PASSED — arm_pred `(2,12,6)`, grip_pred `(2,12,1)`, backward OK, 10.9 GB checkpoint |
| 4. Submit training job | PID 43102, tmux `c5-roboflamingo-libero-baseline`, GPU:1 |
| 5. Training verified | Step 50: Loss 0.0806, Arm 0.0837, Grip 0.8456, GPU 1 at 100%, 48 GB VRAM |

**Patches applied:**
- `factory.py`: `from_config` for MPT (no weight download), CLIP local cache, backbone unfreeze, `trust_remote_code=True` on tokenizer
- `train_libero.py`: `debug=True`, embedding resize before checkpoint load, `TRUST_REMOTE_CODE` env var
- `action_head.py`: `copy.deepcopy(input_feature)` → `input_feature.clone().detach()` (PyTorch 2.6 compatibility)

---
