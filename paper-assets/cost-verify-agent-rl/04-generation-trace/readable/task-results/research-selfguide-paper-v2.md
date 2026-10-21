# research selfguide paper v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_selfguide-paper-v2_20260513T192506_result.json`
- **Structured JSON:** [`e11d6a0d88c625406f9f.json`](../../sessions/e1/e11d6a0d88c625406f9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Self-Guide ALFWorld 训练配置调研

### 1. 模型
**Qwen3-1.7B（base，非 Instruct）**。论文仅对 Qwen2.5-7B 标注 "Instruct"，Qwen3 系列未标注。

### 2. SFT warm-start
**无。** 直接从预训练 checkpoint 开始 GRPO，无 SFT、无中间步骤。

### 3. Batch size
论文未明确。基于 verl-agent 框架默认配置推断：**train_data_size=16（初始状态数）× group_size=8（rollout 数）= 128 条轨迹/步**。

### 4. Reward shaping
- 环境奖励：**纯二值 0/1**（成功=1，否则=0），无 partial progress
- Self-guidance 奖励：**+0.1 / 0 / -0.1**（positive/neutral/negative），每步生成
- 总奖励：`R(τ) = R_env + λ(u) × Σ r_sg`，λ 用梯形调度（step 0-40 关闭，40-50 升温，50-70 全开，70-80 退火）

### 5. Episode max turns
**50 步**（ALFWorld）。

### 6. GRPO-only 基线 72.7%
- 训练 **100 步**，配置与 Self-Guide 相同但 λ=0
- ReAct zero-shot 仅 10.2%，GRPO 训练效果显著

### 7. Self-guidance prompt 格式
同一模型两阶段生成：先生成 SG 标签（positive/neutral/negative + reasoning），再将 SG 注入 actor prompt 后生成 action。模板要求输出两行：`Reason: ...` 和 `Label: ...`。

### 8. Training hyperparameters
| 参数 | 值 | 来源 |
|------|-----|------|
| 总训练步数 | 100 | 论文 |
| Rollout temperature | 1.0 | 论文 |
| Validation temperature | 0.4 | 论文 |
| Max prompt length | 4096 | 论文 |
| Max response length | 1024 | 论文 |
| 优势函数 | group-relative (mean_std_norm) | 论文 |
| Learning rate | 1e-6 | verl-agent 默认 |
| KL loss coef | 0.01 (low_var_kl) | verl-agent 默认 |
| Gamma | 0.95 | verl-agent 默认 |
| Clip ratio ε | 0.2 | verl-agent 默认 |
| Invalid action penalty | 0.1 | verl-agent 默认 |

### 9. 模型初始化
**直接从 Qwen3-1.7B 预训练 checkpoint 开始 GRPO。** 无任何中间步骤。

---

**对 exp_001 失败的关键启示：**
- Self-Guide 从 base 模型直接 GRPO 能到 72.7%，说明无需 SFT 也能训练
- 96% invalid action 是核心问题 — verl-agent 有 `invalid_action_penalty_coef=0.1` 惩罚机制
- group_size=8 保证每个状态有足够 rollout 做方差估计
- 50 步/episode 给了足够的探索空间

报告已保存到 `memory.md`。

---
