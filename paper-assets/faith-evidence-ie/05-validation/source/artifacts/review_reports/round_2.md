---
round: 2
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T01:11:49.780431+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告（Round 2）

**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction
**Venue**: EMNLP 2026（ARR 统一审稿）
**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性）

---

## Summary

本文将 evidence-grounded document-level relation extraction (DocRE) 形式化为结构化生成任务，系统比较了 GRPO、DPO、RSFT 三种 post-SFT 优化范式在 Qwen3（1.7B/4B/8B/14B）和 LLaMA-3.1-8B 上的表现。三个核心发现：(1) evidence tax 是 scale-dependent 的（1.7B 有益，4B+ 近似中性）；(2) gradient-based optimization 导致 extraction-evidence decoupling（GRPO 灾难性、DPO 渐进），而 RSFT 通过离散样本选择避免 decoupling；(3) RSFT 压缩训练方差 4.6–31×。论文提出 CED（基于 NLI 的 contrastive 评分函数）和 EDCR（Evidence-Decoupling Ratio）作为分析工具。

相比 Round 1，论文有显著改进：增加了 test set 评估（5 个 scale）、3-seed 覆盖（1.7B/4B/8B/LLaMA）、matched@2048 fair evaluation protocol、random RSFT baseline、encoder baseline 对比表、MTL 相关文献。但核心统计声明的基础仍然薄弱，方法论原创性问题未解决。

---

## Strengths

**S1. 问题定位精准且实用（R1-S1, R2-S1, 双方一致）。** Evidence grounding 是 LLM-based IE 部署的真实痛点。论文清晰地指出 encoder 方法（SAIS/DREEAM 的分类范式）与 LLM 方法（生成范式）在 evidence 处理上的结构性差异，这一 framing 对社区有价值。

**S2. Decoupling spectrum 分析框架有启发性（R1-S2, R2-S4, 双方一致）。** 将 GRPO collapse → DPO gradual decay → RSFT no decoupling 组织为连续谱，从优化机制角度（gradient pressure vs. discrete selection）解释了不同范式的表现差异。Per-relation EDCR 分析（n=76, ρ=−0.79）和训练动态可视化（Figure 3）从统计和过程两层支撑核心论点。

**S3. 跨尺度 + 跨 model family 的实验覆盖面好（R1-S3, R2-S1, 双方一致）。** 1.7B/4B/8B/14B（Qwen3）+ LLaMA-3.1-8B 的五模型覆盖，DocRED + Re-DocRED 双数据集验证，test set 评估保持 model ranking（Spearman ρ=1.0）。Matched@2048 fair evaluation protocol 和 controlled evaluation subset 体现了对混淆因素的认真处理。

**S4. 对自身局限的透明度（R1-S4, 双方一致）。** 论文在 Section 7 主动承认 EDCR 缺乏 human judgment 验证、variance 基于 3 seeds、SFT vs RSFT variance 测量来源不同等局限。

**S5. 写作质量高（R2-S5）。** "Evidence tax"概念和 decoupling spectrum 叙事框架清晰，Abstract 中的关键数字均可在正文追溯。

---

## Weaknesses

### Must-Fix（阻碍接收的核心问题）

**W1 [CRITICAL] — n=3 seeds 的方差压缩声明缺乏统计基础（R1-W1, R2 交叉回应 AGREE）。**
论文第三个核心贡献 "RSFT compresses training variance 4.6–31×" 基于每组仅 3 个 seed 的标准差比较。n=3 时方差估计的自由度 df=2，σ 的 95% CI 约 [0.52s, 6.29s]——真实 σ 可能比估计值大 6 倍或小 2 倍。"31× compression" 在统计上几乎无法从 n=3 可靠估计。Cohen's d=2.58 的标准误约 1.2-1.5，95% CI 覆盖从接近 0 到 >5 的范围。此外，SFT variance（完整训练的 seed 方差）与 RSFT variance（固定基础上的微调方差）测量不同层次的随机性，RSFT variance 天然更小（R1-W5, R2 交叉回应 AGREE）。两个问题叠加使得 Abstract 中的核心声明不可靠。
**建议**：增加到 5-10 seeds（至少对 1.7B 低成本尺度），或将方差压缩降级为定性观察（"RSFT substantially reduces variance"），不在 Abstract 和 Contributions 中给出具体倍数。

