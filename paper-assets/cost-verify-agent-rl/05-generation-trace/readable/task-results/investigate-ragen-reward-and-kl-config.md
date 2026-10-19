# investigate ragen reward and kl config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_ragen_reward_and_kl_config_20260521T160827_result.json`
- **Structured JSON:** [`42cb0c8880abc3bacf72.json`](../../sessions/42/42cb0c8880abc3bacf72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。以下是汇报：

---

## 1. Reward 计算位置

**Flow**: Env → ContextManager → RewardFn → token_level_rewards → compute_advantage

| 阶段 | 文件:行 | 说明 |
|------|---------|------|
| Env raw reward | `ragen/env/alfworld/env.py:209` | `reward = config.score * float(won)` → 10.0 成功 / 0.0 失败 |
| Score → tensor | `ragen/llm_agent/ctx_manager.py` `get_masks_and_scores()` | 用 `use_turn_scores=True` 将每 turn 的 score 放到对应 `<\|im_end\|>` 位置，存为 `rm_scores` |
| Reward function | `agent_trainer.py:1489` | `compute_reward(batch, self.reward_fn)` → `reward_tensor` |
| token_level_scores | `agent_trainer.py:1532` | `batch.batch["token_level_scores"] = reward_tensor` |
| token_level_rewards | `agent_trainer.py:1543` | `batch.batch["token_level_rewards"] = batch.batch["token_level_scores"]` （因为 `use_kl_in_reward=False`） |
| Advantage 计算 | `agent_trainer.py:1553` | `compute_advantage(data=batch, ...)` |

**建议插入点**: `agent_trainer.py` **line 1543 和 line 1553 之间** — `token_level_rewards` 已赋值，但 advantage 尚未计算。在此处对 `token_level_rewards` 做 length penalty 修改即可影响下游所有 advantage 计算。

**Step overlay 注意**: `compute_advantage()` 内部（line 271+）还有 step-independent overlay，用 `assign_step_rewards()` + `compute_step_discounted_returns()` **替换** GRPO advantage。exp029 config 未设 `advantage_mode: episode_level`，所以走 `compute_step_discounted_returns` 路径。但 overlay 只在 `episode_ids`、`is_terminal`、`reward` 都存在时激活。

---

## 2. Response Length

| 指标 | 来源 | 单位 | Seed 7 Step 9 值 |
|------|------|------|-----------------|
| `train/AlfworldSG/response_length` | `ctx_manager.py:1028` — `response_mask.sum(dim=-1).float().mean()` | **tokens** (per-rollout mean) | **8560** |
| `response_length/mean` | verl `compute_data_metrics` | **tokens** (full sequence) | **14979** |
| `response_length/max` | verl `compute_data_metrics` | **tokens** | **16377** |
| `response_length/min` | verl `compute_data_metrics` | **tokens** | **2749** |

Seed 7 在 step 9 (60%) 被 SIGTERM 杀死。response_length/mean 已接近 `max_prompt_length: 16384` 上限。

---

## 3. KL 配置

| 参数 | 值 | 来源 |
|------|----|------|
| `use_kl_loss` | `True` | config yaml → `actor_rollout_ref.actor` |
| `kl_loss_coef` | **0.01** | config yaml |
| `kl_loss_type` | `low_var_kl` | config yaml |
| `entropy_coeff` | `0.001` | config yaml |
| `use_kl_in_reward` | `False` (default) | base.yaml `kl_ctrl.kl_coef: 0.000` |

**Trainer 使用位置**: `dp_actor.py:454-462` — KL loss 作为 actor update 的额外 loss 项添加到 `policy_loss`:
```python
kld = kl_penalty(logprob=log_prob, ref_logprob=ref_log_prob, kl_penalty=self.config.kl_loss_type)
kl_loss = agg_loss(loss_mat=kld, loss_mask=response_mask, loss_agg_mode=...)
policy_loss = policy_loss + kl_loss * self.config.kl_loss_coef  # 0.01
```

Seed 7 Step 9 实际 `actor/kl_loss: 0.074`, `actor/ppo_kl: 0.0056` — KL 值不高，说明 KL penalty 0.01 未能有效约束 response length 增长。

---

## 4. 代码修改建议

**修改文件**: `ragen/trainer/agent_trainer.py`

**插入位置**: line 1543 之后、line 1553 之前（`fit_iteration` 方法中的 training loop）

**方案**:
```python
# --- Length penalty (insert after line 1543) ---
length_penalty_coef = getattr(self.config.algorithm, "response_length_penalty_coef", 0.0)
length_penalty_threshold = getattr(self.config.algorithm, "response_length_penalty_threshold", 4096)
if length_penalty_coef > 0:
    response_mask = batch.batch["response_mask"]
    resp_lengths = response_mask.sum(dim=-1)  # (batch_size,) in tokens
    excess = (resp_lengths - length_penalty_threshold).clamp(min=0)
    penalty = -length_penalty_coef * excess  # negative reward for excess length
    # Add penalty at last valid token position
    last_pos = response_mask.sum(dim=-1).long() - 1
    last_pos = last_pos.clamp(min=0)
    for i in range(batch.batch["token_level_rewards"].shape[0]):
        batch.batch["token_level_rewards"][i, last_pos[i]] += penalty[i]
```

**新增配置参数** (加到 yaml 的 `algorithm:` 下):
- `response_length_penalty_coef: 0.001` — penalty 系数（每多一个 token 扣多少 reward）
- `response_length_penalty_threshold: 4096` — 超过此 token 数才开始 penalty

**已有但未启用的替代方案**: `grpo_advantage_length_weight: True`（base.yaml:11, agent_trainer.py:1615-1620）— 按相对长度归一化 advantage。方向不同：它让长短 response 的 advantage 量级可比，但不直接惩罚长度。可作为辅助手段。

---
