---
round: 20
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-19T16:09:26.772547+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 20 (Fresh Review)

**论文**: "Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models"
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿模式**: 重新审稿（fresh）
**Reviewer 编排**: 2 名（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性 + 写作质量）
**轮次**: 1 轮（交叉分享后达成共识，无需第二轮）

---

## Summary

论文研究四个 reasoning LLM（3 Qwen + 1 Llama，7-8B 和 32B 两种规模）上 hidden-state (HS) 与 text 探针的 Safety Commitment Point 检测能力对比。核心方法论发现：层选择指标的选择可完全逆转 HS vs. text 的比较结论——crossing-rate composite 指标系统性选择浅层（掩盖 HS 优势），threshold-based 指标选择深层（恢复 HS 精度增益 +19-22pp vs 384d MiniLM）。HS 优势在更强 text encoder（1024d BGE-large）下仅 1/4 模型存活 HB 校正。7-8B 结果为 confirmatory（nested CV 验证），32B 结果为 exploratory（n≤20）。

---

## Strengths

1. **核心发现有实际价值**: 层选择指标引入系统性偏差（shallow-layer compression → crossing rate inflation）是对 safety probing 乃至更广泛 probing 社区的重要方法论警告。五指标消融设计和 random-label decomposition 控制实验为该发现提供了坚实支撑。

2. **实验设计全面、透明度高**: 4 模型 × 2 架构 × 2 规模，配合 20+ 表格消融实验（Appendix A-Z 共 26 个附录）。三级 evidence gradient（confirmatory/significant/exploratory）在每个结论处标注，† 标记 sample-limited 结果。主动披露 M002 Bug（Appendix N）和高 FPR（11-50%）。

3. **统计方法论严谨**: BCa bootstrap（10,000 resamples, trace-level clustering）、Holm-Bonferroni step-down 校正、nested 5-fold CV、control task selectivity（Hewitt & Liang 2019 框架）、exact permutation test（32B）。方法论执行质量在同领域论文中属上乘。

4. **负面结果有价值**: 系统测试 7 种替代方法（BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-model transfer）均未优于监督探针，为后续研究提供有用的 baseline elimination。

5. **诚实的 self-limitation**: "Characterize rather than detect" 定位、acknowledgment of garden-of-forking-paths concern、oracle gap 量化（76.7% for R1-8B）。

---

## Weaknesses

### Must-Fix（6 个，两位 Reviewer 均达成共识）

**N1** [critical | consensus: R1 提出, R2 AGREE] **Position control 叙事误导: 主文称 "3/4 models retain significant non-positional HS advantage"，quadratic control 下实际为 2/4**

Section 5 Discussion 仅基于 linear residualization 报告 "3/4" 这一 headline number。Appendix V Table 26 显示 quadratic $(t/T)^2$ control 下 QwQ-32B 优势被完全吸收（−1.0pp, NS），R1-32B 两种 control 下均 NS，仅 R1-8B (+10.3pp) 和 OT-7B 保持显著。主文以括号形式附带提及 QwQ-32B 的 quadratic 结果，但未修正核心数字。这直接关系到 HS 优势是否为 genuine safety signal 还是 positional artifact 的中心论断。

**N2** [critical | consensus: R1 提出, R2 AGREE with nuance] **HB 校正范围（12 tests）低估 cumulative researcher degrees of freedom**

HB 校正仅覆盖最终 4 models × 3 metrics = 12 comparisons，但实际分析管线涉及 5 种 layer selection metrics × 7 种 W × 5 种 K × 28-64 candidate layers × evidence tier 分类。论文提及 "garden-of-forking-paths concern"（Gelman & Loken 2013），但未量化总探索空间，也未论证 12-test 边界的选择理由。R2 指出 split-sample 策略（K/threshold 在 R1-8B validation 上选定 held fixed）提供部分缓解，但 Limitations 中仍缺乏显式讨论。

**N3** [critical | consensus: R1 提出, R2 AGREE] **"Threshold-based metrics converge by mathematical necessity" claim 数学上不成立**

Abstract 和 Section 4.2 反复声称 threshold-based metrics "share a common confusion matrix and converge by mathematical necessity"。但 "converge" 指 layer selection 的 argmax 一致——R1 提供反例：不同 class balance 下 precision 和 BA 的 argmax 可以分歧。论文观察到的是 empirical convergence（在这些特定模型和数据上），不应包装为 mathematical theorem。

