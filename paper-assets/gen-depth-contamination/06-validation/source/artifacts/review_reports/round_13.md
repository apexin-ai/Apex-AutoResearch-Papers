---
round: 13
review_mode: fresh
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-19T15:52:11.354225+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## 审稿报告 — Round 13（圆桌审稿）

**论文**: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary
**Venue**: EMNLP 2026 (ARR May 2026)
**Deadline**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计 + 统计有效性；R2: 新颖性 + 完整性 + Related Work + 论文整体质量）
**审稿模式**: Fresh（重新审稿，无上轮记忆）

---

## Summary

本文定义并测量了递归合成文本的代际可区分性边界 K*_empirical：使用 15 维统计特征和 OBD-LightGBM 分类器，在 AUC 决策阈值 θ=0.60 下，C4 网络文本 K*=2（8/9 模型配置），Python 代码 K*=1-2（模型依赖），arXiv 学术文本 K*=3。论文还报告了 cross-domain variation（arXiv > C4 > Wikipedia）、cross-model transfer（80-92% accuracy retention at ≤1.5B）、以及下游 K*-aware filtering 实验。

---

## Strengths

**S1. 问题定义原创且有实际意义。** Generational depth estimation 此前未被系统研究。K*_empirical 的形式化（Eq.1，基于 DPI + Markov chain 收敛）清晰有用，填补了 binary detection 和 model collapse 文献之间的空白。[R1, R2 共识]

**S2. 实验覆盖面广，消融充分。** 9 个模型配置（5 架构家族，1B-14B）、4 个域（C4/arXiv/Wikipedia/Code）、4 种解码策略。Appendix 极为详尽（~16 页），包括 LOFO 阈值验证、feature group ablation、LaTeX markup ablation、McNemar test、power analysis、retrain-chain 对比等。这种系统性在 *CL 会议中少见。[R1, R2 共识]

**S3. 统计方法基本扎实。** GroupKFold 按 seed document 分组避免同源泄漏；self-BLEU 仅在同 fold/同 depth 内计算防止信息泄漏；permutation test 验证边界显著性；bootstrap CI 提供不确定性量化。[R1, R2 共识]

**S4. Cross-domain 分析揭示有意义的结构性差异。** arXiv K*=3 > C4 K*=2 > Wikipedia K*=1 的排序与域结构复杂度一致，且被多重验证（cross-scorer、LaTeX ablation、lexical statistics）。Mistral-7B 在 C4 上 K*=1 但 arXiv 上 K*=3 清楚表明 domain structure 是主要决定因素。[R1, R2 共识]

**S5. Limitations section 异常详尽。** 9 条限制逐一列出并附定量证据。这种自我批评的深度在 NLP 论文中罕见。[R1, R2 共识]

**S6. 写作质量整体较高。** 结构清晰，notation 一致，从 Abstract 到 Appendix 保持论证连贯性。引用管理良好（49 entries，0 orphan，0 missing）。[R1, R2 共识]

---

## Weaknesses

### Must-Fix（影响接收决定，两位 Reviewer 完全共识）

**MF-1** [critical] **θ=0.60 的 post-hoc 选择使核心结论 K*=2 的稳健性不足**
- θ=0.60 是在观察到 AUC 分布 discontinuity 后 post-hoc 选定。LOFO θ̂∈[0.5725, 0.6004]，θ=0.60 在区间右端，且 LOFO 使用同一数据分布，不构成外部验证。LOFO 在 Wikipedia 上完全失效（1/6 agreement）。
- 多个配置 margin 极薄：Qwen-cont 1v2 CI lower bound 仅超 θ 0.002（0.602 vs 0.600）；LLaMA-8B CI lower = 0.603。
- K*(θ) 稳定窗口仅 5pp [0.575, 0.625]。θ=0.55 时部分配置跳到 K*=3，θ=0.65 时跳到 K*=1。Discrimination boundary 是 gradual transition，非 sharp phenomenon。
- **两位共识建议**：将 K* 报告为对 θ 的函数或区间（如 K*∈[2,3] at θ∈[0.55,0.60]）；Abstract/Conclusion 明确 θ 依赖性；承认 θ 是需根据应用调整的参数。
- **历史**: FR-1 (R3) → R8-N1 (R8) → R11-W2 (R11) → MF-1 (R13)。此问题经多轮修改（data-driven threshold 定位、LOFO、permutation test），但核心残余问题（非外部验证、极薄 margin、窄稳定窗口）持续存在。

