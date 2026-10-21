---
round: 21
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-24T23:15:14.592622+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 21 审稿报告（含交叉回应）

**论文**: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"
**Venue**: EMNLP 2026 via ARR (May cycle)
**Deadline**: 2026-05-25
**Reviewer 编排**: R1（方法严谨性 + 实验完备性）、R2（新颖性 + 完整性 + NLP 社区适配）
**审稿模式**: Fresh（重新审稿）
**交叉回应**: R1↔R2 完成，共识已达成

---

## Summary

本文推导了一个精确偏差恒等式（Theorem 1），证明当 LLM 标注的误分类率在子群间异质时，标准全局混淆矩阵校正引入子群级偏差 δ_s·Δτ/(1−2π̄)，在 14.9% 的配置中反转 CATE 符号。论文提出 EC-HTE 方法（层次贝叶斯逐子群混淆矩阵估计 + 分层校正），在合成数据（520 配置）和半合成数据（16 个真实 LLM 混淆矩阵 × 4 NLP 任务）上验证，偏差缩减 7.4×（extreme heterogeneity）。另推导 Δτ-free 诊断准则（Proposition 5）和操作条件。

---

## Strengths

**S1. [共识] 问题提出新颖且重要。** "Global correction 可反转 CATE 符号"这一发现在 LLM 标注日益普及的背景下非常及时。Figure 1 三面板直观有效。（R1-S1, R2-S4）

**S2. [共识] 理论贡献干净且可验证。** Theorem 1 的乘积形式 δ_s × Δτ / (1−2π̄) 简洁可解释，合成数据 R² ≥ 0.97，11 个真实 LLM 混淆矩阵聚合 R² = 0.975。推导逻辑清晰（Appendix B）。（R1-S2, R2-S1）

**S3. [共识] 实验验证深度突出。** 33 页附录涵盖 A1-A5 每个假设的敏感性分析、class imbalance、先验敏感性、bootstrap SE、跨模型一致性（6 个 LLM）、PPCI 互补性、F-L 对比、CausalForest oracle coverage、confounded treatment 等。同领域罕见的全面性。（R1-S3, R2-S3）

**S4. [共识] Δτ-free 诊断有实用价值。** Proposition 5 仅需子群误差率即可判断是否应做逐子群校正，无需估计处理效应。R2 交叉回应澄清：诊断的核心价值在于"告诉你何时不应做 per-subgroup 校正"——当 Δπ < 0.15 或 K 过大时，直接运行 EC-HTE 反而有害（variance 增加），诊断作为前置筛选可避免不必要的全流程运行。（R2-S2, R2 对 R1-W3 的反驳）

**S5. [共识] 方法互补性设计好。** EC-HTE（covariate-side）与 PPCI（outcome-side）正交组合，bias 从 0.179 降至 0.007。（R2-S5）

**S6. [共识] 可复现性。** Algorithm 1 完整，匿名代码仓库已提供，MCMC 诊断达标（R̂ < 1.01, ESS > 843）。（R1-S4）

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [R1-N1, R2 AGREE] 非对称误分类下诊断准则退化——正文讨论严重不足**

Proposition 5 在对称假设 (A2) 下 AUC=0.86，但真实 LLM 几乎总是非对称（FPR/FNR 比率 1.1–7.1, Table 12）。非对称下 AUC 降至 0.65。

R2 在交叉回应中补充了重要 nuance：
- AUC=0.65 对筛选工具仍有实用价值（baseline 0.50 上 30% 相对提升）
- 假阳性成本较低（多做 per-subgroup 校正增加 variance 但不引入 bias），假阴性成本更高（遗漏有害 global correction）
- 论文在 Remark 2 已披露此退化，不存在隐瞒

**但核心判断两位 Reviewer 一致**：Proposition 5 被列为三大贡献之一，如果在现实条件下 AUC 仅 0.65，需要在正文中更显著地讨论这一限制，而不是仅在 Remark 2 末尾一句带过。

