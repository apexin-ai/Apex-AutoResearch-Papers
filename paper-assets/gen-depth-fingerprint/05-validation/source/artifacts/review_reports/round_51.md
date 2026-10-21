---
round: 51
review_mode: fresh
overall_score: 3.5 - Borderline Conference (建议 Findings 接收)
timestamp: 2026-05-24T23:10:53.789431+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 51 (Fresh Review)

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh (重新审稿，无前轮记忆)
**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计; R2: 新颖性+写作质量)
**轮次**: 1 轮（交叉回应后关键问题达成共识，无需第 2 轮）

---

## Summary

论文定义了 "depth profiling" 任务——将文本分类为 gen-0（人类）/ gen-1（首次生成）/ gen-2+（多次递归生成），提出 Differential Depth Response (DDR) 框架：recursive base-model generation 下，NLL 分布的 location 特征（entropy mean, TTR, hapax ratio）随深度单调漂移（Cohen's d = 0.74–1.05），而 shape 特征（entropy max, min, tail decay）近似稳定（d < 0.10）。利用 7 个特征 + XGBoost，在 8 个 base-model 生成器（5 个 family，0.6B–8B）上实现 LOGO 3-class F1 = 0.762, leak-free binary F1 = 0.694。

---

## Strengths

**S1** [R1+R2 共识] **研究问题的原创性**：从 binary AI detection 扩展到 ordinal depth classification 是 genuinely novel 的任务定义，填补了 binary detection 与 model collapse 分析之间的空白。

**S2** [R1+R2 共识] **统计方法论严谨程度远超 ACL 平均水平**：Bootstrap CI、Bonferroni 校正、TOST 等价性检验、permutation testing、Granger 因果分析、ANOVA 方差分解——多层次统计验证体系在 NLP 实证论文中罕见。

**S3** [R1+R2 共识] **消融实验覆盖面 exemplary**：26 页附录涵盖温度敏感性、prompt 泛化、文本扰动鲁棒性、跨域迁移、解码策略、参考模型选择、指令微调、finer-grained depth、classifier sensitivity 等 20+ 实验，覆盖了几乎所有可预见的审稿疑问。

**S4** [R1+R2 共识] **DDR 分解的清晰性**：Location drift vs. shape stability 的二元分解是干净、可量化的经验发现（≥8× effect-size gap），ANOVA 方差分解（η²_depth = 0.34–0.37 for location vs. <0.01 for shape，>48× gap）提供有力统计支撑。

**S5** [R1] **LOGO/LOFO 评估协议设计合理**：Leave-One-Generator-Out 和 Leave-One-Family-Out 提供多层次泛化测试；gen-0 共享种子问题通过 independent-seed 实验（F1 = 0.680 vs. 0.694）得到妥善处理。

**S6** [R1+R2 共识] **诚实的局限性讨论**：坦率报告 instruction-tuned 模型下的性能退化、gen-1/gen-2+ 边界的高错误率、base-model-only 限制，未 overclaim。

**S7** [R1+R2 共识] **可复现性高**：匿名代码仓库、标准工具（XGBoost、Pythia-410M）、详尽实验参数。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [R1+R2 共识] **温度敏感性在主文讨论严重不足**
t=0.9 时 3-class F1 从 0.762 降至 0.647（−15%），95% CI 不重叠；cross-temperature 迁移（t=0.7 训练→t=1.0 测试）严重退化，部分 generator（如 Qwen-1.7B）F1 降至 0.418。主文 §4.3 仅约 3 行简述，Limitations 仅提 "single decoding regime"，与 Conclusion "DDR is an empirical regularity" 的强声明矛盾。需要在主文用至少一段讨论温度敏感性的机制和影响，并在 Conclusion 中加温度条件限定。