**W2 [CRITICAL] — EDCR 的 shared-component 问题使统计验证不可靠（R1-W2, R2 交叉回应 AGREE）。**
EDCR = Evi-Recall_TP / Rel-Recall = (TP_evi × G) / TP²。TP 同时出现在分子和分母中，构造了与 Rel-F1（也是 TP 的函数）的机械性负相关。Cross-method ρ=−0.89 (n=7, p=0.007) 中 n=7 极小，GRPO QLoRA 极端点（EDCR=0.9876, Rel-F1=1.38）可能主导相关性——移除后 n=6 时 ρ=−0.83 (p=0.042)，仅边际显著。Per-relation ρ=−0.79 (n=76) 面临同样的 shared-component 问题。
**建议**：报告移除 GRPO QLoRA 后的 ρ；用 partial correlation 控制 TP 共享效应；用 permutation test 验证 per-relation 分析。

**W3 [CRITICAL] — 方法论原创性不足（R2-W1, R1 交叉回应降级为 MAJOR）。**
三个核心贡献逐一审视：(1) Evidence tax 的 scale-dependency 是实验观察，不是方法创新；(2) Decoupling spectrum 中 gradient-based vs selection-based 的根本差异在 multi-objective optimization/reward hacking 文献中已有讨论，EDCR 是两个 recall 的简单比值；(3) RSFT 论文自己承认是 "well-established"，应用于 DocRE + CED 是组合，非创新。CED 的 contrastive formulation 与 flat-NLI 差异仅 0.02pp（R1-W3），论文自己承认 "not essential"。整体定位为 empirical study with analytical tools，方法创新深度不足以进入 main conference。
**R1 部分反驳**：好的 empirical finding 在 EMNLP 有先例；GRPO 在不同 precision 下的不同表现不是简单的 gradient vs selection 二分法。但这需要统计基础更牢固才能成立。

### Should-Fix（显著影响论文质量的问题）

**W4 [MAJOR] — GRPO collapse 分析缺乏机制深度（R2-W3, R1 交叉回应 AGREE）。**
Section 4.3 对 GRPO QLoRA catastrophic collapse 的分析停留在现象描述。未连接 reward hacking 文献，未探讨简单缓解策略（不同 KL 系数、reward normalization），未分析 quantization precision 导致 collapse 的具体机制。Table 2 数据暗示 precision 是关键因素（bf16 G=4 和 G=8 均避免 catastrophe），但论文文字未深入讨论这一关键区分。如果 collapse 主要是 QLoRA 精度问题而非 GRPO 方法本质，"decoupling spectrum" 框架的稳固性受质疑。

**W5 [MAJOR] — DPO 3-epoch 使用不同 evaluation protocol（R1-W4, R2 交叉回应 AGREE）。**
Footnote 1 提到 "earlier evaluation protocol" 但未说明具体差异。Table 2 将 DPO 3-epoch 与其他方法并列，读者会视为直接可比。Decoupling spectrum 是论文核心分析框架之一，其中一个数据点来自不同 protocol 影响整个框架可靠性。建议在同一 protocol 下重评 DPO 3-epoch，或明确排除。

**W6 [MAJOR] — CED contrastive formulation 增量价值不足（R1-W3, R2 交叉回应 AGREE）。**
Appendix B 显示 CED vs flat-NLI 的 Rel-F1 差仅 0.02pp（45.63 vs 45.61），在 3-seed noise level（std≈0.09pp）以内。减法公式（p⁺ − max_j p⁻_j）缺乏理论动机（为什么不是比值或 log-ratio？）。论文自己承认 contrastive formulation "not essential for data selection quality"（Section 3.4）。CED 作为方法贡献被实质性削弱。

