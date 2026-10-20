# monitor v5 epoch1 loss

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5-epoch1-loss_20260514T065740_result.json`
- **Structured JSON:** [`5f72c222f893dbe71ebf.json`](../../sessions/5f/5f72c222f893dbe71ebf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan-002-formal-v5 完整报告

### 进程状态
**已完成** — PID 235437 不存在，TRAINING_COMPLETE sentinel 已写入（14:57:39）。3 epoch 共耗时 ~16 分钟。

### Train Loss（每 10 步记录，共 51 步/epoch）

| Epoch | Steps | Loss 范围 |
|-------|-------|-----------|
| 1 | 10-50 | **11.51 → 6.43 → 7.87 → 5.73 → 5.15** |
| 2 | 60-100 | 4.73 → 4.99 → 4.19 → 4.69 → 5.37 |
| 3 | 110-150 | 4.59 → 4.91 → 4.86 → 4.16 → 4.76 |

**Average train_loss（全程）: 5.59**

### Eval Metrics（每 epoch 结束）

| Metric | Epoch 1 | Epoch 2 | Epoch 3 |
|--------|---------|---------|---------|
| eval_loss | 0.792 | 0.775 | 0.782 |
| accuracy | 0.874 | 0.888 | **0.917** |
| balanced_accuracy | 0.471 | 0.478 | 0.494 |
| **recall_internal** | **0.0** | **0.0** | **0.0** |
| precision_internal | 0.0 | 0.0 | 0.0 |
| f1_internal | 0.0 | 0.0 | 0.0 |
| recall_deterministic | 0.941 | 0.956 | 0.987 |
| f1_macro | 0.466 | 0.470 | 0.478 |

### Confusion Matrix（最终）
```
              pred_internal  pred_deterministic
true_internal        0              30
true_determ          5             385
```

30/30 internal 样本全部误分类为 deterministic，0% internal recall。

### 判断

**确认 Reviewer 诊断正确：**
- train_loss 在 **4-12 范围**（远高于正常的 0.5-0.7）— 异常 ✓
- internal recall = **0.0**，三个 epoch 都是 0 — 异常 ✓
- 模型完全无法学到 internal 类别，class_weights `[4.5, 0.5625]` 导致 loss 被 internal 样本主导但梯度方向混乱，最终模型退化为全部预测 deterministic
- **根因是 class_weights 设置，而非 pad_token_id**

---
