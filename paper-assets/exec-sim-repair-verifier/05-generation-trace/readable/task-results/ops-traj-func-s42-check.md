# ops traj func s42 check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_traj-func-s42-check_20260516T125711_result.json`
- **Structured JSON:** [`d5c7dc4369a0290c2d7f.json`](../../sessions/d5/d5c7dc4369a0290c2d7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**deepseek-traj-func 训练结果：**

| 指标 | 值 |
|------|-----|
| 状态 | ✓ 成功完成 |
| Best eval_loss | **0.0793** (step 1008, epoch 2) |
| Epoch 1 eval_loss | 0.0943 |
| Epoch 3 eval_loss | 0.0884 |
| Train loss | 0.1131 |
| 训练耗时 | 48.5 min |
| Checkpoint | `/root/autodl-tmp/checkpoints_deepseek_traj_func/best` (LoRA adapter, 67MB) |

Best model 在 epoch 2 取得，epoch 3 eval_loss 略有回升（0.0793 → 0.0884），early stopping 选择正确。Registry 已更新为 DONE/success。

---
