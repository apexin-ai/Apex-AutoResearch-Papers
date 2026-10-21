# diag bjb1 18228 sighup batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-18228-sighup-batch_20260517T183435_result.json`
- **Structured JSON:** [`174a759ed8d4c5ac542f.json`](../../sessions/17/174a759ed8d4c5ac542f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断信息充分。以下是诊断报告：

---

## 诊断报告：bjb1-18228 四实验 SIGHUP 失败

### 根因分析

**直接原因**：tmux server 进程被终止，向所有子进程发送 SIGHUP (signal 1)，导致 EXIT_CODE=129 (128+1)。

**排除项**：
- 服务器**未重启**（uptime 4天15小时，自5月13日启动）
- GPU**未掉卡**（nvidia-smi 正常，4块 4090 均在线）
- **非 OOM**（dmesg 为空，容器环境无 journalctl）
- **无 crontab**（crontab 命令不存在）

**最可能原因**：SeetaCloud 平台级操作（如 SSH session 清理、容器 maintenance、或平台自动超时机制）杀死了 tmux server 进程。容器环境缺乏系统级日志，无法进一步确认。另一可能性：其他 agent/session 误执行了 `tmux kill-server`。

### 实验进度（均为 10 tasks × 10 rollouts）

| 实验 | GPU | 完成进度 | 部分结果 |
|---|---|---|---|
| perdof-norm02-seed45-r2 | cuda:0 | 3/10 tasks (30%) | task1: 0%, task2: 0%, task3: 10% |
| obs-only-norm005-seed43-r3 | cuda:1 | 3.5/10 tasks (35%) | task1: 0%, task2: 10%, task3: 10%, task4进行中 |
| obs-only-norm02-k5-seed42 | cuda:2 | 7.5/10 tasks (75%) | task1-6完成(0%,0%,20%,30%,0%,10%), task8进行中 |
| obs-only-norm02-k20-seed42 | cuda:3 | 1.5/10 tasks (15%) | task1: 0%, task2进行中 |

**无可抢救结果**：JSON 输出文件仅在全部 10 个 task 完成后才写入，4个实验均未生成 JSON 文件。日志中的 per-task success rate 可手动提取，但不完整。

### 服务器当前状态

- 在线，4 GPU 正常
- GPU 0 和 GPU 2 正被两个 `openvla_eval.py` debug 进程占用（pid 698064, 699794，约 02:31 CST 启动）
- GPU 1 和 GPU 3 空闲，可立即使用
- tmux socket 存在但 server 未运行（stale socket from 23:57 CST）
- 项目代码目录 `/root/acr-vla-conformal-refinement/` 完整

### 建议

1. **需要全部重跑**，无部分结果可用
2. **防 SIGHUP 措施**：
   - 用 `nohup` + 后台运行代替纯 tmux 内前台执行（`nohup python ... > log 2>&1 &`），即使 tmux 死掉进程也能存活
   - 或在脚本中加 `trap '' HUP` 忽略 SIGHUP
   - 评估脚本改为每完成一个 task 就增量写入 JSON（而非全部完成后一次性写入），避免进度全丢
3. **当前 GPU 0 和 2 被占用**，如需全部 4 GPU 重跑，先等 debug 进程完成或手动终止

---
