# ssh vllm fix verification

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_vllm_fix_verification_20260523T220454_result.json`
- **Structured JSON:** [`ac08768ac2ce76578eac.json`](../../sessions/ac/ac08768ac2ce76578eac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have enough data. Let me compile the results.

**Target per judge:** 500 questions × 18 target models × 2 positions = **18,000**

---

## Verification Results

### 1. `/tmp/final_check.txt` — All clear
- vLLM: ports 8001/8002/8003 all confirmed **max_model_len: 8192** ✓
- All collect.py processes running ✓
- **400 errors: 0** on all three fixed logs ✓

### 2. JSONL counts vs baseline (local judges)

| Judge | Baseline | Current | Delta | % Complete |
|-------|----------|---------|-------|------------|
| llama-3.3-70b | 7,128 | 7,337 | **+209** | 40.8% |
| qwen2.5-72b | 9,922 | 10,045 | **+123** | 55.8% |
| mistral-large-2 | 9,425 | 9,508 | **+83** | 52.8% |

Note: `llama-3.3-70b-shard2` has 5,943 lines (separate output dir), so llama total = 13,280 if combined → 73.8%.

### 3. 400 errors
**0 across all three fixed logs.** Fix confirmed working.

### 4. vLLM max_model_len
**8192** on all three ports. Confirmed.

### 5. API judges (still running)

| Judge | Lines |
|-------|-------|
| claude-sonnet-4.6-proxy | 12,147 |
| claude-opus-4.7-proxy | 9,111 |
| gpt-5.5-proxy | 8,926 |
| qwen3-235b-proxy | 8,946 |
| gemini-2.5-pro-proxy | 8,363 |
| deepseek-v4-pro-proxy | 7,383 |

6 API judge processes confirmed running.

### 6. Rates & ETA (local judges, ~35 min elapsed since restart)

| Judge | Rate (items/hr) | Remaining | ETA |
|-------|----------------|-----------|-----|
| llama | ~358 | 4,720 (if shard2 combined) or 10,663 | ~13h or ~30h |
| qwen | ~211 | 7,955 | ~38h |
| mistral | ~142 | 8,492 | ~60h |

Rates may still be ramping up — these are early estimates. The key takeaway: **the 400 error fix is confirmed working**, all judges are making progress, and no new errors are appearing.

---
