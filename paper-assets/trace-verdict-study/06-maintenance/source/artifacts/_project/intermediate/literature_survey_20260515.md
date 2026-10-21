# Trace-Verdict-Study 文献调研报告

日期：2026-05-15

---

## 方向 1: Trace SFT / Trace-augmented LLM Training 全景

除已知工作外，找到 8 篇直接相关工作：

| # | 标题 | 会议/年份 | 核心做法 | 与我们的关系 |
|---|------|----------|----------|-------------|
| 1 | **SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning** | NeurIPS 2024 | 训练 Code LLM 用自然语言逐行描述控制流和变量状态（"execution monologue"），在全量可执行 Python 上做 SFT | trace-as-text SFT 的代表性工作，关注"模拟执行"而非分类 |
| 2 | **NExT: Teaching LLMs to Reason about Code Execution** | arXiv 2024 (Google DeepMind) | 自训练方法，将行级变量状态 trace 嵌入 CoT，SFT 微调 PaLM 2 做程序修复 | trace SFT 用于 repair，证明 trace-aware CoT 可泛化到推理时无 trace 场景 |
| 3 | **CodeExecutor** | Findings of ACL 2023 | 构造 mutation-based Python 数据集（含逐行变量状态），课程学习做 execution trace pretraining | 最早的 trace pretraining 工作之一，让模型学会"执行"代码 |
| 4 | **What I Cannot Execute, I Do Not Understand (E.T.)** | arXiv 2025 (Meta + Edinburgh) | Execution Tuning，行级/指令级 trace 粒度训练 LLM，1.5M+ 程序，dynamic scratchpad 处理长 trace | 系统研究 trace FT 粒度与有效性，CruxEval ~80% 但下游代码生成收益有限 |
| 5 | **Do Code Semantics Help? (DCSH)** | EMNLP 2025 Findings | 5 种 trace 格式（Scratchpad/NExT/SemCoder/CodeExecutor/Concise）做 SFT，结论：trace 对 SFT 提升有限，对推理时 self-debugging/voting 更有价值 | 直接竞争——对"trace + SFT"方向的系统批判，负面结论恰好是我们的研究动机 |
| 6 | **CWM: Open-Weights LLM for Code Generation with World Models** | arXiv 2025 (Meta FAIR, 32B) | 常规预训练后 mid-training：Python interpreter trace + Docker agentic 轨迹混入（+5T tokens），再 SFT + RL | 工业级 trace mid-training 实践，验证方向被工业界采纳 |
| 7 | **Investigating Execution-Aware LMs for Code Optimization** | ICPC 2025 | CodeT5+ 三种训练策略 × 四种执行信息（行执行次数/行覆盖/分支覆盖/变量状态），代码优化任务 | 消融研究，结论偏负面（执行信息对代码优化提升有限） |
| 8 | **ET-CoT: Execution Trace Chain of Thought** | ICML 2025 Workshop | PyTracify 生成大规模 trace，SFT 微调 LLM 生成 trace CoT 预测程序输出 | CRUXEval-O 和 LiveCodeBench 上验证 |

边缘相关（提示工程而非训练）：
- **Towards Effectively Leveraging Execution Traces for Program Repair** (arXiv 2025, JPMorgan): trace 加入 prompt，长 trace 反而降低效果
- **Runtime Traces Guided APR with Multi-Agent Debate** (arXiv 2026): 多智能体调用 trace，不涉及训练
- **EG-CFG: Execution Guided Line-by-Line Code Generation** (NeurIPS 2025): 推理时执行反馈，不做 trace training

**结论：这是一个真实且活跃的研究方向（8 篇直接相关，2023-2025 年持续产出）。** 关键规律：(1) 多数工作聚焦"模拟执行"（predict output/trace），而非用 trace 提升分类；(2) DCSH 和 ICPC'25 均报告 SFT 收益有限，方向存在争议，恰好是研究空间；(3) Meta CWM 的工业投入验证了方向价值。

---

## 方向 2: Exception/Error/Fault 信息用于 LLM 训练

### DCSH 的 5 种 trace 格式（确认）

1. **Scratchpad** — LLM 做中间计算的草稿格式
2. **NExT** — 执行 trace 作为内联注释嵌入代码
3. **SemCoder** — 自然语言逐行描述执行过程
4. **CodeExecutor** — 记录每行变量状态变化
5. **Concise** — CodeExecutor 变体，忽略值未改变的变量

