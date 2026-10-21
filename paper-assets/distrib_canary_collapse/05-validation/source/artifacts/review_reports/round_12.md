---
round: 12
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-24T14:19:49.324543+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 12 审稿报告：Characterizing the Detectability Landscape of Iterative Model Collapse

**Target Venue**: EMNLP 2026 (Long Paper, via ARR)
**Review Mode**: Fresh (Round 12)
**Reviewers**: R1 (方法严谨性 + 统计有效性), R2 (新颖性 + Framing + 完整性)

---

## Summary

本文在 Pythia-410M 上系统构建了 iterative model collapse 的检测相图（13 个 contamination levels × 多个 observation windows），使用 Permutation Granger Causality (PermG) 识别出 sharp detection onset、power-law detection boundary 和 non-monotonic dip 等结构。在 α=1.0 下对 5 个模型族进行了跨架构探索。核心发现包括：(1) 方法敏感性——同一数据上 5 种检测方法产生 FPR 3%–92%；(2) entropy Granger-precedes diversity collapse by ≥1 generation (14/15 experiments)；(3) canary-triggered intervention proof-of-concept。

---

## Strengths

1. **Method-sensitivity finding 是真正有价值的贡献** [双方共识]：同一数据集上 5 种方法产生 FPR 3%–92%，将方法选择敏感性提升为 primary finding 而非 robustness check，对 model collapse 文献是重要警示。

2. **系统性相图框架** [双方共识]：将 detectability 刻画为 (α, T) 空间中的结构化地形，这一概念工具在 model collapse 文献中具有原创性和可复用性。

3. **统计方法论严谨度罕见** [双方共识]：BH-FDR correction、null-control calibration、specification curve analysis (1,160 configurations)、Shapley value method decomposition——在 model collapse 文献中少见的 robustness 水平。

4. **诚实的 Limitations section** [双方共识]：坦率承认 FPR 膨胀、power 限制、β 不可识别、sync-dip 未解释、单架构局限性。

5. **Reproducibility 较好**：超参详尽（Appendix A），5000 permutations、BH-FDR q=0.05 明确，seed 信息完整。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1 [critical, 双方共识]: PermG FPR 11.1% (CI [1.2%, 30.4%]) 使检测边界区域的定量可靠性不足**

PermG 实际 FPR = 4/36 = 11.1%，超出 BH-FDR 名义 5%，cluster-adjusted CI 上界达名义水平的 6 倍。检测 onset (α≈0.50) 恰好位于 FPR 膨胀最危险的地带——Table 7 (Appendix D) 显示 α=0.45 处 min p_fdr = 0.059–0.091，仅略高于阈值。Null control 仅 6 seeds (36 tests)，样本量不足以可靠估计 FPR。GPT-2-medium 的 standalone FPR 高达 50% (Appendix Z)，但仅在 Limitations/Appendix 中提及。

**缓解因素** (R2 提出)：Fisher exact test (0/64 vs 18/32, p=3.45×10⁻¹¹) + cross-seed 3/3 一致性证明 onset 的**存在性** robust；MMCT consensus (K≥3) 在 null 下 0% FPR。但 onset 的**精确位置** (α_c = 0.483 ± 0.006) 在当前 FPR 不确定性下需要更宽的 error bars。

**Required action**: (a) 增加 null seeds 至 ≥12 或报告 Bonferroni-conservative 边界；(b) GPT-2 50% FPR 必须在正文 §5.5 显著标注；(c) 在 FPR CI 上界条件下报告保守版 α_c。

---

**MF-2 [critical, 双方共识]: 标题/Abstract 的 scope 承诺超过实际交付**

"Characterizing the Detectability Landscape" + "five families (345M–6.9B)" 暗示跨架构全面刻画，但：
- 完整 α×T phase diagram 仅在 Pythia-410M 上构建
- Cross-architecture (Table 1) 仅测试 α=1.0（最极端情形）
- GPT-2-medium standalone FPR=50% 使该架构上的 "检测" 本质上不可靠
- 4 个 non-confirming cases 的 post-hoc "failure mode" 归因 vs 更简约的 "PermG FPR 差异" 解释未被讨论

**Required action**: (a) 标题修改以反映实际 scope（主要是 Pythia-410M 的发现）；(b) Abstract 将 cross-arch 重新措辞为 "exploratory probes at α=1.0"；(c) §5.5 添加 alternative explanation paragraph。

---

**MF-3 [critical, 双方共识]: Power-law boundary 参数不可识别，但被高精度呈现**

β 的 MLE = 0.66 vs CV = 0.24，profile CI [0.24, 0.78]——指数 γ 从 0.64 到 2.08 任意取值。Abstract 中 "LOO-CV: MAE=0.037, 15/15 within CI" 在 3-5 个 T 值上无鉴别力（任何光滑单调函数都能达到类似 MAE）。Sync-dip excluded（5 cells）是 post-hoc 操作；included 后 MAE = 0.203 (5.5×)，暴露模型 systematic failure。

