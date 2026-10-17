---
round: 0
review_mode: 
overall_score: 3.0 — Findings
timestamp: 2026-05-22T23:09:29.566304+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Round 1 综合评审

**论文**: "The Weakest Judge Wins: What Really Drives LLM Evaluation Panel Vulnerability Under Adversarial Attack"
**Target Venue**: EMNLP 2026 (via ACL Rolling Review)
**Reviewers**: R1 (Methods & Experiments), R2 (Novelty, Related Work, Presentation)
**审稿轮次**: Round 1（初审）
**报告日期**: 2026-05-22

---

## Summary

论文研究 multi-judge LLM evaluation panel 在对抗攻击下的脆弱性，借用 Byzantine Fault Tolerance (BFT) 框架分析 panel 组成与脆弱性的关系。通过 15 个模型、455 个 panel、6 种攻击类型、2 个 MCQ benchmark（MMLU, ARC）的大规模实验，论文的核心发现是：panel 中最脆弱 judge 的个体脆弱性（η_max）比 panel 多样性（K_eff）更能预测 panel 的攻击成功率（ASR），且在多种统计校正后 K_eff 的显著性大幅下降。次要发现包括 random fault vs adaptive attack 下 diversity 作用的机制切换、聚合方式对 K_eff 效应方向的调制、以及 targeted vs shared-bias 攻击的分类学。

---

## Strengths

**S1. 实验规模与系统性。** 15 个模型 × 6 families × 455 panels × 6 attack types × 2 benchmarks 的组合设计在 multi-judge evaluation 文献中属于大规模。四种统计校正方法（OLS、Clustered SE、Wild Cluster Bootstrap、Mixed Effects）并用，方法论意识强。[R1, R2 共识]

**S2. Random-vs-Adaptive 对比是最有洞察力的贡献。** §5.3 展示 diversity 在 random fault 下有效、在 adaptive attack 下失效的机制切换，揭示 adversary information advantage 如何改变 panel failure mode。这比单纯报告 "η_max dominates" 更有信息量且更 novel。[R1, R2 共识]

**S3. Aggregation-as-control-lever 发现具有实践价值。** Bayesian calibration 逆转 K_eff 方向、threshold voting 放大 η_max 的发现（Table 4）为 panel 设计提供了可操作的 knob。[R2 首提，R1 认可]

**S4. 攻击分类学有结构性贡献。** GAM 分析揭示的 targeted（diversity 有正面效应）vs shared-bias（diversity 无效或有害）的二分法，比 "η_max 一律主导" 的叙事更精细，实践指导意义更强。[R1, R2 共识]

**S5. 研究问题高度相关且及时。** Multi-judge LLM panel 正被广泛采用（LMSYS Arena, Scale AI 等），其对抗脆弱性分析有直接实践价值。[R1]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [COMPOUND CRITICAL] 15-cluster 统计功效不足 + Title overclaiming = 核心叙事建立在不可靠的统计基础上。**
这是两位 Reviewer 共同识别的最严重问题，由两个独立弱点复合而成：

- **(a) 统计层面 [R1-N1]**：以 15 个 judge 作为聚类单元做 clustered SE，远低于 Cameron-Gelbach-Miller (2008) 推荐的 ≥50 标准。K_eff 从 OLS 下 8/12 显著骤降至 clustered SE 下 0/12，完全可能是 few-cluster 导致的 Type II error（功效不足）而非 K_eff 真的无效。论文未报告 power analysis。

- **(b) Claim 层面 [R2-N2, R1 AGREE]**：论文标题 "Not Diversity" 和 Abstract 将 "K_eff collapses" 直接解读为 "diversity 不重要"，但论文自身数据内部矛盾——OLS 8/12 显著、Bayesian 下 K_eff 方向翻转且 4/12 显著、GAM 中 targeted attacks 下 K_eff 正向显著、random fault 下 2/2 显著。选择最保守（且可能 underpowered）的结果作为 title claim，更接近 cherry-picking 而非 robustness analysis。

- **(c) Compound 效应**：可能的 Type II error + 绝对化 title claim = 将统计不确定性包装为确定性结论。论文当前无法区分三种解释：K_eff genuinely 无效；检验 power 不足；multicollinearity (r=0.70) 导致系数不稳定。

