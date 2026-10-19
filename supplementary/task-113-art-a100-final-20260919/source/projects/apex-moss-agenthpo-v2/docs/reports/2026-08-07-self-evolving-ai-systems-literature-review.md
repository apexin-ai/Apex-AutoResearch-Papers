# Self-Evolving AI Systems 文献综述与 Moss 研究定位

日期：2026-08-07  
文档性质：面向论文选题与实验设计的研究综述  
证据截止：2026-08-07 可公开获取的论文、预印本、官方仓库与 Moss 已封存实验

## 0. 执行摘要

Self-Evolving AI 不是一个单一算法族，而是一个系统问题：系统利用自己的轨迹、环境结果或评测反馈，
持久地修改会影响后续行为的状态。这个状态可以位于模型权重、Prompt、Memory、Skill、Tool、Workflow、
完整 Agent/Harness 代码、Evaluator，甚至任务与环境中。

对 Moss 最重要的结论有七点：

1. **“自进化 Agent”“Skill 进化”和“自进化 Harness”不是互斥概念。** Agent 是系统整体；Harness
   是模型外部控制层；Skill 通常是 Harness 可加载的程序性知识单元。比较工作时必须看实际修改的
   artifact，而不能只看作者采用的名称。
2. **mentor 对 Meta/Living/Moss 的方向判断基本正确。** Meta-Harness 主要做面向一个任务分布的开放
   Harness 程序搜索；Living-Harness 主要演化跨 episode 的 Memory 与 State Graph；Moss 在当前
   instance 的每个反馈轮后重编译角色、记忆/工具路由、Workflow、父代、Scheduler 和 Recovery。
   但 Living 的 State Graph 会改变程序性路径，不能降格为“只有普通 Memory”；Moss 的架构修改也
   发生在可信组件语言内，而不是任意代码空间。
3. **Penguin 更接近 Agent-State/Skill 层优化。** 它修改 `AGENTS.md`、focused Skill 和有限安全配置，
   在整个冻结 Benchmark 上严格变好才接受，否则回滚。称它为 Skill-only 不够准确，但它也不是
   Meta-Harness 式完整 Harness 代码搜索。
4. **Moss 不能把“双层 Harness”“直接修改 Harness”“typed Harness evolution”“test-time evolution”、
   “跨 Benchmark”或“可信可审计优化”单独宣称为首创。** ADAS、AFlow、DGM、Meta-Harness、AHE、
   HarnessX、TTHE、Self-Harness、VeRO、MemoHarness、HarnessOpt-Bench 和 AgentStream 已分别覆盖这些
   主张的很大部分；EvoTest 与 HierFlow 还分别覆盖同一环境多 episode 的系统配置更新和 query-level
   workflow/topology search。
5. **Moss 当前最可防守的是一个较窄的技术组合：** 在冻结外部 evaluator 与可信执行边界内，对一个具体
   benchmark instance 做逐轮、合同化 Harness 架构重编译，并用 `A / B-frozen / B-online` 拆开一次性
   Harness、纯题内适应和额外跨题经验。TTHE 已有 batch reset/accumulate 消融，AgentStream 已有多种
   stream control，因此这里应称“更细粒度的单-instance 受控分解”，不能称绝对首次因果分解。
6. **当前证据支持完整题内 B-frozen 流程，不支持稳定跨题正迁移。** B-frozen 在 LCBench、CompilerGym
   和 SWE-bench 的分数或有效生成率上显示明确价值，但 Prompt/Skill/结构/额外 optimizer compute 尚未
   通过消融拆开；B-online 没有稳定超过 B-frozen。每套 suite 的
   后两题只对 Experience Bank 的跨题更新 sealed，仍允许当前题八轮 evaluator-feedback adaptation，
   所以它们应称为“允许题内适应的跨题迁移 holdout”，不是 evaluator-inaccessible 的完整 held-out test。
