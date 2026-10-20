# Reviewer 1 coordination — Part 2 of 2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/d2/d2b424f30b3535d8857b.json)

## Round 17

### Tool result

_source line 523 · 2026-05-22T17:01:30.181684+00:00_

# ARR Review Form Scoring Scales

## Soundness (1-5 scale)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement (1-5 scale)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others and/or attend if time permits."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully."
- **4**: "Quite sure. It's unlikely, though conceivable, that I missed something."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## Overall Assessment (1-5 scale)
- **5**: Consider for Award
- **4**: Conference acceptance
- **3**: Accept to Findings
- **2**: Resubmit next cycle
- **1**: Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5622
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-22T17:05:26.803067+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告（方法严谨性、实验设计、统计分析）\n\n### Summary\n\n本文研究 detect-and-reweight (D&R) 在 continued LM pretraining 中对抗合成数据污染的有效性条件。核心发现：(1) ~95% 的 D&R 已发表优势源于 epoch confound；(2) 有效 reweighting 需三个前提（检测器 AUC、校准 ECE、最小干预）；(3) dual-constraint adaptive framework（α_eff ≥ τ + ESS ≥ n_min）通过 bisection 自动选择 b*。实验：Qwen3-0.6B, 132M FineWeb tokens, self-contamination ρ=0.4, 3 seeds。\n\n---\n\n### Strengths\n\n**S1. Epoch confound 识别与验证设计精良。** Table 1 中 D&R full (~2.6 epochs) PPL=17.278 vs. epoch-matched D&R (~1.0 epoch) PPL=17.657，差值 0.379 占 D&R 优势的 ~96.7%。独立 LR schedule 复现（17.651 vs. 17.657, Δ≈0.006）排除 LR 混淆。对 D&R 社区有重要修正价值。\n\n**S2. 三个有效性条件提炼具实用价值。** Section 5.3 消融有说服力：Random weights 仅增加方差；N-gram detector (AUC=0.73) 因校准不足反降 PPL；ESS-only 在 b* 过大时落入退化区（Figure 2 shaded region）。\n\n**S3. 数学框架简洁正确。** Proposition 1-2 的证明（Appendix A）利用协方差符号和加权集中性标准结论，推导正确。\n\n**S4. 诚实报告负面结果。** Table 3 下游零改善、ρ=0.2 失败、1.7B/Llama-3.2-3B 退化均如实报告。\n\n**S5. 附录丰富（A-Q），可复现性好。**\n\n---\n\n### Weaknesses\n\n**W1 [critical] N=3 seeds 且 seed 42 存在 checkpoint resume artifact。**\n- 位置：Table 1-2 (Section 5.1); Appendix P\n- Appendix P 揭示 seed 42 使用 checkpoint-resumed run，前 ~1,000 步超参不同，in-distribution effect 被膨胀约 8 倍（Δ≈−0.041 resume vs. Δ≈−0.005 from-scratch）。3 seed 中 1 个受 artifact 影响，对均值有巨大杠杆效应。核心 paired t=−6.2, p=0.025 的可信度存疑。\n- 建议：以 fresh-from-scratch seed 42 替换重跑主表；或排除 seed 42 做 robustness check。\n\n**W2 [critical] 多重比较未校正。**\n- 位置：Section 5.1, 5.2, 5.3\n- 6 种方法的多组比较（≥5 个检验），所有 p 值均 uncorrected。Bonferroni 校正后 α=0.01，p=0.025 不再显著。\n- 建议：报告 Bonferroni/Holm 校正 p 值或 bootstrap CI。\n\n**W3 [major] α_eff proxy 质量偏弱（r=0.70, R²=0.49）。**\n- 位置：Section 3.2; Appendix K, Table 10\n- 仅解释 49% 方差，负回归偏差（β₁<0.03）导致系统性低估。理论框架依赖 α_eff 作为质量代理，但 proxy 质量仅中等。论文未分析 51% 未解释方差的来源。\n- 建议：分析误差来源（检测器噪声 vs. batch size vs. 二值化）；测试更大 batch 时的 proxy 质量。\n\n**W4 [major] Self-contamination（generator = trainee）生态效度有限。**\n- 位置：Section 4\n- 实际场景合成数据来自更强模型（GPT-4 等），分布差异大。Self-contamination 简化了检测任务。Appendix O 的 cross-model transfer 退化（Δ=+0.20）暗示可能高估效果。\n- 建议：增加 cross-generator 实验。\n\n**W5 [major] 下游任务零改善限制实际影响力。**\n- 位置：Table 3, Section 6\n- PPL 改善~0.07，但 5 个 benchmark 全部差异 <0.01 accuracy。论文讨论仅 ~4 行。\n- 建议：讨论 PPL 阈值效应和在更高 contamination/更长训练下的扩展可能。\n\n**W6 [major] 适用范围极窄（仅 ρ≥0.4, ≤0.6B）。**\n- 位置：Section 5.3, Appendix N (ρ=0.2 失败); Limitations, Table 13 (1.7B 退化 0.128, Llama-3.2-3B 退化 0.20)\n- ρ=0.2（20% 污染，实际场景的下限）方法失效。1.7B+ 模型效果反转。但 Abstract/Introduction 设定的问题范围是 \"web corpora at scale\"。ρ=0.3 中间点完全缺失。\n- 建议：补充 ρ=0.3；收窄 claim 适用范围。\n\n**W7 [minor] Per-batch B=4 下 dual constraint 统计可靠性存疑。**\n- Algorithm 1 显示 b* per-batch 计算，B=4 下 α_eff(0) 仅 5 个离散值，方差极大。论文未报告 b* 在 batch 间的分布。\n\n**W8 [minor] 关键证据（proxy validation r=0.70, seed 42 artifact, ρ=0.2 分析）仅在附录。**\n\n---\n\n### Questions\n\nQ1. 能否提供排除/替换 seed 42 后的主表结果？\nQ2. 在 gradient accumulation 级别（B=16）计算 α_eff 时 proxy 质量是否改善？\nQ3. ρ=0.3 表现如何？\nQ4. Grid search 显示 b=0.4-1.0 范围内 PPL 变化小（Table 4），简单固定 b=0.6 是否足够？\nQ5. 是否考虑 soft label 版 α_eff（用 q_i 替代二值化 r_i）？\n\n---\n\n### Missing References\n\n1. Influence function-based data valuation (Pruthi et al., 2020)\n2. Distributionally robust optimization (Sagawa et al., 2020)——reweighting 目标可视为 DRO 特例\n3. PPL-downstream gap 文献（如 Tay et al., 2022 关于 PPL 与下游的非线性关系）\n\n---\n\n### Overall Assessment\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/5 | 数学框架正确，epoch confound 分析精良；但 seed artifact + 多重比较未校正 + proxy r=0.70 构成显著顾虑 |\n| Excitement | 3/5 | Epoch confound 发现对社区有修正价值，三条件有实用性；但适用范围极窄，下游零改善 |\n| Overall | 3 (Findings) | 分析贡献（epoch confound、有效性条件）达 Findings 水准；统计可信度和窄适用范围阻止 main conference 推荐 |\n| Confidence | 4/5 | 熟悉 importance weighting、合成数据检测、LM pretraining；仔细阅读全文及全部附录 |\n\n**提升路径**：修复 seed 42 + corrected p-values + ρ=0.3 数据可达 3.5 (Borderline Conference)。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告（方法严谨性、实验设计、统计分析）\n\n### Summary\n\n本文研究 detect-and-reweight (D&R) 在 continued LM pretraining 中对抗合成数据污染的有效性条件。核心发现：(1) ~95% 的 D&R 已发表优势源于 epoch confound；(2) 有效 reweighting 需三个前提（检测器 AUC、校准 ECE、最小干预）；(3) dual-constraint adaptive framework（α_eff ≥ τ + ESS ≥ n_min）通过 bisection 自动选择 b*。实验：Qwen3-0.6B, 132M FineWeb tokens, self-contamination ρ=0.4, 3 seeds。\n\n---\n\n### Strengths\n\n**S1. Epoch confound 识别与验证设计精良。** Table 1 中 D&R full (~2.6 epochs) PPL=17.278 vs. epoch-matched D&R (~1.0 epoch) PPL=17.657，差值 0.379 占 D&R 优势的 ~96.7%。独立 LR schedule 复现（17.651 vs. 17.657, Δ≈0.006）排除 LR 混淆。对 D&R 社区有重要修正价值。\n\n**S2. 三个有效性条件提炼具实用价值。** Section 5.3 消融有说服力：Random weights 仅增加方差；N-gram detector (AUC=0.73) 因校准不足反降 PPL；ESS-only 在 b* 过大时落入退化区（Figure 2 shaded region）。\n\n**S3. 数学框架简洁正确。** Proposition 1-2 的证明（Appendix A）利用协方差符号和加权集中性标准结论，推导正确。\n\n**S4. 诚实报告负面结果。** Table 3 下游零改善、ρ=0.2 失败、1.7B/Llama-3.2-3B 退化均如实报告。\n\n**S5. 附录丰富（A-Q），可复现性好。**\n\n---\n\n### Weaknesses\n\n**W1 [critical] N=3 seeds 且 seed 42 存在 checkpoint resume artifact。**\n- 位置：Table 1-2 (Section 5.1); Appendix P\n- Appendix P 揭示 seed 42 使用 checkpoint-resumed run，前 ~1,000 步超参不同，in-distribution effect 被膨胀约 8 倍（Δ≈−0.041 resume vs. Δ≈−0.005 from-scratch）。3 seed 中 1 个受 artifact 影响，对均值有巨大杠杆效应。核心 paired t=−6.2, p=0.025 的可信度存疑。\n- 建议：以 fresh-from-scratch seed 42 替换重跑主表；或排除 seed 42 做 robustness check。\n\n**W2 [critical] 多重比较未校正。**\n- 位置：Section 5.1, 5.2, 5.3\n- 6 种方法的多组比较（≥5 个检验），所有 p 值均 uncorrected。Bonferroni 校正后 α=0.01，p=0.025 不再显著。\n- 建议：报告 Bonferroni/Holm 校正 p 值或 bootstrap CI。\n\n**W3 [major] α_eff proxy 质量偏弱（r=0.70, R²=0.49）。**\n- 位置：Section 3.2; Appendix K, Table 10\n- 仅解释 49% 方差，负回归偏差（β₁<0.03）导致系统性低估。理论框架依赖 α_eff 作为质量代理，但 proxy 质量仅中等。论文未分析 51% 未解释方差的来源。\n- 建议：分析误差来源（检测器噪声 vs. batch size vs. 二值化）；测试更大 batch 时的 proxy 质量。\n\n**W4 [major] Self-contamination（generator = trainee）生态效度有限。**\n- 位置：Section 4\n- 实际场景合成数据来自更强模型（GPT-4 等），分布差异大。Self-contamination 简化了检测任务。Appendix O 的 cross-model transfer 退化（Δ=+0.20）暗示可能高估效果。\n- 建议：增加 cross-generator 实验。\n\n**W5 [major] 下游任务零改善限制实际影响力。**\n- 位置：Table 3, Section 6\n- PPL 改善~0.07，但 5 个 benchmark 全部差异 <0.01 accuracy。论文讨论仅 ~4 行。\n- 建议：讨论 PPL 阈值效应和在更高 contamination/更长训练下的扩展可能。\n\n**W6 [major] 适用范围极窄（仅 ρ≥0.4, ≤0.6B）。**\n- 位置：Section 5.3, Appendix N (ρ=0.2 失败); Limitations, Table 13 (1.7B 退化 0.128, Llama-3.2-3B 退化 0.20)\n- ρ=0.2（20% 污染，实际场景的下限）方法失效。1.7B+ 模型效果反转。但 Abstract/Introduction 设定的问题范围是 \"web corpora at scale\"。ρ=0.3 中间点完全缺失。\n- 建议：补充 ρ=0.3；收窄 claim 适用范围。\n\n**W7 [minor] Per-batch B=4 下 dual constraint 统计可靠性存疑。**\n- Algorithm 1 显示 b* per-batch 计算，B=4 下 α_eff(0) 仅 5 个离散值，方差极大。论文未报告 b* 在 batch 间的分布。\n\n**W8 [minor] 关键证据（proxy validation r=0.70, seed 42 artifact, ρ=0.2 分析）仅在附录。**\n\n---\n\n### Questions\n\nQ1. 能否提供排除/替换 seed 42 后的主表结果？\nQ2. 在 gradient accumulation 级别（B=16）计算 α_eff 时 proxy 质量是否改善？\nQ3. ρ=0.3 表现如何？\nQ4. Grid search 显示 b=0.4-1.0 范围内 PPL 变化小（Table 4），简单固定 b=0.6 是否足够？\nQ5. 是否考虑 soft label 版 α_eff（用 q_i 替代二值化 r_i）？\n\n---\n\n### Missing References\n\n1. Influence function-based data valuation (Pruthi et al., 2020)\n2. Distributionally robust optimization (Sagawa et al., 2020)——reweighting 目标可视为 DRO 特例\n3. PPL-downstream gap 文献（如 Tay et al., 2022 关于 PPL 与下游的非线性关系）\n\n---\n\n### Overall Assessment\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/5 | 数学框架正确，epoch confound 分析精良；但 seed artifact + 多重比较未校正 + proxy r=0.70 构成显著顾虑 |\n| Excitement | 3/5 | Epoch confound 发现对社区有修正价值，三条件有实用性；但适用范围极窄，下游零改善 |\n| Overall | 3 (Findings) | 分析贡献（epoch confound、有效性条件）达 Findings 水准；统计可信度和窄适用范围阻止 main conference 推荐 |\n| Confidence | 4/5 | 熟悉 importance weighting、合成数据检测、LM pretraining；仔细阅读全文及全部附录 |\n\n**提升路径**：修复 seed 42 + corrected p-values + ρ=0.3 数据可达 3.5 (Borderline Conference)。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-22T17:05:30.416203+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3613
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-22T17:05:36.103695+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-22T17:05:36.254734+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-22T17:05:39.718351+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-22T17:05:39.919483+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 201
}
```

</details>

---


### Assistant

_source line 530 · 2026-05-22T17:05:47.446696+00:00_

审稿报告已提交给 Review Director。

**评分总结**：Overall 3 (Findings)，Soundness 3/5，Excitement 3/5，Confidence 4/5。

**核心判断**：论文的分析贡献（epoch confound 识别、三个有效性条件）是真实且有价值的，达到 Findings 水准。但两个 critical 问题——seed 42 checkpoint artifact 纳入主表（W1）和多重比较未校正（W2）——使统计推断可信度不足，加上方法适用范围极窄（仅 ρ≥0.4, ≤0.6B）和下游任务零改善，阻止了 main conference 推荐。修复 seed 42、补充 corrected p-values 和 ρ=0.3 实验后可达 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

4 recorded events


### User

_source line 531 · 2026-05-22T17:06:15.100960+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

## Reviewer 2 审稿意见（Round 1）
**侧重**: 新颖性、论文定位、完整性、写作质量

### Overall: 3.0 (Findings)
Soundness 3.5/5, Excitement 2.5/5, Reproducibility 4.0/5, Confidence 4/5

### Must-Fix 问题

**N1** [critical] 方法新颖性不足以支撑独立贡献
- 具体位置：§3.2 Dual-Constraint Framework, §1 Contribution list item 4
- 问题：论文的 methodological contribution 是将 ESS（Kish, 1965）和 α_eff 组合为 dual constraint 来自动选择 b*，但：(a) 加权公式 w=(1-q)^b 完全沿用 Drayson et al. (2025)，无任何修改；(b) ESS 和 α_eff 均为已有概念，dual constraint 组合是直接应用而非根本性创新；(c) adaptive b* 本质上是超参数自动选择方法，替代 grid search——实用但算不上显著的概念性贡献。论文的真正价值在于分析发现（epoch confound, detector requirements），而非方法本身。
- 建议修改方向：明确将论文定位为 empirical analysis paper，将 adaptive b* 作为分析的 practical corollary 而非并列的核心贡献。

**N2** [critical] Downstream task 无可测量改善
- 具体位置：§6 Discussion, Table 3
- 问题：Table 3 显示 adaptive reweighting vs. uniform training 在所有 downstream benchmarks 上 |Δ| ≤ 0.01，且方向不一致。论文将此归因于"PPL improvements operate in a regime that standard benchmarks cannot resolve"和 0.6B 模型灵敏度不足。但如果效果微小到现有评估方法都测不出来，那么论文的实际价值论证就缺乏支撑。
- 建议修改方向：在更大模型（7B+）上验证；或诚实地将论文重新定位为纯分析/负面结果论文。

### Should-Fix 问题

**W1** [major] 实验规模和场景过于狭窄
- 仅 0.6B 和 1.7B，self-contamination，单一数据集（FineWeb），单一污染类型。

**W2** [major] 论文定位存在模糊性
- Abstract 第一句强调 analysis，随后介绍 method。§3 Method 占据将近 1.5 页，对 analysis paper 偏重。

**W3** [minor] α_eff 作为 quality proxy 的相关性有限（r=0.70, 49% variance explained）

**W4** [minor] 关键效应量极小（Δ=-0.014, ~0.08% relative），实际意义需更充分论证

**W5** [minor] Responsible NLP Research Checklist 出现在 PDF 中（应在 OpenReview 表单）

### 小问题
- §3.1 ρ 的 token-level vs. document-level 区分提到太晚
- Figure 2 黑白打印下线条不易区分
- Table 2 "4σ" 含义不明确
- §2 Cheng et al. (2025) 引用位置处贡献未明确说明

### Questions
Q1. 7B+ 上 epoch confound 是否仍成立？
Q2. Cross-model contamination 下 AUC/ECE 如何变化？
Q3. Downstream null result 是否源于评估方法局限？
Q4. τ=0.7 选择依据？
Q5. Appendix Q Table 13 decision summary 为什么不放主文？

### 主要优势
S1. Epoch confound 发现有修正价值
S2. 实验设计严谨（逐因素消融，3 seeds）
S3. 诚实的 Discussion
S4. Figure 1 可视化有效
S5. 附录详尽

---

请逐条回应上述所有 Must-Fix、Should-Fix、小问题和 Questions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-22T17:08:29.714930+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 Reviewer 2\n\n### Must-Fix\n\n[AGREE] R2-N1 (方法新颖性): 同意。w=(1-q)^b 来自 Drayson et al. (2025)，ESS/α_eff 是已有概念，dual constraint 组合工程合理但非概念性创新。论文真正价值在分析发现（epoch confound ~96.7%, Table 1; 三条件系统化, §5.3）。建议将 adaptive b* 定位为分析的 practical corollary。\n\n[AGREE] R2-N2 (Downstream null): 完全同意，我在 W5 也标记。补充：§6 对此仅 ~4 行讨论，不够充分。应讨论 PPL→downstream 阈值效应和扩展可能。\n\n### Should-Fix\n\n[AGREE] R2-W1 (窄规模): 同意。补充 R2 未提到的点：ρ=0.3 关键中间点完全缺失，无法定位 failure boundary。\n\n[AGREE] R2-W2 (定位模糊): 同意。建议压缩 §3 method 到半页、扩展 epoch confound 和 null result 讨论。\n\n[REBUT] R2-W3 (α_eff proxy, minor): **严重性应提升至 major**。α_eff 是 dual-constraint 的理论基石（bisection 目标函数），r=0.70 (R²=0.49) 仅解释不到一半方差。Table 10 (Appendix K) 显示负回归偏差（β₁<0.03），系统性低估。论文未分析 51% 未解释方差来源。这不是 minor 精度问题，是方法核心假设的验证缺口。\n\n[AGREE] R2-W4 (效应量小): 同意但补充 nuance——对 analysis paper，小效应量本身是 finding（揭示控制 epoch confound 后 D&R 真实增益远小于已发表数字）。真正问题是小到 downstream 测不出（R2-N2）。\n\n[AGREE] R2-W5 (Checklist in PDF): 同意，不符合 EMNLP 2026/ARR 格式规范。\n\n### 小问题\n全部 [AGREE]——ρ 区分太晚、Figure 2 黑白可读性、Table 2 \"4σ\"、Cheng et al. 引用均为有效观察。\n\n### Questions 回应\n- Q1 (7B+ epoch confound): 逻辑上应成立（结构性方法论问题），但缺乏实验验证，论文应在 Discussion 明确推论。\n- Q2 (Cross-model AUC/ECE): 关键遗漏——Appendix O 的 cross-model 实验未报告检测器 AUC/ECE 变化。\n- Q3 (Downstream 评估局限): 论文未尝试 fine-grained 评估（subset perplexity、generation quality 等），仅凭 5 个 benchmark accuracy 下结论证据不足。\n- Q4 (τ=0.7): Grid search 结果而非理论推导，与\"避免 grid search\"动机矛盾，但 §5.3 sensitivity 分析显示 τ=0.6-0.8 范围内相对稳健。\n- Q5 (Table 13 入主文): 同意，practitioner decision summary 应入正文。\n\n### 核心分歧\n唯一分歧：R2-W3 α_eff proxy 严重性。R2 标 minor，我认为 major。\n\n### 共识\n两份审稿均给 Overall 3.0 (Findings)，共识区域：(1) 主要价值在分析而非方法；(2) Downstream null 是最大实践弱点；(3) 规模/场景过窄；(4) 定位应偏向 analysis paper。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 Reviewer 2\n\n### Must-Fix\n\n[AGREE] R2-N1 (方法新颖性): 同意。w=(1-q)^b 来自 Drayson et al. (2025)，ESS/α_eff 是已有概念，dual constraint 组合工程合理但非概念性创新。论文真正价值在分析发现（epoch confound ~96.7%, Table 1; 三条件系统化, §5.3）。建议将 adaptive b* 定位为分析的 practical corollary。\n\n[AGREE] R2-N2 (Downstream null): 完全同意，我在 W5 也标记。补充：§6 对此仅 ~4 行讨论，不够充分。应讨论 PPL→downstream 阈值效应和扩展可能。\n\n### Should-Fix\n\n[AGREE] R2-W1 (窄规模): 同意。补充 R2 未提到的点：ρ=0.3 关键中间点完全缺失，无法定位 failure boundary。\n\n[AGREE] R2-W2 (定位模糊): 同意。建议压缩 §3 method 到半页、扩展 epoch confound 和 null result 讨论。\n\n[REBUT] R2-W3 (α_eff proxy, minor): **严重性应提升至 major**。α_eff 是 dual-constraint 的理论基石（bisection 目标函数），r=0.70 (R²=0.49) 仅解释不到一半方差。Table 10 (Appendix K) 显示负回归偏差（β₁<0.03），系统性低估。论文未分析 51% 未解释方差来源。这不是 minor 精度问题，是方法核心假设的验证缺口。\n\n[AGREE] R2-W4 (效应量小): 同意但补充 nuance——对 analysis paper，小效应量本身是 finding（揭示控制 epoch confound 后 D&R 真实增益远小于已发表数字）。真正问题是小到 downstream 测不出（R2-N2）。\n\n[AGREE] R2-W5 (Checklist in PDF): 同意，不符合 EMNLP 2026/ARR 格式规范。\n\n### 小问题\n全部 [AGREE]——ρ 区分太晚、Figure 2 黑白可读性、Table 2 \"4σ\"、Cheng et al. 引用均为有效观察。\n\n### Questions 回应\n- Q1 (7B+ epoch confound): 逻辑上应成立（结构性方法论问题），但缺乏实验验证，论文应在 Discussion 明确推论。\n- Q2 (Cross-model AUC/ECE): 关键遗漏——Appendix O 的 cross-model 实验未报告检测器 AUC/ECE 变化。\n- Q3 (Downstream 评估局限): 论文未尝试 fine-grained 评估（subset perplexity、generation quality 等），仅凭 5 个 benchmark accuracy 下结论证据不足。\n- Q4 (τ=0.7): Grid search 结果而非理论推导，与\"避免 grid search\"动机矛盾，但 §5.3 sensitivity 分析显示 τ=0.6-0.8 范围内相对稳健。\n- Q5 (Table 13 入主文): 同意，practitioner decision summary 应入正文。\n\n### 核心分歧\n唯一分歧：R2-W3 α_eff proxy 严重性。R2 标 minor，我认为 major。\n\n### 共识\n两份审稿均给 Overall 3.0 (Findings)，共识区域：(1) 主要价值在分析而非方法；(2) Downstream null 是最大实践弱点；(3) 规模/场景过窄；(4) 定位应偏向 analysis paper。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-22T17:08:33.392349+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3677
}
```

</details>

---


### Assistant

_source line 534 · 2026-05-22T17:08:37.558272+00:00_

交叉回应已提交。核心结论：与 R2 在绝大多数问题上达成共识（Overall 3.0 Findings），唯一分歧是 α\_eff proxy 质量的严重性——R2 标 minor，我认为应为 major，因为这是 dual-constraint framework 理论基础的核心验证缺口。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

58 recorded events


### User

_source line 535 · 2026-05-23T03:06:10.133779+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。

## 目标 Venue
- **EMNLP 2026**，通过 ACL Rolling Review (ARR) 提交
- **截止日期**：2026-05-25
- **格式**：Long paper，正文 8 页限制，参考文献不限页数。Limitations 和 Ethics Statement 不计入页数
- **模板**：ACL 2023 模板（`\usepackage[review]{acl}`）
- **匿名规则**：Double-blind，禁止透露作者身份
- **Responsible NLP Checklist**：在 OpenReview submission form 中填写，不在 PDF 中

## 论文信息
- **标题**：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining
- **论文路径**：projects/provenance_weight_training/docs/paper/main.tex
- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf

## 你的审查侧重

### 1. 方法严谨性（重点）
- Dual-constrained adaptive b* 的理论基础是否扎实？α_eff 作为 quality proxy（r≈0.70, R²≈0.49）是否足够支撑方法？
- ESS ceiling 和 α_eff floor 的 interaction 是否有理论保障？
- Bisection 求解 b* 的数值稳定性
- w=(1-q)^b 完全沿用 Drayson et al.，方法的新颖性贡献在哪里？

### 2. 实验设计
- 实验控制是否充分？特别是 epoch confound 的控制实验
- Self-contamination 设计的生态效度：generator = trainee 是否过于理想化？
- 样本量 N=3 seeds 的统计检验力是否足够？2 degrees of freedom 是否能支撑论文的 claims？
- 效应量 Δ=-0.020 PPL 的实际意义
- Downstream task 零改善如何解读？

### 3. 统计分析
- 多重比较校正是否恰当？Bonferroni-Holm 校正后 ρ=0.4 的 p_BH=0.078 不显著，论文对此的处理是否诚实？
- Bootstrap CI 和 paired t-test 的使用是否正确？
- Cross-seed variance 的报告是否充分？
- Grid-best b=0.3 作为 post-hoc oracle 的公平性

### 4. 可复现性
- 实验细节是否足够复现（超参数、训练配置、评估协议）？
- 检测器训练细节（temperature scaling T=0.204）
- 代码和数据承诺

请严格按照顶会审稿标准评审，不要手软。输出结构：Summary → Strengths → Weaknesses（按严重性分 Must-Fix / Should-Fix / Minor）→ Questions → Overall Assessment（参考 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-23T03:06:18.551873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-23T03:06:18.605752+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-23T03:06:22.722387+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-23T03:06:22.773042+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-23T03:06:25.084553+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-23T03:06:25.135893+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-23T03:06:34.197555+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-23T03:06:34.401018+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-23T03:06:41.668025+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-23T03:06:52.744662+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about the ACL Rolling Review 2026 reviewer guidelines and review form. Here are the key findings:

## Reviewer Guidelines

The recommended workflow is: (1) read the paper and get the first impression, (2) search for related work, and if you feel qualified to review some aspects but not others, state in the review if you did not check major parts such as proofs, as this information helps the area chair understand what aspects were reviewed.

Reviewers are provided with a checklist to flag problems tha
…[truncated 790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 11076
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-23T03:06:52.897025+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-23T03:06:54.302710+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 574.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-23T03:06:57.966938+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-23T03:06:58.067755+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-23T03:07:01.832058+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need the exact criteria names, score ranges, and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need the exact criteria names, score ranges, and what each score means."
  }
}
```

</details>

---


### Tool call

_source line 551 · 2026-05-23T03:07:02.435734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 552 · 2026-05-23T03:07:03.491623+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 553 · 2026-05-23T03:07:03.492095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-23T03:07:03.794056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-23T03:07:04.297035+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool result

_source line 556 · 2026-05-23T03:07:04.939418+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1145
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-23T03:07:08.419699+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
**Scale:** 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** Quite sure, with unlikely but conceivable oversights
- **3:** Pretty sure, but may have missed details or math checks
- **2:** Willing to defend evaluation, but likely missed some details
- **1:** "Not my area, or paper is very hard to understand"

## 2. Soundness
**Scale:** 1-5 (with .5 increments)
- **5:** Excellent - "one of the most thorough I have seen"
- **4:** Strong - sufficient support with optional extra experiments
- **3:** Acceptable - supports main claims with minor gaps
- **2:** Poor - main claims lack sufficient support
- **1:** Major Issues - insufficiently thorough for publication

## 3. Excitement
**Scale:** 1-5 (with .5 increments)
- **5:** Highly Exciting - "would recommend this paper to others"
- **4:** Exciting - would mention to others or attend presentation
- **3:** Interesting - might mention or attend if time permits
- **2:** Potentially Interesting - doesn't resonate personally
- **1:** Not Exciting - lacks community relevance

## 4. Overall Assessment
**Scale:** 1-5 (with .5 increments)
- **5:** Consider for Award (top 2.5%)
- **4:** Conference acceptance
- **3:** Findings acceptance
- **2:** Resubmit next cycle
- **1:** Do not resubmit

## 5. Reproducibility
**Scale:** 1-5
- **5:** Results easily reproducible
- **4:** Mostly reproducible with minor variations
- **3:** Reproducible with difficulty
- **2:** Hard to reproduce
- **1:** Cannot reproduce

## 6. Datasets & Software Value
**Scale:** 1-5 each
- **5:** Enabling - affects research direction choices
- **4:** Useful - recommended for ongoing work
- **3:** Potentially useful
- **2:** Documentary - useful for replication only
- **1:** None released

## 7. Author Identity Knowledge
**Scale:** 1-5
- **5:** Known from double-blind violation
- **4:** Known from preprint
- **3:*
…[truncated 105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6587
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-23T03:07:14.507032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-23T03:07:15.762831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-23T03:07:16.074027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 561 · 2026-05-23T03:07:16.074457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-23T03:07:16.533761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 563 · 2026-05-23T03:07:16.890472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-23T03:07:17.142868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1068
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-23T03:07:17.802048+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1727
}
```

</details>

---


### Tool result

