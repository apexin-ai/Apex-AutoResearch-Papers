---
round: 26
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T04:53:32.282930+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 27 (Fresh Review)

**论文**: The Capability Ceiling of Self-Consistency: Why Entity-Level Self-Verification Fails in Structured Generation
**Venue**: EMNLP 2026 Main Conference (Long Paper), ARR May cycle
**Deadline**: 2026-05-25
**审稿模式**: Fresh（无历史轮次记忆）
**Reviewer**: R1（方法严谨性）+ R2（新颖性/完整性）
**轮次**: Round 1 初审 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文系统研究了 self-consistency (SC) 在结构化信息抽取（主要是 NER）中的能力天花板。通过四阶段诊断框架（QE → degeneracy → agreement fidelity → LP compression），论文揭示了一个 "correlation-selection gap"：虽然 entity-level agreement signals（如 SJ, VC）与质量存在正相关，但无法有效转化为 sample selection 增益。核心原因是 instance degeneracy——在 fine-tuned 模型上 82.9%（SciERC）的输出完全一致，selection 无从下手。论文测试了七种 entity-level self-verification 方法均告失败，并提出 entity-level construction 和 cross-model ensemble 作为 escape routes。理论贡献包括将 NER SC 形式化为 entity-level MBR decoding 和 degeneracy decomposition 上界。

---

## Strengths

**S1. 实验规模和统计严谨性出色。** 4 个 NER 数据集（SciERC, Few-NERD, CoNLL, WNUT-17）、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）、N∈{2,...,32}、3 seeds（部分）。统计检验完备：Holm-Bonferroni 多重校正、paired bootstrap CI、permutation tests、TOST 等价性检验。42 页附录覆盖几乎所有合理 ablation。[共识]

**S2. Diagnostic cascade 框架有独立工具价值。** 四阶段分解将模糊问题（"为什么 SC 不 work"）转化为可操作的诊断步骤。Figure 1 概括力强。对 instance degeneracy 的量化（82.9% identical outputs, Table 2）提供了有力的失效解释。[共识]

**S3. 七种 entity-level self-verification 方法的系统性 negative result。** ESJ, MRSC, LSC, hidden-state probe, ASB, SCD, supervised classifier 逐一测试均 fail，形成令人信服的 negative result。Hidden-state probe AUROC 0.63-0.88 但无法转化为 selection gain——说明质量信号存在但无法 operationalize。[共识]

**S4. MBR 理论联系。** Proposition 1（majority-vote 是 balanced set-overlap utility 下的 MBR optimal）和 Degeneracy Decomposition（E[ΔF1] ≤ (1-D)·G_nd）提供理论基础。[共识]

**S5. 诚实报告负面结果 + prescriptive protocol。** Entity construction (+1.09pp Few-NERD), LP-weighted construction, cross-model ensemble 具实用价值。[共识]

---

## Weaknesses

### Must-Fix（影响接收决定，共 4 个）

**MF1. [critical] Cascade 因果声称与相关性证据不匹配** [R1-N3 + R2-N2, 强共识]
- §3 "Why Self-Verification Fails"、§4 "Why Single-Signal Selection Fails" 的 "Why" 标题和 Figure 1 箭头暗示因果链
- 实际证据全部是描述性/相关性：Spearman ρ、subgroup 对比、AUROC
- §7.3 自承 "degeneracy alone does not predict LP direction"，与 §4 因果叙事存在内部矛盾
- **建议**: "Why" → "Where and How"；全文软化因果语言为 association/correlation；加显式声明 cascade 是 descriptive diagnostic 而非 causal model

**MF2. [critical] Related Work 严重不足** [R2-N1 + R2-W2, R1 交叉完全同意]
- §8 仅 ~0.5 页
- 5 篇高度相关论文在 .bib 中但未在正文引用：Chen et al. (2024) "Two Failures of SC" (TMLR)、Chen et al. (2024) "Universal SC" (ICML WS)、Aggarwal et al. (2023) "Adaptive-Consistency" (EMNLP)、Thirukovalluru et al. (2024) "Atomic SC" (EMNLP)、Farquhar et al. (2024) "Semantic Entropy" (Nature)
- 缺乏对 conformal prediction、SC code generation failure、entity-level hallucination detection 方向的覆盖
- Chen "Two Failures" 从 reasoning 角度分析 SC failure modes，不讨论会让审稿人质疑 novelty claim
- **建议**: §8 扩充至 0.75-1 页；补引上述论文并讨论差异化贡献

**MF3. [critical] θ_crit=0.70 半经验推导但呈现为理论结果** [R1-N1, R2 交叉完全同意]
- §6.3 / Appendix p.3 / Figure 9: θ_crit 公式嵌入 SciERC 经验参数（G_gap=14.8pp, ε=0.068）
- CoNLL（D=61.7% < 0.70）上 LP 选择也失效，说明该阈值非普适
- Figure 9 标题未标注 data-specific
- **建议**: 明确标注为 data-dependent 经验近似；增加 CoNLL/Few-NERD 的 dataset-specific θ_crit 敏感性分析

