# ops eval tail1024 epoch1

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_tail1024_epoch1_20260518T063358_result.json`
- **Structured JSON:** [`31dfbe52a7d3d999fdaa.json`](../../sessions/31/31dfbe52a7d3d999fdaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### CodeLlama-13B tail-1024 Epoch 1 (checkpoint-148) vs Epoch 3 (final)

| 指标 | Epoch 1 | Epoch 3 | 变化 |
|------|---------|---------|------|
| **Accuracy** | 79.9% [77.7%, 82.2%] | 87.6% [85.6%, 89.3%] | **-7.7pp** |
| **fail_recall** | 0.295 [0.249, 0.346] | 0.563 [0.509, 0.617] | **-0.268** |
| **fail_precision** | 1.00 | 1.00 | 不变 |
| **fail_F1** | 0.456 | 0.721 | -0.265 |
| **pass_recall** | 1.00 | 1.00 | 不变 |
| **pass_precision** | 0.781 | 0.852 | -0.071 |
| n_test | 1190 | 1190 | - |

**结论：epoch 1 没有恢复到 ~96%，反而更差（79.9% vs 87.6%）。** Epoch 1 的 fail_recall 只有 0.295（epoch 3 是 0.563），说明 epoch 1 欠拟合严重，模型几乎把所有样本都预测为 pass。这不是过拟合到恢复的问题，而是 CodeLlama-13B 在 tail-1024 条件下学习本身就困难，3 个 epoch 的训练方向是对的（accuracy 持续提升），但 fail_recall 仍远低于其他条件的 ~96%。

### tail-2048 训练进度
323/444 步（~73%），约 28s/step，预计还需 ~57 分钟完成。

---
