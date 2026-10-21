---
round: 18
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T12:50:10.335931+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 18
## OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 (ACL Rolling Review) | **Deadline**: 2026-05-25

---

## Summary

本文提出 OntoCoDec，将 IE ontology 编译为两层 token-level 解码约束：grammar layer（基于 XGrammar 的 CFG 约束，处理 JSON 结构和 vocabulary membership）和 semantic layer（基于 stateful entity registry 的 domain/range type 约束）。在 SciERC、DocRED、WikiEvents 三个 IE 数据集上，使用 4 个模型（Qwen3-8B、Llama-3.1-8B、Mistral-7B、Llama-3.3-70B）和 3 个 tokenizer family 进行了极为全面的评估。核心结果：LoRA + greedy S1 实现 DR ≤ 0.09%、R-F1 43-46%、CF ≤ 1.4%；beam search (k=4) 在 SciERC 上消除所有 violation 类型。

---

## Strengths

**S1. 评估深度罕见。** 3 个 IE 任务 × 4 个模型 × 3 个 tokenizer family × zero-shot/LoRA 两种设定，配合 25 页 appendix 中的 beam search、采样鲁棒性、文档长度分析、prompt 敏感性、per-relation breakdown 等——在 constrained decoding 论文中几乎没有先例。[R1-S2, R2-S1, 双方共识]

**S2. 理论基础与工程设计结合。** Decidability taxonomy 将 IE 约束分为三个层级，直接映射到两层架构；Proposition 1（Appendix O 完整证明）形式化证明 domain/range 约束超越 CFG 表达能力。Grammar-first fallback（§4）在约束冲突时优雅降级。[R1-S1/S4, R2-S2/S3]

**S3. Empirical enabling dependency 是非平凡发现。** Grammar-only 仅减少 24% DR（Table 1），semantic-only 无法独立工作，两层联合实现 94% DR reduction——这种层间依赖关系不是先验可预测的，且通过五路 ablation 被干净地量化。[R1-S3, R2-S4, 双方共识]

**S4. 局限性讨论诚实透明。** CF trade-off、模型依赖性、GENERIC↔X schema ambiguity、WikiEvents "preliminary" 标注、English-only 评估等均坦诚讨论。Limitations section 涵盖 7+ 个具体局限点。[R1-S5, R2-S5]

