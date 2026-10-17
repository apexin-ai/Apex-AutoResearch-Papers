---
round: 12
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T23:02:27.109950+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 14 审稿报告

**论文**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation
**Venue**: EMNLP 2026 via ARR (May cycle)
**截止日期**: 2026-05-25
**审稿模式**: Fresh（第 14 轮）
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 统计方法学 + 实验设计；R2: 新颖性 + framing + 写作质量 + 完整性）

---

## Summary

论文提出 Controlled Style Decomposition (CSD)，通过 NLI 门控内容保持、per-axis 风格改写和 position-controlled pairwise comparison，系统量化了 LLM judge 在 Likert 和 pairwise 两种评分模式下的风格敏感度差异（"Likert Blindspot"）。在 4 个 target judge、1 个负控制、2 条主要风格轴（formality, verbosity）和 3 个 benchmark 上，pairwise 方法一致检测到 Likert 无法检测的风格偏好。GEE 条件分解揭示了轴间异质性的 confound 结构：verbosity 是 style-dominated（Style OR 8-13），formality 是 conditional effect。

---

## Strengths

**S1** [两位共识] **方法论严谨度在 NLP 实证论文中罕见**。三重控制（NLI 门控 + position control + same-text pairing）、7 种测量方法交叉验证（Table 2）、GEE 相关结构鲁棒性检查（Appendix C）、bootstrap attenuation 分析（Appendix J）、power analysis（Appendix K）——每一项都不是走流程，而是 genuine diagnostic。

**S2** [两位共识] **GEE per-axis confound 结构差异是最有价值的增量贡献**。Table 3 揭示 verbosity 是 style-dominated（Style OR 5-13，Orig OR < 1）而 formality 是 conditional effect（Style OR 和 Orig OR 均显著），为 practitioners 提供了可操作的诊断框架——哪些轴的评估结果可直接解读，哪些需要 decomposition。

**S3** [两位共识] **跨 4 个独立 judge 架构的复现**。GPT-4o、Qwen3-32B、Llama-3.3-70B、Gemini-2.5-Flash 覆盖不同训练策略和架构，Blindspot 在所有 target judge 上一致复现，增强了泛化性。

**S4** [两位共识] **统计分析深度**。FWER 校正（Holm-Bonferroni 6-test 和 8-test 灵敏度）、GEE interaction tests（9 个 judge×axis cells 全部不显著）、NLI 阈值 sweep（11 个阈值 BT 变化 ≤3pp）、bootstrap attenuation curve（7 个样本量 d_median ≈ -0.017 恒定）。

**S5** [R2] **诚实的 Limitations**。Quality-style confounding、construct validity、evaluator-producer bias 三个核心局限均被坦率讨论。

**S6** [R1] **实际影响清晰**。"Likert-only audits may fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines"——对 NLG evaluation pipeline 设计提供了直接可操作的警示。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [R2 提出, R1 AGREE] **"Framework" 泛化声明与实际覆盖不匹配**
Section 1 将 CSD 定位为通用 "black-box framework for per-axis style bias detection"，但仅测试 formality、verbosity、register 三条表面文本属性轴。对 semantic-level 风格轴（hedging, humor, technicality），NLI 门控可能系统性拒绝合法 rewrite——这是论文未讨论的 false positive 维度（区别于已讨论的 false negative 问题）。R1 补充：这不仅是范围问题，更是 NLI gate 的结构性适用限制。
→ 建议：降级为 "methodology"/"experimental protocol" 或限定为 "surface-level stylistic attributes amenable to content-preserving rewriting"。

**MF2** [R1 提出, R2 AGREE] **NLI Gate 人工验证标注一致性不足，样本量偏小**
两名标注者在 50 对样本上 Cohen's κ=0.44（moderate），gate-passed 25 对 Wilson CI 下界 86.76% 意味着 ~13% 可能存在语义变化。对于以 measurement methodology 为核心贡献的论文，pipeline 核心组件的 validation 标准应更高。R2 补充缓解观察：BT 在 11 个 NLI 阈值上变化 ≤1pp（Appendix E），说明 downstream metric 对阈值不敏感——但 sample size 仍是硬伤。
→ 建议：增加标注者至 ≥3 人 + 报告 Fleiss' κ + 对 verbosity condensation 分歧案例进行定性 error analysis。

