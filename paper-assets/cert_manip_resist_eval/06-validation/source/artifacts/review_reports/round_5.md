---
round: 5
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-24T18:13:42.327196+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 5 审稿报告：The Shifting Predictor: Panel-Size-Dependent Vulnerability Patterns in LLM Judge Panels

**Venue**: EMNLP 2026 Main (via ACL Rolling Review)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+统计推断+实验设计；R2: 新颖性+完整性+写作质量+格式合规）
**交叉回应**: 已完成，1 轮达成共识

---

## Summary

本文研究 LLM 多评判面板在对抗性攻击下的脆弱性如何随面板大小变化。作者提出 K_eff（基于互信息的有效独立通道数指标），在 15 个模型 × 6 种攻击 × 2 个基准 × 3 个面板大小（K∈{3,5,7}，最多 6,435 panels）的系统性实验中，发现：(1) K_eff 系数方向在所有 12 个条件下为正（多样性与脆弱性正相关），但显著性因推断方法而异（0–12/12）；(2) "预测因子转移"——K=3 时 η_max 和 K_eff 共同贡献，K≥5 时 K_eff 成为主导预测因子；(3) 聚合方法影响可预测性（R²: threshold 0.83, Bayesian 0.09）。论文使用 5 种推断方法、Cinelli-Hazlett 敏感性分析、crossed random effects 等大量 robustness checks。

---

## Strengths

**S1. 方法论自我批判出色。** 论文反复、明确地承认 diversity-capability 混淆的局限性（Introduction、Section 6、Limitations），不回避对核心发现不利的证据（如 K=3 clustered SE 下 K_eff 0/12、Cinelli-Hazlett 69% 条件失败）。这种科学诚信在同类实证工作中属上乘。[R1-S3, R2-S2, 双方 AGREE]

**S2. 系统性实验设计。** 15 模型 × 6 攻击 × 2 基准 × 3 面板大小的全枚举设计避免了采样偏差。四种聚合方法的比较增加了实用价值。Threat model 定义清晰（Definition 1, Theorem 1）。[R1-S1/S2, R2-S3]

**S3. 丰富的 robustness 检查体系。** 5 种推断方法（OLS、clustered SE、mixed effects、wild bootstrap、fractional logit）+ crossed random effects + Cinelli-Hazlett 敏感性分析 + ε 敏感性 + 温度 pilot + 跨基准预测 + 随机子样本。20 个附录节提供了极其详尽的补充分析。[R1-S4, R2-S1]

**S4. Theorem 1 (Weakest-Link Monotonicity) 提供理论锚点。** 证明本身简单但为 η_max 提供了形式化基础，empirical verification（58% stochastic dominance in 61/105 pairs）加强了理论-实验连接。[R2-S4]

**S5. 实用导向的 panel 设计建议。** Figure 4（panel selection strategy comparison）清晰显示 min(η_max) 在所有 12 条件下 ASR 最低，对部署者有直接价值。[R2-S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, R1+R2 AGREE] **Diversity-capability confound (r=0.70–0.81) 在 69% 条件下可解释 K_eff 关联，核心因果解释力不足。**

Cinelli-Hazlett 分析显示，在 25/36 条件下，已知的 η_max 混淆即可将 K_eff 系数归零（Table 10）。RV 异质性极大（0.005–0.522）：RV=0.005（K=7 MMLU authority bias）意味着极微弱混淆即可消除效应。论文将 Pool A（r=0.50）的 10/12 Cinelli-Hazlett "成功"作为稳健性证据（Appendix L），但 Pool A 最大功效仅 30.1%（Table 12）——在如此低功效下通过 Cinelli-Hazlett 是 trivially expected，不构成稳健性证据。Abstract 的 hedging（"limits causal interpretation"）不够强，标题和 Contribution 1 仍暗示 K_eff 是独立有意义的预测变量。

