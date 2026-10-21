---
round: 18
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T09:49:45.906420+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

**目标 Venue**: EMNLP 2026 (Long Paper, ARR May cycle)
**截止日期**: 2026-05-25
**审稿轮次**: Round 20 (fresh)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work）
**评分共识**: 两位 Reviewer 均给出 Overall 3.0 (Findings)

---

## Summary

本文提出用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor（<1% base params），使用 Gumbel-Sigmoid relaxation + frozen weights 框架。在 LLaMA-3.1-8B 30% sparsity 下 PPL 降低 14.5%（matched sparsity），通过 target-swap ablation (C1) 和 per-layer KL control 将改进分解为 signal type（98% PPL gap）和 coupling scope（24–35% downstream）两个维度。跨架构在 Mistral-7B 和 Qwen-14B 上验证 PPL generalization。论文自我定位为 "primarily an empirical study"。

---

## Strengths

**S1. 系统性的 5-way loss comparison。** 涵盖 Forward KL / Reverse KL / JSD / BCE / MSE 五种 loss 配置，配合 Gumbel/STE relaxation 交叉消融（Table 4），构成该方向目前最全面的实证对比。[R1, R2 共识]

**S2. C1 target-swap ablation 设计有新意。** 将 KL-derived masks 喂给 BCE 训练以解耦 "mask quality" 与 "gradient coupling"，比简单的 loss comparison 更有深度。尽管存在 confound（见 W3），设计思路值得肯定。[R1, R2 共识]

**S3. 诚实的自我定位和 limitation 报告。** 明确声明 "we do not propose a new architecture or algorithm"（§1），坦率承认知识密集型退步、无加速、OOD variance、MSE seed failure。这种透明度在投稿中少见。[R1, R2 共识]

**S4. Compensation redundancy 有实际价值。** 证明 KL predictor 无需 FastForward 式 +67.2M compensation network，简化 inference pipeline。[R2]

**S5. Related Work 覆盖全面。** 覆盖 training-free methods、predictor-based methods、activation engineering、MoE routing、weight pruning 等主要方向，MaskLLM 三点详细对比。引用量和质量均上乘（8/10）。[R2]

**S6. 详尽附录，可重现性高。** 18 页中 ~10 页附录，涵盖 bottleneck sensitivity、temperature schedule、training convergence、penalty dynamics、OOD evaluation、mask visualization 等。[R1]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [Critical, 共识]** **无实际 wall-clock 加速，反增 6.4% 延迟**
- 位置：Appendix A (Table 5), §1 para 5, §5
- 论文动机围绕 "potential inference acceleration"（§1 para 1），但 Table 5 显示 +6.4% latency（126.78 vs 119.11 ms/fwd）。论文承认 "unstructured element-wise masks do not translate to wall-clock speedup"（Appendix A）。当前结果是净减速。
- 影响：一篇 sparsity prediction 论文如果无法展示任何加速效果，其实际贡献局限于 analytical insights。同期工作已实现实际加速（如 Polar Sparsity 2.2× speedup，尽管 R1 指出 sparsity 类型不同不可直接对比）。
- [R1-N1 Critical + R2-N2 Critical, 完全共识]

**N2 [Critical, 共识]** **MMLU/GSM8K 在所有 scale 上系统性退步，未解释**
- 位置：Table 2, Table 13 (Appendix K), Table 17 (Appendix L), §4.2, Limitations
- KL 在 commonsense（ARC-c, WG, HS, PIQA：4/4 wins at 30%）上一致优于 TEAL，但在 knowledge-intensive（MMLU, GSM8K）上一致劣于 TEAL——跨三个架构：8B MMLU -5.2pp; 14B MMLU -8.1pp (global), GSM8K -20pp (σ=5.2pp); Mistral GSM8K -7.3pp。论文仅给出假设性解释（§4.2: "mode-covering may dilute task-specific knowledge pathways"），自标 "hypothesis; mechanistic investigation left to future work"。
- 影响：这不是 edge case，而是一整类核心任务的系统性退步。如果 KL 在 MMLU/GSM8K 上一致劣于零训练成本的 TEAL，用户为什么要付出训练代价？R2 进一步指出：如果 "coupling alignment is the dominant design dimension"，为什么 knowledge tasks 反而更差？存在 claim-evidence mismatch。
- [R1-N2 Critical + R2-N3 Critical, 完全共识]

