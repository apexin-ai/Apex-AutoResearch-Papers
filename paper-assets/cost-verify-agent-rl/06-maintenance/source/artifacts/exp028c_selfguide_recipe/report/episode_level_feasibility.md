# Episode-Level 训练可行性报告

## 当前 step_independent 模式分析

### 代码位置
- **配置**: `RAGEN/config/_alfworld_exp028c_selfguide_recipe.yaml` L83: `context_window_mode: "step_independent"`
- **上下文构建**: `ragen/llm_agent/ctx_manager.py`
  - `_build_step_independent_samples()` (L1040): 训练数据构建
  - `_build_infer_step_independent_messages()` (L1487): 推理上下文构建
- **Advantage 计算**: `ragen/trainer/agent_trainer.py`
  - `compute_advantage()` (L172): 总入口
  - L272: `if context_window_mode == "step_independent" and adv_estimator == GRPO` — step overlay 分支
- **Step reward**: `ragen/trainer/step_rewards.py`
  - `assign_step_rewards()` (L14): 终止步给 episode reward，非终止步给 invalid action penalty
  - `compute_step_discounted_returns()` (L49): 反向折扣 R_t = r_t + gamma * R_{t+1}
- **Step advantage**: `ragen/trainer/core_algos.py`
  - `compute_grpo_step_advantage()` (L194): GRPO 组内归一化 step returns

### 工作原理
1. 每个 episode (50 steps) 被切成独立的 (prompt, response) 对，`history_length=2` 意味着每个 step 只看最近 2 步上下文
2. 128 episodes → ~3200 个训练样本（每个 episode ~25 个 response turn）
3. Advantage 分两阶段：先算标准 GRPO outcome advantage（被后续覆盖），再用 step-level overlay 替换为折扣 returns 的 GRPO 归一化

### Sequence Length
- 每个 step 样本: system (~300 tokens) + 2 turns context (~600 tokens) + response (~200 tokens) ≈ **~1100 tokens**
- 远低于 max_model_len=8192

### 信用分配问题
gamma=0.95, 50 steps → gamma^49 ≈ 0.077。step 0 的折扣 return 只有终止奖励的 7.7%。**早期步骤的梯度信号极弱**，这是切换到 episode-level 的核心动机。

## 切换方案

### 方案 A: 改一个配置参数（最小改动）

```yaml
agent_proxy:
  context_window_mode: "full"  # 从 "step_independent" 改为 "full"
  # 删除或保留 step_independent_history_length（full 模式不用）
```

**改动量: 1 行 YAML**。代码零改动。

`context_window_mode` 可选值:
- `"full"` — 整个 episode 作为一个训练样本（base.yaml 默认值）
- `"step_independent"` — 每步独立训练样本
- `"single_turn"` — 单步单独训练
- `"limited_multi_turn"` — 有限多步

"full" 模式的代码路径已存在且在 exp001-exp015 中被使用过（当时 max_turn=30）。

### 数据流变化

| 阶段 | step_independent | full |
|------|-----------------|------|
| 训练数据构建 | `_build_step_independent_samples()` | `_build_samples_full()` |
| 推理上下文 | 最近 2 步 | 全部历史（截断到 max_prompt_length） |
| 样本数/batch | ~3200 (steps) | 128 (episodes) |
| Advantage | step-level GRPO + discounted returns | episode-level GRPO outcome advantage |
| 每 token 梯度 | 各 step 不同(折扣) | 同一 episode 内所有 token 相同 |

### 必须同步调整的配置

```yaml
agent_proxy:
  context_window_mode: "full"
  max_prompt_length: 16384    # 从 4096 升高，否则 _apply_max_length 会截断长 episode

actor_rollout_ref:
  rollout:
    max_model_len: 16384      # 从 8192 升高，vLLM 推理时需要容纳全历史
    gpu_memory_utilization: 0.5  # 从 0.4 提高，KV cache 需要更多显存
    max_num_batched_tokens: 16384  # 匹配 max_model_len

ppo_mini_batch_size: 32       # 从 128 降低，128 samples 不能用 128 的 mini_batch
```

**关键点**: `_apply_max_length()` (ctx_manager.py L482) 对训练和推理数据都做 token 截断，上限为 `max_prompt_length`。如果不提高，50 turn episode 会被截断到最后 ~10 turns，丧失 "full episode" 的意义。

### Advantage 在 full 模式下如何工作
`compute_advantage()` L210-234:
1. `compute_grpo_outcome_advantage()` 计算 `scores = token_level_rewards.sum(dim=-1)` → episode total reward
2. 组内归一化: `(score - group_mean) / (group_std + eps)`
3. 广播到所有 response tokens: `scores.unsqueeze(-1) * response_mask`
4. **不进入** step_independent overlay (L272 的 if 分支被跳过)

所有 token 共享同一个 advantage 值 — 这正是 Self-Guide/verl-agent 的做法。

## 显存估算

### 当前使用
```
GPU 0: 19729 MiB / 97887 MiB (20.2%)
GPU 1: 19729 MiB / 97887 MiB (20.2%)
```
- 2x RTX PRO 6000 Blackwell, 每卡 98GB
- 当前 vLLM gpu_memory_utilization=0.4 → ~39GB 被 vLLM 预留
- 训练 + vLLM 共占 ~20GB → 大量空闲

### Full Episode 序列长度估算
AlfWorld 每 turn:
- User (env observation): ~50-200 tokens
- Assistant (think + action): ~100-300 tokens
- 每 turn 合计: ~200-400 tokens

