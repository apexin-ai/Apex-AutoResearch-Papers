---
round: 4
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T09:35:53.587935+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5 (Fresh Review)

**论文**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts
**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)
**审稿模式**: Fresh（重新审稿，无先前记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性 / R2: 新颖性与完整性）
**轮次**: Round 1 独立审稿 → 交叉分享 → 1 轮收敛（无需第二轮）

---

## Summary

本文发现当使用全局（pooled）混淆矩阵纠正 LLM 标注错误用于异质性处理效应（HTE）分析时，会引入与子群误分类偏差 δ_s 和 CATE 异质性 Δτ 的乘积成正比的 subgroup-level 偏差（Theorem 1，精确恒等式，非上界）。在 50% 的实验配置中全局纠正使偏差恶化，低误差子群中 84.6% 受损。论文提出 EC-HTE（层级贝叶斯 subgroup-stratified 混淆矩阵估计 + CausalForestDML），并给出 Δτ-free 诊断准则（Proposition 2, AUC=0.86）。实验覆盖 520 合成配置（100 MC runs 每个）、semi-synthetic TweetEval（N=5000）、7 个 LLM（4 开源 + 3 proprietary）及两个 NLP 数据集（TweetEval + Civil Comments）。

---

## Strengths

**S1. [共识]** Theorem 1 的 bias decomposition identity 正确、优雅且有实用价值。Product form δ_s · Δτ / (1−2π̄) 的三因子分解清晰揭示了偏差来源，R² > 0.97 的经验验证令人信服。这是首次给出全局纠偏在异质误分类下引入 CATE 偏差的精确解析表达式。

**S2. [共识]** Proposition 2（"纠偏反而有害"）的充要条件 |δ_s|/((1−2π̄)·π_s) > 1 是对 LLM+causal inference 社区的重要且独立可用的警示。Δτ-free 诊断准则（AUC=0.86）打破了需要先估计 CATE 才能决定是否纠偏的循环依赖。

**S3. [共识]** 实验验证极为全面和诚实：520 配置 × 100 MC runs 的网格搜索，加上 semi-synthetic TweetEval、10 个 LLM（4 开源 + 6 闭源）、两个 NLP 数据集。丰富的鲁棒性检查（asymmetric R²=0.991、multiplicative effects coverage=0.955、R-learner 89% bias reduction、class imbalance R²≥0.976、subgroup misspecification coverage ≥0.945）。

**S4. [共识]** 诚实报告负面结果：仇恨言语案例（Appendix M, FNR=53.3%）、semi-real 混淆矩阵（Appendix R, RMSE=0.784）、TweetEval 不显著结果（p=0.395）均如实呈现。Applicability frontier（Figure 5）是少见的对方法适用边界的明确可视化。

**S5. [共识]** 与现有方法的区分清晰准确：PPI ≡ Global baseline、per-subgroup DSL ≡ Stratified MLE、EC-HTE 的增量贡献是层级部分池化，定位准确且有 Appendix U 的详细论证支撑。

**S6. [共识]** Limitations 部分写作质量高，覆盖 6 个关键局限（样本量需求、plug-in 近似、对称假设、函数形式、离散 subgroup、人口统计数据），既充分又不冗长。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [critical, 共识] κ>100 singularity guard 与论文自身实验证据存在约 80 倍差距**
- 主文 Algorithm 1 使用 κ(Ĉ_s) > 100 作为 guard（仅在 π_s > 0.495 时触发），但 Appendix R 的实验表明：(a) FNR=0.526 的子群（κ 远低于 100）RMSE 已达 0.784（n=100），是 naive 的 6.4×；(b) Appendix R 自己建议 κ(M̂_s) ≤ 1.25 作为 EC-HTE 优于 Global 的充分条件。主文方法描述未同步更新，给实践者错误的安全感。
- **建议**：将 Appendix R 的诊断规则（max(FPR,FNR) < 0.5 AND n_expert/K ≥ 25）整合到 Algorithm 1 中，区分 "numerical singularity guard" 和 "practical applicability conditions"。

**W2. [warning→critical（升级）, 共识] Abstract Δπ×Δτ 符号与 Theorem 1 不一致**
- Abstract 声称偏差 "exactly proportional to the product of misclassification heterogeneity and CATE heterogeneity (Δπ × Δτ)"，但 Theorem 1 为 δ_s · Δτ / (1−2π̄)。Δπ 是全局 range 量，δ_s 是 per-subgroup 量，仅在 K=2 等权重时线性相关。分母项在 Abstract 中完全缺失。定理本身正确，问题在于非正式叙述过度简化。
- R1 建议降为 should-fix；Director 判断：鉴于这是论文第一贡献在最显眼位置的表述，**维持为 must-fix**。
- **建议**：Abstract 改为 "proportional to each subgroup's deviation from the pooled error rate (δ_s) times CATE heterogeneity (Δτ)" 或明确标注 Δπ×Δτ 为 informal summary。

