---
round: 25
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T14:42:46.038603+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 26 (Fresh Review)

**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition"
**Venue**: EMNLP 2026 Main Conference (via ARR May 2026)
**Deadline**: 2026-05-25
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）

---

## Summary

论文研究 test-time compute scaling (self-consistency) 应用于 NER 的效果，评估 5 种 confidence signals（Soft Jaccard, voting confidence, Fleiss' κ, exact match, log-probability）在 4 个 NER benchmark 上的 quality estimation (QE) 和 sample selection 表现。核心发现：所有信号能做可靠的 QE（ρ up to 0.45, AUROC up to 0.82），但无法可靠地选出最优 sample——作者称之为"correlation-selection gap"。论文提出 entity-level construction（实体级聚合）作为缓解方案，在 Few-NERD 上获得 +1.40pp（Holm p_adj=0.006），并给出 degeneracy decomposition 的理论分析。

---

## Strengths

1. **统计方法论远超 NLP 社区平均水平** [R1, R2 共识]：Holm-Bonferroni 多重比较校正（family k=10/19/57）、bootstrap CI (B=10,000)、MDE/power analysis、TOST equivalence testing、permutation tests。这种严谨性在 NER/IE 论文中极为罕见，具有示范价值。

2. **Correlation-selection gap 概念清晰、有实际价值** [R1, R2 共识]：核心观察——信号能估质量但选不出最优 sample——对 NER practitioners 直接有用，改变了 test-time scaling 的使用策略。

3. **实验设计系统全面** [R2]：5 signals × 4 datasets × 2 models × 4B-8B fine-tuned + 72B zero-shot，覆盖难度梯度（WNUT-17 ~42% → CoNLL >90% F1）。

4. **Diagnostic cascade 有洞察力** [R1, R2]：degeneracy → headroom → LP compression 的层级分析为理解"为什么信号选不出最优"提供了直觉和可复用的诊断协议（Appendix ab）。

5. **极其详尽的附录** [R1, R2 共识]：30+ 页、55 个表格，涵盖 temperature/LoRA rank/free-form decoding ablation、calibration、hidden state probes、per-entity-type 分析。

6. **负面结果的诚实报告** [R1]：trained verifier 失败（§5.2）、cross-model 仅 preliminary（§5.1）、construction 在 CoNLL 无效（§7.5）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[W-Critical-1] "Correlation-selection gap" 对 4/5 信号是 structural tautology，framing 过度渲染 novelty** [R1-N1 + R2 交叉 AGREE，共识]

论文评估的 5 个信号中，4 个（SJ, VC, FK, EM）是 instance-level aggregates——对同一 instance 的所有 N 个 candidates 赋予相同分数。它们根据定义无法做 within-instance ranking。论文自己在 §4 (p.4) 承认："selection failure is a design property, not an empirical finding"。但 Abstract 和 Introduction 的 framing 没有前置这个关键区分，读者会以为 5 个信号都是 selection 的候选者，产生虚假 surprise。

真正的 empirical 贡献——LP（唯一 per-sample 信号）因 compression 失败（within-instance range ≈0.041 nats, 60% instances; §4, Figure 8）——在当前 framing 下被淹没。

**修改要求**：重构 Abstract/Intro，将 structural（4/5 信号 by construction 不能 select）与 empirical（LP compression failure）明确区分并前置。

**[W-Critical-2] Entity-level construction 新颖性不足，缺少关键引用** [R2-N1 + R1 交叉 AGREE，共识]

- EL4NER (arXiv:2505.23038, May 2025) 已系统实现了基于多 LLM 的 entity-level span extraction + type voting pipeline，在 ICL 设置下取得 SOTA。**未被引用**。
- Xie et al. (2023a) 已是 entity-level voting 的先驱，论文自己引用但未充分区分。
- Entity-level construction 本质上是将已有的 entity voting 在 MBR 框架下重新包装（LP-weighted variant 仅额外 +0.30pp over uniform）。
- +1.40pp (Few-NERD) 和 +1.02pp (SciERC, p_adj=0.20 不显著) 的改进有限。

**修改要求**：补引 EL4NER 并区分（单模型 SC vs. 多模型 ensemble）。将 construction 定位为 diagnostic-motivated ablation 而非 standalone contribution。

**[W-Critical-3] "First systematic characterization" overclaim** [R2-N3 + R1 交叉 AGREE，共识]