### Nice-to-Fix（改善论文质量的建议）

**W7 [MINOR] — Related Work 遗漏（R2-W4, R1 部分 AGREE）。**
缺少：LMRC (Li & Zhang, 2024; arXiv 2408.13889)——LLM-based DocRE baseline；SummaC (Laban et al., 2022, TACL)——NLI-based faithfulness evaluation 先驱，与 CED 设计理念直接相关；RelPrior (Huang et al., 2025)；Rationale Verification for RE (Li et al., 2025)。

**W8 [MINOR] — CED 对外部 NLI 模型的 sensitivity analysis 不足（R2-W5, R1 AGREE）。**
仅测试 DeBERTa v3-base vs v3-large（同一家族），未测试其他 NLI 模型家族，未分析 DocRE 领域的 OOD 行为。

**W9 [MINOR] — Encoder baseline 对比选择性呈现指标（R1-W7, R2 AGREE）。**
Table 12 强调 TP-only Evi-F1（>80%），淡化 Ign-F1 16-18pp 差距。应更平衡讨论 LLM-based 方法在 absolute extraction performance 上的劣势。

**W10 [MINOR] — 缺少与其他 LLM-based RE 方法的直接数值对比（R1-W8, R2 AGREE）。**
Related Work 讨论了 AutoRE、GLiDRE 等，但未在任何表格中给出 extraction performance 的直接对比。

**W11 [MINOR] — Limitations 遗漏（R2-W6, R1 AGREE）。**
(1) DocRED 证据标注已知不完整，影响 CED/EDCR 计算可靠性；(2) GRPO/DPO/RSFT 计算成本差异未报告；(3) 仅评估 DocRE 一种 IE 任务，generalization 未讨论。

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉回应后达成一致：

- **[AGREE]** n=3 variance claim 统计基础不足，需要增加 seeds 或降级声明（R1-W1）
- **[AGREE]** EDCR shared-component 构造机械性负相关，需要 partial correlation/remove-outlier analysis（R1-W2）
- **[AGREE]** CED contrastive 增量仅 0.02pp，不足以作为方法贡献（R1-W3 = R2-W6 indirect）
- **[AGREE]** SFT vs RSFT variance 测量不同来源，直接比较不公平（R1-W5）
- **[AGREE]** GRPO collapse 分析需要更深机制解释和 reward hacking 文献连接（R2-W3）
- **[AGREE]** DPO 3-epoch evaluation protocol 差异影响 spectrum 可比性（R1-W4）
- **[AGREE]** Missing references: SummaC, LMRC（R2-W4）
- **[AGREE]** 实验覆盖面和分析深度是论文强项（S1-S4）

## Reviewer Divergence

- **方法论原创性的严重程度**：R2 标为 CRITICAL（论文定位为 empirical study，方法创新不足以进入 main conference）；R1 降级为 MAJOR（好的 empirical findings 在 EMNLP 有先例，但需要统计基础更牢固）。最终评分差异（R2: 3.0 vs R1: 3.5）主要源于此分歧。
- **Dev→Test 20pp drop 的严重性**：R1 标为 MAJOR（可能存在 dev overfitting），R2 REBUT（method ranking 完全保持 ρ=1.0，drop 可归因于 annotation density 差异 2.82×）。R1 在交叉回应中未反驳 R2 的 rebuttal，此分歧倾向 R2 观点——drop 不影响 relative comparison 有效性。

---

## Questions

**Q1.** Cross-method EDCR 相关性 (ρ=−0.89, n=7) 中，移除 GRPO QLoRA collapse 极端数据点后，ρ 和 p-value 变为多少？（R1-Q1, R2-Q3）

**Q2.** RSFT variance 声明中的 "4.6–31×" 区间，请提供每个 scale 的 SFT std 和 RSFT std 的 95% CI（基于 χ² 分布）。（R1-Q2）