**建议**：Section 5.4 增加 1 段讨论非对称诊断性能退化；讨论矩阵形式诊断 vs 标量诊断的 trade-off（前者精度更高但输入需求更大）。

---

**MF2. [R2-N1, R1 部分 AGREE] NLP 社区适配性不足**

三个贡献全部属于测量误差理论/因果推断方法论。NLP 任务仅作测试平台，正文缺 NLP 特有洞察，真实数据实验在附录。

R1 在交叉回应中部分同意但认为严重程度不到 Must-Fix：Table 12-13 用 6 个真实 LLM 实证验证了子群异质性是 LLM 标注器的结构性属性（Spearman ρ = 0.82-1.00），这是 NLP-specific 发现。R2 Excitement 3/5，R1 Excitement 3.5/5——R1 认为问题本身对 NLP 社区足够重要。

**综合判断**：维持 Must-Fix——EMNLP AC 对 NLP 社区适配有明确期待，且修改方案清晰、成本低。

**建议**：(a) 将 Appendix M 仇恨言论案例关键结果移入正文；(b) 讨论误分类异质性的语言学来源；(c) 增加 "Implications for NLP Annotation Pipelines" 段落。

---

### 从 Must-Fix 降级为 Should-Fix（交叉回应后调整）

**SF-A. [R1-N2 初审 Must-Fix → 交叉后 Should-Fix] "Exact" 标题与标量近似 R² 退化的张力**

R2 在交叉回应中提供了有力澄清：
- 标题 "Exact Bias Identity" 技术上正确——Theorem 1 在 (A1)-(A5) 下是精确恒等式，矩阵形式放松 (A2) 后也精确
- R1 所引 R²=0.05-0.21 出现在 Δτ=0.05 配置下，此时偏差项本身极小（接近零），R² 低是因为信号极弱而非近似误差大——绝对偏差仍然很小
- Abstract 中 R²=0.975 across 11 real LLM CMs 已包含非对称效应，只是标量近似 vs 矩阵形式的区别应显式标注

**降级理由**：标题准确描述 Theorem 1 本身；Abstract 需加限定但不需改标题。

**建议**：Abstract 标注 "under the symmetric scalar approximation"；Section 3 更明确区分 "exact matrix identity" 和 "scalar approximation"。

---

**SF-B. [R2-N2 初审 Must-Fix → 交叉后 Should-Fix] 与 F-L (2003) 的差异化**

R1 在交叉回应中明确反驳：F-L 是全局标量衰减 β̂=(1−2ε)·β，无子群结构；Theorem 1 的 δ_s·Δτ/(1−2ε̄) 是三因子乘积分解，揭示 bias 方向可在子群间反转——F-L 结构中不存在此现象。实证对比：F-L per-subgroup Bias 0.112, coverage 65.3% vs EC-HTE Bias 0.004, coverage 97.8%（Appendix Z.5 Table 35）。

R2 未对此反驳做进一步 REBUT。

**降级理由**：R1 的反驳有实质依据——Theorem 1 与 F-L 的差异是结构性的（标量衰减 vs 子群乘积分解），novelty 成立。问题转为**展示清晰度**而非**novelty 本身**。

**建议**：将 Appendix Z.5 Table 35 关键数字移入正文 Section 3 或 Table 1 附近；在 Theorem 1 后增加 2-3 句 explicit novelty statement。

---

**SF-C. [R1-N3 初审 Must-Fix → 交叉后 Should-Fix] K ≤ 4 可扩展性限制**

R2 在交叉回应中提供了重要澄清：
- K 是子群数量而非类别数量——由实践者自行选择（如文本长度分位数、hashtag 有无），不等于 NLP 任务的类别数
- K=2-4 覆盖了社会科学因果推断中最常见的子群划分方式
- 真正的限制在于 expert budget（K=4 需 200 标签），在实践中成本合理

R1 未对此做进一步 REBUT。

**降级理由**：R2 澄清了 K 的语义——它是设计参数而非硬约束。限制已在 Section 5.4 和 Limitations 中披露。

