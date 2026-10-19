# diagnose exp020b final state

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp020b-final-state_20260515T005652_result.json`
- **Structured JSON:** [`d1d0a75cd07187aeecb8.json`](../../sessions/d1/d1d0a75cd07187aeecb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp020b GRPO 训练中间报告

### 训练状态：仍在运行（22/30 步，73%）

- PID 385982 活跃
- GPU 0/1 各占 ~40GB，利用率 0%（正在做 rollout/env 交互）
- 预计剩余 ~1.1h（平均 7 min/step）
- 最新 checkpoint: step 20，无 step 25/30

### 关键指标（step 1-20）

| Step | TrainSuc% | Entropy | PG_Loss | PPO_KL | GradNorm | pass@16 |
|-----:|----------:|--------:|--------:|-------:|---------:|--------:|
| 1 | 18.75 | 0.1070 | 0.0001 | 0.0001 | 2.78 | 0.75 |
| 2 | 7.81 | 0.0802 | 0.0002 | 0.0001 | 1.41 | 0.50 |
| 3 | 3.12 | 0.0979 | -0.0000 | 0.0007 | 1.57 | 0.25 |
| 4 | 1.56 | 0.0787 | -0.0000 | 0.0004 | 0.89 | 0.25 |
| 5 | 4.69 | 0.1062 | -0.0001 | 0.0019 | 1.85 | 0.50 |
| 6 | **0.00** | 0.0876 | 0.0000 | 0.0011 | 0.80 | 0.00 |
| 7 | 1.56 | 0.0927 | -0.0000 | 0.0008 | 1.54 | 0.25 |
| 8 | 10.94 | 0.0881 | 0.0000 | 0.0009 | 2.76 | 0.75 |
| 9 | 17.19 | 0.0906 | -0.0006 | 0.0034 | 2.72 | 1.00 |
| 10 | 18.75 | 0.0847 | -0.0008 | 0.0035 | 2.52 | 0.50 |
| 11 | 14.06 | 0.0784 | -0.0002 | 0.0023 | 2.42 | 0.50 |
| 12 | 14.06 | 0.0681 | 0.0000 | 0.0020 | 3.28 | 1.00 |
| 13 | 12.50 | 0.0728 | 0.0001 | 0.0018 | 2.24 | 0.50 |
| **14** | **28.12** | 0.0762 | -0.0000 | 0.0016 | 3.42 | 0.75 |
| 15 | 1.56 | 0.0733 | -0.0000 | 0.0016 | 1.95 | 0.25 |
| 16 | 14.06 | 0.0750 | -0.0000 | 0.0016 | 3.62 | 0.75 |
| 17 | 10.94 | 0.0548 | 0.0005 | 0.0078 | 1.79 | 0.75 |
| 18 | **0.00** | 0.0451 | 0.0000 | 0.0112 | 1.47 | 0.00 |
| 19 | 1.56 | 0.0474 | -0.0001 | 0.0096 | 2.33 | 0.25 |
| 20 | 12.50 | 0.0450 | -0.0007 | 0.0092 | 5.58 | 1.00 |

**Val success**: 0% throughout（step 0 和 step 20 均为 0.0）

**Critic/score/mean**: step 20 = 1.25（总分 10）

### 趋势分析

- **Train success**: 极度不稳定，无上升趋势。step 1 的 18.75% 是 SFT checkpoint 初始水平，GRPO 训练后在 0%-28% 之间剧烈波动，后半程（step 17-20）明显恶化
- **Val success**: 始终为 0%，模型在验证集上完全无法完成任务
- **Entropy**: 从 0.107 → 0.045，坍缩 58%，模型行为多样性严重丧失
- **PPO KL**: 从 0.0001 → 0.0092，增长 100 倍，策略偏移严重
- **Grad norm**: step 20 飙升到 5.58，训练不稳定

### Checkpoint 可用性

| Checkpoint | 状态 |
|-----------|------|
| global_step_5 | 存在（空目录？仅 10 bytes） |
| global_step_10 | 存在 |
| global_step_15 | 存在 |
| global_step_20 | 存在 |
| global_step_25 | 不存在（尚未到达） |
| global_step_30 | 不存在（尚未到达） |

### 结论：**Negative**

GRPO 训练从 SFT checkpoint 出发不仅没有提升，反而**退化**了 SFT 已有的能力：
1. SFT 初始 train success 18.75% → GRPO 后期 0-12.5%
2. Val success 始终 0%，无泛化能力
3. Entropy 坍缩 + KL 飙升 = 典型的 reward hacking / policy collapse 模式

训练还在跑（剩余 step 22-30），但根据当前趋势，最终 8 步不太可能逆转。建议：
- 训练完成后可以不用期待结果改善
- 如需继续探索 GRPO，需要调整 KL 惩罚系数、entropy bonus、或 reward shaping

---