Abstract 声称"the first systematic characterization"，但 Chen et al. (2023) 已研究 SC failure modes、Eikema et al. (2025) 已研究 structured MBR decoding 失效、Kang et al. (2025) 和 Taubenfeld et al. (2025) 已研究 confidence signals 与 SC。论文的"first"仅限于 NER + 这 5 个信号的组合。

**修改要求**：限定 scope 为 "for NER" 或 "in the context of structured entity extraction"。

**[W-Critical-4] 参考文献存在年份错误和疑似虚构引用** [R2-N4 + R1 交叉 AGREE，独立验证确认]

| 问题 | 详情 |
|------|------|
| chen2025twofailures | bib 标注 2025，实际发表于 2023 (arXiv:2305.14279) |
| feng2025optimal | bib 首作 "Feng"，API 返回 "Austin"——需核实 |
| park2024grammar | bib 首作 "Park"，API 返回 "Berg-Kirkpatrick"——可能张冠李戴 |
| **hobelsberger2025systematic** | **Semantic Scholar/OpenAlex 均无法验证（similarity=0.236），疑似虚构引用** |
| 17 orphan bib entries | 在 .bib 中但未被 \cite（包括 openai2024o1, min2022rethinking 等） |

**修改要求**：立即核实 hobelsberger2025systematic 真实性（若虚构是严重学术诚信问题）。修正年份和作者错误。清理 orphan entries。

**[W-Critical-5] Construction 效果跨数据集不一致，p_adj 数值矛盾** [R1-N2 + R2 交叉 AGREE，共识]

- Few-NERD: +1.40pp（Holm p_adj=0.006，显著）✓
- SciERC: +1.02pp — §1 报告 p_adj=0.20（不显著），但 R1 指出 Table 13 显示 p_adj=0.038——**同一结果在不同位置给出不同 p_adj，属报告失误**
- CoNLL: -0.39pp（不显著）✗

4 个数据集中仅 Few-NERD 统计显著，construction 作为 contribution 的可靠性受限。

**修改要求**：澄清 p_adj 矛盾。正文醒目标注 SciERC 不显著。讨论仅 1/4 数据集显著的适用范围。

### Should-Fix（影响评分但不一票否决）

**[W-Warning-1] N=8/16 对 test-time compute scaling 研究范围过窄** [R1-W1 + R2 AGREE]
相关文献测试到 N=64+。Few-NERD N=16 LP 仍有 +0.30pp gain，存在继续 scaling 空间。至少补 N=32 或论证 cost-efficiency。

**[W-Warning-2] Scale/regime confound 未充分控制** [R1-W2 + R2-W1，共识]
Fine-tuned 4B-8B vs. zero-shot 72B 同时变化 fine-tuning、model size、architecture、quantization。需 hedge 结论或补控制实验。

**[W-Warning-3] Cross-model consistency 过于初步** [R1-W3, R2 部分 REBUT]
仅 1 数据集 1 对模型，但论文标注为 "exploratory"。R2 认为定位合理，但若保留在 §5.1 需补实验或缩减为 footnote。

**[W-Warning-4] SciERC 部分关键分析基于 single seed** [R1-W4 + R2 AGREE]
SciERC 仅 551 instances，用于 detailed diagnostic 但 single seed。bootstrap CI 有缓解但与论文整体统计标准不一致。

**[W-Warning-5] Degeneracy decomposition 过松** [R2-N2, R1 部分 REBUT]
R2 称 bound 仅解释 3-12% 的 gap。R1 REBUT 称论文给的是 equality 非 bound，但同意可降级为 analysis tool。分歧点在于 "3-12%" 的出处和 decomposition 的实用价值。**共识**：降级为 analysis tool 而非独立 contribution。

**[W-Warning-6] Diagnostic cascade 是描述性分析而非因果链** [R2-W2, R1 AGREE with nuance]
三个因素（degeneracy, headroom, LP compression）是 correlational structure，未排除第三变量。Entity construction 实验部分建立因果性。共识：标注为 "descriptive diagnostic" 更准确。

**[W-Warning-7] 论文同时做 4 件事，各自深度不够** [R2-W3, R1 部分 REBUT]
R2 认为 QE benchmark + selection failure + construction + theory 各 0.5-1 页，深度不够。R1 认为四部分构成完整故事但同意可重新分层为 2 core + 2 supporting。

