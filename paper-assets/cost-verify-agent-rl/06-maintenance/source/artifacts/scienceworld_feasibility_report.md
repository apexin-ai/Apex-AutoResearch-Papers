# ScienceWorld 环境接入 RAGEN 可行性调研报告

**日期**: 2026-05-19

---

## 1. ScienceWorld 环境概述

### 1.1 基本信息
- **来源**: Allen AI (allenai/ScienceWorld)
- **类型**: Text-based interactive environment，围绕小学科学课程任务
- **安装**: `pip install scienceworld`（需要 Java 1.8+，通过 py4j 与 JVM 通信）
- **Python 版本**: >= 3.8

### 1.2 API 接口

核心方法签名：

```python
class ScienceWorldEnv:
    def __init__(self, taskName=None, serverPath=None, envStepLimit=100)
    def load(self, taskName, variationIdx=0, simplificationStr="", generateGoldPath=False)
    def reset(self) -> Tuple[str, Dict]           # (observation, info)
    def step(self, input_str: str) -> Tuple[str, int, bool, Dict]  # (obs, reward, done, info)
    def close()
    
    # Action space
    def get_valid_action_object_combinations() -> List[str]   # admissible actions
    def get_possible_actions() -> List[str]
    def get_possible_objects() -> List[str]
    
    # Task info
    def get_task_names() -> List[str]
    def get_task_description() -> str
    def get_goal_progress() -> str
    
    # Free actions (不消耗 step)
    def look() -> str
    def inventory() -> str
    def taskdescription() -> str
    
    # Gold path
    def get_gold_action_sequence() -> List[str]    # 需要 load 时设 generateGoldPath=True
    
    # Train/Dev/Test splits
    def get_variations_train() -> List[int]
    def get_variations_dev() -> List[int]
    def get_variations_test() -> List[int]
```

### 1.3 Action Space
- **Text-based**，与 ALFWorld 同类
- 提供 `get_valid_action_object_combinations()` 返回当前 state 下所有合法 action-object 组合
- 典型 action 格式: `"pick up fork"`, `"pour water into beaker"`, `"focus on thermometer"`
- Action space 规模动态变化，通常 50-200 个合法 action

### 1.4 Observation 格式
- **纯文本**描述当前场景状态
- 可通过 `look()` 和 `inventory()` 获取额外信息（free actions）
- 无 state dict，纯自然语言

### 1.5 Reward 信号
- `step()` 返回 integer reward（0-100 分制）
- **非 sparse**：有 subgoal 完成的中间 reward（goal progress 可查询）
- 任务成功 = 达到满分
- 可通过 `get_goal_progress()` 查看细粒度进展

### 1.6 Episode 结构
- `envStepLimit` 默认 100 步
- Variable length，不同任务复杂度差异大
- Gold path 长度通常 10-50 步

### 1.7 任务规模

**10 大类，30 子任务**，总计数千个 variations：

| 大类 | 子任务数 | Variations 范围 | 示例 |
|------|---------|----------------|------|
| 物态变化 (boil/melt/freeze) | 4 | ~30 each | 烧开水、融化冰块 |
| 温度测量 & 熔点 | 3 | 300-540 | 用温度计测量 |
| 电学 & 导电性 | 4 | 20-900 | 连接电路 |
| 生物/非生物分类 | 4 | ~300 each | 分类物品 |
| 植物生长 | 2 | ~126 each | 种植观察 |
| 化学混合 | 3 | 32-36 | 混合物质 |
| 生命周期 | 3 | ~125 each | 分析寿命 |
| 生命阶段 | 2 | 10-14 | 观察生长 |
| 斜面力学 | 3 | 168-1386 | 物理实验 |
| 孟德尔遗传 | 2 | 120-480 | 遗传实验 |

### 1.8 Simplifications
支持 6 种简化选项：`teleportAction`, `openDoors`, `selfWateringFlowerPots`, `noElectricalAction`, `openContainers`。`easy` preset 开启大部分简化。

---

## 2. RAGEN 当前支持状态

### 2.1 ScienceWorld 支持
**不支持**。`grep -ri "scienceworld"` 在整个 RAGEN 代码库中无匹配。

### 2.2 已有环境列表

RAGEN 当前支持 12 个环境（`__init__.py` 注册）：

| 环境 | 类型 | 基类 |
|------|------|------|
| bandit | 离散 | BaseDiscreteActionEnv |
| countdown | 语言 | BaseLanguageBasedEnv |
| sokoban | 离散 | BaseDiscreteActionEnv |
| frozen_lake | 离散 | BaseDiscreteActionEnv |
| metamathqa | 语言 | BaseLanguageBasedEnv |
| lean | 语言 | BaseLanguageBasedEnv |
| deepcoder | 语言 | BaseLanguageBasedEnv |
| sudoku | 语言 | BaseLanguageBasedEnv |
| game_2048 | 语言 | BaseLanguageBasedEnv |
| rubikscube | 语言 | BaseLanguageBasedEnv |
| alfworld* | 语言 | BaseLanguageBasedEnv |
| webshop* | 语言 | BaseLanguageBasedEnv |

