# HarnessX: 可组合、自适应、可进化的 Agent Harness 铸造厂

**深度调研报告**

---

## 论文信息

- **全称**: HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry
- **arXiv 编号**: 2606.14249
- **发表日期**: 2026 年 6 月 12 日
- **作者**: Tingyang Chen, Shuo Lu, Kang Zhao 等 14 位作者
- **团队**: Darwin Agent Team
- **机构**: 小米 (Xiaomi)
- **代码**: [GitHub - Darwin-Agent/HarnessX](https://github.com/Darwin-Agent/HarnessX)（MIT 许可，Beta v0.1.0）

---

## 一、核心问题

AI Agent 的性能不仅取决于模型本身，还严重依赖 **runtime harness**——即介于模型和环境之间的 prompts、tools、memory、control flow 等运行时基础设施。

三个痛点：

1. **Harness 手工制作且静态**：每换一个模型或任务，都需要重新搭建脚手架，无法复用
2. **执行轨迹浪费**：Agent 执行过程中产生大量丰富的 traces，但几乎从未被系统性地蒸馏回来用于改进
3. **Harness 和模型脱节优化**：
   - **Scaffolding ceiling**：harness 已暴露最优工具和上下文，但冻结模型的推理能力无法进一步利用
   - **Training-signal ceiling**：如果 harness 从不暴露某些能力，模型永远学不到

**HarnessX 的核心主张**：Agent 的进步不必只依赖模型 scaling，系统性地组合和进化 runtime interface 是一个可操作的、互补的杠杆。

---

## 二、技术架构

### 2.1 形式化定义

Harness = **(M, C)**

- **M (ModelConfig)**: 模型配置——provider 路由、fallback 机制、per-role 模型分配
- **C (HarnessConfig)**: Harness 配置——完整行为管线（tools, memory, processors, tracing, sandbox）

### 2.2 Processor 抽象

每个 Processor 实现统一接口：

```python
async def process(self, event: Event) -> AsyncIterator[Event]
```

五种操作语义：**pass-through**（透传）、**transform**（变换）、**split**（分裂）、**intercept**（拦截）、**interrupt**（中断）。

挂载在 **8 个 lifecycle hook 点**上：

| Hook | 权限 |
|------|------|
| `task_start` | 允许修改 system prompt |
| `step_start` | 允许结构性历史编辑 |
| `before_model` | 允许修改最后一条 user message |
| `after_model` | 允许修改 response 内容和 tool call |
| `before_tool` | 允许修改 tool 输入，设置 approval flag |
| `after_tool` | 只读 |
| `step_end` | 只读 |
| `task_end` | 只读 |

元数据字段强制执行约束：`_singleton_group` 防止冲突重复、`_order` 控制顺序、`_after` 指定软依赖。

### 2.3 九维行为空间分类法

| 维度 | 内容 |
|------|------|
| D1: Model Selection | 模型选择和路由 |
| D2: Context Assembly | 上下文组装 |
| D3: Memory Management | 记忆管理 |
| D4: Tool Ecosystem | 工具生态系统 |
| D5: Execution Environment | 执行环境 |
| D6: Evaluation & Reward | 评估和奖励 |
| D7: Control & Safety | 控制和安全 |
| D8: Observability | 可观测性 |
| D9: Training Bridge | 训练桥接 |

### 2.4 组合代数（Substitution Algebra）

Harness 组合通过 typed builder operations 完成：

```python
builder | context | coding
```

类型安全的 hook-type contracts 在执行前强制检查一致性。

---

## 三、AEGIS: 自适应进化引擎

### 3.1 Operational Mirror（操作镜像）

关键洞察：将 **harness 进化映射为 MDP**：

- **States**: 当前 harness 配置 + 执行轨迹
- **Actions**: 类型化的编辑操作（typed edits）
- **Feedback**: 轨迹 + verifier 评分

论文预测了三种 RL failure modes 并在实验中验证：

1. **Reward Hacking**：利用 verifier 漏洞。被 Critic 检测并阻止
2. **Catastrophic Forgetting**：改进一组任务的编辑导致其他任务退化。被 seesaw constraint 防止
3. **Under-exploration**：偏向 prompt 微调而非结构性变更。被 Planner 干预解决

### 3.2 AEGIS 四阶段管线

#### Stage 1: Digester（消化器）

- 将每轮 **~10M tokens** 原始轨迹压缩为结构化 per-task summaries
- 每条 summary：outcome、failure category、implicated components、supporting evidence
- 维护 cross-iteration continuity

#### Stage 2: Planner（规划器）

- 从 summaries 构建 **adaptation landscape**（适应地图）
- 识别失败任务、已尝试的编辑、涉及的组件、**未尝试的编辑类型**
- 对抗 under-exploration 的主要防线

#### Stage 3: Evolver（进化器）

- 使用 typed builder operations 生成候选 harness 集合
- 为每个候选提供 **change manifest**：编辑了哪些组件、预期效果
- 对新 processor 代码执行 smoke tests

#### Stage 4: Critic & Gate（评审器与门控）

两层：

- **Critic**（LLM 驱动）：评估候选，检测 non-local effects，可发起**一次修订请求**
- **Deterministic Gate**（非 LLM）：顺序验收检查：
  1. Manifest completeness
  2. Configuration normalization
  3. Build/smoke tests
  4. **Seesaw constraint**：不允许在已通过的任务上产生退化

> **"a deterministic gate, not the model, decides what ships"**

### 3.3 Variant Isolation（变体隔离）

当异构任务需要相互矛盾的 harness 行为时，单一 harness 全局优化会陷入死锁。

解决方案：
- 维护最多 **K 个 harness 变体**
- 每个任务根据历史表现**路由到最佳变体**
- 编辑改善部分任务但退化其他时，**fork 新变体**而非放弃
- 效果：比 single-harness 方法**减少约 14% token 消耗**

---

## 四、Harness-Model 协同进化

### 4.1 双重天花板

两个天花板相互锁定：
- **Scaffolding ceiling**: harness 已最优，但冻结模型无法进一步利用
- **Training-signal ceiling**: 模型有潜力，但 harness 未暴露的能力学不到

协同进化通过**同时训练 harness 和模型**打破双重天花板。

### 4.2 迭代结构（7 步循环）

每轮 (M_t, H_t) → (M_{t+1}, H_{t+1})：

1. **Rollout**: 当前 (M_t, H_t) 执行任务，记录完整轨迹
2. **Verification**: verifier 将轨迹评分为标量 reward
3. **Buffer Insertion**: 评分轨迹连同 harness version identity 追加到 **Shared FIFO Replay Buffer**
4. **Harness Evolution**: AEGIS 读取 buffer 轨迹，提出离散编辑，通过验证后接受
5. **Behavior Log-probabilities**: M_t 下计算 token 级 log-probabilities 并缓存
6. **GRPO Update**: Cross-Harness GRPO 更新
7. **Advance**: 返回 (M_{t+1}, H_{t+1})

### 4.3 Shared Replay Buffer

核心数据结构：
- **FIFO 队列**，容量上限 C 条轨迹
- 每条轨迹携带：完整 trace、verifier reward、**harness version identity**
- Token-level log-probabilities **缓存到磁盘**复用
- FIFO eviction 限制 off-policy bias

### 4.4 Cross-Harness GRPO

核心算法创新——**task-level alignment without action-level alignment**：

- 来自**不同 harness 版本**的轨迹按 **task identity** 分组
- 每条轨迹在其**生成时的 harness** 下 replay
- Group-relative advantage：

```
A_hat(τ_i) = (r_i - μ(G_x)) / (σ(G_x) + ε)
```

G_x 汇集任务 x 的所有轨迹，**不论其生成时的 (M_k, H_k) 版本**。

**直觉**：进化中的 harness 充当 **structured exploration operator**——每个新版本向采样分布注入不同行为模式；模型 RL 更新向得分最高的模式 commit。

---

## 五、实验结果

### 5.1 设置

- **5 个 Benchmark**: GAIA、ALFWorld、WebShop、tau3-Bench、SWE-bench Verified
- **3 个模型族**: Claude Sonnet 4.6、GPT-5.4、Qwen3.5-9B
- **最多 15 轮进化**

### 5.2 主要结果

| 指标 | 数值 |
|------|------|
| 平均绝对增益 | **+14.5%** (across 15 configurations) |
| 最大增益 | **+44.0%** (ALFWorld + Qwen3.5-9B: 53% → 97%) |
| 最小增益 | **+1.1%** (tau3-Bench，接近天花板) |
| 改善配置数 | **14/15** |

**逆 Scaling 规律**：越弱的 agent 从 harness 进化中受益越大。9B 模型在 ALFWorld 上获得 44 点跳跃，模型完全未被触碰。

### 5.3 协同进化额外增益

在 harness-only 基础上额外 **+4.7%** 平均增益。

Qwen3.5-9B 在 GAIA 全流程：baseline 33.97% → harness evolution 47% → co-evolution **55.77%**（相对 +64%）。

### 5.4 计算成本

- GAIA recipe（103 tasks, 8 rounds）：**$1,519**
- 每个 benchmark：100-175M tokens
- 约 ~1,300 次任务执行后 amortize
- 协同进化需要 8 x H100 GPU

---

## 六、代码实现

### 6.1 仓库结构

```
HarnessX/
├── harnessx/       # 核心框架
├── benchmarks/     # 评估套件
├── recipe/         # RL 训练配方
├── examples/       # 使用示例
├── extensions/     # Skill 模块
├── frontend/       # React/TypeScript Lab UI
└── gateway/        # 消息网关服务
```

### 6.2 CLI

```bash
hx "Research prompt"          # 执行 agent 任务
hx -c config.yaml             # 加载 YAML 配置
hx lab                        # 启动 Web UI
```

### 6.3 SDK 最小示例

```python
model = ModelConfig(main=AnthropicProvider("claude-sonnet-4-6"))
harness = model.agentic(HarnessConfig())
result = await harness.run(BaseTask(description="What is 2 + 2?"))
```

### 6.4 Processor 分类

7 个类别：Context、Control（13 个安全/可靠性模块）、Evaluation、Memory、Multi-model、Observability、Tools

### 6.5 开发路线图

| 阶段 | 内容 |
|------|------|
| Phase 1（当前）| 核心管线、13 个 processors、multi-provider |
| Phase 2（进行中）| 贝叶斯优化、meta-harness、自动配置搜索 |
| Phase 3（计划）| 自进化、社区 marketplace |
| Phase 4（计划）| 多模态记忆、第三方集成 |

---

## 七、局限性

1. **成本高**：$1,519/recipe，前期投入大
2. **跨模型族泛化**未验证
3. **Operational mirror** 无法捕获 emergent behaviors
4. **Same-task-set evaluation**：缺少 held-out evaluation，无法声称泛化性
5. **Frontier model 依赖**：进化循环需要 frontier model 作为 meta-agent
6. **Reward hacking 风险**：harness 编辑可能利用 verifier 格式漏洞

> Alpha Signal 审慎提醒："harness edits and actual worker benefits are two different things"

---

## 八、对 MOSS 的启示

### 8.1 关键设计原则

1. **确定性门控优于模型判断**：最终 ship/不 ship 由规则而非 LLM 决定
2. **Seesaw constraint 是必要的**：不允许"进三退一"——已解决的问题不能退化
3. **变体隔离解决异构任务冲突**：不强迫一个 harness 适配所有任务
4. **协同进化打破双重天花板**：仅优化 harness 或仅优化模型都会触顶

### 8.2 与 Meta-Harness 的对比

| 维度 | Meta-Harness | HarnessX |
|------|-------------|----------|
| 搜索空间 | 单文件 Python 程序 | 类型化 Processor 组合 |
| 信息策略 | 不压缩，保留完整轨迹 | Digester 结构化压缩 |
| 安全机制 | 无显式防护 | Seesaw + Critic + Gate |
| 模型训练 | 不涉及 | Cross-Harness GRPO 协同训练 |
| 多任务处理 | 单任务搜索 | Variant Isolation 多变体路由 |
| Proposer | Claude Code 自由编码 | 类型化 builder operations |

### 8.3 MOSS 可借鉴的具体机制

1. **AEGIS 四阶段管线**（Digest → Plan → Evolve → Critic/Gate）可作为 MOSS 进化循环的参考框架
2. **Seesaw constraint** 应纳入 MOSS 的进化规则——防止已解决问题的退化
3. **Variant Isolation** 解决了我们讨论的"探索与利用"难题
4. **Shared Replay Buffer** 可以成为 MOSS 经验沉淀的具体实现
5. **九维行为空间分类法** 可以指导 MOSS 对 Harness 内容的系统化理解
6. **Processor 抽象 + Lifecycle Hooks** 提供了 Harness 内部组件的具体编程模型

### 8.4 MOSS 相对于 HarnessX 的差异化

HarnessX 是一个**框架**——它提供了组件和进化引擎，但需要人类选择 benchmark、定义 recipe、启动进化。

MOSS 的愿景更上一层：**自动发现需要什么 Harness、自动构建、自动测试、自动进化**。MOSS 的独特价值在于"任务入口→沉淀"的完整自循环，以及自举能力。HarnessX 的技术组件（AEGIS、Variant Isolation、Cross-Harness GRPO）可以成为 MOSS 内部的"组件"。

---

## Sources

- [arXiv Paper](https://arxiv.org/abs/2606.14249)
- [arXiv HTML Full Text](https://arxiv.org/html/2606.14249v1)
- [GitHub - Darwin-Agent/HarnessX](https://github.com/Darwin-Agent/HarnessX)
- [Alpha Signal Analysis](https://alphasignalai.substack.com/p/harnessx-turns-the-agent-harness)
- [VentureBeat Coverage](https://venturebeat.com/orchestration/xiaomis-harnessx-rewrites-its-own-ai-scaffolding-mid-task-and-smaller-models-gain-the-most)
- [HuggingFace Papers](https://huggingface.co/papers/2606.14249)
- [Moonlight Review](https://www.themoonlight.io/en/review/harnessx-a-composable-adaptive-and-evolvable-agent-harness-foundry)