**[W-Warning-8] Missing related work** [R2-W4, R1 conditionally AGREE]
缺少：EL4NER (arXiv:2505.23038)、Beyond Majority Voting (arXiv:2510.01499)、Scalable BoN via Self-Certainty (arXiv:2502.18581)、Optimal Aggregation (arXiv:2510.13918)。

**[W-Warning-9] Trained verifier 负面结果 scope 有限** [R1-W5, R2 部分 REBUT]
LightGBM 仅在 SciERC 上测试。R2 指出 AUC=0.923 说明特征足够，问题在于 discrimination→selection 转化。共识：soften 结论从 "cannot close" 到 "do not close in our setting"。

---

## Reviewer Consensus [AGREE]

1. **Framing 需重构**：Abstract/Intro 必须前置 structural/empirical 二分法，突出 LP compression 作为核心 empirical finding [R1-N1 + R2 AGREE]
2. **Construction 应降级**：从 standalone contribution 降为 diagnostic-motivated ablation，补引 EL4NER [R2-N1 + R1 AGREE]
3. **Overclaim 需限定**："first systematic characterization" 限定到 NER [R2-N3 + R1 AGREE]
4. **引用必须修复**：hobelsberger2025systematic 疑似虚构需立即核实 [R2-N4 + R1 独立验证 AGREE]
5. **p_adj 矛盾必须澄清**：SciERC construction 在 §1 和 Table 13 的数值不一致 [R1-N2 + R2 AGREE]
6. **统计方法论是亮点**：Holm-Bonferroni, bootstrap CI, MDE/power analysis 远超 NLP 社区水准 [R1 + R2 共识]
7. **论文适合 Findings**：有用的 empirical study + 统计示范价值，但 novelty 和 practical impact 不足以支撑 Main Conference [R1 + R2 共识]

## Reviewer Divergence [REBUT]

1. **Degeneracy decomposition 的性质**：R1 称论文给的是 equality（E[ΔF₁] = (1−D)·G_nd），R2 称是 bound 且仅解释 3-12%。R1 认为有 diagnostic 价值（快速判断 SC 可行性），R2 认为过松无实用性。**双方同意降级为 analysis tool。**

2. **Cross-model experiment scope**：R1 认为过于初步需扩展或降级；R2 认为标注为 exploratory 定位合理，无需过多期待。**双方同意若保留需明确定位。**

3. **Trained verifier 结论**：R1 认为 scope 有限不够 conclusive；R2 认为 AUC=0.923 恰恰说明问题在 discrimination→selection 转化而非特征不足。**双方同意 soften 结论。**

---

## Questions（需作者澄清）

1. SciERC entity construction 的 p_adj 到底是 0.20 还是 0.038？两处不同的数值源于哪个 Holm family 分组？
2. hobelsberger2025systematic 是否为真实出版物？如果是，请提供具体的出版信息（期刊/会议、DOI）。
3. 如果 4/5 信号 by construction 不能做 selection，为什么 Abstract 仍将"5 confidence signals for QE and sample selection"并列？这是否误导读者？
4. Cross-model consistency 的 +0.42pp（§5.1）是否在 R1 引用的 CI [0.27, 0.58] 内？还是 R1 看到的是 +0.32pp CI [0.27, 0.38]？数值需确认。
5. Proposition 1 的 entity-wise independence 假设在何种 NER 场景下会被 violated？嵌套实体是否会导致 bound 失效？

---

## Missing References

以下为两位 Reviewer 共同或独立建议补充的引用：

1. **EL4NER** (arXiv:2505.23038, May 2025) — entity-level span extraction + type voting 的 ensemble NER pipeline [R2 提出, R1 AGREE, **必须引用**]
2. **Beyond Majority Voting** (arXiv:2510.01499, Oct 2025) — 超越 majority voting 的 aggregation 方法 [R2]
3. **Scalable Best-of-N Selection via Self-Certainty** (arXiv:2502.18581) — 直接相关的 BoN selection 方法 [R2]
4. **Optimal Aggregation of LLM and PRM Signals** (arXiv:2510.13918) — 多 signal 聚合理论框架 [R2]

---

## External Review

**外部审稿：未请求**（项目未配置 external_review）

---

## Visual Layout Check（非评分项）

视觉审查已完成（状态: done）。主要发现：