**Required action**: (a) Abstract 删除 MAE=0.037 和 "15/15 within CI"；(b) 将 boundary 定位为 qualitative trend (α_c 随 T 递减) 而非精确幂律；(c) 正文报告 γ 的完整 CI；(d) 并列呈现 sync-dip included/excluded 两组拟合。

---

**MF-4 [critical, R2 主导，R1 同意超限]: 页数超出 EMNLP 2026 8 页限制**

Table 1 和 Figure 6（§5.5/5.6 引用的正文元素）被 LaTeX 浮动到 page 9。估计主文约 8.5–8.6 页，超限约 0.5 页。EMNLP 2026 strict 8-page limit 不含 Limitations。

**Required action**: 压缩正文（如将 Table 1 移至 Appendix，或合并 §5.5/5.6 到更紧凑的 subsection）以严格遵守 8 页。

---

### Should-Fix（影响评分但不一票否决）

**SF-1 [双方共识]: Intervention proof-of-concept 仅单一极端条件 (α=1.0, N=2, post-hoc threshold)**

仍被列入 Contribution 1。Appendix H CUSUM comparison 显示 simple threshold 同效，削弱 Granger 框架的 practical advantage。建议从 Contribution 1 剥离为独立的 illustrative example。

**SF-2 [R2 提出, R1 部分同意]: Design Principle 'formal design rationale' 作为独立贡献 oversells**

R2 判 critical（near-trivial：连续量先于阈值量是信息论直觉）；R1 rebut（mode amplification 下的特定机制非公理，≥2 gen lag 非先验可知）。**Director 裁定 should-fix**：内容非 trivial，但 "formal design rationale" 的贡献措辞需降级为 "empirically validated ordering principle"。

**SF-3 [双方共识]: Sync-dip (α=0.60) 作为 "四大 regime 之一" 但机制完全未解释**

Limitations 承认 "the sync-dip mechanism at α=0.60 remains open"。建议降级为 "three confirmed regimes + one unexplained anomaly"。

**SF-4 [R2 提出, R1 同意]: 写作信息密度过高**

几乎每句含多个精确数字，关键 findings 淹没在数字洪流中。四 regime 术语引入顺序不统一。建议精确数字移到 tables/figures，正文保留定性描述。

---

### Minor Issues

- Eq.1 sigmoid 上界 0.70 选择理由未说明
- α 采样间隔不均匀 (0.10→0.25 跳跃) 理由未解释
- Table 1 footnotes 信息过密，建议以 Appendix table 替代
- Schaeffer et al. "8 种 collapse 定义" 中本文使用哪种未明确
- Appendix K 对比表中 SIGMA 的 multi-architecture 标注可能不准确
- Design Principle 与 Theorem 共享计数器，编号序列可能令读者混淆
- bf16 vs fp32 的 sensitivity 在 abstract/contributions 中未反映
- CUSUM 负面结果值得主文简要提及

---

## Reviewer Consensus

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| PermG FPR 使 boundary 不可靠 | N1 critical | W3→升级 critical | **[AGREE] critical** |
| 标题/cross-arch scope 过度 | N2 critical | N2 critical | **[AGREE] critical** |
| Power-law 参数不可识别 | W1→升级 critical | N1 critical | **[AGREE] critical** |
| 页数超限 | 同意 | W4 should-fix | **[AGREE] should-fix** |
| Intervention 过薄 | W3 should-fix | W2 should-fix | **[AGREE] should-fix** |
| Sync-dip 无解释 | W2 should-fix | W1 should-fix | **[AGREE] should-fix** |
| 信息密度过高 | 同意 | W5 should-fix | **[AGREE] should-fix** |

---

## Reviewer Divergence

| 问题 | R1 | R2 | Director 裁定 |
|------|----|----|--------------|
| Design Principle trivial? | should-fix (内容非 trivial，framing oversells) | N3 critical (近乎公理) | **should-fix** — R1 的 rebuttal 有理：mode amplification 下的特定机制和 ≥2 gen lag 非先验可知；但贡献措辞确实 oversells |
| MMCT 等权投票 | W4 should-fix (缺 Type I 分析) | REBUT (有 empirical mitigation) | **minor** — Appendix M 的 4 种 weighting schemes 一致性 + null MMCT FPR=0% 提供了充分 empirical evidence |
| Grid 多重比较 | W5 should-fix | REBUT (sigmoid fit 是 single test) | **minor** — onset claim 有 aggregate-level support (sigmoid + Fisher)，但 "four regimes" 命名应更谨慎 |

---

## Questions for Authors

