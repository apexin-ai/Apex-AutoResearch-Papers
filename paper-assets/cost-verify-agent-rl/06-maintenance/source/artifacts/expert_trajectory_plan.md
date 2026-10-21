# ALFWorld Expert Trajectory 数据准备方案

## 1. 现有数据分析

### 当前 SFT 数据 (`/root/autodl-tmp/sft_data/alfworld_sft_ragen.jsonl`)
- **来源**: `u-10bei/sft_alfworld_trajectory_dataset` v1 (模板合成，非真实环境交互)
- **规模**: 1200 条轨迹, 4.3MB
- **任务分布**: 6 类各 200 条 (pick_and_place, clean, heat, cool, examine, pick_two)
- **格式**: JSONL, messages 格式 (system/user/assistant 多轮对话)
- **System prompt**: RAGEN 自有的 self-guidance 格式 (`<think>[Assessment]...[Reasoning]...[Suggestion]...</think><answer>action</answer>`)

### 数据质量问题
1. **模板合成 vs 真实交互**: 现有数据是"轻量模拟器"生成的模板轨迹，非真实 ALFWorld 环境交互。观察文本和动作可能与实际 RAGEN RL 训练环境有分布差异。
2. **缺失任务类型**: ALFWorld train set 有 7 种任务类型，现有数据缺少 `pick_and_place_with_movable_recep`（365 个训练游戏）。
3. **exp008_sft 结果**: action_is_valid 8.4%→90%，但 success_rate=0%。SFT 教了格式但没教有效策略。
4. **HF v5 数据集**: `u-10bei/sft_alfworld_trajectory_dataset_v5` 有 2502 条，使用 function calling 格式（非 RAGEN 格式），各任务类型 417 条。

### ALFWorld 游戏文件清单
| Split | 游戏数 |
|-------|--------|
| train | 3553 |
| valid_seen | 140 |
| valid_unseen | 134 |
| valid_train | 200 |

### 训练集任务类型分布
| 任务类型 | 游戏数 | Expert 策略类 |
|----------|--------|-------------|
| pick_two_obj_and_place | 407 | PickTwoObjAndPlaceTWPolicy |
| pick_and_place_simple | 385 | PickAndPlaceSimpleTWPolicy |
| pick_and_place_with_movable_recep | 365 | **无对应策略类** |
| pick_heat_then_place_in_recep | 340 | PickHeatThenPlaceInRecepTWPolicy |
| pick_cool_then_place_in_recep | 339 | PickCoolThenPlaceInRecepTWPolicy |
| pick_clean_then_place_in_recep | 334 | PickCleanThenPlaceInRecepTWPolicy |
| look_at_obj_in_light | 265 | LookAtObjInLightTWPolicy |
| **合计** | **2435 任务 × ~1.5 trials = 3553 游戏** | |

## 2. ALFWorld HandCoded Expert 分析

### 已安装位置
```
/root/miniconda3/lib/python3.12/site-packages/alfworld/agents/expert/
├── __init__.py               # 导出 HandCodedTWAgent, HandCodedAgentTimeout
├── handcoded_expert.py       # 基类 BasePolicy + 6 种任务策略 + HandCodedAgent
├── handcoded_expert_tw.py    # TextWorld 适配层 (用 PDDL predicates)
└── handcoded_expert_thor.py  # THOR 适配层 (不需要)
```

### Expert 架构
```
HandCodedAgent (textworld.Agent)
  └── HandCodedTWAgent
        ├── reset(game_file) → 读 traj_data.json → 选择 policy
        ├── observe(obs) → 更新 receptacles/objects
        └── act(game_state, reward, done, last_action) → 返回 action
              └── policy.act(game_state, last_action)
                    ├── observe(obs) → 更新搜索状态
                    ├── check_subgoal_completion() → 跳转子目标
                    └── get_next_subgoal() → 导航/交互动作

AlfredExpert (textworld.core.Wrapper)
  ├── _gather_infos() → 设置 state["extra.expert_plan"]
  ├── reset() → 初始化 HandCodedTWAgent
  └── step(command) → 更新 expert plan
```

### Expert 工作原理
`HandCodedTWAgent` 是规则化的子目标分解 agent：

