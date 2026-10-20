# check mt6144 progress v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mt6144_progress_v2_20260515T112358_result.json`
- **Structured JSON:** [`2d0f04fa11734e4e1d35.json`](../../sessions/2d/2d0f04fa11734e4e1d35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
## llama_docred_unconstrained_mt6144 (cuda:0)
Status: RUNNING (uptime 3h05m)
Progress: 548/998 docs (54.9%)
Rate: ~2.96 docs/min
ETA: ~2h32m remaining

## llama_docred_full_s1_mt6144 (cuda:1) ⚠️ 含 CF fallback 逻辑
Status: RUNNING (uptime 3h02m)
Progress: 441/998 docs (44.2%)
Rate: ~2.42 docs/min
ETA: ~3h50m remaining
注: 日志中大量 "Grammar-first fallback triggered" — 语义掩码频繁被跳过，
    full_s1 因 constrained decoding 开销比 unconstrained 慢约 18%。
```

unconstrained 预计约 2.5h 后完成，full_s1 预计约 4h 后完成。需要稍后再检查收集结果。

---
