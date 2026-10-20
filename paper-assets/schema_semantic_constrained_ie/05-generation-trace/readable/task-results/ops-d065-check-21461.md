# ops d065 check 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d065-check-21461_20260520T081817_result.json`
- **Structured JSON:** [`4c78b633413801a0536c.json`](../../sessions/4c/4c78b633413801a0536c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态汇总：**

| Run | 进度 | 状态 | ETA |
|-----|------|------|-----|
| **d065 Qwen greedy unc 4096** (GPU0, PID 167691) | 878/998 (jsonl) / log 在 823 | 运行中 | ~17:20 CST (~60min) |
| **d065 Qwen greedy con 4096** (GPU1, PID 174618) | 700/998 (jsonl) / log 在 656 | 运行中 | ~18:00-18:30 CST (~100-120min) |

- UNC 从 11:14 CST 开始，已跑 ~5h，平均 ~22s/doc，剩 120 doc
- CON 较慢（constrained 解码开销 + 偶有 FAIL 耗时 77s），剩 ~300 doc
- GPU 利用率正常（84-86%），18.9GB/97.9GB 显存

两个 ETA 都超过了原来的预估（~15:50/16:00 UTC）。等完成后需要再查一次行数并跑 eval。要我稍后再来检查吗？

---
