# diagnose cutoff s0 exit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cutoff-s0-exit_20260522T134045_result.json`
- **Structured JSON:** [`7078fc8682521126ae76.json`](../../sessions/70/7078fc8682521126ae76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**cutoff_s0 实验仍在正常运行，没有退出。**

| 项目 | 详情 |
|------|------|
| 状态 | **RUNNING** — 正常训练中 |
| 实际进程 PID | **137021**（不是 136037，136037 是父 torchrun 进程） |
| 当前进度 | **16437/50005 (33%)**, 已运行 5h32m |
| 速度 | ~1.05 it/s |
| 最新 loss | step 16400: occ_loss=0.0089, action_loss=0.1416 |
| 已保存 checkpoint | 10000_chkpt (`/root/autodl-tmp/checkpoints/cutoff_s0/`) |
| 预计剩余 | ~8-9 小时 |
| GPU | cuda:0, 62194 MiB 占用 |

**原因分析**: cron 监控的 PID 136037 是 `torchrun` 启动器进程，而实际训练进程是 PID 137021。136037 可能已退出（torchrun wrapper 行为），但训练本身正常。

不需要更新 registry 状态或删除 cron — 实验仍在进行中。建议将 cron 监控的 PID 更新为 137021，或改用日志/checkpoint 判断完成状态。

---