**MF-2** [critical] **"Largely generator-independent" claim 在 K* 边界处不成立**
- Abstract 声称 "largely generator-independent statistical features…enable 80-92% accuracy retention"，但 80-92% 是 6-class ordinal accuracy，非 K* boundary 的 1v2 AUC。Aggregate transfer 好不等于 boundary transfer 好。
- 7B cross-model transfer 中 4/6 off-diagonal 1v2 pairs 低于 θ（Limitations 点 9），boundary-level transfer 脆弱。
- Qwen-rewrite 迁移仅 61-63%（Figure 4），generation mode 对特征空间的影响（8.4pp within-Qwen spread）大于 model architecture 的影响（3.9pp across continuation models）。
- Cross-scorer 20/22 preservation，但 2 个例外恰为最关键边界配置（Qwen-cont C4, Qwen-7B arXiv）。"Largely robust" 掩盖了边界脆弱性。
- 未测试闭源模型，claim 措辞暗示广泛适用性。
- **两位共识建议**：Abstract 限定为 "within continuation-mode models at ≤1.5B scale"；明确区分 aggregate transfer（高）和 boundary-level transfer（脆弱）；cross-scorer 改为 "robust for non-borderline configurations (20/22); fragile at K* boundary"。
- **历史**: R8-W4 (R8) → R11-N1 (R11) → MF-2 (R13)。逐轮升级，始终未完全解决。

**MF-3** [critical] **Filtering 实验 effect size 极小，discriminability ≠ filtering utility**
- Binary filtering 将 MMLU 退化从 -1.53pp 改善到 -0.77pp，absolute improvement 仅 0.76pp。在 10-50% contamination 下更小（dose-response Appendix），graduated 与 no-filter 不可区分。
- arXiv 上 K*=3 但 graduated filtering 同样失败，论文自己承认 "K* accurately measures discriminability but overestimates filtering utility"。这暴露了 discriminability ≠ filtering utility 的根本 disconnect。
- K*=2 "predicts binary > graduated" 不是来自 K* 的预测力，而是碰巧在 C4 上 K*=2 与两级分类结构对齐。
- 仅在 2 个模型（Qwen-1.5B-Instruct + Pythia-1.4B）上验证。
- **两位共识建议**：Abstract/Conclusion 将 filtering 明确降级为 "proof-of-concept consistency check"；不暗示 K* 直接指导 filtering strategy；讨论 discriminability ≠ filtering utility 的 disconnect。
- **历史**: R8-W3 (R8) → R11-N2 (R11) → MF-3 (R13)。Round 9 曾标记 RESOLVED（框定为 proof of concept），但 Abstract/Conclusion framing 仍过强。

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning] **Prompt-chain vs retrain-chain 差距（K*=2 vs K*=7）需更显著讨论** [R2: Must-Fix, R1: Should-Fix — 严重程度分歧]
- Introduction 以 "web-scale contamination" 和 "data curation" 为动机，但只研究 prompt-chain。Retrain-chain K*=7（Appendix C.1）与 prompt-chain K*=2 差距巨大。
- 真实 contamination 同时涉及 prompting 和 retraining。K*=2 仅代表 prompt-chain 下限。
- Section 5 filtering 结论（binary > graduated）可能在 retrain-chain（K*=7）下翻转。
- **R2**: Introduction 应更早限定 scope；Discussion 增加完整段落分析两种 chain 的差异；理想情况下测试 retrain-chain filtering。
- **R1**: Section 5 开头已限定为 prompt-chain scope，严重程度应为 Should-Fix。但同意 Introduction/Abstract 需更早限定。
- **建议**: Introduction 第 1-2 段和 Abstract 明确限定 prompt-chain scope；Discussion 增加完整段落。

**SF-2** [warning] **Qwen 家族 5/9 过度代表** [两位共识]
- 9 个配置中 5 个来自 Qwen 家族。"8/9 configurations K*=2" 等效为 "all 5 Qwen + 3/4 non-Qwen"，后者更透明。
- Qwen-1.5B 还被用作 7B/14B 的 scorer，引入 same-family bias（Wikipedia 上已证实）。
- **建议**: Abstract/Section 4.1 报告按家族分层结果；Table 2 标注 per-family 配置数；aggregate statistics 同时报告 per-family medians。

**SF-3** [warning] **与 MAUVE 及分布距离度量的关系未讨论** [两位共识]
- MAUVE（Pillutla et al., 2021）是衡量 human vs. machine text 分布差异的标准度量，与本文的 pairwise AUC 概念相关但目标不同。论文使用 JSD（Figure 5）但未将其与 MAUVE 框架联系。
- **建议**: Section 2 添加 distributional quality metrics 讨论。

**SF-4** [warning] **方法论新颖性有限** [R2 提出, R1 部分 REBUT — 分歧]
- **R2**: 15D 特征 + OBD-LightGBM 均为标准方法组合，核心贡献是 empirical characterization。
- **R1**: OBD 框架的应用设计（pairwise AUC CI-based K* definition）和 K*_empirical 的形式化本身有方法论贡献。但同意主要价值在 empirical characterization。
- **建议**: Introduction 更明确定位为 empirical characterization study。