**建议**：Introduction 增加 1 句明确 K 的含义和 K ≤ 4 建议；讨论 K 选择指导准则。

---

### Should-Fix（影响评分但不一票否决）

**SF1. [R1-W1 → R2 REBUT] HTE 估计器多样性**

R2 在交叉回应中反驳：论文实际测试了 3 种估计器（DIM + CausalForestDML + R-learner），覆盖参数、非参数、半参数三种范式。更关键的是，EC-HTE 的偏差校正发生在混淆矩阵反转阶段（Section 4.2），独立于下游 CATE 估计器。Theorem 1 也是 estimator-agnostic。R1 未对此做进一步 REBUT。

**综合判断**：R2 反驳有效——3 种估计器 + estimator-agnostic 校正对会议论文充分。降低优先级。

**SF2. [R1-W2, R2 AGREE] MC=100 覆盖率精度。** SE ≈ 2.2pp，Table 1 应报告 MC SE。两位 Reviewer 完全一致。

**SF3. [R2-W3, R1 AGREE] 正文缺完整真实数据实验。** 移 Appendix M 关键结果入正文。两位 Reviewer 一致。

**SF4. [R2-W2, R1 AGREE] 操作条件是经验导出。** 称 "decision framework" 应调整为 "empirically calibrated operating guidelines"。

**SF5. [R2-W4, R1 AGREE] 噪声标签学习文献关联可更深入。** subgroup-dependent vs instance-dependent noise 结构化联系未建立。

**SF6. [R1-W3 → R2 REBUT] Proposition 5 诊断增量价值。** R2 的反驳有说服力：诊断的核心功能是"不校正"决策（当 Δπ < 0.15 或 K 过大时阻止运行 EC-HTE） + 计算成本节省（一行代码 vs MCMC + CausalForest） + 可解释性。但论文当前未充分传达此定位。**建议**：Section 5.4 增加诊断作为"前置决策工具"的价值阐述。

**SF7. [R2-W5, R1 AGREE] Section 3 符号密度偏高。** 建议 Theorem 1 后增加 K=2 数值示例。

**SF8. [R1-W4, R2 AGREE] HB 先验结构性敏感性。** 仅 Gamma 超参变动，未考虑替代先验族。R2 补充：当前分析对会议论文基本达标。

**SF9. [R1-W5, R2 AGREE] A1 灵敏度参数化受限。** 仅 logistic link、γ ∈ [0, 0.20]。R2 补充：横向覆盖面充分（8 种假设违反类型），参数化是领域标准做法。

**SF10. [R2-W1, R1 AGREE] A3 (P(Z=0)=0.5) 正文讨论不足。** Appendix T 有测试但全在附录。

---

### Minor（不影响接收）

1. Abstract "7.4×" 应标注 Table 1 出处（Global 0.059 vs EC-HTE 0.008 = 7.375×）[R1, R2 AGREE]
2. Figure 3 panel 字号偏小（约正文 60-65%）[R2]
3. \citet / \citep 一致性需全文检查 [R2]
4. 33 页附录建议增加目录索引 [R1, R2 AGREE]
5. Page 33 Algorithm 1 仅占 40%，余 60% 空白 [视觉审查]
6. Table 1 "95% CI Cov." 列未标注 MC 样本量 [R1]
7. Appendix E 未讨论子群大小不均衡影响 [R1, R2 AGREE]
8. Page 8 过度拥挤（Figure 4 + Table 1 + Conclusion + Limitations 全挤一页）[视觉审查]

---

## Reviewer Consensus [AGREE]

交叉回应后两位 Reviewer 在以下关键问题上完全一致：