7. **存在直接命名冲突。** 2026 年 5 月已有论文
   [MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](https://arxiv.org/abs/2605.22794)，
   它会根据生产失败批次改写 Agent Harness 源码。正式投稿前最好更名；至少必须采用可区分的全称并在
   related work 中明确引用，不能把当前项目简称 `Moss` 当作唯一名称。

最推荐的论文主线是：

> **Where Does Harness Self-Evolution Help? A Controlled Study of Local Adaptation and Experience
> Transfer**。与其声称 Harness 会不断泛化，不如测量当前收益究竟来自题内适应流程还是跨题经验，
> 并展示一种把模型提案与可执行权限分开的闭世界、合同约束编译机制。标题暂不使用 `Moss`，直至完成
> 重命名或确定足够清晰的区分性全称。

---

## 1. 范围、方法与术语边界

### 1.1 文献范围

本文用三篇综述建立分类坐标，再回到代表工作的原论文或官方实现核验技术事实：

- [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve](https://arxiv.org/abs/2507.21046)
  已发表于 TMLR 2026，提供 `what / when / how / where / evaluation` 框架；
- [A Comprehensive Survey of Self-Evolving AI Agents](https://arxiv.org/abs/2508.07407) 从
  `System Inputs → Agent System → Environment → Optimiser` 闭环组织领域；
- [Self-Evolving Coding Agents](https://arxiv.org/abs/2608.03392) 给出 coding 场景下 framework、memory、
  skill/tool、model、workflow/topology 的对象分类。

2026 年 7–8 月出现了大量与 Moss 直接相邻的预印本。它们尚未经过同等强度的同行评审，本文会将
“作者报告的结果”与“可由其协议支持的结论”分开。PenguinHarness 是开源产品协议而不是论文，也按
官方固定 commit 分析。

### 1.2 Task、Benchmark 与 instance

本文沿用 Moss 的严格术语：

- `Task`：上游能力范围或目标分布；
- `Benchmark`：从 Task 抽出的有限测量集合；
- `Benchmark instance`：集合中的一道具体题。

在一个公开 Benchmark 上持续变好，只能先称 benchmark-conditioned improvement；在同分布 test split
上变好可支持 benchmark-distribution generalization；要声称 Task-level generalization，还需要独立来源、
环境或 Benchmark 的复制。

### 1.3 严格与宽松的 self-evolution 定义

把系统状态记为

\[
S_t=(\theta_t,P_t,M_t,K_t,W_t,\Gamma_t,J_t,E_t),
\]

分别表示模型权重、Prompt/Context、Memory、Skill、Tool、Workflow/Architecture、Judge/Evaluator 和
Environment/Curriculum。若轨迹为 \(\tau_t\)、反馈为 \(r_t\)，则自进化更新可写成

\[
S_{t+1}=F(S_t,\tau_t,r_t).
\]

严格口径至少要求：

1. 更新依赖系统自己的轨迹、执行结果或反馈，而不是与当前系统无关的普通离线数据处理；
2. 更新结果被持久保存，并会改变后续行为策略；
3. 系统能够自主提出、选择或提交更新，即使 evaluator 和权限边界由人预先冻结。

只把当前答案改写得更好、完成后不保留任何 policy-changing state，更适合称 inference-time refinement。
因此 Self-Refine 是重要前驱，Reflexion 是强题内适应机制，但它们不能自动支持“跨任务持续进化”。

---

## 2. Agent、Harness、Workflow、Memory 与 Skill 的关系

这些概念不是同一层级的互斥标签。一个实用的关系是：

```text
Agent system
├── Base model / policy
└── Harness（模型外部控制层）
    ├── Prompt / context construction
    ├── Memory write, retrieval, forgetting
    ├── Skills / SOPs / reusable procedures
    ├── Tools and permission surface
    ├── Roles, workflow and orchestration topology
    ├── Scheduler, retries and recovery
    └── Output validation, tracing and evaluator interface
```

| 概念 | 最有用的操作性定义 | 常见持久载体 | 不能仅凭什么判断 |
|---|---|---|---|
| Agent | 完成任务的决策系统整体，通常是 model + harness + runtime state | 代码、配置、状态目录 | 项目是否把目录命名为 Agent |
| Harness | 把基础模型变为可执行 Agent 的外部控制层 | Prompt、组件配置、workflow graph、完整程序 | 是否只有一个 system prompt |
| Workflow/Topology | 模型调用、角色、工具和验证步骤之间的控制与信息流 | DAG、状态机、代码、步骤列表 | 是否使用了多个 Agent 名称 |
| Memory | 记录“发生过什么”以及如何组织、检索、合并和遗忘 | 文本、向量库、知识图、experience graph | 是否把长文本塞入 context |
| Skill | 记录“遇到某条件应怎样做”的可复用程序性能力 | SOP 文档、typed contract、workflow template、代码/API | 文件是否叫 `SKILL.md` |
| Tool | 可执行动作或外部能力及其选择策略 | function/API、shell wrapper、tool registry | Agent 是否调用过固定工具 |

Skill 位于 procedural memory 与 executable tool 之间：纯自然语言 SOP 更像程序性 Memory；带 trigger、
输入输出 contract 的 Skill 是中间表示；可执行函数已经接近 Tool。Penguin 的 Agent State 包含 Skill 但
不止 Skill；GDPevo 的持久 artifact 明确是 Skill；Living 的 Memory + State Graph 是 bounded procedural
state；Moss 的直接 artifact 是结构化 Harness IR。

---

## 3. Self-Evolving AI 的七个正交维度

领域不适合只画一棵分类树。一个方法通常同时更新 Prompt、Memory 与 Skill，因此建议为每项工作标注
以下七个坐标。

### 3.1 进化对象：改了什么

| 进化位点 | 典型内容 | 代表工作 | 主要风险 |
|---|---|---|---|
| Model/Policy | 基础权重、adapter、reasoner、verifier | [STaR](https://arxiv.org/abs/2203.14465)、[Self-Rewarding LMs](https://arxiv.org/abs/2401.10020)、[Absolute Zero](https://arxiv.org/abs/2505.03335) | 自举偏差、训练成本、灾难性遗忘 |
| Prompt/Context | system prompt、demonstrations、上下文组装 | [ProTeGi](https://arxiv.org/abs/2305.03495)、[Promptbreeder](https://arxiv.org/abs/2309.16797)、[GEPA](https://arxiv.org/abs/2507.19457) | dev-set 过拟合、只改措辞而非行为 |
| Memory | episodic/semantic/procedural memory，检索和组织 | [Reflexion](https://arxiv.org/abs/2303.11366)、[ExpeL](https://arxiv.org/abs/2308.10144)、[A-MEM](https://arxiv.org/abs/2502.12110) | 错误经验固化、无界增长、检索干扰 |
| Skill/SOP | 可复用规则、procedure、Skill library | [Voyager](https://arxiv.org/abs/2305.16291)、[SkillWeaver](https://arxiv.org/abs/2504.07079)、[GDPevo](https://arxiv.org/abs/2608.03764) | 规则适用域不清、Skill 冲突或后门 |
| Tool | 工具创建、实现、文档、选择策略 | [CREATOR](https://arxiv.org/abs/2305.14318)、[CRAFT](https://arxiv.org/abs/2309.17428)、[AgentOptimizer](https://arxiv.org/abs/2402.11359) | 代码执行权限、工具污染、不可验证副作用 |
| Workflow/Architecture | roles、nodes、edges、控制流、多 Agent topology | [Symbolic Learning](https://arxiv.org/abs/2406.18532)、[ADAS](https://arxiv.org/abs/2408.08435)、[AFlow](https://arxiv.org/abs/2410.10762) | 巨大搜索空间、成本、归因困难 |
| Full Harness/Framework | Prompt、工具、memory、middleware、recovery 与完整代码 | [DGM](https://arxiv.org/abs/2505.22954)、[Meta-Harness](https://arxiv.org/abs/2603.28052)、[AHE](https://arxiv.org/abs/2604.25850) | benchmark hacking、代码安全、版本可复现性 |
| Evaluator/Verifier | judge、reward model、test generator | [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666)、[Meta-Rewarding](https://arxiv.org/abs/2407.19594)、[V-STaR](https://arxiv.org/abs/2402.06457) | actor–judge 共错、reward hacking |
| Environment/Curriculum | 任务、环境、难度、奖励函数 | [POET](https://arxiv.org/abs/1901.01753)、[PAIRED](https://arxiv.org/abs/2012.02096)、[OMNI-EPIC](https://arxiv.org/abs/2405.15568) | curriculum 漂移、只学会生成易题 |

### 3.2 适应时间与目标粒度：何时、为谁而改

| 时间尺度 | 目标 | 例子 | 需要回答的问题 |
|---|---|---|---|
| 当前 trajectory 内 | 当前一步或当前回答 | Self-Refine、部分 ReAct/Reflexion | 改善是否在 episode 结束后消失？ |
| 当前 instance、轮间 | 同一道题、游戏或 query 的后续尝试 | EvoTest、HierFlow、Moss B-frozen | 是 solution retry 还是系统结构真的改变？ |
| 当前 test batch 内 | 同一批无标签输入 | TTHE | 分数是 transductive specialization 还是 forward transfer？ |
| 跨 instance online | 后题使用前题经验 | Living-Harness、Moss B-online | 是否严格 score-before-update、是否遗忘旧能力？ |
| Train/dev batch 后冻结 | 目标任务分布 | GEPA、ADAS、AFlow、Meta-Harness | 是否有真正不可见的 held-out？ |
| Lifetime/continual | 长期部署流 | Voyager、AgentStream 所测方法 | retention、安全与成本是否随时间退化？ |
| Population/open-ended | 多 lineage、环境或 species | POET、Promptbreeder、DGM | novelty 是否真正产生 stepping stones？ |

“题内专用化”和“过拟合”也必须分开：专用化是优化目标；只有当产物离开优化实例或优化题集后失效，
才能据此判断过拟合。Moss B-frozen 有意追求 instance specialization，因此它的主要问题不是“是否专用”，
而是相同预算下是否比只改 solution、Prompt 或 Skill 更有效。

### 3.3 持久化载体

同一句“记住经验”可能表示：把 critique 留在当前上下文、写入外部文本、建立 knowledge graph、生成
Skill contract、写工具代码、提交完整 Agent code，或保存 population archive。载体决定可执行性、可迁移性、
可撤销性和攻击面，必须在实验表中显式记录。

### 3.4 反馈信号

- 程序化与可执行反馈：测试、编译器、环境终态、性能计时；
- scalar score 或 binary correctness；
- 自然语言 critique、完整 execution trace；
- gold demonstration、human preference、LLM-as-a-Judge；
- novelty、learning progress、regret 或多目标 Pareto score。

反馈越丰富不代表越可信。Meta-Harness 证明 raw traces 对搜索很有价值；Moss 使用 suite-specific evaluator
和原因码；GDPevo `reflect-3` 只暴露 train-side `score/correct`。公平比较需要冻结可见信息，而不只是
冻结模型名称。

### 3.5 更新算法

主要机制包括 verbal reflection、规则抽取、retrieval/consolidation、SFT/RL、textual gradient、beam/MCTS、
evolutionary population、program synthesis/code editing 与 co-training。进化对象与算法是两条轴：同一个
evolutionary algorithm 可以搜索 Prompt、Skill、Workflow 或完整代码；同一个 Harness IR 也可以由局部搜索、
MCTS 或 Builder 模型生成。

### 3.6 可修改权限与可信边界

可以把权限从窄到宽排列为：

```text
文本指令
→ 持久 Memory/Skill
→ allowlisted component composition
→ 受限工具代码
→ 任意 workflow/harness code
→ 修改自身 optimizer/model/evaluator
```

开放空间表达力更强，但不等于更可靠；约束空间更可审计，也不等于搜索算法更先进。应同时报告：

- evaluator、task contract、model、budget 是否冻结；
- 候选是否在 sandbox 中执行；
- 是否保留版本、parent、trace 与 provenance；
- 是否有 accept gate、rollback、stale-state removal 和 regression test；
- 中断调用如何计费，恢复是否可能偷偷重发。

### 3.7 证据矩阵

证据不是单向“等级阶梯”：跨 Benchmark、时间前传、长期保持与安全性回答的是不同问题。建议至少逐项
报告以下检查面，而不是用一个“泛化”标签替代：

| 证据面 | 回答的问题 |
|---|---|
| 同一道题后续尝试 | 当前 instance adaptation 是否有效？ |
| 同 Benchmark 未参与选择的 instances | 是否离开 optimizer 直接看过的样本？ |
| 新网站、仓库、环境或模型 | 是否在同 Task family 内换 source/backbone 后保持？ |
| 跨 Benchmark/domain | 机制或领域变化后是否复现？ |
| prequential forward transfer | 状态能否在看见新题反馈之前帮助下一题？ |
| retention/forgetting | 新经验是否损害旧能力？ |
| 安全、成本与长期稳定性 | 提升是否在风险与资源约束下可持续？ |

---

## 4. 研究发展脉络与代表工作

### 4.1 从答案反思到持久经验

[Self-Refine](https://arxiv.org/abs/2303.17651) 和 [Reflexion](https://arxiv.org/abs/2303.11366)
建立了“生成→反馈→再生成”的基本闭环。Reflexion 将 verbal reflection 放入 episodic buffer，已经具有
题内持久性；[ExpeL](https://arxiv.org/abs/2308.10144) 则从训练轨迹抽取可跨题检索的 insights。
这个阶段的主要可变对象仍是 Context/Memory，而不是执行架构。

### 4.2 从 Memory 到 Skill 与 Tool

[Voyager](https://arxiv.org/abs/2305.16291) 将通过环境验证的代码技能加入可复用 Skill library，并用
自动课程持续扩展能力。[CREATOR](https://arxiv.org/abs/2305.14318)、[CRAFT](https://arxiv.org/abs/2309.17428)
和 [AgentOptimizer](https://arxiv.org/abs/2402.11359) 分别探索当前任务工具合成、离线工具抽象与反馈驱动
function 更新。这里的核心变化是经验从“告诉模型怎么想”变成“提供可以调用的操作能力”。

### 4.3 从 Prompt 优化到 Workflow/Agent program search

[ProTeGi](https://arxiv.org/abs/2305.03495)、[OPRO](https://arxiv.org/abs/2309.03409)、
[Promptbreeder](https://arxiv.org/abs/2309.16797)、[TextGrad](https://arxiv.org/abs/2406.07496) 与
[GEPA](https://arxiv.org/abs/2507.19457) 把自然语言反馈变成 Prompt 的搜索或“梯度”。随后
[Symbolic Learning](https://arxiv.org/abs/2406.18532) 将 Prompt、Tool 和堆叠方式统一为 symbolic weights；
[ADAS](https://arxiv.org/abs/2408.08435) 让 meta-agent 直接编写 Agent code；
[AFlow](https://arxiv.org/abs/2410.10762) 用搜索优化代码表示的 workflow。这些工作已经覆盖
“上层优化器设计下层 Agent/Workflow”的基本双层结构。

### 4.4 从 Agent code 到完整 Harness evolution

[Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) 让 coding agent 修改自己的 Python code，
并用 archive 进行开放式分支搜索。[VeRO](https://arxiv.org/abs/2602.22480) 将版本、reward、trace 和
预算控制封装为“Agent 优化 Agent”的外层 Harness；[Meta-Harness](https://arxiv.org/abs/2603.28052)
让 coding proposer 读取全部历史 Harness 代码、分数和 raw traces，直接搜索完整 Harness 程序。

随后几项工作把 Harness 研究进一步细化：

- [Agentic Harness Engineering](https://arxiv.org/abs/2604.25850) 将可编辑组件、压缩后的证据和每次编辑的
  可证伪预测做成三种 observability；
- [MOSS: Source-Level Rewriting](https://arxiv.org/abs/2605.22794) 用生产失败批次驱动 Agent Harness
  源码改写，在临时容器回放后由用户授权替换生产容器，并以健康检查决定提交或回滚；
- [Self-Harness](https://arxiv.org/abs/2606.09498) 从 verifier-grounded 失败聚类提出 bounded edits，并以
  held-in/held-out regression gate 决定版本晋升；
- [HarnessX](https://arxiv.org/abs/2606.14249) 提出 typed primitives、substitution algebra、九维 Harness
  组合和 trace-driven AEGIS 多轮演化；
- [AutoRAS](https://arxiv.org/abs/2606.21445) 用 stack machine 将合法 symbolic primitive sequence
  确定性编译为 executable workflow，并联合优化效果、成本与鲁棒性；
- [TTHE](https://arxiv.org/abs/2607.08124) 在每个无标签 test batch 内以三分支、三轮开放代码搜索演化
  Harness，再由 judge 选择一个版本带到下一批；
- [MemoHarness](https://arxiv.org/abs/2607.14159) 在六维结构化 Harness 空间上离线搜索，再用双层
  Experience Bank 对未见 case 做一次性、无标签适配；
- [Living-Harness](https://arxiv.org/abs/2607.26598) 用固定 Evolution-SOP 在 episode 后更新 Memory 与
  State Graph；
- [Co-Harness](https://arxiv.org/abs/2607.22688) 交替优化 Harness 与模型权重；
- [HarnessOpt-Bench](https://arxiv.org/abs/2608.06301) 把端到端 Harness 优化定义为带真实 held-out、预算
  与可信执行边界的可比较能力。

因此，Moss 的论文必须针对这些最近工作定位，不能只和 Prompt/Memory 方法比较。

### 4.5 从单次结果到流式与因果评测

[AgentStream](https://arxiv.org/abs/2608.00155) 将 context、memory、skill、integrated harness 五种方法放入
Isolated、Sequential、Interleaved 三种任务流，在六个 Benchmark、三个模型上比较，显示没有一种方法
在所有模型与 stream 上占优。[GDPevo](https://arxiv.org/abs/2608.03764) 用 rule hybridization 从构造阶段
保证 `5 train → 5 held-out test` 的规则重组关系；[FinEvo-Bench](https://arxiv.org/abs/2608.06144)
在 120 个金融任务、三条全局交错流中为每个 scaffold 配对 state-reset control。

TTHE 还直接比较了跨 batch 累积与每批重置：作者在预选的 BIRD hard slice 上，以相同 `B10/G3/R3`
协议报告 50% 对 44%；该消融是一次完成运行，不宜外推成稳定效应。但每批 Harness 是在该批输入上
适配后再在同一批评分，论文明确称其为 transductive，并把
“先在下一批适配前评分”的 prequential forward-generalization 检验留作未来工作。这个边界与 Moss
positions 7–8 仍允许题内八轮反馈的问题高度相似。

这些工作说明：“覆盖多个 Benchmark”“有 static baseline”“有 interleaved stream”都已经不是充分的
新颖点。Moss 的剩余价值是把 TTHE 的 batch 级 reset/accumulate、AgentStream 的 stream 级 control
进一步缩到 **单个 instance**，并在冻结任务原生 evaluator 下比较题内 Harness 重编译与跨 instance
状态累计；这是更细的组合与证据粒度，而不是全新提出 reset/accumulate 思路。

---

## 5. 代表方法技术矩阵

| 方法 | 直接进化对象 | 主要尺度 | 搜索/更新空间 | 反馈 | 泛化或 held-out 边界 |
|---|---|---|---|---|---|
| Reflexion | verbal episodic memory | 当前题 retry | 文本反思 | score/critique | 主要是题内适应 |
| ExpeL | 跨题 insights/experience | train→test | 规则抽取与检索 | 成败轨迹 | 有独立 test tasks |
| Voyager | executable Skill library + curriculum | 长期 episode | 代码技能生成/验证 | 环境执行 | 新 Minecraft world/tasks |
| Promptbreeder / GEPA | Prompt 或多 Prompt program | train/dev search | population/reflection | score + trace | 搜索后在 test 上冻结评测 |
| Symbolic Learning | Prompt、Tool、stacking | batch/deployment | symbolic backprop | symbolic loss/trajectory | 标准与真实任务 POC |
| ADAS / AFlow | Agent code / workflow topology | task-distribution | 开放代码或 MCTS | Benchmark score | 同分布 test；ADAS 有跨域/模型 transfer |
| DGM | coding-agent 自身代码 | population/open-ended | 任意 Python code + archive | coding fitness + novelty | SWE-bench 与 Polyglot，仍偏 coding |
| EvoTest | Prompt、Memory、hyperparameter、tool routine | 同一游戏多 episode | configuration evolution + UCB | episode trajectory/return | 同一游戏内 test-time learning，不证明跨任务迁移 |
| HierFlow | task topology + subtask execution | ephemeral query-level test time | topology refinement + MCTS-like search | execution feedback | 当前 query 的临时 workflow，不跨 query 持久化 |
| Meta-Harness | 完整 Harness program | task distribution | 开放 Python code | search-set score + raw traces | 分类/数学有 held-out；TerminalBench-2 无 |
| AHE | Prompt、Tool、Middleware、Memory 等组件 | Benchmark 多轮 | 文件级可逆编辑 | trace、预测、score | 冻结后跨 SWE/模型 transfer |
| MOSS（Cai et al.） | 生产 Agent Harness 源码 | failure batch→deployment | 外部 coding CLI 改完整 source | failure replay + keypoint verdict | 同四题 pre/post；无独立 held-out |
| Self-Harness | declared Harness code surfaces | Benchmark 多轮 | verifier-grounded bounded edits | held-in trace + 双 split gate | held-out 参与每轮 promotion，不是 untouched final test |
| HarnessX | 九维 typed Harness primitives | 固定 task set 多轮 | substitution algebra | trace + verifier + gate | 五 Benchmark；同一 adaptation set，无 held-out |
| AutoRAS | symbolic primitives + workflow | learned conditional policy→per-query compile | stack-machine legal compilation | performance/cost/robustness | 四个 Benchmark、三个 domain；保证 primitive legality，无 authority threat model |
| TTHE | executable Harness code | 无标签 test batch 内及跨 batch | `G` 分支 × `R` 轮开放代码 | execution proxy + agentic judge | transductive；reset/accumulate 有消融，无 forward test |
| MemoHarness | 六维 Harness + Experience Bank | offline search + per-case adaptation | structured dimensions | search labels/trajectories | test case 无反馈、无额外搜索；选择性 transfer |
| Living-Harness | Episodic Memory + State Graph | 跨 episode online | schema-bounded repair state | score-before-update evidence | 跨 backbone reuse；无 held-out task family |
| PenguinHarness | `AGENTS.md`、Skill、有限配置 | frozen Benchmark candidate | Agent-State 文本/配置编辑 | full case matrix + traces | 同一 Benchmark 选择与报告，无独立 held-out |
| GDPevo | task-group Skill | `5 train → 5 test` | Skill/SOP 蒸馏 | self、gold 或三轮 judge | 24 组明确 held-out rule recombination |
| AgentStream Harness | Prompt + Memory + Skill | cross-task stream | 反思后状态编辑 | 当前 task trajectory | 六 Benchmark、多 stream；非题内清空状态 |
| HarnessOpt-Bench | 完整 executable Harness | dev/val search→test | 文件增删改 | graded feedback + fixed target-evaluation budget | evaluator-inaccessible held-out + trusted execution；optimizer inference 计量但未封顶 |
| **Moss** | typed `HarnessDecision` 编译产物 | 当前 instance 每轮；可选跨题 state | allowlisted roles/tools/memory/workflow/parent/scheduler/recovery | 冻结 evaluator score 与原因码 | 当前证据强在题内；跨题 holdout 方向混合 |

---

## 6. 与 Moss 最接近工作的详细比较

### 6.1 Meta-Harness：开放式 Harness 程序搜索

Meta-Harness 的上层 Coding Agent 可以读取文件系统中全部历史候选代码、分数和完整 execution traces，
再生成新的 Python Harness。候选可以修改 Prompt 构造、Retrieval、Memory、State update、Tool logic 和
Orchestration，搜索空间明显大于 Moss 的 Registry。

它的优化目标通常是一个 task distribution：每个候选在 search set 上整体评测，最终选择 Pareto frontier
中的 Harness 去跑 test；候选内部状态一般在 tasks 之间重置。分类和数学实验有 search/test 分离与跨模型
复用，TerminalBench-2 则在同一 89 题上搜索和终评，只有泄漏审计，没有独立 held-out。

因此准确对比是：

> Meta-Harness 在完整历史与开放代码空间中搜索一个面向目标分布的 Harness；Moss 在当前具体 instance
> 的每个反馈轮后，用受限 IR 重新编译下一版专用 Harness。

Moss 不能声称搜索空间更强；可以比较的是粒度、可信边界、预算和适应信号。

### 6.2 Living-Harness：Memory + State Graph 的跨 episode 修复

Living-Harness 冻结 tools、base context、domain rules 和人工设计的 domain-level Evolution-SOP。每个
episode 先使用旧状态执行并评分，再由 posterior generator、memory extractor 和 workflow extractor 将
证据写入：

- Episodic Memory：trigger、failure pattern、missing step、recovery action；
- State Graph：state node、repair edge、transition rule、critical check 和 commit gate。

这些结构会被检索并渲染为后续 Actor 可见的 procedural context，所以它不只是普通 Memory；但它也不
重写任意 Harness code，不更换 Tool 底座或完整角色拓扑。论文明确承认 Evolution-SOP 的 domain rules
由人工指定，尚未证明对未见 domain 的 zero-shot transfer；commit gates 也不提供完整 rollback、旧任务
regression suite 或 stale-entry removal。

Living 的强项是跨 episode 累积和跨 backbone frozen-state reuse；Moss 的强项是当前题内更直接地重配
角色、路由、Workflow、Parent、Scheduler 和 Recovery。当前 Moss 不能声称跨题迁移证据强于 Living。

### 6.3 PenguinHarness：Benchmark-conditioned Agent-State hill climbing

Penguin 的 [`agent-optimization` Skill v9](https://github.com/Prism-Shadow/penguin-harness/blob/047505dccc0cc16ad92be11011347d635f33ceb0/packages/skills/skills/agent-optimization/SKILL.md)
把当前最优 Agent State 作为 Reference。每轮从 Reference 修改 `AGENTS.md`、focused Skill 或安全配置，
在完整 frozen Case × Run matrix 上评测；只有总分严格提高才接受，否则从 snapshot 恢复。它允许用被拒
Candidate 的公开 traces 形成新假设，但不允许读取 private rubric/gold/evaluator state。

所以 Penguin 的核心是版本化 Agent State/Skill 优化，而非 Skill-only；同时其当前协议没有显式搜索完整
角色拓扑、Tool broker 和执行循环。选择、调参和最终报告使用同一 frozen Benchmark，没有独立 held-out，
“general change”主要是合同要求而不是泛化证据。

### 6.4 GDPevo：Skill induction 的 evolution-native benchmark

GDPevo 有 24 个 task groups、240 个任务，覆盖六个宏领域；每组共享一个业务环境并包含 `5 train + 5
held-out test`。其 rule hybridization 将企业 workflow 拆成 atomic rules，在训练题中分散暴露，再在测试题
重新组合，因此 held-out gain 的归因强于任意切分现成 Benchmark。

正式实验全部采用 Skill-based evolution：

- `self`：只读五个训练输入与环境，完成后一次性蒸馏 Skill；
- `fewshot`：另可读训练 gold answers；
- `reflect-3`：每个训练题的答案恰好接收三次 `score/correct`，五题结束后再蒸馏 Skill。

三个 independent Skill attempts 是实验重复，不是 Skill v1→v2→v3 谱系。测试时 Skill 冻结。论文报告
各模型/Harness 组合的 held-out 提升为 2.59–16.44 个百分点，但跨域 transfer 并不稳定：fewshot 的六个
off-diagonal 中五个为负，reflect 更稳但也非普遍正迁移。

GDPevo 的业务标签广、train/test 构造强，但多数任务共享“读取业务规则/记录→访问 API/DB→结构化
产物→规则评分”的交互范式。Moss 的三套 Benchmark 业务领域更少，却分别对应数值超参数搜索、LLVM
pass 序列组合和真实仓库 patch，动作空间与评分动力学更异质。两者是不同类型的广度，不能简单互相取代。

### 6.5 HarnessX、AHE 与 MemoHarness：最直接的 novelty 冲突

HarnessX 已明确提出 typed harness primitives、substitution algebra、trace-driven 多轮适应和 deterministic
acceptance gates，并在五个 Benchmark、最多 15 轮上报告结果。因此“类型化 Harness 组合/演化”本身
不能作为 Moss 的首创。其关键边界是每轮重评同一固定 task set，论文明确承认没有 held-out，peak score
带 selection bias；它优化的是 Benchmark/task-set 级 Harness，而不是为每个 instance 单独清空并维护谱系。

AutoRAS 进一步表明，“从合法 primitives 确定性编译 executable workflow”也不是新概念：它用
trajectory balance 与 textual gradients 学习条件 primitive-sequence policy，再由 stack-machine legality
mask 保证每个 query 的序列可编译。其 primitive alphabet 本身也是闭合空间；Moss 若要与之区分，重点
必须是 task-bound capability、provenance-bound operator、不可扩权、evaluator immutability 及明确的
authority/security threat model，而不是 `compiler` 或 `closed-world` 这两个名称本身。

AHE 已覆盖多组件文件化编辑、证据压缩、预测—结果配对、Git 版本/回滚，以及冻结后的跨 Benchmark、
跨模型 transfer。因此“可逆、可观测、会改 Middleware/Tool/Memory 的 Harness evolution”也不够独特。

MemoHarness 与 Moss 更接近：它把 Harness 分成 context、tool、generation、orchestration、memory、output
六维，维护 per-case + global pattern 双层 Experience Bank，并为每个 test case 生成专用 Harness。关键差异
是 MemoHarness 的 case adaptation 只读当前输入和冻结经验库，没有 test-time label、反馈或额外搜索；
Moss B-frozen 则可以从空跨题经验起步，在同一道题上利用 evaluator feedback 连续重编译八轮。

### 6.6 VeRO 与 HarnessOpt-Bench：可信优化基础设施冲突

VeRO 已提供 versioned snapshot、预算控制、结构化 trace 和 Agent-optimizes-Agent 的外层 Harness。
HarnessOpt-Bench 更进一步：开发/验证/测试严格分离，test 对 optimizer 不可见；target model、evaluator、
seed Harness 与 target-evaluation budget 固定；optimizer 自身 inference 在其实验中被计量但没有硬上限。
每个 Candidate 是不可变 commit，运行在可信隔离环境中，并保存版本供审计。

所以 Moss 不能泛称“首个有预算、版本、held-out 或审计的 Harness optimizer”。可能仍有差异的是 Moss
对外部调用中断的恢复语义：hash-chained append-only operation journal、started-without-artifact 永久计费、
原 operation ID 不重发、content-addressed receipts 与 trusted head 独立重放。但这应作为可验证的
crash-consistency 系统贡献，而不是一句笼统的“更可信”。

### 6.7 TTHE、Self-Harness、HierFlow 与 EvoTest：题内/测试时适应的直接冲突

[TTHE](https://arxiv.org/abs/2607.08124) 是当前与 Moss 时间尺度最接近的工作。它在每个无标签 test batch
中维护 `G` 条 Harness code 分支并演化 `R` 轮；主协议使用 `G=3, R=3`。Proposer 只读执行 trace 和
任务相关 proxy，agentic judge 从最后一轮分支中提交一个 Harness，并把它带到下一批。作者在其预选的
transductive hard slices 上报告提升，并做了两项相关机制验证：

- test-time 的直接 Harness code evolution 可以有效；
- reset-before-batch 与 accumulation-across-batches 可以被单独消融，不能把这个分解本身称为 Moss 首创。

但 TTHE 的评分是 transductive：Harness 在当前 batch 上适配，再在同一 batch 的 frozen hidden-gold
evaluator 上计分；gold 不进入 Proposer/Judge loop，适应只看 label-free traces/proxies。Moss 则把冻结的
task-native evaluator score/reason code 暴露给下一轮 Builder。Moss 的其他差异是适应单元更细到单个
instance、搜索空间是闭世界 Registry 而不是开放 Python code。这些是反馈可见性、粒度与权限的组合差异，
不代表搜索表达力更强，也不能误写成 TTHE 没有外部 evaluator。

[Self-Harness](https://arxiv.org/abs/2606.09498) 固定 model、evaluator、base tool set、budget 和 benchmark，
同时允许编辑 declared Harness 中的 instruction/tool/verification configuration surfaces。它从 held-in
verifier traces 聚类失败，提出 bounded Harness edits；候选必须至少改善一个 split，且 held-in
与 held-out 均不得下降，才能晋升。它已经覆盖 bounded edit、Harness lineage、regression gate 与审计记录。其
`held-out` 不向 proposer 暴露 trace，但每轮都参与 promotion gate，所以更准确地说是 regression split，
不是 evaluator-inaccessible final test。Moss 仍可区别于它的是：模型不能写新的 executable edit，而只能
输出 task-bound、capability-constrained 的组件决策；Moss 的账本也定义了外部调用中断后的保守恢复语义。

[HierFlow](https://arxiv.org/abs/2607.21609) 已把单 query 的 workflow generation 写成 training-free、test-time
topology–execution coupled search：上层根据下层执行反馈增删或修复拓扑，下层进行 MCTS-inspired code
search。它主要产生当前 query 的临时 workflow，不跨 query 保存持续谱系。因此“instance/query-conditioned
workflow topology search”不新；Moss 可比较的是不可覆盖的八轮 Harness lineage、跨题状态边界和
task contract/authority 隔离，而不是仅说“我们会改 Workflow”。

[EvoTest](https://arxiv.org/abs/2510.13220) 在同一个游戏的连续 episodes 间，由 Evolver 改写 Prompt、
deployment memory、hyperparameters 和 tool-use routines，并与 reflection、memory 与 online RL 比较。
所以“同一环境内根据前一轮轨迹更新整个 Agent configuration”已有先例。Moss 的额外价值需要来自：
task-bound executable contracts、reason-coded evaluator feedback、三种动作/评分机制复制，以及对题内与
跨题状态的严格隔离；不能把“有外部环境 reward”列为差异，因为 EvoTest 也使用 Jericho return 更新 UCB。

### 6.8 同名 MOSS：源码级生产 Harness 重写与命名冲突

[Cai et al. 的 MOSS](https://arxiv.org/abs/2605.22794) 与本项目处于同一研究领域，而且直接修改 Harness。
它从生产失败批次出发，用外部 coding-agent CLI 改写完整 Agent Harness source，在 ephemeral trial workers
中回放验证；候选经用户授权后做原地 container swap，health probe 失败则回滚。在 OpenClaw case study
中，同一 failure batch 完成一次 evolution cycle 后，四任务均分（每任务 3 trials）从 0.2526 提高到
0.6100；这不是三次独立 evolution runs。

两者的区别很清楚，但名称冲突不能忽略：

| 维度 | MOSS（Cai et al.） | 本项目 Moss |
|---|---|---|
| 修改面 | 完整生产 Harness source，开放代码空间 | `HarnessDecision` 选择 provenance-bound trusted operators |
| 反馈单元 | 一批生产失败；case study 同四题 pre/post | 单 instance 每轮任务原生 evaluator feedback |
| 部署目标 | 修复并替换 live Agent container | 可控 Benchmark 实验与可恢复谱系 |
| 可信机制 | trial replay、用户同意、health-probe rollback | task contract、closed-world compiler、外置 evaluator/权限、追加账本 |
| 泛化边界 | case study 无独立 held-out | 当前题内证据强；跨题 sealed 结果混合且非 evaluator-blind |

因此本项目不能再使用“首个 MOSS Harness self-evolution”叙事。正式论文应更名；若出于产品原因保留
`Moss`，也必须采用明确的区分性全称、在摘要首处消歧，并引用该论文。

---

## 7. Moss 的技术方案在 taxonomy 中的位置

### 7.1 直接进化对象

Moss Builder 输出严格 `HarnessDecision`，主要字段为：

```text
rule_id
role_graph
memory_views
tools
parent_strategy
workflow
scheduler_mode
recovery_mode
task directive
```

可信编译器把这些 ID 解析为已注册实现。Builder 可以选择组件，但不能提供可执行 Tool、Selector、Recovery
code 或 Workflow node；task contract、Evaluator、Budget 和 Adapter authority 在 Builder 之外冻结。
因此 Moss 确实修改 Harness 架构，而不只是给 Memory 增加一段文本，但它修改的是一个受限的、带类型的
operational architecture，不是任意 Harness 源代码。

### 7.2 两个时间尺度

```text
题内：round r 的 Harness + solution
  → frozen evaluator feedback
  → HarnessDecision r+1
  → trusted compiler
  → 当前 instance 的下一版 Harness

跨题：instance t 三臂全部封存
  → 只蒸馏 B-online 自身的公开轨迹
  → content-addressed Experience Bank
  → 只影响 instance t+1
```

- `A`：v001 构建一次 task-conditioned Harness，之后 Harness 冻结，但仍有相同数量的 solution attempts；
- `B-frozen`：当前 instance 内逐轮重编译，不读取任何前题经验；
- `B-online`：保留同样题内适应，并额外读取已封存前题的 Experience Bank。

这三个 arm 分别估计：一次性冻结 Harness、完整题内 B-frozen procedure 相对 A 的增量，以及 **在题内
适应开启条件下** 的跨题经验增量。它比把“使用 Memory 的方法”和“不用 Memory 的方法”直接比较更
接近受控拆分，但 B-frozen 同时增加 Planner/Builder compute，且还缺少
“Experience 开、当前题反馈关”的第四格，不能识别纯 cold-start transfer 及两种机制的交互。

### 7.3 正式实验证据

已封存 campaign 为 24 instances × 3 arms × 8 rounds = 576 rounds，覆盖 YAHPO Gym/LCBench、
CompilerGym cBench 和 SWE-bench Verified。完整数字见
[Moss Harness Builder 跨 Benchmark 三臂正式实验报告](./2026-08-06-harness-builder-cross-benchmark-final-report.md)。

| 观察 | 当前可以支持的结论 | 不能外推的结论 |
|---|---|---|
| 当前采样的 LCBench 8/8 instances 上，B-frozen 有效轮均值均高于 A | 完整 B-frozen 题内流程在该样本上方向一致 | 收益由结构变化而非 Prompt/反思/额外 compute 引起；任意 HPO Task 都会提升 |
| CompilerGym 双方有效的 6 题全部 B-frozen > A；并把 `crc32`、`blowfish` 从 A 的 0/8 恢复为 8/8 | 完整 B-frozen 流程可同时改善组合动作分数与合同有效性 | 已识别为 Harness architecture 的独立作用；优于所有 pass-sequence optimizer |
| SWE 中达到 4/8 的 instance：A 2/8，B-frozen 6/8 | 完整 B-frozen 流程主要提高当前 patch 生成的合规/可靠率 | 已证明结构因果作用；在 hidden/adversarial SWE 评分中提高解决率 |
| B-online vs B-frozen：学习题与每 suite 两个后位题方向混合；SWE paired gate 失败 | 跨题 Experience Bank 没有稳定正迁移 | 已证明 continual learning 或泛化 |

这些是当前封存报告的描述性结论。有效轮均值条件化在一个会被 arm 影响的 post-treatment 变量上，因此
不能单独作为因果 estimand；后续应并列报告 invalid 按预注册值计入的 intent-to-treat composite、validity
rate 与 conditional-on-valid score，并区分 cumulative/AUC、预承诺 final version 和仅供诊断的 oracle best。

正式账本记录 446 个 valid rounds、95 个 solution contract rejections、28 个 planner contract rejections，
并保存 6 个 terminal failure 与 2 个 started-without-result 的永久计费/不重发证据。它支持可靠恢复与
有效性分析，但不能替代算法对照。

### 7.4 “held-out”应如何精确表述

每套 suite 的 positions 7–8：

- 不再向 Experience Bank 写入，因此对 **跨题学习** 是 sealed；
- 但 B-frozen/B-online 仍能读取当前题的 evaluator feedback 并执行八轮 **题内适应**。

它测量的是：导入的前题经验，在双方都可进行当前题优化时是否带来额外优势。它不是 Meta/GDPevo 式
“冻结最终 artifact 后零更新测试”，更不是 HarnessOpt-Bench 式 evaluator-inaccessible test partition。
论文中建议使用：

> cross-instance-transfer holdout under allowed within-instance adaptation

并把真正的 evaluator-blind frozen-artifact test 作为新增实验。

---

## 8. Moss 可以与不可以主张什么

### 8.1 已经被相关工作覆盖、不能单独作为创新

- “首个 self-evolving Agent/Harness”；
- “首个双层 Builder→Agent/Harness 架构”；
- “首个直接修改 Harness 架构”；
- “首个 typed/composable Harness evolution”；
- “首个 test-time Harness evolution”或“首个同题/同环境多轮系统配置更新”；
- “首个用 trace/evaluator feedback 优化 Harness”；
- “首个有版本、回滚、预算或可信执行的 Agent optimizer”；
- “首个跨多个 Benchmark 或交错任务流评测自进化”；
- “首个 instance-specific Harness”，因为 MemoHarness 已做无反馈的 per-case adaptation；
- “首个把局部适应与跨批/跨题累积分开”，因为 TTHE 已做 reset/accumulate，AgentStream 已做 stream controls；
- “B-online 已证明稳定跨题泛化”。

### 8.2 当前最可防守的差异组合

> **Frozen-evaluator-feedback-driven, single-instance, inter-round Harness recompilation in a task-bound,
> closed-world component language, separated from cross-instance experience accumulation.**

这个定位的每个限定词都有作用：

- `evaluator-feedback-visible`：区别于 MemoHarness 的 zero-feedback adaptation；TTHE 虽由外部 gold 终评，
  但其适应循环只看 label-free traces/proxies；
- `single-instance/inter-round`：比 TTHE 的 batch-level adaptation 更细，并区别于 Meta、AHE、HarnessX 的
  task-set/Benchmark-level search；
- `Harness recompilation`：区别于只改答案、Prompt、Memory 或 Skill；
- `task-bound closed-world component language`：比单纯 `typed` 更准确，区别于开放代码自修改；
- `controlled decomposition`：在单 instance 粒度上估计题内流程与跨题累计的增量，但承认 TTHE/AgentStream
  的近似先例，也承认当前缺少第四格与 optimizer-compute matching。

但这一组合的论文新颖性仍需直接对照才能站稳，尤其是 Skill-only、Prompt-only 和 open-code optimizer。

---

## 9. Contribution 候选与证据审计

| 候选 Contribution | 新颖性判断 | Moss 当前证据 | 主要缺口/审稿风险 | 最小补强实验 |
|---|---|---|---|---|
| **C1. 逐 instance、逐反馈轮的可信 Harness 重编译** | 较窄的组合创新；EvoTest、HierFlow、TTHE 已覆盖相邻粒度，HarnessX 已覆盖 typed composition | 三类机制、576 rounds；B-frozen 相对 A 有明确改善 | 可能只是更强 Prompt/更多反思；没有同预算 Skill/Prompt/open-code 对照 | 同 tasks/model/evaluator/calls 下加入 Prompt-only、Skill/Agent-State、typed Moss；可选 open code |
| **C2. `A/B-frozen/B-online` 细粒度归因协议** | 有价值但非绝对首次；TTHE 有 reset/accumulate，AgentStream/FinEvo 有 stream control | 三臂同题、同八轮、严格 test-then-learn；清楚得到题内正、跨题不稳 | 缺“只开跨题经验、关闭当前题反馈”的纯迁移臂；单 lineage、suite 小 | fresh tasks 上做 2×2：当前题反馈开/关 × 跨题经验开/关；3 seeds 与 paired estimator |
| **C3. Contract-aware、Validity-aware 的题内流程** | 中等；AHE/HarnessX 已做 observability/gates，但 Moss 对 heterogeneous artifact contracts 更具体 | Compiler 与 SWE 的有效性恢复很明显；原因码与强制 `verify_contract` 有证据 | 可能只是 Prompt 中加模板；没有移除 contract operator/typed compiler 的消融 | 去掉 capability card、去掉 typed compile、仅在 Prompt 写模板三项消融 |
| **C4. 证据保全、at-most-once 的演化运行时** | 泛称审计已不新；精确中断语义可能有系统贡献 | hash-chain journal、trusted head、content-addressed receipts、永久计费/不重发均有真实故障证据 | 审稿人可能视为工程实现；尚无和 VeRO/HarnessOpt 的故障注入比较 | 故障注入：planner/solution/evaluator 各阶段 kill；证明不重复 operation/外部调用、预算守恒和确定恢复状态 |
| **C5. 跨题 Experience transfer 的受控负结果** | 作为实证发现有价值，不是正向算法贡献 | LCBench/Compiler 各一正一负 holdout；SWE 不可判定 | 只有每 suite 两题，且允许题内反馈；不能称 true held-out generalization | 两个低成本 suite 各 2 道 fresh held-out × 3 seeds，做 evaluator-blind cold-start 与 retention |
| **C6. 跨机制异质性下的统一编译接口** | 中等；AgentStream/HarnessX 覆盖更多 Benchmark，但动作空间未必如此异质 | HPO、LLVM pass、repo patch 共用 Builder/IR 与三臂合同 | 仅 8 instances/suite；不同 adapter 可能意味着统一性停留在接口层 | 先报告组件使用分布；再随机或匹配关闭字段/operator 做 ablation，才可估计字段作用 |

### 9.1 推荐的 Contribution 组合

不建议把六项并列。最合理的是“两个主贡献 + 一个实证结果 + 一个系统保证”：

1. **候选方法贡献：** 一种把模型提案与可执行 authority 分开的、task-bound closed-world Harness compiler；
   在完成组件对照与 capability-escape 红测前，不能把其相对 AutoRAS/HarnessX 的增量写成已确立结论；
2. **评测主贡献：** 在已有 reset/accumulate 研究之上，把一次构建、题内架构适应与跨题经验细化到单
   instance，并用新增 2×2 在当前 fresh-task 样本内估计纯迁移增量与交互；
3. **实证贡献：** 三种动作/评分机制中，完整题内 B-frozen procedure 改善分数或有效生成率，而跨题
   Experience transfer 尚不稳定；结构本身的独立作用留给 Prompt/Skill/component ablation；
4. **系统保证：** 给出 crash-consistent、budget-conservative、content-addressed、at-most-once
   provenance，而不是泛称“安全”或“exactly-once”。

### 9.2 最有论文价值的核心发现

当前数据实际上支持一个比“Memory 越积越多就越强”更有意思的结论：

> 在当前 24 题、单 lineage 设置中，可观测的正向收益主要来自完整 B-frozen 题内流程；前题经验
> 没有显示稳定增量。若不设 B-frozen，研究者很容易把这两种来源误归因于同一个“continual evolution”。

这可以成为 Moss 的中心 scientific question，而不是把 B-online 的混合结果视为单纯失败。

---

## 10. 建议新增的最小实验

### 10.1 优先级 P0：同台区分“改答案、改 Skill、改 Harness”

在两个成本较低且机制不同的 suite 上先做小规模直接比较，例如 LCBench + CompilerGym：

| Arm | 允许改变什么 | 保持冻结什么 |
|---|---|---|
| `solution-reflect` | 当前候选及题内 critique | Harness、Skill、工具/Workflow |
| `skill-state` | 当前题 Skill/AGENTS-like 指令 | 角色、Tool implementation、Workflow/Scheduler |
| `moss-typed` | 完整 `HarnessDecision` 组件 | trusted registry、evaluator、budget |
| `open-code`（资源允许时） | sandbox 内 Harness code | evaluator、model、task data、预算 |

要求相同 model、reasoning、可见反馈、solution calls、evaluator transactions、optimizer-side calls/tokens
和 wall-clock/GPU envelope，并用至少三条独立 lineage。若开放代码/typed arm 的优化器计算无法机械匹配，
则把 treatment 明确定义为“完整 procedure including compute”，同时报告 cost–quality frontier；不能只匹配
solution calls。这个实验决定 C1 是否真的来自 Harness architecture，而不是额外反思或更长 Prompt。

### 10.2 优先级 P1：少量 fresh held-out 上做完整 2×2

当前三臂缺少“导入跨题经验、但关闭当前题反馈”的纯 transfer arm。最小而信息量高的补充实验可以只用
两个低成本 suite（LCBench + CompilerGym）、每套两道 fresh held-out、三条独立 seed lineage：

| 当前 instance feedback | 前题 Experience | 解释 |
|---|---|---|
| 关 | 关 | cold-start + frozen-Harness repeated inference |
| 关 | 开 | Experience-initialized frozen-Harness repeated inference；纯跨题 transfer |
| 开 | 关 | 纯题内适应，等价于 fresh B-frozen |
| 开 | 开 | 两种机制叠加及交互，等价于 fresh B-online |

执行约束：

1. discovery tasks、Experience Bank 与所有超参数先冻结；instance-conditioned Builder 可以读取当前 task
   input/capability card，但不得看到 pool selection process、labels、reference artifacts、evaluator outcomes
   或尚未到释放时点的反馈；
2. 四臂的 v001 Harness 与对应 solution artifact 必须在任何 held-out evaluator 输出释放前全部提交；
   该时点提供严格可比的 prequential cold-start score；
3. `feedback=关` 两臂此后继续使用冻结 Harness，所有重复结束前都不暴露 evaluator 输出，也不能按分数
   选版本；`feedback=开` 两臂才允许预注册的八轮题内适应；
4. 四臂保持 model、reasoning、共同 seed/base artifact、solution attempts 与 evaluator transactions 可比；
   Experience treatment 可以使编译后的 v001 Harness 不同。用 sham/matched planner calls 匹配 optimizer
   compute，或明确 treatment 是包含额外计算的完整 adaptive procedure，并报告 cost-adjusted frontier；
5. task instance 是主要泛化/推断单位，seed nested within instance，八轮不能当成八个独立样本；四道
   fresh tasks 只是 exploratory pilot，应使用 paired/exact interval，不作 Task-level 显著性外推；
6. 对 `feedback=关` 两臂一次性解封评分；对适应臂逐轮记录协议允许的反馈，并完整报告无效候选、成本
   和置信区间；预注册 intent-to-treat composite（invalid 按协议计零/最低值）、validity rate 与
   conditional-on-valid score，避免只在 post-treatment 的 valid rounds 上条件化；
7. v001 只估计 Experience 的 cold-start effect；八轮 cumulative/AUC 或预承诺 final v008 用于估计
   feedback 主效应与 `Experience × feedback` interaction；`best` 依赖 oracle selection，只作为诊断指标。

这个小矩阵同时补上 TTHE 明确未做的、**相对于 evaluator labels 的** prequential/cold-start 检验；v001
仍可读取当前 task input，因此不能称完全 task-blind。它也把现有 positions 7–8 留在正确位置：
它们仍是“允许题内优化的跨题 Experience 增量测试”，不能替代 evaluator-inaccessible held-out。

### 10.3 优先级 P2：组件因果消融

至少做以下 ablation：

- 去掉 cross-instance memory；
- 只允许 directive/Prompt 改写；
- 固定 role/tool/workflow，只允许 parent/scheduler；
- 去掉 contract compatibility + `verify_contract`；
- 去掉 trusted compilation，保留同样文本指导；
- full Moss。

用 component activation、operational fingerprint 变化和下轮 outcome 建立 edit→effect 配对，避免只报告
最终分数。

### 10.4 优先级 P3：Retention、安全与恢复

- 在 B-online 后周期性重测早期 tasks，量化 forgetting；
- 对 Experience Record 做错误反馈、冲突 Skill、prompt-injection 与 provenance 缺失红测；
- 做 planner/solution/evaluator 不同阶段的故障注入与预算守恒证明；
- 报告总 token、evaluator、时间、有效候选和每单位提升成本。

[Do Self-Evolving Agents Forget?](https://arxiv.org/abs/2605.09315) 已显示 workflow、skill、model、memory
四条进化通道都会发生 capability erosion；[On Safety Risks in Experience-Driven Self-Evolving Agents](https://arxiv.org/abs/2604.16968)
还表明 benign experience 也可能强化“倾向执行”并降低高风险场景拒绝。Moss 的 trust boundary 只有在这些
测试中被测量，才能从工程约束升级为研究贡献。

---

## 11. 推荐论文叙事

### 11.1 一句话定位

> We study externally evaluated, single-instance Harness recompilation: a task-bound closed-world compiler
> turns typed model decisions into executable structure after each round, while controlled arms estimate
> incremental effects of local adaptation and cross-instance experience.

这里不再使用 `neglected timescale` 或 `first test-time Harness evolution`：EvoTest、HierFlow 和 TTHE 已覆盖
相邻时间尺度。可主张的是更细的单-instance 外部评测设置及完整的权限/归因组合。

### 11.2 推荐标题方向

- **Where Does Harness Self-Evolution Help? A Controlled Study of Local Adaptation and Experience Transfer**
- **Task-Bound Harness Recompilation across Heterogeneous AI-for-AI Tasks**
- **Typed Test-Time Harness Recompilation for Heterogeneous AI-for-AI Tasks**

第一项最符合当前证据，也最适合把 B-online 的负/混合结果转化为研究发现；在完成 §10.2 的 2×2、
optimizer-compute matching 和预注册推断前，不建议在标题使用 `causal`。由于已有同领域同名
`MOSS` 论文，三个标题暂时都不带项目名；正式命名应另行决定，而不是只改变大小写。

### 11.3 推荐摘要中的三项 claim

1. 我们提出一个受可信 Registry 约束的 Harness IR/Compiler，使 Builder 能逐轮重配角色、路由、Workflow、
   Parent、Scheduler 和 Recovery，而不获得任意可执行代码权限；
2. 我们在既有 batch/stream controls 上提出更细粒度的单-instance 三臂对照，区分一次性 Harness、当前
   instance 内 recompilation，以及在题内适应开启条件下的跨 instance Experience 增量；
3. 在 HPO、LLVM pass search 和真实 repo patch 三种机制上，完整的局部 B-frozen procedure 改善分数或
   有效生成率，但跨题状态没有显示一致增量；在结构消融完成前，不把 whole-arm gain 单独归因于架构。

在完成 P0 直接对照与真正 held-out 之前，不建议使用 `state of the art`、`general-purpose`、`first`、
`continually improves` 或 `generalizes across tasks`；无论是否更名，都应明确引用同名 MOSS、TTHE 与
Self-Harness。

完成 §10.2 的 fresh 2×2 后，第 2 条才可以升级为“识别纯跨题 cold-start transfer 及其与题内适应的
交互”；当前三臂数据本身不支持这个更强表述。

---

## 12. 参考资料

### 12.1 综述

- Gao et al. [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve](https://arxiv.org/abs/2507.21046), TMLR 2026.
- Zhang et al. [A Comprehensive Survey of Self-Evolving AI Agents](https://arxiv.org/abs/2508.07407), 2025.
- Feng et al. [Self-Evolving Coding Agents](https://arxiv.org/abs/2608.03392), 2026 preprint.

### 12.2 反思、Prompt、Memory、Skill 与 Tool

- Madaan et al. [Self-Refine](https://arxiv.org/abs/2303.17651), 2023.
- Shinn et al. [Reflexion](https://arxiv.org/abs/2303.11366), NeurIPS 2023.
- Zhao et al. [ExpeL](https://arxiv.org/abs/2308.10144), AAAI 2024.
- Wang et al. [Voyager](https://arxiv.org/abs/2305.16291), 2023.
- Fernando et al. [Promptbreeder](https://arxiv.org/abs/2309.16797), ICML 2024.
- Yuksekgonul et al. [TextGrad](https://arxiv.org/abs/2406.07496), 2024.
- Khattab et al. [GEPA](https://arxiv.org/abs/2507.19457), 2025.
- Qian et al. [CREATOR](https://arxiv.org/abs/2305.14318), EMNLP 2023.
- Yuan et al. [CRAFT](https://arxiv.org/abs/2309.17428), ICLR 2024.
- Zhang et al. [AgentOptimizer](https://arxiv.org/abs/2402.11359), ICLR 2024.

### 12.3 Workflow、Agent code 与 Harness

- Zhou et al. [Symbolic Learning Enables Self-Evolving Agents](https://arxiv.org/abs/2406.18532), 2024.
- Hu et al. [Automated Design of Agentic Systems / ADAS](https://arxiv.org/abs/2408.08435), ICLR 2025.
- Zhang et al. [AFlow](https://arxiv.org/abs/2410.10762), ICLR 2025.
- Zhang et al. [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954), ICLR 2026.
- [EvoTest: Evolutionary Test-Time Learning for Self-Improving Agents](https://arxiv.org/abs/2510.13220), ICLR 2026.
- Ursekar et al. [VeRO: A Harness for Agents to Optimize Agents](https://arxiv.org/abs/2602.22480), 2026 preprint.
- Lee et al. [Meta-Harness](https://arxiv.org/abs/2603.28052), 2026 preprint.
- Lin et al. [Agentic Harness Engineering](https://arxiv.org/abs/2604.25850), 2026 preprint.
- Cai et al. [MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](https://arxiv.org/abs/2605.22794), 2026 preprint.
- [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498), 2026 preprint.
- Darwin Agent Team. [HarnessX](https://arxiv.org/abs/2606.14249), 2026 preprint.
- [AutoRAS: Learning Robust Agentic Systems with Primitive Representations](https://arxiv.org/abs/2606.21445), ICML 2026.
- [TTHE: Test-Time Harness Evolution](https://arxiv.org/abs/2607.08124), 2026 preprint.
- Huang et al. [MemoHarness](https://arxiv.org/abs/2607.14159), 2026 preprint.
- [HierFlow: Coupled Hierarchical Search over Topology and Execution for Agentic Workflows](https://arxiv.org/abs/2607.21609), 2026 preprint.
- Du et al. [Living-Harness](https://arxiv.org/abs/2607.26598), 2026 preprint.
- Chen et al. [Co-Harness](https://arxiv.org/abs/2607.22688), 2026 preprint.
- Ursekar et al. [HarnessOpt-Bench](https://arxiv.org/abs/2608.06301), 2026 preprint.

### 12.4 自进化 Benchmark、流式评测与开源协议

- Yan et al. [AgentStream](https://arxiv.org/abs/2608.00155), 2026 preprint.
- Zhou et al. [GDPevo](https://arxiv.org/abs/2608.03764), 2026 preprint；
  [官方数据与评测固定快照](https://github.com/Prism-Shadow/GDPevo/tree/0999c0d1e6f59b1cb8464cac4e5ed856b5dcb9e4).
- FinEvo-Bench Team. [FinEvo-Bench](https://arxiv.org/abs/2608.06144), 2026 preprint.
- Prism-Shadow. [PenguinHarness 固定快照](https://github.com/Prism-Shadow/penguin-harness/tree/047505dccc0cc16ad92be11011347d635f33ceb0), 2026.
- [Moss Harness Builder 跨 Benchmark 三臂正式实验报告](./2026-08-06-harness-builder-cross-benchmark-final-report.md), 2026-08-06.
