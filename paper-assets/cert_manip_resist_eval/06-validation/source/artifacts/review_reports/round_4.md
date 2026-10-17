---
round: 4
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-24T10:54:01.977409+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: The Shifting Bottleneck: Panel-Size-Dependent Predictors of Adversarial Vulnerability in LLM Judge Panels
**Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**Reviewer 配置**: 2 人（R1: 方法严谨性+统计推断, R2: 新颖性+完整性+写作）
**交叉分享**: 完成，1 轮即收敛

---

## Summary

本文系统性地研究了 LLM 多 judge 评审 panel 在对抗性操纵下的脆弱性结构。作者定义了基于 pairwise mutual information 的 effective independence 指标 K_eff，与 weakest-link vulnerability η_max 一起作为 panel attack success rate (ASR) 的预测因子。通过 15 个模型、6 种攻击类型、2 个 benchmark、3 种 panel 大小 (K∈{3,5,7}) 和 4 种聚合规则的全因子实验，论文报告了一个 "predictor shift"：K=3 时两个预测因子共同贡献，K≥5 时 K_eff 成为主导预测器而 η_max 衰减。论文同时承认 diversity-capability confound (r=0.70–0.81) 在 69% 的条件下可完全解释 K_eff 的效应。

---

## Strengths

**S1. 研究问题的时效性和实用性** [R1, R2 共识]
LLM-as-a-judge panel 的对抗安全性是一个 timely 且 under-explored 的问题。Panel composition 如何影响 adversarial robustness 对实际部署有直接指导意义。

**S2. 实验规模和系统性** [R1, R2 共识]
15 模型 × 6 攻击 × 2 benchmark × 3 panel sizes × 4 聚合规则的全因子设计。Exhaustive panel enumeration（455→3,003→6,435 panels）避免了 sampling bias。实验矩阵覆盖面在同领域论文中罕见。

**S3. Robustness check 的广度** [R1, R2 共识]
OLS → clustered SE → mixed effects → wild cluster bootstrap → fractional logit → GAM → Cinelli-Hazlett sensitivity → dominance analysis → subsampling → cross-benchmark prediction 的校正层级远超同领域标准。论文没有 cherry-pick 最好的结果，对所有方法的 significance count 均做了完整报告。

**S4. 对 confound 的学术诚信** [R1, R2 共识]
将 Cinelli-Hazlett 69% 负面结果直接报告在 Abstract 中，diversity-capability confound 作为 "fundamental limitation" 在 Section 6 和 Limitations 首段讨论。这种透明度在同类论文中不常见。

**S5. K_eff vs κ-diversity 差异化** [R1 主导, R2 认可]
Table 14 和 Appendix Q 展示 predictor shift 是 K_eff 特有 (4→7→8) 而 κ-diversity 反而下降 (8→7→6)。这是一个有说服力的 metric differentiation 论证。

**S6. Random fault contrast 和 attacked K_eff stability** [R2 主导]
Random vs adaptive fault 的 R² 对比和 clean vs attacked K_eff 的 rank correlation（Table 8, Appendix H）提供了有效的 sanity check。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, R1-N1 首提, R2 AGREE] **K_eff 公式（Eq. 1）缺乏理论来源和验证**

K_eff = (1/K) Σ_i [1 + Σ_{j≠i} exp(−2·MI(i,j))] 是论文全部分析的核心自变量，但存在三层问题：

(a) exp(−2·MI) 中系数 2 仅在 bivariate Gaussian 下等价于 alienation coefficient (1−ρ²)，在 ordinal/categorical judge outputs 下无明确信息论解释。论文未提供在非 Gaussian 依赖结构下这个特定函数形式的理论动机。

(b) Section 3 声称 "Under the SDPI, η_joint ≤ min(1, K_eff · η_max)"，但既未证明此 bound 也未引用证明。SDPI 关于信息量在数据处理链中的衰减，不直接适用于 ensemble failure probability。Appendix A 仅包含 Theorem 1 的证明，非 SDPI bound。

(c) Section 4.3 提到 Gaussian copula assumption，但未做正式 GoF 检验。闭合形式 K_eff = K − (1/K)ΣΣρ²_{ij} 与 plug-in MI 估计器之间的数值差异未报告。

更深层的问题：Appendix Q 显示 κ-diversity 替代 K_eff 后 predictor shift 消失 (8→7→6)，暗示 shift 可能是 K_eff 构造方式的 artifact 而非 panel 结构的真实属性。

**MF2** [critical, R1-N3 + R2-N1 共识] **Diversity-capability confound (r=0.70–0.81) 根本性限制因果解释**