*ALFWorld 和 WebShop 通过 try/except 动态注册（依赖可选）。

### 2.3 接口模式

RAGEN BaseEnv 接口：
```python
class BaseLanguageBasedEnv(BaseEnv):
    def reset(self, seed=None, **kwargs) -> Any          # 返回 rendered observation
    def step(self, action: str) -> Tuple[Any, float, bool, Dict]  # (obs, reward, done, info)
    def render(self, mode='text') -> Any                  # optional
    def close()                                           # optional
```

ALFWorld 实现额外特性：
- `reset(seed, mode)` 支持 train/val/test 模式切换
- Observation 包含 admissible actions 列表
- Reward: `config.score * float(won)` (sparse, 成功 10.0)
- Info dict 包含 `action_is_valid`, `success`, `anchor_obs`

---

## 3. 适配工程量评估

### 3.1 需要新建的文件

```
RAGEN/ragen/env/scienceworld/
├── __init__.py          # 导出 ScienceWorldEnv, ScienceWorldEnvConfig
├── config.py            # ScienceWorldEnvConfig dataclass
├── env.py               # ScienceWorldEnv(BaseLanguageBasedEnv)
└── utils.py             # task mapping, prompt formatting 等辅助函数
```

### 3.2 需要修改的文件

| 文件 | 修改内容 |
|------|---------|
| `ragen/env/__init__.py` | 添加 try/except 动态注册 ScienceWorld（同 ALFWorld 模式） |
| `config/envs.yaml` | 添加 ScienceWorld 环境配置项 |

### 3.3 实现要点

**env.py 核心逻辑**（对标 ALFWorld 实现）：
1. `__init__`: 创建 `scienceworld.ScienceWorldEnv` 实例，配置 task/variation
2. `reset(seed, mode)`: 
   - 根据 seed 选择 variation（train/dev/test split）
   - 调用 `sw_env.load(taskName, variationIdx)` + `sw_env.reset()`
   - 格式化 observation + admissible actions
3. `step(action)`: 
   - 调用 `sw_env.step(action)`
   - 重新获取 `get_valid_action_object_combinations()` 作为 admissible actions
   - 归一化 reward（ScienceWorld 0-100 → RAGEN 0-1 或 0-10）
   - 返回格式化 observation

**config.py**：
```python
@dataclass
class ScienceWorldEnvConfig(BaseEnvConfig):
    task_name: str = "boil"          # 或 task_id
    simplification: str = ""         # "easy" preset 等
    env_step_limit: int = 100
    score: float = 10.0              # 成功奖励 scale
    use_admissible_actions: bool = True
```

**envs.yaml 配置示例**：
```yaml
ScienceWorld:
    env_type: scienceworld
    max_actions_per_traj: 50
    parallel_friendly: false
    max_workers: 1
    env_instruction: |
      You are a science experiment agent...
    max_tokens: 512
    env_config:
      task_name: "boil"
      simplification: ""
      env_step_limit: 100
```

### 3.4 工程风险与注意事项

| 风险 | 严重度 | 说明 |
|------|--------|------|
| Java/JVM 依赖 | **中** | 需要 Java 1.8+，服务器需预装。py4j 启动有 cold start 延迟 |
| 并行化受限 | **中** | 每个 ScienceWorld 实例启动独立 JVM，内存开销大（~200-500MB/instance）。ALFWorld 也有类似问题（`max_workers: 1`） |
| py4j 通信开销 | **低** | 每次 step/action 通过 socket 与 JVM 通信，延迟 ~5-20ms，相对 LLM 推理时间可忽略 |
| Task 选择策略 | **低** | 30 个子任务难度差异大，需要设计 task sampling 策略 |

### 3.5 预估工作量

| 任务 | 预估时间 |
|------|---------|
| env.py + config.py + utils.py 实现 | 4-6 小时 |
| __init__.py + envs.yaml 注册 | 0.5 小时 |
| 测试与调试（本地 dry-run） | 2-3 小时 |
| Prompt 设计与调优 | 2-4 小时 |
| SFT 数据准备（如需） | 4-8 小时 |
| **总计** | **12-22 Worker-hours** |

---

## 4. Expert Data 可用性

### 4.1 内置 Gold Path
ScienceWorld 自带 oracle agent，通过 `generateGoldPath=True` 可获取每个 variation 的最优 action sequence：
```python
env.load("boil", variationIdx=0, generateGoldPath=True)
env.reset()
gold_actions = env.get_gold_action_sequence()  # ['pick up beaker', 'pour water into beaker', ...]
```
这是最直接的 expert trajectory 来源。

