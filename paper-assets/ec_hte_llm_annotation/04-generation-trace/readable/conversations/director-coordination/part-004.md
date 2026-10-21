# Director coordination — Part 4 of 10

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/fb/fb462ae0cd5c4c630c34.json)

## Round 77

### Tool call

_source line 814 · 2026-05-22T15:49:11.303247+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 11 (Fresh Review)\n\n**Venue**: EMNLP 2026 (via ARR) | **Deadline**: 2026-05-25 | **Reviewers**: 2 | **Cross-sharing**: Complete\n\n---\n\n## Summary\n\n本文推导了一个精确的偏差分解恒等式（Theorem 1），表明当 LLM 标注的误分类率在子群间存在异质性时，使用全局混淆矩阵进行纠偏会引入与 δ_s·Δτ/(1−2π̄) 成正比的偏差。基于此提出 EC-HTE 方法（层次贝叶斯 Dirichlet-Multinomial 子群混淆矩阵估计 + CausalForestDML），并给出 Δτ-free 的实用诊断准则（Proposition 3, AUC=0.86）。实验在合成数据（K=2,4，260/520 configurations）、半合成 TweetEval 和 11 个真实 LLM 混淆矩阵上进行验证。\n\n---\n\n## Strengths\n\n**[S1] 问题定位精准且有实践价值** [R1✓ R2✓]\n识别了 CSS 研究者使用 LLM 标注进行因果推断时的实际问题——全局混淆矩阵纠偏在子群异质性下可能适得其反。Figure 1 有效展示机制差异。\n\n**[S2] 理论结果 clean 且可解释** [R1✓ R2✓]\nTheorem 1 的 δ_s·Δτ/(1−2π̄) 乘积结构是精确恒等式（非渐近近似），将偏差归因为三个可解释组成部分。R1 逐步验证代数推导正确。Corollary 4（多类别）和 Remark 2（非对称）下 product structure 仍成立。\n\n**[S3] 实验验证全面** [R1✓ R2✓]\n269/520 合成网格、TweetEval 半合成、11 个真实 LLM CM 交叉验证（R²=0.975）、PPCI 组合实验、7 个开源 LLM 多模型验证。25 页附录的系统性在 NLP 投稿中突出。Bias identity 的经验验证（R²≥0.975 across 11 model-dataset combinations）尤其令人信服。\n\n**[S4] Δτ-free 诊断准则有独立实用价值** [R1✓ R2✓]\nProposition 3 允许仅凭子群误分类率判断全局纠偏是否有害，无需估计处理效应，对从业者有直接价值。\n\n**[S5] 工程设计合理** [R1✓]\nAlgorithm 1 的前置条件检查、奇异性保护（κ>100 fallback）、方差调整 SE 传播使方法具有实际可部署性。HB 在小样本时（n_expert/K<100）87.5% 配置胜过分层 MLE。\n\n**[S6] PPCI 正交组合分析** [R2✓]\n展示 EC-HTE 与 PPCI 纠正不同误差来源，两者可叠加降偏，帮助读者理解方法在更大生态中的位置。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**[W1] CausalForest 覆盖率系统性低于名义水平，SE 验证不完整** [R1✓ R2✓ — 完全共识]\n- HB EC-HTE + CausalForest 在 K=4 extreme 下覆盖率 0.91（名义 0.95），semi-synthetic 降至 0.84\n- Plug-in SE（Algorithm 1 Line 16）假定 Ĉ 已知，不传播混淆矩阵估计不确定性\n- Appendix Y 仅对 DIM 验证 SE（≥0.96），**从未对 CausalForest 做同等验证**——CausalForest 的方差结构更复杂（honest splitting + forest-level aggregation），plug-in 假设更脆弱\n- 置信区间是因果推断的核心输出，系统性 under-coverage 严重削弱不确定性量化可靠性\n- **修复**: 补充 CausalForest-specific 覆盖率校准实验；考虑 bootstrap SE 替代 plug-in\n\n**[W2] Assumption (A2) 对称误分类与实际 LLM 行为严重不符** [R1=critical, R2=between critical/major]\n- Table 12 显示 GPT-4.1 在 S0 子群 FPR=0.38 vs FNR=0.054（7:1 比例）\n- Appendix J 非对称推广 R²=0.931（product structure 大体成立），但 Proposition 3 AUC 从 0.86 降至 0.82——诊断工具在实际非对称场景下可靠性降低\n- 主文仅以 Remark 2（4 行）一笔带过，非对称 general formula 完全放在附录\n- **修复**: 主文至少以 Remark 呈现非对称 formula；讨论 Prop 3 在非对称下的 AUC 降幅\n\n### Major\n\n**[W3] Assumption (A1) 条件独立性不可检验且无敏感性分析** [R1✓ R2✓ — 完全共识]\n- LLM 误分类可能与文本的结局相关特征相关（情感强度、论证复杂度），使 (A1) 在典型 CSS 场景中系统性违反\n- 若 (A1) 违反，τ_obs(z,s) ≠ Σ M_s[z,z']·τ(z')，Theorem 1 整体失效\n- 论文承认 \"不可经验检验\" 但未提供任何敏感性分析框架\n- **修复**: 参考 Rosenbaum (2002) / Carroll et al. (2006) Ch.9，引入 sensitivity parameter 量化违反时偏差退化\n\n**[W4] Framing 存在选择性强调** [R1 部分同意, R2✓]\n- Abstract 突出正面结果（reducing |bias| from 0.059 to 0.010），TweetEval 上 EC-HTE 未显著改善的结果（aggregate RMSE 0.225 > Global 0.107）在 abstract 中完全缺席\n- \"50% of K=2 configurations (260/520)\" 依赖参数网格设计，未注明\n- R1 认为标题 \"When\" 已限定条件性；R2 认为标题仍有误导性（仅研究全局 CM 纠正一种方式）\n- **修复**: Abstract 平衡呈现正负结果；\"50%\" 注明依赖参数网格或改为 \"a substantial fraction\"\n\n**[W5] 正文超出 8 页限制** [R1✓ R2✓ — 完全共识，严重性分歧：R2=critical, R1=major]\n- Section 5.5（Multi-LLM Validation）和 Section 6（Conclusion）位于第 9 页，属正文内容\n- EMNLP 2026 long paper 正文限制严格 8 页\n- **修复**: 移 Section 5.5 至 Appendix，压缩 Conclusion\n\n**[W6] Assumption (A3) P(Z=1)=0.5 限制泛化性** [R1✓ R2✓ — 共识]\n- Appendix T 显示 P(Z=1) 偏离 0.5 时 EC-HTE RMSE 比值达 1.06-1.68\n- 实际 NLP 分类中类别不平衡是常态（如仇恨言论检测正类比例远低于 50%）\n- Corollary 4 已有理论放松路径，但实验验证不足，主文讨论不充分\n\n**[W7] 方法论新颖性争议** [核心分歧 — R1 rebut, R2 maintain]\n- **R2 立场**: Theorem 1 是 Frazis-Loewenstein (2003) 标量衰减的自然子群推广（代数上不深刻）；方法组合标准组件（HB Dirichlet-Multinomial + CausalForestDML）；Proposition 3 是定理直接推论。更接近 application paper。\n- **R1 立场**: δ_s·Δτ 乘积结构揭示异质误分类下方向可变的偏差放大——与 F-L 同质衰减本质不同（mixing matrix algebra vs OLS projection）；\"debiasing can hurt\" 充要条件在先前文献无对应；组合动机由 Theorem 1 驱动，是 theory-driven methodology paper。\n- **评审未达成一致**。此分歧直接影响评分（R1=3.5 vs R2=3.0）。\n\n**[W8] 缺乏完全真实世界验证** [R1 部分同意, R2✓]\n- 所有 CATE 为合成注入，即使 \"real LLM CM\" 实验中因果结构仍是合成的\n- R1 指出这在因果推断方法论文中是标准做法（Wager & Athey 2018 等），11 个真实 LLM CM 的 R²=0.975 提供部分外部效度\n- **结构性限制**: CATE ground truth 需 RCT，不可能完全真实\n\n**[W9] κ>100 奇异性保护阈值无消融实验** [R1✓ R2✓ — 共识]\n- Algorithm 1 中阈值 100 的选取无理论推导或 κ∈{50,100,200,500} 消融\n\n### Minor\n\n**[W10] \"estimator-agnostic\" 措辞过强** [R1✓ R2 部分同意]\n- 仅验证 DIM、CausalForest、R-learner 三种估计器；T/X/DR-learner 未涉及\n- 建议改为 \"compatible with a range of HTE estimators\"\n\n**[W11] K 仅探索到 4** [R1✓ R2✓]\n- K≥8 时 per-subgroup expert labels 下降，HB partial pooling 行为可能改变\n\n**[W12] Expert label 成本与替代方案比较缺失** [R2✓, R1 认为超出范围]\n- K=4 需至少 200 expert labels\n- 未与替代方案（扩充训练集/calibration/active learning）比较效率\n\n**[W13] 定理/命题编号混用** [R1✓ R2✓]\n- Theorem 1 → Remark 2 → Proposition 3 → Corollary 4 共享计数器\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下关键问题两位 Reviewer 达成一致：\n1. **CausalForest 覆盖率系统性不足** — critical，需补充 CF-specific SE 验证\n2. **(A2) 对称假设远离现实** — 主文需更显著呈现非对称推广 + 讨论诊断降级\n3. **(A1) 无敏感性分析** — 需提供违反时定量退化分析\n4. **正文超 8 页** — 格式违规，需移 Section 5.5 至 Appendix\n5. **Framing 选择性强调** — Abstract 需平衡呈现 TweetEval 负面结果\n6. **(A3) 等概率限制** — 主文讨论不足\n7. **κ>100 无消融** — 需实验验证\n\n## Reviewer Divergence [REBUT]\n\n1. **技术新颖性**（影响评分的核心分歧）: R1 认为 theory-driven methodology（3.5），R2 认为增量性推广（3.0）\n2. **真实世界验证缺失严重性**: R1=minor-to-major（因果推断标准做法），R2=major（声称实用工具但缺验证）\n3. **格式违规严重性**: R2=critical，R1=major（可快速修复）\n4. **(A2) 严重性**: R1=critical，R2=between critical/major（推广路径存在）\n\n---\n\n## Questions\n\n1. **(A1) 敏感性**: 误分类率与潜在结果相关时，EC-HTE 的偏差和覆盖率如何退化？ [R1✓ R2✓]\n2. **K 扩展**: K=8/16 时 HB 表现和 partial pooling 有效性？ [R1✓ R2✓]\n3. **异常值**: GPT-4o-mini on Civil Comments R²=0.776 的根因？ [R1, R2✓]\n4. **Global 覆盖率**: Table 1 中 Global 覆盖率 0.005 对已发表 CSS 研究的含义？ [R1]\n5. **TweetEval 根因**: EC-HTE 未改善是 Δτ 小、δ_s 小、还是子群定义？ [R2, R1 部分回应]\n6. **Scalability**: HB Gibbs 采样计算时间？变分推断替代？ [R1, R2✓]\n7. **联合 SE**: EC-HTE + PPCI 标准误差如何联合传播？ [R1, R2✓]\n8. **成本效益**: 200 expert labels 与直接扩充训练集/calibration 的效率比较？ [R2]\n\n---\n\n## Missing References\n\n1. **Semenova & Chernozhukov (2021)** \"Debiased machine learning of conditional average treatment effects\" [R1 提出, R2 同意] — CATE debiased estimation 核心理论\n2. **Blackwell, Honaker, and King (2017)** \"A Unified Approach to Measurement Error and Missing Data\" [R2 提出, R1 同意] — 政治科学测量误差统一框架\n3. **LLM Calibration 文献** (temperature scaling, Platt scaling, Adaptive Temperature Scaling) [R2] — 减少子群误分类异质性的替代/补充方案\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求——项目配置中未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (2026-05-22T15:23-15:27) | 0 critical / 3 warning / 9 info\n\n**Warnings:**\n1. **Page 3-7 连续 5 页无 figure/table** — Figure 1 (p2) 到 Figure 2+Table 1 (p8) 之间长达 5 页纯文本+公式段。Section 4 方法部分完全无 display item。建议主文加 method overview 图或将 Algorithm 1 移入主文。\n2. **主文仅 3 个 display items**（2 figures + 1 table），低于实证论文典型密度（5-8 个/9 页）。\n3. **Algorithm 1 (p25) 仅占页面上部 ~40%**，下方大面积空白。建议移入主文 Section 4。\n\n**Info:** Figure 1 偏小（建议 figure*）| Figure 2 热力图清晰 | Table 1 格式规范 | 公式渲染正确 | 参考文献格式统一 | Figure 5 对红绿色盲不够友好（建议补 pattern/hatching）\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分理由:**\n论文解决了一个切实且相关的问题，Theorem 1 的偏差分解干净且正确，实验验证在 NLP 投稿中堪称全面（25 页附录、11 个真实 LLM CM、R²=0.975）。但两个 critical issues 构成主要障碍：(1) CausalForest 覆盖率系统性不足（0.84-0.91 vs 0.95），置信区间不可靠；(2) (A2) 对称假设与真实 LLM 行为（7:1 FPR/FNR）严重不符。多个 major issues 未解决：(A1) 无敏感性分析、正文超 8 页、framing 选择性强调。技术新颖性存在审稿人分歧（R1=3.5 Borderline Conference, R2=3.0 Findings）。\n\n**Reviewer 评分**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)\n\n**置信度**: 4/5\n\n**修订优先级:**\n1. **[Must-Fix]** 补充 CausalForest SE 校准实验（与 DIM Appendix Y 等同验证）\n2. **[Must-Fix]** 主文呈现非对称 general formula + Proposition 3 在非对称下 AUC 降幅讨论\n3. **[Must-Fix]** 压缩正文至 ≤ 8 页（移 Section 5.5 至 Appendix）\n4. **[Should-Fix]** 增加 (A1) 违反时的敏感性分析（sensitivity parameter + simulation）\n5. **[Should-Fix]** Abstract 平衡呈现 TweetEval 负面结果\n6. **[Should-Fix]** κ>100 阈值消融实验\n7. **[Nice-to-Have]** K≥8 实验探索\n8. **[Nice-to-Have]** HB Gibbs 计算时间报告 + scalability 讨论\n\n**升级路径**: 如 Must-Fix 1-3 全部解决 + Should-Fix 4-5 至少部分解决，论文可达 3.5 (Borderline Conference) 水平。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Figure 1 caption 描述可能有误：两次 \"under-correcting\"，疑似应为 \"over-correcting low-error subgroups\" [R2]\n- \"50% of K=2 configurations (260/520)\" 依赖参数网格设计，建议注明或改为 \"a substantial fraction\" [R1✓ R2✓]\n\n### Section 2 (Related Work)\n- 三层技术区分策略有效，但第三个区分点（product structure）略有过度声称——F-L 子群化后可自然产生类似结构 [R2]\n- 缺少 Semenova &amp; Chernozhukov (2021)、Blackwell et al. (2017)、LLM calibration 方法的引用 [R1, R2]\n- 与 F-L (2003) 的公式级对比仍缺失（R10 遗留问题）[R1✓ R2✓]\n\n### Section 3 (Bias Decomposition)\n- Theorem 1 代数正确 [R1 验证]\n- (A5) 应明确说明是简化而非必要条件，避免读者误解 [R2]\n- Proposition 3 AUC=0.86 的评估参数范围/分布未说明 [R2]\n- (A2) Remark 2 仅 4 行过于简略，应更显著呈现非对称推广 [R1✓ R2✓]\n\n### Section 4 (EC-HTE)\n- Gamma(3,1) 超先验经 Appendix G 验证不敏感 [R2✓]\n- κ>100 阈值缺消融 [R1✓ R2✓]\n- Plug-in SE \"small relative to outcome variance\" 在 n_expert=25 时可能不成立 [R2]\n- R̂<1.01 收敛标准可能过宽（Vehtari et al. 2021 建议 <1.005）[R1]\n\n### Section 5 (Experiments)\n- Table 1 信息密度合理 [R2✓]\n- Bias identity R²=0.975 是最有说服力的实证结果 [R1✓ R2✓]\n- TweetEval EC-HTE aggregate RMSE (0.225) > Global (0.107) 需更诚实呈现 [R1✓ R2✓]\n- 合成实验 T~Bernoulli(0.5) 独立于协变量（无混杂），有混杂设置下表现未验证 [R1]\n- Section 5.5 应移至 Appendix（超页） [R1✓ R2✓]\n- Section 5.4 recommended workflow 仅两段，建议扩展为结构化 decision flowchart [R2]\n\n### Section 6 (Conclusion)\n- 偏长（约半页），包含前瞻性内容更适合 Discussion [R2]\n- 位于第 9 页，超页 [R1✓ R2✓]\n\n### Limitations\n- 涵盖关键限制但缺少 \"所有实验使用合成/半合成因果结构\" 的明确声明 [R2]\n\n### Appendix\n- 13+ 个附录与 8 页正文之间存在不匹配，体量可能暗示用量弥补深度 [R2]\n- Appendix Y CausalForest SE 验证缺失是重要遗漏 [R1✓ R2✓]\n- Appendix B Corollary 4 更像 sketch，建议补充 J=3 数值例子 [R1]",
  "project": "ec_hte_llm_annotation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 11 (Fresh Review)\n\n**Venue**: EMNLP 2026 (via ARR) | **Deadline**: 2026-05-25 | **Reviewers**: 2 | **Cross-sharing**: Complete\n\n---\n\n## Summary\n\n本文推导了一个精确的偏差分解恒等式（Theorem 1），表明当 LLM 标注的误分类率在子群间存在异质性时，使用全局混淆矩阵进行纠偏会引入与 δ_s·Δτ/(1−2π̄) 成正比的偏差。基于此提出 EC-HTE 方法（层次贝叶斯 Dirichlet-Multinomial 子群混淆矩阵估计 + CausalForestDML），并给出 Δτ-free 的实用诊断准则（Proposition 3, AUC=0.86）。实验在合成数据（K=2,4，260/520 configurations）、半合成 TweetEval 和 11 个真实 LLM 混淆矩阵上进行验证。\n\n---\n\n## Strengths\n\n**[S1] 问题定位精准且有实践价值** [R1✓ R2✓]\n识别了 CSS 研究者使用 LLM 标注进行因果推断时的实际问题——全局混淆矩阵纠偏在子群异质性下可能适得其反。Figure 1 有效展示机制差异。\n\n**[S2] 理论结果 clean 且可解释** [R1✓ R2✓]\nTheorem 1 的 δ_s·Δτ/(1−2π̄) 乘积结构是精确恒等式（非渐近近似），将偏差归因为三个可解释组成部分。R1 逐步验证代数推导正确。Corollary 4（多类别）和 Remark 2（非对称）下 product structure 仍成立。\n\n**[S3] 实验验证全面** [R1✓ R2✓]\n269/520 合成网格、TweetEval 半合成、11 个真实 LLM CM 交叉验证（R²=0.975）、PPCI 组合实验、7 个开源 LLM 多模型验证。25 页附录的系统性在 NLP 投稿中突出。Bias identity 的经验验证（R²≥0.975 across 11 model-dataset combinations）尤其令人信服。\n\n**[S4] Δτ-free 诊断准则有独立实用价值** [R1✓ R2✓]\nProposition 3 允许仅凭子群误分类率判断全局纠偏是否有害，无需估计处理效应，对从业者有直接价值。\n\n**[S5] 工程设计合理** [R1✓]\nAlgorithm 1 的前置条件检查、奇异性保护（κ>100 fallback）、方差调整 SE 传播使方法具有实际可部署性。HB 在小样本时（n_expert/K<100）87.5% 配置胜过分层 MLE。\n\n**[S6] PPCI 正交组合分析** [R2✓]\n展示 EC-HTE 与 PPCI 纠正不同误差来源，两者可叠加降偏，帮助读者理解方法在更大生态中的位置。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**[W1] CausalForest 覆盖率系统性低于名义水平，SE 验证不完整** [R1✓ R2✓ — 完全共识]\n- HB EC-HTE + CausalForest 在 K=4 extreme 下覆盖率 0.91（名义 0.95），semi-synthetic 降至 0.84\n- Plug-in SE（Algorithm 1 Line 16）假定 Ĉ 已知，不传播混淆矩阵估计不确定性\n- Appendix Y 仅对 DIM 验证 SE（≥0.96），**从未对 CausalForest 做同等验证**——CausalForest 的方差结构更复杂（honest splitting + forest-level aggregation），plug-in 假设更脆弱\n- 置信区间是因果推断的核心输出，系统性 under-coverage 严重削弱不确定性量化可靠性\n- **修复**: 补充 CausalForest-specific 覆盖率校准实验；考虑 bootstrap SE 替代 plug-in\n\n**[W2] Assumption (A2) 对称误分类与实际 LLM 行为严重不符** [R1=critical, R2=between critical/major]\n- Table 12 显示 GPT-4.1 在 S0 子群 FPR=0.38 vs FNR=0.054（7:1 比例）\n- Appendix J 非对称推广 R²=0.931（product structure 大体成立），但 Proposition 3 AUC 从 0.86 降至 0.82——诊断工具在实际非对称场景下可靠性降低\n- 主文仅以 Remark 2（4 行）一笔带过，非对称 general formula 完全放在附录\n- **修复**: 主文至少以 Remark 呈现非对称 formula；讨论 Prop 3 在非对称下的 AUC 降幅\n\n### Major\n\n**[W3] Assumption (A1) 条件独立性不可检验且无敏感性分析** [R1✓ R2✓ — 完全共识]\n- LLM 误分类可能与文本的结局相关特征相关（情感强度、论证复杂度），使 (A1) 在典型 CSS 场景中系统性违反\n- 若 (A1) 违反，τ_obs(z,s) ≠ Σ M_s[z,z']·τ(z')，Theorem 1 整体失效\n- 论文承认 \"不可经验检验\" 但未提供任何敏感性分析框架\n- **修复**: 参考 Rosenbaum (2002) / Carroll et al. (2006) Ch.9，引入 sensitivity parameter 量化违反时偏差退化\n\n**[W4] Framing 存在选择性强调** [R1 部分同意, R2✓]\n- Abstract 突出正面结果（reducing |bias| from 0.059 to 0.010），TweetEval 上 EC-HTE 未显著改善的结果（aggregate RMSE 0.225 > Global 0.107）在 abstract 中完全缺席\n- \"50% of K=2 configurations (260/520)\" 依赖参数网格设计，未注明\n- R1 认为标题 \"When\" 已限定条件性；R2 认为标题仍有误导性（仅研究全局 CM 纠正一种方式）\n- **修复**: Abstract 平衡呈现正负结果；\"50%\" 注明依赖参数网格或改为 \"a substantial fraction\"\n\n**[W5] 正文超出 8 页限制** [R1✓ R2✓ — 完全共识，严重性分歧：R2=critical, R1=major]\n- Section 5.5（Multi-LLM Validation）和 Section 6（Conclusion）位于第 9 页，属正文内容\n- EMNLP 2026 long paper 正文限制严格 8 页\n- **修复**: 移 Section 5.5 至 Appendix，压缩 Conclusion\n\n**[W6] Assumption (A3) P(Z=1)=0.5 限制泛化性** [R1✓ R2✓ — 共识]\n- Appendix T 显示 P(Z=1) 偏离 0.5 时 EC-HTE RMSE 比值达 1.06-1.68\n- 实际 NLP 分类中类别不平衡是常态（如仇恨言论检测正类比例远低于 50%）\n- Corollary 4 已有理论放松路径，但实验验证不足，主文讨论不充分\n\n**[W7] 方法论新颖性争议** [核心分歧 — R1 rebut, R2 maintain]\n- **R2 立场**: Theorem 1 是 Frazis-Loewenstein (2003) 标量衰减的自然子群推广（代数上不深刻）；方法组合标准组件（HB Dirichlet-Multinomial + CausalForestDML）；Proposition 3 是定理直接推论。更接近 application paper。\n- **R1 立场**: δ_s·Δτ 乘积结构揭示异质误分类下方向可变的偏差放大——与 F-L 同质衰减本质不同（mixing matrix algebra vs OLS projection）；\"debiasing can hurt\" 充要条件在先前文献无对应；组合动机由 Theorem 1 驱动，是 theory-driven methodology paper。\n- **评审未达成一致**。此分歧直接影响评分（R1=3.5 vs R2=3.0）。\n\n**[W8] 缺乏完全真实世界验证** [R1 部分同意, R2✓]\n- 所有 CATE 为合成注入，即使 \"real LLM CM\" 实验中因果结构仍是合成的\n- R1 指出这在因果推断方法论文中是标准做法（Wager & Athey 2018 等），11 个真实 LLM CM 的 R²=0.975 提供部分外部效度\n- **结构性限制**: CATE ground truth 需 RCT，不可能完全真实\n\n**[W9] κ>100 奇异性保护阈值无消融实验** [R1✓ R2✓ — 共识]\n- Algorithm 1 中阈值 100 的选取无理论推导或 κ∈{50,100,200,500} 消融\n\n### Minor\n\n**[W10] \"estimator-agnostic\" 措辞过强** [R1✓ R2 部分同意]\n- 仅验证 DIM、CausalForest、R-learner 三种估计器；T/X/DR-learner 未涉及\n- 建议改为 \"compatible with a range of HTE estimators\"\n\n**[W11] K 仅探索到 4** [R1✓ R2✓]\n- K≥8 时 per-subgroup expert labels 下降，HB partial pooling 行为可能改变\n\n**[W12] Expert label 成本与替代方案比较缺失** [R2✓, R1 认为超出范围]\n- K=4 需至少 200 expert labels\n- 未与替代方案（扩充训练集/calibration/active learning）比较效率\n\n**[W13] 定理/命题编号混用** [R1✓ R2✓]\n- Theorem 1 → Remark 2 → Proposition 3 → Corollary 4 共享计数器\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下关键问题两位 Reviewer 达成一致：\n1. **CausalForest 覆盖率系统性不足** — critical，需补充 CF-specific SE 验证\n2. **(A2) 对称假设远离现实** — 主文需更显著呈现非对称推广 + 讨论诊断降级\n3. **(A1) 无敏感性分析** — 需提供违反时定量退化分析\n4. **正文超 8 页** — 格式违规，需移 Section 5.5 至 Appendix\n5. **Framing 选择性强调** — Abstract 需平衡呈现 TweetEval 负面结果\n6. **(A3) 等概率限制** — 主文讨论不足\n7. **κ>100 无消融** — 需实验验证\n\n## Reviewer Divergence [REBUT]\n\n1. **技术新颖性**（影响评分的核心分歧）: R1 认为 theory-driven methodology（3.5），R2 认为增量性推广（3.0）\n2. **真实世界验证缺失严重性**: R1=minor-to-major（因果推断标准做法），R2=major（声称实用工具但缺验证）\n3. **格式违规严重性**: R2=critical，R1=major（可快速修复）\n4. **(A2) 严重性**: R1=critical，R2=between critical/major（推广路径存在）\n\n---\n\n## Questions\n\n1. **(A1) 敏感性**: 误分类率与潜在结果相关时，EC-HTE 的偏差和覆盖率如何退化？ [R1✓ R2✓]\n2. **K 扩展**: K=8/16 时 HB 表现和 partial pooling 有效性？ [R1✓ R2✓]\n3. **异常值**: GPT-4o-mini on Civil Comments R²=0.776 的根因？ [R1, R2✓]\n4. **Global 覆盖率**: Table 1 中 Global 覆盖率 0.005 对已发表 CSS 研究的含义？ [R1]\n5. **TweetEval 根因**: EC-HTE 未改善是 Δτ 小、δ_s 小、还是子群定义？ [R2, R1 部分回应]\n6. **Scalability**: HB Gibbs 采样计算时间？变分推断替代？ [R1, R2✓]\n7. **联合 SE**: EC-HTE + PPCI 标准误差如何联合传播？ [R1, R2✓]\n8. **成本效益**: 200 expert labels 与直接扩充训练集/calibration 的效率比较？ [R2]\n\n---\n\n## Missing References\n\n1. **Semenova & Chernozhukov (2021)** \"Debiased machine learning of conditional average treatment effects\" [R1 提出, R2 同意] — CATE debiased estimation 核心理论\n2. **Blackwell, Honaker, and King (2017)** \"A Unified Approach to Measurement Error and Missing Data\" [R2 提出, R1 同意] — 政治科学测量误差统一框架\n3. **LLM Calibration 文献** (temperature scaling, Platt scaling, Adaptive Temperature Scaling) [R2] — 减少子群误分类异质性的替代/补充方案\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求——项目配置中未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (2026-05-22T15:23-15:27) | 0 critical / 3 warning / 9 info\n\n**Warnings:**\n1. **Page 3-7 连续 5 页无 figure/table** — Figure 1 (p2) 到 Figure 2+Table 1 (p8) 之间长达 5 页纯文本+公式段。Section 4 方法部分完全无 display item。建议主文加 method overview 图或将 Algorithm 1 移入主文。\n2. **主文仅 3 个 display items**（2 figures + 1 table），低于实证论文典型密度（5-8 个/9 页）。\n3. **Algorithm 1 (p25) 仅占页面上部 ~40%**，下方大面积空白。建议移入主文 Section 4。\n\n**Info:** Figure 1 偏小（建议 figure*）| Figure 2 热力图清晰 | Table 1 格式规范 | 公式渲染正确 | 参考文献格式统一 | Figure 5 对红绿色盲不够友好（建议补 pattern/hatching）\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分理由:**\n论文解决了一个切实且相关的问题，Theorem 1 的偏差分解干净且正确，实验验证在 NLP 投稿中堪称全面（25 页附录、11 个真实 LLM CM、R²=0.975）。但两个 critical issues 构成主要障碍：(1) CausalForest 覆盖率系统性不足（0.84-0.91 vs 0.95），置信区间不可靠；(2) (A2) 对称假设与真实 LLM 行为（7:1 FPR/FNR）严重不符。多个 major issues 未解决：(A1) 无敏感性分析、正文超 8 页、framing 选择性强调。技术新颖性存在审稿人分歧（R1=3.5 Borderline Conference, R2=3.0 Findings）。\n\n**Reviewer 评分**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)\n\n**置信度**: 4/5\n\n**修订优先级:**\n1. **[Must-Fix]** 补充 CausalForest SE 校准实验（与 DIM Appendix Y 等同验证）\n2. **[Must-Fix]** 主文呈现非对称 general formula + Proposition 3 在非对称下 AUC 降幅讨论\n3. **[Must-Fix]** 压缩正文至 ≤ 8 页（移 Section 5.5 至 Appendix）\n4. **[Should-Fix]** 增加 (A1) 违反时的敏感性分析（sensitivity parameter + simulation）\n5. **[Should-Fix]** Abstract 平衡呈现 TweetEval 负面结果\n6. **[Should-Fix]** κ>100 阈值消融实验\n7. **[Nice-to-Have]** K≥8 实验探索\n8. **[Nice-to-Have]** HB Gibbs 计算时间报告 + scalability 讨论\n\n**升级路径**: 如 Must-Fix 1-3 全部解决 + Should-Fix 4-5 至少部分解决，论文可达 3.5 (Borderline Conference) 水平。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Figure 1 caption 描述可能有误：两次 \"under-correcting\"，疑似应为 \"over-correcting low-error subgroups\" [R2]\n- \"50% of K=2 configurations (260/520)\" 依赖参数网格设计，建议注明或改为 \"a substantial fraction\" [R1✓ R2✓]\n\n### Section 2 (Related Work)\n- 三层技术区分策略有效，但第三个区分点（product structure）略有过度声称——F-L 子群化后可自然产生类似结构 [R2]\n- 缺少 Semenova &amp; Chernozhukov (2021)、Blackwell et al. (2017)、LLM calibration 方法的引用 [R1, R2]\n- 与 F-L (2003) 的公式级对比仍缺失（R10 遗留问题）[R1✓ R2✓]\n\n### Section 3 (Bias Decomposition)\n- Theorem 1 代数正确 [R1 验证]\n- (A5) 应明确说明是简化而非必要条件，避免读者误解 [R2]\n- Proposition 3 AUC=0.86 的评估参数范围/分布未说明 [R2]\n- (A2) Remark 2 仅 4 行过于简略，应更显著呈现非对称推广 [R1✓ R2✓]\n\n### Section 4 (EC-HTE)\n- Gamma(3,1) 超先验经 Appendix G 验证不敏感 [R2✓]\n- κ>100 阈值缺消融 [R1✓ R2✓]\n- Plug-in SE \"small relative to outcome variance\" 在 n_expert=25 时可能不成立 [R2]\n- R̂<1.01 收敛标准可能过宽（Vehtari et al. 2021 建议 <1.005）[R1]\n\n### Section 5 (Experiments)\n- Table 1 信息密度合理 [R2✓]\n- Bias identity R²=0.975 是最有说服力的实证结果 [R1✓ R2✓]\n- TweetEval EC-HTE aggregate RMSE (0.225) > Global (0.107) 需更诚实呈现 [R1✓ R2✓]\n- 合成实验 T~Bernoulli(0.5) 独立于协变量（无混杂），有混杂设置下表现未验证 [R1]\n- Section 5.5 应移至 Appendix（超页） [R1✓ R2✓]\n- Section 5.4 recommended workflow 仅两段，建议扩展为结构化 decision flowchart [R2]\n\n### Section 6 (Conclusion)\n- 偏长（约半页），包含前瞻性内容更适合 Discussion [R2]\n- 位于第 9 页，超页 [R1✓ R2✓]\n\n### Limitations\n- 涵盖关键限制但缺少 \"所有实验使用合成/半合成因果结构\" 的明确声明 [R2]\n\n### Appendix\n- 13+ 个附录与 8 页正文之间存在不匹配，体量可能暗示用量弥补深度 [R2]\n- Appendix Y CausalForest SE 验证缺失是重要遗漏 [R1✓ R2✓]\n- Appendix B Corollary 4 更像 sketch，建议补充 J=3 数值例子 [R1]",
    "project": "ec_hte_llm_annotation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-22T15:49:15.421600+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6b114d432b35fe7a1c2143457ae85b08:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4118
}
```

</details>

---


### Assistant

_source line 816 · 2026-05-22T15:49:21.930286+00:00_

审稿报告已投递至 Research Director。

**Round 11 审稿完成。** 最终评分 **3.0 (Findings)**（R1=3.5, R2=3.0）。

核心发现：
- **2 个 critical**: CausalForest 覆盖率系统性不足（0.84-0.91 vs 0.95）+ (A2) 对称假设远离真实 LLM 行为（7:1 FPR/FNR）
- **7 个 major**: (A1) 无敏感性分析、framing 选择性强调、正文超 8 页、(A3) 等概率限制、方法论新颖性争议、缺真实世界验证、κ>100 无消融
- **核心分歧**: 技术新颖性（R1 认为 theory-driven methodology，R2 认为增量性推广）

Must-Fix 1-3 解决后可升至 3.5 (Borderline Conference)。Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 817 · 2026-05-22T15:49:23.437674+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。主要结论：

- **8 条 Weakness 中 7 条 AGREE、1 条 PARTIALLY AGREE**（W6 关于 "estimator-agnostic"——Appendix S 实际测试了 R-learner 第三种估计器，但总体措辞仍偏强）
- **5 个 Questions 全部 AGREE**
- **Missing References: 1 条 AGREE（Semenova & Chernozhukov 2021）、1 条 REBUT**（treatment assignment measurement error 是不同问题设定，论文研究的是 effect modifier Z 的误分类而非 treatment T 的误分类）
- 与 R1 的主要评分分歧：R1 给 3.5，我维持 3.0，主要因为我对技术新颖性的评估更保守

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 818 · 2026-05-22T15:49:32.796400+00:00_

审稿报告已投递至 Research Director。

**Round 11 审稿完成总结：**

- **Overall: 3.0 (Findings)** | R1=3.5, R2=3.0
- 2 个 critical：CausalForest 覆盖率系统性不足 + (A2) 对称假设与真实 LLM 不符
- 5 个 major：(A1) 无敏感性分析、framing 选择性强调、正文超 8 页、(A3) 等概率限制、κ>100 无消融
- 核心分歧：技术新颖性（R1 认为 theory-driven methodology，R2 认为增量性推广）
- Issue Tracker 已同步更新（17 个 open issues，含 7 个新增）
- 视觉审查已完成（3 warnings：主文连续 5 页无 figure、display items 偏少、Algorithm 1 空白过多）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 79

## Round 79

66 recorded events


### User

_source line 819 · 2026-05-23T06:05:21.731080+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: ec_hte_llm_annotation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings unified)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-23T06:05:29.152996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-23T06:05:29.204002+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-23T06:05:37.536750+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file,WebSearch",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file,WebSearch",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-23T06:05:37.537144+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-23T06:05:41.855511+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-23T06:05:43.211337+00:00_

{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (39 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-027b: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error（准备中）\n- exp-027: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage（准备中）\n\n## 近期结论\n- **exp-036** (success): Bootstrap SE (B=200, re-estimating CM + re-fitting CF per bootstrap) can close the CausalForest under-coverage gap (91% vs nominal 95%) by properly accounting for CM estimation uncertainty that plug-in SE ignores.\n- **exp-037** (success): Temperature scaling reduces per-subgroup misclassification rates but does NOT eliminate heterogeneity (Δπ shrinks from 0.20 to 0.07 but remains nonzero), so EC-HTE is still necessary post-calibration. Calibrated+EC-HTE should achieve the best coverage.\n- **exp-035** (success): EC-HTE with asymmetric CM estimation (full 2x2 FPR/FNR) maintains coverage >=93% under realistic 7:1 FPR/FNR ratios (simulating GPT-4.1 on Civil Comments), and outp
…[truncated 309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-23T06:05:43.713647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-23T06:05:44.266206+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{enumitem}
16	\usepackage{algorithm}
17	\usepackage{algpseudocode}
18	
19	\newtheorem{theorem}{Theorem}
20	\newtheorem{corollary}[theorem]{Corollary}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{remark}[theorem]{Remark}
23	
24	\title{Error-Corrected Heterogeneous Treatment Effects:\\When LLM Annotation Debiasing Hurts}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{theory}
38	
39	\input{method}
40	
41	\input{experiments}
42	
43	\input{conclusion}
44	
45	\input{limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{appendix}
51	
52	%\input{checklist}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-23T06:05:44.366975+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-23T06:05:50.892818+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information related to EMNLP 2026, though the results primarily contain information about 
…[truncated 1229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 6525
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-23T06:05:55.667568+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 831 · 2026-05-23T06:05:56.021091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-23T06:05:57.677760+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-23T06:05:57.728410+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{enumitem}
16	\usepackage{algorithm}
17	\usepackage{algpseudocode}
18	
19	\newtheorem{theorem}{Theorem}
20	\newtheorem{corollary}[theorem]{Corollary}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{remark}[theorem]{Remark}
23	
24	\title{Error-Corrected Heterogeneous Treatment Effects:\\When LLM Annotation Debiasing Hurts}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{theory}
38	
39	\input{method}
40	
41	\input{experiments}
42	
43	\input{conclusion}
44	
45	\input{limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{appendix}
51	
52	%\input{checklist}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 834 · 2026-05-23T06:06:01.894567+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limit and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited page
…[truncated 1020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 6226
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-23T06:06:05.459101+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the search results, here are 
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 9438
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-23T06:06:19.514716+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-23T06:06:20.318282+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Glob",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-23T06:06:20.569719+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-23T06:06:20.720904+00:00_

-rw-r--r-- 1 ubuntu ubuntu 760748 May 23 05:51 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_9/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-23T06:06:25.991230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-23T06:06:26.343029+00:00_

1	\begin{abstract}
2	We derive an exact bias identity for heterogeneous treatment effect (HTE) analysis with LLM-annotated effect modifiers: correcting annotation error with a pooled confusion matrix---standard practice---introduces subgroup-level bias proportional to $\delta_s \cdot \Delta\tau$, the product of each subgroup's misclassification deviation ($\delta_s = \pi_s - \bar{\pi}$) and CATE heterogeneity, verified at $R^2 \geq 0.97$ on both synthetic grids and 11 real LLM confusion matrices.
3	The identity implies that global correction worsens bias in 50\% of $K{=}2$ configurations across our synthetic parameter grid (260/520 $\Delta\pi {\times} \Delta\tau$ cells), with amplification up to 2.86$\times$ (difference-in-means) and 5.9$\times$ ($K{=}4$, CausalForest).
4	Independently, the identity yields a computable diagnostic (AUC $= 0.86$ under symmetric errors) that flags harmful correction using only per-subgroup misclassification rates---actionable without estimating treatment effects.
5	The identity prescribes per-subgroup correction; we provide a hierarchical Bayesian implementation (EC-HTE) that reduces $|\text{bias}|$ from 0.059 to 0.010 under extreme misclassification heterogeneity ($K{=}2$) with nominal coverage ($\geq$0.91), but whose advantage is conditional: when misclassification heterogeneity is moderate and subgroups are unbalanced (e.g., TweetEval), EC-HTE yields comparable bias but higher aggregate RMSE than global correction (0.225 vs.\ 0.124), confirming that the method requires sufficient per-subgroup error-rate heterogeneity.
6	We validate across 520 synthetic configurations (100 Monte Carlo runs each), a semi-synthetic TweetEval experiment ($N{=}5{,}000$), and eight LLMs (open-source 7B--9B and proprietary) across two NLP datasets, confirming both $\Delta\pi$ heterogeneity and the bias identity ($R^2 = 0.975$) on real annotations; EC-HTE is robust to moderate outcome-dependent misclassification ($\gamma \leq 0.2$, coverage $\geq$93.5\%).
7
…[truncated 15 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-23T06:06:26.343395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-23T06:06:26.795293+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.
5	Yet these annotations are not uniformly accurate.
6	\citet{ashwin2025bias} document that LLM misclassification rates vary by up to 5$\times$ across demographic subgroups defined by refugee status, gender, and education level.
7	In a pilot study, GPT-4.1 achieves 85.8\% binary accuracy on TweetEval sentiment, but error rates range from 10.2\% to 20.0\% across text-feature subgroups ($\Delta\pi = 0.098$).
8	When such annotations serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, subgroup-specific errors propagate directly into conditional average treatment effect (CATE) estimates.
9	The resulting bias is not random noise that averages out; it is structured by the same demographic axes that define the research question.
10	Standard correction procedures\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.}, which estimate a single confusion matrix and apply its inverse uniformly, cannot account for this heterogeneity.
11	
12	We formalize this problem and derive an exact bias identity for the correction-induced error.
13	When a pooled confusion matrix is applied to correct subgroup CATEs, it misattributes error across subgroups with an exact product form: the bias in subgroup $s$ equals $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$, where $\delta_s$ is the deviation from the pooled error rate and $\Delta\tau$ is the CATE heterogeneity (Theorem~\ref{thm:bias_identity}).
14	This is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and
…[truncated 4157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-23T06:06:26.795667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-23T06:06:27.297992+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Measurement error and annotation models.}
5	Classical measurement error theory shows that correction via estimated error models can amplify MSE when the error structure is misspecified~\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\cite{hu2008nonparametric}.
6	
7	Three distinctions separate our contribution from prior measurement error analyses.
8	First, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\cite{frazis2003estimating,carroll2006measurement} or confounder~\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.
9	Second, Theorem~\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.
10	Concretely, \citet{frazis2003estimating} derive scalar attenuation $\tilde{\beta} = \beta(1 - \pi_0 - \pi_1)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$---that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.
11	The homogeneous-error setting is a degenerate case: with $K{=}1$, $\delta_s{=}0$ and correction-induced bias vanishes, recovering the classical attenuation result.
12	The algebraic mechanisms also differ: OLS attenuation under misclassified regressors~\cite{frazis2003estimating,blackwell2017unified} versus confusion matrix inversion that redistributes error across subgroups with heterogeneous rates.
13	We empirically verify 
…[truncated 5178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-23T06:06:27.298348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-23T06:06:27.700518+00:00_

1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{theorem}{Theorem}
3	%      \newtheorem{corollary}[theorem]{Corollary}
4	%      \newtheorem{proposition}[theorem]{Proposition}
5	
6	\section{Bias Decomposition: When Debiasing Hurts}
7	\label{sec:theory}
8	
9	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
10	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
11	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
12	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
13	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
14	
15	We state five assumptions maintained throughout.
16	%
17	\begin{itemize}
18	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
19	\item[\textbf{(A2)}] \textit{Symmetric misclassification:} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$.
20	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
21	\item[\textbf{(A4)}] \textit{Non-degeneracy:} $\pi_s \neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.
22	\item[\textbf{(A5)}] \textit{Homogeneous treatment effects across subgroups:} $\tau(z, s) = \tau(z)$ for all $s$, so $\Delta\tau = \ta
…[truncated 8162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-23T06:06:27.700971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-23T06:06:29.006250+00:00_

1	\section{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
2	\label{sec:method}
3	
4	Theorem~\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.
5	EC-HTE corrects subgroup-level misclassification bias in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.
6	The complete procedure is summarized in Algorithm~\ref{alg:echte} (Appendix~\ref{app:algorithm}).
7	
8	\subsection{Hierarchical Bayes Confusion Matrix Estimation}
9	
10	We place a Dirichlet-Multinomial hierarchical model over the confusion matrices $\{C_s\}_{s=1}^K$.
11	For each subgroup $s$, row $j$ of $C_s$ has a Dirichlet prior $\text{Dir}(\alpha_0 \cdot \mathbf{e}_j)$, where $\mathbf{e}_j$ is the $j$-th standard basis vector and $\alpha_0 > 0$ is a shared concentration parameter.
12	A $\text{Gamma}(3, 1)$ hyperprior on $\alpha_0$ controls the strength of partial pooling across subgroups: large $\alpha_0$ pulls subgroup estimates toward the identity matrix (low error), while small $\alpha_0$ allows subgroup-specific rates to dominate.
13	This partial pooling---a James-Stein shrinkage effect---borrows strength across subgroups, reducing variance for small subgroups while preserving heterogeneity where data support it.
14	
15	Posterior inference uses Gibbs sampling (convergence diagnostics in Appendix~\ref{app:algorithm}).
16	HB estimation outperforms stratified MLE in 87.5\% of configurations (21 of 24) across the experimental grid (Section~\ref{sec:ec_hte_eval}), with the largest gains when $n_{\text{expert}} / K < 100$.
17	The advantage requires $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ per subgroup; below this threshold, stratified MLE is preferred because the hierarchical model lacks sufficient observations for stable shrink
…[truncated 4427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-23T06:06:29.207662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-23T06:06:29.258548+00:00_

1	\section{Experiments}
2	
3	\subsection{Setup}
4	
5	We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 MC runs) and semi-synthetic (TweetEval sentiment~\cite{barbieri2020tweeteval}, $K{=}4$ unbalanced subgroups, $\pi \in \{0.05, 0.10, 0.15, 0.25\}$) DGPs; full specifications in Appendix~\ref{app:dgp}.
6	
7	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2024dsl} with homogeneous error), (3) \textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \textit{HB EC-HTE} (our method), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
8	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
9	Primary metrics are $|\text{bias}|$, RMSE, and 95\% CI coverage, averaged across subgroups and 100 MC runs.
10	Robustness validation covers hate speech, six OpenAI models, subgroup misspecification, asymmetric confusion matrices, confounded treatment, and outcome-dependent misclassification (all $\geq$93.5\% coverage; Appendices~\ref{app:hatespeech}--\ref{app:a1_sensitivity}).
11	
12	\subsection{Empirical Validation of the Bias Identity}
13	\label{sec:bias_mechanism}
14	
15	We verify Theorem~\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\Delta\pi \in [0, 0.25]$, $\Delta\tau \in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\ref{app:dgp}).
16	Regressing observed subgroup bias on $\delta_s \cdot \Delta\tau / (1{-}2\bar{\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.974$ ($K{=}4$); residual variance reflects MC noise ($R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\ref{app:classimbalance}).
17	Global correction worsens bias in 50\% of $K{=}2$ configurations (260/520, excluding $\Delta\pi{=}0$), with amplification reaching 2.86$\times$ ($K{=}2$) and 2.41$\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the amplification surface.
18	
19	\begin{figure*}[t]
20	\cen
…[truncated 4703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-23T06:06:29.359407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-23T06:06:29.610711+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We derived an exact bias identity (Theorem~\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup-level bias proportional to $\delta_s \cdot \Delta\tau$, worsening CATE estimates in 50\% of $K{=}2$ configurations.
4	EC-HTE provides subgroup-stratified correction via hierarchical Bayes; the companion diagnostic (Proposition~\ref{prop:debiasing_hurts}; AUC $= 0.86$) flags harmful correction using only per-subgroup misclassification rates.
5	EC-HTE's advantage requires sufficient $\Delta\pi$ and per-subgroup expert budget; when either is marginal, global correction is competitive.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-23T06:06:29.611191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-23T06:06:29.862556+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	EC-HTE requires $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ per subgroup for stable hierarchical Bayesian estimation.
5	For $K{=}2$, EC-HTE remains effective even at $P(Z{=}1) = 0.1$ (Appendix~\ref{app:classimbalance}); for $K{=}4$, $P(Z{=}1) \geq 0.3$ is needed to approach breakeven with global correction at $n_{\text{expert}}{=}250$.
6	Even above this threshold, stratification incurs a variance cost: at $K{=}4$, extreme heterogeneity, and $n_{\text{expert}} \leq 100$, CausalForest RMSE reaches 3.5$\times$ that of the naive estimator.
7	The method also requires moderate baseline classifier accuracy per subgroup; when any subgroup's FNR or FPR approaches 0.5, the confusion matrix row approaches a uniform distribution and inversion amplifies noise (Appendix~\ref{app:semireal}), as confirmed independently in the hate speech case study (Appendix~\ref{app:hatespeech}).
8	These failure modes interact: high per-subgroup error-rate variance combined with low minority prevalence $P(Z{=}1)$ jointly reduces effective per-subgroup expert labels for the positive class, compounding both sources of estimation error.
9	Additionally, our main semi-synthetic experiments use constant treatment effects across subgroups; a supplementary heterogeneous-$\tau$ DGP (Appendix~\ref{app:multilm_opensource}) shows that EC-HTE achieves targeted bias and RMSE improvement in subgroups with large $\Delta\tau$, though aggregate RMSE remains comparable to global correction.
10	At $K{=}8$ with $n_{\text{expert}}{=}250$ (${\approx}31$ labels/subgroup), EC-HTE maintains nominal coverage (95.6\%) but RMSE exceeds global correction, establishing $K{=}8$ as a scalability boundary under fixed budget (Appendix~\ref{app:k8_subgroups}).
11	Hierarchical pooling of confusion matrices across related subgroups may relax the per-subgroup budget requirement; we leave this extension to future work.
12	
13	Assumption~(A1) (conditional independe
…[truncated 4104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-23T06:06:29.863009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-23T06:06:30.116419+00:00_

File content (35362 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-23T06:06:36.643704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-23T06:06:37.096337+00:00_

1	\section{EC-HTE Procedure}
2	\label{app:algorithm}
3	
4	\begin{algorithm}[t]
5	\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
6	\label{alg:echte}
7	\begin{algorithmic}[1]
8	\Require Observations $\{(Y_i, W_i, \hat{Z}_i, X_i)\}_{i=1}^N$; expert labels $\{Z_j^*\}_{j=1}^{n_{\text{expert}}}$; subgroup map $S: \mathcal{X} \to \{1,\ldots,K\}$
9	\Ensure Corrected CATE estimates $\hat{\tau}(z)$ with variance-adjusted CIs
10	\Statex
11	\State \textbf{Preconditions:} verify $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ and $\max_s(\text{FPR}_s, \text{FNR}_s) < 0.5$; if either fails, use global correction
12	\Statex
13	\State \textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}
14	\For{$s = 1, \ldots, K$}
15	    \State $C_s[j,\cdot] \sim \mathrm{Dir}(\alpha_0 \cdot \mathbf{e}_j)$, \; $\alpha_0 \sim \mathrm{Gamma}(3,1)$
16	    \State Gibbs sampler (4 chains, 4000 iter) on $\{(\hat{Z}_j, Z_j^*) : S_j = s\}$
17	    \State $\hat{C}_s \gets$ posterior mean; verify $\hat{R} < 1.01$
18	\EndFor
19	\Statex
20	\State \textbf{Step 2: Correct observed outcome moments}
21	\For{$s = 1, \ldots, K$}
22	    \If{$\kappa(\hat{C}_s) > 100$} $\hat{C}_s \gets \bar{C}$ \Comment{singularity guard}
23	    \EndIf
24	    \State $\tilde{\boldsymbol{\mu}}_s \gets \hat{C}_s^{-1} \hat{\boldsymbol{\mu}}_s$
25	\EndFor
26	\Statex
27	\State \textbf{Step 3: CausalForestDML with variance-adjusted SEs}
28	\State Train CausalForest (honest splitting) on corrected labels
29	\State $\mathrm{se}_{\mathrm{adj},i} \gets \sqrt{\mathrm{diag}(\hat{C}_{S_i}^{-1}\, \mathrm{diag}(\mathrm{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$
30	\State \Return $\hat{\tau}(z)$ with 95\% CIs from $\mathrm{se}_{\mathrm{adj}}$
31	\end{algorithmic}
32	\end{algorithm}
33	
34	\subsection{Condition Number Guard Ablation}
35	\label{app:kappa_ablation}
36	
37	The singularity guard in Algorithm~\ref{alg:echte} (line~6) falls back to global correction when $\kappa(\hat{C}_s) > 100$.
38	We verify that this thres
…[truncated 20813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-23T06:06:37.096701+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-23T06:06:37.147173+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-23T06:06:44.075383+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review configuration"
  }
}
```

</details>

---


### Tool call

_source line 863 · 2026-05-23T06:06:44.126598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": "300",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "offset": "300",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 864 · 2026-05-23T06:06:44.178209+00:00_

300	We sweep $n_{\text{expert}} \in \{25, 50, 75, 100, 150, 250\}$ under extreme heterogeneity ($\Delta\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).
301	Table~\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.
302	
303	\begin{table}[h]
304	\centering
305	\caption{RMSE across expert budgets under extreme heterogeneity.
306	HB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:
307	$n_{\text{expert}}{=}50$ for $K{=}2$ and $n_{\text{expert}}{=}75$ for $K{=}4$.}
308	\label{tab:budget_sensitivity}
309	\small
310	\begin{tabular}{crrrrc}
311	\toprule
312	$K$ & $n_{\text{expert}}$ & Global & Strat.\ MLE & HB EC-HTE & HB vs.\ MLE \\
313	\midrule
314	2 & 25 & \textbf{0.101} & 0.256 & 0.269 & $+4.9\%$ \\
315	2 & 50 & \textbf{0.088} & 0.275 & 0.231 & $\mathbf{-16.1\%}$ \\
316	2 & 75 & 0.084 & 0.091 & \textbf{0.089} & $-1.9\%$ \\
317	2 & 100 & 0.083 & 0.085 & \textbf{0.084} & $-0.8\%$ \\
318	2 & 150 & 0.081 & 0.077 & \textbf{0.077} & $-0.4\%$ \\
319	2 & 250 & 0.080 & 0.075 & \textbf{0.074} & $-0.1\%$ \\
320	\midrule
321	4 & 25 & \textbf{0.129} & 0.401 & 0.612 & $+52.5\%$ \\
322	4 & 50 & \textbf{0.117} & 0.380 & 0.470 & $+23.8\%$ \\
323	4 & 75 & \textbf{0.112} & 0.221 & 0.211 & $\mathbf{-4.4\%}$ \\
324	4 & 100 & \textbf{0.112} & 0.215 & 0.212 & $-1.3\%$ \\
325	4 & 150 & \textbf{0.109} & 0.157 & 0.152 & $-3.6\%$ \\
326	4 & 250 & \textbf{0.108} & 0.127 & 0.126 & $-1.0\%$ \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	Three regimes emerge.
332	At very low budgets ($n_{\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.
333	HB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with
…[truncated 17598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-23T06:06:44.178580+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-23T06:06:48.445393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": "600",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "offset": "600",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-23T06:06:48.546525+00:00_

600	EC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\text{expert}}{=}1{,}000$, consistent across all four models.
601	Global correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\Delta\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\ref{sec:budget}.
602	
603	\begin{table}[t]
604	\centering
605	\caption{Semi-synthetic budget sweep ($K{=}2$, $\Delta\tau{=}0.3$, 50 MC runs\protect\footnote{Appendix experiments use 50 MC replications unless otherwise noted; all main-text results use 100.}). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}
606	\label{tab:multilm_budget}
607	\small
608	\begin{tabular}{lcccc}
609	\toprule
610	Model & $\Delta\pi_{K{=}2}$ & Naive Cov.\ & HB Cov.\ ($n{=}1000$) & Crossover \\
611	\midrule
612	Llama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\
613	Qwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\
614	Gemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\
615	Mistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\
616	\midrule
617	\textit{Average} & --- & \textit{0.714} & \textit{0.939} & --- \\
618	\bottomrule
619	\end{tabular}
620	\end{table}
621	
622	\paragraph{Gemma boundary case.}
623	Gemma-2-9B triggers the Proposition~\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\texttt{False\_medium} FNR $= 0.437$).
624	At small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\times$ naive), illustrating the budget guideline from Appendix~\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.
625	At $n \geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.
626	
627	\paragraph{Heterogeneous-$\tau$ DGP.}
628	To assess whether the
…[truncated 18616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-23T06:06:52.463536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": "899",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "offset": "899",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-23T06:06:52.464238+00:00_

899	
900	To verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\% toxic) from Civil Comments~\cite{borkan2019nuanced}, a toxicity detection dataset.
901	Subgroups are defined by \texttt{text\_length\_bin} $\times$ \texttt{has\_question} ($K{=}4$): S0 (long, no question, 38.8\%), S1 (long, question, 11.4\%), S2 (short, no question, 33.7\%), S3 (short, question, 16.1\%).
902	Subgroup features were chosen a priori based on observable text properties; no feature search was performed.
903	Three proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.
904	
905	Table~\ref{tab:civil_cm} reports per-subgroup FPR and FNR.
906	We define $\Delta\pi = \max_s \pi_s - \min_s \pi_s$, where $\pi_s$ is the overall misclassification rate for subgroup $s$.
907	All three models exhibit $\Delta\pi > 0.05$, with overall heterogeneity $\Delta\pi \in [0.113, 0.160]$---comparable to the $\Delta\pi \in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\ref{app:multilm_opensource}).
908	GPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\in [0.42, 0.61]$ vs.\ FNR $\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).
909	The consistent presence of $\Delta\pi$ heterogeneity across two NLP tasks, seven LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.
910	
911	\begin{table}[h]
912	\centering
913	\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\Delta$ denotes max $-$ min acros
…[truncated 21142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-23T06:06:56.183332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": "1198",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "offset": "1198",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-23T06:06:56.184082+00:00_

1198	\paragraph{DGP.}
1199	$N{=}5{,}000$, $K{=}2$, $\pi = [0.05, 0.25]$, $n_{\text{expert}}{=}250$, 100 MC replications.
1200	A covariate $X \sim \mathcal{N}(0,1)$ confounds both treatment and outcome:
1201	$T \sim \text{Bernoulli}(\sigma(\beta X))$ with $\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),
1202	$Y = 1 + 0.5 Z + 0.3 X + \tau(Z) \cdot T + \varepsilon$, $\varepsilon \sim \mathcal{N}(0,1)$.
1203	Treatment effects are $\tau(Z{=}0){=}0$, $\tau(Z{=}1){=}0.3$.
1204	The IPW-DIM estimator uses \emph{oracle propensity} $e(X) = \sigma(\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.
1205	
1206	\begin{table}[h]
1207	\centering
1208	\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\beta{=}0.5$, 100 MC).}
1209	\label{tab:confounded_dgp}
1210	\small
1211	\begin{tabular}{lccc}
1212	\toprule
1213	Method & Coverage & RMSE & $|\text{Bias}|$ \\
1214	\midrule
1215	Oracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\
1216	HB EC-HTE              & 0.950 & 0.086 & 0.068 \\
1217	Global                  & 0.930 & 0.087 & 0.071 \\
1218	Strat MLE               & 0.950 & 0.087 & 0.069 \\
1219	Naive                   & 0.863 & 0.083 & 0.066 \\
1220	\bottomrule
1221	\end{tabular}
1222	\end{table}
1223	
1224	EC-HTE achieves 95.0\% coverage, within 0.7pp of the oracle (94.3\%), confirming that confusion matrix correction and propensity weighting compose without interference.
1225	The improvement is most pronounced in the high-error subgroup ($\pi{=}0.25$): EC-HTE coverage is 96.0\% vs.\ naive 78.5\% ($+$17.5pp).
1226	Global coverage (93.0\%) falls below the correction methods (95.0\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.
1227	
1228	\paragraph{Sensitivity to confounding strength and propensity estimation.}
1229	We sweep $\beta \in \{0.25, 0.5, 1.0, 2.0\}$ and compare oracle propensity ($e(X) = \sigma(\beta X)$) with estimated propensity (logistic regr
…[truncated 7695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-23T06:07:10.288319+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-23T06:07:10.338910+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-23T06:07:16.265457+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-23T06:07:16.567282+00:00_

&lt;persisted-output>
Output too large (49.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bnmvkinjj.txt

Preview (first 2KB):
issues:
  # === RESOLVED (prior rounds, unchanged) ===
  - id: "R1-N1"
    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 2
    action_items: []
    resolution: "重新推导为精确恒等式"
    resolution_round: 0

  - id: "R2-W8"
    summary: "Proposition 1 限于 K=2"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "Theorem 1 适用一般 K"
    resolution_round: 0

  - id: "R1-N2"
    summary: "Real data ground truth CATE 来源不明"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "恰当定位为 illustrative application"
    resolution_round: 0

  - id: "R1-N3"
    summary: "HB 模型规格严重不完整"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "完整 MCMC 规格"
    resolution_round: 0

  - id: "JOINT-W4"
    summary: "相关工作严重遗漏"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "30+ 引用覆盖"
    resolution_round: 0

  - id: "JOINT-W3"
    summary: "信息密度过高"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "主文精简至合理密度"
    resolution_round: 0

  - id: "R2-W7"
    summary: "真实数据验证单薄"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_r
…[truncated 320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-23T06:07:16.718447+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
  "description": "Check existing review reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-23T06:07:16.769093+00:00_

round_0.md
round_1.md
round_2.md
round_3.md
round_4.md
round_5.md
round_6.md
round_7.md
round_8.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-23T06:07:38.051735+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-23T06:07:58.147330+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20095
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-23T06:07:58.298310+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题：Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\n- 论文路径：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_9/submitted.pdf\n- 目标 venue：EMNLP 2026 (ARR May cycle)\n- 截止日期：2026-05-25\n\n## Venue 要求\n- Long paper：8 页正文 + 无限参考文献\n- 模板：ACL style（`\\usepackage[review]{acl}`）\n- 匿名：double-blind\n- Limitations section：必需，不计入页数\n- Appendix：允许，参与审稿\n\n## 你的审查侧重\n\n**方法严谨性**：\n1. Theorem 1（Bias Decomposition Identity）的推导是否正确？假设 (A1)-(A5) 是否合理、充分、必要？\n2. Proposition 1（Debiasing Can Increase Bias）的条件是否严谨？AUC=0.86 的 claim 是否有足够支撑？\n3. Corollary（Multi-class Extension、A5 Relaxation）是否正确？\n4. 层次贝叶斯模型（Dirichlet-Multinomial + Gamma hyperprior）的设定是否标准？MCMC 收敛诊断是否充分？\n5. 方差传播公式（SE propagation through C_s^{-1}）是否正确？plug-in SE 的局限性是否充分讨论？\n\n**实验设计**：\n1. 合成数据 DGP 是否合理、是否存在对 EC-HTE 有利的隐含偏好？\n2. 半合成 TweetEval 实验是否恰当？CATE injection 方法是否引入 artifact？\n3. 520 个配置的参数网格是否足够覆盖有意义的参数空间？\n4. 100 MC runs 是否足够？Monte Carlo SE 是否报告？\n5. baseline 比较是否公平？PPI/DSL/PPCI 的等价性声明是否准确？\n6. 统计显著性检验（paired t-test vs z-test）是否恰当？p 值解读是否保守？\n7. Coverage 和 RMSE 的报告方式是否可能掩盖子组层面的异质性？\n8. CausalForest 实验的超参数是否合理？是否进行了敏感性分析？\n\n**可复现性**：\n1. 代码和数据承诺是否充分？\n2. 算法描述是否足够详细以供复现？\n\n请以结构化格式输出审稿意见：Summary → Strengths → Weaknesses（逐条编号，标注 severity: must-fix / should-fix / minor） → Questions → Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题：Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\n- 论文路径：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_9/submitted.pdf\n- 目标 venue：EMNLP 2026 (ARR May cycle)\n- 截止日期：2026-05-25\n\n## Venue 要求\n- Long paper：8 页正文 + 无限参考文献\n- 模板：ACL style（`\\usepackage[review]{acl}`）\n- 匿名：double-blind\n- Limitations section：必需，不计入页数\n- Appendix：允许，参与审稿\n\n## 你的审查侧重\n\n**方法严谨性**：\n1. Theorem 1（Bias Decomposition Identity）的推导是否正确？假设 (A1)-(A5) 是否合理、充分、必要？\n2. Proposition 1（Debiasing Can Increase Bias）的条件是否严谨？AUC=0.86 的 claim 是否有足够支撑？\n3. Corollary（Multi-class Extension、A5 Relaxation）是否正确？\n4. 层次贝叶斯模型（Dirichlet-Multinomial + Gamma hyperprior）的设定是否标准？MCMC 收敛诊断是否充分？\n5. 方差传播公式（SE propagation through C_s^{-1}）是否正确？plug-in SE 的局限性是否充分讨论？\n\n**实验设计**：\n1. 合成数据 DGP 是否合理、是否存在对 EC-HTE 有利的隐含偏好？\n2. 半合成 TweetEval 实验是否恰当？CATE injection 方法是否引入 artifact？\n3. 520 个配置的参数网格是否足够覆盖有意义的参数空间？\n4. 100 MC runs 是否足够？Monte Carlo SE 是否报告？\n5. baseline 比较是否公平？PPI/DSL/PPCI 的等价性声明是否准确？\n6. 统计显著性检验（paired t-test vs z-test）是否恰当？p 值解读是否保守？\n7. Coverage 和 RMSE 的报告方式是否可能掩盖子组层面的异质性？\n8. CausalForest 实验的超参数是否合理？是否进行了敏感性分析？\n\n**可复现性**：\n1. 代码和数据承诺是否充分？\n2. 算法描述是否足够详细以供复现？\n\n请以结构化格式输出审稿意见：Summary → Strengths → Weaknesses（逐条编号，标注 severity: must-fix / should-fix / minor） → Questions → Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-23T06:08:17.703950+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19405
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-23T06:08:17.956023+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\n- 论文路径：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_9/submitted.pdf\n- 目标 venue：EMNLP 2026 (ARR May cycle)\n- 截止日期：2026-05-25\n\n## Venue 要求\n- Long paper：8 页正文 + 无限参考文献\n- 模板：ACL style（`\\usepackage[review]{acl}`）\n- 匿名：double-blind\n- Limitations section：必需，不计入页数\n- Appendix：允许，参与审稿\n\n## 你的审查侧重\n\n**新颖性**：\n1. Bias decomposition identity（Theorem 1）相对于经典测量误差文献（Fuller 1987, Carroll 2006, Frazis & Loewenstein 2003）的增量贡献是什么？\"exact identity\"的 claim 是否过度？\n2. EC-HTE 本质上是 per-subgroup confusion matrix inversion + hierarchical Bayes——这在技术上是否足够新颖？与 Dawid & Skene (1979) 的 confusion matrix estimation 有何本质区别？\n3. 与 PPI (Angelopoulos 2023)、DSL (Egami 2024)、PPCI (Sui 2026) 的关系是否清晰界定？\"none corrects bias when the mismeasured variable is the effect modifier\" 的 claim 是否准确？\n4. diagnostic（Proposition 1）作为独立贡献是否有足够价值？AUC=0.86 在合成数据 vs AUC=0.63 在真实数据的差距是否削弱了这一贡献？\n\n**完整性**：\n1. 真实数据验证的深度——论文依赖合成和半合成实验，真实 RCT + ground-truth CATE 的缺失是否构成重大局限？\n2. 论文声称的 applicability conditions 是否足够清晰、实用？\n3. Limitations section 是否覆盖了所有重要局限？是否遗漏了关键风险？\n4. 附录是否过于庞大？是否有材料应该移到主文或删除？\n5. 论文是否对 negative results（TweetEval、hate speech case study）给予了足够的诚实讨论？\n\n**写作质量**：\n1. Abstract 是否信息密度过高？是否能让非专业读者理解核心贡献？\n2. Introduction 的叙事结构是否清晰？motivation → problem → solution → contribution 的逻辑链是否连贯？\n3. 符号使用是否一致？是否有未定义的符号？\n4. Figure 1 和 Figure 2 的信息传达是否有效？\n5. Table 1（main results）的组织是否清晰？是否突出了关键发现？\n6. Related Work 的定位是否准确？是否过于 defensive 或 aggressive？\n7. 论文的 framing（\"When LLM Annotation Debiasing Hurts\"）是否 clickbait-ish？是否与实际内容匹配？\n\n**格式合规**：\n1. 正文是否在 8 页内？\n2. 是否有匿名性泄露？\n3. 引用格式是否符合 ACL 标准？\n4. Limitations section 是否存在且格式正确？\n\n请以结构化格式输出审稿意见：Summary → Strengths → Weaknesses（逐条编号，标注 severity: must-fix / should-fix / minor） → Questions → Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\n- 论文路径：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_9/submitted.pdf\n- 目标 venue：EMNLP 2026 (ARR May cycle)\n- 截止日期：2026-05-25\n\n## Venue 要求\n- Long paper：8 页正文 + 无限参考文献\n- 模板：ACL style（`\\usepackage[review]{acl}`）\n- 匿名：double-blind\n- Limitations section：必需，不计入页数\n- Appendix：允许，参与审稿\n\n## 你的审查侧重\n\n**新颖性**：\n1. Bias decomposition identity（Theorem 1）相对于经典测量误差文献（Fuller 1987, Carroll 2006, Frazis & Loewenstein 2003）的增量贡献是什么？\"exact identity\"的 claim 是否过度？\n2. EC-HTE 本质上是 per-subgroup confusion matrix inversion + hierarchical Bayes——这在技术上是否足够新颖？与 Dawid & Skene (1979) 的 confusion matrix estimation 有何本质区别？\n3. 与 PPI (Angelopoulos 2023)、DSL (Egami 2024)、PPCI (Sui 2026) 的关系是否清晰界定？\"none corrects bias when the mismeasured variable is the effect modifier\" 的 claim 是否准确？\n4. diagnostic（Proposition 1）作为独立贡献是否有足够价值？AUC=0.86 在合成数据 vs AUC=0.63 在真实数据的差距是否削弱了这一贡献？\n\n**完整性**：\n1. 真实数据验证的深度——论文依赖合成和半合成实验，真实 RCT + ground-truth CATE 的缺失是否构成重大局限？\n2. 论文声称的 applicability conditions 是否足够清晰、实用？\n3. Limitations section 是否覆盖了所有重要局限？是否遗漏了关键风险？\n4. 附录是否过于庞大？是否有材料应该移到主文或删除？\n5. 论文是否对 negative results（TweetEval、hate speech case study）给予了足够的诚实讨论？\n\n**写作质量**：\n1. Abstract 是否信息密度过高？是否能让非专业读者理解核心贡献？\n2. Introduction 的叙事结构是否清晰？motivation → problem → solution → contribution 的逻辑链是否连贯？\n3. 符号使用是否一致？是否有未定义的符号？\n4. Figure 1 和 Figure 2 的信息传达是否有效？\n5. Table 1（main results）的组织是否清晰？是否突出了关键发现？\n6. Related Work 的定位是否准确？是否过于 defensive 或 aggressive？\n7. 论文的 framing（\"When LLM Annotation Debiasing Hurts\"）是否 clickbait-ish？是否与实际内容匹配？\n\n**格式合规**：\n1. 正文是否在 8 页内？\n2. 是否有匿名性泄露？\n3. 引用格式是否符合 ACL 标准？\n4. Limitations section 是否存在且格式正确？\n\n请以结构化格式输出审稿意见：Summary → Strengths → Weaknesses（逐条编号，标注 severity: must-fix / should-fix / minor） → Questions → Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-23T06:08:19.414995+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1458
}
```

</details>

---


### Assistant

_source line 884 · 2026-05-23T06:08:25.849017+00:00_

视觉审查 Agent 已派发，Reviewer 1 和 Reviewer 2 已启动。等待审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 80

## Round 80

2 recorded events


### User

_source line 885 · 2026-05-23T06:16:19.719119+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 论文识别了一个真实且重要的问题（全局混淆矩阵校正在 subgroup 层面引入 HTE 偏差），理论框架干净、实验覆盖广泛，但核心技术贡献的新颖性有限（per-subgroup CM inversion 是识别问题后的自然解），diagnostic 的实际性能严重退化削弱了其作为独立贡献的价值。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Theorem 1 正确且证明清晰；EC-HTE 在假设下 sound；但 diagnostic 在真实数据退化严重（AUC 0.86→0.63），削弱 practical soundness |
| Excitement | 3/5 | 问题重要且及时（LLM 替代人工标注是大趋势），但解决方案技术上直截了当，影响范围局限于 HTE+LLM annotation 的特定 niche |
| Reproducibility | 4/5 | Algorithm 1 明确；实验设置详尽（520 synthetic configs, 100 MC runs）；代码承诺 acceptance 后释放 |
| Confidence | 4/5 | 熟悉测量误差、因果推断和 NLP 标注的交叉领域 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] Diagnostic（Proposition 3）作为"independently useful"贡献的 claim 被实际性能严重削弱
- 具体位置：Abstract（"the identity yields a comparable diagnostic (AUC = 0.86)"）; Section 5.4 (p.8); Section 9 (p.9)
- 问题：Abstract 和 Introduction 将 diagnostic 列为独立贡献之一（"Independently, the identity yields a comparable diagnostic"），但主文和附录显示：
  - 合成数据 AUC = 0.86（对称误差，p.8）
  - 真实 LLM 混淆矩阵 AUC = 0.63（p.9）
  - K=2 时 AUC 降至 0.03，diagnostic **反向预测**（p.9："the diagnostic anti-predicts"）
  - Appendix J 显示 K≥4 时 AUC=0.82，但 K=2 是最常见的实际设置（二分类）
  主文仅用一段话（p.9 顶部）讨论了这一退化，且未给出 K=2 场景下的替代方案。Abstract 中报告 AUC=0.86 而不提 real-data degradation，构成选择性报告。
- 为什么影响接收：如果 diagnostic 在最常见的实际设置下不可靠，将其包装为独立贡献会误导实践者。这影响论文 claim 的诚实性。
- 建议修改方向：(a) Abstract 中加入 real-data AUC 的限定（如"AUC=0.86 under synthetic symmetric errors; degrades under asymmetric real-world confusion matrices"）；(b) 将 diagnostic 降级为"在特定条件下有用的辅助工具"而非独立贡献；(c) 在 Section 5.4 讨论 K=2 时的替代决策策略。

**N2** [critical] 缺乏真实因果数据集的验证——所有 ground-truth CATE 均来自合成或半合成 DGP
- 具体位置：Section 5 (Experiments, p.7); Appendix E (Semi-Synthetic DGP); Appendix M (Hate Speech Case Study)
- 问题：论文的实验验证结构为：
  - 纯合成（Section 5.1-5.2）：N=5,000, 人工控制 Δτ 和 δ_s
  - 半合成（Section 5.3, TweetEval）：真实文本特征 + 人工注入的治疗效应
  - 真实 LLM 混淆矩阵（Sections V, W, X）：真实 CM 应用于合成 outcome DGP
  - 仇恨言论案例（Appendix M）：真实数据但**无 ground-truth CATE**
  没有任何实验使用真实 RCT 数据 + 已知 ground-truth CATE。论文在 Abstract 中声称 "verified empirically with H⁰ = 0.991 (K=4) on synthetic grids, and H⁰ = 0.974 (K=4) on ... 11 real LLM confusion matrices"——但 H⁰ 的验证用的仍是合成 outcome。
- 为什么影响接收：因果推断论文的核心主张是"在实际因果估计中改善偏差"。如果所有 ground-truth CATE 都来自研究者自己设计的 DGP，则无法排除 EC-HTE 的优势仅存在于满足其假设的人工场景中。
- 建议修改方向：(a) 在 Limitations 中显著承认这一局限；(b) 讨论为什么在当前 NLP + causal inference 交叉领域获取真实 ground-truth CATE 数据是困难的；(c) 考虑使用经典因果推断基准数据集（如 IHDP, LaLonde）配合文本特征来提供更接近真实的验证。

**N3** [critical] Theorem 1 的"exact identity"framing 可能过度——需更清晰界定相对于经典测量误差文献的增量贡献
- 具体位置：Abstract（"We derive an exact bias identity"）; Section 3 (p.4, Theorem 1); Section 2 (Related Work, p.2-3); Appendix F
- 问题：Theorem 1 的数学内容是：将全局混淆矩阵应用于 subgroup-specific 观测值时，偏差等于 δ_s · Δτ/(1-2π)。证明（Appendix B）仅需几行矩阵乘法。论文在 Related Work (p.2-3) 讨论了三个区分点：
  1. 研究 effect modifier misclassification 而非 regressor
  2. 刻画 correction-induced bias 而非 attenuation
  3. subgroup-specific 且可能 sign-reversing
  这些区分是合理的。但问题在于：
  - Frazis & Loewenstein (2003) 已经推导了 binary misclassified variable 的标量衰减 β̂ = β(1-π₀-π₁)。Theorem 1 本质上是将此结果推广到"全局 vs. per-subgroup 校正"的差异，并应用于 CATE function 而非 regression coefficient。
  - "exact identity"一词暗示数学深度，但等式 (1)-(2) 在技术上是恒等式推导（exact 指不是近似，而非数学上困难）。
  Appendix F 对此讨论得当，但主文中的 framing（尤其是 Abstract 的"We derive an exact bias identity"）可能让读者高估数学贡献。
- 为什么影响接收：如果审稿人认为技术贡献仅是经典结果在新场景的直接推广，可能影响 novelty 评分。
- 建议修改方向：(a) 主文中更明确地说明"novelty 在于识别 effect modifier misclassification 这一此前被忽视的问题并将经典框架适配到 HTE estimation"；(b) 在 Section 3 讨论 Theorem 1 时，增加一句承认代数推导的直接性，强调贡献在于 formalization 而非数学技巧。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] EC-HTE 方法本身的技术新颖性有限——per-subgroup confusion matrix inversion + hierarchical Bayes 是识别问题后的自然解
- 具体位置：Section 4 (p.6); Algorithm 1 (p.29)
- 问题：一旦识别了"全局校正在 subgroup 层面引入偏差"这个问题，解决方案几乎是显而易见的：按 subgroup 估计混淆矩阵，然后分别校正。Hierarchical Bayes 的使用（Dirichlet-Multinomial + Gibbs sampler）是 confusion matrix estimation 的标准做法。论文的贡献主要在 problem identification + careful engineering（singularity guard, condition number monitoring, Laplace smoothing），而非方法论创新。
- 建议：坦诚地将方法贡献定位为"careful adaptation of established techniques to an underexplored problem"，而非暗示方法论突破。

**W2** [warning] 关于 per-subgroup expert label 获取的实际成本讨论不足
- 具体位置：Section 4.1 (p.6); Algorithm 1 preconditions (p.29); Appendix I (Budget Sensitivity)
- 问题：EC-HTE 要求 n_expert × P(Z_minority)/K ≥ 25。对于 K=4 subgroups，P(Z_minority)=0.25，需要 n_expert ≥ 400。Appendix I 的 budget sweep 使用 n_expert ∈ {25, 50, 75, 100, 150, 250}，Table 3 显示在 n_expert=25 时 RMSE 显著恶化。但论文未讨论：获取 400+ 条 per-subgroup 专家标注的成本是否合理？如果专家预算这么充裕，为什么不直接用更多专家标注来减少对 LLM 的依赖？这一 cost-benefit 分析的缺失降低了 practical contribution 的说服力。
- 建议：在 Limitations 或 Section 4 中增加 cost-benefit 讨论，比较 EC-HTE（少量专家标注 + LLM 大规模标注 + correction）与纯专家标注的预期成本。

**W3** [warning] Assumption (A1) 的敏感性分析范围有限
- 具体位置：Section 3 Assumption (A1) (p.4); Section 5 Sensitivity to (A1) (p.5); Appendix Z.2
- 问题：A1 要求 misclassification 仅依赖真实标签 Z 和 subgroup S，与 outcome Y(0), Y(1) 条件独立。Section 5 (p.5) 承认"not empirically testable"。Appendix Z.2 的敏感性分析使用 outcome-dependent misclassification（ν ≤ 0.2），显示 coverage ≥93.5%、bias 仅增加 13.7%。但 ν=0.2 是否代表真实 NLP 场景？在实际中，极端 outcome 的文本可能系统性地更难分类（如极端情感的文本可能包含讽刺、双关等复杂修辞），导致 ν 远大于 0.2。
- 建议：(a) 扩展敏感性分析到更大的 ν 值（0.3-0.5）；(b) 提供经验证据说明真实 NLP 数据中 outcome-dependent misclassification 的典型程度。

**W4** [warning] Abstract 信息密度过高，对非专业读者不友好
- 具体位置：Abstract (p.1)
- 问题：Abstract 第一句直接进入"exact bias identity for heterogeneous treatment effect (HTE) analysis with LLM-annotated effect modifiers"，未为非因果推断领域的 NLP 读者建立背景。随后密集地包含 δ_s、Δτ、H⁰=0.97、AUC=0.86、0.059→0.010 等技术细节。对于 EMNLP 的广泛受众（包括 generation、dialogue、MT 等方向的研究者），这个 abstract 几乎无法在第一遍阅读中理解。
- 建议：将第一句改为建立问题的通俗描述（如"When LLMs replace human annotators for downstream causal analysis, correcting their errors globally can paradoxically worsen estimates for specific subgroups"），然后再进入技术细节。

**W5** [warning] 与 PPCI per-subgroup 的比较不够充分
- 具体位置：Section 2 (p.3); Appendix L (PPCI Complementarity)
- 问题：论文声称"none corrects bias when the mismeasured variable is the effect modifier"（p.2 意译），并将 PPCI (Sui and Candès, 2026) 定位为解决 outcome-side misclassification。但 PPCI 的核心机制是 confusion-matrix-based correction——如果将 PPCI 按 subgroup 应用（per-subgroup PPCI），是否能达到类似效果？Appendix L 展示了 EC-HTE+PPCI 的互补性，但未测试"PPCI per-subgroup 单独使用"这一基线。这让读者难以判断 EC-HTE 的独特价值。
- 建议：在 Appendix L 增加 per-subgroup PPCI 作为 baseline。

## 小问题（不影响接收）

- **M1**: Figure 1 (p.2) caption 较长但信息量好。建议在 caption 首句直接点明关键 takeaway（如"Global correction introduces bias in high-error subgroups while over-correcting low-error subgroups"），然后再解释机制。
- **M2**: Table 1 (p.7) 可以增加一列显示 EC-HTE 相对 Global 的改善百分比，使关键结果更直观。
- **M3**: 脚注 1 (p.1) 澄清了"debiasing"在本文中指测量误差校正而非公平性——这很好。但这个澄清可以提升到 Abstract 或 Introduction 正文中，避免与 NLP 公平性领域的"debiasing"混淆。
- **M4**: Section 5.1 (p.7) "We compare: (1) Naive... (2) Global... (3) Stratified MLE... (4) HB EC-HTE... (5) PPCI... (6) EC-HTE+PPCI" 这个编号列表出现在实验部分但未在 Table 1 中完全对应（Table 1 缺少 PPCI 和 EC-HTE+PPCI，这些在 Appendix L）。建议在 Table 1 注明或交叉引用。
- **M5**: p.5 "Theorem 1 acquires an O(ν) perturbation (Section 5)" 这里引用的应该是 Appendix Z.2 而非 Section 5。
- **M6**: 论文标题 "When LLM Annotation Debiasing Hurts" 准确反映内容，不构成 clickbait。标题与 Theorem 1 和实验结果（50% of K=2 configurations 中 global correction 恶化 CATE）一致。

## 主要优势

1. **问题识别的价值**：论文指出了一个 NLP+因果推断社区此前未充分认识的实际问题——全局混淆矩阵校正在 subgroup 层面的偏差放大效应。这一 insight 本身对实践者有直接价值（Section 5.2 验证 50% of K=2 configurations 受损）。
2. **理论框架的清晰性**：Theorem 1 虽然代数上直接，但提供了一个精确、可操作的偏差表达式（δ_s · Δτ product form），使实践者能在不运行 EC-HTE 的情况下评估风险。Proposition 3 的 Δτ-free diagnostic 思路巧妙（即使实际性能有限）。
3. **实验的彻底性**：520 synthetic configurations × 100 MC runs、8 real LLM confusion matrices、6 open-source models 的多模型验证、semi-synthetic TweetEval、hate speech case study，覆盖了 robustness 的多个维度（budget sensitivity, class imbalance, assumption violations, asymmetric misclassification, confounding）。
4. **负面结果的诚实报告**：论文坦诚讨论了 EC-HTE 在 low Δτ 时优势不显著（Table 1, DIM K=2 Naive 行）、diagnostic 在 K=2 时失效（p.9）、hate speech case study 的 failure modes（Appendix M），以及"marginal, global correction is competitive"的条件（p.8 Limitations, p.9）。这种诚实性在学术论文中值得肯定。
5. **实用性**：Algorithm 1 (p.29) 提供了完整的伪代码；applicability conditions（n_expert threshold, classifier quality threshold）具体可执行；Section 5.4 的 diagnostic 虽有局限但提供了初步筛查工具。
6. **与 PPCI 的互补性**：Appendix L 系统验证了 EC-HTE 和 PPCI 解决不同类型误差且可组合使用，拓展了方法的适用范围。

## 格式合规检查

| 检查项 | 结果 |
|--------|------|
| 正文 ≤ 8 页 | ✓ 正文至 p.8（Conclusion + Limitations 在 p.8 内） |
| 匿名性 | ✓ "Anonymous ACL submission"，无可识别信息 |
| ACL 引用格式 | ✓ 括号引用和行内引用均符合规范 |
| Limitations section | ✓ 存在于 p.8，位于 Conclusion 之后，格式正确 |
| 脚注 1 debiasing 澄清 | ✓ 有效区分了 measurement error correction 和 fairness debiasing |

## Questions for Authors

1. 在 K=2 且误差不对称的实际场景下（这是 NLP 二分类中最常见的设置），如果 Proposition 3 diagnostic 反向预测（AUC=0.03），实践者应如何决定是否使用 EC-HTE？论文是否有替代的决策准则？
2. 你们如何看待将 PPCI 按 subgroup 应用（per-subgroup PPCI）作为替代方案？这是否能达到类似 EC-HTE 的效果？如果不能，技术原因是什么？
3. Appendix Z.2 的 outcome-dependent misclassification 敏感性分析中，ν=0.2 的选择基于什么？你们是否有经验证据表明真实 NLP 数据中 ν 的典型范围？
4. 论文的 cost-benefit 故事是"用少量专家标注+LLM 大规模标注+EC-HTE 校正"。与"直接增加专家标注量"相比，EC-HTE 的 breakeven point 在哪里？Appendix I 的 crossover analysis 部分回答了这个问题，但未提供美元层面的成本对比。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 886 · 2026-05-23T06:16:43.818412+00:00_

Reviewer 2 审稿意见已收到。记录关键发现：

**Reviewer 2 评分：3.5 (Borderline Conference)**

Must-Fix 3 项：
- **N1**: Diagnostic AUC 选择性报告（合成 0.86 vs 真实 0.63，K=2 反向预测）
- **N2**: 缺乏真实因果数据集验证，所有 ground-truth CATE 来自合成/半合成 DGP
- **N3**: "exact identity" framing 可能过度，相对经典测量误差文献增量有限

Should-Fix 5 项：W1 方法新颖性有限、W2 专家标注成本讨论不足、W3 A1 敏感性范围有限、W4 Abstract 过密、W5 缺少 per-subgroup PPCI 基线

等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 81

## Round 81

2 recorded events


### User

_source line 887 · 2026-05-23T06:16:46.392618+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference）。

三个 Must-Fix 问题：
1. Diagnostic (Proposition 3) 在真实数据上严重退化（AUC 0.86→0.63，K=2 时反向预测），但被包装为独立贡献——Abstract 选择性报告
2. 所有 ground-truth CATE 均来自合成/半合成 DGP，无真实因果数据集验证
3. Theorem 1 的"exact identity"framing 可能高估数学贡献——本质是经典测量误差结果在 effect modifier 场景的直接推广

五个 Should-Fix 问题涉及方法技术新颖性有限、expert label 成本讨论不足、A1 假设敏感性分析范围窄、Abstract 信息密度过高、与 per-subgroup PPCI 的对比缺失。

主要优势在于问题识别的价值、实验的彻底性、负面结果的诚实报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 888 · 2026-05-23T06:16:51.351076+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 82

## Round 82

6 recorded events


### User

_source line 889 · 2026-05-23T06:17:44.397704+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 理论贡献扎实（Bias Decomposition Identity 推导正确、结构优美），但方法在最接近实际场景的半合成实验中未展现优势，诊断工具在真实 LLM 混淆矩阵上 AUC 仅 0.63，实际影响力受限。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Theorem 1 推导正确可验证（R²=0.994）；假设合理但 (A2) 对称误分类在实践中不成立；SE 传播公式为 plug-in 方法，未传播 CM 估计不确定性；CausalForest 流程描述存在歧义 |
| Excitement | 3/5 | "Global debiasing can hurt" 是对 CSS 社区有价值的警示；但解决方案（per-subgroup correction）在理论诊断后显而易见；最接近实际的 TweetEval 实验未展示方法优势 |
| Reproducibility | 3/5 | DGP 规范详尽、算法伪代码完整；但未提供匿名代码/数据；MCMC 超参数明确但 CausalForest 与 CM 矫正的集成细节不够清晰 |
| Confidence | 4/5 | 仔细阅读了全部 29 页内容并手动验证了核心推导 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract 和正文对 Diagnostic AUC 的呈现具有误导性
- 具体位置：Abstract 第 7-8 行，Section 5.4
- 问题：Abstract 声明 "the identity yields a composite diagnostic (AUC = 0.86) that flags harmful correction using only per-subgroup misclassification rates"。但 0.86 是在合成数据、对称误分类 (A2) 条件下的结果。在 16 组真实 LLM 混淆矩阵上，AUC 降至 0.63（Section 5.4 和 Appendix X）。Abstract 未提及这一 degradation。对于 K=2，诊断甚至出现 anti-prediction（AUC < 0.5）。
- 为什么影响接收：读者（特别是实践者）会根据 Abstract 中的 0.86 判断该诊断的实用价值，这构成了对论文贡献的过度声明。
- 建议修改方向：Abstract 应同时报告合成和真实 LLM 矩阵的 AUC（或给出范围：0.63–0.86），并注明对称误分类条件下的限制。

**N2** [critical] 最接近实际的 TweetEval 半合成实验中 EC-HTE 未展示优势，但该结果被弱化处理
- 具体位置：Section 5.3 第 2 段，Table 7（Appendix K，tab:main_supp）
- 问题：在 TweetEval 半合成实验（K=4, n_expert=250）中：EC-HTE |bias|=0.027 vs Global |bias|=0.023（Global 更优，p=0.395 无显著差异），EC-HTE RMSE=0.225 vs Global RMSE=0.124（EC-HTE 高出 81%），Coverage 0.91 vs 0.92。这是论文中最接近实际应用场景的实验（真实文本特征定义子组、真实不平衡子组比例），却被放在 Appendix 的补充表格中。主文 Table 1 仅展示了 "extreme heterogeneity" 下的有利结果。
- 为什么影响接收：Table 1 的选择性呈现可能被审稿人和读者视为 cherry-picking。一个在最现实设定下不优于 baseline 的方法，其实际价值需要更坦诚的讨论。
- 建议修改方向：(1) 将 TweetEval 结果纳入 Table 1 或在正文中给出独立表格；(2) 在 Section 5.3 正面讨论 EC-HTE 在何种条件下不应使用（而非仅在 Limitations 中一笔带过）；(3) 明确 EC-HTE 的 "甜区"：extreme heterogeneity + sufficient per-subgroup budget + K≤4。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] CausalForest 与 CM 矫正的集成流程描述存在歧义
- 具体位置：Algorithm 1（Appendix A，p.29），Section 4.2–4.3
- 问题：Algorithm 1 Step 2 写 "Correct observed outcome moments"（μ̃_s = Ĉ_s^{-1} · μ̂_s），Step 3 写 "Train CausalForest (honest splitting) on corrected labels"。但 confusion matrix inversion 矫正的是聚合统计量（moments），不是个体标签。"Corrected labels" 是指：(a) 用后验概率对个体 Z 重新赋值？(b) 先训练 CausalForest 再 post-hoc 矫正 CATE 估计？(c) 其他？这影响对 SE 传播公式含义的理解。
- 建议：明确描述 CausalForest 流程——是 pre-correction（矫正输入）还是 post-correction（矫正输出），两者的统计性质不同。

**W2** [warning] K=8 结果未在正文中提及，对方法可扩展性给出过度乐观印象
- 具体位置：Appendix I（tab:k8_subgroups）
- 问题：K=8, n_expert=250 时，EC-HTE RMSE=0.340 远高于 Global=0.168（2倍），部分子组 RMSE 超过 1.0（s5: 0.421, s6: 0.634）。正文仅在 Limitations 中提到 "K=8 as a scalability boundary" 但未给出具体数字。对于在正文中声称的 "EC-HTE corrects subgroup-level misclassification bias" 的方法，读者需要知道 K 的实际上限。
- 建议：在正文 Section 5 中增加一句关于 K=8 性能降级的说明，引导读者关注 Appendix。

**W3** [warning] SE 传播公式 (Eq. 3) 的 plug-in 性质及其局限性未充分量化
- 具体位置：Section 4.3（Eq. 3），Limitations 第 4 段
- 问题：公式 se_adj = √(diag(Ĉ_s^{-1} diag(se²) Ĉ_s^{-T})) 不传播 Ĉ_s 本身的估计误差。论文声称 "At n_expert ≥ 100, the plug-in approximation is reasonable"，但未给出严格论证。CausalForest 的 plug-in SE 仅达 93.8% coverage（低于名义 95%），需 full bootstrap 才能恢复。建议明确说明：对 DIM 估计量，plug-in SE 是 well-calibrated（≥95% coverage at all budgets）；对 CausalForest，plug-in SE 存在 ~1.2pp 的 under-coverage gap，需 bootstrap 矫正。
- 建议：在 Section 4.3 添加一段比较 DIM 和 CausalForest 下 plug-in SE 的校准差异。

**W4** [warning] 子组定义的实践指导缺失
- 具体位置：Section 5.1, Limitations
- 问题：论文使用 has_hashtag × text_length_bin 作为子组定义，但未讨论：(a) 如何选择能捕获误分类异质性的子组特征？(b) 如果子组定义不匹配真实的误差结构会怎样（Appendix P 测试的是随机翻转子组标签，不是子组定义错误）？(c) 实践中是否需要领域知识来选择子组？这对方法的可操作性至关重要。
- 建议：在 Method 或 Limitations 中增加子组选择的实践指导。

**W5** [warning] Assumption (A2) 对称误分类在实际中普遍不成立，对理论结果的适用性影响需更显著的讨论
- 具体位置：Section 3 (A2), Remark 2, Table 14（Appendix R, tab:semireal_cm）
- 问题：Table 14 显示 GPT-4.1 在 TweetEval 上的 FPR 和 FNR 差异巨大（S0: FPR=0.054, FNR=0.526），完全不满足 (A2)。Remark 2 说明定理推广到非对称情况，但需用 B_s 矩阵逐 cell 计算。这意味着 Theorem 1 和 Proposition 3 的简洁形式在实践中不适用，需要更复杂的非对称诊断。论文仅在 Remark 2 中简略提及，非对称诊断 AUC 从 0.86 降至 0.82（附录中进一步降至 0.63）。建议将非对称扩展更显著地整合到主文叙事中。

**W6** [warning] 无完全真实数据验证
- 具体位置：Limitations 最后一段，Appendix S（Hate Speech）
- 问题：所有实验要么是合成、半合成，要么是真实数据但结果 inconclusive（Hate Speech case study 因 FNR=53.3% 导致功效不足）。论文承认 "We leave full real-data validation... to future work"。但对于声称解决实践问题的方法论文章，完全缺乏成功的真实数据验证是一个值得审稿人注意的问题。
- 建议：如果可能，补充一个 FNR 较低的真实数据案例；否则在 Limitations 中更明确地说明这一限制。

---

## 小问题（不影响接收）

- Abstract 提到 "11 real LLM confusion matrices"（第 9 行），但 Appendix X（tab:screening）实际报告了 16 个 LLM-dataset-K 组合。数字不一致。
- Remark 2 说 Theorem 1 "does not require assumption (A2)"，这与 Theorem 1 声明 "(A1)–(A5)" 矛盾。建议在 Theorem 1 后立即注明 (A2) 是 sufficient 但 not necessary 条件。
- Section 4.1 "HB estimation outperforms stratified MLE in 87.5% of configurations (21 of 24)"：24 个配置如何定义未在此处说明，需要翻到 Appendix 才能理解。
- Figure 2 的 hatched region 标注 "reaching 2.86×" 但图中不容易读出具体倍数。
- Appendix 使用 50 MC runs 的实验（如 Appendix O, S, Z）应在每次出现时标注，而不仅在脚注中一次性说明。
- 格式：Limitations 节 Section~5.4 节使用 \section* 但仍有 \label{sec:limitations}，无编号 section 的 label 在交叉引用中可能出现问题。

---

## 主要优势

1. **理论贡献干净有力**：Theorem 1 的 bias = δ_s · Δτ / (1-2π̄) 是一个优雅的精确恒等式（非 bound），产品结构具有直觉解释力。推导在 Appendix B 中逐步展开，手动验证无误。R² = 0.994 (K=2) 的实证验证令人信服。

2. **问题重要且对 CSS 社区有实际警示价值**：论文首次形式化了 "standard debiasing practice can amplify bias" 这一反直觉发现。随着 LLM 标注在社会科学因果推断中的普及，这一理论洞察具有广泛意义。

3. **实验覆盖面极其广泛**：520 个合成配置、8 个 LLM 模型、2 个数据集、16 种鲁棒性检验（子组噪声、非对称误差、类别不平衡、混杂处理、A1/A5 假设违反、估计量替换）。论文在方法不占优时也坦诚报告（TweetEval p=0.395, Hate Speech inconclusive, K=8 degradation），体现了学术诚信。

4. **与已有方法的关系梳理清晰**：PPI/DSL/PPCI 的等价性分析（Appendix L）有理有据，明确了 EC-HTE 的增量贡献在于 hierarchical partial pooling。

5. **Appendix 中的 PPCI 组合实验（Appendix J）** 和 **F-L 比较（Appendix Z.4）** 增强了方法定位的清晰度。

---

## Questions to Authors

Q1. Algorithm 1 Step 3 中的 "corrected labels" 具体指什么？是对个体观测的 Z 重新赋值（概率性？确定性？），还是对 CausalForest 输出的 CATE 进行 post-hoc 矫正？请明确描述。

Q2. 在 TweetEval 半合成实验中，EC-HTE RMSE 为 Global 的 1.81 倍。作者是否探索过在中等异质性场景下选择性地应用 EC-HTE（如仅对满足诊断条件的子组使用 per-subgroup 矫正，其余用 Global）？这种 hybrid 策略的性能如何？

Q3. 论文假设子组标签 S 是已知的。在实践中，如果误分类异质性的来源不是可观测的文本特征（而是不可观测的数据生成属性），EC-HTE 如何适用？

Q4. Proposition 3 的诊断在真实 LLM 矩阵上 AUC=0.63。作者是否考虑过更强的诊断标准（如基于 B_s 矩阵的非对称版本），能否在保持 Δτ-free 的同时提升真实场景下的 AUC？

---

## Missing References

- Egami et al. (2024) 的 DSL 框架在论文中被引用但等价性讨论主要在 Appendix L。建议在正文 Related Work 中更明确地讨论 DSL 的 per-subgroup 变体与 EC-HTE 的异同。
- 论文未引用 Zrnic & Candès (2024) 关于 cross-prediction PPI 的 active inference 版本在预算有限时的优势分析。Appendix F 简要提及但正文缺失。
- 未讨论 Carroll et al. (2006) 的 measurement error model 框架与本文方法的关系（仅在 Appendix F 提及）。考虑到论文的 econometrics 交叉贡献，正文 Related Work 应更完整。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-23T06:18:31.196850+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] Abstract 和正文对 Diagnostic AUC 的呈现具有误导性\n- Abstract 声明 AUC = 0.86，但这是在合成数据、对称误分类 (A2) 条件下的结果。在 16 组真实 LLM 混淆矩阵上，AUC 降至 0.63（Section 5.4 和 Appendix X）。Abstract 未提及这一 degradation。对于 K=2，诊断甚至出现 anti-prediction（AUC < 0.5）。\n- 建议：Abstract 应同时报告合成和真实 LLM 矩阵的 AUC。\n\n**N2** [critical] 最接近实际的 TweetEval 半合成实验中 EC-HTE 未展示优势，但该结果被弱化处理\n- TweetEval 半合成实验（K=4, n_expert=250）中：EC-HTE |bias|=0.027 vs Global |bias|=0.023（p=0.395），EC-HTE RMSE=0.225 vs Global RMSE=0.124（EC-HTE 高出 81%）。这是最接近实际应用场景的实验，却被放在 Appendix 的补充表格中。主文 Table 1 仅展示 \"extreme heterogeneity\" 下的有利结果。\n- 建议：将 TweetEval 结果纳入 Table 1；明确 EC-HTE 的 \"甜区\"。\n\n### Should-Fix\n\n**W1** CausalForest 与 CM 矫正的集成流程描述存在歧义——Algorithm 1 Step 2 写 \"Correct observed outcome moments\"，Step 3 写 \"Train CausalForest on corrected labels\"。confusion matrix inversion 矫正的是聚合统计量还是个体标签？\n\n**W2** K=8 结果未在正文中提及。K=8, n_expert=250 时，EC-HTE RMSE=0.340 远高于 Global=0.168，部分子组 RMSE 超过 1.0。\n\n**W3** SE 传播公式 (Eq. 3) 的 plug-in 性质及其局限性未充分量化。CausalForest plug-in SE 仅达 93.8% coverage，需 full bootstrap 才能恢复。\n\n**W4** 子组定义的实践指导缺失——如何选择能捕获误分类异质性的子组特征？\n\n**W5** Assumption (A2) 对称误分类在实际中普遍不成立。GPT-4.1 TweetEval: S0 FPR=0.054, FNR=0.526。Theorem 1 和 Proposition 3 的简洁形式在实践中不适用。\n\n**W6** 无完全真实数据验证。所有实验要么合成/半合成，要么真实数据但结果 inconclusive（Hate Speech FNR=53.3%）。\n\n### 小问题\n- Abstract \"11 real LLM confusion matrices\" vs Appendix X 16 个组合——数字不一致\n- Remark 2 说 Theorem 1 \"does not require (A2)\" 但 Theorem 1 声明 \"(A1)–(A5)\"——存在矛盾\n- \"21 of 24 configurations\" 的定义需翻到 Appendix\n\n### 主要优势\n1. Theorem 1 优雅精确，推导手动验证无误\n2. 问题对 CSS 社区有实际警示价值\n3. 实验覆盖极其广泛（520 配置、8 LLM、16 种鲁棒性检验）\n4. 方法不占优时坦诚报告\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] Abstract 和正文对 Diagnostic AUC 的呈现具有误导性\n- Abstract 声明 AUC = 0.86，但这是在合成数据、对称误分类 (A2) 条件下的结果。在 16 组真实 LLM 混淆矩阵上，AUC 降至 0.63（Section 5.4 和 Appendix X）。Abstract 未提及这一 degradation。对于 K=2，诊断甚至出现 anti-prediction（AUC < 0.5）。\n- 建议：Abstract 应同时报告合成和真实 LLM 矩阵的 AUC。\n\n**N2** [critical] 最接近实际的 TweetEval 半合成实验中 EC-HTE 未展示优势，但该结果被弱化处理\n- TweetEval 半合成实验（K=4, n_expert=250）中：EC-HTE |bias|=0.027 vs Global |bias|=0.023（p=0.395），EC-HTE RMSE=0.225 vs Global RMSE=0.124（EC-HTE 高出 81%）。这是最接近实际应用场景的实验，却被放在 Appendix 的补充表格中。主文 Table 1 仅展示 \"extreme heterogeneity\" 下的有利结果。\n- 建议：将 TweetEval 结果纳入 Table 1；明确 EC-HTE 的 \"甜区\"。\n\n### Should-Fix\n\n**W1** CausalForest 与 CM 矫正的集成流程描述存在歧义——Algorithm 1 Step 2 写 \"Correct observed outcome moments\"，Step 3 写 \"Train CausalForest on corrected labels\"。confusion matrix inversion 矫正的是聚合统计量还是个体标签？\n\n**W2** K=8 结果未在正文中提及。K=8, n_expert=250 时，EC-HTE RMSE=0.340 远高于 Global=0.168，部分子组 RMSE 超过 1.0。\n\n**W3** SE 传播公式 (Eq. 3) 的 plug-in 性质及其局限性未充分量化。CausalForest plug-in SE 仅达 93.8% coverage，需 full bootstrap 才能恢复。\n\n**W4** 子组定义的实践指导缺失——如何选择能捕获误分类异质性的子组特征？\n\n**W5** Assumption (A2) 对称误分类在实际中普遍不成立。GPT-4.1 TweetEval: S0 FPR=0.054, FNR=0.526。Theorem 1 和 Proposition 3 的简洁形式在实践中不适用。\n\n**W6** 无完全真实数据验证。所有实验要么合成/半合成，要么真实数据但结果 inconclusive（Hate Speech FNR=53.3%）。\n\n### 小问题\n- Abstract \"11 real LLM confusion matrices\" vs Appendix X 16 个组合——数字不一致\n- Remark 2 说 Theorem 1 \"does not require (A2)\" 但 Theorem 1 声明 \"(A1)–(A5)\"——存在矛盾\n- \"21 of 24 configurations\" 的定义需翻到 Appendix\n\n### 主要优势\n1. Theorem 1 优雅精确，推导手动验证无误\n2. 问题对 CSS 社区有实际警示价值\n3. 实验覆盖极其广泛（520 配置、8 LLM、16 种鲁棒性检验）\n4. 方法不占优时坦诚报告\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-23T06:19:03.290246+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32093
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-23T06:19:03.491403+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] Diagnostic（Proposition 3）作为\"independently useful\"贡献的 claim 被实际性能严重削弱\n- Abstract 将 diagnostic 列为独立贡献之一，但：合成数据 AUC = 0.86，真实 LLM 混淆矩阵 AUC = 0.63，K=2 时 AUC 降至 0.03（反向预测）。主文仅用一段话讨论了退化。Abstract 中报告 AUC=0.86 而不提 real-data degradation 构成选择性报告。\n- 建议：(a) Abstract 中加入 real-data AUC 的限定；(b) 将 diagnostic 降级为辅助工具；(c) 讨论 K=2 时的替代决策策略。\n\n**N2** [critical] 缺乏真实因果数据集验证——所有 ground-truth CATE 均来自合成或半合成 DGP\n- 没有任何实验使用真实 RCT 数据 + 已知 ground-truth CATE。如果所有 CATE 都来自研究者设计的 DGP，无法排除 EC-HTE 的优势仅存在于满足假设的人工场景。\n- 建议：(a) 在 Limitations 中显著承认；(b) 讨论获取真实 ground-truth CATE 数据的困难性；(c) 考虑经典因果推断基准（IHDP, LaLonde）配合文本特征。\n\n**N3** [critical] Theorem 1 的\"exact identity\" framing 可能过度——需更清晰界定增量贡献\n- Frazis & Loewenstein (2003) 已推导了 binary misclassified variable 的标量衰减。Theorem 1 本质上是将此推广到\"全局 vs per-subgroup 校正\"差异并应用于 CATE。证明仅需几行矩阵乘法。\"exact identity\" 暗示数学深度，但等式在技术上是直截了当的。\n- 建议：主文中更明确说明 novelty 在于识别此前被忽视的问题并将经典框架适配到 HTE estimation。\n\n### Should-Fix\n\n**W1** EC-HTE 方法本身技术新颖性有限——per-subgroup CM inversion + HB 是识别问题后的自然解。Dirichlet-Multinomial + Gibbs 是标准做法。贡献主要在 problem identification + careful engineering。\n\n**W2** per-subgroup expert label 获取的实际成本讨论不足。K=4, P(Z_minority)=0.25 需 n_expert ≥ 400。如果专家预算这么充裕，为什么不直接多用专家标注？cost-benefit 分析缺失。\n\n**W3** Assumption (A1) 敏感性分析范围有限。ν=0.2 是否代表真实 NLP 场景？极端 sentiment 的讽刺/双关可能导致 ν 远大于 0.2。\n\n**W4** Abstract 信息密度过高，对非因果推断 NLP 读者不友好。第一句直接进入技术细节，未建立通俗背景。\n\n**W5** 与 PPCI per-subgroup 的比较不够充分。未测试 \"PPCI per-subgroup 单独使用\" 这一 baseline。\n\n### 小问题\n- M1: Figure 1 caption 首句应点明关键 takeaway\n- M2: Table 1 可增加改善百分比列\n- M3: 脚注 1 \"debiasing\" 澄清可提升到正文\n- M4: Section 5.1 编号列表与 Table 1 不完全对应\n- M5: p.5 引用 \"Section 5\" 应为 \"Appendix Z.2\"\n- M6: 标题准确反映内容，不构成 clickbait\n\n### 主要优势\n1. 问题识别有直接价值（50% K=2 configs 受损）\n2. 理论框架清晰（δ_s·Δτ product form）\n3. 实验彻底性（520 configs × 100 MC, 8 LLM）\n4. 负面结果诚实报告\n5. Algorithm 1 完整可执行\n6. EC-HTE+PPCI 互补性验证\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] Diagnostic（Proposition 3）作为\"independently useful\"贡献的 claim 被实际性能严重削弱\n- Abstract 将 diagnostic 列为独立贡献之一，但：合成数据 AUC = 0.86，真实 LLM 混淆矩阵 AUC = 0.63，K=2 时 AUC 降至 0.03（反向预测）。主文仅用一段话讨论了退化。Abstract 中报告 AUC=0.86 而不提 real-data degradation 构成选择性报告。\n- 建议：(a) Abstract 中加入 real-data AUC 的限定；(b) 将 diagnostic 降级为辅助工具；(c) 讨论 K=2 时的替代决策策略。\n\n**N2** [critical] 缺乏真实因果数据集验证——所有 ground-truth CATE 均来自合成或半合成 DGP\n- 没有任何实验使用真实 RCT 数据 + 已知 ground-truth CATE。如果所有 CATE 都来自研究者设计的 DGP，无法排除 EC-HTE 的优势仅存在于满足假设的人工场景。\n- 建议：(a) 在 Limitations 中显著承认；(b) 讨论获取真实 ground-truth CATE 数据的困难性；(c) 考虑经典因果推断基准（IHDP, LaLonde）配合文本特征。\n\n**N3** [critical] Theorem 1 的\"exact identity\" framing 可能过度——需更清晰界定增量贡献\n- Frazis & Loewenstein (2003) 已推导了 binary misclassified variable 的标量衰减。Theorem 1 本质上是将此推广到\"全局 vs per-subgroup 校正\"差异并应用于 CATE。证明仅需几行矩阵乘法。\"exact identity\" 暗示数学深度，但等式在技术上是直截了当的。\n- 建议：主文中更明确说明 novelty 在于识别此前被忽视的问题并将经典框架适配到 HTE estimation。\n\n### Should-Fix\n\n**W1** EC-HTE 方法本身技术新颖性有限——per-subgroup CM inversion + HB 是识别问题后的自然解。Dirichlet-Multinomial + Gibbs 是标准做法。贡献主要在 problem identification + careful engineering。\n\n**W2** per-subgroup expert label 获取的实际成本讨论不足。K=4, P(Z_minority)=0.25 需 n_expert ≥ 400。如果专家预算这么充裕，为什么不直接多用专家标注？cost-benefit 分析缺失。\n\n**W3** Assumption (A1) 敏感性分析范围有限。ν=0.2 是否代表真实 NLP 场景？极端 sentiment 的讽刺/双关可能导致 ν 远大于 0.2。\n\n**W4** Abstract 信息密度过高，对非因果推断 NLP 读者不友好。第一句直接进入技术细节，未建立通俗背景。\n\n**W5** 与 PPCI per-subgroup 的比较不够充分。未测试 \"PPCI per-subgroup 单独使用\" 这一 baseline。\n\n### 小问题\n- M1: Figure 1 caption 首句应点明关键 takeaway\n- M2: Table 1 可增加改善百分比列\n- M3: 脚注 1 \"debiasing\" 澄清可提升到正文\n- M4: Section 5.1 编号列表与 Table 1 不完全对应\n- M5: p.5 引用 \"Section 5\" 应为 \"Appendix Z.2\"\n- M6: 标题准确反映内容，不构成 clickbait\n\n### 主要优势\n1. 问题识别有直接价值（50% K=2 configs 受损）\n2. 理论框架清晰（δ_s·Δτ product form）\n3. 实验彻底性（520 configs × 100 MC, 8 LLM）\n4. 负面结果诚实报告\n5. Algorithm 1 完整可执行\n6. EC-HTE+PPCI 互补性验证\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-23T06:19:04.900872+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 894 · 2026-05-23T06:19:10.164146+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 83

## Round 83

2 recorded events


### User

_source line 895 · 2026-05-23T06:19:12.734638+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference）。

核心判断：
- **理论贡献扎实**：Theorem 1（bias = δ_s·Δτ/(1-2π̄)）推导正确，R²=0.994 验证充分，产品结构具有优雅的可解释性
- **实验覆盖极广**：520 个配置、8 个 LLM、16 种鲁棒性检验，且坦诚报告不利结果
- **两个 Must-Fix 问题**：(1) Abstract 对 Diagnostic AUC 的呈现具有误导性（合成 0.86 vs 真实 LLM 0.63）；(2) 最接近实际的 TweetEval 实验中 EC-HTE RMSE 为 Global 的 1.81 倍，但该结果被放在 Appendix 补充表格中，主文 Table 1 仅展示 extreme heterogeneity 下的有利结果
- **六个 Should-Fix 问题**：CausalForest 集成流程描述歧义、K=8 退化未在正文提及、SE plug-in 局限性量化不足、子组定义指导缺失、(A2) 对称假设在实际中不成立的影响讨论不充分、无成功的完全真实数据验证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 896 · 2026-05-23T06:19:20.420367+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 84

## Round 84

2 recorded events


### User

_source line 897 · 2026-05-23T06:20:38.190857+00:00_

[Reviewer 1 审稿结果]:
逐条回应 Reviewer 2 的审稿意见。

---

## 对 Reviewer 2 Must-Fix 问题的逐条回应

**[AGREE] R2-N1: Diagnostic AUC 在 Abstract 中的呈现具有误导性**

同意。我在自己的 N1 中提出了相同的问题。Abstract 报告 AUC=0.86 而不提及真实 LLM 混淆矩阵上 AUC=0.63 的退化，构成选择性报告。R2 进一步指出 K=2 时 AUC 降至 0.03（反向预测），这比我注意到的更严重——Section 5.4 提到 "For K=2, the diagnostic anti-predicts because |δ₀|=|δ₁| forces score differentiation onto 1/πₛ alone"，但 Abstract 完全未提及这一根本性限制。R2 建议将 diagnostic 降级为辅助工具是合理的。

**[AGREE with nuance] R2-N2: 缺乏真实因果数据集验证**

同意这是一个重要限制，我在 W6 中也指出了这一点。所有 ground-truth CATE 均来自研究者控制的 DGP，无法排除方法优势仅存在于满足假设的场景。Appendix S 的 Hate Speech 案例是唯一使用完全真实数据的实验，但因 FNR=53.3% 导致结果 inconclusive。

但我认为 R2 将其标为 "critical/must-fix" 可能过于严格。原因：(1) 获取同时具备 RCT 设计 + ground-truth CATE + LLM 标注的公开数据集目前确实不存在，Limitations 最后一段已承认这一点；(2) 论文的核心贡献是理论恒等式（Theorem 1），其正确性不依赖于实验验证——这是数学推导，已被代数验证和 R²=0.994 的 MC 模拟确认；(3) 半合成实验使用了 11 组真实 LLM 混淆矩阵（Appendix W, Table 20），部分弥补了纯合成的不足。R2 建议使用 IHDP/LaLonde 等经典因果基准 + 文本特征是有价值的方向，但这些数据集本身不包含 LLM 标注，需要额外的标注工作。建议将此问题定位为 should-fix（在 Limitations 中加强讨论）而非 must-fix。

**[REBUT] R2-N3: Theorem 1 的 "exact identity" framing 过度**

不同意将此作为 must-fix。理由：

1. **与 Frazis & Loewenstein (2003) 的区别是实质性的，非表面的。** F-L 推导的是 OLS 中 misclassified binary regressor 的标量衰减公式，适用于 average treatment effects（ATE），且假设 homogeneous error rates。Theorem 1 针对的是 heterogeneous treatment effects（HTE）中 global correction 引入的 per-subgroup bias，涉及 δₛ × Δτ 的交互项。Appendix Z.4（Table 28）实证表明 F-L 标量矫正在 heterogeneous 设定下反而增加 bias（F-L Per-Subgroup |bias|=0.112 vs Naive=0.062），证明了标量方法不能替代矩阵方法。

2. **数学深度不等于贡献深度。** 证明确实只需几行矩阵代数，但数学 simplicity 恰恰是此结果的优势——它表明一个被广泛使用的标准实践（global confusion matrix correction）存在可被精确刻画的系统性缺陷。ACL ARR reviewer guidelines（H7）明确指出 "simpler solutions are preferable — complexity isn't a virtue"。

3. **"Exact identity" 的表述是准确的。** Equations (1)-(2) 是 population-level 的精确等式（不是 bound 或 approximation），R²=0.994 的实证验证确认了有限样本下的准确性。称其为 "exact identity" 是对数学性质的准确描述。

4. **Novelty 在于问题识别 + HTE 适配。** 论文的 Related Work（Section 2）和 Extended Related Work（Appendix F）已明确说明：F-L (2003) 处理 ATE 而无子组异质性，本文的创新在于将框架扩展到 subgroup-heterogeneous CATE estimation 并揭示了 "debiasing can hurt" 的反直觉结论。这一结论此前未在 NLP/CSS 文献中被形式化。

建议作者在正文中更明确地标注 Theorem 1 相对于 F-L 的增量贡献（如在 proof sketch 后加一段说明），但将此作为 must-fix 是不合理的。

---

## 对 Reviewer 2 Should-Fix 问题的逐条回应

**[AGREE] R2-W1: EC-HTE 方法本身技术新颖性有限**

同意。Per-subgroup CM inversion + Dirichlet-Multinomial HB 是在识别问题后的自然解。论文的主要贡献在于 problem identification + bias identity + thorough empirical validation，而非方法本身的技术创新。这与我的整体评估一致：理论贡献扎实，方法贡献有限。

**[AGREE] R2-W2: Expert label 成本讨论不足**

同意，这是我遗漏的一个重要观点。论文要求 n_expert × P(Z_minority) / K ≥ 25，对于 K=4, P(Z_minority)=0.25，需要 n_expert ≥ 400。如果研究者有预算获取 400+ 专家标签，为什么不直接使用全专家标注进行因果推断？论文应讨论 EC-HTE 在 total annotation budget（LLM 标注 + 专家标注）框架下的成本效益，说明在何种 N/n_expert 比值下 EC-HTE 的价值最大化。Section 5.4 的 budget crossover curves（Appendix I, Figure 3）部分回应了这一问题，但未从经济成本角度分析。

**[REBUT] R2-W3: A1 敏感性分析范围有限**

部分不同意。Table 25（Appendix Z.1）显示 EC-HTE 在 γ=0.2 时仍维持 93.5% coverage，bias 仅增加 13.7%。R2 认为讽刺/双关可能导致 γ 远大于 0.2，但：(1) γ 的定义是 misclassification probability 对 outcome magnitude 的线性敏感度，γ=0.2 已意味着误分类率随 outcome 变化 ±20%，这在 NLP 场景中已是相当极端的 violation；(2) 如果 γ 真的远大于 0.2，则 Assumption (A1) 根本不成立，任何基于混淆矩阵的方法（包括 PPI/DSL）都会失效——这不是 EC-HTE 特有的弱点；(3) 论文在 Section 3 中已引用 sensitivity analysis frameworks (Lash et al., 2009; Dorn et al., 2022) 作为未来 bound 的方向。γ=0.2 作为初步调查范围是合理的。

**[AGREE] R2-W4: Abstract 信息密度过高**

同意这是一个 presentation 问题。Abstract 第一句直接进入 "exact bias identity for heterogeneous treatment effect (HTE) analysis with LLM-annotated effect modifiers"，对非因果推断背景的 NLP 读者不友好。建议在 Abstract 开头增加一句背景（如 "LLMs increasingly replace human annotators in computational social science, but their errors vary across demographic and textual subgroups"），再引入技术贡献。

**[REBUT] R2-W5: 与 PPCI per-subgroup 的比较不充分**

不同意。EC-HTE 和 PPCI 矫正的是不同类型的误差：EC-HTE 矫正 covariate misclassification（effect modifier Z 的误分类），PPCI 矫正 outcome-side prediction error。Appendix J（Table 8）的 4-DGP 正交设计已清楚展示了这一互补性：DGP-A（仅 covariate 误差）PPCI 无效，DGP-B（仅 outcome 误差）EC-HTE 无效。"PPCI per-subgroup 单独使用" 这一 baseline 在 covariate misclassification 设定下不会比 PPCI-global 有本质改善，因为 PPCI 的 rectifier 作用于 outcome predictions 而非 Z labels。Appendix L（Section L）已详细讨论了 PPI/DSL/PPCI 的框架关系。

---

## 对小问题的回应

- M1-M4: 均为合理的 presentation 改进建议，同意。
- M5: 需要验证具体引用位置，但如果确实引用错误则应修正。
- M6: 同意标题准确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 898 · 2026-05-23T06:20:43.660198+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 85

## Round 85

28 recorded events


### User

_source line 899 · 2026-05-23T06:21:13.321271+00:00_

[Reviewer 2 审稿结果]:
逐条回应 Reviewer 1 的审稿意见。

## 交叉回应

### Must-Fix

**[AGREE] R1-N1: Abstract 中 Diagnostic AUC 的呈现具有误导性**

同意。我在自己的审稿意见中将此列为 N1（critical）。Abstract 报告 AUC=0.86 而未提及真实 LLM 混淆矩阵上的退化（0.63）和 K=2 时的反向预测（AUC=0.03），构成选择性报告。补充一点 R1 未提及的：论文在 p.9 承认 "the diagnostic anti-predicts because δ_s = |r_s| forces sign discrimination onto 1/r_s alone"，说明作者理解这一退化的机制但选择不在 Abstract 中体现。这加重了选择性呈现的判断。

---

**[REBUT] R1-N2: TweetEval K=4 结果被弱化处理**

R1 称该结果"被放在 Appendix 的补充表格中"——这一事实判断不准确。Section 5.3（p.7 主文）明确写道：

> "but EC-HTE incurs higher RMSE (0.225 vs. 0.124), driven by moderate Δτ=0.23 and unbalanced subgroup receiving ~30 expert labels each"

论文在主文中报告了 EC-HTE 在此设置下 RMSE 劣势 81% 的事实，并给出了解释（moderate Δτ + 小 subgroup 样本量）。这不是"弱化处理"，而是在主文中坦诚报告了负面结果。

但我**部分同意** R1 关于 Table 1 选择性的批评：Table 1 仅展示 K=2 extreme 配置，未包含 K=4 或 moderate heterogeneity 的结果。这确实使 Table 1 对 EC-HTE 有利。建议 Table 1 增加 K=4 行或至少增加 moderate Δτ 配置，让读者直接对比 EC-HTE 的"甜区"与局限。

此外，R1 提到的 p=0.395（bias 差异不显著）确实仅在附录中出现（主文 Section 5.3 未报告 p 值）。如果 bias 差异统计上不显著，这一信息应出现在主文中。

---

### Should-Fix

**[AGREE] R1-W1: Algorithm 1 Step 2 vs Step 3 的歧义**

Step 2 写"Correct observed outcome moments"（矫正聚合统计量），Step 3 写"Train CausalForest on corrected labels"（在矫正后的标签上训练）。从 Section 4.2（p.6）可知，实际操作是 μ̃_s = Ĉ_s^{-1} μ̂_s——矫正的是 subgroup-level conditional means，然后将矫正后的 pseudo-outcomes 输入 CausalForest。Algorithm 1 的措辞确实混淆了"矫正聚合量"和"矫正个体标签"这两个不同操作。这不是技术错误但会导致误解，应修正。

---

**[AGREE] R1-W2: K=8 结果未在正文中提及**

Appendix L.2（p.15-16）的 K=8 结果显示 EC-HTE RMSE=0.340 远高于 Global=0.168。论文将此归因于"per-subgroup sample size constraint"——K=8 时每个 subgroup 的专家标注仅约 30 条，低于 n_expert × P(Z_minority)/K ≥ 25 的阈值。这表明 EC-HTE 的 scalability 有硬上限。K=8 是社会科学中常见的 subgroup 数量（如年龄×性别×教育的交叉），主文 Limitations 或 Section 4 应提及这一 scalability 瓶颈。

---

**[REBUT] R1-W3: SE 传播 plug-in coverage 93.8% 的问题**

93.8% vs 95% 的差距（1.2 个百分点）在 100 MC runs 的模拟中处于 Monte Carlo 误差范围内（95% coverage 的标准误约 ±2.2pp for n=100）。论文 Section 4.2（p.6）明确指出 "the plug-in SE ... may understate total uncertainty; this limitation is discussed further in the Limitations section"，且 Appendix Y（p.25）展示 full bootstrap SE 恢复到 94-96% coverage。论文的处理方式——承认局限、提供替代方案——是合理的。这不构成一个需要"fix"的问题，而是一个已被妥善 addressed 的 trade-off。

---

**[AGREE] R1-W4: 子组定义的实践指导缺失**

论文在 TweetEval 中使用 hashtag presence × text length 作为 subgroup 定义（Appendix E, p.13），在 hate speech 中使用 platform × length（Appendix M），但未讨论如何在新数据集上选择能捕获 misclassification heterogeneity 的 subgroup 特征。这是 EC-HTE 实用性的关键缺口。Appendix V（Civil Comments Validation, p.23）验证了 misclassification heterogeneity 跨数据集存在，但未给出特征选择的系统指导。建议增加一个 "Practitioner's Guide" 段落。

---

**[REBUT] R1-W5: Assumption (A2) 对称误分类普遍不成立**

R1 的事实观察正确（GPT-4.1 TweetEval FPR=0.054, FNR=0.526 高度不对称），但对论文的批评过重。论文已在多处处理了不对称情形：

1. Remark 2（p.4）：明确给出不对称情形的 product form，证明 Theorem 1 的 **核心结论**（全局校正引入 subgroup bias）不依赖 (A2)
2. Appendix D（p.13）：推导不对称的完整证明
3. Section 5（p.5）"Extension to asymmetric misclassification"：验证不对称下 EC-HTE maintains near-nominal coverage (≥93.5%)
4. Appendix K（Asymmetric Misclassification Extension, p.17）：Table 6 报告不对称条件下的完整结果，EC-HTE RMSE 降低 33%（0.340→0.216）

(A2) 仅用于 Theorem 1 的 **简洁标量形式** δ_s · Δτ/(1−2π) 和 Proposition 3 的 diagnostic。EC-HTE 方法本身不依赖 (A2)——Algorithm 1 直接估计完整的（可能不对称的）混淆矩阵。R1 将 Theorem 1 简洁形式的限制等同于方法本身的限制，这一推理有误。

---

**[AGREE] R1-W6: 无完全真实数据验证**

同意。我在自己的 N2 中同样标注为 critical。所有 ground-truth CATE 来自合成 DGP。Hate speech case study（Appendix M）的 FNR=53.3% 确实使结果 inconclusive——论文将此解读为"failure mode"并坦诚报告，但这也意味着真实数据上的唯一深度案例以失败告终。

---

### 小问题

**[AGREE] "11 real LLM confusion matrices" vs 16 组合**

需要澄清。可能的解释：11 个唯一的 model-level confusion matrices（如 6 models on TweetEval + 4 on Civil Comments + 1 additional），而 16 是 model × subgroup 的组合数。但 Abstract 的措辞确实造成歧义。

---

**[REBUT] Remark 2 与 Theorem 1 假设列表的"矛盾"**

这不是逻辑矛盾，而是论文采用了常见的"先给出强假设下的简洁结果、再 remark 放松假设"的写法。Theorem 1 在 (A1)-(A5) 下给出 bias = δ_s · Δτ/(1−2π) 的标量形式；Remark 2 立即说明去掉 (A2) 后结论仍成立但形式更复杂（引入 D_s(z,l) 矩阵因子）。这不是矛盾，而是 progressive relaxation。但我承认这种写法可能造成困惑——如果 (A2) 不必要，Theorem 1 不应在假设列表中包含它。建议将 Theorem 1 改为 "(A1), (A3)-(A5)"，并将 (A2) 降为"simplifying assumption for scalar form"。

---

**[AGREE] "21 of 24 configurations" 需要翻到 Appendix**

这确实是可读性问题。主文应简要说明 24 configurations 的定义（K × Δτ × estimator 的网格），否则数字缺乏 context。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-23T06:22:00.996553+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-23T06:22:01.902079+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T06:07:41.574281+00:00\", \"completed_at\": \"2026-05-23T06:11:43.626408+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"从 Figure 1 (p2) 到 Table 1 (p7) 跨越 5 页，中间仅有 display equations 作为视觉元素，无 figure 或 table。审稿人滚动浏览此段会感到视觉单调。理论推导部分的 equations 有一定缓解作用，但对实证+理论混合型论文而言，这段 text desert 较长\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-8\", \"message\": \"主体正文 8 页仅含 3 个 display items（Figure 1, Table 1, Figure 2），密度偏低。大量实验结果（Tables 2-30, Figures 3-5）被推入 Appendix，主体缺乏视觉丰富度。建议考虑将 1-2 个关键 appendix 表格/图（如 budget sweep 的 Figure 4 或 cross-model consistency 的关键结果）提入主体\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 出现在第 2 页，提供了清晰的视觉锚点，展示 global vs. subgroup-stratified correction 的 bias 机制。三面板设计信息明确，caption 自包含，Title-Abstract-Figure 1 叙事一致。审稿人第一印象良好\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，最优结果加粗，精度一致（3 位小数），格式规范。列数适中，单栏放置合理\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 heatmap 设计得当——用 hatching 区分 \\\"debiasing helps\\\" vs \\\"hurts\\\" 区域，colorbar 清晰。但轴标签和 colorbar 刻度文字字号偏小（约为正文字号的 60-65%），打印时可能不够清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 29\", \"message\": \"Algorithm 1 伪代码占页面约 40-45%，下方约 55% 为空白。作为末页可接受，但如果空间紧张可考虑将 Algorithm 1 与前页合并\"}, {\"severity\": \"info\", \"dimension\": \"page 28\", \"message\": \"页面内容在约 60% 处结束，底部约 40% 空白。与 page 29 合计约 1 页空间未利用\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item（纯 Title/Abstract/Introduction），这在理论+方法型论文中常见，且 Figure 1 在紧邻的 page 2 出现，不构成问题\"}, {\"severity\": \"info\", \"dimension\": \"pages 4-5\", \"message\": \"数学公式渲染正确，Theorem 1、Proposition 3 排版清晰，无 LaTeX 错误残留。Assumptions (A1)-(A5) 格式统一\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"参考文献格式一致，无 [?] 未解析引用，无跳号。Author 缩写和年份格式统一\"}, {\"severity\": \"info\"
…[truncated 200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-23T06:22:02.203512+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "description": "Read current review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "description": "Read current review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-23T06:22:02.354978+00:00_

&lt;persisted-output>
Output too large (49.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt

Preview (first 2KB):
issues:
  # === RESOLVED (prior rounds, unchanged) ===
  - id: "R1-N1"
    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 2
    action_items: []
    resolution: "重新推导为精确恒等式"
    resolution_round: 0

  - id: "R2-W8"
    summary: "Proposition 1 限于 K=2"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "Theorem 1 适用一般 K"
    resolution_round: 0

  - id: "R1-N2"
    summary: "Real data ground truth CATE 来源不明"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "恰当定位为 illustrative application"
    resolution_round: 0

  - id: "R1-N3"
    summary: "HB 模型规格严重不完整"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "完整 MCMC 规格"
    resolution_round: 0

  - id: "JOINT-W4"
    summary: "相关工作严重遗漏"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "30+ 引用覆盖"
    resolution_round: 0

  - id: "JOINT-W3"
    summary: "信息密度过高"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "主文精简至合理密度"
    resolution_round: 0

  - id: "R2-W7"
    summary: "真实数据验证单薄"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_r
…[truncated 320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-23T06:22:06.219959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
  "limit": "200",
  "offset": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
    "limit": "200",
    "offset": "40"
  }
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-23T06:22:06.271018+00:00_

40	    status: resolved
41	    first_raised_round: 0
42	    last_seen_round: 1
43	    action_items: []
44	    resolution: "完整 MCMC 规格"
45	    resolution_round: 0
46	
47	  - id: "JOINT-W4"
48	    summary: "相关工作严重遗漏"
49	    category: writing
50	    severity: warning
51	    status: resolved
52	    first_raised_round: 0
53	    last_seen_round: 1
54	    action_items: []
55	    resolution: "30+ 引用覆盖"
56	    resolution_round: 0
57	
58	  - id: "JOINT-W3"
59	    summary: "信息密度过高"
60	    category: writing
61	    severity: warning
62	    status: resolved
63	    first_raised_round: 0
64	    last_seen_round: 1
65	    action_items: []
66	    resolution: "主文精简至合理密度"
67	    resolution_round: 0
68	
69	  - id: "R2-W7"
70	    summary: "真实数据验证单薄"
71	    category: experiment
72	    severity: warning
73	    status: resolved
74	    first_raised_round: 0
75	    last_seen_round: 1
76	    action_items: []
77	    resolution: "恰当定位 + 公开数据集"
78	    resolution_round: 0
79	
80	  - id: "R1-W5"
81	    summary: "Pages 9-10 缺 Appendix 标签"
82	    category: format
83	    severity: info
84	    status: resolved
85	    first_raised_round: 0
86	    last_seen_round: 0
87	    action_items: []
88	    resolution: "附录结构重组"
89	    resolution_round: 0
90	
91	  - id: "JOINT-F1"
92	    summary: "Tightness ratio 数值不一致"
93	    category: method
94	    severity: info
95	    status: resolved
96	    first_raised_round: 0
97	    last_seen_round: 0
98	    action_items: []
99	    resolution: "精确恒等式使问题消解"
100	    resolution_round: 0
101	
102	  - id: "R2-W4"
103	    summary: "DSL 区分不充分"
104	    category: framing
105	    severity: info
106	    status: resolved
107	    first_raised_round: 0
108	    last_seen_round: 1
109	    action_items: []
110	    resolution: "Related Work + Appendix E 清晰技术区分 + DSL 等价性证明"
111	    resolution_round: 1
112	
113	  - id: "R1-W1"
114	    summary: "Causal Forest uncertainty propagation 不清楚"
115	    category: method
116	    severity: info
117	    status: resolved
118	    first_raised_round: 0
119	   
…[truncated 3186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-23T06:22:14.454754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
  "offset": "240",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
    "offset": "240",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-23T06:22:14.505728+00:00_

240	    last_seen_round: 1
241	    action_items: []
242	    resolution: "Table 1 footnote + Appendix MC SE"
243	    resolution_round: 2
244	
245	  - id: "RD2-W2"
246	    summary: "诊断 setting-level AUC=0.47 + 循环依赖"
247	    category: method
248	    severity: warning
249	    status: resolved
250	    first_raised_round: 2
251	    last_seen_round: 3
252	    action_items:
253	      - round: 2
254	        action: "切换到 Δτ-free Proposition 2 条件"
255	        assigned_to: paper_agent
256	        status: done
257	    resolution: "Δτ-free 诊断，setting AUC 0.47→0.889"
258	    resolution_round: 2
259	
260	  - id: "RD2-W3"
261	    summary: "A2+A3 假设过强，放松分析不足"
262	    category: method
263	    severity: warning
264	    status: resolved
265	    first_raised_round: 2
266	    last_seen_round: 3
267	    action_items:
268	      - round: 2
269	        action: "exp-019 P(Z=1) sweep + Appendix 集成"
270	        assigned_to: paper_agent
271	        status: done
272	    resolution: "exp-019: R²≥0.976 across P(Z=1)∈[0.1,0.5]"
273	    resolution_round: 2
274	
275	  - id: "RD2-W6"
276	    summary: "贡献列表 5 项偏多"
277	    category: framing
278	    severity: info
279	    status: resolved
280	    first_raised_round: 2
281	    last_seen_round: 3
282	    action_items:
283	      - round: 2
284	        action: "合并至 3 项"
285	        assigned_to: paper_agent
286	        status: done
287	    resolution: "5→3 项"
288	    resolution_round: 2
289	
290	  - id: "RD2-W1"
291	    summary: "g(π̄) 未给闭合形式"
292	    category: method
293	    severity: warning
294	    status: resolved
295	    first_raised_round: 2
296	    last_seen_round: 3
297	    action_items:
298	      - round: 2
299	        action: "Appendix C footnote: J=3 显式 g(π̄)=1/(1-3π̄/2)"
300	        assigned_to: paper_agent
301	        status: done
302	    resolution: "Corollary 1 footnote 给出 J=3 显式表达式"
303	    resolution_round: 2
304	
305	  - id: "RD2-M1"
306	    summary: "遗漏 Fong & Tyler (2021)"
307	    category: writing
308	    severity: info
309	    status: reso
…[truncated 6762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-23T06:22:21.081971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm_annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
  "offset": "540",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm_annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
    "offset": "540",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-23T06:22:21.132846+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_director_2cf1d8af.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-23T06:22:24.194936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
  "offset": "540",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
    "offset": "540",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-23T06:22:24.246130+00:00_

540	    last_seen_round: 9
541	    action_items:
542	      - round: 4
543	        action: "§5.2 补充条件统计 84.6%"
544	        assigned_to: paper_agent
545	        status: done
546	      - round: 6
547	        action: "合并 50%/84.6% 为单句，降低 50% 修辞突出度"
548	        assigned_to: director
549	        status: done
550	      - round: 9
551	        action: "所有出现 50% 的位置加 'across our parameter grid' 限定"
552	        assigned_to: director
553	        status: done
554	    resolution: "Round 9：全部 5 处 50% claim 加 'across our parameter grid' 限定。"
555	    resolution_round: 9
556	
557	  - id: "R3F-W4"
558	    summary: "τ(z) 不依赖 S 的隐含假设未正式声明"
559	    category: method
560	    severity: warning
561	    status: resolved
562	    first_raised_round: 3
563	    last_seen_round: 5
564	    action_items:
565	      - round: 4
566	        action: "Section 3 加 (A5) + 泛化说明"
567	        assigned_to: paper_agent
568	        status: done
569	    resolution: "(A5) 正式列出。L61 说明推广到 subgroup-specific Δτ_s。"
570	    resolution_round: 4
571	
572	  - id: "R3F-W5"
573	    summary: "部分 claims 统计显著性不足"
574	    category: experiment
575	    severity: warning
576	    status: resolved
577	    first_raised_round: 3
578	    last_seen_round: 4
579	    action_items:
580	      - round: 4
581	        action: "§5.3 TweetEval 加 p=0.395 + not statistically significant"
582	        assigned_to: director
583	        status: done
584	    resolution: "§5.3 加 '(p=0.395 vs. Global, not statistically significant)' 标注"
585	    resolution_round: 4
586	
587	  - id: "R3F-W6"
588	    summary: "κ>100 singularity guard 阈值缺乏支撑"
589	    category: method
590	    severity: warning
591	    status: resolved
592	    first_raised_round: 3
593	    last_seen_round: 6
594	    action_items:
595	      - round: 4
596	        action: "method.tex 加等价性说明"
597	        assigned_to: director
598	        status: done
599	      - round: 6
600	        action: "method.tex 加 two-tier 说明 + Algorithm 1 加 preconditions"
601	        assigned_to: director
602	        statu
…[truncated 15081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-23T06:22:30.319685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
  "offset": "1040",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
    "offset": "1040",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-23T06:22:30.370833+00:00_

1040	        status: pending
1041	      - round: 10
1042	        action: "Oracle 实验：使用真实 C_s 进行校正，对比 plug-in SE 覆盖率，隔离 CM 估计误差贡献"
1043	        assigned_to: main_agent
1044	        status: pending
1045	      - round: 11
1046	        action: "补充 CausalForest-specific 覆盖率校准实验（与 DIM Appendix Y 等同验证）"
1047	        assigned_to: main_agent
1048	        status: pending
1049	    resolution: ""
1050	    resolution_round: null
1051	
1052	  - id: "R5-W1"
1053	    summary: "Semi-synthetic TweetEval 中 EC-HTE 未优于 Global，但 Abstract/Intro 叙事以正面结果为主"
1054	    category: framing
1055	    severity: warning
1056	    status: open
1057	    first_raised_round: 5
1058	    last_seen_round: 11
1059	    mentions:
1060	      - round: 5
1061	        reviewers: [1, 2]
1062	        note: "两位 Reviewer 独立提出。"
1063	      - round: 6
1064	        reviewers: []
1065	        note: "Abstract L9 明确 semi-synthetic TweetEval (moderate Δπ) 限定。"
1066	      - round: 9
1067	        reviewers: [1, 2]
1068	        note: "再次提出。Abstract/Conclusion 已有 TweetEval 数据但权重仍不足。"
1069	      - round: 10
1070	        reviewers: [1, 2]
1071	        note: "R1-N2 + R2-W2 再次独立提出。RMSE 0.225 vs 0.124（1.8×）。headline 数字 'bias 0.059→0.010' 仅来自合成极端配置。论文在 Section 5.3 诚实讨论但 abstract/intro 叙事选择性。R1 建议 'never worse' 保险策略定位。共识：Abstract 需平衡正负结果权重。"
1072	      - round: 11
1073	        reviewers: [1, 2]
1074	        note: "R2-W3 标 major。R1 交叉部分同意：Abstract 遗漏 TweetEval 负面结果（aggregate RMSE 0.225 > Global 0.107）。R1 认为标题 'When' 已限定条件性。共识：Abstract 需平衡呈现。"
1075	    action_items:
1076	      - round: 6
1077	        action: "Abstract L9 具体 semi-synthetic 限定"
1078	        assigned_to: director
1079	        status: done
1080	      - round: 9
1081	        action: "Abstract 换入 TweetEval RMSE 数据；Conclusion 加 boundary condition"
1082	        assigned_to: director
1083	        status: done
1084	      - round: 10
1085	        action: "Abstract/Intro headline 数字应同时引用合成正面和半合成负面结果，确保对等权重"
1086	        assigned_to: director
1087	        status: pending
1088	    reso
…[truncated 9121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-23T06:22:37.548482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
  "offset": "1340",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/662a2980-42a8-4643-ba87-bf7b99e8fec6/tool-results/bvurgjm3b.txt",
    "offset": "1340",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-23T06:22:37.548998+00:00_

1340	        note: "R2-W3 标 major。R1 rebut 认为区别比 R2 暗示的更本质（mixing matrix algebra vs OLS projection，不可通过变量替换互推），但同意论文应在 Section 2/3 加 1-2 段公式级对比。共识方向一致：应加公式级对比。分歧在于区别程度（R1 认为更本质，R2 认为可能是 specialization）。"
1341	      - round: 11
1342	        reviewers: [1, 2]
1343	        note: "R2-W2 中隐含涉及（novelty 论证引用 F-L）。R1 在 rebut R2-W2 时明确区分 F-L 同质衰减 vs Theorem 1 异质偏差放大。论文层面公式级对比仍缺失。"
1344	    action_items:
1345	      - round: 10
1346	        action: "Section 2 或 Section 3 加 1-2 段与 F-L (2003) 的公式级对比：(a) F-L 分析 naive attenuation vs Theorem 1 分析 correction-induced bias；(b) F-L 无 δ_s 项；(c) OLS projection vs mixing matrix algebra"
1347	        assigned_to: director
1348	        status: pending
1349	    resolution: ""
1350	    resolution_round: null
1351	
1352	  - id: "R10-W2"
1353	    summary: "DGP 较简单（Y = τ(Z)·T + ε），无混杂变量"
1354	    category: experiment
1355	    severity: info
1356	    status: open
1357	    first_raised_round: 10
1358	    last_seen_round: 11
1359	    mentions:
1360	      - round: 10
1361	        reviewers: [1]
1362	        note: "R1-W2：观察性研究中混杂因素可能同时影响 Z 的分类准确率和处理效应，使 (A1) 更难成立。"
1363	      - round: 11
1364	        reviewers: [1]
1365	        note: "R1 在 Detailed Section Comments (Section 5) 中再次提及：合成实验 T~Bernoulli(0.5) 独立于协变量（无混杂），有混杂设置下 EC-HTE 表现未验证。"
1366	    action_items: []
1367	    resolution: "Rebuttal 项。"
1368	    resolution_round: null
1369	
1370	  - id: "R10-MR1"
1371	    summary: "遗漏 Dorn, Guo, and Kallus (2022) 处理效应误差灵敏度分析 + Lash, Fox, Fink (2009)"
1372	    category: writing
1373	    severity: info
1374	    status: open
1375	    first_raised_round: 10
1376	    last_seen_round: 10
1377	    mentions:
1378	      - round: 10
1379	        reviewers: [1, 2]
1380	        note: "R2-MR1 提出 Dorn et al.，R1 同意。R1 单独提出 Lash et al. (2009) 与 'when correction hurts' 直接相关。两篇可用于 (A1) sensitivity analysis 的方法论支撑。"
1381	      - round: 11
1382	        reviewers: []
1383	        note: "本轮未被直接提及，待 Research Director 确认。"
1384	    action_items: []
1385	    resolution: ""
1386	  
…[truncated 3927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-23T06:27:34.431404+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "issues_yaml": "issues:\n  # === RESOLVED (prior rounds, unchanged) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"JOINT-F1\"\n    summary: \"Tightness ratio 数值不一致\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"精确恒等式使问题消解\"\n    resolution_round: 0\n\n  - id: \"R2-W4\"\n    summary: \"DSL 区分不充分\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Related Work + Appendix E 清晰技术区分 + DSL 等价性证明\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Causal Forest uncertainty propagation 不清楚\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Plug-in SE 明确承认为 limitation\"\n    resolution_round: 1\n\n  - id: \"R1-V2-W4\"\n    summary: \"Moderate regime 实用价值有限\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"三处一致阐述适用条件\"\n    resolution_round: 1\n\n  - id: \"R1-V2-W5\"\n    summary: \"Imai & Yamamoto 区分仅一句话\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"三层区分已足够\"\n    resolution_round: 1\n\n  - id: \"MED-W1\"\n    summary: \"PPCI 互补性无实验证据\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"4-DGP 正交设计验证\"\n    resolution_round: 1\n\n  - id: \"MED-W2\"\n    summary: \"诊断 AUC 仅在 Abstract\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Section 5.4 + Figure 3\"\n    resolution_round: 1\n\n  - id: \"MED-W3\"\n    summary: \"Theorem 1 缺 MC 验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"520 configs MC 验证\"\n    resolution_round: 1\n\n  - id: \"MED-W4\"\n    summary: \"论文无 Figure\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文 2 figures + 1 table\"\n    resolution_round: 1\n\n  - id: \"MED-W5\"\n    summary: \"无合成数据 regime sweep\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整合成 regime sweep\"\n    resolution_round: 1\n\n  - id: \"MED-W6\"\n    summary: \"Abstract 与 Table 1 数字不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"数字一致\"\n    resolution_round: 1\n\n  - id: \"MED-W7\"\n    summary: \"无 CausalForest 结果\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"CausalForest 在 Table 1\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"加法式 CATE 注入未讨论\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Limitations + exp-018 乘法 DGP\"\n    resolution_round: 2\n\n  - id: \"R1-RD1-W3\"\n    summary: \"100 MC runs 无 SE\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Table 1 footnote + Appendix MC SE\"\n    resolution_round: 2\n\n  - id: \"RD2-W2\"\n    summary: \"诊断 setting-level AUC=0.47 + 循环依赖\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Δτ-free 诊断，setting AUC 0.47→0.889\"\n    resolution_round: 2\n\n  - id: \"RD2-W3\"\n    summary: \"A2+A3 假设过强，放松分析不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"exp-019: R²≥0.976 across P(Z=1)∈[0.1,0.5]\"\n    resolution_round: 2\n\n  - id: \"RD2-W6\"\n    summary: \"贡献列表 5 项偏多\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"5→3 项\"\n    resolution_round: 2\n\n  - id: \"RD2-W1\"\n    summary: \"g(π̄) 未给闭合形式\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Corollary 1 footnote 给出 J=3 显式表达式\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"遗漏 Fong & Tyler (2021)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"已添加引用\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"sui2026ppci 作者名有误\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"作者补全\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"统一术语\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Abstract 仅报 AUC=0.83\"\n    category: framing\n    severity: info\n    status: wont_fix\n    first_raised_round: 0\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Δτ-free 修复已提升 setting AUC 至 0.889\"\n    resolution_round: 2\n\n  - id: \"R1-RD1-W5\"\n    summary: \"无正面 real-data evidence\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    action_items: []\n    resolution: \"7 LLM × 2 datasets 验证。Civil Comments Δπ 确认写入论文。\"\n    resolution_round: 3\n\n  - id: \"R2-RD1-W3\"\n    summary: \"Multi-LLM 仅 OpenAI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    action_items: []\n    resolution: \"4 个开源 LLM + 3 个闭源 LLM\"\n    resolution_round: 2\n\n  - id: \"RD2-W4\"\n    summary: \"κ>100 阈值无依据\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    action_items: []\n    resolution: \"κ sweep 经验验证\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"50 MC seeds vs 100\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"100-seed 验证稳定性\"\n    resolution_round: 2\n\n  - id: \"RD2-M5\"\n    summary: \"Gamma(3,1) 敏感性范围过窄\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Gamma(3,1) 2×扰动下 RMSE 变化 ≤4%\"\n    resolution_round: 2\n\n  - id: \"RD2-W5\"\n    summary: \"子群定义缺乏外部效度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Limitations 已补充 text-feature vs demographic subgroup 讨论 + EC-HTE agnostic to subgroup definition 声明\"\n    resolution_round: 3\n\n  - id: \"RD2-F1\"\n    summary: \"正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Conclusion 压缩，主文 ≤ 8 页。PDF 视觉确认 Conclusion 在 page 8 结束。\"\n    resolution_round: 4\n\n  - id: \"R3F-N1\"\n    summary: \"Appendix B 证明中间步骤代数错误（最终结果正确）\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"错误推导路径已删除。保留正确的 δ_s 代换验证路径。\"\n    resolution_round: 4\n\n  - id: \"R3F-N2\"\n    summary: \"Abstract 过度突出合成极端配置结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    action_items: []\n    resolution: \"Abstract 加 (K=2, extreme Δπ) 条件限定 + L7 conditionality 声明\"\n    resolution_round: 4\n\n  - id: \"R3F-W1\"\n    summary: \"主文未点明实验已联合违反 (A2)+(A3) 却仍有效\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"§5.5 明确声明联合假设违反下 coverage ≥0.93\"\n    resolution_round: 4\n\n  - id: \"R3F-W2\"\n    summary: \"遗漏因果推断中二元变量误分类的计量经济学文献\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Appendix 'Econometrics of binary misclassification' 段落\"\n    resolution_round: 4\n\n  - id: \"R3F-W3\"\n    summary: \"'50% of configurations' claim 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 9\n    action_items: []\n    resolution: \"Round 9：全部 5 处 50% claim 加 'across our parameter grid' 限定。\"\n    resolution_round: 9\n\n  - id: \"R3F-W4\"\n    summary: \"τ(z) 不依赖 S 的隐含假设未正式声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    action_items: []\n    resolution: \"(A5) 正式列出。L61 说明推广到 subgroup-specific Δτ_s。\"\n    resolution_round: 4\n\n  - id: \"R3F-W5\"\n    summary: \"部分 claims 统计显著性不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"§5.3 加 '(p=0.395 vs. Global, not statistically significant)' 标注\"\n    resolution_round: 4\n\n  - id: \"R3F-W6\"\n    summary: \"κ>100 singularity guard 阈值缺乏支撑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 6\n    action_items: []\n    resolution: \"method.tex 明确区分 κ>100 (numerical singularity guard) 与 κ≤1.25 (empirical applicability diagnostic)。\"\n    resolution_round: 6\n\n  - id: \"R3F-W7\"\n    summary: \"诊断 AUC=0.86 的 FP/FN 代价不对称未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Appendix 加 'Cost-asymmetric diagnostic thresholds' 段落\"\n    resolution_round: 4\n\n  - id: \"R3F-M1\"\n    summary: \"Section 3 缺直觉数值例子\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"页数极度紧张（8 页刚好）。Rebuttal 可补。\"\n    resolution_round: null\n\n  - id: \"R3F-M3\"\n    summary: \"Proposition 3 未推广到 asymmetric\"\n    category: method\n    severity: info\n    status: wont_fix\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Rebuttal 回应\"\n    resolution_round: null\n\n  - id: \"R5-N2\"\n    summary: \"Corollary (Appendix C) 多分类扩展 g(π̄) 仅对均匀 off-diagonal 成立但未标明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Corollary 声明加 'uniform off-diagonal misclassification' 限定。\"\n    resolution_round: 6\n\n  - id: \"R5-N4\"\n    summary: \"κ>100 singularity guard 与 Appendix R 证据存在~80倍差距\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"method.tex 明确区分两层阈值。\"\n    resolution_round: 6\n\n  - id: \"R5-W2\"\n    summary: \"Audinet de Pieuchon et al. (2025, EMNLP) 讨论严重不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 10\n    action_items: []\n    resolution: \"related_work.tex 已充分讨论 Audinet et al. (2025)。\"\n    resolution_round: 5\n\n  - id: \"R5-W4\"\n    summary: \"CausalForestDML 超参数未完整报告\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Appendix 加完整超参数。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Figure 5 (applicability frontier) 应从 Appendix 移入正文\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"页数限制，无法移入正文。已加 forward reference。\"\n    resolution_round: null\n\n  - id: \"R6-N1\"\n    summary: \"theory.tex 'four assumptions' 与实际列出的 (A1)-(A5) 不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    action_items: []\n    resolution: \"'four assumptions' → 'five assumptions'\"\n    resolution_round: 6\n\n  - id: \"R6-M1\"\n    summary: \"520 配置数无法从文档化 DGP 参数推导\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    action_items: []\n    resolution: \"520 = 26(Δπ) × 20(Δτ) K=2-only grid。统一修正。\"\n    resolution_round: 7\n\n  - id: \"R7-C1\"\n    summary: \"论文对 520 配置的描述与实际数据源不符 + 84.6% 无法复现\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    action_items: []\n    resolution: \"4 文件统一修正。84.6% 删除。编译通过。\"\n    resolution_round: 7\n\n  - id: \"R8-N1\"\n    summary: \"Semi-synthetic TweetEval failure case 正文讨论不够突出\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"§5.3 三因素分析 + 量化 budget threshold。\"\n    resolution_round: 8\n\n  - id: \"R8-W1\"\n    summary: \"核心理论与测量误差文献的技术区分在主文不清晰\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"Related Work §2 三层技术区分。\"\n    resolution_round: 8\n\n  - id: \"R8-W2\"\n    summary: \"CV(π_s) 诊断 setting-level AUC=0.97 优于 Proposition 3 的 0.89\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"§5.4 trade-off 讨论。\"\n    resolution_round: 8\n\n  - id: \"R8-W6\"\n    summary: \"代码和数据可用性未声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"Limitations 末尾：'Code and data generation scripts will be released upon acceptance.'\"\n    resolution_round: 8\n\n  - id: \"R8-W7\"\n    summary: \"Algorithm 1 fallback 到 C̄ 时 SE 使用哪个矩阵未明确\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"method.tex L29 明确。\"\n    resolution_round: 8\n\n  - id: \"R8-M1\"\n    summary: \"遗漏 Greenland (1980)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"related_work.tex L8 引用。\"\n    resolution_round: 8\n\n  - id: \"R5-N1\"\n    summary: \"Abstract notation 过度简化\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Abstract L2 使用精确符号 'proportional to δ_s·Δτ'。\"\n    resolution_round: 6\n\n  - id: \"R5-M1\"\n    summary: \"'50% of configurations' 仍突出但部分由参数网格决定\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 7\n    action_items: []\n    resolution: \"84.6% 删除，替换为理论引用。50% 加 K=2 限定词。\"\n    resolution_round: 7\n\n  - id: \"R9-N1\"\n    summary: \"Theorem 1 novelty overclaimed——'discover' 表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    action_items: []\n    resolution: \"全文统一为 'derive'。\"\n    resolution_round: 9\n\n  - id: \"R9-MR1\"\n    summary: \"遗漏 Feder et al. (2022) 和 Keith et al. (2020)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    action_items: []\n    resolution: \"related_work.tex L18 已包含。\"\n    resolution_round: 8\n\n  - id: \"R3F-M4\"\n    summary: \"'debiasing' 在 NLP 社区有歧义（fairness vs measurement error）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2-M3 再次提出但标 minor——脚注位置已改善，建议提升到 Abstract/正文。R1 同意。\"\n    action_items: []\n    resolution: \"introduction.tex L10 脚注。位置从 Section 3 提前到 Section 1。\"\n    resolution_round: 6\n\n  # === OPEN ISSUES (updated with Round 12 mentions) ===\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性有限\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"第六次复发。R2-W1 标 warning：per-subgroup CM inversion + HB 是识别问题后的自然解。R1 完全同意。R1 rebut R2-N3（Theorem 1 framing）时论证了 δ_s·Δτ 乘积结构与 F-L 同质衰减的实质性区别，但同意 EC-HTE 方法本身新颖性有限。共识：论文主要贡献在 problem identification + bias identity，EC-HTE 是 natural fix。\"\n    action_items:\n      - round: 10\n        action: \"考虑进一步弱化标题或 C2 定位，明确 EC-HTE 是 natural fix 而非 novel method\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3F-M2\"\n    summary: \"K>4 可扩展性未探索\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W2 标 warning：K=8 RMSE=0.340 远超 Global=0.168。R2 交叉同意。论文在 Limitations 提及但主文未给数字。\"\n    action_items: []\n    resolution: \"Rebuttal 回应：K 受 effect modifier levels 限制，K>4 在 CSS 实践中少见\"\n    resolution_round: null\n\n  - id: \"R5-N3\"\n    summary: \"Plug-in SE 近似的覆盖率缺口未量化（CausalForest 93.8% vs 名义 95%）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W3 标 warning。R2 rebut：1.2pp 在 100 MC 的 MC SE 范围内，论文 Appendix Y 已提供 bootstrap 替代方案。R1 同意 rebut 但建议在 Section 4.3 比较 DIM vs CF plug-in 校准差异。共识降为 should-fix。\"\n    action_items:\n      - round: 12\n        action: \"Section 4.3 添加一段比较 DIM 和 CausalForest 下 plug-in SE 的校准差异\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W1\"\n    summary: \"Semi-synthetic TweetEval 中 EC-HTE 未优于 Global，但 Abstract/Intro 叙事以正面结果为主\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-N2 标 critical：Table 1 仅展示 extreme heterogeneity 有利结果。R2 rebut：Section 5.3 主文已坦诚报告 RMSE=0.225 vs 0.124（非 buried），但部分同意 Table 1 应更平衡。共识：Table 1 应包含 moderate 或 TweetEval 配置，p=0.395 应出现在主文中。\"\n    action_items:\n      - round: 12\n        action: \"Table 1 增加 TweetEval 或 moderate heterogeneity 配置行；Section 5.3 主文加 p=0.395\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W3\"\n    summary: \"缺乏完全真实因果数据验证——所有 CATE 为合成注入\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-N2 标 critical，R1-W6 标 warning。R1 在交叉中认为降为 should-fix 更合理——获取 RCT+CATE+LLM 数据集客观困难，核心贡献是理论恒等式不依赖实验验证，11 组真实 LLM CM 的 R²=0.975 提供部分外部效度。共识方向：should-fix（Limitations 加强讨论），非 must-fix。\"\n    action_items: []\n    resolution: \"结构性限制。Rebuttal 回应：CATE ground truth 需 RCT，不可能完全真实。\"\n    resolution_round: null\n\n  - id: \"R5-W5\"\n    summary: \"(A5) 违反仅做有限测试——Appendix O 仅 1 模型、K=2、50 MC runs\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 单独提及。论文 Section 3 L63-64 已添加 Corollary 和推广讨论。Appendix Z.1 有 aligned/adversarial 两种 A5 违反设置。可能已被部分覆盖，待确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W3\"\n    summary: \"合成 DGP 中 equal subgroup weights (w_s=1/K) 可能高估 EC-HTE 优势\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被直接提及。TweetEval 使用不均衡子群（38%/38%/12%/12%），部分覆盖此问题。\"\n    action_items: []\n    resolution: \"Rebuttal 项。\"\n    resolution_round: null\n\n  - id: \"R8-W4\"\n    summary: \"EC-HTE vs Stratified MLE bias 增量仅 0.002\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被直接提及。Appendix I Table 3 低预算对比已提供——HB vs MLE 差异主要在低预算区间。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"Corollary 1 证明不完整——h(j,j') 未推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。Appendix C Corollary 1 proof 已补充 uniform off-diagonal 下的推导。non-uniform 情况标注为 limitation。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-M2\"\n    summary: \"可补充 Wang et al. (2020) PNAS 和 Yadlowsky et al. (2024)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。Wang et al. (2020) 已在 related_work.tex L22 引用。\"\n    action_items: []\n    resolution: \"Rebuttal 项。\"\n    resolution_round: null\n\n  - id: \"R9-W1\"\n    summary: \"正文缺少 EC-HTE 不适用场景的决策树/流程图\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2 在 Questions 中提到 K=2 场景替代决策策略缺失。方向一致但未列为独立 weakness。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W2\"\n    summary: \"Assumption (A2) 对称误差在实际 LLM 标注中普遍不成立，正文讨论不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W5 标 warning。R2 rebut：EC-HTE 方法不依赖 (A2)，Remark 2 + Appendix D 处理非对称。R1 混淆了 Theorem 1 标量形式限制与方法限制。共识：方法本身 sound，但正文应更显著整合非对称扩展，诊断在非对称下 AUC 从 0.86 降至 0.82 需更明确讨论。\"\n    action_items:\n      - round: 12\n        action: \"Section 3 Remark 扩充非对称讨论 + 诊断 AUC 降幅在主文提及\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W3\"\n    summary: \"有限样本余项 R_n = O_p(n^{-1/2}·κ) 未给推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。Appendix Y L1063-1065 已有 matrix perturbation 推导。可能已解决。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-N1\"\n    summary: \"(A1) 条件独立性假设不可检验且敏感性分析范围有限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W3 标 warning：γ=0.2 是否代表真实 NLP 场景？R1 rebut：γ=0.2 已极端（误分类率随 outcome 变化 ±20%），若 γ>>0.2 则所有 CM 方法均失效——非 EC-HTE 特有弱点。论文已引用 sensitivity frameworks (Lash 2009, Dorn 2022)。共识降为 should-fix。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W1\"\n    summary: \"与 Frazis-Loewenstein (2003) 的公式级区分缺失\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-N3 标 critical：Theorem 1 是 F-L 标量衰减在 effect modifier 场景的直接推广。R1 rebut 降为 should-fix：F-L 分析 ATE 标量衰减 vs Theorem 1 分析 correction-induced 子群偏差（δ_s·Δτ 乘积结构），结构上不可互推。Appendix Z.4 Table 28 实证表明 F-L 标量矫正在异质设定下反而增加 bias。共识：应在 Section 2-3 加公式级对比但不构成 must-fix。\"\n    action_items:\n      - round: 12\n        action: \"Section 2 或 Section 3 加 1-2 段与 F-L (2003) 的公式级对比\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单（Y = τ(Z)·T + ε），无混杂变量\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被直接提及。Appendix Z.3 已有 confounded DGP 实验（IPW-DIM，β∈{0.25-2.0}），EC-HTE coverage ≥94.5%。可能已覆盖。\"\n    action_items: []\n    resolution: \"Rebuttal 项。\"\n    resolution_round: null\n\n  - id: \"R10-MR1\"\n    summary: \"遗漏 Dorn, Guo, and Kallus (2022) 和 Lash, Fox, Fink (2009)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。检查论文：theory.tex L76 已引用 lash2009applying 和 dorn2022sharp。\"\n    action_items: []\n    resolution: \"theory.tex L76 已引用。\"\n    resolution_round: 12\n\n  - id: \"R11-F1\"\n    summary: \"正文超出 8 页限制\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2 格式合规检查：正文 ≤ 8 页 ✓。视觉审查确认无 margin 溢出。已修复。\"\n    action_items: []\n    resolution: \"正文收在 8 页内。视觉审查和 R2 格式检查均确认合规。\"\n    resolution_round: 12\n\n  - id: \"R11-W1\"\n    summary: \"(A3) P(Z=1)=0.5 等概率假设限制泛化性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被直接提及。论文 Section 3 L68-70 已讨论放松路径 + Appendix T 有 P(Z=1) sweep。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W2\"\n    summary: \"κ>100 奇异性保护阈值无消融实验支撑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。Appendix A L34-42 已有 κ∈{10,25,50,100,200,500,1000} 消融实验。\"\n    action_items: []\n    resolution: \"Appendix A κ sweep 消融完成。\"\n    resolution_round: 12\n\n  - id: \"R11-W3\"\n    summary: \"'estimator-agnostic' 措辞过强——仅验证 3 种估计器\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。论文措辞已改为 'compatible with a range of CATE estimators'（related_work.tex L21）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W4\"\n    summary: \"Theorem/Proposition/Remark 编号混用共享计数器\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 小问题提及 Remark 2 与 Theorem 1 假设列表的表面矛盾。R2 解释为 progressive relaxation 而非矛盾。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-MR1\"\n    summary: \"遗漏 Semenova & Chernozhukov (2021)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"related_work.tex L19 已引用 semenova2021debiased。\"\n    action_items: []\n    resolution: \"related_work.tex L19 已引用。\"\n    resolution_round: 12\n\n  - id: \"R11-MR2\"\n    summary: \"遗漏 Blackwell, Honaker, and King (2017)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"related_work.tex L12 已引用 blackwell2017unified。\"\n    action_items: []\n    resolution: \"related_work.tex L12 已引用。\"\n    resolution_round: 12\n\n  # === Round 12 NEW ISSUES ===\n\n  - id: \"R12-N1\"\n    summary: \"Abstract 对 Diagnostic AUC 选择性报告——仅报合成 0.86 未报真实 LLM 0.63\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立标为 critical 并交叉完全同意。Abstract 报告 AUC=0.86（合成对称误差），未提及真实 LLM CM AUC=0.63 和 K=2 反向预测（AUC=0.03）。R2 建议将 diagnostic 降级为辅助工具。历史上 diagnostic 呈现问题多次出现（R2-W5, MED-W2）但此前修复侧重于其他方面。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 同时报告合成和真实 AUC（或范围 0.63-0.86），加 symmetric error 条件限定；考虑将 diagnostic 从独立贡献降级为辅助工具\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W1\"\n    summary: \"Expert label 获取成本的 cost-benefit 分析缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W2 提出，R1 交叉完全同意。K=4 P(Z_min)=0.25 需 n_expert≥400。如果有此预算为何不直接增加专家标注？Appendix I budget curves 部分回应但未从经济成本角度分析。\"\n    action_items:\n      - round: 12\n        action: \"Limitations 或 Section 4 增加 cost-benefit 讨论\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W2\"\n    summary: \"Algorithm 1 Step 2-3 'corrected labels' vs 'corrected moments' 歧义\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W1 提出，R2 交叉完全同意。Step 2 矫正聚合统计量但 Step 3 写 'Train CausalForest on corrected labels'。不是技术错误但措辞混淆。\"\n    action_items:\n      - round: 12\n        action: \"Algorithm 1 明确描述 CausalForest 流程——pre-correction vs post-correction\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W3\"\n    summary: \"Abstract 信息密度过高，对非因果推断 NLP 读者不友好\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 交叉同意。第一句直接进入技术细节，未为非专业读者建立背景。建议开头加一句通俗描述。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 首句改为建立问题的通俗描述\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M1\"\n    summary: \"Abstract '11 real LLM confusion matrices' vs Appendix 16 个组合数字不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 小问题提出，R2 交叉同意。可能是 11 个唯一 model-level CM vs 16 个 model×dataset×K 组合，但措辞有歧义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 声称 Theorem 1 'does not require (A2)' 但 Theorem 1 假设列表含 (A1)-(A5)——表面矛盾\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 小问题提出。R2 解释为 progressive relaxation（先给强假设下简洁结果再 remark 放松），非逻辑矛盾。R2 建议将 Theorem 1 改为 (A1),(A3)-(A5) 并将 (A2) 降为 simplifying assumption。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M3\"\n    summary: \"Section 4.1 '21 of 24 configurations' 无上下文——24 的定义需翻到 Appendix\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 小问题提出，R2 交叉同意。主文应简要说明 24 configurations 的定义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "issues_yaml": "issues:\n  # === RESOLVED (prior rounds, unchanged) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"JOINT-F1\"\n    summary: \"Tightness ratio 数值不一致\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"精确恒等式使问题消解\"\n    resolution_round: 0\n\n  - id: \"R2-W4\"\n    summary: \"DSL 区分不充分\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Related Work + Appendix E 清晰技术区分 + DSL 等价性证明\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Causal Forest uncertainty propagation 不清楚\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Plug-in SE 明确承认为 limitation\"\n    resolution_round: 1\n\n  - id: \"R1-V2-W4\"\n    summary: \"Moderate regime 实用价值有限\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"三处一致阐述适用条件\"\n    resolution_round: 1\n\n  - id: \"R1-V2-W5\"\n    summary: \"Imai & Yamamoto 区分仅一句话\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"三层区分已足够\"\n    resolution_round: 1\n\n  - id: \"MED-W1\"\n    summary: \"PPCI 互补性无实验证据\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"4-DGP 正交设计验证\"\n    resolution_round: 1\n\n  - id: \"MED-W2\"\n    summary: \"诊断 AUC 仅在 Abstract\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Section 5.4 + Figure 3\"\n    resolution_round: 1\n\n  - id: \"MED-W3\"\n    summary: \"Theorem 1 缺 MC 验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"520 configs MC 验证\"\n    resolution_round: 1\n\n  - id: \"MED-W4\"\n    summary: \"论文无 Figure\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文 2 figures + 1 table\"\n    resolution_round: 1\n\n  - id: \"MED-W5\"\n    summary: \"无合成数据 regime sweep\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整合成 regime sweep\"\n    resolution_round: 1\n\n  - id: \"MED-W6\"\n    summary: \"Abstract 与 Table 1 数字不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"数字一致\"\n    resolution_round: 1\n\n  - id: \"MED-W7\"\n    summary: \"无 CausalForest 结果\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"CausalForest 在 Table 1\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"加法式 CATE 注入未讨论\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Limitations + exp-018 乘法 DGP\"\n    resolution_round: 2\n\n  - id: \"R1-RD1-W3\"\n    summary: \"100 MC runs 无 SE\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Table 1 footnote + Appendix MC SE\"\n    resolution_round: 2\n\n  - id: \"RD2-W2\"\n    summary: \"诊断 setting-level AUC=0.47 + 循环依赖\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Δτ-free 诊断，setting AUC 0.47→0.889\"\n    resolution_round: 2\n\n  - id: \"RD2-W3\"\n    summary: \"A2+A3 假设过强，放松分析不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"exp-019: R²≥0.976 across P(Z=1)∈[0.1,0.5]\"\n    resolution_round: 2\n\n  - id: \"RD2-W6\"\n    summary: \"贡献列表 5 项偏多\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"5→3 项\"\n    resolution_round: 2\n\n  - id: \"RD2-W1\"\n    summary: \"g(π̄) 未给闭合形式\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Corollary 1 footnote 给出 J=3 显式表达式\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"遗漏 Fong & Tyler (2021)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"已添加引用\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"sui2026ppci 作者名有误\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"作者补全\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"统一术语\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Abstract 仅报 AUC=0.83\"\n    category: framing\n    severity: info\n    status: wont_fix\n    first_raised_round: 0\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Δτ-free 修复已提升 setting AUC 至 0.889\"\n    resolution_round: 2\n\n  - id: \"R1-RD1-W5\"\n    summary: \"无正面 real-data evidence\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    action_items: []\n    resolution: \"7 LLM × 2 datasets 验证。Civil Comments Δπ 确认写入论文。\"\n    resolution_round: 3\n\n  - id: \"R2-RD1-W3\"\n    summary: \"Multi-LLM 仅 OpenAI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    action_items: []\n    resolution: \"4 个开源 LLM + 3 个闭源 LLM\"\n    resolution_round: 2\n\n  - id: \"RD2-W4\"\n    summary: \"κ>100 阈值无依据\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    action_items: []\n    resolution: \"κ sweep 经验验证\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"50 MC seeds vs 100\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"100-seed 验证稳定性\"\n    resolution_round: 2\n\n  - id: \"RD2-M5\"\n    summary: \"Gamma(3,1) 敏感性范围过窄\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Gamma(3,1) 2×扰动下 RMSE 变化 ≤4%\"\n    resolution_round: 2\n\n  - id: \"RD2-W5\"\n    summary: \"子群定义缺乏外部效度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Limitations 已补充 text-feature vs demographic subgroup 讨论 + EC-HTE agnostic to subgroup definition 声明\"\n    resolution_round: 3\n\n  - id: \"RD2-F1\"\n    summary: \"正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Conclusion 压缩，主文 ≤ 8 页。PDF 视觉确认 Conclusion 在 page 8 结束。\"\n    resolution_round: 4\n\n  - id: \"R3F-N1\"\n    summary: \"Appendix B 证明中间步骤代数错误（最终结果正确）\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"错误推导路径已删除。保留正确的 δ_s 代换验证路径。\"\n    resolution_round: 4\n\n  - id: \"R3F-N2\"\n    summary: \"Abstract 过度突出合成极端配置结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    action_items: []\n    resolution: \"Abstract 加 (K=2, extreme Δπ) 条件限定 + L7 conditionality 声明\"\n    resolution_round: 4\n\n  - id: \"R3F-W1\"\n    summary: \"主文未点明实验已联合违反 (A2)+(A3) 却仍有效\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"§5.5 明确声明联合假设违反下 coverage ≥0.93\"\n    resolution_round: 4\n\n  - id: \"R3F-W2\"\n    summary: \"遗漏因果推断中二元变量误分类的计量经济学文献\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Appendix 'Econometrics of binary misclassification' 段落\"\n    resolution_round: 4\n\n  - id: \"R3F-W3\"\n    summary: \"'50% of configurations' claim 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 9\n    action_items: []\n    resolution: \"Round 9：全部 5 处 50% claim 加 'across our parameter grid' 限定。\"\n    resolution_round: 9\n\n  - id: \"R3F-W4\"\n    summary: \"τ(z) 不依赖 S 的隐含假设未正式声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    action_items: []\n    resolution: \"(A5) 正式列出。L61 说明推广到 subgroup-specific Δτ_s。\"\n    resolution_round: 4\n\n  - id: \"R3F-W5\"\n    summary: \"部分 claims 统计显著性不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"§5.3 加 '(p=0.395 vs. Global, not statistically significant)' 标注\"\n    resolution_round: 4\n\n  - id: \"R3F-W6\"\n    summary: \"κ>100 singularity guard 阈值缺乏支撑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 6\n    action_items: []\n    resolution: \"method.tex 明确区分 κ>100 (numerical singularity guard) 与 κ≤1.25 (empirical applicability diagnostic)。\"\n    resolution_round: 6\n\n  - id: \"R3F-W7\"\n    summary: \"诊断 AUC=0.86 的 FP/FN 代价不对称未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Appendix 加 'Cost-asymmetric diagnostic thresholds' 段落\"\n    resolution_round: 4\n\n  - id: \"R3F-M1\"\n    summary: \"Section 3 缺直觉数值例子\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"页数极度紧张（8 页刚好）。Rebuttal 可补。\"\n    resolution_round: null\n\n  - id: \"R3F-M3\"\n    summary: \"Proposition 3 未推广到 asymmetric\"\n    category: method\n    severity: info\n    status: wont_fix\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Rebuttal 回应\"\n    resolution_round: null\n\n  - id: \"R5-N2\"\n    summary: \"Corollary (Appendix C) 多分类扩展 g(π̄) 仅对均匀 off-diagonal 成立但未标明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Corollary 声明加 'uniform off-diagonal misclassification' 限定。\"\n    resolution_round: 6\n\n  - id: \"R5-N4\"\n    summary: \"κ>100 singularity guard 与 Appendix R 证据存在~80倍差距\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"method.tex 明确区分两层阈值。\"\n    resolution_round: 6\n\n  - id: \"R5-W2\"\n    summary: \"Audinet de Pieuchon et al. (2025, EMNLP) 讨论严重不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 10\n    action_items: []\n    resolution: \"related_work.tex 已充分讨论 Audinet et al. (2025)。\"\n    resolution_round: 5\n\n  - id: \"R5-W4\"\n    summary: \"CausalForestDML 超参数未完整报告\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Appendix 加完整超参数。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Figure 5 (applicability frontier) 应从 Appendix 移入正文\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"页数限制，无法移入正文。已加 forward reference。\"\n    resolution_round: null\n\n  - id: \"R6-N1\"\n    summary: \"theory.tex 'four assumptions' 与实际列出的 (A1)-(A5) 不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    action_items: []\n    resolution: \"'four assumptions' → 'five assumptions'\"\n    resolution_round: 6\n\n  - id: \"R6-M1\"\n    summary: \"520 配置数无法从文档化 DGP 参数推导\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    action_items: []\n    resolution: \"520 = 26(Δπ) × 20(Δτ) K=2-only grid。统一修正。\"\n    resolution_round: 7\n\n  - id: \"R7-C1\"\n    summary: \"论文对 520 配置的描述与实际数据源不符 + 84.6% 无法复现\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    action_items: []\n    resolution: \"4 文件统一修正。84.6% 删除。编译通过。\"\n    resolution_round: 7\n\n  - id: \"R8-N1\"\n    summary: \"Semi-synthetic TweetEval failure case 正文讨论不够突出\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"§5.3 三因素分析 + 量化 budget threshold。\"\n    resolution_round: 8\n\n  - id: \"R8-W1\"\n    summary: \"核心理论与测量误差文献的技术区分在主文不清晰\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"Related Work §2 三层技术区分。\"\n    resolution_round: 8\n\n  - id: \"R8-W2\"\n    summary: \"CV(π_s) 诊断 setting-level AUC=0.97 优于 Proposition 3 的 0.89\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"§5.4 trade-off 讨论。\"\n    resolution_round: 8\n\n  - id: \"R8-W6\"\n    summary: \"代码和数据可用性未声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"Limitations 末尾：'Code and data generation scripts will be released upon acceptance.'\"\n    resolution_round: 8\n\n  - id: \"R8-W7\"\n    summary: \"Algorithm 1 fallback 到 C̄ 时 SE 使用哪个矩阵未明确\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"method.tex L29 明确。\"\n    resolution_round: 8\n\n  - id: \"R8-M1\"\n    summary: \"遗漏 Greenland (1980)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 8\n    action_items: []\n    resolution: \"related_work.tex L8 引用。\"\n    resolution_round: 8\n\n  - id: \"R5-N1\"\n    summary: \"Abstract notation 过度简化\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Abstract L2 使用精确符号 'proportional to δ_s·Δτ'。\"\n    resolution_round: 6\n\n  - id: \"R5-M1\"\n    summary: \"'50% of configurations' 仍突出但部分由参数网格决定\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 7\n    action_items: []\n    resolution: \"84.6% 删除，替换为理论引用。50% 加 K=2 限定词。\"\n    resolution_round: 7\n\n  - id: \"R9-N1\"\n    summary: \"Theorem 1 novelty overclaimed——'discover' 表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    action_items: []\n    resolution: \"全文统一为 'derive'。\"\n    resolution_round: 9\n\n  - id: \"R9-MR1\"\n    summary: \"遗漏 Feder et al. (2022) 和 Keith et al. (2020)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    action_items: []\n    resolution: \"related_work.tex L18 已包含。\"\n    resolution_round: 8\n\n  - id: \"R3F-M4\"\n    summary: \"'debiasing' 在 NLP 社区有歧义（fairness vs measurement error）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2-M3 再次提出但标 minor——脚注位置已改善，建议提升到 Abstract/正文。R1 同意。\"\n    action_items: []\n    resolution: \"introduction.tex L10 脚注。位置从 Section 3 提前到 Section 1。\"\n    resolution_round: 6\n\n  # === OPEN ISSUES (updated with Round 12 mentions) ===\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性有限\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"第六次复发。R2-W1 标 warning：per-subgroup CM inversion + HB 是识别问题后的自然解。R1 完全同意。R1 rebut R2-N3（Theorem 1 framing）时论证了 δ_s·Δτ 乘积结构与 F-L 同质衰减的实质性区别，但同意 EC-HTE 方法本身新颖性有限。共识：论文主要贡献在 problem identification + bias identity，EC-HTE 是 natural fix。\"\n    action_items:\n      - round: 10\n        action: \"考虑进一步弱化标题或 C2 定位，明确 EC-HTE 是 natural fix 而非 novel method\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3F-M2\"\n    summary: \"K>4 可扩展性未探索\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W2 标 warning：K=8 RMSE=0.340 远超 Global=0.168。R2 交叉同意。论文在 Limitations 提及但主文未给数字。\"\n    action_items: []\n    resolution: \"Rebuttal 回应：K 受 effect modifier levels 限制，K>4 在 CSS 实践中少见\"\n    resolution_round: null\n\n  - id: \"R5-N3\"\n    summary: \"Plug-in SE 近似的覆盖率缺口未量化（CausalForest 93.8% vs 名义 95%）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W3 标 warning。R2 rebut：1.2pp 在 100 MC 的 MC SE 范围内，论文 Appendix Y 已提供 bootstrap 替代方案。R1 同意 rebut 但建议在 Section 4.3 比较 DIM vs CF plug-in 校准差异。共识降为 should-fix。\"\n    action_items:\n      - round: 12\n        action: \"Section 4.3 添加一段比较 DIM 和 CausalForest 下 plug-in SE 的校准差异\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W1\"\n    summary: \"Semi-synthetic TweetEval 中 EC-HTE 未优于 Global，但 Abstract/Intro 叙事以正面结果为主\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-N2 标 critical：Table 1 仅展示 extreme heterogeneity 有利结果。R2 rebut：Section 5.3 主文已坦诚报告 RMSE=0.225 vs 0.124（非 buried），但部分同意 Table 1 应更平衡。共识：Table 1 应包含 moderate 或 TweetEval 配置，p=0.395 应出现在主文中。\"\n    action_items:\n      - round: 12\n        action: \"Table 1 增加 TweetEval 或 moderate heterogeneity 配置行；Section 5.3 主文加 p=0.395\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W3\"\n    summary: \"缺乏完全真实因果数据验证——所有 CATE 为合成注入\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-N2 标 critical，R1-W6 标 warning。R1 在交叉中认为降为 should-fix 更合理——获取 RCT+CATE+LLM 数据集客观困难，核心贡献是理论恒等式不依赖实验验证，11 组真实 LLM CM 的 R²=0.975 提供部分外部效度。共识方向：should-fix（Limitations 加强讨论），非 must-fix。\"\n    action_items: []\n    resolution: \"结构性限制。Rebuttal 回应：CATE ground truth 需 RCT，不可能完全真实。\"\n    resolution_round: null\n\n  - id: \"R5-W5\"\n    summary: \"(A5) 违反仅做有限测试——Appendix O 仅 1 模型、K=2、50 MC runs\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 单独提及。论文 Section 3 L63-64 已添加 Corollary 和推广讨论。Appendix Z.1 有 aligned/adversarial 两种 A5 违反设置。可能已被部分覆盖，待确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W3\"\n    summary: \"合成 DGP 中 equal subgroup weights (w_s=1/K) 可能高估 EC-HTE 优势\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被直接提及。TweetEval 使用不均衡子群（38%/38%/12%/12%），部分覆盖此问题。\"\n    action_items: []\n    resolution: \"Rebuttal 项。\"\n    resolution_round: null\n\n  - id: \"R8-W4\"\n    summary: \"EC-HTE vs Stratified MLE bias 增量仅 0.002\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被直接提及。Appendix I Table 3 低预算对比已提供——HB vs MLE 差异主要在低预算区间。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"Corollary 1 证明不完整——h(j,j') 未推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。Appendix C Corollary 1 proof 已补充 uniform off-diagonal 下的推导。non-uniform 情况标注为 limitation。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-M2\"\n    summary: \"可补充 Wang et al. (2020) PNAS 和 Yadlowsky et al. (2024)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。Wang et al. (2020) 已在 related_work.tex L22 引用。\"\n    action_items: []\n    resolution: \"Rebuttal 项。\"\n    resolution_round: null\n\n  - id: \"R9-W1\"\n    summary: \"正文缺少 EC-HTE 不适用场景的决策树/流程图\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2 在 Questions 中提到 K=2 场景替代决策策略缺失。方向一致但未列为独立 weakness。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W2\"\n    summary: \"Assumption (A2) 对称误差在实际 LLM 标注中普遍不成立，正文讨论不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W5 标 warning。R2 rebut：EC-HTE 方法不依赖 (A2)，Remark 2 + Appendix D 处理非对称。R1 混淆了 Theorem 1 标量形式限制与方法限制。共识：方法本身 sound，但正文应更显著整合非对称扩展，诊断在非对称下 AUC 从 0.86 降至 0.82 需更明确讨论。\"\n    action_items:\n      - round: 12\n        action: \"Section 3 Remark 扩充非对称讨论 + 诊断 AUC 降幅在主文提及\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W3\"\n    summary: \"有限样本余项 R_n = O_p(n^{-1/2}·κ) 未给推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。Appendix Y L1063-1065 已有 matrix perturbation 推导。可能已解决。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-N1\"\n    summary: \"(A1) 条件独立性假设不可检验且敏感性分析范围有限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W3 标 warning：γ=0.2 是否代表真实 NLP 场景？R1 rebut：γ=0.2 已极端（误分类率随 outcome 变化 ±20%），若 γ>>0.2 则所有 CM 方法均失效——非 EC-HTE 特有弱点。论文已引用 sensitivity frameworks (Lash 2009, Dorn 2022)。共识降为 should-fix。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W1\"\n    summary: \"与 Frazis-Loewenstein (2003) 的公式级区分缺失\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-N3 标 critical：Theorem 1 是 F-L 标量衰减在 effect modifier 场景的直接推广。R1 rebut 降为 should-fix：F-L 分析 ATE 标量衰减 vs Theorem 1 分析 correction-induced 子群偏差（δ_s·Δτ 乘积结构），结构上不可互推。Appendix Z.4 Table 28 实证表明 F-L 标量矫正在异质设定下反而增加 bias。共识：应在 Section 2-3 加公式级对比但不构成 must-fix。\"\n    action_items:\n      - round: 12\n        action: \"Section 2 或 Section 3 加 1-2 段与 F-L (2003) 的公式级对比\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单（Y = τ(Z)·T + ε），无混杂变量\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被直接提及。Appendix Z.3 已有 confounded DGP 实验（IPW-DIM，β∈{0.25-2.0}），EC-HTE coverage ≥94.5%。可能已覆盖。\"\n    action_items: []\n    resolution: \"Rebuttal 项。\"\n    resolution_round: null\n\n  - id: \"R10-MR1\"\n    summary: \"遗漏 Dorn, Guo, and Kallus (2022) 和 Lash, Fox, Fink (2009)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。检查论文：theory.tex L76 已引用 lash2009applying 和 dorn2022sharp。\"\n    action_items: []\n    resolution: \"theory.tex L76 已引用。\"\n    resolution_round: 12\n\n  - id: \"R11-F1\"\n    summary: \"正文超出 8 页限制\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2 格式合规检查：正文 ≤ 8 页 ✓。视觉审查确认无 margin 溢出。已修复。\"\n    action_items: []\n    resolution: \"正文收在 8 页内。视觉审查和 R2 格式检查均确认合规。\"\n    resolution_round: 12\n\n  - id: \"R11-W1\"\n    summary: \"(A3) P(Z=1)=0.5 等概率假设限制泛化性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被直接提及。论文 Section 3 L68-70 已讨论放松路径 + Appendix T 有 P(Z=1) sweep。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W2\"\n    summary: \"κ>100 奇异性保护阈值无消融实验支撑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。Appendix A L34-42 已有 κ∈{10,25,50,100,200,500,1000} 消融实验。\"\n    action_items: []\n    resolution: \"Appendix A κ sweep 消融完成。\"\n    resolution_round: 12\n\n  - id: \"R11-W3\"\n    summary: \"'estimator-agnostic' 措辞过强——仅验证 3 种估计器\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"本轮未被提及。论文措辞已改为 'compatible with a range of CATE estimators'（related_work.tex L21）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W4\"\n    summary: \"Theorem/Proposition/Remark 编号混用共享计数器\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 小问题提及 Remark 2 与 Theorem 1 假设列表的表面矛盾。R2 解释为 progressive relaxation 而非矛盾。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-MR1\"\n    summary: \"遗漏 Semenova & Chernozhukov (2021)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"related_work.tex L19 已引用 semenova2021debiased。\"\n    action_items: []\n    resolution: \"related_work.tex L19 已引用。\"\n    resolution_round: 12\n\n  - id: \"R11-MR2\"\n    summary: \"遗漏 Blackwell, Honaker, and King (2017)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"related_work.tex L12 已引用 blackwell2017unified。\"\n    action_items: []\n    resolution: \"related_work.tex L12 已引用。\"\n    resolution_round: 12\n\n  # === Round 12 NEW ISSUES ===\n\n  - id: \"R12-N1\"\n    summary: \"Abstract 对 Diagnostic AUC 选择性报告——仅报合成 0.86 未报真实 LLM 0.63\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立标为 critical 并交叉完全同意。Abstract 报告 AUC=0.86（合成对称误差），未提及真实 LLM CM AUC=0.63 和 K=2 反向预测（AUC=0.03）。R2 建议将 diagnostic 降级为辅助工具。历史上 diagnostic 呈现问题多次出现（R2-W5, MED-W2）但此前修复侧重于其他方面。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 同时报告合成和真实 AUC（或范围 0.63-0.86），加 symmetric error 条件限定；考虑将 diagnostic 从独立贡献降级为辅助工具\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W1\"\n    summary: \"Expert label 获取成本的 cost-benefit 分析缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W2 提出，R1 交叉完全同意。K=4 P(Z_min)=0.25 需 n_expert≥400。如果有此预算为何不直接增加专家标注？Appendix I budget curves 部分回应但未从经济成本角度分析。\"\n    action_items:\n      - round: 12\n        action: \"Limitations 或 Section 4 增加 cost-benefit 讨论\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W2\"\n    summary: \"Algorithm 1 Step 2-3 'corrected labels' vs 'corrected moments' 歧义\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W1 提出，R2 交叉完全同意。Step 2 矫正聚合统计量但 Step 3 写 'Train CausalForest on corrected labels'。不是技术错误但措辞混淆。\"\n    action_items:\n      - round: 12\n        action: \"Algorithm 1 明确描述 CausalForest 流程——pre-correction vs post-correction\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W3\"\n    summary: \"Abstract 信息密度过高，对非因果推断 NLP 读者不友好\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 交叉同意。第一句直接进入技术细节，未为非专业读者建立背景。建议开头加一句通俗描述。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 首句改为建立问题的通俗描述\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M1\"\n    summary: \"Abstract '11 real LLM confusion matrices' vs Appendix 16 个组合数字不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 小问题提出，R2 交叉同意。可能是 11 个唯一 model-level CM vs 16 个 model×dataset×K 组合，但措辞有歧义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 声称 Theorem 1 'does not require (A2)' 但 Theorem 1 假设列表含 (A1)-(A5)——表面矛盾\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 小问题提出。R2 解释为 progressive relaxation（先给强假设下简洁结果再 remark 放松），非逻辑矛盾。R2 建议将 Theorem 1 改为 (A1),(A3)-(A5) 并将 (A2) 降为 simplifying assumption。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M3\"\n    summary: \"Section 4.1 '21 of 24 configurations' 无上下文——24 的定义需翻到 Appendix\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 小问题提出，R2 交叉同意。主文应简要说明 24 configurations 的定义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-23T06:27:34.532769+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml\", \"bytes\": 32878}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-23T06:29:39.538879+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_visual_check_status,submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_visual_check_status,submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-23T06:29:39.539339+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-23T06:29:41.647619+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-23T06:29:41.748539+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-23T06:29:43.556592+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-23T06:29:43.657767+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T06:07:41.574281+00:00\", \"completed_at\": \"2026-05-23T06:11:43.626408+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"从 Figure 1 (p2) 到 Table 1 (p7) 跨越 5 页，中间仅有 display equations 作为视觉元素，无 figure 或 table。审稿人滚动浏览此段会感到视觉单调。理论推导部分的 equations 有一定缓解作用，但对实证+理论混合型论文而言，这段 text desert 较长\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-8\", \"message\": \"主体正文 8 页仅含 3 个 display items（Figure 1, Table 1, Figure 2），密度偏低。大量实验结果（Tables 2-30, Figures 3-5）被推入 Appendix，主体缺乏视觉丰富度。建议考虑将 1-2 个关键 appendix 表格/图（如 budget sweep 的 Figure 4 或 cross-model consistency 的关键结果）提入主体\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 出现在第 2 页，提供了清晰的视觉锚点，展示 global vs. subgroup-stratified correction 的 bias 机制。三面板设计信息明确，caption 自包含，Title-Abstract-Figure 1 叙事一致。审稿人第一印象良好\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，最优结果加粗，精度一致（3 位小数），格式规范。列数适中，单栏放置合理\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 heatmap 设计得当——用 hatching 区分 \\\"debiasing helps\\\" vs \\\"hurts\\\" 区域，colorbar 清晰。但轴标签和 colorbar 刻度文字字号偏小（约为正文字号的 60-65%），打印时可能不够清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 29\", \"message\": \"Algorithm 1 伪代码占页面约 40-45%，下方约 55% 为空白。作为末页可接受，但如果空间紧张可考虑将 Algorithm 1 与前页合并\"}, {\"severity\": \"info\", \"dimension\": \"page 28\", \"message\": \"页面内容在约 60% 处结束，底部约 40% 空白。与 page 29 合计约 1 页空间未利用\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item（纯 Title/Abstract/Introduction），这在理论+方法型论文中常见，且 Figure 1 在紧邻的 page 2 出现，不构成问题\"}, {\"severity\": \"info\", \"dimension\": \"pages 4-5\", \"message\": \"数学公式渲染正确，Theorem 1、Proposition 3 排版清晰，无 LaTeX 错误残留。Assumptions (A1)-(A5) 格式统一\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"参考文献格式一致，无 [?] 未解析引用，无跳号。Author 缩写和年份格式统一\"}, {\"severity\": \"info\"
…[truncated 200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-23T06:31:47.734602+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 12 审稿报告：Error-Corrected Heterogeneous Treatment Effects\n\n**目标 Venue**: EMNLP 2026 (ARR May cycle)\n**审稿人**: Reviewer 1, Reviewer 2\n**交叉回应**: Reviewer 1 ↔ Reviewer 2 完成\n**Overall Score**: 3.5 (Borderline Conference)\n\n---\n\n## Summary\n\n本文研究 LLM 标注用于因果推断（HTE 估计）时，全局混淆矩阵校正在子组间引入系统性偏差的问题。主要贡献：(1) 推导精确偏差恒等式（Theorem 1），表明全局校正偏差与 δ_s·Δτ 成正比；(2) 提出 EC-HTE，基于分层贝叶斯估计子组混淆矩阵进行分组校正；(3) 给出无需估计处理效应的诊断准则（Proposition 3）。实验覆盖合成、半合成（TweetEval）及多个鲁棒性验证，展示 EC-HTE 在极端异质性条件下将偏差从 0.059 降至 0.010。\n\n论文技术扎实，理论推导严谨，实验设计全面。主要不足在于：(1) 诊断工具在真实 LLM 混淆矩阵上 AUC 降至 0.63，但摘要仅报告 0.86；(2) 方法论新颖性有限——EC-HTE 本质上是识别问题后的自然修复；(3) 缺乏真实因果数据集验证；(4) 主体正文视觉密度偏低，大量关键结果被推入 Appendix。\n\n---\n\n## Strengths\n\n1. **理论贡献清晰且可验证**：偏差恒等式（Theorem 1）提供了精确的解析形式，R²≥0.974 的经验验证令人信服。这一理论结果本身具有独立价值——即使不采用 EC-HTE，从业者也可据此判断全局校正何时有害。\n\n2. **实验覆盖面极广**：100 次 MC 重复、K∈{2,4,8}、对称/非对称混淆矩阵、6 个 OpenAI 模型 + 开源 LLM、hate speech 案例、子组误指定、A1 敏感性分析、混杂处理、R-learner 兼容性等——超过 20 个 Appendix 章节覆盖了几乎所有可预见的质疑。\n\n3. **方法论位置清晰**：准确定位 EC-HTE 与 PPI/DSL/PPCI 的关系——全局校正等价于 pooled DSL，EC-HTE 添加分层部分池化——避免了过度声称新颖性。\n\n4. **写作质量高**：主体正文在 8 页内呈现了完整的理论-方法-实验叙事，Introduction 的 Figure 1 三面板设计有效传达核心直觉。\n\n5. **实用性**：诊断准则（尽管有局限）和预算指南（Appendix 的 crossover curves）为从业者提供了可操作的工具。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则影响接收）\n\n**[W-MF1] 摘要诊断 AUC 选择性报告** [R1 AGREE, R2 AGREE — 共识]\n摘要称 \"AUC = 0.86\" 但仅限合成对称误差条件；在 16 个真实 LLM 模型-数据集组合上 AUC 降至 0.63（Appendix D.9）。对于 K=2，诊断甚至 anti-predict（§4.4 承认）。摘要应同时报告两个数字，或使用更保守的表述（如 \"AUC up to 0.86 under symmetric errors; 0.63 on real LLM confusion matrices\"）。这是诚实报告的问题，不修复会被审稿人标记为 misleading。\n\n**[W-MF2] 主结果表缺乏代表性** [R1 AGREE, R2 AGREE — 共识]\nTable 1 仅展示 extreme heterogeneity 配置，但 §4.3 承认 \"moderate heterogeneity 下方法趋同\"、\"TweetEval 半合成实验中 EC-HTE RMSE 高于 Global\"。主表应至少包含一个非极端配置（moderate 或 TweetEval），否则读者对方法的适用范围产生过于乐观的印象。当前 Table~\\ref{tab:main_supp} 在 Appendix 中，但这些是读者最需要在主体看到的结果。\n\n### Should-Fix（建议修复，不修复会扣分但不致命）\n\n**[W-SF1] Algorithm 1 描述歧义** [R1 AGREE, R2 AGREE — 共识]\nAlgorithm 1 Step 2 \"corrected labels\" 与 Step 3 的操作存在歧义——EC-HTE 校正的是 moments（期望值）而非逐条标签。建议明确使用 \"corrected outcome moments\" 或等价表述，避免与逐条标签校正方法（如 PPCI）混淆。\n\n**[W-SF2] K=8 可扩展性边界应在主体提及** [R1 AGREE, R2 AGREE — 共识]\nK=8 时 EC-HTE RMSE 超过 Global（Appendix D.16），这是方法的重要边界条件。当前仅在 Limitations 一笔带过。建议在 §4.3 加一句明确提及此边界，或在 Table 1 增加 K=8 行。\n\n**[W-SF3] 子组定义指导缺失** [R1 AGREE, R2 AGREE — 共识]\n论文使用 hashtag presence 和 text length 定义子组，但未讨论从业者如何选择子组变量。当子组定义本身与 LLM 误差模式相关（如按文本长度分组，而 LLM 在短文本上系统性更差），子组选择就不是中性的。需要至少一段讨论。\n\n**[W-SF4] 专家标注成本-收益分析不足** [R1 AGREE, R2 AGREE — 共识]\nEC-HTE 需要按子组分配专家标注（每子组 ≥25），但论文未讨论相比全局方法，额外的子组级标注成本是否值得。预算 crossover curves 在 Appendix 但应在主体简要总结。\n\n**[W-SF5] Theorem 1 \"exact identity\" 措辞** [R1 REBUT → R2 ACCEPT downgrade]\n经交叉讨论，R1 的反驳成立——Theorem 1 推导出的是 finite-sample exact identity（非渐近近似），且与 Firth-Liang 方法的区分是实质性的。但建议在 proof sketch 中更明确说明 \"exact\" 的含义（有限样本精确 vs. 渐近），避免歧义。降级为 should-fix。\n\n**[W-SF6] 缺乏真实因果数据集验证** [R1 AGREE, R2 AGREE — 共识]\n所有 CATE 均为合成注入（即使在 \"semi-synthetic\" 中，文本特征真实但效应人工注入）。论文在 Limitations 中承认这一点，并指出 \"suitable public benchmarks\" 不存在。审稿人理解这是结构性限制，但建议讨论是否可使用 LaLonde/IHDP 等经典因果数据集（即使非 NLP 领域）作为补充验证。\n\n### Minor\n\n**[W-M1] 摘要信息密度过高** [R1 AGREE, R2 AGREE — 共识]\n摘要包含 δ_s·Δτ 公式、R²≥0.97、AUC=0.86、5.9× 改善等密集技术细节，对非因果推断背景的 NLP 读者不够友好。建议简化数学表述，保留核心叙事。\n\n**[W-M2] 方法新颖性有限** [R1 AGREE, R2 AGREE — 共识]\nEC-HTE 的核心操作（分层贝叶斯混淆矩阵估计 + 矩校正）是识别问题后的自然修复步骤。主要贡献在于问题识别（偏差恒等式）而非解决方案本身。论文对此定位准确，但应进一步强调理论贡献的独立价值。\n\n**[W-M3] Figure 2 轴标签字号偏小**\nHeatmap 的轴标签和 colorbar 刻度约为正文字号的 60-65%，打印时可能不够清晰。\n\n**[W-M4] A2 对称假设的影响范围应澄清**\n经交叉讨论确认：A2（对称误分类）仅影响诊断准则（Proposition 3），不影响 EC-HTE 方法本身。建议在 Assumptions 列表中明确标注 A2 的适用范围（\"used only for the diagnostic\"）。\n\n**[W-M5] 主体 display item 密度偏低**\n8 页正文仅含 3 个 display items（Figure 1, Table 1, Figure 2），pages 3-6 为纯文本。建议考虑将 Appendix 中的 budget crossover figure 或 cross-model consistency 关键结果移入主体。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位审稿人达成完全共识：\n\n1. **诊断 AUC 报告问题是最关键的修复项**——摘要的选择性报告构成 misleading risk\n2. **Table 1 的代表性不足**——仅展示 extreme 配置给读者错误印象\n3. **理论贡献 > 方法贡献**——偏差恒等式是核心贡献，EC-HTE 是自然延伸\n4. **实验全面性是论文最大优势**——Appendix 的深度覆盖令人印象深刻\n5. **论文适合 EMNLP**——NLP+因果推断的交叉主题、LLM 标注校正的实用性\n\n## Reviewer Divergence\n\n以下问题经交叉讨论后解决，无残留分歧：\n\n1. **Theorem 1 \"exact identity\" 措辞**：R2 初审认为措辞有误导，R1 反驳 F-L 区分是实质性的。R2 接受降级为 should-fix，建议澄清 \"exact\" 的含义。\n2. **A2 对称假设**：R1 初审认为 A2 限制了方法通用性，R2 指出 EC-HTE 本身不依赖 A2。达成共识：仅诊断受影响，方法不受限。\n3. **SE plug-in 校准**：R1 标记 1.2pp 覆盖率缺口为 should-fix，R2 认为在 MC 误差范围内且提供了 bootstrap 替代方案。达成共识：minor issue。\n\n---\n\n## Questions for Authors\n\n1. 在 K=4 TweetEval 半合成实验中，EC-HTE 的 RMSE (0.225) 显著高于 Global (0.124)。能否提供子组级别的分解，说明 RMSE 增加主要来自哪些子组？是否存在子组级别 EC-HTE 优于 Global 的情况？\n\n2. 诊断准则在 K=2 时 anti-predict 的根本原因是 |δ₀|=|δ₁| 的代数约束。是否有修改诊断公式使其在 K=2 也可靠的理论路径？\n\n3. 分层贝叶斯的 Gamma(3,1) 超先验选择依据是什么？是否进行了先验敏感性分析？\n\n4. 子组变量选择（hashtag presence, text length）是否存在事后选择偏差？如果从业者尝试多个子组定义并选择\"最好\"的结果，如何控制多重比较问题？\n\n---\n\n## Missing References\n\n未发现明显遗漏的关键引用。论文对 PPI、DSL、PPCI 等核心竞争方法的引用完整。建议考虑引用：\n- Zrnic & Candès (2024) 关于 cross-prediction 的后续工作（如已发表）\n- 因果推断中测量误差校正的经典统计文献（如 Carroll et al., Measurement Error in Nonlinear Models）中与混淆矩阵反演直接相关的章节\n\n---\n\n## External Review\n\n未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成\n**结果**: 0 critical / 2 warning / 9 info\n\n**Warnings**:\n1. Pages 3-6 从 Figure 1 (p2) 到 Table 1 (p7) 跨越 5 页纯文本，视觉单调（text desert）。理论推导的 display equations 有一定缓解作用，但对实证+理论混合型论文而言偏长。\n2. 主体 8 页仅含 3 个 display items（Figure 1, Table 1, Figure 2），密度偏低。建议将 1-2 个关键 Appendix 表格/图提入主体。\n\n**Info（正面）**:\n- Figure 1 位置得当（p2），三面板设计清晰\n- Table 1 booktabs 格式规范，精度一致\n- Figure 2 heatmap hatching 区分有效\n- 数学公式渲染正确，无 LaTeX 错误\n- 参考文献格式统一，无未解析引用\n- 无 margin 溢出，符合 ACL 模板规范\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 — Borderline Conference**\n\n**理由**：\n\n论文在理论层面做出了有价值的贡献——偏差恒等式（Theorem 1）揭示了一个此前未被形式化的问题（全局混淆矩阵校正在子组间引入系统偏差），经验验证充分（R²≥0.97）。实验设计全面，鲁棒性验证覆盖面远超同类论文。\n\n阻碍更高评分的主要因素：\n1. **方法新颖性有限**：EC-HTE 是识别问题后的直接修复，贡献主要在问题发现而非解决方案\n2. **诊断工具实用性存疑**：核心卖点之一的诊断准则在真实 LLM 数据上 AUC 仅 0.63，K=2 时 anti-predict\n3. **摘要选择性报告**：AUC=0.86 的报告方式有 misleading risk，需立即修复\n4. **缺乏真实因果验证**：所有效应为合成注入，尽管是结构性限制但削弱了对实际场景有效性的信心\n5. **主表代表性不足**：仅展示 extreme 配置，隐藏了方法在中等异质性下的局限\n\n论文整体质量适合 Findings 接收（3.0），但理论贡献的清晰度和实验的全面性使其有机会进入主会议（borderline）。修复 W-MF1（AUC 报告）和 W-MF2（Table 1 代表性）后，论文竞争力将显著提升。\n\n---\n\n## Detailed Comments\n\n### 给作者的具体修改建议（按优先级排序）\n\n1. **摘要 AUC 报告**（Must-Fix）：将 \"AUC = 0.86\" 改为 \"AUC = 0.86 under synthetic symmetric errors (0.63 on real LLM confusion matrices)\" 或类似表述。\n\n2. **Table 1 扩展**（Must-Fix）：增加 moderate heterogeneity 行和/或 TweetEval 半合成行。如空间不够，可将 extreme+moderate 合并为单表，用子表头区分。\n\n3. **Algorithm 1 措辞**（Should-Fix）：Step 2 \"Compute corrected labels\" → \"Compute corrected outcome moments\" 或 \"Apply moment correction\"。\n\n4. **K=8 边界**（Should-Fix）：在 §4.3 末尾加一句：\"At K=8 with n_expert=250, EC-HTE maintains nominal coverage but RMSE exceeds global correction (Appendix X), establishing a practical scalability boundary.\"\n\n5. **子组选择讨论**（Should-Fix）：在 §3 或 Limitations 中增加一段讨论子组变量选择的指导原则和潜在陷阱。\n\n6. **A2 适用范围标注**（Minor）：在 Assumption (A2) 后括注 \"(used for diagnostic only; EC-HTE correction does not require symmetric errors)\"。\n\n7. **Figure 2 字号**（Minor）：增大轴标签和 colorbar 刻度字号至正文字号的 80% 以上。\n",
  "project": "ec_hte_llm_annotation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 12 审稿报告：Error-Corrected Heterogeneous Treatment Effects\n\n**目标 Venue**: EMNLP 2026 (ARR May cycle)\n**审稿人**: Reviewer 1, Reviewer 2\n**交叉回应**: Reviewer 1 ↔ Reviewer 2 完成\n**Overall Score**: 3.5 (Borderline Conference)\n\n---\n\n## Summary\n\n本文研究 LLM 标注用于因果推断（HTE 估计）时，全局混淆矩阵校正在子组间引入系统性偏差的问题。主要贡献：(1) 推导精确偏差恒等式（Theorem 1），表明全局校正偏差与 δ_s·Δτ 成正比；(2) 提出 EC-HTE，基于分层贝叶斯估计子组混淆矩阵进行分组校正；(3) 给出无需估计处理效应的诊断准则（Proposition 3）。实验覆盖合成、半合成（TweetEval）及多个鲁棒性验证，展示 EC-HTE 在极端异质性条件下将偏差从 0.059 降至 0.010。\n\n论文技术扎实，理论推导严谨，实验设计全面。主要不足在于：(1) 诊断工具在真实 LLM 混淆矩阵上 AUC 降至 0.63，但摘要仅报告 0.86；(2) 方法论新颖性有限——EC-HTE 本质上是识别问题后的自然修复；(3) 缺乏真实因果数据集验证；(4) 主体正文视觉密度偏低，大量关键结果被推入 Appendix。\n\n---\n\n## Strengths\n\n1. **理论贡献清晰且可验证**：偏差恒等式（Theorem 1）提供了精确的解析形式，R²≥0.974 的经验验证令人信服。这一理论结果本身具有独立价值——即使不采用 EC-HTE，从业者也可据此判断全局校正何时有害。\n\n2. **实验覆盖面极广**：100 次 MC 重复、K∈{2,4,8}、对称/非对称混淆矩阵、6 个 OpenAI 模型 + 开源 LLM、hate speech 案例、子组误指定、A1 敏感性分析、混杂处理、R-learner 兼容性等——超过 20 个 Appendix 章节覆盖了几乎所有可预见的质疑。\n\n3. **方法论位置清晰**：准确定位 EC-HTE 与 PPI/DSL/PPCI 的关系——全局校正等价于 pooled DSL，EC-HTE 添加分层部分池化——避免了过度声称新颖性。\n\n4. **写作质量高**：主体正文在 8 页内呈现了完整的理论-方法-实验叙事，Introduction 的 Figure 1 三面板设计有效传达核心直觉。\n\n5. **实用性**：诊断准则（尽管有局限）和预算指南（Appendix 的 crossover curves）为从业者提供了可操作的工具。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则影响接收）\n\n**[W-MF1] 摘要诊断 AUC 选择性报告** [R1 AGREE, R2 AGREE — 共识]\n摘要称 \"AUC = 0.86\" 但仅限合成对称误差条件；在 16 个真实 LLM 模型-数据集组合上 AUC 降至 0.63（Appendix D.9）。对于 K=2，诊断甚至 anti-predict（§4.4 承认）。摘要应同时报告两个数字，或使用更保守的表述（如 \"AUC up to 0.86 under symmetric errors; 0.63 on real LLM confusion matrices\"）。这是诚实报告的问题，不修复会被审稿人标记为 misleading。\n\n**[W-MF2] 主结果表缺乏代表性** [R1 AGREE, R2 AGREE — 共识]\nTable 1 仅展示 extreme heterogeneity 配置，但 §4.3 承认 \"moderate heterogeneity 下方法趋同\"、\"TweetEval 半合成实验中 EC-HTE RMSE 高于 Global\"。主表应至少包含一个非极端配置（moderate 或 TweetEval），否则读者对方法的适用范围产生过于乐观的印象。当前 Table~\\ref{tab:main_supp} 在 Appendix 中，但这些是读者最需要在主体看到的结果。\n\n### Should-Fix（建议修复，不修复会扣分但不致命）\n\n**[W-SF1] Algorithm 1 描述歧义** [R1 AGREE, R2 AGREE — 共识]\nAlgorithm 1 Step 2 \"corrected labels\" 与 Step 3 的操作存在歧义——EC-HTE 校正的是 moments（期望值）而非逐条标签。建议明确使用 \"corrected outcome moments\" 或等价表述，避免与逐条标签校正方法（如 PPCI）混淆。\n\n**[W-SF2] K=8 可扩展性边界应在主体提及** [R1 AGREE, R2 AGREE — 共识]\nK=8 时 EC-HTE RMSE 超过 Global（Appendix D.16），这是方法的重要边界条件。当前仅在 Limitations 一笔带过。建议在 §4.3 加一句明确提及此边界，或在 Table 1 增加 K=8 行。\n\n**[W-SF3] 子组定义指导缺失** [R1 AGREE, R2 AGREE — 共识]\n论文使用 hashtag presence 和 text length 定义子组，但未讨论从业者如何选择子组变量。当子组定义本身与 LLM 误差模式相关（如按文本长度分组，而 LLM 在短文本上系统性更差），子组选择就不是中性的。需要至少一段讨论。\n\n**[W-SF4] 专家标注成本-收益分析不足** [R1 AGREE, R2 AGREE — 共识]\nEC-HTE 需要按子组分配专家标注（每子组 ≥25），但论文未讨论相比全局方法，额外的子组级标注成本是否值得。预算 crossover curves 在 Appendix 但应在主体简要总结。\n\n**[W-SF5] Theorem 1 \"exact identity\" 措辞** [R1 REBUT → R2 ACCEPT downgrade]\n经交叉讨论，R1 的反驳成立——Theorem 1 推导出的是 finite-sample exact identity（非渐近近似），且与 Firth-Liang 方法的区分是实质性的。但建议在 proof sketch 中更明确说明 \"exact\" 的含义（有限样本精确 vs. 渐近），避免歧义。降级为 should-fix。\n\n**[W-SF6] 缺乏真实因果数据集验证** [R1 AGREE, R2 AGREE — 共识]\n所有 CATE 均为合成注入（即使在 \"semi-synthetic\" 中，文本特征真实但效应人工注入）。论文在 Limitations 中承认这一点，并指出 \"suitable public benchmarks\" 不存在。审稿人理解这是结构性限制，但建议讨论是否可使用 LaLonde/IHDP 等经典因果数据集（即使非 NLP 领域）作为补充验证。\n\n### Minor\n\n**[W-M1] 摘要信息密度过高** [R1 AGREE, R2 AGREE — 共识]\n摘要包含 δ_s·Δτ 公式、R²≥0.97、AUC=0.86、5.9× 改善等密集技术细节，对非因果推断背景的 NLP 读者不够友好。建议简化数学表述，保留核心叙事。\n\n**[W-M2] 方法新颖性有限** [R1 AGREE, R2 AGREE — 共识]\nEC-HTE 的核心操作（分层贝叶斯混淆矩阵估计 + 矩校正）是识别问题后的自然修复步骤。主要贡献在于问题识别（偏差恒等式）而非解决方案本身。论文对此定位准确，但应进一步强调理论贡献的独立价值。\n\n**[W-M3] Figure 2 轴标签字号偏小**\nHeatmap 的轴标签和 colorbar 刻度约为正文字号的 60-65%，打印时可能不够清晰。\n\n**[W-M4] A2 对称假设的影响范围应澄清**\n经交叉讨论确认：A2（对称误分类）仅影响诊断准则（Proposition 3），不影响 EC-HTE 方法本身。建议在 Assumptions 列表中明确标注 A2 的适用范围（\"used only for the diagnostic\"）。\n\n**[W-M5] 主体 display item 密度偏低**\n8 页正文仅含 3 个 display items（Figure 1, Table 1, Figure 2），pages 3-6 为纯文本。建议考虑将 Appendix 中的 budget crossover figure 或 cross-model consistency 关键结果移入主体。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位审稿人达成完全共识：\n\n1. **诊断 AUC 报告问题是最关键的修复项**——摘要的选择性报告构成 misleading risk\n2. **Table 1 的代表性不足**——仅展示 extreme 配置给读者错误印象\n3. **理论贡献 > 方法贡献**——偏差恒等式是核心贡献，EC-HTE 是自然延伸\n4. **实验全面性是论文最大优势**——Appendix 的深度覆盖令人印象深刻\n5. **论文适合 EMNLP**——NLP+因果推断的交叉主题、LLM 标注校正的实用性\n\n## Reviewer Divergence\n\n以下问题经交叉讨论后解决，无残留分歧：\n\n1. **Theorem 1 \"exact identity\" 措辞**：R2 初审认为措辞有误导，R1 反驳 F-L 区分是实质性的。R2 接受降级为 should-fix，建议澄清 \"exact\" 的含义。\n2. **A2 对称假设**：R1 初审认为 A2 限制了方法通用性，R2 指出 EC-HTE 本身不依赖 A2。达成共识：仅诊断受影响，方法不受限。\n3. **SE plug-in 校准**：R1 标记 1.2pp 覆盖率缺口为 should-fix，R2 认为在 MC 误差范围内且提供了 bootstrap 替代方案。达成共识：minor issue。\n\n---\n\n## Questions for Authors\n\n1. 在 K=4 TweetEval 半合成实验中，EC-HTE 的 RMSE (0.225) 显著高于 Global (0.124)。能否提供子组级别的分解，说明 RMSE 增加主要来自哪些子组？是否存在子组级别 EC-HTE 优于 Global 的情况？\n\n2. 诊断准则在 K=2 时 anti-predict 的根本原因是 |δ₀|=|δ₁| 的代数约束。是否有修改诊断公式使其在 K=2 也可靠的理论路径？\n\n3. 分层贝叶斯的 Gamma(3,1) 超先验选择依据是什么？是否进行了先验敏感性分析？\n\n4. 子组变量选择（hashtag presence, text length）是否存在事后选择偏差？如果从业者尝试多个子组定义并选择\"最好\"的结果，如何控制多重比较问题？\n\n---\n\n## Missing References\n\n未发现明显遗漏的关键引用。论文对 PPI、DSL、PPCI 等核心竞争方法的引用完整。建议考虑引用：\n- Zrnic & Candès (2024) 关于 cross-prediction 的后续工作（如已发表）\n- 因果推断中测量误差校正的经典统计文献（如 Carroll et al., Measurement Error in Nonlinear Models）中与混淆矩阵反演直接相关的章节\n\n---\n\n## External Review\n\n未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成\n**结果**: 0 critical / 2 warning / 9 info\n\n**Warnings**:\n1. Pages 3-6 从 Figure 1 (p2) 到 Table 1 (p7) 跨越 5 页纯文本，视觉单调（text desert）。理论推导的 display equations 有一定缓解作用，但对实证+理论混合型论文而言偏长。\n2. 主体 8 页仅含 3 个 display items（Figure 1, Table 1, Figure 2），密度偏低。建议将 1-2 个关键 Appendix 表格/图提入主体。\n\n**Info（正面）**:\n- Figure 1 位置得当（p2），三面板设计清晰\n- Table 1 booktabs 格式规范，精度一致\n- Figure 2 heatmap hatching 区分有效\n- 数学公式渲染正确，无 LaTeX 错误\n- 参考文献格式统一，无未解析引用\n- 无 margin 溢出，符合 ACL 模板规范\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 — Borderline Conference**\n\n**理由**：\n\n论文在理论层面做出了有价值的贡献——偏差恒等式（Theorem 1）揭示了一个此前未被形式化的问题（全局混淆矩阵校正在子组间引入系统偏差），经验验证充分（R²≥0.97）。实验设计全面，鲁棒性验证覆盖面远超同类论文。\n\n阻碍更高评分的主要因素：\n1. **方法新颖性有限**：EC-HTE 是识别问题后的直接修复，贡献主要在问题发现而非解决方案\n2. **诊断工具实用性存疑**：核心卖点之一的诊断准则在真实 LLM 数据上 AUC 仅 0.63，K=2 时 anti-predict\n3. **摘要选择性报告**：AUC=0.86 的报告方式有 misleading risk，需立即修复\n4. **缺乏真实因果验证**：所有效应为合成注入，尽管是结构性限制但削弱了对实际场景有效性的信心\n5. **主表代表性不足**：仅展示 extreme 配置，隐藏了方法在中等异质性下的局限\n\n论文整体质量适合 Findings 接收（3.0），但理论贡献的清晰度和实验的全面性使其有机会进入主会议（borderline）。修复 W-MF1（AUC 报告）和 W-MF2（Table 1 代表性）后，论文竞争力将显著提升。\n\n---\n\n## Detailed Comments\n\n### 给作者的具体修改建议（按优先级排序）\n\n1. **摘要 AUC 报告**（Must-Fix）：将 \"AUC = 0.86\" 改为 \"AUC = 0.86 under synthetic symmetric errors (0.63 on real LLM confusion matrices)\" 或类似表述。\n\n2. **Table 1 扩展**（Must-Fix）：增加 moderate heterogeneity 行和/或 TweetEval 半合成行。如空间不够，可将 extreme+moderate 合并为单表，用子表头区分。\n\n3. **Algorithm 1 措辞**（Should-Fix）：Step 2 \"Compute corrected labels\" → \"Compute corrected outcome moments\" 或 \"Apply moment correction\"。\n\n4. **K=8 边界**（Should-Fix）：在 §4.3 末尾加一句：\"At K=8 with n_expert=250, EC-HTE maintains nominal coverage but RMSE exceeds global correction (Appendix X), establishing a practical scalability boundary.\"\n\n5. **子组选择讨论**（Should-Fix）：在 §3 或 Limitations 中增加一段讨论子组变量选择的指导原则和潜在陷阱。\n\n6. **A2 适用范围标注**（Minor）：在 Assumption (A2) 后括注 \"(used for diagnostic only; EC-HTE correction does not require symmetric errors)\"。\n\n7. **Figure 2 字号**（Minor）：增大轴标签和 colorbar 刻度字号至正文字号的 80% 以上。\n",
    "project": "ec_hte_llm_annotation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-23T06:31:51.751316+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6b114d432b35fe7a1c2143457ae85b08:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Assistant

_source line 926 · 2026-05-23T06:31:59.846378+00:00_

Round 12 审稿报告已投递至 Research Director。

**评分: 3.5 (Borderline Conference)**

关键发现：
- **Must-Fix 2 项**：摘要诊断 AUC 选择性报告（0.86 vs 真实 0.63）、主结果表仅展示 extreme 配置
- **Should-Fix 6 项**：Algorithm 1 措辞歧义、K=8 边界未在主体提及、子组定义指导缺失、成本-收益分析不足、Theorem 1 "exact" 措辞待澄清、缺乏真实因果数据集
- **Minor 5 项**：摘要信息密度、方法新颖性有限、Figure 2 字号、A2 适用范围标注、display item 密度

两位 Reviewer 在所有关键问题上达成共识，无残留分歧。视觉审查完成（0 critical / 2 warning / 9 info）。Issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 86

## Round 86

40 recorded events


### User

_source line 927 · 2026-05-23T08:48:31.758480+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: ec_hte_llm_annotation
- 论文路径: projects/ec_hte_llm_annotation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-23T08:48:36.886743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-23T08:48:36.988197+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-23T08:48:45.473670+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 931 · 2026-05-23T08:48:45.624741+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-23T08:48:48.385891+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 933 · 2026-05-23T08:48:48.486714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 934 · 2026-05-23T08:48:53.105991+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-23T08:48:55.822449+00:00_

{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (39 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-027b: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error（准备中）\n- exp-027: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage（准备中）\n\n## 近期结论\n- **exp-036** (success): Bootstrap SE (B=200, re-estimating CM + re-fitting CF per bootstrap) can close the CausalForest under-coverage gap (91% vs nominal 95%) by properly accounting for CM estimation uncertainty that plug-in SE ignores.\n- **exp-037** (success): Temperature scaling reduces per-subgroup misclassification rates but does NOT eliminate heterogeneity (Δπ shrinks from 0.20 to 0.07 but remains nonzero), so EC-HTE is still necessary post-calibration. Calibrated+EC-HTE should achieve the best coverage.\n- **exp-035** (success): EC-HTE with asymmetric CM estimation (full 2x2 FPR/FNR) maintains coverage >=93% under realistic 7:1 FPR/FNR ratios (simulating GPT-4.1 on Civil Comments), and outp
…[truncated 309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2716
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-23T08:48:55.874022+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex 2>/dev/null && echo \"MAIN_TEX_EXISTS\" || echo \"MAIN_TEX_MISSING\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
  "description": "Check paper file existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex 2>/dev/null && echo \"MAIN_TEX_EXISTS\" || echo \"MAIN_TEX_MISSING\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
    "description": "Check paper file existence"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-23T08:48:56.779158+00:00_

-rw-r--r-- 1 ubuntu ubuntu 941 May 22 02:56 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
MAIN_TEX_EXISTS
-rw-r--r-- 1 ubuntu ubuntu 761742 May 23 08:44 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-23T08:48:57.080793+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-23T08:49:04.310068+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"

Links: [{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found detailed information about ACL Rolling Review (ARR) 2026 submission guidelines and author instructions. Here are the key points:

## Paper Format and Templates
Paper submissions must use the official ACL style templates, which are available as an Overleaf template and can be downloaded via https://aclrollingreview.org/cfp under 'Paper Submission Process, Criteria and Templates'. All submissions must be in PDF format.

## Anonymity Policy
Submissions will remain anonymous during peer review, but authors are free to post and discuss non-anonymo
…[truncated 963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 7229
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-23T08:49:08.882677+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR cycle"
  }
}
```

</details>

---


### Tool call

_source line 941 · 2026-05-23T08:49:09.585580+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 paper format page limit long short paper requirements",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 paper format page limit long short paper requirements",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 942 · 2026-05-23T08:49:15.156607+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here are the key details about EMNLP 2026 call for papers and the ARR cycle submission deadline:

## Submission Deadline

The ARR submission deadline is May 25, 2026.


…[truncated 962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 6273
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-23T08:49:18.670616+00:00_

Web search results for query: "ACL Rolling Review 2026 paper format page limit long short paper requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here is the information about ACL Rolling Review 2026 paper format and requirements:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

More specifically, short papers have a 4 content pages maximum, and long papers have an 8 content pages maximum.

## Sections Not Counting Toward Page Limit

Sections on ethical considerations and limitations do not count towards page limit. Additionally, discussions about ethical impact do not count towards the page limit, as long as they are placed at the end of the paper.

## Formatting Requirements

ACLPUB formatting guidelines
…[truncated 617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 9085
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-23T08:49:29.110412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-23T08:49:29.462009+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{enumitem}
16	\usepackage{algorithm}
17	\usepackage{algpseudocode}
18	
19	\newtheorem{theorem}{Theorem}
20	\newtheorem{corollary}[theorem]{Corollary}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{remark}[theorem]{Remark}
23	
24	\title{Error-Corrected Heterogeneous Treatment Effects:\\When LLM Annotation Debiasing Hurts}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{theory}
38	
39	\input{method}
40	
41	\input{experiments}
42	
43	\input{conclusion}
44	
45	\input{limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{appendix}
51	
52	%\input{checklist}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-23T08:49:29.763525+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-23T08:49:30.066224+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/paper_framing.md\", \"content\": \"# Paper Framing — ec_hte_llm_annotation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (via ARR)\\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\\n- Format: Long paper, 8 pages + unlimited references\\n\\n## Core Claims (3 条，可证伪)\\n\\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \\\"debiasing\\\" can worsen CATE bias by 2-3x (median across configurations), with amplification up to 5.9x for K=4 subgroups; when naive bias is near zero, global correction creates bias where none existed. For the difference-in-means estimator, the amplification magnitude does NOT monotonically increase with K (K=2 extreme: up to 2.86× vs K=4 extreme: up to 2.41×); however, with nonlinear estimators such as CausalForest, more subgroups amplify the effect substantially (K=4/extreme: up to 5.9×) due to compounding estimation noise in tree-based CATE. Global correction increases subgroup-level bias in ~50% of the parameter space.\\n\\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias when misclassification heterogeneity is sufficiently high, while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction by borrowing strength across groups (classic James-Stein shrinkage). We provide precise crossover thresholds: EC-HTE outperforms global correction in RMSE with as few as 250 expert labels (K=2, high heterogeneity), scaling to ~1000 for K=4. **Boundary condition**: when expert labels per subgroup < ~25, shrinkage can be 
…[truncated 10553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-23T08:49:36.192450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-23T08:49:37.249748+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf (743.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-23T08:49:37.466988+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-23T08:49:37.567894+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-23T08:49:43.140068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf",
  "pages": "11-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf",
    "pages": "11-20"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-23T08:49:43.744131+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf (743.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-23T08:49:52.295063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf",
  "pages": "21-30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf",
    "pages": "21-30"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-23T08:49:52.848828+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf (743.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-23T08:50:19.539367+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-23T08:50:19.640216+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-23T08:50:27.328261+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
  "description": "Check existing review issues and reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
    "description": "Check existing review issues and reports"
  }
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-23T08:50:27.378997+00:00_

-rw-r--r-- 1 ubuntu ubuntu 38306 May 23 06:47 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml
EXISTS
total 164
drwxr-xr-x  2 ubuntu ubuntu  4096 May 23 06:31 .
drwxr-xr-x 35 ubuntu ubuntu  4096 May 23 08:48 ..
-rw-r--r--  1 ubuntu ubuntu  9505 May 21 04:29 round_0.md
-rw-r--r--  1 ubuntu ubuntu 11733 May 21 11:46 round_1.md
-rw-r--r--  1 ubuntu ubuntu 13189 May 21 15:03 round_2.md
-rw-r--r--  1 ubuntu ubuntu 14716 May 22 06:16 round_3.md
-rw-r--r--  1 ubuntu ubuntu 16916 May 22 09:35 round_4.md
-rw-r--r--  1 ubuntu ubuntu 13210 May 22 10:42 round_5.md
-rw-r--r--  1 ubuntu ubuntu 15510 May 22 11:53 round_6.md
-rw-r--r--  1 ubuntu ubuntu 15970 May 22 13:51 round_7.md
-rw-r--r--  1 ubuntu ubuntu 14677 May 22 15:49 round_8.md
-rw-r--r--  1 ubuntu ubuntu 12642 May 23 06:31 round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-23T08:51:00.117838+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-23T08:51:27.180854+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 27063
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-23T08:51:27.333007+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责**方法严谨性 + 实验设计**方向的审稿。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper，正文 8 页，参考文献不限页数，Limitations 和 Ethical Considerations 不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX 入口: `projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf`\n\n## 论文概要\n标题: \"Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\"\n\n本文研究 LLM 标注作为 effect modifier 时，subgroup 级别的 misclassification heterogeneity 对 CATE 估计的影响。核心贡献：(1) 精确 bias identity（Theorem 1）：global correction 引入的 bias 正比于 δ_s · Δτ；(2) EC-HTE 框架：hierarchical Bayesian subgroup-stratified confusion matrix correction；(3) Δτ-free diagnostic（Proposition 3）；(4) 与 PPCI 的组合用于 joint covariate/outcome error。\n\n## 你的审查重点\n\n请严格聚焦以下方面，逐条给出评价：\n\n1. **理论推导的严谨性**\n   - Theorem 1（Bias Decomposition Identity）的 5 个假设（A1-A5）是否合理？哪些假设在实际中最容易违反？\n   - Proposition 3（Debiasing Can Increase Bias）的条件是否充分？\n   - 多类扩展（Corollary 4）的推广是否自然？\n   - 证明是否完整、无漏洞？\n\n2. **EC-HTE 方法设计**\n   - Hierarchical Bayes (Dirichlet-Multinomial) 的先验选择是否合理？α₀ 的 empirical Bayes 估计是否引入偏差？\n   - Singularity guard（κ > 100 fallback）的阈值选择依据是否充分？\n   - Variance-adjusted CausalForest（Eq. 5）的 plug-in SE 近似是否低估不确定性？论文自己承认了这一点，修复方案（bootstrap SE）的计算成本是否可接受？\n   - PPCI 组合的正交性论证是否令人信服？\n\n3. **实验设计与统计有效性**\n   - 520 configurations 的参数网格设计是否覆盖了关键场景？有无明显遗漏？\n   - 100 MC runs 是否足够？MC SE 的报告是否充分？\n   - Semi-synthetic DGP（TweetEval 基础）的 CATE injection 是否合理？这是否削弱了对真实场景的推广？\n   - 真实数据 case study（Hate Speech, Appendix M）只报告了 pattern consistency 而非 ground-truth benchmark，这一局限是否被充分讨论？\n   - 统计显著性检验（Table 13）的检验方式是否恰当？\n\n4. **可复现性**\n   - 关键超参（MCMC chains=4, iterations=4000, warmup=2000）是否报告充分？\n   - CausalForestDML 的超参是否固定且合理？\n   - 代码和数据的可获取性声明是否充分？\n\n请以标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。\nWeaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责**方法严谨性 + 实验设计**方向的审稿。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper，正文 8 页，参考文献不限页数，Limitations 和 Ethical Considerations 不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX 入口: `projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf`\n\n## 论文概要\n标题: \"Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\"\n\n本文研究 LLM 标注作为 effect modifier 时，subgroup 级别的 misclassification heterogeneity 对 CATE 估计的影响。核心贡献：(1) 精确 bias identity（Theorem 1）：global correction 引入的 bias 正比于 δ_s · Δτ；(2) EC-HTE 框架：hierarchical Bayesian subgroup-stratified confusion matrix correction；(3) Δτ-free diagnostic（Proposition 3）；(4) 与 PPCI 的组合用于 joint covariate/outcome error。\n\n## 你的审查重点\n\n请严格聚焦以下方面，逐条给出评价：\n\n1. **理论推导的严谨性**\n   - Theorem 1（Bias Decomposition Identity）的 5 个假设（A1-A5）是否合理？哪些假设在实际中最容易违反？\n   - Proposition 3（Debiasing Can Increase Bias）的条件是否充分？\n   - 多类扩展（Corollary 4）的推广是否自然？\n   - 证明是否完整、无漏洞？\n\n2. **EC-HTE 方法设计**\n   - Hierarchical Bayes (Dirichlet-Multinomial) 的先验选择是否合理？α₀ 的 empirical Bayes 估计是否引入偏差？\n   - Singularity guard（κ > 100 fallback）的阈值选择依据是否充分？\n   - Variance-adjusted CausalForest（Eq. 5）的 plug-in SE 近似是否低估不确定性？论文自己承认了这一点，修复方案（bootstrap SE）的计算成本是否可接受？\n   - PPCI 组合的正交性论证是否令人信服？\n\n3. **实验设计与统计有效性**\n   - 520 configurations 的参数网格设计是否覆盖了关键场景？有无明显遗漏？\n   - 100 MC runs 是否足够？MC SE 的报告是否充分？\n   - Semi-synthetic DGP（TweetEval 基础）的 CATE injection 是否合理？这是否削弱了对真实场景的推广？\n   - 真实数据 case study（Hate Speech, Appendix M）只报告了 pattern consistency 而非 ground-truth benchmark，这一局限是否被充分讨论？\n   - 统计显著性检验（Table 13）的检验方式是否恰当？\n\n4. **可复现性**\n   - 关键超参（MCMC chains=4, iterations=4000, warmup=2000）是否报告充分？\n   - CausalForestDML 的超参是否固定且合理？\n   - 代码和数据的可获取性声明是否充分？\n\n请以标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。\nWeaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。"
  }
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-23T08:51:56.537238+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29204
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-23T08:51:56.688393+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责**新颖性 + 完整性 + 写作质量**方向的审稿。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper，正文 8 页，参考文献不限页数，Limitations 和 Ethical Considerations 不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **Overall Assessment 评分标准**: 5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 论文文件\n- LaTeX 入口: `projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf`\n\n## 论文概要\n标题: \"Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\"\n\n本文研究 LLM 标注作为 effect modifier 用于 HTE 分析时，subgroup-heterogeneous misclassification 引入的 bias。核心贡献：(1) Bias Decomposition Identity（精确恒等式，非 bound）；(2) EC-HTE（hierarchical Bayesian subgroup-stratified correction）；(3) Δτ-free diagnostic；(4) EC-HTE+PPCI 组合处理 covariate+outcome 双重误差。\n\n实验跨 520 synthetic configurations、semi-synthetic TweetEval、real-data Hate Speech case study、8 LLMs（6 proprietary + 4 open-source）、11 model-dataset combinations 验证 bias identity。\n\n## 你的审查重点\n\n请严格聚焦以下方面，逐条给出评价：\n\n1. **新颖性与贡献评估**\n   - 本文定位为 \"problem discovery + formal characterization\"，而非 \"new estimation technique\"。这种贡献模式对 EMNLP 是否足够？\n   - 与 classical measurement error 文献（Fuller 1987, Carroll et al. 2006）的区分是否清晰？论文是否充分 credit 了经典文献中已有的 insight（misspecified correction amplifies MSE）？\n   - 与最近的竞争者（Mozer 2026, PPCI/Sui & Candès 2026, Audinet de Pieuchon et al. 2025）的区分是否令人信服？\n   - δ_s · Δτ product form 的 exact identity 相比 asymptotic bound 的优势是否被过度声称？\n   - HB partial pooling 作为方法贡献，本质是 James-Stein shrinkage 的直接应用——方法新颖性是否足够？\n\n2. **相关工作覆盖**\n   - 是否有重要的遗漏文献？特别检查以下方向：\n     - Causal inference with mismeasured covariates（beyond Carroll, Imai & Yamamoto）\n     - LLM-as-annotator quality/bias 文献\n     - Bayesian measurement error models\n     - HTE estimation under covariate error\n   - 37 篇参考文献对一篇 EMNLP long paper 是否足够？\n   - 引用年份分布是否合理？是否遗漏了 2025-2026 的重要新工作？\n\n3. **写作质量**\n   - Abstract 是否过长或信息过载？\n   - Introduction 的叙事逻辑是否流畅？Problem → Gap → Solution → Results 的结构是否清晰？\n   - 正文 vs 附录的材料分配是否合理？是否有应在正文但被放到附录的关键内容？\n   - 符号系统是否一致？（检查 π_s, δ_s, Δπ, Δτ 等的定义和使用）\n   - Figure 1 和 Figure 2 是否有效传达了核心信息？\n   - 论文标题的 \"When LLM Annotation Debiasing Hurts\" 是否过于 provocative/clickbait？\n\n4. **格式合规性**（EMNLP 2026 / ARR 要求）\n   - 正文是否严格控制在 8 页以内？\n   - Limitations section 是否存在且内容充分（~3 个要点）？\n   - 匿名性是否完整？（检查自引、脚注、代码链接、致谢）\n   - [review] 选项是否正确启用？\n   - 参考文献格式是否符合 ACL style？\n\n5. **Limitations 评估**\n   - 论文自述的 limitations 是否诚实且完整？\n   - 是否有未提及的重要局限？\n\n请以标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。\nWeaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。\n最后给出 Overall Assessment 评分（使用 EMNLP 2026 ARR 评分标准）和 Confidence 评分（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责**新颖性 + 完整性 + 写作质量**方向的审稿。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper，正文 8 页，参考文献不限页数，Limitations 和 Ethical Considerations 不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **Overall Assessment 评分标准**: 5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 论文文件\n- LaTeX 入口: `projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_10/submitted.pdf`\n\n## 论文概要\n标题: \"Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\"\n\n本文研究 LLM 标注作为 effect modifier 用于 HTE 分析时，subgroup-heterogeneous misclassification 引入的 bias。核心贡献：(1) Bias Decomposition Identity（精确恒等式，非 bound）；(2) EC-HTE（hierarchical Bayesian subgroup-stratified correction）；(3) Δτ-free diagnostic；(4) EC-HTE+PPCI 组合处理 covariate+outcome 双重误差。\n\n实验跨 520 synthetic configurations、semi-synthetic TweetEval、real-data Hate Speech case study、8 LLMs（6 proprietary + 4 open-source）、11 model-dataset combinations 验证 bias identity。\n\n## 你的审查重点\n\n请严格聚焦以下方面，逐条给出评价：\n\n1. **新颖性与贡献评估**\n   - 本文定位为 \"problem discovery + formal characterization\"，而非 \"new estimation technique\"。这种贡献模式对 EMNLP 是否足够？\n   - 与 classical measurement error 文献（Fuller 1987, Carroll et al. 2006）的区分是否清晰？论文是否充分 credit 了经典文献中已有的 insight（misspecified correction amplifies MSE）？\n   - 与最近的竞争者（Mozer 2026, PPCI/Sui & Candès 2026, Audinet de Pieuchon et al. 2025）的区分是否令人信服？\n   - δ_s · Δτ product form 的 exact identity 相比 asymptotic bound 的优势是否被过度声称？\n   - HB partial pooling 作为方法贡献，本质是 James-Stein shrinkage 的直接应用——方法新颖性是否足够？\n\n2. **相关工作覆盖**\n   - 是否有重要的遗漏文献？特别检查以下方向：\n     - Causal inference with mismeasured covariates（beyond Carroll, Imai & Yamamoto）\n     - LLM-as-annotator quality/bias 文献\n     - Bayesian measurement error models\n     - HTE estimation under covariate error\n   - 37 篇参考文献对一篇 EMNLP long paper 是否足够？\n   - 引用年份分布是否合理？是否遗漏了 2025-2026 的重要新工作？\n\n3. **写作质量**\n   - Abstract 是否过长或信息过载？\n   - Introduction 的叙事逻辑是否流畅？Problem → Gap → Solution → Results 的结构是否清晰？\n   - 正文 vs 附录的材料分配是否合理？是否有应在正文但被放到附录的关键内容？\n   - 符号系统是否一致？（检查 π_s, δ_s, Δπ, Δτ 等的定义和使用）\n   - Figure 1 和 Figure 2 是否有效传达了核心信息？\n   - 论文标题的 \"When LLM Annotation Debiasing Hurts\" 是否过于 provocative/clickbait？\n\n4. **格式合规性**（EMNLP 2026 / ARR 要求）\n   - 正文是否严格控制在 8 页以内？\n   - Limitations section 是否存在且内容充分（~3 个要点）？\n   - 匿名性是否完整？（检查自引、脚注、代码链接、致谢）\n   - [review] 选项是否正确启用？\n   - 参考文献格式是否符合 ACL style？\n\n5. **Limitations 评估**\n   - 论文自述的 limitations 是否诚实且完整？\n   - 是否有未提及的重要局限？\n\n请以标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。\nWeaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。\n最后给出 Overall Assessment 评分（使用 EMNLP 2026 ARR 评分标准）和 Confidence 评分（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-23T08:51:58.104990+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1416
}
```

</details>

---


### Assistant

_source line 966 · 2026-05-23T08:52:11.380828+00:00_

已完成初始化：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已派发（fire-and-forget） |
| Reviewer 1（方法严谨性 + 实验设计） | ✅ 已分配 Round 1 |
| Reviewer 2（新颖性 + 完整性 + 写作） | ✅ 已分配 Round 1 |
| 外部审稿 | ⏭️ 未配置，跳过 |

等待两位 Reviewer 返回独立初审报告，收齐后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 87

## Round 87

2 recorded events


### User

_source line 967 · 2026-05-23T08:59:31.345104+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 理论推导严谨且有独立价值，实验设计全面（520 configurations），但 plug-in SE 低估不确定性的问题未解决，且缺乏真实数据 CATE 基准验证，限制了方法的实际可信度。

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | Theorem 1 证明完整正确（Appendix B 矩阵代数可验证），R²>0.97 的经验验证有力；但 plug-in SE 在 n_expert<100 时低估不确定性（论文自承，Section 4.3），使 CI coverage 在小样本下不可靠 |
| Excitement | 3.5 / 5 | "global correction can hurt" 洞察非显然且有实践意义；Δτ-free diagnostic (Proposition 3) 独立可用；但问题设定较窄（需同时满足：LLM 标注为 effect modifier + subgroup 间 misclassification heterogeneity），受众范围受限 |
| Reproducibility | 4 / 5 | MCMC 超参（4 chains, 4000 iter, 2000 warmup）、CausalForestDML 配置（Appendix E）均已报告；收敛诊断充分（Table 2, R̂<1.003, ESS>1618）；代码承诺 acceptance 后释放，但目前不可复现 |
| Confidence | 4 / 5 | 我熟悉因果推断中的测量误差校正文献和 confusion matrix 方法，仔细阅读了全部正文和 21 个附录 |

## Paper Summary

本文研究 LLM 标注作为 effect modifier 时，subgroup 级别 misclassification heterogeneity 对 CATE 估计的影响。核心贡献包括：(1) 精确 bias identity (Theorem 1)，证明 global confusion matrix correction 引入的 bias 正比于 δ_s·Δτ/(1−2π̄)；(2) EC-HTE 框架，通过 hierarchical Bayesian subgroup-stratified confusion matrix estimation 进行纠偏；(3) Δτ-free diagnostic (Proposition 3)，可在不知 treatment effect 的情况下判断 global correction 是否有害；(4) 与 PPCI 的组合用于 joint covariate/outcome error correction。实验在 520 个 synthetic/semi-synthetic 配置和 11 个真实 LLM confusion matrix 上验证。

## 主要优势

**S1. 理论贡献干净且有独立价值。** Theorem 1 给出了 bias 的 exact identity（而非 bound），bias = δ_s·Δτ·amplification 的乘积结构直观地揭示了两个来源（misclassification heterogeneity × treatment effect heterogeneity）的交互作用。证明（Appendix B）通过 M_global^{-1}·M_s − I 的矩阵代数推导，逻辑链完整，我逐步验证了 2×2 对称情形下的计算，结果一致。R² > 0.994 (K=2) 和 R² > 0.975 (K=4) 的经验验证（Section 5.2，覆盖 synthetic grids + 11 个真实 LLM confusion matrices）为 identity 的准确性提供了强支撑。

**S2. 实验设计系统且全面。** 520 configurations 参数网格覆盖了 K∈{2,4}、Δτ∈[0,0.5]、Δπ∈[0,0.25] 的关键区间；100 MC runs 配合 MC SE 报告（Table 13，RMSE variance < 3.2%），统计效力充分。Semi-synthetic DGP 基于真实 TweetEval 文本特征定义 subgroup，避免了纯合成数据的 ecological validity 问题。Multi-LLM 验证（Appendix N-O，6 个 OpenAI 模型 + 4 个开源 LLM）确认 heterogeneity 现象跨模型一致（Spearman ρ ≥ 0.82）。

**S3. Diagnostic 工具的实践价值。** Proposition 3 的 Δτ-free diagnostic 只需 per-subgroup misclassification rates 即可判断 global correction 是否有害，AUC = 0.86 at subgroup level（Section 5.4），独立于 EC-HTE 可使用。这为实践者提供了低成本的 screening tool。

**S4. 全面的 robustness 检验。** 附录覆盖了 Assumption A1 违反（Appendix Z.2，outcome-dependent misclassification）、A5 放松（Corollary 4/5，subgroup-specific Δτ）、class imbalance（Appendix T）、asymmetric confusion matrices（Appendix J, Z.5）、multiplicative treatment effects（Appendix R）、confounded treatment（Appendix Z.3）、K=8 subgroups（Appendix L）等关键场景。覆盖面在同类论文中属于上乘。

**S5. 写作结构清晰。** 正文 8 页严格控制在理论核心 + 关键实验，21 个附录按需展开，层次分明。Algorithm 1（page 29）可直接实现。

## Must-Fix 问题（影响接收决定）

**N1** [critical] Plug-in SE 低估不确定性，且 bootstrap 修复仅停留在提议层面
- 具体位置：Section 4.3, Eq. 5, Appendix Y (page 25)
- 问题：Variance-adjusted CausalForest 的 SE 公式 se_adj,i = √(diag(Ĉ_s^{-1}·diag(se_i²)·Ĉ_s^{-T})) 是纯 plug-in 近似——仅传播 CausalForest 原始 SE，**不传播 Ĉ_s 的估计不确定性**。论文自承（Section 4.3）："the standard errors may understate total uncertainty"。Appendix Y 显示 n_expert ≥ 100 时 coverage 93.8%（接近 oracle 94-96%），但 n_expert < 100 时 coverage 下降。问题在于：**EC-HTE 的 HB shrinkage 优势恰恰在 n_expert 较小时最显著**（Table 3, Section I），但在同一 regime 下 CI 不可靠——方法的核心卖点与其已知缺陷在同一参数区间内矛盾。
- 论文提到 bootstrap SE 可修复但未实现。Appendix Y 的 full bootstrap 实验（"re-estimating both the confusion matrix and CausalForest per bootstrap replicate, E=100"）仅验证 n_expert=200 的情况，coverage 从 93.8% 升至 95.0%。但关键的 n_expert<100 区间（HB 优势最大处）没有 bootstrap coverage 数据。
- 为什么影响接收：如果 CI 在方法优势最大的 regime 内不可靠，实践者无法信赖 EC-HTE 在低 expert budget 下的推断结果。这直接削弱了论文的实用性声称。
- 建议修改方向：(a) 至少在 n_expert ∈ {25, 50, 75} 下提供 bootstrap coverage 数据；(b) 在正文明确标注 plug-in SE 的 valid regime（而非仅在 Limitations 中一笔带过）；(c) 如果 bootstrap 在小 n 下也不能恢复 nominal coverage，需要诚实讨论。

**N2** [critical] 缺乏真实数据 CATE 基准验证
- 具体位置：Section 5.3 (semi-synthetic results), Appendix M (hate speech case study)
- 问题：所有定量评估（bias, RMSE, coverage）均来自 synthetic/semi-synthetic DGP，ground-truth τ(z) 是注入的。唯一的真实数据实验（Appendix M，Hate Speech）仅报告 "pattern consistency"（misclassification rates 跨 subgroup 变化方向与理论预测一致），而非 ground-truth CATE 比较。论文承认 "We leave full real-data validation... to future work"（page 9）。
- Semi-synthetic DGP 的 CATE 注入采用简单的加性/线性形式 τ(z) = r + Δτ·(z−0.5)（Appendix E），虽然 Appendix R 补充了 multiplicative 形式，但两者都是参数化的。真实 treatment effect heterogeneity 可能有更复杂的非参数结构。
- 为什么影响接收：对于一个声称具有实践价值的方法论文章，完全依赖合成数据进行性能评估在 reviewers 中通常被视为显著弱点。虽然同时具备 ground-truth CATE + LLM 标注 + subgroup misclassification heterogeneity 的公开数据集确实稀缺，但论文应更充分地论证为什么 semi-synthetic 结果可以推广到真实场景。
- 建议修改方向：(a) 在 hate speech case study 中，利用 expert labels 构建 held-out CATE estimates 作为 pseudo ground-truth（即使只是 point estimates 的方向性比较）；(b) 增加对 semi-synthetic DGP 与真实数据差异的系统讨论（如：real misclassification 是否真的满足 conditional independence A1？real subgroup structure 是否如此清晰？）。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Assumption A3（balanced classes）的限制性在正文中弱化呈现
- 具体位置：Section 3, Assumption A3 (page 4); Appendix T (page 22)
- 问题：A3 要求 P(Z=1) = P(Z=0) = 0.5，这在真实 NLP 任务中很少成立（如 hate speech 通常 <10%）。Theorem 1 的 exact form 在 A3 下成立。Appendix T 测试了 P(Z=1) ∈ {0.1, 0.2, 0.3, 0.4, 0.5}，Table 18 显示 EC-HTE coverage ≥ 0.94，bias identity R² ≥ 0.976，这很好。但正文中 A3 的讨论仅一句 "we discuss relaxation below"，读者需翻到 Appendix T 才能了解实际影响。对于实践者来说，A3 是最可能违反的假设。
- 建议：在正文 Section 3 或 Remark 中增加 2-3 句，明确说明 A3 违反时 bias identity 的变化形式和 EC-HTE 的经验鲁棒性。

**W2** [warning] Subgroup 定义依赖用户先验，缺乏选择指导
- 具体位置：Section 5.1, Appendix E (DGP 设计)
- 问题：EC-HTE 要求用户预定义 subgroup mapping S: X → {1,...,K}。论文中 subgroups 基于可观测文本特征（hashtag presence, text length）。但如果真实 misclassification heterogeneity 沿着未观测到的维度存在（如语义复杂度、隐含讽刺），预定义的 subgroups 可能无法捕获相关异质性。论文未讨论 subgroup misspecification 的后果，也未提供 data-driven subgroup discovery 的指导。
- Appendix P (page 20) 的 robustness to subgroup misspecification 实验在随机 subgroup assignment 下测试——这是极端情况，但未测试 "部分正确" 的 subgroup（如：真实 heterogeneity 沿 3 个维度存在，但用户只用了 1 个）。
- 建议：(a) 增加 "partially correct subgroup" 的 robustness 实验；(b) 在 Discussion 中建议实践者如何选择 subgroups（如先做 exploratory analysis 检查不同特征下的 error rate 差异）。

**W3** [warning] PPCI 组合的 "正交性" 论证不充分
- 具体位置：Section 4.3 (最后一段), Appendix K (page 17)
- 问题：论文声称 EC-HTE（纠正 Z 空间的 misclassification）与 PPCI（纠正 Y 空间的 prediction error）"正交"，但这只是一个直觉论证（"distinct error sources"），而非严格的理论证明。Appendix K 的 4-DGP 设计通过 construction 分离了两种误差源——但在真实场景中，Z 的 misclassification 可能通过 CATE 函数影响 Y 的估计误差，使两种纠正不完全独立。
- Table 8 显示 EC-HTE+PPCI 在 "both errors" DGP 下 bias 降至 0.007，RMSE 降至 0.009——但这可能是因为实验 DGP 的分离设计而非方法本身的正交性。
- 建议：(a) 讨论在什么条件下正交性可能失效（如 confounding between Z error and Y error）；(b) 将 "orthogonality" 改为更谨慎的 "complementarity"。

**W4** [warning] κ > 100 singularity guard 阈值选择缺乏充分论证
- 具体位置：Section 4.1, Algorithm 1 (line 10), Appendix A.1 (page 11-12)
- 问题：fallback 阈值 κ > 100 被描述为 "corresponds to π_s > 0.495"，但：(a) 为什么 0.495 是正确的切割点？(b) 对不同 κ 值的敏感性分析仅出现在 Appendix A.1（condition numbers 远低于 100），没有测试 κ 在 {10, 50, 100, 200} 之间的性能差异。如果在极端情况下某些 subgroup 的 κ 接近 100（如 high error + small sample），阈值的选择会直接影响估计结果。
- 建议：提供 κ 阈值的敏感性实验，至少在 {50, 100, 200} 间比较 RMSE 和 coverage。

## 小问题（不影响接收）

- **M1**: Equation (2) 中的 amplification factor δ_s/(1−2π̄) 在正文中未明确标注变量范围（当 π̄ 接近 0.5 时 amplification 趋于无穷）。建议加注 A4 保证 denominator 非零。
- **M2**: Table 1 (page 7) 的 "Bias" 列标题未说明是 |bias| 还是 signed bias。从数值看应为 |bias|，建议明确标注。
- **M3**: Figure 2 (page 8) 的 heatmap 用了对角线阴影标注 "debiasing hurts" 区域，视觉效果好，但 color bar 的数值范围（0 到 >0.5）在两个子图间不一致（右图范围更大），建议统一。
- **M4**: Section 2 (Related Work) 引用密度高但部分引用（如 Feder et al., 2022; Keith et al., 2020）仅一句话带过，建议增加具体比较。
- **M5**: Appendix Z.3 (confounded treatment, page 27) 测试了 propensity β ∈ {0.25, 0.5, 1.0, 2.0}，但 coverage 仅报告了 β=0.5 时的值 95.0%（Table 26 只有 S0 subgroup 数据），建议补充全 β 范围的 coverage breakdown。

## Questions to Authors

**Q1**: Plug-in SE 在 n_expert < 100 时 coverage 降至多少？能否提供具体数字（Appendix Y 未给出这一区间的 coverage）？

**Q2**: 在 hate speech case study (Appendix M) 中，expert labels 是否可以构建一个 pseudo ground-truth CATE 用于定量比较（哪怕只是 subgroup-averaged 的 ATE 对比）？

**Q3**: 如果实践者不确定 subgroup 定义是否正确（即 misclassification heterogeneity 可能沿未预定义的维度存在），论文是否建议一个 discovery procedure？Proposition 3 的 diagnostic 能否反过来用于 subgroup selection？

**Q4**: Corollary 5 (Appendix Z.1) 将 A5 放松到 subgroup-specific Δτ_s。在这种情况下，bias identity 的乘积结构是否仍然成立？如果 Δτ_s 与 δ_s 相关（即 treatment effect heterogeneity 和 misclassification heterogeneity 沿同一维度变化），amplification 效应会更严重还是更轻？

**Q5**: Table 3 (page 15) 的 budget sensitivity 实验固定 K=2，K=4 下的 budget crossover point 是否会显著不同？直觉上 K=4 需要更多 expert labels 才能使 stratification 优于 global correction。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 968 · 2026-05-23T08:59:42.787126+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 88

## Round 88

2 recorded events


### User

_source line 969 · 2026-05-23T08:59:55.576077+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5 (Borderline Conference)。

核心判断：理论贡献（Theorem 1 的 exact bias identity）严谨且有独立价值，实验覆盖全面（520 configurations + multi-LLM 验证），但两个关键问题影响接收决定：

1. **Plug-in SE 与方法优势的 regime 矛盾**——EC-HTE 的 HB shrinkage 在低 expert budget 时优势最大，但恰好在这个 regime 下 CI coverage 不可靠，且论文未提供小 n 下的 bootstrap coverage 数据
2. **缺乏真实数据 CATE 基准**——所有定量评估依赖 synthetic/semi-synthetic DGP，hate speech case study 仅报告 pattern consistency

此外提出了 4 个 should-fix 问题（A3 balanced classes 限制性弱化呈现、subgroup 选择指导缺失、PPCI 正交性论证不充分、κ 阈值敏感性不足）和 5 个 minor issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 970 · 2026-05-23T09:00:01.882826+00:00_

收到 Reviewer 1 的审稿意见。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 89

## Round 89

6 recorded events


### User

_source line 971 · 2026-05-23T09:00:23.659371+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见 — Round 1 (新颖性 + 完整性 + 写作质量)

**论文**: "Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts"
**Venue**: EMNLP 2026 (ARR May cycle)

---

## Summary

本文研究 LLM 标注作为 effect modifier 用于异质性处理效应 (HTE) 分析时，subgroup-heterogeneous misclassification 引入的 bias 问题。核心贡献包括：(1) Bias Decomposition Identity（Theorem 1），将 correction-induced bias 精确分解为 δ_s · Δτ 的乘积形式；(2) EC-HTE，基于 hierarchical Bayesian 的 subgroup-stratified confusion matrix 校正方法；(3) Δτ-free diagnostic（Proposition 3），无需估计处理效应即可判断 global correction 是否有害；(4) EC-HTE+PPCI 组合处理 covariate+outcome 双重误差。实验覆盖 520 synthetic configurations、semi-synthetic TweetEval、real-data Hate Speech case study、8 LLMs（proprietary + open-source）、11 model-dataset combinations 验证理论预测。

---

## 总体评分

**Overall Assessment**: 3.5 / 5（Borderline Conference）
**一句话总结**: 理论严谨、实验全面地识别了一个重要的实际问题，但方法贡献（hierarchical Bayes partial pooling）本质上是 James-Stein shrinkage 的直接应用，核心理论洞察在经典测量误差文献中有先例，新颖性深度不足以明确支撑主会议接收。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 理论推导严谨（Theorem 1 为精确恒等式，非 bound），R² > 0.97 的验证令人信服；假设讨论充分（A1-A5 逐条分析），sensitivity analysis 覆盖 assumption violation。Appendix B-D 的证明完整。 |
| Excitement | 3 / 5 | 问题重要且实际，但受众较窄（NLP + causal inference 交叉领域）；方法贡献有限，主要价值在问题发现和理论刻画。 |
| Reproducibility | 4 / 5 | 算法伪代码完整（Algorithm 1），DGP 参数详尽（Appendix E），收敛诊断明确（Table 2）；代码承诺 upon acceptance 发布，但当前不可验证。 |
| Confidence | 4 / 5 | 我对测量误差文献和 HTE 估计方法比较熟悉，对本文的理论和实验评估有把握。 |

---

## 主要优势

**S1. 问题识别的实际价值。** 论文揭示了一个非直觉的失败模式：当 LLM 误分类率跨 subgroup 异质时，标准 global confusion-matrix correction 在 50% 的 K=2 配置中恶化 CATE 估计（Section 5.2）。这对正在使用 LLM 标注做社会科学研究的实践者有直接警示意义。Introduction 中 "a researcher who corrects for annotation noise using a pooled confusion matrix may introduce more bias than doing nothing, precisely in the low-error subgroups where original labels were most trustworthy" 的表述准确而有力。

**S2. 精确恒等式的理论贡献。** Theorem 1 给出的 bias = δ_s · Δτ · amplification factor 是一个精确恒等式，不是 asymptotic bound。这比 Frazis & Loewenstein (2003) 的 scalar attenuation β = β(1 − 2π) 更具结构性——它显式分离了 misclassification heterogeneity (δ_s) 和 treatment effect heterogeneity (Δτ) 的交互作用。R² > 0.97 的 empirical validation 跨 520 configurations + 11 real LLM confusion matrices 非常有说服力。

**S3. 实验覆盖面令人印象深刻。** 从 synthetic DGP（520 configurations，参数网格详尽）到 semi-synthetic TweetEval（真实文本特征 + 合成处理效应）再到 real-data Hate Speech case study，再到 8 个 LLM 的 cross-model consistency 验证（Appendix N-O），实验设计层层递进。特别是 Appendix K（PPCI complementarity）、Z（assumption violation robustness）、S（robustness to subgroup misspecification）覆盖了主要 reviewer 可能质疑的方向。

**S4. Δτ-free diagnostic 的实用性。** Proposition 3 提供的诊断条件 |δ_s|/(1−2π_s) > 1 仅依赖 per-subgroup misclassification rates，不需要先估计处理效应，打破了"要诊断需要先知道答案"的循环依赖。AUC = 0.86 在 subgroup level（Figure 3a）的表现足以作为实用筛选工具。

**S5. 完整的实践指南。** Algorithm 1 的伪代码、expert budget crossover curves（Appendix I-J）、diagnostic threshold guidance（Section 5.4）构成了一套可直接使用的 practitioner workflow。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **与经典测量误差文献的区分需要更明确**
- 具体位置：Section 2 (Related Work), Section 3 (第一段)
- 问题："misspecified correction amplifies MSE" 这一核心洞察在经典测量误差文献中已有明确论述。Carroll et al. (2006, Chapter 4) 讨论了 misspecified measurement error model 下 correction 可能增大 variance 甚至 bias 的情况；Fuller (1987, Section 2.3) 分析了 reliability ratio misspecification 的后果。论文在 Section 2 和 Appendix F 中确实提到了三个区分点（effect modifier vs covariate/confounder; exact identity vs bound; correction-induced bias vs measurement-induced bias），但对第一个区分点的论证不够充分——为什么 effect modifier misclassification 在结构上不同于 covariate misclassification？Battistin & Chesher (2014) 已经研究了 treatment effect estimation with covariate measurement error，且 Imai & Yamamoto (2010) 处理了 differential measurement error in causal inference。论文需要更清晰地论证：在什么数学结构上，effect modifier 角色使得本文的 bias identity 不能由已有结果直接推导？
- 为什么影响接收：如果 novelty 主要在于将已知结果应用到新设定，而该设定与已有设定的区别不够本质，则贡献的新颖性会显著降低。
- 建议修改方向：在 Section 2 或 Section 3 开头增加一个明确的 "What is new" 段落，用数学语言展示为什么 effect modifier 角色使得 bias decomposition 的结构与 Frazis & Loewenstein (2003)、Carroll et al. (2006) 的 classical results 不同。不仅要说 "our setting differs" 而要说 "our setting forces a structurally different bias decomposition because..."。

**N2** [critical] **HB partial pooling 方法新颖性不足**
- 具体位置：Section 4.1, Algorithm 1
- 问题：EC-HTE 的核心方法是对 per-subgroup confusion matrices 施加 Dirichlet-Multinomial hierarchical prior，通过 shared concentration parameter α₀ 在 subgroup estimates 之间做 partial pooling。论文自己在 Section 4.1 中明确承认这是 "a James-Stein shrinkage effect"。Dirichlet-Multinomial hierarchical model 是 Bayesian 统计中最基础的模型之一（参见 Gelman et al., Bayesian Data Analysis, Chapter 5），将其应用于 confusion matrices 并不构成方法创新。作为对比，Dawid & Skene (1979) 和 Paun et al. (2018) 在 annotation model 中使用了类似的 hierarchical 结构，但他们的设定更复杂（multiple annotators + latent ground truth）。EC-HTE 本质上是一个更简单的特例（已知 ground truth expert labels 的条件下估计 confusion matrices）。
- 为什么影响接收：如果方法是 "straightforward application of well-known Bayesian machinery to a new setting"，EMNLP reviewer 可能期望看到更多的方法贡献（如：automatically discovering subgroups, handling unknown K, adaptive expert budget allocation）来弥补这一不足。
- 建议修改方向：(a) 更坦诚地定位贡献——不声称方法新颖性，而是强调 "the right tool for the right problem" 的工程价值；(b) 或增加一个 methodological extension（如 subgroup discovery, adaptive allocation），使方法部分有独立贡献。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **相关工作遗漏若干重要文献**
- 具体位置：Section 2 (Related Work), Appendix F
- 问题：
  (a) **LLM annotation variance/reliability 文献**：近期有重要工作直接讨论 LLM 标注的 variance 来源和 measurement error 性质，如 "Variance-Aware LLM Annotation for Strategy Research" (Mellon et al., 2025, arXiv:2601.02370) 识别了 5 类 variance sources；"To Err Is Human; To Annotate, SILICON?" (Bauer et al., 2024, arXiv:2412.14461) 直接研究如何减少 LLM annotation 的 measurement error。这些工作与本文的动机高度相关但未被引用。
  (b) **HTE with mismeasured treatment**：Calvi et al. (2015, arXiv:1511.04162) "Heterogeneous Treatment Effects with Mismeasured Endogenous Treatment" 研究了 mismeasured treatment 下的 HTE 估计，与本文的 effect modifier misclassification 设定有直接关联。
  (c) **Bayesian measurement error models 的更广泛文献**：Richardson & Gilks (1993), Gustafson (2003) 虽被引用但讨论不够充分——特别是 Gustafson (2003, Chapter 6) 关于 identifiability in Bayesian measurement error models 的讨论与 EC-HTE 的 identifiability 条件直接相关。
- 建议：扩充 Section 2 的 "Measurement error details" 和 "Annotation model extensions" 部分，增加上述引用并明确定位区分。

**W2** [warning] **Abstract 信息密度过高**
- 具体位置：Abstract（第1页）
- 问题：Abstract 在约 250 词内塞入了大量具体数字（R² > 0.97, 520 configurations, 50% of K=2 configurations, up to 5×, Δ=0.09, 0.008, GPT-4.1 pilot, 88.8%, 10.2%–20.0%, Δτ = 0.098 等）。虽然这些数字有信息量，但首次阅读时信息过载导致核心 message 被淹没。读者需要在 abstract 中快速抓住 "the problem is X, the solution is Y, the result is Z" 的主线，而不是在第一遍就消化所有实验细节。
- 建议：精简数字到 3-4 个最关键的（如 R² > 0.97 验证 identity, 50% configurations worsened by correction, AUC 0.86 for diagnostic），其余移至 Introduction 或 Experiments。

**W3** [warning] **δ_s · Δτ product form 的 "exact identity" vs "asymptotic bound" 优势被过度强调**
- 具体位置：Section 1 (贡献列表), Section 3 (Theorem 1 后的讨论)
- 问题：论文多次强调 "an exact bias identity showing...a finite-population identity, not a bound"（Abstract, Section 1, Section 3）。但实际上这一精确性的实际优势有限：(a) 在应用中，confusion matrices 本身需要从有限样本估计（Section 4.1），引入 estimation uncertainty，使得 identity 的精确性在 downstream inference 中被噪声覆盖；(b) Frazis & Loewenstein (2003) 的 scalar attenuation result 同样是 exact（不是 bound），只是形式不同。论文的真正优势不是 "exact vs bound" 而是 "structured decomposition revealing the δ_s × Δτ interaction"，建议调整措辞重心。
- 建议：将强调点从 "exact identity (not a bound)" 转移到 "structured decomposition that isolates the interaction between misclassification heterogeneity and treatment effect heterogeneity"，这是更有实质意义的贡献。

**W4** [warning] **Pre-defined subgroup 假设限制实际适用性**
- 具体位置：Limitations section, Section 3 (Assumption A5)
- 问题：EC-HTE 要求 subgroup 是预先定义的（text features → subgroup assignment S: X → {1,...,K}），而在实际 NLP 应用中，subgroup 往往是数据驱动发现的。论文在 Limitations 中提到 "continuous effect modifiers or latent subgroup discovery...future work"，但这一限制可能比论文暗示的更严重——如果 practitioner 不知道哪些特征定义了相关 subgroup，EC-HTE 的整个框架无法启动。与 Causal Forest 等自动发现 heterogeneity 的方法相比，这是一个显著的实用性差距。
- 建议：在 Limitations 中更坦诚地讨论这一限制的严重性，或提供关于如何选择 subgroup 定义的实用指导（e.g., 基于 domain knowledge + 先验误差分析的启发式方法）。

---

## 小问题（不影响接收）

**M1.** 标题 "When LLM Annotation Debiasing Hurts" 稍显 provocative，但论文内容充分支撑了这一声称（50% of K=2 configurations, Figure 2 的 heatmap），可以接受。不过 "debiasing" 一词在因果推断社区有特定含义（Chernozhukov et al., 2018 的 double/debiased ML），与本文的 "confusion matrix correction" 可能造成歧义。论文在脚注 1 中做了澄清，但标题本身可能误导读者。

**M2.** Figure 1 的信息传达有效，但 panel 标注 "(a) Subgroup A (low error)" 和 "(b) Subgroup B (high error)" 可以增加具体的 error rate 数值以帮助理解。

**M3.** Table 1 的列标签 "Cov." 应明确为 "Coverage (95% CI)" 以避免歧义。

**M4.** Section 4.3 的 variance-adjusted CausalForestDML 描述中，plug-in SE 的近似条件 (n_expert ≥ 100) 在正文中提到但 justification 在 Appendix Q。建议在正文中至少用一句话解释为什么这个阈值是合理的（e.g., "below this threshold, confusion matrix estimation variance is non-negligible relative to outcome variance"）。

**M5.** 参考文献 Törnberg (2024/2025) 的年份在 bib 中记为 2025，但 journal 条目似乎是 2024 发表——需要核实年份一致性。

**M6.** 50 条 bib entries 对一篇 EMNLP long paper 来说数量充足（Director 信息提到 37 篇，实际 bib 文件中有 50 条）。引用年份分布合理：覆盖了经典文献（1979-2006）、中期方法论（2008-2020）、和最新工作（2023-2026），包括 Messing (2026)、Mozer (2026)、Sui & Candès (2026) 等 2026 年工作。

---

## Questions for Authors

**Q1.** Theorem 1 的 bias identity 能否从 Carroll et al. (2006) 的 functional measurement error framework 中作为 special case 推导出来？如果能，请明确说明需要哪些额外的结构化假设才能得到你们的 product form；如果不能，请解释为什么。

**Q2.** EC-HTE 的 hierarchical prior 选择（Dirichlet centered at global estimate）是否做过 sensitivity analysis？如果换用 weakly informative prior（如 Dirichlet(1,1)），对 small-sample subgroups 的影响有多大？

**Q3.** Diagnostic（Proposition 3）的 AUC = 0.86 看起来不错，但实际使用中，false negative（漏检 harmful correction）和 false positive（误报 safe correction as harmful）的代价是不对称的。是否考虑过 precision-recall 分析而非 ROC/AUC？

**Q4.** 论文在 Appendix Z.2 展示了 outcome-dependent misclassification（违反 A1）下的 robustness，EC-HTE 维持 ≥ 93.5% coverage。但 violation strength (γ) 的范围设定（0.1-0.5）是否覆盖了实际 LLM 标注中 outcome-dependence 的典型幅度？是否有 empirical evidence 支撑这一范围？

---

## 格式合规性（EMNLP 2026 / ARR）

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✓ | Sections 1-6（含 Conclusion）结束于第 8 页；Limitations 溢出到第 9 页但不计入页数限制 |
| `\usepackage[review]{acl}` | ✓ | main.tex 第 2 行确认 |
| 匿名性 | ✓ | 作者为 "Anonymous"，未发现自引泄露、代码链接（"released upon acceptance"）、致谢 |
| Limitations section | ✓ | 存在且内容充分，覆盖 ~5 个要点（Assumption A1 sensitivity, expert budget, pre-defined subgroups, class balance, coverage threshold） |
| Ethical Considerations | — | 未发现专门 section，但 Limitations 中隐含了部分讨论。ARR 不强制要求。 |
| 参考文献格式 | ✓ | 符合 ACL style |
| ARR Checklist | — | 在 OpenReview 表单中填写（main.tex 中 `%\input{checklist}` 已注释），符合规范 |

---

## Limitations 评估

论文自述的 Limitations（第 8-9 页）涵盖：
1. Assumption (A1) 不可检验性 + sensitivity analysis
2. Expert budget requirements（~60 labels/subgroup for K=2）
3. Pre-defined subgroup 假设
4. Class balance 要求 P(Z=1) ≈ 0.5（Appendix R 放松到 class imbalance）
5. Plug-in SE 的 coverage 在 small n_expert 时不足

**诚实度评价**: 整体诚实且全面。

**未提及的重要局限**:
- (a) **Subgroup 数量 K 的 scalability**：论文实验中 K 最多到 4（semi-synthetic）和 6（open-source LLM），但在高维 text feature 定义的 subgroup 中 K 可能很大。当 K 增大时，per-subgroup expert labels 需求线性增长，hierarchical Bayes 的 partial pooling 优势可能不足以弥补 sparsity。
- (b) **Continuous effect modifiers**: 论文仅处理 discrete subgroups，但实际 NLP 应用中 effect modifier 常为 continuous（如 text length, sentiment score）。离散化引入的 information loss 未讨论。
- (c) **Multi-class classification**: 论文聚焦 binary classification (Z ∈ {0,1})。多分类场景下 confusion matrix 维度增长为 J×J，hierarchical estimation 的样本需求和收敛性质可能显著不同。Appendix C 的 multi-class extension（Corollary 4）给出了理论扩展但未做实验验证。

---

## 最终评分

| 评分项 | 分数 |
|--------|------|
| Overall Assessment | **3.5** (Borderline Conference) |
| Soundness | 4 / 5 |
| Excitement | 3 / 5 |
| Reproducibility | 4 / 5 |
| Confidence | 4 / 5 |

**推荐理由**: 论文识别了一个重要且非直觉的问题（LLM annotation heterogeneous misclassification 使标准 correction 适得其反），提供了严谨的理论刻画和全面的实验验证。两个 Must-Fix 问题——(N1) 与经典文献的区分论证不充分、(N2) 方法贡献本质上是已知工具的直接应用——使得 novelty 深度不足以确信支撑 Conference 级别接收。如果作者能在 rebuttal 中有力地论证 N1（展示 bias identity 不能从已有 results 推导），并补充 N2 的 methodological extension 或更清晰的贡献定位，评分可以上调到 4。当前评分为 3.5，确认为 strong Findings candidate。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-23T09:00:56.642182+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Plug-in SE 低估不确定性，且 bootstrap 修复仅停留在提议层面\n- Variance-adjusted CausalForest 的 SE 公式（Eq. 5）是纯 plug-in 近似，不传播 Ĉ_s 的估计不确定性。EC-HTE 的 HB shrinkage 优势在 n_expert 较小时最显著（Table 3），但在同一 regime 下 CI 不可靠——方法的核心卖点与其已知缺陷在同一参数区间内矛盾。Appendix Y 的 bootstrap 实验仅验证 n_expert=200，未覆盖关键的 n_expert<100 区间。\n\n**N2** [critical] 缺乏真实数据 CATE 基准验证\n- 所有定量评估均来自 synthetic/semi-synthetic DGP，ground-truth τ(z) 是注入的。Hate Speech case study（Appendix M）仅报告 pattern consistency。Semi-synthetic DGP 的 CATE 注入采用简单的加性/线性形式。\n\n### Should-Fix 问题\n\n**W1** [warning] Assumption A3（balanced classes）的限制性在正文中弱化呈现\n**W2** [warning] Subgroup 定义依赖用户先验，缺乏选择指导\n**W3** [warning] PPCI 组合的 \"正交性\" 论证不充分\n**W4** [warning] κ > 100 singularity guard 阈值选择缺乏充分论证\n\n### Minor Issues\n- M1: Eq. (2) amplification factor 变量范围未标注\n- M2: Table 1 \"Bias\" 列标题未说明是 |bias| 还是 signed bias\n- M3: Figure 2 heatmap color bar 范围两子图不一致\n- M4: Section 2 部分引用过于简略\n- M5: Appendix Z.3 coverage breakdown 不完整\n\n### Questions\n- Q1: Plug-in SE 在 n_expert < 100 时 coverage 降至多少？\n- Q2: Hate speech case study 能否构建 pseudo ground-truth CATE？\n- Q3: Proposition 3 的 diagnostic 能否反过来用于 subgroup selection？\n- Q4: Corollary 5 下 Δτ_s 与 δ_s 相关时 amplification 效应如何变化？\n- Q5: K=4 下 budget crossover point 是否显著不同于 K=2？\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor Issues 和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Plug-in SE 低估不确定性，且 bootstrap 修复仅停留在提议层面\n- Variance-adjusted CausalForest 的 SE 公式（Eq. 5）是纯 plug-in 近似，不传播 Ĉ_s 的估计不确定性。EC-HTE 的 HB shrinkage 优势在 n_expert 较小时最显著（Table 3），但在同一 regime 下 CI 不可靠——方法的核心卖点与其已知缺陷在同一参数区间内矛盾。Appendix Y 的 bootstrap 实验仅验证 n_expert=200，未覆盖关键的 n_expert<100 区间。\n\n**N2** [critical] 缺乏真实数据 CATE 基准验证\n- 所有定量评估均来自 synthetic/semi-synthetic DGP，ground-truth τ(z) 是注入的。Hate Speech case study（Appendix M）仅报告 pattern consistency。Semi-synthetic DGP 的 CATE 注入采用简单的加性/线性形式。\n\n### Should-Fix 问题\n\n**W1** [warning] Assumption A3（balanced classes）的限制性在正文中弱化呈现\n**W2** [warning] Subgroup 定义依赖用户先验，缺乏选择指导\n**W3** [warning] PPCI 组合的 \"正交性\" 论证不充分\n**W4** [warning] κ > 100 singularity guard 阈值选择缺乏充分论证\n\n### Minor Issues\n- M1: Eq. (2) amplification factor 变量范围未标注\n- M2: Table 1 \"Bias\" 列标题未说明是 |bias| 还是 signed bias\n- M3: Figure 2 heatmap color bar 范围两子图不一致\n- M4: Section 2 部分引用过于简略\n- M5: Appendix Z.3 coverage breakdown 不完整\n\n### Questions\n- Q1: Plug-in SE 在 n_expert < 100 时 coverage 降至多少？\n- Q2: Hate speech case study 能否构建 pseudo ground-truth CATE？\n- Q3: Proposition 3 的 diagnostic 能否反过来用于 subgroup selection？\n- Q4: Corollary 5 下 Δτ_s 与 δ_s 相关时 amplification 效应如何变化？\n- Q5: K=4 下 budget crossover point 是否显著不同于 K=2？\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor Issues 和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-23T09:01:18.557152+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21914
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-23T09:01:18.710200+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] 与经典测量误差文献的区分需要更明确\n- \"misspecified correction amplifies MSE\" 在 Carroll et al. (2006, Chapter 4) 和 Fuller (1987, Section 2.3) 中已有论述。论文需要更清晰地用数学语言论证 effect modifier 角色使得 bias identity 不能由已有结果直接推导。Battistin & Chesher (2014) 和 Imai & Yamamoto (2010) 已研究了相关问题。\n\n**N2** [critical] HB partial pooling 方法新颖性不足\n- EC-HTE 核心方法是 Dirichlet-Multinomial hierarchical prior + partial pooling，本质是 James-Stein shrinkage 的直接应用。论文自己承认这一点（Section 4.1）。Dawid & Skene (1979)、Paun et al. (2018) 在 annotation model 中有类似结构但更复杂。EC-HTE 是更简单的特例。\n\n### Should-Fix 问题\n\n**W1** [warning] 相关工作遗漏若干重要文献\n- LLM annotation variance 文献（Mellon et al., 2025; Bauer et al., 2024）、HTE with mismeasured treatment（Calvi et al., 2015）、Bayesian ME models（Gustafson 2003 讨论不够深入）\n\n**W2** [warning] Abstract 信息密度过高\n- ~250 词内塞入大量具体数字，核心 message 被淹没\n\n**W3** [warning] \"exact identity\" vs \"asymptotic bound\" 优势被过度强调\n- Frazis & Loewenstein (2003) 的 scalar attenuation 也是 exact，真正优势是 \"structured decomposition\"\n\n**W4** [warning] Pre-defined subgroup 假设限制实际适用性\n- 与 Causal Forest 等自动发现 heterogeneity 的方法相比，需要预定义 subgroup 是显著实用性差距\n\n### Minor Issues\n- M1: 标题 \"debiasing\" 可能与 DML 社区的 \"debiased ML\" 混淆\n- M2: Figure 1 panel 标注缺少具体 error rate 数值\n- M3: Table 1 \"Cov.\" 列标签应明确\n- M4: Section 4.3 plug-in SE 阈值 justification 应在正文\n- M5: Törnberg 年份需核实\n- M6: 50 条 bib entries 数量充足\n\n### 未提及的重要局限\n- (a) K 的 scalability\n- (b) Continuous effect modifiers\n- (c) Multi-class classification（Corollary 4 无实验验证）\n\n### Questions\n- Q1: Theorem 1 能否从 Carroll et al. (2006) framework 推导？\n- Q2: Hierarchical prior sensitivity（Dirichlet(1,1) vs empirical Bayes）\n- Q3: Diagnostic 的 precision-recall 分析（false negative vs false positive 代价不对称）\n- Q4: A1 violation strength γ 范围是否覆盖实际 LLM 标注？\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor Issues、未提及局限和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] 与经典测量误差文献的区分需要更明确\n- \"misspecified correction amplifies MSE\" 在 Carroll et al. (2006, Chapter 4) 和 Fuller (1987, Section 2.3) 中已有论述。论文需要更清晰地用数学语言论证 effect modifier 角色使得 bias identity 不能由已有结果直接推导。Battistin & Chesher (2014) 和 Imai & Yamamoto (2010) 已研究了相关问题。\n\n**N2** [critical] HB partial pooling 方法新颖性不足\n- EC-HTE 核心方法是 Dirichlet-Multinomial hierarchical prior + partial pooling，本质是 James-Stein shrinkage 的直接应用。论文自己承认这一点（Section 4.1）。Dawid & Skene (1979)、Paun et al. (2018) 在 annotation model 中有类似结构但更复杂。EC-HTE 是更简单的特例。\n\n### Should-Fix 问题\n\n**W1** [warning] 相关工作遗漏若干重要文献\n- LLM annotation variance 文献（Mellon et al., 2025; Bauer et al., 2024）、HTE with mismeasured treatment（Calvi et al., 2015）、Bayesian ME models（Gustafson 2003 讨论不够深入）\n\n**W2** [warning] Abstract 信息密度过高\n- ~250 词内塞入大量具体数字，核心 message 被淹没\n\n**W3** [warning] \"exact identity\" vs \"asymptotic bound\" 优势被过度强调\n- Frazis & Loewenstein (2003) 的 scalar attenuation 也是 exact，真正优势是 \"structured decomposition\"\n\n**W4** [warning] Pre-defined subgroup 假设限制实际适用性\n- 与 Causal Forest 等自动发现 heterogeneity 的方法相比，需要预定义 subgroup 是显著实用性差距\n\n### Minor Issues\n- M1: 标题 \"debiasing\" 可能与 DML 社区的 \"debiased ML\" 混淆\n- M2: Figure 1 panel 标注缺少具体 error rate 数值\n- M3: Table 1 \"Cov.\" 列标签应明确\n- M4: Section 4.3 plug-in SE 阈值 justification 应在正文\n- M5: Törnberg 年份需核实\n- M6: 50 条 bib entries 数量充足\n\n### 未提及的重要局限\n- (a) K 的 scalability\n- (b) Continuous effect modifiers\n- (c) Multi-class classification（Corollary 4 无实验验证）\n\n### Questions\n- Q1: Theorem 1 能否从 Carroll et al. (2006) framework 推导？\n- Q2: Hierarchical prior sensitivity（Dirichlet(1,1) vs empirical Bayes）\n- Q3: Diagnostic 的 precision-recall 分析（false negative vs false positive 代价不对称）\n- Q4: A1 violation strength γ 范围是否覆盖实际 LLM 标注？\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor Issues、未提及局限和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-23T09:01:20.171543+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1461
}
```

</details>

---


### Assistant

_source line 976 · 2026-05-23T09:01:26.785662+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 90

## Round 90

2 recorded events


### User

_source line 977 · 2026-05-23T09:01:29.410903+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成。评分 **3.5 (Borderline Conference)**，已提交给 Review Director。

核心判断：问题识别重要（LLM annotation heterogeneous misclassification 使标准 correction 适得其反），理论严谨（exact bias identity, R² > 0.97 验证），实验全面（520 configs, 8 LLMs, real data）。两个 Must-Fix：(N1) 与经典测量误差文献的区分论证不够充分——需要用数学语言展示 effect modifier 角色为何使 bias decomposition 结构性不同；(N2) HB partial pooling 方法是 James-Stein shrinkage 的直接应用，方法新颖性有限。如果 rebuttal 能有力回应 N1 并补充方法贡献定位，评分可上调至 4。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 978 · 2026-05-23T09:01:36.898252+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 91

## Round 91

2 recorded events


### User

_source line 979 · 2026-05-23T09:05:13.452924+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### R1-N1: Plug-in SE 低估不确定性，bootstrap 修复仅停留在提议层面

**[AGREE]** 这是论文一个真实的结构性矛盾，R1 准确地指出了它。

具体证据与我的分析：
- Section 4.3（p6）明确承认 plug-in SE "do not propagate uncertainty from the confusion matrix estimation itself"，并设定 n_expert ≥ 100 为合理性阈值。
- Appendix Y（p25）的 bootstrap 验证仅在 n_expert = 200 的条件下进行（coverage 从 92.5% 提升到 95.0%），未覆盖 n_expert < 100 的关键区间。
- 而 Table 3（p15）恰恰显示 HB partial pooling 相对于 Stratified MLE 的 RMSE 优势在 n_expert ≤ 75 时最大（例如 K=2 extreme: n=25 时 HB RMSE 0.256 vs Strat.MLE 0.269）。

**核心矛盾**：EC-HTE 的 HB shrinkage 在 small n_expert 时提供最大的点估计优势，但在同一 regime 下 CI 的 coverage 保证最弱。这意味着用户在最需要 EC-HTE 的场景下，却无法信任其置信区间——这对一个以 "correction" 为卖点的方法来说是严重的实用性问题。

**补充 R1 未提到的一点**：Appendix Y 的 Monte Carlo 验证确实在 n_expert = 50 时也报告了 plug-in coverage（约 93.8% aggregate），说明即便在较小预算下 coverage 也不至于崩溃。但 93.8% vs 95% 的 gap 在 subgroup level 可能更大，论文未报告 per-subgroup coverage breakdown at small n_expert，这使得问题更难评估。

建议作者在 rebuttal 中提供 n_expert ∈ {25, 50, 75} 下的 bootstrap coverage，并报告 per-subgroup breakdown。

---

### R1-N2: 缺乏真实数据 CATE 基准验证

**[AGREE]**，但认为严重程度应降级为 Should-Fix。

R1 正确指出所有定量评估均来自注入 ground-truth τ(z) 的 DGP。Hate Speech case study（Appendix M, p18）仅展示 pattern consistency（misclassification heterogeneity Δ = 0.117, FNR range 8.5%–21.9%），无法定量验证 CATE correction 的准确性。

然而，这是因果推断方法论文的固有局限，而非本文特有的缺陷：
- **CausalForest 原始论文**（Wager & Athey, 2018）的实验验证同样以 synthetic/semi-synthetic 为主。
- **PPI**（Angelopoulos et al., 2023）的 CATE-level 验证也是 synthetic。
- 论文在 p9 明确承认 "We leave full real-data validation—on a dataset combining RCT design, ground-truth CATEs, and LLM annotations—to future work"，这是诚实的。

论文的验证层次——520 synthetic configs（Section 5.2）→ semi-synthetic TweetEval（Section 5.3）→ real confusion matrices 11 model-dataset combos（Appendix N, R² > 0.975）→ real-data case study patterns（Appendix M）——在方法论文中属于较全面的设计。

**但 R1 的建议有建设性意义**：Hate Speech case study 可以通过 held-out expert labels 构建 pseudo ground-truth CATE（类似 Appendix S 的 R-learner validation, p21, Table 16），这不是根本不可行的。建议作者在 rebuttal 中尝试。

---

## Should-Fix 问题

### R1-W1: Assumption A3（balanced classes）限制性在正文中弱化

**[REBUT]** 论文已有充分的鲁棒性验证。

- Appendix R（p22, Table 18）测试了 P(Z=1) 从 0.1 到 0.9 的全范围 class imbalance，结果 R² ≥ 0.976 across all levels，EC-HTE outperforms global correction at all imbalance levels。
- Remark 2（Section 3, p4）明确指出 "Theorem 1 does not require assumption (A2). For arbitrary asymmetric confusion matrices (FPR ≠ FNR), the product form holds exactly"。
- Section 3 正文说明 A3 "simplifies the exposition; the identity generalizes to subgroup-specific Δτ (Corollary 5, Appendix C)"。
- Appendix J（p17）测试了 asymmetric misclassification extension，EC-HTE with asymmetric formula achieves 94.5% coverage (vs 91.0% symmetric assumption)。

A3 是 **expositional convenience** 而非 structural limitation，论文在正文和附录中都清楚地说明了这一点。我不认为正文需要更多修改，但可以在 Section 3 的 A3 描述后添加一句显式 forward reference 到 Appendix R 和 J。

---

### R1-W2: Subgroup 定义依赖用户先验，缺乏选择指导

**[AGREE]** 这与我自己的 W4 一致。

论文要求 subgroup assignment S: X → {1,...,K} 预先定义（Section 3, Assumption A5）。Limitations（p9）提到 "continuous effect modifiers or latent subgroup discovery...future work"，但未提供任何关于如何选择 subgroup 定义的实用指导。

Section 5.1（p7）的 semi-synthetic 和 Appendix M（p18）的 Hate Speech case study 都使用 domain-driven subgroup 定义（text features: hashtag presence, text length），这在某种程度上展示了实践中的选择方式，但论文未系统讨论。

补充一点：Appendix H（p15）的 Diagnostic ROC Curves 和 Section 5.4 的 actionable diagnostic 实际上可以反过来辅助 subgroup selection——先用粗粒度 subgroup 定义运行 diagnostic，再根据 δ_s 的分布 refine。论文可以把这一 workflow 明确写出来。

---

### R1-W3: PPCI 组合的 "正交性" 论证不充分

**[REBUT]** 经验证据充分，但同意理论论证可加强。

Appendix K（Table 8, p18）采用 2×2 factorial design（4 DGPs: A=covariate only, B=outcome only, C=both, D=none）系统验证了 EC-HTE 和 PPCI 的正交性：
- DGP A（仅 covariate error）：EC-HTE |bias| = 0.017, PPCI = 0.015, EC-HTE+PPCI = 0.017 → EC-HTE 已充分处理
- DGP B（仅 outcome error）：EC-HTE = 0.015, PPCI = **0.020**, EC-HTE+PPCI = **0.012** → PPCI 起关键作用
- DGP C（双重误差）：EC-HTE = 0.179, PPCI = 0.017, EC-HTE+PPCI = **0.007** → 组合效果显著
- DGP D（无误差）：所有方法 |bias| ≤ 0.010

这一 factorial 设计是检验正交性的标准实验方法。Section 4.3（p6）也提供了机制解释："EC-HTE addresses misclassification in the effect modifier Z covariate space, while PPCI corrects prediction error in the outcome model Y(1), Y(0) (prediction space)."

R1 说论证不充分可能指的是缺少形式化的理论保证（如：一个证明两种 correction 在 bias decomposition 中 additive separable）。这一点有道理，但 4-DGP factorial evidence + 机制解释在实践层面已足够支撑 claim。建议作者在 camera-ready 中增加一段 remark 明确定义 "orthogonality" 的技术含义（error sources affect different components of the estimator），避免读者误解为 statistical independence。

---

### R1-W4: κ > 100 singularity guard 阈值缺乏充分论证

**[REBUT]** 论文在 Appendix A（p11-12）已提供阈值不敏感性的经验验证。

Appendix A 的 sweep 结果：
- 在标准 DGP（K=2, extreme heterogeneity, n_expert=250, 100 MC runs）下，所有配置中 maximum observed κ = 1.89（mean 1.45, p99 1.89）
- R̂ < 1.01 且 ESS > 1618 across all runs
- 这意味着阈值从 2 到 1000 之间任意选择都不影响结果——κ > 100 从未在正常配置中触发

Table 2（p15）的收敛诊断进一步确认：所有配置均满足 R̂ < 1.01 和 ESS > 845。Singularity guard 是一个 safety net 而非 tuning parameter。

R1 可能的合理关切是：在 near-degenerate 的极端配置下（π_s → 0.5），κ 可能接近 100 并触发 guard。但这恰恰是 guard 应该触发的场景——此时 confusion matrix 接近 singular，matrix inversion 数值不稳定，fallback 到 global correction 是正确的行为。阈值的选择不需要精确优化，只要在 "clearly invertible" 和 "nearly singular" 之间划线即可。100 是合理的保守值。

---

## Minor Issues

**R1-M1** [AGREE] Eq. (2) amplification factor 的变量有效范围（π_s < 0.5, A5 non-degeneracy）应在公式附近标注。小修改。

**R1-M2** [AGREE] Table 1 的 "Bias" 列确实需要明确是 |bias|（absolute）。从数值看全为正数，应是 absolute bias，但未注明。Table caption 中 "averaged over subgroups" 的描述也暗示了某种 aggregation，应明确说明。

**R1-M3** [REBUT] Figure 2 两个 panel 的 color bar 范围不同是合理的设计选择。Panel (a) Low-error subgroup 的 bias 范围远小于 Panel (b) High-error subgroup，统一 color bar 会使 Panel (a) 的细节完全不可见。图例下方标注了具体数值范围。更好的做法是在 caption 中显式说明两个 panel 的 color scale 不同且为什么这样设计。

**R1-M4** [AGREE] Section 2 部分引用确实简略，特别是对 annotation model extensions 和 treatment effects + measurement error 的讨论。在 8 页限制下这是 space-quality tradeoff，但同意可以改善重点引用的讨论深度。

**R1-M5** [AGREE] 如果 Appendix Z.3 的 coverage breakdown 不完整，应补充。这是支撑 robustness claim 的关键证据。

---

## Questions

**R1-Q1**: Plug-in SE 在 n_expert < 100 时 coverage 降至多少？

**[REBUT]** 论文 Appendix Y（p25）实际上报告了 n_expert = 50 的结果。Table 22 中 CausalForestDML plug-in SE 在 K=2 extreme 下：
- n_expert = 50 (s₁, π=0.05): coverage 0.959, n_expert = 50 (s₂, π=0.25): coverage 0.925
- Aggregate: 0.938（即 93.8%）

所以在 n_expert = 50 时 coverage 并未崩溃（93.8% vs 95% target），但确实低于 nominal level。R1 的关切在 n_expert < 50 时可能更 acute，但论文未测试这个区间。论文也明确给出了 n_expert ≥ 25 × K = 50 的 minimum budget guideline（Algorithm 1, Preconditions），在此之下不推荐使用 EC-HTE。

**R1-Q2**: Hate speech case study 能否构建 pseudo ground-truth CATE？

**[AGREE]** 如我在 N2 回应中所述，这是可行的。Kennedy et al. (2020) 的 Hate Speech corpus 提供了 continuous severity ratings + crowd worker annotations，可以用 held-out gold labels + bootstrapped treatment effects 构建 pseudo ground-truth τ(z)。建议作者在 rebuttal 中补充。

**R1-Q3**: Proposition 3 的 diagnostic 能否反过来用于 subgroup selection？

**[AGREE]** 这是一个很好的 insight。Proposition 3 的条件 |δ_s|/(1−2π_s) > 1 本质上是对每个 subgroup s 的 correction risk 评估。如果 practitioner 有多种候选 subgroup 定义，可以用 diagnostic AUC 作为选择标准——选择使 diagnostic 最具区分力（high AUC）的 subgroup 定义。论文目前没有讨论这一应用，但 Appendix H 的 ROC curves（Figure 3, p15）已经提供了 evaluation framework。

**R1-Q4**: Corollary 5 下 Δτ_s 与 δ_s 相关时 amplification 效应如何变化？

**[REBUT]** 论文在 Appendix Z.2（p26）的 outcome-dependent misclassification robustness测试中间接覆盖了这一场景。当 misclassification 与 outcome 相关时（γ > 0，violation of A1），Δτ_s 和 δ_s 之间的相关性自然产生。Table 25（p26）显示即使在 adversarial configuration 下（high-error S1 = larger treatment effect），EC-HTE 仍维持 ≥ 93.5% coverage with |bias| 适度增大但未失控。这说明 Δτ_s-δ_s 相关性的实际影响是可控的，尽管论文未给出解析表达式来精确量化 amplification 的变化。

**R1-Q5**: K=4 下 budget crossover point 是否显著不同于 K=2？

**[REBUT]** 论文已有相关数据。Table 3（p15）直接比较了 K=2 和 K=4 的 RMSE。Appendix I（p15）给出了 expert budget crossover curves，Figure 5（p22）的 Applicability Frontier 也覆盖了 K=4。具体数据：
- K=2: crossover at n_expert ≈ 50（250 total labels for K=2）
- K=4: Figure 5 的 dashed lines 显示 crossover 在 n_expert ≈ 250 for K=4 extreme

K=4 的 crossover budget 确实显著高于 K=2（per-subgroup label 需求大致相同，但总需求线性增长）。Table 3 中 K=4 的 HB vs MLE 差距在 small budgets 时更大，也说明 partial pooling 在 K=4 时更重要。论文数据是完整的，但建议在正文 Section 5.2 中增加一句明确对比 K=2 vs K=4 crossover 的总结。

---

## 总结评价

R1 的审稿意见整体高质量且切中要害。**N1**（plug-in SE 矛盾）是最有力的批评，指出了方法优势与已知缺陷在同一参数区间的结构性矛盾。**N2**（缺乏 real CATE ground truth）虽然合理，但在因果推断文献中属于普遍性挑战，严重程度应降为 Should-Fix。W1 和 W4 我认为论文已有充分回应（分别在 Appendix R 和 Appendix A），不构成真正的 weakness。W2 和 W3 的关切有部分道理。

如果 R1 和我的评分一致（均为 3.5 Borderline Conference），结合 N1 的实质性缺陷和整体的理论+实验质量，我维持 **3.5** 的评分不变。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 980 · 2026-05-23T09:05:19.692434+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 92

## Round 92

2 recorded events


### User

_source line 981 · 2026-05-23T09:05:31.945356+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部意见的逐条回应，核心判断：

- **N1 (plug-in SE 矛盾)**: [AGREE] — 方法优势与 CI 可靠性在 small n_expert 区间存在结构性矛盾，bootstrap 验证未覆盖关键区间
- **N2 (缺乏 real CATE ground truth)**: [AGREE] 但建议降级为 Should-Fix，因果推断文献的普遍性挑战
- **W1 (A3 balanced classes)**: [REBUT] — Appendix R + Remark 2 已有充分鲁棒性验证
- **W2 (subgroup 选择)**: [AGREE] — 与我自己的 W4 一致
- **W3 (PPCI 正交性)**: [REBUT] — Table 8 的 factorial design 提供了充分经验证据
- **W4 (κ > 100 阈值)**: [REBUT] — Appendix A 的 sweep 显示阈值从未在正常配置触发，不是 load-bearing

维持 Overall 3.5 (Borderline Conference) 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 982 · 2026-05-23T09:05:39.543397+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 93

## Round 93

22 recorded events


### User

_source line 983 · 2026-05-23T09:05:42.298963+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: 与经典测量误差文献的区分**

R2 认为 "misspecified correction amplifies MSE" 在 Carroll et al. (2006) 和 Fuller (1987) 中已有论述，要求论文更清晰地论证 effect modifier 角色的数学独特性。

我认为 R2 低估了 Theorem 1 与经典结果的结构性差异：

1. **Carroll et al. 处理的是 mismeasured regressor 的 attenuation bias**：经典结论为 β̂ = β·κ（κ = reliability ratio），bias 是系数的 scalar attenuation。本文处理的是 mismeasured *effect modifier*——变量 Z 定义 CATE 函数 τ(z) 本身，而非作为回归自变量。这在数学上导致本质不同的 bias 结构。

2. **Theorem 1 的乘积分解是新的**：bias = δ_s · Δτ / (1−2π̄) 将 bias 分解为三个可解释因子——misclassification heterogeneity (δ_s)、treatment effect heterogeneity (Δτ) 和 amplification factor (1/(1−2π̄))。Carroll et al. 的框架无法直接产生这一分解，因为其模型不涉及 subgroup-varying error rates 与 heterogeneous treatment effects 的交互。

3. **关键性质**：bias 为零当且仅当 δ_s=0 或 Δτ=0（Section 3, page 4-5），即 homogeneous errors 或 homogeneous treatment effects 任一成立即消除 bias。这一 "乘积消零" 性质在 Carroll et al. 中没有对应物。

4. **Battistin & Chesher (2014) 和 Imai & Yamamoto (2010)** 的确研究了相关问题，但前者聚焦 heterogeneous error analyses 的 bounds（而非 exact identity），后者处理 treatment misclassification（而非 effect modifier misclassification）。论文 Section 2 (page 3) 已明确指出 "Our setting differs in three respects"。

**不过，R2 的一个子论点有道理**：论文确实应在正文（而非仅 Section 2 的散文描述中）用数学符号对比 Carroll et al. 的 attenuation formula 与 Theorem 1 的 structured decomposition，以更直观地展示差异。这可以用一个 Remark 解决，约 3-4 行。

**结论**：贡献不被 Carroll et al. 涵盖，但表述可以更锐利。建议在 Section 3 增加数学对比 Remark，不影响 novelty 判断。

---

**[REBUT] R2-N2: HB partial pooling 方法新颖性**

R2 认为 EC-HTE 核心方法是 "James-Stein shrinkage 的直接应用"，新颖性不足。

1. **组件 vs 框架**：Dirichlet-Multinomial HB 本身确实是标准工具。但 EC-HTE 的贡献不是发明新的 estimation algorithm，而是构建了一个完整的 pipeline：(a) Theorem 1 揭示*为什么*需要 subgroup-stratified correction → (b) HB 作为*如何*在有限 expert labels 下实现 stratification 的实用手段 → (c) variance-adjusted CausalForest (Eq. 5) 传播不确定性 → (d) Proposition 3 的 diagnostic 判断*何时*需要 correction → (e) PPCI 组合处理 joint errors。剥离 HB 单独评价新颖性相当于只看 pipeline 的一个环节。

2. **Dawid & Skene (1979) 和 Paun et al. (2018) 的区别**：这些工作估计 annotator-specific 参数用于 label aggregation，而非 subgroup-specific confusion matrices 用于 downstream causal inference。EC-HTE 将 confusion matrix estimation 的输出直接接入 CausalForest 的 pseudo-outcome correction（Section 4.2, Eq. 4），这一连接在先前文献中不存在。

3. **经验证据支持框架的价值**：Table 1 (page 7) 显示 EC-HTE (HB) 在 K=2 extreme 下 |bias| 从 Global 的 0.059 降至 0.008 (7.4×)，RMSE 从 0.094 降至 0.012。仅用 "James-Stein shrinkage" 无法解释为什么 Stratified MLE 在同一设定下 RMSE 为 0.087——HB 的优势来自框架设计（shrinkage + fallback + variance adjustment），而非单纯的 shrinkage。

**结论**：HB 组件本身不新颖，但作为 must-fix 不成立。论文应该在 Section 4.1 更明确承认与 Dawid & Skene 的联系，但这是 should-fix 级别的改进，不影响接收。

---

### Should-Fix 问题

**[AGREE] R2-W1: 相关工作遗漏**

R2 指出的文献遗漏是合理的：
- **Mellon et al. (2025)** 和 **Bauer et al. (2024)** 关于 LLM annotation variance 与本文直接相关——它们为 misclassification heterogeneity 的存在提供了独立的经验证据
- **Calvi et al. (2015)** 研究 HTE with mismeasured treatment，虽然 treatment 角色与 effect modifier 不同，但方法论思路有可比性
- **Gustafson (2003)** 已在 Section 2 (page 2) 引用，但仅一句话，对 Bayesian measurement error 模型的讨论确实不够深入

建议在 Section 2 增加一段讨论这些文献，约 4-5 句，明确本文方法与它们的区别。

---

**[AGREE] R2-W2: Abstract 信息密度过高**

我重新阅读了 Abstract (page 1)——确实在约 250 词内塞入了：5×, Δπ=0.03, 50% of K=2 configurations, 74-82%, R² > 0.97, Proposition 3, AUC=1.0, PPCI 等大量数字。核心 message（"global correction hurts when error rates are heterogeneous across subgroups"）被稀释了。建议精简到 3-4 个关键数字，将其余移至 Introduction 或 Results。

---

**[AGREE] R2-W3: "exact identity" vs "asymptotic bound" 的表述**

R2 指出 Frazis & Loewenstein (2003) 的 scalar attenuation β̂ = β(1 − π₀ − π₁) 同样是 exact（非 asymptotic bound）。这一点是正确的。论文 Section 2 (page 3) 中 "derives an exact identity for correction-induced bias" 的措辞暗示 exactness 本身是新颖的，但真正的新颖性在于 **structured decomposition**——将 bias 分解为 δ_s, Δτ, amplification 三个可解释因子的乘积。建议将 "exact identity" 改为 "structured bias decomposition identity" 或类似表述，更准确地传达贡献。

---

**[AGREE] R2-W4: Pre-defined subgroup 限制**

这与我的 W2 一致。论文确实没有提供 data-driven subgroup discovery 方案。与 CausalForest 自动发现异质性的能力相比，EC-HTE 需要用户预定义 S: X → {1,...,K}，这是显著的实用性差距。

补充我自己的观察：Section 5.4 的 diagnostic (Proposition 3) 实际上可以作为 subgroup selection 的基础——对候选 subgroup 划分计算 per-subgroup misclassification rates，选择 Δπ 最大的划分方案。但论文未讨论这一用法。建议在 Discussion 中补充。

---

### Minor Issues

**[AGREE] R2-M1**: "debiasing" 与 DML 社区 "debiased ML" 的术语混淆确实存在。论文 footnote 1 (page 1) 已做澄清（"'debiasing' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing"），但未提及 DML 意义上的 debiasing。建议在 footnote 中加一句。

**[AGREE] R2-M2**: Figure 1 (page 2) 的 panel 标注确实缺少具体 error rate 数值。图注说 "Global correction applies the pooled error rate π̄ uniformly" 但未标注 π̄ 和 π_s 的具体值。补充数值能帮助读者理解 bias 的量级。

**[AGREE] R2-M3**: Table 1 (page 7) "Cov." 列应明确为 "95% CI Coverage"。这与我的 M2 一致。

**[AGREE] R2-M4**: Plug-in SE 的 valid regime (n_expert ≥ 100) 应在正文明确。这与我的 N1 一致——目前此信息仅在 Section 4.3 的末尾和 Appendix Y 中提及。

**[REBUT] R2-M5**: Törnberg 年份——论文引用的是 "Törnberg, 2025"（page 2, References page 10-11）。我在首轮审稿中未发现年份错误。R2 应指出具体哪个 Törnberg 引用有年份问题，否则无法核实。如果是指 Törnberg (2023) vs (2025) 的区分，论文 References 中确实列出了 "Peter Törnberg. 2025. Large language models..."，需要作者确认是否为 preprint 年份更新。

**[AGREE] R2-M6**: Bib entries 数量充足，无异议。

---

### 未提及的重要局限

**[REBUT] R2-Limitation (a): K 的 scalability**

论文 Appendix L (page 16) 已测试 K=8 subgroups（n_expert=250, 100 MC runs）。Table 4 显示 HB EC-HTE 在 K=8 下 |bias|=0.005, RMSE=0.017，coverage=0.95，性能保持稳定。Section 9 (page 9) 也提到 "at K=8 with n_expert=250, EC-HTE maintains nominal coverage (95.6%)"。R2 可能遗漏了这一附录。

当然，K=8 之后的 scalability（如 K=20+）确实未测试。论文 page 9 提到 "interactional subgroups with many levels may exceed the n_expert × P(Z_minority)/K ≥ 25 budget threshold"，暗示 K 的 practical ceiling 受 expert budget 约束。这一限制已被讨论。

**[AGREE] R2-Limitation (b): Continuous effect modifiers**

这是一个真实的局限。论文全程假设 Z 是 discrete（binary sentiment）。如果 Z 是 continuous（如情感强度 0-1），confusion matrix 框架不直接适用。论文的 Limitations section 和 Discussion 均未提及这一点。建议在 Limitations 中增加一句。

**[AGREE] R2-Limitation (c): Corollary 4 (multi-class Z) 无实验验证**

Corollary 4 (page 12, Appendix C) 扩展到 J > 2 effect-modifier levels。但所有实验均使用 binary Z (J=2)。K=4 的实验是 4 个 subgroups（不是 4 个 class），因此不构成 Corollary 4 的验证。这是一个实质性的实验缺口。

不过，Corollary 4 的证明（Appendix C）是 Theorem 1 的直接推广，理论上的正确性不依赖实验。但至少应该有一个 J=3 或 J=4 的 sanity check 实验来验证经验表现。

---

### Questions 回应

**R2-Q1: Theorem 1 能否从 Carroll et al. (2006) 推导？**

不能直接推导。Carroll et al. 的核心框架处理 regression with mismeasured covariates，bias formula 是 attenuation factor × true coefficient。Theorem 1 的 bias 来自 global vs subgroup-specific confusion matrix 的 mismatch（M_global^{-1}·M_s − I），产生 δ_s·Δτ 的乘积结构。Carroll et al. 没有处理 subgroup-heterogeneous error rates 在 CATE 估计中的交互效应。

具体数学区别：Carroll et al. 的 attenuation 公式假设 single error structure across all observations，论文的设定是 subgroup-varying error structures pooled into a global correction。这需要矩阵代数处理 M_global^{-1}·M_s 的乘积（Appendix B, page 12），不可约化为 Carroll et al. 的 scalar attenuation。

但 R2 的启发式观点——"都是关于 misspecified correction amplifying error"——在 high level 上成立。建议在正文增加一个 Remark 对比两者的数学结构，如我在 N1 中建议的。

**R2-Q2: Hierarchical prior sensitivity**

论文 Appendix H (page 15) "Hyperprior sensitivity" 已回答此问题：Scaling Gamma(1,1) hyperprior by factors of 0.5× to 2× produces ±14% RMSE variation for K=2 and −5% for K=4. Coverage remains invariant across the sensitivity range. 这说明 HB 对 prior specification 的鲁棒性可接受。

Dirichlet(1,1)（uniform）vs empirical Bayes α₀ 的比较在 Section 4.1 (page 6) 中有隐含讨论：empirical Bayes α₀ 通过 marginal likelihood maximization 选择，优于 uniform prior。但 R2 要求的 explicit head-to-head 比较（Dirichlet(1,1) vs EB α₀ 的 RMSE/coverage 对比表）确实缺失。建议补充。

**R2-Q3: Diagnostic 的 precision-recall 分析**

Figure 3 (page 15) 报告了 ROC curves（AUC = 0.93 setting-level, 0.73 subgroup-level），但确实缺乏 precision-recall analysis。R2 指出 false negative（漏判 "debiasing hurts"）和 false positive（误判需要 EC-HTE）的代价不对称——这在实践中是关键问题。漏判 false negative 意味着使用了有害的 global correction；false positive 意味着不必要地增加了估计 variance。

Section 5.4 (page 8) 和 Appendix H (page 15) 讨论了 "cost-asymmetric diagnostic thresholds"："practitioners in high-stakes settings should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification." 这是正确的方向，但缺乏定量的 precision-recall curve。建议补充 F1/precision/recall at different thresholds 的表格。

**R2-Q4: A1 violation strength γ 的实际覆盖范围**

Appendix Z.2 (page 26) 测试 γ ∈ {0, 0.05, 0.10, 0.15, 0.20}。Table 25 显示 EC-HTE coverage ≥ 93.5% across full γ range。

R2 问 γ ∈ [0, 0.2] 是否覆盖了实际 LLM 标注的 outcome-dependent misclassification 强度。论文未提供 empirical calibration（即用真实 LLM + 真实 outcome 数据估计 γ 的实际值）。这与我的 N2 一致——缺乏真实数据验证意味着无法确定 γ 的 realistic range。建议在 Appendix Z.2 讨论 γ 的 practical calibration 方法（如用 held-out labels 回归 misclassification indicator on outcome）。

---

### 总结判断

R2 的审稿整体合理，多数 should-fix 和 minor issues 我赞同。但两个 must-fix 的严重程度我有异议：

- **N1（Carroll et al. 区分）**：属于 presentation improvement 而非 fundamental novelty 缺陷。Theorem 1 的乘积分解结构在 Carroll et al. 框架中没有对应物，增加一个数学对比 Remark 即可解决。降为 should-fix。
- **N2（HB 新颖性）**：评价标准偏差——以单个组件的 novelty 来否定框架的 novelty。EC-HTE 的贡献是理论驱动的框架设计，HB 是工具选择。降为 should-fix。

我维持 Overall 3.5 的判断，与 R2 一致。核心限制因素仍是我在首轮审稿中指出的 plug-in SE gap (R1-N1) 和真实数据验证缺失 (R1-N2)，而非 R2 的两个 must-fix。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-23T09:06:21.031741+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool call

_source line 985 · 2026-05-23T09:06:21.032248+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 986 · 2026-05-23T09:06:21.133247+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T08:51:03.745176+00:00\", \"completed_at\": \"2026-05-23T08:55:39.626758+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"连续 4 页无 figure/table。Pages 4-5 有 Theorem/Proposition 环境和公式提供部分视觉锚点，但 page 3（Related Work 纯文本）和 page 6（Method 4.1-4.3 纯文本）完全缺乏 display item，审稿人可能在此段感到节奏单调\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-9\", \"message\": \"主文仅 3 个 display items（Figure 1 page 2, Table 1 page 7, Figure 2 page 8），密度 0.33/页。对于同时声明理论+实证贡献的论文，这偏低。大量关键实验结果（Tables 3-11、Figure 3-4）全部在 Appendix，审稿人可能不会翻阅，导致低估实验力度\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"极度拥挤：Figure 2（双面板热力图）+ Section 5.4 + Section 6 Conclusion + Limitations 起始，全挤在一页。Conclusion 被压缩得很短，给审稿人\\\"草草收尾\\\"的印象\"}, {\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"Limitations 及剩余实验讨论延伸到第 9 页（整页纯文本，无 display item）。如果主文内容实际占 9 页（而非 8 页），需确认 Limitations 部分是否完整归入豁免页——否则可能触发格式违规\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Abstract 非常密集（约 250 词），填满了右栏大部分空间。内容信息量大但视觉上略显拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（首个 display item）出现在第 2 页顶部右栏，位置好。但图内文字标签（\\\"Subgroup A (low-error)\\\"、\\\"Subgroup B (high-error)\\\"）字号偏小，约为正文 60%，打印后可能难以阅读\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 自包含，传达了 global vs. subgroup-stratified correction 的核心机制——锚定效应正面\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，最优值加粗，小数位数一致（3 位），格式专业\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 热力图使用蓝-红渐变 + 斜线阴影标注\\\"debiasing hurts\\\"区域，设计有效。但 axis label \\\"Δπ (misclassification gap)\\\" 和 \\\"Δτ (CATE heterogeneity)\\\" 字号偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 10-11\", \"message\": \"References 格式统一，未发现 [?] 未解析引用或跳号。Author 缩写、年份格式一致\"}, {\"severity\": \"i
…[truncated 843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-23T09:06:21.133841+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-23T09:07:03.305131+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "description": "Check issue tracker size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "description": "Check issue tracker size"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-23T09:07:03.657509+00:00_

1242 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-23T09:07:12.240349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-23T09:07:12.391993+00:00_

1	issues:
2	  # === RESOLVED (prior rounds, unchanged) ===
3	  - id: "R1-N1"
4	    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
5	    category: method
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 0
9	    last_seen_round: 2
10	    action_items: []
11	    resolution: "重新推导为精确恒等式"
12	    resolution_round: 0
13	
14	  - id: "R2-W8"
15	    summary: "Proposition 1 限于 K=2"
16	    category: method
17	    severity: critical
18	    status: resolved
19	    first_raised_round: 0
20	    last_seen_round: 1
21	    action_items: []
22	    resolution: "Theorem 1 适用一般 K"
23	    resolution_round: 0
24	
25	  - id: "R1-N2"
26	    summary: "Real data ground truth CATE 来源不明"
27	    category: experiment
28	    severity: critical
29	    status: resolved
30	    first_raised_round: 0
31	    last_seen_round: 1
32	    action_items: []
33	    resolution: "恰当定位为 illustrative application"
34	    resolution_round: 0
35	
36	  - id: "R1-N3"
37	    summary: "HB 模型规格严重不完整"
38	    category: method
39	    severity: critical
40	    status: resolved
41	    first_raised_round: 0
42	    last_seen_round: 1
43	    action_items: []
44	    resolution: "完整 MCMC 规格"
45	    resolution_round: 0
46	
47	  - id: "JOINT-W4"
48	    summary: "相关工作严重遗漏"
49	    category: writing
50	    severity: warning
51	    status: resolved
52	    first_raised_round: 0
53	    last_seen_round: 1
54	    action_items: []
55	    resolution: "30+ 引用覆盖"
56	    resolution_round: 0
57	
58	  - id: "JOINT-W3"
59	    summary: "信息密度过高"
60	    category: writing
61	    severity: warning
62	    status: resolved
63	    first_raised_round: 0
64	    last_seen_round: 1
65	    action_items: []
66	    resolution: "主文精简至合理密度"
67	    resolution_round: 0
68	
69	  - id: "R2-W7"
70	    summary: "真实数据验证单薄"
71	    category: experiment
72	    severity: warning
73	    status: resolved
74	    first_raised_round: 0
75	    last_seen_round: 1
76	    action_items: []
77	    resolution: "恰当定位 + 公开数据集"
78	    resolution_round: 0
79	

…[truncated 540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-23T09:07:18.616297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-23T09:07:19.219057+00:00_

100	    resolution_round: 0
101	
102	  - id: "R2-W4"
103	    summary: "DSL 区分不充分"
104	    category: framing
105	    severity: info
106	    status: resolved
107	    first_raised_round: 0
108	    last_seen_round: 1
109	    action_items: []
110	    resolution: "Related Work + Appendix E 清晰技术区分 + DSL 等价性证明"
111	    resolution_round: 1
112	
113	  - id: "R1-W1"
114	    summary: "Causal Forest uncertainty propagation 不清楚"
115	    category: method
116	    severity: info
117	    status: resolved
118	    first_raised_round: 0
119	    last_seen_round: 1
120	    action_items: []
121	    resolution: "Plug-in SE 明确承认为 limitation"
122	    resolution_round: 1
123	
124	  - id: "R1-V2-W4"
125	    summary: "Moderate regime 实用价值有限"
126	    category: experiment
127	    severity: info
128	    status: resolved
129	    first_raised_round: 0
130	    last_seen_round: 1
131	    action_items: []
132	    resolution: "三处一致阐述适用条件"
133	    resolution_round: 1
134	
135	  - id: "R1-V2-W5"
136	    summary: "Imai & Yamamoto 区分仅一句话"
137	    category: writing
138	    severity: info
139	    status: resolved
140	    first_raised_round: 0
141	    last_seen_round: 1
142	    action_items: []
143	    resolution: "三层区分已足够"
144	    resolution_round: 1
145	
146	  - id: "MED-W1"
147	    summary: "PPCI 互补性无实验证据"
148	    category: method
149	    severity: critical
150	    status: resolved
151	    first_raised_round: 0
152	    last_seen_round: 1
153	    action_items: []
154	    resolution: "4-DGP 正交设计验证"
155	    resolution_round: 1
156	
157	  - id: "MED-W2"
158	    summary: "诊断 AUC 仅在 Abstract"
159	    category: method
160	    severity: critical
161	    status: resolved
162	    first_raised_round: 0
163	    last_seen_round: 1
164	    action_items: []
165	    resolution: "Section 5.4 + Figure 3"
166	    resolution_round: 1
167	
168	  - id: "MED-W3"
169	    summary: "Theorem 1 缺 MC 验证"
170	    category: method
171	    severity: warning
172	    status: resolved
173	    first_raised_round: 0
174	    last_seen_round: 1
1
…[truncated 3337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-23T09:07:24.791012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "offset": "299",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "offset": "299",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-23T09:07:24.842116+00:00_

299	
300	  - id: "RD2-M2"
301	    summary: "sui2026ppci 作者名有误"
302	    category: writing
303	    severity: info
304	    status: resolved
305	    first_raised_round: 2
306	    last_seen_round: 3
307	    action_items: []
308	    resolution: "作者补全"
309	    resolution_round: 2
310	
311	  - id: "RD2-M3"
312	    summary: "术语不一致"
313	    category: writing
314	    severity: info
315	    status: resolved
316	    first_raised_round: 2
317	    last_seen_round: 3
318	    action_items: []
319	    resolution: "统一术语"
320	    resolution_round: 2
321	
322	  - id: "R2-W5"
323	    summary: "Abstract 仅报 AUC=0.83"
324	    category: framing
325	    severity: info
326	    status: wont_fix
327	    first_raised_round: 0
328	    last_seen_round: 3
329	    action_items: []
330	    resolution: "Δτ-free 修复已提升 setting AUC 至 0.889"
331	    resolution_round: 2
332	
333	  - id: "R1-RD1-W5"
334	    summary: "无正面 real-data evidence"
335	    category: experiment
336	    severity: critical
337	    status: resolved
338	    first_raised_round: 1
339	    last_seen_round: 5
340	    action_items: []
341	    resolution: "7 LLM × 2 datasets 验证。Civil Comments Δπ 确认写入论文。"
342	    resolution_round: 3
343	
344	  - id: "R2-RD1-W3"
345	    summary: "Multi-LLM 仅 OpenAI"
346	    category: experiment
347	    severity: info
348	    status: resolved
349	    first_raised_round: 1
350	    last_seen_round: 2
351	    action_items: []
352	    resolution: "4 个开源 LLM + 3 个闭源 LLM"
353	    resolution_round: 2
354	
355	  - id: "RD2-W4"
356	    summary: "κ>100 阈值无依据"
357	    category: method
358	    severity: info
359	    status: resolved
360	    first_raised_round: 2
361	    last_seen_round: 5
362	    action_items: []
363	    resolution: "κ sweep 经验验证"
364	    resolution_round: 2
365	
366	  - id: "RD2-M4"
367	    summary: "50 MC seeds vs 100"
368	    category: experiment
369	    severity: info
370	    status: resolved
371	    first_raised_round: 2
372	    last_seen_round: 3
373	    action_items: []
374	    resolution: "100-seed 验
…[truncated 6713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-23T09:07:34.730260+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"status: open\\|status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "description": "Find open/in-progress issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"status: open\\|status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "description": "Find open/in-progress issues"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-23T09:07:34.831125+00:00_

750:    status: open
788:    status: open
826:    status: open
841:    status: open
856:    status: open
871:    status: open
886:    status: open
901:    status: open
916:    status: open
950:    status: open
965:    status: open
980:    status: open
999:    status: open
1044:    status: open
1074:    status: open
1089:    status: open
1204:    status: open
1219:    status: open
1234:    status: open

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-23T09:07:38.897321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "offset": "740",
  "limit": "510"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "offset": "740",
    "limit": "510"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-23T09:07:38.998684+00:00_

740	    action_items: []
741	    resolution: "introduction.tex L10 脚注。位置从 Section 3 提前到 Section 1。"
742	    resolution_round: 6
743	
744	  # === OPEN ISSUES (updated with Round 12 mentions) ===
745	
746	  - id: "R2-W1"
747	    summary: "方法论新颖性有限"
748	    category: framing
749	    severity: warning
750	    status: open
751	    first_raised_round: 0
752	    last_seen_round: 12
753	    mentions:
754	      - round: 12
755	        reviewers: [1, 2]
756	        note: "第六次复发。R2-W1 标 warning：per-subgroup CM inversion + HB 是识别问题后的自然解。R1 完全同意。R1 rebut R2-N3（Theorem 1 framing）时论证了 δ_s·Δτ 乘积结构与 F-L 同质衰减的实质性区别，但同意 EC-HTE 方法本身新颖性有限。共识：论文主要贡献在 problem identification + bias identity，EC-HTE 是 natural fix。"
757	    action_items:
758	      - round: 10
759	        action: "考虑进一步弱化标题或 C2 定位，明确 EC-HTE 是 natural fix 而非 novel method"
760	        assigned_to: director
761	        status: pending
762	    resolution: ""
763	    resolution_round: null
764	
765	  - id: "R3F-M2"
766	    summary: "K>4 可扩展性未探索"
767	    category: experiment
768	    severity: info
769	    status: resolved
770	    first_raised_round: 3
771	    last_seen_round: 12
772	    mentions:
773	      - round: 12
774	        reviewers: [1, 2]
775	        note: "R1-W2 标 warning：K=8 RMSE=0.340 远超 Global=0.168。R2 交叉同意。论文在 Limitations 提及但主文未给数字。"
776	    action_items:
777	      - round: 12
778	        action: "experiments.tex 加 K=8 scalability boundary 句"
779	        assigned_to: agent
780	        status: done
781	    resolution: "主文 experiments.tex 加 K=8 边界条件句（coverage 95.6% but RMSE > Global）。Reviewer 验证 PASS。"
782	    resolution_round: 12
783	
784	  - id: "R5-N3"
785	    summary: "Plug-in SE 近似的覆盖率缺口未量化（CausalForest 93.8% vs 名义 95%）"
786	    category: method
787	    severity: warning
788	    status: open
789	    first_raised_round: 5
790	    last_seen_round: 12
791	    mentions:
792	      - round: 12
793	        reviewers: [1, 2]
794	        note: "R1-W3 标 warning。R2 rebut：1.2pp 在 100 MC 的 MC SE 范围内，论文 Appendix Y 已提供 bootstrap 替
…[truncated 15464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-23T09:11:57.170266+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "issues_yaml": "issues:\n  # === RESOLVED (prior rounds, unchanged) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"JOINT-F1\"\n    summary: \"Tightness ratio 数值不一致\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"精确恒等式使问题消解\"\n    resolution_round: 0\n\n  - id: \"R2-W4\"\n    summary: \"DSL 区分不充分\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Related Work + Appendix E 清晰技术区分 + DSL 等价性证明\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Causal Forest uncertainty propagation 不清楚\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Plug-in SE 明确承认为 limitation\"\n    resolution_round: 1\n\n  - id: \"R1-V2-W4\"\n    summary: \"Moderate regime 实用价值有限\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"三处一致阐述适用条件\"\n    resolution_round: 1\n\n  - id: \"R1-V2-W5\"\n    summary: \"Imai & Yamamoto 区分仅一句话\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"三层区分已足够\"\n    resolution_round: 1\n\n  - id: \"MED-W1\"\n    summary: \"PPCI 互补性无实验证据\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"4-DGP 正交设计验证\"\n    resolution_round: 1\n\n  - id: \"MED-W2\"\n    summary: \"诊断 AUC 仅在 Abstract\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Section 5.4 + Figure 3\"\n    resolution_round: 1\n\n  - id: \"MED-W3\"\n    summary: \"Theorem 1 缺 MC 验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"520 configs MC 验证\"\n    resolution_round: 1\n\n  - id: \"MED-W4\"\n    summary: \"论文无 Figure\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文 2 figures + 1 table\"\n    resolution_round: 1\n\n  - id: \"MED-W5\"\n    summary: \"无合成数据 regime sweep\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整合成 regime sweep\"\n    resolution_round: 1\n\n  - id: \"MED-W6\"\n    summary: \"Abstract 与 Table 1 数字不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"数字一致\"\n    resolution_round: 1\n\n  - id: \"MED-W7\"\n    summary: \"无 CausalForest 结果\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"CausalForest 在 Table 1\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"加法式 CATE 注入未讨论\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Limitations + exp-018 乘法 DGP\"\n    resolution_round: 2\n\n  - id: \"R1-RD1-W3\"\n    summary: \"100 MC runs 无 SE\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Table 1 footnote + Appendix MC SE\"\n    resolution_round: 2\n\n  - id: \"RD2-W2\"\n    summary: \"诊断 setting-level AUC=0.47 + 循环依赖\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Δτ-free 诊断，setting AUC 0.47→0.889\"\n    resolution_round: 2\n\n  - id: \"RD2-W3\"\n    summary: \"A2+A3 假设过强，放松分析不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"exp-019: R²≥0.976 across P(Z=1)∈[0.1,0.5]\"\n    resolution_round: 2\n\n  - id: \"RD2-W6\"\n    summary: \"贡献列表 5 项偏多\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"5→3 项\"\n    resolution_round: 2\n\n  - id: \"RD2-W1\"\n    summary: \"g(π̄) 未给闭合形式\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Corollary 1 footnote 给出 J=3 显式表达式\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"遗漏 Fong & Tyler (2021)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"已添加引用\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"sui2026ppci 作者名有误\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 3\n    action_items: []\n    resolution: \"作者补全\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"统一术语\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Abstract 仅报 AUC=0.83\"\n    category: framing\n    severity: info\n    status: wont_fix\n    first_raised_round: 0\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Δτ-free 修复已提升 setting AUC 至 0.889\"\n    resolution_round: 2\n\n  - id: \"R1-RD1-W5\"\n    summary: \"无正面 real-data evidence\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    action_items: []\n    resolution: \"7 LLM × 2 datasets 验证。Civil Comments Δπ 确认写入论文。\"\n    resolution_round: 3\n\n  - id: \"R2-RD1-W3\"\n    summary: \"Multi-LLM 仅 OpenAI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    action_items: []\n    resolution: \"4 个开源 LLM + 3 个闭源 LLM\"\n    resolution_round: 2\n\n  - id: \"RD2-W4\"\n    summary: \"κ>100 阈值无依据\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    action_items: []\n    resolution: \"κ sweep 经验验证\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"50 MC seeds vs 100\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"100-seed 验证稳定性\"\n    resolution_round: 2\n\n  - id: \"RD2-M5\"\n    summary: \"Gamma(3,1) 敏感性范围过窄\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Gamma(3,1) 2×扰动下 RMSE 变化 ≤4%\"\n    resolution_round: 2\n\n  - id: \"RD2-W5\"\n    summary: \"子群定义缺乏外部效度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Limitations 已补充 text-feature vs demographic subgroup 讨论 + EC-HTE agnostic to subgroup definition 声明\"\n    resolution_round: 3\n\n  - id: \"RD2-F1\"\n    summary: \"正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Conclusion 压缩，主文 ≤ 8 页。PDF 视觉确认 Conclusion 在 page 8 结束。\"\n    resolution_round: 4\n\n  - id: \"R3F-N1\"\n    summary: \"Appendix B 证明中间步骤代数错误（最终结果正确）\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"错误推导路径已删除。保留正确的 δ_s 代换验证路径。\"\n    resolution_round: 4\n\n  - id: \"R3F-N2\"\n    summary: \"Abstract 过度突出合成极端配置结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    action_items: []\n    resolution: \"Abstract 加 (K=2, extreme Δπ) 条件限定 + L7 conditionality 声明\"\n    resolution_round: 4\n\n  - id: \"R3F-W1\"\n    summary: \"主文未点明实验已联合违反 (A2)+(A3) 却仍有效\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"§5.5 明确声明联合假设违反下 coverage ≥0.93\"\n    resolution_round: 4\n\n  - id: \"R3F-W2\"\n    summary: \"遗漏因果推断中二元变量误分类的计量经济学文献\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Appendix 'Econometrics of binary misclassification' 段落\"\n    resolution_round: 4\n\n  - id: \"R3F-W3\"\n    summary: \"'50% of configurations' claim 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 9\n    action_items: []\n    resolution: \"Round 9：全部 5 处 50% claim 加 'across our parameter grid' 限定。\"\n    resolution_round: 9\n\n  - id: \"R3F-W4\"\n    summary: \"τ(z) 不依赖 S 的隐含假设未正式声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    action_items: []\n    resolution: \"(A5) 正式列出。L61 说明推广到 subgroup-specific Δτ_s。\"\n    resolution_round: 4\n\n  - id: \"R3F-W5\"\n    summary: \"部分 claims 统计显著性不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"§5.3 加 '(p=0.395 vs. Global, not statistically significant)' 标注\"\n    resolution_round: 4\n\n  - id: \"R3F-W6\"\n    summary: \"κ>100 singularity guard 阈值缺乏支撑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 6\n    action_items: []\n    resolution: \"method.tex 明确区分 κ>100 (numerical singularity guard) 与 κ≤1.25 (empirical applicability diagnostic)。\"\n    resolution_round: 6\n\n  - id: \"R3F-W7\"\n    summary: \"诊断 AUC=0.86 的 FP/FN 代价不对称未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Appendix 加 'Cost-asymmetric diagnostic thresholds' 段落\"\n    resolution_round: 4\n\n  - id: \"R3F-M1\"\n    summary: \"Section 3 缺直觉数值例子\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"页数极度紧张（8 页刚好）。Rebuttal 可补。\"\n    resolution_round: null\n\n  - id: \"R3F-M3\"\n    summary: \"Proposition 3 未推广到 asymmetric\"\n    category: method\n    severity: info\n    status: wont_fix\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Rebuttal 回应\"\n    resolution_round: null\n\n  - id: \"R5-N2\"\n    summary: \"Corollary (Appendix C) 多分类扩展 g(π̄) 仅对均匀 off-diagonal 成立但未标明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Corollary 声明加 'uniform off-diagonal misclassification' 限定。\"\n    resolution_round: 6\n\n  - id: \"R5-N4\"\n    summary: \"κ>100 singularity guard 与 Appendix R 证据存在~80倍差距\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"method.tex 明确区分两层阈值。\"\n    resolution_round: 6\n\n  - id: \"R5-W2\"\n    summary: \"Audinet de Pieuchon et al. (2025, EMNLP) 讨论严重不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 10\n    action_items: []\n    resolution: \"related_work.tex 已充分讨论 Audinet et al. (2025)。\"\n    resolution_round: 5\n\n  - id: \"R5-W4\"\n    summary: \"CausalForestDML 超参数未完整报告\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Appendix 加完整超参数。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Figure 5 (applicability frontier) 应从 Appendix 移入正文\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"页数限制，无法移入正文。已加 forward reference。\"\n    resolution_round: null\n\n  - id: \"R6-N1\"\n    summary: \"theory.tex 'four assumptions' 与实际列出的 (A1)-(A5) 不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    action_items: []\n    resolution: \"'four assumptions' → 'five assumptions'\"\n    resolution_round: 6\n\n  - id: \"R6-M1\"\n    summary: \"520 配置数无法从文档化 DGP 参数推导\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    action_items: []\n    resolution: \"DGP 参数完整文档化\"\n    resolution_round: 6\n\n  - id: \"R6-M2\"\n    summary: \"'debiasing' 术语歧义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    action_items: []\n    resolution: \"introduction.tex L10 脚注。位置从 Section 3 提前到 Section 1。\"\n    resolution_round: 6\n\n  # === OPEN ISSUES (updated with Round 13 mentions) ===\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性有限\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"第六次复发。R2-W1 标 warning：per-subgroup CM inversion + HB 是识别问题后的自然解。R1 完全同意。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-N2 标 critical：HB partial pooling 是 James-Stein shrinkage 直接应用，Dawid&Skene/Paun 更复杂。R1 rebut：评价框架 vs 组件。Director 裁定 should-fix：论文应更坦诚定位贡献为 problem identification + bias identity，EC-HTE 是 natural fix 而非 novel method。\"\n    action_items:\n      - round: 10\n        action: \"考虑进一步弱化标题或 C2 定位，明确 EC-HTE 是 natural fix 而非 novel method\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3F-M2\"\n    summary: \"K>4 可扩展性未探索\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W2 标 warning：K=8 RMSE=0.340 远超 Global=0.168。R2 交叉同意。论文在 Limitations 提及但主文未给数字。\"\n    action_items:\n      - round: 12\n        action: \"experiments.tex 加 K=8 scalability boundary 句\"\n        assigned_to: agent\n        status: done\n    resolution: \"主文 experiments.tex 加 K=8 边界条件句（coverage 95.6% but RMSE > Global）。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R5-N3\"\n    summary: \"Plug-in SE 近似的覆盖率缺口未量化（CausalForest 93.8% vs 名义 95%）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W3 标 warning。R2 rebut：1.2pp 在 100 MC 的 MC SE 范围内。共识降为 should-fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-N1 升级为 critical：指出 HB shrinkage 优势与 CI 不可靠性在同一 small n_expert regime 存在结构性矛盾。R2 完全同意。Bootstrap 仅验证 n_expert=200，关键的 n_expert<100 区间缺失。Director 确认为本轮唯一共识 must-fix。\"\n    action_items:\n      - round: 13\n        action: \"提供 n_expert∈{25,50,75} 下 bootstrap coverage 数据（含 per-subgroup breakdown）\"\n        assigned_to: director\n        status: pending\n      - round: 13\n        action: \"正文 Section 4.3 明确标注 plug-in SE valid regime（n_expert≥100）\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W1\"\n    summary: \"Semi-synthetic TweetEval 中 EC-HTE 未优于 Global，但 Abstract/Intro 叙事以正面结果为主\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Table 1 caption 强化。Reviewer 验证 PASS。\"\n    action_items: []\n    resolution: \"Table 1 caption 强化（零空间约束下最优方案）。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R5-W3\"\n    summary: \"缺乏完全真实因果数据验证——所有 CATE 为合成注入\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"共识方向：should-fix（Limitations 加强讨论），非 must-fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-N2 标 critical，R2 同意但建议降级 should-fix（因果推断文献普遍挑战）。R2 建议在 Hate Speech case study 用 held-out expert labels 构建 pseudo ground-truth CATE。Director 裁定 should-fix。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W5\"\n    summary: \"(A5) 违反仅做有限测试——Appendix O 仅 1 模型、K=2、50 MC runs\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 单独提及。论文 Appendix Z.1 有 aligned/adversarial 两种 A5 违反设置。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W3\"\n    summary: \"合成 DGP 中 equal subgroup weights (w_s=1/K) 可能高估 EC-HTE 优势\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。TweetEval 使用不均衡子群（38%/38%/12%/12%），部分覆盖。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W4\"\n    summary: \"EC-HTE vs Stratified MLE bias 增量仅 0.002\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"Corollary 1 证明不完整——h(j,j') 未推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被提及。Appendix C 有 uniform off-diagonal 下的推导。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-M2\"\n    summary: \"可补充 Wang et al. (2020) PNAS 和 Yadlowsky et al. (2024)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被提及。Wang et al. (2020) 已在 related_work.tex 引用。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W1\"\n    summary: \"正文缺少 EC-HTE 不适用场景的决策树/流程图\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W2\"\n    summary: \"Assumption (A2) 对称误差在实际 LLM 标注中普遍不成立，正文讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"A2 假设后加括注明确仅影响诊断。Reviewer 验证 PASS。\"\n    action_items: []\n    resolution: \"A2 假设后加括注明确仅影响诊断。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R9-W3\"\n    summary: \"有限样本余项 R_n = O_p(n^{-1/2}·κ) 未给推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被提及。Appendix Y L1063-1065 已有 matrix perturbation 推导。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-N1\"\n    summary: \"(A1) 条件独立性假设不可检验且敏感性分析范围有限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [2]\n        note: \"R2-Q4 问 γ∈[0,0.2] 是否覆盖实际 LLM 标注的 outcome-dependence 幅度。缺乏 empirical calibration。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W1\"\n    summary: \"与 Frazis-Loewenstein (2003) 的公式级区分缺失\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"共识：应在 Section 2-3 加公式级对比但不构成 must-fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-N1 标 critical：与 Carroll et al. (2006)/Fuller (1987) 的区分不充分。R1 rebut：Theorem 1 的 δ_s·Δτ 乘积分解在 Carroll 框架无对应物。两者共识：增加数学对比 Remark 即可。Director 裁定 should-fix。\"\n    action_items:\n      - round: 13\n        action: \"Section 3 增加 Remark 对比 Carroll et al. attenuation formula 与 Theorem 1 structured decomposition\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单（Y = τ(Z)·T + ε），无混杂变量\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 10\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。Appendix Z.3 有 confounded DGP 实验。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-MR1\"\n    summary: \"遗漏 Dorn, Guo, and Kallus (2022) 和 Lash, Fox, Fink (2009)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 12\n    action_items: []\n    resolution: \"theory.tex L76 已引用。\"\n    resolution_round: 12\n\n  - id: \"R11-F1\"\n    summary: \"正文超出 8 页限制\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [2]\n        note: \"R2 格式合规检查：正文 ≤ 8 页 ✓。视觉审查确认。\"\n    action_items: []\n    resolution: \"正文收在 8 页内。视觉审查和 R2 格式检查均确认合规。\"\n    resolution_round: 12\n\n  - id: \"R11-W1\"\n    summary: \"(A3) P(Z=1)=0.5 等概率假设限制泛化性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1]\n        note: \"R1-W1 提出但 R2 rebut（Appendix R 已验证 P(Z=1)∈{0.1-0.5} 下 R²≥0.976）。Director 接受 R2 rebut，A3 为 expositional convenience 非 structural limitation。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W2\"\n    summary: \"κ>100 奇异性保护阈值无消融实验支撑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1]\n        note: \"R1-W4 提出。R2 rebut：Appendix A sweep 显示阈值从未在正常配置触发。Director 接受 R2 rebut。\"\n    action_items: []\n    resolution: \"Appendix A κ sweep 消融完成。R2 rebut 充分。\"\n    resolution_round: 13\n\n  - id: \"R11-W3\"\n    summary: \"'estimator-agnostic' 措辞过强——仅验证 3 种估计器\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被提及。措辞已改为 'compatible with a range of CATE estimators'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W4\"\n    summary: \"Theorem/Proposition/Remark 编号混用共享计数器\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-N1\"\n    summary: \"Abstract 对 Diagnostic AUC 选择性报告——仅报合成 0.86 未报真实 LLM 0.63\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    action_items: []\n    resolution: \"Abstract/Intro 三处修复。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R12-W1\"\n    summary: \"Expert label 获取成本的 cost-benefit 分析缺失\"\n    category: writing\n    severity: warning\n    status: wont_fix\n    first_raised_round: 12\n    last_seen_round: 12\n    action_items: []\n    resolution: \"已有覆盖。Rebuttal 项。\"\n    resolution_round: null\n\n  - id: \"R12-W2\"\n    summary: \"Algorithm 1 Step 2-3 'corrected labels' vs 'corrected moments' 歧义\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    action_items: []\n    resolution: \"Algorithm 1 术语统一为 'corrected outcome moments'。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R12-W3\"\n    summary: \"Abstract 信息密度过高，对非因果推断 NLP 读者不友好\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W2 标 warning，R1 交叉 AGREE。~250 词内塞入过多数字，核心 message 被稀释。建议精简到 3-4 个关键数字。\"\n    action_items:\n      - round: 13\n        action: \"精简 Abstract 数字到 3-4 个关键值，其余移至 Intro/Results\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M1\"\n    summary: \"Abstract '11 real LLM confusion matrices' vs Appendix 16 个组合数字不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 声称 Theorem 1 'does not require (A2)' 但 Theorem 1 假设列表含 (A1)-(A5)——表面矛盾\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M3\"\n    summary: \"Section 4.1 '21 of 24 configurations' 无上下文——24 的定义需翻到 Appendix\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 13 NEW ISSUES ===\n\n  - id: \"R13-W1\"\n    summary: \"Subgroup 选择指导缺失——EC-HTE 要求预定义 S:X→{1,...,K} 但无 data-driven discovery 方案\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W2 + R2-W4 独立提出，交叉完全同意。论文要求用户预定义 subgroup，但未讨论 subgroup misspecification 后果或选择指导。与 CausalForest 自动发现异质性相比是显著实用性差距。Proposition 3 的 diagnostic 可反向用于 subgroup selection（R1-Q3、R2 交叉同意）但论文未讨论。\"\n    action_items:\n      - round: 13\n        action: \"Limitations 或 Discussion 补充 subgroup selection guidance\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W2\"\n    summary: \"'Exact identity' 强调过度——真正优势是 structured decomposition 而非 exactness\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W3 提出，R1 交叉 AGREE。Frazis & Loewenstein (2003) 的 scalar attenuation 也是 exact。论文多处强调 'exact identity, not a bound' 但真正新颖性在于 δ_s × Δτ 的结构化分解。建议将措辞重心转移。\"\n    action_items:\n      - round: 13\n        action: \"将 'exact identity (not a bound)' 改为 'structured bias decomposition identity'\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W3\"\n    summary: \"遗漏 LLM annotation variance 文献——Mellon et al. (2025)、Bauer et al. (2024)、Calvi et al. (2015)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W1 提出，R1 交叉 AGREE。Mellon et al. 识别 5 类 variance sources、Bauer et al. 研究 LLM annotation ME reduction，与本文动机直接相关。Calvi et al. 研究 HTE with mismeasured treatment。\"\n    action_items:\n      - round: 13\n        action: \"Section 2 补充引用讨论\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W4\"\n    summary: \"Continuous effect modifiers 未讨论——论文全程假设 Z 为 discrete\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2 未提及局限 (b) 提出，R1 交叉 AGREE。confusion matrix 框架对 continuous Z 不直接适用。Limitations 未提及。\"\n    action_items:\n      - round: 13\n        action: \"Limitations 补充 continuous effect modifier 限制\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"Corollary 4 多分类扩展 (J>2) 无实验验证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2 未提及局限 (c) 提出，R1 交叉 AGREE。所有实验 J=2（binary Z）。K=4 是 4 个 subgroups 不是 4 个 class。至少应有 J=3 的 sanity check。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M1\"\n    summary: \"Table 1 'Bias' 列未明确标注为 |bias|（绝对值）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-M2 + R2-M3 独立提出，均 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M2\"\n    summary: \"Table 1 'Cov.' 列标签应明确为 '95% CI Coverage'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-M3 + R2-M3 独立提出，均 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M3\"\n    summary: \"Figure 1 panel 标注缺少具体 error rate 数值（π̄ 和 π_s）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [2]\n        note: \"R2-M2 提出。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M4\"\n    summary: \"Törnberg (2025) bib 年份需核实——可能应为 2024\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [2]\n        note: \"R2-M5 提出。R1 未能确认，需作者核实。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M5\"\n    summary: \"PPCI 组合的 'orthogonality' 应改为更谨慎的 'complementarity'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W3 提出。R2 rebut 经验证据充分但同意理论保证缺失。建议改术语。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "issues_yaml": "issues:\n  # === RESOLVED (prior rounds, unchanged) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"JOINT-F1\"\n    summary: \"Tightness ratio 数值不一致\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"精确恒等式使问题消解\"\n    resolution_round: 0\n\n  - id: \"R2-W4\"\n    summary: \"DSL 区分不充分\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Related Work + Appendix E 清晰技术区分 + DSL 等价性证明\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Causal Forest uncertainty propagation 不清楚\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Plug-in SE 明确承认为 limitation\"\n    resolution_round: 1\n\n  - id: \"R1-V2-W4\"\n    summary: \"Moderate regime 实用价值有限\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"三处一致阐述适用条件\"\n    resolution_round: 1\n\n  - id: \"R1-V2-W5\"\n    summary: \"Imai & Yamamoto 区分仅一句话\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"三层区分已足够\"\n    resolution_round: 1\n\n  - id: \"MED-W1\"\n    summary: \"PPCI 互补性无实验证据\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"4-DGP 正交设计验证\"\n    resolution_round: 1\n\n  - id: \"MED-W2\"\n    summary: \"诊断 AUC 仅在 Abstract\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Section 5.4 + Figure 3\"\n    resolution_round: 1\n\n  - id: \"MED-W3\"\n    summary: \"Theorem 1 缺 MC 验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"520 configs MC 验证\"\n    resolution_round: 1\n\n  - id: \"MED-W4\"\n    summary: \"论文无 Figure\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文 2 figures + 1 table\"\n    resolution_round: 1\n\n  - id: \"MED-W5\"\n    summary: \"无合成数据 regime sweep\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整合成 regime sweep\"\n    resolution_round: 1\n\n  - id: \"MED-W6\"\n    summary: \"Abstract 与 Table 1 数字不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"数字一致\"\n    resolution_round: 1\n\n  - id: \"MED-W7\"\n    summary: \"无 CausalForest 结果\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"CausalForest 在 Table 1\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"加法式 CATE 注入未讨论\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Limitations + exp-018 乘法 DGP\"\n    resolution_round: 2\n\n  - id: \"R1-RD1-W3\"\n    summary: \"100 MC runs 无 SE\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Table 1 footnote + Appendix MC SE\"\n    resolution_round: 2\n\n  - id: \"RD2-W2\"\n    summary: \"诊断 setting-level AUC=0.47 + 循环依赖\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Δτ-free 诊断，setting AUC 0.47→0.889\"\n    resolution_round: 2\n\n  - id: \"RD2-W3\"\n    summary: \"A2+A3 假设过强，放松分析不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"exp-019: R²≥0.976 across P(Z=1)∈[0.1,0.5]\"\n    resolution_round: 2\n\n  - id: \"RD2-W6\"\n    summary: \"贡献列表 5 项偏多\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"5→3 项\"\n    resolution_round: 2\n\n  - id: \"RD2-W1\"\n    summary: \"g(π̄) 未给闭合形式\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Corollary 1 footnote 给出 J=3 显式表达式\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"遗漏 Fong & Tyler (2021)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"已添加引用\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"sui2026ppci 作者名有误\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 3\n    action_items: []\n    resolution: \"作者补全\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"统一术语\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Abstract 仅报 AUC=0.83\"\n    category: framing\n    severity: info\n    status: wont_fix\n    first_raised_round: 0\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Δτ-free 修复已提升 setting AUC 至 0.889\"\n    resolution_round: 2\n\n  - id: \"R1-RD1-W5\"\n    summary: \"无正面 real-data evidence\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    action_items: []\n    resolution: \"7 LLM × 2 datasets 验证。Civil Comments Δπ 确认写入论文。\"\n    resolution_round: 3\n\n  - id: \"R2-RD1-W3\"\n    summary: \"Multi-LLM 仅 OpenAI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    action_items: []\n    resolution: \"4 个开源 LLM + 3 个闭源 LLM\"\n    resolution_round: 2\n\n  - id: \"RD2-W4\"\n    summary: \"κ>100 阈值无依据\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    action_items: []\n    resolution: \"κ sweep 经验验证\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"50 MC seeds vs 100\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"100-seed 验证稳定性\"\n    resolution_round: 2\n\n  - id: \"RD2-M5\"\n    summary: \"Gamma(3,1) 敏感性范围过窄\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 3\n    action_items: []\n    resolution: \"Gamma(3,1) 2×扰动下 RMSE 变化 ≤4%\"\n    resolution_round: 2\n\n  - id: \"RD2-W5\"\n    summary: \"子群定义缺乏外部效度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Limitations 已补充 text-feature vs demographic subgroup 讨论 + EC-HTE agnostic to subgroup definition 声明\"\n    resolution_round: 3\n\n  - id: \"RD2-F1\"\n    summary: \"正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Conclusion 压缩，主文 ≤ 8 页。PDF 视觉确认 Conclusion 在 page 8 结束。\"\n    resolution_round: 4\n\n  - id: \"R3F-N1\"\n    summary: \"Appendix B 证明中间步骤代数错误（最终结果正确）\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"错误推导路径已删除。保留正确的 δ_s 代换验证路径。\"\n    resolution_round: 4\n\n  - id: \"R3F-N2\"\n    summary: \"Abstract 过度突出合成极端配置结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    action_items: []\n    resolution: \"Abstract 加 (K=2, extreme Δπ) 条件限定 + L7 conditionality 声明\"\n    resolution_round: 4\n\n  - id: \"R3F-W1\"\n    summary: \"主文未点明实验已联合违反 (A2)+(A3) 却仍有效\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"§5.5 明确声明联合假设违反下 coverage ≥0.93\"\n    resolution_round: 4\n\n  - id: \"R3F-W2\"\n    summary: \"遗漏因果推断中二元变量误分类的计量经济学文献\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Appendix 'Econometrics of binary misclassification' 段落\"\n    resolution_round: 4\n\n  - id: \"R3F-W3\"\n    summary: \"'50% of configurations' claim 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 9\n    action_items: []\n    resolution: \"Round 9：全部 5 处 50% claim 加 'across our parameter grid' 限定。\"\n    resolution_round: 9\n\n  - id: \"R3F-W4\"\n    summary: \"τ(z) 不依赖 S 的隐含假设未正式声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    action_items: []\n    resolution: \"(A5) 正式列出。L61 说明推广到 subgroup-specific Δτ_s。\"\n    resolution_round: 4\n\n  - id: \"R3F-W5\"\n    summary: \"部分 claims 统计显著性不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"§5.3 加 '(p=0.395 vs. Global, not statistically significant)' 标注\"\n    resolution_round: 4\n\n  - id: \"R3F-W6\"\n    summary: \"κ>100 singularity guard 阈值缺乏支撑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 6\n    action_items: []\n    resolution: \"method.tex 明确区分 κ>100 (numerical singularity guard) 与 κ≤1.25 (empirical applicability diagnostic)。\"\n    resolution_round: 6\n\n  - id: \"R3F-W7\"\n    summary: \"诊断 AUC=0.86 的 FP/FN 代价不对称未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Appendix 加 'Cost-asymmetric diagnostic thresholds' 段落\"\n    resolution_round: 4\n\n  - id: \"R3F-M1\"\n    summary: \"Section 3 缺直觉数值例子\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"页数极度紧张（8 页刚好）。Rebuttal 可补。\"\n    resolution_round: null\n\n  - id: \"R3F-M3\"\n    summary: \"Proposition 3 未推广到 asymmetric\"\n    category: method\n    severity: info\n    status: wont_fix\n    first_raised_round: 3\n    last_seen_round: 4\n    action_items: []\n    resolution: \"Rebuttal 回应\"\n    resolution_round: null\n\n  - id: \"R5-N2\"\n    summary: \"Corollary (Appendix C) 多分类扩展 g(π̄) 仅对均匀 off-diagonal 成立但未标明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Corollary 声明加 'uniform off-diagonal misclassification' 限定。\"\n    resolution_round: 6\n\n  - id: \"R5-N4\"\n    summary: \"κ>100 singularity guard 与 Appendix R 证据存在~80倍差距\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"method.tex 明确区分两层阈值。\"\n    resolution_round: 6\n\n  - id: \"R5-W2\"\n    summary: \"Audinet de Pieuchon et al. (2025, EMNLP) 讨论严重不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 10\n    action_items: []\n    resolution: \"related_work.tex 已充分讨论 Audinet et al. (2025)。\"\n    resolution_round: 5\n\n  - id: \"R5-W4\"\n    summary: \"CausalForestDML 超参数未完整报告\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"Appendix 加完整超参数。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Figure 5 (applicability frontier) 应从 Appendix 移入正文\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 6\n    action_items: []\n    resolution: \"页数限制，无法移入正文。已加 forward reference。\"\n    resolution_round: null\n\n  - id: \"R6-N1\"\n    summary: \"theory.tex 'four assumptions' 与实际列出的 (A1)-(A5) 不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    action_items: []\n    resolution: \"'four assumptions' → 'five assumptions'\"\n    resolution_round: 6\n\n  - id: \"R6-M1\"\n    summary: \"520 配置数无法从文档化 DGP 参数推导\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    action_items: []\n    resolution: \"DGP 参数完整文档化\"\n    resolution_round: 6\n\n  - id: \"R6-M2\"\n    summary: \"'debiasing' 术语歧义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    action_items: []\n    resolution: \"introduction.tex L10 脚注。位置从 Section 3 提前到 Section 1。\"\n    resolution_round: 6\n\n  # === OPEN ISSUES (updated with Round 13 mentions) ===\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性有限\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"第六次复发。R2-W1 标 warning：per-subgroup CM inversion + HB 是识别问题后的自然解。R1 完全同意。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-N2 标 critical：HB partial pooling 是 James-Stein shrinkage 直接应用，Dawid&Skene/Paun 更复杂。R1 rebut：评价框架 vs 组件。Director 裁定 should-fix：论文应更坦诚定位贡献为 problem identification + bias identity，EC-HTE 是 natural fix 而非 novel method。\"\n    action_items:\n      - round: 10\n        action: \"考虑进一步弱化标题或 C2 定位，明确 EC-HTE 是 natural fix 而非 novel method\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3F-M2\"\n    summary: \"K>4 可扩展性未探索\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W2 标 warning：K=8 RMSE=0.340 远超 Global=0.168。R2 交叉同意。论文在 Limitations 提及但主文未给数字。\"\n    action_items:\n      - round: 12\n        action: \"experiments.tex 加 K=8 scalability boundary 句\"\n        assigned_to: agent\n        status: done\n    resolution: \"主文 experiments.tex 加 K=8 边界条件句（coverage 95.6% but RMSE > Global）。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R5-N3\"\n    summary: \"Plug-in SE 近似的覆盖率缺口未量化（CausalForest 93.8% vs 名义 95%）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W3 标 warning。R2 rebut：1.2pp 在 100 MC 的 MC SE 范围内。共识降为 should-fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-N1 升级为 critical：指出 HB shrinkage 优势与 CI 不可靠性在同一 small n_expert regime 存在结构性矛盾。R2 完全同意。Bootstrap 仅验证 n_expert=200，关键的 n_expert<100 区间缺失。Director 确认为本轮唯一共识 must-fix。\"\n    action_items:\n      - round: 13\n        action: \"提供 n_expert∈{25,50,75} 下 bootstrap coverage 数据（含 per-subgroup breakdown）\"\n        assigned_to: director\n        status: pending\n      - round: 13\n        action: \"正文 Section 4.3 明确标注 plug-in SE valid regime（n_expert≥100）\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W1\"\n    summary: \"Semi-synthetic TweetEval 中 EC-HTE 未优于 Global，但 Abstract/Intro 叙事以正面结果为主\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Table 1 caption 强化。Reviewer 验证 PASS。\"\n    action_items: []\n    resolution: \"Table 1 caption 强化（零空间约束下最优方案）。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R5-W3\"\n    summary: \"缺乏完全真实因果数据验证——所有 CATE 为合成注入\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"共识方向：should-fix（Limitations 加强讨论），非 must-fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-N2 标 critical，R2 同意但建议降级 should-fix（因果推断文献普遍挑战）。R2 建议在 Hate Speech case study 用 held-out expert labels 构建 pseudo ground-truth CATE。Director 裁定 should-fix。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W5\"\n    summary: \"(A5) 违反仅做有限测试——Appendix O 仅 1 模型、K=2、50 MC runs\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 单独提及。论文 Appendix Z.1 有 aligned/adversarial 两种 A5 违反设置。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W3\"\n    summary: \"合成 DGP 中 equal subgroup weights (w_s=1/K) 可能高估 EC-HTE 优势\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。TweetEval 使用不均衡子群（38%/38%/12%/12%），部分覆盖。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W4\"\n    summary: \"EC-HTE vs Stratified MLE bias 增量仅 0.002\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"Corollary 1 证明不完整——h(j,j') 未推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被提及。Appendix C 有 uniform off-diagonal 下的推导。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-M2\"\n    summary: \"可补充 Wang et al. (2020) PNAS 和 Yadlowsky et al. (2024)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被提及。Wang et al. (2020) 已在 related_work.tex 引用。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W1\"\n    summary: \"正文缺少 EC-HTE 不适用场景的决策树/流程图\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W2\"\n    summary: \"Assumption (A2) 对称误差在实际 LLM 标注中普遍不成立，正文讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"A2 假设后加括注明确仅影响诊断。Reviewer 验证 PASS。\"\n    action_items: []\n    resolution: \"A2 假设后加括注明确仅影响诊断。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R9-W3\"\n    summary: \"有限样本余项 R_n = O_p(n^{-1/2}·κ) 未给推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被提及。Appendix Y L1063-1065 已有 matrix perturbation 推导。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-N1\"\n    summary: \"(A1) 条件独立性假设不可检验且敏感性分析范围有限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [2]\n        note: \"R2-Q4 问 γ∈[0,0.2] 是否覆盖实际 LLM 标注的 outcome-dependence 幅度。缺乏 empirical calibration。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W1\"\n    summary: \"与 Frazis-Loewenstein (2003) 的公式级区分缺失\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"共识：应在 Section 2-3 加公式级对比但不构成 must-fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-N1 标 critical：与 Carroll et al. (2006)/Fuller (1987) 的区分不充分。R1 rebut：Theorem 1 的 δ_s·Δτ 乘积分解在 Carroll 框架无对应物。两者共识：增加数学对比 Remark 即可。Director 裁定 should-fix。\"\n    action_items:\n      - round: 13\n        action: \"Section 3 增加 Remark 对比 Carroll et al. attenuation formula 与 Theorem 1 structured decomposition\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单（Y = τ(Z)·T + ε），无混杂变量\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 10\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。Appendix Z.3 有 confounded DGP 实验。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-MR1\"\n    summary: \"遗漏 Dorn, Guo, and Kallus (2022) 和 Lash, Fox, Fink (2009)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 12\n    action_items: []\n    resolution: \"theory.tex L76 已引用。\"\n    resolution_round: 12\n\n  - id: \"R11-F1\"\n    summary: \"正文超出 8 页限制\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [2]\n        note: \"R2 格式合规检查：正文 ≤ 8 页 ✓。视觉审查确认。\"\n    action_items: []\n    resolution: \"正文收在 8 页内。视觉审查和 R2 格式检查均确认合规。\"\n    resolution_round: 12\n\n  - id: \"R11-W1\"\n    summary: \"(A3) P(Z=1)=0.5 等概率假设限制泛化性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1]\n        note: \"R1-W1 提出但 R2 rebut（Appendix R 已验证 P(Z=1)∈{0.1-0.5} 下 R²≥0.976）。Director 接受 R2 rebut，A3 为 expositional convenience 非 structural limitation。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W2\"\n    summary: \"κ>100 奇异性保护阈值无消融实验支撑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1]\n        note: \"R1-W4 提出。R2 rebut：Appendix A sweep 显示阈值从未在正常配置触发。Director 接受 R2 rebut。\"\n    action_items: []\n    resolution: \"Appendix A κ sweep 消融完成。R2 rebut 充分。\"\n    resolution_round: 13\n\n  - id: \"R11-W3\"\n    summary: \"'estimator-agnostic' 措辞过强——仅验证 3 种估计器\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被提及。措辞已改为 'compatible with a range of CATE estimators'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W4\"\n    summary: \"Theorem/Proposition/Remark 编号混用共享计数器\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-N1\"\n    summary: \"Abstract 对 Diagnostic AUC 选择性报告——仅报合成 0.86 未报真实 LLM 0.63\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    action_items: []\n    resolution: \"Abstract/Intro 三处修复。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R12-W1\"\n    summary: \"Expert label 获取成本的 cost-benefit 分析缺失\"\n    category: writing\n    severity: warning\n    status: wont_fix\n    first_raised_round: 12\n    last_seen_round: 12\n    action_items: []\n    resolution: \"已有覆盖。Rebuttal 项。\"\n    resolution_round: null\n\n  - id: \"R12-W2\"\n    summary: \"Algorithm 1 Step 2-3 'corrected labels' vs 'corrected moments' 歧义\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    action_items: []\n    resolution: \"Algorithm 1 术语统一为 'corrected outcome moments'。Reviewer 验证 PASS。\"\n    resolution_round: 12\n\n  - id: \"R12-W3\"\n    summary: \"Abstract 信息密度过高，对非因果推断 NLP 读者不友好\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W2 标 warning，R1 交叉 AGREE。~250 词内塞入过多数字，核心 message 被稀释。建议精简到 3-4 个关键数字。\"\n    action_items:\n      - round: 13\n        action: \"精简 Abstract 数字到 3-4 个关键值，其余移至 Intro/Results\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M1\"\n    summary: \"Abstract '11 real LLM confusion matrices' vs Appendix 16 个组合数字不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 声称 Theorem 1 'does not require (A2)' 但 Theorem 1 假设列表含 (A1)-(A5)——表面矛盾\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M3\"\n    summary: \"Section 4.1 '21 of 24 configurations' 无上下文——24 的定义需翻到 Appendix\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"本轮未被直接提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 13 NEW ISSUES ===\n\n  - id: \"R13-W1\"\n    summary: \"Subgroup 选择指导缺失——EC-HTE 要求预定义 S:X→{1,...,K} 但无 data-driven discovery 方案\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W2 + R2-W4 独立提出，交叉完全同意。论文要求用户预定义 subgroup，但未讨论 subgroup misspecification 后果或选择指导。与 CausalForest 自动发现异质性相比是显著实用性差距。Proposition 3 的 diagnostic 可反向用于 subgroup selection（R1-Q3、R2 交叉同意）但论文未讨论。\"\n    action_items:\n      - round: 13\n        action: \"Limitations 或 Discussion 补充 subgroup selection guidance\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W2\"\n    summary: \"'Exact identity' 强调过度——真正优势是 structured decomposition 而非 exactness\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W3 提出，R1 交叉 AGREE。Frazis & Loewenstein (2003) 的 scalar attenuation 也是 exact。论文多处强调 'exact identity, not a bound' 但真正新颖性在于 δ_s × Δτ 的结构化分解。建议将措辞重心转移。\"\n    action_items:\n      - round: 13\n        action: \"将 'exact identity (not a bound)' 改为 'structured bias decomposition identity'\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W3\"\n    summary: \"遗漏 LLM annotation variance 文献——Mellon et al. (2025)、Bauer et al. (2024)、Calvi et al. (2015)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W1 提出，R1 交叉 AGREE。Mellon et al. 识别 5 类 variance sources、Bauer et al. 研究 LLM annotation ME reduction，与本文动机直接相关。Calvi et al. 研究 HTE with mismeasured treatment。\"\n    action_items:\n      - round: 13\n        action: \"Section 2 补充引用讨论\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W4\"\n    summary: \"Continuous effect modifiers 未讨论——论文全程假设 Z 为 discrete\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2 未提及局限 (b) 提出，R1 交叉 AGREE。confusion matrix 框架对 continuous Z 不直接适用。Limitations 未提及。\"\n    action_items:\n      - round: 13\n        action: \"Limitations 补充 continuous effect modifier 限制\"\n        assigned_to: director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"Corollary 4 多分类扩展 (J>2) 无实验验证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2 未提及局限 (c) 提出，R1 交叉 AGREE。所有实验 J=2（binary Z）。K=4 是 4 个 subgroups 不是 4 个 class。至少应有 J=3 的 sanity check。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M1\"\n    summary: \"Table 1 'Bias' 列未明确标注为 |bias|（绝对值）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-M2 + R2-M3 独立提出，均 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M2\"\n    summary: \"Table 1 'Cov.' 列标签应明确为 '95% CI Coverage'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-M3 + R2-M3 独立提出，均 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M3\"\n    summary: \"Figure 1 panel 标注缺少具体 error rate 数值（π̄ 和 π_s）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [2]\n        note: \"R2-M2 提出。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M4\"\n    summary: \"Törnberg (2025) bib 年份需核实——可能应为 2024\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [2]\n        note: \"R2-M5 提出。R1 未能确认，需作者核实。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M5\"\n    summary: \"PPCI 组合的 'orthogonality' 应改为更谨慎的 'complementarity'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W3 提出。R2 rebut 经验证据充分但同意理论保证缺失。建议改术语。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-23T09:11:57.271749+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml\", \"bytes\": 32077}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-23T09:14:20.289907+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: \"Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审稿模式**: Fresh（初审，2 Reviewers × 1 轮 + 交叉分享）\n\n---\n\n## Summary\n\n本文研究 LLM 标注作为 effect modifier 用于异质性处理效应（HTE）分析时，subgroup-heterogeneous misclassification 对 CATE 估计引入的 bias。核心贡献：(1) Bias Decomposition Identity（Theorem 1）——精确恒等式将 correction-induced bias 分解为 δ_s · Δτ / (1−2π̄) 的乘积形式；(2) EC-HTE——基于 hierarchical Bayesian subgroup-stratified confusion matrix 的纠偏框架；(3) Δτ-free diagnostic（Proposition 3）——仅需 per-subgroup error rates 即可判断 global correction 是否有害；(4) EC-HTE+PPCI 组合处理 covariate+outcome 双重误差。实验覆盖 520 synthetic configurations、semi-synthetic TweetEval、Hate Speech real-data case study、8 LLMs（6 proprietary + 4 open-source）。\n\n---\n\n## Strengths\n\n**S1. 问题识别的实际价值与非直觉性。** 论文揭示了一个重要的失败模式：当 LLM 误分类率跨 subgroup 异质时，标准 global confusion-matrix correction 在 50% 的 K=2 配置中恶化 CATE 估计（Section 5.2）。\"debiasing can be worse than doing nothing\" 的发现对 CSS 实践者有直接警示意义。[两位 Reviewer 一致认可]\n\n**S2. Theorem 1 的理论贡献干净且有独立价值。** bias = δ_s · Δτ · amplification factor 的乘积分解结构直观地揭示了 misclassification heterogeneity 与 treatment effect heterogeneity 的交互作用。证明（Appendix B）完整可验证，R² > 0.994 (K=2) 和 R² > 0.974 (K=4) 的经验验证覆盖 520 synthetic configurations + 11 real LLM confusion matrices。[两位 Reviewer 一致认可，Soundness 评 4/5]\n\n**S3. 实验设计系统全面。** 520 configurations 参数网格、100 MC runs + MC SE 报告、semi-synthetic TweetEval（真实文本特征 + 合成 CATE）、multi-LLM 一致性验证（Spearman ρ ≥ 0.82）、21 个 Appendix 覆盖主要 assumption violation 场景。实验规模在同类论文中属上乘。[两位 Reviewer 一致认可]\n\n**S4. Diagnostic 工具的实用性。** Proposition 3 的 Δτ-free diagnostic 打破了 \"要诊断需要先知道答案\" 的循环依赖，AUC = 0.86 at subgroup level。独立于 EC-HTE 可使用，为实践者提供低成本 screening tool。[两位 Reviewer 一致认可]\n\n**S5. 完整的实践指南。** Algorithm 1 伪代码可直接实现，expert budget crossover curves（Appendix I-J）、diagnostic threshold guidance（Section 5.4）构成完整 workflow。[两位 Reviewer 一致认可]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-MF1. [CONSENSUS] Plug-in SE 与方法优势的 regime 矛盾**\n- **来源**: R1-N1（critical），R2 交叉完全 [AGREE]\n- **问题**: EC-HTE 的 HB shrinkage 在低 expert budget（n_expert < 100）时提供最大的点估计优势（Table 3, K=2 n=25: HB RMSE 0.256 vs MLE 0.269），但恰好在这个 regime 下 plug-in SE（Eq. 5）不传播 confusion matrix estimation uncertainty，CI coverage 不可靠。Appendix Y 的 bootstrap 修复仅验证 n_expert=200（coverage 93.8%→95.0%），**未覆盖 n_expert < 100 的关键区间**。方法的核心卖点与其已知缺陷在同一参数区间内存在结构性矛盾。\n- **影响**: 实践者在最需要 EC-HTE 的场景下无法信赖其置信区间。\n- **修改方向**: (a) 提供 n_expert ∈ {25, 50, 75} 下 bootstrap coverage（含 per-subgroup breakdown）；(b) 正文 Section 4.3 明确标注 plug-in SE valid regime；(c) 如 bootstrap 在小 n 下也不恢复 nominal coverage，诚实讨论。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W-SF1. [DIVERGENT → Director 裁定 should-fix] 与经典测量误差文献的区分不够锐利**\n- **来源**: R2-N1（critical），R1 [REBUT] 降级\n- **分歧**: R2 认为 \"misspecified correction amplifies MSE\" 在 Carroll et al. (2006)/Fuller (1987) 中已有论述，要求数学语言论证区分。R1 反驳：Theorem 1 的 δ_s·Δτ 乘积分解在 Carroll 框架无对应物——前者处理 mismeasured regressor 的 scalar attenuation，后者处理 effect modifier misclassification 下 global vs subgroup correction 的 mismatch，结构不可互推。\n- **Director 裁定**: R1 论证有说服力，贡献不被 Carroll 涵盖。但论文表述可更锐利——应在 Section 3 增加 Remark 用数学符号对比 F-L attenuation formula 与 Theorem 1 的 structured decomposition。降为 should-fix。\n\n**W-SF2. [DIVERGENT → Director 裁定 should-fix] HB partial pooling 方法新颖性有限**\n- **来源**: R2-N2（critical），R1 [REBUT] 降级\n- **分歧**: R2 认为 Dirichlet-Multinomial HB 是 James-Stein shrinkage 的直接应用，方法新颖性不足。R1 反驳：应评价框架整体（Theorem 1 → HB → variance-adjusted CF → diagnostic → PPCI 组合），不应剥离 HB 单独评价。\n- **Director 裁定**: HB 组件确实不新颖（论文自承），但框架设计有工程价值。论文应更坦诚地定位贡献——主要在 problem identification + bias identity，EC-HTE 是 \"the right tool for the right problem\" 而非方法创新。降为 should-fix。\n\n**W-SF3. [DIVERGENT → Director 裁定 should-fix] 缺乏真实数据 CATE 基准验证**\n- **来源**: R1-N2（critical），R2 [AGREE 但建议降级]\n- **分歧**: R1 认为所有定量评估依赖 synthetic/semi-synthetic DGP 是 must-fix。R2 同意问题存在但认为是因果推断方法论文的固有局限——CausalForest、PPI 原始论文同样如此。\n- **Director 裁定**: 结构性限制，非本文特有。验证层次（520 synthetic → semi-synthetic → 11 real CMs R²=0.975 → Hate Speech patterns）在方法论文中已属充分。降为 should-fix，建议在 Hate Speech case study 中用 held-out expert labels 构建 pseudo ground-truth CATE 进行方向性比较。\n\n**W-SF4. [CONSENSUS] Subgroup 选择指导缺失**\n- **来源**: R1-W2 + R2-W4，交叉完全 [AGREE]\n- **问题**: EC-HTE 要求预定义 subgroup mapping S: X → {1,...,K}，但未提供 subgroup misspecification 后果分析或 data-driven discovery 指导。与 CausalForest 自动发现异质性相比是显著实用性差距。Appendix P 的随机 subgroup 实验是极端情况，缺乏 \"partially correct subgroup\" 测试。\n- **修改方向**: Limitations 补充 subgroup selection guidance；讨论 Proposition 3 diagnostic 反向用于 subgroup selection 的可能性。\n\n**W-SF5. [CONSENSUS] Abstract 信息密度过高**\n- **来源**: R2-W2，R1 交叉 [AGREE]\n- **问题**: ~250 词内塞入 10+ 个具体数字，核心 message 被稀释。\n- **修改方向**: 精简到 3-4 个关键数字（R² > 0.97、50% configurations worsened、AUC 0.86、7.4× bias reduction），其余移至 Introduction。\n\n**W-SF6. [CONSENSUS] \"Exact identity\" 强调过度**\n- **来源**: R2-W3，R1 交叉 [AGREE]\n- **问题**: 论文多处强调 \"exact identity, not a bound\"，但 Frazis & Loewenstein (2003) 的 scalar attenuation 同样是 exact。真正新颖性在于 δ_s × Δτ 的结构化分解。\n- **修改方向**: 将措辞重心从 \"exact identity (not a bound)\" 转移到 \"structured bias decomposition identity\"。\n\n**W-SF7. [CONSENSUS] 遗漏若干相关文献**\n- **来源**: R2-W1，R1 交叉 [AGREE]\n- **遗漏**: Mellon et al. (2025) LLM annotation variance sources；Bauer et al. (2024) LLM annotation ME reduction；Calvi et al. (2015) HTE with mismeasured treatment。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **达成共识** [AGREE]：\n1. Plug-in SE regime 矛盾是最实质性的技术缺陷 [Must-Fix]\n2. 问题识别的实际价值和 Theorem 1 的理论贡献是论文最大的强项\n3. 实验覆盖面令人印象深刻\n4. Subgroup 选择指导缺失需要补充\n5. Abstract 应精简数字密度\n6. \"Exact identity\" 措辞应调整为 \"structured decomposition\"\n7. A3 balanced classes 是 expositional convenience 非 structural limitation（R2 rebut R1-W1，R1 接受）\n8. κ > 100 singularity guard 是 safety net 非 tuning parameter（R2 rebut R1-W4，R1 接受）\n9. PPCI 组合的 Table 8 factorial design 提供了充分经验证据（R2 rebut R1-W3，部分接受）\n\n## Reviewer Divergence\n\n以下问题存在分歧，**Director 已裁定**：\n1. **Carroll et al. 区分**：R2 标 critical → R1 rebut（乘积分解结构性不同）→ Director 裁定 should-fix（presentation fix）\n2. **HB 方法新颖性**：R2 标 critical → R1 rebut（框架 vs 组件）→ Director 裁定 should-fix（重新定位贡献）\n3. **Real data validation**：R1 标 critical → R2 同意但降级 → Director 裁定 should-fix（结构性限制）\n\n---\n\n## Questions（需作者回应）\n\n**Q1.** [R1] Plug-in SE 在 n_expert ∈ {25, 50, 75} 下的 bootstrap coverage 是多少（含 per-subgroup breakdown）？\n\n**Q2.** [R2] Theorem 1 的 bias identity 能否从 Carroll et al. (2006) 的 functional measurement error framework 中作为 special case 推导？如果不能，请用数学语言说明。\n\n**Q3.** [R1+R2] 如果实践者不确定 subgroup 定义是否正确，Proposition 3 的 diagnostic 能否反向用于 subgroup selection？\n\n**Q4.** [R2] Diagnostic 的 precision-recall 分析（false negative vs false positive 代价不对称）？\n\n**Q5.** [R2] A1 violation strength γ ∈ [0, 0.2] 是否覆盖了实际 LLM 标注的 outcome-dependence 幅度？有无 empirical calibration？\n\n**Q6.** [R1] Corollary 5 下，若 Δτ_s 与 δ_s 正相关（treatment effect heterogeneity 与 misclassification heterogeneity 沿同一维度），amplification 效应会更严重还是更轻？\n\n---\n\n## Missing References\n\n- Mellon et al. (2025). \"Variance-Aware LLM Annotation for Strategy Research.\" arXiv:2601.02370.\n- Bauer et al. (2024). \"To Err Is Human; To Annotate, SILICON?\" arXiv:2412.14461.\n- Calvi et al. (2015). \"Heterogeneous Treatment Effects with Mismeasured Endogenous Treatment.\" arXiv:1511.04162.\n\n---\n\n## External Review\n\n**外部审稿**: 未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（4 warnings, 0 critical, 12 info）。主要发现：\n\n1. **[warning] Pages 3-6 连续 4 页无 figure/table**。Related Work（p3）和 Method 4.1-4.3（p6）完全缺乏 display item，审稿人可能在此段感到节奏单调。\n2. **[warning] 主文仅 3 个 display items**（Figure 1 p2, Table 1 p7, Figure 2 p8），密度 0.33/页偏低。大量关键实验结果全在 Appendix，审稿人可能不会翻阅。\n3. **[warning] Page 8 极度拥挤**：Figure 2 + Section 5.4 + Conclusion + Limitations 起始全挤在一页，Conclusion 被压缩。\n4. **[warning] Page 9 Limitations 延伸**：整页纯文本，无 display item。需确认 Limitations 完整归入豁免页。\n\n格式合规确认：正文 ≤ 8 页 ✓，`[review]` 选项 ✓，匿名性 ✓，Limitations section 存在 ✓，参考文献格式 ✓。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5（Borderline Conference）\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4/5 | 4/5 | **4/5** |\n| Excitement | 3.5/5 | 3/5 | **3/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**综合判断**: 论文识别了一个重要且非直觉的问题，提供了严谨的理论刻画（exact bias identity, R² > 0.97）和全面的实验验证（520 configurations, 8 LLMs, 11 model-dataset combos）。主要限制因素：(1) plug-in SE 与方法优势的 regime 矛盾是唯一的共识 must-fix——如果 rebuttal 能提供小 n 下的 bootstrap coverage 数据，可消除此顾虑；(2) 方法贡献（HB partial pooling）是标准工具的直接应用，创新性有限但工程价值明确；(3) 缺乏真实 CATE ground truth 验证是结构性限制，非本文特有。\n\n**推荐**: Strong Findings candidate。如果 rebuttal 有力回应 W-MF1（提供小 n bootstrap coverage）并调整贡献定位（W-SF1/SF2），可上调至 4（Conference）。\n\n**EMNLP 2026 ARR 评分对照**: 3.5 = Borderline Conference。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 叙事逻辑清晰：Problem → Gap → Solution → Results。\"a researcher who corrects for annotation noise using a pooled confusion matrix may introduce more bias than doing nothing\" 准确有力。\n- 贡献列表 3 项（identity, EC-HTE, diagnostic）层次分明。\n- Footnote 1 澄清 \"debiasing\" 含义（annotation measurement-error bias, not algorithmic fairness）是好的，但可增加对 DML \"debiased\" 的区分。\n\n### Section 2 (Related Work)\n- 三层区分（measurement error, annotation models, HTE+LLM）结构合理。\n- 与 Frazis & Loewenstein (2003) 的区分需加强数学层面的论证。\n- 遗漏 Mellon et al. (2025)、Bauer et al. (2024)、Calvi et al. (2015)。\n\n### Section 3 (Bias Decomposition)\n- Theorem 1 证明完整（Appendix B 可验证），R² 验证有力。\n- 5 个假设（A1-A5）逐条列出，sensitivity 分析覆盖各假设违反。\n- Remark 2 声称 \"does not require (A2)\" 与 Theorem 1 假设列表的表面矛盾需澄清。\n- Proposition 3 的 diagnostic 有独立实用价值，AUC = 0.86（synthetic symmetric），但真实 LLM CM 上 AUC 降至 0.63——需在正文讨论。\n\n### Section 4 (EC-HTE)\n- HB estimation (Section 4.1) 描述完整，α₀ 的 empirical Bayes 估计合理。\n- Singularity guard κ > 100 是合理的 safety net（Appendix A 验证阈值不敏感）。\n- **Plug-in SE (Section 4.3, Eq. 5) 是主要弱点**：不传播 CM estimation uncertainty，n_expert < 100 时 coverage 缺口需量化。\n- PPCI 组合描述清晰，Table 8 的 4-DGP factorial design 提供充分经验证据。\n\n### Section 5 (Experiments)\n- 520 configurations + 100 MC runs 设计系统，MC SE < 3.2%。\n- Table 1 仅展示 extreme heterogeneity 有利结果——caption 已注明 moderate/TweetEval 在 Table 7，但审稿人可能不翻 Appendix。\n- Semi-synthetic TweetEval 中 EC-HTE 未显著优于 Global（p=0.395）——论文在正文诚实报告，是加分项。\n- Section 5.4 的 diagnostic workflow 有独立实用价值。\n\n### Section 6 (Conclusion)\n- 过于压缩（视觉审查确认 page 8 拥挤）。\n\n### Limitations\n- 覆盖 5 个要点，整体诚实。\n- 未提及：continuous effect modifiers、Corollary 4 多分类扩展无实验验证。\n",
  "project": "ec_hte_llm_annotation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: \"Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审稿模式**: Fresh（初审，2 Reviewers × 1 轮 + 交叉分享）\n\n---\n\n## Summary\n\n本文研究 LLM 标注作为 effect modifier 用于异质性处理效应（HTE）分析时，subgroup-heterogeneous misclassification 对 CATE 估计引入的 bias。核心贡献：(1) Bias Decomposition Identity（Theorem 1）——精确恒等式将 correction-induced bias 分解为 δ_s · Δτ / (1−2π̄) 的乘积形式；(2) EC-HTE——基于 hierarchical Bayesian subgroup-stratified confusion matrix 的纠偏框架；(3) Δτ-free diagnostic（Proposition 3）——仅需 per-subgroup error rates 即可判断 global correction 是否有害；(4) EC-HTE+PPCI 组合处理 covariate+outcome 双重误差。实验覆盖 520 synthetic configurations、semi-synthetic TweetEval、Hate Speech real-data case study、8 LLMs（6 proprietary + 4 open-source）。\n\n---\n\n## Strengths\n\n**S1. 问题识别的实际价值与非直觉性。** 论文揭示了一个重要的失败模式：当 LLM 误分类率跨 subgroup 异质时，标准 global confusion-matrix correction 在 50% 的 K=2 配置中恶化 CATE 估计（Section 5.2）。\"debiasing can be worse than doing nothing\" 的发现对 CSS 实践者有直接警示意义。[两位 Reviewer 一致认可]\n\n**S2. Theorem 1 的理论贡献干净且有独立价值。** bias = δ_s · Δτ · amplification factor 的乘积分解结构直观地揭示了 misclassification heterogeneity 与 treatment effect heterogeneity 的交互作用。证明（Appendix B）完整可验证，R² > 0.994 (K=2) 和 R² > 0.974 (K=4) 的经验验证覆盖 520 synthetic configurations + 11 real LLM confusion matrices。[两位 Reviewer 一致认可，Soundness 评 4/5]\n\n**S3. 实验设计系统全面。** 520 configurations 参数网格、100 MC runs + MC SE 报告、semi-synthetic TweetEval（真实文本特征 + 合成 CATE）、multi-LLM 一致性验证（Spearman ρ ≥ 0.82）、21 个 Appendix 覆盖主要 assumption violation 场景。实验规模在同类论文中属上乘。[两位 Reviewer 一致认可]\n\n**S4. Diagnostic 工具的实用性。** Proposition 3 的 Δτ-free diagnostic 打破了 \"要诊断需要先知道答案\" 的循环依赖，AUC = 0.86 at subgroup level。独立于 EC-HTE 可使用，为实践者提供低成本 screening tool。[两位 Reviewer 一致认可]\n\n**S5. 完整的实践指南。** Algorithm 1 伪代码可直接实现，expert budget crossover curves（Appendix I-J）、diagnostic threshold guidance（Section 5.4）构成完整 workflow。[两位 Reviewer 一致认可]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-MF1. [CONSENSUS] Plug-in SE 与方法优势的 regime 矛盾**\n- **来源**: R1-N1（critical），R2 交叉完全 [AGREE]\n- **问题**: EC-HTE 的 HB shrinkage 在低 expert budget（n_expert < 100）时提供最大的点估计优势（Table 3, K=2 n=25: HB RMSE 0.256 vs MLE 0.269），但恰好在这个 regime 下 plug-in SE（Eq. 5）不传播 confusion matrix estimation uncertainty，CI coverage 不可靠。Appendix Y 的 bootstrap 修复仅验证 n_expert=200（coverage 93.8%→95.0%），**未覆盖 n_expert < 100 的关键区间**。方法的核心卖点与其已知缺陷在同一参数区间内存在结构性矛盾。\n- **影响**: 实践者在最需要 EC-HTE 的场景下无法信赖其置信区间。\n- **修改方向**: (a) 提供 n_expert ∈ {25, 50, 75} 下 bootstrap coverage（含 per-subgroup breakdown）；(b) 正文 Section 4.3 明确标注 plug-in SE valid regime；(c) 如 bootstrap 在小 n 下也不恢复 nominal coverage，诚实讨论。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W-SF1. [DIVERGENT → Director 裁定 should-fix] 与经典测量误差文献的区分不够锐利**\n- **来源**: R2-N1（critical），R1 [REBUT] 降级\n- **分歧**: R2 认为 \"misspecified correction amplifies MSE\" 在 Carroll et al. (2006)/Fuller (1987) 中已有论述，要求数学语言论证区分。R1 反驳：Theorem 1 的 δ_s·Δτ 乘积分解在 Carroll 框架无对应物——前者处理 mismeasured regressor 的 scalar attenuation，后者处理 effect modifier misclassification 下 global vs subgroup correction 的 mismatch，结构不可互推。\n- **Director 裁定**: R1 论证有说服力，贡献不被 Carroll 涵盖。但论文表述可更锐利——应在 Section 3 增加 Remark 用数学符号对比 F-L attenuation formula 与 Theorem 1 的 structured decomposition。降为 should-fix。\n\n**W-SF2. [DIVERGENT → Director 裁定 should-fix] HB partial pooling 方法新颖性有限**\n- **来源**: R2-N2（critical），R1 [REBUT] 降级\n- **分歧**: R2 认为 Dirichlet-Multinomial HB 是 James-Stein shrinkage 的直接应用，方法新颖性不足。R1 反驳：应评价框架整体（Theorem 1 → HB → variance-adjusted CF → diagnostic → PPCI 组合），不应剥离 HB 单独评价。\n- **Director 裁定**: HB 组件确实不新颖（论文自承），但框架设计有工程价值。论文应更坦诚地定位贡献——主要在 problem identification + bias identity，EC-HTE 是 \"the right tool for the right problem\" 而非方法创新。降为 should-fix。\n\n**W-SF3. [DIVERGENT → Director 裁定 should-fix] 缺乏真实数据 CATE 基准验证**\n- **来源**: R1-N2（critical），R2 [AGREE 但建议降级]\n- **分歧**: R1 认为所有定量评估依赖 synthetic/semi-synthetic DGP 是 must-fix。R2 同意问题存在但认为是因果推断方法论文的固有局限——CausalForest、PPI 原始论文同样如此。\n- **Director 裁定**: 结构性限制，非本文特有。验证层次（520 synthetic → semi-synthetic → 11 real CMs R²=0.975 → Hate Speech patterns）在方法论文中已属充分。降为 should-fix，建议在 Hate Speech case study 中用 held-out expert labels 构建 pseudo ground-truth CATE 进行方向性比较。\n\n**W-SF4. [CONSENSUS] Subgroup 选择指导缺失**\n- **来源**: R1-W2 + R2-W4，交叉完全 [AGREE]\n- **问题**: EC-HTE 要求预定义 subgroup mapping S: X → {1,...,K}，但未提供 subgroup misspecification 后果分析或 data-driven discovery 指导。与 CausalForest 自动发现异质性相比是显著实用性差距。Appendix P 的随机 subgroup 实验是极端情况，缺乏 \"partially correct subgroup\" 测试。\n- **修改方向**: Limitations 补充 subgroup selection guidance；讨论 Proposition 3 diagnostic 反向用于 subgroup selection 的可能性。\n\n**W-SF5. [CONSENSUS] Abstract 信息密度过高**\n- **来源**: R2-W2，R1 交叉 [AGREE]\n- **问题**: ~250 词内塞入 10+ 个具体数字，核心 message 被稀释。\n- **修改方向**: 精简到 3-4 个关键数字（R² > 0.97、50% configurations worsened、AUC 0.86、7.4× bias reduction），其余移至 Introduction。\n\n**W-SF6. [CONSENSUS] \"Exact identity\" 强调过度**\n- **来源**: R2-W3，R1 交叉 [AGREE]\n- **问题**: 论文多处强调 \"exact identity, not a bound\"，但 Frazis & Loewenstein (2003) 的 scalar attenuation 同样是 exact。真正新颖性在于 δ_s × Δτ 的结构化分解。\n- **修改方向**: 将措辞重心从 \"exact identity (not a bound)\" 转移到 \"structured bias decomposition identity\"。\n\n**W-SF7. [CONSENSUS] 遗漏若干相关文献**\n- **来源**: R2-W1，R1 交叉 [AGREE]\n- **遗漏**: Mellon et al. (2025) LLM annotation variance sources；Bauer et al. (2024) LLM annotation ME reduction；Calvi et al. (2015) HTE with mismeasured treatment。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **达成共识** [AGREE]：\n1. Plug-in SE regime 矛盾是最实质性的技术缺陷 [Must-Fix]\n2. 问题识别的实际价值和 Theorem 1 的理论贡献是论文最大的强项\n3. 实验覆盖面令人印象深刻\n4. Subgroup 选择指导缺失需要补充\n5. Abstract 应精简数字密度\n6. \"Exact identity\" 措辞应调整为 \"structured decomposition\"\n7. A3 balanced classes 是 expositional convenience 非 structural limitation（R2 rebut R1-W1，R1 接受）\n8. κ > 100 singularity guard 是 safety net 非 tuning parameter（R2 rebut R1-W4，R1 接受）\n9. PPCI 组合的 Table 8 factorial design 提供了充分经验证据（R2 rebut R1-W3，部分接受）\n\n## Reviewer Divergence\n\n以下问题存在分歧，**Director 已裁定**：\n1. **Carroll et al. 区分**：R2 标 critical → R1 rebut（乘积分解结构性不同）→ Director 裁定 should-fix（presentation fix）\n2. **HB 方法新颖性**：R2 标 critical → R1 rebut（框架 vs 组件）→ Director 裁定 should-fix（重新定位贡献）\n3. **Real data validation**：R1 标 critical → R2 同意但降级 → Director 裁定 should-fix（结构性限制）\n\n---\n\n## Questions（需作者回应）\n\n**Q1.** [R1] Plug-in SE 在 n_expert ∈ {25, 50, 75} 下的 bootstrap coverage 是多少（含 per-subgroup breakdown）？\n\n**Q2.** [R2] Theorem 1 的 bias identity 能否从 Carroll et al. (2006) 的 functional measurement error framework 中作为 special case 推导？如果不能，请用数学语言说明。\n\n**Q3.** [R1+R2] 如果实践者不确定 subgroup 定义是否正确，Proposition 3 的 diagnostic 能否反向用于 subgroup selection？\n\n**Q4.** [R2] Diagnostic 的 precision-recall 分析（false negative vs false positive 代价不对称）？\n\n**Q5.** [R2] A1 violation strength γ ∈ [0, 0.2] 是否覆盖了实际 LLM 标注的 outcome-dependence 幅度？有无 empirical calibration？\n\n**Q6.** [R1] Corollary 5 下，若 Δτ_s 与 δ_s 正相关（treatment effect heterogeneity 与 misclassification heterogeneity 沿同一维度），amplification 效应会更严重还是更轻？\n\n---\n\n## Missing References\n\n- Mellon et al. (2025). \"Variance-Aware LLM Annotation for Strategy Research.\" arXiv:2601.02370.\n- Bauer et al. (2024). \"To Err Is Human; To Annotate, SILICON?\" arXiv:2412.14461.\n- Calvi et al. (2015). \"Heterogeneous Treatment Effects with Mismeasured Endogenous Treatment.\" arXiv:1511.04162.\n\n---\n\n## External Review\n\n**外部审稿**: 未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（4 warnings, 0 critical, 12 info）。主要发现：\n\n1. **[warning] Pages 3-6 连续 4 页无 figure/table**。Related Work（p3）和 Method 4.1-4.3（p6）完全缺乏 display item，审稿人可能在此段感到节奏单调。\n2. **[warning] 主文仅 3 个 display items**（Figure 1 p2, Table 1 p7, Figure 2 p8），密度 0.33/页偏低。大量关键实验结果全在 Appendix，审稿人可能不会翻阅。\n3. **[warning] Page 8 极度拥挤**：Figure 2 + Section 5.4 + Conclusion + Limitations 起始全挤在一页，Conclusion 被压缩。\n4. **[warning] Page 9 Limitations 延伸**：整页纯文本，无 display item。需确认 Limitations 完整归入豁免页。\n\n格式合规确认：正文 ≤ 8 页 ✓，`[review]` 选项 ✓，匿名性 ✓，Limitations section 存在 ✓，参考文献格式 ✓。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5（Borderline Conference）\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4/5 | 4/5 | **4/5** |\n| Excitement | 3.5/5 | 3/5 | **3/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**综合判断**: 论文识别了一个重要且非直觉的问题，提供了严谨的理论刻画（exact bias identity, R² > 0.97）和全面的实验验证（520 configurations, 8 LLMs, 11 model-dataset combos）。主要限制因素：(1) plug-in SE 与方法优势的 regime 矛盾是唯一的共识 must-fix——如果 rebuttal 能提供小 n 下的 bootstrap coverage 数据，可消除此顾虑；(2) 方法贡献（HB partial pooling）是标准工具的直接应用，创新性有限但工程价值明确；(3) 缺乏真实 CATE ground truth 验证是结构性限制，非本文特有。\n\n**推荐**: Strong Findings candidate。如果 rebuttal 有力回应 W-MF1（提供小 n bootstrap coverage）并调整贡献定位（W-SF1/SF2），可上调至 4（Conference）。\n\n**EMNLP 2026 ARR 评分对照**: 3.5 = Borderline Conference。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 叙事逻辑清晰：Problem → Gap → Solution → Results。\"a researcher who corrects for annotation noise using a pooled confusion matrix may introduce more bias than doing nothing\" 准确有力。\n- 贡献列表 3 项（identity, EC-HTE, diagnostic）层次分明。\n- Footnote 1 澄清 \"debiasing\" 含义（annotation measurement-error bias, not algorithmic fairness）是好的，但可增加对 DML \"debiased\" 的区分。\n\n### Section 2 (Related Work)\n- 三层区分（measurement error, annotation models, HTE+LLM）结构合理。\n- 与 Frazis & Loewenstein (2003) 的区分需加强数学层面的论证。\n- 遗漏 Mellon et al. (2025)、Bauer et al. (2024)、Calvi et al. (2015)。\n\n### Section 3 (Bias Decomposition)\n- Theorem 1 证明完整（Appendix B 可验证），R² 验证有力。\n- 5 个假设（A1-A5）逐条列出，sensitivity 分析覆盖各假设违反。\n- Remark 2 声称 \"does not require (A2)\" 与 Theorem 1 假设列表的表面矛盾需澄清。\n- Proposition 3 的 diagnostic 有独立实用价值，AUC = 0.86（synthetic symmetric），但真实 LLM CM 上 AUC 降至 0.63——需在正文讨论。\n\n### Section 4 (EC-HTE)\n- HB estimation (Section 4.1) 描述完整，α₀ 的 empirical Bayes 估计合理。\n- Singularity guard κ > 100 是合理的 safety net（Appendix A 验证阈值不敏感）。\n- **Plug-in SE (Section 4.3, Eq. 5) 是主要弱点**：不传播 CM estimation uncertainty，n_expert < 100 时 coverage 缺口需量化。\n- PPCI 组合描述清晰，Table 8 的 4-DGP factorial design 提供充分经验证据。\n\n### Section 5 (Experiments)\n- 520 configurations + 100 MC runs 设计系统，MC SE < 3.2%。\n- Table 1 仅展示 extreme heterogeneity 有利结果——caption 已注明 moderate/TweetEval 在 Table 7，但审稿人可能不翻 Appendix。\n- Semi-synthetic TweetEval 中 EC-HTE 未显著优于 Global（p=0.395）——论文在正文诚实报告，是加分项。\n- Section 5.4 的 diagnostic workflow 有独立实用价值。\n\n### Section 6 (Conclusion)\n- 过于压缩（视觉审查确认 page 8 拥挤）。\n\n### Limitations\n- 覆盖 5 个要点，整体诚实。\n- 未提及：continuous effect modifiers、Corollary 4 多分类扩展无实验验证。\n",
    "project": "ec_hte_llm_annotation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-23T09:14:24.356624+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6b114d432b35fe7a1c2143457ae85b08:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 1004 · 2026-05-23T09:14:35.356545+00:00_

审稿报告已投递。

**本轮审稿总结**：

- **Overall**: 3.5 / 5（Borderline Conference），两位 Reviewer 一致
- **唯一共识 Must-Fix**: Plug-in SE 与 HB shrinkage 优势在 small n_expert regime 的结构性矛盾——bootstrap coverage 数据缺失
- **3 个分歧裁定为 Should-Fix**: Carroll et al. 区分（presentation fix）、HB 方法新颖性（贡献重新定位）、真实数据验证（结构性限制）
- **4 个共识 Should-Fix**: Subgroup 选择指导、Abstract 信息过载、"exact identity" 措辞、遗漏文献
- **推荐**: Strong Findings candidate，rebuttal 有力回应 plug-in SE gap 可上调至 4（Conference）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 94

## Round 94

2 recorded events


### User

_source line 1005 · 2026-05-23T09:14:38.243109+00:00_

[Reviewer 1 审稿结果]:
已完成两项任务：

1. **首轮审稿** — 聚焦方法严谨性 + 实验设计，给出 Overall 3.5 (Borderline Conference)，提出 2 个 Must-Fix（plug-in SE 低估不确定性、缺乏真实数据 CATE 基准）和 4 个 Should-Fix。

2. **对 R2 的逐条交叉回应** — 对 R2 的 2 个 Must-Fix 均给出 [REBUT]（N1: Theorem 1 的乘积分解结构不可由 Carroll et al. 直接推导，建议降为 should-fix；N2: 框架 novelty 不应以单个 HB 组件评价），对 4 个 Should-Fix 中 3 个 [AGREE]、1 个 [AGREE] 并补充自己的观察，对 Minor Issues 5 个 [AGREE] + 1 个 [REBUT]（M5 年份需 R2 提供具体指向）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1006 · 2026-05-23T09:14:58.081173+00:00_

审稿报告已投递完成。

**本轮审稿总结**：

- **Overall**: 3.5 / 5（Borderline Conference），两位 Reviewer 一致
- **唯一共识 Must-Fix**: Plug-in SE 与方法优势的 regime 矛盾——HB shrinkage 在小 n_expert 时优势最大，但 CI coverage 恰在此区间不可靠，bootstrap 修复未覆盖关键区间
- **3 个分歧问题 Director 裁定降为 Should-Fix**: Carroll et al. 区分（presentation fix）、HB 方法新颖性（重新定位贡献）、真实数据验证（结构性限制）
- **4 个共识 Should-Fix**: subgroup 选择指导缺失、Abstract 信息过载、"exact identity" 措辞调整、遗漏文献
- **推荐**: Strong Findings candidate。Rebuttal 若能提供小 n bootstrap coverage + 调整贡献定位，可上调至 4（Conference）

Issue tracker 已同步更新（Round 13），视觉审查结果已拼入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 95

## Round 95

50 recorded events


### User

_source line 1007 · 2026-05-23T13:11:31.192501+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: ec_hte_llm_annotation
- 论文路径: projects/ec_hte_llm_annotation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-23T13:11:38.285198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-23T13:11:38.388258+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-23T13:11:46.777410+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__request_study_approval",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__request_study_approval",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-23T13:11:46.777932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-23T13:11:49.438564+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-23T13:11:49.489264+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-23T13:11:56.380008+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-23T13:11:57.635392+00:00_

{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (39 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-027b: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error（准备中）\n- exp-027: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage（准备中）\n\n## 近期结论\n- **exp-036** (success): Bootstrap SE (B=200, re-estimating CM + re-fitting CF per bootstrap) can close the CausalForest under-coverage gap (91% vs nominal 95%) by properly accounting for CM estimation uncertainty that plug-in SE ignores.\n- **exp-037** (success): Temperature scaling reduces per-subgroup misclassification rates but does NOT eliminate heterogeneity (Δπ shrinks from 0.20 to 0.07 but remains nonzero), so EC-HTE is still necessary post-calibration. Calibrated+EC-HTE should achieve the best coverage.\n- **exp-035** (success): EC-HTE with asymmetric CM estimation (full 2x2 FPR/FNR) maintains coverage >=93% under realistic 7:1 FPR/FNR ratios (simulating GPT-4.1 on Civil Comments), and outp
…[truncated 309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-23T13:11:57.786359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-23T13:11:58.690653+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{enumitem}
16	\usepackage{algorithm}
17	\usepackage{algpseudocode}
18	
19	\newtheorem{theorem}{Theorem}
20	\newtheorem{corollary}[theorem]{Corollary}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{remark}[theorem]{Remark}
23	
24	\title{Error-Corrected Heterogeneous Treatment Effects:\\When LLM Annotation Debiasing Hurts}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{theory}
38	
39	\input{method}
40	
41	\input{experiments}
42	
43	\input{conclusion}
44	
45	\input{limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{appendix}
51	
52	%\input{checklist}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-23T13:11:58.791533+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1019 · 2026-05-23T13:11:59.394333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf",
    "limit": "1"
  }
}
```

</details>

---


### Tool result

_source line 1020 · 2026-05-23T13:11:59.444999+00:00_

This PDF has 29 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-23T13:12:04.264056+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission guidelines. However, the search results pr
…[truncated 1279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 5472
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-23T13:12:10.639411+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 1023 · 2026-05-23T13:12:10.890684+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 submission guidelines author instructions page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR 2026 submission guidelines author instructions page limit template"
  }
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-23T13:12:13.049523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-23T13:12:13.753159+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf (747KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool result

_source line 1026 · 2026-05-23T13:12:15.281291+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here is the information about EMNLP 20
…[truncated 838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 4641
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-23T13:12:18.142631+00:00_

Web search results for query: "ARR 2026 submission guidelines author instructions page limit template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here's what I found regarding ARR 2026 submission guidelines:

## Key ARR 2026 Submission Guidelines

### Page Limits
Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references. Content covering broader impacts/ethical considerations and acknowledgments do not count towards the page limit.

### Formatting and Templates
The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template. ACL provides style files for LaTeX and Microsoft Word that meet these requirements, found at https://github.com/acl-org/acl-style-files, and their use is strongly recommended.

### Author Instructi
…[truncated 699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 7251
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-23T13:12:25.824381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf",
  "pages": "11-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf",
    "pages": "11-20"
  }
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-23T13:12:26.828483+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf (747KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-23T13:12:26.989301+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for papers main conference submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org call for papers main conference submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1031 · 2026-05-23T13:12:27.694110+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1032 · 2026-05-23T13:12:34.021317+00:00_

Web search results for query: "site:2026.emnlp.org call for papers main conference submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"}]

I found information about EMNLP 2026's main conference paper submission guidelines. Here are the key details:

## Submission Process and Requirements

Papers must be submitted, at latest, by the ARR 2026 May cycle. Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.

## Paper Types and Focus

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using e
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 7032
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-23T13:12:34.021830+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'ec_hte_llm_annotation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6327
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-23T13:12:47.327968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf",
  "pages": "21-29"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf",
    "pages": "21-29"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-23T13:12:48.032632+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf (747KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-23T13:12:48.096955+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-23T13:12:48.147891+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/decisions.yaml\", \"content\": \"_next_id: 22\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:52 UTC\\n  summary: MVP PASS：核心假设验证通过，评估框架修正为子群水平\\n  rationale: 三轮模拟（v1 CausalForest + v2 差分估计 + v3 子群分析）完成。核心发现：(1) 全局校正在低误差子群造成系统性伤害（bias\\n    恶化 7.8x），EC-HTE 分层校正修复此问题（|bias|<0.015）；(2) 边际 CATE 评估掩盖此效应（正负偏差抵消），子群水平才是正确评估维度；(3)\\n    EC-HTE 在高误差子群方差偏高→层级贝叶斯 partial pooling 是 research 阶段核心优先级。Pass 标准 1 修正为子群水平后\\n    PASS（子群 B EC-HTE RMSE 0.063 vs Global 0.100），标准 2/3/4 均 PASS。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:44 UTC\\n  summary: Dream Round 1 分析完成：best=4 (Weak Accept), median=3.5 (Borderline Conference),\\n    worst=2.5 (Borderline Reject)。达到启动门槛（best≥weak accept, median≥borderline）。识别6项确认行动项、4项观察项。更新\\n    framing 和 plan 后批准 P0 CPU 实验（exp-001, exp-002）立即启动。exp-007 (PPCI comparison) 升级为\\n    P0。\\n  rationale: 三档一致的结构性问题：(1) 薄弱文献（11 refs vs 40+ expected），(2) MCMC 实现细节缺失，(3) 方法新颖性定位需明确为\\\"问题发现\\\"而非\\\"新技术\\\"，(4)\\n    信息密度过高需增加图表减少表格，(5) K=2 理论 vs K>2 实验的 gap，(6) 真实数据验证缺失。数据依赖性问题（coverage undercoverage,\\n    diagnostic AUROC, PPCI dominance）仅在2档或单档出现，记录为观察项待真实实验验证。framing/plan 改动为渐进式改善（sharpening\\n    novelty positioning, adding requirements），不构成重大方向转变，当前 Dream 评分已达标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 21:32 UTC\\n  summary: 'Dream Round 2 analysis: proceed with P0 experiments, 10 writing requirements\\n    codified'\\n  rationale: 'Dream Round 2 (dream_20260520T194535): best=4/6, median=3.5/6, worst=3/6.\\n    Worst improved +0.5 from Round 1 (was 2.5). Three-tier consistent issues all addressable\\n    in writing phase: (1) bibliography 9→30-35 refs, (2) \\\"bias bound\\\"→\\\"bias decomposition\\n    identity\\\", (3) DGP specification, (4) figures, (5) Fuller 1987 contextualization,\\n    (6) \\\"never worse\\\" qualification, (7) inve
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-23T13:13:11.665989+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-23T13:13:11.716557+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-23T13:13:18.042044+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-23T13:13:18.042513+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-23T13:13:18.494475+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-23T13:13:18.595442+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/memory.md\", \"content\": \"# Memory — ec_hte_llm_annotation\\n\\n## 研究发现\\n\\n### 非对称诊断等价性 (2026-05-23, Worker A)\\n对 K_Z=2（二值标签），非对称诊断公式 |B_s[1,1] - B_s[1,0]| / (FPR_s + FNR_s) 恒等于对称公式 |δ_s| / ((1-2π̄)·π_s)。FPR/FNR 不对称性在行差中完全抵消。AUC=0.63 的真正原因是 τ_s=0 子组的 MC 噪声，排除后 AUC=1.0。\\n\\n### Centered EB 优于 Dir(α/2, α/2) (2026-05-23, Worker C)\\n原始 HB 用 Dir(α/2, α/2) 向 (0.5, 0.5) 收缩是错误目标。Centered EB 向 global CM 收缩，在 moderate heterogeneity 下 RMSE ≈ Global（消除弱点），在 extreme 下 RMSE < Global < original HB。K4 extreme 下 original HB RMSE > Global 的问题也被修复。\\n\\n### Bootstrap SE 在小 n_expert 下的表现 (2026-05-23, Task G)\\nDIM + Centered EB, K=2 extreme (π=[0.05,0.25]), 20 MC × B=100。Bootstrap coverage 在所有 n_expert ≥25 下均达 nominal (≥95%): n=25→100%, n=50→98.8%, n=75→97.5%, n=100→96.3%, n=200→95.0%。Plug-in SE 在 n≥50 时 ≥92.5%，最弱点 n=75 (91.2%)。高误差子群 s1 (π=0.25) 是 bootstrap 的主要受益者。数据: results/exp_bootstrap_small_n_summary.csv\\n\\n## 决策记录\\n\\n### API 模型版本 (已验证)\\n- GPT-4.1: `gpt-4.1-2025-04-14`\\n- GPT-5.4: `gpt-5.4` (reasoning model, 慢, ~1min/call)\\n- GPT-5.5 不可用（reasoning tokens 消耗 max_tokens budget）\\n\\n### 论文写作\\n- EMNLP 2026 DDL: 2026-05-25 (ARR)\\n- 8 页主文限制，Limitations/References 不计入\\n- R15 审稿修复已全部完成（8 项，2026-05-23）\\n- Messing (2026) 已加入 Related Work\\n- 数据完整性审计完成：AUC=0.86 确认正确（Δπ-only diagnostic），AUC=0.82→0.66 已修复（3处），74-82% coverage 确认正确\\n- 匿名代码仓库已推送: https://github.com/anonymous-nlp-2026-2/ec_hte_llm_annotation (74 files, commit 5b722d5)\\n\\n### 实验边界条件\\n- K=8 是 scalability boundary：coverage 95.6% 但 RMSE > Global\\n- 分类器质量阈值：任一子群 FNR≈0.5 时 CM 反转放大噪声（exp-015, exp-004 确认）\\n- 预算阈值：n_expert/K ≥ 25 per subgroup，K=4 时 n_expert ≥ 100\\n- Class imbalance: P(Z=1)=0.18 + K=4 → per-subgroup Z=1 labels 不足，EC-HTE 失效（exp-015, exp-016）\\n\", \"total_chars\": 1646, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-23T13:13:23.465552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-23T13:13:23.818464+00:00_

1	issues:
2	  # === RESOLVED (prior rounds, unchanged) ===
3	  - id: "R1-N1"
4	    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
5	    category: method
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 0
9	    last_seen_round: 2
10	    action_items: []
11	    resolution: "重新推导为精确恒等式"
12	    resolution_round: 0
13	
14	  - id: "R2-W8"
15	    summary: "Proposition 1 限于 K=2"
16	    category: method
17	    severity: critical
18	    status: resolved
19	    first_raised_round: 0
20	    last_seen_round: 1
21	    action_items: []
22	    resolution: "Theorem 1 适用一般 K"
23	    resolution_round: 0
24	
25	  - id: "R1-N2"
26	    summary: "Real data ground truth CATE 来源不明"
27	    category: experiment
28	    severity: critical
29	    status: resolved
30	    first_raised_round: 0
31	    last_seen_round: 1
32	    action_items: []
33	    resolution: "恰当定位为 illustrative application"
34	    resolution_round: 0
35	
36	  - id: "R1-N3"
37	    summary: "HB 模型规格严重不完整"
38	    category: method
39	    severity: critical
40	    status: resolved
41	    first_raised_round: 0
42	    last_seen_round: 1
43	    action_items: []
44	    resolution: "完整 MCMC 规格"
45	    resolution_round: 0
46	
47	  - id: "JOINT-W4"
48	    summary: "相关工作严重遗漏"
49	    category: writing
50	    severity: warning
51	    status: resolved
52	    first_raised_round: 0
53	    last_seen_round: 1
54	    action_items: []
55	    resolution: "30+ 引用覆盖"
56	    resolution_round: 0
57	
58	  - id: "JOINT-W3"
59	    summary: "信息密度过高"
60	    category: writing
61	    severity: warning
62	    status: resolved
63	    first_raised_round: 0
64	    last_seen_round: 1
65	    action_items: []
66	    resolution: "主文精简至合理密度"
67	    resolution_round: 0
68	
69	  - id: "R2-W7"
70	    summary: "真实数据验证单薄"
71	    category: experiment
72	    severity: warning
73	    status: resolved
74	    first_raised_round: 0
75	    last_seen_round: 1
76	    action_items: []
77	    resolution: "恰当定位 + 公开数据集"
78	    resolution_round: 0
79	

…[truncated 36270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-23T13:14:03.793735+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-23T13:14:04.198604+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-23T13:14:05.103665+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-23T13:14:09.077003+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3973
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-23T13:14:17.869358+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-23T13:14:17.920166+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/paper_framing.md\", \"content\": \"# Paper Framing — ec_hte_llm_annotation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (via ARR)\\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\\n- Format: Long paper, 8 pages + unlimited references\\n\\n## Core Claims (3 条，可证伪)\\n\\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \\\"debiasing\\\" can worsen CATE bias by 2-3x (median across configurations), with amplification up to 5.9x for K=4 subgroups; when naive bias is near zero, global correction creates bias where none existed. For the difference-in-means estimator, the amplification magnitude does NOT monotonically increase with K (K=2 extreme: up to 2.86× vs K=4 extreme: up to 2.41×); however, with nonlinear estimators such as CausalForest, more subgroups amplify the effect substantially (K=4/extreme: up to 5.9×) due to compounding estimation noise in tree-based CATE. Global correction increases subgroup-level bias in ~50% of the parameter space.\\n\\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias when misclassification heterogeneity is sufficiently high, while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction by borrowing strength across groups (classic James-Stein shrinkage). We provide precise crossover thresholds: EC-HTE outperforms global correction in RMSE with as few as 250 expert labels (K=2, high heterogeneity), scaling to ~1000 for K=4. **Boundary condition**: when expert labels per subgroup < ~25, shrinkage can be 
…[truncated 3348 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-23T13:15:11.568096+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### 论文信息\n- **标题**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\n- **论文路径**: `projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf`（29 页）\n\n### 目标 Venue\n- **EMNLP 2026 Main**（via ARR）\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤ 8 页, 参考文献不限\n- **Limitations 章节**: 必须，不计入页数限制（不能过长）\n- **模板**: ACL style (`[review]{acl}`)\n- **匿名**: Double-blind\n- **Abstract**: ≤ 200 words\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下维度：\n\n1. **理论证明正确性**：\n   - Theorem 1 (Bias Decomposition Identity) 的证明是否完整、正确\n   - Proposition 3 (Debiasing Can Increase Bias) 的条件和推导\n   - Corollary 4 (Multi-class Extension) 的假设和推广\n   - 各 Remark 的准确性\n   - 假设 (A1)-(A5) 的合理性、必要性和可验证性\n\n2. **统计方法论**：\n   - HB (Hierarchical Bayes) 混淆矩阵估计的模型规格\n   - Gibbs sampling 的收敛性\n   - Plug-in SE 近似 vs Bootstrap SE 的覆盖率校准\n   - 奇异性保护 (κ>100) 的合理性\n   - CausalForest variance-adjusted SE 的推导\n\n3. **实验设计**：\n   - 合成 DGP 是否充分覆盖参数空间\n   - Monte Carlo 实验的统计效力（100 runs 是否足够）\n   - Semi-synthetic TweetEval 实验的生态效度\n   - 真实 LLM 混淆矩阵验证的可信度\n   - Baseline 比较的公平性（Naive, Global, Stratified MLE, PPCI）\n\n4. **假设敏感性**：\n   - (A1) 条件独立性的不可检验性和敏感性分析范围\n   - (A2) 对称误差假设的限制及 asymmetric 扩展充分性\n   - (A3) P(Z=1)=0.5 balanced effect modifier 的限制\n   - (A5) homogeneous treatment effects 的违反后果\n\n请输出完整的审稿报告，包括：Summary, Strengths, Weaknesses (分 Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (使用 EMNLP 2026 评分标准)。",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### 论文信息\n- **标题**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\n- **论文路径**: `projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf`（29 页）\n\n### 目标 Venue\n- **EMNLP 2026 Main**（via ARR）\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤ 8 页, 参考文献不限\n- **Limitations 章节**: 必须，不计入页数限制（不能过长）\n- **模板**: ACL style (`[review]{acl}`)\n- **匿名**: Double-blind\n- **Abstract**: ≤ 200 words\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下维度：\n\n1. **理论证明正确性**：\n   - Theorem 1 (Bias Decomposition Identity) 的证明是否完整、正确\n   - Proposition 3 (Debiasing Can Increase Bias) 的条件和推导\n   - Corollary 4 (Multi-class Extension) 的假设和推广\n   - 各 Remark 的准确性\n   - 假设 (A1)-(A5) 的合理性、必要性和可验证性\n\n2. **统计方法论**：\n   - HB (Hierarchical Bayes) 混淆矩阵估计的模型规格\n   - Gibbs sampling 的收敛性\n   - Plug-in SE 近似 vs Bootstrap SE 的覆盖率校准\n   - 奇异性保护 (κ>100) 的合理性\n   - CausalForest variance-adjusted SE 的推导\n\n3. **实验设计**：\n   - 合成 DGP 是否充分覆盖参数空间\n   - Monte Carlo 实验的统计效力（100 runs 是否足够）\n   - Semi-synthetic TweetEval 实验的生态效度\n   - 真实 LLM 混淆矩阵验证的可信度\n   - Baseline 比较的公平性（Naive, Global, Stratified MLE, PPCI）\n\n4. **假设敏感性**：\n   - (A1) 条件独立性的不可检验性和敏感性分析范围\n   - (A2) 对称误差假设的限制及 asymmetric 扩展充分性\n   - (A3) P(Z=1)=0.5 balanced effect modifier 的限制\n   - (A5) homogeneous treatment effects 的违反后果\n\n请输出完整的审稿报告，包括：Summary, Strengths, Weaknesses (分 Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (使用 EMNLP 2026 评分标准)。",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-23T13:15:27.919441+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16351
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-23T13:15:28.371489+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### 论文信息\n- **标题**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\n- **论文路径**: `projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf`（29 页）\n\n### 目标 Venue\n- **EMNLP 2026 Main**（via ARR）\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤ 8 页, 参考文献不限\n- **Limitations 章节**: 必须，不计入页数限制（不能过长）\n- **模板**: ACL style (`[review]{acl}`)\n- **匿名**: Double-blind\n- **Abstract**: ≤ 200 words\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性/完整性\n\n请重点审查以下维度：\n\n1. **贡献新颖性与定位**：\n   - 核心贡献是 bias mechanism discovery (Theorem 1) 还是 method (EC-HTE)？定位是否清晰准确？\n   - 与 Frazis & Loewenstein (2003) scalar attenuation 的关系——Theorem 1 是否真正超越已有结果？\n   - HB partial pooling 相对于 Dawid & Skene (1979) / Paun et al. (2018) 是否足够新颖？\n   - 诊断准则 (Proposition 3) 的独立价值\n   - 标题 \"When LLM Annotation Debiasing Hurts\" 是否准确反映内容？\n\n2. **相关工作完整性**：\n   - 因果推断中的测量误差文献覆盖是否充分（Fuller 1987, Carroll et al. 2006, Frazis & Loewenstein 2003）\n   - LLM annotation quality 文献（Ashwin et al. 2025, Gilardi et al. 2023, Törnberg 2024 等）\n   - HTE estimation 文献（Athey & Imbens 2016, Wager & Athey 2018, Kennedy 2023 等）\n   - PPI/DSL 相关工作（Angelopoulos et al. 2023, Egami et al. 2024, Sui & Candès 2026）\n   - 是否有重要遗漏——特别是 LLM annotation variance/error sources 方面\n\n3. **写作质量与可读性**：\n   - Abstract 是否 ≤ 200 words，信息密度是否合适\n   - 论文结构是否清晰，符合 EMNLP 读者预期\n   - 符号使用的一致性和清晰度\n   - Figure/Table 的质量和信息传递效率\n   - Limitations 章节的覆盖度和篇幅\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页\n   - 匿名是否严格（无自引泄露）\n   - 参考文献格式是否符合 ACL 规范\n   - Appendix 内容是否应该在正文\n\n5. **可复现性**：\n   - 实验细节是否充分（超参数、数据集、代码）\n   - 是否有足够信息让读者独立复现核心结果\n\n请输出完整的审稿报告，包括：Summary, Strengths, Weaknesses (分 Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (使用 EMNLP 2026 评分标准)。",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### 论文信息\n- **标题**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts\n- **论文路径**: `projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_11/submitted.pdf`（29 页）\n\n### 目标 Venue\n- **EMNLP 2026 Main**（via ARR）\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤ 8 页, 参考文献不限\n- **Limitations 章节**: 必须，不计入页数限制（不能过长）\n- **模板**: ACL style (`[review]{acl}`)\n- **匿名**: Double-blind\n- **Abstract**: ≤ 200 words\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性/完整性\n\n请重点审查以下维度：\n\n1. **贡献新颖性与定位**：\n   - 核心贡献是 bias mechanism discovery (Theorem 1) 还是 method (EC-HTE)？定位是否清晰准确？\n   - 与 Frazis & Loewenstein (2003) scalar attenuation 的关系——Theorem 1 是否真正超越已有结果？\n   - HB partial pooling 相对于 Dawid & Skene (1979) / Paun et al. (2018) 是否足够新颖？\n   - 诊断准则 (Proposition 3) 的独立价值\n   - 标题 \"When LLM Annotation Debiasing Hurts\" 是否准确反映内容？\n\n2. **相关工作完整性**：\n   - 因果推断中的测量误差文献覆盖是否充分（Fuller 1987, Carroll et al. 2006, Frazis & Loewenstein 2003）\n   - LLM annotation quality 文献（Ashwin et al. 2025, Gilardi et al. 2023, Törnberg 2024 等）\n   - HTE estimation 文献（Athey & Imbens 2016, Wager & Athey 2018, Kennedy 2023 等）\n   - PPI/DSL 相关工作（Angelopoulos et al. 2023, Egami et al. 2024, Sui & Candès 2026）\n   - 是否有重要遗漏——特别是 LLM annotation variance/error sources 方面\n\n3. **写作质量与可读性**：\n   - Abstract 是否 ≤ 200 words，信息密度是否合适\n   - 论文结构是否清晰，符合 EMNLP 读者预期\n   - 符号使用的一致性和清晰度\n   - Figure/Table 的质量和信息传递效率\n   - Limitations 章节的覆盖度和篇幅\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页\n   - 匿名是否严格（无自引泄露）\n   - 参考文献格式是否符合 ACL 规范\n   - Appendix 内容是否应该在正文\n\n5. **可复现性**：\n   - 实验细节是否充分（超参数、数据集、代码）\n   - 是否有足够信息让读者独立复现核心结果\n\n请输出完整的审稿报告，包括：Summary, Strengths, Weaknesses (分 Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (使用 EMNLP 2026 评分标准)。",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 1055 · 2026-05-23T13:15:29.685028+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1313
}
```

</details>

---


### Assistant

_source line 1056 · 2026-05-23T13:15:45.521759+00:00_

两名 Reviewer 和视觉审查 Agent 已同时派发：

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性（理论证明、统计方法、实验设计、假设敏感性） | 审稿中 |
| Reviewer 2 | 新颖性/完整性（贡献定位、相关工作、写作质量、格式合规） | 审稿中 |
| Visual Agent | PDF 排版质量（布局、图表、空白分布） | 运行中 |

等待 Reviewer 回稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 96

## Round 96

2 recorded events


### User

_source line 1057 · 2026-05-23T13:26:20.934925+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿报告 — Round 1（新颖性/完整性）

**论文**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts
**Venue**: EMNLP 2026 Main (via ARR)

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 理论贡献清晰实用（Theorem 1 的 bias identity + Proposition 3 的 diagnostic），实验验证全面，但核心洞见数学深度有限，方法组合已有技术而非方法论创新，缺乏真实因果 ground truth 验证。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 理论正确且经验验证充分（R² ≥ 0.97）。假设清晰，sensitivity analysis 覆盖多种违反模式。有限样本中 bias identity 的误差项未给出 formal bound，但 bootstrap SE 部分弥补了这一点。 |
| Excitement | 3/5 | 问题重要且及时（LLM annotation → causal inference），但核心洞见（全局校正在异质误差下引入 bias）在形式化之前已较为直觉性。方法层面组合 HB + per-subgroup correction + CausalForest，无显著方法论创新。 |
| Reproducibility | 4/5 | 实验细节充分（Appendix E: DGP 参数、MCMC 配置、超参数全部记录）。代码承诺接收后发布，审稿时不可用。 |
| Overall Assessment | 3.5/5 | Borderline Conference — 详见下文分析 |

---

## 主要优势

**S1: 问题识别精准且具实践意义。** 论文清晰地展示了一个被广泛使用的实践（global confusion matrix correction）在 subgroup-heterogeneous 误差率下会 *增加* bias——在 50% 的 K=2 实验配置中 global correction 恶化了 bias（Section 5.2, 260/520 configurations）。这个发现对正在使用 LLM annotation 进行因果推断的 CSS 研究者直接有用。

**S2: Theorem 1 的 bias identity 形式优美且精确。** 不是 bound 而是 exact identity：bias_global(τ, s) = δ_s · Δτ · 1/(1−2π)，分解为三个可解释的因子（subgroup error deviation × CATE heterogeneity × amplification）。R² ≥ 0.97 在合成网格和 11 组真实 LLM confusion matrix 组合上得到经验验证（Section 5.2, Appendix N），确认了 population-level identity 在有限样本中的实用准确性。

**S3: Proposition 3 的诊断准则独立可用。** Δτ-free diagnostic 允许从业者在估计任何 treatment effect *之前* 仅使用 pilot sample 的 per-subgroup 错误率即可判断 global correction 是否有害。在有非零 CATE heterogeneity 的 subgroups 上 AUC = 1.0（Section 5.4）。这一工具即使不采用 EC-HTE 也有价值。

**S4: 实验验证覆盖面堪称典范。** Synthetic DGP（Section 5.1）→ Semi-synthetic TweetEval（Section 5.3）→ CausalForest 集成（Table 1）→ 4 个开源 LLM（Appendix O）→ 真实 hate speech 案例（Appendix M）→ PPCI 互补性（Appendix L）→ 16 组 LLM-dataset 诊断验证（Appendix X, Table 21）→ 大量 robustness checks（Appendices P-Z）。实验设计完整，涵盖了我能想到的几乎所有合理变体。

**S5: Limitations 诚实且信息丰富。** 论文坦诚了 EC-HTE 的适用边界：n_expert ≥ K·P(Z_min)·K ≥ 25、extreme heterogeneity 需要 n_expert ≥ 100、near-degenerate confusion matrix 下性能退化。Applicability frontier（Figure 5）将这些限制可视化。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Theorem 1 与 Frazis & Loewenstein (2003) scalar attenuation 的区分在正文中不够充分**
- 具体位置：Section 2 第 3 段（"Three distinctions separate our contribution..."）；Appendix Z.4
- 问题：论文声称与 F-L (2003) 有三点区别：(i) mismeasured variable 是 effect modifier 而非 standard regressor；(ii) misclassification rates vary across subgroups 产生 δ_s·Δτ product structure；(iii) bias 来源于 correction procedure 而非 misclassification 本身。这些区分是正确的，但正文处理仅约 5 行。Appendix Z.4（Table 29）提供了有说服力的经验对比（F-L per-subgroup overcorrects high-error subgroups，F-L global 的 aggregate bias 高于 uncorrected estimator），但这一关键对比被放在 17 页附录的最后，审稿人很可能不会读到。
- 为什么影响接收：不熟悉 measurement error 文献的 NLP reviewer 可能将 Theorem 1 误读为经典 attenuation result 的简单推广。当前正文未充分阻止这种误读，可能导致 novelty 被低估。
- 建议修改方向：在 Section 2 或 Section 3 增加一段正式对比（~4-5 sentences），明确说明：(a) F-L 分析的是 misclassification 的 attenuation effect，而 Theorem 1 分析的是 *correction procedure* 引入的 new bias；(b) δ_s · Δτ product structure 在 F-L 框架中不存在；(c) 引入 Appendix Z.4 的关键经验结果（F-L scalar 在 aggregate 层面表现更差）。

**N2** [critical] **核心贡献的定位模糊——bias mechanism discovery vs. method**
- 具体位置：Section 1 contributions list；Abstract
- 问题：论文同时声称三个贡献（bias identity、diagnostic、EC-HTE method），但未明确表态哪个是 *primary* contribution。从技术深度看，Theorem 1 + Proposition 3 是主要理论贡献，EC-HTE 是 practical instantiation。但 abstract 和 title 给人的印象是方法（EC-HTE）是核心。这种定位模糊使得 reviewer 难以准确评估 novelty：如果 primary contribution 是 bias identity，则 novelty 取决于与 F-L 等经典结果的区分度；如果是 method，则 HB + per-subgroup correction 的组合需要展示更强的方法论创新。
- 为什么影响接收：定位不清会导致不同 reviewer 从不同维度评估 novelty，产生分歧。明确定位有助于 AC 做出一致判断。
- 建议修改方向：在 Introduction 末尾明确声明 primary contribution 是 bias mechanism discovery（Theorem 1 + Proposition 3），EC-HTE 是 instantiation。或者反过来，但两种定位对后续论证有不同要求。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **缺乏真实因果 ground truth 验证**
- 具体位置：Section 5 全部实验；Limitations（page 9）
- 问题：所有实验使用 synthetic 或 semi-synthetic treatment effects。Hate speech 案例（Appendix M）和 4 LLM 实验（Appendix O）使用真实 misclassification patterns 但合成 CATEs。论文坦承 "We leave full real-data validation... to future work"（page 9）。对于声称对 causal inference 有实际影响的论文，完全缺乏 real causal ground truth（例如 RCT + LLM-annotated outcomes）使得实践性 claims 仅依赖 synthetic validation。
- 建议：(a) 在 Limitations 中更详细地论证为何 semi-synthetic 设计是 real causal validation 的合理 proxy（例如：real confusion matrix heterogeneity 是关键，而这在 semi-synthetic 中已验证）；(b) 或在一个有已知因果效应的实验数据上引入 LLM annotation 噪声并验证 EC-HTE。

**W2** [warning] **HB partial pooling 相对于 Dawid-Skene / Paun et al. 的新颖性未充分阐明**
- 具体位置：Section 4.1；Appendix F
- 问题：Section 4.1 的 hierarchical Bayes confusion matrix estimator 使用标准 Dirichlet-Multinomial 模型。论文在 Appendix F 承认 Dawid-Skene 渊源，但 Section 4.1 本身未清晰阐明超越 standard application 的创新点。James-Stein shrinkage effect 是 well-known 的。贡献在于 *应用场景*（subgroup-stratified confusion matrices for HTE），而非方法本身。
- 建议：在 Section 4.1 明确将 HB 定位为 "known technique, novel application context"，或简要说明为何现有 crowdsourcing 方法（如 Dawid-Skene 的 annotator-level modeling）不适用于 subgroup-level confusion matrix 估计。

**W3** [warning] **Assumption (A1) 对 LLM text annotation 的现实性需要更多讨论**
- 具体位置：Section 3, (A1)；Appendix Z.2
- 问题：(A1) 假设 misclassification 仅依赖于 true label Z 和 subgroup S，不依赖于 potential outcomes Y(0), Y(1)。对于 LLM text classification，使注释困难的特征（歧义、讽刺、隐含含义）可能与 treatment effects 相关。Appendix Z.2 测试了 outcome-dependent misclassification，EC-HTE 保持 ≥93.5% coverage，这令人放心。但测试的违反函数（P(Z=1) dependent on Y）是特定形式，可能未涵盖现实中的违反模式（例如 text difficulty 同时影响 annotation error 和 outcome）。
- 建议：在 Limitations 中讨论 (A1) 在 LLM annotation 中可能违反的具体场景，以及 Appendix Z.2 的测试范围是否足以覆盖这些模式。

**W4** [warning] **Scalability to K >> 4 未充分讨论**
- 具体位置：Limitations；Section 4
- 问题：EC-HTE 主要在 K=2 和 K=4 上测试。在真实 NLP 应用中，subgroups 可能由多个交叉特征定义（text length × topic × register × demographic），使 K 迅速增长。Expert budget 需求 K·P(Z_min)·K ≥ 25 线性增长于 K。论文提到 "subgroup definitions should be pre-specified based on domain knowledge" 但未讨论 K 增大时的应对策略。
- 建议：讨论 hierarchical subgroup merging、adaptive budget allocation across subgroups、或与 continuous-covariate HTE methods (e.g., GenericML) 的集成可能性。

**W5** [warning] **Abstract 信息过密**
- 具体位置：Abstract
- 问题：Abstract 约 175 words，在限制内，但塞入了 bias identity、diagnostic、AUC=1.0、EC-HTE、7.4× reduction、coverage >0.96 等大量数值信息。特别是 "the lowest aggregate AUC on real LLM confusion matrices is driven by subgroups where correction is unnecessary" 需要大量上下文才能理解，对首次阅读者不友好。
- 建议：简化数值细节（去掉 AUC=1.0 括号注释和 coverage 数值），为直觉解释留出空间。

---

## 小问题（不影响接收）

- Figure 1（page 2）：概念图字体偏小，"over-correcting low-error subgroups" 和 "under-correcting high-error subgroups" 的视觉对比可加强（例如用颜色或箭头粗细区分方向）。
- Section 3, Remark 2（page 4）：声称 "the asymmetric B_s-based formulation is algebraically equivalent and offers no improvement"，但 Appendix J 的 asymmetric extension 在 FPR ≠ FNR 条件下改善了性能（Table 6: lower RMSE）。两处表述需对齐——Remark 2 应注明 equivalence 限于 symmetric 条件。
- References：部分引用使用 arXiv 版本而非已发表版本（例如 Pangakis et al. 2023 已发表于 EMNLP 2023 Findings）。建议更新至已发表版本。
- Table 1 标题 "Main results (extreme heterogeneity)"：括号中的 "extreme" 可能被误读为 cherry-picking 最有利设置。建议在标题中解释选择 extreme 的原因，或改为 "Main results under varying heterogeneity"。
- Footnote 1（page 1）："debiasing refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing" 这一重要区分放在脚注中容易被忽略，考虑纳入 Introduction 正文第一段。
- 匿名检查：未发现自引泄露或身份暴露。标注 "Anonymous ACL submission" 合规。
- 页数检查：正文（Sections 1-6 Conclusion）在第 8 页内完成。Limitations 从 page 8 下方开始至 page 9，不计入页数限制。合规。

---

## Questions for Authors

**Q1**: Theorem 1 是 population-level identity。在有限样本中 confusion matrix estimation 的方差如何与 bias identity 交互？Appendix Y 提供了 plug-in SE，但 bias identity 本身的有限样本 approximation error 是否有 formal rate（例如 √n-consistent）？

**Q2**: 对于 K > 4 的场景（例如 K=8 或 K=16），EC-HTE 的 expert budget 需求如何增长？是否存在 practical ceiling on K，超过该值 HB estimation 不再可靠？

**Q3**: Proposition 3 的 diagnostic 使用 AUC 评估，但从业者需要 binary decision（是否使用 global correction），而非 ranking。诊断准则的 threshold 应如何选择？论文提到 classifier quality threshold（page 6, "a singularity guard"），但 sensitivity to threshold choice 未充分讨论。

**Q4**: EC-HTE 与 DSL（Egami et al. 2024）的关系需要更多讨论。DSL 也在 subgroup-specific 设置下校正 LLM annotation error。两种方法的 key structural difference 是什么——仅是 confusion matrix correction vs. label model，还是有更深层的 estimand difference？

---

## Missing References

1. **Data programming / label model literature**: Ratner et al. (2017, "Data Programming: Creating Large Training Sets, Quickly"; 2020, Snorkel) 使用 generative label model 处理 noisy annotations。与 confusion-matrix-based correction 概念上相关，作为替代 paradigm 应在 Related Work 中讨论。

2. **Subgroup-specific calibration / multicalibration**: Hébert-Johnson et al. (2018, "Multicalibration: Calibration for the Computationally-Identifiable Masses") 关注模型在 subgroup 上的 differential calibration。与论文对 differential error rates across subgroups 的关注相关。

3. **Prompt sensitivity as annotation variance source**: Lu et al. (2022, "Fantastically Ordered Prompts and Where to Find Them") 展示 prompt 设计对 LLM classification quality 的影响。这是论文 confusion matrix model 未捕获的另一种 annotation variance 来源，与 Related Work 中 LLM annotation quality 讨论相关。

4. **Causal inference with proxies**: Miao et al. (2018, "Identifying Causal Effects with Proxy Variables of an Unmeasured Confounder") 和 Tchetgen Tchetgen et al. (2024) 的 proximal causal inference 框架，将 proxy measurement 嵌入因果识别。虽然设置不同（proxy for confounder vs. proxy for outcome），但 methodological connection 值得一提。

---

## 主要优势总结

- 问题选择精准：LLM annotation → causal inference 的交叉领域，随着 LLM 在 CSS 中的普及日益重要
- 理论贡献干净：exact bias identity 而非 bound，可解释的 product structure
- 实践工具有独立价值：Proposition 3 诊断准则无需估计 treatment effects
- 实验设计堪称标杆：从 synthetic → semi-synthetic → real confusion matrices → robustness checks 的完整验证链
- 写作诚实透明：Limitations 坦诚适用边界，不过度声称

---

## 整体评价

这是一篇扎实、执行良好的论文，解决了一个真实且重要的实践问题。Theorem 1 的 bias identity 形式优美且经验验证充分，Proposition 3 的诊断准则有独立实用价值。实验验证的广度和深度在同类论文中属于上乘。

主要不足在于：(1) 核心理论洞见虽然形式化优雅，但数学深度有限——本质是对 wrong-level correction 引入 bias 的代数分析；(2) EC-HTE 方法组合 HB partial pooling + per-subgroup correction + CausalForest，均为已有技术的直接应用而非方法论创新；(3) 全部实验使用 synthetic/semi-synthetic treatment effects，缺乏真实因果 ground truth 验证。

论文在 Borderline Conference 和 Findings 之间。如果作者能在 rebuttal 中 (a) 更清晰地区分 Theorem 1 与 F-L (2003) 的关系，(b) 明确 primary contribution 的定位，我倾向于接受至 main conference。当前评分：**3.5（Borderline Conference）**。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1058 · 2026-05-23T13:26:40.486196+00:00_

Reviewer 2 审稿已收到（3.5 Borderline Conference）。核心关切：(1) Theorem 1 与 F-L 2003 区分正文不足，(2) 贡献定位模糊。等待 Reviewer 1 回稿后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 97

## Round 97

2 recorded events


### User

_source line 1059 · 2026-05-23T13:26:43.040273+00:00_

[Reviewer 2 审稿结果]:
审稿完成。报告已提交至 Review Director，评分 **3.5（Borderline Conference）**。

核心判断：
- **Theorem 1 的 bias identity** 形式优美（exact identity, R²≥0.97 验证），**Proposition 3 的诊断准则**有独立实用价值——这两项是论文最强的贡献
- 主要不足是核心洞见数学深度有限（本质是 wrong-level correction 的代数分析）、EC-HTE 方法组合已有技术无方法论创新、缺乏真实因果 ground truth
- 提出 2 个 Must-Fix（与 F-L 2003 的区分需在正文中加强；primary contribution 定位需明确）和 5 个 Should-Fix（缺 real causal validation、HB 新颖性、A1 假设现实性、scalability、abstract 信息过密）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1060 · 2026-05-23T13:26:55.317083+00:00_

Reviewer 2 报告已收录（3.5 Borderline Conference）。等待 Reviewer 1 完成审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 98

## Round 98

6 recorded events


### User

_source line 1061 · 2026-05-23T13:28:28.360404+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告 — 方法严谨性审查

**论文**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts
**Venue**: EMNLP 2026 Main (via ARR)

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 核心理论贡献（Theorem 1 偏差分解恒等式）正确且有洞察力，实验验证异常全面，但 Proposition 3 的文字解读疑似存在不等号方向错误，且方法自身的适用性筛选条件过于严格以至于无现有 LLM 通过，削弱了实际价值的论证。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | Theorem 1 证明正确完整，R²≥0.97 跨11个LLM-数据集组合验证；但 Proposition 3 文字解读可能有方向性错误 |
| Excitement | 3.5/5 | 桥接NLP标注质量与因果推断的真实需求，"去偏可能有害"的反直觉发现有价值，但受众相对较窄 |
| Reproducibility | 4/5 | Algorithm 1 完整可实现，DGP 完全指定，29个附录覆盖所有实验细节 |
| Overall | 3.5/5 | Borderline Conference — 理论贡献扎实但存在需要解决的方法论问题 |
| Confidence | 4/5 | 仔细阅读全文29页，独立验证了核心证明代数，对所审维度有较高把握 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Proposition 3 文字解读中不等号方向疑似错误

- 具体位置：Section 3, page 5, Proposition 3 后的解读段落
- 问题：Proposition 3 的形式化条件 |δ_s|/((1−2ε)·ε_s) > 1 本身是正确的。但后续文字解读声称 "any subgroup with ε_s > ε/(2(1−ε)) ≈ 0.088 is harmed"。我独立推导了两种情形：

  **Case 1 — 低误差子群 (ε_s < ε, δ_s < 0)**：条件化简为 (ε − ε_s)/((1−2ε)·ε_s) > 1 → ε_s < ε/(2(1−ε))。即 ε_s < 0.088 时子群受损（过度纠正）。

  **Case 2 — 高误差子群 (ε_s > ε, δ_s > 0)**：条件化简为 (ε_s − ε)/((1−2ε)·ε_s) > 1 → ε_s > 0.5（近随机分类，被 (A4) 排除）。

  代数验证：设 ε=0.15, ε_s=0.05：|δ_s|/((1−2ε)·ε_s) = 0.10/(0.7×0.05) = 2.86 > 1 ✓（受损）。设 ε_s=0.10：0.05/(0.7×0.10) = 0.71 < 1 ✗（不受损）。边界值 ε_s=0.088：0.062/(0.7×0.088) = 1.006 ≈ 1 ✓（边界）。

  这与 "ε_s < 0.088 的低误差子群受损" 一致，与 "ε_s > 0.088 受损" 矛盾。论文后续说"low-error subgroups are over-corrected" 与我的推导方向一致，进一步提示文字中的不等号可能写反了。

  Appendix D 的证明代数本身看起来是正确的。但如果主文的方向性解读确实有误，会直接影响论文核心贡献之一（Δτ-free diagnostic 的使用指导）的可信度。

- 为什么影响接收：Proposition 3 是论文三大贡献之一。解读方向错误会误导从业者的纠正决策。
- 建议：(1) 请作者明确验证低误差子群条件的不等号方向，如有误则修正；(2) 在 camera-ready 中使用更清晰的数学排版确保 < 和 > 不被误读。

---

**N2** [critical] 实际 LLM 混淆矩阵中无配置通过全部适用性筛选条件

- 具体位置：Appendix X, page 24, Table 21
- 问题：论文提出三个适用性筛选条件（Proposition 3 诊断、κ(C_s) ≤ 1.25 条件数、专家预算充分性）。但 Table 21 显示，在 16 个 LLM-数据集-K 组合中，**无一通过全部三个条件**。瓶颈是 κ(C_s) ≤ 1.25，现有 LLM 均不满足。

  这引发理论与实践的张力：论文 Section 5.4 强调 "先诊断再纠正" 的工作流（先用 Proposition 3 判断是否应纠正），但诊断的筛选标准如此严格以至于任何现有 LLM 都无法通过。虽然放松条件后 EC-HTE 在 79%（41/52）配置中优于 Global correction，但这与主文宣称的严格诊断驱动工作流不一致。

  另外，κ ≤ 1.25 的阈值选择未在文中得到充分论证。Algorithm 1 的奇异性保护使用 κ > 100 作为 fallback 条件，与 κ ≤ 1.25 的筛选条件差距极大（80×）。这两个阈值之间的关系和各自的理论依据需要解释。

- 为什么影响接收：如果方法自身的适用性筛选无法被现有 LLM 满足，论文的实际价值论证存在缺口。
- 建议：(1) 在主文明确讨论筛选条件的保守性；(2) 提供实用化的分层筛选阈值（如 κ ≤ 2 或 κ ≤ 5），并验证在放松阈值下方法仍有统计保证；(3) 解释 Algorithm 1 的 κ>100 guard 与 Table 21 的 κ≤1.25 筛选之间的关系。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 二元效应修饰变量假设（A3）限制适用范围

- 具体位置：Section 3, Assumption (A3); Corollary 4 (Appendix C)
- 问题：论文限定效应修饰变量 Z ∈ {0,1} 且 P(Z=1) = 0.5。实际因果推断中效应修饰变量通常是连续的（年龄、收入等）或多水平的。Corollary 4 扩展到多类别但仍限于离散 Z，且假设 uniform off-diagonal misclassification 进一步限制了通用性。论文未讨论连续 Z 的理论扩展方向，也未分析对 Z 进行离散化后的近似误差。对于使用 CausalForest 等天然处理连续异质性的估计器的场景，这一限制尤为突出。
- 建议：至少讨论连续 Z 下偏差分解的理论形式，或证明离散化后近似误差在合理网格密度下可控。

**W2** [warning] 有限样本分析缺乏正式理论推导

- 具体位置：Section 3, page 5, "Finite-sample remainder" 段
- 问题：论文声称有限样本余项 R_s = O_p(n^{−1/2}_expert)，但未给出推导。对于以理论严谨性为核心贡献的论文，从 population identity 到 finite-sample estimator 的过渡是关键步骤。具体而言，混淆矩阵估计误差 ΔC_s = Ĉ_s − C_s 如何通过矩阵求逆 C_s^{−1} 传播到 CATE 偏差，需要用 matrix perturbation theory 或 delta method 分析。矩阵求逆的误差放大因子与 κ(C_s) 直接相关，高条件数时余项可能显著。
- 建议：补充 delta method 推导，或引用矩阵扰动理论（如 ||C^{−1} − Ĉ^{−1}|| ≤ κ(C)²·||ΔC||/||C|| 形式的界）给出形式化误差传播分析。

**W3** [warning] Frazis-Loewenstein 标量衰减纠正未在主文中比较

- 具体位置：仅出现在 Appendix Z.4
- 问题：论文的核心论点之一是混淆矩阵求逆优于标量衰减纠正。但经典的 Frazis-Loewenstein (2003) 方法仅在附录 Z.4 讨论。主文 baselines（Naive, Global, Strat MLE, PPCI）中缺少这一最直接的理论对照。Appendix Z.4 显示 F-L per-subgroup 版本的覆盖率达 95.3%，且 F-L per-subgroup "dramatically over-corrects the high-error subgroup"——这些重要发现应在主文中呈现。
- 建议：在 Table 1 中加入 F-L 比较，或在 Related Work 中更充分讨论与 F-L 的理论关系（特别是 F-L 的标量衰减与全混淆矩阵求逆在何种条件下等价或不等价）。

**W4** [warning] Assumption (A1) 敏感性分析范围有限

- 具体位置：Appendix Z.2, page 27
- 问题：(A1) 条件独立性（标注误差独立于处理分配）是不可检验的核心假设。Appendix Z.2 仅考虑了一种违反形式（outcome-dependent misclassification，γ ∈ [0, 0.20]）。实际中可能出现的其他违反模式——如 treatment-dependent misclassification（处理组和对照组的标注准确率不同）、或 Z×T 交互对误分类率的影响——未被覆盖。γ = 0.20 的上界也可能偏保守，实际场景中 outcome 与标注误差的关联可能更强。
- 建议：(1) 增加 treatment-dependent misclassification 的敏感性场景；(2) 考虑采用形式化的 partial identification 框架（如 Manski bounds）为 (A1) 违反下的 CATE 估计提供保守但有效的区间。

**W5** [warning] Plug-in SE 系统性欠覆盖未得到充分处理

- 具体位置：Appendix Y, page 25; Section 4.3
- 问题：Plug-in SE 聚合覆盖率 93.8%，系统性低于名义 95%。在高误差子群中欠覆盖更严重（92.5%），因为 C^{−1} 放大了估计不确定性。论文建议 n_expert ≥ 50 时用 bootstrap，但缺乏形式化的选择准则。Appendix Y 的 Table 22 显示 bootstrap 在小 n_expert 时将 CI 宽度增加 2-3×，但未讨论这种 power loss 的实际影响。
- 建议：给出 plug-in vs bootstrap 的形式化决策规则（如基于 κ(Ĉ_s) 或 n_expert/K 的显式阈值），而非笼统建议。

---

## 小问题（不影响接收）

- **符号冲突**：Appendix E (page 13) DGP 公式中噪声项 ε 与混淆矩阵误差率 ε 使用相同符号。虽然上下文可区分，建议用不同符号（如 η 或 u）避免混淆。
- **Table 1 表注含糊**："RMSE exceeds Global" 的确切含义不够清晰——是指 EC-HTE 的 RMSE 超过 Global 的配置，还是所有方法的 RMSE 相对于 Global 的比较？建议改写为 "configurations where EC-HTE RMSE > Global RMSE"。
- **Debiasing 术语使用不一致**：Footnote 1 定义 debiasing 特指标注误差纠正，但正文部分段落未加引号使用，可能引起与 algorithmic fairness debiasing 的混淆。
- **Appendix S 表述过于绝对**："EC-HTE reduces R-learner |bias| by 89%" 建议加上置信区间或标准误。
- **Corollary 4 假设过强**：uniform off-diagonal misclassification 在 K>2 多类别场景中很少成立。虽然论文标注了这一限制，但对 non-uniform 情形的退化行为未讨论。

---

## 主要优势

1. **核心定理正确且有深刻洞察力**：Theorem 1 的偏差分解恒等式 bias(z,s) = [M^{−1}_global · M_s − I]_{z,.} · τ 是精确的 population-level identity（非渐近近似）。将偏差分解为 δ_s（子群误差偏差）× Δτ（处理效应异质性）× 1/(1−2ε)（放大因子）的乘积结构既优雅又有实际意义。我独立验证了 Appendix B 的矩阵代数推导，确认核心证明无误。R² ≥ 0.97 跨 11 个 LLM-数据集组合的经验验证进一步增强了可信度。

2. **实验验证的彻底性罕见**：29 个附录系统覆盖了：MCMC 收敛诊断（Appendix G）、SE 覆盖率校准（Appendix Y）、五项假设逐条敏感性分析（Appendix Z.1-Z.6）、多种下游估计器兼容性（DIM, CausalForest, R-learner, IPW-DIM）、真实 LLM 混淆矩阵验证（11 模型-数据集组合）、以及 PPCI 互补性分析（Appendix L）。这种程度的彻底性在顶会论文中少见。

3. **Δτ-free 诊断有独立价值**：Proposition 3 允许从业者仅通过比较子群误差率（无需估计处理效应）判断全局纠正是否有害。AUC = 0.86 的诊断准确率在 pilot 阶段有实用价值，且论文正确指出这一诊断可在不采用 EC-HTE 的情况下独立使用（Section 5.4）。

4. **层次贝叶斯混淆矩阵估计设计精良**：Dirichlet-Multinomial 分层模型的 James-Stein 收缩效应在小样本子群中降低方差，在大样本子群中保留异质性。κ > 100 奇异性保护经全面验证（实际最大 κ = 1.845，53× 安全余量；sweeping κ ∈ {10, 25, 50, 100, 200, 500, 1000} 所有值产生同样结果）。收敛诊断指标优异（R̂ < 1.0034, ESS > 1618, 零发散转换）。

5. **与 PPCI 互补而非竞争**：论文展示 EC-HTE 纠正标注误差（label error），PPCI 纠正协变量误差（covariate error），二者独立且可叠加。合并后偏差从 0.179 降至 0.007（Appendix L），且论文用 4-DGP 正交设计验证了互补性的结构化原因。这增加了方法的实际部署价值。

---

## Questions for Authors

1. 请确认 Section 3 page 5 中 Proposition 3 低误差子群条件的不等号方向：应为 ε_s < ε/(2(1−ε)) 还是 ε_s > ε/(2(1−ε))？我的推导和后文 "low-error subgroups are over-corrected" 的表述均指向 ε_s < 0.088 受损。

2. Appendix X Table 21 中 κ ≤ 1.25 的阈值来源是什么？它与 Algorithm 1 的 κ > 100 fallback 之间的关系如何？是否有介于两者之间的实用阈值可以推荐？

3. 在 Assumption (A1) 违反场景中，是否考虑过 treatment-dependent misclassification（处理组标注准确率 ≠ 对照组）的敏感性分析？这在药物RCT的标注任务中是常见的违反模式。

4. 论文使用 100 次 Monte Carlo run。Appendix Q 给出 MCSE < 3.2%，但对于检测不同方法间 RMSE 差异 < 0.01 的统计效力是否充足？是否考虑过 power analysis？

---

## Missing References

论文引用覆盖面广，未发现重大遗漏。以下可能值得补充但非必须：

- Cinelli & Hazlett (2020) "Making sense of sensitivity" — 形式化敏感性分析框架，可用于 (A1) 敏感性分析
- Manski (2003) "Partial Identification of Probability Distributions" — partial identification 方法，与 Assumption (A1) 不可检验性相关
- Stewart & Sun (1990) "Matrix Perturbation Theory" — 支撑有限样本矩阵求逆误差传播分析

---

## 格式合规性检查（EMNLP 2026）

- ✅ 正文 ≤ 8 页（Sections 1-6 在 page 8 内结束）
- ✅ Abstract ≤ 200 words（约 170-190 words）
- ✅ Limitations 章节存在且不计入页数
- ✅ Double-blind（"Anonymous ACL submission"）
- ✅ ACL style template

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-23T13:29:35.821262+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：Reviewer 2 的 Must-Fix 和 Should-Fix 与你的发现是否一致或互补。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿报告 — Round 1（新颖性/完整性）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] **Theorem 1 与 Frazis & Loewenstein (2003) scalar attenuation 的区分在正文中不够充分**\n- 具体位置：Section 2 第 3 段（\"Three distinctions separate our contribution...\"）；Appendix Z.4\n- 问题：论文声称与 F-L (2003) 有三点区别：(i) mismeasured variable 是 effect modifier 而非 standard regressor；(ii) misclassification rates vary across subgroups 产生 δ_s·Δτ product structure；(iii) bias 来源于 correction procedure 而非 misclassification 本身。这些区分是正确的，但正文处理仅约 5 行。Appendix Z.4（Table 29）提供了有说服力的经验对比（F-L per-subgroup overcorrects high-error subgroups，F-L global 的 aggregate bias 高于 uncorrected estimator），但这一关键对比被放在 17 页附录的最后，审稿人很可能不会读到。\n- 建议修改方向：在 Section 2 或 Section 3 增加一段正式对比（~4-5 sentences），明确说明：(a) F-L 分析的是 misclassification 的 attenuation effect，而 Theorem 1 分析的是 *correction procedure* 引入的 new bias；(b) δ_s · Δτ product structure 在 F-L 框架中不存在；(c) 引入 Appendix Z.4 的关键经验结果（F-L scalar 在 aggregate 层面表现更差）。\n\n**N2** [critical] **核心贡献的定位模糊——bias mechanism discovery vs. method**\n- 具体位置：Section 1 contributions list；Abstract\n- 问题：论文同时声称三个贡献（bias identity、diagnostic、EC-HTE method），但未明确表态哪个是 *primary* contribution。从技术深度看，Theorem 1 + Proposition 3 是主要理论贡献，EC-HTE 是 practical instantiation。但 abstract 和 title 给人的印象是方法（EC-HTE）是核心。这种定位模糊使得 reviewer 难以准确评估 novelty。\n- 建议修改方向：在 Introduction 末尾明确声明 primary contribution 是 bias mechanism discovery（Theorem 1 + Proposition 3），EC-HTE 是 instantiation。\n\n### Should-Fix 问题\n\n**W1** [warning] **缺乏真实因果 ground truth 验证**\n- 所有实验使用 synthetic 或 semi-synthetic treatment effects。论文坦承 \"We leave full real-data validation... to future work\"。\n- 建议：在 Limitations 中更详细论证 semi-synthetic 设计是 real causal validation 的合理 proxy。\n\n**W2** [warning] **HB partial pooling 相对于 Dawid-Skene / Paun et al. 的新颖性未充分阐明**\n- Section 4.1 的 hierarchical Bayes confusion matrix estimator 使用标准 Dirichlet-Multinomial 模型。James-Stein shrinkage effect 是 well-known 的。贡献在于应用场景而非方法本身。\n- 建议：在 Section 4.1 明确将 HB 定位为 \"known technique, novel application context\"。\n\n**W3** [warning] **Assumption (A1) 对 LLM text annotation 的现实性需要更多讨论**\n- (A1) 假设 misclassification 仅依赖于 true label Z 和 subgroup S，不依赖于 potential outcomes Y(0), Y(1)。对于 LLM text classification，使注释困难的特征可能与 treatment effects 相关。\n- Appendix Z.2 测试了 outcome-dependent misclassification，EC-HTE 保持 ≥93.5% coverage，这令人放心。但测试的违反函数是特定形式。\n\n**W4** [warning] **Scalability to K >> 4 未充分讨论**\n- EC-HTE 主要在 K=2 和 K=4 上测试。真实 NLP 应用中 K 可能迅速增长。\n- 建议：讨论 hierarchical subgroup merging 或 adaptive budget allocation 的可能性。\n\n**W5** [warning] **Abstract 信息过密**\n- Abstract 约 175 words，在限制内，但塞入大量数值信息。\n\n### 小问题\n- Figure 1 字体偏小\n- Remark 2 与 Appendix J asymmetric extension 的表述需对齐\n- 部分引用使用 arXiv 版本而非已发表版本\n- Table 1 标题 \"extreme heterogeneity\" 可能被误读为 cherry-picking\n- Footnote 1 的重要区分放在脚注容易被忽略\n\n### Missing References\n1. Ratner et al. (2017/2020) Data Programming / Snorkel\n2. Hébert-Johnson et al. (2018) Multicalibration\n3. Lu et al. (2022) prompt sensitivity\n4. Miao et al. (2018) / Tchetgen Tchetgen et al. (2024) proximal causal inference",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：Reviewer 2 的 Must-Fix 和 Should-Fix 与你的发现是否一致或互补。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿报告 — Round 1（新颖性/完整性）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] **Theorem 1 与 Frazis & Loewenstein (2003) scalar attenuation 的区分在正文中不够充分**\n- 具体位置：Section 2 第 3 段（\"Three distinctions separate our contribution...\"）；Appendix Z.4\n- 问题：论文声称与 F-L (2003) 有三点区别：(i) mismeasured variable 是 effect modifier 而非 standard regressor；(ii) misclassification rates vary across subgroups 产生 δ_s·Δτ product structure；(iii) bias 来源于 correction procedure 而非 misclassification 本身。这些区分是正确的，但正文处理仅约 5 行。Appendix Z.4（Table 29）提供了有说服力的经验对比（F-L per-subgroup overcorrects high-error subgroups，F-L global 的 aggregate bias 高于 uncorrected estimator），但这一关键对比被放在 17 页附录的最后，审稿人很可能不会读到。\n- 建议修改方向：在 Section 2 或 Section 3 增加一段正式对比（~4-5 sentences），明确说明：(a) F-L 分析的是 misclassification 的 attenuation effect，而 Theorem 1 分析的是 *correction procedure* 引入的 new bias；(b) δ_s · Δτ product structure 在 F-L 框架中不存在；(c) 引入 Appendix Z.4 的关键经验结果（F-L scalar 在 aggregate 层面表现更差）。\n\n**N2** [critical] **核心贡献的定位模糊——bias mechanism discovery vs. method**\n- 具体位置：Section 1 contributions list；Abstract\n- 问题：论文同时声称三个贡献（bias identity、diagnostic、EC-HTE method），但未明确表态哪个是 *primary* contribution。从技术深度看，Theorem 1 + Proposition 3 是主要理论贡献，EC-HTE 是 practical instantiation。但 abstract 和 title 给人的印象是方法（EC-HTE）是核心。这种定位模糊使得 reviewer 难以准确评估 novelty。\n- 建议修改方向：在 Introduction 末尾明确声明 primary contribution 是 bias mechanism discovery（Theorem 1 + Proposition 3），EC-HTE 是 instantiation。\n\n### Should-Fix 问题\n\n**W1** [warning] **缺乏真实因果 ground truth 验证**\n- 所有实验使用 synthetic 或 semi-synthetic treatment effects。论文坦承 \"We leave full real-data validation... to future work\"。\n- 建议：在 Limitations 中更详细论证 semi-synthetic 设计是 real causal validation 的合理 proxy。\n\n**W2** [warning] **HB partial pooling 相对于 Dawid-Skene / Paun et al. 的新颖性未充分阐明**\n- Section 4.1 的 hierarchical Bayes confusion matrix estimator 使用标准 Dirichlet-Multinomial 模型。James-Stein shrinkage effect 是 well-known 的。贡献在于应用场景而非方法本身。\n- 建议：在 Section 4.1 明确将 HB 定位为 \"known technique, novel application context\"。\n\n**W3** [warning] **Assumption (A1) 对 LLM text annotation 的现实性需要更多讨论**\n- (A1) 假设 misclassification 仅依赖于 true label Z 和 subgroup S，不依赖于 potential outcomes Y(0), Y(1)。对于 LLM text classification，使注释困难的特征可能与 treatment effects 相关。\n- Appendix Z.2 测试了 outcome-dependent misclassification，EC-HTE 保持 ≥93.5% coverage，这令人放心。但测试的违反函数是特定形式。\n\n**W4** [warning] **Scalability to K >> 4 未充分讨论**\n- EC-HTE 主要在 K=2 和 K=4 上测试。真实 NLP 应用中 K 可能迅速增长。\n- 建议：讨论 hierarchical subgroup merging 或 adaptive budget allocation 的可能性。\n\n**W5** [warning] **Abstract 信息过密**\n- Abstract 约 175 words，在限制内，但塞入大量数值信息。\n\n### 小问题\n- Figure 1 字体偏小\n- Remark 2 与 Appendix J asymmetric extension 的表述需对齐\n- 部分引用使用 arXiv 版本而非已发表版本\n- Table 1 标题 \"extreme heterogeneity\" 可能被误读为 cherry-picking\n- Footnote 1 的重要区分放在脚注容易被忽略\n\n### Missing References\n1. Ratner et al. (2017/2020) Data Programming / Snorkel\n2. Hébert-Johnson et al. (2018) Multicalibration\n3. Lu et al. (2022) prompt sensitivity\n4. Miao et al. (2018) / Tchetgen Tchetgen et al. (2024) proximal causal inference",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-23T13:30:07.645202+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31823
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-23T13:30:07.896868+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：Reviewer 1 的 Must-Fix 和 Should-Fix 与你的发现是否一致或互补。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿报告 — 方法严谨性审查\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Proposition 3 文字解读中不等号方向疑似错误\n- 具体位置：Section 3, page 5, Proposition 3 后的解读段落\n- 问题：Proposition 3 的形式化条件 |δ_s|/((1−2ε)·ε_s) > 1 本身是正确的。但后续文字解读声称 \"any subgroup with ε_s > ε/(2(1−ε)) ≈ 0.088 is harmed\"。\n- R1 独立推导：\n  - Case 1（低误差子群 ε_s < ε, δ_s < 0）：条件化简为 ε_s < ε/(2(1−ε))。即 ε_s < 0.088 时子群受损（过度纠正）。\n  - Case 2（高误差子群 ε_s > ε, δ_s > 0）：条件化简为 ε_s > 0.5（近随机分类，被 A4 排除）。\n  - 代数验证确认 ε_s < 0.088 方向正确，与 \"ε_s > 0.088 受损\" 矛盾。\n- 为什么影响接收：Proposition 3 是论文三大贡献之一。解读方向错误会误导从业者的纠正决策。\n\n**N2** [critical] 实际 LLM 混淆矩阵中无配置通过全部适用性筛选条件\n- 具体位置：Appendix X, page 24, Table 21\n- 问题：16 个 LLM-数据集-K 组合中无一通过全部三个筛选条件（Proposition 3 诊断、κ(C_s) ≤ 1.25、专家预算充分性）。瓶颈是 κ(C_s) ≤ 1.25。\n- 放松条件后 EC-HTE 在 79%（41/52）配置中优于 Global correction，但这与主文宣称的严格诊断驱动工作流不一致。\n- κ ≤ 1.25 与 Algorithm 1 的 κ > 100 fallback 之间差距 80×，关系需解释。\n- 建议：提供实用化的分层筛选阈值（如 κ ≤ 2 或 κ ≤ 5）。\n\n### Should-Fix 问题\n\n**W1** [warning] 二元效应修饰变量假设（A3）限制适用范围\n- Z ∈ {0,1} 且 P(Z=1) = 0.5 限制了泛化性。Corollary 4 扩展到多类别但假设 uniform off-diagonal misclassification。\n- 建议：至少讨论连续 Z 下偏差分解的理论形式。\n\n**W2** [warning] 有限样本分析缺乏正式理论推导\n- R_s = O_p(n^{−1/2}_expert) 未给出推导。从 population identity 到 finite-sample estimator 的过渡是关键步骤。\n- 建议：补充 delta method 推导或矩阵扰动理论分析。\n\n**W3** [warning] Frazis-Loewenstein 标量衰减纠正未在主文中比较\n- F-L 仅在 Appendix Z.4 讨论。主文 baselines 中缺少这一最直接的理论对照。\n- Appendix Z.4 显示 F-L per-subgroup 覆盖率达 95.3% 但 over-corrects high-error subgroups。\n- 建议：在 Table 1 中加入 F-L 比较。\n\n**W4** [warning] Assumption (A1) 敏感性分析范围有限\n- 仅考虑一种违反形式（outcome-dependent misclassification，γ ∈ [0, 0.20]）。\n- 未覆盖 treatment-dependent misclassification。\n- 建议：增加 treatment-dependent misclassification 场景；考虑 partial identification 框架。\n\n**W5** [warning] Plug-in SE 系统性欠覆盖未得到充分处理\n- Plug-in SE 聚合覆盖率 93.8%，高误差子群 92.5%。\n- 建议：给出 plug-in vs bootstrap 的形式化决策规则。\n\n### 小问题\n- Appendix E 噪声符号 ε 与误差率 ε 冲突\n- Table 1 表注含糊\n- Debiasing 术语不一致\n- Appendix S \"89% reduction\" 缺置信区间\n- Corollary 4 uniform off-diagonal 假设过强\n\n### Missing References\n- Cinelli & Hazlett (2020) — 形式化敏感性分析\n- Manski (2003) — partial identification\n- Stewart & Sun (1990) — matrix perturbation theory",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：Reviewer 1 的 Must-Fix 和 Should-Fix 与你的发现是否一致或互补。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿报告 — 方法严谨性审查\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Proposition 3 文字解读中不等号方向疑似错误\n- 具体位置：Section 3, page 5, Proposition 3 后的解读段落\n- 问题：Proposition 3 的形式化条件 |δ_s|/((1−2ε)·ε_s) > 1 本身是正确的。但后续文字解读声称 \"any subgroup with ε_s > ε/(2(1−ε)) ≈ 0.088 is harmed\"。\n- R1 独立推导：\n  - Case 1（低误差子群 ε_s < ε, δ_s < 0）：条件化简为 ε_s < ε/(2(1−ε))。即 ε_s < 0.088 时子群受损（过度纠正）。\n  - Case 2（高误差子群 ε_s > ε, δ_s > 0）：条件化简为 ε_s > 0.5（近随机分类，被 A4 排除）。\n  - 代数验证确认 ε_s < 0.088 方向正确，与 \"ε_s > 0.088 受损\" 矛盾。\n- 为什么影响接收：Proposition 3 是论文三大贡献之一。解读方向错误会误导从业者的纠正决策。\n\n**N2** [critical] 实际 LLM 混淆矩阵中无配置通过全部适用性筛选条件\n- 具体位置：Appendix X, page 24, Table 21\n- 问题：16 个 LLM-数据集-K 组合中无一通过全部三个筛选条件（Proposition 3 诊断、κ(C_s) ≤ 1.25、专家预算充分性）。瓶颈是 κ(C_s) ≤ 1.25。\n- 放松条件后 EC-HTE 在 79%（41/52）配置中优于 Global correction，但这与主文宣称的严格诊断驱动工作流不一致。\n- κ ≤ 1.25 与 Algorithm 1 的 κ > 100 fallback 之间差距 80×，关系需解释。\n- 建议：提供实用化的分层筛选阈值（如 κ ≤ 2 或 κ ≤ 5）。\n\n### Should-Fix 问题\n\n**W1** [warning] 二元效应修饰变量假设（A3）限制适用范围\n- Z ∈ {0,1} 且 P(Z=1) = 0.5 限制了泛化性。Corollary 4 扩展到多类别但假设 uniform off-diagonal misclassification。\n- 建议：至少讨论连续 Z 下偏差分解的理论形式。\n\n**W2** [warning] 有限样本分析缺乏正式理论推导\n- R_s = O_p(n^{−1/2}_expert) 未给出推导。从 population identity 到 finite-sample estimator 的过渡是关键步骤。\n- 建议：补充 delta method 推导或矩阵扰动理论分析。\n\n**W3** [warning] Frazis-Loewenstein 标量衰减纠正未在主文中比较\n- F-L 仅在 Appendix Z.4 讨论。主文 baselines 中缺少这一最直接的理论对照。\n- Appendix Z.4 显示 F-L per-subgroup 覆盖率达 95.3% 但 over-corrects high-error subgroups。\n- 建议：在 Table 1 中加入 F-L 比较。\n\n**W4** [warning] Assumption (A1) 敏感性分析范围有限\n- 仅考虑一种违反形式（outcome-dependent misclassification，γ ∈ [0, 0.20]）。\n- 未覆盖 treatment-dependent misclassification。\n- 建议：增加 treatment-dependent misclassification 场景；考虑 partial identification 框架。\n\n**W5** [warning] Plug-in SE 系统性欠覆盖未得到充分处理\n- Plug-in SE 聚合覆盖率 93.8%，高误差子群 92.5%。\n- 建议：给出 plug-in vs bootstrap 的形式化决策规则。\n\n### 小问题\n- Appendix E 噪声符号 ε 与误差率 ε 冲突\n- Table 1 表注含糊\n- Debiasing 术语不一致\n- Appendix S \"89% reduction\" 缺置信区间\n- Corollary 4 uniform off-diagonal 假设过强\n\n### Missing References\n- Cinelli & Hazlett (2020) — 形式化敏感性分析\n- Manski (2003) — partial identification\n- Stewart & Sun (1990) — matrix perturbation theory",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-23T13:30:09.311518+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1414
}
```

</details>

---


### Assistant

_source line 1066 · 2026-05-23T13:30:17.948200+00:00_

交叉分享已发出，等待两位 Reviewer 逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 1067 · 2026-05-23T13:30:20.516055+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心发现摘要：**

- **Overall: 3.5 (Borderline Conference)**
- **Soundness: 4/5** — Theorem 1 证明正确，R²≥0.97 验证充分
- **两个 Must-Fix 问题：**
  1. Proposition 3 的文字解读中不等号方向疑似有误——我的独立代数推导表明低误差子群（ε_s < 0.088）受损，而非 ε_s > 0.088
  2. 16 个真实 LLM 配置中无一通过论文自身提出的全部适用性筛选条件（κ≤1.25 过严），削弱实际价值论证
- **五个 Should-Fix 问题：** 二元 Z 限制、有限样本分析不正式、F-L 比较缺失、(A1) 敏感性分析范围窄、plug-in SE 系统性欠覆盖
- **主要优势：** 核心定理正确优雅、29 个附录的验证彻底性罕见、Δτ-free 诊断有独立实用价值、HB 估计器设计精良、与 PPCI 互补性展示增加方法价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1068 · 2026-05-23T13:30:31.438025+00:00_

收到 Reviewer 1 初审报告。等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1069 · 2026-05-23T13:31:45.699522+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条评议

---

### Must-Fix 问题

**[AGREE] R2-N1: Frazis-Loewenstein 对比不足**

同意，且与我的 W3 完全一致。我在审稿中也独立指出 F-L 比较被放在 Appendix Z.4 是一个结构性问题。补充两点：

(1) Appendix Z.4 的经验结果实际上**有力支撑**了论文的核心论点——F-L scalar 在 aggregate 层面甚至比 uncorrected estimator 更差，F-L per-subgroup 虽然覆盖率达 95.3% 但 dramatically over-corrects high-error subgroups。这些结果如果放在主文，能显著增强论文的说服力。

(2) R2 提到的三点区分（effect modifier vs regressor、δ_s·Δτ product structure、correction-induced bias vs attenuation bias）在理论上是准确的。特别是第(c)点——Theorem 1 分析的是**纠正程序本身引入的新偏差**，而非 misclassification 的衰减效应——这是论文最本质的理论区分，值得在 Section 2 或 Section 3 开头用 1-2 句话明确点出。

---

**[REBUT] R2-N2: 贡献定位模糊**

不同意将此列为 Must-Fix。理由：

(1) 论文 Introduction (page 2) 的贡献列表已按理论重要性排序：Theorem 1（bias identity）→ Proposition 3（diagnostic）→ EC-HTE（method）。这个顺序本身就暗示了 primary contribution 是理论发现。

(2) 论文标题 "When LLM Annotation Debiasing Hurts" 强调的是**现象/机制发现**，而非方法名称。如果方法是核心贡献，标题会是 "EC-HTE: Error-Corrected Heterogeneous Treatment Effects" 之类。

(3) Abstract 中 Theorem 1 和 Proposition 3 占据前半段，EC-HTE 出现在后半段作为 practical solution，结构上已体现了理论优先。

(4) 在 NLP/CL 社区，读者通常期望论文既有理论发现又有可用方法。要求作者明确声明"method is secondary"反而可能降低对实践导向 reviewer 的吸引力。

建议：降为 Minor。如果作者愿意，可在 Introduction 末尾加一句 "Our primary contribution is the bias mechanism discovery; EC-HTE instantiates this insight" 但这不应是接收条件。

---

### Should-Fix 问题

**[AGREE] R2-W1: 缺乏真实因果 ground truth**

同意这是一个合理关切。但需要指出，这是该领域（measurement error in causal inference）的**结构性限制**，而非本文特有的缺陷：

- 真实因果 ground truth 需要 RCT + ground-truth labels + known subgroup-specific misclassification rates 同时存在，这在实际中极为罕见。
- 论文的 semi-synthetic 设计（real text features → real LLM confusion matrices → synthetic treatment effects）是该领域的标准做法（cf. Kennedy 2023, Angelopoulos et al. 2023）。
- Appendix M 的 hate speech case study 和 Appendix V 的 Civil Comments 验证提供了一定程度的真实数据接触，虽然处理效应仍是合成的。

建议作者在 Limitations 中增加 1-2 句话，解释 semi-synthetic 设计为何是 causal validation 的合理 proxy（如：保留了真实 LLM 误差结构，同时允许 ground-truth CATE 的精确计算）。

---

**[AGREE] R2-W2: HB partial pooling 相对于 Dawid-Skene 的新颖性**

完全同意。Section 4.1 的 Dirichlet-Multinomial 分层模型是标准技术，James-Stein shrinkage 是 well-known 效应。论文的贡献在于：(a) 将其应用于 per-subgroup confusion matrix estimation 这一特定场景；(b) 与下游 CausalForest 的方差传播衔接。这应该在 Section 4.1 开头就明确说明，而非让读者去猜测方法新颖性在哪里。

不过，我要补充的是，HB 估计在论文中的**工程价值**不应被低估：κ>100 奇异性保护（Appendix A.1 验证了 53× safety margin）、收敛诊断标准（R̂ < 1.0034）、以及与 CausalForest variance-adjusted SE 的衔接设计，都是扎实的工程贡献，即使理论上不新颖。

---

**[AGREE] R2-W3: Assumption (A1) 现实性**

同意，且与我的 W4 互补。R2 的关注点更具体："使注释困难的特征可能与 treatment effects 相关"——这是一个在 LLM text annotation 场景下非常合理的担忧。例如，如果 treatment 是政策干预，而 LLM 对涉及该政策的复杂文本更容易误标注，则 (A1) 被违反。

我的 W4 关注的是敏感性分析的**覆盖范围**（仅 outcome-dependent 一种违反形式），R2 关注的是 (A1) 在 **LLM annotation 特定场景下的合理性**。两者互补，合并后对作者的要求是：(1) 增加 treatment-dependent misclassification 的敏感性测试；(2) 在 Section 4 或 Limitations 中讨论 LLM 特有的 (A1) 违反模式。

---

**[AGREE] R2-W4: Scalability to K >> 4**

同意。我的审稿也注意到 per-subgroup expert labels 的预算随 K 线性增长。Appendix I（Expert Budget Crossover Curves）显示 K=4 时每子群约需 30 labels 才能使 EC-HTE 优于 Global——对于 K=10，这意味着 300+ expert labels，成本可能不可接受。

R2 建议的 "hierarchical subgroup merging" 和 "adaptive budget allocation" 是合理的扩展方向。论文的 HB 模型实际上已经暗含了 merging 的思路（通过 shrinkage 将数据不足的子群拉向全局均值），但没有显式讨论何时应该合并子群。

---

**[REBUT] R2-W5: Abstract 信息过密**

不同意。理由：

(1) Abstract 约 175 words，距 200-word 限制有余量。对于包含理论结果 + 诊断 + 方法 + 实验验证的论文，这一信息密度是合理的。

(2) Abstract 中的数值信息（R² ≥ 0.97, 50% of configurations, AUC = 1.0）直接量化了核心 claim，比模糊的定性描述（"substantially reduces bias"）更有信息量。

(3) 对比同类论文（如 Angelopoulos et al. 2023 PPI, Kennedy 2023 DR-learner），数值密集的 abstract 在 CL/ML 社区是常态。

建议：降为不影响接收的风格偏好，无需修改。

---

### 小问题

**[AGREE]** Figure 1 字体偏小 — 同意，但这是排版问题。

**[AGREE]** Remark 2 与 Appendix J 表述需对齐 — 同意，我也注意到 Remark 2 提到 "algebraically equivalent" 但 Appendix J 的 asymmetric formula 有额外的 (FPR, FNR) 参数，技术上不完全等价。

**[AGREE]** 部分引用使用 arXiv 版本 — 同意，应更新为已发表版本。

**[AGREE]** Table 1 标题 "extreme heterogeneity" 可能被误读为 cherry-picking — 同意这个 framing risk。但论文在 Table 7（Appendix K）提供了 moderate heterogeneity 结果，且 Table 1 标题中有 "Moderate heterogeneity... in Table 7" 的指引。建议改为 "Main results under extreme and moderate heterogeneity" 合并两张表，或改标题为 "Main results (high Δτ regime)"。

**[AGREE]** Footnote 1 的重要区分放在脚注容易被忽略 — 同意。"debiasing" 的定义区分（annotation error correction vs algorithmic fairness）应在正文中明确，而非藏在脚注。

---

### Missing References 评议

**[REBUT] Ratner et al. (2017/2020) Data Programming / Snorkel**: Data programming 处理的是多弱标注源聚合（label aggregation），本文处理的是单 LLM 标注器的子群混淆矩阵纠正用于因果推断。问题设置不同——Snorkel 不涉及处理效应估计，也不分析纠正程序引入的偏差。引用不必要。

**[PARTIALLY AGREE] Hébert-Johnson et al. (2018) Multicalibration**: Multicalibration 要求预测器在所有可识别子群上校准。这与论文的子群特异性混淆矩阵纠正有概念相似性（都关注子群层面的公平/准确性），但技术框架完全不同（calibration vs confusion matrix inversion）。可在 Related Work 一句话提及作为更广泛的 subgroup-fairness 文献背景，但不是必须的。

**[REBUT] Lu et al. (2022) prompt sensitivity**: Prompt sensitivity 影响 LLM 标注质量，但这是上游问题。本文的框架将 LLM 标注误差视为给定的混淆矩阵，不关心误差的来源。Lu et al. 的工作属于 "如何减少标注误差"，本文属于 "给定标注误差如何纠正下游推断"，二者正交。

**[AGREE] Miao et al. (2018) / Tchetgen Tchetgen et al. (2024) proximal causal inference**: 同意这是一个有价值的引用。Proximal causal inference 使用 proxy variables 进行因果识别，LLM 标注可以被视为 true label 的 proxy。论文的混淆矩阵求逆框架与 proximal CI 的 bridge function 有结构相似性。在 Related Work 中建立这一联系可以增强论文对 causal inference 社区读者的吸引力。但需注意，proximal CI 通常假设两个 proxies（treatment proxy + outcome proxy），而本文只有一个 outcome proxy（LLM annotation），所以直接套用 proximal CI 框架不完全适用。

---

### 综合评议

R2 的审稿与我的审稿在多个维度互补：

| 议题 | R1 (我) | R2 | 关系 |
|------|---------|-----|------|
| F-L 对比不足 | W3 (Should-Fix) | N1 (Must-Fix) | 一致，R2 更严格 |
| Proposition 3 不等号 | N1 (Must-Fix) | 未提及 | R1 独有 |
| 适用性筛选过严 | N2 (Must-Fix) | 未提及 | R1 独有 |
| 贡献定位 | 未提及 | N2 (Must-Fix) | R2 独有，我认为应降级 |
| (A1) 敏感性 | W4 (Should-Fix) | W3 (Should-Fix) | 互补（范围 vs 现实性）|
| 二元 Z 限制 | W1 (Should-Fix) | 未提及 | R1 独有 |
| 有限样本分析 | W2 (Should-Fix) | 未提及 | R1 独有 |
| 真实 ground truth | 未提及 | W1 (Should-Fix) | R2 独有 |
| HB 新颖性 | 未提及 | W2 (Should-Fix) | R2 独有 |
| Scalability | 隐含于讨论 | W4 (Should-Fix) | R2 更明确 |

**合并后的核心问题优先级**：
1. [R1-N1] Proposition 3 不等号方向验证 — 影响核心贡献可信度
2. [R1-N2] 适用性筛选条件与实际 LLM 的 gap — 影响实际价值论证
3. [R1-W3 + R2-N1] F-L 对比移入主文 — 影响新颖性论证
4. [R1-W4 + R2-W3] (A1) 敏感性分析扩展 — 影响 soundness

我维持 **Overall 3.5 (Borderline Conference)** 的评分。R2 的意见没有改变我对论文技术质量的判断——核心理论正确，实验全面，但存在需要解决的方法论问题（特别是我的 N1 和 N2）。R2 的 N2（贡献定位）我不认为是 critical issue。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1070 · 2026-05-23T13:32:01.927152+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1071 · 2026-05-23T13:32:04.450623+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。逐条评议了 R2 的全部 Must-Fix、Should-Fix、小问题和 Missing References，标注了 [AGREE]/[REBUT]/[PARTIALLY AGREE]，并附上了与我自己发现的交叉对比表和合并后的优先级排序。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1072 · 2026-05-23T13:32:11.196395+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 102

## Round 102

10 recorded events


### User

_source line 1073 · 2026-05-23T13:34:44.477032+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1

---

### Must-Fix 问题

**[REBUT] R1-N1: Proposition 3 不等号方向疑似错误**

我以 165 DPI 重新渲染了 page 5 并逐字核对。论文原文为：

> "For low-error subgroups (ε_s < ε, δ_s < 0), it holds whenever ε_s < ε/(2(1 − ε))—easily satisfied: when ε = 0.15, any subgroup with ε_s < 0.088 is harmed."

文中使用的是 **"ε_s < 0.088"**（小于号），与代数推导一致：低误差子群在 ε_s 低于阈值时被过度纠正。R1 引用的 "ε_s > ε/(2(1−ε)) ≈ 0.088" 似为误读——原文不等号方向为 "<" 而非 ">"。

R1 的独立代数推导本身是正确的（Case 1: ε_s < ε/(2(1−ε))），且与论文原文一致，并无矛盾。

**但 R1 提出的 clarity concern 有价值**：这段文字信息密度很高，将两个 case 压缩在一段中，容易引起歧义。建议作者将 high-error case 和 low-error case 分开为两个明确的条目（如 bullet points），避免误读。

**结论：数学无误，但呈现可改进。不应作为 Must-Fix，可降级为 Minor（writing clarity）。**

---

**[AGREE] R1-N2: 无实际 LLM 配置通过全部适用性条件**

我重新阅读了 page 24 的 Table 21 和下方文字。论文自身确认："No combination passes all three conditions; the bottleneck is κ(C_s) ≤ 1.25, which requires FPR_s + FNR_s ≤ 0.20 for all subgroups—a threshold no current LLM achieves uniformly."

这是一个实质性问题。论文在 Section 5.4 中建立了一套诊断驱动的工作流（先检查 Proposition 3 → 检查 condition number → 检查 expert budget），但在真实 LLM 数据上，这套严格筛选从未被通过。放松条件后 EC-HTE 在 79%（41/52）配置中优于 Global，这证明了方法的实用性，但也意味着：

1. **严格诊断工作流在实践中是空集**——从业者实际上需要忽略 κ ≤ 1.25 条件才能使用 EC-HTE
2. **κ ≤ 1.25（screening）与 κ > 100（Algorithm 1 fallback）之间差距 ~80×**——论文未解释 1.25 到 100 之间的行为

R1 建议提供分层阈值（κ ≤ 2 或 κ ≤ 5）是好建议。这不需要新实验——Appendix G 的 condition number analysis 已有相关数据，只需重新呈现为分层推荐。

**补充 R1 未提到的一点**：论文 Appendix X 同时指出，在放松条件下 EC-HTE 仍然系统性地优于 stratified MLE（52/52 = 100%），这减轻了 N2 的严重程度。方法本身有效，只是推荐的适用性筛选阈值过于保守。

**建议修改方向**：(1) 提供 κ ∈ {1.25, 2, 5, 10} 的分层性能表；(2) 在 Section 5.4 或 Limitations 中承认严格条件是 sufficient 而非 necessary。

---

### Should-Fix 问题

**[AGREE] R1-W1: 二元 Z 假设限制适用范围**

Z ∈ {0,1} 且 P(Z=1) = 0.5 确实限制了适用性。在 NLP 应用中，effect modifier 通常是多类别甚至连续变量（如 sentiment score、toxicity level）。Corollary 4（Appendix C）扩展到 K > 2 个 effect-modifier levels，但假设 uniform off-diagonal misclassification——这对 LLM annotation 不现实（LLM 对相邻类别的混淆通常高于远距离类别）。

这与我的 W4（scalability to K >> 4）互补：W1 关注 effect modifier 维度的扩展性，W4 关注 subgroup 维度。两者共同指向同一个基本限制——论文的理论框架在低维离散设定下工作良好，但向高维/连续设定的扩展路径不清晰。

**建议**：至少讨论连续 Z 下的 bias decomposition 形式（即使不给出 full theorem），以及 non-uniform off-diagonal misclassification 对 Corollary 4 的影响。

---

**[AGREE] R1-W2: 有限样本分析缺乏正式理论推导**

这与我的 Q1 对应。论文在 Appendix Y 提供了 plug-in SE 和 bootstrap SE，但从 population-level bias identity（Theorem 1）到 finite-sample estimator 的过渡缺乏 formal rate。R1 建议的 delta method 或 matrix perturbation theory 是标准工具。

具体而言：Theorem 1 是 exact identity under (A1)-(A5)。当 confusion matrix 从 n_expert 个专家标签估计时，估计误差为 O_p(n_expert^{-1/2})。论文声称 R_s = O_p(n^{-1/2}_expert) 但未推导。Appendix Y 的 plug-in SE 经验验证了 coverage（93.8%），但 formal derivation 会使结论更有力。

**补充**：从实际影响看，这更多是 technical rigor 问题而非 correctness 问题——经验 coverage 接近 nominal，方法在实践中有效。对于 EMNLP 受众（而非 JASA/Biometrika），我认为这是 should-fix 而非 must-fix。

---

**[AGREE] R1-W3: Frazis-Loewenstein 未在主文比较**

与我的 N1 完全一致。F-L (2003) 是 Theorem 1 最直接的理论对照，仅放在 Appendix Z.4 是不够的。Appendix Z.4 Table 29 的关键发现（F-L per-subgroup over-corrects high-error subgroups；F-L global 的 aggregate bias 高于 uncorrected estimator）应进入主文。

R1 建议在 Table 1 中加入 F-L 比较——这是一个具体、可操作的建议，比我的 N1 更精确。我支持。在 Table 1 中增加 F-L scalar 和 F-L per-subgroup 两行，可以直接展示 Theorem 1 相对于经典结果的附加价值。

---

**[AGREE] R1-W4: Assumption (A1) 敏感性分析范围有限**

与我的 W3 一致。R1 更具体地指出了缺失的 violation 类型：treatment-dependent misclassification。论文 Appendix Z.2 仅测试了 outcome-dependent misclassification（P(Z=1) dependent on Y），但未测试 treatment-dependent misclassification（P(Z=1) dependent on T）。在 NLP 因果推断中，treatment assignment 可能影响 text features（例如 treatment group 的文本更正式），进而影响 LLM classification quality。

R1 建议的 partial identification 框架（Manski 2003）也是一个有建设性的方向——当 (A1) 违反时，point identification 可能不可能，partial identification 提供了 principled 的替代方案。

**补充我的 W3 未涵盖的点**：R1 的 treatment-dependent misclassification concern 更具实践相关性。在 RCT 中，treatment assignment 会系统性地改变文本特征（例如 treated 个体的 response 更正式），使得 LLM 在 treatment/control 组的 misclassification 率不同——这直接违反 (A1)。

---

**[AGREE] R1-W5: Plug-in SE 系统性欠覆盖**

我的审稿中未单独标记此问题，但 R1 的观察是正确的。Plug-in SE 的聚合覆盖率 93.8% 低于 nominal 95%，高误差子群 92.5% 更低。对于因果推断应用（尤其是 policy decisions），1-2% 的 under-coverage 是实质性的。

R1 建议的 formal decision rule（plug-in vs. bootstrap）是合理的。论文在 Appendix Y 提供了两种 SE 方法的比较，但缺乏明确的推荐——什么条件下用 plug-in（计算快但 under-covers），什么条件下用 bootstrap（准确但计算成本高）。

**建议**：以 n_expert 或 condition number κ(C_s) 为分界条件，给出 plug-in vs. bootstrap 的推荐规则。

---

### 小问题

**[AGREE] ε 符号冲突**：Appendix E 的 outcome noise ε 与 Section 3 的误差率 ε 确实冲突。应使用不同符号（如 σ_ε 或 η）。

**[AGREE] Table 1 表注含糊**：同意。我在小问题中也标记了 Table 1 标题的 "extreme heterogeneity" 修饰语可能被误读。

**[AGREE] Debiasing 术语不一致**：论文在脚注 1 中做了区分，但正文中有时将 debiasing 用于 fairness 语境。应统一术语。

**[AGREE] Appendix S "89% reduction" 缺置信区间**：这是一个定量声明，应提供不确定性度量。

**[AGREE] Corollary 4 uniform off-diagonal 过强**：与 W1 一致。

---

### Missing References

**[AGREE] Cinelli & Hazlett (2020)**：Omitted Variable Bias 的形式化敏感性分析框架。与 Assumption (A1) 的 sensitivity analysis 直接相关——如果将 outcome-dependent misclassification 视为一种 omitted variable，C&H 的 robustness value 框架可以量化 (A1) 违反需要多大才能逆转结论。好建议。

**[AGREE] Manski (2003)**：Partial identification 在 (A1) 不成立时提供了 principled alternative to point identification。与 R1-W4 的建议一致。

**[REBUT] Stewart & Sun (1990)**：Matrix perturbation theory 确实与 confusion matrix estimation error 的传播相关，但这是一个相当 technical 的参考。对于 EMNLP 受众，更自然的参考是 delta method（已在统计文献中标准化）或 bootstrap theory。不认为这是一个必须引用的 missing reference。

---

### 总结评估

R1 和我的审稿在以下方面高度一致：
1. **F-L 对比应进入主文**（R1-W3 ≈ R2-N1）
2. **Assumption (A1) 敏感性不够**（R1-W4 ≈ R2-W3）
3. **缺乏真实因果 ground truth**（R1 未单独标记，但隐含于 N2 的适用性讨论中 ≈ R2-W1）
4. **Overall 评分一致：3.5 Borderline Conference**

R1 和我的审稿互补之处：
- R1 更深入地审查了**技术细节**（Proposition 3 代数、condition number gap、plug-in SE coverage）
- 我更关注**新颖性定位和写作**（contribution positioning、abstract 信息密度、HB vs. Dawid-Skene 区分）

关于 R1-N1（Proposition 3 方向错误）：经我独立验证，**论文原文的不等号方向（ε_s < 0.088）是正确的**，与代数推导一致。R1 可能误读了不等号方向。但文本 clarity 确实可改进——建议降级为 Minor。

关于 R1-N2（无配置通过全部条件）：这是一个**实质性问题但非致命缺陷**。方法在放松条件下仍然有效（79% 优于 Global，100% 优于 Stratified MLE），说明 κ ≤ 1.25 阈值过于保守。关键修改是提供分层推荐阈值并承认 sufficient vs. necessary 的区别。

**我维持 Overall 3.5（Borderline Conference）不变。** 如果作者在 rebuttal 中能 (a) 澄清 Proposition 3 的 case analysis 格式，(b) 提供 condition number 的分层推荐，(c) 在 Table 1 中加入 F-L 对比，(d) 明确 primary contribution 定位，我倾向上调至 4.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-23T13:35:34.296772+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-23T13:35:34.297218+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T13:14:08.777164+00:00\", \"completed_at\": \"2026-05-23T13:18:42.850201+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-6\", \"message\": \"主文连续 4 页无 figure 或 table。Pages 4-6 有方程式提供视觉变化，但 page 3（Related Work）为纯文本。从 Figure 1（p2）到 Table 1（p7）跨度 4 页，审稿人可能感到视觉单调。建议在 Section 3（理论部分）或 Section 4（方法部分）增加一个概念图或流程图。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页仅 3 个 display items（Figure 1, Table 1, Figure 2）。该论文兼具理论和实证贡献，但大量实验结果（Tables 3-31, Figures 3-6）全部推入附录。审稿人在主文中只能看到 1 个结果表和 1 个结果图，可能质疑实验展示力度不足。建议将 1-2 个关键附录表/图提升至主文。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8-9\", \"message\": \"Limitations 章节过长——从 page 8 右栏底部延续到 page 9 大部分内容，约 1.5 栏文字。EMNLP 规定 Limitations 不计入页数限制但\\\"provided they do not contain excessive additional content\\\"。当前长度可能触发审稿人或 AC 对\\\"excessive content\\\"的质疑。建议精简到 3-4 个核心点（~0.5 栏）。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 出现在 page 2 顶部而非 page 1，这在 ACL 论文中常见且可接受。Figure 1 有效传达核心 bias 机制，是一个好的视觉锚点。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 heatmap 的 axis labels（Δπ, Δτ）和 colorbar 标注字号偏小，在打印时可能不够清晰。建议适当增大坐标轴标签字号。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 排版规范：使用 booktabs 风格，最优结果加粗，精度一致。符合顶会标准。\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"附录 Figure 3（ROC curves）面板内文字较小，但作为附录补充材料可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"附录 Figure 4（4-panel RMSE vs budget 线图）清晰可读，dashed vertical lines 标注 crossover points 是好的设计。\"}, {\"severity\": \"info\", \"dimension\": \"page 22\", \"message\": \"附录 Figure 5（applicability frontier）和 Figure 6（R-learner vs CausalForest）排版紧凑但可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 29\", \"message\": \"最后一页（Algorithm 1）约 60% 填充，底部约 40% 空白。作为附录末页可接受。\"}], \"counts\": {\"critical\": 0, \"warning
…[truncated 58 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-23T13:35:34.397911+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-23T13:35:34.498837+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---
