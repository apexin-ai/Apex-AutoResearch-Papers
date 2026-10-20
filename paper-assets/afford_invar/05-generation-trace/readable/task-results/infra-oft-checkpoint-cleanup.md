# infra oft checkpoint cleanup

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_oft-checkpoint-cleanup_20260520T001936_result.json`
- **Structured JSON:** [`f791bcc0132194ffc34e.json`](../../sessions/f7/f791bcc0132194ffc34e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 清理结果
- **删除**: `--1500_chkpt` 和 `--2000_chkpt`，释放 **~30GB** (172G → 156G used)
- **保留**: `--2500_chkpt` 和 `--3000_chkpt`（各 15GB）
- **磁盘**: 350G 总量，156G 已用，**195G 可用（45%）**

### Transfer v2 checkpoint
- 3 个 checkpoint（500/1000/1500），各 **756MB**（只存 LoRA，不是 merged），无需清理

### 自动清理
- 清理脚本: `/root/autodl-tmp/afford_invar/cleanup_old_checkpoints.sh`（保留最新 2 个）
- 后台守护进程已启动（PID 127525，每 5 分钟执行一次）
- crontab 不可用，改用 nohup 后台循环

### ⚠️ OFT baseline 已崩溃
日志尾部显示 `EADDRINUSE: port 29503` — 训练进程已停止，不会再产生新 checkpoint。如需恢复训练，需要先释放端口或换一个端口。

---
