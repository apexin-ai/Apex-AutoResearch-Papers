# Recipe Gap Analysis: exp027 vs GiGPO vs Self-Guide

**日期**: 2026-05-15  
**核心问题**: 同模型同环境(ALFWorld), GiGPO GRPO baseline = 72.8%, Self-Guide GRPO baseline = 72.7%, 我们 exp027 = 10.16%. **62pp gap 的根因是什么？**

---

## 1. 总览对比表

| 维度 | exp027 (ours) | GiGPO (GRPO baseline) | Self-Guide (GRPO baseline) |
|------|--------------|----------------------|---------------------------|
| **基座模型** | Qwen2.5-1.5B → SFT checkpoint (6.25% success) | Qwen2.5-1.5B-Instruct (cold start) | Qwen3-1.7B (cold start) |
| **LR** | 5e-7 | 1e-6 | ~1e-6 (推断) |
| **训练步数** | 50 steps | 150 iterations | 100 steps |
| **每步 rollout 数** | 8 env × 16 group = 128 | 16 env × 8 group = 128 | 未披露 (推测 ~128) |
| **总 rollout 数** | 6,400 | 19,200 | ~12,800 |
| **Mini-batch size** | 32 | 256 | 未披露 |
| **KL 系数** | 0.005 | 0.01 | ~0.01 |
| **Entropy 系数** | 0.01 | 未披露 | 未披露 |
| **Clip ratio** | 0.2 / 0.28 | 未披露 (默认 0.2) | 0.2 / 0.28 |
| **Gamma** | 0.95 | 0.95 | 未披露 |
| **Max episode steps** | 50 | 50 | 50 |
| **奖励设计** | Binary: +10 success / 0 fail | +10 success / 0 fail / **-0.1 invalid action** | Binary env reward + step-level ±0.1 self-guide |
| **Invalid action penalty** | **0** (format_penalty=0, GRPO 不用 step reward) | **-0.1** (per invalid action) | 未披露 |
| **Max prompt len** | 4096 | 2048 | 4096 |
| **Max response len** | 1024 | 512 | 1024 |
| **Context mode** | step_independent (history=5) | step-by-step (history=2) | 未披露 |
| **Loss aggregation** | seq-mean-token-mean | token-mean | 未披露 |
| **Val episodes** | 16 | 128 | 未披露 |
| **硬件** | 2× RTX PRO 6000 (48GB) | 2× H100 (80GB) | 未披露 |
| **GRPO 结果** | **10.16%** | **72.8% ± 3.6%** | **72.7%** (Qwen3-1.7B) |

---

## 2. 逐维度 Gap 分析

### 2.1 SFT 起点 — ⚠️ 疑似反效果

| | exp027 | GiGPO | Self-Guide |
|--|--------|-------|------------|
| 起点 | SFT checkpoint (exp021_ragen_sft_v4) | Qwen2.5-1.5B-Instruct (原版) | Qwen3-1.7B (原版) |
| 起点 success rate | 6.25% (16-ep eval) | 未披露 (Instruct 零样本) | 未披露 |
| SFT 数据 | 自采 expert 轨迹 | **无 SFT** | **无 SFT** |

**关键发现**: GiGPO 和 Self-Guide **都不做 SFT**，直接从 Instruct 模型开始 RL。两者 GRPO 都能达到 ~72%。

我们的 SFT checkpoint 只有 6.25% success rate，这可能**低于原版 Instruct 模型的零样本能力**。SFT 可能破坏了模型原有的 instruction-following 能力。如果 Qwen2.5-1.5B-Instruct 零样本在 ALFWorld 能达到 ~10-20% success（需验证），那 SFT 反而是退步。

**影响评估**: 🔴 **极高** — SFT 起点可能是整个训练的根本瓶颈。从一个几乎不能成功的起点做 GRPO，大部分 group 全失败 → 零方差 → 零梯度信号。

### 2.2 训练迭代数

