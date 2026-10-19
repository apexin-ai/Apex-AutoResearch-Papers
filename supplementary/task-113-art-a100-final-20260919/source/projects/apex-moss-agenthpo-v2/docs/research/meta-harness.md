# Meta-Harness: End-to-End Optimization of Model Harnesses

**深度调研报告**

---

## 论文信息

- **完整标题**: Meta-Harness: End-to-End Optimization of Model Harnesses
- **arXiv ID**: 2603.28052
- **发布日期**: 2026 年 3 月 30 日
- **作者**: Yoonho Lee, Roshen Nair, Qizheng Zhang (Stanford), Kangwook Lee (KRAFTON), Omar Khattab (MIT), Chelsea Finn (Stanford)
- **实验室**: Stanford IRIS Lab
- **项目主页**: https://yoonholee.com/meta-harness/
- **代码仓库**: https://github.com/stanford-iris-lab/meta-harness (1.2k stars, MIT License)

---

## 一、核心问题

LLM 系统的性能不仅取决于模型权重，还高度依赖于 **harness**（模型外壳/脚手架）——即决定存储什么信息、检索什么信息、以何种方式呈现给模型的那套代码。论文指出，仅改变 harness 而保持模型不变，同一 benchmark 上的性能差距可达 **6 倍**。

然而，harness 的设计目前仍主要依赖人工手动迭代。现有的文本优化器（text optimizers）表现不佳，核心原因是：**它们对反馈信息的压缩过于激进**。

论文通过关键对比表量化了这个差距：

| 方法 | 历史记录 | 日志内容 | 每次迭代上下文 |
|------|---------|---------|-------------|
| OPRO | 滑动窗口 | Score pairs | 0.002M tokens |
| TextGrad | 仅上一轮 | Textual feedback | 0.015M tokens |
| AlphaEvolve | 滑动窗口 | Program DB + scores | 0.022M tokens |
| **Meta-Harness** | **完整历史** | **所有日志/分数** | **10.0M tokens** |

Meta-Harness 每次迭代可处理的上下文量是现有方法的 **100-500 倍**。

---

## 二、技术方法详解

### 2.1 形式化定义

```
H* = arg max_H E_{x~X, τ~p_M(H,x)} r(τ, x)
```

- **H** 是一个 harness（包裹 LLM 的有状态程序）
- **M** 是固定的基座模型（frozen LLM）
- **X** 是任务分布
- **τ** 是执行轨迹（execution trajectory）
- **r(τ, x)** 是奖励函数

关键：harness H 是 **可执行代码**（单文件 Python 程序），不是模板或提示词。

### 2.2 系统架构四大组件

1. **Fixed Model (M)**: 冻结的 LLM，优化过程不修改模型权重
2. **Task Distribution (X)**: 用于评估 harness 性能的问题实例集合
3. **Agentic Proposer (P)**: 使用 Claude Code (Opus 4.6) 作为编码代理，负责分析历史、诊断故障、提出新 harness 候选
4. **Filesystem Database (D)**: 完整的搜索历史文件系统，存储所有候选 harness 的源代码、评估分数和执行轨迹

### 2.3 搜索循环（Search Loop）

每一轮迭代：

1. **Proposer 查询文件系统**: 通过 `grep`、`cat`、文件导航自由浏览历史。中位数每次读取 **82 个文件**，引用超过 **20 个先前候选方案**
2. **生成 k 个新 harness 候选**: 基于历史分析写出新的 Python 程序。没有硬编码的进化算子，Proposer 完全自主决定修改什么
3. **接口验证**: 检查新候选是否满足基本接口要求
4. **评估**: 在 search-set 任务上运行，收集性能分数和执行轨迹。单次评估可产生高达 **10,000,000 tokens** 的诊断信息
5. **存储结果**: 代码、分数、轨迹存入文件系统
6. **循环重复**: 典型配置 20 轮迭代，约 60 个 harness 候选

### 2.4 核心设计原则：不压缩的诊断信息

与所有先前方法最本质的区别：

- **不做摘要**: 消融实验证明 LLM 生成的摘要反而损害性能（Scores-only: 34.6 → Scores + summaries: 34.9 → Full Meta-Harness: **50.0**）
- **文件系统作为记忆**: 不使用向量数据库或检索增强，直接让 coding agent 用终端工具浏览文件
- **Proposer 自主诊断**: 完全委托给 coding agent 决定如何诊断和修改

### 2.5 Proposer 的因果推理能力

论文展示了 TerminalBench-2 实验中 Proposer 的推理轨迹：

1. **Iteration 1-2**: 同时修改结构和提示模板，两次都导致回退
2. **Iteration 3**: 识别混淆因素——"Prompt template changes caused agent to delete necessary state"
3. **Iteration 4-6**: 测试状态机假设，持续观察到修改导致的回退
4. **Iteration 7**: 转向纯增量式修改（environment bootstrap），成为最佳候选
5. **Iteration 8**: 确立安全模式后，组合正交修复

