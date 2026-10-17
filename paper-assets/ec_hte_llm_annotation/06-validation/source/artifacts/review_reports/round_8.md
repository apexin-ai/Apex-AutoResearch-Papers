---
round: 8
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T15:49:11.333680+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 11 (Fresh Review)

**Venue**: EMNLP 2026 (via ARR) | **Deadline**: 2026-05-25 | **Reviewers**: 2 | **Cross-sharing**: Complete

---

## Summary

本文推导了一个精确的偏差分解恒等式（Theorem 1），表明当 LLM 标注的误分类率在子群间存在异质性时，使用全局混淆矩阵进行纠偏会引入与 δ_s·Δτ/(1−2π̄) 成正比的偏差。基于此提出 EC-HTE 方法（层次贝叶斯 Dirichlet-Multinomial 子群混淆矩阵估计 + CausalForestDML），并给出 Δτ-free 的实用诊断准则（Proposition 3, AUC=0.86）。实验在合成数据（K=2,4，260/520 configurations）、半合成 TweetEval 和 11 个真实 LLM 混淆矩阵上进行验证。

---

## Strengths

**[S1] 问题定位精准且有实践价值** [R1✓ R2✓]
识别了 CSS 研究者使用 LLM 标注进行因果推断时的实际问题——全局混淆矩阵纠偏在子群异质性下可能适得其反。Figure 1 有效展示机制差异。

**[S2] 理论结果 clean 且可解释** [R1✓ R2✓]
Theorem 1 的 δ_s·Δτ/(1−2π̄) 乘积结构是精确恒等式（非渐近近似），将偏差归因为三个可解释组成部分。R1 逐步验证代数推导正确。Corollary 4（多类别）和 Remark 2（非对称）下 product structure 仍成立。

**[S3] 实验验证全面** [R1✓ R2✓]
269/520 合成网格、TweetEval 半合成、11 个真实 LLM CM 交叉验证（R²=0.975）、PPCI 组合实验、7 个开源 LLM 多模型验证。25 页附录的系统性在 NLP 投稿中突出。Bias identity 的经验验证（R²≥0.975 across 11 model-dataset combinations）尤其令人信服。

**[S4] Δτ-free 诊断准则有独立实用价值** [R1✓ R2✓]
Proposition 3 允许仅凭子群误分类率判断全局纠偏是否有害，无需估计处理效应，对从业者有直接价值。

**[S5] 工程设计合理** [R1✓]
Algorithm 1 的前置条件检查、奇异性保护（κ>100 fallback）、方差调整 SE 传播使方法具有实际可部署性。HB 在小样本时（n_expert/K<100）87.5% 配置胜过分层 MLE。

**[S6] PPCI 正交组合分析** [R2✓]
展示 EC-HTE 与 PPCI 纠正不同误差来源，两者可叠加降偏，帮助读者理解方法在更大生态中的位置。

---

## Weaknesses

### Critical

**[W1] CausalForest 覆盖率系统性低于名义水平，SE 验证不完整** [R1✓ R2✓ — 完全共识]
- HB EC-HTE + CausalForest 在 K=4 extreme 下覆盖率 0.91（名义 0.95），semi-synthetic 降至 0.84
- Plug-in SE（Algorithm 1 Line 16）假定 Ĉ 已知，不传播混淆矩阵估计不确定性
- Appendix Y 仅对 DIM 验证 SE（≥0.96），**从未对 CausalForest 做同等验证**——CausalForest 的方差结构更复杂（honest splitting + forest-level aggregation），plug-in 假设更脆弱
- 置信区间是因果推断的核心输出，系统性 under-coverage 严重削弱不确定性量化可靠性
- **修复**: 补充 CausalForest-specific 覆盖率校准实验；考虑 bootstrap SE 替代 plug-in

**[W2] Assumption (A2) 对称误分类与实际 LLM 行为严重不符** [R1=critical, R2=between critical/major]
- Table 12 显示 GPT-4.1 在 S0 子群 FPR=0.38 vs FNR=0.054（7:1 比例）
- Appendix J 非对称推广 R²=0.931（product structure 大体成立），但 Proposition 3 AUC 从 0.86 降至 0.82——诊断工具在实际非对称场景下可靠性降低
- 主文仅以 Remark 2（4 行）一笔带过，非对称 general formula 完全放在附录
- **修复**: 主文至少以 Remark 呈现非对称 formula；讨论 Prop 3 在非对称下的 AUC 降幅

