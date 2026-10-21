# analysis plan 005 postprocess

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-005-postprocess_20260515T041900_result.json`
- **Structured JSON:** [`ef998ea25f2cae3eda86.json`](../../sessions/ef/ef998ea25f2cae3eda86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**当前状态：3 个生成任务均在运行中，尚未完成。**

| Prompt Type | Records | Seeds | Max Seed | Depth Distribution (0/1/2/3/4) |
|---|---|---|---|---|
| continuation | 1785 | 381 | 380 | 381 / 378 / 359 / 342 / 325 |
| elaboration | 1670 | 336 | 335 | 336 / 336 / 334 / 333 / 331 |
| inspired_rewriting | 1703 | 348 | 347 | 348 / 347 / 339 / 335 / 334 |

**进度与 ETA**（sessions 从 11:28 开始，已运行 ~52 分钟）：

- **continuation**: 381/995 seeds (38%), ~7.3 seeds/min → 剩余 ~84 min, 预计 **~13:45**
- **elaboration**: 336/995 seeds (34%), ~6.5 seeds/min → 剩余 ~101 min, 预计 **~14:00**
- **inspired_rewriting**: 348/995 seeds (35%), ~6.7 seeds/min → 剩余 ~97 min, 预计 **~13:57**

**初步观察**：
- continuation 的高 depth 样本衰减明显（depth 0→4: 381→325, 丢失 15%），elaboration 几乎无衰减（336→331, 仅 1.5%）。这说明 continuation 在递归生成时更容易产生低质量/被过滤的文本。
- GPU 0 使用率 81%（跑 Pythia-2.8B 生成），GPU 1-3 各 ~66%（3 个 prompt type 并行）。

全部完成预计在 **14:00 左右**。届时可以执行后处理（验证 → 特征提取 → XGBoost 对比）。需要我到时再来检查，还是你手动触发？

---
