# check hsweep h10 seed2 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_hsweep_h10_seed2_progress_20260524T031210_result.json`
- **Structured JSON:** [`ebfda14b551fa493fe58.json`](../../sessions/eb/ebfda14b551fa493fe58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告：hsweep_h10_seed2

| 项目 | 状态 |
|------|------|
| **进程** | PID 95503 存活，已运行 3h04m |
| **GPU** | cuda:0 使用率 100%，显存 73GB/98GB |
| **当前 step** | **仍在 step 1**（尚未完成第一个训练 step） |
| **W&B metrics** | 0 个数据点（无训练 metrics 上报） |
| **Checkpoint** | 无（save_freq=5，step 5 才保存） |

### val_before_train 结果（step 0）

| 指标 | 值 |
|------|------|
| val success rate | **12.5%**（32 episodes 中 4 个成功） |
| val pass@1 | 12.5% |
| val response_length | 78.6 |
| val num_actions | 44.06 |
| val action_is_valid | 76.1% |
| val reward/mean | 0.378 |

### 判断

**正常运行中** — 进程存活、GPU 满载，但进度较慢。val_before_train 花了 ~579 秒，之后进入 step 1 的 training rollout（16 groups × 8 episodes = 128 rollouts，AlfWorld 每 episode 最多 50 actions，h=10），加上 1-GPU，单 step 耗时预计 2-3 小时。

当前已运行 ~3h，正处于 step 1 的 actor update 阶段（tmux 显示 `compute_policy_loss` 调用），说明 step 1 即将完成。

**预计 5 个 step 全部完成：~12-15 小时后**（约明天凌晨）。

---
