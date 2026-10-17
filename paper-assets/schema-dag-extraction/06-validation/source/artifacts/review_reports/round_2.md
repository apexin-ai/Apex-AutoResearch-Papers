---
round: 2
overall_score: borderline
timestamp: 2026-05-16T03:03:05.885772+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 圆桌审稿报告 — Round 2

**论文**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿人**: Reviewer 1 (方法严谨性 + 实验设计 + 统计分析), Reviewer 2 (新颖性 + 完整性 + 写作质量 + 格式合规)
**轮次**: Round 2（论文已针对 Round 1 的 18 个 issue 进行修订）
**外部审稿**: 未启用

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能下降的机制，提出将退化分解为 type count 和 type confusability 两个独立通道。引入 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 作为量化指标，在 Few-NERD (NER)、FewRel (RE)、MAVEN (ED) 三个数据集上进行控制实验。主要发现：(1) RE 上两通道 cleanly separable；(2) NER 上 confusability 同时影响 detection；(3) MAVEN 上出现 centrality confound 导致 per-type BCS 方向反转；(4) SDGD 负面结果表明 union-based merge 存在结构性挑战。跨模型验证在 Llama-3.1-8B 上复现了主要效应。

---

## Strengths

**S1. 研究问题重要且定义清晰。** 首次系统性隔离 type count 与 type confusability 的独立效应，填补了零样本 IE 退化机制研究的空白。三个 research question 直接可检验。【R1, R2 共识】

**S2. 实验设计精心。** Count curves + BCS-controlled 双范式互补，within-pool controlled comparison (Table 4) 消除跨 pool 混淆，permutation test 比较跨条件 slope 一致性。这是 empirical IE 研究中少见的控制实验水平。【R1 重点肯定】

**S3. 诚实报告 modest effect sizes 和负面结果。** Pairwise r²=1.3-1.7% 如实量化，SDGD 负面结果完整报告而非隐藏，MAVEN centrality confound 作为独立分析呈现。科学态度端正。【R1, R2 共识】

**S4. Centrality confound 分析有独立方法论价值。** 识别 same-domain schema 下 BCS 聚合失效的机制，连接 representation degeneration 文献，partial correlation 验证严谨。对 schema analysis 从业者有直接指导意义。【R1 重点肯定】

**S5. Round 1 修订实质性改进。** Discussion section 新增、Limitations 重构为编号列表、factorial test 移入 Appendix 作为 negative result、Contribution 2 改为 "modest predictor"、SDGD 措辞降格、Sclar et al. 引用补充、residualized BCS 分析加入 Appendix。共 8/18 个 Round 1 issue 已解决。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [Critical] v1/v2 prompt 切换引入系统性混淆，仍未解决。** v1 prompt（含 offset 要求，96.5% 错误率）用于 count curves + BCS-controlled NER + SDGD；v2 prompt 用于后续实验和 cross-model 验证。v1→v2 使 Qwen3 count=1 recall 差 11% (0.72 vs 0.64)。论文跨实验引用数字时（如 Abstract headline numbers），prompt 版本不同使比较无效。核心 framework 的两个 channel 建立在不同 prompt 版本上。**Prompt 模板仍未公开**，读者无法判断变化性质。
- Round 1 状态：SW3 (warning) → Round 2 升级为 Critical
- 两 Reviewer 共识 Critical。
- **要求**：(a) 公开完整 prompt template 至 Appendix；(b) 对关键实验报告两版 prompt 结果 or 全部统一至一版。

**C2. [Critical] 16-rel BCS gap (9.1 pp) 基于单 batch，无统计可靠性。** Table 3 caption 明确标注"single extreme batch per BCS level; bootstrap CIs require multiple batches"。但 9.1 pp 在 Abstract 和 §5.3 中与 31.2 pp 对比以论证 BCS range 解释 absolute gap 差异——对比的一端无任何 CI。
- Round 1 状态：MW1 部分解决（within-pool 已补），16-rel 独立 pool 单 batch 问题持续。
- 两 Reviewer 共识。
- **要求**：补充多 batch CI，或将 9.1 pp 降级为 illustrative，叙事重心移至 Table 4 回归分析。

**C3. [Critical] 80-rel 整体 BCS-accuracy 回归不显著，但 extreme batches 做 headline result。** Table 4: Full 80-rel slope = −0.151, CI [−0.930, +0.657], p = 0.698。31.2 pp 来自同一 pool 的 extreme batches，出现在 Abstract/Introduction/Discussion/Conclusion。
- R1 认为这是 cherry-picked endpoints；R2 反驳认为 within-pool sub-analysis (slope −0.401, p=0.027) 提供有效支撑，问题在 framing。**程度分歧，非方向分歧**——两方均认为当前 framing 不当。
- **要求**：31.2 pp 出现时必须注明 full 80-rel 条件不显著 (underpowered)，核心统计论证应指向 within-pool slope。

