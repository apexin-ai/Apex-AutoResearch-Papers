# verl-agent 代码库调研报告

## 基本信息

- **仓库地址**: https://github.com/langfengQ/verl-agent
- **版本**: v0.1.0 (commit 796ed31)
- **论文**: "Group-in-Group Policy Optimization for LLM Agent Training" (arXiv:2505.10978)
- **基础框架**: veRL (Volcano Engine Reinforcement Learning for LLM)
- **许可**: Apache 2.0

## 核心架构

```
verl-agent/
├── agent_system/                    # Agent 系统核心
│   ├── environments/                # 环境管理
│   │   ├── base.py                  # EnvironmentManagerBase 基类
│   │   ├── env_manager.py           # 所有具体 EnvManager + make_envs()
│   │   ├── prompts/                 # 各环境的 prompt template
│   │   │   ├── alfworld.py
│   │   │   ├── webshop.py
│   │   │   ├── sokoban.py
│   │   │   ├── search.py
│   │   │   ├── appworld.py
│   │   │   └── gym_cards.py
│   │   └── env_package/             # 具体环境实现
│   │       ├── alfworld/            # ALFWorld（含完整 alfworld 源码 fork）
│   │       ├── webshop/
│   │       ├── sokoban/
│   │       ├── search/
│   │       ├── appworld/
│   │       └── gym_cards/
│   ├── memory/                      # Memory 系统
│   │   ├── base.py                  # BaseMemory ABC
│   │   └── memory.py               # SimpleMemory, SearchMemory
│   ├── multi_turn_rollout/          # 多轮交互 rollout
│   │   ├── rollout_loop.py          # TrajectoryCollector（核心 agent loop）
│   │   └── utils.py                 # 辅助函数
│   └── reward_manager/
│       └── episode.py               # EpisodeRewardManager
├── gigpo/
│   └── core_gigpo.py                # GiGPO 算法核心
├── verl/                            # veRL 框架（actor/critic/rollout/trainer）
│   └── trainer/ppo/ray_trainer.py   # 主训练器（集成 GiGPO）
└── examples/                        # 训练脚本和数据预处理
```

## 1. EnvironmentManager 接口

### 基类: `EnvironmentManagerBase`
**文件**: `agent_system/environments/base.py`

```python
class EnvironmentManagerBase:
    def __init__(self, envs, projection_f, config):
        self.envs = envs           # 底层向量化环境
        self.projection_f = projection_f  # text action → env action 映射函数
        self.config = config

    def reset(self, kwargs) -> Dict[str, Any]:
        """返回 {'text': List[str], 'image': ndarray/Tensor, 'anchor': Any}, infos"""

    def step(self, text_actions: List[str]):
        """返回 next_observations, rewards, dones, infos
        next_observations = {'text': ..., 'image': ..., 'anchor': ...}
        anchor: 不含历史/提示的原始观测（GiGPO step grouping 用）"""

    def build_text_obs(self) -> List[str]:
        """构建给模型的 text observation（含历史、admissible actions 等）"""

    def close(self) -> None: ...

    def success_evaluator(self, *args, **kwargs) -> Dict[str, np.ndarray]:
        """评估 episode 是否成功，默认检查 info['won']"""
```

**关键设计**: 观测字典包含三个 key：
- `text`: 经过 prompt template 格式化的完整文本（含历史）
- `image`: 多模态观测（可选）
- `anchor`: **不含历史/提示的原始观测**，用于 GiGPO 的 step grouping（同一状态下的不同 trajectory step 会被分到同组）

### ALFWorld EnvManager
**文件**: `agent_system/environments/env_manager.py:133-242`

