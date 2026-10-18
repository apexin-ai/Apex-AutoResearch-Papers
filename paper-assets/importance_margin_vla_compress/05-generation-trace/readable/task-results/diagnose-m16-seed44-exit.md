# diagnose m16 seed44 exit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_m16_seed44_exit_20260519T044855_result.json`
- **Structured JSON:** [`c3540a079d70712c19fb.json`](../../sessions/c3/c3540a079d70712c19fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练进程**仍在运行**，并未退出。

- **状态**: 正常训练中，step 11450/100000（11.45%）
- **最新 loss**: ~0.08-0.18 范围，正常
- **eval/action_loss** (step 10000): 0.1190
- **速度**: 5.0 sps，稳定
- **Checkpoint**: `checkpoint.pt` 存在，1.75GB，最新保存在 step 11000
- **tmux session**: 已消失，但进程通过 nohup 在后台运行，不受影响
- **进程数**: 1 主进程 + 4 worker 进程，GPU 占用正常

结论：训练正常进行中，无需更新 registry 或删除 cron。tmux session 消失不影响训练（nohup 启动）。

---