**关键发现：5 种格式全部是完整语义执行信息（变量状态、逐行描述），不包含 exception-only 变体。没有人在 trace 格式消融中测试过 exception-only。**

### 找到的相关工作

| # | 标题 | 会议/年份 | 核心做法 | 与我们的关系 |
|---|------|----------|----------|-------------|
| 1 | **Fault Localization via Fine-tuning LLMs with Mutation Generated Stack Traces** | ICST 2025 Industry (Jambigi et al.) | 变异生成 64K 条 crash 数据，FT LLM，输入仅 stack trace（方法名+行号），预测 root cause 函数。SAP HANA 66.9% | **最接近的工作**——仅用 crash/exception 信号（无完整 trace），发现最小信号就够用。加入源代码反而降低准确率。但任务是 fault localization |
| 2 | **SBEST: Leveraging Stack Traces for Spectrum-based FL** | EMSE 2024 (Pacheco et al.) | 将 stack trace 整合进 SBFL。关键实证：**98.3% 的 bug 修复直接对应 stack trace 中的 exception** | "minimal diagnostic signal"的最强实证支撑——98.3% 相关性证明 exception 信号的充分性 |
| 3 | **LLM4PatchCorrect** | TSE 2024 (Zhou et al.) | ICL，输入 = bug description + execution trace + failing tests + coverage + similar patches，判断 patch correct/overfitting。StarCoder，84.4% acc | 做 binary verdict 但需要多种信号组合才达 84.4%，我们用 exception-only 达 99.83%，对比鲜明 |
| 4 | **AutoCrashFL** | arXiv 2025 (SAP) | LLM agent + crash dump + source code，工业规模 crash root cause 定位，30% acc@1 | 同样以 crash/exception 为核心输入，工业规模验证 |
| 5 | **Crash Report Enhancement with LLMs** | arXiv 2025 | LLM 增强 crash report（stack trace + repo 代码），bug 定位准确率 10.6% → 40.2-43.1% | stack trace/exception 作为核心输入信号的又一例证 |

**结论：没有发现任何人专门用 exception-only 信号做 verdict prediction 并报告 99%+ 准确率。** ICST'25 的 stack trace FT 和 SBEST 的 98.3% 实证是最接近的支撑。fault localization 领域有"minimal diagnostic signal"的初步发现，但未迁移到 verdict/classification 任务。这是明确的文献空白。

---

## 方向 3: 信息粒度 / 任务复杂度匹配

### 信息论核心文献

| # | 标题 | 会议/年份 | 核心做法 | 与我们的关系 |
|---|------|----------|----------|-------------|
| 1 | **Deep Learning and the Information Bottleneck Principle** | IEEE ITW 2015 (Tishby & Zaslavsky) | DNN 每层是对输入的有损压缩，最优表示应最大化与标签的互信息同时最小化与输入的互信息 | **直接理论支撑**——IB 框架证明分类网络应压缩任务无关信息，exception-only 等价于手动执行此压缩 |
| 2 | **On the Information Bottleneck Theory of Deep Learning** | ICLR 2018 (Saxe et al.) | 反驳 Tishby 的"压缩普遍性"——压缩只在双饱和激活下出现；但确认输入含任务无关子集时表示会压缩无关信息 | 部分支撑——不能说"压缩所以更好"，应说"去掉任务无关噪声使信号更纯净" |
| 3 | **Minimal Achievable Sufficient Statistic (MASS) Learning** | ICML 2019 | 训练目标使网络学到"最小充分统计量"，引入 CDI 处理确定性变量 | **形式化支撑**——exception-only 是 pass/fail 任务的近似最小充分统计量 |

### 任务导向压缩

| # | 标题 | 会议/年份 | 核心做法 | 与我们的关系 |
|---|------|----------|----------|-------------|
| 4 | **Task-Oriented Lossy Compression with Classification Constraints** | IEEE ITW 2024 | 推导 binary/Gaussian 源的率-失真-分类闭合解，证明分类任务的最小充分信息量远小于重建任务 | **信息论量化支撑**——binary classification 只需极少信息，full trace 的信息率远超所需 |

### LLM 长上下文性能退化

