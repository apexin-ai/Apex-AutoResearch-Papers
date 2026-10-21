# diagnose train smart compress m16 seed44

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_smart_compress_m16_seed44_20260519T043838_result.json`
- **Structured JSON:** [`dad44d30d31ed775d148.json`](../../sessions/da/dad44d30d31ed775d148.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：**误报（false positive）**

**训练实际正在正常运行**，cron 监控判断错误。

### 根本原因
训练以 `WANDB_MODE=offline` 启动，W&B 数据仅保存本地。cron 监控查不到在线 W&B metrics，误判为"no sentinel/W&B"，标记为失败。

### 关键证据
- 日志中 `"Starting training"` 仅出现 **1 次**（未崩溃重启）
- 日志中 **无任何 error/traceback/OOM**
- 最新日志：`step=8300/100000, loss=0.1497, sps=5.0`（12:38:50，正常推进中）
- Loss 从 1.19 稳步下降至 ~0.10，训练健康
- Checkpoint 已正常保存（step 1000/2000/.../8000）

### 服务器状态
| 项目 | 状态 |
|------|------|
| GPU 0 | RTX PRO 6000, 3366MiB/97887MiB, 66% util, 45°C, 正常 |
| GPU 1 | 另有两个 python 进程占用，95% util |
| 磁盘 | 207G/250G (83%), 剩余 44G |

### 是否需要操作
- **训练无需重试**，当前运行正常
- 如需 cron 监控正确识别此任务，需要：要么改用 `WANDB_MODE=online`，要么让监控脚本支持检测 offline W&B 或读取日志 sentinel

---
