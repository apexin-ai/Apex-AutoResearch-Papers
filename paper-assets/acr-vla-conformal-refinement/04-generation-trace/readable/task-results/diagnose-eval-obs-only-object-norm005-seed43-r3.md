# diagnose eval obs only object norm005 seed43 r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm005-seed43-r3_20260517T183425_result.json`
- **Structured JSON:** [`505d6ceb257a330f377b.json`](../../sessions/50/505d6ceb257a330f377b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 失败根因：SIGHUP (exit code 129)

所有 4 个实验均以 `EXIT_CODE=129` 终止。129 = 128 + 1，即收到 **SIGHUP 信号**。没有 traceback、没有 OOM、没有 segfault，dmesg 和 syslog 均无异常记录。

**最可能原因：tmux session 被意外终止**（或 SSH 连接断开且进程未正确挂载在 tmux 下）。4 个实验同时在同一台服务器上被杀，指向同一根因。

### 输出文件状态

`eval_object_obs_only_norm005_seed43_r2.json` **不存在**。实验在完成所有 task 前被中断，未写入结果文件。

### 各实验被杀时的进度

| 实验 | 已完成 tasks | 被杀位置 |
|------|-------------|---------|
| norm005-seed43-r3 | 3/10 | task 4 (bbq_sauce) rollout 5/10 |
| norm02-k5-seed42 | 6/10 | task 7 (butter) rollout 5/10 |
| norm02-k20-seed42 | 1/10 | task 2 (cream_cheese) rollout 5/10 |
| perdof-norm02-seed45-r2 | 3/10 | task 3 之后 |

### 部分结果（被杀前已完成的 tasks）

**norm005-seed43-r3** (3 tasks): alphabet_soup 0%, cream_cheese 10%, salad_dressing 10%

**norm02-k5-seed42** (6 tasks): alphabet_soup 0%, cream_cheese 0%, salad_dressing 20%, bbq_sauce 30%, ketchup 0%, tomato_sauce 10%

**norm02-k20-seed42** (1 task): alphabet_soup 0%

**perdof-norm02-seed45-r2** (3 tasks): alphabet_soup 0%, cream_cheese 0%, salad_dressing 10%

### GPU 当前状态

cuda:1 当前被 PID 702904 占用（5613MiB），无 ECC 错误。GPU 硬件正常。

### 建议

1. **直接重跑所有 4 个实验**，不需要修代码。确保 tmux session 稳定
2. 检查 bjb1-18228 上的 tmux session 管理机制，确认是否有自动清理脚本误杀了 session
3. 当前 cuda:1 已有新进程占用，重跑前确认 GPU 资源分配

---