**N4** [critical | consensus: R2 提出, R1 AGREE（部分反驳严重性）] **遗漏关键相关工作: Chan & Yong (2025) "Can We Predict Alignment Before Models Finish Thinking?"**

arXiv:2507.12428 直接使用 CoT activations 上的线性探针预测 reasoning model 的 final response safe/unsafe，报告 +13 F1 over text baselines，与本文 Contribution 2 高度重合。R1 指出三个关键差异（检测目标不同、无 layer selection analysis、本文 characterization 是 conditional 的），Contribution 1 不受影响，但 "HS > text" 这一 high-level finding 不再完全新颖。

**N5** [critical | consensus: R2 提出, R1 AGREE] **核心新颖性定位模糊: 与 "不同层编码不同信息" 的已有认知区分度不足**

"不同层编码不同信息"是 probing 研究的基本认知（Tenney et al. 2019; Alain & Bengio 2017）。论文需更清楚地论证其发现超越这一泛泛认知：不仅是层选择敏感，而是**标准层选择指标引入系统性偏差**（如 CR-composite 在 random labels 下仍 100% 选浅层）。两位 Reviewer 均建议将 Contribution 1 重新框定为 "metric-induced systematic bias"。

**N6** [critical | consensus: R2 提出, R1 AGREE] **纯诊断论文缺乏解决方案**

论文诊断了层选择敏感性问题但未提出或验证任何修复方案。Discussion 引用 Pais et al. 2026 multi-layer ensembling 为 "complementary solution" 但仅停留在引用层面。R1 指出 Appendix W 已有构建 layer-robust 方案的素材。至少需要一个 proof-of-concept（如 multi-layer ensemble 或多指标投票），即使结果不理想也比完全回避更有说服力。

### Should-Fix（13 个，含 2 个分歧）

**W1** [warning | consensus] BCa bootstrap CI 在 n=17-20 下可靠性不足（acceleration parameter â jackknife 不稳定）。R2 指出主要影响已标为 exploratory 的 32B 结果，实际风险有限。

**W2** [warning | consensus] LOO-CV 层选择不稳定性在 32B 达 35-40%（dominant layer agreement 仅 65-68%）。需 sensitivity analysis：top-N 候选层分别计算 HS advantage 方向和显著性。

**W3** [warning | consensus with nuance] R1-32B 仅 W=1 显著，coverage 25%。"Exploratory" 标记已是 caveat，但可更显式标注 post-hoc 选择性质和 noise-fitting 风险。

**W4** [warning | consensus] 架构同质性（3/4 Qwen）caveat 不足。正文频繁将 R1-8B (Llama) 和 OT-7B (Qwen) 并列，给人跨架构一致性印象。应在首次并列处标注架构。

**W5** [warning | consensus] Discussion Section 5 中 "likely generalizable to any threshold-based detection study" 在单一数据集下过于笃定。需加条件限定。

**W6** [warning | consensus] Evidence gradient 中 "significant" 易与统计显著性混淆。建议改用 "supported" 或 "corroborated"。

**W7** [warning | consensus（R1 strongly agree）] R1-8B FPR seed-sensitivity（3/5 seeds pass HB, std=0.115）在 Abstract "confirmatory" 措辞下不够突出。Abstract 应增加 seed-sensitivity caveat。

**W8** [warning | consensus] bib 条目 safeint2025 和 rcs2026 作者字段为 "others"，不符合 ACL style 规范。

**W9** [warning | consensus] geiger2025causal 年份标注为 2025，JMLR 发表年份实为 2023（待核实）。

**W10** [warning | consensus] QwQ-32B 优势被 quadratic control 完全吸收，n=17 下难以区分 overfit 还是 genuine positional artifact。需讨论 bias-variance tradeoff。

**W11** [warning | R1 agree with reservation] 缺少 Kadali & Papalexakis (2026) 扩展版引用（R1 无法独立确认存在，需作者核实）。

---

## Reviewer Consensus

以下关键问题两位 Reviewer 达成共识 [AGREE]：

