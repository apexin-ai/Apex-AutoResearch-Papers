# monitor cwm v10 status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_cwm-v10-status-check_20260512T234911_result.json`
- **Structured JSON:** [`e67c96c4ed5dab0480e4.json`](../../sessions/e6/e67c96c4ed5dab0480e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM v10 训练状态报告

**在运行：是（但实际上是 v9 的 resume run）**

| 项目 | 值 |
|---|---|
| PID | 105205 |
| GPU | cuda:2 (RTX 5090)，21058 MiB，89% 利用率，423W |
| 进程启动时间 | 2026-05-13 07:39:16 (UTC+8) — 约 10 分钟前 |
| 训练开始时间 | 07:45:21 (加载数据/模型耗时 ~6 分钟) |
| 当前 step | **235 / 6633** (3.5%) |
| 速度 | ~7.85 s/it |
| 预计剩余 | ~13.9 小时 |

### 关键发现

该进程的命令行实际上是 **v9 的配置**：
- `--output_dir /root/autodl-tmp/checkpoints_repo_cwm_v9/`
- `--resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_v9/checkpoint-200`
- 日志写入 `/root/autodl-tmp/cwm_v9_train.log`

没有找到任何名为 v10 的日志或目录。Registry 中的 v10 实际上是 v9 代码从 checkpoint-200 resume 的训练。

### Checkpoints

`/root/autodl-tmp/checkpoints_repo_cwm_v9/` 下：
- checkpoint-100 (06:15)
- checkpoint-200 (06:40)
- checkpoint-205 (07:34) ← 当前 run 新产生

### 日志路径

- 当前 stdout: `/root/autodl-tmp/cwm_v9_train.log`
- 之前的 v9 stdout: `/tmp/repo-level-cwm-v9_stdout.log`

---
