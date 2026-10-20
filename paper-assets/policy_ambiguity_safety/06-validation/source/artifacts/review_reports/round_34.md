---
round: 34
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-25T21:38:40.052991+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 34 审稿报告 — Policy Ambiguity Is Nocuous

**论文**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety"
**Venue**: EMNLP 2026 via ARR (May cycle)
**审稿模式**: Fresh (重新审稿)
**Reviewer 配置**: 2 名 Reviewer（R1: 统计方法 + 实验设计；R2: 新颖性 + 完整性）
**交叉回应**: R1 完成（7 AGREE / 6 REBUT），R2 完成（9 AGREE / 2 REBUT）

---

## Summary

论文研究政策文本中的语言歧义（policy ambiguity）对客服 AI agent 安全性的因果效应。研究者基于需求工程（RE）文献构建了六类歧义分类体系，在 τ²-bench 上合成 300 对 matched clause pairs（歧义 vs 消歧），并在 5 个 frontier LLM（GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3）上进行受控实验。主要发现：(1) 歧义条件下违规率增加 +34.0 pp（pooled McNemar OR=15.1）；(2) clause wording 解释 22.4% 方差而 ambiguity type 仅 0.4%；(3) 41.3% 的 clause pairs 展示 convergent nocuity（多模型收敛到同一错误解释）。附带 SOPBench 跨基准验证（+12.7 pp）和 healthcare pilot（+58.8 pp, n=50）。

## Strengths

**S1: 严谨的因果推断设计。** Matched-pair design 搭配 perturbation control（Δ=−0.67 pp, Section 4.5）提供了较强的内部因果效度。在 agent safety 文献中，因果推断设计（而非相关性分析）是少见的贡献。

**S2: Clause-level vs type-level 方差分解具有实践价值。** 22.4% vs 0.4% 的方差对比直接挑战了 RE 文献中按歧义类型分级风险的传统做法。NMI（0.23 vs 0.01）和 Cramér's V（0.45 vs 0.14）从不同角度佐证了 clause wording > type 的结论。

**S3: Convergent nocuity 是有理论深度的新概念。** 41.3% 跨 3+ 模型收敛到同一错误解释，超过 ambient baseline 1.7%（+39.6 pp excess），揭示了政策歧义导致系统性而非随机性安全风险。

**S4: 统计方法全面、透明度高。** McNemar、ICC、NMI、Cramér's V、TOST、logistic regression、MH 分层分析等多种方法综合使用。26 页附录提供详尽的方法细节和补充分析。

## Weaknesses

### Must-Fix

**MF1: 合成 clause pairs 的生态效度差距严重且讨论不足。** [R1+R2 共识]

主实验效应 +34.0 pp 基于合成匹配 clause pairs，SOPBench 跨基准验证效应仅 +12.7 pp（主实验的 37%，Appendix AD Table 23）。论文在 Limitations（p.9）承认 "upper bound" 但正文 Section 7 仅用一句话带过此差距。Healthcare pilot（+58.8 pp）样本量仅 n=50，Introduction 中 "+58.8 pp" 的语气过于确定（未标注 pilot）。"First causal study" 的 framing 需要限定。

**要求的修改**：
- (A) Abstract/Introduction 中 "first causal study" 加限定词（如 "first controlled matched-pair study on synthetic clause pairs"）
- (B) Section 7 增加 2-3 句讨论 34.0→12.7 pp 衰减的可能原因（clause 自然度、benchmark 难度差异等）
- (C) Healthcare pilot 明确标注 "pilot"，降低措辞确定性
- (D) 正文或附录显式列出因果识别假设（SUTVA, no unmeasured confounders, exclusive manipulation of ambiguity）

### Should-Fix

**SF1: Pooled McNemar 检验违反独立性假设。** [R1 Must-Fix → R2 Should-Fix → Director 裁定 Should-Fix High]

Pooled McNemar 将 5 models × 300 pairs = 1,497 对视为独立配对，但 ICC(1) = 0.892–0.940 证实同一 clause pair 在不同模型上的违规行为高度相关。论文已在 Appendix J 提供 MH 分层分析（MH OR = 9.57 [7.63, 12.01]）并在 Section 5.1 报告了 per-model 结果（全部 p < 10⁻⁵），结论方向不变。但正文以 pooled 为主的报告框架需调整。

**要求**：正文以 per-model McNemar 为主要证据框架，pooled 降为辅助。补充 mixed-effects logistic regression（clause random intercept + model random slope）作为首选统计模型。

**SF2: ~46% 残差系统方差来源未充分讨论。** [R1+R2 共识]