1. **Position control 3/4→2/4 误导性**（R1-N1）: 两位均同意主文 headline number 需修正以反映 quadratic control 结果
2. **"Mathematical necessity" claim 不成立**（R1-N3）: 两位均同意 argmax 一致性是 empirical regularity 而非数学定理
3. **遗漏 Chan & Yong 2025**（R2-N1）: 两位均同意应引用，R1 补充该工作与本文检测目标不同（final response vs CP）
4. **新颖性需重新框定**（R2-N2）: 两位均建议从 "layer selection matters" 转向 "metric-induced systematic bias"
5. **需至少一个解决方案**（R2-N3）: 两位均同意纯诊断论文需要 proof-of-concept
6. **R1-8B FPR seed-sensitivity**（R2-W6）: R1 强烈同意——40% 概率在不同划分下 "confirmatory" 地位不成立
7. **"Significant" 术语歧义**（R2-W3）: 两位均建议替换为无歧义标签

## Reviewer Divergence

两个 Should-Fix 级别的分歧：

**D1: Fixed K=5 是否低估 32B HS advantage**
- R1: Fixed K=5 可能 systematically underestimate 32B 模型的 HS 优势
- R2 [REBUT]: 固定 K 是正确方法论选择（避免小样本 overfit），Appendix E 已验证 K 不敏感。如果低估了 32B 优势，结论更保守反而更可信。
- **评估**: R2 论据更有说服力。Fixed K 是 split-sample 策略的一部分，R1 的关切已被实验数据（Table 18 K-ablation）部分消解。

**D2: "Confirmatory" 术语是否误导**
- R1: post-hoc 分析称 "confirmatory" 有误导性，应改为 "corroborating"
- R2 [REBUT]: 论文明确定义为 validation strategy（nested CV + hold-out），已承认 post-hoc 性质。在 probing 文献中有先例。
- **评估**: 分歧实质轻微。两位均同意 "significant" 术语应改（R2-W3），R2 建议首次使用 "confirmatory" 时加脚注定义——这一折衷方案合理。

---

## Questions

1. Chan & Yong (2025) 使用 CoT activations 预测 final response alignment——该工作是否研究了层选择对结论的影响？如未研究，这是本文 Contribution 1 的独特增量。
2. R1-32B 在 W=1 时的 25% coverage 检测：这 5/20 条 trace 是否有系统性特征（如特定 harm category、特定长度区间）？
3. Quadratic control 在 n=17 下是否有 overfit 风险——作者能否在 7-8B 模型（n 较大）上比较 quadratic vs 更高阶/non-parametric position control？
4. Multi-layer ensembling（Pais et al. 2026）是否在当前数据上验证过？如有初步结果应纳入论文。

---

## Missing References

1. **Chan & Yong (2025)** "Can We Predict Alignment Before Models Finish Thinking?" (arXiv:2507.12428) — 直接使用 CoT activations 线性探针做安全预测，+13 F1 over text baseline [两位 Reviewer 共识]
2. **Kadali & Papalexakis (2026)** — 如存在 arXiv:2510.06594 的扩展版本，应更新引用 [R2 提出, R1 agree with reservation]

---

## External Review (Stanford Agentic Reviewer)

外部审稿未配置（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 状态: **timeout**（715 秒后超时）。本轮未获得视觉审查结果。

基于 PDF 阅读的基本排版观察：
- 主正文约 8 页（Section 7 Limitations 从第 8 页开始），符合 EMNLP 2026 Long paper 8 页限制
- ACL template 正确（`\usepackage[review]{acl}`）
- 匿名化正确（"Anonymous ARR Submission"）
- Figure 1 heatmap 信息密度高，打印时可能难以辨认（R2 小问题 #3）
- 28 页总长度（8 页正文 + 约 4 页 references + 16 页 appendix）

---

## Overall Assessment

**评分: 3.0 — Findings**
**置信度: 4/5（两位 Reviewer 独立审稿 + 完整交叉分享，关键问题达成共识）**

**评分依据**:

两位 Reviewer 独立评分均为 3.5（Borderline Conference），但交叉分享后全部 6 个 Must-Fix 获得共识确认，整体问题负担将评分拉至 3.0：

1. **核心贡献有效但范围较窄**: 层选择指标引入系统性偏差是真实且有用的方法论警告，但（a）与已有 probing 认知的区分度需加强（N5），（b）遗漏了直接相关的竞争工作（N4），（c）纯诊断定位无解决方案（N6）。
2. **统计 claim 需修正**: "Mathematical necessity"（N3）和 "3/4 models"（N1）的表述均不准确，前者是逻辑错误，后者是选择性呈现。对于以方法论严谨性为核心卖点的论文，这些问题不可忽视。
3. **HB 校正范围讨论缺失**（N2）: 论文给读者 "已做多重校正" 的印象，但实际仅校正了末端 12 tests，未量化或讨论 cumulative researcher degrees of freedom。
4. **缓解因素**: 实验设计全面（26 个附录）、透明度高（evidence gradient + bug disclosure）、负面结果有价值。这些品质使论文适合 Findings 接收。

