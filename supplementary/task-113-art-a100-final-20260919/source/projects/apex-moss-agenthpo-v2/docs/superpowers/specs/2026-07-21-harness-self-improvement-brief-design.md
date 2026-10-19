# Harness 自进化研究对比与 MOSS 融合方案：文档设计

## 目标与受众

面向技术管理者撰写一份可直接用于研究汇报和技术讨论的中文 Markdown 文档。文档横向比较 Meta-Harness、WECO AIDE² 和 Recursive Harness Self-Improvement（RHI），提取三者中可复用的机制，并给出融合后的 MOSS 架构与分阶段落地路线。

最终文档路径：`docs/research/harness-self-improvement-comparison.md`。

## 写作原则

- 不按论文逐篇展开长篇介绍，而是按统一维度横向比较。
- 不单列基础术语教程；Agent、Harness、Benchmark 等概念在比较表和正文中按需解释。
- 明确区分“优化方法可用于多个任务”和“同一个进化产物能跨任务泛化”。
- 明确区分内部搜索任务、private evaluation 与外部 held-out benchmark。
- 将论文主张、实验事实和本文推论分开表述，避免夸大 recursive self-improvement。
- 主要结论使用表格、Mermaid 流程图和简短判断，技术细节服务于决策讨论。

## 文档结构

### 1. 执行摘要

用一张总表概括三项工作的定位：

- Meta-Harness：基于完整历史和原始 trace 的代码级 Harness 搜索。
- AIDE²：在异构内部任务上进化通用 autoresearch Harness，并用外部 benchmark 验证迁移。
- RHI：基于相邻版本成对反馈的任务级文本 Harness 快速适配。

执行摘要需直接给出证据强度判断：AIDE² 的跨 benchmark 泛化证据最强，Meta-Harness 的方法通用但产物偏任务专用，RHI 证明任务内快速优化而未证明产物跨任务迁移。

### 2. 三项工作的横向对比

按照以下统一维度比较：

1. 系统目标与优化对象。
2. 内层执行 Harness 与外层优化器的关系。
3. Harness 的表示形式：可执行代码或结构化 Prompt。
4. 候选生成、评估、接受、拒绝和停止机制。
5. 历史信息与上下文的保存和访问方式。
6. 反馈信号：标量分数、private score、执行 trace、LLM pairwise preference。
7. Benchmark 设计与内部/外部评测隔离。
8. 样本、数据集、benchmark 与任务族层面的泛化证据。
9. 性能、推理成本、搜索成本与 reward hacking。
10. 已证明的结论和仍未证明的主张。

本节至少包含：

- 一张三者架构对比表。
- 一张统一的自进化数据流 Mermaid 图。
- 一张 benchmark 与泛化证据表。
- 一张主要结果与局限表。

### 3. 可借鉴机制提取

分别提炼可复用而非论文专属的机制：

- Meta-Harness：文件系统完整历史、原始 trace、Coding Agent Proposer、因果诊断、可执行代码作为搜索对象。
- AIDE²：异构任务选择压力、固定成本约束、private score、外部 held-out benchmark、树搜索与 lineage、上下文按操作裁剪、防 reward hacking。
- RHI：任务级文本覆盖层、相邻版本比较、累计自然语言反馈、Contract/Hop 优化、低成本局部迭代。

同时标明组合边界：

- “完整历史存储”与“单次调用上下文裁剪”属于不同层级，可以同时采用。
- 全局 Harness 进化与任务级局部适配应分层，不能混用同一评测集。
- LLM-as-Judge 适合开放式任务，但必须配合可执行 verifier、Judge 校准和回归门禁。

### 4. 融合后的 MOSS 方案

提出三层体系：

1. **全局进化层**：进化可跨任务复用的核心 Harness 代码和搜索策略。
2. **任务适配层**：为单个任务生成轻量 Prompt Harness，优化 roles、contracts、hops 和验收规则。
3. **执行与评测层**：运行任务、保存完整 trace，并隔离 public、private 与 external held-out evaluation。

架构需覆盖：

- Harness 注册表和版本 lineage。
- 文件系统 trace/history 数据库。
- 全局 Coding Agent Proposer。
- 任务级 RHI Optimizer。
- 标量 evaluator、可执行 verifier、LLM Judge 和 reward-hacking detector。
- 固定预算、回滚、回归检查和外部 benchmark 冻结策略。

数据流需明确：

```text
任务执行 → 完整轨迹存储 → 任务级快速适配
                      ↘ 聚合失败模式 → 全局 Harness 候选
                                      → private selection
                                      → 冻结版本外部评测
```

### 5. 分阶段实施与讨论问题

给出三个阶段：

- Phase 1：补齐完整 trace、版本和评测隔离，建立可信基线。
- Phase 2：加入任务级 RHI 适配与 Contract/Hop 优化。
- Phase 3：加入全局代码级 Proposer、异构任务进化和外部泛化门禁。

最后列出需要 mentor 决策的问题，包括：

- MOSS 首期优先优化全局 Harness 还是任务局部 Harness。
- 哪些指标进入 private selection，哪些 benchmark 永久冻结。
- LLM Judge 与可执行 verifier 的权重。
- 搜索总成本如何核算和设定预算。
- 哪种程度的跨 benchmark 迁移才允许标记为新版本。

## 来源与证据要求

核心事实优先引用论文、官方项目页和官方仓库：

- Meta-Harness 论文与 Stanford IRIS Lab 仓库。
- WECO AIDE² 官方研究报告与 RSI 分级文章。
- RHI arXiv 论文。
- MLE-Bench、ALE-Bench、WeatherBench 2、KernelBench 官方资料。

文档中对尚未公开代码、尚未独立复现、合成任务、LLM-as-Judge 偏差和搜索成本未完全计入等限制必须明确标注。

## 验收标准

- 三项工作均按相同维度完成横向对比，没有重复的逐篇长介绍。
- 架构、进化对象、反馈信号、benchmark 和泛化边界表述准确。
- MOSS 融合方案能够对应三项工作的具体机制，并说明组合层级。
- Mermaid 语法可解析，Markdown 标题、表格和链接结构完整。
- 不包含 `TBD`、`TODO`、占位文本或未经标注的推测。
- 不修改代码、`CLAUDE.md` 或 `AGENTS.md`。