**C4. [Critical] 缺少 Responsible NLP Research Checklist。** ACL ARR 必须项，缺失导致 desk reject 风险。Round 1 已提出 (m3)，仍未解决。
- 两 Reviewer 共识。
- **要求**：立即补充。

**C5. [Critical] reflect-learn-2026 引用作者为占位符 `[To be verified]`。** 提交带占位符的 bib 条目不可接受。
- R2 列为 Critical，R1 认为应为 Should-Fix（5 分钟可修复的格式问题）。
- **要求**：补全作者信息，或删除引用并调整正文。

### Should-Fix（影响评分但不一票否决）

**W1. [Major] "Multi-channel degradation framework" 过度声称。** 框架仅在 RE 上 cleanly work：NER 有 channel 耦合 + non-monotonic count curve + 不显著 factorial test；ED 完全反转。"Framework" 暗示通用性，但证据支持的是 "empirical observations primarily demonstrated on RE"。两 Reviewer 共识。

**W2. [Major] Pairwise→batch 信号放大机制未形式化。** r²=1.3-1.7% 跳至 31.2 pp gap 缺乏形式化论证。within-pool quartile Δ 仅 −3.92 pp (CI 穿越零)。论文需区分 extreme batches 的理论最大效应和 representative batches 的典型效应，用 BCS range × slope 计算 realistic practical effect。两 Reviewer 共识（R1-W5 + R2-N3）。

**W3. [Major] Pairwise SCS-confusion bootstrap CI 基于非独立观测。** 1,953/11,026 type pairs 不独立（同 type 出现在多 pairs），percentile bootstrap 低估真实不确定性，p < 10^{-10} 可能被高估。应使用 type-level cluster-robust bootstrap。R1 提出，R2 AGREE。

**W4. [Major] NER count=22→44 recall 上升 (0.527→0.551) 未报 CI。** "Minor non-monotonicity" 需 CI 支撑——若 CI 不重叠则说明 count channel 在 NER 上非单调，影响 "count drives recall decline" 叙事。R1 提出，R2 AGREE。

**W5. [Major] SDGD 仅在 Few-NERD 测试，泛化性不足。** RE 是 channels 最 cleanly separable 的任务；若 SDGD 在 RE 上也失败则大大增强 merge amplification 论点。仅在一个任务上就得出"structural challenge for union-based merge pipelines"的一般性结论，证据不够。R1 提出，R2 AGREE。

**W6. [Major] RE "clean channel separation" 可能是 classification 任务形式的 artifact。** FewRel RE 是 closed-set classification（给定 entity pair 选 relation），不含 entity detection 环节。Missed rate flat (10-16%) 可能是任务形式产物——classification 本身消除了 detection 维度，使 "RE 上 channels cleanly separate" 成为循环论证。应在 Limitations/Discussion 讨论。R1 交叉回应中提出。

**W7. [Major] MAVEN 反转在 Abstract 中仍被低估。** 三个数据集中最大的 (168 types) 结果与主假设方向相反。Abstract 用 "generally suppresses recall" 一带而过，应给 MAVEN 反转和 centrality confound 独立陈述（1-2 句）。两 Reviewer 共识。

**W8. [Major] Prompt template 仍未公开。** v1→v2 导致 precision 翻倍，说明 prompt 设计对结果影响巨大。不公开严重影响可复现性。Round 1 (SW6) 未解决。两 Reviewer 共识。

**W9. [Warning] 正文仅一幅 Figure（Round 1 为零，已改善）。** Error taxonomy 是支撑 Channel 2 的关键证据但仍在 Appendix。R2 列为 Critical，R1 降级为 warning——以 8 页限制合理安排优先级。建议至少补一幅 error taxonomy 或 centrality scatter plot。

**W10. [Warning] FewRel 数据构造外部效度。** 合并 train+val 非标准用法；closed-set classification 与 extraction 有本质差异但论文并列讨论。R2 提出，R1 AGREE。

**W11. [Warning] 51% floor "confusion subgroup" 解释为推测。** Discussion 中未标注为 hypothesis。R1, R2 共识。