| 场景 | 估算 seq length |
|------|----------------|
| 10 turns (快速完成) | ~3000 tokens |
| 30 turns (中等) | ~9000 tokens |
| 50 turns (满步) | ~15000 tokens |
| System prompt | ~300 tokens |

**保守估计**: 50 turn 满步 episode ≈ **12000-16000 tokens**

### 显存影响分析

| 组件 | step_independent (当前) | full episode |
|------|------------------------|--------------|
| vLLM KV cache | max_model_len=8192, 0.4 ratio | 需要 max_model_len >= 16384, 0.5 ratio |
| 训练 seq length | ~1100 tokens/sample | ~12000-16000 tokens/sample |
| 训练 batch 维度 | ~3200 samples x 1100 tokens | 128 samples x 15000 tokens |
| microbatch (per GPU) | 1 sample x ~1100 tokens | 1 sample x ~15000 tokens |

**Activation 内存估算** (Qwen 2.5 3B, FSDP 2-GPU, microbatch=1):
- 当前 (1100 tokens): ~2-4 GB activations per GPU
- Full (15000 tokens): ~25-40 GB activations per GPU (flash attention 下近似线性缩放)
- Model params + optimizer (FSDP): ~12 GB per GPU
- vLLM (0.5 ratio): ~49 GB per GPU

**总估算**: 12 + 35 + 49 = ~96 GB per GPU → **接近极限但大概率可行**

如果 OOM:
1. 降低 gpu_memory_utilization 到 0.45
2. 使用 gradient checkpointing (如果 verl 支持)
3. 减少 env_groups 降低 vLLM 推理 batch

### vLLM 推理阶段
推理时每 turn 单独生成，context 逐步增长。Turn 50 时 context ≈ 15000 tokens + response_length 1024 ≈ 16024。
- 需要 max_model_len >= 16384
- KV cache 占用增加 ~2x

## 风险和 Tradeoffs

### 训练速度
- **单 step 耗时**: 15000 tokens vs 1100 tokens → 前向/反向慢 ~10-14x
- **样本数**: 128 vs 3200 → 少 25x
- **总计算量/step**: 128 x 15000 vs 3200 x 1100 ≈ 1.92M vs 3.52M tokens → **Full 模式 token 数略少**
- **但**: padding 和 variable-length 序列降低 GPU 利用率；vLLM 推理时间也受 context 增长影响
- **实际估计**: 每个训练 step 耗时可能相近或慢 1.5-2x（推理阶段更慢，训练阶段略快）

### 稳定性
- Episode-level advantage 信号更粗粒度 — 所有 token 同一 advantage，无法区分"好步骤"和"坏步骤"
- 但 GRPO 的 group normalization 提供了基线减法，不同 episode 的对比仍然有效
- Self-Guide 论文验证了此方法在 AlfWorld 上有效

### 兼容性
- `use_turn_scores: True` 在 full 模式下仍有效 — 将每 turn reward 放在对应 EOS token 位置
- `collapse_detection.multi_turn_enabled: false` (当前已关闭)，full 模式无冲突
- `ppo_mini_batch_size` 需要调整（128 samples 无法用 128 的 mini_batch_size）

### 潜在问题
1. **Padding waste**: 快速完成的 episode (10 turns, ~3K tokens) 和满步 episode (50 turns, ~15K tokens) 在同一 batch 中，短序列大量 padding
2. **Long context gradient**: 虽然 Qwen 2.5 3B 支持 32K 上下文，但训练时 15K token 序列的梯度传播可能不如短序列稳定
3. **vLLM 推理减速**: 晚期 turn (turn 40-50) 的 KV cache 很长，推理速度显著下降

## 与 Self-Guide / verl-agent 的关系

- **RAGEN 不是 verl-agent 的 fork**。RAGEN 基于 verl (base RL library) 构建，是独立框架
- GiGPO 代码从 verl-agent 移植 (`core_algos.py` L251: "Adapted from verl-agent")
- AlfWorld 环境和 reward scheme 对齐了 verl-agent (`env/alfworld/env.py` L6: "Modified to match verl-agent")
- verl-agent 的 episode-level 训练在概念上等同于 RAGEN 的 `context_window_mode: "full"` + GRPO
- **不能直接复用 verl-agent 代码**，但 RAGEN 的 "full" 模式已经实现了等价功能

## 建议

### 推荐方案: 两阶段验证

**Phase 1: 中等长度测试 (max_prompt_length=8192)**
```yaml
agent_proxy:
  context_window_mode: "full"
  max_prompt_length: 8192       # 容纳 ~20-25 turns

actor_rollout_ref:
  rollout:
    max_model_len: 12288        # 保守值
    gpu_memory_utilization: 0.45
    max_num_batched_tokens: 12288

ppo_mini_batch_size: 32

es_manager:
  train:
    env_groups: 8               # 从 16 减半，降低显存压力
    group_size: 8
```
- 50 turn episode 会被截断到最后 ~20-25 turns，但已比 h=2 好很多
- 显存更安全
- 验证 full 模式训练管线是否正常

**Phase 2: 完整 episode (max_prompt_length=16384)**
- Phase 1 确认无 OOM 和管线问题后提高
- 或者结合 gradient checkpointing

### 备选方案: 折中 — 增大 step_independent history

不切换模式，只增加 history_length:
```yaml
agent_proxy:
  context_window_mode: "step_independent"
  step_independent_history_length: 10  # 从 2 提到 10
  max_prompt_length: 8192
```
- 优点: 改动最小，保留 step-level advantage，显存增加可控
- 缺点: 仍然切断上下文，不是真正的 episode-level 训练，不匹配 Self-Guide 方法论

### 不推荐: 直接跳到 max_prompt_length=32768
- 显存风险高，如果 OOM 需要反复调试
