---
round: 1
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-23T06:33:21.878954+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels

**Venue**: EMNLP 2026 via ARR May 2026 cycle
**审稿模式**: Fresh（初审）
**Reviewer 编排**: 2 人（R1 方法严谨性 / R2 新颖性与完整性）
**轮次**: Round 1（1 轮初审 + 交叉分享后收敛，无需第二轮）

---

## Summary

论文研究 LLM 多评委面板中 panel size 如何调节对抗攻击脆弱性的主导因素。通过 15 个模型（9 API + 6 本地量化）、6 种攻击、2 个基准、3 种面板大小（K∈{3,5,7}）的全排列实验，发现 K=3 时个体脆弱性（η_max）主导，K≥5 时多样性指标（K_eff）成为主要预测因子，且 K_eff 系数为正（diversity 与更高 vulnerability 相关联）。GAM 分析揭示该聚合效应掩盖了攻击类型依赖的方向分裂：targeted attacks 下 diversity 有害，shared-bias attacks 下 diversity 保护。Bayesian calibration 可逆转 K_eff 方向。

---

## Strengths

1. **研究问题有价值**：挑战 "diversity = robustness" 的 conventional wisdom，如果结论成立将对 LLM evaluation 实践产生广泛影响。[R1+R2 共识]

2. **实验规模大且系统**：15 models × 6 attacks × 2 benchmarks × 3 K values 的全排列设计（455–6,435 panels），覆盖所有可能的面板组合。[R1+R2 共识]

3. **多层 robustness checks**：4 种非独立性校正方法（OLS / Clustered SE / Mixed Effects / Wild Cluster Bootstrap）、ε 敏感性分析、random-vs-adaptive fault contrast，体现了良好的统计严谨性意识。[R1]

4. **Attack-type taxonomy 有独立价值**：GAM 揭示的 targeted vs. shared-bias 6:6 方向分裂比简单 "diversity is harmful" 更有信息量，即使主要因果声明受混淆威胁，这一分类仍有贡献。[R1+R2 共识]

5. **Aggregation analysis 提供 actionable insight**：Bayesian calibration 逆转 K_eff 方向的发现暗示可操作的防御策略。[R1+R2 共识]

6. **统计诚实度高**：坦承 OLS 膨胀、informative null、diversity-capability confound（Appendix C.2），尽管正文措辞未完全反映这些 caveats。[R2]