**Q3.** DPO 3-epoch 的 "earlier evaluation protocol" 与当前 protocol 的具体差异是什么？对 Rel-F1 和 Evi-F1 的影响幅度？（R1-Q3）

**Q4.** GRPO collapse 是否在其他 KL 系数（如 0.1, 0.5）或不使用 QLoRA 时依然发生？Quantization precision 是 collapse 的主因还是 GRPO 方法本身？（R2-Q2）

**Q5.** CED 的减法公式 (p⁺ − max p⁻_j) 是否尝试过其他组合方式（ratio、log-ratio）？（R1-Q5）

**Q6.** RSFT "avoids decoupling" 的机制解释（Section F, "discrete selection"）在 N→∞ 的极限下是否依然成立？（R2-Q5）

**Q7.** DocRED 标注密度 vs Re-DocRED（2.82× 差异）对 CED 的 negative samples 可靠性有何影响？（R2-Q4）

---

## Missing References

1. **LMRC** (Li, X. & Zhang, M., 2024; arXiv 2408.13889) — LLM with Relation Classifier for DocRE，重要 LLM-based DocRE baseline（R2-W4, R1 AGREE）
2. **SummaC** (Laban et al., 2022, TACL) — NLI-based faithfulness evaluation 先驱，CED 设计理念直接相关（R2-W4, R1 AGREE）
3. **RelPrior** (Huang et al., 2025; arXiv 2511.08143) — Relation as a Prior for LLM-based DocRE（R2-W4）
4. **Rationale Verification for RE** (Li et al., 2025, AAAI) — RE 中的 rationale verification（R2-W4）
5. **Reward hacking 综述** — GRPO collapse 分析的理论背景（R2-W3）

---

## External Review

外部审稿未请求（项目配置未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成。3 个 warnings，9 个 info：

**Warnings：**
1. **主文无 figure**：8 页主文包含 0 个 figure，所有 4 个 figure 全在 appendix（p13/p16/p17）。对实证为主的论文，审稿人前 5 页翻阅无视觉锚点，第一印象为"文字墙"。建议将 Figure 1（decoupling spectrum scatter plot）移入主文 Section 4.3。
2. **Display items 密度低**：主文仅 3 个 display items（全部 table），低于实证论文 8 页 5-8 个的典型密度。
3. **Pages 1-5 无视觉元素**：连续 5 页纯文本。

**Info（良好）：**
- Tables 使用 booktabs 风格，格式规范，最优值加粗
- References 无 [?] 未解析引用
- EDCR 公式渲染正确
- 末页内容充实无大面积空白

**建议**：将 Figure 1（decoupling spectrum）和/或 Figure 2（scaling bars）移入主文。Figure 4 的红绿色标对色盲不友好（约 8% 男性读者），建议改为红蓝或 Okabe-Ito 色板。

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 — 方法合理但统计推断基础薄弱（n=3 variance, EDCR shared-component） |
| Excitement | 3.5/5 | 2.5/5 | 3/5 — 分析视角有启发但方法创新有限，核心 insight (selection > gradient for multi-objective) 不算新颖 |
| Reproducibility | 4/5 | 4/5 | 4/5 — Hyperparameters 详尽，数据集公开，声明开源 |
| Overall | 3.5/5 | 3.0/5 | **3.0/5 — Findings** |

### 置信度：4/5（两位 Reviewer 均对 DocRE 和 LLM post-training 方法较为熟悉）

### Overall Score: 3.0（Findings — 可被 Findings 接收）

### 理由

本文是一项覆盖面广、分析深入的 empirical study。Evidence tax 的 scale-dependency 发现和 RSFT variance compression 的实践价值是真实的贡献。但论文面临两层核心问题：

**第一层：统计方法论薄弱（R1 主要关注）。** n=3 的方差压缩声明（"4.6-31×"）在统计上不可靠——置信区间跨越数个数量级；EDCR 的 shared-component 构造了与 Rel-F1 的机械性负相关，n=7 的 cross-method 验证受极端点主导。这些问题可在 revision 中通过增加 seeds 和提供 partial correlation 来修复。

