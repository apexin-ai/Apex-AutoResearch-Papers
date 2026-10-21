---
round: 11
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-23T13:43:24.082779+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 17（Fresh Review）

**论文**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts
**Venue**: EMNLP 2026 Main (via ARR)
**审稿日期**: 2026-05-23
**Reviewer 编排**: 2 人圆桌（R1: 方法严谨性 / R2: 新颖性/完整性）
**轮次**: 1 轮初审 + 交叉分享，关键问题达成共识

---

## Summary

论文研究 LLM 标注作为因果推断效应修饰变量时的测量误差问题。核心发现是：当 LLM 误分类率在子群间异质时，对子群 CATE 应用全局（pooled）混淆矩阵校正会引入系统性偏差——低误差子群被过度校正，高误差子群校正不足。Theorem 1 给出偏差的精确恒等式分解：bias ∝ δ_s · Δτ / (1−2π̄)。论文提出 EC-HTE（层级贝叶斯分层混淆矩阵校正 + CausalForest 集成），并给出一个不依赖处理效应估计的诊断准则（Proposition 3）。实验覆盖合成、半合成（TweetEval）、真实 LLM 混淆矩阵验证、以及大量 robustness checks（29 个 Appendix）。

---

## Strengths

**S1 [consensus]**: Theorem 1 的偏差分解恒等式形式优美且精确——非渐近近似而是 exact identity。将偏差分解为 δ_s（子群误差偏差）× Δτ（CATE 异质性）× 1/(1−2π̄)（放大因子）的乘积结构既有理论洞察力又可操作。R² ≥ 0.97 跨 11 个真实 LLM-数据集组合验证。

**S2 [consensus]**: Proposition 3 的 Δτ-free 诊断准则有独立实用价值——从业者仅通过比较子群误差率即可判断全局校正是否有害，无需估计处理效应。在 τ_s > 0 的子群上诊断 AUC = 1.0。

**S3 [consensus]**: 实验验证的彻底性在同类论文中罕见——从合成 DGP（520 配置）→ 半合成 TweetEval → CausalForest 集成 → 4 开源 + 3 闭源 LLM → 真实 hate speech / Civil Comments 案例 → PPCI 互补性 → 16 组 LLM-dataset 诊断验证 → 假设 (A1)-(A5) 逐条敏感性分析 → bootstrap SE 校准。

**S4 [consensus]**: HB 混淆矩阵估计设计精良——κ>100 奇异性保护经全面验证（实际最大 κ=1.845, 53× 安全余量）、MCMC 收敛诊断优异（R̂ < 1.0034, ESS > 1618）、与 PPCI 互补性经 4-DGP 正交设计验证。

**S5 [consensus]**: 论文诚实透明——Limitations 坦诚适用边界（expert budget 阈值、near-degenerate CM 退化、K=8 scalability boundary），不过度声称。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [consensus: R1-N2 + R2-N2 agree]**: **κ≤1.25 适用性筛选条件过严——无实际 LLM 配置通过全部条件**
- Table 21 (Appendix X) 的 16 个 LLM-dataset-K 组合无一同时满足三个筛选条件（Proposition 3 诊断 + κ(C_s) ≤ 1.25 + expert budget）。瓶颈为 κ(C_s) ≤ 1.25，要求所有子群 FPR_s + FNR_s ≤ 0.20——无现有 LLM 满足。
- κ ≤ 1.25（Section 5.4 筛选）与 κ > 100（Algorithm 1 fallback guard）之间差距 ~80×，中间行为未讨论。
- 放松条件后 EC-HTE 在 79% (41/52) 配置优于 Global、100% (52/52) 优于 Stratified MLE——方法本身有效，但推荐筛选过于保守。
- **要求**：(a) 提供 κ ∈ {1.25, 2, 5, 10} 分层性能表；(b) Section 5.4 承认 κ ≤ 1.25 为 sufficient 非 necessary；(c) 解释两层阈值的功能差异。

**MF2 [consensus: R2-N1 + R1-W3 agree]**: **Frazis-Loewenstein (2003) scalar attenuation 对比不充分——关键经验结果被埋在 Appendix Z.4**
- 论文声称的三点区分（effect modifier vs regressor、δ_s·Δτ product structure、correction-induced vs attenuation bias）正确但仅 5 行处理。
- Appendix Z.4 Table 29 的关键发现（F-L scalar aggregate bias > uncorrected estimator；F-L per-subgroup dramatically over-corrects high-error subgroups）有力支撑论文论点，但放在附录第 28 页，审稿人很可能不会读到。
- **要求**：(a) Section 2 或 Section 3 增加 4-5 句正式对比段落；(b) Table 1 增加 F-L scalar 和 F-L per-subgroup 比较行。

### Should-Fix（影响评分但不一票否决）

**SF1 [consensus: R2-W1 + R1 agree]**: **缺乏真实因果 ground truth 验证**——所有 CATE 为合成注入。两位 Reviewer 均认为这是因果推断领域的结构性限制（需 RCT + ground-truth labels + known subgroup rates 同时存在），非本文特有缺陷。建议 Limitations 增加 1-2 句论证 semi-synthetic 设计为何是合理 proxy。

