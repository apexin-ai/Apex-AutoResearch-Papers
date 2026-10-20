# analysis deepseek training logs

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-training-logs_20260516T080159_result.json`
- **Structured JSON:** [`192614715bda0b963bb9.json`](../../sessions/19/192614715bda0b963bb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/deepseek_training_analysis.md`。

**摘要：**

| | CWM (seed123) | CLS |
|---|---|---|
| 状态 | SUCCESS | SUCCESS |
| Best eval_loss | **0.04076** (epoch 2) | **0.07008** (epoch 1) |
| Final train_loss | 0.0976 | 0.0948 |
| 训练时长 | 87.4 min | 90.7 min |
| 过拟合 | epoch 3 轻微 (+10.7%) | epoch 1 起单调上升 |

CWM eval_loss 比 CLS 低 42%（0.041 vs 0.070）。日志中无 accuracy 指标，两者均只记录了 loss。Checkpoint 均已正确保存（adapter_model.safetensors 67MB）。

---