```python
class AlfWorldEnvironmentManager(EnvironmentManagerBase):
    def __init__(self, envs, projection_f, config):
        self.memory = SimpleMemory()  # 历史记录

    def reset(self, kwargs):
        text_obs, image_obs, infos = self.envs.reset()
        self.memory.reset(batch_size=len(text_obs))
        self.extract_task(text_obs)  # 从初始观测提取任务描述
        full_text_obs = self.build_text_obs(text_obs, admissible_commands, init=True)
        return {'text': full_text_obs, 'image': image_obs, 'anchor': text_obs}, infos

    def step(self, text_actions):
        actions, valids = self.projection_f(text_actions, self.envs.get_admissible_commands)
        text_obs, image_obs, rewards, dones, infos = self.envs.step(actions)
        self.memory.store({'text_obs': self.pre_text_obs, 'action': actions})
        # ...
        return {'text': full_text_obs, 'image': image_obs, 'anchor': text_obs}, ...

    def build_text_obs(self, text_obs, admissible_actions, init=False):
        # init 时用 ALFWORLD_TEMPLATE_NO_HIS，后续用 ALFWORLD_TEMPLATE（含历史）
```

### 已有环境实现

| 环境 | EnvManager 类 | Memory | 特点 |
|------|--------------|--------|------|
| ALFWorld | `AlfWorldEnvironmentManager` | `SimpleMemory` | 文本+多模态，admissible actions |
| WebShop | `WebshopEnvironmentManager` | `SimpleMemory` | 文本，available actions |
| Sokoban | `SokobanEnvironmentManager` | `SimpleMemory` | 文本+视觉 |
| Search-R1 | `SearchEnvironmentManager` | `SearchMemory` | 检索增强 |
| GymCards | `GymCardEnvironmentManager` | 无 | 视觉，单步 |
| AppWorld | `AppWorldEnvironmentManager` | `SimpleMemory` | 代码执行 |

### 环境工厂: `make_envs(config)`
**文件**: `agent_system/environments/env_manager.py:602-699`

根据 `config.env.env_name` 字符串分派到对应的 `build_*_envs()` 和 `*EnvironmentManager`。

## 2. SimpleMemory 系统

**文件**: `agent_system/memory/memory.py`

```python
class SimpleMemory(BaseMemory):
    """按 batch 维度存储每步的 observation-action 对"""

    def reset(self, batch_size: int):
        self._data = [[] for _ in range(batch_size)]  # List[List[Dict]]

    def store(self, record: Dict[str, List[Any]]):
        """存储一步记录，record 的每个 value 长度 = batch_size
        例: {'text_obs': [obs_0, obs_1, ...], 'action': [act_0, act_1, ...]}"""
        for env_idx in range(self.batch_size):
            self._data[env_idx].append({k: record[k][env_idx] for k in self.keys})

    def fetch(self, history_length, obs_key="text_obs", action_key="action"):
        """取最近 history_length 步，格式化为:
        [Observation 1: '...', Action 1: '...']
        [Observation 2: '...', Action 2: '...']
        返回 (memory_contexts: List[str], valid_lengths: List[int])"""
```

**扩展点**:
- `store()` 和 `fetch()` 是修改历史的关键入口
- `_data[env_idx]` 可以直接访问和修改某个环境的完整历史
- `history_length` 控制滑动窗口大小（来自 `config.env.history_length`）

## 3. Prompt 系统

**文件**: `agent_system/environments/prompts/alfworld.py`

```python
ALFWORLD_TEMPLATE_NO_HIS = """
You are an expert agent operating in the ALFRED Embodied Environment.
Your current observation is: {current_observation}
Your admissible actions of the current situation are: [{admissible_actions}].

Now it's your turn to take an action.
You should first reason step-by-step about the current situation.
This reasoning process MUST be enclosed within <think> </think> tags.
Once you've finished your reasoning, you should choose an admissible action
for current step and present it within <action> </action> tags.
"""

ALFWORLD_TEMPLATE = """
You are an expert agent operating in the ALFRED Embodied Environment.
Your task is to: {task_description}
Prior to this step, you have already taken {step_count} step(s).
Below are the most recent {history_length} observations and the
corresponding actions you took: {action_history}
You are now at step {current_step} and your current observation is:
{current_observation}
Your admissible actions of the current situation are: [{admissible_actions}].
...
"""
```