1. **初始化**: `reset(game_file)` 从 `traj_data.json` 读取 `task_type` + `pddl_params`（object_target, parent_target 等）
2. **子目标分解**: 每种任务分解为固定子目标序列：
   - `pick_and_place`: find obj → take → find recep → put
   - `pick_heat`: find obj → take → goto microwave → heat → find recep → put
   - `pick_cool`: find obj → take → goto fridge → cool → find recep → put
   - `pick_clean`: find obj → take → goto sinkbasin → clean → find recep → put
   - `look_at_obj`: find obj → take → goto lamp → use lamp
   - `pick_two`: (循环两次) find obj → take → find recep → put
3. **动作选择**: 基于 PDDL state facts + admissible_commands 判断当前子目标进度
4. **搜索策略**: 按 `VAL_RECEPTACLE_OBJECTS` 先验顺序搜索 receptacles（如 apple 优先查 fridge/countertop/microwave）
5. **Fallback**: 如果 expert 动作 == last_action 或不在 admissible_commands 中，随机选择一个 admissible action

### Expert 特性
- **成功率**: ~80-90%，非 100%（搜索可能超时）
- **非最优**: 按固定优先级搜索，不是最短路径
- **最大步数**: 初始化参数 `max_steps=150`，超时抛 `HandCodedAgentTimeout`
- **关键依赖**: 需要 `request_infos.facts=True` 来获取 PDDL predicates

### 两种 Expert 模式
| 模式 | 实现 | 特点 |
|------|------|------|
| `handcoded` | HandCodedTWAgent 规则决策 | 闭环、逐步反应、需要 facts |
| `planner` | TextWorld 的 Fast Downward | PDDL 规划、全局最优、但慢 |

## 3. 文献数据量参考

| 工作 | SFT 数据量 | 场景 | 备注 |
|------|-----------|------|------|
| exp008_sft (我们) | 1200 | ALFWorld | action_is_valid 90%, success 0% |
| SPEAR (Tencent) | 无 SFT, self-imitation buffer 2048 | ALFWorld | GRPO 72.8% → 88.9% (+16.1%) |
| ALFWorld 原论文 | 3553 游戏 × DAgger | ALFWorld | DAgger 迭代收集 |
| AgentTrek | 42-3553 expert trajectories | ALFWorld | GPT SFT |
| Warm Up Before Train (EMNLP 2025) | 50-100 target domain | 通用 | + domain-agnostic warmup |
| WebShop 饱和点 | ~1000 traj | WebShop | 25→1000 后饱和 |
| HF u-10bei v5 | 2502 条 | ALFWorld | 模板合成, function calling 格式 |

**结论**: 1200 条模板数据质量不够。目标 **2000-3000 条真实环境交互**的 expert 轨迹。

## 4. 推荐方案: HandCodedTWAgent 批量收集

### 方案比较

| 方案 | 优点 | 缺点 | 推荐度 |
|------|------|------|--------|
| A. HandCodedTWAgent 批量 rollout | 真实交互、API 现成、覆盖全任务 | Expert 非最优、~80-90% 成功率 | ★★★★★ |
| B. PDDL planner (Fast Downward) | 全局最优路径 | 极慢、需 PDDL→text 转换 | ★★★ |
| C. 更多模板合成 | 最简单 | 和现有数据同质、非真实交互 | ★★ |
| D. LLM rollout 收集 | 多样性高 | API 成本高、成功率低 | ★★ |

**选择方案 A**，原因：
1. ALFWorld 已安装 `HandCodedTWAgent`，通过 `AlfredExpert` wrapper 一行拿到 expert plan
2. 3553 个训练游戏（每个可多次 rollout）提供足够多样性
3. 真实环境交互产生的 obs/action 与 RAGEN RL 训练时分布一致
4. Expert 利用 PDDL state predicates 做决策，轨迹质量远高于模板合成

### 生成脚本设计

