# ops kill orphan 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_orphan_19828_20260518T234204_result.json`
- **Structured JSON:** [`6064b7de93327d1738b2.json`](../../sessions/60/6064b7de93327d1738b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**Kill 前 → Kill 后 (cuda:1)**

| 指标 | Kill 前 | Kill 后 | 变化 |
|------|---------|---------|------|
| memory.used | 75,180 MiB | 37,607 MiB | **-37,573 MiB (-50%)** |
| utilization.gpu | 98% | 98% | 不变 |
| 进程数 | 2 (395612 + 399353) | 1 (399353) | -1 |

- PID 395612 (bf16 v1 孤儿) 已终止，释放 ~37.5 GB 显存
- PID 399353 (fp32 v2) 正常运行，CPU 131%，独占 cuda:1
- cuda:1 从 77% 显存占用降至 38%，fp32 v2 不再受内存争抢

---
