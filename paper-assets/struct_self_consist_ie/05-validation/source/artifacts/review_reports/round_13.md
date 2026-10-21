---
round: 13
overall_score: borderline
timestamp: 2026-05-16T06:55:11.632731+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 13 审稿报告 — struct_self_consist_ie

**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition
**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)
**Reviewers**: 2 人 (R1: 方法/实验/统计; R2: 新颖性/相关工作/写作)
**轮次**: Round 1 独立审稿 + 交叉回应，1 轮收敛

---

## Summary

论文研究 LLM-based NER 中 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 quality estimation 和 best-of-N selection 两个维度的表现差异。核心发现是 "correlation-selection gap"：signals 达到 moderate QE（Spearman ρ 至 0.45）但无法改善 sample selection。诊断链深入分析了 LP 压缩机制（entity-token ablation、free-form ablation、verbalized confidence）。实验覆盖 3 个 NER + 1 个 RE 数据集、2 个模型族、4B/8B scale。

---

## Strengths

1. **QE/selection 解耦的方法论价值** [共识]：Prior work 仅报告 consistency-accuracy 相关性（Yao et al. 2026），本文首次系统验证 QE 不等价于 selection，并定量化 oracle headroom（13-18pp）与实际 selection gain（≈0pp）的落差。

2. **统计方法论严谨** [共识]：Bootstrap CI with Bonferroni、TOST equivalence testing with 内外锚定（识别并解决了 oracle-headroom circularity）、Fisher combined p、multi-seed Kendall's W。在 NLP empirical papers 中属上乘。

3. **LP 压缩诊断链层次分明** [共识]：全序列 LP → entity-token LP（4× variance 但 -2.0pp selection）→ free-form decoding（std ratio 0.97）→ verbalized confidence（更压缩）→ non-tied subset（+2.9pp, p=0.004）。5 层消融系统排除假说，最终指向 entity-token intrinsic overconfidence。

4. **Free-form ablation RE reversal** [共识]：4-seed 一致���（+1.84±0.12pp），是真正的 empirical finding，揭示 constrained decoding 对 RE LP selection 的抑制效应。

5. **诚实的 negative-result reporting** [共识]：†RE hedging 一致、thinking-token confound 三部分定量排除、Appendix 质量高（FK independence test、LOO-SJ 等价证明、OOD transfer、SJ normalizer robustness）。

---

## Weaknesses

### Must-Fix (2 项，强共识)

**MF1** [R3-W2, 持续 11 轮] Contribution framing 混淆 by-construction 与 empirical finding

4/5 信号 by construction 对同一 instance 赋相同 QE 分数——这不是 surprising empirical finding 而是信号设计的定义性后果。MBR/consensus-proximity 将这些转换为 per-sample rankings 后仍然失败（因 utility 在 across-instances 维度与 F1 相关但 within-instance 不相关）——**这才是核心 empirical finding**，但被 "4/5 signals can't select" 的 trivial framing 掩盖。

- 当前 Abstract line 4-5, Intro Contribution 1, Section 4.3 line 85 均将 definitional + empirical 混为同一"gap"
- R1: "叙事使读者误以为 gap 对 instance-level signals 是显而易见的定义问题"
- R2: "如果 gap 的 4/5 成分是 by-construction, novelty 主要集中在 LP 压缩和 MBR across/within 不对称"

**建议**：Contribution 1 重组为纯 empirical：(a) MBR consensus-proximity produces per-sample rankings but fails because utility correlates across but not within instances; (b) LP—the only natively per-sample signal—is too compressed (median 0.041 nats) with entity-token overconfidence as root cause。将 "instance-level signals assign identical scores" 降为 Section 3.1 的 methodological premise 而非 finding。

**MF2** [R0-C3, 持续 14 轮] Selection gap 的 effective test bed 仅限 SciERC (n=529)

