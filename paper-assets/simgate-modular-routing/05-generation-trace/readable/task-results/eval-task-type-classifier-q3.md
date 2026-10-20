# eval task type classifier q3

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_task-type-classifier-q3_20260516T200346_result.json`
- **Structured JSON:** [`483c3ff011129e68d683.json`](../../sessions/48/483c3ff011129e68d683.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

```
=== Task-type Classifier Results ===

Majority vote per task type:
  所有 11 个 task type 的 majority label 都是 no-pref（50%–75%）
  Overall accuracy: 61.2%
  Balanced accuracy: 33.3%（≈ 随机三分类）

Logistic Regression (5-fold CV):
  Mean accuracy: 60.0% (±2.4%)
  Mean balanced accuracy: 32.8% (±1.0%)

LOOCV accuracy: 61.2%
```

**结论：routing signal 不是 task-type-level property。** Accuracy 61.2% 远低于 80% 阈值，balanced accuracy 仅 33.3%（等同随机猜测）。分类器退化为全部预测 no-pref（因为 no-pref 占 150/245 = 61%），无法区分 det-pref 和 int-pref。Task type 单独不能预测 routing label——routing 决策发生在 episode 层面，取决于 episode-specific 因素而非 task 类型。

结果已保存到 `guided_router/task_classifier_results.json`。

---