**MF3** [R2 提出, R1 AGREE] **核心发现的增量新颖性论证不足**
Forced-choice > absolute rating 是 Thurstone (1927)、Stevens (1946)、Krosnick (1999)、Preston & Colman (2000) 反复验证的经典心理测量结论。论文在 Section 2 引用了这些工作，但未充分论证在 LLM judge 领域"重新量化"此现象的独立新颖性。R1 同意但指出 GEE decomposition 的 per-axis confound 结构差异是 genuine insight——论文应将 novelty 重心从"发现 divergence"转向"quantifying and decomposing per-axis confound structures"。
→ 建议：重构 novelty narrative，Abstract/标题突出 GEE decomposition 方法论贡献，将 divergence 发现降为 motivating observation。

**MF4** [R1 提出, R2 部分 AGREE] **TOST 等价检验 Δ=15pp 缺乏外部校准，负控制论证力不足**
Δ=15pp 理由是"approximately where format preference would materially affect model rankings"——校准标准不够透明。Δ=10pp 下 Claude 未通过等价检验（p=0.156），BT=56.2%（偏离 chance 6.2pp）。R2 REBUT "循环论证"标签（SESOI 在实践中很少有外部金标准），但 AGREE 校准不足。共识：正文需讨论不同 Δ 下结论变化 + 将 Claude 从 "negative control" 重新 framing 为 "weak-effect/attenuated-bias control"。

---

### Should-Fix（影响评分但不一票否决）

**SF1** [R2 提出, R1 AGREE] **Construct divergence 解释发展不足**
三种解释中，construct divergence（两种模式测量不同构念）在理论上最有趣但讨论最薄弱——Section 5.1 仅一句话。如果 construct divergence 是正确解释，"Blindspot" 就不是缺陷而是自然结果，根本改变 practical implication narrative。
→ 建议：Section 5.1 用一段专门讨论 construct divergence 的含义和可检验预测。

**SF2** [R2 提出, R1 AGREE] **Claude Sonnet 4 负控制结果讨论不充分**
Claude 不展示 Blindspot 暗示这可能是 model-specific training artifact 而非 measurement-mode intrinsic property——对论文核心叙事构成潜在挑战。论文将此归因于"RLHF training composition"但未深入分析。
→ 建议：讨论 Claude 负结果对 "measurement-mode divergence" 叙事的含义——是否说明 Blindspot 可通过训练消除？

**SF3** [R1 提出, R2 AGREE] **Bootstrap CI 方法类型未报告**
论文报告"10,000 pair-level resamples"但未指明 percentile vs BCa。对 bounded [0,1] 参数（BT win probability），percentile intervals 在小样本下覆盖率可能不足。
→ 建议：明确报告 CI 类型。

**SF4** [R1 提出, R2 AGREE] **BT 模型 unidimensionality 假设仅在脚注讨论**
BT 假设单一潜在"quality"维度。对以 measurement methodology 为核心贡献的论文，此假设的讨论不应止于脚注。
→ 建议：提升到 Limitations，讨论违反条件和影响方向。

**SF5** [R2 提出, R1 AGREE] **Abstract 数字密度过高**
至少 6 个定量数字，信息密度影响可读性。
→ 建议：保留 1-2 个关键数字，其余移入正文。

**SF6** [R1 提出, R2 部分 AGREE] **Direction-aware NLI gate 恢复的 21 对未经人工验证**
主 pipeline gate-passed pairs 有 50 对人工验证，放宽标准恢复的 21 对应至少接受同等水平人工检查。R2 补充：影响有限（BT Δ ≈ -1pp），但严谨性需要。

**SF7** [两位共识] **样本外部效度论证不足**
LLMBar (n=100) + AlpacaEval + MT-Bench 三个 benchmark 均偏向 general instruction-following。Cross-benchmark replication 仅 "selected configurations"，未充分讨论。

---

### Minor（不影响接收）

| # | 问题 | 来源 | 交叉 |
|---|------|------|------|
| M1 | Conclusion 最后一行可能溢出到 p.9 | R1 | R2 AGREE |
| M2 | LLM rewriting 未报告 decoding seed | R1 | R2 AGREE |
| M3 | Table 1 caption 自解释性不足 + 信息密度过高 | R1+R2 | 共识 |
| M4 | Figure 4 y 轴标签与 caption 术语不一致 | R1 | R2 AGREE |
| M5 | Table 3 显著性标记格式不一致 | R1 | R2 AGREE |
| M6 | "style bias" vs "style preference" vs "style sensitivity" 术语混用 | R2 | R1 AGREE |
| M7 | Section 3.5 Design Rationale 位置突兀 | R2 | R1 AGREE |
| M8 | Appendix 过多（A-S, 19 个），建议合并同类 | R2 | R1 AGREE |
| M9 | Introduction motivating example 应在例子后立即引入替代解释 | R1+R2 | 共识 |
| M10 | 与 RATE 的差异化论证组织分散，核心差异被稀释 | R2 | R1 REBUT（内容充分但 organization 可改善） |