- CoNLL: 论文自认 ceiling-effect control（single-sample F1=0.91, oracle headroom ~4pp）
- WNUT-17: signals collapse（52% zero-F1）
- 标题/Abstract "three NER benchmarks" 和 "Named Entity Recognition" 超出 effective support
- LLaMA SciERC + 4B ablation 增加模型维度信心，但仍限于 scientific domain
- TACRED 已证不可行（D105 结构不兼容）

**建议**：(a) 收窄 claim 措辞——明确 selection gap 在 "medium-difficulty regimes" 验证，CoNLL/WNUT 验证 boundary conditions 而非 gap 本身；或 (b) 增加一个中等难度��用领域数据集（如 OntoNotes subset、Few-NERD）。

---

### Should-Fix (5 项)

**SF1** [R12-N1] ρ=0.45 headline number 来自 ceiling-effect dataset [共识]
- Abstract/Intro 用 "ρ up to 0.45" 但此值来自 CoNLL EM（ceiling dataset）
- Primary test bed SciERC 最佳仅 VC ρ=0.379
- **建议**：headline 改用 primary dataset 数值，或标注来源

**SF2** [R12-W1] 纯诊断无有效 remedy [部分共识]
- Entity-token LP 失败（-2.0pp）、verbalized conf 失败（-2.45pp）
- LP×VC combination / calibration-based rescoring 未测试
- R1: 诊断性论文不必须含 remedy (ARR H13)；R2: 限制 excitement
- **建议**：至少尝试一个 lightweight pilot（即使 negative 也有信息量）

**SF3** [R13-W1] RE 覆盖策略不统一 [共识]
- RE 出现在 Abstract、所有主表、Discussion，但仅 SciERC 单 benchmark + 40% zero-F1
- †RE 标记 >15 处，hedging noise 大
- Free-form RE reversal 是最有趣发现但被埋 appendix
- **建议**：全移 Appendix（作为 exploratory extension）或增加第二个 RE benchmark

**SF4** [R11-W7/R13] 缺少 greedy (argmax) decoding baseline [共识]
- "Single" = T=1.0 draw ≠ greedy decoding
- Greedy 是部署中最自然的 no-cost baseline
- 无论结果��何都对叙事有价值（如 greedy > all signals → gap 更 striking）

**SF5** [R11-W1] 与 Yao et al. (2026) 的增量贡献 framing [部分共识]
- SJ vs EM 改进仅 Δρ=+0.065（borderline, "would not survive Bonferroni"）
- Difficulty gradient 是自然的 multi-dataset 延伸
- R1 辩护：LP diagnostic chain 和 QE-selection separation 是 non-trivial
- **建议**：重心转向 MBR failure mechanism + LP diagnostics，structural matching 降为 methodological choice

---

### Minor (6 项)

| ID | Issue | 共识 |
|----|-------|------|
| R11-W3 | 3 seeds Kendall W=1.000 统计信息量不足，正文应弱化 ranking stability claim | 共识 |
| R13-W2 | Abstract 过度压缩（9句覆盖全部机制+数字），建议精简 | 共识 |
| R12-M1 | Discussion LP hypotheses "three mechanisms" → 实际 (a)(b)(c)(d) 四个 | 共识 |
| R13-M1 | Bib issues: mejer2011→2010, feng2025 author mismatch, 4 条 OpenAlex unmatched | R2 |
| R13-M2 | Table 2 "Fisher p" vs Appendix "Fisher combined p" 术语不一致 | R2 |
| R12-M2 | Soft Jaccard 命名（max 分母）：transparent footnote + robustness table，非实质问题 | 降级为 preference |

---

## Reviewer Consensus

**[AGREE]** 两位在以下关键问题上完全一致：
- MF1: by-construction/empirical framing 混淆（最核心问题，持续 11 轮）
- MF2: effective test bed 仅 SciERC
- SF1: ρ=0.45 headline 来源
- SF4: 缺少 greedy baseline
- 统计方法论是论文优势
- LP diagnostic chain 是核心贡献

## Reviewer Divergence

