# monitor exp013e early steps

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp013e-early-steps_20260514T091535_result.json`
- **Structured JSON:** [`189ae580257630a35186.json`](../../sessions/18/189ae580257630a35186.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp013e 状态报告

### 进程状态：**已死**

| 项目 | 值 |
|------|-----|
| PID 298696 | 不存在 |
| 启动时间 | 2026-05-14 17:07:58 |
| 恢复 checkpoint | exp008_grpo/global_step_5 |
| Ray object_store_memory | 30 GB (32212254720) ✅ 正确设置 |
| CUDA_VISIBLE_DEVICES | 0,1 ✅ |
| env_groups | 4, group_size=16 ✅ |

### 内存门：**未到达**

exp013e **从未执行任何训练步**。流程是：
1. 加载 checkpoint (step 5)
2. 初始 validation (step 5)
3. **崩溃** — 在第一个 training rollout 之前就死了

这与 exp013b/c/d 的崩溃模式**不同**。b/c/d 是 step 6 rollout 时 Plasma OOM；exp013e 连 step 6 都没开始。

### 死因

```
ray.exceptions.ActorUnavailableError: RPC error: Socket closed rpc_code: 14
```

**不是 Plasma OOM**。Ray actor 进程意外死亡导致 RPC socket 断开。可能原因：
- Worker 进程被 cgroup OOM killer 杀掉（系统级，不是 Plasma 层）
- vLLM worker 初始化 training rollout 时崩溃
- 日志中无 `KILLED`/`OOM`/`raylet` 关键词，Ray session logs 也已清理，无法确认根因

### Validation 指标 (step 5, checkpoint 基线)

| 指标 | 值 |
|------|-----|
| success | 0.0 |
| action_is_valid | 0.656 |
| action_is_effective | 0.973 |
| reward/mean@16 | 2.953 |
| reward/std@16 | 1.608 |
| reward/best@16 | 4.497 |
| reward/worst@16 | 0.416 |

无训练指标（pg_loss, grad_norm 等），因为训练循环从未启动。

### 结论

exp013e 在 validation → training 过渡阶段因 Ray actor 死亡而崩溃。30GB object_store 设置正确但未经受训练 rollout 的考验。需要排查 worker 死亡的根因（建议下次加 `HYDRA_FULL_ERROR=1` 并检查 `dmesg` 中的 OOM killer 记录），然后重新启动。

---
