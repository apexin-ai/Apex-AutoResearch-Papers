# WebShop & ScienceWorld 环境预调研报告

**日期**: 2026-05-12
**目的**: 为 ETADN 从 ALFWorld 扩展到 WebShop + ScienceWorld 做技术准备

---

## 1. WebShop 环境调研

### 1.1 ETO 集成方式

**核心文件**: `eval_agent/envs/webshop_env.py`

```python
class WebShopEnv(BaseEnv):
    def __init__(self, task: WebShopTask, env: WebAgentTextEnv, **kwargs):
        self.env = env  # webshop.web_agent_site.envs.WebAgentTextEnv
        self.session_id = task.session_id
```

- 底层依赖 `webshop` 包的 `WebAgentTextEnv`（OpenAI Gym 接口）
- Agent 输出格式与 ALFWorld 完全一致：`"Thought: ...\nAction: ..."`
- `parse_action()` 用同一正则 `r"Action: (.*)"` 提取 action
- `reset()` 调用 `env.reset(session_id)` 加载指定购物任务，初始 observation 从 `env.observation` 获取

**关键差异（vs ALFWorld）**:

| 维度 | ALFWorld | WebShop |
|------|----------|---------|
| reward 处理 | `info['won'][0]` (binary) | `env.step()` 直接返回 reward (continuous) |
| done 判定 | reward=True 即 done | `env.step()` 返回 done 标志（buy 操作触发） |
| reward 记录 | `state.reward = reward` | 仅在 done 时赋值 `state.reward = reward` |
| max_steps 超时 | `reward = reward`（保留最后值）| `reward = 0`（强制清零）|

### 1.2 环境搭建依赖

WebShop 需要运行一个本地 web 服务：

- **Python 包**: `webshop` (pip install 或从源码)
- **搜索引擎**: Pyserini + BM25 索引（用于商品搜索）
- **Flask web server**: 提供商品页面渲染
- **数据**: 1.18M 商品数据（从 Amazon 爬取），需下载并建索引
- **Java**: Pyserini 的 Lucene 后端需要 Java
- **安装复杂度**: **高** — 需要搭建 web 服务 + 搜索索引，比 ALFWorld 的 `pip install alfworld` 复杂得多

### 1.3 轨迹收集流程

**Task Loader** (`eval_agent/tasks/webshop.py`):
```python
class WebShopTask(Task):
    def __init__(self, session_id: str, **kwargs):
        self.session_id = session_id  # 商品 session 编号

    @classmethod
    def load_tasks(cls, split, part_num, part_idx):
        idxs = json.load(open("eval_agent/data/webshop/{split}_indices.json"))
        # 支持 part_num/part_idx 分片并行
```

- **Train**: 1,000 个 session（从 12,087 条 instruction 中采样）
- **Test**: 200 个 session
- 每个 task 由 `session_id`（整数）唯一标识
- 轨迹格式与 ALFWorld 一致：`conversations` 列表 + `meta.reward`

**与 ALFWorld 差异**:
- ALFWorld task 由 `game_file` 路径标识，WebShop 由 `session_id` 整数标识
- ALFWorld `env` 对象在 task 中创建，WebShop `env` 是全局共享的 `WebAgentTextEnv`

### 1.4 评估 Protocol

- **ETO 标准**: test split 200 tasks，temperature=0.0 greedy
- **原论文标准**: 500 test instructions（ETO 用的是子集）
- **指标**: Average Reward（0-1 连续值），不是 Success Rate

### 1.5 Action Space

仅两种 action：
- **`search[query]`** — 在搜索页面可用，输入搜索关键词
- **`click[element]`** — 在结果/商品页面可用，点击元素（商品标题、选项按钮、Buy Now 等）

Action space 比 ALFWorld 简单得多（ALFWorld 有 go/take/put/open/close/use/examine/heat/cool/clean 等）。

### 1.6 Observation Format

Text 模式（Simple mode）返回简化文本：
```
WebShop
Instruction: i need a long lasting 6.76 fl oz bottle of l'eau d'issey, price < $100
[Search]

---（搜索后）---
Page 1 (Total results: 50)
[Back to Search]
[Next >]
[B000VOHH8I] L'Eau d'Issey Pour Homme ... $64.98
[B001FSJK...] ...
```

