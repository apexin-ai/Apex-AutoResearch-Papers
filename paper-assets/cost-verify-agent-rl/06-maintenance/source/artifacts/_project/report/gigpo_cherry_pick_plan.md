# GiGPO 深度分析与 Cherry-pick 方案

> 日期：2026-05-15
> 基于 verl-agent commit（/root/autodl-tmp/verl-agent）和 RAGEN（/root/cost-verify-agent-rl）源码分析

---

## 1. GiGPO 算法核心差异（vs GRPO）

### 1.1 核心思想

GRPO 只有 **episode-level** 优势估计：整条轨迹的 reward 与同组其他轨迹比较，得到一个标量 advantage，该标量赋给轨迹中所有 token。

GiGPO 增加 **step-level** 优势估计：利用不同轨迹中出现的**相同环境状态（anchor state）**，对每一步的 action 进行更细粒度的 credit assignment。

**关键公式**（论文 Eq. 8）：
```
A(a_t^i) = A^E(τ_i) + ω · A^S(a_t^i)
```
- `A^E(τ_i)`：episode-level advantage（与 GRPO 相同）
- `A^S(a_t^i)`：step-level advantage（GiGPO 独有）
- `ω`：权重，默认 1.0

### 1.2 Episode-level Advantage（`episode_norm_reward`）

```python
# gigpo/core_gigpo.py L179-L230
scores = token_level_rewards.sum(dim=-1)  # episode total reward
# 按 index（prompt group）分组
for i in range(bsz):
    id2score[index[i]].append(scores[i])
# mean-std normalization
scores[i] = (scores[i] - mean) / (std + eps)   # mean_std_norm mode
scores[i] = scores[i] - mean                    # mean_norm mode (remove_std=True)
```

与 GRPO 的区别：
- 支持 `traj_index` 去重：同一 trajectory 的多个 step 只计一次 episode reward
- `compute_mean_std_cross_steps=True`（默认）：跨 steps 计算 mean/std，更稳定

### 1.3 Step-level Advantage（`step_norm_reward` + `build_step_group`）

**Step 1: Anchor State Grouping**（`build_step_group`, L82-L136）

```python
# 对每个 prompt group (index):
#   收集所有 step 的 anchor_obs（不含历史的纯环境观测）
#   按 exact match 或 similarity 分组
#   同组的 step 共享一个 step_group_uid

# 精确匹配模式（默认）：
clusters = defaultdict(list)
for obs in obs_group:
    clusters[to_hashable(obs)].append(idx)

# 相似度匹配模式（enable_similarity=True）：
# SequenceMatcher(None, a, b).ratio() >= threshold (默认 0.95)
```

**Step 2: Discounted Returns**（`compute_step_discounted_returns`, L33-L75）

```python
# 对每条 trajectory，从后向前计算折扣回报：
# R_t = r_t + gamma * R_{t+1}   (gamma=0.95 for ALFWorld)
```

**Step 3: Step-level Normalization**（`step_norm_reward`, L250-L290）

```python
# 按 step_group_uid 分组
# 组内 mean-std normalization
scores[i] = (scores[i] - group_mean) / (group_std + eps)
```

**为什么这解决了 GRPO 的问题：**

| 场景 | GRPO | GiGPO |
|------|------|-------|
| 组内所有 episode 全失败（reward=0） | advantage=0, 零梯度 | step-level advantage 仍有信号（不同步骤的折扣回报不同） |
| 组内所有 episode 全成功（reward=10） | advantage=0, 零梯度 | step-level advantage 区分好/坏的步骤 |
| 某步骤 action 在多条轨迹重复出现 | 无法区分该步骤的贡献 | anchor grouping 精确评估该 action 的价值 |

### 1.4 KL 约束

```bash
# run_alfworld.sh
actor_rollout_ref.actor.use_kl_loss=True
actor_rollout_ref.actor.kl_loss_coef=0.01           # β = 0.01
actor_rollout_ref.actor.kl_loss_type=low_var_kl      # low-variance KL estimator
algorithm.use_kl_in_reward=False                      # KL 不加入 reward，直接作为 loss term
```

