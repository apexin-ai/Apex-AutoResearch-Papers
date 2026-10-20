# ALFWorld 数据与轨迹收集调研报告

## 1. ALFWorld 任务类型与分布

### 1.1 六种任务类型

| 编号 | 内部名称 | 显示名称 | 描述 |
|------|---------|---------|------|
| 1 | `pick_and_place` | Pick & Place | 找到物体并放到指定位置 |
| 2 | `look_at_obj_in_light` | Examine in Light | 找到物体并用灯检查 |
| 3 | `pick_clean_then_place` | Clean & Place | 找到物体→清洗→放到指定位置 |
| 4 | `pick_heat_then_place` | Heat & Place | 找到物体→加热→放到指定位置 |
| 5 | `pick_cool_then_place` | Cool & Place | 找到物体→冷却→放到指定位置 |
| 6 | `pick_two_obj_and_place` | Pick Two & Place | 找到两个同类物体并放到指定位置 |

### 1.2 数据分布（来自 ALFWorld 论文 Table 1）

| 任务类型 | Train | Valid Seen | Valid Unseen |
|---------|-------|-----------|-------------|
| Pick & Place | 790 | 35 | 24 |
| Examine in Light | 308 | 13 | 18 |
| Clean & Place | 650 | 27 | 31 |
| Heat & Place | 459 | 16 | 23 |
| Cool & Place | 533 | 25 | 21 |
| Pick Two & Place | 813 | 24 | 17 |
| **总计** | **3,553** | **140** | **134** |

- **Train**: 3,553 个任务用于训练
- **Valid Seen**: 140 个任务，使用训练中见过的房间布局
- **Valid Unseen**: 134 个任务，使用全新的房间布局
- **环境**: 120 个房间（30 厨房 + 30 卧室 + 30 浴室 + 30 客厅）
- **Max steps**: 50 步/episode

### 1.3 典型步数

论文设定 max steps = 50。根据 HuggingFace 公开数据集的统计，实际成功轨迹的步数范围为 9-51 步，平均约 17 步（取决于任务复杂度）。Pick & Place 最简单（~10 步），Pick Two & Place 最复杂（~25+ 步）。

---

## 2. 轨迹数据格式

### 2.1 ALFWorld 原生 Observation/Action 格式

**Observation** 为自然语言文本，描述当前所见：
```
You are in the middle of a room. Looking quickly around you, you see a 
cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, 
a coffeemachine 1, a countertop 3, a countertop 2, a countertop 1, 
a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, 
a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, 
a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, 
a toaster 1.

Your task is to: put a hot apple in countertop.
```

**Action** 为文本命令，从 admissible actions 中选择：
```
go to fridge 1
open fridge 1
take apple 1 from fridge 1
go to microwave 1
heat apple 1 with microwave 1
go to countertop 1
put apple 1 in/on countertop 1
```

### 2.2 Action 空间

ALFWorld 的 TextWorld 动作类型（高层）：

```python
ALF_ACTION_LIST = [
    "pass",       # 跳过
    "goto",       # go to {receptacle}
    "pick",       # take {object} from {receptacle}
    "put",        # put {object} in/on {receptacle}
    "open",       # open {receptacle}
    "close",      # close {receptacle}
    "toggle",     # toggle {object/receptacle}
    "heat",       # heat {object} with {receptacle}
    "clean",      # clean {object} with {receptacle}
    "cool",       # cool {object} with {receptacle}
    "slice",      # slice {object}
    "inventory",  # 查看背包
    "examine",    # examine {object/receptacle}
    "look",       # 环顾四周
]
```

每步环境返回 `info['admissible_commands']`（当前合法动作列表），通常 10-15 个选项。

### 2.3 verl-agent 中的轨迹存储格式

verl-agent 使用 `SimpleMemory` + `TrajectoryCollector` 管理轨迹：

**SimpleMemory 存储结构**（per environment）:
```python
# _data[env_idx] = [
#     {"text_obs": "You are in the middle...", "action": "go to fridge 1"},
#     {"text_obs": "You open the fridge...", "action": "take apple 1 from fridge 1"},
#     ...
# ]
```

**TrajectoryCollector 输出格式**（DataProto）:
```python
{
    'input_ids': tensor,           # tokenized prompt
    'responses': tensor,           # tokenized model output
    'attention_mask': tensor,      # mask
    'anchor_obs': str,             # 原始 observation（无 history），用于 GiGPO 分组
    'episode_rewards': float,      # 10.0 if won, 0.0 otherwise
    'episode_lengths': int,        # 总步数
    'is_action_valid': int,        # 1 if <action>...</action> 格式正确
    'traj_uid': str,               # 轨迹唯一标识
}
```

