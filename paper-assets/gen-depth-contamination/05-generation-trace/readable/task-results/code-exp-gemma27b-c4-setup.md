# code exp gemma27b c4 setup

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_gemma27b_c4_setup_20260522T075802_result.json`
- **Structured JSON:** [`55f73d6b45deb869826a.json`](../../sessions/55/55f73d6b45deb869826a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Generation is running successfully with bf16. Progress: 5/625 batches at ~14.3s/batch for depth 1. That's ~2.5 hours per depth, ~12.5 hours total for all 5 depths (generation only).

Summary:
- **Model**: Gemma-2-27B loaded in bf16, no NaN errors
- **Generation**: depth 1 in progress, ~14.3s/batch, ~2.5h per depth
- **Estimated total**: ~12-15h for Phase 1 (generation + self-scoring) + ~1h for Phase 2 (Qwen cross-scoring)
- **Server**: cqa1-22115, cuda:0, tmux session `exp_gemma27b_c4`
- **PID**: 26893
- **Registry**: `seed_gemma27b_c4_s42` → RUNNING
- **Fix applied**: Added `--dtype bf16` flag to `run_pipeline.py` to handle Gemma-2's logit softcapping (fp16 causes NaN overflow)

---