**[程度分歧]**（方向一致，仅严重性不同）：
- **Overall score**: R1 3.5/5 (Borderline Conference) vs R2 3/5 (Findings)。分歧源于 LP diagnostic chain 的独立贡献权重——R1 认为 5 层消融超越 incremental，R2 认为缺乏 remedy 限制 excitement。
- **SF2 (remedy)**: R1 认为诊断论文不必���含 remedy；R2 认为影响 acceptance level。
- **SF5 (Yao incremental)**: R1 部分辩护 LP chain；R2 认为整体偏 incremental。

**[已解决分歧]**：
- R1-W2 (N≤16 scaling): R2 rebut 合理——论文 claim 是 diminishing returns �� asymptotic。不纳入 final recommendations。
- R1-W5 (SJ naming): R2 rebut 合理——footnote + robustness table 已 transparent。降为 preference。
- Q4 (RE reversal significance): R2 提供 4-seed evidence (σ=0.12pp)，reversal robust。已解决。

---

## Questions (需作者澄清)

1. MBR within-instance utility-F1 correlation 具体多少？（如 SJ-utility 的 within-instance ρ）——这是支撑 MF1 reframe 的关键数据空白。
2. LP×VC combination 或 LP z-score normalization 是否有任何初步数据？
3. Non-tied LP subset (+2.9pp) 部署时无 ground-truth 选 ε，是否有 oracle-free proxy 可预测哪些 instances LP 有 discriminative power？
4. Entity-token LP variance CoNLL (median 2×10⁻¹⁰) vs SciERC (4×) 的巨大差异是否与 entity type diversity (4 vs 6 types) 和 model certainty level 有关？
5. 4B QE 优于 8B 是否因 output diversity 更大？缺 Table 8 对应的 4B diversity 数据。

---

## Missing References

R2 引用���整性检查：50 entries, 0 orphan, 0 missing bib。所有关键引用已覆盖。

Minor bib issues（R13-M1）需核实但不影响引用完整性。

---

## External Review (Stanford Agentic Reviewer)

状态：not_requested。项目未配置外部审稿。

---

## Overall Assessment

**Score: Borderline (weak accept for Findings track, not strong enough for Main Conference)**

**置信度**: 4/5

**理由**：
- 研究问题有价值（QE ≠ selection 的系统验证），LP 压缩诊断链深入且多层
- 统计方法论在同类论文中属上乘
- 但：(1) 核心 framing 将 definitional 与 empirical 混淆已持续 11 轮未根本解决；(2) effective test bed 仅 SciERC 一个中等难度数据集；(3) 纯诊断无 remedy 限制 impact
- 修正 MF1+MF2 后定位为 Findings paper 合理；Main Conference 需要额外贡献（remedy pilot 或第二个 medium-difficulty dataset）

**R1**: 3.5/5 — Borderline Conference，认为 LP diagnostic chain 足够支撑
**R2**: 3/5 — Findings level，认为缺乏 remedy + incremental over Yao

---

## Detailed Comments

### Section-by-Section

**Abstract**: 信息过度压缩（SF3），ρ=0.45 headline 来自 ceiling dataset（SF1），MBR mechanical 细节不适合 abstract level。

**Introduction**: Contribution 1 需重组（MF1）。与 Yao et al. 的差异描述可接受但应更精确（SF5）。

**Method (§3)**: 信号定义严谨，instance-level vs per-sample 区分清晰。SJ footnote 透明。Evaluation framework 合理（gold-empty exclusion justified）。

**Experiments (§4)**: Table 1 QE 结果 solid。Table 2 selection 结果��核心 evidence 但需 greedy baseline（SF4）。Scale ablation 限定合理（"within 3B-8B"）。

**Discussion (§5)**: LP hypotheses 编号错误（minor）。Entity-token ablation 是强贡献���Free-form RE reversal 值得更 prominent treatment。"Likely requires learned per-sample scoring" 结论合理。

**Limitations**: 全面覆盖 13 项，诚实透明。

**Appendix**: 质量高，FK independence/OOD/TOST external anchors/N-scaling 均有独立价值。