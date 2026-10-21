# ops d108 progress check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d108-progress-check_20260520T181134_result.json`
- **Structured JSON:** [`1554d932ee49f7630f79.json`](../../sessions/15/1554d932ee49f7630f79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**D108 L2 Norm Sweep 已全部完成。** 4 个 GPU 均已空闲（0% 利用率，0 MiB 显存）。

## 结果汇总（libero_object, 10 tasks × 50 episodes = 500 total）

| k 值 | Success Rate | 耗时 (min) | 完成时间 |
|------|-------------|-----------|---------|
| **0.3** | **25.0%** | 310 | 05-21 02:04 |
| **0.5** | **39.2%** | 281 | 05-21 01:35 |
| **0.9** | **70.6%** | 242 | 05-21 01:20 |
| **0.95** | **70.6%** | 250 | 05-21 01:28 |

趋势清晰：k=0.9 和 k=0.95 性能相同（70.6%），k 降到 0.5 大幅下降到 39.2%，k=0.3 进一步降到 25.0%。拐点在 0.5→0.9 之间。

---
