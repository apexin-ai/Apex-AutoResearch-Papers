# code fix bca bootstrap llama baseline

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-bca-bootstrap-llama-baseline_20260524T061836_result.json`
- **Structured JSON:** [`78d53d905a2db3f57748.json`](../../sessions/78/78d53d905a2db3f57748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`llama_free` 的 mean=+0.262, SD=1.542，已经是 V2 的值了。文件中也不存在 `-0.312` 这个字面量。

当前 `bca_bootstrap.py` 中 Llama clean baseline **已经是正确的 V2 值**，不需要修改。

---
