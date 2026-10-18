# diagnose train acis stage1only k03 k07

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_acis_stage1only_k03_k07_20260517T074121_result.json`
- **Structured JSON:** [`bb47ff2443e6cb379c35.json`](../../sessions/bb/bb47ff2443e6cb379c35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**两个实验都在正常运行，cron 误报。**

**直接原因：** `WANDB_MODE=offline` 导致 W&B 数据仅保存在本地，不同步到云端。cron 监控通过检查 W&B 云端 run 和 sentinel 文件判断进程存活状态，两者都不存在，因此误判为 dead。

**当前状态：**
- k03: step ~6050/10000，GPU 3 (PID 11343)，正常训练中
- k07: step ~6200/10000，GPU 2 (PID 11257)，正常训练中
- 两个 tmux session 均存活，无任何错误日志
- 每个任务有 4 个 dataloader worker 在 CPU 上运行

**磁盘：** `/autodl-pub` 96% (6.7T/7.0T) 但这不是工作目录。实际工作盘 `/dev/sda2` 仅用 16G/879G (2%)，空间充足，不影响训练。

**结论：** 无需重跑，实验正在正常推进。需要修复的是 cron 监控逻辑：要么让这些 run 使用 online W&B，要么让 cron 检测 sentinel 文件 / 检查进程 PID 存活而非仅依赖 W&B 云端状态。

---
