# experiment llama folio fix rerun

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_llama-folio-fix-rerun_20260522T110510_result.json`
- **Structured JSON:** [`315edab2b1f3f95fb6c2.json`](../../sessions/31/315edab2b1f3f95fb6c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，实验正常运行。

**汇报：**

| 项目 | 值 |
|------|-----|
| 新 vLLM PID | 595261 (port 8002, max-model-len=8192) |
| Master PID | 596151 |
| 首个问题结果 | folio_0: SICA=Unknown, SC=Unknown, gold=Unknown → **两个都正确** |
| 首个问题耗时 | 70.5s |
| SICA accuracy (1/1) | 1.0 |
| SC accuracy (1/1) | 1.0 |
| ETA | FOLIO 204 题 × ~70s/题 × 3 seeds ≈ **~12 小时** |

根因确认：之前 `max-model-len=4096` + `max_tokens=4096` 导致所有请求 400。现已改为 `max-model-len=8192` + `max_tokens=2048`，请求全部 200 OK。

---
