---
round: 17
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T08:40:23.457870+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 19 (Fresh)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
**审稿日期**: 2026-05-22
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验评估; R2: 新颖性+完整性+格式合规）

---

## Summary

本文用 forward KL divergence + Gumbel-Sigmoid 松弛替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器（75.9M 参数，&lt;1% base）。在 LLaMA-3.1-8B 30% 稀疏度下 PPL 优于 TEAL 14.5%（matched sparsity），发现的 mask pattern 与 magnitude-based 方法有 46-68% Jaccard 偏离。Target-swap ablation (C1) 证明 mask quality 是推理质量的近端驱动因素。Per-layer KL 控制实验将效果分解为 signal type（占 PPL gap 97.5%）和 coupling scope（贡献 downstream 3-9pp）。跨架构评估在 Mistral-7B PPL 泛化，Qwen-2.5-14B 出现 MMLU/GSM8K 下降。

---

## Strengths

**S1. 研究问题有价值** [共识]
BCE 将每个神经元独立处理的局限性是 contextual sparsity 文献中被忽视的问题。用 output-distribution objective 替代 per-neuron classification 是自然且有意义的研究方向。

**S2. 消融设计系统且精巧** [共识]
C1 target-swap ablation、per-layer KL decomposition、5 种 loss 变体对比（Table 4）、Gumbel vs STE 对比形成完整消融体系。实验控制严格：所有 baseline 使用相同架构/数据/优化器，仅改变损失函数（Appendix G）。

**S3. 训练效率优势明确** [R1]
KL 在 1000 steps（~45 min）达到的效果优于 BCE 2700 steps（~46 min），wall-clock 相当但 PPL 差距 2.4×（11.79 vs 28.13）。

**S4. Negative results 报告诚实** [共识]
14B MMLU/GSM8K 下降、global allocation 高 MMLU variance（σ=9.5pp）、50% downstream collapse 均被充分讨论。

**S5. 附录内容充实** [R1]
19 个附录覆盖 inference latency、bottleneck sensitivity、temperature schedule、training convergence、penalty controller dynamics、OOD evaluation 等，增强可复现性。

**S6. Related work 覆盖全面** [R2]
包含 2024-2026 年 activation sparsity 最新文献：R-Sparse、DIP、SparseInfer、MoC、SVD-CSP、Polar Sparsity、MoNE、D2D-MoE 等。

---

## Weaknesses

### Critical (Must-Fix)

**C1. 97.5% signal-type 归因与下游指标矛盾** [共识: R1-N1 Critical, R2 AGREE]
§4.5 和 Conclusion 声称 "signal type accounts for 97.5% of the PPL gap"，但同一节承认 per-layer KL（无 cross-layer coupling）在 commonsense tasks 上 underperform 3-5pp，BoolQ 差距 9.2pp。Coupling scope 对下游贡献远超 PPL 暗示的 2.5%。论文主叙事反复使用 97.5% 但未补充下游指标的定量 2D 分解，可能给读者 "coupling 不重要" 的错误印象。

**C2. C1 target-swap ablation 因果推断不足** [共识: R1-N2 + R2-W2, 互补关切]
两个叠加 confound 削弱 C1 的因果推断力：
- **循环论证** (R1): KL-derived masks 由 coupling 发现 → BCE 用这些 masks 也能达到类似 PPL → 结论 "mask quality > coupling"。但如果没有 KL 的 coupled gradients，这些高质量 masks 根本不存在。C1 证明的是 transferability，不是 "coupling 不重要"。
- **Soft-vs-hard confound** (R2): C1 同时改变 mask 表征（hard vs soft）和 target。BCE+Gumbel 排除仅排除了 softness 有利于 BCE 的可能，未排除 softness×KL-targets interaction。
论文在 Appendix P 承认 trajectory dependence，但 §4.4 主叙事对此 qualification 不够突出。

**C3. 无 wall-clock speedup，efficiency motivation 空洞** [共识: R1-N3 + R2-N2]
Table 5 实测 +6.4% overhead（126.78 vs 119.11 ms/forward）。Introduction 开篇以 "high contextual sparsity" 和 FFN 神经元冗余为动机暗示 efficiency gain，但全文无任何 speedup 结果。Triton block-sparse 在 Appendix A 提到但未实际测试。对于 sparsity 方法论文，motivation-contribution gap 过大。

**C4. 与 MaskLLM 新颖性区分** [分歧: R2 Critical, R1 REBUT → Should-Fix]
核心配方（frozen backbone + learnable masks + KL + Gumbel relaxation）与 MaskLLM (NeurIPS 2024) 高度重合。§2 的三点区分（sparsity type、mask generation、allocation）被 R2 判定为 application-level adaptation。R1 反驳：weight sparsity → activation sparsity 涉及 predictor network 泛化到 unseen inputs，非 trivial 迁移；核心贡献在分析框架（C1、2D decomposition）而非配方本身。R1 部分同意需更 sharp 的 MaskLLM 对比。
**Director 判定**: 新颖性确实有限——"KL 优于 BCE" 已被 MaskLLM 方法选择隐含验证。但分析贡献（target-swap ablation、signal type vs coupling scope 分解）有独立价值。此 issue 是 Findings vs Conference 的核心分界线。