论文核心 claim——K_eff 与 ASR 正相关且在 K≥5 成为主导——无法与更平凡的解释区分：更 diverse 的 panel 倾向包含更弱的模型，弱模型更容易被攻击。

- Cinelli-Hazlett 分析：25/36 (69%) 条件下 K_eff 的 robustness value 不超过已知 η_max confound（Table 9）。RV 分布极度异质（0.005–0.522），最低 RV=0.005 意味着极微弱 confounder 即可消除效应。
- Pool A subsampling (r=0.50, 126 panels at K=5)：RV 改善到 10/12，但 (a) 仅占 full pool 4.2%，(b) MDE 未报告，(c) r=0.50 仍是 medium-to-large correlation。
- API-only 9 模型（Appendix F, Table 7）：predictor shift 不 replicate（K_eff 仅 3/12 significant），强烈暗示 full pool 的 shift 主要由 AWQ 量化模型引入的 capability variance 驱动。

论文对此的透明度值得肯定，但透明性不等于解决。当前 framing（title "Shifting Bottleneck"、abstract "uniformly positively associated"）显著强于实际证据。

**MF3** [critical, R1-N2 首提, R2 部分 AGREE] **少 cluster 下 wild bootstrap 不可靠，predictor shift 可能部分是 power artifact**

- K=3: 13 clusters, K=5: ≤11, K=7: ≤9——均低于 Cameron et al. (2008) 推荐的 ≥20。
- MDE 从 K=3 的 0.144 降至 K=5 的 0.048、K=7 的 0.036（Table 12）。Significance count 增长 (4→7→8) 至少部分反映 power 增长（3,003 vs 455 panels），而非真实效应结构变化。
- 论文引用 MacKinnon & Webb (2018) 为 Rademacher weights 辩护，但该文结论是 <10 clusters 时 rejection rate 仍显著偏离 nominal level。
- 跨 K 比较中 cluster 数反向变化（13→≤9）使 bootstrap p-value 的跨 K 可比性存疑。

R2 nuance：Fractional logit 不依赖 cluster bootstrap，其 9/12→11/12→12/12 模式也显示 shift，部分缓解纯 bootstrap artifact 的担忧。但 fractional logit 使用 robust SE 而非 cluster bootstrap，可能低估 panel composition 的非独立性。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, R2-N2 首提, R1 REBUT 降级] **Benchmark scope 仅限 multiple-choice**

仅用 MMLU 和 ARC（both multiple-choice format）。LLM-as-a-judge 主要应用是 open-ended generation evaluation，评分空间、攻击面、聚合方式均不同。标题 "LLM Judge Panels" 暗示普遍适用性。

R1 REBUT：论文的统计框架不依赖 benchmark 类型；cross-benchmark prediction (Appendix J) 提供部分泛化证据。但 R1 同意标题应加 scope qualifier。

**SF2** [warning, R1-W1 首提, R2 AGREE] **log(ASR + ε) 规范不稳定，应以 fractional logit 为主**

ARC K=7 零值率 38-40%，log(10⁻⁶) ≈ −13.8 产生极大 leverage。K=3 时三个条件 K_eff 符号变化取决于 ε 选择。Fractional logit 已有且结果更强 (9/12, 11/12, 12/12)——提升为 primary specification 是方法论和结果的双赢。

**SF3** [warning, R1-W2 首提, R2 AGREE] **Tier 分类偏斜和 AWQ confound**

15 模型中 9 个 lightweight（6 个因 INT4 量化降级，非固有能力）。Table 1 caption 已说明但未充分讨论。API-only 分析显示 predictor shift 不 replicate——这应在正文而非仅 Appendix 中讨论。

**SF4** [warning, R1-W3 首提, R2 AGREE] **"uniformly positive" 表述误导**

Abstract/正文反复使用 "uniformly positively associated"。但 clustered SE 下 0/12 显著，bootstrap 4/12。Coefficient direction uniformly positive ≠ uniformly significant。应报告跨方法 effect size 和 CI，加 qualifier 明确 direction vs significance 区分。

**SF5** [warning, R2-W1 首提, R1 AGREE] **标题 "Shifting Bottleneck" 暗示过强**

K* ∈ (3, 5) 仅有一个间隔点（K=3→5），两个数据点声称 "shift" 统计上不严格。建议改为更 hedged 的标题。

**SF6** [warning, R2-W2 首提, R1 AGREE] **聚合规则分析表面化**