**N2** [R1+R2 共识] **Binary F1=0.694 的实际意义未被充分论证**
排除 trivial 的 gen-0 分类后，gen-1 vs. gen-2+ 的核心区分能力仅 F1=0.694（~30% 错分率），gen-1→gen-2+ 边界错误率高达 48.4%（Appendix i）。3-class F1=0.762 被 gen-0 高可分性（F1≈0.921）拉高，实质上 depth profiling 相对于 binary detection 的增量价值应由 gen-1/gen-2+ 区分衡量。论文 framing 暗示实用价值（§1 "data provenance and corpus curation"），但性能数据不支持。应将核心错误分析从 Appendix 提升到主文，并更显著地标注 feasibility study 定位。

**N3** [R2 提出, R1 同意] **DDR 新颖性质疑——shape 稳定性可能从架构约束 trivially 推导**
DDR 核心发现可拆解为：(1) location drift 与 Shumailov et al. (2024) 尾部侵蚀方向一致（场景不同但机制类似）；(2) shape stability 论文自身 §5 归因于 "architecturally bounded: entropy max by log|V|, tail decay by softmax geometry"，暗示这是模型固有约束而非递归生成独特发现。R1 补充：组合价值和 LOGO 跨生成器验证有增量贡献，但更适合 Findings 级别。需要论证 shape 稳定性为何不是 trivially predictable（提供反例/边界条件），或强化 DDR 的 downstream utility 不可替代性。

**N4** [R2 提出, R1 同意] **Base-model-only 限制实际价值**
Instruction-tuned 模型下 DDR 信号大幅压缩（3-class F1 下降 3.7–19.9 pp）；QLoRA 恢复（F1=0.89–0.91）仅是 within-model 5-fold CV，非 cross-generator LOGO——而 cross-generator transfer 正是论文核心卖点。Base→instruct 迁移 F1=0.490（Table 19），实际场景中递归生成几乎全来自 instruct/RLHF 模型。虽然标题已标注 "Base-Model"，但应更直接讨论 base model 场景的独立价值（如 pretraining corpus contamination 检测），并明确 QLoRA 恢复的评估局限性。

### Should-Fix（影响评分但不一票否决）

**W1** [R1 提出, R2 部分反驳] **DDR 描述性框架与分类任务之间的逻辑断层**
DDR 是 post-hoc 解释性框架，分类器使用全部 7 个原始特征而非 DDR 分解后的 derived representation。R2 提供了有力反驳：LOFO 分析（Table 8-9）验证了两类特征独立贡献，ANOVA（Figure 7）量化了分区的统计显著性，DDR 类似于 bias-variance tradeoff 的解释角色。但两位 Reviewer 同意论文叙事在 "DDR 解释分类" 和 "DDR 驱动分类" 之间摇摆，需要修正 framing。

**W2** [R1+R2 共识] **"Entropy" 术语全文误导性使用**
§3.3 定义 "entropy" 为 reference-model NLL，但特征命名始终使用 entropy_mean、entropy_std 等，DDR 分析中讨论 "entropy stability" 可能使读者误解为信息论 entropy 的稳定性。此问题从 Round 32 起跨 14 轮反复出现。建议评估全文统一使用 "NLL" 或 "ref-entropy" 的可行性，至少在 Introduction 首次出现和 Table 1 中加强标注。

**W3** [R2 提出, R1 同意] **OOD Detection 方法论连接缺失**
NLL 统计特征与 OOD detection 方法论高度重叠，近期有 "Human Texts Are Outliers" 直接将 AI 文本检测重构为 OOD 问题。Related Work §2 应补充简要讨论，说明 depth profiling 与 OOD detection 的区别。

**W4** [R1+R2 共识] **跨域实验规模过小 + Code 域性能下降未分析**
Appendix j 每域仅 200 seeds × depth 3，Code 域 binary F1 降至 0.63 但缺乏原因分析。建议扩大规模或明确标注为 preliminary/exploratory，并讨论 Code 域下降原因。