### Major (Should-Fix)

**M1. 14B 实验覆盖不足 + GSM8K 严重退步** [共识: R1-W1, R2-W1]
Qwen-2.5-14B 仅有 30% sparsity 完整评估。GSM8K 从 dense 87.57% 降至 KL 32.1±5.2%（TEAL 52.1%），−20pp 且高 seed variance。Contribution 4（"preliminary cross-scale evaluation"）基础薄弱。缺 50% sparsity 14B 下游结果。Limitations 解释（"task-and-scale-dependent effects"）过于笼统。
（注: R1 声称 TEAL 14B GSM8K 未报告为事实性错误，Table 13 已含此数据。）

**M2. Knowledge-intensive 任务退步缺机制解释** [共识: R1-W2, R2 AGREE]
8B 30% MMLU −5.2pp, 14B GSM8K −20pp, 跨三个模型一致。Limitations 仅一句推测（"mass-covering property may preserve output breadth at the expense of reasoning-critical pathways"），未利用已有的 per-layer Jaccard divergence 框架与 task-specific 性能关联。

**M3. MSE 50% failed seed 报告不透明** [共识: R1-W3, R2 AGREE]
Table 4 50% MSE 仅报告 s42 (229.26)，Appendix G 提到 s123 failure（PPL=15,789, sparsity 仅 5.1%）但主文未标注。30% MSE 已更新为 3-seed（18.52±1.68），但 50% 的处理方式不一致。

### Minor (Nice-to-Fix)

**m1. "2D Taxonomy" / "Coupling Alignment Hierarchy" 术语** [分歧 severity: R2 Major → R1 Minor]
Table 1 仅 2×3 分类表，"hierarchy" 过于宏大。R1 认为 §4.5 的 2D 分解有实质分析价值，问题仅在术语。Director 判定: 术语需谦逊化（Minor），2D 分解本身有效。

**m2. Actual sparsity mismatch 主表不够显著** [共识: R1-W5, R2 AGREE]
KL 28.5% vs TEAL 29.3% at 30% target。主表仅 footnote 标注，abstract 14.5% 用 matched-sparsity 但未说明。

**m3. OOD variance 增大 (CV 0.2%→6.3%) 讨论不充分** [共识: R1-W4]

**m4. 30% sparsity sweet spot 限制实际影响** [共识: R2-W4, R1 AGREE]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识：

| Issue | R1 | R2 | Status |
|-------|----|----|--------|
| 97.5% 归因 vs 下游矛盾 | Critical | AGREE | **共识** |
| C1 因果推断不足 | Critical (circularity) | Major (confound) | **共识 (互补)** |
| 无 wall-clock speedup | Critical | Critical | **共识** |
| 14B 实验不足 | Major | Major | **共识** |
| Knowledge-intensive 退步缺解释 | Major | AGREE | **共识** |
| MSE failed seed 透明度 | Major | AGREE | **共识** |
| Sparsity mismatch 显示 | Minor | AGREE | **共识** |
| OOD variance 讨论 | Minor | AGREE | **共识** |
| Checklist 格式违规 | AGREE | 提出者 | **共识** |

## Reviewer Divergence

| Issue | R1 | R2 | Director 判定 |
|-------|----|----|--------------|
| MaskLLM novelty 严重性 | REBUT (Should-Fix): 贡献在分析框架 | Critical: 配方重合 | 分歧记录。是 Findings/Conference 分界线 |
| Taxonomy overclaim 级别 | Minor: 2D 分解有实质价值 | Major: 仅分类表 | 术语 Minor, 分解有效 |
| "redundant" 措辞误导 | REBUT: 有实验支撑 | Minor: 可能误导 | Minor |

---

## Questions for Authors

1. 能否提供下游指标（ARC-c, WG, MMLU, BoolQ）的定量 2D 分解（signal type vs coupling scope 的 % 贡献），而非仅 raw gap？
2. 是否有证据表明其他方法（evolutionary search、gradient-free optimization）能发现与 KL 类似质量的 masks？这将澄清 coupling 是 mask discovery 的必要条件还是充分条件。
3. C1 中 BCE 训练是否也使用了 Gumbel-Sigmoid？如果仅用 hard threshold，则 C1 vs KL 的差异可能部分来自 relaxation method。
4. 14B GSM8K −20pp 且 σ=5.2pp：是否分析过哪些层的 masks 在不同 seeds 间差异最大？
5. Per-layer KL 的 train-inference distribution shift（训练时 mask 1 层，推理时 mask 32 层）是否可通过 mask-K-layers curriculum 控制？
6. 是否测试过多样化训练数据（C4 子集、code）对 MMLU 等 knowledge-intensive downstream 的影响？

---

## Missing References