**SF2 [consensus: R2-W2 + R1 agree]**: **HB partial pooling 相对于 Dawid-Skene / Paun et al. 的新颖性未阐明**——Section 4.1 使用标准 Dirichlet-Multinomial 分层模型，James-Stein shrinkage 是 well-known。应明确定位为 "known technique, novel application context"。

**SF3 [consensus: R1-W4 + R2-W3 agree, 互补]**: **Assumption (A1) 敏感性分析范围有限**——Appendix Z.2 仅测试 outcome-dependent misclassification（γ ∈ [0, 0.20]），缺少 treatment-dependent misclassification。对 LLM text annotation，treatment assignment 可能系统改变文本特征进而影响 LLM 分类质量。建议增加 treatment-dependent 场景 + 讨论 LLM 特有违反模式。

**SF4 [consensus: R1-W1 + R2 agree]**: **二元效应修饰变量假设 (A3) 限制泛化性**——Z ∈ {0,1} 且 P(Z=1) = 0.5。Corollary 4 扩展到多类别但假设 uniform off-diagonal misclassification（对 LLM 不现实）。连续 Z 的理论扩展方向和离散化近似误差未讨论。

**SF5 [consensus: R1-W2 + R2 agree]**: **有限样本分析缺乏正式推导**——R_s = O_p(n^{-1/2}_expert) 声称未给推导。从 population identity 到 finite-sample estimator 的过渡需 delta method 或 matrix perturbation analysis。对 EMNLP 受众属 should-fix 非 must-fix。

**SF6 [consensus: R1-W5 + R2 agree]**: **Plug-in SE 系统性欠覆盖（93.8% vs 95%）缺乏 formal decision rule**——高误差子群 92.5%。Bootstrap 修正有效但 CI 宽度增加 2-3×。应给出基于 n_expert 或 κ(Ĉ_s) 的 plug-in vs bootstrap 选择规则。

**SF7 [consensus: R2-W4 + R1 agree]**: **Scalability to K >> 4 未充分讨论**——K=4 每子群需 ~30 labels，K=10 则需 300+。HB 模型隐含 shrinkage-based merging 但未显式讨论何时应合并子群。

---

## Reviewer Consensus

| 议题 | R1 | R2 | 共识 |
|------|-----|-----|------|
| κ≤1.25 过严 | N2 (Must-Fix) | AGREE | **Must-Fix** |
| F-L 对比入主文 | W3 (Should-Fix) | N1 (Must-Fix) | **Must-Fix** |
| 缺真实因果验证 | AGREE | W1 (Should-Fix) | Should-Fix |
| HB 新颖性定位 | AGREE | W2 (Should-Fix) | Should-Fix |
| (A1) 敏感性不足 | W4 (Should-Fix) | W3 (Should-Fix) | Should-Fix |
| 二元 Z 限制 | W1 (Should-Fix) | AGREE | Should-Fix |
| 有限样本推导 | W2 (Should-Fix) | AGREE | Should-Fix |
| Plug-in SE 规则 | W5 (Should-Fix) | AGREE | Should-Fix |
| Scalability K>>4 | AGREE | W4 (Should-Fix) | Should-Fix |

---

## Reviewer Divergence

| 议题 | R1 | R2 | Director 裁定 |
|------|-----|-----|-------------|
| Proposition 3 方向错误 | N1 (Must-Fix) | REBUT (原文正确) | **降级 Minor**：R2 验证原文 "ε_s < 0.088" 与代数一致，R1 疑为误读。但 clarity 可改进——建议分列 bullet points。 |
| 贡献定位模糊 | REBUT (结构已暗示) | N2 (Must-Fix) | **降级 Should-Fix**：论文结构已将 Theorem 1 置于首位，但可加一句明确声明。 |
| Abstract 信息过密 | REBUT (CL/ML 正常) | W5 (Should-Fix) | **驳回**：~175 words 在 200 限制内，数值密度对定量论文合理。风格偏好。 |

---

## Questions for Authors

1. Table 21 中 κ ≤ 1.25 阈值的理论或经验依据是什么？在 κ ∈ (1.25, 100) 范围内 EC-HTE 的行为如何？是否有分层推荐阈值？

2. 对于 treatment-dependent misclassification（处理组和对照组的 LLM 标注准确率不同），EC-HTE 的 robustness 如何？这在药物 RCT 或政策干预文本分析中是常见场景。

3. Remark 2 声称 asymmetric formulation "algebraically equivalent"，但 Appendix J 的 asymmetric formula 使用完整 2×2 FPR/FNR 参数且性能有改善（Table 6: RMSE 从 0.083 降至 0.074）。请澄清 equivalence 的具体范围。

4. 连续效应修饰变量（如 toxicity score）下 bias decomposition 的理论形式是什么？离散化引入的近似误差是否可控？

5. 对于 K > 4 的场景，HB partial pooling 的 shrinkage 能否被解释为隐式的 subgroup merging？是否有理论指导何时应显式合并子群？

---

## Missing References

