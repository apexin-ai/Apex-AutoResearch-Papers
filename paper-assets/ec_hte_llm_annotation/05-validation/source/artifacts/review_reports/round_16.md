---
round: 16
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T14:27:12.540139+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 16 Consolidated Review Report

**Venue**: EMNLP 2026 (via ARR)
**Reviewers**: 2 (方法严谨性 + 新颖性/完整性)
**Rounds**: 1 (交叉回应后收敛，无需额外轮次)
**Paper**: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"

---

## Summary

本文推导了一个精确偏差恒等式，刻画全局混淆矩阵校正如何在子群级引入乘积形式偏差 δ_s·Δτ/(1−2π̄)。该恒等式在 520+ 合成配置和 11 个真实 LLM 混淆矩阵上以 R²≥0.97 验证。基于该恒等式提出的诊断条件可在不估计处理效应的情况下预测校正何时加剧偏差（合成 AUC=0.86，真实 LLM AUC=0.63），配套的分层贝叶斯校正方法（EC-HTE）实现 7.4× 偏差缩减并维持近名义覆盖率。

## Strengths

**S1. 精确偏差恒等式新颖且验证充分。** 乘积形式分解提供清晰的机制洞见（何时以及为何全局校正失效）。R²≥0.97 横跨合成网格 + 11 个真实 LLM CM，令人信服。

**S2. 实验覆盖全面。** K∈{2,4,8}、非对称 CM（48 配置）、处理依赖误分类、混杂处理、结果依赖误分类、8 个真实 LLM × 2 数据集——鲁棒性验证程序彻底。

**S3. 实际影响明确。** 14.9% 符号反转率和 7.4× 偏差缩减量化了真实问题（LLM 标注偏差对因果推断的影响），并给出可操作的解决方案。PPCI 组合展示了方法的可组合性。

**S4. 局限性报告透明。** AUC=0.63（真实 LLM）、K=8 退化、n_expert/K≥50 建议均有报告——虽然部分结果埋在附录中。

**S5. 形式化基础扎实。** Theorem 1 作为种群级精确恒等式（非界）数学上干净。Corollary 6 推广到一般 K 和 J。

## Weaknesses

### Must-Fix

**W1. [共识] CausalForest 偏差传播缺乏形式化论证（R1-M1, R2-N1 均 AGREE）。**
Theorem 1 刻画的是混淆矩阵校正层的偏差——子群级结果矩。论文声称该恒等式"传递"到 CausalForest CATE 估计，但 CausalForest 使用自适应分裂、诚实分裂和 bootstrap 聚合，使偏差传播关系非线性。经验 R²>0.97（Table 1）表明传播在实践中成立，但"经验验证" ≠ "理论保证"。

同时，论文与 Frazis & Loewenstein (2003) 的理论距离界定不够精确——两位 Reviewer 从不同方向（R1: 向上推广能力, R2: 向下原创性）指向同一问题。

**所需修改**：(a) 将 Theorem 1 明确定位为"校正层恒等式"，与估计器级保证分开声明；(b) 将 "estimator-agnostic" 改为 "empirically verified for DIM, Stratified MLE, HB EC-HTE, CausalForest"；(c) 加 1-2 句 sketch argument 说明为何经验传播预期成立。

**W2. [共识] 诊断在真实 LLM 数据上接近随机（AUC=0.63）（R1-M2, R2-N2 均 AGREE）。**
Proposition 5 的诊断在合成数据上 AUC=0.86，但在真实 LLM 错误率分布上仅 0.63——接近随机猜测。两个叠加原因：
(a) 诊断对 τ_s≈0 的场景不敏感（小绝对偏差虽相对偏差大，但 binary classification 阈值不稳定）；
(b) 真实 LLM CM 高度非对称（GPT-4.1 TweetEval: FPR=0.38, FNR=0.04; Civil Comments GPT-4o: FPR=0.517, FNR=0.032），但 Proposition 5 在对称（FPR=FNR）下推导。

AUC=0.63 目前埋在 Appendix X (p.25)，严重削弱论文的第二核心贡献。

**所需修改**：(a) 在主文 Section 5.4 报告 AUC=0.63（非仅附录）；(b) 明确声明诊断的适用边界——对称 + |Δτ|>threshold；(c) 将诊断框架为具有明确操作包络的工具，而非通用解决方案。

### Should-Fix