**[R1, R2 共识] 修改建议**：(1) 报告 clustered SE 下的 statistical power；(2) 补充 CR2/CR3 small-sample correction；(3) 将标题改为条件化表述（如 "Under Adaptive Attack, Individual Judge Vulnerability Dominates Panel Diversity"）。

**W2. [CRITICAL] Log-log OLS 对有界响应变量的模型误设 [R1-N2, R2 AGREE]。**
ASR ∈ [0,1] 是有界比例变量，使用 log(ASR + ε) 的 OLS 存在三个问题：(a) 预测值可能超出 [0,1]；(b) ε = 10⁻⁹ 对近零 ASR 创造人为地板效应且未检验敏感性；(c) Beta regression 或 fractional logit 是处理 (0,1) 比例变量的标准方法。如果模型误设导致系数偏差，η_max 与 K_eff 的相对重要性排序可能改变。

**[R1, R2 共识] 修改建议**：以 beta regression 作为主分析或至少 robustness check；报告 ε 敏感性分析。

**W3. [CRITICAL] 实验范围不足以支撑一般性 claim [R1-N3, R2-W2, 共识]。**
论文标题和 Abstract 提出关于 "multi-judge LLM evaluation panel" 的一般性结论，但实验仅覆盖：(a) K=3 固定 panel 大小——未检验 K=5,7,9 时 majority voting 容错增强是否改变结论；(b) 两个 MCQ benchmark（MMLU, ARC）——当前 LLM-as-judge 最广泛应用是开放式评价（chatbot evaluation, code generation），攻击面和 judge bias 表现形式不同；(c) Oracle adversary——完全知识对手下攻击自然精准针对最弱 judge，现实中对手通常不知 panel 组成。

**[R1, R2 共识] 修改建议**：扩展实验覆盖（K>3 / 开放式 benchmark / partial-knowledge adversary），或大幅弱化 claim 为条件性结论。

**W4. [CRITICAL — R2; SHOULD-FIX — R1] Related Work section 过短，engagement 深度不足 [R2-N1, R1-W2]。**
Related Work 仅约半页（~20-30 行），对每个子领域仅 1-3 句 surface-level 描述。两位 Reviewer 对此严重性评估不同：

- **R2 评为 critical**：认为缺少 Dawid-Skene (1979) 众包聚合文献、AlpacaEval/FLASK 等主流 LLM-as-judge 框架、以及 2024-2025 ensemble adversarial defense 最新进展的讨论，无法建立论文在文献中的 positioning。
- **R1 评为 should-fix**：指出核心 ensemble 文献（Kuncheva & Whitaker 2003, Krogh & Vedelsby 1995, Brown et al. 2005, Tramèr et al. 2018）已被引用，只是讨论不够深入。

**Director 判断**：引用数量充分（~35 篇），但 Related Work section 的 discussion depth 确实不足以让读者判断 incremental contribution。定为 **critical — 影响接收但非 blocking**。

**修改建议**：扩展至 ~1 页，对 ensemble diversity theory、crowdsourcing aggregation、LLM-as-judge frameworks、adversarial ensemble defense 四个方向各 3-5 句深入讨论并明确区分点。

**W5. [CRITICAL — R2; PARTIAL AGREE — R1] BFT 类比概念错位 [R2-N3]。**
BFT 处理系统内部 Byzantine 节点（可 equivocation），本文的 adversary 是系统外部通过 adversarial inputs 欺骗 judges。Theorem 1 (Weakest-Link Monotonicity) 在 oracle adversary 下近乎 tautological——用更弱 judge 替换自然增加 ASR。

- **R1 PARTIALLY AGREE**：Introduction 中 BFT 类比不够精确可能给读者造成理论框架比实际更强的印象，但 §5.3 的 random-vs-adaptive 实证区分有效且是论文贡献之一。

**修改建议**：明确承认 BFT 是启发性类比而非严格 formal mapping；降低 Theorem 1 叙事权重。

### Should-Fix（影响评分但不一票否决）

