# fix 1 7b planb control check ckpt

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_1_7b-planb-control-check-ckpt_20260518T194649_result.json`
- **Structured JSON:** [`0728afb4e9aafa86f5a3.json`](../../sessions/07/0728afb4e9aafa86f5a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

**adaptive_1_7b_seed42:**
- Checkpoints: `checkpoint-5500`, `checkpoint-6000`, `checkpoint-6103`
- `checkpoint-2500` is **gone** — confirmed deleted by `save_total_limit=3`
- `final/` exists with valid model files (3.4GB `model.safetensors`, config, tokenizer)

**uniform_1_7b_seed42_resumed:**
- Checkpoints: `checkpoint-2500`, `checkpoint-3000`, `checkpoint-3051`
- `final/` exists with valid model files (same size, 3.4GB)

Key takeaway: For the adaptive planb control experiment, `checkpoint-2500` is unavailable. However, `final/` (which corresponds to the end of training at step 6103) is intact. The uniform_resumed run used a `_resumed` suffix and had `checkpoint-2500` as its starting point — for adaptive, since the original checkpoint-2500 is deleted, you'd need to either:
1. Use the `final/` model directly (full training, not a checkpoint-2500 resume)
2. Use `checkpoint-5500` as the earliest available checkpoint
3. Retrain from scratch with `save_total_limit` increased to preserve checkpoint-2500

---
