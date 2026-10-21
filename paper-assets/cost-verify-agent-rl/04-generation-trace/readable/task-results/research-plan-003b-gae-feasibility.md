# research plan 003b gae feasibility

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_003b_gae_feasibility_20260517T072927_result.json`
- **Structured JSON:** [`f5ace95e9299c3c9a2cf.json`](../../sessions/f5/f5ace95e9299c3c9a2cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集足够信息。以下是完整评估：

---

## GAE 实现可行性评估

### 1. 代码架构概要

**训练循环调用链**：
```
RayAgentTrainer.fit()
  → rollout (actor_rollout_wg.generate_sequences)
  → compute_log_prob (actor_rollout_wg.compute_log_prob)
  → [if use_critic] critic_wg.compute_values(batch) → batch["values"]
  → compute_reward
  → compute_advantage(batch, adv_estimator=...)
    ├── GAE路径: core_algos.compute_gae_advantage_return(token_level_rewards, values, response_mask, γ, λ)
    ├── GRPO路径: compute_grpo_outcome_advantage(...)
    └── step_independent overlay: assign_step_rewards → compute_step_discounted_returns → compute_grpo_step_advantage
  → actor update
  → [if use_critic] critic_wg.update_critic(batch)
```

**关键发现：verl 框架已内建完整 GAE+Critic 支持。** `AdvantageEstimator.GAE` 路径、Critic Worker、Value Loss 全部已实现。

### 2. Critic Head 实现评估

**不需要从头实现。** verl 已有完整 critic 基础设施：

| 组件 | 文件 | 状态 |
|------|------|------|
| Critic Worker | `verl/verl/workers/roles/critic.py` | ✅ 完整实现 |
| DP Critic | `verl/verl/workers/critic/dp_critic.py` | ✅ 完整实现 |
| RAGEN Critic | `ragen/workers/critic/dp_critic.py` | ✅ 已适配 |
| Value Loss | `verl/verl/trainer/ppo/core_algos.py` | ✅ `compute_value_loss` |
| GAE 计算 | `verl/verl/trainer/ppo/core_algos.py:213` | ✅ `compute_gae_advantage_return` |

**模型初始化机制**（`verl/verl/workers/roles/critic.py:78-90`）：
- 自动将 `Qwen3ForCausalLM` → `Qwen3ForTokenClassification`
- 添加 `classifier_dropout=0` 的 linear head（hidden_size → 1）
- Critic 是**独立模型**（与 actor 分离），用自己的 optimizer 训练

**需要改的**：
- 配置文件中设置 `algorithm.adv_estimator: gae` 和 `critic.enable: true`
- 提供 critic 模型路径（可以用 actor 同一 checkpoint 初始化）
- 分配 GPU 资源给 critic worker

**主要风险**：
- Critic 需要额外 GPU 显存。Qwen3-1.7B 的 TokenClassification 版本约需 ~4GB（bf16）
- 2× RTX PRO 6000 96GB 完全够用，但需规划 resource pool 分配

### 3. GAE Advantage 计算评估

**verl 的 token-level GAE 已完整实现**（`core_algos.py:213-260`）：

```python
def compute_gae_advantage_return(token_level_rewards, values, response_mask, gamma, lam):
    # 标准 GAE，per-token 计算
    # δ_t = r_t + γ*V(s_{t+1}) - V(s_t)
    # A_t = Σ(γλ)^l * δ_{t+l}
    # 通过 response_mask 处理 padding
```

**在 `compute_advantage` 函数中已接入**（`agent_trainer.py:200-208`）：
```python
if adv_estimator == AdvantageEstimator.GAE:
    if bi_level_gae:
        advantages, returns = core_algos.compute_bi_level_gae_advantage_return(...)
    else:
        advantages, returns = core_algos.compute_gae_advantage_return(
            token_level_rewards=data.batch["token_level_rewards"],
            values=data.batch["values"],
            response_mask=data.batch["response_mask"],
            gamma=gamma, lam=lam,
        )