- **PowerInfer-2** (Xue et al., 2024): on-device sparsity work [R1 提出, R2 AGREE]
- **AWQ** (Lin et al., 2024, MLSys): activation-aware channel selection 与本文 importance scoring 有方法论联系 [R2 提出, R1 AGREE]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置未开启 paperreview_ai）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 因 API 限额错误未完成（status: done with error: "You've hit your limit · resets 6pm (UTC)"）。无排版审查结果。完成后会自动补发到 Group C。

---

## Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5**

| 维度 | 分数 |
|------|------|
| Soundness | 3/5 |
| Excitement | 2.5/5 |
| Reproducibility | 4/5 |

### 评分理由

**达到 Findings bar 的因素：**
- 研究问题有价值且明确（BCE 独立性 → KL coupled optimization）
- 消融设计系统：C1 target-swap、per-layer KL decomposition、5 种 loss 对比
- 3-seed 评估、严格控制变量、充实附录，可复现性强
- Signal type vs coupling scope 的 2D 分解是有用的分析框架
- Negative results（14B regression、downstream collapse at 50%）诚实报告

**阻碍 Conference 接收的因素：**
1. **核心配方新颖性有限**: KL + Gumbel for mask optimization 已被 MaskLLM 建立。论文的贡献在分析框架而非方法创新，但分析叙事本身有关键缺口（97.5% 归因矛盾、C1 循环论证）。
2. **分析叙事断裂**: 97.5% signal-type 归因是论文最吸引人的 claim，但仅基于 PPL，与下游指标矛盾（coupling scope 贡献 3-9pp）。C1 的因果推断因循环论证和 soft-vs-hard confound 而不足。这两个缺口使论文无法清晰回答 "what specifically does KL contribute"。
3. **实用价值未验证**: +6.4% overhead，无任何 speedup 数据。30% 是唯一可用 regime，40%+ 下游崩溃。Motivation-contribution gap 过大。
4. **Scale 泛化存疑**: 14B GSM8K −20pp（σ=5.2pp）暗示方法可能有 scale limitation，但缺乏分析。

**推荐**: Findings 接收。实证贡献（KL 系统性优于 BCE for sparsity prediction training, 2D decomposition 框架）有发表价值。但需修正 97.5% 归因叙事（补充下游定量分解）、澄清 C1 的因果推断边界（明确标注循环性）、删除 PDF 中的 Checklist section（格式违规）。

---

## Detailed Comments

### §1 Introduction
- 第一段以 efficiency 为动机但全文无 speedup——考虑将 opening motivation 调整为 "understanding how training objective shapes sparsity prediction quality"，与 p.8 ("This paper is primarily an empirical study...") 一致。
- Contribution 1 ("coupling alignment hierarchy") 用 "hierarchy" 过于宏大，建议 "ranking" 或 "ordering"。
- Contribution 4 ("preliminary cross-scale evaluation") 过于薄弱，考虑降级或与 Contribution 1 合并为附加证据。

### §3.6 Gradient Analysis
- "suggestive" 标注恰当，但 §4.5 的 97.5% 归因暗示了更强的因果关系，两者 tension 需解决。

### §3.7 Two-Dimensional Taxonomy
- Table 1 作为分类工具有用，但作为 contribution 被高估。建议在 Contribution list 中降级。

### §4.4 Target-Swap Ablation (C1)
- 需在主叙事中更突出讨论：(a) 循环性——KL coupling 是发现高质量 masks 的必要条件；(b) soft-vs-hard confound 未完全排除。当前 qualification 在 Appendix P，对主文读者不够可见。

### §4.5 Per-Layer KL Decomposition
- 97.5% 数字需限定为 "PPL-level attribution"，并补充下游指标的定量分解。
- 承认的 train-inference distribution shift confound 需要更多讨论——训练时 mask 1 层 vs 推理时 mask 32 层的 gap 可能系统性低估了 coupling scope 的贡献。

### §4.6 Cross-Architecture and Scale
- 14B 结果需更具体的失败模式分析，尤其 GSM8K 高 seed variance 的来源。TEAL 在 14B GSM8K 为 52.1%，KL 为 32.1±5.2%——这不仅是 "scale-dependent effect"，可能是 KL 的 mode-covering 特性在高容量模型上反而有害的证据。

### Table 2
- Caption footnote 密度过高，建议将 actual sparsity 移入主表单独列。
- MSE 50% (229.26) 应标注 "s42 only; s123 failure (PPL=15,789, sparsity 5.1%)"。

### Table 4
- 标注 30% MSE 为 3-seed, 50% MSE 为 s42 only with footnote about s123 catastrophic failure。

### Limitations
- "Scaling to 70B remains untested" 应说明原因（计算资源 vs 方法论障碍）。
- 训练数据同质性的讨论可更深入——C4 OOD variance 增大 31× 暗示 predictor 对 domain 敏感。

### Ethics Statement
- 合理且完整。

### Format
- **必须删除** PDF 中的 "Responsible NLP Research Checklist" section（A1-E1 条目）。根据 EMNLP 2026/ARR 规定，该 checklist 仅在 OpenReview submission form 中填写，不出现在论文 PDF 中。