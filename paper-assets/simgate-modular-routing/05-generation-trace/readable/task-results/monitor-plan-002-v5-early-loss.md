# monitor plan 002 v5 early loss

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_plan-002-v5-early-loss_20260514T065644_result.json`
- **Structured JSON:** [`c67b97228319dcfa215d.json`](../../sessions/c6/c67b97228319dcfa215d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**LOSS_ABNORMAL — v5 问题未修复。**

训练已完成（3 epochs, 958s），结果：

| 阶段 | Train Loss | Eval Loss |
|------|-----------|-----------|
| Epoch 0.2 | **11.51** | — |
| Epoch 0.4 | 6.43 | — |
| Epoch 0.6 | 7.87 | — |
| Epoch 0.8 | 5.73 | — |
| Epoch 1.0 | 5.15 | 0.79 |
| Epoch 2.2-2.9 | 4.16~4.91 | 0.78 |
| **平均** | **5.59** | — |

**Class weights**: `internal=4.5, deterministic=0.5625` — 已生效打印。

**核心问题**：
1. Train loss 全程 4-11，远超正常值 0.5-0.7，与 v3/v4 一样异常
2. **Internal 类完全没学到** — 3 个 epoch 的 eval 中 precision/recall/f1 全为 0.0，模型把所有样本都预测为 deterministic
3. Train loss (5.59) 与 eval loss (0.78) 差距巨大，说明 class_weights 放大了 train loss 但没有实际引导模型学到少数类
4. Grad norm 极高（604→70-160），训练不稳定
5. 无 assert 错误

**结论**：单纯加 class_weights 不足以解决类别不平衡问题。可能需要检查：数据是否真的有可区分的 internal 模式、loss 计算逻辑是否正确、或换用 focal loss / oversampling 等策略。

---