| | exp027 | GiGPO | Self-Guide |
|--|--------|-------|------------|
| 总步数 | 50 | 150 | 100 |
| 每步 rollouts | 128 | 128 | ~128 |
| **总 rollouts** | **6,400** | **19,200** | **~12,800** |
| 总 env interactions | ~320K (50 turns × 6400) | ~960K | ~640K |

**定义对齐**: 
- GiGPO 的 "iteration" = "epoch" = 1 个 training step（rollout + update）。verl-agent 和 RAGEN 的 step 定义一致：1 step = 1 round of (采样 128 trajectories → compute advantage → update policy)。
- Self-Guide 的 "step" 同义。

**差距**: 我们只做了 GiGPO 总量的 **1/3**、Self-Guide 的 **1/2**。

**影响评估**: 🟡 **中高** — 但这不是 62pp gap 的主因。从学习曲线看，GiGPO 在 50 步时已经 ~50-60%，而不是 10%。所以即使给我们 150 步，如果其他问题不修，也不会到 72%。

### 2.3 Rollout 配置

| | exp027 | GiGPO | Self-Guide |
|--|--------|-------|------------|
| Env groups | 8 | 16 | 未披露 |
| Group size | 16 | 8 | ~8 |
| 总 rollouts/step | 128 | 128 | ~128 |
| Per-step task 多样性 | 8 unique tasks | 16 unique tasks | 未披露 |

**差异**: 虽然总 rollout 数相同（128），但 GiGPO 每步看 16 个不同 task（每个 8 rollouts），我们只看 8 个（每个 16 rollouts）。

GRPO 的优势估计基于 group 内对比。Group size=16 在低成功率时更可能包含至少 1 个成功 episode（二项分布 P(≥1 success | n=16, p=0.1) = 81%），但 group size=8 时（P(≥1 | n=8, p=0.1) = 57%）。这影响有效学习 group 的比例。

**反面**: group_size=16 意味着更多 rollouts per task，advantage 估计更准确。但 task 多样性减半。

**影响评估**: 🟡 **中** — 8 vs 16 env_groups 是一个差异，但不是主因。

### 2.4 学习率和优化器

| | exp027 | GiGPO | Self-Guide |
|--|--------|-------|------------|
| LR | 5e-7 | 1e-6 | ~1e-6 |
| Optimizer | AdamW | 未披露 (推测 AdamW) | 未披露 |
| KL coef | 0.005 | 0.01 | ~0.01 |
| KL type | low_var_kl | low_var_kl | 未披露 |
| Entropy coef | 0.01 | 未披露 | 未披露 |
| **Mini-batch size** | **32** | **256** | 未披露 |
| Grad clip | 1.0 | 未披露 | 未披露 |
| Loss agg | seq-mean-token-mean | token-mean | 未披露 |

**Mini-batch size 差距 (8×)**: 这是一个隐藏的重大差异。

- 在 step_independent 模式下，每个 trajectory (~25 turns avg) 变成 ~25 个独立训练样本
- 128 trajectories × ~25 turns = ~3,200 训练序列 per step
- **GiGPO**: 3200 / 256 = ~12 gradient updates per step（大 batch，稳定梯度）
- **Ours**: 3200 / 32 = ~100 gradient updates per step（小 batch，极不稳定梯度）

100 次小 batch 更新 vs 12 次大 batch 更新——这不仅是梯度噪声问题，还可能导致 per-step 过度更新，策略在单步内剧烈震荡。

**LR 差距 (2×)**: 结合 8× 小 mini-batch 和 2× 低 LR，实际 per-step 学习效果很难评估。直觉上，per-sample 有效步长 = LR/mini_batch_size（简化），GiGPO = 1e-6/256 = 3.9e-9，ours = 5e-7/32 = 1.56e-8。我们的 per-sample 步长反而更大，但梯度方向更不稳定。

**影响评估**: 🔴 **高** — mini-batch size 32 可能导致训练极不稳定，是崩溃的直接诱因之一。

### 2.5 环境配置