```python
# scripts/collect_expert_trajectories.py
"""
用 ALFWorld HandCodedTWAgent 收集 expert 轨迹，转换为 RAGEN SFT 格式。

核心流程:
1. 遍历 train game files (3553 个 .tw-pddl 文件)
2. 对每个游戏，用 AlfredExpert wrapper 获取 expert_plan
3. 只保留 won=True 的成功轨迹
4. 转换为 RAGEN self-guidance messages 格式

输出: /root/autodl-tmp/sft_data/expert_trajectories.jsonl
"""

import os
import json
import glob
import yaml
import textworld
import textworld.gym
from alfworld.agents.environment.alfred_tw_env import (
    AlfredTWEnv, AlfredDemangler, AlfredInfos,
    AlfredExpert, AlfredExpertType
)

SYSTEM_PROMPT = """You're a helpful assistant. You are an expert agent in the ALFRED Embodied Environment.
Complete household tasks by navigating and interacting with objects.

Before each action, you MUST first produce a self-guidance assessment:
[Assessment: positive/neutral/negative] - evaluate your current progress.
[Reasoning: one sentence analyzing what has been accomplished and what remains.]
[Suggestion: the best next action from admissible actions.]

Your reasoning with self-guidance MUST be enclosed within <think> </think> tags.
Then choose an admissible action and present it within <answer>...</answer> tags."""


def collect_single_game(game_file, max_steps=50):
    """收集单个游戏的 expert 轨迹"""
    request_infos = textworld.EnvInfos(
        won=True,
        admissible_commands=True,
        extras=["gamefile", "expert_plan"]
    )
    
    wrappers = [
        AlfredDemangler(),
        AlfredInfos(),
        AlfredExpert(expert_type=AlfredExpertType.HANDCODED)
    ]
    
    env_id = textworld.gym.register_game(
        game_file,
        request_infos=request_infos,
        max_episode_steps=max_steps,
        wrappers=wrappers
    )
    env = textworld.gym.make(env_id)
    
    try:
        obs, info = env.reset()
        trajectory = []
        done = False
        
        while not done:
            expert_action = info.get('extra.expert_plan', ['look'])[0]
            admissible = info['admissible_commands'][0]
            
            trajectory.append({
                'observation': obs[0],
                'admissible_actions': admissible,
                'action': expert_action
            })
            
            obs, _, dones, info = env.step([expert_action])
            done = dones[0]
        
        won = info.get('won', [False])[0]
        return trajectory if won else None
    
    except Exception as e:
        print(f"Error in {game_file}: {e}")
        return None
    finally:
        env.close()


def infer_assessment(step_obs, action, step_idx, total_steps):
    """根据 observation 和 action 推断 self-guidance assessment"""
    if step_idx == 0:
        return "neutral"
    
    obs_lower = step_obs.lower()
    
    # 关键进展动作 → positive
    if any(kw in action for kw in ['take', 'heat', 'cool', 'clean', 'use', 'put']):
        return "positive"
    
    # 搜索中看到空/关闭 → negative
    if 'nothing' in obs_lower or 'closed' in obs_lower or 'empty' in obs_lower:
        return "negative"
    
    # 看到有东西 → neutral/positive
    if 'you see' in obs_lower:
        return "neutral"
    
    return "neutral"


def generate_reasoning(step, action, task_desc, step_idx):
    """生成简短的 reasoning 文本"""
    obs_lower = step['observation'].lower()
    
    if step_idx == 0:
        return f"I need to {task_desc}. Let me start searching."
    
    if 'take' in action:
        obj = action.replace('take ', '').split(' from ')[0]
        return f"Found {obj}. I should pick it up."
    elif 'put' in action:
        return f"Now I'll place the object to complete the task."
    elif 'heat' in action or 'cool' in action or 'clean' in action:
        return f"Processing the object as required by the task."
    elif 'use' in action:
        return f"Using the device to complete the task."
    elif 'open' in action:
        return f"Opening to check contents."
    elif 'go to' in action:
        dest = action.replace('go to ', '')
        return f"Moving to {dest} to search."
    elif 'close' in action:
        return f"Closing after checking."
    
    return f"Continuing to work on the task."


def trajectory_to_messages(trajectory, task_desc):
    """将 expert 轨迹转换为 RAGEN SFT messages 格式"""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    total = len(trajectory)
    for i, step in enumerate(trajectory):
        # User message
        actions_str = ", ".join(step['admissible_actions'])
        user_content = f"{step['observation']}\n\nAdmissible actions: [{actions_str}]"
        if i == 0:
            # 第一条 user message 包含 task description（已在 observation 中）
            user_content = step['observation']
            if step['admissible_actions']:
                user_content += f"\n\nAdmissible actions: [{actions_str}]"
        
        messages.append({"role": "user", "content": user_content})
        
        # Assistant message with self-guidance
        assessment = infer_assessment(step['observation'], step['action'], i, total)
        reasoning = generate_reasoning(step, step['action'], task_desc, i)
        action = step['action']
        
        messages.append({
            "role": "assistant",
            "content": (
                f"<think>[Assessment: {assessment}] "
                f"[Reasoning: {reasoning}] "
                f"[Suggestion: {action}]</think>"
                f"<answer>{action}</answer>"
            )
        })
    
    return {"messages": messages}


def extract_task_description(first_obs):
    """从第一个 observation 中提取 task description"""
    if "Your task is to:" in first_obs:
        return first_obs.split("Your task is to:")[-1].strip()
    return "complete the task"


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='/root/autodl-tmp/sft_data/expert_trajectories.jsonl')
    parser.add_argument('--max_steps', type=int, default=50)
    parser.add_argument('--data_path', default='/root/autodl-tmp/alfworld')
    args = parser.parse_args()
    
    # 找到所有 train game files
    game_files = sorted(glob.glob(
        os.path.join(args.data_path, 'json_2.1.1/train/*/trial_*/game.tw-pddl')
    ))
    print(f"Found {len(game_files)} game files")
    
    # 断点续传: 检查已处理的游戏
    processed = set()
    if os.path.exists(args.output):
        with open(args.output) as f:
            for line in f:
                data = json.loads(line)
                if 'game_file' in data:
                    processed.add(data['game_file'])
        print(f"Already processed {len(processed)} games, resuming...")
    
    stats = {'total': 0, 'success': 0, 'fail': 0, 'error': 0, 'task_types': {}}
    
    with open(args.output, 'a') as fout:
        for i, game_file in enumerate(game_files):
            if game_file in processed:
                continue
            
            stats['total'] += 1
            
            # 获取 task type
            task_dir = os.path.basename(os.path.dirname(os.path.dirname(game_file)))
            task_type = task_dir.rsplit('-', 1)[0] if '-' in task_dir else task_dir
            # Normalize: pick_and_place_simple-Apple-None-Cabinet-1 → pick_and_place_simple
            for t in ['pick_and_place_simple', 'pick_two_obj_and_place',
                       'pick_heat_then_place_in_recep', 'pick_cool_then_place_in_recep',
                       'pick_clean_then_place_in_recep', 'look_at_obj_in_light',
                       'pick_and_place_with_movable_recep']:
                if task_dir.startswith(t):
                    task_type = t
                    break
            
            trajectory = collect_single_game(game_file, args.max_steps)
            
            if trajectory is None:
                stats['fail'] += 1
            else:
                stats['success'] += 1
                task_desc = extract_task_description(trajectory[0]['observation'])
                messages = trajectory_to_messages(trajectory, task_desc)
                messages['game_file'] = game_file
                messages['task_type'] = task_type
                messages['num_steps'] = len(trajectory)
                fout.write(json.dumps(messages, ensure_ascii=False) + '\n')
                
                stats['task_types'][task_type] = stats['task_types'].get(task_type, 0) + 1
            
            if (i + 1) % 100 == 0:
                print(f"Progress: {i+1}/{len(game_files)}, "
                      f"success={stats['success']}, fail={stats['fail']}")
    
    print(f"\n=== Final Stats ===")
    print(f"Total: {stats['total']}")
    print(f"Success: {stats['success']} ({100*stats['success']/max(1,stats['total']):.1f}%)")
    print(f"Fail: {stats['fail']}")
    print(f"\nTask type distribution:")
    for t, n in sorted(stats['task_types'].items(), key=lambda x: -x[1]):
        print(f"  {t}: {n}")


if __name__ == '__main__':
    main()
```