### Should-Fix（影响评分但不一票否决）

**W3. [warning, 共识] Corollary（Appendix C）多分类扩展证明不完整**
- 证明在 "Expanding the matrix-vector product and collecting terms yields" 处跳过关键代数推导。g(π̄) = 1/(1−Jπ̄/(J−1)) 仅对均匀 off-diagonal 误分类成立，但 Corollary 陈述未明确限定此条件。对一般 J×J 混淆矩阵，g(π̄) 不再是标量。
- 缓解因素：Corollary 仅在附录中，不影响主文所有 J=2 实验。
- **建议**：补全均匀 off-diagonal 的完整推导，或将 Corollary 明确限定为 "uniform off-diagonal misclassification" 的特殊情况。

**W4. [warning, 共识] Plug-in SE 近似的覆盖率缺口未量化**
- 论文声称 n_expert ≥ 100 时 plug-in 合理，但从未给出 n=50 或 n=100 时 plug-in vs bootstrap SE 的覆盖率对比。Table 1 仅报告 n≥250 的 coverage。
- 缓解因素：Limitations 已承认此局限，主实验均在 n≥250 进行。
- **建议**：补充 3-4 个代表性配置下 plug-in vs bootstrap coverage 的消融实验。

**W5. [warning, 共识] Semi-synthetic TweetEval 中 EC-HTE 未显著优于 Global，但主文叙事偏向正面**
- TweetEval K=4, extreme: EC-HTE |bias|=0.027 vs Global=0.023 (p=0.395, 不显著), RMSE=0.225 vs 0.124 (几乎 2×)。这是最接近真实场景的实验，结果应在 Abstract/Introduction 中更突出呈现，而非将叙事重心放在 K=2 极端异质性的最佳配置上。
- **建议**：Abstract 或 Introduction 中增加一句限定。

**W6. [warning, 共识] Audinet de Pieuchon et al. (2025, EMNLP) 讨论严重不足**
- 该工作直接 benchmark DSL/PPI 用于 LLM 标注 debiasing 的下游参数估计，发现 bias-variance tradeoff。作为最直接的 prior work，仅在 Appendix F 一句话提及。
- **建议**：在 Section 2 的 "Prediction-powered and design-based correction" 段落中加入 2-3 句，明确说明其 scope (population-level) 与本文的区别 (subgroup-conditional CATE)。

**W7. [warning, 共识] 缺乏完全真实因果数据验证**
- 所有实验中 CATE 均为合成注入。Multi-LLM 验证了 Δπ 异质性的真实存在（证据链前半段），但 EC-HTE 的 CATE correction 效果从未在完全真实场景中被验证。
- 缓解因素：合成实验设计全面合理，Limitations 已承认。非一票否决。
- **建议**：如不可行，在 Introduction 中更早、更明确说明此局限。

**W8. [warning, 共识] (A5) 违反仅做有限测试**
- Appendix O 的 heterogeneous-τ DGP 仅 1 模型、K=2、50 MC runs，远少于主实验的 520 配置 × 100 MC。
- **建议**：在主实验网格子集上补充系统性违反 (A5) 的实验（至少 Δτ_s 与 δ_s 正相关/负相关两种情形）。

### Minor（不影响接收）

**M1.** CausalForestDML 超参数未完整报告（树数量、最小叶子大小、子采样比例、交叉拟合折数）。应在 Appendix 补充。

**M2.** "50% of configurations" 声称部分由对称参数网格设计决定。建议降低修辞突出度，强调 84.6% low-error subgroup 损害率。

**M3.** Figure 5 (applicability frontier) 是最有实践价值的图之一，应从 Appendix 移入正文。Figure 2 的 (a)(b) colorbar 范围不统一。

**M4.** "debiasing" 脚注（Section 3）位置不够显眼，建议移至 Abstract 或 Introduction。

**M5.** Appendix E 的 DGP 参数组合如何得到正好 520 个配置，建议明确列出计数公式。

**M6.** Törnberg (2024) 仍为 arXiv 格式，若已正式发表应更新。

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉分享中达成一致：

