# monitor exp016 status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp016-status-check_20260514T145204_result.json`
- **Structured JSON:** [`4f88a15b02ed19cea37b.json`](../../sessions/4f/4f88a15b02ed19cea37b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp016 状态
- **进程**: alive — 当前 step 12/30 (40%), 已运行 50m41s, 预计剩余 ~2h07m
- **从 exp015 checkpoint step 5 恢复**, 实际新训练 steps: 6-12

### 关键指标 (step 6 → 10 趋势)

| 指标 | Step 6 | Step 7 | Step 10 |
|------|--------|--------|---------|
| success | 0% | **4.7%** | 0% |
| pass@16 | 0 | **0.5** | 0 |
| action_is_valid | 52.1% | 65.5% | 66.4% |
| action_is_effective | 86.5% | 88.8% | 90.4% |
| pg_loss | 0.0 | — | 0.0 |
| grad_norm | 0.841 | — | 0.856 |
| entropy | 0.0976 | — | 0.1046 |
| ppo_kl | 1.7e-4 | — | -9.1e-5 |
| raw_reward | 0.0 | 0.0 | 0.0 |
| manager_invalid_action | 13.5% | 11.2% | 9.6% |

### 严重问题

**pg_loss 恒为 0.0** — 所有 step 的 rewards/advantages/returns 全部为 0。即使 step 7 有 4.7% success 和 pass@16=0.5，raw_reward 仍为 0。reward 信号完全缺失，PPO 无法学习。grad_norm ~0.85 仅来自 entropy loss。

这不是 collapse（grad_norm 没有趋近 0），而是 **reward function 没有为成功 episode 赋值**。模型在空转。

### Kill/Go 评估
**建议 Kill**。跑完 30 步也不会有任何策略提升，因为没有 reward 信号驱动梯度更新。需要先修复 reward function 让 success=True 的 episode 拿到非零 reward。

---

## Expert Trajectory 收集
- **进度**: 2165 条 (jsonl), 文件 11.5MB
- **目标**: ~3553 → 完成约 **60.9%**
- **最后写入**: 22:52 (expert_trajectories.jsonl), 22:46 (progress.json) — 可能仍在运行
- **PID 状态**: 无法确认（pipe 命令被 ssh_read_only 拦截）

---

## GPU
- GPU 0: 48309 MiB / 97887 MiB (49.4%), util 0%
- GPU 1: 48835 MiB / 97887 MiB (49.9%), util 0%

GPU utilization 0% 说明当前处于 rollout generation 阶段（vLLM inference），不在 actor update 阶段。

---