**MF4. [critical] 种子数不对称影响统计效力均衡性** [R1-N2, R2 交叉同意但略降严重度]
- SciERC 3 seeds vs. Few-NERD/CoNLL 1 seed
- Few-NERD（最强正面信号 +1.39pp）无法验证跨 seed 稳定性
- 核心负面结论在 3/4 数据集上依赖单次运行
- 缓解因素：Table 11 (3-seed mean)、Table 20 (multi-seed stability)、bootstrap CI 部分覆盖
- **建议**: 至少为 Few-NERD 补做 3-seed 实验

### Should-Fix（影响评分但不一票否决，共 6 个）

**SF1. [warning] 标题 "Structured Generation" 范围过宽** [R1-W2 + R2-W3, 强共识]
- 实验仅覆盖 NER（4 datasets）+ 1 个 exploratory RE（单数据集单模型）
- "Structured Generation" 在 NLP 社区涵盖 code/SQL/JSON 等
- **建议**: 标题缩窄为 "Named Entity Recognition" 或 "Structured Information Extraction"

**SF2. [warning] Escape routes 效果量边际 + cost-benefit 缺失** [R1-W1 + R2-W4, 共识但有 nuance]
- 最大增益 +1.39pp（Few-NERD LP selection），entity construction +1.09pp
- 8x 推理开销换 ~1pp F1，实用价值存疑
- R2 partial rebut: 对 negative result 论文，边际 escape routes 恰好强化负面结论
- R1 rebut R2: entity construction 是 post-hoc aggregation，边际成本为零（已有 N 个样本时）
- **建议**: §9 增加 cost-benefit 分析框架

**SF3. [warning] 与 Yun et al. (2025) "Diversity Collapse" 差异化不够** [R2-W1, R1 交叉同意]
- Yun et al. 已证明 constrained decoding 导致 diversity collapse，与本文 degeneracy 发现高度相关
- §8 仅一句引用
- **建议**: 明确区分——Yun 关注 diversity 本身，本文关注 diversity collapse 对 downstream selection 的功能性影响

**SF4. [warning] 缺少 structured MBR baseline 实验对比** [R1-W4, R2 交叉同意]
- §6.1 引用 Eikema et al. (2025) 但未实验对比
- 至少应实现 standard MBR with token-level F1 utility，或对比不同 utility function
- 验证 Proposition 1 实际有效性的必要步骤

**SF5. [warning] 36 orphan bib entries** [R1 + R2 均发现]
- 81 bib entries 中仅 45 被引用
- 应清理未使用条目

**SF6. [warning] Seed 不对称的统计影响** [与 MF4 关联但 severity 不同]
- SciERC 是 primary test bed 但样本量小（n=529），MDE ≈ 1.5pp
- Few-NERD 作为 "definitive test" 但仅 1 seed
- Bootstrap CI (B=10000) 部分缓解但不替代 cross-seed validation

### Minor（不影响接收，共 6 个）

**M1.** per-sample signal 定义完全 defer 到 Appendix（§2.1 首次使用时应给简要定义）
**M2.** Figure 2 bar chart 灰度打印时颜色难区分（建议 hatching patterns）
**M3.** Table 1 "One score per input" 列缺乏正文解释
**M4.** §6.2 inverse scaling 机制（SciERC converges more slowly）仅一句带过
**M5.** Limitations 未讨论 closed-source API 模型的 degeneracy profile 差异
**M6.** 36 orphan bib entries 应清理

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全一致（交叉后无分歧）：

1. **因果声称过强**（R1-N3 = R2-N2）— 最核心问题，§3/§4 的 "Why" 标题和 Figure 1 箭头必须修改
2. **Related Work 严重不足**（R2-N1）— 5 篇直接相关论文在 bib 中未引用，§8 需大幅扩充
3. **θ_crit 呈现方式误导**（R1-N1）— 必须标注为 data-dependent 经验近似
4. **Scope overclaim**（R1-W2 = R2-W3）— 标题和 scope 需缩窄至 NER
5. **Orphan bib entries**（R1 + R2）— 36 条未引用条目需清理
6. **MBR baseline 缺失**（R1-W4）— Proposition 1 应有实验验证

## Reviewer Divergence [REBUT]

以下问题存在温和分歧（不影响整体判断）：

1. **LODO transfer 分析充分性**（R1-W3 vs R2 REBUT）— R1 认为不充分，R2 认为论文 claim 是 "transfer fails" 而非 "we can do transfer"，要求额外分析超出 claim 支撑范围（ARR H13）。**Director 判断**: R2 论证有理，transfer 分析充分度维持为 minor concern。

2. **Cost-benefit 论证**（R2-W4 vs R1 partial REBUT）— R2 要求讨论 8x 推理开销的 cost-benefit，R1 指出 entity construction 是 post-hoc aggregation（边际成本为零）。**Director 判断**: 两者都有道理，建议添加简短 cost-benefit 讨论但不阻塞。