vs RAGEN：
- RAGEN exp023c: `kl_loss_coef=0.5`（高 50x！）→ 过度约束
- verl-agent 用更低的 KL coef 配合 step-level advantage → 不需要强 KL 约束也能防止 collapse

### 1.5 Invalid Action Penalty

```bash
# run_alfworld.sh
actor_rollout_ref.actor.use_invalid_action_penalty=True
actor_rollout_ref.actor.invalid_action_penalty_coef=0.1   # -0.1 per invalid action
```

verl-agent 对每个 invalid action 施加 -0.1 penalty，作为 step-level reward 的一部分。这与 step-level advantage 配合：invalid action 不仅拉低 episode reward，还在 step-level 被精确定位和惩罚。

RAGEN 只有 `valid_action_bonus`（之前设 0.0），无 invalid action penalty。

---

## 2. Step-Independent Rollout 机制

### 2.1 verl-agent 的实现

```
rollout_loop.py: vanilla_multi_turn_loop()
├── for _step in range(max_steps):
│   ├── obs = envs.get_current_obs()         # 环境当前状态
│   ├── batch = preprocess_batch(obs)         # 构建模型输入
│   │   └── preprocess_single_sample():
│   │       ├── obs_text = obs['text']        # 由 env_manager.build_text_obs() 构建
│   │       ├── chat = [{"role": "user", "content": obs_text}]
│   │       └── input_ids = tokenizer.apply_chat_template(chat)
│   ├── response = actor_rollout_wg.generate(batch)   # 模型生成
│   ├── action = decode(response)
│   ├── next_obs, reward, done = envs.step(action)
│   └── store (batch, response, reward, anchor_obs) per step
└── gather_rollout_data() → concatenate all steps
```

**关键特性：每一步是独立的 (prompt, response) 对。**

env_manager 的 `build_text_obs()` 控制输入结构：

```python
# alfworld prompts:
ALFWORLD_TEMPLATE = """
You are an expert agent operating in the ALFRED Embodied Environment.
Your task is to: {task_description}
Prior to this step, you have already taken {step_count} step(s).
Below are the most recent {history_length} observations and the corresponding actions you took:
{action_history}
You are now at step {current_step} and your current observation is: {current_observation}
Your admissible actions of the current situation are: [{admissible_actions}].
...
"""
```

- `history_length` 控制包含多少历史步骤（bounded！）
- `anchor_obs` = 当前纯观测（不含历史、不含 prompt 框架），用于 GiGPO step grouping

### 2.2 RAGEN 的实现

```
ctx_manager.py: ContextManager (72KB)
├── 全历史拼接模式（context_window_mode="full"）
│   ├── System prompt + User Turn 1 + Assistant Turn 1 + User Turn 2 + ...
│   └── 所有历史 turn 拼接为一条长 sequence
├── context 随 step 线性增长
│   └── 50 步 ALFWorld → ~25K tokens（超出 2048 max_response_length）
└── 导致：
    ├── 后期步骤 context 截断/OOM
    ├── 早期步骤的 token 被 padding/masking 大量浪费
    └── GRPO advantage 在超长 sequence 上稀释
```

### 2.3 核心差异对比

| 维度 | RAGEN (full-history) | verl-agent (step-independent) |
|------|---------------------|------------------------------|
| **每步 context 长度** | O(step_count × avg_turn_len) | O(history_length × avg_turn_len)，常数 |
| **30 步时 context** | ~15K-25K tokens | ~2-3K tokens |
| **训练 sample 数** | 1 sample/episode（全拼接） | max_steps samples/episode（每步一个） |
| **GRPO 分组** | 按 episode 分（N=group_size） | 按 episode 分 + 按 step 分（N=group_size × overlapping_steps） |
| **anchor 状态** | 不存在 | 每步记录纯环境观测 |
| **token 效率** | 大量 padding/重复 | 每步 payload 密集 |