1. **Overall 3.5 (Borderline Conference)**
2. **Soundness 4/5** — Theorem 1 推导正确，实验设计严谨
3. **非对称诊断退化是核心弱点** — AUC 0.86→0.65，正文讨论不足（Must-Fix）
4. **NLP 社区适配需加强** — 真实数据和 NLP 洞察应进正文（R1 认为 Should-Fix，R2 认为 Must-Fix）
5. **MC=100 需报告 SE** [AGREE]
6. **操作条件应标为 empirical guidelines** [AGREE]
7. **Section 3 符号密度高，需数值示例** [AGREE]
8. **HB 先验和 A1 灵敏度可扩展** [AGREE]
9. **实验全面性是显著优势** [AGREE]
10. **格式合规**（Abstract ≤ 200 words, 正文 ≤ 8 页, 匿名性, ACL 模板）[AGREE]

---

## Reviewer Divergence（交叉后仍存在的分歧）

| 问题 | R1 | R2 | 交叉后共识 |
|------|----|----|-----------|
| NLP 适配严重性 | Should-Fix（Excitement 3.5） | Must-Fix（Excitement 3） | 维持 Must-Fix（EMNLP AC 明确期待 NLP 适配） |
| F-L 差异化 | R1 REBUT：结构性不同 | R2 未进一步反驳 | 降为 Should-Fix（展示问题而非 novelty 问题）|
| "Exact" 标题 | Must-Fix | Should-Fix（技术上正确） | 降为 Should-Fix |
| K ≤ 4 严重性 | Must-Fix | Should-Fix（K 是设计参数） | 降为 Should-Fix |
| HTE 估计器 | Should-Fix（缺 X-learner） | REBUT（3 种够了 + estimator-agnostic） | 降低优先级 |
| 诊断增量价值 | Should-Fix（标签需求相同） | REBUT（"不校正"决策功能） | 维持 Should-Fix（论文需更好阐述） |

---

## Questions for Authors

1. [R1-Q1, R2 补充] 矩阵形式诊断 vs 标量诊断的 trade-off 如何？在专家标签充足时，是否应推荐矩阵形式？
2. [R1-Q2] K=8, n_expert=1000（125 labels/subgroup）时 EC-HTE 能否恢复？
3. [R2-Q1, R1 REBUT 提供部分回答] Theorem 1 相对 F-L 的核心新增洞察：δ_s × Δτ 交互导致 sign reversal——这一点如何在正文中更显式传达？
4. [R2-Q3] 真实仇恨言论案例中子群定义的语言学依据？LLM 误差异质性的根本原因？
5. [R1-Q4, R2 补充] Real-data case study 中 EC-HTE 是否改变了 CATE 的方向性结论？R2 指出论文未明确报告是否存在 sign reversal——如仅改善 CI 宽度则 impact 减弱。
6. [R2-Q5] 子群划分函数 S 本身有噪声时对 Theorem 1 的影响？

---

## Missing References

1. **Wood-Doughty et al. (2018)** "Challenges of Using Text Classifiers for Causal Inference" — 最早系统讨论文本分类器用于因果推断的挑战，高度相关 [R1 AGREE, R2 提出]
2. **Veitch et al. (2020)** "Adapting Text Embeddings for Causal Inference" — text-as-confounder 与本文 text-as-effect-modifier 互补 [R1 AGREE, R2 提出]
3. **Kadavath et al. (2022)** "Language Models (Mostly) Know What They Know" — LLM 校准。R1 认为与本文正交，非核心缺失；R2 认为校准作为替代方案值得讨论 [分歧]

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 已完成（4 warning, 0 critical, 16 info）

主要发现：
- **[warning] Page 1-2**: 前两页纯文本，Figure 1 在第 3 页。建议考虑提前视觉锚点。
- **[warning] Page 4-5**: 连续两页密集数学无 display item。
- **[warning] Page 8**: 过度拥挤——Figure 4 + Table 1 + Section 5.3-5.4 + Conclusion + Limitations 全挤一页。
- **[warning] Page 33**: Algorithm 1 仅占 40%，余 60% 空白。
- **[info]** Figure 1 质量优秀，Figure 2 pipeline 对比是最佳视觉元素，Table 1 booktabs 规范。公式渲染无错误，正文 8 页合规。

---

## Overall Assessment

**评分**: 3.5 / 5 (Borderline Conference)

**EMNLP 2026 评分标准**: 3.5 = Borderline Conference