| # | 标题 | 会议/年份 | 核心做法 | 与我们的关系 |
|---|------|----------|----------|-------------|
| 5 | **Lost in the Middle: How Language Models Use Long Contexts** | TACL 2023 (Liu et al.) | 多文档 QA 中信息在中间时性能低于闭卷基线，U 形曲线，30+ 文档时准确率降 30%+ | **最强实证类比**——full trace 把 exception 信号淹没在执行细节中，等价于相关信息在超长上下文中间 |
| 6 | **Context Length Alone Hurts LLM Performance Despite Perfect Retrieval** | arXiv 2025 | 控制变量：检索完美时仅增加上下文长度就导致 5 个模型性能降 13.9%-85%，即使无关 token 替换为空白仍下降 | **极强直接支撑**——full trace 的长度本身就是负担，exception-only 消除了长度惩罚 |

### 输入特征与标签粒度匹配

| # | 标题 | 会议/年份 | 核心做法 | 与我们的关系 |
|---|------|----------|----------|-------------|
| 7 | **Quantifying Impact of Uninformative Features on Classification** | APL Machine Learning 2023 | 系统量化无信息特征对分类的影响，对 kNN 等基于距离的算法有显著伤害 | 背景支撑——full trace 的执行细节对 LLM 等价于无信息特征 |
| 8 | **Should We Always Train on Fine-Grained Classes?** | arXiv 2025 | 粗粒度标签训练在大数据集上优于细粒度；细粒度决策边界与粗粒度任务无关时成为干扰 | **标签-输入粒度匹配直接论证**——binary pass/fail 不需要细粒度执行路径信息 |
| 9 | **An Information-Theoretic Approach to Analyze NLP Classification Tasks** | arXiv 2024 (Cambridge) | 互信息分解输入对输出的影响，发现输入难度与任务输出复杂度存在信息论耦合 | 方法论参考——可用于定量分析 trace 粒度 vs 任务输出复杂度 |

反例注意：
- **Rethinking Minimal Sufficient Representation in Contrastive Learning** (CVPR 2022): 对比学习中保留非最小信息反而有助于下游分类。但场景是自监督预训练后迁移（下游任务未知），与我们直接 inference/已知目标的场景不可比。

**结论：有充分的理论支撑链。** IB (Tishby 2015) → MASS (ICML 2019) → 任务导向压缩 (ITW 2024) 构成理论框架；Lost in the Middle (TACL 2023) + Context Length Hurts (arXiv 2025) 提供 LLM 特有的实证机制。**但没有找到专门研究"trace 信息粒度 vs 代码分析任务复杂度"的系统性工作**——这是新颖性空间。

---

## 方向 4: Verdict/Classification 任务上的 Trace 使用

### Test Verdict / Pass-Fail Classification

| # | 标题 | 会议/年份 | 核心做法 | 与我们的关系 |
|---|------|----------|----------|-------------|
| 1 | **Learning to Encode and Classify Test Executions** | ACM SAC 2021 (Tsimpourlas et al.) | 方法调用序列 + 全局状态 trace → 神经网络嵌入分类器，9% 标注 trace 做 pass/fail 分类，precision/recall/specificity 均 >95% | **最直接前驱**——trace → pass/fail 分类，但解决 test oracle 问题（无标签场景），且不用 LLM |
| 2 | **AbstractTrace** | Applied Sciences 2024 (MDPI) | execution trace 做测试套件聚类和分类，去冗余优化测试套件 | trace 用于测试管理，任务不同（套件优化 vs 结果预测） |

### Patch Correctness Prediction（最成熟的相关领域）

| # | 标题 | 会议/年份 | 用 Trace? | 准确率 | 与我们的关系 |
|---|------|----------|----------|--------|-------------|
| 3 | **PATCH-SIM** | ICSE 2018 (Xiong et al.) | **是**（complete-path spectrum） | — | 经典方法，trace 相似度比较，非分类模型 |
| 4 | **Crex** | IST 2022 | **是**（micro-trace） | F1=89.0% | **唯一用动态 trace 做 patch correctness 分类的方法**，限 C 程序 |
| 5 | **ODS** | TSE 2021 (Ye et al.) | 否 | 71.9% | 纯 AST 静态特征 baseline |
| 6 | **Invalidator** | TSE 2023 (Le-Cong et al.) | 否 | 81% | Daikon 不变量 + PLM，无 trace |
| 7 | **APPT** | TSE 2024 | 否 | 79.7% | BERT FT，纯代码，已知 baseline |
| 8 | **LLM4PatchCorrect** | TSE 2024 (Zhou et al.) | **是**（多信号之一） | 84.4% | ICL + 多信号组合，trace 是输入之一 |
| 9 | **ComPass** | EMSE 2026 (Zhang et al.) | 否 | 88.35% | 对比学习+BERT，当前 SOTA，不用 trace |
| 10 | **Code Representation for PCA** | arXiv 2026 (Zhang et al.) | 否 | 82.69% (CPG+GGNN) | 500+ 模型系统对比，图结构表示天花板 |