**这是 RAGEN 失败而 verl-agent 成功的最关键差异。** RAGEN 的全历史拼接导致：
1. 后期步骤 context 爆炸，信噪比极低
2. 每个 episode 只产生 1 个训练 sample → GRPO 学习信号稀疏
3. 无法做 step-level credit assignment

---

## 3. RAGEN vs verl-agent 完整对比表

| 维度 | RAGEN | verl-agent | 影响 |
|------|-------|-----------|------|
| **Framework** | verl 0.6.1 submodule | verl ~0.7+ | API 差异 |
| **vLLM** | 0.8.2 | 0.11.0 | 巨大版本跳跃 |
| **RL Algorithm** | GRPO（episode-only） | GiGPO（episode + step） | 核心差异 |
| **Rollout** | 全历史拼接 | Step-independent | 核心差异 |
| **Context Size** | O(steps) | O(1) bounded | 效率 |
| **Samples/Episode** | 1 | max_steps | 数据效率 |
| **Action Tag** | `<answer>` | `<action>` | 格式差异 |
| **Prompt** | System/User/Assistant 多轮 | 单条 User message | 格式差异 |
| **Reward** | 10.0 × won | 10.0 × won + (-0.1) × invalid | 信号差异 |
| **KL coef** | 0.5 | 0.01 | 50x 差异 |
| **LR** | 5e-7 | 1e-6 | 2x 差异 |
| **Group size** | 4 | 8 | 2x 差异 |
| **Collapse detection** | ✅ (核心特性) | ❌ | RAGEN 独有 |
| **Rollout filter** | ✅ (top_p/top_k) | ✅ (filter_groups) | 不同实现 |
| **Async rollout** | ❌ | ✅ (asyncio) | 性能差异 |
| **Memory module** | ctx_manager 内置 | SimpleMemory/SearchMemory | 不同抽象 |

---

## 4. Cherry-pick 方案

### 4.1 策略：最小侵入性移植

保留 RAGEN 框架整体架构，只移植 GiGPO 核心算法 + 改造 rollout 为 step-independent 模式。

### 4.2 模块清单

#### Module 1: GiGPO 算法核心（优先级 P0）

| 文件 | 动作 | 行数 | 说明 |
|------|------|------|------|
| `ragen/trainer/gigpo_algos.py` | **新建** | ~300 | 从 `gigpo/core_gigpo.py` 移植，函数签名适配 RAGEN DataProto |
| `ragen/trainer/core_algos.py` | **修改** | +20 | 添加 `compute_gigpo_outcome_advantage` 调用入口 |
| `ragen/trainer/agent_trainer.py` | **修改** | +30 | 添加 GiGPO 作为 advantage estimator 选项 |

需移植的函数：
```
compute_gigpo_outcome_advantage()  # 主入口
episode_norm_reward()              # episode-level advantage
step_norm_reward()                 # step-level advantage
build_step_group()                 # anchor state grouping
compute_step_discounted_returns()  # 折扣回报
to_hashable()                     # 辅助函数
are_similar()                     # 相似度比较
```

**适配点：**
- verl-agent 用 `batch.non_tensor_batch['anchor_obs']` 和 `batch.non_tensor_batch['traj_uid']` → RAGEN 需添加这些字段
- verl-agent 的 `step_rewards` 是 per-step scalar tensor → RAGEN 当前只有 episode-level reward

#### Module 2: Step-Independent Rollout（优先级 P0）

| 文件 | 动作 | 行数 | 说明 |
|------|------|------|------|
| `ragen/llm_agent/ctx_manager.py` | **修改** | +150 | 添加 `step_independent` context mode |
| `ragen/llm_agent/agent_proxy.py` | **修改** | +50 | 支持 per-step sample 收集 |
| `ragen/llm_agent/es_manager.py` | **修改** | +30 | 添加 `anchor_obs` 记录 |

