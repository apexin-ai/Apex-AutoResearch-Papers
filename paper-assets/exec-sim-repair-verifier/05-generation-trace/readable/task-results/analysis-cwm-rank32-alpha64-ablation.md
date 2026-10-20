# analysis cwm rank32 alpha64 ablation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm-rank32-alpha64-ablation_20260515T154249_result.json`
- **Structured JSON:** [`2ba319e36f0d31ea8ad7.json`](../../sessions/2b/2ba319e36f0d31ea8ad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 训练指标
```
train_loss: 0.2069
eval_loss_epoch1: 0.0665
eval_loss_epoch2: 0.0555
eval_loss_epoch3: 0.0606
total_steps: 1434 (3 epochs)
训练状态: 正常完成 (EXIT_CODE=0)
```

### 评估指标
```
overall_accuracy: 87.0%
pass_f1: 86.8%
fail_f1: 87.3%
pass_precision: 91.8%
pass_recall: 82.3%
fail_precision: 82.9%
fail_recall: 92.1%
exact_match_rate: 84.6%
unparseable_predictions: 0 (推断自 confusion matrix 总和=1890)
```

### 与 baseline 对比

| 配置 | Rank | Alpha | Ratio | Accuracy |
|------|------|-------|-------|----------|
| CWM baseline | 16 | 32 | 2 | **87.51%** |
| rank32-ablation-v2 | 32 | 32 | 1 | 87.0% |
| **rank32-alpha64 (本实验)** | 32 | **64** | **2** | **87.0%** |

### 分析

rank=32, alpha=64 (ratio=2) 的准确率为 87.0%，与 rank=32, alpha=32 (ratio=1) 完全一致，均低于 baseline (rank=16) 的 87.51%。

这说明：
- **alpha/rank ratio 不是导致 rank32 降低的原因**——修正 ratio 到 2 没有恢复性能
- **rank=32 本身就比 rank=16 差**，对这个任务而言 rank=16 已经足够，增加 rank 带来的过参数化反而轻微损害了泛化

eval_loss 走势也支持这一点：epoch2 最低 (0.0555) 但 epoch3 回升 (0.0606)，出现轻微过拟合，与更大 rank 的过参数化一致。

---
