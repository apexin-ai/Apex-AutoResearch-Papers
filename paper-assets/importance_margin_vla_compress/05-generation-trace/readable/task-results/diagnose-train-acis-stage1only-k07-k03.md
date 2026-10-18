# diagnose train acis stage1only k07 k03

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_acis_stage1only_k07_k03_20260517T074151_result.json`
- **Structured JSON:** [`6d18aebc00a36cb9c4e1.json`](../../sessions/6d/6d18aebc00a36cb9c4e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：两个实验均正常运行，未失败

| 项目 | train_acis_stage1only_k07 | train_acis_stage1only_k03 |
|------|--------------------------|--------------------------|
| 进程 | PID 11257 **存活** | PID 11343 **存活** |
| 当前进度 | step 6300/10000 | step 6200/10000 |
| margin_loss | ~0.22 | ~0.08 |
| 速度 | 4.2 sps | 4.1 sps |
| GPU | cuda:2, 2872MiB | cuda:3, 2872MiB |
| tmux | session 存活 | session 存活 |

**两个实验都在正常训练中**，远超之前的"最后已知状态"（k07 从 2300→6300，k03 从 5000→6200）。日志无任何 error/traceback，checkpoint 也正常保存（step 5000 已存）。

磁盘状态：`/root/autodl-tmp` 87% (35G 剩余)，足够继续训练。`/autodl-pub` 96% 但训练不写入该分区。

另外 GPU 1 上有一个 `libero_fullft_batch64_v2` 进程（PID 14927），GPU 0 空闲。

预计完成时间：按 4.2 sps 计算，k07 剩余 ~3700 步约 15 分钟，k03 剩余 ~3800 步约 15 分钟。

---