1. **[AGREE] Theorem 1 和 Proposition 2 正确且有实用价值** — 理论贡献是论文最强部分
2. **[AGREE] κ>100 guard 与自身证据矛盾** — 最严重的技术问题
3. **[AGREE] Abstract 符号不精确** — 需修正但定理本身无误
4. **[AGREE] Semi-synthetic 叙事偏差** — Abstract/Intro 应更平衡
5. **[AGREE] Corollary 证明不完整** — 限于附录，须补全或限定
6. **[AGREE] Plug-in SE 未量化** — 应补充消融实验
7. **[AGREE] Audinet et al. 讨论不足** — 应移入主文 Related Work
8. **[AGREE] (A5) 测试不足** — 需更系统的违反实验
9. **[AGREE] 无真实因果数据** — 非一票否决但限制说服力
10. **[AGREE] Figure 5 应移入正文** — 提升实用性叙事

---

## Reviewer Divergence

**R2-N2: 方法论新颖性**
- R2 认为 EC-HTE 是已有组件的直接组合（HB + CausalForest + 矩阵求逆），方法论创新有限，标为 critical。
- R1 **[REBUT]**：核心贡献不在方法本身而在理论发现（Theorem 1 是对 measurement error 文献的实质性推进，Proposition 2 是新发现，Δτ-free 诊断打破循环依赖）。EC-HTE 的 HB partial pooling 相对于 stratified MLE 在 87.5% 配置中有改进，并非平凡。
- **Director 判断**：R1 的反驳有力。论文已定位为 "problem-identification paper"，理论贡献是核心价值。但建议在 Introduction 中更明确将 EC-HTE 定位为 "a natural correction enabled by this insight"，避免过度声称方法新颖性。**不作为 must-fix。**

**R1-W3: 代码仓库缺失**
- R1 标为 should-fix（无代码仓库、MCMC 框架未报告）。
- R2 **[REBUT]**（部分）：double-blind 期间不提供代码是标准做法。MCMC 细节（4 chains, 4000 iterations, etc.）足以复现。建议降为 minor。
- **Director 判断**：同意 R2。降为 minor，仅需在 Appendix 指明概率编程框架。

**R1-W5: R² 数值不一致**
- R1 认为 Abstract 和 Section 3 的 R² 不一致。
- R2 **[REBUT]**：逐行核实后确认 0.994 (K=2 symmetric) 和 0.991 (asymmetric, Remark 2) 是不同实验的不同数值，无实际矛盾。可读性可改善。
- **Director 判断**：同意 R2。非实质性问题，仅建议在 Remark 2 中更清楚标注。**不列入报告 weaknesses。**

---

## Questions

1. 在 plug-in SE 近似下，n_expert=50, K=4 时 bootstrap 或 full Bayesian propagation 给出的覆盖率与 plug-in 的差距是多少？
2. Corollary 的 g(π̄) 公式对非均匀 off-diagonal 误分类如何修改？是否应限定为 "uniform off-diagonal case"？
3. Algorithm 1 中 κ>100 的阈值如何与 Appendix R 建议的 κ(M̂_s) ≤ 1.25 + max(FPR,FNR) < 0.5 协调？实践者应使用哪个？
4. Semi-synthetic TweetEval 中 RMSE=0.225 vs 0.124（1.8×），是否意味着子群大小不均衡时 stratification variance cost 过高？是否有缓解策略？
5. Assumption (A5) 在 Δτ_s 与 δ_s 正相关时（实际场景中可能出现），bias identity 的 practical implications 如何变化？
6. EC-HTE 与 Audinet de Pieuchon et al. (2025) 发现的 bias-variance tradeoff 有何关系？

---

## Missing References

1. **Audinet de Pieuchon et al. (2025, EMNLP)** — 已在附录引用但主文讨论严重不足。最直接的 prior work。
2. **Schennach (2020)** — "Mismeasured and Unobserved Variables"，更一般的测量误差理论框架。
3. **Zhang et al. (2023)** — 系统性评估 LLM 标注质量的近期工作。
4. 引用覆盖度总体评估：测量误差（Fuller, Carroll, Gustafson, Hu & Schennach）、计量经济学误分类（Bound, Frazis, Mahajan, Lewbel）、HTE（causal forests, DML, meta-learners）、纠正方法（PPI, DSL, PPCI, ForestIV）、标注模型（Dawid & Skene 到 Paun et al.）——**总体全面，无其他重大遗漏**。

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求（项目配置中 external_review.paperreview_ai.enabled 未启用）。

---

## Visual Layout Check（非评分项）

**状态**: done（耗时约 3.5 分钟）

