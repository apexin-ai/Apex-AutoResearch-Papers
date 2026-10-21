# ops check grid b0 3 and dr completion

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_grid_b0_3_and_dr_completion_20260518T080958_result.json`
- **Structured JSON:** [`a7a1dcae216eb7fcd9bb.json`](../../sessions/a7/a7a1dcae216eb7fcd9bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

```
contamination_60_grid_b0_3_seed42: DONE ✓
  - 6103/6103 steps, runtime 2h41m
  - Output: final/, checkpoint-6103, checkpoint-6000, checkpoint-5500
  - train_loss: 6.608, epoch: 0.26
  - Registry → ANALYZING, checkpoint_path + log_path 已设置
  - cuda:2 已释放 (0%, 0 MiB)

detect_remove_q05_seed123: RUNNING
  - ~step 1850+/8477 (~22%), ETA ~30min
  - checkpoint-500 存在, 无 final/
  - PID 13576 on cuda:0 (76%, 70237 MiB), 无 tmux session（后台进程）
  - 3.59 it/s

detect_remove_q05_seed456: RUNNING
  - step 1850/8477 (22%), ETA ~31min
  - checkpoint-500 存在, 无 final/
  - cuda:1 (99%, 70237 MiB), tmux session 活跃
  - 3.59 it/s

contamination_60_random_seed42: RUNNING
  - step 5648/6103 (93%), ETA ~16min
  - checkpoint-4500, 5000, 5500 存在
  - cuda:3 (99%, 41757 MiB), tmux session 活跃
```

seed123/456 还在早期阶段（22%），远未完成，无法跑 eval。contamination_60_random_seed42 约 16 分钟后完成。

---
