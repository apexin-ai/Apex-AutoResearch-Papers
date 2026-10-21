# eval d063 val sweep home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d063-val-sweep-home_20260514T084118_result.json`
- **Structured JSON:** [`a3d9ebf8e09a1f4c1e6a.json`](../../sessions/a3/a3d9ebf8e09a1f4c1e6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Val sweep 正在正常运行，无需额外操作。当前进度：

**已完成 (5/13)**（seed123_home 系列全部完成）:

| Checkpoint | Acc | F1 Macro | Fail F1 | Pass F1 |
|---|---|---|---|---|
| seed123_home/ckpt-200 | 62.51 | 55.54 | 37.94 | 73.14 |
| seed123_home/ckpt-400 | 80.72 | 67.03 | 45.78 | 88.27 |
| seed123_home/ckpt-600 | 76.78 | 66.81 | 48.63 | 85.00 |
| seed123_home/ckpt-800 | **81.81** | **69.14** | **49.37** | 88.91 |
| seed123_home/ckpt-1000 | 82.30 | 67.63 | 45.84 | **89.42** |

**正在评估**: `checkpoints_repo_cls_v5/checkpoint-600`

**剩余 7 个**: v5 系列 (checkpoint-4000/4200/4400/4600) + home 系列 (checkpoint-200/2400/2600)

预计还需约 3-4 小时完成全部 sweep。tmux session `val_sweep` 在正常运行，不需要用 submit_training_job 重新启动。

---