**共识推荐（R1 + R2 均 AGREE）**:
- Miao et al. (2018) / Tchetgen Tchetgen et al. (2024) — proximal causal inference，LLM annotation 可视为 true label 的 proxy，bridge function 与 CM inversion 有结构相似性
- Cinelli & Hazlett (2020) — 形式化敏感性分析框架，可量化 (A1) 违反需要多大才能逆转结论

**可选参考（部分 AGREE）**:
- Hébert-Johnson et al. (2018) Multicalibration — subgroup-specific calibration，概念相关但技术框架不同
- Manski (2003) Partial Identification — (A1) 不成立时的替代框架

**驳回（R1 REBUT）**:
- Ratner et al. (2017/2020) Data Programming / Snorkel — 处理多弱标注源聚合，与单 LLM 的 subgroup CM 纠正设置不同
- Lu et al. (2022) prompt sensitivity — 上游标注质量问题，与本文的下游推断纠正正交

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 0 critical, 7 info）。

**Warnings**:
1. **Pages 3-6 连续 4 页无 figure/table**：从 Figure 1 (p2) 到 Table 1 (p7) 跨度 4 页。建议 Section 3/4 增加概念图或流程图。
2. **主文仅 3 个 display items**（Figure 1, Table 1, Figure 2）：大量实验结果推入附录，审稿人在主文中只能看到 1 个结果表和 1 个结果图。建议将 1-2 个关键附录表/图提升至主文。
3. **Limitations 章节过长**（~1.5 栏）：EMNLP 规定 Limitations 不计入页数但不能包含 "excessive additional content"。当前长度可能触发质疑，建议精简到 3-4 个核心点。

**Info**: Figure 1 位置合理（p2 顶部）、Figure 2 axis labels 字号偏小、Table 1 排版符合顶会标准、附录图表可读。

---

## Overall Assessment

**评分**: 3.5 / 5（Borderline Conference）
**置信度**: 4/5

**理由**:

论文解决了一个真实、重要且及时的问题——随着 LLM 在 CSS 因果推断中的普及，识别 global correction 的 subgroup-level bias 具有直接的实践价值。Theorem 1 的 bias identity 形式优美，Proposition 3 的诊断准则有独立实用价值，实验验证的广度和深度在同类论文中属于上乘。

两个 Must-Fix 问题阻止了更高评分：
1. **κ ≤ 1.25 筛选条件过严**使得论文自身推荐的诊断工作流在所有已测试的真实 LLM 上为空集，削弱了实际价值论证。方法在放松条件下仍有效（79% 优于 Global），但这与 Section 5.4 的严格叙事不一致。
2. **F-L 对比缺失**使得与最直接的理论先驱的区分度不足，可能导致 novelty 被低估。

七个 Should-Fix 问题中最重要的是：缺乏真实因果 ground truth（领域结构性限制）、HB 新颖性定位（应承认为 known technique）、(A1) 敏感性分析范围（缺 treatment-dependent 场景）。

**如果 rebuttal 能**：(a) 提供 κ 分层推荐阈值并承认 sufficient vs necessary，(b) 将 F-L 对比移入主文（Table 1 或 Section 2-3），(c) 明确 primary contribution 为 bias mechanism discovery 而非 method，**倾向上调至 4.0（Conference）**。

---

## Detailed Comments

### Section 1 (Introduction)
- 贡献列表三项，顺序暗示理论优先，但可加一句明确声明（R2-N2，降级为 should-fix）
- Footnote 1 的 "debiasing" 定义区分重要，考虑纳入正文（R1+R2 minor agree）

### Section 2 (Related Work)
- 与 F-L (2003) 的对比仅 5 行，应扩展为独立段落，引入 Appendix Z.4 的关键经验对比（MF2）
- 可补充 Miao et al. (2018) proximal CI 和 Cinelli & Hazlett (2020) 敏感性框架

### Section 3 (Theory)
- Theorem 1 证明正确，代数经独立验证
- Proposition 3 的 case analysis 文字密度过高，建议分列 low-error / high-error 两个 bullet（R17-M1）
- Remark 2 与 Appendix J 的 asymmetric extension 表述需对齐

### Section 4 (Method)
- Section 4.1 开头应明确 HB 为 "known technique, novel application context"（SF2）
- Algorithm 1 清晰可实现

### Section 5 (Experiments)
- Table 1 标题 "extreme heterogeneity" 可改为 "high Δτ regime" 以避免 cherry-picking 误读
- Section 5.4 的诊断工作流与 Table 21 的 κ ≤ 1.25 空集矛盾需正面处理（MF1）

### Limitations
- 覆盖度好但略长（~1.5 栏），建议精简
- 可补充 semi-synthetic 设计为何是 real causal validation 的合理 proxy（SF1）
- 缺 treatment-dependent misclassification 讨论（SF3）
- 缺连续 Z 扩展方向讨论（SF4）

### Appendix
- 29 个附录验证彻底，但需确保正文中的 key findings 不被埋没
- Appendix E 噪声符号 ε 与 Section 3 误差率 ε 冲突（R17-M2）
- 部分引用应更新至已发表版本（R17-M3）