包含：页面类型（搜索/结果/商品详情）、可点击元素列表、商品属性。

### 1.7 Episode 长度

- **ETO config**: `max_steps = 10`
- **原论文人类数据**: 平均 11.3 states，1.9 items visited
- **模型轨迹**: 平均 4.5 states
- 比 ALFWorld (max_steps=40) 短得多

### 1.8 Reward 定义

**连续值 [0, 1]**，公式：

```
r = r_type × (|U_att ∩ Y_att| + |U_opt ∩ Y_opt| + 1[y_price ≤ u_price]) / (|U_att| + |U_opt| + 1)
```

- `r_type`: 商品标题匹配度（TextMatch）
- `U_att/Y_att`: instruction/商品属性交集
- `U_opt/Y_opt`: instruction/商品选项交集（精确匹配）
- 价格约束: 满足预算=1，否则=0

**与 ALFWorld 区别**: ALFWorld 是 binary (0/1)，WebShop 是 continuous。这意味着：
- Preference pair 构建逻辑不同：ALFWorld 直接用成功/失败，WebShop 用 reward 大小比较
- 可以有 "部分成功" 的轨迹（reward=0.6 vs reward=0.3）

---

## 2. ScienceWorld 环境调研

### 2.1 ETO 集成方式

**核心文件**: `eval_agent/envs/sciworld_env.py`

```python
class SciWorldEnv(BaseEnv):
    def __init__(self, task: SciWorldTask, env: ScienceWorldEnv, **kwargs):
        self.env = env  # scienceworld.ScienceWorldEnv
        self.max_steps_dict = json.load(open("eval_agent/data/sciworld/max_steps.json"))
```

**关键差异（vs ALFWorld）**:

| 维度 | ALFWorld | ScienceWorld |
|------|----------|--------------|
| reward 来源 | `info['won'][0]` (binary) | `info['raw_score']` (continuous) |
| reward 记录 | 覆盖式 | **取最大值**: `if reward > self.state.reward: self.state.reward = reward` |
| max_steps | 全局固定 40 | **按 task 类型动态设置**，从 `max_steps.json` 读取 |
| max_steps 超时 reward | 保留最后 reward | 保留历史最高 reward（不清零） |
| env reset | task 自带 env 对象 | `env.load(sub_task_name, variation_idx, simplificationStr="easy")` |
| simplification | 无 | **"easy" 模式**: 允许瞬移(teleport)、简化 action hints |

**`reset()` 逻辑**:
```python
def reset(self):
    self.max_steps = self.max_steps_dict[self.task.sub_task_name]  # 按任务设置
    self.env.load(self.task.sub_task_name, self.task.variation_idx,
                  simplificationStr="easy", generateGoldPath=False)
    obs, info = self.env.reset()
    cur_task = info['taskDesc']  # 任务描述从 info 获取
```

### 2.2 环境搭建依赖

- **Python 包**: `scienceworld` (`pip install scienceworld`)
- **Java**: **必需** — ScienceWorld 核心是 4 万行 Scala 编译的 JAR（`scienceworld.jar`）
- **py4j**: Python-Java 桥接
- **JRE 1.8+**: 运行 JAR
- **安装复杂度**: **中等** — `pip install scienceworld` 会自带 JAR，但需要系统有 Java

ETO 配置中明确指定 JAR 路径：`"env_jar_path": "envs/scienceworld/scienceworld.jar"`

### 2.3 轨迹收集流程

**Task Loader** (`eval_agent/tasks/sciworld.py`):
```python
class SciWorldTask(Task):
    def __init__(self, sub_task_name: str, variation_idx: int, **kwargs):
        self.sub_task_name = sub_task_name    # e.g., "task-1-boil"
        self.variation_idx = variation_idx     # 变体编号

    @classmethod
    def load_tasks(cls, split, part_num, part_idx):
        task_idxs = json.load(open(f"eval_agent/data/sciworld/{split}_indices.json"))
        taskname2id = json.load(open("eval_agent/data/sciworld/taskname2id.json"))
        # 每条记录是 [task_name, variation_idx] pair
```