- **[Critical] Page 7 display items 严重过密**：4 个表格（Table 2/3/4/5）+ 1 个 figure（Figure 3）挤在同一页，Figure 3 条形图极小，可读性差。相邻 page 6 和 page 8 均为纯文本——视觉节奏极不均匀。**建议移动部分 items 到 p6/p8**。
- **[Warning] Pages 6, 8 纯文本**：无任何 figure/table/equation，形成"文-密-文"不良节奏。
- **[Warning] Page 42 末页 ~75% 空白**，Page 34 ~60% 空白。
- **[Warning] Pages 36-41 附录表格密度极高**：部分字号接近 7pt 可读性边界。
- **[Info] Figure 6 (p18) heatmap 红绿色阶对色盲不友好**：建议改用 viridis 或 blue-orange。
- **[Info] 正面**：booktabs 风格统一，公式渲染正确，无 [?] 未解析引用，无 margin 溢出。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 2.5 | 3.0 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4 | 4 | 4 |

**评分理由**：

论文是一项扎实的实证研究，core insight（LP compression 作为 NER selection failure 的根本原因）有诊断价值，统计方法论在 NLP 社区具有示范意义。但存在以下主要问题阻碍主会议接收：

1. **Novelty 受限**：核心概念"correlation-selection gap"对 80% 的信号（4/5 instance-level）是定义上的必然而非实验发现，framing 制造了虚假 surprise；entity-level construction 是已有方法的迁移应用且效果不一致。
2. **Contribution 深度不够**：4 个 contributions 各自偏浅——construction 仅 1/4 数据集显著，degeneracy bound 太松（R1/R2 分歧但同意降级），论文试图同时做太多事情。
3. **引用问题严重**：疑似虚构引用（hobelsberger2025systematic）、年份/作者错误、缺少直接相关工作（EL4NER）。
4. **实验覆盖有限**：N=8/16 偏小，scale confound 未控制，cross-model 过于初步。

**定位建议**：如果作者 (1) 重构 framing 聚焦 LP compression 作为核心 empirical finding，(2) 将 construction 和 decomposition 降级为 supporting analyses，(3) 修复引用问题，(4) 限定 overclaim scope——论文在 Findings 中将是一篇有价值的诊断性工作。统计方法论值得社区学习。

---

## Detailed Comments

### Section 1 (Introduction)
- Contribution #2 中 "That 4/5 signals are instance-level is definitional; the empirical contribution is that LP..." 这句话应该出现在 Abstract 和 Intro 前几段，而非埋在 contribution list 中。当前读者需要读到 §3-4 才能理解核心概念的 80% 是 trivial 的。
- "first systematic characterization" → "first systematic characterization for NER"

### Section 3 (Diagnostic Framework)
- §3.1 对 instance-level vs. per-sample 的区分是论文最重要的 methodological insight，应 promote 到 Introduction。
- FK 的 "inter-rater agreement" 描述不准确——实际是 type-level agreement across N samples，非标准 inter-rater reliability 场景。

### Section 4 (Why Single-Signal Selection Fails)
- "Definitional vs. empirical" 区分在 §4 首段出现太晚，应在 §1 前置。

### Section 5 (Adaptive Methods)
- §5.1 Cross-model: 仅 1 数据集 1 对模型，+0.42pp。要么补实验要么缩减为 footnote。
- §5.2 Trained verifier: AUC=0.923 但 +0.30pp——结论 "cannot close" 改为 "do not close in our setting"。

### Section 6 (Threshold Regime Analysis)
- §6.3 Degeneracy decomposition: 论文称 equality，bound ratio 3-12%（争议）。建议明确定位为 diagnostic tool。
- Proposition 1 的 entity-wise independence 假设未讨论何时 violated。

### Section 7 (Experiments)
- Table 5 construction results: p_adj 矛盾需修复。
- CoNLL -0.39pp 负面结果值得更多分析（是 degeneracy 还是 headroom 不足？两者在 CoNLL 上同时成立）。
- Few-NERD 3 epochs vs 其他 5 epochs: 主文应解释原因。

### Section 8 (Discussion)
- LP compression 的 mechanistic 解释（exposure bias, constrained decoding 压缩 LP 动态范围）已有但可加深。
- Diagnostic cascade 应标注为 "descriptive" 而非暗示因果关系。

### References
- 立即核实 hobelsberger2025systematic。
- 修正 chen2025twofailures 年份（2023 非 2025）。
- 核实 feng2025optimal 和 park2024grammar 作者信息。
- 补引 EL4NER。
- 清理 17 条 orphan bib entries。

### Format/Layout
- Page 7 过密（4 表 +1 图），建议分散到 p6/p8。
- Figure 6 heatmap 色阶对色盲不友好。