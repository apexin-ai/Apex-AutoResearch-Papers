# analysis deepseek cwm func

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-cwm-func_20260516T075814_result.json`
- **Structured JSON:** [`a3fb892cab071c054569.json`](../../sessions/a3/a3fb892cab071c054569.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## deepseek-cwm-func 训练结果汇总

### 状态：完整完成 ✓

训练正常完成 3 个 epoch，EXIT_CODE=0，总耗时 ~87 分钟（5215s）。

### 关键指标

| 指标 | 值 |
|------|------|
| **最终 train loss** | 0.0986 (avg), 最后 step 0.0152 |
| **Best eval loss** | **0.04292** (epoch 2, step 956) |
| **Epoch 1 eval loss** | 0.04581 |
| **Epoch 2 eval loss** | 0.04292 ← best |
| **Epoch 3 eval loss** | 0.04575 |
| Train speed | 8.8 samples/s, 0.275 steps/s |

### Loss 趋势

Train loss 持续下降：1.89 → 0.10 → 0.08 → ... → 0.012（最后 step）。但 eval loss 在 epoch 2 达到最优后 epoch 3 略微回升（0.04292 → 0.04575），有轻微 overfitting 迹象。

### Checkpoints

| 路径 | 说明 |
|------|------|
| `checkpoints_deepseek_cwm_func/best/` | Best model（对应 step 956 / epoch 2） |
| `checkpoints_deepseek_cwm_func/checkpoint-956/` | epoch 2 结束时 |
| `checkpoints_deepseek_cwm_func/checkpoint-1434/` | epoch 3 结束时（最终） |

总大小：456 MB（LoRA adapter，非全量模型）。

### Best checkpoint

- 路径：`/root/autodl-tmp/checkpoints_deepseek_cwm_func/checkpoint-956`
- 对应 metric：eval_loss = 0.04292
- `best/` 目录已保存该 adapter 的副本

### 注意事项

- Epoch 3 eval loss 比 epoch 2 高 6.6%，说明 2 epoch 可能已经足够
- 无 eval accuracy 指标输出（仅记录 eval_loss），后续 eval 需要用 generation + exact match 方式评估

---