- **Train**: 1,000 个 (task_name, variation_idx) pairs
- **Dev**: 250 个 pairs
- **Test**: 410 个 pairs（含 seen + unseen tasks）
- 每个 task 由 `sub_task_name` + `variation_idx` 唯一标识

**与 ALFWorld 差异**:
- ALFWorld 只有 train/test，ScienceWorld 有 train/dev/test 三个 split
- ScienceWorld task 标识是二元组 (task_name, variation_idx)，更复杂
- ScienceWorld 有 unseen task 类型测试（task-8 摩擦力, task-9 遗传学在训练集中不存在）

### 2.4 评估 Protocol

- **ETO 标准**:
  - Test (seen): 247 pairs — tasks 1-7 + task 10（训练中见过的任务类型，不同 variation）
  - Test (unseen): 70 pairs — task 8 (摩擦力) + task 9 (遗传学)，训练中完全未见
  - 合计 ~410 pairs
- **指标**: Average Score（归一化到 0-100），取 episode 内最高分

### 2.5 Action Space

**25 个 action 模板**:

| 类别 | 数量 | 示例 |
|------|------|------|
| Zero-arg | 4 | `look around`, `inventory`, `wait`, `task` |
| One-arg | 16 | `open OBJ`, `pick up OBJ`, `go to LOC`, `teleport to LOC`, `focus on OBJ`, `mix OBJ` |
| Two-arg | 5 | `connect OBJ to OBJ`, `pour OBJ into OBJ`, `use OBJ on OBJ` |

- 每步约 ~200K 可能的 action-object 组合（因为要和场景中的物体组合）
- 比 ALFWorld 和 WebShop 都复杂得多
- "easy" 模式下有 `teleport to LOC` 简化导航

### 2.6 Observation Format

文本观测，包含：
- 当前房间描述 + 可见物体
- Agent 背包内容
- 任务目标描述
- "easy" 模式下有 action hints

环境共 10 个房间: kitchen, foundry, workshop, bathroom, outside, living room, bedroom, greenhouse, art studio, hallway。

### 2.7 Episode 长度

**按任务类型动态设置**（从 `max_steps.json`）:

| 任务 | Max Steps | 说明 |
|------|-----------|------|
| task-6-lifespan-(shortest-lived) | 10 | 最简单 |
| task-6-lifespan-(longest-lived-then-shortest-lived) | 12 | |
| task-3-find-* | 15 | 分类任务 |
| task-2-power-component | 20 | |
| task-2a-test-conductivity-* | 30 | |
| task-4-grow-plant | 30 | |
| task-5-chemistry-mix-paint-(secondary) | 15 | |
| task-5-chemistry-mix-paint-(tertiary) | 30 | |
| task-5-chemistry-mix | 60 | |
| task-4-grow-fruit | 60 | |
| task-1-change/freeze/melt | 80 | |
| task-1-boil | 100 | |
| task-10-measure-melting-point | **120** | 最复杂 |

范围 **10-120 步**，远超 ALFWorld 的固定 40 步。这对 ETADN 的 time discount 设计有重要影响。

### 2.8 Reward 定义

- **连续值 [0, 1]**（论文中 rescale 到 0-100）
- 每个任务有 2-15 个 subgoals（必须 + 可选）
- `info['raw_score']` 反映已完成 subgoal 比例
- 代码中取 **episode 内最高分**（不是最终分）：`if reward > self.state.reward: self.state.reward = reward`
- 与 ALFWorld 的 binary reward 和 WebShop 的 final reward 都不同

### 2.9 任务复杂度（vs ALFWorld）

| 维度 | ALFWorld | ScienceWorld |
|------|----------|--------------|
| 任务类型 | 6 类 | 30 类（10 个课程主题） |
| 变体机制 | 不同物体/位置 | 不同物质/生物/起始位置/环境 |
| 推理深度 | 1-3 步推理 | 3-15 步推理（需领域知识） |
| 领域知识 | 常识（厨房操作）| 科学知识（化学/物理/生物/遗传） |
| 最长 episode | 40 步 | 120 步 |
| Unseen generalization | 无（同分布测试）| 有（task-8, task-9 完全 unseen）|