**格式**: ReAct 风格 — `<think>推理</think><action>动作</action>`

## 4. Agent Loop（核心交互循环）

**文件**: `agent_system/multi_turn_rollout/rollout_loop.py`
**类**: `TrajectoryCollector`

### 主循环 `vanilla_multi_turn_loop()`

```
for _step in range(config.env.max_steps):
    1. preprocess_batch(gen_batch, obs)     → tokenize text obs
    2. actor_rollout_wg.generate_sequences() → 模型生成 response
    3. tokenizer.batch_decode(responses)     → 得到 text_actions
    4. envs.step(text_actions)               → next_obs, rewards, dones, infos
    5. 记录 episode_rewards, episode_lengths
    6. 将 step 数据追加到 total_batch_list
    7. 如果所有 env done，break
```

### 数据流关键变量

- `uid_batch`: episode group UID（同一 task 的 `group_n` 个 trajectory 共享一个 uid）
- `traj_uid`: 每条 trajectory 的唯一 ID
- `anchor_obs`: 不含历史的原始观测（存入 `non_tensor_batch['anchor_obs']`）
- `is_action_valid`: action 格式是否合法
- `rewards`: 每步环境返回的即时奖励
- `active_masks`: 标记 trajectory 是否仍然活跃

### 动态采样 `dynamic_multi_turn_loop()`
反复调用 `vanilla_multi_turn_loop()` + `filter_group_data()`，直到收集到足够的有效 trajectory-step。用于 DAPO/Dynamic GiGPO。

## 5. 训练数据格式

### RL 训练数据
**文件**: `examples/data_preprocess/prepare.py`

RL 训练的"数据"只是占位符，真正的 prompt 由 EnvManager 在 rollout 时动态构建：
```python
{"data_source": "text", "prompt": [{"role": "user", "content": ""}],
 "ability": "agent", "extra_info": {"split": "train", "index": idx}}
```
保存为 parquet。

### SFT 训练数据
**文件**: `examples/data_preprocess/multiturn.py`

多轮 SFT 格式: `{"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}`

## 6. 奖励系统

### ALFWorld 环境奖励
**文件**: `agent_system/environments/env_package/alfworld/envs.py:48-53`

```python
def compute_reward(info, multi_modal=False):
    if multi_modal:
        reward = 10.0 * float(info['won']) + float(info['goal_condition_success_rate'])
    else:
        reward = 10.0 * float(info['won'])  # 纯稀疏奖励：完成 +10，未完成 0
```

### EpisodeRewardManager
**文件**: `agent_system/reward_manager/episode.py`

将 episode 累积奖励放置到最后一个有效 response token 的位置：
```python
reward_tensor[i, valid_response_length - 1] = episode_rewards  # 或 / episode_lengths
```

### Invalid Action Penalty
**文件**: `verl/trainer/ppo/ray_trainer.py:200-222`

```python
reward_tensor[i, valid_response_length - 1] -= penalty_coef * (1 - is_action_valid)
step_rewards[i] -= penalty_coef * (1 - is_action_valid)
```

### GiGPO Step-level Reward
**文件**: `gigpo/core_gigpo.py:87-132`

`compute_step_discounted_returns()`: 将每步即时奖励转换为折扣回报 $G_t = r_t + \gamma G_{t+1}$

## 7. GiGPO 算法核心

**文件**: `gigpo/core_gigpo.py`

### 优势计算 (Eq. 3, 6, 7, 8)

```python
def compute_gigpo_outcome_advantage(...):
    # Eq. 3: Episode-level advantage（跨 trajectory 归一化）
    episode_advantages = episode_norm_reward(token_level_rewards, ...)

    # Eq. 6: Step grouping（按 anchor_obs 分组，同一状态→同组）
    step_group_uids = build_step_group(anchor_obs, index, ...)

    # Eq. 7: Step-level advantage（组内归一化）
    step_advantages = step_norm_reward(step_rewards, ..., step_group_uids, ...)

    # Eq. 8: Joint advantage
    scores = episode_advantages + step_advantage_w * step_advantages
```