Figure 2 方差分解显示 residual 60.8%（含约 46% 系统方差），clause identity (22.4%)、model (15.8%)、type (0.4%) 合计仅解释 39.2%。可能来源：clause × model 交互效应、scenario/conversation trajectory effects、clause 的复杂 surface features（嵌套深度、从句结构等）。附录有零散分析（token-length Appendix K, logistic regression Appendix I）但正文缺专门段落。

**要求**：正文增加 1 段讨论残差方差可能组成。将 "clause-level auditing outperforms type-level screening" 修改为更审慎的 "clause-level features are the strongest identified actionable predictor"。

**SF3: Incompleteness confound 位置过晚。** [R1+R2 强共识]

Section 5.1 首次报告六类型结果时未即时标注 incompleteness 类型的 information-addition confound。读者在 Table 4 时不知道 incompleteness 效应量可能部分来自信息添加而非歧义消除，直到 Section 4.5 perturbation control 才首次提及。

**要求**：Section 5.1 首次报告六类型结果时立即加注 incompleteness 的 information-addition caveat。

**SF4: Per-type judge agreement 差异需正文讨论。** [R1+R2 共识]

Coreferential κ = 0.479、authorization scope cross-judge κ = 0.385，远低于 lexical κ = 0.904。这两个类型的 per-type 效应估计可靠性显著降低。论文在 Section 5.2 已注意到 authorization scope 的不确定性，但 coreferential 的可靠性问题讨论不够。

**要求**：Table 4 或 Section 5.1 标注哪些类型受低 judge agreement 影响。Figure 3 authorization scope 列增加视觉区分。

**SF5: Real-world prevalence audit 的 LLM judge 循环性。** [R2 提出, R1 同意]

Appendix AH 的 87% 歧义率使用 LLM judge 标注。Human validation κ = 0.295 偏低，意味着 LLM 和人类对 "什么算歧义" 的判断一致性有限。LLM 可能对某些歧义类型系统性过度/不足敏感，prevalence 估计有偏。

**要求**：Appendix AH 更醒目地报告 human validation κ = 0.295，并讨论 LLM 可能的系统性偏差方向。

**SF6: Introduction 数字密度过高。** [R2 提出, R1 同意]

Abstract 和 Introduction 短空间内压缩 10+ 统计数字（+34.0 pp, +31.0 pp, OR=15.1, NMI=0.23, V=0.45, ICC=0.919, 22.4%, 41.3% 等），损害叙事流畅性，读者难以区分核心发现与支撑证据。

**要求**：Introduction 聚焦 3-4 个核心数字（+34.0 pp 效应、22.4% vs 0.4% 方差对比、41.3% convergent nocuity），其余移至 Section 5。

### Divergent Issues（分歧记录）

**[DIV1] Type-mechanism dissociation 新颖度**
- R1：对 RE 文献按类型分级风险假设的重要实证挑战——如果 type 仅解释 0.4% 方差，则按类型审计策略无效。NMI=0.01 + V=0.14 是非平凡发现。建议补 permutation null model comparison。
- R2：六种类型是粗粒度分类，clause 内方差 > type 间方差是预期结果，新颖度有限。
- **Director 倾向**：R1 论证更有说服力。Type-level risk screening 是 RE 领域的隐含实践假设，0.4% 方差挑战了该假设。但补充 permutation baseline 可增强说服力。按 Should-Fix 处理——补 permutation null model（随机分 6 组的 NMI baseline, 10,000 次置换）。

**[DIV2] Cross-judge 设计不对称性**
- R1：GPT-4.1 judge "+8 pp harder" 影响绝对违规率的跨模型比较。
- R2：Treatment effect Δpp 不受 judge 偏差影响——同一模型的两个条件由同一 judge 评判，偏差在做差时消除。
- **Director 判断**：R2 反驳有效。核心 claim 是 Δpp 而非绝对率。Minor 级别——Table 4 caption 注明绝对率受 judge 影响即可。

**[DIV3] 模型选择偏向 frontier**
- R1：部署导向研究（customer-service agent deployment），frontier 模型选择合理。小模型有 floor effect 风险。
- R2：缺少 7B-70B 模型限制 generalizability。
- **Director 判断**：R1 论证更有说服力。Limitations 已有 frontier-class scope sentence。无需额外实验。

## Questions for Authors

1. 补 mixed-effects logistic regression（clause random intercept + model random slope）后，效应量估计与 pooled McNemar OR=15.1 相比变化多大？
2. NMI = 0.01（type → mechanism）是否显著低于随机 6-group permutation distribution？请提供 permutation p-value。
3. 排除 incompleteness 类型后，convergent nocuity rate 是否仍显著高于 ambient baseline 1.7%？
4. Human validation κ = 0.295 中，LLM judge 对歧义 prevalence 是系统性高估还是低估？具体数字如何？
5. 正文报告框架从 pooled McNemar 切换到 per-model Δpp 后，核心叙事是否需要重构？