---

## 3. 三环境对比表

| 维度 | ALFWorld | WebShop | ScienceWorld |
|------|----------|---------|--------------|
| **Action space** | 自然语言命令（~10 类动词） | 2 种：`search[q]` / `click[e]` | 25 个模板（~200K 组合/步） |
| **Observation format** | 房间文本描述 | 简化商品页面文本 | 房间+物体+背包文本描述 |
| **Episode 长度** | 固定 40 步 | 固定 10 步 | 按任务 10-120 步 |
| **Reward 类型** | Binary (0/1) | Continuous [0,1] 属性匹配 | Continuous [0,1] subgoal 完成度 |
| **Reward 记录** | 覆盖式 | 仅 done 时记录 | 取 episode 最高值 |
| **Train split** | 3,321 tasks | 1,000 sessions | 1,000 (task, variation) pairs |
| **Test split** | 134 tasks | 200 sessions | 410 pairs (247 seen + 70 unseen) |
| **Dev split** | 无 | 无 | 250 pairs |
| **环境安装复杂度** | 低（pip install alfworld）| **高**（web server + 搜索索引 + 数据）| 中（pip install + Java） |
| **外部依赖** | ai2thor, textworld | Flask, Pyserini, Java | Java (JRE 1.8+), py4j |
| **任务多样性** | 6 类 | 5 商品类别 | 30 类（10 课程主题）|
| **领域知识需求** | 低（家务常识）| 中（购物策略）| **高**（科学知识）|
| **Unseen 泛化测试** | 无 | 无 | 有（task-8, task-9）|
| **Preference 构建** | 成功 vs 失败（binary）| reward 大小比较（continuous）| golden=1.0 vs predicted（continuous）|
| **ETO 报告性能** | ~70% SR | ~63 avg reward | ~65.6 seen / ~55.5 unseen |

---

## 4. 错误分类 Taxonomy 适配分析

### 4.1 当前三分类回顾

在 ALFWorld 上定义的三分类：

| 错误类型 | 定义 | ALFWorld 示例 | 纠正跨度 |
|----------|------|--------------|----------|
| **Action Error** | 单步执行错误，策略正确 | 拿错物体、去错容器 | ~1 步 |
| **Verification Error** | 未检查前提/结果，错误级联 | 未发现 "Nothing happens"、重复失败动作 | ~2-4 步 |
| **Planning Error** | 根本策略错误 | 跳过必要子任务、误解目标 | ~5-15 步 |

### 4.2 WebShop 适配

**三分类可直接适用**，但具体表现不同：

| 错误类型 | WebShop 表现 | 示例 |
|----------|-------------|------|
| **Action Error** | 点击错误元素 | 选了错误的 size/color 选项、点了错误的商品 |
| **Verification Error** | 未核实属性匹配 | 未检查价格是否满足预算、未确认所有属性匹配就 Buy |
| **Planning Error** | 搜索策略错误 | 搜索关键词太宽泛/太窄、没有 refine search、盲目浏览不比较 |

**WebShop 特有模式**:
- **Premature Buy**: 未充分比较就购买（Verification → Planning 边界模糊）
- **Search Failure**: 搜索词不匹配任何好商品（Planning Error）
- **Partial Match**: 选了属性部分匹配的商品（可能是 Action 也可能是 Planning）

**适配难点**: WebShop 只有 10 步，episode 极短。Planning Error 和 Verification Error 的边界更模糊——一个错误的搜索可能直接导致整个 episode 失败，很难区分是 "策略错" 还是 "搜索词选择错"。

### 4.3 ScienceWorld 适配

**三分类可直接适用**，且比 ALFWorld 更自然：

