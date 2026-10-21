# diagnose plan 008 router size

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-008-router-size_20260515T135414_result.json`
- **Structured JSON:** [`a3c86a618d5f187f713d.json`](../../sessions/a3/a3c86a618d5f187f713d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。Registry 已更新，cron 已清除。

## 结果摘要

**conclusion: negative** — 三个模型全部退化，router capacity 不是瓶颈。

| Model | BalAcc | IntRecall | DetRecall | EvalLoss |
|-------|--------|-----------|-----------|----------|
| Qwen3-1.7B | 0.50 | 1.00 | 0.00 | 0.474 |
| Qwen2.5-1.5B | 0.50 | 1.00 | 0.00 | 1.463 |
| Qwen2.5-3B | 0.50 | 1.00 | 0.00 | 1.380 |

三个模型（1.5B/1.7B/3B）行为完全一致：把所有 306 个样本都预测为 internal（少数类），deterministic recall=0。balanced_acc=0.5 = (1.0+0.0)/2，是纯退化结果。

**解读**：三者差异为零，匹配第三种情况——**router capacity 不是瓶颈，routing signal 本身有限（支撑 C1）**。问题不在模型大小，而在训练信号/数据本身不足以区分两类路由。值得注意的是 Qwen3-1.7B 的 eval_loss (0.474) 远低于另外两个 (~1.4)，但这并未转化为任何分类能力的差异。

---
