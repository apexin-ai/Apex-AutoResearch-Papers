# harvest eval xvla random k05 goal seed43 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_xvla_random_k05_goal_seed43_v4_20260524T005647_result.json`
- **Structured JSON:** [`b7d89be9ce19962c38fb.json`](../../sessions/b7/b7d89be9ce19962c38fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success.

## 结果报告

**eval_xvla_random_k05_goal_seed43_v4** — 正常完成，10 task 全跑完。

| | seed42 | seed43 | Mean |
|---|---|---|---|
| **SR** | 67.2% | 68.6% | **67.9%** |

差异仅 1.4pp，CV 非常一致。两个 seed 的 95% Wilson CI 重叠，结果可靠。

Per-task 分布也一致：T5 (push plate) 和 T9 (wine on rack) 两个 seed 都是 0%，T0/T4/T7/T8 都接近满分。

**westd-38929 GPU 3 已空闲可用。** 无 cron 需要删除（本 session 无活跃 cron）。

---