**W5** [R1+R2 共识] **Discussion §5 机制解释是 post-hoc 直觉**
Shape 稳定性归因于 "log|V| bound" 和 "softmax geometry" 是直觉性解释，非 formal verification。R1 指出 Pythia (50K vocab) 和 Qwen (150K+ vocab) 类似稳定性并不反驳（实际值远低于上界），但同意应标注为 hypothesis/conjecture。

**W6** [R1 提出, R2 认同] **XGBoost 固定超参数未调优**
n_estimators=200, max_depth=6, lr=0.1 接近默认值。Table 11 的 classifier sensitivity 分析部分缓解（LR 0.71, RF 0.725, XGBoost 0.762），但应补充一次 systematic tuning 结果。

**W7** [R1+R2 共识] **5-class 深度分类性能主文讨论不足**
5-class F1≈0.50（Table 5），表明深度分辨率被 bound 在约 3 classes。标题 "Depth Profiling" 暗示任意深度分类可能性，但主文几乎未讨论这一天花板。

**W8** [R1 提出, R2 部分反驳] **泛化声明可能过度**
Abstract/Conclusion 使用 "empirical regularity" 等强语言，但实验覆盖有限（≤8B 参数、英文 Wikipedia、主要 t=0.7）。R2 认为在当前覆盖范围内术语合理，但同意应加温度条件限定。

---

## Reviewer Consensus [AGREE]

1. **研究问题新颖、实验设计严谨**——两位 Reviewer 一致认可任务定义的原创性和统计方法论的高水准
2. **F1=0.694 实际意义有限**——gen-1/gen-2+ 核心区分接近 coin-flip，3-class F1 被 gen-0 拉高
3. **Base-model-only 限制严重**——instruct 模型下信号退化，QLoRA 恢复非 cross-generator
4. **温度敏感性削弱泛化声明**——t=0.9 F1 降 15%，主文讨论不足
5. **DDR 更适合定位为 empirical finding 而非方法论贡献**
6. **"Entropy" 术语需全文修正**
7. **OOD detection 方法论连接缺失**
8. **格式完全合规**（正文 ≤8 页、Limitations 存在、匿名化合规、AI 披露完整）
9. **建议 Findings 接收**

---

## Reviewer Divergence [REBUT]

1. **DDR 形式化断层的严重性**：R1 认为 DDR 与分类之间存在逻辑断层（critical），R2 反驳认为 DDR 作为解释性框架合理且有 LOFO/ANOVA 支撑（降级为 writing fix）。**Director 判断**：R2 论据更有力（LOFO Table 8-9 确实验证了两组特征的独立贡献），但 R1 的关切合理——论文叙事确实在 "explains" 和 "drives" 之间摇摆。降级为 Should-Fix (W1)。

2. **泛化声明的合理性**：R1 认为 "empirical regularity" 过强，R2 认为在实验覆盖范围内合理但需加温度限定。**Director 判断**：温度限定是关键——加上条件后表述可接受。纳入 N1 的 action item。

---

## Questions

1. 如果论文能展示至少一个 instruction-tuned 模型的 LOGO 评估结果（即使性能下降），是否足以回应 base-model-only 的关切？
2. DDR 的 shape stability 是否有反例——是否存在某种生成条件（如极高温度 t≥1.2、或特定架构如 MoE）下 shape 也会漂移？
3. Gen-1/gen-2+ 区分的 oracle 上限是多少？最佳单 generator 内分类性能 vs. 跨 generator 的 gap 有多大？

---

## Missing References

1. **OOD detection 方法论文献**：NLL/perplexity-based OOD detection（如 "Human Texts Are Outliers", arXiv 2510.08602）——R2-W3, R1 同意
2. **注**：R2-W2 建议补充与 concurrent work（Broken Telephone, Markovian Chains）的实证对比，R1 REBUT 认为标准过高。Director 判断：概念对比（Appendix z.8 Table 52）已充分，实证对比为 nice-to-have 而非 must-fix。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用 external_review.paperreview_ai）。

---