**如果作者完成以下修改，论文有望从 3.0 提升至 3.5-4.0**:
- 修正 N1（position control 叙事）和 N3（mathematical necessity claim）——文字修改，1-2 天
- 补充 Chan & Yong 2025 引用和对比讨论（N4）——文字修改，1 天
- 重新框定新颖性为 "metric-induced systematic bias"（N5）——framing 重组，1-2 天
- 添加至少一个 proof-of-concept 解决方案（N6）——需实验，2-3 天
- 量化 researcher degrees of freedom 并论证 HB 边界（N2）——分析 + 写作，1 天

---

## Detailed Comments

### Abstract (p.1)
- "threshold-based metrics share a common confusion matrix and converge to the same deep layer by mathematical necessity" → 修正为 empirical observation（N3）
- "confirmatory at 7-8B" 后应添加 R1-8B FPR seed-sensitivity caveat（W7）
- † 符号内联定义略拥挤但清晰

### Section 1 Introduction (p.1-2)
- Contribution 1 措辞需从 "layer selection sensitivity" 转向 "metric-induced systematic bias in layer selection"（N5）
- 与 Chan & Yong 2025 的关系需讨论（N4）
- "primarily Qwen-based (3/4 models)" 的 caveat 已存在，但 Introduction 后续讨论中容易被遗忘

### Section 2 Related Work (p.2-3)
- 引用完整性总体良好（68 条 bib，无孤立/缺失条目）
- 需补充: Chan & Yong 2025 (N4), 可能的 Kadali 2026 扩展版 (W11)
- bib 修复: safeint2025/rcs2026 作者 "others" → 补全 (W8); geiger2025causal 年份 2025→2023 (W9)
- Pais et al. 2026 已引用但仅作为 "complementary solution" 提及——应在有实验验证后扩展讨论（N6）

### Section 3 Methods (p.3-5)
- Section 3.3 Layer Selection Sensitivity: "by mathematical necessity" 需修正（N3）
- Section 3.5 Evaluation Protocol: bootstrap 描述为 "resampling traces as clusters"——符合 trace-level 重采样（R19 R1-N1 可能已修复）
- 12-test HB 的边界选择理由需补充（N2）

### Section 4 Experiments (p.5-7)
- Section 4.3 HS vs Text: 7-8B 结果首次并列时应标注架构 (R1-8B [Llama], OT-7B [Qwen])（W4）
- Section 4.3 Position mediation: 需同时报告 linear 和 quadratic 两种 control 的结果数字（N1）
- Section 4.4 32B Analysis: R1-32B W=1 的 post-hoc 选择性质需更显式标注（W3）
- Section 4.2: "by mathematical necessity" 两处出现，均需修正（N3）

### Section 5 Discussion (p.8)
- "Three of four models retain significant non-positional HS advantage" → 同时报告 quadratic 下 2/4（N1）
- "likely generalizable to any threshold-based detection study" → 加条件限定（W5）
- "Guidance for future research": multi-layer ensembling 不应仅是引用，需实验验证（N6）
- QwQ-32B position-mediated advantage 应标记为 "inconclusive pending larger sample"（W10）

### Section 6 Conclusion (p.8)
- 简洁合理，但需反映 N1 和 N5 的修正

### Section 7 Limitations (p.8-9)
- 全面且诚实
- 应补充: (1) HB 仅覆盖 12 tests 是对 Type I error 的 underestimate（N2）; (2) "confirmatory" 定义为 validation strategy 而非 pre-registration 的脚注（D2）

### Appendix (p.10-28)
- 极其详尽（26 个附录），大大增强可复现性
- Table 26 (Appendix V) 的 quadratic position control 结果应在主文更显著地讨论（N1）
- Appendix N M002 Bug Disclosure 展示良好科学诚信

### Figures
- Figure 1 (Layer heatmap): 信息密度高，打印可读性可能受限
- Figure 2 (Forest plot): 清晰直观地展示 encoder-conditional HS advantage

---

**Issue Tracker 已同步更新**: `projects/contrastive_trace_safety/artifacts/review_issues.yaml`（19 条 issue: 6 Must-Fix + 11 Should-Fix + 2 Divergence，含 R19 遗留问题跟踪）