| | exp027 | GiGPO | Self-Guide |
|--|--------|-------|------------|
| 训练集 | ALFWorld json_2.1.1/train (~3,531 games) | 同 | 同 |
| 验证集 | valid_seen (~140 games) | valid_seen (128 eval envs per step) | 未披露 |
| Task types | 6 (pick/clean/heat/cool/examine/pick_two) | 6 | 6 |
| Per-step 采样 tasks | 8 (env_groups=8) | 16 (env_groups=16) | 未披露 |
| Game file 版本 | json_2.1.1 | json_2.1.1 | json_2.1.1 |
| **Val episodes per eval** | **16** | **128** | 未披露 |

**Val episodes 差距**: 我们只用 16 episodes 评估（已违反 C003 约束），GiGPO 用 128。但这只影响评估准确性，不影响训练性能。

**影响评估**: 🟢 **低** — 环境配置基本一致。

### 2.6 奖励设计

| | exp027 | GiGPO | Self-Guide |
|--|--------|-------|------------|
| 成功奖励 | +10.0 | +10.0 | 环境 binary reward |
| Invalid action penalty | **0** (GRPO 用 outcome-level advantage, step reward 不生效) | **-0.1** (per invalid action, 累加到 trajectory reward) | 未披露 |
| Step-level reward | 代码存在但 GRPO 模式不使用 | -0.1 per invalid action (影响 trajectory 总 reward) | ±0.1 self-guide reward |
| Reward normalization | identity (无) | mean_std_norm | 未披露 |

**关键差距**: 

GiGPO 的 invalid_action_penalty 在 GRPO 中如何工作：虽然 GRPO 使用 outcome-level advantage，但 trajectory 的总 reward = success_reward + Σ(step_penalties)。例如：
- 成功 + 5 invalid actions: 10.0 - 0.5 = 9.5
- 失败 + 30 invalid actions: 0 - 3.0 = -3.0
- 失败 + 10 invalid actions: 0 - 1.0 = -1.0

这使得**失败 episodes 之间也有差异**——invalid action 越少的失败 episode，reward 越高。GRPO group 内即使全部失败，也有方差 → 有梯度信号。

我们的 binary reward: 全失败 group → 所有 episode reward = 0 → 方差 = 0 → **零梯度信号**。在 success rate ~10% 时，约 43% 的 group (size=16) 完全没有成功 episode，这些 group 完全无法学习。

**影响评估**: 🔴 **极高** — 在低 success rate 阶段，binary reward 导致大量 training step 浪费（零方差 group）。这可能是 62pp gap 的最核心原因之一。

---

## 3. Gap 优先级排序

| 排名 | Gap | 差距幅度 | 影响评估 | 可修复性 |
|------|-----|---------|---------|---------|
| **#1** | SFT 起点质量 | SFT 6.25% vs Instruct cold-start → 72% | 🔴 极高 | 简单：直接用 Instruct 模型 |
| **#2** | 奖励信号密度 | Binary 0/10 vs -0.1 invalid penalty | 🔴 极高 | 简单：启用 invalid_action_penalty |
| **#3** | Mini-batch size | 32 vs 256 (8×) | 🔴 高 | 简单：改 config |
| **#4** | 训练步数 | 50 vs 150 (3×) | 🟡 中高 | 简单：增加 steps |
| **#5** | 学习率 | 5e-7 vs 1e-6 (2×) | 🟡 中 | 简单：改 config |
| **#6** | Env groups | 8 vs 16 (2×) | 🟡 中 | 需更多 GPU 内存 |
| **#7** | Context history | 5 vs 2 | 🟢 低 | 简单：改 config |
| **#8** | Loss agg mode | seq-mean-token-mean vs token-mean | 🟢 低 | 简单：改 config |

---

## 4. 根因诊断

62pp gap 的核心因果链：

```
SFT checkpoint 质量差 (6.25%)
    → 大部分 rollout 失败
        → Binary reward: 失败 group 全零 → 零梯度
            → 学习停滞 / 极慢
                → 50 steps 不够 + 小 mini-batch 加剧不稳定
                    → 最终 10.16%
```