## Visual Layout Check（非评分项）

**状态**: done (完成于 2026-05-24 22:55 UTC)
**总计**: 0 critical, 1 warning, 15 info

**Warning:**
- Page 16: Table 11（classifier comparison）和 Table 13（sampling sensitivity）列数较多，字号明显缩小。Table 13 有 7+ 列，部分数字在正常缩放下可读性差，建议检查 `\resizebox` 调整。

**Info highlights:**
- Page 1: 首页无 display item，Figure 1 在 page 2 顶部。Abstract 信息密度高，影响有限。
- Page 4: Figure 2 pipeline 图部分内部文字框字号偏小。
- Page 6: Figure 4 单栏尺寸偏小，数据点和 axis labels 处于可读性下限，建议改为 figure*。
- Page 7: 单页 3 个 display items（Figure 5 + Figure 6 + Table 3），信息密度极高但未溢出。
- Page 36: 末页底部约 1/4 空白，作为附录最后一页可接受。

整体排版质量良好，无 critical 问题。

---

## Overall Assessment

**评分**: 3.5 / 5 — Borderline Conference
**建议**: Findings 接收

**置信度**: 4/5（两位 Reviewer 均对 AI text detection、distributional analysis 和 model collapse 领域熟悉）

**理由**:
论文定义了一个 genuinely novel 的任务（depth profiling），提供了 clean 的经验分解（DDR），实验设计和统计方法论的严谨程度在 ACL 社区中属 top-tier。这些优势使其适合 ACL 出版物。

然而，四个核心问题限制了其主会议级别的影响力：(1) 中等性能（binary F1=0.694）下的实际价值论证不足；(2) 仅限 base model，instruct 模型下信号退化且缺 cross-generator 验证；(3) DDR shape stability 的新颖性可能从架构约束 trivially 推导；(4) 温度敏感性（t=0.9 降 15%）与 "empirical regularity" 泛化声明矛盾。

综合来看，论文的 task formulation 和 empirical rigor 具有独立学术价值，适合 Findings 接收。若能充分回应 N1-N4（温度讨论、性能定位、新颖性论证、instruct scope），可重新考虑主会议。

---

## Detailed Comments

### §1 Introduction
- "data provenance and corpus curation" 动机偏强，与当前性能不匹配。建议加 "feasibility" 或 "exploratory" 限定。
- 脚注 1 匿名 GitHub repo 合规，无泄露。

### §3 Method
- Table 1 特征命名建议从 entropy_* 改为 nll_* 或加注。
- Figure 2 (c) LOGO 示意图中 "evaluation folds on one generator" 可改为 "held-out generator"。
- §3.3 "entropy" 术语定义后续未一致执行。

### §4 Results
- §4.1: Binary F1=0.694 作为 primary metric 标注清晰，但应在此处讨论 gen-1/gen-2+ 错误率而非仅引用 Appendix。
- §4.2: DDR 形式化定义清晰，k-means validation (sil=0.660) 有效。但 Cohen's d=0.20 阈值应注明来源或敏感性。
- §4.3: 温度敏感性讨论不足，是最需要加强的段落。
- Table 3: Binoculars binary F1=0.539 远低于其 binary detection SOTA，值得简要分析原因（设计目标不同）。

### §5 Discussion
- 机制解释（log|V|, softmax geometry）应标注为 hypothesis。
- 与 model collapse 的区分（fixed parameters vs. weight updates）清晰有效。
- ANOVA 方差分解（Figure 7）是论文最有力的统计证据之一。

### §6 Conclusion
- "empirical regularity" 需加温度和 base-model 条件限定。

### Limitations
- 内容充分（3 点：base models, English Wikipedia, depth resolution），但温度敏感性应作为第 4 点显著列出。

### Appendix
- 覆盖面极广，是论文最大优势之一。
- Table 13 (p.16) 排版需优化（字号过小）。
- Appendix i (error analysis) 核心发现应提升到主文。