**W3. [共识] (A3) 平衡 Z 假设放松讨论在主文中不足（R1-S1, R2-W2）。**
Appendix T 显示 P(Z=1)=0.1 时 R²≥0.976、coverage≥90%——证据令人信服。但主文仅一句话提及此放松。建议在 Section 3 增加 2-3 句总结 Appendix T 的定量结果。

**W4. [共识] Expert budget 与论文动机的张力需量化（R1-S4, R2-W1）。**
论文以 LLM 替代昂贵人工标注为动机，但 EC-HTE 需 n_expert≥25/subgroup。K=4→100 标签，K=8→250。对 N=5000 样本，这是 2-5% 标注预算（20-50× 成本节约）。此对比缺失。建议在 Section 4.1 或 Limitations 加简短成本-收益段落。

**W5. [共识] 无真实因果 ground truth 验证（R1-S2, R2 同意但降低严重性）。**
所有实验使用合成或半合成 DGP。真实数据分析（UC Berkeley 仇恨言论）产生空结果（"all corrected CIs contain zero"）。RCT+LLM 标注数据集稀缺是领域固有困难（两位 Reviewer 均承认），半合成策略是标准做法（cf. Wager & Athey 2018, PPI）。但 Limitations 应更显著讨论此限制及其对方法外部效度的影响。

**W6. [共识] 多假设联合违反缺控制实验（R1-S3, R2 同意但降低严重性）。**
论文分别测试各假设违反，但真实 LLM 部署中多个假设同时不成立。Appendix R 的 11 个真实 LLM CM 天然联合违反（聚合 R²=0.975），提供部分缓解。建议论文明确承认此 gap 并引用 Appendix R 证据。

### Minor

**W7. Figure 2 pipeline 图使用红绿配色，对色盲用户不友好。建议改用 blue+orange 或添加纹理。**

## Reviewer Consensus

| 问题 | R1 | R2 | 结论 |
|------|----|----|------|
| CausalForest 理论桥接 | M1 | N1 (AGREE) | 共识：须将 Theorem 1 限定为校正层恒等式 |
| 诊断 AUC=0.63 | M2 | N2 (AGREE) | 共识：非对称 CM 因果导致退化，须主文报告 |
| (A3) 放松讨论 | S1 | W2 (AGREE) | 共识：主文需 2-3 句补充 |
| Expert budget 量化 | S4 | W1 (AGREE) | 共识：需成本-收益对比 |
| 无真实因果验证 | S2 | AGREE (降级) | 共识：领域限制，不阻挡接收 |
| 联合假设测试 | S3 | AGREE (降级) | 共识：Appendix R 部分缓解 |

## Reviewer Divergence

| 问题 | R1 | R2 | 裁定 |
|------|----|----|------|
| DGP 简单性 (S5) | Should-Fix：二值效应修饰变量过简 | REBUT：K∈{2,4,8} 已测试，Corollary 6 推广，离散 Z 是 CM 方法固有需求 | **R2 反驳成立。** DGP 的离散子群结构与问题设定匹配。K=8 实验存在。剩余可扩展性问题由 W4（expert budget）覆盖。从 Should-Fix 降级为观察记录。 |

## Questions for Authors

**Q1.** 能否提供形式化论证（即使是 sketch）说明为何偏差恒等式的预测精度（R²>0.97）在 CausalForest 的自适应分割中得以保持？充分条件即可。

**Q2.** 诊断（Proposition 5）在合成数据上达到 AUC≥0.80 所需的最小 |Δτ| 是多少？这将有助于界定其操作包络。

**Q3.** K=4 且 n_expert=25/subgroup 时，MCMC 后验是否收敛（R̂<1.01），还是结果由 Dirichlet 先验主导？

**Q4.** 是否考虑过 Proposition 5 的非对称推广——使用 FPR 和 FNR 两个参数而非单一 π_s？即使是启发式版本也会显著提升实际诊断价值。

## Missing References

本轮未发现新的关键遗漏引用。此前轮次的遗漏引用问题（Northcutt et al. 2021, Tan et al. 2024, Gligoric et al. 2025, Knox et al. 2022）均已修复。

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 本轮未配置外部审稿。

## Visual Layout Check（非评分项）

**状态：已完成**（2026-05-24 14:01–14:06 UTC）

发现（3 warnings, 4 info）：