**W6. [WARNING] r=0.70 confound 未充分解决 [R1-W1, R2-W1, 共识]。**
η_max 与 K_eff 的 Pearson r=0.70（~49% 方差共享）。论文使用的 clustered SE / mixed effects / bootstrap 解决的是观测间相关性，不是预测变量间多重共线性。K_eff 系数 SE 同时被 multicollinearity（VIF ≈ 2.0）和 few-cluster correction 双重膨胀。Dominance analysis 在高共线性下分离能力有限，缺少 within-tier 控制实验。
**建议**：报告 VIF；增加 within-tier 实验；使用 partial correlation 或 mediation analysis；软化 "Not Diversity" framing。

**W7. [WARNING] Theorem 1 理论深度有限 [R1-W3, R2-W3, 共识]。**
Theorem 1 的 stochastic dominance 条件（在所有 attacks 和所有 realizations 下 pointwise 更弱）过强，现实中 judges 有异质脆弱性 profile，此条件可能很少成立。在 oracle adversary 下定理近乎定义性。论文未验证条件的 empirical prevalence。
**建议**：报告满足条件的 panel pair 比例；弱化为 "on average" stochastic dominance；或推导 partial-knowledge 下的 bound。

**W8. [WARNING] 攻击实现细节不足 [R1-W4, R2 PARTIAL AGREE]。**
Appendix E (Table 5) 提供了 6 种攻击类型的 representative templates，但缺少 injection position、scoring prompt、重排序机制、变体数量等关键参数。
**建议**：补充完整攻击实现伪代码或参数表。

**W9. [WARNING] 模型版本标识不精确 [R1-W5, R2 AGREE]。**
部分 API 模型（如 "gpt-4o"）无确切版本号或 snapshot date，影响复现性。
**建议**：补充每个 API 模型的具体版本号或 API 调用时间窗口。

**W10. [WARNING] 前 5 页缺 framework 概念图 [R2-W4]。**
Method section 完全没有视觉辅助，涉及 panel construction、adversary model、η_max/K_eff、多种 aggregation rules 的复杂实验设计需要概念图帮助读者建立整体理解。
**建议**：在 Section 3 添加 framework figure。

**W11. [WARNING] Abstract 数字密度过高 [R2-W5]。**
~150 字中包含 12+ 个数字/比率，读起来像 result summary 而非 narrative hook。
**建议**：精简到 3-4 个最关键数字。

### Minor（不影响接收）

- **M1**: Table 4 Bayesian method R²=0.104 很低，"reversal" 的实际意义需更审慎表述。[R2]
- **M2**: 标题 "Wins" 含义不直观——weakest judge "wins" 什么？[R2]
- **M3**: §4.1 "RTX 4000 (96GB)" 型号不存在，推测为 RTX 6000 Ada 或 A100，需核实。[R2]
- **M4**: Limitations 仅 3 点 ~10 行，建议添加 benchmark scope limitation。[R2]
- **M5**: Equation 2 中 ε 值应在公式中直接注明而非仅在文字中提及。[R1]
- **M6**: Figure 1 y 轴标签过长，可简化。[R1]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识：

1. **Overall 3.0 (Findings)** — R1 和 R2 独立评分一致，交叉分享后均确认
2. **η_max dominance 是论文最稳健的贡献** — 在 4 种校正方法下保持显著（5-11/12 条件），相对 K_eff 有明确 robustness 优势
3. **K_eff null result 不确定** — 15-cluster power issue + title overclaiming 构成 compound problem，是论文最核心的方法论弱点
4. **实验范围受限** — K=3 / MCQ / oracle adversary 三重限制约束了发现的外部效度
5. **Title overclaims** — "Not Diversity" 将 underpowered 的统计结果呈现为确定性结论，不够严谨
6. **BFT 类比需精确化** — Introduction 中不够精确，但 §5.3 的实证区分有效（R1 PARTIALLY AGREE）
7. **Random-vs-Adaptive contrast 和 Aggregation modulation 是更 novel 的贡献** — 论文应考虑重新定位叙事重心

---

## Reviewer Divergence

以下问题两位 Reviewer 存在分歧：