**SF-5** [warning] **Cross-scorer "largely robust" 措辞与边界案例不匹配** [两位共识]
- 20/22 统计上 "largely robust"，但 2 个例外恰为最关键的边界配置。
- **建议**: 改为 "robust for non-borderline configurations (20/22); the two exceptions are the most marginal configurations, consistent with thin margins at the decision boundary."

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：

1. **θ=0.60 post-hoc 选择**是论文最根本的脆弱点——K*=2 结论在 θ 微调 2-3pp 后显著改变，LOFO 不构成外部验证。
2. **"Generator-independent" claim 过度泛化**——aggregate transfer（高）与 boundary-level transfer（脆弱）的 disconnect 在 Abstract 中未被反映。
3. **Filtering effect size 过小且存在 disconnect**——K* accurately measures discriminability but overestimates filtering utility（arXiv case 为直接证据）。
4. **Qwen 5/9 过度代表**需要透明报告。
5. **MAUVE 缺失**是 Related Work 的明显缺口。
6. **问题定义原创、实验系统、统计严谨**是论文的核心优势。

---

## Reviewer Divergence

| 问题 | R1 | R2 | 分析 |
|------|-----|-----|------|
| Prompt-chain scope 严重程度 | Should-Fix (W3) | Must-Fix (N2) | R1 认为 Section 5 已限定 scope；R2 认为 Introduction/Abstract 的动机与 scope 不匹配更为根本。建议作为高优先级 Should-Fix 处理 |
| 方法论新颖性 | 部分 REBUT | Should-Fix (W1) | R1 认为 OBD + K* formalization 有方法论贡献；R2 认为核心是 empirical characterization。两者同意：定位应更明确 |
| One-wash laundering 术语 | Should-Fix (W4) | REBUT | R1 认为隐含对抗性含义需验证或换词；R2 认为是描述性术语（类似 catastrophic forgetting）。共识：Abstract 首次使用时加 parenthetical clarification 即可 |
| 模型规模天花板 ≤14B | 部分 REBUT | Should-Fix (W5) | R1 指出论文已有 scale invariance 证据链（1.5B→14B K* 稳定）；R2 认为 70B+ 模型是 2026 年主要污染源。共识：在 Limitations 补充对 >30B 的预测并标注为未验证外推 |

以上分歧均在 Should-Fix 及以下级别，不影响核心评价。

---

## Questions

1. **[关键]** 7B cross-model transfer 中 4/6 off-diagonal 1v2 pairs 低于 θ——能否提供每个 pair 的具体 1v2 AUC 和 CI？
2. **[关键]** Neural probe self-familiarity 归因（Qwen K*_neural=3 vs Pythia/OLMo K*_neural=2）是否有 cross-model probe 实验直接验证？
3. LOFO 唯一 C4 mismatch 的具体 θ̂ 和 K* 差异？是否暗示 θ 最优值依赖 generation mode？
4. Filtering 在 contamination ratio < 50% 时，binary 与 no-filter 差异是否仍统计显著？
5. Retrain-chain 在 full fine-tuning（非 LoRA）或更大模型上预计 K* 如何变化？

---

## Missing References

1. **Pillutla et al., 2021**: "MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers" (NeurIPS 2021) — 直接相关的分布距离度量 [R1, R2 共识]
2. **Pillutla et al., 2023**: "MAUVE Scores for Generative Models: Theory and Practice" (JMLR 2023) — MAUVE 理论分析 [R2 提出, R1 AGREE]
3. **Holtzman et al., 2020**: "The Curious Case of Neural Text Degeneration" (ICLR 2020) — 论文使用 nucleus sampling p=0.95 但未引用原始论文 [R2 提出, R1 AGREE]

---

## External Review (Stanford Agentic Reviewer)

**状态：未配置**。项目未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态：timeout**（运行 926 秒后超时）。视觉审查 Agent 未能在时限内完成。建议下次审稿前确认 PDF 渲染环境可用。

---

## Overall Assessment

**评分：3.5 — Borderline Conference（更适合 Findings）**

**置信度：4/5**（两位 Reviewer 均具备 synthetic text detection / model collapse / ordinal classification 领域经验，独立审稿后交叉验证达成高度共识）

### 评分理由

**支持 Conference 的因素：**
- 问题定义原创且有实际意义，填补 binary detection 和 model collapse 之间的空白
- 实验覆盖面在 *CL 论文中属上乘（9 configs × 5 families × 4 domains × 4 decoding）
- 统计方法严谨（GroupKFold、bootstrap CI、permutation test、LOFO、McNemar）
- Cross-domain variation 是有价值的 empirical insight
- Limitations 的详尽程度树立了标杆