---

## Reviewer Consensus

两位 Reviewer 在以下问题上达成完全共识 [AGREE]：
1. "Framework" 泛化声明需要降级或限定范围
2. NLI gate 人工验证不足（κ=0.44, n=50 是硬伤）
3. Novelty 重心应从"发现 divergence"转向"GEE decomposition + per-axis confound structures"
4. TOST Δ=15pp 校准不够透明，Claude 应从"negative control"重新 framing
5. Construct divergence 解释发展不足
6. Claude 负控制讨论不充分
7. GEE per-axis decomposition 是论文最有价值的增量贡献
8. 统计分析深度在 NLP 实证论文中罕见，是显著优势

---

## Reviewer Divergence

**唯一分歧：标题 "Blindspot" 是否隐含 attenuation 偏向**

- **R2** [Must-Fix N2]："Blindspot" 在认知科学中含义是"盲区"——预设 attenuation 解释，排斥 amplification 和 construct divergence。建议更中性标题。
- **R1** [部分 REBUT]："Blindspot" 描述可观测现象（Likert 系统性无法检测 pairwise 能检测的效应），类似 "survivorship bias" 命名模式而非机制预设。但 AGREE Introduction 的 motivating example 确实偏向 attenuation，应提前引入替代解释。

**Director 判断**：标题 "Blindspot" 可保留（描述现象的命名约定在学术文献中常见），但 Introduction 应在 motivating example 后**立即**简要引入三种非排他性解释，避免读者在前 6 页形成单向认知。此问题从 Must-Fix 降为 Should-Fix——标题选择属作者判断范围，但 framing 不平衡需修正。

---

## Questions

1. **Attenuation vs construct divergence 的可区分性**：Appendix J 的 bootstrap attenuation 数据（d_median ≈ -0.017 在所有样本量下恒定）是否足以区分"true null effect"（construct divergence）和"merely underpowered"（attenuation）？如果 Likert ATE 是 true null，这对 Blindspot 机制讨论意味什么？

2. **NLI gate 过滤的 pairs 的 style effect 偏向**：被过滤的 ~38% pairs 是否系统性对应更大的 style 效应？如果是，NLI 门控可能系统性低估实际 style bias 幅度。

3. **Claude 负结果的机制性解释**：Claude 不展示 Blindspot 是否可能通过改进 judge prompt（而非更改 measurement mode）来缓解其他 judge 的 Blindspot？这对 practical recommendation 的影响？

4. **GEE 的 causal interpretation**：论文使用 "Controlled" 语言，但 GEE 本身是 associational。能否更精确界定哪些 inference 是 causal（来自实验设计）、哪些是 conditional association（来自统计模型）？

---

## Missing References

| 引用 | 来源 | 理由 |
|------|------|------|
| **Luce (1959)** "Individual Choice Behavior" | R1+R2 独立建议 | BT 模型是 Luce choice axiom 的特例，论文使用 BT 但未引用理论基础 |
| **Williams et al. (2018)** MNLI | R1 建议, R2 AGREE | NLI gate 使用 DeBERTa fine-tuned on MNLI，但未引用 MNLI 原始论文 |
| Kim et al. (2024) "Prometheus 2" | R2 建议 | R1 REBUT（关联度有限）。Director 判断：可选，非必须 |

---

## External Review

外部审稿：未启用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 8 info）：

**Warnings:**
- **Page 6**: 单页堆叠 3 个 display items（Table 1 + Figure 3 + Table 2），极拥挤。Table 1 脚注字号约 6pt，阅读困难。建议将 Table 2 移至后续页面。
- **Page 5**: 全页纯文本含 5 个 section heading，节奏碎片化，缺乏视觉锚点。

**Info highlights:**
- Figure 2 DAG 设计清晰，caption 自包含且适当谦虚
- Figure 4 power curves 建议补充 marker shape 增强打印友好性
- 首页无 display item（Figure 1 在 p.2），可考虑 teaser 提升第一印象
- Appendix 表格排版规范，booktabs 风格一致

---

## Overall Assessment

**Overall Score: 3.5 / 5（Borderline Conference）**