### Step Grouping 机制
`build_step_group()`: 在同一 episode group (uid) 内，将 `anchor_obs` 相同的 step 聚类到同一组。支持精确匹配和模糊匹配（SequenceMatcher）。

## 8. ALFWorld 集成状态

**已完整集成**。包括：

1. **环境封装** (`env_package/alfworld/`):
   - 完整的 alfworld 源码 fork（TextWorld + AI2Thor 支持）
   - `AlfworldWorker` (Ray actor) + `AlfworldEnvs` (向量化封装)
   - 支持 `AlfredTWEnv`（文本）和 `AlfredThorEnv`（多模态）

2. **Projection 函数** (`projection.py`):
   - 从模型输出提取 `<action>...</action>` 内容
   - 验证 `<think>...</think>` 格式
   - 返回 `(actions, valids)` 用于 invalid action penalty

3. **训练脚本** (`examples/*/run_alfworld.sh`):
   - GiGPO/GRPO/PPO/DAPO/GSPO/RLOO 全部有 ALFWorld 配置
   - 默认: Qwen2.5-1.5B, 16 train batch, 8 group size, 50 max steps, 150 epochs

4. **6 种任务类型**: pick_and_place, pick_two_obj_and_place, look_at_obj_in_light, pick_heat_then_place_in_recep, pick_cool_then_place_in_recep, pick_clean_then_place_in_recep

## 9. 面向 Error Injection 的扩展点分析

### 扩展点 1: Memory.store() / Memory.fetch() — 历史截断/篡改

**位置**: `agent_system/memory/memory.py`
**方式**: 继承 `SimpleMemory`，重写 `store()` 或 `fetch()` 来注入错误历史

```python
class ErrorInjectMemory(SimpleMemory):
    def store(self, record):
        # 可以在这里修改 record 中的 obs 或 action
        super().store(record)

    def fetch(self, history_length, ...):
        contexts, lengths = super().fetch(history_length, ...)
        # 可以在这里截断、打乱、替换历史
        return modified_contexts, lengths
```

**可注入的错误类型**:
- 历史截断（减少 history_length 或删除某些步骤）
- 观测替换（将某步的 observation 替换为错误内容）
- 动作替换（将历史中的 action 替换为错误动作）
- 顺序打乱（交换历史步骤的顺序）

### 扩展点 2: build_text_obs() — Prompt 级注入

**位置**: `AlfWorldEnvironmentManager.build_text_obs()` (`env_manager.py:180-212`)
**方式**: 重写此方法，在 prompt template 中注入错误信息

可注入:
- 修改 `task_description`（任务描述错误）
- 修改 `admissible_actions`（可用动作列表错误）
- 修改 `current_observation`（当前观测错误）
- 修改 `action_history`（历史动作错误）

### 扩展点 3: EnvManager.step() — 观测/奖励篡改

**位置**: `AlfWorldEnvironmentManager.step()` (`env_manager.py:150-168`)
**方式**: 在 `self.envs.step()` 返回后、返回给 agent loop 前修改观测或奖励

```python
def step(self, text_actions):
    actions, valids = self.projection_f(...)
    text_obs, image_obs, rewards, dones, infos = self.envs.step(actions)
    # >>> 在这里可以篡改 text_obs, rewards, dones <<<
    self.memory.store(...)
    ...
```

### 扩展点 4: anchor_obs — 影响 GiGPO Step Grouping

**位置**: `env_manager.py` 中返回的 `'anchor': text_obs`
**影响**: `anchor_obs` 决定了 GiGPO 的 step grouping。修改 anchor 会影响哪些 step 被分到同一组进行 advantage 归一化。

### 扩展点 5: Projection 函数 — Action 解析篡改

