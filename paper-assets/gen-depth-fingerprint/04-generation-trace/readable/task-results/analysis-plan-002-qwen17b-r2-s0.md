# analysis plan 002 qwen17b r2 s0

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-002-qwen17b-r2-s0_20260514T231628_result.json`
- **Structured JSON:** [`d26323e4afa8af02e4d1.json`](../../sessions/d2/d26323e4afa8af02e4d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

**plan-002-qwen17b-r2-s0 结果：success**

- 2291 条记录，498 个 seed，无重复，2.50 MB
- depth 分布：`{0:498, 1:492, 2:468, 3:435, 4:398}`
- 跳过 199 条（vs shard1 的 53 条），主要在高 depth 层——depth4 只保留 398/498 (80%)
- 耗时 4548s (~76 min)，EXIT_CODE=0

注意：shard0 的跳过率(8.0%)明显高于 shard1(2.2%)，高 depth 衰减更严重，可能是 shard0 的 seed 分布导致更多 empty output。

---
