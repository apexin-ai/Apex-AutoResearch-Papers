# ssh kill duplicate qwen processes

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-duplicate-qwen-processes_20260521T182007_result.json`
- **Structured JSON:** [`47b84937669d93dd4fc7.json`](../../sessions/47/47b84937669d93dd4fc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

### Step 1: Kill 重复进程 ✅
- PID 80555, 80556, 80557, 80558 均已 SIGTERM 正常退出（无需 SIGKILL）

### Step 2: 验证已 kill ✅
- 4 个进程均已不存在

### Step 3: 原始训练进程 ⚠️
- **PID 4561 (s456 CWM 训练) 已不在运行**。最新 checkpoint 为 step 6100 / epoch 2.76，max_steps = 6633，还差 533 步未完成。最后 checkpoint 写入时间为 01:52 CST。可能是重复进程抢 GPU 3 导致 OOM 崩溃
- **PID 4271 (s123 CWM 训练) 仍在运行** ✅，已运行 20h41m

### Step 4: Checkpoint 目录 ✅ 未被污染
- 目录 `/root/autodl-tmp/checkpoints_repo_cwm_8b_s456/` 只有 5 个 checkpoint（300, 5800, 5900, 6000, 6100），时间线连续，无异常文件。你提到的 `checkpoints_qwen3_8b_cwm_repo_s456_v3` 路径不存在，重复进程未写入此目录

### Step 5: Watch 脚本 ✅
- PID 80733 仍在运行

### 需要决策
s456 训练停在 step 6100/6633（~92% 完成），需要从 checkpoint-6100 恢复训练。是否现在重启？

---