*跨轮追踪*：R3 首次提出（78%），R4 更新为 69%，R5 仍未充分解决。Pool A 解读问题是本轮新增批评。

**MF2** [critical, R1+R2 AGREE] **Predictor shift 在 API-only 子集不复现，可能是量化 artifact。**

去掉 6 个 AWQ INT4 量化模型后（9 API 模型，r=0.85, VIF=4.4），K_eff 从 7/12 降至 2–3/12，η_max 反而增强至 8/12，predictor shift 完全消失（Table 8）。关键论证：共线性（VIF=4.4）不解释方向性消失——如果 K_eff 效应是真实的，高共线性应导致两个预测变量均不显著（mutual suppression），而非 η_max 单独显著。Appendix H 随机子采样进一步确认 K_eff 主导率在 n_local=3–4 时达峰值。论文未报告 API-only 子集的统计功效，无法区分"shift 不存在"和"检测不到 shift"。

*跨轮追踪*：R3 首次提出（tier 偏斜），R4 确认非复现，R5 升级为 critical——R1 提供了共线性不解释方向性消失的论证。

**MF3** [critical, R1 AGREE with reservation from R2] **低 cluster 数 (9–13) 使统计推断可靠性不足。**

Cluster 数（K=3:13, K=5:≤11, K=7:≤9）远低于 Cameron et al. (2008) 的 ≥20 阈值。K=7 时 Rademacher weights 仅 2⁹=512 唯一权重向量但 B=9,999，每个向量重复约 20 次。OLS 12/12 vs bootstrap 4/12 的骤降可解释为 OLS 的 type I error 膨胀，而非 bootstrap 保守。Crossed RE 的 t(14) df 选择未讨论 Satterthwaite/KR 替代。"X/12 显著"的计数方法丢失效应量和 p-value 分布信息。

R2 程度更温和：认为 fractional logit（不依赖 bootstrap）和 crossed RE 部分缓解此问题。

*跨轮追踪*：R3 首次提出（warning），R4 升级为 critical，R5 持续。

**MF4** [critical, R1-N1, R2 AGREE on framing] **K_eff 的 Gaussian copula 理论基础被 97–100% 拒绝，但正文仍使用"有效独立通道数"解释。**

Cramér-von Mises GoF 在 α=0.05 下拒绝了 97–100% 的 judge pairs 的 Gaussian copula（Appendix T）。Appendix T 最后一段已将 K_eff 定位为"nonparametric, information-theoretic measure of pairwise alienation"——实际上承认是经验性指标。但 Section 3 和 Section 6 仍使用"effective independent channels"的语言，造成 framing 不一致。Plug-in MI 和 closed-form 的排序一致性（Spearman ρ≈0.86）只说明两种操作化相关，不验证"有效独立通道数"这一语义解释的正确性。

R2 认为问题更多在 framing 层面而非方法论层面。双方 AGREE 修改方向：将"effective independent channels"降格为 motivating analogy。

*跨轮追踪*：R4 首次提出，D044 策略转向已 in_progress，R5 认为 framing 不一致仍未完全解决。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, R1+R2 AGREE] **log(ASR+ε) 在高零值率下不适当，fractional logit 应为主要规范。**
K=7 ARC 零 ASR 率达 38–40%。ε=10⁻⁶ 使零 ASR 映射到 log(10⁻⁶)≈−13.8，形成双峰结构。K=3 时 3 个条件出现 K_eff 系数符号翻转（Appendix M）。Fractional logit 98.6% 方向一致（71/72）且结果更强（9/12→11/12→12/12），应提升为 primary specification。

**SF2** [warning, R2 Must-Fix → R1 降为 Should-Fix, 最终取 Should-Fix] **仅覆盖多选题基准（MMLU+ARC），泛化性受限。**
LLM judge panel 的主要应用场景是 open-ended generation，多选题是最简单的评估类型。论文标题和 Introduction 面向一般性结论但证据仅覆盖 MC 格式。R1 指出方法论框架不依赖 MC 格式，建议通过标题/abstract scope qualifier 解决（framing 问题而非实验设计缺陷）。