展示了 Proposer 在形成和测试**因果假设**，而非随机探索。

---

## 三、实验结果

### 3.1 在线文本分类

- Meta-Harness: **48.6%** 平均准确率 vs ACE 的 40.9%（**+7.7 点**）
- 上下文 token 用量：11.4K vs ACE 的 50.8K（减少 **4.4 倍**）
- 在 LawBench（215 个类别）上提升最大：**+16 个百分点**
- OOD 泛化：9 个未见数据集上 73.1% vs ACE 的 70.2%，6/9 获胜

**发现的关键行为**:
- **Draft-Verification**: 检索 5 个相似样本，草案预测，再检索确认者/挑战者验证
- **Label-Primed Query**: 预展示完整标签空间，提供每标签覆盖率

### 3.2 检索增强数学推理

- 在 5 个模型上平均提升 **4.7 个百分点**
- 发现了**四路词法路由器**（Four-Route Lexical Router），针对组合数学/几何/数论/代数各自使用不同检索策略

### 3.3 TerminalBench-2 代理编程

- Opus 4.6: **76.4%** 通过率，排名 **#2**
- Haiku 4.5: **37.6%** 通过率，排名 **#1**
- 发现了 **Environment Bootstrapping**: agent 循环开始前收集沙箱快照（OS、语言、工具、目录内容），注入初始 prompt

---

## 四、消融实验

| 配置 | 中位精度 |
|------|---------|
| Scores-only | 34.6 |
| Scores + LLM-generated summaries | 34.9 |
| **Full Meta-Harness** | **50.0** |

LLM 生成的摘要几乎没有帮助（仅 +0.3），原始执行轨迹的访问带来 **+15.4 点** 巨大提升。

---

## 五、代码实现

```
meta-harness/
  reference_examples/
    text_classification/
      claude_wrapper.py        # Proposer agent 封装
      meta_harness.py          # 主搜索循环
    terminal_bench_2/
      claude_wrapper.py
      scripts/run_eval.sh
  ONBOARDING.md                # 新领域接入指南
```

```bash
# 快速启动
cd reference_examples/text_classification
uv sync
uv run python meta_harness.py --iterations 1
```

默认使用 Claude Code (Opus 4.6) 作为 Proposer。

---

## 六、局限性

1. 单一 Proposer 依赖（仅测试了 Claude Code）
2. 单任务搜索，缺乏跨任务迁移
3. 单文件 Python 程序限制，多文件架构未支持
4. 计算密集（每次约 60 个 harness 候选）
5. 未报告优化过程的总 token 消耗
6. 原始轨迹摄入存在安全隐患

---

## 七、对 MOSS 的启示

### 7.1 核心范式验证

论文用硬数据证明了 **"优化模型周围的代码"可以产生与"优化模型本身"同等甚至更大的收益**。Harness 变化可造成 6 倍性能差异。这直接验证了 MOSS 的核心假设。

### 7.2 文件系统作为优化记忆

Meta-Harness 不使用向量数据库或复杂知识图谱，而是用**普通文件系统**存储所有历史信息，让 coding agent 自行决定读取什么。这种极简但高效的设计说明：MOSS 的数据层不需要复杂基础设施，只需要有组织的文件结构。

### 7.3 不压缩原则

**最重要的实证发现**：摘要和压缩是有害的。对 MOSS 来说，这意味着应保留完整的执行历史和轨迹，让 agent 自己 grep 出需要的信息，而不是预先压缩。

### 7.4 Harness 是代码

Harness 以可执行 Python 程序形式存在，不是配置文件。这强化了我们调研后的判断——MOSS 的 Harness 核心部分应该是代码。

### 7.5 Proposer Agent 的能力上限

系统的天花板直接取决于底层 coding agent 的能力。MOSS 应设计为**可插拔的**，随时替换更强的基座 agent。

### 7.6 自指结构

Meta-Harness 本身就是一个 harness（管理 Proposer agent 的信息输入），用来发现更好的 harness。这种**自指（self-referential）**结构是实现真正自进化系统的基础模式。

---

## Sources

- [arXiv Paper](https://arxiv.org/abs/2603.28052)
- [arXiv HTML Full Text](https://arxiv.org/html/2603.28052v1)
- [GitHub Repository](https://github.com/stanford-iris-lab/meta-harness)
- [Project Page](https://yoonholee.com/meta-harness/)
- [Hugging Face Blog](https://huggingface.co/blog/Svngoku/meta-harness-end-to-end-optimization-of-model)
- [NerdHeadz Analysis](https://www.nerdheadz.com/blog/stanford-just-proved-what-weve-been-saying-its-the-harness-not-the-model)
- [Emergent Mind](https://www.emergentmind.com/papers/2603.28052)