核心改动：
```python
# ctx_manager.py 新增 step_independent 模式
if context_window_mode == "step_independent":
    # 每步构建独立 prompt：
    # 1. system prompt
    # 2. 最近 N 步历史（bounded by history_length）
    # 3. 当前观测 + admissible actions
    # 4. 生成指令
    # → 输出为独立的 (prompt, response) pair
    pass
```

**关键设计决策：**
- 不改 env.py（环境逻辑不变）
- 在 ctx_manager 层面做 step-independent → 复用 RAGEN 所有下游逻辑
- `anchor_obs` = env.render_cache（当前观测，不含格式化）

#### Module 3: 数据管道扩展（优先级 P0）

| 文件 | 动作 | 行数 | 说明 |
|------|------|------|------|
| `ragen/env/alfworld/env.py` | **修改** | +10 | step() 返回 anchor_obs |
| Config YAML | **修改** | +15 | 添加 GiGPO 相关配置 |

```yaml
# _alfworld_exp025_gigpo.yaml 新增配置
algorithm:
  adv_estimator: gigpo
  gamma: 0.95
  gigpo:
    step_advantage_w: 1.0
    mode: mean_std_norm
    enable_similarity: false
    similarity_thresh: 0.95
agent_proxy:
  context_window_mode: step_independent
  history_length: 5
actor_rollout_ref:
  actor:
    kl_loss_coef: 0.01
    kl_loss_type: low_var_kl
    use_invalid_action_penalty: true
    invalid_action_penalty_coef: 0.1
```

#### Module 4: Invalid Action Penalty（优先级 P1）

| 文件 | 动作 | 行数 | 说明 |
|------|------|------|------|
| `ragen/trainer/agent_trainer.py` | **修改** | +20 | step reward 中加入 invalid action penalty |
| `ragen/env/alfworld/env.py` | **修改** | +5 | step() info 中标记 is_action_valid |

### 4.3 工程量估计

| 模块 | 新增行数 | 修改行数 | 文件数 | 复杂度 |
|------|---------|---------|--------|--------|
| GiGPO 算法 | 300 | 50 | 3 | 低（直接移植） |
| Step-independent rollout | 150 | 80 | 3 | **高**（ctx_manager 改造） |
| 数据管道 | 0 | 25 | 2 | 低 |
| Invalid action penalty | 0 | 25 | 2 | 低 |
| Config + 集成 | 30 | 20 | 2 | 低 |
| **合计** | **~480** | **~200** | **~8** | **中等** |

预计工期：**3-5 天**（含测试调试）

### 4.4 实施顺序

```
Phase 1（Day 1-2）: GiGPO 算法移植 + 单元测试
  ├── 1a. 移植 core_gigpo.py → ragen/trainer/gigpo_algos.py
  ├── 1b. 写单元测试验证 advantage 计算正确性
  └── 1c. 在 trainer 中注册 GiGPO estimator

Phase 2（Day 2-3）: Step-independent rollout
  ├── 2a. ctx_manager 添加 step_independent 模式
  ├── 2b. agent_proxy 支持 per-step sample
  ├── 2c. es_manager 记录 anchor_obs
  └── 2d. 验证 rollout 输出格式

Phase 3（Day 3-4）: 集成 + 数据管道
  ├── 3a. 连通 GiGPO advantage 计算
  ├── 3b. 添加 step_rewards 计算
  ├── 3c. 添加 invalid action penalty
  └── 3d. Config YAML

Phase 4（Day 4-5）: 端到端测试
  ├── 4a. Dryrun（1-2 step）验证训练循环
  ├── 4b. 短实验（10 steps）验证 advantage 值合理性
  └── 4c. 正式实验启动
```

---

## 5. 风险与建议

### 5.1 技术风险