**N3 [Critical, Director 升级]** **"Coupling alignment" 核心术语 conflates signal type 和 coupling mechanism；98% 归因方法论不严谨**
- 位置：Abstract line 5, §1 Contributions, §4.5, §5 Conclusion
- Per-layer KL（无 cross-layer coupling 但有 output-distribution signal）达到 E2E KL 98% 的 PPL 效果（9.05 vs 8.81, Table 4）→ cross-layer coupling 仅贡献 2.5% PPL gap。但论文用 "coupling alignment" 作核心术语（Conclusion: "Coupling alignment—optimizing through the output distribution—is the dominant design dimension"），暗示 cross-layer coupling 是关键——这与 per-layer KL 数据矛盾。实际驱动力是 signal type（output distribution vs intermediate activations），而非 inter-layer gradient coupling。
- 98% 分解假设 signal type 和 coupling scope 正交（无交互效应），但从 MSE→KL 同时改变了 (a) loss target, (b) gradient flow topology, (c) optimization landscape（论文脚注 §4.5 自己承认）。98% 应标注为 upper bound estimate 而非 point estimate，但正文在 Abstract/Contributions/Conclusion 中反复引用。
- [R1-W2 Major + R2-W2 Major, 完全共识; Director 因对核心 narrative 的全局影响升级为 Critical]

### Should-Fix（影响评分但不一票否决）

**W1 [Major, 共识]** **Per-layer KL 训练-推理不匹配混淆了 2D 分解的因果推断**
- 位置：§4.5, Table 4
- Per-layer KL 训练时每步仅 mask 1/32 层，推理时 32 层同时 mask。30% downstream 差距（"coupling scope 24–35%"）可能大部分来自 train-inference mismatch 而非缺乏 cross-layer coupling。50% 时 per-layer KL 退化到 34.85（vs E2E 11.92, 3× gap），更可能是 mismatch catastrophe 而非 "coupling transitions from optional to essential"（§4.5）。
- 论文在 §4.5 末尾仅一句 caveat，但 "coupling scope 24–35%" 在 Abstract/Conclusion 反复出现。需 gradual K (1→4→16→32 layers/step) 实验才能区分 coupling effect 和 mismatch effect。
- [R1-W1 Major, R2 agrees 且称"R1 最有洞察力的观察"]

**W2 [Major, 分歧]** **与 MaskLLM (NeurIPS 2024) 核心配方高度重叠**
- 位置：§2 (Related Work), §1 Contributions
- 核心配方（frozen weights + learnable masks + forward KL + Gumbel relaxation）与 MaskLLM 一致。三点区分（sparsity type / mask generation / allocation）中，R2 认为均为 application-level 差异；R1 认为 predictor network（函数逼近 vs 参数优化）和 global top-k allocation（跨层依赖）是非平凡技术差异，但同意方法新颖性有限。
- 在 "primarily empirical study" 定位下，贡献主要依赖 analysis framework（C1 ablation + 2D decomposition），但这些 insights 受上述 confounds 影响，surprise factor 有限。
- [R2-N1 Critical; R1 部分 REBUT; Director 判定: Warning — recipe overlap 真实存在，但 predictor+global allocation 有技术差异]

**W3 [Major→Warning, 共识]** **C1 target-swap ablation 存在 trajectory confound**
- 位置：Table 3, footnote †, Appendix P
- (a) s42 oracle 来自 "earlier training run"（PPL gap 0.65pp vs retrained ≤0.02pp）；(b) oracle masks 编码特定 KL 训练轨迹；(c) 50% 仅 s42 单 seed。§4.3 用 "confirms" 三次但应降为 "suggestive evidence"。Retrained s123/s456 一致性（≤0.02pp）部分缓解但不消除 confound。
- [R1-W4 Major + R2-W1 Major, 共识]

**W4 [Warning]** **WikiText 同分布评估 + C4 OOD seed 覆盖不足**
- WikiText-103 训练 → WikiText-2 评估本质同分布。C4 OOD 提供初步验证（Table 10-11, downstream Δ≤1.1pp），但 30% OOD 仅 2-seed (global)，downstream robustness 仅 seed 42。
- [R1-W3 Major; R2 REBUT severity→minor; Director 判定: Warning]

**W5 [Warning]** **MSE 50% 实质 single-seed (s123 catastrophic failure)**
- Table 4 MSE 50% = 229.26 仅 s42。Appendix G 提及 s123 failure (PPL=15789, 5.1% sparsity) 但主文未标注。MSE instability 本身加强 KL>MSE 论点，但 baseline 的有效性受限。
- [R1-W5 Minor + R2 agrees]

### Minor

