# diagnose eval pi05 zeromask random k09 object seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_zeromask_random_k09_object_seed42_v3_20260526T061035_result.json`
- **Structured JSON:** [`5d8135f023b9d4bda009.json`](../../sessions/5d/5d8135f023b9d4bda009.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：SUCCESS**

| 指标 | 值 |
|------|-----|
| Overall SR | **98.0%** (490/500) |
| 耗时 | 83 min |

Per-task: T0=96%, T1=96%, T2=100%, T3=94%, T4=98%, T5=100%, T6=100%, T7=98%, T8=100%, T9=98%

v3 结果与 ROADMAP D234 记录的 98.0% 完全一致，确认 zeromask random k=0.9 Object 结果稳定可复现。Cron 已无需清除（不存在）。Registry 已标记 DONE/success。

---