### 相关但不同任务

| # | 标题 | 会议/年份 | 核心做法 | 与我们的关系 |
|---|------|----------|----------|-------------|
| 11 | **REval** | arXiv 2024 (浙大/北大) | 评估 LLM 在 4 类执行任务（覆盖/状态/路径/输出预测）的能力，GPT-4-Turbo 82.6% | LLM 理解 trace 能力基准，非 verdict 分类 |
| 12 | **CANNIER** | EMSE 2023 | test rerun + ML，用 verdict 历史序列和时长预测 flaky test | flaky test 领域使用 verdict 序列作为特征 |
| 13 | **FlaKat** | arXiv 2024 | doc2vec/code2vec/tf-idf 分类 flaky test 根因 | flaky test 纯静态，无 trace |
| 14 | **DL-CIBuild** | ASE 2022 | LSTM-RNN 预测 CI build 失败，特征为 build 历史和 commit 元数据 | CI 失败预测，build-level 粒度，不用 trace |

**结论："test verdict prediction"作为独立任务几乎没有被系统研究。** 最接近的是 SAC 2021 的 test oracle 工作和 patch correctness 领域。Patch correctness 主流（ODS/APPT/Invalidator/ComPass）均不用 trace，仅 PATCH-SIM 和 Crex 用了 trace。**没有工作将 LLM + execution trace + test verdict classification 三者结合**——这是明确的文献空白。

---

## 综合评估

### "虚空画靶"风险评估

**风险不大，但需要精准定位。**

trace SFT 是真实且活跃的方向（8+ 篇，2023-2025），但现有工作的任务集中在"模拟执行"（输出预测）和"程序修复"，**不是分类**。test verdict prediction 本身作为独立任务缺乏足够的研究积累，可能被质疑"任务本身是否有足够价值"。

建议的回应：将 verdict prediction 定位为 patch correctness prediction 的自然延伸（该领域成熟，有 APPT/ODS/Invalidator/ComPass 等多个 baseline），但强调现有方法几乎都是纯静态的，trace 作为动态信号未被充分探索。

### 最接近的竞争工作

1. **DCSH (EMNLP 2025)**: 5 种 trace 格式 SFT 消融，但 (a) 无 exception-only 变体，(b) 任务是代码生成不是分类，(c) 负面结论恰好是我们的出发点
2. **LLM4PatchCorrect (TSE 2024)**: LLM + trace + binary verdict，但 (a) 是 ICL 不是 SFT，(b) 需要多信号组合才达 84.4%，(c) 无 trace 粒度消融
3. **Crex (IST 2022)**: 唯一用 trace 做 patch correctness 分类的方法，但 (a) 非 LLM，(b) micro-trace 限 C 程序，(c) 无 exception-only 变体
4. **ICST 2025 (Jambigi et al.)**: stack trace-only FT，最小信号够用的发现最接近我们，但任务是 fault localization

### 建议的 Framing 调整

1. **核心卖点重新聚焦**：不是"trace SFT"（DCSH 已覆盖且结论负面），而是 **"trace 粒度选择对分类任务的影响"**——DCSH 证明 full trace 对 SFT 帮助有限，我们的贡献是揭示原因（信息粒度不匹配）并给出解法（exception-only）

2. **理论框架嫁接**：将 IB 理论 (Tishby 2015) + Lost in the Middle (Liu et al. 2023) + Context Length Hurts (2025) 组合为解释框架——exception-only 同时解决了两个问题：(a) 信息论层面的最小充分统计量，(b) LLM 工程层面的长上下文退化

3. **Baseline 对齐**：将 patch correctness 领域的 APPT (79.7%)、ComPass (88.35%)、LLM4PatchCorrect (84.4%) 作为直接 baseline，强调它们要么不用 trace 要么需要多信号组合

4. **差异化声明**：文献中 (a) 无 exception-only trace 格式的消融实验，(b) 无 trace 粒度 vs 任务输出复杂度的系统性研究，(c) 无 LLM + trace + binary verdict 三者结合——三重空白支撑新颖性
