# ops fix twostage network

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_twostage_network_20260516T042516_result.json`
- **Structured JSON:** [`f54058b5cd083e40478a.json`](../../sessions/f5/f54058b5cd083e40478a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复结果

| 项 | 状态 |
|---|---|
| 原卡死进程 133659 | KILLED |
| 实际运行进程 | **PID 136367**（tmux 启动于 12:28，已含 network_turbo + WANDB_MODE=offline） |
| 训练进度 | Stage 1 step 600/10000，sps=4.4，margin_loss≈0.14 |
| GPU 1 显存 | 3371 MiB（正在使用） |
| Registry | 已更新（pid=136367） |

**说明**：上一个 worker 描述的需重启情况已在 12:28 由 tmux session 自行修复（`mvp_imm_anchor_v8_1` tmux 同时启动了 v8b_twostage）。我误发起的 nohup 重启缺少 `WANDB_MODE=offline`，已因 wandb API key 错误自行退出，未影响 GPU。日志文件存在双进程写入痕迹（前部有 wandb 错误尾巴），但训练输出（tee 写入）后续正常。

---