**第二层：方法论原创性不足（R2 主要关注）。** 三个贡献均为经验观察：evidence tax 是实验发现、decoupling spectrum 反映已知的 gradient vs selection 差异、RSFT 是 well-established 方法的应用。CED 的 contrastive formulation 与 flat-NLI 差异仅 0.02pp，EDCR 是两个 recall 的简单比值。这一问题在 revision 中较难根本解决。

两层问题叠加：如果统计基础更牢固，empirical study 的定位仍可支撑 Findings 甚至 Borderline Conference（R1 观点）；但在当前统计基础下，empirical findings 的可信度和方法创新的缺乏共同限制了论文水平。

**相比 Round 1 的改进**：test set 评估（5 scale, ρ=1.0）、3-seed 覆盖、matched@2048 protocol、random baseline、encoder comparison table、MTL 引用——这些显著改善了论文质量，从 Round 1 的多项 CRITICAL 格式/数据缺失问题到 Round 2 的主要争议集中在统计方法论和原创性深度。

**上调条件**：
- 3.0 → 3.5（Borderline Conference）：修复 W1（增加 seeds 或降级声明）+ W2（EDCR partial correlation）+ 移入至少 1 个 figure 到主文
- 3.5 → 4.0（Conference）：以上 + 深化 GRPO collapse 机制分析 + 补充 missing references + 重新定位 CED 角色

---

## Detailed Comments

### Section 1 (Introduction)
- "Evidence tax" 概念和 gap 叙事有效，但 "compresses training variance 4.6-31×" 在 Abstract 中过于强调。建议改为 "substantially reduces training variance"。
- Contribution 3 的表述 "RSFT compresses training variance 4.6–31×" 应附带 caveat 说明 n=3 和方差来源差异。

### Section 3 (Method)
- CED 的 contrastive formulation（Section 3.4）：既然论文自己确认 flat-NLI 效果相当，应降低 CED 的 novelty claim，将其定位为"一种可选的评分变体"而非核心方法贡献。
- EDCR（Section 3.5）：shared-component caveat 已在论文中提及（"this correlation should be interpreted as a diagnostic pattern rather than an independent discovery"），但论文随后仍在 per-relation 分析中声称独立验证——需明确 per-relation EDCR 也有同样的 shared-component 结构。

### Section 4 (Experiments)
- Table 2 (Decoupling spectrum)：DPO 3-epoch 行应更显眼地标注 "different evaluation protocol"，或从 spectrum 分析中排除。
- Section 4.4 (Scaling)：14B RSFT test 上低于 SFT 0.37pp（Table 9 注释）应在主文讨论，不仅在脚注中。这对 scaling narrative 是一个约束。
- Table 3 (RSFT performance)：RSFT Tax 列的不同 seeds/methods（1.7B s42; 4B Method B s44; 8B, 14B: s42; LLaMA: 3-seed mean）使跨行比较复杂。建议统一或更清晰标注。

### Section 5 (Analysis)
- EDCR cross-method ρ=−0.89 (n=7)：建议附报 remove-GRPO-QLoRA 的 ρ（已有 n=6 数据 ρ=−0.83, p=0.042）。
- Per-relation ρ=−0.79 (n=76)：建议添加 partial correlation controlling for TP。

### Section 7 (Limitations)
- 缺少：(1) DocRED 证据标注不完整对 CED/EDCR 可靠性的影响；(2) GRPO/DPO/RSFT 计算成本对比；(3) 仅评估 DocRE 的 generalization 限制。

### Format
- 主文 8 页无 figure：Figure 1 (spectrum scatter) 直接可视化核心概念，强烈建议移入主文。当前 3 个 display items 密度远低于实证论文典型水平。
- Figure 4 红绿色标建议改为色盲友好配色。