**SF3** [warning, R1+R2 AGREE] **Predictor shift 可能部分是统计功效差异的产物。**
MDE 从 K=3 的 0.144 降至 K=5 的 0.048（3 倍改善）。K_eff 显著性增长（4→7→8）可能部分反映功效增强。η_max 方差随 K 增大可能收缩，造成不对称功效。双方 AGREE 应以 standardized effect size 变化而非显著性计数作为跨 K 比较的主要证据。

**SF4** [warning, R1+R2 AGREE] **聚合规则分析表面化。**
Threshold R²=0.83 vs Bayesian R²=0.09 的 10 倍差异仅一段话解释。Bayesian 非单调行为（6/12→7/12→0/12）的"posterior concentration"假说未经验证，且与其单调递减预测矛盾（K=5 达峰值）。Bayesian 在 K=7 完全中和 K_eff（0/12）是重要安全工程发现但被边缘化。

**SF5** [warning, R1+R2 AGREE] **INT4 量化混淆未被充分控制。**
6 个 AWQ INT4 量化模型全在 lightweight tier，量化状态与 capability tier 完全混淆。需在主回归中加入量化 dummy variable 及 K_eff 交互项，直接检验 predictor shift 是否依赖量化模型参与。

**SF6** [warning, R2-W4, R1 conditional REBUT] **K_eff 相对 κ-diversity 增量贡献有限（ρ=0.978）。**
K_eff 的唯一独特优势在于展现 predictor shift（κ-diversity 显示 8→7→6 无 shift），但此优势条件性地依赖于 shift 本身的可信度——而 shift 受到 MF1/MF2/SF3 的质疑。

**SF7** [warning, R2-W3, R1 AGREE minor] **Conclusion 过于简略（约 5–6 行），缺少 implications 和 future work。**

### Minor（不影响接收）

- 数字密度过高：Results/Analysis 几乎每句含多个括号统计量，缺乏直觉解释 [R2]
- OpenRouter API 快照一致性未讨论，应报告数据采集时间窗口 [R1-M1, R2]
- Temperature pilot 仅 3/15 模型，不足以支撑 "robust to temperature" 的一般性声明 [R1-M2]
- Table 2 报告标准化系数但未报告原始系数，effect size 的实际显著性不清楚 [R1-M5]
- Crossed RE 的 t(14) df 未讨论 Satterthwaite/KR 替代 [R1-M4]
- gemini-3.5-flash 26.3% format error rate 可能引入噪声 [R2]
- Abstract "newly characterized in the LLM judge setting" 表述不精确 [R2]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：

1. **Diversity-capability confound 是最根本的问题**（MF1）：r=0.70–0.81 下 69% 条件失败，Pool A 功效不足不能作为稳健性证据
2. **API-only 非复现严重削弱 predictor shift**（MF2）：共线性不解释方向性消失，量化模型驱动 K_eff 变异
3. **Fractional logit 应为 primary specification**（SF1）：双方一致建议
4. **量化 dummy variable 必须加入回归**（SF5）：直接检验 shift 是否依赖量化模型
5. **以 effect size 而非显著性计数展示 predictor shift**（SF3）：跨 K 的标准化系数变化轨迹
6. **聚合分析需要深化**（SF4）：验证 Bayesian posterior concentration 假说
7. **Overall 评分 3.0（Findings）**：双方独立评分一致
8. **论文的方法论透明度和自我批判值得肯定**（S1）

---

## Reviewer Divergence [REBUT]