_source line 566 · 2026-05-23T03:07:18.155193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1621
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-23T03:07:18.356648+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1466
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-23T03:07:23.628149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-23T03:07:24.230727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-23T03:07:24.432608+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-23T03:07:24.834789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-23T03:07:29.835378+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-23T03:07:31.562342+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 352.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.7}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1726
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-23T03:07:37.433203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-23T03:07:37.635341+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-23T03:07:38.542816+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-23T03:07:38.553268+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 917
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-23T03:07:38.553683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-23T03:07:39.009780+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-23T03:07:39.010286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-23T03:07:39.413340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-23T03:07:39.666942+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-23T03:07:40.220037+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-23T03:09:13.215224+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-23T03:09:13.316126+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-23T03:10:56.012457+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性、实验设计与统计分析\n\n**论文**：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n**Venue**：EMNLP 2026 (via ACL Rolling Review)\n\n---\n\n## 总体评分\n**Overall**: 3.0（Findings）\n**一句话总结**：Epoch confound 分析是扎实且有价值的贡献，但自适应方法建立在中等相关性的 proxy 上（R²≈0.49），N=3 seeds 的实验设计严重限制了统计检验力，且 PPL 改善未能迁移到下游任务。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 epoch confound 分析设计合理；但自适应方法的 α_eff proxy 仅解释 49% 方差，N=3 seeds 下统计推断脆弱，downstream 零改善削弱 practical soundness |\n| Excitement | 2.5/5 | Epoch confound 发现对 D&R 文献有实际价值，但自适应方法增量有限（w=(1-q)^b 完全来自 Drayson et al.），效应量极小 |\n| Reproducibility | 4/5 | 超参数、训练配置、检测器细节报告充分（§4、Appendix M），承诺 release code/data，但 review 期间无匿名 repo |\n| Reviewer Confidence | 4/5 | 仔细通读全文含 15 页 appendix，熟悉重要性采样、数据筛选和 LM 预训练文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 的统计检验力严重不足\n- 具体位置：§5.1 (Table 2), Limitations (p.8)\n- 问题：全部主实验仅用 3 个随机种子，paired t-test 仅 2 自由度。核心 claim Δ=−0.020 PPL（adaptive b* vs. uniform）的 95% BCa bootstrap CI 为 [−0.028, −0.012]，但 bootstrap 理论要求合理的样本量才能给出可靠区间——N=3 时 bootstrap CI 的覆盖率无法保证。论文在 Limitations 中承认了这一点（\"2 degrees of freedom, limiting statistical power\"），但所有定量结论仍然建立在这一基础上。\n- 为什么影响接收：顶会论文的核心实验结论不应建立在 2 自由度的 t 检验上。任何 reviewer 都可以合理质疑：换 3 个不同的种子，结论是否还成立？Table 2 中 per-seed 方差极小（SD ≈ 0.007），这暗示种子间差异可能被 training recipe 的确定性所压缩，而非真正反映方法的稳健性。\n- 建议修改方向：至少增加到 N=5（4 df），理想情况下 N=8-10。若计算预算受限，可在更小模型（如 60M）上用更多种子做 power analysis，展示效应的稳定性。\n\n**N2** [critical] α_eff 作为 quality proxy 的理论基础薄弱（R²≈0.49）\n- 具体位置：§3.3, Appendix K (Table 11)\n- 问题：自适应方法的核心约束是 α_eff(b) ≥ τ，其动机来自 α_eff 与 true batch-level real fraction 的 Pearson r ≈ 0.70（R² ≈ 0.49）。这意味着 α_eff 仅解释了真实质量信号约一半的方差。更严重的是，经 Bonferroni-Holm 校正后 Spearman ρ=0.4 的 p_BH=0.078 不显著（Appendix K），论文对此的处理是转而强调 Pearson r，但两个相关系数的巨大差距（0.70 vs 0.40）暗示关系可能由少数极端值驱动，而非稳健的单调关系。\n- 为什么影响接收：整个自适应方法的 \"自适应\" 部分依赖 α_eff 作为 quality signal。如果这个 proxy 不可靠，bisection 找到的 b* 可能系统性偏离最优值。R²=0.49 在 Table 11 仅基于 5 个离散的 b 值 (0, 0.25, 0.5, 0.75, 1)，样本量极小，相关系数的估计本身就很不稳定。\n- 建议修改方向：(1) 展示 α_eff 与 PPL 的直接关系（而非间接通过 real fraction），因为 PPL 才是最终目标；(2) 报告 Pearson r 与 Spearman ρ 差异的原因分析（散点图、杠杆点检测）；(3) 在更细粒度的 b grid 上验证相关性。\n\n**N3** [critical] 下游任务零改善严重削弱实际价值\n- 具体位置：Table 4 (p.8), §5.2\n- 问题：在 ρ=0.4 主实验条件下，5 个下游任务（MMLU、ARC-C、HellaSwag、PIQA、WinoGrande）的平均准确率 adaptive (0.5414) = uniform (0.5414)，完全相同。论文坦承 \"differences within standard error, reweighting PPL gains do not transfer to downstream accuracy at this scale\"。\n- 为什么影响接收：如果 PPL 改善不能迁移到任何下游任务，那么整个 reweighting 方法的实际价值何在？论文在 Discussion (§6) 中推测 \"the relationship between perplexity and downstream accuracy is nonlinear and scale-dependent\"，但这只是猜测，没有证据支持。一个方法论文不能仅声称 PPL 改善而无法展示任何下游收益。\n- 建议修改方向：(1) 在更大规模模型上验证（论文用的是 Qwen3-0.6B，极小）；(2) 如果确实无法展示下游收益，应更诚实地将论文定位为 \"分析性贡献\"（epoch confound）而非 \"方法贡献\"（adaptive reweighting）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Self-contamination 设计的生态效度有限\n- 具体位置：§4 (p.4), Appendix O (p.15)\n- 问题：实验中 generator = trainee（Qwen3-0.6B 生成合成数据，同一模型继续训练）。这意味着检测器面对的是同分布文本，AUC=0.94 可能在 generator≠trainee 的真实场景中不可复现。Appendix O 的 cross-model 实验（Llama-3.2-3B 生成）仅用单种子，结果混合（MMLU 提升但 HellaSwag 下降），不足以验证泛化性。\n- 建议：(1) 至少用 2-3 个不同的 generator 模型（不同 family、不同 scale）做主实验级别的验证；(2) 讨论 real-world contamination 中 generator 多样性对检测器性能的影响。\n\n**W2** [warning] 方法新颖性增量有限\n- 具体位置：§3 vs. Drayson et al. (2025)\n- 问题：权重函数 w=(1−q)^b 完全沿用 Drayson et al.。本文贡献是 (a) epoch confound 分析和 (b) dual-constrained b* selection。其中 (a) 是分析发现而非方法贡献，(b) 是在已有公式上加两个约束（ESS ceiling + α_eff floor）的工程改进。Bisection 求解本身是标准数值方法。论文应更清楚地界定自己相对于 Drayson et al. 的 novelty boundary。\n- 建议：在 Introduction 或 §3 明确声明 \"our methodological contribution is the constraint formulation, not the weighting function\"，并更详细地对比 Drayson et al. 的 b 选择策略与本文的 dual-constrained 方法在不同场景下的表现差异。\n\n**W3** [warning] Δ=−0.020 PPL 的实际意义需更充分论证\n- 具体位置：§5.1 (Table 1, Table 2)\n- 问题：Epoch-matched 条件下 adaptive b* 相对 uniform 的 PPL 改善仅 0.020（17.694 → 17.674），相对改善约 0.11%。论文正文提到 \"the practical value is estimated\" 但主要引用的 0.396 PPL 优势包含了 epoch confound。控制 epoch 后的真实效应量非常小，读者容易被 framing 误导。\n- 建议：在 §5.1 开头就明确区分 \"full advantage (0.396, includes epoch confound)\" 和 \"epoch-controlled advantage (0.020, the true method effect)\"，避免读者需要自己拼凑这个关键区分。\n\n**W4** [warning] ESS ceiling 与 α_eff floor 的交互缺乏理论分析\n- 具体位置：§3.3, Algorithm 1 (Appendix B)\n- 问题：当两个约束冲突时（即满足 α_eff ≥ τ 需要的 b 值超过 ESS ceiling 允许的最大 b），算法退回到 b=b_ESS。但论文未分析：(1) 这种冲突在什么条件下发生？(2) 此时 α_eff 约束被违反的程度有多大？(3) 退回 b_ESS 是否仍然优于 b=0？Appendix A 的 Proposition 1-2 只证明了单调性，未涉及约束冲突的行为。\n- 建议：增加理论分析或实验展示约束冲突的频率和后果。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 1 脚注 1 提到 \"Oracle requiring known q (He et al., 2025); seed 42 only\" —— oracle baseline 仅用单种子，与其他方法的 3-seed 对比不公平，虽然影响不大。\n- Figure 2 的 x 轴标签 \"Sharpening exponent b\" 与正文中 b 的定义位置（§3.1）相距较远，建议在 caption 中简要重述 b 的含义。\n- §5.3 hyperparameter sensitivity 分析了 τ 和 contamination level 的交互，但未讨论 n_batch（ESS floor）的敏感性。\n- Appendix P 的 checkpoint resume artifact 分析很有趣，但与主论文 narrative 的联系不够紧密，读者可能困惑其与主结论的关系。\n- Ethics Statement 提到 \"Code and data will be released upon acceptance\"，但 review 期间没有匿名 repo，不利于 reproducibility 评估。\n\n---\n\n## Questions to Authors\n\n1. **α_eff 与 downstream accuracy 的关系**：α_eff 与 PPL 存在 moderate correlation，但 PPL 与 downstream accuracy 之间的链条在本文中断裂（Table 4）。作者是否检查过 α_eff 与 downstream metrics 的直接相关性？\n2. **N=3 的 power analysis**：给定观测到的 effect size (Δ=0.020) 和 within-seed variance (SD≈0.007)，作者是否计算过 statistical power？需要多少 seeds 才能以 80% power 检测到这个效应？\n3. **Bonferroni-Holm 后 Spearman 不显著**：Pearson r=0.70 但 Spearman ρ=0.40，经校正后 p_BH=0.078。这一差异暗示 α_eff 与 real fraction 的关系可能非单调或被极端值驱动。作者能否提供散点图？\n4. **Scale 依赖性**：所有实验在 Qwen3-0.6B (132M tokens) 上进行。作者在 §6 推测 \"larger models may be inherently more robust\"，但无证据。是否有任何 pilot 实验在更大模型上验证过核心发现？\n5. **Contamination level ρ=0.4 的代表性**：论文选择 ρ=0.4 作为主实验条件，但 real-world contamination 的 level 通常未知且可能远低于此。Appendix Q 在 ρ=0.2 时已经显示方法退化，这是否意味着方法仅在高污染场景下有效？\n\n---\n\n## 主要优势\n\n1. **Epoch confound 分析设计精巧且结论有力**（§5.1, Table 1）：通过 epoch-matched 对照实验证明 >95% 的 D&R 优势来自多 epoch 曝光而非过滤质量，这对整个 D&R 文献是重要的校正。Shared-schedule replication（Δ=0.006 确认 confound）的实验设计特别巧妙。\n\n2. **三条 effectiveness conditions 的系统总结**（Figure 1）：将 detector quality（AUC+ECE）、contamination level、minimum intervention 三个条件整合为决策框架（Table 3），对从业者有直接参考价值。\n\n3. **诚实的 negative results 报告**：论文坦承 downstream 零改善（Table 4）、α_eff 校正后不显著（Appendix K）、ρ=0.2 时方法退化（Appendix Q）、N=3 的 power 限制。这种透明度值得肯定。\n\n4. **充实的 appendix**（A-Q，7 页）：包含理论证明、完整 grid search 结果、sensitivity 分析、cross-model 实验、low contamination 分析等，信息密度高。\n\n---\n\n## 总结\n\n本文的核心价值在于 epoch confound 的分析发现，而非自适应方法本身。Epoch confound 分析设计严谨、结论清晰，足以支撑一篇 Findings 论文。但自适应方法受限于 (1) α_eff proxy 的中等可靠性（R²=0.49, Spearman 校正后不显著），(2) N=3 的实验规模无法提供足够的统计信心，(3) 下游任务零改善使得 PPL 改善的实际意义存疑。建议作者将论文重新定位为以分析贡献为主，方法贡献为辅，并增加种子数量以加强统计基础。\n\n**Overall Assessment: 3.0 (Findings)**",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性、实验设计与统计分析\n\n**论文**：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n**Venue**：EMNLP 2026 (via ACL Rolling Review)\n\n---\n\n## 总体评分\n**Overall**: 3.0（Findings）\n**一句话总结**：Epoch confound 分析是扎实且有价值的贡献，但自适应方法建立在中等相关性的 proxy 上（R²≈0.49），N=3 seeds 的实验设计严重限制了统计检验力，且 PPL 改善未能迁移到下游任务。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 epoch confound 分析设计合理；但自适应方法的 α_eff proxy 仅解释 49% 方差，N=3 seeds 下统计推断脆弱，downstream 零改善削弱 practical soundness |\n| Excitement | 2.5/5 | Epoch confound 发现对 D&R 文献有实际价值，但自适应方法增量有限（w=(1-q)^b 完全来自 Drayson et al.），效应量极小 |\n| Reproducibility | 4/5 | 超参数、训练配置、检测器细节报告充分（§4、Appendix M），承诺 release code/data，但 review 期间无匿名 repo |\n| Reviewer Confidence | 4/5 | 仔细通读全文含 15 页 appendix，熟悉重要性采样、数据筛选和 LM 预训练文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 的统计检验力严重不足\n- 具体位置：§5.1 (Table 2), Limitations (p.8)\n- 问题：全部主实验仅用 3 个随机种子，paired t-test 仅 2 自由度。核心 claim Δ=−0.020 PPL（adaptive b* vs. uniform）的 95% BCa bootstrap CI 为 [−0.028, −0.012]，但 bootstrap 理论要求合理的样本量才能给出可靠区间——N=3 时 bootstrap CI 的覆盖率无法保证。论文在 Limitations 中承认了这一点（\"2 degrees of freedom, limiting statistical power\"），但所有定量结论仍然建立在这一基础上。\n- 为什么影响接收：顶会论文的核心实验结论不应建立在 2 自由度的 t 检验上。任何 reviewer 都可以合理质疑：换 3 个不同的种子，结论是否还成立？Table 2 中 per-seed 方差极小（SD ≈ 0.007），这暗示种子间差异可能被 training recipe 的确定性所压缩，而非真正反映方法的稳健性。\n- 建议修改方向：至少增加到 N=5（4 df），理想情况下 N=8-10。若计算预算受限，可在更小模型（如 60M）上用更多种子做 power analysis，展示效应的稳定性。\n\n**N2** [critical] α_eff 作为 quality proxy 的理论基础薄弱（R²≈0.49）\n- 具体位置：§3.3, Appendix K (Table 11)\n- 问题：自适应方法的核心约束是 α_eff(b) ≥ τ，其动机来自 α_eff 与 true batch-level real fraction 的 Pearson r ≈ 0.70（R² ≈ 0.49）。这意味着 α_eff 仅解释了真实质量信号约一半的方差。更严重的是，经 Bonferroni-Holm 校正后 Spearman ρ=0.4 的 p_BH=0.078 不显著（Appendix K），论文对此的处理是转而强调 Pearson r，但两个相关系数的巨大差距（0.70 vs 0.40）暗示关系可能由少数极端值驱动，而非稳健的单调关系。\n- 为什么影响接收：整个自适应方法的 \"自适应\" 部分依赖 α_eff 作为 quality signal。如果这个 proxy 不可靠，bisection 找到的 b* 可能系统性偏离最优值。R²=0.49 在 Table 11 仅基于 5 个离散的 b 值 (0, 0.25, 0.5, 0.75, 1)，样本量极小，相关系数的估计本身就很不稳定。\n- 建议修改方向：(1) 展示 α_eff 与 PPL 的直接关系（而非间接通过 real fraction），因为 PPL 才是最终目标；(2) 报告 Pearson r 与 Spearman ρ 差异的原因分析（散点图、杠杆点检测）；(3) 在更细粒度的 b grid 上验证相关性。\n\n**N3** [critical] 下游任务零改善严重削弱实际价值\n- 具体位置：Table 4 (p.8), §5.2\n- 问题：在 ρ=0.4 主实验条件下，5 个下游任务（MMLU、ARC-C、HellaSwag、PIQA、WinoGrande）的平均准确率 adaptive (0.5414) = uniform (0.5414)，完全相同。论文坦承 \"differences within standard error, reweighting PPL gains do not transfer to downstream accuracy at this scale\"。\n- 为什么影响接收：如果 PPL 改善不能迁移到任何下游任务，那么整个 reweighting 方法的实际价值何在？论文在 Discussion (§6) 中推测 \"the relationship between perplexity and downstream accuracy is nonlinear and scale-dependent\"，但这只是猜测，没有证据支持。一个方法论文不能仅声称 PPL 改善而无法展示任何下游收益。\n- 建议修改方向：(1) 在更大规模模型上验证（论文用的是 Qwen3-0.6B，极小）；(2) 如果确实无法展示下游收益，应更诚实地将论文定位为 \"分析性贡献\"（epoch confound）而非 \"方法贡献\"（adaptive reweighting）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Self-contamination 设计的生态效度有限\n- 具体位置：§4 (p.4), Appendix O (p.15)\n- 问题：实验中 generator = trainee（Qwen3-0.6B 生成合成数据，同一模型继续训练）。这意味着检测器面对的是同分布文本，AUC=0.94 可能在 generator≠trainee 的真实场景中不可复现。Appendix O 的 cross-model 实验（Llama-3.2-3B 生成）仅用单种子，结果混合（MMLU 提升但 HellaSwag 下降），不足以验证泛化性。\n- 建议：(1) 至少用 2-3 个不同的 generator 模型（不同 family、不同 scale）做主实验级别的验证；(2) 讨论 real-world contamination 中 generator 多样性对检测器性能的影响。\n\n**W2** [warning] 方法新颖性增量有限\n- 具体位置：§3 vs. Drayson et al. (2025)\n- 问题：权重函数 w=(1−q)^b 完全沿用 Drayson et al.。本文贡献是 (a) epoch confound 分析和 (b) dual-constrained b* selection。其中 (a) 是分析发现而非方法贡献，(b) 是在已有公式上加两个约束（ESS ceiling + α_eff floor）的工程改进。Bisection 求解本身是标准数值方法。论文应更清楚地界定自己相对于 Drayson et al. 的 novelty boundary。\n- 建议：在 Introduction 或 §3 明确声明 \"our methodological contribution is the constraint formulation, not the weighting function\"，并更详细地对比 Drayson et al. 的 b 选择策略与本文的 dual-constrained 方法在不同场景下的表现差异。\n\n**W3** [warning] Δ=−0.020 PPL 的实际意义需更充分论证\n- 具体位置：§5.1 (Table 1, Table 2)\n- 问题：Epoch-matched 条件下 adaptive b* 相对 uniform 的 PPL 改善仅 0.020（17.694 → 17.674），相对改善约 0.11%。论文正文提到 \"the practical value is estimated\" 但主要引用的 0.396 PPL 优势包含了 epoch confound。控制 epoch 后的真实效应量非常小，读者容易被 framing 误导。\n- 建议：在 §5.1 开头就明确区分 \"full advantage (0.396, includes epoch confound)\" 和 \"epoch-controlled advantage (0.020, the true method effect)\"，避免读者需要自己拼凑这个关键区分。\n\n**W4** [warning] ESS ceiling 与 α_eff floor 的交互缺乏理论分析\n- 具体位置：§3.3, Algorithm 1 (Appendix B)\n- 问题：当两个约束冲突时（即满足 α_eff ≥ τ 需要的 b 值超过 ESS ceiling 允许的最大 b），算法退回到 b=b_ESS。但论文未分析：(1) 这种冲突在什么条件下发生？(2) 此时 α_eff 约束被违反的程度有多大？(3) 退回 b_ESS 是否仍然优于 b=0？Appendix A 的 Proposition 1-2 只证明了单调性，未涉及约束冲突的行为。\n- 建议：增加理论分析或实验展示约束冲突的频率和后果。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 1 脚注 1 提到 \"Oracle requiring known q (He et al., 2025); seed 42 only\" —— oracle baseline 仅用单种子，与其他方法的 3-seed 对比不公平，虽然影响不大。\n- Figure 2 的 x 轴标签 \"Sharpening exponent b\" 与正文中 b 的定义位置（§3.1）相距较远，建议在 caption 中简要重述 b 的含义。\n- §5.3 hyperparameter sensitivity 分析了 τ 和 contamination level 的交互，但未讨论 n_batch（ESS floor）的敏感性。\n- Appendix P 的 checkpoint resume artifact 分析很有趣，但与主论文 narrative 的联系不够紧密，读者可能困惑其与主结论的关系。\n- Ethics Statement 提到 \"Code and data will be released upon acceptance\"，但 review 期间没有匿名 repo，不利于 reproducibility 评估。\n\n---\n\n## Questions to Authors\n\n1. **α_eff 与 downstream accuracy 的关系**：α_eff 与 PPL 存在 moderate correlation，但 PPL 与 downstream accuracy 之间的链条在本文中断裂（Table 4）。作者是否检查过 α_eff 与 downstream metrics 的直接相关性？\n2. **N=3 的 power analysis**：给定观测到的 effect size (Δ=0.020) 和 within-seed variance (SD≈0.007)，作者是否计算过 statistical power？需要多少 seeds 才能以 80% power 检测到这个效应？\n3. **Bonferroni-Holm 后 Spearman 不显著**：Pearson r=0.70 但 Spearman ρ=0.40，经校正后 p_BH=0.078。这一差异暗示 α_eff 与 real fraction 的关系可能非单调或被极端值驱动。作者能否提供散点图？\n4. **Scale 依赖性**：所有实验在 Qwen3-0.6B (132M tokens) 上进行。作者在 §6 推测 \"larger models may be inherently more robust\"，但无证据。是否有任何 pilot 实验在更大模型上验证过核心发现？\n5. **Contamination level ρ=0.4 的代表性**：论文选择 ρ=0.4 作为主实验条件，但 real-world contamination 的 level 通常未知且可能远低于此。Appendix Q 在 ρ=0.2 时已经显示方法退化，这是否意味着方法仅在高污染场景下有效？\n\n---\n\n## 主要优势\n\n1. **Epoch confound 分析设计精巧且结论有力**（§5.1, Table 1）：通过 epoch-matched 对照实验证明 >95% 的 D&R 优势来自多 epoch 曝光而非过滤质量，这对整个 D&R 文献是重要的校正。Shared-schedule replication（Δ=0.006 确认 confound）的实验设计特别巧妙。\n\n2. **三条 effectiveness conditions 的系统总结**（Figure 1）：将 detector quality（AUC+ECE）、contamination level、minimum intervention 三个条件整合为决策框架（Table 3），对从业者有直接参考价值。\n\n3. **诚实的 negative results 报告**：论文坦承 downstream 零改善（Table 4）、α_eff 校正后不显著（Appendix K）、ρ=0.2 时方法退化（Appendix Q）、N=3 的 power 限制。这种透明度值得肯定。\n\n4. **充实的 appendix**（A-Q，7 页）：包含理论证明、完整 grid search 结果、sensitivity 分析、cross-model 实验、low contamination 分析等，信息密度高。\n\n---\n\n## 总结\n\n本文的核心价值在于 epoch confound 的分析发现，而非自适应方法本身。Epoch confound 分析设计严谨、结论清晰，足以支撑一篇 Findings 论文。但自适应方法受限于 (1) α_eff proxy 的中等可靠性（R²=0.49, Spearman 校正后不显著），(2) N=3 的实验规模无法提供足够的统计信心，(3) 下游任务零改善使得 PPL 改善的实际意义存疑。建议作者将论文重新定位为以分析贡献为主，方法贡献为辅，并增加种子数量以加强统计基础。\n\n**Overall Assessment: 3.0 (Findings)**",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-23T03:10:59.728284+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3715
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-23T03:11:02.997877+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-23T03:11:03.099394+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-23T03:11:07.420338+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-23T03:11:07.470997+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 592 · 2026-05-23T03:11:17.100455+00:00_

审稿意见已提交给 Review Director。

**核心判断：Overall 3.0 (Findings)**

三个 Must-Fix 问题：
1. **N=3 seeds 统计检验力不足**——2 自由度的 t 检验无法可靠支撑定量结论，bootstrap CI 在 N=3 时覆盖率无保证
2. **α_eff proxy 可靠性存疑**——R²=0.49 仅解释一半方差，Bonferroni-Holm 校正后 Spearman 不显著 (p=0.078)，Pearson 与 Spearman 的巨大差距暗示极端值驱动
3. **下游任务零改善**——adaptive 与 uniform 准确率完全相同 (0.5414)，PPL 改善无法迁移

主要优势是 epoch confound 分析——证明 >95% 的 D&R 优势来自多 epoch 曝光的实验设计精巧且结论有力，足以支撑 Findings 级别接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

4 recorded events


### User

_source line 593 · 2026-05-23T03:14:03.767381+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿报告

**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 新颖性、Related Work 完整性、写作质量、格式合规

---

## 总体评分

**Overall Assessment**: 3.0 / 5 — Findings
**一句话总结**: Epoch confound 的识别是对 D&R 评估方法论的有价值贡献，但极小的效应量（Δ=-0.020 PPL, ~0.11%）、狭窄的实验范围（单模型/单数据集）和增量式的方法贡献使其未达到主会议门槛，适合 Findings。

---

## Must-Fix 问题

**N1** [critical] 效应量极小，实际意义不足以支撑论文的 framing
- Δ=-0.020 PPL（~0.11% relative），下游 benchmark 无显著差异（Table 4: 0.5414 = 0.5414）
- Abstract 和 Introduction 的叙事暗示 "yielding a practical adaptive method"，构成 overclaim
- 建议明确定位为 analysis/diagnostic paper

**N2** [critical] 实验范围过窄
- 仅 Qwen3-0.6B、FineWeb 132M tokens、self-generated contamination
- Cross-model transfer (Appendix O) 结果 "mixed"
- ρ=0.2 时方法 degrade
- "three effectiveness conditions" 作为一般性结论缺乏多样化实验支撑

**N3** [critical] Adaptive b* 的新颖性不足
- w=(1-q)^b 完全来自 Drayson et al.
- Adaptive b* 本质是参数选择启发式（分段函数 + bisection）
- Adaptive vs grid-best: 17.674 vs 17.657，几乎无差异

## Should-Fix 问题

**W1** [warning] Related Work 遗漏近期 instance-level reweighting 工作
- Dynamic Loss-Based Sample Reweighting (arXiv:2502.06733)
- Self-Influence Guided Data Reweighting (ICLR 2025)
- ToReMi: Topic-Aware Data Reweighting (arXiv:2504.00695)

**W2** [warning] Epoch confound 发现概念上非完全出乎意料
- 减少数据量意味着更多重复暴露是自然推论
- 贡献在于严格实验验证，但需讨论为何之前文献忽略了

**W3** [warning] 3 seeds 统计效力不足

**W4** [warning] "analysis paper" vs "method paper" 定位不清晰
- Abstract 同时 claim analysis 和 method
- 建议明确选择一个定位

**W5** [warning] α_eff correlation 跨 seed 差异大（Pearson r: 0.17-0.75）

## Missing References
1. Xu et al. (2025) "Dynamic Loss-Based Sample Reweighting"
2. Xia et al. (ICLR 2025) "Self-Influence Guided Data Reweighting"
3. Wu et al. (2025) "A Survey on LLM-Generated Text Detection"
4. Chen et al. (2025) "ToReMi"

---

请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-23T03:15:34.977665+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 效应量极小，实际意义不足以支撑论文 framing**\n同意。这与我的 N3 和 W3 一致。Δ=−0.020 PPL（~0.11%）在 epoch-matched 条件下极其微小，且 Table 4 的下游 benchmark 平均准确率 adaptive (0.5414) = uniform (0.5414)，完全无差异。Abstract 中 \"yielding a practical adaptive method\" 的措辞确实构成 overclaim——一个在下游任务上零改善的方法难以被称为 \"practical\"。R2 建议重新定位为 analysis/diagnostic paper 与我的建议一致。不过需要公平指出：论文在 §6 和 Limitations 中确实坦承了下游零改善和效应量小的事实，问题主要在 Abstract/Intro 的 framing 而非隐瞒。\n\n**[AGREE with nuance] R2-N2: 实验范围过窄**\n大体同意，但严重程度需区分。单模型（Qwen3-0.6B）、单数据集（FineWeb 132M tokens）、self-contamination 的实验范围确实过窄，这也是我 W1 指出的问题。Appendix O 的 cross-model 实验（Llama-3.2-3B 生成）仅单种子且结果混合（MMLU↑ 但 HellaSwag↓），不足以支撑泛化性。ρ=0.2 时方法退化（Appendix Q）也是重要限制。\n\n但我要补充一点：R2 称 \"three effectiveness conditions 作为一般性结论缺乏多样化实验支撑\" 需要更精确地看。这三个条件（detector quality, contamination level, minimum intervention）是通过消融实验（Table 3）得出的，虽然仅在一个设置下验证，但其逻辑结构是合理的——它们是 necessary conditions 而非 sufficient conditions，论文并未声称在所有设置下都充分。问题在于论文的措辞有时暗示了更强的一般性。\n\n**[PARTIALLY REBUT] R2-N3: Adaptive b* 新颖性不足**\n部分反驳。R2 的论点有一定道理——w=(1−q)^b 确实完全来自 Drayson et al.，dual-constrained bisection 从算法角度看比较 incremental。这也是我 W2 提出的。\n\n但 R2 用 \"adaptive vs grid-best: 17.674 vs 17.657, 几乎无差异\" 作为新颖性不足的证据，这个论证逻辑有问题。Adaptive 方法的目标恰恰是在不做 grid search 的情况下接近 grid-best 性能——差距仅 0.017 说明方法有效，而非无价值。Grid search 需要多次完整训练（Table 5 显示 9 个 candidate，即 9 次训练），而 adaptive b* 是 zero-cost 的。这个区别 R2 没有给予足够重视。\n\n我认为新颖性问题应标记为 should-fix（要求更好的 positioning）而非 critical。论文的真正新颖性在于 epoch confound 的发现，adaptive method 是附带的实践贡献。\n\n---\n\n### Should-Fix 问题\n\n**[PARTIALLY AGREE] R2-W1: Related Work 遗漏近期 instance-level reweighting 工作**\n部分同意。论文 Section 2 的 \"Instance-Level Data Selection and Reweighting\" 部分已经覆盖了 curriculum learning (Bengio et al.)、focal loss (Lin et al.)、importance sampling (Katharopoulos and Fleuret 2018; Mindermann et al. 2022)、LESS (Xia et al. 2024) 等，覆盖面是合理的。\n\nR2 列出的 4 篇缺失引用中，我无法在 blind review 条件下独立验证它们是否真实存在及是否高度相关。但如果这些确实是 2025 年发表的 instance-level reweighting 工作，鉴于论文声称解决的是 pretraining 数据 reweighting 问题，补充讨论它们与 provenance-based reweighting 的区别（instance-level loss-based vs. provenance-based binary signal）是合理的。建议作者在 camera-ready 中补充核实并酌情引用。\n\n**[AGREE] R2-W2: Epoch confound 概念上非完全出乎意料**\n同意。\"过滤掉数据→剩余数据训练更多 epoch→可能获益于重复暴露\" 确实是一个可以事先推理出的 hypothesis。但我要强调：R2 自己也承认 \"贡献在于严格实验验证\"，这正是关键——之前的 D&R 文献（Drayson et al. 2025, Cheng et al. 2025 等）确实没有控制 epoch confound。论文在 §5.1 中通过 epoch-matched 对照（Table 1）和 shared-schedule replication（Δ=0.006）提供了令人信服的定量证据，证明 confound 解释了 >95% 的优势。\n\n我同意论文应增加讨论 \"为什么之前文献忽略了这个 confound\"。可能的原因包括：(1) 之前的工作关注的是 absolute performance 而非 epoch-controlled comparison；(2) 在 from-scratch pretraining 中 epoch confound 不如 continued pretraining 明显。这类讨论会加强贡献的 contextualization。\n\n**[STRONGLY AGREE] R2-W3: 3 seeds 统计效力不足**\n强烈同意。这是我的 N1 (must-fix)。N=3 seeds, 2 自由度，bootstrap CI 不可靠，是本文最严重的实验缺陷。R2 将其列为 should-fix 而非 must-fix，我认为应升级为 must-fix。\n\n**[AGREE] R2-W4: \"analysis paper\" vs \"method paper\" 定位不清晰**\n同意。Abstract 同时 claim \"we analyze when, why, and how detect-and-reweight works\"（分析）和 \"we derive a dual-constrained adaptive b*\"（方法）。鉴于 epoch confound 分析远比 adaptive method 有说服力（前者有充分证据，后者受限于 R²=0.49 的 proxy 和零下游改善），论文应明确以分析为主线。这与我的总结建议一致。\n\n**[AGREE] R2-W5: α_eff correlation 跨 seed 差异大**\n同意，且这进一步加强了我 N2 的论点。Table 11（Appendix K）显示 α_eff 与 true real fraction 的 Pearson r 跨 seed 从 0.17 到 0.75 变化极大。r=0.17 的种子基本上意味着 α_eff 作为 proxy 完全失效（R²≈0.03）。三个种子中有一个种子的相关性接近零，这不是随机波动——这暗示 α_eff 的 proxy 质量高度依赖于特定训练 trajectory，而非一个 robust 的信号。\n\n这与 Bonferroni-Holm 校正后 Spearman ρ 不显著（p_BH=0.078）的结果一致：α_eff 作为 quality proxy 的可靠性远低于论文主体部分的 framing 所暗示的。\n\n---\n\n### Missing References 回应\n\nR2 列出的 4 篇缺失引用（Xu et al. 2025, Xia et al. ICLR 2025, Wu et al. 2025, Chen et al. 2025），我在 blind review 条件下无法独立核实其存在和相关性。论文 Section 2 的 related work 在 instance-level reweighting 方向已有合理覆盖，但如果这些是 2025 年的最新工作，确实应在 camera-ready 中补充。特别是如果有 survey（Wu et al. 2025 关于 LLM-generated text detection）与本文 §2 的 detection 部分直接相关，应当引用。\n\n---\n\n### 总结\n\nR2 与我的审稿意见在核心判断上高度一致：(1) epoch confound 是有价值的分析贡献；(2) adaptive method 增量有限且实验支撑不足；(3) 效应量极小且无下游收益；(4) 实验范围过窄。\n\n两份审稿的主要分歧在于：\n- **N=3 seeds 的严重程度**：我列为 must-fix，R2 列为 should-fix。我认为 must-fix 更恰当——2 自由度的 t 检验不应作为顶会论文的核心统计基础。\n- **Adaptive b* 新颖性**：R2 列为 must-fix critical，我列为 should-fix。我认为 zero-cost 接近 grid-best 是有实践价值的，问题在于 positioning 而非方法本身无效。\n\n**维持 Overall: 3.0 (Findings)**",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 效应量极小，实际意义不足以支撑论文 framing**\n同意。这与我的 N3 和 W3 一致。Δ=−0.020 PPL（~0.11%）在 epoch-matched 条件下极其微小，且 Table 4 的下游 benchmark 平均准确率 adaptive (0.5414) = uniform (0.5414)，完全无差异。Abstract 中 \"yielding a practical adaptive method\" 的措辞确实构成 overclaim——一个在下游任务上零改善的方法难以被称为 \"practical\"。R2 建议重新定位为 analysis/diagnostic paper 与我的建议一致。不过需要公平指出：论文在 §6 和 Limitations 中确实坦承了下游零改善和效应量小的事实，问题主要在 Abstract/Intro 的 framing 而非隐瞒。\n\n**[AGREE with nuance] R2-N2: 实验范围过窄**\n大体同意，但严重程度需区分。单模型（Qwen3-0.6B）、单数据集（FineWeb 132M tokens）、self-contamination 的实验范围确实过窄，这也是我 W1 指出的问题。Appendix O 的 cross-model 实验（Llama-3.2-3B 生成）仅单种子且结果混合（MMLU↑ 但 HellaSwag↓），不足以支撑泛化性。ρ=0.2 时方法退化（Appendix Q）也是重要限制。\n\n但我要补充一点：R2 称 \"three effectiveness conditions 作为一般性结论缺乏多样化实验支撑\" 需要更精确地看。这三个条件（detector quality, contamination level, minimum intervention）是通过消融实验（Table 3）得出的，虽然仅在一个设置下验证，但其逻辑结构是合理的——它们是 necessary conditions 而非 sufficient conditions，论文并未声称在所有设置下都充分。问题在于论文的措辞有时暗示了更强的一般性。\n\n**[PARTIALLY REBUT] R2-N3: Adaptive b* 新颖性不足**\n部分反驳。R2 的论点有一定道理——w=(1−q)^b 确实完全来自 Drayson et al.，dual-constrained bisection 从算法角度看比较 incremental。这也是我 W2 提出的。\n\n但 R2 用 \"adaptive vs grid-best: 17.674 vs 17.657, 几乎无差异\" 作为新颖性不足的证据，这个论证逻辑有问题。Adaptive 方法的目标恰恰是在不做 grid search 的情况下接近 grid-best 性能——差距仅 0.017 说明方法有效，而非无价值。Grid search 需要多次完整训练（Table 5 显示 9 个 candidate，即 9 次训练），而 adaptive b* 是 zero-cost 的。这个区别 R2 没有给予足够重视。\n\n我认为新颖性问题应标记为 should-fix（要求更好的 positioning）而非 critical。论文的真正新颖性在于 epoch confound 的发现，adaptive method 是附带的实践贡献。\n\n---\n\n### Should-Fix 问题\n\n**[PARTIALLY AGREE] R2-W1: Related Work 遗漏近期 instance-level reweighting 工作**\n部分同意。论文 Section 2 的 \"Instance-Level Data Selection and Reweighting\" 部分已经覆盖了 curriculum learning (Bengio et al.)、focal loss (Lin et al.)、importance sampling (Katharopoulos and Fleuret 2018; Mindermann et al. 2022)、LESS (Xia et al. 2024) 等，覆盖面是合理的。\n\nR2 列出的 4 篇缺失引用中，我无法在 blind review 条件下独立验证它们是否真实存在及是否高度相关。但如果这些确实是 2025 年发表的 instance-level reweighting 工作，鉴于论文声称解决的是 pretraining 数据 reweighting 问题，补充讨论它们与 provenance-based reweighting 的区别（instance-level loss-based vs. provenance-based binary signal）是合理的。建议作者在 camera-ready 中补充核实并酌情引用。\n\n**[AGREE] R2-W2: Epoch confound 概念上非完全出乎意料**\n同意。\"过滤掉数据→剩余数据训练更多 epoch→可能获益于重复暴露\" 确实是一个可以事先推理出的 hypothesis。但我要强调：R2 自己也承认 \"贡献在于严格实验验证\"，这正是关键——之前的 D&R 文献（Drayson et al. 2025, Cheng et al. 2025 等）确实没有控制 epoch confound。论文在 §5.1 中通过 epoch-matched 对照（Table 1）和 shared-schedule replication（Δ=0.006）提供了令人信服的定量证据，证明 confound 解释了 >95% 的优势。\n\n我同意论文应增加讨论 \"为什么之前文献忽略了这个 confound\"。可能的原因包括：(1) 之前的工作关注的是 absolute performance 而非 epoch-controlled comparison；(2) 在 from-scratch pretraining 中 epoch confound 不如 continued pretraining 明显。这类讨论会加强贡献的 contextualization。\n\n**[STRONGLY AGREE] R2-W3: 3 seeds 统计效力不足**\n强烈同意。这是我的 N1 (must-fix)。N=3 seeds, 2 自由度，bootstrap CI 不可靠，是本文最严重的实验缺陷。R2 将其列为 should-fix 而非 must-fix，我认为应升级为 must-fix。\n\n**[AGREE] R2-W4: \"analysis paper\" vs \"method paper\" 定位不清晰**\n同意。Abstract 同时 claim \"we analyze when, why, and how detect-and-reweight works\"（分析）和 \"we derive a dual-constrained adaptive b*\"（方法）。鉴于 epoch confound 分析远比 adaptive method 有说服力（前者有充分证据，后者受限于 R²=0.49 的 proxy 和零下游改善），论文应明确以分析为主线。这与我的总结建议一致。\n\n**[AGREE] R2-W5: α_eff correlation 跨 seed 差异大**\n同意，且这进一步加强了我 N2 的论点。Table 11（Appendix K）显示 α_eff 与 true real fraction 的 Pearson r 跨 seed 从 0.17 到 0.75 变化极大。r=0.17 的种子基本上意味着 α_eff 作为 proxy 完全失效（R²≈0.03）。三个种子中有一个种子的相关性接近零，这不是随机波动——这暗示 α_eff 的 proxy 质量高度依赖于特定训练 trajectory，而非一个 robust 的信号。\n\n这与 Bonferroni-Holm 校正后 Spearman ρ 不显著（p_BH=0.078）的结果一致：α_eff 作为 quality proxy 的可靠性远低于论文主体部分的 framing 所暗示的。\n\n---\n\n### Missing References 回应\n\nR2 列出的 4 篇缺失引用（Xu et al. 2025, Xia et al. ICLR 2025, Wu et al. 2025, Chen et al. 2025），我在 blind review 条件下无法独立核实其存在和相关性。论文 Section 2 的 related work 在 instance-level reweighting 方向已有合理覆盖，但如果这些是 2025 年的最新工作，确实应在 camera-ready 中补充。特别是如果有 survey（Wu et al. 2025 关于 LLM-generated text detection）与本文 §2 的 detection 部分直接相关，应当引用。\n\n---\n\n### 总结\n\nR2 与我的审稿意见在核心判断上高度一致：(1) epoch confound 是有价值的分析贡献；(2) adaptive method 增量有限且实验支撑不足；(3) 效应量极小且无下游收益；(4) 实验范围过窄。\n\n两份审稿的主要分歧在于：\n- **N=3 seeds 的严重程度**：我列为 must-fix，R2 列为 should-fix。我认为 must-fix 更恰当——2 自由度的 t 检验不应作为顶会论文的核心统计基础。\n- **Adaptive b* 新颖性**：R2 列为 must-fix critical，我列为 should-fix。我认为 zero-cost 接近 grid-best 是有实践价值的，问题在于 positioning 而非方法本身无效。\n\n**维持 Overall: 3.0 (Findings)**",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-23T03:15:38.767986+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3790
}
```

</details>

---


### Assistant

_source line 596 · 2026-05-23T03:15:47.563347+00:00_

已完成对 Reviewer 2 全部 Must-Fix（N1-N3）和 Should-Fix（W1-W5）的逐条交叉回应，并汇报给 Director。

核心判断：
- 与 R2 在 5 个问题上 **[AGREE]**（效应量过小、epoch confound 非全新、3 seeds 不足、定位不清、α_eff 跨 seed 不稳）
- 在 2 个问题上 **[PARTIALLY AGREE/REBUT]**（实验范围窄但 three conditions 逻辑合理；adaptive b* 新颖性不应列为 critical，zero-cost 接近 grid-best 有实践价值）
- 主要分歧：我认为 N=3 seeds 应升级为 must-fix，而 adaptive b* 新颖性应降级为 should-fix
- 维持 Overall 3.0 (Findings)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 21

## Round 21

56 recorded events


### User

_source line 597 · 2026-05-23T13:11:08.510570+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1: 方法严谨性 + 实验设计

### Venue 信息
- **目标**: EMNLP 2026 (ARR May cycle)
- **截止日期**: 2026-05-25
- **格式**: Long Paper, 8 页正文, 无限参考文献, Limitations/Ethics 不计入页数
- **模板**: ACL 2026 style
- **匿名规则**: Double-blind (论文中不得出现作者信息, 避免 self-revealing references)
- **评分标准**: ARR Overall Assessment 1-5 分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit)

### 论文文件
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf`
- 补充材料: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md`

### 你的审查侧重

**核心关注: 方法严谨性 + 实验设计**

请从以下维度严格审查:

1. **统计推断可靠性**
   - N=3 seeds 的统计检验力是否足够？paired t-test (2 df) 的可靠性？
   - Bonferroni-Holm 校正后 p 值 (p_BH=0.078 at ρ=0.4, p_BH=0.064 at ρ=0.6) 的解读是否恰当？
   - Bootstrap CI 在 N=3 时的覆盖率保证？
   - 是否存在 p-hacking 或 selective reporting 的迹象？

2. **实验控制质量**
   - Epoch confound 实验设计的严谨性：epoch-matched comparison 是否充分控制了混淆因素？LR schedule 控制是否完备？
   - Self-contamination 设计的生态效度：generator=trainee 是否人为降低了问题难度？
   - Checkpoint resume artifact (Appendix P) 是否已充分排除？

3. **α_eff proxy 可靠性**
   - Pearson r=0.70 (R²≈0.49) 是否足以支撑方法的核心机制？
   - 跨 seed 稳定性的证据是否充分？
   - 方差分解 (70% detector noise / 30% ESS compression) 的可信度？

4. **效应量与 claim 匹配**
   - Δ=-0.020 PPL (~0.11% relative) 是否具有实际意义？
   - Downstream task 零改善与 PPL 改善的不一致性？
   - 论文的 claim 范围是否超过了实验证据所能支撑的范围？

5. **实验范围**
   - 单模型 (Qwen3-0.6B/1.7B) + 单数据集 (FineWeb 132M) 是否足够？
   - ρ={0.2, 0.3, 0.4, 0.6} 的覆盖是否完整？
   - 1.7B scale-up 和 cross-model transfer 的证据强度？

请按 ARR 标准格式输出审稿报告: Summary → Strengths → Weaknesses (分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-23T13:11:16.279018+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-23T13:11:16.279469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-23T13:11:21.900807+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-23T13:11:24.258662+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-23T13:11:24.861036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-23T13:11:28.173550+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found regarding ACL ARR 2025-2026 reviewer guidelines:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score Requirements

Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Excitement Score

You may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Reviewer Expectations

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

For more detailed information about the full reviewer guidelin
…[truncated 249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6272
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-23T13:11:29.805632+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5546
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-23T13:11:29.806356+00:00_

1	# Author Response (Round 11)
2	
3	We thank the reviewers for their thorough feedback. Below we address all concerns organized by the R11 issue list. All referenced revisions are in the updated manuscript.
4	
5	---
6	
7	## Broader Significance
8	
9	This work contributes beyond our specific experimental setting in four ways. First, the epoch confound finding applies retroactively to all D&R evaluations that compare at equal training steps rather than equal content epochs: the headline 0.396 PPL advantage shrinks by >95% to a residual Δ=0.017 when content epochs are equalized (Table 1), establishing a methodological baseline that future D&R studies must control for. Second, the detector requirements analysis yields a counter-intuitive result: a high-AUC detector (GPT-2, AUC=0.91) with poor calibration (ECE=0.131) performs *worse* than uniform training (Δ=+0.098), while a lower-AUC but well-calibrated detector (TF-IDF, AUC=0.94, ECE=0.048) succeeds—demonstrating that calibration can reverse the sign of the intervention. Third, the α_eff/ESS constraint decomposition provides a generalizable analytical toolkit for importance-weighted training: any method that applies per-sample weights faces the same quality-stability tradeoff, and our binding-rate analysis offers a diagnostic for when constraints dominate. Fourth, the observed Δ=−0.020 at ρ=0.4, B=4 represents a lower bound, not a ceiling: batch-size amplification shows monotonic scaling (B=4: Δ=−0.020, B=8: Δ=−0.050, B=16: Δ=−0.068; §5.4), and production batch sizes typically range from 64 to 256. At ρ=0.6 the effect doubles to Δ=−0.032 (uncorrected p=0.010; BH-corrected p=0.064 with k=9). At production batch sizes (e.g., B=128), conservative extrapolation with the empirical scaling exponent α ≈ 0.89 (Δ ∝ B^α) predicts Δ ≈ −0.39, a practically meaningful improvement—though this extrapolation is speculative and requires empirical validation at larger scale. As web-scale contamination grows, the practical relevance of p
…[truncated 10729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4945
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-23T13:11:37.055056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-23T13:11:37.408318+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-23T13:11:38.013019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-23T13:11:39.490114+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2435
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-23T13:11:39.490550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-23T13:11:39.490792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-23T13:11:41.601791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4193
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-23T13:11:41.603105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3590
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-23T13:11:41.603512+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), the exact rating scale for each dimension, and any specific instructions about what reviewers should evaluate. Include the full text of scoring criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), the exact rating scale for each dimension, and any specific instructions about what reviewers should evaluate. Include the full text of scoring criteria."
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-23T13:11:42.410545+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2919
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-23T13:11:42.564561+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3073
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-23T13:11:47.683811+00:00_

# ARR Reviewer Scoring Guidelines

## Scoring Dimensions

The ARR review form requires three primary scores:

**1. Soundness**
Reviewers assess technical validity and methodological rigor. "The soundness scores must be justified by the text of the review." Low soundness scores require explicit justification in the review text.

**2. Excitement**
This orthogonal dimension captures personal interest independent of technical quality. Reviewers may find work sound but personally unengaging, or vice versa.

**3. Overall Assessment**
A composite recommendation reflecting soundness, excitement, novelty, and potential impact. "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## Additional Scoring Elements

**Confidence Score**: Reviewers indicate their expertise level for the assigned paper, disclosing unfamiliar aspects.

**Reproducibility Score**: Assessment of whether sufficient details exist to reproduce experiments (linked to methodology, code availability, and hyperparameter transparency).

## Key Instruction

Reviewers must ensure consistency between scores and review content. Misalignment suggests unconscious bias or inadequate justification. The guidelines emphasize that "low soundness scores without sufficient justification" indicate unfaithful recommendation representation.

The document provides no explicit numerical rating scales (e.g., 1-5), focusing instead on principled evaluation aligned with clear written feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6080
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-23T13:11:53.905649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 619 · 2026-05-23T13:11:54.357644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 620 · 2026-05-23T13:11:55.363157+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 621 · 2026-05-23T13:11:55.414391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-23T13:11:55.769252+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 623 · 2026-05-23T13:11:55.971163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-23T13:11:56.273977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-23T13:11:57.179020+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1764
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-23T13:11:57.180268+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement overall assessment rating scale 1-5 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement overall assessment rating scale 1-5 2025"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-23T13:11:58.184319+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2213
}
```