**W6 [Info]** Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在 downstream 对比未控制 [R1-W6, R2 agrees]
**W7 [Info]** 30% sparsity sweet spot 实用价值有限（MMLU -24.6pp, GSM8K -41pp vs dense）[R2-W3, R1 部分 REBUT Polar Sparsity 对比]
**W8 [Info]** 术语过度创造（"coupling alignment ranking" = loss function comparison）[R2-W4, R1 agrees]
**W9 [Info]** Batched inference 对 contextual sparsity 的影响完全未讨论 [R2-W5, R1 agrees]
**W10 [Info]** Abstract "universally use BCE" 不准确（ShadowLLM 用 MSE）[R2, R1 agrees]

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：
1. **无实际加速** (R1-N1 = R2-N2, both Critical)
2. **知识密集型任务系统性退步未解释** (R1-N2 = R2-N3, both Critical)
3. **"Coupling alignment" 术语混淆 + 98% 归因不严谨** (R1-W2 = R2-W2, both Major)
4. **Per-layer KL train-inference mismatch** (R1-W1, R2 fully agrees)
5. **C1 ablation trajectory confound** (R1-W4 ≈ R2-W1, both Major)
6. **MSE 50% single-seed** (R1-W5, R2 agrees)
7. **术语过度创造** (R2-W4, R1 agrees)
8. **Batched inference 未讨论** (R2-W5, R1 agrees)

---

## Reviewer Divergence

**D1. MaskLLM 新颖性程度**
- R2: "完全一致"，三点区分均 application-level (Critical)
- R1: predictor network 和 global allocation 是非平凡差异，但同意方法新颖性有限 (REBUT)
- Director 判定：recipe-level overlap 真实存在。R1 的技术差异论证有道理（predictor 需泛化到 unseen inputs，global allocation 创造跨层依赖），但不足以构成 strong methodological novelty。在 empirical study 定位下，analysis framework 的贡献需要足够 surprising 的 insights 支撑——而当前 insights 受 confounds 影响。

**D2. 30% sparsity ceiling 对比 Polar Sparsity**
- R2: 对比 Polar Sparsity 50% <1% drop (Major)
- R1: 不同 sparsity 类型（attention head vs FFN neuron）不可直接对比 (REBUT)
- Director 判定：R1 的 REBUT 有技术依据。但 practical utility 问题成立：30% FFN sparsity + 无加速 = 部署价值有限。

**D3. WikiText 同分布严重性**
- R1: Major（本质同分布）
- R2: Minor（C4 OOD + downstream robustness 部分缓解）
- Director 判定：Warning。同分布主表是合理批评，但 C4 data (Table 10-11) 提供了初步 OOD 验证。

---

## Questions（需要作者在 rebuttal 中回答）

**Q1.** [关键] Per-layer KL 的 downstream 原始数值（ARC-c, WG, MMLU, GSM8K, HS, PIQA）是多少？目前仅有 coupling scope 百分比但无法 verify。

**Q2.** [关键] Per-layer KL 训练时如果 mask K>1 层/步（如 K=2, 4, 8, 16, 32），性能如何变化？这能直接区分 coupling effect 和 train-inference mismatch effect。

**Q3.** [关键] 如果将论文核心术语从 "coupling alignment" 改为 "output-distribution alignment"，核心 claims 是否仍然成立？这一修改是否能更准确地反映 per-layer KL 数据？

**Q4.** MMLU/GSM8K 退化是否与特定层的 mask divergence 相关？Per-layer Jaccard divergence（Figure 7, Appendix M）能否与 per-task performance 关联？

**Q5.** MaskLLM 在 activation sparsity 场景下的表现如何？如果将 MaskLLM 的 direct-parameter mask 方案适配到 activation sparsity，KL 优势是否仍成立？

**Q6.** C1 ablation 50% sparsity 是否能补充 s123/s456 结果？s42 oracle 来自 earlier run 的 0.65pp gap 是否说明结论对 oracle provenance 敏感？

**Q7.** 是否尝试过 KL 蒸馏温度 $T>1$？标准知识蒸馏中 $T=2$–$4$ 通常优于 $T=1$。

**Q8.** 更多样化的训练数据（C4 或 RedPajama 子集替代 WikiText-103）是否能缓解 MMLU regression？

---

## Missing References

