# diag crm object training progress v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_crm-object-training-progress-v2_20260521T191008_result.json`
- **Structured JSON:** [`7c6135c5a2b7e4700f68.json`](../../sessions/7c/7c6135c5a2b7e4700f68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**CRM Object Training 状态**

| 项目 | 值 |
|---|---|
| 进程 | PID 800111 存活，已运行 48:58 |
| 当前 | Epoch 7（batch ~350/1950） |
| 已完成 | 6/50 epochs |
| Epoch 6 | train_loss=0.009881, val_loss=0.005511 (best) |
| Epoch 5 | train_loss=0.010034, val_loss=0.005544 |
| Checkpoints | epoch0002–epoch0006.pt + crm_best.pt |

**Loss 趋势**: train 从 0.029（epoch 5 起点）→ 0.0099（epoch 6 末）稳定下降；val 从 0.005544 → 0.005511，已开始平台。

**ETA**: 每 epoch ≈ 7.3 分钟（checkpoint 时间戳 02:40 → 03:09, 4 epochs/29min）。剩余 ~43.5 epochs × 7.3min ≈ **5.3 小时**（约 08:30 完成）。

---