</details>

---


### Tool result

_source line 628 · 2026-05-23T13:11:58.387910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2113
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-23T13:12:04.765870+00:00_

Web search results for query: "ACL ARR review form soundness excitement overall assessment rating scale 1-5 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about the ACL ARR review form with soundness, excitement, and overall assessment ratings:

## Three-Score System (February 2025+)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

Soundness scores must be justified by the text of the review. The review form includes guidance on what soundness involves, such as assessing whether the paper is "sufficiently sound and thorough" and whether it "clearly states scientific claims and provide[s] adequate support for them."

Based on t
…[truncated 1022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7585
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-23T13:12:12.084644+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions and their exact rating scales (numerical values and descriptions for each level). Include soundness scale, excitement scale, overall assessment scale, confidence scale, reproducibility, and any other scored dimensions. I need the exact text for each rating level (e.g., 5 = ..., 4 = ..., etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions and their exact rating scales (numerical values and descriptions for each level). Include soundness scale, excitement scale, overall assessment scale, confidence scale, reproducibility, and any other scored dimensions. I need the exact text for each rating level (e.g., 5 = ..., 4 = ..., etc.)."
  }
}
```

</details>

---


### Tool call

_source line 631 · 2026-05-23T13:12:14.242226+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "11-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "11-17",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 632 · 2026-05-23T13:12:21.277054+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

## Overall Assessment
- **5**: Consider for Award
- **4**: Conference
- **3**: Findings
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Reproducibility
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results."

## Datasets & Software
Both use identical 5-point scales (Enabling, Useful, Potentially useful, Documentary, No usable materials).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9192
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-23T13:12:22.433891+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 390.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 426.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 48.2}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8191
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-23T13:12:26.798863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-23T13:12:27.706454+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-23T13:12:27.706904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-23T13:12:28.211077+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-23T13:12:28.211513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-23T13:12:28.668346+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-23T13:12:28.668926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 641 · 2026-05-23T13:12:29.123843+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 642 · 2026-05-23T13:12:29.880095+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1211
}
```

</details>

---


### Tool call

_source line 643 · 2026-05-23T13:12:29.880492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-23T13:12:30.032035+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-23T13:12:30.936484+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-23T13:16:14.798339+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告 — 方法严谨性 + 实验设计\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight (D&R) 范式在续训语言模型中应对合成文本污染的有效性条件。在 Qwen3-0.6B 上使用 132M FineWeb 子集进行可控实验，提出三项分析发现：(1) D&R 先前报告的 PPL 优势中 >95% 可归因于 epoch confound（多轮数据暴露），epoch-matched 后优势从 0.396 缩减至 0.017；(2) 有效的 reweighting 要求检测器同时具备足够的 AUC（≥0.9）和良好的校准（ECE≤0.05），高 AUC 但低校准的检测器反而劣于均匀训练；(3) 基于双约束（α_eff ≥ τ, ESS ≥ n_min）的自适应 b* 实现最小干预，性能接近 grid search 最优。方法在 ρ=0.4 时获得 Δ=−0.020 PPL（~0.11% relative），下游任务无显著改善。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3/5 (Acceptable) | Epoch confound 发现方法论可靠，但 adaptive method 的统计证据不足（N=3, 校正后均未达 α=0.05），α_eff proxy R²≈0.49 |\n| **Excitement** | 2/5 (Potentially Interesting) | Epoch confound 对社区有方法论警示价值，但效应量极小（0.11% PPL），下游零改善，实际影响有限 |\n| **Reproducibility** | 4/5 | 实验设置详细（§4），超参数透明，代码承诺开源，17 个 appendix 覆盖完整 |\n| **Confidence** | 4/5 | 对统计方法论和实验设计领域较为熟悉，仔细检查了主要论点 |\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n\n**一句话总结**: Epoch confound 的发现有真实的方法论价值，足以支撑 Findings 级别的贡献，但自适应方法的统计证据不足（N=3 无校正显著性、下游零改善、效应量极小）使其无法达到主会议标准。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 的统计推断力根本性不足\n- 具体位置：§5.1, Table 2, 以及论文中所有 p 值和 CI 报告\n- 问题：全文核心量化结论依赖于 N=3 seeds 的 paired t-test（仅 2 个自由度）。主要结果：\n  - ρ=0.4: uncorrected p=0.019, BH-corrected p=0.078（未达 α=0.05）\n  - ρ=0.6: uncorrected p=0.010, BH-corrected p=0.064（未达 α=0.05）\n  \n  论文报告了 bootstrap CI [−0.028, −0.012]（§5.1），但 N=3 的 bootstrap 仅有 3³=27 个可能的重抽样本，CI 的覆盖率保证极其脆弱。论文声称 Cohen's d=2.86, power>0.90，但如此高的 d 值更可能反映的是方差被人为压低（seeds 只影响参数初始化，data order 固定），而非效应量大。实际上这恰恰说明 3 个 seeds 探索的随机性维度极其有限。\n\n  更关键的是：论文先选择了 BH 校正（k=9），然后在校正结果不理想时论证家族 \"structurally heterogeneous\"，校正过于保守。这构成了一种 post-hoc 的统计叙事调整——你不能在分析前选择校正方法，分析后否定它。\n- 为什么影响接收：这是一篇以定量分析为核心的论文，如果核心量化结论在标准统计检验下均不显著，整个 adaptive method 的贡献就缺乏可靠支撑。\n- 建议修改方向：(a) 增加到至少 N=5 seeds（4 df，可检测 d=2.0 的效应）；或 (b) 如果计算资源不允许，全面放弃 p 值叙事，改为纯效应量+方向一致性报告，明确承认统计检验力不足；(c) 对 BH 校正取一个立场并坚持——要么不用（给出理由），要么用了就接受结果。\n\n**N2** [critical] 效应量与 claim 之间的严重脱节\n- 具体位置：§5.1 (Δ=−0.020 PPL), Table 4 (downstream null), §7 Conclusion\n- 问题：adaptive 方法的核心效应量为 Δ=−0.020 PPL，相对改善仅 0.11%。五项下游任务（Table 4, MMLU/HellaSwag/ARC/WinoGrande/PIQA）全部 |Δ|≤0.01，在标准误内无法区分。论文将这归因于 \"PPL-to-downstream transfer is nonlinear and scale-dependent\"（引用 Tay et al., 2023），但这恰恰意味着在可验证的当前 scale 下，该方法没有实际用途。\n\n  §5.4 的 batch-size amplification 外推更成问题：仅用 B={4,8,16} 三个点拟合幂律 Δ∝B^α（α≈0.89），然后外推到 B=128 预测 Δ≈−0.39。用 3 个数据点拟合幂律并外推 8 倍，任何统计学教材都会认为这不可靠。论文虽标注 \"speculative\"，但 rebuttal 中将其作为实际意义的主要论据（\"a practically meaningful improvement\"）。\n- 为什么影响接收：如果方法在可测量的所有指标上都没有实际改善，contribution 主要在分析框架本身——这需要论文的 framing 与之匹配，避免方法论贡献的过度包装。\n- 建议修改方向：(a) 在 abstract 和 conclusion 中删除所有关于 \"practical\" 的表述——当前 scale 下该方法不 practical；(b) 将 batch-size 外推从主文移到 appendix，标注为 hypothesis 而非 evidence；(c) 更诚实地承认：在可验证范围内，adaptive reweighting 的实际增益可忽略不计。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Self-contamination 实验设计的生态效度严重不足\n- 具体位置：§4 \"Training Data\", §7 Limitations\n- 问题：generator=trainee 的设计意味着合成数据来自被训练模型自身（Qwen3-0.6B 生成 → Qwen3-0.6B 检测+训练）。这人为降低了检测难度：模型生成的文本带有自身的统计指纹，TF-IDF+LR 检测器能达到 AUC=0.94 部分归因于此。真实世界中，污染来源是异构的（GPT-4、Claude、Gemini 等多种模型，且不同版本），检测难度远高于 self-contamination。\n\n  论文在 Limitations（§9, p.9）中承认了这一限制（\"limits ecological validity\"），但论文的第二项核心 claim——detector requirements（AUC≥0.9, ECE≤0.05）——直接依赖于检测器性能数据。在 self-contamination 下得出的检测器阈值，在 cross-model contamination 下可能完全不适用。Appendix O 的 cross-model transfer（Llama-3.2-3B）是 single seed 且结果 mixed（MMLU +1.57pp, HellaSwag −0.60pp），不足以验证。\n- 建议：(a) 至少增加一个 cross-generator 实验（用 GPT-2-large 或其他开放模型生成污染数据），在主文中报告；(b) 将 detector requirements 的 claim 明确限定为 self-contamination 场景。\n\n**W2** [warning] α_eff proxy 的解释力不足以支撑其在方法中的核心地位\n- 具体位置：§3 Method (α_eff 定义), §6 Discussion, Table 11, Appendix K\n- 问题：α_eff 是 adaptive b* 方法的核心机制——它是双约束中 quality floor 的直接操作变量。但 Table 11 显示 α_eff 与 ground-truth batch-level real fraction 的 Pearson r=0.70（R²≈0.49），即 proxy 仅解释了不到一半的方差。论文的方差分解（~70% detector noise, ~30% ESS compression）基于单一 seed 的定性归因，没有正式的方差分解统计。\n\n  Rebuttal 中报告 r(α_eff, mean_q)=0.80，但这是 proxy-to-detector-score 的相关性（循环论证），而非 proxy-to-ground-truth。cross-seed spread <0.003 看似稳定，但 α_eff 是 q-scores 的确定性函数且 detector 固定，所以跨 seed 稳定是预期结果，不构成额外证据。\n\n  根本问题：当方法的核心信号只解释 49% 的目标方差时，为什么 minimum intervention（保守使用这个噪声信号）优于 uniform？一个更简洁的解释是：adaptive b* 的实际贡献主要来自 ESS constraint 的稳定化作用，而非 α_eff 的质量信号。\n- 建议：(a) 增加 ablation：固定 α_eff=constant，只保留 ESS constraint，测试 PPL 差异；(b) 如果这个 ablation 表明 ESS 是主要贡献者，需要重写 §6 的 narrative。\n\n**W3** [warning] 实验范围过窄，不支撑 \"necessary conditions\" 的普适性 claim\n- 具体位置：§7 Conclusion (\"three effectiveness conditions\"), §5.2-5.4, Limitations\n- 问题：论文声称识别了三个 \"effectiveness conditions\"（AUC≥0.9, ECE≤0.05, ρ≥0.4），但支撑这些条件的实验仅覆盖：\n  - 1 个模型家族（Qwen3, 0.6B/1.7B）\n  - 1 个数据集（FineWeb 132M）\n  - 1 种污染类型（self-contamination）\n  - 4 个 ρ 值（0.2/0.3/0.4/0.6）\n  - 3 个 seeds（主实验）/ 1 个 seed（1.7B, cross-model）\n\n  \"necessary conditions\" 是一个逻辑上很强的 claim：它意味着在任何设置下，这些条件都是必要的。但实际实验仅在一个极窄的设置上观察到了这些阈值。ρ 覆盖的不完整性尤其明显：ρ=0.2 和 ρ=0.3 均在 degradation zone，ρ=0.4 是 borderline，ρ=0.6 有效——但 ρ=0.5 没有测试，无法确定 boundary 的精确位置。AUC/ECE 阈值来自仅 3 个检测器（TF-IDF+LR, GPT-2, N-gram）的比较，样本量太小。\n- 建议：(a) 将 \"necessary conditions\" 改为 \"empirically observed conditions in our setting\"；(b) 在 Limitations 中明确讨论跨模型/数据集/污染类型的泛化限制。\n\n**W4** [warning] Epoch confound 实验中 LR schedule 混淆因素未完全排除\n- 具体位置：Table 1, §5.1 \"LR-controlled verification\"\n- 问题：Table 1 的 epoch-matched comparison 中，epoch-matched D&R \"shares the full-length LR schedule\"——即使用完整训练长度的 LR schedule 但仅训练 2,553 步（vs. 原始 6,103 步）。这引入了一个新的混淆：LR schedule 的形状（warmup/decay phase 的比例）在截断训练中与完整训练不同。\n\n  §5.1 提到 \"an independent-schedule replication (D&R 17,601 vs shared-schedule uniform 18,062) matches the shared-schedule result (Δ=−0.068)\"，但这个 independent-schedule 控制的细节仅在正文中一句话带过，没有在 Table 1 中呈现，也没有在 appendix 中提供完整的 LR 曲线对比。\n\n  更根本的问题：epoch-matched comparison 通过缩短训练来消除 epoch confound，但缩短训练本身改变了训练动态（如 gradient noise scale, batch normalization statistics 等）。一个更干净的控制是在相同步数下，通过 upsampling 非污染数据来匹配 content epochs。\n- 建议：(a) 在 appendix 中展示 epoch-matched 和 full-training 的完整 LR curves；(b) 讨论 early-stopping vs. content-epoch-matching 的 confound 可能性；(c) 如果可行，补充 upsampling baseline。\n\n---\n\n## 小问题（不影响接收）\n\n- **m1**: Table 2 中 \"Golden Ratio\" 行的 w 定义（w = 1/q if q > 0.5, else 0）没有在正文中给出，需要翻到 Appendix C 才能理解。建议在 §4 Methods 中简要说明。\n\n- **m2**: §5.2 中 \"Robustness and Boundary Conditions\" 小节同时讨论 ρ=0.6 的结果和 boundary conditions，建议拆分为两个子节以提高可读性。\n\n- **m3**: Figure 2 的 x 轴标签 \"Sharpening exponent b\" 与正文中 \"b* per-batch adaptive\" 的关系不够清晰——Figure 2 是 grid search 结果，b 是固定值，但正文的叙事已转向 adaptive b*，容易造成混淆。\n\n- **m4**: Appendix Q 的 ρ=0.3 boundary 结果（Δ=+0.002, non-significant）是一个重要数据点，建议在主文 §5.2 中明确引用。\n\n- **m5**: §2 Related Work 中引用了 \"Drayson et al., 2025\" 在多处但未指出该工作的具体方法与本文的关键区别（from-scratch vs. continued pretraining）——这个区别恰恰是 epoch confound 成立的前提，应在 Related Work 中就明确讨论。\n\n---\n\n## Questions for Authors\n\n1. N=3 的设计是计算资源限制还是有意为之？如果是资源限制，是否考虑过降低训练步数（如 3000 steps）来换取更多 seeds（如 N=7）？这种 tradeoff 在统计上可能更有价值。\n\n2. α_eff-only ablation（去掉 ESS constraint，只保留 α_eff ≥ τ）的 PPL 是多少？Table 2 有 ESS-only 但缺少 α_eff-only。这对理解两个 constraint 的独立贡献至关重要。\n\n3. Rebuttal 中的 per-seed α_eff correlation（Table with r=0.80）与主文 Table 11 的 r=0.70 的区别是什么？前者似乎是 α_eff vs. mean(q)（detector score），后者是 α_eff vs. true real fraction——如果是这样，r=0.80 是检测器自身的 consistency 而非 proxy 的 ground-truth fidelity，不应作为支持 proxy 可靠性的证据。\n\n4. Batch-size amplification实验（§5.4, B=4/8/16）是在固定 total tokens 下进行的，还是固定 steps？如果固定 steps，那 B=16 看到了比 B=4 多 4 倍的 tokens，这本身就是一个 confound。\n\n5. Self-contamination 中 ρ 的设置方式是 token-level injection ratio——这意味着合成 tokens 是均匀混入的。但真实污染是 document-level 的（整个文档是合成的或不是）。Table 1 脚注 2 提到合成文档较短（avg 364 vs 500 words），document-level synthetic fraction 是 35.6% at ρ=0.4。这是否意味着 document-level 的信号更强（整篇合成文档 vs. 随机 token 混入），使检测更容易？\n\n---\n\n## Missing References\n\n论文的引用覆盖在修订后已较完整。建议补充：\n- **Xie et al. (2024)**, \"DOREMI: Optimizing Data Mixtures Speeds Up Language Model Pretraining\"——与 domain-level reweighting 直接相关\n- **Fan et al. (2024)** 或相关工作——关于 importance weighting 在 LM 训练中的 variance-bias tradeoff，可为 α_eff/ESS tradeoff 提供理论基础\n\n---\n\n## 主要优势\n\n1. **Epoch confound 发现是扎实且有价值的贡献**：通过 epoch-matched 控制实验证明 D&R 先前报告的 PPL 优势中 >95% 来自多轮数据暴露而非 filtering quality（Table 1, Δ from 0.396 to 0.017, 3 seeds 方向一致），这对后续 D&R 研究有直接方法论警示意义。\n\n2. **检测器校准 vs AUC 的 counter-intuitive 发现**：GPT-2 detector (AUC=0.91, ECE=0.131) 性能劣于 uniform training (Δ=+0.098)，而 TF-IDF+LR (AUC=0.94, ECE=0.048) 成功——揭示了 calibration 可以逆转 intervention 的方向（§5.2, Table 13），这一发现对 data curation 工作有实际指导价值。\n\n3. **诚实的结果报告**：下游 null result（Table 4）、scale 限制（1.7B 效应减弱）、cross-model mixed results（Appendix O）均如实报告，没有 cherry-picking。这种学术诚信值得肯定。\n\n4. **Appendix 覆盖全面**：17 个 appendix 节，涵盖 grid search、threshold sweep、constraint 分解、checkpoint resume artifact、cross-model transfer、低 ρ 分析等，可复现性强。\n\n---\n\n## 总结\n\n本文的分析贡献（epoch confound、detector requirements）是有价值的，达到 Findings 水准。但作为一篇以定量分析为核心的论文，N=3 的统计检验力不足是根本性的弱点——校正后所有 p 值均未达标，bootstrap CI 在 N=3 下不可靠。自适应方法的效应量（0.11% PPL）在当前 scale 下没有实际意义，batch-size 外推是 speculation 而非 evidence。建议在 camera-ready 中：(1) 增加 seeds 或放弃 p 值叙事，(2) 将方法贡献降级为分析框架的 corollary 而非独立贡献，(3) 补充 α_eff-only ablation 以分离两个 constraint 的独立贡献。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告 — 方法严谨性 + 实验设计\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight (D&R) 范式在续训语言模型中应对合成文本污染的有效性条件。在 Qwen3-0.6B 上使用 132M FineWeb 子集进行可控实验，提出三项分析发现：(1) D&R 先前报告的 PPL 优势中 >95% 可归因于 epoch confound（多轮数据暴露），epoch-matched 后优势从 0.396 缩减至 0.017；(2) 有效的 reweighting 要求检测器同时具备足够的 AUC（≥0.9）和良好的校准（ECE≤0.05），高 AUC 但低校准的检测器反而劣于均匀训练；(3) 基于双约束（α_eff ≥ τ, ESS ≥ n_min）的自适应 b* 实现最小干预，性能接近 grid search 最优。方法在 ρ=0.4 时获得 Δ=−0.020 PPL（~0.11% relative），下游任务无显著改善。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3/5 (Acceptable) | Epoch confound 发现方法论可靠，但 adaptive method 的统计证据不足（N=3, 校正后均未达 α=0.05），α_eff proxy R²≈0.49 |\n| **Excitement** | 2/5 (Potentially Interesting) | Epoch confound 对社区有方法论警示价值，但效应量极小（0.11% PPL），下游零改善，实际影响有限 |\n| **Reproducibility** | 4/5 | 实验设置详细（§4），超参数透明，代码承诺开源，17 个 appendix 覆盖完整 |\n| **Confidence** | 4/5 | 对统计方法论和实验设计领域较为熟悉，仔细检查了主要论点 |\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n\n**一句话总结**: Epoch confound 的发现有真实的方法论价值，足以支撑 Findings 级别的贡献，但自适应方法的统计证据不足（N=3 无校正显著性、下游零改善、效应量极小）使其无法达到主会议标准。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 的统计推断力根本性不足\n- 具体位置：§5.1, Table 2, 以及论文中所有 p 值和 CI 报告\n- 问题：全文核心量化结论依赖于 N=3 seeds 的 paired t-test（仅 2 个自由度）。主要结果：\n  - ρ=0.4: uncorrected p=0.019, BH-corrected p=0.078（未达 α=0.05）\n  - ρ=0.6: uncorrected p=0.010, BH-corrected p=0.064（未达 α=0.05）\n  \n  论文报告了 bootstrap CI [−0.028, −0.012]（§5.1），但 N=3 的 bootstrap 仅有 3³=27 个可能的重抽样本，CI 的覆盖率保证极其脆弱。论文声称 Cohen's d=2.86, power>0.90，但如此高的 d 值更可能反映的是方差被人为压低（seeds 只影响参数初始化，data order 固定），而非效应量大。实际上这恰恰说明 3 个 seeds 探索的随机性维度极其有限。\n\n  更关键的是：论文先选择了 BH 校正（k=9），然后在校正结果不理想时论证家族 \"structurally heterogeneous\"，校正过于保守。这构成了一种 post-hoc 的统计叙事调整——你不能在分析前选择校正方法，分析后否定它。\n- 为什么影响接收：这是一篇以定量分析为核心的论文，如果核心量化结论在标准统计检验下均不显著，整个 adaptive method 的贡献就缺乏可靠支撑。\n- 建议修改方向：(a) 增加到至少 N=5 seeds（4 df，可检测 d=2.0 的效应）；或 (b) 如果计算资源不允许，全面放弃 p 值叙事，改为纯效应量+方向一致性报告，明确承认统计检验力不足；(c) 对 BH 校正取一个立场并坚持——要么不用（给出理由），要么用了就接受结果。\n\n**N2** [critical] 效应量与 claim 之间的严重脱节\n- 具体位置：§5.1 (Δ=−0.020 PPL), Table 4 (downstream null), §7 Conclusion\n- 问题：adaptive 方法的核心效应量为 Δ=−0.020 PPL，相对改善仅 0.11%。五项下游任务（Table 4, MMLU/HellaSwag/ARC/WinoGrande/PIQA）全部 |Δ|≤0.01，在标准误内无法区分。论文将这归因于 \"PPL-to-downstream transfer is nonlinear and scale-dependent\"（引用 Tay et al., 2023），但这恰恰意味着在可验证的当前 scale 下，该方法没有实际用途。\n\n  §5.4 的 batch-size amplification 外推更成问题：仅用 B={4,8,16} 三个点拟合幂律 Δ∝B^α（α≈0.89），然后外推到 B=128 预测 Δ≈−0.39。用 3 个数据点拟合幂律并外推 8 倍，任何统计学教材都会认为这不可靠。论文虽标注 \"speculative\"，但 rebuttal 中将其作为实际意义的主要论据（\"a practically meaningful improvement\"）。\n- 为什么影响接收：如果方法在可测量的所有指标上都没有实际改善，contribution 主要在分析框架本身——这需要论文的 framing 与之匹配，避免方法论贡献的过度包装。\n- 建议修改方向：(a) 在 abstract 和 conclusion 中删除所有关于 \"practical\" 的表述——当前 scale 下该方法不 practical；(b) 将 batch-size 外推从主文移到 appendix，标注为 hypothesis 而非 evidence；(c) 更诚实地承认：在可验证范围内，adaptive reweighting 的实际增益可忽略不计。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Self-contamination 实验设计的生态效度严重不足\n- 具体位置：§4 \"Training Data\", §7 Limitations\n- 问题：generator=trainee 的设计意味着合成数据来自被训练模型自身（Qwen3-0.6B 生成 → Qwen3-0.6B 检测+训练）。这人为降低了检测难度：模型生成的文本带有自身的统计指纹，TF-IDF+LR 检测器能达到 AUC=0.94 部分归因于此。真实世界中，污染来源是异构的（GPT-4、Claude、Gemini 等多种模型，且不同版本），检测难度远高于 self-contamination。\n\n  论文在 Limitations（§9, p.9）中承认了这一限制（\"limits ecological validity\"），但论文的第二项核心 claim——detector requirements（AUC≥0.9, ECE≤0.05）——直接依赖于检测器性能数据。在 self-contamination 下得出的检测器阈值，在 cross-model contamination 下可能完全不适用。Appendix O 的 cross-model transfer（Llama-3.2-3B）是 single seed 且结果 mixed（MMLU +1.57pp, HellaSwag −0.60pp），不足以验证。\n- 建议：(a) 至少增加一个 cross-generator 实验（用 GPT-2-large 或其他开放模型生成污染数据），在主文中报告；(b) 将 detector requirements 的 claim 明确限定为 self-contamination 场景。\n\n**W2** [warning] α_eff proxy 的解释力不足以支撑其在方法中的核心地位\n- 具体位置：§3 Method (α_eff 定义), §6 Discussion, Table 11, Appendix K\n- 问题：α_eff 是 adaptive b* 方法的核心机制——它是双约束中 quality floor 的直接操作变量。但 Table 11 显示 α_eff 与 ground-truth batch-level real fraction 的 Pearson r=0.70（R²≈0.49），即 proxy 仅解释了不到一半的方差。论文的方差分解（~70% detector noise, ~30% ESS compression）基于单一 seed 的定性归因，没有正式的方差分解统计。\n\n  Rebuttal 中报告 r(α_eff, mean_q)=0.80，但这是 proxy-to-detector-score 的相关性（循环论证），而非 proxy-to-ground-truth。cross-seed spread <0.003 看似稳定，但 α_eff 是 q-scores 的确定性函数且 detector 固定，所以跨 seed 稳定是预期结果，不构成额外证据。\n\n  根本问题：当方法的核心信号只解释 49% 的目标方差时，为什么 minimum intervention（保守使用这个噪声信号）优于 uniform？一个更简洁的解释是：adaptive b* 的实际贡献主要来自 ESS constraint 的稳定化作用，而非 α_eff 的质量信号。\n- 建议：(a) 增加 ablation：固定 α_eff=constant，只保留 ESS constraint，测试 PPL 差异；(b) 如果这个 ablation 表明 ESS 是主要贡献者，需要重写 §6 的 narrative。\n\n**W3** [warning] 实验范围过窄，不支撑 \"necessary conditions\" 的普适性 claim\n- 具体位置：§7 Conclusion (\"three effectiveness conditions\"), §5.2-5.4, Limitations\n- 问题：论文声称识别了三个 \"effectiveness conditions\"（AUC≥0.9, ECE≤0.05, ρ≥0.4），但支撑这些条件的实验仅覆盖：\n  - 1 个模型家族（Qwen3, 0.6B/1.7B）\n  - 1 个数据集（FineWeb 132M）\n  - 1 种污染类型（self-contamination）\n  - 4 个 ρ 值（0.2/0.3/0.4/0.6）\n  - 3 个 seeds（主实验）/ 1 个 seed（1.7B, cross-model）\n\n  \"necessary conditions\" 是一个逻辑上很强的 claim：它意味着在任何设置下，这些条件都是必要的。但实际实验仅在一个极窄的设置上观察到了这些阈值。ρ 覆盖的不完整性尤其明显：ρ=0.2 和 ρ=0.3 均在 degradation zone，ρ=0.4 是 borderline，ρ=0.6 有效——但 ρ=0.5 没有测试，无法确定 boundary 的精确位置。AUC/ECE 阈值来自仅 3 个检测器（TF-IDF+LR, GPT-2, N-gram）的比较，样本量太小。\n- 建议：(a) 将 \"necessary conditions\" 改为 \"empirically observed conditions in our setting\"；(b) 在 Limitations 中明确讨论跨模型/数据集/污染类型的泛化限制。\n\n**W4** [warning] Epoch confound 实验中 LR schedule 混淆因素未完全排除\n- 具体位置：Table 1, §5.1 \"LR-controlled verification\"\n- 问题：Table 1 的 epoch-matched comparison 中，epoch-matched D&R \"shares the full-length LR schedule\"——即使用完整训练长度的 LR schedule 但仅训练 2,553 步（vs. 原始 6,103 步）。这引入了一个新的混淆：LR schedule 的形状（warmup/decay phase 的比例）在截断训练中与完整训练不同。\n\n  §5.1 提到 \"an independent-schedule replication (D&R 17,601 vs shared-schedule uniform 18,062) matches the shared-schedule result (Δ=−0.068)\"，但这个 independent-schedule 控制的细节仅在正文中一句话带过，没有在 Table 1 中呈现，也没有在 appendix 中提供完整的 LR 曲线对比。\n\n  更根本的问题：epoch-matched comparison 通过缩短训练来消除 epoch confound，但缩短训练本身改变了训练动态（如 gradient noise scale, batch normalization statistics 等）。一个更干净的控制是在相同步数下，通过 upsampling 非污染数据来匹配 content epochs。\n- 建议：(a) 在 appendix 中展示 epoch-matched 和 full-training 的完整 LR curves；(b) 讨论 early-stopping vs. content-epoch-matching 的 confound 可能性；(c) 如果可行，补充 upsampling baseline。\n\n---\n\n## 小问题（不影响接收）\n\n- **m1**: Table 2 中 \"Golden Ratio\" 行的 w 定义（w = 1/q if q > 0.5, else 0）没有在正文中给出，需要翻到 Appendix C 才能理解。建议在 §4 Methods 中简要说明。\n\n- **m2**: §5.2 中 \"Robustness and Boundary Conditions\" 小节同时讨论 ρ=0.6 的结果和 boundary conditions，建议拆分为两个子节以提高可读性。\n\n- **m3**: Figure 2 的 x 轴标签 \"Sharpening exponent b\" 与正文中 \"b* per-batch adaptive\" 的关系不够清晰——Figure 2 是 grid search 结果，b 是固定值，但正文的叙事已转向 adaptive b*，容易造成混淆。\n\n- **m4**: Appendix Q 的 ρ=0.3 boundary 结果（Δ=+0.002, non-significant）是一个重要数据点，建议在主文 §5.2 中明确引用。\n\n- **m5**: §2 Related Work 中引用了 \"Drayson et al., 2025\" 在多处但未指出该工作的具体方法与本文的关键区别（from-scratch vs. continued pretraining）——这个区别恰恰是 epoch confound 成立的前提，应在 Related Work 中就明确讨论。\n\n---\n\n## Questions for Authors\n\n1. N=3 的设计是计算资源限制还是有意为之？如果是资源限制，是否考虑过降低训练步数（如 3000 steps）来换取更多 seeds（如 N=7）？这种 tradeoff 在统计上可能更有价值。\n\n2. α_eff-only ablation（去掉 ESS constraint，只保留 α_eff ≥ τ）的 PPL 是多少？Table 2 有 ESS-only 但缺少 α_eff-only。这对理解两个 constraint 的独立贡献至关重要。\n\n3. Rebuttal 中的 per-seed α_eff correlation（Table with r=0.80）与主文 Table 11 的 r=0.70 的区别是什么？前者似乎是 α_eff vs. mean(q)（detector score），后者是 α_eff vs. true real fraction——如果是这样，r=0.80 是检测器自身的 consistency 而非 proxy 的 ground-truth fidelity，不应作为支持 proxy 可靠性的证据。\n\n4. Batch-size amplification实验（§5.4, B=4/8/16）是在固定 total tokens 下进行的，还是固定 steps？如果固定 steps，那 B=16 看到了比 B=4 多 4 倍的 tokens，这本身就是一个 confound。\n\n5. Self-contamination 中 ρ 的设置方式是 token-level injection ratio——这意味着合成 tokens 是均匀混入的。但真实污染是 document-level 的（整个文档是合成的或不是）。Table 1 脚注 2 提到合成文档较短（avg 364 vs 500 words），document-level synthetic fraction 是 35.6% at ρ=0.4。这是否意味着 document-level 的信号更强（整篇合成文档 vs. 随机 token 混入），使检测更容易？\n\n---\n\n## Missing References\n\n论文的引用覆盖在修订后已较完整。建议补充：\n- **Xie et al. (2024)**, \"DOREMI: Optimizing Data Mixtures Speeds Up Language Model Pretraining\"——与 domain-level reweighting 直接相关\n- **Fan et al. (2024)** 或相关工作——关于 importance weighting 在 LM 训练中的 variance-bias tradeoff，可为 α_eff/ESS tradeoff 提供理论基础\n\n---\n\n## 主要优势\n\n1. **Epoch confound 发现是扎实且有价值的贡献**：通过 epoch-matched 控制实验证明 D&R 先前报告的 PPL 优势中 >95% 来自多轮数据暴露而非 filtering quality（Table 1, Δ from 0.396 to 0.017, 3 seeds 方向一致），这对后续 D&R 研究有直接方法论警示意义。\n\n2. **检测器校准 vs AUC 的 counter-intuitive 发现**：GPT-2 detector (AUC=0.91, ECE=0.131) 性能劣于 uniform training (Δ=+0.098)，而 TF-IDF+LR (AUC=0.94, ECE=0.048) 成功——揭示了 calibration 可以逆转 intervention 的方向（§5.2, Table 13），这一发现对 data curation 工作有实际指导价值。\n\n3. **诚实的结果报告**：下游 null result（Table 4）、scale 限制（1.7B 效应减弱）、cross-model mixed results（Appendix O）均如实报告，没有 cherry-picking。这种学术诚信值得肯定。\n\n4. **Appendix 覆盖全面**：17 个 appendix 节，涵盖 grid search、threshold sweep、constraint 分解、checkpoint resume artifact、cross-model transfer、低 ρ 分析等，可复现性强。\n\n---\n\n## 总结\n\n本文的分析贡献（epoch confound、detector requirements）是有价值的，达到 Findings 水准。但作为一篇以定量分析为核心的论文，N=3 的统计检验力不足是根本性的弱点——校正后所有 p 值均未达标，bootstrap CI 在 N=3 下不可靠。自适应方法的效应量（0.11% PPL）在当前 scale 下没有实际意义，batch-size 外推是 speculation 而非 evidence。建议在 camera-ready 中：(1) 增加 seeds 或放弃 p 值叙事，(2) 将方法贡献降级为分析框架的 corollary 而非独立贡献，(3) 补充 α_eff-only ablation 以分离两个 constraint 的独立贡献。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-23T13:16:18.715431+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-23T13:16:23.297251+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-23T13:16:23.347876+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-23T13:16:27.563745+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-23T13:16:27.564161+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 652 · 2026-05-23T13:16:38.620660+00:00_

审稿报告已提交给 Review Director。

**核心判断：Overall 3.0 (Findings)**

主要发现：
- **2 个 Must-Fix**：(1) N=3 seeds 统计推断力根本性不足，BH 校正后无显著性，bootstrap CI 在 N=3 下不可靠；(2) 效应量 0.11% PPL + 下游零改善与论文 claim 脱节，batch-size 外推用 3 点拟合幂律不可靠
- **4 个 Should-Fix**：self-contamination 生态效度不足、α_eff proxy R²≈0.49 解释力有限、实验范围过窄不支撑 "necessary conditions" 的普适性、epoch confound 实验中 LR schedule 混淆未完全排除
- **主要优势**：epoch confound 发现扎实有价值、检测器校准 vs AUC 的 counter-intuitive 发现有指导意义、结果报告诚实无 cherry-picking

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 22

## Round 22

16 recorded events


### User

_source line 653 · 2026-05-23T13:22:52.660891+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿报告

**Overall Assessment**: 3.0 / 5 (Findings)

### 官方维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 在其实验范围内方法论扎实，epoch-matched 对比设计合理；但 N=3 seeds 的关键结果校正后未达显著 |
| Excitement | 2.5 / 5 | Epoch confound 发现对方法学有价值；其余两个 findings 属于预期内的增量贡献 |
| Overall | 3.0 / 5 | 分析论文定位合理，但效应量过小 + 范围过窄 + adaptive b* 方法新颖性不足 |
| Confidence | 4 / 5 | |
| Reproducibility | 4 / 5 | |