### Major

**[W3] Assumption (A1) 条件独立性不可检验且无敏感性分析** [R1✓ R2✓ — 完全共识]
- LLM 误分类可能与文本的结局相关特征相关（情感强度、论证复杂度），使 (A1) 在典型 CSS 场景中系统性违反
- 若 (A1) 违反，τ_obs(z,s) ≠ Σ M_s[z,z']·τ(z')，Theorem 1 整体失效
- 论文承认 "不可经验检验" 但未提供任何敏感性分析框架
- **修复**: 参考 Rosenbaum (2002) / Carroll et al. (2006) Ch.9，引入 sensitivity parameter 量化违反时偏差退化

**[W4] Framing 存在选择性强调** [R1 部分同意, R2✓]
- Abstract 突出正面结果（reducing |bias| from 0.059 to 0.010），TweetEval 上 EC-HTE 未显著改善的结果（aggregate RMSE 0.225 > Global 0.107）在 abstract 中完全缺席
- "50% of K=2 configurations (260/520)" 依赖参数网格设计，未注明
- R1 认为标题 "When" 已限定条件性；R2 认为标题仍有误导性（仅研究全局 CM 纠正一种方式）
- **修复**: Abstract 平衡呈现正负结果；"50%" 注明依赖参数网格或改为 "a substantial fraction"

**[W5] 正文超出 8 页限制** [R1✓ R2✓ — 完全共识，严重性分歧：R2=critical, R1=major]
- Section 5.5（Multi-LLM Validation）和 Section 6（Conclusion）位于第 9 页，属正文内容
- EMNLP 2026 long paper 正文限制严格 8 页
- **修复**: 移 Section 5.5 至 Appendix，压缩 Conclusion

**[W6] Assumption (A3) P(Z=1)=0.5 限制泛化性** [R1✓ R2✓ — 共识]
- Appendix T 显示 P(Z=1) 偏离 0.5 时 EC-HTE RMSE 比值达 1.06-1.68
- 实际 NLP 分类中类别不平衡是常态（如仇恨言论检测正类比例远低于 50%）
- Corollary 4 已有理论放松路径，但实验验证不足，主文讨论不充分

**[W7] 方法论新颖性争议** [核心分歧 — R1 rebut, R2 maintain]
- **R2 立场**: Theorem 1 是 Frazis-Loewenstein (2003) 标量衰减的自然子群推广（代数上不深刻）；方法组合标准组件（HB Dirichlet-Multinomial + CausalForestDML）；Proposition 3 是定理直接推论。更接近 application paper。
- **R1 立场**: δ_s·Δτ 乘积结构揭示异质误分类下方向可变的偏差放大——与 F-L 同质衰减本质不同（mixing matrix algebra vs OLS projection）；"debiasing can hurt" 充要条件在先前文献无对应；组合动机由 Theorem 1 驱动，是 theory-driven methodology paper。
- **评审未达成一致**。此分歧直接影响评分（R1=3.5 vs R2=3.0）。

**[W8] 缺乏完全真实世界验证** [R1 部分同意, R2✓]
- 所有 CATE 为合成注入，即使 "real LLM CM" 实验中因果结构仍是合成的
- R1 指出这在因果推断方法论文中是标准做法（Wager & Athey 2018 等），11 个真实 LLM CM 的 R²=0.975 提供部分外部效度
- **结构性限制**: CATE ground truth 需 RCT，不可能完全真实

**[W9] κ>100 奇异性保护阈值无消融实验** [R1✓ R2✓ — 共识]
- Algorithm 1 中阈值 100 的选取无理论推导或 κ∈{50,100,200,500} 消融

### Minor

**[W10] "estimator-agnostic" 措辞过强** [R1✓ R2 部分同意]
- 仅验证 DIM、CausalForest、R-learner 三种估计器；T/X/DR-learner 未涉及
- 建议改为 "compatible with a range of HTE estimators"

**[W11] K 仅探索到 4** [R1✓ R2✓]
- K≥8 时 per-subgroup expert labels 下降，HB partial pooling 行为可能改变