**S5. 可复现性良好。** Prompt 模板（Appendix A）、超参数（Appendix G）、seed 方差分析均提供。基于公开库 XGrammar 构建，无需额外训练。承诺 acceptance 后开源代码。[R1-S4, R2 Reproducibility 4/5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [critical, 双方共识] 缺乏与外部 constrained IE 基线的直接实验对比**
所有实验对比均为内部 ablation 或 post-hoc filtering 对比。Table 15-16（Appendix D）的 GCD-equivalent baseline 是 OntoCoDec 自身 grammar layer 的简化版，而非独立实现的外部系统。GoLLIE（Sainz et al., 2024, 代码已开源）、KnowCoder、CodeIE 等仅有概念讨论，无相同 evaluation protocol 下的实验数据。**这是连续 7 轮（R12-R18）最高频 critical issue**，此前尝试的 grammar-only proxy、trie-only baseline 均未被 reviewer 接受。缺乏 head-to-head 对比，读者无法判断 OntoCoDec 相对于现有方法的增量收益。
- **建议**：至少在 SciERC 上直接运行 GoLLIE，在相同 protocol 下报告 violation rate + F1。
- [R1-W1 critical, R2 交叉 AGREE]

**MF2 [critical, 双方共识] 引用错误——疑似 AI hallucination**
引用 "Luca Cotti et al., 2025. OntologyCL..." (arXiv:2510.01409) 存在多处事实错误：实际标题为 **OntoLogX**（非 OntologyCL），副标题为 **Cybersecurity Logs**（非 synchronous logs），三个作者名均拼错（Idilio→Ildio, Anisa Rula→Anna Ruia, Federico Cerutti→Federico Creviti）。标题 + 领域描述 + 三个作者名同时出错，模式与 AI hallucination 一致。引用准确性是学术诚信的基本要求。R2 抽查 10 篇中 9 篇正确、1 篇严重错误（10% 错误率虽然样本小但足以引起警觉）。
- **建议**：立即修正该引用 + 对全部 references 进行系统性人工核查。
- [R2-N2 critical, R1 交叉 AGREE]

### Major Issues（影响评分）

**W1 [warning, 分歧保留] 核心新颖性不足——系统集成而非算法创新**
Grammar layer 直接套用 XGrammar（Dong et al., 2025），semantic layer 是 PICARD 式 runtime constraint checking 向 IE 域的移植，Proposition 1 使用标准 pumping lemma。R2 认为 novelty 不足以支撑主会议（Excitement 2.5/5）；R1 部分反驳——constraint composition（§4 asymmetric conjunction + fallback）非 trivial、enabling dependency 有科学价值——但认同核心判断为 engineering contribution（Excitement 3/5）。**分歧保留**：R1 认为 EMNLP 接收 systems paper 有先例，R2 认为 Findings 是此 profile 的天花板。
- **建议**：更清晰阐述与 PICARD 的技术区别（token-level proactive masking vs beam hypothesis pruning）；强调 enabling dependency 作为核心科学发现而非附属分析。
- [R2-N1 critical → R1 partial REBUT → divergence]

**W2 [warning, 双方共识] κ̄ 统计支撑不足 + 近似 tautological**
κ̄ 仅在 3 个 schema 上计算。Figure 2 对 6 个数据点拟合线性模型，R²=0.886 但 **p=0.138 > 0.05（统计不显著）**。更严格约束 → 更多/更少 violation 接近循环论证。且 κ̄ 在 SciERC 和 WikiEvents 上值几乎相同（均 ~0.020）但 constraint enforcement 效果差异显著，解释力不足。
- **建议**：降级为 purely descriptive tool，移除 predictive/explanatory 措辞；或增加至 n≥10 datasets。
- [R1-W4, R2-W4, R1-Q2, 双方共识]

**W3 [warning, 双方共识] Entity registry 顺序依赖未被实验量化**
Entity registry 使用 "first-registered-type" 语义，早期 type 错误传播到后续所有 relation 约束。论文讨论了 S1/S2 和 fallback 缓解机制，但无实验直接量化 entity ordering 影响。且存在 genuine type polysemy 问题（如 "Python" 既可为 Method 也可为 OtherScientificTerm），first-lock 语义无法处理。
- **建议**：设计 gold/shuffled/predicted order 对比实验。
- [R1-W5, R1-Q5, R2 交叉 AGREE]

**W4 [warning, 双方共识] "四个模型(7-70B)" 声称具有误导性**
70B（Llama-3.3-70B AWQ INT4）仅 p.8 一段文字（~5 行），无独立表格、无 ablation、无 beam search、无 fine-tuning。与其他 8B 模型的完整多节评估严重不对称。且 AWQ INT4 量化对 logit 分布的影响未被隔离。
- **建议**：要么完善 70B 评估，要么降格为 "preliminary observation" 并修改 headline claim；对 8B 模型补充 quantized vs full-precision 对比。
- [R2-W1, R1-W7, 双方共识]

**W5 [warning, 双方共识] WikiEvents fine-tuning 统计效力不足 (n=20)**
n=20 文档的 bootstrap 95% CI ±3-5 pp，F1 差异大多在 CI 范围内。Abstract/Introduction 引用 "3 datasets" 时 preliminary qualification 不够显著。
- [R1-W6, R2-W2, 双方共识]

**W6 [warning, 双方共识] Zero-shot 实验占比过大但 F1 极低**
SciERC zero-shot R-F1 仅 1.30-8.05（跨模型），在如此低绝对 F1 下 constraint enforcement 的实际意义有限（将 type-inconsistent garbage 变为 type-consistent garbage）。Fine-tuned setting（R-F1 40-46%）更有部署价值但篇幅更少（~1 页 vs ~2.5 页）。
- **建议**：重新平衡篇幅分配，或更清晰论证低 F1 下 constraint enforcement 的独立价值。
- [R2-W3, R1 交叉 AGREE]

**W7 [warning, 双方共识] Abstract 数值密度过高 + DR 42-99% 范围过宽**
Abstract ~200 词含 15+ 数字，zero-shot 和 fine-tuned 数字交替出现，读者认知负担过高。42-99% 跨所有配置的 min-max 掩盖典型表现。
- **建议**：ZS/FT 分开报告；DR range 按数据集或 median/IQR 报告。
- [R2-W5, R1-W8, 双方共识]

**W8 [warning, 双方共识] GCD-equivalent baseline 对比藏在 appendix**
Table 15（GCD-equivalent grammar-only）是最接近 prior work 的直接对比，不应隐藏在 appendix。但 R1 指出即使移入主文，仍非真正外部 baseline。
- [R2-W6, R1 交叉 AGREE]

**W9 [warning, R2 发现 R1 AGREE with nuance] Proposition 1 有限 entity set caveat 缺失**
Proposition 1 证明无界 entity set 下非 CF，但实际 schema entity set 有限（SciERC: 6, DocRED: 96）。有限情形下语言是 regular（DFA 可实现），只是 O(|T|^n) 状态数工程不可行。主文无此 caveat。
- **建议**：主文添加 remark，区分 theoretical impossibility 和 engineering intractability。
- [R1-W3, R2 AGREE with nuance]

### Minor Issues

- Table 1 密度过高（6+ 列 × 多行），建议拆分或增加视觉分隔 [R2, R1 AGREE]
- Figure 1 视觉层次不够分明，内部文字标签字号偏小(~60-65% 正文字号) [R2, R1 AGREE, 视觉审查确认]
- §3.3 asymmetric conjunction 可加 Venn 图辅助理解 [R2, R1 AGREE]
- §6 Related Work 仅半栏，严重依赖 Appendix B [R17 遗留]

---

## Reviewer Consensus [AGREE]

以下问题双方达成一致：
1. **外部 baseline 缺失是最关键问题** — 连续 7 轮未解决，GoLLIE 代码已开源可直接运行
2. **引用错误必须修正** — 标题+3 个作者名同时错误，需全面核查
3. **κ̄ 统计基础薄弱** — n=3, p=0.138, near-tautological，应降级为 descriptive tool
4. **Entity ordering 需要量化** — first-lock 语义的影响未实验验证
5. **70B 和 WikiEvents 评估不够深入** — headline claim 与评估深度不匹配
6. **论文核心贡献是 engineering contribution** — 分歧仅在其是否达到主会议门槛

## Reviewer Divergence [REBUT]

**分歧 1：Novelty 严重度**
- R2：critical (Excitement 2.5/5) — grammar=XGrammar 直用，semantic=PICARD 移植，Prop1=标准 pumping lemma → Findings 天花板
- R1：major 但非 critical (Excitement 3/5) — constraint composition 非 trivial，enabling dependency 有科学价值，EMNLP 接收 systems paper 有先例
- **Director 判断**：novelty 确实有限但非零。Enabling dependency 的量化证实、decidability taxonomy 的概念框架、grammar-first fallback 的设计均有增量价值。将 novelty 定为 major 而非 critical，但这是阻止论文进入 Conference 级别的主要因素。

**已解决分歧：R1-W2 beam search overclaim**
- R1 声称 abstract 写 k=3 且仅 Llama 达到全零 → R2 用 LaTeX 源码证据证明论文写 k=4，且 LoRA+k=4 对两个 calibrated 模型均达全零 violation → **R1 事实基础被推翻，W2 撤销**

---

## Questions（需作者澄清）

1. 是否可在 SciERC 上直接运行 GoLLIE 提供 same-protocol 对比？[R1-Q1]
2. κ̄ 在 SciERC 和 WikiEvents 上值接近（均 ~0.020）但效果差异显著——是否有其他 schema property 更具预测力？[R1-Q2]
3. Grammar-first fallback rate 跨模型差异大（Qwen 0.93% vs Llama 12.02%）——哪些模型特征决定 fallback rate？[R1-Q3]
4. Entity registry "first-registered-type" 语义如何处理 genuine type polysemy（如 "Python" 在不同 context 可能为不同 type）？[R1-Q5]

---

## Missing References

参考文献覆盖较全面。建议补充：
- **InstructUIE** (Wang et al., 2023) 的 type violation 行为讨论——instruction-tuning IE 方法的 schema compliance 模式与 decoding-time enforcement 形成有意义的对比 [R1 建议]

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 6 info）：

**Warnings:**
- 页 1-2 连续纯文本（Abstract + Introduction），审稿人前 2 页无视觉锚点
- 页 4-5 Method 后半至 Experiments 开头存在视觉断档
- 页 6 单页堆叠 3 个表格（Tables 1-3），视觉密度偏高

**Info:**
- Figure 1 内部文字标签字号偏小（~60-65% 正文字号）
- 页 8 Related Work + Conclusion 压缩在同一页
- 主正文仅 1 个 figure，其余全是表格，视觉多样性不足

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 4.0 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.5-3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | 3.0 |

**评分理由**：
论文在工程层面执行出色——实验之全面在 constrained decoding 文献中罕见，grammar-first fallback 和 empirical enabling dependency 是有价值的贡献。Decidability taxonomy 提供了有用的概念框架。

但存在两个互相强化的核心限制：
1. **核心技术新颖性有限**（grammar=XGrammar 直用，semantic=PICARD 式移植）——双方共识为 engineering contribution，分歧仅在是否达到主会议门槛
2. **缺乏外部 baseline 对比**（连续 7 轮 critical）——在无法量化增量收益的情况下，engineering contribution 的价值更难评估

引用错误（MF2）虽属修正即可的问题，但与 AI hallucination 模式一致的事实损害了论文整体可信度。

"Careful integration of known components + exhaustive evaluation" 是典型的 Findings profile。修复 MF1（外部 baseline）+ MF2（引用）+ 主要 writing issues 后有潜力提至 3.5 (Borderline Conference)，但 novelty ceiling 仍是主要限制因素。

---

## Detailed Comments

### §1 Introduction
- "four autoregressive LMs (7-70B)" 夸大了评估均衡性，70B 仅一段文字
- 建议区分 ZS 和 FT 的核心数字，避免 range 混淆

### §2 Background / §3 Method
- Proposition 1 主文需添加有限 entity set caveat
- §3.4 S2 描述篇幅可压缩（方案已在实验中证明不优于 S1）

### §4 Constraint Composition
- Asymmetric conjunction 是论文的技术亮点之一，但呈现可更直观（Venn 图）

### §5 Experiments
- Table 15 GCD-equivalent baseline 应移入主文
- Zero-shot vs fine-tuned 篇幅需重新平衡
- κ̄ 分析应明确标注统计不显著 (p=0.138) 和 n=3 限制
- WikiEvents fine-tuning 在 abstract/intro 引用时需保持 "preliminary" qualification

### §6 Related Work
- 仅半栏，对 GCD/GoLLIE/EnriCo 的定位对比可从 Appendix B 移入

### References
- arXiv:2510.01409 引用存在多处事实错误，需立即修正
- 建议对全部 references 进行系统性人工核查

### Limitations
- 已较全面，可补充 entity ordering sensitivity 的量化讨论
- 70B AWQ INT4 quantization 影响的讨论可更具体