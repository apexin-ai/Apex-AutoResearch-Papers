---
name: Schema-Semantic Constrained IE Writing Patterns
description: 从8篇深度精读论文蒸馏的约束解码+结构化IE领域写作规范——叙事结构、图表编排、论证策略
source_papers: 8 deep-read
---

## 叙事结构共识

**Intro 5段式主导**（6/8，GoLLIE/GCD/BoostCD/CodeIE/GenIE/XGrammar，置信度：高）
①背景+重要性 ②现有缺陷 ③本文方案 ④结果预览 ⑤贡献列表。贡献 3 条最常见（7/8），CRANE 典范：理论+方法+实验各一条。

**故事类型分布**：
- **突破局限型**（4/8: GoLLIE/BoostCD/CRANE/IterGen）：现有范式根本缺陷→修复→验证。CRANE 用 TC0 复杂度理论量化"缺陷"，是理论深度最强的版本。
- **统一框架型**（2/8: GCD/KnowCoder）：多任务统一→通用框架→跨任务验证。
- **化繁为简型**（2/8: PICARD/XGrammar）：复杂问题的简洁解法。XGrammar "99%可预计算"是极强的化简叙事。

**Hook 策略**："LLM 能做 X 但在 Y 上失败"的能力落差最有效（5/8）。变体：CRANE "约束解码本应帮助却反而损害"（反直觉翻转）；XGrammar "128K token 每步全检查是不可接受的"（量化痛点）。

**关键洞察呈现位置**：Section 3 方法段揭示技术洞察（GCD likelihood misalignment, GoLLIE 正则化），或 Figure 1 用示例展示（BoostCD 互补错误, CRANE 三路对比）。

## 图表编排规范

**Figure 1 以 method_overview 为主流**（6/8: GCD/KnowCoder/IterGen/PICARD/GenIE/XGrammar，置信度：高）
标配元素：流程图+真实示例+创新模块高亮。次选：motivation 对比图（BoostCD 双路径错误, CRANE 三路对比）适用于"现有方法有明确缺陷"的故事。

**主结果用表格，趋势分析用图**（8/8 共识，置信度：高）
F1 数字→Table；数据效率/scaling/batch size→折线图（GenIE, XGrammar）。消融以表格为主（5/8），图为辅（2/8）。XGrammar 用对数坐标柱状图展示 100x speedup。

**图的叙事节奏**：method overview → schema/prompt/architecture 详图 → 主结果 → 消融/分析。典型 4-6 figures（IE 论文），系统论文可达 10 figures（XGrammar 拆解每个技术组件）。

## 主结果表编排

**行=方法、列=数据集×指标**（6/8，置信度：高）
行按类别分组（pipeline vs e2e, finetuned vs zero-shot），列按数据集分组。CRANE 变体：行=方法×模型，展示跨模型一致性。

**Baseline 5-9 个**（中位数 6），必须覆盖：①领域 SOTA ②通用 LLM 基线 ③约束/无约束对比。

**高亮**：bold_best 是唯一共识（8/8）。统计报告：单次运行可接受（5/8），但 mean±std（GoLLIE）或 95% CI（BoostCD）显著加分。

## 消融表设计

**full_numbers 最常见**（5/8: GCD/BoostCD/GenIE/CodeIE/CRANE，置信度：高）
delta_from_base（GoLLIE/KnowCoder/XGrammar）用于强调增量贡献。XGrammar 逐步叠加+speedup 倍数是系统论文消融典范。

## 值得模仿的叙事技巧

1. **理论+实证双重论证**（CRANE）：用复杂度理论（TC0）解释实证现象（约束降低准确率），将工程问题提升为科学问题
2. **互补错误可视化**（BoostCD）：同一输入的两种错误对比，使集成动机不证自明
3. **消融统计检验**（GoLLIE）：每个组件的 delta 配 p-value，消融从定性变定量
4. **"免费午餐"框架化**（PICARD）：强调无需重训只需推理约束，降低读者采纳心理门槛
5. **2×2 交叉实验**（CodeIE）：分离表示和模型两个变量，精确归因贡献来源
6. **99% 预计算叙事**（XGrammar）：用一个极端数字（99% context-independent）锚定全文核心洞察