| 严重程度 | 发现 |
|---------|------|
| ⚠️ warning | Figure 1（p2）到 Table 1（p7）之间跨 5 页无 figure/table，正文仅 3 个 display items（2 fig + 1 table），实证内容的视觉密度偏低。建议将附录中某个关键图表（如 Figure 5 applicability frontier）提升至正文。 |
| ℹ️ info | Figure 2 heatmap 的 axis tick labels 和 "debiasing helps/hurts" 标注字号偏小（约正文 60%），打印后可能影响可读性。 |
| ℹ️ info | 正文全部实验结果压缩在最后 2 页（Table 1 + Figure 2），审稿人需耐心翻过 5 页理论才看到数据。对第一印象略有不利。 |
| ℹ️ info | 最后一页（p21）内容约占 60%，有一定空白（附录末页影响不大）。 |
| ℹ️ info | "Recommended workflow" 框排版整洁，是加分项。 |

视觉审查与 Reviewer 意见一致：Figure 5 (applicability frontier) 应移入正文以改善 pp.3-7 的视觉密度。

---

## Overall Assessment

**评分**: 3.5 — Borderline Conference

**EMNLP 2026 评分标准**: 3.5 = Borderline Conference（介于可被主会议接收和仅适合 Findings 之间）

**置信度**: 4/5（两位 Reviewer 独立给出相同评分，交叉后维持，13 条意见中 10 条共识）

**理由**:

论文在**问题识别层面**有清晰的贡献——Theorem 1（精确 bias identity）和 Proposition 2（"纠偏反而有害"的充要条件 + Δτ-free 诊断）是对 measurement error × causal heterogeneity 文献的实质性推进。实验验证极为全面和诚实（520 配置 × 100 MC、7 LLM × 2 数据集、多种鲁棒性检查），在同类论文中属于高标准。

**主要障碍**:
1. **方法论与叙事不一致（W1, W2, W5）**: κ>100 guard 与自身实验矛盾、Abstract 符号不精确、semi-synthetic 负面结果被正面叙事淹没——这三个问题共同指向论文在"方法可靠性"的呈现上存在缺陷。
2. **理论完整性（W3, W4）**: Corollary 证明跳步、plug-in SE 未量化——可修复但需要实质性工作。
3. **验证完整性（W7, W8）**: 无真实因果数据、(A5) 违反测试不足——限制了论文对目标受众（CSS 研究者）的说服力。

**与 Conference (4.0) 的差距**: 如果作者能解决 W1（κ guard 更新）、W2（Abstract 符号精确化）、W5（叙事平衡）和 W6（Audinet et al. 讨论），论文有望达到 Conference 水准。W3-W4 可通过 rebuttal 期间的补充实验解决。W7 是结构性限制，需在 rebuttal 中充分论证合成验证为何足够。

**与 Findings (3.0) 的距离**: 论文远高于 Findings 下限。理论贡献的质量、实验的全面性和诊断工具的独立实用性使其成为有竞争力的 Borderline Conference 候选。

---

## Detailed Comments

### Section 3 (Theory)
- Theorem 1 证明正确完整（Appendix B 的 δ_s 代换验证路径清晰）。
- (A5) 假设正式列出是必要的改进。theory.tex line 61 的泛化说明应更明确给出 Δτ_s ≠ 0 时的完整 bias 表达式。
- Remark 2（asymmetric extension, R²=0.991）与主定理的 R²=0.994 容易混淆，建议加明确标注。

### Section 4 (Method)
- HB 模型规格和收敛诊断充分（4 chains, 4000 iter, R̂ < 1.0034, ESS > 1618）。
- **κ>100 guard 是最紧急的修改项**：至少应在 Algorithm 1 中加入 max(FPR,FNR) < 0.5 条件。
- plug-in SE 的 n_expert ≥ 100 声称需要定量支撑。
- CausalForestDML 超参数应在 Appendix 补充。

### Section 5 (Experiments)
- 520 配置的参数网格设计合理，覆盖了 Δπ × Δτ 的完整空间。
- Semi-synthetic TweetEval 的诚实报告值得肯定，但应在 Abstract/Intro 中更突出。
- Multi-LLM 验证（Section 5.5）是重要的实践证据，Δπ ∈ [0.08, 0.198] 确认了误分类异质性的普遍性。
- 配置计数（520 = ?）应在 Appendix E 明确说明。

### Related Work (Section 2)
- 覆盖全面，与 PPI/DSL/PPCI/ForestIV 的区分准确。
- Audinet de Pieuchon et al. (2025) 必须在主文中讨论。
- Imai & Yamamoto (2010) 的三层区分（treatment misclassification vs effect modifier misclassification）清晰。

### Format Compliance
- ✅ 正文 ≤ 8 页（Conclusion 在 page 8 结束）
- ✅ `[review]` 选项启用
- ✅ 匿名完整（\author{Anonymous}，无自引泄露）
- ✅ Limitations 章节充分
- ⚠️ Figure 2 colorbar 不统一、font size 偏小
- ⚠️ Törnberg (2024) 引用格式需确认