Threshold R²=0.829 vs Bayesian R²=0.087 是 ~10x 差异，但仅一段讨论。更关键的是 Bayesian calibration 在 K=5 恢复 (7/12) 但 K=7 又回到 0/12 的非单调行为未解释。这可能是论文最 actionable 的发现，却被边缘化。

**SF7** [warning, R1-N3 + R2-W4 共识] **因果语言局部泄漏**

整体把控改善（vs Round 3），但残留：Abstract "must match"、Introduction "diversity's role"、Conclusion "manage independence"。需系统性全文扫描替换。

**SF8** [warning, R1-W5 首提, R2 AGREE] **Mixed effects 模型应使用 crossed random effects**

当前对 3 个 judge position 分别拟合 random intercept model 取 max p-value。应使用 crossed random effects (judge × position)——现有方法过度保守但不等同于正确建模。

**SF9** [warning, R2-W3 首提] **缺少相关工作：CollabEval (2026)、DBEI 正文对比**

DBEI (Kuai et al., 2026) 是 K_eff 的直接竞争指标，应在正文做 head-to-head 对比（当前仅 Appendix Q）。CollabEval 的三阶段 multi-agent evaluation 与聚合规则分析相关。

---

## Reviewer Consensus [AGREE]

1. **Confound 是 fundamental limitation**：diversity-capability 共线性 (r=0.70-0.81) 使因果推断不成立，69% 条件下 Cinelli-Hazlett RV 不超过已知 confound。论文的透明度值得肯定，但 framing 仍 overclaim。[R1-N3 + R2-N1, 双方 AGREE]

2. **K_eff 理论基础有缺口**：SDPI bound 未证明，exp(-2·MI) 系数无理论动机，Gaussian copula 未检验。κ-diversity 替代后 predictor shift 消失暗示 shift 可能是构造 artifact。[R1-N1, R2 AGREE]

3. **"Uniformly positive" 表述需加 qualifier**：direction (12/12) vs significance (0-12/12 method-dependent) 的区分必须在 abstract 中明确。[R1-W3, R2 AGREE]

4. **Fractional logit 应为主要规范**：log(ASR+ε) 对零值不稳定，fractional logit 方法论更正确且结果更强。[R1-W1, R2 AGREE]

5. **标题和因果语言需 hedge**：title "Shifting Bottleneck" 过于 assertive，abstract/conclusion 中因果暗示需系统清理。[R2-W1 + R2-W4, R1 AGREE]

6. **聚合分析是被忽视的亮点**：Bayesian calibration 的 R² 近 10x 衰减和 K-dependent 非单调行为值得深入分析。[R2-W2, R1 AGREE]

7. **AWQ/tier confound**：API-only 分析显示 predictor shift 不 replicate，应在正文讨论。[R1-W2, R2 AGREE]

---

## Reviewer Divergence [REBUT]

1. **Benchmark scope 严重程度**
   - R2 (Must-Fix): multiple-choice only 无法支撑标题泛化性，需增加 open-ended benchmark
   - R1 (Should-Fix): 统计框架不依赖 benchmark，cross-benchmark prediction 提供部分泛化证据，标题加 scope qualifier 即可
   - **Director 判定**: Should-Fix。R1 论证有说服力——框架的方法论贡献独立于 benchmark 选择。但标题必须加 scope qualifier。

2. **攻击模板数量**
   - R2 (Must-Fix): 每种 1-2 variants，结论可能与 wording 绑定
   - R1 (Should-Fix): K_eff 是 panel composition 函数，独立于 attack template；跨 6 种不同机制的一致性比 within-attack 变体更有说服力
   - **Director 判定**: Should-Fix。R1 的论证合理——template 影响 η_max 估计但不影响 K_eff。但 Appendix H 中 position bias ρ=0.08 说明某些攻击确实改变 inter-judge dependence。

3. **Human evaluation baseline**
   - R2 (Should-Fix): 需要 human panel 作为参照
   - R1 (REBUT): 论文研究 LLM-specific adversarial vulnerability，human judges 不会被程序化攻击以相同方式 fool
   - **Director 判定**: 不纳入。R1 论证合理——research question 是 LLM-specific 的。

4. **Theorem 1 贡献**
   - R2 (Should-Fix): majority voting 下近乎 tautological
   - R1 (REBUT): 在 adaptive adversary + 任意 correlation structure 下 non-trivial；stochastic dominance 仅 58% pairs 成立，前提条件非 trivially satisfied
   - **Director 判定**: 不纳入为独立 issue，但论文应降低 Theorem 1 的 framing 强度——定位为 formalization 而非 novel insight。