**限制 Conference 的因素：**
- 核心发现 K*=2 高度依赖 post-hoc 阈值 θ=0.60，margin 极薄（0.002），稳定窗口仅 5pp
- "Generator-independent" claim 在 K* boundary 不成立，aggregate vs boundary disconnect 在 Abstract 中未被反映
- 唯一的下游应用验证（filtering）effect size 极小（0.76pp MMLU），且 K* overestimates filtering utility（arXiv case）
- 方法论创新有限——核心贡献是 empirical characterization 而非方法突破
- Prompt-chain K*=2 vs retrain-chain K*=7 的巨大差距削弱了对实际 contamination 场景的指导价值

### 升级路径

如果修正以下三点，论文可从 3.5 提升至 4.0（Conference 水平）：
1. 将 K* 报告为 θ 的函数或区间，而非单一值；Abstract/Conclusion 明确 θ 依赖性
2. 将 "generator-independent" claim 严格限定为 "within continuation-mode models at ≤1.5B scale, for aggregate metrics"；明确 boundary-level transfer 的脆弱性
3. 将 filtering 降级为 "proof-of-concept consistency check"；Abstract/Conclusion 不暗示 K* 直接指导 filtering

---

## Detailed Comments

### Abstract
- "Largely generator-independent statistical features" → 建议改为 "scorer-anchored features that transfer across generators within tested continuation-mode configurations"
- "80-92% accuracy retention among tested continuation-mode generators" → 补充 "at ≤1.5B scale; boundary-level transfer is fragile at 7B"
- "K* characterizes discriminability boundaries that inform...filtering strategy" → 弱化为 "K* characterizes discriminability boundaries; initial filtering experiments show consistency with the two-level structure but with limited effect sizes"
- "one-wash laundering effect" → 首次使用时加 parenthetical definition

### Section 3.1 (Threshold)
- Eq.1 后补充 K*=0 edge case 说明或注明 0v1 始终满足条件
- 更诚实地呈现 θ：承认 LOFO 不构成外部验证（使用同一数据分布）；承认 LOFO 在 Wikipedia 上不适用；将 θ 定位为 "operational parameter that requires application-specific calibration"
- 建议在正文中（而非仅 Figure 3）报告 K*(θ) 在 θ∈[0.55, 0.65] 范围内的行为

### Section 3.2 (Features)
- Table 2 caption 注明 CI 方法（bootstrap, 1000 resamples）
- Table 2 caption 明确标注哪些 cells 用 self-scoring vs cross-scoring

### Section 4.1 (Results)
- "8/9 configurations" 的表述应补充 per-family breakdown（"K*=2 across all 5 tested architecture families on C4, with 8/9 individual configurations; Qwen contributes 5 configurations spanning three scales"）

### Section 4.2 (Transfer)
- 明确区分 aggregate transfer metrics（80-92% ordinal accuracy, 96-100% mean AUC retention）和 boundary-level transfer（1v2: 4/6 off-diagonal 7B pairs below θ）
- Cross-scorer "largely robust" → "robust for non-borderline configurations (20/22); fragile at K* boundary"
- Appendix 补充 7B 每个 off-diagonal pair 的 1v2 AUC + CI 表

### Section 5 (Filtering)
- 开头明确为 "proof-of-concept consistency check"（已有类似表述，需更强调）
- 讨论 discriminability ≠ filtering utility 的 disconnect（arXiv case）
- 讨论在 realistic contamination levels（10-50%）下 effect size 大幅缩小

### Section 6 (Discussion)
- 增加完整段落讨论 prompt-chain vs retrain-chain 差异对实际 contamination 场景的影响
- K*=2（prompt-chain）应被明确定位为 "conservative lower bound on discrimination depth"

### Section 2 (Related Work)
- 补充 MAUVE（Pillutla et al., 2021/2023）和 Holtzman et al., 2020 (nucleus sampling)
- 讨论 per-text depth estimation 与 population-level distributional metrics 的互补关系

### Conclusion
- 最后一句 generic future work → 替换为具体 directions（retrain-chain K* 测量、>30B scale trend、adaptive filtering）
- 不应暗示 K* 直接指导 filtering

### Limitations
- 补充对 >30B 模型的预测（基于 scale trend）并标注为未验证外推

### Format
- 正文 8 页 ✓
- Limitations section ✓（9 条，详尽）
- Ethics Statement ✓
- 匿名 ✓（Anonymous）
- ACL style template ✓
- 引用格式 ✓（49 entries, 0 orphan, 0 missing）
- Figure 4 colorbar 建议标注 "Retention (%)"