**[W12] Expert label 成本与替代方案比较缺失** [R2✓, R1 认为超出范围]
- K=4 需至少 200 expert labels
- 未与替代方案（扩充训练集/calibration/active learning）比较效率

**[W13] 定理/命题编号混用** [R1✓ R2✓]
- Theorem 1 → Remark 2 → Proposition 3 → Corollary 4 共享计数器

---

## Reviewer Consensus [AGREE]

以下关键问题两位 Reviewer 达成一致：
1. **CausalForest 覆盖率系统性不足** — critical，需补充 CF-specific SE 验证
2. **(A2) 对称假设远离现实** — 主文需更显著呈现非对称推广 + 讨论诊断降级
3. **(A1) 无敏感性分析** — 需提供违反时定量退化分析
4. **正文超 8 页** — 格式违规，需移 Section 5.5 至 Appendix
5. **Framing 选择性强调** — Abstract 需平衡呈现 TweetEval 负面结果
6. **(A3) 等概率限制** — 主文讨论不足
7. **κ>100 无消融** — 需实验验证

## Reviewer Divergence [REBUT]

1. **技术新颖性**（影响评分的核心分歧）: R1 认为 theory-driven methodology（3.5），R2 认为增量性推广（3.0）
2. **真实世界验证缺失严重性**: R1=minor-to-major（因果推断标准做法），R2=major（声称实用工具但缺验证）
3. **格式违规严重性**: R2=critical，R1=major（可快速修复）
4. **(A2) 严重性**: R1=critical，R2=between critical/major（推广路径存在）

---

## Questions

1. **(A1) 敏感性**: 误分类率与潜在结果相关时，EC-HTE 的偏差和覆盖率如何退化？ [R1✓ R2✓]
2. **K 扩展**: K=8/16 时 HB 表现和 partial pooling 有效性？ [R1✓ R2✓]
3. **异常值**: GPT-4o-mini on Civil Comments R²=0.776 的根因？ [R1, R2✓]
4. **Global 覆盖率**: Table 1 中 Global 覆盖率 0.005 对已发表 CSS 研究的含义？ [R1]
5. **TweetEval 根因**: EC-HTE 未改善是 Δτ 小、δ_s 小、还是子群定义？ [R2, R1 部分回应]
6. **Scalability**: HB Gibbs 采样计算时间？变分推断替代？ [R1, R2✓]
7. **联合 SE**: EC-HTE + PPCI 标准误差如何联合传播？ [R1, R2✓]
8. **成本效益**: 200 expert labels 与直接扩充训练集/calibration 的效率比较？ [R2]

---

## Missing References

1. **Semenova & Chernozhukov (2021)** "Debiased machine learning of conditional average treatment effects" [R1 提出, R2 同意] — CATE debiased estimation 核心理论
2. **Blackwell, Honaker, and King (2017)** "A Unified Approach to Measurement Error and Missing Data" [R2 提出, R1 同意] — 政治科学测量误差统一框架
3. **LLM Calibration 文献** (temperature scaling, Platt scaling, Adaptive Temperature Scaling) [R2] — 减少子群误分类异质性的替代/补充方案

---

## External Review (Stanford Agentic Reviewer)

未请求——项目配置中未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: done (2026-05-22T15:23-15:27) | 0 critical / 3 warning / 9 info

**Warnings:**
1. **Page 3-7 连续 5 页无 figure/table** — Figure 1 (p2) 到 Figure 2+Table 1 (p8) 之间长达 5 页纯文本+公式段。Section 4 方法部分完全无 display item。建议主文加 method overview 图或将 Algorithm 1 移入主文。
2. **主文仅 3 个 display items**（2 figures + 1 table），低于实证论文典型密度（5-8 个/9 页）。
3. **Algorithm 1 (p25) 仅占页面上部 ~40%**，下方大面积空白。建议移入主文 Section 4。

**Info:** Figure 1 偏小（建议 figure*）| Figure 2 热力图清晰 | Table 1 格式规范 | 公式渲染正确 | 参考文献格式统一 | Figure 5 对红绿色盲不够友好（建议补 pattern/hatching）

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分理由:**
论文解决了一个切实且相关的问题，Theorem 1 的偏差分解干净且正确，实验验证在 NLP 投稿中堪称全面（25 页附录、11 个真实 LLM CM、R²=0.975）。但两个 critical issues 构成主要障碍：(1) CausalForest 覆盖率系统性不足（0.84-0.91 vs 0.95），置信区间不可靠；(2) (A2) 对称假设与真实 LLM 行为（7:1 FPR/FNR）严重不符。多个 major issues 未解决：(A1) 无敏感性分析、正文超 8 页、framing 选择性强调。技术新颖性存在审稿人分歧（R1=3.5 Borderline Conference, R2=3.0 Findings）。

