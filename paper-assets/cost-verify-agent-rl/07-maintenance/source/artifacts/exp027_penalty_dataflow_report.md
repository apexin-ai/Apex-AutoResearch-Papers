# invalid_action_penalty 数据流追踪报告

## 结论

**`invalid_action_penalty_coef=0.1` 已在 exp027 中生效。** 通过 step_independent overlay 路径，penalty 汇入 GRPO step advantage。代码修改已完成，新增 `reward_include_step_penalties` 选项使 penalty 也能汇入 episode-level reward。

## 完整数据流

```
AlfredTXTEnv.step(action)
  │ action_is_available = action in self.available_actions
  │ reward = 10.0 * won (binary: 0 or 10)
  │ info["action_is_valid"] = action_is_available
  ▼
EnvStateManager.step()  [es_manager.py:205-282]
  │ _execute_actions() → turn_info.update(info)  # 捕获 action_is_valid
  │ _log_env_state() → history[turn]["info"] = turn_info
  │ format_penalty=0 (exp027) → rollout_cache["penalty"] += 0
  ▼
ContextManager._build_step_independent_samples()  [ctx_manager.py:1040-1145]
  │ is_action_valid = turn.get('info', {}).get('action_is_valid', 1.0)
  │ → non_tensor_batch["is_action_valid"]
  │ → non_tensor_batch["is_terminal"]
  │ → non_tensor_batch["reward"] = 二值 episode reward
  │ → non_tensor_batch["episode_ids"]
  │ → score_tensor (二值 reward on last token) → token_level_scores
  ▼
AgentTrainer training loop  [agent_trainer.py:1506-1522]
  │ token_level_rewards = token_level_scores
  │ invalid_action_penalty_coef = getattr(config.algorithm, ..., 0.1)  ← 代码默认值
  │ reward_include_step_penalties = getattr(config.algorithm, ..., False)  ← 新增
  ▼
compute_advantage()  [agent_trainer.py:172]
  │
  ├─ [NEW] reward_include_step_penalties=True 时:
  │   _adjust_token_rewards_with_step_penalties()
  │   → token_level_rewards[i, -1] += Σ(-penalty_coef * invalid_count_per_episode)
  │
  ├─ Phase 1: GRPO outcome advantage
  │   scores = token_level_rewards.sum(-1)  ← 现在包含 penalty (如果启用)
  │   → 分组归一化 → data.batch["advantages"]
  │   (在 step_independent 模式下被 Phase 2 覆写)
  │
  └─ Phase 2: Step-independent overlay
      ├─ assign_step_rewards(): 每个 invalid action 扣 -0.1, terminal 加 episode_reward
      ├─ compute_step_discounted_returns(): γ=0.95 折扣回报
      └─ compute_grpo_step_advantage(): 按 uid=env_id 分组归一化
         → **覆写** data.batch["advantages"]  ← 最终 advantage
```

## 两条 penalty 路径

| 机制 | 配置项 | 当前值 | 作用层 | 生效状态 |
|------|--------|--------|--------|----------|
| format_penalty | `es_manager.format_penalty` | 0 | episode reward (via rollout_cache["penalty"]) | 不生效 (=0) |
| invalid_action_penalty | `algorithm.invalid_action_penalty_coef` | 0.1 (默认) | step_returns (via assign_step_rewards) | **已生效** |
| [NEW] reward_include_step_penalties | `algorithm.reward_include_step_penalties` | False (默认) | token_level_rewards (episode-level) | 需显式开启 |

## 代码修改

### 修改文件: `ragen/trainer/agent_trainer.py`

**新增函数**: `_adjust_token_rewards_with_step_penalties()` (line 149)
- 计算每个 episode 的累积 invalid action penalty
- 将 penalty 加到 token_level_rewards 的 last token
- 只修改 token_level_rewards，不修改 non_tensor_batch["reward"]（避免与 assign_step_rewards 双重计算）

**修改函数**: `compute_advantage()` (line 172)
- 新增参数 `reward_include_step_penalties=False`
- 在 Phase 1 之前调用 `_adjust_token_rewards_with_step_penalties()`

**修改调用点**:
- `_process_rollout_and_compute_advantage()` (line 922-938)
- training loop (line 1506-1522)

### 测试结果

```
8/8 新增测试通过
17/17 GiGPO 现有测试通过
```

## exp028a 配置建议

```yaml
algorithm:
  adv_estimator: grpo
  invalid_action_penalty_coef: 0.1        # 显式设置（之前靠默认值）
  reward_include_step_penalties: true      # 新功能：penalty 也汇入 episode-level reward
  # advantage_type: grpo                  # 默认值，可不设
```

### reward_include_step_penalties 的效果

对于 GRPO step_independent 模式（exp027/028a）：
- Phase 2 (step_returns) 已经包含 per-step penalty → 这是主要梯度来源
- Phase 1 (outcome advantage) 被 Phase 2 覆写，`reward_include_step_penalties` 对最终 advantage 无直接影响
- 但开启后 token_level_rewards 中的 episode reward 更准确，有利于 metrics 和日志

对于 GiGPO 模式：
- Episode-level advantage 使用 token_level_rewards → `reward_include_step_penalties=true` 使失败 episode 间产生区分
- Step-level advantage 使用 step_returns → 已有 per-step penalty
- 两个组件受益且不双重计算（因为 non_tensor_batch["reward"] 未被修改）

## 残余问题

**全合法动作的失败 episode 仍是零方差**：如果模型输出的动作都在 admissible_actions 中但任务失败，所有 step_return=0 → 零方差。penalty 只对 invalid action 生效，对 "valid but useless" 动作无帮助。可能需要额外的 shaping（如 progress reward）来解决。