1. **Excitement**: R1 = 3.5/5, R2 = 2.5/5
   - R1：BFT 框架应用于 LLM 评估新颖，攻击分类学揭示非平凡结构，实验设计有 ambition
   - R2：核心发现可从安全学/集成学习第一性原理预期，是 confirmatory result 而非 discovery
   - **Director 判断**：两种视角均合理。在 LLM-as-Judge 具体语境下的实证验证有增量价值，但不足以达到 Excitement ≥ 4（"exciting, would mention to others"）的 Main Conference 门槛。收敛至 3.0。

2. **Related Work 严重性**: R2 = critical, R1 = should-fix
   - R2：缺少 Dawid-Skene、AlpacaEval/FLASK 等关键文献讨论，无法建立 positioning
   - R1：核心 ensemble 文献已被引用（Kuncheva & Whitaker, Krogh & Vedelsby, Brown et al.），只是讨论过浅
   - **Director 判断**：引用数量充分（~35 篇），但 discussion depth 不够。定为 critical（影响接收）但非 blocking。

3. **Core finding novelty**: R2 = confirmatory/predictable, R1 = novel in context
   - R2：Schneier (2000) + Kuncheva & Whitaker (2003) + BFT f<n/3 共同使发现可预期
   - R1：在 LLM-as-Judge 领域 diversity 被广泛视为核心防御策略，挑战此共识有价值；但同意 novelty 可能被高估
   - **Director 判断**：Core finding 是 confirmatory-with-nuance，不是纯 novel 也不是纯 redundant。论文应更诚实地定位相对于经典理论的增量。

---

## Questions（需要作者在 Rebuttal 中回应）

1. **15 clusters 下的统计功效是多少？** 在 r=0.70 confound + 15 clusters 的条件下，检测 K_eff 的 medium effect size (d=0.5) 的 power 是否 > 0.80？如果 power 不足，"K_eff collapses" 能否仍被解读为 "diversity doesn't matter"？
2. **是否可提供 K>3 panel 的结果？** K=5 或 K=7 时 η_max 是否仍然主导？majority voting 容错增强是否改变结论？
3. **Beta regression 作为 robustness check 是否改变 η_max vs K_eff 的相对重要性排序？**
4. **K_eff 的精确计算公式是什么？** 从 pairwise MI 到 K_eff 的映射不透明，请提供完整公式。
5. **Title 是否可改为条件化表述？** 考虑到论文自身数据在不同方法下的矛盾结果。

---

## Missing References

以下为 R2 建议补充讨论（非补充引用）的方向——论文已引用核心文献但 engagement 不够深入：

- **众包/标注聚合**：Dawid & Skene (1979) — multi-annotator aggregation 的基础性工作，与 multi-judge aggregation 直接相关
- **LLM-as-judge 主流框架**：AlpacaEval (Li et al. 2023), Length-Controlled AlpacaEval (Dubois et al. 2024), FLASK (Ye et al. 2024) — 对 judge bias 的处理与本文攻击类型相关
- **Ensemble adversarial defense 最新进展**：2024-2025 年关于 ensemble adversarial defense 的工作（orthogonal distillation, transferable attack 理解等）

**注**：R1 指出论文实际有 ~35 篇参考文献（非 Director 初始摘要中的 7 篇），已覆盖 Kuncheva & Whitaker (2003)、Krogh & Vedelsby (1995)、Brown et al. (2005)、Tramèr et al. (2018) 等核心文献。问题不在于引用数量不足，而在于 Related Work section 的 discussion depth 不够。

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 本轮审稿未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态：未派发。** 视觉审查 Agent 未在本轮启动。

---

## Overall Assessment

**综合评分：3.0 / 5 — Findings**

| 维度 | R1 | R2 | 收敛 |
|------|-----|-----|------|
| Soundness | 3.0 | 3.0 | **3.0** |
| Excitement | 3.5 | 2.5 | **3.0** |
| Reproducibility | 3.0 | 3.0 | **3.0** |
| **Overall** | **3.0** | **3.0** | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分理由**：

论文在实验规模（15 models × 455 panels × 6 attacks）和统计方法意识（4 种 correction 并用）上表现扎实。η_max dominance、random-vs-adaptive contrast、aggregation modulation 三个发现对 multi-judge LLM evaluation 社区有参考价值，属于 Findings 级别的贡献。