## Missing References

1. **AgentHarm** (Andriushchenko et al., ICLR 2025) — Agent safety benchmark，应在 Section 2 (Related Work) 的 agent safety 部分引用并讨论差异。[R1+R2 共识]
2. **ToolEmu** (Ruan et al., ICLR 2024) — 确认引用版本信息。[R1 提出]
3. R32 遗留的 3 篇参考文献仍 open（见 Issue Tracker R32-M1）。

## External Review

外部审稿：**未请求**。

## Visual Layout Check（非评分项）

视觉审查已完成。0 critical / 2 warning / 6 info。

**Warnings:**
- **Page 18**: 六张表格（Tables 16–21）挤在单页，视觉极度密集。建议将 Tables 16–17（示例表）与 Tables 18–21（数据表）分到两页。
- **Page 26**: 末页仅约 15% 内容（AI Assistants 声明），余下 85% 空白。可并入前一页或合并到上一个 appendix section 末尾。

**Info:**
- Page 2: Figure 1 节点文字偏小（建议 ≥8pt）
- Page 6: Figure 3 热力图单色调渐变（色盲友好性），但已标注数值，影响有限
- Page 6: Figure 4 森林图 marker 标签较小
- Page 7: Table 4 列头缩写较多（需对照脚注）
- Page 8: Figure 5 + Figure 6 + Discussion 挤在一页，密度高
- Page 12: Tables 6–9 密度较高但可读

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

| 维度 | 评分 | 说明 |
|------|------|------|
| Soundness | 4 / 5 | 设计严谨，统计报告框架可优化 |
| Excitement | 3.5 / 5 | 有价值的新发现，生态效度限制影响力 |
| Clarity | 3.5 / 5 | 结构清晰，数字密度和术语门槛偏高 |
| **Overall** | **3.5** | **Borderline Conference** |

R1 Overall 3.5, Soundness 4, Excitement 4。R2 Overall 3.5, Soundness 4, Excitement 3.5。交叉回应后均维持 3.5。

**定位**：强 Findings 候选。论文有清晰的研究贡献（首次系统量化政策歧义对 agent 安全的影响、clause-level vs type-level 方差分解、convergent nocuity 概念）和较强的内部效度。核心短板在合成基准的外部效度差距（34.0 → 12.7 pp）和统计报告框架的优化空间。

**提升至 Conference (4.0) 的路径**：
1. 解决 MF1（外部效度讨论深化 + "first causal study" framing 限定）
2. 解决 SF1（统计报告框架：per-model 为主 + mixed-effects model）
3. 解决 SF2（残差方差讨论 + auditing claim 措辞调整）
4. 补充 permutation null model for NMI（DIV1）

## Detailed Comments

### 统计方法层面
- Per-model McNemar 应作为主要证据框架，pooled 降为辅助。五个模型各自独立的显著性（all p < 10⁻⁵）比 pooled 更有说服力且无独立性假设问题。
- Mixed-effects logistic regression（clause random intercept + model random slope）应作为首选统计模型，更准确地处理 clause-level 聚类。
- MH 分层分析已在 Appendix J（MH OR = 9.57, Breslow-Day p = 0.022 heterogeneity），正文引用应更显著。
- Permutation null model for NMI = 0.01 可增强 type-mechanism dissociation 的说服力——证明 0.01 不是随机分组的预期值。

### 写作层面
- Introduction 精简至 3-4 核心数字：+34.0 pp 效应、22.4% vs 0.4% 方差对比、41.3% convergent nocuity。
- Section 5.1 首次报告六类型结果时立即标注 incompleteness confound。
- Healthcare pilot 明确标注 "pilot" 和 n=50。
- "Clause-level auditing outperforms type-level screening" 改为 "clause-level features are the strongest identified actionable predictor"。
- Discussion 加 1 句 RLHF implication（convergent nocuity 是否误导 reward model）。
- Table 4 caption 注明绝对率受 judge 影响、跨模型比较应关注 Δpp。
- §6.2 disambiguation neglect 分母 614 明确标注来源。

### 可视化层面
- Figure 2 caption 增加方差分解逻辑说明 + "At random" 标签和红色标记线解释。
- Figure 3 authorization scope 列视觉区分（低 κ 标注）。
- Table 4 footnote 字体适当放大。
- Table 5 TOST 列名在 caption 中完整说明，或移至 Appendix。
- Appendix P (Li et al. taxonomy mapping) 在正文 §3 更显著引用。