**置信度**: 4 / 5（交叉回应后提升——两位 Reviewer 独立评估高度一致）

**判断理由**:

论文在理论严谨性（Soundness 4/5）和实验全面性上达到 Conference 水平。Theorem 1 的乘积分解是一个干净、可验证的理论结果，与 F-L (2003) 的差异是结构性的（交叉回应中 R1 有效反驳了 R2 的 "形式相似" 判断）。"Debiasing hurts" 的发现对 LLM 标注日益普及的 NLP 社区有实际意义。

两个因素将总分从 Conference (4.0) 压至 Borderline (3.5)：

1. **非对称诊断退化**（Must-Fix）：Proposition 5 作为核心贡献之一，在现实 LLM 非对称条件下 AUC 仅 0.65，正文讨论不足。虽然 R2 指出 AUC=0.65 对筛选工具仍有价值，但论文需更显著地呈现此限制。

2. **NLP 社区适配**（Must-Fix）：核心贡献在统计方法论，NLP 任务仅为测试平台，正文缺 NLP 特有洞察和真实数据实验。R1 认为 Excitement 3.5（问题重要性足够），R2 认为 Excitement 3（受众窄）。

**升级路径 → 4.0 (Conference)**：
- Section 5.4 充分讨论非对称诊断退化 + 矩阵形式 trade-off
- Appendix M 真实数据移入正文 + NLP 标注管道影响讨论
- Theorem 1 后增加数值示例降低 Section 3 认知负担
- Table 1 报告 MC SE

**降级风险 → 3.0 (Findings)**：
- AC 认为 NLP 社区 excitement 不足

当前定位：一篇 solid 的 Findings paper；修改到位可达 Conference。升级所需改动量合理（正文内调整，无需新实验）。

---

## Detailed Comments

### Section 1 (Introduction)
- Contribution 2 措辞调整为 "empirically calibrated operating guidelines"
- 增加 1 句明确 K 的含义（子群数量而非类别数量）和 K ≤ 4 建议
- NLP motivation example（content moderation）有效，但后续 NLP 洞察未跟进

### Section 2 (Related Work)
- Noisy label learning 段落已添加但仅 3 句——建议建立 subgroup-dependent vs instance-dependent noise 联系
- 缺 Wood-Doughty 2018, Veitch 2020（text + causal inference 核心文献）
- F-L nesting statement 存在但不够显式——R1 建议将 Table 35 关键数字移入正文

### Section 3 (Theory)
- Theorem 1 推导正确，三因子分解优雅
- A2 "expository simplification" 标注和 Remark 2 是改进
- 建议 Theorem 1 后增加 K=2 数值示例（ε₁=0.05, ε₂=0.25）降低认知负担
- 更明确区分 "exact matrix identity"（Remark 2）和 "scalar approximation"（Eq. 2）
- Proposition 5: 正文讨论非对称 AUC 退化 + 阐述"不校正"决策的价值定位

### Section 4 (Method)
- HB 估计规格完整，<5ms 是优势
- κ-guard 设计合理
- 先验敏感性：当前 Gamma 超参变动对会议论文基本达标，替代先验族（logistic-normal）可作为 camera-ready 扩展

### Section 5 (Experiments)
- 合成验证（520 配置）全面
- 应包含至少一个真实 NLP 数据实验（移 Appendix M 关键发现入正文）
- Table 1 报告 MC SE
- 3 种 HTE 估计器（DIM + CausalForest + R-learner）覆盖三种范式，对会议论文充分（R2 交叉回应有效反驳了 R1 的 "缺 X-learner" 关切——校正与下游估计器无关）

### Section 6 (Conclusion)
- 3 句话含 adoption guideline，长度合理
- 可增加 1 句讨论非对称推广的未来方向

### Limitations
- 覆盖 3 个要点，长度合规
- 建议增加 A3 class imbalance 和 K 含义的显式提及

### Appendix
- 深度突出，是论文核心竞争力之一
- 建议增加目录索引
- Page 33 空白过多