Related Work 覆盖全面（R2 评估 8/10）。可考虑补充（均非 critical）：
- LazyLLM (Fu et al., 2024) — token-level dynamic pruning for attention + FFN
- COTS (Zhang et al., 2025, arXiv:2511.09822) — multi-channel sparse FFN exploitation
- LLM in a Flash (Alizadeh et al., 2024) — flash memory 上的 sparse inference 部署
- Outlier Suppression+ (Wei et al., 2023) — activation outlier 对 sparsity 的影响

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 因额度限制报错退出（`agent_error: You've hit your limit · resets 6pm UTC`）。未产生有效的排版审查结果。用户可在额度恢复后重新触发。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

**评分理由**：

论文是一项扎实的实证研究，5-way loss comparison 和 C1 target-swap ablation 是主要亮点，Related Work 全面，limitation 报告诚实。这些品质使论文达到 Findings 水平。

但三个 Critical 问题阻止 Main conference 接收：

1. **无实际加速**（+6.4% overhead）：一篇 sparsity prediction 论文无法展示任何推理加速，实际贡献局限于 analytical insights。论文需要在 Triton block-sparse POC 或完全 reframe 为纯分析论文之间做出选择。

2. **知识密集型任务系统性退步未解释**：MMLU/GSM8K 跨三个架构一致劣于零训练成本的 TEAL，且仅有未验证假说。这直接动摇了 method 的实用价值和 "coupling alignment is dominant" 的核心 claim。

3. **核心 framing 存在问题**："coupling alignment" 术语暗示 cross-layer coupling 是关键，但 per-layer KL 数据显示 signal type（output distribution vs intermediate）才是 PPL 的主要驱动力（98% gap）。加之 per-layer KL 的 train-inference mismatch confound，coupling scope 的 downstream 贡献（24–35%）的可靠性也受到质疑。98% 归因是 confounded estimate 而非 clean causal decomposition。

**提升至 3.5 (Borderline Conference) 的条件**：
- 在 rebuttal 中提供 Q2（gradual K 实验）的结果，量化 train-inference mismatch vs coupling effect
- 将核心术语从 "coupling alignment" 修正为 "output-distribution alignment"
- 提供 MMLU regression 的初步机制解释（如 per-layer divergence 与 task performance 关联分析）
- §1 完全去除 efficiency/acceleration 动机

**提升至 4.0 (Conference) 的额外条件**：
- 展示至少一个 sparsity level 的 wall-clock speedup POC
- MaskLLM 在 activation sparsity 上的 baseline 对比

---

## Detailed Comments

### §1 Introduction
- Para 1 "potential inference acceleration" 仍以 efficiency 为动机，与 Table 5 (+6.4% overhead) 矛盾。应 reframe 为 understanding training objective design space for sparsity prediction。
- "coupling alignment ranking" (Contributions item 1) 术语需修正为更准确的表述。

### §3 Method
- §3.4 forward vs reverse KL 论证（mode-covering for sparsity prediction）直觉合理，但 §4.5 reverse KL 30% 3-seed 结果显示 reverse KL 在 commonsense 上也优于 TEAL，部分削弱 "missing critical neurons" 论证。
- §3.6 梯度分析自标 "suggestive"（合理），但正文引用时偶尔暗示更强因果关系，需统一用语。

### §4 Experiments
- Table 2: actual sparsity 差异（KL 28.5% vs TEAL 29.3%）应在表格内更显著标注，而非仅 footnote。
- §4.2 Task-Type Split: "hypothesis; mechanistic investigation left to future work" 的坦率值得肯定，但这个 future work 对于支撑核心 claim 至关重要。
- §4.4 C1 ablation: "confirms" 应改为 "suggests" 或 "provides evidence consistent with"（出现 3 次）。
- §4.5 Per-layer KL: 
  - "coupling scope contributes 24–35%" 的 claim 需标注 train-inference mismatch caveat（当前仅在段末一句）。
  - "signal type accounts for 98%" 需标注为 upper bound estimate。
  - Per-layer KL downstream 原始数值应以表格形式呈现，而非仅在文字中给出百分比。

### §5 Conclusion
- "Coupling alignment—optimizing through the output distribution—is the dominant design dimension" 建议修正为 "Output-distribution alignment—optimizing through the model's final prediction—is the dominant design dimension for PPL; cross-layer coupling provides additional downstream benefits whose magnitude requires further investigation."

### Limitations
- 应补充 batched inference 讨论。
- 应更显著讨论 knowledge-intensive regression 的 scale-dependent 趋势（8B: -5.2pp MMLU → 14B: -8.1pp MMLU）。

### Appendix
- MSE s123 50% catastrophic failure (PPL=15,789) 应在主文 §4.5 更显著提及。
- Per-layer KL downstream 原始数值应出现在某个附录表格中。