5. **Dominance analysis under collinearity**
   - R1 (Should-Fix): co-dominance 可能是 identification failure
   - R2 (REBUT): VIF 2.0-2.9 不极端，dominance analysis 不是唯一证据
   - **Director 判定**: 不升级。R2 论证合理——dominance analysis 是辅助证据，非核心依赖。

---

## Questions

Q1. K_eff 的 SDPI bound（η_joint ≤ K_eff · η_max）是否有严格证明？如果是 conjecture/heuristic，请明确标注。[R1]

Q2. 在 K=7（≤9 clusters）下，wild cluster bootstrap 的 nominal size 是否经过校准？能否报告 null hypothesis 下的 empirical rejection rate？[R1]

Q3. API-only 9 模型（Table 7）显示 predictor shift 不 replicate 且 r=0.85 时 K_eff 仅 3/12 significant。这是否表明 shift 主要由 AWQ quantization confound 驱动？[R1, R2 补充]

Q4. Gaussian copula assumption 是否做过正式检验？pairwise 依赖显著偏离 Gaussian copula 时，K_eff 闭合形式与 plug-in MI 估计的差异有多大？[R1]

Q5. Fractional logit (9/12, 11/12, 12/12) 与 wild bootstrap (4/12, 7/12, 8/12) 结果差异巨大。这两种方法对 panel non-independence 的处理有何不同？如果 fractional logit 更可靠，为何不以其为主要分析？[R1, R2 补充]

Q6. 如果用 DBEI (Kuai et al., 2026) 或 κ-diversity 替代 K_eff 做 predictor shift 分析，结果如何？κ-diversity 的 8→7→6 模式（Appendix Q）暗示 shift 可能是 K_eff 构造的 artifact——作者如何回应？[R2]

Q7. Bayesian calibration 在 K=5 恢复 K_eff significance (7/12) 但 K=7 又回到 0/12 的非单调行为原因是什么？[R2]

---

## Missing References

