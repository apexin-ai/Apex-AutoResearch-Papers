# monitor precompute v5 status and train

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_precompute-v5-status-and-train_20260514T092051_result.json`
- **Structured JSON:** [`ec715605185363222b82.json`](../../sessions/ec/ec715605185363222b82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. Precompute-v5: 未运行 / 失败

- 3 个 shard 进程 (PID 180251/180400/180480) 全部已死
- `/root/autodl-tmp/crm_cache_v5/` 目录**不存在**
- precompute-v5-shard{0,1,2}.log 日志文件**不存在**
- 现有 `/root/autodl-tmp/crm_cache/` 仅包含 spatial shard0 的 2,402 samples（partial 文件），object 为空目录
- **结论：precompute-v5 从未成功启动，或启动后立即失败且未产生任何输出**

### 2. Cache 验证: N/A

precompute 未完成，无法验证。

### 3. CRM 训练: BLOCKED

- 无可用 cache，无法启动训练
- 额外问题：**bjb2 只有 1 块 RTX 4090 D**，无法做 3 路并行训练（任务描述中的 cuda:0/1/3 不适用于此机器）
- bjb1 有 4x RTX 4090（cuda:0/1/3 空闲），reconvla 占用 cuda:2

### 4. reconvla + vla-mean 状态

**reconvla (bjb1, PID 118108)**: RUNNING，已运行 9h 38m
- 模式：reconvla, benchmark: spatial, 10 rollouts/task
- 进度：**8/10 tasks 完成**，task 9 进行中 (rollout 5/10)，~85%
- 已完成 task 成绩率：60%, 100%, 0%, 30%, 10%, 10%, 90%, 0% → **均值 37.5%**
- 注：`/root/runs/` 下有一份更早的 v3 日志显示 EXIT_CODE=1（crashed with `ValueError: executing action in terminated episode`），但当前进程写入 `/root/autodl-tmp/eval_results/` 的日志正常推进中

**vla-mean (bjb2, PID 143106)**: RUNNING，已运行 6h 12m
- 模式：vla_only (baseline_mode=mean), benchmark: spatial
- 进度：**3/10 tasks 完成**，task 4 进行中 (rollout 5/10)，~35%
- 已完成 task 成绩率：70%, 100%, 0% → **均值 56.7%**

### 需要决策

1. Precompute-v5 需要重新启动，但需要先确认：用 bjb1（有 3 块空闲 GPU）还是 bjb2（只有 1 块 GPU 且被 vla-mean 占用）？
2. 训练也需要在有多 GPU 的机器上执行——bjb1 等 reconvla 完成后可以释放 cuda:2，届时 4 块 GPU 全可用。

---