| 严重性 | 位置 | 发现 |
|--------|------|------|
| ⚠️ Warning | pp.1-2 | 连续 2 页纯文本（Introduction + Related Work），无 display item。审稿人前 2 分钟只看到文字。建议将 Figure 1 提前或在 Introduction 嵌入 motivating example 图。 |
| ⚠️ Warning | pp.4-6 | 连续 3 页无 figure/table（Sections 3-4 数学推导）。理论内容密集可部分豁免，但跨度较长。建议将 Figure 2（pipeline，当前 p.7）提前到 Section 3 开头。 |
| ⚠️ Warning | pp.1-8 | 正文仅 3 个 display items（2 figures + 1 table），低于实证论文通常的 5-8 个。~30 tables 在附录。建议提升 1-2 个关键附录图/表到正文。 |
| ℹ️ Info | p.7 | Figure 2 红绿配色，对色盲不友好。 |
| ℹ️ Info | p.8 | Table 1 承载全部正文实验结果。可补充可视化图辅助。 |
| ℹ️ Info | p.15 | 附录单页 4 个 display items，视觉拥挤。 |
| ℹ️ Info | p.32 | 末页填充约 55%。 |

## Overall Assessment

**评分：3.5 — Borderline Conference**

**置信度：4/5**

**评分理由：**

本文解决了一个真实且及时的问题——LLM 标注偏差对异质处理效应估计的影响。核心贡献中，偏差恒等式（Theorem 1）数学上干净且验证充分，EC-HTE 校正方法实际有效（7.4× 偏差缩减，≥93% 覆盖率）。实验覆盖在该领域中属最全面之列。

两个问题阻止论文获得明确的 Conference 接收：

1. **诊断（Proposition 5）作为核心贡献之一，在真实 LLM 数据上接近随机（AUC=0.63）。** 论文以三级结果（1.0/0.86/0.63）呈现，但在目标部署场景中该工具不可靠。需主文显著披露并诚实界定适用范围。

2. **理论贡献边界不精确。** "Estimator-agnostic" 声明和 CausalForest 传播经验上强但形式上未证明。与 Frazis & Loewenstein (2003) 的新颖性需更尖锐的界定。

两个问题均可通过 framing 调整和 1-2 个额外形式化论证修复——不需要新实验。如果作者执行推荐的修改（明确限定 Theorem 1 范围、主文报告 AUC=0.63、补充成本-收益分析、添加 2-3 句形式化限定），论文可提升至 Conference 水平。

偏差恒等式本身是扎实的贡献，EC-HTE 方法填补了实际空白。执行质量高。本稿与接收之间的差距主要在于声明的精确性，而非贡献的实质。

## Detailed Comments

### Abstract (p.1)
三级 AUC 报告结构（1.0/0.86/0.63）清晰。14.9% 符号反转已正确限定在 τ(0)=0.03 条件下。无新问题。

### Introduction (pp.1-2)
动机清晰，"when debiasing hurts" 框架引人。但贡献列表中的 "estimator-agnostic" 声明应加限定。代码发布承诺已注明。

### Related Work (p.3)
经多轮修复，覆盖面全面（F-L, PPI, DSL, Blette et al., Northcutt et al., Knox et al., Gligoric et al., Tan et al.）。与 F-L 的区分可再尖锐 1-2 句——具体说明代数差异。

### Theory — Section 3 (pp.3-5)
Theorem 1 干净，乘积分解有洞察力。(A3) 放松需在此处补充 2-3 句（当前仅 "we discuss relaxation below"）。(A1)-(A5) 框架已正确枚举。

### Method — Section 4 (pp.5-7)
EC-HTE 算法呈现清晰。Section 4.3（CausalForest 集成）需形式化桥接论证或显式限定。κ≤1.25 筛选阈值已提及；建议在此简要说明理由而非仅在附录。

### Experiments — Section 5 (pp.7-8)
Table 1 密集但信息量大。7.4× 偏差缩减、coverage≥93%、符号反转消除均令人信服。Section 5.4 诊断评估应显著纳入 AUC=0.63 真实 LLM 结果（当前在 Appendix X）。引用 Table 22 筛选结果的句子良好但应扩展。

### Conclusion (p.8)
适当简短。未检测到过度声明。

### Limitations (p.8)
覆盖关键限制。应补充：(1) 诊断操作包络（对称 + |Δτ|>threshold）；(2) expert budget 成本-收益量化；(3) 缺乏 ground-truth CATE 验证作为显式限制（非仅暗示）。