```

**与 step_independent 模式的交互**：
- 当前 step_independent overlay 只在 `adv_estimator == GRPO` 时生效（`agent_trainer.py:272`）
- 如果用 GAE，会走标准 token-level GAE 路径
- 在 `full` context window mode 下，GAE 正常工作：每个 sample 是完整 episode 的所有 tokens
- 在 `step_independent` mode 下，每个 sample 是单个 turn 的 tokens，GAE 变为 turn 内 token-level 的 GAE。这**不是论文需要的 turn-level GAE**。

**关键问题**：论文的 "step" = agent 的一个 action turn。标准 token-level GAE 在 `full` mode 下是���理 baseline（在整个 episode 的 token sequence 上计算 GAE）。在 `step_independent` mode 下则语义变了。

**推荐**：在 `full` context window mode 下跑 GAE baseline。这是最标准的 PPO 实现方式。

**预估新增代码量**：0 行新算法代码。只需配置修改。

### 4. 替代方案：REINFORCE baseline

**与 GRPO 的本质区别**：

| 方法 | 公式 | 区别 |
|------|------|------|
| GRPO | A = (R - μ_group) / σ_group | 组内标准化 |
| REINFORCE baseline | A = R - b | 只减 baseline |
| REINFORCE++ baseline | A = (R - running_mean) / running_std | 用历史 running stats |

- `compute_grpo_outcome_advantage`：组内 normalize（减均值除标准差）
- `compute_reinforce_plus_plus_baseline_outcome_advantage`：per-prompt running mean baseline（已在 verl 中实现）
- 当 group_size = n（GRPO 的 n 次采样），GRPO 的 baseline 是同一 prompt 的其他 sample 均值

**REINFORCE baseline 和 GRPO 不完全等价**：
- GRPO 的 baseline 是同 batch 内同 prompt 的采样均值（per-batch），方差归一化
- REINFORCE baseline 通常是 running mean 或 value function 输出
- 它们数学形式不同，可以作为独立 baseline

**实现成本**：verl 已有 `REINFORCE_PLUS_PLUS_BASELINE`，配置切换即可。

**是否满足 Reviewer 要求**：部分满足。Reviewer 要的是"标准 RL baseline"，GAE+Critic 是最标准的 PPO baseline。REINFORCE++ baseline 是轻量替代。

### 5. 兼容性风险

| 风险点 | 严重性 | 说明 |
|--------|--------|------|
| Critic GPU 资源分配 | 中 | 需要在 resource pool 中为 critic 分配 GPU，可与 actor 共存（colocate） |
| `full` mode 下 multi-turn reward | 低 | Token-level rewards 已在 `full` mode 下正确赋值（episode 结束时给 reward） |
| Checkpoint 管理 | 低 | Critic checkpoint 独立保存/加载，框架已支持 |
| `step_independent` mode 下 GAE 语义 | 高 | 如果在 step_independent mode 跑 GAE，每个 sample 只是一个 turn，GAE 退化为 turn 内的 token-level TD |
| bi_level_gae | 低 | 已有实现，可作为 `full` mode 下的增强方案 |

**最大风险**：如果当前实验只支持 `step_independent` mode，切回 `full` mode 可能需要验证 rollout 逻辑是否���常工作。

### 6. 推荐方案

**推荐：在 `full` context window mode 下启用 verl 原生 GAE（γ=1.0, λ=0.95）**

理由：
1. **零新代码**：verl 已完整实现 GAE + Critic Worker + Value Loss + Checkpoint
2. **标准 PPO baseline**：完全满足 Reviewer 对 "standard RL baseline" 的要求
3. **公平对比**：`full` mode GAE vs `full` mode episode-level GRPO vs step_independent GRPO，三者使用相同 rollout 粒度

实施步骤：
1. 修改 config：`algorithm.adv_estimator: gae`，`critic.enable: true`
2. 设置 critic model path = actor model path（用同一 pretrained model 初始化 value head）
3. 分配 resource pool（actor+critic 可 colocate 在同一 GPU）
4. 设置 `gamma: 1.0`, `lam: 0.95`

**预估总工作量**：
- 代码修改：~20 行（全在 config yaml 中）
- 验证 critic 正常训练：~2-4 小时
- 完整 baseline 实验：与当前实验同等时间
- 潜在 debug（资源分配/显存）：~4-8 小时

**备选方案**（如果 GPU 显存紧张不想跑 critic）：
- 用 `REINFORCE_PLUS_PLUS_BASELINE`，配置切换一行即可
- 但说服力弱于 GAE，Reviewer 可能追问

---
