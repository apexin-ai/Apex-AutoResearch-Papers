# analysis eval pi05 attn k095 long seed42 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_attn_k095_long_seed42_strict_w41_20260527T110319_result.json`
- **Structured JSON:** [`d3075c687086bb39a7d5.json`](../../sessions/d3/d3075c687086bb39a7d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验仍在运行中，尚未完成。

**当前进度：**
- Task 0: **94.0%** (47/50) — 已完成，耗时 13 min
- Task 1: 进行中，已跑 30 episodes（30/30 = 100% so far）
- 剩余 Task 2-9 未开始

**时间估算：** 每个 task 约 13 分钟，10 个 task 总计约 130 分钟。实验从 18:41 开始，预计约 20:51 完成（服务器时间）。

**初步观察：**
- Task 0 的 94% SR 是个不错的起步，比 lenient 的节奏来看表现正常
- 无错误或异常，pruning 正常工作（243/256 tokens kept per image）

需要等实验跑完再做完整分析和 registry 更新。要不要我稍后再来检查结果？

---