- Genest, C. & Rémillard, B. (2008). Validity of the parametric bootstrap for goodness-of-fit testing in semiparametric models. *Annales de l'IHP* — Gaussian copula GoF 检验标准方法 [R1]
- MacKinnon, J.G., Nielsen, M.Ø., & Webb, M.D. (2023). Cluster-robust inference: A guide to empirical practice. *Journal of Econometrics* — 比 2018 年参考更新的少 cluster 推荐 [R1]
- Roodman, D., MacKinnon, J.G., Nielsen, M.Ø., & Webb, M.D. (2019). Fast and wild: Bootstrap inference in Stata using boottest. *The Stata Journal* — <20 clusters Rademacher weights size distortion 数据 [R1]
- CollabEval (2026) — multi-agent collaborative evaluation framework，三阶段流程与聚合规则分析相关 [R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 config 中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 critical, 3 warning, 19 info）。

**Critical**:
- **Page 19**: 严重空间浪费——Table 14 仅 3 行数据，其下约 3/4 页面完全空白。应合并到前一页或与 page 20 内容合并。

**Warning**:
- **Page 7**: 三个 display item（Table 3 + Figure 2 + Figure 3）密集堆叠，正文解释空间有限。考虑将一个 item 移至相邻页。
- **Page 14**: 约 8 个短小 appendix 节挤在一页，无 display item，密度高且无视觉节奏变化。
- **Page 20**: Tables 15-16 占页面上半部分，下方约 45% 空白。与 page 19 Table 14 合并可节省一整页。

**Info highlights**:
- 正文 8 页内完成（Section 7 Conclusion 在 page 8），符合 EMNLP 8 页限制。
- Display items 密度 0.88/页，与实证论文预期匹配。
- 模板页眉 "Anonymous ACL submission"，符合匿名审稿。
- 颜色方案无色盲不友好设计。
- 全文无 margin 溢出、LaTeX 错误残留或公式渲染异常。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**（可被 Findings 接收）

**Confidence: 4/5**

**判定依据**:

论文在 LLM judge panel 对抗脆弱性领域做出了 systematic empirical contribution：实验规模大（15 models, 6 attacks, ~10,000 panels across 3 K values）、统计方法全面（6+ robustness corrections）、对 confound 的透明度值得肯定。

但三个 critical 问题阻止 Conference 接收：

1. **K_eff 理论基础缺口**：核心指标的公式未获理论支撑，SDPI bound 未证明，且 κ-diversity 替代后 predictor shift 消失暗示 shift 可能是构造 artifact。

2. **Confound 不可分离**：69% 条件下 Cinelli-Hazlett 无法排除 capability confound，API-only 分析显示 predictor shift 不 replicate——核心发现可能主要反映 AWQ 量化引入的 capability variance 而非 diversity 效应。

3. **推断基础脆弱**：少 cluster 下 bootstrap 可靠性不足，predictor shift 的 significance count 增长可能部分是 power artifact（MDE 从 0.144 降至 0.036）。

**升级路径**（从 3.0 → 3.5+）：
- 证明或撤回 SDPI bound，对 K_eff 做 Gaussian copula GoF 检验
- 以 fractional logit 为主要规范，用 effect size 而非 significance count 呈现 predictor shift
- 正文讨论 API-only shift 不 replicate 和 AWQ confound
- 标题加 scope qualifier，abstract 中 "uniformly positive" 加 method-dependent qualifier
- 深化聚合规则分析（特别是 Bayesian calibration 的非单调行为）

**R1 评分**: 3.5 (Borderline Conference) — 认为方法论框架和 robustness check 的广度有独立价值
**R2 评分**: 3.0 (Findings) — 认为 confound + benchmark scope + attack template 限制使论文不够 Conference threshold

Director 采纳 R2 评分：confound 不可分离 + K_eff 理论基础缺口共同构成结构性限制，即使 framing 改善也难以仅通过写作修改达到 Conference 水平。但实证贡献（系统性的 confound characterization + aggregation 分析 + methodology pipeline）足以支撑 Findings。

---

## Detailed Comments

### Section 1 (Introduction)
- Figure 1 框架概览图有效，但首页无 display item（视觉审查建议考虑将 Figure 1 提升至首页）
- Contribution 3 个 bullet point 结构清晰，但 Contribution 1 "uniformly positively associated" 需加 method-dependent qualifier
- 最后一段 "Our findings describe descriptive associations" 的 caveat 位置正确

### Section 2 (Related Work)
- CJT 段落定位改善（vs Round 3），不再 overclaim "contrary to CJT"
- Kuai et al. (2026) DBEI 提及但正文对比不足，应 promote Appendix Q 核心结果
- 建议增加 CollabEval (2026) 讨论
- Ensemble adversarial literature (Tramer 2018, Kariyappa 2019, Pang 2019) 覆盖充分

### Section 3 (Threat Model)
- Definition 1 (Adaptive Adversary) 清晰且有必要
- Theorem 1 (Weakest-Link Monotonicity)：62% stochastic dominance rate 限制了适用范围，应讨论 non-dominant 42% pairs 对回归的影响
- SDPI bound claim（page 4）是最需要修复的单点——要么证明要么撤回

### Section 4 (Methodology)
- Table 1 模型列表清晰，caption 已包含 tier 标准和 AWQ caveat
- Eq. 2 (log-log OLS) 是合理的 starting point，但 ε sensitivity 和高零值率问题需用 fractional logit 解决
- Section 4.6 (Robustness)：cluster 数讨论已加入但辩护逻辑不充分——"low cluster counts alone do not explain" 是 insufficient defense

### Section 5 (Results)
- Table 2 (Dominance): 10 co-dominant 的呈现应附加 collinearity caveat
- Table 3 (Method Comparison): 这是 Round 3 修改的亮点，清晰展示 method sensitivity
- Figure 3 (Predictor Shift): 有效可视化，但 shaded region K* ∈ (3,5) 的两端点均为实测值，shift 的存在基于两个数据点
- Table 4 (Aggregation): Bayesian R²=0.087 是重要发现但正文讨论不足
- Section 5.5 Fractional logit 结果 (9/12, 11/12, 12/12) 是论文最强的 robustness evidence

### Section 6 (Analysis)
- Confound 讨论诚实但解读偏乐观——"stable" 描述掩盖 RV 异质性 (0.005-0.522)
- Pool A 分析有价值但应报告 MDE 和 confidence interval
- Aggregation mechanism 段落过于简略——Bayesian calibration 的 K-dependent 非单调行为是最值得深入的发现

### Section 7 (Conclusion)
- 过于简短（约 4 行），结论应更充分地反映 confound limitation
- "screen η_max at K=3, manage independence at K≥5" 的操作建议在 confound 未解决下过于 assertive

### Limitations
- 覆盖面合理（confound, inference sensitivity, benchmark/attack scope, panel size range）
- 建议将 AWQ confound 单独列为限制点
- 攻击模板对 η_max（有影响）vs K_eff（无影响）的机制区分应明确

### Appendix
- 内容全面但 page 19 排版问题需修复（Table 14 空白浪费）
- Appendix H (Attacked K_eff Stability) 中 position bias ARC ρ=0.08 应在正文标注为例外
- Appendix Q (κ-diversity comparison) 核心结果应 promote 到正文