### 关键实现细节

#### AlfredExpert Wrapper 工作方式
```python
# alfred_tw_env.py 中的 AlfredExpert._gather_infos():
# 1. handcoded 模式: 用 HandCodedTWAgent 逐步计算 expert_plan
#    - expert.observe(feedback) → 更新 receptacle/object 信息
#    - expert.act(state, reward, done, prev_command) → 返回 action
#    - 设置 state["extra.expert_plan"] = [action]
# 2. planner 模式: 直接用 TextWorld 的 policy_commands (Fast Downward)
#    - 设置 state["extra.expert_plan"] = state["policy_commands"]
```

#### 需注意的问题
1. **`pick_and_place_with_movable_recep` 无策略类**: `HandCodedTWAgent.get_task_policy()` 中只有 6 种 policy，该任务类型 (365 games) 会抛 `Exception("Invalid Task Type")`。**处理方式**: try/except 跳过，约损失 10% 游戏。
2. **Expert 超时**: `max_steps=150` 默认值太大。设 `max_steps=50` 过滤低效轨迹（SFT 不需要长搜索）。
3. **TMPDIR**: 必须 `export TMPDIR=/root/autodl-tmp/tmp/`，否则 fast_downward 写 /tmp 爆盘。
4. **textworld.gym 注册**: 每个游戏单独注册 env_id，避免 batch 模式下 expert 状态混乱。