**Reviewer 评分**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)

**置信度**: 4/5

**修订优先级:**
1. **[Must-Fix]** 补充 CausalForest SE 校准实验（与 DIM Appendix Y 等同验证）
2. **[Must-Fix]** 主文呈现非对称 general formula + Proposition 3 在非对称下 AUC 降幅讨论
3. **[Must-Fix]** 压缩正文至 ≤ 8 页（移 Section 5.5 至 Appendix）
4. **[Should-Fix]** 增加 (A1) 违反时的敏感性分析（sensitivity parameter + simulation）
5. **[Should-Fix]** Abstract 平衡呈现 TweetEval 负面结果
6. **[Should-Fix]** κ>100 阈值消融实验
7. **[Nice-to-Have]** K≥8 实验探索
8. **[Nice-to-Have]** HB Gibbs 计算时间报告 + scalability 讨论

**升级路径**: 如 Must-Fix 1-3 全部解决 + Should-Fix 4-5 至少部分解决，论文可达 3.5 (Borderline Conference) 水平。

---

## Detailed Comments

### Section 1 (Introduction)
- Figure 1 caption 描述可能有误：两次 "under-correcting"，疑似应为 "over-correcting low-error subgroups" [R2]
- "50% of K=2 configurations (260/520)" 依赖参数网格设计，建议注明或改为 "a substantial fraction" [R1✓ R2✓]

### Section 2 (Related Work)
- 三层技术区分策略有效，但第三个区分点（product structure）略有过度声称——F-L 子群化后可自然产生类似结构 [R2]
- 缺少 Semenova &amp; Chernozhukov (2021)、Blackwell et al. (2017)、LLM calibration 方法的引用 [R1, R2]
- 与 F-L (2003) 的公式级对比仍缺失（R10 遗留问题）[R1✓ R2✓]

### Section 3 (Bias Decomposition)
- Theorem 1 代数正确 [R1 验证]
- (A5) 应明确说明是简化而非必要条件，避免读者误解 [R2]
- Proposition 3 AUC=0.86 的评估参数范围/分布未说明 [R2]
- (A2) Remark 2 仅 4 行过于简略，应更显著呈现非对称推广 [R1✓ R2✓]

### Section 4 (EC-HTE)
- Gamma(3,1) 超先验经 Appendix G 验证不敏感 [R2✓]
- κ>100 阈值缺消融 [R1✓ R2✓]
- Plug-in SE "small relative to outcome variance" 在 n_expert=25 时可能不成立 [R2]
- R̂<1.01 收敛标准可能过宽（Vehtari et al. 2021 建议 <1.005）[R1]

### Section 5 (Experiments)
- Table 1 信息密度合理 [R2✓]
- Bias identity R²=0.975 是最有说服力的实证结果 [R1✓ R2✓]
- TweetEval EC-HTE aggregate RMSE (0.225) > Global (0.107) 需更诚实呈现 [R1✓ R2✓]
- 合成实验 T~Bernoulli(0.5) 独立于协变量（无混杂），有混杂设置下表现未验证 [R1]
- Section 5.5 应移至 Appendix（超页） [R1✓ R2✓]
- Section 5.4 recommended workflow 仅两段，建议扩展为结构化 decision flowchart [R2]

### Section 6 (Conclusion)
- 偏长（约半页），包含前瞻性内容更适合 Discussion [R2]
- 位于第 9 页，超页 [R1✓ R2✓]

### Limitations
- 涵盖关键限制但缺少 "所有实验使用合成/半合成因果结构" 的明确声明 [R2]

### Appendix
- 13+ 个附录与 8 页正文之间存在不匹配，体量可能暗示用量弥补深度 [R2]
- Appendix Y CausalForest SE 验证缺失是重要遗漏 [R1✓ R2✓]
- Appendix B Corollary 4 更像 sketch，建议补充 J=3 数值例子 [R1]