| 问题 | R1 立场 | R2 立场 | 最终判定 |
|------|---------|---------|---------|
| Soundness | 2.5/5 | 3.5/5 | R1 因 copula 拒绝和 cluster 数给出更低分；R2 认为方法论执行扎实，问题更多在 framing 和生态系统限制 |
| Excitement | 3.5/5 | 2.5/5 | R1 认为研究问题本身有价值；R2 认为描述性发现影响力有限 |
| MC-only 严重程度 | Should-Fix（framing 问题） | Must-Fix（实验覆盖不足） | 取 Should-Fix——方法论不依赖 MC 格式，可通过 scope qualifier 解决 |
| K_eff vs κ-diversity | 部分 REBUT（Table 16 shift 特异性） | 增量贡献不明确 | R1 rebut 有说服力但附带 caveat |
| tilde 符号 η_joint ~ K_eff·η_max | 可能误导 | 上下文已足够清晰 | R2 REBUT 有说服力，不构成实质问题 |

---

## Questions for Authors

**Q1** [R1+R2 共同提出] 在主回归中加入量化状态 dummy variable（及其与 K_eff 的交互项）后，predictor shift 是否仍然存在？这是区分"diversity 效应"和"量化 artifact"的关键检验。

**Q2** [R1] API-only 子集（C(9,3)=84, C(9,5)=126 panels）在不同 K 下的统计功效估计是多少？以区分"shift 不存在"和"检测不到 shift"。

**Q3** [R1] 是否考虑过 exp(−2·MI) 以外的 MI→有效通道数映射函数？其他变换（如 exp(−c·MI) 中 c 的敏感性，或 sigmoid 变换）是否产生类似的 predictor shift？

**Q4** [R1] Cinelli-Hazlett RV=0.005（K=7 MMLU authority bias）vs RV=0.522（K=7 MMLU prompt injection）的巨大异质性如何解释？是否暗示 K_eff 效应是攻击类型特异性的？

**Q5** [R2] Bayesian calibration 在 K=7 完全中和 K_eff（0/12）。这一发现的安全工程意义是什么？为何不将此作为主要贡献？

**Q6** [R2] K∈{3,5,7} 全为奇数。偶数 K 下的 tie-breaking 机制可能如何改变 predictor shift 的性质？

**Q7** [R1] 300 items 的 ASR 估计的标准误约多少？是否存在 attenuation bias？

---

## Missing References

1. **Li et al. (2024)** "Understanding Model Ensemble in Transferable Adversarial Attack" (arXiv:2410.06851) — 信息论角度分析 ensemble diversity 对对抗迁移的影响 [R2 首提, R1 AGREE]
2. **Zhu et al. (2020)** "DVERGE: Diversifying Vulnerabilities for Enhanced Robust Generation of Ensembles" (NeurIPS 2020) — training-time diversity control 增强鲁棒性 vs 本文 post-hoc diversity 与脆弱性正相关，表面矛盾值得讨论 [R2 首提, R1 AGREE]
3. **Cameron & Miller (2015)** "A Practitioner's Guide to Cluster-Robust Inference" (J. Human Resources) — 对小 cluster 数推断有更详细讨论 [R1]
4. **MacKinnon & Webb (2017)** "Wild Bootstrap Inference for Wildly Different Cluster Sizes" (J. Applied Econometrics) — 不均衡 cluster 大小问题 [R1]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（2026-05-24 17:51–17:55 UTC）

**Findings**（0 critical, 2 warning, 13 info）：

- **[warning] Page 7**: Display items 过度集中——Figure 2（4 面板柱状图）+ Figure 3（折线图）+ Table 4 同时出现。图表尺寸被压缩，axis label 和 legend 文字偏小（接近正文字号 60–65%），打印时可能影响可读性。建议将 Table 4 或 Figure 3 移至 page 8。
- **[warning] Page 8**: 整页纯文本（Section 6 + Limitations），与 page 7 高密度形成强烈反差。布局节奏不均衡。
- **[info]** 所有表格使用 booktabs 风格，格式统一。未发现 margin overflow 或 LaTeX 渲染错误。正文 8 页含 3 figures + 4 tables = 7 display items，密度适中。References 格式一致，无 [?] 未解析引用。

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

