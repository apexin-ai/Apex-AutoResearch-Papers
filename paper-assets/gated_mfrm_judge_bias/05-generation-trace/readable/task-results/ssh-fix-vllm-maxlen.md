# ssh fix vllm maxlen

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_vllm_maxlen_20260522T161646_result.json`
- **Structured JSON:** [`d6af6d0d8990c05e3ad7.json`](../../sessions/d6/d6af6d0d8990c05e3ad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Summary:

| Port | Model | Change | Status |
|------|-------|--------|--------|
| 8001 | llama-3.3-70b | untouched | ✅ running |
| 8002 | qwen2.5-72b (PID 405118) | max-model-len 4096→8192, +enforce-eager | ✅ serving, 0 context length errors |
| 8003 | mistral-large-2 (PID 405185) | max-model-len 4096→8192, +enforce-eager | ✅ serving, 0 context length errors |

Both restarted with `VLLM_USE_FLASHINFER_SAMPLER=0`, `--enforce-eager`, `--max-model-len 8192`. Judge collector processes recovered and are actively writing results. No more context length errors.

Note: `generate_vllm_online.py` (PID 247295) was already dead before the restart — not caused by this change.

---