**W12. [Warning] "model-invariant floor" 基于仅两个 decoder-only 模型。** 应限定为 "consistent across tested models"。R1 提出。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全共识：
1. v1/v2 prompt 混淆是关键方法论问题 (C1)
2. 16-rel 单 batch 无 CI 统计不可靠 (C2)
3. 缺 Responsible NLP Checklist (C4)
4. reflect-learn-2026 引用不完整 (C5)
5. "Framework" overclaim (W1)
6. Pairwise→batch 放大缺形式化 (W2)
7. 非独立 bootstrap CI (W3)
8. SDGD 仅在 NER 测试 (W5)
9. Prompt template 必须公开 (W8)
10. MAVEN 在 Abstract 中被低估 (W7)

## Reviewer Divergence [REBUT]

| 议题 | R1 立场 | R2 立场 | 性质 |
|------|---------|---------|------|
| 80-rel 回归不显著 (C3) | Cherry-picked endpoints | Within-pool sub-analysis 有效支撑，framing 问题 | 程度之争 |
| 正文 figure 数量 (W9) | Warning 级别 | Critical 级别 | 严重性之争 |
| reflect-learn-2026 (C5) | Should-Fix | Critical | 严重性之争 |
| Soundness 评分 | 2.5/5 | 3.5/5 | R1 更重视统计方法论缺陷 |
| R2-Q4 type description SCS | Future work, 非当前弱点 | 合理问题 | 范围之争 |
| R2-Q5 closed-source 模型 | 不必要，开源更可复现 | 合理建议 | 范围之争 |

---

## Questions for Authors

1. **v1/v2 prompt 鲁棒性**：能否提供 v1/v2 完整 prompt 文本？核心结论（两通道分离、BCS-accuracy 关系）在两个 prompt 版本下是否都成立？
2. **16-rel batch 限制**：16-rel 为何仅一个 extreme batch？是 pool size 限制还是 compute budget？能否补充多 batch CI？
3. **Pairwise→batch 放大**：r²=1.5% 但 BCS gap=31.2 pp。请用 typical BCS range × slope 量化 realistic practical effect，区分 extreme vs representative batches 的效应。
4. **NER non-monotonicity**：count=22→44 recall 上升 (0.527→0.551) 的 bootstrap CI 是否重叠？
5. **SDGD on RE**：为什么没有在 FewRel 上测试 SDGD？若 merge amplification 在 RE (classification) 上也成立，"structural challenge" claim 大大增强。
6. **RE 任务形式**：RE 是 closed-set classification，"clean channel separation" 是否部分归因于任务不含 detection 环节？
7. **Non-independent bootstrap**：pairwise 分析的 bootstrap 是否 accounted for type-level clustering？

---

## Missing References

以下引用经两位 Reviewer 共识（或一方提出、另一方 AGREE）应补充：
1. **Reimers & Gurevych (EMNLP 2019)** Sentence-BERT — all-MiniLM-L6-v2 的训练框架出处
2. **Li et al. (2023)** "Evaluating ChatGPT's Information Extraction Capabilities" — zero-shot IE evaluation
3. **Wadhwa et al. (2023)** "Revisiting Relation Extraction in the era of Large Language Models" — LLM RE 相关
4. **reflect-learn-2026** — 需补全作者/DOI 或删除

R1 反驳的引用（不强制要求）：
- AFET / hierarchical label confusion 文献 (Ren et al. 2016) — R1 认为技术差异较大，相关性有限

---

## External Review (Stanford Agentic Reviewer)

未启用。项目配置 `external_review.paperreview_ai.enabled: false`。

---

## Overall Assessment

**评分: Borderline (介于 weak reject 和 weak accept 之间)**
**置信度: 4/5**

**R1 评分**: 3.0/5 (Soundness 2.5, Excitement 3.0)
**R2 评分**: 3.0/5 (Soundness 3.5, Excitement 2.5)
**综合**: 3.0/5，当前版本适合 **Findings track**，距主会差距在统计严谨性和 framing 诚实度。

### 核心判断

论文选题有价值——首次系统性隔离 count vs confusability 确实是该领域的空白。实验设计（count curves + BCS-controlled + within-pool 控制）体现了高于一般经验性 IE 论文的方法论水平。centrality confound 分析有独立贡献。SDGD 负面结果对社区有信息量。

但关键统计证据存在多处可靠性问题：
- **16-rel 单 batch 无 CI** 使跨条件对比的一端无统计基础
- **80-rel 整体回归不显著** 而 extreme batches 做 headline result（尽管 within-pool sub-analysis 部分弥补）
- **pairwise r²=1.5% → batch-level 31.2 pp 的放大缺乏形式化**
- **非独立 bootstrap** 可能高估显著性
- **v1/v2 prompt 混淆** 使跨实验比较的可信度存疑