### 覆盖范围预估

| 任务类型 | 可用游戏 | 预估成功数 (85%) | 现有 SFT |
|----------|---------|-----------------|---------|
| pick_and_place_simple | 385 | ~327 | 200 |
| pick_two_obj_and_place | 407 | ~346 | 200 |
| pick_heat_then_place | 340 | ~289 | 200 |
| pick_cool_then_place | 339 | ~288 | 200 |
| pick_clean_then_place | 334 | ~284 | 200 |
| look_at_obj_in_light | 265 | ~225 | 200 |
| pick_and_place_with_movable_recep | 365 | **跳过** | **0** |
| **合计** | **2070** | **~1759** | **1200** |

如果每个游戏有 ~1.5 trials 且多次 rollout，可达 2500+。

### 预估时间和资源

- **计算**: 单线程约 1-2 小时（~3200 游戏 × ~1-2s/游戏）
- **磁盘**: ~10-15MB（2000+ 条 JSONL）
- **GPU**: 不需要 GPU，纯 CPU 任务
- **依赖**: 仅需 alfworld + textworld（已安装 @ python 3.12）
- **风险**: fast_downward planner 写 `/tmp` → 需设 `TMPDIR=/root/autodl-tmp/tmp/`

## 5. 实施步骤

### Step 1: 验证 Expert 可用性 (30 min)
```bash
export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR
export ALFWORLD_DATA=/root/autodl-tmp/alfworld

# 测试 5 个游戏
python3 -c "
from alfworld.agents.expert import HandCodedTWAgent
import textworld
# ... 测试单个游戏 ...
"
```

### Step 2: 编写收集脚本 (已完成，见上文)
- `scripts/collect_expert_trajectories.py`
- 支持断点续传、统计输出

### Step 3: 批量收集 (1-2 hr)
```bash
export TMPDIR=/root/autodl-tmp/tmp/
export ALFWORLD_DATA=/root/autodl-tmp/alfworld
cd /root/cost-verify-agent-rl

nohup python3 scripts/collect_expert_trajectories.py \
    --output /root/autodl-tmp/sft_data/expert_trajectories.jsonl \
    --max_steps 50 \
    --data_path /root/autodl-tmp/alfworld \
    > /tmp/collect_expert.log 2>&1 &
```

### Step 4: 质量检查 (30 min)
- 验证成功率、任务分布、步数分布
- 抽样 10 条检查轨迹质量
- 对比 expert 轨迹与现有模板轨迹的 observation 差异

### Step 5: 合并数据 & SFT 训练 (2 hr)
- 合并 expert_trajectories.jsonl + 现有 alfworld_sft_ragen.jsonl
- 去重（按 game_file / task description）
- 用 LLaMA-Factory 做 SFT（复用 exp008_sft 配置）
- 评估新 SFT 模型的 action_is_valid 和 success_rate

**总预估时间: 5-6 小时（含等待时间）**

## 6. 后续考虑

### 数据增强选项
1. **多次 rollout**: 同一游戏多次运行（expert 有 random fallback），获得轨迹多样性
2. **步数过滤**: 只保留步数 < 30 的高效轨迹
3. **Reasoning 增强**: 用 LLM 为 expert 轨迹生成更丰富的 reasoning（当前规则生成较机械）
4. **Negative 样本**: 保留部分失败轨迹作为 DPO/GRPO 的 rejected 样本

### 与 SPEAR 的配合
收集的 expert trajectories 可直接作为 SPEAR 的初始 replay buffer（trajectory_buffer_size=2048），跳过冷启动的盲目 exploration。

### pick_and_place_with_movable_recep 适配
如需覆盖此任务类型（365 games），需要：
1. 分析 `traj_data.json` 中该任务的 `pddl_params` 结构
2. 编写 `PickAndPlaceWithMovableRecepTWPolicy` 继承 `BasePolicy`
3. 子目标: find obj → take → find movable_recep → put in movable → find final_recep → put movable on final
4. 预估工作量: 2-3 小时