| Reviewer | Overall | Soundness | Excitement | Reproducibility | Confidence |
|----------|---------|-----------|------------|-----------------|------------|
| R1 | 3.5 | 3.5 | 3.5 | 4.0 | 4 |
| R2 | 3.5 | 4.0 | 3.0 | 4.0 | 4 |
| **综合** | **3.5** | **3.75** | **3.25** | **4.0** | **4** |

**判断依据**：

论文在方法论执行上接近会议水平（Soundness 3.75），统计分析的深度和严谨度在 NLP 实证论文中属上乘。GEE per-axis confound decomposition 是 genuine insight，对 NLG evaluation practice 有直接价值。

但三个因素将其拉到 Borderline：
1. **Novelty cap**（Excitement 3.25）：核心发现是已知心理测量结论的 domain transfer，论文未充分论证 LLM judge 领域的独立贡献。如果将 novelty narrative 重构为 GEE decomposition + per-axis confound taxonomy，可能提升 Excitement。
2. **NLI gate 验证不足**：作为 measurement methodology 论文，pipeline 核心组件的人工验证标准偏低（κ=0.44, n=50）。
3. **Framing 不平衡**：三种解释（attenuation/amplification/construct divergence）的权重分配不均，标题和叙事偏向 attenuation。

**升级到 4.0 (Conference) 的路径**：(1) 重构 novelty narrative 突出 GEE decomposition；(2) 增加 NLI gate 人工标注（≥100 对 + 第 3 标注员）；(3) 将 "framework" 降级为 "methodology"；(4) Introduction 提前引入三种解释；(5) 正文讨论 TOST Δ sensitivity。

---

## Detailed Comments

### Section 1 (Introduction)
- Motivating example (GPT-4o formal vs casual) 有效但暗示 Likert 判断是"错误的"。应在例子后立即引入 amplification 和 construct divergence 作为等权重替代解释。[R2 N2, R1 部分 AGREE]
- Contributions 第一条 "black-box framework" 应降级为 "methodology" 或加限定语。[R2 N1, R1 AGREE]
- GEE decomposition 应提升为与 Blindspot 平行的核心贡献，而非被 Blindspot 遮蔽。[R2 N3, R1 AGREE]

### Section 2 (Related Work)
- Measurement Sensitivity 段落引用了 Thurstone (1927) 等经典文献，但未充分论证在 LLM judge 领域量化此现象的独立价值。建议论证 LLM judges 的 RLHF pipeline 引入了人类评估不存在的 mode-specific biases。[R2 N3]
- 与 RATE 的差异化论证分散在两处，建议在 RW 末尾增加集中对比段落。[R2 W2, R1 部分 REBUT]
- 缺少 Luce (1959)（BT 理论基础）和 Williams et al. (2018) MNLI（NLI gate 基础引用）。[R1+R2]

### Section 3 (Method)
- Section 3.5 Design Rationale 位置可优化（移至 3.1-3.2 之间或合并）。[R2 Minor-4, R1 AGREE]
- NLI gate 的 content preservation 验证（Section 5.4）中 κ=0.44 的 disagreement cases 应做定性 error analysis。[R1 N1, R2 AGREE]

### Section 4-5 (Experiments & Analysis)
- Table 1 信息密度极高，建议拆分或增强 caption 自解释性。[R1 M3, R2 Minor-1]
- Section 5.1 "Interpreting the divergence" 应扩展 construct divergence 讨论——如果两种模式测量不同构念，practitioners 应如何选择 format？[R2 W4, R1 AGREE]
- BT unidimensionality 假设应从脚注提升到 Limitations。[R1 W4, R2 AGREE]
- Bootstrap CI 类型应明确报告。[R1 W1, R2 AGREE]

### Section 6 (Conclusion)
- "Likert-only audits may fail to surface..." 应平衡表述为 "the two modes may capture different aspects of style preferences"。[R2 N2]
- 可能有一行溢出到 p.9，需确认并修复。[R1 M1]

### Limitations
- 讨论坦率且全面，是论文优势之一。[R2 S5]
- 建议增加：(1) CSD 对 semantic-level 风格轴的适用性边界；(2) TOST Δ 的 sensitivity analysis discussion；(3) BT unidimensionality 假设的违反条件；(4) Claude 负结果对 mode-intrinsic vs model-specific 的含义。

### Appendix
- 19 个 appendix 内容充实但数量过多。建议合并同类（如 C+H → "Model Diagnostics"，E+F+N → "NLI Gate Analyses"）。[R2 Minor-5, R1 AGREE]
- Appendix P 缺少 rewriting decoding seed。[R1 M2, R2 AGREE]