**位置**: `agent_system/environments/env_package/alfworld/projection.py`
**方式**: 修改 `alfworld_projection()` 来改变 action 解析行为

### 扩展点 6: Rollout Loop — Trajectory 级 Hook

**位置**: `agent_system/multi_turn_rollout/rollout_loop.py:332-406`
**方式**: 在 `vanilla_multi_turn_loop()` 的 for 循环中添加 hook

关键插入点：
1. `preprocess_batch()` 之后 — 修改 tokenized input
2. `generate_sequences()` 之后 — 修改模型输出
3. `envs.step()` 之后 — 修改环境返回值
4. `total_batch_list[i].append()` 之前 — 修改记录的 trajectory 数据

### 扩展点 7: Reward Manager — 奖励函数修改

**位置**: `agent_system/reward_manager/episode.py` 和 `verl/trainer/ppo/ray_trainer.py:200-222`
**方式**: 自定义 reward 函数或修改 `apply_invalid_action_penalty()`

### 扩展点 8: Trajectory Logging

**现有机制**: `total_batch_list` 和 `total_infos` 包含完整的 trajectory 数据（每步的 input_ids, responses, rewards, active_masks, anchor_obs, is_action_valid 等）。这些数据在 `gather_rollout_data()` 中被转换为 `DataProto`。

**没有内置的 trajectory 持久化/replay 机制**。需要自行添加序列化逻辑。

## 10. 关键文件路径索引

| 组件 | 文件路径 |
|------|---------|
| EnvManager 基类 | `agent_system/environments/base.py` |
| 所有 EnvManager | `agent_system/environments/env_manager.py` |
| Memory 基类 | `agent_system/memory/base.py` |
| SimpleMemory | `agent_system/memory/memory.py` |
| ALFWorld prompt | `agent_system/environments/prompts/alfworld.py` |
| ALFWorld 环境封装 | `agent_system/environments/env_package/alfworld/envs.py` |
| ALFWorld projection | `agent_system/environments/env_package/alfworld/projection.py` |
| ALFWorld 配置 | `agent_system/environments/env_package/alfworld/configs/config_tw.yaml` |
| Rollout Loop | `agent_system/multi_turn_rollout/rollout_loop.py` |
| Reward Manager | `agent_system/reward_manager/episode.py` |
| GiGPO 核心 | `gigpo/core_gigpo.py` |
| 主训练器 | `verl/trainer/ppo/ray_trainer.py` |
| 训练配置 | `verl/trainer/config/ppo_trainer.yaml` |
| ALFWorld GiGPO 脚本 | `examples/gigpo_trainer/run_alfworld.sh` |
| 数据预处理 | `examples/data_preprocess/prepare.py` |

## 11. 面向 Error Injection Agent 的实施建议

### 推荐方案：继承式扩展

最小侵入的方式是：

1. **自定义 Memory**: 继承 `SimpleMemory`，重写 `fetch()` 实现历史篡改（截断、mask、乱序）
2. **自定义 EnvManager**: 继承 `AlfWorldEnvironmentManager`，重写 `build_text_obs()` 和 `step()` 实现观测/prompt 篡改
3. **在 `make_envs()` 中注册**: 添加新的 env_name（如 `alfworld_error_inject/AlfredTWEnv`）
4. **Trajectory Logger**: 在 `gather_rollout_data()` 后添加序列化钩子

### 不需要修改的部分

- GiGPO 核心算法（`core_gigpo.py`）可以直接复用
- Rollout Loop（`rollout_loop.py`）不需要修改，通过 EnvManager 接口注入
- 训练器（`ray_trainer.py`）不需要修改
- Projection 函数可以直接复用

### Plan State 表示

verl-agent **没有显式的 plan state**。Agent 的"计划"完全由 `<think>` 标签中的推理文本体现，没有结构化的 plan 表示。如果要实现 plan 修改，需要：
- 解析 `<think>` 内容提取计划步骤
- 或在 prompt 中注入错误的计划提示