7. **可复现性好**：种子固定（42）、超参全报告、代码开源承诺。API 模型快照日期已标注。[R1+R2 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [R1-N2 + R2-N1, 共识] **K_eff 与 η_max 的 r=0.70 结构性混淆使 "diversity is harmful" 因果声明不可靠**

这是两位 Reviewer 一致认定的最核心问题。K_eff 与 η_max 的 Pearson 相关 r=0.70，控制 η_max 后 K_eff 的 partial r 仅 0.12（unique variance 1.4%），而 η_max 控制 K_eff 后 partial r 为 0.31。15 模型中 6 个本地模型全部 AWQ INT4 量化（clean accuracy 0.253–0.543），远低于 API 模型（0.767–0.968）。高 K_eff 的 panel 几乎必然包含跨 tier 的弱模型，因此 K_eff 的正系数可能仅反映 "panel 包含弱模型" 而非 "independence 本身有害"。

论文在 Appendix C.2 坦承 "observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it"，但 Abstract 仍以因果语言断言 "diversity increases vulnerability because independent judges can be targeted individually"，Introduction 说 "diversity is harmful in both regimes"，Conclusion 重复此 claim。正文与 Appendix 的 caveat 之间存在严重不一致。

此外，论文报告 VIF 平均 3.0，但 raw r=0.70 计算 VIF 应为 ~1.96，说明 log 空间中的相关性更高（~r=0.82），混淆比正文声称的更严重。应报告 log 空间的 r 值。

**需要**：(1) 全文因果措辞降级为相关性；(2) 仅用 9 个 API 模型构建 panels（C(9,3)=84）检查 K_eff 效应是否保持——这是区分 diversity 效应和 capability 效应的最直接方法；(3) 加入 panel 平均 clean accuracy 和 local model 数量作为控制变量。

**MF-2** [R2-N2 + R1 agree] **"Diversity is harmful" 在 abstract/conclusion 中被过度概括**

Abstract 后半段虽然提到 GAM 的攻击类型分裂，但开头和 Conclusion 的措辞是无条件的 "diversity increases vulnerability"。实际上：(a) GAM 揭示 6:6 方向分裂——targeted attacks 下 diversity 有害，shared-bias attacks 下 diversity 保护；(b) Bayesian calibration 将 K_eff 方向从 7+/1− 翻转为 1+/6−。一个方向可被攻击类型和聚合规则两个维度独立翻转的效应不应被称为 "harmful"。

**需要**：重新框架为 "diversity's effect is attack-mechanism-dependent and aggregation-rule-dependent"，并在 Abstract、Contribution 1、Conclusion 中反映此 nuance。

**MF-3** [R1-N1 + R2 agree] **Log-log OLS 在 bounded [0,1] ASR 数据上的适用性**

ASR ∈ [0,1] 是 bounded fractional response variable。log(ASR + ε) 的 OLS 回归存在问题：(a) ASR=0 时 log(10⁻⁶) ≈ −13.8 创造高杠杆点；(b) bounded variable 的 log 变换下残差分布违反 OLS 假设。标准替代方案是 beta regression（Ferrari & Cribari-Neto 2004）或 fractional logit（Papke & Wooldridge 1996）。ε 敏感性分析只说明对 ε 值不敏感，未解决根本问题。R2 认为可降级为 should-fix（因已有 bootstrap 作为 distribution-free 校正），但同意应做替代 specification 的 robustness check。

**需要**：至少用 beta regression 或 fractional logit 重跑全部 12 conditions × 3 K values 作为 robustness check。

### Should-Fix（影响评分但不一票否决）

**SF-1** [R2-N3 + R1 agree with nuance] **Analysis section 仅 1 段（4 句话），分析深度严重不足**

5 个 Results subsection、3 个 contribution、6 个 appendix section 的论文，Analysis（Section 6）仅 1 段。R1 指出分析内容并非缺失而是散落在 Appendix C.1–C.4 和 Results 各 subsection 中，但正文未整合。缺少：(1) regime transition 的深入理论分析（超越 "majority-threshold arithmetic" 的一句话解释）；(2) K_eff-η_max 混淆的正文讨论（目前仅在 Appendix C.2）；(3) 实际部署指导。考虑 8 页限制，建议扩展至 0.5 页。

**SF-2** [R1-N3, R2 部分 rebut] **仅三个离散 K 值支撑 "regime transition" 的术语**

K ∈ {3, 5, 7} 三个点不足以确立 transition 是连续还是阶跃，K* 精确位置未知。R2 反驳称 K=3→K=5 的翻转幅度极大（η_max 5/12→0/12，K_eff 1/12→7/12），三点数据足以支撑核心发现，但同意术语可以更精确。**建议**将 "regime transition" 改为 "K-dependent dominance shift" 或 "regime change between K=3 and K≥5"。

**SF-3** [R1-W1 + R2 agree] **Theorem 1 实证覆盖率仅 58%**

仅 61/105 judge pairs 满足 pointwise dominance 条件。42% 存在 vulnerability 交叉，theorem 的 monotonicity 保证不成立。论文将 Theorem 用于预测 β₂ > 0，但近半数不满足条件削弱了预测力。应讨论不满足条件的 42% pairs 的特征（哪些攻击导致 violation）。

**SF-4** [R1-W2 + R2 agree] **Clean-data K_eff 预测 attacked ASR 的假设未验证**

K_eff 从 clean data MI 计算，用于预测 attacked conditions 下的 ASR，隐含假设 inter-judge correlation 在攻击前后不变。Shared-bias attacks 可能增大相关性，targeted attacks 可能降低相关性。建议在 attacked conditions 下重新计算 K_eff 对比，或至少讨论此假设的局限性。

**SF-5** [R1-W3 + R2-W3 共识] **6 个 AWQ INT4 模型创造二元 capability 结构**

6 个本地模型全部 INT4 量化，与 9 个 API 模型形成二元结构。论文提到排除 accuracy < 0.5 的 sensitivity check 但仅报告 η_max 稳定性，**未报告 K_eff 在排除弱 judges 后的变化**。这是 make-or-break 的验证——必须报告。

**SF-6** [R1-W4 + R2 agree] **Wild cluster bootstrap 13 clusters per position 可能过度保守**

经典 rule of thumb ≥ 50 clusters（Cameron et al. 2008）。13 clusters + max-p 聚合极为保守，可能解释 K_eff 从 OLS 8/12 暴降到 bootstrap 0–1/12。但 R2 指出这是双刃剑：K≥5 下 K_eff 7/12 在极端保守条件下存活更有说服力。应讨论 cluster 数量的影响。

**SF-7** [R1-W5 + R2 agree] **Oracle adversary 过强，实际适用性有限**

全知 adversary 在 LLM judge 部署中不现实。Appendix C.4 的 partial-information 实验仅 leave-one-out，仍假设攻击者知道大部分 panel 信息。应增加 black-box adversary 实验（攻击者不知 panel 组成）或在 Discussion 中更明确限定结论适用范围。

**SF-8** [R2-W1 + R1 agree] **Abstract 数字密集（12+ 统计量）**

核心 message 被数字淹没，建议保留 2–3 个关键数字，其余移至 Results。

**SF-9** [R2-W2 + R1 agree] **Conclusion 过于简短（5 句话）**

近乎重复 abstract 数字，缺少 implications（LLM evaluation 实践指导）和 future work（如 causal identification via training-based diversity control）。

**SF-10** [R2-W4 + R1 agree] **遗漏重要相关工作**

- Shi et al. (2024), "Is LLM-as-a-Judge Robust?" (arXiv:2402.14016) — 直接相关
- Correlated-voter CJT 现代文献（Ladha 1992; Kaniovski & Zaigraev 2011）— CJT 段落仅引原始 Condorcet 1785
- CAP (Comparative Augmented Prompting) — LLM judge 鲁棒性方法

### Minor（不影响接收）

- gemini-3.5-flash ARC=1.00 但 26.3% format error rate，应说明 format errors 如何处理（影响 η_j 计算）
- Threshold voting R²=0.89 可能接近 tautological（unanimity 下 ASR ≈ f(η_max)），需解释
- K_eff 定义（Eq.1 用 MI）与实际计算（Gaussian copula ρ closed form）的等价性依赖 Gaussian assumption，应在定义时说明
- MI 估计稳定性：300 items × 3 categories，tie 频率低时 MI 估计可能不稳定，建议报告 MI 分布或 standard errors
- "Code and Data Availability" 作为 Limitations 的 paragraph 出现，建议分离
- Figure 1 框架图位于第 5 页，前 3 页无任何 display item（视觉审查建议前移）
- Figure 2 y 轴 count data（0-12 整数）建议标注具体数值
- Appendix A Theorem 1 证明仅考虑替换最后一个 position，应明确 wlog 说明

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上完全一致 [AGREE]：

1. **r=0.70 diversity-capability 混淆是最核心问题**，使 "diversity is harmful" 因果声明不可靠（R1-N2 = R2-N1）
2. **"Diversity is harmful" 需要根本性重新表述**，考虑 GAM 6:6 split 和 Bayesian reversal（R2-N2, R1 agree）
3. **Log-log OLS 需要替代 specification robustness check**（R1-N1, R2 agree）
4. **Analysis section 需要扩展**（R2-N3, R1 agree with nuance）
5. **AWQ INT4 模型子集分析是必要的 robustness check**（R1-W3 = R2-W3）
6. **Clean-data K_eff 预测 attacked ASR 的假设需验证**（R1-W2, R2 agree）
7. **Abstract 数字过密、Conclusion 过短**（R2-W1/W2, R1 agree）
8. **遗漏 Shi et al. 2024 等相关工作**（R2-W4, R1 agree）

## Reviewer Divergence

唯一分歧点：

- **R1-N3（三个 K 值是否足以支撑 "regime transition"）**：R1 列为 must-fix（需增加 K=4），R2 部分反驳——认为 K=3→K=5 的翻转幅度（η_max 5/12→0/12，K_eff 1/12→7/12）足以支撑核心发现，但同意术语应从 "regime transition" 调整为 "K-dependent dominance shift"。**Director 判定**：降级为 should-fix，通过术语调整解决。三个数据点确实不足以精确定位 transition threshold，但核心翻转模式已充分确立。

---

## Questions to Authors

1. 仅使用 9 个 API 模型（移除所有 INT4 quantized local models）构建 panels 后，K_eff 的正系数和 regime transition 是否仍然成立？
2. 在 attacked conditions 下重新计算 inter-judge MI，K_eff 与 clean data K_eff 的相关性如何？差异是否影响回归结论？
3. 排除 clean accuracy < 0.5 的 judges 后，K_eff 的显著性和方向如何变化？（论文提到做了此 check 但仅报告 η_max 结果）
4. Beta regression / fractional logit 的结果是否与 log-log OLS 一致？
5. 为什么不将 Appendix C.2 关于 observational regression 因果局限性的讨论纳入正文？

---

## Missing References

- Papke, L.E. & Wooldridge, J.M. (1996). Econometric methods for fractional response variables. *Journal of Applied Econometrics*. [R1]
- Ferrari, S. & Cribari-Neto, F. (2004). Beta regression for modelling rates and proportions. *Journal of Applied Statistics*. [R1]
- Cameron, A.C., Gelbach, J.B. & Miller, D.L. (2008). Bootstrap-based improvements for inference with clustered errors. *Review of Economics and Statistics*. [R1]
- Shi, W., et al. (2024). Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment. arXiv:2402.14016. [R2]
- Ladha, K.K. (1992). The Condorcet jury theorem, free speech, and correlated votes. *American Journal of Political Science*. [R2]
- Kaniovski, S. & Zaigraev, A. (2011). Optimal jury design for homogeneous juries with correlated votes. *Theory and Decision*. [R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~3 分钟）。0 critical / 3 warning / 8 info。

**Warning 发现**：
1. **前 3 页无任何 display item**（figure/table）：审稿人需翻到第 4 页才见 Table 1、第 5 页才见 Figure 1。框架图（Figure 1）是最佳视觉锚点，建议前移至第 1-2 页。
2. **连续 2 页纯文本**（Introduction），视觉节奏单调。
3. **第 7 页承载 3 个 display items**（Figure 2 + Figure 3 + Table 4），页面拥挤，bar chart 尺寸偏小。

**Info 发现**：Table 1 作为第一个 display item 仅提供配置信息不传达核心发现（锚点偏弱）；Figure 1 设计清晰但位置偏后；Tables 2-3 booktabs 规范；Figure 2-3 色彩区分度尚可但建议验证色盲友好性；参考文献无未解析引用。

---

## Overall Assessment

**评分：3.0 — Findings**（可被 Findings 接收）

**置信度**：4/5（两位 Reviewer 均具备统计方法和 ensemble robustness 领域知识，核心判断一致）

**理由**：

论文研究问题有价值（挑战 diversity = security 直觉）、实验规模可观（15 模型全排列 × 3 K 值）、统计 robustness 意识良好（4 种校正方法）。Attack-type taxonomy（targeted vs. shared-bias 6:6 split）和 aggregation analysis（Bayesian reversal）具有独立贡献价值。

但三个根本性问题阻碍主会议接收：
1. **因果推断不可靠**：r=0.70 的 diversity-capability 混淆下，K_eff 的 partial r 仅 0.12，"diversity is harmful" 无法与 "including weak models is harmful" 区分。正文因果措辞与 Appendix caveat 不一致。
2. **核心 claim 过度概括**：方向可被攻击类型（6:6 split）和聚合规则（Bayesian reversal）独立翻转的效应不应被无条件称为 "harmful"。
3. **统计框架选择不当**：bounded [0,1] ASR 使用 log-log OLS 而非 beta regression / fractional logit，缺乏替代 specification 的 robustness check。

如果 (1) 因果措辞降级为相关性、(2) 核心 claim 重新框架为 attack-type-dependent、(3) beta regression robustness check 确认结论稳健、(4) API-only 子集分析支持 K_eff 独立效应，则论文可达到 3.5（Borderline Conference）或更高。

---

## Detailed Comments

### Section 1 (Introduction)
- Contribution 1 "Diversity coefficient positive in both regimes" 忽略 GAM 层面的方向逆转，需加限定
- "diversity is harmful in both regimes" 措辞需改为 "K_eff is positively associated with vulnerability in both regimes at the aggregate level"
- 建议在 contributions 中增加对 attack-type taxonomy 的突出程度（目前作为 Contribution 3 的子项）

### Section 3 (Threat Model)
- Theorem 1 的 58% 覆盖率应在正文讨论（目前仅出现在定理陈述中），分析不满足条件的 42% pairs 特征
- Oracle adversary 定义后应更明确讨论其与实际 LLM judge 部署的距离
- K_eff 定义（Eq.1）基于 MI，但 §4.3 实际通过 Gaussian copula ρ 计算 closed form，等价性依赖 Gaussian assumption——应在定义时注明

### Section 4 (Methodology)
- §4.3: K_eff 在 clean data 上计算但用于预测 attacked ASR，隐含假设需明确讨论
- §4.5: Equation 2 的 ε=10⁻⁶ 需在方程内或紧邻处标注
- §4.6: 13 clusters per position 的 few-cluster 问题应讨论，引用 Cameron et al. (2008)

### Section 5 (Results)
- Table 1: gemini-3.5-flash ARC=1.00 + 26.3% format error rate 的处理方式需澄清
- Table 3: 应讨论 bootstrap 的保守程度——K_eff 0/12 可能部分是 methodological artifact
- §5.1: 排除 accuracy < 0.5 judges 的 sensitivity check 必须同时报告 K_eff 结果
- §5.5: Threshold voting R²=0.89 的 near-tautological 性质需讨论

### Section 6 (Analysis)
- 需大幅扩展：整合 Appendix C.2 的 confound 讨论、regime transition 的理论深度、部署指导
- Partial r 数据（K_eff: 0.12, η_max: 0.31）应在正文突出讨论

### Section 7 (Conclusion)
- 需扩展：加入 practical implications 和 future work
- "Diversity is harmful in both regimes" 需加限定词

### Limitations
- 覆盖面合理（non-independence、MCQ format、K* precision），但应增加 diversity-capability confound 作为主要 limitation
- "Code and Data Availability" paragraph 建议从 Limitations 分离

### Formatting
- Figure 1 建议前移至 page 1-2 以改善视觉锚定
- 第 7 页 display items 过于集中，考虑重新分布