# check 14b baseline progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_14b-baseline-progress_20260522T181315_result.json`
- **Structured JSON:** [`62ffbb7c524712aa2a96.json`](../../sessions/62/62ffbb7c524712aa2a96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 模型下载（进行中）
- **下载进程** PID 200698（modelscope snapshot_download）仍在运行
- **当前进度**: 3.76 GB / ~29 GB（约 13%）
- 所有 8 个 shard 文件在 `._____temp/` 中，尚未移入主目录
- **下载速率**: 从日志看约 300 MB/min（~5 MB/s）
- **注意**: 日志显示 02:01 时从 6.1G 回落到 16M，下载发生过一次重启

### 时间估算
- 剩余 ~25 GB，按当前速率约需 **80-90 分钟**（预计 UTC 03:40 前后完成）
- 下载完成后，eval 脚本会自动启动 0-shot 和 3-shot 评估

### 并行任务
服务器上有两个后台任务都在等同一份模型下载完成：
1. **PID 201294** (`run_14b_eval.sh`) — 你关注的 baseline eval（0-shot + 3-shot）
2. **PID 200355** (`auto_train_14b.sh`, tmux session `cls14b-func-s42`) — cls QLoRA 训练 + eval

### GPU 状态
4× RTX 5090，全部空闲（0% 利用率，0 MiB 显存占用），等待下载完成。

### 结果文件
`results_14b_0shot.json` 和 `results_14b_3shot.json` 均不存在，尚未开始评估。

---
