---
round: 16
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T01:35:47.285217+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 18 (Fresh Review)

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewer 编排**: R1 (方法严谨性 + 实验验证) + R2 (新颖性 + Related Work + 写作 + 格式)

---

## Summary

本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor（75.9M params, &lt;1% base），配合 Gumbel-Sigmoid relaxation 和 adaptive penalty controller。核心发现：KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，在 LLaMA-3.1-8B 上 PPL 减少 14.5%（matched sparsity）。Target-swap ablation (C1) 确认 mask quality 而非 training objective 本身驱动推理质量。跨架构评估覆盖 Mistral-7B 和 Qwen-2.5-14B，论文自定位为 "primarily empirical study"。

---

## Strengths

**S1. C1 Target-Swap Ablation 设计精巧 [R1, R2 共识]** — Table 3 通过让 BCE predictor 使用 KL-derived oracle masks，干净地解耦了 mask quality 与 gradient coupling 的贡献。50% sparsity 下 max Δ≤0.79pp (s42)，30% 下 3 seed 一致性 ≤1.70pp。在 activation sparsity 领域中这种实验设计较为少见，为 "mask quality drives inference quality" 提供了有说服力的因果证据。

**S2. 消融覆盖面广且系统性强 [R1, R2 共识]** — Table 4 系统对比 divergence 类型（forward KL/JSD/reverse KL）、relaxation 方法（Gumbel vs STE）、loss isolation（BCE+Gumbel vs BCE）。Appendix 17 个 section 覆盖 bottleneck 敏感性、OOD 评估、training stability、SNR 分析等。实验透彻度超过同领域大多数工作。

**S3. 诚实的结果报告与自我定位 [R1, R2 共识]** — 明确报告 MMLU −5.2pp、Qwen-14B GSM8K −20pp、50% 下游 capacity cliff。自承 "primarily empirical study"，降低期望校准成本。

**S4. 二维 Taxonomy 有组织价值 [R1, R2 共识]** — Table 1 沿 correction granularity × training signal coupling 组织先前工作，定位清晰。

**S5. Multi-seed 评估 + 多架构验证 [R1, R2 共识]** — 关键结论均 3-seed 评估；覆盖 3 个模型家族 (7B-14B)。

---

## Weaknesses

### Must-Fix (Critical)

**W1. 方法论新颖性有限，与 MaskLLM 核心配方重合 [R2 主导，R1 partial agree]**
核心训练配方（frozen backbone + learnable masks + KL divergence + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文声称的三点区别——activation vs weight sparsity, dynamic vs static masks, predictor vs learnable parameters——均为 application-level differences 而非 methodological innovation。论文未讨论关键 counterfactual：将 MaskLLM 策略直接迁移到 activation sparsity 是否足以复现核心结果。作为 "primarily empirical study"，novelty 可达 Findings bar，但对 main conference 缺乏方法论或理论层面的新贡献。

**W2. 无实际推理加速，Introduction framing 仍存在张力 [R1, R2 共识]**
Appendix A Table 6 实测显示 KL pipeline 增加 6.4% 延迟（126.78 vs 119.11 ms/fwd）。论文承认 unstructured masks 无 wall-clock speedup，且 Introduction §1 已声明 "primarily empirical study" + "Wall-clock speedup requires sparse kernel support not addressed here"，但开篇仍以 "SwiGLU FFNs exhibit high contextual sparsity" 建立 efficiency 动机，framing 张力尚未完全消解。

**W3. Knowledge-intensive tasks 系统性退步，跨模型一致 [R1, R2 共识]**
MMLU: KL 40.7% vs TEAL 45.9% (−5.2pp, LLaMA-8B 30%); Qwen-14B: GSM8K 32.1±5.2% vs TEAL 52.1% (−20pp); Mistral-7B: GSM8K reversed across all seeds。三个模型上 knowledge-intensive tasks 均无改进或退步。§4.2 仅提供假设性解释（forward KL mode-covering "may dilute task-specific knowledge pathways"），无实验验证。若 "better masks" 仅在 PPL 和 commonsense tasks 上体现，"mask quality drives inference quality" 的 claim 实用意义受限。

**W4. Gradient coupling 因果解释不完整，缺少 per-layer KL 关键对照 [R1, R2 共识]**
§3.6 梯度分析停留在直觉描述。当前实验中 BCE/MSE/KL 同时变化 loss type × scope × signal source 三个维度，无法隔离 coupling 的独立效果。关键缺失实验：per-layer KL（每层独立优化该层 output 对 dense output 的 KL divergence），可固定 loss type + signal source 仅改变 scope，真正隔离 "coupling" 效果。论文已标注 "suggestive" 并以 C1 ablation 提供 mask quality 的因果证据，但 "gradient coupling discovers mask patterns" 等措辞仍有 overclaiming 之嫌。

### Should-Fix (Major)

