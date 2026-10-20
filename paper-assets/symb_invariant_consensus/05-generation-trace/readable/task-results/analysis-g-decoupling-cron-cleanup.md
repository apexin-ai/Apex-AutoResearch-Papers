# analysis g decoupling cron cleanup

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_g-decoupling-cron-cleanup_20260520T205454_result.json`
- **Structured JSON:** [`8911931fed1f8819db09.json`](../../sessions/89/8911931fed1f8819db09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job（可能是在之前的 session 中创建的，已随 session 结束自动清除）。

**总结：**
- 实验已完成，3 种 decoupling 策略均为 negative：conservative 53.92%、standard 54.41%（= SC baseline）、aggressive 53.92%
- Registry 已更新为 DONE，metrics 包含全部 3 种策略结果
- 无需清理 cron（本 session 无活跃 cron）

---
