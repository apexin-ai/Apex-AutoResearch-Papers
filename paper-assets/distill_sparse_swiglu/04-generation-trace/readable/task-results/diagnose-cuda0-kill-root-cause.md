# diagnose cuda0 kill root cause

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cuda0_kill_root_cause_20260515T200619_result.json`
- **Structured JSON:** [`51d580dd9f0d7877759c.json`](../../sessions/51/51d580dd9f0d7877759c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完毕。

## 根因判断：**外部终止（SIGHUP），不是 OOM**

**EXIT_CODE=129 = 128 + 1 = SIGHUP**，不是 SIGKILL（那应该是 137）。

### 排除项

| 怀疑项 | 结论 | 证据 |
|--------|------|------|
| 系统 OOM | ❌ | 921 GiB RAM 可用，dmesg 无 OOM 记录 |
| GPU OOM | ❌ | 进程稳定跑了 900 步（90.7/97.9GB），非 OOM crash |
| cgroup 内存限制 | ❌ | 当前 71.5 GiB，限额 220 GiB |
| 磁盘满 | ❌ | 根分区 47%，数据盘 3% |
| Crontab/Watchdog | ❌ | 无 crontab，无 kill 相关进程 |

### 实际原因

**SIGHUP 是 tmux session 被销毁时发送的信号。** `kill_job` 工具先发 SIGTERM（日志中打印了 "Terminated"），然后销毁 session（产生 SIGHUP，exit code 129）。

这 3 次 kill 都是 **agent-ml-research 框架或另一个 worker 显式终止了 tmux session**——很可能是为了释放 cuda:0 跑其他实验，或者 plan 被更新后重新提交。

### 3 次 kill 时间线

1. `bce_isocompute_s42.log` — 跑到 Step 500+，被 kill
2. `bce_isocompute_s42_v2.log` — 跑到 Step 900/2700，"Terminated"，EXIT_CODE=129（20:01:16Z）
3. 第三次可能在模型加载后很快被 kill（未留下足够日志）

### 当前状态

**第 4 次尝试（PID 129187）正在正常运行：**
- tmux session: `bce_isocompute_v2_s42`
- 已到 Step 250/1000，1.05s/step
- cuda:0 占用 90.7/97.9GB，GPU 利用率 100%
- 预计 ~13 分钟内完成

### 建议

不需要修 OOM/资源问题。要防止再被 kill：
- 确认没有其他 worker 或 plan 会对 `bce_isocompute_v2_s42` session 调用 `kill_job`
- 如果有多个实验要跑 cuda:0，做好排队，避免冲突

---

关于消息底部的 `submit_training_job` 请求：`plan_005_subsumption_s42` tmux session 已存在（04:20:20 创建），subsumption test 看起来已经被提交到 cuda:1 上了。我没有 `submit_training_job` 工具，如需手动执行该命令可以用 `ssh_execute` 代替。

---
