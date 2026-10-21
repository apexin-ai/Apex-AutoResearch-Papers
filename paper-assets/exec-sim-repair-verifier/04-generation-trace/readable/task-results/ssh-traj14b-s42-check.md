# ssh traj14b s42 check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_traj14b-s42-check_20260523T104704_result.json`
- **Structured JSON:** [`bd157d1602e48a0bc200.json`](../../sessions/bd/bd157d1602e48a0bc200.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在，无需删除。

## 汇报

### traj14b-func-s42 — 训练成功

| 指标 | 值 |
|------|-----|
| best checkpoint | `/root/autodl-tmp/checkpoints/traj14b-func-s42/best` (step 504, epoch 2) |
| best eval_loss | **0.0762** |
| final eval_loss (epoch 3) | 0.0958 |
| train_loss | 0.1312 |
| 训练时长 | ~1h37m (5838s) |

Eval loss 曲线：epoch 1 → 0.0977, epoch 2 → 0.0762 (best), epoch 3 → 0.0958（轻微过拟合，best checkpoint 正确保存在 epoch 2）。

### traj14b-func-s456 — 也已完成

| 指标 | 值 |
|------|-----|
| best checkpoint | `/root/autodl-tmp/checkpoints/traj14b-func-s456/best` |
| final eval_loss | 0.0971 |
| train_loss | 0.1257 |
| 训练时长 | ~1h37m (5811s) |

三个 seed 全部训练完成。

---