### 4.2 已有 SFT 数据集
- **ETO (ACL 2024)**: HuggingFace `agent-eto/eto-sft-trajectory` 包含 ScienceWorld SFT trajectories
  - 对话格式: `{"id": "...", "conversations": [{"from": "human/gpt", "value": "..."}]}`
  - 可直接用于 SFT warmstart
- **cognitiveailab/t5-scienceworld**: 包含 goldpaths-all.zip，T5 训练用的 gold trajectory 数据

### 4.3 自动生成方案
若需更多数据：
1. **Gold path 批量生成**: 遍历所有 task + variation，调用 `get_gold_action_sequence()` 收集
2. **LLM rollout 收集**: 用 GPT-4/Claude 在环境中交互，筛选成功 trajectory
3. **ETO 方法**: 先 SFT，再收集失败 trajectory 做 contrastive DPO

### 4.4 数据量估算
- 30 个子任务 × 平均 100+ variations × 每条 10-50 步 ≈ 3000+ expert trajectories
- 足够支持 SFT warmstart

---

## 5. 相关工作总结

### 5.1 直接相关论文

| 论文 | 年份 | 方法 | ScienceWorld 结果 | 模型 |
|------|------|------|-------------------|------|
| **EMPO2** | 2026.02 | Exploratory Memory + On/Off-policy RL | Avg 75.9（vs GRPO 33.2，+128.6%）| Qwen2.5-7B-Instruct |
| **ETO** | 2024 (ACL) | SFT + Contrastive DPO | +22% over SFT on unseen test | - |
| **StepAgent** | 2024.11 | Step-wise RL + Inverse RL | step-wise reward 优于 sparse | - |
| **Reinforcement World Model** | 2026.02 | Action-conditioned world model | 自监督学习环境动态 | - |
| **CLIN** | 2023 | Continual learning + memory | ScienceWorld persistent memory | - |

### 5.2 关键发现

1. **EMPO2 是当前 SOTA**：在 19 个 ScienceWorld 任务上平均 75.9 分，使用 GRPO + memory augmentation，基于 verl 框架
2. **训练设置惯例**: 前 5 个 variations 训练，20 个 unseen test variations 评估
3. **GRPO baseline 在 ScienceWorld 上有效但不强**：33.2 平均分，说明有很大提升空间
4. **SFT warmstart 有帮助**：ETO 证明先 SFT 再 RL 效果好于纯 RL
5. **与我们研究的关联**: ScienceWorld 的 multi-step reasoning + sparse reward 特性正好适合验证 step-independent RL 的 sign misattribution 问题

---

## 6. 可行性结论和建议

### 6.1 可行性评估：**高度可行**

| 维度 | 评分 | 理由 |
|------|------|------|
| API 兼容性 | ★★★★★ | Text-based, 标准 reset/step 接口，与 ALFWorld 高度相似 |
| 工程复杂度 | ★★★★☆ | 有 ALFWorld 模板参考，主要是 wrapper 工作。Java 依赖略增复杂度 |
| Expert Data | ★★★★★ | 内置 gold path + 现成 SFT 数据集 |
| 研究价值 | ★★★★★ | 验证 generalizability 的理想第二环境 |
| 社区基准 | ★★★★☆ | EMPO2/ETO 等提供了充足的 baseline 对比数据 |

### 6.2 与 ALFWorld 的对比

| 特性 | ALFWorld | ScienceWorld |
|------|----------|--------------|
| 任务类型 | 家庭任务（6类） | 科学实验（30子任务） |
| Action space | Admissible actions | Admissible actions |
| Reward | Sparse (success only) | 有中间 reward (0-100) |
| 任务多样性 | 中 | 高（10大类30子任务） |
| 平均 episode 长度 | 15-50 步 | 10-50 步 |
| 依赖 | Python (textworld) | Java + py4j |
| 并行化 | 困难 | 困难（JVM 开销） |

### 6.3 建议

1. **推荐接入**：ScienceWorld 是验证 sign misattribution 发现 generalizability 的优质第二环境
2. **优先实现路径**：
   - Phase 1: 实现基础 wrapper（1-2天），单任务（如 "boil"）验证 GRPO baseline
   - Phase 2: 生成 gold path SFT 数据，做 SFT warmstart
   - Phase 3: 运行完整实验（多任务），验证 step-independent RL 的发现
3. **Task 选择建议**: 参考 EMPO2 的 19 个任务设置，前 5 variations 训练 + 20 unseen test
4. **Reward 处理**: ScienceWorld 的中间 reward (0-100) 可直接用于验证 step-level credit assignment，比 ALFWorld 的 binary reward 更适合分析 sign misattribution

### 6.4 风险缓解

- **Java 依赖**: Docker 镜像预装或 conda 安装 openjdk
- **并行瓶颈**: 与 ALFWorld 相同，设 `max_workers: 1`，`parallel_friendly: false`
- **JVM 内存**: 预分配足够内存，避免 OOM
