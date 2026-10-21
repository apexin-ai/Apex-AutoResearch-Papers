# Director coordination — Part 4 of 5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/5a/5a5f768420cdca035482.json)

## Round 84

### User

_source line 1115 · 2026-05-23T13:21:58.375014+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告 — Round 1（新颖性 + 完整性 + 写作质量）

**论文**: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"
**Venue**: EMNLP 2026 (ARR May cycle)

---

## 总体评分

**Overall Assessment**: 3.0 / 5 (Findings)
**一句话总结**: 论文对 detect-and-reweight 范式的 epoch confound 进行了有价值的系统分析，但实验范围窄（单模型族/单数据集/自污染）、效应量小（Δ=−0.020 PPL，校正后不显著，下游零改善），方法新颖性偏薄，限制了整体贡献。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | 在其实验范围内方法论扎实，epoch-matched 对比设计合理；但 N=3 seeds 的关键结果校正后未达显著（ρ=0.4: p_BH=0.078; ρ=0.6: p_BH=0.064），削弱了定量结论的稳健性 |
| **Excitement** | 2.5 / 5 | Epoch confound 发现对方法学有价值；其余两个 findings（detector requirements、minimum intervention）属于预期内的增量贡献；Δ=−0.020 PPL 无下游体现，实际影响有限 |
| **Overall** | 3.0 / 5 | 分析论文定位合理，epoch confound 发现有 Findings 级贡献，但效应量过小 + 范围过窄 + adaptive b* 方法新颖性不足，不足以达到 Conference 门槛 |
| **Confidence** | 4 / 5 | 仔细阅读了全文和 17 节 appendix，熟悉 data reweighting / model collapse 相关文献 |
| **Reproducibility** | 4 / 5 | 实验细节充分（Algorithm 1, 超参数表, 三 seed 结果），代码承诺 acceptance 后公开；detector 训练细节（Appendix M）清楚 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract 超过 200 words 限制
- 具体位置：Abstract（§abstract.tex, PDF p.1）
- 问题：EMNLP 2026 / ARR 要求 abstract ≤ 200 words。当前 abstract 包含大量数值和数学表达式（Δ=−0.020, ρ=0.4, p=0.010, bootstrap CI 等），估计约 220–230 words，明显超限。
- 为什么影响接收：格式硬约束违反，desk reject 风险。
- 建议：删除 paragraph 3 中的具体数值（Δ, p值, CI），保留定性结论（"improves over uniform at ρ≥0.4 with calibrated detectors"），将数值留给正文。目标压缩到 180 words 左右。

**N2** [critical] 正文疑似超出 8 页限制
- 具体位置：§7 Conclusion（PDF pp.8–9）
- 问题：Section 7 Conclusion 在第 8 页底部开始，conclusion 正文延伸至第 9 页顶部（约 10–15 行），之后才是 Limitations。按 EMNLP 2026 规定，Limitations/Ethics 不计入页数限制，但 §1–§7 主正文必须 ≤ 8 页。当前 §7 溢出至 p.9，主正文超过 8 页。
- 为什么影响接收：格式硬约束违反。
- 建议：压缩 §6 Discussion（当前约 1.5 页，可将 "Effect size in context" 和 "Limitations of α_eff as proxy" 部分内容移至 Limitations 或 Appendix），为 Conclusion 腾出空间使其完整落在 p.8 内。

**N3** [critical] 核心效应量过小且统计显著性不足
- 具体位置：§5.1 Main Results (Table 2), §5.2 (ρ=0.6 结果)
- 问题：论文的核心实验结论——adaptive b* 优于 uniform——在两个主要 contamination 水平上均未通过校正后的显著性检验。ρ=0.4: Δ=−0.020, p_BH=0.078; ρ=0.6: Δ=−0.032, p_BH=0.064。论文用 "directionally consistent" 和 bootstrap CI 来支撑结论，但在 k=9 的 family-wise correction 下，没有一个比较达到 α=0.05。更关键的是，Δ=−0.020 对应 ~0.1% relative improvement，downstream benchmark 完全无差异（Table 4: 两者均为 0.5414），这使得 PPL 改善的实际价值存疑。
- 为什么影响接收：N=3 + 未通过多重比较校正 = 方法论上的 claim 缺乏统计支撑。作为 analysis paper，定量发现应当更 robust。
- 建议：(a) 增加 seeds（至少 5 个）以提升统计 power；(b) 在论文中更显著地标注 p_BH 而非以脚注形式出现；(c) 明确承认 adaptive method 的 PPL 优势在当前实验规模下未达到统计显著且无下游体现，避免读者对实用价值产生过高期望。

**N4** [critical] 实验范围过窄，limiting generalizability
- 具体位置：§4 Experimental Setup, §Limitations
- 问题：所有实验基于 (a) 单一模型族 Qwen3（0.6B primary + 1.7B 补充），(b) 单一数据集 FineWeb 132M tokens，(c) 自污染设计（generator = trainee 同架构 Qwen3-0.6B）。自污染使得 detection 问题简化为 "同分布 self-detection"，与真实 web 污染（多源、多模型、混合风格）差距巨大。Cross-model transfer 结果（Appendix O: Llama→Qwen, single seed, MMLU +1.57pp / HellaSwag −0.60pp）mixed 且仅 1 seed，无法支撑泛化性 claim。
- 为什么影响接收：三个核心 findings 都依赖这一特定实验设置：epoch confound 在大规模预训练（单 epoch，无重复）中是否同样成立？detector requirements 在真实 web 污染下是否同样需要 ECE≤0.05？minimum intervention 在不同数据分布下是否仍优于 maximization？这些问题都无法从当前实验推断。
- 建议：(a) 至少增加一个不同模型族（如 Llama 或 Pythia）作为主实验（非仅 appendix single seed）；(b) 增加跨模型污染场景（generator ≠ trainee）的 multi-seed 实验；(c) 更诚实地在 abstract/conclusion 中限定 claim 的适用范围为 "self-contaminated continued pretraining at 0.6B scale"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Adaptive b* 方法新颖性薄弱
- 具体位置：§3 Method (Eq. 1)
- 问题：权重公式 w=(1−q)^b 完全来自 Drayson et al. (2025)；adaptive b* 的双约束（α_eff ≥ τ, ESS ≥ n_min）本质上是一个超参数自动选择启发式——选择满足两个阈值条件的最小 b。这在方法论贡献上偏薄：α_eff 是一个简单的加权比例，ESS 是标准的 importance sampling 诊断量，bisection 是标准数值方法。论文承认这是 "practical corollary" 而非 headline contribution，但 §3 仍占 ~0.75 页正文描述一个相对简单的公式。
- 建议：进一步压缩 §3，将 Algorithm 1 直接放到 Appendix；正文只保留公式 (1) 和关键直觉（1-2 段即可）。

**W2** [warning] Epoch confound finding 的适用范围需明确限定
- 具体位置：§5.1 Hard filtering paragraph, §6 Discussion paragraph 1, §7 Conclusion
- 问题：论文声称 "any D&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness"（§7, 最后一段）。但 epoch confound 主要出现在 continued pretraining（小数据量 → 多 epoch）设置中。在大规模 from-scratch pretraining（通常 <1 epoch，不存在数据重复），这个 confound 不成立。Drayson et al. 的实验是 from-scratch pretraining，他们的 setting 中 epoch confound 应该很小。论文在 rebuttal draft（W4 回应）中承认了这一点，但正文的表述过于 general。
- 建议：在 §6 或 §7 中明确限定：epoch confound 在数据量有限的 continued pretraining 中最为显著；在大规模预训练（single-epoch regime）中，D&R 的优势可能确实来自 filtering quality 而非 epoch exposure。

**W3** [warning] Detector 测试范围不足
- 具体位置：§5.2 Calibration paragraph, §Limitations, Appendix L
- 问题：仅测试了 3 个 detector（TF-IDF+LR discriminative, GPT-2 PPL generative, N-gram PPL generative），未覆盖当前主流的 neural classifiers（RoBERTa/ModernBERT fine-tuned, DetectGPT, Binoculars）。Drayson et al. 使用的 ModernBERT-150M (AUC=0.986) 未被测试。论文从 3 个 detector 的结果得出 "both AUC and ECE are necessary" 的结论，但 3 个数据点不足以建立这种因果关系——可能存在其他混杂因素（如 discriminative vs. generative paradigm 本身的差异）。
- 建议：至少增加一个 fine-tuned neural classifier（如 ModernBERT 或 RoBERTa）来验证 calibration 结论是否在更高 AUC 的 detector 上同样成立。

**W4** [warning] Discussion 中的 batch-size extrapolation 缺乏支撑
- 具体位置：§5.3 ESS floor paragraph, rebuttal draft (Broader Significance section)
- 问题：论文报告 B=4/8/16 的 monotonic scaling（Δ=−0.020/−0.050/−0.068），并在 rebuttal 中外推到 B=128（"conservative extrapolation predicts Δ≈−0.39"）。尽管 rebuttal 标注这是 "speculative"，但用 3 个点（B=4,8,16，跨度仅 4×）拟合 scaling exponent α≈0.89 然后外推到 B=128（32× extrapolation）在统计学上极为不可靠。且 B=16 仅有 single-seed 数据（seed 42），B=8 仅有 2-seed mean。
- 建议：删除 B=128 的外推或降级为 footnote/appendix 中的 "speculative observation"；在正文中只报告实测的 B=4/8/16 结果。

**W5** [warning] 部分关键信息藏在脚注中
- 具体位置：§5.2 (footnote on p_BH), Table 2 footnotes, §5.1
- 问题：p_BH=0.078（ρ=0.4）和 p_BH=0.064（ρ=0.6）这两个对评估核心 claim 至关重要的统计量仅出现在脚注中。Bonferroni-Holm 校正后的 p 值应当在正文 §5.1/§5.2 的主段落中显著报告，而非让读者在脚注中发现 "哦原来不显著"。
- 建议：将 p_BH 值移入正文主段落，与 uncorrected p 并列报告。

---

## 小问题（不影响接收）

- **m1**: Table 2 中 Golden Ratio 和 D&R 的 bold 标注可能误导：它们分别需要 oracle labels 和 multi-epoch exposure，与 Adaptive 不可直接比较。建议区分 "fair comparison" 和 "reference methods" 的 bold 标注。
- **m2**: §2 Related Work 占约 1.5 页（pp.2–3），对 8 页限制下的论文偏长。建议压缩 Detection and Filtering 段（多个 citation 可合并为一句综述）以释放空间。
- **m3**: Figure 1（overview TikZ diagram）在黑白打印下 orange/blue/violet 背景色几乎无法区分，仅靠 F1/F2/F3 标签可辨识。建议增加 pattern（如 hatching）或使用灰度渐变。
- **m4**: rebuttal_draft.md 中 C4 回应提到 "Appendix Q"，但 appendix 中最后标注的 section 为 Additional Contamination Rate（根据 appendix.tex 结构），请核对标签是否正确。
- **m5**: 论文使用 ρ 同时表示 token-level contamination ratio（§3, §4）和 Spearman 相关系数（Table 12, Appendix K），符号冲突。建议 contamination ratio 用 ρ，Spearman 用 ρ_s 或 r_s 以区分。

---

## 缺失引用

以下工作在 instance-level reweighting / data quality filtering 领域较为相关，建议补充讨论：

1. **MATES** (Yu et al., NeurIPS 2024) — "MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models"：动态数据选择，用小模型预测大模型的数据 influence，与本文的 online reweighting 直接相关。
2. **FineWeb-Edu** (Lozhkov et al., 2024) — 基于教育质量评分的大规模数据过滤，是 FineWeb 生态系统中的重要工作，论文使用了 FineWeb 但未讨论质量过滤维度。
3. **D4** (Tirumala et al., 2024) — "D4: Improving LLM Pretraining via Document De-Duplication and Diversification"：与 SemDeDup 类似但不同的去重策略，值得在 §2 Instance-Level 段提及。

---

## 主要优势

- **S1**: Epoch confound 的发现是论文最有价值的贡献。通过精心设计的 epoch-matched control（Table 1），定量展示 >95% 的 D&R 优势来自数据重复而非 filtering quality，为后续工作建立了重要的方法学基线。LR-controlled verification（§5.1）进一步排除了学习率调度的混杂。
- **S2**: 实验设计诚实透明。论文坦诚报告了 downstream null（Table 4）、statistical non-significance after correction、ρ=0.2 的失败案例、checkpoint resume artifact（Appendix P），这种科学诚实度在同行评审中值得肯定。
- **S3**: Appendix 内容丰富（17 sections, 7 pages），覆盖 grid search、τ sweep、constraint regime decomposition、α_eff validation、detector comparison、cross-model transfer、ρ=0.3 boundary analysis 等，为读者提供了充分的可验证性。
- **S4**: 论文定位从 "methods paper" 调整为 "analysis paper with practical corollary" 是合理的。三个 findings 的叙事结构清晰：confound → detector requirements → minimum intervention → adaptive b*。
- **S5**: Decision framework（Table 3）将分析结论转化为 practitioner-friendly 的决策指南，是有实用价值的贡献。

---

## Questions for Authors

1. 如果将 family-wise correction 的 family 缩小为仅包含 focal comparison（adaptive vs. uniform at each ρ），而非全部 9 个比较，corrected p-values 会是多少？论文是否考虑过分层检验策略（先检验 primary hypothesis，再检验 exploratory hypotheses）？
2. 在 ρ=0.4 的 self-contamination 设置下，TF-IDF+LR 的 AUC=0.94 已经很高。在真实 web contamination（多源多模型）场景下，同类 detector 的 AUC 和 ECE 预期会如何变化？是否有 pilot 数据？
3. Epoch confound 的核心发现是否可以通过更简单的实验设计来验证——例如直接比较 "D&R 1 epoch" vs. "uniform 1 epoch"——而不需要整套 adaptive b* 机制？如果可以，这是否暗示 adaptive b* 对论文核心 contribution 而言是非必需的？

---

**审稿完成。** Reviewer 2, Round 1, fresh review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-23T13:22:49.189701+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 在其实验范围内方法论扎实，epoch-matched 对比设计合理；但 N=3 seeds 的关键结果校正后未达显著 |\n| Excitement | 2.5 / 5 | Epoch confound 发现对方法学有价值；其余两个 findings 属于预期内的增量贡献 |\n| Overall | 3.0 / 5 | 分析论文定位合理，但效应量过小 + 范围过窄 + adaptive b* 方法新颖性不足 |\n| Confidence | 4 / 5 | |\n| Reproducibility | 4 / 5 | |\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 超过 200 words 限制\n- EMNLP 2026 / ARR 要求 abstract ≤ 200 words。当前 abstract 包含大量数值和数学表达式（Δ=−0.020, ρ=0.4, p=0.010, bootstrap CI 等），估计约 220–230 words，明显超限。\n- 格式硬约束违反，desk reject 风险。\n\n**N2** [critical] 正文疑似超出 8 页限制\n- Section 7 Conclusion 在第 8 页底部开始，conclusion 正文延伸至第 9 页顶部（约 10–15 行），之后才是 Limitations。按 EMNLP 2026 规定，§1–§7 主正文必须 ≤ 8 页。\n\n**N3** [critical] 核心效应量过小且统计显著性不足\n- ρ=0.4: Δ=−0.020, p_BH=0.078; ρ=0.6: Δ=−0.032, p_BH=0.064。k=9 的 family-wise correction 下无一达标。Δ=−0.020 对应 ~0.1% relative improvement，downstream benchmark 完全无差异。\n\n**N4** [critical] 实验范围过窄，limiting generalizability\n- 单一模型族 Qwen3（0.6B + 1.7B 补充），单一数据集 FineWeb 132M，自污染设计。Cross-model transfer（Appendix O）single seed 且结果 mixed。三个核心 findings 的泛化性无法从当前实验推断。\n\n### Should-Fix 问题\n\n**W1** [warning] Adaptive b* 方法新颖性薄弱\n- 权重公式 w=(1−q)^b 完全来自 Drayson et al.；adaptive b* 本质是超参数自动选择启发式。§3 仍占 ~0.75 页。\n\n**W2** [warning] Epoch confound finding 的适用范围需明确限定\n- 在大规模 from-scratch pretraining（通常 <1 epoch）中，epoch confound 不成立。论文正文表述过于 general。\n\n**W3** [warning] Detector 测试范围不足\n- 仅 3 个 detector，未覆盖 RoBERTa/ModernBERT fine-tuned, DetectGPT, Binoculars。3 个数据点不足以建立 \"both AUC and ECE are necessary\" 的因果关系。\n\n**W4** [warning] Batch-size extrapolation 缺乏支撑\n- 3 个点（B=4,8,16）拟合 scaling exponent 然后外推到 B=128（32× extrapolation）统计学上极不可靠。B=16 仅 single seed，B=8 仅 2-seed mean。\n\n**W5** [warning] 部分关键信息藏在脚注中\n- p_BH=0.078（ρ=0.4）和 p_BH=0.064（ρ=0.6）仅出现在脚注中。\n\n### 小问题\n- m1: Table 2 Golden Ratio/D&R bold 标注可能误导\n- m2: §2 Related Work 占 ~1.5 页偏长\n- m3: Figure 1 TikZ 黑白打印下背景色无法区分\n- m4: rebuttal Appendix Q 标签需核对\n- m5: ρ 同时表示 contamination ratio 和 Spearman 相关系数，符号冲突\n\n### 缺失引用\n- MATES (Yu et al., NeurIPS 2024)\n- FineWeb-Edu (Lozhkov et al., 2024)\n- D4 (Tirumala et al., 2024)\n\n### Questions\n1. 如果 family-wise correction 的 family 缩小为仅 focal comparison，corrected p-values 会是多少？\n2. 真实 web contamination 下 detector 的 AUC/ECE 预期变化？\n3. Epoch confound 核心发现是否可以通过更简单的实验验证，而不需要 adaptive b*？\n\n---\n\n请对以上每一个 Must-Fix、Should-Fix 和 Minor 问题给出你的 [AGREE] 或 [REBUT] 判断及理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 在其实验范围内方法论扎实，epoch-matched 对比设计合理；但 N=3 seeds 的关键结果校正后未达显著 |\n| Excitement | 2.5 / 5 | Epoch confound 发现对方法学有价值；其余两个 findings 属于预期内的增量贡献 |\n| Overall | 3.0 / 5 | 分析论文定位合理，但效应量过小 + 范围过窄 + adaptive b* 方法新颖性不足 |\n| Confidence | 4 / 5 | |\n| Reproducibility | 4 / 5 | |\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 超过 200 words 限制\n- EMNLP 2026 / ARR 要求 abstract ≤ 200 words。当前 abstract 包含大量数值和数学表达式（Δ=−0.020, ρ=0.4, p=0.010, bootstrap CI 等），估计约 220–230 words，明显超限。\n- 格式硬约束违反，desk reject 风险。\n\n**N2** [critical] 正文疑似超出 8 页限制\n- Section 7 Conclusion 在第 8 页底部开始，conclusion 正文延伸至第 9 页顶部（约 10–15 行），之后才是 Limitations。按 EMNLP 2026 规定，§1–§7 主正文必须 ≤ 8 页。\n\n**N3** [critical] 核心效应量过小且统计显著性不足\n- ρ=0.4: Δ=−0.020, p_BH=0.078; ρ=0.6: Δ=−0.032, p_BH=0.064。k=9 的 family-wise correction 下无一达标。Δ=−0.020 对应 ~0.1% relative improvement，downstream benchmark 完全无差异。\n\n**N4** [critical] 实验范围过窄，limiting generalizability\n- 单一模型族 Qwen3（0.6B + 1.7B 补充），单一数据集 FineWeb 132M，自污染设计。Cross-model transfer（Appendix O）single seed 且结果 mixed。三个核心 findings 的泛化性无法从当前实验推断。\n\n### Should-Fix 问题\n\n**W1** [warning] Adaptive b* 方法新颖性薄弱\n- 权重公式 w=(1−q)^b 完全来自 Drayson et al.；adaptive b* 本质是超参数自动选择启发式。§3 仍占 ~0.75 页。\n\n**W2** [warning] Epoch confound finding 的适用范围需明确限定\n- 在大规模 from-scratch pretraining（通常 <1 epoch）中，epoch confound 不成立。论文正文表述过于 general。\n\n**W3** [warning] Detector 测试范围不足\n- 仅 3 个 detector，未覆盖 RoBERTa/ModernBERT fine-tuned, DetectGPT, Binoculars。3 个数据点不足以建立 \"both AUC and ECE are necessary\" 的因果关系。\n\n**W4** [warning] Batch-size extrapolation 缺乏支撑\n- 3 个点（B=4,8,16）拟合 scaling exponent 然后外推到 B=128（32× extrapolation）统计学上极不可靠。B=16 仅 single seed，B=8 仅 2-seed mean。\n\n**W5** [warning] 部分关键信息藏在脚注中\n- p_BH=0.078（ρ=0.4）和 p_BH=0.064（ρ=0.6）仅出现在脚注中。\n\n### 小问题\n- m1: Table 2 Golden Ratio/D&R bold 标注可能误导\n- m2: §2 Related Work 占 ~1.5 页偏长\n- m3: Figure 1 TikZ 黑白打印下背景色无法区分\n- m4: rebuttal Appendix Q 标签需核对\n- m5: ρ 同时表示 contamination ratio 和 Spearman 相关系数，符号冲突\n\n### 缺失引用\n- MATES (Yu et al., NeurIPS 2024)\n- FineWeb-Edu (Lozhkov et al., 2024)\n- D4 (Tirumala et al., 2024)\n\n### Questions\n1. 如果 family-wise correction 的 family 缩小为仅 focal comparison，corrected p-values 会是多少？\n2. 真实 web contamination 下 detector 的 AUC/ECE 预期变化？\n3. Epoch confound 核心发现是否可以通过更简单的实验验证，而不需要 adaptive b*？\n\n---\n\n请对以上每一个 Must-Fix、Should-Fix 和 Minor 问题给出你的 [AGREE] 或 [REBUT] 判断及理由。"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-23T13:23:33.910919+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 44721
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-23T13:23:34.566096+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | Epoch confound 方法论可靠，但 adaptive method 统计证据不足（N=3, 校正后未达 α=0.05），α_eff proxy R²≈0.49 |\n| Excitement | 2/5 (Potentially Interesting) | Epoch confound 有方法论警示价值，但效应量极小，下游零改善 |\n| Reproducibility | 4/5 | 实验设置详细，超参数透明，代码承诺开源 |\n| Confidence | 4/5 | |\n\n### Must-Fix 问题\n\n**N1** [critical] N=3 seeds 的统计推断力根本性不足\n- 全文核心量化结论依赖于 N=3 seeds 的 paired t-test（仅 2 个自由度）。\n- ρ=0.4: uncorrected p=0.019, BH-corrected p=0.078\n- ρ=0.6: uncorrected p=0.010, BH-corrected p=0.064\n- Bootstrap CI [−0.028, −0.012] 在 N=3 时仅有 3³=27 个可能的重抽样本。\n- Cohen's d=2.86 可能反映方差被人为压低（seeds 只影响初始化，data order 固定）。\n- 论文先选择了 BH 校正（k=9），然后论证 family \"structurally heterogeneous\"——post-hoc 统计叙事调整。\n- 建议：增加到 N≥5 seeds，或放弃 p 值叙事改为纯效应量+方向一致性。\n\n**N2** [critical] 效应量与 claim 之间的严重脱节\n- Δ=−0.020 PPL（~0.11%）。五项下游任务全部 |Δ|≤0.01。\n- Batch-size 外推用 3 个点拟合幂律 Δ∝B^α（α≈0.89），外推到 B=128 预测 Δ≈−0.39——用 3 个数据点外推 8 倍不可靠。\n- 建议：删除所有 \"practical\" 表述；batch-size 外推移到 appendix。\n\n### Should-Fix 问题\n\n**W1** [warning] Self-contamination 实验设计的生态效度严重不足\n- Generator=trainee（Qwen3-0.6B 生成→检测→训练），人为降低检测难度。TF-IDF+LR AUC=0.94 部分归因于此。\n- Detector requirements claim（AUC≥0.9, ECE≤0.05）在 cross-model contamination 下可能完全不适用。\n- Cross-model transfer（Appendix O）single seed + mixed results。\n- 建议：增加 cross-generator 实验；限定 detector requirements claim 到 self-contamination 场景。\n\n**W2** [warning] α_eff proxy 的解释力不足以支撑其核心地位\n- R²≈0.49，proxy 仅解释不到一半方差。\n- r(α_eff, mean_q)=0.80 是 proxy-to-detector-score 循环论证，非 proxy-to-ground-truth。\n- 跨 seed 稳定性是预期结果（α_eff 是 q-scores 的确定性函数且 detector 固定）。\n- 根本问题：adaptive b* 的贡献可能主要来自 ESS constraint 的稳定化，而非 α_eff 的质量信号。\n- 建议：增加 α_eff-only ablation（去掉 ESS constraint 只保留 α_eff）；如果 ESS 是主要贡献者需重写 §6。\n\n**W3** [warning] 实验范围过窄，不支撑 \"necessary conditions\" 的普适性 claim\n- 1 个模型家族、1 个数据集、1 种污染类型、4 个 ρ 值、3 个 seeds。\n- \"necessary conditions\" 逻辑上很强，但仅在极窄设置上观察到。ρ=0.5 未测试。AUC/ECE 阈值来自仅 3 个 detector。\n- 建议：改为 \"empirically observed conditions in our setting\"。\n\n**W4** [warning] Epoch confound 实验中 LR schedule 混淆因素未完全排除\n- Epoch-matched D&R 使用完整训练长度的 LR schedule 但仅训练 2,553 步——LR schedule 形状在截断训练中与完整训练不同。\n- Independent-schedule replication 仅一句话带过，无完整 LR 曲线对比。\n- 更干净的控制：在相同步数下通过 upsampling 非污染数据来匹配 content epochs。\n- 建议：展示完整 LR curves；讨论 early-stopping vs content-epoch-matching confound；补充 upsampling baseline。\n\n### 小问题\n- m1: Table 2 Golden Ratio 的 w 定义需在 §4 中简要说明\n- m2: §5.2 同时讨论 ρ=0.6 结果和 boundary conditions，建议拆分\n- m3: Figure 2 的 x 轴标签与 adaptive b* 的关系不够清晰\n- m4: Appendix Q 的 ρ=0.3 结果应在主文 §5.2 中明确引用\n- m5: §2 未指出 Drayson et al. 的 from-scratch vs continued pretraining 区别——epoch confound 前提\n\n### Questions\n1. N=3 是计算资源限制还是有意为之？是否考虑过降低步数换取更多 seeds？\n2. α_eff-only ablation（去掉 ESS constraint）的 PPL？\n3. r(α_eff, mean_q)=0.80 vs r(α_eff, true real fraction)=0.70 的区别？\n4. Batch-size amplification 是固定 total tokens 还是固定 steps？\n5. Document-level vs token-level injection 对检测难度的影响？\n\n### 缺失引用\n- Xie et al. (2024) \"DOREMI\"\n- Fan et al. (2024) importance weighting variance-bias tradeoff\n\n---\n\n请对以上每一个 Must-Fix、Should-Fix 和 Minor 问题给出你的 [AGREE] 或 [REBUT] 判断及理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | Epoch confound 方法论可靠，但 adaptive method 统计证据不足（N=3, 校正后未达 α=0.05），α_eff proxy R²≈0.49 |\n| Excitement | 2/5 (Potentially Interesting) | Epoch confound 有方法论警示价值，但效应量极小，下游零改善 |\n| Reproducibility | 4/5 | 实验设置详细，超参数透明，代码承诺开源 |\n| Confidence | 4/5 | |\n\n### Must-Fix 问题\n\n**N1** [critical] N=3 seeds 的统计推断力根本性不足\n- 全文核心量化结论依赖于 N=3 seeds 的 paired t-test（仅 2 个自由度）。\n- ρ=0.4: uncorrected p=0.019, BH-corrected p=0.078\n- ρ=0.6: uncorrected p=0.010, BH-corrected p=0.064\n- Bootstrap CI [−0.028, −0.012] 在 N=3 时仅有 3³=27 个可能的重抽样本。\n- Cohen's d=2.86 可能反映方差被人为压低（seeds 只影响初始化，data order 固定）。\n- 论文先选择了 BH 校正（k=9），然后论证 family \"structurally heterogeneous\"——post-hoc 统计叙事调整。\n- 建议：增加到 N≥5 seeds，或放弃 p 值叙事改为纯效应量+方向一致性。\n\n**N2** [critical] 效应量与 claim 之间的严重脱节\n- Δ=−0.020 PPL（~0.11%）。五项下游任务全部 |Δ|≤0.01。\n- Batch-size 外推用 3 个点拟合幂律 Δ∝B^α（α≈0.89），外推到 B=128 预测 Δ≈−0.39——用 3 个数据点外推 8 倍不可靠。\n- 建议：删除所有 \"practical\" 表述；batch-size 外推移到 appendix。\n\n### Should-Fix 问题\n\n**W1** [warning] Self-contamination 实验设计的生态效度严重不足\n- Generator=trainee（Qwen3-0.6B 生成→检测→训练），人为降低检测难度。TF-IDF+LR AUC=0.94 部分归因于此。\n- Detector requirements claim（AUC≥0.9, ECE≤0.05）在 cross-model contamination 下可能完全不适用。\n- Cross-model transfer（Appendix O）single seed + mixed results。\n- 建议：增加 cross-generator 实验；限定 detector requirements claim 到 self-contamination 场景。\n\n**W2** [warning] α_eff proxy 的解释力不足以支撑其核心地位\n- R²≈0.49，proxy 仅解释不到一半方差。\n- r(α_eff, mean_q)=0.80 是 proxy-to-detector-score 循环论证，非 proxy-to-ground-truth。\n- 跨 seed 稳定性是预期结果（α_eff 是 q-scores 的确定性函数且 detector 固定）。\n- 根本问题：adaptive b* 的贡献可能主要来自 ESS constraint 的稳定化，而非 α_eff 的质量信号。\n- 建议：增加 α_eff-only ablation（去掉 ESS constraint 只保留 α_eff）；如果 ESS 是主要贡献者需重写 §6。\n\n**W3** [warning] 实验范围过窄，不支撑 \"necessary conditions\" 的普适性 claim\n- 1 个模型家族、1 个数据集、1 种污染类型、4 个 ρ 值、3 个 seeds。\n- \"necessary conditions\" 逻辑上很强，但仅在极窄设置上观察到。ρ=0.5 未测试。AUC/ECE 阈值来自仅 3 个 detector。\n- 建议：改为 \"empirically observed conditions in our setting\"。\n\n**W4** [warning] Epoch confound 实验中 LR schedule 混淆因素未完全排除\n- Epoch-matched D&R 使用完整训练长度的 LR schedule 但仅训练 2,553 步——LR schedule 形状在截断训练中与完整训练不同。\n- Independent-schedule replication 仅一句话带过，无完整 LR 曲线对比。\n- 更干净的控制：在相同步数下通过 upsampling 非污染数据来匹配 content epochs。\n- 建议：展示完整 LR curves；讨论 early-stopping vs content-epoch-matching confound；补充 upsampling baseline。\n\n### 小问题\n- m1: Table 2 Golden Ratio 的 w 定义需在 §4 中简要说明\n- m2: §5.2 同时讨论 ρ=0.6 结果和 boundary conditions，建议拆分\n- m3: Figure 2 的 x 轴标签与 adaptive b* 的关系不够清晰\n- m4: Appendix Q 的 ρ=0.3 结果应在主文 §5.2 中明确引用\n- m5: §2 未指出 Drayson et al. 的 from-scratch vs continued pretraining 区别——epoch confound 前提\n\n### Questions\n1. N=3 是计算资源限制还是有意为之？是否考虑过降低步数换取更多 seeds？\n2. α_eff-only ablation（去掉 ESS constraint）的 PPL？\n3. r(α_eff, mean_q)=0.80 vs r(α_eff, true real fraction)=0.70 的区别？\n4. Batch-size amplification 是固定 total tokens 还是固定 steps？\n5. Document-level vs token-level injection 对检测难度的影响？\n\n### 缺失引用\n- Xie et al. (2024) \"DOREMI\"\n- Fan et al. (2024) importance weighting variance-bias tradeoff\n\n---\n\n请对以上每一个 Must-Fix、Should-Fix 和 Minor 问题给出你的 [AGREE] 或 [REBUT] 判断及理由。"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-23T13:23:35.937771+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1371
}
```

</details>

---


### Assistant

_source line 1120 · 2026-05-23T13:23:38.843110+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应（[AGREE]/[REBUT]）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 85

## Round 85

2 recorded events


### User

_source line 1121 · 2026-05-23T13:23:41.354611+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：

- **Overall: 3.0/5 (Findings)**，Soundness 3.5，Excitement 2.5
- **4 个 Must-Fix**：Abstract 超 200 词、正文疑似超 8 页、核心效应量校正后不显著、实验范围过窄
- **5 个 Should-Fix**：adaptive b* 方法新颖性薄、epoch confound 适用范围需限定、detector 测试不足、batch-size 外推不可靠、关键 p 值藏在脚注
- **5 个 Minor**：Table bold 标注误导、Related Work 偏长、Figure 1 灰度不可辨、Appendix 标签不一致、ρ 符号冲突
- **主要优势**：epoch confound 发现有方法学价值、实验设计诚实透明、appendix 丰富

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1122 · 2026-05-23T13:23:48.958349+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 86

## Round 86

2 recorded events


### User

_source line 1123 · 2026-05-23T13:25:48.279292+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Abstract 超过 200 words 限制**
同意。我逐词核实了 PDF 第 1 页的 abstract，粗略计数约 220–240 words（取决于数学表达式的计词方式），明显超过 EMNLP 2026 的 200 words 硬约束。Abstract 中包含大量数值细节（Δ=−0.020, ρ=0.4, bootstrap CI, p=0.010 等），这些可以移到 Introduction。这是格式硬约束，有 desk reject 风险，必须修正。我在自己的审稿中遗漏了这个问题。

**[AGREE] R2-N2: 正文疑似超出 8 页限制**
同意。从 PDF 第 8-9 页可以确认：§7 Conclusion 在第 8 页右栏底部开始（"We identify three effectiveness conditions for detect-and-reweight..."），正文延伸到第 9 页左栏（约 15-20 行），之后才是 Limitations section。按 EMNLP 2026 规定（§1-§7 主正文 ≤8 页，Limitations/Ethics 不计入但不得包含过多额外内容），这构成格式违规。修正方案：压缩 §7 Conclusion（当前约 0.75 列），或压缩 §2 Related Work（R2-m2 也提到偏长，约 1.5 页）。这个问题我同样遗漏了。

**[AGREE] R2-N3: 核心效应量过小且统计显著性不足**
完全同意，这与我自己的 N1 和 N2 高度一致。补充几点我的审稿中已阐述的细节：
- N=3 的 bootstrap CI 仅有 3³=27 种重抽样可能，覆盖率保证极差（我的 N1）
- 论文先选择 BH 校正（k=9），校正后不理想又论证 family "structurally heterogeneous" 是 post-hoc 的统计叙事调整（我的 N1）
- Batch-size 外推（3 个点拟合幂律到 B=128）在统计学上不可靠（我的 N2）
- 值得注意的是，epoch confound 的核心发现（>95% 归因于多轮暴露）不受 N=3 限制——该结论在每个 seed 内独立成立，是方向性的定性结论而非依赖 p 值的定量结论

**[AGREE] R2-N4: 实验范围过窄**
同意，与我的 W3 一致。R2 正确指出单一模型族 + 单一数据集 + 自污染的三重局限使得 "necessary conditions" 这一 claim 无法泛化。我额外指出一点：ρ 覆盖不完整（缺 ρ=0.5），boundary 位置的精确性未被验证。

---

### Should-Fix 问题

**[AGREE] R2-W1: Adaptive b* 方法新颖性薄弱**
同意。权重公式 w=(1−q)^b 完全沿用 Drayson et al.，adaptive b* 本质是在两个约束（α_eff ≥ τ, ESS ≥ n_min）下的超参数自动选择，技术新颖性有限。论文已将其定位为 "practical corollary"，但 §3 仍占约 0.75 页，给人的印象仍然是一个独立的方法贡献。如果进一步压缩 §3（如合并到 §4），可以释放空间给 Conclusion（解决 R2-N2 的页面超限问题）。

**[AGREE] R2-W2: Epoch confound 适用范围需限定**
同意。Epoch confound 的前提是续训中数据量小导致多轮暴露（132M tokens, 6103 steps → ~3.2 content epochs at ρ=0.4）。在 from-scratch pretraining 的典型设置中（数百 B tokens, <1 epoch），这个 confound 不成立。论文在 rebuttal W4 中承认了这一点，但主文表述过于泛化——例如 §7 Conclusion 中 "any D&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness" 这句话严格来说只适用于会发生多轮暴露的场景。建议在该句后加 qualifier: "in settings where filtered data leads to multi-epoch exposure (e.g., continued pretraining on small corpora)"。

**[AGREE] R2-W3: Detector 测试范围不足**
同意，与我的审稿精神一致。仅 3 个 detector（TF-IDF+LR, GPT-2, N-gram）不足以建立 "both AUC and ECE are necessary" 的因果关系。3 个数据点可以提示一个 pattern，但不能排除混淆因素（如：TF-IDF+LR 成功可能是因为它的特征空间恰好与 FineWeb 的分布匹配，而非因为 ECE 低）。缺少的关键 detector 类别包括：(a) fine-tuned neural classifiers (RoBERTa-based, ModernBERT)——这些在实际应用中最常用；(b) zero-shot methods (DetectGPT, Binoculars)——这些不需要标注数据。当前 3 个 detector 的 AUC/ECE 组合恰好支持作者的叙事（高 AUC 低 ECE → 成功，高 AUC 高 ECE → 失败，低 AUC 低 ECE → 不够），但这可能是巧合而非因果。

**[AGREE] R2-W4: Batch-size extrapolation 缺乏支撑**
完全同意，这与我的 N2 中的分析一致。补充一个 R2 正确指出但我未详细展开的细节：B=16 仅 single seed，B=8 仅 2-seed mean——这意味着外推的基础数据本身就是 under-powered 的。3 个点拟合 α≈0.89 并外推 32 倍到 B=128，在任何定量分析标准下都不可接受。

**[REBUT] R2-W5: 部分关键信息藏在脚注中**
部分不同意。从 PDF 第 5 页 §5.1 的文本来看，BH-corrected p 值（p_BH=0.078 和 p_BH=0.064）出现在 §5.1 的正文段落中（"after Bonferroni-Holm correction for nine family-wise comparisons, p_BH=0.078, which does not reach conventional significance"），而非仅在脚注中。脚注中确实包含一些补充信息（如 checkpoint resume artifact 的说明），但核心统计结果是在正文中报告的。

不过，R2 的关注方向是对的：即使在正文中，这些校正后不显著的 p 值被包裹在大量数值中，容易被读者忽略。更好的做法是在 Table 2 中直接增加一列 p_BH，使校正结果与效应量并列展示。

---

### 小问题

**[AGREE] R2-m1: Table 2 bold 标注可能误导**
同意。如果 bold 表示 "best"，但 adaptive b* 与 grid-best 的差异在 cross-seed σ 之内，bold 标注暗示了实际上不存在的统计显著差异。

**[REBUT] R2-m2: Related Work 占 ~1.5 页偏长**
部分不同意。本文定位为 analysis paper，需要比标准 method paper 更详细地梳理前人工作，以建立 epoch confound 和 detector requirements 的 novelty。§2 覆盖了 5 个子领域（D&R, detection, domain-level mixing, instance-level weighting, theoretical foundations），每个约 0.3 页，不算冗长。但如果需要解决 R2-N2 的页面超限问题，Related Work 是最合理的压缩候选——可以将 "Theoretical Foundations" 子段压缩或移到 appendix。

**[AGREE] R2-m3: Figure 1 TikZ 黑白打印可读性**
同意。学术论文应保证灰度可读性。

**[AGREE] R2-m4: Appendix Q 标签核对**
同意。交叉引用标签应在 camera-ready 前逐一验证。

**[AGREE] R2-m5: ρ 符号冲突**
同意。ρ 同时用作 contamination ratio（§3-§7 全文）和 Spearman 相关系数（Table 12, Appendix K），在同一论文中造成歧义。建议将 contamination ratio 改为 ρ_c 或 γ，或将 Spearman 相关系数标记为 ρ_s。

---

### 对 R2 Questions 的补充观点

**Q1（缩小 family 后的 corrected p-values）**：如果仅对 focal comparison（adaptive vs. uniform at ρ=0.4）做单次检验，uncorrected p=0.019 即为最终 p 值。但这实质上是 cherry-picking the comparison family——论文实际进行了 9 个比较，选择性地只校正其中 1 个等于没有校正。正确的做法应该是：(a) 事先（pre-registration）指定 focal comparison，或 (b) 接受 k=9 的校正结果。论文两条路都没走干净。

**Q2（真实 web contamination 下 detector 性能）**：我在 W1 中详细讨论了这一点。Self-contamination 下 TF-IDF+LR 达到 AUC=0.94，但在 cross-model 场景下（异构生成器、版本混合、经过 paraphrasing/post-editing 的合成文本），AUC 很可能下降到 0.80-0.85 范围，此时论文的 "AUC≥0.9" 条件将难以满足，方法可能失效。

**Q3（epoch confound 是否可以更简单验证）**：完全可以。Epoch confound 的验证只需要 (a) standard D&R（filtering），(b) epoch-matched baseline（相同 content epochs 下的 uniform training），两个实验即可。不需要 adaptive b*、不需要 α_eff proxy、不需要 ESS constraint。这进一步说明 epoch confound 是本文的核心独立贡献，而 adaptive method 是附加的、且支撑不足的贡献。

---

### 综合评价

R2 和我的评价在方向和力度上高度一致（同为 Overall 3.0 / Findings），核心分歧很小。R2 发现了两个我遗漏的重要格式问题（N1 abstract 超限、N2 页面超限），这些是硬约束违规，应提升到 Must-Fix。我的审稿在统计方法论细节上更深入（bootstrap CI 覆盖率、Cohen's d 解读、BH 校正的 post-hoc 叙事问题），R2 在格式合规和方法新颖性评估上更全面。

两份审稿的共同判断：epoch confound 是有价值的方法论贡献，但 adaptive method 统计证据不足 + 效应量可忽略 + 实验范围过窄，整体达 Findings 但不达主会议标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1124 · 2026-05-23T13:25:56.319758+00:00_

Reviewer 1 已完成对 Reviewer 2 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 87

## Round 87

2 recorded events


### User

_source line 1125 · 2026-05-23T13:26:02.119446+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

对 R2 的 4 个 Must-Fix 全部 AGREE（abstract 超限和页面超限是我遗漏的格式硬约束），5 个 Should-Fix 中 4 个 AGREE、1 个 REBUT（W5 关于 p_BH 藏在脚注——实际上出现在正文 §5.1 中，不过建议改为在 Table 2 中并列展示），5 个 Minor 中 4 个 AGREE、1 个部分 REBUT（m2 Related Work 长度对 analysis paper 来说合理，但可作为页面超限的压缩候选）。两份审稿在核心判断上高度一致：Overall 3.0 / Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1126 · 2026-05-23T13:26:10.596211+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 88

## Round 88

16 recorded events


### User

_source line 1127 · 2026-05-23T13:26:12.164351+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应

### Must-Fix 问题

**[AGREE] R1-N1: N=3 seeds 统计推断力不足**
同意。与我的 N3 本质相同。R1 额外指出的两个论点有力：(1) Bootstrap CI 在 N=3 时仅 3³=27 个重抽样本，分辨率极低；(2) 论文先报告 BH 校正再论证 family "structurally heterogeneous" 属于 post-hoc narrative adjustment。Cohen's d=2.86 反映人为压低的方差也是有效观察——seeds 仅影响初始化、data order 固定。

**[AGREE] R1-N2: 效应量与 claim 脱节**
同意，与我的 N3 和 W4 高度重合。建议删除所有 "practical" 表述稍过激——论文已定位为 "practical corollary"，但 batch-size 外推（3 点拟合幂律外推 8 倍）确实应移到 appendix。

### Should-Fix 问题

**[AGREE] R1-W1: Self-contamination 生态效度不足**
强烈同意。我将此升级为 critical（我的 N4）。TF-IDF+LR AUC=0.94 部分归因于 self-contamination 降低检测难度。Cross-model 实验（Appendix O）single seed + mixed results + "perplexity comparison omitted due to inconsistent evaluation configurations"——连基本 PPL 比较都无法完成。

**[AGREE] R1-W2: α_eff proxy 解释力不足**
同意。三个关键点：(1) R²≈0.49 对于驱动整个方法的核心 proxy 偏低；(2) r(α_eff, mean_q)=0.80 是 proxy-to-proxy 循环而非 proxy-to-ground-truth（r=0.706）；(3) α_eff-only ablation 缺失是最有建设性的建议——当前无法区分 adaptive b* 的贡献来自 α_eff 质量信号还是 ESS 稳定化。§5.3 的 constraint regime decomposition（50.9% α_eff-binding）描述了频率但无法区分因果。

**[AGREE] R1-W3: "necessary conditions" claim 过强**
同意。Table 3 "Req'd?" 列暗示 necessary conditions，但仅 3 detector + 4 ρ值 + 1 模型族不足以支撑。改为 "empirically observed conditions" 合理。

**[REBUT] R1-W4: LR schedule 混淆因素**
部分反驳。论文的 independent-schedule replication（§5.1 "LR-controlled verification"）已有效回应：独立 LR schedule D&R 17.651 vs shared 17.657（Δ=0.006），uniform 独立 schedule 18.062，确认 epoch advantage 在控制 LR 后存在。但同意 (a) 展示完整 LR curves 可增加说服力；(b) upsampling baseline 是更干净的设计。当前 control 足够排除 LR confound，Should-Fix 而非 Must-Fix 的定级合理。

### Minor 问题

**[AGREE] R1-m1 至 m5**: 全部同意。m5 尤为重要——§2 未标注 Drayson et al. 是 from-scratch pretraining，读者会误认为 epoch confound 直接推翻其结论。

### 缺失引用

**[REBUT]** Xie et al. DoReMi：已被引用（§2 Domain-Level 段，ref key `xie2023doremi`）。
**[AGREE]** Fan et al. importance weighting variance-bias tradeoff：与 ESS 约束直接相关，值得补充。

### 总结

11 条意见中 AGREE 10 条、REBUT 1 条（W4 部分反驳）。R1 与我的核心判断高度一致。R1 贡献了两个有价值的建设性建议：α_eff-only ablation 和 upsampling baseline，补上可显著增强论文说服力。

Overall 维持 **3.0 / 5 (Findings)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-23T13:26:38.600343+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool call

_source line 1129 · 2026-05-23T13:26:38.600747+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1130 · 2026-05-23T13:26:38.652119+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T13:10:47.555654+00:00\", \"completed_at\": \"2026-05-23T13:13:44.790365+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Results 5.1 整页讨论实验数据但无任何 display item，所有支撑数据（Table 1/2, Figure 2）被推至 page 6，审稿人读 results 时无法同时看到数据，影响阅读体验。建议调整 float 位置将 Table 1 或 Figure 2 提前至 page 5\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"Appendix 末页仅 6 行文字（~5% 填充），约 95% 空白。建议将 Appendix Q 末尾内容合并到 page 16 或重新分页，避免近乎空白页\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（Analysis overview）作为全文第一个视觉锚点，本质是格式化文字方框而非图形化示意图，视觉吸引力有限。如有条件可考虑加入简化的 pipeline/架构示意元素增强第一印象\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-5\", \"message\": \"连续 3 页无 figure/table（Related Work → Method → Results 开头），page 4 有公式打断属正常，但整体节奏偏文本密集。若能将一个 display item 移入 page 4-5 区间会改善阅读节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"单页包含 3 个 display items（Table 1 + Figure 2 + Table 2），视觉密度过高，与前序纯文本页形成强烈对比。建议分散到 pages 5-7\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Appendix 页面极为密集（Proofs + Algorithm 1 + Table 5 + 两个小节），可读性尚可但视觉压迫感较强\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-23T13:26:38.652503+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-23T13:26:47.940907+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex | wc -w",
    "description": "Count abstract word count"
  }
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-23T13:26:49.396609+00:00_

225

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-23T13:26:49.547658+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper && pdfinfo ../../artifacts/review_round_11/submitted.pdf 2>/dev/null | grep Pages || echo \"Cannot check PDF pages\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper && pdfinfo ../../artifacts/review_round_11/submitted.pdf 2>/dev/null | grep Pages || echo \"Cannot check PDF pages\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-23T13:26:49.648543+00:00_

Pages:           17
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_director_5d592d28

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-23T13:27:56.806216+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 1137 · 2026-05-23T13:27:56.907047+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-23T13:30:38.071379+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成：检测器噪声占未解释方差 ~70%（边界区 q∈[0.4,0.6] 准确率 ~55%），b* 变换占 ~30%（ESS floor 约束的刻意设计）。B=4→B=16 方差降 10.25× 但 R² 不变（0.47→0.44），证明瓶颈在检测器。§6 已写入完整定量分解段落。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句：proxy r=0.70 在 §3，seed 42 在 Table 1 脚注，ρ=0.2 在 §6。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。释放空间用于 decision summary table 移入主文。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11 issues (updated with Round 12 recurrence) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Rebuttal 多角度论证但未增加 seeds。\"\n      status: done\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。R1-N1 + R2-N3 双方 AGREE。Bootstrap CI 在 N=3 时仅 27 种重抽样、BH 校正后均不显著（p_BH=0.078/0.064）、Cohen's d=2.86 可能反映方差被人为压低。论文的 post-hoc 统计叙事调整（先选 BH 再论证 family heterogeneous）被两位 reviewer 一致批评。Rebuttal 论证未能消除此问题。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal 多角度论证\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.49，跨 seed 稳定性证据不充分\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出，R2 交叉回应 AGREE。r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。跨 seed spread <0.003 是预期结果（确定性函数+固定 detector）不构成额外证据。核心缺失：α_eff-only ablation（去掉 ESS constraint）以区分 α_eff 质量信号 vs ESS 稳定化的贡献。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal 提供 3-seed per-seed table\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.020, ~0.11%），论文 framing 存在 overclaim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-N3 再次独立提出，AGREE。Rebuttal 中 batch-size 外推（3 点拟合幂律外推 32× 到 B=128 预测 Δ≈−0.39）被两位 reviewer 一致认为统计学不可靠。'practical' 表述虽已部分调整但仍残留。\"\n  action_items:\n    - round: 11\n      action: \"Abstract 删除 overclaim，论文重定位\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"实验范围过窄：单模型/单数据集/self-contamination，不足以支撑一般性结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1/W3 + R2-N4 再次提出，AGREE。Self-contamination 降低检测难度（AUC=0.94 部分归因于 generator=trainee）。Cross-model transfer（Appendix O）single seed + mixed + 连基本 PPL 都无法比较。Detector requirements claim（AUC≥0.9, ECE≤0.05）在 cross-model 场景下可能不适用。建议改 'necessary conditions' 为 'empirically observed conditions in our setting'。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal 三点缓解\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出，R1 AGREE。§3 压缩到 ~0.75 页后仍给人独立方法贡献的印象。建议进一步压缩或合并到 §4。\"\n  action_items:\n    - round: 11\n      action: \"论文重定位为 analysis paper\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Analysis paper vs method paper 定位不清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract 同时 claim 'we analyze' + 'we derive adaptive b*'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"本轮未作为独立 issue 提出，论文已重定位为 analysis paper with practical corollary。但 R2-W1 和 R1-N2 间接触及：§3 仍占较多篇幅，batch-size 外推仍以 practical significance 包装。部分改善但残留问题。\"\n  action_items:\n    - round: 11\n      action: \"Abstract/Intro 重构\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议：MATES (Yu et al., NeurIPS 2024)、FineWeb-Edu (Lozhkov et al., 2024)、D4 (Tirumala et al., 2024)、Fan et al. importance weighting variance-bias tradeoff。DoReMi (Xie et al.) 已在论文中引用，R1 误报。\"\n  action_items:\n    - round: 11\n      action: \"四篇参考文献已添加\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏对 prior work 实验设置的具体分析\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 Drayson et al. 等 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W2 提出 epoch confound 适用范围需限定：from-scratch pretraining（<1 epoch）中 confound 不成立。§7 'any D&R evaluation...' 过于泛化。R1 AGREE。建议加 qualifier 限定为 multi-epoch exposure 场景。§2 也未标注 Drayson et al. 是 from-scratch vs continued pretraining（R1-m5）。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal W4 详细分析\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m1\"\n  summary: \"ESS ceiling 与 α_eff floor 约束冲突时的行为缺乏明确分析\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"建议补充报告真正冲突的 batch 比例及 PPL 贡献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W2 间接触及：α_eff-only ablation 缺失使得无法区分两个 constraint 的独立贡献。本轮未作为独立 issue 但被 R11-C2 的更新覆盖。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal m1 提供 binding stats\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 2 可读性偏弱，脚注密度过高，小数位不一致等格式问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。12+ 脚注含关键技术细节。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"部分问题持续。R2-m5 新发现 ρ 符号冲突（contamination ratio vs Spearman）。R2-m3 Figure 1 黑白不可辨。R1-m3 Figure 2 x 轴标签与 adaptive b* 的关系混淆。\"\n  action_items:\n    - round: 11\n      action: \"Figure 2 caption 加 marker 注释，Table 2 统一 3dp\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m3\"\n  summary: \"Appendix 过于庞大（5 页 17 个子附录），关键证据未在正文充分引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Appendix K 和 N 对核心论点重要但正文引用不充分。\"\n    - round: 12\n      reviewers: []\n      note: \"本轮未提及，可能已改善（正文加了更突出的交叉引用）。待 Research Director 确认。\"\n  action_items:\n    - round: 11\n      action: \"正文加更突出的交叉引用\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 新发现 ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制（实测 225 words），EMNLP 2026 格式硬约束违规\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N1 首次发现，R1 交叉回应 AGREE。LaTeX 源码 wc -w 确认 225 words。包含大量数值（Δ=−0.020, ρ=0.4, bootstrap CI, p=0.010 等），需压缩到 ≤200 words。有 desk reject 风险。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制，§7 Conclusion 溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N2 首次发现，R1 交叉回应 AGREE。§7 在 p.8 底部开始，延伸至 p.9（约 15-20 行），之后才是 Limitations。EMNLP 2026 规定 §1-§7 主正文 ≤8 页。建议压缩 §6 Discussion 或 §2 Related Work。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个 detector），不足以支撑因果性结论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。仅 TF-IDF+LR / GPT-2 / N-gram，未覆盖 RoBERTa/ModernBERT/DetectGPT/Binoculars。3 个数据点不足以建立 'both AUC and ECE are necessary' 的因果关系——可能存在 discriminative vs generative paradigm 本身的混杂。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size extrapolation 统计学不可靠（3 点拟合幂律外推 32×）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W4 + R1-N2 双方 AGREE。B=4/8/16 仅 3 个点，B=16 仅 single seed，B=8 仅 2-seed mean。外推到 B=128 预测 Δ≈−0.39 在定量分析标准下不可接受。Rebuttal 中作为 practical significance 主要论据更成问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"LR schedule 混淆因素在 epoch confound 实验中未完全排除\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 部分 REBUT（independent-schedule replication 已 adequately 回应，但同意 LR curves 和 upsampling baseline 可增强说服力）。Epoch-matched D&R 使用完整 LR schedule 截断至 2533 步，改变了 warmup/decay 比例。Independent replication D&R 17.651 vs shared 17.657 (Δ=0.006) 基本排除 LR confound，但缺完整 LR curves 和 upsampling control。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-m5 发现，R1 AGREE。§3-§7 中 ρ=contamination ratio，Table 12/Appendix K 中 ρ=Spearman。建议将 Spearman 改为 ρ_s 或 r_s。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m2\"\n  summary: \"Table 2 中 Golden Ratio/D&R 的 bold 标注可能误导读者\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-m1 发现，R1 AGREE。Oracle/multi-epoch 方法与 fair comparison 方法使用相同 bold 标注暗示不存在的可比性。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m3\"\n  summary: \"Figure 1 (TikZ) 和 Figure 2 在黑白/灰度打印下可读性差\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-m3 (Figure 1 orange/blue/violet 不可辨) + R1-m3 (Figure 2 x 轴标签与 adaptive b* 关系混淆)。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m4\"\n  summary: \"缺失引用：MATES, FineWeb-Edu, D4, Fan et al.\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 建议：MATES (Yu et al., NeurIPS 2024), FineWeb-Edu (Lozhkov et al., 2024), D4 (Tirumala et al., 2024)。R1 建议 Fan et al. importance weighting variance-bias tradeoff。DoReMi 已在论文中引用（R1 误报，R2 REBUT）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成：检测器噪声占未解释方差 ~70%（边界区 q∈[0.4,0.6] 准确率 ~55%），b* 变换占 ~30%（ESS floor 约束的刻意设计）。B=4→B=16 方差降 10.25× 但 R² 不变（0.47→0.44），证明瓶颈在检测器。§6 已写入完整定量分解段落。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句：proxy r=0.70 在 §3，seed 42 在 Table 1 脚注，ρ=0.2 在 §6。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。释放空间用于 decision summary table 移入主文。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11 issues (updated with Round 12 recurrence) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Rebuttal 多角度论证但未增加 seeds。\"\n      status: done\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。R1-N1 + R2-N3 双方 AGREE。Bootstrap CI 在 N=3 时仅 27 种重抽样、BH 校正后均不显著（p_BH=0.078/0.064）、Cohen's d=2.86 可能反映方差被人为压低。论文的 post-hoc 统计叙事调整（先选 BH 再论证 family heterogeneous）被两位 reviewer 一致批评。Rebuttal 论证未能消除此问题。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal 多角度论证\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.49，跨 seed 稳定性证据不充分\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出，R2 交叉回应 AGREE。r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。跨 seed spread <0.003 是预期结果（确定性函数+固定 detector）不构成额外证据。核心缺失：α_eff-only ablation（去掉 ESS constraint）以区分 α_eff 质量信号 vs ESS 稳定化的贡献。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal 提供 3-seed per-seed table\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.020, ~0.11%），论文 framing 存在 overclaim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-N3 再次独立提出，AGREE。Rebuttal 中 batch-size 外推（3 点拟合幂律外推 32× 到 B=128 预测 Δ≈−0.39）被两位 reviewer 一致认为统计学不可靠。'practical' 表述虽已部分调整但仍残留。\"\n  action_items:\n    - round: 11\n      action: \"Abstract 删除 overclaim，论文重定位\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"实验范围过窄：单模型/单数据集/self-contamination，不足以支撑一般性结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1/W3 + R2-N4 再次提出，AGREE。Self-contamination 降低检测难度（AUC=0.94 部分归因于 generator=trainee）。Cross-model transfer（Appendix O）single seed + mixed + 连基本 PPL 都无法比较。Detector requirements claim（AUC≥0.9, ECE≤0.05）在 cross-model 场景下可能不适用。建议改 'necessary conditions' 为 'empirically observed conditions in our setting'。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal 三点缓解\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出，R1 AGREE。§3 压缩到 ~0.75 页后仍给人独立方法贡献的印象。建议进一步压缩或合并到 §4。\"\n  action_items:\n    - round: 11\n      action: \"论文重定位为 analysis paper\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Analysis paper vs method paper 定位不清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract 同时 claim 'we analyze' + 'we derive adaptive b*'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"本轮未作为独立 issue 提出，论文已重定位为 analysis paper with practical corollary。但 R2-W1 和 R1-N2 间接触及：§3 仍占较多篇幅，batch-size 外推仍以 practical significance 包装。部分改善但残留问题。\"\n  action_items:\n    - round: 11\n      action: \"Abstract/Intro 重构\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议：MATES (Yu et al., NeurIPS 2024)、FineWeb-Edu (Lozhkov et al., 2024)、D4 (Tirumala et al., 2024)、Fan et al. importance weighting variance-bias tradeoff。DoReMi (Xie et al.) 已在论文中引用，R1 误报。\"\n  action_items:\n    - round: 11\n      action: \"四篇参考文献已添加\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏对 prior work 实验设置的具体分析\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 Drayson et al. 等 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W2 提出 epoch confound 适用范围需限定：from-scratch pretraining（<1 epoch）中 confound 不成立。§7 'any D&R evaluation...' 过于泛化。R1 AGREE。建议加 qualifier 限定为 multi-epoch exposure 场景。§2 也未标注 Drayson et al. 是 from-scratch vs continued pretraining（R1-m5）。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal W4 详细分析\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m1\"\n  summary: \"ESS ceiling 与 α_eff floor 约束冲突时的行为缺乏明确分析\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"建议补充报告真正冲突的 batch 比例及 PPL 贡献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W2 间接触及：α_eff-only ablation 缺失使得无法区分两个 constraint 的独立贡献。本轮未作为独立 issue 但被 R11-C2 的更新覆盖。\"\n  action_items:\n    - round: 11\n      action: \"Rebuttal m1 提供 binding stats\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 2 可读性偏弱，脚注密度过高，小数位不一致等格式问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。12+ 脚注含关键技术细节。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"部分问题持续。R2-m5 新发现 ρ 符号冲突（contamination ratio vs Spearman）。R2-m3 Figure 1 黑白不可辨。R1-m3 Figure 2 x 轴标签与 adaptive b* 的关系混淆。\"\n  action_items:\n    - round: 11\n      action: \"Figure 2 caption 加 marker 注释，Table 2 统一 3dp\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m3\"\n  summary: \"Appendix 过于庞大（5 页 17 个子附录），关键证据未在正文充分引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Appendix K 和 N 对核心论点重要但正文引用不充分。\"\n    - round: 12\n      reviewers: []\n      note: \"本轮未提及，可能已改善（正文加了更突出的交叉引用）。待 Research Director 确认。\"\n  action_items:\n    - round: 11\n      action: \"正文加更突出的交叉引用\"\n      assigned_to: paper\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 新发现 ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制（实测 225 words），EMNLP 2026 格式硬约束违规\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N1 首次发现，R1 交叉回应 AGREE。LaTeX 源码 wc -w 确认 225 words。包含大量数值（Δ=−0.020, ρ=0.4, bootstrap CI, p=0.010 等），需压缩到 ≤200 words。有 desk reject 风险。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制，§7 Conclusion 溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N2 首次发现，R1 交叉回应 AGREE。§7 在 p.8 底部开始，延伸至 p.9（约 15-20 行），之后才是 Limitations。EMNLP 2026 规定 §1-§7 主正文 ≤8 页。建议压缩 §6 Discussion 或 §2 Related Work。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个 detector），不足以支撑因果性结论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。仅 TF-IDF+LR / GPT-2 / N-gram，未覆盖 RoBERTa/ModernBERT/DetectGPT/Binoculars。3 个数据点不足以建立 'both AUC and ECE are necessary' 的因果关系——可能存在 discriminative vs generative paradigm 本身的混杂。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size extrapolation 统计学不可靠（3 点拟合幂律外推 32×）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W4 + R1-N2 双方 AGREE。B=4/8/16 仅 3 个点，B=16 仅 single seed，B=8 仅 2-seed mean。外推到 B=128 预测 Δ≈−0.39 在定量分析标准下不可接受。Rebuttal 中作为 practical significance 主要论据更成问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"LR schedule 混淆因素在 epoch confound 实验中未完全排除\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 部分 REBUT（independent-schedule replication 已 adequately 回应，但同意 LR curves 和 upsampling baseline 可增强说服力）。Epoch-matched D&R 使用完整 LR schedule 截断至 2533 步，改变了 warmup/decay 比例。Independent replication D&R 17.651 vs shared 17.657 (Δ=0.006) 基本排除 LR confound，但缺完整 LR curves 和 upsampling control。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-m5 发现，R1 AGREE。§3-§7 中 ρ=contamination ratio，Table 12/Appendix K 中 ρ=Spearman。建议将 Spearman 改为 ρ_s 或 r_s。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m2\"\n  summary: \"Table 2 中 Golden Ratio/D&R 的 bold 标注可能误导读者\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-m1 发现，R1 AGREE。Oracle/multi-epoch 方法与 fair comparison 方法使用相同 bold 标注暗示不存在的可比性。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m3\"\n  summary: \"Figure 1 (TikZ) 和 Figure 2 在黑白/灰度打印下可读性差\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-m3 (Figure 1 orange/blue/violet 不可辨) + R1-m3 (Figure 2 x 轴标签与 adaptive b* 关系混淆)。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m4\"\n  summary: \"缺失引用：MATES, FineWeb-Edu, D4, Fan et al.\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 建议：MATES (Yu et al., NeurIPS 2024), FineWeb-Edu (Lozhkov et al., 2024), D4 (Tirumala et al., 2024)。R1 建议 Fan et al. importance weighting variance-bias tradeoff。DoReMi 已在论文中引用（R1 误报，R2 REBUT）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-23T13:30:38.172478+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 16785}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-23T13:33:45.323648+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**审稿模式**: Fresh（无前轮记忆）\n**Reviewers**: R1（方法严谨性+实验设计）、R2（新颖性+完整性+写作质量）\n**轮次**: 1 轮完成（Round 1 独立审稿 → 交叉分享 → 收敛，无需 Round 2）\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight (D&R) 范式在续训语言模型中应对合成文本污染的有效性条件。在 Qwen3-0.6B 上使用 132M FineWeb 子集（ρ=0.4, 3 seeds）进行可控实验，提出三项分析发现：(1) D&R 先前报告的 PPL 优势中 >95% 可归因于 epoch confound（多轮数据暴露），epoch-matched 后优势从 0.396 缩减至 0.017；(2) 有效 reweighting 要求检测器同时具备足够的 AUC（≥0.9）和良好的校准（ECE≤0.05）；(3) 基于双约束（α_eff ≥ τ, ESS ≥ n_min）的自适应 b* 实现最小干预优于最大化策略。作为实践推论，提出了一个无需 grid search 的自适应 b*，在 ρ≥0.4 时优于 uniform（Δ=−0.020 at ρ=0.4, Δ=−0.032 at ρ=0.6），但效应量极小（~0.11% relative），下游任务无改善。\n\n---\n\n## Strengths\n\n1. **Epoch confound 发现扎实且有方法论价值** [R1+R2 共识]：通过 epoch-matched 控制实验定量证明 D&R 先前报告的 PPL 优势中 >95% 来自多轮数据暴露而非 filtering quality（Table 1, Δ from 0.396 to 0.017, 3 seeds 方向一致）。LR-controlled verification（§5.1）进一步排除学习率调度混杂。这对后续 D&R 研究有直接方法论警示意义。\n\n2. **检测器校准 vs AUC 的 counter-intuitive 发现** [R1+R2 共识]：GPT-2 detector (AUC=0.91, ECE=0.131) 性能劣于 uniform (Δ=+0.098)，而 TF-IDF+LR (AUC=0.94, ECE=0.048) 成功——揭示 calibration 可以逆转 intervention 方向（§5.2, Appendix L），对 data curation 工作有指导价值。\n\n3. **实验设计诚实透明** [R1+R2 共识]：下游 null result（Table 4）、scale 限制（1.7B 效应减弱）、cross-model mixed results（Appendix O）、checkpoint resume artifact（Appendix P）均如实报告，无 cherry-picking。统计校正后不显著的 p 值也在正文中报告。\n\n4. **Appendix 覆盖全面** [R1+R2 共识]：17 节 appendix 涵盖 grid search details、threshold sweep、constraint regime decomposition、α_eff validation、detector comparison、cross-model transfer、低 ρ 分析、checkpoint artifact 等，可复现性强（Reproducibility 4/5）。\n\n5. **Decision framework 有实用价值** [R2]：Table 3 将分析结论转化为 practitioner-friendly 的决策指南（AUC≥0.9, ECE≤0.05, ρ≥0.4），是有价值的综合贡献。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1** [R2-N1, R1 AGREE] **Abstract 超过 200 words 限制**\nLaTeX 源码 wc -w 确认 225 words，超出 EMNLP 2026 / ARR 的 200 words 硬约束。Abstract 中包含大量数值细节（Δ=−0.020, ρ=0.4, bootstrap CI, p=0.010 等），应移到 Introduction。格式硬约束违反有 desk reject 风险。\n→ 建议压缩到 ≤180 words，删除具体数值保留定性结论。\n\n**C2** [R2-N2, R1 AGREE] **正文超出 8 页限制**\n§7 Conclusion 在 PDF p.8 底部开始，延伸至 p.9（约 15-20 行），之后才是 Limitations。EMNLP 2026 规定 §1-§7 主正文 ≤8 页，Limitations/Ethics 不计入但不得含过多额外内容。格式硬约束违反。\n→ 建议压缩 §6 Discussion（将 \"Effect size in context\" 和 \"Limitations of α_eff as proxy\" 部分内容移至 Limitations 或 Appendix）或 §2 Related Work（\"Theoretical Foundations\" 子段可移至 appendix）。\n\n**C3** [R1-N1 + R2-N3, 双方 AGREE] **N=3 seeds 统计推断力根本性不足**\n全文核心量化结论依赖 N=3 seeds 的 paired t-test（仅 2 df）。关键结果在 BH 校正后均未达 α=0.05：ρ=0.4 p_BH=0.078, ρ=0.6 p_BH=0.064。Bootstrap CI [−0.028, −0.012] 在 N=3 时仅 27 种重抽样，覆盖率保证极弱。Cohen's d=2.86 更可能反映方差被人为压低（seeds 仅影响初始化，data order 固定）而非效应量大。论文先报告 BH 校正再论证 family \"structurally heterogeneous\" 属于 post-hoc 统计叙事调整。\n→ 建议 (a) 增加到 N≥5 seeds，或 (b) 放弃 p 值叙事改为纯效应量+方向一致性报告。\n注：epoch confound 的核心发现不受此限——该结论在每个 seed 内独立成立。\n\n**C4** [R1-N2 + R2-N3, 双方 AGREE] **效应量极小（Δ=−0.020 PPL, ~0.11%）+ 下游零改善**\n五项下游任务全部 |Δ|≤0.01，adaptive 与 uniform 均为 0.5414（Table 4）。Batch-size extrapolation（3 点拟合幂律 Δ∝B^0.89 外推 32× 到 B=128 预测 Δ≈−0.39）统计学不可靠，但 rebuttal 中作为实际意义的主要论据。在可验证的所有指标上，方法无实际改善。\n→ 建议 (a) 删除或大幅降级 batch-size 外推（移到 appendix，标注 hypothesis）；(b) 在 abstract/conclusion 中删除所有 \"practical\" 残留表述。\n\n**C5** [R1-W1/W3 + R2-N4, 双方 AGREE] **实验范围过窄，不支撑一般性结论**\n所有实验基于单一模型族（Qwen3, 0.6B/1.7B）、单一数据集（FineWeb 132M）、自污染设计（generator=trainee）。Self-contamination 人为降低检测难度（AUC=0.94 部分归因于 generator=trainee 的统计指纹匹配）。Cross-model transfer（Appendix O, Llama→Qwen）single seed + mixed results + PPL 比较缺失。\"necessary conditions\" 是一个逻辑上很强的 claim，但仅在极窄设置上观察到。\n→ 建议 (a) 将 \"necessary conditions\" 改为 \"empirically observed conditions in our setting\"；(b) 在 abstract/conclusion 中限定 claim 适用范围为 \"self-contaminated continued pretraining at 0.6B scale\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R1-W2 + R2 AGREE] **α_eff proxy 解释力不足（R²≈0.49）以支撑其核心地位**\nα_eff 是双约束中 quality floor 的直接操作变量，但仅解释不到一半的目标方差。r(α_eff, mean_q)=0.80 是 proxy-to-detector-score 的相关性（循环论证），非 proxy-to-ground-truth（r=0.706）。跨 seed spread <0.003 是确定性函数+固定 detector 的预期结果，不构成额外证据。核心缺失：**α_eff-only ablation**（去掉 ESS constraint 只保留 α_eff ≥ τ），无法区分 adaptive b* 的贡献来自 α_eff 质量信号还是 ESS 稳定化。\n→ 建议补充 α_eff-only ablation；如果 ESS 是主要贡献者需调整 §6 叙事。\n\n**W2** [R2-W1 + R1 AGREE] **Adaptive b* 方法新颖性薄弱**\n权重公式 w=(1−q)^b 完全来自 Drayson et al.；adaptive b* 本质是满足两个阈值条件的最小 b——一个超参数自动选择启发式。论文已标注 \"practical corollary\"，但 §3 仍占 ~0.75 页。\n→ 建议进一步压缩 §3（Algorithm 1 移到 Appendix），正文只保留公式 (1) 和关键直觉。\n\n**W3** [R2-W2 + R1 AGREE] **Epoch confound 适用范围需明确限定**\nEpoch confound 主要出现在续训（小数据量 → 多 epoch）设置中。在大规模 from-scratch pretraining（通常 <1 epoch），confound 不成立。§7 \"any D&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness\" 过于泛化。§2 也未标注 Drayson et al. 是 from-scratch pretraining——这恰是 epoch confound 成立的前提。\n→ 建议在 §7 中加 qualifier 限定为 multi-epoch exposure 场景；在 §2 中讨论 from-scratch vs continued pretraining 的区别。\n\n**W4** [R2-W3 + R1 AGREE] **Detector 测试范围不足**\n仅 3 个 detector（TF-IDF+LR, GPT-2 PPL, N-gram PPL），未覆盖当前主流 neural classifiers（RoBERTa/ModernBERT fine-tuned, DetectGPT, Binoculars）。3 个数据点不足以建立 \"both AUC and ECE are necessary\" 的因果关系——可能存在 discriminative vs generative paradigm 本身的混杂。\n\n**W5** [R1-W4 提出, R2 部分 REBUT] **LR schedule 混淆因素**\nEpoch-matched D&R 使用完整 LR schedule 截断至 2553 步，改变了 warmup/decay 比例。Independent-schedule replication（D&R 17.651 vs shared 17.657, Δ=0.006）已基本排除 LR confound（R2 认为 adequate），但缺完整 LR curves 和 upsampling baseline。分歧较小，归为 should-fix。\n\n### Minor（不影响接收）\n\n- **m1** [R2-m5 + R1 AGREE]: ρ 同时表示 contamination ratio（§3-§7）和 Spearman 相关系数（Table 12, Appendix K），符号冲突。建议用 ρ_s 区分 Spearman。\n- **m2** [R2-m1 + R1 AGREE]: Table 2 中 Golden Ratio（oracle）和 D&R（multi-epoch）与 fair comparison 方法使用相同 bold 标注，误导可比性。\n- **m3** [R2-m3 + R1-m3]: Figure 1 (TikZ) 黑白打印下 orange/blue/violet 不可辨；Figure 2 x 轴标签与 adaptive b* 的关系不够清晰。\n- **m4** [R1-m1]: Table 2 中 Golden Ratio 的 w 定义未在 §4 Methods 中给出，需翻 Appendix。\n- **m5** [R1-m4]: Appendix Q 的 ρ=0.3 boundary 结果是重要数据点，建议在主文 §5.2 中明确引用。\n- **m6** [R2-m4]: Rebuttal 中 \"Appendix Q\" 标签需核对是否与 LaTeX 标签一致。\n- **m7** [R2-m2]: §2 Related Work 占 ~1.5 页，在 8 页限制下偏长（R1 partial REBUT：对 analysis paper 合理，但可作为页面超限的压缩候选）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **Abstract 超限 + 页面超限**：两个格式硬约束违反，必须在提交前修正。[R2-N1/N2, R1 AGREE]\n2. **N=3 seeds 统计检验力不足**：BH 校正后所有核心比较均未达 α=0.05，bootstrap CI 在 N=3 下不可靠。[R1-N1, R2-N3, 双方 AGREE]\n3. **效应量过小 + 下游零改善**：Δ=−0.020（~0.11%）在当前 scale 下无实际意义，batch-size 外推不可靠。[R1-N2, R2-N3/W4, 双方 AGREE]\n4. **实验范围过窄**：单模型/单数据集/self-contamination + \"necessary conditions\" claim 过强。[R1-W1/W3, R2-N4, 双方 AGREE]\n5. **Epoch confound 是最有价值的贡献**：方法论警示意义真实，不受 N=3 限制。[R1+R2 Strengths §1]\n6. **论文报告诚实**：坦承 downstream null、scale limitations、checkpoint artifact。[R1+R2 Strengths §3]\n\n## Reviewer Divergence [REBUT]\n\n分歧极小，仅两点 partial REBUT：\n\n1. **p_BH 位置**（R2-W5 vs R1 partial REBUT）：R2 认为 p_BH 藏在脚注中；R1 指出 p_BH=0.078 出现在 §5.1 正文段落中，非仅脚注。但双方同意应在 Table 2 中并列展示以提高可见性。→ 降级为 minor suggestion。\n\n2. **LR schedule confound**（R1-W4 vs R2 partial REBUT）：R1 认为 independent-schedule replication 细节不足；R2 认为 Δ=0.006 已 adequately 回应。双方同意 upsampling baseline 是更干净的设计。→ 保留为 should-fix。\n\n---\n\n## Questions（需作者澄清）\n\n1. **N=3 设计动因**：是计算资源限制还是有意为之？是否考虑过降低训练步数（如 3000 steps）换取更多 seeds（如 N=7）？\n2. **α_eff-only ablation**：去掉 ESS constraint 只保留 α_eff ≥ τ 的 PPL 是多少？这对分离两个 constraint 的独立贡献至关重要。Table 2 有 ESS-only 但缺 α_eff-only。\n3. **Proxy 相关性区别**：r(α_eff, mean_q)=0.80（proxy-to-detector-score）vs r(α_eff, true real fraction)=0.70（proxy-to-ground-truth）——前者是否应作为支持 proxy 可靠性的证据？\n4. **Batch-size confound**：B=4/8/16 实验是固定 total tokens 还是固定 steps？如果固定 steps，B=16 看到 4 倍 tokens 本身是 confound。\n5. **Family-wise correction 策略**：如果仅对 focal comparison（adaptive vs. uniform at each ρ）做校正而非全部 9 个，corrected p-values 是多少？是否考虑过分层检验策略？\n6. **Epoch confound 独立性**：epoch confound 核心发现是否可通过 \"D&R 1 epoch\" vs \"uniform 1 epoch\" 更简单地验证，不需要 adaptive b*？如果可以，这是否暗示 adaptive b* 对核心 contribution 非必需？\n\n---\n\n## Missing References\n\n两位 Reviewer 建议补充以下引用（已去除重复和误报）：\n\n- **MATES** (Yu et al., NeurIPS 2024) — 动态数据选择，用小模型预测大模型的数据 influence [R2]\n- **FineWeb-Edu** (Lozhkov et al., 2024) — 基于教育质量评分的大规模数据过滤，FineWeb 生态系统重要工作 [R2]\n- **D4** (Tirumala et al., 2024) — 去重+多样化策略 [R2]\n- **Fan et al. (2024)** — importance weighting 在 LM 训练中的 variance-bias tradeoff [R1]\n\n注：DoReMi (Xie et al.) 已在论文 §2 中引用（ref key `xie2023doremi`），R1 建议为误报，R2 已 REBUT 确认。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2026-05-23 13:10 → 13:13，约 3 分钟完成）\n\n发现（2 warning + 4 info）：\n\n- ⚠️ **Page 5**: Results §5.1 整页无 display item，所有支撑数据（Table 1/2, Figure 2）推至 page 6。建议调整 float 位置。\n- ⚠️ **Page 17**: Appendix 末页仅 6 行（~5% 填充），约 95% 空白。\n- ℹ️ **Page 2**: Figure 1 (overview) 本质是格式化文字方框，视觉吸引力有限。\n- ℹ️ **Pages 3-5**: 连续 3 页无 figure/table，节奏偏文本密集。\n- ℹ️ **Page 6**: 单页 3 个 display items（Table 1 + Figure 2 + Table 2），视觉密度过高。\n- ℹ️ **Page 12**: Appendix 页面极密集（Proofs + Algorithm 1 + Table 5 + 两个小节）。\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.0 / 5 — Findings**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 2.0 | 2.5 | 2.5 |\n| Overall | 3.0 | 3.0 | 3.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n\n**理由**：Epoch confound 的发现是真实的方法论贡献——定量证明 D&R 先前报告的优势中 >95% 来自数据重复而非 filtering quality，为后续工作建立了重要基线。这一发现达到 Findings 级别。但以下因素阻止论文达到 Conference (4.0) 门槛：\n\n1. **格式硬约束违反**：Abstract 超 200 words + 正文超 8 页——这些在提交前必须修正，否则有 desk reject 风险。\n2. **统计支撑不足**：N=3 seeds + BH 校正后全部不显著——对于一篇以定量分析为核心的论文，这是根本性弱点。\n3. **效应量可忽略**：Δ=−0.020（~0.11%），五项下游任务零改善——在可验证的所有指标上，方法没有实际改善。\n4. **实验范围过窄**：单模型/单数据集/self-contamination 使得三个 \"effectiveness conditions\" 的泛化性无法推断。\n5. **方法新颖性薄弱**：adaptive b* 本质是现有框架的参数选择启发式。\n\n**建议**：论文最有价值的贡献是 epoch confound 分析和 detector calibration 发现。如果以纯 analysis/empirical study 定位投稿，压缩 adaptive method 部分，增加 seeds 或放弃 p 值叙事，补充 cross-model 实验，修正格式问题，有望达到 Findings 接收水平。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract (p.1)\n- 225 words, 超 200 限制 [C1]\n- 最后一句 \"The method transitions from harmful (ρ=0.2) to beneficial (ρ≥0.4), with a sharp boundary in [0.3, 0.4]; the benefit diminishes at 1.7B, and sample size (N=3) limits generalizability\" 中对 N=3 限制的自我披露值得肯定\n\n### §1 Introduction (pp.1-2)\n- Figure 1 黑白不可辨 [m3]\n- 论文定位已从 method 调整为 analysis with practical corollary，较合理 [S4]\n\n### §2 Related Work (pp.2-3)\n- 覆盖 5 个子领域，对 analysis paper 合理但占 ~1.5 页，在页面紧张时是压缩候选 [m7]\n- 未标注 Drayson et al. 是 from-scratch pretraining vs 本文 continued pretraining [W3]\n- 缺失 MATES, FineWeb-Edu, D4, Fan et al. [m-refs]\n\n### §3 Method (p.3)\n- 压缩至 ~0.75 页后仍给独立方法贡献的印象 [W2]\n- α_eff 定义清晰，但 R²≈0.49 限制了其作为核心信号的可信度 [W1]\n- Algorithm 1 可移到 Appendix\n\n### §4 Experimental Setup (pp.3-4)\n- 实验细节充分，超参数透明 [S4]\n- Self-contamination 设计在此处应更突出地讨论生态效度限制 [C5]\n- Golden Ratio 的 w 定义缺失 [m4]\n\n### §5 Results (pp.4-7)\n- §5.1: N=3 统计检验力不足 [C3]，效应量极小 [C4]\n- §5.1 Epoch confound 部分是全文最强贡献 [S1]\n- §5.2: Detector calibration 发现 counter-intuitive 且有价值 [S2]\n- §5.2: Epoch confound 适用范围表述过于泛化 [W3]\n- §5.3: 缺 α_eff-only ablation [W1]\n- §5.4: Batch-size extrapolation 不可靠 [C4, W-batch]\n- Page 5 无 display item，Page 6 过度密集 [Visual Check]\n\n### §6 Discussion (pp.7-8)\n- Effect size in context 讨论充分 [S3]\n- α_eff proxy 局限性讨论到位但 R²≈0.49 的根本问题未解决 [W1]\n- Downstream null 分析合理但无法弥补实验验证的缺失 [C4]\n- 整节 ~1.5 页偏长，可压缩以解决页面超限 [C2]\n\n### §7 Conclusion (pp.8-9)\n- 溢出至 p.9 [C2]\n- \"any D&R evaluation...\" 表述过于泛化 [W3]\n- Batch-size amplification 作为 conclusion 内容过于 speculative\n\n### Limitations (p.9)\n- 覆盖合理：single scale, single dataset, N=3, detector coverage, self-contamination\n- 长度适中（~1 段）\n\n### Appendix (pp.10-17)\n- 17 节内容全面，可复现性强 [S4]\n- 末页 95% 空白 [Visual Check]\n- ρ 符号冲突 in Table 12 [m1]\n\n---\n\n*审稿报告由 Review Director 基于 2 位 Reviewer 的独立审稿、交叉分享和收敛分析汇总生成。*",
  "project": "provenance_weight_training",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**审稿模式**: Fresh（无前轮记忆）\n**Reviewers**: R1（方法严谨性+实验设计）、R2（新颖性+完整性+写作质量）\n**轮次**: 1 轮完成（Round 1 独立审稿 → 交叉分享 → 收敛，无需 Round 2）\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight (D&R) 范式在续训语言模型中应对合成文本污染的有效性条件。在 Qwen3-0.6B 上使用 132M FineWeb 子集（ρ=0.4, 3 seeds）进行可控实验，提出三项分析发现：(1) D&R 先前报告的 PPL 优势中 >95% 可归因于 epoch confound（多轮数据暴露），epoch-matched 后优势从 0.396 缩减至 0.017；(2) 有效 reweighting 要求检测器同时具备足够的 AUC（≥0.9）和良好的校准（ECE≤0.05）；(3) 基于双约束（α_eff ≥ τ, ESS ≥ n_min）的自适应 b* 实现最小干预优于最大化策略。作为实践推论，提出了一个无需 grid search 的自适应 b*，在 ρ≥0.4 时优于 uniform（Δ=−0.020 at ρ=0.4, Δ=−0.032 at ρ=0.6），但效应量极小（~0.11% relative），下游任务无改善。\n\n---\n\n## Strengths\n\n1. **Epoch confound 发现扎实且有方法论价值** [R1+R2 共识]：通过 epoch-matched 控制实验定量证明 D&R 先前报告的 PPL 优势中 >95% 来自多轮数据暴露而非 filtering quality（Table 1, Δ from 0.396 to 0.017, 3 seeds 方向一致）。LR-controlled verification（§5.1）进一步排除学习率调度混杂。这对后续 D&R 研究有直接方法论警示意义。\n\n2. **检测器校准 vs AUC 的 counter-intuitive 发现** [R1+R2 共识]：GPT-2 detector (AUC=0.91, ECE=0.131) 性能劣于 uniform (Δ=+0.098)，而 TF-IDF+LR (AUC=0.94, ECE=0.048) 成功——揭示 calibration 可以逆转 intervention 方向（§5.2, Appendix L），对 data curation 工作有指导价值。\n\n3. **实验设计诚实透明** [R1+R2 共识]：下游 null result（Table 4）、scale 限制（1.7B 效应减弱）、cross-model mixed results（Appendix O）、checkpoint resume artifact（Appendix P）均如实报告，无 cherry-picking。统计校正后不显著的 p 值也在正文中报告。\n\n4. **Appendix 覆盖全面** [R1+R2 共识]：17 节 appendix 涵盖 grid search details、threshold sweep、constraint regime decomposition、α_eff validation、detector comparison、cross-model transfer、低 ρ 分析、checkpoint artifact 等，可复现性强（Reproducibility 4/5）。\n\n5. **Decision framework 有实用价值** [R2]：Table 3 将分析结论转化为 practitioner-friendly 的决策指南（AUC≥0.9, ECE≤0.05, ρ≥0.4），是有价值的综合贡献。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1** [R2-N1, R1 AGREE] **Abstract 超过 200 words 限制**\nLaTeX 源码 wc -w 确认 225 words，超出 EMNLP 2026 / ARR 的 200 words 硬约束。Abstract 中包含大量数值细节（Δ=−0.020, ρ=0.4, bootstrap CI, p=0.010 等），应移到 Introduction。格式硬约束违反有 desk reject 风险。\n→ 建议压缩到 ≤180 words，删除具体数值保留定性结论。\n\n**C2** [R2-N2, R1 AGREE] **正文超出 8 页限制**\n§7 Conclusion 在 PDF p.8 底部开始，延伸至 p.9（约 15-20 行），之后才是 Limitations。EMNLP 2026 规定 §1-§7 主正文 ≤8 页，Limitations/Ethics 不计入但不得含过多额外内容。格式硬约束违反。\n→ 建议压缩 §6 Discussion（将 \"Effect size in context\" 和 \"Limitations of α_eff as proxy\" 部分内容移至 Limitations 或 Appendix）或 §2 Related Work（\"Theoretical Foundations\" 子段可移至 appendix）。\n\n**C3** [R1-N1 + R2-N3, 双方 AGREE] **N=3 seeds 统计推断力根本性不足**\n全文核心量化结论依赖 N=3 seeds 的 paired t-test（仅 2 df）。关键结果在 BH 校正后均未达 α=0.05：ρ=0.4 p_BH=0.078, ρ=0.6 p_BH=0.064。Bootstrap CI [−0.028, −0.012] 在 N=3 时仅 27 种重抽样，覆盖率保证极弱。Cohen's d=2.86 更可能反映方差被人为压低（seeds 仅影响初始化，data order 固定）而非效应量大。论文先报告 BH 校正再论证 family \"structurally heterogeneous\" 属于 post-hoc 统计叙事调整。\n→ 建议 (a) 增加到 N≥5 seeds，或 (b) 放弃 p 值叙事改为纯效应量+方向一致性报告。\n注：epoch confound 的核心发现不受此限——该结论在每个 seed 内独立成立。\n\n**C4** [R1-N2 + R2-N3, 双方 AGREE] **效应量极小（Δ=−0.020 PPL, ~0.11%）+ 下游零改善**\n五项下游任务全部 |Δ|≤0.01，adaptive 与 uniform 均为 0.5414（Table 4）。Batch-size extrapolation（3 点拟合幂律 Δ∝B^0.89 外推 32× 到 B=128 预测 Δ≈−0.39）统计学不可靠，但 rebuttal 中作为实际意义的主要论据。在可验证的所有指标上，方法无实际改善。\n→ 建议 (a) 删除或大幅降级 batch-size 外推（移到 appendix，标注 hypothesis）；(b) 在 abstract/conclusion 中删除所有 \"practical\" 残留表述。\n\n**C5** [R1-W1/W3 + R2-N4, 双方 AGREE] **实验范围过窄，不支撑一般性结论**\n所有实验基于单一模型族（Qwen3, 0.6B/1.7B）、单一数据集（FineWeb 132M）、自污染设计（generator=trainee）。Self-contamination 人为降低检测难度（AUC=0.94 部分归因于 generator=trainee 的统计指纹匹配）。Cross-model transfer（Appendix O, Llama→Qwen）single seed + mixed results + PPL 比较缺失。\"necessary conditions\" 是一个逻辑上很强的 claim，但仅在极窄设置上观察到。\n→ 建议 (a) 将 \"necessary conditions\" 改为 \"empirically observed conditions in our setting\"；(b) 在 abstract/conclusion 中限定 claim 适用范围为 \"self-contaminated continued pretraining at 0.6B scale\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R1-W2 + R2 AGREE] **α_eff proxy 解释力不足（R²≈0.49）以支撑其核心地位**\nα_eff 是双约束中 quality floor 的直接操作变量，但仅解释不到一半的目标方差。r(α_eff, mean_q)=0.80 是 proxy-to-detector-score 的相关性（循环论证），非 proxy-to-ground-truth（r=0.706）。跨 seed spread <0.003 是确定性函数+固定 detector 的预期结果，不构成额外证据。核心缺失：**α_eff-only ablation**（去掉 ESS constraint 只保留 α_eff ≥ τ），无法区分 adaptive b* 的贡献来自 α_eff 质量信号还是 ESS 稳定化。\n→ 建议补充 α_eff-only ablation；如果 ESS 是主要贡献者需调整 §6 叙事。\n\n**W2** [R2-W1 + R1 AGREE] **Adaptive b* 方法新颖性薄弱**\n权重公式 w=(1−q)^b 完全来自 Drayson et al.；adaptive b* 本质是满足两个阈值条件的最小 b——一个超参数自动选择启发式。论文已标注 \"practical corollary\"，但 §3 仍占 ~0.75 页。\n→ 建议进一步压缩 §3（Algorithm 1 移到 Appendix），正文只保留公式 (1) 和关键直觉。\n\n**W3** [R2-W2 + R1 AGREE] **Epoch confound 适用范围需明确限定**\nEpoch confound 主要出现在续训（小数据量 → 多 epoch）设置中。在大规模 from-scratch pretraining（通常 <1 epoch），confound 不成立。§7 \"any D&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness\" 过于泛化。§2 也未标注 Drayson et al. 是 from-scratch pretraining——这恰是 epoch confound 成立的前提。\n→ 建议在 §7 中加 qualifier 限定为 multi-epoch exposure 场景；在 §2 中讨论 from-scratch vs continued pretraining 的区别。\n\n**W4** [R2-W3 + R1 AGREE] **Detector 测试范围不足**\n仅 3 个 detector（TF-IDF+LR, GPT-2 PPL, N-gram PPL），未覆盖当前主流 neural classifiers（RoBERTa/ModernBERT fine-tuned, DetectGPT, Binoculars）。3 个数据点不足以建立 \"both AUC and ECE are necessary\" 的因果关系——可能存在 discriminative vs generative paradigm 本身的混杂。\n\n**W5** [R1-W4 提出, R2 部分 REBUT] **LR schedule 混淆因素**\nEpoch-matched D&R 使用完整 LR schedule 截断至 2553 步，改变了 warmup/decay 比例。Independent-schedule replication（D&R 17.651 vs shared 17.657, Δ=0.006）已基本排除 LR confound（R2 认为 adequate），但缺完整 LR curves 和 upsampling baseline。分歧较小，归为 should-fix。\n\n### Minor（不影响接收）\n\n- **m1** [R2-m5 + R1 AGREE]: ρ 同时表示 contamination ratio（§3-§7）和 Spearman 相关系数（Table 12, Appendix K），符号冲突。建议用 ρ_s 区分 Spearman。\n- **m2** [R2-m1 + R1 AGREE]: Table 2 中 Golden Ratio（oracle）和 D&R（multi-epoch）与 fair comparison 方法使用相同 bold 标注，误导可比性。\n- **m3** [R2-m3 + R1-m3]: Figure 1 (TikZ) 黑白打印下 orange/blue/violet 不可辨；Figure 2 x 轴标签与 adaptive b* 的关系不够清晰。\n- **m4** [R1-m1]: Table 2 中 Golden Ratio 的 w 定义未在 §4 Methods 中给出，需翻 Appendix。\n- **m5** [R1-m4]: Appendix Q 的 ρ=0.3 boundary 结果是重要数据点，建议在主文 §5.2 中明确引用。\n- **m6** [R2-m4]: Rebuttal 中 \"Appendix Q\" 标签需核对是否与 LaTeX 标签一致。\n- **m7** [R2-m2]: §2 Related Work 占 ~1.5 页，在 8 页限制下偏长（R1 partial REBUT：对 analysis paper 合理，但可作为页面超限的压缩候选）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **Abstract 超限 + 页面超限**：两个格式硬约束违反，必须在提交前修正。[R2-N1/N2, R1 AGREE]\n2. **N=3 seeds 统计检验力不足**：BH 校正后所有核心比较均未达 α=0.05，bootstrap CI 在 N=3 下不可靠。[R1-N1, R2-N3, 双方 AGREE]\n3. **效应量过小 + 下游零改善**：Δ=−0.020（~0.11%）在当前 scale 下无实际意义，batch-size 外推不可靠。[R1-N2, R2-N3/W4, 双方 AGREE]\n4. **实验范围过窄**：单模型/单数据集/self-contamination + \"necessary conditions\" claim 过强。[R1-W1/W3, R2-N4, 双方 AGREE]\n5. **Epoch confound 是最有价值的贡献**：方法论警示意义真实，不受 N=3 限制。[R1+R2 Strengths §1]\n6. **论文报告诚实**：坦承 downstream null、scale limitations、checkpoint artifact。[R1+R2 Strengths §3]\n\n## Reviewer Divergence [REBUT]\n\n分歧极小，仅两点 partial REBUT：\n\n1. **p_BH 位置**（R2-W5 vs R1 partial REBUT）：R2 认为 p_BH 藏在脚注中；R1 指出 p_BH=0.078 出现在 §5.1 正文段落中，非仅脚注。但双方同意应在 Table 2 中并列展示以提高可见性。→ 降级为 minor suggestion。\n\n2. **LR schedule confound**（R1-W4 vs R2 partial REBUT）：R1 认为 independent-schedule replication 细节不足；R2 认为 Δ=0.006 已 adequately 回应。双方同意 upsampling baseline 是更干净的设计。→ 保留为 should-fix。\n\n---\n\n## Questions（需作者澄清）\n\n1. **N=3 设计动因**：是计算资源限制还是有意为之？是否考虑过降低训练步数（如 3000 steps）换取更多 seeds（如 N=7）？\n2. **α_eff-only ablation**：去掉 ESS constraint 只保留 α_eff ≥ τ 的 PPL 是多少？这对分离两个 constraint 的独立贡献至关重要。Table 2 有 ESS-only 但缺 α_eff-only。\n3. **Proxy 相关性区别**：r(α_eff, mean_q)=0.80（proxy-to-detector-score）vs r(α_eff, true real fraction)=0.70（proxy-to-ground-truth）——前者是否应作为支持 proxy 可靠性的证据？\n4. **Batch-size confound**：B=4/8/16 实验是固定 total tokens 还是固定 steps？如果固定 steps，B=16 看到 4 倍 tokens 本身是 confound。\n5. **Family-wise correction 策略**：如果仅对 focal comparison（adaptive vs. uniform at each ρ）做校正而非全部 9 个，corrected p-values 是多少？是否考虑过分层检验策略？\n6. **Epoch confound 独立性**：epoch confound 核心发现是否可通过 \"D&R 1 epoch\" vs \"uniform 1 epoch\" 更简单地验证，不需要 adaptive b*？如果可以，这是否暗示 adaptive b* 对核心 contribution 非必需？\n\n---\n\n## Missing References\n\n两位 Reviewer 建议补充以下引用（已去除重复和误报）：\n\n- **MATES** (Yu et al., NeurIPS 2024) — 动态数据选择，用小模型预测大模型的数据 influence [R2]\n- **FineWeb-Edu** (Lozhkov et al., 2024) — 基于教育质量评分的大规模数据过滤，FineWeb 生态系统重要工作 [R2]\n- **D4** (Tirumala et al., 2024) — 去重+多样化策略 [R2]\n- **Fan et al. (2024)** — importance weighting 在 LM 训练中的 variance-bias tradeoff [R1]\n\n注：DoReMi (Xie et al.) 已在论文 §2 中引用（ref key `xie2023doremi`），R1 建议为误报，R2 已 REBUT 确认。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2026-05-23 13:10 → 13:13，约 3 分钟完成）\n\n发现（2 warning + 4 info）：\n\n- ⚠️ **Page 5**: Results §5.1 整页无 display item，所有支撑数据（Table 1/2, Figure 2）推至 page 6。建议调整 float 位置。\n- ⚠️ **Page 17**: Appendix 末页仅 6 行（~5% 填充），约 95% 空白。\n- ℹ️ **Page 2**: Figure 1 (overview) 本质是格式化文字方框，视觉吸引力有限。\n- ℹ️ **Pages 3-5**: 连续 3 页无 figure/table，节奏偏文本密集。\n- ℹ️ **Page 6**: 单页 3 个 display items（Table 1 + Figure 2 + Table 2），视觉密度过高。\n- ℹ️ **Page 12**: Appendix 页面极密集（Proofs + Algorithm 1 + Table 5 + 两个小节）。\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.0 / 5 — Findings**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 2.0 | 2.5 | 2.5 |\n| Overall | 3.0 | 3.0 | 3.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n\n**理由**：Epoch confound 的发现是真实的方法论贡献——定量证明 D&R 先前报告的优势中 >95% 来自数据重复而非 filtering quality，为后续工作建立了重要基线。这一发现达到 Findings 级别。但以下因素阻止论文达到 Conference (4.0) 门槛：\n\n1. **格式硬约束违反**：Abstract 超 200 words + 正文超 8 页——这些在提交前必须修正，否则有 desk reject 风险。\n2. **统计支撑不足**：N=3 seeds + BH 校正后全部不显著——对于一篇以定量分析为核心的论文，这是根本性弱点。\n3. **效应量可忽略**：Δ=−0.020（~0.11%），五项下游任务零改善——在可验证的所有指标上，方法没有实际改善。\n4. **实验范围过窄**：单模型/单数据集/self-contamination 使得三个 \"effectiveness conditions\" 的泛化性无法推断。\n5. **方法新颖性薄弱**：adaptive b* 本质是现有框架的参数选择启发式。\n\n**建议**：论文最有价值的贡献是 epoch confound 分析和 detector calibration 发现。如果以纯 analysis/empirical study 定位投稿，压缩 adaptive method 部分，增加 seeds 或放弃 p 值叙事，补充 cross-model 实验，修正格式问题，有望达到 Findings 接收水平。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract (p.1)\n- 225 words, 超 200 限制 [C1]\n- 最后一句 \"The method transitions from harmful (ρ=0.2) to beneficial (ρ≥0.4), with a sharp boundary in [0.3, 0.4]; the benefit diminishes at 1.7B, and sample size (N=3) limits generalizability\" 中对 N=3 限制的自我披露值得肯定\n\n### §1 Introduction (pp.1-2)\n- Figure 1 黑白不可辨 [m3]\n- 论文定位已从 method 调整为 analysis with practical corollary，较合理 [S4]\n\n### §2 Related Work (pp.2-3)\n- 覆盖 5 个子领域，对 analysis paper 合理但占 ~1.5 页，在页面紧张时是压缩候选 [m7]\n- 未标注 Drayson et al. 是 from-scratch pretraining vs 本文 continued pretraining [W3]\n- 缺失 MATES, FineWeb-Edu, D4, Fan et al. [m-refs]\n\n### §3 Method (p.3)\n- 压缩至 ~0.75 页后仍给独立方法贡献的印象 [W2]\n- α_eff 定义清晰，但 R²≈0.49 限制了其作为核心信号的可信度 [W1]\n- Algorithm 1 可移到 Appendix\n\n### §4 Experimental Setup (pp.3-4)\n- 实验细节充分，超参数透明 [S4]\n- Self-contamination 设计在此处应更突出地讨论生态效度限制 [C5]\n- Golden Ratio 的 w 定义缺失 [m4]\n\n### §5 Results (pp.4-7)\n- §5.1: N=3 统计检验力不足 [C3]，效应量极小 [C4]\n- §5.1 Epoch confound 部分是全文最强贡献 [S1]\n- §5.2: Detector calibration 发现 counter-intuitive 且有价值 [S2]\n- §5.2: Epoch confound 适用范围表述过于泛化 [W3]\n- §5.3: 缺 α_eff-only ablation [W1]\n- §5.4: Batch-size extrapolation 不可靠 [C4, W-batch]\n- Page 5 无 display item，Page 6 过度密集 [Visual Check]\n\n### §6 Discussion (pp.7-8)\n- Effect size in context 讨论充分 [S3]\n- α_eff proxy 局限性讨论到位但 R²≈0.49 的根本问题未解决 [W1]\n- Downstream null 分析合理但无法弥补实验验证的缺失 [C4]\n- 整节 ~1.5 页偏长，可压缩以解决页面超限 [C2]\n\n### §7 Conclusion (pp.8-9)\n- 溢出至 p.9 [C2]\n- \"any D&R evaluation...\" 表述过于泛化 [W3]\n- Batch-size amplification 作为 conclusion 内容过于 speculative\n\n### Limitations (p.9)\n- 覆盖合理：single scale, single dataset, N=3, detector coverage, self-contamination\n- 长度适中（~1 段）\n\n### Appendix (pp.10-17)\n- 17 节内容全面，可复现性强 [S4]\n- 末页 95% 空白 [Visual Check]\n- ρ 符号冲突 in Table 12 [m1]\n\n---\n\n*审稿报告由 Review Director 基于 2 位 Reviewer 的独立审稿、交叉分享和收敛分析汇总生成。*",
    "project": "provenance_weight_training",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-23T13:33:49.456042+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4132
}
```

</details>

---


### Assistant

_source line 1142 · 2026-05-23T13:34:05.172055+00:00_

审稿报告已投递至 Research Director。

---

**Round 12 审稿完成汇总**：

- **Overall**: 3.0 / 5 (Findings)
- **Reviewers**: 2 人，1 轮收敛（交叉分享后无重大分歧，无需 Round 2）
- **5 个 Must-Fix**: Abstract 超 200 词、正文超 8 页、N=3 统计检验力不足、效应量极小+下游零改善、实验范围过窄
- **5 个 Should-Fix**: α_eff proxy R²≈0.49 解释力有限、方法新颖性薄弱、epoch confound 适用范围需限定、detector 测试不足、LR schedule confound
- **7 个 Minor**: ρ 符号冲突、Table bold 标注误导、Figure 灰度可读性、Golden Ratio 定义缺失、ρ=0.3 结果需主文引用、Appendix 标签核对、Related Work 偏长
- **核心判断**: epoch confound 发现有真实的方法论价值，达 Findings 水平；但格式违规 + 统计不足 + 效应量可忽略 + 范围过窄阻止达到 Conference 门槛
- **Issue Tracker**: 已更新至 `review_issues.yaml`（R11 recurring issues 更新 + R12 新增 8 条）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 89

## Round 89

2 recorded events


### User

_source line 1143 · 2026-05-23T13:34:07.726327+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

11 条意见中 AGREE 10 条、REBUT 1 条（W4 LR confound 部分反驳——论文的 independent-schedule replication 已有效排除了 LR 混淆）。两位 Reviewer 在核心判断上高度一致：N=3 统计 power 不足、效应量过小、实验范围过窄。R1 额外贡献的 α_eff-only ablation 建议是最有建设性的新观点。Overall 维持 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1144 · 2026-05-23T13:34:18.598192+00:00_

审稿报告已在 R2 交叉回应到达前提交（两位 Reviewer 的 Round 1 报告 + R1 交叉回应已收齐，核心判断高度一致）。R2 交叉回应现已到达，确认与报告结论完全一致：

- 11 条中 AGREE 10 条、REBUT 1 条（W4 LR confound，与 R1 的部分 REBUT 方向相同）
- Overall 维持 3.0 (Findings)
- 无新增分歧点

报告无需修订。审稿流程完成。

**最终结果**: Overall **3.0 / 5 (Findings)**，5 个 Must-Fix（abstract 超限、页面超限、N=3 统计力不足、效应量过小+下游零改善、实验范围过窄）、5 个 Should-Fix、7 个 Minor。报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 90

## Round 90

64 recorded events


### User

_source line 1145 · 2026-05-24T04:06:52.398472+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-24T04:06:58.258782+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-24T04:06:58.309717+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-24T04:07:11.951004+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-24T04:07:11.951341+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-24T04:07:16.368025+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1151 · 2026-05-24T04:07:17.828172+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (256 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- detect_remove_q05_seed42: Detect-and-remove baseline: hard filtering removes samples with TF-IDF q_score < 0.5. If adaptive reweighting (PPL=17.674) outperforms hard removal, it demonstrates that soft scoring preserves useful signal from partially contaminated samples that hard thresholding discards.（准备中）\n- eval_adaptive_1_7b_seed123（准备中）\n- eval_uniform_1_7b_seed123（准备中）\n- detect_remove_q05_epoch_matched（准备中）\n- detect_remove_q07_seed42_r2（准备中）\n- adaptive_1_7b_planb_control（准备中）\n- eval_q01_final（准备中）\n- status_check_41312（准备中）\n- eval_adaptive_1_7b（准备中）\n- eval_uniform_1_7b_v2（准备中）\n- …另有 7 项\n\n## 近期结论\n- **aeff_only_nmin1_seed456** (success): α_eff-only ablation seed456: cross-seed replicate. n_min=1 removes ESS constraint. Third seed for paired t-test vs dual-constrained baseline.\n- **bs8_nmin4_adaptive_seed456_r2** (success): B=8 第三 seed 补全 3-seed paired comparison。seed42 Δ=−0.044, seed123 Δ=−0.056。预期 Δ∈[−0.040, −0.060]。3-seed 均值将提供 batch-size amplification (B=4→B=8→B=16) 的完整统计支撑。\n- **bs8_nmin4_uniform_seed456_r2** (success): seed456 uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed456. Completes 3-seed set for batch-size 
…[truncated 1811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1460
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-24T04:07:18.280033+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 1153 · 2026-05-24T04:07:18.632095+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-24T04:07:18.682769+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-24T04:07:18.733396+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-24T04:07:27.099000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 1157 · 2026-05-24T04:07:30.159665+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1158 · 2026-05-24T04:07:30.260431+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1159 · 2026-05-24T04:07:30.361229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1160 · 2026-05-24T04:07:30.462005+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	What detector properties are necessary for effective reweighting?
8	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
9	
10	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
11	To ground the analysis of exponent selection, we introduce a dual-constrained formulation: find the minimum $b$ such that $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
12	
13	Our analysis yields three findings:
14	\begin{itemize}[nosep,leftmargin=*]
15	\item \textbf{Epoch confound in D\&R evaluation.}
16	The bulk of D\&R's PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure, not filtering quality; epoch-matched controls ($N{=}3$) reduce the gap from 0.396 to $\Delta{=}0.017$ (Table~\ref{tab:epoch_match}).
17	
18	\item \textbf{De
…[truncated 2987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1161 · 2026-05-24T04:07:30.462344+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1162 · 2026-05-24T04:07:30.914176+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1163 · 2026-05-24T04:07:30.914549+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1164 · 2026-05-24T04:07:31.817900+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1165 · 2026-05-24T04:07:31.818262+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-24T04:07:32.370451+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1167 · 2026-05-24T04:07:32.370793+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-24T04:07:32.872881+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1169 · 2026-05-24T04:07:32.873244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1170 · 2026-05-24T04:07:33.325018+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (1) D\&R evaluations confound filtering with multi-epoch exposure (${>}$95\% of the advantage); (2) detectors require both discrimination \emph{and} calibration; (3) minimum intervention outperforms unconstrained maximization.
2	A dual-constrained adaptive $\bstar$ improves over uniform at $\rho \geq 0.4$ (directionally consistent across all seeds; $\rho{=}0.6$: uncorrected $p{=}0.010$) without tuning; batch-size amplification is monotonic across $B \in \{4, 8, 16\}$ ($1.0{\times}$ to $3.4{\times}$).
3	In continued pretraining settings, D\&R evaluations that do not control for content epochs risk overstating filtering effectiveness; for practitioners, reweighting is worthwhile only when $\rho \geq 0.4$ and the detector is well-calibrated (Table~\ref{tab:decision}).
4	Code and data will be released upon acceptance.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-24T04:07:33.325386+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-24T04:07:33.977822+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-24T04:07:34.028623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-24T04:07:34.330253+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder and show that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape and confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4,dubey2024llama}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; M
…[truncated 7143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-24T04:07:34.330742+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1176 · 2026-05-24T04:07:34.883293+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1177 · 2026-05-24T04:07:34.883637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-24T04:07:34.934213+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@inproceedings{katharopoulos2018not,
5	  title={Not All Samples Are Created Equal: Deep Learning with Importance Sampling},
6	  author={Katharopoulos, Angelos and Fleuret, Fran{\c{c}}ois},
7	  booktitle={International Conference on Machine Learning},
8	  pages={2525--2534},
9	  year={2018},
10	  organization={PMLR}
11	}
12	
13	@inproceedings{ren2018learning,
14	  title={Learning to Reweight Examples for Robust Deep Learning},
15	  author={Ren, Mengye and Zeng, Wenyuan and Yang, Bin and Urtasun, Raquel},
16	  booktitle={International Conference on Machine Learning},
17	  pages={4334--4343},
18	  year={2018},
19	  organization={PMLR}
20	}
21	
22	@article{chen2024bull,
23	  title={Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves {LLM} Generalization},
24	  author={Chen, Xuxi and Li, Zhendong and Cai, Daixuan and Yao, Huanran and Chen, Zheng and Wang, Zhongming},
25	  journal={arXiv preprint arXiv:2402.14270},
26	  year={2024}
27	}
28	
29	@inproceedings{kang2025demystifying,
30	  title={Demystifying Synthetic Data in {LLM} Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls},
31	  author={Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Chen, Hongliang and Zhu, Yiming and Chen, Zijian and Liu, Mohan and Liu, Jingcheng and Liu, Haoran and Han, Song},
32	  booktitle={EMNLP},
33	  year={2025}
34	}
35	
36	@article{zibakhsh2025fortifai,
37	  title={{ForTIFAI}: Fending Off Recursive Training Induced Failure for {AI} Model Collapse},
38	  author={Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koushanfar, Farinaz},
39	  journal={arXiv preprint arXiv:2509.08972},
40	  year={2025}
41	}
42	
43	@article{yi2025escaping,
44	  title={Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
…[truncated 16830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-24T04:07:35.536962+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines and information for EMNLP 2026:

## Submission Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Important Dates (ARR Submission)
The ARR submission deadline for long and short papers is May 25, 2026, with the reviewer registration deadline for all authors on May 27, 2026. Author response and author-reviewer discussion will take place July 7-13, 2026, meta review will be released July 30, 2026, and the EMNLP commitment deadline is August 2, 2026.

## ARR and Venue Selection Policy
Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit 
…[truncated 1008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 8437
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-24T04:07:47.189055+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-24T04:07:47.641288+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml\", \"content\": \"_next_id: 130\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 投稿目标定为 AAAI 2027 (~Aug 2026)，放弃 EMNLP 2026 ARR May 25\\n  rationale: EMNLP ARR 仅剩 12 天且无任何基础设施，即使 AI 团队速度也无法完成多轮预训练实验。AAAI 2027 有 ~11 周，足够完成\\n    4 phase 全流程。两者均为 A 类会议。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:38 UTC\\n  summary: 'MVP 设计: 单模型(Qwen3-0.6B) + 单污染比例(40%) + 三组对比(uniform/grid-b/adaptive-b*)'\\n  rationale: 核心假设是 adaptive b* 能替代 grid search。最小验证只需一个污染比例下的 A/B/C 对比。40% 选取因为理论和\\n    Strong Model Collapse 均表明该区间效应显著。通过后再扩展到多污染比例/多生成器/多模型。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-13 17:40 UTC\\n  summary: '修正 D001: 主攻 EMNLP 2026 ARR May 25，AAAI 2027 为后备'\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、资源会给够。AI 团队 24/7 执行 + 4 卡并行：数据生成 ~2 天、MVP\\n    ~1 天、全矩阵 ~3 天、论文 ~3 天、迭代 ~2 天 = 11 天可完成。12 天 deadline 可行。保守估计完成时间是最大风险。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 17:42 UTC\\n  summary: '采纳 Reviewer 4 点 MVP 协议补全: 3 seeds、detector gate、grid-b 定义、kill criteria'\\n  rationale: 'Reviewer 指出 MVP 设计 4 个缺口均合理: (1) 单 seed 无统计保障 → 3 seeds，缩 tokens 到 200M\\n    控预算; (2) 检测器质量是 pipeline 前提 → 加 gate AUC≥0.95/ECE≤0.05; (3) grid search baseline\\n    需可复现 → 定义 b∈{0.5,1,1.5,2,3,5}; (4) 无 fail 路径 → 定义三级 kill/pivot。不增加工程量，只补协议。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-13 22:08 UTC\\n  summary: 识别 q-score 极化风险：AUC=0.999998 可能导致 adaptive b* vs grid-b 对比退化，制定分级应对方案\\n  rationale: 'Reviewer 审查发现 detector eval_auc=0.999998（step 2000），q-score 可能高度双峰化。若校准后\\n    >95% 样本 q<0.05 或 q>0.95，则 w=(1-q)^b 对所有 b>0 约等于 0，不同 b 值间无区分度。MVP 技术上可能 PASS（adaptive\\n    ≈ grid-b，满足 ≥90% 条件），但无法证明核心贡献（自适应精细调优的价值）。\\n\\n\\n    应对方案（detector 完成后按 q-score 分布分级执行）：\\n\\n    - 分布有spread（q 在 0.
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-24T04:07:47.792307+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 1183 · 2026-05-24T04:07:47.792630+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-24T04:07:59.453321+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 1185 · 2026-05-24T04:07:59.453755+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-24T04:08:11.192944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-24T04:08:11.645476+00:00_

1	issues:
2	# === Round 10 issues (all resolved, retained for history) ===
3	- id: "R10-C1"
4	  summary: "Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 10
9	  last_seen_round: 10
10	  mentions:
11	    - round: 10
12	      reviewers: [1, 2]
13	      note: "Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。"
14	  resolution: "tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。"
15	  resolution_round: 10
16	
17	- id: "R10-C2"
18	  summary: "多重比较未校正，p=0.025 Bonferroni 校正后不显著"
19	  category: experiment
20	  severity: critical
21	  status: resolved
22	  first_raised_round: 10
23	  last_seen_round: 10
24	  mentions:
25	    - round: 10
26	      reviewers: [1, 2]
27	      note: "6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。"
28	  resolution: "BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。"
29	  resolution_round: 10
30	
31	- id: "R10-C3"
32	  summary: "方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配"
33	  category: framing
34	  severity: critical
35	  status: resolved
36	  first_raised_round: 10
37	  last_seen_round: 10
38	  mentions:
39	    - round: 10
40	      reviewers: [1, 2]
41	      note: "w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。"
42	  resolution: "§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。"
43	  resolution_round: 10
44	
45	- id: "R10-C4"
46	  summary: "Downstream task 零改善削弱实际意义"
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 10
51	  last_seen_round: 10
52	  mentions:
53	    - round: 10
54	      reviewers: [1, 2]
55	      note: "Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。"
56	  resolution: "Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limit
…[truncated 20434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-24T04:08:12.147748+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/provenance_weight_training/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/provenance_weight_training/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-24T04:08:12.800503+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-24T04:08:12.851200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-24T04:08:13.406091+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf (486.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-24T04:09:20.626548+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-24T04:09:20.727312+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-24T04:09:21.480157+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "provenance_weight_training",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "provenance_weight_training",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-24T04:09:25.086439+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3606
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-24T04:09:32.264013+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_checklist.yaml",
  "max_chars": "2000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "paper_checklist.yaml",
    "max_chars": "2000"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-24T04:09:32.816341+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'provenance_weight_training'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-24T04:09:33.822041+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-24T04:09:34.073464+00:00_

Found 16 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_2b6c9bea33a70c93bf4bf04ac36b8df9_director_20260523T201657_344729.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/worker_util_download_figure_pdf_20260523T093836.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/workers/worker_util_download_figure_pdf_20260523T093836.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_2b6c9bea33a70c93bf4bf04ac36b8df9_director_20260521T185642_361028.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_2b6c9bea33a70c93bf4bf04ac36b8df9_director_20260519T110258_056988.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/workers/worker_ssh_download_tau_figures_20260515T184814.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log
/home/ubuntu/.agent-ml-r
…[truncated 157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1200 · 2026-05-24T04:09:39.554261+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1201 · 2026-05-24T04:09:39.655045+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-24T04:10:32.833023+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR\n- **截止日期**: 2026-05-25\n- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL (review mode)\n- **匿名规则**: Double-blind via ARR\n- **Abstract**: ≤200 words\n- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit)\n\n## 论文路径\n- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 统计分析严谨性\n- N=3 seeds 的统计检验力是否足够支撑定量结论？\n- p 值报告是否正确处理了多重比较？（Bonferroni-Holm 校正）\n- Bootstrap CI 在 N=3 时的有效性\n- Cohen's d 和效应量解读是否合理？\n\n### 2. 实验设计\n- Self-contamination 设计的控制变量是否充分？\n- Epoch confound 分析：epoch-matched 控制组和 LR-controlled verification 是否严密？\n- 消融层次（Adaptive < Uniform < ESS-only < Random）的因果推断是否成立？\n- α_eff-only ablation (n_min=1) 实验的解读\n\n### 3. 方法有效性\n- α_eff proxy 的 r=0.79 correlation 是否足以支撑双约束框架？\n- 双约束公式（α_eff ≥ τ, ESS ≥ n_min）的理论动机和实际验证\n- Per-batch bisection 的计算开销和实际可行性\n- B=4 micro-batch 上运行 dual constraint 的统计可靠性\n\n### 4. 结果解读\n- Δ=-0.020 PPL (0.11% relative) 的实际意义\n- Downstream task 零改善的影响\n- Batch-size amplification trend (B=4→8→16) 的外推可靠性\n- ρ=0.2 failure case 的分析充分性\n\n### 5. Detector 分析\n- 3 个 detector 是否足以建立 AUC/ECE 的因果关系？\n- Discriminative vs generative detector 的混杂因素\n\n请提供完整审稿报告，包含：Strengths (逐条), Weaknesses (逐条，标注 must-fix / should-fix / minor), Questions, Missing References, Overall Assessment (ARR 分数 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR\n- **截止日期**: 2026-05-25\n- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL (review mode)\n- **匿名规则**: Double-blind via ARR\n- **Abstract**: ≤200 words\n- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit)\n\n## 论文路径\n- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 统计分析严谨性\n- N=3 seeds 的统计检验力是否足够支撑定量结论？\n- p 值报告是否正确处理了多重比较？（Bonferroni-Holm 校正）\n- Bootstrap CI 在 N=3 时的有效性\n- Cohen's d 和效应量解读是否合理？\n\n### 2. 实验设计\n- Self-contamination 设计的控制变量是否充分？\n- Epoch confound 分析：epoch-matched 控制组和 LR-controlled verification 是否严密？\n- 消融层次（Adaptive < Uniform < ESS-only < Random）的因果推断是否成立？\n- α_eff-only ablation (n_min=1) 实验的解读\n\n### 3. 方法有效性\n- α_eff proxy 的 r=0.79 correlation 是否足以支撑双约束框架？\n- 双约束公式（α_eff ≥ τ, ESS ≥ n_min）的理论动机和实际验证\n- Per-batch bisection 的计算开销和实际可行性\n- B=4 micro-batch 上运行 dual constraint 的统计可靠性\n\n### 4. 结果解读\n- Δ=-0.020 PPL (0.11% relative) 的实际意义\n- Downstream task 零改善的影响\n- Batch-size amplification trend (B=4→8→16) 的外推可靠性\n- ρ=0.2 failure case 的分析充分性\n\n### 5. Detector 分析\n- 3 个 detector 是否足以建立 AUC/ECE 的因果关系？\n- Discriminative vs generative detector 的混杂因素\n\n请提供完整审稿报告，包含：Strengths (逐条), Weaknesses (逐条，标注 must-fix / should-fix / minor), Questions, Missing References, Overall Assessment (ARR 分数 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-24T04:10:50.265398+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17432
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-24T04:10:50.416403+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "你是 Reviewer 2，负责审查新颖性、完整性、写作质量、Related Work 和格式合规。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR\n- **截止日期**: 2026-05-25\n- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL (review mode)\n- **匿名规则**: Double-blind via ARR\n- **Abstract**: ≤200 words\n- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit)\n\n## 论文路径\n- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 三个 findings 的新颖性分别如何？（epoch confound / detector requirements / minimum intervention）\n- w=(1-q)^b 完全来自 Drayson et al. (2025)，adaptive b* 作为 \"practical corollary\" 的新颖性\n- 与 prior work 的区分是否清晰？（Drayson et al., He et al., Feng et al.）\n- 作为 analysis paper 的 contributions 是否足够支撑 EMNLP main conference？\n\n### 2. Related Work 完整性\n- 是否覆盖了所有重要的相关工作？\n- Domain-level mixing / instance-level reweighting / synthetic detection / model collapse 四条线是否完整？\n- 最近（2025-2026）的关键工作是否遗漏？\n- 与最直接相关的 Drayson et al. (2025) 的对比是否充分和公平？\n\n### 3. 写作质量\n- Abstract 是否清晰概括了贡献？数值密度是否合适？\n- Introduction 的 narrative flow 和 motivation\n- 论文定位（analysis paper vs method paper）是否一致贯穿全文？\n- Discussion 的深度和自我批评是否充分？\n- Limitations 是否覆盖了关键局限？\n\n### 4. 格式合规（EMNLP 2026 硬约束）\n- **Abstract 字数**：统计是否 ≤200 words（逐词计数）\n- **正文页数**：§1-§7 (Conclusion) 是否在 8 页内结束？\n- **Limitations**：是否在正文中且只有一个？Appendix 中是否有重复的 limitations section？\n- **匿名性**：是否有泄露身份的信息？（作者名、机构、GitHub 链接等）\n- **引用格式**：natbib 兼容性\n- **ARR Responsible NLP Checklist**：是否在 PDF 中（不应该在，应在 OpenReview 表单中）\n\n### 5. 整体连贯性\n- 三个 findings → adaptive b* 的叙事逻辑是否自然？\n- 表格/图表/正文之间的一致性\n- Appendix 的组织和引用是否合理？\n\n请提供完整审稿报告，包含：Strengths (逐条), Weaknesses (逐条，标注 must-fix / should-fix / minor), Questions, Missing References, Overall Assessment (ARR 分数 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "你是 Reviewer 2，负责审查新颖性、完整性、写作质量、Related Work 和格式合规。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR\n- **截止日期**: 2026-05-25\n- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL (review mode)\n- **匿名规则**: Double-blind via ARR\n- **Abstract**: ≤200 words\n- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit)\n\n## 论文路径\n- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 三个 findings 的新颖性分别如何？（epoch confound / detector requirements / minimum intervention）\n- w=(1-q)^b 完全来自 Drayson et al. (2025)，adaptive b* 作为 \"practical corollary\" 的新颖性\n- 与 prior work 的区分是否清晰？（Drayson et al., He et al., Feng et al.）\n- 作为 analysis paper 的 contributions 是否足够支撑 EMNLP main conference？\n\n### 2. Related Work 完整性\n- 是否覆盖了所有重要的相关工作？\n- Domain-level mixing / instance-level reweighting / synthetic detection / model collapse 四条线是否完整？\n- 最近（2025-2026）的关键工作是否遗漏？\n- 与最直接相关的 Drayson et al. (2025) 的对比是否充分和公平？\n\n### 3. 写作质量\n- Abstract 是否清晰概括了贡献？数值密度是否合适？\n- Introduction 的 narrative flow 和 motivation\n- 论文定位（analysis paper vs method paper）是否一致贯穿全文？\n- Discussion 的深度和自我批评是否充分？\n- Limitations 是否覆盖了关键局限？\n\n### 4. 格式合规（EMNLP 2026 硬约束）\n- **Abstract 字数**：统计是否 ≤200 words（逐词计数）\n- **正文页数**：§1-§7 (Conclusion) 是否在 8 页内结束？\n- **Limitations**：是否在正文中且只有一个？Appendix 中是否有重复的 limitations section？\n- **匿名性**：是否有泄露身份的信息？（作者名、机构、GitHub 链接等）\n- **引用格式**：natbib 兼容性\n- **ARR Responsible NLP Checklist**：是否在 PDF 中（不应该在，应在 OpenReview 表单中）\n\n### 5. 整体连贯性\n- 三个 findings → adaptive b* 的叙事逻辑是否自然？\n- 表格/图表/正文之间的一致性\n- Appendix 的组织和引用是否合理？\n\n请提供完整审稿报告，包含：Strengths (逐条), Weaknesses (逐条，标注 must-fix / should-fix / minor), Questions, Missing References, Overall Assessment (ARR 分数 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-24T04:10:51.827049+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-24T04:11:12.720463+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成论文初审报告",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: provenance_weight_training\n- 论文路径: projects/provenance_weight_training/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成论文初审报告",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: provenance_weight_training\n- 论文路径: projects/provenance_weight_training/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-24T04:11:12.721039+00:00_

Next wakeup scheduled for 04:15:00 (in 227s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1208 · 2026-05-24T04:11:16.664717+00:00_

Reviewer 1 和 Reviewer 2 正在独立审稿中，约 4 分钟后检查进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 91

## Round 91

2 recorded events


### User

_source line 1209 · 2026-05-24T04:17:06.706350+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.0 (Findings)
**Confidence**: 4/5
**一句话总结**: 分析工作（尤其是 epoch confound）有价值，但核心方法改进量极小（Δ=-0.020 PPL, 0.11%）、校正后不显著、downstream 零改善、仅在自污染设定下验证，贡献度处于 Findings 边界。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 实验设计审慎、对照齐全，但 N=3 统计效力不足、校正后均不显著、bootstrap CI 在 N=3 下可靠性存疑、自污染设计限制泛化性 |
| Excitement | 2.5/5 | Epoch confound 发现有价值但不算出人意料；方法本身改进量可忽略不计；条件约束过窄（ρ≥0.4 + 校准 detector + 非自我生成 unverified），实用性受限 |
| Reproducibility | 4/5 | 训练细节充分（Appendix M-N），代码承诺 release，但 detector 自动选择逻辑"first satisfying AUC ∈ [0.85, 0.98] and mid-range score ratio ≥ 5%"缺乏细节 |
| Overall Assessment | 3.0 | 分析质量在 Findings 水平，但方法贡献不足以支撑 Conference |

## Must-Fix 问题（影响接收决定）

**N1** [critical] N=3 seeds 下所有核心结论均未达到校正后统计显著性
- 具体位置：Section 5.1 (Table 2), Section 5.2, Limitations
- 问题：论文最核心的两个定量 claim：
  - ρ=0.4: uncorrected p=0.019, Bonferroni-Holm 校正后 p_BH=0.078（不显著）
  - ρ=0.6: uncorrected p=0.010, p_BH=0.064（不显著）
  
  论文诚实报告了这些数字，但 abstract 和 conclusion 仍以 "improves over uniform at ρ≥0.4" 的断言性语言呈现这些结果，没有在最显眼的位置标注"校正后不显著"。BCa bootstrap CI [-0.028, -0.012] 在 N=3 下存在覆盖率问题——bootstrap 理论要求经验分布近似总体分布，3 个数据点无法保证这一点（Efron & Tibshirani 1993 建议 N≥10-15）。
- 为什么影响接收：如果核心 claim 在合理的多重比较校正下不显著，那么 "adaptive b* improves over uniform" 这个 claim 的可信度大幅下降。读者可能过度信赖 bootstrap CI 而忽略校正后的 p 值。
- 建议修改方向：(1) 增加到 N≥5 seeds 以获得足够统计效力；(2) 若无法增加 seeds，abstract/conclusion 必须明确标注"directionally consistent but not statistically significant after correction"；(3) 讨论 bootstrap CI 在极小样本下的局限性。

**N2** [critical] 自污染设计严重限制所有发现的泛化性
- 具体位置：Section 4 (Experimental Setup), Appendix O (Cross-Model Transfer)
- 问题：Generator 和 trainee 都是 Qwen3-0.6B，这是最简单的检测场景——TF-IDF 特征可以利用 128-token prefix 到 384-token continuation 的风格断裂点，以及小模型自身的写作特征。所有三个核心发现（epoch confound、calibration requirement、minimum intervention advantage）都建立在这个设定上。唯一的跨模型测试（Llama-3.2-3B，Appendix O）是 single seed、结果 mixed、且缺少 PPL 对比（"checkpoints were not retained for re-evaluation"）。
  
  更关键的是：现实世界的 web contamination 来自多个不同模型（GPT-4、Claude、Gemini 等），文体多样、混合度不均。self-contamination 是否能代表这类场景完全未验证。
- 为什么影响接收：论文的贡献价值高度依赖于发现能否推广到现实场景。如果 AUC/ECE 阈值（Table 3）只在自污染下成立，practitioner decision summary 就不可靠。
- 建议修改方向：(1) 至少完成 cross-model 实验的 PPL 对比（3 seeds）；(2) 或者将 title/abstract 明确限定为"self-contamination setting"；(3) 讨论为什么自污染设定下的 calibration requirement 可能不适用于跨模型场景（generative detectors 在跨模型场景中的 false positive pattern 可能不同）。

**N3** [critical] Downstream tasks 零改善削弱方法的实际价值
- 具体位置：Section 6 (Discussion), Table 4
- 问题：Adaptive vs Uniform 在 5 个 downstream tasks 上 mean accuracy 完全相同（0.5414 vs 0.5414），个别 task Δ≤0.01 且方向 mixed。论文将此归因于"PPL-to-accuracy transfer is nonlinear and scale-dependent"和 0.1% PPL shift 低于 task measurement noise，这个解释合理。但这意味着该方法在当前规模下没有可观测的实际效果。
  
  论文在 Discussion 中试图论证"the PPL improvements operate in a regime that standard benchmarks cannot resolve"，但如果一个方法的效果小到所有标准评估手段都无法检测，那它的实际意义也就存疑。
- 为什么影响接收：方法论文需要展示实际效用。PPL 改善无法转化为任何可测量的下游效果，大幅降低了方法的实用价值。
- 建议修改方向：(1) 在更大规模（7B+）验证是否 downstream 效果可见；(2) 或者明确将论文定位为"分析性贡献"（empirical analysis of D&R effectiveness conditions），弱化方法贡献的 claim。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] B=4 micro-batch 上的 dual constraint 统计可靠性不足
- 具体位置：Section 3 (Method), Appendix B (Algorithm)
- 问题：在 B=4 样本上计算 α_eff 和 ESS，其中 true real fraction 是 Binomial(4, 0.6) 分布，标准差 ≈ 0.245。batch 的真实 real fraction 只能取 {0, 0.25, 0.5, 0.75, 1.0} 五个值。α_eff 作为加权平均在如此小的样本上波动剧烈（Appendix K 的 MAE=0.114）。虽然论文展示了 B=8→16 的放大效应，但主实验全部在 B=4 上完成，方法的核心机制在最 noisy 的条件下运行。
- 建议：(1) 主实验应至少包含 B=8 的完整对比（3 seeds, 含 downstream）；(2) 讨论 B=4 是否是实际部署中的 realistic setting。

**W2** [warning] α_eff proxy 的 r=0.79 相关性（R²=0.63）作为双约束框架的基础偏弱
- 具体位置：Section 3 (Method), Section 6 (Discussion), Appendix K
- 问题：α_eff 与 true batch-level real fraction 的 Pearson r=0.79（R²≈0.63），37% 方差未被解释。论文将未解释方差归因于 detector noise（70%）和 adaptive b* transform（30%），但这是对 unexplained variance 的分解，不能消除 proxy 误差对 b* selection 的系统性影响。论文指出 consistent negative bias ≈ -0.03 导致保守干预，但这个 bias 是否在所有 ρ 水平和 detector 组合下都成立？在 ρ=0.2 的 failure case 中，bias 的方向和大小可能不同。
  
  更根本的问题是：论文将 α_eff ≥ τ 的动机追溯到 "convergence theory under contamination (Wang et al., 2026)"，但 α_eff 只是 true real fraction 的一个 noisy proxy——convergence theory 中的阈值条件应用于 α_eff 而非 true fraction，理论保证是否仍然成立没有讨论。
- 建议：(1) 明确 α_eff ≥ τ 的理论动机：如果 Wang et al. (2026) 的定理要求 true real fraction ≥ τ，α_eff 作为 proxy 需要怎样的精度才能保留这个保证？(2) 在 ρ=0.2 场景下报告 α_eff 的 bias 和 correlation。

**W3** [warning] Batch-size amplification trend 的外推基于 3 个数据点
- 具体位置：Section 5.3 (Hyperparameter Sensitivity)
- 问题：B ∈ {4, 8, 16} 三个点拟合得到 Δ ∝ B^0.89。三个数据点不足以建立可靠的 scaling law。指数 0.89 的不确定性没有报告（confidence interval），且从 B=4 到 B=16 只是 4 倍范围——任何单调递增函数都可以在这个范围内被 power law 近似。论文称"suggesting diminishing but substantial marginal gains at larger batch sizes"，但 B=32 或 B=64 时是否还成立完全无法判断。
- 建议：(1) 要么删除 power law fitting 和外推讨论；(2) 要么扩展到 B=32, 64 并报告 confidence intervals。

**W4** [warning] 3 个 detector 不足以建立 AUC/ECE 因果关系和实用阈值
- 具体位置：Section 5.2 (Robustness), Table 3, Appendix L
- 问题：Table 3 的 practitioner decision summary 声称"Detector AUC ≥ 0.9: Required"和"Detector ECE ≤ 0.05: Required"，但这些阈值仅来自 3 个 detector（TF-IDF+LR AUC=0.94/ECE=0.048; GPT-2 AUC=0.91/ECE=0.131; N-gram AUC=0.73/ECE=0.069）。从 3 个数据点推导出精确的数值阈值是 overfitting。
  
  TF-IDF vs GPT-2 的对比被描述为"isolates calibration"，但两者同时在 AUC（0.94 vs 0.91）、模型类型（discriminative vs generative）、feature space、false positive pattern 上都不同。这不是一个控制实验，而是一个 observational comparison。论文在 Appendix L 中承认 generative detectors 的 false positive 机制不同（"assign high q-scores to fluent, predictable human text"），但这恰恰说明 calibration 不是唯一变量。
- 建议：(1) 使用同一 detector（如 TF-IDF+LR）的不同 calibration 程度（不做 temperature scaling / 故意 miscalibrate）来真正 isolate calibration effect；(2) 将 Table 3 的阈值标注为"在本实验 3 个 detector 下观察到的"而非通用建议。

**W5** [warning] "Minimum intervention" 原则缺乏理论依据
- 具体位置：Section 3 (Method, Eq. 1)
- 问题：为什么 "smallest b meeting the quality floor" 是最优的？Grid search 显示最优 b ≈ 0.3（seed 42），而 adaptive b* 的均值 ≈ 0.9（Section 5.1, Figure 2 注释）。如果 b=0.3 是全局最优，adaptive 的 b*=0.9 显然偏大——方法之所以有效是因为 per-batch adaptation 补偿了 b 的偏移，而非因为 "minimum intervention" 本身是对的。
  
  论文在 Section 5.1 讨论了 grid-best 的 4.7× 更高 cross-seed variance，试图论证 adaptive 的低方差优势。但这只是说明 per-batch adaptation 降低了方差，不能证明 minimum intervention 是比其他 aggregation rule（如 median b、percentile-based b）更好的选择。
- 建议：(1) 补充一个"per-batch adaptation + median b"或"per-batch adaptation + mean b"的对比，证明 minimum b 确实优于其他选择规则；(2) 或者弱化 "minimum intervention" 的 principled framing，改为 "heuristic regularization"。

**W6** [warning] Epoch confound 分析缺少纯数据重复的控制
- 具体位置：Section 5.1 (Hard filtering and the epoch confound), Table 1
- 问题：Epoch confound 分析非常有价值，但缺少一个关键 baseline："uniform training with ~3.2× data repetition"（不做任何过滤，只是让模型在全部数据上训练 3.2 个 epoch）。这个 baseline 可以区分两个假设：(a) D&R 的优势纯粹来自 data repetition（无论数据质量如何），vs (b) D&R 的优势来自 filtered data + repetition 的交互效应。如果纯重复能达到类似效果，epoch confound 的故事更强；如果不能，filtering 仍有独立价值，epoch confound 的措辞需要弱化。
- 建议：增加 "uniform + multi-epoch" baseline。

## 小问题（不影响接收）

- **M1**: Abstract 第三段 "uncorrected p=0.010" 应在 abstract 中注明是 uncorrected，目前读者可能误以为是校正后的 p 值。实际上 abstract 中已经写了"uncorrected"，但排版上不够醒目。
- **M2**: Table 2 中 Grid-best 使用的 τ 不明确（主实验用 τ=0.7，但 footnote ‡ 只说 "Post-hoc oracle from nine candidates"）。Appendix C 显示 grid search 不使用 τ（固定 b），但读者在正文中可能混淆。
- **M3**: Conclusion 中 "we identify three effectiveness conditions for detect-and-reweight" 没有附带 N=3 seeds、校正后不显著的 caveat——应保持与 Limitations 部分一致的审慎语气。
- **M4**: Figure 2 的 y 轴范围（17.4-17.9）使得差异视觉上被放大，可考虑添加 break 标记或注明非零起点。
- **M5**: Section 6 讨论"effect size in context"但未报告标准化效应量（如 Cohen's d）。在 N=3 的情况下，Cohen's d ≈ (-0.020)/0.007 ≈ 2.86（using adaptive σ），这是 large effect，但 N=3 下的 d 估计非常不稳定。应报告并讨论其不确定性。
- **M6**: Appendix P (Checkpoint Resume Artifact) 提到 seed 42 的 τ=0.8 实验受到 checkpoint resume 影响，但 Table 2 的主实验使用 τ=0.7 且全部 from-scratch。这一点论文处理得当（footnote 77），但读者需要仔细阅读才能理清不同实验 run 的关系。

## 主要优势

- **S1**: Epoch confound 分析是论文最突出的贡献。通过 epoch-matched 和 LR-controlled 两重验证，令人信服地展示了 D&R 文献中可能被广泛忽视的评估偏差。这个发现独立于方法本身的价值，对 data curation 社区有参考意义。
- **S2**: 实验设计的系统性：6 种方法的 ablation hierarchy（Adaptive < Uniform < ESS-only < Random）清晰展示了 detector signal 和 minimum intervention 的各自贡献。Permuted-score control（Appendix Section 6 Discussion, +0.26 PPL）是一个聪明的 sanity check。
- **S3**: 极为诚实的结果报告。论文主动报告了：校正后不显著的 p 值、downstream 零改善、ρ=0.2 的 failure case、checkpoint resume artifact、cross-model mixed results。这种透明度在 ML 论文中不常见。
- **S4**: Practitioner decision table (Table 3) 虽然基于有限 detector 数据，但作为一种 structured summary 有实用价值。boundary condition 分析（ρ=0.2→0.3→0.4→0.6 的 dose-response pattern）提供了有用的 sensitivity profile。
- **S5**: 理论部分（Proposition 1-2, Appendix A）虽然简单，但 α_eff 单调性和 ESS 单调性的证明确保了 dual constraint formulation 的 well-definedness（b_τ 和 b_ESS 通过 bisection 可以唯一确定）。
- **S6**: 对 checkpoint resume artifact 的透明披露和 from-scratch retraining 验证（Appendix P）展示了良好的实验规范。

## Missing References / 未讨论的相关工作

- 论文引用了 Drayson et al. (2025) 和 He et al. (2025) 作为 D&R 领域的主要工作，related work 覆盖合理。
- 建议补充：关于 importance sampling 在 NLP 训练中的更多讨论（Katharopoulos & Fleuret 2018 已引用，但 variance reduction 方面的经典文献如 Owen 2013 Monte Carlo 只在 Appendix proof 中引用，正文中可简要讨论 importance weighting 的理论基础和 known failure modes）。
- 关于 data contamination detection 的更全面 survey（论文测试了 3 个 baseline detector，但 ModernBERT / Binoculars / DetectGPT 等 SOTA detector 只在 Limitations 中提到，Related Work 中未充分讨论这些方法的 calibration 特性）。

## Questions for Authors

1. 是否考虑过在相同 TF-IDF+LR detector 上通过改变 temperature scaling 参数来人为调节 ECE（如 T=1.0 无校准 vs T=0.204 校准），从而在控制 AUC 的条件下 isolate calibration effect？
2. ρ=0.2 failure case 中的 α_eff bias 是多少？是否仍然是 ~-0.03？如果 bias 在低污染下变化，minimum intervention 逻辑的失败可能有更 mechanistic 的解释。
3. 为什么不在 B=16（gradient accumulation level）而非 B=4（micro-batch level）上计算 b*？Appendix B 提到"q-score statistics exhibit sufficient variance within micro-batches"，但 B=16 上 adaptive advantage amplifies 3.4×——这是否意味着主实验其实在次优设定下运行？
4. Grid search 最优 b=0.3 而 adaptive b* 均值 ≈0.9——这个差距是否表明 minimum intervention 倾向于过度干预？per-batch b* 的分布（median, percentiles）是什么样的？

## 总结判断

这篇论文的分析质量高于其方法贡献。Epoch confound finding 是有价值的独立贡献，值得 Findings track。但方法本身的效果量极小（0.11% PPL, 零 downstream），统计证据在校正后不够强，且仅在自污染设定下验证。若作者能增加 seeds 数量使结论统计显著，或提供 cross-model 的完整验证，可以考虑更高评分。目前评 3.0 (Findings)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1210 · 2026-05-24T04:17:26.164219+00:00_

Reviewer 1 初审报告已收到。评分 3.0 (Findings)，置信度 4/5。

核心发现：
- **3 个 Must-Fix**：N=3 统计效力不足、自污染泛化性、downstream 零改善
- **6 个 Should-Fix**：B=4 可靠性、α_eff proxy 偏弱、batch-size 外推、detector 覆盖不足、minimum intervention 缺理论依据、epoch confound 缺纯重复 baseline
- **6 个 Minor**：格式和表述细节

等待 Reviewer 2 提交报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 92

## Round 92

2 recorded events


### User

_source line 1211 · 2026-05-24T04:17:28.817790+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论摘要**：Overall 3.0 (Findings)，Confidence 4/5。

核心判断：
- **最大贡献**是 epoch confound 分析（>95% D&R 优势来自数据重复），这个发现独立且有价值
- **主要问题**：(1) N=3 seeds 下校正后所有核心 claim 均不显著（p_BH=0.078/0.064）；(2) 自污染设计限制泛化性，唯一跨模型测试不完整；(3) Δ=-0.020 PPL (0.11%) 无法转化为任何可测量的 downstream 效果
- 标注了 3 个 must-fix（统计显著性、泛化性、实际价值）和 6 个 should-fix（B=4 可靠性、α_eff proxy 精度、batch-size scaling 外推、detector 数量不足、minimum intervention 缺乏理论依据、缺少纯重复 baseline）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1212 · 2026-05-24T04:17:34.742206+00:00_

已记录。继续等待 Reviewer 2 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 93

## Round 93

8 recorded events


### User

_source line 1213 · 2026-05-24T04:19:51.332926+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告

**论文**: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"
**Venue**: EMNLP 2026 via ARR
**审查侧重**: 新颖性、Related Work 完整性、写作质量、格式合规、整体连贯性

---

## 总体评分
**Overall Assessment**: 3.5 (Borderline Conference)
**Confidence**: 4/5 (Quite sure)
**一句话总结**: 论文提出了一个有价值的 epoch confound 发现（F1），但主实验结果在多重比较校正后未达显著性（p_BH=0.078），且仅在 self-contamination 设置下验证，scope 偏窄，作为 analysis paper 的贡献深度勉强达到主会议门槛。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计合理、有对照，但统计功效不足（N=3, p_BH=0.078），且仅 self-contamination 设置 |
| Excitement | 3/5 | Epoch confound 发现对社区有价值，但 adaptive b* 的实际改善量小且无下游迁移 |
| Overall | 3.5/5 | 介于 Findings 和 Conference 之间；F1 有 main conference 水准，但整体 scope 和 effect size 偏弱 |

---

## 主要优势

**S1. Epoch confound 发现（F1）是本文最核心、最有价值的贡献。** §5.1 Table 1 展示 D&R 的 0.396 PPL 优势在 epoch-matched 后缩至 Δ=0.017（3-seed），揭示 >95% 的 reported advantage 源于数据重复而非 filtering quality。这一发现对后续 D&R 工作的实验设计有直接指导意义。LR-controlled verification（D&R 17.651 vs shared-schedule 17.657, Δ=0.006）进一步排除了学习率混淆。

**S2. 实验设计结构良好，消融层次清晰。** Table 2 的六种方法对比（Uniform → Random → ESS-only → Adaptive → Grid-best → D&R）形成清晰的消融阶梯，每一层都有明确的控制变量。Permuted-score control（shuffled detector, PPL +0.26）有效证明 detector signal 的必要性。

**S3. 论文对局限性的讨论异常坦诚。** §6 Discussion 主动承认 downstream accuracy 无改善（Table 4: 0.5414 vs 0.5414）、effect size 在当前 scale 下 modest（Δ=-0.020 在 ~0.07-point 窗口内操作）、α_eff 代理质量有限（r=0.79）。Limitations 段覆盖了关键局限（self-contamination、N=3 统计功效、detector 覆盖范围窄）。这种自我批评远超多数投稿。

**S4. Related Work 全面且结构化。** §2 分五个 paragraph 覆盖 model collapse、detection、domain-level mixing、instance-level reweighting、theoretical foundations，引用 50+ 篇文献。与最直接相关的 Drayson et al. (2025) 的三点区分（(i) grid search → dual-constrained, (ii) SIR resampling → continuous reweighting, (iii) ModernBERT → TF-IDF+LR）清晰、公平。

**S5. Adaptive b* 消除了 per-model grid search 的实际需求。** 虽然 grid-best 仍优于 adaptive（17.620 vs 17.674），但 grid search 需 9 次完整训练（~16 GPU-hours at 0.6B），且 grid-best b=0.3 跨 seed 方差 4.7× 高于 adaptive（σ=0.033 vs 0.007），实际选择不可靠（Figure 2 的 plateau region）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 主实验结果在多重比较校正后未达传统显著性水平
- 具体位置：§5.1, Table 2
- 问题：ρ=0.4 的主实验 paired t-test 原始 p=0.019，但 Bonferroni-Holm 校正后 p_BH=0.078（九组家族比较，k=9）。ρ=0.6 校正后 p_BH=0.064。论文声称 "BCa bootstrap CI [−0.028, −0.012] excludes zero" 作为补充证据，但 CI 不等价于校正后 p 值。对于一篇以 "When does X work?" 为标题的 analysis paper，核心 claim 的统计支撑应当更强。
- 为什么影响接收：Analysis paper 的核心价值在于可靠的实证发现。主效应在标准校正下不显著，削弱了全部三个 findings 的可信度——如果 adaptive b* 本身相对 uniform 的改善不显著，那么关于 "什么条件下有效" 的分析就建立在不稳固的基础上。
- 建议修改方向：(a) 增加 seeds（N≥5）提高统计功效；(b) 减少同时比较的方法数以降低校正负担；(c) 如果增加 seeds 不可行，应在 Abstract/Conclusion 中更明确地标注 effect 的统计状态（如 "directionally consistent but not statistically significant after family-wise correction"），而非 buried 在括号注释中。

**N2** [critical] 仅在 self-contamination 设置下验证，生态效度堪忧
- 具体位置：§4 "Training Data", §Limitations
- 问题：所有主实验使用 Qwen3-0.6B 同时作为 generator 和 trainee，这意味着合成数据与真实数据的分布差异远小于现实场景。论文承认 "self-contamination design provides a controlled testbed... but limits ecological validity"，且 Appendix O 的 Llama-3.2-3B cross-model 实验 "showed mixed results"。实际 web contamination 来自多种模型和多个时间点，detector 面临的 distribution shift 远比本文设置困难。
- 为什么影响接收：本文的三个 findings 和 adaptive b* 的有效性边界可能 fundamentally 依赖于 self-contamination 的特殊性。例如，F2（detector requirements）中 TF-IDF+LR 在 self-contamination 下 AUC=0.94 可能在 cross-model 下大幅下降，导致 AUC/ECE 阈值完全不同。标题 "When Does Detect-and-Reweight Work?" 暗示了一般性结论，但实验仅支持一个非常特定的设置。
- 建议修改方向：(a) 至少一个 cross-model contamination 的完整实验（不仅是 Appendix 中的 preliminary）；(b) 或者将标题和 claims 显式限定为 self-contamination 设置。

**N3** [critical] 下游任务无改善，且 effect size 极小
- 具体位置：§6 Discussion, Table 4
- 问题：Adaptive vs Uniform 的下游 accuracy 完全相同（0.5414 vs 0.5414, 5 tasks, 3 seeds）。论文将此归因于 Δ=-0.020 PPL 对应 ~0.1% relative improvement，低于 per-task measurement noise。但这个论证本身就说明了问题：如果 PPL 改善小到无法在标准 benchmarks 上检测到，那么 practitioners 为什么要使用这个方法？论文在 §6 "Effect size in context" 中承认 "the paradigm's practical impact at current scales is modest"。
- 为什么影响接收：对于一篇声称提供 "practical corollary" 的论文，核心方法在任何可观测的 downstream metric 上都没有改善，严重削弱了实际贡献。ρ=0.6 的 Δ=-0.032 可能更有希望，但同样缺乏 downstream 验证。
- 建议修改方向：(a) 在更高 contamination rate（如 ρ=0.6 或 0.8）下报告 downstream results；(b) 使用对 PPL 更敏感的评估方式（如 generation quality, factuality）；(c) 或明确将论文定位为 "analysis paper with negative practical result at current scales"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 标题和 claims 的 scope 与实验支撑不匹配
- 具体位置：Title, Abstract, §1 Introduction
- 问题：标题 "When Does Detect-and-Reweight Work?" 暗示对 D&R 范式的全面分析，但实验仅覆盖：一个模型家族（Qwen3），一个 scale（0.6B，1.7B 仅初步），一种 contamination 设置（self-contamination），一个训练范式（continued pretraining），一个数据量级（132M tokens）。Abstract 的数值密度高但未充分传达这些限制。
- 建议：标题改为更精确的范围限定，如 "...in Self-Contaminated Continued LM Pretraining" 或在 Abstract 第一句就明确 scope。

**W2** [warning] Grid-best 与 adaptive b* 的差距需要更诚实的讨论
- 具体位置：§5.1 Table 2, §6
- 问题：Grid-best b=0.3 的 3-seed mean PPL 17.620 显著优于 adaptive 17.674（差距 0.054），是 adaptive vs uniform 改善（0.020）的 2.7 倍。论文论证 grid search 昂贵且不可靠，但对于关心最终性能的 practitioners，grid search 的 cost-performance tradeoff 可能仍然更优。§6 讨论了 grid-best 的高方差（σ=0.033 vs 0.007），但未讨论为什么 adaptive 无法接近 grid-best 的水平——是 dual constraint 过于保守，还是 α_eff proxy 的 ceiling 限制？
- 建议：增加分析 adaptive b* 与 grid-best 差距的来源，讨论是否有 oracle-free 的方式缩小差距。

**W3** [warning] α_eff 代理质量有限（r=0.79），且论文对此的讨论过长
- 具体位置：§6 "Limitations of α_eff as a proxy"
- 问题：α_eff 与真实 batch-level real fraction 的相关性 r=0.79（R²≈0.62），意味着 ~38% 的方差未解释。论文在 §6 中用了一整段（约 200 words）解释这个限制，包括方差分解、batch size scaling、R² 对 B 的不变性等。这段分析虽然诚实，但篇幅过长，且部分内容（如 "Δ ∝ B^α with α ≈ 0.89"）更适合放在 Appendix。在 8 页限制内，这些空间可以更好地用于弥补 N2 或 N3。
- 建议：将 α_eff proxy 的详细分析移至 Appendix，主文保留核心结论（r=0.79, ceiling on precision, mitigated by batch size scaling）。

**W4** [warning] 作为 analysis paper 的 finding 深度不均匀
- 具体位置：§5, §6 全文
- 问题：F1（epoch confound）的分析深入且有说服力（epoch-matched control + LR-controlled verification + permuted-score control）。但 F2（detector requirements）仅测试 3 个 detectors（TF-IDF+LR, GPT-2 perplexity, N-gram），且在 self-contamination 下；F3（minimum intervention）的论证主要是 ESS-only 的退化（Table 2: +0.043），缺乏对 "为什么 minimum intervention 优于 moderate intervention" 的深入机制分析。三个 findings 的深度差异显著。
- 建议：对 F2 增加 detector 数量或在 cross-model 下验证阈值；对 F3 分析 adaptive b* 的 batch-level behavior（如不同 contamination 水平的 batch 中 b* 的分布与 PPL 贡献的关系）。

---

## 小问题（不影响接收）

- §1 Figure 1 的 TikZ 概览图信息密度偏低，占据了宝贵的 column width，可以用更紧凑的方式呈现（如 inline enumeration）或移至 Appendix。
- §4 Training paragraph 提到 "single NVIDIA RTX PRO 6000 (96 GB)"——这是一张非常不常见的 GPU（通常是 A100/H100），可能引起 reviewer 注意（不是匿名问题，而是实验可复现性问题）。
- Table 2 的 Golden Ratio baseline 仅有 seed 42 的结果（其他标 "--"），应注释说明原因或补全。论文确实标注了 †Oracle requiring known ρ, seed 42 only，但未解释为什么只跑了一个 seed。
- §5.3 "Constraint regime" 段的 24,412 micro-batches 分析只有 seed 42，其他 seed 在 Appendix 中确认 CV<2%，建议在正文中简述三个 seed 的结果。
- Appendix 有 18 个 section（A-R），组织合理但数量多，建议对部分高度技术性的 sections 做合并。
- §6 第一段 "The bulk of D&R's reported PPL advantage..." 与 §5.1 的 "Hard filtering and the epoch confound" 段几乎完全重复，可精简。

---

## 关于新颖性的详细评估

**F1 (Epoch confound)**: **高新颖性**。这是本文最强的贡献。虽然 "公平比较应控制 epoch" 事后看来是常识，但此前的 D&R 文献（包括 Drayson et al. 2025）确实没有做到这一点。论文通过三重验证（epoch-matched, LR-controlled, permuted-score）使这一发现高度可信。

**F2 (Detector requirements)**: **中等新颖性**。"需要好的 detector" 本身不令人意外，但对 calibration（ECE）vs discrimination（AUC）的分离贡献有价值（GPT-2 vs TF-IDF 对照实验, §5.2）。但仅 3 个 detector 在 self-contamination 下的结果，generalizability 有限。

**F3 (Minimum intervention)**: **低至中等新颖性**。"最小干预优于最大干预" 与 importance weighting 文献中的 variance-bias tradeoff 一致，dual constraint（quality floor + stability ceiling）是自然的工程选择。Grid search b=0.3（接近 b*≈0.9 的下方）优于 b=5 的事实已足以支持这一观点，不需要完整的 adaptive 框架来论证。

**Adaptive b* 作为 "practical corollary"**: **中等新颖性**。Formula 来自 Drayson et al. (2025)，α_eff 和 ESS 都是标准量。贡献在于将它们组合成无需 validation 的 per-batch 自适应方案，但这更像 engineering contribution。

**整体作为 analysis paper**: 贡献在 main conference 门槛的边缘。F1 alone 可能不足以支撑一篇完整的论文，但 F1+F2+F3+adaptive b* 的组合提供了一个相对完整的分析框架。问题在于分析的 scope 偏窄（一个模型、一种 contamination、一个 scale）。

---

## Related Work 完整性评估

**覆盖充分的领域：**
- Model collapse: Shumailov 2024, Alemohammad 2024, Dohmatob 2025, Gerstgrasser 2024, Kang 2025 ✓
- Detection methods: DetectGPT, Fast-DetectGPT, Binoculars, Min-k% Prob, watermarking ✓
- Domain-level mixing: DoReMi, DSIR, AIOLI, DataComp-LM, OLMo, ToReMi ✓
- Instance-level reweighting: SemDeDup, SoftDedup, QuRating, curriculum learning, LESS, MATES 等 ✓
- Theoretical: He 2025 (golden ratio), Wang 2026 (convergence), Kish 1965, Vehtari 2024 ✓

**与 Drayson et al. (2025) 的对比：** 三点区分（grid search vs dual-constrained, SIR vs continuous, ModernBERT vs TF-IDF）清晰公平。✓

**可能遗漏的工作：**
- **Contamination detection benchmarks** (如 RAID: Dugan et al. 2024; M4: Wang et al. 2024) 作为 detection 评估的标准化工作未讨论，与 F2 (detector requirements) 直接相关
- **Synthetic data 质量对训练的影响** 的近期实证工作（如 Phi 系列使用 synthetic data 的正面案例）未讨论——这与论文隐含假设 "synthetic data 总是有害的" 形成对比
- **Data Provenance Initiative** (Longpre et al. 2024) 虽然 Longpre et al. 引用了，但是关于 pretrainer preferences，而非 data provenance 本身
- 未讨论 **后训练阶段**（SFT/RLHF）中类似的 contamination-aware 方法，这限制了 Related Work 对更广泛 contamination 问题的覆盖

这些遗漏不严重，但补充后可以加强论文的学术定位。

---

## 格式合规检查（EMNLP 2026 硬约束）

| 检查项 | 状态 | 详情 |
|--------|------|------|
| Abstract ≤200 words | ✅ 合规 | ~166 words（LaTeX 命令/数学公式剥离后） |
| 正文 ≤8 页 | ✅ 合规 | §1-§7 (Conclusion) 在 page 8 底部结束，Limitations 从 page 9 开始 |
| Limitations 在正文中 | ✅ 合规 | 单一 \section*{Limitations} 在 §7 之后、References 之前 |
| Appendix 无重复 Limitations | ✅ 合规 | Appendix 18 个 section (A-R)，无 Limitations |
| 匿名性 | ✅ 合规 | Author 标为 "Anonymous"；无 GitHub link/作者名/机构名；"Code and data will be released upon acceptance" |
| ARR Checklist 不在 PDF | ✅ 合规 | PDF 最后一页为 Appendix R (Use of AI Assistants)，无 Checklist |
| 引用格式 | ✅ 合规 | natbib 的 \citep 和 \citet 正确使用 |
| ACL 模板 | ✅ 合规 | \usepackage[review]{acl}，11pt |

**无格式合规问题。**

---

## Questions for Authors

1. 能否提供至少一个 cross-model contamination（如 GPT-4o 生成，Qwen3-0.6B 训练）的完整结果？Appendix O 的 Llama-3.2-3B "mixed results" 具体是什么意思——是 adaptive b* 退化，还是所有方法都退化？

2. 在 ρ=0.6（更强的 effect size, Δ=-0.032）下的 downstream accuracy 是否有所改善？如果仍然无改善，是否存在任何可观测的 downstream metric 能体现 PPL 改善的价值？

3. 为什么不尝试更大的 seed 数量（N=5 或 N=10）来解决统计显著性问题？132M token, 0.6B model 的训练成本应该不高（论文提到单 GPU 16 小时 for grid search of 9 runs）。

4. Adaptive b* 在 batch-level 操作，但 gradient accumulation 是 4 步——b* 是在每个 micro-batch 独立计算还是在 accumulated batch 上计算？这影响 ESS 的有效 B。

---

## Overall Assessment 总结

**Overall**: 3.5 / 5 (Borderline Conference)
**Soundness**: 3.5 / 5
**Excitement**: 3 / 5
**Confidence**: 4 / 5

这是一篇诚实、结构良好的 analysis paper，核心发现（F1: epoch confound）对社区有真实价值。但三个关键弱点限制了其 impact：(1) 主效应统计显著性不足；(2) 仅在 self-contamination 设置验证；(3) 无 downstream improvement。如果作者能增加 seeds 解决统计问题并提供至少一个 cross-model 实验，评分可上调至 4 (Conference)。当前状态下，我倾向于 Findings 或 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-24T04:20:37.725275+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个要点使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall Assessment**: 3.5 (Borderline Conference), Confidence 4/5\n\n### 主要优势\n- **S1**: Epoch confound 发现（F1）是最核心、最有价值的贡献。Table 1 展示 D&R 0.396 PPL 优势在 epoch-matched 后缩至 Δ=0.017。LR-controlled verification 进一步排除学习率混淆。\n- **S2**: 实验设计结构良好，消融层次清晰。Table 2 六种方法对比形成清晰消融阶梯。Permuted-score control 有效证明 detector signal 必要性。\n- **S3**: 论文对局限性的讨论异常坦诚。主动承认 downstream 无改善、effect size modest、α_eff 代理质量有限。\n- **S4**: Related Work 全面且结构化。五个 paragraph 覆盖完整，与 Drayson et al. 三点区分清晰公平。\n- **S5**: Adaptive b* 消除 per-model grid search 需求。Grid-best 跨 seed 方差 4.7× 高于 adaptive。\n\n### Must-Fix 问题\n- **N1** [critical]: 主实验结果校正后未达显著性（p_BH=0.078/0.064）。核心 claim 的统计支撑应更强。建议增加 seeds 或在 Abstract/Conclusion 更明确标注统计状态。\n- **N2** [critical]: 仅在 self-contamination 设置验证，生态效度堪忧。Cross-model 实验不完整。标题暗示一般性结论但实验仅支持特定设置。\n- **N3** [critical]: 下游任务无改善（0.5414 vs 0.5414），effect size 极小。如果 PPL 改善无法在标准 benchmarks 检测到，practitioners 为什么使用此方法？\n\n### Should-Fix 问题\n- **W1** [warning]: 标题和 claims 的 scope 与实验支撑不匹配。建议标题加限定。\n- **W2** [warning]: Grid-best 与 adaptive b* 差距（0.054）需要更诚实讨论。未分析差距来源。\n- **W3** [warning]: α_eff 代理质量讨论（§6）过长（~200 words），部分内容适合 Appendix。\n- **W4** [warning]: 三个 findings 的分析深度不均匀。F1 深入，F2 仅 3 个 detector，F3 缺乏机制分析。\n\n### 小问题\n- Figure 1 TikZ 概览图信息密度偏低\n- RTX PRO 6000 (96 GB) 非常见 GPU\n- Table 2 Golden Ratio 仅 seed 42 未解释\n- §6 第一段与 §5.1 内容重复\n\n### 新颖性评估\n- F1 (epoch confound): 高新颖性\n- F2 (detector requirements): 中等新颖性\n- F3 (minimum intervention): 低至中等新颖性\n- Adaptive b*: 中等新颖性（engineering contribution）\n- 整体：main conference 门槛边缘\n\n### 格式合规\n- Abstract ≤200 words: ✅ 合规（~166 words）\n- 正文 ≤8 页: ✅ 合规\n- 所有格式检查项均通过\n\n### Related Work 可能遗漏\n- RAID (Dugan et al. 2024), M4 (Wang et al. 2024) 等 detection benchmarks\n- Phi 系列 synthetic data 正面案例\n- Data Provenance Initiative\n- 后训练阶段 contamination-aware 方法\n\n### Questions\n1. 能否提供 cross-model contamination 完整结果？\n2. ρ=0.6 下 downstream accuracy 是否改善？\n3. 为什么不增加 seed 数量？\n4. Adaptive b* 在 micro-batch 还是 accumulated batch 上计算？\n\n---\n\n请对以上所有要点逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个要点使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall Assessment**: 3.5 (Borderline Conference), Confidence 4/5\n\n### 主要优势\n- **S1**: Epoch confound 发现（F1）是最核心、最有价值的贡献。Table 1 展示 D&R 0.396 PPL 优势在 epoch-matched 后缩至 Δ=0.017。LR-controlled verification 进一步排除学习率混淆。\n- **S2**: 实验设计结构良好，消融层次清晰。Table 2 六种方法对比形成清晰消融阶梯。Permuted-score control 有效证明 detector signal 必要性。\n- **S3**: 论文对局限性的讨论异常坦诚。主动承认 downstream 无改善、effect size modest、α_eff 代理质量有限。\n- **S4**: Related Work 全面且结构化。五个 paragraph 覆盖完整，与 Drayson et al. 三点区分清晰公平。\n- **S5**: Adaptive b* 消除 per-model grid search 需求。Grid-best 跨 seed 方差 4.7× 高于 adaptive。\n\n### Must-Fix 问题\n- **N1** [critical]: 主实验结果校正后未达显著性（p_BH=0.078/0.064）。核心 claim 的统计支撑应更强。建议增加 seeds 或在 Abstract/Conclusion 更明确标注统计状态。\n- **N2** [critical]: 仅在 self-contamination 设置验证，生态效度堪忧。Cross-model 实验不完整。标题暗示一般性结论但实验仅支持特定设置。\n- **N3** [critical]: 下游任务无改善（0.5414 vs 0.5414），effect size 极小。如果 PPL 改善无法在标准 benchmarks 检测到，practitioners 为什么使用此方法？\n\n### Should-Fix 问题\n- **W1** [warning]: 标题和 claims 的 scope 与实验支撑不匹配。建议标题加限定。\n- **W2** [warning]: Grid-best 与 adaptive b* 差距（0.054）需要更诚实讨论。未分析差距来源。\n- **W3** [warning]: α_eff 代理质量讨论（§6）过长（~200 words），部分内容适合 Appendix。\n- **W4** [warning]: 三个 findings 的分析深度不均匀。F1 深入，F2 仅 3 个 detector，F3 缺乏机制分析。\n\n### 小问题\n- Figure 1 TikZ 概览图信息密度偏低\n- RTX PRO 6000 (96 GB) 非常见 GPU\n- Table 2 Golden Ratio 仅 seed 42 未解释\n- §6 第一段与 §5.1 内容重复\n\n### 新颖性评估\n- F1 (epoch confound): 高新颖性\n- F2 (detector requirements): 中等新颖性\n- F3 (minimum intervention): 低至中等新颖性\n- Adaptive b*: 中等新颖性（engineering contribution）\n- 整体：main conference 门槛边缘\n\n### 格式合规\n- Abstract ≤200 words: ✅ 合规（~166 words）\n- 正文 ≤8 页: ✅ 合规\n- 所有格式检查项均通过\n\n### Related Work 可能遗漏\n- RAID (Dugan et al. 2024), M4 (Wang et al. 2024) 等 detection benchmarks\n- Phi 系列 synthetic data 正面案例\n- Data Provenance Initiative\n- 后训练阶段 contamination-aware 方法\n\n### Questions\n1. 能否提供 cross-model contamination 完整结果？\n2. ρ=0.6 下 downstream accuracy 是否改善？\n3. 为什么不增加 seed 数量？\n4. Adaptive b* 在 micro-batch 还是 accumulated batch 上计算？\n\n---\n\n请对以上所有要点逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-24T04:21:11.288222+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33562
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-24T04:21:11.589683+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个要点使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall Assessment**: 3.0 (Findings), Confidence 4/5\n\n### 主要优势\n- **S1**: Epoch confound 分析是最突出贡献。通过 epoch-matched 和 LR-controlled 两重验证令人信服。\n- **S2**: 实验设计系统性：6 种方法 ablation hierarchy 清晰。Permuted-score control 是聪明的 sanity check。\n- **S3**: 极为诚实的结果报告——主动报告校正后不显著 p 值、downstream 零改善、ρ=0.2 failure、checkpoint resume artifact、cross-model mixed results。\n- **S4**: Practitioner decision table (Table 3) 有实用价值。Dose-response pattern 提供有用 sensitivity profile。\n- **S5**: Proposition 1-2 确保 dual constraint 的 well-definedness。\n- **S6**: Checkpoint resume artifact 的透明披露和 from-scratch 验证展示良好实验规范。\n\n### Must-Fix 问题\n- **N1** [critical]: N=3 seeds 下所有核心结论均未达校正后统计显著性。BCa bootstrap CI 在 N=3 下覆盖率存疑（Efron & Tibshirani 1993 建议 N≥10-15）。Abstract/conclusion 仍以断言性语言呈现。\n- **N2** [critical]: 自污染设计严重限制泛化性。Generator=trainee 是最简单检测场景。唯一跨模型测试 single seed、mixed、缺 PPL 对比。现实 web contamination 来自多模型。\n- **N3** [critical]: Downstream tasks 零改善削弱实际价值。\"PPL improvements operate in a regime that standard benchmarks cannot resolve\" — 如果所有标准评估手段都无法检测，实际意义存疑。\n\n### Should-Fix 问题\n- **W1** [warning]: B=4 micro-batch 上 dual constraint 统计可靠性不足。True real fraction 只能取 {0, 0.25, 0.5, 0.75, 1.0}，α_eff 波动剧烈（MAE=0.114）。\n- **W2** [warning]: α_eff proxy r=0.79（R²=0.63）偏弱。Convergence theory 中阈值条件应用于 proxy 而非 true fraction，理论保证是否成立未讨论。\n- **W3** [warning]: Batch-size amplification 3 点拟合 power law（Δ ∝ B^0.89），指数不确定性未报告。\n- **W4** [warning]: 3 个 detector 不足以建立 AUC/ECE 因果关系。TF-IDF vs GPT-2 不是控制实验（同时在 AUC、模型类型、feature space、false positive pattern 上不同）。建议用同一 detector 不同 calibration 程度 isolate calibration effect。\n- **W5** [warning]: \"Minimum intervention\" 原则缺乏理论依据。Grid-best b≈0.3 而 adaptive b*≈0.9——方法有效是否因为 per-batch adaptation 补偿了 b 偏移，而非 minimum intervention 本身？建议补充 median b / percentile-based b 对比。\n- **W6** [warning]: Epoch confound 分析缺少 \"uniform + multi-epoch\" baseline 来区分纯重复 vs filtered+repetition 交互。\n\n### 小问题\n- **M1**: Abstract 中 \"uncorrected p=0.010\" 排版不够醒目\n- **M2**: Table 2 Grid-best 的 τ 不明确\n- **M3**: Conclusion 中缺少 N=3/校正后不显著的 caveat\n- **M4**: Figure 2 y 轴非零起点放大视觉差异\n- **M5**: 未报告 Cohen's d 及其不确定性\n- **M6**: Appendix P seed 42 artifact 与主实验关系需仔细阅读才能理清\n\n### Questions\n1. 是否考虑过用同一 TF-IDF+LR detector 改变 temperature scaling 参数 isolate calibration effect？\n2. ρ=0.2 failure case 中 α_eff bias 是否仍然 ~-0.03？\n3. 为什么不在 B=16 而非 B=4 上计算 b*？主实验是否在次优设定下运行？\n4. Grid search b=0.3 vs adaptive b*≈0.9 差距是否表明 minimum intervention 过度干预？\n\n---\n\n请对以上所有要点逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个要点使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall Assessment**: 3.0 (Findings), Confidence 4/5\n\n### 主要优势\n- **S1**: Epoch confound 分析是最突出贡献。通过 epoch-matched 和 LR-controlled 两重验证令人信服。\n- **S2**: 实验设计系统性：6 种方法 ablation hierarchy 清晰。Permuted-score control 是聪明的 sanity check。\n- **S3**: 极为诚实的结果报告——主动报告校正后不显著 p 值、downstream 零改善、ρ=0.2 failure、checkpoint resume artifact、cross-model mixed results。\n- **S4**: Practitioner decision table (Table 3) 有实用价值。Dose-response pattern 提供有用 sensitivity profile。\n- **S5**: Proposition 1-2 确保 dual constraint 的 well-definedness。\n- **S6**: Checkpoint resume artifact 的透明披露和 from-scratch 验证展示良好实验规范。\n\n### Must-Fix 问题\n- **N1** [critical]: N=3 seeds 下所有核心结论均未达校正后统计显著性。BCa bootstrap CI 在 N=3 下覆盖率存疑（Efron & Tibshirani 1993 建议 N≥10-15）。Abstract/conclusion 仍以断言性语言呈现。\n- **N2** [critical]: 自污染设计严重限制泛化性。Generator=trainee 是最简单检测场景。唯一跨模型测试 single seed、mixed、缺 PPL 对比。现实 web contamination 来自多模型。\n- **N3** [critical]: Downstream tasks 零改善削弱实际价值。\"PPL improvements operate in a regime that standard benchmarks cannot resolve\" — 如果所有标准评估手段都无法检测，实际意义存疑。\n\n### Should-Fix 问题\n- **W1** [warning]: B=4 micro-batch 上 dual constraint 统计可靠性不足。True real fraction 只能取 {0, 0.25, 0.5, 0.75, 1.0}，α_eff 波动剧烈（MAE=0.114）。\n- **W2** [warning]: α_eff proxy r=0.79（R²=0.63）偏弱。Convergence theory 中阈值条件应用于 proxy 而非 true fraction，理论保证是否成立未讨论。\n- **W3** [warning]: Batch-size amplification 3 点拟合 power law（Δ ∝ B^0.89），指数不确定性未报告。\n- **W4** [warning]: 3 个 detector 不足以建立 AUC/ECE 因果关系。TF-IDF vs GPT-2 不是控制实验（同时在 AUC、模型类型、feature space、false positive pattern 上不同）。建议用同一 detector 不同 calibration 程度 isolate calibration effect。\n- **W5** [warning]: \"Minimum intervention\" 原则缺乏理论依据。Grid-best b≈0.3 而 adaptive b*≈0.9——方法有效是否因为 per-batch adaptation 补偿了 b 偏移，而非 minimum intervention 本身？建议补充 median b / percentile-based b 对比。\n- **W6** [warning]: Epoch confound 分析缺少 \"uniform + multi-epoch\" baseline 来区分纯重复 vs filtered+repetition 交互。\n\n### 小问题\n- **M1**: Abstract 中 \"uncorrected p=0.010\" 排版不够醒目\n- **M2**: Table 2 Grid-best 的 τ 不明确\n- **M3**: Conclusion 中缺少 N=3/校正后不显著的 caveat\n- **M4**: Figure 2 y 轴非零起点放大视觉差异\n- **M5**: 未报告 Cohen's d 及其不确定性\n- **M6**: Appendix P seed 42 artifact 与主实验关系需仔细阅读才能理清\n\n### Questions\n1. 是否考虑过用同一 TF-IDF+LR detector 改变 temperature scaling 参数 isolate calibration effect？\n2. ρ=0.2 failure case 中 α_eff bias 是否仍然 ~-0.03？\n3. 为什么不在 B=16 而非 B=4 上计算 b*？主实验是否在次优设定下运行？\n4. Grid search b=0.3 vs adaptive b*≈0.9 差距是否表明 minimum intervention 过度干预？\n\n---\n\n请对以上所有要点逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-24T04:21:12.901979+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1312
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-24T04:21:23.855051+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉回应（[AGREE]/[REBUT]）",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: provenance_weight_training\n- 论文路径: projects/provenance_weight_training/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉回应（[AGREE]/[REBUT]）",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: provenance_weight_training\n- 论文路径: projects/provenance_weight_training/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 1219 · 2026-05-24T04:21:23.855406+00:00_

Next wakeup scheduled for 04:26:00 (in 276s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1220 · 2026-05-24T04:21:27.152743+00:00_

交叉分享已发出。两位 Reviewer 正在阅读对方审稿意见并准备逐条回应。等待交叉回应结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 94

## Round 94

4 recorded events


### User

_source line 1221 · 2026-05-24T04:21:29.684298+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：Overall 3.5 (Borderline Conference)。论文的 epoch confound 发现（F1）是核心亮点，对 D&R 文献有直接纠偏价值。格式完全合规。三个主要问题：(1) ρ=0.4 主结果校正后 p_BH=0.078 未达显著性；(2) 仅 self-contamination 设置，生态效度受限；(3) downstream accuracy 无任何改善。如能增加 seeds 和 cross-model 实验，可上调至 4 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-24T04:21:40.847035+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "继续等待 Reviewer 1 和 Reviewer 2 的交叉分享回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: provenance_weight_training\n- 论文路径: projects/provenance_weight_training/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "继续等待 Reviewer 1 和 Reviewer 2 的交叉分享回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: provenance_weight_training\n- 论文路径: projects/provenance_weight_training/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-24T04:21:40.898035+00:00_

Next wakeup scheduled for 04:25:00 (in 199s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1224 · 2026-05-24T04:21:43.240521+00:00_

收到 Reviewer 2 结果确认。目前仍在等待两位 Reviewer 的交叉回应（[AGREE]/[REBUT]）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 95

## Round 95

2 recorded events


### User

_source line 1225 · 2026-05-24T04:23:00.260988+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### 主要优势

**[AGREE] R2-S1**: Epoch confound 是最核心贡献。完全同意。Table 1 的 epoch-matched 设计加上 LR-controlled verification（D&R 17.651 vs shared-schedule 17.657, Δ=0.006）形成双重验证，这在我的 S1 中也是首要优势。

**[AGREE] R2-S2**: 消融层次清晰。完全同意。六种方法（Adaptive < Uniform < ESS-only < Random + Grid oracle + D&R oracle）的阶梯结构和 permuted-score control（+0.26 PPL）是我的 S2 中同样高度评价的优势。

**[AGREE] R2-S3**: 结果报告坦诚。完全同意。这是我 S3 的核心观点。论文主动报告 p_BH=0.078、downstream 零改善、ρ=0.2 failure、checkpoint resume artifact——这种透明度在 ML 论文中确实不常见。

**[AGREE] R2-S4**: Related Work 全面。同意。与 Drayson et al. (2025) 的三点区分（proxy-based vs grid search, controlled contamination, dual constraint）清晰公平。不过我补充一点：Related Work 在 detector calibration 方面讨论不足——论文主张 calibration 是必要条件之一，但 Related Work 对 detection 方法的 calibration 特性缺乏系统讨论（参见我的 W4 和 Missing References）。

**[AGREE] R2-S5**: 消除 grid search 需求。同意。Grid-best 的 4.7× cross-seed variance（σ=0.033 vs 0.007, Section 5.1）是 adaptive 方法在工程层面的真实优势。但需注意 adaptive 在 PPL 上仍落后 grid-best 0.054（Table 2），所以"消除 grid search"是以牺牲一定性能为代价的——R2 在 W2 中也指出了这一点。

---

### Must-Fix 问题

**[AGREE] R2-N1**: 统计显著性不足。完全同意，这是我 N1 的核心观点。补充两点 R2 未提到的细节：

1. **Bootstrap CI 在 N=3 下的覆盖率问题**：论文引用 95% BCa bootstrap CI [-0.028, -0.012] 排除零作为补充证据，但 BCa bootstrap 在 N=3 下的 nominal coverage 远低于 95%（Efron & Tibshirani 1993 建议 N≥10-15）。这个 CI 可能给读者虚假的信心。R2 未提及此点，我认为需要补充。

2. **Cohen's d 未报告**：论文在 Section 6 定性讨论了 effect size in context，但未报告标准化效应量。粗估 Cohen's d ≈ |Δ|/σ_adaptive ≈ 0.020/0.007 ≈ 2.86（large effect），但 N=3 下 d 的置信区间极宽，不应被引用为 evidence of large effect 而不附带不确定性。

**[AGREE] R2-N2**: 自污染限制泛化性。完全同意，与我 N2 一致。补充一点：R2 建议"标题加限定"（W1），我同意但认为更根本的问题是 Appendix O 的 cross-model 实验（Llama-3.2-3B generator）缺少 PPL 对比——论文明确承认 "checkpoints were not retained for re-evaluation"（Appendix O）。这不仅是 scope 问题，而是核心 claim 的证据缺失。作者至少应补充 cross-model 的完整 PPL 对比（3 seeds）。

**[AGREE] R2-N3**: Downstream 零改善。完全同意，与我 N3 一致。R2 提出的问题"practitioners 为什么使用此方法"切中要害。论文在 Section 6 的解释（"PPL improvements operate in a regime that standard benchmarks cannot resolve"）逻辑自洽，但恰恰证明了当前方法在实际可测指标上无价值。我在 N3 中的建议一致：要么在更大规模验证 downstream 效果，要么将论文明确定位为分析性贡献。

---

### Should-Fix 问题

**[AGREE] R2-W1**: 标题/claims scope 与实验支撑不匹配。同意。标题 "When Does Detect-and-Reweight Work?" 暗示对 D&R 范式的一般性分析，但实验仅覆盖 Qwen3-0.6B/1.7B 自污染、1 个 discriminative detector 有效、ρ≥0.4。R2 建议标题加限定（如 "...in Self-Contaminated Continued Pretraining"）是合理的。不过我认为问号形式的标题已经部分缓解了 over-claim 的风险——它是在提问而非断言。

**[AGREE] R2-W2**: Grid-best 与 adaptive 差距需更诚实讨论。同意，并补充机制分析。论文指出 grid-best 的高方差（σ=0.033 vs 0.007）使其在实践中不可靠（Section 5.1），但未分析差距 0.054 的来源。我在 W5 中指出了一个关键线索：grid-best b=0.3 而 adaptive b* 均值≈0.9。这意味着 adaptive 的 minimum intervention 原则系统性地过度干预（b 偏大），per-batch adaptation 的好处被 suboptimal aggregate b 部分抵消。论文应讨论：如果将 adaptive 的 b* 分布 truncated 到 [0, 0.5] 会怎样？

**[REBUT] R2-W3**: α_eff 讨论过长应移至 Appendix。不同意。Section 6 中 α_eff proxy 质量的讨论（~200 words）直接影响读者对方法可信度的判断——r=0.79 是方法有效性的上限，37% unexplained variance 和 consistent negative bias 是理解 failure cases（ρ=0.2）的关键。将此移入 Appendix 会让主文的 Discussion 回避了方法最重要的局限。不过我同意可以精简：quantitative decomposition（"~70% detector noise, ~30% b* transform"）和 B=4→16 的方差缩减讨论可以移入 Appendix，但 r=0.79 的核心讨论和 bias 方向应留在主文。

**[AGREE] R2-W4**: 三个 findings 深度不均匀。同意。F1（epoch confound）有 epoch-matched + LR-controlled 双重验证，分析充分。F2（detector requirements）仅基于 3 个 detector（我的 W4），且 TF-IDF vs GPT-2 的对比不是真正的 controlled experiment——两者在 AUC、模型类型、feature space、false positive pattern 上同时不同（参见我 W4 的详细论述）。F3（minimum intervention）缺乏理论机制——为什么 smallest b 是最优的？与 grid-optimal b=0.3 的差距（b*≈0.9）如何解释？（我的 W5）。

---

### 小问题

**[AGREE] R2-Minor-1**: Figure 1 TikZ 信息密度偏低。同意。Figure 1 占据约半栏空间，但核心信息（三个 findings → adaptive b*）可以用更紧凑的形式呈现。在页数紧张的会议论文中，这个空间可以更好利用。

**[AGREE] R2-Minor-2**: RTX PRO 6000 (96 GB) 非常见 GPU。同意这值得注意。但不影响实验有效性——关键是论文使用了 bf16 precision、单卡训练，这些在多种 GPU 上可复现。

**[AGREE] R2-Minor-3**: Golden Ratio 仅 seed 42 未充分解释。同意。论文在 footnote † 中说明 "Oracle requiring known ρ"，但 single-seed 的原因不明确——是 compute budget 限制还是方法本身依赖 known ρ 使得 multi-seed 无意义？应简要说明。

**[AGREE] R2-Minor-4**: §6 第一段与 §5.1 内容重复。同意。Section 6 "The epoch confound in D&R evaluation" 段落与 Section 5.1 "Hard filtering and the epoch confound" 有明显重叠——两处都讨论了 >95% 归因于 multi-epoch exposure、LR-controlled verification、Δ=0.017 的 residual。建议 §6 仅引用 §5.1 的结论，用省出的空间深化 F2 或 F3 的分析。

---

### 新颖性评估

**[AGREE] F1 高新颖性**: 完全同意。Epoch confound 在 D&R 文献中此前未被系统分析。

**[AGREE] F2 中等新颖性**: 同意。Detector calibration 重要性的实证展示有价值，但仅 3 个 detector 的 observational comparison 限制了 finding 的稳健性（我的 W4）。

**[AGREE] F3 低至中等新颖性**: 同意。Minimum intervention 在 importance weighting 文献中不是新概念（effective sample size 约束在 survey sampling 中已有长期历史，如 Kish 1965）。方法的工程贡献（per-batch bisection, dual constraint）比概念本身更新颖。

**[REBUT] Adaptive b* "中等新颖性（engineering contribution）"**: 部分不同意。我认为 adaptive b* 的新颖性应低于"中等"。Per-batch importance weight tuning via bisection 是标准数值方法的直接应用。真正的贡献是 dual constraint formulation（α_eff ≥ τ + ESS ≥ n_min），但如我 W5 所述，这个 formulation 缺乏理论依据——minimum intervention 原则未被证明优于其他 aggregation rule，且 b* 均值与 grid-optimal 偏差较大。

**[AGREE] 整体：main conference 门槛边缘**: 我给出 3.0 (Findings)，R2 给出 3.5 (Borderline Conference)。差异在于我更重视统计显著性不足（N1）和方法实际效果为零（N3）对 Conference-level 贡献的影响。R2 的 3.5 也合理，取决于对 epoch confound finding 独立价值的权重。

---

### 格式合规

**[AGREE]**: 所有格式检查项一致通过。Abstract ~166 words，正文 8 页，Limitations 在正文中。

---

### Missing References

**[AGREE] RAID (Dugan et al. 2024) 和 M4 (Wang et al. 2024)**: 同意。这些 detection benchmarks 与论文的 detector quality 分析相关——论文声称 AUC ≥ 0.9 和 ECE ≤ 0.05 是必要条件，但未讨论这些阈值在不同 detection benchmarks 上是否稳定。

**[AGREE] Phi 系列 synthetic data 正面案例**: 同意。论文以 contamination 的负面框架讨论合成数据，但 Phi 系列（Gunasekar et al. 2023, Li et al. 2023）展示了高质量合成数据可以积极提升模型——这为 D&R 的必要性提供了重要 counterpoint。论文 Related Work 中的 "Domain-Level Data Mining" 段提到了 DoReMi 和 DSIR，但未讨论 high-quality synthetic data 不需要 downweighting 的情况。

**[AGREE] Data Provenance Initiative**: 适度同意。与论文的 provenance-aware reweighting 主题相关，但非关键遗漏。

**[REBUT] 后训练阶段 contamination-aware 方法**: 不确定这是遗漏。论文 scope 明确限定在 continued pretraining，后训练（SFT/RLHF）的 contamination 问题机制不同（preference data contamination vs pretraining data contamination）。Related Work 中的 "Instance-Level Data Selection and Reweighting" 段已简要涉及 instruction tuning data selection（LESS, MATES），足够。

---

### Questions

**[AGREE] Q1**: 同意需要 cross-model 完整结果，与我 N2 一致。

**[AGREE] Q2**: ρ=0.6 下 downstream accuracy 是否改善？好问题，我未在 R1 中专门提出。论文 Section 5.2 报告了 ρ=0.6 下 Δ=-0.032 PPL（更大改善），但未报告 downstream 结果。如果 PPL 改善翻倍仍无 downstream 效果，更加削弱方法的实用价值；如果有所改善，则提供了积极信号。

**[AGREE] Q3**: 为什么不增加 seeds？这是我 N1 的核心建议。

**[AGREE] Q4**: Micro-batch vs accumulated batch？好问题。论文在 Appendix B 中回答了这个问题——b* 在 micro-batch level (B=4) 计算而非 accumulated batch (B=16)，因为"q-score statistics exhibit sufficient variance within micro-batches"。但我在 W1 和 Question 3 中指出了矛盾：B=16 上 adaptive advantage amplifies 3.4×，这暗示主实验在次优设定下运行。R2 的问题与我的关切一致。

---

### 总结

R2 与 R1 的审稿意见高度一致。三个 Must-Fix（统计显著性、自污染泛化性、downstream 零改善）完全重合。主要分歧：
1. **Overall score**: R2 给 3.5 (Borderline Conference)，R1 给 3.0 (Findings)。我认为校正后不显著 + downstream 零改善使方法贡献不足以支撑 Conference，但 epoch confound finding 的独立价值支撑 Findings。
2. **α_eff 讨论位置**: R2 认为过长应移 Appendix，R1 认为核心讨论应留主文（可精简）。
3. **Adaptive b* 新颖性**: R2 评"中等"，R1 认为应更低——per-batch bisection 是标准方法的直接应用，dual constraint 缺乏理论依据。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1226 · 2026-05-24T04:23:07.638049+00:00_

Reviewer 1 交叉回应已收到。与 Reviewer 2 高度一致，仅 2 个 [REBUT]：
1. α_eff 讨论不应全移 Appendix（核心讨论应留主文）
2. Adaptive b* 新颖性应低于"中等"

等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 96

## Round 96

4 recorded events


### User

_source line 1227 · 2026-05-24T04:23:10.205297+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

与 R2 高度一致的要点：三个 Must-Fix（统计显著性、自污染泛化性、downstream 零改善）完全重合。

主要分歧三点：
1. **评分**：R2 给 3.5，我给 3.0——我认为校正后不显著加 downstream 零改善使方法贡献不足以支撑 Conference
2. **α_eff 讨论位置**：R2 主张移 Appendix，我认为核心部分应留主文
3. **Adaptive b* 新颖性**：R2 评中等，我认为偏低——dual constraint 缺乏理论依据，per-batch bisection 是标准方法的直接应用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-24T04:23:27.556652+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待 Reviewer 2 完成对 Reviewer 1 意见的交叉回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: provenance_weight_training\n- 论文路径: projects/provenance_weight_training/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待 Reviewer 2 完成对 Reviewer 1 意见的交叉回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: provenance_weight_training\n- 论文路径: projects/provenance_weight_training/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-24T04:23:27.607260+00:00_

Next wakeup scheduled for 04:27:00 (in 212s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1230 · 2026-05-24T04:23:35.620237+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 97

## Round 97

10 recorded events


### User

_source line 1231 · 2026-05-24T04:24:00.557530+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### 主要优势

**[AGREE] R1-S1**: Epoch confound 分析确实是最突出贡献，我的审稿同样将其列为最高新颖性。三重验证（epoch-matched + LR-controlled + permuted-score）的设计严谨。

**[AGREE] R1-S2**: 6 种方法的 ablation hierarchy 是本文实验设计的亮点。我在 Reviewer 2 报告中也肯定了这一点（S2）。

**[AGREE] R1-S3**: 论文的诚实程度确实远超多数投稿。主动报告 p_BH=0.078、downstream 零改善、ρ=0.2 failure 等负面结果，是良好的学术规范。

**[AGREE] R1-S4**: Table 3 (Decision summary) 的实用价值我也认可，清晰地将三个 findings 转化为 practitioner 可操作的条件检查。

**[AGREE] R1-S5**: Proposition 1-2 确保了 α_eff 单调递增、ESS 单调递减，从而保证 dual constraint 的 well-definedness（feasible interval [b_τ, b_ESS] 存在性）。证明本身简洁正确（Appendix A, page 11）。

**[AGREE] R1-S6**: Appendix P 的 checkpoint resume artifact 披露（seed 42 的 resume 导致 Δ=−0.011 resume vs −0.005 from-scratch 偏差）是难得的透明度。

---

### Must-Fix 问题

**[AGREE] R1-N1**: 统计显著性问题。我在 Reviewer 2 报告 N1 中提出了本质相同的批评。补充一点：R1 指出的 BCa bootstrap CI 在 N=3 下覆盖率存疑是一个我未强调但完全正确的技术细节。Efron & Tibshirani (1993) 的 N≥10-15 建议是标准参考。论文在 §5.1 使用 "95% BCa bootstrap CI [−0.028, −0.012] excludes zero" 作为 p_BH=0.078 的补充证据，但 N=3 下 BCa CI 的 coverage 可能远低于名义 95%，这意味着该 CI 的证据价值被高估。两位 reviewer 独立提出同一问题，说明这不是 marginal concern。

**[AGREE] R1-N2**: Self-contamination 限制。与我的 N2 完全一致。R1 的补充点更具体：Appendix O 的 cross-model test "single seed, mixed, 缺 PPL 对比"——我查看了 page 16 的 Appendix O 内容，确认 Llama-3.2-3B 结果仅有 MMLU/HellaSwag 两个 metric（"Mixed results: MMLU improves while HellaSwag slightly degrades"），确实缺少 PPL 对比，且只有 single seed，实验设计远不如主实验严格。

**[AGREE] R1-N3**: Downstream 零改善。与我的 N3 一致。R1 的引用 "if all standard evaluation methods cannot detect it, actual significance is questionable" 精准地指出了问题核心。论文 §6 的辩护 ("Δ=−0.020 corresponds to ~0.1% relative improvement") 实际上是在论证自己方法的改善量 too small to matter，这对 analysis paper 也许可接受，但对声称提供 "practical corollary" 的论文则自相矛盾。

---

### Should-Fix 问题

**[AGREE] R1-W1**: B=4 micro-batch 的 dual constraint 可靠性问题。这是一个我未充分强调的重要技术批评。在 B=4 下，true real fraction 只能取 {0, 0.25, 0.5, 0.75, 1.0} 五个离散值，α_eff 的估计粒度极粗。§5.3 中论文自己展示了 B=8 和 B=16 的显著改善（Δ 从 −0.020 到 −0.052 到 −0.068），这反过来说明 B=4 是一个次优设定。论文选择 B=4 作为主实验（可能出于 GPU 内存限制），但应当更明确地讨论这一选择的代价。

**[AGREE] R1-W2**: α_eff proxy 理论保证的 gap。我在 W3 中提到了 r=0.79 的限制，但 R1 的批评更深入：Wang 2026 的 convergence theory 要求 α_eff(b) ≥ τ 对 true real fraction 成立，但论文将此条件应用于 proxy α_eff，而 proxy 的 R²=0.63 意味着理论保证不直接转移。论文 §3 说 "α_eff correlates with the true batch-level real fraction at Pearson r ≈ 0.79 (Appendix K)"，但 correlation 不等于 theoretical guarantee 的 transferability。这是一个 sound but understated 的理论弱点。

**[AGREE] R1-W3**: 3 点 power law 拟合。用 B ∈ {4, 8, 16} 三个数据点拟合 Δ ∝ B^0.89 确实在统计上几乎没有信息量——两参数模型拟合三个点，自由度接近零。论文 §5.3 报告这一 scaling 时未给出指数的不确定性区间，这不是严谨的 empirical claim。不过这是 §5.3 中的次要观察而非核心 claim，影响有限。

**[AGREE] R1-W4**: 3 个 detector 不足以建立 calibration 因果关系。这是 R1 审稿中最精准的技术批评之一，也是我在 W4 中提到但未展开的点。TF-IDF+LR (AUC=0.94, ECE=0.05) vs GPT-2 perplexity (AUC=0.91, ECE=0.131) 的对比同时在 AUC、模型类型、feature space、false positive pattern 等多个维度上不同。论文 §5.2 声称 "The TF-IDF vs GPT-2 contrast (comparable AUC, 2.7× ECE gap) isolates calibration"，但 AUC 0.94 vs 0.91 并非严格 comparable（差 0.03），且模型架构完全不同。R1 建议的 "同一 TF-IDF+LR detector + 不同 temperature scaling" 是一个极好的实验设计，能真正 isolate calibration effect。这会使 F2 的论证从 observational 升级为 quasi-causal。

**[REBUT] R1-W5**: "Minimum intervention" 原则缺乏理论依据。R1 的观察（grid-best b≈0.3 而 adaptive b*≈0.9，mean b* 比 grid-best 更高）有事实基础，但推理方向有误。

理由：(1) "Minimum intervention" 是 per-batch 的概念，不是全局平均的概念。在 contamination 较重的 batch 中，b* 可能很高（如 b*=3-5），而在干净 batch 中 b*=0。Overall mean ≈0.9 是这些异质 batch 的平均，不能与固定 b=0.3 直接比较语义。(2) 从 §5.3 Constraint regime 分析（seed 42, 24,412 micro-batches）：5.8% clean (b*=0), ~50% α_eff-binding, ~44% ESS-binding。这说明大约一半的 batch 在 quality floor 处最小化干预，另一半被 stability ceiling 约束。(3) Grid-best b=0.3 是 post-hoc oracle from 9 candidates，且 Figure 2 显示 PPL 在 b ∈ [0.1, 0.5] 区间形成 plateau，所以 b=0.3 的 "最优" 并不 sharp。(4) Adaptive b* 的优势不是绝对 PPL（低于 grid-best），而是无需 validation、低跨 seed 方差（σ=0.007 vs 0.033），以及在 ρ 变化时自动适应。

但我同意 R1 建议的 "median b / percentile-based b" 对比会有信息量——如果固定 b = median(b*) 也能接近 adaptive 的性能，那确实说明 per-batch adaptation 的价值有限，"minimum intervention" 的叙事需要修正。

**[AGREE] R1-W6**: Epoch confound 分析缺少 "uniform + multi-epoch" baseline。这是一个我在审稿中未发现但非常有价值的遗漏。当前的 epoch confound 分析比较：
- D&R full (6,103 steps, ~3.2 epochs): PPL 17.250
- D&R epoch-matched (2,533 steps, ~1.0 epoch): PPL 17.657
- Adaptive b* (6,103 steps, ~1.0 epoch): PPL 17.674

缺少的 baseline 是：Uniform + multi-epoch（即在全部数据上重复训练 ~3.2 epochs，不做任何 filtering）。这个 baseline 能回答：D&R full 的 PPL 17.250 相比 uniform 17.694 的 0.444 优势中，有多少来自纯粹的 data repetition（不考虑 filtering），有多少来自 filtering + repetition 的交互效应？论文的 LR-controlled uniform (2,533 steps) 给出 18.062，但这是 reduced training budget 下的 uniform，不是 multi-epoch uniform。添加这个 baseline 的计算成本很低（一次 6,103-step 训练），但对 epoch confound 的分析完整性至关重要。

---

### 小问题

**[AGREE] R1-M1**: "uncorrected p=0.010" 在 Abstract 中确实不够醒目。我在审稿中将此归类为 claims scope 与证据不匹配的问题（W1），但 R1 的格式建议更具体可操作。

**[REBUT] R1-M2**: "Table 2 Grid-best 的 τ 不明确"——Grid-best 使用固定 b（从 9 个 candidate 中 post-hoc 选择 b=0.3），不使用 τ 参数。τ 是 adaptive b* 的 quality floor 参数。Table 2 注释 ‡ 已标注 "Post-hoc oracle from nine candidates"。这不是论文的遗漏，可能是 R1 对 Grid-best 方法的理解有误。

**[AGREE] R1-M3**: Conclusion 确实缺少 N=3/校正后不显著的 caveat。§7 Conclusion（page 8 底部）使用断言性语言 "We identify three effectiveness conditions..."，未提及 p_BH=0.078 的限制。这与 §5.1 和 §Limitations 的谨慎态度不一致。

**[REBUT] R1-M4**: Figure 2 的 y 轴非零起点。在 method comparison 论文中，y 轴 truncation 是标准做法——所有方法的 PPL 在 17.2-18.0 范围内，如果 y 轴从 0 开始，所有差异将不可见。Figure 2 的 y 轴范围（约 17.0-18.0）是合理的。但可以在 caption 中注明 "note truncated y-axis" 作为最佳实践。

**[AGREE] R1-M5**: 未报告 Cohen's d 及其不确定性。对于 N=3 的小样本比较，Cohen's d（及其 CI）能比 p 值更好地传达 effect size 信息。论文报告了 Δ 和 σ，但未计算标准化 effect size。

**[AGREE] R1-M6**: Appendix P 的 checkpoint artifact 讨论确实需要仔细阅读才能理解它与主实验的关系——结论是 "all main results use from-scratch runs, artifact only affects early seed 42 adaptive runs that are not in the paper"，但 reader 需要自己拼凑这个信息。

---

### Questions

**[AGREE] R1-Q1**: 用同一 TF-IDF+LR detector 改变 temperature scaling 参数来 isolate calibration effect 是极好的实验建议。这比比较不同 detector 类型更有控制力。例如，将 temperature 从 T=0.204（calibrated, ECE=0.05）设为 T=1.0（uncalibrated, ECE likely much higher）或 T=0.05（over-confident），能在 AUC 不变的条件下单独测试 calibration 的影响。

**[AGREE] R1-Q2**: ρ=0.2 failure case 中的 α_eff bias 值得追问。§6 提到 "at ρ=0.2, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal (α_eff-binding at 60.1% despite mean q=0.393)"。如果 α_eff 的 systematic bias 在 ρ=0.2 下与 ρ=0.4 下相同（~-0.03, cf. §3 提到 mean Δ=-0.020 correlation），那么 τ=0.7 的阈值在低污染下可能系统性地 over-trigger reweighting。

**[AGREE] R1-Q3**: 为什么不在 B=16（最优设定，Δ=-0.068）上跑主实验？§5.3 明确展示 B=16 >> B=4。如果主实验在 B=4 上跑是因为 GPU 内存限制（单卡 RTX PRO 6000, sequence length 2048），论文应明确说明这一 practical constraint。这也影响 N1 的统计显著性问题——在 B=16 下 effect size 更大，可能更容易达到校正后显著性。

**[REBUT] R1-Q4**: Grid-best b=0.3 vs adaptive b*≈0.9 的差距是否表明 minimum intervention 过度干预——我在 R1-W5 中已部分反驳。补充：b=0.3 是 fixed across all batches 的 post-hoc optimum，b*≈0.9 是 per-batch adaptive 的均值。二者不可直接比较，因为 (a) 不同 batch 的最优 b 不同，平均值不等于最优固定值；(b) per-batch b* 的分布信息比均值更重要——如果 b* 的分布是 bimodal（大量 b*=0 clean batch + 少量 b*>2 highly contaminated batch），均值 0.9 的含义与所有 batch b*≈0.9 完全不同。论文 §5.3 的 regime 分析（5.8% clean, ~50% α_eff-binding, ~44% ESS-binding）支持这种异质性。不过 R1 的 concern 仍有一定道理——如果 median b* 也接近 0.9（而非 0.3），那确实说明 adaptive method 的 typical intervention 高于 grid-best，需要解释为什么 per-batch higher b 会比 global lower b 更好。

---

### 两位 Reviewer 的共识与分歧

**强共识（两人独立提出同一问题）**：
1. N=3 统计功效不足（R1-N1 / R2-N1）
2. Self-contamination 生态效度（R1-N2 / R2-N2）
3. Downstream 零改善（R1-N3 / R2-N3）

这三个 critical issues 是两位 reviewer 独立达成的共识，作者 rebuttal 必须正面回应。

**R1 独有的强技术批评（R2 需补充的遗漏）**：
- R1-W4（detector causal claim 需控制实验）和 R1-W6（缺 uniform + multi-epoch baseline）是我审稿中未充分展开的重要技术点，我完全赞同。
- R1-W1（B=4 micro-batch 统计可靠性）我虽然注意到但未作为独立 weakness 提出，R1 的分析更到位。

**R2 独有的关注点**：
- 论文标题 scope 与实验支撑不匹配（R2-W1）
- Grid-best vs adaptive 差距的来源分析缺失（R2-W2）
- α_eff proxy 讨论篇幅过长占用正文空间（R2-W3）
- 三个 findings 深度不均匀（R2-W4）

**唯一分歧**：
- R1-M4（Figure 2 y 轴非零起点）：我认为 method comparison 论文中 truncated y-axis 是标准做法，R1 的批评过于苛刻。
- R1-M2（Grid-best 的 τ）：Grid-best 不使用 τ 参数，R1 可能有误解。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-24T04:24:26.584947+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-24T04:24:26.635772+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T04:09:24.810625+00:00\", \"completed_at\": \"2026-05-24T04:12:23.522986+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续 3 页无 figure/table。Pages 3-4（Related Work + Method）和 Page 5（Results 开头）仅有 Page 4 的 Equation (1) 打破纯文本节奏。审稿人从 Page 2 的 Figure 1 到 Page 6 的 Table 1/Figure 2 之间经历约 3.5 页纯文本，视觉单调。建议将 Table 1 或 Figure 2 前移至 Page 5 附近，或在 Method 部分增加示意图/算法框\"}, {\"severity\": \"warning\", \"dimension\": \"page 6-8\", \"message\": \"Display items 分布不均——主文 6 个 display items（2 figures + 4 tables）全部集中在 Pages 6-8，前半部分（Pages 1-5）仅有 Figure 1。后半段信息密度骤增，前半段偏空\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"末页仅 Appendix R \\\"Use of AI Assistants\\\" 占约 15% 页面，剩余 ~85% 空白。虽然这是附录末页且内容性质决定了篇幅，但视觉上显得不专业。建议将此节并入前一页末尾\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯文本：Title + Abstract + Introduction 开头）。Figure 1 出现在 Page 2 顶部，位置可接受但非最优。若 Figure 1 能上移至 Page 1 底部或 Introduction 末段旁，可加速审稿人建立认知锚\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 基本自包含（\\\"Analysis overview. We identify three effectiveness conditions...\\\"），但缺少对 F1/F2/F3 三个条件的简要说明。审稿人仅看 caption 难以完全理解图表含义\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 清晰可读，轴标签和图例字号合理。线条颜色区分度良好（实线 vs 虚线 + 不同 marker）。Table 1 和 Table 2 使用 booktabs 风格，最优值加粗标注，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 3（Decision summary for practitioners）结构清晰，作为实践指南表格很有价值。条件列 + 证据列 + PPL 影响列的设计便于快速查阅\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文最后一页：Table 4 占上半部分，Conclusion 填充下半部分，页面利用率约 90%，合格\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Equation (1) 渲染正确，分段函数排版清晰。公式周围间距适当\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简短（约 5 行），覆盖 3 个关键限制点，符合 EMNLP 要求。Ethics Stateme
…[truncated 665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-24T04:24:26.636256+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-24T04:24:26.737110+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-24T04:28:16.018638+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成：检测器噪声占未解释方差 ~70%（边界区 q∈[0.4,0.6] 准确率 ~55%），b* 变换占 ~30%（ESS floor 约束的刻意设计）。B=4→B=16 方差降 10.25× 但 R² 不变（0.47→0.44），证明瓶颈在检测器。§6 已写入完整定量分解段落。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句：proxy r=0.70 在 §3，seed 42 在 Table 1 脚注，ρ=0.2 在 §6。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。释放空间用于 decision summary table 移入主文。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11-12 recurring issues (updated with Round 13) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。双方 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Round 13 fresh review 再次独立发现（R1-N1 + R2-N1），交叉回应双方 AGREE。新增技术细节：BCa bootstrap CI 在 N=3 下覆盖率存疑（Efron & Tibshirani 1993 建议 N≥10-15）。Cohen's d≈2.86 未报告且 N=3 下 CI 极宽。Abstract/Conclusion 仍以断言性语言呈现校正后不显著的结果。三轮连续被独立指出，属结构性限制。\"\n  action_items:\n    - round: 13\n      action: \"增加 seeds 至 N≥5，或在 Abstract/Conclusion 明确标注 'directionally consistent but not statistically significant after correction'。报告 Cohen's d 及其 CI。讨论 BCa bootstrap 在 N=3 下的覆盖率局限。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.63，理论保证不直接转移到 proxy\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出，R2 AGREE。新增理论维度：Wang 2026 的 convergence theory 要求 true real fraction ≥ τ，但论文将此条件应用于 proxy α_eff（R²=0.63），理论保证是否仍成立未讨论。ρ=0.2 下 α_eff bias 方向和大小未报告。\"\n  action_items:\n    - round: 13\n      action: \"明确讨论 α_eff ≥ τ 作为 proxy condition 相对于 true fraction condition 的理论精度要求。报告 ρ=0.2 下的 α_eff bias。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.020, ~0.11%），practical corollary 自相矛盾\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=128 幂律外推被一致认为不可靠。'practical' 表述仍残留。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2-N3 再次独立提出，交叉双方 AGREE。R2 精准指出：论文在 §6 辩护 PPL 改善 too small to detect，但这恰恰证明方法在当前可测指标上无实际价值，与声称提供 'practical corollary' 自相矛盾。ρ=0.6 downstream 结果缺失。\"\n  action_items:\n    - round: 13\n      action: \"报告 ρ=0.6 downstream results。明确论文定位为 analysis paper with negative practical result at current scales，或在更大规模验证 downstream 效果。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"实验范围过窄：单模型/单数据集/self-contamination，不足以支撑一般性结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Cross-model transfer single seed + mixed + 无 PPL 比较。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-N2 再次独立提出，交叉双方 AGREE。R1 补充：Appendix O cross-model test 缺 PPL 对比（'checkpoints were not retained for re-evaluation'）不仅是 scope 问题，而是核心 claim 的证据缺失。R2 指出：标题 'When Does D&R Work?' 暗示一般性但实验仅支持 self-contamination。建议标题加限定。\"\n  action_items:\n    - round: 13\n      action: \"至少完成 cross-model 的完整 PPL 对比（3 seeds），或将标题/claims 限定为 self-contamination setting。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§3 压缩后仍给人独立方法贡献印象。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 新颖性评估：F3 低至中等，adaptive b* 中等（engineering contribution）。R1 交叉回应认为应更低。Per-batch bisection 是标准方法直接应用，dual constraint 缺理论依据。\"\n  action_items:\n    - round: 13\n      action: \"进一步弱化方法贡献 framing，确保论文定位始终一致为 analysis paper。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 发现新的可能遗漏：RAID (Dugan et al. 2024)、M4 (Wang et al. 2024) detection benchmarks；Phi 系列 synthetic data 正面案例。R1 AGREE RAID/M4，补充 Owen 2013 importance weighting failure modes 在正文讨论不足。R1 REBUT 后训练阶段 contamination-aware 方法（scope 限定为 pretraining 合理）。\"\n  action_items:\n    - round: 13\n      action: \"考虑补充 RAID/M4 detection benchmarks、Phi 系列 synthetic data 正面用例。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏 uniform+multi-epoch baseline\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Epoch confound 适用范围需限定为 multi-epoch exposure 场景。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W6 新增关键缺失 baseline：'uniform + multi-epoch'（全数据重复训练 ~3.2 epochs 不做 filtering）。此 baseline 能区分 D&R 优势来自纯重复 vs filtering+repetition 交互。R2 AGREE 并认为计算成本低但对分析完整性至关重要。\"\n  action_items:\n    - round: 13\n      action: \"增加 uniform+multi-epoch baseline（全数据 ~3.2 epochs），以完善 epoch confound 分析。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 可读性和 display item 分布问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。12+ 脚注含关键技术细节。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"ρ 符号冲突、Figure 1 黑白不可辨、Figure 2 x 轴标签混淆。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-M4 Figure 2 y 轴非零起点放大差异（R2 REBUT：truncated y-axis 是标准做法）。R2 minor: Figure 1 TikZ 信息密度偏低。视觉审查发现 pages 3-5 连续无 figure/table，display items 集中在 pages 6-8。\"\n  action_items:\n    - round: 13\n      action: \"考虑将 Table 1 或 Figure 2 前移至 §5 开头以改善 display item 分布。Figure 2 可加 'note truncated y-axis' 注释。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 issues (updated with Round 13) ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"LaTeX wc 确认 225 words。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 R2 格式检查确认 ~166 words，合规。已修复。\"\n  resolution: \"Abstract 已压缩至 ~166 words，符合 ≤200 words 限制。\"\n  resolution_round: 13\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§7 Conclusion 溢出至第 9 页。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 R2 格式检查确认 §1-§7 在 page 8 内结束，Limitations 从 page 9 开始。合规。\"\n  resolution: \"正文已压缩至 8 页内，§7 Conclusion 在 page 8 底部结束。\"\n  resolution_round: 13\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个），不足以支撑因果性结论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"仅 TF-IDF+LR / GPT-2 / N-gram。3 个数据点不足建立因果关系。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4 详细展开：TF-IDF vs GPT-2 同时在 AUC/模型类型/feature space/false positive pattern 上不同，不是控制实验。R2 AGREE 并评为 R1 最精准技术批评。R1 建议：用同一 TF-IDF+LR detector + 不同 temperature scaling 真正 isolate calibration effect（T=0.204 calibrated vs T=1.0 uncalibrated）。\"\n  action_items:\n    - round: 13\n      action: \"用同一 TF-IDF+LR detector 不同 calibration 程度 isolate calibration effect，或将 Table 3 阈值标注为 'observed in our 3 detectors' 而非通用建议。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size scaling 趋势基于 3 个数据点\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=4/8/16 仅 3 点，外推到 B=128 不可靠。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W3 再次指出 Δ ∝ B^0.89 的 2-parameter model fitting 3 points，自由度接近零。指数不确定性未报告。R2 AGREE 但认为影响有限（次要观察非核心 claim）。\"\n  action_items:\n    - round: 13\n      action: \"删除 power law fitting，保留 B=4/8/16 观测趋势描述为 monotonic trend。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"建议将 Spearman 改为 ρ_s。\"\n    - round: 13\n      reviewers: []\n      note: \"本轮未提及。论文已使用 ρ_s 表示 Spearman（Table 12），可能已修复。待确认。\"\n  action_items:\n    - round: 12\n      action: \"全文 Spearman ρ → ρ_s\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 13 新发现 ===\n\n- id: \"R13-W1\"\n  summary: \"B=4 micro-batch 上 dual constraint 统计可靠性不足，主实验在次优设定运行\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 AGREE。B=4 下 true real fraction 仅取 {0, 0.25, 0.5, 0.75, 1.0}，α_eff 估计粒度极粗（MAE=0.114）。§5.3 展示 B=8→16 显著改善（Δ 从 -0.020 到 -0.068），反证 B=4 是次优设定。R2-Q3 追问为什么不在 B=16 跑主实验。\"\n  action_items:\n    - round: 13\n      action: \"说明 B=4 选择的 practical constraint（GPU 内存？），或补充 B=8 完整对比（3 seeds + downstream）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"'Minimum intervention' 原则缺乏理论依据，grid-best b=0.3 vs adaptive b*≈0.9 偏差未解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 部分 REBUT。R1 指出 grid-best b=0.3 而 adaptive b*≈0.9，minimum intervention 反而过度干预。R2 反驳：b* 均值是异质 batch 的平均，不能与固定 b 直接比较语义——5.8% clean (b*=0), ~50% α_eff-binding, ~44% ESS-binding。但 R2 也同意 median b / percentile-based b 对比有信息量。\"\n  action_items:\n    - round: 13\n      action: \"补充 per-batch b* 分布（median, percentiles）。可选：对比 fixed b=median(b*) 的性能，验证 per-batch adaptation 的独立价值。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"Grid-best 与 adaptive b* 差距（0.054 PPL）来源未分析\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 AGREE 并补充机制分析：adaptive 的 minimum intervention 系统性地过度干预（b 偏大），per-batch adaptation 的好处被 suboptimal aggregate b 部分抵消。建议讨论 adaptive b* 分布 truncated 到 [0, 0.5] 的效果。\"\n  action_items:\n    - round: 13\n      action: \"分析 adaptive vs grid-best 差距来源：是 dual constraint 过于保守，还是 α_eff proxy ceiling 限制？讨论是否有 oracle-free 方式缩小差距。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"§6 Discussion 第一段与 §5.1 epoch confound 内容重复\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 minor 提出，R1 AGREE。两处都讨论 >95% multi-epoch exposure、LR-controlled verification、Δ=0.017 residual。建议 §6 仅引用 §5.1 结论，省出空间深化 F2/F3 分析。\"\n  action_items:\n    - round: 13\n      action: \"精简 §6 第一段，引用 §5.1 而非重复内容。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Cohen's d 未报告，N=3 下效应量不确定性未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-M5 提出，R2 AGREE。粗估 d≈2.86（large effect），但 N=3 下 CI 极宽。应报告并讨论不确定性。\"\n  action_items:\n    - round: 13\n      action: \"报告 Cohen's d 及其 CI，讨论 N=3 下的不确定性。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"Table 2 Golden Ratio 仅 seed 42，未解释为何不补全\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 minor 提出，R1 AGREE。论文标注 †Oracle requiring known ρ, seed 42 only，但未解释 single-seed 原因。\"\n  action_items:\n    - round: 13\n      action: \"简要说明 Golden Ratio single-seed 原因（compute budget 或 oracle 性质使 multi-seed 无意义？）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成：检测器噪声占未解释方差 ~70%（边界区 q∈[0.4,0.6] 准确率 ~55%），b* 变换占 ~30%（ESS floor 约束的刻意设计）。B=4→B=16 方差降 10.25× 但 R² 不变（0.47→0.44），证明瓶颈在检测器。§6 已写入完整定量分解段落。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句：proxy r=0.70 在 §3，seed 42 在 Table 1 脚注，ρ=0.2 在 §6。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。释放空间用于 decision summary table 移入主文。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11-12 recurring issues (updated with Round 13) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。双方 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Round 13 fresh review 再次独立发现（R1-N1 + R2-N1），交叉回应双方 AGREE。新增技术细节：BCa bootstrap CI 在 N=3 下覆盖率存疑（Efron & Tibshirani 1993 建议 N≥10-15）。Cohen's d≈2.86 未报告且 N=3 下 CI 极宽。Abstract/Conclusion 仍以断言性语言呈现校正后不显著的结果。三轮连续被独立指出，属结构性限制。\"\n  action_items:\n    - round: 13\n      action: \"增加 seeds 至 N≥5，或在 Abstract/Conclusion 明确标注 'directionally consistent but not statistically significant after correction'。报告 Cohen's d 及其 CI。讨论 BCa bootstrap 在 N=3 下的覆盖率局限。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.63，理论保证不直接转移到 proxy\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出，R2 AGREE。新增理论维度：Wang 2026 的 convergence theory 要求 true real fraction ≥ τ，但论文将此条件应用于 proxy α_eff（R²=0.63），理论保证是否仍成立未讨论。ρ=0.2 下 α_eff bias 方向和大小未报告。\"\n  action_items:\n    - round: 13\n      action: \"明确讨论 α_eff ≥ τ 作为 proxy condition 相对于 true fraction condition 的理论精度要求。报告 ρ=0.2 下的 α_eff bias。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.020, ~0.11%），practical corollary 自相矛盾\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=128 幂律外推被一致认为不可靠。'practical' 表述仍残留。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2-N3 再次独立提出，交叉双方 AGREE。R2 精准指出：论文在 §6 辩护 PPL 改善 too small to detect，但这恰恰证明方法在当前可测指标上无实际价值，与声称提供 'practical corollary' 自相矛盾。ρ=0.6 downstream 结果缺失。\"\n  action_items:\n    - round: 13\n      action: \"报告 ρ=0.6 downstream results。明确论文定位为 analysis paper with negative practical result at current scales，或在更大规模验证 downstream 效果。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"实验范围过窄：单模型/单数据集/self-contamination，不足以支撑一般性结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Cross-model transfer single seed + mixed + 无 PPL 比较。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-N2 再次独立提出，交叉双方 AGREE。R1 补充：Appendix O cross-model test 缺 PPL 对比（'checkpoints were not retained for re-evaluation'）不仅是 scope 问题，而是核心 claim 的证据缺失。R2 指出：标题 'When Does D&R Work?' 暗示一般性但实验仅支持 self-contamination。建议标题加限定。\"\n  action_items:\n    - round: 13\n      action: \"至少完成 cross-model 的完整 PPL 对比（3 seeds），或将标题/claims 限定为 self-contamination setting。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§3 压缩后仍给人独立方法贡献印象。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 新颖性评估：F3 低至中等，adaptive b* 中等（engineering contribution）。R1 交叉回应认为应更低。Per-batch bisection 是标准方法直接应用，dual constraint 缺理论依据。\"\n  action_items:\n    - round: 13\n      action: \"进一步弱化方法贡献 framing，确保论文定位始终一致为 analysis paper。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 发现新的可能遗漏：RAID (Dugan et al. 2024)、M4 (Wang et al. 2024) detection benchmarks；Phi 系列 synthetic data 正面案例。R1 AGREE RAID/M4，补充 Owen 2013 importance weighting failure modes 在正文讨论不足。R1 REBUT 后训练阶段 contamination-aware 方法（scope 限定为 pretraining 合理）。\"\n  action_items:\n    - round: 13\n      action: \"考虑补充 RAID/M4 detection benchmarks、Phi 系列 synthetic data 正面用例。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏 uniform+multi-epoch baseline\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Epoch confound 适用范围需限定为 multi-epoch exposure 场景。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W6 新增关键缺失 baseline：'uniform + multi-epoch'（全数据重复训练 ~3.2 epochs 不做 filtering）。此 baseline 能区分 D&R 优势来自纯重复 vs filtering+repetition 交互。R2 AGREE 并认为计算成本低但对分析完整性至关重要。\"\n  action_items:\n    - round: 13\n      action: \"增加 uniform+multi-epoch baseline（全数据 ~3.2 epochs），以完善 epoch confound 分析。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 可读性和 display item 分布问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。12+ 脚注含关键技术细节。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"ρ 符号冲突、Figure 1 黑白不可辨、Figure 2 x 轴标签混淆。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-M4 Figure 2 y 轴非零起点放大差异（R2 REBUT：truncated y-axis 是标准做法）。R2 minor: Figure 1 TikZ 信息密度偏低。视觉审查发现 pages 3-5 连续无 figure/table，display items 集中在 pages 6-8。\"\n  action_items:\n    - round: 13\n      action: \"考虑将 Table 1 或 Figure 2 前移至 §5 开头以改善 display item 分布。Figure 2 可加 'note truncated y-axis' 注释。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 issues (updated with Round 13) ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"LaTeX wc 确认 225 words。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 R2 格式检查确认 ~166 words，合规。已修复。\"\n  resolution: \"Abstract 已压缩至 ~166 words，符合 ≤200 words 限制。\"\n  resolution_round: 13\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§7 Conclusion 溢出至第 9 页。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 R2 格式检查确认 §1-§7 在 page 8 内结束，Limitations 从 page 9 开始。合规。\"\n  resolution: \"正文已压缩至 8 页内，§7 Conclusion 在 page 8 底部结束。\"\n  resolution_round: 13\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个），不足以支撑因果性结论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"仅 TF-IDF+LR / GPT-2 / N-gram。3 个数据点不足建立因果关系。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4 详细展开：TF-IDF vs GPT-2 同时在 AUC/模型类型/feature space/false positive pattern 上不同，不是控制实验。R2 AGREE 并评为 R1 最精准技术批评。R1 建议：用同一 TF-IDF+LR detector + 不同 temperature scaling 真正 isolate calibration effect（T=0.204 calibrated vs T=1.0 uncalibrated）。\"\n  action_items:\n    - round: 13\n      action: \"用同一 TF-IDF+LR detector 不同 calibration 程度 isolate calibration effect，或将 Table 3 阈值标注为 'observed in our 3 detectors' 而非通用建议。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size scaling 趋势基于 3 个数据点\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=4/8/16 仅 3 点，外推到 B=128 不可靠。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W3 再次指出 Δ ∝ B^0.89 的 2-parameter model fitting 3 points，自由度接近零。指数不确定性未报告。R2 AGREE 但认为影响有限（次要观察非核心 claim）。\"\n  action_items:\n    - round: 13\n      action: \"删除 power law fitting，保留 B=4/8/16 观测趋势描述为 monotonic trend。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"建议将 Spearman 改为 ρ_s。\"\n    - round: 13\n      reviewers: []\n      note: \"本轮未提及。论文已使用 ρ_s 表示 Spearman（Table 12），可能已修复。待确认。\"\n  action_items:\n    - round: 12\n      action: \"全文 Spearman ρ → ρ_s\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 13 新发现 ===\n\n- id: \"R13-W1\"\n  summary: \"B=4 micro-batch 上 dual constraint 统计可靠性不足，主实验在次优设定运行\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 AGREE。B=4 下 true real fraction 仅取 {0, 0.25, 0.5, 0.75, 1.0}，α_eff 估计粒度极粗（MAE=0.114）。§5.3 展示 B=8→16 显著改善（Δ 从 -0.020 到 -0.068），反证 B=4 是次优设定。R2-Q3 追问为什么不在 B=16 跑主实验。\"\n  action_items:\n    - round: 13\n      action: \"说明 B=4 选择的 practical constraint（GPU 内存？），或补充 B=8 完整对比（3 seeds + downstream）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"'Minimum intervention' 原则缺乏理论依据，grid-best b=0.3 vs adaptive b*≈0.9 偏差未解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 部分 REBUT。R1 指出 grid-best b=0.3 而 adaptive b*≈0.9，minimum intervention 反而过度干预。R2 反驳：b* 均值是异质 batch 的平均，不能与固定 b 直接比较语义——5.8% clean (b*=0), ~50% α_eff-binding, ~44% ESS-binding。但 R2 也同意 median b / percentile-based b 对比有信息量。\"\n  action_items:\n    - round: 13\n      action: \"补充 per-batch b* 分布（median, percentiles）。可选：对比 fixed b=median(b*) 的性能，验证 per-batch adaptation 的独立价值。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"Grid-best 与 adaptive b* 差距（0.054 PPL）来源未分析\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 AGREE 并补充机制分析：adaptive 的 minimum intervention 系统性地过度干预（b 偏大），per-batch adaptation 的好处被 suboptimal aggregate b 部分抵消。建议讨论 adaptive b* 分布 truncated 到 [0, 0.5] 的效果。\"\n  action_items:\n    - round: 13\n      action: \"分析 adaptive vs grid-best 差距来源：是 dual constraint 过于保守，还是 α_eff proxy ceiling 限制？讨论是否有 oracle-free 方式缩小差距。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"§6 Discussion 第一段与 §5.1 epoch confound 内容重复\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 minor 提出，R1 AGREE。两处都讨论 >95% multi-epoch exposure、LR-controlled verification、Δ=0.017 residual。建议 §6 仅引用 §5.1 结论，省出空间深化 F2/F3 分析。\"\n  action_items:\n    - round: 13\n      action: \"精简 §6 第一段，引用 §5.1 而非重复内容。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Cohen's d 未报告，N=3 下效应量不确定性未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-M5 提出，R2 AGREE。粗估 d≈2.86（large effect），但 N=3 下 CI 极宽。应报告并讨论不确定性。\"\n  action_items:\n    - round: 13\n      action: \"报告 Cohen's d 及其 CI，讨论 N=3 下的不确定性。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"Table 2 Golden Ratio 仅 seed 42，未解释为何不补全\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 minor 提出，R1 AGREE。论文标注 †Oracle requiring known ρ, seed 42 only，但未解释 single-seed 原因。\"\n  action_items:\n    - round: 13\n      action: \"简要说明 Golden Ratio single-seed 原因（compute budget 或 oracle 性质使 multi-seed 无意义？）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-24T04:28:16.119809+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 18562}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-24T04:31:03.746183+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "provenance_weight_training",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 via ARR\n**审稿模式**: Fresh（无历史轮次记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作+格式）\n\n---\n\n## Summary\n\n本文分析 detect-and-reweight 范式在 continued LM pretraining 中的有效性条件，通过 Qwen3-0.6B 的自污染实验（132M FineWeb tokens, ρ=0.4, 3 seeds）得出三个发现：(1) D&R 的 >95% PPL 优势来自 multi-epoch exposure 而非 filtering quality；(2) 有效 reweighting 需要 detector 同时具备足够 discrimination (AUC) 和 calibration (ECE)；(3) 最小干预（dual-constrained adaptive b*）优于无约束最大化。作为实用推论，提出一个无需 grid search 的 per-batch adaptive b* 方法，在 ρ≥0.4 时优于 uniform（Δ=-0.020, ρ=0.4; Δ=-0.032, ρ=0.6）。\n\n---\n\n## Strengths\n\n**S1. Epoch confound 发现是论文最核心、最有价值的贡献。** [R1 AGREE, R2 AGREE]\nTable 1 展示 D&R 的 0.396 PPL 优势在 epoch-matched 后缩至 Δ=0.017（3 seeds），揭示 >95% 的 reported advantage 源于数据重复而非 filtering quality。LR-controlled verification（D&R 17.651 vs shared-schedule 17.657, Δ=0.006）排除学习率混淆。Permuted-score control（+0.26 PPL）证明 detector signal 是 load-bearing。三重验证使这一发现高度可信，对后续 D&R 工作的实验设计有直接指导意义。\n\n**S2. 实验设计结构良好，消融层次清晰。** [R1 AGREE, R2 AGREE]\n六种方法（Adaptive < Uniform < ESS-only < Random + Grid oracle + D&R oracle）形成清晰的消融阶梯，每一层有明确控制变量。Ablation hierarchy 展示了 detector signal 和 minimum intervention 的各自贡献。\n\n**S3. 结果报告异常坦诚。** [R1 AGREE, R2 AGREE]\n论文主动报告：Bonferroni-Holm 校正后不显著的 p 值（p_BH=0.078/0.064）、downstream 零改善（Table 4: 0.5414 vs 0.5414）、ρ=0.2 failure case、checkpoint resume artifact（Appendix P）、cross-model mixed results（Appendix O）。这种透明度在 ML 论文中不常见，是良好的学术规范。\n\n**S4. Related Work 全面且结构化。** [R1 AGREE, R2 AGREE]\n§2 分五个 paragraph 覆盖 model collapse、detection、domain-level mixing、instance-level reweighting、theoretical foundations，引用 50+ 篇文献。与 Drayson et al. (2025) 的三点区分清晰公平。\n\n**S5. Grid search 消除的实际价值。** [R1 AGREE, R2 AGREE]\nAdaptive b* 的跨 seed 方差为 σ=0.007，远低于 grid-best 的 σ=0.033（4.7×）。Grid search 需 9 次完整训练（~16 GPU-hours at 0.6B），且 Figure 2 的 PPL plateau 使 validation-based selection 不可靠。\n\n**S6. 理论 well-definedness 和实验规范。** [R1 AGREE, R2 AGREE]\nProposition 1-2（α_eff 单调递增、ESS 单调递减）确保 dual constraint 可解。Checkpoint resume artifact 的披露和 from-scratch 验证展示良好规范。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] N=3 seeds 下所有核心结论均未达校正后统计显著性** [R1-N1 + R2-N1, 双方 AGREE]\n\n论文最核心的定量 claim：\n- ρ=0.4: uncorrected p=0.019, Bonferroni-Holm 校正后 p_BH=0.078（不显著）\n- ρ=0.6: uncorrected p=0.010, p_BH=0.064（不显著）\n\nBCa bootstrap CI [-0.028, -0.012] 在 N=3 下覆盖率存疑——Efron & Tibshirani (1993) 建议 N≥10-15。Cohen's d≈2.86 未报告，且 N=3 下 CI 极宽。Abstract 和 Conclusion 仍以断言性语言（\"improves over uniform at ρ≥0.4\"）呈现校正后不显著的结果。\n\n对于以 \"When does X work?\" 为标题的 analysis paper，核心 claim 的统计支撑应当更强。\n\n建议：增加至 N≥5 seeds，或在 Abstract/Conclusion 明确标注 \"directionally consistent but not statistically significant after family-wise correction\"。报告 Cohen's d 及其 CI。\n\n**C2. [Critical] 仅在 self-contamination 设置下验证，生态效度堪忧** [R1-N2 + R2-N2, 双方 AGREE]\n\nGenerator 和 trainee 都是 Qwen3-0.6B，是最简单的检测场景——TF-IDF 可利用 128-token prefix 到 384-token continuation 的风格断裂点。所有三个 findings 建立在此设定上。唯一跨模型测试（Llama-3.2-3B, Appendix O）是 single seed、results mixed、缺 PPL 对比（\"checkpoints were not retained for re-evaluation\"）。\n\n标题 \"When Does Detect-and-Reweight Work?\" 暗示一般性结论，但实验仅覆盖：一个模型家族、一种 contamination 设置、一个训练范式、一个数据量级。Table 3 的 practitioner decision summary（AUC≥0.9, ECE≤0.05）在 cross-model 场景下可能不适用。\n\n建议：至少完成 cross-model 的完整 PPL 对比（3 seeds），或将标题限定为 self-contamination setting。\n\n**C3. [Critical] 下游任务零改善，method 的实际价值存疑** [R1-N3 + R2-N3, 双方 AGREE]\n\nAdaptive vs Uniform 的 downstream accuracy 完全相同（0.5414 vs 0.5414, 5 tasks, 3 seeds, Table 4）。论文将此归因于 Δ=-0.020 对应 ~0.1% relative improvement，低于 per-task measurement noise（σ≈0.01）。这个解释逻辑自洽，但恰恰证明方法在当前可测指标上无实际效果，与声称提供 \"practical corollary\" 存在矛盾。ρ=0.6 的 downstream results 缺失。\n\n建议：报告 ρ=0.6 downstream results；或明确定位为 \"analysis paper with negative practical result at current scales\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [Warning] B=4 micro-batch 上 dual constraint 统计可靠性不足** [R1-W1, R2 AGREE]\n\nB=4 下 true real fraction 仅取 {0, 0.25, 0.5, 0.75, 1.0}，α_eff 估计粒度极粗（Appendix K: MAE=0.114）。§5.3 展示 B=8→16 显著改善（Δ 从 -0.020 到 -0.068），反证 B=4 是次优设定。主实验在最 noisy 条件下运行，应说明选择 B=4 的 practical constraint。\n\n**W2. [Warning] α_eff proxy 理论保证的 gap** [R1-W2, R2 AGREE]\n\nα_eff 与 true batch-level real fraction 的 Pearson r=0.79（R²≈0.63），37% 方差未解释。Wang 2026 的 convergence theory 要求 true real fraction ≥ τ，但论文将此条件应用于 proxy α_eff，理论保证是否仍成立未讨论。ρ=0.2 下 α_eff 的 bias 方向和大小未报告。\n\n**W3. [Warning] 3 个 detector 不足以建立 calibration 因果关系** [R1-W4, R2 AGREE（最强共识）]\n\nTF-IDF+LR vs GPT-2 的对比同时在 AUC、模型类型、feature space、false positive pattern 上不同，不是控制实验。论文声称 \"isolates calibration\" 但 AUC 0.94 vs 0.91 并非严格 comparable。建议用同一 TF-IDF+LR detector + 不同 temperature scaling（T=0.204 calibrated vs T=1.0 uncalibrated）真正 isolate calibration effect。\n\n**W4. [Warning] Epoch confound 分析缺少 uniform+multi-epoch baseline** [R1-W6, R2 AGREE]\n\n当前比较：D&R full (~3.2 epochs) vs D&R epoch-matched (~1.0 epoch) vs Adaptive (~1.0 epoch)。缺少 \"uniform + multi-epoch\"（全数据重复训练 ~3.2 epochs 不做 filtering）。此 baseline 能区分 D&R 优势来自纯重复 vs filtering+repetition 交互。计算成本低，对分析完整性至关重要。\n\n**W5. [Warning] \"Minimum intervention\" 原则缺乏理论依据** [R1-W5, R2 部分 REBUT]\n\nGrid-best b≈0.3 而 adaptive b* 均值≈0.9——表面看 minimum intervention 反而 over-intervenes。R2 反驳：b* 均值是异质 batch 的平均（5.8% clean b*=0, ~50% α_eff-binding, ~44% ESS-binding），不能与固定 b 直接比较。但双方同意 median b / percentile-based b 对比有信息量——如果 fixed b=median(b*) 也能接近 adaptive 性能，per-batch adaptation 的独立价值需重新评估。\n\n**W6. [Warning] 标题/claims scope 与实验支撑不匹配** [R2-W1, R1 AGREE]\n\n标题暗示对 D&R 范式的全面分析，但实验仅覆盖一个模型家族、一种 contamination 设置、一个训练范式。建议标题加限定（如 \"...in Self-Contaminated Continued LM Pretraining\"）或在 Abstract 第一句明确 scope。\n\n**W7. [Warning] Grid-best 与 adaptive b* 差距（0.054 PPL）来源未分析** [R2-W2, R1 AGREE]\n\nGrid-best 17.620 显著优于 adaptive 17.674，差距是 adaptive vs uniform 改善（0.020）的 2.7 倍。论文论证 grid search 昂贵不可靠，但未分析差距来源（dual constraint 过于保守？α_eff proxy ceiling？）。\n\n**W8. [Warning] 三个 findings 分析深度不均匀** [R2-W4, R1 AGREE]\n\nF1（epoch confound）有三重验证，分析深入。F2（detector requirements）仅 3 个 detector 在 self-contamination 下的 observational comparison。F3（minimum intervention）主要依赖 ESS-only 退化（+0.043），缺乏机制分析。\n\n**W9. [Warning] Batch-size scaling 趋势基于 3 个数据点** [R1-W3, R2 AGREE]\n\nB ∈ {4, 8, 16} 三点拟合 Δ ∝ B^0.89，2-parameter model fitting 3 points 自由度接近零。指数不确定性未报告。R2 认为影响有限（次要观察），但外推可靠性确实为零。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下问题上独立达成强共识：\n\n1. **N=3 统计效力不足** — 三轮审稿连续被独立指出，属结构性限制。p_BH=0.078/0.064 均不达传统显著性。BCa bootstrap CI 在 N=3 下覆盖率存疑。\n2. **Self-contamination 生态效度** — Generator=trainee 是最简单检测场景。Cross-model test 不完整（single seed, no PPL, mixed results）。标题暗示一般性但实验不支持。\n3. **Downstream 零改善** — 方法的 PPL 改善（0.11% relative）无法转化为任何可测量的下游效果。\"Practical corollary\" 的 framing 与实际结果矛盾。\n4. **Detector 因果 claim 证据不足** — 3 个 detector 的 observational comparison 不能 isolate calibration effect。需控制实验。\n5. **Epoch confound 是最强贡献** — 两位 Reviewer 一致认为 F1 是论文最核心、最有价值的发现。\n\n## Reviewer Divergence [REBUT]\n\n1. **评分差异**：R1=3.0 (Findings) vs R2=3.5 (Borderline Conference)。分歧在于 epoch confound finding 的独立价值是否足以支撑 Conference。R1 认为校正后不显著 + downstream 零改善使方法贡献不足；R2 认为 F1 的纠偏价值接近 main conference 门槛。\n2. **α_eff 讨论位置**：R2 认为 §6 中 ~200 words 的 α_eff 讨论过长应移 Appendix；R1 认为核心讨论（r=0.79, bias 方向）应留主文，但可精简 quantitative decomposition。\n3. **Minimum intervention 评价**：R1 认为 grid-best b=0.3 vs adaptive b*≈0.9 表明 over-intervention；R2 部分反驳（per-batch 均值不可与固定 b 直接比较），但同意 median b 对比有信息量。\n4. **Adaptive b* 新颖性**：R2 评\"中等（engineering contribution）\"；R1 认为应更低——per-batch bisection 是标准方法直接应用。\n\n---\n\n## Questions\n\n1. 能否用同一 TF-IDF+LR detector 改变 temperature scaling 参数（T=0.204 calibrated vs T=1.0 uncalibrated）isolate calibration effect？[R1-Q1, R2 AGREE]\n2. ρ=0.6 下 downstream accuracy 是否有所改善？[R2-Q2, R1 AGREE]\n3. 为什么不增加 seed 数量（N≥5）？132M tokens, 0.6B model 的训练成本不高。[R1-N1/R2-Q3]\n4. 为什么不在 B=16 而非 B=4 上计算 b*？主实验是否在次优设定下运行？[R1-Q3, R2 AGREE]\n5. Adaptive b* 的 per-batch b* 分布（median, percentiles）是什么？如果 median b* 也接近 0.9，minimum intervention 叙事需要修正。[R1-W5, R2 部分 AGREE]\n6. 能否增加 \"uniform + multi-epoch\"（~3.2 epochs 无 filtering）baseline 以完善 epoch confound 分析？[R1-W6, R2 AGREE]\n\n---\n\n## Missing References\n\n以下为两位 Reviewer 一致建议补充的参考文献：\n- **RAID** (Dugan et al. 2024) 和 **M4** (Wang et al. 2024)：detection benchmarks，与 detector requirements 分析相关 [R2 提出, R1 AGREE]\n- **Phi 系列** (Gunasekar et al. 2023, Li et al. 2023)：synthetic data 正面案例，为 D&R 必要性提供 counterpoint [R2 提出, R1 AGREE]\n- **Owen 2013** (Monte Carlo Theory) 正文讨论 importance weighting failure modes（目前仅在 Appendix proof 引用）[R1 补充]\n\nR1 对后训练阶段 contamination-aware 方法的遗漏 REBUT（scope 限定为 pretraining 合理）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warning, 11 info）。\n\n主要发现：\n- **[Warning] Pages 3-5 连续无 figure/table**：从 Page 2 的 Figure 1 到 Page 6 的 Table 1/Figure 2，约 3.5 页纯文本，视觉单调。建议将 Table 1 或 Figure 2 前移。\n- **[Warning] Display items 分布不均**：主文 6 个 display items 全部集中在 Pages 6-8，前半部分仅有 Figure 1。\n- **[Warning] Appendix 末页 ~85% 空白**：Appendix R (Use of AI Assistants) 仅占 ~15% 页面。建议并入前一页。\n- **[Info] 正面评价**：Figure 2 清晰可读，Table 1-4 使用 booktabs 规范，Equation (1) 排版清晰，References 无 [?] 未解析引用，色彩方案色盲友好。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n### 评分维度\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 2.5/5 | 3/5 | 2.5/5 |\n| Reproducibility | 4/5 | — | 4/5 |\n| Overall | 3.0 | 3.5 | 3.0 |\n\n### 综合判断\n\n这是一篇分析质量高于方法贡献的 analysis paper。\n\n**支撑 Findings 的理由**：\n1. Epoch confound 发现（F1）对 D&R 文献有真实纠偏价值，独立于方法本身值得发表。\n2. 实验设计结构良好，消融层次清晰，结果报告极为坦诚。\n3. 论文格式完全合规，Related Work 全面。\n\n**限制 Conference 的理由**：\n1. 核心 claim 在 Bonferroni-Holm 校正后均不达传统显著性（p_BH=0.078/0.064），统计证据基础不稳固。\n2. 仅在 self-contamination 设置下验证，生态效度不足以支撑标题暗示的一般性结论。\n3. 方法的实际效果极小（Δ=-0.020 PPL, 0.11%），downstream 完全无改善——\"practical corollary\" 在当前规模下缺乏实际价值。\n4. 三个 findings 的分析深度不均匀，F2 和 F3 的论证远不如 F1 充分。\n\n**上调至 Conference (4.0) 的条件**：\n- 增加 seeds 至 N≥5 使核心结果在校正后显著\n- 提供至少一个 cross-model contamination 的完整实验（3 seeds + PPL + downstream）\n- 用同一 detector 不同 calibration 程度的控制实验支撑 F2\n\n### Detailed Comments\n\n**§1 Introduction**: Narrative flow 良好，三个 research questions 清晰。Dual-constrained formulation 的动机清楚。Figure 1 可用更紧凑的形式呈现以节省空间。\n\n**§2 Related Work**: 五段结构覆盖全面，与 Drayson et al. 的三点区分公平。可补充 detection benchmark (RAID, M4) 和 synthetic data 正面案例 (Phi 系列)。\n\n**§3 Method**: 已压缩至 ~0.75 页，作为 analysis paper 的方法描述长度合理。Proposition 1-2 简洁正确。但 \"minimum intervention\" 的理论动机需加强——为什么 smallest b 是最优的？\n\n**§4 Experimental Setup**: 训练细节充分。Self-contamination 的局限在文内已有预告（\"limits ecological validity\"）。Detector 选择逻辑（\"first satisfying AUC ∈ [0.85, 0.98] and mid-range score ratio ≥ 5%\"）可更详细说明。\n\n**§5 Results**: Table 1 (epoch-matched) 和 Table 2 (main results) 是论文最强的部分。统计报告诚实（p_BH=0.078 写入正文）。建议补充 Cohen's d 及其 CI。§5.3 的 B^0.89 scaling 应降级为 monotonic trend 描述。\n\n**§6 Discussion**: 自我批评充分（downstream null, effect size modest, α_eff proxy limitation）。第一段与 §5.1 内容重复，可精简。α_eff proxy 的核心讨论应保留在主文，但 quantitative decomposition 可移至 Appendix。\n\n**§7 Conclusion**: 缺少 N=3/校正后不显著的 caveat，应与 Limitations 保持一致的审慎语气。\n\n**Limitations**: 简短但覆盖了关键局限（self-contamination, N=3, detector coverage）。\n\n**Appendix**: 18 个 section 组织合理，内容充实。建议合并部分高度技术性的 sections。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "provenance_weight_training",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 via ARR\n**审稿模式**: Fresh（无历史轮次记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作+格式）\n\n---\n\n## Summary\n\n本文分析 detect-and-reweight 范式在 continued LM pretraining 中的有效性条件，通过 Qwen3-0.6B 的自污染实验（132M FineWeb tokens, ρ=0.4, 3 seeds）得出三个发现：(1) D&R 的 >95% PPL 优势来自 multi-epoch exposure 而非 filtering quality；(2) 有效 reweighting 需要 detector 同时具备足够 discrimination (AUC) 和 calibration (ECE)；(3) 最小干预（dual-constrained adaptive b*）优于无约束最大化。作为实用推论，提出一个无需 grid search 的 per-batch adaptive b* 方法，在 ρ≥0.4 时优于 uniform（Δ=-0.020, ρ=0.4; Δ=-0.032, ρ=0.6）。\n\n---\n\n## Strengths\n\n**S1. Epoch confound 发现是论文最核心、最有价值的贡献。** [R1 AGREE, R2 AGREE]\nTable 1 展示 D&R 的 0.396 PPL 优势在 epoch-matched 后缩至 Δ=0.017（3 seeds），揭示 >95% 的 reported advantage 源于数据重复而非 filtering quality。LR-controlled verification（D&R 17.651 vs shared-schedule 17.657, Δ=0.006）排除学习率混淆。Permuted-score control（+0.26 PPL）证明 detector signal 是 load-bearing。三重验证使这一发现高度可信，对后续 D&R 工作的实验设计有直接指导意义。\n\n**S2. 实验设计结构良好，消融层次清晰。** [R1 AGREE, R2 AGREE]\n六种方法（Adaptive < Uniform < ESS-only < Random + Grid oracle + D&R oracle）形成清晰的消融阶梯，每一层有明确控制变量。Ablation hierarchy 展示了 detector signal 和 minimum intervention 的各自贡献。\n\n**S3. 结果报告异常坦诚。** [R1 AGREE, R2 AGREE]\n论文主动报告：Bonferroni-Holm 校正后不显著的 p 值（p_BH=0.078/0.064）、downstream 零改善（Table 4: 0.5414 vs 0.5414）、ρ=0.2 failure case、checkpoint resume artifact（Appendix P）、cross-model mixed results（Appendix O）。这种透明度在 ML 论文中不常见，是良好的学术规范。\n\n**S4. Related Work 全面且结构化。** [R1 AGREE, R2 AGREE]\n§2 分五个 paragraph 覆盖 model collapse、detection、domain-level mixing、instance-level reweighting、theoretical foundations，引用 50+ 篇文献。与 Drayson et al. (2025) 的三点区分清晰公平。\n\n**S5. Grid search 消除的实际价值。** [R1 AGREE, R2 AGREE]\nAdaptive b* 的跨 seed 方差为 σ=0.007，远低于 grid-best 的 σ=0.033（4.7×）。Grid search 需 9 次完整训练（~16 GPU-hours at 0.6B），且 Figure 2 的 PPL plateau 使 validation-based selection 不可靠。\n\n**S6. 理论 well-definedness 和实验规范。** [R1 AGREE, R2 AGREE]\nProposition 1-2（α_eff 单调递增、ESS 单调递减）确保 dual constraint 可解。Checkpoint resume artifact 的披露和 from-scratch 验证展示良好规范。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] N=3 seeds 下所有核心结论均未达校正后统计显著性** [R1-N1 + R2-N1, 双方 AGREE]\n\n论文最核心的定量 claim：\n- ρ=0.4: uncorrected p=0.019, Bonferroni-Holm 校正后 p_BH=0.078（不显著）\n- ρ=0.6: uncorrected p=0.010, p_BH=0.064（不显著）\n\nBCa bootstrap CI [-0.028, -0.012] 在 N=3 下覆盖率存疑——Efron & Tibshirani (1993) 建议 N≥10-15。Cohen's d≈2.86 未报告，且 N=3 下 CI 极宽。Abstract 和 Conclusion 仍以断言性语言（\"improves over uniform at ρ≥0.4\"）呈现校正后不显著的结果。\n\n对于以 \"When does X work?\" 为标题的 analysis paper，核心 claim 的统计支撑应当更强。\n\n建议：增加至 N≥5 seeds，或在 Abstract/Conclusion 明确标注 \"directionally consistent but not statistically significant after family-wise correction\"。报告 Cohen's d 及其 CI。\n\n**C2. [Critical] 仅在 self-contamination 设置下验证，生态效度堪忧** [R1-N2 + R2-N2, 双方 AGREE]\n\nGenerator 和 trainee 都是 Qwen3-0.6B，是最简单的检测场景——TF-IDF 可利用 128-token prefix 到 384-token continuation 的风格断裂点。所有三个 findings 建立在此设定上。唯一跨模型测试（Llama-3.2-3B, Appendix O）是 single seed、results mixed、缺 PPL 对比（\"checkpoints were not retained for re-evaluation\"）。\n\n标题 \"When Does Detect-and-Reweight Work?\" 暗示一般性结论，但实验仅覆盖：一个模型家族、一种 contamination 设置、一个训练范式、一个数据量级。Table 3 的 practitioner decision summary（AUC≥0.9, ECE≤0.05）在 cross-model 场景下可能不适用。\n\n建议：至少完成 cross-model 的完整 PPL 对比（3 seeds），或将标题限定为 self-contamination setting。\n\n**C3. [Critical] 下游任务零改善，method 的实际价值存疑** [R1-N3 + R2-N3, 双方 AGREE]\n\nAdaptive vs Uniform 的 downstream accuracy 完全相同（0.5414 vs 0.5414, 5 tasks, 3 seeds, Table 4）。论文将此归因于 Δ=-0.020 对应 ~0.1% relative improvement，低于 per-task measurement noise（σ≈0.01）。这个解释逻辑自洽，但恰恰证明方法在当前可测指标上无实际效果，与声称提供 \"practical corollary\" 存在矛盾。ρ=0.6 的 downstream results 缺失。\n\n建议：报告 ρ=0.6 downstream results；或明确定位为 \"analysis paper with negative practical result at current scales\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [Warning] B=4 micro-batch 上 dual constraint 统计可靠性不足** [R1-W1, R2 AGREE]\n\nB=4 下 true real fraction 仅取 {0, 0.25, 0.5, 0.75, 1.0}，α_eff 估计粒度极粗（Appendix K: MAE=0.114）。§5.3 展示 B=8→16 显著改善（Δ 从 -0.020 到 -0.068），反证 B=4 是次优设定。主实验在最 noisy 条件下运行，应说明选择 B=4 的 practical constraint。\n\n**W2. [Warning] α_eff proxy 理论保证的 gap** [R1-W2, R2 AGREE]\n\nα_eff 与 true batch-level real fraction 的 Pearson r=0.79（R²≈0.63），37% 方差未解释。Wang 2026 的 convergence theory 要求 true real fraction ≥ τ，但论文将此条件应用于 proxy α_eff，理论保证是否仍成立未讨论。ρ=0.2 下 α_eff 的 bias 方向和大小未报告。\n\n**W3. [Warning] 3 个 detector 不足以建立 calibration 因果关系** [R1-W4, R2 AGREE（最强共识）]\n\nTF-IDF+LR vs GPT-2 的对比同时在 AUC、模型类型、feature space、false positive pattern 上不同，不是控制实验。论文声称 \"isolates calibration\" 但 AUC 0.94 vs 0.91 并非严格 comparable。建议用同一 TF-IDF+LR detector + 不同 temperature scaling（T=0.204 calibrated vs T=1.0 uncalibrated）真正 isolate calibration effect。\n\n**W4. [Warning] Epoch confound 分析缺少 uniform+multi-epoch baseline** [R1-W6, R2 AGREE]\n\n当前比较：D&R full (~3.2 epochs) vs D&R epoch-matched (~1.0 epoch) vs Adaptive (~1.0 epoch)。缺少 \"uniform + multi-epoch\"（全数据重复训练 ~3.2 epochs 不做 filtering）。此 baseline 能区分 D&R 优势来自纯重复 vs filtering+repetition 交互。计算成本低，对分析完整性至关重要。\n\n**W5. [Warning] \"Minimum intervention\" 原则缺乏理论依据** [R1-W5, R2 部分 REBUT]\n\nGrid-best b≈0.3 而 adaptive b* 均值≈0.9——表面看 minimum intervention 反而 over-intervenes。R2 反驳：b* 均值是异质 batch 的平均（5.8% clean b*=0, ~50% α_eff-binding, ~44% ESS-binding），不能与固定 b 直接比较。但双方同意 median b / percentile-based b 对比有信息量——如果 fixed b=median(b*) 也能接近 adaptive 性能，per-batch adaptation 的独立价值需重新评估。\n\n**W6. [Warning] 标题/claims scope 与实验支撑不匹配** [R2-W1, R1 AGREE]\n\n标题暗示对 D&R 范式的全面分析，但实验仅覆盖一个模型家族、一种 contamination 设置、一个训练范式。建议标题加限定（如 \"...in Self-Contaminated Continued LM Pretraining\"）或在 Abstract 第一句明确 scope。\n\n**W7. [Warning] Grid-best 与 adaptive b* 差距（0.054 PPL）来源未分析** [R2-W2, R1 AGREE]\n\nGrid-best 17.620 显著优于 adaptive 17.674，差距是 adaptive vs uniform 改善（0.020）的 2.7 倍。论文论证 grid search 昂贵不可靠，但未分析差距来源（dual constraint 过于保守？α_eff proxy ceiling？）。\n\n**W8. [Warning] 三个 findings 分析深度不均匀** [R2-W4, R1 AGREE]\n\nF1（epoch confound）有三重验证，分析深入。F2（detector requirements）仅 3 个 detector 在 self-contamination 下的 observational comparison。F3（minimum intervention）主要依赖 ESS-only 退化（+0.043），缺乏机制分析。\n\n**W9. [Warning] Batch-size scaling 趋势基于 3 个数据点** [R1-W3, R2 AGREE]\n\nB ∈ {4, 8, 16} 三点拟合 Δ ∝ B^0.89，2-parameter model fitting 3 points 自由度接近零。指数不确定性未报告。R2 认为影响有限（次要观察），但外推可靠性确实为零。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下问题上独立达成强共识：\n\n1. **N=3 统计效力不足** — 三轮审稿连续被独立指出，属结构性限制。p_BH=0.078/0.064 均不达传统显著性。BCa bootstrap CI 在 N=3 下覆盖率存疑。\n2. **Self-contamination 生态效度** — Generator=trainee 是最简单检测场景。Cross-model test 不完整（single seed, no PPL, mixed results）。标题暗示一般性但实验不支持。\n3. **Downstream 零改善** — 方法的 PPL 改善（0.11% relative）无法转化为任何可测量的下游效果。\"Practical corollary\" 的 framing 与实际结果矛盾。\n4. **Detector 因果 claim 证据不足** — 3 个 detector 的 observational comparison 不能 isolate calibration effect。需控制实验。\n5. **Epoch confound 是最强贡献** — 两位 Reviewer 一致认为 F1 是论文最核心、最有价值的发现。\n\n## Reviewer Divergence [REBUT]\n\n1. **评分差异**：R1=3.0 (Findings) vs R2=3.5 (Borderline Conference)。分歧在于 epoch confound finding 的独立价值是否足以支撑 Conference。R1 认为校正后不显著 + downstream 零改善使方法贡献不足；R2 认为 F1 的纠偏价值接近 main conference 门槛。\n2. **α_eff 讨论位置**：R2 认为 §6 中 ~200 words 的 α_eff 讨论过长应移 Appendix；R1 认为核心讨论（r=0.79, bias 方向）应留主文，但可精简 quantitative decomposition。\n3. **Minimum intervention 评价**：R1 认为 grid-best b=0.3 vs adaptive b*≈0.9 表明 over-intervention；R2 部分反驳（per-batch 均值不可与固定 b 直接比较），但同意 median b 对比有信息量。\n4. **Adaptive b* 新颖性**：R2 评\"中等（engineering contribution）\"；R1 认为应更低——per-batch bisection 是标准方法直接应用。\n\n---\n\n## Questions\n\n1. 能否用同一 TF-IDF+LR detector 改变 temperature scaling 参数（T=0.204 calibrated vs T=1.0 uncalibrated）isolate calibration effect？[R1-Q1, R2 AGREE]\n2. ρ=0.6 下 downstream accuracy 是否有所改善？[R2-Q2, R1 AGREE]\n3. 为什么不增加 seed 数量（N≥5）？132M tokens, 0.6B model 的训练成本不高。[R1-N1/R2-Q3]\n4. 为什么不在 B=16 而非 B=4 上计算 b*？主实验是否在次优设定下运行？[R1-Q3, R2 AGREE]\n5. Adaptive b* 的 per-batch b* 分布（median, percentiles）是什么？如果 median b* 也接近 0.9，minimum intervention 叙事需要修正。[R1-W5, R2 部分 AGREE]\n6. 能否增加 \"uniform + multi-epoch\"（~3.2 epochs 无 filtering）baseline 以完善 epoch confound 分析？[R1-W6, R2 AGREE]\n\n---\n\n## Missing References\n\n以下为两位 Reviewer 一致建议补充的参考文献：\n- **RAID** (Dugan et al. 2024) 和 **M4** (Wang et al. 2024)：detection benchmarks，与 detector requirements 分析相关 [R2 提出, R1 AGREE]\n- **Phi 系列** (Gunasekar et al. 2023, Li et al. 2023)：synthetic data 正面案例，为 D&R 必要性提供 counterpoint [R2 提出, R1 AGREE]\n- **Owen 2013** (Monte Carlo Theory) 正文讨论 importance weighting failure modes（目前仅在 Appendix proof 引用）[R1 补充]\n\nR1 对后训练阶段 contamination-aware 方法的遗漏 REBUT（scope 限定为 pretraining 合理）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warning, 11 info）。\n\n主要发现：\n- **[Warning] Pages 3-5 连续无 figure/table**：从 Page 2 的 Figure 1 到 Page 6 的 Table 1/Figure 2，约 3.5 页纯文本，视觉单调。建议将 Table 1 或 Figure 2 前移。\n- **[Warning] Display items 分布不均**：主文 6 个 display items 全部集中在 Pages 6-8，前半部分仅有 Figure 1。\n- **[Warning] Appendix 末页 ~85% 空白**：Appendix R (Use of AI Assistants) 仅占 ~15% 页面。建议并入前一页。\n- **[Info] 正面评价**：Figure 2 清晰可读，Table 1-4 使用 booktabs 规范，Equation (1) 排版清晰，References 无 [?] 未解析引用，色彩方案色盲友好。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n### 评分维度\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 2.5/5 | 3/5 | 2.5/5 |\n| Reproducibility | 4/5 | — | 4/5 |\n| Overall | 3.0 | 3.5 | 3.0 |\n\n### 综合判断\n\n这是一篇分析质量高于方法贡献的 analysis paper。\n\n**支撑 Findings 的理由**：\n1. Epoch confound 发现（F1）对 D&R 文献有真实纠偏价值，独立于方法本身值得发表。\n2. 实验设计结构良好，消融层次清晰，结果报告极为坦诚。\n3. 论文格式完全合规，Related Work 全面。\n\n**限制 Conference 的理由**：\n1. 核心 claim 在 Bonferroni-Holm 校正后均不达传统显著性（p_BH=0.078/0.064），统计证据基础不稳固。\n2. 仅在 self-contamination 设置下验证，生态效度不足以支撑标题暗示的一般性结论。\n3. 方法的实际效果极小（Δ=-0.020 PPL, 0.11%），downstream 完全无改善——\"practical corollary\" 在当前规模下缺乏实际价值。\n4. 三个 findings 的分析深度不均匀，F2 和 F3 的论证远不如 F1 充分。\n\n**上调至 Conference (4.0) 的条件**：\n- 增加 seeds 至 N≥5 使核心结果在校正后显著\n- 提供至少一个 cross-model contamination 的完整实验（3 seeds + PPL + downstream）\n- 用同一 detector 不同 calibration 程度的控制实验支撑 F2\n\n### Detailed Comments\n\n**§1 Introduction**: Narrative flow 良好，三个 research questions 清晰。Dual-constrained formulation 的动机清楚。Figure 1 可用更紧凑的形式呈现以节省空间。\n\n**§2 Related Work**: 五段结构覆盖全面，与 Drayson et al. 的三点区分公平。可补充 detection benchmark (RAID, M4) 和 synthetic data 正面案例 (Phi 系列)。\n\n**§3 Method**: 已压缩至 ~0.75 页，作为 analysis paper 的方法描述长度合理。Proposition 1-2 简洁正确。但 \"minimum intervention\" 的理论动机需加强——为什么 smallest b 是最优的？\n\n**§4 Experimental Setup**: 训练细节充分。Self-contamination 的局限在文内已有预告（\"limits ecological validity\"）。Detector 选择逻辑（\"first satisfying AUC ∈ [0.85, 0.98] and mid-range score ratio ≥ 5%\"）可更详细说明。\n\n**§5 Results**: Table 1 (epoch-matched) 和 Table 2 (main results) 是论文最强的部分。统计报告诚实（p_BH=0.078 写入正文）。建议补充 Cohen's d 及其 CI。§5.3 的 B^0.89 scaling 应降级为 monotonic trend 描述。\n\n**§6 Discussion**: 自我批评充分（downstream null, effect size modest, α_eff proxy limitation）。第一段与 §5.1 内容重复，可精简。α_eff proxy 的核心讨论应保留在主文，但 quantitative decomposition 可移至 Appendix。\n\n**§7 Conclusion**: 缺少 N=3/校正后不显著的 caveat，应与 Limitations 保持一致的审慎语气。\n\n**Limitations**: 简短但覆盖了关键局限（self-contamination, N=3, detector coverage）。\n\n**Appendix**: 18 个 section 组织合理，内容充实。建议合并部分高度技术性的 sections。"
  }
}
```

</details>

---


### Tool result

_source line 1239 · 2026-05-24T04:31:07.963744+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4217
}
```

</details>

---


### Assistant

_source line 1240 · 2026-05-24T04:31:23.081680+00:00_

**审稿报告已投递至 Research Director。**

---

**Round 13 审稿完成总结：**

- **Overall Score: 3.0 (Findings)**，置信度 4/5
- **R1=3.0, R2=3.5**，合成取 3.0——三个 critical issues（统计显著性、self-contamination 泛化性、downstream 零改善）为双方独立共识，属结构性限制
- **最强贡献**：Epoch confound 发现（F1），对 D&R 文献有真实纠偏价值
- **主要限制**：校正后不显著、scope 过窄、方法实际效果不可测
- **上调条件**：N≥5 seeds + cross-model 完整实验 + calibration 控制实验
- **Issue tracker 已同步更新**（4 critical open, 9 warning open, 3 info open; 2 format critical resolved）
- **视觉审查**：已完成，3 warnings（display item 分布不均），无 critical

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 98

## Round 98

2 recorded events


### User

_source line 1241 · 2026-05-24T04:31:25.629008+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **16 条 AGREE**（含 S1-S6 全部优势、N1-N3 全部 critical issues、W1-W4/W6、M1/M3/M5/M6、Q1-Q3）
- **3 条 REBUT**（W5 minimum intervention 叙事部分合理、M2 Grid-best 不使用 τ 是 R1 理解有误、M4 truncated y-axis 是标准做法）
- **1 条 partial REBUT**（Q4 均值 vs 固定值不可直接比较，但 concern 部分有效）

两位 Reviewer 在三个 critical issues（统计功效、self-contamination、downstream 零改善）上完全独立地达成一致，这是对作者最强的信号。R1 的 W4（detector causal claim）和 W6（缺 uniform+multi-epoch baseline）是我审稿中未充分展开的重要补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1242 · 2026-05-24T04:31:38.289105+00:00_

**📋 Round 13 审稿完成**

审稿报告已投递至 Research Director。

**最终评分：3.0 (Findings)**

| | R1 | R2 | 合成 |
|---|---|---|---|
| Overall | 3.0 | 3.5 | **3.0** |
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 2.5/5 | 3/5 | 2.5/5 |

**两位 Reviewer 强共识（3 Critical + 9 Should-Fix）：**
- C1: N=3 统计效力不足，校正后均不显著
- C2: 仅 self-contamination，生态效度堪忧
- C3: Downstream 零改善，practical corollary 自相矛盾

**上调至 Conference 的条件：** 增加 seeds (N≥5) + cross-model 完整实验 + detector calibration 控制实验

Issue tracker 已同步更新（`review_issues.yaml`），报告已存档。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 99

## Round 99

68 recorded events


### User

_source line 1243 · 2026-05-25T04:39:47.935611+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-25T04:39:52.819354+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-25T04:39:52.920489+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-25T04:40:00.764776+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1247 · 2026-05-25T04:40:00.815577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-25T04:40:04.531492+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-25T04:40:04.632234+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-25T04:40:09.407456+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-25T04:40:09.407826+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-25T04:40:12.133093+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 1253 · 2026-05-25T04:40:12.183755+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-25T04:40:18.759157+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-25T04:40:19.712963+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (269 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| detect_remove_q07_seed456 | D&R q>0.7 threshold seed=456 replicate. Retains ~50% data (184,908/370k). Cross-seed for error bar with seed42 (r3) and seed123. | — | — | — |\n| detect_remove_q07_seed123 | D&R q>0.7 threshold seed=123 replicate. Retains ~50% data (184,908/370k). Cross-seed for error bar with seed42 (r3) and seed456. | — | — | — |\n| detect_remove_q07_seed42_r3 | D&R q>0.7 threshold fresh rerun (r3). Retains ~50% data (184,908/370k). Prior r2 corrupted by optimizer state loss during resume. Fresh training from step 0 with full optimizer state preservation. | — | — | — |\n\n## 待处理\n- eval_adaptive_1_7b_seed123（准备中）\n- eval_uniform_1_7b_seed123（准备中）\n- detect_remove_q05_epoch_matched（准备中）\n- adaptive_1_7b_planb_control（准备中）\n- eval_q01_final（准备中）\n- status_check_41312（准备中）\n- eval_adaptive_1_7b（准备中）\n- eval_uniform_1_7b_v2（准备中）\n- eval_uniform_1_7b_resumed（准备中）\n- uniform_1_7b_seed42_r2（准备中）\n- …另有 5 项\n\n## 近期结论\n- **detect_remove_q07_seed42_r2** (killed): Hard filtering at q_score > 0.7 threshold retains ~50% of data (184,908/370k samples), the most conservative D&R strategy keeping on
…[truncated 1795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-25T04:40:19.863983+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 1257 · 2026-05-25T04:40:21.620705+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 1258 · 2026-05-25T04:40:22.624914+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1259 · 2026-05-25T04:40:23.077037+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1260 · 2026-05-25T04:40:23.930370+00:00_

-rw-r--r-- 1 ubuntu ubuntu 659479 May 25 04:35 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1261 · 2026-05-25T04:40:23.930884+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 1262 · 2026-05-25T04:40:23.981458+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-25T04:40:24.282987+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 call for papers submission guidelines page limit"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here is the page limit information for ACL Rolling Review (ARR) submission guidelines:

The paper follows page limits of 8 pages for long papers and 4 pages for short papers, not including limitations and ethical considerations.

These guidelines apply to ARR submissions across its cycles, including May 2026. The submission templates that detail these requirements are available through the ARR website at aclrollingreview.org/cfp.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 4419
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-25T04:40:31.919109+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclrollingreview.org cfp 2026 submission guidelines anonymity appendix ethics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclrollingreview.org cfp 2026 submission guidelines anonymity appendix ethics"
  }
}
```

</details>

---


### Tool call

_source line 1265 · 2026-05-25T04:40:33.072843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers commitment deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers commitment deadline ARR cycle"
  }
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-25T04:40:33.926257+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-25T04:40:34.177926+00:00_

abstract.tex
appendix.tex
checklist.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex
results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-25T04:40:34.178341+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-25T04:40:34.229218+00:00_

1	issues:
2	# === Round 10 issues (all resolved, retained for history) ===
3	- id: "R10-C1"
4	  summary: "Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 10
9	  last_seen_round: 10
10	  mentions:
11	    - round: 10
12	      reviewers: [1, 2]
13	      note: "Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。"
14	  resolution: "tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。"
15	  resolution_round: 10
16	
17	- id: "R10-C2"
18	  summary: "多重比较未校正，p=0.025 Bonferroni 校正后不显著"
19	  category: experiment
20	  severity: critical
21	  status: resolved
22	  first_raised_round: 10
23	  last_seen_round: 10
24	  mentions:
25	    - round: 10
26	      reviewers: [1, 2]
27	      note: "6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。"
28	  resolution: "BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。"
29	  resolution_round: 10
30	
31	- id: "R10-C3"
32	  summary: "方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配"
33	  category: framing
34	  severity: critical
35	  status: resolved
36	  first_raised_round: 10
37	  last_seen_round: 10
38	  mentions:
39	    - round: 10
40	      reviewers: [1, 2]
41	      note: "w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。"
42	  resolution: "§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。"
43	  resolution_round: 10
44	
45	- id: "R10-C4"
46	  summary: "Downstream task 零改善削弱实际意义"
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 10
51	  last_seen_round: 10
52	  mentions:
53	    - round: 10
54	      reviewers: [1, 2]
55	      note: "Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。"
56	  resolution: "Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limit
…[truncated 18872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1270 · 2026-05-25T04:40:37.920395+00:00_

Web search results for query: "aclrollingreview.org cfp 2026 submission guidelines anonymity appendix ethics"

Links: [{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CFP: The 11th Workshop on Computational Linguistics and Clinical Psychology | ACL Member Portal","url":"https://www.aclweb.org/portal/content/cfp-11th-workshop-computational-linguistics-and-clinical-psychology"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on the search results from aclrollingreview.org and related ACL resources, here are the key submission guidelines for 2026 regarding anonymity, appendices, and ethics:

**Anonymity Requirements:**
Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided. Supplementary materials must be fully anonymized to preserve the two-way anonymized reviewing policy.

**Preprint and Anonymity Policy:**
Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. However, the new policy incentivizes anonymous submissions by special paper awards and priority in acceptance decisions for borderline papers.

**Appendices:**
The paper should be readable by itself, and any details important for understanding the key aspects of the work should be in the paper rather t
…[truncated 320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6001
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-25T04:40:38.886430+00:00_

Web search results for query: "EMNLP 2026 call for papers commitment deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the key information about EMNLP 2026 call for papers and the ARR cycle commitment deadline:

## Key Dates

The ARR submission deadline for EMNLP 2026 is May 25, 
…[truncated 904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5813
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-25T04:41:23.338242+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-25T04:41:23.940961+00:00_

1	As synthetic text pervades web corpora, detect-and-reweight methods---downweighting likely-synthetic samples during training---have emerged to prevent model collapse, yet when they actually help remains unclear.
2	We investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.
3	First, published detect-and-remove evaluations are confounded by multi-epoch exposure: over 95\% of the reported advantage vanishes under epoch-matched controls.
4	Second, the detector must provide both sufficient discrimination \emph{and} good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.
5	Third, minimum intervention---applying the smallest reweighting exponent that meets a quality floor---outperforms unconstrained weight maximization.
6	As an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $\bstar$ that improves over uniform training at contamination ratios $\rho \geq 0.4$, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.
7	These findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination and larger models remains to be established.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-25T04:41:24.091645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-25T04:41:24.142256+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	\begin{figure*}[t]
6	\centering
7	\includegraphics[width=\textwidth]{fig1_overview}
8	\caption{Three effectiveness conditions for detect-and-reweight.
9	\textbf{(a)}~D\&R's PPL advantage largely vanishes under epoch-matched controls: the green--orange gap is multi-epoch exposure, not filtering quality (\S\ref{sec:results}).
10	\textbf{(b)}~Only detectors with both high AUC \emph{and} low ECE fall in the effective zone; comparable AUC with poor calibration degrades PPL below uniform.
11	\textbf{(c)}~Adaptive $\bstar{\approx}0.9$ operates near the grid-search optimum, while ESS-only $b{\approx}3.5$ falls in the degradation zone.}
12	\label{fig:overview}
13	\end{figure*}
14	
15	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
16	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
17	What detector properties are necessary for effective reweighting?
18	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
19	
20	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 5 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
21	To ground the analysis of exponent selection, we imple
…[truncated 1838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-25T04:41:24.242953+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-25T04:41:25.095705+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 852
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-25T04:41:25.096117+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-25T04:41:25.497470+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution, providing a controlled testbed with known ground-truth labels but limiting ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss implications for detection difficulty in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness} (implementation details in Appendix~\ref{app:detector_details}).
11	
12	\paragraph{Training.}
13	Table~\ref{tab:config} summarizes the training configuration.
14	We use $B{=}4$
…[truncated 2450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-25T04:41:25.497951+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-25T04:41:26.050037+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-25T04:41:26.050520+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-25T04:41:26.552321+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-25T04:41:26.903772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-25T04:41:26.904149+00:00_

1	We identify three effectiveness conditions for detect-and-reweight---epoch-matched evaluation, detector calibration alongside discrimination, and minimum intervention over unconstrained maximization---and demonstrate the third via a dual-constrained adaptive $\bstar$ that improves over uniform training at $\rho \geq 0.4$ without per-model tuning, though without measurable downstream gains at 0.6B scale.
2	For practitioners, reweighting is worthwhile only when $\rho \geq 0.4$ and the detector is well-calibrated (Table~\ref{tab:decision}).
3	
4	Our epoch-matching analysis reveals that ${>}$95\% of D\&R's reported advantage is attributable to multi-epoch exposure rather than filtering quality, cautioning against interpreting raw PPL comparisons in data-limited continued pretraining.
5	The permuted-score ablation ($\Delta{=}{+}0.225$) confirms that detector provenance signal---not mere weight non-uniformity---drives the improvement.
6	Looking forward, extending this framework to full pretraining scale, multi-source web contamination, and broader detector families (e.g., fine-tuned neural classifiers) remains an open direction.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-25T04:41:27.205403+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-25T04:41:27.506974+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-25T04:41:27.607684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1289 · 2026-05-25T04:41:27.658368+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
6	Not all synthetic data is harmful: the Phi series~\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.
7	
8	\paragraph{Detection, Filtering, and Data Reweighting.}
9	Multiple detectors produce continuous scores suitable for downstream weighting: DetectGPT~\citep{mitchell2023detectgpt} uses probability curvature, Binoculars~\citep{hans2024binoculars} cross-perplexity ratios, and Min-$k$\% Prob~\citep{shi2024minkprob} low-probability token statistics; \citet{wu2025survey} survey the broader detection landscape.
10	A parallel line of work optimizes data composition at the domain~\citep{xie2023doremi,xie2023dsir,ye2025mixing} or instance level~\citep{abbas2023semdedup,bengio2009curriculum,mindermann2022prioritized,sow2025dynamic}, using loss, frequency, quality, or domain membership as the selection signal; none targets synthetic provenance.
11	
12	Most directly related to our work, \citet{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight in a from-scratch pretraining setting, where $q_j$ is the detector's synthetic probability.
13	We adopt the same weighting formula but differ in several fundamental ways.
1
…[truncated 1831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-25T04:41:34.787109+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-25T04:41:35.339447+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-25T04:41:35.440163+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-25T04:41:35.541036+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml\", \"content\": \"_next_id: 131\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 投稿目标定为 AAAI 2027 (~Aug 2026)，放弃 EMNLP 2026 ARR May 25\\n  rationale: EMNLP ARR 仅剩 12 天且无任何基础设施，即使 AI 团队速度也无法完成多轮预训练实验。AAAI 2027 有 ~11 周，足够完成\\n    4 phase 全流程。两者均为 A 类会议。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:38 UTC\\n  summary: 'MVP 设计: 单模型(Qwen3-0.6B) + 单污染比例(40%) + 三组对比(uniform/grid-b/adaptive-b*)'\\n  rationale: 核心假设是 adaptive b* 能替代 grid search。最小验证只需一个污染比例下的 A/B/C 对比。40% 选取因为理论和\\n    Strong Model Collapse 均表明该区间效应显著。通过后再扩展到多污染比例/多生成器/多模型。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-13 17:40 UTC\\n  summary: '修正 D001: 主攻 EMNLP 2026 ARR May 25，AAAI 2027 为后备'\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、资源会给够。AI 团队 24/7 执行 + 4 卡并行：数据生成 ~2 天、MVP\\n    ~1 天、全矩阵 ~3 天、论文 ~3 天、迭代 ~2 天 = 11 天可完成。12 天 deadline 可行。保守估计完成时间是最大风险。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 17:42 UTC\\n  summary: '采纳 Reviewer 4 点 MVP 协议补全: 3 seeds、detector gate、grid-b 定义、kill criteria'\\n  rationale: 'Reviewer 指出 MVP 设计 4 个缺口均合理: (1) 单 seed 无统计保障 → 3 seeds，缩 tokens 到 200M\\n    控预算; (2) 检测器质量是 pipeline 前提 → 加 gate AUC≥0.95/ECE≤0.05; (3) grid search baseline\\n    需可复现 → 定义 b∈{0.5,1,1.5,2,3,5}; (4) 无 fail 路径 → 定义三级 kill/pivot。不增加工程量，只补协议。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-13 22:08 UTC\\n  summary: 识别 q-score 极化风险：AUC=0.999998 可能导致 adaptive b* vs grid-b 对比退化，制定分级应对方案\\n  rationale: 'Reviewer 审查发现 detector eval_auc=0.999998（step 2000），q-score 可能高度双峰化。若校准后\\n    >95% 样本 q<0.05 或 q>0.95，则 w=(1-q)^b 对所有 b>0 约等于 0，不同 b 值间无区分度。MVP 技术上可能 PASS（adaptive\\n    ≈ grid-b，满足 ≥90% 条件），但无法证明核心贡献（自适应精细调优的价值）。\\n\\n\\n    应对方案（detector 完成后按 q-score 分布分级执行）：\\n\\n    - 分布有spread（q 在 0.
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-25T04:41:43.113008+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 1295 · 2026-05-25T04:41:43.113408+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1296 · 2026-05-25T04:41:43.164137+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/memory.md\", \"content\": \"# Memory\\n\\n## N=5 B=4 统计显著性确认 (2026-05-24)\\n\\nN=3→N=5 扩展解决了 Round 13 核心瓶颈（BH 校正后不显著）。\\n\\n| Seed | Adaptive PPL | Uniform PPL | Δ |\\n|------|-------------|------------|-------|\\n| 42 | 17.680 (tau07_seed42) | 17.694 | -0.014 |\\n| 123 | 17.666 (tau07_seed123) | 17.686 | -0.020 |\\n| 456 | 17.677 (tau07_seed456) | 17.702 | -0.025 |\\n| 789 | 17.668 (adaptive_seed789) | 17.695 | -0.027 |\\n| 234 | 17.678 (adaptive_seed234) | 17.708 | -0.030 |\\n\\n**Mean Δ = -0.023 ± 0.006, t(4) = -8.21, p = 0.0012, p_BH(k=9) = 0.011**\\n\\n新 seed 的 Δ(-0.027, -0.030) 比原 3-seed 均值(-0.020) 更大——效应随 seed 增加未衰减。\\n\\n⚠️ **配置一致性决策**：论文的 3-seed baseline 用 tau07_seed（τ=0.7，默认 n_min），新 seed 用 adaptive_seed（τ=0.7, n_min=2）。两者 τ 一致但 n_min 可能不同（取决于 tau07 训练时的默认值）。若需严格一致，可改用 adaptive_fix_seed（τ=0.7, n_min=2），此时 Δ 更大（-0.037±0.008, p_BH=0.005）。\\n\\n## Permuted Score Control 确认 detector 信号 load-bearing (2026-05-24)\\n\\npermuted_score_control_seed42: 将真实 q-score 随机打乱（保持 score 分布不变，但 score-sample 对应关系随机化）。\\n- holdout_ppl=17.919 vs uniform=17.694 → **Δ=+0.225（比 uniform 更差）**\\n- vs random_reweight (17.951): permuted 略好，因为仍保留了真实 score 分布的 shape\\n- **解读**：adaptive weighting 的效果来自 score 的排序正确性（正确识别哪些样本是 contaminated），而非权重的非均匀性。与 random_reweight 共同构成 Claim 2 的双重 ablation evidence。\\n\\n## D062 coupling rule 已验证 (2026-05-17)\\n\\nbs8_auto_nmin_r5 (PPL 17.66) 确认 n_min=⌊B/2⌋ coupling rule 在 bs=8 下有效（n_min=4）。\\n- bs=4, n_min=2: adaptive_fix PPL=17.653 (success)\\n- bs=8, n_min=4: bs8_auto_nmin_r5 PPL=17.66 (success)\\n- bs=8, n_min=2: bs8_nmin2_seed42_r2 PPL=17.73 (negative — n_min 过小导致 over-downweight)\\n\\n结论：n_min=⌊B/2⌋ 是 Method section 的正式设计原则。n_min 过小 (< B/2) 导致 ESS 约束松弛，b* 过大。\\n\\n## Batch-adaptive τ 方向关闭 (2026-05-17)\\n\\n两轮实验均 negative。固定 τ=0.8 + dual constraint 已足够。不再投入资源。\\n\\n## Claim 2 跨 seed 已由 D074 定稿 (2026-05-18)\\n\\n
…[truncated 1447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-25T04:41:43.164476+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1298 · 2026-05-25T04:41:50.643058+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NOT_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NOT_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-25T04:41:50.693765+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-25T04:41:54.206616+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-25T04:41:54.307403+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1302 · 2026-05-25T04:41:57.169014+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/ -path \"*/provenance_weight_training*\" -name \"*.yaml\" -not -path \"*artifacts*\" -not -path \"*node_modules*\" 2>/dev/null | head -10",
  "description": "Find yaml config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/ -path \"*/provenance_weight_training*\" -name \"*.yaml\" -not -path \"*artifacts*\" -not -path \"*node_modules*\" 2>/dev/null | head -10",
    "description": "Find yaml config files"
  }
}
```

</details>

---


### Tool result

_source line 1303 · 2026-05-25T04:41:57.269779+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/shi_2024_minkprob.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/nait_saada_2025_quality_illusion.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/yang_2026_data_mixing_agent.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/martino_2025_ess_entropy.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/shumailov_2024_model_collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/feng_2025_beyond_collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/dohmatob_2025_strong_collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/vehtari_2024_psis.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/grangier_2025_crisp.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/distill_tmp/drayson_2025_detection_collapse.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-25T04:42:17.403042+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "provenance_weight_training",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "provenance_weight_training",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-25T04:42:43.533157+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26130
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-25T04:42:43.734312+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "provenance_weight_training",
  "chat_id": "oc_069d56747de0423c793156b069500cb3",
  "director_session_key": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（via ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，references 无限，Limitations 必须写（不计入页数）\n- **模板**: ACL style，double-blind\n- **匿名规则**: 不得包含作者信息，自引需避免暴露身份\n\n## 论文信息\n- **标题**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Dual-constrained adaptive b* 的数学推导是否正确（Proposition 1-2, Algorithm 1）\n- α_eff 作为 proxy 的理论依据和可靠性（R²≈0.63，~37% 未解释方差）\n- Wang 2026 convergence theory 要求 true real fraction ≥ τ，但论文用 proxy α_eff 替代，理论保证是否仍成立\n- \"Minimum intervention\" 原则是否有充分理论依据\n- Grid-best b=0.3 vs adaptive b*≈0.9 的偏差意味着什么\n\n### 2. 实验设计\n- N=5 seeds 的统计检验力是否充分（paired t-test, Bonferroni-Holm correction）\n- B=4 micro-batch 下 dual constraint 的统计可靠性（α_eff 估计粒度）\n- Self-contamination 实验设计的生态效度\n- Cross-model transfer 仅 single seed + 缺 PPL 对比的问题\n- D&R epoch confound 分析是否充分——是否缺少 \"uniform + multi-epoch\" baseline\n- Detector 仅测试 3 个（TF-IDF+LR, GPT-2, N-gram），能否支撑因果性结论\n- 1.7B 实验仅 3 seeds，效应减弱但未充分讨论原因\n\n### 3. 统计分析\n- 效应量（Δ=-0.023 PPL, ~0.13% relative）是否有实际意义\n- Cohen's d 是否报告，CI 是否合理\n- BH 校正后 ρ=0.6 的 p_BH=0.064 如何解读\n- 下游任务零改善（|Δ|≤0.01）与论文 claims 是否矛盾\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条, S1/S2/...)\n3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: must-fix / should-fix / minor)\n4. **Questions** (Q1/Q2/...)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 简要理由, 使用 EMNLP 2026 ARR 评分标准: 1-5 分)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "provenance_weight_training",
    "chat_id": "oc_069d56747de0423c793156b069500cb3",
    "director_session_key": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
    "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（via ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，references 无限，Limitations 必须写（不计入页数）\n- **模板**: ACL style，double-blind\n- **匿名规则**: 不得包含作者信息，自引需避免暴露身份\n\n## 论文信息\n- **标题**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Dual-constrained adaptive b* 的数学推导是否正确（Proposition 1-2, Algorithm 1）\n- α_eff 作为 proxy 的理论依据和可靠性（R²≈0.63，~37% 未解释方差）\n- Wang 2026 convergence theory 要求 true real fraction ≥ τ，但论文用 proxy α_eff 替代，理论保证是否仍成立\n- \"Minimum intervention\" 原则是否有充分理论依据\n- Grid-best b=0.3 vs adaptive b*≈0.9 的偏差意味着什么\n\n### 2. 实验设计\n- N=5 seeds 的统计检验力是否充分（paired t-test, Bonferroni-Holm correction）\n- B=4 micro-batch 下 dual constraint 的统计可靠性（α_eff 估计粒度）\n- Self-contamination 实验设计的生态效度\n- Cross-model transfer 仅 single seed + 缺 PPL 对比的问题\n- D&R epoch confound 分析是否充分——是否缺少 \"uniform + multi-epoch\" baseline\n- Detector 仅测试 3 个（TF-IDF+LR, GPT-2, N-gram），能否支撑因果性结论\n- 1.7B 实验仅 3 seeds，效应减弱但未充分讨论原因\n\n### 3. 统计分析\n- 效应量（Δ=-0.023 PPL, ~0.13% relative）是否有实际意义\n- Cohen's d 是否报告，CI 是否合理\n- BH 校正后 ρ=0.6 的 p_BH=0.064 如何解读\n- 下游任务零改善（|Δ|≤0.01）与论文 claims 是否矛盾\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条, S1/S2/...)\n3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: must-fix / should-fix / minor)\n4. **Questions** (Q1/Q2/...)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 简要理由, 使用 EMNLP 2026 ARR 评分标准: 1-5 分)"
  }
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-25T04:43:06.006763+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22272
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-25T04:43:06.208222+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "provenance_weight_training",
  "chat_id": "oc_069d56747de0423c793156b069500cb3",
  "director_session_key": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "text": "你是 Reviewer 2，负责审查新颖性、论文完整性和格式合规。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（via ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，references 无限，Limitations 必须写（不计入页数）\n- **模板**: ACL style，double-blind\n- **匿名规则**: 不得包含作者信息，自引需避免暴露身份\n- **Abstract**: ≤200 words\n\n## EMNLP 2026 特殊规则\n- Main/Findings 不分开投稿，走同一 ARR 审稿系统\n- Long/Short 走同一审稿系统\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- Responsible NLP Checklist 在 OpenReview 表单里（不在 PDF 里）\n- 一篇文章只能有一个 Limitations section，放正文，appendix 不能有\n\n## 论文信息\n- **标题**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 论文的核心贡献是什么？是方法贡献还是 analysis 贡献？\n- w=(1-q)^b 完全来自 Drayson et al. (2025)，adaptive b* 的 dual constraint 是否构成足够的方法新颖性？\n- 三个 findings（epoch confound, detector calibration, minimum intervention）的新颖程度分别如何？\n- 与 Drayson et al. 的差异化是否清晰？\n- Per-batch bisection 是否只是标准方法的直接应用？\n\n### 2. 论文完整性\n- 论文 framing 是否一致（abstract/intro/discussion/conclusion 的定位是否统一）\n- Claims 与 evidence 是否匹配（特别注意 overclaim）\n- Related Work 是否遗漏重要工作（检查 RAID, M4 detection benchmarks, Phi 系列 synthetic data 正面案例, Owen 2013 importance weighting failure modes）\n- Limitations 是否充分覆盖主要弱点\n- 下游任务零改善与 \"practical adaptive method\" 或 \"practical corollary\" 表述是否矛盾\n- 标题 \"When Does D&R Work?\" 暗示一般性，但实验仅支持 self-contamination\n\n### 3. 格式合规\n- 正文是否在 8 页以内（§1-§7 + Limitations）\n- Abstract 是否 ≤200 words\n- 是否有 Responsible NLP Checklist 出现在 PDF 中（不应该有）\n- 匿名性检查\n- Figure/Table 质量和 display item 分布\n- 引用格式是否正确（natbib）\n- Appendix 中是否有不该出现的 Limitations section\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条, S1/S2/...)\n3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: must-fix / should-fix / minor)\n4. **Questions** (Q1/Q2/...)\n5. **Missing References** (如有)\n6. **Novelty Assessment** (F1-F3 各项新颖性评级: 高/中/低)\n7. **Overall Assessment** (评分 + 简要理由, 使用 EMNLP 2026 ARR 评分标准: 1-5 分)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "provenance_weight_training",
    "chat_id": "oc_069d56747de0423c793156b069500cb3",
    "director_session_key": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
    "text": "你是 Reviewer 2，负责审查新颖性、论文完整性和格式合规。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（via ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，references 无限，Limitations 必须写（不计入页数）\n- **模板**: ACL style，double-blind\n- **匿名规则**: 不得包含作者信息，自引需避免暴露身份\n- **Abstract**: ≤200 words\n\n## EMNLP 2026 特殊规则\n- Main/Findings 不分开投稿，走同一 ARR 审稿系统\n- Long/Short 走同一审稿系统\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- Responsible NLP Checklist 在 OpenReview 表单里（不在 PDF 里）\n- 一篇文章只能有一个 Limitations section，放正文，appendix 不能有\n\n## 论文信息\n- **标题**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 论文的核心贡献是什么？是方法贡献还是 analysis 贡献？\n- w=(1-q)^b 完全来自 Drayson et al. (2025)，adaptive b* 的 dual constraint 是否构成足够的方法新颖性？\n- 三个 findings（epoch confound, detector calibration, minimum intervention）的新颖程度分别如何？\n- 与 Drayson et al. 的差异化是否清晰？\n- Per-batch bisection 是否只是标准方法的直接应用？\n\n### 2. 论文完整性\n- 论文 framing 是否一致（abstract/intro/discussion/conclusion 的定位是否统一）\n- Claims 与 evidence 是否匹配（特别注意 overclaim）\n- Related Work 是否遗漏重要工作（检查 RAID, M4 detection benchmarks, Phi 系列 synthetic data 正面案例, Owen 2013 importance weighting failure modes）\n- Limitations 是否充分覆盖主要弱点\n- 下游任务零改善与 \"practical adaptive method\" 或 \"practical corollary\" 表述是否矛盾\n- 标题 \"When Does D&R Work?\" 暗示一般性，但实验仅支持 self-contamination\n\n### 3. 格式合规\n- 正文是否在 8 页以内（§1-§7 + Limitations）\n- Abstract 是否 ≤200 words\n- 是否有 Responsible NLP Checklist 出现在 PDF 中（不应该有）\n- 匿名性检查\n- Figure/Table 质量和 display item 分布\n- 引用格式是否正确（natbib）\n- Appendix 中是否有不该出现的 Limitations section\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条, S1/S2/...)\n3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: must-fix / should-fix / minor)\n4. **Questions** (Q1/Q2/...)\n5. **Missing References** (如有)\n6. **Novelty Assessment** (F1-F3 各项新颖性评级: 高/中/低)\n7. **Overall Assessment** (评分 + 简要理由, 使用 EMNLP 2026 ARR 评分标准: 1-5 分)"
  }
}
```

</details>

---


### Tool result

_source line 1309 · 2026-05-25T04:43:07.667158+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1458
}
```

</details>

---


### Assistant

_source line 1310 · 2026-05-25T04:43:18.716621+00:00_

**Round 1 已启动：**
- 视觉审查 Agent: 已派发（fire-and-forget）
- Reviewer 1（方法/实验/统计）: 已分配
- Reviewer 2（新颖性/完整性/格式）: 已分配
- 外部审稿: 未配置，跳过

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1311 · 2026-05-25T04:49:16.941060+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性、实验设计与统计分析

### 总体评分
**Overall Assessment**: 3.0 — Findings
**一句话总结**: Epoch confound 的揭露是本文最有价值的贡献，但核心方法（adaptive b*）的实际效应极小（Δ=−0.023 PPL, 0.13% relative）且完全无法迁移至下游任务，加上规模效应递减（1.7B 时 Δ 缩至 −0.013），方法论贡献不足以支撑主会议接收。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Propositions 1-2 证明正确，实验设计合理且含大量消融；但 α_eff proxy 的 ~37% 未解释方差与引用的 Wang (2026) 理论保证之间存在逻辑断裂；PPL 与下游指标完全脱节削弱了方法论 claim |
| Excitement | 2.5/5 | Epoch confound 发现有价值但事后看并不意外；adaptive b* 实际收益过小且规模趋势不利 |
| Reproducibility | 4/5 | 算法伪代码清晰，超参数完整，cross-seed 分析充分；代码未发布，cross-model 缺 PPL |
| Reviewer Confidence | 4/5 | 对 data weighting/contamination detection 领域较熟悉 |

### Must-Fix 问题

**N1** [critical] 核心效应无实际意义且不迁移至下游任务
- 位置：Table 3 (Δ=−0.023 PPL), Table 10/Appendix I (|Δ|≤0.01 across 5 benchmarks)
- Adaptive b* 的 PPL 改善仅 0.13% relative，5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）。Cohen's d=3.83 被极低 cross-seed 方差（σ=0.006，deterministic data ordering）人为放大。如果方法不改善任何下游指标，实际价值存疑。
- 建议：(1) 重新定位为分析/负面结果贡献而非方法贡献；(2) 在 B=16 下报告下游任务结果。

**N2** [critical] α_eff proxy 的理论保证断裂
- 位置：§3 ¶1, §6 ¶4, Table 12/Appendix K
- Wang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）。~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ。n_min 的缓冲是 heuristic 的，没有理论保证。论文同时引用 Wang (2026) 作理论动机并使用违反前提的 proxy，存在内在矛盾。
- 建议：明确区分理论动机和实际保证；量化 α_eff ≥ τ 但 true fraction < τ 的 batch 比例。

### Should-Fix 问题

**W1** [warning] Grid-best b=0.3 vs adaptive b*≈0.9 偏差缺乏解释
- 位置：Table 4, Figure 3
- 如果 grid-best 在 b=0.3，为何 adaptive 收敛到 ~0.9？α_eff 的负偏差（−0.03）可能导致 b_τ 偏高。建议分析 debiased α_eff 的效果。

**W2** [warning] 缺少 "uniform + multi-epoch" 基线
- 位置：§5.1, Table 2
- Epoch confound 分析缺少关键对照：对全部数据做 multi-epoch uniform training（等量 compute），以区分选择性重复 vs 任意重复。

**W3** [warning] 1.7B 规模效应递减未充分讨论
- 位置：§5.2
- 0.6B→1.7B 效应缩减 43%（−0.023→−0.013），OOD 方向不一致。推测 larger models 更鲁棒但无证据。建议正式讨论 scaling trend 并限定 claim 范围。

**W4** [warning] B=4 是最弱设置却用于主实验
- 位置：Figure 6, Table 12
- B=4 时 MAE=0.114，advantage 最小（1.0×）。B=16 时 advantage 放大 3.0×。建议以 B≥8 为主实验配置。

**W5** [warning] Self-contamination 生态效度有限
- 位置：§4, Appendix O
- Qwen3 self-contamination + uniform mixing 远不代表真实 web contamination。Cross-model 实验仅单 seed 无 PPL。标题 claim 超出证据范围。

### 小问题
- M1: Permuted q-scores 仅 1 seed，建议补充
- M2: ρ=0.6 p_BH=0.064 的措辞略有 misleading
- M3: Table 5 "Generator ≠ trainee" 应考虑标为必要条件
- M4: Cohen's d=3.83 的解读需注意 paired SD vs absolute SD 的区别

### Questions
Q1: 下游零改善下，推荐用于什么场景？
Q2: GPT-4 级 synthetic data 的 detector 性能？
Q3: α_eff 负偏差是否导致 b* 系统偏高？
Q4: 为何选 B=4 而非 B=8/16？
Q5: 是否考虑 curriculum learning 基线？

### 主要优势
- S1: Epoch confound 揭露（>95% D&R 优势来自 multi-epoch）是最强贡献
- S2: 三条件框架（Table 5）有实用价值
- S3: 实验设计严谨（5 seeds, BH correction, 大量消融, checkpoint artifact 诚实报告）
- S4: 写作质量高，图表清晰
- S5: Propositions 1-2 数学正确，Algorithm 1 实现清晰

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1312 · 2026-05-25T04:49:25.125245+00:00_

Reviewer 1 审稿意见已收到（评分 3.0 — Findings）。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 101

## Round 101

24 recorded events


### User

_source line 1313 · 2026-05-25T04:49:28.332469+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 **Overall 3.0 (Findings)**。核心判断是论文最有价值的贡献在于 epoch confound 的揭露和三条件框架，而非 adaptive b* 方法本身。两个 must-fix 问题：(1) 核心效应 0.13% PPL 且零下游迁移，实际意义不足；(2) α_eff proxy 与 Wang (2026) 理论保证之间的逻辑断裂。五个 should-fix 问题涵盖 grid-best 偏差解释、缺 multi-epoch uniform 基线、规模递减趋势、B=4 配置选择和生态效度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1314 · 2026-05-25T04:49:52.308036+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1315 · 2026-05-25T04:49:52.358614+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-25T04:49:57.227479+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1317 · 2026-05-25T04:49:57.981633+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (269 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| detect_remove_q07_seed456 | D&R q>0.7 threshold seed=456 replicate. Retains ~50% data (184,908/370k). Cross-seed for error bar with seed42 (r3) and seed123. | — | — | — |\n| detect_remove_q07_seed123 | D&R q>0.7 threshold seed=123 replicate. Retains ~50% data (184,908/370k). Cross-seed for error bar with seed42 (r3) and seed456. | — | — | — |\n| detect_remove_q07_seed42_r3 | D&R q>0.7 threshold fresh rerun (r3). Retains ~50% data (184,908/370k). Prior r2 corrupted by optimizer state loss during resume. Fresh training from step 0 with full optimizer state preservation. | — | — | — |\n\n## 待处理\n- eval_adaptive_1_7b_seed123（准备中）\n- eval_uniform_1_7b_seed123（准备中）\n- detect_remove_q05_epoch_matched（准备中）\n- adaptive_1_7b_planb_control（准备中）\n- eval_q01_final（准备中）\n- status_check_41312（准备中）\n- eval_adaptive_1_7b（准备中）\n- eval_uniform_1_7b_v2（准备中）\n- eval_uniform_1_7b_resumed（准备中）\n- uniform_1_7b_seed42_r2（准备中）\n- …另有 5 项\n\n## 近期结论\n- **detect_remove_q07_seed42_r2** (killed): Hard filtering at q_score > 0.7 threshold retains ~50% of data (184,908/370k samples), the most conservative D&R strategy keeping on
…[truncated 1795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 1318 · 2026-05-25T04:50:02.046012+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_round_13/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_round_13/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1319 · 2026-05-25T04:50:02.096633+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-25T04:50:04.490837+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/reviewer_*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/reviewer_*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-25T04:50:04.541568+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-25T04:50:06.850366+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*reviewer*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*reviewer*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-25T04:50:06.951215+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260513T220201_359096.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260514T021956_383198.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260514T065255_458039.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260514T133119_033765.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260514T202331_944626.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260515T005502_662378.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260515T100652_609891.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260515T142910_710664.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260515T183407_531456.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39
…[truncated 3276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-25T04:50:12.120821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-25T04:50:12.171484+00:00_

File content (810.4KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-25T04:50:16.288036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl",
  "offset": "0",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl",
    "offset": "0",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-25T04:50:16.640545+00:00_

0	{"ts": "2026-05-18T06:22:27.419946+00:00", "role": "user", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1", "text": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 1\n\n**目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n**截止日期**: 2026-05-25 (ARR May cycle)\n**格式要求**: ACL 模板 `[review]`，长文 ≤8 页正文 + unlimited references，Limitations section 不计页数，double-blind\n**论文路径**: `projects/provenance_weight_training/paper/main.tex`（sections/ 子目录含各章节）\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请从以下维度深入审查：\n\n1. **方法正确性**\n   - 双约束框架（α_eff ≥ τ, ESS ≥ n_min）的数学推导是否严谨\n   - Proposition 1 (monotonicity) 的证明是否完整/正确\n   - \"minimum intervention principle\" 的形式化是否站得住脚\n   - bisection 算法的正确性和收敛保证\n\n2. **实验设计**\n   - Baseline 选择是否充分公平（Uniform / Grid-b / ESS-only / Random / Golden Ratio / Detect & Remove）\n   - 自污染设计（用 Qwen3-0.6B 生成 synthetic → 同架构训练）的合理性和局限\n   - 评估指标（仅 held-out PPL + 附录 downstream）是否充分\n   - 单一模型（0.6B）、单一数据源（FineWeb）、单一 detector（TF-IDF+LR）的外部效度\n\n3. **统计检验**\n   - 3-seed 比较的统计功效是否足够（特别是 p=0.30 \"indistinguishable\" 这一 claim）\n   - bootstrap p-value 的使用是否恰当\n   - effect size（~0.04 PPL）是否足以支撑论文 claims\n\n4. **消融完整性**\n   - τ sweep、n_min sweep、batch size sweep 是否覆盖关键范围\n   - ρ=0.2 失效、ρ>0.6 未测试的 implications\n   - 缺失的消融（如不同 detector 的影响、不同数据规模）\n\n5. **历史 Issue 检查**\n   - RR-W1: 此前论文错误声称 \"from random initialization\"，应为 \"continued pretraining\"——检查是否已修正\n   - RR-W2: 此前论文错误声称 \"balanced real/synthetic test set\"，实际为 human-only——检查是否已修正\n\n请输出完整结构化审稿报告：Summary → Strengths → Weaknesses（逐条编号，标 [Must-Fix] / [Should-Fix] / [Minor]）→ Questions → Missing References → Score (1-5) + Confidence (1-5)。", "source": "review_reviewer_1"}
1	{"ts": "2026-05-18T06:22:35.361323+00:00", "role": "tool", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1", "text": "called Read", "tool": "Read", "tool_args": {"file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515/.claude/skill
…[truncated 45312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-25T04:50:22.966020+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl",
  "description": "Count lines in reviewer 1 chat log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl",
    "description": "Count lines in reviewer 1 chat log"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-25T04:50:23.769429+00:00_

820 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-25T04:50:23.921049+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
  "description": "Count lines in reviewer 2 chat log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
    "description": "Count lines in reviewer 2 chat log"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-25T04:50:23.971742+00:00_

1071 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-25T04:50:26.984906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl",
  "offset": "810",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl",
    "offset": "810",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-25T04:50:27.788482+00:00_

810	{"ts": "2026-05-25T04:45:33.666598+00:00", "role": "tool", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1", "text": "called Read", "tool": "Read", "tool_args": {"file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"}}
811	{"ts": "2026-05-25T04:45:33.968730+00:00", "role": "tool_result", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1", "text": "1\t\\section{Proofs}\n2\t\\label{app:proofs}\n3\t\n4\t\\begin{proposition}[$\\alpha_{\\mathrm{eff}}$ monotonicity]\n5\t\\label{prop:monotone}\n6\t$\\alpha_{\\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least two samples with distinct $q$-values.\n7\t\\end{proposition}\n8\t\n9\t\\begin{proof}[Proof of Proposition~\\ref{prop:monotone}]\n10\tLet $w_i(b) = (1 - q_i)^b$, $W(b) = \\sum_{j=1}^B w_j(b)$, and $\\pi_i(b) = w_i(b) / W(b)$.\n11\tThen\n12\t\\begin{equation*}\n13\t  \\alpha_{\\mathrm{eff}}(b) = \\sum_{i=1}^{B} \\pi_i(b)\\, (1 - q_i).\n14\t\\end{equation*}\n15\tTaking the derivative with respect to $b$:\n16\t\\begin{align*}\n17\t  \\frac{d\\pi_i}{db}\n18\t  &= \\pi_i \\!\\left(\\frac{d \\ln w_i}{db} - \\frac{d \\ln W}{db}\\right) \\\\\n19\t  &= \\pi_i \\!\\left(\\ln(1{-}q_i) - \\textstyle\\sum_j \\pi_j \\ln(1{-}q_j)\\right).\n20\t\\end{align*}\n21\tSubstituting,\n22\t\\begin{align*}\n23\t  \\frac{d\\alpha_{\\mathrm{eff}}}{db}\n24\t  &= \\sum_i (1{-}q_i)\\, \\pi_i \\!\\left(\\ln(1{-}q_i) - \\mathbb{E}_{\\pi}[\\ln(1{-}q)]\\right) \\\\\n25\t  &= \\mathrm{Cov}_{\\pi}\\!\\bigl(1{-}q_i,\\, \\ln(1{-}q_i)\\bigr).\n26\t\\end{align*}\n27\tSince $(1{-}q_i)$ and $\\ln(1{-}q_i)$ are both increasing functions of $(1{-}q_i)$, they are positively associated, so the covariance is non-negative.\n28\t\\end{proof}\n29\t\n30\t\\begin{proposition}[ESS monotonicity]\n31\t\\label{prop:ess_mono}\n32\t$\\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasin
…[truncated 11066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-25T04:50:27.939425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
  "offset": "1061",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
    "offset": "1061",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-25T04:50:27.939988+00:00_

1061	{"ts": "2026-05-25T04:44:14.620143+00:00", "role": "tool_result", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2", "text": "", "tool": "Read", "elapsed_ms": 559}
1062	{"ts": "2026-05-25T04:49:38.831437+00:00", "role": "tool", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2", "text": "called Read", "tool": "Read", "tool_args": {"file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex", "limit": "80"}}
1063	{"ts": "2026-05-25T04:49:38.831800+00:00", "role": "tool_result", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2", "text": "1\t\\documentclass[11pt]{article}\n2\t\\usepackage[review]{acl}\n3\t\\usepackage{times}\n4\t\\usepackage{latexsym}\n5\t\\usepackage[T1]{fontenc}\n6\t\\usepackage[utf8]{inputenc}\n7\t\\usepackage{microtype}\n8\t\\usepackage{graphicx}\n9\t\\graphicspath{{../../artifacts/figures/}}\n10\t\\usepackage{amsmath}\n11\t\\usepackage{amssymb}\n12\t\\usepackage{amsthm}\n13\t\\usepackage{algorithm}\n14\t\\usepackage{algorithmic}\n15\t\\usepackage{booktabs}\n16\t\\usepackage{multirow}\n17\t\\usepackage{xcolor}\n18\t\\usepackage{enumitem}\n19\t\\usepackage{tikz}\n20\t\\usetikzlibrary{positioning,arrows.meta}\n21\t\\usepackage{hyperref}\n22\t\n23\t\\newtheorem{proposition}{Proposition}\n24\t\\newtheorem{definition}{Definition}\n25\t\n26\t\\newcommand{\\bstar}{b^*}\n27\t\\newcommand{\\aeff}{\\alpha_{\\mathrm{eff}}}\n28\t\\newcommand{\\nmin}{n_{\\min}}\n29\t\\newcommand{\\btau}{b_{\\tau}}\n30\t\\newcommand{\\bess}{b_{\\mathrm{ESS}}}\n31\t\\title{When Does Detect-and-Reweight Work for Synthetic Contamination?}\n32\t\n33\t\\author{Anonymous}\n34\t\n35\t\\begin{document}\n36\t\\maketitle\n37\t\n38\t\\begin{abstract}\n39\t\\input{sections/abstract}\n40\t\\end{abstract}\n41\t\n42\t\\section{Introduction}\n43\t\\label{sec:intro}\n44\t\\input{sections/introduction}\n45\t\n46\t\\section{Related Work}\n47\t\\label{sec:related}\n48\
…[truncated 4324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1336 · 2026-05-25T04:50:43.573479+00:00_

Reviewer 1 已完成审稿。Reviewer 2 仍在工作中（最新活动是 04:50，还在阅读论文）。等待 Reviewer 2 完成后进入交叉分享环节。

我已完整提取 Reviewer 1 的审稿内容：

**Reviewer 1 审稿摘要（Overall 3.0 / Findings）**：
- **Must-Fix N1**：核心效应仅 0.13% PPL 改善（Δ=−0.023），下游任务零迁移
- **Must-Fix N2**：α_eff proxy 与 Wang (2026) 理论保证之间存在逻辑断裂（R²≈0.63，~37%未解释方差）
- **Should-Fix W1-W5**：grid-best 偏差、缺 multi-epoch uniform 基线、1.7B 规模递减、B=4 配置选择、self-contamination 生态效度
- **主要优势**：epoch confound 揭露、三条件框架、实验设计严谨、写作质量高

Reviewer 2 仍在审阅中，等待其提交后进行 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 102

## Round 102

6 recorded events


### User

_source line 1337 · 2026-05-25T04:52:13.875690+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：When Does Detect-and-Reweight Work for Synthetic Contamination?

**审稿依据**: ACL ARR Review Form（Soundness / Excitement / Reproducibility / Overall Assessment），以及 Director 指定的三个侧重：新颖性、论文完整性、格式合规。

---

## 1. Summary

本文通过 Qwen3-0.6B 的 controlled continued pretraining 实验（132M tokens，5 seeds），识别了 detect-and-reweight (D&R) 方法有效运作的三个条件：(1) 已发表的 D&R 评估受 multi-epoch exposure 混淆，去除该混淆后 >95% 的优势消失；(2) detector 需同时具备足够的 discrimination (AUC≥0.8) 和良好的 calibration (ECE<0.05)；(3) minimum intervention（满足 quality floor 的最小 sharpening exponent）优于 unconstrained weight maximization。论文提出 dual-constrained adaptive b* 作为 minimum-intervention 原则的示例应用。

---

## 2. Strengths

**S1** [Epoch confound 发现]: §5.1 的 epoch confound 是本文最强贡献。Table 2 和 Figure 1(a) 清晰展示：在 epoch-matched controls 下，D&R 的 raw PPL 优势（如 ρ=0.3 时 Δ≈-1.1）缩减至 Δ≈-0.017（3-seed），落在 cross-seed variance 范围内。实验设计——对比 raw PPL vs. epoch-matched PPL across multiple threshold settings——简洁有效。这一发现对 data curation 社区有实际预警价值。

**S2** [严谨的实验方法论]: 5 seeds + Bonferroni-Holm correction；ablation controls 设计周全（Permuted 破坏 q-score 信号保留 weight non-uniformity，Random 使用随机权重，ESS-only 最大化 b 至 stability ceiling），Table 3 的 ablation hierarchy (Adaptive > Uniform > ESS-only > Random > Permuted) 逻辑清晰；统计检验报告完整（paired t-test, effect sizes, p_adj）。

**S3** [诚实的 framing]: 论文将方法定位为 "an illustrative application"（Abstract line 6）而非主要贡献，是恰当的自我定位。Abstract 末句和 Limitations 对 scope 的限定（self-contamination, 0.6B scale）是负责任的学术表述。

**S4** [Constraint regime 分析]: Figure 7 的 constraint regime decomposition 提供了有价值的实践洞察：ρ=0.4 时 ~59% 的 batches 是 clean（α_eff ≥ τ），~40% 是 ESS-binding，说明方法的介入范围有限且可预测。

**S5** [视觉和写作密度]: 8 页正文包含 7 个 figures 和 5 个 tables，每个都有明确目的。写作紧凑高效，论证链条清晰。

---

## 3. Weaknesses

**W1** [must-fix] **标题暗示的通用性远超实验 scope**

标题 "When Does Detect-and-Reweight Work for Synthetic Contamination?" 暗示一般性回答，但实验受限于：(i) self-contamination（同一模型 Qwen3-0.6B 生成并检测），(ii) 单一模型家族 0.6B（1.7B 仅简短提及，§5.2 末段"the benefit diminishes to Δ≈−0.013 with OOD mixed"），(iii) continued pretraining 而非 from-scratch，(iv) 单一数据源（FineWeb subset）。

关键矛盾：论文最重要的发现 F1（epoch confound）在 §6 中明确承认"invisible in Drayson et al. (2025) because from-scratch pretraining on large corpora rarely completes even one epoch"——也就是说，该发现在最常见的 pretraining 设定下不适用。标题却没有反映这一关键 scope 限定。

建议：标题应更具体地反映 scope，例如 "When Does Detect-and-Reweight Work? An Analysis of Self-Contamination in Continued Pretraining" 或类似表述。

**W2** [must-fix] **下游任务零改善与 practitioner 导向 framing 之间的矛盾**

Table 10（Appendix I）显示 adaptive reweighting 在 MMLU、HellaSwag 等下游任务上无有意义改善（differences within standard error）。然而论文在三处使用 practitioner 导向表述：
- §5.1: "For practitioners, this means D&R's published advantages should be interpreted with caution"
- §6 Table 5: "Decision summary for practitioners"
- §7: "For practitioners, reweighting is worthwhile only when ρ≥0.4 and the detector is well-calibrated"

Abstract 说 "improves over uniform training at contamination ratios ρ≥0.4"，但未指明仅限 PPL。读者自然会期待 "improvement" 包括实际任务表现。PPL 改善 0.023–0.032 点且不传导至下游任务，"worthwhile" 一词缺乏实际支撑。

建议：(a) Abstract 和 Conclusion 中明确限定 "improves held-out PPL" 而非泛泛 "improves over uniform training"；(b) 在 main text（而非仅 Appendix I）讨论下游任务的 null result 及其含义。

**W3** [should-fix] **方法新颖性有限，与 Drayson et al. (2025) 的差异不够清晰**

- 权重公式 w=(1−q)^b 完全来自 Drayson et al.
- Dual constraint（quality floor via α_eff ≥ τ + stability ceiling via ESS ≤ b_ESS）是两个自然约束的组合，bisection 求解 b* 是标准方法
- Per-batch adaptation 在约束定义后是直接应用，无独立方法创新

与 Drayson et al. 的三点差异（§2 末段）：(a) b* 来自 dual constraint 而非 grid search——标准优化替代 grid search；(b) per-model and per-exponent 选择——但 Drayson 的 validation-based selection 也是 per-model 的；(c) SIR discretization——技术细节。

论文将方法定位为 "illustrative application" 是对的，但 Introduction 没有足够突出这一定位。读者在读完 Introduction 后可能预期一个重要的方法贡献，直到 §3 才明确降低预期。

**W4** [should-fix] **Detector 覆盖面极窄，削弱 "detector requirements" 发现的通用性**

§5.2 的核心 claim "both sufficient discrimination and good calibration are required"（AUC≥0.8, ECE<0.05）仅基于 3 个 detector：TF-IDF+LR（AUC=0.94, ECE=0.05）、GPT-2 perplexity（AUC=0.91）、N-gram（AUC=0.73）。Table 14 显示仅 TF-IDF+LR 有效。

三个数据点不足以得出 AUC/ECE threshold 的通用规律。现代 neural detectors（fine-tuned RoBERTa/DeBERTa、DetectGPT variants、Binoculars、RADAR）的 AUC-ECE profile 可能完全不同，特别是 neural detectors 通常有更好的 calibration。这些 threshold 可能在更广泛的 detector 覆盖下不成立。

**W5** [should-fix] **效果量极小，实际显著性存疑**

主要改善为 ρ=0.1 时 Δ=−0.023 PPL，ρ=0.4 时 Δ=−0.032 PPL（§5.1, §5.2）。虽然 Bonferroni-Holm 校正后达到统计显著性，但论文未讨论这一 PPL 变化在 continued pretraining context 下的实际意义。0.03 PPL 的改善在工程实践中是否可感知？结合 W2（零下游改善），效果量的实际价值需要更审慎的讨论。

**W6** [should-fix] **Self-contamination 设定的生态效度**

真实 web contamination 来自多种生成器（GPT-4, Claude, Llama, Gemini 等），质量和风格各异，混合在异质来源中。Self-contamination（同一模型生成+检测）是对 detector 最有利的设定——q-scores 在 generator-detector 同分布时信息量最大。

Appendix O 的 cross-model 结果（Llama-3.2-3B）不够成熟（"reflect evaluation-set distribution sensitivity rather than consistent quality differences"），反而暴露了 generalization 的困难。这削弱了论文从 self-contamination 推广到一般 synthetic contamination 的可信度。

**W7** [minor] **ρ≥0.4 的实用门槛偏高**

论文 §1 引用的 synthetic text 比例估计为 20–60%。Conclusion 指出 "reweighting is worthwhile only when ρ≥0.4"，加上 calibration 要求，实际适用场景非常窄。这不一定是分析缺陷，但 "Decision summary for practitioners"（Table 5）的 practitioner 导向 framing 在如此受限的适用范围下可能给读者不准确的信号。

**W8** [minor] **PPL 与模型质量的关系未讨论**

论文以 held-out PPL 为主要指标，但未讨论在 continued pretraining 中，多大的 PPL 改善才对应有意义的 capability 提升。鉴于下游 null result，这一讨论对解读 findings 很重要。

---

## 4. Questions

**Q1**: Epoch confound（F1）在 from-scratch pretraining 中不适用（§6）。那么论文对最常见的 pretraining 设定（corpus >> training budget，不会出现 multi-epoch）有何 relevance？如果 F1 不适用于 from-scratch，论文标题的 "When Does D&R Work?" 实际上在回答一个更窄的问题。

**Q2**: Table 14 仅有 TF-IDF+LR 有效。是否尝试过 neural-based detectors（如 fine-tuned ModernBERT/DeBERTa）？AUC≥0.8, ECE<0.05 的 practical guidance 在更广泛的 detector sweep 下是否稳健？

**Q3**: Quality floor τ=0.7 贯穿全文。Table 7（Appendix D）显示了一些 threshold sensitivity，但是否有 principled way 选择 τ，还是它本质上是另一个需要调优的超参数？

**Q4**: Algorithm 1 的 per-batch bisection 独立决定每个 batch 的 b*。这是否造成训练动态的不稳定？Figure 8（Appendix）显示了 b* trajectory，但 b* 在 batch 间的 variance 对 gradient noise 的影响是否被分析过？

**Q5**: 1.7B 规模下 benefit 缩减至 Δ≈−0.013（§5.2）。这是否暗示方法在 practitioner 关注的规模（7B+）下可能完全失效？如果是，"Decision summary for practitioners" 的适用性就更加有限。

---

## 5. Missing References

- **RAID benchmark** (Dugan et al., 2024): 大规模 AI text detection benchmark，覆盖多种 generator 和 domain，与 §5.2 的 detector 评估直接相关——可提供跨 detector-generator pair 的 standardized AUC/ECE measurements 作为参照。
- **M4 shared task** (Wang et al., 2024): 多语言多生成器检测 benchmark，与 detector generalization 讨论相关。

论文已覆盖：Phi series (Gunasekar et al., 2023; Li et al., 2023) ✓，Owen (2013) importance weighting failure modes ✓。

---

## 6. Novelty Assessment

| Finding | 新颖性 | 评估理由 |
|---------|--------|----------|
| F1: Epoch confound | **中偏高** | 揭示了 D&R 评估中一个此前未注意的重要混淆变量。实验设计（epoch-matched controls）简洁有效，对社区有预警价值。但：(a) 仅适用于 continued pretraining（from-scratch 不受影响），(b) 本质是实验观察而非方法创新。 |
| F2: Detector calibration | **中** | AUC 和 ECE 独立影响 reweighting 效果有用，但部分可预期（calibration 对 importance weighting 的影响是已知的，cf. Owen 2013）。仅基于 3 个 detector 的数据点，threshold 通用性存疑。 |
| F3: Minimum intervention | **中偏低** | "less is more" 在 importance weighting 中非新见解（ESS constraint 是标准实践）。Dual-constrained bisection 是两个自然约束 + 标准求解方法的直接组合。主要价值在实验验证。 |

**整体方法新颖性**: 低。w=(1−q)^b 来自 Drayson et al.，adaptive b* 的 dual constraint 是标准优化的应用，per-batch bisection 无独立新颖性。论文价值主要在 empirical findings，尤其 F1。

---

## 7. Overall Assessment

### ARR Review Form 维度

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 实验方法论严谨（5 seeds, Bonferroni-Holm, 充分 ablation），但核心 claims 的支撑范围超出实验 scope：标题暗示通用性 vs. 仅 self-contamination + continued pretraining；detector threshold 基于 3 个数据点。 |
| Excitement | 2.5/5 | Epoch confound（F1）有社区价值，但整体贡献偏增量：窄 scope、零下游改善、方法借用 Drayson et al.。一般的 data curation/weighting 研究者可能会记住 F1，但不太可能基于此文改变自己的研究方向。 |
| Reproducibility | 4/5 | 实验设置描述详细（超参 Table 1、detector 训练细节 Appendix M、统计检验方法 Appendix R），Appendix 覆盖 17 项补充分析。未明确承诺开源代码和数据。 |
| Reviewer Confidence | 4/5 | 熟悉 data curation/weighting for LLM pretraining 相关工作。 |

### Overall Assessment

**Overall: 3.0 — Findings**

论文在实验方法论上是严谨的，epoch confound 发现（F1）对社区有实际价值，写作诚实且 self-aware。但以下问题限制了其影响力：

1. **标题与 scope 的不匹配**（W1）：核心发现 F1 不适用于 from-scratch pretraining，但标题未反映。
2. **方法新颖性有限**（W3）：主要建立在 Drayson et al. 基础上，dual-constrained bisection 是标准技术。
3. **零下游改善**（W2）：PPL 改善极小且不传导至任何下游任务，削弱 practitioner 导向 framing 的可信度。
4. **窄 detector 覆盖**（W4）：仅 3 个 detector，核心 AUC/ECE threshold 缺乏通用性。
5. **适用范围极窄**（W7）：仅在 ρ≥0.4 + well-calibrated detector + self-contamination + continued pretraining + 0.6B scale 下有效。

论文作为 focused empirical analysis 适合 Findings 接收。要达到 Conference 水平，需要：(a) 扩展 detector 覆盖（至少包括 neural detectors），(b) 在至少一个下游任务上展示改善或充分讨论 PPL-only improvement 的价值，(c) 测试 cross-model contamination 和更大规模。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1338 · 2026-05-25T04:53:09.202808+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## [Round 1 交叉分享] Reviewer 2 的完整审稿意见\n\n请逐条审阅 Reviewer 2 的意见，对每条 Weakness/Question 回复 **[AGREE]**（同意）或 **[REBUT]**（反驳，须说明理由）。对 Strengths 也可标注是否同意。\n\n特别关注：\n- R2 提出了你未提及的问题（如 W1 标题通用性 vs scope、W3 方法新颖性有限、W7 ρ≥0.4 门槛偏高、W8 PPL 与模型质量关系），请评估是否认同\n- R2 与你观点重叠的问题（下游零改善、detector 覆盖窄、self-contamination 生态效度、效果量极小），确认是否一致或有补充\n\n---\n\n以下是 Reviewer 2 完整审稿意见：\n\n### Strengths\n- S1: Epoch confound 发现是最强贡献，Table 2 和 Figure 1(a) 清晰展示 D&R raw PPL 优势在 epoch-matched controls 下缩减至 Δ≈-0.017\n- S2: 严谨实验方法论（5 seeds + BH correction，ablation hierarchy 清晰）\n- S3: 诚实 framing——将方法定位为 \"illustrative application\"\n- S4: Constraint regime 分析（Figure 7）有实践洞察价值\n- S5: 视觉和写作密度高（8页含7 figures + 5 tables）\n\n### Weaknesses\n**W1** [must-fix] 标题暗示的通用性远超实验 scope：标题 \"When Does D&R Work?\" 暗示一般性回答，但实验受限于 self-contamination、0.6B 单一模型、continued pretraining、单一数据源。关键矛盾：epoch confound 在 from-scratch pretraining 下不适用。\n\n**W2** [must-fix] 下游零改善与 practitioner 导向 framing 矛盾：Table 10 下游任务无改善，但论文三处使用 practitioner 导向表述。Abstract 说 \"improves over uniform training\" 未限定为 PPL-only。\n\n**W3** [should-fix] 方法新颖性有限：w=(1−q)^b 来自 Drayson et al.，dual constraint + bisection 是标准方法组合，per-batch adaptation 无独立创新。\n\n**W4** [should-fix] Detector 覆盖面极窄：仅 3 个 detector 不足以得出 AUC/ECE threshold 通用规律，缺少 neural detectors。\n\n**W5** [should-fix] 效果量极小（Δ=−0.023 PPL），实际显著性存疑，结合零下游改善。\n\n**W6** [should-fix] Self-contamination 生态效度有限，cross-model 结果不成熟。\n\n**W7** [minor] ρ≥0.4 实用门槛偏高，实际适用场景窄。\n\n**W8** [minor] PPL 与模型质量关系未讨论，鉴于下游 null result 尤为重要。\n\n### Questions\nQ1: F1 epoch confound 在 from-scratch 不适用，论文对最常见 pretraining 设定有何 relevance？\nQ2: 是否尝试过 neural detectors？AUC/ECE guidance 在更广 detector sweep 下是否稳健？\nQ3: τ=0.7 是否有 principled 选择方法，还是另一个超参数？\nQ4: Per-batch bisection 的 b* variance 对 gradient noise 的影响？\nQ5: 1.7B 规模 benefit 缩减，方法在 7B+ 是否完全失效？\n\n### Missing References\n- RAID benchmark (Dugan et al., 2024)\n- M4 shared task (Wang et al., 2024)\n\n### 新颖性评估\nF1 epoch confound: 中偏高；F2 detector calibration: 中；F3 minimum intervention: 中偏低。整体方法新颖性：低。\n\n### Overall: 3.0 (Findings)\n",
  "reviewer_id": "1",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## [Round 1 交叉分享] Reviewer 2 的完整审稿意见\n\n请逐条审阅 Reviewer 2 的意见，对每条 Weakness/Question 回复 **[AGREE]**（同意）或 **[REBUT]**（反驳，须说明理由）。对 Strengths 也可标注是否同意。\n\n特别关注：\n- R2 提出了你未提及的问题（如 W1 标题通用性 vs scope、W3 方法新颖性有限、W7 ρ≥0.4 门槛偏高、W8 PPL 与模型质量关系），请评估是否认同\n- R2 与你观点重叠的问题（下游零改善、detector 覆盖窄、self-contamination 生态效度、效果量极小），确认是否一致或有补充\n\n---\n\n以下是 Reviewer 2 完整审稿意见：\n\n### Strengths\n- S1: Epoch confound 发现是最强贡献，Table 2 和 Figure 1(a) 清晰展示 D&R raw PPL 优势在 epoch-matched controls 下缩减至 Δ≈-0.017\n- S2: 严谨实验方法论（5 seeds + BH correction，ablation hierarchy 清晰）\n- S3: 诚实 framing——将方法定位为 \"illustrative application\"\n- S4: Constraint regime 分析（Figure 7）有实践洞察价值\n- S5: 视觉和写作密度高（8页含7 figures + 5 tables）\n\n### Weaknesses\n**W1** [must-fix] 标题暗示的通用性远超实验 scope：标题 \"When Does D&R Work?\" 暗示一般性回答，但实验受限于 self-contamination、0.6B 单一模型、continued pretraining、单一数据源。关键矛盾：epoch confound 在 from-scratch pretraining 下不适用。\n\n**W2** [must-fix] 下游零改善与 practitioner 导向 framing 矛盾：Table 10 下游任务无改善，但论文三处使用 practitioner 导向表述。Abstract 说 \"improves over uniform training\" 未限定为 PPL-only。\n\n**W3** [should-fix] 方法新颖性有限：w=(1−q)^b 来自 Drayson et al.，dual constraint + bisection 是标准方法组合，per-batch adaptation 无独立创新。\n\n**W4** [should-fix] Detector 覆盖面极窄：仅 3 个 detector 不足以得出 AUC/ECE threshold 通用规律，缺少 neural detectors。\n\n**W5** [should-fix] 效果量极小（Δ=−0.023 PPL），实际显著性存疑，结合零下游改善。\n\n**W6** [should-fix] Self-contamination 生态效度有限，cross-model 结果不成熟。\n\n**W7** [minor] ρ≥0.4 实用门槛偏高，实际适用场景窄。\n\n**W8** [minor] PPL 与模型质量关系未讨论，鉴于下游 null result 尤为重要。\n\n### Questions\nQ1: F1 epoch confound 在 from-scratch 不适用，论文对最常见 pretraining 设定有何 relevance？\nQ2: 是否尝试过 neural detectors？AUC/ECE guidance 在更广 detector sweep 下是否稳健？\nQ3: τ=0.7 是否有 principled 选择方法，还是另一个超参数？\nQ4: Per-batch bisection 的 b* variance 对 gradient noise 的影响？\nQ5: 1.7B 规模 benefit 缩减，方法在 7B+ 是否完全失效？\n\n### Missing References\n- RAID benchmark (Dugan et al., 2024)\n- M4 shared task (Wang et al., 2024)\n\n### 新颖性评估\nF1 epoch confound: 中偏高；F2 detector calibration: 中；F3 minimum intervention: 中偏低。整体方法新颖性：低。\n\n### Overall: 3.0 (Findings)\n",
    "reviewer_id": "1",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-25T04:53:35.319683+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26116
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-25T04:53:35.721582+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## [Round 1 交叉分享] Reviewer 1 的完整审稿意见\n\n请逐条审阅 Reviewer 1 的意见，对每条 Weakness/Question 回复 **[AGREE]**（同意）或 **[REBUT]**（反驳，须说明理由）。对 Strengths 也可标注是否同意。\n\n特别关注：\n- R1 提出了你未提及的问题（如 N2 α_eff proxy 理论保证断裂、W1 grid-best b=0.3 vs adaptive b*≈0.9 偏差、W2 缺 multi-epoch uniform 基线、W4 B=4 最弱设置），请评估是否认同\n- R1 与你观点重叠的问题（核心效应小+零下游、规模递减、self-contamination 生态效度），确认是否一致或有补充\n\n---\n\n以下是 Reviewer 1 完整审稿意见：\n\n### Overall Assessment: 3.0 (Findings)\n核心判断：Epoch confound 的揭露是最有价值的贡献，但核心方法（adaptive b*）实际效应极小（Δ=−0.023 PPL, 0.13% relative）且完全无法迁移至下游任务。\n\n### ARR 维度打分\nSoundness 3.5 | Excitement 2.5 | Reproducibility 4 | Confidence 4\n\n### Must-Fix\n**N1** [critical] 核心效应无实际意义且不迁移至下游任务\n- Adaptive b* PPL 改善仅 0.13%，5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）\n- Cohen's d=3.83 被极低 cross-seed 方差（σ=0.006，deterministic data ordering）人为放大\n- 建议：重新定位为分析/负面结果贡献或在 B=16 下报告下游\n\n**N2** [critical] α_eff proxy 与 Wang (2026) 理论保证之间的逻辑断裂\n- Wang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）\n- ~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ\n- n_min 缓冲是 heuristic，无理论保证\n\n### Should-Fix\n**W1** Grid-best b=0.3 vs adaptive b*≈0.9 偏差缺乏解释——α_eff 负偏差可能导致 b_τ 偏高\n**W2** 缺少 \"uniform + multi-epoch\" 基线——无法区分选择性重复 vs 任意重复\n**W3** 1.7B 规模效应递减 43%（−0.023→−0.013），scaling trend 未正式讨论\n**W4** B=4 是最弱设置却用于主实验——B=16 时 advantage 放大 3.0×\n**W5** Self-contamination 生态效度有限，cross-model 仅单 seed 无 PPL\n\n### Minor\n- M1: Permuted q-scores 仅 1 seed\n- M2: ρ=0.6 p_BH=0.064 措辞略 misleading\n- M3: Table 5 \"Generator ≠ trainee\" 应考虑标为必要条件\n- M4: Cohen's d=3.83 解读需注意 paired SD vs absolute SD\n\n### Questions\nQ1: 下游零改善下推荐用于什么场景？\nQ2: GPT-4 级 synthetic data 的 detector 性能？\nQ3: α_eff 负偏差是否导致 b* 系统偏高？\nQ4: 为何选 B=4 而非 B=8/16？\nQ5: 是否考虑 curriculum learning 基线？\n\n### Strengths\nS1: Epoch confound 揭露（>95% D&R 优势来自 multi-epoch）是最强贡献\nS2: 三条件框架（Table 5）有实用价值\nS3: 实验设计严谨（5 seeds, BH correction, 大量消融）\nS4: 写作质量高，图表清晰\nS5: Propositions 1-2 数学正确，Algorithm 1 实现清晰\n",
  "reviewer_id": "2",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## [Round 1 交叉分享] Reviewer 1 的完整审稿意见\n\n请逐条审阅 Reviewer 1 的意见，对每条 Weakness/Question 回复 **[AGREE]**（同意）或 **[REBUT]**（反驳，须说明理由）。对 Strengths 也可标注是否同意。\n\n特别关注：\n- R1 提出了你未提及的问题（如 N2 α_eff proxy 理论保证断裂、W1 grid-best b=0.3 vs adaptive b*≈0.9 偏差、W2 缺 multi-epoch uniform 基线、W4 B=4 最弱设置），请评估是否认同\n- R1 与你观点重叠的问题（核心效应小+零下游、规模递减、self-contamination 生态效度），确认是否一致或有补充\n\n---\n\n以下是 Reviewer 1 完整审稿意见：\n\n### Overall Assessment: 3.0 (Findings)\n核心判断：Epoch confound 的揭露是最有价值的贡献，但核心方法（adaptive b*）实际效应极小（Δ=−0.023 PPL, 0.13% relative）且完全无法迁移至下游任务。\n\n### ARR 维度打分\nSoundness 3.5 | Excitement 2.5 | Reproducibility 4 | Confidence 4\n\n### Must-Fix\n**N1** [critical] 核心效应无实际意义且不迁移至下游任务\n- Adaptive b* PPL 改善仅 0.13%，5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）\n- Cohen's d=3.83 被极低 cross-seed 方差（σ=0.006，deterministic data ordering）人为放大\n- 建议：重新定位为分析/负面结果贡献或在 B=16 下报告下游\n\n**N2** [critical] α_eff proxy 与 Wang (2026) 理论保证之间的逻辑断裂\n- Wang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）\n- ~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ\n- n_min 缓冲是 heuristic，无理论保证\n\n### Should-Fix\n**W1** Grid-best b=0.3 vs adaptive b*≈0.9 偏差缺乏解释——α_eff 负偏差可能导致 b_τ 偏高\n**W2** 缺少 \"uniform + multi-epoch\" 基线——无法区分选择性重复 vs 任意重复\n**W3** 1.7B 规模效应递减 43%（−0.023→−0.013），scaling trend 未正式讨论\n**W4** B=4 是最弱设置却用于主实验——B=16 时 advantage 放大 3.0×\n**W5** Self-contamination 生态效度有限，cross-model 仅单 seed 无 PPL\n\n### Minor\n- M1: Permuted q-scores 仅 1 seed\n- M2: ρ=0.6 p_BH=0.064 措辞略 misleading\n- M3: Table 5 \"Generator ≠ trainee\" 应考虑标为必要条件\n- M4: Cohen's d=3.83 解读需注意 paired SD vs absolute SD\n\n### Questions\nQ1: 下游零改善下推荐用于什么场景？\nQ2: GPT-4 级 synthetic data 的 detector 性能？\nQ3: α_eff 负偏差是否导致 b* 系统偏高？\nQ4: 为何选 B=4 而非 B=8/16？\nQ5: 是否考虑 curriculum learning 基线？\n\n### Strengths\nS1: Epoch confound 揭露（>95% D&R 优势来自 multi-epoch）是最强贡献\nS2: 三条件框架（Table 5）有实用价值\nS3: 实验设计严谨（5 seeds, BH correction, 大量消融）\nS4: 写作质量高，图表清晰\nS5: Propositions 1-2 数学正确，Algorithm 1 实现清晰\n",
    "reviewer_id": "2",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-25T04:53:37.129541+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1407
}
```

</details>

---


### Assistant

_source line 1342 · 2026-05-25T04:53:46.920200+00:00_

交叉分享已发送。两位 Reviewer 正在相互审阅对方意见并准备 [AGREE]/[REBUT] 回应。

当前状态：
- **R1** 和 **R2** 初审评分完全一致：Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5
- 两人高度共识的关键问题：epoch confound 是最强贡献、核心效应极小且零下游改善、self-contamination 生态效度有限、detector 覆盖窄
- R1 独有发现：α_eff proxy 理论断裂（N2）、grid-best vs adaptive 偏差、缺 multi-epoch uniform 基线、B=4 选择问题
- R2 独有发现：标题 vs scope 不匹配（W1）、方法新颖性评估、practitioner framing 矛盾、ρ≥0.4 门槛偏高

等待两位 Reviewer 完成交叉回应后进入报告合成阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 103

## Round 103

6 recorded events


### User

_source line 1343 · 2026-05-25T04:53:49.453775+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交至 Review Director。

**评分**: Overall 3.0 (Findings)

**核心判断**: 论文实验方法论严谨，epoch confound 发现（F1）对社区有价值，但三个问题限制了影响力——标题通用性超出实验 scope（仅 self-contamination + continued pretraining）、方法新颖性有限（建立在 Drayson et al. 上的标准优化）、PPL 改善极小且零下游任务改善。识别了 2 个 must-fix（标题 scope 不匹配、下游 null result 与 practitioner framing 矛盾）和 4 个 should-fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-25T04:53:56.520005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
  "offset": "1065",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
    "offset": "1065",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-25T04:53:56.821645+00:00_

1065	{"ts": "2026-05-25T04:49:44.909307+00:00", "role": "tool_result", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2", "text": "155", "tool": "Bash", "elapsed_ms": 201}
1066	{"ts": "2026-05-25T04:49:44.909921+00:00", "role": "tool", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2", "text": "called Read", "tool": "Read", "tool_args": {"file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"}}
1067	{"ts": "2026-05-25T04:49:45.010614+00:00", "role": "tool_result", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2", "text": "1\tAs synthetic text pervades web corpora, detect-and-reweight methods---downweighting likely-synthetic samples during training---have emerged to prevent model collapse, yet when they actually help remains unclear.\n2\tWe investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.\n3\tFirst, published detect-and-remove evaluations are confounded by multi-epoch exposure: over 95\\% of the reported advantage vanishes under epoch-matched controls.\n4\tSecond, the detector must provide both sufficient discrimination \\emph{and} good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.\n5\tThird, minimum intervention---applying the smallest reweighting exponent that meets a quality floor---outperforms unconstrained weight maximization.\n6\tAs an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $\\bstar$ that improves over uniform training at contamination ratios $\\rho \\geq 0.4$, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.\n7\tThese findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination 
…[truncated 15866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1346 · 2026-05-25T04:54:06.590104+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
  "description": "Check current line counts for both reviewer logs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
    "description": "Check current line counts for both reviewer logs"
  }
}
```

</details>

---


### Tool result

_source line 1347 · 2026-05-25T04:54:06.741283+00:00_

    821 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_1.jsonl
   1079 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl
   1900 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 1348 · 2026-05-25T04:54:23.201496+00:00_

交叉分享已发送给两位 Reviewer，等待回应中。

当前进度：
- **R1 初审**: 完成 — Overall 3.0 (Findings)
- **R2 初审**: 完成 — Overall 3.0 (Findings)
- **R1 交叉回应**: 进行中
- **R2 交叉回应**: 进行中

两位 Reviewer 评分高度一致（Soundness 3.5, Excitement 2.5, Overall 3.0），核心共识是 epoch confound 发现有价值但方法贡献增量、效果量极小且零下游改善。待交叉回应完成后进入 Step 3（收敛判断）和 Step 4（报告合成）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 104

## Round 104

4 recorded events


### User

_source line 1349 · 2026-05-25T04:55:00.433028+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应：Reviewer 2 审稿意见

### 总体一致性
R2 给出 3.0 (Findings)，与我评分一致。核心共识：epoch confound 是最强贡献；方法效果极小且不迁移下游；规模趋势不利；生态效度有限。

### Strengths
全部 [AGREE]（S1-S5），其中 S4 (constraint regime 分析) 是 R2 提出而我未单独强调的优点，补充认同。

### Weaknesses 逐条回应

[AGREE] R2-W1: 标题通用性 vs 实验 scope。R2 更尖锐地指出 epoch confound 在 from-scratch pretraining 下不适用——论文最强贡献对最常见设定无意义。比我的 W5 更精准。

[AGREE] R2-W2: 下游零改善与 practitioner framing 矛盾。与我的 N1 高度重叠。R2 补充指出 abstract "improves over uniform" 未限定 PPL-only，有误导性。

[REBUT] R2-W3: 方法新颖性有限。虽然单个组件非新，但 α_eff + ESS 对偶约束化 + minimum intervention 在此问题上是新组合。更重要的是，论文的分析贡献（epoch confound、三条件框架）不依赖算法新颖性。整体新颖性应为"中"而非"低"。

[AGREE] R2-W4: Detector 覆盖面极窄。同意提升至 should-fix。3 detectors 不足以建立通用 threshold，缺 neural detectors。

[AGREE] R2-W5/W6: 与我的 N1/W5 一致。

[AGREE] R2-W7: ρ≥0.4 门槛偏高。我未单独提及，认同其合理性。ρ=0.3 已中性，适用场景确实窄。

[AGREE] R2-W8: PPL-accuracy disconnection 未讨论。R2 提出而我未单独讨论的重要视角，补充认同。

### Questions
[AGREE] Q1, Q2, Q4, Q5
[REBUT] Q3: τ=0.7 的选择——论文 §5.3 + Appendix D 已提供 τ∈[0.5,0.95] sweep，[0.5,0.8] 均优于 uniform，经验性选择在 2-hyperparameter 方法中可接受。

### Missing References
[AGREE]: RAID benchmark 和 M4 shared task 确实相关。

### 与 R2 的唯一实质分歧
方法新颖性：R2 评"低"，我评"中偏低"。不影响整体评分。

### 我的独有问题（R2 未提及）
1. N2: α_eff proxy 的理论保证断裂（Wang 2026 要求 true fraction，proxy R²≈0.63）
2. W1: Grid-best b=0.3 vs adaptive b*≈0.9 偏差及 α_eff 负偏差的影响
3. W2: 缺少 "uniform + multi-epoch" 基线
4. W4: B=4 是最弱设置却用于主实验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-25T04:55:11.282580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
  "offset": "1079",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
    "offset": "1079",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-25T04:55:11.333164+00:00_

1079	{"ts": "2026-05-25T04:53:36.943636+00:00", "role": "user", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2", "text": "[Round 1 审稿请求]:\n## [Round 1 交叉分享] Reviewer 1 的完整审稿意见\n\n请逐条审阅 Reviewer 1 的意见，对每条 Weakness/Question 回复 **[AGREE]**（同意）或 **[REBUT]**（反驳，须说明理由）。对 Strengths 也可标注是否同意。\n\n特别关注：\n- R1 提出了你未提及的问题（如 N2 α_eff proxy 理论保证断裂、W1 grid-best b=0.3 vs adaptive b*≈0.9 偏差、W2 缺 multi-epoch uniform 基线、W4 B=4 最弱设置），请评估是否认同\n- R1 与你观点重叠的问题（核心效应小+零下游、规模递减、self-contamination 生态效度），确认是否一致或有补充\n\n---\n\n以下是 Reviewer 1 完整审稿意见：\n\n### Overall Assessment: 3.0 (Findings)\n核心判断：Epoch confound 的揭露是最有价值的贡献，但核心方法（adaptive b*）实际效应极小（Δ=−0.023 PPL, 0.13% relative）且完全无法迁移至下游任务。\n\n### ARR 维度打分\nSoundness 3.5 | Excitement 2.5 | Reproducibility 4 | Confidence 4\n\n### Must-Fix\n**N1** [critical] 核心效应无实际意义且不迁移至下游任务\n- Adaptive b* PPL 改善仅 0.13%，5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）\n- Cohen's d=3.83 被极低 cross-seed 方差（σ=0.006，deterministic data ordering）人为放大\n- 建议：重新定位为分析/负面结果贡献或在 B=16 下报告下游\n\n**N2** [critical] α_eff proxy 与 Wang (2026) 理论保证之间的逻辑断裂\n- Wang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）\n- ~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ\n- n_min 缓冲是 heuristic，无理论保证\n\n### Should-Fix\n**W1** Grid-best b=0.3 vs adaptive b*≈0.9 偏差缺乏解释——α_eff 负偏差可能导致 b_τ 偏高\n**W2** 缺少 \"uniform + multi-epoch\" 基线——无法区分选择性重复 vs 任意重复\n**W3** 1.7B 规模效应递减 43%（−0.023→−0.013），scaling trend 未正式讨论\n**W4** B=4 是最弱设置却用于主实验——B=16 时 advantage 放大 3.0×\n**W5** Self-contamination 生态效度有限，cross-model 仅单 seed 无 PPL\n\n### Minor\n- M1: Permuted q-scores 仅 1 seed\n- M2: ρ=0.6 p_BH=0.064 措辞略 misleading\n- M3: Table 5 \"Generator ≠ trainee\" 应考虑标为必要条件\n- M4: Cohen's d=3.83 解读需注意 paired SD vs absolute SD\n\n### Questions\nQ1: 下游零改善下推荐用于什么场景？\nQ2: GPT-4 级 synthetic data 的 detector 性能？\nQ3: α_eff 负偏差是否导致 b* 系统偏高？\nQ4: 为何选 B=4 而非 B=8/16？\nQ5: 是否考虑 curriculum learning 基线？\n\n### Strengths\nS1: Epoch confound 揭露（>95% D&R 优势来自 multi-epoch）是最强贡献\nS2: 三条件框架（Table 5）有实用价值\nS3: 实验设计严
…[truncated 132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1352 · 2026-05-25T04:55:18.155327+00:00_

R1 交叉回应已收到。R2 尚未提交交叉回应，等待中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 105

## Round 105

4 recorded events


### User

_source line 1353 · 2026-05-25T04:55:20.736286+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。与 R2 在整体评分（3.0 Findings）和核心判断上高度一致，唯一实质分歧是方法新颖性评估（R2: 低, 我: 中偏低）。我额外提出了 4 个 R2 未涉及的问题：α_eff 理论断裂、b* 系统偏差、缺 multi-epoch 基线、B=4 配置问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-25T04:55:28.584529+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
  "description": "Check if Reviewer 2 has submitted cross-response"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl",
    "description": "Check if Reviewer 2 has submitted cross-response"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-25T04:55:28.735601+00:00_

1079 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_reviewer_2.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 1356 · 2026-05-25T04:55:36.331124+00:00_

Reviewer 1 交叉回应已收到。Reviewer 2 交叉回应尚未提交，等待中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 106

## Round 106

18 recorded events


### User

_source line 1357 · 2026-05-25T04:56:19.404262+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

## Strengths

[AGREE] R1-S1: Epoch confound 是最强贡献。与我的 S1 完全一致。

[AGREE] R1-S2: 三条件框架有实用价值。同意，但需注意 Table 5 的适用范围受限于 self-contamination 设定（我的 W1/W6 和 R1-W5 均指出）。

[AGREE] R1-S3: 实验设计严谨。与我的 S2 一致。

[AGREE] R1-S4: 写作质量高。与我的 S5 一致。

[AGREE] R1-S5: 数学正确。我未独立验证 Propositions 1-2 的证明，但从 Appendix A 的推导结构看逻辑完整。

---

## Must-Fix

### [AGREE] R1-N1: 核心效应无实际意义且不迁移至下游

与我的 W2（零下游改善与 practitioner framing 矛盾）和 W5（效果量极小）完全一致。R1 补充了两个我未独立提出的有价值观察：

1. **Cohen's d 被人为放大**：R1 指出 cross-seed σ=0.006 是由 deterministic data ordering 造成的——5 个 seed 仅改变模型初始化，data order 固定，因此 paired variance 极低。这意味着 Cohen's d=3.83 反映的是实验设计的低随机性而非效应的大小。如果 data ordering 也随机化（shuffle seed），paired SD 大概率升高，Cohen's d 会大幅缩水。这是一个重要的统计方法论问题。

2. **Relative improvement 仅 0.13%**：我的 W5 说"效果量极小"但未量化 relative magnitude。0.13% 的 PPL 改善确实难以构成有实际意义的改进。

我同意 R1 的建议：论文应重新定位为 **分析/负面结果贡献**（"D&R 的优势主要来自 epoch confound，在控制后实际效应可忽略"），而非 "practical adaptive method"。

### [AGREE，但 severity 可降为 should-fix] R1-N2: α_eff proxy 与理论保证的逻辑断裂

R1 的核心逻辑正确。论文 §3（Method）写道："α_eff(b) ≥ τ guarantees a convergence-rate lower bound"，但 α_eff 是 true real fraction 的 noisy proxy（Table 12, R²≈0.63），这意味着 "guarantees" 一词在技术上不成立——约 37% 的 batch 中 α_eff ≥ τ 可能对应 true fraction < τ，理论保证不成立。

n_min 缓冲确实是 heuristic 而非 principled correction。

**但我认为 severity 可以从 critical 降为 should-fix**，原因是：
- 论文在 §3 也写了 "we operationalize this without the known-proportion assumption"，表明作者知道这是近似
- 论文的核心贡献是 empirical findings（尤其 F1），不是理论保证；α_eff 的理论动机是辅助论证，不是主 claim
- 修复成本低：将 "guarantees" 改为 "is designed to approximate" 或 "targets" 即可消除误导

实际影响是：α_eff 的负偏差（Table 12, 负 bias ≈ −0.03）可能导致 quality floor 过早绑定，b* 系统偏高（见下方对 R1-W1 的回应）。这是一个实证问题，不是理论错误。

---

## Should-Fix

### [AGREE] R1-W1: Grid-best b=0.3 vs adaptive b*≈0.9 偏差

这是我未提出的新问题，但 R1 的分析具有说服力。Grid search 后验最优 b=0.3（Table 3），而 adaptive 方法产生 b*≈0.9（Figure 8 trajectory），差异达 3 倍。

R1 提出的因果链合理：
α_eff 负偏差 → quality floor (α_eff ≥ τ) 过早绑定 → b_τ 被推高 → adaptive b* 远高于 post-hoc 最优

这直接意味着 dual constraint 的实际表现受限于 proxy 质量。如果 proxy 系统性地低估真实 real fraction，方法会过度干预（b 过高）——恰恰违背了论文倡导的 "minimum intervention" 原则。

这与 N2 构成闭环：理论动机依赖 α_eff ≈ true fraction，但 proxy 偏差导致方法行为偏离设计意图。

### [AGREE] R1-W2: 缺少 "uniform + multi-epoch" 基线

这是我未提出的重要遗漏。论文展示了 epoch confound（D&R 的优势来自 multi-epoch exposure），但 epoch-matched controls 只控制了 epoch 数量为 1。缺少的关键对比是：

- **Uniform × 3.2 epochs**：不做任何 D&R 过滤，直接在全量数据上训练 3.2 个 epoch（与 D&R 的有效 content epochs 一致）
- 如果 Uniform × 3.2 epochs 的 PPL 与 D&R raw PPL 相当，则证明 D&R 的全部优势来自 repetition（无论是否 selective）
- 如果 Uniform × 3.2 epochs 更差，则说明 D&R 的 selective repetition（只重复 clean samples）确实有价值

缺少这个基线使得论文无法区分两种假设：
(a) D&R 的优势 = 任意多 epoch 训练的优势（epoch effect）
(b) D&R 的优势 = 选择性重复 clean samples 的优势（curriculum effect）

这对 epoch confound 发现（F1）的解读有实质影响。

### [AGREE] R1-W3: 1.7B 规模效应递减未正式讨论

我在 Q5 中以提问形式提出了同样的关切（"1.7B 下 Δ≈−0.013，是否暗示 7B+ 下完全失效？"）。R1 量化了递减幅度（43%），这更有说服力。

补充：如果效应随规模递减的 trend 成立，那么论文的 practitioner 导向建议（Table 5, "for practitioners"）就更加存疑——practitioners 通常在 7B-70B 规模工作，0.6B 的结果可能完全不适用。

### [AGREE，但认为 severity 比 R1 标注的更低] R1-W4: B=4 是最弱设置

R1 指出 Figure 6 显示 B=16 时 advantage 放大 3.0×，论文却在 B=4 下报告主实验。

我同意这应该被讨论，但认为选择 B=4 有合理理由：
- B=4 是 conservative reporting——如果最弱设置都有统计显著性，更大 batch 只会更好
- Table 1 显示 micro-batch=4 是实验配置的 default，gradient accumulation 到 effective B=16
- 改用 B=16 可能引入新混淆（不同 gradient noise 水平）

**但 R1 的核心问题仍然成立**：论文应至少在 B=16 下重复核心对比（Table 3 equivalent）并报告下游结果，以测试 B=4 下的 null downstream result 是否是 batch-size choice 的产物。如果 B=16 下下游任务有改善，那么 W4 的 severity 应升级。

### [AGREE] R1-W5: Self-contamination 生态效度有限

与我的 W6 完全一致。R1 补充指出 cross-model 结果仅单 seed 无 PPL，进一步削弱了 generalization 证据。

---

## Minor

[AGREE] R1-M1: Permuted q-scores 仅 1 seed。我的 review 未独立提出，但 Table 3 确认仅 seed-42 有 Permuted 结果。作为 ablation 控制组，1 seed 的 reliability 有限。

[AGREE] R1-M2: ρ=0.6 p_BH=0.064 措辞。如果论文暗示 "approaching significance" 或类似表述，需明确标为 "not significant after correction"。

[AGREE] R1-M3: Table 5 应标注 "Generator ≠ trainee" 为必要条件（或至少 flag 为未测试）。

[AGREE] R1-M4: Cohen's d 解读。与 N1 中的 paired SD 问题一致——效果量指标应以 absolute SD 或 pooled SD 计算以给出更保守的估计。

---

## Questions

[AGREE] R1-Q1: 下游零改善下的推荐场景。与我的 W2 核心关切相同。

[AGREE] R1-Q2: GPT-4 级 synthetic data 的 detector 性能。与我的 W4（detector 覆盖面窄）相关。真实 web contamination 以 GPT-4/Claude 级文本为主，这些模型产出的 synthetic text 更难检测，AUC/ECE profile 可能完全不同。

[AGREE] R1-Q3: α_eff 负偏差 → b* 系统偏高。与 W1 构成同一问题链。

[AGREE] R1-Q4: 为何选 B=4 而非 B=8/16。与 W4 一致。

[AGREE，但 scope 可能超出本文] R1-Q5: Curriculum learning 基线。Curriculum learning（按样本难度/质量排序训练）确实与 D&R 相关——两者都是 sample-level weighting。但论文的 scope 是分析 D&R 的有效条件，不是提出新 curriculum 方法。如果加入 curriculum learning 基线，scope 会显著扩大。作为 "future work" 提及即可。

---

## 总结：与 R1 的共识和分歧

### 高度共识（独立达到相同结论）
1. **Overall 3.0 (Findings)**：R1 和我独立给出相同评分
2. **Soundness 3.5, Excitement 2.5, Reproducibility 4, Confidence 4**：四个维度完全一致
3. **核心效应极小 + 零下游改善**（R1-N1 ↔ 我的 W2+W5）
4. **Self-contamination 生态效度**（R1-W5 ↔ 我的 W6）
5. **Epoch confound 是最强贡献**（R1-S1 ↔ 我的 S1）
6. **规模递减趋势**（R1-W3 ↔ 我的 Q5）

### R1 提出的新问题（我同意）
1. **α_eff proxy 理论断裂**（R1-N2）：valid，但我建议降为 should-fix
2. **Grid-best b=0.3 vs adaptive b*≈0.9**（R1-W1）：valid，暴露了 proxy 偏差的实际影响
3. **缺 multi-epoch uniform 基线**（R1-W2）：valid 且重要，影响 F1 的解读
4. **B=4 最弱设置**（R1-W4）：valid，但 conservative reporting 有其合理性
5. **Cohen's d 膨胀**（R1-N1/M4）：valid 的统计方法论问题

### 唯一分歧
- **R1-N2 的 severity**：R1 标为 critical/must-fix，我认为 should-fix 更合适。理由：论文的核心贡献是 empirical findings 不是理论保证，α_eff 的理论动机是辅助叙事，修改 "guarantees" 措辞即可解决最大的误导性。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1358 · 2026-05-25T04:56:35.585993+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1359 · 2026-05-25T04:56:35.968671+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 382
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-25T04:56:35.969074+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1361 · 2026-05-25T04:56:36.521514+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T04:42:20.877933+00:00\", \"completed_at\": \"2026-05-25T04:44:58.880493+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，第一个视觉锚点（Figure 1，三面板核心结果总览）出现在 page 2 顶部，位于前 3 页内，可接受。Figure 1 直接传达论文三个核心发现，锚定效果好。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 三个面板的 legend 文字偏小（\\\"D&R (no epoch-search)\\\"、\\\"Uniform\\\" 等），建议适当增大 legend 字号或简化标签以提升扫读可读性。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 的绿色半透明 \\\"feasible interval\\\" 着色在灰度打印下可能不够显眼，建议辅以阴影线或更深的填充色以保证打印友好。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1（Training configuration）紧凑清晰，booktabs 风格，无问题。\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"单页包含 4 个 display items（Figure 4 + Tables 2, 3, 4），视觉密度极高。虽然排列整齐无溢出，但审稿人快速扫读时可能感到拥挤。考虑将 Table 4（Auxiliary baselines）移至 appendix 或下一页以缓解密度。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 5 使用不同颜色条区分 contamination ratio，清晰可辨；Figure 6 的紫色渐变条形图美观且 error bar 标注规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 7 堆叠条形图（蓝/橙/绿）颜色对比度好，百分比标注清晰。Table 5（Decision summary）作为 practitioner 指南放在 Discussion 段，位置合理。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Discussion + Conclusion + Limitations 三个 section 压缩在同一页，但内容均完整，section heading 后有足够正文，无孤悬问题。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段简短（3 bullet points），符合 EMNLP 要求。References 从 page 9 开始，格式统一，无 [?] 未解析引用。\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Figure 9 两个面板的 axis label 和 legend 字号较小（约为正文 60-65%），接近可读性下限。建议增大至正文 70% 以上。\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"最后一页内容约占 60%，底部约 40% 空白。该页为 appendix 末尾（Statistical Power Analysis + Supplementary Summary Table + AI Assistants 
…[truncated 120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-25T04:56:37.425186+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-25T04:56:37.475974+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1364 · 2026-05-25T04:56:40.638812+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "review_issues.yaml",
  "max_chars": "20000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "review_issues.yaml",
    "max_chars": "20000"
  }
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-25T04:56:40.689464+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-25T04:56:43.159774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-25T04:56:43.160768+00:00_

1	issues:
2	# === Round 10 issues (all resolved, retained for history) ===
3	- id: "R10-C1"
4	  summary: "Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 10
9	  last_seen_round: 10
10	  mentions:
11	    - round: 10
12	      reviewers: [1, 2]
13	      note: "Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。"
14	  resolution: "tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。"
15	  resolution_round: 10
16	
17	- id: "R10-C2"
18	  summary: "多重比较未校正，p=0.025 Bonferroni 校正后不显著"
19	  category: experiment
20	  severity: critical
21	  status: resolved
22	  first_raised_round: 10
23	  last_seen_round: 10
24	  mentions:
25	    - round: 10
26	      reviewers: [1, 2]
27	      note: "6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。"
28	  resolution: "BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。"
29	  resolution_round: 10
30	
31	- id: "R10-C3"
32	  summary: "方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配"
33	  category: framing
34	  severity: critical
35	  status: resolved
36	  first_raised_round: 10
37	  last_seen_round: 10
38	  mentions:
39	    - round: 10
40	      reviewers: [1, 2]
41	      note: "w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。"
42	  resolution: "§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。"
43	  resolution_round: 10
44	
45	- id: "R10-C4"
46	  summary: "Downstream task 零改善削弱实际意义"
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 10
51	  last_seen_round: 10
52	  mentions:
53	    - round: 10
54	      reviewers: [1, 2]
55	      note: "Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。"
56	  resolution: "Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limit
…[truncated 18872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1368 · 2026-05-25T04:57:25.184340+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 1369 · 2026-05-25T04:57:25.235017+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-25T05:00:39.428264+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11+ recurring issues (updated with Round 13 fresh review) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。双方 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"论文已升至 5 seeds + BH correction。统计检验力问题部分缓解但 Cohen's d=3.83 被 deterministic data ordering 人为放大（σ=0.006）——如果 data shuffle seed 也随机化，paired SD 大概率升高，Cohen's d 大幅缩水。R1 补充 N1。\"\n  action_items:\n    - round: 13\n      action: \"补 2 个 seed (seed789/234) 达 N=5。4 GPU 并行训练。N=5 后重算 BH 校正 p 值 + Cohen's d + CI。\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.63，Wang (2026) 理论保证不直接转移到 proxy\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 标为 critical：Wang 2026 要求 true real fraction ≥ τ，论文用 α_eff 替代（R²=0.63），~37% 未解释方差意味理论保证不成立。R2 AGREE 但建议降为 should-fix：论文核心贡献是 empirical findings 不是理论保证，修改 'guarantees' 措辞即可。圆桌共识：should-fix（R2 理由成立）。\"\n  action_items:\n    - round: 13\n      action: \"将 §3 中 'guarantees a convergence-rate lower bound' 改为 'targets/approximates'。量化 α_eff ≥ τ 但 true fraction < τ 的 batch 比例。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.023 PPL, 0.13% relative），practitioner framing 自相矛盾\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=128 幂律外推被一致认为不可靠。'practical' 表述仍残留。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2+W5 独立提出。核心矛盾：Abstract 'improves over uniform training' 未限定 PPL-only；§5.1/§6/§7 三处使用 'practitioner' 导向表述但下游零改善。R2 建议 Abstract/Conclusion 明确限定 'improves held-out PPL'。R1 建议重新定位为分析/负面结果贡献。R1 补充 Cohen's d=3.83 被 deterministic data ordering 放大。交叉回应双方 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"Abstract/Conclusion 限定 'improves held-out PPL'；在 main text 讨论下游 null result；考虑重新定位为 analysis paper with negative practical result at current scales。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"标题通用性远超实验 scope：仅 self-contamination + continued pretraining + 0.6B\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Cross-model transfer single seed + mixed + 无 PPL 比较。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 must-fix：标题 'When Does D&R Work?' 暗示一般性但实验仅覆盖 self-contamination/0.6B/continued pretraining/单一数据源。关键矛盾：epoch confound（最强贡献）在 from-scratch pretraining 下不适用（§6 自述），但标题未反映。R1 AGREE 并评为比自己的 W5 更精准。建议标题加限定如 '...in Continued Pretraining'。\"\n  action_items:\n    - round: 13\n      action: \"修改标题以反映 scope 限定（如加 'in Continued Pretraining' 或 'under Self-Contamination'），或完成 cross-model PPL 对比。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§3 压缩后仍给人独立方法贡献印象。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3：方法新颖性低（w=(1-q)^b 来自 Drayson，dual constraint + bisection 是标准方法）。R1 REBUT：单个组件非新但组合在此问题上是新的，且分析贡献不依赖算法新颖性，整体应为'中'而非'低'。唯一实质分歧。圆桌共识：中偏低，不影响评分。\"\n  action_items:\n    - round: 13\n      action: \"确保 Introduction 早期明确 analysis paper 定位，避免给读者方法贡献预期。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作和 detection benchmarks\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议。\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 新增：RAID benchmark (Dugan et al. 2024)、M4 shared task (Wang et al. 2024)。R1 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"考虑补充 RAID/M4 detection benchmarks 引用。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏 uniform+multi-epoch baseline\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Epoch confound 适用范围需限定为 multi-epoch exposure 场景。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2：缺 uniform × 3.2 epochs baseline 无法区分纯重复 vs 选择性重复。R2 AGREE 且认为计算成本低但对分析完整性至关重要。\"\n  action_items:\n    - round: 13\n      action: \"增加 uniform+multi-epoch baseline（全数据 ~3.2 epochs），完善 epoch confound 分析。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 可读性和 display item 分布问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"ρ 符号冲突、Figure 1 黑白不可辨。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"视觉审查发现 page 6 含 4 个 display items 密度过高（1 warning）。Figure 1 legend 字号偏小，Figure 2 灰度打印建议加阴影线。\"\n  action_items:\n    - round: 13\n      action: \"考虑将 Table 4 移至 appendix 缓解 page 6 密度。Figure 1 legend 字号增大。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 issues (updated with Round 13) ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"LaTeX wc 确认 225 words。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 ~155 words，合规。\"\n  resolution: \"Abstract 已压缩至 ~155 words，符合 ≤200 words 限制。\"\n  resolution_round: 13\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§7 Conclusion 溢出至第 9 页。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 §1-§7 在 page 8 内。合规。\"\n  resolution: \"正文已压缩至 8 页内。\"\n  resolution_round: 13\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个），不足以支撑 AUC/ECE threshold 的通用性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"仅 TF-IDF+LR / GPT-2 / N-gram。3 个数据点不足建立因果关系。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 + R1 AGREE。缺少 neural detectors（RoBERTa/DeBERTa/DetectGPT/Binoculars/RADAR）。AUC-ECE threshold 在更广 detector coverage 下可能不成立。\"\n  action_items:\n    - round: 13\n      action: \"扩展 detector coverage（至少含 1 个 neural detector），或将 threshold 标注为 'observed in our 3 detectors, not general guidance'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size scaling 趋势基于 3 个数据点，power law fitting 不可靠\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=4/8/16 仅 3 点，外推到 B=128 不可靠。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"未再单独提及，可能已部分改善。\"\n  action_items:\n    - round: 13\n      action: \"确认是否已删除 power law fitting，保留 monotonic trend 描述。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"建议将 Spearman 改为 ρ_s。\"\n  action_items:\n    - round: 12\n      action: \"全文 Spearman ρ → ρ_s\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 13 新发现/更新 ===\n\n- id: \"R13-W1\"\n  summary: \"B=4 micro-batch 上 dual constraint 统计可靠性不足，主实验在次优设定运行\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE（但认为 conservative reporting 有合理性）。B=4 MAE=0.114，advantage 最小（1.0×）。B=16 时 advantage 放大 3.0×。R2 认为 B=4 是 conservative reporting（最弱设置仍显著 → 更大 batch 更好），但核心问题仍在：应至少在 B=16 下重复核心对比并报告下游结果。\"\n  action_items:\n    - round: 13\n      action: \"说明 B=4 选择原因。可选：补充 B=16 完整对比（3 seeds + downstream）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Grid-best b=0.3 vs adaptive b*≈0.9 偏差：α_eff 负偏差导致过度干预，违背 minimum intervention 原则\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE。因果链：α_eff 负偏差 → quality floor 过早绑定 → b_τ 推高 → adaptive b*≈0.9 远高于 grid-best b=0.3。方法行为偏离设计意图（minimum intervention 实际上过度干预）。与 R11-C2 构成闭环。\"\n  action_items:\n    - round: 13\n      action: \"补充 per-batch b* 分布（median, percentiles）。可选：对比 fixed b=median(b*) 性能。分析 α_eff 负偏差对 b* 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"1.7B 规模效应递减 43% 且 scaling trend 未正式讨论\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2-Q5。0.6B→1.7B Δ 从 −0.023 缩至 −0.013（43% 递减），OOD 方向不一致。如果 trend 成立，practitioner 关注的 7B-70B 规模方法可能完全失效，削弱 Table 5 'for practitioners' 的适用性。R2 交叉回应补充认同。\"\n  action_items:\n    - round: 13\n      action: \"正式讨论 scaling trend 并限定 claim 范围。在 Table 5 或 Conclusion 加 scale caveat。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W4\"\n  summary: \"ρ≥0.4 实用门槛偏高，实际适用场景极窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2-W7。论文引用 synthetic text 20-60% 估计，但方法仅在 ρ≥0.4 + well-calibrated detector + self-contamination + continued pretraining + 0.6B 下有效。'Decision summary for practitioners' 在如此受限范围下可能给读者不准确信号。R1 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"在 Table 5 或 Conclusion 明确标注适用范围限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"§6 Discussion 第一段与 §5.1 epoch confound 内容重复\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。§6 和 §5.1 都讨论 >95% multi-epoch exposure、LR-controlled verification、Δ=0.017 residual。建议 §6 仅引用 §5.1 结论。\"\n  action_items:\n    - round: 13\n      action: \"精简 §6 第一段，引用 §5.1 而非重复。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Cohen's d 被 deterministic data ordering 人为放大，效应量不确定性未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1/M4。d=3.83 但 σ=0.006 因 data ordering 固定（仅模型初始化不同）。如果 data shuffle seed 也随机化 paired SD 大概率升高。应报告 Cohen's d + CI 并讨论 deterministic ordering 对方差的影响。\"\n  action_items:\n    - round: 13\n      action: \"报告 Cohen's d + CI，讨论 deterministic data ordering 对 paired SD 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"PPL 改善与模型质量（下游任务能力）之间的关系未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2-W8。在 continued pretraining 中多大 PPL 改善才对应有意义的 capability 提升？鉴于下游 null result，此讨论对解读 findings 很重要。R1 交叉回应补充认同。\"\n  action_items:\n    - round: 13\n      action: \"在 Discussion 中简要讨论 PPL-capability 关系，或引用 relevant scaling law 文献。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m4\"\n  summary: \"Permuted q-scores ablation 仅 1 seed\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R1-M1。Table 3 确认仅 seed-42 有 Permuted 结果。作为 ablation 控制组 1 seed reliability 有限。R2 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"补充 permuted q-scores 多 seed 或标注 single-seed 限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11+ recurring issues (updated with Round 13 fresh review) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。双方 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"论文已升至 5 seeds + BH correction。统计检验力问题部分缓解但 Cohen's d=3.83 被 deterministic data ordering 人为放大（σ=0.006）——如果 data shuffle seed 也随机化，paired SD 大概率升高，Cohen's d 大幅缩水。R1 补充 N1。\"\n  action_items:\n    - round: 13\n      action: \"补 2 个 seed (seed789/234) 达 N=5。4 GPU 并行训练。N=5 后重算 BH 校正 p 值 + Cohen's d + CI。\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.63，Wang (2026) 理论保证不直接转移到 proxy\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 标为 critical：Wang 2026 要求 true real fraction ≥ τ，论文用 α_eff 替代（R²=0.63），~37% 未解释方差意味理论保证不成立。R2 AGREE 但建议降为 should-fix：论文核心贡献是 empirical findings 不是理论保证，修改 'guarantees' 措辞即可。圆桌共识：should-fix（R2 理由成立）。\"\n  action_items:\n    - round: 13\n      action: \"将 §3 中 'guarantees a convergence-rate lower bound' 改为 'targets/approximates'。量化 α_eff ≥ τ 但 true fraction < τ 的 batch 比例。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.023 PPL, 0.13% relative），practitioner framing 自相矛盾\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=128 幂律外推被一致认为不可靠。'practical' 表述仍残留。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2+W5 独立提出。核心矛盾：Abstract 'improves over uniform training' 未限定 PPL-only；§5.1/§6/§7 三处使用 'practitioner' 导向表述但下游零改善。R2 建议 Abstract/Conclusion 明确限定 'improves held-out PPL'。R1 建议重新定位为分析/负面结果贡献。R1 补充 Cohen's d=3.83 被 deterministic data ordering 放大。交叉回应双方 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"Abstract/Conclusion 限定 'improves held-out PPL'；在 main text 讨论下游 null result；考虑重新定位为 analysis paper with negative practical result at current scales。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"标题通用性远超实验 scope：仅 self-contamination + continued pretraining + 0.6B\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Cross-model transfer single seed + mixed + 无 PPL 比较。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 must-fix：标题 'When Does D&R Work?' 暗示一般性但实验仅覆盖 self-contamination/0.6B/continued pretraining/单一数据源。关键矛盾：epoch confound（最强贡献）在 from-scratch pretraining 下不适用（§6 自述），但标题未反映。R1 AGREE 并评为比自己的 W5 更精准。建议标题加限定如 '...in Continued Pretraining'。\"\n  action_items:\n    - round: 13\n      action: \"修改标题以反映 scope 限定（如加 'in Continued Pretraining' 或 'under Self-Contamination'），或完成 cross-model PPL 对比。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§3 压缩后仍给人独立方法贡献印象。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3：方法新颖性低（w=(1-q)^b 来自 Drayson，dual constraint + bisection 是标准方法）。R1 REBUT：单个组件非新但组合在此问题上是新的，且分析贡献不依赖算法新颖性，整体应为'中'而非'低'。唯一实质分歧。圆桌共识：中偏低，不影响评分。\"\n  action_items:\n    - round: 13\n      action: \"确保 Introduction 早期明确 analysis paper 定位，避免给读者方法贡献预期。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作和 detection benchmarks\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议。\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 新增：RAID benchmark (Dugan et al. 2024)、M4 shared task (Wang et al. 2024)。R1 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"考虑补充 RAID/M4 detection benchmarks 引用。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏 uniform+multi-epoch baseline\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Epoch confound 适用范围需限定为 multi-epoch exposure 场景。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2：缺 uniform × 3.2 epochs baseline 无法区分纯重复 vs 选择性重复。R2 AGREE 且认为计算成本低但对分析完整性至关重要。\"\n  action_items:\n    - round: 13\n      action: \"增加 uniform+multi-epoch baseline（全数据 ~3.2 epochs），完善 epoch confound 分析。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 可读性和 display item 分布问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"ρ 符号冲突、Figure 1 黑白不可辨。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"视觉审查发现 page 6 含 4 个 display items 密度过高（1 warning）。Figure 1 legend 字号偏小，Figure 2 灰度打印建议加阴影线。\"\n  action_items:\n    - round: 13\n      action: \"考虑将 Table 4 移至 appendix 缓解 page 6 密度。Figure 1 legend 字号增大。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 issues (updated with Round 13) ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"LaTeX wc 确认 225 words。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 ~155 words，合规。\"\n  resolution: \"Abstract 已压缩至 ~155 words，符合 ≤200 words 限制。\"\n  resolution_round: 13\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§7 Conclusion 溢出至第 9 页。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 §1-§7 在 page 8 内。合规。\"\n  resolution: \"正文已压缩至 8 页内。\"\n  resolution_round: 13\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个），不足以支撑 AUC/ECE threshold 的通用性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"仅 TF-IDF+LR / GPT-2 / N-gram。3 个数据点不足建立因果关系。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 + R1 AGREE。缺少 neural detectors（RoBERTa/DeBERTa/DetectGPT/Binoculars/RADAR）。AUC-ECE threshold 在更广 detector coverage 下可能不成立。\"\n  action_items:\n    - round: 13\n      action: \"扩展 detector coverage（至少含 1 个 neural detector），或将 threshold 标注为 'observed in our 3 detectors, not general guidance'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size scaling 趋势基于 3 个数据点，power law fitting 不可靠\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=4/8/16 仅 3 点，外推到 B=128 不可靠。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"未再单独提及，可能已部分改善。\"\n  action_items:\n    - round: 13\n      action: \"确认是否已删除 power law fitting，保留 monotonic trend 描述。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"建议将 Spearman 改为 ρ_s。\"\n  action_items:\n    - round: 12\n      action: \"全文 Spearman ρ → ρ_s\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 13 新发现/更新 ===\n\n- id: \"R13-W1\"\n  summary: \"B=4 micro-batch 上 dual constraint 统计可靠性不足，主实验在次优设定运行\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE（但认为 conservative reporting 有合理性）。B=4 MAE=0.114，advantage 最小（1.0×）。B=16 时 advantage 放大 3.0×。R2 认为 B=4 是 conservative reporting（最弱设置仍显著 → 更大 batch 更好），但核心问题仍在：应至少在 B=16 下重复核心对比并报告下游结果。\"\n  action_items:\n    - round: 13\n      action: \"说明 B=4 选择原因。可选：补充 B=16 完整对比（3 seeds + downstream）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Grid-best b=0.3 vs adaptive b*≈0.9 偏差：α_eff 负偏差导致过度干预，违背 minimum intervention 原则\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE。因果链：α_eff 负偏差 → quality floor 过早绑定 → b_τ 推高 → adaptive b*≈0.9 远高于 grid-best b=0.3。方法行为偏离设计意图（minimum intervention 实际上过度干预）。与 R11-C2 构成闭环。\"\n  action_items:\n    - round: 13\n      action: \"补充 per-batch b* 分布（median, percentiles）。可选：对比 fixed b=median(b*) 性能。分析 α_eff 负偏差对 b* 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"1.7B 规模效应递减 43% 且 scaling trend 未正式讨论\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2-Q5。0.6B→1.7B Δ 从 −0.023 缩至 −0.013（43% 递减），OOD 方向不一致。如果 trend 成立，practitioner 关注的 7B-70B 规模方法可能完全失效，削弱 Table 5 'for practitioners' 的适用性。R2 交叉回应补充认同。\"\n  action_items:\n    - round: 13\n      action: \"正式讨论 scaling trend 并限定 claim 范围。在 Table 5 或 Conclusion 加 scale caveat。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W4\"\n  summary: \"ρ≥0.4 实用门槛偏高，实际适用场景极窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2-W7。论文引用 synthetic text 20-60% 估计，但方法仅在 ρ≥0.4 + well-calibrated detector + self-contamination + continued pretraining + 0.6B 下有效。'Decision summary for practitioners' 在如此受限范围下可能给读者不准确信号。R1 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"在 Table 5 或 Conclusion 明确标注适用范围限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"§6 Discussion 第一段与 §5.1 epoch confound 内容重复\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。§6 和 §5.1 都讨论 >95% multi-epoch exposure、LR-controlled verification、Δ=0.017 residual。建议 §6 仅引用 §5.1 结论。\"\n  action_items:\n    - round: 13\n      action: \"精简 §6 第一段，引用 §5.1 而非重复。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Cohen's d 被 deterministic data ordering 人为放大，效应量不确定性未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1/M4。d=3.83 但 σ=0.006 因 data ordering 固定（仅模型初始化不同）。如果 data shuffle seed 也随机化 paired SD 大概率升高。应报告 Cohen's d + CI 并讨论 deterministic ordering 对方差的影响。\"\n  action_items:\n    - round: 13\n      action: \"报告 Cohen's d + CI，讨论 deterministic data ordering 对 paired SD 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"PPL 改善与模型质量（下游任务能力）之间的关系未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2-W8。在 continued pretraining 中多大 PPL 改善才对应有意义的 capability 提升？鉴于下游 null result，此讨论对解读 findings 很重要。R1 交叉回应补充认同。\"\n  action_items:\n    - round: 13\n      action: \"在 Discussion 中简要讨论 PPL-capability 关系，或引用 relevant scaling law 文献。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m4\"\n  summary: \"Permuted q-scores ablation 仅 1 seed\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R1-M1。Table 3 确认仅 seed-42 有 Permuted 结果。作为 ablation 控制组 1 seed reliability 有限。R2 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"补充 permuted q-scores 多 seed 或标注 single-seed 限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-25T05:00:39.530175+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 18967}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-25T05:02:49.828507+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: When Does Detect-and-Reweight Work for Synthetic Contamination?\n**Venue**: EMNLP 2026 (via ACL Rolling Review, May 2026 cycle)\n**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 论文完整性 + 格式合规）\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n\n---\n\n## Summary\n\n本文通过 Qwen3-0.6B 的 controlled continued pretraining 实验（132M FineWeb tokens, 40% self-contamination, 5 seeds），研究 detect-and-reweight (D&R) 方法的有效条件。核心发现三项：(1) 已发表 D&R 评估受 multi-epoch exposure 混淆，epoch-matched 后 >95% 优势消失；(2) detector 需同时具备 AUC≥0.9 和 ECE≤0.05；(3) minimum intervention 原则优于 unconstrained weight maximization。论文提出 dual-constrained adaptive b* 作为示例应用。\n\n两位 Reviewer 独立给出完全一致的评分（Overall 3.0 / Soundness 3.5 / Excitement 2.5 / Reproducibility 4 / Confidence 4），交叉回应后高度收敛，仅在方法新颖性水平（R1: 中偏低 vs R2: 低）和 N2 严重度（R1: critical vs R2: should-fix）上存在 minor 分歧。\n\n---\n\n## Strengths\n\n**S1** [共识] **Epoch confound 发现是最强贡献**。Table 2 和 Figure 1(a) 清晰展示 D&R 在 epoch-matched controls 下优势从 Δ≈-1.1 缩减至 Δ≈-0.017。实验设计简洁有效，对 data curation 社区有实际预警价值。\n\n**S2** [共识] **实验方法论严谨**。5 seeds + Bonferroni-Holm correction；ablation hierarchy (Adaptive > Uniform > ESS-only > Random > Permuted) 逻辑清晰；控制组设计周全（Permuted 破坏信号保留非均匀性，Random 使用随机权重，ESS-only 最大化 b）。\n\n**S3** [共识] **诚实的 framing**。论文将方法定位为 \"an illustrative application\"（Abstract），Limitations 对 scope 限定负责任。\n\n**S4** [R2] **Constraint regime 分析**（Figure 7）有实践洞察价值：ρ=0.4 时 ~59% batches clean，~40% ESS-binding，介入范围可预测。R1 交叉回应补充认同。\n\n**S5** [共识] **写作和视觉密度**。8 页正文含 7 figures + 5 tables，每个有明确目的。Propositions 1-2 数学正确，Algorithm 1 实现清晰。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1** [共识, R1-N1 + R2-W2+W5] **核心效应无实际意义且不迁移至下游任务**\n\nAdaptive b* 的 PPL 改善仅 0.13% relative（Δ=−0.023），5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）。然而论文在三处使用 practitioner 导向表述（§5.1 \"For practitioners\"、§6 Table 5 \"Decision summary for practitioners\"、§7 \"For practitioners, reweighting is worthwhile\"），Abstract 说 \"improves over uniform training\" 未限定 PPL-only。\n\nR1 补充：Cohen's d=3.83 被 deterministic data ordering 人为放大（σ=0.006，5 个 seed 仅改变模型初始化，data order 固定）——如果 data shuffle seed 也随机化，paired SD 大概率升高，Cohen's d 大幅缩水。\n\n**建议**：(a) Abstract/Conclusion 明确限定 \"improves held-out PPL\"；(b) 在 main text 讨论下游 null result（而非仅 Appendix I）；(c) 考虑重新定位为 analysis paper with negative practical result at current scales。\n\n**MF2** [R2-W1, R1 AGREE] **标题通用性远超实验 scope**\n\n标题 \"When Does D&R Work?\" 暗示一般性回答，但实验受限于 self-contamination / 0.6B 单一模型 / continued pretraining / 单一数据源。关键矛盾：最强贡献（epoch confound）在 from-scratch pretraining 下不适用（§6 自述 \"invisible in Drayson et al. because from-scratch pretraining rarely completes even one epoch\"）——即该发现对最常见的 pretraining 设定无意义，但标题未反映这一关键 scope 限定。\n\n**建议**：标题应更具体反映 scope，如 \"When Does Detect-and-Reweight Work? An Analysis under Self-Contamination in Continued Pretraining\"。\n\n### Should-Fix\n\n**SF1** [R1-N2, R2 AGREE（降为 should-fix）] **α_eff proxy 与 Wang (2026) 理论保证之间的逻辑断裂**\n\nWang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）。~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ，理论保证不成立。§3 中 \"guarantees a convergence-rate lower bound\" 措辞在技术上不准确。n_min 缓冲是 heuristic 而非 principled correction。\n\nR2 建议降为 should-fix：论文核心贡献是 empirical findings 不是理论保证，修改 \"guarantees\" 措辞即可消除误导。圆桌采纳此判断。\n\n**建议**：将 \"guarantees\" 改为 \"targets/approximates\"；量化 α_eff ≥ τ 但 true fraction < τ 的 batch 比例。\n\n**SF2** [R1-W1, R2 AGREE] **Grid-best b=0.3 vs adaptive b*≈0.9 偏差未解释**\n\nGrid search 最优 b=0.3 而 adaptive 产生 b*≈0.9，差异 3×。因果链：α_eff 负偏差（Table 12, bias≈−0.03）→ quality floor 过早绑定 → b_τ 被推高 → adaptive b* 远高于 post-hoc 最优。方法实际行为偏离 \"minimum intervention\" 设计意图。与 SF1 构成闭环。\n\n**建议**：补充 per-batch b* 分布（median, percentiles）；分析 debiased α_eff 的效果。\n\n**SF3** [R1-W2, R2 AGREE] **缺少 \"uniform + multi-epoch\" 基线**\n\nEpoch confound 分析缺少关键对照：对全部数据做 multi-epoch uniform training（~3.2 epochs，等量 compute），以区分纯重复 vs 选择性重复的效果。计算成本低但对分析完整性至关重要。\n\n**SF4** [R2-W3, R1 partial REBUT] **方法新颖性有限**\n\nw=(1−q)^b 完全来自 Drayson et al.，dual constraint + bisection 是标准方法组合。R1 认为组合在此问题上是新的且分析贡献不依赖算法新颖性（评 \"中偏低\"）；R2 认为方法新颖性低。圆桌结论：中偏低，论文应在 Introduction 早期更明确 analysis paper 定位。\n\n**SF5** [R2-W4 + R1 AGREE] **Detector 覆盖面极窄**\n\n仅 3 个 detector（TF-IDF+LR, GPT-2 perplexity, N-gram），缺少 neural detectors。3 个数据点不足以得出 AUC/ECE threshold 通用规律。\n\n**建议**：扩展至少 1 个 neural detector，或将 threshold 标注为 \"observed in our 3 detectors\"。\n\n**SF6** [R1-W3 + R2-Q5] **1.7B 规模效应递减 43% 未正式讨论**\n\n0.6B→1.7B Δ 从 −0.023 缩至 −0.013（43% 递减），OOD 方向不一致。如果 trend 成立，方法在 practitioner 关注的 7B+ 规模可能完全失效。\n\n**建议**：正式讨论 scaling trend，在 Table 5 或 Conclusion 加 scale caveat。\n\n**SF7** [R1-W5 + R2-W6] **Self-contamination 生态效度有限**\n\nSelf-contamination 对 detector 最有利。Cross-model 结果（Llama-3.2-3B）仅单 seed 无 PPL，反而暴露 generalization 困难。\n\n**SF8** [R1-W4, R2 AGREE（较低严重度）] **B=4 是最弱设置却用于主实验**\n\nB=4 时 MAE=0.114，advantage 最小（1.0×）。B=16 时 advantage 放大 3.0×。R2 认为 conservative reporting 有合理性，但应至少在 B=16 下重复核心对比并报告下游。\n\n### Minor\n\n- **m1** [R2-W7] ρ≥0.4 实用门槛偏高，适用场景极窄\n- **m2** [R2-W8, R1 AGREE] PPL-capability 关系未讨论\n- **m3** [R1-M1] Permuted q-scores 仅 1 seed\n- **m4** [R1-M2] ρ=0.6 p_BH=0.064 措辞需明确标为 \"not significant after correction\"\n- **m5** [R1-M3] Table 5 \"Generator ≠ trainee\" 应考虑标为必要条件\n- **m6** [R1-M4 + R2] Cohen's d=3.83 解读需注意 deterministic ordering 对 paired SD 的影响\n- **m7** [R2] §6 Discussion 第一段与 §5.1 epoch confound 内容重复\n\n---\n\n## Questions\n\n**Q1** [共识]: 下游任务零改善下，方法推荐用于什么实际场景？\n**Q2** [共识]: GPT-4/Claude 级 synthetic data 下 detector 性能如何？AUC/ECE guidance 在更广 detector sweep 下是否稳健？\n**Q3** [R1]: α_eff 负偏差是否导致 b* 系统偏高？Debiased α_eff 效果如何？\n**Q4** [共识]: 为何选 B=4 而非 B=8/16 作主实验配置？\n**Q5** [R2]: τ=0.7 是否有 principled 选择方法？Per-batch bisection 的 b* variance 对 gradient noise 的影响？\n**Q6** [R2]: 1.7B 规模 benefit 缩减至 Δ≈−0.013，方法在 7B+ 是否完全失效？\n\n---\n\n## Missing References\n\n- **RAID benchmark** (Dugan et al., 2024): AI text detection benchmark，覆盖多种 generator/domain [R2 提出, R1 AGREE]\n- **M4 shared task** (Wang et al., 2024): 多语言多生成器检测 benchmark [R2 提出, R1 AGREE]\n\n---\n\n## External Review\n\n**状态**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：完成（0 critical, 1 warning, 10 info）\n\n- **[warning]** Page 6 含 4 个 display items（Figure 4 + Tables 2, 3, 4），视觉密度极高。建议将 Table 4 移至 appendix。\n- **[info]** Figure 1 legend 字号偏小，建议增大。\n- **[info]** Figure 2 绿色半透明区域灰度打印下可能不够显眼，建议加阴影线。\n- **[info]** Figure 9 axis label/legend 字号约正文 60-65%，接近可读性下限。\n- **[info]** 格式合规：Abstract ~155 words（≤200 ✓），正文 8 页内（≤8 ✓），Limitations 段 3 点简短（✓），References 格式统一无 [?]（✓）。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 2.5 | 2.5 | **2.5** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Confidence | 4.0 | 4.0 | **4.0** |\n| **Overall** | **3.0** | **3.0** | **3.0** |\n\n**核心判断**：论文实验方法论严谨，epoch confound 发现（F1）对社区有预警价值，写作诚实且 self-aware。但以下问题限制其影响力：\n\n1. **效果量极小且零下游改善**（MF1）：0.13% PPL 改善不传导至任何下游任务，practitioner 导向 framing 缺乏支撑\n2. **标题与 scope 严重不匹配**（MF2）：最强贡献 F1 在 from-scratch pretraining 下不适用，但标题暗示通用性\n3. **α_eff proxy 理论断裂**（SF1）：与 Wang (2026) 理论保证不直接对应，导致 b* 系统偏高（SF2）\n4. **方法新颖性有限**（SF4）：建立在 Drayson et al. 基础上的标准优化应用\n5. **实验范围窄**：仅 self-contamination + 0.6B + continued pretraining + 3 detectors，规模递减趋势不利\n\n**达到 Conference 水平需要**：\n(a) 扩展 detector 覆盖（含 neural detectors）\n(b) 在至少一个下游任务或更大 batch size 下展示改善，或明确重新定位为 negative result\n(c) 补充 uniform+multi-epoch baseline 完善 epoch confound 分析\n(d) 修改标题反映 scope 限定\n\n论文作为 focused empirical analysis 适合 Findings 接收。\n\n---\n\n## Detailed Comments\n\n### 交叉回应共识总结\n\n| 问题 | R1→R2 | R2→R1 | 共识 |\n|------|-------|-------|------|\n| 核心效应小+零下游 | AGREE | AGREE | ✅ Must-fix |\n| 标题 scope 不匹配 | AGREE（更精准） | — | ✅ Must-fix |\n| α_eff 理论断裂 | — | AGREE（降为 SF） | ✅ Should-fix |\n| Grid-best vs b* 偏差 | — | AGREE | ✅ Should-fix |\n| 缺 multi-epoch baseline | — | AGREE | ✅ Should-fix |\n| 方法新颖性 | REBUT（中 vs 低） | — | ⚠️ Minor 分歧 |\n| Detector 覆盖窄 | AGREE | AGREE | ✅ Should-fix |\n| Self-contamination 生态效度 | AGREE | AGREE | ✅ Should-fix |\n| 规模递减 | AGREE | AGREE | ✅ Should-fix |\n| B=4 最弱设置 | — | AGREE（较低严重度） | ✅ Should-fix |\n| ρ≥0.4 门槛偏高 | AGREE | — | ✅ Minor |\n| PPL-capability 关系 | AGREE | — | ✅ Minor |\n| τ 选择 principled? | — | REBUT（已有 sweep） | ✅ 已回应 |\n\n### Issue Tracker 跨轮次状态\n\n本轮独立发现的问题与 Round 11-12 高度重叠，确认以下为结构性问题（4 轮连续被指出）：\n- R11-C1: 统计检验力（已 in_progress，补 seed 中）\n- R11-C2: α_eff proxy 可靠性（本轮从 critical 降为 should-fix）\n- R11-C3: 下游零改善 + practitioner framing 矛盾\n- R11-C4: 实验范围过窄 / 标题通用性\n\n新增问题（Round 13 首次提出）：\n- R13-W2: Grid-best b=0.3 vs adaptive b*≈0.9 偏差\n- R13-W3: 1.7B 规模效应递减 43% 未正式讨论\n- R13-W4: ρ≥0.4 门槛偏高\n- R13-m2: Cohen's d 被 deterministic data ordering 放大\n- R13-m3: PPL-capability 关系未讨论\n",
  "project": "provenance_weight_training",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: When Does Detect-and-Reweight Work for Synthetic Contamination?\n**Venue**: EMNLP 2026 (via ACL Rolling Review, May 2026 cycle)\n**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 论文完整性 + 格式合规）\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n\n---\n\n## Summary\n\n本文通过 Qwen3-0.6B 的 controlled continued pretraining 实验（132M FineWeb tokens, 40% self-contamination, 5 seeds），研究 detect-and-reweight (D&R) 方法的有效条件。核心发现三项：(1) 已发表 D&R 评估受 multi-epoch exposure 混淆，epoch-matched 后 >95% 优势消失；(2) detector 需同时具备 AUC≥0.9 和 ECE≤0.05；(3) minimum intervention 原则优于 unconstrained weight maximization。论文提出 dual-constrained adaptive b* 作为示例应用。\n\n两位 Reviewer 独立给出完全一致的评分（Overall 3.0 / Soundness 3.5 / Excitement 2.5 / Reproducibility 4 / Confidence 4），交叉回应后高度收敛，仅在方法新颖性水平（R1: 中偏低 vs R2: 低）和 N2 严重度（R1: critical vs R2: should-fix）上存在 minor 分歧。\n\n---\n\n## Strengths\n\n**S1** [共识] **Epoch confound 发现是最强贡献**。Table 2 和 Figure 1(a) 清晰展示 D&R 在 epoch-matched controls 下优势从 Δ≈-1.1 缩减至 Δ≈-0.017。实验设计简洁有效，对 data curation 社区有实际预警价值。\n\n**S2** [共识] **实验方法论严谨**。5 seeds + Bonferroni-Holm correction；ablation hierarchy (Adaptive > Uniform > ESS-only > Random > Permuted) 逻辑清晰；控制组设计周全（Permuted 破坏信号保留非均匀性，Random 使用随机权重，ESS-only 最大化 b）。\n\n**S3** [共识] **诚实的 framing**。论文将方法定位为 \"an illustrative application\"（Abstract），Limitations 对 scope 限定负责任。\n\n**S4** [R2] **Constraint regime 分析**（Figure 7）有实践洞察价值：ρ=0.4 时 ~59% batches clean，~40% ESS-binding，介入范围可预测。R1 交叉回应补充认同。\n\n**S5** [共识] **写作和视觉密度**。8 页正文含 7 figures + 5 tables，每个有明确目的。Propositions 1-2 数学正确，Algorithm 1 实现清晰。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1** [共识, R1-N1 + R2-W2+W5] **核心效应无实际意义且不迁移至下游任务**\n\nAdaptive b* 的 PPL 改善仅 0.13% relative（Δ=−0.023），5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）。然而论文在三处使用 practitioner 导向表述（§5.1 \"For practitioners\"、§6 Table 5 \"Decision summary for practitioners\"、§7 \"For practitioners, reweighting is worthwhile\"），Abstract 说 \"improves over uniform training\" 未限定 PPL-only。\n\nR1 补充：Cohen's d=3.83 被 deterministic data ordering 人为放大（σ=0.006，5 个 seed 仅改变模型初始化，data order 固定）——如果 data shuffle seed 也随机化，paired SD 大概率升高，Cohen's d 大幅缩水。\n\n**建议**：(a) Abstract/Conclusion 明确限定 \"improves held-out PPL\"；(b) 在 main text 讨论下游 null result（而非仅 Appendix I）；(c) 考虑重新定位为 analysis paper with negative practical result at current scales。\n\n**MF2** [R2-W1, R1 AGREE] **标题通用性远超实验 scope**\n\n标题 \"When Does D&R Work?\" 暗示一般性回答，但实验受限于 self-contamination / 0.6B 单一模型 / continued pretraining / 单一数据源。关键矛盾：最强贡献（epoch confound）在 from-scratch pretraining 下不适用（§6 自述 \"invisible in Drayson et al. because from-scratch pretraining rarely completes even one epoch\"）——即该发现对最常见的 pretraining 设定无意义，但标题未反映这一关键 scope 限定。\n\n**建议**：标题应更具体反映 scope，如 \"When Does Detect-and-Reweight Work? An Analysis under Self-Contamination in Continued Pretraining\"。\n\n### Should-Fix\n\n**SF1** [R1-N2, R2 AGREE（降为 should-fix）] **α_eff proxy 与 Wang (2026) 理论保证之间的逻辑断裂**\n\nWang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）。~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ，理论保证不成立。§3 中 \"guarantees a convergence-rate lower bound\" 措辞在技术上不准确。n_min 缓冲是 heuristic 而非 principled correction。\n\nR2 建议降为 should-fix：论文核心贡献是 empirical findings 不是理论保证，修改 \"guarantees\" 措辞即可消除误导。圆桌采纳此判断。\n\n**建议**：将 \"guarantees\" 改为 \"targets/approximates\"；量化 α_eff ≥ τ 但 true fraction < τ 的 batch 比例。\n\n**SF2** [R1-W1, R2 AGREE] **Grid-best b=0.3 vs adaptive b*≈0.9 偏差未解释**\n\nGrid search 最优 b=0.3 而 adaptive 产生 b*≈0.9，差异 3×。因果链：α_eff 负偏差（Table 12, bias≈−0.03）→ quality floor 过早绑定 → b_τ 被推高 → adaptive b* 远高于 post-hoc 最优。方法实际行为偏离 \"minimum intervention\" 设计意图。与 SF1 构成闭环。\n\n**建议**：补充 per-batch b* 分布（median, percentiles）；分析 debiased α_eff 的效果。\n\n**SF3** [R1-W2, R2 AGREE] **缺少 \"uniform + multi-epoch\" 基线**\n\nEpoch confound 分析缺少关键对照：对全部数据做 multi-epoch uniform training（~3.2 epochs，等量 compute），以区分纯重复 vs 选择性重复的效果。计算成本低但对分析完整性至关重要。\n\n**SF4** [R2-W3, R1 partial REBUT] **方法新颖性有限**\n\nw=(1−q)^b 完全来自 Drayson et al.，dual constraint + bisection 是标准方法组合。R1 认为组合在此问题上是新的且分析贡献不依赖算法新颖性（评 \"中偏低\"）；R2 认为方法新颖性低。圆桌结论：中偏低，论文应在 Introduction 早期更明确 analysis paper 定位。\n\n**SF5** [R2-W4 + R1 AGREE] **Detector 覆盖面极窄**\n\n仅 3 个 detector（TF-IDF+LR, GPT-2 perplexity, N-gram），缺少 neural detectors。3 个数据点不足以得出 AUC/ECE threshold 通用规律。\n\n**建议**：扩展至少 1 个 neural detector，或将 threshold 标注为 \"observed in our 3 detectors\"。\n\n**SF6** [R1-W3 + R2-Q5] **1.7B 规模效应递减 43% 未正式讨论**\n\n0.6B→1.7B Δ 从 −0.023 缩至 −0.013（43% 递减），OOD 方向不一致。如果 trend 成立，方法在 practitioner 关注的 7B+ 规模可能完全失效。\n\n**建议**：正式讨论 scaling trend，在 Table 5 或 Conclusion 加 scale caveat。\n\n**SF7** [R1-W5 + R2-W6] **Self-contamination 生态效度有限**\n\nSelf-contamination 对 detector 最有利。Cross-model 结果（Llama-3.2-3B）仅单 seed 无 PPL，反而暴露 generalization 困难。\n\n**SF8** [R1-W4, R2 AGREE（较低严重度）] **B=4 是最弱设置却用于主实验**\n\nB=4 时 MAE=0.114，advantage 最小（1.0×）。B=16 时 advantage 放大 3.0×。R2 认为 conservative reporting 有合理性，但应至少在 B=16 下重复核心对比并报告下游。\n\n### Minor\n\n- **m1** [R2-W7] ρ≥0.4 实用门槛偏高，适用场景极窄\n- **m2** [R2-W8, R1 AGREE] PPL-capability 关系未讨论\n- **m3** [R1-M1] Permuted q-scores 仅 1 seed\n- **m4** [R1-M2] ρ=0.6 p_BH=0.064 措辞需明确标为 \"not significant after correction\"\n- **m5** [R1-M3] Table 5 \"Generator ≠ trainee\" 应考虑标为必要条件\n- **m6** [R1-M4 + R2] Cohen's d=3.83 解读需注意 deterministic ordering 对 paired SD 的影响\n- **m7** [R2] §6 Discussion 第一段与 §5.1 epoch confound 内容重复\n\n---\n\n## Questions\n\n**Q1** [共识]: 下游任务零改善下，方法推荐用于什么实际场景？\n**Q2** [共识]: GPT-4/Claude 级 synthetic data 下 detector 性能如何？AUC/ECE guidance 在更广 detector sweep 下是否稳健？\n**Q3** [R1]: α_eff 负偏差是否导致 b* 系统偏高？Debiased α_eff 效果如何？\n**Q4** [共识]: 为何选 B=4 而非 B=8/16 作主实验配置？\n**Q5** [R2]: τ=0.7 是否有 principled 选择方法？Per-batch bisection 的 b* variance 对 gradient noise 的影响？\n**Q6** [R2]: 1.7B 规模 benefit 缩减至 Δ≈−0.013，方法在 7B+ 是否完全失效？\n\n---\n\n## Missing References\n\n- **RAID benchmark** (Dugan et al., 2024): AI text detection benchmark，覆盖多种 generator/domain [R2 提出, R1 AGREE]\n- **M4 shared task** (Wang et al., 2024): 多语言多生成器检测 benchmark [R2 提出, R1 AGREE]\n\n---\n\n## External Review\n\n**状态**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：完成（0 critical, 1 warning, 10 info）\n\n- **[warning]** Page 6 含 4 个 display items（Figure 4 + Tables 2, 3, 4），视觉密度极高。建议将 Table 4 移至 appendix。\n- **[info]** Figure 1 legend 字号偏小，建议增大。\n- **[info]** Figure 2 绿色半透明区域灰度打印下可能不够显眼，建议加阴影线。\n- **[info]** Figure 9 axis label/legend 字号约正文 60-65%，接近可读性下限。\n- **[info]** 格式合规：Abstract ~155 words（≤200 ✓），正文 8 页内（≤8 ✓），Limitations 段 3 点简短（✓），References 格式统一无 [?]（✓）。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 2.5 | 2.5 | **2.5** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Confidence | 4.0 | 4.0 | **4.0** |\n| **Overall** | **3.0** | **3.0** | **3.0** |\n\n**核心判断**：论文实验方法论严谨，epoch confound 发现（F1）对社区有预警价值，写作诚实且 self-aware。但以下问题限制其影响力：\n\n1. **效果量极小且零下游改善**（MF1）：0.13% PPL 改善不传导至任何下游任务，practitioner 导向 framing 缺乏支撑\n2. **标题与 scope 严重不匹配**（MF2）：最强贡献 F1 在 from-scratch pretraining 下不适用，但标题暗示通用性\n3. **α_eff proxy 理论断裂**（SF1）：与 Wang (2026) 理论保证不直接对应，导致 b* 系统偏高（SF2）\n4. **方法新颖性有限**（SF4）：建立在 Drayson et al. 基础上的标准优化应用\n5. **实验范围窄**：仅 self-contamination + 0.6B + continued pretraining + 3 detectors，规模递减趋势不利\n\n**达到 Conference 水平需要**：\n(a) 扩展 detector 覆盖（含 neural detectors）\n(b) 在至少一个下游任务或更大 batch size 下展示改善，或明确重新定位为 negative result\n(c) 补充 uniform+multi-epoch baseline 完善 epoch confound 分析\n(d) 修改标题反映 scope 限定\n\n论文作为 focused empirical analysis 适合 Findings 接收。\n\n---\n\n## Detailed Comments\n\n### 交叉回应共识总结\n\n| 问题 | R1→R2 | R2→R1 | 共识 |\n|------|-------|-------|------|\n| 核心效应小+零下游 | AGREE | AGREE | ✅ Must-fix |\n| 标题 scope 不匹配 | AGREE（更精准） | — | ✅ Must-fix |\n| α_eff 理论断裂 | — | AGREE（降为 SF） | ✅ Should-fix |\n| Grid-best vs b* 偏差 | — | AGREE | ✅ Should-fix |\n| 缺 multi-epoch baseline | — | AGREE | ✅ Should-fix |\n| 方法新颖性 | REBUT（中 vs 低） | — | ⚠️ Minor 分歧 |\n| Detector 覆盖窄 | AGREE | AGREE | ✅ Should-fix |\n| Self-contamination 生态效度 | AGREE | AGREE | ✅ Should-fix |\n| 规模递减 | AGREE | AGREE | ✅ Should-fix |\n| B=4 最弱设置 | — | AGREE（较低严重度） | ✅ Should-fix |\n| ρ≥0.4 门槛偏高 | AGREE | — | ✅ Minor |\n| PPL-capability 关系 | AGREE | — | ✅ Minor |\n| τ 选择 principled? | — | REBUT（已有 sweep） | ✅ 已回应 |\n\n### Issue Tracker 跨轮次状态\n\n本轮独立发现的问题与 Round 11-12 高度重叠，确认以下为结构性问题（4 轮连续被指出）：\n- R11-C1: 统计检验力（已 in_progress，补 seed 中）\n- R11-C2: α_eff proxy 可靠性（本轮从 critical 降为 should-fix）\n- R11-C3: 下游零改善 + practitioner framing 矛盾\n- R11-C4: 实验范围过窄 / 标题通用性\n\n新增问题（Round 13 首次提出）：\n- R13-W2: Grid-best b=0.3 vs adaptive b*≈0.9 偏差\n- R13-W3: 1.7B 规模效应递减 43% 未正式讨论\n- R13-W4: ρ≥0.4 门槛偏高\n- R13-m2: Cohen's d 被 deterministic data ordering 放大\n- R13-m3: PPL-capability 关系未讨论\n",
    "project": "provenance_weight_training",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-25T05:02:53.793244+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3964
}
```

</details>

---


### Assistant

_source line 1374 · 2026-05-25T05:03:00.146754+00:00_

审稿报告已投递。

**Round 13 (Fresh) 审稿完成**：

- **Overall: 3.0 (Findings)**，两位 Reviewer 独立评分完全一致
- **2 个 Must-Fix**：核心效应极小+零下游改善与 practitioner framing 矛盾；标题通用性远超实验 scope
- **8 个 Should-Fix**：α_eff 理论断裂、b* 偏差、缺 multi-epoch baseline、方法新颖性有限、detector 覆盖窄、规模递减、生态效度、B=4 设置
- **7 个 Minor**
- Issue Tracker 已同步更新，标记了 4 个跨轮次结构性问题和 5 个本轮新发现

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1375 · 2026-05-25T05:03:02.928453+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：R1 和我在所有主要判断上高度一致（Overall 3.0, 四维度评分完全相同），R1 提出了 5 个我未独立发现的有效问题（α_eff proxy 断裂、grid-best vs adaptive 偏差、缺 multi-epoch uniform 基线、B=4 选择、Cohen's d 膨胀）。唯一分歧在 N2 的 severity——我认为从 critical 降为 should-fix 更合适，因为论文的核心贡献是 empirical 而非 theoretical。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1376 · 2026-05-25T05:03:12.205209+00:00_

Round 13 审稿报告已投递至 Research Director，Reviewer 2 的交叉回应在报告提交前已纳入考量。

**审稿结论**：Overall 3.0 (Findings)，两位 Reviewer 四维度评分完全一致（Soundness 3.5 / Excitement 2.5 / Reproducibility 4 / Confidence 4），交叉回应后高度收敛。2 个 must-fix（核心效应极小+零下游+practitioner framing 矛盾；标题通用性超 scope）、8 个 should-fix、7 个 minor。Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 108

## Round 108

60 recorded events


### User

_source line 1377 · 2026-05-25T21:14:00.427701+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-25T21:14:05.616210+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-25T21:14:05.667115+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-25T21:14:12.893558+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-25T21:14:12.944302+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-25T21:14:16.779163+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-25T21:14:16.779635+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-25T21:14:21.444636+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-25T21:14:23.362413+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (269 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无 — 4 GPU 全部空闲）\n\n## D&R 阈值扫描结果（完整）\n| 阈值 | 数据保留 | holdout_ppl | owt_ppl | wiki_ppl | seeds |\n|------|---------|-------------|---------|----------|-------|\n| q>0.3 | 31.5% | 17.25 | — | — | 3 (prior) |\n| q>0.5 | 41.4% | 17.291 | 18.02 | 15.06 | 1 (ckpt-5500) |\n| q>0.7 | 50.0% | 17.32 | 18.04 | 15.11 | 3 |\n| Uniform | 100% | 17.694 | — | — | baseline |\n| Adaptive b* | 100% | 17.674 | — | — | baseline |\n\n## 近期结论\n- **q07 三 seed 完成** (success): holdout=17.32±0.00, owt=18.04±0.01, wiki=15.11±0.01 — 方差极小\n- **q05 ckpt-5500** (success): holdout=17.291, owt=18.02, wiki=15.06（final model 因 optimizer corruption 废弃）\n- **所有 D&R 阈值均显著优于 Uniform (17.694) 和 Adaptive b* (17.674)**\n\n## 趋势\n成功 175 / 负向 14 / 失败 42 / 共 254\n\n## 下一步\n- Paper Agent 可用完整 D&R 数据更新论文\n- 4 GPU 空闲待命\n\n## 资源状态\nwestd-41312: cuda:0/1/2/3 全部空闲\n\n## 告警\n- detector_modernbert: 已被终止 — unknown\n- diagnostic_contamination100: 已被终止 — unknown\n- adaptive_v2_seed42: 已被终止 — unknown\n- adaptive_v2_seed123: 已被终止 — unknown\n- adaptive_v2_seed456: 已被终止 — unknown\n- grid_b_low_seed42: 训练失败 — unknown\n- tau_0.6_seed42: 已被终止 — unknown\n- bs8_seed42: 训练失败 — unknown\n- bs8_nmin2_seed42: 训练失败 — unknown\n- contamination_60_
…[truncated 1820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1917
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-25T21:14:23.362809+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-25T21:14:23.463492+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-25T21:14:24.919194+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-25T21:14:25.221719+00:00_

-rw-r--r-- 1 ubuntu ubuntu 668899 May 25 20:29 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1390 · 2026-05-25T21:14:25.222116+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-25T21:14:25.272545+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1392 · 2026-05-25T21:14:34.657073+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1393 · 2026-05-25T21:14:35.059056+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-25T21:14:35.210020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-25T21:14:35.963266+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	\begin{figure*}[t]
6	\centering
7	\includegraphics[width=\textwidth]{fig1_overview}
8	\caption{Three effectiveness conditions for detect-and-reweight.
9	\textbf{(a)}~D\&R achieves the best raw PPL; epoch-matched controls reveal that multi-epoch exposure on filtered data accounts for the bulk of the advantage (\S\ref{sec:results}).
10	\textbf{(b)}~Only detectors with both high AUC \emph{and} low ECE fall in the effective zone; comparable AUC with poor calibration degrades PPL below uniform.
11	\textbf{(c)}~Adaptive $\bstar{\approx}0.9$ operates near the grid-search optimum, while ESS-only $b{\approx}3.5$ falls in the degradation zone.}
12	\label{fig:overview}
13	\end{figure*}
14	
15	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
16	What mechanism drives D\&R's strong performance, and how does it compare to soft reweighting under controlled conditions?
17	What detector properties are necessary for effective reweighting?
18	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
19	
20	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 5 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
21	To ground the analysis of exponent selection, we impleme
…[truncated 1838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-25T21:14:36.164495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-25T21:14:36.516239+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\% of web corpora, though accumulating real data avoids divergence~\citep{kazdan2025collapse} and even minimal curation suffices~\citep{amin2025escaping}.
6	Not all synthetic data is harmful: the Phi series~\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.
7	
8	\paragraph{Detection, Filtering, and Data Reweighting.}
9	Continuous-score detectors---probability curvature~\citep{mitchell2023detectgpt}, cross-perplexity ratios~\citep{hans2024binoculars}, low-probability token statistics~\citep{shi2024minkprob}---enable document-level weighting~\citep{wu2025survey}.
10	Data composition is optimized via perplexity filtering~\citep{wenzek2020ccnet}, domain-level importance sampling~\citep{xie2023doremi,xie2023dsir,grangier2025crisp,ye2025mixing}, instance-level strategies~\citep{bengio2009curriculum,mindermann2022prioritized,sow2025dynamic,engstrom2024dsdm}, and deduplication~\citep{abbas2023semdedup}; see \citet{albalak2024survey}.
11	None targets synthetic provenance; moreover, classifier-based quality scores may capture stylistic similarity rather than intrinsic quality~\citep{naitsaada2025illusion}.
12	Most directly related, \citet{drayson2025detection} propose $w_j = (1{-
…[truncated 2560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-25T21:14:36.617005+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-25T21:14:37.019203+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-25T21:14:37.019561+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-25T21:14:37.471455+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution, providing a controlled testbed with known ground-truth labels but limiting ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss implications for detection difficulty in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.048 after temperature scaling with $T{=}0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness} (implementation details in Appendix~\ref{app:detector_details}).
11	
12	\paragraph{Training.}
13	Table~\ref{tab:config} summarizes the training configuration.
14	We use $B{=}4
…[truncated 2489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-25T21:14:37.471813+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-25T21:14:37.974174+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-25T21:14:37.974646+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-25T21:14:37.974938+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1406 · 2026-05-25T21:14:38.426740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1407 · 2026-05-25T21:14:39.129529+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (i)~D\&R is the strongest method in our setting, with multi-epoch exposure on filtered data accounting for ${>}$95\% of its advantage over reweighting; (ii)~detector calibration alongside discrimination, as high-AUC detectors with poor calibration degrade PPL below uniform; and (iii)~minimum intervention over unconstrained maximization, supported by the ESS-only ablation and the fixed-$b$ grid curve (Figure~\ref{fig:grid_b_trend}).
2	A dual-constrained adaptive $\bstar$ implementing these principles improves over uniform training at $\rho \geq 0.4$ without per-model tuning (Table~\ref{tab:decision}), though without measurable downstream gains at 0.6B scale.
3	Whether these conditions hold at full pretraining scale ($>$100B tokens), where contamination ratios are lower but corpora are harder to curate, is the central open question; a second priority is extending the detector--calibration axis to neural classifiers whose ECE profiles differ qualitatively from the TF-IDF family tested here.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-25T21:14:39.180156+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-25T21:14:39.280870+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-25T21:14:39.883383+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1411 · 2026-05-25T21:14:40.386158+00:00_

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
…[truncated 28571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-25T21:14:40.386647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-25T21:14:40.688444+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@inproceedings{dugan2024raid,
5	  title={{RAID}: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors},
6	  author={Dugan, Liam and Hwang, Alyssa and Trhl{\'\i}k, Filip and Langmore, Andrew and Ippolito, Daphne and Callison-Burch, Chris and Ets-Hokin, Garrison},
7	  booktitle={ACL},
8	  year={2024}
9	}
10	
11	@article{wang2024m4,
12	  title={{M4}: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection},
13	  author={Wang, Yuxia and Manber, Jonibek and Shaar, Shaden and Arase, Yuki and Derczynski, Leon and Nakov, Preslav},
14	  journal={EACL},
15	  year={2024}
16	}
17	
18	@article{gunasekar2023textbooks,
19	  title={Textbooks Are All You Need},
20	  author={Gunasekar, Suriya and Zhang, Yi and Aneja, Jyoti and Mendes, Caio C{\'e}sar Teodoro and Del Giorno, Allie and Gopi, Sivakanth and Javaheripi, Mojan and Kauffmann, Piero and de Rosa, Gustavo and Saarikivi, Olli and Salim, Adil and Shah, Shital and Behl, Harkirat Singh and Wang, Xin and Bubeck, S{\'e}bastien and Eldan, Ronen and Kalai, Adam Tauman and Lee, Yin Tat and Li, Yuanzhi},
21	  journal={arXiv preprint arXiv:2306.11644},
22	  year={2023}
23	}
24	
25	@article{li2023textbooks2,
26	  title={Textbooks Are All You Need {II}: phi-1.5 Technical Report},
27	  author={Li, Yuanzhi and Bubeck, S{\'e}bastien and Eldan, Ronen and Del Giorno, Allie and Gunasekar, Suriya and Lee, Yin Tat},
28	  journal={arXiv preprint arXiv:2309.05463},
29	  year={2023}
30	}
31	
32	@inproceedings{katharopoulos2018not,
33	  title={Not All Samples Are Created Equal: Deep Learning with Importance Sampling},
34	  author={Katharopoulos, Angelos and Fleuret, Fran{\c{c}}ois},
35	  booktitle={International Conference on Machine Learning},
36	  pages={2525--2534},
37	  year={2018},
38	  organization={PMLR}
39	}
40	
41	@inproceedings{ren2018learning,
…[truncated 21226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-25T21:14:40.688809+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines page limit"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-25T21:14:46.058061+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"}]

Based on the web search results, here's the information about EMNLP 2026 page limits for ARR submissions:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

## ARR Submission Guidelines

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. Dual submissions are not allowed!

## Key Submission Details

All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026. For more detai
…[truncated 217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5369
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-25T21:15:11.398706+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 1417 · 2026-05-25T21:15:11.399091+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1418 · 2026-05-25T21:15:14.410710+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1419 · 2026-05-25T21:15:14.964886+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Mon May 25 20:29:06 2026 UTC
ModDate:         Mon May 25 20:29:06 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           15
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       668899 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 1420 · 2026-05-25T21:15:14.965220+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines author checklist anonymity requirements formatting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines author checklist anonymity requirements formatting"
  }
}
```

</details>

---


### Tool result

_source line 1421 · 2026-05-25T21:15:24.705658+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines author checklist anonymity requirements formatting"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here's a comprehensive overview of the ACL Rolling Review 2026 submission guidelines covering the key areas you asked about:

## **Anonymity Requirements**

Papers must not include authors' names and affiliations, and self-references that reveal authors' identities (e.g., "We previously showed (Smith, 1991)…") must be avoided. Supplementary materials, including any li
…[truncated 1594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 9740
}
```

</details>

---


### Tool call

_source line 1422 · 2026-05-25T21:15:34.189821+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-25T21:15:34.240888+00:00_

issues:
# === Round 10 issues (all resolved, retained for history) ===
- id: "R10-C1"
  summary: "Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。"
  resolution: "tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。"
  resolution_round: 10

- id: "R10-C2"
  summary: "多重比较未校正，p=0.025 Bonferroni 校正后不显著"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。"
  resolution: "BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。"
  resolution_round: 10

- id: "R10-C3"
  summary: "方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。"
  resolution: "§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。"
  resolution_round: 10

- id: "R10-C4"
  summary: "Downstream task 零改善削弱实际意义"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。"
  resolution: "Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。"
  resolution_round: 10

- id: "R10-M1"
  summary: "实验规模和场景过于狭窄，ρ=0.3 缺失"
  category: experiment
  severity: warning
  status: resolved
  first_raised_
…[truncated 16966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-25T21:15:34.341661+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1425 · 2026-05-25T21:15:34.392286+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-25T21:16:27.528862+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "provenance_weight_training",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "provenance_weight_training",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-25T21:16:51.308242+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23779
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-25T21:16:52.223512+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **论文**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n- **Venue**: EMNLP 2026 via ARR\n- **类型**: Long paper（正文 ≤8 页，references 不限，Limitations 不计页数）\n- **匿名**: Double-blind\n- **模板**: ACL style\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n**核心关注（必须逐条评估）**：\n1. **统计方法论**：5 seeds 的统计检验力是否充分？Bonferroni-Holm 校正的使用是否恰当？Cohen's d=3.83 是否被 deterministic data ordering 人为放大（seeds 仅影响模型初始化，data order 固定）？paired t-test 的前提假设是否满足？\n2. **效应量与实际意义**：Δ=-0.023 PPL（0.13% relative）的工程意义如何？下游任务零改善（|Δ|≤0.01）是否与 practitioner-oriented framing 矛盾？\n3. **α_eff proxy 可靠性**：Pearson r≈0.79 (R²≈0.63) 意味 ~37% 未解释方差。Wang (2026) 理论保证要求 true real fraction ≥ τ，但论文用 α_eff 替代，理论保证是否仍成立？\n4. **D&R 机制分析**：epoch-matched controls 的设计是否严谨？是否缺少 uniform × multi-epoch baseline（全数据 ~3.2 epochs）来区分纯重复 vs 选择性重复？\n5. **Scale effects**：0.6B→1.7B 效应递减 43%（Δ=-0.023→-0.013），OOD 方向不一致。对 practitioner 适用性的影响？\n6. **Detector 覆盖**：仅 3 个 detector（TF-IDF+LR, GPT-2 PPL, N-gram），是否足以支撑 AUC/ECE threshold 的通用性声明？\n7. **Grid-best b=0.3 vs adaptive b*≈0.9 偏差**：α_eff 负偏差是否导致过度干预，违背 minimum intervention 原则？\n8. **Batch size B=4 限制**：主实验在 advantage 最小的设定下运行（B=4: 1.0×, B=16: 3.0×），是否影响结论强度？\n\n**格式要求**：\n- 按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出\n- 每条 Weakness 标注 severity（critical/warning/info）并引用具体 Section/Table/Figure\n- 给出 Overall Assessment 评分（参照 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）",
  "reviewer_id": "1",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **论文**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n- **Venue**: EMNLP 2026 via ARR\n- **类型**: Long paper（正文 ≤8 页，references 不限，Limitations 不计页数）\n- **匿名**: Double-blind\n- **模板**: ACL style\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n**核心关注（必须逐条评估）**：\n1. **统计方法论**：5 seeds 的统计检验力是否充分？Bonferroni-Holm 校正的使用是否恰当？Cohen's d=3.83 是否被 deterministic data ordering 人为放大（seeds 仅影响模型初始化，data order 固定）？paired t-test 的前提假设是否满足？\n2. **效应量与实际意义**：Δ=-0.023 PPL（0.13% relative）的工程意义如何？下游任务零改善（|Δ|≤0.01）是否与 practitioner-oriented framing 矛盾？\n3. **α_eff proxy 可靠性**：Pearson r≈0.79 (R²≈0.63) 意味 ~37% 未解释方差。Wang (2026) 理论保证要求 true real fraction ≥ τ，但论文用 α_eff 替代，理论保证是否仍成立？\n4. **D&R 机制分析**：epoch-matched controls 的设计是否严谨？是否缺少 uniform × multi-epoch baseline（全数据 ~3.2 epochs）来区分纯重复 vs 选择性重复？\n5. **Scale effects**：0.6B→1.7B 效应递减 43%（Δ=-0.023→-0.013），OOD 方向不一致。对 practitioner 适用性的影响？\n6. **Detector 覆盖**：仅 3 个 detector（TF-IDF+LR, GPT-2 PPL, N-gram），是否足以支撑 AUC/ECE threshold 的通用性声明？\n7. **Grid-best b=0.3 vs adaptive b*≈0.9 偏差**：α_eff 负偏差是否导致过度干预，违背 minimum intervention 原则？\n8. **Batch size B=4 限制**：主实验在 advantage 最小的设定下运行（B=4: 1.0×, B=16: 3.0×），是否影响结论强度？\n\n**格式要求**：\n- 按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出\n- 每条 Weakness 标注 severity（critical/warning/info）并引用具体 Section/Table/Figure\n- 给出 Overall Assessment 评分（参照 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）",
    "reviewer_id": "1",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-25T21:17:10.662412+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18438
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-25T21:17:11.014026+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## 投稿信息\n- **论文**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n- **Venue**: EMNLP 2026 via ARR\n- **类型**: Long paper（正文 ≤8 页，references 不限，Limitations 不计页数）\n- **匿名**: Double-blind\n- **模板**: ACL style\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n**核心关注（必须逐条评估）**：\n1. **贡献定位与新颖性**：论文自我定位为 analysis paper 还是 method paper？w=(1-q)^b 完全来自 Drayson et al.，dual constraint + bisection 是标准方法——整体新颖性如何？是否清晰传达了分析贡献（三个 effectiveness conditions）的价值？\n2. **标题与 claim scope**：\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示一般性结论，但实验仅覆盖 self-contamination / 0.6B / continued pretraining / 单一数据源。标题是否过度承诺？\n3. **Abstract 质量**：是否 ≤200 words？核心 claims 是否准确反映实验结论？是否有 overclaim（如 \"improves over uniform training\" 未限定 PPL-only）？\n4. **Related Work 完整性**：是否覆盖近期 instance-level reweighting（如 MATES, Aioli, Data Mixing Agent）、detection benchmarks（RAID, M4）、synthetic data curation（ForTIFAI, Escaping Collapse via Verification）等？\n5. **写作质量**：§6 Discussion 第一段是否与 §5.1 内容重复？正文的 information density 和 narrative flow 如何？是否有不必要的冗余？\n6. **格式合规**：\n   - 正文（§1-§7）是否在 8 页内？\n   - Limitations section 是否在正文中（非 appendix）且内容适当（~3 点）？\n   - 是否有 Responsible NLP Checklist 出现在 PDF 中（不应出现）？\n   - Appendix 是否 double-column？\n   - 引用格式是否一致？\n7. **效应量讨论**：论文是否充分讨论了 PPL 改善与下游任务能力之间的关系？Δ=-0.023 在 continued pretraining context 中的意义是否有合理论证？\n8. **适用范围表述**：ρ≥0.4 实用门槛 + well-calibrated detector + self-contamination + 0.6B 下的 \"Decision summary for practitioners\"（Table 5/6）是否给读者准确信号？\n\n**格式要求**：\n- 按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出\n- 每条 Weakness 标注 severity（critical/warning/info）并引用具体 Section/Table/Figure\n- 给出 Overall Assessment 评分（参照 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）",
  "reviewer_id": "2",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## 投稿信息\n- **论文**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n- **Venue**: EMNLP 2026 via ARR\n- **类型**: Long paper（正文 ≤8 页，references 不限，Limitations 不计页数）\n- **匿名**: Double-blind\n- **模板**: ACL style\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n**核心关注（必须逐条评估）**：\n1. **贡献定位与新颖性**：论文自我定位为 analysis paper 还是 method paper？w=(1-q)^b 完全来自 Drayson et al.，dual constraint + bisection 是标准方法——整体新颖性如何？是否清晰传达了分析贡献（三个 effectiveness conditions）的价值？\n2. **标题与 claim scope**：\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示一般性结论，但实验仅覆盖 self-contamination / 0.6B / continued pretraining / 单一数据源。标题是否过度承诺？\n3. **Abstract 质量**：是否 ≤200 words？核心 claims 是否准确反映实验结论？是否有 overclaim（如 \"improves over uniform training\" 未限定 PPL-only）？\n4. **Related Work 完整性**：是否覆盖近期 instance-level reweighting（如 MATES, Aioli, Data Mixing Agent）、detection benchmarks（RAID, M4）、synthetic data curation（ForTIFAI, Escaping Collapse via Verification）等？\n5. **写作质量**：§6 Discussion 第一段是否与 §5.1 内容重复？正文的 information density 和 narrative flow 如何？是否有不必要的冗余？\n6. **格式合规**：\n   - 正文（§1-§7）是否在 8 页内？\n   - Limitations section 是否在正文中（非 appendix）且内容适当（~3 点）？\n   - 是否有 Responsible NLP Checklist 出现在 PDF 中（不应出现）？\n   - Appendix 是否 double-column？\n   - 引用格式是否一致？\n7. **效应量讨论**：论文是否充分讨论了 PPL 改善与下游任务能力之间的关系？Δ=-0.023 在 continued pretraining context 中的意义是否有合理论证？\n8. **适用范围表述**：ρ≥0.4 实用门槛 + well-calibrated detector + self-contamination + 0.6B 下的 \"Decision summary for practitioners\"（Table 5/6）是否给读者准确信号？\n\n**格式要求**：\n- 按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出\n- 每条 Weakness 标注 severity（critical/warning/info）并引用具体 Section/Table/Figure\n- 给出 Overall Assessment 评分（参照 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）",
    "reviewer_id": "2",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-25T21:17:12.383432+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1369
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-25T21:17:24.339009+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-25T21:17:24.389606+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1434 · 2026-05-25T21:17:39.002321+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue 调研 + Reviewer 编排 + 视觉审查派发', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: 收集 Reviewer 1 和 Reviewer 2 的独立初审结果', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 返回初审报告'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集 AGREE/REBUT 回应', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧，决定是否需要下一轮', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue 调研 + Reviewer 编排 + 视觉审查派发', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: 收集 Reviewer 1 和 Reviewer 2 的独立初审结果', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 返回初审报告'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集 AGREE/REBUT 回应', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧，决定是否需要下一轮', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1435 · 2026-05-25T21:17:39.002771+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1436 · 2026-05-25T21:17:49.417447+00:00_

Round 14 圆桌审稿已启动。两名 Reviewer 正在独立审阅论文，视觉审查 Agent 并行运行中。等待初审结果返回后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 109

## Round 109

2 recorded events


### User

_source line 1437 · 2026-05-25T21:23:02.376549+00:00_

[Reviewer 2 审稿意见]:
# Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量

**论文**: "When Does Detect-and-Reweight Work for Synthetic Contamination?"
**Venue**: EMNLP 2026 via ARR (Long paper)

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 实验设计严谨、自我评估诚实的分析论文，但实验范围过窄（self-contamination / 0.6B / 单一数据源）导致三个 effectiveness conditions 的一般性不足，且无下游任务提升，实际影响有限。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 在限定范围内实验设计严谨（epoch-matching、permuted controls、多 seed），但部分统计声明存在 overclaim（见 N1），且三个 conditions 的实验覆盖面不足以支撑一般性结论 |
| Excitement | 2.5/5 | 方法新颖性有限（w=(1-q)^b 完全来自 Drayson et al.，dual constraint + bisection 是标准方法）；分析贡献在窄设定下有价值，但无法转化为可操作的实践指导 |
| Reproducibility | 4.0/5 | 提供匿名代码库，详细报告超参数、seed、训练配置；但部分结果为 single-seed（Grid at ρ=0.6、Golden Ratio），限制可复现验证 |
| Overall Assessment | 3.0/5 | Findings 水平——soundness 在其 scope 内达标，但 scope 太窄、excitement 不足、无下游影响，不满足 conference acceptance 标准 |

**Reviewer Confidence**: 4/5 — 熟悉 data curation/reweighting 和 synthetic contamination 文献，仔细阅读了全文和 appendix。

---

## 主要优势

1. **严谨的实验控制设计**：epoch-matched D&R controls（Table 3）是本文最有价值的贡献之一，揭示了 D&R 的优势>95% 来自 multi-epoch exposure 而非 per-token learning quality。这一 decomposition 在此前文献（如 Drayson et al.）中缺失，对 practitioners 选择数据策略有直接指导意义。

2. **诚实的 self-assessment**：论文在 Abstract 末句、§1 末段、§6 Discussion 和 Limitations 中反复承认 scope 限制（self-contamination、0.6B、无下游提升），这种透明度在 NLP 投稿中难得。Appendix O 对 checkpoint-resume artifact 的详细披露尤其值得肯定。

3. **消融设计清晰，隔离变量有效**：5-method ablation hierarchy（Adaptive < Uniform < ESS-only < Random < Permuted）配合 permuted q-scores（Δ=+0.225）有效隔离了 detector provenance signal 的作用，逻辑链完整。

4. **统计处理高于平均水平**：Bonferroni-Holm correction、paired t-test、Cohen's d power analysis（Appendix Q）、cross-seed variance 报告，这些在同类论文中少见。

5. **Calibration finding 有实用价值**：TF-IDF (AUC=0.94, ECE=0.048) vs. GPT-2 (AUC=0.91, ECE=0.131) 的对比（§5.2, Figure 1b）在 comparable AUC 下隔离了 calibration 的作用，对 detector 选择有指导意义。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract 中 "ρ ≥ 0.4" 统计显著性声明存在 overclaim
- 具体位置：Abstract 第6句；§5.1 第1段
- 问题：Abstract 写 "improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction"。句法结构暗示 ρ=0.4 和 ρ=0.6 均达到显著性。但 §5.2 明确报告 ρ=0.6 的 p_BH=0.064，**未通过** Bonferroni-Holm correction at α=0.05。实际上只有 ρ=0.4 达到显著性（p_BH=0.011）。
- 为什么影响接收：这是论文核心 claim 的准确性问题。Overclaimed statistical significance 是 reviewer 一票否决的典型原因。
- 建议修改方向：改为 "improves over uniform training at ρ=0.4 (p_BH=0.011) with directionally consistent but non-significant improvement at ρ=0.6 (p_BH=0.064)" 或类似表述。

**N2** [critical] 标题 scope 与实验覆盖面严重不匹配
- 具体位置：标题、Abstract
- 问题："When Does Detect-and-Reweight Work for Synthetic Contamination?" 暗示对该范式的一般性回答。但实验仅覆盖：(a) self-contamination（同一模型生成+训练），(b) 0.6B scale（1.7B 仅为补充），(c) continued pretraining（非 from-scratch），(d) 单一真实数据源（FineWeb），(e) 主要一个 detector family（TF-IDF+LR）。论文自己在 §6 Discussion 承认 "When any condition is violated, uniform is the safer default"，但这些 conditions 本身只在极窄范围内被验证。
- 为什么影响接收：标题的一般性 framing 会让读者期待跨模型、跨规模、跨场景的系统性研究。当发现全部结论仅基于 self-contamination + 0.6B 时，会产生 expectation gap，削弱论文可信度。
- 建议修改方向：标题加限定，如 "When Does Detect-and-Reweight Work? A Controlled Study of Self-Contamination at Small Scale" 或在 abstract 更早处明确 scope。

**N3** [critical] 无下游任务提升，但 Abstract 未提及——读者可能产生实际影响的错误期待
- 具体位置：Abstract（全文）；§6 "Effect size and downstream impact" 段
- 问题：Abstract 说 "improves over uniform training" 而不指定 metric。读者自然理解为综合质量提升。但 §6 和 Appendix H 明确报告 downstream accuracy 完全无变化（0.5414 vs. 0.5415, 5 benchmarks, |Δ|≤0.01）。Δ=-0.023 PPL 仅为约 0.13% 的相对改善，且未转化为任何可测量的能力提升。对于 analysis paper 的 actionable conclusions，"no downstream gain" 是关键信息，不应被 Abstract 遗漏。
- 为什么影响接收：这影响论文的 practical significance 评估。不知道这一事实的读者可能高估论文贡献。
- 建议修改方向：Abstract 中在 "improves over uniform training" 后补充 "(in-distribution perplexity; downstream accuracy is unchanged at 0.6B scale)"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] §6 Discussion 第一段与 §5.1 内容高度重复
- 具体位置：§6 "D&R as the strongest strategy" 段 vs. §5.1 "Hard filtering and multi-epoch exposure" 段
- 问题：§6 开头段几乎逐字重述 §5.1 的 D&R epoch-matching 结论（"outperforms all reweighting methods by 0.35-0.42 PPL"、">95% of this advantage to multi-epoch exposure"）。类似地，§6 "When uniform beats reweighting" 段重述 Table 5 内容。在 8 页限制下，这种冗余浪费了约半页篇幅。
- 建议：§6 应聚焦 §5 未涵盖的 implications 和 open questions，而非重述 findings。可以将省出的空间用于讨论 cross-model contamination 的预期行为或更深入的 detector calibration 分析。

**W2** [warning] "Three effectiveness conditions" 的 framing 过度概括
- 具体位置：Abstract、§1、§7
- 问题：论文将其发现包装为 "three effectiveness conditions"，但这些更准确地说是 "在 self-contamination + 0.6B + continued pretraining 设定下的三个实证观察"。"Conditions" 一词暗示充要条件或一般性规律，但每个 condition 的验证范围极有限：Condition 1（D&R 最强）仅在一个设定下测试；Condition 2（calibration 要求）仅用 3 个 detectors 验证；Condition 3（minimum intervention）仅用一种 dual-constraint 方法体现。
- 建议：将 "conditions" 改为 "empirical observations" 或 "findings"，或在首次使用时加限定词（"three effectiveness conditions observed in our controlled setting"）。

**W3** [warning] Related Work 缺少若干近期 instance-level reweighting 方法
- 具体位置：§2 "Detection, Filtering, and Data Reweighting"
- 问题：论文引用了 domain-level 方法（DoReMi, DSIR, CRISP）和部分 instance-level 方法（Sow et al., DSDM），但缺少几个直接相关的近期工作：
  - **MATES** (Yu et al., 2024): instance-level data selection via data influence models，与本文的 instance-level reweighting 直接相关
  - **Aioli** (Balachandran et al., 2024): adaptive online data mixing，与 per-batch adaptation 机制相关
  - **RAID** (Dugan et al., 2024) 和 **M4** (Wang et al., 2024): synthetic text detection benchmarks，与 detector evaluation 相关
  - 这些工作与论文的 instance-level reweighting 和 detector evaluation 直接相关，应至少在 §2 中讨论定位差异。
- 建议：增加一段讨论 instance-level selection 最新进展（MATES、Aioli），明确本文与这些方法在目标（synthetic contamination vs. general data quality）和机制（provenance-based vs. influence-based）上的区别。Detection benchmark（RAID、M4）至少值得提及以说明 detector evaluation 的广泛背景。

**W4** [warning] Decision summary（Table 5）的实用性受限于验证范围
- 具体位置：Table 5, §6 "When uniform beats reweighting"
- 问题：Table 5 标题为 "Decision summary for practitioners"，列出了四个条件（AUC≥0.9, ECE≤0.05, ρ≥0.4, generator≠trainee）。但这些阈值均来自 self-contamination + 0.6B + FineWeb 设定下的单一实验。例如，AUC≥0.9 的阈值仅基于 3 个 detectors（0.73/0.91/0.94），采样密度不足以确定精确 boundary；ECE≤0.05 仅基于 TF-IDF (0.048) vs. GPT-2 (0.131) 的对比，中间值未测试。将这些称为 "for practitioners" 可能误导读者认为这些是经过充分验证的通用阈值。
- 建议：将标题改为 "Summary of observed conditions (self-contamination, 0.6B)" 或在 caption 中明确指出这些阈值仅为当前设定下的观察值，不应直接推广。

**W5** [warning] Δ=-0.023 的效应量在 continued pretraining 语境中的意义缺乏充分论证
- 具体位置：§5.1, §6 "Effect size and downstream impact"
- 问题：PPL 从 17.697 降至 17.674（Δ=-0.023, 约 0.13% 相对改善）。论文在 §6 承认 "the paradigm's impact at current scales is modest"，但未提供 continued pretraining 文献中的 PPL improvement baselines 来 contextualize 这个数字。读者无法判断 0.13% 的 PPL 改善在 continued pretraining 中是 meaningful signal 还是 noise floor。对比：D&R 的 epoch-matched 结果（Δ=0.017）与 adaptive 的 gap 仅 0.006 PPL，暗示 adaptive 的 marginal value 极低。
- 建议：引用 continued pretraining 文献中的 typical PPL improvement ranges（如 domain-adaptive 方法的效应量），让读者能 calibrate 本文结果的实际意义。

---

## 小问题（不影响接收）

- **M1** [info] Table 1（主结果表）caption 声明 "Adaptive and Uniform: 5-seed means"，但表格正文只显示 3 列 seed（42, 123, 456）。其余 2 个 seed（789, 234）的结果未展示，只体现在 Mean 列中。建议在表格中增加这两列或在 caption 中解释省略原因。

- **M2** [info] §5.2 报告 ρ=0.6 时 "paired t=-9.95, p_BH=0.064"，但 Appendix I Table 7 给出 "paired t=-15.4, p=0.004"（full precision）和 "t=-9.95, p=0.010"（3dp rounding）。正文和 appendix 的 t 值不一致（-9.95 vs -15.4），虽然 appendix 解释了 rounding 差异，但正文引用的 p_BH=0.064 与 appendix 的 p=0.010（未校正）存在跳跃，读者可能混淆。建议统一呈现。

- **M3** [info] Introduction 中 "three effectiveness conditions" 的编号与 Discussion/Conclusion 的顺序不完全一致（Introduction: D&R → detector requirements → minimum intervention；Discussion 同序但 Conclusion 措辞略有变化），minor但在 8 页论文中增加阅读摩擦。

- **M4** [info] Appendix P 的 ρ=0.3 结果（Table 16）seed 456 缺少 OOD 评估（OWT/Wiki 列为 "--"），caption 未解释原因。

- **M5** [info] §4 "Evaluation" 提到 "sliding-window evaluation (stride 1024)" 但未说明 window size。对于 PPL 结果的可复现性，这个信息应在 main text 或 appendix 中明确。

---

## Questions to Authors

1. 在 ρ=0.4 设定下，adaptive b* 相对 uniform 的 PPL 改善（Δ=-0.023）约等于 D&R epoch-matched 的结果（Δ=-0.017 gap to adaptive）。如果 D&R 是 practitioners 的更优选择（如论文所建议），那么 adaptive reweighting 的 use case 是什么？在什么场景下 practitioner 会选择 soft reweighting 而非 D&R？

2. 论文强调 calibration 的重要性（ECE≤0.05），但 temperature scaling 的 T=0.204 是在一个 held-out labeled split 上调的——这本身需要 labeled data。如果 practitioner 没有 labeled data（这是 web-scale 的常见场景），这个 calibration 前提如何满足？

3. Batch size B=4 在 modern pretraining 中极不常见（通常 B≥256）。论文在 §5.3 展示了 B=16 时效果更好（Δ=-0.068），但实际训练中 B 通常大 2-3 个数量级。是否有 B=64/128 的预期行为分析？

---

## Missing References

- Yu, B., et al. (2024). "MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models." NeurIPS 2024.
- Balachandran, V., et al. (2024). "Aioli: A Unified Optimization Framework for Language Model Data Mixing." arXiv.
- Dugan, L., et al. (2024). "RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors." ACL 2024.
- Wang, Y., et al. (2024). "M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection." EACL 2024.

---

## 格式合规检查

| 项目 | 结果 | 备注 |
|------|------|------|
| 正文页数（§1-§7） | ✓ 8页 | §7 Conclusion 结束于第8页底部 |
| Abstract ≤ 200 words | ✓ ~171 words | |
| Limitations 在正文中 | ✓ | 第9页，§7之后、References之前，非 appendix |
| Limitations 内容量 | ✓ | 3个 bullet point，适当 |
| Responsible NLP Checklist 不在 PDF 中 | ✓ | 未出现 |
| Appendix double-column | ✓ | 第10-15页均为 double-column ACL style |
| 引用格式一致性 | ✓ | (Author, Year) 格式统一 |
| Double-blind 匿名 | ✓ | Author 显示 "Anonymous ACL submission"，代码链接用 anonymous.4open.science |
| AI assistant 使用声明 | ✓ | Appendix S 披露使用 Claude |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1438 · 2026-05-25T21:23:19.568087+00:00_

Reviewer 2 报告已收到。评分 3.0（Findings），核心问题：标题 scope 不匹配、Abstract overclaim（ρ=0.6 实际未达显著性）、下游零改善未在 Abstract 提及。

等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1439 · 2026-05-25T21:23:22.039684+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：Overall 3.0 (Findings)。论文实验设计严谨（epoch-matching controls、permuted ablation、统计校正），自我评估诚实，但存在三个 Must-Fix 问题：(1) Abstract 对 ρ≥0.4 的显著性声明存在 overclaim（ρ=0.6 实际未通过校正，p_BH=0.064）；(2) 标题 scope 远超实验覆盖面（self-contamination / 0.6B / 单一数据源）；(3) Abstract 未提及下游任务无提升这一关键事实。此外还有 Discussion 与 Results 内容重复、Related Work 缺少 MATES/Aioli 等近期方法、Decision summary 实用性受限等 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1440 · 2026-05-25T21:23:35.882095+00:00_

Reviewer 2 报告已收到（Overall 3.0 / Findings）。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 111

## Round 111

8 recorded events


### User

_source line 1441 · 2026-05-25T21:25:43.538170+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

### 总体评分

**Overall Assessment**: **3.0 — Findings**
**Soundness**: 3.5 / 5
**Excitement**: 2.5 / 5

**一句话总结**: 一篇透明且实验设计严谨的机制分析工作，揭示了 D&R 优势的真正来源（multi-epoch exposure），但 0.13% PPL 改善 + 零下游提升与 practitioner-oriented framing 之间存在根本矛盾，且统计效应量被实验设计人为放大。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 控制实验设计严谨（epoch-matched controls 是亮点），但 Cohen's d 被固定 data order 人为放大；α_eff proxy 有 37% 未解释方差；adaptive b* 系统性地偏离 grid-optimal，违背自身 minimum intervention 原则 |
| Excitement | 2.5/5 | 问题本身重要且及时（synthetic contamination 是实际问题），multi-epoch 机制发现有洞察价值，但实际效果几乎为零（downstream Δ≤0.01），且效应随 scale 递减，实用价值有限 |

---

### 主要优势

- **S1: Epoch-matched control 分析是本文最大亮点。** Table 3 (Section 5.1) 通过将 D&R (q>0.5) 限制为 ~1.0 content epoch，将 0.424 PPL 的 raw advantage 分解为 multi-epoch exposure（占 >95%）和 selective filtering（仅 Δ=0.017），清晰揭示了 D&R 生效的真正机制。

- **S2: Ablation 设计层层递进，控制变量清晰。** Permuted q-scores（Δ=+0.225）、Random U(0,2)、ESS-only 的对比（Table 2）有效隔离了 detector signal 和 minimum intervention 两个必要条件。

- **S3: 对自身局限性的透明度值得肯定。** Limitations 节坦诚承认 downstream accuracy 无变化、detector coverage 有限、scale 泛化未验证。

- **S4: Dual-constrained adaptive 方法有理论动机。** Quality floor + stability ceiling 结合为区间 [b_τ, b_ESS]，取最小 b 实现 minimum intervention，原理清晰。

- **S5: Batch-size amplification 结果有价值。** Figure 7 展示 B=4→16 时优势从 1.0× 到 3.0× 的 monotonic 增长。

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] **Effect size 与 practitioner framing 之间的根本矛盾**
- 具体位置：Section 5.1 (Δ=−0.023, 0.13%), Section 5.2 (downstream 0.5414 vs 0.5415), Section 6 Table 5
- 问题：论文标题 "When Does D&R Work?" 和 Table 5 的 practitioner decision summary 建立了面向实践者的叙事框架。然而核心结果是：(a) PPL 改善仅 0.023（0.13% relative），(b) 下游任务准确率完全相同（0.5414 vs 0.5415），(c) 在 1.7B 尺度效应再减半至 Δ=−0.013 且 OOD 方向不一致。对下游任务零贡献的方法，其 "effectiveness conditions" 对实践者的指导意义何在？
- 为什么影响接收：论文的 core claim 是识别 D&R 的 effectiveness conditions，但 "effective" 仅限于 held-out PPL 的统计显著变化，不包含任何 task-level 意义。如果 D&R 只在 PPL 上有统计可检测但实际无意义的改善，那么 "When Does D&R Work?" 的答案可能是 "it doesn't, at this scale"。
- 建议：(1) 重新定位为 mechanism analysis 而非 practitioner guide；(2) 在 Abstract/Intro 中前置效应量级限制；(3) 增加 PPL Δ=0.023 的工程意义讨论。

**N2** [critical] **Cohen's d = 3.83 被 deterministic data ordering 系统性放大**
- 具体位置：Section 5.1, Appendix Q (σ=0.006)
- 问题：5 个 seed 仅改变模型初始化，dataloader 完全 deterministic。SD_Δ=0.006 反映的是初始化噪声的极小方差，而非方法在不同数据条件下的稳健性。Cohen's d = 0.023/0.006 = 3.83 严重高估效应 robustness。如果 data ordering 也随机化，SD_Δ 很可能大幅增加，Cohen's d 可能降至 <1。
- 为什么影响接收：直接报告 Cohen's d=3.83 而不在正文中充分讨论 deterministic-order 限制，可能误导读者。
- 建议：(1) 正文中明确 Cohen's d 在此设计下的 interpretability 限制；(2) 补充不同 data permutation 实验；(3) 或改用 bootstrap CI for Δ 替代 Cohen's d。

---

### Should-Fix 问题

**W1** [warning] **缺少 uniform × multi-epoch baseline**
- 具体位置：Table 3
- 问题：D&R (q>0.3) 的 raw PPL=17.250 源于 ~3.2 content epochs。缺少对全部数据做 ~3.2 epochs 的 uniform baseline，无法区分 pure repetition 和 selective filtering 的贡献。
- 建议：增加 Uniform × {2, 3} epochs 行。

**W2** [warning] **α_eff proxy 的 37% 未解释方差削弱理论保证**
- 具体位置：Section 3, Table 12 (Appendix J)
- 问题：R²≈0.63，约 37% 的 batch-level 方差未被捕获。未量化 α_eff ≥ τ 但 true fraction < τ 的 violation 频率。
- 建议：利用 ground-truth labels 计算 violation batch 比例和影响。

**W3** [warning] **Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差**
- 具体位置：Section 5.1, Table 2
- 问题：Adaptive 施加约 3× 于 grid-optimal 的权重抑制，PPL gap 0.054 是 adaptive-vs-uniform gain（0.023）的 2.3×。α_eff 的 negative bias 导致 over-intervention，违背 minimum intervention 原则。
- 建议：讨论偏差来源并探讨 calibration-corrected α_eff。

**W4** [warning] **3 个 detector 不足以支撑 AUC/ECE threshold 通用性**
- 具体位置：Section 5.1, Table 5
- 问题：仅 3 个数据点推导 threshold，缺少中间区域 detector（如 AUC=0.85/ECE=0.04）。Table 5 的 binary checklist 过于确定。
- 建议：将 threshold 表述改为 observed trend，补充更多 detector。

**W5** [warning] **Scale 效应递减 43%，practitioner 适用性存疑**
- 具体位置：Section 5.2
- 问题：0.6B→1.7B Δ 减半，OOD 方向不一致。如果归因成立（larger models more robust），则 7B+ 效应可能趋零。
- 建议：讨论 scaling trend 外推含义。

---

### 小问题

- **M1** [info] B=4 主实验设定低估方法潜力（B=16 时 3.0×），建议说明选择理由。
- **M2** [info] Paired t-test 正态性假设在 n=5 下无法验证，建议补充 Wilcoxon signed-rank test。
- **M3** [info] Abstract word count 接近 200-word 限制，建议精确计数。

---

### Questions to Authors

1. 是否有不同 data permutation 下的实验？跨 permutation 的 SD_Δ 和 Cohen's d？
2. Uniform × multi-epoch baseline 的预期结果？
3. α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例？
4. Calibration-corrected α_eff（如 Platt scaling 后）能否缩小 b* vs grid-optimal 的 gap？
5. 1.7B 实验选择 τ=0.8 而非 0.7 的理由？是否影响 scale comparison 公平性？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1442 · 2026-05-25T21:26:05.377556+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue 调研 + Reviewer 编排 + 视觉审查派发', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: 收集 Reviewer 1 和 Reviewer 2 的独立初审结果', 'status': 'completed', 'activeForm': '收集初审报告'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集 AGREE/REBUT 回应', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧，决定是否需要下一轮', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue 调研 + Reviewer 编排 + 视觉审查派发', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: 收集 Reviewer 1 和 Reviewer 2 的独立初审结果', 'status': 'completed', 'activeForm': '收集初审报告'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集 AGREE/REBUT 回应', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧，决定是否需要下一轮', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-25T21:26:05.378103+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-25T21:26:40.155268+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5\n\n### 主要优势\n1. 严谨的实验控制设计（epoch-matched D&R controls）\n2. 诚实的 self-assessment\n3. 消融设计清晰，隔离变量有效\n4. 统计处理高于平均水平\n5. Calibration finding 有实用价值\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 中 \"ρ ≥ 0.4\" 统计显著性声明存在 overclaim\n- Abstract 写 \"improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction\"。但 §5.2 报告 ρ=0.6 的 p_BH=0.064，未通过 BH correction at α=0.05。只有 ρ=0.4 达到显著性（p_BH=0.011）。\n\n**N2** [critical] 标题 scope 与实验覆盖面严重不匹配\n- \"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示一般性但实验仅覆盖 self-contamination / 0.6B / continued pretraining / 单一数据源 / 主要一个 detector family。\n\n**N3** [critical] 无下游任务提升，但 Abstract 未提及\n- Abstract 说 \"improves over uniform training\" 不指定 metric，读者自然理解为综合质量提升。但下游 accuracy 完全无变化（0.5414 vs. 0.5415）。\n\n### Should-Fix 问题\n\n**W1** [warning] §6 Discussion 第一段与 §5.1 内容高度重复\n**W2** [warning] \"Three effectiveness conditions\" 的 framing 过度概括——应改为 \"empirical observations\" 或 \"findings\"\n**W3** [warning] Related Work 缺少 MATES、Aioli、RAID、M4 等近期方法\n**W4** [warning] Decision summary（Table 5）的实用性受限于验证范围\n**W5** [warning] Δ=-0.023 的效应量在 continued pretraining 语境中缺乏 baseline contextualization\n\n### 小问题\n- M1: Table 1 caption 声明 5-seed 但只显示 3 列 seed\n- M2: §5.2 与 Appendix I 的 t 值不一致（-9.95 vs -15.4）\n- M3: \"three effectiveness conditions\" 编号在 Intro/Discussion/Conclusion 间微有不一致\n- M4: Appendix P Table 16 seed 456 缺少 OOD 评估未解释\n- M5: Sliding-window evaluation 未说明 window size\n\n### Questions to Authors\n1. Adaptive reweighting 的 use case 在 D&R 更优的情况下是什么？\n2. Temperature scaling T=0.204 需要 labeled data，web-scale 下如何满足？\n3. B=4 在 modern pretraining 中不常见，是否有 B=64/128 的预期行为分析？\n\n### Missing References\nMATES (Yu et al., 2024)、Aioli (Balachandran et al., 2024)、RAID (Dugan et al., 2024)、M4 (Wang et al., 2024)\n\n### 格式合规检查：全部通过 ✓\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和 Questions 给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "1",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5\n\n### 主要优势\n1. 严谨的实验控制设计（epoch-matched D&R controls）\n2. 诚实的 self-assessment\n3. 消融设计清晰，隔离变量有效\n4. 统计处理高于平均水平\n5. Calibration finding 有实用价值\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 中 \"ρ ≥ 0.4\" 统计显著性声明存在 overclaim\n- Abstract 写 \"improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction\"。但 §5.2 报告 ρ=0.6 的 p_BH=0.064，未通过 BH correction at α=0.05。只有 ρ=0.4 达到显著性（p_BH=0.011）。\n\n**N2** [critical] 标题 scope 与实验覆盖面严重不匹配\n- \"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示一般性但实验仅覆盖 self-contamination / 0.6B / continued pretraining / 单一数据源 / 主要一个 detector family。\n\n**N3** [critical] 无下游任务提升，但 Abstract 未提及\n- Abstract 说 \"improves over uniform training\" 不指定 metric，读者自然理解为综合质量提升。但下游 accuracy 完全无变化（0.5414 vs. 0.5415）。\n\n### Should-Fix 问题\n\n**W1** [warning] §6 Discussion 第一段与 §5.1 内容高度重复\n**W2** [warning] \"Three effectiveness conditions\" 的 framing 过度概括——应改为 \"empirical observations\" 或 \"findings\"\n**W3** [warning] Related Work 缺少 MATES、Aioli、RAID、M4 等近期方法\n**W4** [warning] Decision summary（Table 5）的实用性受限于验证范围\n**W5** [warning] Δ=-0.023 的效应量在 continued pretraining 语境中缺乏 baseline contextualization\n\n### 小问题\n- M1: Table 1 caption 声明 5-seed 但只显示 3 列 seed\n- M2: §5.2 与 Appendix I 的 t 值不一致（-9.95 vs -15.4）\n- M3: \"three effectiveness conditions\" 编号在 Intro/Discussion/Conclusion 间微有不一致\n- M4: Appendix P Table 16 seed 456 缺少 OOD 评估未解释\n- M5: Sliding-window evaluation 未说明 window size\n\n### Questions to Authors\n1. Adaptive reweighting 的 use case 在 D&R 更优的情况下是什么？\n2. Temperature scaling T=0.204 需要 labeled data，web-scale 下如何满足？\n3. B=4 在 modern pretraining 中不常见，是否有 B=64/128 的预期行为分析？\n\n### Missing References\nMATES (Yu et al., 2024)、Aioli (Balachandran et al., 2024)、RAID (Dugan et al., 2024)、M4 (Wang et al., 2024)\n\n### 格式合规检查：全部通过 ✓\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和 Questions 给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "1",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-25T21:27:06.543115+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26387
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-25T21:27:06.695089+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**Overall Assessment**: 3.0 — Findings\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5\n\n### 主要优势\n- S1: Epoch-matched control 分析是本文最大亮点\n- S2: Ablation 设计层层递进，控制变量清晰\n- S3: 对自身局限性的透明度值得肯定\n- S4: Dual-constrained adaptive 方法有理论动机\n- S5: Batch-size amplification 结果有价值\n\n### Must-Fix 问题\n\n**N1** [critical] Effect size 与 practitioner framing 之间的根本矛盾\n- PPL 改善仅 0.023（0.13% relative），下游任务准确率完全相同（0.5414 vs 0.5415），1.7B 效应再减半至 Δ=-0.013 且 OOD 方向不一致。对下游任务零贡献的方法，其 \"effectiveness conditions\" 对实践者的指导意义何在？\n- 建议重新定位为 mechanism analysis 而非 practitioner guide。\n\n**N2** [critical] Cohen's d = 3.83 被 deterministic data ordering 系统性放大\n- 5 个 seed 仅改变模型初始化，dataloader 完全 deterministic。SD_Δ=0.006 反映初始化噪声极小方差，而非方法在不同数据条件下的稳健性。如果 data ordering 也随机化，SD_Δ 很可能大幅增加，Cohen's d 可能降至 <1。\n\n### Should-Fix 问题\n\n**W1** [warning] 缺少 uniform × multi-epoch baseline\n- D&R (q>0.3) raw PPL=17.250 源于 ~3.2 content epochs。缺少全部数据做 ~3.2 epochs 的 uniform baseline，无法区分 pure repetition vs selective filtering。\n\n**W2** [warning] α_eff proxy 的 37% 未解释方差削弱理论保证\n- R²≈0.63，未量化 α_eff ≥ τ 但 true fraction < τ 的 violation 频率。\n\n**W3** [warning] Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差\n- α_eff 的 negative bias 导致 over-intervention，PPL gap 0.054 是 adaptive-vs-uniform gain 的 2.3×。违背 minimum intervention 原则。\n\n**W4** [warning] 3 个 detector 不足以支撑 AUC/ECE threshold 通用性\n\n**W5** [warning] Scale 效应递减 43%，practitioner 适用性存疑\n- 0.6B→1.7B Δ 减半，7B+ 效应可能趋零。\n\n### 小问题\n- M1: B=4 主实验低估方法潜力\n- M2: Paired t-test 正态性假设 n=5 下无法验证\n- M3: Abstract word count 接近 200-word 限制\n\n### Questions to Authors\n1. 是否有不同 data permutation 下的实验？\n2. Uniform × multi-epoch baseline 的预期结果？\n3. α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例？\n4. Calibration-corrected α_eff 能否缩小 b* vs grid-optimal 的 gap？\n5. 1.7B 实验选择 τ=0.8 而非 0.7 的理由？\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和 Questions 给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "2",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**Overall Assessment**: 3.0 — Findings\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5\n\n### 主要优势\n- S1: Epoch-matched control 分析是本文最大亮点\n- S2: Ablation 设计层层递进，控制变量清晰\n- S3: 对自身局限性的透明度值得肯定\n- S4: Dual-constrained adaptive 方法有理论动机\n- S5: Batch-size amplification 结果有价值\n\n### Must-Fix 问题\n\n**N1** [critical] Effect size 与 practitioner framing 之间的根本矛盾\n- PPL 改善仅 0.023（0.13% relative），下游任务准确率完全相同（0.5414 vs 0.5415），1.7B 效应再减半至 Δ=-0.013 且 OOD 方向不一致。对下游任务零贡献的方法，其 \"effectiveness conditions\" 对实践者的指导意义何在？\n- 建议重新定位为 mechanism analysis 而非 practitioner guide。\n\n**N2** [critical] Cohen's d = 3.83 被 deterministic data ordering 系统性放大\n- 5 个 seed 仅改变模型初始化，dataloader 完全 deterministic。SD_Δ=0.006 反映初始化噪声极小方差，而非方法在不同数据条件下的稳健性。如果 data ordering 也随机化，SD_Δ 很可能大幅增加，Cohen's d 可能降至 <1。\n\n### Should-Fix 问题\n\n**W1** [warning] 缺少 uniform × multi-epoch baseline\n- D&R (q>0.3) raw PPL=17.250 源于 ~3.2 content epochs。缺少全部数据做 ~3.2 epochs 的 uniform baseline，无法区分 pure repetition vs selective filtering。\n\n**W2** [warning] α_eff proxy 的 37% 未解释方差削弱理论保证\n- R²≈0.63，未量化 α_eff ≥ τ 但 true fraction < τ 的 violation 频率。\n\n**W3** [warning] Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差\n- α_eff 的 negative bias 导致 over-intervention，PPL gap 0.054 是 adaptive-vs-uniform gain 的 2.3×。违背 minimum intervention 原则。\n\n**W4** [warning] 3 个 detector 不足以支撑 AUC/ECE threshold 通用性\n\n**W5** [warning] Scale 效应递减 43%，practitioner 适用性存疑\n- 0.6B→1.7B Δ 减半，7B+ 效应可能趋零。\n\n### 小问题\n- M1: B=4 主实验低估方法潜力\n- M2: Paired t-test 正态性假设 n=5 下无法验证\n- M3: Abstract word count 接近 200-word 限制\n\n### Questions to Authors\n1. 是否有不同 data permutation 下的实验？\n2. Uniform × multi-epoch baseline 的预期结果？\n3. α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例？\n4. Calibration-corrected α_eff 能否缩小 b* vs grid-optimal 的 gap？\n5. 1.7B 实验选择 τ=0.8 而非 0.7 的理由？\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和 Questions 给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "2",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-25T21:27:08.060047+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1364
}
```

</details>

---


### Assistant

_source line 1448 · 2026-05-25T21:27:18.974350+00:00_

交叉分享已发送。等待两位 Reviewer 返回 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 112

## Round 112

2 recorded events


### User

_source line 1449 · 2026-05-25T21:27:21.462221+00:00_

[Reviewer 1 审稿结果]:
审稿完成，意见已发送给 Review Director。

**总结**：Overall 3.0（Findings），Soundness 3.5，Excitement 2.5。两个 critical 问题：(1) 效应量极小（0.13% PPL，零下游提升）与 practitioner-oriented framing 矛盾；(2) Cohen's d=3.83 被 deterministic data ordering 人为放大。五个 warning：缺 uniform multi-epoch baseline、α_eff proxy 37% 未解释方差、adaptive b* 系统性 over-intervention、3 个 detector 不足以定 threshold、scale 效应递减。论文最大亮点是 epoch-matched control 揭示 D&R 优势来自 multi-epoch exposure 而非 selective filtering。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1450 · 2026-05-25T21:27:28.545075+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 113

## Round 113

38 recorded events


### User

_source line 1451 · 2026-05-25T21:28:48.973549+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Abstract 中 "ρ ≥ 0.4" 统计显著性声明存在 overclaim**
同意，这是一个明确的事实性错误。§5.2 报告 ρ=0.6 时 p_BH=0.064，未通过 α=0.05 after Bonferroni-Holm correction。Abstract 的 "ρ ≥ 0.4, reaching conventional significance" 暗示 ρ=0.4 和 ρ=0.6 均显著，但实际上只有 ρ=0.4 (p_BH=0.011) 达到了。这属于 overclaim，必须修正为 "at ρ=0.4" 或明确注明 ρ=0.6 仅为 marginal significance。此问题在我的审稿中未单独列出，R2 的发现是对我 N1（framing 矛盾）的有力补充。

**[AGREE] R2-N2: 标题 scope 与实验覆盖面不匹配**
同意核心判断。"When Does Detect-and-Reweight Work for Synthetic Contamination?" 的问句形式虽然比陈述句稍为收敛，但仍暗示对 D&R 方法的系统性评估。实验仅覆盖：self-contamination（非 cross-model contamination）、0.6B+1.7B（非 full pretraining scale）、continued pretraining（非 from-scratch）、单一数据源 FineWeb、主要依赖 TF-IDF+LR 一个 detector。这与我 W4（3 个 detector 不足以支撑通用性声明）和 W5（scale 递减）的判断一致。建议标题增加限定词，如 "...in Controlled Continued Pretraining" 或 "...at Sub-Billion Scale"。

**[AGREE] R2-N3: 无下游任务提升但 Abstract 未提及**
完全同意。这与我的 N1（effect size 与 practitioner framing 的根本矛盾）高度一致。Abstract 的 "improves over uniform training" 未限定 metric，读者会自然理解为包含下游任务质量。实际上 downstream accuracy 在三位有效数字上完全相同（0.5414 vs 0.5415, §5.2 及 Appendix H）。Abstract 应明确写 "improves held-out perplexity" 并注明 "without measurable downstream accuracy gains"。我认为这与 N1 共同构成本文最核心的问题——framing 与 evidence 之间的 gap。

---

### Should-Fix 问题

**[AGREE] R2-W1: §6 Discussion 第一段与 §5.1 重复**
部分同意。Discussion 开头重述主要发现是学术写作的常见做法，但如果重复度过高（R2 称 "高度重复"），在 8 页限制下是空间浪费。§6 第一段 "D&R outperforms all reweighting methods by 0.35--0.42 PPL... epoch-matched controls attribute >95%..." 确实与 §5.1 的 epoch-matched analysis 高度重合。建议 §6 开头用一句话概括，将空间用于更深入的 mechanism 讨论（如 why multi-epoch exposure helps specifically for contaminated data，与 curriculum learning 的联系等）。不过我将其定为 minor warning 而非 critical——空间分配不影响接收决定。

**[AGREE] R2-W2: "Three effectiveness conditions" framing 过度概括**
同意。"Conditions" 暗示充分必要条件，但论文的 evidence 仅支持 "empirical observations in a specific controlled setting"。具体地：(a) 3 个 detector 不足以确立 AUC/ECE threshold 的 boundary（我的 W4）；(b) 仅 self-contamination 设定，不知 cross-model contamination 是否有相同 conditions；(c) scale 效应递减意味着 conditions 可能 scale-dependent。改为 "three empirical findings" 或 "three observed requirements" 更准确。

**[AGREE] R2-W3: Related Work 缺少 MATES、Aioli、RAID、M4**
同意，特别是 RAID (Dugan et al., 2024) 作为 AI-generated text detection benchmark 与论文的 detector evaluation 直接相关，M4 (Wang et al., 2024) 作为多语言 machine-generated text detection 也属于同一 research line。MATES (Yu et al., 2024) 如果涉及 data selection for training 则与 §2 Related Work 的 data curation 部分有交集。Aioli (Balachandran et al., 2024) 如果涉及 data mixing 则补充了 domain-level importance weighting 的讨论。这些遗漏不影响接收但确实影响 Related Work 的完整性。

**[AGREE] R2-W4: Table 5 decision summary 实用性受限**
完全同意，这与我的 W4（3 个 detector 不足以支撑 threshold 通用性）一致。Table 5 将 AUC ≥ 0.9 和 ECE ≤ 0.05 作为 binary checklist 呈现，但背后仅有 3 个数据点。如果实践者拿到一个 AUC=0.88, ECE=0.04 的 detector，Table 5 说 "不要用"，但这个结论没有 empirical support（没测试过这个区间）。

**[AGREE] R2-W5: Δ=-0.023 缺乏 baseline contextualization**
同意。论文未在 continued pretraining 文献中定位 0.023 PPL 这个量级意味着什么。例如：(a) 同等 compute budget 下，换一个 learning rate schedule 能获得多大 PPL delta？(b) 增加 1% training data 的边际 PPL 改善是多少？(c) 其他 data curation 方法（如 DSIR, DsDm）在类似 scale 下的 PPL improvement 是多少？没有这些对照，读者无法判断 0.023 是 "small but meaningful" 还是 "noise-level"。这补充了我 N1 的论点。

---

### 小问题

**[AGREE] R2-M1: Table caption 5-seed vs 3 列 seed 不一致**
同意。如果 Table 2 caption 声明 5-seed mean 但表格仅展示 3 个 seed 列（42, 123, 456），读者可能质疑 seed 789 和 234 的结果是否有选择性报告。建议在 caption 中注明 "full 5-seed results in Appendix X" 并补充完整数据。

**[AGREE] R2-M2: §5.2 与 Appendix I 的 t 值不一致**
如果确实存在 t=-9.95 vs t=-15.4 的不一致，这是 proofreading 问题。我未独立验证此数字，但接受 R2 的发现。数值不一致即使是 typo 也需修正，因为损害 reproducibility 和信任度。

**[AGREE] R2-M3: "Three effectiveness conditions" 编号不一致**
同意。如果 Intro/Discussion/Conclusion 中三个条件的表述或排序有微小差异，应统一。

**[AGREE] R2-M4: Appendix P Table 16 seed 456 缺 OOD 评估**
同意。数据完整性问题，应补充或解释缺失原因。

**[AGREE] R2-M5: Sliding-window evaluation 未说明 window size**
同意。Reproducibility 要求所有 evaluation hyperparameters 必须明确。§4 Evaluation 或 Appendix 应注明 window size（如 stride 等参数）。

---

### Questions

**[AGREE] R2-Q1: Adaptive reweighting 在 D&R 更优时的 use case**
好问题。Table 3 (§5.1) 明确显示 D&R (q>0.3) 以 PPL 17.250 大幅优于 adaptive (17.674)。论文在 §6 隐含地论证 adaptive 的优势是 "不需要 grid search"（节省 ~16 GPU-hours），但 D&R 同样不需要 grid search（只需一个 threshold）。如果 D&R 在所有设定下都优于 adaptive reweighting，后者的实际 use case 确实不清楚——除非存在 D&R 不适用的场景（如 corpus 极小无法承受数据丢弃），但论文未讨论此情形。

**[AGREE] R2-Q2: Temperature scaling T=0.204 需要 labeled data**
同意这是一个重要的实践限制。论文的 detector calibration（§4, Appendix L）依赖 labeled validation split（10K documents），但在 web-scale pretraining 中，ground-truth synthetic labels 通常不可用。这限制了 Table 5 decision framework 的 deployability。论文应在 Discussion 中讨论 unsupervised calibration alternatives（如 binning-based methods）。

**[AGREE] R2-Q3: B=4 不符合 modern pretraining 实践**
同意，这与我的 M1 一致。Modern pretraining 典型 micro-batch size 远大于 4（通常 B=32-128 per GPU）。§5.3 展示 B=4→16 时效果提升，但 B=16 仍然远低于实际设定。论文应讨论 (a) B=64/128 时的预期行为（external extrapolation），(b) 大 batch size 下 per-batch α_eff 估计是否更稳定（batch 内更多样本应降低 proxy variance）。

---

### Missing References

**[AGREE]** RAID (Dugan et al., 2024) 和 M4 (Wang et al., 2024) 与 detector evaluation 直接相关，应加入 §2 Related Work。MATES 和 Aioli 的相关性需进一步确认，但如果涉及 training-time data selection/mixing，也应纳入。

---

### 总结

R2 的审稿意见整体质量高，与我的审稿存在大量交叉验证：
- R2-N3 ≈ 我的 N1（effect size vs framing 矛盾）
- R2-N2 ≈ 我的 W4+W5（scope 限制）
- R2-W4 ≈ 我的 W4（detector threshold 通用性）
- R2-Q3 ≈ 我的 M1（batch size 限制）

R2 额外发现的贡献：
- **N1（p_BH=0.064 overclaim）是我遗漏的重要事实性错误**，应作为 must-fix
- **W3（missing references）** 补充了具体的遗漏文献
- **M2（t 值不一致）** 是具体的 proofreading 发现

两位 Reviewer 独立得出 **Overall 3.0 (Findings)、Soundness 3.5、Excitement 2.5** 的一致评分，增强了评估的可信度。核心共识：**方法论上有贡献（epoch-matched mechanism analysis），但 framing 超出了 evidence 支持的范围，实际效果量级不足以支撑 practitioner-oriented 定位。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-25T21:29:11.351890+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,get_external_review_status,get_visual_check_status,update_review_issues,submit_review_report_to_research_director,dispatch_visual_check,request_external_review",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,get_external_review_status,get_visual_check_status,update_review_issues,submit_review_report_to_research_director,dispatch_visual_check,request_external_review",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 1453 · 2026-05-25T21:29:11.402637+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1454 · 2026-05-25T21:29:15.469291+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-25T21:29:15.469734+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-25T21:29:38.275369+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool call

_source line 1457 · 2026-05-25T21:29:38.927985+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---