**评分理由**：

论文研究了一个新颖且有时效性的问题（LLM judge panel 的 diversity-vulnerability tradeoff），实验设计系统化（15 模型全枚举），方法论透明度和自我批判在同类工作中属上乘。

然而，四个相互关联的核心问题限制了贡献的稳健性：

1. **Diversity-capability confound 无法分离**（r=0.70–0.81, Cinelli-Hazlett 69% 条件失败）——核心发现可能完全由 capability deficit 解释
2. **Predictor shift 在 API-only 子集不复现**——可能是量化 artifact 而非真实结构效应
3. **低 cluster 数使统计推断不可靠**（9–13 clusters vs ≥20 阈值）——OLS 可能存在 type I error 膨胀
4. **K_eff 理论解释在 copula 被拒后不成立**——"有效独立通道数"语义失去支撑

这些问题共同导致核心 claim 的证据强度与 abstract/introduction 的 framing 不匹配。论文作为 Findings 接收是合适的，条件是：(1) framing 与证据强度匹配（abstract 加入更强的 hedging）；(2) 加入量化 dummy variable 控制分析；(3) 以 effect size 而非显著性计数展示 predictor shift；(4) 将 fractional logit 提升为 primary specification。

**官方维度评分（综合两位 Reviewer）**：

| 维度 | R1 | R2 | 综合 | 理由 |
|------|----|----|------|------|
| Soundness | 2.5 | 3.5 | 3.0 | 方法论执行扎实但理论基础和推断可靠性存在问题 |
| Excitement | 3.5 | 2.5 | 3.0 | 问题有价值但描述性发现的影响力受限于混淆 |
| Reproducibility | 4.0 | 4.0 | 4.0 | 细节充分，承诺开源，但 API 快照一致性需讨论 |

**Confidence**: 4/5（两位 Reviewer 均为高置信度）

---

## Detailed Comments

### Section 3 (Threat Model)
- Eq. 1 的 exp(−2·MI) 变换需重定位为经验性 MI-based 指标，放弃"有效独立通道数"的 literal interpretation [MF4]
- η_joint ~ K_eff · η_max 的 tilde 符号已有"intuition rather than a formal bound"的 qualifier，不构成实质问题 [R2 REBUT R1-W5]

### Section 4 (Methodology)
- Table 1: 6 个 AWQ INT4 模型全在 lightweight tier——量化状态与 capability tier 完全混淆 [MF2, SF5]
- Section 4.5: log(ASR+ε) 应降为 robustness check，fractional logit 提升为 primary [SF1]
- Section 4.6: cluster count 低于阈值——应报告 cluster 大小均衡性、考虑 Webb six-point distribution [MF3]

### Section 5 (Results)
- Section 5.2: predictor shift 应以跨 K 的 standardized effect size 变化轨迹为主要证据，而非 "X/12 显著"计数 [SF3]
- Section 5.5: 聚合方法分析需扩展——验证 Bayesian posterior concentration 假说，讨论非单调行为 [SF4]

### Section 6 (Analysis)
- API-only 非复现的讨论应更突出——目前放在正文末尾且未在 abstract/intro 反映 [MF2]
- Pool A Cinelli-Hazlett 结果不应作为稳健性证据——功效仅 30.1% [MF1]

### Section 7 (Conclusion)
- 扩展至 1/3–1/2 column，增加 deployment implications 和 future work [SF7]

### Limitations
- 已覆盖主要局限但 MC-only scope 的标注需从 Limitations 延伸到标题/abstract [SF2]

### Related Work
- 增加 Li et al. (2024), Zhu et al. (2020) DVERGE, Cameron & Miller (2015), MacKinnon & Webb (2017)

### 格式合规
- ✅ 正文 8 页，abstract 约 187 词，double-blind，Limitations 在正文内，附录无 Limitations
- ⚠️ Page 7 display item 密度过高，建议重新分布