**W5. MSE baseline 单 seed 掩盖高方差 [R1 主导，R2 强烈同意]**
Appendix G 承认 MSE with seed 123 仅达 5.1% sparsity (PPL=15,789)——完全失败。但 Table 2/4 中 MSE 均为 seed 42 单 seed 结果。一个方法 3 seed 中 1 个完全失败，用另一个 seed 代表该方法性能不够公正。应报告 3-seed（含失败 seed）或 2-seed + 明确排除说明。

**W6. Table 2 actual sparsity 不匹配 [R1 主导，R2 同意]**
KL 30% actual=28.5% vs TEAL 30% actual=29.3%，0.8pp 差异意味着 KL 保留更多神经元。正文提供了 matched comparison (14.5% at 28.5%)，但 Table 2 headline 仍在不同 actual sparsity 下比较。建议增加 TEAL at 28.5% 行或在 caption 中更显著标注。

**W7. Seed-to-seed mask Jaccard divergence 未报告 [R2 主导，R1 强烈同意]**
论文报告 KL-vs-magnitude mask divergence 46-68%，但未报告 KL seed A vs KL seed B 的 mask divergence。若 seed 间 divergence 也达 40-60%，则 46-68% 的数字不具 unique discriminative power。PPL stability (CV=0.6%) 不等于 mask-level consistency。

### Nice-to-Fix (Minor)

**W8. 14B scale 结果有限 [R1, R2 共识]** — Qwen-14B 仅 30% sparsity，GSM8K 大幅退步，Contribution 4 基础薄弱。

**W9. 训练数据同质性 [R1, R2 共识]** — WikiText-103 单域训练，C4 OOD cross-seed variance 增大 31× (CV 0.2%→6.3%)。

**W10. Abstract 信息密度过高 [R2]** — ~200 词塞入过多具体数字，模糊核心 message。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| C1 ablation 设计优秀 | ✅ S1 | ✅ S1 | **[AGREE]** |
| 消融全面，实验透彻 | ✅ S2 | ✅ S2 | **[AGREE]** |
| 无 wall-clock speedup | ✅ W1 Critical | ✅ W4 Minor | **[AGREE]** (严重程度有差异) |
| Downstream 不一致 | ✅ W2 Major | ✅ W2 Major | **[AGREE]** |
| Actual sparsity mismatch | ✅ W3 Major | ✅ agree | **[AGREE]** |
| MSE single-seed | ✅ W4 Major | ✅ agree | **[AGREE]** |
| Gradient coupling 缺形式化 | ✅ W5 Major | ✅ W3 Major | **[AGREE]** |
| Seed mask divergence 未报告 | ✅ agree | ✅ Q2 | **[AGREE]** |
| 14B limited | ✅ W6 Minor | ✅ agree | **[AGREE]** |
| Training data homogeneity | ✅ W7 Minor | ✅ W6 Minor | **[AGREE]** |

## Reviewer Divergence

| 问题 | R1 | R2 | 分歧 |
|------|----|----|------|
| **Novelty / MaskLLM** | Application differences 非 trivial，empirical contributions 可能 borderline conference | Novelty 不足 main conference，仅达 Findings bar | R1 更看重 execution quality 和 C1 方法论贡献; R2 更强调方法层面的增量性 |
| **Gradient coupling overclaiming** | "Suggestive" 标注 + C1 evidence 足够，不应归为 overclaiming | "Discovers" 等措辞暗示 emergent discovery，是 overclaiming | R1 认为 hedge 到位；R2 认为仍有误导性 |

---

## Questions

**Q1.** C1 s42 oracle 来自 "earlier training run"，s123/s456 使用 matched retrained oracles。统一 matched oracles 后 s42 gap 是否缩小？[R1]

**Q2.** Reverse KL predictor 的下游 metrics？若 mode-seeking 更好保留 knowledge pathways (MMLU)，可验证 W3 的假设性解释。[R1, R2 共识]

**Q3.** Table 2 缺 BCE 30% uniform 条目。Table 4 的 BCE 30% PPL=15.71 是否 uniform allocation？[R1]

**Q4.** MSE seed 123 失败是 Gumbel+Lagrangian 组合不稳定还是 MSE 固有缺陷？KL 有无类似 failure seed？[R1, R2 共识]

**Q5.** KL training cost 约 2.6× BCE，每个 sparsity target 需独立训练。是否可训练单个 predictor 支持多 sparsity levels？[R1, R2 共识]

**Q6.** KL seed A vs KL seed B 的 mask Jaccard divergence 是多少？作为 46-68% KL-vs-magnitude divergence 的 reference baseline。[R2, R1 agree]

---

## Missing References

- **Mixture-of-Channels (MoC)** (arXiv 2511.09323, Nov 2025) — SwiGLU native gating + Top-K channel selection，问题域高度重合 [R2]
- **"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering"** (arXiv 2507.14179, Jul 2025) — predictor network 的替代方案 [R2]
- D2DMoE (Szatkowski et al., 2024) 在 taxonomy 中命名但未实验覆盖 [R1, R2 partial agree]

