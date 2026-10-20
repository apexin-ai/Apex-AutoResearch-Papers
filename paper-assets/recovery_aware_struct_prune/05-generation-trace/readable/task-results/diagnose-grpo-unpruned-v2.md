# diagnose grpo unpruned v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_unpruned_v2_20260516T015949_result.json`
- **Structured JSON:** [`02ca7ba51ca0f90c7fe5.json`](../../sessions/02/02ca7ba51ca0f90c7fe5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 根因

**实验没有失败，PID 75381 仍在 cuda:1 上正常运行（83248MiB 显存，2% GPU-Util 表示正处于 checkpoint 写入或 data loading 阶段）。** Cron 监控误判。

### 2. 详细证据

**进程存活**：
```
GPU 1: PID 75381, 83248MiB / 97887MiB, 2% util
```

**训练正常推进**：已完成 20/100 steps，4 个 checkpoint 已保存（step 5, 10, 15, 20），最新 checkpoint-20 写入时间 10:00:21。

**W&B 已连接**：
```
wandb: Syncing run grpo_unpruned_v2
wandb: Run data is saved locally in /root/recovery_aware_struct_prune/wandb/run-20260516_094902-nhsx0bt2
```

**训练指标（step 20）**：reward=0.552, loss=0.024, kl=0.0046, step_time≈21s

**Cron 误判可能原因**：监控可能在检查原始 PID 74579（wandb credentials 失败后已死亡），而非重启后的 PID 75381。或者监控的 W&B metrics 查询窗口太短——前 10 分钟模型加载+前几步训练还没产出 W&B log point。

### 3. 是否可重试

**不需要重试，实验正在运行。** 需要的是修正 cron 监控状态为 running。

### 4. 需要关注的风险

**磁盘空间告急**：数据盘 93% 已用（20GB 剩余）。每个 checkpoint 约 33GB（15GB model + 18GB optimizer）。当前 4 个 checkpoint 已占 ~132GB。save_steps=5，还需保存 16 个 checkpoint（step 25-100），**磁盘一定会满**。

建议：
- 立即将 cron 监控状态修正为 running
- 减少 checkpoint 保留数量（如 `save_total_limit=2`），或增大 `save_steps` 到 20-25
- 清理旧 checkpoint 释放空间，否则后续写入会因磁盘满而失败（类似之前 v7 的问题）

---