3. **Table 1 列标签**（R2-M3 vs R1 REBUT）— R1 认为 §2.2 已定义，属常规做法。**Director 判断**: minor，不要求修改。

4. **AUROC→selection gap 瓶颈**（R2-Q3 vs R1 REBUT）— R2 问是否 bottleneck 在 aggregation，R1 认为论文已解释为 degeneracy 限制可优化空间。**Director 判断**: 建议增加一句显式说明。

---

## Questions for Authors

**Q1.** [R2] T>1.2 是否能 recover diversity 改善 selection？Appendix 温度分析仅到 T=1.2。
**Q2.** [R2] 本文 failure mode 与 Chen et al. (2024) "Two Failures" 识别的 hypothetical/compositional consistency failure 的关系？
**Q3.** [R2] Hidden-state probe AUROC 0.63-0.88 但 selection gain 有限——bottleneck 在 quality estimation 还是 aggregation？
**Q4.** [R2] 是否考虑过 entity-level filtering（high-consistency select, low-consistency abstain）作为中间方案？

---

## Missing References

**优先补引（在 .bib 中但未引用）**:
1. Chen et al. (2024) "Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs" (TMLR)
2. Chen et al. (2024) "Universal Self-Consistency for Large Language Model Generation" (ICML Workshop)
3. Aggarwal et al. (2023) "Let's Sample Step by Step: Adaptive-Consistency" (EMNLP)
4. Thirukovalluru et al. (2024) "Atomic Self-Consistency for Better Long Form Generations" (EMNLP)
5. Farquhar et al. (2024) "Detecting Hallucinations in LLMs Using Semantic Entropy" (Nature)
6. Kuleshov & Liang (2015) "Calibrated Structured Prediction" (NeurIPS) — 在 bib 中未引用

**建议补引（可能不在 .bib 中）**:
7. PASC (2025) "Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP Pipelines"
8. "Existing LLMs Are Not Self-Consistent For Simple Tasks" (2025)

---

## External Review (Stanford Agentic Reviewer)

**状态**: pending（已于 2026-05-21T04:34 发送请求，尚未返回）

---

## Visual Layout Check（非评分项）

**状态**: agent 超时（300s timeout），无实际 findings。
用户可选择重新触发视觉审查。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3 | 3 | 3 |
| Reproducibility | 4 | 4 | 4 |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4 | 4 | 4 |

**评价**: 实验质量出色，diagnostic cascade 有工具价值，负面结果对 practitioner 有直接 actionable 意义。但四个 Must-Fix 问题（因果声称、Related Work 缺口、θ_crit 呈现、seed 不对称）限制了当前版本的接收可能性。核心 insight（degeneracy 导致 SC 失效）novelty 有限——与 Yun et al. (2025) diversity collapse 发现存在重叠，增量贡献主要在于量化 diversity collapse 对 selection 的功能性影响。

**修改后预期**: 如果 4 个 Must-Fix 全部解决（因果语言软化、§8 扩充、θ_crit 标注、seed 补充），论文可达 **3.0-3.5**（Findings 至 Borderline Conference）。是否能冲击 Main Conference 取决于 novelty argument 的改善——需要更清晰地回答 "beyond Yun et al., what is new?"。

---

## Detailed Comments

### §1 Introduction
- "Why" framing 需全面软化为描述性语言
- Scope claim 需限定为 NER 而非 structured generation

### §2 Diagnostic Framework
- per-sample signal 定义不应完全 defer 到 Appendix

### §3 Why Self-Verification Fails → 建议改为 "Where/How"
- Hidden-state probe AUROC 0.63-0.88 vs selection gain gap 可增加一句解释

### §4 Why Single-Signal Selection Fails → 建议改为 "Where/How"
- "degeneracy alone does not predict LP direction" (§7.3) 与本节因果叙事的张力需要显式 reconcile

### §5 Adaptive Methods / Escape Routes
- Cost-benefit 分析缺失
- Cross-model SC 仅 1 数据集 1 对模型，需扩展或缩减

### §6 Theory
- §6.3 θ_crit 必须标注为 data-dependent；增加敏感性分析
- Degeneracy decomposition 定位为 diagnostic tool 而非 tight bound

### §7 Experiments
- Seed 不对称需要解释和缓解（至少 Few-NERD 3-seed）
- Holm-Bonferroni k 的 family 定义需透明化

### §8 Related Work
- 从 ~0.5 页扩充至 0.75-1 页
- 必须覆盖：SC failure modes、fine-grained SC 变体、sample-based 不确定性、conformal prediction、Yun et al. 差异化

### §9 Discussion
- 增加 cost-benefit 分析
- 增加 closed-source API 模型的 degeneracy 讨论

### Limitations
- 增加 closed-source API degeneracy profile 差异的讨论

### References
- 清理 36 orphan bib entries
- 引用并讨论 5 篇在 bib 中但未引用的高度相关论文