但论文存在一个严重的 compound problem：核心叙事 "K_eff collapses, therefore diversity doesn't matter" 同时在 **概念层面**（core finding 可从安全学/集成学习第一性原理预期，novelty 有限）和 **统计层面**（15-cluster power issue 使得 K_eff null 可能是 artifact）受到挑战。标题和 Abstract 的绝对化表述将统计不确定性包装为确定性结论，构成 overclaiming。

此外，实验范围受限（K=3 / MCQ / oracle adversary）、Related Work 讨论过浅、BFT 类比不够精确、log-log OLS 模型误设等问题共同限制了论文达到 Main Conference 的门槛。

**达到 Main Conference (3.5-4.0) 的路径**：
1. 提供 power analysis 证明 K_eff null 不是 artifact，或增加 judges 到 30+
2. 扩展至 K>3 和非 MCQ 任务
3. 将标题和叙事重心从 "Not Diversity"（confirmatory）转向 "mechanism switch + aggregation design"（more novel）
4. 补充 beta regression robustness check
5. 扩展 Related Work discussion depth

当前版本推荐 **Findings**。

---

## Detailed Comments

### Section 1 (Introduction)
- BFT 类比在此处建立了读者对形式化理论深度的预期，但后续 Theorem 1 未能匹配此预期。建议明确说明 BFT 是启发性类比。
- "Not Diversity" 的 framing 应从 Introduction 开始就条件化，避免读者在第一页就形成 "diversity is irrelevant" 的过强印象。

### Section 2 (Related Work)
- 当前半页长度不够。已引用的经典文献（Kuncheva & Whitaker, Brown et al.）需要更深入的讨论——它们的具体结论是什么？本文如何扩展/挑战/验证它们？
- 缺少 crowdsourcing aggregation（Dawid-Skene）和 LLM-as-judge frameworks（AlpacaEval, FLASK）的讨论。

### Section 3 (Method / Formal Framework)
- Theorem 1 的 stochastic dominance 条件（所有 attacks × 所有 realizations 下 pointwise）过强。建议报告 empirical prevalence 或弱化条件。
- K_eff 的计算公式不够清晰——从 pairwise MI 到 K_eff 的具体映射需要明确。
- 缺少 framework figure，读者需在脑中重建 panel construction → attack → vulnerability measurement 的完整流程。

### Section 4 (Experimental Setup)
- ε = 10⁻⁹ 应在 Equation 2 中直接注明且做敏感性分析。
- 模型版本号应精确化（特别是 GPT 和 Claude 系列）。
- "RTX 4000 (96GB)" 型号不存在，需核实。

### Section 5 (Results)
- §5.1-5.2：η_max 的稳健性有充分展示，是论文最强部分。
- §5.3：Random-vs-adaptive contrast 是最有洞察力的贡献，建议提升其在整体叙事中的权重。
- §5.4：GAM 的 targeted vs shared-bias 分类有结构性贡献。
- §5.5：Aggregation modulation 发现有实践价值，但 Bayesian method 的 R²=0.104 很低，"reversal" 的实际意义需审慎表述。

### Section 6 (Analysis)
- r=0.70 confound 的讨论不应仅在 Appendix C.2，正文应显著讨论 multicollinearity（报告 VIF）。
- 缺少 within-tier 控制实验直接分离 η_max 和 K_eff。

### Section 7 (Conclusion)
- 应反映论文证据的条件性和不确定性，而非重复 "Not Diversity" 的绝对化表述。

### Limitations
- 当前 3 点 ~10 行，建议添加 benchmark scope limitation（MCQ only）。
- 第三点 "observational analysis is observational" 不够 constructive，建议提供具体的因果推断改进路径。

### Abstract
- 数字密度过高（12+ 个数字/比率），建议精简到 3-4 个关键数字。

---

*报告由 Review Director 基于 R1、R2 两位 Reviewer 的独立审稿、交叉分享和收敛回应合成。所有事实判断均以 Reviewer 直接阅读论文 PDF 的结果为准。*