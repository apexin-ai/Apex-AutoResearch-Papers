# ops status check westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_westb_20260518T150944_result.json`
- **Structured JSON:** [`ef5ca9f9eeac718713e8.json`](../../sessions/ef/ef5ca9f9eeac718713e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## nvidia-smi 摘要
| GPU | 状态 | PID | 显存 | 利用率 | 温度 |
|-----|------|-----|------|--------|------|
| GPU0 | **运行中** | 806188 | 86875/97887 MiB | 99% | 79°C |
| GPU1 | **空闲** | — | 0 MiB | 0% | 32°C |

## 1.5B CKA-only GRPO (cuda:0) — W&B 8zkpr0hh
- **PID 存活**: yes (PID 806188)
- **当前 step**: **71/100** (ETA ~54min)
- **每10步 metrics 趋势**:

| Step | reward_mean | frac_reward_zero_std | loss |
|------|-------------|---------------------|------|
| 10 | 0.2194 | 0.10 | 0.01359 |
| 20 | 0.1975 | 0.25 | 0.04807 |
| 30 | 0.1519 | 0.225 | 0.05423 |
| 50 | 0.2238 | 0.10 | 0.02032 |
| 60 | 0.2300 | 0.20 | 0.06082 |
| 70 | **0.2569** | **0.125** | 0.02904 |

reward 在 step 30 触底后持续回升，step 70 达到最高 0.2569。frac_reward_zero_std 保持较低。

## 1.5B Standard GRPO (cuda:1) — W&B mm31apn0
- **PID 存活**: **no — 已完成** (23:07:40 退出，EXIT_CODE=0)
- **完成**: 100/100 steps，耗时 53min
- **模型已保存**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b`
- **关键 metrics 趋势**:

| Step | reward_mean | frac_reward_zero_std | loss |
|------|-------------|---------------------|------|
| 10 | 0.0569 | 0.325 | -0.00821 |
| 20 | 0.0919 | 0.200 | 0.00316 |
| 30 | 0.0706 | 0.175 | 0.00532 |
| 80 | 0.0944 | 0.300 | 0.00375 |
| 90 | 0.0656 | 0.325 | 0.00660 |
| 100 | **0.0844** | **0.150** | 0.01506 |

Standard GRPO reward 全程低迷 (0.05–0.09)，远低于 CKA-only。clipped_ratio 极高 (>0.95)，说明几乎所有 completion 都撞到 max_length=512 截断。

## SCP 活动
**无** rsync/scp 进程。

## tmux 会话
`scoring_ablation_v2` — 已完成（SFT gradient 训练结束，shell idle）。

---

**关键对比**: CKA-only reward_mean (0.26@step70) 约为 Standard (0.08@step100) 的 **3倍**，且 Standard 的 clipped_ratio ~97% 暗示模型几乎无法在 512 token 内完成推理。CKA-only 预计约 55 分钟后完成。

---