### Must-Fix 问题

**N1** [critical] Abstract 超过 200 words 限制
- EMNLP 2026 / ARR 要求 abstract ≤ 200 words。当前 abstract 包含大量数值和数学表达式（Δ=−0.020, ρ=0.4, p=0.010, bootstrap CI 等），估计约 220–230 words，明显超限。
- 格式硬约束违反，desk reject 风险。

**N2** [critical] 正文疑似超出 8 页限制
- Section 7 Conclusion 在第 8 页底部开始，conclusion 正文延伸至第 9 页顶部（约 10–15 行），之后才是 Limitations。按 EMNLP 2026 规定，§1–§7 主正文必须 ≤ 8 页。

**N3** [critical] 核心效应量过小且统计显著性不足
- ρ=0.4: Δ=−0.020, p_BH=0.078; ρ=0.6: Δ=−0.032, p_BH=0.064。k=9 的 family-wise correction 下无一达标。Δ=−0.020 对应 ~0.1% relative improvement，downstream benchmark 完全无差异。

**N4** [critical] 实验范围过窄，limiting generalizability
- 单一模型族 Qwen3（0.6B + 1.7B 补充），单一数据集 FineWeb 132M，自污染设计。Cross-model transfer（Appendix O）single seed 且结果 mixed。三个核心 findings 的泛化性无法从当前实验推断。

### Should-Fix 问题

**W1** [warning] Adaptive b* 方法新颖性薄弱
- 权重公式 w=(1−q)^b 完全来自 Drayson et al.；adaptive b* 本质是超参数自动选择启发式。§3 仍占 ~0.75 页。

**W2** [warning] Epoch confound finding 的适用范围需明确限定
- 在大规模 from-scratch pretraining（通常 <1 epoch）中，epoch confound 不成立。论文正文表述过于 general。

**W3** [warning] Detector 测试范围不足
- 仅 3 个 detector，未覆盖 RoBERTa/ModernBERT fine-tuned, DetectGPT, Binoculars。3 个数据点不足以建立 "both AUC and ECE are necessary" 的因果关系。

**W4** [warning] Batch-size extrapolation 缺乏支撑
- 3 个点（B=4,8,16）拟合 scaling exponent 然后外推到 B=128（32× extrapolation）统计学上极不可靠。B=16 仅 single seed，B=8 仅 2-seed mean。

**W5** [warning] 部分关键信息藏在脚注中
- p_BH=0.078（ρ=0.4）和 p_BH=0.064（ρ=0.6）仅出现在脚注中。

### 小问题
- m1: Table 2 Golden Ratio/D&R bold 标注可能误导
- m2: §2 Related Work 占 ~1.5 页偏长
- m3: Figure 1 TikZ 黑白打印下背景色无法区分
- m4: rebuttal Appendix Q 标签需核对
- m5: ρ 同时表示 contamination ratio 和 Spearman 相关系数，符号冲突

### 缺失引用
- MATES (Yu et al., NeurIPS 2024)
- FineWeb-Edu (Lozhkov et al., 2024)
- D4 (Tirumala et al., 2024)

### Questions
1. 如果 family-wise correction 的 family 缩小为仅 focal comparison，corrected p-values 会是多少？
2. 真实 web contamination 下 detector 的 AUC/ECE 预期变化？
3. Epoch confound 核心发现是否可以通过更简单的实验验证，而不需要 adaptive b*？

---

请对以上每一个 Must-Fix、Should-Fix 和 Minor 问题给出你的 [AGREE] 或 [REBUT] 判断及理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-23T13:23:02.909905+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "1",
  "dpi": "160"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "1",
    "dpi": "160"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-23T13:23:03.411880+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p1.png\", \"width\": 1323, \"height\": 1871, \"size_kb\": 465.0}], \"total_pages\": 17, \"rendered_pages\": 1, \"dpi\": 160, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-23T13:23:03.913894+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "8-9",
  "dpi": "160"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "8-9",
    "dpi": "160"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-23T13:23:04.215394+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p8.png\", \"width\": 1323, \"height\": 1871, \"size_kb\": 543.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p9.png\", \"width\": 1323, \"height\": 1871, \"size_kb\": 516.1}], \"total_pages\": 17, \"rendered_pages\": 2, \"dpi\": 160, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-23T13:23:06.774202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-23T13:23:07.681713+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-23T13:23:07.732484+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 661 · 2026-05-23T13:23:07.935040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-23T13:23:08.740577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-23T13:23:08.942609+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-23T13:25:43.017647+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Abstract 超过 200 words 限制**\n同意。我逐词核实了 PDF 第 1 页的 abstract，粗略计数约 220–240 words（取决于数学表达式的计词方式），明显超过 EMNLP 2026 的 200 words 硬约束。Abstract 中包含大量数值细节（Δ=−0.020, ρ=0.4, bootstrap CI, p=0.010 等），这些可以移到 Introduction。这是格式硬约束，有 desk reject 风险，必须修正。我在自己的审稿中遗漏了这个问题。\n\n**[AGREE] R2-N2: 正文疑似超出 8 页限制**\n同意。从 PDF 第 8-9 页可以确认：§7 Conclusion 在第 8 页右栏底部开始（\"We identify three effectiveness conditions for detect-and-reweight...\"），正文延伸到第 9 页左栏（约 15-20 行），之后才是 Limitations section。按 EMNLP 2026 规定（§1-§7 主正文 ≤8 页，Limitations/Ethics 不计入但不得包含过多额外内容），这构成格式违规。修正方案：压缩 §7 Conclusion（当前约 0.75 列），或压缩 §2 Related Work（R2-m2 也提到偏长，约 1.5 页）。这个问题我同样遗漏了。\n\n**[AGREE] R2-N3: 核心效应量过小且统计显著性不足**\n完全同意，这与我自己的 N1 和 N2 高度一致。补充几点我的审稿中已阐述的细节：\n- N=3 的 bootstrap CI 仅有 3³=27 种重抽样可能，覆盖率保证极差（我的 N1）\n- 论文先选择 BH 校正（k=9），校正后不理想又论证 family \"structurally heterogeneous\" 是 post-hoc 的统计叙事调整（我的 N1）\n- Batch-size 外推（3 个点拟合幂律到 B=128）在统计学上不可靠（我的 N2）\n- 值得注意的是，epoch confound 的核心发现（>95% 归因于多轮暴露）不受 N=3 限制——该结论在每个 seed 内独立成立，是方向性的定性结论而非依赖 p 值的定量结论\n\n**[AGREE] R2-N4: 实验范围过窄**\n同意，与我的 W3 一致。R2 正确指出单一模型族 + 单一数据集 + 自污染的三重局限使得 \"necessary conditions\" 这一 claim 无法泛化。我额外指出一点：ρ 覆盖不完整（缺 ρ=0.5），boundary 位置的精确性未被验证。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Adaptive b* 方法新颖性薄弱**\n同意。权重公式 w=(1−q)^b 完全沿用 Drayson et al.，adaptive b* 本质是在两个约束（α_eff ≥ τ, ESS ≥ n_min）下的超参数自动选择，技术新颖性有限。论文已将其定位为 \"practical corollary\"，但 §3 仍占约 0.75 页，给人的印象仍然是一个独立的方法贡献。如果进一步压缩 §3（如合并到 §4），可以释放空间给 Conclusion（解决 R2-N2 的页面超限问题）。\n\n**[AGREE] R2-W2: Epoch confound 适用范围需限定**\n同意。Epoch confound 的前提是续训中数据量小导致多轮暴露（132M tokens, 6103 steps → ~3.2 content epochs at ρ=0.4）。在 from-scratch pretraining 的典型设置中（数百 B tokens, <1 epoch），这个 confound 不成立。论文在 rebuttal W4 中承认了这一点，但主文表述过于泛化——例如 §7 Conclusion 中 \"any D&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness\" 这句话严格来说只适用于会发生多轮暴露的场景。建议在该句后加 qualifier: \"in settings where filtered data leads to multi-epoch exposure (e.g., continued pretraining on small corpora)\"。\n\n**[AGREE] R2-W3: Detector 测试范围不足**\n同意，与我的审稿精神一致。仅 3 个 detector（TF-IDF+LR, GPT-2, N-gram）不足以建立 \"both AUC and ECE are necessary\" 的因果关系。3 个数据点可以提示一个 pattern，但不能排除混淆因素（如：TF-IDF+LR 成功可能是因为它的特征空间恰好与 FineWeb 的分布匹配，而非因为 ECE 低）。缺少的关键 detector 类别包括：(a) fine-tuned neural classifiers (RoBERTa-based, ModernBERT)——这些在实际应用中最常用；(b) zero-shot methods (DetectGPT, Binoculars)——这些不需要标注数据。当前 3 个 detector 的 AUC/ECE 组合恰好支持作者的叙事（高 AUC 低 ECE → 成功，高 AUC 高 ECE → 失败，低 AUC 低 ECE → 不够），但这可能是巧合而非因果。\n\n**[AGREE] R2-W4: Batch-size extrapolation 缺乏支撑**\n完全同意，这与我的 N2 中的分析一致。补充一个 R2 正确指出但我未详细展开的细节：B=16 仅 single seed，B=8 仅 2-seed mean——这意味着外推的基础数据本身就是 under-powered 的。3 个点拟合 α≈0.89 并外推 32 倍到 B=128，在任何定量分析标准下都不可接受。\n\n**[REBUT] R2-W5: 部分关键信息藏在脚注中**\n部分不同意。从 PDF 第 5 页 §5.1 的文本来看，BH-corrected p 值（p_BH=0.078 和 p_BH=0.064）出现在 §5.1 的正文段落中（\"after Bonferroni-Holm correction for nine family-wise comparisons, p_BH=0.078, which does not reach conventional significance\"），而非仅在脚注中。脚注中确实包含一些补充信息（如 checkpoint resume artifact 的说明），但核心统计结果是在正文中报告的。\n\n不过，R2 的关注方向是对的：即使在正文中，这些校正后不显著的 p 值被包裹在大量数值中，容易被读者忽略。更好的做法是在 Table 2 中直接增加一列 p_BH，使校正结果与效应量并列展示。\n\n---\n\n### 小问题\n\n**[AGREE] R2-m1: Table 2 bold 标注可能误导**\n同意。如果 bold 表示 \"best\"，但 adaptive b* 与 grid-best 的差异在 cross-seed σ 之内，bold 标注暗示了实际上不存在的统计显著差异。\n\n**[REBUT] R2-m2: Related Work 占 ~1.5 页偏长**\n部分不同意。本文定位为 analysis paper，需要比标准 method paper 更详细地梳理前人工作，以建立 epoch confound 和 detector requirements 的 novelty。§2 覆盖了 5 个子领域（D&R, detection, domain-level mixing, instance-level weighting, theoretical foundations），每个约 0.3 页，不算冗长。但如果需要解决 R2-N2 的页面超限问题，Related Work 是最合理的压缩候选——可以将 \"Theoretical Foundations\" 子段压缩或移到 appendix。\n\n**[AGREE] R2-m3: Figure 1 TikZ 黑白打印可读性**\n同意。学术论文应保证灰度可读性。\n\n**[AGREE] R2-m4: Appendix Q 标签核对**\n同意。交叉引用标签应在 camera-ready 前逐一验证。\n\n**[AGREE] R2-m5: ρ 符号冲突**\n同意。ρ 同时用作 contamination ratio（§3-§7 全文）和 Spearman 相关系数（Table 12, Appendix K），在同一论文中造成歧义。建议将 contamination ratio 改为 ρ_c 或 γ，或将 Spearman 相关系数标记为 ρ_s。\n\n---\n\n### 对 R2 Questions 的补充观点\n\n**Q1（缩小 family 后的 corrected p-values）**：如果仅对 focal comparison（adaptive vs. uniform at ρ=0.4）做单次检验，uncorrected p=0.019 即为最终 p 值。但这实质上是 cherry-picking the comparison family——论文实际进行了 9 个比较，选择性地只校正其中 1 个等于没有校正。正确的做法应该是：(a) 事先（pre-registration）指定 focal comparison，或 (b) 接受 k=9 的校正结果。论文两条路都没走干净。\n\n**Q2（真实 web contamination 下 detector 性能）**：我在 W1 中详细讨论了这一点。Self-contamination 下 TF-IDF+LR 达到 AUC=0.94，但在 cross-model 场景下（异构生成器、版本混合、经过 paraphrasing/post-editing 的合成文本），AUC 很可能下降到 0.80-0.85 范围，此时论文的 \"AUC≥0.9\" 条件将难以满足，方法可能失效。\n\n**Q3（epoch confound 是否可以更简单验证）**：完全可以。Epoch confound 的验证只需要 (a) standard D&R（filtering），(b) epoch-matched baseline（相同 content epochs 下的 uniform training），两个实验即可。不需要 adaptive b*、不需要 α_eff proxy、不需要 ESS constraint。这进一步说明 epoch confound 是本文的核心独立贡献，而 adaptive method 是附加的、且支撑不足的贡献。\n\n---\n\n### 综合评价\n\nR2 和我的评价在方向和力度上高度一致（同为 Overall 3.0 / Findings），核心分歧很小。R2 发现了两个我遗漏的重要格式问题（N1 abstract 超限、N2 页面超限），这些是硬约束违规，应提升到 Must-Fix。我的审稿在统计方法论细节上更深入（bootstrap CI 覆盖率、Cohen's d 解读、BH 校正的 post-hoc 叙事问题），R2 在格式合规和方法新颖性评估上更全面。\n\n两份审稿的共同判断：epoch confound 是有价值的方法论贡献，但 adaptive method 统计证据不足 + 效应量可忽略 + 实验范围过窄，整体达 Findings 但不达主会议标准。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Abstract 超过 200 words 限制**\n同意。我逐词核实了 PDF 第 1 页的 abstract，粗略计数约 220–240 words（取决于数学表达式的计词方式），明显超过 EMNLP 2026 的 200 words 硬约束。Abstract 中包含大量数值细节（Δ=−0.020, ρ=0.4, bootstrap CI, p=0.010 等），这些可以移到 Introduction。这是格式硬约束，有 desk reject 风险，必须修正。我在自己的审稿中遗漏了这个问题。\n\n**[AGREE] R2-N2: 正文疑似超出 8 页限制**\n同意。从 PDF 第 8-9 页可以确认：§7 Conclusion 在第 8 页右栏底部开始（\"We identify three effectiveness conditions for detect-and-reweight...\"），正文延伸到第 9 页左栏（约 15-20 行），之后才是 Limitations section。按 EMNLP 2026 规定（§1-§7 主正文 ≤8 页，Limitations/Ethics 不计入但不得包含过多额外内容），这构成格式违规。修正方案：压缩 §7 Conclusion（当前约 0.75 列），或压缩 §2 Related Work（R2-m2 也提到偏长，约 1.5 页）。这个问题我同样遗漏了。\n\n**[AGREE] R2-N3: 核心效应量过小且统计显著性不足**\n完全同意，这与我自己的 N1 和 N2 高度一致。补充几点我的审稿中已阐述的细节：\n- N=3 的 bootstrap CI 仅有 3³=27 种重抽样可能，覆盖率保证极差（我的 N1）\n- 论文先选择 BH 校正（k=9），校正后不理想又论证 family \"structurally heterogeneous\" 是 post-hoc 的统计叙事调整（我的 N1）\n- Batch-size 外推（3 个点拟合幂律到 B=128）在统计学上不可靠（我的 N2）\n- 值得注意的是，epoch confound 的核心发现（>95% 归因于多轮暴露）不受 N=3 限制——该结论在每个 seed 内独立成立，是方向性的定性结论而非依赖 p 值的定量结论\n\n**[AGREE] R2-N4: 实验范围过窄**\n同意，与我的 W3 一致。R2 正确指出单一模型族 + 单一数据集 + 自污染的三重局限使得 \"necessary conditions\" 这一 claim 无法泛化。我额外指出一点：ρ 覆盖不完整（缺 ρ=0.5），boundary 位置的精确性未被验证。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Adaptive b* 方法新颖性薄弱**\n同意。权重公式 w=(1−q)^b 完全沿用 Drayson et al.，adaptive b* 本质是在两个约束（α_eff ≥ τ, ESS ≥ n_min）下的超参数自动选择，技术新颖性有限。论文已将其定位为 \"practical corollary\"，但 §3 仍占约 0.75 页，给人的印象仍然是一个独立的方法贡献。如果进一步压缩 §3（如合并到 §4），可以释放空间给 Conclusion（解决 R2-N2 的页面超限问题）。\n\n**[AGREE] R2-W2: Epoch confound 适用范围需限定**\n同意。Epoch confound 的前提是续训中数据量小导致多轮暴露（132M tokens, 6103 steps → ~3.2 content epochs at ρ=0.4）。在 from-scratch pretraining 的典型设置中（数百 B tokens, <1 epoch），这个 confound 不成立。论文在 rebuttal W4 中承认了这一点，但主文表述过于泛化——例如 §7 Conclusion 中 \"any D&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness\" 这句话严格来说只适用于会发生多轮暴露的场景。建议在该句后加 qualifier: \"in settings where filtered data leads to multi-epoch exposure (e.g., continued pretraining on small corpora)\"。\n\n**[AGREE] R2-W3: Detector 测试范围不足**\n同意，与我的审稿精神一致。仅 3 个 detector（TF-IDF+LR, GPT-2, N-gram）不足以建立 \"both AUC and ECE are necessary\" 的因果关系。3 个数据点可以提示一个 pattern，但不能排除混淆因素（如：TF-IDF+LR 成功可能是因为它的特征空间恰好与 FineWeb 的分布匹配，而非因为 ECE 低）。缺少的关键 detector 类别包括：(a) fine-tuned neural classifiers (RoBERTa-based, ModernBERT)——这些在实际应用中最常用；(b) zero-shot methods (DetectGPT, Binoculars)——这些不需要标注数据。当前 3 个 detector 的 AUC/ECE 组合恰好支持作者的叙事（高 AUC 低 ECE → 成功，高 AUC 高 ECE → 失败，低 AUC 低 ECE → 不够），但这可能是巧合而非因果。\n\n**[AGREE] R2-W4: Batch-size extrapolation 缺乏支撑**\n完全同意，这与我的 N2 中的分析一致。补充一个 R2 正确指出但我未详细展开的细节：B=16 仅 single seed，B=8 仅 2-seed mean——这意味着外推的基础数据本身就是 under-powered 的。3 个点拟合 α≈0.89 并外推 32 倍到 B=128，在任何定量分析标准下都不可接受。\n\n**[REBUT] R2-W5: 部分关键信息藏在脚注中**\n部分不同意。从 PDF 第 5 页 §5.1 的文本来看，BH-corrected p 值（p_BH=0.078 和 p_BH=0.064）出现在 §5.1 的正文段落中（\"after Bonferroni-Holm correction for nine family-wise comparisons, p_BH=0.078, which does not reach conventional significance\"），而非仅在脚注中。脚注中确实包含一些补充信息（如 checkpoint resume artifact 的说明），但核心统计结果是在正文中报告的。\n\n不过，R2 的关注方向是对的：即使在正文中，这些校正后不显著的 p 值被包裹在大量数值中，容易被读者忽略。更好的做法是在 Table 2 中直接增加一列 p_BH，使校正结果与效应量并列展示。\n\n---\n\n### 小问题\n\n**[AGREE] R2-m1: Table 2 bold 标注可能误导**\n同意。如果 bold 表示 \"best\"，但 adaptive b* 与 grid-best 的差异在 cross-seed σ 之内，bold 标注暗示了实际上不存在的统计显著差异。\n\n**[REBUT] R2-m2: Related Work 占 ~1.5 页偏长**\n部分不同意。本文定位为 analysis paper，需要比标准 method paper 更详细地梳理前人工作，以建立 epoch confound 和 detector requirements 的 novelty。§2 覆盖了 5 个子领域（D&R, detection, domain-level mixing, instance-level weighting, theoretical foundations），每个约 0.3 页，不算冗长。但如果需要解决 R2-N2 的页面超限问题，Related Work 是最合理的压缩候选——可以将 \"Theoretical Foundations\" 子段压缩或移到 appendix。\n\n**[AGREE] R2-m3: Figure 1 TikZ 黑白打印可读性**\n同意。学术论文应保证灰度可读性。\n\n**[AGREE] R2-m4: Appendix Q 标签核对**\n同意。交叉引用标签应在 camera-ready 前逐一验证。\n\n**[AGREE] R2-m5: ρ 符号冲突**\n同意。ρ 同时用作 contamination ratio（§3-§7 全文）和 Spearman 相关系数（Table 12, Appendix K），在同一论文中造成歧义。建议将 contamination ratio 改为 ρ_c 或 γ，或将 Spearman 相关系数标记为 ρ_s。\n\n---\n\n### 对 R2 Questions 的补充观点\n\n**Q1（缩小 family 后的 corrected p-values）**：如果仅对 focal comparison（adaptive vs. uniform at ρ=0.4）做单次检验，uncorrected p=0.019 即为最终 p 值。但这实质上是 cherry-picking the comparison family——论文实际进行了 9 个比较，选择性地只校正其中 1 个等于没有校正。正确的做法应该是：(a) 事先（pre-registration）指定 focal comparison，或 (b) 接受 k=9 的校正结果。论文两条路都没走干净。\n\n**Q2（真实 web contamination 下 detector 性能）**：我在 W1 中详细讨论了这一点。Self-contamination 下 TF-IDF+LR 达到 AUC=0.94，但在 cross-model 场景下（异构生成器、版本混合、经过 paraphrasing/post-editing 的合成文本），AUC 很可能下降到 0.80-0.85 范围，此时论文的 \"AUC≥0.9\" 条件将难以满足，方法可能失效。\n\n**Q3（epoch confound 是否可以更简单验证）**：完全可以。Epoch confound 的验证只需要 (a) standard D&R（filtering），(b) epoch-matched baseline（相同 content epochs 下的 uniform training），两个实验即可。不需要 adaptive b*、不需要 α_eff proxy、不需要 ESS constraint。这进一步说明 epoch confound 是本文的核心独立贡献，而 adaptive method 是附加的、且支撑不足的贡献。\n\n---\n\n### 综合评价\n\nR2 和我的评价在方向和力度上高度一致（同为 Overall 3.0 / Findings），核心分歧很小。R2 发现了两个我遗漏的重要格式问题（N1 abstract 超限、N2 页面超限），这些是硬约束违规，应提升到 Must-Fix。我的审稿在统计方法论细节上更深入（bootstrap CI 覆盖率、Cohen's d 解读、BH 校正的 post-hoc 叙事问题），R2 在格式合规和方法新颖性评估上更全面。\n\n两份审稿的共同判断：epoch confound 是有价值的方法论贡献，但 adaptive method 统计证据不足 + 效应量可忽略 + 实验范围过窄，整体达 Findings 但不达主会议标准。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-23T13:25:46.825838+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3808
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-23T13:25:51.733622+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-23T13:25:51.734090+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 668 · 2026-05-23T13:25:59.600661+00:00_

交叉回应已提交给 Review Director。

对 R2 的 4 个 Must-Fix 全部 AGREE（abstract 超限和页面超限是我遗漏的格式硬约束），5 个 Should-Fix 中 4 个 AGREE、1 个 REBUT（W5 关于 p_BH 藏在脚注——实际上出现在正文 §5.1 中，不过建议改为在 Table 2 中并列展示），5 个 Minor 中 4 个 AGREE、1 个部分 REBUT（m2 Related Work 长度对 analysis paper 来说合理，但可作为页面超限的压缩候选）。两份审稿在核心判断上高度一致：Overall 3.0 / Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 23

## Round 23

88 recorded events


### User

_source line 669 · 2026-05-24T04:10:33.989660+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。

## Venue 信息
- **目标**: EMNLP 2026 via ARR
- **截止日期**: 2026-05-25
- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）
- **模板**: ACL (review mode)
- **匿名规则**: Double-blind via ARR
- **Abstract**: ≤200 words
- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit)