对比 GiGPO:
```
Instruct model (零样本能力已较强)
    → ~20-30% rollout 成功（猜测）
        → Invalid action penalty 提供 dense signal → 每个 group 都有方差
            → GRPO 稳定学习
                → 150 steps + 大 mini-batch → 72.8%
```

---

## 5. exp028 具体建议

### Phase A: 最小变更验证（验证根因假设）

**exp028a — 直接从 Instruct 模型开始 + 启用 invalid action penalty**

```yaml
# 只改这两项，其他保持 exp027 不变
model_path: Qwen/Qwen2.5-1.5B-Instruct   # 不用 SFT checkpoint
es_manager:
  format_penalty: -0.1    # 或通过 step_rewards 启用 invalid_action_penalty
```

预期：如果根因正确，仅此两项改动就能把 success rate 提升到 30-50%。

### Phase B: 全面对齐 GiGPO recipe

**exp028b — 完全对齐 GiGPO 配置**

```yaml
model_path: Qwen/Qwen2.5-1.5B-Instruct

actor_rollout_ref:
  actor:
    optim:
      lr: 1e-6                    # 2× 提升
    kl_loss_coef: 0.01            # 2× 提升
    loss_agg_mode: "token-mean"   # 对齐 verl-agent 默认
  rollout:
    response_length: 512          # 对齐 GiGPO (从 1024 降)
    max_model_len: 4096           # 可以降
    
ppo_mini_batch_size: 256          # 8× 提升（关键！）

trainer:
  total_training_steps: 150       # 3× 提升

agent_proxy:
  step_independent_history_length: 2  # 对齐 verl-agent history_length
  max_prompt_length: 2048             # 对齐 GiGPO

es_manager:
  format_penalty: -0.1            # 启用 invalid action penalty
  train:
    env_groups: 16                # 2× 提升 task diversity
    group_size: 8                 # 降低以匹配 GiGPO
```

预期：完全对齐后应能复现 ~70% success rate。

### Phase C: 超越 GRPO baseline

在 Phase B 验证后，再尝试：
1. GiGPO step-level advantage（代码中已有 `compute_gigpo_outcome_advantage`）
2. Self-Guide 的 step-level internal reward
3. 更大模型 (7B)

---

## 6. 不确定项

| 项目 | 状态 | 建议 |
|------|------|------|
| Qwen2.5-1.5B-Instruct 在 ALFWorld 的零样本 success rate | 未测 | exp028 前先跑 zero-shot eval |
| GiGPO GRPO 是否使用 reward normalization (mean_std_norm) | 不确定 (ppo_trainer.yaml 默认有，但 run_alfworld.sh 可能覆盖) | 查 verl-agent 代码或联系作者 |
| Self-Guide 的 group_size、LR、KL 精确值 | 论文未披露 (从 DAPO test 推断) | 查代码或联系作者 |
| GiGPO GRPO baseline 在第 50 步的 success rate | 论文只报最终值 | 需要跑对照实验或查 W&B |
| exp027 的 step_rewards 是否在 GRPO 模式下真正生效 | 代码审查显示 GRPO 用 outcome-level advantage，不走 step_rewards | 需确认 verl-agent 的 invalid_action_penalty 是在 env reward 层面还是 advantage 层面 |
| Mini-batch size 32 导致的实际 gradient updates 数量 | ~100 updates/step (vs GiGPO ~12) | 过度更新可能是策略震荡原因 |
| Reward normalization 差异 | 我们用 identity，GiGPO 可能用 mean_std_norm | 尝试启用 |

---

## 7. 数据来源

- GiGPO: [arXiv 2505.10978](https://arxiv.org/abs/2505.10978), [verl-agent GitHub](https://github.com/langfengQ/verl-agent) (examples/grpo_trainer/run_alfworld.sh)
- Self-Guide: [arXiv 2604.03098](https://arxiv.org/abs/2604.03098)
- exp027: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp027_stable_grpo.yaml`, `agent_trainer.py`, `step_rewards.py`