**Reward 计算**:
```python
reward = 10.0 * float(info['won'])  # text-only 模式：成功 +10，失败 0
```

---

## 3. 成功轨迹收集方案

### 3.1 GPT-4o Rollout 方案

**基本思路**: 用 GPT-4o 作为 agent，在 ALFWorld TextWorld 环境中 rollout，收集成功轨迹。

**方案 A：基于 verl-agent 框架改造（推荐）**

verl-agent 已有完整的 ALFWorld 环境集成（`AlfWorldEnvironmentManager`），只需：
1. 将 LLM backbone 从本地模型替换为 GPT-4o API 调用
2. 复用现有的 `SimpleMemory`、prompt template、action projection
3. 保存成功轨迹（reward > 0 的 episode）

关键改造点：
- 在 `TrajectoryCollector` 的 rollout loop 中，将 vLLM 生成替换为 OpenAI API 调用
- 使用 verl-agent 的 `ALFWORLD_TEMPLATE` 构建 prompt（含 history）
- action 提取复用 `alfworld_projection()` 函数

**方案 B：独立 rollout 脚本**

更轻量，直接调用 ALFWorld 的 gym 接口：

```python
import alfworld.agents.environment as environment
import openai
import json

def collect_trajectory(env, task_idx, client):
    obs, info = env.reset()
    trajectory = {"task": obs[0], "steps": [], "success": False}
    
    for step in range(50):
        admissible = info['admissible_commands'][0]
        
        prompt = f"""You are in an ALFWorld environment.
Observation: {obs[0]}
Admissible actions: {admissible}

Think step by step, then choose one action.
Format: Think: <reasoning>\nAct: <chosen action>"""
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256,
            temperature=0.0
        )
        
        action = parse_action(response.choices[0].message.content)
        obs, reward, done, info = env.step([action])
        
        trajectory["steps"].append({
            "observation": obs[0],
            "thought": parse_thought(response.choices[0].message.content),
            "action": action,
            "admissible_commands": admissible
        })
        
        if done[0]:
            trajectory["success"] = info['won'][0]
            break
    
    return trajectory
```

### 3.2 Prompt Template

**ReAct 原版格式**（ysymyth/ReAct）:
```
Interact with a household to solve a task. Here are two examples.
[1-2 个 in-context 示例，每种任务类型一个]

Here is the task.
> Observation: [环境描述]
Think 1: [推理]
Act 1: [动作]
Obs 1: [环境反馈]
Think 2: [推理]
Act 2: [动作]
...
```

**verl-agent 格式**（`<think>/<action>` tags）:
```
You are an expert agent operating in the ALFRED Embodied Environment. 
Your task is to: {task_description}
Prior to this step, you have already taken {step_count} step(s). 
Below are the most recent {history_length} observations and the 
corresponding actions you took: {action_history}
You are now at step {current_step} and your current observation is: 
{current_observation}
Your admissible actions of the current situation are: [{admissible_actions}].

Now it's your turn to take an action.
You should first reason step-by-step about the current situation. 
This reasoning process MUST be enclosed within <think> </think> tags. 
Once you've finished your reasoning, you should choose an admissible 
action for current step and present it within <action> </action> tags.
```

**推荐**: 对 TaxEI 项目，使用简化版 ReAct prompt（无 few-shot example），因为 GPT-4o 在 zero-shot 下已有 93%+ 成功率。

### 3.3 成本估算

**已知参数**:
- GPT-4o 定价: input $2.50/M tokens, output $10.00/M tokens
- 平均每步 prompt 长度: ~500 tokens（observation + history + admissible actions）
- 平均每步 output 长度: ~100 tokens（think + action）
- 平均成功轨迹步数: ~17 步
- GPT-4o 在 ALFWorld 的成功率: ~93%（zero-shot）

**估算**:

```
每条成功轨迹的 API 调用:
  - Input tokens: 17 步 × 500 tokens × (1 + 累积 history 增长) ≈ 17 × 800 = 13,600 tokens
  - Output tokens: 17 步 × 100 tokens = 1,700 tokens
  - 单轨迹成本: 13,600/1M × $2.50 + 1,700/1M × $10.00 = $0.034 + $0.017 = $0.051

考虑 93% 成功率，收集 500 条成功轨迹需要:
  - 总 rollout 次数: 500 / 0.93 ≈ 538 次
  - 总成本: 538 × $0.051 ≈ $27.4
  
使用 GPT-4o-mini（$0.15/$0.60 per M tokens）:
  - 单轨迹成本: ≈ $0.003
  - 总成本: ≈ $1.7（但成功率可能降至 ~80%）
```