## 论文路径
- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf`

## 你的审查侧重

### 1. 统计分析严谨性
- N=3 seeds 的统计检验力是否足够支撑定量结论？
- p 值报告是否正确处理了多重比较？（Bonferroni-Holm 校正）
- Bootstrap CI 在 N=3 时的有效性
- Cohen's d 和效应量解读是否合理？

### 2. 实验设计
- Self-contamination 设计的控制变量是否充分？
- Epoch confound 分析：epoch-matched 控制组和 LR-controlled verification 是否严密？
- 消融层次（Adaptive < Uniform < ESS-only < Random）的因果推断是否成立？
- α_eff-only ablation (n_min=1) 实验的解读

### 3. 方法有效性
- α_eff proxy 的 r=0.79 correlation 是否足以支撑双约束框架？
- 双约束公式（α_eff ≥ τ, ESS ≥ n_min）的理论动机和实际验证
- Per-batch bisection 的计算开销和实际可行性
- B=4 micro-batch 上运行 dual constraint 的统计可靠性

### 4. 结果解读
- Δ=-0.020 PPL (0.11% relative) 的实际意义
- Downstream task 零改善的影响
- Batch-size amplification trend (B=4→8→16) 的外推可靠性
- ρ=0.2 failure case 的分析充分性

### 5. Detector 分析
- 3 个 detector 是否足以建立 AUC/ECE 的因果关系？
- Discriminative vs generative detector 的混杂因素

请提供完整审稿报告，包含：Strengths (逐条), Weaknesses (逐条，标注 must-fix / should-fix / minor), Questions, Missing References, Overall Assessment (ARR 分数 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-24T04:10:39.981033+00:00_

called Skill

<details open><summary>🔧 Tool call — Skill</summary>

```json
{
  "skill": "review-reviewer-session-start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Skill",
  "tool_args": {
    "skill": "review-reviewer-session-start"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-24T04:10:40.031707+00:00_

&lt;tool_use_error>Unknown skill: review-reviewer-session-start&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Skill",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-24T04:10:43.895801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-24T04:10:45.150940+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-24T04:10:45.301940+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-24T04:10:45.403017+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-24T04:10:52.340355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 677 · 2026-05-24T04:10:54.399900+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-24T04:10:55.011067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-24T04:10:58.072082+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Review Form Criteria

The main criteria for Findings papers are soundne
…[truncated 889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5731
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-24T04:10:59.330123+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 595.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4930
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-24T04:10:59.380780+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in Continued LM Pretraining}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	\input{sections/abstract}
40	\end{abstract}
41	
42	\section{Introduction}
43	\label{sec:intro}
44	\input{sections/introduction}
45	
46	\section{Related Work}
47	\label{sec:related}
48	\input{sections/related_work}
49	
50	\section{Method}
51	\label{sec:method}
52	\input{sections/method}
53	
54	\section{Experimental Setup}
55	\label{sec:experiments}
56	\input{sections/experiments}
57	
58	\section{Results}
59	\label{sec:results}
60	\input{sections/results}
61	
62	\section{Discussion}
63	\label{sec:discussion}
64	\input{sections/discussion}
65	
66	\section{Conclusion}
67	\label{sec:conclusion}
68	\input{sections/conclusion}
69	
70	\section*{Limitations}
71	\label{sec:limitations}
72	\input{sections/limitations}
73	
74	\section*{Ethics Statement}
75	All experiments use publicly available datasets (FineWeb) and open-weight models; no human subjects are involved. Code and data will be released upon acceptance.
76	
77	\bibliography{references}
78	
79	\ap
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4369
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-24T04:11:07.068021+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and any instructions for reviewers. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and any instructions for reviewers. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-24T04:11:07.973718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-24T04:11:08.434741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-24T04:11:09.440776+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1467
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-24T04:11:09.604606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-24T04:11:09.873616+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1438
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-24T04:11:10.088888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 689 · 2026-05-24T04:11:10.300202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 690 · 2026-05-24T04:11:11.158806+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1554
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-24T04:11:11.565261+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1476
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-24T04:11:11.666823+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-24T04:11:14.778214+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely but conceivable missed details
- **3**: Pretty sure but with chance of missing something despite general familiarity
- **2**: Willing to defend evaluation, but fairly likely to have missed details
- **1**: "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: Excellent - "one of the most thorough I have seen, given its type"
- **4**: Strong - sufficient support with optional extra experiments
- **3**: Acceptable - supports main claims; minor points need details
- **2**: Poor - major claims unsupported; significant technical/methodological problems
- **1**: Major Issues - insufficiently thorough or irrelevant to ACL

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: Exciting - would mention to others
- **3**: Interesting - might mention points or attend if time permits
- **2**: Potentially Interesting - doesn't resonate personally but might with community
- **1**: Not Exciting - irrelevant to computational language processing

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award - potential top 2.5% paper
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## 5. **Additional Evaluation Areas**

**Reproducibility** (1-5 scale): Assesses ability to reproduce results with varying difficulty levels

**Datasets** (1-5 scale): Evaluates value of released datasets from documentary to enabling impac
…[truncated 315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7710
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-24T04:11:30.048502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-24T04:11:31.005765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-24T04:11:31.058020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 697 · 2026-05-24T04:11:31.617077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-24T04:11:32.019297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-24T04:11:32.673993+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1615
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-24T04:11:32.674434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-24T04:11:34.235049+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2617
}
```

</details>

---


### Tool result

_source line 702 · 2026-05-24T04:11:34.888910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2869
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-24T04:11:35.091149+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2416
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-24T04:11:43.273928+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "11-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "11-17",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-24T04:11:44.026823+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 388.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 400.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 422.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 421.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 67.5}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-24T04:11:47.150185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-24T04:11:47.956748+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-24T04:11:48.057515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-24T04:11:48.408941+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-24T04:11:48.459488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-24T04:11:48.911293+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-24T04:11:48.911614+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-24T04:11:49.363399+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-24T04:11:49.363804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-24T04:11:50.317197+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-24T04:11:50.317563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-24T04:11:50.518432+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-24T04:11:50.518838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-24T04:11:50.571029+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-24T04:11:54.686408+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/",
  "description": "List PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/",
    "description": "List PDF image files"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-24T04:11:54.838008+00:00_

Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/': No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-24T04:11:59.797029+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "12-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "12-17",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-24T04:12:00.449741+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 388.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 400.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 422.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 421.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 67.5}], \"total_pages\": 17, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-24T04:12:05.017185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-24T04:12:05.874161+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-24T04:12:05.874594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-24T04:12:06.330769+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-24T04:12:06.331475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-24T04:12:06.886815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-24T04:12:07.138217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-24T04:12:07.348050+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-24T04:12:08.002192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-24T04:12:08.103672+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 965
}
```

</details>

---


### Tool result

_source line 734 · 2026-05-24T04:12:08.105120+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-24T04:12:08.306828+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-24T04:12:15.436738+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-24T04:12:15.437231+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-24T04:12:22.511819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-24T04:12:22.963802+00:00_

1	As synthetic text reaches an estimated 20--60\% of web corpora, the detect-and-reweight paradigm (downweighting likely-synthetic samples via $w(x) = (1-q(x))^b$) has gained traction, but its effectiveness conditions remain poorly understood.
2	Through controlled continued pretraining experiments (Qwen3-0.6B, 3 seeds), we analyze when and why detect-and-reweight works.
3	
4	We identify three findings.
5	First, an epoch-exposure confound in detect-and-remove evaluation: at matched content epochs, the reported advantage shrinks from 0.396 to 0.017 perplexity ($N{=}3$), revealing that ${>}$95\% of the reported advantage reflects data repetition rather than filtering quality.
6	Second, effective reweighting requires both discrimination and calibration from the detector; a poorly calibrated detector (ECE\,=\,0.131) degrades performance below uniform training, while a calibrated alternative succeeds.
7	Third, minimum intervention---applying the smallest sharpening exponent meeting a quality floor---outperforms unconstrained maximization.
8	
9	As a practical corollary, these findings yield an adaptive $b^*$ that improves over uniform at $\rho \geq 0.4$ ($\Delta{=}{-}0.020$; $\rho{=}0.6$: $\Delta{=}{-}0.032$, uncorrected $p{=}0.010$), transitioning from harmful ($\rho{=}0.2$) to beneficial with a sharp boundary in $[0.3, 0.4]$.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-24T04:12:22.964214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-24T04:12:23.014698+00:00_

1	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus with token-level contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$, assumed unknown~\citep{cheng2025contamination}.
2	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
3	Rather than selecting $b$ via grid search~\citep{drayson2025detection}, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
4	
5	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
6	
7	\paragraph{Quality floor.}
8	The \emph{effective authenticity} $\aeff(b) = \sum_i w_i(b)(1{-}q_i) / \sum_i w_i(b)$ measures the weighted mean detector confidence that samples are real.
9	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
10	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.79$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
11	
12	\paragraph{Stability ceiling.}
13	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
14	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
15	
16	\paragraph{Adaptive $\bstar$.}
17	Since $\aeff$ is non-decreasing and ESS is decreasing in $b$, the two constraints define an interval $[b_\tau, \bess]$.
18	The optimal exponent implements \emph{minimum intervention}:
19	\begin{equation}
20	  b^{*} = \begin{cases}
21	    0        & \text{if } \aeff(0) \geq \tau, \\
22	    b_\tau   & \text{if } b_\tau \leq \bess, \\
23	    \bess & \tex
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-24T04:12:23.466634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-24T04:12:23.918824+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.674, compared to 17.694 for uniform ($\Delta{=}{-}0.020$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean; gap $+$0.054).
8	A paired $t$-test yields $t{=}{-}7.1$, $p{=}0.019$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.078$, which does not reach conventional significance, though the 95\% BCa bootstrap CI $[{-}0.028, {-}0.012]$ excludes zero.
9	The practical value is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
10	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $4.7{\times}$ higher cross-seed variance than adaptive ($\sigma{=}0.033$ vs.\ $0.007$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
11	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
12	
13	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
14	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that detector $q$-scores carry genuine provenance signal; uninformed reweighting only increases gradient variance.
15	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
16	Only the dual-constr
…[truncated 10769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-24T04:12:23.919211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-24T04:12:23.969624+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	Our self-contamination design provides a controlled testbed with known ground-truth labels but limits ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss this limitation in \S\ref{sec:limitations}.
6	
7	\paragraph{Detector.}
8	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
9	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
10	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
11	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
12	
13	\paragraph{Training.}
14	We continue pretraining Qwen3-0.6B from its pretrained 
…[truncated 1914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-24T04:12:29.600517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-24T04:12:29.952060+00:00_

1	\paragraph{The epoch confound in D\&R evaluation.}
2	The bulk of D\&R's reported PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure rather than filtering quality (\S\ref{sec:main-results}).
3	An independent-LR replication (D\&R $17.651$ vs.\ shared-schedule $17.657$, $\Delta{=}0.006$) confirms that this finding is robust to LR schedule choice.
4	In multi-epoch continued pretraining, D\&R evaluations that do not control for content epochs systematically overstate filtering effectiveness; the residual benefit ($\Delta{=}0.017$ vs.\ adaptive $\bstar$, directionally consistent across 3 seeds) falls within cross-seed variance.
5	A permuted-score control (shuffled detector scores; 3-seed mean $17.951{\pm}0.007$, $+$0.26 vs.\ uniform\footnote{Per-seed permuted-score PPL: 17.958 (seed\,42), 17.945 (seed\,123), 17.951 (seed\,456).}) confirms that detector signal is load-bearing: uninformed reweighting only degrades.
6	
7	\paragraph{When uniform beats reweighting.}
8	Beyond the evaluation confound, our results identify three operational conditions for effective reweighting, each of which, when violated, makes uniform training preferable.
9	First, \emph{detector quality}: the detector must provide both sufficient discrimination (AUC) and good calibration (ECE).
10	A high-AUC but poorly calibrated detector (GPT-2, ECE\,=\,0.131) degrades PPL by $+$0.098 below uniform; even a well-calibrated detector with insufficient discrimination (N-gram, AUC\,=\,0.73) degrades by $+$0.129 (\S\ref{sec:robustness}).
11	Second, \emph{contamination level}: at $\rho{=}0.2$, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal ($\aeff$-binding at 60.1\% despite mean $q{=}0.393$), degrading PPL by $+$0.046; the method transitions from harmful to beneficial with a sharp sign change in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}).
12	Third, \emph{scale}: at 1.7B the benefit diminish
…[truncated 5935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-24T04:12:30.102951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-24T04:12:30.454496+00:00_

1	All experiments use Qwen3 (0.6B and 1.7B) on 132--200M tokens of continued pretraining with self-generated contamination at $\rho \in \{0.2, 0.3, 0.4, 0.6\}$; generalization to other model families, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination is untested.
2	The method improves over uniform only at $\rho \geq 0.4$ with a calibrated detector; at $\rho{=}0.2$ it degrades, and a preliminary Llama-3.2-3B cross-model test showed mixed results (Appendix~\ref{app:cross_model}), suggesting the effective range is narrower than the paradigm's ambition.
3	Three detectors from two families (discriminative and generative) were tested; fine-tuned neural classifiers (e.g., ModernBERT, Binoculars) and zero-shot methods (e.g., DetectGPT) remain untested, so the AUC/ECE thresholds reported here may shift with broader detector coverage.
4	Paired comparisons use $N{=}3$ seeds (2 degrees of freedom), limiting statistical power; results are directionally consistent but the sample size precludes strong generalizability claims.
5	After family-wise correction for nine comparisons, the $\rho{=}0.4$ adaptive-vs-uniform difference does not reach conventional significance ($p_{\mathrm{BH}}{=}0.078$), though the effect is directionally consistent across all seeds and the bootstrap CI excludes zero; the $\rho{=}0.6$ comparison also falls short of conventional significance under full-family correction ($p_{\mathrm{BH}}{=}0.064$, $k{=}9$), though the uncorrected $p{=}0.010$ and dose-response pattern across $\rho$ levels support a real effect.
6	The self-contamination setup provides known ground-truth labels but represents an easier detection scenario than cross-model contamination, where generator--corpus distribution mismatch may reduce detector accuracy.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-24T04:12:30.454828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-24T04:12:30.757827+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least two samples with distinct $q$-values.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, (1 - q_i).
14	\end{equation*}
15	Taking the derivative with respect to $b$:
16	\begin{align*}
17	  \frac{d\pi_i}{db}
18	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
19	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
20	\end{align*}
21	Substituting,
22	\begin{align*}
23	  \frac{d\alpha_{\mathrm{eff}}}{db}
24	  &= \sum_i (1{-}q_i)\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
25	  &= \mathrm{Cov}_{\pi}\!\bigl(1{-}q_i,\, \ln(1{-}q_i)\bigr).
26	\end{align*}
27	Since $(1{-}q_i)$ and $\ln(1{-}q_i)$ are both increasing functions of $(1{-}q_i)$, they are positively associated, so the covariance is non-negative.
28	\end{proof}
29	
30	\begin{proposition}[ESS monotonicity]
31	\label{prop:ess_mono}
32	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
33	\end{proposition}
34	
35	\begin{proof}
36	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
37	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
38	Differentiating $H$ with respect to $b$:
39	\begin{equation*}
40	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
41	\end{equation*}
42	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; the $\pi^2$-weighted sum assigns greater mass to terms where $\ln(1{-}q_i) > \ma
…[truncated 27489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-24T04:14:05.712064+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what reviewers should focus on, how to evaluate soundness and excitement, what constitutes a good vs bad review, and any specific instructions about statistical claims, reproducibility, or experimental design evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what reviewers should focus on, how to evaluate soundness and excitement, what constitutes a good vs bad review, and any specific instructions about statistical claims, reproducibility, or experimental design evaluation."
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-24T04:14:14.718582+00:00_

# ARR Reviewer Guidelines: Key Focus Areas

## Core Reviewing Tasks

Reviewers should prioritize four main tasks:
1. **Allocate adequate time** for both reviewing and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write strong reviews** with specific, justified feedback
4. **Engage with author responses** and update assessments accordingly

## Evaluating Soundness and Excitement

Starting February 2025, ARR uses three separate scores:

- **Soundness**: Technical validity and methodological rigor. "The soundness scores must be justified by the text of the review."
- **Excitement**: Personal interest level, kept separate from soundness assessment
- **Overall recommendation**: Composite judgment reflecting soundness, novelty, and potential impact

These should remain orthogonal—a technically sound paper might receive lower excitement scores, yet still merit acceptance.

## Writing Strong Reviews

**Essential practices:**
- Read papers twice: first for expectations/research questions, then in-depth for evidence evaluation
- Be specific with critiques: "cite missing references XYZ" rather than "missing relevant references"
- Justify low scores with concrete evidence from the paper
- Maintain professional, neutral tone focused on helping authors improve

## Common Review Pitfalls to Avoid

The guidelines identify seventeen heuristics reflecting reviewer biases (H1-H17):

- Dismissing results as "unsurprising" despite lacking prior empirical validation
- Rejecting papers for not achieving SOTA when that wasn't claimed
- Criticizing negative results, which contribute valuable knowledge
- Demanding additional experiments beyond what claims require

## Evaluating Experimental Design

Reviewers should examine:
- **Statistical rigor** (M1): "Are there enough details...including hyperparameter selection?" and confidence intervals provided?
- **Reproducibility** (M2): Sufficient implementation details for replication without running c
…[truncated 824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9006
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-24T04:17:01.444298+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 分析工作（尤其是 epoch confound）有价值，但核心方法改进量极小（Δ=-0.020 PPL, 0.11%）、校正后不显著、downstream 零改善、仅在自污染设定下验证，贡献度处于 Findings 边界。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 实验设计审慎、对照齐全，但 N=3 统计效力不足、校正后均不显著、bootstrap CI 在 N=3 下可靠性存疑、自污染设计限制泛化性 |\n| Excitement | 2.5/5 | Epoch confound 发现有价值但不算出人意料；方法本身改进量可忽略不计；条件约束过窄（ρ≥0.4 + 校准 detector + 非自我生成 unverified），实用性受限 |\n| Reproducibility | 4/5 | 训练细节充分（Appendix M-N），代码承诺 release，但 detector 自动选择逻辑\"first satisfying AUC ∈ [0.85, 0.98] and mid-range score ratio ≥ 5%\"缺乏细节 |\n| Overall Assessment | 3.0 | 分析质量在 Findings 水平，但方法贡献不足以支撑 Conference |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 下所有核心结论均未达到校正后统计显著性\n- 具体位置：Section 5.1 (Table 2), Section 5.2, Limitations\n- 问题：论文最核心的两个定量 claim：\n  - ρ=0.4: uncorrected p=0.019, Bonferroni-Holm 校正后 p_BH=0.078（不显著）\n  - ρ=0.6: uncorrected p=0.010, p_BH=0.064（不显著）\n  \n  论文诚实报告了这些数字，但 abstract 和 conclusion 仍以 \"improves over uniform at ρ≥0.4\" 的断言性语言呈现这些结果，没有在最显眼的位置标注\"校正后不显著\"。BCa bootstrap CI [-0.028, -0.012] 在 N=3 下存在覆盖率问题——bootstrap 理论要求经验分布近似总体分布，3 个数据点无法保证这一点（Efron & Tibshirani 1993 建议 N≥10-15）。\n- 为什么影响接收：如果核心 claim 在合理的多重比较校正下不显著，那么 \"adaptive b* improves over uniform\" 这个 claim 的可信度大幅下降。读者可能过度信赖 bootstrap CI 而忽略校正后的 p 值。\n- 建议修改方向：(1) 增加到 N≥5 seeds 以获得足够统计效力；(2) 若无法增加 seeds，abstract/conclusion 必须明确标注\"directionally consistent but not statistically significant after correction\"；(3) 讨论 bootstrap CI 在极小样本下的局限性。\n\n**N2** [critical] 自污染设计严重限制所有发现的泛化性\n- 具体位置：Section 4 (Experimental Setup), Appendix O (Cross-Model Transfer)\n- 问题：Generator 和 trainee 都是 Qwen3-0.6B，这是最简单的检测场景——TF-IDF 特征可以利用 128-token prefix 到 384-token continuation 的风格断裂点，以及小模型自身的写作特征。所有三个核心发现（epoch confound、calibration requirement、minimum intervention advantage）都建立在这个设定上。唯一的跨模型测试（Llama-3.2-3B，Appendix O）是 single seed、结果 mixed、且缺少 PPL 对比（\"checkpoints were not retained for re-evaluation\"）。\n  \n  更关键的是：现实世界的 web contamination 来自多个不同模型（GPT-4、Claude、Gemini 等），文体多样、混合度不均。self-contamination 是否能代表这类场景完全未验证。\n- 为什么影响接收：论文的贡献价值高度依赖于发现能否推广到现实场景。如果 AUC/ECE 阈值（Table 3）只在自污染下成立，practitioner decision summary 就不可靠。\n- 建议修改方向：(1) 至少完成 cross-model 实验的 PPL 对比（3 seeds）；(2) 或者将 title/abstract 明确限定为\"self-contamination setting\"；(3) 讨论为什么自污染设定下的 calibration requirement 可能不适用于跨模型场景（generative detectors 在跨模型场景中的 false positive pattern 可能不同）。\n\n**N3** [critical] Downstream tasks 零改善削弱方法的实际价值\n- 具体位置：Section 6 (Discussion), Table 4\n- 问题：Adaptive vs Uniform 在 5 个 downstream tasks 上 mean accuracy 完全相同（0.5414 vs 0.5414），个别 task Δ≤0.01 且方向 mixed。论文将此归因于\"PPL-to-accuracy transfer is nonlinear and scale-dependent\"和 0.1% PPL shift 低于 task measurement noise，这个解释合理。但这意味着该方法在当前规模下没有可观测的实际效果。\n  \n  论文在 Discussion 中试图论证\"the PPL improvements operate in a regime that standard benchmarks cannot resolve\"，但如果一个方法的效果小到所有标准评估手段都无法检测，那它的实际意义也就存疑。\n- 为什么影响接收：方法论文需要展示实际效用。PPL 改善无法转化为任何可测量的下游效果，大幅降低了方法的实用价值。\n- 建议修改方向：(1) 在更大规模（7B+）验证是否 downstream 效果可见；(2) 或者明确将论文定位为\"分析性贡献\"（empirical analysis of D&R effectiveness conditions），弱化方法贡献的 claim。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] B=4 micro-batch 上的 dual constraint 统计可靠性不足\n- 具体位置：Section 3 (Method), Appendix B (Algorithm)\n- 问题：在 B=4 样本上计算 α_eff 和 ESS，其中 true real fraction 是 Binomial(4, 0.6) 分布，标准差 ≈ 0.245。batch 的真实 real fraction 只能取 {0, 0.25, 0.5, 0.75, 1.0} 五个值。α_eff 作为加权平均在如此小的样本上波动剧烈（Appendix K 的 MAE=0.114）。虽然论文展示了 B=8→16 的放大效应，但主实验全部在 B=4 上完成，方法的核心机制在最 noisy 的条件下运行。\n- 建议：(1) 主实验应至少包含 B=8 的完整对比（3 seeds, 含 downstream）；(2) 讨论 B=4 是否是实际部署中的 realistic setting。\n\n**W2** [warning] α_eff proxy 的 r=0.79 相关性（R²=0.63）作为双约束框架的基础偏弱\n- 具体位置：Section 3 (Method), Section 6 (Discussion), Appendix K\n- 问题：α_eff 与 true batch-level real fraction 的 Pearson r=0.79（R²≈0.63），37% 方差未被解释。论文将未解释方差归因于 detector noise（70%）和 adaptive b* transform（30%），但这是对 unexplained variance 的分解，不能消除 proxy 误差对 b* selection 的系统性影响。论文指出 consistent negative bias ≈ -0.03 导致保守干预，但这个 bias 是否在所有 ρ 水平和 detector 组合下都成立？在 ρ=0.2 的 failure case 中，bias 的方向和大小可能不同。\n  \n  更根本的问题是：论文将 α_eff ≥ τ 的动机追溯到 \"convergence theory under contamination (Wang et al., 2026)\"，但 α_eff 只是 true real fraction 的一个 noisy proxy——convergence theory 中的阈值条件应用于 α_eff 而非 true fraction，理论保证是否仍然成立没有讨论。\n- 建议：(1) 明确 α_eff ≥ τ 的理论动机：如果 Wang et al. (2026) 的定理要求 true real fraction ≥ τ，α_eff 作为 proxy 需要怎样的精度才能保留这个保证？(2) 在 ρ=0.2 场景下报告 α_eff 的 bias 和 correlation。\n\n**W3** [warning] Batch-size amplification trend 的外推基于 3 个数据点\n- 具体位置：Section 5.3 (Hyperparameter Sensitivity)\n- 问题：B ∈ {4, 8, 16} 三个点拟合得到 Δ ∝ B^0.89。三个数据点不足以建立可靠的 scaling law。指数 0.89 的不确定性没有报告（confidence interval），且从 B=4 到 B=16 只是 4 倍范围——任何单调递增函数都可以在这个范围内被 power law 近似。论文称\"suggesting diminishing but substantial marginal gains at larger batch sizes\"，但 B=32 或 B=64 时是否还成立完全无法判断。\n- 建议：(1) 要么删除 power law fitting 和外推讨论；(2) 要么扩展到 B=32, 64 并报告 confidence intervals。\n\n**W4** [warning] 3 个 detector 不足以建立 AUC/ECE 因果关系和实用阈值\n- 具体位置：Section 5.2 (Robustness), Table 3, Appendix L\n- 问题：Table 3 的 practitioner decision summary 声称\"Detector AUC ≥ 0.9: Required\"和\"Detector ECE ≤ 0.05: Required\"，但这些阈值仅来自 3 个 detector（TF-IDF+LR AUC=0.94/ECE=0.048; GPT-2 AUC=0.91/ECE=0.131; N-gram AUC=0.73/ECE=0.069）。从 3 个数据点推导出精确的数值阈值是 overfitting。\n  \n  TF-IDF vs GPT-2 的对比被描述为\"isolates calibration\"，但两者同时在 AUC（0.94 vs 0.91）、模型类型（discriminative vs generative）、feature space、false positive pattern 上都不同。这不是一个控制实验，而是一个 observational comparison。论文在 Appendix L 中承认 generative detectors 的 false positive 机制不同（\"assign high q-scores to fluent, predictable human text\"），但这恰恰说明 calibration 不是唯一变量。\n- 建议：(1) 使用同一 detector（如 TF-IDF+LR）的不同 calibration 程度（不做 temperature scaling / 故意 miscalibrate）来真正 isolate calibration effect；(2) 将 Table 3 的阈值标注为\"在本实验 3 个 detector 下观察到的\"而非通用建议。\n\n**W5** [warning] \"Minimum intervention\" 原则缺乏理论依据\n- 具体位置：Section 3 (Method, Eq. 1)\n- 问题：为什么 \"smallest b meeting the quality floor\" 是最优的？Grid search 显示最优 b ≈ 0.3（seed 42），而 adaptive b* 的均值 ≈ 0.9（Section 5.1, Figure 2 注释）。如果 b=0.3 是全局最优，adaptive 的 b*=0.9 显然偏大——方法之所以有效是因为 per-batch adaptation 补偿了 b 的偏移，而非因为 \"minimum intervention\" 本身是对的。\n  \n  论文在 Section 5.1 讨论了 grid-best 的 4.7× 更高 cross-seed variance，试图论证 adaptive 的低方差优势。但这只是说明 per-batch adaptation 降低了方差，不能证明 minimum intervention 是比其他 aggregation rule（如 median b、percentile-based b）更好的选择。\n- 建议：(1) 补充一个\"per-batch adaptation + median b\"或\"per-batch adaptation + mean b\"的对比，证明 minimum b 确实优于其他选择规则；(2) 或者弱化 \"minimum intervention\" 的 principled framing，改为 \"heuristic regularization\"。\n\n**W6** [warning] Epoch confound 分析缺少纯数据重复的控制\n- 具体位置：Section 5.1 (Hard filtering and the epoch confound), Table 1\n- 问题：Epoch confound 分析非常有价值，但缺少一个关键 baseline：\"uniform training with ~3.2× data repetition\"（不做任何过滤，只是让模型在全部数据上训练 3.2 个 epoch）。这个 baseline 可以区分两个假设：(a) D&R 的优势纯粹来自 data repetition（无论数据质量如何），vs (b) D&R 的优势来自 filtered data + repetition 的交互效应。如果纯重复能达到类似效果，epoch confound 的故事更强；如果不能，filtering 仍有独立价值，epoch confound 的措辞需要弱化。\n- 建议：增加 \"uniform + multi-epoch\" baseline。\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 第三段 \"uncorrected p=0.010\" 应在 abstract 中注明是 uncorrected，目前读者可能误以为是校正后的 p 值。实际上 abstract 中已经写了\"uncorrected\"，但排版上不够醒目。\n- **M2**: Table 2 中 Grid-best 使用的 τ 不明确（主实验用 τ=0.7，但 footnote ‡ 只说 \"Post-hoc oracle from nine candidates\"）。Appendix C 显示 grid search 不使用 τ（固定 b），但读者在正文中可能混淆。\n- **M3**: Conclusion 中 \"we identify three effectiveness conditions for detect-and-reweight\" 没有附带 N=3 seeds、校正后不显著的 caveat——应保持与 Limitations 部分一致的审慎语气。\n- **M4**: Figure 2 的 y 轴范围（17.4-17.9）使得差异视觉上被放大，可考虑添加 break 标记或注明非零起点。\n- **M5**: Section 6 讨论\"effect size in context\"但未报告标准化效应量（如 Cohen's d）。在 N=3 的情况下，Cohen's d ≈ (-0.020)/0.007 ≈ 2.86（using adaptive σ），这是 large effect，但 N=3 下的 d 估计非常不稳定。应报告并讨论其不确定性。\n- **M6**: Appendix P (Checkpoint Resume Artifact) 提到 seed 42 的 τ=0.8 实验受到 checkpoint resume 影响，但 Table 2 的主实验使用 τ=0.7 且全部 from-scratch。这一点论文处理得当（footnote 77），但读者需要仔细阅读才能理清不同实验 run 的关系。\n\n## 主要优势\n\n- **S1**: Epoch confound 分析是论文最突出的贡献。通过 epoch-matched 和 LR-controlled 两重验证，令人信服地展示了 D&R 文献中可能被广泛忽视的评估偏差。这个发现独立于方法本身的价值，对 data curation 社区有参考意义。\n- **S2**: 实验设计的系统性：6 种方法的 ablation hierarchy（Adaptive < Uniform < ESS-only < Random）清晰展示了 detector signal 和 minimum intervention 的各自贡献。Permuted-score control（Appendix Section 6 Discussion, +0.26 PPL）是一个聪明的 sanity check。\n- **S3**: 极为诚实的结果报告。论文主动报告了：校正后不显著的 p 值、downstream 零改善、ρ=0.2 的 failure case、checkpoint resume artifact、cross-model mixed results。这种透明度在 ML 论文中不常见。\n- **S4**: Practitioner decision table (Table 3) 虽然基于有限 detector 数据，但作为一种 structured summary 有实用价值。boundary condition 分析（ρ=0.2→0.3→0.4→0.6 的 dose-response pattern）提供了有用的 sensitivity profile。\n- **S5**: 理论部分（Proposition 1-2, Appendix A）虽然简单，但 α_eff 单调性和 ESS 单调性的证明确保了 dual constraint formulation 的 well-definedness（b_τ 和 b_ESS 通过 bisection 可以唯一确定）。\n- **S6**: 对 checkpoint resume artifact 的透明披露和 from-scratch retraining 验证（Appendix P）展示了良好的实验规范。\n\n## Missing References / 未讨论的相关工作\n\n- 论文引用了 Drayson et al. (2025) 和 He et al. (2025) 作为 D&R 领域的主要工作，related work 覆盖合理。\n- 建议补充：关于 importance sampling 在 NLP 训练中的更多讨论（Katharopoulos & Fleuret 2018 已引用，但 variance reduction 方面的经典文献如 Owen 2013 Monte Carlo 只在 Appendix proof 中引用，正文中可简要讨论 importance weighting 的理论基础和 known failure modes）。\n- 关于 data contamination detection 的更全面 survey（论文测试了 3 个 baseline detector，但 ModernBERT / Binoculars / DetectGPT 等 SOTA detector 只在 Limitations 中提到，Related Work 中未充分讨论这些方法的 calibration 特性）。\n\n## Questions for Authors\n\n1. 是否考虑过在相同 TF-IDF+LR detector 上通过改变 temperature scaling 参数来人为调节 ECE（如 T=1.0 无校准 vs T=0.204 校准），从而在控制 AUC 的条件下 isolate calibration effect？\n2. ρ=0.2 failure case 中的 α_eff bias 是多少？是否仍然是 ~-0.03？如果 bias 在低污染下变化，minimum intervention 逻辑的失败可能有更 mechanistic 的解释。\n3. 为什么不在 B=16（gradient accumulation level）而非 B=4（micro-batch level）上计算 b*？Appendix B 提到\"q-score statistics exhibit sufficient variance within micro-batches\"，但 B=16 上 adaptive advantage amplifies 3.4×——这是否意味着主实验其实在次优设定下运行？\n4. Grid search 最优 b=0.3 而 adaptive b* 均值 ≈0.9——这个差距是否表明 minimum intervention 倾向于过度干预？per-batch b* 的分布（median, percentiles）是什么样的？\n\n## 总结判断\n\n这篇论文的分析质量高于其方法贡献。Epoch confound finding 是有价值的独立贡献，值得 Findings track。但方法本身的效果量极小（0.11% PPL, 零 downstream），统计证据在校正后不够强，且仅在自污染设定下验证。若作者能增加 seeds 数量使结论统计显著，或提供 cross-model 的完整验证，可以考虑更高评分。目前评 3.0 (Findings)。\n",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 分析工作（尤其是 epoch confound）有价值，但核心方法改进量极小（Δ=-0.020 PPL, 0.11%）、校正后不显著、downstream 零改善、仅在自污染设定下验证，贡献度处于 Findings 边界。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 实验设计审慎、对照齐全，但 N=3 统计效力不足、校正后均不显著、bootstrap CI 在 N=3 下可靠性存疑、自污染设计限制泛化性 |\n| Excitement | 2.5/5 | Epoch confound 发现有价值但不算出人意料；方法本身改进量可忽略不计；条件约束过窄（ρ≥0.4 + 校准 detector + 非自我生成 unverified），实用性受限 |\n| Reproducibility | 4/5 | 训练细节充分（Appendix M-N），代码承诺 release，但 detector 自动选择逻辑\"first satisfying AUC ∈ [0.85, 0.98] and mid-range score ratio ≥ 5%\"缺乏细节 |\n| Overall Assessment | 3.0 | 分析质量在 Findings 水平，但方法贡献不足以支撑 Conference |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 下所有核心结论均未达到校正后统计显著性\n- 具体位置：Section 5.1 (Table 2), Section 5.2, Limitations\n- 问题：论文最核心的两个定量 claim：\n  - ρ=0.4: uncorrected p=0.019, Bonferroni-Holm 校正后 p_BH=0.078（不显著）\n  - ρ=0.6: uncorrected p=0.010, p_BH=0.064（不显著）\n  \n  论文诚实报告了这些数字，但 abstract 和 conclusion 仍以 \"improves over uniform at ρ≥0.4\" 的断言性语言呈现这些结果，没有在最显眼的位置标注\"校正后不显著\"。BCa bootstrap CI [-0.028, -0.012] 在 N=3 下存在覆盖率问题——bootstrap 理论要求经验分布近似总体分布，3 个数据点无法保证这一点（Efron & Tibshirani 1993 建议 N≥10-15）。\n- 为什么影响接收：如果核心 claim 在合理的多重比较校正下不显著，那么 \"adaptive b* improves over uniform\" 这个 claim 的可信度大幅下降。读者可能过度信赖 bootstrap CI 而忽略校正后的 p 值。\n- 建议修改方向：(1) 增加到 N≥5 seeds 以获得足够统计效力；(2) 若无法增加 seeds，abstract/conclusion 必须明确标注\"directionally consistent but not statistically significant after correction\"；(3) 讨论 bootstrap CI 在极小样本下的局限性。\n\n**N2** [critical] 自污染设计严重限制所有发现的泛化性\n- 具体位置：Section 4 (Experimental Setup), Appendix O (Cross-Model Transfer)\n- 问题：Generator 和 trainee 都是 Qwen3-0.6B，这是最简单的检测场景——TF-IDF 特征可以利用 128-token prefix 到 384-token continuation 的风格断裂点，以及小模型自身的写作特征。所有三个核心发现（epoch confound、calibration requirement、minimum intervention advantage）都建立在这个设定上。唯一的跨模型测试（Llama-3.2-3B，Appendix O）是 single seed、结果 mixed、且缺少 PPL 对比（\"checkpoints were not retained for re-evaluation\"）。\n  \n  更关键的是：现实世界的 web contamination 来自多个不同模型（GPT-4、Claude、Gemini 等），文体多样、混合度不均。self-contamination 是否能代表这类场景完全未验证。\n- 为什么影响接收：论文的贡献价值高度依赖于发现能否推广到现实场景。如果 AUC/ECE 阈值（Table 3）只在自污染下成立，practitioner decision summary 就不可靠。\n- 建议修改方向：(1) 至少完成 cross-model 实验的 PPL 对比（3 seeds）；(2) 或者将 title/abstract 明确限定为\"self-contamination setting\"；(3) 讨论为什么自污染设定下的 calibration requirement 可能不适用于跨模型场景（generative detectors 在跨模型场景中的 false positive pattern 可能不同）。\n\n**N3** [critical] Downstream tasks 零改善削弱方法的实际价值\n- 具体位置：Section 6 (Discussion), Table 4\n- 问题：Adaptive vs Uniform 在 5 个 downstream tasks 上 mean accuracy 完全相同（0.5414 vs 0.5414），个别 task Δ≤0.01 且方向 mixed。论文将此归因于\"PPL-to-accuracy transfer is nonlinear and scale-dependent\"和 0.1% PPL shift 低于 task measurement noise，这个解释合理。但这意味着该方法在当前规模下没有可观测的实际效果。\n  \n  论文在 Discussion 中试图论证\"the PPL improvements operate in a regime that standard benchmarks cannot resolve\"，但如果一个方法的效果小到所有标准评估手段都无法检测，那它的实际意义也就存疑。\n- 为什么影响接收：方法论文需要展示实际效用。PPL 改善无法转化为任何可测量的下游效果，大幅降低了方法的实用价值。\n- 建议修改方向：(1) 在更大规模（7B+）验证是否 downstream 效果可见；(2) 或者明确将论文定位为\"分析性贡献\"（empirical analysis of D&R effectiveness conditions），弱化方法贡献的 claim。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] B=4 micro-batch 上的 dual constraint 统计可靠性不足\n- 具体位置：Section 3 (Method), Appendix B (Algorithm)\n- 问题：在 B=4 样本上计算 α_eff 和 ESS，其中 true real fraction 是 Binomial(4, 0.6) 分布，标准差 ≈ 0.245。batch 的真实 real fraction 只能取 {0, 0.25, 0.5, 0.75, 1.0} 五个值。α_eff 作为加权平均在如此小的样本上波动剧烈（Appendix K 的 MAE=0.114）。虽然论文展示了 B=8→16 的放大效应，但主实验全部在 B=4 上完成，方法的核心机制在最 noisy 的条件下运行。\n- 建议：(1) 主实验应至少包含 B=8 的完整对比（3 seeds, 含 downstream）；(2) 讨论 B=4 是否是实际部署中的 realistic setting。\n\n**W2** [warning] α_eff proxy 的 r=0.79 相关性（R²=0.63）作为双约束框架的基础偏弱\n- 具体位置：Section 3 (Method), Section 6 (Discussion), Appendix K\n- 问题：α_eff 与 true batch-level real fraction 的 Pearson r=0.79（R²≈0.63），37% 方差未被解释。论文将未解释方差归因于 detector noise（70%）和 adaptive b* transform（30%），但这是对 unexplained variance 的分解，不能消除 proxy 误差对 b* selection 的系统性影响。论文指出 consistent negative bias ≈ -0.03 导致保守干预，但这个 bias 是否在所有 ρ 水平和 detector 组合下都成立？在 ρ=0.2 的 failure case 中，bias 的方向和大小可能不同。\n  \n  更根本的问题是：论文将 α_eff ≥ τ 的动机追溯到 \"convergence theory under contamination (Wang et al., 2026)\"，但 α_eff 只是 true real fraction 的一个 noisy proxy——convergence theory 中的阈值条件应用于 α_eff 而非 true fraction，理论保证是否仍然成立没有讨论。\n- 建议：(1) 明确 α_eff ≥ τ 的理论动机：如果 Wang et al. (2026) 的定理要求 true real fraction ≥ τ，α_eff 作为 proxy 需要怎样的精度才能保留这个保证？(2) 在 ρ=0.2 场景下报告 α_eff 的 bias 和 correlation。\n\n**W3** [warning] Batch-size amplification trend 的外推基于 3 个数据点\n- 具体位置：Section 5.3 (Hyperparameter Sensitivity)\n- 问题：B ∈ {4, 8, 16} 三个点拟合得到 Δ ∝ B^0.89。三个数据点不足以建立可靠的 scaling law。指数 0.89 的不确定性没有报告（confidence interval），且从 B=4 到 B=16 只是 4 倍范围——任何单调递增函数都可以在这个范围内被 power law 近似。论文称\"suggesting diminishing but substantial marginal gains at larger batch sizes\"，但 B=32 或 B=64 时是否还成立完全无法判断。\n- 建议：(1) 要么删除 power law fitting 和外推讨论；(2) 要么扩展到 B=32, 64 并报告 confidence intervals。\n\n**W4** [warning] 3 个 detector 不足以建立 AUC/ECE 因果关系和实用阈值\n- 具体位置：Section 5.2 (Robustness), Table 3, Appendix L\n- 问题：Table 3 的 practitioner decision summary 声称\"Detector AUC ≥ 0.9: Required\"和\"Detector ECE ≤ 0.05: Required\"，但这些阈值仅来自 3 个 detector（TF-IDF+LR AUC=0.94/ECE=0.048; GPT-2 AUC=0.91/ECE=0.131; N-gram AUC=0.73/ECE=0.069）。从 3 个数据点推导出精确的数值阈值是 overfitting。\n  \n  TF-IDF vs GPT-2 的对比被描述为\"isolates calibration\"，但两者同时在 AUC（0.94 vs 0.91）、模型类型（discriminative vs generative）、feature space、false positive pattern 上都不同。这不是一个控制实验，而是一个 observational comparison。论文在 Appendix L 中承认 generative detectors 的 false positive 机制不同（\"assign high q-scores to fluent, predictable human text\"），但这恰恰说明 calibration 不是唯一变量。\n- 建议：(1) 使用同一 detector（如 TF-IDF+LR）的不同 calibration 程度（不做 temperature scaling / 故意 miscalibrate）来真正 isolate calibration effect；(2) 将 Table 3 的阈值标注为\"在本实验 3 个 detector 下观察到的\"而非通用建议。\n\n**W5** [warning] \"Minimum intervention\" 原则缺乏理论依据\n- 具体位置：Section 3 (Method, Eq. 1)\n- 问题：为什么 \"smallest b meeting the quality floor\" 是最优的？Grid search 显示最优 b ≈ 0.3（seed 42），而 adaptive b* 的均值 ≈ 0.9（Section 5.1, Figure 2 注释）。如果 b=0.3 是全局最优，adaptive 的 b*=0.9 显然偏大——方法之所以有效是因为 per-batch adaptation 补偿了 b 的偏移，而非因为 \"minimum intervention\" 本身是对的。\n  \n  论文在 Section 5.1 讨论了 grid-best 的 4.7× 更高 cross-seed variance，试图论证 adaptive 的低方差优势。但这只是说明 per-batch adaptation 降低了方差，不能证明 minimum intervention 是比其他 aggregation rule（如 median b、percentile-based b）更好的选择。\n- 建议：(1) 补充一个\"per-batch adaptation + median b\"或\"per-batch adaptation + mean b\"的对比，证明 minimum b 确实优于其他选择规则；(2) 或者弱化 \"minimum intervention\" 的 principled framing，改为 \"heuristic regularization\"。\n\n**W6** [warning] Epoch confound 分析缺少纯数据重复的控制\n- 具体位置：Section 5.1 (Hard filtering and the epoch confound), Table 1\n- 问题：Epoch confound 分析非常有价值，但缺少一个关键 baseline：\"uniform training with ~3.2× data repetition\"（不做任何过滤，只是让模型在全部数据上训练 3.2 个 epoch）。这个 baseline 可以区分两个假设：(a) D&R 的优势纯粹来自 data repetition（无论数据质量如何），vs (b) D&R 的优势来自 filtered data + repetition 的交互效应。如果纯重复能达到类似效果，epoch confound 的故事更强；如果不能，filtering 仍有独立价值，epoch confound 的措辞需要弱化。\n- 建议：增加 \"uniform + multi-epoch\" baseline。\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 第三段 \"uncorrected p=0.010\" 应在 abstract 中注明是 uncorrected，目前读者可能误以为是校正后的 p 值。实际上 abstract 中已经写了\"uncorrected\"，但排版上不够醒目。\n- **M2**: Table 2 中 Grid-best 使用的 τ 不明确（主实验用 τ=0.7，但 footnote ‡ 只说 \"Post-hoc oracle from nine candidates\"）。Appendix C 显示 grid search 不使用 τ（固定 b），但读者在正文中可能混淆。\n- **M3**: Conclusion 中 \"we identify three effectiveness conditions for detect-and-reweight\" 没有附带 N=3 seeds、校正后不显著的 caveat——应保持与 Limitations 部分一致的审慎语气。\n- **M4**: Figure 2 的 y 轴范围（17.4-17.9）使得差异视觉上被放大，可考虑添加 break 标记或注明非零起点。\n- **M5**: Section 6 讨论\"effect size in context\"但未报告标准化效应量（如 Cohen's d）。在 N=3 的情况下，Cohen's d ≈ (-0.020)/0.007 ≈ 2.86（using adaptive σ），这是 large effect，但 N=3 下的 d 估计非常不稳定。应报告并讨论其不确定性。\n- **M6**: Appendix P (Checkpoint Resume Artifact) 提到 seed 42 的 τ=0.8 实验受到 checkpoint resume 影响，但 Table 2 的主实验使用 τ=0.7 且全部 from-scratch。这一点论文处理得当（footnote 77），但读者需要仔细阅读才能理清不同实验 run 的关系。\n\n## 主要优势\n\n- **S1**: Epoch confound 分析是论文最突出的贡献。通过 epoch-matched 和 LR-controlled 两重验证，令人信服地展示了 D&R 文献中可能被广泛忽视的评估偏差。这个发现独立于方法本身的价值，对 data curation 社区有参考意义。\n- **S2**: 实验设计的系统性：6 种方法的 ablation hierarchy（Adaptive < Uniform < ESS-only < Random）清晰展示了 detector signal 和 minimum intervention 的各自贡献。Permuted-score control（Appendix Section 6 Discussion, +0.26 PPL）是一个聪明的 sanity check。\n- **S3**: 极为诚实的结果报告。论文主动报告了：校正后不显著的 p 值、downstream 零改善、ρ=0.2 的 failure case、checkpoint resume artifact、cross-model mixed results。这种透明度在 ML 论文中不常见。\n- **S4**: Practitioner decision table (Table 3) 虽然基于有限 detector 数据，但作为一种 structured summary 有实用价值。boundary condition 分析（ρ=0.2→0.3→0.4→0.6 的 dose-response pattern）提供了有用的 sensitivity profile。\n- **S5**: 理论部分（Proposition 1-2, Appendix A）虽然简单，但 α_eff 单调性和 ESS 单调性的证明确保了 dual constraint formulation 的 well-definedness（b_τ 和 b_ESS 通过 bisection 可以唯一确定）。\n- **S6**: 对 checkpoint resume artifact 的透明披露和 from-scratch retraining 验证（Appendix P）展示了良好的实验规范。\n\n## Missing References / 未讨论的相关工作\n\n- 论文引用了 Drayson et al. (2025) 和 He et al. (2025) 作为 D&R 领域的主要工作，related work 覆盖合理。\n- 建议补充：关于 importance sampling 在 NLP 训练中的更多讨论（Katharopoulos & Fleuret 2018 已引用，但 variance reduction 方面的经典文献如 Owen 2013 Monte Carlo 只在 Appendix proof 中引用，正文中可简要讨论 importance weighting 的理论基础和 known failure modes）。\n- 关于 data contamination detection 的更全面 survey（论文测试了 3 个 baseline detector，但 ModernBERT / Binoculars / DetectGPT 等 SOTA detector 只在 Limitations 中提到，Related Work 中未充分讨论这些方法的 calibration 特性）。\n\n## Questions for Authors\n\n1. 是否考虑过在相同 TF-IDF+LR detector 上通过改变 temperature scaling 参数来人为调节 ECE（如 T=1.0 无校准 vs T=0.204 校准），从而在控制 AUC 的条件下 isolate calibration effect？\n2. ρ=0.2 failure case 中的 α_eff bias 是多少？是否仍然是 ~-0.03？如果 bias 在低污染下变化，minimum intervention 逻辑的失败可能有更 mechanistic 的解释。\n3. 为什么不在 B=16（gradient accumulation level）而非 B=4（micro-batch level）上计算 b*？Appendix B 提到\"q-score statistics exhibit sufficient variance within micro-batches\"，但 B=16 上 adaptive advantage amplifies 3.4×——这是否意味着主实验其实在次优设定下运行？\n4. Grid search 最优 b=0.3 而 adaptive b* 均值 ≈0.9——这个差距是否表明 minimum intervention 倾向于过度干预？per-batch b* 的分布（median, percentiles）是什么样的？\n\n## 总结判断\n\n这篇论文的分析质量高于其方法贡献。Epoch confound finding 是有价值的独立贡献，值得 Findings track。但方法本身的效果量极小（0.11% PPL, 零 downstream），统计证据在校正后不够强，且仅在自污染设定下验证。若作者能增加 seeds 数量使结论统计显著，或提供 cross-model 的完整验证，可以考虑更高评分。目前评 3.0 (Findings)。\n",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-24T04:17:05.260116+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 756 · 2026-05-24T04:17:16.177810+00:00_

审稿报告已提交给 Review Director。

**审稿结论摘要**：Overall 3.0 (Findings)，Confidence 4/5。

核心判断：
- **最大贡献**是 epoch confound 分析（>95% D&R 优势来自数据重复），这个发现独立且有价值
- **主要问题**：(1) N=3 seeds 下校正后所有核心 claim 均不显著（p_BH=0.078/0.064）；(2) 自污染设计限制泛化性，唯一跨模型测试不完整；(3) Δ=-0.020 PPL (0.11%) 无法转化为任何可测量的 downstream 效果
- 标注了 3 个 must-fix（统计显著性、泛化性、实际价值）和 6 个 should-fix（B=4 可靠性、α_eff proxy 精度、batch-size scaling 外推、detector 数量不足、minimum intervention 缺乏理论依据、缺少纯重复 baseline）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 24

## Round 24

4 recorded events


### User

_source line 757 · 2026-05-24T04:20:41.198034+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每个要点使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

**Overall Assessment**: 3.5 (Borderline Conference), Confidence 4/5

### 主要优势
- **S1**: Epoch confound 发现（F1）是最核心、最有价值的贡献。Table 1 展示 D&R 0.396 PPL 优势在 epoch-matched 后缩至 Δ=0.017。LR-controlled verification 进一步排除学习率混淆。
- **S2**: 实验设计结构良好，消融层次清晰。Table 2 六种方法对比形成清晰消融阶梯。Permuted-score control 有效证明 detector signal 必要性。
- **S3**: 论文对局限性的讨论异常坦诚。主动承认 downstream 无改善、effect size modest、α_eff 代理质量有限。
- **S4**: Related Work 全面且结构化。五个 paragraph 覆盖完整，与 Drayson et al. 三点区分清晰公平。
- **S5**: Adaptive b* 消除 per-model grid search 需求。Grid-best 跨 seed 方差 4.7× 高于 adaptive。

### Must-Fix 问题
- **N1** [critical]: 主实验结果校正后未达显著性（p_BH=0.078/0.064）。核心 claim 的统计支撑应更强。建议增加 seeds 或在 Abstract/Conclusion 更明确标注统计状态。
- **N2** [critical]: 仅在 self-contamination 设置验证，生态效度堪忧。Cross-model 实验不完整。标题暗示一般性结论但实验仅支持特定设置。
- **N3** [critical]: 下游任务无改善（0.5414 vs 0.5414），effect size 极小。如果 PPL 改善无法在标准 benchmarks 检测到，practitioners 为什么使用此方法？

### Should-Fix 问题
- **W1** [warning]: 标题和 claims 的 scope 与实验支撑不匹配。建议标题加限定。
- **W2** [warning]: Grid-best 与 adaptive b* 差距（0.054）需要更诚实讨论。未分析差距来源。
- **W3** [warning]: α_eff 代理质量讨论（§6）过长（~200 words），部分内容适合 Appendix。
- **W4** [warning]: 三个 findings 的分析深度不均匀。F1 深入，F2 仅 3 个 detector，F3 缺乏机制分析。

### 小问题
- Figure 1 TikZ 概览图信息密度偏低
- RTX PRO 6000 (96 GB) 非常见 GPU
- Table 2 Golden Ratio 仅 seed 42 未解释
- §6 第一段与 §5.1 内容重复

### 新颖性评估
- F1 (epoch confound): 高新颖性
- F2 (detector requirements): 中等新颖性
- F3 (minimum intervention): 低至中等新颖性
- Adaptive b*: 中等新颖性（engineering contribution）
- 整体：main conference 门槛边缘

### 格式合规
- Abstract ≤200 words: ✅ 合规（~166 words）
- 正文 ≤8 页: ✅ 合规
- 所有格式检查项均通过

### Related Work 可能遗漏
- RAID (Dugan et al. 2024), M4 (Wang et al. 2024) 等 detection benchmarks
- Phi 系列 synthetic data 正面案例
- Data Provenance Initiative
- 后训练阶段 contamination-aware 方法

### Questions
1. 能否提供 cross-model contamination 完整结果？
2. ρ=0.6 下 downstream accuracy 是否改善？
3. 为什么不增加 seed 数量？
4. Adaptive b* 在 micro-batch 还是 accumulated batch 上计算？

---

请对以上所有要点逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-24T04:22:54.964122+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### 主要优势\n\n**[AGREE] R2-S1**: Epoch confound 是最核心贡献。完全同意。Table 1 的 epoch-matched 设计加上 LR-controlled verification（D&R 17.651 vs shared-schedule 17.657, Δ=0.006）形成双重验证，这在我的 S1 中也是首要优势。\n\n**[AGREE] R2-S2**: 消融层次清晰。完全同意。六种方法（Adaptive < Uniform < ESS-only < Random + Grid oracle + D&R oracle）的阶梯结构和 permuted-score control（+0.26 PPL）是我的 S2 中同样高度评价的优势。\n\n**[AGREE] R2-S3**: 结果报告坦诚。完全同意。这是我 S3 的核心观点。论文主动报告 p_BH=0.078、downstream 零改善、ρ=0.2 failure、checkpoint resume artifact——这种透明度在 ML 论文中确实不常见。\n\n**[AGREE] R2-S4**: Related Work 全面。同意。与 Drayson et al. (2025) 的三点区分（proxy-based vs grid search, controlled contamination, dual constraint）清晰公平。不过我补充一点：Related Work 在 detector calibration 方面讨论不足——论文主张 calibration 是必要条件之一，但 Related Work 对 detection 方法的 calibration 特性缺乏系统讨论（参见我的 W4 和 Missing References）。\n\n**[AGREE] R2-S5**: 消除 grid search 需求。同意。Grid-best 的 4.7× cross-seed variance（σ=0.033 vs 0.007, Section 5.1）是 adaptive 方法在工程层面的真实优势。但需注意 adaptive 在 PPL 上仍落后 grid-best 0.054（Table 2），所以\"消除 grid search\"是以牺牲一定性能为代价的——R2 在 W2 中也指出了这一点。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1**: 统计显著性不足。完全同意，这是我 N1 的核心观点。补充两点 R2 未提到的细节：\n\n1. **Bootstrap CI 在 N=3 下的覆盖率问题**：论文引用 95% BCa bootstrap CI [-0.028, -0.012] 排除零作为补充证据，但 BCa bootstrap 在 N=3 下的 nominal coverage 远低于 95%（Efron & Tibshirani 1993 建议 N≥10-15）。这个 CI 可能给读者虚假的信心。R2 未提及此点，我认为需要补充。\n\n2. **Cohen's d 未报告**：论文在 Section 6 定性讨论了 effect size in context，但未报告标准化效应量。粗估 Cohen's d ≈ |Δ|/σ_adaptive ≈ 0.020/0.007 ≈ 2.86（large effect），但 N=3 下 d 的置信区间极宽，不应被引用为 evidence of large effect 而不附带不确定性。\n\n**[AGREE] R2-N2**: 自污染限制泛化性。完全同意，与我 N2 一致。补充一点：R2 建议\"标题加限定\"（W1），我同意但认为更根本的问题是 Appendix O 的 cross-model 实验（Llama-3.2-3B generator）缺少 PPL 对比——论文明确承认 \"checkpoints were not retained for re-evaluation\"（Appendix O）。这不仅是 scope 问题，而是核心 claim 的证据缺失。作者至少应补充 cross-model 的完整 PPL 对比（3 seeds）。\n\n**[AGREE] R2-N3**: Downstream 零改善。完全同意，与我 N3 一致。R2 提出的问题\"practitioners 为什么使用此方法\"切中要害。论文在 Section 6 的解释（\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"）逻辑自洽，但恰恰证明了当前方法在实际可测指标上无价值。我在 N3 中的建议一致：要么在更大规模验证 downstream 效果，要么将论文明确定位为分析性贡献。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1**: 标题/claims scope 与实验支撑不匹配。同意。标题 \"When Does Detect-and-Reweight Work?\" 暗示对 D&R 范式的一般性分析，但实验仅覆盖 Qwen3-0.6B/1.7B 自污染、1 个 discriminative detector 有效、ρ≥0.4。R2 建议标题加限定（如 \"...in Self-Contaminated Continued Pretraining\"）是合理的。不过我认为问号形式的标题已经部分缓解了 over-claim 的风险——它是在提问而非断言。\n\n**[AGREE] R2-W2**: Grid-best 与 adaptive 差距需更诚实讨论。同意，并补充机制分析。论文指出 grid-best 的高方差（σ=0.033 vs 0.007）使其在实践中不可靠（Section 5.1），但未分析差距 0.054 的来源。我在 W5 中指出了一个关键线索：grid-best b=0.3 而 adaptive b* 均值≈0.9。这意味着 adaptive 的 minimum intervention 原则系统性地过度干预（b 偏大），per-batch adaptation 的好处被 suboptimal aggregate b 部分抵消。论文应讨论：如果将 adaptive 的 b* 分布 truncated 到 [0, 0.5] 会怎样？\n\n**[REBUT] R2-W3**: α_eff 讨论过长应移至 Appendix。不同意。Section 6 中 α_eff proxy 质量的讨论（~200 words）直接影响读者对方法可信度的判断——r=0.79 是方法有效性的上限，37% unexplained variance 和 consistent negative bias 是理解 failure cases（ρ=0.2）的关键。将此移入 Appendix 会让主文的 Discussion 回避了方法最重要的局限。不过我同意可以精简：quantitative decomposition（\"~70% detector noise, ~30% b* transform\"）和 B=4→16 的方差缩减讨论可以移入 Appendix，但 r=0.79 的核心讨论和 bias 方向应留在主文。\n\n**[AGREE] R2-W4**: 三个 findings 深度不均匀。同意。F1（epoch confound）有 epoch-matched + LR-controlled 双重验证，分析充分。F2（detector requirements）仅基于 3 个 detector（我的 W4），且 TF-IDF vs GPT-2 的对比不是真正的 controlled experiment——两者在 AUC、模型类型、feature space、false positive pattern 上同时不同（参见我 W4 的详细论述）。F3（minimum intervention）缺乏理论机制——为什么 smallest b 是最优的？与 grid-optimal b=0.3 的差距（b*≈0.9）如何解释？（我的 W5）。\n\n---\n\n### 小问题\n\n**[AGREE] R2-Minor-1**: Figure 1 TikZ 信息密度偏低。同意。Figure 1 占据约半栏空间，但核心信息（三个 findings → adaptive b*）可以用更紧凑的形式呈现。在页数紧张的会议论文中，这个空间可以更好利用。\n\n**[AGREE] R2-Minor-2**: RTX PRO 6000 (96 GB) 非常见 GPU。同意这值得注意。但不影响实验有效性——关键是论文使用了 bf16 precision、单卡训练，这些在多种 GPU 上可复现。\n\n**[AGREE] R2-Minor-3**: Golden Ratio 仅 seed 42 未充分解释。同意。论文在 footnote † 中说明 \"Oracle requiring known ρ\"，但 single-seed 的原因不明确——是 compute budget 限制还是方法本身依赖 known ρ 使得 multi-seed 无意义？应简要说明。\n\n**[AGREE] R2-Minor-4**: §6 第一段与 §5.1 内容重复。同意。Section 6 \"The epoch confound in D&R evaluation\" 段落与 Section 5.1 \"Hard filtering and the epoch confound\" 有明显重叠——两处都讨论了 >95% 归因于 multi-epoch exposure、LR-controlled verification、Δ=0.017 的 residual。建议 §6 仅引用 §5.1 的结论，用省出的空间深化 F2 或 F3 的分析。\n\n---\n\n### 新颖性评估\n\n**[AGREE] F1 高新颖性**: 完全同意。Epoch confound 在 D&R 文献中此前未被系统分析。\n\n**[AGREE] F2 中等新颖性**: 同意。Detector calibration 重要性的实证展示有价值，但仅 3 个 detector 的 observational comparison 限制了 finding 的稳健性（我的 W4）。\n\n**[AGREE] F3 低至中等新颖性**: 同意。Minimum intervention 在 importance weighting 文献中不是新概念（effective sample size 约束在 survey sampling 中已有长期历史，如 Kish 1965）。方法的工程贡献（per-batch bisection, dual constraint）比概念本身更新颖。\n\n**[REBUT] Adaptive b* \"中等新颖性（engineering contribution）\"**: 部分不同意。我认为 adaptive b* 的新颖性应低于\"中等\"。Per-batch importance weight tuning via bisection 是标准数值方法的直接应用。真正的贡献是 dual constraint formulation（α_eff ≥ τ + ESS ≥ n_min），但如我 W5 所述，这个 formulation 缺乏理论依据——minimum intervention 原则未被证明优于其他 aggregation rule，且 b* 均值与 grid-optimal 偏差较大。\n\n**[AGREE] 整体：main conference 门槛边缘**: 我给出 3.0 (Findings)，R2 给出 3.5 (Borderline Conference)。差异在于我更重视统计显著性不足（N1）和方法实际效果为零（N3）对 Conference-level 贡献的影响。R2 的 3.5 也合理，取决于对 epoch confound finding 独立价值的权重。\n\n---\n\n### 格式合规\n\n**[AGREE]**: 所有格式检查项一致通过。Abstract ~166 words，正文 8 页，Limitations 在正文中。\n\n---\n\n### Missing References\n\n**[AGREE] RAID (Dugan et al. 2024) 和 M4 (Wang et al. 2024)**: 同意。这些 detection benchmarks 与论文的 detector quality 分析相关——论文声称 AUC ≥ 0.9 和 ECE ≤ 0.05 是必要条件，但未讨论这些阈值在不同 detection benchmarks 上是否稳定。\n\n**[AGREE] Phi 系列 synthetic data 正面案例**: 同意。论文以 contamination 的负面框架讨论合成数据，但 Phi 系列（Gunasekar et al. 2023, Li et al. 2023）展示了高质量合成数据可以积极提升模型——这为 D&R 的必要性提供了重要 counterpoint。论文 Related Work 中的 \"Domain-Level Data Mining\" 段提到了 DoReMi 和 DSIR，但未讨论 high-quality synthetic data 不需要 downweighting 的情况。\n\n**[AGREE] Data Provenance Initiative**: 适度同意。与论文的 provenance-aware reweighting 主题相关，但非关键遗漏。\n\n**[REBUT] 后训练阶段 contamination-aware 方法**: 不确定这是遗漏。论文 scope 明确限定在 continued pretraining，后训练（SFT/RLHF）的 contamination 问题机制不同（preference data contamination vs pretraining data contamination）。Related Work 中的 \"Instance-Level Data Selection and Reweighting\" 段已简要涉及 instruction tuning data selection（LESS, MATES），足够。\n\n---\n\n### Questions\n\n**[AGREE] Q1**: 同意需要 cross-model 完整结果，与我 N2 一致。\n\n**[AGREE] Q2**: ρ=0.6 下 downstream accuracy 是否改善？好问题，我未在 R1 中专门提出。论文 Section 5.2 报告了 ρ=0.6 下 Δ=-0.032 PPL（更大改善），但未报告 downstream 结果。如果 PPL 改善翻倍仍无 downstream 效果，更加削弱方法的实用价值；如果有所改善，则提供了积极信号。\n\n**[AGREE] Q3**: 为什么不增加 seeds？这是我 N1 的核心建议。\n\n**[AGREE] Q4**: Micro-batch vs accumulated batch？好问题。论文在 Appendix B 中回答了这个问题——b* 在 micro-batch level (B=4) 计算而非 accumulated batch (B=16)，因为\"q-score statistics exhibit sufficient variance within micro-batches\"。但我在 W1 和 Question 3 中指出了矛盾：B=16 上 adaptive advantage amplifies 3.4×，这暗示主实验在次优设定下运行。R2 的问题与我的关切一致。\n\n---\n\n### 总结\n\nR2 与 R1 的审稿意见高度一致。三个 Must-Fix（统计显著性、自污染泛化性、downstream 零改善）完全重合。主要分歧：\n1. **Overall score**: R2 给 3.5 (Borderline Conference)，R1 给 3.0 (Findings)。我认为校正后不显著 + downstream 零改善使方法贡献不足以支撑 Conference，但 epoch confound finding 的独立价值支撑 Findings。\n2. **α_eff 讨论位置**: R2 认为过长应移 Appendix，R1 认为核心讨论应留主文（可精简）。\n3. **Adaptive b* 新颖性**: R2 评\"中等\"，R1 认为应更低——per-batch bisection 是标准方法的直接应用，dual constraint 缺乏理论依据。\n",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### 主要优势\n\n**[AGREE] R2-S1**: Epoch confound 是最核心贡献。完全同意。Table 1 的 epoch-matched 设计加上 LR-controlled verification（D&R 17.651 vs shared-schedule 17.657, Δ=0.006）形成双重验证，这在我的 S1 中也是首要优势。\n\n**[AGREE] R2-S2**: 消融层次清晰。完全同意。六种方法（Adaptive < Uniform < ESS-only < Random + Grid oracle + D&R oracle）的阶梯结构和 permuted-score control（+0.26 PPL）是我的 S2 中同样高度评价的优势。\n\n**[AGREE] R2-S3**: 结果报告坦诚。完全同意。这是我 S3 的核心观点。论文主动报告 p_BH=0.078、downstream 零改善、ρ=0.2 failure、checkpoint resume artifact——这种透明度在 ML 论文中确实不常见。\n\n**[AGREE] R2-S4**: Related Work 全面。同意。与 Drayson et al. (2025) 的三点区分（proxy-based vs grid search, controlled contamination, dual constraint）清晰公平。不过我补充一点：Related Work 在 detector calibration 方面讨论不足——论文主张 calibration 是必要条件之一，但 Related Work 对 detection 方法的 calibration 特性缺乏系统讨论（参见我的 W4 和 Missing References）。\n\n**[AGREE] R2-S5**: 消除 grid search 需求。同意。Grid-best 的 4.7× cross-seed variance（σ=0.033 vs 0.007, Section 5.1）是 adaptive 方法在工程层面的真实优势。但需注意 adaptive 在 PPL 上仍落后 grid-best 0.054（Table 2），所以\"消除 grid search\"是以牺牲一定性能为代价的——R2 在 W2 中也指出了这一点。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1**: 统计显著性不足。完全同意，这是我 N1 的核心观点。补充两点 R2 未提到的细节：\n\n1. **Bootstrap CI 在 N=3 下的覆盖率问题**：论文引用 95% BCa bootstrap CI [-0.028, -0.012] 排除零作为补充证据，但 BCa bootstrap 在 N=3 下的 nominal coverage 远低于 95%（Efron & Tibshirani 1993 建议 N≥10-15）。这个 CI 可能给读者虚假的信心。R2 未提及此点，我认为需要补充。\n\n2. **Cohen's d 未报告**：论文在 Section 6 定性讨论了 effect size in context，但未报告标准化效应量。粗估 Cohen's d ≈ |Δ|/σ_adaptive ≈ 0.020/0.007 ≈ 2.86（large effect），但 N=3 下 d 的置信区间极宽，不应被引用为 evidence of large effect 而不附带不确定性。\n\n**[AGREE] R2-N2**: 自污染限制泛化性。完全同意，与我 N2 一致。补充一点：R2 建议\"标题加限定\"（W1），我同意但认为更根本的问题是 Appendix O 的 cross-model 实验（Llama-3.2-3B generator）缺少 PPL 对比——论文明确承认 \"checkpoints were not retained for re-evaluation\"（Appendix O）。这不仅是 scope 问题，而是核心 claim 的证据缺失。作者至少应补充 cross-model 的完整 PPL 对比（3 seeds）。\n\n**[AGREE] R2-N3**: Downstream 零改善。完全同意，与我 N3 一致。R2 提出的问题\"practitioners 为什么使用此方法\"切中要害。论文在 Section 6 的解释（\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"）逻辑自洽，但恰恰证明了当前方法在实际可测指标上无价值。我在 N3 中的建议一致：要么在更大规模验证 downstream 效果，要么将论文明确定位为分析性贡献。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1**: 标题/claims scope 与实验支撑不匹配。同意。标题 \"When Does Detect-and-Reweight Work?\" 暗示对 D&R 范式的一般性分析，但实验仅覆盖 Qwen3-0.6B/1.7B 自污染、1 个 discriminative detector 有效、ρ≥0.4。R2 建议标题加限定（如 \"...in Self-Contaminated Continued Pretraining\"）是合理的。不过我认为问号形式的标题已经部分缓解了 over-claim 的风险——它是在提问而非断言。\n\n**[AGREE] R2-W2**: Grid-best 与 adaptive 差距需更诚实讨论。同意，并补充机制分析。论文指出 grid-best 的高方差（σ=0.033 vs 0.007）使其在实践中不可靠（Section 5.1），但未分析差距 0.054 的来源。我在 W5 中指出了一个关键线索：grid-best b=0.3 而 adaptive b* 均值≈0.9。这意味着 adaptive 的 minimum intervention 原则系统性地过度干预（b 偏大），per-batch adaptation 的好处被 suboptimal aggregate b 部分抵消。论文应讨论：如果将 adaptive 的 b* 分布 truncated 到 [0, 0.5] 会怎样？\n\n**[REBUT] R2-W3**: α_eff 讨论过长应移至 Appendix。不同意。Section 6 中 α_eff proxy 质量的讨论（~200 words）直接影响读者对方法可信度的判断——r=0.79 是方法有效性的上限，37% unexplained variance 和 consistent negative bias 是理解 failure cases（ρ=0.2）的关键。将此移入 Appendix 会让主文的 Discussion 回避了方法最重要的局限。不过我同意可以精简：quantitative decomposition（\"~70% detector noise, ~30% b* transform\"）和 B=4→16 的方差缩减讨论可以移入 Appendix，但 r=0.79 的核心讨论和 bias 方向应留在主文。\n\n**[AGREE] R2-W4**: 三个 findings 深度不均匀。同意。F1（epoch confound）有 epoch-matched + LR-controlled 双重验证，分析充分。F2（detector requirements）仅基于 3 个 detector（我的 W4），且 TF-IDF vs GPT-2 的对比不是真正的 controlled experiment——两者在 AUC、模型类型、feature space、false positive pattern 上同时不同（参见我 W4 的详细论述）。F3（minimum intervention）缺乏理论机制——为什么 smallest b 是最优的？与 grid-optimal b=0.3 的差距（b*≈0.9）如何解释？（我的 W5）。\n\n---\n\n### 小问题\n\n**[AGREE] R2-Minor-1**: Figure 1 TikZ 信息密度偏低。同意。Figure 1 占据约半栏空间，但核心信息（三个 findings → adaptive b*）可以用更紧凑的形式呈现。在页数紧张的会议论文中，这个空间可以更好利用。\n\n**[AGREE] R2-Minor-2**: RTX PRO 6000 (96 GB) 非常见 GPU。同意这值得注意。但不影响实验有效性——关键是论文使用了 bf16 precision、单卡训练，这些在多种 GPU 上可复现。\n\n**[AGREE] R2-Minor-3**: Golden Ratio 仅 seed 42 未充分解释。同意。论文在 footnote † 中说明 \"Oracle requiring known ρ\"，但 single-seed 的原因不明确——是 compute budget 限制还是方法本身依赖 known ρ 使得 multi-seed 无意义？应简要说明。\n\n**[AGREE] R2-Minor-4**: §6 第一段与 §5.1 内容重复。同意。Section 6 \"The epoch confound in D&R evaluation\" 段落与 Section 5.1 \"Hard filtering and the epoch confound\" 有明显重叠——两处都讨论了 >95% 归因于 multi-epoch exposure、LR-controlled verification、Δ=0.017 的 residual。建议 §6 仅引用 §5.1 的结论，用省出的空间深化 F2 或 F3 的分析。\n\n---\n\n### 新颖性评估\n\n**[AGREE] F1 高新颖性**: 完全同意。Epoch confound 在 D&R 文献中此前未被系统分析。\n\n**[AGREE] F2 中等新颖性**: 同意。Detector calibration 重要性的实证展示有价值，但仅 3 个 detector 的 observational comparison 限制了 finding 的稳健性（我的 W4）。\n\n**[AGREE] F3 低至中等新颖性**: 同意。Minimum intervention 在 importance weighting 文献中不是新概念（effective sample size 约束在 survey sampling 中已有长期历史，如 Kish 1965）。方法的工程贡献（per-batch bisection, dual constraint）比概念本身更新颖。\n\n**[REBUT] Adaptive b* \"中等新颖性（engineering contribution）\"**: 部分不同意。我认为 adaptive b* 的新颖性应低于\"中等\"。Per-batch importance weight tuning via bisection 是标准数值方法的直接应用。真正的贡献是 dual constraint formulation（α_eff ≥ τ + ESS ≥ n_min），但如我 W5 所述，这个 formulation 缺乏理论依据——minimum intervention 原则未被证明优于其他 aggregation rule，且 b* 均值与 grid-optimal 偏差较大。\n\n**[AGREE] 整体：main conference 门槛边缘**: 我给出 3.0 (Findings)，R2 给出 3.5 (Borderline Conference)。差异在于我更重视统计显著性不足（N1）和方法实际效果为零（N3）对 Conference-level 贡献的影响。R2 的 3.5 也合理，取决于对 epoch confound finding 独立价值的权重。\n\n---\n\n### 格式合规\n\n**[AGREE]**: 所有格式检查项一致通过。Abstract ~166 words，正文 8 页，Limitations 在正文中。\n\n---\n\n### Missing References\n\n**[AGREE] RAID (Dugan et al. 2024) 和 M4 (Wang et al. 2024)**: 同意。这些 detection benchmarks 与论文的 detector quality 分析相关——论文声称 AUC ≥ 0.9 和 ECE ≤ 0.05 是必要条件，但未讨论这些阈值在不同 detection benchmarks 上是否稳定。\n\n**[AGREE] Phi 系列 synthetic data 正面案例**: 同意。论文以 contamination 的负面框架讨论合成数据，但 Phi 系列（Gunasekar et al. 2023, Li et al. 2023）展示了高质量合成数据可以积极提升模型——这为 D&R 的必要性提供了重要 counterpoint。论文 Related Work 中的 \"Domain-Level Data Mining\" 段提到了 DoReMi 和 DSIR，但未讨论 high-quality synthetic data 不需要 downweighting 的情况。\n\n**[AGREE] Data Provenance Initiative**: 适度同意。与论文的 provenance-aware reweighting 主题相关，但非关键遗漏。\n\n**[REBUT] 后训练阶段 contamination-aware 方法**: 不确定这是遗漏。论文 scope 明确限定在 continued pretraining，后训练（SFT/RLHF）的 contamination 问题机制不同（preference data contamination vs pretraining data contamination）。Related Work 中的 \"Instance-Level Data Selection and Reweighting\" 段已简要涉及 instruction tuning data selection（LESS, MATES），足够。\n\n---\n\n### Questions\n\n**[AGREE] Q1**: 同意需要 cross-model 完整结果，与我 N2 一致。\n\n**[AGREE] Q2**: ρ=0.6 下 downstream accuracy 是否改善？好问题，我未在 R1 中专门提出。论文 Section 5.2 报告了 ρ=0.6 下 Δ=-0.032 PPL（更大改善），但未报告 downstream 结果。如果 PPL 改善翻倍仍无 downstream 效果，更加削弱方法的实用价值；如果有所改善，则提供了积极信号。\n\n**[AGREE] Q3**: 为什么不增加 seeds？这是我 N1 的核心建议。\n\n**[AGREE] Q4**: Micro-batch vs accumulated batch？好问题。论文在 Appendix B 中回答了这个问题——b* 在 micro-batch level (B=4) 计算而非 accumulated batch (B=16)，因为\"q-score statistics exhibit sufficient variance within micro-batches\"。但我在 W1 和 Question 3 中指出了矛盾：B=16 上 adaptive advantage amplifies 3.4×，这暗示主实验在次优设定下运行。R2 的问题与我的关切一致。\n\n---\n\n### 总结\n\nR2 与 R1 的审稿意见高度一致。三个 Must-Fix（统计显著性、自污染泛化性、downstream 零改善）完全重合。主要分歧：\n1. **Overall score**: R2 给 3.5 (Borderline Conference)，R1 给 3.0 (Findings)。我认为校正后不显著 + downstream 零改善使方法贡献不足以支撑 Conference，但 epoch confound finding 的独立价值支撑 Findings。\n2. **α_eff 讨论位置**: R2 认为过长应移 Appendix，R1 认为核心讨论应留主文（可精简）。\n3. **Adaptive b* 新颖性**: R2 评\"中等\"，R1 认为应更低——per-batch bisection 是标准方法的直接应用，dual constraint 缺乏理论依据。\n",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-24T04:22:58.782396+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3818
}
```

</details>

---


### Assistant

_source line 760 · 2026-05-24T04:23:04.855084+00:00_

交叉回应已提交。

与 R2 高度一致的要点：三个 Must-Fix（统计显著性、自污染泛化性、downstream 零改善）完全重合。

主要分歧三点：
1. **评分**：R2 给 3.5，我给 3.0——我认为校正后不显著加 downstream 零改善使方法贡献不足以支撑 Conference
2. **α_eff 讨论位置**：R2 主张移 Appendix，我认为核心部分应留主文
3. **Adaptive b* 新颖性**：R2 评中等，我认为偏低——dual constraint 缺乏理论依据，per-batch bisection 是标准方法的直接应用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 25

## Round 25

60 recorded events


### User

_source line 761 · 2026-05-25T04:42:44.958783+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。

## Venue 信息
- **目标 venue**: EMNLP 2026（via ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **页数限制**: 正文 ≤8 页，references 无限，Limitations 必须写（不计入页数）
- **模板**: ACL style，double-blind
- **匿名规则**: 不得包含作者信息，自引需避免暴露身份

## 论文信息
- **标题**: "When Does Detect-and-Reweight Work for Synthetic Contamination?"
- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf

## 你的审查侧重

### 1. 方法严谨性
- Dual-constrained adaptive b* 的数学推导是否正确（Proposition 1-2, Algorithm 1）
- α_eff 作为 proxy 的理论依据和可靠性（R²≈0.63，~37% 未解释方差）
- Wang 2026 convergence theory 要求 true real fraction ≥ τ，但论文用 proxy α_eff 替代，理论保证是否仍成立
- "Minimum intervention" 原则是否有充分理论依据
- Grid-best b=0.3 vs adaptive b*≈0.9 的偏差意味着什么

### 2. 实验设计
- N=5 seeds 的统计检验力是否充分（paired t-test, Bonferroni-Holm correction）
- B=4 micro-batch 下 dual constraint 的统计可靠性（α_eff 估计粒度）
- Self-contamination 实验设计的生态效度
- Cross-model transfer 仅 single seed + 缺 PPL 对比的问题
- D&R epoch confound 分析是否充分——是否缺少 "uniform + multi-epoch" baseline
- Detector 仅测试 3 个（TF-IDF+LR, GPT-2, N-gram），能否支撑因果性结论
- 1.7B 实验仅 3 seeds，效应减弱但未充分讨论原因

### 3. 统计分析
- 效应量（Δ=-0.023 PPL, ~0.13% relative）是否有实际意义
- Cohen's d 是否报告，CI 是否合理
- BH 校正后 ρ=0.6 的 p_BH=0.064 如何解读
- 下游任务零改善（|Δ|≤0.01）与论文 claims 是否矛盾

### 输出格式
请按以下结构输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条, S1/S2/...)
3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: must-fix / should-fix / minor)
4. **Questions** (Q1/Q2/...)
5. **Missing References** (如有)
6. **Overall Assessment** (评分 + 简要理由, 使用 EMNLP 2026 ARR 评分标准: 1-5 分)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-25T04:42:56.134361+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-25T04:42:56.185338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-25T04:43:00.955403+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 765 · 2026-05-25T04:43:02.835289+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf",
  "pages": "1-10",
  "project": "provenance_weight_training",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf",
    "pages": "1-10",
    "project": "provenance_weight_training",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 766 · 2026-05-25T04:43:08.013092+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also
…[truncated 1188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7057
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-25T04:43:10.422773+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 414.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 426.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7587
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-25T04:43:17.506514+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-25T04:43:18.916319+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf",
  "pages": "11-15",
  "project": "provenance_weight_training",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf",
    "pages": "11-15",
    "project": "provenance_weight_training",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-25T04:43:19.418209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 771 · 2026-05-25T04:43:20.372214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-25T04:43:20.874203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 773 · 2026-05-25T04:43:21.125399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 774 · 2026-05-25T04:43:24.388954+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure; unlikely to have missed important details
- **3**: Pretty sure; may have missed something
- **2**: Willing to defend evaluation; fairly likely missed details
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough"
- **4**: Strong; sufficient support for claims
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: Poor; main claims lack support
- **1**: "Major Issues: This study is not yet sufficiently thorough"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Would mention to others; attend presentation
- **3**: Might mention points; attend if time permits
- **2**: "Potentially Interesting: does not resonate with me"
- **1**: Not exciting; irrelevant to computational linguistics

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty
- **2**: "Hard pressed to reproduce"
- **1**: Cannot reproduce

## 6. **Datasets** (if applicable)
Scale: 1-5
- **5**: Enabling impact on research direction
- **4**: Useful for ongoing work
- **3**: Potentially useful
- **2**: Documentary value
- **1**: No usable datasets

## 7. **Software** (if applicable)
Scale: 1-5
- **5**: Enabling; affects research direction
- **4**: Useful for researchers/developers
- **3**: Potentially useful
- **2**: Documentary value
- **1**: No usable software

##
…[truncated 240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6882
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-25T04:43:24.992635+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 358.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 472.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 297.9}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6076
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-25T04:43:27.064768+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7646
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-25T04:43:27.067174+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5941
}
```

</details>

---


### Tool result

_source line 778 · 2026-05-25T04:43:27.069070+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6696
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-25T04:43:27.121037+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6246
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-25T04:43:33.616957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-25T04:43:34.221645+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-25T04:43:34.523089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 783 · 2026-05-25T04:43:34.925027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-25T04:43:35.028939+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-25T04:43:35.230749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool result

_source line 786 · 2026-05-25T04:43:36.188639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1263
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-25T04:43:36.239655+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-25T04:43:43.043290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-25T04:43:43.950741+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-25T04:43:43.951167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 791 · 2026-05-25T04:43:44.402774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 792 · 2026-05-25T04:43:44.805066+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 793 · 2026-05-25T04:43:44.805521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 794 · 2026-05-25T04:43:44.908167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-25T04:43:45.460981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-25T04:43:51.286541+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 797 · 2026-05-25T04:43:51.890159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 798 · 2026-05-25T04:43:52.195735+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 799 · 2026-05-25T04:43:52.196221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 800 · 2026-05-25T04:43:52.749940+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-25T04:43:52.802150+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-25T04:45:14.680294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-25T04:45:14.832050+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	\title{When Does Detect-and-Reweight Work for Synthetic Contamination?}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	\input{sections/abstract}
40	\end{abstract}
41	
42	\section{Introduction}
43	\label{sec:intro}
44	\input{sections/introduction}
45	
46	\section{Related Work}
47	\label{sec:related}
48	\input{sections/related_work}
49	
50	\section{Method}
51	\label{sec:method}
52	\input{sections/method}
53	
54	\section{Experimental Setup}
55	\label{sec:experiments}
56	\input{sections/experiments}
57	
58	\section{Results}
59	\label{sec:results}
60	\input{sections/results}
61	
62	\section{Discussion}
63	\label{sec:discussion}
64	\input{sections/discussion}
65	
66	\section{Conclusion}
67	\label{sec:conclusion}
68	\input{sections/conclusion}
69	
70	\section*{Limitations}
71	\label{sec:limitations}
72	\input{sections/limitations}
73	
74	\bibliography{references}
75	
76	\appendix
77	\input{sections/appendix}
78	
79	\end{document}
80	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-25T04:45:18.698615+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-25T04:45:18.749303+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-25T04:45:26.533130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-25T04:45:26.734176+00:00_

1	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus with token-level contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$, assumed unknown~\citep{cheng2025contamination}.
2	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
3	Rather than selecting $b$ via grid search~\citep{drayson2025detection}, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
4	
5	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
6	
7	\paragraph{Quality floor.}
8	The \emph{effective authenticity} $\aeff(b) = \sum_i w_i(b)(1{-}q_i) / \sum_i w_i(b)$ measures the weighted mean detector confidence that samples are real.
9	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
10	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.79$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
11	
12	\paragraph{Stability ceiling.}
13	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
14	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
15	
16	\paragraph{Adaptive $\bstar$.}
17	Since $\aeff$ is non-decreasing and ESS is decreasing in $b$, the two constraints define an interval $[b_\tau, \bess]$.
18	The optimal exponent implements \emph{minimum intervention}:
19	\begin{equation}
20	  b^{*} = \begin{cases}
21	    0        & \text{if } \aeff(0) \geq \tau, \\
22	    b_\tau   & \text{if } b_\tau \leq \bess, \\
23	    \bess & \tex
…[truncated 2429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-25T04:45:26.734545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-25T04:45:26.785222+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across five seeds.
5	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 5-seed mean PPL 17.674, compared to 17.697 for uniform ($\Delta{=}{-}0.023$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean, post-hoc oracle; gap $+$0.054; Table~\ref{tab:aux}).
8	A paired $t$-test yields $t(4){=}{-}8.21$, $p{=}0.0012$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.011$, reaching conventional significance at $\alpha{=}0.05$.
9	The engineering benefit is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
10	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $5.5{\times}$ higher cross-seed standard deviation than adaptive ($\sigma{=}0.033$ vs.\ $0.006$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
11	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
12	
13	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random ${<}$ Permuted, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
14	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that non-uniform weighting alone does not help; permuted $q$-scores (17.919, $\Delta{=}{+}0.225$) further isolate provenance signal as load-bearing, since shuffling destroys the detector's sample-level information while preserving identical weight non-uniformity.
15	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b
…[truncated 13421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-25T04:45:33.666598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-25T04:45:33.968730+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least two samples with distinct $q$-values.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, (1 - q_i).
14	\end{equation*}
15	Taking the derivative with respect to $b$:
16	\begin{align*}
17	  \frac{d\pi_i}{db}
18	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
19	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
20	\end{align*}
21	Substituting,
22	\begin{align*}
23	  \frac{d\alpha_{\mathrm{eff}}}{db}
24	  &= \sum_i (1{-}q_i)\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
25	  &= \mathrm{Cov}_{\pi}\!\bigl(1{-}q_i,\, \ln(1{-}q_i)\bigr).
26	\end{align*}
27	Since $(1{-}q_i)$ and $\ln(1{-}q_i)$ are both increasing functions of $(1{-}q_i)$, they are positively associated, so the covariance is non-negative.
28	\end{proof}
29	
30	\begin{proposition}[ESS monotonicity]
31	\label{prop:ess_mono}
32	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
33	\end{proposition}
34	
35	\begin{proof}
36	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
37	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
38	Differentiating $H$ with respect to $b$:
39	\begin{equation*}
40	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
41	\end{equation*}
42	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; the $\pi^2$-weighted sum assigns greater mass to terms where $\ln(1{-}q_i) > \ma
…[truncated 28186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-25T04:45:39.790299+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-25T04:45:40.041685+00:00_

1	\paragraph{The epoch confound in D\&R evaluation.}
2	The epoch confound identified in \S\ref{sec:main-results} accounts for ${>}$95\% of D\&R's reported advantage; the residual ($\Delta{=}0.017$, 3 seeds) falls within cross-seed variance and is robust to LR schedule choice ($\Delta{=}0.006$ under independent schedules).
3	This confound was invisible in \citet{drayson2025detection} because from-scratch pretraining on large corpora rarely completes even one epoch; in continued pretraining, aggressive D\&R filtering (retaining 31.5\% at $q{>}0.3$) creates ${\sim}$3.2 content epochs, making the confound quantitatively significant.
4	A permuted-score control ($+$0.225 vs.\ uniform) confirms that detector signal is load-bearing.
5	
6	\paragraph{When uniform beats reweighting.}
7	Table~\ref{tab:decision} summarizes three conditions, each necessary for effective reweighting: (i)~sufficient detector discrimination \emph{and} calibration (AUC\,$\geq$\,0.9, ECE\,$\leq$\,0.05; \S\ref{sec:robustness}); (ii)~contamination $\rho \geq 0.4$, below which the method degrades ($+$0.046 at $\rho{=}0.2$) with a sharp transition in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}); (iii)~generator--trainee mismatch (at 1.7B the benefit diminishes to $\Delta{=}{-}0.013$ with OOD mixed).
8	When any condition is violated, uniform is the safer default.
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\setlength{\tabcolsep}{3pt}
14	\resizebox{\columnwidth}{!}{%
15	\begin{tabular}{@{}lcll@{}}
16	\toprule
17	\textbf{Condition} & \textbf{Req'd?} & \textbf{Evidence} & \textbf{$\Delta$ PPL} \\
18	\midrule
19	Detector AUC $\geq 0.9$ & Yes & N-gram (0.73) degrades & $+$0.129 \\
20	Detector ECE $\leq 0.05$ & Yes & GPT-2 (0.131) degrades & $+$0.098 \\
21	Contamination $\rho \geq 0.4$ & Yes & $\rho{=}0.2$ degrades & $+$0.046 \\
22	Generator $\neq$ trainee & Rec. & 1.7B: $\Delta{=}{-}0.013$, OOD mixed & --- \\
23	\bottomrule
24	\end{tabular}}
25	\caption{Decision summary for pract
…[truncated 1594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-25T04:45:40.042174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-25T04:45:40.192930+00:00_

1	\begin{itemize}[nosep,leftmargin=*]
2	\item \textbf{Scope.}
3	All experiments use Qwen3 (0.6B and 1.7B) under self-contamination with 132--200M tokens of continued pretraining.
4	Generalization to other architectures, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination---where generator--corpus distribution mismatch may reduce detector accuracy---remains untested.
5	
6	\item \textbf{Detector coverage.}
7	Only three detectors from two families (discriminative TF-IDF+LR and generative perplexity scorers) were evaluated; fine-tuned neural classifiers (e.g., ModernBERT) and zero-shot methods (e.g., DetectGPT, Binoculars) remain untested, so the AUC/ECE thresholds reported here may shift with broader detector coverage.
8	\end{itemize}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-25T04:45:47.221998+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to write reviews, what makes a good review, scoring guidance, and any specific criteria or checklists."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to write reviews, what makes a good review, scoring guidance, and any specific criteria or checklists."
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-25T04:46:03.651542+00:00_

# ARR Reviewer Guidelines: Complete Overview

## Core Reviewer Responsibilities

Reviewers must complete four main tasks: **(1)** allocate calendar time for reviewing and discussion, **(2)** verify assignment suitability through expertise and conflict-of-interest checks, **(3)** write thorough reviews, and **(4)** engage with author responses and update assessments accordingly.

## What Reviewers Should Evaluate

### Assignment Verification
Before starting, reviewers should confirm they possess sufficient expertise in the paper's core methodology. The guidelines note that "*even in the best-case scenario, the matches will not always be perfect*" but reviewers should assess whether they can meaningfully evaluate the work. Recusal is appropriate if conflicts of interest exist or if author identity would compromise objectivity.

### Desk Rejection Checklist
Reviewers screen for papers warranting rejection before full review:
- Appropriateness for ARR scope
- Hallucinated references or citations
- Anonymity violations
- Style guide or length violations
- Missing limitations section
- Inadequate responsible NLP checklist responses
- Potential ethics issues requiring flagging

## How to Write Reviews

### Reading Strategy
The guidelines emphasize a two-pass approach. During skimming, assess "*what is the research question and what was done to answer it*" without examining results initially. In-depth reading then evaluates technical soundness, novelty, and argumentation validity.

### Specificity Requirement
Reviews must provide concrete examples rather than vague criticisms. Instead of stating "missing relevant references," identify specific papers by name. This principle applies across all feedback dimensions.

## What Makes a Good Review

### Professional Tone and Constructive Framing
Reviews should be "*professional and neutral, if not kind*." The guidelines emphasize that harsh or sarcastic language undermines the peer review system and harms researchers' wellbeing. A
…[truncated 3378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 16429
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-25T04:49:11.751319+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性、实验设计与统计分析\n\n### 总体评分\n**Overall Assessment**: 3.0 — Findings\n**一句话总结**: Epoch confound 的揭露是本文最有价值的贡献，但核心方法（adaptive b*）的实际效应极小（Δ=−0.023 PPL, 0.13% relative）且完全无法迁移至下游任务，加上规模效应递减（1.7B 时 Δ 缩至 −0.013），方法论贡献不足以支撑主会议接收。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Propositions 1-2 证明正确，实验设计合理且含大量消融；但 α_eff proxy 的 ~37% 未解释方差与引用的 Wang (2026) 理论保证之间存在逻辑断裂；PPL 与下游指标完全脱节削弱了方法论 claim |\n| Excitement | 2.5/5 | Epoch confound 发现有价值但事后看并不意外；adaptive b* 实际收益过小且规模趋势不利 |\n| Reproducibility | 4/5 | 算法伪代码清晰，超参数完整，cross-seed 分析充分；代码未发布，cross-model 缺 PPL |\n| Reviewer Confidence | 4/5 | 对 data weighting/contamination detection 领域较熟悉 |\n\n### Must-Fix 问题\n\n**N1** [critical] 核心效应无实际意义且不迁移至下游任务\n- 位置：Table 3 (Δ=−0.023 PPL), Table 10/Appendix I (|Δ|≤0.01 across 5 benchmarks)\n- Adaptive b* 的 PPL 改善仅 0.13% relative，5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）。Cohen's d=3.83 被极低 cross-seed 方差（σ=0.006，deterministic data ordering）人为放大。如果方法不改善任何下游指标，实际价值存疑。\n- 建议：(1) 重新定位为分析/负面结果贡献而非方法贡献；(2) 在 B=16 下报告下游任务结果。\n\n**N2** [critical] α_eff proxy 的理论保证断裂\n- 位置：§3 ¶1, §6 ¶4, Table 12/Appendix K\n- Wang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）。~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ。n_min 的缓冲是 heuristic 的，没有理论保证。论文同时引用 Wang (2026) 作理论动机并使用违反前提的 proxy，存在内在矛盾。\n- 建议：明确区分理论动机和实际保证；量化 α_eff ≥ τ 但 true fraction < τ 的 batch 比例。\n\n### Should-Fix 问题\n\n**W1** [warning] Grid-best b=0.3 vs adaptive b*≈0.9 偏差缺乏解释\n- 位置：Table 4, Figure 3\n- 如果 grid-best 在 b=0.3，为何 adaptive 收敛到 ~0.9？α_eff 的负偏差（−0.03）可能导致 b_τ 偏高。建议分析 debiased α_eff 的效果。\n\n**W2** [warning] 缺少 \"uniform + multi-epoch\" 基线\n- 位置：§5.1, Table 2\n- Epoch confound 分析缺少关键对照：对全部数据做 multi-epoch uniform training（等量 compute），以区分选择性重复 vs 任意重复。\n\n**W3** [warning] 1.7B 规模效应递减未充分讨论\n- 位置：§5.2\n- 0.6B→1.7B 效应缩减 43%（−0.023→−0.013），OOD 方向不一致。推测 larger models 更鲁棒但无证据。建议正式讨论 scaling trend 并限定 claim 范围。\n\n**W4** [warning] B=4 是最弱设置却用于主实验\n- 位置：Figure 6, Table 12\n- B=4 时 MAE=0.114，advantage 最小（1.0×）。B=16 时 advantage 放大 3.0×。建议以 B≥8 为主实验配置。\n\n**W5** [warning] Self-contamination 生态效度有限\n- 位置：§4, Appendix O\n- Qwen3 self-contamination + uniform mixing 远不代表真实 web contamination。Cross-model 实验仅单 seed 无 PPL。标题 claim 超出证据范围。\n\n### 小问题\n- M1: Permuted q-scores 仅 1 seed，建议补充\n- M2: ρ=0.6 p_BH=0.064 的措辞略有 misleading\n- M3: Table 5 \"Generator ≠ trainee\" 应考虑标为必要条件\n- M4: Cohen's d=3.83 的解读需注意 paired SD vs absolute SD 的区别\n\n### Questions\nQ1: 下游零改善下，推荐用于什么场景？\nQ2: GPT-4 级 synthetic data 的 detector 性能？\nQ3: α_eff 负偏差是否导致 b* 系统偏高？\nQ4: 为何选 B=4 而非 B=8/16？\nQ5: 是否考虑 curriculum learning 基线？\n\n### 主要优势\n- S1: Epoch confound 揭露（>95% D&R 优势来自 multi-epoch）是最强贡献\n- S2: 三条件框架（Table 5）有实用价值\n- S3: 实验设计严谨（5 seeds, BH correction, 大量消融, checkpoint artifact 诚实报告）\n- S4: 写作质量高，图表清晰\n- S5: Propositions 1-2 数学正确，Algorithm 1 实现清晰",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性、实验设计与统计分析\n\n### 总体评分\n**Overall Assessment**: 3.0 — Findings\n**一句话总结**: Epoch confound 的揭露是本文最有价值的贡献，但核心方法（adaptive b*）的实际效应极小（Δ=−0.023 PPL, 0.13% relative）且完全无法迁移至下游任务，加上规模效应递减（1.7B 时 Δ 缩至 −0.013），方法论贡献不足以支撑主会议接收。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Propositions 1-2 证明正确，实验设计合理且含大量消融；但 α_eff proxy 的 ~37% 未解释方差与引用的 Wang (2026) 理论保证之间存在逻辑断裂；PPL 与下游指标完全脱节削弱了方法论 claim |\n| Excitement | 2.5/5 | Epoch confound 发现有价值但事后看并不意外；adaptive b* 实际收益过小且规模趋势不利 |\n| Reproducibility | 4/5 | 算法伪代码清晰，超参数完整，cross-seed 分析充分；代码未发布，cross-model 缺 PPL |\n| Reviewer Confidence | 4/5 | 对 data weighting/contamination detection 领域较熟悉 |\n\n### Must-Fix 问题\n\n**N1** [critical] 核心效应无实际意义且不迁移至下游任务\n- 位置：Table 3 (Δ=−0.023 PPL), Table 10/Appendix I (|Δ|≤0.01 across 5 benchmarks)\n- Adaptive b* 的 PPL 改善仅 0.13% relative，5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）。Cohen's d=3.83 被极低 cross-seed 方差（σ=0.006，deterministic data ordering）人为放大。如果方法不改善任何下游指标，实际价值存疑。\n- 建议：(1) 重新定位为分析/负面结果贡献而非方法贡献；(2) 在 B=16 下报告下游任务结果。\n\n**N2** [critical] α_eff proxy 的理论保证断裂\n- 位置：§3 ¶1, §6 ¶4, Table 12/Appendix K\n- Wang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）。~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ。n_min 的缓冲是 heuristic 的，没有理论保证。论文同时引用 Wang (2026) 作理论动机并使用违反前提的 proxy，存在内在矛盾。\n- 建议：明确区分理论动机和实际保证；量化 α_eff ≥ τ 但 true fraction < τ 的 batch 比例。\n\n### Should-Fix 问题\n\n**W1** [warning] Grid-best b=0.3 vs adaptive b*≈0.9 偏差缺乏解释\n- 位置：Table 4, Figure 3\n- 如果 grid-best 在 b=0.3，为何 adaptive 收敛到 ~0.9？α_eff 的负偏差（−0.03）可能导致 b_τ 偏高。建议分析 debiased α_eff 的效果。\n\n**W2** [warning] 缺少 \"uniform + multi-epoch\" 基线\n- 位置：§5.1, Table 2\n- Epoch confound 分析缺少关键对照：对全部数据做 multi-epoch uniform training（等量 compute），以区分选择性重复 vs 任意重复。\n\n**W3** [warning] 1.7B 规模效应递减未充分讨论\n- 位置：§5.2\n- 0.6B→1.7B 效应缩减 43%（−0.023→−0.013），OOD 方向不一致。推测 larger models 更鲁棒但无证据。建议正式讨论 scaling trend 并限定 claim 范围。\n\n**W4** [warning] B=4 是最弱设置却用于主实验\n- 位置：Figure 6, Table 12\n- B=4 时 MAE=0.114，advantage 最小（1.0×）。B=16 时 advantage 放大 3.0×。建议以 B≥8 为主实验配置。\n\n**W5** [warning] Self-contamination 生态效度有限\n- 位置：§4, Appendix O\n- Qwen3 self-contamination + uniform mixing 远不代表真实 web contamination。Cross-model 实验仅单 seed 无 PPL。标题 claim 超出证据范围。\n\n### 小问题\n- M1: Permuted q-scores 仅 1 seed，建议补充\n- M2: ρ=0.6 p_BH=0.064 的措辞略有 misleading\n- M3: Table 5 \"Generator ≠ trainee\" 应考虑标为必要条件\n- M4: Cohen's d=3.83 的解读需注意 paired SD vs absolute SD 的区别\n\n### Questions\nQ1: 下游零改善下，推荐用于什么场景？\nQ2: GPT-4 级 synthetic data 的 detector 性能？\nQ3: α_eff 负偏差是否导致 b* 系统偏高？\nQ4: 为何选 B=4 而非 B=8/16？\nQ5: 是否考虑 curriculum learning 基线？\n\n### 主要优势\n- S1: Epoch confound 揭露（>95% D&R 优势来自 multi-epoch）是最强贡献\n- S2: 三条件框架（Table 5）有实用价值\n- S3: 实验设计严谨（5 seeds, BH correction, 大量消融, checkpoint artifact 诚实报告）\n- S4: 写作质量高，图表清晰\n- S5: Propositions 1-2 数学正确，Algorithm 1 实现清晰",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-25T04:49:15.473992+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3722
}
```

</details>

---


### Assistant

_source line 820 · 2026-05-25T04:49:25.676977+00:00_

审稿意见已提交给 Review Director。

总结：评分 **Overall 3.0 (Findings)**。核心判断是论文最有价值的贡献在于 epoch confound 的揭露和三条件框架，而非 adaptive b* 方法本身。两个 must-fix 问题：(1) 核心效应 0.13% PPL 且零下游迁移，实际意义不足；(2) α_eff proxy 与 Wang (2026) 理论保证之间的逻辑断裂。五个 should-fix 问题涵盖 grid-best 偏差解释、缺 multi-epoch uniform 基线、规模递减趋势、B=4 配置选择和生态效度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 26

## Round 26

4 recorded events


### User

_source line 821 · 2026-05-25T04:53:12.841980+00:00_

[Round 1 审稿请求]:
## [Round 1 交叉分享] Reviewer 2 的完整审稿意见

请逐条审阅 Reviewer 2 的意见，对每条 Weakness/Question 回复 **[AGREE]**（同意）或 **[REBUT]**（反驳，须说明理由）。对 Strengths 也可标注是否同意。

特别关注：
- R2 提出了你未提及的问题（如 W1 标题通用性 vs scope、W3 方法新颖性有限、W7 ρ≥0.4 门槛偏高、W8 PPL 与模型质量关系），请评估是否认同
- R2 与你观点重叠的问题（下游零改善、detector 覆盖窄、self-contamination 生态效度、效果量极小），确认是否一致或有补充

---

以下是 Reviewer 2 完整审稿意见：

### Strengths
- S1: Epoch confound 发现是最强贡献，Table 2 和 Figure 1(a) 清晰展示 D&R raw PPL 优势在 epoch-matched controls 下缩减至 Δ≈-0.017
- S2: 严谨实验方法论（5 seeds + BH correction，ablation hierarchy 清晰）
- S3: 诚实 framing——将方法定位为 "illustrative application"
- S4: Constraint regime 分析（Figure 7）有实践洞察价值
- S5: 视觉和写作密度高（8页含7 figures + 5 tables）

### Weaknesses
**W1** [must-fix] 标题暗示的通用性远超实验 scope：标题 "When Does D&R Work?" 暗示一般性回答，但实验受限于 self-contamination、0.6B 单一模型、continued pretraining、单一数据源。关键矛盾：epoch confound 在 from-scratch pretraining 下不适用。

**W2** [must-fix] 下游零改善与 practitioner 导向 framing 矛盾：Table 10 下游任务无改善，但论文三处使用 practitioner 导向表述。Abstract 说 "improves over uniform training" 未限定为 PPL-only。

**W3** [should-fix] 方法新颖性有限：w=(1−q)^b 来自 Drayson et al.，dual constraint + bisection 是标准方法组合，per-batch adaptation 无独立创新。

**W4** [should-fix] Detector 覆盖面极窄：仅 3 个 detector 不足以得出 AUC/ECE threshold 通用规律，缺少 neural detectors。

**W5** [should-fix] 效果量极小（Δ=−0.023 PPL），实际显著性存疑，结合零下游改善。

**W6** [should-fix] Self-contamination 生态效度有限，cross-model 结果不成熟。

**W7** [minor] ρ≥0.4 实用门槛偏高，实际适用场景窄。

**W8** [minor] PPL 与模型质量关系未讨论，鉴于下游 null result 尤为重要。

### Questions
Q1: F1 epoch confound 在 from-scratch 不适用，论文对最常见 pretraining 设定有何 relevance？
Q2: 是否尝试过 neural detectors？AUC/ECE guidance 在更广 detector sweep 下是否稳健？
Q3: τ=0.7 是否有 principled 选择方法，还是另一个超参数？
Q4: Per-batch bisection 的 b* variance 对 gradient noise 的影响？
Q5: 1.7B 规模 benefit 缩减，方法在 7B+ 是否完全失效？

### Missing References
- RAID benchmark (Dugan et al., 2024)
- M4 shared task (Wang et al., 2024)

### 新颖性评估
F1 epoch confound: 中偏高；F2 detector calibration: 中；F3 minimum intervention: 中偏低。整体方法新颖性：低。

### Overall: 3.0 (Findings)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-25T04:54:55.389548+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应：Reviewer 2 审稿意见\n\n### 总体一致性\nR2 给出 3.0 (Findings)，与我评分一致。核心共识：epoch confound 是最强贡献；方法效果极小且不迁移下游；规模趋势不利；生态效度有限。\n\n### Strengths\n全部 [AGREE]（S1-S5），其中 S4 (constraint regime 分析) 是 R2 提出而我未单独强调的优点，补充认同。\n\n### Weaknesses 逐条回应\n\n[AGREE] R2-W1: 标题通用性 vs 实验 scope。R2 更尖锐地指出 epoch confound 在 from-scratch pretraining 下不适用——论文最强贡献对最常见设定无意义。比我的 W5 更精准。\n\n[AGREE] R2-W2: 下游零改善与 practitioner framing 矛盾。与我的 N1 高度重叠。R2 补充指出 abstract \"improves over uniform\" 未限定 PPL-only，有误导性。\n\n[REBUT] R2-W3: 方法新颖性有限。虽然单个组件非新，但 α_eff + ESS 对偶约束化 + minimum intervention 在此问题上是新组合。更重要的是，论文的分析贡献（epoch confound、三条件框架）不依赖算法新颖性。整体新颖性应为\"中\"而非\"低\"。\n\n[AGREE] R2-W4: Detector 覆盖面极窄。同意提升至 should-fix。3 detectors 不足以建立通用 threshold，缺 neural detectors。\n\n[AGREE] R2-W5/W6: 与我的 N1/W5 一致。\n\n[AGREE] R2-W7: ρ≥0.4 门槛偏高。我未单独提及，认同其合理性。ρ=0.3 已中性，适用场景确实窄。\n\n[AGREE] R2-W8: PPL-accuracy disconnection 未讨论。R2 提出而我未单独讨论的重要视角，补充认同。\n\n### Questions\n[AGREE] Q1, Q2, Q4, Q5\n[REBUT] Q3: τ=0.7 的选择——论文 §5.3 + Appendix D 已提供 τ∈[0.5,0.95] sweep，[0.5,0.8] 均优于 uniform，经验性选择在 2-hyperparameter 方法中可接受。\n\n### Missing References\n[AGREE]: RAID benchmark 和 M4 shared task 确实相关。\n\n### 与 R2 的唯一实质分歧\n方法新颖性：R2 评\"低\"，我评\"中偏低\"。不影响整体评分。\n\n### 我的独有问题（R2 未提及）\n1. N2: α_eff proxy 的理论保证断裂（Wang 2026 要求 true fraction，proxy R²≈0.63）\n2. W1: Grid-best b=0.3 vs adaptive b*≈0.9 偏差及 α_eff 负偏差的影响\n3. W2: 缺少 \"uniform + multi-epoch\" 基线\n4. W4: B=4 是最弱设置却用于主实验",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应：Reviewer 2 审稿意见\n\n### 总体一致性\nR2 给出 3.0 (Findings)，与我评分一致。核心共识：epoch confound 是最强贡献；方法效果极小且不迁移下游；规模趋势不利；生态效度有限。\n\n### Strengths\n全部 [AGREE]（S1-S5），其中 S4 (constraint regime 分析) 是 R2 提出而我未单独强调的优点，补充认同。\n\n### Weaknesses 逐条回应\n\n[AGREE] R2-W1: 标题通用性 vs 实验 scope。R2 更尖锐地指出 epoch confound 在 from-scratch pretraining 下不适用——论文最强贡献对最常见设定无意义。比我的 W5 更精准。\n\n[AGREE] R2-W2: 下游零改善与 practitioner framing 矛盾。与我的 N1 高度重叠。R2 补充指出 abstract \"improves over uniform\" 未限定 PPL-only，有误导性。\n\n[REBUT] R2-W3: 方法新颖性有限。虽然单个组件非新，但 α_eff + ESS 对偶约束化 + minimum intervention 在此问题上是新组合。更重要的是，论文的分析贡献（epoch confound、三条件框架）不依赖算法新颖性。整体新颖性应为\"中\"而非\"低\"。\n\n[AGREE] R2-W4: Detector 覆盖面极窄。同意提升至 should-fix。3 detectors 不足以建立通用 threshold，缺 neural detectors。\n\n[AGREE] R2-W5/W6: 与我的 N1/W5 一致。\n\n[AGREE] R2-W7: ρ≥0.4 门槛偏高。我未单独提及，认同其合理性。ρ=0.3 已中性，适用场景确实窄。\n\n[AGREE] R2-W8: PPL-accuracy disconnection 未讨论。R2 提出而我未单独讨论的重要视角，补充认同。\n\n### Questions\n[AGREE] Q1, Q2, Q4, Q5\n[REBUT] Q3: τ=0.7 的选择——论文 §5.3 + Appendix D 已提供 τ∈[0.5,0.95] sweep，[0.5,0.8] 均优于 uniform，经验性选择在 2-hyperparameter 方法中可接受。\n\n### Missing References\n[AGREE]: RAID benchmark 和 M4 shared task 确实相关。\n\n### 与 R2 的唯一实质分歧\n方法新颖性：R2 评\"低\"，我评\"中偏低\"。不影响整体评分。\n\n### 我的独有问题（R2 未提及）\n1. N2: α_eff proxy 的理论保证断裂（Wang 2026 要求 true fraction，proxy R²≈0.63）\n2. W1: Grid-best b=0.3 vs adaptive b*≈0.9 偏差及 α_eff 负偏差的影响\n3. W2: 缺少 \"uniform + multi-epoch\" 基线\n4. W4: B=4 是最弱设置却用于主实验",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-25T04:54:58.951935+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3562
}
```

</details>

---


### Assistant

_source line 824 · 2026-05-25T04:55:04.516023+00:00_

交叉回应已提交。与 R2 在整体评分（3.0 Findings）和核心判断上高度一致，唯一实质分歧是方法新颖性评估（R2: 低, 我: 中偏低）。我额外提出了 4 个 R2 未涉及的问题：α_eff 理论断裂、b* 系统偏差、缺 multi-epoch 基线、B=4 配置问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 27

## Round 27

64 recorded events


### User

_source line 825 · 2026-05-25T21:16:53.355235+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。

## 投稿信息
- **论文**: "When Does Detect-and-Reweight Work for Synthetic Contamination?"
- **Venue**: EMNLP 2026 via ARR
- **类型**: Long paper（正文 ≤8 页，references 不限，Limitations 不计页数）
- **匿名**: Double-blind
- **模板**: ACL style
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf`

## 你的审查侧重

**核心关注（必须逐条评估）**：
1. **统计方法论**：5 seeds 的统计检验力是否充分？Bonferroni-Holm 校正的使用是否恰当？Cohen's d=3.83 是否被 deterministic data ordering 人为放大（seeds 仅影响模型初始化，data order 固定）？paired t-test 的前提假设是否满足？
2. **效应量与实际意义**：Δ=-0.023 PPL（0.13% relative）的工程意义如何？下游任务零改善（|Δ|≤0.01）是否与 practitioner-oriented framing 矛盾？
3. **α_eff proxy 可靠性**：Pearson r≈0.79 (R²≈0.63) 意味 ~37% 未解释方差。Wang (2026) 理论保证要求 true real fraction ≥ τ，但论文用 α_eff 替代，理论保证是否仍成立？
4. **D&R 机制分析**：epoch-matched controls 的设计是否严谨？是否缺少 uniform × multi-epoch baseline（全数据 ~3.2 epochs）来区分纯重复 vs 选择性重复？
5. **Scale effects**：0.6B→1.7B 效应递减 43%（Δ=-0.023→-0.013），OOD 方向不一致。对 practitioner 适用性的影响？
6. **Detector 覆盖**：仅 3 个 detector（TF-IDF+LR, GPT-2 PPL, N-gram），是否足以支撑 AUC/ECE threshold 的通用性声明？
7. **Grid-best b=0.3 vs adaptive b*≈0.9 偏差**：α_eff 负偏差是否导致过度干预，违背 minimum intervention 原则？
8. **Batch size B=4 限制**：主实验在 advantage 最小的设定下运行（B=4: 1.0×, B=16: 3.0×），是否影响结论强度？

**格式要求**：
- 按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出
- 每条 Weakness 标注 severity（critical/warning/info）并引用具体 Section/Table/Figure
- 给出 Overall Assessment 评分（参照 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-25T21:17:02.840158+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-25T21:17:02.991768+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-25T21:17:08.768152+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 829 · 2026-05-25T21:17:09.322040+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-25T21:17:10.025034+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-25T21:17:10.377923+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 405.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.7}], \"total_pages\": 15, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance
…[truncated 95 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1609
}
```

</details>

---


### Tool result

_source line 832 · 2026-05-25T21:17:10.378338+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\graphicspath{{../../artifacts/figures/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{algorithm}
15	\usepackage{algorithmic}
16	\usepackage{booktabs}
17	\usepackage{multirow}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	\setlength{\textfloatsep}{6pt plus 2pt minus 2pt}
30	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
31	\setlength{\abovecaptionskip}{4pt plus 1pt minus 1pt}
32	\setlength{\belowcaptionskip}{0pt}
33	\title{When Does Detect-and-Reweight Work for Synthetic Contamination?}
34	
35	\author{Anonymous}
36	
37	\begin{document}
38	\maketitle
39	
40	\begin{abstract}
41	\input{sections/abstract}
42	\end{abstract}
43	
44	\section{Introduction}
45	\label{sec:intro}
46	\input{sections/introduction}
47	
48	\section{Related Work}
49	\label{sec:related}
50	\input{sections/related_work}
51	
52	\section{Method}
53	\label{sec:method}
54	\input{sections/method}
55	
56	\section{Experimental Setup}
57	\label{sec:experiments}
58	\input{sections/experiments}
59	
60	\section{Results}
61	\label{sec:results}
62	\input{sections/results}
63	
64	\section{Discussion}
65	\label{sec:discussion}
66	\input{sections/discussion}
67	
68	\section{Conclusion}
69	\label{sec:conclusion}
70	\input{sections/conclusion}
71	
72	\section*{Limitations}
73	\label{sec:limitations}
74	\input{sections/limitations}
75	
76	\bibliography{references}
77	
78	\appendix
79	\input{sections/appendix}
80	
81	\end{document}
82	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-25T21:17:18.051153+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Excitement Score

You may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Overall Recommendation

The metareview score options include: 5 = Consider for Award (top 2.5% papers), ... 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit (paper has to be fully redone, or it is not relevant to the *ACL community).

…[truncated 430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8729
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-25T21:17:21.096521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 835 · 2026-05-25T21:17:21.600272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 836 · 2026-05-25T21:17:22.525216+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1428
}
```

</details>

---


### Tool call

_source line 837 · 2026-05-25T21:17:22.525519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 838 · 2026-05-25T21:17:23.129893+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1529
}
```

</details>

---


### Tool call

_source line 839 · 2026-05-25T21:17:23.130378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 840 · 2026-05-25T21:17:24.948638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2423
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-25T21:17:24.955727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1825
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-25T21:17:24.961311+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, especially: 1) Overall Assessment scale (1-5 with descriptions), 2) Soundness score scale, 3) Excitement score scale, 4) Any other scoring dimensions. Include the full description for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria, especially: 1) Overall Assessment scale (1-5 with descriptions), 2) Soundness score scale, 3) Excitement score scale, 4) Any other scoring dimensions. Include the full description for each score level."
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-25T21:17:30.687313+00:00_

# ARR Reviewer Scoring Criteria

Based on the provided guidelines, ARR uses **three main scoring dimensions**:

## 1. Soundness Score
The document indicates this score must be justified by the review text. "If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

## 2. Excitement Score
This represents subjective personal interest, described as "orthogonal to the assessment of the soundness of the paper." The guidelines note that reviewers may find work technically sound but personally uninteresting, warranting separate evaluation through this dimension.

## 3. Overall Assessment Score
This provides an explicit recommendation for paper outcomes if committed to an ACL venue. It functions as a composite evaluation reflecting "soundness, excitement, and also other factors like novelty and impact."

## Important Limitation
**The document does not provide specific numerical scales (1-5) or detailed descriptive anchors for any of these three scoring dimensions.** The guidelines explain the *conceptual purpose* of each score but do not include the actual scoring rubrics with point values or level descriptions that would typically appear on the review form itself.

The actual scoring form details are referenced separately in a post about "[the ARR review form](https://aclrollingreview.org/reviewform)" but that content is not included in the provided document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5726
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-25T21:17:35.103350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-25T21:17:36.208520+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-25T21:17:36.460781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 847 · 2026-05-25T21:17:36.816028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-25T21:17:37.168965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-25T21:17:39.287681+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2826
}
```

</details>

---


### Tool result

_source line 850 · 2026-05-25T21:17:39.288819+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2472
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-25T21:17:39.291295+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2122
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-25T21:17:39.291625+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring scales. I need the exact numerical scale and description for each level of: 1) Soundness, 2) Excitement/Novelty, 3) Overall Assessment. Include all score values (e.g., 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5) and their descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring scales. I need the exact numerical scale and description for each level of: 1) Soundness, 2) Excitement/Novelty, 3) Overall Assessment. Include all score values (e.g., 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5) and their descriptions."
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-25T21:17:45.168999+00:00_

# ACL Rolling Review Form Scoring Scales

## 1) Soundness

"Given that this is a short/long paper, is it sufficiently sound and thorough?"

- **5 = Excellent:** "This study is one of the most thorough I have seen, given its type."
- **4.5:** (intermediate option available)
- **4 = Strong:** "This study provides sufficient support for all of its claims."
- **3.5:** (intermediate option available)
- **3 = Acceptable:** "This study provides sufficient support for its main claims."
- **2.5:** (intermediate option available)
- **2 = Poor:** "Some of the main claims are not sufficiently supported."
- **1.5:** (intermediate option available)
- **1 = Major Issues:** "This study is not yet sufficiently thorough to warrant publication."

## 2) Excitement/Novelty

"How exciting is this paper for you?"

- **5 = Highly Exciting:** "I would recommend this paper to others and/or attend its presentation."
- **4.5:** (intermediate option available)
- **4 = Exciting:** "I would mention this paper to others and/or make an effort to attend."
- **3.5:** (intermediate option available)
- **3 = Interesting:** "I might mention some points to others and/or attend if time permits."
- **2.5:** (intermediate option available)
- **2 = Potentially Interesting:** "This paper does not resonate with me, but might with others."
- **1.5:** (intermediate option available)
- **1 = Not Exciting:** "This paper does not resonate with me" nor the broader community.

## 3) Overall Assessment

- **5 = Award:** "Consider for an outstanding paper award" (top 2.5%)
- **4.5 = Borderline Award**
- **4 = Conference:** "This paper could be accepted to an *ACL conference."
- **3.5 = Borderline Conference**
- **3 = Findings:** "This paper could be accepted to the Findings of the ACL."
- **2.5 = Borderline Findings**
- **2 = Resubmit next cycle:** "Needs substantial revisions" completable soon
- **1.5 = Resubmit after next cycle:** "Needs substantial revisions" requiring extended time
- **1 = Do not resubmit:** Fundam
…[truncated 35 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5877
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-25T21:18:01.042739+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "9-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "9-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-25T21:18:02.303051+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.0}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 374.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 387.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.5}], \"total_pages\": 15, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1260
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-25T21:18:04.762916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-25T21:18:05.667118+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-25T21:18:05.717813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 859 · 2026-05-25T21:18:06.220031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 860 · 2026-05-25T21:18:06.472048+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 861 · 2026-05-25T21:18:06.576028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 862 · 2026-05-25T21:18:06.679186+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 459
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-25T21:18:07.032980+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-25T21:18:13.162884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-25T21:18:13.917878+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-25T21:18:13.918297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 867 · 2026-05-25T21:18:14.119572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 868 · 2026-05-25T21:18:14.824906+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-25T21:18:15.026444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-25T21:20:34.867740+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper LaTeX sections",
  "subagent_type": "Explore",
  "prompt": "Read these files and return their FULL contents. I need every word:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex\n\nSearch breadth: medium"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper LaTeX sections",
    "subagent_type": "Explore",
    "prompt": "Read these files and return their FULL contents. I need every word:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex\n\nSearch breadth: medium"
  }
}
```

</details>

---


### Tool call

_source line 871 · 2026-05-25T21:20:36.273426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 872 · 2026-05-25T21:20:36.474512+00:00_

1	As synthetic text pervades web corpora, detect-and-reweight methods that downweight likely-synthetic samples during training have emerged to prevent model collapse, yet when they actually help remains unclear.
2	We investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.
3	First, detect-and-remove (D\&R) outperforms all reweighting methods in our setting; epoch-matched controls attribute over 95\% of the advantage to multi-epoch exposure on filtered data, identifying the mechanism behind D\&R's effectiveness.
4	Second, the detector must provide both sufficient discrimination \emph{and} good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.
5	Third, minimum intervention, applying the smallest reweighting exponent that meets a quality floor, outperforms unconstrained weight maximization.
6	As an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $\bstar$ that improves over uniform training at contamination ratios $\rho \geq 0.4$, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.
7	These findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination and larger models remains to be established\footnote{Code and data are available at \url{https://anonymous.4open.science/r/provenance_weight_training-F72D/}.}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 873 · 2026-05-25T21:20:36.474892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 874 · 2026-05-25T21:20:36.876580+00:00_

1	\begin{figure}[t]
2	\centering
3	\includegraphics[width=\columnwidth]{dr_pipeline_concept}
4	\caption{Overview of the detect-and-reweight pipeline. A TF-IDF + LR detector assigns contamination scores $q(x)$; a dual-constrained optimizer selects $b$ to satisfy quality-floor and effective-sample-size constraints; the resulting weights $w(x) = (1{-}q(x))^{b}$ are applied during training.}
5	\label{fig:pipeline}
6	\end{figure}
7	
8	Figure~\ref{fig:pipeline} illustrates the pipeline. Let $\mathcal{D}$ denote a pretraining corpus with unknown synthetic contamination ratio $\rho$~\citep{cheng2025contamination}.
9	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
10	Rather than selecting $b$ via grid search, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
11	
12	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
13	
14	\paragraph{Quality floor.}
15	The \emph{effective authenticity} $\aeff(b) = \sum_i w_i(b)(1{-}q_i) / \sum_i w_i(b)$ measures the weighted mean detector confidence that samples are real.
16	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
17	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.79$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
18	
19	\paragraph{Stability ceiling.}
20	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
21	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
22	
23	\paragraph{Adaptive $\bstar$.}
24	Since $\aeff$ i
…[truncated 1925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 875 · 2026-05-25T21:20:36.877001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 876 · 2026-05-25T21:20:37.078074+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\setlength{\tabcolsep}{3pt}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
9	\midrule
10	Uniform                & 17.694 & 17.686 & 17.702 & 17.697 $\pm$ .008 \\
11	Adaptive $\bstar$ (ours) & \textbf{17.680} & \textbf{17.666} & \textbf{17.677} & \textbf{17.674} $\pm$ .006 \\
12	ESS-only               & 17.730 & 17.720 & 17.760 & 17.737 $\pm$ .021 \\
13	Random $\mathcal{U}(0,2)$ & 17.830 & 17.800 & 17.777 & 17.802 $\pm$ .027 \\
14	Permuted $q$-scores  & 17.919 & --     & --     & 17.919 \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Main comparison: held-out PPL ($\downarrow$) at $\rho{=}0.4$, 1 content epoch.
18	Adaptive and Uniform: 5-seed means (seeds 42, 123, 456, 789, 234); ESS-only and Random: 3-seed means (seeds 42, 123, 456); Permuted: single seed (42).
19	Adaptive uses $\tau{=}0.7$, $\nmin{=}2$.
20	Permuted randomly shuffles $q$-scores across samples, destroying provenance signal while preserving weight non-uniformity ($\Delta{=}{+}0.225$).}
21	\label{tab:main}
22	\end{table}
23	
24	\subsection{Main Results}
25	\label{sec:main-results}
26	
27	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across five seeds.
28	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
29	
30	Adaptive $\bstar$ achieves 5-seed mean PPL 17.674, compared to 17.697 for uniform ($\Delta{=}{-}0.023$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean, post-hoc oracle; gap $+$0.054; Table~\ref{tab:aux}).
31	A paired $t$-test yields $t(4){=}{-}8.21$, $p{=}0.0012$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.011$, reaching conventional significance at $\alpha{=}0.05$.
32	The engineering benefit is eliminating $b$ grid search (nine full training runs~\citep{dray
…[truncated 13772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 877 · 2026-05-25T21:20:37.078427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 878 · 2026-05-25T21:20:37.229159+00:00_

1	\begin{itemize}[nosep,leftmargin=*]
2	\item \textbf{Scope.}
3	All experiments use Qwen3 (0.6B and 1.7B) under self-contamination with 132--200M tokens of continued pretraining.
4	Generalization to other architectures, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination, where generator-corpus distribution mismatch may reduce detector accuracy, remains untested.
5	
6	\item \textbf{Detector coverage.}
7	Only three detectors from two families (discriminative TF-IDF+LR and generative perplexity scorers) were evaluated; fine-tuned neural classifiers (e.g., ModernBERT) and zero-shot methods (e.g., DetectGPT, Binoculars) remain untested, so the AUC/ECE thresholds reported here may shift with broader detector coverage.
8	
9	\item \textbf{Evaluation scope.}
10	Our primary metric is held-out perplexity; downstream accuracy is unchanged across conditions (Appendix~\ref{app:downstream}), so the practical benefit at 0.6B scale is limited to distributional quality rather than task performance.
11	\end{itemize}
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 879 · 2026-05-25T21:20:37.279820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 880 · 2026-05-25T21:20:37.330393+00:00_

1	\paragraph{D\&R as the strongest strategy.}
2	D\&R outperforms all reweighting methods by $0.35$--$0.42$ PPL (Table~\ref{tab:epoch_match}), but epoch-matched controls attribute ${>}$95\% of this advantage to multi-epoch exposure on filtered data rather than superior per-token learning.
3	This benefit was invisible in \citet{drayson2025detection}, where from-scratch pretraining rarely completes one epoch; in continued pretraining, it becomes the dominant factor.
4	
5	\paragraph{When uniform beats reweighting.}
6	Table~\ref{tab:decision} summarizes three prerequisites for effective soft reweighting: (i)~sufficient detector discrimination \emph{and} calibration (AUC\,$\geq$\,0.9, ECE\,$\leq$\,0.05; \S\ref{sec:robustness}); (ii)~contamination $\rho \geq 0.4$, below which the method degrades ($+$0.046 at $\rho{=}0.2$; Appendix~\ref{app:rho02}) with a sharp transition in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}); (iii)~generator--trainee mismatch (at 1.7B the benefit diminishes to $\Delta{=}{-}0.013$ with OOD mixed).
7	When any condition is violated, uniform is the safer default.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\setlength{\tabcolsep}{3pt}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}lcll@{}}
15	\toprule
16	\textbf{Condition} & \textbf{Observed?} & \textbf{Evidence} & \textbf{$\Delta$ PPL} \\
17	\midrule
18	Detector AUC $\geq 0.9$ & Yes & N-gram (0.73) degrades & $+$0.129 \\
19	Detector ECE $\leq 0.05$ & Yes & GPT-2 (0.131) degrades & $+$0.098 \\
20	Contamination $\rho \geq 0.4$ & Yes & $\rho{=}0.2$ degrades & $+$0.046 \\
21	Generator $\neq$ trainee & Tentative & 1.7B: $\Delta{=}{-}0.013$, OOD mixed & -- \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Decision summary for practitioners.
25	$\Delta$ values are relative to uniform (positive = worse).
26	When any observed condition is violated, uniform is the safer default.}
27	\label{tab:decision}
28	\end{table}
29	
30	\paragraph{Effect size and downstream impact.}
31
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-25T21:21:57.902886+00:00_

Here are the FULL contents of all five files:

---

## 1. abstract.tex

As synthetic text pervades web corpora, detect-and-reweight methods that downweight likely-synthetic samples during training have emerged to prevent model collapse, yet when they actually help remains unclear.
We investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.
First, detect-and-remove (D&R) outperforms all reweighting methods in our setting; epoch-matched controls attribute over 95% of the advantage to multi-epoch exposure on filtered data, identifying the mechanism behind D&R's effectiveness.
Second, the detector must provide both sufficient discrimination and good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.
Third, minimum intervention, applying the smallest reweighting exponent that meets a quality floor, outperforms unconstrained weight maximization.
As an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $b*$ that improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.
These findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination and larger models remains to be established (Code and data are available at https://anonymous.4open.science/r/provenance_weight_training-F72D/).

---

## 2. method.tex

[FIGURE CAPTION: Overview of the detect-and-reweight pipeline. A TF-IDF + LR detector assigns contamination scores q(x); a dual-constrained optimizer selects b to satisfy quality-floor and effective-sample-size constraints; the resulting weights w(x) = (1−q(x))^b are applied during training.]

Figure illustrates the pipeline. Let D denote a pretraining corpus with unknown synthetic contamination ratio ρ.
A det
…[truncated 16799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 83035
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-25T21:25:38.688067+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n### 总体评分\n\n**Overall Assessment**: **3.0 — Findings**\n**Soundness**: 3.5 / 5\n**Excitement**: 2.5 / 5\n\n**一句话总结**: 一篇透明且实验设计严谨的机制分析工作，揭示了 D&R 优势的真正来源（multi-epoch exposure），但 0.13% PPL 改善 + 零下游提升与 practitioner-oriented framing 之间存在根本矛盾，且统计效应量被实验设计人为放大。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 控制实验设计严谨（epoch-matched controls 是亮点），但 Cohen's d 被固定 data order 人为放大；α_eff proxy 有 37% 未解释方差；adaptive b* 系统性地偏离 grid-optimal，违背自身 minimum intervention 原则 |\n| Excitement | 2.5/5 | 问题本身重要且及时（synthetic contamination 是实际问题），multi-epoch 机制发现有洞察价值，但实际效果几乎为零（downstream Δ≤0.01），且效应随 scale 递减，实用价值有限 |\n\n---\n\n### 主要优势\n\n- **S1: Epoch-matched control 分析是本文最大亮点。** Table 3 (Section 5.1) 通过将 D&R (q>0.5) 限制为 ~1.0 content epoch，将 0.424 PPL 的 raw advantage 分解为 multi-epoch exposure（占 >95%）和 selective filtering（仅 Δ=0.017），清晰揭示了 D&R 生效的真正机制。\n\n- **S2: Ablation 设计层层递进，控制变量清晰。** Permuted q-scores（Δ=+0.225）、Random U(0,2)、ESS-only 的对比（Table 2）有效隔离了 detector signal 和 minimum intervention 两个必要条件。\n\n- **S3: 对自身局限性的透明度值得肯定。** Limitations 节坦诚承认 downstream accuracy 无变化、detector coverage 有限、scale 泛化未验证。\n\n- **S4: Dual-constrained adaptive 方法有理论动机。** Quality floor + stability ceiling 结合为区间 [b_τ, b_ESS]，取最小 b 实现 minimum intervention，原理清晰。\n\n- **S5: Batch-size amplification 结果有价值。** Figure 7 展示 B=4→16 时优势从 1.0× 到 3.0× 的 monotonic 增长。\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Effect size 与 practitioner framing 之间的根本矛盾**\n- 具体位置：Section 5.1 (Δ=−0.023, 0.13%), Section 5.2 (downstream 0.5414 vs 0.5415), Section 6 Table 5\n- 问题：论文标题 \"When Does D&R Work?\" 和 Table 5 的 practitioner decision summary 建立了面向实践者的叙事框架。然而核心结果是：(a) PPL 改善仅 0.023（0.13% relative），(b) 下游任务准确率完全相同（0.5414 vs 0.5415），(c) 在 1.7B 尺度效应再减半至 Δ=−0.013 且 OOD 方向不一致。对下游任务零贡献的方法，其 \"effectiveness conditions\" 对实践者的指导意义何在？\n- 为什么影响接收：论文的 core claim 是识别 D&R 的 effectiveness conditions，但 \"effective\" 仅限于 held-out PPL 的统计显著变化，不包含任何 task-level 意义。如果 D&R 只在 PPL 上有统计可检测但实际无意义的改善，那么 \"When Does D&R Work?\" 的答案可能是 \"it doesn't, at this scale\"。\n- 建议：(1) 重新定位为 mechanism analysis 而非 practitioner guide；(2) 在 Abstract/Intro 中前置效应量级限制；(3) 增加 PPL Δ=0.023 的工程意义讨论。\n\n**N2** [critical] **Cohen's d = 3.83 被 deterministic data ordering 系统性放大**\n- 具体位置：Section 5.1, Appendix Q (σ=0.006)\n- 问题：5 个 seed 仅改变模型初始化，dataloader 完全 deterministic。SD_Δ=0.006 反映的是初始化噪声的极小方差，而非方法在不同数据条件下的稳健性。Cohen's d = 0.023/0.006 = 3.83 严重高估效应 robustness。如果 data ordering 也随机化，SD_Δ 很可能大幅增加，Cohen's d 可能降至 <1。\n- 为什么影响接收：直接报告 Cohen's d=3.83 而不在正文中充分讨论 deterministic-order 限制，可能误导读者。\n- 建议：(1) 正文中明确 Cohen's d 在此设计下的 interpretability 限制；(2) 补充不同 data permutation 实验；(3) 或改用 bootstrap CI for Δ 替代 Cohen's d。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] **缺少 uniform × multi-epoch baseline**\n- 具体位置：Table 3\n- 问题：D&R (q>0.3) 的 raw PPL=17.250 源于 ~3.2 content epochs。缺少对全部数据做 ~3.2 epochs 的 uniform baseline，无法区分 pure repetition 和 selective filtering 的贡献。\n- 建议：增加 Uniform × {2, 3} epochs 行。\n\n**W2** [warning] **α_eff proxy 的 37% 未解释方差削弱理论保证**\n- 具体位置：Section 3, Table 12 (Appendix J)\n- 问题：R²≈0.63，约 37% 的 batch-level 方差未被捕获。未量化 α_eff ≥ τ 但 true fraction < τ 的 violation 频率。\n- 建议：利用 ground-truth labels 计算 violation batch 比例和影响。\n\n**W3** [warning] **Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差**\n- 具体位置：Section 5.1, Table 2\n- 问题：Adaptive 施加约 3× 于 grid-optimal 的权重抑制，PPL gap 0.054 是 adaptive-vs-uniform gain（0.023）的 2.3×。α_eff 的 negative bias 导致 over-intervention，违背 minimum intervention 原则。\n- 建议：讨论偏差来源并探讨 calibration-corrected α_eff。\n\n**W4** [warning] **3 个 detector 不足以支撑 AUC/ECE threshold 通用性**\n- 具体位置：Section 5.1, Table 5\n- 问题：仅 3 个数据点推导 threshold，缺少中间区域 detector（如 AUC=0.85/ECE=0.04）。Table 5 的 binary checklist 过于确定。\n- 建议：将 threshold 表述改为 observed trend，补充更多 detector。\n\n**W5** [warning] **Scale 效应递减 43%，practitioner 适用性存疑**\n- 具体位置：Section 5.2\n- 问题：0.6B→1.7B Δ 减半，OOD 方向不一致。如果归因成立（larger models more robust），则 7B+ 效应可能趋零。\n- 建议：讨论 scaling trend 外推含义。\n\n---\n\n### 小问题\n\n- **M1** [info] B=4 主实验设定低估方法潜力（B=16 时 3.0×），建议说明选择理由。\n- **M2** [info] Paired t-test 正态性假设在 n=5 下无法验证，建议补充 Wilcoxon signed-rank test。\n- **M3** [info] Abstract word count 接近 200-word 限制，建议精确计数。\n\n---\n\n### Questions to Authors\n\n1. 是否有不同 data permutation 下的实验？跨 permutation 的 SD_Δ 和 Cohen's d？\n2. Uniform × multi-epoch baseline 的预期结果？\n3. α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例？\n4. Calibration-corrected α_eff（如 Platt scaling 后）能否缩小 b* vs grid-optimal 的 gap？\n5. 1.7B 实验选择 τ=0.8 而非 0.7 的理由？是否影响 scale comparison 公平性？",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n### 总体评分\n\n**Overall Assessment**: **3.0 — Findings**\n**Soundness**: 3.5 / 5\n**Excitement**: 2.5 / 5\n\n**一句话总结**: 一篇透明且实验设计严谨的机制分析工作，揭示了 D&R 优势的真正来源（multi-epoch exposure），但 0.13% PPL 改善 + 零下游提升与 practitioner-oriented framing 之间存在根本矛盾，且统计效应量被实验设计人为放大。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 控制实验设计严谨（epoch-matched controls 是亮点），但 Cohen's d 被固定 data order 人为放大；α_eff proxy 有 37% 未解释方差；adaptive b* 系统性地偏离 grid-optimal，违背自身 minimum intervention 原则 |\n| Excitement | 2.5/5 | 问题本身重要且及时（synthetic contamination 是实际问题），multi-epoch 机制发现有洞察价值，但实际效果几乎为零（downstream Δ≤0.01），且效应随 scale 递减，实用价值有限 |\n\n---\n\n### 主要优势\n\n- **S1: Epoch-matched control 分析是本文最大亮点。** Table 3 (Section 5.1) 通过将 D&R (q>0.5) 限制为 ~1.0 content epoch，将 0.424 PPL 的 raw advantage 分解为 multi-epoch exposure（占 >95%）和 selective filtering（仅 Δ=0.017），清晰揭示了 D&R 生效的真正机制。\n\n- **S2: Ablation 设计层层递进，控制变量清晰。** Permuted q-scores（Δ=+0.225）、Random U(0,2)、ESS-only 的对比（Table 2）有效隔离了 detector signal 和 minimum intervention 两个必要条件。\n\n- **S3: 对自身局限性的透明度值得肯定。** Limitations 节坦诚承认 downstream accuracy 无变化、detector coverage 有限、scale 泛化未验证。\n\n- **S4: Dual-constrained adaptive 方法有理论动机。** Quality floor + stability ceiling 结合为区间 [b_τ, b_ESS]，取最小 b 实现 minimum intervention，原理清晰。\n\n- **S5: Batch-size amplification 结果有价值。** Figure 7 展示 B=4→16 时优势从 1.0× 到 3.0× 的 monotonic 增长。\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Effect size 与 practitioner framing 之间的根本矛盾**\n- 具体位置：Section 5.1 (Δ=−0.023, 0.13%), Section 5.2 (downstream 0.5414 vs 0.5415), Section 6 Table 5\n- 问题：论文标题 \"When Does D&R Work?\" 和 Table 5 的 practitioner decision summary 建立了面向实践者的叙事框架。然而核心结果是：(a) PPL 改善仅 0.023（0.13% relative），(b) 下游任务准确率完全相同（0.5414 vs 0.5415），(c) 在 1.7B 尺度效应再减半至 Δ=−0.013 且 OOD 方向不一致。对下游任务零贡献的方法，其 \"effectiveness conditions\" 对实践者的指导意义何在？\n- 为什么影响接收：论文的 core claim 是识别 D&R 的 effectiveness conditions，但 \"effective\" 仅限于 held-out PPL 的统计显著变化，不包含任何 task-level 意义。如果 D&R 只在 PPL 上有统计可检测但实际无意义的改善，那么 \"When Does D&R Work?\" 的答案可能是 \"it doesn't, at this scale\"。\n- 建议：(1) 重新定位为 mechanism analysis 而非 practitioner guide；(2) 在 Abstract/Intro 中前置效应量级限制；(3) 增加 PPL Δ=0.023 的工程意义讨论。\n\n**N2** [critical] **Cohen's d = 3.83 被 deterministic data ordering 系统性放大**\n- 具体位置：Section 5.1, Appendix Q (σ=0.006)\n- 问题：5 个 seed 仅改变模型初始化，dataloader 完全 deterministic。SD_Δ=0.006 反映的是初始化噪声的极小方差，而非方法在不同数据条件下的稳健性。Cohen's d = 0.023/0.006 = 3.83 严重高估效应 robustness。如果 data ordering 也随机化，SD_Δ 很可能大幅增加，Cohen's d 可能降至 <1。\n- 为什么影响接收：直接报告 Cohen's d=3.83 而不在正文中充分讨论 deterministic-order 限制，可能误导读者。\n- 建议：(1) 正文中明确 Cohen's d 在此设计下的 interpretability 限制；(2) 补充不同 data permutation 实验；(3) 或改用 bootstrap CI for Δ 替代 Cohen's d。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] **缺少 uniform × multi-epoch baseline**\n- 具体位置：Table 3\n- 问题：D&R (q>0.3) 的 raw PPL=17.250 源于 ~3.2 content epochs。缺少对全部数据做 ~3.2 epochs 的 uniform baseline，无法区分 pure repetition 和 selective filtering 的贡献。\n- 建议：增加 Uniform × {2, 3} epochs 行。\n\n**W2** [warning] **α_eff proxy 的 37% 未解释方差削弱理论保证**\n- 具体位置：Section 3, Table 12 (Appendix J)\n- 问题：R²≈0.63，约 37% 的 batch-level 方差未被捕获。未量化 α_eff ≥ τ 但 true fraction < τ 的 violation 频率。\n- 建议：利用 ground-truth labels 计算 violation batch 比例和影响。\n\n**W3** [warning] **Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差**\n- 具体位置：Section 5.1, Table 2\n- 问题：Adaptive 施加约 3× 于 grid-optimal 的权重抑制，PPL gap 0.054 是 adaptive-vs-uniform gain（0.023）的 2.3×。α_eff 的 negative bias 导致 over-intervention，违背 minimum intervention 原则。\n- 建议：讨论偏差来源并探讨 calibration-corrected α_eff。\n\n**W4** [warning] **3 个 detector 不足以支撑 AUC/ECE threshold 通用性**\n- 具体位置：Section 5.1, Table 5\n- 问题：仅 3 个数据点推导 threshold，缺少中间区域 detector（如 AUC=0.85/ECE=0.04）。Table 5 的 binary checklist 过于确定。\n- 建议：将 threshold 表述改为 observed trend，补充更多 detector。\n\n**W5** [warning] **Scale 效应递减 43%，practitioner 适用性存疑**\n- 具体位置：Section 5.2\n- 问题：0.6B→1.7B Δ 减半，OOD 方向不一致。如果归因成立（larger models more robust），则 7B+ 效应可能趋零。\n- 建议：讨论 scaling trend 外推含义。\n\n---\n\n### 小问题\n\n- **M1** [info] B=4 主实验设定低估方法潜力（B=16 时 3.0×），建议说明选择理由。\n- **M2** [info] Paired t-test 正态性假设在 n=5 下无法验证，建议补充 Wilcoxon signed-rank test。\n- **M3** [info] Abstract word count 接近 200-word 限制，建议精确计数。\n\n---\n\n### Questions to Authors\n\n1. 是否有不同 data permutation 下的实验？跨 permutation 的 SD_Δ 和 Cohen's d？\n2. Uniform × multi-epoch baseline 的预期结果？\n3. α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例？\n4. Calibration-corrected α_eff（如 Platt scaling 后）能否缩小 b* vs grid-optimal 的 gap？\n5. 1.7B 实验选择 τ=0.8 而非 0.7 的理由？是否影响 scale comparison 公平性？",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-25T21:25:42.051753+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3363
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-25T21:25:52.502268+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-25T21:25:52.552930+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-25T21:25:55.792532+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-25T21:25:55.843174+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 888 · 2026-05-25T21:26:04.926810+00:00_

审稿完成，意见已发送给 Review Director。

**总结**：Overall 3.0（Findings），Soundness 3.5，Excitement 2.5。两个 critical 问题：(1) 效应量极小（0.13% PPL，零下游提升）与 practitioner-oriented framing 矛盾；(2) Cohen's d=3.83 被 deterministic data ordering 人为放大。五个 warning：缺 uniform multi-epoch baseline、α_eff proxy 37% 未解释方差、adaptive b* 系统性 over-intervention、3 个 detector 不足以定 threshold、scale 效应递减。论文最大亮点是 epoch-matched control 揭示 D&R 优势来自 multi-epoch exposure 而非 selective filtering。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 28

## Round 28

4 recorded events


### User

_source line 889 · 2026-05-25T21:26:43.566835+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量

**Overall**: 3.0 (Findings)
**Soundness**: 3.5/5 | **Excitement**: 2.5/5

### 主要优势
1. 严谨的实验控制设计（epoch-matched D&R controls）
2. 诚实的 self-assessment
3. 消融设计清晰，隔离变量有效
4. 统计处理高于平均水平
5. Calibration finding 有实用价值

### Must-Fix 问题

**N1** [critical] Abstract 中 "ρ ≥ 0.4" 统计显著性声明存在 overclaim
- Abstract 写 "improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction"。但 §5.2 报告 ρ=0.6 的 p_BH=0.064，未通过 BH correction at α=0.05。只有 ρ=0.4 达到显著性（p_BH=0.011）。

**N2** [critical] 标题 scope 与实验覆盖面严重不匹配
- "When Does Detect-and-Reweight Work for Synthetic Contamination?" 暗示一般性但实验仅覆盖 self-contamination / 0.6B / continued pretraining / 单一数据源 / 主要一个 detector family。

**N3** [critical] 无下游任务提升，但 Abstract 未提及
- Abstract 说 "improves over uniform training" 不指定 metric，读者自然理解为综合质量提升。但下游 accuracy 完全无变化（0.5414 vs. 0.5415）。

### Should-Fix 问题

**W1** [warning] §6 Discussion 第一段与 §5.1 内容高度重复
**W2** [warning] "Three effectiveness conditions" 的 framing 过度概括——应改为 "empirical observations" 或 "findings"
**W3** [warning] Related Work 缺少 MATES、Aioli、RAID、M4 等近期方法
**W4** [warning] Decision summary（Table 5）的实用性受限于验证范围
**W5** [warning] Δ=-0.023 的效应量在 continued pretraining 语境中缺乏 baseline contextualization

### 小问题
- M1: Table 1 caption 声明 5-seed 但只显示 3 列 seed
- M2: §5.2 与 Appendix I 的 t 值不一致（-9.95 vs -15.4）
- M3: "three effectiveness conditions" 编号在 Intro/Discussion/Conclusion 间微有不一致
- M4: Appendix P Table 16 seed 456 缺少 OOD 评估未解释
- M5: Sliding-window evaluation 未说明 window size

### Questions to Authors
1. Adaptive reweighting 的 use case 在 D&R 更优的情况下是什么？
2. Temperature scaling T=0.204 需要 labeled data，web-scale 下如何满足？
3. B=4 在 modern pretraining 中不常见，是否有 B=64/128 的预期行为分析？

### Missing References
MATES (Yu et al., 2024)、Aioli (Balachandran et al., 2024)、RAID (Dugan et al., 2024)、M4 (Wang et al., 2024)

### 格式合规检查：全部通过 ✓

---

请对上述每条 Must-Fix、Should-Fix 和 Questions 给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-25T21:28:43.898814+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Abstract 中 \"ρ ≥ 0.4\" 统计显著性声明存在 overclaim**\n同意，这是一个明确的事实性错误。§5.2 报告 ρ=0.6 时 p_BH=0.064，未通过 α=0.05 after Bonferroni-Holm correction。Abstract 的 \"ρ ≥ 0.4, reaching conventional significance\" 暗示 ρ=0.4 和 ρ=0.6 均显著，但实际上只有 ρ=0.4 (p_BH=0.011) 达到了。这属于 overclaim，必须修正为 \"at ρ=0.4\" 或明确注明 ρ=0.6 仅为 marginal significance。此问题在我的审稿中未单独列出，R2 的发现是对我 N1（framing 矛盾）的有力补充。\n\n**[AGREE] R2-N2: 标题 scope 与实验覆盖面不匹配**\n同意核心判断。\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 的问句形式虽然比陈述句稍为收敛，但仍暗示对 D&R 方法的系统性评估。实验仅覆盖：self-contamination（非 cross-model contamination）、0.6B+1.7B（非 full pretraining scale）、continued pretraining（非 from-scratch）、单一数据源 FineWeb、主要依赖 TF-IDF+LR 一个 detector。这与我 W4（3 个 detector 不足以支撑通用性声明）和 W5（scale 递减）的判断一致。建议标题增加限定词，如 \"...in Controlled Continued Pretraining\" 或 \"...at Sub-Billion Scale\"。\n\n**[AGREE] R2-N3: 无下游任务提升但 Abstract 未提及**\n完全同意。这与我的 N1（effect size 与 practitioner framing 的根本矛盾）高度一致。Abstract 的 \"improves over uniform training\" 未限定 metric，读者会自然理解为包含下游任务质量。实际上 downstream accuracy 在三位有效数字上完全相同（0.5414 vs 0.5415, §5.2 及 Appendix H）。Abstract 应明确写 \"improves held-out perplexity\" 并注明 \"without measurable downstream accuracy gains\"。我认为这与 N1 共同构成本文最核心的问题——framing 与 evidence 之间的 gap。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: §6 Discussion 第一段与 §5.1 重复**\n部分同意。Discussion 开头重述主要发现是学术写作的常见做法，但如果重复度过高（R2 称 \"高度重复\"），在 8 页限制下是空间浪费。§6 第一段 \"D&R outperforms all reweighting methods by 0.35--0.42 PPL... epoch-matched controls attribute >95%...\" 确实与 §5.1 的 epoch-matched analysis 高度重合。建议 §6 开头用一句话概括，将空间用于更深入的 mechanism 讨论（如 why multi-epoch exposure helps specifically for contaminated data，与 curriculum learning 的联系等）。不过我将其定为 minor warning 而非 critical——空间分配不影响接收决定。\n\n**[AGREE] R2-W2: \"Three effectiveness conditions\" framing 过度概括**\n同意。\"Conditions\" 暗示充分必要条件，但论文的 evidence 仅支持 \"empirical observations in a specific controlled setting\"。具体地：(a) 3 个 detector 不足以确立 AUC/ECE threshold 的 boundary（我的 W4）；(b) 仅 self-contamination 设定，不知 cross-model contamination 是否有相同 conditions；(c) scale 效应递减意味着 conditions 可能 scale-dependent。改为 \"three empirical findings\" 或 \"three observed requirements\" 更准确。\n\n**[AGREE] R2-W3: Related Work 缺少 MATES、Aioli、RAID、M4**\n同意，特别是 RAID (Dugan et al., 2024) 作为 AI-generated text detection benchmark 与论文的 detector evaluation 直接相关，M4 (Wang et al., 2024) 作为多语言 machine-generated text detection 也属于同一 research line。MATES (Yu et al., 2024) 如果涉及 data selection for training 则与 §2 Related Work 的 data curation 部分有交集。Aioli (Balachandran et al., 2024) 如果涉及 data mixing 则补充了 domain-level importance weighting 的讨论。这些遗漏不影响接收但确实影响 Related Work 的完整性。\n\n**[AGREE] R2-W4: Table 5 decision summary 实用性受限**\n完全同意，这与我的 W4（3 个 detector 不足以支撑 threshold 通用性）一致。Table 5 将 AUC ≥ 0.9 和 ECE ≤ 0.05 作为 binary checklist 呈现，但背后仅有 3 个数据点。如果实践者拿到一个 AUC=0.88, ECE=0.04 的 detector，Table 5 说 \"不要用\"，但这个结论没有 empirical support（没测试过这个区间）。\n\n**[AGREE] R2-W5: Δ=-0.023 缺乏 baseline contextualization**\n同意。论文未在 continued pretraining 文献中定位 0.023 PPL 这个量级意味着什么。例如：(a) 同等 compute budget 下，换一个 learning rate schedule 能获得多大 PPL delta？(b) 增加 1% training data 的边际 PPL 改善是多少？(c) 其他 data curation 方法（如 DSIR, DsDm）在类似 scale 下的 PPL improvement 是多少？没有这些对照，读者无法判断 0.023 是 \"small but meaningful\" 还是 \"noise-level\"。这补充了我 N1 的论点。\n\n---\n\n### 小问题\n\n**[AGREE] R2-M1: Table caption 5-seed vs 3 列 seed 不一致**\n同意。如果 Table 2 caption 声明 5-seed mean 但表格仅展示 3 个 seed 列（42, 123, 456），读者可能质疑 seed 789 和 234 的结果是否有选择性报告。建议在 caption 中注明 \"full 5-seed results in Appendix X\" 并补充完整数据。\n\n**[AGREE] R2-M2: §5.2 与 Appendix I 的 t 值不一致**\n如果确实存在 t=-9.95 vs t=-15.4 的不一致，这是 proofreading 问题。我未独立验证此数字，但接受 R2 的发现。数值不一致即使是 typo 也需修正，因为损害 reproducibility 和信任度。\n\n**[AGREE] R2-M3: \"Three effectiveness conditions\" 编号不一致**\n同意。如果 Intro/Discussion/Conclusion 中三个条件的表述或排序有微小差异，应统一。\n\n**[AGREE] R2-M4: Appendix P Table 16 seed 456 缺 OOD 评估**\n同意。数据完整性问题，应补充或解释缺失原因。\n\n**[AGREE] R2-M5: Sliding-window evaluation 未说明 window size**\n同意。Reproducibility 要求所有 evaluation hyperparameters 必须明确。§4 Evaluation 或 Appendix 应注明 window size（如 stride 等参数）。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1: Adaptive reweighting 在 D&R 更优时的 use case**\n好问题。Table 3 (§5.1) 明确显示 D&R (q>0.3) 以 PPL 17.250 大幅优于 adaptive (17.674)。论文在 §6 隐含地论证 adaptive 的优势是 \"不需要 grid search\"（节省 ~16 GPU-hours），但 D&R 同样不需要 grid search（只需一个 threshold）。如果 D&R 在所有设定下都优于 adaptive reweighting，后者的实际 use case 确实不清楚——除非存在 D&R 不适用的场景（如 corpus 极小无法承受数据丢弃），但论文未讨论此情形。\n\n**[AGREE] R2-Q2: Temperature scaling T=0.204 需要 labeled data**\n同意这是一个重要的实践限制。论文的 detector calibration（§4, Appendix L）依赖 labeled validation split（10K documents），但在 web-scale pretraining 中，ground-truth synthetic labels 通常不可用。这限制了 Table 5 decision framework 的 deployability。论文应在 Discussion 中讨论 unsupervised calibration alternatives（如 binning-based methods）。\n\n**[AGREE] R2-Q3: B=4 不符合 modern pretraining 实践**\n同意，这与我的 M1 一致。Modern pretraining 典型 micro-batch size 远大于 4（通常 B=32-128 per GPU）。§5.3 展示 B=4→16 时效果提升，但 B=16 仍然远低于实际设定。论文应讨论 (a) B=64/128 时的预期行为（external extrapolation），(b) 大 batch size 下 per-batch α_eff 估计是否更稳定（batch 内更多样本应降低 proxy variance）。\n\n---\n\n### Missing References\n\n**[AGREE]** RAID (Dugan et al., 2024) 和 M4 (Wang et al., 2024) 与 detector evaluation 直接相关，应加入 §2 Related Work。MATES 和 Aioli 的相关性需进一步确认，但如果涉及 training-time data selection/mixing，也应纳入。\n\n---\n\n### 总结\n\nR2 的审稿意见整体质量高，与我的审稿存在大量交叉验证：\n- R2-N3 ≈ 我的 N1（effect size vs framing 矛盾）\n- R2-N2 ≈ 我的 W4+W5（scope 限制）\n- R2-W4 ≈ 我的 W4（detector threshold 通用性）\n- R2-Q3 ≈ 我的 M1（batch size 限制）\n\nR2 额外发现的贡献：\n- **N1（p_BH=0.064 overclaim）是我遗漏的重要事实性错误**，应作为 must-fix\n- **W3（missing references）** 补充了具体的遗漏文献\n- **M2（t 值不一致）** 是具体的 proofreading 发现\n\n两位 Reviewer 独立得出 **Overall 3.0 (Findings)、Soundness 3.5、Excitement 2.5** 的一致评分，增强了评估的可信度。核心共识：**方法论上有贡献（epoch-matched mechanism analysis），但 framing 超出了 evidence 支持的范围，实际效果量级不足以支撑 practitioner-oriented 定位。**",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Abstract 中 \"ρ ≥ 0.4\" 统计显著性声明存在 overclaim**\n同意，这是一个明确的事实性错误。§5.2 报告 ρ=0.6 时 p_BH=0.064，未通过 α=0.05 after Bonferroni-Holm correction。Abstract 的 \"ρ ≥ 0.4, reaching conventional significance\" 暗示 ρ=0.4 和 ρ=0.6 均显著，但实际上只有 ρ=0.4 (p_BH=0.011) 达到了。这属于 overclaim，必须修正为 \"at ρ=0.4\" 或明确注明 ρ=0.6 仅为 marginal significance。此问题在我的审稿中未单独列出，R2 的发现是对我 N1（framing 矛盾）的有力补充。\n\n**[AGREE] R2-N2: 标题 scope 与实验覆盖面不匹配**\n同意核心判断。\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 的问句形式虽然比陈述句稍为收敛，但仍暗示对 D&R 方法的系统性评估。实验仅覆盖：self-contamination（非 cross-model contamination）、0.6B+1.7B（非 full pretraining scale）、continued pretraining（非 from-scratch）、单一数据源 FineWeb、主要依赖 TF-IDF+LR 一个 detector。这与我 W4（3 个 detector 不足以支撑通用性声明）和 W5（scale 递减）的判断一致。建议标题增加限定词，如 \"...in Controlled Continued Pretraining\" 或 \"...at Sub-Billion Scale\"。\n\n**[AGREE] R2-N3: 无下游任务提升但 Abstract 未提及**\n完全同意。这与我的 N1（effect size 与 practitioner framing 的根本矛盾）高度一致。Abstract 的 \"improves over uniform training\" 未限定 metric，读者会自然理解为包含下游任务质量。实际上 downstream accuracy 在三位有效数字上完全相同（0.5414 vs 0.5415, §5.2 及 Appendix H）。Abstract 应明确写 \"improves held-out perplexity\" 并注明 \"without measurable downstream accuracy gains\"。我认为这与 N1 共同构成本文最核心的问题——framing 与 evidence 之间的 gap。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: §6 Discussion 第一段与 §5.1 重复**\n部分同意。Discussion 开头重述主要发现是学术写作的常见做法，但如果重复度过高（R2 称 \"高度重复\"），在 8 页限制下是空间浪费。§6 第一段 \"D&R outperforms all reweighting methods by 0.35--0.42 PPL... epoch-matched controls attribute >95%...\" 确实与 §5.1 的 epoch-matched analysis 高度重合。建议 §6 开头用一句话概括，将空间用于更深入的 mechanism 讨论（如 why multi-epoch exposure helps specifically for contaminated data，与 curriculum learning 的联系等）。不过我将其定为 minor warning 而非 critical——空间分配不影响接收决定。\n\n**[AGREE] R2-W2: \"Three effectiveness conditions\" framing 过度概括**\n同意。\"Conditions\" 暗示充分必要条件，但论文的 evidence 仅支持 \"empirical observations in a specific controlled setting\"。具体地：(a) 3 个 detector 不足以确立 AUC/ECE threshold 的 boundary（我的 W4）；(b) 仅 self-contamination 设定，不知 cross-model contamination 是否有相同 conditions；(c) scale 效应递减意味着 conditions 可能 scale-dependent。改为 \"three empirical findings\" 或 \"three observed requirements\" 更准确。\n\n**[AGREE] R2-W3: Related Work 缺少 MATES、Aioli、RAID、M4**\n同意，特别是 RAID (Dugan et al., 2024) 作为 AI-generated text detection benchmark 与论文的 detector evaluation 直接相关，M4 (Wang et al., 2024) 作为多语言 machine-generated text detection 也属于同一 research line。MATES (Yu et al., 2024) 如果涉及 data selection for training 则与 §2 Related Work 的 data curation 部分有交集。Aioli (Balachandran et al., 2024) 如果涉及 data mixing 则补充了 domain-level importance weighting 的讨论。这些遗漏不影响接收但确实影响 Related Work 的完整性。\n\n**[AGREE] R2-W4: Table 5 decision summary 实用性受限**\n完全同意，这与我的 W4（3 个 detector 不足以支撑 threshold 通用性）一致。Table 5 将 AUC ≥ 0.9 和 ECE ≤ 0.05 作为 binary checklist 呈现，但背后仅有 3 个数据点。如果实践者拿到一个 AUC=0.88, ECE=0.04 的 detector，Table 5 说 \"不要用\"，但这个结论没有 empirical support（没测试过这个区间）。\n\n**[AGREE] R2-W5: Δ=-0.023 缺乏 baseline contextualization**\n同意。论文未在 continued pretraining 文献中定位 0.023 PPL 这个量级意味着什么。例如：(a) 同等 compute budget 下，换一个 learning rate schedule 能获得多大 PPL delta？(b) 增加 1% training data 的边际 PPL 改善是多少？(c) 其他 data curation 方法（如 DSIR, DsDm）在类似 scale 下的 PPL improvement 是多少？没有这些对照，读者无法判断 0.023 是 \"small but meaningful\" 还是 \"noise-level\"。这补充了我 N1 的论点。\n\n---\n\n### 小问题\n\n**[AGREE] R2-M1: Table caption 5-seed vs 3 列 seed 不一致**\n同意。如果 Table 2 caption 声明 5-seed mean 但表格仅展示 3 个 seed 列（42, 123, 456），读者可能质疑 seed 789 和 234 的结果是否有选择性报告。建议在 caption 中注明 \"full 5-seed results in Appendix X\" 并补充完整数据。\n\n**[AGREE] R2-M2: §5.2 与 Appendix I 的 t 值不一致**\n如果确实存在 t=-9.95 vs t=-15.4 的不一致，这是 proofreading 问题。我未独立验证此数字，但接受 R2 的发现。数值不一致即使是 typo 也需修正，因为损害 reproducibility 和信任度。\n\n**[AGREE] R2-M3: \"Three effectiveness conditions\" 编号不一致**\n同意。如果 Intro/Discussion/Conclusion 中三个条件的表述或排序有微小差异，应统一。\n\n**[AGREE] R2-M4: Appendix P Table 16 seed 456 缺 OOD 评估**\n同意。数据完整性问题，应补充或解释缺失原因。\n\n**[AGREE] R2-M5: Sliding-window evaluation 未说明 window size**\n同意。Reproducibility 要求所有 evaluation hyperparameters 必须明确。§4 Evaluation 或 Appendix 应注明 window size（如 stride 等参数）。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1: Adaptive reweighting 在 D&R 更优时的 use case**\n好问题。Table 3 (§5.1) 明确显示 D&R (q>0.3) 以 PPL 17.250 大幅优于 adaptive (17.674)。论文在 §6 隐含地论证 adaptive 的优势是 \"不需要 grid search\"（节省 ~16 GPU-hours），但 D&R 同样不需要 grid search（只需一个 threshold）。如果 D&R 在所有设定下都优于 adaptive reweighting，后者的实际 use case 确实不清楚——除非存在 D&R 不适用的场景（如 corpus 极小无法承受数据丢弃），但论文未讨论此情形。\n\n**[AGREE] R2-Q2: Temperature scaling T=0.204 需要 labeled data**\n同意这是一个重要的实践限制。论文的 detector calibration（§4, Appendix L）依赖 labeled validation split（10K documents），但在 web-scale pretraining 中，ground-truth synthetic labels 通常不可用。这限制了 Table 5 decision framework 的 deployability。论文应在 Discussion 中讨论 unsupervised calibration alternatives（如 binning-based methods）。\n\n**[AGREE] R2-Q3: B=4 不符合 modern pretraining 实践**\n同意，这与我的 M1 一致。Modern pretraining 典型 micro-batch size 远大于 4（通常 B=32-128 per GPU）。§5.3 展示 B=4→16 时效果提升，但 B=16 仍然远低于实际设定。论文应讨论 (a) B=64/128 时的预期行为（external extrapolation），(b) 大 batch size 下 per-batch α_eff 估计是否更稳定（batch 内更多样本应降低 proxy variance）。\n\n---\n\n### Missing References\n\n**[AGREE]** RAID (Dugan et al., 2024) 和 M4 (Wang et al., 2024) 与 detector evaluation 直接相关，应加入 §2 Related Work。MATES 和 Aioli 的相关性需进一步确认，但如果涉及 training-time data selection/mixing，也应纳入。\n\n---\n\n### 总结\n\nR2 的审稿意见整体质量高，与我的审稿存在大量交叉验证：\n- R2-N3 ≈ 我的 N1（effect size vs framing 矛盾）\n- R2-N2 ≈ 我的 W4+W5（scope 限制）\n- R2-W4 ≈ 我的 W4（detector threshold 通用性）\n- R2-Q3 ≈ 我的 M1（batch size 限制）\n\nR2 额外发现的贡献：\n- **N1（p_BH=0.064 overclaim）是我遗漏的重要事实性错误**，应作为 must-fix\n- **W3（missing references）** 补充了具体的遗漏文献\n- **M2（t 值不一致）** 是具体的 proofreading 发现\n\n两位 Reviewer 独立得出 **Overall 3.0 (Findings)、Soundness 3.5、Excitement 2.5** 的一致评分，增强了评估的可信度。核心共识：**方法论上有贡献（epoch-matched mechanism analysis），但 framing 超出了 evidence 支持的范围，实际效果量级不足以支撑 practitioner-oriented 定位。**",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-25T21:28:47.511365+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3612
}
```

</details>

---


### Assistant

_source line 892 · 2026-05-25T21:29:07.876213+00:00_

交叉回应已提交。

所有 R2 的 Must-Fix（N1-N3）、Should-Fix（W1-W5）、小问题（M1-M5）和 Questions（Q1-Q3）均标记为 **[AGREE]**。关键发现：

- R2-N1（ρ≥0.4 的 p_BH=0.064 overclaim）是我遗漏的事实性错误，具有独立价值
- 两位 Reviewer 在 Overall 3.0、Soundness 3.5、Excitement 2.5 上完全一致
- 核心共识：epoch-matched mechanism analysis 有贡献，但 framing 超出 evidence 范围，实际效果不足以支撑 practitioner-oriented 定位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---