1. 如果 FPR 恰好在 5% 名义水平，α_c(T) 会如何移动？能否提供 FPR=5% vs 11.1% 下的敏感性分析？
2. GPT-2-medium 的 50% FPR 是 PermG 在高 null-drift 架构上的根本局限，还是可通过架构特定校准解决？
3. Sync-dip 是否在所有 seed 中一致出现？有无证据排除 seed-specific artifact？
4. 如果仅保留 MMCT-conditioned claims (K≥3, 0% FPR)，abstract 和 contributions 的核心 findings 是否仍然成立？
5. 为什么不使用 two-sample distributional tests (MMD, KS) 作为替代或补充 detection 方案？

---

## Missing References

- **Adams & MacKay (2007)**: Bayesian online changepoint detection — Related Work 未覆盖 online change-point detection 经典文献
- **Papana et al. (2013) / Siggiridou & Kugiumtzis (2016)**: 置换 Granger 因果性验证方面的工作
- **Two-sample distributional testing literature** (MMD, Wasserstein): 作为替代 detection 方案未被系统讨论

---

## External Review

**Status**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**Status**: ✅ 完成

Findings:
- **[warning]** Pages 6-7-8 布局节奏失衡：pages 6-7 连续纯文本无 display item，page 8 塞入 Figures 3/4/5 导致每图面积偏小。建议将 Figure 3 或 4 前移均衡视觉节奏。
- **[info]** Figures 3-5 axis labels、legend 字号约正文 65-70%，接近可读下限，建议 ≥70%。
- **[info]** 前 2 页无视觉锚点，第一个 display item 在 page 3。ACL 格式下可接受。
- **[info]** Figure 1 热力图分数标注字号偏小，PDF 屏幕阅读需放大。
- **[info]** Appendix 末页填充约 55-60%（非严重问题）。

---

## Overall Assessment

**Score: 3.0 — Findings**

**Confidence: 4/5**

**Rationale**:

论文的 method-sensitivity finding（FPR 3%–92%）和 phase-diagram 框架具有真正的原创性和实用价值，统计方法论严谨度在 model collapse 文献中罕见。然而三个 critical 问题共同将论文拉至 Findings 水平：

1. **FPR 膨胀 + null sample 不足** → 核心定量 claims (detection boundary) 的可靠性存疑
2. **Scope overclaiming** → 标题和 abstract 承诺的泛化程度远超单架构 + α=1.0 探索的实际交付
3. **Power-law boundary 参数不可识别** → Contribution 1 的定量核心本质上未确定

这些问题不是 writing 问题——它们动摇了论文核心贡献的证据基础。如果作者能：(a) 增加 null control seeds 并报告保守版边界；(b) 校准标题/abstract 的 scope 与实际交付匹配；(c) 将 boundary 降级为定性趋势——论文有潜力从 Findings 上升至 Borderline Conference (3.5)。当前版本适合 Findings track。

---

## Detailed Comments

### §1 Introduction
- Contribution 1 将 power-law boundary、canary mechanism 和 intervention 打包在一起，每项的 evidence level 差异很大（boundary: weak, canary: moderate, intervention: minimal）。建议拆分为独立 contributions 并明确各自的 evidence strength。
- "five families (345M–6.9B)" 在第一页给读者设定了跨架构全面验证的期望，但实际仅 α=1.0 单点探索。

### §3 Cascade Ordering
- Design Principles 1-2 提供了有用的 motivation，但 "formal design rationale" 措辞暗示比实际提供的更深的形式化。建议改为 "empirically motivated design principles"。

### §4 Method
- PermG FPR 11.1% 的讨论足够诚实，但 MMCT consensus 作为 primary safeguard 的 role 应在 §4.1 开头而非末尾强调——让读者先知道 standalone PermG 的局限和论文的应对策略。
- §4.2 的 boundary model 在参数不可识别的前提下，作为 contribution 的价值在于定性框架而非定量预测。

### §5 Experiments
- §5.2 的 sharp onset 是论文最引人注目的发现。Fisher exact test + cross-seed 一致性提供了 onset 存在性的强证据。但 α_c = 0.483 ± 0.006 的精度声明与 §5.1 自承认的 β 不可识别性矛盾。
- §5.5 Cross-architecture: GPT-2-medium 的 50% standalone FPR 应在本节正文中以 caveat paragraph 呈现，而非仅在 Appendix Z 和 Limitations 中。读者可能只看 Table 1 的 "6/8"，不会注意到该结果在 50% FPR 背景下本质不可解读。
- §5.6 Intervention: 从 page budget 角度，0.5 页用于 N=2 single-condition proof-of-concept 的 ROI 很低。该空间可更好地用于 §5.5 的 FPR caveat 或 §5.3 的 dip mechanism 讨论。

### §6 Discussion
- 篇幅合理但略显保守。鉴于 scope 需要收紧，Discussion 是添加 "what this study does NOT claim" 的自然位置。

### Limitations
- 全面且诚实。建议增加一句关于 intervention 的 limitation（仅在最有利条件下测试，practical applicability unknown）。

### Format
- **页数**: 需严格压缩至 8 页正文。
- **Float placement**: Pages 6-7 纯文本 + page 8 图片堆积 = 不均衡，调整 float 命令。