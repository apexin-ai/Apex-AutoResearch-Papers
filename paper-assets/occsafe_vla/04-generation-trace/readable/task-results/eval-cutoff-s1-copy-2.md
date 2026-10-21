# eval cutoff s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cutoff_s1_20260523T002334_result.json`
- **Structured JSON:** [`bb21f4d7461516221f31.json`](../../sessions/bb/bb21f4d7461516221f31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**cutoff_s1 训练验证**:
- 50005 steps 完成，EXIT_CODE=0
- Checkpoint 完整（4 model shards + action_head + occ_head + proprio_projector）
- OCC loss cutoff 行为：loss 在 35K 后仍被 forward pass 计算并 log（0.011-0.015），但不参与 backprop

**cutoff_s1_eval 已在运行**:
- tmux session `cutoff_s1_eval` on westd-34685 cuda:3
- Task 0 已完成：TSR=0.980, CAR=0.980
- Task 1 进行中

**Registry 已更新**:
- `cutoff_s1`: 设置了 checkpoint_path 和 log_path
- `cutoff_s1_eval`: 创建并设为 RUNNING，parent=cutoff_s1

---