**结论**: GPT-4o 收集 500 条成功轨迹，API 成本约 **$25-35**，非常经济。

### 3.4 verl-agent 可复用组件

| 组件 | 路径 | 可复用程度 |
|-----|------|----------|
| AlfWorldEnvironmentManager | `agent_system/environments/env_manager.py:133-242` | 直接复用 |
| SimpleMemory | `agent_system/memory/memory.py` | 直接复用 |
| Prompt Templates | `agent_system/environments/prompts/alfworld.py` | 直接复用 |
| Action Projection | `agent_system/environments/env_package/alfworld/projection.py` | 直接复用 |
| ALFWorld Env Wrapper | `agent_system/environments/env_package/alfworld/envs.py` | 需改造（去掉 Ray） |
| TrajectoryCollector | `agent_system/multi_turn_rollout/rollout_loop.py` | 需较大改造 |

verl-agent 的 rollout 是面向 RL 训练的（vLLM 推理 + DataProto 格式），直接复用于 GPT-4o rollout 改造成本较高。**建议写一个独立的轻量 rollout 脚本**，只复用环境管理和 prompt 部分。

---

## 4. 已有公开数据集

### 4.1 可直接使用的数据集

| 数据集 | 条数 | 来源 | 格式 | 适用性 |
|-------|------|------|------|--------|
| [u-10bei/sft_alfworld_trajectory_dataset_v5](https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v5) | 2,502 | 模板生成（非真实环境） | Chat + function-calling JSON | ⚠️ 非真实环境轨迹 |
| [awawa-agi/alfworld-raw](https://huggingface.co/datasets/awawa-agi/alfworld-raw) | 3,827 | ALFWorld 原始任务定义 | PDDL + TextWorld 规格 | ❌ 仅任务定义，非轨迹 |
| [hkust-nlp/agentboard](https://huggingface.co/datasets/hkust-nlp/agentboard) | 134 (ALFWorld) | AgentBoard 评估集 | JSONL + subgoals | ❌ 仅测试任务，无轨迹 |

### 4.2 学术论文中的轨迹数据

| 论文 | 轨迹数据 | 公开程度 |
|-----|---------|---------|
| ReAct (Yao et al., 2023) | 每种任务 1-2 条 few-shot 示例 | 公开（GitHub） |
| ActRe (Qu et al., 2024) | ~600 条合成轨迹 | 未明确公开 |
| A3T | 迭代收集，4 轮后 96% 成功率 | 未明确公开 |
| InterAct | 98% 成功率轨迹 | 未明确公开 |

### 4.3 评估与建议

**u-10bei 数据集的问题**: 这是**模板模拟生成**的数据，不是在真实 ALFWorld 环境中执行产生的。用于 SFT 训练可能没问题，但用于 TaxEI 的 error injection 需要**真实环境中的轨迹**（包含 observation 的自然变化），因此**不建议直接使用**。

**建议**: 自己用 GPT-4o 在真实 ALFWorld 环境中收集 500 条轨迹，成本低（~$30），质量有保证。

---

## 5. 技术细节

### 5.1 安装

```bash
# 创建 conda 环境（要求 Python 3.9+）
conda create -n alfworld python=3.9
conda activate alfworld

# 安装 alfworld（text-only 版本足够）
pip install alfworld

# 或安装完整版（含 AI2-THOR 视觉环境）
pip install 'alfworld[full]'

# 下载数据（PDDL 文件 + TextWorld 游戏文件）
alfworld-download

# 最新版本: 0.4.2 (2025-01)
```

### 5.2 已知坑

1. **Python 版本**: 必须 Python 3.9+。Python 3.11+ 可能有 textworld 编译问题。推荐 3.9 或 3.10。

2. **textworld 编译**: `alfworld[full]` 需要编译 textworld C 依赖。如果编译失败：
   ```bash
   # 先装依赖
   sudo apt-get install build-essential libffi-dev
   # 只装 text 版本（不需要编译 textworld 额外组件）
   pip install alfworld
   ```

3. **Shell quoting**: zsh 用户需要：
   ```bash
   pip install 'alfworld[full]'  # 注意引号
   ```

4. **数据下载**: `alfworld-download` 需要从 GitHub Release 下载 ~200MB 数据。在国内服务器可能需要代理。AutoDL 上需先 `source /etc/network_turbo`。

5. **Windows 不支持**: ALFWorld 仅支持 Linux 和 macOS。

6. **AI2-THOR 版本**: 如果使用 `AlfredThorEnv`（视觉环境），需要 X display 或 xvfb。Text-only 模式不需要。

7. **环境重置**: 每次 `env.reset()` 会加载一个新的 TextWorld 游戏文件，初始化较慢（~0.5s/task）。

### 5.3 快速验证

```python
import alfworld.agents.environment as environment
import yaml

# 加载配置
with open('base_config.yaml') as f:
    config = yaml.safe_load(f)

# 创建 text-only 环境
env_type = config['env']['type']  # 'AlfredTWEnv'
env = getattr(environment, env_type)(config, train_eval='train')
env = env.init_env(batch_size=1)

# 重置并交互
obs, info = env.reset()
print(obs[0])  # 初始 observation
print(info['admissible_commands'][0])  # 可选动作列表

# 执行动作
obs, scores, dones, infos = env.step(['go to fridge 1'])
print(obs[0])  # 新 observation
```

### 5.4 AutoDL 部署注意事项

```bash
# 1. 启用代理
source /etc/network_turbo

# 2. 创建 conda 环境（使用 autodl-tmp 避免根分区满）
conda create -p /root/autodl-tmp/envs/alfworld python=3.9 -y
conda activate /root/autodl-tmp/envs/alfworld

# 3. 安装
pip install alfworld

# 4. 下载数据到 autodl-tmp
export ALFWORLD_DATA=/root/autodl-tmp/alfworld_data
alfworld-download

# 5. 验证
python -c "import alfworld; print(alfworld.__version__)"
```

---

## 6. TaxEI 轨迹收集实施建议

### 6.1 推荐方案

1. **在 AutoDL 5090 上安装 ALFWorld**（text-only，无需 GPU）
2. **写一个独立的 GPT-4o rollout 脚本**，复用 verl-agent 的 prompt template
3. **从 train split 的 3,553 个任务中采样**，按任务类型均匀采样
4. **每种任务类型收集 ~83 条成功轨迹**（总计 500 条）
5. **保存格式**: JSON，每条包含 task_type, task_description, steps[], success, gamefile

### 6.2 建议的轨迹存储格式

```json
{
    "id": "traj_001",
    "task_type": "pick_heat_then_place",
    "task_description": "put a hot apple in countertop",
    "gamefile": "pick_heat_then_place_in_recep-Apple-None-Countertop-12/trial_T20190907_105557_364325",
    "num_steps": 15,
    "success": true,
    "steps": [
        {
            "step": 0,
            "observation": "You are in the middle of a room...",
            "admissible_commands": ["go to cabinet 1", "go to fridge 1", ...],
            "thought": "I need to find an apple. The fridge is a likely place.",
            "action": "go to fridge 1"
        },
        {
            "step": 1,
            "observation": "You arrive at loc 5. The fridge 1 is closed.",
            "admissible_commands": ["open fridge 1", "go to cabinet 1", ...],
            "thought": "The fridge is closed. I need to open it to look inside.",
            "action": "open fridge 1"
        }
    ]
}
```

### 6.3 Error Injection 扩展点

收集到成功轨迹后，可注入两类 error：

- **Planning Error**: 在 thought 中修改推理（如选择错误目标、遗漏步骤），导致 action 偏离最优路径
- **Context Error**: 在 observation 或 history 中注入噪声（如遗漏物体、混淆位置），模拟 context 理解错误

verl-agent 中的扩展点（参考 `AlfWorldEnvironmentManager`）:
- `SimpleMemory.fetch()` — 修改 history 字符串
- `build_text_obs()` — 在 prompt 中注入错误
- `alfworld_projection()` — 修改 action 解析

---

## 参考资源

- ALFWorld 论文: https://arxiv.org/abs/2010.03768
- ALFWorld GitHub: https://github.com/alfworld/alfworld
- ReAct 论文: https://arxiv.org/abs/2210.03629
- ReAct GitHub (ALFWorld prompt): https://github.com/ysymyth/ReAct
- verl-agent GitHub: https://github.com/langfengQ/verl-agent
- HuggingFace ALFWorld SFT 数据集: https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v5
- HuggingFace ALFWorld Raw 数据集: https://huggingface.co/datasets/awawa-agi/alfworld-raw
- AgentBoard: https://huggingface.co/datasets/hkust-nlp/agentboard
- ReAct Meets ActRe: https://arxiv.org/abs/2403.14589
- GPT-4o 定价: https://developers.openai.com/api/docs/pricing