| 错误类型 | ScienceWorld 表现 | 示例 |
|----------|------------------|------|
| **Action Error** | 操作错误对象/动作 | `pour blue_paint into red_paint`（应该是 yellow_paint）、`teleport to kitchen`（应该去 workshop） |
| **Verification Error** | 未确认操作结果 | 没检查混合是否成功、没读温度计读数、没确认植物是否在生长 |
| **Planning Error** | 实验方案错误 | 做三原色混合时顺序错误、忘记连接电路再测导电性、不知道需要先加热再测熔点 |

**ScienceWorld 特有模式**:
- **Domain Knowledge Gap**: 缺少科学知识导致的 Planning Error（不知道绿色 = 蓝 + 黄）
- **Multi-step Verification**: 某些任务需要多次验证（如测量两个物质的熔点做比较），漏掉一次就是 Verification Error
- **Resource Management**: 用完了关键材料但没完成任务（Planning Error 的变体）

**适配优势**: ScienceWorld 的长 episode（最长 120 步）使三分类的纠正跨度区分更清晰。Action Error (1步) vs Verification Error (2-5步) vs Planning Error (10-50步) 的差异更明显。

### 4.4 Taxonomy 适配结论

| 问题 | 回答 |
|------|------|
| 三分类是否通用？ | **是**，三个环境都有明确的 Action/Verification/Planning 错误 |
| 需要新增分类？ | **暂不需要**。WebShop 的 "Premature Buy" 和 ScienceWorld 的 "Domain Knowledge Gap" 可归入现有分类 |
| 需要修改分类定义？ | **需要微调**。每个环境的具体判据不同，但三分类框架不变 |
| 分类 prompt 需要适配？ | **必须适配**。需要针对不同环境的 action space 和 observation format 修改判据和示例 |

### 4.5 γ_e 映射的跨环境考虑

| 环境 | Action γ_e | Verify γ_e | Plan γ_e | 理由 |
|------|-----------|-----------|---------|------|
| ALFWorld (40步) | 0.85 | 0.92 | 0.97 | 基准设定 |
| WebShop (10步) | 0.80 | 0.88 | 0.95 | episode 短，需要更强的 credit 集中 |
| ScienceWorld (10-120步) | 0.85-0.90 | 0.92-0.95 | 0.97-0.99 | episode 长度变化大，可能需要按 task 类型动态调整 |

**WebShop 特殊考虑**: 只有 10 步，φ(t,T) 的 discount 效果较弱（T 太小）。可能需要更激进的 γ_e 设置，或者考虑步级别的 credit 而非 turn 级别。

**ScienceWorld 特殊考虑**: max_steps 从 10 到 120 变化巨大。同一个 γ_e=0.97 在 T=10 和 T=120 下 discount profile 完全不同。可能需要 γ_e 根据 T 做归一化，或者用 `φ(t,T) = (T-t)/T` 线性 decay 替代指数 decay。

---

## 5. ETADN 扩展实施建议

### 5.1 优先级排序

1. **ScienceWorld 优先**：安装简单（pip + Java），代码改动小（与 ALFWorld 结构最相似），且有 unseen task 泛化测试（论文亮点）
2. **WebShop 其次**：环境搭建复杂，但 continuous reward 为 preference 构建提供更丰富的信号

### 5.2 代码改动量估算

| 改动 | ScienceWorld | WebShop |
|------|-------------|---------|
| Env wrapper 适配 | 0.5 天（已有 ETO 代码）| 1 天（需搭建 web 服务）|
| Task loader | 0.5 天 | 0.5 天 |
| Error classifier prompt | 1 天（30 类任务需覆盖）| 0.5 天（action space 简单）|
| Preference 构建 | 0.5 天（continuous reward）| 0.5 天 |
| 环境安装 | 0.5 天 | **2 天**（web server + 数据索引）|
| **合计** | **3 天** | **4.5 天** |

### 5.3 风险点

- **WebShop 环境稳定性**: Flask server + Pyserini 在 AutoDL 上可能有端口/内存问题
- **ScienceWorld Java**: AutoDL 可能需要手动装 JRE
- **ScienceWorld episode 长度差异**: T=10 到 T=120 对 DMPO discount 函数的影响需要额外实验
- **WebShop continuous reward**: preference pair 构建的 win/loss 阈值需要调参（reward 差多少算 "更好"？）