"Multi-channel degradation framework" 的叙事超出了证据支持的范围——仅在 RE (closed-set classification) 上 cleanly work，NER 有 channel 耦合，ED 完全反转。论文应定位为 "empirical observations with controlled experiments across three IE tasks"，而非 "framework"。

### 与 Round 1 的进展

Round 1 的 18 个 issue 中，8 个已解决（Discussion 新增、Limitations 重构、factorial 降格、SDGD 措辞、术语统一、Sclar 引用、residualized BCS、SDGD prompt 标注）。核心未解决项：v1/v2 prompt 混淆（升级为 Critical）、16-rel 单 batch（持续 Critical）、Checklist 缺失（升级为 Critical）、prompt 未公开（持续）。新发现：80-rel 回归不显著、RE-as-classification artifact、非独立 bootstrap。

### 修改路径建议（非处方性，仅为评估框架）

**最小可行修改（Findings track）**：
1. 补 Responsible NLP Checklist
2. 修复 reflect-learn-2026 和 json-schema-bench-2025 引用
3. 公开 v1/v2 prompt template
4. 16-rel 9.1 pp 降级为 illustrative 或补 CI
5. 31.2 pp 出现时注明 full 80-rel 不显著
6. "Framework" → "empirical decomposition/observations"
7. Abstract 给 MAVEN 反转独立陈述

**进一步提升（主会竞争力）**：
8. 对关键实验报告两版 prompt 结果
9. Pairwise→batch 放大的形式化量化
10. FewRel SDGD 补充实验
11. Type-level cluster bootstrap
12. Discussion 增加 RE-as-classification 限制

---

## Detailed Comments by Section

### Abstract
- "two degradation channels...across three IE tasks" 但 MAVEN 反转。需限定。
- "count channel that generally suppresses recall" 中 "generally" 试图覆盖 MAVEN 例外，但不够明确。
- headline numbers (0.72→0.42, 85.7%→50.4%) 未标注 prompt 版本和模型。

### Introduction
- RQ1-RQ3 定义清晰且在论文中有对应实验回答。
- Contribution 1 "framework" 过度；Contribution 2 已改为 "modest predictor"（进步）；Contribution 3 "consistent across schema sizes" 需 80-rel 不显著的 qualification；Contribution 4 "structural challenge" 仅基于 NER 一个任务。

### Related Work (§2)
- §2.1 覆盖了 2023-2025 zero-shot IE 主要工作。
- §2.2 对 LLM-PEE 的差异化清晰。
- §2.3 anisotropy 文献连接有创意。
- 缺 Sentence-BERT、Li et al. 2023、Wadhwa et al. 2023。

### Experimental Setup (§3)
- §3.1 数据集选择合理，但 FewRel train+val 合并需更多说明。
- §3.2 SCS/BCS 定义清晰，但 "cosine similarity of type name embeddings" 的局限性应提前讨论。
- §3.4 实验设计精心——within-pool 控制尤其值得肯定。
- §3.5 v1/v2 prompt 描述不够——需完整 template。FP8 量化对结果的影响未讨论。

### Results (§5)
- §5.1 count curves: NER non-monotonicity 需 CI。MAVEN 反转需更多讨论。
- §5.2 pairwise: r²=1.3-1.7% framing 已改善，但 conditioning-on-outcome 讨论可再强化。
- §5.3 BCS-controlled: within-pool analysis 是方法论亮点。16-rel 单 batch 和 80-rel 不显著是主要弱点。
- §5.4 error taxonomy: 支撑 Channel 2 的关键证据，建议部分移入正文。
- §5.5 centrality confound: 独立有价值，分析严谨。

### SDGD (§6)
- 半页正文过短，对 Contribution 4 而言不够。
- 仅在 NER 测试，RE 缺失是遗憾。
- merge amplification 的诊断有价值。

### Discussion (§7)
- Boundary conditions 讨论合理。
- 51% floor 的 "confusion subgroup" 解释应标注为 conjecture。
- "model-invariant" 应限定为 "consistent across tested models"。

### Limitations
- 结构大幅改善（Round 1 最大进步之一）。
- Item 3 (cross-pool slope consistency) 更像 result 而非 limitation。
- 缺 FewRel classification vs extraction 讨论。

### Appendix
- Residualized BCS 分析 (§C) 质量高。
- Factorial analysis (§B) 作为 negative result 放置得当。
- SDGD full protocol (§A) 完整。
- 缺 prompt templates。