---

## External Review (Stanford Agentic Reviewer)

**状态：pending** — 外部审稿请求已于 2026-05-21T01:18:43 UTC 发送，尚未返回。

---

## Visual Layout Check（非评分项）

**状态：error** — 视觉审查 Agent 因配额耗尽 (rate limit) 而失败，未能完成 PDF 渲染检查。用户可在配额重置后（2026-05-22 18:00 UTC）重新触发。

**R2 格式合规检查结果（替代）**: 页数 ✅ (8页正文)、模板 ✅ (ACL)、匿名 ✅、Limitations ✅、Ethics ✅、Checklist ✅、引用 ✅ (50条引用全部验证通过，1 orphan bib entry `de2024griffin` 未引用)。

---

## Overall Assessment

**Overall: 3.0 (Findings)** | R1: 3.5 (Borderline Conference) | R2: 3.0 (Findings)
**Confidence: 4/5**

本文是一篇执行质量较高的 empirical study，C1 target-swap ablation 有独立方法论价值，消融覆盖极其全面，结果报告诚实。然而存在四个核心短板：

1. **Novelty**: 核心 KL+Gumbel 训练配方与 MaskLLM 高度重合，区别仅在 application level。论文诚实地自定位为 empirical study，但 empirical insights（KL 优于 BCE for activation sparsity）的影响范围有限。

2. **Downstream inconsistency**: Knowledge-intensive tasks 跨三个模型系统性退步（MMLU −5.2pp, GSM8K −20pp at 14B），"quality improvement" claim 仅在 PPL + commonsense tasks 上成立，削弱了实用价值。

3. **因果解释不完整**: Gradient coupling 叙事缺少 per-layer KL 关键对照实验，无法隔离 coupling scope 的独立贡献。

4. **No speedup**: Pipeline 增加 6.4% overhead，无实际推理加速。

R1 (3.5) 和 R2 (3.0) 的 0.5 分差距主要源于 novelty 权重：R1 认为 C1 ablation 质量和消融覆盖面可能补偿方法论增量性；R2 认为一个 well-designed ablation 不能弥补核心 novelty 不足。综合两方观点，本文更适合 **Findings** 轨道——execution quality 达标，但 impact 和 novelty 不足以进入 main conference。

**升档路径 (→3.5 Borderline Conference)**:
- 补充 per-layer KL ablation，若结果支持 coupling hypothesis
- 提供 reverse KL 下游 metrics，验证 mode-covering 假设
- MSE 补 multi-seed 或明确排除说明
- 报告 cross-seed mask Jaccard distance

**降档风险 (→2.5 Borderline Findings)**:
- MaskLLM 策略直接迁移即可复现结果（Q1 from R2）
- Seed-level mask divergence 与 KL-vs-magnitude divergence 可比（invalidates §4.4 core finding）

---

## Detailed Comments

### Abstract
- 信息密度过高，建议精简具体数字，突出 1-2 个核心定量发现
- "coupled gradient discovers mask patterns" 措辞有 overclaiming 之嫌，建议改为 "output-distribution optimization yields different mask patterns"

### Introduction (§1)
- 开篇 efficiency 动机与 "primarily empirical study" 定位存在张力
- Contribution 4 ("preliminary analysis at 7-14B") 基础薄弱（仅 30% sparsity, GSM8K −20pp）

### Method (§3)
- §3.4 forward KL 论证清晰，引用充分
- §3.6 gradient analysis 标注 "suggestive" 是合适的 hedge，但 "coupling" 措辞在全文中仍被用作因果性表述
- §3.7 taxonomy 有组织价值但 MSE failure 的解释需要 per-layer KL 实验支持

### Experiments (§4)
- Table 2: 缺 BCE 30% uniform 条目；actual sparsity mismatch 需更显著标注
- Table 3 (C1): 设计精巧，是论文最强贡献。s42 oracle provenance 差异需澄清
- Table 4: 30%+50% 双列消融全面。但 MSE 仅 seed 42
- §4.4 mask divergence: 缺 cross-seed mask Jaccard 作为 reference baseline
- §4.6 allocation analysis: non-monotonic 发现有趣但 14B 数据不足

### Related Work (§2)
- MaskLLM 三点区分描述准确但需强调为 methodological 而非仅 application-level
- 缺 MoC (2511.09323) 和 Activation Pattern Clustering (2507.14179) 讨论
- Orphan bib entry: `de2024griffin` 未在正文引用

### Limitations
- 全面且诚实。训练数据同质性、PPL-downstream gap、scale 限制均已讨论

### Ethics
- 合规，无 concerns

### Format
- 8 页正文 ✅，ACL 模板 ✅，匿名 ✅，完整 checklist ✅