| 风险 | 严重度 | 概率 | 缓解措施 |
|------|--------|------|----------|
| verl DataProto API 不兼容（0.6.1 vs 0.7+） | 高 | 中 | `traj_uid` 字段需确认 RAGEN 是否支持；不支持则手动添加 |
| Step-independent rollout 与 RAGEN collapse detector 不兼容 | 中 | 高 | 需适配 collapse_metrics.py 的输入格式 |
| ctx_manager 改造过于复杂 | 高 | 中 | 可考虑绕过 ctx_manager，直接在 agent_proxy 层实现新 rollout 逻辑 |
| Anchor state grouping 在 ALFWorld 效果不佳（状态空间太大，重复少） | 中 | 中 | 先用 episode-only（ω=0），确认 step-independent rollout 本身的收益 |
| Invalid action penalty 与 sparse reward 交互导致新问题 | 低 | 低 | 初始实验设 penalty=0，确认基线后再开启 |

### 5.2 建议

1. **先做 step-independent rollout，后做 GiGPO**：rollout 改造对训练效果的影响可能比算法差异更大（context 从 25K→3K tokens）。可以先用标准 GRPO + step-independent rollout 跑一个 baseline。

2. **分离验证**：
   - Exp A: GRPO + step-independent rollout → 验证 rollout 改造效果
   - Exp B: GiGPO + step-independent rollout → 验证 GiGPO 增量收益

3. **保留 RAGEN 的 collapse detector**：这是 RAGEN 的独有价值，verl-agent 没有。移植时确保 collapse_metrics.py 仍能工作。

4. **考虑直接用 verl-agent 跑 ALFWorld 作为 upper bound**：在 cherry-pick 前，先在 bjb1-17606 上直接用 verl-agent 训练 ALFWorld，确认 72.7% success 可以复现。如果复现失败，cherry-pick 的 expected value 降低。

5. **KL coef 降到 0.01-0.05**：当前 RAGEN 用 0.5 是过度约束。无论是否 cherry-pick GiGPO，KL coef 都应该大幅降低。

---

## 附录 A: verl-agent ALFWorld 完整超参数

```bash
# examples/gigpo_trainer/run_alfworld.sh
train_data_size=16          # 16 unique tasks per batch
val_data_size=128           # 128 val tasks
group_size=8                # 8 rollouts per task

model=Qwen/Qwen2.5-1.5B-Instruct
lr=1e-6
max_prompt_length=2048
max_response_length=512
ppo_mini_batch_size=256
ppo_micro_batch_size_per_gpu=32

kl_loss_coef=0.01
kl_loss_type=low_var_kl
use_kl_in_reward=False
use_invalid_action_penalty=True
invalid_action_penalty_coef=0.1

gamma=0.95
step_advantage_w=1.0
gigpo_mode=mean_std_norm

env_max_steps=50
total_epochs=150
test_freq=5
n_gpus=2
tensor_model_parallel_size=2
val_temperature=0.4
```

## 附录 B: 关键代码路径映射

| verl-agent 源文件 | RAGEN 对应文件 | cherry-pick 动作 |
|-------------------|---------------|-----------------|
| `gigpo/core_gigpo.py` | `ragen/trainer/gigpo_algos.py`（新建） | 直接移植 |
| `verl/trainer/ppo/ray_trainer.py:244-365` | `ragen/trainer/agent_trainer.py:compute_advantage()` | 添加 GiGPO case |
| `verl/trainer/ppo/ray_trainer.py:1112-1116` | `ragen/trainer/agent_trainer.py:fit()` | 添加 step_rewards 计算 |
| `agent_system/multi_turn_rollout/rollout_loop.py` | `ragen/llm_agent/ctx_manager.py` | 改造为 step-independent |
| `agent_system/environments/env_manager.py:AlfWorldEnvironmentManager` | `ragen/env/alfworld/env.py` | 添加 anchor_obs |
| `agent_system/environments/prompts/alfworld.py` | `ragen/env/alfworld/env.py:_format_observation()` | 参考 prompt 格式 |
| `agent_system/reward_manager/episode.py` | `RAGEN/train.py:DummyRewardManager` | 最小改动 |
